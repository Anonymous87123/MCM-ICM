# P-B-2019-1924588-bd69a632

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team # 1924588

<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->
Team Control Number

<!-- b000006 | prose | pages [1] -->
For office use only

<!-- b000007 | prose | pages [1] -->
For office use only

<!-- b000008 | title | pages [1] -->
1924588

<!-- b000009 | prose | pages [1] -->
T1

<!-- b000010 | prose | pages [1] -->
T2

<!-- b000011 | prose | pages [1] -->
T3

<!-- b000012 | prose | pages [1] -->
F1

<!-- b000013 | prose | pages [1] -->
F2

<!-- b000014 | prose | pages [1] -->
F3 Problem Chosen

<!-- b000015 | prose | pages [1] -->
T4 B F4

<!-- b000016 | prose | pages [1] -->
2019 MCM/ICM Summary Sheet Multi-Directional Comprehensive Disaster Response

<!-- b000017 | prose | pages [1] -->
System Based on Optimization

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | prose | pages [1] -->
According to the actual situation of Puerto Rico, we designed a disaster response system from the perspective of disaster area demand, company cost, realizability and security.

<!-- b000021 | prose | pages [1] -->
First, we identified the number and type of UAVs(unmanned aerial vehicle) in the UAV

<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | prose | pages [1] -->
fleet based on the geographical location and needs of Puerto Rican hospitals. Minimum UAVs are used to save costs. Solving this optimization problem, we get two schemes: scheme one needs four UAVs (B, C, D and H), the number of which is 1B, 1C, 1D and 3H; scheme two needs four UAVs (B, C, G and H), the number of which is 2B, 1C, 1G and 3H. Each scheme needs three containers.

<!-- b000024 | prose | pages [1] -->
Second, we designed the packaging configuration for containers. The number of medical

<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | prose | pages [1] -->
packages is large, so the heuristic algorithm is not effective. We propose a one-dimensional maximum utilization packing scheme of “medical package first, UAV later”. It can not only realize the greater use of container space, but also be easy to achieve when loading containers. The maximum space utilization rate is 93.22% and the minimum utilization rate is 68.14%.

<!-- b000027 | prose | pages [1] -->
Third, we gridded the main roads in Puerto Rico's main disaster areas and transformed

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | prose | pages [1] -->
the continuous problems into discrete ones. We identified the optimal location of the disaster response system by using grid search method. The three containers’ locations are as follows:

<!-- b000030 | prose | pages [1] -->
W , 18.34 ( 18.47 N , 66.

<!-- b000031 | prose | pages [1] -->
55 W , 18.34 ) ( N , 66.

<!-- b000032 | prose | pages [1] -->
03 ) ( N , 65.

<!-- b000033 | prose | pages [1] -->
69 W . )

<!-- b000034 | prose | pages [1] -->
Fourth, the payload packaging configuration of UAV is designed by using optimization

<!-- b000035 | furniture | pages [1] -->


<!-- b000036 | prose | pages [1] -->
methods. Drone B load 2MED1,drone C load 1MED1+1MED3, drone D load 4MED1+2MED3 or 3MED1+3MED2 or 2 MED1+1MED2+2MED3. UAV flight delivery routes need to avoid mountain and high buildings, so we use Voronio Diagram and Dijkstra algorithm to get delivery route. The flight schedule of UAV is obtained according to the delivery route.

<!-- b000037 | prose | pages [1] -->
Fifth, in order to make the UAV reconnaissance the road as wide as possible, flight

<!-- b000038 | furniture | pages [1] -->


<!-- b000039 | prose | pages [1] -->
schedule of the UAV are obtained by using ant colony optimization (ACO). It can use the limited flight time to reconnoitre the road as much as possible.

<!-- b000040 | prose | pages [1] -->
To sum up, we considered many factors to design DroneGo system.

<!-- b000041 | furniture | pages [1] -->


<!-- b000042 | keywords | pages [1] -->
Keywords: Optimization; ACO; Gridding; Voronio; Dijkstra

<!-- b000043 | furniture | pages [2] -->


<!-- b000044 | furniture | pages [2] -->
Team # 1924588

<!-- b000045 | heading | pages [2] -->
Contents

<!-- b000046 | furniture | pages [2] -->


<!-- b000047 | contents | pages [2] -->
1  Introduction ..................................................................................................................................................... 1

<!-- b000048 | contents | pages [2] -->
1.1 Problem Background........................................................................................................................... 1

<!-- b000049 | contents | pages [2] -->
1.2 Restatement of the Problem .............................................................................................................. 1

<!-- b000050 | contents | pages [2] -->
1.3 Literature Review ................................................................................................................................. 2

<!-- b000051 | contents | pages [2] -->
2  Assumptions and Justifications ................................................................................................................ 2

<!-- b000052 | contents | pages [2] -->
3  Notations .......................................................................................................................................................... 3

<!-- b000053 | contents | pages [2] -->
4  Model Establishment .................................................................................................................................... 3

<!-- b000054 | contents | pages [2] -->
4.1 Identify Drones and Medical Packages ........................................................................................ 4

<!-- b000055 | contents | pages [2] -->
4.1.1 Determining the Number of Unmanned Aerial Vehicles.......................................... 4

<!-- b000056 | contents | pages [2] -->
4.1.2 Selection of Unmanned Aerial Vehicle Types ............................................................... 5

<!-- b000057 | contents | pages [2] -->
4.1.3 Selection of Container Number and Cargo Loading Scheme.................................. 5

<!-- b000058 | contents | pages [2] -->
4.2 ISO Cargo Containers Packing Configuration ........................................................................... 6

<!-- b000059 | contents | pages [2] -->
4.3 Optimization model of the best container location ............................................................... 11

<!-- b000060 | contents | pages [2] -->
4.3.1 Road Grid Model.................................................................................................................... 11

<!-- b000061 | contents | pages [2] -->
4.3.2 Mapping Hospital Location to Grid Model ................................................................. 12

<!-- b000062 | contents | pages [2] -->
4.3.3. Establishment of Optimization Model .......................................................................... 12

<!-- b000063 | contents | pages [2] -->
4.3.4 Result .......................................................................................................................................... 13

<!-- b000064 | contents | pages [2] -->
4.4 Drone Payload Packaging Configuration .................................................................................. 14

<!-- b000065 | contents | pages [2] -->
4.5 UAV Delivery Route and Timetable ............................................................................................ 14

<!-- b000066 | contents | pages [2] -->
4.5.1 Delivery Route Division ...................................................................................................... 15

<!-- b000067 | contents | pages [2] -->
4.5.2 Delivery Route Planning Model ....................................................................................... 15

<!-- b000068 | contents | pages [2] -->
4.5.3 Delivery Route Solution ...................................................................................................... 16

<!-- b000069 | contents | pages [2] -->
4.5.4 Delivery schedule................................................................................................................... 17

<!-- b000070 | contents | pages [2] -->
4.6 Drone Flight Plan ................................................................................................................................ 17

<!-- b000071 | contents | pages [2] -->
4.6.1 Model establishment ............................................................................................................. 17

<!-- b000072 | contents | pages [2] -->
4.6.2 Using Ant Colony Optimization (ACO) to Solve the Problem ............................. 18

<!-- b000073 | contents | pages [2] -->
4.6.3 Result .......................................................................................................................................... 19

<!-- b000074 | contents | pages [2] -->
5  Testing Our Model ...................................................................................................................................... 20

<!-- b000075 | contents | pages [2] -->
6  Evaluation of Our Model .......................................................................................................................... 20

<!-- b000076 | contents | pages [2] -->
References.............................................................................................................................................................. 22

<!-- b000077 | furniture | pages [3] -->


<!-- b000078 | furniture | pages [3] -->
Team # 1924588

<!-- b000079 | contents | pages [3] -->
Appendix ............................................................................................................................................................... 23

<!-- b000080 | furniture | pages [3] -->


<!-- b000081 | furniture | pages [3] -->


<!-- b000082 | furniture | pages [4] -->
Team # 1924588

<!-- b000083 | heading | pages [4] -->
MEMO

<!-- b000084 | furniture | pages [4] -->


<!-- b000085 | prose | pages [4] -->
From: Team 1924588, MCM 2019

<!-- b000086 | furniture | pages [4] -->


<!-- b000087 | prose | pages [4] -->
To: The Chief Operating Officer (CEO) of HELP, Inc. Date: January 28, 2019 Subject: Findings and recommendations for DroneGo disaster response system

<!-- b000088 | furniture | pages [4] -->


<!-- b000089 | prose | pages [4] -->
Dear CEO, we are honored to inform you our achievements and recommendations for you.

<!-- b000090 | prose | pages [4] -->
After a careful study of DroneGo system and the devastation in Puerto Rico, we get the following

<!-- b000091 | furniture | pages [4] -->


<!-- b000092 | prose | pages [4] -->
results. First of all, from the perspective of cost saving for HELP, Inc., we believe that drones used for disaster relief should not be disposable, but should be equipped with replaceable batteries during transportation or realize the reuse of drones by means of designing solar energy charging on the drone or something. On this premise, we figured out that the DroneGo system only needs six drones to achieve the disaster relief mission. Three drones are used for medical supply delivery and video reconnaissance, the other drones,which are named tethered drone, are uesd to provide wireless networks and transmit the data. As for the cargo containers' quantity, we think that three cargo containers can transport more medical packages so that the hospitals in Puerto Rico can last a longer time. And then, we designed a packaging scheme for cargo containers to keep as many medical packages as possible. Please refer to the text for the specific package plan. We have found the three best locations for cargo containers, respectively at 18.47 W , 18.34 W and ( N , 66.

<!-- b000093 | prose | pages [4] -->
55 ) ( N , 66.

<!-- b000094 | prose | pages [4] -->
03 )

<!-- b000095 | prose | pages [4] -->
W . Next, we took the obstacles such as mountains and buildings into consideration, ( 18.34 N , 65.

<!-- b000096 | prose | pages [4] -->
69 ) and designed a bunch of safe and efficient delivery routes for drones. At the same time, the delivery schedule are formulated for each of the drone. Finally, in order to enable the drone to reconnoitre the main roads as much as possible, we used ant colony optimization（ACO） algorithm to get the best reconnaissance routes of each drone, and work out the time plan of drone based on the combination of medical supply delivery and video reconnaissance.

<!-- b000097 | prose | pages [4] -->
Through our model analysis, we can draw the conclusion that a small number of drones can

<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | prose | pages [4] -->
complete the medical supply delivery mission. However, if we want to achieve a wider range of road reconnaissance in disaster areas, we need to increase the number of drones invested.

<!-- b000100 | prose | pages [4] -->
Based on the results and conclusions above, we put forward the following suggestions for you: ⚫ Replaceable batteries or solar recharging devices should be designed to reuse the drones.

<!-- b000101 | prose | pages [4] -->
⚫ Select the three best locations of W , W  , ( ( 18.47 N , 66.

<!-- b000102 | prose | pages [4] -->
55 ) ( 18.34 N , 66.

<!-- b000103 | prose | pages [4] -->
03 ) W ,which can not only reduce the number of drones used, but also make the ( 18.34 N , 65.

<!-- b000104 | prose | pages [4] -->
69 ) reconnaissance range as large as possible. ⚫ When planning the route of drones, then influence of obstacles should be considered carefully to

<!-- b000105 | prose | pages [4] -->
complete the missions of medical supply delivery and video reconnaissance safely and successfully. ⚫ If you think that all the main roads must be reconnoitred, you can achieve this goal by using more

<!-- b000106 | prose | pages [4] -->
drones. We sincerely hope that DroneGo disaster response system will be carried out perfectly. Please contact us if you have any problems.

<!-- b000107 | furniture | pages [4] -->


<!-- b000108 | furniture | pages [5] -->


<!-- b000109 | furniture | pages [5] -->
Team # 1924588                                                                  Page 1 of 29

<!-- b000110 | heading | pages [5] -->
1  Introduction

<!-- b000111 | heading | pages [5] -->
1.1 Problem Background

<!-- b000112 | prose | pages [5] -->
The U.S. territory of Puerto Rico was hit by a severe hurricane in 2017 that caused significant damage. The combined destructive power of the hurricane's storm surge and wave action caused extensive damage to buildings and roads, particularly along the east and southeast coast of Puerto Rico. The storm left 3.4 million people on the island without power. The storm destroyed the majority of the island's cellular communication networks. The electrical power and the cell service outages lasted for up across indicates much of the island. Widespread flooding blocked and damaged many highways and roads across the island, making it nearly impossible for emergency services ground vehicles to plan and navigate their routes. Demand for medical services has continued to surge for some time as people with chronic diseases have turned to hospitals and temporary shelters for treatment.

<!-- b000113 | heading | pages [5] -->
1.2 Restatement of the Problem

<!-- b000114 | furniture | pages [5] -->


<!-- b000115 | prose | pages [5] -->
Non-governmental organizations (NGOs) usually provide adequate and timely response to natural disasters. We need to design a transportable disaster response system called "DroneGo." for HELP, Inc. to improve its response capabilities. We also need to select some of the candidate drones to make up DroneGo fleet for medical supply and video reconnaissance. In addition, we also need to put drones and medical packages into ISO containers with reasonable design and deploy them to the affected areas. The simple structure of the DroneGo disaster response system is shown in figure 1:

<!-- b000116 | furniture | pages [5] -->


<!-- b000117 | caption | pages [5] -->
Figure 1 DroneGo disaster response system

<!-- b000118 | prose | pages [5] -->
In order to solve those problems, we will proceed as follows:

<!-- b000119 | furniture | pages [6] -->


<!-- b000120 | furniture | pages [6] -->
Team # 1924588                                                                  Page 2 of 29

<!-- b000121 | prose | pages [6] -->
⚫ Recommend a drone fleet and set of medical packages for the HELP, Inc.

<!-- b000122 | prose | pages [6] -->
DroneGo disaster response system.

<!-- b000123 | prose | pages [6] -->
⚫ Design packaging configurations for ISO cargo containers to transport the

<!-- b000124 | prose | pages [6] -->
system to disaster areas.

<!-- b000125 | prose | pages [6] -->
⚫ Identify the best location to deploy the disaster response system's ISO cargo

<!-- b000126 | prose | pages [6] -->
containers.

<!-- b000127 | prose | pages [6] -->
⚫ Provide payload packaging configurations for medical packages packed in the

<!-- b000128 | prose | pages [6] -->
drone's cargo bay.

<!-- b000129 | prose | pages [6] -->
⚫ Establish the delivery routes for drones and give a schedule for the delivery of

<!-- b000130 | prose | pages [6] -->
the medical package by the drones.

<!-- b000131 | prose | pages [6] -->
⚫ Provides flight plans for unmanned aerial vehicles to conduct video

<!-- b000132 | prose | pages [6] -->
reconnaissance.

<!-- b000133 | heading | pages [6] -->
1.3 Literature Review

<!-- b000134 | prose | pages [6] -->
Part of the problem involves packing problem. Packing problem is a traditional optimal combination problem, which has been studied a lot. The solution of three-dimensional packing problem is usually divided into two parts: heuristic placement method and search algorithm for better solution. S Martello proposed an accurate branch and bound algorithm

<!-- b000135 | heading | pages [6] -->
and combined the original approximation algorithm[1]. E Falkenauer shows how the bin

<!-- b000136 | prose | pages [6] -->
packing GGA can be enhanced with a local optimization inspired by the dominance criterion[2]. JO Berkey and PY Wang developed new bin-packing heuristics by adapting the bottom-left packing method and the next-fit, first-fit and best-fit level-oriented packing heuristics to the finite-bin case[3]. Kyungdaw Kang put forward a hybrid genetic algorithm with a new packing strategy for the three-dimensional bin packing problem[4].And so on.

<!-- b000137 | heading | pages [6] -->
2  Assumptions and Justifications

<!-- b000138 | prose | pages [6] -->
⚫ Considering the high cost of drones, the disaster response system is designed with fewer

<!-- b000139 | prose | pages [6] -->
drones, which enables ISO cargo containers to deliver more medical packages. ⚫ We don't think the drones are disposable. Drones are supposed to contain replaceable

<!-- b000140 | prose | pages [6] -->
batteries when they arrive in disaster areas, so they can be reused. In addition, a certain time should be set aside between the two operations of the UAV to change the battery, and it is not allowed to work at night. We assume that this time needs about 3 to 4 hours, so the UAV can work up to three times a day. ⚫ As for the H-type UAV, we cannot use it to transport medicine packages or detect

<!-- b000141 | prose | pages [6] -->
problems in the road network according to its characteristics. The H-type UAV[5][6] has the function of providing mobile network. Since much of Puerto Rico's mobile communications network has been destroyed, each container should be equipped with an H-type drone to provide Internet connectivity.

<!-- b000142 | furniture | pages [7] -->


<!-- b000143 | furniture | pages [7] -->
Team # 1924588                                                                  Page 3 of 29

<!-- b000144 | prose | pages [7] -->
⚫ When using container transport drones and medical packages, the transport time is long

<!-- b000145 | prose | pages [7] -->
and the quantity of goods is large and the weight is large. Therefore, we believe that medical packages can only be positively placed in containers, not upright or inverted. Of course, medical packages can be rotated horizontally to increase the space utilization of containers while they are being placed. When the medical package is transported by UAVs, the transportation time is shorter, the quantity of the goods is less and the weight is smaller, so we think that the medical package can be placed in Drone cargo bay in various ways. ⚫ Suppose that the longest flight time of UAV at full load is 2/3 of that at no load, and the

<!-- b000146 | prose | pages [7] -->
maximum speed remains unchanged. ⚫ Suppose UAVs take up one minute of flight time each as they go up and down. ⚫ The number of medical packages delivered by UAVs is an integral multiple of the daily

<!-- b000147 | prose | pages [7] -->
consumption of the target hospital.

<!-- b000148 | heading | pages [7] -->
3  Notations

<!-- b000149 | furniture | pages [7] -->


<!-- b000150 | prose | pages [7] -->
Here are the notations and their meanings in our paper:

<!-- b000151 | caption | pages [7] -->
Table 1 notation explanation

<!-- b000152 | prose | pages [7] -->
meanings Distance between hospital

<!-- b000153 | heading | pages [7] -->
Notation

<!-- b000154 | prose | pages [7] -->
S h ( , h ) h and hospital nh

<!-- b000155 | furniture | pages [7] -->


<!-- b000156 | prose | pages [7] -->
m n m m

<!-- b000157 | prose | pages [7] -->
Mp h The daily weight of medical required by hospital m m

<!-- b000158 | prose | pages [7] -->
D The maximum flight distance of drone i i

<!-- b000159 | prose | pages [7] -->
iZ The maximum load of drone i

<!-- b000160 | prose | pages [7] -->
iV The shipping container dimensions of drone i

<!-- b000161 | prose | pages [7] -->
Represents whether the grid is passed by the road TG

<!-- b000162 | prose | pages [7] -->
G Real distance represented by unit length in grid Coordinate System

<!-- b000163 | furniture | pages [7] -->


<!-- b000164 | prose | pages [7] -->
ave

<!-- b000165 | prose | pages [7] -->
kP The location of cargo container k in grid Coordinate System

<!-- b000166 | heading | pages [7] -->
4  Model Establishment

<!-- b000167 | prose | pages [7] -->
Before building the model, there are several issues that need to be addressed. First of all, in designing the number of UAVs and medical packages, designing delivery routes and other tasks, the most basic goal must be to enable UAVs to meet the daily needs of hospitals. Secondly, while meeting the needs, medical packages should be maintained for as long as possible to ensure that the five hospitals in the disaster area can rely on these packages to survive the months of the disaster. Third, considering the high cost of UAVs, we want to reduce the number of UAVs as much as possible, so that ISO cargo containers can have more space to load more medical packages.

<!-- b000168 | furniture | pages [8] -->


<!-- b000169 | furniture | pages [8] -->
Team # 1924588                                                                  Page 4 of 29

<!-- b000170 | prose | pages [8] -->
In short, we need to select as few UAVs as possible to meet the needs of each hospital. Use the selected UAV for maximum video reconnaissance in the affected area.

<!-- b000171 | heading | pages [8] -->
4.1 Identify Drones and Medical Packages

<!-- b000172 | prose | pages [8] -->
To recommend a drone fleet and medical package for HELP, Inc. should first understand the basic situation of Puerto Rico's disaster. Five hospitals' location is in attachment 4, the location is shown in Figure 2 .

<!-- b000173 | furniture | pages [8] -->


<!-- b000174 | caption | pages [8] -->
Figure 2 hospitals' location

<!-- b000175 | heading | pages [8] -->
4.1.1 Determining the Number of Unmanned Aerial Vehicles

<!-- b000176 | prose | pages [8] -->
According to the hospital location map and the full or no-load flight distance of UAV, we found that Hospital Pavia Arecibo is far away from other hospitals. As the distance between Hospital Pavia Arecibo and the nearest Puerto Rico Children's Hospital exceeds the maximum flight distance of any type of UAV, it is not possible to find an ISO cargo container placement point to deliver medical packages for Hospital Pavia Arecibo and other hospitals. Therefore, there must be an UAV and an ISO cargo container dedicated to this hospital. The other four hospitals except Hospital Pavia Arecibo are relatively close. Based on the idea of S h ( , h ) h and nh . The minimizing the number of UAVs. For two hospitals with distance , m n m

<!-- b000177 | prose | pages [8] -->
Mp and Mp . As long as any UAV can be weights of the medical packages they need are m n

<!-- b000178 | prose | pages [8] -->
D and payload found, its maximum flight distance i

<!-- b000179 | prose | pages [8] -->


<!-- b000180 | prose | pages [8] -->
S h

<!-- b000181 | prose | pages [8] -->
( m

<!-- b000182 | prose | pages [8] -->


<!-- b000183 | prose | pages [8] -->
Mp

<!-- b000184 | prose | pages [8] -->


<!-- b000185 | furniture | pages [8] -->


<!-- b000186 | prose | pages [8] -->
m

<!-- b000187 | prose | pages [8] -->


<!-- b000188 | prose | pages [8] -->
Mp

<!-- b000189 | prose | pages [8] -->


<!-- b000190 | prose | pages [8] -->
n

<!-- b000191 | prose | pages [8] -->
iZ meet the requirements：

<!-- b000192 | prose | pages [8] -->


<!-- b000193 | prose | pages [8] -->
, ,

<!-- b000194 | prose | pages [8] -->
h h

<!-- b000195 | prose | pages [8] -->
)

<!-- b000196 | prose | pages [8] -->
D

<!-- b000197 | prose | pages [8] -->
n n i

<!-- b000198 | prose | pages [8] -->
 

<!-- b000199 | prose | pages [8] -->
Z

<!-- b000200 | furniture | pages [8] -->


<!-- b000201 | prose | pages [8] -->
(1)

<!-- b000202 | prose | pages [8] -->
i

<!-- b000203 | prose | pages [8] -->
 

<!-- b000204 | prose | pages [8] -->
Z

<!-- b000205 | prose | pages [8] -->
i

<!-- b000206 | prose | pages [8] -->
It is possible to use the same UAV to distribute medicines to multiple hospitals. Finally, we get two possible UAV fleet schemes：

<!-- b000207 | furniture | pages [9] -->


<!-- b000208 | furniture | pages [9] -->
Team # 1924588                                                                  Page 5 of 29

<!-- b000209 | furniture | pages [9] -->


<!-- b000210 | caption | pages [9] -->
Figure 3 possible UAV fleet schemes

<!-- b000211 | prose | pages [9] -->
In solving the problem B later, we will decide which scheme to use according to the road investigation situation of the two schemes.

<!-- b000212 | heading | pages [9] -->
4.1.2 Selection of Unmanned Aerial Vehicle Types

<!-- b000213 | prose | pages [9] -->
For hospitals, UAVs serving them need to satisfy certain conditions and choose the most

<!-- b000214 | furniture | pages [9] -->


<!-- b000215 | prose | pages [9] -->
suitable UAV among them. This is a multi-objective programming problem. For UAVs serving only one hospital, the programming model is：

<!-- b000216 | prose | pages [9] -->
 +  + max V Z

<!-- b000217 | furniture | pages [9] -->


<!-- b000218 | prose | pages [9] -->
1 i 2 i   D s t Z . .

<!-- b000219 | prose | pages [9] -->
Mp

<!-- b000220 | furniture | pages [9] -->


<!-- b000221 | prose | pages [9] -->
(2) 3 i i n

<!-- b000222 | prose | pages [9] -->
For UAVs serving multiple hospitals, the programming model is：

<!-- b000223 | prose | pages [9] -->
 +  + 

<!-- b000224 | prose | pages [9] -->
max

<!-- b000225 | prose | pages [9] -->
V Z

<!-- b000226 | prose | pages [9] -->
1

<!-- b000227 | prose | pages [9] -->
i

<!-- b000228 | prose | pages [9] -->
2

<!-- b000229 | prose | pages [9] -->
i

<!-- b000230 | prose | pages [9] -->
 

<!-- b000231 | prose | pages [9] -->
Z Mp

<!-- b000232 | prose | pages [9] -->
i

<!-- b000233 | prose | pages [9] -->
1

<!-- b000234 | prose | pages [9] -->
 

<!-- b000235 | prose | pages [9] -->
Z Mp

<!-- b000236 | prose | pages [9] -->


<!-- b000237 | prose | pages [9] -->
i

<!-- b000238 | prose | pages [9] -->
2

<!-- b000239 | furniture | pages [9] -->


<!-- b000240 | prose | pages [9] -->
s t

<!-- b000241 | prose | pages [9] -->
. .

<!-- b000242 | prose | pages [9] -->
 

<!-- b000243 | prose | pages [9] -->
Z Mp

<!-- b000244 | prose | pages [9] -->


<!-- b000245 | prose | pages [9] -->
i k

<!-- b000246 | prose | pages [9] -->
 

<!-- b000247 | prose | pages [9] -->
D

<!-- b000248 | prose | pages [9] -->
3 3

<!-- b000249 | prose | pages [9] -->
i

<!-- b000250 | furniture | pages [9] -->


<!-- b000251 | prose | pages [9] -->
(3)

<!-- b000252 | prose | pages [9] -->
= 

<!-- b000253 | prose | pages [9] -->
D m n S h

<!-- b000254 | prose | pages [9] -->
( ,

<!-- b000255 | prose | pages [9] -->
h

<!-- b000256 | prose | pages [9] -->
)

<!-- b000257 | prose | pages [9] -->
m n i

<!-- b000258 | prose | pages [9] -->
, , , 1,2

<!-- b000259 | prose | pages [9] -->
k m

<!-- b000260 | prose | pages [9] -->
,

<!-- b000261 | prose | pages [9] -->
n

<!-- b000262 | prose | pages [9] -->
Ultimately, the results of our selection of UAV models are as follows:：

<!-- b000263 | prose | pages [9] -->
⚫ The first option: a C-type UAV, a D-type UAV, a B-type UAV and three H-type UAVs. ⚫ The second option：a C-type UAV, a D-type UAV, two B UAVs and three H UAVs are

<!-- b000264 | prose | pages [9] -->
required.

<!-- b000265 | heading | pages [9] -->
4.1.3 Selection of Container Number and Cargo Loading Scheme

<!-- b000266 | prose | pages [9] -->
We choose three ISO cargo containers to pack UAVs and medical packages for two reasons.：

<!-- b000267 | prose | pages [9] -->
⚫ From the map, we can see that the location of five hospitals is too scattered. By

<!-- b000268 | prose | pages [9] -->
analyzing the location of Caribbean Medical Center, Puerto Rico Children's Hospital

<!-- b000269 | furniture | pages [10] -->


<!-- b000270 | furniture | pages [10] -->
Team # 1924588                                                                  Page 6 of 29

<!-- b000271 | prose | pages [10] -->
and Hospital Pavia Arecibo, we can find that the distance between any two hospitals is greater than the maximum flight distance of UAV, so it is impossible to transport UAV and medical packages with two or less containers. ⚫ From the perspective of the disaster area, we need more containers to carry medical

<!-- b000272 | prose | pages [10] -->
packages so that the medical needs of the hospitals in the disaster area can be satisfied for a longer period of time. The three ISO cargo containers contain different cargo. The loading materials for each of

<!-- b000273 | furniture | pages [10] -->


<!-- b000274 | prose | pages [10] -->
the three containers of the two schemes are shown in table 2 and table 3.

<!-- b000275 | prose | pages [10] -->
Scheme 1：

<!-- b000276 | caption | pages [10] -->
Table 2 Scheme 1

<!-- b000277 | prose | pages [10] -->
ISO cargo container cargo container1 Type of Drone B Medical Package MED1 cargo container2 cargo container3 C D MED1, MED2, MED3 MED1, MED3 In this scenario, cargo container1 serves Hospital Pavia Arecibo. Cargo container2 serves Hospital Pavia Santurce, Puerto Rico Children's Hospital and Hospital HIMA. Cargo container3 serves Caribbean Medical Center.

<!-- b000278 | prose | pages [10] -->
Scheme 2：

<!-- b000279 | caption | pages [10] -->
Table 3 Scheme 2

<!-- b000280 | prose | pages [10] -->
ISO cargo container cargo container 1 Type of Drone B Medical Package MED1

<!-- b000281 | furniture | pages [10] -->


<!-- b000282 | prose | pages [10] -->
cargo container 2 cargo container3 G B and C MED1,MED2,MED3 MED1,MED3

<!-- b000283 | prose | pages [10] -->
In this scheme, cargo container1 serves Hospital Pavia Arecibo. Cargo container2 serves Hospital Pavia Santurce and Puerto Rico Children's Hospital. Cargo container3 serves Hospital HIMA Caribbean Medical Center.

<!-- b000284 | heading | pages [10] -->
4.2 ISO Cargo Containers Packing Configuration

<!-- b000285 | prose | pages [10] -->
After analysis, we need to pack three containers. The goal is to make each container hold the required drones and as many medical packages as possible. This problem is regarded as a three-dimensional packing problem. It is a combinatorial optimization problem that focuses on how to achieve optimal space utilization in a limited space. The 3BP problem is a NP-hard problem. There are many solutions to typical three-dimensional packing problems, most of which use the heuristic algorithm to solve the problems and obtain an approximate solution. However, the heuristic algorithm is not suitable for solving the problems we need to solve here. First, in the disaster response system, the total number of medical packages and drones to be loaded in each container is very large. If we use heuristic algorithm to solve the problem, its convergence rate is too slow. Secondly, the packing scheme obtained by heuristic algorithm is too difficult to realize in practice.

<!-- b000286 | prose | pages [10] -->
Therefore, we propose a one-dimensional maximum utilization (ODMU) method of

<!-- b000287 | furniture | pages [10] -->


<!-- b000288 | prose | pages [10] -->
“medical package first, UAV later", which can not only use the space of ISO cargo container

<!-- b000289 | furniture | pages [11] -->


<!-- b000290 | furniture | pages [11] -->
Team # 1924588                                                                  Page 7 of 29

<!-- b000291 | prose | pages [11] -->
as much as possible, but also facilitate the loading of medical package into the container in the actual situation.

<!-- b000292 | heading | pages [11] -->
4.2.1 Model establishment

<!-- b000293 | prose | pages [11] -->
{ C C C , , } We can assume that: The ISO cargo containers is

<!-- b000294 | prose | pages [11] -->
  =  U U , U , U , U

<!-- b000295 | prose | pages [11] -->
. The drone shipping 1 2 3

<!-- b000296 | prose | pages [11] -->
  = P P P P , , . The medical packages is containers is A B C H . 1 2 3

<!-- b000297 | prose | pages [11] -->
Consider that the internal dimensions of ISO cargo containers are：Length is L . Width is W . Height is H . The volume is V . The size of a drone transport container is：{ length

<!-- b000298 | prose | pages [11] -->
i

<!-- b000299 | prose | pages [11] -->
L , width

<!-- b000300 | prose | pages [11] -->
W , height

<!-- b000301 | prose | pages [11] -->
H

<!-- b000302 | prose | pages [11] -->
V },

<!-- b000303 | prose | pages [11] -->
, volume

<!-- b000304 | prose | pages [11] -->
U

<!-- b000305 | prose | pages [11] -->
U

<!-- b000306 | prose | pages [11] -->
U

<!-- b000307 | prose | pages [11] -->
U

<!-- b000308 | prose | pages [11] -->
i

<!-- b000309 | prose | pages [11] -->
i

<!-- b000310 | prose | pages [11] -->
i

<!-- b000311 | prose | pages [11] -->
i

<!-- b000312 | prose | pages [11] -->
W , height

<!-- b000313 | prose | pages [11] -->
L , width

<!-- b000314 | prose | pages [11] -->
packages are：{length

<!-- b000315 | prose | pages [11] -->
jP

<!-- b000316 | prose | pages [11] -->
jP

<!-- b000317 | prose | pages [11] -->
= = A , , H . The size of the emergency medical

<!-- b000318 | prose | pages [11] -->
j = 1,2,3

<!-- b000319 | prose | pages [11] -->
H H

<!-- b000320 | prose | pages [11] -->
V },

<!-- b000321 | prose | pages [11] -->
, volume

<!-- b000322 | prose | pages [11] -->
. Let the sum of the

<!-- b000323 | prose | pages [11] -->
jP

<!-- b000324 | prose | pages [11] -->
jP

<!-- b000325 | prose | pages [11] -->
{ V V , , V } ： volumes of all drones and medical packages be

<!-- b000326 | prose | pages [11] -->
 = V (

<!-- b000327 | furniture | pages [11] -->


<!-- b000328 | prose | pages [11] -->
tk

<!-- b000329 | prose | pages [11] -->
k = 1,2,3

<!-- b000330 | prose | pages [11] -->
t 1 t 2 t 3

<!-- b000331 | prose | pages [11] -->
+ cV n V ) (4)

<!-- b000332 | furniture | pages [11] -->


<!-- b000333 | prose | pages [11] -->
i i U j P i j

<!-- b000334 | prose | pages [11] -->
jn represents the number of ic  represents the number of drones of type i , ,

<!-- b000335 | prose | pages [11] -->
medical packages of type j .

<!-- b000336 | prose | pages [11] -->
The assumption is that medical packages and drone shipping container cannot be inverted. "Medical package first, drone later" one-dimensional maximum utilization(ODMU) method steps are as follows：

<!-- b000337 | prose | pages [11] -->
Step1: Suppose the ISO cargo container only contains one kind of medical package. At the very beginning, only medical packages are considered, and drones are not considered. Fill the container with medical packages.

<!-- b000338 | prose | pages [11] -->
Step2: If there are two or three kinds of medical packages in the container, pack them proportionally according to the number of medical packages that need delivery every day. For example, if the ratio of three medical packages is 5:2:3, pack five No. 1 packages, two No. 2 packages, and three No. 3 packages together. Fill the container with packed medical packages until the packed medical packages cannot be put in.

<!-- b000339 | prose | pages [11] -->
Step3: When putting medical packages into ISO cargo containers, ODMU method is used to place them. This placement method can not only make space

<!-- b000340 | prose | pages [11] -->
more convenient, but also make it easier to place a large number of medical packages in containers. The specific steps are as follows：

<!-- b000341 | prose | pages [11] -->
⚫ Assume that the width of the medical package is w, the length is l , and the height is h .

<!-- b000342 | prose | pages [11] -->
First consider minimizing the remaining length of one side (length or width) of the ISO cargo container. Making the best use of one side (long or wide) of the container when placing the medical package. By reasonable combination of length and width, the remaining length of this edge is minimized. [ ] means take integer：

<!-- b000343 | furniture | pages [11] -->


<!-- b000344 | prose | pages [11] -->
= − −

<!-- b000345 | prose | pages [11] -->
=

<!-- b000346 | prose | pages [11] -->
L L n l n w

<!-- b000347 | prose | pages [11] -->
W W

<!-- b000348 | prose | pages [11] -->
remain 1 2 remain 1

<!-- b000349 | prose | pages [11] -->
 

<!-- b000350 | prose | pages [11] -->
 

<!-- b000351 | prose | pages [11] -->
W

<!-- b000352 | prose | pages [11] -->
W (5)

<!-- b000353 | prose | pages [11] -->
−

<!-- b000354 | prose | pages [11] -->
= −

<!-- b000355 | prose | pages [11] -->
*

<!-- b000356 | prose | pages [11] -->
l

<!-- b000357 | prose | pages [11] -->
W W

<!-- b000358 | prose | pages [11] -->
*

<!-- b000359 | prose | pages [11] -->
w

<!-- b000360 | furniture | pages [11] -->


<!-- b000361 | prose | pages [11] -->


<!-- b000362 | prose | pages [11] -->


<!-- b000363 | prose | pages [11] -->
remain 2

<!-- b000364 | prose | pages [11] -->
l

<!-- b000365 | prose | pages [11] -->
w

<!-- b000366 | prose | pages [11] -->
 

<!-- b000367 | prose | pages [11] -->
 

<!-- b000368 | furniture | pages [12] -->


<!-- b000369 | furniture | pages [12] -->
Team # 1924588                                                                  Page 8 of 29

<!-- b000370 | prose | pages [12] -->
− − − −

<!-- b000371 | prose | pages [12] -->
n w W

<!-- b000372 | prose | pages [12] -->
min(

<!-- b000373 | prose | pages [12] -->
L n l

<!-- b000374 | prose | pages [12] -->
1 2

<!-- b000375 | prose | pages [12] -->
  

<!-- b000376 | prose | pages [12] -->
n

<!-- b000377 | prose | pages [12] -->
0,

<!-- b000378 | prose | pages [12] -->
n

<!-- b000379 | furniture | pages [12] -->


<!-- b000380 | prose | pages [12] -->
1 1

<!-- b000381 | prose | pages [12] -->
 

<!-- b000382 | prose | pages [12] -->
s t

<!-- b000383 | prose | pages [12] -->
. .

<!-- b000384 | prose | pages [12] -->
n

<!-- b000385 | prose | pages [12] -->
0,

<!-- b000386 | prose | pages [12] -->
n

<!-- b000387 | prose | pages [12] -->


<!-- b000388 | prose | pages [12] -->
2 2

<!-- b000389 | prose | pages [12] -->
+  

<!-- b000390 | prose | pages [12] -->
n l n w

<!-- b000391 | prose | pages [12] -->
1 2

<!-- b000392 | prose | pages [12] -->
, ,

<!-- b000393 | prose | pages [12] -->
n l n w

<!-- b000394 | prose | pages [12] -->
)

<!-- b000395 | prose | pages [12] -->
1 2

<!-- b000396 | prose | pages [12] -->
N N

<!-- b000397 | furniture | pages [12] -->


<!-- b000398 | prose | pages [12] -->
(6)

<!-- b000399 | prose | pages [12] -->
N N

<!-- b000400 | prose | pages [12] -->
+ 

<!-- b000401 | prose | pages [12] -->
L or n l n w W

<!-- b000402 | prose | pages [12] -->
1 2

<!-- b000403 | prose | pages [12] -->
⚫ Calculate the maximum number of medical packages that can be placed on a two-

<!-- b000404 | prose | pages [12] -->
dimensional plane. (Since it is assumed that the medical package and the drone shipping container cannot be inverted, each two-dimensional plane is placed at the same height as the medical package）

<!-- b000405 | furniture | pages [12] -->


<!-- b000406 | caption | pages [12] -->
Figure 4 Two-dimensional plane placement

<!-- b000407 | prose | pages [12] -->
⚫ Place the medical packages overlapping until the top space is not enough to place the

<!-- b000408 | prose | pages [12] -->
medical packages.

<!-- b000409 | furniture | pages [12] -->


<!-- b000410 | caption | pages [12] -->
Figure 5 Residual space

<!-- b000411 | prose | pages [12] -->
= H

<!-- b000412 | furniture | pages [12] -->


<!-- b000413 | prose | pages [12] -->
remain

<!-- b000414 | prose | pages [12] -->
H − H H

<!-- b000415 | prose | pages [12] -->
[ ]*

<!-- b000416 | prose | pages [12] -->
h

<!-- b000417 | furniture | pages [12] -->


<!-- b000418 | prose | pages [12] -->
(7) h

<!-- b000419 | prose | pages [12] -->
Step4: Suppose the medical package is full of ISO containers. Consider removing a certain number of medical packages from containers until UAVs can be put in. After putting the medical package in place, there will be some gaps in the left (or right) side, front and upper side of the container. Therefore, when loading the UAV, priority should be given to removing

<!-- b000420 | furniture | pages [13] -->


<!-- b000421 | furniture | pages [13] -->
Team # 1924588                                                                  Page 9 of 29

<!-- b000422 | prose | pages [13] -->
the medical package from the slotted position. This will minimize the number of medical packages taken out.

<!-- b000423 | furniture | pages [13] -->


<!-- b000424 | caption | pages [13] -->
Figure 6 UAV placement

<!-- b000425 | prose | pages [13] -->
There are two ways to put UAVs in containers:

<!-- b000426 | prose | pages [13] -->
⚫ The length direction of the UAV corresponds to the length direction of the

<!-- b000427 | prose | pages [13] -->
container, and the width direction of the UAV corresponds to the width direction of the container.

<!-- b000428 | prose | pages [13] -->
⚫ The length direction of the UAV corresponds to the width direction of the

<!-- b000429 | prose | pages [13] -->
container, and the width direction of the UAV corresponds to the length direction of the container.

<!-- b000430 | prose | pages [13] -->
The number of medical packages to be removed from the height of the container is calculated as follows：

<!-- b000431 | prose | pages [13] -->
H

<!-- b000432 | prose | pages [13] -->
U

<!-- b000433 | prose | pages [13] -->
=

<!-- b000434 | prose | pages [13] -->
n

<!-- b000435 | prose | pages [13] -->
[ i

<!-- b000436 | furniture | pages [13] -->


<!-- b000437 | prose | pages [13] -->
H

<!-- b000438 | prose | pages [13] -->
− −

<!-- b000439 | prose | pages [13] -->
H

<!-- b000440 | prose | pages [13] -->
remain ]+1

<!-- b000441 | prose | pages [13] -->
(8)

<!-- b000442 | furniture | pages [13] -->


<!-- b000443 | prose | pages [13] -->
h

<!-- b000444 | prose | pages [13] -->
The number of medical packages to be removed from the length of the container is calculated as follows：

<!-- b000445 | prose | pages [13] -->
−

<!-- b000446 | prose | pages [13] -->
L L U remain

<!-- b000447 | prose | pages [13] -->
=

<!-- b000448 | prose | pages [13] -->
n [ ]+1 i

<!-- b000449 | furniture | pages [13] -->


<!-- b000450 | prose | pages [13] -->
L 1 l

<!-- b000451 | furniture | pages [13] -->


<!-- b000452 | prose | pages [13] -->
−

<!-- b000453 | prose | pages [13] -->
W L U remain

<!-- b000454 | prose | pages [13] -->
=

<!-- b000455 | prose | pages [13] -->
n [ ]+1 i

<!-- b000456 | furniture | pages [13] -->


<!-- b000457 | prose | pages [13] -->
L 2 l

<!-- b000458 | prose | pages [13] -->
−

<!-- b000459 | prose | pages [13] -->
L L U remain or n =[ ]+1 i

<!-- b000460 | prose | pages [13] -->
(9)

<!-- b000461 | furniture | pages [13] -->


<!-- b000462 | prose | pages [13] -->
L 1 w

<!-- b000463 | prose | pages [13] -->
−

<!-- b000464 | prose | pages [13] -->
W L U remain or n =[ ]+1 i

<!-- b000465 | prose | pages [13] -->
(10)

<!-- b000466 | furniture | pages [13] -->


<!-- b000467 | prose | pages [13] -->
L 2 w

<!-- b000468 | prose | pages [13] -->
The number of medical packages to be removed from the width of the container is calculated as follows：

<!-- b000469 | prose | pages [13] -->
−

<!-- b000470 | prose | pages [13] -->
W W U remain

<!-- b000471 | prose | pages [13] -->
=

<!-- b000472 | prose | pages [13] -->
n [ ]+1 i

<!-- b000473 | furniture | pages [13] -->


<!-- b000474 | prose | pages [13] -->
W 1 l

<!-- b000475 | furniture | pages [13] -->


<!-- b000476 | prose | pages [13] -->
−

<!-- b000477 | prose | pages [13] -->
L W

<!-- b000478 | furniture | pages [13] -->


<!-- b000479 | prose | pages [13] -->
U remain

<!-- b000480 | prose | pages [13] -->
=

<!-- b000481 | prose | pages [13] -->
n [ ]+1 i W 2 l

<!-- b000482 | furniture | pages [13] -->


<!-- b000483 | furniture | pages [13] -->


<!-- b000484 | prose | pages [13] -->
−

<!-- b000485 | prose | pages [13] -->
W W U remain or n =[ ]+1 i

<!-- b000486 | prose | pages [13] -->
(11)

<!-- b000487 | furniture | pages [13] -->


<!-- b000488 | prose | pages [13] -->
W 1 w

<!-- b000489 | prose | pages [13] -->
−

<!-- b000490 | prose | pages [13] -->
L W

<!-- b000491 | prose | pages [13] -->
(12)

<!-- b000492 | prose | pages [13] -->
U remain or n =[ ]+1 i

<!-- b000493 | furniture | pages [13] -->


<!-- b000494 | prose | pages [13] -->
W 2 w

<!-- b000495 | furniture | pages [14] -->


<!-- b000496 | furniture | pages [14] -->
Team # 1924588                                                                  Page 10 of 29

<!-- b000497 | prose | pages [14] -->
The final number of medical packages to be removed is calculated as follows:

<!-- b000498 | prose | pages [14] -->
num num min{

<!-- b000499 | prose | pages [14] -->
num 1= n * n * n ,

<!-- b000500 | furniture | pages [14] -->


<!-- b000501 | prose | pages [14] -->
L 1 W 1 H

<!-- b000502 | prose | pages [14] -->
1, 2}

<!-- b000503 | furniture | pages [14] -->


<!-- b000504 | prose | pages [14] -->
num 2= n * n * n (13) L 2 W 2 H

<!-- b000505 | prose | pages [14] -->
Step5: Follow these steps to design the associated packing configuration for three ISO cargo containers. Finally, the corresponding number of medical packages and drones can be put into the ISO cargo container according to the designed scheme. This method can make full use of shipping container space.

<!-- b000506 | heading | pages [14] -->
4.2.2 Result

<!-- b000507 | prose | pages [14] -->
The size of the ISO container, the size of the medical package and the size of the UAV

<!-- b000508 | furniture | pages [14] -->


<!-- b000509 | prose | pages [14] -->
shipping container given in the attachment are substituted into the model for solving, and the results are shown in table 4：

<!-- b000510 | prose | pages [14] -->
Scheme 1：

<!-- b000511 | caption | pages [14] -->
Table 4 ISO container scheme 1

<!-- b000512 | prose | pages [14] -->
Container Number Proportion of three medical 1 2 3

<!-- b000513 | prose | pages [14] -->
（1:0:0） packages （3:2:2） （3:0:2）

<!-- b000514 | prose | pages [14] -->
3352 MED1

<!-- b000515 | prose | pages [14] -->
Number

<!-- b000516 | prose | pages [14] -->
MED2

<!-- b000517 | prose | pages [14] -->
MED3

<!-- b000518 | prose | pages [14] -->
Medical total volume

<!-- b000519 | prose | pages [14] -->
1350 1983

<!-- b000520 | prose | pages [14] -->
0 900 0

<!-- b000521 | prose | pages [14] -->
0 900 1322

<!-- b000522 | prose | pages [14] -->
1642480 （Cubic inch） 1143900 1415862

<!-- b000523 | prose | pages [14] -->
1B+1H UAV UAV total volume （Cubic 1G+1H 1B+1C+1H

<!-- b000524 | prose | pages [14] -->
219675 inch） 217283 309675

<!-- b000525 | prose | pages [14] -->
93.22% Spatial Utilization Rate

<!-- b000526 | prose | pages [14] -->
Scheme 2：

<!-- b000527 | prose | pages [14] -->
68.14% 86.38%

<!-- b000528 | caption | pages [14] -->
Table 4 ISO container scheme 1

<!-- b000529 | prose | pages [14] -->
Container Number Proportion of three medical 1 2 3

<!-- b000530 | prose | pages [14] -->
（1:0:0） packages （5:2:3） （1:0:1）

<!-- b000531 | prose | pages [14] -->
3352 MED1

<!-- b000532 | prose | pages [14] -->
Number

<!-- b000533 | prose | pages [14] -->
MED2

<!-- b000534 | prose | pages [14] -->
MED3

<!-- b000535 | prose | pages [14] -->
1550 1847

<!-- b000536 | prose | pages [14] -->
0 620 0

<!-- b000537 | prose | pages [14] -->
0 930 1847

<!-- b000538 | furniture | pages [15] -->


<!-- b000539 | furniture | pages [15] -->
Team # 1924588                                                                  Page 11 of 29

<!-- b000540 | prose | pages [15] -->
Medical total volume

<!-- b000541 | prose | pages [15] -->
1642480 （Cubic inch） 1195980 1525622

<!-- b000542 | prose | pages [15] -->
1B+1H UAV UAV total volume（Cubic 1C+1H 1D+1H

<!-- b000543 | prose | pages [15] -->
219675 inch） 289875 212375

<!-- b000544 | prose | pages [15] -->
93.22% Spatial Utilization Rate 74.38% 87%

<!-- b000545 | prose | pages [15] -->
From table 4 and table 5, we can get the results of the two schemes. The number of medical packages is sufficient to provide long-term support to hospitals in Puerto Rico. In addition, we can see that the utilization rate of space is relatively high. If only package No. 1 is placed in the container, the space utilization rate can reach 93.22%. In the case of multiple packages placed in a container, because packages need to be packed proportionally first, and then put the packaged package into the container., the waste of space during packaging will make the space utilization rate relatively low. However, in terms of realizability, the use of this scheme loses part of the space utilization rate in exchange for greater convenience.

<!-- b000546 | heading | pages [15] -->
4.3 Optimization model of the best container location

<!-- b000547 | prose | pages [15] -->
According to the analysis in question A, we have come to the conclusion that the three containers of the DroneGo disaster-related system must be placed in three different locations. Under the condition of completing the distribution task of medical supplies, the road network should be reconnoitered as comprehensively as possible.

<!-- b000548 | heading | pages [15] -->
4.3.1 Road Grid Model

<!-- b000549 | furniture | pages [15] -->


<!-- b000550 | prose | pages [15] -->
In order to describe the situation of road reconnaissance, we first grid the road. The main disaster area of Puerto Rico is transformed into a discrete space set by meshing. The length and area of each grid are equal. A distinction is made between a grid with a main road and a grid without a main road. The former is marked by 1, called "traversed grid"(TG). The latter is marked by 0, called " untraversed grid ".Set the symbol TG, if the grid is traversed grid, TG=1. Otherwise TG=0. Complete the discrete treatment of roads. We can construct a new coordinate system in a meshed graph, called " Grid coordinate system". The results of road gridding are shown in the figure 7.

<!-- b000551 | furniture | pages [15] -->


<!-- b000552 | caption | pages [15] -->
Figure 7 The results of road gridding

<!-- b000553 | furniture | pages [16] -->


<!-- b000554 | furniture | pages [16] -->
Team # 1924588                                                                  Page 12 of 29

<!-- b000555 | furniture | pages [16] -->


<!-- b000556 | prose | pages [16] -->
According to the actual distance and the number of meshes, the transformation relationship between the real coordinates and the grid coordinates can be calculated, that is, the distance represented by the unit length in the Grid coordinate system is as follows：

<!-- b000557 | prose | pages [16] -->
113.99

<!-- b000558 | prose | pages [16] -->
km = G

<!-- b000559 | prose | pages [16] -->
ave 91

<!-- b000560 | prose | pages [16] -->
cells =

<!-- b000561 | prose | pages [16] -->
1.281

<!-- b000562 | prose | pages [16] -->
km cell

<!-- b000563 | prose | pages [16] -->
/

<!-- b000564 | furniture | pages [16] -->


<!-- b000565 | heading | pages [16] -->
4.3.2 Mapping Hospital Location to Grid Model

<!-- b000566 | prose | pages [16] -->
According to the location coordinates of the hospitals in attachment 4 and the corresponding relationship between the grid coordinates and the geographical coordinates, the positions of the hospitals in the grid coordinate system can be expressed. The results are as follows.：

<!-- b000567 | caption | pages [16] -->
Table 5 The positions of the hospitals

<!-- b000568 | prose | pages [16] -->
Hospital Ⅲ HospitalⅠ HospitalⅡ Hospital Ⅳ Hospital Ⅴ (6 , 57) (15 , 92) (25 , 61) (11 , 51) (4 , 4) Represents in grid coordinates as shown in Figure 8.

<!-- b000569 | furniture | pages [16] -->


<!-- b000570 | caption | pages [16] -->
Figure 8 The positions of the hospitals

<!-- b000571 | heading | pages [16] -->
4.3.3. Establishment of Optimization Model

<!-- b000572 | furniture | pages [16] -->


<!-- b000573 | prose | pages [16] -->
Determine the place where containers are put into operation, and optimize the objective of investigating the road network as comprehensively as possible. In the road grid model, if the container is placed at this location, we will take that location as the center of the circle. The area that the UAV can detect is a circular area with a radius of half of the maximum flight distance of the UAV. The larger the number of traversed grids included in the investigation area, the wider the range of roads that the UAV can detect. The constraints of the optimization model are that the distance between each container and its corresponding hospital is less than half of the maximum flight distance of the UAV.

<!-- b000574 | prose | pages [16] -->
D . If the iF in a container, the maximum flight distance of the cargo is

<!-- b000575 | furniture | pages [16] -->


<!-- b000576 | prose | pages [16] -->
For an UAV i

<!-- b000577 | prose | pages [16] -->
P x y ( , ) .Take ( , x y ) position of ISO cargo container in grid coordinates is as the center of k i j i j

<!-- b000578 | prose | pages [16] -->
D , can be written as i

<!-- b000579 | prose | pages [16] -->
the circle, so a circle with radius 2

<!-- b000580 | prose | pages [16] -->
The objective of optimization is：

<!-- b000581 | prose | pages [16] -->
Cir .

<!-- b000582 | prose | pages [16] -->
i

<!-- b000583 | furniture | pages [17] -->


<!-- b000584 | furniture | pages [17] -->
Team # 1924588                                                                  Page 13 of 29

<!-- b000585 | prose | pages [17] -->


<!-- b000586 | furniture | pages [17] -->


<!-- b000587 | prose | pages [17] -->
 TG TG max , , Cir

<!-- b000588 | furniture | pages [17] -->


<!-- b000589 | prose | pages [17] -->
(14) i

<!-- b000590 | prose | pages [17] -->
For example, in scheme 1, ISO cargo Container2. If UAVs in containers need to serve multiple h ( , ) p q , the constraint condition are： hospitals and the coordinates of the hospital are

<!-- b000591 | prose | pages [17] -->


<!-- b000592 | prose | pages [17] -->
D

<!-- b000593 | prose | pages [17] -->


<!-- b000594 | prose | pages [17] -->
S h

<!-- b000595 | prose | pages [17] -->
( ,

<!-- b000596 | prose | pages [17] -->
P

<!-- b000597 | prose | pages [17] -->
)

<!-- b000598 | prose | pages [17] -->


<!-- b000599 | prose | pages [17] -->
m k

<!-- b000600 | prose | pages [17] -->
2

<!-- b000601 | prose | pages [17] -->
s t

<!-- b000602 | prose | pages [17] -->
. .

<!-- b000603 | furniture | pages [17] -->


<!-- b000604 | prose | pages [17] -->
 =

<!-- b000605 | prose | pages [17] -->
S h

<!-- b000606 | prose | pages [17] -->
( ,

<!-- b000607 | prose | pages [17] -->
P

<!-- b000608 | prose | pages [17] -->
)

<!-- b000609 | prose | pages [17] -->


<!-- b000610 | prose | pages [17] -->
m k

<!-- b000611 | prose | pages [17] -->
m

<!-- b000612 | prose | pages [17] -->
=

<!-- b000613 | prose | pages [17] -->
i i

<!-- b000614 | prose | pages [17] -->
, ,

<!-- b000615 | prose | pages [17] -->
m

<!-- b000616 | prose | pages [17] -->
1,2,3

<!-- b000617 | furniture | pages [17] -->


<!-- b000618 | prose | pages [17] -->
(15)

<!-- b000619 | prose | pages [17] -->
− + −

<!-- b000620 | prose | pages [17] -->
2 2

<!-- b000621 | prose | pages [17] -->
( (

<!-- b000622 | prose | pages [17] -->
x x p

<!-- b000623 | prose | pages [17] -->
) (

<!-- b000624 | prose | pages [17] -->
y q

<!-- b000625 | prose | pages [17] -->
)

<!-- b000626 | prose | pages [17] -->
i i j

<!-- b000627 | prose | pages [17] -->
For example, container3 in Scheme 2. If there are multiple UAVs in the container for transportation, the constraint condition is：

<!-- b000628 | prose | pages [17] -->


<!-- b000629 | prose | pages [17] -->
D

<!-- b000630 | prose | pages [17] -->


<!-- b000631 | prose | pages [17] -->
S h

<!-- b000632 | prose | pages [17] -->
( ,

<!-- b000633 | prose | pages [17] -->
P

<!-- b000634 | prose | pages [17] -->
)

<!-- b000635 | prose | pages [17] -->


<!-- b000636 | prose | pages [17] -->
m k

<!-- b000637 | prose | pages [17] -->
2

<!-- b000638 | prose | pages [17] -->
s t

<!-- b000639 | prose | pages [17] -->
. .

<!-- b000640 | furniture | pages [17] -->


<!-- b000641 | prose | pages [17] -->
 =

<!-- b000642 | prose | pages [17] -->
S h

<!-- b000643 | prose | pages [17] -->
( ,

<!-- b000644 | prose | pages [17] -->
P

<!-- b000645 | prose | pages [17] -->
)

<!-- b000646 | prose | pages [17] -->


<!-- b000647 | prose | pages [17] -->
m k

<!-- b000648 | heading | pages [17] -->
4.3.4 Result

<!-- b000649 | prose | pages [17] -->
= =

<!-- b000650 | prose | pages [17] -->
i i

<!-- b000651 | prose | pages [17] -->
, ,

<!-- b000652 | prose | pages [17] -->
m

<!-- b000653 | prose | pages [17] -->
1,2;

<!-- b000654 | prose | pages [17] -->
i

<!-- b000655 | prose | pages [17] -->
1,2

<!-- b000656 | furniture | pages [17] -->


<!-- b000657 | prose | pages [17] -->
(16)

<!-- b000658 | prose | pages [17] -->
− + −

<!-- b000659 | prose | pages [17] -->
2 2

<!-- b000660 | prose | pages [17] -->
( (

<!-- b000661 | prose | pages [17] -->
x x p

<!-- b000662 | prose | pages [17] -->
) (

<!-- b000663 | prose | pages [17] -->
y q

<!-- b000664 | prose | pages [17] -->
)

<!-- b000665 | prose | pages [17] -->
i i j

<!-- b000666 | prose | pages [17] -->
We found that there was no grid location in scheme 2, which could satisfy the need for two UAVs in cargo container3 to serve the target hospital at the same time. Therefore, we choose the scheme 1. The optimal grid points of three containers are obtained and the results are as follows:

<!-- b000667 | caption | pages [17] -->
Table 6 The optimal grid points of three containers

<!-- b000668 | prose | pages [17] -->
cargo container1 cargo container 2

<!-- b000669 | furniture | pages [17] -->


<!-- b000670 | prose | pages [17] -->
Coordinates (4,19)

<!-- b000671 | prose | pages [17] -->
Latitude and

<!-- b000672 | prose | pages [17] -->
(18.47, -66.5459) longitude

<!-- b000673 | prose | pages [17] -->
cargo container 3

<!-- b000674 | prose | pages [17] -->
(15,61) (15,89)

<!-- b000675 | prose | pages [17] -->
(18.339, -66.0305) (18.339, -65.6868)

<!-- b000676 | prose | pages [17] -->
The location in the map is shown in Figure 9, where the blue coordinates are the location of containers (red dots represent obstacles such as mountains, buildings, etc., which will be used in subsequent solutions).

<!-- b000677 | furniture | pages [17] -->


<!-- b000678 | caption | pages [17] -->
Figure 9 The location of containers

<!-- b000679 | furniture | pages [18] -->


<!-- b000680 | furniture | pages [18] -->
Team # 1924588                                                                  Page 14 of 29

<!-- b000681 | heading | pages [18] -->
4.4 Drone Payload Packaging Configuration

<!-- b000682 | prose | pages [18] -->
The drones deliver medical packages to hospitals, ensuring that each shipment will meet at least one day's hospital demand. If UAVs can deliver more than one day at a time to meet the needs of hospitals, then UAVs do not have to deliver medical packages to hospitals every day. UAV can use the extra time to accomplish some reconnaissance tasks. It has been assumed that the number of medical packages transported by UAVs is an integral multiple of the hospital's daily demand, and then the configuration of medical packages for Drone Cargo Bay is designed as follows[8].

<!-- b000683 | prose | pages [18] -->
W , height is bL , width is H , the length Let the length of drone cargo bay type 1 be

<!-- b000684 | furniture | pages [18] -->


<!-- b000685 | prose | pages [18] -->
bL , width is

<!-- b000686 | prose | pages [18] -->
b 1 1 b 1

<!-- b000687 | prose | pages [18] -->
W , height is of drone cargo bay type 2 is 2

<!-- b000688 | prose | pages [18] -->
  +  + ( n w n l ) L ( n w

<!-- b000689 | furniture | pages [18] -->


<!-- b000690 | prose | pages [18] -->
i jj j ii bk j jj ,

<!-- b000691 | prose | pages [18] -->
 + ( n m n m p 1 1 p 2

<!-- b000692 | prose | pages [18] -->
n n n ,

<!-- b000693 | prose | pages [18] -->
H . b b 2 2 b 2

<!-- b000694 | prose | pages [18] -->
  +  n l n l ) W ( n h n h ) H

<!-- b000695 | prose | pages [18] -->
(17)

<!-- b000696 | prose | pages [18] -->
i ii bk jj m ii n bk ,

<!-- b000697 | furniture | pages [18] -->


<!-- b000698 | furniture | pages [18] -->


<!-- b000699 | prose | pages [18] -->
+  n m ) M

<!-- b000700 | prose | pages [18] -->
(18)

<!-- b000701 | prose | pages [18] -->
2 2 p 3 3 max

<!-- b000702 | furniture | pages [18] -->


<!-- b000703 | prose | pages [18] -->
is the number of three types of medical packages. , p 2 p 3 p 1

<!-- b000704 | prose | pages [18] -->
The final drone payload packing configurations are as follows（MED1 is green, MED2 is yellow, MED3 is blue）：

<!-- b000705 | prose | pages [18] -->
Drone D →HospitalⅠ: Drone B →HospitalⅤ:

<!-- b000706 | furniture | pages [18] -->


<!-- b000707 | prose | pages [18] -->
Drone C→Hospital Ⅲ:

<!-- b000708 | furniture | pages [18] -->


<!-- b000709 | prose | pages [18] -->
Drone C→HospitalⅡ:

<!-- b000710 | furniture | pages [18] -->


<!-- b000711 | prose | pages [18] -->
Drone C→Hospital Ⅳ:

<!-- b000712 | furniture | pages [18] -->


<!-- b000713 | caption | pages [18] -->
Figure 10 Drone payload packing configurations

<!-- b000714 | heading | pages [18] -->
4.5 UAV Delivery Route and Timetable

<!-- b000715 | prose | pages [18] -->
Normally, non-military UAVs fly at altitudes between 100 and 500 meters. As can be seen from the topographic map of Puerto Rico in attachment 1, there are many mountains and buildings in parts of the disaster area. Therefore, these obstacles need to be avoided in the design of delivery routes to improve the safety of UAVs. Distribution of obstacles in parts of the disaster area is shown in Figure 11.

<!-- b000716 | furniture | pages [19] -->


<!-- b000717 | furniture | pages [19] -->
Team # 1924588                                                                  Page 15 of 29

<!-- b000718 | furniture | pages [19] -->


<!-- b000719 | caption | pages [19] -->
Figure 11 Distribution of obstacles

<!-- b000720 | heading | pages [19] -->
4.5.1 Delivery Route Division

<!-- b000721 | prose | pages [19] -->
According to the figure above, we divide the UAV delivery into two types:

<!-- b000722 | prose | pages [19] -->
⚫ When there are many buildings or mountains near the container or UAV target

<!-- b000723 | prose | pages [19] -->
hospital, the UAV delivery route planning model with threat source is constructed to solve the problem, which is suitable for UAV in cargo container2. ⚫ When there are few buildings near the container and the target hospital, UAV flies to

<!-- b000724 | prose | pages [19] -->
the nearest road, then to the target hospital along the highway or directly to the target hospital along the straight line. It is suitable for cargo container1 and cargo container3 (Delivery and reconnaissance tasks can be carried out simultaneously)

<!-- b000725 | heading | pages [19] -->
4.5.2 Delivery Route Planning Model

<!-- b000726 | furniture | pages [19] -->


<!-- b000727 | prose | pages [19] -->
In order to avoid tall buildings and mountains during transportation, we consider mountains and buildings as a source of threat. Delivery routes are designed to find the nearest route to a destination hospital with minimal threat. Therefore, we first make the middle perpendicular of any two threat sources to form Voronio diagram. If the UAV flies along the edge of the Voronio diagram, the threat source will be the least, because the points on each edge of the Voronio diagram are equidistant from the corresponding two threat sources to ensure the security. Take cargo container2 as an example, and Voronio diagram is made according to the threat sources around it, as shown in figure 12.

<!-- b000728 | furniture | pages [19] -->


<!-- b000729 | caption | pages [19] -->
Figure 12 Voronio diagram

<!-- b000730 | furniture | pages [20] -->


<!-- b000731 | furniture | pages [20] -->
Team # 1924588                                                                  Page 16 of 29

<!-- b000732 | furniture | pages [20] -->


<!-- b000733 | prose | pages [20] -->
Each intersection point and three hospital locations in the figure 12 are regarded as target nodes.

<!-- b000734 | heading | pages [20] -->
4.5.3 Delivery Route Solution

<!-- b000735 | prose | pages [20] -->
According to Voronio diagram, we select Dijkstra algorithm to select the shortest route from the cargo container to other nodes. It should be noted that, since the starting point and destination location are not on the safe route, it is necessary to adjust the optimal route obtained by the algorithm. The algorithm flow chart is as follows:：

<!-- b000736 | furniture | pages [20] -->


<!-- b000737 | caption | pages [20] -->
Figure 13 algorithm flow chart

<!-- b000738 | prose | pages [20] -->
By calculation, the delivery route of the delivering for the hospital is expressed in the grid coordinate system as follows:

<!-- b000739 | caption | pages [20] -->
Table 7 The delivery route

<!-- b000740 | prose | pages [20] -->
D-type UAV to Caribbean Medical Center

<!-- b000741 | prose | pages [20] -->
C-type UAV to Hospital HIMA

<!-- b000742 | prose | pages [20] -->
C-type UAV to Hospital Pavia Santurce

<!-- b000743 | prose | pages [20] -->
C-type to Puerto Rico Children's Hospital

<!-- b000744 | prose | pages [20] -->
B-type UAV to Hospital Pavia Arecibo

<!-- b000745 | prose | pages [20] -->
→ (15,89) (15,92)

<!-- b000746 | prose | pages [20] -->
→ (15,61) (25,61)

<!-- b000747 | prose | pages [20] -->
→ → → (15,61) (13 58) (11,58) (6 57) ， ，

<!-- b000748 | prose | pages [20] -->
→ → (15,61) (11,54) (11,51)

<!-- b000749 | prose | pages [20] -->
→ → → (4,19) (5,18) (5,5) (4,4)

<!-- b000750 | prose | pages [20] -->
All the delivery routes are shown in the grid coordinate system as shown in Figure 14：

<!-- b000751 | furniture | pages [20] -->


<!-- b000752 | caption | pages [20] -->
Figure 14 The delivery routes

<!-- b000753 | furniture | pages [21] -->


<!-- b000754 | furniture | pages [21] -->
Team # 1924588                                                                  Page 17 of 29

<!-- b000755 | heading | pages [21] -->
4.5.4 Delivery schedule

<!-- b000756 | prose | pages [21] -->
According to the location of the container, the number and type of UAV, and the packing configuration of each medical package delivered by the UAV. We set the delivery schedule of the UAV as follows (only the time schedule for completing the delivery task is given, considering that the overall time schedule for the reconnaissance video task will be completed in Question C.b).

<!-- b000757 | caption | pages [21] -->
Table 8 Time schedule for the reconnaissance video task

<!-- b000758 | prose | pages [21] -->
Day2 Day1 time of

<!-- b000759 | prose | pages [21] -->
time of

<!-- b000760 | prose | pages [21] -->
time of

<!-- b000761 | prose | pages [21] -->
departure

<!-- b000762 | prose | pages [21] -->
return

<!-- b000763 | prose | pages [21] -->
departure

<!-- b000764 | prose | pages [21] -->
1F →Ⅰ 8:30 8: 41

<!-- b000765 | prose | pages [21] -->
Day3

<!-- b000766 | prose | pages [21] -->
time of

<!-- b000767 | prose | pages [21] -->
time of

<!-- b000768 | prose | pages [21] -->
time of

<!-- b000769 | prose | pages [21] -->
return

<!-- b000770 | prose | pages [21] -->
departure

<!-- b000771 | prose | pages [21] -->
return

<!-- b000772 | prose | pages [21] -->
1F →Ⅰ 8:30 8: 41

<!-- b000773 | prose | pages [21] -->
1F →Ⅰ 8:30

<!-- b000774 | prose | pages [21] -->
F →Ⅱ 8:30 8:58 2

<!-- b000775 | prose | pages [21] -->
F →Ⅴ 8:30 9 : 02 3

<!-- b000776 | prose | pages [21] -->
F →Ⅲ12:30 12 :54 2

<!-- b000777 | prose | pages [21] -->
F →Ⅱ 8:30

<!-- b000778 | prose | pages [21] -->
8: 41

<!-- b000779 | prose | pages [21] -->
8:58 2

<!-- b000780 | prose | pages [21] -->
F →Ⅴ 8:30 9 : 02 3

<!-- b000781 | prose | pages [21] -->
F →Ⅳ16:30 2

<!-- b000782 | prose | pages [21] -->
F →Ⅳ16:30 16 :57 2

<!-- b000783 | prose | pages [21] -->
F →Ⅳ 16:30 16 :57 16 :57 2

<!-- b000784 | prose | pages [21] -->
（The UAV's fourth day schedule is the same as the first day, and the cycle is three days, so we only give a three-day schedule.）

<!-- b000785 | heading | pages [21] -->
4.6 Drone Flight Plan

<!-- b000786 | heading | pages [21] -->
4.6.1 Model establishment

<!-- b000787 | prose | pages [21] -->
The flight plan of the UAV includes two aspects: flight schedule and flight route arrangement. The time arrangement can be determined according to the working frequency of the UAV and the schedule of the delivery of medical packages by the UAV. Here we mainly discuss the arrangement of flight routes[7].

<!-- b000788 | prose | pages [21] -->
The ISO container where the drone is located is the starting point for each drone mission,

<!-- b000789 | furniture | pages [21] -->


<!-- b000790 | prose | pages [21] -->
while the TG near the container is the area the drone needs to reconnoitre. Our goal is to allow the drone to fly through all TG and back to the container within its own reconnaissance range with the minimum flight distance. Let's the starting point plus all the TG's in the range = V {1,2, N } is the set of points for all points to pass through. have N points.

<!-- b000791 | prose | pages [21] -->
 d ,i j V （ The distance between each point is ij

<!-- b000792 | prose | pages [21] -->


<!-- b000793 | prose | pages [21] -->
）.

<!-- b000794 | prose | pages [21] -->
The connection between i and j is on the optimal route of the drone

<!-- b000795 | prose | pages [21] -->
1

<!-- b000796 | prose | pages [21] -->
=  x

<!-- b000797 | prose | pages [21] -->
ij 0

<!-- b000798 | prose | pages [21] -->
otherwise

<!-- b000799 | prose | pages [21] -->


<!-- b000800 | furniture | pages [21] -->


<!-- b000801 | prose | pages [21] -->
Then the UAV line planning model can be written in the following linear programming form:

<!-- b000802 | furniture | pages [22] -->


<!-- b000803 | furniture | pages [22] -->
Team # 1924588                                                                  Page 18 of 29

<!-- b000804 | prose | pages [22] -->


<!-- b000805 | prose | pages [22] -->
min

<!-- b000806 | prose | pages [22] -->
d x

<!-- b000807 | prose | pages [22] -->
ij ij

<!-- b000808 | prose | pages [22] -->


<!-- b000809 | prose | pages [22] -->
i j

<!-- b000810 | prose | pages [22] -->


<!-- b000811 | prose | pages [22] -->
N

<!-- b000812 | prose | pages [22] -->


<!-- b000813 | prose | pages [22] -->
=

<!-- b000814 | prose | pages [22] -->
x

<!-- b000815 | prose | pages [22] -->
1

<!-- b000816 | prose | pages [22] -->


<!-- b000817 | prose | pages [22] -->
ij

<!-- b000818 | prose | pages [22] -->


<!-- b000819 | prose | pages [22] -->
=

<!-- b000820 | prose | pages [22] -->
j

<!-- b000821 | prose | pages [22] -->
1

<!-- b000822 | prose | pages [22] -->


<!-- b000823 | prose | pages [22] -->
N

<!-- b000824 | furniture | pages [22] -->


<!-- b000825 | prose | pages [22] -->


<!-- b000826 | prose | pages [22] -->
=

<!-- b000827 | prose | pages [22] -->
x

<!-- b000828 | prose | pages [22] -->
1

<!-- b000829 | prose | pages [22] -->
s t

<!-- b000830 | prose | pages [22] -->
. .

<!-- b000831 | prose | pages [22] -->


<!-- b000832 | prose | pages [22] -->
ij

<!-- b000833 | prose | pages [22] -->
=

<!-- b000834 | prose | pages [22] -->
i

<!-- b000835 | prose | pages [22] -->
1

<!-- b000836 | prose | pages [22] -->


<!-- b000837 | prose | pages [22] -->


<!-- b000838 | prose | pages [22] -->


<!-- b000839 | prose | pages [22] -->
x

<!-- b000840 | prose | pages [22] -->
|

<!-- b000841 | prose | pages [22] -->
K

<!-- b000842 | prose | pages [22] -->


<!-- b000843 | prose | pages [22] -->
ij

<!-- b000844 | prose | pages [22] -->


<!-- b000845 | prose | pages [22] -->


<!-- b000846 | prose | pages [22] -->
i j K

<!-- b000847 | prose | pages [22] -->
,

<!-- b000848 | prose | pages [22] -->
 

<!-- b000849 | prose | pages [22] -->
x

<!-- b000850 | prose | pages [22] -->
{0,1}

<!-- b000851 | prose | pages [22] -->


<!-- b000852 | prose | pages [22] -->
ij

<!-- b000853 | prose | pages [22] -->
=

<!-- b000854 | prose | pages [22] -->
i

<!-- b000855 | prose | pages [22] -->
1,2,

<!-- b000856 | prose | pages [22] -->
N

<!-- b000857 | furniture | pages [22] -->


<!-- b000858 | prose | pages [22] -->
(19)

<!-- b000859 | prose | pages [22] -->
=

<!-- b000860 | prose | pages [22] -->
j

<!-- b000861 | prose | pages [22] -->
1,2,

<!-- b000862 | prose | pages [22] -->
N

<!-- b000863 | prose | pages [22] -->
− 

<!-- b000864 | prose | pages [22] -->
| 1

<!-- b000865 | prose | pages [22] -->
K V

<!-- b000866 | prose | pages [22] -->


<!-- b000867 | prose | pages [22] -->
i j

<!-- b000868 | prose | pages [22] -->
,

<!-- b000869 | prose | pages [22] -->
V

<!-- b000870 | heading | pages [22] -->
4.6.2 Using Ant Colony Optimization (ACO) to Solve the Problem

<!-- b000871 | prose | pages [22] -->
N =0, Set the maximum Step1: Parameter initialization, set the time t=0 and number of cycles

<!-- b000872 | prose | pages [22] -->
N

<!-- b000873 | prose | pages [22] -->
c

<!-- b000874 | prose | pages [22] -->
, put m ants in N locations, equalize pheromones on each path, number of cycles c max

<!-- b000875 | prose | pages [22] -->
= const . ij

<!-- b000876 | prose | pages [22] -->
Step2：Number of cycles plus 1.

<!-- b000877 | prose | pages [22] -->
Step3: Each individual ant chooses the next place to move forward according to the state transition probability formula.

<!-- b000878 | prose | pages [22] -->


<!-- b000879 | prose | pages [22] -->


<!-- b000880 | prose | pages [22] -->
 

<!-- b000881 | prose | pages [22] -->
[ ( )] [

<!-- b000882 | prose | pages [22] -->
t

<!-- b000883 | prose | pages [22] -->
( )]

<!-- b000884 | prose | pages [22] -->
t

<!-- b000885 | prose | pages [22] -->
ij ij

<!-- b000886 | prose | pages [22] -->


<!-- b000887 | prose | pages [22] -->


<!-- b000888 | prose | pages [22] -->


<!-- b000889 | prose | pages [22] -->


<!-- b000890 | prose | pages [22] -->
[

<!-- b000891 | prose | pages [22] -->
T t

<!-- b000892 | prose | pages [22] -->
( )] [

<!-- b000893 | prose | pages [22] -->
= 

<!-- b000894 | prose | pages [22] -->
k

<!-- b000895 | prose | pages [22] -->
p

<!-- b000896 | prose | pages [22] -->
( )

<!-- b000897 | prose | pages [22] -->
t

<!-- b000898 | furniture | pages [22] -->


<!-- b000899 | prose | pages [22] -->
is is ij

<!-- b000900 | prose | pages [22] -->


<!-- b000901 | prose | pages [22] -->
s J

<!-- b000902 | prose | pages [22] -->
( )

<!-- b000903 | prose | pages [22] -->
i

<!-- b000904 | prose | pages [22] -->


<!-- b000905 | prose | pages [22] -->
k

<!-- b000906 | prose | pages [22] -->


<!-- b000907 | prose | pages [22] -->
0

<!-- b000908 | prose | pages [22] -->
= − J ( ) i {1,2, n } In the above formula, k

<!-- b000909 | prose | pages [22] -->
 

<!-- b000910 | prose | pages [22] -->


<!-- b000911 | prose | pages [22] -->
,

<!-- b000912 | prose | pages [22] -->
j J

<!-- b000913 | prose | pages [22] -->
( )

<!-- b000914 | prose | pages [22] -->
i

<!-- b000915 | prose | pages [22] -->
k

<!-- b000916 | prose | pages [22] -->


<!-- b000917 | prose | pages [22] -->
( )]

<!-- b000918 | prose | pages [22] -->
t t

<!-- b000919 | furniture | pages [22] -->


<!-- b000920 | prose | pages [22] -->
(20)

<!-- b000921 | prose | pages [22] -->
,

<!-- b000922 | prose | pages [22] -->
otherwise

<!-- b000923 | prose | pages [22] -->
  represents the mesh points that ants are k k

<!-- b000924 | prose | pages [22] -->
 records the dots that ants have traveled through. allowed to select next, k ij t ( ) is a heuristic

<!-- b000925 | prose | pages [22] -->
factor, usually the reciprocal of the distance between grid point i and grid point j .

<!-- b000926 | prose | pages [22] -->
Step4: If not all N grid points have been traversed, then jump to Step2.

<!-- b000927 | prose | pages [22] -->
Step5: When all ants complete a tour, the pheromones on each path are updated according to the formula:

<!-- b000928 | prose | pages [22] -->


<!-- b000929 | prose | pages [22] -->
+ = −

<!-- b000930 | prose | pages [22] -->
(

<!-- b000931 | prose | pages [22] -->
t N

<!-- b000932 | prose | pages [22] -->
) (1

<!-- b000933 | prose | pages [22] -->
ij

<!-- b000934 | prose | pages [22] -->


<!-- b000935 | prose | pages [22] -->


<!-- b000936 | prose | pages [22] -->
( )

<!-- b000937 | prose | pages [22] -->
t

<!-- b000938 | furniture | pages [22] -->


<!-- b000939 | prose | pages [22] -->
ij

<!-- b000940 | prose | pages [22] -->
    (0 1)

<!-- b000941 | furniture | pages [22] -->


<!-- b000942 | furniture | pages [22] -->


<!-- b000943 | prose | pages [22] -->


<!-- b000944 | prose | pages [22] -->
+ 

<!-- b000945 | prose | pages [22] -->


<!-- b000946 | prose | pages [22] -->
) ( )

<!-- b000947 | prose | pages [22] -->
t

<!-- b000948 | prose | pages [22] -->
( )

<!-- b000949 | prose | pages [22] -->
t

<!-- b000950 | prose | pages [22] -->
ij ij

<!-- b000951 | prose | pages [22] -->
m

<!-- b000952 | prose | pages [22] -->
 = = 

<!-- b000953 | prose | pages [22] -->


<!-- b000954 | prose | pages [22] -->
k

<!-- b000955 | furniture | pages [22] -->


<!-- b000956 | prose | pages [22] -->
(21)

<!-- b000957 | prose | pages [22] -->
ij

<!-- b000958 | prose | pages [22] -->
=

<!-- b000959 | prose | pages [22] -->
k

<!-- b000960 | prose | pages [22] -->
1

<!-- b000961 | prose | pages [22] -->
represents the pheromone Volatilization Coefficient on In the above formula,   k k ant leaves on the path in an represents the pheromone quantity that the the path.

<!-- b000962 | prose | pages [22] -->
ij

<!-- b000963 | prose | pages [22] -->
iteration.

<!-- b000964 | prose | pages [22] -->


<!-- b000965 | prose | pages [22] -->
th

<!-- b000966 | prose | pages [22] -->
Q when the ant k passed by ij on this tour

<!-- b000967 | prose | pages [22] -->
,

<!-- b000968 | prose | pages [22] -->


<!-- b000969 | prose | pages [22] -->


<!-- b000970 | prose | pages [22] -->
= 

<!-- b000971 | prose | pages [22] -->
k

<!-- b000972 | prose | pages [22] -->
L

<!-- b000973 | prose | pages [22] -->
k ij

<!-- b000974 | prose | pages [22] -->


<!-- b000975 | prose | pages [22] -->
0,

<!-- b000976 | furniture | pages [22] -->


<!-- b000977 | prose | pages [22] -->
otherwise

<!-- b000978 | furniture | pages [23] -->


<!-- b000979 | furniture | pages [23] -->
Team # 1924588                                                                  Page 19 of 29

<!-- b000980 | prose | pages [23] -->
kL represents the length of the path that the

<!-- b000981 | prose | pages [23] -->
 N N Step6：If the number of cycles

<!-- b000982 | prose | pages [23] -->
k ant travels during this tour. th

<!-- b000983 | prose | pages [23] -->
, then the loop ends, otherwise jump to Step2. c c max

<!-- b000984 | heading | pages [23] -->
4.6.3 Result

<!-- b000985 | prose | pages [23] -->
For the B-type UAV in cargo container 1, the left side of the container can be reconnoitered simultaneously during delivery, so the UAV only needs to perform the reconnaissance task on the right side of the container. Using ACO algorithm, the optimal route selection in the maximum flight range of UAV is obtained as follows：

<!-- b000986 | prose | pages [23] -->
→ → → → → → → → (7,20) route 1:(4,19) (6,18) (7,19) (8,20) (7,25) (6,32) (6,26) (4,19)

<!-- b000987 | prose | pages [23] -->
For the D-type UAV in cargo container3, besides carrying medical packages, it can

<!-- b000988 | furniture | pages [23] -->


<!-- b000989 | furniture | pages [23] -->


<!-- b000990 | prose | pages [23] -->
reconnaissance at most twice a day. In order to get the maximum scope of reconnaissance, we get two optimal reconnaissance routes.：

<!-- b000991 | prose | pages [23] -->
→ → → → route 2:(15,89) (13,89) (12,88) (11,87)

<!-- b000992 | prose | pages [23] -->
→ → → → route 3:(15,89) (14,91) (14,92) (15,92)

<!-- b000993 | prose | pages [23] -->
→ → (12,87) (13,88) (15,89)

<!-- b000994 | furniture | pages [23] -->


<!-- b000995 | prose | pages [23] -->
→ (16,93) (15,89)

<!-- b000996 | furniture | pages [23] -->


<!-- b000997 | prose | pages [23] -->
For the C-type UAV in cargo container2, in order to reconnoiter more roads, it is necessary to reconnoiter in three directions by observing the road distribution grid. The three optimal paths are calculated as follows:：

<!-- b000998 | prose | pages [23] -->
→ → → → → → → → (9,61) route 4:(15,61) (10,61) (9,60) (8,60) → → → → route 5:(15,61) (11,58) (16,58) (16,59) → → → → route 6:(15,61) (10,54) 10,53 9,54 （ ）（ ） (10,62) (10,65) (11,66) (15,60)

<!-- b000999 | furniture | pages [23] -->


<!-- b001000 | prose | pages [23] -->
→ → → (20,59) (19,60) (17,60) (15,61) → → (8,55) (9,55) (15,61)

<!-- b001001 | furniture | pages [23] -->


<!-- b001002 | prose | pages [23] -->
All the optimal reconnaissance routes are shown in the grid coordinate system and on the map as shown in Figure 15.

<!-- b001003 | furniture | pages [23] -->


<!-- b001004 | caption | pages [23] -->
Figure 15 Optimal reconnaissance routes

<!-- b001005 | prose | pages [23] -->
At the same time, we give the overall schedule of UAV operation as shown in table 10.

<!-- b001006 | caption | pages [23] -->
Table 9 Schedule of UAV operation

<!-- b001007 | prose | pages [23] -->
Day2 Day1

<!-- b001008 | prose | pages [23] -->
time of

<!-- b001009 | prose | pages [23] -->
Day3

<!-- b001010 | prose | pages [23] -->
time of

<!-- b001011 | prose | pages [23] -->
time of

<!-- b001012 | prose | pages [23] -->
time of departure

<!-- b001013 | prose | pages [23] -->
time of departure

<!-- b001014 | prose | pages [23] -->
return

<!-- b001015 | prose | pages [23] -->
time of departure return

<!-- b001016 | prose | pages [23] -->
return

<!-- b001017 | furniture | pages [24] -->


<!-- b001018 | furniture | pages [24] -->
Team # 1924588                                                                  Page 20 of 29

<!-- b001019 | prose | pages [24] -->
F →Ⅰ 8:30 F →Ⅰ 8:30 F →Ⅰ 8:30 8: 41 8: 41 1 1

<!-- b001020 | prose | pages [24] -->
F →Ⅱ 8:30 8:58 2 F ⎯⎯⎯→ route 4 2

<!-- b001021 | prose | pages [24] -->
F →Ⅴ 8:30 9 : 02 3

<!-- b001022 | prose | pages [24] -->
F →Ⅲ12:30 12 :54

<!-- b001023 | prose | pages [24] -->
F ⎯⎯⎯→ route 1

<!-- b001024 | prose | pages [24] -->
2

<!-- b001025 | prose | pages [24] -->
3

<!-- b001026 | prose | pages [24] -->
F ⎯⎯⎯→ route 2

<!-- b001027 | prose | pages [24] -->
13: 01 F ⎯⎯⎯→ route 1 12:30

<!-- b001028 | prose | pages [24] -->
1

<!-- b001029 | prose | pages [24] -->
3

<!-- b001030 | prose | pages [24] -->
F ⎯⎯⎯→ route 5

<!-- b001031 | prose | pages [24] -->
12 : 40 F ⎯⎯⎯→ route 2 12:30

<!-- b001032 | prose | pages [24] -->
2

<!-- b001033 | prose | pages [24] -->
1

<!-- b001034 | prose | pages [24] -->
8: 41 1

<!-- b001035 | prose | pages [24] -->
F →Ⅱ 8:30 8:58 2

<!-- b001036 | prose | pages [24] -->
8:56 8:30

<!-- b001037 | prose | pages [24] -->
F →Ⅴ 8:30 9 : 02 3

<!-- b001038 | prose | pages [24] -->
F ⎯⎯⎯→ route 1 12:30

<!-- b001039 | prose | pages [24] -->
12:30 13: 01

<!-- b001040 | prose | pages [24] -->
13: 01 3

<!-- b001041 | prose | pages [24] -->
F ⎯⎯⎯→ route 2 12:30

<!-- b001042 | prose | pages [24] -->
12:30 12 : 40

<!-- b001043 | prose | pages [24] -->
12 : 40 1

<!-- b001044 | prose | pages [24] -->
F ⎯⎯⎯→ route 6 12:30

<!-- b001045 | prose | pages [24] -->
13:55 12:30

<!-- b001046 | prose | pages [24] -->
12 :57 2

<!-- b001047 | prose | pages [24] -->
F →Ⅳ 16:30 16 :57 F →Ⅳ16:30 16 :57 2 2

<!-- b001048 | prose | pages [24] -->
F ⎯⎯⎯→ route 3

<!-- b001049 | prose | pages [24] -->
16 : 43 F ⎯⎯⎯→ route 3 16:30

<!-- b001050 | prose | pages [24] -->
1

<!-- b001051 | prose | pages [24] -->
1

<!-- b001052 | prose | pages [24] -->
F →Ⅳ 16:30 16 :57 2

<!-- b001053 | prose | pages [24] -->
F ⎯⎯⎯→ route 3 16:30

<!-- b001054 | prose | pages [24] -->
16:30 16 : 43

<!-- b001055 | prose | pages [24] -->
16 : 43 1 (The UAV's fourth day schedule is the same as the first day, and the cycle is three days)

<!-- b001056 | heading | pages [24] -->
5  Testing Our Model

<!-- b001057 | prose | pages [24] -->
In question C, we designed the delivery route and reconnaissance route of drone successfully. Because question C adds consideration to the effect of obstacles on the basis of question B, we need to test the designed delivery routes and reconnaissance routes and judge whether the tasks performed along these routes will exceed the maximum flight distance of the drone. If not, the result of the model is perfect. Otherwise, the model needs to be modified.

<!-- b001058 | caption | pages [24] -->
Table 11 is the result of inspection of delivery routes and reconnaissance routes.

<!-- b001059 | caption | pages [24] -->
Table 10 The result of inspection of delivery routes and reconnaissance routes

<!-- b001060 | prose | pages [24] -->
The delivery distance of

<!-- b001061 | prose | pages [24] -->
Maximum flight

<!-- b001062 | prose | pages [24] -->
1F

<!-- b001063 | prose | pages [24] -->
1F distance of

<!-- b001064 | prose | pages [24] -->
11.7km 7.685km

<!-- b001065 | prose | pages [24] -->
The Reconnaissance

<!-- b001066 | prose | pages [24] -->
1F distance of

<!-- b001067 | prose | pages [24] -->
10.329km,11.518m

<!-- b001068 | prose | pages [24] -->
The delivery distance of

<!-- b001069 | prose | pages [24] -->
Maximum flight

<!-- b001070 | prose | pages [24] -->
F

<!-- b001071 | prose | pages [24] -->
F distance of

<!-- b001072 | prose | pages [24] -->
2

<!-- b001073 | prose | pages [24] -->
2

<!-- b001074 | prose | pages [24] -->
27.6km 25.616km,

<!-- b001075 | prose | pages [24] -->
The Reconnaissance

<!-- b001076 | prose | pages [24] -->
F distance of 2

<!-- b001077 | prose | pages [24] -->
26.449km,26.974m,27.070km 25.816km,27.331km

<!-- b001078 | prose | pages [24] -->
The delivery distance of

<!-- b001079 | prose | pages [24] -->
Maximum flight

<!-- b001080 | prose | pages [24] -->
F

<!-- b001081 | prose | pages [24] -->
F distance of

<!-- b001082 | prose | pages [24] -->
3

<!-- b001083 | prose | pages [24] -->
3

<!-- b001084 | prose | pages [24] -->
40.5km 40.473km

<!-- b001085 | prose | pages [24] -->
The Reconnaissance

<!-- b001086 | prose | pages [24] -->
F distance of 3

<!-- b001087 | prose | pages [24] -->
40.237km According to the results, all of the routes designed in question C meet the limit of maximum flight distance, which shows that the model established is reasonable.

<!-- b001088 | heading | pages [24] -->
6  Evaluation of Our Model

<!-- b001089 | heading | pages [24] -->
Strength

<!-- b001090 | prose | pages [24] -->
⚫ Through detailed analysis and reasonable simplification of the model, we created a new

<!-- b001091 | prose | pages [24] -->
three-dimensional packing method, which solves the packing problem of drone and

<!-- b001092 | furniture | pages [25] -->


<!-- b001093 | furniture | pages [25] -->
Team # 1924588                                                                  Page 21 of 29

<!-- b001094 | prose | pages [25] -->
medical packages in the cargo containers well and achieves satisfactory spatial utilization rate.

<!-- b001095 | prose | pages [25] -->
⚫ The longitude and latitude are meshed to get a new grid coordinate system, which

<!-- b001096 | prose | pages [25] -->
makes the road usage easy to be measured. And the calculation of question B and C is simplified.

<!-- b001097 | prose | pages [25] -->
⚫ Considering a lot of factors, such as flight distance, load limitation, obstacles and so on.

<!-- b001098 | prose | pages [25] -->
Therefore, we obtain a more realistic result.

<!-- b001099 | prose | pages [25] -->
⚫ Our model will save plenty of cost for HELP, Inc. realistically,

<!-- b001100 | heading | pages [25] -->
Weakness

<!-- b001101 | prose | pages [25] -->
⚫ In order to reduce the number of drones and save money, some roads cannot be

<!-- b001102 | prose | pages [25] -->
reconnoitred by drones.

<!-- b001103 | prose | pages [25] -->
⚫ Due to the time relation, the exact formula of the maximum flight distance when the

<!-- b001104 | prose | pages [25] -->
drone is loaded has not been solved

<!-- b001105 | furniture | pages [25] -->


<!-- b001106 | furniture | pages [25] -->


<!-- b001107 | furniture | pages [25] -->


<!-- b001108 | furniture | pages [25] -->


<!-- b001109 | furniture | pages [25] -->


<!-- b001110 | furniture | pages [25] -->


<!-- b001111 | furniture | pages [25] -->


<!-- b001112 | furniture | pages [25] -->


<!-- b001113 | furniture | pages [25] -->


<!-- b001114 | furniture | pages [25] -->


<!-- b001115 | furniture | pages [25] -->


<!-- b001116 | furniture | pages [25] -->


<!-- b001117 | furniture | pages [25] -->


<!-- b001118 | furniture | pages [25] -->


<!-- b001119 | furniture | pages [25] -->


<!-- b001120 | furniture | pages [25] -->


<!-- b001121 | furniture | pages [25] -->


<!-- b001122 | furniture | pages [25] -->


<!-- b001123 | furniture | pages [25] -->


<!-- b001124 | furniture | pages [25] -->


<!-- b001125 | furniture | pages [26] -->


<!-- b001126 | furniture | pages [26] -->
Team # 1924588                                                                  Page 22 of 29

<!-- b001127 | heading | pages [26] -->
References

<!-- b001128 | references | pages [26] -->
[1] Martello S, Pisinger D, Vigo D. The three-dimensional bin packing problem[J]. Operations Research,

<!-- b001129 | references | pages [26] -->
2000, 48(2): 256-267.

<!-- b001130 | references | pages [26] -->
[2] Falkenauer E. A hybrid grouping genetic algorithm for bin packing[J]. Journal of heuristics, 1996, 2(1):

<!-- b001131 | references | pages [26] -->
5-30..

<!-- b001132 | references | pages [26] -->
[3] Berkey J O, Wang P Y. Two-dimensional finite bin-packing algorithms[J]. Journal of the operational

<!-- b001133 | references | pages [26] -->
research society, 1987, 38(5): 423-429.

<!-- b001134 | references | pages [26] -->
[4] Kang K, Moon I, Wang H. A hybrid genetic algorithm with a new packing strategy for the three-

<!-- b001135 | references | pages [26] -->
dimensional bin packing problem[J]. Applied Mathematics and Computation, 2012, 219(3): 1287-1299.

<!-- b001136 | references | pages [26] -->
[5] Nicotra M M, Naldi R, Garone E. Nonlinear control of a tethered uav: The taut cable case[J]. Automatica,

<!-- b001137 | references | pages [26] -->
2017, 78: 174-184.

<!-- b001138 | references | pages [26] -->
[6] Portmann H. Unmanned aerial vehicle catcher: U.S. Patent 7,264,204[P]. 2007-9-4.

<!-- b001139 | references | pages [26] -->
[7] Duan H, Li P. Uav path planning[M]//Bio-inspired Computation in Unmanned Aerial Vehicles.

<!-- b001140 | references | pages [26] -->
Springer, Berlin, Heidelberg, 2014: 99-142.

<!-- b001141 | references | pages [26] -->
[8] Wan Y, Liu J, Tsai P C. The assignment of storage locations to containers for a container stack[J]. Naval

<!-- b001142 | references | pages [26] -->
Research Logistics (NRL), 2009, 56(8): 699-713.

<!-- b001143 | furniture | pages [26] -->


<!-- b001144 | furniture | pages [26] -->


<!-- b001145 | furniture | pages [26] -->


<!-- b001146 | furniture | pages [26] -->


<!-- b001147 | furniture | pages [26] -->


<!-- b001148 | furniture | pages [26] -->


<!-- b001149 | furniture | pages [26] -->


<!-- b001150 | furniture | pages [26] -->


<!-- b001151 | furniture | pages [26] -->


<!-- b001152 | furniture | pages [26] -->


<!-- b001153 | furniture | pages [26] -->


<!-- b001154 | furniture | pages [26] -->


<!-- b001155 | furniture | pages [26] -->


<!-- b001156 | furniture | pages [26] -->


<!-- b001157 | furniture | pages [26] -->


<!-- b001158 | furniture | pages [26] -->


<!-- b001159 | furniture | pages [26] -->


<!-- b001160 | furniture | pages [26] -->


<!-- b001161 | furniture | pages [27] -->


<!-- b001162 | furniture | pages [27] -->
Team # 1924588                                                                  Page 23 of 29

<!-- b001163 | heading | pages [27] -->
Appendix

<!-- b001164 | prose | pages [27] -->
⚫ Establishment of grid coordinate system

<!-- b001165 | prose | pages [27] -->
grid.m clear p= imread('The path.jpg'); m=p(:,:,2); rows=size(m,1); column=size(m,2); for n=1:rows for k=1:column if m(n,k)>=200 m(n,k)=255; end end end precision=5; for i=1:fix(rows/precision) m(i*precision,:)=0; end for j=1:fix(column/precision) m(:,precision*j)=0; end M=[]; Q=0; T=zeros(fix(rows/precision),fix(column/precision)); for i=1:fix(rows/precision) for j=1:fix(column/precision) k=sum(m(((i-1)*precision+1):i*precision,((j-1)*precision+1):j*precision)); k=sum(k,2); M=[M k]; if k<(precision-1)*(precision-1.5)*255 m(((i-1)*precision+1):i*precision,((j-1)*precision+1):j*precision)=0; Q=Q+1; T(i,j)=1; end end end imshow(m);

<!-- b001166 | furniture | pages [27] -->


<!-- b001167 | prose | pages [27] -->
⚫ Three-dimensional packing

<!-- b001168 | prose | pages [27] -->
packing.m clear,clc BOX=[231,92,94];%ISO container internal dimensions L × W × H MED1=[14 7 5];%Medical Packagedimensionsl×w ×h

<!-- b001169 | furniture | pages [28] -->


<!-- b001170 | furniture | pages [28] -->
Team # 1924588                                                                  Page 24 of 29

<!-- b001171 | prose | pages [28] -->
%BOX_L Maximum capacity l_max=fix(BOX(1)/MED1(1)); w_max=fix(BOX(1)/MED1(2)); M=[]; fori=0:l_max% I=fix(BOX(2)/MED1(2));%BOX_WCorresponding capacity II=mod(BOX(2),MED1(2));% Remaining length j=fix((BOX(1)-i*MED1(1))/MED1(2)); J=fix(BOX(2)/MED1(1)); JJ=mod(BOX(2),MED1(1)); remain=BOX(1)-i*MED1(1)-j*MED1(2); M=[M;i,I,II,j,J,JJ,remain,i*I+j*J]; end [value,index]=max(M(:,end)); M(index,end)

<!-- b001172 | furniture | pages [28] -->


<!-- b001173 | furniture | pages [28] -->


<!-- b001174 | prose | pages [28] -->
⚫ The Optimum Location of Containers

<!-- b001175 | prose | pages [28] -->
cargo.m clc clear T=xlsread('T.xlsx') S=113.990; n=91; Save=S/n; Sd=39.5/2; r=Sd/Save; re=[]; maxsum=0; suum=[]; for i=3:1:15 for j=3:30 if sqrt((4-i)^2+(4-j)^2)>r continue else ymin=max(1,ceil(i-r)); ymax=min(30,floor(i+r)); xmin=max(1,ceil(j-r)); xmax=min(97,floor(j+r)); sum=0; for p=ymin:ymax for q=xmin:xmax sum=sum+T(p,q); end end suum=[suum sum]; if sum>=maxsum

<!-- b001176 | furniture | pages [29] -->


<!-- b001177 | furniture | pages [29] -->
Team # 1924588                                                                  Page 25 of 29

<!-- b001178 | prose | pages [29] -->
maxsum=sum; re=[i,j,sum] end

<!-- b001179 | furniture | pages [29] -->


<!-- b001180 | prose | pages [29] -->
end end end

<!-- b001181 | furniture | pages [29] -->


<!-- b001182 | prose | pages [29] -->
⚫ The generation of Voronio diagrams

<!-- b001183 | prose | pages [29] -->
Vd.m a=[ 12,52 4,50 8,48 21,49 11,57 11,60 19,54 21,54 20,56 23,62] x=[52 50 48 49 57 60 54 54 56 62] y=[12 4 8 21 11 11 19 21 20 23] voronoi(x,y) hold on plot(61,15,'-xr',61,25,'-*k',57,6,'-*k',51,11,'-*k') legend('Obstacles','Safest route','Starting point','Destination') ylabel('The abscissa of the grid') xlabel('The ordinate of the grid') set(gca,'XAxisLocation','top'); set(gca,'YDir','reverse');

<!-- b001184 | furniture | pages [29] -->


<!-- b001185 | prose | pages [29] -->
⚫ ant colony optimization

<!-- b001186 | prose | pages [29] -->
Q4.m function [R_best,L_best,L_ave,Shortest_Route,Shortest_Length]=Q4(C,NC_max,m,Alpha,Beta,Rho,Q)

<!-- b001187 | furniture | pages [29] -->


<!-- b001188 | prose | pages [29] -->
n=size(C,1); D=zeros(n,n); for i=1:n for j=1:n if i~=j D(i,j)=((C(i,1)-C(j,1))^2+(C(i,2)-C(j,2))^2)^0.5; else D(i,j)=eps; end D(j,i)=D(i,j); end end

<!-- b001189 | furniture | pages [29] -->


<!-- b001190 | furniture | pages [30] -->


<!-- b001191 | furniture | pages [30] -->
Team # 1924588                                                                  Page 26 of 29

<!-- b001192 | furniture | pages [30] -->


<!-- b001193 | prose | pages [30] -->
Eta=1./D; Tau=ones(n,n);     Tabu=zeros(m,n); NC=1; R_best=zeros(NC_max,n); L_best=inf.*ones(NC_max,1); L_ave=zeros(NC_max,1);

<!-- b001194 | furniture | pages [30] -->


<!-- b001195 | furniture | pages [30] -->


<!-- b001196 | prose | pages [30] -->
while NC<=NC_max Randpos=[]; for i=1:(ceil(m/n)) Randpos=[Randpos,randperm(n)]; end Tabu(:,1)=(Randpos(1,1:m))';

<!-- b001197 | furniture | pages [30] -->


<!-- b001198 | furniture | pages [30] -->


<!-- b001199 | furniture | pages [30] -->


<!-- b001200 | prose | pages [30] -->
for j=2:n for i=1:m visited=Tabu(i,1:(j-1)); J=zeros(1,(n-j+1)); P=J; Jc=1; for k=1:n if length(find(visited==k))==0 J(Jc)=k; Jc=Jc+1; end end

<!-- b001201 | furniture | pages [30] -->


<!-- b001202 | furniture | pages [30] -->


<!-- b001203 | furniture | pages [30] -->


<!-- b001204 | furniture | pages [30] -->


<!-- b001205 | furniture | pages [30] -->


<!-- b001206 | prose | pages [30] -->
for k=1:length(J) P(k)=(Tau(visited(end),J(k))^Alpha)*(Eta(visited(end),J(k))^Beta);

<!-- b001207 | furniture | pages [30] -->


<!-- b001208 | prose | pages [30] -->
end P=P/(sum(P)); Pcum=cumsum(P); Select=find(Pcum>=rand); to_visit=J(Select(1)); Tabu(i,j)=to_visit; end end

<!-- b001209 | furniture | pages [30] -->


<!-- b001210 | furniture | pages [30] -->


<!-- b001211 | furniture | pages [31] -->


<!-- b001212 | furniture | pages [31] -->
Team # 1924588                                                                  Page 27 of 29

<!-- b001213 | furniture | pages [31] -->


<!-- b001214 | prose | pages [31] -->
if NC>=2 Tabu(1,:)=R_best(NC-1,:); end

<!-- b001215 | furniture | pages [31] -->


<!-- b001216 | furniture | pages [31] -->


<!-- b001217 | prose | pages [31] -->
L=zeros(m,1); for i=1:m R=Tabu(i,:); for j=1:(n-1) L(i)=L(i)+D(R(j),R(j+1)); end L(i)=L(i)+D(R(1),R(n)); end

<!-- b001218 | furniture | pages [31] -->


<!-- b001219 | furniture | pages [31] -->


<!-- b001220 | furniture | pages [31] -->


<!-- b001221 | furniture | pages [31] -->


<!-- b001222 | furniture | pages [31] -->


<!-- b001223 | prose | pages [31] -->
L_best(NC)=min(L);        pos=find(L==L_best(NC)); R_best(NC,:)=Tabu(pos(1),:); L_ave(NC)=mean(L); NC=NC+1

<!-- b001224 | furniture | pages [31] -->


<!-- b001225 | furniture | pages [31] -->


<!-- b001226 | furniture | pages [31] -->


<!-- b001227 | furniture | pages [31] -->


<!-- b001228 | prose | pages [31] -->
Delta_Tau=zeros(n,n); for i=1:m for j=1:(n-1) Delta_Tau(Tabu(i,j),Tabu(i,j+1))=Delta_Tau(Tabu(i,j),Tabu(i,j+1))+Q/L(i); end Delta_Tau(Tabu(i,n),Tabu(i,1))=Delta_Tau(Tabu(i,n),Tabu(i,1))+Q/L(i); end Tau=(1-Rho).*Tau+Delta_Tau; Tabu=zeros(m,n); end

<!-- b001229 | furniture | pages [31] -->


<!-- b001230 | prose | pages [31] -->
Pos=find(L_best==min(L_best)); Shortest_Route=R_best(Pos(1),:) Shortest_Length=L_best(Pos(1)) figure(1) DrawRoute(C,Shortest_Route) figure(2) plot(L_best) title('The shortest distance')

<!-- b001231 | furniture | pages [31] -->


<!-- b001232 | furniture | pages [31] -->


<!-- b001233 | furniture | pages [32] -->


<!-- b001234 | furniture | pages [32] -->
Team # 1924588                                                                  Page 28 of 29

<!-- b001235 | prose | pages [32] -->
function DrawRoute(C,R)

<!-- b001236 | furniture | pages [32] -->


<!-- b001237 | prose | pages [32] -->
N=length(R); scatter(C(:,1),C(:,2)); hold on plot([C(R(1),1),C(R(N),1)],[C(R(1),2),C(R(N),2)],'r') hold on for ii=2:N plot([C(R(ii-1),1),C(R(ii),1)],[C(R(ii-1),2),C(R(ii),2)],'r') hold on end hold on plot(C(1,1),C(1,2),'-*k') ylabel('The abscissa of the grid') xlabel('The ordinate of the grid') set(gca,'XAxisLocation','top'); set(gca,'YDir','reverse'); title('Optimization results of drone detection path ')

<!-- b001238 | furniture | pages [32] -->


<!-- b001239 | furniture | pages [32] -->


<!-- b001240 | prose | pages [32] -->
⚫ Packing ISO cargo containers

<!-- b001241 | prose | pages [32] -->
ISO.m clear,clc BOX=[231,92,94];% ISO container internal dimensions L × W × H MED1=[14 7 5];% Medical Package dimensions l×w ×h % BOX_L Maximum capacity l_max=fix(BOX(1)/MED1(1)); w_max=fix(BOX(1)/MED1(2)); M=[]; for i=0:l_max% I=fix(BOX(2)/MED1(2));% BOX_W Corresponding capacity II=mod(BOX(2),MED1(2)); % Remaining length j=fix((BOX(1)-i*MED1(1))/MED1(2)); J=fix(BOX(2)/MED1(1)); JJ=mod(BOX(2),MED1(1)); remain=BOX(1)-i*MED1(1)-j*MED1(2); M=[M;i,I,II,j,J,JJ,remain,i*I+j*J]; end [value,index]=max(M(:,end)); M(index,end) %% BOX_W Maximum capacity % l_max=fix(BOX(2)/MED1(1)); % w_max=fix(BOX(2)/MED1(2)); % M=[]; % for i=0:l_max%l 的个数 %   I=fix(BOX(1)/MED1(2)); % BOX_L Corresponding capacity %     j=fix((BOX(2)-i*MED1(1))/MED1(2));

<!-- b001242 | furniture | pages [33] -->


<!-- b001243 | furniture | pages [33] -->
Team # 1924588                                                                  Page 29 of 29

<!-- b001244 | prose | pages [33] -->
%     J=fix(BOX(1)/MED1(1)); %     remain=BOX(2)-i*MED1(1)-j*MED1(2); %     M=[M;i,j,remain,i*I+j*J]; % end % [value,index]=max(M(:,4)); % M(index,end)

<!-- b001245 | furniture | pages [33] -->


<!-- b001246 | furniture | pages [33] -->

