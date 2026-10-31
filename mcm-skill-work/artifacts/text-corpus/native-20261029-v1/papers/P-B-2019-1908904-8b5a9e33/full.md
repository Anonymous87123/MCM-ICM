# P-B-2019-1908904-8b5a9e33

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
1908904

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

<!-- b000012 | title | pages [1] -->
B

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | title | pages [1] -->
2019

<!-- b000016 | prose | pages [1] -->
MCM/ICM

<!-- b000017 | heading | pages [1] -->
Summary Sheet

<!-- b000018 | title | pages [1] -->
Arrangement for DroneGo

<!-- b000019 | heading | pages [1] -->
Summary

<!-- b000020 | prose | pages [1] -->
After the worst hurricane to ever hit Puerto Rico, lots of people were injured. Highways and roads were blocked and damaged by the ﬂood. We establish a model to both meet the needs of medicine delivery and road reconnaissance with rotor wing drones.

<!-- b000021 | prose | pages [1] -->
Our model takes into account the following factors: the number of cargo containers, the type and the number of drones, the number of medicines, the associated packing conﬁguration for each cargo container, the exact lo- cations of cargo containers, and the schedule for each drone. Before estab- lishing the model, we develop necessary assumptions and essential nota- tions to make a reliable scenario.

<!-- b000022 | prose | pages [1] -->
After analyzing the locations of hospitals and ﬂight distance of drones, we decide to set three containers because of the long distance among hos- pitals. Then, we quantify the associated packing conﬁguration quality by the following three aspects: the minimum time to complete medical sup- ply delivery, the amount of medical supply, and the reconnaissance ability. We use AHP Algorithm and the normalization method to determine the weights of these three factors and evaluate the Comprehensive Evaluation (CE) value. Then we use the greedy algorithm to get the best-associated packing conﬁguration with the highest CE value under the ideal condition.

<!-- b000023 | prose | pages [1] -->
After that, we choose the approximate optimal positions for all cargo containers by image analysis to determine the optimate associated packing conﬁguration in reality (using Bisection). We process the map of roads and populated places into pixels. Then, we can determine the exact location of containers by counting the occupied pixels of roads and populated places.

<!-- b000024 | prose | pages [1] -->
We provide the schedule plan for each drone. Then, we test our model and provide the evidence to show the stability and reliability of the work. In the end, we analyze the strengths and weakness of the model and conclude the result in our report.

<!-- b000025 | keywords | pages [1] -->
Keywords: Drone, Route Planning, 3D Bin-Packing, AHP

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
Introduction· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000028 | contents | pages [2] -->
1

<!-- b000029 | contents | pages [2] -->
1

<!-- b000030 | contents | pages [2] -->
1.1 Background · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000031 | contents | pages [2] -->
1

<!-- b000032 | contents | pages [2] -->
1.2 Our work · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000033 | contents | pages [2] -->
1

<!-- b000034 | contents | pages [2] -->
Assumption · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000035 | contents | pages [2] -->
2

<!-- b000036 | contents | pages [2] -->
2

<!-- b000037 | contents | pages [2] -->
Notations · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000038 | contents | pages [2] -->
3

<!-- b000039 | contents | pages [2] -->
3

<!-- b000040 | contents | pages [2] -->
Speciﬁc formulation of problem · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
4

<!-- b000043 | contents | pages [2] -->
AHP Model · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000044 | contents | pages [2] -->
5

<!-- b000045 | contents | pages [2] -->
5

<!-- b000046 | contents | pages [2] -->
5.1 Establish an AHP Model · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000047 | contents | pages [2] -->
5

<!-- b000048 | contents | pages [2] -->
5.2 The Reason why We Choose These Three Aspects · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000049 | contents | pages [2] -->
5

<!-- b000050 | contents | pages [2] -->
5.3 Weights of the Three Aspects · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000051 | contents | pages [2] -->
6

<!-- b000052 | contents | pages [2] -->
5.4 Normalization · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000053 | contents | pages [2] -->
6

<!-- b000054 | contents | pages [2] -->
5.4.1 Amount of medical supply · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000055 | contents | pages [2] -->
6

<!-- b000056 | contents | pages [2] -->
5.4.2 Minimum time to complete medical supply delivery · · · · · · · · · · · · · · · ·

<!-- b000057 | contents | pages [2] -->
7

<!-- b000058 | contents | pages [2] -->
5.4.3 Reconnaissance ability · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000059 | contents | pages [2] -->
8

<!-- b000060 | contents | pages [2] -->
Packing Model · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000061 | contents | pages [2] -->
6

<!-- b000062 | contents | pages [2] -->
8

<!-- b000063 | contents | pages [2] -->
6.1 Design Packing Conﬁguration with Greedy Algorithm · · · · · · · · · · · · · · · · · ·

<!-- b000064 | contents | pages [2] -->
8

<!-- b000065 | contents | pages [2] -->
6.2 Roughly Find the Positions for the Cargo Containers· · · · · · · · · · · · · · · · · · · ·

<!-- b000066 | contents | pages [2] -->
9

<!-- b000067 | contents | pages [2] -->
6.3 Packing model in reality · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000068 | contents | pages [2] -->
12

<!-- b000069 | contents | pages [2] -->
6.4 3D Bin-packing · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000070 | contents | pages [2] -->
12

<!-- b000071 | contents | pages [2] -->
Accurate Locations · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000072 | contents | pages [2] -->
7

<!-- b000073 | contents | pages [2] -->
13

<!-- b000074 | contents | pages [2] -->
Timetable of Flights· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000075 | contents | pages [2] -->
8

<!-- b000076 | contents | pages [2] -->
14

<!-- b000077 | contents | pages [2] -->
Sensitivity Evaluation of the Model· · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000078 | contents | pages [2] -->
9

<!-- b000079 | contents | pages [2] -->
17

<!-- b000080 | contents | pages [2] -->
9.1 Sensitivity of the max distance reduction rate for drones · · · · · · · · · · · · · · · · ·

<!-- b000081 | contents | pages [2] -->
17

<!-- b000082 | contents | pages [2] -->
9.2 Sensitivity of the weight in AHP · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000083 | contents | pages [2] -->
17

<!-- b000084 | contents | pages [3] -->
Strengths and weaknesses · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000085 | contents | pages [3] -->
10

<!-- b000086 | contents | pages [3] -->
18

<!-- b000087 | contents | pages [3] -->
10.1 Strengths · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000088 | contents | pages [3] -->
18

<!-- b000089 | contents | pages [3] -->
10.2 Weakness · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000090 | contents | pages [3] -->
19

<!-- b000091 | contents | pages [3] -->
Conclusions · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000092 | contents | pages [3] -->
11

<!-- b000093 | contents | pages [3] -->
19

<!-- b000094 | contents | pages [3] -->
Memo · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000095 | contents | pages [3] -->
20

<!-- b000096 | contents | pages [3] -->
References · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000097 | contents | pages [3] -->
22

<!-- b000098 | contents | pages [3] -->
Appendices · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000099 | contents | pages [3] -->
A

<!-- b000100 | contents | pages [3] -->
23

<!-- b000101 | contents | pages [3] -->
A.1 Greedy Algorithm· · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000102 | contents | pages [3] -->
23

<!-- b000103 | contents | pages [3] -->
A.2 Binary Search with 3D bin-packing API · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000104 | contents | pages [3] -->
24

<!-- b000105 | contents | pages [3] -->
A.3 Image Generating · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000106 | contents | pages [3] -->
26

<!-- b000107 | contents | pages [3] -->
A.4 Image Processing and Optimal Position · · · · · · · · · · · · · · · · · · · · · · · · · · · · ·

<!-- b000108 | contents | pages [3] -->
28

<!-- b000109 | furniture | pages [4] -->
Team # 1908904

<!-- b000110 | furniture | pages [4] -->
Page 1 of 30

<!-- b000111 | contents | pages [4] -->
1

<!-- b000112 | heading | pages [4] -->
Introduction

<!-- b000113 | prose | pages [4] -->
1.1

<!-- b000114 | heading | pages [4] -->
Background

<!-- b000115 | prose | pages [4] -->
Hurricane is a powerful tropical cyclone in the Atlantic and North Paciﬁc with winds of more than 54.7 meters per second. A single ferocious hurricane can wreak havoc on a country. In 2017, a hurricane hit the United States territory of Puerto Rico, causing extensive property damage and up to 2,900 casualties. Storm surges destroyed coastal infrastructure, and hurricane-force rain damaged the most of the island’s electricity transmission lines. Widespread ﬂooding has blocked and damaged many highways and roads across the island.

<!-- b000116 | prose | pages [4] -->
With the progress of science and technology, in the reconstruction, we can use drones to transport medical supplies to increase the hospital’s medicines re- serves, use drones to detect road conditions, and to make preparations for fur- ther reconstruction in disaster areas. The rotor wing drone has the advantages of simple structure, strong maintainability and no casualties. It can be widely used in aerial photography, environmental detection and other ﬁelds, and has a huge industrial prospect [1]. Hence, rotor wing drones can be excellent at transporting cargo and reconnaissance.

<!-- b000117 | prose | pages [4] -->
1.2 Our work

<!-- b000118 | prose | pages [4] -->
However, in the scenario of using drones to deliver medicine and to detect road conditions, different drones have different sizes, functions, deadweight, ﬂight speeds and maximum ﬂight times. There are also different speciﬁcations for different types of medicines and Drone Cargo Bay, which all have to meet the carrying capacity of containers.

<!-- b000119 | prose | pages [4] -->
To best meet the needs of the medicines transportation and the road reconnais- sance, we need to establish a reasonable model to make rational use of all aspects of resources and achieve the optimization of resource allocation.

<!-- b000120 | prose | pages [4] -->
However, how should we deﬁne the "good" of our model? To answer this ques- tion, our group deﬁned the model as

<!-- b000121 | prose | pages [4] -->
• long days for medicines maintenance

<!-- b000122 | prose | pages [4] -->
• wide range of reconnaissance road

<!-- b000123 | prose | pages [4] -->
• short time for medicines delivery and reconnaissance mission.

<!-- b000124 | furniture | pages [5] -->
Team # 1908904

<!-- b000125 | furniture | pages [5] -->
Page 2 of 30

<!-- b000126 | prose | pages [5] -->
2

<!-- b000127 | heading | pages [5] -->
Assumption

<!-- b000128 | prose | pages [5] -->
• The max distances the drones can reach are only related to their load conditions and their types. That means we ignore the wind or other unsure factors. We initially assume that the max distance will reduce to 80% when drones are carrying goods.

<!-- b000129 | prose | pages [5] -->
• The drones can be cycle used (by charging to use next time). For a drone is not very cheap and DroneGo is a Non-Government Organization, we should concern the ﬁnancial cost.

<!-- b000130 | prose | pages [5] -->
• The time for charging is same for all kinds of drones. They may roughly equal in the reality; thus, assuming they are equal can simplify our calcula- tion and the arrange of time.

<!-- b000131 | prose | pages [5] -->
• The drones only can be charged at cargo containers of the DroneGo dis- aster response system. Because the electrical system in the island is ruined in the disaster.

<!-- b000132 | prose | pages [5] -->
• The medicines do not need to be placed head on in the containers/cargo bay; most medicines and medical equipment are well-packed in daily life, with this assumption, we can use the space of containers/cargo bay better.

<!-- b000133 | prose | pages [5] -->
• Drones, medicines and cargo bays are packed separately in the container (medicines will not be placed in cargo bays and then placed them to- gether in the container). It is normal in our daily life.

<!-- b000134 | prose | pages [5] -->
• Environments and weather do not have inﬂuence in drones ﬂying/ob- serving. Our plan is arranged for most situation; thus, we ignore the ex- treme weather which exists rarely.

<!-- b000135 | prose | pages [5] -->
• The whole island is on a plane. For the difference of longitude is less than 2 degrees and difference of latitude is less than 0.5 degrees in the island, which just has a tiny inﬂuence on the shape of the island. Thus, we can ignore it for computational convenience.

<!-- b000136 | prose | pages [5] -->
• Hospitals can store redundant medical in a day. That is, except the daily demand, the hospital can store more medical for the following days.

<!-- b000137 | prose | pages [5] -->
• The drone of H type is used to offer communication between other drones and control center [2].So, each container should have at least one H.

<!-- b000138 | furniture | pages [6] -->
Team # 1908904

<!-- b000139 | prose | pages [6] -->
3

<!-- b000140 | heading | pages [6] -->
Notations

<!-- b000141 | prose | pages [6] -->
Description Symbols

<!-- b000142 | prose | pages [6] -->
D

<!-- b000143 | furniture | pages [6] -->
Page 3 of 30

<!-- b000144 | prose | pages [6] -->
Unit

<!-- b000145 | prose | pages [6] -->
days the number of days medicals can supply

<!-- b000146 | prose | pages [6] -->
LDi, WDi, HDi in. the length, width and height of the ith kind of drone

<!-- b000147 | prose | pages [6] -->
the length, width and height of the corresponding LBi, WBi, HBi in. bay for ith kind of drone

<!-- b000148 | prose | pages [6] -->
LMi, WMi, HMi in. the length, width and height of MEDi

<!-- b000149 | prose | pages [6] -->
Lc, Wc, Hc in. the length, width and height of the cargo container

<!-- b000150 | prose | pages [6] -->
the payload of the ith drone (here i is the drone num- zi ber but not type)

<!-- b000151 | prose | pages [6] -->
nd

<!-- b000152 | prose | pages [6] -->
lbs.

<!-- b000153 | prose | pages [6] -->
pieces the total number of the drones A-G

<!-- b000154 | prose | pages [6] -->
nMi pieces the number of the MEDi

<!-- b000155 | prose | pages [6] -->
nDi pieces the number of the ith kind of drone

<!-- b000156 | prose | pages [6] -->
CE None the comprehensive evaluation

<!-- b000157 | prose | pages [6] -->
T0 the charging time

<!-- b000158 | prose | pages [6] -->
A

<!-- b000159 | prose | pages [6] -->
min

<!-- b000160 | prose | pages [6] -->
None the average space used of all cargo containers

<!-- b000161 | prose | pages [6] -->
the largest distance the ith kind of drone can deliver xiR km medicines and come back

<!-- b000162 | prose | pages [6] -->
the largest distance the ith kind of drone can reach xiS with medicines km

<!-- b000163 | prose | pages [6] -->
the largest distance the ith kind of drone can reach xiM with medicines

<!-- b000164 | prose | pages [6] -->
(*Note: normally, i ∈[A, H])

<!-- b000165 | prose | pages [6] -->
km

<!-- b000166 | furniture | pages [7] -->
Team # 1908904

<!-- b000167 | furniture | pages [7] -->
Page 4 of 30

<!-- b000168 | prose | pages [7] -->
4 Speciﬁc formulation of problem

<!-- b000169 | prose | pages [7] -->
Above all, in terms of the number of containers, it is obvious that more contain- ers can provide more drones and medical supply. In addition, the area where the container is located can charge the drones. Therefore, more containers will make the drones more ﬂexible and create a wider reconnaissance range. The most im- portant point is that one or two cargo containers cannot cover the ﬁve hospitals (this will be shown in Part 7). Due to the reasons above, we ﬁrstly consider the number of containers is 3.

<!-- b000170 | prose | pages [7] -->
We think the helicopter has the ability to transport containers to inland. There- fore, in terms of the location of the container, we need to consider the location of the container inside Puerto Rico so that the container can meet the daily needs of the hospital and the road reconnaissance.

<!-- b000171 | caption | pages [7] -->
Figure 1: ﬂow diagram of solution

<!-- b000172 | furniture | pages [8] -->
Team # 1908904

<!-- b000173 | furniture | pages [8] -->
Page 5 of 30

<!-- b000174 | prose | pages [8] -->
5

<!-- b000175 | heading | pages [8] -->
AHP Model

<!-- b000176 | prose | pages [8] -->
5.1

<!-- b000177 | heading | pages [8] -->
Establish an AHP Model

<!-- b000178 | prose | pages [8] -->
To evaluate the proportion of medicine and drones which will be installed in the cargo container, we establish an AHP model which focuses on the following three aspects:

<!-- b000179 | prose | pages [8] -->
• Minimum time to complete medical supply delivery, during which we use all drones to deliver medicines to the ﬁve hospitals without rest until all medicines are conveyed properly.

<!-- b000180 | prose | pages [8] -->
• Amount of medical supply, which are the days our medicines can support the ﬁve hospitals keep working properly. By some easy calculations we can get that we need 7 MED1, 2 MED2, 4 MED3 per day; thus, to keep hospitals working D days, the amount of medical supply should be (let Vm = 7 nM1 + 2 nM2 + 4 nM3):

<!-- b000181 | prose | pages [8] -->
D × Vm

<!-- b000182 | prose | pages [8] -->
• Reconnaissance ability, which measures the total reconnaissance ability under the situation we choose.

<!-- b000183 | prose | pages [8] -->
5.2 The Reason why We Choose These Three Aspects

<!-- b000184 | prose | pages [8] -->
The amount of the medical supply judges that how long can the hospitals keep working, which is important because people’s life is vital in the whole rescue activity.

<!-- b000185 | prose | pages [8] -->
We consider the minimum time to complete medical supply delivery for two reasons:

<!-- b000186 | prose | pages [8] -->
• It ensures that the ﬁve hospitals have plenty medicines so that can help save people, and more medical supply at the beginning days in hospital can let the hospitals deal with some emergencies in reality (even though the medical demanded is given in the question).

<!-- b000187 | prose | pages [8] -->
• It reﬂects the efﬁciency of the NGO; faster completion of the task that means the organization can do more things with the same time. Time-cost is one thing we should consider. (*we have not counted in the time the drones cost on detecting the roads because it is not an urgent task and detection is much faster than restoration of the roads)

<!-- b000188 | prose | pages [8] -->
The problem requires us to detect roads as many as we can; thus, we choose reconnaissance ability as one of the factors we focus on.

<!-- b000189 | furniture | pages [9] -->
Team # 1908904

<!-- b000190 | furniture | pages [9] -->
Page 6 of 30

<!-- b000191 | prose | pages [9] -->
Weights of the Three Aspects 5.3

<!-- b000192 | prose | pages [9] -->
The main task is to bring the medicines to the hospitals, which relates to people’s life; thus, we regard it as the most important factor.

<!-- b000193 | prose | pages [9] -->
If we bring one Type B Drone (which can ﬂy furthest) in each cargo container, we can attain the largest reconnaissance area; thus, more drones can only observe the road more frequent or faster but cannot expand the detectable area anymore. As a result, we give it the smallest proportion.

<!-- b000194 | prose | pages [9] -->
Minimum

<!-- b000195 | prose | pages [9] -->
Aspect

<!-- b000196 | prose | pages [9] -->
time for delivery

<!-- b000197 | prose | pages [9] -->
Minimum time for

<!-- b000198 | prose | pages [9] -->
1 delivery

<!-- b000199 | prose | pages [9] -->
Amount of medical

<!-- b000200 | prose | pages [9] -->
4 supply

<!-- b000201 | prose | pages [9] -->
Reconnaissance

<!-- b000202 | prose | pages [9] -->
1 3

<!-- b000203 | prose | pages [9] -->
ability

<!-- b000204 | prose | pages [9] -->
Amount of

<!-- b000205 | prose | pages [9] -->
Reconnaissance

<!-- b000206 | prose | pages [9] -->
medical

<!-- b000207 | prose | pages [9] -->
Weight ability

<!-- b000208 | prose | pages [9] -->
supply

<!-- b000209 | prose | pages [9] -->
1 3 0.2051 4

<!-- b000210 | prose | pages [9] -->
1 8 0.7167

<!-- b000211 | prose | pages [9] -->
1 1 0.0783 8

<!-- b000212 | caption | pages [9] -->
Table 1: Pairwise comparison matrix of hierarchy

<!-- b000213 | prose | pages [9] -->
Through calculating the weights of three factors, we get the maximum eigen- value λ is 3.0183 and the consistency ratio CR is 0.0158. CR < 0.1, so the Consis- tency Test is right.

<!-- b000214 | prose | pages [9] -->
5.4 Normalization

<!-- b000215 | prose | pages [9] -->
Now we have already got the weight of each aspect; however, to analysis the three factors together, we need to normalize them so that they will have the same unit. Followings are our considering steps and normalized results:

<!-- b000216 | prose | pages [9] -->
We decide to give a mark (between 0 and 1) to each factor in every situation, which carries different number and kinds of drones as well as medicines. Details of the principles to give the marks are below.

<!-- b000217 | prose | pages [9] -->
5.4.1 Amount of medical supply

<!-- b000218 | prose | pages [9] -->
As we calculated, the ﬁve hospitals need 7 MED1, 2 MED2 and 4 MED3 per day. We deﬁne this one-day’s medical demand as a supply unit. For ensuring the basic medical demand during the ﬁrst many days after the disaster, we decide to supply at least 120 supply units. (which are enough for four months). In our

<!-- b000219 | furniture | pages [10] -->
Team # 1908904

<!-- b000220 | furniture | pages [10] -->
Page 7 of 30

<!-- b000221 | prose | pages [10] -->
marking system, a scheme which has 120 supply units is worth 0.6 marks; when the amount of medical supply approaches inﬁnity, the scheme worth 1 mark. To achieve these two criterions, we give a marking function:

<!-- b000222 | prose | pages [10] -->
D D + 80 , (D >= 120) f(D) =

<!-- b000223 | prose | pages [10] -->
Minimum time to complete medical supply delivery 5.4.2

<!-- b000224 | prose | pages [10] -->
We can know the function of time is (zi is the payload of drone i):

<!-- b000225 | prose | pages [10] -->
T = Pnd D × Vm

<!-- b000226 | prose | pages [10] -->
zi di

<!-- b000227 | prose | pages [10] -->
i=1

<!-- b000228 | prose | pages [10] -->
vi +T0

<!-- b000229 | prose | pages [10] -->
• For the speed of the fastest drone is 79km/h (63.2km/h with cargo bay) and the speed of the slowest drone is 60km/h (48km/h with cargo bay), assume that distance is 7km(the Type D Drones’ furthest ﬂight with cargo bay), a round-turn for this two drones cost Pnd

<!-- b000230 | prose | pages [10] -->
i=1 zi. The percentage difference is 4.998%; thus, we can regard the time for different types of drones is roughly same (consdering di

<!-- b000231 | prose | pages [10] -->
vi as a constant).

<!-- b000232 | prose | pages [10] -->
• When we only have one drone, we can take 1042 units of medicines; thus, if we add a drone, the impact of nd is much larger than the decrement in D. We decide to ignore the tiny change of D × Vm (Vm is a constant).

<!-- b000233 | prose | pages [10] -->
• In our greedy algorithm (we will introduce its details in Part Six), we adjust our plan by adding one drone per time and compare it with the former con- dition. Adding one drone will not inﬂuence the average of all drones’ pay- load capability when there are more than 10 drones; thus, we can reason- able assume the average of the drones’ payload capability does not change.

<!-- b000234 | prose | pages [10] -->
1 Finally, we can get T ∝ nd.

<!-- b000235 | prose | pages [10] -->
The full one mark of this factor is given by the following situation: With carrying 120 supply units of medicines (which ensure the medical supply) in the three cargo containers and three Type H Drones, the rest room is full of Type D Drones (which has the smallest volume of shipping container).

<!-- b000236 | prose | pages [10] -->
Vc = Lc × Wc × Hc Vh = LDH × WDH × HDH

<!-- b000237 | prose | pages [10] -->
Vd = LDD × WDD × HDD

<!-- b000238 | prose | pages [10] -->
Nmax = 3 × Vc −3 ∗Vh −120 × Vm

<!-- b000239 | prose | pages [10] -->
Vd To calculate other conditions’ marks, we simply use the number of the drones to divide the largest number Nmax.

<!-- b000240 | prose | pages [10] -->
g(n) = nd Nmax

<!-- b000241 | furniture | pages [11] -->
Team # 1908904

<!-- b000242 | prose | pages [11] -->
5.4.3 Reconnaissance ability

<!-- b000243 | furniture | pages [11] -->
Page 8 of 30

<!-- b000244 | prose | pages [11] -->
It is obvious that if we add a drone, the reconnaissance ability will be higher. A drone which can ﬂy further is able to detect more area and roads, which shows it has a higher reconnaissance ability. However, the drone’s ﬂying time is limited, the reconnaissance ability should not be exactly proportional to the area which it can reach. We regard it roughly be proportional to the sum of all drone’s max ﬂying distance.

<!-- b000245 | prose | pages [11] -->
The full one mark of this factor is given by the following situation: With carrying 120 supply units of medicines (which ensure the medical supply) in the three cargo containers and three Type H Drones, the rest room is full of Type B Drones (which has the largest ratio of ﬂight distance to its volume of shipping container). This situation has the largest sum of all drone’s max ﬂying distance.

<!-- b000246 | prose | pages [11] -->
Vb = LDB × WDB × HDB

<!-- b000247 | prose | pages [11] -->
Dmax = 3 × Vc −3 × (Vh −120 × Vm)

<!-- b000248 | prose | pages [11] -->
× 52.67

<!-- b000249 | prose | pages [11] -->
Vb Vb

<!-- b000250 | prose | pages [11] -->
To calculate other conditions’ marks, we simply use the sum of all drone’s max ﬂying distance in that situation to divide the largest sum to get the mark:

<!-- b000251 | prose | pages [11] -->
h(xn) =

<!-- b000252 | prose | pages [11] -->
6

<!-- b000253 | heading | pages [11] -->
Packing Model

<!-- b000254 | prose | pages [11] -->
PG

<!-- b000255 | prose | pages [11] -->
i=A xiM Dmax

<!-- b000256 | heading | pages [11] -->
Design Packing Conﬁguration with Greedy Algorithm

<!-- b000257 | prose | pages [11] -->
6.1

<!-- b000258 | prose | pages [11] -->
The “optimal” is deﬁned by the comprehensive evaluation CE, which can be calculated by the normalization formula in the AHP model. When the CE is the highest, the associated packing conﬁguration is the best.

<!-- b000259 | prose | pages [11] -->
CE = ωf · f(D) + ωg · g(n) + ωh · h(xn) ∈[0, 1]

<!-- b000260 | prose | pages [11] -->
The core idea of this model is the Greedy Algorithm. We put the drones into containers one by one, and guarantee that each time they are placed, they can achieve the highest comprehensive evaluation CE score. It’s rational that each new drone added will reduce the space to store the medicine. However, although the minimum time to complete medical supply delivery increases, the amount of medical supply decreases. Overall, the CE will increase ﬁrst and then decrease as the new drones added. And our ultimate goal is to get the condition where the comprehensive evaluation of packing conﬁguration score is the highest. Then, we get the amount of each type of drones shown in the Table 2.

<!-- b000261 | furniture | pages [12] -->
Team # 1908904

<!-- b000262 | furniture | pages [12] -->
Page 9 of 30

<!-- b000263 | prose | pages [12] -->
Type A B C D E F G H

<!-- b000264 | prose | pages [12] -->
Number 0 121 0 54 0 0 0 3

<!-- b000265 | caption | pages [12] -->
Table 2: The amount of each type of drones

<!-- b000266 | prose | pages [12] -->
As what we can see from the ﬁgure above, the types and number of drones ob- tained by greedy algorithm are: 121 drones of type B, 54 drones of type D, and 3 drones of type H. We ﬁnd that the result is rational and acceptable due to fol- lowing aspects:

<!-- b000267 | prose | pages [12] -->
• The type D drones have the smallest volume and a not bad max payload capability. They have the largest ratio of max payload capability to the volume.

<!-- b000268 | prose | pages [12] -->
• The type B drones have the furthest ﬂight distance, which means that the area they can reconnoiter is the largest. Hence, type B drones have the best ability of reconnaissance when we don’t consider the speed of each type of drones.

<!-- b000269 | prose | pages [12] -->
• What’s more, type B drones are the drones that have the highest speed; thus, they can connect each cargo container to allow even greater ﬂexibility (from cargo container A to B for recharging).

<!-- b000270 | prose | pages [12] -->
By calculating how much space is left in the container, we can calculate the ap- proximate number of days the medicine can last.

<!-- b000271 | prose | pages [12] -->
D = Lc × Wc × Hc −PH

<!-- b000272 | prose | pages [12] -->
i=A nDi × (LDi × WDi × HDi + LBi × WBi × HBi) P3

<!-- b000273 | prose | pages [12] -->
i=1 nMi × LMi × WMi × HMi = 411 days

<!-- b000274 | prose | pages [12] -->
The number of days obtained by this formula is an ideal value, that is, to com- pletely use the space of the container to package materials. However, we know that in reality, packing often leads to space waste. There will be some space which can not be used to store any items. Therefore, the actual number of days that the medicine can sustain is going to be less than but close to the ideal num- ber of days. Roughly, the actual number of days will be 20% less than the ideal time. However, 411 days is much larger than expected: 120 days (4 months), so the difference has little effect on our result.

<!-- b000275 | prose | pages [12] -->
6.2 Roughly Find the Positions for the Cargo Containers

<!-- b000276 | prose | pages [12] -->
Steps of Drawing the Map for Analysis

<!-- b000277 | prose | pages [12] -->
We use image analysis to roughly ﬁnd the positions for the cargo containers. Followings are some calculations for drawing the image:

<!-- b000278 | furniture | pages [13] -->
Team # 1908904

<!-- b000279 | furniture | pages [13] -->
Page 10 of 30

<!-- b000280 | prose | pages [13] -->
The furthest distance that the Type B drone can carry medicines to hospital and ﬂy back (xBR):

<!-- b000281 | prose | pages [13] -->
xBR = vB × tB

<!-- b000282 | prose | pages [13] -->
→

<!-- b000283 | prose | pages [13] -->
(1) 1 80% + 1

<!-- b000284 | prose | pages [13] -->
xBR = 23.4 km

<!-- b000285 | prose | pages [13] -->
The furthest distance that the Type D drone can carry medicines to hospital and ﬂy back (xDR):

<!-- b000286 | prose | pages [13] -->
xDR = vD × tD

<!-- b000287 | prose | pages [13] -->
→

<!-- b000288 | prose | pages [13] -->
(2) 1 80% + 1

<!-- b000289 | prose | pages [13] -->
xDR = 8 km

<!-- b000290 | prose | pages [13] -->
The furthest distance that the Type B drone can ﬂy from one cargo container to another cargo container with medicines and cargo bay (xBS):

<!-- b000291 | prose | pages [13] -->
xBS = VB × tB × 80% → xBS = 42.5 km

<!-- b000292 | prose | pages [13] -->
We use MATLAB to plot the following Figure 5.

<!-- b000293 | caption | pages [13] -->
Figure 2: Image for analyzing the rough locations

<!-- b000294 | prose | pages [13] -->
• The ﬁve red dots represent the ﬁve hospitals.

<!-- b000295 | prose | pages [13] -->
• The ﬁve blue circles (radius = xDR, with the center at the ﬁve red dots) means if the cargo container is in the blue circles, Type D drones can deliver medicines to the corresponding hospital.

<!-- b000296 | prose | pages [13] -->
• The ﬁve green circles (radius = xBR, with the center at the ﬁve red dots) means if the cargo container is in the green circles, Type B drones can de- liver medicines to the corresponding hospital.

<!-- b000297 | furniture | pages [14] -->
Team # 1908904

<!-- b000298 | furniture | pages [14] -->
Page 11 of 30

<!-- b000299 | prose | pages [14] -->
• The red circle (radius = xBR+ xBS, with the center at the most left red dot) means the furthest positions Type B drones can ﬂy to (with the precondi- tion that Type B drones can deliver medicines to the most left hospital). If we set another cargo container in the red circle, Type B drones can deliver medicines between these two containers.

<!-- b000300 | prose | pages [14] -->
• The dashed line is the approximate coastline, and the line between the mid- dle two red dots represents the coastline there. We cannot place cargo con- tainers above them.

<!-- b000301 | prose | pages [14] -->
(* We will give the information for the black circle and Area A, B, C after some analysis.)

<!-- b000302 | prose | pages [14] -->
The Aspects of a Good Locations for Cargo Containers

<!-- b000303 | prose | pages [14] -->
• The number of hospitals which can be covered by the delivery ability of two types of drones.

<!-- b000304 | prose | pages [14] -->
• Whether the drones can transfer the medicines from the cargo container to another cargo container or not. This ability allows we load medicines in other containers and transfer to the one needs them. It will promote the maximum of the days which medicines can keep supplying.

<!-- b000305 | heading | pages [14] -->
Results of the Rough Positions for the Three Cargo Containers

<!-- b000306 | prose | pages [14] -->
We choose Area A (which is shown in the picture) to place the Cargo Container A, because a cargo container there

<!-- b000307 | prose | pages [14] -->
• can supply medicines to the middle two hospitals by Type B and D drones;

<!-- b000308 | prose | pages [14] -->
• can supply medicines to the bottom hospital by Type B drones;

<!-- b000309 | prose | pages [14] -->
• remain the possibility to transfer medicines to other two cargo containers (one in the left and one in the right).

<!-- b000310 | prose | pages [14] -->
We choose Area B (which is shown in the picture) to place the Cargo Container B, because a cargo container there

<!-- b000311 | prose | pages [14] -->
• can supply medicines to the bottom hospital and the right one by Type B drones;

<!-- b000312 | prose | pages [14] -->
• can transfer medicines to Cargo Container A which is in Area A.

<!-- b000313 | prose | pages [14] -->
We draw the black circle (radius = xBS, with the center at Area A), which shows the furthest positions where Type B drones can ﬂy (from Area A) to. Thus, we choose Area C (which is shown in the picture) to place the Cargo Container C, because a cargo container there

<!-- b000314 | furniture | pages [15] -->
Team # 1908904

<!-- b000315 | furniture | pages [15] -->
Page 12 of 30

<!-- b000316 | prose | pages [15] -->
• can supply medicines to the left hospital by Type B drones;

<!-- b000317 | prose | pages [15] -->
• can transfer medicines to Cargo Container A which is in Area A.

<!-- b000318 | prose | pages [15] -->
6.3

<!-- b000319 | heading | pages [15] -->
Packing model in reality

<!-- b000320 | prose | pages [15] -->
Now, we have got the approximate position of each cargo container, so that we can determine the associated packing conﬁguration for each of them.

<!-- b000321 | prose | pages [15] -->
For cargo containers B and C, they are so far away from every hospital that type D drones cannot be used to deliver medicine. Thus, all the type D drones should be packed in cargo container A.Only Hosp1 and Hosp2, which are both quite close to cargo container A, need the medicine 2. Therefore, it’s rational to pack all the medicine 2 in the Cargo container A. Cargo container B and C initially only have type B drones. Although they will both need to deliver medicine to the Hosp1, Hosp2, and Hosp3, Cargo container B has more load(offers medicine to two hospitals directly, but C only has one) than C, it will need much more room for medicine storage. Hence, we decide to pack more type B drones ( 3

<!-- b000322 | prose | pages [15] -->
5ND2) in Cargo container C than B (2

<!-- b000323 | prose | pages [15] -->
5ND2) ;

<!-- b000324 | prose | pages [15] -->
6.4 3D Bin-packing

<!-- b000325 | prose | pages [15] -->
3DBP [3] is developed by company 3Dbinpacking, which established in 2012 and designed to solve the three-dimensional packing problem. By using the available API supported by 3DBP, we use the Bisection method to ﬁnd the best packing condition.

<!-- b000326 | prose | pages [15] -->
The key idea is that we ﬁrstly decrease all kinds of good in ideal condition to 70% to ensure that all the cargo container can pack everything. The percent- age of each good keep the same as initial after decreasing. Firstly, we make cargo container B pack more medicine 3 as Hosp4 and Hosp5 need. Secondly, we make cargo container C pack more medicine 1 as Hosp1 needs. Finally, we pack all the remaining thing in cargo container A. If three cargo containers can pack all the things when we increase the decreasing percentage (initially set to 70%), we will adopt the new packing plan. With the help of the Bisection method, we can get the ﬁnal result shown in Table 3.

<!-- b000327 | prose | pages [15] -->
(a) Container A (b) Container B (c) container C

<!-- b000328 | caption | pages [15] -->
Figure 3: Conﬁguration of each container

<!-- b000329 | furniture | pages [16] -->
Team # 1908904

<!-- b000330 | prose | pages [16] -->
Items and properties Container A

<!-- b000331 | prose | pages [16] -->
B 0 D 42 H 1 Type 1 42 MED 1 831 MED 2 718 MED 3 677 Space used 77.60%

<!-- b000332 | furniture | pages [16] -->
Page 13 of 30

<!-- b000333 | prose | pages [16] -->
Container B Container C

<!-- b000334 | prose | pages [16] -->
39 60 0 0 1 1 39 60 1077 605 0 0 759 0 89.34% 81.64%

<!-- b000335 | caption | pages [16] -->
Table 3: Pairwise comparison matrix of hierarchy

<!-- b000336 | prose | pages [16] -->
The detail of packing is shown in Figure 3. We can calculate the average space used of the three cargo containers: A = 82.86%.

<!-- b000337 | prose | pages [16] -->
7 Accurate Locations

<!-- b000338 | caption | pages [16] -->
Figure 4: routes, cities and range

<!-- b000339 | prose | pages [16] -->
Based on the approximate location of three cargo containers(as shown in Figure 4), we use the discretization method to calculate the accurate locations. Firstly we discretize roads and reconnaissance area into pixels. By computing the pixel number of roads and highways, and the number of populated places in the re- connaissance area, we use standardization to get the standard of every point. During this process, we give the weight of highway and road length as 0.6 and populated places as 0.4. After that, we calculate all the point inside the brown area (the approximate location) to get the exact locations, which are shown in

<!-- b000340 | caption | pages [16] -->
Table 4 and Figure 5.

<!-- b000341 | prose | pages [16] -->
In Figure 5, the black curves represent the highways and roads. The red points represent the populated places and the green points represent the accurate loca- tion we get.

<!-- b000342 | furniture | pages [17] -->
Team # 1908904

<!-- b000343 | prose | pages [17] -->
Cargo Container Latitude

<!-- b000344 | prose | pages [17] -->
A 18.40 B 18.21 C 18.43

<!-- b000345 | furniture | pages [17] -->
Page 14 of 30

<!-- b000346 | prose | pages [17] -->
Longitude

<!-- b000347 | prose | pages [17] -->
-66.12 -65.82 -66.51

<!-- b000348 | caption | pages [17] -->
Table 4: Accurate location of each cargo container

<!-- b000349 | caption | pages [17] -->
Figure 5: accurate location

<!-- b000350 | prose | pages [17] -->
8 Timetable of Flights

<!-- b000351 | prose | pages [17] -->
The initial conditions of three cargo containers are mentioned in the Part 6 We can know a whole ﬂight is less than two hours (the ﬂying period is less than one hour, and charging period is one hour); thus, we set two hours as a ﬂight period. There are ten hours (8:00 – 18:00) per day, during which the drones can ﬂy. We use 30 Type B drones (initially in Cargo Container C) to detect the roads. They will detect all the areas which they can ﬂy to and come back two hours by two hours (ﬁve times per day); thus, we do not list them in the timetable. Our aims of setting the timetables are trying to deliver the medicines as soon as possible and to completion at the same time for the ﬁve hospitals.

<!-- b000352 | prose | pages [17] -->
*Notes:

<!-- b000353 | prose | pages [17] -->
• 1⃝- 5⃝represents the ﬁve hospitals: 1⃝: Hospital Pavia Arecibo, 2⃝: Puerto Rico Children’s Hospital, 3⃝: Hospital Pavia Santurce, 4⃝: Hospital HIMA,

<!-- b000354 | prose | pages [17] -->
5⃝: Caribbean Medical Center.

<!-- b000355 | prose | pages [17] -->
• A, B and C represent Cargo Container A, B and C.

<!-- b000356 | prose | pages [17] -->
• N × Type X(n × MEDi + m × MEDj) →Location L represents ﬂights that N Type/, X drones ﬂy to location L with each carrying nMEDiand

<!-- b000357 | furniture | pages [18] -->
Team # 1908904

<!-- b000358 | furniture | pages [18] -->
Page 15 of 30

<!-- b000359 | prose | pages [18] -->
mMEDj. (e.g. 42 × D(4 × MED2) →2⃝means 42 Type D drones ﬂy to 2⃝ with each carrying 4 MED2; A ﬂight which does not carry any medicines represented with no bracket.)

<!-- b000360 | prose | pages [18] -->
• A ﬂight to the hospitals will ﬂy back to the original place, while a ﬂight to another cargo container won’t. Every drone always carries a cargo bay, we do not consider cargo bays separately anymore.

<!-- b000361 | caption | pages [18] -->
Figure 6: timetable for day 1

<!-- b000362 | prose | pages [18] -->
After Day One, each hospital has medicines which can maintain at least 12 days.

<!-- b000363 | furniture | pages [19] -->
Team # 1908904

<!-- b000364 | furniture | pages [19] -->
Page 16 of 30

<!-- b000365 | caption | pages [19] -->
Figure 7: timetable for day 2

<!-- b000366 | prose | pages [19] -->
• After Day Two, every period’s ﬂights are cyclic: Departure from Cargo Container A: 

<!-- b000367 | prose | pages [19] -->
11 × B(2 × MED1) →3⃝

<!-- b000368 | prose | pages [19] -->


<!-- b000369 | prose | pages [19] -->
2 × B(1 × MED1 + 1 × MED3) →2⃝

<!-- b000370 | prose | pages [19] -->


<!-- b000371 | prose | pages [19] -->
each time.

<!-- b000372 | prose | pages [19] -->
42 × D(1 × MED1 + 1 × MED3) →2⃝

<!-- b000373 | prose | pages [19] -->
After looping 11 times, the 22th time (on Day 5)’s ﬂights are: 

<!-- b000374 | prose | pages [19] -->
7 × B(2 × MED1) →3⃝ 1 × B(1 × MED1) →3⃝

<!-- b000375 | prose | pages [19] -->


<!-- b000376 | prose | pages [19] -->


<!-- b000377 | prose | pages [19] -->


<!-- b000378 | prose | pages [19] -->
30 × D(1 × MED1 + 1 × MED3) →2⃝

<!-- b000379 | prose | pages [19] -->
• Departure from Cargo Container C: 17 × B(2 × MED1) →1⃝each time. After looping 7 times, the 18th time (on Day 4)’s ﬂights are: 16 × B(2 × MED1) →1⃝

<!-- b000380 | prose | pages [19] -->


<!-- b000381 | prose | pages [19] -->
1 × B(1 × MED1) →1⃝

<!-- b000382 | prose | pages [19] -->
As the result, after Day 5(the last day we still need to deliver medicines) all hos- pitals have medicines which can keep 359 days.

<!-- b000383 | furniture | pages [20] -->
Team # 1908904

<!-- b000384 | furniture | pages [20] -->
Page 17 of 30

<!-- b000385 | heading | pages [20] -->
Sensitivity Evaluation of the Model

<!-- b000386 | prose | pages [20] -->
9

<!-- b000387 | heading | pages [20] -->
Sensitivity of the max distance reduction rate for drones

<!-- b000388 | prose | pages [20] -->
9.1

<!-- b000389 | prose | pages [20] -->
According to equations 1 and 2, we can know that the rate of distance reduction for drones largely determines the maximum distance that the cargo containers from hospitals. The change of this rate will result in the shift of the exact cargo containers location.

<!-- b000390 | prose | pages [20] -->
Firstly, we make the ratio increase of 0.025. We calculate the furthest distances from a cargo container that the Type B and Type D drones can carry medicines to a hospital and ﬂy back: xBR = 23.81km, xDR = 8.14km

<!-- b000391 | prose | pages [20] -->
Secondly, we make the ratio decrease of 0.025. After the same calculation, we get: xBR = 23.00km, xDR = 7.86km

<!-- b000392 | prose | pages [20] -->
We show the exact ﬁnal location for each cargo container in Table 5.

<!-- b000393 | prose | pages [20] -->
Container A

<!-- b000394 | prose | pages [20] -->
0.8 (18.40, -66.12) 0.825 (18.39, -66.11) 0.775 (18.40, -66.12)

<!-- b000395 | prose | pages [20] -->
Container B Container C

<!-- b000396 | prose | pages [20] -->
(18.21, -65.82) (18.43, -66.51) (18.20, -65.82) (18.43, -66.51) (18.21, -65.82) (18.43, -66.52)

<!-- b000397 | caption | pages [20] -->
Table 5: sensitive test result of distance reduction

<!-- b000398 | prose | pages [20] -->
We ﬁnd that the change in the rate of distance reduction for drones will shift of the exact cargo containers location, but the difference is so small that we can even ignore it.

<!-- b000399 | heading | pages [20] -->
Sensitivity of the weight in AHP

<!-- b000400 | prose | pages [20] -->
9.2

<!-- b000401 | prose | pages [20] -->
We evaluate the associated packing conﬁguration by the minimum time to com- plete medical supply delivery, the amount of medical supply, and the reconnais- sance ability. The weight of these three factors will result in different packing plan of drones’ selection in the ideal condition.

<!-- b000402 | prose | pages [20] -->
Firstly, we increase the weight of one factor and equally remove the difference to the other two factors. We make the same progress for the other factors.

<!-- b000403 | prose | pages [20] -->
Secondly, we decrease the weight of one factor and equally remove the differ- ence to the other two factors. We make the same progress for the other factors.

<!-- b000404 | prose | pages [20] -->
We show the ﬁnal result of the drone selection in Figure 8.

<!-- b000405 | furniture | pages [21] -->
Team # 1908904

<!-- b000406 | furniture | pages [21] -->
Page 18 of 30

<!-- b000407 | caption | pages [21] -->
Figure 8: the sensitive test of AHP

<!-- b000408 | prose | pages [21] -->
We ﬁnd that the only drones our model choose are type B and type D. The maxi- mum percentage difference β1 of the number of B Drones is 9.92%. The maximum percentage difference β2 of the number of D Drones is 33.3%. The maximum per- centage difference β3 of the number of D (days) is 2.4%. In fact, the number of D cannot inﬂuence the result a lot. So, they are small enough to show that our model is stable and reliable.

<!-- b000409 | prose | pages [21] -->
10

<!-- b000410 | heading | pages [21] -->
Strengths and weaknesses

<!-- b000411 | prose | pages [21] -->
In this part, we will analyze the strengths and weaknesses of our model.

<!-- b000412 | prose | pages [21] -->
10.1

<!-- b000413 | heading | pages [21] -->
Strengths

<!-- b000414 | prose | pages [21] -->
• High space utilization 3-D packing problem is a Non-deterministic Polynomial(N-P) problem, which means that we cannot get the answer directly only by calculation. How- ever, the 3DBP model provides an excellent simulation to approach the best packing way.

<!-- b000415 | prose | pages [21] -->
• Good ﬂexibility Based on the AHP method, it’s available for us that we can change the weight of each aspect to satisﬁed different demands for we need in reality.

<!-- b000416 | prose | pages [21] -->
• Both consider the populated place and the roads for reconnaissance Both consider the populated place and the roads for reconnaissance In the

<!-- b000417 | furniture | pages [22] -->
Team # 1908904

<!-- b000418 | furniture | pages [22] -->
Page 19 of 30

<!-- b000419 | prose | pages [22] -->
exact position calculation, our model both consider the main cities and the roads. It’s reasonable that there are many main roads in and around the populated place. It improves the reliability of our model.

<!-- b000420 | prose | pages [22] -->
10.2

<!-- b000421 | heading | pages [22] -->
Weakness

<!-- b000422 | prose | pages [22] -->
• The max distance reduction rate for drones are the same In our model, the max distance reduction rate for all types of drones are the same. With physical analysis, we can know that the speed and the ﬂight time are related to the power and weight of drones. Actually, the max distance reduction rate for the different type of drones might be different.

<!-- b000423 | prose | pages [22] -->
• Ignore the altitude Although most of the mountains (high altitude area) are around the island, there still exits some distance error caused by altitude difference.

<!-- b000424 | prose | pages [22] -->
11

<!-- b000425 | heading | pages [22] -->
Conclusions

<!-- b000426 | prose | pages [22] -->
The NGO should set three cargo containers at (18.40, -66.12), (18.43, -66.51) and (18.21, -65.28) (latitude, longitude). We determine to bring 121 Type B drones and 42 Type D drones to complete the task. The average space used ratio is 82.86%. Our plan brings medicines which are enough for 359 days; what’s more, we can deliver all the medicines in ﬁve days. We can detect as much as possible roads, and there are about 9 cities is in our reconnaissance range as well. (Figure 9 is created by Google map. The red points represent the accurate locations of three cargo containers, and the blue points represent the ﬁve hospitals. )

<!-- b000427 | caption | pages [22] -->
Figure 9: location in Google Map

<!-- b000428 | furniture | pages [23] -->
Team # 1908904

<!-- b000429 | prose | pages [23] -->
A letter to HELP, Inc January 28, 2019

<!-- b000430 | prose | pages [23] -->
Dear CEO of HELP, Inc:

<!-- b000431 | furniture | pages [23] -->
Page 20 of 30

<!-- b000432 | prose | pages [23] -->
Hearing that HELP, Inc is a Non-governmental Organization and recently developing a transportable disaster response system; We are more than glad to share our mathematical model to give some recommendations.

<!-- b000433 | prose | pages [23] -->
We strongly advise you to transport three cargo containers to Puerto Rico. Otherwise, there will be hospitals which cannot receive medicines.

<!-- b000434 | prose | pages [23] -->
Besides, due to the non-proﬁt property of HELP, Inc, we recommend using rechargeable drones. When considering the minimum time to complete medical supply de- livery, the amount of medical supply, and the available reconnaissance area, we select type B, D, and H drones. Also, a rational packing plan is given in the ﬁgure below, which allows three cargo contains to pack 359 days unit medicine and has 82.86% average space used.

<!-- b000435 | prose | pages [23] -->
After considering the connection between containers, the number of hospi- tals, the length of roads, and the number of populated places, we give you a reliable timetable for the drones (shown below), which can complete all the task within ﬁve days and allow a part of drones to detect roads.

<!-- b000436 | prose | pages [23] -->
However, due to the max ﬂight distance limit of drones and the medicine requirement of hospitals, it’s impossible to detect the whole Puerto Irco only by three containers. Meanwhile, to increase the efﬁciency of medicine delivery and reconnaissance ability, we use more drones, which will result in a lower space used of cargo containers.

<!-- b000437 | prose | pages [23] -->
We hope that our model can help HELP, Inc to save even one more people’s life. And we also hope that there will be more organizations like HELP, Inc. Dis- asters are horrible, but people’s care can resist everything.

<!-- b000438 | prose | pages [23] -->
Items and properties Container A

<!-- b000439 | prose | pages [23] -->
B 0 D 42 H 1 Type 1 42 MED 1 831 MED 2 718 MED 3 677 Space used 77.60%

<!-- b000440 | prose | pages [23] -->
Container B Container C

<!-- b000441 | prose | pages [23] -->
39 60 0 0 1 1 39 60 1077 605 0 0 759 0 89.34% 81.64%

<!-- b000442 | furniture | pages [24] -->
Team # 1908904

<!-- b000443 | furniture | pages [24] -->
Page 21 of 30

<!-- b000444 | prose | pages [24] -->
Yours sincerely,

<!-- b000445 | furniture | pages [24] -->
Team #1908904

<!-- b000446 | prose | pages [24] -->
MCM2019

<!-- b000447 | furniture | pages [25] -->
Team # 1908904

<!-- b000448 | furniture | pages [25] -->
Page 22 of 30

<!-- b000449 | heading | pages [25] -->
References

<!-- b000450 | references | pages [25] -->
[1] W. Wei, M. Hao, X. Jin-qi, and S. Chang-yin, “Research on standardized de-

<!-- b000451 | references | pages [25] -->
sign method of airframe for multi-rotor uav,” no. 5, pp. 147–150, 2014.

<!-- b000452 | references | pages [25] -->
[2] L. Wei and L. Yuejun, “The research on building high-altitude communica-

<!-- b000453 | references | pages [25] -->
tion base station by using uav,” Communication World, no. 9, pp. 12–13, 2017.

<!-- b000454 | references | pages [25] -->
[3] 3Dbinpacking, “Single bin packing,” https://www.3dbinpacking.com/en/

<!-- b000455 | references | pages [25] -->
about-us, accessed January 4, 2019.

<!-- b000456 | furniture | pages [26] -->
Team # 1908904

<!-- b000457 | furniture | pages [26] -->
Page 23 of 30

<!-- b000458 | references | pages [26] -->
A

<!-- b000459 | heading | pages [26] -->
Appendices

<!-- b000460 | prose | pages [26] -->
A.1

<!-- b000461 | heading | pages [26] -->
Greedy Algorithm

<!-- b000462 | prose | pages [26] -->
#include "greedy.h" #include <stdio.h>

<!-- b000463 | prose | pages [26] -->
int Greedy(int drone_num[], float w_time, float w_amount, float w_scale) {

<!-- b000464 | prose | pages [26] -->
float scale = 0; int total_load = 0; int occupy = 3 * drone[7].d_size.height * drone[7].d_size.width

<!-- b000465 | prose | pages [26] -->
* drone[7].d_size.length; int pack = (7 * med[0].m_size.height

<!-- b000466 | prose | pages [26] -->
* med[0].m_size.length * med[0].m_size.width + 2 * med[1].m_size.height * med[1].m_size.length * med[1].m_size.width + 4 * med[2].m_size.height * med[2].m_size.length * med[2].m_size.width); float grade = 0; while (1) {

<!-- b000467 | prose | pages [26] -->
int n = 0; float m = 0; for (int i = 1; i < 7; i++) {

<!-- b000468 | prose | pages [26] -->
float amount = ISO.length * ISO.width * ISO.height * 3

<!-- b000469 | prose | pages [26] -->
- occupy; int t = drone[i].type; amount -= bay_size[t].height * bay_size[t].width

<!-- b000470 | prose | pages [26] -->
* bay_size[t].length; amount -= (drone[i].d_size.height * drone[i].d_size.width

<!-- b000471 | prose | pages [26] -->
* drone[i].d_size.length); amount = amount / pack; if (amount < 120) continue; int num = 0; for (int j = 0; j<8; j++) num+=drone_num[j]; float time = 1.0 *num/394; amount = amount / (80 +amount); float temp_scale = scale; if (drone[i].video)

<!-- b000472 | prose | pages [26] -->
temp_scale += (1.0*drone[i].v*drone[i].t/60.0); temp_scale = temp_scale / (256 * 52.67); float n_grade = amount * w_amount + time * w_time +

<!-- b000473 | prose | pages [26] -->
temp_scale * w_scale; if (n_grade > m) { m = n_grade; n = i; } } if (m >= grade) {

<!-- b000474 | prose | pages [26] -->
grade = m; drone_num[n]++; scale += 1.0*drone[n].v*drone[n].t/60.0; int t = drone[n].type; occupy += drone[n].d_size.height * drone[n].d_size.width

<!-- b000475 | prose | pages [26] -->
* drone[n].d_size.length; occupy += bay_size[t].height * bay_size[t].width

<!-- b000476 | prose | pages [26] -->
* bay_size[t].length; total_load += drone[n].load; }

<!-- b000477 | furniture | pages [27] -->
Team # 1908904

<!-- b000478 | furniture | pages [27] -->
Page 24 of 30

<!-- b000479 | prose | pages [27] -->
if (m < grade) { break; } } return (ISO.length * ISO.width * ISO.height * 3 - occupy)/pack; }

<!-- b000480 | prose | pages [27] -->
void test(float w1, float w2, float w3) {

<!-- b000481 | prose | pages [27] -->
int drone_num[8] = {0, 0, 0, 0, 0, 0, 0, 3}; printf("%d\n", Greedy(drone_num, w1, w2, w3)); for (int i = 0; i < 8; i++)

<!-- b000482 | prose | pages [27] -->
printf("%d ",drone_num[i]); printf("\n"); } int main() {

<!-- b000483 | prose | pages [27] -->
float w[3] = {0.2051, 0.7167, 0.0783}; test(w[0], w[1], w[2]); }

<!-- b000484 | prose | pages [27] -->
A.2 Binary Search with 3D bin-packing API

<!-- b000485 | prose | pages [27] -->
#!/usr/bin/python

<!-- b000486 | prose | pages [27] -->
import http.client import urllib import json

<!-- b000487 | prose | pages [27] -->
DAY_MAX = 370 DAY_MIN = 330 ORIGIN_B = 121 ORIGIN_DAY = 411 ORIGIN_D = 52

<!-- b000488 | prose | pages [27] -->
def getAns(item_list):

<!-- b000489 | prose | pages [27] -->
bin_list = [{"w": 231, "h": 92, "d": 94, "max_wg": 1000, "id": "1"}] conn = http.client.HTTPConnection(host=’eu.api.3dbinpacking.com’, port=80) #data = {"bins": bin_list, "items": item_list, "username": "yjsxuanyuan", "api_key "images_width": 250, "images_height": 250, "images_complete": 1}}

<!-- b000490 | prose | pages [27] -->
data = {"bins": bin_list, "items": item_list, "username": "yjsxuanyuan", "api_key params = urllib.parse.urlencode( {’query’:json.dumps(data)} ) headers = {"Content-type": "application/x-www-form-urlencoded",

<!-- b000491 | prose | pages [27] -->
"Accept": "text/plain"} conn.request( "POST", "/packer/pack", params, headers ) content = conn.getresponse( ).read( ) conn.close() ans = json.loads(content); return ans;

<!-- b000492 | prose | pages [27] -->
item_list_all = [ {"w": 30, "h": 30, "d": 22, "q": 121, "vr": 1, "wg": 0, "id": "B"}, {"w": 65, "h": 75, "d": 41, "q": 3, "vr": 1, "wg": 0, "id": "H"}, {"w": 8, "h": 10, "d": 14, "q": 121 + 52, "vr": 1, "wg": 0, "id": "Type 1"}, {"w": 14, "h": 7, "d": 5, "q": 7*411, "vr": 1, "wg": 0, "id": "MED 1"}, {"w": 12, "h": 7, "d": 4, "q": 4*411, "vr": 1, "wg": 0, "id": "MED 3"}, {"w": 25, "h": 20, "d": 25, "q": 52, "vr": 1, "wg": 0, "id": "D"},

<!-- b000493 | furniture | pages [28] -->
Team # 1908904

<!-- b000494 | furniture | pages [28] -->
Page 25 of 30

<!-- b000495 | prose | pages [28] -->
{"w": 5, "h": 8, "d": 5, "q": 2*411, "vr": 1, "wg": 0, "id": "MED 2"} ]

<!-- b000496 | prose | pages [28] -->
dl = DAY_MIN; dr = DAY_MAX; while (dl < dr):

<!-- b000497 | prose | pages [28] -->
day = (dl + dr + 1)// 2 b_num = 339 * ORIGIN_B // ORIGIN_DAY; d_num = 339 * ORIGIN_D // ORIGIN_DAY;

<!-- b000498 | prose | pages [28] -->
print(day,":")

<!-- b000499 | prose | pages [28] -->
item_list1 = [ {"w": 30, "h": 30, "d": 22, "q": b_num - b_num * 2 // 5, "vr": 1, "wg": 0, "id": {"w": 8, "h": 10, "d": 14, "q": b_num - b_num * 2 // 5, "vr": 1, "wg": 0, "id": "Type 1"}, {"w": 65, "h": 75, "d": 41, "q": 1, "vr": 1, "wg": 0, "id": "H"}, {"w": 14, "h": 7, "d": 5, "q": day, "vr": 1, "wg": 0, "id": "MED 1"} ]

<!-- b000500 | prose | pages [28] -->
item_list3 = [ {"w": 30, "h": 30, "d": 22, "q": b_num * 2// 5, "vr": 1, "wg": 0, "id": "B"}, {"w": 65, "h": 75, "d": 41, "q": 1, "vr": 1, "wg": 0, "id": "H"}, {"w": 8, "h": 10, "d": 14, "q": b_num * 2// 5, "vr": 1, "wg": 0, "id": "Type 1"} {"w": 14, "h": 7, "d": 5, "q": 3*day, "vr": 1, "wg": 0, "id": "MED 1"}, {"w": 12, "h": 7, "d": 4, "q": 2*day, "vr": 1, "wg": 0, "id": "MED 3"} ]

<!-- b000501 | prose | pages [28] -->
ans = getAns(item_list3) maxn3 = 0 if (not ans["response"]["bins_packed"][0]["not_packed_items"]):

<!-- b000502 | prose | pages [28] -->
l = 0 #130 r = 2*day while (l < r):

<!-- b000503 | prose | pages [28] -->
print(l,r) mid = (l + r + 1) // 2 temp_list = item_list3[:] temp_list[-1] = item_list3[-1].copy() temp_list[-1]["q"] += mid ans2 = getAns(temp_list) if (not ans2["response"]["bins_packed"][0]["not_packed_items"]):

<!-- b000504 | prose | pages [28] -->
l = mid else:

<!-- b000505 | prose | pages [28] -->
r = mid - 1 maxn3 = l print(l) else:

<!-- b000506 | prose | pages [28] -->
dr = day - 1 continue

<!-- b000507 | furniture | pages [29] -->
Team # 1908904

<!-- b000508 | furniture | pages [29] -->
Page 26 of 30

<!-- b000509 | prose | pages [29] -->
maxn1 = 0 ans = getAns(item_list1) if (not ans["response"]["bins_packed"][0]["not_packed_items"]):

<!-- b000510 | prose | pages [29] -->
l = 0 #130 r = 3 * day while (l < r):

<!-- b000511 | prose | pages [29] -->
mid = (l + r + 1) // 2# temp_list = item_list1[:] temp_list[-1] = item_list1[-1].copy() temp_list[-1]["q"] += mid ans2 = getAns(temp_list) if (not ans2["response"]["bins_packed"][0]["not_packed_items"]):

<!-- b000512 | prose | pages [29] -->
l = mid else:

<!-- b000513 | prose | pages [29] -->
r = mid - 1 maxn1 = l print(l) else:

<!-- b000514 | prose | pages [29] -->
dr = day - 1 continue

<!-- b000515 | prose | pages [29] -->
item_list2 = [ {"w": 8, "h": 10, "d": 14, "q": d_num, "vr": 1, "wg": 0, "id": "Type 1"}, {"w": 25, "h": 20, "d": 25, "q": d_num, "vr": 1, "wg": 0, "id": "D"}, {"w": 65, "h": 75, "d": 41, "q":

<!-- b000516 | prose | pages [29] -->
1,"vr": 1, "wg": 0, "id": "H"}, {"w": 5, "h": 8, "d": 5, "q": 2*day, "vr": 1, "wg": 0, "id": "MED 2"}, {"w": 14, "h": 7, "d": 5, "q": 3*day-maxn1, "vr": 1, "wg": 0, "id": "MED 1"}, {"w": 12, "h": 7, "d": 4, "q": 2*day-maxn3, "vr": 1, "wg": 0, "id": "MED 3"} ]

<!-- b000517 | prose | pages [29] -->
ans = getAns(item_list2) print(ans)

<!-- b000518 | prose | pages [29] -->
if (not ans["response"]["bins_packed"][0]["not_packed_items"]):

<!-- b000519 | prose | pages [29] -->
dl = day else:

<!-- b000520 | prose | pages [29] -->
dr = day - 1

<!-- b000521 | prose | pages [29] -->
A.3 Image Generating

<!-- b000522 | prose | pages [29] -->
hospital = [18.33 -65.65 18.22 -66.03 18.44 -66.07 18.40 -66.16 18.47 -66.73];

<!-- b000523 | prose | pages [29] -->
position = [18.40 -66.12 18.43 -66.52 18.21 -65.82];

<!-- b000524 | prose | pages [29] -->
hospital = hospital’;

<!-- b000525 | furniture | pages [30] -->
Team # 1908904

<!-- b000526 | furniture | pages [30] -->
Page 27 of 30

<!-- b000527 | prose | pages [30] -->
position = position’;

<!-- b000528 | prose | pages [30] -->
[m, n] = size(hospital); [m2,n2] = size(position);

<!-- b000529 | prose | pages [30] -->
hospital(1,:) = (hospital(1, :) - 17.91)*1000; hospital(2,:) = (hospital(2,:) + 67.32)*1000;

<!-- b000530 | prose | pages [30] -->
position(1,:) = (position(1, :) - 17.91)*1000; position(2,:) = (position(2,:) + 67.32)*1000;

<!-- b000531 | prose | pages [30] -->
standard = 9.5;

<!-- b000532 | prose | pages [30] -->
figure hold on

<!-- b000533 | prose | pages [30] -->
% r = 26.3*standard; % % for i= 1: 3 % theta = 0:pi/100:2*pi; % x=r*cos(theta)+position(2,i); % y=r*sin(theta)+position(1,i); % plot(x,y,’-g’); % end

<!-- b000534 | prose | pages [30] -->
plot(hospital(2,:),hospital(1,:),’.r’,’markersize’,16);

<!-- b000535 | prose | pages [30] -->
plot(position(2,:),position(1,:),’.g’,’markersize’,16);

<!-- b000536 | prose | pages [30] -->
axis equal;

<!-- b000537 | prose | pages [30] -->
ax.YAxis.Visible = ’off’;

<!-- b000538 | prose | pages [30] -->
ax.XAxis.Visible = ’off’; set(gca,’xtick’,[],’ytick’,[],’xcolor’,’w’,’ycolor’,’w’);

<!-- b000539 | prose | pages [30] -->
axis([0, 2000, 0, 1000]);

<!-- b000540 | prose | pages [30] -->
r = 23.00 * standard;

<!-- b000541 | prose | pages [30] -->
for i= 1: 5

<!-- b000542 | prose | pages [30] -->
theta = 0:pi/100:2*pi; x=r*cos(theta)+hospital(2,i); y=r*sin(theta)+hospital(1,i); plot(x,y,’-g’); end

<!-- b000543 | prose | pages [30] -->
r = 7.86* standard; for i= 1: 5

<!-- b000544 | prose | pages [30] -->
theta = 0:pi/100:2*pi; x=r*cos(theta)+hospital(2,i);

<!-- b000545 | furniture | pages [31] -->
Team # 1908904

<!-- b000546 | furniture | pages [31] -->
Page 28 of 30

<!-- b000547 | prose | pages [31] -->
y=r*sin(theta)+hospital(1,i); plot(x,y,’-b’); end

<!-- b000548 | prose | pages [31] -->
a = position(2,1); b = position(1,1); plot(a,b,’.’); r = 42.5 * standard; theta = 0:pi/100:2*pi; x=r*cos(theta)+a; y=r*sin(theta)+b; plot(x,y,’-r’,’Color’,[0,0,0]);

<!-- b000549 | prose | pages [31] -->
%plot([0,2000],[hospital(1:5),hospital(1:5)],’--’); plot([0,2000],[hospital(1,5),hospital(1,5)],’--’,’Color’,[0.5,0.5,0.5]);

<!-- b000550 | prose | pages [31] -->
r = standard * 65.4; theta = 0:pi/100:2*pi;

<!-- b000551 | prose | pages [31] -->
x=r*cos(theta)+hospital(2,5); y=r*sin(theta)+hospital(1,5); plot(x,y,’-r’);

<!-- b000552 | prose | pages [31] -->
plot(1)

<!-- b000553 | prose | pages [31] -->
A.4 Image Processing and Optimal Position

<!-- b000554 | prose | pages [31] -->
from skimage import io import matplotlib.pyplot as plt

<!-- b000555 | prose | pages [31] -->
area = set({}) area2 = set({}) area3 = set({}) hospital = [] r = round(26.3 / 0.10377) // 5

<!-- b000556 | prose | pages [31] -->
def inrange(x1, y1, x0, y0, r):

<!-- b000557 | prose | pages [31] -->
return (x1-x0)**2 + (y1-y0)**2 < r**2

<!-- b000558 | prose | pages [31] -->
city_img = io.imread(’city.png’, as_grey=True) range_img = io.imread(’range.png’, as_grey=True) road_img = io.imread(’road.png’, as_grey=True) hospital_img = io.imread(’hospital.png’, as_grey=True) range2_img = io.imread(’range2.png’, as_grey=True)

<!-- b000559 | prose | pages [31] -->
for i in range(800):

<!-- b000560 | prose | pages [31] -->
for j in range(2000):

<!-- b000561 | prose | pages [31] -->
city_img[i//5][j//5] = min(city_img[i][j], city_img[i//5][j//5]) range_img[i//5][j//5] = min(range_img[i][j], range_img[i//5][j//5]) range2_img[i//5][j//5] = min(range2_img[i][j], range2_img[i//5][j//5]) road_img[i//5][j//5] = min(road_img[i][j], road_img[i//5][j//5]) hospital_img[i//5][j//5] = min(hospital_img[i][j], hospital_img[i//5][j//5]) for i in range(160):

<!-- b000562 | prose | pages [31] -->
for j in range(400):

<!-- b000563 | furniture | pages [32] -->
Team # 1908904

<!-- b000564 | furniture | pages [32] -->
Page 29 of 30

<!-- b000565 | prose | pages [32] -->
if (range_img[i][j] != 1.0):

<!-- b000566 | prose | pages [32] -->
area.add( (i,j) ); if (range2_img[i][j] != 1.0):

<!-- b000567 | prose | pages [32] -->
area2.add( (i,j) ); if (hospital_img[i][j] != 1.0):

<!-- b000568 | prose | pages [32] -->
hospital.append((i,j))

<!-- b000569 | prose | pages [32] -->
print(hospital)

<!-- b000570 | prose | pages [32] -->
road_w = [[0] * 400 for i in range(160)] city_w = [[0] * 400 for i in range(160)]

<!-- b000571 | prose | pages [32] -->
def getPosition(area):

<!-- b000572 | prose | pages [32] -->
mean_road = 0 mean_city = 0 for (x0, y0) in area:

<!-- b000573 | prose | pages [32] -->
i1 = round(max(x0-r, 0)) i2 = round(min(x0+r,160)) i3 = round(max(y0-r, 0)) i4 = round(min(y0+r,400)) for x1 in range(i1,i2):

<!-- b000574 | prose | pages [32] -->
for y1 in range(i3,i4):

<!-- b000575 | prose | pages [32] -->
if (inrange(x1, y1, x0, y0, r)):

<!-- b000576 | prose | pages [32] -->
if (road_img[x1][y1] < 0.5):

<!-- b000577 | prose | pages [32] -->
road_w[x1][y1] += 1 mean_road += 1 road_img[x1][y1] = 1.0 if (city_img[x1][y1] != 1.0):

<!-- b000578 | prose | pages [32] -->
city_w[x1][y1] += 1 mean_city += 1 city_img[x1][y1] = 1.0 mean_road /= len(area) mean_city /= len(area) maxn = 0 maxx = 0 maxy = 0 for (x0, y0) in area:

<!-- b000579 | prose | pages [32] -->
if (road_w[x0][y0] * 0.4 / mean_road + city_w[x0][y0] * 0.6 / mean_city > maxn):

<!-- b000580 | prose | pages [32] -->
maxn = road_w[x0][y0] * 0.4 / mean_road + city_w[x0][y0] * 0.6 / mean_city maxx = x0 maxy = y0 print(18.47-(maxx-hospital[0][0])/51*0.25) print(-66.73+(maxy-hospital[0][1])/133*0.67) return (maxx, maxy)

<!-- b000581 | prose | pages [32] -->
(maxx,maxy) = getPosition(area)

<!-- b000582 | prose | pages [32] -->
i1 = round(max(maxx-round(42.5 / 0.10377) // 5, 0)) i2 = round(min(maxx+round(42.5 / 0.10377) // 5,160)) i3 = round(max(maxy-round(42.5 / 0.10377) // 5, 0)) i4 = round(min(maxy+round(42.5 / 0.10377) // 5,400)) for x1 in range(i1,i2):

<!-- b000583 | prose | pages [32] -->
for y1 in range(i3,i4):

<!-- b000584 | furniture | pages [33] -->
Team # 1908904

<!-- b000585 | furniture | pages [33] -->
Page 30 of 30

<!-- b000586 | prose | pages [33] -->
if (inrange(x1, y1, hospital[0][0], hospital[0][1], r) and inrange(x1,y1, maxx, ma

<!-- b000587 | prose | pages [33] -->
area3.add((x1, y1))

<!-- b000588 | prose | pages [33] -->
getPosition(area3)

<!-- b000589 | prose | pages [33] -->
getPosition(area2)
