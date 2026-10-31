# P-B-2019-1923964-678ee565

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
1923964

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

<!-- b000014 | prose | pages [1] -->
B

<!-- b000015 | heading | pages [1] -->
2019 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000016 | prose | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000017 | title | pages [1] -->
Go Safe with Drones

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | prose | pages [1] -->
We use Dijkstra Algorithm and Particle Swarm Optimization (PSO) to develop a set of models which can solve for a universally practicable DroneGo disaster response system.

<!-- b000020 | prose | pages [1] -->
Before model construction, we make some basic assumptions essential to further analyses. To model reasonably and effectively, we deﬁne three computable optimiza- tion objectives.

<!-- b000021 | prose | pages [1] -->
First, we rebuild a three-dimensional map by interpolation with intensive data col- lection. Deriving an equation of ﬂying time versus payload and the pattern of onboard cameras’ scanning, we pay attention to the models’ authenticity.

<!-- b000022 | prose | pages [1] -->
Next, we design an optimization model for delivery to minimize the total deliv- ering time. Adopting Optimal Combination Algorithm (OCA), we provide a detailed and universal solving strategy to identify the best locations. Moreover, Dijkstra Al- gorithm is applied to derive the drones’ three-dimensional delivery routes. To design the reconnaissance model, we creatively transform the evaluation problem of road seg- ments to the evaluation of settlements. This easy-to-practice model reduces the prob- lem’s complexity remarkably. General importance, a quantiﬁable index, is introduced for evaluation. Then we use improved PSO algorithm to identify the best reconnais- sance area.

<!-- b000023 | prose | pages [1] -->
Based on two models above, we build a combined model to address multi-objective optimization problems. Different weights of objectives are introduced according to speciﬁc scenarios. Provided the weights, we can solve for optimal results.

<!-- b000024 | prose | pages [1] -->
In addition, we apply our models to Haiti’s earthquake in 2010 to test the prac- ticability and effectiveness. The predicted locations of containers are approximately overlapped with the relief centers at that time, which demonstrates our models’ uni- versality. Furtherly, we conceive a more comprehensive model including the factors of weather conditions and the extent of damage.

<!-- b000025 | prose | pages [1] -->
Finally, we conduct sensitivity analyses and prove our models to be quite robust against the changes in the method of assigning settlement’s importance.

<!-- b000026 | heading | pages [2] -->
Contents

<!-- b000027 | contents | pages [2] -->
1

<!-- b000028 | heading | pages [2] -->
Introduction

<!-- b000029 | prose | pages [2] -->
3 Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000030 | prose | pages [2] -->
2

<!-- b000031 | heading | pages [2] -->
Assumptions and Justiﬁcations

<!-- b000032 | prose | pages [2] -->
3

<!-- b000033 | prose | pages [2] -->
4 General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 Assumptions of Delivering Supplies . . . . . . . . . . . . . . . . . . . . . 2.2 2.3 Assumptions of Reconnaissance

<!-- b000034 | prose | pages [2] -->
3

<!-- b000035 | heading | pages [2] -->
Notations

<!-- b000036 | prose | pages [2] -->
4

<!-- b000037 | heading | pages [2] -->
Model Preparations

<!-- b000038 | prose | pages [2] -->
5 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | prose | pages [2] -->
5

<!-- b000040 | prose | pages [2] -->
5

<!-- b000041 | prose | pages [2] -->
6 Reconstruction of 3-Dimensional Topographic Map 4.1 . . . . . . . . . . . .

<!-- b000042 | prose | pages [2] -->
6 Flight Time under Different Payload . . . . . . . . . . . . . . . . . . . . . 4.2 7 Pattern of Onboard Camera Scanning 4.3

<!-- b000043 | prose | pages [2] -->
5

<!-- b000044 | heading | pages [2] -->
Models

<!-- b000045 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000046 | prose | pages [2] -->
7

<!-- b000047 | prose | pages [2] -->
8 Model of Delivering Supplies . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 8 Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.1 8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.2 Models Design 8 A Possible Package Conﬁguration . . . . . . . . . . . . . . . . . . 5.1.3 10 Model of Reconnaissance . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 11 Importance Level of the Settlements . . . . . . . . . . . . . . . . . 5.2.1 11 Importance Level of the Roads . . . . . . . . . . . . . . . . . . . . 5.2.2 12 Model Solving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 13 Combined Model of Delivering Supplies and Reconnaissance 5.3 . . . . . .

<!-- b000048 | prose | pages [2] -->
14 Best Locations and Packing Conﬁgurations . . . . . . . . . . . . . 5.3.1 15 Delivery Routes and Schedule 5.3.2 . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | prose | pages [2] -->
16 Payload Packing Conﬁgurations . . . . . . . . . . . . . . . . . . . 5.3.3 17 Flight Plan to Access Major Roads . . . . . . . . . . . . . . . . . . 5.3.4

<!-- b000050 | prose | pages [2] -->
6

<!-- b000051 | heading | pages [2] -->
Applying of Models

<!-- b000052 | prose | pages [2] -->
7

<!-- b000053 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000054 | prose | pages [2] -->
7.1 Importance Level of Settlements

<!-- b000055 | prose | pages [2] -->
17

<!-- b000056 | prose | pages [2] -->
18

<!-- b000057 | prose | pages [2] -->
18 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | prose | pages [2] -->
18 Assigning Methods of Importance . . . . . . . . . . . . . . . . . . 7.1.1 19 Underestimation of Some Settlements’ Importance 7.1.2 . . . . . . . .

<!-- b000059 | prose | pages [2] -->
19 Drones’ Maximum Navigation Radius . . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000060 | prose | pages [2] -->
8

<!-- b000061 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000062 | prose | pages [2] -->
19

<!-- b000063 | prose | pages [2] -->
20 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 Weaknesses

<!-- b000064 | prose | pages [2] -->
9

<!-- b000065 | heading | pages [2] -->
Future Work

<!-- b000066 | heading | pages [2] -->
10 Conclusions

<!-- b000067 | heading | pages [2] -->
11 Appendix

<!-- b000068 | heading | pages [2] -->
References

<!-- b000069 | references | pages [2] -->
21

<!-- b000070 | references | pages [2] -->
21

<!-- b000071 | references | pages [2] -->
21

<!-- b000072 | references | pages [2] -->
22

<!-- b000073 | furniture | pages [3] -->
Team # 1923964

<!-- b000074 | furniture | pages [3] -->
Page 1 of 23

<!-- b000075 | heading | pages [3] -->
Memo

<!-- b000076 | prose | pages [3] -->
Dear CEO of Help, Inc.:

<!-- b000077 | prose | pages [3] -->
Never in the ﬁeld of history are so many natural disasters faced by human-beings. We do appreciate Help, Inc.’s contribution to the recovery of Puerto Rico and it is out of our sincere hope that DroneGo system be enhanced. In response to your questions about the optimal design of DroneGo system in different scenarios, we are writing to inform you of our work of modelling.

<!-- b000078 | prose | pages [3] -->
We discuss your optimization objectives in different scenarios. With an urgent de- mand for medical resources, your only optimization objective is to minimize total time for delivering medical packages. In this case, we recommend you to apply our delivery model. This model uses Dijkstra Algorithm to solve for optimal locations of containers that minimize the total delivery time.

<!-- b000079 | prose | pages [3] -->
If the need of reconstructing road networks overwhelms medical demand, recon- noitering as many major roads as possible will be your single optimization objective. Acknowledging this, our reconnaissance model will suit you well. This model uses Particle Swarm Optimization(PSO) to solve for containers’ best locations which maxi- mize the total value of all roads reconnoitered.

<!-- b000080 | prose | pages [3] -->
In reality, medical demand and the need of reconstruction are both of great impor- tance. Sometimes your medical packages supply fails to meet the demand. This kind of problem should be solved by our combined multi-objective optimization model. Ac- tually, each objective will have a speciﬁc weight. These weights are to be determined according to speciﬁc scenarios. With given weights, our combined model will solve for best locations of containers and optimal packing conﬁguration, along with ﬂight plan and delivery routes.

<!-- b000081 | prose | pages [3] -->
Our most creative work is that we ﬁnd a both practical and convenient way to de- ﬁne each road’s importance level. We divide each road into segments. A segment is the indivisible part of a road, which connects two settlements without crossing another settlement. Each segment’s importance level is determined by the sum of the impor- tance levels of the two settlements located on its two endpoints.

<!-- b000082 | prose | pages [3] -->
We use general importance to express a settlement’s importance level. General importance is the sum of self importance and connective importance. We score each settlement’s self importance according to its scale. We deﬁne a settlement’s neighbor- ing settlements as the other settlements connected to it by a single segment. Then each settlement’s connective importance is the sum of self importance of all its neighboring settlements.

<!-- b000083 | prose | pages [3] -->
Following this rationale, we successfully transformed the importance of road into importance of settlement. Intuitively, a road with higher importance level will be of greater value. Therefore, to maximize the total value of roads reconnoitered, we can simply maximize the total value of settlements of all the roads reconnoitered.

<!-- b000084 | prose | pages [3] -->
In consideration of Puerto Ricos scenario, our models derive the results as follows. Locations of container 1, 2 that minimize total delivery time are (18.38, −65.85), (18.31, −66.09) respectively. And container 3 locates in the accessible surroundings of Arecibo. The sign ( , ) denotes ( latitude, longitude).

<!-- b000085 | prose | pages [3] -->
Locations of containers that maximize the total importance value of roads recon-

<!-- b000086 | furniture | pages [4] -->
Team # 1923964

<!-- b000087 | furniture | pages [4] -->
Page 2 of 23

<!-- b000088 | prose | pages [4] -->
noitered are (18.36, −65.85) for container 1, (18.27, −66.12) for container 2 and (18.23, -66.76) for container 3.

<!-- b000089 | prose | pages [4] -->
Now consider multi-objective optimization situation. In Puerto Rico scenario, sim- ple calculation shows that the medical packages’ supply can easily meet the demand over 1 year. Therefore, we do not need to worry about the amount of medical packages. Besides, computer process shows that every point in the feasible region of delivery pos- sesses very similar total delivery time. Thus, minimizing total delivery time is not the major optimization objective. We just need to ﬁnd the locations that maximize total importance value of roads reconnoitered in the feasible region. The model’s results are as follows.

<!-- b000090 | prose | pages [4] -->
Best locations of containers (18.36, −65.85) for container 1, (18.27, −66.12) for con-

<!-- b000091 | prose | pages [4] -->
tainer 2 and (18.23, −66.76) for container 3.

<!-- b000092 | prose | pages [4] -->
Flight plan and routes A drone F will deliver supplies between Bayamon and San

<!-- b000093 | prose | pages [4] -->
Pablo, while a drone B between San Juan and Fajardo. Besides, each of the three drone B’s will navigate in one of the three reconnaissance areas, observing roads from close to far away.

<!-- b000094 | prose | pages [4] -->
Packing conﬁgurations of the drones Our drone ﬂeet consists of drone B and drone

<!-- b000095 | prose | pages [4] -->
F. We pack all the medical packages required by a certain destination each day into a single parcel. Therefore, each drone’s payload packing conﬁguration is the corresponding parcel required by each city.

<!-- b000096 | prose | pages [4] -->
Conﬁgurations of containers Container 1 includes 1908 MED 1, 954 MED 2 and 954

<!-- b000097 | prose | pages [4] -->
MED 3. Container 2: includes 1224 MED 1, 306 MED 2 and 918 MED 3. Container 3 includes 3720 MED 1.

<!-- b000098 | prose | pages [4] -->
Before you get to apply our models, here are things worth your attention. First, sensitivity tests show that our models will not be affected too much by methods of as- signing importance but will be considerably impacted by the individual changes of im- portance. Therefore, to ensure effectiveness, you need to correctly rank all settlements’ importance levels. The way of assigning importance levels is not much important as long as the order of levels is correct. Second, the variation of navigation radius make inﬂuence on the best locations. So you need to identify the actual navigation radius of drones.

<!-- b000099 | prose | pages [4] -->
In conclusion, From an overall perspective, we separate the problem into two mis- sions and establish models for them respectively. For the overall design, we focus on the reality by considering three practicable factors. For the design of two individual models, we pay more attention to the practicability by sorting out the feasible groups of destinations, introducing segments and importance evaluation function. The com- bination of the two models is natural and derives the comprehensive results including the ﬂeets’ composition, each drone’s payload conﬁgurations, delivery route, schedule and ﬂight plan as well as the containers’ best locations and packing conﬁgurations.

<!-- b000100 | prose | pages [4] -->
Thank you again for considering our models and hope our models will be of help to your cause!

<!-- b000101 | prose | pages [4] -->
Yours Sincerely,

<!-- b000102 | furniture | pages [4] -->
Team #1923964

<!-- b000103 | furniture | pages [5] -->
Team # 1923964

<!-- b000104 | furniture | pages [5] -->
Page 3 of 23

<!-- b000105 | prose | pages [5] -->
1

<!-- b000106 | heading | pages [5] -->
Introduction

<!-- b000107 | prose | pages [5] -->
The sudden attack of the savage hurricane on Puerto Rico in 2017 caused immea- surable loss of lives and property. It must be depressing to witness the devastating power of the storm surge and wave action brought by the hurricane. The only comfort that can convey strengths and conﬁdence to the inhabitants is the adequate and timely assistance from the outside world, which makes our work meaningful in the future.

<!-- b000108 | prose | pages [5] -->
Due to the serious damage of infrastructures including roads, poles and transmis- sion lines, the inhabitants are probably in short of transportation and electricity, which insulates them entirely from the emergency teams. In addition, the unclearness of the inside damage retards the rescuing progress. Thus, we must utilize the drones of high mobility to deliver indispensable supplies as well as implement reconnaissance for the next-step ground transportation. Lives are suffering with seconds elapsing, so the res- cuing work must hurry!

<!-- b000109 | prose | pages [5] -->
1.1

<!-- b000110 | heading | pages [5] -->
Problem Restatement

<!-- b000111 | prose | pages [5] -->
We need to develop a disaster relief response system named DroneGo Fleet and im- prove its response capabilities based on the situations of Puerto Rico in 2017.

<!-- b000112 | prose | pages [5] -->
• What we Know:

<!-- b000113 | prose | pages [5] -->
– 5 different destinations

<!-- b000114 | prose | pages [5] -->
– Complete geographic information of Puerto Rico

<!-- b000115 | prose | pages [5] -->
• What we Have:

<!-- b000116 | prose | pages [5] -->
– 7 kinds of drones (A-G) with their sizes, performances and conﬁgurations

<!-- b000117 | prose | pages [5] -->
capabilities as well as a tethered equipment (H)

<!-- b000118 | prose | pages [5] -->
– 3 kinds of pre-packaged medical supplies with their size

<!-- b000119 | prose | pages [5] -->
– 3 ISO standard dry cargo containers with given sizes

<!-- b000120 | prose | pages [5] -->
• What we Should Do

<!-- b000121 | heading | pages [5] -->
1. Arrange the ﬂight. For single objective of delivering supplies, select speciﬁc

<!-- b000122 | prose | pages [5] -->
drones and design the packing conﬁgurations for up to 3 cargo containers.

<!-- b000123 | heading | pages [5] -->
2. Identify the best locations. Cargo containers can be set here for drones to

<!-- b000124 | prose | pages [5] -->
achieve the optimal effect of both delivering and reconnoitring targets.

<!-- b000125 | heading | pages [5] -->
3. Propose dispatching schedule. Assign payload packing conﬁgurations, de-

<!-- b000126 | prose | pages [5] -->
livery routes separately and ﬂight plan to each type of drones.

<!-- b000127 | prose | pages [5] -->
1.2 Our Work

<!-- b000128 | prose | pages [5] -->
In our paper, we establish three models to solve the problem. Starting from sim- plicity, we consider delivery and reconnaissance separately and design two single- objective optimization models. To achieve a comprehensive solution, we combine the two models as a multi-objective optimization model.

<!-- b000129 | prose | pages [5] -->
To make models close to reality, we take several practical factors into account. They are

<!-- b000130 | furniture | pages [6] -->
Team # 1923964

<!-- b000131 | furniture | pages [6] -->
Page 4 of 23

<!-- b000132 | caption | pages [6] -->
Figure 1: Solving strategy

<!-- b000133 | prose | pages [6] -->
• The inﬂuence of the hilly topography whose surface is mostly uneven;

<!-- b000134 | prose | pages [6] -->
• The inﬂuence of payload on the drones’ navigation radius;

<!-- b000135 | prose | pages [6] -->
• The inﬂuence of the scanning pattern of onboard cameras.

<!-- b000136 | prose | pages [6] -->
A crucial problem is discussed in the paper about how to evaluate the effectiveness of reconnaissance. To make it clear, we introduce importance level of settlements and segments (the smallest compartments of roads) and an importance evaluation function.

<!-- b000137 | prose | pages [6] -->
Since the response system is developed for the potential future crisis, we apply our model to another island country. The application shows that our models are meaning- ful and universal.

<!-- b000138 | prose | pages [6] -->
For sensitivity analysis, we vary the parameters including the importance levels and the drones’ navigation radius and derive corresponding results. The tests and comparisons demonstrate the robustness of our models.

<!-- b000139 | prose | pages [6] -->
2

<!-- b000140 | heading | pages [6] -->
Assumptions and Justiﬁcations

<!-- b000141 | prose | pages [6] -->
2.1

<!-- b000142 | heading | pages [6] -->
General Assumptions

<!-- b000143 | prose | pages [6] -->
• The economic expenses are almost ﬁxed.

<!-- b000144 | prose | pages [6] -->
Because of the ﬁxed number of containers and the deﬁnite requirement of minimizing the used space of each container, the total cost on materials is almost ﬁxed.

<!-- b000145 | prose | pages [6] -->
• Compared to the materials’ cost, the ﬂying cost is negligible.

<!-- b000146 | prose | pages [6] -->
A previous study in Lesotho indicated that each trip cost only 24 cents while the cost on base stations and drones are $900,000.[12]

<!-- b000147 | prose | pages [6] -->
• All drones are equipped with an ample number of batteries.

<!-- b000148 | prose | pages [6] -->
• All drones have to return to corresponding containers for battery replacement after each ﬂight.

<!-- b000149 | prose | pages [6] -->
The above two assumptions are based on that most searching and rescuing drones are powered by electricity.[1] This is a compulsory condition because of the lack of power throughout the disaster area.

<!-- b000150 | prose | pages [6] -->
• The volume and mass of batteries are ignored.

<!-- b000151 | prose | pages [6] -->
• The feasible response region of the drones is large enough to cover the entire island.

<!-- b000152 | furniture | pages [7] -->
Team # 1923964

<!-- b000153 | furniture | pages [7] -->
Page 5 of 23

<!-- b000154 | prose | pages [7] -->
This requirement is practicable since the control radius of the drones of industrial grade can reach about 30km[2], which is larger than their maximum navigation radius dis- cussed in Subsection 4.2.

<!-- b000155 | prose | pages [7] -->
• People can load or download the drones’ packages in every delivering task.

<!-- b000156 | prose | pages [7] -->
• The time of drones’ ascending and descending is ignored.

<!-- b000157 | prose | pages [7] -->
This is because the drones cannot ﬂy over 120m.[8] The maximum ascending speed is about 5m/s.[13]

<!-- b000158 | prose | pages [7] -->
• The inﬂuence area of each distribution centre is almost a circle determined by the drones’ navigation radius.

<!-- b000159 | prose | pages [7] -->
2.2

<!-- b000160 | heading | pages [7] -->
Assumptions of Delivering Supplies

<!-- b000161 | prose | pages [7] -->
• The longer the drones stay in the air, the greater the probability of failure is.

<!-- b000162 | prose | pages [7] -->
Flying task is of great risk because of the complex terrains and the changeful tropical climate in Puerto Rico. More speciﬁcally, the working time of each aerial mission obeys exponential distribution.

<!-- b000163 | prose | pages [7] -->
• For safety considerations, the government should be able to transport as many medical packages to the disaster-stricken area as possible.

<!-- b000164 | prose | pages [7] -->
2.3

<!-- b000165 | heading | pages [7] -->
Assumptions of Reconnaissance

<!-- b000166 | prose | pages [7] -->
In addition to all the assumptions above, we hypothesize

<!-- b000167 | prose | pages [7] -->
• The vegetation height does not hinder the camera’s photographic effect.

<!-- b000168 | prose | pages [7] -->
Compared to the ﬂight attitude that can reach over 120m, the height of the dominant shrub layer (usually 6-10m) can be ignored.[7][8]

<!-- b000169 | prose | pages [7] -->
• The time consumed for the onboard cameras’ rotating is ignored.

<!-- b000170 | prose | pages [7] -->
3

<!-- b000171 | heading | pages [7] -->
Notations

<!-- b000172 | prose | pages [7] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000173 | furniture | pages [8] -->
Team # 1923964

<!-- b000174 | furniture | pages [8] -->
Page 6 of 23

<!-- b000175 | caption | pages [8] -->
Table 1: Notations

<!-- b000176 | prose | pages [8] -->
Symbol Deﬁnition

<!-- b000177 | prose | pages [8] -->
T0 Maximum ﬂight time with no cargo Tf Maximum ﬂight time with full cargo v Flying speed of the drones H Flying height of the drones r Maximum navigation radius R Maximum scanning radius of onboard cameras A Distance Matrix E(·) Importance evaluation function si Self importance of settlement i ci Connective importance of settlement i gi General importance of settlement i

<!-- b000178 | prose | pages [8] -->
4

<!-- b000179 | heading | pages [8] -->
Model Preparations

<!-- b000180 | prose | pages [8] -->
4.1 Reconstruction of 3-Dimensional Topographic Map

<!-- b000181 | prose | pages [8] -->
To make calculations close to real circumstances, especially when Puerto Rico lo- cates on a hilly island, we should take the uneven ground into consideration.

<!-- b000182 | prose | pages [8] -->
We sample over 110 discrete data points from Google Maps of Puerto Rico and use interpolation to simulate the topography by Matlab.[3]

<!-- b000183 | caption | pages [8] -->
Figure 2: The 3-dimensional map of Puerto Rico

<!-- b000184 | prose | pages [8] -->
Interpolation generates a large number of grids and identiﬁes their altitude ordi- nates. These discrete points are dense enough to rebuild the 3-dimensional map.

<!-- b000185 | prose | pages [8] -->
Instead of deriving geodesic curve, we use Dijkstra algorithm to calculate the min- imum distance between any two points on the land surface. Thus, the ﬂying distance can be determined more accurately and realistically than the 2-dimentional situations.

<!-- b000186 | furniture | pages [9] -->
Team # 1923964

<!-- b000187 | furniture | pages [9] -->
Page 7 of 23

<!-- b000188 | prose | pages [9] -->
Flight Time under Different Payload 4.2

<!-- b000189 | prose | pages [9] -->
Since the ﬂight time decreases as the drone’s payload increases, we should realize that reaching the same distance, each ﬂight should have different time consumed on the delivering trip and the returning trip.

<!-- b000190 | prose | pages [9] -->
We select points from the working curves (see in Appendix [4]) and ﬁt them into negative exponential function

<!-- b000191 | prose | pages [9] -->
T = T0e−λb (1)

<!-- b000192 | prose | pages [9] -->
where T refers to ﬂight time while b refers to the payload in unit of lbs. We derive sequently

<!-- b000193 | prose | pages [9] -->
T = 29.23e−0.08498b

<!-- b000194 | prose | pages [9] -->
T = 34.63e−0.08187b

<!-- b000195 | prose | pages [9] -->
T = 37.80e−0.07689b

<!-- b000196 | prose | pages [9] -->
r = −0.9981

<!-- b000197 | prose | pages [9] -->
r = −0.9992

<!-- b000198 | prose | pages [9] -->
r = −0.9989

<!-- b000199 | prose | pages [9] -->
for the three working curves lower in the ﬁgure. We assume that λ is a function of T0, and then we derive λ of different T0 given in problem by spline interpolation from the above data. Substituting λ, T0 and maximum payload b into eqn(4.2), we get Tf for each type of drones.

<!-- b000200 | prose | pages [9] -->
Just to be safe, we choose maximum ﬂight time with full cargo to calculate the maximum navigation radius. As described in assumptions, the drones have to return back after each delivering, so radius r = v × Tf/2, which is shown in the table below.

<!-- b000201 | caption | pages [9] -->
Table 2: Navigation radius of different types of the drones

<!-- b000202 | prose | pages [9] -->
T0(min) Drone Speed(km/h)

<!-- b000203 | prose | pages [9] -->
A 40 35 B 79 40 C 64 35 D 60 18 E 60 15 F 79 24 G 64 16

<!-- b000204 | prose | pages [9] -->
Maximum Navigation Tf(min) Payload(lbs) Radius(km)

<!-- b000205 | prose | pages [9] -->
34.02 3.5 11.34 37.76 8 24.86 31.23 14 16.66 16.67 11 8.34 13.69 15 6.85 20.06 22 13.21 14.08 20 7.51

<!-- b000206 | prose | pages [9] -->
Pattern of Onboard Camera Scanning 4.3

<!-- b000207 | prose | pages [9] -->
The area covered by the onboard camera is determined by the drones’ ﬂight alti- tude, H, as well as the required resolution of picture.

<!-- b000208 | prose | pages [9] -->
Let θ be the camera lens’ angle of view, and α be the angle between vertical line and the angular bisector of θ. α actually signiﬁes the direction that camera points towards. Since the camera can rotate and point towards a number of directions, the covering area is a circle with a radius of R. Obviously, as α increases, the covering area increases. However, the requirement of high resolution limit the maximum detectable distance. From technical instruction, we use the following equation to calculate.[10]

<!-- b000209 | prose | pages [9] -->
(Field of View(FOV)

<!-- b000210 | prose | pages [9] -->
Sensor Resolution = Image Resolution = 2

<!-- b000211 | prose | pages [9] -->
Smallest Feature

<!-- b000212 | furniture | pages [10] -->
Team # 1923964

<!-- b000213 | furniture | pages [10] -->
Page 8 of 23

<!-- b000214 | caption | pages [10] -->
Figure 3: The illustration of onboard camera scanning

<!-- b000215 | prose | pages [10] -->
From Figure 3, we derive

<!-- b000216 | prose | pages [10] -->
FOV + H tan(α −θ/2) = H tan(α + θ/2)

<!-- b000217 | prose | pages [10] -->
R = H tan(α + θ/2)

<!-- b000218 | prose | pages [10] -->
For pictures with 1080p whose resolution is 1920×1080, we choose the smaller value 1080 as the sensor resolution. We set smallest feature as 5 metres, the mean width of roads on Puerto Rico, and H as 120 metres, the US legal altitude of drones.[11]

<!-- b000219 | prose | pages [10] -->
From four kinds of commercially available DJI drones, we set θ as 72◦.[9]

<!-- b000220 | prose | pages [10] -->
Thus, we get α = 51.5◦, R = 2.75km.

<!-- b000221 | prose | pages [10] -->
5

<!-- b000222 | heading | pages [10] -->
Models

<!-- b000223 | prose | pages [10] -->
5.1

<!-- b000224 | heading | pages [10] -->
Model of Delivering Supplies

<!-- b000225 | prose | pages [10] -->
In this part, our single purpose is to deliver medical supplies.

<!-- b000226 | prose | pages [10] -->
5.1.1 Analysis

<!-- b000227 | prose | pages [10] -->
The problem requires us to recommend a composition of the drone ﬂeet and pro- vide the best locations for containers. Obviously, the two requirements are not inde- pendent. For each possible location, there may exist an optimal composition of the drones. Thus, it is a multi-objective optimization problem. Hoping to obtain the opti- mal solution, we are going to transform it into a single-objective optimization problem. Here, we construct the objective function as the total ﬂight time.

<!-- b000228 | prose | pages [10] -->
5.1.2

<!-- b000229 | heading | pages [10] -->
Model Design

<!-- b000230 | prose | pages [10] -->
Assume that there is a number n of destinations, a number m of kinds of drones and a number l of cargo containers.

<!-- b000231 | furniture | pages [11] -->
Team # 1923964

<!-- b000232 | furniture | pages [11] -->
Page 9 of 23

<!-- b000233 | prose | pages [11] -->
Here we have essential preparation works for models design.

<!-- b000234 | prose | pages [11] -->
For a given set of destinations, we derive a Distance Matrix A= (aij)n×n, where aij is the distance between destination i and destination j.

<!-- b000235 | prose | pages [11] -->
We construct a Destinations Combination Matrix B. It is a 0-1 matrix. Let each of its rows represent a combination of destinations. Thus, there are 2n −1 rows1 and n columns.

<!-- b000236 | prose | pages [11] -->
{ 0 if destination j does not exist in the combination i

<!-- b000237 | prose | pages [11] -->
bij =

<!-- b000238 | prose | pages [11] -->
1 if destination j exists in the combination i

<!-- b000239 | prose | pages [11] -->
i = 1, 2, · · · , 2n −1 αi = (bi1, bi2, · · · , bin)

<!-- b000240 | prose | pages [11] -->
αi denotes a row vector of B.

<!-- b000241 | prose | pages [11] -->
Similarly, we construct a Drones Combination Matrix D. βj(j = 1, 2, · · · , 2m−1) is a row vector of D

<!-- b000242 | prose | pages [11] -->
Deﬁnition 1. If all drones included in a speciﬁc combination βj are able to arrive at all destinations included in a speciﬁc combination αi, then there exists a corresponding relationship between βj and αi

<!-- b000243 | prose | pages [11] -->
Deﬁnition 2. If for αi and αj, there not exists integer k from 1 to n to make bik = bjk = 1, then αi∩αj=∅.

<!-- b000244 | prose | pages [11] -->
Deﬁnition 3. Group is a combination of row vectors.

<!-- b000245 | prose | pages [11] -->
For example, βi, βj and βk form a group {βi, βj, βk}. Naturally, we have βi∩{βj, βk}= βi∩βj∩βk.

<!-- b000246 | prose | pages [11] -->
Since each αi possibly corresponds to a βj, we construct a mapping f. f(i) = j signiﬁes that αi corresponds to a βj. When there are more than one βj that can satisfy Deﬁnition 1, let f(i) be the subscript of the βj that contains the most drones.

<!-- b000247 | prose | pages [11] -->
With all the above preparation works, we give a strategy to solve the problem.

<!-- b000248 | prose | pages [11] -->
Procedure 1: Sort out the isolated destinations

<!-- b000249 | prose | pages [11] -->
Check whether there exists the destinations whose distances from all other desti- nations exceed the largest maximum ﬂight radius of all available drones. If there exists, assign an individual container for each of them.

<!-- b000250 | prose | pages [11] -->
Procedure 2: Find out all possible groups

<!-- b000251 | prose | pages [11] -->
Step 0 Let i=1.

<!-- b000252 | prose | pages [11] -->
Step 1 For any k̸ = i, examine whether αk∩{αi}=∅. If yes, add αk into the

<!-- b000253 | prose | pages [11] -->
group {αi} to get {αi, αk} and make l = l −1.

<!-- b000254 | prose | pages [11] -->
Step 2 Judgement:

<!-- b000255 | prose | pages [11] -->
If ∑

<!-- b000256 | prose | pages [11] -->
αi∈group αj = (1, 1, · · · , 1

<!-- b000257 | prose | pages [11] -->
) and l ≥0, and there is no such a group

<!-- b000258 | prose | pages [11] -->
| {z } all 1

<!-- b000259 | prose | pages [11] -->
before, keep the group in reserve. Let i = i + 1, back to Step 1.

<!-- b000260 | prose | pages [11] -->
If ∑

<!-- b000261 | prose | pages [11] -->
αi∈group αj̸ = (1, 1, · · · , 1

<!-- b000262 | prose | pages [11] -->
) and l ≥0, back to Step 2.

<!-- b000263 | prose | pages [11] -->
| {z } all 1

<!-- b000264 | prose | pages [11] -->
If i > 2n −1, end and retrieve all possible groups.

<!-- b000265 | prose | pages [11] -->
1This is because ∑n i=1 = 2n −1

<!-- b000266 | furniture | pages [12] -->
Team # 1923964

<!-- b000267 | furniture | pages [12] -->
Page 10 of 23

<!-- b000268 | prose | pages [12] -->
Procedure 3: Derive the optimal point of all possible groups

<!-- b000269 | prose | pages [12] -->
Step 1 For each possible group, using the mapping f to ﬁnd the available βj

<!-- b000270 | prose | pages [12] -->
according to the αi in the group.

<!-- b000271 | prose | pages [12] -->
Step 2 For each pair of αi and βj, utilize Greedy strategy to allocate different

<!-- b000272 | prose | pages [12] -->
drones to the required air lines and consider the corresponding total ﬂight time as the minimum time of the group.

<!-- b000273 | prose | pages [12] -->
Notice: If for a pair of αi and βj, there is only one element 1 in αi, (there is only

<!-- b000274 | prose | pages [12] -->
one destination in that combination) then selects the drone whose required number of ﬂight is the least and use the equation

<!-- b000275 | prose | pages [12] -->
number of ﬂight needed×maximum ﬂight time

<!-- b000276 | prose | pages [12] -->
2 to calculate the time needed.2

<!-- b000277 | prose | pages [12] -->
Procedure 4: Compare all groups’ optimal point and select the best

<!-- b000278 | prose | pages [12] -->
5.1.3 A Possible Package Conﬁguration

<!-- b000279 | prose | pages [12] -->
As assumptions described before, the drones are equipped with an ample number of batteries. Since ﬂying time is short, we can utilize only one drone to run the air lines between a speciﬁc destination and a speciﬁc container. Denote the container carrying drone B as container 1, the other as container 2, the one assigned to Arecibo as container 3.

<!-- b000280 | prose | pages [12] -->
From estimation we can ﬁnd that if we simply put one B into container 1 and load MED 1 and MED 3 as packages (roughly in the size and shape of 14×7×9 cuboids) vertically into the container, more than 1900 packages of MED 1 and 1900 packages of MED 3 can be loaded into container 1. Under the consuming speed offered in the problem background[5][6], the amount of medical packages can cope with two years consumption. This is totally plausible.

<!-- b000281 | prose | pages [12] -->
In container 2, we pack the medical supplies needed each day (including 2 MED 1,

<!-- b000282 | heading | pages [12] -->
2 MED 2 and 6 MED 3) into a single pile, roughly in the size and shape of a 14×14×20

<!-- b000283 | prose | pages [12] -->
cuboid. The combination of a pile is because container 2 is obliged to give considera- tion to 3 destinations in the meantime. Thus, if we only load one F into container 2, we can load more than 324 piles, which is deﬁnitely enough for Puerto Rico.

<!-- b000284 | prose | pages [12] -->
As for Arecibo, we simply ﬁll the container 3 with a drone B and as many MED 1 as possible.

<!-- b000285 | prose | pages [12] -->
In general, the package conﬁgurations for delivering purpose only are stated as follow.

<!-- b000286 | prose | pages [12] -->
Drone Container Destination Fleet

<!-- b000287 | prose | pages [12] -->
San Juan 1 B

<!-- b000288 | prose | pages [12] -->
Packing Locations Conﬁgurations

<!-- b000289 | prose | pages [12] -->
1908 MED 1 (18.38, −65.85) 954 MED 2, 954 MED 3 Fajardo

<!-- b000290 | prose | pages [12] -->
Bayamon 2 F 1296 MED 1 (18.31, −66.09) 324 MED 2, 972 MED 3 Cauguas

<!-- b000291 | prose | pages [12] -->
3 Arecibo B in the accessible 3720 MED 1 surrounding of Arecibo

<!-- b000292 | prose | pages [12] -->
2This is a compromise. Otherwise, the situation that container should locate deﬁnitely on the desti- nation is contrary to common sense.

<!-- b000293 | furniture | pages [13] -->
Team # 1923964

<!-- b000294 | prose | pages [13] -->
5.2

<!-- b000295 | heading | pages [13] -->
Model of Reconnaissance

<!-- b000296 | furniture | pages [13] -->
Page 11 of 23

<!-- b000297 | prose | pages [13] -->
To make the problem clearer step by step, we establish the model for reconnais- sance purpose only before considering both missions at the same time.

<!-- b000298 | prose | pages [13] -->
The target of video reconnaissance is to report the potential damaged road net- works. One of the optimization objectives is to maximize the effectiveness. We need to make clear what contributes to the effectiveness. Thus, a measurement of the impor- tance of speciﬁc constructions is introduced below.

<!-- b000299 | prose | pages [13] -->
5.2.1 Importance Level of the Settlements

<!-- b000300 | prose | pages [13] -->
Obviously, the larger the scale of a settlement is and the more roads connected it with other settlements, the more important the settlement would be. Thus, a set- tlements importance is combined by self importance, denoted by S and connective importance, denoted by C. The sum of S and C is deﬁned as a settlements general importance, denoted by G.

<!-- b000301 | prose | pages [13] -->
The self importance, S, depends on the city level. We divide all settlements on Puerto Rico into six categories as follow.

<!-- b000302 | prose | pages [13] -->
Number one is the region capital San Juan. Number two is the second largest city in Puerto Rico, Payamon. Number three is district capital, for example Mayaguez. Notice that some intersections of some roads are not settlements at all but simply road crossings. Few people live around these endpoints. We consider these crossings as the ﬁfth kind of settlements. We score ﬁve kinds of settlements with integer scores 1 to 5. The higher the city level is, the higher the score it gets. We denote the following score of city level as individual importance.

<!-- b000303 | prose | pages [13] -->
Example Settlements Categories Self Importance

<!-- b000304 | prose | pages [13] -->
San Juan (Capital) 1 6 Payamon (Second Largest) 2 5 Mayaguez, etc (District Capital) 3 4 Yellow tinted areas 4 3 Small circles areas 5 2

<!-- b000305 | prose | pages [13] -->
Intersection not 6 1 highlighted on map

<!-- b000306 | prose | pages [13] -->
Previous to discussion about connective importance, we need to introduce a Con- nection Matrix to describe the relationship of all settlements.

<!-- b000307 | prose | pages [13] -->
Connection Matrix X is a 0-1 matrix.

<!-- b000308 | prose | pages [13] -->


<!-- b000309 | prose | pages [13] -->
x11

<!-- b000310 | prose | pages [13] -->


<!-- b000311 | prose | pages [13] -->
x21

<!-- b000312 | prose | pages [13] -->


<!-- b000313 | prose | pages [13] -->
X =

<!-- b000314 | prose | pages [13] -->


<!-- b000315 | prose | pages [13] -->
...

<!-- b000316 | prose | pages [13] -->


<!-- b000317 | prose | pages [13] -->


<!-- b000318 | prose | pages [13] -->
· · · x12 x1n

<!-- b000319 | prose | pages [13] -->


<!-- b000320 | prose | pages [13] -->
· · · x22 x2n

<!-- b000321 | prose | pages [13] -->
 

<!-- b000322 | prose | pages [13] -->
... ...

<!-- b000323 | prose | pages [13] -->
...

<!-- b000324 | prose | pages [13] -->


<!-- b000325 | prose | pages [13] -->
· · · xn2 xn1

<!-- b000326 | prose | pages [13] -->
when i = j, xi,j=0 when i̸ = j

<!-- b000327 | prose | pages [13] -->
{ 0

<!-- b000328 | prose | pages [13] -->
xnn

<!-- b000329 | prose | pages [13] -->
if there is no segment connecting settlement i and settlement

<!-- b000330 | prose | pages [13] -->
xi,j =

<!-- b000331 | prose | pages [13] -->
if there is a segment connecting settlement i and settlement 1

<!-- b000332 | furniture | pages [14] -->
Team # 1923964

<!-- b000333 | furniture | pages [14] -->
Page 12 of 23

<!-- b000334 | prose | pages [14] -->
n is the total number of settlements. We sample 46 points in all from the given map and set n = 46. Segment is deﬁned later in Deﬁnition 4.

<!-- b000335 | prose | pages [14] -->
A settlement’s connective importance, C, depends on the other settlements con- nected to it with a segment. We deﬁne connective importance of settlement i as

<!-- b000336 | prose | pages [14] -->
n ∑

<!-- b000337 | prose | pages [14] -->
ci =

<!-- b000338 | prose | pages [14] -->
sjxi,j

<!-- b000339 | prose | pages [14] -->
j=1

<!-- b000340 | prose | pages [14] -->
where sj is the self importance of settlement i.

<!-- b000341 | prose | pages [14] -->
Hence, we derive

<!-- b000342 | prose | pages [14] -->
C = XS

<!-- b000343 | prose | pages [14] -->
where C=(c1, c2, . . . , cn)T is the connective importance vector, S=(s1, s2, . . . , sn)T

<!-- b000344 | prose | pages [14] -->
is the self importance vector.

<!-- b000345 | prose | pages [14] -->
Combining the two aspects of importance, we get general importance.

<!-- b000346 | prose | pages [14] -->
G = S + C = IS + XS = (I + X)S (2)

<!-- b000347 | prose | pages [14] -->
where I is the identity matrix. The physical meaning of the equation is self-evident that general importance depends on settlement itself as well as the surrounding networks. If we use the function E(·) to evaluate the importance of settlement i, then E(i) = gi.

<!-- b000348 | prose | pages [14] -->
5.2.2 Importance Level of the Roads

<!-- b000349 | prose | pages [14] -->
For purpose of ground-based route planning, we need to rank the roads according to their importance. A trip of reconnaissance covering more roads of greater impor- tance would bring more beneﬁt. Thus, we need to deﬁne each roads importance level.

<!-- b000350 | prose | pages [14] -->
First, we need to keep in mind what a road is. Notice that every road on Puerto Rico is divided by the settlements located on it. Therefore, roads are divided by settlements into small segments. The indivisible part of a road is the segment which connects two settlements without crossing another segment. As shown in the ﬁgure below, line segment AB and BC are indivisible parts of road L, while AC is not. Hence, we give an exact deﬁnition of segment.

<!-- b000351 | caption | pages [14] -->
Figure 4: The illustration of segment and road

<!-- b000352 | prose | pages [14] -->
Deﬁnition 4. Segment is the indivisible part of a road, which connects two settlements and not crossing other settlements.

<!-- b000353 | prose | pages [14] -->
Obviously, segments are the minimum compositions of a road. It will be straight- forward and practical to deﬁne each segments importance level and then rank all seg- ments according to the levels. Undoubtedly, segments with higher importance level should be reconnoitered and restored more quickly.

<!-- b000354 | furniture | pages [15] -->
Team # 1923964

<!-- b000355 | furniture | pages [15] -->
Page 13 of 23

<!-- b000356 | prose | pages [15] -->
A segments importance depends on the two settlements it connects. Segments themselves are of little importance. Only if a segment connects two important set- tlements will it become important.

<!-- b000357 | prose | pages [15] -->
We use function E(·) to evaluate importance. For convenience and easiness to comprehend, we derive

<!-- b000358 | prose | pages [15] -->
E(ij) = E(i) + E(j) (3)

<!-- b000359 | prose | pages [15] -->
where ij signiﬁes the segment that connects two settlements i and j.

<!-- b000360 | prose | pages [15] -->
Since E(i) = gi, E(ij) = gi + gj. Therefore, the importance evaluation of seg- ments, the most tiny compartments of roads, is transformed into the importance eval- uation of settlements.

<!-- b000361 | prose | pages [15] -->
By the evaluation introduced above, we abstract the map into the combination of nodes and lines by UCINET, as shown in Figure 6. For settlements whose general importance varies between 4 and 8, we signify them as grey up-triangles. For settle- ments whose general importance varies between 9 and 12, we signify them as yellow diamonds. For settlements whose general importance varies between 13 and 16, we signify them as purple inverted-triangles. For settlements whose general importance varies between 17 and 20, we signify them as red circles. For settlements whose gen- eral importance is larger than 20, we signify them as black tinted areas. The relative sizes of the nodes depend on their absolute value of general importance.

<!-- b000362 | caption | pages [15] -->
Figure 5: The abstract expression of settlements and segments

<!-- b000363 | prose | pages [15] -->
5.2.3

<!-- b000364 | heading | pages [15] -->
Model Solving

<!-- b000365 | prose | pages [15] -->
We hope to identify the best locations for cargo containers. With the previous eval- uation of importance of segments and settlements, we set the objective function Z as the sum of importance of all segments that lie in the covered area of the drones. It can be converted into the function of the general importance of settlements.

<!-- b000366 | prose | pages [15] -->
∑

<!-- b000367 | prose | pages [15] -->
∑

<!-- b000368 | prose | pages [15] -->
E(ij) =

<!-- b000369 | prose | pages [15] -->
Z =

<!-- b000370 | prose | pages [15] -->
ij∈Ω

<!-- b000371 | prose | pages [15] -->
(gi + gj) (4)

<!-- b000372 | prose | pages [15] -->
ij∈Ω

<!-- b000373 | prose | pages [15] -->
where Ωis the drones’ detectable area, a circle determined by their maximum naviga- tion radius r plus scanning radius R.

<!-- b000374 | prose | pages [15] -->
For problem whose independent variables are locations, Particle Swarm Optimiza- tion(PSO) is a good solution.

<!-- b000375 | furniture | pages [16] -->
Team # 1923964

<!-- b000376 | furniture | pages [16] -->
Page 14 of 23

<!-- b000377 | prose | pages [16] -->
Step 0 Initialize a great number of particles in the feasible region. The particles possess

<!-- b000378 | prose | pages [16] -->
3 dimensions including longitude, latitude and velocity.

<!-- b000379 | prose | pages [16] -->
Step 1 Set the feasible region as a circle whose centre is the speciﬁc particle’s location

<!-- b000380 | prose | pages [16] -->
and radius is r + R.

<!-- b000381 | prose | pages [16] -->
Step 2 Identify the settlements locating within the feasible region.

<!-- b000382 | prose | pages [16] -->
Step 3 Identify the connective relationship among the settlements by the connective

<!-- b000383 | prose | pages [16] -->
matrix C.

<!-- b000384 | prose | pages [16] -->
Step 4 Sum up the general importance of the connecting settlements as equation 5.2.3

<!-- b000385 | prose | pages [16] -->
shows.

<!-- b000386 | prose | pages [16] -->
Step 5 Particles adjust their locations and velocity according to their value of Z. Back

<!-- b000387 | prose | pages [16] -->
to Step 1.

<!-- b000388 | prose | pages [16] -->
Finally, most particles would converge to the location where there is the largest value of Z. Thus, we derive the location, from which the drones’ coverage reach the maximum importance.

<!-- b000389 | prose | pages [16] -->
Since drone B possess the largest ﬂight radius among A H, it is the most suitable choice. For the reconnoitring problem across the whole island, we get the result as below.

<!-- b000390 | prose | pages [16] -->
18.5

<!-- b000391 | prose | pages [16] -->
Quebradillas

<!-- b000392 | prose | pages [16] -->
Arecibo

<!-- b000393 | prose | pages [16] -->
Aguadilla

<!-- b000394 | prose | pages [16] -->
18.4

<!-- b000395 | prose | pages [16] -->
Centrol Puntas

<!-- b000396 | prose | pages [16] -->
San Sebastian

<!-- b000397 | prose | pages [16] -->
18.3

<!-- b000398 | prose | pages [16] -->
Lares

<!-- b000399 | prose | pages [16] -->
Utuado

<!-- b000400 | prose | pages [16] -->
Barceloneta

<!-- b000401 | prose | pages [16] -->
Dorado

<!-- b000402 | prose | pages [16] -->
Manati

<!-- b000403 | prose | pages [16] -->
San Juan

<!-- b000404 | prose | pages [16] -->
Unnamed 6

<!-- b000405 | prose | pages [16] -->
Bayamon

<!-- b000406 | prose | pages [16] -->
Rio Grande

<!-- b000407 | prose | pages [16] -->
Corozal

<!-- b000408 | prose | pages [16] -->
Fajardo

<!-- b000409 | prose | pages [16] -->
Aguas Buenas

<!-- b000410 | prose | pages [16] -->
Utuado'

<!-- b000411 | prose | pages [16] -->
Jayuya

<!-- b000412 | prose | pages [16] -->
latitude/°

<!-- b000413 | prose | pages [16] -->
Mayaguez

<!-- b000414 | prose | pages [16] -->
18.2

<!-- b000415 | prose | pages [16] -->
Canstaner

<!-- b000416 | prose | pages [16] -->
Adjuntas

<!-- b000417 | prose | pages [16] -->
Indiera Alta

<!-- b000418 | prose | pages [16] -->
18.1

<!-- b000419 | prose | pages [16] -->
San German

<!-- b000420 | prose | pages [16] -->
Yauco

<!-- b000421 | prose | pages [16] -->
Caguas

<!-- b000422 | prose | pages [16] -->
Comerio

<!-- b000423 | prose | pages [16] -->
Juncos

<!-- b000424 | prose | pages [16] -->
Orocovis

<!-- b000425 | prose | pages [16] -->
Naguabo

<!-- b000426 | prose | pages [16] -->
San Lorenzo

<!-- b000427 | prose | pages [16] -->
Unnamed 4 Unnamed 3

<!-- b000428 | prose | pages [16] -->
Unnamed 1

<!-- b000429 | prose | pages [16] -->
Humacao

<!-- b000430 | prose | pages [16] -->
Unnamed 5

<!-- b000431 | prose | pages [16] -->
Unnamed 2

<!-- b000432 | prose | pages [16] -->
Cayey

<!-- b000433 | prose | pages [16] -->
Coamo

<!-- b000434 | prose | pages [16] -->
Ponce

<!-- b000435 | prose | pages [16] -->
18

<!-- b000436 | prose | pages [16] -->
Cabo Rojo Ensenada

<!-- b000437 | prose | pages [16] -->
17.9

<!-- b000438 | prose | pages [16] -->
-67.4 -67.2 -67 -66.8 -66.6

<!-- b000439 | prose | pages [16] -->
Maunabo

<!-- b000440 | prose | pages [16] -->
Guayama

<!-- b000441 | prose | pages [16] -->
Santa Isabel

<!-- b000442 | prose | pages [16] -->
Punta Figuras

<!-- b000443 | prose | pages [16] -->
-66.4 -66.2 -66 -65.8 -65.6 longtitude/°

<!-- b000444 | caption | pages [16] -->
Figure 6: The global result of Particles Swarm Optimization

<!-- b000445 | prose | pages [16] -->
Another practicable method is exhaustion. By generating a huge number of grids that divide the feasible region into tiny parts, we calculate each point’s value of Z and ﬁnd the maximum among them. The steps are similar to the above and the result is as shown below.

<!-- b000446 | heading | pages [16] -->
Combined Model of Delivering Supplies and Reconnaissance

<!-- b000447 | prose | pages [16] -->
5.3

<!-- b000448 | prose | pages [16] -->
In this part, we combine the two models established in section 5.1 and 5.2, and obtain a comprehensive solution to the problem. Notice that drone F cannot implement

<!-- b000449 | furniture | pages [17] -->
Team # 1923964

<!-- b000450 | furniture | pages [17] -->
Page 15 of 23

<!-- b000451 | caption | pages [17] -->
Figure 7: The global result of exhaustion

<!-- b000452 | prose | pages [17] -->
reconnaissance. We add one drone B to the container that supplies packages for San Pablo and Bayamon.

<!-- b000453 | prose | pages [17] -->
Best Locations and Packing Conﬁgurations 5.3.1

<!-- b000454 | prose | pages [17] -->
18.6

<!-- b000455 | prose | pages [17] -->
18.5

<!-- b000456 | prose | pages [17] -->
Quebradillas

<!-- b000457 | prose | pages [17] -->
Quebradillas

<!-- b000458 | prose | pages [17] -->
Quebradillas

<!-- b000459 | prose | pages [17] -->
Quebradillas

<!-- b000460 | prose | pages [17] -->
Arecibo

<!-- b000461 | prose | pages [17] -->
Arecibo

<!-- b000462 | prose | pages [17] -->
Arecibo

<!-- b000463 | prose | pages [17] -->
Arecibo

<!-- b000464 | prose | pages [17] -->
Barceloneta

<!-- b000465 | prose | pages [17] -->
Barceloneta

<!-- b000466 | prose | pages [17] -->
Barceloneta

<!-- b000467 | prose | pages [17] -->
Barceloneta

<!-- b000468 | prose | pages [17] -->
Aguadilla

<!-- b000469 | prose | pages [17] -->
Aguadilla

<!-- b000470 | prose | pages [17] -->
Aguadilla

<!-- b000471 | prose | pages [17] -->
Aguadilla

<!-- b000472 | prose | pages [17] -->
18.4

<!-- b000473 | prose | pages [17] -->
Centrol Puntas

<!-- b000474 | prose | pages [17] -->
Centrol Puntas

<!-- b000475 | prose | pages [17] -->
Centrol Puntas

<!-- b000476 | prose | pages [17] -->
Centrol Puntas

<!-- b000477 | prose | pages [17] -->
San Sebastian

<!-- b000478 | prose | pages [17] -->
San Sebastian

<!-- b000479 | prose | pages [17] -->
San Sebastian

<!-- b000480 | prose | pages [17] -->
San Sebastian

<!-- b000481 | prose | pages [17] -->
18.3

<!-- b000482 | prose | pages [17] -->
Lares

<!-- b000483 | prose | pages [17] -->
Lares

<!-- b000484 | prose | pages [17] -->
Lares

<!-- b000485 | prose | pages [17] -->
Lares

<!-- b000486 | prose | pages [17] -->
latitude/°

<!-- b000487 | prose | pages [17] -->
Utuado

<!-- b000488 | prose | pages [17] -->
Utuado

<!-- b000489 | prose | pages [17] -->
Utuado

<!-- b000490 | prose | pages [17] -->
Utuado

<!-- b000491 | prose | pages [17] -->
Utuado'

<!-- b000492 | prose | pages [17] -->
Utuado'

<!-- b000493 | prose | pages [17] -->
Utuado'

<!-- b000494 | prose | pages [17] -->
Utuado'

<!-- b000495 | prose | pages [17] -->
Jayuya

<!-- b000496 | prose | pages [17] -->
Jayuya

<!-- b000497 | prose | pages [17] -->
Jayuya

<!-- b000498 | prose | pages [17] -->
Jayuya

<!-- b000499 | prose | pages [17] -->
18.2

<!-- b000500 | prose | pages [17] -->
Mayaguez

<!-- b000501 | prose | pages [17] -->
Mayaguez

<!-- b000502 | prose | pages [17] -->
Mayaguez

<!-- b000503 | prose | pages [17] -->
Mayaguez

<!-- b000504 | prose | pages [17] -->
Canstaner

<!-- b000505 | prose | pages [17] -->
Canstaner

<!-- b000506 | prose | pages [17] -->
Canstaner

<!-- b000507 | prose | pages [17] -->
Canstaner

<!-- b000508 | prose | pages [17] -->
Adjuntas

<!-- b000509 | prose | pages [17] -->
Adjuntas

<!-- b000510 | prose | pages [17] -->
Adjuntas

<!-- b000511 | prose | pages [17] -->
Adjuntas

<!-- b000512 | prose | pages [17] -->
Indiera Alta

<!-- b000513 | prose | pages [17] -->
Indiera Alta

<!-- b000514 | prose | pages [17] -->
Indiera Alta

<!-- b000515 | prose | pages [17] -->
Indiera Alta

<!-- b000516 | prose | pages [17] -->
18.1

<!-- b000517 | prose | pages [17] -->
San German

<!-- b000518 | prose | pages [17] -->
San German

<!-- b000519 | prose | pages [17] -->
San German

<!-- b000520 | prose | pages [17] -->
San German

<!-- b000521 | prose | pages [17] -->
Yauco

<!-- b000522 | prose | pages [17] -->
Yauco

<!-- b000523 | prose | pages [17] -->
Yauco

<!-- b000524 | prose | pages [17] -->
Yauco

<!-- b000525 | prose | pages [17] -->
Ponce

<!-- b000526 | prose | pages [17] -->
Ponce

<!-- b000527 | prose | pages [17] -->
Ponce

<!-- b000528 | prose | pages [17] -->
Ponce

<!-- b000529 | prose | pages [17] -->
18

<!-- b000530 | prose | pages [17] -->
Cabo Rojo

<!-- b000531 | prose | pages [17] -->
Cabo Rojo

<!-- b000532 | prose | pages [17] -->
Cabo Rojo

<!-- b000533 | prose | pages [17] -->
Cabo Rojo

<!-- b000534 | prose | pages [17] -->
Ensenada

<!-- b000535 | prose | pages [17] -->
Ensenada

<!-- b000536 | prose | pages [17] -->
Ensenada

<!-- b000537 | prose | pages [17] -->
Ensenada

<!-- b000538 | prose | pages [17] -->
17.9

<!-- b000539 | prose | pages [17] -->
-67.2 -67 -66.8 -66.6

<!-- b000540 | prose | pages [17] -->
Dorado

<!-- b000541 | prose | pages [17] -->
Dorado

<!-- b000542 | prose | pages [17] -->
Dorado

<!-- b000543 | prose | pages [17] -->
Dorado

<!-- b000544 | prose | pages [17] -->
Manati

<!-- b000545 | prose | pages [17] -->
Manati

<!-- b000546 | prose | pages [17] -->
Manati

<!-- b000547 | prose | pages [17] -->
Manati

<!-- b000548 | prose | pages [17] -->
San Juan

<!-- b000549 | prose | pages [17] -->
San Juan

<!-- b000550 | prose | pages [17] -->
San Juan

<!-- b000551 | prose | pages [17] -->
San Juan

<!-- b000552 | prose | pages [17] -->
Unnamed 6

<!-- b000553 | prose | pages [17] -->
Unnamed 6

<!-- b000554 | prose | pages [17] -->
Unnamed 6

<!-- b000555 | prose | pages [17] -->
Unnamed 6

<!-- b000556 | prose | pages [17] -->
Bayamon

<!-- b000557 | prose | pages [17] -->
Bayamon

<!-- b000558 | prose | pages [17] -->
Bayamon

<!-- b000559 | prose | pages [17] -->
Bayamon

<!-- b000560 | prose | pages [17] -->
Rio Grande

<!-- b000561 | prose | pages [17] -->
Rio Grande

<!-- b000562 | prose | pages [17] -->
Rio Grande

<!-- b000563 | prose | pages [17] -->
Rio Grande

<!-- b000564 | prose | pages [17] -->
Corozal

<!-- b000565 | prose | pages [17] -->
Corozal

<!-- b000566 | prose | pages [17] -->
Corozal

<!-- b000567 | prose | pages [17] -->
Corozal

<!-- b000568 | prose | pages [17] -->
Fajardo

<!-- b000569 | prose | pages [17] -->
Fajardo

<!-- b000570 | prose | pages [17] -->
Fajardo

<!-- b000571 | prose | pages [17] -->
Fajardo

<!-- b000572 | prose | pages [17] -->
Aguas Buenas

<!-- b000573 | prose | pages [17] -->
Aguas Buenas

<!-- b000574 | prose | pages [17] -->
Aguas Buenas

<!-- b000575 | prose | pages [17] -->
Aguas Buenas

<!-- b000576 | prose | pages [17] -->
Caguas

<!-- b000577 | prose | pages [17] -->
Caguas

<!-- b000578 | prose | pages [17] -->
Caguas

<!-- b000579 | prose | pages [17] -->
Caguas

<!-- b000580 | prose | pages [17] -->
Comerio

<!-- b000581 | prose | pages [17] -->
Comerio

<!-- b000582 | prose | pages [17] -->
Comerio

<!-- b000583 | prose | pages [17] -->
Comerio

<!-- b000584 | prose | pages [17] -->
Juncos

<!-- b000585 | prose | pages [17] -->
Juncos

<!-- b000586 | prose | pages [17] -->
Juncos

<!-- b000587 | prose | pages [17] -->
Juncos

<!-- b000588 | prose | pages [17] -->
Orocovis

<!-- b000589 | prose | pages [17] -->
Orocovis

<!-- b000590 | prose | pages [17] -->
Orocovis

<!-- b000591 | prose | pages [17] -->
Orocovis

<!-- b000592 | prose | pages [17] -->
Naguabo

<!-- b000593 | prose | pages [17] -->
Naguabo

<!-- b000594 | prose | pages [17] -->
Naguabo

<!-- b000595 | prose | pages [17] -->
Naguabo

<!-- b000596 | prose | pages [17] -->
San Lorenzo

<!-- b000597 | prose | pages [17] -->
San Lorenzo

<!-- b000598 | prose | pages [17] -->
San Lorenzo

<!-- b000599 | prose | pages [17] -->
San Lorenzo

<!-- b000600 | prose | pages [17] -->
Unnamed 3Unnamed 4

<!-- b000601 | prose | pages [17] -->
Unnamed 3Unnamed 4

<!-- b000602 | prose | pages [17] -->
Unnamed 3Unnamed 4

<!-- b000603 | prose | pages [17] -->
Unnamed 3Unnamed 4

<!-- b000604 | prose | pages [17] -->
Unnamed 1

<!-- b000605 | prose | pages [17] -->
Unnamed 1

<!-- b000606 | prose | pages [17] -->
Unnamed 1

<!-- b000607 | prose | pages [17] -->
Unnamed 1

<!-- b000608 | prose | pages [17] -->
Humacao

<!-- b000609 | prose | pages [17] -->
Humacao

<!-- b000610 | prose | pages [17] -->
Humacao

<!-- b000611 | prose | pages [17] -->
Humacao

<!-- b000612 | prose | pages [17] -->
Unnamed 5

<!-- b000613 | prose | pages [17] -->
Unnamed 5

<!-- b000614 | prose | pages [17] -->
Unnamed 5

<!-- b000615 | prose | pages [17] -->
Unnamed 5

<!-- b000616 | prose | pages [17] -->
Unnamed 2

<!-- b000617 | prose | pages [17] -->
Unnamed 2

<!-- b000618 | prose | pages [17] -->
Unnamed 2

<!-- b000619 | prose | pages [17] -->
Unnamed 2

<!-- b000620 | prose | pages [17] -->
Cayey

<!-- b000621 | prose | pages [17] -->
Cayey

<!-- b000622 | prose | pages [17] -->
Cayey

<!-- b000623 | prose | pages [17] -->
Cayey

<!-- b000624 | prose | pages [17] -->
Coamo

<!-- b000625 | prose | pages [17] -->
Coamo

<!-- b000626 | prose | pages [17] -->
Coamo

<!-- b000627 | prose | pages [17] -->
Coamo

<!-- b000628 | prose | pages [17] -->
Maunabo

<!-- b000629 | prose | pages [17] -->
Maunabo

<!-- b000630 | prose | pages [17] -->
Maunabo

<!-- b000631 | prose | pages [17] -->
Maunabo

<!-- b000632 | prose | pages [17] -->
Guayama

<!-- b000633 | prose | pages [17] -->
Guayama

<!-- b000634 | prose | pages [17] -->
Guayama

<!-- b000635 | prose | pages [17] -->
Guayama

<!-- b000636 | prose | pages [17] -->
Santa Isabel

<!-- b000637 | prose | pages [17] -->
Santa Isabel

<!-- b000638 | prose | pages [17] -->
Santa Isabel

<!-- b000639 | prose | pages [17] -->
Santa Isabel

<!-- b000640 | prose | pages [17] -->
Punta Figuras

<!-- b000641 | prose | pages [17] -->
Punta Figuras

<!-- b000642 | prose | pages [17] -->
Punta Figuras

<!-- b000643 | prose | pages [17] -->
Punta Figuras

<!-- b000644 | prose | pages [17] -->
-66.4 -66.2 -66 -65.8 -65.6 longtitude/°

<!-- b000645 | caption | pages [17] -->
Figure 8: The PSO algorithm identiﬁes the best locations of 3 containers.

<!-- b000646 | prose | pages [17] -->
As shown in Section 5.2, the PSO algorithm is used again to identify the best loca- tions of cargo containers. But differently, since we need to meet the demand of the an- ticipated medical supplies, we shall narrow the feasible region according to the drones’ maximum navigation radius. The results of PSO give the best locations as below.

<!-- b000647 | furniture | pages [18] -->
Team # 1923964

<!-- b000648 | prose | pages [18] -->
Destinations Drone Container to Supply Fleet

<!-- b000649 | prose | pages [18] -->
San Juan

<!-- b000650 | furniture | pages [18] -->
Page 16 of 23

<!-- b000651 | prose | pages [18] -->
Packing Location Conﬁgurations

<!-- b000652 | prose | pages [18] -->
1908 MED 1, 954 MED 2 (18.36, −65.85) 1 B Fajardo

<!-- b000653 | prose | pages [18] -->
Bayamon

<!-- b000654 | prose | pages [18] -->
954 MED 3

<!-- b000655 | prose | pages [18] -->
1224 MED 1, 306 MED 2 (18.27, −66,12) 2 B, F Caguas 918 MED 3

<!-- b000656 | prose | pages [18] -->
(18.23, −66.76) 3 Arecibo B

<!-- b000657 | prose | pages [18] -->
5.3.2 Delivery Routes and Schedule

<!-- b000658 | prose | pages [18] -->
3720 MED 1

<!-- b000659 | prose | pages [18] -->
Notice that the delivery route in the three-dimensional space is not actually straight because of the rugged terrain in reality. Since the maximum ﬂight height is around 120 meters, far below the height of the mountains that the drones will come across in its journeys.[8] We assume drones are ﬂying close to the ground. Thus, we applied Dijk- stra algorithm to derive the minimum distance as well as the drones’ optimal delivery route. The 3-dimensional routes are illustrated below.

<!-- b000660 | caption | pages [18] -->
Figure 9: The 3-dimensional delivery routes of the drones

<!-- b000661 | prose | pages [18] -->
Since the total time needed to deliver supplies is ﬁxed after the delivery routes are given by Dijkstra algorithm, the schedule is clear. We make the drones ﬂy along the above routes and replace their batteries and reload packages after each return. Then the drones can take off again and ﬂy to another destination.

<!-- b000662 | caption | pages [18] -->
Figure 10: The illustration of delivery schedule

<!-- b000663 | furniture | pages [19] -->
Team # 1923964

<!-- b000664 | prose | pages [19] -->
5.3.3 Payload Packing Conﬁgurations

<!-- b000665 | furniture | pages [19] -->
Page 17 of 23

<!-- b000666 | prose | pages [19] -->
As described before in Section 5.1.3, we pack all the medical packages required by a certain destination each day into a single parcel. Therefore, each drone’s payload packing conﬁguration is the corresponding parcel required by each city. The drone will ﬂy directly to the destination and return to the container.

<!-- b000667 | prose | pages [19] -->
With simple calculation by exhaustion, we know that this is the most time-saving way of package conﬁguration. If the medical packages required by a destination is delivered by two or more drones for multiple times, total delivery time will increase.

<!-- b000668 | prose | pages [19] -->
5.3.4 Flight Plan to Access Major Roads

<!-- b000669 | prose | pages [19] -->
With the highest speed, longest ﬂying range and relatively small size, drone B will be used in video reconnaissance.

<!-- b000670 | prose | pages [19] -->
Given the best locations, the settlements and segments of roads within the drones’ coverage area are deﬁnite, as the bold lines shown in ﬁgure below. Thus, we need to work out a ﬂight plan aiming to inspect the segments of major roads.

<!-- b000671 | prose | pages [19] -->
18.5

<!-- b000672 | prose | pages [19] -->
Quebradillas

<!-- b000673 | prose | pages [19] -->
Quebradillas

<!-- b000674 | prose | pages [19] -->
Quebradillas

<!-- b000675 | prose | pages [19] -->
Quebradillas

<!-- b000676 | prose | pages [19] -->
Arecibo

<!-- b000677 | prose | pages [19] -->
Arecibo

<!-- b000678 | prose | pages [19] -->
Arecibo

<!-- b000679 | prose | pages [19] -->
Arecibo

<!-- b000680 | prose | pages [19] -->
Barceloneta

<!-- b000681 | prose | pages [19] -->
Barceloneta

<!-- b000682 | prose | pages [19] -->
Barceloneta

<!-- b000683 | prose | pages [19] -->
Barceloneta

<!-- b000684 | prose | pages [19] -->
Aguadilla

<!-- b000685 | prose | pages [19] -->
Aguadilla

<!-- b000686 | prose | pages [19] -->
Aguadilla

<!-- b000687 | prose | pages [19] -->
Aguadilla

<!-- b000688 | prose | pages [19] -->
18.4

<!-- b000689 | prose | pages [19] -->
Centrol Puntas

<!-- b000690 | prose | pages [19] -->
Centrol Puntas

<!-- b000691 | prose | pages [19] -->
Centrol Puntas

<!-- b000692 | prose | pages [19] -->
Centrol Puntas

<!-- b000693 | prose | pages [19] -->
San Sebastian

<!-- b000694 | prose | pages [19] -->
San Sebastian

<!-- b000695 | prose | pages [19] -->
San Sebastian

<!-- b000696 | prose | pages [19] -->
San Sebastian

<!-- b000697 | prose | pages [19] -->
Utuado'

<!-- b000698 | prose | pages [19] -->
18.3

<!-- b000699 | prose | pages [19] -->
Utuado

<!-- b000700 | prose | pages [19] -->
Lares

<!-- b000701 | prose | pages [19] -->
Jayuya

<!-- b000702 | prose | pages [19] -->
Jayuya

<!-- b000703 | prose | pages [19] -->
Jayuya

<!-- b000704 | prose | pages [19] -->
Canstaner

<!-- b000705 | prose | pages [19] -->
Mayaguez

<!-- b000706 | prose | pages [19] -->
Mayaguez

<!-- b000707 | prose | pages [19] -->
Mayaguez

<!-- b000708 | prose | pages [19] -->
Mayaguez

<!-- b000709 | prose | pages [19] -->
18.2

<!-- b000710 | prose | pages [19] -->
Adjuntas

<!-- b000711 | prose | pages [19] -->
Adjuntas

<!-- b000712 | prose | pages [19] -->
Adjuntas

<!-- b000713 | prose | pages [19] -->
Adjuntas

<!-- b000714 | prose | pages [19] -->
Indiera Alta

<!-- b000715 | prose | pages [19] -->
Indiera Alta

<!-- b000716 | prose | pages [19] -->
Indiera Alta

<!-- b000717 | prose | pages [19] -->
Indiera Alta

<!-- b000718 | prose | pages [19] -->
18.1

<!-- b000719 | prose | pages [19] -->
San German

<!-- b000720 | prose | pages [19] -->
San German

<!-- b000721 | prose | pages [19] -->
San German

<!-- b000722 | prose | pages [19] -->
San German

<!-- b000723 | prose | pages [19] -->
Yauco

<!-- b000724 | prose | pages [19] -->
Yauco

<!-- b000725 | prose | pages [19] -->
Yauco

<!-- b000726 | prose | pages [19] -->
Yauco

<!-- b000727 | prose | pages [19] -->
Ponce

<!-- b000728 | prose | pages [19] -->
Ponce

<!-- b000729 | prose | pages [19] -->
Ponce

<!-- b000730 | prose | pages [19] -->
Ponce

<!-- b000731 | prose | pages [19] -->
18

<!-- b000732 | prose | pages [19] -->
Cabo Rojo

<!-- b000733 | prose | pages [19] -->
Cabo Rojo

<!-- b000734 | prose | pages [19] -->
Cabo Rojo

<!-- b000735 | prose | pages [19] -->
Cabo Rojo

<!-- b000736 | prose | pages [19] -->
Ensenada

<!-- b000737 | prose | pages [19] -->
Ensenada

<!-- b000738 | prose | pages [19] -->
Ensenada

<!-- b000739 | prose | pages [19] -->
Ensenada

<!-- b000740 | prose | pages [19] -->
17.9 -67.2 -67 -66.8 -66.6

<!-- b000741 | prose | pages [19] -->
Dorado

<!-- b000742 | prose | pages [19] -->
Dorado

<!-- b000743 | prose | pages [19] -->
Dorado

<!-- b000744 | prose | pages [19] -->
Dorado

<!-- b000745 | prose | pages [19] -->
Manati

<!-- b000746 | prose | pages [19] -->
Manati

<!-- b000747 | prose | pages [19] -->
Manati

<!-- b000748 | prose | pages [19] -->
Manati

<!-- b000749 | prose | pages [19] -->
San Juan

<!-- b000750 | prose | pages [19] -->
San Juan

<!-- b000751 | prose | pages [19] -->
San Juan

<!-- b000752 | prose | pages [19] -->
San Juan

<!-- b000753 | prose | pages [19] -->
Unnamed 6

<!-- b000754 | prose | pages [19] -->
Unnamed 6

<!-- b000755 | prose | pages [19] -->
Unnamed 6

<!-- b000756 | prose | pages [19] -->
Unnamed 6

<!-- b000757 | prose | pages [19] -->
Rio Grande

<!-- b000758 | prose | pages [19] -->
Bayamon

<!-- b000759 | prose | pages [19] -->
Rio Grande

<!-- b000760 | prose | pages [19] -->
Rio Grande

<!-- b000761 | prose | pages [19] -->
Bayamon

<!-- b000762 | prose | pages [19] -->
Bayamon

<!-- b000763 | prose | pages [19] -->
Bayamon

<!-- b000764 | prose | pages [19] -->
Rio Grande

<!-- b000765 | prose | pages [19] -->
Corozal

<!-- b000766 | prose | pages [19] -->
Corozal

<!-- b000767 | prose | pages [19] -->
Corozal

<!-- b000768 | prose | pages [19] -->
Corozal

<!-- b000769 | prose | pages [19] -->
Fajardo

<!-- b000770 | prose | pages [19] -->
Fajardo

<!-- b000771 | prose | pages [19] -->
Fajardo

<!-- b000772 | prose | pages [19] -->
Fajardo

<!-- b000773 | prose | pages [19] -->
Aguas Buenas

<!-- b000774 | prose | pages [19] -->
Aguas Buenas

<!-- b000775 | prose | pages [19] -->
Aguas Buenas

<!-- b000776 | prose | pages [19] -->
Aguas Buenas

<!-- b000777 | prose | pages [19] -->
Caguas

<!-- b000778 | prose | pages [19] -->
Caguas

<!-- b000779 | prose | pages [19] -->
Caguas

<!-- b000780 | prose | pages [19] -->
Caguas

<!-- b000781 | prose | pages [19] -->
Comerio

<!-- b000782 | prose | pages [19] -->
Comerio

<!-- b000783 | prose | pages [19] -->
Comerio

<!-- b000784 | prose | pages [19] -->
Comerio

<!-- b000785 | prose | pages [19] -->
Juncos

<!-- b000786 | prose | pages [19] -->
Juncos

<!-- b000787 | prose | pages [19] -->
Juncos

<!-- b000788 | prose | pages [19] -->
Juncos

<!-- b000789 | prose | pages [19] -->
Orocovis

<!-- b000790 | prose | pages [19] -->
Orocovis

<!-- b000791 | prose | pages [19] -->
Orocovis

<!-- b000792 | prose | pages [19] -->
Orocovis

<!-- b000793 | prose | pages [19] -->
Naguabo

<!-- b000794 | prose | pages [19] -->
Naguabo

<!-- b000795 | prose | pages [19] -->
Naguabo

<!-- b000796 | prose | pages [19] -->
Naguabo

<!-- b000797 | prose | pages [19] -->
San Lorenzo

<!-- b000798 | prose | pages [19] -->
San Lorenzo

<!-- b000799 | prose | pages [19] -->
San Lorenzo

<!-- b000800 | prose | pages [19] -->
San Lorenzo

<!-- b000801 | prose | pages [19] -->
Unnamed 4

<!-- b000802 | prose | pages [19] -->
Unnamed 4

<!-- b000803 | prose | pages [19] -->
Unnamed 4

<!-- b000804 | prose | pages [19] -->
Unnamed 4

<!-- b000805 | prose | pages [19] -->
Unnamed 3

<!-- b000806 | prose | pages [19] -->
Unnamed 3

<!-- b000807 | prose | pages [19] -->
Unnamed 3

<!-- b000808 | prose | pages [19] -->
Unnamed 3

<!-- b000809 | prose | pages [19] -->
Unnamed 1

<!-- b000810 | prose | pages [19] -->
Unnamed 1

<!-- b000811 | prose | pages [19] -->
Unnamed 1

<!-- b000812 | prose | pages [19] -->
Unnamed 1

<!-- b000813 | prose | pages [19] -->
Humacao

<!-- b000814 | prose | pages [19] -->
Humacao

<!-- b000815 | prose | pages [19] -->
Humacao

<!-- b000816 | prose | pages [19] -->
Humacao

<!-- b000817 | prose | pages [19] -->
Unnamed 5

<!-- b000818 | prose | pages [19] -->
Unnamed 5

<!-- b000819 | prose | pages [19] -->
Unnamed 5

<!-- b000820 | prose | pages [19] -->
Unnamed 5

<!-- b000821 | prose | pages [19] -->
Cayey

<!-- b000822 | prose | pages [19] -->
Cayey

<!-- b000823 | prose | pages [19] -->
Cayey

<!-- b000824 | prose | pages [19] -->
Cayey

<!-- b000825 | prose | pages [19] -->
Unnamed 2

<!-- b000826 | prose | pages [19] -->
Coamo

<!-- b000827 | prose | pages [19] -->
Coamo

<!-- b000828 | prose | pages [19] -->
Coamo

<!-- b000829 | prose | pages [19] -->
Coamo

<!-- b000830 | prose | pages [19] -->
Maunabo

<!-- b000831 | prose | pages [19] -->
Maunabo

<!-- b000832 | prose | pages [19] -->
Maunabo

<!-- b000833 | prose | pages [19] -->
Maunabo

<!-- b000834 | prose | pages [19] -->
Guayama

<!-- b000835 | prose | pages [19] -->
Guayama

<!-- b000836 | prose | pages [19] -->
Guayama

<!-- b000837 | prose | pages [19] -->
Guayama

<!-- b000838 | prose | pages [19] -->
Santa Isabel

<!-- b000839 | prose | pages [19] -->
Santa Isabel

<!-- b000840 | prose | pages [19] -->
Santa Isabel

<!-- b000841 | prose | pages [19] -->
Santa Isabel

<!-- b000842 | prose | pages [19] -->
Punta Figuras

<!-- b000843 | prose | pages [19] -->
Punta Figuras

<!-- b000844 | prose | pages [19] -->
Punta Figuras

<!-- b000845 | prose | pages [19] -->
Punta Figuras

<!-- b000846 | prose | pages [19] -->
-66.4 -66.2 -66 -65.8 -65.6

<!-- b000847 | caption | pages [19] -->
Figure 11: The segments of major roads within each coverage area

<!-- b000848 | prose | pages [19] -->
An accessing mission consists of three successive phases: setting off to the target segment, inspecting along the segment and returning to container before running out of power. Due to the urgency of rescuing work, it must be better for the drones to provide feedback of information as soon as possible. Thus, in order to reduce the waste of time on the ﬁrst and third phases, the drones should begin accessing from those segments close to the centre to those far away. Adopting the distance between the centre and the segments’ midpoint as a criterion, we rank the segments of roads from small to large by distance. The ﬂight plans are listed below. Segments of roads are expressed by the two settlements they connect. The arrows indicate the accessing sequence.

<!-- b000849 | prose | pages [19] -->
Container 1 Rio Grande-Fajardo →San Juan-Rio Grande →Naguabo-Juncos →Humacao-

<!-- b000850 | prose | pages [19] -->
Fajardo →Caguas-Juncos →Humacao-San Lorenzo →San Juan-Caguas → Caguas-San Lorenzo

<!-- b000851 | prose | pages [19] -->
Container 2 Aguas Buenas-Unnamed 4 →Bayamon Aguas-Buenas →Aguas Buenas-

<!-- b000852 | prose | pages [19] -->
Caguas →Comerio-Bayamon →San Juan-Aguas Buenas →Comerio-Unnamed

<!-- b000853 | furniture | pages [20] -->
Team # 1923964

<!-- b000854 | furniture | pages [20] -->
Page 18 of 23

<!-- b000855 | prose | pages [20] -->
4 →San Juan-Caguas →Caguas-Cayey →Bayamon-San Juan →Unnamed 4- Cayey →Caguas-Juncos →Caguas-San Lorenzo →Bayamon-Unnamed 6 → Unnamed 2-Cayey →Corozal-Unnamed 6

<!-- b000856 | prose | pages [20] -->
Container 3 Utuado-Adjuntas →Lares-Utuado →Canstaner-Adjuntas →Lares-Canstaner

<!-- b000857 | prose | pages [20] -->
→Utuado-Utuado’ →Indiera Alta-Canstaner →Arecibo-Utuado →Utuado’- Jayuya →Lares-Arecibo →Yauco-Indiera Alta

<!-- b000858 | prose | pages [20] -->
6

<!-- b000859 | heading | pages [20] -->
Applying of Models

<!-- b000860 | prose | pages [20] -->
Notice that the response system is developed for potential crisis, especially a larger- scale one, in the future. We test our models by altering the case as Haiti whose popu- lation and area are about three times larger than Puerto Rcio. In 2010, Haiti suffered a earthquake and witnessed the participation of drones in the rescuing work.[12]

<!-- b000861 | caption | pages [20] -->
Figure 12: Haiti’s comparison between the importance illustration and best locations

<!-- b000862 | prose | pages [20] -->
As shown above, we abstract the map of Haiti. Applying the same importance eval- uation criteria and the optimization function, we identify the best three locations. The service regions of the containers cover the most population-dense districts including Haiti’s top 5 signiﬁcant cities.

<!-- b000863 | prose | pages [20] -->
The successful application of Haiti demonstrates our models’ practicability and universality.

<!-- b000864 | prose | pages [20] -->
7

<!-- b000865 | heading | pages [20] -->
Sensitivity Analysis

<!-- b000866 | prose | pages [20] -->
7.1 Importance Level of Settlements

<!-- b000867 | prose | pages [20] -->
Since the values assigned to different settlements in Section 5.2.1 are subjective, we check up whether the variations of importance level affect the result remarkably. Two major possible defects are the arbitrariness of assigning settlements importance and the underestimation of some settlements.

<!-- b000868 | furniture | pages [21] -->
Team # 1923964

<!-- b000869 | prose | pages [21] -->
7.1.1 Assigning Methods of Importance

<!-- b000870 | furniture | pages [21] -->
Page 19 of 23

<!-- b000871 | prose | pages [21] -->
Different from linear methods in Section 5.2.1, we set the values of different settle- ments’ importance as 1, 2, 4, 8, 16, 32, which is an exponential sequence.

<!-- b000872 | prose | pages [21] -->
Destination Fajardo & San Juan Arecibo Caguas & Bayamon (18.32, −65.88) (18.31, −66.83) Linear (18.38, −66.17) (18.32, −65.88) (18.34, −66.55) Exponential (18.38, −66.17)

<!-- b000873 | prose | pages [21] -->
As shown in the table, different methods of assigning importance have a little im- pact on the best locations. Instinctively, we may make a bold prediction of robustness with respect to assigning methods so long as they satisfy the order preservation of the settlements.

<!-- b000874 | prose | pages [21] -->
Underestimation of Some Settlements’ Importance 7.1.2

<!-- b000875 | prose | pages [21] -->
Underestimation of some places’ importance is common. For example on Puerto Rico, Mayaguez on the western coast may possess abundant historical cultural relics and remains that deserve timely rescue and Loiza Aldea on the northeast coast may be an important harbour that allows supplies being transported into the island. Therefore, it would be well to change their values of importance from 4 to 5 and from 3 to 5 respectively. Our models give the result as follows.

<!-- b000876 | prose | pages [21] -->
Destination Fajardo & San Juan Arecibo Caguas & Bayamon (18.32, −65.88) (18.31, −66.83) Original (18.38, −66.17) (18.32, −65.65) (18.27, −66.71) Modiﬁed (18.23, −66.03)

<!-- b000877 | prose | pages [21] -->
As shown above, the individual changes of importance bring about an actual im- pact on the best locations. It is worth pointing out that the inﬂuence of individual changes can spread far away through the connective matrix X. In general, t he mod- erate changes of locations are still acceptable.

<!-- b000878 | prose | pages [21] -->
Drones’ Maximum Navigation Radius 7.2

<!-- b000879 | prose | pages [21] -->
Varying the maximum navigation radius, we check up the corresponding changes in best locations. Under the restriction of delivering supplies for up to 3 containers, the largest maximum navigation radius r among all kinds of drones should be no less than 22km. Thus, we set r as 23, 26 and 40km.

<!-- b000880 | furniture | pages [22] -->
Team # 1923964

<!-- b000881 | furniture | pages [22] -->
Page 20 of 23

<!-- b000882 | caption | pages [22] -->
Figure 13: Comparison of global optimization results

<!-- b000883 | prose | pages [22] -->
Apart from the density map of global optimization results, we identify the best 3 locations under different radii, as shown below.

<!-- b000884 | prose | pages [22] -->
Radius 23 km

<!-- b000885 | prose | pages [22] -->
Destination

<!-- b000886 | prose | pages [22] -->
26 km 40 km

<!-- b000887 | prose | pages [22] -->
(18.33,−66.79) Arecibo (18.31, −66.83) (18.25 −66.58) (18.34, −65.85) Fajardo & San Juan (18.32, −65.88) (18.32, −66.00) (18.38, −66.17) Caguas & Bayamon (18.38, −66.17) (18.38, −66.17)

<!-- b000888 | prose | pages [22] -->
The comparison indicates that the variation of different extent of radius make re- markably different inﬂuence on the best locations. The changes can be explained by the length distribution of segments (see in Appendix). Since the settlements are dis- cretely located, there exist a minimum distance among them. Tiny changes of radius can hardly include new settlements and therefore, they lead to little changes of the coverage’s contents. Hence, only large variations can contribute to signiﬁcant changes of locations.

<!-- b000889 | prose | pages [22] -->
8

<!-- b000890 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b000891 | prose | pages [22] -->
8.1

<!-- b000892 | heading | pages [22] -->
Strengths

<!-- b000893 | prose | pages [22] -->
• Taking topographic factors into account, models are adaptable to regions of var- ious terrains but not limit to Puerto Rico.

<!-- b000894 | prose | pages [22] -->
• Models are close to reality, such as safety concern of maximum ﬂying time with full cargo and simulation of cameras’ scanning pattern.

<!-- b000895 | prose | pages [22] -->
• Reasonable and easy-to-practice evaluation of importance level instructs the re- connaissance effectively.

<!-- b000896 | prose | pages [22] -->
• Robustness and practicability are demonstrated by sensitivity analysis.

<!-- b000897 | furniture | pages [23] -->
Team # 1923964

<!-- b000898 | furniture | pages [23] -->
Page 21 of 23

<!-- b000899 | prose | pages [23] -->
8.2

<!-- b000900 | heading | pages [23] -->
Weaknesses

<!-- b000901 | prose | pages [23] -->
• The time complexity of the delivering model obeys exponential pattern and brings about difﬁculties of solving a large-scale problem.

<!-- b000902 | prose | pages [23] -->
Due to the complexity of the problem, we can hardly derive a systematic programme to solve it.

<!-- b000903 | prose | pages [23] -->
• The importance levels assigned to the settlements are subjective and lack detailed considerations.

<!-- b000904 | prose | pages [23] -->
• The inﬂuence of weather condition is ignored.

<!-- b000905 | prose | pages [23] -->
The possibility of encountering extreme weather shortly after a disaster should be consid- ered. But for conciseness of modeling and feasibility of calculations, we have to abandon the consideration pitifully.

<!-- b000906 | prose | pages [23] -->
9

<!-- b000907 | heading | pages [23] -->
Future Work

<!-- b000908 | prose | pages [23] -->
As mentioned in weaknesses in Section 9.2, the weather condition is not taken into account. Actually, there are more factors that deserve inclusion in our models.

<!-- b000909 | prose | pages [23] -->
The most remarkable factor is the extent to which an area is suffering the disaster. The more severe the circumstances are, the more urgently it demands rescue. The factor can be quantitated by a series of measurements. For example, measurements include the distances away from the epicenter in an earthquake and the minimum distances away from the trajectory in a hurricane.

<!-- b000910 | prose | pages [23] -->
In addition, the feedback of the reconnaissance can instruct further missions in- cluding materials supplied by trucks. The ground transportation is obviously more economical.

<!-- b000911 | prose | pages [23] -->
However, due to the limited time information available for the problem, we cannot reﬁne our models adequately.

<!-- b000912 | prose | pages [23] -->
10

<!-- b000913 | heading | pages [23] -->
Conclusions

<!-- b000914 | prose | pages [23] -->
From a top-down perspective, we separate the complicated problem into two rela- tively simpliﬁed missions and establish a model for them respectively.

<!-- b000915 | prose | pages [23] -->
For the overall design, we emphasize the reality by considering three practicable factors. For the design of two individual models, we emphasize the practicability by sorting out the feasible groups of destinations, introducing segments and importance evaluation function.

<!-- b000916 | prose | pages [23] -->
We combine the two models naturally and derive a comprehensive solution in- cluding the ﬂeets’ composition, each drone’s payload conﬁgurations, delivery route, schedule and ﬂight plan as well as the containers’ best locations and packing conﬁgu- rations.

<!-- b000917 | furniture | pages [24] -->
Team # 1923964

<!-- b000918 | furniture | pages [24] -->
Page 22 of 23

<!-- b000919 | prose | pages [24] -->
11

<!-- b000920 | heading | pages [24] -->
Appendix

<!-- b000921 | prose | pages [24] -->
Flight time versus payload

<!-- b000922 | caption | pages [24] -->
Figure 14: Relationship between ﬂight time and the drone’s payload [4]

<!-- b000923 | prose | pages [24] -->
Distribution of segments’ length

<!-- b000924 | caption | pages [24] -->
Figure 15: The frequency map of segments’ length

<!-- b000925 | furniture | pages [25] -->
Team # 1923964

<!-- b000926 | heading | pages [25] -->
References

<!-- b000927 | furniture | pages [25] -->
Page 23 of 23

<!-- b000928 | references | pages [25] -->
[1] Outstanding Drone: Top 10 Drones for Search and Rescue Operations. (2019)

<!-- b000929 | references | pages [25] -->
2018.11.8.

<!-- b000930 | references | pages [25] -->
https://www.outstandingdrone.com/search-rescue-drones/

<!-- b000931 | references | pages [25] -->
#1FlyByCopters_X8_640_Quadcopter_Drone.

<!-- b000932 | references | pages [25] -->
https://baike.baidu.com/

<!-- b000933 | references | pages [25] -->
2018.12.05

<!-- b000934 | references | pages [25] -->
[2] BaiduBaike: control radius.

<!-- b000935 | references | pages [25] -->
item/%E6%8E%A7%E5%88%B6%E5%8D%8A%E5%BE%84/23192207?fr=aladdin

<!-- b000936 | references | pages [25] -->
http://haiba.qhdi.com/

<!-- b000937 | references | pages [25] -->
[3] Google Maps: Puerto Rico

<!-- b000938 | references | pages [25] -->
https://freeflysystems.zendesk.com/hc/en-us/

<!-- b000939 | references | pages [25] -->
[4] Freeﬂy Systems

<!-- b000940 | references | pages [25] -->
signin?return_to=https%3A%2F%2Ffreeflysystems.zendesk.com

<!-- b000941 | references | pages [25] -->
%2Fhc%2Fen-us%2Farticles%2F204720589-What-is-the-max-flight

<!-- b000942 | references | pages [25] -->
-time-on-the-ALTA-6

<!-- b000943 | references | pages [25] -->
[5] Vann R. Newkirk II: Can Puerto Rico Recover From Maria Before the Next Storm

<!-- b000944 | references | pages [25] -->
2018.04.26. https://www.theatlantic.

<!-- b000945 | references | pages [25] -->
Hits? The Atlantic Monthly. Politics

<!-- b000946 | references | pages [25] -->
com/politics/archive/2018/04/puerto-ricos-next-public-health-

<!-- b000947 | references | pages [25] -->
challenges/558896/

<!-- b000948 | references | pages [25] -->
Puerto Ricos recovery, 7 months after Hurricane Maria.

<!-- b000949 | references | pages [25] -->
[6] PBS News Hour:

<!-- b000950 | references | pages [25] -->
https://www.pbs.org/newshour/nation/puerto-ricos-

<!-- b000951 | references | pages [25] -->
2018.04.19.

<!-- b000952 | references | pages [25] -->
recovery-7-months-after-hurricane-maria

<!-- b000953 | references | pages [25] -->
https://zh.wikipedia.org/wiki/

<!-- b000954 | references | pages [25] -->
2018.11.16.

<!-- b000955 | references | pages [25] -->
[7] Wikipedia: Tropical Forest.

<!-- b000956 | references | pages [25] -->
%E7%83%AD%E5%B8%A6%E9%9B%A8%E6%9E%97

<!-- b000957 | references | pages [25] -->
https://www.

<!-- b000958 | references | pages [25] -->
[8] The Drone Logic: How High Drones Can Fly?

<!-- b000959 | references | pages [25] -->
2018.03.28.

<!-- b000960 | references | pages [25] -->
thedronelogic.com/how-drones-work/drone-flight-time/

<!-- b000961 | references | pages [25] -->
https://pro.dji.com/

<!-- b000962 | references | pages [25] -->
[9] DJI: Professional Product. Glimbal Cameras.(2019)

<!-- b000963 | references | pages [25] -->
?site=brandsite&from=nav

<!-- b000964 | references | pages [25] -->
[10] National Instruments: Calculating Camera Sensor Resolution and Lens Focal

<!-- b000965 | references | pages [25] -->
Length. (2019) 2018.02.15. http://www.ni.com/product-documentation

<!-- b000966 | references | pages [25] -->
/54616/en/

<!-- b000967 | references | pages [25] -->
[11] Federal Aviation Administration. Unmanned Aircraft Systems. 2018.12.20.

<!-- b000968 | references | pages [25] -->
https://www.faa.gov/uas/

<!-- b000969 | references | pages [25] -->
Flying aid drones tested in Haiti and Dominican Republic.

<!-- b000970 | references | pages [25] -->
[12] The Guardian:

<!-- b000971 | references | pages [25] -->
https://www.theguardian.com/global-development/

<!-- b000972 | references | pages [25] -->
2013.01.09.

<!-- b000973 | references | pages [25] -->
2013/jan/09/flying-aid-drones-haiti-dominican-republic

<!-- b000974 | references | pages [25] -->
[13] DJI: Inspire 2. (2019) https://www.dji.com/cn/inspire-2/specs
