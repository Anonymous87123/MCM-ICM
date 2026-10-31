# P-B-2019-1908286-37248927

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
1908286

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | prose | pages [1] -->
2019 MCM/ICM Summary Sheet

<!-- b000007 | prose | pages [1] -->
Hurricane Maria Damage left Puerto Rico people a lot of pain and devastation. HELP,Inc., an NGO, is attempting to improve its response capabilities by designing a transportable disaster response system called "DroneGo".

<!-- b000008 | prose | pages [1] -->
In order to better assess the transport capability of the drone ﬂeet, we establish a Transport Capability Evaluation Model of the drone ﬂeet, so that we can maximize the medicine transportation capability of the drone ﬂeet when the disaster location is unknown. In this model, we use the algorithm of linear programming to solve the limitations of volume, weight and other simple factors. After that, we used an algorithm based on three-space segmentation and improved Monte Carlo simulation to solve the size limitation of the objects. As a result, we obtain a reliable evaluation of the transport capability of drones, and it can be found that among the drones, the transportation capability of drone G is the strongest.

<!-- b000009 | prose | pages [1] -->
Through the research on the reconnaissance method of the drones, we get the Reconnaissance Ca- pability Model of the drone ﬂeet. In this model, we ﬁnd that the reconnaissance capability of drone B is the strongest. Based on these two models (TCM & RCM) and abundant geographic information, we developed a Geospatial Analysis Model. We employ the Analytical Hierarchy Process (AHP) in the space of all position, obtaining a spatial distribution of drone ﬂeet ˛a´rs transportation capability and re- connaissance capability. Then, we establish an overall Efﬁciency Evaluation Model for the drone ﬂeet, using a nonlinear programming with a variable parameter to obtain the optimal solution of the drone ﬂeet overall efﬁciency and its spatial location. Consequently, we can determine a conﬁguration of the drone ﬂeet and each container’s drop point. DroneGo users can also adjust the variable parameter de- pending on whether they care more about their ﬂeet ˛a´rs transport capability or reconnaissance capability to determine different options. For the problem of multiple containers, we use a dynamic programming rule that allows users to arrange multiple containers.

<!-- b000010 | prose | pages [1] -->
In considering that the transportation capability of the drone ﬂeet is as important as the reconnais- sance capability, we get results that the medicine delivery can be maintained for more than two months and road reconnaissance coverage can reach nearly 60%. Meanwhile we construct an efﬁcient Schedule Arrangement Model and Route Arrangement Model of drones using an integer programming model and an improved greedy algorithm, so that the drone ﬂeet can be auto arranged.

<!-- b000011 | prose | pages [1] -->
The sensitivity analysis shows the strong robustness of our model. Meanwhile, we further discuss the possibility of developing a DroneGo system software, and provide practicable advice to the HELP, Inc. CEO.

<!-- b000012 | keywords | pages [1] -->
Keywords: Multi-Objective Programming,Dynamic Programming, Drone Rescue Model, AHP

<!-- b000013 | furniture | pages [2] -->
Team # 1908286

<!-- b000014 | furniture | pages [2] -->
Page 1 of 22

<!-- b000015 | heading | pages [2] -->
Contents

<!-- b000016 | contents | pages [2] -->
1 Introduction

<!-- b000017 | contents | pages [2] -->
2

<!-- b000018 | contents | pages [2] -->
2 Assumptions and Justiﬁcation

<!-- b000019 | contents | pages [2] -->
2

<!-- b000020 | contents | pages [2] -->
3 Transportation Capability Evaluation Model

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
3.1

<!-- b000023 | contents | pages [2] -->
Assumptions in This Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
3

<!-- b000025 | contents | pages [2] -->
3.2

<!-- b000026 | contents | pages [2] -->
Three Space Division Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
3

<!-- b000028 | contents | pages [2] -->
3.3

<!-- b000029 | contents | pages [2] -->
Putting MEDs into Bays

<!-- b000030 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
5

<!-- b000032 | contents | pages [2] -->
3.4

<!-- b000033 | contents | pages [2] -->
Drone Transport Capability Model . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
6

<!-- b000035 | contents | pages [2] -->
3.5

<!-- b000036 | contents | pages [2] -->
Putting Drones and Bays into Cargo Conatainers . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
7

<!-- b000038 | contents | pages [2] -->
3.6

<!-- b000039 | contents | pages [2] -->
Monte-Carlo Simulation And Results . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
7

<!-- b000041 | contents | pages [2] -->
4 Geospatial Analysis Model

<!-- b000042 | contents | pages [2] -->
8

<!-- b000043 | contents | pages [2] -->
4.1

<!-- b000044 | contents | pages [2] -->
Drone Reconnaissance Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
8

<!-- b000046 | contents | pages [2] -->
4.2

<!-- b000047 | contents | pages [2] -->
Geographical Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
9

<!-- b000049 | contents | pages [2] -->
4.3

<!-- b000050 | contents | pages [2] -->
Singal Location Determination

<!-- b000051 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
10

<!-- b000053 | contents | pages [2] -->
4.4

<!-- b000054 | contents | pages [2] -->
Multiple Locations Determination

<!-- b000055 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
13

<!-- b000057 | contents | pages [2] -->
4.5

<!-- b000058 | contents | pages [2] -->
Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
14

<!-- b000060 | contents | pages [2] -->
5 Fleet Arrange Model

<!-- b000061 | contents | pages [2] -->
14

<!-- b000062 | contents | pages [2] -->
5.1

<!-- b000063 | contents | pages [2] -->
Schedule Arrangement Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
14

<!-- b000065 | contents | pages [2] -->
5.2

<!-- b000066 | contents | pages [2] -->
Drone Route Planning Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
16

<!-- b000068 | contents | pages [2] -->
6 Sensitivity Analysis

<!-- b000069 | contents | pages [2] -->
19

<!-- b000070 | contents | pages [2] -->
7 Strengths and Weaknesses

<!-- b000071 | contents | pages [2] -->
19

<!-- b000072 | contents | pages [2] -->
7.1

<!-- b000073 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
19

<!-- b000075 | contents | pages [2] -->
7.2

<!-- b000076 | contents | pages [2] -->
Weaknesses

<!-- b000077 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
20

<!-- b000079 | contents | pages [2] -->
8 Conclusion

<!-- b000080 | contents | pages [2] -->
20

<!-- b000081 | furniture | pages [3] -->
Team # 1908286

<!-- b000082 | furniture | pages [3] -->
Page 2 of 22

<!-- b000083 | contents | pages [3] -->
An optional Design of DroneGo

<!-- b000084 | heading | pages [3] -->
1 Introduction

<!-- b000085 | prose | pages [3] -->
People in disaster areas are in great need of timely emergency services. [1] Drones can help a lot in emergency rescue. According to a drone manufacturer DJI [2], drones have saved 59 lives since 2013.

<!-- b000086 | prose | pages [3] -->
In this paper, we will

<!-- b000087 | prose | pages [3] -->
• Analyze three dimensional packing problem and develop Three Space Division Model and improved Monte-Carlo Simulation to solve the problem of packing restrictions in the transportation.

<!-- b000088 | prose | pages [3] -->
• Analyze the transportation capability and detective capability of each Drone type,apply AHP method to considers the inﬂuence of many possible factors on the selection of con- tainer drop location , including transportation, population, geography and medical infor- mation.

<!-- b000089 | prose | pages [3] -->
• Build a model to determine drone payload packing conﬁguration and solve it with a com- plex integer programming quickly and accurately.

<!-- b000090 | prose | pages [3] -->
• Improve greedy algorithm and ﬁgure out the drone route planing quickly and accurately.

<!-- b000091 | heading | pages [3] -->
2 Assumptions and Justiﬁcation

<!-- b000092 | prose | pages [3] -->
We make some general assumptions to simplify our model. These assumptions together with corresponding justiﬁcation are listed below:

<!-- b000093 | prose | pages [3] -->
• There are no charging devices for drones. In 2017, Hurricane Maria knocked down 80% of Puerto Rico’s utility poles and all transmission lines. We can infer that electricity are not available on the island. Our Cargo will not include charging equipment or generating set, due to extra weight and inconvenience.

<!-- b000094 | prose | pages [3] -->
• The cargo weight does not inﬂuence the maximum ﬂight distance of a drone. That is, maximum ﬂight distance is exactly the same with or without a cargo. We make the assumption for simplicity. In reality, the weight of a delivery drone is often larger than that of its cargo. It is quite reasonable to neglect the inﬂuence of cargo weight. And this will greatly simply our model.

<!-- b000095 | prose | pages [3] -->
• For each Cargo Container, we will load one tethered Drone (type H). In natural disasters, communication facilities are often affected to various degrees, and emergency communi- cation becomes an urgent need. It can act as an emergency communication base station.

<!-- b000096 | prose | pages [3] -->
Tethered drones will greatly enhance the disaster response capability of DroneGo system.

<!-- b000097 | prose | pages [3] -->
• One drone can carry one drone cargo bay or no bay for every ﬂight. If the drone carries one, it can only deliver the bay to one location. Both of the two types of drone cargo bay are "top loaded", that is, loaded on the top of a drone. If we distribute more than one bay at a ﬂight, connections between cargo bays could be unstable. We can deliver a drone cargo bay to only one place since it is an integral package that cannot be open in transit.

<!-- b000098 | prose | pages [3] -->
• Helicopters can transport cargo containers to any given place in the disaster area. In disaster-affected areas, timely external assistance is urgently needed to restore order. There- fore, we consider air transportation rather than sea transportation. Although Puerto Rico is an island, air transportation will bring adaptability to our model in other situations.

<!-- b000099 | prose | pages [3] -->
• Communication and data transmission of drones are always available. We can achieve telecommunication by radio communication or satellite communication. Drone commu- nication dose not rely on ground devices.

<!-- b000100 | furniture | pages [4] -->
Team # 1908286

<!-- b000101 | furniture | pages [4] -->
Page 3 of 22

<!-- b000102 | prose | pages [4] -->
• For the ith type of drone, its maximum Flight Distance, denoted by Disti is in direct proportion to the product of Speed and FlightTime(No Cargo). From that assumption, we have Disti = α × Speed × Flight Time (No Cargo), where α represents distance-loss coefﬁcient. Here we neglect the effect of weather (especially wind) and different battery and motor of different drones of a speciﬁc type. To determine α, we note that there are mostly mountains with few plains. And Puerto Rico has a mean elevation of 261 m. [3] The high elevation shortens the maximum ﬂight distance. We have α < 1. For simpliﬁcation, we choose α = 0.9.

<!-- b000103 | prose | pages [4] -->
More detailed assumptions will be listed if needed.

<!-- b000104 | heading | pages [4] -->
3 Transportation Capability Evaluation Model

<!-- b000105 | prose | pages [4] -->
In this section, we will evaluate transportation ability of each type of drones. For simplicity, we will focus on the need of medical transportation here. We will incorporate road reconnais- sance into our model in Section 5.

<!-- b000106 | heading | pages [4] -->
3.1 Assumptions in This Model

<!-- b000107 | prose | pages [4] -->
We will use the following assumptions in this section:

<!-- b000108 | prose | pages [4] -->
• All Cargo Containers(CC), Drone (in shipping containers), Drone Cargo Bays (DCB), and Medical packages (MP) are cuboids.

<!-- b000109 | prose | pages [4] -->
• Drones and Drone Cargo Bays should be placed into Cargo Containers in parallel, which is "parallel placement". That is, the inner subface of Drones or Bays must be par- allel to the corresponding surface of the Cargo Container. There are two reasons. For one thing, the parallel placement is one of the most commonly used packing methods. For another thing, cargos can be easily placed in this way and have a high stability.

<!-- b000110 | prose | pages [4] -->
• The thickness of Drone Cargo Bays can be neglected.

<!-- b000111 | prose | pages [4] -->
• Goods can be arbitrarily rotated, but must still satisfy the "parallel placement" condi- tion.

<!-- b000112 | prose | pages [4] -->
• As is interpreted in the problem description, each Cargo Container’s contents should be packed, so all Medical Packages should be packed in Drone Cargo Bays. We do not consider Medical Packages directly placed in a Cargo Container.

<!-- b000113 | heading | pages [4] -->
3.2 Three Space Division Model

<!-- b000114 | heading | pages [4] -->
3.2.1 One Goods Condition

<!-- b000115 | prose | pages [4] -->
To design a packing conﬁguration for DroneGo, we need to put MEDs into Bays and put Bays or Drones into Containers. Due to various kinds of goods in the problem, this is a three- dimensional heterogeneous container loading problem. We use the Three Space Division Method and Monte Carlo Simulation to solve it.

<!-- b000116 | prose | pages [4, 5] -->
Note that we refer to a rectangular container that contains goods as a box. As is shown in Figure 1, L, W and H is the length, width and height of the container, respectively. Similarly, l, w and h is the length, width and height of the cargo, respectively. We set up a Cartesian coordinate at the left bottom vertex of the container. Note that we consider the position of the container is unchanged. We put the cargo into the container, so that two left bottom vertexes coincide. Arrangement problem is a way to think about ways to put the cargo. To put h into x, y and z coordinates, we have A3 3 = 6. There are six ways to put the cargo inside. That is, there are six possible combinations of the coordinates of the diagonal vertex of the cargo.

<!-- b000117 | furniture | pages [5] -->
Team # 1908286

<!-- b000118 | furniture | pages [5] -->
Page 4 of 22

<!-- b000120 | caption | pages [5] -->
Figure 1: Three Space Division

<!-- b000121 | prose | pages [5] -->
For every speciﬁc combination, we can see that the rest space in the container are cut into three parts (spaceX, spaceY and spaceZ) , see ﬁgure 1. One possible sequence (shown in Figure 1) to generate the three parts is

<!-- b000122 | prose | pages [5] -->
1. Procedure X: Cut the remaining space using a plane perpendicular to the X-axis and get spaceX.

<!-- b000123 | prose | pages [5] -->
2. Procedure Y: Cut the remaining space using a plane perpendicular to the Y-axis and get spaceY.

<!-- b000124 | prose | pages [5] -->
3. Procedure Z: Cut the remaining space using a plane perpendicular to the Z-axis and get spaceZ.

<!-- b000125 | prose | pages [5] -->
We refer to this sequence as a X-Y-Z sequence. The rest are similar. Arrangement problem is a way to think about the space cutting process. To generate a sequence from procedure X, Y and Z we have A3 3 = 6.

<!-- b000126 | prose | pages [5] -->
Thus, if a cargo can be put into the cargo, we have the total cases of three space division: 6 × 6 = 36 Then we consider every new space as a new container. And the three space division process goes on, until the cargo can not be put into any of the existing containers. In this way, we can traverse all situations and ﬁnd the optimal solution for a speciﬁc objective function.

<!-- b000127 | heading | pages [5] -->
3.2.2 Multiple Goods Condition

<!-- b000128 | prose | pages [5] -->
To clarify the problem, we will use the following notations:

<!-- b000129 | prose | pages [5] -->
• K = {1, 2, . . . , |K|} is the set of Boxes’ number;

<!-- b000130 | prose | pages [5] -->
• R = {1, 2, . . . , |R|} is the set of goods’ types;

<!-- b000131 | prose | pages [5] -->
• Mr = {1, 2, . . . , |Mr|} is the set of goods’ number (same type) ;

<!-- b000132 | prose | pages [5] -->
• sB = (L W H)T is Box Size column vector; r = (lr wr hr)T is the rth type of Goods Size column vector;

<!-- b000133 | prose | pages [5] -->
• sG

<!-- b000134 | prose | pages [5] -->
• Xk is the number of goods in the kth box;

<!-- b000135 | prose | pages [5] -->
•  1, if the mth Goods of Type r is in Box k Ykrm = is an Existing Flag; 0, otherwise

<!-- b000136 | prose | pages [5] -->
• u = (xkrm ykrm zkrm)T is coordinates of the mth goods of Type r in Box k;

<!-- b000137 | prose | pages [5] -->
•  1, if the length of the mth Goods of Type r is parallel to the x-axis lxrm = 0, otherwise

<!-- b000138 | prose | pages [5] -->
is a Conﬁguration Variable;

<!-- b000139 | prose | pages [5] -->
• lxrm lyrm lzrm !

<!-- b000140 | prose | pages [5] -->
wxrm wyrm wzrm P = is Conﬁguration Matrix.

<!-- b000141 | prose | pages [5, 6] -->
hxrm hyrm hzrm Undeﬁned elements in the matrix is deﬁned similarly to lxrm.

<!-- b000142 | furniture | pages [6] -->
Team # 1908286

<!-- b000143 | furniture | pages [6] -->
Page 5 of 22

<!-- b000145 | prose | pages [6] -->
In multiple-goods-condition, we consider the container loading problem as a Single-objective integer programming problem. Constraint Conditions of the three-dimensional heterogeneous container loading problem are listed below:

<!-- b000146 | prose | pages [6] -->
1. Boxes should contain all goods:

<!-- b000147 | prose | pages [6] -->
|K| |R| X X Xk = Mr r=1 k=1 2. Corresponding Rule. Each goods should be placed into just only one box:

<!-- b000148 | prose | pages [6] -->
|K| X ∀r ∈R, ∀m ∈Mr, Ykmr = 1 k=1

<!-- b000149 | prose | pages [6] -->
3. Conﬁguration Constraint. Each edge in each goods should be parallel to just only one edge of the corresponding box. Let P = (pab)3×3, we have

<!-- b000150 | prose | pages [6] -->
3 3 X X pab = 1 pab = 1.

<!-- b000151 | prose | pages [6] -->
a=1 b=1

<!-- b000152 | prose | pages [6] -->
4. Box Size Constraint. All goods should be inside the corresponding box:

<!-- b000153 | prose | pages [6] -->
∀k ∈K, ∀r ∈R, ∀m ∈Mr, Ykrm(u + P · sG r ) ≤sB We can solve the programming problem with a speciﬁc objective function.

<!-- b000154 | heading | pages [6] -->
3.3 Putting MEDs into Bays

<!-- b000155 | prose | pages [6] -->
Since there are only three types of MEDs and two types of Bays, putting MEDs into Bays is relatively simple. In 3D heterogeneous container loading problems, space utilization(SU) usually decreases as type of goods R increases. For simplicity, we only consider two types of MEDs or less in a Bay. We do not need to consider an objective function in this process. Rather, we list all possible combinations subject to its constraint conditions.

<!-- b000156 | prose | pages [6] -->
Let R = {1, 2, 3}, whose elements 1, 2 and 3 correspond to MED1, MED2 and MED3, re- spectively. And |Mr| is the number of MEDr. For type q Bay (q = 1, 2), we have the following constraint conditions:

<!-- b000157 | prose | pages [6] -->
P|K| k=1 Xk = P3  r=1 Mr  P|K|  k=1 Ykmr = 1, ∀r ∈R, ∀m ∈Mr    P3 , (1) a=1 pab = 1 P3  b=1 pab = 1    q , ∀k ∈K, ∀r ∈R, ∀m ∈Mr Ykrm(u + P · sG r ) ≤sB 

<!-- b000158 | prose | pages [6] -->
where sB 1 = (8 10 14)T, sB 2 = (24 20 20)T.

<!-- b000159 | prose | pages [6] -->
For type i Drone, an additional constraint is that total weight cannot exceed Max Payload Capability(MPCi): 2|M1| + 2|M2| + 3|M3| ≤MPCi (2)

<!-- b000160 | prose | pages [6] -->
(1 and (2) determine whether we can put a set of MEDs into a Bay. If that set of MEDs works, we calculate its space utilization:

<!-- b000161 | prose | pages [6, 7] -->
P3 r=1 (|Mr|lrwrhr) SU = , LqWqHq where (l1 w1 h1)T = (14 7 5)T, (l2 w2 h2)T = (5 8 5)T, (l3 w3 h3)T = (12 7 4)T, (L1 W1 H1)T = (8 10 14)T, (L2 W2 H2)T = (24 20 20)T.

<!-- b000162 | furniture | pages [7] -->
Team # 1908286

<!-- b000163 | furniture | pages [7] -->
Page 6 of 22

<!-- b000165 | prose | pages [7] -->
We draw the space utilization plot of Drone D (Bay 1) and Drone F (Bay 2), see Figure 2. From the ﬁgure we can see that space utilization of Bay 2 is relatively low. The reason is that the inequality (2) is strict. In most cases, the max payload capability is so small that the all sets of MEDs that satisfy (2) can be loaded. So the sub-ﬁgures for Bay 2 clearly shows the inequality (2).

<!-- b000166 | caption | pages [7] -->
Figure 2: Space Utilization with different MEDs and different Bays

<!-- b000167 | prose | pages [7] -->
From Figure 2, we conclude that the Transport Capability matrix is

<!-- b000168 | prose | pages [7] -->
1 1 1   2 4 2   7 7 4     2 4 2 TC = . (4)   7 7 5     11 11 7   10 10 6

<!-- b000169 | heading | pages [7] -->
3.4 Drone Transport Capability Model

<!-- b000170 | prose | pages [7] -->
Since we only consider medicine transport in this section, there must be a corresponding Drone Cargo Bay on each drone. The number of Typei Drones to carry NumMEDj MEDjs is Numij = NumMEDj/TCij . Note that we use Numij to evaluate transport capability, so it may be a decimal. The volume needed when one Typei Drone carries all MEDs for one day is

<!-- b000171 | prose | pages [7] -->
3 X V Med Day + V Bay Numij)(V drone = ( ) i i i j=1

<!-- b000172 | prose | pages [7] -->
. The number of days that a Typei Drone can continue transporting MEDs to all needed place is

<!-- b000173 | prose | pages [7, 8] -->
Daysi = Vcontainer/V Med Day i Transport Capability Index of Typei Drone is deﬁned as the normalization of maximum day Daysi:

<!-- b000174 | furniture | pages [8] -->
Team # 1908286

<!-- b000175 | furniture | pages [8] -->
Page 7 of 22

<!-- b000177 | prose | pages [8] -->
1≤k≤7 {Daysk} TCIi = Daysi/ max

<!-- b000178 | prose | pages [8] -->
We have two matrices:

<!-- b000179 | prose | pages [8] -->
2.97 0.0629     15.92 0.3371     8.78 0.1859         24.45 0.5178 Days = TCI = (5)     41.46 0.8782         28.98 0.6139     47.21 1.0000

<!-- b000180 | heading | pages [8] -->
3.5 Putting Drones and Bays into Cargo Conatainers

<!-- b000181 | prose | pages [8] -->
According to TCI matrix (5), Type E and G Drones have the best transport capability. We will choose Type E and G as alternative transport drones. The corresponding Bays are Bays 2. We will also load one Drone H (tethered drone) in each Cargo Container, because it helps to build emergency communication.

<!-- b000182 | prose | pages [8] -->
Let R = {4, 5, 6, 7}. 4, 5, 6 and 7 represent Bay 2, Drone E, H and G, respectively. The number of MEDs in Bay 2 only relies on Type i drone’s Max Payload Capability MPCi. So we conclude that for Drone ﬂeet consisting of E and G, transport capability is only relevant to Total Load Weight:

<!-- b000183 | prose | pages [8] -->
X MPCi × |Mi| = 15|M5| + 20|M7| TLW = (6) i=5,7

<!-- b000184 | prose | pages [8] -->
Our problem can be stated as

<!-- b000185 | prose | pages [8] -->
TLW = 15|M5| + 20|M7| max

<!-- b000186 | prose | pages [8] -->
Equation (??) shows that each Drone must carry one Bay, so the total number of Drones E and G equal to the number of Bays 2. Equation (??) shows that each Cargo Container should have one Type H Drone.

<!-- b000187 | heading | pages [8] -->
3.6 Monte-Carlo Simulation And Results

<!-- b000188 | prose | pages [8] -->
We use Monte-Carlo Simulation to get a satisfactory solution of the problem in Section 4.5. Since this is a NP-completeness problem, it takes too long to traverse all situations. Our objec- tive function will not have major changes with a narrow change of inputs. That is, the optimal point is not an isolated singularity. That’s why we choose Monte-Carlo Simulation.

<!-- b000189 | prose | pages [8] -->
If the probability to ﬁnd the optimal point is 10−5 for one simulation, the probability to ﬁnd the optimal point will be 1 −0.999991000000 = 0.999954 with one billion simulations. Figure 3 is our simulation process using Three Space Division method. We start at a feasible solution |M4| = 50, |M5| = 30, |M6| = 1, |M7| = 20.

<!-- b000190 | furniture | pages [9] -->
Team # 1908286

<!-- b000191 | furniture | pages [9] -->
Page 8 of 22

<!-- b000192 | caption | pages [9] -->
Figure 3: Monte-Carlo Simulation Process

<!-- b000193 | caption | pages [9] -->
Table 1: Satisfactory Packing Conﬁguration for Each Container

<!-- b000194 | prose | pages [9] -->
Using the Three Space Division Model and Monte-Carlo Simulation, we obtain the satisfac- tory packing conﬁguration for each container (with or without Drone H). The result shows that the ideal optimal solution is, at most, slightly better than our satisﬁed solution(space utiliza- tion up to 97.97%). It also validates that Drone G has the best transportation capability, which perfectly ﬁt the highest Drone G TCI value.

<!-- b000195 | heading | pages [9] -->
4 Geospatial Analysis Model

<!-- b000196 | heading | pages [9] -->
4.1 Drone Reconnaissance Model

<!-- b000197 | prose | pages [9] -->
For a video-capable drone, in order to effectively estimate its maximum viewing radius, rview, we make the following assumptions:

<!-- b000198 | prose | pages [9] -->
1. The height between a drone and the ground is 20 meters.

<!-- b000199 | prose | pages [9] -->
2. The drone’s lens can swing back and forth from side to side, with unlimited viewing angles.

<!-- b000200 | prose | pages [9] -->
3. The camera on a drone (if it has one) is a two megapixel camera (a 1080P lens).

<!-- b000201 | prose | pages [9] -->
4. The resolution of road detection is one meter.

<!-- b000202 | prose | pages [9, 10] -->
We see  tan(θ + ∆θ) = rview/20 , tan θ = (rview −1)/20 where • θ is the camera’s forward viewing angle;

<!-- b000203 | furniture | pages [10] -->
Team # 1908286

<!-- b000204 | furniture | pages [10] -->
Page 9 of 22

<!-- b000206 | prose | pages [10] -->
• ∆θ is the smallest resolution angle;

<!-- b000207 | prose | pages [10] -->
• rview is the maximum viewing radius.

<!-- b000208 | prose | pages [10] -->
For a two megapixel camera, we have ∆θ = 3 × 10−3rad. Plugging it into (7), we obtain

<!-- b000209 | prose | pages [10] -->
 θ = 1.322 rad rview = 79.7 m .

<!-- b000210 | prose | pages [10] -->
Since rview is close to 100 m, we can divide the island map into grid on the order of one hundred meters, as is shown in Figure[ÍijÆˇn]. Every grid covers a 100 m × 100 m square. Cor- responding to the longitude and latitude,(x, y) is the grid point coordinates of the position.

<!-- b000211 | heading | pages [10] -->
4.2 Geographical Features

<!-- b000212 | prose | pages [10] -->
We divide the location selection problem into two major parts Transport and Reconnais- sance. Then we decide that the information of highway, population, geographic and medical are important to Transport and Reconnaissance. Using the map in the attachment and from Puerto Rico Maps [4], we ﬁnd seven features for the four types of information, see Table 2.

<!-- b000213 | caption | pages [10] -->
Table 2: Features (FO is the Feather Order)

<!-- b000214 | prose | pages [10] -->
FO 1 2 3 4 5 6 7 Hospital High Main Highways Population location feature(FO) population Harbours Altitude highways & roads distribution & medical areas needs

<!-- b000215 | prose | pages [10] -->
For a certain position, Feature1 means the main highways. Feature 2 means the highways we extract from attachment 1. Feature 3 means the density of population [4]. Feature4 means high population areas from the given map. Feature 5 means the distance from harbors. [3] Feature 6 means the altitude. Feature 7 means the index considering transporting MEDs.

<!-- b000216 | prose | pages [10] -->
The feature maps are shown in Figure 4. Note that all feature maps are normalized, so that for every map, the sum of all values is 1 :

<!-- b000217 | prose | pages [10] -->
X X Feature(FO, x, y), ∀FO ∈{Z|1 ≤FO ≤7}, x y

<!-- b000218 | prose | pages [10] -->
where Feature(FO, x, y) is the geographical distribution function of featureFO.

<!-- b000219 | prose | pages [10] -->
The weight of hospital j

<!-- b000220 | prose | pages [10] -->
3 X MedWighti × MedNumberji HOSj = i=1

<!-- b000221 | prose | pages [10] -->
We assign the values in hospital map.

<!-- b000222 | prose | pages [10] -->
We calculate Transport cost for MEDj by Demand number for MEDj:

<!-- b000223 | prose | pages [10, 11] -->
3 X MedWeightj = Medj/ Medi i=1 We have MedWeight = (0.2949 0.2681 0.4369)T j = 1, 2, 3 (8)

<!-- b000224 | furniture | pages [11] -->
Team # 1908286

<!-- b000225 | furniture | pages [11] -->
Page 10 of 22

<!-- b000227 | prose | pages [11] -->
From (8) we see MedWeight2 is smallest, because MED 2 has the least demand.

<!-- b000228 | heading | pages [11] -->
4.3 Singal Location Determination

<!-- b000229 | heading | pages [11] -->
4.3.1 Detail Information of TI and RI

<!-- b000230 | prose | pages [11] -->
T Idetail is an evaluation index for Drone Type i of feature FO in position p1(x, y) and evaluates the detailed transport capability. Let p1 be the target position for Cargo Container. Let p2 be the corresponding point in feature map, we have

<!-- b000231 | prose | pages [11] -->
X TIdetail(i, FO, p1) = TIα(i, p1, p2)Feature(FO, p2).

<!-- b000232 | prose | pages [11] -->
p2

<!-- b000233 | prose | pages [11] -->
Similarly, RIdetail(i, FO, p1) = P p2 RIα(i, p1, p2)Feature(FO, p2).

<!-- b000234 | prose | pages [11] -->
T Iα is a function of i, p1 and p2:

<!-- b000235 | prose | pages [11] -->
TIα(i, p1, p2) = TIdistance(i, p1, p2)TIcover(i)TCI(i)

<!-- b000236 | prose | pages [11] -->
Similarly, RIα(i, p1, p2) = RIdistance(i, p1, p2)RIcover(i)RCI(i)

<!-- b000237 | prose | pages [11] -->
T Idistance measures Transporting Index with ﬂight distance:

<!-- b000238 | prose | pages [11] -->
1 −dis(p1,p2)  DIS(i) βTI, dis < DIS TIdistance = , (9) 0, otherwise

<!-- b000239 | prose | pages [11] -->
where

<!-- b000240 | prose | pages [11] -->
• dis(p1, p2) is the distance between p1, p2;

<!-- b000241 | prose | pages [11] -->
• DIS(i) is the longest ﬂight distance.

<!-- b000242 | prose | pages [11] -->
DIS(i) = α × Speed × Flight Time (No Cargo), see(2) (10)

<!-- b000243 | prose | pages [11] -->
The function (9) shows that closer points are more important within coverage area. βTI = 0.2 produces a linear transformation.

<!-- b000244 | prose | pages [11] -->
Similarly, 1 −(1 −dis(p1,p2)  DIS(i) )βRI, dis < DIS RIdistance = , (11) 0, otherwise

<!-- b000245 | prose | pages [11] -->
where βRI = 0.2. βRI produces a linear transformation. Compare (9) and (11), function (11) shows that in reconnaissance, farther points are preferred, because the close ones can be detect- ed on the way to medical

<!-- b000246 | prose | pages [11] -->
T Icover measures Transporting Index with coverage area. The effectiveness of each point in coverage area is equally important.

<!-- b000247 | prose | pages [11] -->
TIcover(i) = 1/(π · (DIS(i))2 · β′ TI), (12)

<!-- b000248 | prose | pages [11] -->
where β′ TI is determined by βTI; β′ TI = 13/15.

<!-- b000249 | prose | pages [11, 12] -->
(i) = 1/(π · (DIS(i))2 · β′ β′ Similarly, RIcover RI), RI = 14/15 T CI measures Transporting Index with and Transporting Capability of Drone Type i with unit volume. We computed the result of TCI(i) in matrix TCI (5). Similarly, We calculate RCI1(i) = (DIS(i))2/V (i),where V(i) is the total volume of Type i drones and corresponding Bays. Then we normalize it as RCI(i) = RCI1(i)/ max 1≤p≤7 RCI1(p)

<!-- b000250 | furniture | pages [12] -->
Team # 1908286

<!-- b000251 | furniture | pages [12] -->
Page 11 of 22

<!-- b000253 | prose | pages [12] -->
After we calculate TIdetail(i, FO, x, y) and RIdetail(i, FO, x, y), we should take all features into account and calculate the integrate Transport Index of all features T I(i, x, y):

<!-- b000254 | prose | pages [12] -->
X wTI(FO) · TIdetail(i, FO, x, y) TI(i, x, y) = (13) FO Similarly, RI(i, x, y) = P FO wRI(FO) · RIdetail(i, FO, x, y). We obtain a Reconnaissance Capa- bility Index matrix 0.0768   1.0000   0.1105     0.1850 RCI = (14)   0.1190     0.1782   0.1194 Matrix (14) shows that Drone B is the best type to detect highways and roads. Note that Drone B is a lot better than the other types.

<!-- b000255 | prose | pages [12] -->
We listed a few results of the detail information of TI and RI based on Puerto Rico case (see Figure 4).

<!-- b000256 | prose | pages [12] -->
(a) Main Highways (b) Highways and Roads (c) Populated Places

<!-- b000257 | prose | pages [12] -->
(d) TI Drone G Main Highways (e) TI Drone G Highways & Roads (f) TI Drone G Populated Places

<!-- b000258 | prose | pages [12] -->
(g) RI Drone E Main Highways (h) RI Drone E Highways &c Roads (i) RI Drone E Populated Places

<!-- b000259 | caption | pages [12] -->
Figure 4: Samples of Detail Information of TI and RI

<!-- b000260 | heading | pages [12] -->
4.3.2 TI and RI

<!-- b000261 | prose | pages [12] -->
To determine the weight of different features, we employ Analytic Hierarchy Process (AHP). Since those features in Table 2 have different effects on TI and RI, we use AHP twice for TI and RI. The comparison matrices are listed below:

<!-- b000262 | furniture | pages [13] -->
Team # 1908286

<!-- b000263 | furniture | pages [13] -->
Page 12 of 22

<!-- b000264 | prose | pages [13] -->
(a) Comparison Matrix For TI (b) Comparison Matrix For RI

<!-- b000265 | prose | pages [13] -->
To test the consistency of the matrices, we calculate the Consistency Ratio (CR), which is deﬁned as the ratio of Consistency Index (CI) to Average Random Consistency Index (RI′). n = 4 , RI′ = 0.90, CR = (λmax −n)/(n −1). For TI, CI = 0.0532, CR = 0.0598 < 0.1. For RI, CI = 0.0526, CR = 0.0591 < 0.1.so the consistency of the matrices is conﬁrmed.

<!-- b000266 | prose | pages [13] -->
As is indicated in Figure 6, for Transporting Index, Medical information is the most im- portant factor weighting 67.03%. That is because hospital destination of a Drone transporting MEDs. For Reconnaissance Index, highway information take up the highest at 60.11%. One possible reason is that the ﬂight distance of Drones is limited. Drones must get close enough to detect highways.

<!-- b000267 | prose | pages [13] -->
Then we put the weight terms into (13) and (4.3.1), and get TI and RI (see Figure5).

<!-- b000268 | prose | pages [13] -->
(c) TI Drone B (d) TI Drone E (e) TI Drone G

<!-- b000269 | prose | pages [13] -->
(f) RI Drone B (g) RI Drone E (h) RI Drone G

<!-- b000270 | caption | pages [13] -->
Figure 5: Samples of TI and RI

<!-- b000271 | caption | pages [13] -->
Figure 6: Sections and their weight when determining location using AHP

<!-- b000272 | furniture | pages [14] -->
Team # 1908286

<!-- b000273 | furniture | pages [14] -->
Page 13 of 22

<!-- b000274 | heading | pages [14] -->
4.3.3 Efﬁciency Evaluation

<!-- b000275 | prose | pages [14] -->
To show the relative relationship between TI and RI, we introduce an important parameter λ as the transport objective coefﬁcient. 0 ≤λ ≤1. λ shows the importance of transport. The bigger λ is, the more important transport is.

<!-- b000276 | prose | pages [14] -->
The location selection problem is a multi-objective programming problem. We simplify it to a single-objective-programming by using λ. Considering transport and reconnaissance, our objective function is the overall efﬁciency:

<!-- b000277 | prose | pages [14] -->
ALLRI1−λ E = TIλ ALL, (15)

<!-- b000278 | prose | pages [14] -->
In function (15),we deﬁne the Transport Index for all types of drones:

<!-- b000279 | prose | pages [14] -->
7 X v(i) · TI(i), TIALL = (16) i=1 where v(i) is the volume percentage of Type i drones and corresponding Bays in all types. Since v(i) = V (i)/ P7 p=1 V (p), we have P7 i=1 v(i) = 1.

<!-- b000280 | prose | pages [14] -->
Similarly, RIALL is the RI for all types of drones: RIALL = P7 i=1 v(i) · RI(i)

<!-- b000281 | prose | pages [14] -->
We compute the Best Efﬁciency for each position (x, y). Our programming problem can be stated as ALLRI1−λ E = TIλ max ALL 7 X v(i) = 1 s.t.

<!-- b000282 | prose | pages [14] -->
i=1 ∀i ∈{Z|1 ≤i ≤7} v(i) ≥0,

<!-- b000283 | prose | pages [14] -->
(a) lambda = 0.2 (b) lambda = 0.4 (c) lambda = 0.5

<!-- b000284 | prose | pages [14] -->
(d) lambda = 0.6 (e) lambda = 0.8 (f) lambda = 1.0

<!-- b000285 | caption | pages [14] -->
Figure 7: Single Location Determination Based on Different λ Values

<!-- b000286 | prose | pages [14] -->
We apply this method to the Puerto Rico situation (see Figure 7).

<!-- b000287 | heading | pages [14] -->
4.4 Multiple Locations Determination

<!-- b000288 | prose | pages [14] -->
Selecting multiple best locations is a dynamic programming problem. Each location selec- tion can effect the new selection. To show the effect,we set the two following rules:

<!-- b000289 | furniture | pages [15] -->
Team # 1908286

<!-- b000290 | furniture | pages [15] -->
Page 14 of 22

<!-- b000291 | prose | pages [15] -->
• Effects on Transportation. After each selection, we assume the Container satisﬁes 1/3 of all MEDs demands if its Drones and MED sullplies allow. Note that the container should ﬁrst provide MEDs to nearby medical centers. And we should renormalize the the Medical Infromation feature.

<!-- b000292 | prose | pages [15] -->
• Effects on Reconnaissance. After each selection, we assume Drones of the Container can detect all highways within the container’s Maximun Reconnaissance Scope. High- way Information feature within that scope should decrease. We will multiply them by a coefﬁcient of r0 = 0.1.

<!-- b000293 | heading | pages [15] -->
4.5 Results

<!-- b000294 | caption | pages [15] -->
Table 3: The Result of Multiple Locations Determination Modle(λ = 0.5)

<!-- b000295 | caption | pages [15] -->
Table 4: The Location Selection Related To λ

<!-- b000296 | heading | pages [15] -->
5 Fleet Arrange Model

<!-- b000297 | heading | pages [15] -->
5.1 Schedule Arrangement Model

<!-- b000298 | heading | pages [15] -->
5.1.1 Satisfactory Solution on MEDs

<!-- b000299 | prose | pages [15] -->
We maximize the ability of DroneGo ﬂeet to satisfy the anticipated Medical Package De- mand. According to the choices of drone type given in Part B, we will only employ drone B, E and G to transport MEDs. First, we search satisfactory solution on how to put MEDs into a Bay. Then we can use those schemes to assemble a best schedule so that we maximize the ability of DroneGo ﬂeet to satisfy the anticipated Medical Package Demand.

<!-- b000300 | prose | pages [15] -->
We will use the following notations in this section:

<!-- b000301 | prose | pages [15, 16] -->
• MEDweight is the weight of MED j; j • MEDNum is the number of MED j put into a bay in a satisfactory solution; j

<!-- b000302 | furniture | pages [16] -->
Team # 1908286

<!-- b000303 | furniture | pages [16] -->
Page 15 of 22

<!-- b000305 | prose | pages [16] -->
• Drone 1,2 and 3 correspond to B,E and G, respectively;

<!-- b000306 | prose | pages [16] -->
• kij is the jth scheme for Type i drones;

<!-- b000307 | prose | pages [16] -->
• Ki = (ki1 ki2 . . . kir)T is the set of all the satisfactory schemes for drone i.

<!-- b000308 | prose | pages [16] -->
By using the Transport Capability matrix (4) in Section 4.3, we demonstrate that for drone B, E and G, only Max Payload Capacity (MPC) will play a decisive role on whether a scheme is fea- sible. Actually, satisfactory solutions must be at the feasible region. Consequently, satisfactory solution for a Type i drone should subject to the stated constraints:

<!-- b000309 | prose | pages [16] -->
3 X MEDweight × MEDnum ≤MPCi j j 1

<!-- b000310 | prose | pages [16] -->
3 X MEDweight MEDweight ×MEDnum + min > MPCi j j j j 1

<!-- b000311 | prose | pages [16] -->
We use integer programming method to search feasible solutions.

<!-- b000312 | prose | pages [16] -->
ki1 is the 1st solution.

<!-- b000313 | prose | pages [16] -->
Eventually we get K1,K2 K3. for drone 1 2 3 respectively has 3,27,44 satisfactory schemes.

<!-- b000314 | heading | pages [16] -->
5.1.2 Maximum Effective Days Model

<!-- b000315 | prose | pages [16] -->
Now we have known all satisfactory schemes on how to put MEDs into a Bay for drone B,E and G.To evaluate the the ability of DroneGo ﬂeet to transport Emergency Medical Package,we make an assumption: Every delivery location’s need for MED should be satisﬁed equally.

<!-- b000316 | prose | pages [16] -->
Since delivery location has the certain anticipated Medical Package Demand everyday,we can calculate a Maximum supply days if the type and number of drone and the schemes for each corresponding drone are determined.

<!-- b000317 | prose | pages [16] -->
we will use the following notations:

<!-- b000318 | prose | pages [16] -->
• MEDneed = (mj1 mj2 mj3) is the need of sth delivery location within the range of trans- s portation. mj1, mj2, mj3 is corresponding to the number of MED1,2,3.

<!-- b000319 | prose | pages [16] -->
• Numirs is the number of drone i which carry out the rth scheme ;

<!-- b000320 | prose | pages [16] -->
• |Ri| is the number of satisfactory schemes for drone i;

<!-- b000321 | prose | pages [16] -->
• S is the number of delivery location;

<!-- b000322 | prose | pages [16] -->
• Dayss is Maximum supply days for delivery position s.

<!-- b000323 | prose | pages [16] -->
Here is the Linear Programming model. For delivery position s,

<!-- b000324 | prose | pages [16] -->
| Ri | 3 X X Numirs kis ≥Dayss × MEDr max r i=1 |S| | Ri | X X Numirs = Qk s.t.

<!-- b000325 | prose | pages [16, 17] -->
s r Numirs ≥0 | Ri | 3P P Numirs kis r i=1 1≤s≤|S|{Dayss} = min max Dayseffective = min 1≤s≤|S|( ) MEDs |S| | Ri | X X Numirs = Qk s.t.

<!-- b000326 | furniture | pages [17] -->
Team # 1908286

<!-- b000327 | furniture | pages [17] -->
Page 16 of 22

<!-- b000329 | prose | pages [17] -->
s r Numirs ≥0

<!-- b000330 | caption | pages [17] -->
Table 5: Optimal Drone Payload Packing Conﬁgurations And Drone Schedule

<!-- b000331 | prose | pages [17] -->
Through the use of integer linear programming, we can ﬁnd the optimal drone payload packing conﬁgurations by traversing all possible combinations of the satisﬁed scheme when the number of each drone type and delivery locations’ MEDs need are certain. Now we apply the Schedule Arrangement Model to the situation in Table 3. The result indicates that we can get an optimal solution in a given situation. Moreover, the result directly gives the drone payload packing conﬁgurations for every drone.

<!-- b000332 | heading | pages [17] -->
5.2 Drone Route Planning Model

<!-- b000333 | prose | pages [17] -->
Now that we have conﬁrmed the drone delivery plan. Under this scheme, the basic delivery strategy of each drone has been determined. Since we assume that each drone will not move once it has delivered the goods, the extra distance of the drone other than delivery can be used to detect the highways and roads. We can use a Greedy Search Algorithm to arrange individual drones. The algorithm is shown in Figure 8:

<!-- b000334 | furniture | pages [18] -->
Team # 1908286

<!-- b000335 | furniture | pages [18] -->
Page 17 of 22

<!-- b000336 | caption | pages [18] -->
Figure 8: Individual Drone Route Planning Algorithm

<!-- b000337 | prose | pages [18] -->
• Searching nearby, that is, searching the nearest road. Since most roads are continuous, the nearby search algorithm is simple, easy to operate and efﬁcient.

<!-- b000338 | prose | pages [18] -->
• The searched road should not be searched any more, and it should be deleted from the overall search targets.

<!-- b000339 | prose | pages [18] -->
• Delivery ﬁrst strategy, because delivery is urgent, so if you choose between delivery and search, then you must choose delivery.

<!-- b000340 | prose | pages [18] -->
In the algorithm, we call the hospital where the drones need to deliver as the target location. The keys of the algorithm are listed as follows Searching nearby, that is, searching the nearest road. Since most roads are continuous, the nearby search algorithm is simple, easy to operate and efﬁcient. The searched road should not be searched any more, and it should be deleted from the overall search targets. Delivery ﬁrst strategy, because delivery is urgent, so if you choose between delivery and search, then you must choose delivery.

<!-- b000341 | prose | pages [18] -->
For the drone ﬂeet as a whole, we need to select different drones for reconnaissance. Since short-range drones cannot detect points far from the targets and containers, we should priori- tize the path of these drones to maximize their reconnaissance potential. The number of drugs required by the hospital will be changed each time the drone delivers the goods, and the next delivery mission of the drone will also be changed accordingly. More speciﬁcally, if the delivery demand of a certain drug in a hospital has been met, the drone loaded with that drug should not be used as the target place.

<!-- b000342 | prose | pages [18] -->
Further, to improve the algorithm, we can ﬁnd that among the three selected drones, drone B, E and G, the transport capacity of drone B is the weakest, but its reconnaissance capability is the strongest. Even if we deduct the medicine delivery amount of drone B, the effect on the overall drug delivery amount is not signiﬁcant. Therefore, we should use drone B only for reconnaissance. If we apply the above strategy to the 3 container transport model with λ == 0.5, we can obtain the results of transportation path in Figure 10.

<!-- b000343 | furniture | pages [19] -->
Team # 1908286

<!-- b000344 | furniture | pages [19] -->
Page 18 of 22

<!-- b000345 | caption | pages [19] -->
Figure 9: Drone Fleet Route Planning Algorithm

<!-- b000346 | prose | pages [19] -->
Under the model of λ = 0.5, our road reconnaissance coverage for Puerto Rico reached 59.86% (see Figure 10). We can ﬁnd that, in order to meet the needs of the three hospitals n- earby Puerto Rico ˛a´r capital, we use a lot of drones to transport medicine, so the reconnaissance coverage rate of this area is not high, however, in the area of transport demand is relatively small, the container 3, our reconnaissance coverage is very high. This result is consistent with our hypothesis that λ = 0.5, which means reconnaissance and transportation is equally im- portant. At the same time, since we consider the range reduction of drone affected by various reasons, that is, the ratio between the total range used and the ideal total range calculated is α = 0.9, the reconnaissance capability of drone ﬂeet may be better in actual use.

<!-- b000347 | prose | pages [19] -->
(a) Container 1(C1) (b) C1 drone B (c) C1 drone G

<!-- b000348 | prose | pages [19] -->
(d) Container 3(C3) (e) C3 drone B (f) C3 drone E

<!-- b000349 | prose | pages [19] -->
(g) Container 2(C2) (h) C2 drone E (i) All(routes under reconnaissance in black, undetectcted in gray)

<!-- b000350 | caption | pages [19] -->
Figure 10: Drone Routes(the yellow line in the ﬁgure is the ﬂight path of this drone, and the blue dot at

<!-- b000351 | prose | pages [19] -->
the end of the yellow line represents the ﬁnal position of the drone)

<!-- b000352 | furniture | pages [20] -->
Team # 1908286

<!-- b000353 | furniture | pages [20] -->
Page 19 of 22

<!-- b000354 | heading | pages [20] -->
6 Sensitivity Analysis

<!-- b000355 | prose | pages [20] -->
As is shown on Geospatial Analysis Model, we use AHP to get the weight vector of wTI and the weight vector of wRI. However, AHP is based on subjective inputs to some extent. Aiming to determine how robust our rankings are in the AHP process, we use the following proportionality equation for adjusting weights:

<!-- b000356 | prose | pages [20] -->
j = 1 −w′ p w′ wj, 1 −wp

<!-- b000357 | prose | pages [20] -->
where w′ j is the new weight, wp the original largest weight of the criterion to be adjusted,and w′ p the value after the criterion is adjusted.

<!-- b000358 | caption | pages [20] -->
Table 6: Sensitivity Analysis Result of AHP

<!-- b000359 | prose | pages [20] -->
We respectively apply a −10%, −20%, +10%, +20% variation to the wTI and wRI,and record the the results under each circumstance, respectively. The following is the new results:

<!-- b000360 | prose | pages [20] -->
In the table above, note that Latitude and longitude are used to indicate location and dis- tance between original and new position is shown if position changes. We can conclude that

<!-- b000361 | prose | pages [20] -->
• Above all, the table shows the strong robustness of our model.It is conspicuous that the results only change slightly,notwithstanding we let wDI or wTI have a sizable change.

<!-- b000362 | prose | pages [20] -->
• Remarkably, some positions of container and drone proportion don ˛a´rt vary with different wTI and wRI. Via analyzing the corresponding data, a reasonable explanation is that this position or proportion has much better performance than those adjacent choices.

<!-- b000363 | heading | pages [20] -->
7 Strengths and Weaknesses

<!-- b000364 | heading | pages [20] -->
7.1 Strengths

<!-- b000365 | prose | pages [20, 21] -->
• A model based on Three Space Division Model and improved Monte-Carlo Simulation can solve the problem of packing restrictions in the transportation of goods and have high realizability by considering weight and volume limitations.

<!-- b000366 | furniture | pages [21] -->
Team # 1908286

<!-- b000367 | furniture | pages [21] -->
Page 20 of 22

<!-- b000369 | prose | pages [21] -->
• Based on the AHP method,the Geospatial Analysis Model fully considers the inﬂuence of many possible factors on the selection of container drop location , including transporta- tion, population, geography and medical information. Therefore, the result of the model is highly credible.

<!-- b000370 | prose | pages [21] -->
• Complex integer programming model and improved greedy algorithm is able to give the drone schedule planning and route planning quickly and accurately.

<!-- b000371 | prose | pages [21] -->
• Flexibility and adaptability are also advantages of the Location Determination Model.

<!-- b000372 | prose | pages [21] -->
When the company change its strategy, new decisions can be quickly derived without modifying the algorithm.

<!-- b000373 | heading | pages [21] -->
7.2 Weaknesses

<!-- b000374 | prose | pages [21] -->
• While utilizing improved Monte-Carlo Simulation,the quality of the result may not achieve our high expectation.

<!-- b000375 | prose | pages [21] -->
• The rule of how to transport MEDs to different delivery position is uncertain.It can be further improved to meet different actual needs

<!-- b000376 | prose | pages [21] -->
• The correctness of our conclusions is related to the accuracy of the data collected and the estimates of transportation, population, geography and medical information.

<!-- b000377 | heading | pages [21] -->
8 Conclusion

<!-- b000378 | prose | pages [21] -->
To help with post-disaster relief, we designed a prototype of the DroneGo. The system estab- lishes the Drone Transport Model and Drone Survey Model, taking into account the characteris- tics of drone, medicine and container such as weight and size, as well as a variety of geographic information such as road information, population information, rescue information and medical information. We conclude that the Transportation Capability of Drone G is the strongest and the Reconnaissance Capability of drone B is the strongest. When users considered medicine delivery to be as important as road reconnaissance, we got results that the medicine delivery can be maintained for more than two months and road reconnaissance coverage reached nearly 60%.

<!-- b000379 | prose | pages [21] -->
To further provide advice to the DroneGo users, in our system, users can also input a d- ifferent transport/reconnaissance parameter, i.e., different emphasis on transport and recon- naissance. In this case, our DroneGo system can provide different ﬂeet conﬁgurations and container drop points to meet their needs. Meanwhile we construct an efﬁcient schedule ar- rangement and route arrangement model of drones using an integer programming model and an improved greedy algorithm, so the drone ﬂeet can be auto arranged.

<!-- b000380 | heading | pages [21] -->
References

<!-- b000381 | references | pages [21] -->
[1] Wikipedia, “Hurricane maria,” https://en.wikipedia.org/wiki/Hurricane_Maria#Puerto_

<!-- b000382 | references | pages [21] -->
Rico_3, accessed January 29, 2019.

<!-- b000383 | references | pages [21] -->
[2] M. Winn, “We need to be using drones to rescue harvey victims,” https://www.cia.gov/

<!-- b000384 | references | pages [21] -->
library/publications/the-world-factbook/geos/rq.html#Geo, accessed January 29, 2019.

<!-- b000385 | references | pages [21] -->
[3] CIA, “Central america ::

<!-- b000386 | references | pages [21] -->
Puerto rico,” https://w3techs.com/technologies/overview/

<!-- b000387 | references | pages [21] -->
content_language/all, accessed January 29, 2019.

<!-- b000388 | furniture | pages [22] -->
Team # 1908286

<!-- b000389 | furniture | pages [22] -->
Page 21 of 22

<!-- b000390 | references | pages [22] -->
[4] “Puerto rico maps,” http://www.topuertorico.org/maps.shtml, accessed January 29, 2019.

<!-- b000391 | references | pages [22] -->
Memo to CEO of HELP, Inc.

<!-- b000392 | references | pages [22] -->
To: HELP, Inc. CEO

<!-- b000393 | references | pages [22] -->
From: Team 1908286

<!-- b000394 | references | pages [22] -->
Date: January 28, 2019

<!-- b000395 | references | pages [22] -->
Subject: Study of DroneGo disaster response system based on Puerto Rico hurricane in 2017

<!-- b000396 | references | pages [22] -->
In the post-disaster relief, unmanned aerial vehicles, also called drones, are not limited by

<!-- b000397 | references | pages [22] -->
road conditions, so they can quickly provide medicines and other urgent materials to the af-

<!-- b000398 | references | pages [22] -->
fected areas, which can alleviate the shortage of local post-disaster medical drugs. Meanwhile,

<!-- b000399 | references | pages [22] -->
drones can also be used to survey the highways and roads situation and support post-disaster

<!-- b000400 | references | pages [22] -->
relief. We aim to develop a "DroneGo" disaster response system based on a drone ﬂeet, which

<!-- b000401 | references | pages [22] -->
can be used to provide medical assistance to the people in the disaster area, as well as to provide

<!-- b000402 | references | pages [22] -->
information on the disaster situation to the rescue workers.

<!-- b000403 | references | pages [22] -->
In 2017, the worst hurricane to ever hit the United States territory of Puerto Rico left the

<!-- b000404 | references | pages [22] -->
island with severe damage. The DroneGo system needs to be designed to better help NGOs

<!-- b000405 | references | pages [22] -->
use drones for post-disaster exploration and drug delivery missions in similar disasters. The

<!-- b000406 | references | pages [22] -->
system can reasonably plan the selection of a certain drone ﬂeet, container delivery location,

<!-- b000407 | references | pages [22] -->
drone medicine delivery schedule and route planning of exploration road based on the known

<!-- b000408 | references | pages [22] -->
properties of drone, medicine and containers, as well as, medical needs and highways and

<!-- b000409 | references | pages [22] -->
roads reconnaissance needs in disaster areas and other relevant information.

<!-- b000410 | references | pages [22] -->
We designed a prototype of the DroneGo system based on ofﬁcial drone, medicine and con-

<!-- b000411 | references | pages [22] -->
tainer information and applied it to the disaster situation in Puerto Rico. When users con-

<!-- b000412 | references | pages [22] -->
sidered medicine delivery to be as important as road reconnaissance, we got results that the

<!-- b000413 | references | pages [22] -->
medicine delivery can be maintained for more than two months and road reconnaissance cov-

<!-- b000414 | references | pages [22] -->
erage reached nearly 60%. Users can also input a different transport/reconnaissance parameter,

<!-- b000415 | references | pages [22] -->
i.e., different emphasis on transport and reconnaissance. At the same time, our DroneGo sys-

<!-- b000416 | references | pages [22] -->
tem can also quickly obtain the program of drone ﬂeet composition, delivery and arrangement.

<!-- b000417 | references | pages [22] -->
In addition, our DroneGo system can also form a model for drone transportation and recon-

<!-- b000418 | references | pages [22] -->
naissance evaluation for more geographic information (such as population distribution, road

<!-- b000419 | references | pages [22] -->
information, rescue information, medical information, etc.). The approach we are using can be

<!-- b000420 | references | pages [22] -->
further reﬁned and extended to develop a post-disaster rescue drone ﬂeet arrangement system.

<!-- b000421 | references | pages [22] -->
According to our ˛aˇrDroneGo ˛a´s system, we can develop a software (see Figure 11), which will

<!-- b000422 | references | pages [22] -->
greatly help post-disaster relief missions.

<!-- b000423 | references | pages [22] -->
Firstly, for the loading problem of drone ﬂeet, we use an indicator of drone ﬂeet transport

<!-- b000424 | references | pages [22] -->
capacity to form our drone Transport Capacity Model to solve the problem of maximizing the

<!-- b000425 | references | pages [22] -->
drone ﬂeet medicine transport capacity when the disaster location is unknown. Among them,

<!-- b000426 | references | pages [22] -->
the biggest obstacle we encountered is the limitation of goods packing. We developed an al-

<!-- b000427 | references | pages [22] -->
gorithm based on the three-space division method and an improved Monte Carlo simulation,

<!-- b000428 | references | pages [22] -->
which can better solve this problem in a short time. At the same time, we also consider the

<!-- b000429 | references | pages [22] -->
weight, volume and other restrictions, so that our results are highly achievable. In terms of

<!-- b000430 | references | pages [22] -->
speciﬁc solutions, Drone G is considered to be the most transportable.

<!-- b000431 | references | pages [22] -->
Secondly, if we got the information of the disaster area, we can use our DroneGo system

<!-- b000432 | references | pages [22] -->
based on spatial geographic information, which integrated the previous drone Transportation

<!-- b000433 | references | pages [22] -->
Capability Model and a drone Reconnaissance Capability Model. Combining with different ge-

<!-- b000434 | references | pages [22] -->
ographic information, we used Analytic Hierarchy Process (AHP) to analyze the distribution

<!-- b000435 | furniture | pages [23] -->
Team # 1908286

<!-- b000436 | furniture | pages [23] -->
Page 22 of 22

<!-- b000437 | references | pages [23] -->
of drone transportation capability and reconnaissance capability along with the location. In or-

<!-- b000438 | references | pages [23] -->
der to better balance ˛aˇrDroneGo ˛a´s system users to transportation capacity and reconnaissance

<!-- b000439 | references | pages [23] -->
ability of different needs, we set up an overall Efﬁciency Evaluation Model, using the nonlinear

<!-- b000440 | references | pages [23] -->
programming and dynamic programming to get the speciﬁc conﬁguration of the drone ﬂeet

<!-- b000441 | references | pages [23] -->
and container drop point selection. In the system, users can adjust the transportation / recon-

<!-- b000442 | references | pages [23] -->
naissance parameter to get the response of different targets. Through the case study of Puerto

<!-- b000443 | references | pages [23] -->
Rico, we are able to further verify the feasibility of our system.

<!-- b000444 | references | pages [23] -->
We use an integer programming model and an improved greedy algorithm to construct

<!-- b000445 | references | pages [23] -->
the Schedule Arrangement Model and Route Arrangement Model of drones. In drone ﬂeet

<!-- b000446 | references | pages [23] -->
and containers delivery plan chosen by our DroneGo system, we got the medicine transport

<!-- b000447 | references | pages [23] -->
to maintain nearly two months, as well as the results of road reconnaissance coverage reached

<!-- b000448 | references | pages [23] -->
nearly 60%. Finally, the sensitivity of AHP is analyzed to verify the robustness of the system.

<!-- b000449 | references | pages [23] -->
If you want to know more details, please read our essay about this subject. We will be

<!-- b000450 | references | pages [23] -->
glad to discuss more about DroneGo system with you in the future and follow through on any

<!-- b000451 | references | pages [23] -->
decisions you make.

<!-- b000452 | references | pages [23] -->
Attached: DroneGo system software frame, January 28 2019

<!-- b000453 | caption | pages [23] -->
Figure 11: DroneGo system software frame
