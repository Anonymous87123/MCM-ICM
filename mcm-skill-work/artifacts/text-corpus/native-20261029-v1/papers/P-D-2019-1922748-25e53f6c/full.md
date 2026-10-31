# P-D-2019-1922748-25e53f6c

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | prose | pages [1] -->
1922748

<!-- b000007 | prose | pages [1] -->
T1 ________________

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | prose | pages [1] -->
T2 ________________

<!-- b000010 | prose | pages [1] -->
F1 ________________

<!-- b000011 | prose | pages [1] -->
F2 ________________

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T3 ________________

<!-- b000014 | prose | pages [1] -->
F3 ________________

<!-- b000015 | title | pages [1] -->
D

<!-- b000016 | prose | pages [1] -->
T4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | prose | pages [1] -->
F4 ________________

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | prose | pages [1] -->
2019 MCM/ICM

<!-- b000021 | heading | pages [1] -->
Summary Sheet

<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | prose | pages [1] -->
A  Systematic  Dynamic  Route  Planning  Model

<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | heading | pages [1] -->
Summary

<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | prose | pages [1] -->
The object of our model is to provide an emergency evacuation for the Louvre. In the meantime, this model can also identify potential bottlenecks and has certain adaptability. However, complex building structures and the interaction among people makes the problem much harder. In this paper, we present a system dynamic planning model. And both the systematicness during the planning and the individuality of the visitors are considered in our model.

<!-- b000030 | furniture | pages [1] -->


<!-- b000031 | prose | pages [1] -->
The first part of our model is to solve the influence of individual factors. The effect will be ultimately reflected in the flow speed of the crowd. In this way, while calculating the flow speed of the crowd, we adopt N&M model and Stable Evacuation Speed model (SES Model) to deal with different situation.

<!-- b000032 | furniture | pages [1] -->


<!-- b000033 | prose | pages [1] -->
The second part is to visualize the building into a graph. Then simplify the problem from muti- to-muti plan to single-to-single plan through adding two virtual nodes. This step makes the following solution much easier.

<!-- b000034 | furniture | pages [1] -->


<!-- b000035 | prose | pages [1] -->
The third part of the model is the systematic planning of evacuation route. Here a new algorithm with Ford-Fulkerson algorithm as the core, and considering the previous two parts of the model are proposed. In this way, the algorithm can carry out route planning from the perspective of system, and fully consider the micro factors.

<!-- b000036 | furniture | pages [1] -->


<!-- b000037 | prose | pages [1] -->
Then, a simulated building is built to verify the validity of the model. The model obtains the result within 0.457s with a scale of 770 people. Besides, to a certain extent, the result matches practical case. In addition, it is able to evacuate the crowd from the dangerous room with the fastest speed in the emergency treatment, which shows excellent performance.

<!-- b000038 | furniture | pages [1] -->


<!-- b000039 | prose | pages [1] -->
Finally, we implement this model to the Louvre. It cost 36.15s to get the result with a scale of 6700 people and accuracy of 0.1s. The total evacuation cost 288.7s.  After the flow and margin matrices are visualized, it clearly shows the whole evacuation process and potential bottlenecks. Also, we present a series of suggestions for practical use of the model.

<!-- b000040 | furniture | pages [1] -->


<!-- b000041 | keywords | pages [1] -->
Key words: N&M model;Stable evacuation speed model;Ford-Fulkerson algorithm;System

<!-- b000042 | prose | pages [1] -->
dynamic planning

<!-- b000043 | heading | pages [2] -->
Contents

<!-- b000044 | contents | pages [2] -->
1

<!-- b000045 | heading | pages [2] -->
Introduction

<!-- b000046 | prose | pages [2] -->
1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Restatement of problems 1 Overview of our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000047 | prose | pages [2] -->
2

<!-- b000048 | heading | pages [2] -->
Assumptions

<!-- b000049 | prose | pages [2] -->
3

<!-- b000050 | heading | pages [2] -->
Symbols and Notation

<!-- b000051 | prose | pages [2] -->
4

<!-- b000052 | heading | pages [2] -->
Microscopic model:

<!-- b000053 | heading | pages [2] -->
personnel evacuation speed model

<!-- b000054 | prose | pages [2] -->
2

<!-- b000055 | prose | pages [2] -->
3

<!-- b000056 | prose | pages [2] -->
3

<!-- b000057 | prose | pages [2] -->
3 A possible model of diﬀerent road segments (N&M model) . . . . . . . . . . 4.1 3 A possible model considering the degree of congestion . . . . . . . . . . . . . 4.2

<!-- b000058 | prose | pages [2] -->
5 Construction of the graph

<!-- b000059 | prose | pages [2] -->
4

<!-- b000060 | prose | pages [2] -->
6 Description of the diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 6 Matrix model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 7 Dynamic system planning algorithm . . . . . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000061 | prose | pages [2] -->
6

<!-- b000062 | heading | pages [2] -->
Simulation model validation

<!-- b000063 | prose | pages [2] -->
9

<!-- b000064 | prose | pages [2] -->
11 model initialization instructions . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 11 Evacuation plan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 11 Three types of bottleneck problems . . . . . . . . . . . . . . . . . . . . . . . 6.3 12 Adaptive analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.4 14 Entry of emergency personnel . . . . . . . . . . . . . . . . . . . . . . . . . . 6.5

<!-- b000065 | prose | pages [2] -->
7

<!-- b000066 | heading | pages [2] -->
Louvre evacuation model

<!-- b000067 | prose | pages [2] -->
15

<!-- b000068 | prose | pages [2] -->
15 Application of the dynamic node graph in the Louvre . . . . . . . . . . . . . 7.1 15 Analysis of the results of the Louvre model . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000069 | prose | pages [2] -->
8

<!-- b000070 | heading | pages [2] -->
How to use the model

<!-- b000071 | prose | pages [2] -->
9

<!-- b000072 | heading | pages [2] -->
Conclusion

<!-- b000073 | prose | pages [2] -->
16

<!-- b000074 | prose | pages [2] -->
17

<!-- b000075 | prose | pages [2] -->
18 Sensitivity analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 18 The model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2 19 The algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3 19

<!-- b000076 | furniture | pages [3] -->
Team#1922748

<!-- b000077 | furniture | pages [3] -->
page 1 of 20

<!-- b000078 | prose | pages [3] -->
1

<!-- b000079 | heading | pages [3] -->
Introduction

<!-- b000080 | prose | pages [3] -->
1.1

<!-- b000081 | heading | pages [3] -->
Background

<!-- b000082 | prose | pages [3] -->
Today, museums, libraries, and exhibition halls around the world are paying more attention to the safe evacuation of venues, and are looking for suitable emergency evacuation methods. Therefore, it is vital to establish a widely used and adaptable emergency evacuation model. In recent years, many scholars have put forward their own opinions in this ﬁeld, and established various models. Among them, Wakim proposed a Markov pedestrian model based on the analysis of pedestrian dynamic behavior and Markov chain[1]; Helbing, a German scholar, proposed a social force model that can organize a series of self-organizing phenomena in the process of current human movement[2]. The above models are very suitable for the study of individual movement in emergency evacuation. And they’re very accurate for the bottleneck problem, which means situations when movement is dramatically slowed or even stopped. However, for a large, multi-story venue like the Louvre, an evacuation model with a general view from the whole to the local is needed. Therefore, based on the establishment of the spatial simulation maximum ﬂow node graph model, we use the maximum ﬂow method to explore how to choose the most appropriate evacuation scheme in case of emergency.

<!-- b000083 | prose | pages [3] -->
1.2 Restatement of problems

<!-- b000084 | prose | pages [3] -->
The Louvre is one of the largest and most visited art museums in the world. Due to the diversity of visitors and the complex structure of the building, it poses a great challenge to safe evacuation. We need to develop an emergency evacuation model to provide museum staﬀwith options for evacuation options in diﬀerent situations, and to popularize other large crowded structures.

<!-- b000085 | prose | pages [3] -->
The established model needs to accomplish the following objectives: I.Give instructions to allow museum personnel to explore a range of options to evacuate visitors from the museum;

<!-- b000086 | prose | pages [3] -->
II.Identify potential bottlenecks that may limit export movement; III.Allow emergency personnel to enter buildings as soon as possible; IV.The models can be used to solve a wide range of considerations and various types of potential threats;

<!-- b000087 | prose | pages [3] -->
V.Extend to other large crowded structures.

<!-- b000088 | prose | pages [3] -->
At the same time, the model should consider several implicit objectives: I.How to evacuate when the total number is diﬀerent; II.When there are individual inﬂuence such as small group or diﬀerent language speakers, how to arrange evacuation plan;

<!-- b000089 | prose | pages [3] -->
III.When and how any additional exits. The mind map (Figure 1) shows the issues that need to be addressed.

<!-- b000090 | furniture | pages [4] -->
Team#1922748

<!-- b000091 | furniture | pages [4] -->
page 2 of 20

<!-- b000092 | caption | pages [4] -->
Figure 1: Problem unfolding

<!-- b000093 | prose | pages [4] -->
1.3 Overview of our work

<!-- b000094 | prose | pages [4] -->
In our research program, the ﬁrst step is the microscopic part: to ﬁnd out the law of human ﬂow speed based on the existing crowd movement model, including ”staircase model”, ”corridor model” and ”room exit model”. The second step is to establish a spatial node graph for the venue with the idea of graph theory. And use nodes to represent various parts of the venue, such as rooms and halls, lines to indicate the stairs, corridors, etc. connected to each part.

<!-- b000095 | prose | pages [4] -->
The third step is the macro part: combined with the idea of the Ford- Fulkerson algorithm, we set the optimization goal as the speed of all exits ﬂow at each moment is the maximum that can be achieved, and dynamically observe the evacuation and make adjustments by iterative method. The ﬁnal step is to promote the model so that rescuers can get in time and make the model able to cope with other potential threats.

<!-- b000096 | prose | pages [4] -->
The ﬂow chart (Figure 2) illustrate the above ideas in a more visual way.

<!-- b000097 | caption | pages [4] -->
Figure 2: Method and process

<!-- b000098 | furniture | pages [5] -->
Team#1922748

<!-- b000099 | prose | pages [5] -->
2

<!-- b000100 | heading | pages [5] -->
Assumptions

<!-- b000101 | furniture | pages [5] -->
page 3 of 20

<!-- b000102 | prose | pages [5] -->
1. The guiding signs and notiﬁcations of the venues are clear enough for emergency evacua- tion. 2. While evacuating, the vast majority of people are rational enough to follow the signs and notiﬁcations and complete the escape. 3. No additional accidents such as stampedes occur during evacuation. 4. When evacuating, the crowd will not evacuate in opposite directions. 5. The doors of each main room are of moderate size and width, which will not cause over- crowding.

<!-- b000103 | prose | pages [5] -->
3

<!-- b000104 | heading | pages [5] -->
Symbols and Notation

<!-- b000105 | caption | pages [5] -->
Table 1: Symbol descriptions

<!-- b000106 | prose | pages [5] -->
descriptions symbol units Evacuation Speed of Flow v m/s m2/people Average personal area Sind m2 Total area of human ﬂow Stotal

<!-- b000107 | prose | pages [5] -->
\ Crowd congestion D \ Speed coeﬃcient k people/m2 Population density ρ

<!-- b000108 | prose | pages [5] -->
Human ﬂow q people/s \ Overall matrix of the model G

<!-- b000109 | prose | pages [5] -->
Note: Symbols not mentioned in the table will be explained if they appear below.

<!-- b000110 | prose | pages [5] -->
4

<!-- b000111 | heading | pages [5] -->
Microscopic model:

<!-- b000112 | heading | pages [5] -->
personnel evacuation speed model

<!-- b000113 | heading | pages [5] -->
A possible model of diﬀerent road segments (N&M model)

<!-- b000114 | prose | pages [5] -->
4.1

<!-- b000115 | prose | pages [5] -->
According to the related research of Predtechenski and Milinskii [3], the average evacuation speed is a function of the ﬂow density. Besides,they used the observation data of the aisle and stairs to ﬁt the relationship curve. Unfortunately, this is a complex nonlinear relationship, that is not suitable for a wide range of applications.

<!-- b000116 | prose | pages [5] -->
After that, Nelson and Mowrer et al[4]. simpliﬁed the relationship between velocity and ﬂow density to a linear relationship, and selected diﬀerent linear coeﬃcients for diﬀerent e- vacuation channels. When 0.54 persons/m2 ≤D ≤3.8 persons/m2, the relationship between the moving speed and the ﬂow density is as follows.

<!-- b000117 | prose | pages [5] -->
v = k −0.266kD (1)

<!-- b000118 | furniture | pages [6] -->
Team#1922748

<!-- b000119 | furniture | pages [6] -->
page 4 of 20

<!-- b000120 | prose | pages [6] -->
Where, we deﬁne D as the crowd congestion degree, that is, the ratio of the actual area of the human body in the crowd to the total area of the ﬂow of people, which reﬂects the overall crowding degree of the crowd. It can be derived from D = NSind

<!-- b000121 | prose | pages [6] -->
Stotal , Where,Sind refers to the average personal occupation area, Stotal refers to the total area of the ﬂow of people. And k in the formula (1) can be determined from Table 2[5].

<!-- b000122 | caption | pages [6] -->
Table 2: Speed coeﬃcient k

<!-- b000123 | prose | pages [6] -->
Evacuation Channel Type

<!-- b000124 | prose | pages [6] -->
Stairs Riser/mm

<!-- b000125 | prose | pages [6] -->
190

<!-- b000126 | prose | pages [6] -->
Stairs

<!-- b000127 | prose | pages [6] -->
178 165 165

<!-- b000128 | prose | pages [6] -->
k

<!-- b000129 | prose | pages [6] -->
Tread/mm

<!-- b000130 | prose | pages [6] -->
254 1.00 279 1.08 305 1.16 330 1.23 Corridor,Aisle,Ramp, Doorway 1.40

<!-- b000131 | prose | pages [6] -->
Corresponding to the above table, k is taken as 1 and 1.4 respectively to obtain the ”staircase model”and ”corridor model”.

<!-- b000132 | prose | pages [6] -->
In summary, N&M Model[6] considers the relationship between evacuation speed and ﬂow density[7], and gives diﬀerent models such as the staircase model and corridor model for diﬀerent road sections, but it is not suitable for the situation where the ﬂow density is relatively large, such as the narrow exit of the room. So we try to ﬁnd a better model to replace it.

<!-- b000133 | heading | pages [6] -->
A possible model considering the degree of congestion

<!-- b000134 | prose | pages [6] -->
4.2

<!-- b000135 | prose | pages [6] -->
4.2.1 Crowding in two directions

<!-- b000136 | prose | pages [6] -->
According to research by Lu Junan and others, the speed of personnel escape is aﬀected by Front- Crowding and Side-Crowding.[8]

<!-- b000137 | prose | pages [6] -->
Front-Crowding: In an escaped group, taking the exit as the coordinate origin, suppose the location of the j-th person is at xj, the speed of him is dxj

<!-- b000138 | prose | pages [6] -->
dt . So the distance from the previous j −1-th person is |xj −xj−1|, which is recorded as A, also, the relative velocity is

<!-- b000139 | prose | pages [6] -->
dxj

<!-- b000140 | prose | pages [6] -->
dt −dxj−1

<!-- b000141 | prose | pages [6] -->
dt , which is recorded as B. Then the forward damping force caused by crowding before and after is proportional to B

<!-- b000142 | prose | pages [6] -->
A. Side-Crowding: Here we use a frictional damping force to describe the level of Side- Crowding[9]. Note that Side-Crowding is generally suitable when the crowd density is par- ticularly large, and when the population density is small, it has little eﬀect.

<!-- b000143 | prose | pages [6] -->
4.2.2 Escape velocity dynamic equation

<!-- b000144 | prose | pages [6] -->
According to Newton’s second law, we have obtained the following escape velocity dynamics equation.

<!-- b000145 | prose | pages [6] -->
d2xj

<!-- b000146 | prose | pages [6] -->
dt −dxj−1

<!-- b000147 | prose | pages [6] -->
dt2 = α(dxj

<!-- b000148 | prose | pages [6] -->
−mj

<!-- b000149 | prose | pages [6] -->
)/ |xj −xj−1| + fj (2) dt

<!-- b000150 | furniture | pages [7] -->
Team#1922748

<!-- b000151 | furniture | pages [7] -->
page 5 of 20

<!-- b000152 | prose | pages [7] -->
Where j = 2 N, which constitutes a system of equations with N −1 equations.

<!-- b000153 | heading | pages [7] -->
Stable evacuation speed model (SES Model)

<!-- b000154 | prose | pages [7] -->
4.2.3

<!-- b000155 | prose | pages [7] -->
Performing integration of the above formula,we get

<!-- b000156 | prose | pages [7] -->
dt =λjLn (xj−1 (t) −xj (t)) −Fj

<!-- b000157 | prose | pages [7] -->
dxj

<!-- b000158 | prose | pages [7] -->
+ cj (3)

<!-- b000159 | prose | pages [7] -->
mj

<!-- b000160 | prose | pages [7] -->
In the formula, Fj is the integral term of fj and cj is a constant term. Let each person occupy a square with an area of LL,Set the front interval as L + d1, the side interval is L + d2.

<!-- b000161 | prose | pages [7] -->
1 1 L+d1, side density ρ2 = Then front density ρ1 = Evacuation speed L+d2.

<!-- b000162 | prose | pages [7] -->
v(ρ1, ρ2) = dxj

<!-- b000163 | prose | pages [7] -->
(4) dt

<!-- b000164 | prose | pages [7] -->
When v(ρ1, ρ2) = 0, ρ1=ρ1m, ρ2 = ρ2m. ρ1m and ρ2m represent front and side maximum density respectively. Then use the expression containing ρ1mρ2m to indicate cj. Substituting a into equation (1), we get

<!-- b000165 | prose | pages [7] -->
{

<!-- b000166 | prose | pages [7] -->
ρ1 −k(ρ2−ρ2m)

<!-- b000167 | prose | pages [7] -->
λjLnρ1m

<!-- b000168 | prose | pages [7] -->
vj(ρ1, ρ2) =

<!-- b000169 | prose | pages [7] -->
vm (ρic < ρi ≤ρim, i = 1, 2) mj mj (5) (ρi ≤ρic, i = 1, 2)

<!-- b000170 | prose | pages [7] -->
When the density is small, the velocity of the human ﬂow is not aﬀected by it, and the critical density does not aﬀect the velocity[10].

<!-- b000171 | prose | pages [7] -->
Considering other factors such as personnel characteristics, the degree of inﬂuence before and after congestion is diﬀerent, we attain

<!-- b000172 | prose | pages [7] -->
+ β(ρ2m −ρ2)

<!-- b000173 | prose | pages [7] -->
vj(ρ1, ρ2) = vm (αLn ρ1m/ρ1

<!-- b000174 | prose | pages [7] -->
+ γ) (6)

<!-- b000175 | prose | pages [7] -->
ρ2m −ρ2c

<!-- b000176 | prose | pages [7] -->
ρ1m/ρ1c

<!-- b000177 | prose | pages [7] -->
where, ρ = ρ1ρ2=D, ρ1c and ρ2c are respectively the critical densities of two directions. α, β, γ is corresponding weight of each aspect.

<!-- b000178 | prose | pages [7] -->
The above is the evacuation escape speed model, also known as the SES Model. It is analyzed that the above model is a generalized model. When the ﬂow density is large, neither of α, β, γ is zero. When the ﬂow density gets smaller, it can be considered to be mainly aﬀected by Front-Crowding; when the ﬂow density is small enough, only the impact of personnel characteristics can be considered. At this time, the population structure is relatively uniform under normal circumstances, the characteristics of the personnel should be consistent, and v is a certain value[11]. Here ia an example to implement this model.

<!-- b000179 | prose | pages [7] -->
According to the ﬁre safety principle data prepared by M.Y.Roytman et al.[12], the adult body thickness in the front and rear direction is about 0.32 m, and the body width in both directions is 0.5 m.Considering that the contact between the human body is the highest density, it can be considered that the maximum density ρ1m and ρ2m in the front and side directions are 3 persons/m and 2 persons/m, respectively. According to the research data of Ando et al.[13], when distance between the human body lines is about 0.75 m. According

<!-- b000180 | furniture | pages [8] -->
Team#1922748

<!-- b000181 | furniture | pages [8] -->
page 6 of 20

<!-- b000182 | prose | pages [8] -->
to this, the critical density ρ1c and ρ2c of the front direction and the side direction are about 0.89 persons/m and 1.33 persons/m, respectively. Substituting the above ρ1m, ρ2m, ρ1c and ρ2c into the model, we obtain:

<!-- b000183 | prose | pages [8] -->
A = 1.32 −0.82Ln(ρ) (7) B = 3.0 −0.76ρ

<!-- b000184 | prose | pages [8] -->
vj(ρ) = vm (αA + βB + γ) (8)

<!-- b000185 | prose | pages [8] -->
The SES model considers the combined eﬀects of factors such as Front-Crowding,Side- Crowding and other personnel characteristics on evacuation speed during evacuation, and can comprehensively reﬂect the inﬂuencing factors of evacuation speed[14]. The only downside is that due to the uncertainty and ambiguity of the characteristics of the personnel, the eﬀect of this part on the whole cannot be well described.

<!-- b000186 | prose | pages [8] -->
5 Construction of the graph

<!-- b000187 | prose | pages [8] -->
5.1 Description of the diagram

<!-- b000188 | prose | pages [8] -->
Graphs are one of the most powerful frameworks in data structure and algorithmics. Graphs can be used to represent almost any type of structure or system. In this problem, the Louvre is a complex space building structure. To explore its personnel evacuation plan, the method of constructing a node graph can be adopted. To simplify the calculation, we added two hypothetical nodes 1 and 9.

<!-- b000189 | prose | pages [8] -->
For the sake of convenience, we can use the schematic shown in Figure 3 to represent the idea of a node graph. In Figure 3, we imagine a building with six rooms, where the numbers 2 to 7 represent these rooms. The green line segments indicate the relationship between the rooms, where the solid lines indicate the corridors, and the dotted lines indicate that there is a staircase between the connections of the rooms.

<!-- b000190 | caption | pages [8] -->
Figure 3: Node graph of a hypothetical building

<!-- b000191 | prose | pages [8] -->
It can be seen that in Figure 3, the green box shows the entire structure of the building. If we use the maximum ﬂow method to calculate the node graph on this basis, we will ﬁnd that

<!-- b000192 | furniture | pages [9] -->
Team#1922748

<!-- b000193 | furniture | pages [9] -->
page 7 of 20

<!-- b000194 | prose | pages [9] -->
this is a ”multi-target to multi-target” problem, that is, corresponding to evacuation from multiple rooms to multiple exits. Although the node structure diagram in the green frame is very intuitive, such multi-objective planning brings a lot of trouble to the calculation. In addition, the Louvre itself is a large and complex space building, and the planning of the evacuation plan will be very complicated and diﬃcult to calculate.

<!-- b000195 | prose | pages [9] -->
So, we added two special nodes, which are represented by the number 9 and the number 1 in Figure 3.

<!-- b000196 | prose | pages [9] -->
Node 9 is called ”sink point” and represents the external environment. Its black line with the numbers 6, 7, and 8 indicates the three exits of the building. Node 1 is called the source point and does not have practical meaning. However, the number (not shown in Figure 3) on the line connecting it to each room indicates the number of people remaining in the room at a certain moment. It is worth noting that when the problem is solved later, all the connections will have numbers, and their meanings will be diﬀerent, which will be explained in the later process.

<!-- b000197 | prose | pages [9] -->
The addition of two special nodes makes the multi-objective programming problem that is complicated and diﬃcult to calculate become a simple and easy to calculate single-objective programming problem. The function of node 1 is to represent the remaining number truly and accurately. The function of node 9 is to express the ﬂow of people leaving the building from the exit. This creates a new ”single goal to single goal” issue. This result corresponds to the relationship between the total number of people remaining in all rooms and the ﬂow of people leaving all exits. The simpliﬁcation of the goal brings great convenience to the optimization of the algorithm.

<!-- b000198 | prose | pages [9] -->
In addition, adding two virtual nodes has other beneﬁts that will be explained in the theory of algorithm in the next section.

<!-- b000199 | prose | pages [9] -->
5.2

<!-- b000200 | heading | pages [9] -->
Matrix model

<!-- b000201 | prose | pages [9] -->
After the model of the graph is established, all we need to do is to incorporate the numerical calculations on this basis.

<!-- b000202 | prose | pages [9] -->
In order to clearly show the variation of human ﬂow during the simulated evacuation process and to see the optimal evacuation route planning, we can integrate various data with the help of the matrix.

<!-- b000203 | prose | pages [9] -->
In this model, the data needed to simulate the evacuation law are as follows:

<!-- b000204 | heading | pages [9] -->
I. The number of people in each room at any time of evacuation. We use the number of

<!-- b000205 | prose | pages [9] -->
source points connected to each room to represent them.

<!-- b000206 | heading | pages [9] -->
II. During the evacuation process, the number of people passing between adjacent parts

<!-- b000207 | prose | pages [9] -->
(rooms) during a period of time, that is, the ﬂow of people carried by corridors or stairs during a period of time. We use numbers on the connecting lines between rooms to represent them.

<!-- b000208 | heading | pages [9] -->
III. In the process of evacuation, the number of people evacuated from each exit at any

<!-- b000209 | prose | pages [9] -->
time, in other words, the ﬂow of the exit. They are represented by numbers on the connecting line between the outlet and the outside (sink point).

<!-- b000210 | prose | pages [9] -->
Assuming that a building is divided into n parts, we can interpret it as n rooms, then we build a model with n nodes. At the same time, we can establish a matrix of n × n, in which the elements represent the connection between nodes. Since this n-order matrix can only represent the exchange of people between rooms in the building, and can not reﬂect the

<!-- b000211 | furniture | pages [10] -->
Team#1922748

<!-- b000212 | furniture | pages [10] -->
page 8 of 20

<!-- b000213 | prose | pages [10] -->
number of people remaining in the room or evacuating the building, we extend this n-order matrix to a circle and turn it into a (n + 2) × (n + 2) matrix, as shown in Figure 4.

<!-- b000214 | prose | pages [10] -->
The ﬁnal n + 2 matrix is composed of several parts, which can establish their respective matrices.

<!-- b000215 | heading | pages [10] -->
”corridor model” Cq and ”staircase model” Sq

<!-- b000216 | prose | pages [10] -->
5.2.1

<!-- b000217 | prose | pages [10] -->
Firstly, the ”corridor model” channel traﬃc matrix Cq satisﬁes the following set of equations:

<!-- b000218 | prose | pages [10] -->


<!-- b000219 | prose | pages [10] -->
ci,j = v = k −0.266kD

<!-- b000220 | prose | pages [10] -->


<!-- b000221 | prose | pages [10] -->
ci,j = cj,i

<!-- b000222 | prose | pages [10] -->


<!-- b000223 | prose | pages [10] -->
ci,i = 0

<!-- b000224 | prose | pages [10] -->
{ 2 ≤i ≤n + 1

<!-- b000225 | prose | pages [10] -->
(9)

<!-- b000226 | prose | pages [10] -->
2 ≤j ≤n + 1 . The other elements are all 0. Ci,j represents the ﬂow

<!-- b000227 | prose | pages [10] -->
Among them,

<!-- b000228 | prose | pages [10] -->
of people through the channel over a period of time. This value is calculated by the channel model combined with the density of the ﬂow and the moving speed. Ci,j = Cj,i indicates that the maximum velocity in both directions on the channel is equal. From the matrix point of view, this shows that the human traﬃc matrix is a symmetrical matrix, and the diagonal line is all zero because it has no practical meaning. The meaning of Ci,n+2 = 0 is that the channel model only expresses the interconnection between the various parts of the building, but does not express the relationship between the exit and the outside world. The last column of the total matrix represents the ﬂow of people at the exit of the building. Therefore, the last column of the traﬃc matrix is 0. The matrix is in the following form:

<!-- b000229 | prose | pages [10] -->


<!-- b000230 | prose | pages [10] -->


<!-- b000231 | prose | pages [10] -->
· · · 0 c1,2 c1,n+2 = 0

<!-- b000232 | prose | pages [10] -->
... ...

<!-- b000233 | prose | pages [10] -->


<!-- b000234 | prose | pages [10] -->


<!-- b000235 | prose | pages [10] -->
· · · 0 s1,2 s1,n+2 = 0

<!-- b000236 | prose | pages [10] -->
... ...

<!-- b000237 | prose | pages [10] -->
, Sq=

<!-- b000238 | prose | pages [10] -->


<!-- b000239 | prose | pages [10] -->
· · · c2,1

<!-- b000240 | prose | pages [10] -->
Cq=

<!-- b000241 | prose | pages [10] -->
...

<!-- b000242 | prose | pages [10] -->
... ... · · · · · · · · · cn+2,1 0

<!-- b000243 | prose | pages [10] -->


<!-- b000244 | prose | pages [10] -->


<!-- b000245 | prose | pages [10] -->
· · · s2,1

<!-- b000246 | prose | pages [10] -->
(10)

<!-- b000247 | prose | pages [10] -->
...

<!-- b000248 | prose | pages [10] -->
... ... · · · · · · · · · sn+2,1 0

<!-- b000249 | prose | pages [10] -->
Then the ”staircase model” channel traﬃc matrix Sq. It diﬀers from the ”corridor model” channel traﬃc matrix in that, over a period of time, the calculation method of the traﬃc through the corridor is diﬀerent. It uses the formula of the staircase model:

<!-- b000250 | prose | pages [10] -->
si,j = vj(ρ) = vm (αA + βB + γ) (11)

<!-- b000251 | prose | pages [10] -->
”initial matrix” En and ”export matrix” Ex 5.2.2

<!-- b000252 | prose | pages [10] -->
Next, the initial matrix En. It represents the number of people in each room at the initial Finally, the export matrix Ex. time of evacuation.

<!-- b000253 | prose | pages [10] -->
It represents the number of people evacuated from each exit during the evacuation process, i.e. the exit ﬂow. It diﬀers from the initial matrix En in that it only has the last column which is not zero. En and Ex satisfy the following equation:

<!-- b000254 | prose | pages [10] -->
{ en1,j = tj

<!-- b000255 | prose | pages [10] -->
eni,j = 0, (2 ≤i ≤n + 2) ,

<!-- b000256 | prose | pages [10] -->
{ exi,n+2 = Tj

<!-- b000257 | prose | pages [10] -->
(12) exi,j = 0, (1 ≤j ≤n + 1)

<!-- b000258 | furniture | pages [11] -->
Team#1922748

<!-- b000259 | furniture | pages [11] -->
page 9 of 20

<!-- b000260 | prose | pages [11] -->
The tj is the number that the source point connects with each room at any time. Tj is the number on the connection line between the exit and the outside world (the sink point). Since the initial matrix only represents the remaining number of people in the internal room, it is independent of the channel, so the number of all rows except the ﬁrst row is 0. The matrices are in the following form:

<!-- b000261 | prose | pages [11] -->


<!-- b000262 | prose | pages [11] -->
· · · 0 en1,2 en1,n−1

<!-- b000263 | prose | pages [11] -->
0

<!-- b000264 | prose | pages [11] -->
...

<!-- b000265 | prose | pages [11] -->


<!-- b000266 | prose | pages [11] -->
0

<!-- b000267 | prose | pages [11] -->
· · · 0 0

<!-- b000268 | prose | pages [11] -->
En =

<!-- b000269 | prose | pages [11] -->
...

<!-- b000270 | prose | pages [11] -->
...

<!-- b000271 | prose | pages [11] -->
... ... · · ·

<!-- b000272 | prose | pages [11] -->
0

<!-- b000273 | prose | pages [11] -->
· · · · · · 0 0

<!-- b000274 | prose | pages [11] -->


<!-- b000275 | prose | pages [11] -->


<!-- b000276 | prose | pages [11] -->
 

<!-- b000277 | prose | pages [11] -->
· · · 0 0 0

<!-- b000278 | prose | pages [11] -->
...

<!-- b000279 | prose | pages [11] -->


<!-- b000280 | prose | pages [11] -->


<!-- b000281 | prose | pages [11] -->
· · · 0 ex2,n+2

<!-- b000282 | prose | pages [11] -->
, Ex =

<!-- b000283 | prose | pages [11] -->
...

<!-- b000284 | prose | pages [11] -->
... ...

<!-- b000285 | prose | pages [11] -->
(13)

<!-- b000286 | prose | pages [11] -->
· · · · · · 0 0 exn−1,n+2 · · · 0 0 0

<!-- b000287 | prose | pages [11] -->
The four matrices ultimately form the overall matrix G, visually displayed in Figure 4:

<!-- b000288 | prose | pages [11] -->
G = Cq + Sq + En + Ex (14)

<!-- b000289 | caption | pages [11] -->
Figure 4: Overall matrix diagram

<!-- b000290 | heading | pages [11] -->
Dynamic system planning algorithm

<!-- b000291 | prose | pages [11] -->
5.3

<!-- b000292 | heading | pages [11] -->
Introducing Ford-Fulkerson algorithm

<!-- b000293 | prose | pages [11] -->
5.3.1

<!-- b000294 | prose | pages [11] -->
In the above we have transformed the multi-nodes to multi-nodes model of the building into a single-node to single-node model. In this model, the number of people ﬂowing out of the source at any time should be equal to the number of people entering the sink point. Therefore, in the process of escape, the number of people who escaped is the number of people who go from the source to the sink point. In order to get the maximum of escape speed, we need to make full use of the channel resources in the building at any time to maximize the escape rate. In the established model, the problem is equivalent to obtaining the maximum ﬂow from the source to the sink at any time. For such problems, we can apply the Ford-Fulkerson algorithm and make appropriate corrections. The algorithm is described in detail below[15].

<!-- b000295 | prose | pages [11] -->
Before describing the algorithm, we need to further clarify the meaning of each edge in the model. there are three kinds of nodes, source points, sink points, and room points in

<!-- b000296 | furniture | pages [12] -->
Team#1922748

<!-- b000297 | furniture | pages [12] -->
page 10 of 20

<!-- b000298 | prose | pages [12] -->
the model. The value on the line connecting the source point to the room node indicates the initial number of rooms in the corresponding room. The connection between the room nodes indicates the connection between the rooms, and the value indicates the maximum ﬂow allowed by the channel. The connection between the sink point and the exit room nodes indicates the connection between the exit and the exterior of the building, and its value indicates the maximum passenger ﬂow allowed by the exit.

<!-- b000299 | prose | pages [12] -->
The original Ford-Fulkerson algorithm is an iterative algorithm. In each iteration, the value of the stream is increased by looking for an ”augment path”[16]. The augmented path can be seen as a path from the source point to the sink point, and more streams can be added along this path. Iterating until the augmented path can no longer be found, at least one of the paths from the source point to the sink point must be full (ie, the size of the edge stream is equal to the size of the edge). The resulting stream at this point is the maximum ﬂow in this case, which can be proved by the maximum ﬂow minimum cut theorem. And we will not prove this here.

<!-- b000300 | prose | pages [12] -->
5.3.2

<!-- b000301 | heading | pages [12] -->
Application of Ford-Fulkerson algorithm

<!-- b000302 | prose | pages [12] -->
Since the model we built is not a traditional single-node to single-node mode, and the situ- ation we considered is far more complicated than the Ford-Fulkerson algorithm. Therefore, we properly use the Ford-Fulkerson algorithm in the solution of the problem and propose a dynamic system planning algorithm based on the Ford-Fulkerson algorithm[17]. The algo- rithm takes the general planning and the planning of some rooms in emergency into account. The speciﬁc ﬂow chart is shown in Figure A-1 (shown in appendix).

<!-- b000303 | prose | pages [12] -->
As shown in the ﬂow chart of Figure A-1, the algorithm is divided into two parts, e- mergency handling and general case processing. In general case processing, each iteration represents a situation within a time period, such as within 0 to 1 second. When the number of people in the source point is less than 0.5, the iteration stops and the algorithm ends. In each iteration, the ﬂow matrix and the margin matrix can be derived by the Ford-Fulkerson algorithm. Then, the value of the edge between the source point and the room node in the original model, which is the initial number of people in each room is corrected by the ﬂow matrix. And the current ﬂow velocity model is used to correct the maximum ﬂow of the channel by the current ﬂow density in each channel and the ﬂow density at the exit. This will provide a picture of the ﬂow of people in each time period. Finally, speciﬁc path planning is obtained from all traﬃc matrices. And the degree of use of each channel can be derived from the margin matrix[18].

<!-- b000304 | prose | pages [12] -->
In emergency handling, we make the following processing. As shown in the emergency processing section of Figure A-1, ﬁrst, the person in the emergency room is transferred to the adjacent non-emergency room by default, and the entrance degree of the emergency room is set to zero. According to the maximum ﬂow rate of the connecting channel, the time required for the transition TT can be calculated. Since the emergency transfer route remains unchanged from 0 to TT, regardless of the external situation. In this way, in the general case, at the beginning of each iteration from 0 to TT, the number of people transferred from the emergency room during the time period is added to the remaining number of people in the non-emergency room. And set the corresponding route and ﬁnally integrated into the traﬃc matrix.

<!-- b000305 | furniture | pages [13] -->
Team#1922748

<!-- b000306 | furniture | pages [13] -->
page 11 of 20

<!-- b000307 | prose | pages [13] -->
6

<!-- b000308 | heading | pages [13] -->
Simulation model validation

<!-- b000309 | prose | pages [13] -->
6.1

<!-- b000310 | heading | pages [13] -->
model initialization instructions

<!-- b000311 | prose | pages [13] -->
According to the graph model and matrix model deﬁned in 5.1 and 5.2, we initialize the number of nodes in the node (taking random numbers between 100 and 200), and specify the maximum ﬂow rates of each exit are 40 People/s, 35 People/s, 30 People/s.

<!-- b000312 | prose | pages [13] -->
As shown in Figure 5, 1 is a virtual ingress node, 9 is a virtual egress node, and 2-8 are actual nodes (where in the 6, 7, 8 nodes adjacent to the egress are called ﬁrst-level nodes, and the ﬁrst-level nodes are called second-level nodes), the value on the red line segment represents the initial number of people in the node, the value on the blue line segment represents the reachable maximum ﬂow of the diﬀerent channels between the nodes, and the value on the green line segment represents the maximum ﬂow of each exit.

<!-- b000313 | caption | pages [13] -->
Figure 5: Model initialization

<!-- b000314 | prose | pages [13] -->
6.2 Evacuation plan

<!-- b000315 | prose | pages [13] -->
According to the requirements of the topic, it is our goal to evacuate all personnel as quickly as possible. In order to achieve this goal, we substituted the model into the algorithm and solved it iteratively.

<!-- b000316 | prose | pages [13] -->
Here we take 5s as a time step and make a ﬂow diagram. As shown in Figure 6, the values on the red line have no practical meaning. The values on the blue and green lines indicate the channel and exit ﬂow in the 5S time step. It can be seen intuitively that the ﬁrst step of the evacuation plan is to empty the exit rooms 6, 7and 8. Then the personnel at the second- level nodes move to the adjacent ﬁrst-level nodes (Figure 6(a)). As the operating pressure of the evacuation medium-term channel increases, the channel between the two nodes may be required to be shunted (Figure 6(b)). Then, with the decrease of remaining number, the channel pressure between the two nodes decreases. The ﬂow reduction is even reduced to 0 (Figure 6(c)), and eventually all evacuation is completed.

<!-- b000317 | prose | pages [13] -->
In fact, our evacuation plan is a continuous process of the ﬂow chart given in each time section.

<!-- b000318 | prose | pages [13] -->
According to this evacuation plan, all the people can be evacuated as soon as possible.

<!-- b000319 | furniture | pages [14] -->
Team#1922748

<!-- b000320 | furniture | pages [14] -->
page 12 of 20

<!-- b000321 | prose | pages [14] -->
(a) Flow in 15s (b) Flows in 35s (c) Flows in 40s

<!-- b000322 | caption | pages [14] -->
Figure 6: Evacuation ﬂow

<!-- b000323 | prose | pages [14] -->
6.3 Three types of bottleneck problems

<!-- b000324 | prose | pages [14] -->
There are many bottlenecks in the actual evacuation of the building crowd. We divide them into three categories: (1) bottlenecks due to channel supply and demand imbalances (2) bottlenecks due to uneven distribution of exports (3) single room export bottlenecks.

<!-- b000325 | prose | pages [14] -->
6.3.1 Bottlenecks due to imbalance in channel ﬂow

<!-- b000326 | prose | pages [14] -->
What we can ﬁnd from the ﬂow-time ﬁgure of the exit, shown in Figure 7(a), is that the ﬂow drops occurs at around 10s, 30s and 35s.

<!-- b000327 | prose | pages [14] -->
(a) Exit ﬂow - time graph (b) Flow Margin-time graph

<!-- b000328 | caption | pages [14] -->
Figure 7: Bottleneck phenomenon

<!-- b000329 | prose | pages [14] -->
Next, we reﬁne the reason of the drop in ﬂow, and make the channel Flow Margin-time graph of node 6 as Figure 7(b).

<!-- b000330 | prose | pages [14] -->
Node 6 has two inlet channels and one outlet channel, corresponding to the three curves in the ﬁgure. The Flow Margin is deﬁned as the diﬀerence between the maximum ﬂow of the channel and the actual ﬂow, reﬂecting the remaining capacity of the channel. To minimize evacuation time, the Flow Margin must be minimized. It can be seen from the ﬁgure that the ﬂow margin of node 6 has a rise in 10s and about 42s respectively. The sharp rise in 42s is clearly due to the decline in the total number of people remaining. The reason for the slight increase at 10s is that the sum of the maximum ﬂow of channels 3-6 and 5-6 is less than the maximum ﬂow of channels 6-9 (15+12.1<30), that

<!-- b000331 | furniture | pages [15] -->
Team#1922748

<!-- b000332 | furniture | pages [15] -->
page 13 of 20

<!-- b000333 | prose | pages [15] -->
is, the ﬂow ”unbalance between supply and demand” occurs. Reﬂected in Figure 7(a), this creates a bottleneck in ﬂow at 10s.

<!-- b000334 | prose | pages [15] -->
In order to solve the problem ,we choose to expand the width of the restricted channel while keep the density unchanged to meet the ﬂow supply and demand balance. Figure 7(a) also shows the optimized outlet ﬂow-time diagram. It can be seen that the bottleneck is eliminated ,as well as , evacuation time shortened. The total evacuation time is about 43.2s. (The accuracy is related to the selected time step)

<!-- b000335 | prose | pages [15] -->
6.3.2 Bottlenecks due to uneven distribution of exports

<!-- b000336 | prose | pages [15] -->
As mentioned above, there is a bottleneck at 30s in the exit ﬂow-time chart.

<!-- b000337 | prose | pages [15] -->
Make the remaining number of people in the 2.3.4.5-time chart, as shown in Figure 8.It can be seen that the absolute values of the slopes of nodes 3 and 2 are smaller than those of nodes 4 and 5, and the comparison of 3 to 4 is slower than the similar number of people. 2 to 5 fell more slowly. At around 30-35s, people in node 2, 4, 5 have been evacuated, but 3 has the remaining number, which caused a small decline in export ﬂows. There are two main reasons for the bottleneck: one is the uneven distribution of personnel in diﬀerent rooms, and the other is the uneven distribution of exports. These two reasons together cause the uneven speed of the overall personnel escape (that is, the slope is diﬀerent). The solution is to make the distribution of exports as uniform as possible in the case of similar numbers of people, especially in rooms far from the exit, there should be more outward access.

<!-- b000338 | caption | pages [15] -->
Figure 8: Num of remaining-time graph

<!-- b000339 | prose | pages [15] -->
6.3.3 Single room export bottleneck

<!-- b000340 | prose | pages [15] -->
In addition to the two types of bottlenecks shown in Figure 7(a), there is still a bottleneck problem that is not reﬂected in this situation, that is, the single-room export bottleneck problem.

<!-- b000341 | prose | pages [15] -->
According to Helbing [19], Chunshan Lv [20] Weiguo Song [21] and others, the simulation of the evacuation model is carried out using a cellular automaton and a social force model: in the case of a relatively large population density, It is easy to form an ”arched” blockage at the exit of the room, and the greater the speed expected by the personnel, the more obvious the blockage.

<!-- b000342 | furniture | pages [16] -->
Team#1922748

<!-- b000343 | furniture | pages [16] -->
page 14 of 20

<!-- b000344 | prose | pages [16] -->
In order to solve this bottleneck problem, we can control the evacuation of the expected speed by manual guidance, guidance, etc. to reduce or even eliminate the export blockage. (In fact, we have set the ﬂow velocity of 0.8m/s in the aforementioned model, and have considered the factors of export bottlenecks.) According to research by relevant experts [22], there are some more practical and speciﬁc measures that can eﬀectively prevent The bottleneck, such as setting a cylindrical obstacle, etc., a few meters before the exit.

<!-- b000345 | prose | pages [16] -->
6.4 Adaptive analysis

<!-- b000346 | prose | pages [16] -->
According to the topic requirements, museum managers hope to obtain an adaptive model that can be used to address a wide range of considerations and various types of potential threats.

<!-- b000347 | prose | pages [16] -->
Let’s take a ﬁre accident in a room as an example to show that our model is adaptable. Assuming that room 8 is on ﬁre, it should meet such requirements: First, only leaving is allowed for room 8. Secondly, people in room 8 have to be evacuated as soon as possible. According to our aforementioned algorithm, the above two requirements can be achieved by blocking the entry channel of the node 8 which is shown in Figure9 (c), (d) and lead people evacuate to neighboring rooms just like Figure9 (a), (b).

<!-- b000348 | prose | pages [16] -->
(a) Normal situation in 5s (b) Emergency situation in 5s

<!-- b000349 | prose | pages [16] -->
(c) Normal situation in 15s (d) Emergency situation in 15s

<!-- b000350 | caption | pages [16] -->
Figure 9: Adaptive model schematic

<!-- b000351 | prose | pages [16] -->
According to the emergence of diﬀerent emergencies, the transformation of our model can lead to the corresponding evacuation plan, which is adaptable and can be applied.

<!-- b000352 | furniture | pages [17] -->
Team#1922748

<!-- b000353 | furniture | pages [17] -->
page 15 of 20

<!-- b000354 | prose | pages [17] -->
6.5 Entry of emergency personnel

<!-- b000355 | prose | pages [17] -->
When an accident occurs, emergency personnel is often required to enter the building in time for rescue. In the actual rescue, how to realize the entry of emergency personnel is also an important issue that should be considered in the case of ensuring the rapid evacuation of personnel. We give two options for this: The ﬁrst one is real-time monitoring of channel ﬂow. When the ﬂow of people drops to 60%-70% of the maximum ﬂow, the emergency personnel are allowed to enter in. Second, when the situation is particularly urgent, priority is given to emergency personnel.We choose a shortest path, dedicated to emergency personnel use and close all channels and stairs link to this room in the model. Combined with domestic and foreign rescue cases, our program meets the actual requirements.

<!-- b000356 | prose | pages [17] -->
7

<!-- b000357 | heading | pages [17] -->
Louvre evacuation model

<!-- b000358 | prose | pages [17] -->
7.1 Application of the dynamic node graph in the Louvre

<!-- b000359 | prose | pages [17] -->
As mentioned before, we can use nodes to represent the relatively independent parts of the building. We can call these parts diﬀerent rooms.Therefore, we can divide the Louvre into ﬁve parts, representing the ground (0F), the ﬁrst ﬂoor (1F), the second ﬂoor (2F), the negative ﬁrst ﬂoor (-1F) and the negative second ﬂoor (-2F). These ﬁve ﬂoors can form ﬁve plane dynamic system node maps. The connecting part is the ”channel between layers” formed by the actual stairs.

<!-- b000360 | prose | pages [17] -->
In the actual process of building the model, we simplify each ﬂoor of the Louvre into a node diagram. Figure 10 shows the results of ﬁrst ﬂoor (1F)[23] as an example.

<!-- b000361 | prose | pages [17] -->
(a) Actual 1F (b) Node graph of 1F

<!-- b000362 | caption | pages [17] -->
Figure 10: Louvre node graph

<!-- b000363 | prose | pages [17] -->
After the dynamic node diagram of each layer is established, the layers are connected according to the actual distribution of stairs in the Louvre, as shown in Figure 11.

<!-- b000364 | furniture | pages [18] -->
Team#1922748

<!-- b000365 | furniture | pages [18] -->
page 16 of 20

<!-- b000366 | caption | pages [18] -->
Figure 11: Louvre’s spatial node graph

<!-- b000367 | prose | pages [18] -->
7.2

<!-- b000368 | heading | pages [18] -->
Analysis of the results of the Louvre model

<!-- b000369 | prose | pages [18] -->
7.2.1 Evacuation simulation

<!-- b000370 | prose | pages [18] -->
In the previous analysis of the model results, we have analyzed the evacuation of simple buildings.

<!-- b000371 | prose | pages [18] -->
Now let’s take a look at the evacuation plan for the complex building of the Louvre.

<!-- b000372 | prose | pages [18] -->
(a) Flow in 50s (b) Flow in 120s

<!-- b000373 | prose | pages [18] -->
(c) Flow in 190s (d) Flow in 250s

<!-- b000374 | caption | pages [18] -->
Figure 12: Dynamic ﬂow distribution

<!-- b000375 | prose | pages [18] -->
In our simulation of the actual evacuation of the Louvre, we assumed some assumptions: I. The number of people in the hall is about 7,000; II. All persons are reasonably distributed according to the actual size of each room; III. In the evacuation process, the ﬂow density meets the actual statistical value

<!-- b000376 | furniture | pages [19] -->
Team#1922748

<!-- b000377 | furniture | pages [19] -->
page 17 of 20

<!-- b000378 | prose | pages [19] -->
In Figure 12(a), we can see that the four green lines meet at a point, which is the sink point, indicating the external environment. The number of people on the four green lines connected to it is the ﬂow of the four main exits. In Figure 12, in the same layer, the numbers on the line indicate the ﬂow of people carried by the corridors and other channels in a period of time; the lines between the diﬀerent layers represent the actual stairs, they The numbers above indicate the ﬂow of people carried by the stairs over a period of time.

<!-- b000379 | prose | pages [19] -->
As can be seen from Figure 12, this is a dynamic evacuation process simulation model. From the simulation, we can summarize the following conclusions:

<!-- b000380 | heading | pages [19] -->
I. At the beginning of the evacuation, it is necessary to keep the exit area open;

<!-- b000381 | heading | pages [19] -->
II. In the middle of the evacuation, it is found that the rooms far away from the exit are

<!-- b000382 | prose | pages [19] -->
very congested, so consider opening other exits closer to them;

<!-- b000383 | heading | pages [19] -->
III. In the later stage of evacuation, it can be found that the ﬂow of some channels has been

<!-- b000384 | prose | pages [19] -->
reduced, allowing rescuers to enter the venue in time.

<!-- b000385 | prose | pages [19] -->
7.2.2 Bottleneck analysis

<!-- b000386 | prose | pages [19] -->
It can be seen from Figure 13, the personnel in the hall can basically be evacuated within ﬁve minutes.

<!-- b000387 | caption | pages [19] -->
Figure 13: Export ﬂow-time diagram

<!-- b000388 | caption | pages [19] -->
Figure 14 shows a schematic diagram of the margin of channel ﬂow at each time. The

<!-- b000389 | prose | pages [19] -->
red lines indicate that a channel is fully loaded, which is highly likely to cause an evacuation bottleneck. According to the blue line near the red line (not full load channel), the evacuation route can be re-planned to solve the bottleneck problem.

<!-- b000390 | prose | pages [19] -->
8

<!-- b000391 | heading | pages [19] -->
How to use the model

<!-- b000392 | prose | pages [19] -->
In order to give museum personnel a complete model exploration method, we give the fol- lowing suggestions:

<!-- b000393 | heading | pages [19] -->
I. Based on the details and dimensions of the museum, perfect the model and establish the

<!-- b000394 | prose | pages [19] -->
most accurate spatial node map;

<!-- b000395 | heading | pages [19] -->
II. Set up a density detector at each key part of the hall to detect the density in real time

<!-- b000396 | prose | pages [19] -->
to ensure the accuracy of the data;

<!-- b000397 | heading | pages [19] -->
III. Once the accident occurs, the model is quickly used for evacuation simulation. Because

<!-- b000398 | furniture | pages [20] -->
Team#1922748

<!-- b000399 | furniture | pages [20] -->
page 18 of 20

<!-- b000400 | prose | pages [20] -->
(a) Margin in 50s (b) Margin in 120s

<!-- b000401 | prose | pages [20] -->
(c) Margin in 190s (d) Margin in 250s

<!-- b000402 | caption | pages [20] -->
Figure 14: Channel margin diagram

<!-- b000403 | prose | pages [20] -->
the calculation speed of this model is much faster than the actual evacuation speed, museum personnel can ﬁnd the optimal evacuation route in advance and give timely instructions; (recommended to install clear and conspicuous indicator lights in the evacuation section)

<!-- b000404 | heading | pages [20] -->
IV. Because the model is adaptable, museum personnel can adjust the model based on actual

<!-- b000405 | prose | pages [20] -->
accidents. For example, if a room is on ﬁre, the route can be re-planned according to the model calculation results to ensure that people can get real-time and optimal solutions;

<!-- b000406 | heading | pages [20] -->
V. Through the simulation of the model, the bottleneck in the evacuation process can be

<!-- b000407 | prose | pages [20] -->
quickly identiﬁed, so that the extra exits can be arranged to make the export distribution most reasonable;

<!-- b000408 | heading | pages [20] -->
VI. Through dynamic simulations, museum personnel can ﬁnd the most appropriate route

<!-- b000409 | prose | pages [20] -->
and time for rescuers to enter.

<!-- b000410 | prose | pages [20] -->
9

<!-- b000411 | heading | pages [20] -->
Conclusion

<!-- b000412 | prose | pages [20] -->
9.1

<!-- b000413 | heading | pages [20] -->
Sensitivity analysis

<!-- b000414 | prose | pages [20] -->
In the actual evacuation process, due to some objective reasons, such as the error of the density detector, the model will produce a certain deviation in the process of evacuation plan simulation. To determine the eﬀect of these deviations on the ﬁnal result, we performed a sensitivity analysis. Set the parameter to the ﬂow density so that it has a 5% error. The results produced are shown in Figure 15.

<!-- b000415 | prose | pages [20] -->
It can be seen that the model can guarantee the accuracy of the simulation within a certain

<!-- b000416 | furniture | pages [21] -->
Team#1922748

<!-- b000417 | furniture | pages [21] -->
page 19 of 20

<!-- b000418 | prose | pages [21] -->
(a) Veriﬁcation model (b) Louvre model

<!-- b000419 | caption | pages [21] -->
Figure 15: Sensitivity analysis diagram

<!-- b000420 | prose | pages [21] -->
error range. The museum only needs to ensure that the error of the ﬂow density detection device is small to get accurate results. In addition, in the actual evacuation process, the ﬂow density of each part is time-varying, so the accuracy of the current event detection device is more needed. Since the model can respond to the changing results quickly, to a certain extent, the model can eliminate the impact of errors through iterative updating. In this way, the museum can ﬁnd the best evacuation plan more accurately.

<!-- b000421 | prose | pages [21] -->
9.2

<!-- b000422 | heading | pages [21] -->
The model

<!-- b000423 | prose | pages [21] -->
9.2.1

<!-- b000424 | heading | pages [21] -->
Strength

<!-- b000425 | prose | pages [21] -->
The model has great generalization because it does not consider any special circumstances but the general situation. And the model fully measures the structure inside the building, and the calculation result is that the route plan is more intuitive. In addition, when there is a need to open or close a channel, room or exit, it can be easily modiﬁed in the model. This also reﬂects the excellent adaptability of the model.

<!-- b000426 | prose | pages [21] -->
9.2.2

<!-- b000427 | heading | pages [21] -->
Weaknesses

<!-- b000428 | prose | pages [21] -->
While using the model, in order to fully exert its dynamic capabilities, it may be necessary to monitor the ﬂow density of the channel and the exit. Thus there are certain limitations.

<!-- b000429 | prose | pages [21] -->
9.3

<!-- b000430 | heading | pages [21] -->
The algorithm

<!-- b000431 | prose | pages [21] -->
9.3.1

<!-- b000432 | heading | pages [21] -->
Strength

<!-- b000433 | prose | pages [21] -->
I.The eﬀects of individual interactions and the physical parameters of speciﬁc channels are taken into account in the calculation of the maximum ﬂow allowed in channels.

<!-- b000434 | prose | pages [21] -->
In the application of the N&M model and the SES model, real-time human ﬂow density is adopted, and therefore, it has certain dynamics. II.Since the planning is performed from the perspective of the system, the algorithm is

<!-- b000435 | furniture | pages [22] -->
Team#1922748

<!-- b000436 | furniture | pages [22] -->
page 20 of 20

<!-- b000437 | prose | pages [22] -->
extremely fast compared with other algorithms, such as a cellular automaton-based planning algorithm. This allows a number of possible scenarios to be tried by modifying the model parameters in response to an unexpected situation. III.Since the ﬂow and the margin at any moment in the model can be obtained directly from the algorithm, the bottleneck problem that may occur in the planning scheme and the model can be found directly through the visualization of the ﬂow matrix and the margin matrix.

<!-- b000438 | prose | pages [22] -->
9.3.2

<!-- b000439 | heading | pages [22] -->
Weaknesses

<!-- b000440 | prose | pages [22] -->
Firstly, the Ford-Fulkerson algorithm has certain limitations. When there is a special case for each value in the graph, the algorithm will loop indeﬁnitely. However, considering that we apply the algorithm to the human ﬂow problem, the probability of occurrence in a special case is almost zero.

<!-- b000441 | prose | pages [22] -->
Secondly, the calculation result will occupy a large amount of storage space with the increase of precision. However, in general buildings, the required storage space is still within acceptable limits.

<!-- b000442 | heading | pages [23] -->
References

<!-- b000443 | references | pages [23] -->
[1]C. F. Wakim, S. Capperon and J. Oksman, A Markovian model of pedestrian behav-

<!-- b000444 | references | pages [23] -->
ior[C].2004 IEEE International Conference on Systems, Man and Cybernetics .IEEE , 2004(4):

<!-- b000445 | references | pages [23] -->
4028-4033.

<!-- b000446 | references | pages [23] -->
[2]Dirk Helbing,Pter Molnr.Social force model for pedestrian dynamics[J].Physical review, E.

<!-- b000447 | references | pages [23] -->
Statistical physics, plasmas, ﬂuids, and related interdisciplinary topics,1995,51(5):4282-4286.

<!-- b000448 | references | pages [23] -->
[3]PREDTECHENSKII V M, MILINSKI A I.Planning for foot traﬃc ﬂow in building[M].

<!-- b000449 | references | pages [23] -->
Stroiizdat Publishers, Moscow,1969

<!-- b000450 | references | pages [23] -->
[4]PHILIT J D, CRAIG J D, RICHARD L R, et al.SFPEHandbook of Fire Protection En-

<!-- b000451 | references | pages [23] -->
gineering[ S] .Published by National ﬁre protection association , 1995

<!-- b000452 | references | pages [23] -->
[5]Zhong, Wei & Tu, Rui & Yang, Jian-peng & Tianshui, Liang.

<!-- b000453 | references | pages [23] -->
(2013).

<!-- b000454 | references | pages [23] -->
Simulation of

<!-- b000455 | references | pages [23] -->
Evacuation Process in a Supermarket with Cellular Automata. Procedia Engineering. 52.

<!-- b000456 | references | pages [23] -->
687-692. 10.1016/j.proeng.2013.02.207.

<!-- b000457 | references | pages [23] -->
[6]Li Junmei, Hu Cheng, Li Yanfeng, et al. Study on the eﬀect of population density of

<!-- b000458 | references | pages [23] -->
diﬀerent types of evacuation channels on walking speed[J]. Architecture Science, 2014, 30(8):

<!-- b000459 | references | pages [23] -->
122-129. DOI: 10.13614/j.cnki. 11-1962/tu.2014.08.023

<!-- b000460 | references | pages [23] -->
[7]Lee, Eric Wai Ming,Shi, Meng,Ma, Yi.A novel grid-based mesoscopic model for evacuation

<!-- b000461 | references | pages [23] -->
dynamics[J].Physica, A. Statistical mechanics and its applications,2018,497:198-210.

<!-- b000462 | references | pages [23] -->
[8]Lu Junan, Fang Zheng, Lu Zhaoming, et al. Mathematical model of evacuation speed

<!-- b000463 | references | pages [23] -->
of building personnel[J]. Journal of Wuhan University (Engineering Science), 2002, 35(2):

<!-- b000464 | references | pages [23] -->
66-70. DOI:10.3969/j.issn .1671-8844.2002.02.016.

<!-- b000465 | references | pages [23] -->
[9]Jin Nanjiang, Mao Zhanli. Research on evacuation path model of multi-story buildings in

<!-- b000466 | references | pages [23] -->
ﬁre environment [J]. Industrial Safety and Environmental Protection, 2018, 44 (4): 1-4.

<!-- b000467 | references | pages [23] -->
[10]Jia Yu. Research on the law of evacuation behavior and speed model of the intersection

<!-- b000468 | references | pages [23] -->
of people in the middle school teaching building [D]. Southwest Jiaotong University, 2016.

<!-- b000469 | references | pages [23] -->
[11]C. Y. Wang and W. G. Weng, Study on evacuation characteristics in an ultra high-rise

<!-- b000470 | references | pages [23] -->
building with social force model,17th International IEEE Conference on Intelligent Trans-

<!-- b000471 | references | pages [23] -->
portation Systems (ITSC), Qingdao, 2014, pp. 566-571.

<!-- b000472 | references | pages [23] -->
[12]ROYTMAN, M Y.Principles of ﬁre safety standards for building construction[ M] .Amerind

<!-- b000473 | references | pages [23] -->
publishing Co.New Delhi , 1975 .

<!-- b000474 | references | pages [23] -->
[13]Ando KOta HOki T Forecasting the ﬂow of people ( in Japanese)J Railway Research

<!-- b000475 | references | pages [23] -->
Review198845(8): 8-14

<!-- b000476 | references | pages [24] -->
[14]H. Wang, Q. Chen, J. Yan, Z. Yuan and D. Liang, Emergency Guidance Evacuation in

<!-- b000477 | references | pages [24] -->
Fire Scene Based on Pathﬁnder,2014 7th International Conference on Intelligent Computa-

<!-- b000478 | references | pages [24] -->
tion Technology and Automation, Changsha, 2014, pp. 226-230.

<!-- b000479 | references | pages [24] -->
[15]Zhang Yan, Ren Han. Ford-Fulkerson algorithm and short circle in embedded graph[J].

<!-- b000480 | references | pages [24] -->
Chinese Journal of Applied Mathematics, 2008(05): 780-785.

<!-- b000481 | references | pages [24] -->
[16]Xia Xiaomei, Zhou Qianmin.NoC Path Assignment Based on Oriented Ford-Fulkerson

<!-- b000482 | references | pages [24] -->
Algorithm[J].Journal of Hefei University of Technology(Natural Science),2006(03):316-321.

<!-- b000483 | references | pages [24] -->
[17]Elvin J Moore,Wisut Kichainukon,Utomporn Phalavonk.Maximum ﬂow in road networks

<!-- b000484 | references | pages [24] -->
with speed-dependent capacities application to Bangkok traﬃc[J].(4):489.

<!-- b000485 | references | pages [24] -->
[18]Uri Zwick,The smallest networks on which the Ford-Fulkerson maximum ﬂow procedure

<!-- b000486 | references | pages [24] -->
may fail to terminate,Theoretical Computer Science,Volume 148, Issue 1,1995,Pages 165-

<!-- b000487 | references | pages [24] -->
170,ISSN 0304-3975,

<!-- b000488 | references | pages [24] -->
[19]Helbing D, Farkas I, Vicsek T. Simulating dynamical features of escape panic [J]. Nature,

<!-- b000489 | references | pages [24] -->
2000, 407: 487 - 490.

<!-- b000490 | references | pages [24] -->
[20]Lv Chunshan, Weng Wenguo, Yang Rui, et al. Personnel evacuation model based on

<!-- b000491 | references | pages [24] -->
motion mode and cellular automata in ﬁre environment[J]. Journal of Tsinghua Universi-

<!-- b000492 | references | pages [24] -->
ty(Science and Technology), 2007, 47(12): 2163-2167.

<!-- b000493 | references | pages [24] -->
[21]Song Weiguo, Yu Yanfei, Fan Weicheng, et al. A kind of evacuation of cellular automata

<!-- b000494 | references | pages [24] -->
model considering friction and repulsion[J]. Science in China, Series E, 2005, 35(7): 725-736.

<!-- b000495 | references | pages [24] -->
10.3969/j.issn.1674-7259.2005.07.006.

<!-- b000496 | references | pages [24] -->
[22]Wei Chengjie. Research on pedestrian motion modeling and evacuation based on Markov

<!-- b000497 | references | pages [24] -->
model [D]. Beijing Jiaotong University, 2018.

<!-- b000498 | references | pages [24] -->
[23]Interactive Floor Plans,Retrieved from https://www.louvre.fr/en/plan

<!-- b000499 | heading | pages [25] -->
Appendix

<!-- b000500 | prose | pages [25] -->
Other ﬁgures

<!-- b000501 | prose | pages [25] -->
Figure A-1: Flow diagrams of algorithm

<!-- b000502 | prose | pages [26] -->
(a) Real -2F (b) Simulation of -2F

<!-- b000503 | prose | pages [26] -->
(c) Real -1F (d) Simulation of -1F

<!-- b000504 | prose | pages [26] -->
(e) Real 0F (f) Simulation of 0F

<!-- b000505 | prose | pages [26] -->
Figure A-2: -2F ∼0F

<!-- b000506 | prose | pages [27] -->
(a) Real 1F (b) Simulation of 1F

<!-- b000507 | prose | pages [27] -->
(c) Real 2F (d) Simulation of 2F

<!-- b000508 | prose | pages [27] -->
Figure A-3: 1F ∼2F

<!-- b000509 | prose | pages [27] -->
control procedures

<!-- b000510 | prose | pages [27] -->
BFS

<!-- b000511 | prose | pages [27] -->
function [ out, Parent ] = BFSGraph, start, End, parent, ROW visited = zeros(1, ROW); queue = []; queue = [queue, start]; visited(start) = 1; while queue u = queue(1); queue(1) = []; for i = 1:ROW if (visited(i)==0)&&(Graph(u, i)¿0) queue = [queue, i]; visited(i) = 1; parent(i) = u; end

<!-- b000512 | prose | pages [28] -->
end end out = visited(End); Parent = parent; end

<!-- b000513 | prose | pages [28] -->
Ford fulkerson

<!-- b000514 | prose | pages [28] -->
function [max ﬂow, Remain] = Ford fulkerson(Graph, s, e, ROW) NUM INF = inf; parent = zeros(1, ROW); parent(:) = -1; max ﬂow = 0; start = s; End = e; [out, parent] = BFS (Graph, start, End, parent, ROW); while out path ﬂow = NUM INF; start = End; while start = s path ﬂow = min(path ﬂow, Graph(parent(1, start), start)); start = parent(1, start); end max ﬂow = max ﬂow + path ﬂow; v = End; while v = start u = parent(1, v); Graph(u, v) = Graph(u, v) - path ﬂow; Graph(v, u) = Graph(v, u) + path ﬂow; v = parent(1, v); end [out, parent] = BFS(Graph, start, End, parent, ROW); end Remain = Graph; end

<!-- b000515 | prose | pages [28] -->
Channel

<!-- b000516 | prose | pages [28] -->
function [Graph Channel] = Channel(Channel width, Channel density, ac) v = 1 - 0.266.*1.40.*Channel density; Graph Channel = v.*ac.*Channel width.*Channel density; end

<!-- b000517 | prose | pages [29] -->
Stairs

<!-- b000518 | prose | pages [29] -->
function [Graph Stairs] = Stairs(Stairs width, Stairs density, ac) v = 1 - 0.266.*1.08.*Stairs density; Graph Stairs = v.*ac.*Stairs width.*Stairs density; end

<!-- b000519 | prose | pages [29] -->
Main

<!-- b000520 | prose | pages [29] -->
function[Max ﬂow, Flow, Remain, Time] = Main(G,ac)%Stairs width, Stairs density, Chan- nel width, Channel density, Graph enter, Graph exit, ac)%, Emergency) Graph = G;%Channel(Channel width, Channel density, ac) + Stairs(Stairs width, Stairs density, ac) + Graph enter + (Graph exit./5.*ac); ROW = length(Graph); Graph(2:ROW,:) = Graph(2:ROW,:).*ac./5; Total = sum(Graph(1,:)) % Emergency situation % Only leaving is allowed % Use this section by uncommenting all about this %{ if ∼isempty(Emergency) Graph(2:ROW,Emergency) = 0; Ge = Graph; t = []; for i = 1:length(Emergency) v = sum(Graph(Emergency(i),:),2); t = [t, ac*Graph(1,Emergency(i))/v]; end Graph(1, Emergency) = 0; Graph(Emergency, :) = 0; end %} i = 0; Max ﬂow = []; Flow = zeros(ROW, ROW, 1); Remain = zeros(ROW, ROW, 1); while Total¿0.5 i = i+1; mf = 0; %{ if ∼isempty(Emergency) for j = 1:length(Emergency) if i*ac-t(j)¡ac Graph(1,:) = Graph(1,:) + Ge(Emergency(j),:).*(min(t(j),i*ac)-i*ac+ac)./ac;

<!-- b000521 | prose | pages [30] -->
mf = mf+Graph(1,ROW); Graph(1,ROW) = 0; end end end %} Copy = Graph; [max ﬂow, Copy] = Ford fulkerson(Copy, 1, ROW, ROW); Remain(:, :, i) = Copy; Temp = Graph - Copy; Temp(Temp¡0) = 0; %{ if isempty(Emergency) for j = 1:length(Emergency) if i*ac-t(j)¡ac Temp(Emergency(j),:) = Temp(Emergency(j),:) + Ge(Emergency(j),:); end end end %} Flow(:, :, i) = Temp; max ﬂow = max ﬂow + mf; Max ﬂow = [Max ﬂow, max ﬂow]; Total = Total - max ﬂow Graph(1, :) = Graph(1, :) - Temp(1, :); end Time = i*ac; end
