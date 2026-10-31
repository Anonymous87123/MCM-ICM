# P-D-2019-1900007-65267201

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
1900007

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
D

<!-- b000015 | prose | pages [1] -->
2019 2019 MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | title | pages [1] -->
Analysis of the Optimal Evacuation Plan Based on 2D

<!-- b000018 | title | pages [1] -->
and 3D Models

<!-- b000019 | heading | pages [1] -->
Summary

<!-- b000020 | prose | pages [1] -->
We are tasked to analyze the optimal evacuation plan for the Louvre. To this end, we con- struct both the 2D model and the 3D model to derive the optimal plan. We successfully utilize our models to determine the potential bottlenecks, plan the use of additional exits and let the emergency personnel enter. We take three dimensions of factors into account: the diversity of evacuees (e.g. the disabled, the elderly, etc.), people’s behaviors and the attributes of the build- ing. We provide sufﬁcient visualized results in order to explain our model intuitively.

<!-- b000021 | prose | pages [1] -->
In the 2D Island-Bridge Model, we reasonably planarize the building and discretize the space into dense nodes. Then, we construct the Basic Searching Submodel to calculate the optimal evacuation route and time for different varieties of people. We also form a method to solve the unbalanced usage of each exit. Then, we form the Danger Index Submodel, which gives insight to the real-time distribution of Danger Index in the building. Furthermore, we utilize these submodels to answer how to take advantage of additional exits and how to let the emergency personnel enter. Finally, we carry out the sensitivity analysis by operating our 2D model under different density of people and different inﬂuential range of danger. The re- sult is stable despite these differences, which proves the robustness of the 2D model. Since the methodology of this model always holds true, it can be adapted to different buildings with only slight adjustments.

<!-- b000022 | prose | pages [1] -->
In the 3D Celluar Automata Model, we precisely construct a 3D copy of the Louvre using AutoCAD, which makes our simulation resemble the real-world situation. We implement the model in Pathﬁnder software and carry out 3D simulation. The results clearly demonstrate that the bottlenecks are all around exits or stairs. We also give a heat map of the evacuation time in different places of each ﬂoor.

<!-- b000023 | prose | pages [1] -->
As a conclusion, we write a letter of advice to the emergency manager, offering some prac- tical suggestions about the evacuation plan.

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | heading | pages [2] -->
Introduction

<!-- b000027 | prose | pages [2] -->
1 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 1 Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 1 Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000028 | prose | pages [2] -->
2

<!-- b000029 | heading | pages [2] -->
Preparation of the Models

<!-- b000030 | prose | pages [2] -->
1

<!-- b000031 | prose | pages [2] -->
3 Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 3 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000032 | prose | pages [2] -->
3

<!-- b000033 | heading | pages [2] -->
The 2D Island-Bridge Model (2D-IBM)

<!-- b000034 | prose | pages [2] -->
4

<!-- b000035 | prose | pages [2] -->
4 Basic Structure of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4 Dimensionality Reduction Method . . . . . . . . . . . . . . . . . . . . . . 3.2 6 Spacial Discretization Method . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 7 Basic Searching Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 8 Danger Index Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.5 11 How to Utilize Additional Exits? . . . . . . . . . . . . . . . . . . . . . . . 3.6 13 How to Let Emergency Personnel Enter? . . . . . . . . . . . . . . . . . . . 3.7 13 Model Evaluation and Sensitivity Analysis 3.8 . . . . . . . . . . . . . . . . .

<!-- b000036 | prose | pages [2] -->
14

<!-- b000037 | heading | pages [2] -->
The 3D Cellular Automata Model (3D-CAM)

<!-- b000038 | prose | pages [2] -->
4 15 The Mechanism of the Model . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 15 . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Visualized Result of the Model 16 Determining the Potential Bottleneck . . . . . . . . . . . . . . . . . . . . . 4.3

<!-- b000039 | prose | pages [2] -->
5

<!-- b000040 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000041 | prose | pages [2] -->
17

<!-- b000042 | prose | pages [2] -->
18 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 Weaknesses 18

<!-- b000043 | heading | pages [2] -->
Conclusion: A Letter of Advice to the Emergency Manager

<!-- b000044 | prose | pages [2] -->
6

<!-- b000045 | heading | pages [2] -->
References

<!-- b000046 | heading | pages [2] -->
Appendices

<!-- b000047 | prose | pages [2] -->
18

<!-- b000048 | prose | pages [2] -->
19

<!-- b000049 | prose | pages [2] -->
20

<!-- b000050 | prose | pages [2] -->
A Our Simulation Codes Written in MATLAB 20

<!-- b000051 | furniture | pages [3] -->
Team # 1900007

<!-- b000052 | furniture | pages [3] -->
Page 1 of 26

<!-- b000053 | prose | pages [3] -->
1

<!-- b000054 | heading | pages [3] -->
Introduction

<!-- b000055 | prose | pages [3] -->
1.1 Restatement of the Problem

<!-- b000056 | prose | pages [3] -->
In France alone, there have been at least 12 major terror-related incidents since 2012, and the number is still increasing. In face of an emergency, panic-stricken people, if not properly guided, tend to ﬂee around like headless chickens, causing massive chaos at the scene. The mayhem could hurt even more than the attack itself, especially in crowded space such as indoor museums like the Louvre. Therefore, establishing an effecitve emergency evacuation plan is critical as to eliminate unnecessary disorder and casualties. Here, we are required to design a model to guide evacuation from the Louvre or other multi-storey buildings.

<!-- b000057 | prose | pages [3] -->
There are three major objectives:

<!-- b000058 | prose | pages [3] -->
• Find the optimal evacuation plan, which means enabling people to evacuate the buliding in the fastest and safest manner, as well as allowing emergency per- sonnel to enter as quickly as possible.

<!-- b000059 | prose | pages [3] -->
• Determine the potential bottlenecks that may cause congestion and stagnation. In our model, a bottleneck is deﬁned as a particular location where the passing speed is extremely slow.

<!-- b000060 | prose | pages [3] -->
• Universalize the model, that is, adjust our model so that it can be adapted to a broad set of potential threats.

<!-- b000061 | prose | pages [3] -->
1.2 Literature Review

<!-- b000062 | prose | pages [3] -->
Based on the differences in mechanisms of spacial movement, current models of indoor emergency evacuation can be divided into four catagories[1]: network-based models, particle-based models, cellular-based models and ant-based models.

<!-- b000063 | prose | pages [3] -->
The network-based model simpliﬁed evacuation as a ﬂow of people moving at a certain speed in the network[2]. The particle-based model considered people as self- driving particles controlled by various internal and external forces[3]. The cellular- based model employed cellular automata theory to simulate the evacuation process by the spatio-temporal modeling method[4]. The ant-based model utilized ant colony algorithm, to perceive the real-time change and ﬁnd the optimal path in a dynamic way[5].

<!-- b000064 | prose | pages [3] -->
1.3 Our work

<!-- b000065 | prose | pages [3] -->
We construct two distinctive models: the 2D Island-Bridge Model (2D-IBM) and the 3D Cellular Automata Model (3D-CAM).

<!-- b000066 | heading | pages [3] -->
In the 2D Island-Bridge Model (2D-IBM), we develop the following methods or

<!-- b000067 | prose | pages [3] -->
submodels in four steps.

<!-- b000068 | furniture | pages [4] -->
Team # 1900007

<!-- b000069 | furniture | pages [4] -->
Page 2 of 26

<!-- b000070 | prose | pages [4] -->
First, we develop a Dimensionality Reduction Method, which planarizes the move- ment on 3D multi-storey building as equivalent 2D horizontal motion. Secondly, we establish the Spacial Discretization Method. We discretize the space of the 2D "build- ing" into dense nodes with certain coordinates. People are designed to move from one node to the other. Thirdly, we form a Basic Searching Model, which bases the evacuees’ route choice on three factors: their distance from each exit, their distance from the source of danger and the maximum capacity of each exit. We use it to solve the problem of congestion around exits, which is a potential bottleneck. The Dijkstra Searching Algorithm is utilized in this model. Fourthly, we form the Danger Index Model, which can provide the real-time distribution of Danger Index in the buiding. Thus, the emergency manager can have a direct understanding of emergency. In this model, the density of evacuees in each mesh are also included, thus adding the degree of congestion and stagnation into consideration.

<!-- b000071 | prose | pages [4] -->
After completing the construction of the 2D-IBM Model, we employ it to discuss problems of how to utilize additional exits and how to let emergency personnel enter. Finally, we carry out the sensitivity analysis and validate that our 2D-IBM Model stays robust despite the changes of the attributes of the building, the location of the danger source, the inﬂuence range of danger and the density of people.

<!-- b000072 | prose | pages [4] -->
In the the 3D Celluar Automata Model, we construct a 3D model of the Louvre using AutoCAD, and then implement it into Pathﬁnder, a professional and mature software, to simulate the evacuation process based on Celluar Automata Method. The 3D simulation clearly demonstrates the bottlenecks of evacuation and provide some other useful data.

<!-- b000073 | prose | pages [4] -->
All in all, we take a wide varieties of factors into consideration, including the di- versity of evacuees, human behavior patterns, and building information. The speciﬁc factors we consider are shown in Figure 1.

<!-- b000074 | caption | pages [4] -->
Figure 1: The Factors that We Take into Account

<!-- b000075 | furniture | pages [5] -->
Team # 1900007

<!-- b000076 | furniture | pages [5] -->
Page 3 of 26

<!-- b000077 | prose | pages [5] -->
2

<!-- b000078 | heading | pages [5] -->
Preparation of the Models

<!-- b000079 | prose | pages [5] -->
2.1

<!-- b000080 | heading | pages [5] -->
Assumptions

<!-- b000081 | prose | pages [5] -->
It is difﬁcult to study the actual situation in the Louvre because of the irregular shape of the building, the extreme complication of interior structure and the unpre- dictability of human behavior. In order to simplify the problem and to hold the cor- rectness of results at the same time, we make the assumptions below:

<!-- b000082 | prose | pages [5] -->
(If there is no special explanation, the assumptions below are applied to both the 2D-IBM and the 3D-CAM Model. )

<!-- b000083 | heading | pages [5] -->
1. We simplify the shape of the Louvre museum, viewing each storey as a stan-

<!-- b000084 | prose | pages [5] -->
dard, two-dimensional ’U’ shape composed of three rectangles (the grey area).

<!-- b000085 | heading | pages [5] -->
[Only Applicable in the 2D-IBM Model]

<!-- b000086 | prose | pages [5] -->
The exact data are labeled in Figure 2. With careful calculation, we set the total area of the simpliﬁed storey almost the same as that of the real-world condition. Therefore, the range of movement holds the same.

<!-- b000087 | caption | pages [5] -->
Figure 2: The Simpliﬁed Storey in the Louvre

<!-- b000088 | heading | pages [5] -->
2. We assume that EVERY place of the simpliﬁed storey is walkable.

<!-- b000089 | prose | pages [5] -->
That is to say, we ignore the physical barriers (e.g. exhibits) in the way, because we can hardly know the exact distribution of exhibits and other facilities. The only barrier of movement we consider is the boundaries and the source of danger.

<!-- b000090 | heading | pages [5] -->
3. We treat every staircase and every escalator as identical, and suppose that they

<!-- b000091 | prose | pages [5] -->
both function as two-way stairs in case of emergency. First, it is understandable that escalators will be shut down in case of emergency, made to function the same as staircases. Therefore, staircases and escalators are treated equally as passageways between two storeys. Plus, we assume that pas- sageways between two storeys share completely identical attributes for simplicity.

<!-- b000092 | heading | pages [5] -->
4. We regard the initial distribution of evacuees as random.

<!-- b000093 | prose | pages [5] -->
Though there might be more people piling up in front of some world-renowned

<!-- b000094 | furniture | pages [6] -->
Team # 1900007

<!-- b000095 | furniture | pages [6] -->
Page 4 of 26

<!-- b000096 | prose | pages [6] -->
masterpiece (e.g. the Mona Lisa), the cumulative effect is localized and small- scale. Compared to a total of 400,000 art works in the Louvre, the masterpiece which may cause cumulative effect resembles a drop in the ocean. Thus, random initial distribution of people is a reasonable assumption.

<!-- b000097 | heading | pages [6] -->
5. We suppose that evacuees become aware of the emergency and start escaping

<!-- b000098 | prose | pages [6] -->
simultaneously. Plus, they will follow the guidance. That is, ﬁrst, we ignore the time lag of knowing the emergency, because it is tiny compared to the whole evacuation process. Second, if evacuees do not follow the guidance, their behavior will become unpredictable, and the evacuation plan will be of little use.

<!-- b000099 | heading | pages [6] -->
6. We regard different evacuees as points with different attributes moving in the

<!-- b000100 | heading | pages [6] -->
two-dimensional space. [Only Applicable in the 2D-IBM Model]

<!-- b000101 | prose | pages [6] -->
This assumption is a complement of the "simpliﬁed storey assumption" (assump- tion 1) discussed above. It should be stressed that, each point of evacuee, though abstracted, still has its distinctive human characteristics. For example, the maxi- mum speed of the point representing the elderly is slower than that of the young "point".

<!-- b000102 | heading | pages [6] -->
7. The data provided by the Louvre are representative.

<!-- b000103 | prose | pages [6] -->
Though the most recent annual report of the Louvre[6] was updated in 2014, we still assume these data are representative and ignore the potential errors related to them. Some important data we will use are listed in Table 1.

<!-- b000104 | caption | pages [6] -->
Table 1: Some Important Data about the Louvre

<!-- b000105 | prose | pages [6] -->
Item Data

<!-- b000106 | prose | pages [6] -->
Visitors per Year 9.3 million Ratio of Young and not Disabled Visitors 72.1% Ratio of Old and not Disabled Visitors 21.1% Ratio of Disabled Visitors

<!-- b000107 | prose | pages [6] -->
2.2

<!-- b000108 | heading | pages [6] -->
Notation

<!-- b000109 | prose | pages [6] -->
6.8%

<!-- b000110 | prose | pages [6] -->
The primary notations in our paper are listed in Table 2. There can be some other notations to be deﬁned later.

<!-- b000111 | heading | pages [6] -->
The 2D Island-Bridge Model (2D-IBM)

<!-- b000112 | prose | pages [6] -->
3

<!-- b000113 | prose | pages [6] -->
3.1

<!-- b000114 | heading | pages [6] -->
Basic Structure of the Model

<!-- b000115 | heading | pages [6] -->
In the 2D Island-Bridge Model (2D-IBM), we develop the following methods and

<!-- b000116 | prose | pages [6] -->
submodels subsequently.

<!-- b000117 | furniture | pages [7] -->
Team # 1900007

<!-- b000118 | furniture | pages [7] -->
Page 5 of 26

<!-- b000119 | caption | pages [7] -->
Table 2: Notation

<!-- b000120 | prose | pages [7] -->
Symbol Deﬁnition

<!-- b000121 | prose | pages [7] -->
dis(i, j) the distance between node i and node j e(i,j) the weight of edge between node i and node j Rdead the radius of deadly area which can not be entered Snode the sum of nodes Speople the sum of people indoor in the case of emergency ρpeople the density of people indoor in the case of emergency Sdis the sum of distance travelled by all evacuees Vrange the maximum visual range of an individual α(s)

<!-- b000122 | prose | pages [7] -->
the maximum ratio of people exiting from exit s exit (an independent variable reﬂecting the attribute of exit s) S(s)

<!-- b000123 | prose | pages [7] -->
the number of people exiting from exit s exit tindividual the average time for each individual to evacuate telderly the average time for each elder to evacuate tyouth the average time for each young people to evacuate tdisabled the average time for each disabled people to evacuate Rmesh the radius of each single mesh N (i)

<!-- b000124 | prose | pages [7] -->
the number of people in mesh i mesh w(i)

<!-- b000125 | prose | pages [7] -->
the density weight of mesh i density w(i)

<!-- b000126 | prose | pages [7] -->
the emergency weight of mesh i emergency w(i)

<!-- b000127 | prose | pages [7] -->
the exit weight of mesh i exit DI(i) the danger index of mesh i

<!-- b000128 | prose | pages [7] -->
• Step 1: We develop a Dimensionality Reduction Method, which planarizes the movement on staircases as equivalent 2D horizontal motion. Based on this method, we substitute the multi-storey building into a 2D planar space. Each storey resembles an "island", and each staircase resembles a "bridge" connecting two islands. See Figure 3.

<!-- b000129 | prose | pages [7] -->
• Step 2: We establish the Spacial Discretization Method. We discretize the space of the "island" into dense nodes, and then place the "island" in a rectangular co- ordinate system to get the coordinate of each node. We save these nodes’ coordi- nates in the form of matrix for the sake of programming. People are designed to move from one node to the other.

<!-- b000130 | prose | pages [7] -->
• Step 3: We build a Basic Searching Model, which bases the evacuees’ route choice on three factors: their distance from each exit, their distance from the source of danger and the maximum capacity of each exit. We also take into ac- count the diversity of visitors, such as the elderly, the disabled, etc. Then, we uti-

<!-- b000131 | heading | pages [7] -->
lize Dijkstra Searching Algorithm to implement the model in MATLAB. After

<!-- b000132 | prose | pages [7] -->
randomly distributing people in the "building" and selecting a source of danger, we simulate the optimal evacuation route for every individual, and visualize the result.

<!-- b000133 | prose | pages [7] -->
• Step 4: We optimize the Basic Searching Model and form the Field-based Model In this reﬁned model, we add the degree of congestion and stagnation into con- sideration by measuring the density of evacuees in each mesh. Then, We calculate

<!-- b000134 | furniture | pages [8] -->
Team # 1900007

<!-- b000135 | furniture | pages [8] -->
Page 6 of 26

<!-- b000136 | caption | pages [8] -->
Figure 3: Schematic Diagram of the Dimensionality Reduction Method. Each storey resembles

<!-- b000137 | prose | pages [8] -->
an island, and each staircase resembles a bridge connecting two "island"s.

<!-- b000138 | prose | pages [8] -->
the weight of each mesh in terms of the inﬂuence exerted by density of people, distance from danger and distance from exits. After that, we combine the three kind of weight to form Danger Index (DI) of each mesh, and calculate it. Finally, we visualize the result with a heat map.

<!-- b000139 | prose | pages [8] -->
Dimensionality Reduction Method 3.2

<!-- b000140 | heading | pages [8] -->
The philosophy of the 2D Island-Bridge Model (2D-IBM) is dimensionality reduc-

<!-- b000141 | prose | pages [8] -->
tion. Dimensionality reduction is the process of reducing the number of irrelevant variables in order to obtain a set of principal variables which can reﬂect the attributes of the high dimensional object. For example, the sun shines through leaves (high dimen- sion, 3D), casting shadow (low dimension, 2D) on the ground. Despite the dimension of shadow is lower than that of leaves, you can still have a rough idea of the leaves’ shape. In other words, it is feasible to simulate the core attributes of high-dimensional objects with low-dimentional ones.

<!-- b000142 | prose | pages [8] -->
Back to our problem, evacuees move both horizontally and vertically on stairs, which is a 3D motion. Our Dimensionality Reduction Method seeks to planarize the movement on stairs as 2D horizontal motion.

<!-- b000143 | prose | pages [8] -->
We abstract all the stairs between two storeys as "bound-together", and then choose a "junction point" on either storey. We take the distance between each stair and "junc- tion point" into account. Then we calculate the equivalent length and width of the planarized "bound-together" stair with the equations below:

<!-- b000144 | prose | pages [8] -->
dis(i, junc) ηi = Pn

<!-- b000145 | prose | pages [8] -->
(1) i=1 dis(i, junc)

<!-- b000146 | prose | pages [8] -->
(Length)eq = 1

<!-- b000147 | prose | pages [8] -->
n ·

<!-- b000148 | prose | pages [8] -->
n X

<!-- b000149 | prose | pages [8] -->
[ηi · (length)i]

<!-- b000150 | prose | pages [8] -->
i=1

<!-- b000151 | furniture | pages [9] -->
Team # 1900007

<!-- b000152 | furniture | pages [9] -->
Page 7 of 26

<!-- b000153 | prose | pages [9] -->
(Width)eq = (width)i (3)

<!-- b000154 | prose | pages [9] -->
where n is the number of stairs between two neighbouring storeys, i is the serial num- ber of a stair, and dis(i, junc) is the distance between the "junction point" and stair # i, (length)i and (width)i are the original length and width of stair # i.

<!-- b000155 | prose | pages [9] -->
In Equation (1), ηi ∈[0, 1] is the normalized distribution coefﬁcient, which has a positive correlation with the equivalent length. And ηi · (length)i represents the weighed length of each stair. Therefore, Equation (2) represents the ultimate equiv- alent length between two storeys.

<!-- b000156 | prose | pages [9] -->
According to Assumption 3, we treat every staircase as identical, so the equations can be simpliﬁed as below.

<!-- b000157 | prose | pages [9] -->
(Length)eq = L

<!-- b000158 | prose | pages [9] -->
n

<!-- b000159 | prose | pages [9] -->
ηi = L

<!-- b000160 | prose | pages [9] -->
X

<!-- b000161 | prose | pages [9] -->
n ·

<!-- b000162 | prose | pages [9] -->
(4) n

<!-- b000163 | prose | pages [9] -->
i=1

<!-- b000164 | prose | pages [9] -->
(Width)eq = W (5)

<!-- b000165 | prose | pages [9] -->
Then, we substitute the data into the equations above (L = 100m, W = 20m, n = 3(−2F, −1F), 13(−1F, 0F), 28(0F, 1F), 14(1F, 2F)) and get the exact shape of the equiv- alent 2D "building". See Figure 4.

<!-- b000166 | caption | pages [9] -->
Figure 4: The Dimensionality-reduction Building

<!-- b000167 | prose | pages [9] -->
3.3 Spacial Discretization Method

<!-- b000168 | prose | pages [9] -->
We discretize the space of the 2D "building" into dense nodes, and then place the "building" in a rectangular coordinate system to get the coordinate of each node. We save these nodes’ coordinates in the form of matrix for the sake of programming. (The four blue circle in Figure 5 respectively represent one of the four frequently-used exits.)

<!-- b000169 | furniture | pages [10] -->
Team # 1900007

<!-- b000170 | furniture | pages [10] -->
Page 8 of 26

<!-- b000171 | caption | pages [10] -->
Figure 5: Node Distribution of the 2D Model

<!-- b000172 | prose | pages [10] -->
3.4

<!-- b000173 | heading | pages [10] -->
Basic Searching Model

<!-- b000174 | prose | pages [10] -->
We base the Basic Searching Model on Dijkstra Searching Algorithm (DSA), which can ﬁgure out the optimal route from a given origin to an appointed destination. In our model, each evacuee is considered as an origin, and the closest exit for him/her is the corresponding destination. The Dijkstra Searching Algorithm can only ﬁnd the short- est path to a single destination at a time, but the evacuee has 4 potential destinations (4 different exits). So in order to ﬁgure out the optimal exit, we separatedly set the 4 exits as the destination and carry out Dijkstra Searching Algorithm. Certainly, we will ﬁnd four different "short route". The optimal exit for that evacuee is the exit of the shortest route among the four.

<!-- b000175 | prose | pages [10] -->
In a traditional Dijkstra Searching Algorithm, the weight of an edge is deﬁned as the geometric distance between the two nodes.

<!-- b000176 | prose | pages [10] -->
However, we make some adjustions based on real-world conditions. First, evac- uees can only assess the condition within their visual threshold and choose to head towards one place. So in our model, only the weight between adjacent nodes within an evacuee’s visual threshold can be set in the traditonal way: dis(i, j). Plus, it is ap- parent that evacuees should not choose the nodes located in the deadly zone, even if it is close to both of the exit and the current node. Therefore, the weight of all edges within the deadly zone should be set as inﬁnity.

<!-- b000177 | prose | pages [10] -->
To sum up, in our model, weight of the edge between Node #i and Node #j is de- ﬁned by the equation below.

<!-- b000178 | furniture | pages [11] -->
Team # 1900007

<!-- b000179 | furniture | pages [11] -->
Page 9 of 26

<!-- b000180 | prose | pages [11] -->


<!-- b000181 | prose | pages [11] -->
i̸ = j, dis(i, j) ≤Vrange, and Node #j is not in the danger zone dis(i, j)

<!-- b000182 | prose | pages [11] -->
 

<!-- b000183 | prose | pages [11] -->
e(i,j) =

<!-- b000184 | prose | pages [11] -->
0 i = j,

<!-- b000185 | prose | pages [11] -->
(6)

<!-- b000186 | prose | pages [11] -->


<!-- b000187 | prose | pages [11] -->
∞ otherwise.

<!-- b000188 | prose | pages [11] -->


<!-- b000189 | prose | pages [11] -->
where

<!-- b000190 | prose | pages [11] -->
• e(i, j) is the weight of edge between Node #i and Node #j,

<!-- b000191 | prose | pages [11] -->
• dis(i, j) is the geometric distance between Node #i and Node #j,

<!-- b000192 | prose | pages [11] -->
• Rdead is the radius of the deadly zone,

<!-- b000193 | prose | pages [11] -->
• Vrange is an individual’s maximum visual threshold.

<!-- b000194 | prose | pages [11] -->
We draw a ﬂow chart to illustrate our Basic Searching Model. See Figure 6.

<!-- b000195 | caption | pages [11] -->
Figure 6: The Flow Chart Describing the Basic Search Model

<!-- b000196 | prose | pages [11] -->
After implementing the model in MATLAB, we can ﬁgure out the optimal evac- uation route for each individual and its length. Given the speed and proportion of different kinds of people (e.g. the elderly, the disabled), we can calculate the average evacuation time using the equations below.

<!-- b000197 | prose | pages [11] -->
Sdis Speople · P Pk · vk

<!-- b000198 | prose | pages [11] -->
k ∈{elder, young, disabled}

<!-- b000199 | prose | pages [11] -->
tindividual =

<!-- b000200 | prose | pages [11] -->
,

<!-- b000201 | furniture | pages [12] -->
Team # 1900007

<!-- b000202 | furniture | pages [12] -->
Page 10 of 26

<!-- b000203 | prose | pages [12] -->
Sdis

<!-- b000204 | prose | pages [12] -->
k ∈{elder, young, disabled}

<!-- b000205 | prose | pages [12] -->
tk =

<!-- b000206 | prose | pages [12] -->
, (8)

<!-- b000207 | prose | pages [12] -->
Speople · vk

<!-- b000208 | prose | pages [12] -->
We also establish a method to avoid congestion around exits, which may become the potential bottleneck. If we do not control the maximum ratio of people passing through a certain exit, chances are that the majority of evacuees are allocated to the same exit because of the limited number and uneven distribution of the exits, just as the following ﬁgure illustrates. See Figure 7.

<!-- b000209 | prose | pages [12] -->
Part(I) of Figure 7 shows optimal evacuation routes(the lines). Part(II) illustrates the ratio of people passing through each exit. We can clearly see that 90% of the evacuees leave the building from Exit #1, making this exit extremely overloaded. The overused exit will be jammed and may become the potential bottleneck.

<!-- b000210 | caption | pages [12] -->
Figure 7: The Result Without Setting the Ratio of People Passing Through a Certain Exit.

<!-- b000211 | prose | pages [12] -->
To solve the congestion around exits, all exits should be utilized in a balanced way. We can adjust the maximum ratio of people using exit #s (α(s)

<!-- b000212 | prose | pages [12] -->
exit) to disperse the pressure of it. For example, we set α(s)

<!-- b000213 | prose | pages [12] -->
exit as 50% for the four exits, and carry out simulation again. The results are shown in Figure 8. It is clear that the overuse and congestion of Exit #1 are greatly relieved.

<!-- b000214 | caption | pages [12] -->
Figure 8: The Result after Setting α(s)

<!-- b000215 | prose | pages [12] -->
exit as 50%.

<!-- b000216 | furniture | pages [13] -->
Team # 1900007

<!-- b000217 | furniture | pages [13] -->
Page 11 of 26

<!-- b000218 | prose | pages [13] -->
Utilizing the equations discussed above, we plug in a set of reasonable data listed in Table 3, and calculate the average time to leave the Louvre for the elderly, the youth, the disabled, and all the evacuees respectively.

<!-- b000219 | caption | pages [13] -->
Table 3: Some Data we Use in the Basic Searching Model

<!-- b000220 | prose | pages [13] -->
Plug-in Data Item

<!-- b000221 | prose | pages [13] -->
Vrange Rdead Exy 21 m 30 m (580 m, 550 m) Speople Pyouth Pelderly Pdisabled vyouth velderly vdisabled ρpeople 1471 72.1% 21.1% 6.8% 1.28 m/s 1.03 m/s 0.78 m/s 0.4 people per node αs

<!-- b000222 | prose | pages [13] -->
exit 0.5

<!-- b000223 | prose | pages [13] -->
The result of the average evacuation time and distance are listed in Table 4

<!-- b000224 | caption | pages [13] -->
Table 4: Some Data we Use in the Basic Searching Model

<!-- b000225 | prose | pages [13] -->
Item

<!-- b000226 | prose | pages [13] -->
Sdis tindividual telderly tyouth tdisabled

<!-- b000227 | prose | pages [13] -->
3.5

<!-- b000228 | heading | pages [13] -->
Danger Index Model

<!-- b000229 | prose | pages [13] -->
Result

<!-- b000230 | prose | pages [13] -->
6.33 × 105 m 364.85 s 413.98 s 336.35 s 551.95 s

<!-- b000231 | prose | pages [13] -->
In order to have a good command of the real-time change of emergency, we estab- lish the Danger Index Model. In this model, we introduce a new concept–"mesh" as the smallest unit of our study, which is the circular area with a node as its centre.

<!-- b000232 | prose | pages [13] -->
We add the the density of evacuees in each mesh into consideration. Then, We cal- culate the weight of each mesh in terms of the inﬂuence exerted by density of people, distance from danger and distance from exits. After that, we combine the three kind of weight to form Danger Index (DI) of each mesh, and calculate it. Finally, we visualize the result with a heat map.

<!-- b000233 | prose | pages [13] -->
The weight of a mesh can be calculated in terms of the inﬂuence exerted by the density of people, the distance from exits and the distance from the source of danger.

<!-- b000234 | furniture | pages [14] -->
Team # 1900007

<!-- b000235 | furniture | pages [14] -->
Page 12 of 26

<!-- b000236 | prose | pages [14] -->
• Density Weight: High density of people surrounding an evacuee will cause con- gestion and lower the speed, so the density weight of mesh #i can be calculated using the following equation:

<!-- b000237 | prose | pages [14] -->
w(i)

<!-- b000238 | prose | pages [14] -->
N (i)

<!-- b000239 | prose | pages [14] -->
mesh

<!-- b000240 | prose | pages [14] -->
density =

<!-- b000241 | prose | pages [14] -->
where N (i)

<!-- b000242 | prose | pages [14] -->
(9)

<!-- b000243 | prose | pages [14] -->
π × R2

<!-- b000244 | prose | pages [14] -->
mesh

<!-- b000245 | prose | pages [14] -->
mesh is the number of people in mesh #i, and Rmesh is the radius of mesh #i.

<!-- b000246 | prose | pages [14] -->
• Emergency Weight: It is widely accepted that the degree of danger is inversely proportional to the distance from it. Thus, the emergency weight of mesh #i can be deﬁned by the following equation:

<!-- b000247 | prose | pages [14] -->
w(i)

<!-- b000248 | prose | pages [14] -->
1 emergency = (10) dis(i, Exy)

<!-- b000249 | prose | pages [14] -->
where Exy is the source of danger, and dis(i, Exy) stands for the distance between mesh #i and the source of danger.

<!-- b000250 | prose | pages [14] -->
• Exit Weight: The weight of exit is deﬁned as

<!-- b000251 | prose | pages [14] -->
w(i)

<!-- b000252 | prose | pages [14] -->
exit = min{dis(i, Exit(s))} (11)

<!-- b000253 | prose | pages [14] -->
where dis(i, Exit(s)) refers to the distance from mesh #i to exit #s, because the more distant from the exit, the more time-consuming the evacuation process will be.

<!-- b000254 | prose | pages [14] -->
The overall degree of danger depends on all of the three factors. Thus, we deﬁne the Danger Index (DI) by calculating the weighed sum of these three kinds of weight, as

<!-- b000255 | prose | pages [14] -->
DI(i) = a · w(i)

<!-- b000256 | prose | pages [14] -->
density + b · w(i)

<!-- b000257 | prose | pages [14] -->
danger + c · w(i)

<!-- b000258 | prose | pages [14] -->
(12) exit

<!-- b000259 | prose | pages [14] -->
where a,b and c are the ratios of the three weight components. In different cases, the signiﬁcance of each component varies, so we should adjust these ratios to ﬁt different conditions.

<!-- b000260 | prose | pages [14] -->
For example, we use two different sets of ratios, and visualize the real-time distri- bution Danger Index of every place using the 3D heat map. At the beginning of an emergency, the source of danger is very inﬂuential, so we set a high ratio for Emer- gency Weight, and the result is shown in Part(I) of Figure 9. However, after some time, the source of danger alleviates, so we can lower the ratio of emergency, and ﬁgure out the up-to-date distribution of Danger Index like Part(II) of Figure 9.

<!-- b000261 | prose | pages [14] -->
The emergency manager can adjust the ratio of the current key inﬂuence, and have an understanding of the real-time Danger Index in the building.

<!-- b000262 | furniture | pages [15] -->
Team # 1900007

<!-- b000263 | furniture | pages [15] -->
Page 13 of 26

<!-- b000264 | caption | pages [15] -->
Figure 9: Distribution of Danger Index with Different Sets of Ratios

<!-- b000265 | prose | pages [15] -->
How to Utilize Additional Exits? 3.6

<!-- b000266 | prose | pages [15] -->
Utilizing the Danger Index Model, we can easily take advantage of the additional exits. Here is our plan.

<!-- b000267 | prose | pages [15] -->
First, all of the four main exits should be used for evacuation purpose, since they are more familiar to the evacuees and can be monitored by the app "Afﬂuences".

<!-- b000268 | prose | pages [15] -->
Plus, based on the real-time Danger Index (DI) distribution, we can calculate the proportion of the additional exits that should be open for evacuation purpose. We set a danger threshold. When the emergency happens, we count the number of evacuees located in meshes whose DI is above the security threshold, and deﬁne the number as Pdanger. Suppose we have n additional exits, and i of them are open for evacuation purpose, we can adjust i according to Pdanger. The speciﬁc relationship between them can be described by Equation (13).

<!-- b000269 | prose | pages [15] -->


<!-- b000270 | prose | pages [15] -->
n

<!-- b000271 | prose | pages [15] -->
  

<!-- b000272 | prose | pages [15] -->
n −1

<!-- b000273 | prose | pages [15] -->
   

<!-- b000274 | prose | pages [15] -->
n −2

<!-- b000275 | prose | pages [15] -->
i =

<!-- b000276 | prose | pages [15] -->
...

<!-- b000277 | prose | pages [15] -->
     

<!-- b000278 | prose | pages [15] -->
0

<!-- b000279 | prose | pages [15] -->


<!-- b000280 | prose | pages [15] -->
Pdanger > a, b < Pdanger ≤a, c < Pdanger ≤b,

<!-- b000281 | prose | pages [15] -->
(13)

<!-- b000282 | prose | pages [15] -->
... ... Pdanger ≈0.

<!-- b000283 | prose | pages [15] -->
a, b, c. . . in the equation can be determined by Fuzzy Sets or Monte Carlo method. However, due to the lack of speciﬁc data, we will not detail it here.

<!-- b000284 | prose | pages [15] -->
How to Let Emergency Personnel Enter? 3.7

<!-- b000285 | prose | pages [15] -->
To assist the emergency personnel, we can utilize our Basic Searching Model and Danger Index Model to determine the best doors to enter and optimal routes in the building.

<!-- b000286 | prose | pages [15] -->
First, emergency personnel should enter from the underused main exits and the

<!-- b000287 | furniture | pages [16] -->
Team # 1900007

<!-- b000288 | furniture | pages [16] -->
Page 14 of 26

<!-- b000289 | prose | pages [16] -->
additional exits that are not open for evacuation. As for the former, the ratio of evac- uees passing through a certain main exit can be adjusted by our Basic Searching Model. Therefore, we can decrease the ratio of an exit to make way for the emergency person- nel. As for the latter, the additional exits that are not open for evacuation can all be used to enter the building.

<!-- b000290 | prose | pages [16] -->
Second,upon entering the building, emergency personnel should travel from places with low Danger Index to the ones with high Danger Index, which is just the contrary to evacuees. (The real-time distribution of Danger Index can be calculated by our Dan- ger Index Model.) In this way, they can quickly cope with the source of danger or dredge the crowd with high density.

<!-- b000291 | prose | pages [16] -->
3.8

<!-- b000292 | heading | pages [16] -->
Model Evaluation and Sensitivity Analysis

<!-- b000293 | prose | pages [16] -->
To test the sensitivity, we operate the model under several different conditions. We change the density of people (ρpeople), the radius of the deadly zone (Rdead), the maximum ratio of usage of exit #i (α(i)

<!-- b000294 | prose | pages [16] -->
exit), and calculate the corresponding average time of evacuation for each kind of people. Then, we visualize our results with the ﬁgures below.

<!-- b000295 | caption | pages [16] -->
Figure 10: The Framewok of the 3D Cellular Automata Model(3D-CAM)

<!-- b000296 | prose | pages [16] -->
The ﬁrst and second part of Figure 10 tell us that the evacuation time for each kind of people is almost same despite the difference of the density of people (ρpeople) and the varied radius of the deadly zone (Rdead). This means our model is not sensitive to these varibles. Thus, we can apply the 2D-IBM Model to analyze emergency events of different severity and different number of inﬂuenced people. Therefore, though the number of guests in the museum varies throughout the day and year, the results are stable.

<!-- b000297 | prose | pages [16] -->
The third part of Figure 10 shows that the time of evacuation is not that stable when α(i)

<!-- b000298 | prose | pages [16] -->
exit is smaller than 0.5. But if α(i)

<!-- b000299 | prose | pages [16] -->
exit varies between 0.5 to 0.7, the evacuation time is nearly constant. We can conclude that our model is robust when the capacity of the

<!-- b000300 | furniture | pages [17] -->
Team # 1900007

<!-- b000301 | furniture | pages [17] -->
Page 15 of 26

<!-- b000302 | prose | pages [17] -->
exits is enough. However, if the capacity of each door becomes too small, evacuees have to wind their way to avoid potential congestion. Thus our model becomes a little unstable under such condition.

<!-- b000303 | prose | pages [17] -->
The fourth part of Figure 10 reﬂects that the sum of people passing through exit #1 or #2 of the Louvre increases greatly as the density of people rises, while that of exit #3 or #4 is hardly affected. This diagram shows that the usage of exit #1 and #2 is near the saturation state, as apposed to exit #3 and exit #4, which are usually underused.

<!-- b000304 | prose | pages [17] -->
4

<!-- b000305 | heading | pages [17] -->
The 3D Cellular Automata Model (3D-CAM)

<!-- b000306 | prose | pages [17] -->
4.1

<!-- b000307 | heading | pages [17] -->
The Mechanism of the Model

<!-- b000308 | prose | pages [17] -->
The 2D-IBM Model is concise, but somehow too abstract. In order to simulate the evacuation process in an intuitive way, we build the 3D Cellular Automata Model (3D- CAM). In this model, we construct a 3D copy of the Louvre using AutoCAD, and then implement it into Pathﬁnder, a professional and mature software which simulates the evacuation process based on Celluar Automata Method. The 3D simulation clearly demonstrates the bottlenecks of evacuation on each ﬂoor and gives the heat map of the evacuation time in different places of each ﬂoor.

<!-- b000309 | caption | pages [17] -->
Figure 11: The Framewok of the 3D Cellular Automata Model(3D-CAM)

<!-- b000310 | furniture | pages [18] -->
Team # 1900007

<!-- b000311 | furniture | pages [18] -->
Page 16 of 26

<!-- b000312 | prose | pages [18] -->
The framework of the 3D-CAM Model is illustrated in Figure 11. As shown in this ﬁgure, the ﬂoor plan of the Louvre, location of staircases and exits and human behavior patterns are integrated to guide the evacuation. The 3D indoor space is divided into triangular cellular space[9], like Figure 12.

<!-- b000313 | caption | pages [18] -->
Figure 12: Triangular Cellular Space[9]

<!-- b000314 | prose | pages [18] -->
The search of evacuation routes for each individual is divided into two different modes, the SFPE Mode and the Steering Mode. Attributes of the two modes are shown in the ﬁgure. The mechanism of the former resembles our Basic Searching Model and the latter is like our Danger Index Model. After implementing the data and selecting a simulation mode, the Pathﬁnder software can provide visualized real-time condition of the evacuation process.

<!-- b000315 | prose | pages [18] -->
4.2

<!-- b000316 | heading | pages [18] -->
Visualized Result of the Model

<!-- b000317 | caption | pages [18] -->
Figure 13: The Heat Map of Evacuation Time in Different Places of Each Floor

<!-- b000318 | prose | pages [18] -->
After running the simulation, we can get the heat map of evacuation time in dif- ferent places of each ﬂoor. See Figure 13. The "hotter" a spot is, the longer it will take an individual to evacuate from that spot. Different colors in the heat map is of simi- lar meaning to the different "Danger Index" in our 2D-IBM Model. Comparing Figure

<!-- b000319 | heading | pages [18] -->
13 with Figure 9, we notice that the distribute of color is of the same trend, which

<!-- b000320 | prose | pages [18] -->
indirectly proves that our Danger Index Model is reasonable.

<!-- b000321 | furniture | pages [19] -->
Team # 1900007

<!-- b000322 | furniture | pages [19] -->
Page 17 of 26

<!-- b000323 | prose | pages [19] -->
4.3 Determining the Potential Bottleneck

<!-- b000324 | prose | pages [19] -->
The Pathﬁnder simulation dynamically shows the real-time density of evacuees in a certain place, and forms the heat map of density on each ﬂoor. With the aid of it, we can easily ﬁgure out the bottlenecks on each ﬂoor, which are clearly shown in Figure 14, 15.

<!-- b000325 | prose | pages [19] -->
These bottlenecks are located either near staircases or close to exits, which makes sense. However, due to the difference of locations, not all the stairs or exits can be the potential bottleneck. For example, only a few evacuees choose to leave from distant exits.

<!-- b000326 | caption | pages [19] -->
Figure 14: The Potential Bottlenecks on each Floor

<!-- b000327 | caption | pages [19] -->
Figure 15: The Potential Bottlenecks–Focus

<!-- b000328 | furniture | pages [20] -->
Team # 1900007

<!-- b000329 | furniture | pages [20] -->
Page 18 of 26

<!-- b000330 | prose | pages [20] -->
5

<!-- b000331 | heading | pages [20] -->
Strengths and Weaknesses

<!-- b000332 | prose | pages [20] -->
5.1

<!-- b000333 | heading | pages [20] -->
Strengths

<!-- b000334 | heading | pages [20] -->
1. Our Dimensionality Reduction Method successfully planarizes the building, thus

<!-- b000335 | prose | pages [20] -->
simplifying the calculation greatly.

<!-- b000336 | heading | pages [20] -->
2. Our Basic Searching Model and Danger Index Model take the attributes of the

<!-- b000337 | prose | pages [20] -->
building into consideration (e.g. the capacity of exits, the distribution of stair- cases, etc.), so it can be adapted to other large and crowded structures easily.

<!-- b000338 | heading | pages [20] -->
3. Our Basic Searching Model and Danger Index Model consider many hominine

<!-- b000339 | prose | pages [20] -->
factors (e.g. the diversity of evacuees, the density of evacuees, etc.), so our routes can guarantee the evacuees’ security to a large extent.

<!-- b000340 | heading | pages [20] -->
4. Our model is not sensitive to the density of people and the severity of the emer-

<!-- b000341 | prose | pages [20] -->
gency, which gurantees its robustness.

<!-- b000342 | heading | pages [20] -->
5. Our 3D Cellular Automata Model successfully constructs a well-designed 3D

<!-- b000343 | prose | pages [20] -->
model of Louvre, allowing the simulation to resemble the real-world situation.

<!-- b000344 | prose | pages [20] -->
5.2

<!-- b000345 | heading | pages [20] -->
Weaknesses

<!-- b000346 | heading | pages [20] -->
1. The Dijkstra Searching Method needs to call the searching function repeatedly,

<!-- b000347 | prose | pages [20] -->
leading to a comparatively high Time Complexity of the algorithm.

<!-- b000348 | heading | pages [20] -->
2. Our 2D Island-Bridge Model discretizes the spaces into nodes. The discretization

<!-- b000349 | prose | pages [20] -->
method replace the continuous movement of people with the leap between two adjacent nodes. This method deserves further justiﬁcation.

<!-- b000350 | prose | pages [20] -->
6

<!-- b000351 | heading | pages [20] -->
Conclusion: A Letter of Advice to the Emergency Man-

<!-- b000352 | prose | pages [20] -->
ager

<!-- b000353 | prose | pages [20] -->
Dear Sir/Madam,

<!-- b000354 | prose | pages [20] -->
We are a group of students participating in the 2019 ICM contest who chose the "Time to Leave the Louvre" problem. We would like to give some advice based on our work to better your evacuation plan.

<!-- b000355 | prose | pages [20] -->
First of all, we think it’s crucial to add more dectectors and sensors in the mu- seum to monitor the density of evacuees and collect some other information. Plus, you should also suggest the visitors to utilize the positioning function of their smartphones to help you calculate their distance to each exit and the danger source. With these data in hand, you can have a good command of the real-time distribution of Danger Index in the building by our Danger Index Model. Then, you can work out the optimal evac- uation route for people in different places of the museum. It’s necessary to implement

<!-- b000356 | furniture | pages [21] -->
Team # 1900007

<!-- b000357 | furniture | pages [21] -->
Page 19 of 26

<!-- b000358 | prose | pages [21] -->
an evacuation navigation function in the "Afﬂuences" APP, so that everyone can get to know their own optimal route.

<!-- b000359 | prose | pages [21] -->
Secondly, we strongly advice you to guarantee that the exits and stairs are not oc- cupied or stuck. Stairs and Exits play key roles in the evacuation process, and they are very likely to cause congestion or stagnation and become bottlenecks of evacuation.

<!-- b000360 | prose | pages [21] -->
Finally, we will be very glad if you can take time to read our paper and we hope our advice will be of help to you. If you have any questions, please feel free to ask us.

<!-- b000361 | prose | pages [21] -->
Sincerely,

<!-- b000362 | prose | pages [21] -->
Members of Team #1900007

<!-- b000363 | heading | pages [21] -->
References

<!-- b000364 | references | pages [21] -->
[1] Xiong, Q.; Zhu, Q.; Du, Z.; Zhu, X.; Zhang, Y.; Niu, L.; Li, Y.; Zhou, Y. A Dy-

<!-- b000365 | references | pages [21] -->
namic Indoor Field Model for Emergency Evacuation Simulation. ISPRS Interna-

<!-- b000366 | references | pages [21] -->
tional Journal of Geo-Information, 2017, 6, 104.

<!-- b000367 | references | pages [21] -->
[2] Lo, S.M.; Fang, Z.; Chen, D.H. Use of a modiﬁed network model for analyzing

<!-- b000368 | references | pages [21] -->
evacuation patterns in high-rise buildings. J. Archit. Eng, 2001, 7, 21–29.

<!-- b000369 | references | pages [21] -->
[3] Helbing, D.; Farkas, I.; Vicsek, T. Simulating dynamical features of escape panic.

<!-- b000370 | references | pages [21] -->
Nature, 2000, 407, 487–490.

<!-- b000371 | references | pages [21] -->
[4] Kirchner, A.; Schadschneider, A. Simulation of evacuation processes using a

<!-- b000372 | references | pages [21] -->
bionics-inspired cellular automaton model for pedestrian dynamics. Phys. A Stat.

<!-- b000373 | references | pages [21] -->
Mech. Appl., 2002, 312, 260–276.

<!-- b000374 | references | pages [21] -->
[5] FENG Weiwei; QIU Jiong. Application of Ant Colony Algorithm in Fire Evacua-

<!-- b000375 | references | pages [21] -->
tion Platform(in Chinese). Electronic Science and Technology., 2015, 4, 13-16.

<!-- b000376 | references | pages [21] -->
[6] Louvre 2014 Annual Report.pdf.

<!-- b000377 | references | pages [21] -->
https://www.louvre.fr/sites/default/files/rapport_activite/

<!-- b000378 | references | pages [21] -->
fichiers/PDF/louvre-2014-annual-report.pdf

<!-- b000379 | references | pages [21] -->
[7] Louvre Plan Visitors Mobility Impairments.pdf.

<!-- b000380 | references | pages [21] -->
https://www.louvre.fr/sites/default/files/medias/

<!-- b000381 | references | pages [21] -->
medias_fichiers/fichiers/pdf/louvre-plan-visitors-

<!-- b000382 | references | pages [21] -->
mobility-impairments.pdf

<!-- b000383 | references | pages [21] -->
[8] Louvre Interactive Floor Plans.

<!-- b000384 | references | pages [21] -->
https://www.louvre.fr/en/plan

<!-- b000385 | references | pages [21] -->
[9] Pathﬁnder 2012 Technical Reference.pdf.

<!-- b000386 | furniture | pages [22] -->
Team # 1900007

<!-- b000387 | furniture | pages [22] -->
Page 20 of 26

<!-- b000388 | heading | pages [22] -->
Appendices

<!-- b000389 | prose | pages [22] -->
A Our Simulation Codes Written in MATLAB

<!-- b000390 | prose | pages [22] -->
DijkstraMain.m

<!-- b000391 | prose | pages [22] -->
1 clear a l l

<!-- b000392 | prose | pages [22] -->
2 c l c

<!-- b000393 | prose | pages [22] -->
3 load ( ’node . mat ’ ) ;

<!-- b000394 | prose | pages [22] -->
4 C=X;

<!-- b000395 | prose | pages [22] -->
5 n=size (C, 1 ) ;

<!-- b000396 | prose | pages [22] -->
6 D=zeros (n , n) ;

<!-- b000397 | prose | pages [22] -->
7

<!-- b000398 | prose | pages [22] -->
8 viewpoint =21;

<!-- b000399 | prose | pages [22] -->
9 emerg =[580 ,550];

<!-- b000400 | prose | pages [22] -->
10 s c a t t e r ( emerg ( 1 , 1 ) , emerg ( 1 , 2 ) ,100 , ’ r ’ , ’ f i l l e d ’ ) ;

<!-- b000401 | prose | pages [22] -->
11 hold on

<!-- b000402 | prose | pages [22] -->
12 thread =30;

<!-- b000403 | prose | pages [22] -->
13 totalpeople =0;

<!-- b000404 | prose | pages [22] -->
14 t o t a l d i s t a n c e =0;

<!-- b000405 | prose | pages [22] -->
15 e = [ 0 , 0 , 0 , 0 ] ;

<!-- b000406 | prose | pages [22] -->
16 alphaexit =0.35;

<!-- b000407 | prose | pages [22] -->
17 dens =0.4;

<!-- b000408 | prose | pages [22] -->
18 Contain=alphaexit ∗3700∗dens ;

<!-- b000409 | prose | pages [22] -->
19 for i =1:n

<!-- b000410 | prose | pages [22] -->
20 for j =1:n

<!-- b000411 | prose | pages [22] -->
21 i f i ~= j

<!-- b000412 | prose | pages [22] -->
22 D( i , j )=sqrt ( (C( i , 1 )−C( j , 1 ) ) ^2+(C( i , 2 )−C( j , 2 ) ) ^2) ;

<!-- b000413 | prose | pages [22] -->
23 else

<!-- b000414 | prose | pages [22] -->
24 D( i , j ) =0;

<!-- b000415 | prose | pages [22] -->
25 end

<!-- b000416 | prose | pages [22] -->
26 D( j , i )=D( i , j ) ;

<!-- b000417 | prose | pages [22] -->
27 end

<!-- b000418 | prose | pages [22] -->
28 end

<!-- b000419 | prose | pages [22] -->
29

<!-- b000420 | prose | pages [22] -->
30 for i =1:n

<!-- b000421 | prose | pages [22] -->
31 for j =1:n

<!-- b000422 | prose | pages [22] -->
32 i f D( i , j )>viewpoint||sqrt ( (C( i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i , 2 )−emerg ( 1 , 2 ) ) ^2)<= thread

<!-- b000423 | prose | pages [22] -->
33 D( i , j )=inf ;

<!-- b000424 | prose | pages [22] -->
34 end

<!-- b000425 | prose | pages [22] -->
35 end

<!-- b000426 | prose | pages [22] -->
36 end

<!-- b000427 | prose | pages [22] -->
37

<!-- b000428 | prose | pages [22] -->
38

<!-- b000429 | prose | pages [22] -->
39 for i i =1:3700

<!-- b000430 | prose | pages [22] -->
rand<=dens&&(sqrt ( (C( i i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i i , 2 )−emerg ( 1 , 2 ) ) ^2)>thread ) 40 i f

<!-- b000431 | prose | pages [22] -->
41 s t a r t = i i ;

<!-- b000432 | prose | pages [22] -->
42 totalpeople=totalpeople +1;

<!-- b000433 | prose | pages [22] -->
43 e x i t =X( 3 7 0 1 : 3 7 0 4 , : ) ;

<!-- b000434 | prose | pages [22] -->
44

<!-- b000435 | prose | pages [22] -->
45 i f e ( 1 , 1 )<=Contain

<!-- b000436 | prose | pages [22] -->
46 [ mydistance1 , mypath1]= Djsk (D, start ,3701) ;

<!-- b000437 | prose | pages [22] -->
47 else

<!-- b000438 | prose | pages [22] -->
48 mydistance1=inf ;

<!-- b000439 | furniture | pages [23] -->
Team # 1900007

<!-- b000440 | furniture | pages [23] -->
Page 21 of 26

<!-- b000441 | prose | pages [23] -->
49 end

<!-- b000442 | prose | pages [23] -->
50

<!-- b000443 | prose | pages [23] -->
51 i f e ( 1 , 2 )<=Contain

<!-- b000444 | prose | pages [23] -->
52 [ mydistance2 , mypath2]= Djsk (D, start ,3702) ;

<!-- b000445 | prose | pages [23] -->
53 else

<!-- b000446 | prose | pages [23] -->
54 mydistance2=inf ;

<!-- b000447 | prose | pages [23] -->
55 end

<!-- b000448 | prose | pages [23] -->
56

<!-- b000449 | prose | pages [23] -->
57 i f e ( 1 , 3 )<=Contain

<!-- b000450 | prose | pages [23] -->
58 [ mydistance3 , mypath3]= Djsk (D, start ,3703) ;

<!-- b000451 | prose | pages [23] -->
59 else

<!-- b000452 | prose | pages [23] -->
60 mydistance3=inf ;

<!-- b000453 | prose | pages [23] -->
61 end

<!-- b000454 | prose | pages [23] -->
62

<!-- b000455 | prose | pages [23] -->
63 i f e ( 1 , 4 )<=Contain

<!-- b000456 | prose | pages [23] -->
64 [ mydistance4 , mypath4]= Djsk (D, start ,3704) ;

<!-- b000457 | prose | pages [23] -->
65 else

<!-- b000458 | prose | pages [23] -->
66 mydistance4=inf ;

<!-- b000459 | prose | pages [23] -->
67 end

<!-- b000460 | prose | pages [23] -->
68 Pd=[ mydistance1 , mydistance2 , mydistance3 , mydistance4 ] ;

<!-- b000461 | prose | pages [23] -->
69 [ value , index ]=min(Pd) ;

<!-- b000462 | prose | pages [23] -->
70 [ mydistance , mypath]= Djsk (D, start ,3700+ index ) ;

<!-- b000463 | prose | pages [23] -->
71 e (1 , index )=e (1 , index ) +1;

<!-- b000464 | prose | pages [23] -->
72 t o t a l d i s t a n c e = t o t a l d i s t a n c e +value ;

<!-- b000465 | prose | pages [23] -->
73 Xp = [ ] ; Yp = [ ] ;

<!-- b000466 | prose | pages [23] -->
74 for i =1: size ( mypath , 2 )

<!-- b000467 | prose | pages [23] -->
75 Xp=[Xp,C( mypath ( i ) ,1) ] ;

<!-- b000468 | prose | pages [23] -->
76 Yp=[Yp,C( mypath ( i ) ,2) ] ;

<!-- b000469 | prose | pages [23] -->
77 end

<!-- b000470 | prose | pages [23] -->
78 s c a t t e r (C( : , 1 ) ,C( : , 2 ) , ’b . ’ ) ;

<!-- b000471 | prose | pages [23] -->
79 hold on

<!-- b000472 | prose | pages [23] -->
80 s c a t t e r ( e x i t ( : , 1 ) , e x i t ( : , 2 ) ,100 , ’p ’ , ’ f i l l e d ’ ) ;

<!-- b000473 | prose | pages [23] -->
81 hold on

<!-- b000474 | prose | pages [23] -->
82 plot (Xp, Yp) ;

<!-- b000475 | prose | pages [23] -->
83 hold on

<!-- b000476 | prose | pages [23] -->
84 end

<!-- b000477 | prose | pages [23] -->
85 xlabel ( ’x/m’ ) ;

<!-- b000478 | prose | pages [23] -->
86 ylabel ( ’y/m’ ) ;

<!-- b000479 | prose | pages [23] -->
87 end

<!-- b000480 | prose | pages [23] -->
Djsk.m

<!-- b000481 | prose | pages [23] -->
function [ res , index ] = Djsk (mp, stat , ends ) 1

<!-- b000482 | prose | pages [23] -->
n=size (mp, 1 ) ; 2

<!-- b000483 | prose | pages [23] -->
bj=zeros (n , 1 ) ; 3

<!-- b000484 | prose | pages [23] -->
dis=mp( stat , : ) ; 4

<!-- b000485 | prose | pages [23] -->
path=ones (n , 1 ) ; path=path . ∗s t a t ; 5

<!-- b000486 | prose | pages [23] -->
dis ( s t a t ) =0; bj ( s t a t ) =1; 6

<!-- b000487 | prose | pages [23] -->
for i =1:n 7

<!-- b000488 | prose | pages [23] -->
min=Inf ; k=1; 8

<!-- b000489 | prose | pages [23] -->
for j =1:n 9

<!-- b000490 | prose | pages [23] -->
i f ( bj ( j ) ~=1)&&(dis ( j )<min) ,min=dis ( j ) ; k= j ; end 10

<!-- b000491 | prose | pages [23] -->
end 11

<!-- b000492 | prose | pages [23] -->
bj ( k ) =1; 12

<!-- b000493 | prose | pages [23] -->
for j =1:n 13

<!-- b000494 | prose | pages [23] -->
i f ( bj ( j ) ~=1)&&(dis ( j ) >( dis ( k )+mp(k , j ) ) ) , dis ( j )=dis ( k )+mp(k , j ) ; path ( j )=k ; 14 end

<!-- b000495 | prose | pages [23] -->
end 15

<!-- b000496 | prose | pages [23] -->
end 16

<!-- b000497 | furniture | pages [24] -->
Team # 1900007

<!-- b000498 | furniture | pages [24] -->
Page 22 of 26

<!-- b000499 | prose | pages [24] -->
tem=ends ; index ( 1 ) =ends ; i =2; 17

<!-- b000500 | prose | pages [24] -->
while path ( tem )~= s t a t 18

<!-- b000501 | prose | pages [24] -->
index ( i )=path ( tem ) ; 19

<!-- b000502 | prose | pages [24] -->
tem=path ( tem ) ; 20

<!-- b000503 | prose | pages [24] -->
i = i +1; 21

<!-- b000504 | prose | pages [24] -->
end 22

<!-- b000505 | prose | pages [24] -->
index ( i )= s t a t ; index=index ( length ( index ) : −1:1) ; res=dis ( ends ) ; 23

<!-- b000506 | prose | pages [24] -->
end 24

<!-- b000507 | prose | pages [24] -->
DangerIndex.m

<!-- b000508 | prose | pages [24] -->
1 clear a l l

<!-- b000509 | prose | pages [24] -->
2 c l c

<!-- b000510 | prose | pages [24] -->
3 load ( ’node . mat ’ ) ;

<!-- b000511 | prose | pages [24] -->
4 emerg =[580 ,550];

<!-- b000512 | prose | pages [24] -->
5 X=[X; emerg ] ;

<!-- b000513 | prose | pages [24] -->
6 C=X;

<!-- b000514 | prose | pages [24] -->
7 n=size (C, 1 ) ;

<!-- b000515 | prose | pages [24] -->
8 totaldens =0.4;

<!-- b000516 | prose | pages [24] -->
9 viewpoint =21;

<!-- b000517 | prose | pages [24] -->
10 C=[C, zeros (n , 1 ) ] ;

<!-- b000518 | prose | pages [24] -->
11 hold on

<!-- b000519 | prose | pages [24] -->
12 thread =0;

<!-- b000520 | prose | pages [24] -->
13 e = [ 0 , 0 , 0 , 0 ] ;

<!-- b000521 | prose | pages [24] -->
14 Rfield =21;

<!-- b000522 | prose | pages [24] -->
15 Nfield=zeros (n , 1 ) ;

<!-- b000523 | prose | pages [24] -->
16

<!-- b000524 | prose | pages [24] -->
17 rho=zeros (3700 ,1) ;

<!-- b000525 | prose | pages [24] -->
18 Wemerg=zeros (3700 ,1) ;

<!-- b000526 | prose | pages [24] -->
19 Wexit=zeros (3700 ,1) ;

<!-- b000527 | prose | pages [24] -->
20 Neg=zeros (3700 ,1) ;

<!-- b000528 | prose | pages [24] -->
21

<!-- b000529 | prose | pages [24] -->
22

<!-- b000530 | prose | pages [24] -->
23 for i =1:n

<!-- b000531 | prose | pages [24] -->
24 for j =1:n

<!-- b000532 | prose | pages [24] -->
25 i f i ~= j

<!-- b000533 | prose | pages [24] -->
26 D( i , j )=sqrt ( (C( i , 1 )−C( j , 1 ) ) ^2+(C( i , 2 )−C( j , 2 ) ) ^2) ;

<!-- b000534 | prose | pages [24] -->
27 else

<!-- b000535 | prose | pages [24] -->
28 D( i , j ) =0;

<!-- b000536 | prose | pages [24] -->
29 end

<!-- b000537 | prose | pages [24] -->
30 D( j , i )=D( i , j ) ;

<!-- b000538 | prose | pages [24] -->
31 end

<!-- b000539 | prose | pages [24] -->
32 end

<!-- b000540 | prose | pages [24] -->
33

<!-- b000541 | prose | pages [24] -->
34 for i =1:n

<!-- b000542 | prose | pages [24] -->
35 for j =1:n

<!-- b000543 | prose | pages [24] -->
36 i f D( i , j )>viewpoint||sqrt ( (C( i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i , 2 )−emerg ( 1 , 2 ) ) ^2)<= thread

<!-- b000544 | prose | pages [24] -->
37 D( i , j )=inf ;

<!-- b000545 | prose | pages [24] -->
38 end

<!-- b000546 | prose | pages [24] -->
39 end

<!-- b000547 | prose | pages [24] -->
40 end

<!-- b000548 | prose | pages [24] -->
41

<!-- b000549 | prose | pages [24] -->
42 for i =1:3700

<!-- b000550 | prose | pages [24] -->
rand<=totaldens&&(sqrt ( (C( i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i , 2 )−emerg ( 1 , 2 ) ) ^2)> 43 i f

<!-- b000551 | prose | pages [24] -->
thread )

<!-- b000552 | prose | pages [24] -->
44 C( i , 3 ) =1;

<!-- b000553 | prose | pages [24] -->
45 end

<!-- b000554 | prose | pages [24] -->
46 end

<!-- b000555 | furniture | pages [25] -->
Team # 1900007

<!-- b000556 | furniture | pages [25] -->
Page 23 of 26

<!-- b000557 | prose | pages [25] -->
47

<!-- b000558 | prose | pages [25] -->
48 for i =1:3700

<!-- b000559 | prose | pages [25] -->
j =max(1 , i −64) : min( i +64 ,3700) 49 for

<!-- b000560 | prose | pages [25] -->
( sqrt ( (C( i , 1 )−C( j , 1 ) ) ^2+(C( i , 2 )−C( j , 2 ) ) ^2) <=21)&&(C( j , 3 ) ==1) 50 i f

<!-- b000561 | prose | pages [25] -->
51 Nfield ( i , 1 ) =Nfield ( i , 1 ) +1;

<!-- b000562 | prose | pages [25] -->
52 end

<!-- b000563 | prose | pages [25] -->
53 end

<!-- b000564 | prose | pages [25] -->
54 end

<!-- b000565 | prose | pages [25] -->
55 for i =1:3700

<!-- b000566 | prose | pages [25] -->
56 s t a r t = i ;

<!-- b000567 | prose | pages [25] -->
57 e x i t =X( 3 7 0 1 : 3 7 0 4 , : ) ;

<!-- b000568 | prose | pages [25] -->
58 [ mydistance1 , mypath1]= Djsk (D, start ,3701) ;

<!-- b000569 | prose | pages [25] -->
59 [ mydistance2 , mypath2]= Djsk (D, start ,3702) ;

<!-- b000570 | prose | pages [25] -->
60 [ mydistance3 , mypath3]= Djsk (D, start ,3703) ;

<!-- b000571 | prose | pages [25] -->
61 [ mydistance4 , mypath4]= Djsk (D, start ,3704) ;

<!-- b000572 | prose | pages [25] -->
62 Pd=[ mydistance1 , mydistance2 , mydistance3 , mydistance4 ] ;

<!-- b000573 | prose | pages [25] -->
63 [ value , index ]=min(Pd) ;

<!-- b000574 | prose | pages [25] -->
64 Wexit ( i , 1 ) =value ;

<!-- b000575 | prose | pages [25] -->
65 disemerg=sqrt ( (C( i , 1 )−emerg ( 1 , 1 ) ) ^2+(C( i , 2 )−emerg ( 1 , 2 ) ) ^2) ;

<!-- b000576 | prose | pages [25] -->
66 Wemerg( i , 1 ) =1/disemerg ;

<!-- b000577 | prose | pages [25] -->
67

<!-- b000578 | prose | pages [25] -->
68

<!-- b000579 | prose | pages [25] -->
69 end

<!-- b000580 | prose | pages [25] -->
70

<!-- b000581 | prose | pages [25] -->
71 for i =1:3700

<!-- b000582 | prose | pages [25] -->
72 rho ( i , 1 ) =Nfield ( i , 1 ) /( pi ∗Rfield ^2) ;

<!-- b000583 | prose | pages [25] -->
73 end

<!-- b000584 | prose | pages [25] -->
74

<!-- b000585 | prose | pages [25] -->
75 a=10^2;

<!-- b000586 | prose | pages [25] -->
76 b=10^4;

<!-- b000587 | prose | pages [25] -->
77 c =1;

<!-- b000588 | prose | pages [25] -->
78

<!-- b000589 | prose | pages [25] -->
79 for i =1:3700

<!-- b000590 | prose | pages [25] -->
80 Neg( i , 1 ) =a∗rho ( i , 1 ) +b∗Wemerg( i , 1 ) +c∗Wexit ( i , 1 ) ;

<!-- b000591 | prose | pages [25] -->
81 end

<!-- b000592 | prose | pages [25] -->
82

<!-- b000593 | prose | pages [25] -->
83 f1 =1:600;

<!-- b000594 | prose | pages [25] -->
84 f2 =1:1000;

<!-- b000595 | prose | pages [25] -->
85 [ F1 , F2]= meshgrid ( f1 , f2 ) ;

<!-- b000596 | prose | pages [25] -->
86 F3=zeros (600 ,1000) ;

<!-- b000597 | prose | pages [25] -->
87 F1=F1 ’ ; F2=F2 ’ ;

<!-- b000598 | prose | pages [25] -->
88 for i =1:600

<!-- b000599 | prose | pages [25] -->
89 for j =1:1000

<!-- b000600 | prose | pages [25] -->
90 for i i =1:3700

<!-- b000601 | prose | pages [25] -->
91 i f i ==X( i i , 1 )&&j ==X( i i , 2 )

<!-- b000602 | prose | pages [25] -->
92 F3 ( i , j )=Neg( i i , 1 ) ;

<!-- b000603 | prose | pages [25] -->
93 end

<!-- b000604 | prose | pages [25] -->
94 end

<!-- b000605 | prose | pages [25] -->
95 end

<!-- b000606 | prose | pages [25] -->
96 end

<!-- b000607 | prose | pages [25] -->
97

<!-- b000608 | prose | pages [25] -->
98 mesh( F1 , F2 , F3 ) ;

<!-- b000609 | prose | pages [25] -->
NodeFormation.m

<!-- b000610 | prose | pages [25] -->
1 cnt =1;

<!-- b000611 | prose | pages [25] -->
2 X= [ ] ;

<!-- b000612 | prose | pages [25] -->
3 for i =1:64

<!-- b000613 | prose | pages [25] -->
4 for j =1:5

<!-- b000614 | furniture | pages [26] -->
Team # 1900007

<!-- b000615 | furniture | pages [26] -->
Page 24 of 26

<!-- b000616 | prose | pages [26] -->
5 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000617 | prose | pages [26] -->
6 X( cnt , 2 ) =10∗( j −1) +5;

<!-- b000618 | prose | pages [26] -->
7 cnt=cnt +1;

<!-- b000619 | prose | pages [26] -->
8 end

<!-- b000620 | prose | pages [26] -->
9 end

<!-- b000621 | prose | pages [26] -->
10 for i =1:23

<!-- b000622 | prose | pages [26] -->
11 for j =1:6

<!-- b000623 | prose | pages [26] -->
12 X( cnt , 1 ) =10∗( i −1) +420;

<!-- b000624 | prose | pages [26] -->
13 X( cnt , 2 ) =10∗( j −1) +60;

<!-- b000625 | prose | pages [26] -->
14 cnt=cnt +1;

<!-- b000626 | prose | pages [26] -->
15 end

<!-- b000627 | prose | pages [26] -->
16 end

<!-- b000628 | prose | pages [26] -->
17 for i =1:64

<!-- b000629 | prose | pages [26] -->
18 for j =1:4

<!-- b000630 | prose | pages [26] -->
19 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000631 | prose | pages [26] -->
20 X( cnt , 2 ) =10∗( j −1) +130;

<!-- b000632 | prose | pages [26] -->
21 cnt=cnt +1;

<!-- b000633 | prose | pages [26] -->
22 end

<!-- b000634 | prose | pages [26] -->
23 end

<!-- b000635 | prose | pages [26] -->
24 for i =1:4

<!-- b000636 | prose | pages [26] -->
25 for j =1:18

<!-- b000637 | prose | pages [26] -->
26 X( cnt , 1 ) =5∗( i −1) +553;

<!-- b000638 | prose | pages [26] -->
27 X( cnt , 2 ) =5∗( j −1) +175;

<!-- b000639 | prose | pages [26] -->
28 cnt=cnt +1;

<!-- b000640 | prose | pages [26] -->
29 end

<!-- b000641 | prose | pages [26] -->
30 end

<!-- b000642 | prose | pages [26] -->
31 for i =1:64

<!-- b000643 | prose | pages [26] -->
32 for j =1:5

<!-- b000644 | prose | pages [26] -->
33 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000645 | prose | pages [26] -->
34 X( cnt , 2 ) =10∗( j −1) +270;

<!-- b000646 | prose | pages [26] -->
35 cnt=cnt +1;

<!-- b000647 | prose | pages [26] -->
36 end

<!-- b000648 | prose | pages [26] -->
37 end

<!-- b000649 | prose | pages [26] -->
38 for i =1:17

<!-- b000650 | prose | pages [26] -->
39 for j =1:6

<!-- b000651 | prose | pages [26] -->
40 X( cnt , 1 ) =10∗( i −1) +480;

<!-- b000652 | prose | pages [26] -->
41 X( cnt , 2 ) =10∗( j −1) +320;

<!-- b000653 | prose | pages [26] -->
42 cnt=cnt +1;

<!-- b000654 | prose | pages [26] -->
43 end

<!-- b000655 | prose | pages [26] -->
44 end

<!-- b000656 | prose | pages [26] -->
45 for i =1:64

<!-- b000657 | prose | pages [26] -->
46 for j =1:5

<!-- b000658 | prose | pages [26] -->
47 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000659 | prose | pages [26] -->
48 X( cnt , 2 ) =10∗( j −1) +390;

<!-- b000660 | prose | pages [26] -->
49 cnt=cnt +1;

<!-- b000661 | prose | pages [26] -->
50 end

<!-- b000662 | prose | pages [26] -->
51 end

<!-- b000663 | prose | pages [26] -->
52 for i =1:4

<!-- b000664 | prose | pages [26] -->
53 for j =1:4

<!-- b000665 | prose | pages [26] -->
54 X( cnt , 1 ) =5∗( i −1) +553;

<!-- b000666 | prose | pages [26] -->
55 X( cnt , 2 ) =5∗( j −1) +435;

<!-- b000667 | prose | pages [26] -->
56 cnt=cnt +1;

<!-- b000668 | prose | pages [26] -->
57 end

<!-- b000669 | prose | pages [26] -->
58 end

<!-- b000670 | prose | pages [26] -->
59 for i =1:64

<!-- b000671 | prose | pages [26] -->
60 for j =1:5

<!-- b000672 | prose | pages [26] -->
61 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000673 | prose | pages [26] -->
62 X( cnt , 2 ) =10∗( j −1) +460;

<!-- b000674 | prose | pages [26] -->
63 cnt=cnt +1;

<!-- b000675 | prose | pages [26] -->
64 end

<!-- b000676 | furniture | pages [27] -->
Team # 1900007

<!-- b000677 | furniture | pages [27] -->
Page 25 of 26

<!-- b000678 | prose | pages [27] -->
65 end

<!-- b000679 | prose | pages [27] -->
66 for i =1:17

<!-- b000680 | prose | pages [27] -->
67 for j =1:7

<!-- b000681 | prose | pages [27] -->
68 X( cnt , 1 ) =10∗( i −1) +480;

<!-- b000682 | prose | pages [27] -->
69 X( cnt , 2 ) =10∗( j −1) +510;

<!-- b000683 | prose | pages [27] -->
70 cnt=cnt +1;

<!-- b000684 | prose | pages [27] -->
71 end

<!-- b000685 | prose | pages [27] -->
72 end

<!-- b000686 | prose | pages [27] -->
73 for i =1:64

<!-- b000687 | prose | pages [27] -->
74 for j =1:4

<!-- b000688 | prose | pages [27] -->
75 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000689 | prose | pages [27] -->
76 X( cnt , 2 ) =10∗( j −1) +580;

<!-- b000690 | prose | pages [27] -->
77 cnt=cnt +1;

<!-- b000691 | prose | pages [27] -->
78 end

<!-- b000692 | prose | pages [27] -->
79 end

<!-- b000693 | prose | pages [27] -->
80 for i =1:4

<!-- b000694 | prose | pages [27] -->
81 for j =1:2

<!-- b000695 | prose | pages [27] -->
82 X( cnt , 1 ) =5∗( i −1) +553;

<!-- b000696 | prose | pages [27] -->
83 X( cnt , 2 ) =5∗( j −1) +625;

<!-- b000697 | prose | pages [27] -->
84 cnt=cnt +1;

<!-- b000698 | prose | pages [27] -->
85 end

<!-- b000699 | prose | pages [27] -->
86 end

<!-- b000700 | prose | pages [27] -->
87 for i =1:64

<!-- b000701 | prose | pages [27] -->
88 for j =1:4

<!-- b000702 | prose | pages [27] -->
89 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000703 | prose | pages [27] -->
90 X( cnt , 2 ) =10∗( j −1) +640;

<!-- b000704 | prose | pages [27] -->
91 cnt=cnt +1;

<!-- b000705 | prose | pages [27] -->
92 end

<!-- b000706 | prose | pages [27] -->
93 end

<!-- b000707 | prose | pages [27] -->
94 for i =1:17

<!-- b000708 | prose | pages [27] -->
95 for j =1:6

<!-- b000709 | prose | pages [27] -->
96 X( cnt , 1 ) =10∗( i −1) +480;

<!-- b000710 | prose | pages [27] -->
97 X( cnt , 2 ) =10∗( j −1) +690;

<!-- b000711 | prose | pages [27] -->
98 cnt=cnt +1;

<!-- b000712 | prose | pages [27] -->
99 end

<!-- b000713 | prose | pages [27] -->
100 end

<!-- b000714 | prose | pages [27] -->
101 for i =1:64

<!-- b000715 | prose | pages [27] -->
102 for j =1:5

<!-- b000716 | prose | pages [27] -->
103 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000717 | prose | pages [27] -->
104 X( cnt , 2 ) =10∗( j −1) +755;

<!-- b000718 | prose | pages [27] -->
105 cnt=cnt +1;

<!-- b000719 | prose | pages [27] -->
106 end

<!-- b000720 | prose | pages [27] -->
107 end

<!-- b000721 | prose | pages [27] -->
108 for i =1:4

<!-- b000722 | prose | pages [27] -->
109 for j =1:4

<!-- b000723 | prose | pages [27] -->
110 X( cnt , 1 ) =5∗( i −1) +553;

<!-- b000724 | prose | pages [27] -->
111 X( cnt , 2 ) =5∗( j −1) +805;

<!-- b000725 | prose | pages [27] -->
112 cnt=cnt +1;

<!-- b000726 | prose | pages [27] -->
113 end

<!-- b000727 | prose | pages [27] -->
114 end

<!-- b000728 | prose | pages [27] -->
115 for i =1:64

<!-- b000729 | prose | pages [27] -->
116 for j =1:5

<!-- b000730 | prose | pages [27] -->
117 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000731 | prose | pages [27] -->
118 X( cnt , 2 ) =10∗( j −1) +825;

<!-- b000732 | prose | pages [27] -->
119 cnt=cnt +1;

<!-- b000733 | prose | pages [27] -->
120 end

<!-- b000734 | prose | pages [27] -->
121 end

<!-- b000735 | prose | pages [27] -->
122 for i =1:17

<!-- b000736 | prose | pages [27] -->
123 for j =1:7

<!-- b000737 | prose | pages [27] -->
124 X( cnt , 1 ) =10∗( i −1) +480;

<!-- b000738 | furniture | pages [28] -->
Team # 1900007

<!-- b000739 | furniture | pages [28] -->
Page 26 of 26

<!-- b000740 | prose | pages [28] -->
125 X( cnt , 2 ) =10∗( j −1) +875;

<!-- b000741 | prose | pages [28] -->
126 cnt=cnt +1;

<!-- b000742 | prose | pages [28] -->
127 end

<!-- b000743 | prose | pages [28] -->
128 end

<!-- b000744 | prose | pages [28] -->
129 for i =1:64

<!-- b000745 | prose | pages [28] -->
130 for j =1:5

<!-- b000746 | prose | pages [28] -->
131 X( cnt , 1 ) =10∗( i −1) +5;

<!-- b000747 | prose | pages [28] -->
132 X( cnt , 2 ) =10∗( j −1) +945;

<!-- b000748 | prose | pages [28] -->
133 cnt=cnt +1;

<!-- b000749 | prose | pages [28] -->
134 end

<!-- b000750 | prose | pages [28] -->
135 end

<!-- b000751 | prose | pages [28] -->
136 X( 3 7 0 1 , : ) =[478 ,536];

<!-- b000752 | prose | pages [28] -->
137 X( 3 7 0 2 , : ) =[404 ,622];

<!-- b000753 | prose | pages [28] -->
138 X( 3 7 0 3 , : ) =[324 ,623];

<!-- b000754 | prose | pages [28] -->
139 X( 3 7 0 4 , : ) =[113 ,454];
