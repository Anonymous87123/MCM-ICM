Summary

The object of our model is to provide an emergency evacuation for the Louvre. In the meantime, this model can also identify potential bottlenecks and has certain adaptability. However, complex building structures and the interaction among people makes the problem much harder. In this paper, we present a system dynamic planning model. And both the systematicness during the planning and the individuality of the visitors are considered in our model.

The first part of our model is to solve the influence of individual factors. The effect will be ultimately reflected in the flow speed of the crowd. In this way, while calculating the flow speed of the crowd, we adopt N&M model and Stable Evacuation Speed model (SES Model) to deal with different situation.

The second part is to visualize the building into a graph. Then simplify the problem from muti-to-muti plan to single-to-single plan through adding two virtual nodes. This step makes the following solution much easier.

The third part of the model is the systematic planning of evacuation route. Here a new algorithm with Ford-Fulkerson algorithm as the core, and considering the previous two parts of the model are proposed. In this way, the algorithm can carry out route planning from the perspective of system, and fully consider the micro factors.

Then, a simulated building is built to verify the validity of the model. The model obtains the result within 0.457s with a scale of 770 people. Besides, to a certain extent, the result matches practical case. In addition, it is able to evacuate the crowd from the dangerous room with the fastest speed in the emergency treatment, which shows excellent performance.

Finally, we implement this model to the Louvre. It cost 36.15s to get the result with a scale of 6700 people and accuracy of 0.1s. The total evacuation cost 288.7s.  After the flow and margin matrices are visualized, it clearly shows the whole evacuation process and potential bottlenecks. Also, we present a series of suggestions for practical use of the model.

1 Introduction

1.1 Background

Today, museums, libraries, and exhibition halls around the world are paying more attention to the safe evacuation of venues, and are looking for suitable emergency evacuation methods. Therefore, it is vital to establish a widely used and adaptable emergency evacuation model. In recent years, many scholars have put forward their own opinions in this ﬁeld, and established various models. Among them, Wakim proposed a Markov pedestrian model based on the analysis of pedestrian dynamic behavior and Markov chain[1]; Helbing, a German scholar, proposed a social force model that can organize a series of self-organizing phenomena in the process of current human movement[2]. The above models are very suitable for the study of individual movement in emergency evacuation. And they’re very accurate for the bottleneck problem, which means situations when movement is dramatically slowed or even stopped. However, for a large, multi-story venue like the Louvre, an evacuation model with a general view from the whole to the local is needed. Therefore, based on the establishment of the spatial simulation maximum ﬂow node graph model, we use the maximum ﬂow method to explore how to choose the most appropriate evacuation scheme in case of emergency.

1.2 Restatement of problems

The Louvre is one of the largest and most visited art museums in the world. Due to the diversity of visitors and the complex structure of the building, it poses a great challenge to safe evacuation. We need to develop an emergency evacuation model to provide museum staﬀwith options for evacuation options in diﬀerent situations, and to popularize other large crowded structures.

The established model needs to accomplish the following objectives:

I.Give instructions to allow museum personnel to explore a range of options to evacuate visitors from the museum;

II.Identify potential bottlenecks that may limit export movement;

III.Allow emergency personnel to enter buildings as soon as possible;

IV.The models can be used to solve a wide range of considerations and various types of potential threats;

V.Extend to other large crowded structures.

At the same time, the model should consider several implicit objectives:

I.How to evacuate when the total number is diﬀerent;

II.When there are individual inﬂuence such as small group or diﬀerent language speakers, how to arrange evacuation plan;

III.When and how any additional exits.

The mind map (Figure 1) shows the issues that need to be addressed.

1.3 Overview of our work

In our research program, the ﬁrst step is the microscopic part: to ﬁnd out the law of human ﬂow speed based on the existing crowd movement model, including ”staircase model”, ”corridor model” and ”room exit model”. The second step is to establish a spatial node graph for the venue with the idea of graph theory. And use nodes to represent various parts of the venue, such as rooms and halls, lines to indicate the stairs, corridors, etc. connected to each part. The third step is the macro part: combined with the idea of the Ford- Fulkerson algorithm, we set the optimization goal as the speed of all exits ﬂow at each moment is the maximum that can be achieved, and dynamically observe the evacuation and make adjustments by iterative method. The ﬁnal step is to promote the model so that rescuers can get in time and make the model able to cope with other potential threats.

The ﬂow chart (Figure 2) illustrate the above ideas in a more visual way.

2 Assumptions

1. The guiding signs and notiﬁcations of the venues are clear enough for emergency evacua- tion. 2. While evacuating, the vast majority of people are rational enough to follow the signs and notiﬁcations and complete the escape. 3. No additional accidents such as stampedes occur during evacuation. 4. When evacuating, the crowd will not evacuate in opposite directions. 5. The doors of each main room are of moderate size and width, which will not cause over- crowding.

3 Symbols and Notation

symbol descriptions units v Evacuation Speed of Flow m/s m2/people Sind Average personal area m2 Stotal Total area of human ﬂow \ D Crowd congestion \ k Speed coeﬃcient people/m2 ρ Population density q Human ﬂow people/s \ G Overall matrix of the model

Note: Symbols not mentioned in the table will be explained if they appear below.

4 Microscopic model:

personnel evacuation speed model

4.1 A possible model of diﬀerent road segments (N&M model)

According to the related research of Predtechenski and Milinskii [3], the average evacuation speed is a function of the ﬂow density. Besides,they used the observation data of the aisle and stairs to ﬁt the relationship curve. Unfortunately, this is a complex nonlinear relationship, that is not suitable for a wide range of applications.

After that, Nelson and Mowrer et al[4]. simpliﬁed the relationship between velocity and ﬂow density to a linear relationship, and selected diﬀerent linear coeﬃcients for diﬀerent e- vacuation channels. When 0.54 persons/m2 ≤D ≤3.8 persons/m2, the relationship between the moving speed and the ﬂow density is as follows.

v = k −0.266kD (1) Where, we deﬁne D as the crowd congestion degree, that is, the ratio of the actual area of the human body in the crowd to the total area of the ﬂow of people, which reﬂects the overall crowding degree of the crowd. It can be derived from D = NSind Stotal , Where,Sind refers to the average personal occupation area, Stotal refers to the total area of the ﬂow of people. And k in the formula (1) can be determined from Table 2[5].

Evacuation Channel Type k Stairs Tread/mm Riser/mm 190 254 1.00 Stairs 178 279 1.08 165 305 1.16 165 330 1.23 Corridor,Aisle,Ramp, Doorway 1.40

Corresponding to the above table, k is taken as 1 and 1.4 respectively to obtain the ”staircase model”and ”corridor model”.

In summary, N&M Model[6] considers the relationship between evacuation speed and ﬂow density[7], and gives diﬀerent models such as the staircase model and corridor model for diﬀerent road sections, but it is not suitable for the situation where the ﬂow density is relatively large, such as the narrow exit of the room. So we try to ﬁnd a better model to replace it.

4.2 A possible model considering the degree of congestion

4.2.1 Crowding in two directions

According to research by Lu Junan and others, the speed of personnel escape is aﬀected by Front- Crowding and Side-Crowding.[8] Front-Crowding: In an escaped group, taking the exit as the coordinate origin, suppose the location of the j-th person is at xj, the speed of him is dxj dt . So the distance from the previous j −1-th person is |xj −xj−1|, which is recorded as A, also, the relative velocity is dxj dt −dxj−1 dt , which is recorded as B. Then the forward damping force caused by crowding before and after is proportional to B A.

Side-Crowding: Here we use a frictional damping force to describe the level of Side- Crowding[9]. Note that Side-Crowding is generally suitable when the crowd density is par- ticularly large, and when the population density is small, it has little eﬀect.

4.2.2 Escape velocity dynamic equation

According to Newton’s second law, we have obtained the following escape velocity dynamics equation.

d2xj dt2 = α(dxj dt −dxj−1 −mj )/ |xj −xj−1| + fj (2) dt Where j = 2 N, which constitutes a system of equations with N −1 equations.

4.2.3 Stable evacuation speed model (SES Model)

Performing integration of the above formula,we get

dxj dt =λjLn (xj−1 (t) −xj (t)) −Fj + cj (3) mj In the formula, Fj is the integral term of fj and cj is a constant term.

Let each person occupy a square with an area of LL,Set the front interval as L + d1, the side interval is L + d2.

1 1 Then front density ρ1 = L+d1, side density ρ2 = L+d2.

Evacuation speed

v(ρ1, ρ2) = dxj (4) dt When v(ρ1, ρ2) = 0, ρ1=ρ1m, ρ2 = ρ2m. ρ1m and ρ2m represent front and side maximum density respectively. Then use the expression containing ρ1mρ2m to indicate cj. Substituting a into equation (1), we get { ρ1 −k(ρ2−ρ2m) λjLnρ1m (ρic < ρi ≤ρim, i = 1, 2) mj vj(ρ1, ρ2) = (5) (ρi ≤ρic, i = 1, 2) vm

When the density is small, the velocity of the human ﬂow is not aﬀected by it, and the critical density does not aﬀect the velocity[10].

Considering other factors such as personnel characteristics, the degree of inﬂuence before and after congestion is diﬀerent, we attain

+ β(ρ2m −ρ2) vj(ρ1, ρ2) = vm (αLn ρ1m/ρ1 + γ) (6) ρ2m −ρ2c ρ1m/ρ1c where, ρ = ρ1ρ2=D, ρ1c and ρ2c are respectively the critical densities of two directions. α, β, γ is corresponding weight of each aspect.

The above is the evacuation escape speed model, also known as the SES Model.

It is analyzed that the above model is a generalized model. When the ﬂow density is large, neither of α, β, γ is zero. When the ﬂow density gets smaller, it can be considered to be mainly aﬀected by Front-Crowding; when the ﬂow density is small enough, only the impact of personnel characteristics can be considered. At this time, the population structure is relatively uniform under normal circumstances, the characteristics of the personnel should be consistent, and v is a certain value[11]. Here ia an example to implement this model.

According to the ﬁre safety principle data prepared by M.Y.Roytman et al.[12], the adult body thickness in the front and rear direction is about 0.32 m, and the body width in both directions is 0.5 m.Considering that the contact between the human body is the highest density, it can be considered that the maximum density ρ1m and ρ2m in the front and side directions are 3 persons/m and 2 persons/m, respectively. According to the research data of Ando et al.[13], when distance between the human body lines is about 0.75 m. According to this, the critical density ρ1c and ρ2c of the front direction and the side direction are about 0.89 persons/m and 1.33 persons/m, respectively. Substituting the above ρ1m, ρ2m, ρ1c and ρ2c into the model, we obtain:

A = 1.32 −0.82Ln(ρ) (7) B = 3.0 −0.76ρ

vj(ρ) = vm (αA + βB + γ) (8) The SES model considers the combined eﬀects of factors such as Front-Crowding,Side- Crowding and other personnel characteristics on evacuation speed during evacuation, and can comprehensively reﬂect the inﬂuencing factors of evacuation speed[14]. The only downside is that due to the uncertainty and ambiguity of the characteristics of the personnel, the eﬀect of this part on the whole cannot be well described.

5 Construction of the graph

5.1 Description of the diagram

Graphs are one of the most powerful frameworks in data structure and algorithmics. Graphs can be used to represent almost any type of structure or system. In this problem, the Louvre is a complex space building structure. To explore its personnel evacuation plan, the method of constructing a node graph can be adopted. To simplify the calculation, we added two hypothetical nodes 1 and 9.

For the sake of convenience, we can use the schematic shown in Figure 3 to represent the idea of a node graph. In Figure 3, we imagine a building with six rooms, where the numbers 2 to 7 represent these rooms. The green line segments indicate the relationship between the rooms, where the solid lines indicate the corridors, and the dotted lines indicate that there is a staircase between the connections of the rooms.

It can be seen that in Figure 3, the green box shows the entire structure of the building. If we use the maximum ﬂow method to calculate the node graph on this basis, we will ﬁnd that this is a ”multi-target to multi-target” problem, that is, corresponding to evacuation from multiple rooms to multiple exits. Although the node structure diagram in the green frame is very intuitive, such multi-objective planning brings a lot of trouble to the calculation. In addition, the Louvre itself is a large and complex space building, and the planning of the evacuation plan will be very complicated and diﬃcult to calculate.

So, we added two special nodes, which are represented by the number 9 and the number 1 in Figure 3.

Node 9 is called ”sink point” and represents the external environment. Its black line with the numbers 6, 7, and 8 indicates the three exits of the building. Node 1 is called the source point and does not have practical meaning. However, the number (not shown in Figure 3) on the line connecting it to each room indicates the number of people remaining in the room at a certain moment. It is worth noting that when the problem is solved later, all the connections will have numbers, and their meanings will be diﬀerent, which will be explained in the later process.

The addition of two special nodes makes the multi-objective programming problem that is complicated and diﬃcult to calculate become a simple and easy to calculate single-objective programming problem. The function of node 1 is to represent the remaining number truly and accurately. The function of node 9 is to express the ﬂow of people leaving the building from the exit. This creates a new ”single goal to single goal” issue. This result corresponds to the relationship between the total number of people remaining in all rooms and the ﬂow of people leaving all exits. The simpliﬁcation of the goal brings great convenience to the optimization of the algorithm.

In addition, adding two virtual nodes has other beneﬁts that will be explained in the theory of algorithm in the next section.

5.2 Matrix model

After the model of the graph is established, all we need to do is to incorporate the numerical calculations on this basis. In order to clearly show the variation of human ﬂow during the simulated evacuation process and to see the optimal evacuation route planning, we can integrate various data with the help of the matrix.

In this model, the data needed to simulate the evacuation law are as follows:

I. The number of people in each room at any time of evacuation. We use the number of source points connected to each room to represent them.

II. During the evacuation process, the number of people passing between adjacent parts

(rooms) during a period of time, that is, the ﬂow of people carried by corridors or stairs during a period of time. We use numbers on the connecting lines between rooms to represent them.

III. In the process of evacuation, the number of people evacuated from each exit at any time, in other words, the ﬂow of the exit. They are represented by numbers on the connecting line between the outlet and the outside (sink point).

Assuming that a building is divided into n parts, we can interpret it as n rooms, then we build a model with n nodes. At the same time, we can establish a matrix of n × n, in which the elements represent the connection between nodes. Since this n-order matrix can only represent the exchange of people between rooms in the building, and can not reﬂect the number of people remaining in the room or evacuating the building, we extend this n-order matrix to a circle and turn it into a (n + 2) × (n + 2) matrix, as shown in Figure 4.

The ﬁnal n + 2 matrix is composed of several parts, which can establish their respective matrices.

5.2.1

”corridor model” Cq and ”staircase model” Sq

Firstly, the ”corridor model” channel traﬃc matrix Cq satisﬁes the following set of equations:

 ci,j = v = k −0.266kD  ci,j = cj,i (9)  ci,i = 0 { 2 ≤i ≤n + 1 Among them, 2 ≤j ≤n + 1 . The other elements are all 0. Ci,j represents the ﬂow of people through the channel over a period of time. This value is calculated by the channel model combined with the density of the ﬂow and the moving speed. Ci,j = Cj,i indicates that the maximum velocity in both directions on the channel is equal. From the matrix point of view, this shows that the human traﬃc matrix is a symmetrical matrix, and the diagonal line is all zero because it has no practical meaning. The meaning of Ci,n+2 = 0 is that the channel model only expresses the interconnection between the various parts of the building, but does not express the relationship between the exit and the outside world. The last column of the total matrix represents the ﬂow of people at the exit of the building. Therefore, the last column of the traﬃc matrix is 0. The matrix is in the following form:

    · · · · · · 0 c1,2 c1,n+2 = 0 0 s1,2 s1,n+2 = 0 ... ... ... ...  , Sq=   · · · · · · c2,1 s2,1 Cq= (10) ... ... ... ... ... ... · · · · · · · · · · · · · · · · · · cn+2,1 0 sn+2,1 0

Then the ”staircase model” channel traﬃc matrix Sq. It diﬀers from the ”corridor model” channel traﬃc matrix in that, over a period of time, the calculation method of the traﬃc through the corridor is diﬀerent. It uses the formula of the staircase model:

si,j = vj(ρ) = vm (αA + βB + γ) (11)

5.2.2 ”initial matrix” En and ”export matrix” Ex

Next, the initial matrix En. It represents the number of people in each room at the initial time of evacuation. Finally, the export matrix Ex. It represents the number of people evacuated from each exit during the evacuation process, i.e. the exit ﬂow. It diﬀers from the initial matrix En in that it only has the last column which is not zero. En and Ex satisfy the following equation:

{ en1,j = tj { exi,n+2 = Tj eni,j = 0, (2 ≤i ≤n + 2) , (12) exi,j = 0, (1 ≤j ≤n + 1) The tj is the number that the source point connects with each room at any time. Tj is the number on the connection line between the exit and the outside world (the sink point). Since the initial matrix only represents the remaining number of people in the internal room, it is independent of the channel, so the number of all rows except the ﬁrst row is 0. The matrices are in the following form:

    · · · 0 0 0 · · · 0 en1,2 en1,n−1 0 ...   · · · 0 ex2,n+2 ...  , Ex = 0 · · · 0 0 ... ... ... En = (13) ... ... ... · · · ... · · · · · · 0 0 exn−1,n+2 0 · · · · · · 0 0 · · · 0 0 0

The four matrices ultimately form the overall matrix G, visually displayed in Figure 4:

G = Cq + Sq + En + Ex (14)

5.3 Dynamic system planning algorithm

5.3.1 Introducing Ford-Fulkerson algorithm

In the above we have transformed the multi-nodes to multi-nodes model of the building into a single-node to single-node model. In this model, the number of people ﬂowing out of the source at any time should be equal to the number of people entering the sink point. Therefore, in the process of escape, the number of people who escaped is the number of people who go from the source to the sink point. In order to get the maximum of escape speed, we need to make full use of the channel resources in the building at any time to maximize the escape rate. In the established model, the problem is equivalent to obtaining the maximum ﬂow from the source to the sink at any time. For such problems, we can apply the Ford-Fulkerson algorithm and make appropriate corrections. The algorithm is described in detail below[15].

Before describing the algorithm, we need to further clarify the meaning of each edge in the model. there are three kinds of nodes, source points, sink points, and room points in the model. The value on the line connecting the source point to the room node indicates the initial number of rooms in the corresponding room. The connection between the room nodes indicates the connection between the rooms, and the value indicates the maximum ﬂow allowed by the channel. The connection between the sink point and the exit room nodes indicates the connection between the exit and the exterior of the building, and its value indicates the maximum passenger ﬂow allowed by the exit.

The original Ford-Fulkerson algorithm is an iterative algorithm. In each iteration, the value of the stream is increased by looking for an ”augment path”[16]. The augmented path can be seen as a path from the source point to the sink point, and more streams can be added along this path. Iterating until the augmented path can no longer be found, at least one of the paths from the source point to the sink point must be full (ie, the size of the edge stream is equal to the size of the edge). The resulting stream at this point is the maximum ﬂow in this case, which can be proved by the maximum ﬂow minimum cut theorem. And we will not prove this here.

5.3.2 Application of Ford-Fulkerson algorithm

Since the model we built is not a traditional single-node to single-node mode, and the situ- ation we considered is far more complicated than the Ford-Fulkerson algorithm. Therefore, we properly use the Ford-Fulkerson algorithm in the solution of the problem and propose a dynamic system planning algorithm based on the Ford-Fulkerson algorithm[17]. The algo- rithm takes the general planning and the planning of some rooms in emergency into account. The speciﬁc ﬂow chart is shown in Figure A-1 (shown in appendix).

As shown in the ﬂow chart of Figure A-1, the algorithm is divided into two parts, e- mergency handling and general case processing. In general case processing, each iteration represents a situation within a time period, such as within 0 to 1 second. When the number of people in the source point is less than 0.5, the iteration stops and the algorithm ends. In each iteration, the ﬂow matrix and the margin matrix can be derived by the Ford-Fulkerson algorithm. Then, the value of the edge between the source point and the room node in the original model, which is the initial number of people in each room is corrected by the ﬂow matrix. And the current ﬂow velocity model is used to correct the maximum ﬂow of the channel by the current ﬂow density in each channel and the ﬂow density at the exit. This will provide a picture of the ﬂow of people in each time period. Finally, speciﬁc path planning is obtained from all traﬃc matrices. And the degree of use of each channel can be derived from the margin matrix[18].

In emergency handling, we make the following processing. As shown in the emergency processing section of Figure A-1, ﬁrst, the person in the emergency room is transferred to the adjacent non-emergency room by default, and the entrance degree of the emergency room is set to zero. According to the maximum ﬂow rate of the connecting channel, the time required for the transition TT can be calculated. Since the emergency transfer route remains unchanged from 0 to TT, regardless of the external situation. In this way, in the general case, at the beginning of each iteration from 0 to TT, the number of people transferred from the emergency room during the time period is added to the remaining number of people in the non-emergency room. And set the corresponding route and ﬁnally integrated into the traﬃc matrix.

6 Simulation model validation

6.1 model initialization instructions

According to the graph model and matrix model deﬁned in 5.1 and 5.2, we initialize the number of nodes in the node (taking random numbers between 100 and 200), and specify the maximum ﬂow rates of each exit are 40 People/s, 35 People/s, 30 People/s.

As shown in Figure 5, 1 is a virtual ingress node, 9 is a virtual egress node, and 2-8 are actual nodes (where in the 6, 7, 8 nodes adjacent to the egress are called ﬁrst-level nodes, and the ﬁrst-level nodes are called second-level nodes), the value on the red line segment represents the initial number of people in the node, the value on the blue line segment represents the reachable maximum ﬂow of the diﬀerent channels between the nodes, and the value on the green line segment represents the maximum ﬂow of each exit.

6.2 Evacuation plan

According to the requirements of the topic, it is our goal to evacuate all personnel as quickly as possible. In order to achieve this goal, we substituted the model into the algorithm and solved it iteratively.

Here we take 5s as a time step and make a ﬂow diagram. As shown in Figure 6, the values on the red line have no practical meaning. The values on the blue and green lines indicate the channel and exit ﬂow in the 5S time step. It can be seen intuitively that the ﬁrst step of the evacuation plan is to empty the exit rooms 6, 7and 8. Then the personnel at the second- level nodes move to the adjacent ﬁrst-level nodes (Figure 6(a)). As the operating pressure of the evacuation medium-term channel increases, the channel between the two nodes may be required to be shunted (Figure 6(b)). Then, with the decrease of remaining number, the channel pressure between the two nodes decreases. The ﬂow reduction is even reduced to 0 (Figure 6(c)), and eventually all evacuation is completed.

In fact, our evacuation plan is a continuous process of the ﬂow chart given in each time section. According to this evacuation plan, all the people can be evacuated as soon as possible.

(a) Flow in 15s (b) Flows in 35s (c) Flows in 40s

6.3 Three types of bottleneck problems

There are many bottlenecks in the actual evacuation of the building crowd. We divide them into three categories: (1) bottlenecks due to channel supply and demand imbalances (2) bottlenecks due to uneven distribution of exports (3) single room export bottlenecks.

6.3.1 Bottlenecks due to imbalance in channel ﬂow

What we can ﬁnd from the ﬂow-time ﬁgure of the exit, shown in Figure 7(a), is that the ﬂow drops occurs at around 10s, 30s and 35s.

(a) Exit ﬂow - time graph (b) Flow Margin-time graph

Next, we reﬁne the reason of the drop in ﬂow, and make the channel Flow Margin-time graph of node 6 as Figure 7(b). Node 6 has two inlet channels and one outlet channel, corresponding to the three curves in the ﬁgure. The Flow Margin is deﬁned as the diﬀerence between the maximum ﬂow of the channel and the actual ﬂow, reﬂecting the remaining capacity of the channel. To minimize evacuation time, the Flow Margin must be minimized. It can be seen from the ﬁgure that the ﬂow margin of node 6 has a rise in 10s and about 42s respectively. The sharp rise in 42s is clearly due to the decline in the total number of people remaining. The reason for the slight increase at 10s is that the sum of the maximum ﬂow of channels 3-6 and 5-6 is less than the maximum ﬂow of channels 6-9 (15+12.1<30), that is, the ﬂow ”unbalance between supply and demand” occurs. Reﬂected in Figure 7(a), this creates a bottleneck in ﬂow at 10s.

In order to solve the problem ,we choose to expand the width of the restricted channel while keep the density unchanged to meet the ﬂow supply and demand balance. Figure 7(a) also shows the optimized outlet ﬂow-time diagram. It can be seen that the bottleneck is eliminated ,as well as , evacuation time shortened. The total evacuation time is about 43.2s. (The accuracy is related to the selected time step)

6.3.2 Bottlenecks due to uneven distribution of exports

As mentioned above, there is a bottleneck at 30s in the exit ﬂow-time chart. Make the remaining number of people in the 2.3.4.5-time chart, as shown in Figure 8.It can be seen that the absolute values of the slopes of nodes 3 and 2 are smaller than those of nodes 4 and 5, and the comparison of 3 to 4 is slower than the similar number of people. 2 to 5 fell more slowly. At around 30-35s, people in node 2, 4, 5 have been evacuated, but 3 has the remaining number, which caused a small decline in export ﬂows. There are two main reasons for the bottleneck: one is the uneven distribution of personnel in diﬀerent rooms, and the other is the uneven distribution of exports. These two reasons together cause the uneven speed of the overall personnel escape (that is, the slope is diﬀerent). The solution is to make the distribution of exports as uniform as possible in the case of similar numbers of people, especially in rooms far from the exit, there should be more outward access.

6.3.3 Single room export bottleneck

In addition to the two types of bottlenecks shown in Figure 7(a), there is still a bottleneck problem that is not reﬂected in this situation, that is, the single-room export bottleneck problem.

According to Helbing [19], Chunshan Lv [20] Weiguo Song [21] and others, the simulation of the evacuation model is carried out using a cellular automaton and a social force model: in the case of a relatively large population density, It is easy to form an ”arched” blockage at the exit of the room, and the greater the speed expected by the personnel, the more obvious the blockage.

In order to solve this bottleneck problem, we can control the evacuation of the expected speed by manual guidance, guidance, etc. to reduce or even eliminate the export blockage. (In fact, we have set the ﬂow velocity of 0.8m/s in the aforementioned model, and have considered the factors of export bottlenecks.) According to research by relevant experts [22], there are some more practical and speciﬁc measures that can eﬀectively prevent The bottleneck, such as setting a cylindrical obstacle, etc., a few meters before the exit.

6.4 Adaptive analysis

According to the topic requirements, museum managers hope to obtain an adaptive model that can be used to address a wide range of considerations and various types of potential threats. Let’s take a ﬁre accident in a room as an example to show that our model is adaptable. Assuming that room 8 is on ﬁre, it should meet such requirements: First, only leaving is allowed for room 8. Secondly, people in room 8 have to be evacuated as soon as possible. According to our aforementioned algorithm, the above two requirements can be achieved by blocking the entry channel of the node 8 which is shown in Figure9 (c), (d) and lead people evacuate to neighboring rooms just like Figure9 (a), (b).

(a) Normal situation in 5s (b) Emergency situation in 5s

(c) Normal situation in 15s (d) Emergency situation in 15s

According to the emergence of diﬀerent emergencies, the transformation of our model can lead to the corresponding evacuation plan, which is adaptable and can be applied.

6.5 Entry of emergency personnel

When an accident occurs, emergency personnel is often required to enter the building in time for rescue. In the actual rescue, how to realize the entry of emergency personnel is also an important issue that should be considered in the case of ensuring the rapid evacuation of personnel. We give two options for this: The ﬁrst one is real-time monitoring of channel ﬂow. When the ﬂow of people drops to 60%-70% of the maximum ﬂow, the emergency personnel are allowed to enter in. Second, when the situation is particularly urgent, priority is given to emergency personnel.We choose a shortest path, dedicated to emergency personnel use and close all channels and stairs link to this room in the model. Combined with domestic and foreign rescue cases, our program meets the actual requirements.

7 Louvre evacuation model

7.1 Application of the dynamic node graph in the Louvre

As mentioned before, we can use nodes to represent the relatively independent parts of the building. We can call these parts diﬀerent rooms.Therefore, we can divide the Louvre into ﬁve parts, representing the ground (0F), the ﬁrst ﬂoor (1F), the second ﬂoor (2F), the negative ﬁrst ﬂoor (-1F) and the negative second ﬂoor (-2F). These ﬁve ﬂoors can form ﬁve plane dynamic system node maps. The connecting part is the ”channel between layers” formed by the actual stairs.

In the actual process of building the model, we simplify each ﬂoor of the Louvre into a node diagram. Figure 10 shows the results of ﬁrst ﬂoor (1F)[23] as an example.

(a) Actual 1F (b) Node graph of 1F

After the dynamic node diagram of each layer is established, the layers are connected according to the actual distribution of stairs in the Louvre, as shown in Figure 11.

7.2 Analysis of the results of the Louvre model

7.2.1 Evacuation simulation

In the previous analysis of the model results, we have analyzed the evacuation of simple buildings. Now let’s take a look at the evacuation plan for the complex building of the Louvre.

(a) Flow in 50s (b) Flow in 120s

(c) Flow in 190s (d) Flow in 250s

In our simulation of the actual evacuation of the Louvre, we assumed some assumptions: I. The number of people in the hall is about 7,000; II. All persons are reasonably distributed according to the actual size of each room; III. In the evacuation process, the ﬂow density meets the actual statistical value In Figure 12(a), we can see that the four green lines meet at a point, which is the sink point, indicating the external environment. The number of people on the four green lines connected to it is the ﬂow of the four main exits. In Figure 12, in the same layer, the numbers on the line indicate the ﬂow of people carried by the corridors and other channels in a period of time; the lines between the diﬀerent layers represent the actual stairs, they The numbers above indicate the ﬂow of people carried by the stairs over a period of time.

As can be seen from Figure 12, this is a dynamic evacuation process simulation model.

From the simulation, we can summarize the following conclusions: I. At the beginning of the evacuation, it is necessary to keep the exit area open; II. In the middle of the evacuation, it is found that the rooms far away from the exit are very congested, so consider opening other exits closer to them; III. In the later stage of evacuation, it can be found that the ﬂow of some channels has been reduced, allowing rescuers to enter the venue in time.

7.2.2 Bottleneck analysis

It can be seen from Figure 13, the personnel in the hall can basically be evacuated within ﬁve minutes.

red lines indicate that a channel is fully loaded, which is highly likely to cause an evacuation bottleneck. According to the blue line near the red line (not full load channel), the evacuation route can be re-planned to solve the bottleneck problem.

8 How to use the model

In order to give museum personnel a complete model exploration method, we give the fol- lowing suggestions: I. Based on the details and dimensions of the museum, perfect the model and establish the most accurate spatial node map; II. Set up a density detector at each key part of the hall to detect the density in real time to ensure the accuracy of the data; III. Once the accident occurs, the model is quickly used for evacuation simulation. Because (a) Margin in 50s (b) Margin in 120s

(c) Margin in 190s (d) Margin in 250s

the calculation speed of this model is much faster than the actual evacuation speed, museum personnel can ﬁnd the optimal evacuation route in advance and give timely instructions; (recommended to install clear and conspicuous indicator lights in the evacuation section) IV. Because the model is adaptable, museum personnel can adjust the model based on actual accidents. For example, if a room is on ﬁre, the route can be re-planned according to the model calculation results to ensure that people can get real-time and optimal solutions;

V. Through the simulation of the model, the bottleneck in the evacuation process can be

quickly identiﬁed, so that the extra exits can be arranged to make the export distribution most reasonable;

VI. Through dynamic simulations, museum personnel can ﬁnd the most appropriate route

and time for rescuers to enter.

9 Conclusion

9.1 Sensitivity analysis

In the actual evacuation process, due to some objective reasons, such as the error of the density detector, the model will produce a certain deviation in the process of evacuation plan simulation. To determine the eﬀect of these deviations on the ﬁnal result, we performed a sensitivity analysis. Set the parameter to the ﬂow density so that it has a 5% error. The results produced are shown in Figure 15.

It can be seen that the model can guarantee the accuracy of the simulation within a certain (a) Veriﬁcation model (b) Louvre model

error range. The museum only needs to ensure that the error of the ﬂow density detection device is small to get accurate results. In addition, in the actual evacuation process, the ﬂow density of each part is time-varying, so the accuracy of the current event detection device is more needed. Since the model can respond to the changing results quickly, to a certain extent, the model can eliminate the impact of errors through iterative updating. In this way, the museum can ﬁnd the best evacuation plan more accurately.

9.2 The model

9.2.1 Strength

The model has great generalization because it does not consider any special circumstances but the general situation. And the model fully measures the structure inside the building, and the calculation result is that the route plan is more intuitive. In addition, when there is a need to open or close a channel, room or exit, it can be easily modiﬁed in the model. This also reﬂects the excellent adaptability of the model.

9.2.2 Weaknesses

While using the model, in order to fully exert its dynamic capabilities, it may be necessary to monitor the ﬂow density of the channel and the exit. Thus there are certain limitations.

9.3 The algorithm

9.3.1 Strength

I.The eﬀects of individual interactions and the physical parameters of speciﬁc channels are taken into account in the calculation of the maximum ﬂow allowed in channels. In the application of the N&M model and the SES model, real-time human ﬂow density is adopted, and therefore, it has certain dynamics. II.Since the planning is performed from the perspective of the system, the algorithm is extremely fast compared with other algorithms, such as a cellular automaton-based planning algorithm. This allows a number of possible scenarios to be tried by modifying the model parameters in response to an unexpected situation. III.Since the ﬂow and the margin at any moment in the model can be obtained directly from the algorithm, the bottleneck problem that may occur in the planning scheme and the model can be found directly through the visualization of the ﬂow matrix and the margin matrix.

9.3.2 Weaknesses

Firstly, the Ford-Fulkerson algorithm has certain limitations. When there is a special case for each value in the graph, the algorithm will loop indeﬁnitely. However, considering that we apply the algorithm to the human ﬂow problem, the probability of occurrence in a special case is almost zero.

Secondly, the calculation result will occupy a large amount of storage space with the increase of precision. However, in general buildings, the required storage space is still within acceptable limits.

Appendix

Other ﬁgures

Figure A-1: Flow diagrams of algorithm (a) Real -2F (b) Simulation of -2F

(c) Real -1F (d) Simulation of -1F

(e) Real 0F (f) Simulation of 0F

Figure A-2: -2F ∼0F (a) Real 1F (b) Simulation of 1F

(c) Real 2F (d) Simulation of 2F

Figure A-3: 1F ∼2F

control procedures

BFS

function [ out, Parent ] = BFSGraph, start, End, parent, ROW visited = zeros(1, ROW); queue = []; queue = [queue, start]; visited(start) = 1; while queue u = queue(1); queue(1) = []; for i = 1:ROW if (visited(i)==0)&&(Graph(u, i)¿0) queue = [queue, i]; visited(i) = 1; parent(i) = u; end end end out = visited(End); Parent = parent; end

Ford fulkerson

function [max ﬂow, Remain] = Ford fulkerson(Graph, s, e, ROW) NUM INF = inf; parent = zeros(1, ROW); parent(:) = -1; max ﬂow = 0; start = s; End = e; [out, parent] = BFS (Graph, start, End, parent, ROW); while out path ﬂow = NUM INF; start = End; while start = s path ﬂow = min(path ﬂow, Graph(parent(1, start), start)); start = parent(1, start); end max ﬂow = max ﬂow + path ﬂow; v = End; while v = start u = parent(1, v); Graph(u, v) = Graph(u, v) - path ﬂow; Graph(v, u) = Graph(v, u) + path ﬂow; v = parent(1, v); end [out, parent] = BFS(Graph, start, End, parent, ROW); end Remain = Graph; end

Channel

function [Graph Channel] = Channel(Channel width, Channel density, ac) v = 1 - 0.266.*1.40.*Channel density; Graph Channel = v.*ac.*Channel width.*Channel density; end Stairs

function [Graph Stairs] = Stairs(Stairs width, Stairs density, ac) v = 1 - 0.266.*1.08.*Stairs density; Graph Stairs = v.*ac.*Stairs width.*Stairs density; end

Main

function[Max ﬂow, Flow, Remain, Time] = Main(G,ac)%Stairs width, Stairs density, Chan- nel width, Channel density, Graph enter, Graph exit, ac)%, Emergency) Graph = G;%Channel(Channel width, Channel density, ac) + Stairs(Stairs width, Stairs density, ac) + Graph enter + (Graph exit./5.*ac); ROW = length(Graph); Graph(2:ROW,:) = Graph(2:ROW,:).*ac./5; Total = sum(Graph(1,:)) % Emergency situation % Only leaving is allowed % Use this section by uncommenting all about this %{ if ∼isempty(Emergency) Graph(2:ROW,Emergency) = 0; Ge = Graph; t = []; for i = 1:length(Emergency) v = sum(Graph(Emergency(i),:),2); t = [t, ac*Graph(1,Emergency(i))/v]; end Graph(1, Emergency) = 0; Graph(Emergency, :) = 0; end %} i = 0; Max ﬂow = []; Flow = zeros(ROW, ROW, 1); Remain = zeros(ROW, ROW, 1); while Total¿0.5 i = i+1; mf = 0; %{ if ∼isempty(Emergency) for j = 1:length(Emergency) if i*ac-t(j)¡ac Graph(1,:) = Graph(1,:) + Ge(Emergency(j),:).*(min(t(j),i*ac)-i*ac+ac)./ac;

mf = mf+Graph(1,ROW); Graph(1,ROW) = 0; end end end %} Copy = Graph; [max ﬂow, Copy] = Ford fulkerson(Copy, 1, ROW, ROW); Remain(:, :, i) = Copy; Temp = Graph - Copy; Temp(Temp¡0) = 0; %{ if isempty(Emergency) for j = 1:length(Emergency) if i*ac-t(j)¡ac Temp(Emergency(j),:) = Temp(Emergency(j),:) + Ge(Emergency(j),:); end end end %} Flow(:, :, i) = Temp; max ﬂow = max ﬂow + mf; Max ﬂow = [Max ﬂow, max ﬂow]; Total = Total - max ﬂow Graph(1, :) = Graph(1, :) - Temp(1, :); end Time = i*ac; end
