# P-B-2019-1923964-678ee565

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
1923964

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | heading | pages [1] -->
2019 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000007 | front_matter | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000008 | title | pages [1] -->
Go Safe with Drones

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
We use Dijkstra Algorithm and Particle Swarm Optimization (PSO) to develop a set of models which can solve for a universally practicable DroneGo disaster response system.

<!-- b000011 | prose | pages [1] -->
Before model construction, we make some basic assumptions essential to further analyses. To model reasonably and effectively, we deﬁne three computable optimiza- tion objectives.

<!-- b000012 | prose | pages [1] -->
First, we rebuild a three-dimensional map by interpolation with intensive data col- lection. Deriving an equation of ﬂying time versus payload and the pattern of onboard cameras’ scanning, we pay attention to the models’ authenticity.

<!-- b000013 | prose | pages [1] -->
Next, we design an optimization model for delivery to minimize the total deliv- ering time. Adopting Optimal Combination Algorithm (OCA), we provide a detailed and universal solving strategy to identify the best locations. Moreover, Dijkstra Al- gorithm is applied to derive the drones’ three-dimensional delivery routes. To design the reconnaissance model, we creatively transform the evaluation problem of road seg- ments to the evaluation of settlements. This easy-to-practice model reduces the prob- lem’s complexity remarkably. General importance, a quantiﬁable index, is introduced for evaluation. Then we use improved PSO algorithm to identify the best reconnais- sance area.

<!-- b000014 | prose | pages [1] -->
Based on two models above, we build a combined model to address multi-objective optimization problems. Different weights of objectives are introduced according to speciﬁc scenarios. Provided the weights, we can solve for optimal results.

<!-- b000015 | prose | pages [1] -->
In addition, we apply our models to Haiti’s earthquake in 2010 to test the prac- ticability and effectiveness. The predicted locations of containers are approximately overlapped with the relief centers at that time, which demonstrates our models’ uni- versality. Furtherly, we conceive a more comprehensive model including the factors of weather conditions and the extent of damage.

<!-- b000016 | prose | pages [1] -->
Finally, we conduct sensitivity analyses and prove our models to be quite robust against the changes in the method of assigning settlement’s importance.

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1 Introduction

<!-- b000019 | contents | pages [2] -->
3

<!-- b000020 | contents | pages [2] -->
1.1

<!-- b000021 | contents | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000022 | contents | pages [2] -->
3

<!-- b000023 | contents | pages [2] -->
1.2

<!-- b000024 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
3

<!-- b000026 | contents | pages [2] -->
2 Assumptions and Justiﬁcations

<!-- b000027 | contents | pages [2] -->
4

<!-- b000028 | contents | pages [2] -->
2.1

<!-- b000029 | contents | pages [2] -->
General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
4

<!-- b000031 | contents | pages [2] -->
2.2

<!-- b000032 | contents | pages [2] -->
Assumptions of Delivering Supplies . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
5

<!-- b000034 | contents | pages [2] -->
2.3

<!-- b000035 | contents | pages [2] -->
Assumptions of Reconnaissance

<!-- b000036 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
5

<!-- b000038 | contents | pages [2] -->
3 Notations

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
4 Model Preparations

<!-- b000041 | contents | pages [2] -->
6

<!-- b000042 | contents | pages [2] -->
4.1

<!-- b000043 | contents | pages [2] -->
Reconstruction of 3-Dimensional Topographic Map

<!-- b000044 | contents | pages [2] -->
. . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
6

<!-- b000046 | contents | pages [2] -->
4.2

<!-- b000047 | contents | pages [2] -->
Flight Time under Different Payload . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
7

<!-- b000049 | contents | pages [2] -->
4.3

<!-- b000050 | contents | pages [2] -->
Pattern of Onboard Camera Scanning

<!-- b000051 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
7

<!-- b000053 | contents | pages [2] -->
5 Models

<!-- b000054 | contents | pages [2] -->
8

<!-- b000055 | contents | pages [2] -->
5.1

<!-- b000056 | contents | pages [2] -->
Model of Delivering Supplies . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
8

<!-- b000058 | contents | pages [2] -->
5.1.1

<!-- b000059 | contents | pages [2] -->
Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
8

<!-- b000061 | contents | pages [2] -->
5.1.2

<!-- b000062 | contents | pages [2] -->
Models Design

<!-- b000063 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
8

<!-- b000065 | contents | pages [2] -->
5.1.3

<!-- b000066 | contents | pages [2] -->
A Possible Package Conﬁguration . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
10

<!-- b000068 | contents | pages [2] -->
5.2

<!-- b000069 | contents | pages [2] -->
Model of Reconnaissance . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
11

<!-- b000071 | contents | pages [2] -->
5.2.1

<!-- b000072 | contents | pages [2] -->
Importance Level of the Settlements . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
11

<!-- b000074 | contents | pages [2] -->
5.2.2

<!-- b000075 | contents | pages [2] -->
Importance Level of the Roads . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
12

<!-- b000077 | contents | pages [2] -->
5.2.3

<!-- b000078 | contents | pages [2] -->
Model Solving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
13

<!-- b000080 | contents | pages [2] -->
5.3

<!-- b000081 | contents | pages [2] -->
Combined Model of Delivering Supplies and Reconnaissance

<!-- b000082 | contents | pages [2] -->
. . . . . .

<!-- b000083 | contents | pages [2] -->
14

<!-- b000084 | contents | pages [2] -->
5.3.1

<!-- b000085 | contents | pages [2] -->
Best Locations and Packing Conﬁgurations . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
15

<!-- b000087 | contents | pages [2] -->
5.3.2

<!-- b000088 | contents | pages [2] -->
Delivery Routes and Schedule

<!-- b000089 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
16

<!-- b000091 | contents | pages [2] -->
5.3.3

<!-- b000092 | contents | pages [2] -->
Payload Packing Conﬁgurations . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
17

<!-- b000094 | contents | pages [2] -->
5.3.4

<!-- b000095 | contents | pages [2] -->
Flight Plan to Access Major Roads . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
17

<!-- b000097 | contents | pages [2] -->
6 Applying of Models

<!-- b000098 | contents | pages [2] -->
18

<!-- b000099 | contents | pages [2] -->
7 Sensitivity Analysis

<!-- b000100 | contents | pages [2] -->
18

<!-- b000101 | contents | pages [2] -->
7.1

<!-- b000102 | contents | pages [2] -->
Importance Level of Settlements

<!-- b000103 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [2] -->
18

<!-- b000105 | contents | pages [2] -->
7.1.1

<!-- b000106 | contents | pages [2] -->
Assigning Methods of Importance . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [2] -->
19

<!-- b000108 | contents | pages [2] -->
7.1.2

<!-- b000109 | contents | pages [2] -->
Underestimation of Some Settlements’ Importance

<!-- b000110 | contents | pages [2] -->
. . . . . . . .

<!-- b000111 | contents | pages [2] -->
19

<!-- b000112 | contents | pages [2] -->
7.2

<!-- b000113 | contents | pages [2] -->
Drones’ Maximum Navigation Radius . . . . . . . . . . . . . . . . . . . .

<!-- b000114 | contents | pages [2] -->
19

<!-- b000115 | contents | pages [2] -->
8 Strengths and Weaknesses

<!-- b000116 | contents | pages [2] -->
20

<!-- b000117 | contents | pages [2] -->
8.1

<!-- b000118 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
20

<!-- b000120 | contents | pages [2] -->
8.2

<!-- b000121 | contents | pages [2] -->
Weaknesses

<!-- b000122 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [2] -->
21

<!-- b000124 | contents | pages [2] -->
9 Future Work

<!-- b000125 | contents | pages [2] -->
21

<!-- b000126 | contents | pages [2] -->
10 Conclusions

<!-- b000127 | contents | pages [2] -->
21

<!-- b000128 | contents | pages [2] -->
11 Appendix

<!-- b000129 | contents | pages [2] -->
22

<!-- b000130 | contents | pages [2] -->
References

<!-- b000131 | furniture | pages [3] -->
Team # 1923964

<!-- b000132 | furniture | pages [3] -->
Page 1 of 23

<!-- b000133 | heading | pages [3] -->
Memo

<!-- b000134 | prose | pages [3] -->
Dear CEO of Help, Inc.:

<!-- b000135 | prose | pages [3] -->
Never in the ﬁeld of history are so many natural disasters faced by human-beings. We do appreciate Help, Inc.’s contribution to the recovery of Puerto Rico and it is out of our sincere hope that DroneGo system be enhanced. In response to your questions about the optimal design of DroneGo system in different scenarios, we are writing to inform you of our work of modelling.

<!-- b000136 | prose | pages [3] -->
We discuss your optimization objectives in different scenarios. With an urgent de- mand for medical resources, your only optimization objective is to minimize total time for delivering medical packages. In this case, we recommend you to apply our delivery model. This model uses Dijkstra Algorithm to solve for optimal locations of containers that minimize the total delivery time.

<!-- b000137 | prose | pages [3] -->
If the need of reconstructing road networks overwhelms medical demand, recon- noitering as many major roads as possible will be your single optimization objective. Acknowledging this, our reconnaissance model will suit you well. This model uses Particle Swarm Optimization(PSO) to solve for containers’ best locations which maxi- mize the total value of all roads reconnoitered.

<!-- b000138 | prose | pages [3] -->
In reality, medical demand and the need of reconstruction are both of great impor- tance. Sometimes your medical packages supply fails to meet the demand. This kind of problem should be solved by our combined multi-objective optimization model. Ac- tually, each objective will have a speciﬁc weight. These weights are to be determined according to speciﬁc scenarios. With given weights, our combined model will solve for best locations of containers and optimal packing conﬁguration, along with ﬂight plan and delivery routes.

<!-- b000139 | prose | pages [3] -->
Our most creative work is that we ﬁnd a both practical and convenient way to de- ﬁne each road’s importance level. We divide each road into segments. A segment is the indivisible part of a road, which connects two settlements without crossing another settlement. Each segment’s importance level is determined by the sum of the impor- tance levels of the two settlements located on its two endpoints.

<!-- b000140 | prose | pages [3] -->
We use general importance to express a settlement’s importance level. General importance is the sum of self importance and connective importance. We score each settlement’s self importance according to its scale. We deﬁne a settlement’s neighbor- ing settlements as the other settlements connected to it by a single segment. Then each settlement’s connective importance is the sum of self importance of all its neighboring settlements.

<!-- b000141 | prose | pages [3] -->
Following this rationale, we successfully transformed the importance of road into importance of settlement. Intuitively, a road with higher importance level will be of greater value. Therefore, to maximize the total value of roads reconnoitered, we can simply maximize the total value of settlements of all the roads reconnoitered.

<!-- b000142 | prose | pages [3] -->
In consideration of Puerto Ricos scenario, our models derive the results as follows. Locations of container 1, 2 that minimize total delivery time are (18.38, −65.85), (18.31, −66.09) respectively. And container 3 locates in the accessible surroundings of Arecibo. The sign ( , ) denotes ( latitude, longitude).

<!-- b000143 | prose | pages [3, 4] -->
Locations of containers that maximize the total importance value of roads recon- noitered are (18.36, −65.85) for container 1, (18.27, −66.12) for container 2 and (18.23, -66.76) for container 3.

<!-- b000144 | furniture | pages [4] -->
Team # 1923964

<!-- b000145 | furniture | pages [4] -->
Page 2 of 23

<!-- b000147 | prose | pages [4] -->
Now consider multi-objective optimization situation. In Puerto Rico scenario, sim- ple calculation shows that the medical packages’ supply can easily meet the demand over 1 year. Therefore, we do not need to worry about the amount of medical packages. Besides, computer process shows that every point in the feasible region of delivery pos- sesses very similar total delivery time. Thus, minimizing total delivery time is not the major optimization objective. We just need to ﬁnd the locations that maximize total importance value of roads reconnoitered in the feasible region. The model’s results are as follows.

<!-- b000148 | prose | pages [4] -->
Best locations of containers (18.36, −65.85) for container 1, (18.27, −66.12) for con- tainer 2 and (18.23, −66.76) for container 3.

<!-- b000149 | prose | pages [4] -->
Flight plan and routes A drone F will deliver supplies between Bayamon and San Pablo, while a drone B between San Juan and Fajardo. Besides, each of the three drone B’s will navigate in one of the three reconnaissance areas, observing roads from close to far away.

<!-- b000150 | prose | pages [4] -->
Packing conﬁgurations of the drones Our drone ﬂeet consists of drone B and drone F. We pack all the medical packages required by a certain destination each day into a single parcel. Therefore, each drone’s payload packing conﬁguration is the corresponding parcel required by each city.

<!-- b000151 | prose | pages [4] -->
Conﬁgurations of containers Container 1 includes 1908 MED 1, 954 MED 2 and 954 MED 3. Container 2: includes 1224 MED 1, 306 MED 2 and 918 MED 3. Container 3 includes 3720 MED 1.

<!-- b000152 | prose | pages [4] -->
Before you get to apply our models, here are things worth your attention. First, sensitivity tests show that our models will not be affected too much by methods of as- signing importance but will be considerably impacted by the individual changes of im- portance. Therefore, to ensure effectiveness, you need to correctly rank all settlements’ importance levels. The way of assigning importance levels is not much important as long as the order of levels is correct. Second, the variation of navigation radius make inﬂuence on the best locations. So you need to identify the actual navigation radius of drones.

<!-- b000153 | prose | pages [4] -->
In conclusion, From an overall perspective, we separate the problem into two mis- sions and establish models for them respectively. For the overall design, we focus on the reality by considering three practicable factors. For the design of two individual models, we pay more attention to the practicability by sorting out the feasible groups of destinations, introducing segments and importance evaluation function. The com- bination of the two models is natural and derives the comprehensive results including the ﬂeets’ composition, each drone’s payload conﬁgurations, delivery route, schedule and ﬂight plan as well as the containers’ best locations and packing conﬁgurations.

<!-- b000154 | prose | pages [4] -->
Thank you again for considering our models and hope our models will be of help to your cause!

<!-- b000155 | prose | pages [4] -->
Yours Sincerely,

<!-- b000156 | furniture | pages [4] -->
Team #1923964

<!-- b000157 | furniture | pages [5] -->
Team # 1923964

<!-- b000158 | furniture | pages [5] -->
Page 3 of 23

<!-- b000159 | heading | pages [5] -->
1 Introduction

<!-- b000160 | prose | pages [5] -->
The sudden attack of the savage hurricane on Puerto Rico in 2017 caused immea- surable loss of lives and property. It must be depressing to witness the devastating power of the storm surge and wave action brought by the hurricane. The only comfort that can convey strengths and conﬁdence to the inhabitants is the adequate and timely assistance from the outside world, which makes our work meaningful in the future.

<!-- b000161 | prose | pages [5] -->
Due to the serious damage of infrastructures including roads, poles and transmis- sion lines, the inhabitants are probably in short of transportation and electricity, which insulates them entirely from the emergency teams. In addition, the unclearness of the inside damage retards the rescuing progress. Thus, we must utilize the drones of high mobility to deliver indispensable supplies as well as implement reconnaissance for the next-step ground transportation. Lives are suffering with seconds elapsing, so the res- cuing work must hurry!

<!-- b000162 | heading | pages [5] -->
1.1 Problem Restatement

<!-- b000163 | prose | pages [5] -->
We need to develop a disaster relief response system named DroneGo Fleet and im- prove its response capabilities based on the situations of Puerto Rico in 2017.

<!-- b000164 | prose | pages [5] -->
• What we Know:

<!-- b000165 | prose | pages [5] -->
– 5 different destinations – Complete geographic information of Puerto Rico

<!-- b000166 | prose | pages [5] -->
• What we Have:

<!-- b000167 | prose | pages [5] -->
– 7 kinds of drones (A-G) with their sizes, performances and conﬁgurations capabilities as well as a tethered equipment (H) – 3 kinds of pre-packaged medical supplies with their size – 3 ISO standard dry cargo containers with given sizes

<!-- b000168 | prose | pages [5] -->
• What we Should Do

<!-- b000169 | heading | pages [5] -->
1. Arrange the ﬂight. For single objective of delivering supplies, select speciﬁc

<!-- b000170 | prose | pages [5] -->
drones and design the packing conﬁgurations for up to 3 cargo containers.

<!-- b000171 | heading | pages [5] -->
2. Identify the best locations. Cargo containers can be set here for drones to

<!-- b000172 | prose | pages [5] -->
achieve the optimal effect of both delivering and reconnoitring targets.

<!-- b000173 | heading | pages [5] -->
3. Propose dispatching schedule. Assign payload packing conﬁgurations, de-

<!-- b000174 | prose | pages [5] -->
livery routes separately and ﬂight plan to each type of drones.

<!-- b000175 | heading | pages [5] -->
1.2 Our Work

<!-- b000176 | prose | pages [5] -->
In our paper, we establish three models to solve the problem. Starting from sim- plicity, we consider delivery and reconnaissance separately and design two single- objective optimization models. To achieve a comprehensive solution, we combine the two models as a multi-objective optimization model.

<!-- b000177 | prose | pages [5, 6] -->
To make models close to reality, we take several practical factors into account. They are • The inﬂuence of the hilly topography whose surface is mostly uneven;

<!-- b000178 | furniture | pages [6] -->
Team # 1923964

<!-- b000179 | furniture | pages [6] -->
Page 4 of 23

<!-- b000180 | caption | pages [6] -->
Figure 1: Solving strategy

<!-- b000182 | prose | pages [6] -->
• The inﬂuence of payload on the drones’ navigation radius;

<!-- b000183 | prose | pages [6] -->
• The inﬂuence of the scanning pattern of onboard cameras.

<!-- b000184 | prose | pages [6] -->
A crucial problem is discussed in the paper about how to evaluate the effectiveness of reconnaissance. To make it clear, we introduce importance level of settlements and segments (the smallest compartments of roads) and an importance evaluation function.

<!-- b000185 | prose | pages [6] -->
Since the response system is developed for the potential future crisis, we apply our model to another island country. The application shows that our models are meaning- ful and universal.

<!-- b000186 | prose | pages [6] -->
For sensitivity analysis, we vary the parameters including the importance levels and the drones’ navigation radius and derive corresponding results. The tests and comparisons demonstrate the robustness of our models.

<!-- b000187 | heading | pages [6] -->
2 Assumptions and Justiﬁcations

<!-- b000188 | heading | pages [6] -->
2.1 General Assumptions

<!-- b000189 | prose | pages [6] -->
• The economic expenses are almost ﬁxed.

<!-- b000190 | prose | pages [6] -->
Because of the ﬁxed number of containers and the deﬁnite requirement of minimizing the used space of each container, the total cost on materials is almost ﬁxed.

<!-- b000191 | prose | pages [6] -->
• Compared to the materials’ cost, the ﬂying cost is negligible.

<!-- b000192 | prose | pages [6] -->
A previous study in Lesotho indicated that each trip cost only 24 cents while the cost on base stations and drones are $900,000.[12]

<!-- b000193 | prose | pages [6] -->
• All drones are equipped with an ample number of batteries.

<!-- b000194 | prose | pages [6] -->
• All drones have to return to corresponding containers for battery replacement after each ﬂight.

<!-- b000195 | prose | pages [6] -->
The above two assumptions are based on that most searching and rescuing drones are powered by electricity.[1] This is a compulsory condition because of the lack of power throughout the disaster area.

<!-- b000196 | prose | pages [6] -->
• The volume and mass of batteries are ignored.

<!-- b000197 | prose | pages [6] -->
• The feasible response region of the drones is large enough to cover the entire island.

<!-- b000198 | furniture | pages [7] -->
Team # 1923964

<!-- b000199 | furniture | pages [7] -->
Page 5 of 23

<!-- b000200 | prose | pages [7] -->
This requirement is practicable since the control radius of the drones of industrial grade can reach about 30km[2], which is larger than their maximum navigation radius dis- cussed in Subsection 4.2.

<!-- b000201 | prose | pages [7] -->
• People can load or download the drones’ packages in every delivering task.

<!-- b000202 | prose | pages [7] -->
• The time of drones’ ascending and descending is ignored.

<!-- b000203 | prose | pages [7] -->
This is because the drones cannot ﬂy over 120m.[8] The maximum ascending speed is about 5m/s.[13]

<!-- b000204 | prose | pages [7] -->
• The inﬂuence area of each distribution centre is almost a circle determined by the drones’ navigation radius.

<!-- b000205 | heading | pages [7] -->
2.2 Assumptions of Delivering Supplies

<!-- b000206 | prose | pages [7] -->
• The longer the drones stay in the air, the greater the probability of failure is.

<!-- b000207 | prose | pages [7] -->
Flying task is of great risk because of the complex terrains and the changeful tropical climate in Puerto Rico. More speciﬁcally, the working time of each aerial mission obeys exponential distribution.

<!-- b000208 | prose | pages [7] -->
• For safety considerations, the government should be able to transport as many medical packages to the disaster-stricken area as possible.

<!-- b000209 | heading | pages [7] -->
2.3 Assumptions of Reconnaissance

<!-- b000210 | prose | pages [7] -->
In addition to all the assumptions above, we hypothesize

<!-- b000211 | prose | pages [7] -->
• The vegetation height does not hinder the camera’s photographic effect.

<!-- b000212 | prose | pages [7] -->
Compared to the ﬂight attitude that can reach over 120m, the height of the dominant shrub layer (usually 6-10m) can be ignored.[7][8]

<!-- b000213 | prose | pages [7] -->
• The time consumed for the onboard cameras’ rotating is ignored.

<!-- b000214 | heading | pages [7] -->
3 Notations

<!-- b000215 | prose | pages [7] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000216 | furniture | pages [8] -->
Team # 1923964

<!-- b000217 | furniture | pages [8] -->
Page 6 of 23

<!-- b000218 | caption | pages [8] -->
Table 1: Notations

<!-- b000219 | prose | pages [8] -->
Symbol Deﬁnition

<!-- b000220 | prose | pages [8] -->
T0 Maximum ﬂight time with no cargo Tf Maximum ﬂight time with full cargo v Flying speed of the drones H Flying height of the drones r Maximum navigation radius R Maximum scanning radius of onboard cameras A Distance Matrix E(·) Importance evaluation function si Self importance of settlement i ci Connective importance of settlement i gi General importance of settlement i

<!-- b000221 | heading | pages [8] -->
4 Model Preparations

<!-- b000222 | heading | pages [8] -->
4.1 Reconstruction of 3-Dimensional Topographic Map

<!-- b000223 | prose | pages [8] -->
To make calculations close to real circumstances, especially when Puerto Rico lo- cates on a hilly island, we should take the uneven ground into consideration.

<!-- b000224 | prose | pages [8] -->
We sample over 110 discrete data points from Google Maps of Puerto Rico and use interpolation to simulate the topography by Matlab.[3]

<!-- b000225 | caption | pages [8] -->
Figure 2: The 3-dimensional map of Puerto Rico

<!-- b000226 | prose | pages [8] -->
Interpolation generates a large number of grids and identiﬁes their altitude ordi- nates. These discrete points are dense enough to rebuild the 3-dimensional map.

<!-- b000227 | prose | pages [8] -->
Instead of deriving geodesic curve, we use Dijkstra algorithm to calculate the min- imum distance between any two points on the land surface. Thus, the ﬂying distance can be determined more accurately and realistically than the 2-dimentional situations.

<!-- b000228 | furniture | pages [9] -->
Team # 1923964

<!-- b000229 | furniture | pages [9] -->
Page 7 of 23

<!-- b000230 | heading | pages [9] -->
4.2 Flight Time under Different Payload

<!-- b000231 | prose | pages [9] -->
Since the ﬂight time decreases as the drone’s payload increases, we should realize that reaching the same distance, each ﬂight should have different time consumed on the delivering trip and the returning trip.

<!-- b000232 | prose | pages [9] -->
We select points from the working curves (see in Appendix [4]) and ﬁt them into negative exponential function T = T0e−λb (1)

<!-- b000233 | prose | pages [9] -->
where T refers to ﬂight time while b refers to the payload in unit of lbs. We derive sequently T = 29.23e−0.08498b r = −0.9981 T = 34.63e−0.08187b r = −0.9992 T = 37.80e−0.07689b r = −0.9989

<!-- b000234 | prose | pages [9] -->
for the three working curves lower in the ﬁgure. We assume that λ is a function of T0, and then we derive λ of different T0 given in problem by spline interpolation from the above data. Substituting λ, T0 and maximum payload b into eqn(4.2), we get Tf for each type of drones.

<!-- b000235 | prose | pages [9] -->
Just to be safe, we choose maximum ﬂight time with full cargo to calculate the maximum navigation radius. As described in assumptions, the drones have to return back after each delivering, so radius r = v × Tf/2, which is shown in the table below.

<!-- b000236 | caption | pages [9] -->
Table 2: Navigation radius of different types of the drones

<!-- b000237 | prose | pages [9] -->
Maximum Navigation T0(min) Tf(min) Drone Speed(km/h) Payload(lbs) Radius(km)

<!-- b000238 | prose | pages [9] -->
A 40 35 34.02 3.5 11.34 B 79 40 37.76 8 24.86 C 64 35 31.23 14 16.66 D 60 18 16.67 11 8.34 E 60 15 13.69 15 6.85 F 79 24 20.06 22 13.21 G 64 16 14.08 20 7.51

<!-- b000239 | heading | pages [9] -->
4.3 Pattern of Onboard Camera Scanning

<!-- b000240 | prose | pages [9] -->
The area covered by the onboard camera is determined by the drones’ ﬂight alti- tude, H, as well as the required resolution of picture.

<!-- b000241 | prose | pages [9, 10] -->
Let θ be the camera lens’ angle of view, and α be the angle between vertical line and the angular bisector of θ. α actually signiﬁes the direction that camera points towards. Since the camera can rotate and point towards a number of directions, the covering area is a circle with a radius of R. Obviously, as α increases, the covering area increases. However, the requirement of high resolution limit the maximum detectable distance. From technical instruction, we use the following equation to calculate.[10] (Field of View(FOV) Sensor Resolution = Image Resolution = 2 Smallest Feature From Figure 3, we derive

<!-- b000242 | furniture | pages [10] -->
Team # 1923964

<!-- b000243 | furniture | pages [10] -->
Page 8 of 23

<!-- b000244 | caption | pages [10] -->
Figure 3: The illustration of onboard camera scanning

<!-- b000246 | prose | pages [10] -->
FOV + H tan(α −θ/2) = H tan(α + θ/2)

<!-- b000247 | prose | pages [10] -->
R = H tan(α + θ/2)

<!-- b000248 | prose | pages [10] -->
For pictures with 1080p whose resolution is 1920×1080, we choose the smaller value 1080 as the sensor resolution. We set smallest feature as 5 metres, the mean width of roads on Puerto Rico, and H as 120 metres, the US legal altitude of drones.[11] From four kinds of commercially available DJI drones, we set θ as 72◦.[9] Thus, we get α = 51.5◦, R = 2.75km.

<!-- b000249 | heading | pages [10] -->
5 Models

<!-- b000250 | heading | pages [10] -->
5.1 Model of Delivering Supplies

<!-- b000251 | prose | pages [10] -->
In this part, our single purpose is to deliver medical supplies.

<!-- b000252 | heading | pages [10] -->
5.1.1 Analysis

<!-- b000253 | prose | pages [10] -->
The problem requires us to recommend a composition of the drone ﬂeet and pro- vide the best locations for containers. Obviously, the two requirements are not inde- pendent. For each possible location, there may exist an optimal composition of the drones. Thus, it is a multi-objective optimization problem. Hoping to obtain the opti- mal solution, we are going to transform it into a single-objective optimization problem. Here, we construct the objective function as the total ﬂight time.

<!-- b000254 | heading | pages [10] -->
5.1.2 Model Design

<!-- b000255 | prose | pages [10] -->
Assume that there is a number n of destinations, a number m of kinds of drones and a number l of cargo containers.

<!-- b000256 | furniture | pages [11] -->
Team # 1923964

<!-- b000257 | furniture | pages [11] -->
Page 9 of 23

<!-- b000258 | prose | pages [11] -->
Here we have essential preparation works for models design.

<!-- b000259 | prose | pages [11] -->
For a given set of destinations, we derive a Distance Matrix A= (aij)n×n, where aij is the distance between destination i and destination j.

<!-- b000260 | prose | pages [11] -->
We construct a Destinations Combination Matrix B. It is a 0-1 matrix. Let each of its rows represent a combination of destinations. Thus, there are 2n −1 rows1 and n columns.

<!-- b000261 | prose | pages [11] -->
{ 0 if destination j does not exist in the combination i bij = 1 if destination j exists in the combination i i = 1, 2, · · · , 2n −1 αi = (bi1, bi2, · · · , bin) αi denotes a row vector of B.

<!-- b000262 | prose | pages [11] -->
Similarly, we construct a Drones Combination Matrix D. βj(j = 1, 2, · · · , 2m−1) is a row vector of D

<!-- b000263 | prose | pages [11] -->
Deﬁnition 1. If all drones included in a speciﬁc combination βj are able to arrive at all destinations included in a speciﬁc combination αi, then there exists a corresponding relationship between βj and αi

<!-- b000264 | prose | pages [11] -->
Deﬁnition 2. If for αi and αj, there not exists integer k from 1 to n to make bik = bjk = 1, then αi∩αj=∅.

<!-- b000265 | prose | pages [11] -->
Deﬁnition 3. Group is a combination of row vectors.

<!-- b000266 | prose | pages [11] -->
For example, βi, βj and βk form a group {βi, βj, βk}. Naturally, we have βi∩{βj, βk}= βi∩βj∩βk.

<!-- b000267 | prose | pages [11] -->
Since each αi possibly corresponds to a βj, we construct a mapping f. f(i) = j signiﬁes that αi corresponds to a βj. When there are more than one βj that can satisfy Deﬁnition 1, let f(i) be the subscript of the βj that contains the most drones.

<!-- b000268 | prose | pages [11] -->
With all the above preparation works, we give a strategy to solve the problem.

<!-- b000269 | prose | pages [11] -->
Procedure 1: Sort out the isolated destinations Check whether there exists the destinations whose distances from all other desti- nations exceed the largest maximum ﬂight radius of all available drones. If there exists, assign an individual container for each of them.

<!-- b000270 | prose | pages [11] -->
Procedure 2: Find out all possible groups

<!-- b000271 | prose | pages [11] -->
Step 0 Let i=1.

<!-- b000272 | prose | pages [11] -->
Step 1 For any k̸ = i, examine whether αk∩{αi}=∅. If yes, add αk into the group {αi} to get {αi, αk} and make l = l −1.

<!-- b000273 | prose | pages [11] -->
Step 2 Judgement: If ∑ αi∈group αj = (1, 1, · · · , 1 ) and l ≥0, and there is no such a group | {z } all 1 before, keep the group in reserve. Let i = i + 1, back to Step 1.

<!-- b000274 | prose | pages [11] -->
If ∑ αi∈group αj̸ = (1, 1, · · · , 1 ) and l ≥0, back to Step 2. | {z } all 1 If i > 2n −1, end and retrieve all possible groups.

<!-- b000275 | prose | pages [11, 12] -->
1This is because ∑n i=1 = 2n −1 Procedure 3: Derive the optimal point of all possible groups

<!-- b000276 | furniture | pages [12] -->
Team # 1923964

<!-- b000277 | furniture | pages [12] -->
Page 10 of 23

<!-- b000279 | prose | pages [12] -->
Step 1 For each possible group, using the mapping f to ﬁnd the available βj according to the αi in the group.

<!-- b000280 | prose | pages [12] -->
Step 2 For each pair of αi and βj, utilize Greedy strategy to allocate different drones to the required air lines and consider the corresponding total ﬂight time as the minimum time of the group.

<!-- b000281 | prose | pages [12] -->
Notice: If for a pair of αi and βj, there is only one element 1 in αi, (there is only one destination in that combination) then selects the drone whose required number of ﬂight is the least and use the equation number of ﬂight needed×maximum ﬂight time to calculate the time needed.2 2

<!-- b000282 | prose | pages [12] -->
Procedure 4: Compare all groups’ optimal point and select the best

<!-- b000283 | heading | pages [12] -->
5.1.3 A Possible Package Conﬁguration

<!-- b000284 | prose | pages [12] -->
As assumptions described before, the drones are equipped with an ample number of batteries. Since ﬂying time is short, we can utilize only one drone to run the air lines between a speciﬁc destination and a speciﬁc container. Denote the container carrying drone B as container 1, the other as container 2, the one assigned to Arecibo as container 3.

<!-- b000285 | prose | pages [12] -->
From estimation we can ﬁnd that if we simply put one B into container 1 and load MED 1 and MED 3 as packages (roughly in the size and shape of 14×7×9 cuboids) vertically into the container, more than 1900 packages of MED 1 and 1900 packages of MED 3 can be loaded into container 1. Under the consuming speed offered in the problem background[5][6], the amount of medical packages can cope with two years consumption. This is totally plausible.

<!-- b000286 | prose | pages [12] -->
In container 2, we pack the medical supplies needed each day (including 2 MED 1, 2 MED 2 and 6 MED 3) into a single pile, roughly in the size and shape of a 14×14×20 cuboid. The combination of a pile is because container 2 is obliged to give considera- tion to 3 destinations in the meantime. Thus, if we only load one F into container 2, we can load more than 324 piles, which is deﬁnitely enough for Puerto Rico.

<!-- b000287 | prose | pages [12] -->
As for Arecibo, we simply ﬁll the container 3 with a drone B and as many MED 1 as possible.

<!-- b000288 | prose | pages [12] -->
In general, the package conﬁgurations for delivering purpose only are stated as follow.

<!-- b000289 | prose | pages [12] -->
Drone Packing Container Destination Locations Fleet Conﬁgurations

<!-- b000290 | prose | pages [12] -->
San Juan 1908 MED 1 (18.38, −65.85) 1 B Fajardo 954 MED 2, 954 MED 3

<!-- b000291 | prose | pages [12] -->
Bayamon 1296 MED 1 (18.31, −66.09) 2 F Cauguas 324 MED 2, 972 MED 3

<!-- b000292 | prose | pages [12] -->
in the accessible 3 Arecibo B 3720 MED 1 surrounding of Arecibo

<!-- b000293 | prose | pages [12] -->
2This is a compromise. Otherwise, the situation that container should locate deﬁnitely on the desti- nation is contrary to common sense.

<!-- b000294 | furniture | pages [13] -->
Team # 1923964

<!-- b000295 | furniture | pages [13] -->
Page 11 of 23

<!-- b000296 | heading | pages [13] -->
5.2 Model of Reconnaissance

<!-- b000297 | prose | pages [13] -->
To make the problem clearer step by step, we establish the model for reconnais- sance purpose only before considering both missions at the same time.

<!-- b000298 | prose | pages [13] -->
The target of video reconnaissance is to report the potential damaged road net- works. One of the optimization objectives is to maximize the effectiveness. We need to make clear what contributes to the effectiveness. Thus, a measurement of the impor- tance of speciﬁc constructions is introduced below.

<!-- b000299 | heading | pages [13] -->
5.2.1 Importance Level of the Settlements

<!-- b000300 | prose | pages [13] -->
Obviously, the larger the scale of a settlement is and the more roads connected it with other settlements, the more important the settlement would be. Thus, a set- tlements importance is combined by self importance, denoted by S and connective importance, denoted by C. The sum of S and C is deﬁned as a settlements general importance, denoted by G.

<!-- b000301 | prose | pages [13] -->
The self importance, S, depends on the city level. We divide all settlements on Puerto Rico into six categories as follow.

<!-- b000302 | prose | pages [13] -->
Number one is the region capital San Juan. Number two is the second largest city in Puerto Rico, Payamon. Number three is district capital, for example Mayaguez. Notice that some intersections of some roads are not settlements at all but simply road crossings. Few people live around these endpoints. We consider these crossings as the ﬁfth kind of settlements. We score ﬁve kinds of settlements with integer scores 1 to 5. The higher the city level is, the higher the score it gets. We denote the following score of city level as individual importance.

<!-- b000303 | prose | pages [13] -->
Settlements Categories Example Self Importance

<!-- b000304 | prose | pages [13] -->
1 San Juan (Capital) 6 2 Payamon (Second Largest) 5 3 Mayaguez, etc (District Capital) 4 4 Yellow tinted areas 3 5 Small circles areas 2 Intersection not 6 1 highlighted on map

<!-- b000305 | prose | pages [13] -->
Previous to discussion about connective importance, we need to introduce a Con- nection Matrix to describe the relationship of all settlements.

<!-- b000306 | prose | pages [13] -->
Connection Matrix X is a 0-1 matrix.

<!-- b000307 | prose | pages [13] -->
  · · · x11 x12 x1n   · · · x21 x22 x2n   X =   ... ... ...   · · · xn1 xn2 xnn

<!-- b000308 | prose | pages [13, 14] -->
when i = j, xi,j=0 when i̸ = j { 0 if there is no segment connecting settlement i and settlement xi,j = 1 if there is a segment connecting settlement i and settlement n is the total number of settlements. We sample 46 points in all from the given map and set n = 46. Segment is deﬁned later in Deﬁnition 4.

<!-- b000309 | furniture | pages [14] -->
Team # 1923964

<!-- b000310 | furniture | pages [14] -->
Page 12 of 23

<!-- b000312 | prose | pages [14] -->
A settlement’s connective importance, C, depends on the other settlements con- nected to it with a segment. We deﬁne connective importance of settlement i as

<!-- b000313 | prose | pages [14] -->
n ∑ ci = sjxi,j j=1

<!-- b000314 | prose | pages [14] -->
where sj is the self importance of settlement i.

<!-- b000315 | prose | pages [14] -->
Hence, we derive C = XS where C=(c1, c2, . . . , cn)T is the connective importance vector, S=(s1, s2, . . . , sn)T is the self importance vector.

<!-- b000316 | prose | pages [14] -->
Combining the two aspects of importance, we get general importance.

<!-- b000317 | prose | pages [14] -->
G = S + C = IS + XS = (I + X)S (2)

<!-- b000318 | prose | pages [14] -->
where I is the identity matrix. The physical meaning of the equation is self-evident that general importance depends on settlement itself as well as the surrounding networks. If we use the function E(·) to evaluate the importance of settlement i, then E(i) = gi.

<!-- b000319 | heading | pages [14] -->
5.2.2 Importance Level of the Roads

<!-- b000320 | prose | pages [14] -->
For purpose of ground-based route planning, we need to rank the roads according to their importance. A trip of reconnaissance covering more roads of greater impor- tance would bring more beneﬁt. Thus, we need to deﬁne each roads importance level.

<!-- b000321 | prose | pages [14] -->
First, we need to keep in mind what a road is. Notice that every road on Puerto Rico is divided by the settlements located on it. Therefore, roads are divided by settlements into small segments. The indivisible part of a road is the segment which connects two settlements without crossing another segment. As shown in the ﬁgure below, line segment AB and BC are indivisible parts of road L, while AC is not. Hence, we give an exact deﬁnition of segment.

<!-- b000322 | caption | pages [14] -->
Figure 4: The illustration of segment and road

<!-- b000323 | prose | pages [14] -->
Deﬁnition 4. Segment is the indivisible part of a road, which connects two settlements and not crossing other settlements.

<!-- b000324 | prose | pages [14] -->
Obviously, segments are the minimum compositions of a road. It will be straight- forward and practical to deﬁne each segments importance level and then rank all seg- ments according to the levels. Undoubtedly, segments with higher importance level should be reconnoitered and restored more quickly.

<!-- b000325 | furniture | pages [15] -->
Team # 1923964

<!-- b000326 | furniture | pages [15] -->
Page 13 of 23

<!-- b000327 | prose | pages [15] -->
A segments importance depends on the two settlements it connects. Segments themselves are of little importance. Only if a segment connects two important set- tlements will it become important.

<!-- b000328 | prose | pages [15] -->
We use function E(·) to evaluate importance. For convenience and easiness to comprehend, we derive E(ij) = E(i) + E(j) (3)

<!-- b000329 | prose | pages [15] -->
where ij signiﬁes the segment that connects two settlements i and j.

<!-- b000330 | prose | pages [15] -->
Since E(i) = gi, E(ij) = gi + gj. Therefore, the importance evaluation of seg- ments, the most tiny compartments of roads, is transformed into the importance eval- uation of settlements.

<!-- b000331 | prose | pages [15] -->
By the evaluation introduced above, we abstract the map into the combination of nodes and lines by UCINET, as shown in Figure 6. For settlements whose general importance varies between 4 and 8, we signify them as grey up-triangles. For settle- ments whose general importance varies between 9 and 12, we signify them as yellow diamonds. For settlements whose general importance varies between 13 and 16, we signify them as purple inverted-triangles. For settlements whose general importance varies between 17 and 20, we signify them as red circles. For settlements whose gen- eral importance is larger than 20, we signify them as black tinted areas. The relative sizes of the nodes depend on their absolute value of general importance.

<!-- b000332 | caption | pages [15] -->
Figure 5: The abstract expression of settlements and segments

<!-- b000333 | heading | pages [15] -->
5.2.3 Model Solving

<!-- b000334 | prose | pages [15] -->
We hope to identify the best locations for cargo containers. With the previous eval- uation of importance of segments and settlements, we set the objective function Z as the sum of importance of all segments that lie in the covered area of the drones. It can be converted into the function of the general importance of settlements.

<!-- b000335 | prose | pages [15] -->
∑ ∑ Z = E(ij) = (gi + gj) (4) ij∈Ω ij∈Ω

<!-- b000336 | prose | pages [15] -->
where Ωis the drones’ detectable area, a circle determined by their maximum naviga- tion radius r plus scanning radius R.

<!-- b000337 | prose | pages [15] -->
For problem whose independent variables are locations, Particle Swarm Optimiza- tion(PSO) is a good solution.

<!-- b000338 | furniture | pages [16] -->
Team # 1923964

<!-- b000339 | furniture | pages [16] -->
Page 14 of 23

<!-- b000340 | prose | pages [16] -->
Step 0 Initialize a great number of particles in the feasible region. The particles possess 3 dimensions including longitude, latitude and velocity.

<!-- b000341 | prose | pages [16] -->
Step 1 Set the feasible region as a circle whose centre is the speciﬁc particle’s location and radius is r + R.

<!-- b000342 | prose | pages [16] -->
Step 2 Identify the settlements locating within the feasible region.

<!-- b000343 | prose | pages [16] -->
Step 3 Identify the connective relationship among the settlements by the connective matrix C.

<!-- b000344 | prose | pages [16] -->
Step 4 Sum up the general importance of the connecting settlements as equation 5.2.3 shows.

<!-- b000345 | prose | pages [16] -->
Step 5 Particles adjust their locations and velocity according to their value of Z. Back to Step 1.

<!-- b000346 | prose | pages [16] -->
Finally, most particles would converge to the location where there is the largest value of Z. Thus, we derive the location, from which the drones’ coverage reach the maximum importance.

<!-- b000347 | prose | pages [16] -->
Since drone B possess the largest ﬂight radius among A H, it is the most suitable choice. For the reconnoitring problem across the whole island, we get the result as below.

<!-- b000348 | prose | pages [16] -->
18.5 Quebradillas Arecibo Barceloneta Dorado Manati Aguadilla San Juan Unnamed 6 18.4 Bayamon Rio Grande Centrol Puntas Corozal San Sebastian Fajardo 18.3 Lares Utuado Aguas Buenas Utuado' Jayuya Caguas Comerio latitude/° Juncos Orocovis Naguabo San Lorenzo 18.2 Mayaguez Canstaner Unnamed 4 Unnamed 3 Adjuntas Unnamed 1 Indiera Alta Humacao Unnamed 5 Unnamed 2 Cayey 18.1 San German Coamo Yauco Ponce Maunabo 18 Cabo Rojo Guayama Ensenada Santa Isabel Punta Figuras

<!-- b000349 | prose | pages [16] -->
17.9 -67.4 -67.2 -67 -66.8 -66.6 -66.4 -66.2 -66 -65.8 -65.6 longtitude/°

<!-- b000350 | caption | pages [16] -->
Figure 6: The global result of Particles Swarm Optimization

<!-- b000351 | prose | pages [16] -->
Another practicable method is exhaustion. By generating a huge number of grids that divide the feasible region into tiny parts, we calculate each point’s value of Z and ﬁnd the maximum among them. The steps are similar to the above and the result is as shown below.

<!-- b000352 | heading | pages [16] -->
5.3 Combined Model of Delivering Supplies and Reconnaissance

<!-- b000353 | prose | pages [16, 17] -->
In this part, we combine the two models established in section 5.1 and 5.2, and obtain a comprehensive solution to the problem. Notice that drone F cannot implement reconnaissance. We add one drone B to the container that supplies packages for San Pablo and Bayamon.

<!-- b000354 | furniture | pages [17] -->
Team # 1923964

<!-- b000355 | furniture | pages [17] -->
Page 15 of 23

<!-- b000356 | caption | pages [17] -->
Figure 7: The global result of exhaustion

<!-- b000358 | heading | pages [17] -->
5.3.1 Best Locations and Packing Conﬁgurations

<!-- b000359 | prose | pages [17] -->
18.6

<!-- b000360 | prose | pages [17] -->
18.5 Quebradillas Quebradillas Quebradillas Quebradillas Arecibo Arecibo Arecibo Arecibo Barceloneta Barceloneta Barceloneta Barceloneta Dorado Dorado Dorado Dorado Manati Manati Manati Manati Aguadilla Aguadilla Aguadilla Aguadilla San Juan San Juan San Juan San Juan Unnamed 6 Unnamed 6 Unnamed 6 Unnamed 6 18.4 Bayamon Bayamon Bayamon Bayamon Rio Grande Rio Grande Rio Grande Rio Grande Centrol Puntas Centrol Puntas Centrol Puntas Centrol Puntas Corozal Corozal Corozal Corozal San Sebastian San Sebastian San Sebastian San Sebastian Fajardo Fajardo Fajardo Fajardo 18.3 Lares Lares Lares Lares latitude/° Utuado Utuado Utuado Utuado Aguas Buenas Aguas Buenas Aguas Buenas Aguas Buenas Utuado' Utuado' Utuado' Utuado' Jayuya Jayuya Jayuya Jayuya Caguas Caguas Caguas Caguas Comerio Comerio Comerio Comerio Juncos Juncos Juncos Juncos Orocovis Orocovis Orocovis Orocovis Naguabo Naguabo Naguabo Naguabo San Lorenzo San Lorenzo San Lorenzo San Lorenzo 18.2 Mayaguez Mayaguez Mayaguez Mayaguez Canstaner Canstaner Canstaner Canstaner Unnamed 3Unnamed 4 Unnamed 3Unnamed 4 Unnamed 3Unnamed 4 Unnamed 3Unnamed 4 Adjuntas Adjuntas Adjuntas Adjuntas Unnamed 1 Unnamed 1 Unnamed 1 Unnamed 1 Indiera Alta Indiera Alta Indiera Alta Indiera Alta Humacao Humacao Humacao Humacao Unnamed 5 Unnamed 5 Unnamed 5 Unnamed 5 Unnamed 2 Unnamed 2 Unnamed 2 Unnamed 2 Cayey Cayey Cayey Cayey 18.1 San German San German San German San German Coamo Coamo Coamo Coamo Yauco Yauco Yauco Yauco Ponce Ponce Ponce Ponce Maunabo Maunabo Maunabo Maunabo 18 Cabo Rojo Cabo Rojo Cabo Rojo Cabo Rojo Guayama Guayama Guayama Guayama Ensenada Ensenada Ensenada Ensenada Santa Isabel Santa Isabel Santa Isabel Santa Isabel Punta Figuras Punta Figuras Punta Figuras Punta Figuras 17.9

<!-- b000361 | prose | pages [17] -->
-67.2 -67 -66.8 -66.6 -66.4 -66.2 -66 -65.8 -65.6 longtitude/°

<!-- b000362 | caption | pages [17] -->
Figure 8: The PSO algorithm identiﬁes the best locations of 3 containers.

<!-- b000363 | prose | pages [17] -->
As shown in Section 5.2, the PSO algorithm is used again to identify the best loca- tions of cargo containers. But differently, since we need to meet the demand of the an- ticipated medical supplies, we shall narrow the feasible region according to the drones’ maximum navigation radius. The results of PSO give the best locations as below.

<!-- b000364 | furniture | pages [18] -->
Team # 1923964

<!-- b000365 | furniture | pages [18] -->
Page 16 of 23

<!-- b000366 | prose | pages [18] -->
Destinations Drone Packing Container Location to Supply Fleet Conﬁgurations

<!-- b000367 | prose | pages [18] -->
San Juan 1908 MED 1, 954 MED 2 (18.36, −65.85) 1 B Fajardo 954 MED 3

<!-- b000368 | prose | pages [18] -->
Bayamon 1224 MED 1, 306 MED 2 (18.27, −66,12) 2 B, F Caguas 918 MED 3

<!-- b000369 | prose | pages [18] -->
(18.23, −66.76) 3 Arecibo B 3720 MED 1

<!-- b000370 | heading | pages [18] -->
5.3.2 Delivery Routes and Schedule

<!-- b000371 | prose | pages [18] -->
Notice that the delivery route in the three-dimensional space is not actually straight because of the rugged terrain in reality. Since the maximum ﬂight height is around 120 meters, far below the height of the mountains that the drones will come across in its journeys.[8] We assume drones are ﬂying close to the ground. Thus, we applied Dijk- stra algorithm to derive the minimum distance as well as the drones’ optimal delivery route. The 3-dimensional routes are illustrated below.

<!-- b000372 | caption | pages [18] -->
Figure 9: The 3-dimensional delivery routes of the drones

<!-- b000373 | prose | pages [18] -->
Since the total time needed to deliver supplies is ﬁxed after the delivery routes are given by Dijkstra algorithm, the schedule is clear. We make the drones ﬂy along the above routes and replace their batteries and reload packages after each return. Then the drones can take off again and ﬂy to another destination.

<!-- b000374 | caption | pages [18] -->
Figure 10: The illustration of delivery schedule

<!-- b000375 | furniture | pages [19] -->
Team # 1923964

<!-- b000376 | furniture | pages [19] -->
Page 17 of 23

<!-- b000377 | heading | pages [19] -->
5.3.3 Payload Packing Conﬁgurations

<!-- b000378 | prose | pages [19] -->
As described before in Section 5.1.3, we pack all the medical packages required by a certain destination each day into a single parcel. Therefore, each drone’s payload packing conﬁguration is the corresponding parcel required by each city. The drone will ﬂy directly to the destination and return to the container.

<!-- b000379 | prose | pages [19] -->
With simple calculation by exhaustion, we know that this is the most time-saving way of package conﬁguration. If the medical packages required by a destination is delivered by two or more drones for multiple times, total delivery time will increase.

<!-- b000380 | heading | pages [19] -->
5.3.4 Flight Plan to Access Major Roads

<!-- b000381 | prose | pages [19] -->
With the highest speed, longest ﬂying range and relatively small size, drone B will be used in video reconnaissance.

<!-- b000382 | prose | pages [19] -->
Given the best locations, the settlements and segments of roads within the drones’ coverage area are deﬁnite, as the bold lines shown in ﬁgure below. Thus, we need to work out a ﬂight plan aiming to inspect the segments of major roads.

<!-- b000383 | prose | pages [19] -->
18.5 Quebradillas Quebradillas Quebradillas Quebradillas Arecibo Arecibo Arecibo Arecibo Barceloneta Barceloneta Barceloneta Barceloneta Dorado Dorado Dorado Dorado Manati Manati Manati Manati Aguadilla Aguadilla Aguadilla Aguadilla San Juan San Juan San Juan San Juan Unnamed 6 Unnamed 6 Unnamed 6 Unnamed 6 18.4 Bayamon Bayamon Bayamon Bayamon Rio Grande Rio Grande Rio Grande Rio Grande Centrol Puntas Centrol Puntas Centrol Puntas Centrol Puntas Corozal Corozal Corozal Corozal San Sebastian San Sebastian San Sebastian San Sebastian Fajardo Fajardo Fajardo Fajardo Utuado' 18.3 Utuado Lares Aguas Buenas Aguas Buenas Aguas Buenas Aguas Buenas Jayuya Jayuya Jayuya Caguas Caguas Caguas Caguas Comerio Comerio Comerio Comerio Juncos Juncos Juncos Juncos Orocovis Orocovis Orocovis Orocovis Naguabo Naguabo Naguabo Naguabo San Lorenzo San Lorenzo San Lorenzo San Lorenzo Canstaner 18.2 Mayaguez Mayaguez Mayaguez Mayaguez Unnamed 4 Unnamed 4 Unnamed 4 Unnamed 4 Unnamed 3 Unnamed 3 Unnamed 3 Unnamed 3 Adjuntas Adjuntas Adjuntas Adjuntas Unnamed 1 Unnamed 1 Unnamed 1 Unnamed 1 Indiera Alta Indiera Alta Indiera Alta Indiera Alta Humacao Humacao Humacao Humacao Unnamed 5 Unnamed 5 Unnamed 5 Unnamed 5 Cayey Cayey Cayey Cayey 18.1 Unnamed 2 San German San German San German San German Coamo Coamo Coamo Coamo Yauco Yauco Yauco Yauco Ponce Ponce Ponce Ponce Maunabo Maunabo Maunabo Maunabo 18 Cabo Rojo Cabo Rojo Cabo Rojo Cabo Rojo Guayama Guayama Guayama Guayama Ensenada Ensenada Ensenada Ensenada Santa Isabel Santa Isabel Santa Isabel Santa Isabel Punta Figuras Punta Figuras Punta Figuras Punta Figuras

<!-- b000384 | prose | pages [19] -->
17.9 -67.2 -67 -66.8 -66.6 -66.4 -66.2 -66 -65.8 -65.6

<!-- b000385 | caption | pages [19] -->
Figure 11: The segments of major roads within each coverage area

<!-- b000386 | prose | pages [19] -->
An accessing mission consists of three successive phases: setting off to the target segment, inspecting along the segment and returning to container before running out of power. Due to the urgency of rescuing work, it must be better for the drones to provide feedback of information as soon as possible. Thus, in order to reduce the waste of time on the ﬁrst and third phases, the drones should begin accessing from those segments close to the centre to those far away. Adopting the distance between the centre and the segments’ midpoint as a criterion, we rank the segments of roads from small to large by distance. The ﬂight plans are listed below. Segments of roads are expressed by the two settlements they connect. The arrows indicate the accessing sequence.

<!-- b000387 | prose | pages [19] -->
Container 1 Rio Grande-Fajardo →San Juan-Rio Grande →Naguabo-Juncos →Humacao- Fajardo →Caguas-Juncos →Humacao-San Lorenzo →San Juan-Caguas → Caguas-San Lorenzo

<!-- b000388 | prose | pages [19, 20] -->
Container 2 Aguas Buenas-Unnamed 4 →Bayamon Aguas-Buenas →Aguas Buenas- Caguas →Comerio-Bayamon →San Juan-Aguas Buenas →Comerio-Unnamed 4 →San Juan-Caguas →Caguas-Cayey →Bayamon-San Juan →Unnamed 4- Cayey →Caguas-Juncos →Caguas-San Lorenzo →Bayamon-Unnamed 6 → Unnamed 2-Cayey →Corozal-Unnamed 6

<!-- b000389 | furniture | pages [20] -->
Team # 1923964

<!-- b000390 | furniture | pages [20] -->
Page 18 of 23

<!-- b000392 | prose | pages [20] -->
Container 3 Utuado-Adjuntas →Lares-Utuado →Canstaner-Adjuntas →Lares-Canstaner →Utuado-Utuado’ →Indiera Alta-Canstaner →Arecibo-Utuado →Utuado’- Jayuya →Lares-Arecibo →Yauco-Indiera Alta

<!-- b000393 | heading | pages [20] -->
6 Applying of Models

<!-- b000394 | prose | pages [20] -->
Notice that the response system is developed for potential crisis, especially a larger- scale one, in the future. We test our models by altering the case as Haiti whose popu- lation and area are about three times larger than Puerto Rcio. In 2010, Haiti suffered a earthquake and witnessed the participation of drones in the rescuing work.[12]

<!-- b000395 | caption | pages [20] -->
Figure 12: Haiti’s comparison between the importance illustration and best locations

<!-- b000396 | prose | pages [20] -->
As shown above, we abstract the map of Haiti. Applying the same importance eval- uation criteria and the optimization function, we identify the best three locations. The service regions of the containers cover the most population-dense districts including Haiti’s top 5 signiﬁcant cities.

<!-- b000397 | prose | pages [20] -->
The successful application of Haiti demonstrates our models’ practicability and universality.

<!-- b000398 | heading | pages [20] -->
7 Sensitivity Analysis

<!-- b000399 | heading | pages [20] -->
7.1 Importance Level of Settlements

<!-- b000400 | prose | pages [20] -->
Since the values assigned to different settlements in Section 5.2.1 are subjective, we check up whether the variations of importance level affect the result remarkably. Two major possible defects are the arbitrariness of assigning settlements importance and the underestimation of some settlements.

<!-- b000401 | furniture | pages [21] -->
Team # 1923964

<!-- b000402 | furniture | pages [21] -->
Page 19 of 23

<!-- b000403 | heading | pages [21] -->
7.1.1 Assigning Methods of Importance

<!-- b000404 | prose | pages [21] -->
Different from linear methods in Section 5.2.1, we set the values of different settle- ments’ importance as 1, 2, 4, 8, 16, 32, which is an exponential sequence.

<!-- b000405 | prose | pages [21] -->
Destination Arecibo Fajardo & San Juan Caguas & Bayamon (18.31, −66.83) (18.32, −65.88) (18.38, −66.17) Linear (18.34, −66.55) (18.32, −65.88) (18.38, −66.17) Exponential

<!-- b000406 | prose | pages [21] -->
As shown in the table, different methods of assigning importance have a little im- pact on the best locations. Instinctively, we may make a bold prediction of robustness with respect to assigning methods so long as they satisfy the order preservation of the settlements.

<!-- b000407 | heading | pages [21] -->
7.1.2 Underestimation of Some Settlements’ Importance

<!-- b000408 | prose | pages [21] -->
Underestimation of some places’ importance is common. For example on Puerto Rico, Mayaguez on the western coast may possess abundant historical cultural relics and remains that deserve timely rescue and Loiza Aldea on the northeast coast may be an important harbour that allows supplies being transported into the island. Therefore, it would be well to change their values of importance from 4 to 5 and from 3 to 5 respectively. Our models give the result as follows.

<!-- b000409 | prose | pages [21] -->
Destination Arecibo Fajardo & San Juan Caguas & Bayamon (18.31, −66.83) (18.32, −65.88) (18.38, −66.17) Original (18.27, −66.71) (18.32, −65.65) (18.23, −66.03) Modiﬁed

<!-- b000410 | prose | pages [21] -->
As shown above, the individual changes of importance bring about an actual im- pact on the best locations. It is worth pointing out that the inﬂuence of individual changes can spread far away through the connective matrix X. In general, t he mod- erate changes of locations are still acceptable.

<!-- b000411 | heading | pages [21] -->
7.2 Drones’ Maximum Navigation Radius

<!-- b000412 | prose | pages [21] -->
Varying the maximum navigation radius, we check up the corresponding changes in best locations. Under the restriction of delivering supplies for up to 3 containers, the largest maximum navigation radius r among all kinds of drones should be no less than 22km. Thus, we set r as 23, 26 and 40km.

<!-- b000413 | furniture | pages [22] -->
Team # 1923964

<!-- b000414 | furniture | pages [22] -->
Page 20 of 23

<!-- b000415 | caption | pages [22] -->
Figure 13: Comparison of global optimization results

<!-- b000416 | prose | pages [22] -->
Apart from the density map of global optimization results, we identify the best 3 locations under different radii, as shown below.

<!-- b000417 | prose | pages [22] -->
Radius 23 km 26 km 40 km Destination (18.33,−66.79) (18.31, −66.83) (18.25 −66.58) Arecibo (18.34, −65.85) (18.32, −65.88) (18.32, −66.00) Fajardo & San Juan (18.38, −66.17) (18.38, −66.17) (18.38, −66.17) Caguas & Bayamon

<!-- b000418 | prose | pages [22] -->
The comparison indicates that the variation of different extent of radius make re- markably different inﬂuence on the best locations. The changes can be explained by the length distribution of segments (see in Appendix). Since the settlements are dis- cretely located, there exist a minimum distance among them. Tiny changes of radius can hardly include new settlements and therefore, they lead to little changes of the coverage’s contents. Hence, only large variations can contribute to signiﬁcant changes of locations.

<!-- b000419 | heading | pages [22] -->
8 Strengths and Weaknesses

<!-- b000420 | heading | pages [22] -->
8.1 Strengths

<!-- b000421 | prose | pages [22] -->
• Taking topographic factors into account, models are adaptable to regions of var- ious terrains but not limit to Puerto Rico.

<!-- b000422 | prose | pages [22] -->
• Models are close to reality, such as safety concern of maximum ﬂying time with full cargo and simulation of cameras’ scanning pattern.

<!-- b000423 | prose | pages [22] -->
• Reasonable and easy-to-practice evaluation of importance level instructs the re- connaissance effectively.

<!-- b000424 | prose | pages [22] -->
• Robustness and practicability are demonstrated by sensitivity analysis.

<!-- b000425 | furniture | pages [23] -->
Team # 1923964

<!-- b000426 | furniture | pages [23] -->
Page 21 of 23

<!-- b000427 | heading | pages [23] -->
8.2 Weaknesses

<!-- b000428 | prose | pages [23] -->
• The time complexity of the delivering model obeys exponential pattern and brings about difﬁculties of solving a large-scale problem.

<!-- b000429 | prose | pages [23] -->
Due to the complexity of the problem, we can hardly derive a systematic programme to solve it.

<!-- b000430 | prose | pages [23] -->
• The importance levels assigned to the settlements are subjective and lack detailed considerations.

<!-- b000431 | prose | pages [23] -->
• The inﬂuence of weather condition is ignored.

<!-- b000432 | prose | pages [23] -->
The possibility of encountering extreme weather shortly after a disaster should be consid- ered. But for conciseness of modeling and feasibility of calculations, we have to abandon the consideration pitifully.

<!-- b000433 | heading | pages [23] -->
9 Future Work

<!-- b000434 | prose | pages [23] -->
As mentioned in weaknesses in Section 9.2, the weather condition is not taken into account. Actually, there are more factors that deserve inclusion in our models.

<!-- b000435 | prose | pages [23] -->
The most remarkable factor is the extent to which an area is suffering the disaster. The more severe the circumstances are, the more urgently it demands rescue. The factor can be quantitated by a series of measurements. For example, measurements include the distances away from the epicenter in an earthquake and the minimum distances away from the trajectory in a hurricane.

<!-- b000436 | prose | pages [23] -->
In addition, the feedback of the reconnaissance can instruct further missions in- cluding materials supplied by trucks. The ground transportation is obviously more economical.

<!-- b000437 | prose | pages [23] -->
However, due to the limited time information available for the problem, we cannot reﬁne our models adequately.

<!-- b000438 | heading | pages [23] -->
10 Conclusions

<!-- b000439 | prose | pages [23] -->
From a top-down perspective, we separate the complicated problem into two rela- tively simpliﬁed missions and establish a model for them respectively.

<!-- b000440 | prose | pages [23] -->
For the overall design, we emphasize the reality by considering three practicable factors. For the design of two individual models, we emphasize the practicability by sorting out the feasible groups of destinations, introducing segments and importance evaluation function.

<!-- b000441 | prose | pages [23] -->
We combine the two models naturally and derive a comprehensive solution in- cluding the ﬂeets’ composition, each drone’s payload conﬁgurations, delivery route, schedule and ﬂight plan as well as the containers’ best locations and packing conﬁgu- rations.

<!-- b000442 | furniture | pages [24] -->
Team # 1923964

<!-- b000443 | furniture | pages [24] -->
Page 22 of 23

<!-- b000444 | heading | pages [24] -->
11 Appendix

<!-- b000445 | prose | pages [24] -->
Flight time versus payload

<!-- b000446 | caption | pages [24] -->
Figure 14: Relationship between ﬂight time and the drone’s payload [4]

<!-- b000447 | prose | pages [24] -->
Distribution of segments’ length

<!-- b000448 | caption | pages [24] -->
Figure 15: The frequency map of segments’ length

<!-- b000449 | furniture | pages [25] -->
Team # 1923964

<!-- b000450 | furniture | pages [25] -->
Page 23 of 23

<!-- b000451 | heading | pages [25] -->
References

<!-- b000452 | references | pages [25] -->
[1] Outstanding Drone: Top 10 Drones for Search and Rescue Operations. (2019)

<!-- b000453 | references | pages [25] -->
2018.11.8.

<!-- b000454 | references | pages [25] -->
https://www.outstandingdrone.com/search-rescue-drones/

<!-- b000455 | references | pages [25] -->
#1FlyByCopters_X8_640_Quadcopter_Drone.

<!-- b000456 | references | pages [25] -->
https://baike.baidu.com/

<!-- b000457 | references | pages [25] -->
[2] BaiduBaike: control radius.

<!-- b000458 | references | pages [25] -->
2018.12.05

<!-- b000459 | references | pages [25] -->
item/%E6%8E%A7%E5%88%B6%E5%8D%8A%E5%BE%84/23192207?fr=aladdin

<!-- b000460 | references | pages [25] -->
http://haiba.qhdi.com/

<!-- b000461 | references | pages [25] -->
[3] Google Maps: Puerto Rico

<!-- b000462 | references | pages [25] -->
https://freeflysystems.zendesk.com/hc/en-us/

<!-- b000463 | references | pages [25] -->
[4] Freeﬂy Systems

<!-- b000464 | references | pages [25] -->
signin?return_to=https%3A%2F%2Ffreeflysystems.zendesk.com

<!-- b000465 | references | pages [25] -->
%2Fhc%2Fen-us%2Farticles%2F204720589-What-is-the-max-flight

<!-- b000466 | references | pages [25] -->
-time-on-the-ALTA-6

<!-- b000467 | references | pages [25] -->
[5] Vann R. Newkirk II: Can Puerto Rico Recover From Maria Before the Next Storm

<!-- b000468 | references | pages [25] -->
2018.04.26. https://www.theatlantic.

<!-- b000469 | references | pages [25] -->
Hits? The Atlantic Monthly. Politics

<!-- b000470 | references | pages [25] -->
com/politics/archive/2018/04/puerto-ricos-next-public-health-

<!-- b000471 | references | pages [25] -->
challenges/558896/

<!-- b000472 | references | pages [25] -->
[6] PBS News Hour:

<!-- b000473 | references | pages [25] -->
Puerto Ricos recovery, 7 months after Hurricane Maria.

<!-- b000474 | references | pages [25] -->
https://www.pbs.org/newshour/nation/puerto-ricos-

<!-- b000475 | references | pages [25] -->
2018.04.19.

<!-- b000476 | references | pages [25] -->
recovery-7-months-after-hurricane-maria

<!-- b000477 | references | pages [25] -->
https://zh.wikipedia.org/wiki/

<!-- b000478 | references | pages [25] -->
[7] Wikipedia: Tropical Forest.

<!-- b000479 | references | pages [25] -->
2018.11.16.

<!-- b000480 | references | pages [25] -->
%E7%83%AD%E5%B8%A6%E9%9B%A8%E6%9E%97

<!-- b000481 | references | pages [25] -->
https://www.

<!-- b000482 | references | pages [25] -->
[8] The Drone Logic: How High Drones Can Fly?

<!-- b000483 | references | pages [25] -->
2018.03.28.

<!-- b000484 | references | pages [25] -->
thedronelogic.com/how-drones-work/drone-flight-time/

<!-- b000485 | references | pages [25] -->
https://pro.dji.com/

<!-- b000486 | references | pages [25] -->
[9] DJI: Professional Product. Glimbal Cameras.(2019)

<!-- b000487 | references | pages [25] -->
?site=brandsite&from=nav

<!-- b000488 | references | pages [25] -->
[10] National Instruments: Calculating Camera Sensor Resolution and Lens Focal

<!-- b000489 | references | pages [25] -->
Length. (2019) 2018.02.15. http://www.ni.com/product-documentation

<!-- b000490 | references | pages [25] -->
/54616/en/

<!-- b000491 | references | pages [25] -->
[11] Federal Aviation Administration. Unmanned Aircraft Systems. 2018.12.20.

<!-- b000492 | references | pages [25] -->
https://www.faa.gov/uas/

<!-- b000493 | references | pages [25] -->
[12] The Guardian:

<!-- b000494 | references | pages [25] -->
Flying aid drones tested in Haiti and Dominican Republic.

<!-- b000495 | references | pages [25] -->
https://www.theguardian.com/global-development/

<!-- b000496 | references | pages [25] -->
2013.01.09.

<!-- b000497 | references | pages [25] -->
2013/jan/09/flying-aid-drones-haiti-dominican-republic

<!-- b000498 | references | pages [25] -->
[13] DJI: Inspire 2. (2019) https://www.dji.com/cn/inspire-2/specs
