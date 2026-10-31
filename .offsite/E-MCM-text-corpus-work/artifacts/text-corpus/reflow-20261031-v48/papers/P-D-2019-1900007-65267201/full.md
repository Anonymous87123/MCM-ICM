# P-D-2019-1900007-65267201

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
1900007

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000005 | title | pages [1] -->
D

<!-- b000006 | prose | pages [1] -->
2019 2019 MCM/ICM

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Analysis of the Optimal Evacuation Plan Based on 2D

<!-- b000009 | title | pages [1] -->
and 3D Models

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
We are tasked to analyze the optimal evacuation plan for the Louvre. To this end, we con- struct both the 2D model and the 3D model to derive the optimal plan. We successfully utilize our models to determine the potential bottlenecks, plan the use of additional exits and let the emergency personnel enter. We take three dimensions of factors into account: the diversity of evacuees (e.g. the disabled, the elderly, etc.), people’s behaviors and the attributes of the build- ing. We provide sufﬁcient visualized results in order to explain our model intuitively.

<!-- b000012 | prose | pages [1] -->
In the 2D Island-Bridge Model, we reasonably planarize the building and discretize the space into dense nodes. Then, we construct the Basic Searching Submodel to calculate the optimal evacuation route and time for different varieties of people. We also form a method to solve the unbalanced usage of each exit. Then, we form the Danger Index Submodel, which gives insight to the real-time distribution of Danger Index in the building. Furthermore, we utilize these submodels to answer how to take advantage of additional exits and how to let the emergency personnel enter. Finally, we carry out the sensitivity analysis by operating our 2D model under different density of people and different inﬂuential range of danger. The re- sult is stable despite these differences, which proves the robustness of the 2D model. Since the methodology of this model always holds true, it can be adapted to different buildings with only slight adjustments.

<!-- b000013 | prose | pages [1] -->
In the 3D Celluar Automata Model, we precisely construct a 3D copy of the Louvre using AutoCAD, which makes our simulation resemble the real-world situation. We implement the model in Pathﬁnder software and carry out 3D simulation. The results clearly demonstrate that the bottlenecks are all around exits or stairs. We also give a heat map of the evacuation time in different places of each ﬂoor.

<!-- b000014 | prose | pages [1] -->
As a conclusion, we write a letter of advice to the emergency manager, offering some prac- tical suggestions about the evacuation plan.

<!-- b000015 | heading | pages [2] -->
Contents

<!-- b000016 | contents | pages [2] -->
1 Introduction

<!-- b000017 | contents | pages [2] -->
1

<!-- b000018 | contents | pages [2] -->
1.1

<!-- b000019 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | contents | pages [2] -->
1

<!-- b000021 | contents | pages [2] -->
1.2

<!-- b000022 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [2] -->
1

<!-- b000024 | contents | pages [2] -->
1.3

<!-- b000025 | contents | pages [2] -->
Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
1

<!-- b000027 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000028 | contents | pages [2] -->
3

<!-- b000029 | contents | pages [2] -->
2.1

<!-- b000030 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
3

<!-- b000032 | contents | pages [2] -->
2.2

<!-- b000033 | contents | pages [2] -->
Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
4

<!-- b000035 | contents | pages [2] -->
3 The 2D Island-Bridge Model (2D-IBM)

<!-- b000036 | contents | pages [2] -->
4

<!-- b000037 | contents | pages [2] -->
3.1

<!-- b000038 | contents | pages [2] -->
Basic Structure of the Model . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
4

<!-- b000040 | contents | pages [2] -->
3.2

<!-- b000041 | contents | pages [2] -->
Dimensionality Reduction Method . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
6

<!-- b000043 | contents | pages [2] -->
3.3

<!-- b000044 | contents | pages [2] -->
Spacial Discretization Method . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
7

<!-- b000046 | contents | pages [2] -->
3.4

<!-- b000047 | contents | pages [2] -->
Basic Searching Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
8

<!-- b000049 | contents | pages [2] -->
3.5

<!-- b000050 | contents | pages [2] -->
Danger Index Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
11

<!-- b000052 | contents | pages [2] -->
3.6

<!-- b000053 | contents | pages [2] -->
How to Utilize Additional Exits? . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
13

<!-- b000055 | contents | pages [2] -->
3.7

<!-- b000056 | contents | pages [2] -->
How to Let Emergency Personnel Enter? . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
13

<!-- b000058 | contents | pages [2] -->
3.8

<!-- b000059 | contents | pages [2] -->
Model Evaluation and Sensitivity Analysis

<!-- b000060 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
14

<!-- b000062 | contents | pages [2] -->
4 The 3D Cellular Automata Model (3D-CAM)

<!-- b000063 | contents | pages [2] -->
15

<!-- b000064 | contents | pages [2] -->
4.1

<!-- b000065 | contents | pages [2] -->
The Mechanism of the Model . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
15

<!-- b000067 | contents | pages [2] -->
4.2

<!-- b000068 | contents | pages [2] -->
Visualized Result of the Model

<!-- b000069 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
16

<!-- b000071 | contents | pages [2] -->
4.3

<!-- b000072 | contents | pages [2] -->
Determining the Potential Bottleneck . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
17

<!-- b000074 | contents | pages [2] -->
5 Strengths and Weaknesses

<!-- b000075 | contents | pages [2] -->
18

<!-- b000076 | contents | pages [2] -->
5.1

<!-- b000077 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
18

<!-- b000079 | contents | pages [2] -->
5.2

<!-- b000080 | contents | pages [2] -->
Weaknesses

<!-- b000081 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
18

<!-- b000083 | contents | pages [2] -->
6 Conclusion: A Letter of Advice to the Emergency Manager

<!-- b000084 | contents | pages [2] -->
18

<!-- b000085 | contents | pages [2] -->
References

<!-- b000086 | contents | pages [2] -->
19

<!-- b000087 | contents | pages [2] -->
Appendices

<!-- b000088 | contents | pages [2] -->
20

<!-- b000089 | contents | pages [2] -->
A Our Simulation Codes Written in MATLAB

<!-- b000090 | contents | pages [2] -->
20

<!-- b000091 | furniture | pages [3] -->
Team # 1900007

<!-- b000092 | furniture | pages [3] -->
Page 1 of 26

<!-- b000093 | heading | pages [3] -->
1 Introduction

<!-- b000094 | heading | pages [3] -->
1.1 Restatement of the Problem

<!-- b000095 | prose | pages [3] -->
In France alone, there have been at least 12 major terror-related incidents since 2012, and the number is still increasing. In face of an emergency, panic-stricken people, if not properly guided, tend to ﬂee around like headless chickens, causing massive chaos at the scene. The mayhem could hurt even more than the attack itself, especially in crowded space such as indoor museums like the Louvre. Therefore, establishing an effecitve emergency evacuation plan is critical as to eliminate unnecessary disorder and casualties. Here, we are required to design a model to guide evacuation from the Louvre or other multi-storey buildings.

<!-- b000096 | prose | pages [3] -->
There are three major objectives:

<!-- b000097 | prose | pages [3] -->
• Find the optimal evacuation plan, which means enabling people to evacuate the buliding in the fastest and safest manner, as well as allowing emergency per- sonnel to enter as quickly as possible.

<!-- b000098 | prose | pages [3] -->
• Determine the potential bottlenecks that may cause congestion and stagnation.

<!-- b000099 | prose | pages [3] -->
In our model, a bottleneck is deﬁned as a particular location where the passing speed is extremely slow.

<!-- b000100 | prose | pages [3] -->
• Universalize the model, that is, adjust our model so that it can be adapted to a broad set of potential threats.

<!-- b000101 | heading | pages [3] -->
1.2 Literature Review

<!-- b000102 | prose | pages [3] -->
Based on the differences in mechanisms of spacial movement, current models of indoor emergency evacuation can be divided into four catagories[1]: network-based models, particle-based models, cellular-based models and ant-based models.

<!-- b000103 | prose | pages [3] -->
The network-based model simpliﬁed evacuation as a ﬂow of people moving at a certain speed in the network[2]. The particle-based model considered people as self- driving particles controlled by various internal and external forces[3]. The cellular- based model employed cellular automata theory to simulate the evacuation process by the spatio-temporal modeling method[4]. The ant-based model utilized ant colony algorithm, to perceive the real-time change and ﬁnd the optimal path in a dynamic way[5].

<!-- b000104 | heading | pages [3] -->
1.3 Our work

<!-- b000105 | prose | pages [3] -->
We construct two distinctive models: the 2D Island-Bridge Model (2D-IBM) and the 3D Cellular Automata Model (3D-CAM).

<!-- b000106 | prose | pages [3] -->
In the 2D Island-Bridge Model (2D-IBM), we develop the following methods or submodels in four steps.

<!-- b000107 | furniture | pages [4] -->
Team # 1900007

<!-- b000108 | furniture | pages [4] -->
Page 2 of 26

<!-- b000109 | prose | pages [4] -->
First, we develop a Dimensionality Reduction Method, which planarizes the move- ment on 3D multi-storey building as equivalent 2D horizontal motion. Secondly, we establish the Spacial Discretization Method. We discretize the space of the 2D "build- ing" into dense nodes with certain coordinates. People are designed to move from one node to the other. Thirdly, we form a Basic Searching Model, which bases the evacuees’ route choice on three factors: their distance from each exit, their distance from the source of danger and the maximum capacity of each exit. We use it to solve the problem of congestion around exits, which is a potential bottleneck. The Dijkstra Searching Algorithm is utilized in this model. Fourthly, we form the Danger Index Model, which can provide the real-time distribution of Danger Index in the buiding. Thus, the emergency manager can have a direct understanding of emergency. In this model, the density of evacuees in each mesh are also included, thus adding the degree of congestion and stagnation into consideration.

<!-- b000110 | prose | pages [4] -->
After completing the construction of the 2D-IBM Model, we employ it to discuss problems of how to utilize additional exits and how to let emergency personnel enter. Finally, we carry out the sensitivity analysis and validate that our 2D-IBM Model stays robust despite the changes of the attributes of the building, the location of the danger source, the inﬂuence range of danger and the density of people.

<!-- b000111 | prose | pages [4] -->
In the the 3D Celluar Automata Model, we construct a 3D model of the Louvre using AutoCAD, and then implement it into Pathﬁnder, a professional and mature software, to simulate the evacuation process based on Celluar Automata Method. The 3D simulation clearly demonstrates the bottlenecks of evacuation and provide some other useful data.

<!-- b000112 | prose | pages [4] -->
All in all, we take a wide varieties of factors into consideration, including the di- versity of evacuees, human behavior patterns, and building information. The speciﬁc factors we consider are shown in Figure 1.

<!-- b000113 | caption | pages [4] -->
Figure 1: The Factors that We Take into Account

<!-- b000114 | furniture | pages [5] -->
Team # 1900007

<!-- b000115 | furniture | pages [5] -->
Page 3 of 26

<!-- b000116 | heading | pages [5] -->
2 Preparation of the Models

<!-- b000117 | heading | pages [5] -->
2.1 Assumptions

<!-- b000118 | prose | pages [5] -->
It is difﬁcult to study the actual situation in the Louvre because of the irregular shape of the building, the extreme complication of interior structure and the unpre- dictability of human behavior. In order to simplify the problem and to hold the cor- rectness of results at the same time, we make the assumptions below:

<!-- b000119 | prose | pages [5] -->
(If there is no special explanation, the assumptions below are applied to both the 2D-IBM and the 3D-CAM Model. )

<!-- b000120 | heading | pages [5] -->
1. We simplify the shape of the Louvre museum, viewing each storey as a stan-

<!-- b000121 | prose | pages [5] -->
dard, two-dimensional ’U’ shape composed of three rectangles (the grey area).

<!-- b000122 | heading | pages [5] -->
[Only Applicable in the 2D-IBM Model]

<!-- b000123 | prose | pages [5] -->
The exact data are labeled in Figure 2. With careful calculation, we set the total area of the simpliﬁed storey almost the same as that of the real-world condition.

<!-- b000124 | prose | pages [5] -->
Therefore, the range of movement holds the same.

<!-- b000125 | caption | pages [5] -->
Figure 2: The Simpliﬁed Storey in the Louvre

<!-- b000126 | prose | pages [5] -->
2. We assume that EVERY place of the simpliﬁed storey is walkable.

<!-- b000127 | prose | pages [5] -->
That is to say, we ignore the physical barriers (e.g. exhibits) in the way, because we can hardly know the exact distribution of exhibits and other facilities. The only barrier of movement we consider is the boundaries and the source of danger.

<!-- b000128 | heading | pages [5] -->
3. We treat every staircase and every escalator as identical, and suppose that they

<!-- b000129 | prose | pages [5] -->
both function as two-way stairs in case of emergency.

<!-- b000130 | prose | pages [5] -->
First, it is understandable that escalators will be shut down in case of emergency, made to function the same as staircases. Therefore, staircases and escalators are treated equally as passageways between two storeys. Plus, we assume that pas- sageways between two storeys share completely identical attributes for simplicity.

<!-- b000131 | heading | pages [5] -->
4. We regard the initial distribution of evacuees as random.

<!-- b000132 | prose | pages [5, 6] -->
Though there might be more people piling up in front of some world-renowned masterpiece (e.g. the Mona Lisa), the cumulative effect is localized and small- scale. Compared to a total of 400,000 art works in the Louvre, the masterpiece which may cause cumulative effect resembles a drop in the ocean. Thus, random initial distribution of people is a reasonable assumption.

<!-- b000133 | furniture | pages [6] -->
Team # 1900007

<!-- b000134 | furniture | pages [6] -->
Page 4 of 26

<!-- b000136 | heading | pages [6] -->
5. We suppose that evacuees become aware of the emergency and start escaping

<!-- b000137 | prose | pages [6] -->
simultaneously. Plus, they will follow the guidance.

<!-- b000138 | prose | pages [6] -->
That is, ﬁrst, we ignore the time lag of knowing the emergency, because it is tiny compared to the whole evacuation process. Second, if evacuees do not follow the guidance, their behavior will become unpredictable, and the evacuation plan will be of little use.

<!-- b000139 | heading | pages [6] -->
6. We regard different evacuees as points with different attributes moving in the

<!-- b000140 | prose | pages [6] -->
two-dimensional space. [Only Applicable in the 2D-IBM Model] This assumption is a complement of the "simpliﬁed storey assumption" (assump- tion 1) discussed above. It should be stressed that, each point of evacuee, though abstracted, still has its distinctive human characteristics. For example, the maxi- mum speed of the point representing the elderly is slower than that of the young "point".

<!-- b000141 | prose | pages [6] -->
7. The data provided by the Louvre are representative.

<!-- b000142 | prose | pages [6] -->
Though the most recent annual report of the Louvre[6] was updated in 2014, we still assume these data are representative and ignore the potential errors related to them. Some important data we will use are listed in Table 1.

<!-- b000143 | caption | pages [6] -->
Table 1: Some Important Data about the Louvre

<!-- b000144 | prose | pages [6] -->
Item Data

<!-- b000145 | prose | pages [6] -->
Visitors per Year 9.3 million Ratio of Young and not Disabled Visitors 72.1% Ratio of Old and not Disabled Visitors 21.1% Ratio of Disabled Visitors 6.8%

<!-- b000146 | heading | pages [6] -->
2.2 Notation

<!-- b000147 | prose | pages [6] -->
The primary notations in our paper are listed in Table 2. There can be some other notations to be deﬁned later.

<!-- b000148 | heading | pages [6] -->
3 The 2D Island-Bridge Model (2D-IBM)

<!-- b000149 | heading | pages [6] -->
3.1 Basic Structure of the Model

<!-- b000150 | prose | pages [6] -->
In the 2D Island-Bridge Model (2D-IBM), we develop the following methods and submodels subsequently.

<!-- b000151 | furniture | pages [7] -->
Team # 1900007

<!-- b000152 | furniture | pages [7] -->
Page 5 of 26

<!-- b000153 | caption | pages [7] -->
Table 2: Notation

<!-- b000154 | prose | pages [7] -->
Symbol Deﬁnition

<!-- b000155 | prose | pages [7] -->
dis(i, j) the distance between node i and node j e(i,j) the weight of edge between node i and node j Rdead the radius of deadly area which can not be entered Snode the sum of nodes Speople the sum of people indoor in the case of emergency ρpeople the density of people indoor in the case of emergency Sdis the sum of distance travelled by all evacuees Vrange the maximum visual range of an individual α(s) the maximum ratio of people exiting from exit s exit (an independent variable reﬂecting the attribute of exit s) S(s) the number of people exiting from exit s exit tindividual the average time for each individual to evacuate telderly the average time for each elder to evacuate tyouth the average time for each young people to evacuate tdisabled the average time for each disabled people to evacuate Rmesh the radius of each single mesh N (i) the number of people in mesh i mesh w(i) the density weight of mesh i density w(i) the emergency weight of mesh i emergency w(i) the exit weight of mesh i exit DI(i) the danger index of mesh i

<!-- b000156 | prose | pages [7] -->
• Step 1: We develop a Dimensionality Reduction Method, which planarizes the movement on staircases as equivalent 2D horizontal motion. Based on this method, we substitute the multi-storey building into a 2D planar space. Each storey resembles an "island", and each staircase resembles a "bridge" connecting two islands. See Figure 3.

<!-- b000157 | prose | pages [7] -->
• Step 2: We establish the Spacial Discretization Method. We discretize the space of the "island" into dense nodes, and then place the "island" in a rectangular co- ordinate system to get the coordinate of each node. We save these nodes’ coordi- nates in the form of matrix for the sake of programming. People are designed to move from one node to the other.

<!-- b000158 | prose | pages [7] -->
• Step 3: We build a Basic Searching Model, which bases the evacuees’ route choice on three factors: their distance from each exit, their distance from the source of danger and the maximum capacity of each exit. We also take into ac- count the diversity of visitors, such as the elderly, the disabled, etc. Then, we uti- lize Dijkstra Searching Algorithm to implement the model in MATLAB. After randomly distributing people in the "building" and selecting a source of danger, we simulate the optimal evacuation route for every individual, and visualize the result.

<!-- b000159 | prose | pages [7, 8] -->
• Step 4: We optimize the Basic Searching Model and form the Field-based Model In this reﬁned model, we add the degree of congestion and stagnation into con- sideration by measuring the density of evacuees in each mesh. Then, We calculate an island, and each staircase resembles a bridge connecting two "island"s.

<!-- b000160 | furniture | pages [8] -->
Team # 1900007

<!-- b000161 | furniture | pages [8] -->
Page 6 of 26

<!-- b000162 | caption | pages [8] -->
Figure 3: Schematic Diagram of the Dimensionality Reduction Method. Each storey resembles

<!-- b000164 | prose | pages [8] -->
the weight of each mesh in terms of the inﬂuence exerted by density of people, distance from danger and distance from exits. After that, we combine the three kind of weight to form Danger Index (DI) of each mesh, and calculate it. Finally, we visualize the result with a heat map.

<!-- b000165 | heading | pages [8] -->
3.2 Dimensionality Reduction Method

<!-- b000166 | prose | pages [8] -->
The philosophy of the 2D Island-Bridge Model (2D-IBM) is dimensionality reduc- tion. Dimensionality reduction is the process of reducing the number of irrelevant variables in order to obtain a set of principal variables which can reﬂect the attributes of the high dimensional object. For example, the sun shines through leaves (high dimen- sion, 3D), casting shadow (low dimension, 2D) on the ground. Despite the dimension of shadow is lower than that of leaves, you can still have a rough idea of the leaves’ shape. In other words, it is feasible to simulate the core attributes of high-dimensional objects with low-dimentional ones.

<!-- b000167 | prose | pages [8] -->
Back to our problem, evacuees move both horizontally and vertically on stairs, which is a 3D motion. Our Dimensionality Reduction Method seeks to planarize the movement on stairs as 2D horizontal motion.

<!-- b000168 | prose | pages [8] -->
We abstract all the stairs between two storeys as "bound-together", and then choose a "junction point" on either storey. We take the distance between each stair and "junc- tion point" into account. Then we calculate the equivalent length and width of the planarized "bound-together" stair with the equations below:

<!-- b000169 | prose | pages [8] -->
dis(i, junc) ηi = (1) Pn i=1 dis(i, junc)

<!-- b000170 | prose | pages [8, 9] -->
n (Length)eq = 1 X n · [ηi · (length)i] i=1 (Width)eq = (width)i (3)

<!-- b000171 | furniture | pages [9] -->
Team # 1900007

<!-- b000172 | furniture | pages [9] -->
Page 7 of 26

<!-- b000174 | prose | pages [9] -->
where n is the number of stairs between two neighbouring storeys, i is the serial num- ber of a stair, and dis(i, junc) is the distance between the "junction point" and stair # i, (length)i and (width)i are the original length and width of stair # i.

<!-- b000175 | prose | pages [9] -->
In Equation (1), ηi ∈[0, 1] is the normalized distribution coefﬁcient, which has a positive correlation with the equivalent length. And ηi · (length)i represents the weighed length of each stair. Therefore, Equation (2) represents the ultimate equiv- alent length between two storeys.

<!-- b000176 | prose | pages [9] -->
According to Assumption 3, we treat every staircase as identical, so the equations can be simpliﬁed as below.

<!-- b000177 | prose | pages [9] -->
n (Length)eq = L ηi = L X n · (4) n i=1

<!-- b000178 | prose | pages [9] -->
(Width)eq = W (5)

<!-- b000179 | prose | pages [9] -->
Then, we substitute the data into the equations above (L = 100m, W = 20m, n = 3(−2F, −1F), 13(−1F, 0F), 28(0F, 1F), 14(1F, 2F)) and get the exact shape of the equiv- alent 2D "building". See Figure 4.

<!-- b000180 | caption | pages [9] -->
Figure 4: The Dimensionality-reduction Building

<!-- b000181 | heading | pages [9] -->
3.3 Spacial Discretization Method

<!-- b000182 | prose | pages [9] -->
We discretize the space of the 2D "building" into dense nodes, and then place the "building" in a rectangular coordinate system to get the coordinate of each node. We save these nodes’ coordinates in the form of matrix for the sake of programming. (The four blue circle in Figure 5 respectively represent one of the four frequently-used exits.)

<!-- b000183 | furniture | pages [10] -->
Team # 1900007

<!-- b000184 | furniture | pages [10] -->
Page 8 of 26

<!-- b000185 | caption | pages [10] -->
Figure 5: Node Distribution of the 2D Model

<!-- b000186 | heading | pages [10] -->
3.4 Basic Searching Model

<!-- b000187 | prose | pages [10] -->
We base the Basic Searching Model on Dijkstra Searching Algorithm (DSA), which can ﬁgure out the optimal route from a given origin to an appointed destination. In our model, each evacuee is considered as an origin, and the closest exit for him/her is the corresponding destination. The Dijkstra Searching Algorithm can only ﬁnd the short- est path to a single destination at a time, but the evacuee has 4 potential destinations (4 different exits). So in order to ﬁgure out the optimal exit, we separatedly set the 4 exits as the destination and carry out Dijkstra Searching Algorithm. Certainly, we will ﬁnd four different "short route". The optimal exit for that evacuee is the exit of the shortest route among the four.

<!-- b000188 | prose | pages [10] -->
In a traditional Dijkstra Searching Algorithm, the weight of an edge is deﬁned as the geometric distance between the two nodes.

<!-- b000189 | prose | pages [10] -->
However, we make some adjustions based on real-world conditions. First, evac- uees can only assess the condition within their visual threshold and choose to head towards one place. So in our model, only the weight between adjacent nodes within an evacuee’s visual threshold can be set in the traditonal way: dis(i, j). Plus, it is ap- parent that evacuees should not choose the nodes located in the deadly zone, even if it is close to both of the exit and the current node. Therefore, the weight of all edges within the deadly zone should be set as inﬁnity.

<!-- b000190 | prose | pages [10] -->
To sum up, in our model, weight of the edge between Node #i and Node #j is de- ﬁned by the equation below.

<!-- b000191 | furniture | pages [11] -->
Team # 1900007

<!-- b000192 | furniture | pages [11] -->
Page 9 of 26

<!-- b000193 | prose | pages [11] -->
 i̸ = j, dis(i, j) ≤Vrange, and Node #j is not in the danger zone dis(i, j)   e(i,j) = 0 i = j, (6)  ∞ otherwise. 

<!-- b000194 | prose | pages [11] -->
where

<!-- b000195 | prose | pages [11] -->
• e(i, j) is the weight of edge between Node #i and Node #j,

<!-- b000196 | prose | pages [11] -->
• dis(i, j) is the geometric distance between Node #i and Node #j,

<!-- b000197 | prose | pages [11] -->
• Rdead is the radius of the deadly zone,

<!-- b000198 | prose | pages [11] -->
• Vrange is an individual’s maximum visual threshold.

<!-- b000199 | prose | pages [11] -->
We draw a ﬂow chart to illustrate our Basic Searching Model. See Figure 6.

<!-- b000200 | caption | pages [11] -->
Figure 6: The Flow Chart Describing the Basic Search Model

<!-- b000201 | prose | pages [11] -->
After implementing the model in MATLAB, we can ﬁgure out the optimal evac- uation route for each individual and its length. Given the speed and proportion of different kinds of people (e.g. the elderly, the disabled), we can calculate the average evacuation time using the equations below.

<!-- b000202 | prose | pages [11, 12] -->
Sdis Speople · P Pk · vk k ∈{elder, young, disabled} tindividual = , Sdis k ∈{elder, young, disabled} tk = , (8) Speople · vk

<!-- b000203 | furniture | pages [12] -->
Team # 1900007

<!-- b000204 | furniture | pages [12] -->
Page 10 of 26

<!-- b000206 | prose | pages [12] -->
We also establish a method to avoid congestion around exits, which may become the potential bottleneck. If we do not control the maximum ratio of people passing through a certain exit, chances are that the majority of evacuees are allocated to the same exit because of the limited number and uneven distribution of the exits, just as the following ﬁgure illustrates. See Figure 7.

<!-- b000207 | prose | pages [12] -->
Part(I) of Figure 7 shows optimal evacuation routes(the lines). Part(II) illustrates the ratio of people passing through each exit. We can clearly see that 90% of the evacuees leave the building from Exit #1, making this exit extremely overloaded. The overused exit will be jammed and may become the potential bottleneck.

<!-- b000208 | caption | pages [12] -->
Figure 7: The Result Without Setting the Ratio of People Passing Through a Certain Exit.

<!-- b000209 | prose | pages [12] -->
To solve the congestion around exits, all exits should be utilized in a balanced way. We can adjust the maximum ratio of people using exit #s (α(s) exit) to disperse the pressure of it. For example, we set α(s) exit as 50% for the four exits, and carry out simulation again. The results are shown in Figure 8. It is clear that the overuse and congestion of Exit #1 are greatly relieved.

<!-- b000210 | caption | pages [12] -->
Figure 8: The Result after Setting α(s)

<!-- b000211 | prose | pages [12] -->
exit as 50%.

<!-- b000212 | furniture | pages [13] -->
Team # 1900007

<!-- b000213 | furniture | pages [13] -->
Page 11 of 26

<!-- b000214 | prose | pages [13] -->
Utilizing the equations discussed above, we plug in a set of reasonable data listed in Table 3, and calculate the average time to leave the Louvre for the elderly, the youth, the disabled, and all the evacuees respectively.

<!-- b000215 | caption | pages [13] -->
Table 3: Some Data we Use in the Basic Searching Model

<!-- b000216 | prose | pages [13] -->
Item Plug-in Data

<!-- b000217 | prose | pages [13] -->
Vrange 21 m Rdead 30 m Exy (580 m, 550 m) Speople 1471 Pyouth 72.1% Pelderly 21.1% Pdisabled 6.8% vyouth 1.28 m/s velderly 1.03 m/s vdisabled 0.78 m/s ρpeople 0.4 people per node αs 0.5 exit

<!-- b000218 | prose | pages [13] -->
The result of the average evacuation time and distance are listed in Table 4

<!-- b000219 | caption | pages [13] -->
Table 4: Some Data we Use in the Basic Searching Model

<!-- b000220 | prose | pages [13] -->
Item Result 6.33 × 105 m Sdis tindividual 364.85 s telderly 413.98 s tyouth 336.35 s tdisabled 551.95 s

<!-- b000221 | heading | pages [13] -->
3.5 Danger Index Model

<!-- b000222 | prose | pages [13] -->
In order to have a good command of the real-time change of emergency, we estab- lish the Danger Index Model. In this model, we introduce a new concept–"mesh" as the smallest unit of our study, which is the circular area with a node as its centre.

<!-- b000223 | prose | pages [13] -->
We add the the density of evacuees in each mesh into consideration. Then, We cal- culate the weight of each mesh in terms of the inﬂuence exerted by density of people, distance from danger and distance from exits. After that, we combine the three kind of weight to form Danger Index (DI) of each mesh, and calculate it. Finally, we visualize the result with a heat map.

<!-- b000224 | prose | pages [13] -->
The weight of a mesh can be calculated in terms of the inﬂuence exerted by the density of people, the distance from exits and the distance from the source of danger.

<!-- b000225 | furniture | pages [14] -->
Team # 1900007

<!-- b000226 | furniture | pages [14] -->
Page 12 of 26

<!-- b000227 | prose | pages [14] -->
• Density Weight: High density of people surrounding an evacuee will cause con- gestion and lower the speed, so the density weight of mesh #i can be calculated using the following equation:

<!-- b000228 | prose | pages [14] -->
N (i) w(i) mesh density = (9) π × R2 mesh

<!-- b000229 | prose | pages [14] -->
where N (i) mesh is the number of people in mesh #i, and Rmesh is the radius of mesh #i.

<!-- b000230 | prose | pages [14] -->
• Emergency Weight: It is widely accepted that the degree of danger is inversely proportional to the distance from it. Thus, the emergency weight of mesh #i can be deﬁned by the following equation:

<!-- b000231 | prose | pages [14] -->
1 w(i) emergency = (10) dis(i, Exy)

<!-- b000232 | prose | pages [14] -->
where Exy is the source of danger, and dis(i, Exy) stands for the distance between mesh #i and the source of danger.

<!-- b000233 | prose | pages [14] -->
• Exit Weight: The weight of exit is deﬁned as

<!-- b000234 | prose | pages [14] -->
w(i) exit = min{dis(i, Exit(s))} (11)

<!-- b000235 | prose | pages [14] -->
where dis(i, Exit(s)) refers to the distance from mesh #i to exit #s, because the more distant from the exit, the more time-consuming the evacuation process will be.

<!-- b000236 | prose | pages [14] -->
The overall degree of danger depends on all of the three factors. Thus, we deﬁne the Danger Index (DI) by calculating the weighed sum of these three kinds of weight, as DI(i) = a · w(i) density + b · w(i) danger + c · w(i) (12) exit

<!-- b000237 | prose | pages [14] -->
where a,b and c are the ratios of the three weight components. In different cases, the signiﬁcance of each component varies, so we should adjust these ratios to ﬁt different conditions.

<!-- b000238 | prose | pages [14] -->
For example, we use two different sets of ratios, and visualize the real-time distri- bution Danger Index of every place using the 3D heat map. At the beginning of an emergency, the source of danger is very inﬂuential, so we set a high ratio for Emer- gency Weight, and the result is shown in Part(I) of Figure 9. However, after some time, the source of danger alleviates, so we can lower the ratio of emergency, and ﬁgure out the up-to-date distribution of Danger Index like Part(II) of Figure 9.

<!-- b000239 | prose | pages [14] -->
The emergency manager can adjust the ratio of the current key inﬂuence, and have an understanding of the real-time Danger Index in the building.

<!-- b000240 | furniture | pages [15] -->
Team # 1900007

<!-- b000241 | furniture | pages [15] -->
Page 13 of 26

<!-- b000242 | caption | pages [15] -->
Figure 9: Distribution of Danger Index with Different Sets of Ratios

<!-- b000243 | prose | pages [15] -->
3.6 How to Utilize Additional Exits?

<!-- b000244 | prose | pages [15] -->
Utilizing the Danger Index Model, we can easily take advantage of the additional exits. Here is our plan.

<!-- b000245 | prose | pages [15] -->
First, all of the four main exits should be used for evacuation purpose, since they are more familiar to the evacuees and can be monitored by the app "Afﬂuences".

<!-- b000246 | prose | pages [15] -->
Plus, based on the real-time Danger Index (DI) distribution, we can calculate the proportion of the additional exits that should be open for evacuation purpose. We set a danger threshold. When the emergency happens, we count the number of evacuees located in meshes whose DI is above the security threshold, and deﬁne the number as Pdanger. Suppose we have n additional exits, and i of them are open for evacuation purpose, we can adjust i according to Pdanger. The speciﬁc relationship between them can be described by Equation (13).

<!-- b000247 | prose | pages [15] -->
 n Pdanger > a,    n −1 b < Pdanger ≤a,     n −2 c < Pdanger ≤b, i = (13) ... ...       Pdanger ≈0. 0 

<!-- b000248 | prose | pages [15] -->
a, b, c. . . in the equation can be determined by Fuzzy Sets or Monte Carlo method. However, due to the lack of speciﬁc data, we will not detail it here.

<!-- b000249 | prose | pages [15] -->
3.7 How to Let Emergency Personnel Enter?

<!-- b000250 | prose | pages [15] -->
To assist the emergency personnel, we can utilize our Basic Searching Model and Danger Index Model to determine the best doors to enter and optimal routes in the building.

<!-- b000251 | prose | pages [15, 16] -->
First, emergency personnel should enter from the underused main exits and the additional exits that are not open for evacuation. As for the former, the ratio of evac- uees passing through a certain main exit can be adjusted by our Basic Searching Model. Therefore, we can decrease the ratio of an exit to make way for the emergency person- nel. As for the latter, the additional exits that are not open for evacuation can all be used to enter the building.

<!-- b000252 | furniture | pages [16] -->
Team # 1900007

<!-- b000253 | furniture | pages [16] -->
Page 14 of 26

<!-- b000255 | prose | pages [16] -->
Second,upon entering the building, emergency personnel should travel from places with low Danger Index to the ones with high Danger Index, which is just the contrary to evacuees. (The real-time distribution of Danger Index can be calculated by our Dan- ger Index Model.) In this way, they can quickly cope with the source of danger or dredge the crowd with high density.

<!-- b000256 | heading | pages [16] -->
3.8 Model Evaluation and Sensitivity Analysis

<!-- b000257 | prose | pages [16] -->
To test the sensitivity, we operate the model under several different conditions. We change the density of people (ρpeople), the radius of the deadly zone (Rdead), the maximum ratio of usage of exit #i (α(i) exit), and calculate the corresponding average time of evacuation for each kind of people. Then, we visualize our results with the ﬁgures below.

<!-- b000258 | caption | pages [16] -->
Figure 10: The Framewok of the 3D Cellular Automata Model(3D-CAM)

<!-- b000259 | prose | pages [16] -->
The ﬁrst and second part of Figure 10 tell us that the evacuation time for each kind of people is almost same despite the difference of the density of people (ρpeople) and the varied radius of the deadly zone (Rdead). This means our model is not sensitive to these varibles. Thus, we can apply the 2D-IBM Model to analyze emergency events of different severity and different number of inﬂuenced people. Therefore, though the number of guests in the museum varies throughout the day and year, the results are stable.

<!-- b000260 | prose | pages [16, 17] -->
The third part of Figure 10 shows that the time of evacuation is not that stable when α(i) exit is smaller than 0.5. But if α(i) exit varies between 0.5 to 0.7, the evacuation time is nearly constant. We can conclude that our model is robust when the capacity of the exits is enough. However, if the capacity of each door becomes too small, evacuees have to wind their way to avoid potential congestion. Thus our model becomes a little unstable under such condition.

<!-- b000261 | furniture | pages [17] -->
Team # 1900007

<!-- b000262 | furniture | pages [17] -->
Page 15 of 26

<!-- b000264 | prose | pages [17] -->
The fourth part of Figure 10 reﬂects that the sum of people passing through exit #1 or #2 of the Louvre increases greatly as the density of people rises, while that of exit #3 or #4 is hardly affected. This diagram shows that the usage of exit #1 and #2 is near the saturation state, as apposed to exit #3 and exit #4, which are usually underused.

<!-- b000265 | heading | pages [17] -->
4 The 3D Cellular Automata Model (3D-CAM)

<!-- b000266 | heading | pages [17] -->
4.1 The Mechanism of the Model

<!-- b000267 | prose | pages [17] -->
The 2D-IBM Model is concise, but somehow too abstract. In order to simulate the evacuation process in an intuitive way, we build the 3D Cellular Automata Model (3D- CAM). In this model, we construct a 3D copy of the Louvre using AutoCAD, and then implement it into Pathﬁnder, a professional and mature software which simulates the evacuation process based on Celluar Automata Method. The 3D simulation clearly demonstrates the bottlenecks of evacuation on each ﬂoor and gives the heat map of the evacuation time in different places of each ﬂoor.

<!-- b000268 | caption | pages [17] -->
Figure 11: The Framewok of the 3D Cellular Automata Model(3D-CAM)

<!-- b000269 | furniture | pages [18] -->
Team # 1900007

<!-- b000270 | furniture | pages [18] -->
Page 16 of 26

<!-- b000271 | prose | pages [18] -->
The framework of the 3D-CAM Model is illustrated in Figure 11. As shown in this ﬁgure, the ﬂoor plan of the Louvre, location of staircases and exits and human behavior patterns are integrated to guide the evacuation. The 3D indoor space is divided into triangular cellular space[9], like Figure 12.

<!-- b000272 | caption | pages [18] -->
Figure 12: Triangular Cellular Space[9]

<!-- b000273 | prose | pages [18] -->
The search of evacuation routes for each individual is divided into two different modes, the SFPE Mode and the Steering Mode. Attributes of the two modes are shown in the ﬁgure. The mechanism of the former resembles our Basic Searching Model and the latter is like our Danger Index Model. After implementing the data and selecting a simulation mode, the Pathﬁnder software can provide visualized real-time condition of the evacuation process.

<!-- b000274 | heading | pages [18] -->
4.2 Visualized Result of the Model

<!-- b000275 | caption | pages [18] -->
Figure 13: The Heat Map of Evacuation Time in Different Places of Each Floor

<!-- b000276 | prose | pages [18] -->
After running the simulation, we can get the heat map of evacuation time in dif- ferent places of each ﬂoor. See Figure 13. The "hotter" a spot is, the longer it will take an individual to evacuate from that spot. Different colors in the heat map is of simi- lar meaning to the different "Danger Index" in our 2D-IBM Model. Comparing Figure 13 with Figure 9, we notice that the distribute of color is of the same trend, which indirectly proves that our Danger Index Model is reasonable.

<!-- b000277 | furniture | pages [19] -->
Team # 1900007

<!-- b000278 | furniture | pages [19] -->
Page 17 of 26

<!-- b000279 | heading | pages [19] -->
4.3 Determining the Potential Bottleneck

<!-- b000280 | prose | pages [19] -->
The Pathﬁnder simulation dynamically shows the real-time density of evacuees in a certain place, and forms the heat map of density on each ﬂoor. With the aid of it, we can easily ﬁgure out the bottlenecks on each ﬂoor, which are clearly shown in Figure 14, 15.

<!-- b000281 | prose | pages [19] -->
These bottlenecks are located either near staircases or close to exits, which makes sense. However, due to the difference of locations, not all the stairs or exits can be the potential bottleneck. For example, only a few evacuees choose to leave from distant exits.

<!-- b000282 | caption | pages [19] -->
Figure 14: The Potential Bottlenecks on each Floor

<!-- b000283 | caption | pages [19] -->
Figure 15: The Potential Bottlenecks–Focus

<!-- b000284 | furniture | pages [20] -->
Team # 1900007

<!-- b000285 | furniture | pages [20] -->
Page 18 of 26

<!-- b000286 | heading | pages [20] -->
5 Strengths and Weaknesses

<!-- b000287 | heading | pages [20] -->
5.1 Strengths

<!-- b000288 | heading | pages [20] -->
1. Our Dimensionality Reduction Method successfully planarizes the building, thus

<!-- b000289 | prose | pages [20] -->
simplifying the calculation greatly.

<!-- b000290 | heading | pages [20] -->
2. Our Basic Searching Model and Danger Index Model take the attributes of the

<!-- b000291 | prose | pages [20] -->
building into consideration (e.g. the capacity of exits, the distribution of stair- cases, etc.), so it can be adapted to other large and crowded structures easily.

<!-- b000292 | heading | pages [20] -->
3. Our Basic Searching Model and Danger Index Model consider many hominine

<!-- b000293 | prose | pages [20] -->
factors (e.g. the diversity of evacuees, the density of evacuees, etc.), so our routes can guarantee the evacuees’ security to a large extent.

<!-- b000294 | prose | pages [20] -->
4. Our model is not sensitive to the density of people and the severity of the emer- gency, which gurantees its robustness.

<!-- b000295 | heading | pages [20] -->
5. Our 3D Cellular Automata Model successfully constructs a well-designed 3D

<!-- b000296 | prose | pages [20] -->
model of Louvre, allowing the simulation to resemble the real-world situation.

<!-- b000297 | heading | pages [20] -->
5.2 Weaknesses

<!-- b000298 | heading | pages [20] -->
1. The Dijkstra Searching Method needs to call the searching function repeatedly,

<!-- b000299 | prose | pages [20] -->
leading to a comparatively high Time Complexity of the algorithm.

<!-- b000300 | heading | pages [20] -->
2. Our 2D Island-Bridge Model discretizes the spaces into nodes. The discretization

<!-- b000301 | prose | pages [20] -->
method replace the continuous movement of people with the leap between two adjacent nodes. This method deserves further justiﬁcation.

<!-- b000302 | heading | pages [20] -->
6 Conclusion: A Letter of Advice to the Emergency Man-

<!-- b000303 | prose | pages [20] -->
ager

<!-- b000304 | prose | pages [20] -->
Dear Sir/Madam,

<!-- b000305 | prose | pages [20] -->
We are a group of students participating in the 2019 ICM contest who chose the "Time to Leave the Louvre" problem. We would like to give some advice based on our work to better your evacuation plan.

<!-- b000306 | prose | pages [20, 21] -->
First of all, we think it’s crucial to add more dectectors and sensors in the mu- seum to monitor the density of evacuees and collect some other information. Plus, you should also suggest the visitors to utilize the positioning function of their smartphones to help you calculate their distance to each exit and the danger source. With these data in hand, you can have a good command of the real-time distribution of Danger Index in the building by our Danger Index Model. Then, you can work out the optimal evac- uation route for people in different places of the museum. It’s necessary to implement an evacuation navigation function in the "Afﬂuences" APP, so that everyone can get to know their own optimal route.

<!-- b000307 | furniture | pages [21] -->
Team # 1900007

<!-- b000308 | furniture | pages [21] -->
Page 19 of 26

<!-- b000310 | prose | pages [21] -->
Secondly, we strongly advice you to guarantee that the exits and stairs are not oc- cupied or stuck. Stairs and Exits play key roles in the evacuation process, and they are very likely to cause congestion or stagnation and become bottlenecks of evacuation.

<!-- b000311 | prose | pages [21] -->
Finally, we will be very glad if you can take time to read our paper and we hope our advice will be of help to you. If you have any questions, please feel free to ask us.

<!-- b000312 | prose | pages [21] -->
Sincerely,

<!-- b000313 | prose | pages [21] -->
Members of Team #1900007

<!-- b000314 | heading | pages [21] -->
References

<!-- b000315 | references | pages [21] -->
[1] Xiong, Q.; Zhu, Q.; Du, Z.; Zhu, X.; Zhang, Y.; Niu, L.; Li, Y.; Zhou, Y. A Dy-

<!-- b000316 | references | pages [21] -->
namic Indoor Field Model for Emergency Evacuation Simulation. ISPRS Interna-

<!-- b000317 | references | pages [21] -->
tional Journal of Geo-Information, 2017, 6, 104.

<!-- b000318 | references | pages [21] -->
[2] Lo, S.M.; Fang, Z.; Chen, D.H. Use of a modiﬁed network model for analyzing

<!-- b000319 | references | pages [21] -->
evacuation patterns in high-rise buildings. J. Archit. Eng, 2001, 7, 21–29.

<!-- b000320 | references | pages [21] -->
[3] Helbing, D.; Farkas, I.; Vicsek, T. Simulating dynamical features of escape panic.

<!-- b000321 | references | pages [21] -->
Nature, 2000, 407, 487–490.

<!-- b000322 | references | pages [21] -->
[4] Kirchner, A.; Schadschneider, A. Simulation of evacuation processes using a

<!-- b000323 | references | pages [21] -->
bionics-inspired cellular automaton model for pedestrian dynamics. Phys. A Stat.

<!-- b000324 | references | pages [21] -->
Mech. Appl., 2002, 312, 260–276.

<!-- b000325 | references | pages [21] -->
[5] FENG Weiwei; QIU Jiong. Application of Ant Colony Algorithm in Fire Evacua-

<!-- b000326 | references | pages [21] -->
tion Platform(in Chinese). Electronic Science and Technology., 2015, 4, 13-16.

<!-- b000327 | references | pages [21] -->
[6] Louvre 2014 Annual Report.pdf.

<!-- b000328 | references | pages [21] -->
https://www.louvre.fr/sites/default/files/rapport_activite/

<!-- b000329 | references | pages [21] -->
fichiers/PDF/louvre-2014-annual-report.pdf

<!-- b000330 | references | pages [21] -->
[7] Louvre Plan Visitors Mobility Impairments.pdf.

<!-- b000331 | references | pages [21] -->
https://www.louvre.fr/sites/default/files/medias/

<!-- b000332 | references | pages [21] -->
medias_fichiers/fichiers/pdf/louvre-plan-visitors-

<!-- b000333 | references | pages [21] -->
mobility-impairments.pdf

<!-- b000334 | references | pages [21] -->
[8] Louvre Interactive Floor Plans.

<!-- b000335 | references | pages [21] -->
https://www.louvre.fr/en/plan

<!-- b000336 | references | pages [21] -->
[9] Pathﬁnder 2012 Technical Reference.pdf.

<!-- b000337 | furniture | pages [22] -->
Team # 1900007

<!-- b000338 | furniture | pages [22] -->
Page 20 of 26

<!-- b000339 | heading | pages [22] -->
Appendices

<!-- b000340 | prose | pages [22] -->
A Our Simulation Codes Written in MATLAB

<!-- b000341 | prose | pages [22] -->
DijkstraMain.m 1 clear a l l 2 c l c 3 load ( ’node . mat ’ ) ; 4 C=X; 5 n=size (C, 1 ) ; 6 D=zeros (n , n) ; 7 8 viewpoint =21; 9 emerg =[580 ,550]; 10 s c a t t e r ( emerg ( 1 , 1 ) , emerg ( 1 , 2 ) ,100 , ’ r ’ , ’ f i l l e d ’ ) ; 11 hold on 12 thread =30; 13 totalpeople =0; 14 t o t a l d i s t a n c e =0; 15 e = [ 0 , 0 , 0 , 0 ] ; 16 alphaexit =0.35; 17 dens =0.4; 18 Contain=alphaexit ∗3700∗dens ; 19 for i =1:n 20 for j =1:n 21 i f i ~= j 22 D( i , j )=sqrt ( (C( i , 1 )−C( j , 1 ) ) ^2+(C( i , 2 )−C( j , 2 ) ) ^2) ; 23 else 24 D( i , j ) =0; 25 end 26 D( j , i )=D( i , j ) ; 27 end 28 end 29 30 for i =1:n 31 for j =1:n 32 i f D( i , j )>viewpoint||sqrt ( (C( i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i , 2 )−emerg ( 1 , 2 ) ) ^2)<= thread 33 D( i , j )=inf ; 34 end 35 end 36 end 37 38 39 for i i =1:3700 rand<=dens&&(sqrt ( (C( i i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i i , 2 )−emerg ( 1 , 2 ) ) ^2)>thread ) 40 i f 41 s t a r t = i i ; 42 totalpeople=totalpeople +1; 43 e x i t =X( 3 7 0 1 : 3 7 0 4 , : ) ; 44 45 i f e ( 1 , 1 )<=Contain 46 [ mydistance1 , mypath1]= Djsk (D, start ,3701) ; 47 else 48 mydistance1=inf ;

<!-- b000342 | furniture | pages [23] -->
Team # 1900007

<!-- b000343 | furniture | pages [23] -->
Page 21 of 26

<!-- b000344 | prose | pages [23] -->
49 end 50 51 i f e ( 1 , 2 )<=Contain 52 [ mydistance2 , mypath2]= Djsk (D, start ,3702) ; 53 else 54 mydistance2=inf ; 55 end 56 57 i f e ( 1 , 3 )<=Contain 58 [ mydistance3 , mypath3]= Djsk (D, start ,3703) ; 59 else 60 mydistance3=inf ; 61 end 62 63 i f e ( 1 , 4 )<=Contain 64 [ mydistance4 , mypath4]= Djsk (D, start ,3704) ; 65 else 66 mydistance4=inf ; 67 end 68 Pd=[ mydistance1 , mydistance2 , mydistance3 , mydistance4 ] ; 69 [ value , index ]=min(Pd) ; 70 [ mydistance , mypath]= Djsk (D, start ,3700+ index ) ; 71 e (1 , index )=e (1 , index ) +1; 72 t o t a l d i s t a n c e = t o t a l d i s t a n c e +value ; 73 Xp = [ ] ; Yp = [ ] ; 74 for i =1: size ( mypath , 2 ) 75 Xp=[Xp,C( mypath ( i ) ,1) ] ; 76 Yp=[Yp,C( mypath ( i ) ,2) ] ; 77 end 78 s c a t t e r (C( : , 1 ) ,C( : , 2 ) , ’b . ’ ) ; 79 hold on 80 s c a t t e r ( e x i t ( : , 1 ) , e x i t ( : , 2 ) ,100 , ’p ’ , ’ f i l l e d ’ ) ; 81 hold on 82 plot (Xp, Yp) ; 83 hold on 84 end 85 xlabel ( ’x/m’ ) ; 86 ylabel ( ’y/m’ ) ; 87 end

<!-- b000345 | prose | pages [23, 24] -->
Djsk.m function [ res , index ] = Djsk (mp, stat , ends ) 1 n=size (mp, 1 ) ; 2 bj=zeros (n , 1 ) ; 3 dis=mp( stat , : ) ; 4 path=ones (n , 1 ) ; path=path . ∗s t a t ; 5 dis ( s t a t ) =0; bj ( s t a t ) =1; 6 for i =1:n 7 min=Inf ; k=1; 8 for j =1:n 9 i f ( bj ( j ) ~=1)&&(dis ( j )<min) ,min=dis ( j ) ; k= j ; end 10 end 11 bj ( k ) =1; 12 for j =1:n 13 i f ( bj ( j ) ~=1)&&(dis ( j ) >( dis ( k )+mp(k , j ) ) ) , dis ( j )=dis ( k )+mp(k , j ) ; path ( j )=k ; 14 end end 15 end 16 tem=ends ; index ( 1 ) =ends ; i =2; 17 while path ( tem )~= s t a t 18 index ( i )=path ( tem ) ; 19 tem=path ( tem ) ; 20 i = i +1; 21 end 22 index ( i )= s t a t ; index=index ( length ( index ) : −1:1) ; res=dis ( ends ) ; 23 end 24

<!-- b000346 | furniture | pages [24] -->
Team # 1900007

<!-- b000347 | furniture | pages [24] -->
Page 22 of 26

<!-- b000349 | prose | pages [24, 25] -->
DangerIndex.m 1 clear a l l 2 c l c 3 load ( ’node . mat ’ ) ; 4 emerg =[580 ,550]; 5 X=[X; emerg ] ; 6 C=X; 7 n=size (C, 1 ) ; 8 totaldens =0.4; 9 viewpoint =21; 10 C=[C, zeros (n , 1 ) ] ; 11 hold on 12 thread =0; 13 e = [ 0 , 0 , 0 , 0 ] ; 14 Rfield =21; 15 Nfield=zeros (n , 1 ) ; 16 17 rho=zeros (3700 ,1) ; 18 Wemerg=zeros (3700 ,1) ; 19 Wexit=zeros (3700 ,1) ; 20 Neg=zeros (3700 ,1) ; 21 22 23 for i =1:n 24 for j =1:n 25 i f i ~= j 26 D( i , j )=sqrt ( (C( i , 1 )−C( j , 1 ) ) ^2+(C( i , 2 )−C( j , 2 ) ) ^2) ; 27 else 28 D( i , j ) =0; 29 end 30 D( j , i )=D( i , j ) ; 31 end 32 end 33 34 for i =1:n 35 for j =1:n 36 i f D( i , j )>viewpoint||sqrt ( (C( i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i , 2 )−emerg ( 1 , 2 ) ) ^2)<= thread 37 D( i , j )=inf ; 38 end 39 end 40 end 41 42 for i =1:3700 rand<=totaldens&&(sqrt ( (C( i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i , 2 )−emerg ( 1 , 2 ) ) ^2)> 43 i f thread ) 44 C( i , 3 ) =1; 45 end 46 end 47 48 for i =1:3700 j =max(1 , i −64) : min( i +64 ,3700) 49 for ( sqrt ( (C( i , 1 )−C( j , 1 ) ) ^2+(C( i , 2 )−C( j , 2 ) ) ^2) <=21)&&(C( j , 3 ) ==1) 50 i f 51 Nfield ( i , 1 ) =Nfield ( i , 1 ) +1; 52 end 53 end 54 end 55 for i =1:3700 56 s t a r t = i ; 57 e x i t =X( 3 7 0 1 : 3 7 0 4 , : ) ; 58 [ mydistance1 , mypath1]= Djsk (D, start ,3701) ; 59 [ mydistance2 , mypath2]= Djsk (D, start ,3702) ; 60 [ mydistance3 , mypath3]= Djsk (D, start ,3703) ; 61 [ mydistance4 , mypath4]= Djsk (D, start ,3704) ; 62 Pd=[ mydistance1 , mydistance2 , mydistance3 , mydistance4 ] ; 63 [ value , index ]=min(Pd) ; 64 Wexit ( i , 1 ) =value ; 65 disemerg=sqrt ( (C( i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i , 2 )−emerg ( 1 , 2 ) ) ^2) ; 66 Wemerg( i , 1 ) =1/disemerg ; 67 68 69 end 70 71 for i =1:3700 72 rho ( i , 1 ) =Nfield ( i , 1 ) /( pi ∗Rfield ^2) ; 73 end 74 75 a=10^2; 76 b=10^4; 77 c =1; 78 79 for i =1:3700 80 Neg( i , 1 ) =a∗rho ( i , 1 ) +b∗Wemerg( i , 1 ) +c∗Wexit ( i , 1 ) ; 81 end 82 83 f1 =1:600; 84 f2 =1:1000; 85 [ F1 , F2]= meshgrid ( f1 , f2 ) ; 86 F3=zeros (600 ,1000) ; 87 F1=F1 ’ ; F2=F2 ’ ; 88 for i =1:600 89 for j =1:1000 90 for i i =1:3700 91 i f i ==X( i i , 1 )&&j ==X( i i , 2 ) 92 F3 ( i , j )=Neg( i i , 1 ) ; 93 end 94 end 95 end 96 end 97 98 mesh( F1 , F2 , F3 ) ;

<!-- b000350 | furniture | pages [25] -->
Team # 1900007

<!-- b000351 | furniture | pages [25] -->
Page 23 of 26

<!-- b000353 | prose | pages [25, 26, 27] -->
NodeFormation.m 1 cnt =1; 2 X= [ ] ; 3 for i =1:64 4 for j =1:5 5 X( cnt , 1 ) =10∗( i −1) +5; 6 X( cnt , 2 ) =10∗( j −1) +5; 7 cnt=cnt +1; 8 end 9 end 10 for i =1:23 11 for j =1:6 12 X( cnt , 1 ) =10∗( i −1) +420; 13 X( cnt , 2 ) =10∗( j −1) +60; 14 cnt=cnt +1; 15 end 16 end 17 for i =1:64 18 for j =1:4 19 X( cnt , 1 ) =10∗( i −1) +5; 20 X( cnt , 2 ) =10∗( j −1) +130; 21 cnt=cnt +1; 22 end 23 end 24 for i =1:4 25 for j =1:18 26 X( cnt , 1 ) =5∗( i −1) +553; 27 X( cnt , 2 ) =5∗( j −1) +175; 28 cnt=cnt +1; 29 end 30 end 31 for i =1:64 32 for j =1:5 33 X( cnt , 1 ) =10∗( i −1) +5; 34 X( cnt , 2 ) =10∗( j −1) +270; 35 cnt=cnt +1; 36 end 37 end 38 for i =1:17 39 for j =1:6 40 X( cnt , 1 ) =10∗( i −1) +480; 41 X( cnt , 2 ) =10∗( j −1) +320; 42 cnt=cnt +1; 43 end 44 end 45 for i =1:64 46 for j =1:5 47 X( cnt , 1 ) =10∗( i −1) +5; 48 X( cnt , 2 ) =10∗( j −1) +390; 49 cnt=cnt +1; 50 end 51 end 52 for i =1:4 53 for j =1:4 54 X( cnt , 1 ) =5∗( i −1) +553; 55 X( cnt , 2 ) =5∗( j −1) +435; 56 cnt=cnt +1; 57 end 58 end 59 for i =1:64 60 for j =1:5 61 X( cnt , 1 ) =10∗( i −1) +5; 62 X( cnt , 2 ) =10∗( j −1) +460; 63 cnt=cnt +1; 64 end 65 end 66 for i =1:17 67 for j =1:7 68 X( cnt , 1 ) =10∗( i −1) +480; 69 X( cnt , 2 ) =10∗( j −1) +510; 70 cnt=cnt +1; 71 end 72 end 73 for i =1:64 74 for j =1:4 75 X( cnt , 1 ) =10∗( i −1) +5; 76 X( cnt , 2 ) =10∗( j −1) +580; 77 cnt=cnt +1; 78 end 79 end 80 for i =1:4 81 for j =1:2 82 X( cnt , 1 ) =5∗( i −1) +553; 83 X( cnt , 2 ) =5∗( j −1) +625; 84 cnt=cnt +1; 85 end 86 end 87 for i =1:64 88 for j =1:4 89 X( cnt , 1 ) =10∗( i −1) +5; 90 X( cnt , 2 ) =10∗( j −1) +640; 91 cnt=cnt +1; 92 end 93 end 94 for i =1:17 95 for j =1:6 96 X( cnt , 1 ) =10∗( i −1) +480; 97 X( cnt , 2 ) =10∗( j −1) +690; 98 cnt=cnt +1; 99 end 100 end 101 for i =1:64 102 for j =1:5 103 X( cnt , 1 ) =10∗( i −1) +5; 104 X( cnt , 2 ) =10∗( j −1) +755; 105 cnt=cnt +1; 106 end 107 end 108 for i =1:4 109 for j =1:4 110 X( cnt , 1 ) =5∗( i −1) +553; 111 X( cnt , 2 ) =5∗( j −1) +805; 112 cnt=cnt +1; 113 end 114 end 115 for i =1:64 116 for j =1:5 117 X( cnt , 1 ) =10∗( i −1) +5; 118 X( cnt , 2 ) =10∗( j −1) +825; 119 cnt=cnt +1; 120 end 121 end 122 for i =1:17 123 for j =1:7 124 X( cnt , 1 ) =10∗( i −1) +480;

<!-- b000354 | furniture | pages [26] -->
Team # 1900007

<!-- b000355 | furniture | pages [26] -->
Page 24 of 26

<!-- b000357 | furniture | pages [27] -->
Team # 1900007

<!-- b000358 | furniture | pages [27] -->
Page 25 of 26

<!-- b000360 | furniture | pages [28] -->
Team # 1900007

<!-- b000361 | furniture | pages [28] -->
Page 26 of 26

<!-- b000362 | prose | pages [28] -->
125 X( cnt , 2 ) =10∗( j −1) +875; 126 cnt=cnt +1; 127 end 128 end 129 for i =1:64 130 for j =1:5 131 X( cnt , 1 ) =10∗( i −1) +5; 132 X( cnt , 2 ) =10∗( j −1) +945; 133 cnt=cnt +1; 134 end 135 end 136 X( 3 7 0 1 , : ) =[478 ,536]; 137 X( 3 7 0 2 , : ) =[404 ,622]; 138 X( 3 7 0 3 , : ) =[324 ,623]; 139 X( 3 7 0 4 , : ) =[113 ,454];
