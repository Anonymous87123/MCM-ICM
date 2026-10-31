For ofﬁce use only For ofﬁce use only

T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

2019 MCM/ICM Summary Sheet

Hurricane Maria Damage left Puerto Rico people a lot of pain and devastation. HELP,Inc., an NGO, is attempting to improve its response capabilities by designing a transportable disaster response system called "DroneGo".

In order to better assess the transport capability of the drone ﬂeet, we establish a Transport Capability Evaluation Model of the drone ﬂeet, so that we can maximize the medicine transportation capability of the drone ﬂeet when the disaster location is unknown. In this model, we use the algorithm of linear programming to solve the limitations of volume, weight and other simple factors. After that, we used an algorithm based on three-space segmentation and improved Monte Carlo simulation to solve the size limitation of the objects. As a result, we obtain a reliable evaluation of the transport capability of drones, and it can be found that among the drones, the transportation capability of drone G is the strongest.

Through the research on the reconnaissance method of the drones, we get the Reconnaissance Ca- pability Model of the drone ﬂeet. In this model, we ﬁnd that the reconnaissance capability of drone B is the strongest. Based on these two models (TCM & RCM) and abundant geographic information, we developed a Geospatial Analysis Model. We employ the Analytical Hierarchy Process (AHP) in the space of all position, obtaining a spatial distribution of drone ﬂeet ˛a´rs transportation capability and re- connaissance capability. Then, we establish an overall Efﬁciency Evaluation Model for the drone ﬂeet, using a nonlinear programming with a variable parameter to obtain the optimal solution of the drone ﬂeet overall efﬁciency and its spatial location. Consequently, we can determine a conﬁguration of the drone ﬂeet and each container’s drop point. DroneGo users can also adjust the variable parameter de- pending on whether they care more about their ﬂeet ˛a´rs transport capability or reconnaissance capability to determine different options. For the problem of multiple containers, we use a dynamic programming rule that allows users to arrange multiple containers.

In considering that the transportation capability of the drone ﬂeet is as important as the reconnais- sance capability, we get results that the medicine delivery can be maintained for more than two months and road reconnaissance coverage can reach nearly 60%. Meanwhile we construct an efﬁcient Schedule Arrangement Model and Route Arrangement Model of drones using an integer programming model and an improved greedy algorithm, so that the drone ﬂeet can be auto arranged.

The sensitivity analysis shows the strong robustness of our model. Meanwhile, we further discuss the possibility of developing a DroneGo system software, and provide practicable advice to the HELP, Inc. CEO.

1 Introduction

People in disaster areas are in great need of timely emergency services. [1] Drones can help a lot in emergency rescue. According to a drone manufacturer DJI [2], drones have saved 59 lives since 2013.

In this paper, we will

• Analyze three dimensional packing problem and develop Three Space Division Model and improved Monte-Carlo Simulation to solve the problem of packing restrictions in the transportation.

• Analyze the transportation capability and detective capability of each Drone type,apply AHP method to considers the inﬂuence of many possible factors on the selection of con- tainer drop location , including transportation, population, geography and medical infor- mation.

• Build a model to determine drone payload packing conﬁguration and solve it with a com- plex integer programming quickly and accurately.

• Improve greedy algorithm and ﬁgure out the drone route planing quickly and accurately.

2 Assumptions and Justiﬁcation

We make some general assumptions to simplify our model. These assumptions together with corresponding justiﬁcation are listed below:

• There are no charging devices for drones. In 2017, Hurricane Maria knocked down 80% of Puerto Rico’s utility poles and all transmission lines. We can infer that electricity are not available on the island. Our Cargo will not include charging equipment or generating set, due to extra weight and inconvenience.

• The cargo weight does not inﬂuence the maximum ﬂight distance of a drone. That is, maximum ﬂight distance is exactly the same with or without a cargo. We make the assumption for simplicity. In reality, the weight of a delivery drone is often larger than that of its cargo. It is quite reasonable to neglect the inﬂuence of cargo weight. And this will greatly simply our model.

• For each Cargo Container, we will load one tethered Drone (type H). In natural disasters, communication facilities are often affected to various degrees, and emergency communi- cation becomes an urgent need. It can act as an emergency communication base station.

Tethered drones will greatly enhance the disaster response capability of DroneGo system.

• One drone can carry one drone cargo bay or no bay for every ﬂight. If the drone carries one, it can only deliver the bay to one location. Both of the two types of drone cargo bay are "top loaded", that is, loaded on the top of a drone. If we distribute more than one bay at a ﬂight, connections between cargo bays could be unstable. We can deliver a drone cargo bay to only one place since it is an integral package that cannot be open in transit.

• Helicopters can transport cargo containers to any given place in the disaster area. In disaster-affected areas, timely external assistance is urgently needed to restore order. There- fore, we consider air transportation rather than sea transportation. Although Puerto Rico is an island, air transportation will bring adaptability to our model in other situations.

• Communication and data transmission of drones are always available. We can achieve telecommunication by radio communication or satellite communication. Drone commu- nication dose not rely on ground devices.

• For the ith type of drone, its maximum Flight Distance, denoted by Disti is in direct proportion to the product of Speed and FlightTime(No Cargo). From that assumption, we have Disti = α × Speed × Flight Time (No Cargo), where α represents distance-loss coefﬁcient. Here we neglect the effect of weather (especially wind) and different battery and motor of different drones of a speciﬁc type. To determine α, we note that there are mostly mountains with few plains. And Puerto Rico has a mean elevation of 261 m. [3] The high elevation shortens the maximum ﬂight distance. We have α < 1. For simpliﬁcation, we choose α = 0.9.

More detailed assumptions will be listed if needed.

3 Transportation Capability Evaluation Model

In this section, we will evaluate transportation ability of each type of drones. For simplicity, we will focus on the need of medical transportation here. We will incorporate road reconnais- sance into our model in Section 5.

3.1 Assumptions in This Model

We will use the following assumptions in this section:

• All Cargo Containers(CC), Drone (in shipping containers), Drone Cargo Bays (DCB), and Medical packages (MP) are cuboids.

• Drones and Drone Cargo Bays should be placed into Cargo Containers in parallel, which is "parallel placement". That is, the inner subface of Drones or Bays must be par- allel to the corresponding surface of the Cargo Container. There are two reasons. For one thing, the parallel placement is one of the most commonly used packing methods. For another thing, cargos can be easily placed in this way and have a high stability.

• The thickness of Drone Cargo Bays can be neglected.

• Goods can be arbitrarily rotated, but must still satisfy the "parallel placement" condi- tion.

• As is interpreted in the problem description, each Cargo Container’s contents should be packed, so all Medical Packages should be packed in Drone Cargo Bays. We do not consider Medical Packages directly placed in a Cargo Container.

3.2 Three Space Division Model

3.2.1 One Goods Condition

To design a packing conﬁguration for DroneGo, we need to put MEDs into Bays and put Bays or Drones into Containers. Due to various kinds of goods in the problem, this is a three- dimensional heterogeneous container loading problem. We use the Three Space Division Method and Monte Carlo Simulation to solve it.

Note that we refer to a rectangular container that contains goods as a box. As is shown in Figure 1, L, W and H is the length, width and height of the container, respectively. Similarly, l, w and h is the length, width and height of the cargo, respectively. We set up a Cartesian coordinate at the left bottom vertex of the container. Note that we consider the position of the container is unchanged. We put the cargo into the container, so that two left bottom vertexes coincide. Arrangement problem is a way to think about ways to put the cargo. To put h into x, y and z coordinates, we have A3 3 = 6. There are six ways to put the cargo inside. That is, there are six possible combinations of the coordinates of the diagonal vertex of the cargo.

For every speciﬁc combination, we can see that the rest space in the container are cut into three parts (spaceX, spaceY and spaceZ) , see ﬁgure 1. One possible sequence (shown in Figure 1) to generate the three parts is

1. Procedure X: Cut the remaining space using a plane perpendicular to the X-axis and get spaceX.

2. Procedure Y: Cut the remaining space using a plane perpendicular to the Y-axis and get spaceY.

3. Procedure Z: Cut the remaining space using a plane perpendicular to the Z-axis and get spaceZ.

We refer to this sequence as a X-Y-Z sequence. The rest are similar. Arrangement problem is a way to think about the space cutting process. To generate a sequence from procedure X, Y and Z we have A3 3 = 6.

Thus, if a cargo can be put into the cargo, we have the total cases of three space division: 6 × 6 = 36 Then we consider every new space as a new container. And the three space division process goes on, until the cargo can not be put into any of the existing containers. In this way, we can traverse all situations and ﬁnd the optimal solution for a speciﬁc objective function.

3.2.2 Multiple Goods Condition

To clarify the problem, we will use the following notations:

• K = {1, 2, . . . , |K|} is the set of Boxes’ number;

• R = {1, 2, . . . , |R|} is the set of goods’ types;

• Mr = {1, 2, . . . , |Mr|} is the set of goods’ number (same type) ;

• sB = (L W H)T is Box Size column vector; r = (lr wr hr)T is the rth type of Goods Size column vector;

• sG

• Xk is the number of goods in the kth box;

•  1, if the mth Goods of Type r is in Box k Ykrm = is an Existing Flag; 0, otherwise

• u = (xkrm ykrm zkrm)T is coordinates of the mth goods of Type r in Box k;

•  1, if the length of the mth Goods of Type r is parallel to the x-axis lxrm = 0, otherwise

is a Conﬁguration Variable;

• lxrm lyrm lzrm !

wxrm wyrm wzrm P = is Conﬁguration Matrix.

hxrm hyrm hzrm Undeﬁned elements in the matrix is deﬁned similarly to lxrm.

In multiple-goods-condition, we consider the container loading problem as a Single-objective integer programming problem. Constraint Conditions of the three-dimensional heterogeneous container loading problem are listed below:

1. Boxes should contain all goods:

|K| |R| X X Xk = Mr r=1 k=1 2. Corresponding Rule. Each goods should be placed into just only one box:

|K| X ∀r ∈R, ∀m ∈Mr, Ykmr = 1 k=1

3. Conﬁguration Constraint. Each edge in each goods should be parallel to just only one edge of the corresponding box. Let P = (pab)3×3, we have

3 3 X X pab = 1 pab = 1.

a=1 b=1

4. Box Size Constraint. All goods should be inside the corresponding box:

∀k ∈K, ∀r ∈R, ∀m ∈Mr, Ykrm(u + P · sG r ) ≤sB We can solve the programming problem with a speciﬁc objective function.

3.3 Putting MEDs into Bays

Since there are only three types of MEDs and two types of Bays, putting MEDs into Bays is relatively simple. In 3D heterogeneous container loading problems, space utilization(SU) usually decreases as type of goods R increases. For simplicity, we only consider two types of MEDs or less in a Bay. We do not need to consider an objective function in this process. Rather, we list all possible combinations subject to its constraint conditions.

Let R = {1, 2, 3}, whose elements 1, 2 and 3 correspond to MED1, MED2 and MED3, re- spectively. And |Mr| is the number of MEDr. For type q Bay (q = 1, 2), we have the following constraint conditions:

P|K| k=1 Xk = P3  r=1 Mr  P|K|  k=1 Ykmr = 1, ∀r ∈R, ∀m ∈Mr    P3 , (1) a=1 pab = 1 P3  b=1 pab = 1    q , ∀k ∈K, ∀r ∈R, ∀m ∈Mr Ykrm(u + P · sG r ) ≤sB 

where sB 1 = (8 10 14)T, sB 2 = (24 20 20)T.

For type i Drone, an additional constraint is that total weight cannot exceed Max Payload Capability(MPCi): 2|M1| + 2|M2| + 3|M3| ≤MPCi (2)

(1 and (2) determine whether we can put a set of MEDs into a Bay. If that set of MEDs works, we calculate its space utilization:

P3 r=1 (|Mr|lrwrhr) SU = , LqWqHq where (l1 w1 h1)T = (14 7 5)T, (l2 w2 h2)T = (5 8 5)T, (l3 w3 h3)T = (12 7 4)T, (L1 W1 H1)T = (8 10 14)T, (L2 W2 H2)T = (24 20 20)T.

We draw the space utilization plot of Drone D (Bay 1) and Drone F (Bay 2), see Figure 2. From the ﬁgure we can see that space utilization of Bay 2 is relatively low. The reason is that the inequality (2) is strict. In most cases, the max payload capability is so small that the all sets of MEDs that satisfy (2) can be loaded. So the sub-ﬁgures for Bay 2 clearly shows the inequality (2).

From Figure 2, we conclude that the Transport Capability matrix is

1 1 1   2 4 2   7 7 4     2 4 2 TC = . (4)   7 7 5     11 11 7   10 10 6

3.4 Drone Transport Capability Model

Since we only consider medicine transport in this section, there must be a corresponding Drone Cargo Bay on each drone. The number of Typei Drones to carry NumMEDj MEDjs is Numij = NumMEDj/TCij . Note that we use Numij to evaluate transport capability, so it may be a decimal. The volume needed when one Typei Drone carries all MEDs for one day is

3 X V Med Day + V Bay Numij)(V drone = ( ) i i i j=1

. The number of days that a Typei Drone can continue transporting MEDs to all needed place is

Daysi = Vcontainer/V Med Day i Transport Capability Index of Typei Drone is deﬁned as the normalization of maximum day Daysi:

1≤k≤7 {Daysk} TCIi = Daysi/ max

We have two matrices:

2.97 0.0629     15.92 0.3371     8.78 0.1859         24.45 0.5178 Days = TCI = (5)     41.46 0.8782         28.98 0.6139     47.21 1.0000

3.5 Putting Drones and Bays into Cargo Conatainers

According to TCI matrix (5), Type E and G Drones have the best transport capability. We will choose Type E and G as alternative transport drones. The corresponding Bays are Bays 2. We will also load one Drone H (tethered drone) in each Cargo Container, because it helps to build emergency communication.

Let R = {4, 5, 6, 7}. 4, 5, 6 and 7 represent Bay 2, Drone E, H and G, respectively. The number of MEDs in Bay 2 only relies on Type i drone’s Max Payload Capability MPCi. So we conclude that for Drone ﬂeet consisting of E and G, transport capability is only relevant to Total Load Weight:

X MPCi × |Mi| = 15|M5| + 20|M7| TLW = (6) i=5,7

Our problem can be stated as

TLW = 15|M5| + 20|M7| max

Equation (??) shows that each Drone must carry one Bay, so the total number of Drones E and G equal to the number of Bays 2. Equation (??) shows that each Cargo Container should have one Type H Drone.

3.6 Monte-Carlo Simulation And Results

We use Monte-Carlo Simulation to get a satisfactory solution of the problem in Section 4.5. Since this is a NP-completeness problem, it takes too long to traverse all situations. Our objec- tive function will not have major changes with a narrow change of inputs. That is, the optimal point is not an isolated singularity. That’s why we choose Monte-Carlo Simulation.

If the probability to ﬁnd the optimal point is 10−5 for one simulation, the probability to ﬁnd the optimal point will be 1 −0.999991000000 = 0.999954 with one billion simulations. Figure 3 is our simulation process using Three Space Division method. We start at a feasible solution |M4| = 50, |M5| = 30, |M6| = 1, |M7| = 20.

Using the Three Space Division Model and Monte-Carlo Simulation, we obtain the satisfac- tory packing conﬁguration for each container (with or without Drone H). The result shows that the ideal optimal solution is, at most, slightly better than our satisﬁed solution(space utiliza- tion up to 97.97%). It also validates that Drone G has the best transportation capability, which perfectly ﬁt the highest Drone G TCI value.

4 Geospatial Analysis Model

4.1 Drone Reconnaissance Model

For a video-capable drone, in order to effectively estimate its maximum viewing radius, rview, we make the following assumptions:

1. The height between a drone and the ground is 20 meters.

2. The drone’s lens can swing back and forth from side to side, with unlimited viewing angles.

3. The camera on a drone (if it has one) is a two megapixel camera (a 1080P lens).

4. The resolution of road detection is one meter.

We see  tan(θ + ∆θ) = rview/20 , tan θ = (rview −1)/20 where • θ is the camera’s forward viewing angle;

• ∆θ is the smallest resolution angle;

• rview is the maximum viewing radius.

For a two megapixel camera, we have ∆θ = 3 × 10−3rad. Plugging it into (7), we obtain

 θ = 1.322 rad rview = 79.7 m .

Since rview is close to 100 m, we can divide the island map into grid on the order of one hundred meters, as is shown in Figure[ÍijÆˇn]. Every grid covers a 100 m × 100 m square. Cor- responding to the longitude and latitude,(x, y) is the grid point coordinates of the position.

4.2 Geographical Features

We divide the location selection problem into two major parts Transport and Reconnais- sance. Then we decide that the information of highway, population, geographic and medical are important to Transport and Reconnaissance. Using the map in the attachment and from Puerto Rico Maps [4], we ﬁnd seven features for the four types of information, see Table 2.

FO 1 2 3 4 5 6 7 Hospital High Main Highways Population location feature(FO) population Harbours Altitude highways & roads distribution & medical areas needs

For a certain position, Feature1 means the main highways. Feature 2 means the highways we extract from attachment 1. Feature 3 means the density of population [4]. Feature4 means high population areas from the given map. Feature 5 means the distance from harbors. [3] Feature 6 means the altitude. Feature 7 means the index considering transporting MEDs.

The feature maps are shown in Figure 4. Note that all feature maps are normalized, so that for every map, the sum of all values is 1 :

X X Feature(FO, x, y), ∀FO ∈{Z|1 ≤FO ≤7}, x y

where Feature(FO, x, y) is the geographical distribution function of featureFO.

The weight of hospital j

3 X MedWighti × MedNumberji HOSj = i=1

We assign the values in hospital map.

We calculate Transport cost for MEDj by Demand number for MEDj:

3 X MedWeightj = Medj/ Medi i=1 We have MedWeight = (0.2949 0.2681 0.4369)T j = 1, 2, 3 (8)

From (8) we see MedWeight2 is smallest, because MED 2 has the least demand.

4.3 Singal Location Determination

4.3.1 Detail Information of TI and RI

T Idetail is an evaluation index for Drone Type i of feature FO in position p1(x, y) and evaluates the detailed transport capability. Let p1 be the target position for Cargo Container. Let p2 be the corresponding point in feature map, we have

X TIdetail(i, FO, p1) = TIα(i, p1, p2)Feature(FO, p2).

p2

Similarly, RIdetail(i, FO, p1) = P p2 RIα(i, p1, p2)Feature(FO, p2).

T Iα is a function of i, p1 and p2:

TIα(i, p1, p2) = TIdistance(i, p1, p2)TIcover(i)TCI(i)

Similarly, RIα(i, p1, p2) = RIdistance(i, p1, p2)RIcover(i)RCI(i)

T Idistance measures Transporting Index with ﬂight distance:

1 −dis(p1,p2)  DIS(i) βTI, dis < DIS TIdistance = , (9) 0, otherwise

where

• dis(p1, p2) is the distance between p1, p2;

• DIS(i) is the longest ﬂight distance.

DIS(i) = α × Speed × Flight Time (No Cargo), see(2) (10)

The function (9) shows that closer points are more important within coverage area. βTI = 0.2 produces a linear transformation.

Similarly, 1 −(1 −dis(p1,p2)  DIS(i) )βRI, dis < DIS RIdistance = , (11) 0, otherwise

where βRI = 0.2. βRI produces a linear transformation. Compare (9) and (11), function (11) shows that in reconnaissance, farther points are preferred, because the close ones can be detect- ed on the way to medical

T Icover measures Transporting Index with coverage area. The effectiveness of each point in coverage area is equally important.

TIcover(i) = 1/(π · (DIS(i))2 · β′ TI), (12)

where β′ TI is determined by βTI; β′ TI = 13/15.

(i) = 1/(π · (DIS(i))2 · β′ β′ Similarly, RIcover RI), RI = 14/15 T CI measures Transporting Index with and Transporting Capability of Drone Type i with unit volume. We computed the result of TCI(i) in matrix TCI (5). Similarly, We calculate RCI1(i) = (DIS(i))2/V (i),where V(i) is the total volume of Type i drones and corresponding Bays. Then we normalize it as RCI(i) = RCI1(i)/ max 1≤p≤7 RCI1(p)

After we calculate TIdetail(i, FO, x, y) and RIdetail(i, FO, x, y), we should take all features into account and calculate the integrate Transport Index of all features T I(i, x, y):

X wTI(FO) · TIdetail(i, FO, x, y) TI(i, x, y) = (13) FO Similarly, RI(i, x, y) = P FO wRI(FO) · RIdetail(i, FO, x, y). We obtain a Reconnaissance Capa- bility Index matrix 0.0768   1.0000   0.1105     0.1850 RCI = (14)   0.1190     0.1782   0.1194 Matrix (14) shows that Drone B is the best type to detect highways and roads. Note that Drone B is a lot better than the other types.

We listed a few results of the detail information of TI and RI based on Puerto Rico case (see Figure 4).

(a) Main Highways (b) Highways and Roads (c) Populated Places

(d) TI Drone G Main Highways (e) TI Drone G Highways & Roads (f) TI Drone G Populated Places

(g) RI Drone E Main Highways (h) RI Drone E Highways &c Roads (i) RI Drone E Populated Places

4.3.2 TI and RI

To determine the weight of different features, we employ Analytic Hierarchy Process (AHP). Since those features in Table 2 have different effects on TI and RI, we use AHP twice for TI and RI. The comparison matrices are listed below:

(a) Comparison Matrix For TI (b) Comparison Matrix For RI

To test the consistency of the matrices, we calculate the Consistency Ratio (CR), which is deﬁned as the ratio of Consistency Index (CI) to Average Random Consistency Index (RI′). n = 4 , RI′ = 0.90, CR = (λmax −n)/(n −1). For TI, CI = 0.0532, CR = 0.0598 < 0.1. For RI, CI = 0.0526, CR = 0.0591 < 0.1.so the consistency of the matrices is conﬁrmed.

As is indicated in Figure 6, for Transporting Index, Medical information is the most im- portant factor weighting 67.03%. That is because hospital destination of a Drone transporting MEDs. For Reconnaissance Index, highway information take up the highest at 60.11%. One possible reason is that the ﬂight distance of Drones is limited. Drones must get close enough to detect highways.

Then we put the weight terms into (13) and (4.3.1), and get TI and RI (see Figure5).

(c) TI Drone B (d) TI Drone E (e) TI Drone G

(f) RI Drone B (g) RI Drone E (h) RI Drone G

4.3.3 Efﬁciency Evaluation

To show the relative relationship between TI and RI, we introduce an important parameter λ as the transport objective coefﬁcient. 0 ≤λ ≤1. λ shows the importance of transport. The bigger λ is, the more important transport is.

The location selection problem is a multi-objective programming problem. We simplify it to a single-objective-programming by using λ. Considering transport and reconnaissance, our objective function is the overall efﬁciency:

ALLRI1−λ E = TIλ ALL, (15)

In function (15),we deﬁne the Transport Index for all types of drones:

7 X v(i) · TI(i), TIALL = (16) i=1 where v(i) is the volume percentage of Type i drones and corresponding Bays in all types. Since v(i) = V (i)/ P7 p=1 V (p), we have P7 i=1 v(i) = 1.

Similarly, RIALL is the RI for all types of drones: RIALL = P7 i=1 v(i) · RI(i)

We compute the Best Efﬁciency for each position (x, y). Our programming problem can be stated as ALLRI1−λ E = TIλ max ALL 7 X v(i) = 1 s.t.

i=1 ∀i ∈{Z|1 ≤i ≤7} v(i) ≥0,

(a) lambda = 0.2 (b) lambda = 0.4 (c) lambda = 0.5

(d) lambda = 0.6 (e) lambda = 0.8 (f) lambda = 1.0

We apply this method to the Puerto Rico situation (see Figure 7).

4.4 Multiple Locations Determination

Selecting multiple best locations is a dynamic programming problem. Each location selec- tion can effect the new selection. To show the effect,we set the two following rules:

• Effects on Transportation. After each selection, we assume the Container satisﬁes 1/3 of all MEDs demands if its Drones and MED sullplies allow. Note that the container should ﬁrst provide MEDs to nearby medical centers. And we should renormalize the the Medical Infromation feature.

• Effects on Reconnaissance. After each selection, we assume Drones of the Container can detect all highways within the container’s Maximun Reconnaissance Scope. High- way Information feature within that scope should decrease. We will multiply them by a coefﬁcient of r0 = 0.1.

4.5 Results

5 Fleet Arrange Model

5.1 Schedule Arrangement Model

5.1.1 Satisfactory Solution on MEDs

We maximize the ability of DroneGo ﬂeet to satisfy the anticipated Medical Package De- mand. According to the choices of drone type given in Part B, we will only employ drone B, E and G to transport MEDs. First, we search satisfactory solution on how to put MEDs into a Bay. Then we can use those schemes to assemble a best schedule so that we maximize the ability of DroneGo ﬂeet to satisfy the anticipated Medical Package Demand.

We will use the following notations in this section:

• MEDweight is the weight of MED j; j • MEDNum is the number of MED j put into a bay in a satisfactory solution; j

• Drone 1,2 and 3 correspond to B,E and G, respectively;

• kij is the jth scheme for Type i drones;

• Ki = (ki1 ki2 . . . kir)T is the set of all the satisfactory schemes for drone i.

By using the Transport Capability matrix (4) in Section 4.3, we demonstrate that for drone B, E and G, only Max Payload Capacity (MPC) will play a decisive role on whether a scheme is fea- sible. Actually, satisfactory solutions must be at the feasible region. Consequently, satisfactory solution for a Type i drone should subject to the stated constraints:

3 X MEDweight × MEDnum ≤MPCi j j 1

3 X MEDweight MEDweight ×MEDnum + min > MPCi j j j j 1

We use integer programming method to search feasible solutions.

ki1 is the 1st solution.

Eventually we get K1,K2 K3. for drone 1 2 3 respectively has 3,27,44 satisfactory schemes.

5.1.2 Maximum Effective Days Model

Now we have known all satisfactory schemes on how to put MEDs into a Bay for drone B,E and G.To evaluate the the ability of DroneGo ﬂeet to transport Emergency Medical Package,we make an assumption: Every delivery location’s need for MED should be satisﬁed equally.

Since delivery location has the certain anticipated Medical Package Demand everyday,we can calculate a Maximum supply days if the type and number of drone and the schemes for each corresponding drone are determined.

we will use the following notations:

• MEDneed = (mj1 mj2 mj3) is the need of sth delivery location within the range of trans- s portation. mj1, mj2, mj3 is corresponding to the number of MED1,2,3.

• Numirs is the number of drone i which carry out the rth scheme ;

• |Ri| is the number of satisfactory schemes for drone i;

• S is the number of delivery location;

• Dayss is Maximum supply days for delivery position s.

Here is the Linear Programming model. For delivery position s,

| Ri | 3 X X Numirs kis ≥Dayss × MEDr max r i=1 |S| | Ri | X X Numirs = Qk s.t.

s r Numirs ≥0 | Ri | 3P P Numirs kis r i=1 1≤s≤|S|{Dayss} = min max Dayseffective = min 1≤s≤|S|( ) MEDs |S| | Ri | X X Numirs = Qk s.t.

s r Numirs ≥0

Through the use of integer linear programming, we can ﬁnd the optimal drone payload packing conﬁgurations by traversing all possible combinations of the satisﬁed scheme when the number of each drone type and delivery locations’ MEDs need are certain. Now we apply the Schedule Arrangement Model to the situation in Table 3. The result indicates that we can get an optimal solution in a given situation. Moreover, the result directly gives the drone payload packing conﬁgurations for every drone.

5.2 Drone Route Planning Model

Now that we have conﬁrmed the drone delivery plan. Under this scheme, the basic delivery strategy of each drone has been determined. Since we assume that each drone will not move once it has delivered the goods, the extra distance of the drone other than delivery can be used to detect the highways and roads. We can use a Greedy Search Algorithm to arrange individual drones. The algorithm is shown in Figure 8:

• Searching nearby, that is, searching the nearest road. Since most roads are continuous, the nearby search algorithm is simple, easy to operate and efﬁcient.

• The searched road should not be searched any more, and it should be deleted from the overall search targets.

• Delivery ﬁrst strategy, because delivery is urgent, so if you choose between delivery and search, then you must choose delivery.

In the algorithm, we call the hospital where the drones need to deliver as the target location. The keys of the algorithm are listed as follows Searching nearby, that is, searching the nearest road. Since most roads are continuous, the nearby search algorithm is simple, easy to operate and efﬁcient. The searched road should not be searched any more, and it should be deleted from the overall search targets. Delivery ﬁrst strategy, because delivery is urgent, so if you choose between delivery and search, then you must choose delivery.

For the drone ﬂeet as a whole, we need to select different drones for reconnaissance. Since short-range drones cannot detect points far from the targets and containers, we should priori- tize the path of these drones to maximize their reconnaissance potential. The number of drugs required by the hospital will be changed each time the drone delivers the goods, and the next delivery mission of the drone will also be changed accordingly. More speciﬁcally, if the delivery demand of a certain drug in a hospital has been met, the drone loaded with that drug should not be used as the target place.

Further, to improve the algorithm, we can ﬁnd that among the three selected drones, drone B, E and G, the transport capacity of drone B is the weakest, but its reconnaissance capability is the strongest. Even if we deduct the medicine delivery amount of drone B, the effect on the overall drug delivery amount is not signiﬁcant. Therefore, we should use drone B only for reconnaissance. If we apply the above strategy to the 3 container transport model with λ == 0.5, we can obtain the results of transportation path in Figure 10.

Under the model of λ = 0.5, our road reconnaissance coverage for Puerto Rico reached 59.86% (see Figure 10). We can ﬁnd that, in order to meet the needs of the three hospitals n- earby Puerto Rico ˛a´r capital, we use a lot of drones to transport medicine, so the reconnaissance coverage rate of this area is not high, however, in the area of transport demand is relatively small, the container 3, our reconnaissance coverage is very high. This result is consistent with our hypothesis that λ = 0.5, which means reconnaissance and transportation is equally im- portant. At the same time, since we consider the range reduction of drone affected by various reasons, that is, the ratio between the total range used and the ideal total range calculated is α = 0.9, the reconnaissance capability of drone ﬂeet may be better in actual use.

(a) Container 1(C1) (b) C1 drone B (c) C1 drone G

(d) Container 3(C3) (e) C3 drone B (f) C3 drone E

(g) Container 2(C2) (h) C2 drone E (i) All(routes under reconnaissance in black, undetectcted in gray)

the end of the yellow line represents the ﬁnal position of the drone)

6 Sensitivity Analysis

As is shown on Geospatial Analysis Model, we use AHP to get the weight vector of wTI and the weight vector of wRI. However, AHP is based on subjective inputs to some extent. Aiming to determine how robust our rankings are in the AHP process, we use the following proportionality equation for adjusting weights:

j = 1 −w′ p w′ wj, 1 −wp

where w′ j is the new weight, wp the original largest weight of the criterion to be adjusted,and w′ p the value after the criterion is adjusted.

We respectively apply a −10%, −20%, +10%, +20% variation to the wTI and wRI,and record the the results under each circumstance, respectively. The following is the new results:

In the table above, note that Latitude and longitude are used to indicate location and dis- tance between original and new position is shown if position changes. We can conclude that

• Above all, the table shows the strong robustness of our model.It is conspicuous that the results only change slightly,notwithstanding we let wDI or wTI have a sizable change.

• Remarkably, some positions of container and drone proportion don ˛a´rt vary with different wTI and wRI. Via analyzing the corresponding data, a reasonable explanation is that this position or proportion has much better performance than those adjacent choices.

7 Strengths and Weaknesses

7.1 Strengths

• A model based on Three Space Division Model and improved Monte-Carlo Simulation can solve the problem of packing restrictions in the transportation of goods and have high realizability by considering weight and volume limitations.

• Based on the AHP method,the Geospatial Analysis Model fully considers the inﬂuence of many possible factors on the selection of container drop location , including transporta- tion, population, geography and medical information. Therefore, the result of the model is highly credible.

• Complex integer programming model and improved greedy algorithm is able to give the drone schedule planning and route planning quickly and accurately.

• Flexibility and adaptability are also advantages of the Location Determination Model.

When the company change its strategy, new decisions can be quickly derived without modifying the algorithm.

7.2 Weaknesses

• While utilizing improved Monte-Carlo Simulation,the quality of the result may not achieve our high expectation.

• The rule of how to transport MEDs to different delivery position is uncertain.It can be further improved to meet different actual needs

• The correctness of our conclusions is related to the accuracy of the data collected and the estimates of transportation, population, geography and medical information.

8 Conclusion

To help with post-disaster relief, we designed a prototype of the DroneGo. The system estab- lishes the Drone Transport Model and Drone Survey Model, taking into account the characteris- tics of drone, medicine and container such as weight and size, as well as a variety of geographic information such as road information, population information, rescue information and medical information. We conclude that the Transportation Capability of Drone G is the strongest and the Reconnaissance Capability of drone B is the strongest. When users considered medicine delivery to be as important as road reconnaissance, we got results that the medicine delivery can be maintained for more than two months and road reconnaissance coverage reached nearly 60%.

To further provide advice to the DroneGo users, in our system, users can also input a d- ifferent transport/reconnaissance parameter, i.e., different emphasis on transport and recon- naissance. In this case, our DroneGo system can provide different ﬂeet conﬁgurations and container drop points to meet their needs. Meanwhile we construct an efﬁcient schedule ar- rangement and route arrangement model of drones using an integer programming model and an improved greedy algorithm, so the drone ﬂeet can be auto arranged.
