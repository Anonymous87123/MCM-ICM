# P-B-2019-1908286-37248927

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
1908286

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
2019 MCM/ICM Summary Sheet

<!-- b000016 | prose | pages [1] -->
Hurricane Maria Damage left Puerto Rico people a lot of pain and devastation. HELP,Inc., an NGO, is attempting to improve its response capabilities by designing a transportable disaster response system called "DroneGo".

<!-- b000017 | prose | pages [1] -->
In order to better assess the transport capability of the drone ﬂeet, we establish a Transport Capability Evaluation Model of the drone ﬂeet, so that we can maximize the medicine transportation capability of the drone ﬂeet when the disaster location is unknown. In this model, we use the algorithm of linear programming to solve the limitations of volume, weight and other simple factors. After that, we used an algorithm based on three-space segmentation and improved Monte Carlo simulation to solve the size limitation of the objects. As a result, we obtain a reliable evaluation of the transport capability of drones, and it can be found that among the drones, the transportation capability of drone G is the strongest.

<!-- b000018 | prose | pages [1] -->
Through the research on the reconnaissance method of the drones, we get the Reconnaissance Ca- pability Model of the drone ﬂeet. In this model, we ﬁnd that the reconnaissance capability of drone B is the strongest. Based on these two models (TCM & RCM) and abundant geographic information, we developed a Geospatial Analysis Model. We employ the Analytical Hierarchy Process (AHP) in the space of all position, obtaining a spatial distribution of drone ﬂeet ˛a´rs transportation capability and re- connaissance capability. Then, we establish an overall Efﬁciency Evaluation Model for the drone ﬂeet, using a nonlinear programming with a variable parameter to obtain the optimal solution of the drone ﬂeet overall efﬁciency and its spatial location. Consequently, we can determine a conﬁguration of the drone ﬂeet and each container’s drop point. DroneGo users can also adjust the variable parameter de- pending on whether they care more about their ﬂeet ˛a´rs transport capability or reconnaissance capability to determine different options. For the problem of multiple containers, we use a dynamic programming rule that allows users to arrange multiple containers.

<!-- b000019 | prose | pages [1] -->
In considering that the transportation capability of the drone ﬂeet is as important as the reconnais- sance capability, we get results that the medicine delivery can be maintained for more than two months and road reconnaissance coverage can reach nearly 60%. Meanwhile we construct an efﬁcient Schedule Arrangement Model and Route Arrangement Model of drones using an integer programming model and an improved greedy algorithm, so that the drone ﬂeet can be auto arranged.

<!-- b000020 | prose | pages [1] -->
The sensitivity analysis shows the strong robustness of our model. Meanwhile, we further discuss the possibility of developing a DroneGo system software, and provide practicable advice to the HELP, Inc. CEO.

<!-- b000021 | keywords | pages [1] -->
Keywords: Multi-Objective Programming,Dynamic Programming, Drone Rescue Model, AHP

<!-- b000022 | furniture | pages [2] -->
Team # 1908286

<!-- b000023 | furniture | pages [2] -->
Page 1 of 22

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | heading | pages [2] -->
Introduction

<!-- b000027 | prose | pages [2] -->
2

<!-- b000028 | heading | pages [2] -->
Assumptions and Justiﬁcation

<!-- b000029 | prose | pages [2] -->
2

<!-- b000030 | prose | pages [2] -->
2

<!-- b000031 | heading | pages [2] -->
Transportation Capability Evaluation Model

<!-- b000032 | prose | pages [2] -->
3 3 Assumptions in This Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 3 Three Space Division Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 Putting MEDs into Bays 5 Drone Transport Capability Model . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 6 Putting Drones and Bays into Cargo Conatainers . . . . . . . . . . . . . . . . . . . 3.5 7 Monte-Carlo Simulation And Results . . . . . . . . . . . . . . . . . . . . . . . . . . 3.6

<!-- b000033 | prose | pages [2] -->
4

<!-- b000034 | heading | pages [2] -->
Geospatial Analysis Model

<!-- b000035 | prose | pages [2] -->
7

<!-- b000036 | prose | pages [2] -->
8 Drone Reconnaissance Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 8 Geographical Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Singal Location Determination 10 . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 Multiple Locations Determination 13 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5

<!-- b000037 | prose | pages [2] -->
5

<!-- b000038 | heading | pages [2] -->
Fleet Arrange Model

<!-- b000039 | prose | pages [2] -->
14

<!-- b000040 | prose | pages [2] -->
14 Schedule Arrangement Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 14 Drone Route Planning Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2

<!-- b000041 | prose | pages [2] -->
6

<!-- b000042 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000043 | prose | pages [2] -->
7

<!-- b000044 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000045 | prose | pages [2] -->
16

<!-- b000046 | prose | pages [2] -->
19

<!-- b000047 | prose | pages [2] -->
19 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Weaknesses

<!-- b000048 | prose | pages [2] -->
8

<!-- b000049 | heading | pages [2] -->
Conclusion

<!-- b000050 | prose | pages [2] -->
20

<!-- b000051 | prose | pages [2] -->
20

<!-- b000052 | furniture | pages [3] -->
Team # 1908286

<!-- b000053 | furniture | pages [3] -->
Page 2 of 22

<!-- b000054 | prose | pages [3] -->
An optional Design of DroneGo

<!-- b000055 | prose | pages [3] -->
1

<!-- b000056 | heading | pages [3] -->
Introduction

<!-- b000057 | prose | pages [3] -->
People in disaster areas are in great need of timely emergency services. [1] Drones can help a lot in emergency rescue. According to a drone manufacturer DJI [2], drones have saved 59 lives since 2013.

<!-- b000058 | prose | pages [3] -->
In this paper, we will

<!-- b000059 | prose | pages [3] -->
• Analyze three dimensional packing problem and develop Three Space Division Model and improved Monte-Carlo Simulation to solve the problem of packing restrictions in the transportation. • Analyze the transportation capability and detective capability of each Drone type,apply AHP method to considers the inﬂuence of many possible factors on the selection of con- tainer drop location , including transportation, population, geography and medical infor- mation. • Build a model to determine drone payload packing conﬁguration and solve it with a com- plex integer programming quickly and accurately. • Improve greedy algorithm and ﬁgure out the drone route planing quickly and accurately.

<!-- b000060 | prose | pages [3] -->
2

<!-- b000061 | heading | pages [3] -->
Assumptions and Justiﬁcation

<!-- b000062 | prose | pages [3] -->
We make some general assumptions to simplify our model. These assumptions together with corresponding justiﬁcation are listed below:

<!-- b000063 | prose | pages [3] -->
• There are no charging devices for drones. In 2017, Hurricane Maria knocked down 80% of Puerto Rico’s utility poles and all transmission lines. We can infer that electricity are not available on the island. Our Cargo will not include charging equipment or generating set, due to extra weight and inconvenience. • The cargo weight does not inﬂuence the maximum ﬂight distance of a drone. That is, maximum ﬂight distance is exactly the same with or without a cargo. We make the assumption for simplicity. In reality, the weight of a delivery drone is often larger than that of its cargo. It is quite reasonable to neglect the inﬂuence of cargo weight. And this will greatly simply our model. • For each Cargo Container, we will load one tethered Drone (type H). In natural disasters, communication facilities are often affected to various degrees, and emergency communi- cation becomes an urgent need. It can act as an emergency communication base station. Tethered drones will greatly enhance the disaster response capability of DroneGo system. • One drone can carry one drone cargo bay or no bay for every ﬂight. If the drone carries one, it can only deliver the bay to one location. Both of the two types of drone cargo bay are "top loaded", that is, loaded on the top of a drone. If we distribute more than one bay at a ﬂight, connections between cargo bays could be unstable. We can deliver a drone cargo bay to only one place since it is an integral package that cannot be open in transit. • Helicopters can transport cargo containers to any given place in the disaster area. In disaster-affected areas, timely external assistance is urgently needed to restore order. There- fore, we consider air transportation rather than sea transportation. Although Puerto Rico is an island, air transportation will bring adaptability to our model in other situations. • Communication and data transmission of drones are always available. We can achieve telecommunication by radio communication or satellite communication. Drone commu- nication dose not rely on ground devices.

<!-- b000064 | furniture | pages [4] -->
Team # 1908286

<!-- b000065 | furniture | pages [4] -->
Page 3 of 22

<!-- b000066 | prose | pages [4] -->
• For the ith type of drone, its maximum Flight Distance, denoted by Disti is in direct

<!-- b000067 | heading | pages [4] -->
proportion to the product of Speed and FlightTime(No Cargo). From that assumption,

<!-- b000068 | prose | pages [4] -->
we have Disti = α × Speed × Flight Time (No Cargo), where α represents distance-loss coefﬁcient. Here we neglect the effect of weather (especially wind) and different battery and motor of different drones of a speciﬁc type. To determine α, we note that there are mostly mountains with few plains. And Puerto Rico has a mean elevation of 261 m. [3] The high elevation shortens the maximum ﬂight distance. We have α < 1. For simpliﬁcation, we choose α = 0.9.

<!-- b000069 | prose | pages [4] -->
More detailed assumptions will be listed if needed.

<!-- b000070 | prose | pages [4] -->
3

<!-- b000071 | heading | pages [4] -->
Transportation Capability Evaluation Model

<!-- b000072 | prose | pages [4] -->
In this section, we will evaluate transportation ability of each type of drones. For simplicity, we will focus on the need of medical transportation here. We will incorporate road reconnais- sance into our model in Section 5.

<!-- b000073 | prose | pages [4] -->
3.1

<!-- b000074 | heading | pages [4] -->
Assumptions in This Model

<!-- b000075 | prose | pages [4] -->
We will use the following assumptions in this section:

<!-- b000076 | prose | pages [4] -->
• All Cargo Containers(CC), Drone (in shipping containers), Drone Cargo Bays (DCB), and Medical packages (MP) are cuboids. • Drones and Drone Cargo Bays should be placed into Cargo Containers in parallel, which is "parallel placement". That is, the inner subface of Drones or Bays must be par- allel to the corresponding surface of the Cargo Container. There are two reasons. For one thing, the parallel placement is one of the most commonly used packing methods. For another thing, cargos can be easily placed in this way and have a high stability. • The thickness of Drone Cargo Bays can be neglected. • Goods can be arbitrarily rotated, but must still satisfy the "parallel placement" condi- tion. • As is interpreted in the problem description, each Cargo Container’s contents should be packed, so all Medical Packages should be packed in Drone Cargo Bays. We do not consider Medical Packages directly placed in a Cargo Container.

<!-- b000077 | prose | pages [4] -->
3.2

<!-- b000078 | heading | pages [4] -->
Three Space Division Model

<!-- b000079 | prose | pages [4] -->
3.2.1 One Goods Condition

<!-- b000080 | prose | pages [4] -->
To design a packing conﬁguration for DroneGo, we need to put MEDs into Bays and put Bays or Drones into Containers. Due to various kinds of goods in the problem, this is a three- dimensional heterogeneous container loading problem. We use the Three Space Division Method and Monte Carlo Simulation to solve it.

<!-- b000081 | prose | pages [4] -->
Note that we refer to a rectangular container that contains goods as a box. As is shown in Figure 1, L, W and H is the length, width and height of the container, respectively. Similarly, l, w and h is the length, width and height of the cargo, respectively. We set up a Cartesian coordinate at the left bottom vertex of the container. Note that we consider the position of the container is unchanged. We put the cargo into the container, so that two left bottom vertexes coincide. Arrangement problem is a way to think about ways to put the cargo. To put

<!-- b000082 | furniture | pages [5] -->
Team # 1908286

<!-- b000083 | furniture | pages [5] -->
Page 4 of 22

<!-- b000084 | prose | pages [5] -->
h into x, y and z coordinates, we have A3

<!-- b000085 | prose | pages [5] -->
3 = 6. There are six ways to put the cargo inside. That is, there are six possible combinations of the coordinates of the diagonal vertex of the cargo.

<!-- b000086 | caption | pages [5] -->
Figure 1: Three Space Division

<!-- b000087 | prose | pages [5] -->
For every speciﬁc combination, we can see that the rest space in the container are cut into three parts (spaceX, spaceY and spaceZ) , see ﬁgure 1. One possible sequence (shown in Figure 1) to generate the three parts is

<!-- b000088 | heading | pages [5] -->
1. Procedure X: Cut the remaining space using a plane perpendicular to the X-axis and get

<!-- b000089 | prose | pages [5] -->
spaceX.

<!-- b000090 | heading | pages [5] -->
2. Procedure Y: Cut the remaining space using a plane perpendicular to the Y-axis and get

<!-- b000091 | prose | pages [5] -->
spaceY.

<!-- b000092 | heading | pages [5] -->
3. Procedure Z: Cut the remaining space using a plane perpendicular to the Z-axis and get

<!-- b000093 | prose | pages [5] -->
spaceZ.

<!-- b000094 | prose | pages [5] -->
We refer to this sequence as a X-Y-Z sequence. The rest are similar. Arrangement problem is a way to think about the space cutting process. To generate a sequence from procedure X, Y and Z we have A3

<!-- b000095 | prose | pages [5] -->
3 = 6.

<!-- b000096 | prose | pages [5] -->
Thus, if a cargo can be put into the cargo, we have the total cases of three space division: 6 × 6 = 36 Then we consider every new space as a new container. And the three space division process goes on, until the cargo can not be put into any of the existing containers. In this way, we can traverse all situations and ﬁnd the optimal solution for a speciﬁc objective function.

<!-- b000097 | prose | pages [5] -->
3.2.2 Multiple Goods Condition

<!-- b000098 | prose | pages [5] -->
To clarify the problem, we will use the following notations:

<!-- b000099 | prose | pages [5] -->
• K = {1, 2, . . . , |K|} is the set of Boxes’ number; • R = {1, 2, . . . , |R|} is the set of goods’ types; • Mr = {1, 2, . . . , |Mr|} is the set of goods’ number (same type) ; • sB = (L W H)T is Box Size column vector;

<!-- b000100 | prose | pages [5] -->
r = (lr wr hr)T is the rth type of Goods Size column vector; • sG • Xk is the number of goods in the kth box; •

<!-- b000101 | prose | pages [5] -->


<!-- b000102 | prose | pages [5] -->
1, if the mth Goods of Type r is in Box k

<!-- b000103 | prose | pages [5] -->
Ykrm =

<!-- b000104 | prose | pages [5] -->
is an Existing Flag; 0, otherwise

<!-- b000105 | prose | pages [5] -->
• u = (xkrm ykrm zkrm)T is coordinates of the mth goods of Type r in Box k; •

<!-- b000106 | prose | pages [5] -->


<!-- b000107 | prose | pages [5] -->
1, if the length of the mth Goods of Type r is parallel to the x-axis

<!-- b000108 | prose | pages [5] -->
lxrm =

<!-- b000109 | prose | pages [5] -->
0, otherwise

<!-- b000110 | prose | pages [5] -->
is a Conﬁguration Variable; •

<!-- b000111 | prose | pages [5] -->
lxrm lyrm lzrm

<!-- b000112 | prose | pages [5] -->
!

<!-- b000113 | prose | pages [5] -->
wxrm wyrm wzrm

<!-- b000114 | prose | pages [5] -->
P =

<!-- b000115 | prose | pages [5] -->
is Conﬁguration Matrix.

<!-- b000116 | prose | pages [5] -->
hxrm hyrm hzrm

<!-- b000117 | furniture | pages [6] -->
Team # 1908286

<!-- b000118 | furniture | pages [6] -->
Page 5 of 22

<!-- b000119 | prose | pages [6] -->
Undeﬁned elements in the matrix is deﬁned similarly to lxrm.

<!-- b000120 | prose | pages [6] -->
In multiple-goods-condition, we consider the container loading problem as a Single-objective integer programming problem. Constraint Conditions of the three-dimensional heterogeneous container loading problem are listed below:

<!-- b000121 | prose | pages [6] -->
1. Boxes should contain all goods:

<!-- b000122 | prose | pages [6] -->
|K| X

<!-- b000123 | prose | pages [6] -->
|R| X

<!-- b000124 | prose | pages [6] -->
Xk =

<!-- b000125 | prose | pages [6] -->
k=1

<!-- b000126 | prose | pages [6] -->
Mr

<!-- b000127 | prose | pages [6] -->
r=1

<!-- b000128 | prose | pages [6] -->
2. Corresponding Rule. Each goods should be placed into just only one box:

<!-- b000129 | prose | pages [6] -->
|K| X

<!-- b000130 | prose | pages [6] -->
∀r ∈R, ∀m ∈Mr,

<!-- b000131 | prose | pages [6] -->
Ykmr = 1

<!-- b000132 | prose | pages [6] -->
k=1

<!-- b000133 | prose | pages [6] -->
3. Conﬁguration Constraint. Each edge in each goods should be parallel to just only one edge of the corresponding box. Let P = (pab)3×3, we have

<!-- b000134 | prose | pages [6] -->
3 X

<!-- b000135 | prose | pages [6] -->
pab = 1

<!-- b000136 | prose | pages [6] -->
a=1

<!-- b000137 | prose | pages [6] -->
3 X

<!-- b000138 | prose | pages [6] -->
pab = 1.

<!-- b000139 | prose | pages [6] -->
b=1

<!-- b000140 | prose | pages [6] -->
4. Box Size Constraint. All goods should be inside the corresponding box:

<!-- b000141 | prose | pages [6] -->
∀k ∈K, ∀r ∈R, ∀m ∈Mr, Ykrm(u + P · sG

<!-- b000142 | prose | pages [6] -->
r ) ≤sB

<!-- b000143 | prose | pages [6] -->
We can solve the programming problem with a speciﬁc objective function.

<!-- b000144 | prose | pages [6] -->
3.3 Putting MEDs into Bays

<!-- b000145 | prose | pages [6] -->
Since there are only three types of MEDs and two types of Bays, putting MEDs into Bays is relatively simple. In 3D heterogeneous container loading problems, space utilization(SU) usually decreases as type of goods R increases. For simplicity, we only consider two types of MEDs or less in a Bay. We do not need to consider an objective function in this process. Rather, we list all possible combinations subject to its constraint conditions.

<!-- b000146 | prose | pages [6] -->
Let R = {1, 2, 3}, whose elements 1, 2 and 3 correspond to MED1, MED2 and MED3, re- spectively. And |Mr| is the number of MEDr. For type q Bay (q = 1, 2), we have the following constraint conditions:

<!-- b000147 | prose | pages [6] -->
P|K|

<!-- b000148 | prose | pages [6] -->
k=1 Xk = P3

<!-- b000149 | prose | pages [6] -->


<!-- b000150 | prose | pages [6] -->
r=1 Mr

<!-- b000151 | prose | pages [6] -->


<!-- b000152 | prose | pages [6] -->
P|K|

<!-- b000153 | prose | pages [6] -->


<!-- b000154 | prose | pages [6] -->
k=1 Ykmr = 1, ∀r ∈R, ∀m ∈Mr

<!-- b000155 | prose | pages [6] -->
  

<!-- b000156 | prose | pages [6] -->
P3

<!-- b000157 | prose | pages [6] -->
a=1 pab = 1 P3

<!-- b000158 | prose | pages [6] -->


<!-- b000159 | prose | pages [6] -->
b=1 pab = 1

<!-- b000160 | prose | pages [6] -->
  

<!-- b000161 | prose | pages [6] -->
, (1)

<!-- b000162 | prose | pages [6] -->
q , ∀k ∈K, ∀r ∈R, ∀m ∈Mr

<!-- b000163 | prose | pages [6] -->
Ykrm(u + P · sG

<!-- b000164 | prose | pages [6] -->
r ) ≤sB

<!-- b000165 | prose | pages [6] -->


<!-- b000166 | prose | pages [6] -->
where sB

<!-- b000167 | prose | pages [6] -->
1 = (8 10 14)T, sB 2 = (24 20 20)T.

<!-- b000168 | prose | pages [6] -->
For type i Drone, an additional constraint is that total weight cannot exceed Max Payload Capability(MPCi):

<!-- b000169 | prose | pages [6] -->
2|M1| + 2|M2| + 3|M3| ≤MPCi (2)

<!-- b000170 | prose | pages [6] -->
(1 and (2) determine whether we can put a set of MEDs into a Bay. If that set of MEDs works, we calculate its space utilization:

<!-- b000171 | prose | pages [6] -->
P3

<!-- b000172 | prose | pages [6] -->
r=1 (|Mr|lrwrhr)

<!-- b000173 | prose | pages [6] -->
SU =

<!-- b000174 | prose | pages [6] -->
,

<!-- b000175 | prose | pages [6] -->
LqWqHq

<!-- b000176 | furniture | pages [7] -->
Team # 1908286

<!-- b000177 | furniture | pages [7] -->
Page 6 of 22

<!-- b000178 | prose | pages [7] -->
where (l1 w1 h1)T = (14 7 5)T, (l2 w2 h2)T = (5 8 5)T, (l3 w3 h3)T = (12 7 4)T, (L1 W1 H1)T = (8 10 14)T, (L2 W2 H2)T = (24 20 20)T.

<!-- b000179 | prose | pages [7] -->
We draw the space utilization plot of Drone D (Bay 1) and Drone F (Bay 2), see Figure 2. From the ﬁgure we can see that space utilization of Bay 2 is relatively low. The reason is that the inequality (2) is strict. In most cases, the max payload capability is so small that the all sets of MEDs that satisfy (2) can be loaded. So the sub-ﬁgures for Bay 2 clearly shows the inequality (2).

<!-- b000180 | caption | pages [7] -->
Figure 2: Space Utilization with different MEDs and different Bays

<!-- b000181 | prose | pages [7] -->
From Figure 2, we conclude that the Transport Capability matrix is

<!-- b000182 | prose | pages [7] -->


<!-- b000183 | prose | pages [7] -->
  

<!-- b000184 | prose | pages [7] -->
TC =

<!-- b000185 | prose | pages [7] -->
  

<!-- b000186 | prose | pages [7] -->
11

<!-- b000187 | prose | pages [7] -->


<!-- b000188 | prose | pages [7] -->
10 1 1 1 1

<!-- b000189 | prose | pages [7] -->


<!-- b000190 | prose | pages [7] -->
2 2 4 2

<!-- b000191 | prose | pages [7] -->


<!-- b000192 | prose | pages [7] -->
7 7 7 4

<!-- b000193 | prose | pages [7] -->
 

<!-- b000194 | prose | pages [7] -->
2 2 4 2

<!-- b000195 | prose | pages [7] -->
.

<!-- b000196 | prose | pages [7] -->
(4)

<!-- b000197 | prose | pages [7] -->


<!-- b000198 | prose | pages [7] -->
7 7 7 5

<!-- b000199 | prose | pages [7] -->
 

<!-- b000200 | prose | pages [7] -->
11 7

<!-- b000201 | prose | pages [7] -->


<!-- b000202 | prose | pages [7] -->
10 6

<!-- b000203 | heading | pages [7] -->
Drone Transport Capability Model

<!-- b000204 | prose | pages [7] -->
3.4

<!-- b000205 | prose | pages [7] -->
Since we only consider medicine transport in this section, there must be a corresponding Drone Cargo Bay on each drone. The number of Typei Drones to carry NumMEDj MEDjs is

<!-- b000206 | prose | pages [7] -->
Numij = NumMEDj/TCij

<!-- b000207 | prose | pages [7] -->
. Note that we use Numij to evaluate transport capability, so it may be a decimal. The volume needed when one Typei Drone carries all MEDs for one day is

<!-- b000208 | prose | pages [7] -->
3 X

<!-- b000209 | prose | pages [7] -->
V Med Day

<!-- b000210 | prose | pages [7] -->
+ V Bay

<!-- b000211 | prose | pages [7] -->
Numij)(V drone

<!-- b000212 | prose | pages [7] -->
= ( i

<!-- b000213 | prose | pages [7] -->
j=1

<!-- b000214 | prose | pages [7] -->
)

<!-- b000215 | prose | pages [7] -->
i

<!-- b000216 | prose | pages [7] -->
i

<!-- b000217 | prose | pages [7] -->
. The number of days that a Typei Drone can continue transporting MEDs to all needed place is

<!-- b000218 | prose | pages [7] -->
Daysi = Vcontainer/V Med Day

<!-- b000219 | prose | pages [7] -->
i

<!-- b000220 | furniture | pages [8] -->
Team # 1908286

<!-- b000221 | furniture | pages [8] -->
Page 7 of 22

<!-- b000222 | prose | pages [8] -->
Transport Capability Index of Typei Drone is deﬁned as the normalization of maximum day Daysi:

<!-- b000223 | prose | pages [8] -->
1≤k≤7 {Daysk}

<!-- b000224 | prose | pages [8] -->
TCIi = Daysi/ max

<!-- b000225 | prose | pages [8] -->
We have two matrices:

<!-- b000226 | prose | pages [8] -->
2.97

<!-- b000227 | prose | pages [8] -->


<!-- b000228 | prose | pages [8] -->


<!-- b000229 | prose | pages [8] -->
15.92

<!-- b000230 | prose | pages [8] -->


<!-- b000231 | prose | pages [8] -->


<!-- b000232 | prose | pages [8] -->
8.78

<!-- b000233 | prose | pages [8] -->


<!-- b000234 | prose | pages [8] -->


<!-- b000235 | prose | pages [8] -->


<!-- b000236 | prose | pages [8] -->


<!-- b000237 | prose | pages [8] -->
24.45

<!-- b000238 | prose | pages [8] -->
Days =

<!-- b000239 | prose | pages [8] -->


<!-- b000240 | prose | pages [8] -->


<!-- b000241 | prose | pages [8] -->
41.46

<!-- b000242 | prose | pages [8] -->


<!-- b000243 | prose | pages [8] -->


<!-- b000244 | prose | pages [8] -->


<!-- b000245 | prose | pages [8] -->


<!-- b000246 | prose | pages [8] -->
28.98

<!-- b000247 | prose | pages [8] -->


<!-- b000248 | prose | pages [8] -->


<!-- b000249 | prose | pages [8] -->
47.21

<!-- b000250 | prose | pages [8] -->
0.0629

<!-- b000251 | prose | pages [8] -->


<!-- b000252 | prose | pages [8] -->


<!-- b000253 | prose | pages [8] -->
0.3371

<!-- b000254 | prose | pages [8] -->


<!-- b000255 | prose | pages [8] -->


<!-- b000256 | prose | pages [8] -->
0.1859

<!-- b000257 | prose | pages [8] -->


<!-- b000258 | prose | pages [8] -->


<!-- b000259 | prose | pages [8] -->


<!-- b000260 | prose | pages [8] -->


<!-- b000261 | prose | pages [8] -->
0.5178

<!-- b000262 | prose | pages [8] -->
TCI =

<!-- b000263 | prose | pages [8] -->
(5)

<!-- b000264 | prose | pages [8] -->


<!-- b000265 | prose | pages [8] -->


<!-- b000266 | prose | pages [8] -->
0.8782

<!-- b000267 | prose | pages [8] -->


<!-- b000268 | prose | pages [8] -->


<!-- b000269 | prose | pages [8] -->


<!-- b000270 | prose | pages [8] -->


<!-- b000271 | prose | pages [8] -->
0.6139

<!-- b000272 | prose | pages [8] -->


<!-- b000273 | prose | pages [8] -->


<!-- b000274 | prose | pages [8] -->
1.0000

<!-- b000275 | prose | pages [8] -->
Putting Drones and Bays into Cargo Conatainers 3.5

<!-- b000276 | prose | pages [8] -->
According to TCI matrix (5), Type E and G Drones have the best transport capability. We will choose Type E and G as alternative transport drones. The corresponding Bays are Bays 2. We will also load one Drone H (tethered drone) in each Cargo Container, because it helps to build emergency communication.

<!-- b000277 | prose | pages [8] -->
Let R = {4, 5, 6, 7}. 4, 5, 6 and 7 represent Bay 2, Drone E, H and G, respectively. The number of MEDs in Bay 2 only relies on Type i drone’s Max Payload Capability MPCi. So we conclude that for Drone ﬂeet consisting of E and G, transport capability is only relevant to Total Load Weight:

<!-- b000278 | prose | pages [8] -->
X

<!-- b000279 | prose | pages [8] -->
MPCi × |Mi| = 15|M5| + 20|M7|

<!-- b000280 | prose | pages [8] -->
TLW =

<!-- b000281 | prose | pages [8] -->
i=5,7

<!-- b000282 | prose | pages [8] -->
Our problem can be stated as

<!-- b000283 | prose | pages [8] -->
(6)

<!-- b000284 | prose | pages [8] -->
TLW = 15|M5| + 20|M7| max

<!-- b000285 | prose | pages [8] -->
Equation (??) shows that each Drone must carry one Bay, so the total number of Drones E and G equal to the number of Bays 2. Equation (??) shows that each Cargo Container should have one Type H Drone.

<!-- b000286 | heading | pages [8] -->
Monte-Carlo Simulation And Results

<!-- b000287 | prose | pages [8] -->
3.6

<!-- b000288 | prose | pages [8] -->
We use Monte-Carlo Simulation to get a satisfactory solution of the problem in Section 4.5. Since this is a NP-completeness problem, it takes too long to traverse all situations. Our objec- tive function will not have major changes with a narrow change of inputs. That is, the optimal point is not an isolated singularity. That’s why we choose Monte-Carlo Simulation.

<!-- b000289 | prose | pages [8] -->
If the probability to ﬁnd the optimal point is 10−5 for one simulation, the probability to ﬁnd the optimal point will be 1 −0.999991000000 = 0.999954 with one billion simulations. Figure 3 is our simulation process using Three Space Division method. We start at a feasible solution |M4| = 50, |M5| = 30, |M6| = 1, |M7| = 20.

<!-- b000290 | furniture | pages [9] -->
Team # 1908286

<!-- b000291 | furniture | pages [9] -->
Page 8 of 22

<!-- b000292 | caption | pages [9] -->
Figure 3: Monte-Carlo Simulation Process

<!-- b000293 | caption | pages [9] -->
Table 1: Satisfactory Packing Conﬁguration for Each Container

<!-- b000294 | prose | pages [9] -->
Using the Three Space Division Model and Monte-Carlo Simulation, we obtain the satisfac- tory packing conﬁguration for each container (with or without Drone H). The result shows that the ideal optimal solution is, at most, slightly better than our satisﬁed solution(space utiliza- tion up to 97.97%). It also validates that Drone G has the best transportation capability, which perfectly ﬁt the highest Drone G TCI value.

<!-- b000295 | prose | pages [9] -->
4

<!-- b000296 | heading | pages [9] -->
Geospatial Analysis Model

<!-- b000297 | prose | pages [9] -->
4.1

<!-- b000298 | heading | pages [9] -->
Drone Reconnaissance Model

<!-- b000299 | prose | pages [9] -->
For a video-capable drone, in order to effectively estimate its maximum viewing radius, rview, we make the following assumptions:

<!-- b000300 | prose | pages [9] -->
1. The height between a drone and the ground is 20 meters. 2. The drone’s lens can swing back and forth from side to side, with unlimited viewing angles. 3. The camera on a drone (if it has one) is a two megapixel camera (a 1080P lens). 4. The resolution of road detection is one meter.

<!-- b000301 | prose | pages [9] -->
We see 

<!-- b000302 | prose | pages [9] -->
tan(θ + ∆θ) = rview/20 , tan θ = (rview −1)/20

<!-- b000303 | prose | pages [9] -->
where

<!-- b000304 | furniture | pages [10] -->
Team # 1908286

<!-- b000305 | prose | pages [10] -->
• θ is the camera’s forward viewing angle; • ∆θ is the smallest resolution angle; • rview is the maximum viewing radius.

<!-- b000306 | furniture | pages [10] -->
Page 9 of 22

<!-- b000307 | prose | pages [10] -->
For a two megapixel camera, we have ∆θ = 3 × 10−3rad. Plugging it into (7), we obtain

<!-- b000308 | prose | pages [10] -->


<!-- b000309 | prose | pages [10] -->
θ = 1.322 rad rview = 79.7 m .

<!-- b000310 | prose | pages [10] -->
Since rview is close to 100 m, we can divide the island map into grid on the order of one hundred meters, as is shown in Figure[ÍijÆˇn]. Every grid covers a 100 m × 100 m square. Cor- responding to the longitude and latitude,(x, y) is the grid point coordinates of the position.

<!-- b000311 | prose | pages [10] -->
4.2 Geographical Features

<!-- b000312 | prose | pages [10] -->
We divide the location selection problem into two major parts Transport and Reconnais- sance. Then we decide that the information of highway, population, geographic and medical are important to Transport and Reconnaissance. Using the map in the attachment and from Puerto Rico Maps [4], we ﬁnd seven features for the four types of information, see Table 2.

<!-- b000313 | caption | pages [10] -->
Table 2: Features (FO is the Feather Order)

<!-- b000314 | furniture | pages [10] -->


<!-- b000315 | prose | pages [10] -->
FO 1 2 3

<!-- b000316 | prose | pages [10] -->
Main

<!-- b000317 | prose | pages [10] -->
Highways

<!-- b000318 | prose | pages [10] -->
Population

<!-- b000319 | prose | pages [10] -->
feature(FO) highways

<!-- b000320 | prose | pages [10] -->
& roads

<!-- b000321 | prose | pages [10] -->
distribution

<!-- b000322 | prose | pages [10] -->
4 5 6 7

<!-- b000323 | prose | pages [10] -->
Hospital

<!-- b000324 | prose | pages [10] -->
High

<!-- b000325 | prose | pages [10] -->
location

<!-- b000326 | prose | pages [10] -->
population

<!-- b000327 | prose | pages [10] -->
Harbours Altitude

<!-- b000328 | prose | pages [10] -->
& medical

<!-- b000329 | prose | pages [10] -->
areas

<!-- b000330 | prose | pages [10] -->
needs

<!-- b000331 | prose | pages [10] -->
For a certain position, Feature1 means the main highways. Feature 2 means the highways we extract from attachment 1. Feature 3 means the density of population [4]. Feature4 means high population areas from the given map. Feature 5 means the distance from harbors. [3] Feature 6 means the altitude. Feature 7 means the index considering transporting MEDs.

<!-- b000332 | prose | pages [10] -->
The feature maps are shown in Figure 4. Note that all feature maps are normalized, so that for every map, the sum of all values is 1 :

<!-- b000333 | prose | pages [10] -->
X

<!-- b000334 | prose | pages [10] -->
X

<!-- b000335 | prose | pages [10] -->
Feature(FO, x, y), ∀FO ∈{Z|1 ≤FO ≤7},

<!-- b000336 | prose | pages [10] -->
x

<!-- b000337 | prose | pages [10] -->
y

<!-- b000338 | prose | pages [10] -->
where Feature(FO, x, y) is the geographical distribution function of featureFO.

<!-- b000339 | prose | pages [10] -->
The weight of hospital j

<!-- b000340 | prose | pages [10] -->
3 X

<!-- b000341 | prose | pages [10] -->
MedWighti × MedNumberji

<!-- b000342 | prose | pages [10] -->
HOSj =

<!-- b000343 | prose | pages [10] -->
i=1

<!-- b000344 | prose | pages [10] -->
We assign the values in hospital map.

<!-- b000345 | prose | pages [10] -->
We calculate Transport cost for MEDj by Demand number for MEDj:

<!-- b000346 | prose | pages [10] -->
3 X

<!-- b000347 | prose | pages [10] -->
MedWeightj = Medj/

<!-- b000348 | prose | pages [10] -->
Medi

<!-- b000349 | prose | pages [10] -->
i=1

<!-- b000350 | furniture | pages [11] -->
Team # 1908286

<!-- b000351 | prose | pages [11] -->
We have

<!-- b000352 | furniture | pages [11] -->
Page 10 of 22

<!-- b000353 | prose | pages [11] -->
MedWeight = (0.2949 0.2681 0.4369)T j = 1, 2, 3 (8)

<!-- b000354 | prose | pages [11] -->
From (8) we see MedWeight2 is smallest, because MED 2 has the least demand.

<!-- b000355 | prose | pages [11] -->
4.3 Singal Location Determination

<!-- b000356 | prose | pages [11] -->
4.3.1 Detail Information of TI and RI

<!-- b000357 | prose | pages [11] -->
is an evaluation index for Drone Type i of feature FO in position p1(x, y) and T Idetail evaluates the detailed transport capability. Let p1 be the target position for Cargo Container. Let p2 be the corresponding point in feature map, we have

<!-- b000358 | prose | pages [11] -->
X

<!-- b000359 | prose | pages [11] -->
TIα(i, p1, p2)Feature(FO, p2).

<!-- b000360 | prose | pages [11] -->
TIdetail(i, FO, p1) =

<!-- b000361 | prose | pages [11] -->
p2

<!-- b000362 | prose | pages [11] -->
Similarly, RIdetail(i, FO, p1) = P

<!-- b000363 | prose | pages [11] -->
p2 RIα(i, p1, p2)Feature(FO, p2).

<!-- b000364 | prose | pages [11] -->
T Iα is a function of i, p1 and p2:

<!-- b000365 | prose | pages [11] -->
TIα(i, p1, p2) = TIdistance(i, p1, p2)TIcover(i)TCI(i)

<!-- b000366 | prose | pages [11] -->
Similarly, RIα(i, p1, p2) = RIdistance(i, p1, p2)RIcover(i)RCI(i)

<!-- b000367 | prose | pages [11] -->
T Idistance measures Transporting Index with ﬂight distance:

<!-- b000368 | prose | pages [11] -->
1 −dis(p1,p2)

<!-- b000369 | prose | pages [11] -->


<!-- b000370 | prose | pages [11] -->
DIS(i) βTI,

<!-- b000371 | prose | pages [11] -->
TIdistance =

<!-- b000372 | prose | pages [11] -->
0,

<!-- b000373 | prose | pages [11] -->
where

<!-- b000374 | prose | pages [11] -->
• dis(p1, p2) is the distance between p1, p2; • DIS(i) is the longest ﬂight distance.

<!-- b000375 | prose | pages [11] -->
dis < DIS , (9) otherwise

<!-- b000376 | prose | pages [11] -->
DIS(i) = α × Speed × Flight Time (No Cargo), see(2) (10)

<!-- b000377 | prose | pages [11] -->
The function (9) shows that closer points are more important within coverage area. βTI = 0.2 produces a linear transformation.

<!-- b000378 | prose | pages [11] -->
Similarly,

<!-- b000379 | prose | pages [11] -->
1 −(1 −dis(p1,p2)

<!-- b000380 | prose | pages [11] -->


<!-- b000381 | prose | pages [11] -->
RIdistance =

<!-- b000382 | prose | pages [11] -->
0, DIS(i) )βRI, dis < DIS , (11) otherwise

<!-- b000383 | prose | pages [11] -->
where βRI = 0.2. βRI produces a linear transformation. Compare (9) and (11), function (11) shows that in reconnaissance, farther points are preferred, because the close ones can be detect- ed on the way to medical

<!-- b000384 | prose | pages [11] -->
T Icover measures Transporting Index with coverage area. The effectiveness of each point in coverage area is equally important.

<!-- b000385 | prose | pages [11] -->
TIcover(i) = 1/(π · (DIS(i))2 · β′

<!-- b000386 | prose | pages [11] -->
where β′

<!-- b000387 | prose | pages [11] -->
TI is determined by βTI; β′

<!-- b000388 | prose | pages [11] -->
TI = 13/15.

<!-- b000389 | prose | pages [11] -->
(i) = 1/(π · (DIS(i))2 · β′ Similarly, RIcover

<!-- b000390 | prose | pages [11] -->
TI), (12)

<!-- b000391 | prose | pages [11] -->
β′ RI),

<!-- b000392 | prose | pages [11] -->
RI = 14/15

<!-- b000393 | furniture | pages [12] -->
Team # 1908286

<!-- b000394 | furniture | pages [12] -->
Page 11 of 22

<!-- b000395 | prose | pages [12] -->
measures Transporting Index with and Transporting Capability of Drone Type i with T CI unit volume. We computed the result of TCI(i) in matrix TCI (5). Similarly, We calculate RCI1(i) = (DIS(i))2/V (i),where V(i) is the total volume of Type i drones and corresponding Bays. Then we normalize it as RCI(i) = RCI1(i)/ max

<!-- b000396 | prose | pages [12] -->
1≤p≤7 RCI1(p)

<!-- b000397 | prose | pages [12] -->
After we calculate TIdetail(i, FO, x, y) and RIdetail(i, FO, x, y), we should take all features into account and calculate the integrate Transport Index of all features T I(i, x, y):

<!-- b000398 | prose | pages [12] -->
X

<!-- b000399 | prose | pages [12] -->
wTI(FO) · TIdetail(i, FO, x, y)

<!-- b000400 | prose | pages [12] -->
TI(i, x, y) =

<!-- b000401 | prose | pages [12] -->
FO

<!-- b000402 | prose | pages [12] -->
Similarly, RI(i, x, y) = P

<!-- b000403 | prose | pages [12] -->
(13)

<!-- b000404 | prose | pages [12] -->
FO wRI(FO) · RIdetail(i, FO, x, y). We obtain a Reconnaissance Capa- bility Index matrix

<!-- b000405 | prose | pages [12] -->


<!-- b000406 | prose | pages [12] -->
  

<!-- b000407 | prose | pages [12] -->
RCI =

<!-- b000408 | prose | pages [12] -->
   

<!-- b000409 | prose | pages [12] -->
0.0768

<!-- b000410 | prose | pages [12] -->


<!-- b000411 | prose | pages [12] -->
1.0000

<!-- b000412 | prose | pages [12] -->


<!-- b000413 | prose | pages [12] -->
0.1105

<!-- b000414 | prose | pages [12] -->
 

<!-- b000415 | prose | pages [12] -->
0.1850

<!-- b000416 | prose | pages [12] -->
(14)

<!-- b000417 | prose | pages [12] -->


<!-- b000418 | prose | pages [12] -->
0.1190

<!-- b000419 | prose | pages [12] -->
 

<!-- b000420 | prose | pages [12] -->
0.1782

<!-- b000421 | prose | pages [12] -->


<!-- b000422 | prose | pages [12] -->
0.1194

<!-- b000423 | prose | pages [12] -->
Matrix (14) shows that Drone B is the best type to detect highways and roads. Note that Drone B is a lot better than the other types.

<!-- b000424 | prose | pages [12] -->
We listed a few results of the detail information of TI and RI based on Puerto Rico case (see Figure 4).

<!-- b000425 | prose | pages [12] -->
(b) Highways and Roads (a) Main Highways (c) Populated Places

<!-- b000426 | prose | pages [12] -->
(e) TI Drone G Highways & Roads (d) TI Drone G Main Highways (f) TI Drone G Populated Places

<!-- b000427 | prose | pages [12] -->
(h) RI Drone E Highways &c Roads (g) RI Drone E Main Highways (i) RI Drone E Populated Places

<!-- b000428 | caption | pages [12] -->
Figure 4: Samples of Detail Information of TI and RI

<!-- b000429 | prose | pages [12] -->
4.3.2 TI and RI

<!-- b000430 | prose | pages [12] -->
To determine the weight of different features, we employ Analytic Hierarchy Process (AHP). Since those features in Table 2 have different effects on TI and RI, we use AHP twice for TI and RI. The comparison matrices are listed below:

<!-- b000431 | furniture | pages [13] -->
Team # 1908286

<!-- b000432 | furniture | pages [13] -->
Page 12 of 22

<!-- b000433 | prose | pages [13] -->
(a) Comparison Matrix For TI (b) Comparison Matrix For RI

<!-- b000434 | prose | pages [13] -->
To test the consistency of the matrices, we calculate the Consistency Ratio (CR), which is deﬁned as the ratio of Consistency Index (CI) to Average Random Consistency Index (RI′). n = 4 , RI′ = 0.90, CR = (λmax −n)/(n −1). For TI, CI = 0.0532, CR = 0.0598 < 0.1. For RI, CI = 0.0526, CR = 0.0591 < 0.1.so the consistency of the matrices is conﬁrmed.

<!-- b000435 | prose | pages [13] -->
As is indicated in Figure 6, for Transporting Index, Medical information is the most im- portant factor weighting 67.03%. That is because hospital destination of a Drone transporting MEDs. For Reconnaissance Index, highway information take up the highest at 60.11%. One possible reason is that the ﬂight distance of Drones is limited. Drones must get close enough to detect highways.

<!-- b000436 | prose | pages [13] -->
Then we put the weight terms into (13) and (4.3.1), and get TI and RI (see Figure5).

<!-- b000437 | prose | pages [13] -->
(c) TI Drone B (d) TI Drone E (e) TI Drone G

<!-- b000438 | prose | pages [13] -->
(f) RI Drone B (g) RI Drone E (h) RI Drone G

<!-- b000439 | caption | pages [13] -->
Figure 5: Samples of TI and RI

<!-- b000440 | caption | pages [13] -->
Figure 6: Sections and their weight when determining location using AHP

<!-- b000441 | furniture | pages [14] -->
Team # 1908286

<!-- b000442 | prose | pages [14] -->
4.3.3 Efﬁciency Evaluation

<!-- b000443 | furniture | pages [14] -->
Page 13 of 22

<!-- b000444 | prose | pages [14] -->
To show the relative relationship between TI and RI, we introduce an important parameter λ as the transport objective coefﬁcient. 0 ≤λ ≤1. λ shows the importance of transport. The bigger λ is, the more important transport is.

<!-- b000445 | prose | pages [14] -->
The location selection problem is a multi-objective programming problem. We simplify it to a single-objective-programming by using λ. Considering transport and reconnaissance, our objective function is the overall efﬁciency:

<!-- b000446 | prose | pages [14] -->
E = TIλ

<!-- b000447 | prose | pages [14] -->
ALLRI1−λ

<!-- b000448 | prose | pages [14] -->
ALL, (15)

<!-- b000449 | prose | pages [14] -->
In function (15),we deﬁne the Transport Index for all types of drones:

<!-- b000450 | prose | pages [14] -->
7 X

<!-- b000451 | prose | pages [14] -->
TIALL =

<!-- b000452 | prose | pages [14] -->
i=1

<!-- b000453 | prose | pages [14] -->
v(i) · TI(i), (16)

<!-- b000454 | prose | pages [14] -->
where v(i) is the volume percentage of Type i drones and corresponding Bays in all types. Since v(i) = V (i)/ P7

<!-- b000455 | prose | pages [14] -->
p=1 V (p), we have P7

<!-- b000456 | prose | pages [14] -->
i=1 v(i) = 1.

<!-- b000457 | prose | pages [14] -->
Similarly, RIALL is the RI for all types of drones: RIALL = P7

<!-- b000458 | prose | pages [14] -->
i=1 v(i) · RI(i)

<!-- b000459 | prose | pages [14] -->
We compute the Best Efﬁciency for each position (x, y). Our programming problem can be stated as

<!-- b000460 | prose | pages [14] -->
ALLRI1−λ

<!-- b000461 | prose | pages [14] -->
E = TIλ max

<!-- b000462 | prose | pages [14] -->
7 X

<!-- b000463 | prose | pages [14] -->
v(i) = 1

<!-- b000464 | prose | pages [14] -->
s.t.

<!-- b000465 | prose | pages [14] -->
i=1

<!-- b000466 | prose | pages [14] -->
v(i) ≥0,

<!-- b000467 | prose | pages [14] -->
ALL

<!-- b000468 | prose | pages [14] -->
∀i ∈{Z|1 ≤i ≤7}

<!-- b000469 | prose | pages [14] -->
(b) lambda = 0.4 (a) lambda = 0.2 (c) lambda = 0.5

<!-- b000470 | prose | pages [14] -->
(e) lambda = 0.8 (d) lambda = 0.6 (f) lambda = 1.0

<!-- b000471 | caption | pages [14] -->
Figure 7: Single Location Determination Based on Different λ Values

<!-- b000472 | prose | pages [14] -->
We apply this method to the Puerto Rico situation (see Figure 7).

<!-- b000473 | prose | pages [14] -->
4.4 Multiple Locations Determination

<!-- b000474 | prose | pages [14] -->
Selecting multiple best locations is a dynamic programming problem. Each location selec- tion can effect the new selection. To show the effect,we set the two following rules:

<!-- b000475 | furniture | pages [15] -->
Team # 1908286

<!-- b000476 | furniture | pages [15] -->
Page 14 of 22

<!-- b000477 | prose | pages [15] -->
• Effects on Transportation. After each selection, we assume the Container satisﬁes 1/3 of all MEDs demands if its Drones and MED sullplies allow. Note that the container should ﬁrst provide MEDs to nearby medical centers. And we should renormalize the the Medical Infromation feature. • Effects on Reconnaissance. After each selection, we assume Drones of the Container can detect all highways within the container’s Maximun Reconnaissance Scope. High- way Information feature within that scope should decrease. We will multiply them by a coefﬁcient of r0 = 0.1.

<!-- b000478 | prose | pages [15] -->
4.5

<!-- b000479 | heading | pages [15] -->
Results

<!-- b000480 | caption | pages [15] -->
Table 3: The Result of Multiple Locations Determination Modle(λ = 0.5)

<!-- b000481 | caption | pages [15] -->
Table 4: The Location Selection Related To λ

<!-- b000482 | prose | pages [15] -->
5

<!-- b000483 | heading | pages [15] -->
Fleet Arrange Model

<!-- b000484 | prose | pages [15] -->
5.1

<!-- b000485 | heading | pages [15] -->
Schedule Arrangement Model

<!-- b000486 | prose | pages [15] -->
5.1.1

<!-- b000487 | heading | pages [15] -->
Satisfactory Solution on MEDs

<!-- b000488 | prose | pages [15] -->
We maximize the ability of DroneGo ﬂeet to satisfy the anticipated Medical Package De- mand. According to the choices of drone type given in Part B, we will only employ drone B, E and G to transport MEDs. First, we search satisfactory solution on how to put MEDs into a Bay. Then we can use those schemes to assemble a best schedule so that we maximize the ability of DroneGo ﬂeet to satisfy the anticipated Medical Package Demand.

<!-- b000489 | prose | pages [15] -->
We will use the following notations in this section:

<!-- b000490 | prose | pages [15] -->
• MEDweight is the weight of MED j; j

<!-- b000491 | furniture | pages [16] -->
Team # 1908286

<!-- b000492 | prose | pages [16] -->
• MEDNum

<!-- b000493 | furniture | pages [16] -->
Page 15 of 22

<!-- b000494 | prose | pages [16] -->
is the number of MED j put into a bay in a satisfactory solution; j • Drone 1,2 and 3 correspond to B,E and G, respectively; • kij is the jth scheme for Type i drones; • Ki = (ki1 ki2 . . . kir)T is the set of all the satisfactory schemes for drone i.

<!-- b000495 | prose | pages [16] -->
By using the Transport Capability matrix (4) in Section 4.3, we demonstrate that for drone B, E and G, only Max Payload Capacity (MPC) will play a decisive role on whether a scheme is fea- sible. Actually, satisfactory solutions must be at the feasible region. Consequently, satisfactory solution for a Type i drone should subject to the stated constraints:

<!-- b000496 | prose | pages [16] -->
3 X

<!-- b000497 | prose | pages [16] -->
MEDweight

<!-- b000498 | prose | pages [16] -->
× MEDnum j

<!-- b000499 | prose | pages [16] -->
1

<!-- b000500 | prose | pages [16] -->
3 X

<!-- b000501 | prose | pages [16] -->
MEDweight

<!-- b000502 | prose | pages [16] -->
×MEDnum

<!-- b000503 | prose | pages [16] -->
j

<!-- b000504 | prose | pages [16] -->
j

<!-- b000505 | prose | pages [16] -->
1

<!-- b000506 | prose | pages [16] -->
≤MPCi j

<!-- b000507 | prose | pages [16] -->
MEDweight

<!-- b000508 | prose | pages [16] -->
+ min

<!-- b000509 | prose | pages [16] -->
> MPCi j

<!-- b000510 | prose | pages [16] -->
j

<!-- b000511 | prose | pages [16] -->
We use integer programming method to search feasible solutions.

<!-- b000512 | prose | pages [16] -->
ki1 is the 1st solution.

<!-- b000513 | prose | pages [16] -->
Eventually we get K1,K2 K3. for drone 1 2 3 respectively has 3,27,44 satisfactory schemes.

<!-- b000514 | prose | pages [16] -->
5.1.2

<!-- b000515 | heading | pages [16] -->
Maximum Effective Days Model

<!-- b000516 | prose | pages [16] -->
Now we have known all satisfactory schemes on how to put MEDs into a Bay for drone B,E and G.To evaluate the the ability of DroneGo ﬂeet to transport Emergency Medical Package,we make an assumption: Every delivery location’s need for MED should be satisﬁed equally.

<!-- b000517 | prose | pages [16] -->
Since delivery location has the certain anticipated Medical Package Demand everyday,we can calculate a Maximum supply days if the type and number of drone and the schemes for each corresponding drone are determined.

<!-- b000518 | prose | pages [16] -->
we will use the following notations:

<!-- b000519 | prose | pages [16] -->
• MEDneed = (mj1 mj2 mj3) is the need of sth delivery location within the range of trans- s portation. mj1, mj2, mj3 is corresponding to the number of MED1,2,3. • Numirs is the number of drone i which carry out the rth scheme ; • |Ri| is the number of satisfactory schemes for drone i; • S is the number of delivery location; • Dayss is Maximum supply days for delivery position s.

<!-- b000520 | prose | pages [16] -->
Here is the Linear Programming model. For delivery position s,

<!-- b000521 | prose | pages [16] -->
| Ri |

<!-- b000522 | prose | pages [16] -->
3 X

<!-- b000523 | prose | pages [16] -->
X

<!-- b000524 | prose | pages [16] -->
Numirs kis ≥Dayss × MEDr

<!-- b000525 | prose | pages [16] -->
max

<!-- b000526 | prose | pages [16] -->
r

<!-- b000527 | prose | pages [16] -->
i=1

<!-- b000528 | prose | pages [16] -->
|S|

<!-- b000529 | prose | pages [16] -->
| Ri |

<!-- b000530 | prose | pages [16] -->
X

<!-- b000531 | prose | pages [16] -->
X

<!-- b000532 | prose | pages [16] -->
Numirs = Qk

<!-- b000533 | prose | pages [16] -->
s.t.

<!-- b000534 | prose | pages [16] -->
s

<!-- b000535 | prose | pages [16] -->
r

<!-- b000536 | prose | pages [16] -->
Numirs ≥0

<!-- b000537 | furniture | pages [17] -->
Team # 1908286

<!-- b000538 | furniture | pages [17] -->
Page 16 of 22

<!-- b000539 | prose | pages [17] -->
| Ri |

<!-- b000540 | prose | pages [17] -->
3P

<!-- b000541 | prose | pages [17] -->
P

<!-- b000542 | prose | pages [17] -->
Numirs kis

<!-- b000543 | prose | pages [17] -->
r

<!-- b000544 | prose | pages [17] -->
i=1

<!-- b000545 | prose | pages [17] -->
1≤s≤|S|{Dayss} = min

<!-- b000546 | prose | pages [17] -->
max Dayseffective = min

<!-- b000547 | prose | pages [17] -->
1≤s≤|S|(

<!-- b000548 | prose | pages [17] -->
)

<!-- b000549 | prose | pages [17] -->
MEDs

<!-- b000550 | prose | pages [17] -->
|S|

<!-- b000551 | prose | pages [17] -->
| Ri |

<!-- b000552 | prose | pages [17] -->
X

<!-- b000553 | prose | pages [17] -->
X

<!-- b000554 | prose | pages [17] -->
Numirs = Qk

<!-- b000555 | prose | pages [17] -->
s.t.

<!-- b000556 | prose | pages [17] -->
s

<!-- b000557 | prose | pages [17] -->
r

<!-- b000558 | prose | pages [17] -->
Numirs ≥0

<!-- b000559 | caption | pages [17] -->
Table 5: Optimal Drone Payload Packing Conﬁgurations And Drone Schedule

<!-- b000560 | prose | pages [17] -->
Through the use of integer linear programming, we can ﬁnd the optimal drone payload packing conﬁgurations by traversing all possible combinations of the satisﬁed scheme when the number of each drone type and delivery locations’ MEDs need are certain. Now we apply the Schedule Arrangement Model to the situation in Table 3. The result indicates that we can get an optimal solution in a given situation. Moreover, the result directly gives the drone payload packing conﬁgurations for every drone.

<!-- b000561 | prose | pages [17] -->
5.2

<!-- b000562 | heading | pages [17] -->
Drone Route Planning Model

<!-- b000563 | prose | pages [17] -->
Now that we have conﬁrmed the drone delivery plan. Under this scheme, the basic delivery strategy of each drone has been determined. Since we assume that each drone will not move once it has delivered the goods, the extra distance of the drone other than delivery can be used to detect the highways and roads. We can use a Greedy Search Algorithm to arrange individual drones. The algorithm is shown in Figure 8:

<!-- b000564 | furniture | pages [18] -->
Team # 1908286

<!-- b000565 | furniture | pages [18] -->
Page 17 of 22

<!-- b000566 | caption | pages [18] -->
Figure 8: Individual Drone Route Planning Algorithm

<!-- b000567 | prose | pages [18] -->
• Searching nearby, that is, searching the nearest road. Since most roads are continuous, the nearby search algorithm is simple, easy to operate and efﬁcient. • The searched road should not be searched any more, and it should be deleted from the overall search targets. • Delivery ﬁrst strategy, because delivery is urgent, so if you choose between delivery and search, then you must choose delivery.

<!-- b000568 | prose | pages [18] -->
In the algorithm, we call the hospital where the drones need to deliver as the target location. The keys of the algorithm are listed as follows Searching nearby, that is, searching the nearest road. Since most roads are continuous, the nearby search algorithm is simple, easy to operate and efﬁcient. The searched road should not be searched any more, and it should be deleted from the overall search targets. Delivery ﬁrst strategy, because delivery is urgent, so if you choose between delivery and search, then you must choose delivery.

<!-- b000569 | prose | pages [18] -->
For the drone ﬂeet as a whole, we need to select different drones for reconnaissance. Since short-range drones cannot detect points far from the targets and containers, we should priori- tize the path of these drones to maximize their reconnaissance potential. The number of drugs required by the hospital will be changed each time the drone delivers the goods, and the next delivery mission of the drone will also be changed accordingly. More speciﬁcally, if the delivery demand of a certain drug in a hospital has been met, the drone loaded with that drug should not be used as the target place.

<!-- b000570 | prose | pages [18] -->
Further, to improve the algorithm, we can ﬁnd that among the three selected drones, drone B, E and G, the transport capacity of drone B is the weakest, but its reconnaissance capability is the strongest. Even if we deduct the medicine delivery amount of drone B, the effect on the overall drug delivery amount is not signiﬁcant. Therefore, we should use drone B only for reconnaissance. If we apply the above strategy to the 3 container transport model with λ == 0.5, we can obtain the results of transportation path in Figure 10.

<!-- b000571 | furniture | pages [19] -->
Team # 1908286

<!-- b000572 | furniture | pages [19] -->
Page 18 of 22

<!-- b000573 | caption | pages [19] -->
Figure 9: Drone Fleet Route Planning Algorithm

<!-- b000574 | prose | pages [19] -->
Under the model of λ = 0.5, our road reconnaissance coverage for Puerto Rico reached 59.86% (see Figure 10). We can ﬁnd that, in order to meet the needs of the three hospitals n- earby Puerto Rico ˛a´r capital, we use a lot of drones to transport medicine, so the reconnaissance coverage rate of this area is not high, however, in the area of transport demand is relatively small, the container 3, our reconnaissance coverage is very high. This result is consistent with our hypothesis that λ = 0.5, which means reconnaissance and transportation is equally im- portant. At the same time, since we consider the range reduction of drone affected by various reasons, that is, the ratio between the total range used and the ideal total range calculated is α = 0.9, the reconnaissance capability of drone ﬂeet may be better in actual use.

<!-- b000575 | prose | pages [19] -->
(a) Container 1(C1) (b) C1 drone B (c) C1 drone G

<!-- b000576 | prose | pages [19] -->
(d) Container 3(C3) (e) C3 drone B (f) C3 drone E

<!-- b000577 | prose | pages [19] -->
(g) Container 2(C2) (h) C2 drone E (i) All(routes under reconnaissance in black, undetectcted in gray)

<!-- b000578 | caption | pages [19] -->
Figure 10: Drone Routes(the yellow line in the ﬁgure is the ﬂight path of this drone, and the blue dot at

<!-- b000579 | prose | pages [19] -->
the end of the yellow line represents the ﬁnal position of the drone)

<!-- b000580 | furniture | pages [20] -->
Team # 1908286

<!-- b000581 | furniture | pages [20] -->
Page 19 of 22

<!-- b000582 | prose | pages [20] -->
6

<!-- b000583 | heading | pages [20] -->
Sensitivity Analysis

<!-- b000584 | prose | pages [20] -->
As is shown on Geospatial Analysis Model, we use AHP to get the weight vector of wTI and the weight vector of wRI. However, AHP is based on subjective inputs to some extent. Aiming to determine how robust our rankings are in the AHP process, we use the following proportionality equation for adjusting weights:

<!-- b000585 | prose | pages [20] -->
j = 1 −w′

<!-- b000586 | prose | pages [20] -->
p

<!-- b000587 | prose | pages [20] -->
w′

<!-- b000588 | prose | pages [20] -->
wj, 1 −wp

<!-- b000589 | prose | pages [20] -->
where w′

<!-- b000590 | prose | pages [20] -->
j is the new weight, wp the original largest weight of the criterion to be adjusted,and w′

<!-- b000591 | prose | pages [20] -->
p the value after the criterion is adjusted.

<!-- b000592 | caption | pages [20] -->
Table 6: Sensitivity Analysis Result of AHP

<!-- b000593 | prose | pages [20] -->
We respectively apply a −10%, −20%, +10%, +20% variation to the wTI and wRI,and record the the results under each circumstance, respectively. The following is the new results:

<!-- b000594 | prose | pages [20] -->
In the table above, note that Latitude and longitude are used to indicate location and dis- tance between original and new position is shown if position changes. We can conclude that

<!-- b000595 | prose | pages [20] -->
• Above all, the table shows the strong robustness of our model.It is conspicuous that the results only change slightly,notwithstanding we let wDI or wTI have a sizable change. • Remarkably, some positions of container and drone proportion don ˛a´rt vary with different wTI and wRI. Via analyzing the corresponding data, a reasonable explanation is that this position or proportion has much better performance than those adjacent choices.

<!-- b000596 | prose | pages [20] -->
7

<!-- b000597 | heading | pages [20] -->
Strengths and Weaknesses

<!-- b000598 | prose | pages [20] -->
7.1

<!-- b000599 | heading | pages [20] -->
Strengths

<!-- b000600 | prose | pages [20] -->
• A model based on Three Space Division Model and improved Monte-Carlo Simulation

<!-- b000601 | furniture | pages [21] -->
Team # 1908286

<!-- b000602 | furniture | pages [21] -->
Page 20 of 22

<!-- b000603 | prose | pages [21] -->
can solve the problem of packing restrictions in the transportation of goods and have high realizability by considering weight and volume limitations. • Based on the AHP method,the Geospatial Analysis Model fully considers the inﬂuence of many possible factors on the selection of container drop location , including transporta- tion, population, geography and medical information. Therefore, the result of the model is highly credible. • Complex integer programming model and improved greedy algorithm is able to give the drone schedule planning and route planning quickly and accurately. • Flexibility and adaptability are also advantages of the Location Determination Model. When the company change its strategy, new decisions can be quickly derived without modifying the algorithm.

<!-- b000604 | prose | pages [21] -->
7.2

<!-- b000605 | heading | pages [21] -->
Weaknesses

<!-- b000606 | prose | pages [21] -->
• While utilizing improved Monte-Carlo Simulation,the quality of the result may not achieve our high expectation. • The rule of how to transport MEDs to different delivery position is uncertain.It can be further improved to meet different actual needs • The correctness of our conclusions is related to the accuracy of the data collected and the estimates of transportation, population, geography and medical information.

<!-- b000607 | prose | pages [21] -->
8

<!-- b000608 | heading | pages [21] -->
Conclusion

<!-- b000609 | prose | pages [21] -->
To help with post-disaster relief, we designed a prototype of the DroneGo. The system estab- lishes the Drone Transport Model and Drone Survey Model, taking into account the characteris- tics of drone, medicine and container such as weight and size, as well as a variety of geographic information such as road information, population information, rescue information and medical information. We conclude that the Transportation Capability of Drone G is the strongest and the Reconnaissance Capability of drone B is the strongest. When users considered medicine delivery to be as important as road reconnaissance, we got results that the medicine delivery can be maintained for more than two months and road reconnaissance coverage reached nearly 60%.

<!-- b000610 | prose | pages [21] -->
To further provide advice to the DroneGo users, in our system, users can also input a d- ifferent transport/reconnaissance parameter, i.e., different emphasis on transport and recon- naissance. In this case, our DroneGo system can provide different ﬂeet conﬁgurations and container drop points to meet their needs. Meanwhile we construct an efﬁcient schedule ar- rangement and route arrangement model of drones using an integer programming model and an improved greedy algorithm, so the drone ﬂeet can be auto arranged.

<!-- b000611 | heading | pages [21] -->
References

<!-- b000612 | references | pages [21] -->
[1] Wikipedia, “Hurricane maria,” https://en.wikipedia.org/wiki/Hurricane_Maria#Puerto_

<!-- b000613 | references | pages [21] -->
Rico_3, accessed January 29, 2019.

<!-- b000614 | references | pages [21] -->
[2] M. Winn, “We need to be using drones to rescue harvey victims,” https://www.cia.gov/

<!-- b000615 | references | pages [21] -->
library/publications/the-world-factbook/geos/rq.html#Geo, accessed January 29, 2019.

<!-- b000616 | references | pages [21] -->
[3] CIA, “Central america ::

<!-- b000617 | references | pages [21] -->
Puerto rico,” https://w3techs.com/technologies/overview/

<!-- b000618 | references | pages [21] -->
content_language/all, accessed January 29, 2019.

<!-- b000619 | furniture | pages [22] -->
Team # 1908286

<!-- b000620 | furniture | pages [22] -->
Page 21 of 22

<!-- b000621 | references | pages [22] -->
[4] “Puerto rico maps,” http://www.topuertorico.org/maps.shtml, accessed January 29, 2019.

<!-- b000622 | references | pages [22] -->
Memo to CEO of HELP, Inc.

<!-- b000623 | references | pages [22] -->
To: HELP, Inc. CEO

<!-- b000624 | references | pages [22] -->
From: Team 1908286

<!-- b000625 | references | pages [22] -->
Date: January 28, 2019

<!-- b000626 | references | pages [22] -->
Subject: Study of DroneGo disaster response system based on Puerto Rico hurricane in 2017

<!-- b000627 | references | pages [22] -->
In the post-disaster relief, unmanned aerial vehicles, also called drones, are not limited by

<!-- b000628 | references | pages [22] -->
road conditions, so they can quickly provide medicines and other urgent materials to the af-

<!-- b000629 | references | pages [22] -->
fected areas, which can alleviate the shortage of local post-disaster medical drugs. Meanwhile,

<!-- b000630 | references | pages [22] -->
drones can also be used to survey the highways and roads situation and support post-disaster

<!-- b000631 | references | pages [22] -->
relief. We aim to develop a "DroneGo" disaster response system based on a drone ﬂeet, which

<!-- b000632 | references | pages [22] -->
can be used to provide medical assistance to the people in the disaster area, as well as to provide

<!-- b000633 | references | pages [22] -->
information on the disaster situation to the rescue workers.

<!-- b000634 | references | pages [22] -->
In 2017, the worst hurricane to ever hit the United States territory of Puerto Rico left the

<!-- b000635 | references | pages [22] -->
island with severe damage. The DroneGo system needs to be designed to better help NGOs

<!-- b000636 | references | pages [22] -->
use drones for post-disaster exploration and drug delivery missions in similar disasters. The

<!-- b000637 | references | pages [22] -->
system can reasonably plan the selection of a certain drone ﬂeet, container delivery location,

<!-- b000638 | references | pages [22] -->
drone medicine delivery schedule and route planning of exploration road based on the known

<!-- b000639 | references | pages [22] -->
properties of drone, medicine and containers, as well as, medical needs and highways and

<!-- b000640 | references | pages [22] -->
roads reconnaissance needs in disaster areas and other relevant information.

<!-- b000641 | references | pages [22] -->
We designed a prototype of the DroneGo system based on ofﬁcial drone, medicine and con-

<!-- b000642 | references | pages [22] -->
tainer information and applied it to the disaster situation in Puerto Rico. When users con-

<!-- b000643 | references | pages [22] -->
sidered medicine delivery to be as important as road reconnaissance, we got results that the

<!-- b000644 | references | pages [22] -->
medicine delivery can be maintained for more than two months and road reconnaissance cov-

<!-- b000645 | references | pages [22] -->
erage reached nearly 60%. Users can also input a different transport/reconnaissance parameter,

<!-- b000646 | references | pages [22] -->
i.e., different emphasis on transport and reconnaissance. At the same time, our DroneGo sys-

<!-- b000647 | references | pages [22] -->
tem can also quickly obtain the program of drone ﬂeet composition, delivery and arrangement.

<!-- b000648 | references | pages [22] -->
In addition, our DroneGo system can also form a model for drone transportation and recon-

<!-- b000649 | references | pages [22] -->
naissance evaluation for more geographic information (such as population distribution, road

<!-- b000650 | references | pages [22] -->
information, rescue information, medical information, etc.). The approach we are using can be

<!-- b000651 | references | pages [22] -->
further reﬁned and extended to develop a post-disaster rescue drone ﬂeet arrangement system.

<!-- b000652 | references | pages [22] -->
According to our ˛aˇrDroneGo ˛a´s system, we can develop a software (see Figure 11), which will

<!-- b000653 | references | pages [22] -->
greatly help post-disaster relief missions.

<!-- b000654 | references | pages [22] -->
Firstly, for the loading problem of drone ﬂeet, we use an indicator of drone ﬂeet transport

<!-- b000655 | references | pages [22] -->
capacity to form our drone Transport Capacity Model to solve the problem of maximizing the

<!-- b000656 | references | pages [22] -->
drone ﬂeet medicine transport capacity when the disaster location is unknown. Among them,

<!-- b000657 | references | pages [22] -->
the biggest obstacle we encountered is the limitation of goods packing. We developed an al-

<!-- b000658 | references | pages [22] -->
gorithm based on the three-space division method and an improved Monte Carlo simulation,

<!-- b000659 | references | pages [22] -->
which can better solve this problem in a short time. At the same time, we also consider the

<!-- b000660 | references | pages [22] -->
weight, volume and other restrictions, so that our results are highly achievable. In terms of

<!-- b000661 | references | pages [22] -->
speciﬁc solutions, Drone G is considered to be the most transportable.

<!-- b000662 | references | pages [22] -->
Secondly, if we got the information of the disaster area, we can use our DroneGo system

<!-- b000663 | references | pages [22] -->
based on spatial geographic information, which integrated the previous drone Transportation

<!-- b000664 | references | pages [22] -->
Capability Model and a drone Reconnaissance Capability Model. Combining with different ge-

<!-- b000665 | references | pages [22] -->
ographic information, we used Analytic Hierarchy Process (AHP) to analyze the distribution

<!-- b000666 | furniture | pages [23] -->
Team # 1908286

<!-- b000667 | furniture | pages [23] -->
Page 22 of 22

<!-- b000668 | references | pages [23] -->
of drone transportation capability and reconnaissance capability along with the location. In or-

<!-- b000669 | references | pages [23] -->
der to better balance ˛aˇrDroneGo ˛a´s system users to transportation capacity and reconnaissance

<!-- b000670 | references | pages [23] -->
ability of different needs, we set up an overall Efﬁciency Evaluation Model, using the nonlinear

<!-- b000671 | references | pages [23] -->
programming and dynamic programming to get the speciﬁc conﬁguration of the drone ﬂeet

<!-- b000672 | references | pages [23] -->
and container drop point selection. In the system, users can adjust the transportation / recon-

<!-- b000673 | references | pages [23] -->
naissance parameter to get the response of different targets. Through the case study of Puerto

<!-- b000674 | references | pages [23] -->
Rico, we are able to further verify the feasibility of our system.

<!-- b000675 | references | pages [23] -->
We use an integer programming model and an improved greedy algorithm to construct

<!-- b000676 | references | pages [23] -->
the Schedule Arrangement Model and Route Arrangement Model of drones. In drone ﬂeet

<!-- b000677 | references | pages [23] -->
and containers delivery plan chosen by our DroneGo system, we got the medicine transport

<!-- b000678 | references | pages [23] -->
to maintain nearly two months, as well as the results of road reconnaissance coverage reached

<!-- b000679 | references | pages [23] -->
nearly 60%. Finally, the sensitivity of AHP is analyzed to verify the robustness of the system.

<!-- b000680 | references | pages [23] -->
If you want to know more details, please read our essay about this subject. We will be

<!-- b000681 | references | pages [23] -->
glad to discuss more about DroneGo system with you in the future and follow through on any

<!-- b000682 | references | pages [23] -->
decisions you make.

<!-- b000683 | references | pages [23] -->
Attached: DroneGo system software frame, January 28 2019

<!-- b000684 | caption | pages [23] -->
Figure 11: DroneGo system software frame
