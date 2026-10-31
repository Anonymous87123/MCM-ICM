# P-B-2019-1915782-41065334

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
For office use only For office use only 1915782 T1 ________________ F1 ________________ T2 ________________ F2 ________________ Problem Chosen T3 ________________ F3 ________________

<!-- b000003 | front_matter | pages [1] -->
B

<!-- b000004 | front_matter | pages [1] -->
T4 ________________ F4 ________________

<!-- b000005 | prose | pages [1] -->
2019 MCM/ICM

<!-- b000006 | title | pages [1] -->
Messengers of Hope

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
In 2017, the hurricane disaster brought many casualties and substantial economic and property losses to Puerto Rico. We help the NGO HELP, Inc. design a mobile disaster response system that uses drones to transport medical packages to selected areas and to take video reconnaissance of roads in disaster areas.

<!-- b000009 | prose | pages [1] -->
Containers are used to load the system to the disaster area. For the loading problem, the configuration problem of packages in containers is simplified into the combinatorial optimization problem of three-dimensional packing and the optimal configuration problem of medical packages and shipping containers. In this paper, the goal is the maximum space utilization rate of the ISO container, and the constraints in the loading process are as follows: in order to maintain the stability of the contents, each about to be loaded item must be fully supported; In order to facilitate loading and unloading, each item can be entirely separated by vertical or horizontal plane; The ratio of the 3 medical packages is certain. We establish a single objective programming model and use the improved 3D-RSO algorithm to solve the model.

<!-- b000010 | prose | pages [1] -->
Aiming at the location problem, this paper establishes a two-objective programming model aiming at achieving the shortest transportation time and the longest total reconnaissance road to determine the number and location of ISO containers. By analysis and calculation, it is found that under the condition of meeting the daily demand of five hospitals, at least 3 containers are needed to supply medical packages.

<!-- b000011 | prose | pages [1] -->
For the medical supply delivery and video reconnaissance, the specific quantity of drones is determined firstly, and then the loading model is used to determine the assembly scheme of the ISO container. Then the route and schedule of the drone transport medical package are calculated by traversal calculation of all roads. Finally, the transportation plan and the length of roads that can be detected are given.

<!-- b000012 | prose | pages [1] -->
The optimal geographical location distribution (in latitude and longitude coordinates) of the ISO container is calculated as follows: container 1 at (18.3805,-66.5109), container 2 at (18.3490,-66.2830), and container 3 at (18.2191,-65.8241).And we give the detailed daily transportation plan. The daily medical supply delivery can be completed in 38.7124min. The total length of the road that can be detected is 722.38km. The daily video reconnaissance can be completed in 12h. It is calculated that the specific assembly scheme of ISO container is that container 1 contains 53 drones B, 1 Tether H, 700 MED1, 350 MED2, and 350 MED3, and the space utilization rate is 89.10%. Container 2 contains 54 drones B, 1 Tether H, 684 MED1, 342 MED2, and 342 MED3, and the space utilization rate is 89.48%. Container 3 contains 53 drones B, 1 Tether H, 809 MED1, 0 MED2, and 539 MED3, and the space utilization rate is 91.45%.

<!-- b000013 | prose | pages [1] -->
Finally, the sensitivity analysis and extension of the model are given.

<!-- b000014 | keywords | pages [1] -->
Keyword: Drone; The location problem; The loading problem; Emergency rescue

<!-- b000015 | heading | pages [2] -->
MEMORANDUM

<!-- b000016 | prose | pages [2] -->
To: CEO of HELP, Inc.

<!-- b000017 | prose | pages [2] -->
From: Team 1915782

<!-- b000018 | prose | pages [2] -->
Subject: A DroneGo disaster response system

<!-- b000019 | prose | pages [2] -->
Date: Monday, January 28, 2019

<!-- b000020 | prose | pages [2] -->
We know that HELP, Inc. is trying to design the ’DroneGo’ system to improve the ability to respond to natural disasters. Therefore, we established the mathematical model and solved the sit- uation that the drone needs to complete the medical supply mission and the video reconnaissance mission. It is a great honor to present our results to you.

<!-- b000021 | prose | pages [2] -->
It is recommended to use three ISO standard containers to load the required items. The calcu- lation shows that one or two containers are not sufﬁcient for medical supply missions and video reconnaissance missions.

<!-- b000022 | prose | pages [2] -->
The loading conditions of the three containers are different. In container 1, there are 53 type B drones for transport and reconnaissance, one type H drones for the signal repeater, 700 MED1, 350 MED2, and 350 MED3, which is enough to support the medical package demand for 350 days.Container 2 contains 54 type B drones, 1 type H drones, 684 MED1 drones, 342 MED2 drones and 342 MED3 drones, which is enough to support the medical package demand for 342 days. Container 3 contains 3 type B drones, 1 type H drones, 809 MED1, and 539 MED3, which is enough to support the medical package demand for 269 days. All three containers have a space utilization rate of around 90%, so they save a lot of buffer materials.

<!-- b000023 | prose | pages [2] -->
Upon completion of loading of container, it is suggested that the container 1 transport through the Port of Arecibo or Antonio (Nery) Juarbe Pol Airport transportation to Puerto Rico, after sending it through the local vehicle (66.5109,18.3805). The container 2 transport by the Port of San Juan or Fernando Ribas Dominicci Airport transportation to Puerto Rico, after sending it through the local vehicle (66.2830,18.3490). Container 3 transport through the Port of Ceiba or Jos´e Aponte DE la Torre Airport transportation to Puerto Rico, after sending it through the local vehicle (65.8241,18.2191).

<!-- b000024 | prose | pages [2] -->
Each drone has the same daily schedule for missions. To simplify the presentation, ﬁgure 1 is used to present the daily transportation plan of scheme 1. It is worth mentioning that all the drones can complete the task in 38.7 minutes.

<!-- b000025 | prose | pages [3] -->
Since the situation in the disaster area is changing rapidly, the drones need to perform the same reconnaissance missions every day. Each container has a similar reconnaissance mission. Make 20 drone B ﬂy at 300m altitudes, using the 74 degree wide-angle lens, respectively in different directions of ﬂying straight spying for 20 minutes, and returned along with a straight line. It just can complete 20 degree range of reconnaissance. Charge and maintain the returning drone, and send another 20 type B drones in a non-repeated direction. Working in shifts like this, all reconnaissance missions can be completed in 12 hours, without the danger of having the drone work at night. Also, there are a total of 30 spare drones B to replace the damaged ones. Based on this scheme, the drone unit of container 1 can detect the road of 313km, the drone unit of container 2 can detect the road of 362km, and the drone unit of container 3 can detect the road of 252km. Excluding duplicate roads, this covers 43.5% of the island’s roads.

<!-- b000026 | prose | pages [3] -->
If you think more attention should be paid to video reconnaissance to rebuild the disaster area, rather than strengthening the prevention of secondary disasters. We also have a slightly different set of plans in place.

<!-- b000027 | prose | pages [3] -->
In this scenario, container 1 contains 68 type B drones, 1 type H drones, and 630 MED1 drones, which is enough to support 630 days of medical bag demand. Container 2 contains 68 type B drones, 1 type H drones, 321 MED1, 212 MED2, 213 MED3, which is enough to support the de- mand for medical packages for 106 days. In container 3, there are 68 type B drones, 1 type H drones, 396 MED1 drones and 263 MED3 drones, which is enough to support the medical pack- age demand for 131 days. More drones are being loaded to speed up the reconnaissance.

<!-- b000028 | caption | pages [3] -->
Figure 2 is the daily transportation plan of scheme 2.

<!-- b000029 | prose | pages [3] -->
At this point, the container 1 should be at (18.2948, 66.7748), container 2 should be at (18.2705, 18.2705), container 3 should be in (18.2419,65.8781). And container 1 no longer ships medical packages to container 2. All unoccupied drones should be used for reconnaissance to improve efﬁciency.

<!-- b000030 | prose | pages [3] -->
Under this scheme, the unmanned unit of container 1 can detect the road of 352km, the un- manned unit of container 2 can detect the road of 470km, and the unmanned unit of container 3 can detect the road of 319km. Excluding duplicated roads, this covered 60.4% of the island’s roads.

<!-- b000031 | prose | pages [3] -->
You can choose between option 1, which focuses on the prevention of secondary disasters, and option 2, which focuses on video reconnaissance, which is more efﬁcient. It is worth noting that either option is excellent for both medical supply and video reconnaissance missions. We hope our efforts can be of help to you. Thank you very much for the opportunity to show us.

<!-- b000032 | prose | pages [3] -->
2 Bae

<!-- b000033 | furniture | pages [4] -->
Team # 1915782

<!-- b000034 | furniture | pages [4] -->
Page 1 of 20

<!-- b000035 | heading | pages [4] -->
Contents

<!-- b000036 | contents | pages [4] -->
1 Introduction. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [4] -->
2

<!-- b000038 | contents | pages [4] -->
1.1

<!-- b000039 | contents | pages [4] -->
Background

<!-- b000040 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [4] -->
2

<!-- b000042 | contents | pages [4] -->
1.2

<!-- b000043 | contents | pages [4] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [4] -->
2

<!-- b000045 | contents | pages [4] -->
2 Analysis of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [4] -->
2

<!-- b000047 | contents | pages [4] -->
3 Symbols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [4] -->
3

<!-- b000049 | contents | pages [4] -->
4 Simplifying Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [4] -->
4

<!-- b000051 | contents | pages [4] -->
5 Data Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [4] -->
4

<!-- b000053 | contents | pages [4] -->
6 Model and Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [4] -->
5

<!-- b000055 | contents | pages [4] -->
6.1

<!-- b000056 | contents | pages [4] -->
Three-dimensional Loading Model . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [4] -->
5

<!-- b000058 | contents | pages [4] -->
6.1.1

<!-- b000059 | contents | pages [4] -->
The Algorithm of the Loading Model

<!-- b000060 | contents | pages [4] -->
. . . . . . . . . . . . .

<!-- b000061 | contents | pages [4] -->
7

<!-- b000062 | contents | pages [4] -->
6.2

<!-- b000063 | contents | pages [4] -->
Container’s Location and Reconnaissance of Road Networks . . . .

<!-- b000064 | contents | pages [4] -->
9

<!-- b000065 | contents | pages [4] -->
6.2.1

<!-- b000066 | contents | pages [4] -->
Determine the Number of Cargo Containers . . . . . . . . .

<!-- b000067 | contents | pages [4] -->
9

<!-- b000068 | contents | pages [4] -->
6.2.2

<!-- b000069 | contents | pages [4] -->
Drone Transport Model

<!-- b000070 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [4] -->
10

<!-- b000072 | contents | pages [4] -->
6.2.3

<!-- b000073 | contents | pages [4] -->
Reconnaissance Model . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [4] -->
12

<!-- b000075 | contents | pages [4] -->
6.2.4

<!-- b000076 | contents | pages [4] -->
Location Model . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [4] -->
12

<!-- b000078 | contents | pages [4] -->
6.2.5

<!-- b000079 | contents | pages [4] -->
The Algorithm of the Location Model . . . . . . . . . . . . .

<!-- b000080 | contents | pages [4] -->
12

<!-- b000081 | contents | pages [4] -->
6.3

<!-- b000082 | contents | pages [4] -->
The Flight Plan

<!-- b000083 | contents | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [4] -->
13

<!-- b000085 | contents | pages [4] -->
6.4

<!-- b000086 | contents | pages [4] -->
Solution of Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [4] -->
14

<!-- b000088 | contents | pages [4] -->
7 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [4] -->
16

<!-- b000090 | contents | pages [4] -->
8 Model Extension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [4] -->
17

<!-- b000092 | contents | pages [4] -->
9 Strengths and Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [4] -->
19

<!-- b000094 | contents | pages [4] -->
9.1

<!-- b000095 | contents | pages [4] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [4] -->
19

<!-- b000097 | contents | pages [4] -->
9.2

<!-- b000098 | contents | pages [4] -->
Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [4] -->
19

<!-- b000100 | contents | pages [4] -->
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000101 | contents | pages [4] -->
20

<!-- b000102 | furniture | pages [5] -->
Team # 1915782

<!-- b000103 | furniture | pages [5] -->
Page 2 of 20

<!-- b000104 | heading | pages [5] -->
1 Introduction

<!-- b000105 | heading | pages [5] -->
1.1 Background

<!-- b000106 | prose | pages [5] -->
The U.S. territory of Puerto Rico was hit by the worst hurricane in 2017, wreaking havoc on the island and killing more than 2,900 people. The hurri- cane caused widespread damage in Puerto Rico, damaging about 80 percent of Puerto Rico’s utility poles and all transmission lines, so much so that the entire island lost power. The storm also damaged much of the island’s cellular com- munications network, trapping 3 to 4 million residents for months. As time went on, hospitals and NGOs were running short of lifesaving equipment and medical supplies. HELP, Inc., an NGO, is trying to use a transportable disaster response system called ’DroneGo’ to deliver medical supplies and high-resolution aeri- al video reconnaissance to disaster areas. It is necessary to design a reasonable mobile disaster response system.

<!-- b000107 | heading | pages [5] -->
1.2 Restatement of the Problem

<!-- b000108 | prose | pages [5] -->
Consider the background information, the requirements identiﬁed in the prob- lem statement, and the information provided in the problem attachment to ad- dress the following issues:

<!-- b000109 | prose | pages [5] -->
1. A ﬂeet of drones and a set of medical packages are recommended for HELP, Inc. DroneGo disaster response system, which will meet the requirements of Puerto Rico hurricane scenario. Design packaging conﬁgurations for up to three ISO cargo containers to ship the system to Puerto Rico.

<!-- b000110 | prose | pages [5] -->
2. Determine the best location or location in Puerto Rico to place one, two, or three containers of the DroneGo disaster response system so it can perform medical supply delivery and video reconnaissance of the road network.

<!-- b000111 | prose | pages [5] -->
3. For each type of drone included in a drone formation:

<!-- b000112 | prose | pages [5] -->
(a) Provide drone payload packaging conﬁgurations (that is, medical pack- ages packed into the drone cargo bay), delivery routes and schedules to meet the emergency medical package requirements identiﬁed in the Puerto Rico hurricane scenario.

<!-- b000113 | prose | pages [5] -->
(b) Provide a drone ﬂight plan that enables the drone ﬂeet to use onboard cameras to evaluate major highways and highways to help support the company’s mission.

<!-- b000114 | heading | pages [5] -->
2 Analysis of the Problem

<!-- b000115 | prose | pages [5] -->
Developing the DroneGo disaster response system for hurricane-ravaged Puer- to Rico can be divided into three sub-problems:

<!-- b000116 | prose | pages [5] -->
Problem 1 :Optimal loading of ISO container is a must. According to the speciﬁc dimensions of drones, medical packages and ISO containers given in the attachment, the reasonable assembly mode of ISO container is determined. Our main goal is to make ISO containers not only more space-efﬁcient but also easier to load and unload by placing the contents properly.

<!-- b000117 | furniture | pages [6] -->
Team # 1915782

<!-- b000118 | furniture | pages [6] -->
Page 3 of 20

<!-- b000119 | prose | pages [6] -->
Problem 2 :The determination of the number and location of ISO containers is the key to the whole problem, which requires to analysis of the geographical location of 5 hospitals and the performance of each drone. In order to carry out feasible rescue work in disaster areas in a timely manner, the shortest time for drones to complete the transport of medical packages and the longest reconnais- sance road length should be taken into account to determine the number of ISO containers and the optimal geographical location of each ISO container.

<!-- b000120 | prose | pages [6] -->
Considering subproblems 1 and 2, when the number of containers and the optimal geographical locations are determined, 5 hospitals should be assigned to different ISO containers. Considering the differences in the types and quan- tities of medical packages required by different hospitals, the speciﬁc assembly scheme of each ISO container was determined. Problem 3 :When the ISO container’s location and assembly scheme is deter- mined, determine the route and schedule of the drone medical package delivery. Then provide the best way for drones to monitor the roads, and ﬁnd all the roads that can be reconnaissanced and calculate their total length.

<!-- b000121 | heading | pages [6] -->
3 Symbols

<!-- b000122 | prose | pages [6, 7] -->
Deﬁnitions Descriptions a Longtitude b Latitude q Angle between two places and the center of the earth The straight distance between two place Dis Radius of the earth Rearth A rectangular container C The length of container C L The width of container C W The height of container C H A set of different kinds of boxes B Type index variable i The ith type of box bi The length of the ith box li The width of the ith box wi The height of the ith box hi Whether the ith box can be assembled and placed around r A set of the number of each kind of box Q The number of layers of boxes in a container f The position occupied by the kth box, which is called region k S( f,k) The top area of the kth box A(f,k) The total bottom area of the boxes stacked on the f-layer k region The number of ith type of box qi Deﬁnitions Descriptions q( f,k) The number of the ith type of box located on the f-layer in the k region i The set of all boxes that have been put into container C F The total volume of all boxes that have been put into container C VF The number of Cargo Containers,n = 1,2,3 n The serial number of Cargo Container,d = 1,..,n d The location of the dth Cargo Container Cd Hospital index variable,j=1,2,...,5 j The location of the jth hospital D j µ The ratio of the actual drone’s ﬂight time to the ﬂight time without load N(i1) The dth container contains the number of type i1 medical packages d N(i1) The number of type i1 packages required for the j hospital j N(i2) The dth container contains the number of type i2 drone d N(i2) The number of type i2 drone to the j hospital j N(i2,i1) The number of type i1 medical packages carried by type i2 drone V (i1) The volume of type i1 medical packages G(i1) The weight of type i1 medical packages V (i2) The limited volume of type i2 drone G(i2) The limited weight of type i2 drone t(i2) The no-load limit ﬂight time of type i2 drone v(i2) The ﬂight speed of type i2 drone L(i2) The no-load limit ﬂight distance of type i2 drone x(i2) Whether the number of i2 drone from the dth container to the j hospital d j

<!-- b000123 | furniture | pages [7] -->
Team # 1915782

<!-- b000124 | furniture | pages [7] -->
Page 4 of 20

<!-- b000126 | heading | pages [7] -->
4 Simplifying Assumptions

<!-- b000127 | prose | pages [7] -->
1. It is assumed that the ﬂight time of the drone will decrease due to the weight of medical package, and it is linearly related to the weight.

<!-- b000128 | prose | pages [7] -->
2. Ignore the effects of wind, weather on drone ﬂight and road conditions.

<!-- b000129 | prose | pages [7] -->
3. ISO container should be located close to a city or highway or road.

<!-- b000130 | prose | pages [7] -->
4. The drone must be recharged at the location of an ISO container.

<!-- b000131 | prose | pages [7] -->
5. Containers can only be transported to Puerto Rico via an airport or port.

<!-- b000132 | prose | pages [7] -->
6. Same medical supply delivery mission and video reconnaissance mission should be completed daily.

<!-- b000133 | heading | pages [7] -->
5 Data Processing

<!-- b000134 | prose | pages [7, 8] -->
Calculate the distance between any two places on the earth according to the longitude and latitude coordinates[2].We know that (a1,b1) is the longitude and latitude coordinates of place 1, and (a2,b2) is the longitude and latitude coordi- nates of place 2.The Angle between them and the center of the earth is q.

<!-- b000135 | furniture | pages [8] -->
Team # 1915782

<!-- b000136 | furniture | pages [8] -->
Page 5 of 20

<!-- b000138 | prose | pages [8] -->
q = arccos[cos(90−a1)·cos(90−a2) (1) +sin(90−a1)·sin(90−a2)·cos(b1 −b2)] Then, the distance between the two places can be calculated by using the arc length formula.

<!-- b000139 | prose | pages [8] -->
Dis = p · q (2) 180 ·Rearth

<!-- b000140 | heading | pages [8] -->
6 Model and Solution

<!-- b000141 | prose | pages [8] -->
First of all, the number of containers must be determined. Then in the case of comprehensive consideration of drone transport model and reconnaissance model, the speciﬁc location of the container and the loading data are determined by location model. Finally, the packing scheme is obtained by three-dimensional loading model calculation.

<!-- b000142 | caption | pages [8] -->
Figure 1: Thinking process chart

<!-- b000143 | heading | pages [8] -->
6.1 Three-dimensional Loading Model

<!-- b000144 | prose | pages [8, 9] -->
Loading as many shipping container and emergency medical packages as possible in a cargo container is a typical three-dimensional packing problem as well as an optimization combination problem. In this study, three-dimensional Knapsack Loading Problems (referred to as 3D-KIP) with the value of volume were studied, that is, a group of small cuboids of different sizes (shipping con- tainer and emergency medical packages) were put into a large cuboid (cargo con- tainer) of a given size, aiming to maximize the total volume of all small cuboids that were put in[2].(See Figure 2) Given a rectangular container C and a set B of boxes. The length, width and height of container C are expressed as L , W and H respectively, as shown in the formula (3) [2]:

<!-- b000145 | furniture | pages [9] -->
Team # 1915782

<!-- b000146 | furniture | pages [9] -->
Page 6 of 20

<!-- b000147 | caption | pages [9] -->
Figure 2: Schematic diagram of loading relationship

<!-- b000149 | prose | pages [9] -->
(3) C = (L,W,H) B is a set of different kinds of boxes,bi is the ith type of boxes, as shown in the formula (4):

<!-- b000150 | prose | pages [9] -->
(4) B = {bi},(i = 1,2,...,11) (5) bi = (li,wi,hi,rli,rwi,rhi) Where li , wi and hi respectively represent the length, width and height of the ith box, and rli , rwi and rhi represent whether the ith box can be assembled and placed around its own length, width and height.

<!-- b000151 | prose | pages [9] -->
For a complete loading, if F is the set of all boxes that have been put into container C, the total volume can be expressed as formula (6) [2]:

<!-- b000152 | prose | pages [9] -->
VF = Â (6) li ·wi ·hi bi2F The number of each kind of box in the container is different, and the number of each kind of box is represented by a set Q ,as shown in the formula (7):

<!-- b000153 | prose | pages [9] -->
(7) Q = {q1,...,qi,...,qn},(i = 1,2,...,11) Use S( f,k) to represent the top area of the kth box.

<!-- b000154 | prose | pages [9] -->
Among them:

<!-- b000155 | prose | pages [9] -->
• f represents the number of layers of boxes in a container.

<!-- b000156 | prose | pages [9] -->
• k represents the position occupied by the kth box, which is called region. In the same layer of boxes, the top area of each box is the region.

<!-- b000157 | prose | pages [9] -->
Use A( f,k) to represent the total bottom area of the boxes stacked on the f-layer k region.

<!-- b000158 | prose | pages [9, 10] -->
11 Â q( f,k) ·S(f,k) A( f,k) = (8) i i i=1 Take q( f,k) as the decision variable. i The constraint conditions are as follows:

<!-- b000159 | furniture | pages [10] -->
Team # 1915782

<!-- b000160 | furniture | pages [10] -->
Page 7 of 20

<!-- b000162 | prose | pages [10] -->
1. The total area of the bottom of the boxes stacked on top of the f-layer k region should be less than or equal to the area of the f-layer k region (the bottom layer is the bottom of the container).This restriction allows boxes to be loaded and unloaded in batches by forklifts.

<!-- b000163 | prose | pages [10] -->
⇢A(1,k) L·W , f = 1 (9) A( f,k) S( f,k) , f ≥2 i

<!-- b000164 | caption | pages [10] -->
Figure 3: Two loading modes that do not meet the constraint conditions

<!-- b000165 | prose | pages [10] -->
2. Various types of box in all layers and all regions for each type are greater than or equal to the total number of boxes required.

<!-- b000166 | prose | pages [10] -->
Â f Â q( f,k) (10) ≥qi i k

<!-- b000167 | prose | pages [10] -->
3. According to Attachment 4:Anticipated Medical Package Demand,We can see that the daily demand for MED 1,MED 2 and MED 3 Emergency Medical Packages in 5 hospitals is 7,2 and 4, respectively. So, the ratio of the number of medical kits required should be 7:2:4.

<!-- b000168 | prose | pages [10] -->
(11) q1 : q2 : q3 = 7 : 2 : 4 In order to make the most of the space in the container and load more boxes, the objective function is to maximize the space utilization of the container.

<!-- b000169 | prose | pages [10] -->
VF (12) max Z = L·W ·H The single-objective programming function that maximizes the space occu- pancy of container space is as follows:

<!-- b000170 | prose | pages [10] -->
VF max Z = L·W ·H 8 i=1 q( f,k) ·S( f,k) > A( f,k) = Â11 > > i i > > A(1,k) L·W , f = 1 < A( f,k) S(f,k) (13) s.t. , f ≥2 > i > > Âf Âk q( f,k) > = qi > : i q1 : q2 : q3 = 7 : 2 : 4

<!-- b000171 | furniture | pages [11] -->
Team # 1915782

<!-- b000172 | furniture | pages [11] -->
Page 8 of 20

<!-- b000173 | heading | pages [11] -->
6.1.1 The Algorithm of the Loading Model

<!-- b000174 | prose | pages [11] -->
3D-RSO algorithm is a heuristic residual space optimization algorithm, which does not need additional preprocessing and optimal solution search operation in the solution process, and can achieve an optimal solution with minimal compu- tational consumption. Compared with other algorithms at the present stage, this algorithm has obvious advantages in solving efﬁciency[2].

<!-- b000175 | caption | pages [11] -->
Figure 4: 3D-RSO algorithm ﬂow chart

<!-- b000176 | heading | pages [11] -->
Some additional notes on the 3D-RSO algorithm ﬂow chart:

<!-- b000177 | prose | pages [11] -->
For any subspace that is put into a new box,the top view is shown in ﬁgure 5.

<!-- b000178 | caption | pages [11] -->
Figure 5: Legend to place rules

<!-- b000179 | prose | pages [11, 12] -->
If the area of S3 is larger than or equal to the area of S2 ,then generate 3 sub- spaces as shown in ﬁgure a.If the area of S3 is smaller than the area of S2 ,then generate 3 subspaces as shown in ﬁgure b.The surfaces in contact with each of the three subspaces are perpendicular to the underside, and the S1 subspace is directly above the new box[2].

<!-- b000180 | furniture | pages [12] -->
Team # 1915782

<!-- b000181 | furniture | pages [12] -->
Page 9 of 20

<!-- b000183 | prose | pages [12] -->
(a) (b)

<!-- b000184 | caption | pages [12] -->
Figure 6: Subspaces produce rules

<!-- b000185 | prose | pages [12] -->
Introducing the evaluation function, the larger the function value, the better.

<!-- b000186 | prose | pages [12] -->
f (A,B) = −(l (B)−l (A)+a)·(w(B)−w(A)+a) (14)

<!-- b000187 | caption | pages [12] -->
Figure 7: Legend to place rules

<!-- b000188 | prose | pages [12] -->
The parameters a = 0.1 are modiﬁed to avoid the situation that the evalu- ation degree is 0.Based on the uncertainty of the number of medical packages in this topic and the idea of the closed-loop feedback system[4], the 3D-RSO al- gorithm is improved by inputting the calculation results of each time into the preset parameters. This improved algorithm improves the space utilization of the calculated results.

<!-- b000189 | heading | pages [12] -->
6.2 Container’s Location and Reconnaissance of Road Networks

<!-- b000190 | heading | pages [12] -->
6.2.1 Determine the Number of Cargo Containers

<!-- b000191 | heading | pages [12] -->
1. How about one container? The distance between Puerto Rico Children’s

<!-- b000192 | prose | pages [12] -->
Hospital and Pavia Arecibo Hospital is 60.63 km.The type B is the longest s- ingle - ﬂight drone, however it can only ﬂy up to 52.67 km at a time.Because the drone has to return, it is impossible to transport the medical packages even if the containers are placed halfway between the two hospitals. As a result, the drones used to transport medicines for Puerto Rico Children’s Hospital and for Hospital Pavia Arecibo must have come from two differ- ent cargo containers.

<!-- b000193 | prose | pages [12, 13] -->
2. Will two containers be enough? As Puerto Rico Children’s Hospital is the closest Hospital to Pavia Arecibo Hospital. As a result, in the case of two cargo containers, one must supply medicine only for Pavia Arecibo Hospital and the other for 4 other hospitals.

<!-- b000194 | furniture | pages [13] -->
Team # 1915782

<!-- b000195 | furniture | pages [13] -->
Page 10 of 20

<!-- b000197 | prose | pages [13] -->
Take these 4 hospitals as vertices and construct a quadrilateral. Traverse each coordinate point in the quadrilateral (longitude and latitude preci- sion is 0.01), and calculate the distance between each point and 4 hospi- tals.However, the point that satisﬁes the condition does not exist. In other words, two containers can not complete the transport task.

<!-- b000198 | prose | pages [13] -->
3. Three containers is the best choice.Because Puerto Rico Children’s Hos- pital and Hospital Pavia Arecibo must be supplied with medicines in two different containers, containers 1 and 2 should be placed between Puer- to Rico Children’s Hospital and Hospital Pavia Arecibo. Since the HIMA Hospital is surrounded by the Cordillera Central (Puerto Rico) mountains and the El Yunque (Puerto Rico) mountains, drones cannot cross them, so container 3 needs to be placed on the road between the Caribbean Medi- cal Center and the HIMA Hospital and transported to them.The remaining Hospital Pavia Santurce is transported by container 2.

<!-- b000199 | heading | pages [13] -->
6.2.2 Drone Transport Model

<!-- b000200 | prose | pages [13] -->
In practice, containers can only be transported to Puerto Rico by port or air- port and then transport by vehicles, so containers can only be placed near the road. Due to the complex situation in the disaster area, containers should be placed as close as possible to the port or airport to avoid long-distance container transport.

<!-- b000201 | prose | pages [13] -->
Drones cannot transport medical packages directly across mountainous areas because of their limited climbing capacity.The containers that supplied medicine to Hospital Pavia Arecibo were not able to supply medicine directly to other hospitals.Hospital Pavia Arecibo, however, has very low demand for medicines (only 1 MED1 per day), as secondary disasters may result in a temporary surge in drug demand, containers of drug stocks should be balanced to the extent pos- sible to cope with such a situation. Avoid situations in which there is a large drug stockpile.So this article considers transferring some of the medicines in the container supplied to Hospital Pavia Arecibo to other containers to avoid the situation that large quantities of medicines being stored for a long time.

<!-- b000202 | prose | pages [13] -->
The constraint conditions are as follows:

<!-- b000203 | prose | pages [13] -->
1. The number of medical packages in all containers is equal to the most rea- sonable loading capacity.

<!-- b000204 | prose | pages [13] -->
n Â N(i1) (15) = qi1 d d=1

<!-- b000205 | prose | pages [13] -->
2. The number of drone in all containers is equal to the most reasonable load- ing capacity.

<!-- b000206 | prose | pages [13, 14] -->
n Â N(i2) (16) = qi2 d d=1 3. The various medical packages should meet the daily number of medical packages required by each hospital.

<!-- b000207 | furniture | pages [14] -->
Team # 1915782

<!-- b000208 | furniture | pages [14] -->
Page 11 of 20

<!-- b000210 | prose | pages [14] -->
n Â x(i2) d j = N(i2) (17) j d=1

<!-- b000211 | prose | pages [14] -->
n 11 Â Â N(i2) ·N(i2,i1) ≥N(i1) (18) j j i2=4 d=1

<!-- b000212 | prose | pages [14] -->
4. Drones have a limited amount of carrier space for medical packaging. The left formula is the combined volume, and the right formula is the limited carrier product.

<!-- b000213 | prose | pages [14] -->
3 Â N(i2,i1) ·V (i1) V (i2) (19) i1=1

<!-- b000214 | prose | pages [14] -->
5. Drones have a limited amount of carrier weight for medical packaging.

<!-- b000215 | prose | pages [14] -->
3 Â N(i2,i1) ·G(i1) G(i2) (20) i1=1

<!-- b000216 | prose | pages [14] -->
6. When there is no load, the value is 1 (the load has no inﬂuence on the ﬂight duration); when there is A full load, the value is e (it is e times longer than when there is no load).

<!-- b000217 | prose | pages [14] -->
i1=1 N(i2,i1) ·G(i1) µ = 1−(1−e) Â3 (21) G(i2)

<!-- b000218 | prose | pages [14] -->
The drone’s range is limited,in order for the drone to be able to sustainably deliver medical ﬁrst medical packages to various hospitals, and it needs to return after delivering medical packages.

<!-- b000219 | prose | pages [14] -->
L(i2) = v(i2) · µt(i2) (22)

<!-- b000220 | prose | pages [14] -->
The left side of the formula (22) represents the limit distance of the drone ﬂight, and the right side represents the sum of the distance from the cargo container to the hospital.

<!-- b000221 | prose | pages [14] -->
& ' v(i2) · µ −1 ·ti2 ≥2Dis (23) Cd,D j 2

<!-- b000222 | prose | pages [14] -->
The objective function is the drones with the longest transport time that should have the shortest transport time:

<!-- b000223 | prose | pages [14] -->
& ' ·x(i2) Dis Cd,D j d j (24) min T = max v(i2) d, j,i2

<!-- b000224 | furniture | pages [15] -->
Team # 1915782

<!-- b000225 | furniture | pages [15] -->
Page 12 of 20

<!-- b000226 | heading | pages [15] -->
6.2.3 Reconnaissance Model

<!-- b000227 | prose | pages [15] -->
⇣ ⌘ Cd, L(i2) Let the reconnaissance area covered by the drone be S ,which refers 2 to the circle with Cd as the center and L(i2) 2 (half of the maximum ﬂying distance of the drone) as the radius. So, ! !2 Cd, L(i2) L(i2) = p · (25) S 2 2

<!-- b000228 | prose | pages [15] -->
⇣ ⌘ Cd, L(i2) The total length of the road in the monitored area is L . 2 Establish a target function that takes the longest road of drone reconnaissance as the target. ! Cd, L(i2) (26) max P = L 2

<!-- b000229 | heading | pages [15] -->
6.2.4 Location Model

<!-- b000230 | prose | pages [15] -->
Location Model is the combination of Drone Transport Model and Recon- naissance Model. Taking into account the shortest transport time and the longest total length of the road under investigation, the objective planning function for selecting the optimal container location is as follows:

<!-- b000231 | prose | pages [15] -->
min T P max Z = j1 +j2 T max P 8 > d=1 N(i1) Ân > = qi1 > d > > d=1 N(i2) > Ân = qi2 > > d > > d=1 x(i2) d j = N(i2) > Ân > > j < i2=4 N(i2) ·N(i2,i1) ≥N(i1) Ân d=1 Â11 (27) s.t. j j > i1=1 N(i2,i1) ·V (i1) V (i2) Â3 > > > > > i1=1 N(i2,i1) ·G(i1) G(i2) Â3 > > > > L(i2) = v(i2) · µt(i2) > > & ' > : v(i2) · µ−1 2 ·ti2 ≥2Dis Cd,Dj

<!-- b000232 | heading | pages [15] -->
6.2.5 The Algorithm of the Location Model

<!-- b000233 | prose | pages [15] -->
Based on the previous analysis, all road information on the map was extract- ed, and the scale of the map and the position of each location in the map were determined through the Google map[5]. Under the condition that the constraint conditions are satisﬁed, all the points on the road in the map are traversal, and the corresponding objective function is calculated, and then the optimization re- sults under the current preset parameters are selected.

<!-- b000234 | furniture | pages [16] -->
Team # 1915782

<!-- b000235 | furniture | pages [16] -->
Page 13 of 20

<!-- b000236 | heading | pages [16] -->
6.3 The Flight Plan

<!-- b000237 | prose | pages [16] -->
In order to monitor as long a road as possible, the type B drone was chosen. Assume that B drone that was chosen for reconnaissance scope L(5) is 26.34 km, 2 altitude Fh is 300 m, unmanned aerial vehicles to carry the camera Angle is 74 degree (in the range of normal wide-angle lens Angle)[8].

<!-- b000238 | caption | pages [16] -->
Figure 8: Reconnaissance schematic diagram of drone

<!-- b000239 | prose | pages [16] -->
(28) lv = 2Fh ·tan(37degree) = 0.452km 2 3 ⇣ ⌘2 ⇣ ⌘2 L(5) L(5) −l2 + 64 v 2 2 q = arccos (29) 75 = 1degree ⇣ ⌘2 L(5) 2 2

<!-- b000240 | prose | pages [16] -->
A single drone reconnaissance for 1 degree, considering the road reconnais- sance should be done during the day time, so the hypothesis road reconnaissance time limit for 12 h. And completed a drone 1 degree reconnaissance need 40 min, in ignoring drone under the condition of charging time, so the ﬁrst ISO container requiring minimum number of monitor road with B unmanned aerial vehicle is

<!-- b000241 | prose | pages [16] -->
d = 360⇥40 N5 12⇥60 = 20.

<!-- b000242 | prose | pages [16] -->
Moreover, considering that the drone must return to ISO container for charg- ing and maintenance, the number of drones should be doubled, so that the two groups of reconnaissance drones can work alternately. This not only takes into account the inevitable charging situation of the drone, but also reduces the work burden of the drone and the use frequency of the drone.

<!-- b000243 | furniture | pages [17] -->
Team # 1915782

<!-- b000244 | furniture | pages [17] -->
Page 14 of 20

<!-- b000245 | prose | pages [17] -->
Considering that in addition to reconnaissance drones and drones transport- ing medical packages, the number of shipping containers in each container is different from that of medical packages, and the load capacity of drones is limit- ed, so the number of drones in each ISO container is 43, 44 and 43, respectively.

<!-- b000246 | prose | pages [17] -->
Finally, as the damage of drones is inevitable, the number of original drones should be increased by 1/4 on the basis of the original ones to prevent emergen- cies. Therefore, the ﬁnal number of each ISO container drone is 53, 54 and 53. In addition to the above number of unmanned aerial vehicles, the ISO container is to load as much medicine as possible to complete the ISO container loading task.

<!-- b000247 | heading | pages [17] -->
6.4 Solution of Model

<!-- b000248 | prose | pages [17] -->
In fact, the location of the container, the conﬁguration of the number and type of shipping containers and medical packages in the container, the rules of packing, the performance of the drone, the number of medical packages required by different hospitals and other factors are mutually restricted. Therefore, this paper gives the best result of the comprehensive full-text model.

<!-- b000249 | prose | pages [17] -->
Based on 2.6GhzCPU and Windows10 platform, it takes about 5.5 seconds to run this traversal calculation.

<!-- b000250 | caption | pages [17] -->
Table 1: Solution of Location model

<!-- b000251 | prose | pages [17] -->
max P min T Container Latitude Longtitude (km) (min)

<!-- b000252 | prose | pages [17] -->
Container1 18.3805 -66.5109 38.7124 312.9891 Container2 18.3490 -66.2830 37.9140 362.1548 Container3 18.2191 -65.8241 33.9136 251.7731

<!-- b000253 | prose | pages [17] -->
The calculation results in Table 1 show that the locations of the container 1 to 3 are at the longitude and latitude coordinates of (18.3805,-66.5109),(18.3490,- 66.2830) and (18.2191,-65.8241) respectively.As shown in Table 1, take container 1 as an example: it takes up to 38.7124 minutes for the drone from container 1 to transport the medical package to the hospital farthest from container 1 in a straight line and return. Within the supply range of container 1, the total road length that can be detected by drone is 312.9891 km.

<!-- b000254 | prose | pages [17] -->
Starting from the three containers, the reconnaissance coverage rate of the entire island road by the drone is 43.477%.

<!-- b000255 | prose | pages [17] -->
As shown in ﬁgure 9,the center of the circle represents the geographical loca- tion of the container. It can be found that there are overlaps between the color blocks, which is called the supply range of the container in this paper. Over- lapping hospital or road segments can be supplied with medical packages or reconnaissance by drones from two different containers. In particular, the sup- ply scope of container 1 and container 2 includes each other’s containers, which means that partial transfer of medical packages can exist between containers.

<!-- b000256 | furniture | pages [18] -->
Team # 1915782

<!-- b000257 | furniture | pages [18] -->
Page 15 of 20

<!-- b000258 | caption | pages [18] -->
Figure 9:

<!-- b000259 | prose | pages [18] -->
Location model in which contents can be transferred between containers[6][7]

<!-- b000260 | prose | pages [18] -->
Depending on the location of the Airport and Port, we recommend that con- tainer 1 be shipped to Puerto Rico via Port of Arecibo or Antonio (Nery) Juarbe Pol Airport and then transported by vehicle to the designated location. Contain- er 2 is shipped to Puerto Rico via Port of San Juan or Fernando Ribas Dominicci Airport and then transported by vehicle to the designated location. Container 3 is shipped to Puerto Rico via Port of Ceiba or Jos´e Aponte de la Torre Airport and then transported by vehicle to designated locations.

<!-- b000261 | prose | pages [18] -->
It can be known from the calculation that the total length of the section where container 1 overlaps with container 2 is 176.8999 km, and the total length of the section where container 2 and container 3 collide is 27.6256 km.

<!-- b000262 | caption | pages [18] -->
Table 2: The result of the Loading model

<!-- b000263 | prose | pages [18] -->
Space Container Drone B Drone H MED 1 MED 2 MED 3 Days Utilization

<!-- b000264 | prose | pages [18] -->
Container1 43+10 1 700 350 350 89.10% 350 Container2 44+10 1 684 342 342 89.48% 342 Container3 43+10 1 809 0 539 91.45% 269

<!-- b000265 | caption | pages [18] -->
Table 2 is the result of the loading model. To simplify the article, we take

<!-- b000266 | prose | pages [18, 19] -->
container 3 as an example to explain. Container 1 is loaded with 43+10 type B drones, among which 43 are operational drones and 10 are standby drones. Con- tainer 1 is equipped with an H Tether[3], which serves as a signal base station. There are 809 MED1, 0 MED2 and 539 MED3 in container 1. With such a large number of contents and a space utilization rate of 91.445%, these contents can support the drug demand of hospitals within the container supply range for 269 days, which is a very good result.

<!-- b000267 | furniture | pages [19] -->
Team # 1915782

<!-- b000268 | furniture | pages [19] -->
Page 16 of 20

<!-- b000270 | prose | pages [19] -->
(a) Container1 (b) Container2

<!-- b000271 | prose | pages [19] -->
(c) Container3

<!-- b000272 | caption | pages [19] -->
Figure 10: Loading condition of three containers

<!-- b000273 | prose | pages [19] -->
Based on 2.6GhzCPU and Windows10 platform, it only takes about 0.35 sec- onds to run the 3D-RSO algorithm every time.

<!-- b000274 | caption | pages [19] -->
Figure 11: Daily transport and transhipment plan

<!-- b000275 | caption | pages [19] -->
Figure 11 shows the daily transport and transshipment plan intuitively.

<!-- b000276 | heading | pages [19] -->
7 Sensitivity Analysis

<!-- b000277 | prose | pages [19, 20] -->
Since the impact of hurricane on Puerto Rico is diverse, the weight of the two targets in the model should be changed in the face of different hurricane disasters and actual situations. In this way, the location of ISO container will be more practical and suitable for rescue work. Therefore, we take 0.1 as the change gradient of weight and calculate 10 sets of results to test the sensitivity and feasibility of the model.

<!-- b000278 | furniture | pages [20] -->
Team # 1915782

<!-- b000279 | furniture | pages [20] -->
Page 17 of 20

<!-- b000281 | caption | pages [20] -->
Table 3: Sensitivity Analysis

<!-- b000282 | prose | pages [20] -->
j1=0.1 j2=0.9 j1=0.2 j2=0.8 j1=0.3 j2=0.7 j1=0.4 j2=0.6 j1=0.5 j2=0.5 Container1 30.6622 0.2441 0.24406 0.2441 0.2441 minT(min) Container2 37.7495 37.7495 37.7495 8.2333 8.2331 Container3 39.8384 39.8384 39.8384 39.8384 33.9136 Container1 352.0325 239.8834 239.8834 239.8834 239.8834 maxP (km) Container2 470.2871 470.2871 470.2871 271.2144 271.2144 Container3 318.7733 318.7733 318.7733 318.7733 251.7731 Coverage Rate 0.6042 0.5367 0.5367 0.4064 0.4007 j1=0.6 j2=0.4 j1=0.7 j2=0.3 j1=0.8 j2=0.2 j1=0.9 j2=0.1 j1=1 j2=0 Container1 0.2441 0.2441 0.2441 0.2441 0.2441 minT(min) Container2 8.2331 8.2331 8.2331 8.2331 8.2331 Container3 33.9136 33.8503 33.8503 33.8503 33.8503 Container1 239.8833 239.88333 239.8834 239.8834 238.5980 maxP (km) Container2 271.2144 271.2144 271.2144 271.2144 271.2144 Container3 251.7731 249.6844 249.6844 249.6844 249.6844 Coverage Rate 0.4007 0.4008 0.4008 0.4008 0.4001

<!-- b000283 | prose | pages [20] -->
It can be found from this table that the inﬂuence of j1 and j2 on the result is not gradual, and there is a phi threshold that determines the ﬁnal calculation result. When the values of j1 and j2 are close to the threshold, the sensitivity is very high. However, when the value is far from the threshold, the calculation results are almost unaffected. Therefore, it can be seen that j1 and j2 should be carefully determined according to the actual situation, especially when the value is close to the threshold.

<!-- b000284 | heading | pages [20] -->
8 Model Extension

<!-- b000285 | prose | pages [20] -->
Compared with the detailed scheme described in this paper, the following scheme improves the road detection capability by sacriﬁcing part of the system’s medical rescue capability. In this scheme, the transshipment between containers is no longer considered, that is, j1 = 0,j2 = 1. In addition, when the containers are packed, as many drones as possible are carried to improve the efﬁciency of reconnaissance and broaden the scope of reconnaissance.

<!-- b000286 | prose | pages [20] -->
In this scheme, there is no intersection area between the supply scope of con- tainer 1 and container 2, and there is still intersection between container 2 and container 3. The total length of the road at the intersection is 137.2139 km. At this time, the reconnaissance coverage rate of the drone on the road of the whole island reaches 60.4%, which is higher than that of scheme 1.

<!-- b000287 | furniture | pages [21] -->
Team # 1915782

<!-- b000288 | furniture | pages [21] -->
Page 18 of 20

<!-- b000289 | caption | pages [21] -->
Table 4: Solution of Location model of Scheme 2

<!-- b000290 | prose | pages [21] -->
max P min T Container Latitude Longtitude (km) (min)

<!-- b000291 | prose | pages [21] -->
Container1 18.2948 -66.7748 30.6622 352.0325 Container2 18.2705 -66.2200 37.7495 470.2871 Container3 18.2419 -65.8781 39.8384 318.7733

<!-- b000292 | caption | pages [21] -->
Figure 12: Location model in which contents can not be transferred between

<!-- b000293 | prose | pages [21] -->
containers[6][7] As can be seen from table 5, with the increase of the number of drones, the number of medical packages in the container decreases correspondingly. The supply time of materials in container 2 and container 3 to the disaster area is obviously shortened. Moreover, as containers cannot transfer boxes, material consumption is very uneven, and the medical packages in container 1 can last for 630 days.

<!-- b000294 | caption | pages [21] -->
Table 5: The result of the Loading model of Scheme 2

<!-- b000295 | prose | pages [21] -->
Space Container Drone B Drone H MED 1 MED 2 MED 3 Days Utilization

<!-- b000296 | prose | pages [21, 22] -->
Container1 68 1 630 0 350 92.86% 630 Container2 68 1 321 212 213 90.98% 106 Container3 68 1 396 0 263 91.54% 131 The detailed daily transport plan in scheme 2 is shown in ﬁgure 13.

<!-- b000297 | furniture | pages [22] -->
Team # 1915782

<!-- b000298 | furniture | pages [22] -->
Page 19 of 20

<!-- b000300 | caption | pages [22] -->
Figure 13: A loading model in which contents cannot be transferred between

<!-- b000301 | prose | pages [22] -->
containers

<!-- b000302 | heading | pages [22] -->
9 Strengths and Weakness

<!-- b000303 | heading | pages [22] -->
9.1 Strengths

<!-- b000304 | prose | pages [22] -->
• In the loading model of containers, the orderly stacking method is adopted in this paper, so that the boxes have the overall stability of the group and are convenient for loading and unloading, which is in line with the actual situation of container transportation.

<!-- b000305 | prose | pages [22] -->
• Considering the transportation of containers in disaster-hit areas under the real situation, the ports or airports to transport containers are selected, so that containers can only be transported and placed along highways, which improves the feasibility of the model.

<!-- b000306 | prose | pages [22] -->
• The improved 3D-RSO algorithm is convenient and effective in solving the 3D loading model, which can obtain the results in a very short time, is very suitable for the allocation of materials in emergency, and it has a very high space utilization rate.

<!-- b000307 | prose | pages [22] -->
• Considering the transfer of medical packages between containers, the dis- tribution of medical packages is balanced, which improves the system’s ability to withstand possible secondary disasters and extends the time of disaster relief.

<!-- b000308 | prose | pages [22] -->
• In addition, a plan focusing on road reconnaissance missions was present- ed, giving a more comprehensive consideration to the problem.

<!-- b000309 | heading | pages [22] -->
9.2 Weakness

<!-- b000310 | prose | pages [22] -->
• The inﬂuence of load on drone is relatively simple. Due to the complexity of drone’s ﬂight process, this paper did not deeply study the mechanism and process of drone’s ﬂight, and there are some errors.

<!-- b000311 | furniture | pages [23] -->
Team # 1915782

<!-- b000312 | furniture | pages [23] -->
Page 20 of 20

<!-- b000313 | prose | pages [23] -->
• Without considering the inﬂuence of altitude, wind, weather and other fac- tors on drone ﬂight, it lacks practicality.

<!-- b000314 | prose | pages [23] -->
• Without reasonable planning for the medical bag loaded by the drone, it only meets the daily needs of the hospital, resulting in a low utilization efﬁciency of the drone transporting the medical bag.

<!-- b000315 | heading | pages [23] -->
References

<!-- b000316 | references | pages [23] -->
[1] Liu Lirong, Li Wei. Derivation of calculation formula for mutual conversion

<!-- b000317 | references | pages [23] -->
of GPS coordinates and direction and distance [A]. Technical application [J].

<!-- b000318 | references | pages [23] -->
Chongqing: Chongqing Jiaotong University, 2018:106

<!-- b000319 | references | pages [23] -->
[2] Zhengyang Shang,Jinan Gu, Shixi Tang,Xiaohong Sun. An efﬁcient resid-

<!-- b000320 | references | pages [23] -->
ual space optimization algorithm for three dimensional packing problem-

<!-- b000321 | references | pages [23] -->
s[J/OL].Computer Engineering and Applications. http://kns.cnki.

<!-- b000322 | references | pages [23] -->
net/kcms/detail/11.2127.tp.20181220.1008.019.html

<!-- b000323 | references | pages [23] -->
[3] Establishment and guarantee of emergency communication system with

<!-- b000324 | references | pages [23] -->
tethered drone [J]. Satellite and network,2017,(6):56-57.

<!-- b000325 | references | pages [23] -->
[4] Control theory - Wikipedia[DB/OL].

<!-- b000326 | references | pages [23] -->
https://en.wikipedia.org/wiki/Control_theory#Classical_

<!-- b000327 | references | pages [23] -->
control_theory,28 January 2019.

<!-- b000328 | references | pages [23] -->
[5] Google Maps[DB/OL].

<!-- b000329 | references | pages [23] -->
http://ditu.google.cn/,2019.

<!-- b000330 | references | pages [23] -->
[6] Puerto Rico Ports Authority - Wikipedia[DB/OL].

<!-- b000331 | references | pages [23] -->
https://en.wikipedia.org/wiki/Puerto_Rico_Ports_

<!-- b000332 | references | pages [23] -->
Authority,11 October 2018.

<!-- b000333 | references | pages [23] -->
[7] List of airports in Puerto Rico - Wikipedia[DB/OL].

<!-- b000334 | references | pages [23] -->
https://en.wikipedia.org/wiki/List_of_airports_in_

<!-- b000335 | references | pages [23] -->
Puerto_Rico,16 September 2018.

<!-- b000336 | references | pages [23] -->
[8] A Brief Discussion on the Wide Angle Lens of the Camera[A].Journal of

<!-- b000337 | references | pages [23] -->
TaiYuan Urban Vocational college[J].Taiyuan:Taiyuan City Vocational and

<!-- b000338 | references | pages [23] -->
Technical College,2009,(4):122-123.
