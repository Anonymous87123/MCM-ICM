# P-B-2011-11759-ee4be862

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Control Number: 11759

<!-- b000002 | furniture | pages [1] -->
Page 1 of 51

<!-- b000003 | heading | pages [1] -->
Abstract

<!-- b000004 | prose | pages [1] -->
We propose and evaluate two models to determine the minimum number of very high frequency (VHF) repeaters necessary to accomodate a given geographic distru- biton of users. By utilizing cluster analysis, each model uniquely designs a network of open and “continuous tone-coded squelch system” (CTCSS) repeaters to simulta- neously accomodate the desired user load. In addition, the models are mindful of connectivity issues and seek to establish the best connectivity for the set of users. Through the comparison of these two models, we seek to establish the minimum num- ber of repeaters required.

<!-- b000005 | prose | pages [1] -->
In the “Bender” Snaking Model, a network is established by creating a “snake” or chain of open repeaters across the area. The model determines the most eﬀective placement for each open repeater and is mindful to maintain channel availability cy placing CTCSS repeaters when necessary.

<!-- b000006 | prose | pages [1] -->
In the Branching Model, a backbone network is established between the two most populous areas and branch networks are subsequentially added to existing network. After the branched network has been completed, CTCSS lines are placed to both mitigate channel saturation and establish dedicated long-distance lines. This model seeks to create the best connectivity for the users in the area with the minimum number of repeaters used.

<!-- b000007 | prose | pages [1] -->
We test our models on two likely area distrubitions: a city/suburban-like user distribution and a rural-like user distribution. We compare the results and propose the minimum number of repeaters necessary for each scenario. By comparing the two models, we are able to decide if the number is realistic and what the beneﬁts of a diﬀerent network design may correlate to for the users.

<!-- b000008 | prose | pages [1] -->
Finally, we stress-test our models with 10,000 users in the same area and discuss the defects of line-of-sight propagation caused by mountains in the area.

<!-- b000009 | contents | pages [2] -->
Optimizing VHF Repeater Coordination Using Cluster

<!-- b000010 | contents | pages [2] -->
Analysis

<!-- b000011 | contents | pages [2] -->
MCM Competition Problem B

<!-- b000012 | contents | pages [2] -->
Control Number: 11759

<!-- b000013 | heading | pages [2] -->
Contents

<!-- b000014 | contents | pages [2] -->
1 Problem Restatement

<!-- b000015 | contents | pages [2] -->
4

<!-- b000016 | contents | pages [2] -->
2 Assumptions and Justiﬁcations

<!-- b000017 | contents | pages [2] -->
4

<!-- b000018 | contents | pages [2] -->
3 Available Technology

<!-- b000019 | contents | pages [2] -->
5

<!-- b000020 | contents | pages [2] -->
3.1

<!-- b000021 | contents | pages [2] -->
Repeaters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000022 | contents | pages [2] -->
5

<!-- b000023 | contents | pages [2] -->
3.2

<!-- b000024 | contents | pages [2] -->
Continuous Tone-Coded Squelch System

<!-- b000025 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
6

<!-- b000027 | contents | pages [2] -->
4 The “Bender” Snake Model

<!-- b000028 | contents | pages [2] -->
6

<!-- b000029 | contents | pages [2] -->
4.1

<!-- b000030 | contents | pages [2] -->
Description

<!-- b000031 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
7

<!-- b000033 | contents | pages [2] -->
4.2

<!-- b000034 | contents | pages [2] -->
Mathematical Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
7

<!-- b000036 | contents | pages [2] -->
5 The Branching Model

<!-- b000037 | contents | pages [2] -->
11

<!-- b000038 | contents | pages [2] -->
5.1

<!-- b000039 | contents | pages [2] -->
Description

<!-- b000040 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
11

<!-- b000042 | contents | pages [2] -->
5.2

<!-- b000043 | contents | pages [2] -->
Mathematical Intepretation

<!-- b000044 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
12

<!-- b000046 | contents | pages [2] -->
6 Model Comparison Summary

<!-- b000047 | contents | pages [2] -->
14

<!-- b000048 | contents | pages [2] -->
2

<!-- b000049 | furniture | pages [3] -->
Control Number: 11759

<!-- b000050 | furniture | pages [3] -->
Page 3 of 51

<!-- b000051 | heading | pages [3] -->
7 Case Studies

<!-- b000052 | prose | pages [3] -->
15

<!-- b000053 | prose | pages [3] -->
7.1 City Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

<!-- b000054 | prose | pages [3] -->
7.2 Rural Distrubition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

<!-- b000055 | prose | pages [3] -->
8 10,000 Simultaneous Users 22

<!-- b000056 | heading | pages [3] -->
9 Mountainous Terrain

<!-- b000057 | prose | pages [3] -->
23

<!-- b000058 | heading | pages [3] -->
10 Sensitivity to Parameters

<!-- b000059 | prose | pages [3] -->
24

<!-- b000060 | heading | pages [3] -->
11 Strengths & Weaknesses

<!-- b000061 | prose | pages [3] -->
25

<!-- b000062 | heading | pages [3] -->
12 Conclusion

<!-- b000063 | prose | pages [3] -->
26

<!-- b000064 | heading | pages [3] -->
13 Appendix A: Full-Page Plots

<!-- b000065 | prose | pages [3] -->
29

<!-- b000066 | heading | pages [3] -->
14 Appendix B: Source Code

<!-- b000067 | prose | pages [3] -->
36

<!-- b000068 | furniture | pages [4] -->
Control Number: 11759

<!-- b000069 | furniture | pages [4] -->
Page 4 of 51

<!-- b000070 | heading | pages [4] -->
1 Problem Restatement

<!-- b000071 | prose | pages [4] -->
Without the aid of repeaters, VHF radio would only permit low-power users to commu- nicate when direct line-of-sight could be established between the transmitter and receiver. Repeaters alleviate this restriction by amplifying and rebroadcasting these signals in order to make them available to a larger geographical area. By accounting for mutual repeater interference due to geographical proximity and utilizing a “continuous tone-coded squelch system” (CTCSS) or “private line” (PL), we seek to ﬁnd the minimal number of repeaters required to support 1,000 simultaneous users. The users inhabit a 40 mile radius ﬂat cir- cular area and are permitted to broadcast between 145-148 MHz. The repeaters transmit frequency is 600 kHz above or below the received frequency and 54 diﬀerent CTCSS tones are available. We then examine how our model adapts to accommodate 10,000 users and consider the potential defects of line-of-sight propagation in the presence of mountainous areas.

<!-- b000072 | heading | pages [4] -->
2 Assumptions and Justiﬁcations

<!-- b000073 | prose | pages [4] -->
• Geometry is Euclidean. Since the area is given to be ﬂat, we assume that Euclidean geometry may be used.

<!-- b000074 | prose | pages [4] -->
• The system is closed. We assume that all signals originate from within our system.

<!-- b000075 | prose | pages [4] -->
We also assume that there will be no outside interference in the system.

<!-- b000076 | prose | pages [4] -->
• Antennas are isotropic. Because the eﬀective transmission area of each user and each antenna is relatively small compared to the whole area, we assume that antennas operate isotropically. This is a fundamental assumption made in modern network design [4].

<!-- b000077 | prose | pages [4] -->
• Each user is a “low-power” user. Typical VHF radio transmitters are eﬀective across small towns without repeater support [8]. Since the area being considered is over 5000 square miles, the area of a small town is negligible and we can assume that users will not be able to communicate with one another without repeater support, i.e.

<!-- b000078 | prose | pages [4] -->
each user is a low-power user.

<!-- b000079 | prose | pages [4] -->
• Each user “plays nice.” In order to avoid users purposefully or accidentally drown- ing out the signals of others, we require that all users have the same equipment, e.g.

<!-- b000080 | prose | pages [4] -->
all users broadcast at the same intensity and all users have the same range limitations.

<!-- b000081 | prose | pages [4] -->
As a result, the requirements to connect a single user will be static. Speciﬁcally, each users will have to be within some ﬁxed maximum distance from a repeater to connect to the network.

<!-- b000082 | prose | pages [4, 5] -->
• There are more than 1,000 (or 10,000) potential users. It would be unrealistic for any company or group of individuals to place an appreciable number of repeaters in order to accommodate one individual. We assume that the number of potential users in the area exceeds the number that must be simultaneously accomodated.

<!-- b000083 | furniture | pages [5] -->
Control Number: 11759

<!-- b000084 | furniture | pages [5] -->
Page 5 of 51

<!-- b000086 | prose | pages [5] -->
• The geographic distribution of users is known. The geographical distribution of users must be a known constraint before repeater requirements can be determined. The demand for network connectivity will not exist unless there is a preexisting community present.

<!-- b000087 | prose | pages [5] -->
• Users and repeaters are distinct entities. In reality, most VHF radio repeaters are maintained by individual users or a localized group of users. These repeaters are openly available and are typically not used as mobile stations [9]. Thus we assume that users are not broadcasting from repeaters and that they may be treated as two distinct entities.

<!-- b000088 | prose | pages [5] -->
• VHF signals are not aﬀected by physical entities in the area. The physical presence of users and antennas will not interfere with the propagation of waves in the VHF spectrum. However, land features such as mountains will aﬀect propagation [11].

<!-- b000089 | heading | pages [5] -->
3 Available Technology

<!-- b000090 | prose | pages [5] -->
The problem statement makes two diﬀerent pieces of technology available: repeaters and continuous tone-coded squelch systems. We will now outline these technologies.

<!-- b000091 | heading | pages [5] -->
3.1 Repeaters

<!-- b000092 | prose | pages [5] -->
Repeaters are stationary devices that pick up weak signals (i.e. signals from users), amplify them, and retransmit them on a diﬀerent frequency. This allows users to circumvent the line- of-sight limitation of VHF and broadcast their signal greater distances. To avoid inteference with the incoming (weak) signal, the repeater rebroadcasts the new (strong) signal 600 kHz above or below the received signal. To avoid repeaters interfering with one another the Metropolitan Coordination Association states that repeaters must be at least 10 miles apart [1]. Overlapping repeater “zones” will allow signals to pass from one repeater to another, allowing signals to travel signiﬁcant distances.

<!-- b000093 | prose | pages [5] -->
Note that the range of a repeater is directly correlated to its height. The line-of-sight p calculation to determine the eﬀectve distance is given by disance in miles = 1.5Af, where Af is the height of the antenna in feet [11].

<!-- b000094 | furniture | pages [6] -->
Control Number: 11759

<!-- b000095 | furniture | pages [6] -->
Page 6 of 51

<!-- b000096 | heading | pages [6] -->
3.2 Continuous Tone-Coded Squelch System

<!-- b000097 | prose | pages [6] -->
Continuous Tone-Coded Squelch Systems (CTCSS), often called Private Lines (PL), further mitigates interference by associating a subaudible tone with signals being received/transmit- ted by the repeater. In order to communicate through a private line repeater, users must also broadcast this tone. This allows users in a densely populated area to communicate on the same channel with minimal interference. Private line repeaters are not necessarily closed [2] as these CTCSS tones are often published. Since it is our intention to increase the number of available channels, CTCSS tones will be common knowledge to all users.

<!-- b000098 | heading | pages [6] -->
4 The “Bender” Snake Model

<!-- b000099 | prose | pages [6] -->
The “Bender1” Snake Model seeks to maximize the number of connected users by eﬃciently creating a snake-like chain of open repeaters across the area.

<!-- b000100 | caption | pages [6] -->
Figure 1 describes this model without reclustering.

<!-- b000101 | prose | pages [6] -->
Create and Score Clusters

<!-- b000102 | prose | pages [6] -->
Place 1st Repeater (Open)

<!-- b000103 | prose | pages [6] -->
Enough yes End of Users & Method Channels?

<!-- b000104 | prose | pages [6] -->
no

<!-- b000105 | prose | pages [6] -->
Add Place New Enough Repeater Repeater no Channels? (PL) (Open)

<!-- b000106 | prose | pages [6] -->
yes Find Optimal Direction

<!-- b000107 | caption | pages [6] -->
Figure 1: Flow Chart for “Bender” Snake Model

<!-- b000108 | prose | pages [6] -->
1Named after Bender, a team member’s dog who has a habit of snaking around doors, corners and furniture.

<!-- b000109 | furniture | pages [7] -->
Control Number: 11759

<!-- b000110 | furniture | pages [7] -->
Page 7 of 51

<!-- b000111 | heading | pages [7] -->
4.1 Description

<!-- b000112 | prose | pages [7] -->
Using k-means clustering[10], we establish clusters of users to deterrmine the optimal initial open repeater placement. Optimal placement is determined by the greatest number of users we can cover when placing a single open repeater. This may also be referred to as “scoring” a cluster where a higher score correlates to coverage for more users. A second open repeater is optimally placed along the perimeter of the newly established network area. This process is repeated iteravely by placing a new open repeater along the permitter of the most recently established open repeater. The placement of the second open repeater is always in the direction of a cluster point, i.e. other high density locations. This ensures that a network is established between the most users using the least number of repeaters. The model is mindful of ensuring that enough channels are available to users by placing CTCSS repeaters accordingly.

<!-- b000113 | prose | pages [7] -->
By design, network growth tends toward establishing connectivity near and between cluster points. As more users around each cluster are accomodated, the score associated with their respective cluster should reﬂect that change. To account for this, cluster scores may be reevaluated to encourage intelligent networking in the model. This is known as reclustering.

<!-- b000114 | heading | pages [7] -->
4.2 Mathematical Interpretation

<!-- b000115 | prose | pages [7] -->
The model is designed to be highly versatile and supports a number of diﬀerent parameters that may be changed based on a given situation. They are:

<!-- b000116 | prose | pages [7] -->
Parameter Description n Number of users within 40 miles k Number of k-means cluster points ds Maximum distance for user-to-repeater communication hr Height of repeater towers dh Repeater output distance ∆f Frequency separation / channel width

<!-- b000117 | prose | pages [7] -->
Before we begin, we must deﬁne a few additional terms. Let Nc be the number of people with network connectivity (i.e. within range of an open repeater) and let Nf be the number of people with access to an available frequency range. Let O denote the number of available channels. Initially, we will have Nc = 0, Nf = 0 and O = 0.

<!-- b000118 | prose | pages [7] -->
So let n be the number of users within the 40 mile radius. For user i with 1 ≤i ≤n, let (xi, yi) denote the user’s location in Cartesian coordinates. We arrange these coordinates into an n × 2 matrix M where

<!-- b000119 | prose | pages [7] -->
Mj,1 = xj and Mj,2 = yj for all integers j ∈[1, n].

<!-- b000120 | furniture | pages [8] -->
Control Number: 11759

<!-- b000121 | furniture | pages [8] -->
Page 8 of 51

<!-- b000122 | prose | pages [8] -->
For each user, determine the number of users within the seperation distance ds. Recall that we are using Euclidean geometry, so when considering the jth user if

<!-- b000123 | prose | pages [8] -->
q (Mj,1 −Mk,1)2 −(Mj,2 −Mk,2)2 ds ≥

<!-- b000124 | prose | pages [8] -->
then the kth user is within range of the jth user. We denote the user with the greatest number of additional users in range as the pth user.

<!-- b000125 | prose | pages [8] -->
We place an open repeater at the location of the pth user and set R1 = (Mp,1, Mp,2). The allowable frequency range is 3 MHz so there will be 3/∆f channels available. The action of placing the ﬁrst repeater makes this many channels available. Now O = 3/∆f.

<!-- b000126 | prose | pages [8] -->
Let N1 be the number of people who are within range of our ﬁrst repeater. We must update our Nc and Nf values accordingly. Thus

<!-- b000127 | prose | pages [8] -->
Nc = N1 and Nf = min(Nc, O)

<!-- b000128 | prose | pages [8] -->
Now we calculate the metric by which this model determines Private Line (CTCSS) repeater placement. Let

<!-- b000129 | prose | pages [8] -->
D = max(Nc −O, 0)

<!-- b000130 | prose | pages [8] -->
be the deﬁcit of available channels (i.e. the number of users who do not have access to a repeater channel). We update our matrix M by removing the users who are within range of the repeater. Now M is a (n −Nc) × 2 matrix. From here, if D > 0 we add CTCSS repeaters to mitigate this deﬁcit and if D = 0, we continue to place open repeaters and expand the network.

<!-- b000131 | prose | pages [8] -->
If D > 0, we will add a Private (CTCSS) Line. We calculate the optimal angle to place the CTCSS line a distance of dp from our ﬁrst repeater. We then determine the location to place the CTCSS repeater.

<!-- b000132 | prose | pages [8] -->
The explicit CTCSS algorithm is given below.

<!-- b000133 | furniture | pages [9] -->
Control Number: 11759

<!-- b000134 | furniture | pages [9] -->
Page 9 of 51

<!-- b000135 | prose | pages [9] -->
Data: Previously placed open repeater location, Ri−1 Result: The optimal location to place a new CTCSS Line Ri = (xi, yi) Let P be a partition of [0, 360] (in our case studies |P| = 360);

<!-- b000136 | prose | pages [9] -->
for θ ∈P do Rθ = (xθ, yθ) = Ri−1 + (dp cos(θ), dp sin(θ));

<!-- b000137 | prose | pages [9] -->
for j ∈[1, n −Nc] do Let xj = Mj,1 and yj = Mj,2; (xθ −xj)2 + (yθ −yj)2 ≤ds then p if uθ = uθ + 1;

<!-- b000138 | prose | pages [9] -->
end end end Let θc be the θ for which uθ is maximum. Then Ri = Ri−1 + ( dp cos(θc), dp sin(θc) ) is the optimal location for the new repeater.

<!-- b000139 | heading | pages [9] -->
Algorithm 1: Finding CTCSS Repeater Location

<!-- b000140 | prose | pages [9] -->
The addition of a CTCSS line corresponds to an additional 3/∆f channels. Therefore our new value for O is O = O′ + 3/∆f where O′ is the previous value of O. Now we recalculate Nc, Nf, and our deﬁcit D using our updated matrix M (which does not include points already covered by repeaters).

<!-- b000141 | prose | pages [9] -->
If D = 0 then all users who desire access have access. To increase the number of supported users, we will add an open repeater to expand our network. We use “k-means” cluster analysis to determine the most densly populated areas. After the cluster points are determined, we collect their locations and let {c1, ..., ck} be that collection of coordinates. The model snakes around the map by adding repeaters to include more users in the network.

<!-- b000142 | prose | pages [9] -->
The explicit open repeater placement algorithm is given below.

<!-- b000143 | prose | pages [9] -->
Data: Previously placed open repeater location, Ri−1 Result: The optimal location to place a new open repeater Ri = (xi, yi) for t ∈[0, k] do Let θt be the angle from the current repeater Ri−1 to ct;

<!-- b000144 | prose | pages [9] -->
Rt = (xt, yt) = Ri−1 + (dh cos(θt), dh sin(θt));

<!-- b000145 | prose | pages [9] -->
for j ∈[0, n −Nc] do Let xj = Mj,1 and yj = Mj,2; (xt −xj)2 + (yt −yj)2 ≤ds then p if ut = ut + 1;

<!-- b000146 | prose | pages [9] -->
end end end Let tc be the t for which ut is maximum. Then Ri = Ri−1 + (dh cos(θtc), dh sin(θtc)) is the optimal location for the new repeater.

<!-- b000147 | heading | pages [9] -->
Algorithm 2: Finding Open Repeater Location

<!-- b000148 | furniture | pages [10] -->
Control Number: 11759

<!-- b000149 | furniture | pages [10] -->
Page 10 of 51

<!-- b000150 | prose | pages [10] -->
The action of adding an open line did not add any new channels. We have, however, added new users to the network and must recalculate Nc, Nf, and our deﬁcit D using our updated matrix M (which does not include points already covered by repeaters). If D > 0, then we apply Algorithm 1 again and if D = 0, we apply Algorithm 2.

<!-- b000151 | prose | pages [10] -->
We repeat this process until Nf ≥1000. This would mean that there are at least 1,000 simultaneously supported users on our network.

<!-- b000152 | furniture | pages [11] -->
Control Number: 11759

<!-- b000153 | furniture | pages [11] -->
Page 11 of 51

<!-- b000154 | heading | pages [11] -->
5 The Branching Model

<!-- b000155 | prose | pages [11] -->
The aptly named Branching Model creates a backbone network of open repeaters that sup- ports a number of branch connections. All open repeater branches are designed along the shortest distance possible. This model provides us with a point of comparison for the ﬁrst model.

<!-- b000156 | caption | pages [11] -->
Figure 2 describes the creation of the backbone and branches.

<!-- b000157 | prose | pages [11] -->
Create and Score Clusters

<!-- b000158 | prose | pages [11] -->
Create Backbone Network (Open)

<!-- b000159 | prose | pages [11] -->
Recreate and Rescore Clusters no

<!-- b000160 | prose | pages [11] -->
Connect Highest Enough Score Users?

<!-- b000161 | prose | pages [11] -->
Cluster yes

<!-- b000162 | prose | pages [11] -->
Add yes Enough End of Repeater no Channels? Method (PL)

<!-- b000163 | caption | pages [11] -->
Figure 2: Flow Chart for Branching Model

<!-- b000164 | heading | pages [11] -->
5.1 Description

<!-- b000165 | prose | pages [11, 12] -->
Akin to the ﬁrst model, the Branching Method uses k-means cluster analysis and scoring to determine the optimal placement of repeaters. The diﬀerence, however, is the process in which this model creates the network. The model creates a backbone network of open repeaters between the two highest scoring clusters. After the backbone has been estab- lished, the model reclusters and rescores the remaining users and creates a branch of open repeaters between the existing network and the highest scoring cluster. This ensures that the fewest repeaters are used in branching out the network to high density locations. After the entire network has been established, the model places CTCSS repeaters to ensure chan- nel availability is not a concern in user-dense locations so that all users may be supported simultaneously.

<!-- b000166 | furniture | pages [12] -->
Control Number: 11759

<!-- b000167 | furniture | pages [12] -->
Page 12 of 51

<!-- b000169 | prose | pages [12] -->
This model requires reclustering after every iteration.

<!-- b000170 | heading | pages [12] -->
5.2 Mathematical Intepretation

<!-- b000171 | prose | pages [12] -->
The Branching Model supports even more customization than the ﬁrst model. The param- eters relevant to this model are listed below.

<!-- b000172 | prose | pages [12] -->
Parameter Description n Number of users within 40 miles k Number of k-means cluster points ds Maximum distance for user-to-repeater communication hr Height of repeater towers dh Repeater output distance ∆f Frequency separation/ channel width ln Number of Long Distance Lines lc Number of Locations in Long Distance Connections

<!-- b000173 | prose | pages [12] -->
We will review a few deﬁnitions for consistency. Let Nc be the number of people with network connectivity (i.e. within range of a repeater) and Nf be the number of people with access to an available frequency range. The number of channels available will be denoted again by O. Initially, Nc = 0, Nf = 0 and O = 0.

<!-- b000174 | prose | pages [12] -->
Let n be the number of users within a 40 mile radius. With k-means clustering, we identify and score clusters of users.. Letting {c1, ..., ck} be the locations of the k cluster points, the model creates a backbone of repeaters between the two highest scoring cluster locations.

<!-- b000175 | prose | pages [12] -->
For each cluster point ci, we calculate how many users are within ds of ci, i.e. how many users will beneﬁt from the placement of a repeater there. We set R1 = ci for whichever i has the most people within range. Now calculate Nc as before. The algorithm continues until the desired number of users have been added (in our case this is 1000 users). This only means that users are within range of a repeater. This does not ensure that all users have available channels. This will be resolved after the branched network has been established.

<!-- b000176 | prose | pages [12] -->
The explicit open repeater branching algorithm is given below.

<!-- b000177 | furniture | pages [13] -->
Control Number: 11759

<!-- b000178 | furniture | pages [13] -->
Page 13 of 51

<!-- b000179 | prose | pages [13] -->
Data: First open repeater location, R1 = (x, y)

<!-- b000180 | heading | pages [13] -->
Result: The locations of the repeaters

<!-- b000181 | prose | pages [13] -->
for i ∈[1, k] do Let (xi, yi) = ci;

<!-- b000182 | prose | pages [13] -->
(x −xi)2 + (y −yi)2; p φ(i) = end Then T = (xi, yi) st φ(i) = max(φ([1, k]));

<!-- b000183 | prose | pages [13] -->
θ = angle between R1,T;

<!-- b000184 | prose | pages [13] -->
s = distance between R1, T;

<!-- b000185 | prose | pages [13] -->
Set j = 2;

<!-- b000186 | prose | pages [13] -->
while s > dh do Rj = Rj−1 + (dh cos(θ), dh sin(θ));

<!-- b000187 | prose | pages [13] -->
Recalculate s;

<!-- b000188 | prose | pages [13] -->
j = j + 1;

<!-- b000189 | prose | pages [13] -->
end while Nc < 1000 do Rerun “k-means” cluster analysis to obtain new {c1, ..., ck};

<!-- b000190 | prose | pages [13] -->
T = ci st ci has the most users in range;

<!-- b000191 | prose | pages [13] -->
Choose i st Ri is the existing repeater closest to T;

<!-- b000192 | prose | pages [13] -->
Let s be the distance between RT and T;

<!-- b000193 | prose | pages [13] -->
Let θ be the distance between RT and T;

<!-- b000194 | prose | pages [13] -->
while s > dh do Rj = Rj−1 + (dh cos(θ), dh sin(θ));

<!-- b000195 | prose | pages [13] -->
Recalculate s;

<!-- b000196 | prose | pages [13] -->
j = j + 1;

<!-- b000197 | prose | pages [13] -->
end end

<!-- b000198 | heading | pages [13] -->
Algorithm 3: Branching Method Open Repeater Placement

<!-- b000199 | prose | pages [13] -->
With the open network established, we must resolve the issue of channel availability. This is easily accomplished by placement of CTCSS repeaters in high user density areas. In our opinion, the method in which this model establishes long-distance CTCSS lines is out- standing. By specifying a diﬀerent value for ln, one can change the number of CTCSS lines connecting the most highly populated areas. While this potentially increases the number of repeaters, it oﬀers greater connectivity between regions. This is accomplished by ﬁrst running k-means cluster analysis on the user data and choosing the lc clusters with the most users in range. Starting from the cluster with the most users, we create a chain of repeaters with a particular CTCSS channel, a distance of dh apart, until the next closest repeater is in range (similar to the second half of Algorithm 3). This creates a long distance connection on a speciﬁc CTCSS channel. This allows long distance users to communicate with more densely populated areas (e.g. rural or sub-urban users communicating with an urban user) without wasting an open frequency in the dense location.

<!-- b000200 | furniture | pages [14] -->
Control Number: 11759

<!-- b000201 | furniture | pages [14] -->
Page 14 of 51

<!-- b000202 | prose | pages [14] -->
Once the speciﬁed number of long distance connections have been made, any deﬁcits in channel demand are mitigated by placing local CTCSS repeaters in highly populated areas (again by k-means clustering).

<!-- b000203 | heading | pages [14] -->
6 Model Comparison Summary

<!-- b000204 | prose | pages [14] -->
The fundamental similarities and diﬀerences between the models are:

<!-- b000205 | prose | pages [14] -->
Similarities

<!-- b000206 | prose | pages [14] -->
• k-means clustering is prevalant in both models. Both models make use of k- means cluster analysis to identify large groups of users. By ranking these clusters in terms of potential connected users, both models attempt to provide the most eﬃcient connectivity scheme possible.

<!-- b000207 | prose | pages [14] -->
• Variable-strength repeaters may be employed in both models. By accounting for variable broadcasting strength, isolated users may be accomodated without fear of channel interference or an inordinate use of additional repeaters in both models.

<!-- b000208 | prose | pages [14] -->
• The change of frequency from a repeater (±600 kHz) is resolved last in both models. After the repeaters are conﬁgured, the “up” and “down” repeater broadcast assignments may be made in both models to ﬁt the speciﬁc conﬁguration of the network.

<!-- b000209 | prose | pages [14] -->
Diﬀerences

<!-- b000210 | prose | pages [14] -->
• The models generate the network diﬀerently. The “Bender” Snake Model places open repeaters along a continuous trajectory as determined by cluster points. In con- trast, The Branching Model creates a single backbone and allows for growth in any direction toward a cluster point.

<!-- b000211 | prose | pages [14] -->
• Reclustering is required for the Branching Model. In order for branching to occur, the optimum target location must be determined after every iteration. The other model may utilize reclustering but does not require it.

<!-- b000212 | prose | pages [14] -->
• The method in which private lines are introduced diﬀers between the mod- els. The “Bender” Snake Model places private line repeaters as is necessary whereas the Branching Model places private line repeaters after the entire network has been established.

<!-- b000213 | furniture | pages [15] -->
Control Number: 11759

<!-- b000214 | furniture | pages [15] -->
Page 15 of 51

<!-- b000215 | heading | pages [15] -->
7 Case Studies

<!-- b000216 | prose | pages [15] -->
We developed two population distributions to test our models on. The two cases are: a city- like user distribution and a rural distribution with small towns of users. When we discuss “parity,” we refer to the ±600 kHz diﬀerence in the recieving and broadcast frequencies of the repeaters. The graphs that show these assignments represent each open line repeater as a node, each labeled with “+” or “-” accordingly. We assign parity to each repeater such that no one repeater is connected to the rest of the network solely through another repeater with identical parity. This prevents a signal being either stepped up or stepped down repeatedly such that it eventually falls outside the available frequency range and cannot be recieved.

<!-- b000217 | prose | pages [15] -->
The parameters for these case studies were set to values we deemed reasonable based on our research from our referenced sources.

<!-- b000218 | heading | pages [15] -->
7.1 City Distribution

<!-- b000219 | prose | pages [15] -->
This distribution represents a city (located at the center of the area) with surrounding suburbs/neighborhoods.

<!-- b000220 | caption | pages [15] -->
Figure 3: Surface Plot of Users

<!-- b000221 | furniture | pages [16] -->
Control Number: 11759

<!-- b000222 | furniture | pages [16] -->
Page 16 of 51

<!-- b000223 | heading | pages [16] -->
Snaking Model

<!-- b000224 | prose | pages [16] -->
Parameter Description n = 1400 The number of users within 40mi k = 5 Number of k-means cluster points ds = 10mi Maximum distance for user to repeater communication hr = 150ft Height of repeater towers to be placed Repeater output distance2) dh = 15mi ∆f = .025 Frequency seperation ln = 3 Number of Long Distance Lines lc = 5 Number of Locations in Long Distance Connections

<!-- b000225 | prose | pages [16] -->
The model places the ﬁrst open repeater slightly north of the city to cover most of the users located there. This creates a large channel deﬁcit and the model places two CTCSS repeaters on this iteration to compensate. Next, a repeater is placed to the northwest and the simulation proceeds to spiral counterclockwise around the city, placing CTCSS repeaters as necessary. The model also places two CTCSS repeaters on the fourth iteration. There are 9 open line repeaters and 8 CTCSS repeaters for a total of 17 repeaters.

<!-- b000226 | prose | pages [16] -->
"Bender" Snaking Method Repeater Placement 40

<!-- b000227 | prose | pages [16] -->
30

<!-- b000228 | prose | pages [16] -->
20

<!-- b000229 | prose | pages [16] -->
10

<!-- b000230 | prose | pages [16] -->
Miles 0

<!-- b000231 | prose | pages [16] -->
−10

<!-- b000232 | prose | pages [16] -->
−20

<!-- b000233 | prose | pages [16] -->
−30

<!-- b000234 | prose | pages [16] -->
Potential User Open Repeater CTCSS Repeater Cluster Pt −40 −40 −30 −20 −10 0 10 20 30 40 Miles

<!-- b000235 | caption | pages [16] -->
Figure 4: Repeater Placement (Snaking Model)

<!-- b000236 | prose | pages [16] -->
The model creates a closed loop of 9 open line repeaters. Since this number is odd, the parity does not work bi-directionally around the loop. There will be some signal leakage when the two step-up repeaters communicate directly but the signal will travel in the opposite direction around the entire network and be recieved.

<!-- b000237 | furniture | pages [17] -->
Control Number: 11759

<!-- b000238 | furniture | pages [17] -->
Page 17 of 51

<!-- b000239 | prose | pages [17] -->
+

<!-- b000240 | prose | pages [17] -->
- + -

<!-- b000241 | prose | pages [17] -->
+ - +

<!-- b000242 | prose | pages [17] -->
+ -

<!-- b000243 | caption | pages [17] -->
Figure 5: Repeater Parity (Snaking Model)

<!-- b000244 | heading | pages [17] -->
Branching Model

<!-- b000245 | prose | pages [17] -->
The model places the ﬁrst open repeater in the city and creates three main branches to cover the surrounding suburbia. This web structure is highlighed with the black lines. The branching structure of open line repeaters is designed to eﬃciently cover the surface area rather than simply rushing from one population center to the next linearly. This structure is created ﬁrst, and CTCSS lines are placed afterwords.

<!-- b000246 | prose | pages [17] -->
Branching Method Repeater Placement 40

<!-- b000247 | prose | pages [17] -->
30

<!-- b000248 | prose | pages [17] -->
20

<!-- b000249 | prose | pages [17] -->
10

<!-- b000250 | prose | pages [17] -->
Miles 0

<!-- b000251 | prose | pages [17] -->
−10

<!-- b000252 | prose | pages [17] -->
−20

<!-- b000253 | prose | pages [17] -->
−30

<!-- b000254 | prose | pages [17] -->
Potential User Open Repeater CTCSS Repeater −40 −40 −30 −20 −10 0 10 20 30 40 Miles

<!-- b000255 | caption | pages [17] -->
Figure 6: Repeater Placement (Branching Model)

<!-- b000256 | prose | pages [17, 18] -->
The process of CTCSS repeater placement is designed to create higher connectivity than the Snaking model. In the Snaking model, CTCSS repeaters are used to provide more channels locally, but when the network is loaded to capacity not all users will be able to talk long- distance. In the Branching model, we assign one squelch tone as long distance, here denoted by 1 (blue circles). Each of these points has 3 CTCSS repeaters, denoted as types 1,2 and 3. Tones 4-8 provide local lines in a manner similar to Snaking. This model creates 8 open Branching Method CTCSS Repeater Subaudible Channel Arrangment 40

<!-- b000257 | furniture | pages [18] -->
Control Number: 11759

<!-- b000258 | furniture | pages [18] -->
Page 18 of 51

<!-- b000260 | prose | pages [18] -->
30

<!-- b000261 | prose | pages [18] -->
7 20

<!-- b000262 | prose | pages [18] -->
1 10 5 1 Miles 8 0 1 4

<!-- b000263 | prose | pages [18] -->
6 −10 1

<!-- b000264 | prose | pages [18] -->
−20 1

<!-- b000265 | prose | pages [18] -->
−30

<!-- b000266 | prose | pages [18] -->
Potential User CTCSS Repeater −40 −40 −30 −20 −10 0 10 20 30 40 Miles

<!-- b000267 | caption | pages [18] -->
Figure 7: CTCSS Line Placement (Branching Model)

<!-- b000268 | prose | pages [18] -->
repeaters and 17 CTCSS repeaters for a total of 26. This number is substantually higher than the “minimum number” of 17 that the Snaking model produced. These extra lines are necessitated by the long distance backbone. The aim of this model is to provide both the best connectivity with the fewest number of repeaters.

<!-- b000269 | prose | pages [18] -->
The parity assignment is quite simple here.

<!-- b000270 | prose | pages [18] -->
+ + - -

<!-- b000271 | prose | pages [18] -->
+ - -

<!-- b000272 | prose | pages [18] -->
+ -

<!-- b000273 | caption | pages [18] -->
Figure 8: Repeater Parity (Branching Model)

<!-- b000274 | furniture | pages [19] -->
Control Number: 11759

<!-- b000275 | furniture | pages [19] -->
Page 19 of 51

<!-- b000276 | heading | pages [19] -->
7.2 Rural Distrubition

<!-- b000277 | prose | pages [19] -->
This distribution represents a rural area with eight small towns of concentrated population with approximately 100 people spread randomly throughout the area. The total user popu- lation is 1400. We attempt to provide connectivity to 1000 people using both the Snaking and Branching models.

<!-- b000278 | caption | pages [19] -->
Figure 9: Surface Plot of Users

<!-- b000279 | heading | pages [19] -->
Snaking Model

<!-- b000280 | prose | pages [19] -->
The model starts near the northwestern-most town. We note that it places the open-line repeater so that it covers all of the targeted town but approximately half of the population in the second town. This coverage is optimal, however a connectivity deﬁcit is created since more than 120 people lie within range and channel availability becomes an issue. The model then places a CTCSS repeater near the open repeater to provide more channels locally. This is not suﬃcient to cover the deﬁcit, so the model places an additional CTCSS repeater on the same spot, this one with a diﬀerent squelch tone. This resolves the deﬁcit so it resumes placing open-line repeaters. The next placement is essentially due south of the previous, as it gravitates towards the two southern clusters that represent the two towns in the area. The placement of this new repeater does not create a channel deﬁcit so there is no need for another CTCSS repeater. The model proceeds south again on the next iteration, then snakes around towards the southeastern town, and ﬁnally turns north, placing CTCSS repeaters as needed along the way. The open line repeater near the middle is placed last. Note that the 6th iteration (the southeastern most group) also places two CTCSS repeaters on the same spot for a total of 8 CTCSS repeaters and 10 open repeaters. The model uses 18 total repeaters to create a network that accomodates 1080 users.

<!-- b000281 | furniture | pages [20] -->
Control Number: 11759

<!-- b000282 | furniture | pages [20] -->
Page 20 of 51

<!-- b000283 | prose | pages [20] -->
"Bender" Snaking Method Repeater Placement 40

<!-- b000284 | prose | pages [20] -->
30

<!-- b000285 | prose | pages [20] -->
20

<!-- b000286 | prose | pages [20] -->
10

<!-- b000287 | prose | pages [20] -->
Miles 0

<!-- b000288 | prose | pages [20] -->
−10

<!-- b000289 | prose | pages [20] -->
−20

<!-- b000290 | prose | pages [20] -->
−30

<!-- b000291 | prose | pages [20] -->
Potential User Open Repeater CTCSS Repeater Cluster Pt −40 −40 −30 −20 −10 0 10 20 30 40 Miles

<!-- b000292 | caption | pages [20] -->
Figure 10: Repeater Placement (Snaking Model)

<!-- b000293 | prose | pages [20] -->
Repeater parity is assigned after the simulation is complete. This is generally a simple process for the Snaking model. However, note the southeastern node group where there are two step up repeaters connected. While this will result in some signal leakage outside of the available spectrum, the path that involves the step down node allows these two step up nodes to communicate without signal loss.

<!-- b000294 | prose | pages [20] -->
+

<!-- b000295 | prose | pages [20] -->
- + +

<!-- b000296 | prose | pages [20] -->
+ -

<!-- b000297 | prose | pages [20] -->
- +

<!-- b000298 | prose | pages [20, 21] -->
+ - Branching Method The branching structure is highlighted with the black lines. The four-long node line that connects the two biggest towns is the main spine, and all other node structures branch oﬀof this. The branching structure of open line repeaters is designed to eﬃciently cover the surface area rather than simply rushing from one population center to the next linearly. This structure is created ﬁrst, and CTCSS lines are placed afterwords.

<!-- b000299 | caption | pages [20] -->
Figure 11: Repeater Parity (Snaking Model)

<!-- b000300 | furniture | pages [21] -->
Control Number: 11759

<!-- b000301 | furniture | pages [21] -->
Page 21 of 51

<!-- b000303 | prose | pages [21] -->
Branching Method Repeater Placement 40

<!-- b000304 | prose | pages [21] -->
30

<!-- b000305 | prose | pages [21] -->
20

<!-- b000306 | prose | pages [21] -->
10

<!-- b000307 | prose | pages [21] -->
Miles 0

<!-- b000308 | prose | pages [21] -->
−10

<!-- b000309 | prose | pages [21] -->
−20

<!-- b000310 | prose | pages [21] -->
−30

<!-- b000311 | prose | pages [21] -->
Potential User Open Repeater CTCSS Repeater −40 −40 −30 −20 −10 0 10 20 30 40 Miles

<!-- b000312 | caption | pages [21] -->
Figure 12: Repeater Placement (Branching Model)

<!-- b000313 | prose | pages [21] -->
CTCSS Subaudible Channel Arrangement 40

<!-- b000314 | prose | pages [21] -->
30

<!-- b000315 | prose | pages [21] -->
20 7 6 1

<!-- b000316 | prose | pages [21] -->
10 1 5 Miles 0 1

<!-- b000317 | prose | pages [21] -->
−10

<!-- b000318 | prose | pages [21] -->
1

<!-- b000319 | prose | pages [21] -->
−20

<!-- b000320 | prose | pages [21] -->
8 1 4 −30

<!-- b000321 | prose | pages [21, 22] -->
Potential User Open Repeater CTCSS Repeater −40 −40 −30 −20 −10 0 10 20 30 40 Miles The process of CTCSS repeater placement is designed to create higher connectivity than the Snaking model. In the Snaking model, CTCSS repeaters are used to provide more channels locally, but when the network is loaded to capacity not all users will be able to talk long- distance. In the Branching model, we assign one squelch tone as long distance, here denoted by 1 (blue circles). Each of these points has 3 CTCSS repeaters, one each of types: 1, 2 and 3. Tones 4-8 provide local lines in a manner similar to the Snaking method. This model creates 8 open repeaters and 17 CTCSS repeaters for a total of 25. This number is substantually higher than the “minimum number” of 18 that the Snaking model produces. These extra lines are necessitated by the building of the long distance backbone. The aim of this model is to provide better connectivity, and not provide an absolute minimum repeater number.

<!-- b000322 | caption | pages [21] -->
Figure 13: CTCSS Line Placement (Branching Model)

<!-- b000323 | furniture | pages [22] -->
Control Number: 11759

<!-- b000324 | furniture | pages [22] -->
Page 22 of 51

<!-- b000326 | prose | pages [22] -->
+ + + -

<!-- b000327 | prose | pages [22] -->
-

<!-- b000328 | prose | pages [22] -->
+

<!-- b000329 | prose | pages [22] -->
- +

<!-- b000330 | caption | pages [22] -->
Figure 14: Repeater Parity (Branching Model)

<!-- b000331 | prose | pages [22] -->
Parity assignment for this model is fairly trivial.

<!-- b000332 | prose | pages [22] -->
8 10,000 Simultaneous Users

<!-- b000333 | prose | pages [22] -->
Our model is highly adaptable to varying situations and stresses. As such, when considering repeater placement for a network capable of simulateously supporting 10,000 users, we simply run our models against a data set with a little over 10,000 users (we use 12,000). Our models work exactly as before when trying to support 1,000 users. An important point to note however, is that the frequency seperation must be lowered to accomodate more users. We choose the frequency separation to be 10 kHz for 10,000 users (whereas before we chose 25 kHz for 1,000 users).

<!-- b000334 | prose | pages [22] -->
The minimum number of repeaters necessary to simulateously support 10,000 users is 19 open repeaters and 33 CTCSS repeaters all running on a diﬀerent CTCSS tone for a total of 42 repeaters. We conclude that even with 10,000 users, an eﬃcient network can be established within the constaints of the problem.

<!-- b000335 | furniture | pages [23] -->
Control Number: 11759

<!-- b000336 | furniture | pages [23] -->
Page 23 of 51

<!-- b000337 | prose | pages [23] -->
Snaking Method Repeater Placement (10k users) 40

<!-- b000338 | prose | pages [23] -->
30

<!-- b000339 | prose | pages [23] -->
20

<!-- b000340 | prose | pages [23] -->
10

<!-- b000341 | prose | pages [23] -->
Miles 0

<!-- b000342 | prose | pages [23] -->
−10

<!-- b000343 | prose | pages [23] -->
−20

<!-- b000344 | prose | pages [23] -->
−30

<!-- b000345 | prose | pages [23] -->
−40 −40 −30 −20 −10 0 10 20 30 40 Miles

<!-- b000346 | caption | pages [23] -->
Figure 15: Results for 10,000 Simultaneous Users

<!-- b000347 | heading | pages [23] -->
9 Mountainous Terrain

<!-- b000348 | prose | pages [23] -->
While VHF radio signals are blocked by large land structures, the line-of-sight propagation method also permits an increased eﬀective range when the height of the antenna is increased. As a result, the mountains could be used to our advantage by placing repeaters on top of them rather than around them. This is not a completely trivial ﬁx, however, as the new eﬀective distance is proportional to the square root of the antenna’s height. This would provide diminishing returns.

<!-- b000349 | prose | pages [23] -->
In the case where there is one large topographical peak (i.e. one large mountain peak), the obvious solution is to place one strong repeater on the mountain peak to provide the most coverage. However, now consider the case where this mountain does not have one discernable, well-deﬁned peak and the area containing these peaks is relatively large and wide-spread (i.e. a mountain range). These numerous peaks may block the signal from a single repeater on the mountain and may not be accessible from all surrounding areas. The strength of the signal may vary with the angle due to an uneven distribution of peaks and valleys in the mountain range. In this situation, we would use a multiple-repeater network conﬁgured around the base and valleys that naturally occur in the mountain range. This would circumvent the mountain range and allow for connectivity. However, this also eliminates the line-of-sight advantage that the mountain could provide. There would most likely be ways to leverage the height advantage the mountains provide on a case-by-case basis.

<!-- b000350 | furniture | pages [24] -->
Control Number: 11759

<!-- b000351 | furniture | pages [24] -->
Page 24 of 51

<!-- b000352 | heading | pages [24] -->
10 Sensitivity to Parameters

<!-- b000353 | prose | pages [24] -->
Number of Cluster Points Since our model so heavily relies upon k-means cluster anal- ysis, it is natural to wonder how the number of cluster points aﬀects model performance. By running our model with variable inital cluster points (k = 5, 10, 20) we are able to gauge whether this has a signiﬁcant impact on performance. We chose to use the rural population distrubition since it provided a more interesting analysis.

<!-- b000354 | prose | pages [24] -->
"Bender" Snaking Method Repeater Placement (k=20) "Bender" Snaking Method Repeater Placement (k=10) 40 40

<!-- b000355 | prose | pages [24] -->
30 30

<!-- b000356 | prose | pages [24] -->
20 20

<!-- b000357 | prose | pages [24] -->
10 10

<!-- b000358 | prose | pages [24] -->
Miles Miles 0 0

<!-- b000359 | prose | pages [24] -->
−10 −10

<!-- b000360 | prose | pages [24] -->
−20 −20

<!-- b000361 | prose | pages [24] -->
−30 −30

<!-- b000362 | prose | pages [24] -->
−40 −40 −40 −30 −20 −10 0 10 20 30 40 −40 −30 −20 −10 0 10 20 30 40 Miles Miles (a) k = 10 (b) k = 20

<!-- b000363 | caption | pages [24] -->
Figure 16: “Bender” Snaking Model Cluster Point Sensitivity Rural Case

<!-- b000364 | prose | pages [24] -->
When k = 5 or k = 10, the model determines that nine open line repeaters and eight CTCSS lines are necessary. When k = 20, the model requires eight open lines and eight CTCSS lines be available. We conclude that our model does not seem to be very sensitive to changes in the number of initial cluster points.

<!-- b000365 | prose | pages [24] -->
Seperation Distance When determining optimal placement for repeaters, our model places each repeater a distance of dh apart so that repeater connectivity and communi- cation is guaranteed. The value we use for dh will have a large inﬂuence on the performance of the model. In our case studies, we set dh = 15. This is the distance that a 150 ft repeater would be able to transmit its signal. For dh = 10 and dh = 20, the height of the necessary repeater is 66 ft. 8 in. and 266 ft. 8 in. respectively.

<!-- b000366 | prose | pages [24] -->
dh Tower Height (ft) Open 10 66’ 10 15 150’ 8 20 266’ 7

<!-- b000367 | prose | pages [24, 25] -->
Clearly, tower height (and hence seperation distance) has a signiﬁcant impact on model performance. However, while increasing the tower height does decrease the minimum number Branching Method Repeater Placement (d=20) Branching Method Repeater Placement (d=10) 40 40

<!-- b000368 | furniture | pages [25] -->
Control Number: 11759

<!-- b000369 | furniture | pages [25] -->
Page 25 of 51

<!-- b000371 | prose | pages [25] -->
30 30

<!-- b000372 | prose | pages [25] -->
20 20

<!-- b000373 | prose | pages [25] -->
10 10

<!-- b000374 | prose | pages [25] -->
Miles Miles 0 0

<!-- b000375 | prose | pages [25] -->
−10 −10

<!-- b000376 | prose | pages [25] -->
−20 −20

<!-- b000377 | prose | pages [25] -->
−30 −30

<!-- b000378 | prose | pages [25] -->
−40 −40 −40 −30 −20 −10 0 10 20 30 40 −40 −30 −20 −10 0 10 20 30 40 Miles Miles (a) d = 10 (b) d = 20

<!-- b000379 | caption | pages [25] -->
Figure 17: Branching Model Seperation Distance Sensitivity Rural Case

<!-- b000380 | prose | pages [25] -->
of repeaters necessary, it will increase the cost of each repeater. This is a choice the user will have to make.

<!-- b000381 | prose | pages [25] -->
Initial Number of People Our algorithms run until the desired number of people are connected to the network and there are enough channels available to those people. Changing the starting population of users drastically impacts model performance. This is not surprising as a higher population would allow our model to capture the desired number of people faster.

<!-- b000382 | prose | pages [25] -->
dh Open CTCSS 1400 10 8 3000 3 8 10000 1 8

<!-- b000383 | prose | pages [25] -->
Therefore, the higher the initial number of potential users, the fewer repeaters are necessary to sustain 1000 simulateous users.

<!-- b000384 | heading | pages [25] -->
11 Strengths & Weaknesses

<!-- b000385 | heading | pages [25] -->
Strengths

<!-- b000386 | prose | pages [25] -->
• Versatility of the models. Both models are highly versatile and can account for many changing parameters. We were very impressed that our model accomodates 10,000 users under the established requirements.

<!-- b000387 | furniture | pages [26] -->
Control Number: 11759

<!-- b000388 | furniture | pages [26] -->
Page 26 of 51

<!-- b000389 | prose | pages [26] -->
• Smart clustering. The fact that reclustering can be implemented (or is required) in the models creates a smarter algorithm that targets the highest priority targets at that moment. This allows for the “best” decision possible to be made at any given iteration.

<!-- b000390 | prose | pages [26] -->
• Eﬃcient use of CTCSS Lines. Both models, even with 10,000 users, do not exhaust the use of private lines. These unused lines could accomodate more traﬃc if it were desired.

<!-- b000391 | heading | pages [26] -->
Weaknesses

<!-- b000392 | prose | pages [26] -->
• Large reliance on k-cluster analysis. Other clustering methods exist and our choice to exclusively use k-clustering limits our model. Running the models with diﬀerent clustering methods would have been more illuminating to see if there were more eﬃcient ways to network and support the users.

<!-- b000393 | prose | pages [26] -->
• No use of Quality Threshold. Quality Threshold (QT) is a clustering method for which a distance treshhold, not the number of clusters, is set. Implenenting this method of clustering could have improved eﬃciency.

<!-- b000394 | prose | pages [26] -->
• Diﬃculty with populations close to target. We found that if only 1000 users were present, the algorithm would circle around itself trying to hunt down the last remaining user. We supplanted this concern with the assumption that there were more users than we desired to connect. We felt this was a realistic liberty to take as the problem did not state that there were precisely 1000 potential users in the area.

<!-- b000395 | heading | pages [26] -->
12 Conclusion

<!-- b000396 | prose | pages [26] -->
The absolute fewest number of repeaters required to support 1,000 users is 17. This number was created by the “Bender” Snaking Model with the city distribution of users. We felt this number was reasonable for the given area and user population. The Branching Model yielded a network of 26 repeaters but established connectivty for a signiﬁcantly larger area.

<!-- b000397 | prose | pages [26] -->
When considering the rural distribution, the “Bender” Snaking Model reported 18 necessary repeaters while the Branching Model reported 25. The diﬀerence in required repeaters (7) was consistent with the diﬀerence in repeaters for the city distribution (9).

<!-- b000398 | prose | pages [26] -->
By comparing the two models, we were able to make a few fundamental conclusions:

<!-- b000399 | prose | pages [26, 27] -->
• Better connectivity requires more repeaters. We can’t argue with the minimum number of repreaters reported by our model but we did note that better connectivity (which potentially correlates into better service) for the users required more repeaters.

<!-- b000400 | furniture | pages [27] -->
Control Number: 11759

<!-- b000401 | furniture | pages [27] -->
Page 27 of 51

<!-- b000403 | prose | pages [27] -->
This seems true to life as a more robust networks of any kind can support a greater load.

<!-- b000404 | prose | pages [27] -->
• 54 CTCSS lines are not necessary. We never exhausted our pool of CTCSS lines.

<!-- b000405 | prose | pages [27] -->
Even with the 10,000 user load, 12 CTCSS tones were still available to use.

<!-- b000406 | prose | pages [27] -->
• CTCSS lines have multiple applications. While CTCSS lines are primarily used to reduce interference problems in densely populated areas, they also may be used to establish dedicated long-distance communication lines.

<!-- b000407 | furniture | pages [28] -->
Control Number: 11759

<!-- b000408 | furniture | pages [28] -->
Page 28 of 51

<!-- b000409 | heading | pages [28] -->
References

<!-- b000410 | references | pages [28] -->
[1] Metropolitan Coordination Association, Inc. Coordination Guidelines, February 2011.

<!-- b000411 | references | pages [28] -->
http://www.metrocor.net/coordination guidelines.htm.

<!-- b000412 | references | pages [28] -->
[2] Metropolitan Coordination Association, Inc. CTCSS (PL) Tones Frequencies, February

<!-- b000413 | references | pages [28] -->
2011. http://www.metrocor.net/ctcss.htm.

<!-- b000414 | references | pages [28] -->
[3] Institute for Telecommunication Sciences. High Frequency Propegation Models, Febru-

<!-- b000415 | references | pages [28] -->
ary 2011. http://elbert.its.bldrdoc.gov/hf.html.

<!-- b000416 | references | pages [28] -->
[4] Adrian W. Graham, Nicholas C. Kirkman, and Peter M. Paul. Mobile Radio Network

<!-- b000417 | references | pages [28] -->
Design in the VHF and UHF Bands. John Wily & Sons, Ltd, West Sussex, England,

<!-- b000418 | references | pages [28] -->
2007.

<!-- b000419 | references | pages [28] -->
[5] Leif J. Harcke, Kenneth S. Dueker, and David B. Leeson. Frequency Coordination in

<!-- b000420 | references | pages [28] -->
the Amateur Radio Emergency Service. ECJ, 1(1):31–36, 2004.

<!-- b000421 | references | pages [28] -->
[6] Barry LcLarnon. Vhf/Uhf/Microwave Radio Propagation: A Primer for Digital Ex-

<!-- b000422 | references | pages [28] -->
perimenters.

<!-- b000423 | references | pages [28] -->
A workship given at the 1997 TAPR/ARRL Digital Communications

<!-- b000424 | references | pages [28] -->
Conference, February 2011. http://www.tapr.org/ve3jf.dcc97.html.

<!-- b000425 | references | pages [28] -->
[7] The

<!-- b000426 | references | pages [28] -->
American

<!-- b000427 | references | pages [28] -->
Radio

<!-- b000428 | references | pages [28] -->
Relay

<!-- b000429 | references | pages [28] -->
League.

<!-- b000430 | references | pages [28] -->
Band

<!-- b000431 | references | pages [28] -->
Plan,

<!-- b000432 | references | pages [28] -->
February

<!-- b000433 | references | pages [28] -->
2011.

<!-- b000434 | references | pages [28] -->
http://www.arrl.org/band-plan-1#2m.

<!-- b000435 | references | pages [28] -->
[8] Wikipedia. 2-Meter Band, February 2011. http://en.wikipedia.org/wiki/2-meter band.

<!-- b000436 | references | pages [28] -->
[9] Wikipedia.

<!-- b000437 | references | pages [28] -->
Amateur

<!-- b000438 | references | pages [28] -->
Radio

<!-- b000439 | references | pages [28] -->
Repeater,

<!-- b000440 | references | pages [28] -->
February

<!-- b000441 | references | pages [28] -->
2011.

<!-- b000442 | references | pages [28] -->
http://en.wikipedia.org/wiki/Amateur radio repeater.

<!-- b000443 | references | pages [28] -->
[10] Wikipedia.

<!-- b000444 | references | pages [28] -->
k-means

<!-- b000445 | references | pages [28] -->
Clustering,

<!-- b000446 | references | pages [28] -->
February

<!-- b000447 | references | pages [28] -->
2011.

<!-- b000448 | references | pages [28] -->
http://en.wikipedia.org/wiki/K-means clustering.

<!-- b000449 | references | pages [28] -->
[11] Wikipedia.

<!-- b000450 | references | pages [28] -->
Very

<!-- b000451 | references | pages [28] -->
High

<!-- b000452 | references | pages [28] -->
Frequency,

<!-- b000453 | references | pages [28] -->
February

<!-- b000454 | references | pages [28] -->
2011.

<!-- b000455 | references | pages [28] -->
http://en.wikipedia.org/wiki/Very high frequency.

<!-- b000456 | furniture | pages [29] -->
Control Number: 11759

<!-- b000457 | furniture | pages [29] -->
Page 29 of 51

<!-- b000458 | heading | pages [29] -->
13 Appendix A: Full-Page Plots

<!-- b000459 | prose | pages [29] -->
"Bender" Snaking Method Repeater Placement 40

<!-- b000460 | prose | pages [29] -->
30

<!-- b000461 | prose | pages [29] -->
20

<!-- b000462 | prose | pages [29] -->
10

<!-- b000463 | prose | pages [29] -->
Miles 0

<!-- b000464 | prose | pages [29] -->
−10

<!-- b000465 | prose | pages [29] -->
−20

<!-- b000466 | prose | pages [29] -->
−30

<!-- b000467 | prose | pages [29, 30] -->
Potential User Open Repeater CTCSS Repeater Cluster Pt −40 −40 −30 −20 −10 0 10 20 30 40 Miles Branching Method Repeater Placement 40

<!-- b000468 | caption | pages [29] -->
Figure 18: Repeater Placement (Snaking Model)

<!-- b000469 | furniture | pages [30] -->
Control Number: 11759

<!-- b000470 | furniture | pages [30] -->
Page 30 of 51

<!-- b000472 | prose | pages [30] -->
30

<!-- b000473 | prose | pages [30] -->
20

<!-- b000474 | prose | pages [30] -->
10

<!-- b000475 | prose | pages [30] -->
Miles 0

<!-- b000476 | prose | pages [30] -->
−10

<!-- b000477 | prose | pages [30] -->
−20

<!-- b000478 | prose | pages [30] -->
−30

<!-- b000479 | prose | pages [30, 31] -->
Potential User Open Repeater CTCSS Repeater −40 −40 −30 −20 −10 0 10 20 30 40 Miles Branching Method CTCSS Repeater Subaudible Channel Arrangment 40

<!-- b000480 | caption | pages [30] -->
Figure 19: Repeater Placement (Branching Model)

<!-- b000481 | furniture | pages [31] -->
Control Number: 11759

<!-- b000482 | furniture | pages [31] -->
Page 31 of 51

<!-- b000484 | prose | pages [31] -->
30

<!-- b000485 | prose | pages [31] -->
7

<!-- b000486 | prose | pages [31] -->
20

<!-- b000487 | prose | pages [31] -->
1

<!-- b000488 | prose | pages [31] -->
10

<!-- b000489 | prose | pages [31] -->
5

<!-- b000490 | prose | pages [31] -->
1 Miles 8 0 1 4

<!-- b000491 | prose | pages [31] -->
6 −10 1

<!-- b000492 | prose | pages [31] -->
−20 1

<!-- b000493 | prose | pages [31] -->
−30

<!-- b000494 | prose | pages [31, 32] -->
Potential User CTCSS Repeater −40 −40 −30 −20 −10 0 10 20 30 40 Miles "Bender" Snaking Method Repeater Placement 40

<!-- b000495 | caption | pages [31] -->
Figure 20: CTCSS Line Placement (Branching Model)

<!-- b000496 | furniture | pages [32] -->
Control Number: 11759

<!-- b000497 | furniture | pages [32] -->
Page 32 of 51

<!-- b000499 | prose | pages [32] -->
30

<!-- b000500 | prose | pages [32] -->
20

<!-- b000501 | prose | pages [32] -->
10

<!-- b000502 | prose | pages [32] -->
Miles 0

<!-- b000503 | prose | pages [32] -->
−10

<!-- b000504 | prose | pages [32] -->
−20

<!-- b000505 | prose | pages [32] -->
−30

<!-- b000506 | prose | pages [32, 33] -->
Potential User Open Repeater CTCSS Repeater Cluster Pt −40 −40 −30 −20 −10 0 10 20 30 40 Miles Branching Method Repeater Placement 40

<!-- b000507 | caption | pages [32] -->
Figure 21: Repeater Placement (Snaking Model)

<!-- b000508 | furniture | pages [33] -->
Control Number: 11759

<!-- b000509 | furniture | pages [33] -->
Page 33 of 51

<!-- b000511 | prose | pages [33] -->
30

<!-- b000512 | prose | pages [33] -->
20

<!-- b000513 | prose | pages [33] -->
10

<!-- b000514 | prose | pages [33] -->
Miles 0

<!-- b000515 | prose | pages [33] -->
−10

<!-- b000516 | prose | pages [33] -->
−20

<!-- b000517 | prose | pages [33] -->
−30

<!-- b000518 | prose | pages [33, 34] -->
Potential User Open Repeater CTCSS Repeater −40 −40 −30 −20 −10 0 10 20 30 40 Miles CTCSS Subaudible Channel Arrangement 40

<!-- b000519 | caption | pages [33] -->
Figure 22: Repeater Placement (Branching Model)

<!-- b000520 | furniture | pages [34] -->
Control Number: 11759

<!-- b000521 | furniture | pages [34] -->
Page 34 of 51

<!-- b000523 | prose | pages [34] -->
30

<!-- b000524 | prose | pages [34] -->
20 7 6 1

<!-- b000525 | prose | pages [34] -->
10

<!-- b000526 | prose | pages [34] -->
1 5

<!-- b000527 | prose | pages [34] -->
Miles 0 1

<!-- b000528 | prose | pages [34] -->
−10

<!-- b000529 | prose | pages [34] -->
1

<!-- b000530 | prose | pages [34] -->
−20

<!-- b000531 | prose | pages [34] -->
8 1 4 −30

<!-- b000532 | prose | pages [34, 35] -->
Potential User Open Repeater CTCSS Repeater −40 −40 −30 −20 −10 0 10 20 30 40 Miles Snaking Method Repeater Placement (10k users) 40

<!-- b000533 | caption | pages [34] -->
Figure 23: CTCSS Line Placement (Branching Model)

<!-- b000534 | furniture | pages [35] -->
Control Number: 11759

<!-- b000535 | furniture | pages [35] -->
Page 35 of 51

<!-- b000537 | prose | pages [35] -->
30

<!-- b000538 | prose | pages [35] -->
20

<!-- b000539 | prose | pages [35] -->
10

<!-- b000540 | prose | pages [35] -->
Miles 0

<!-- b000541 | prose | pages [35] -->
−10

<!-- b000542 | prose | pages [35] -->
−20

<!-- b000543 | prose | pages [35] -->
−30

<!-- b000544 | prose | pages [35] -->
−40 −40 −30 −20 −10 0 10 20 30 40 Miles

<!-- b000545 | caption | pages [35] -->
Figure 24: Results for 10,000 Simultaneous Users

<!-- b000546 | furniture | pages [36] -->
Control Number: 11759

<!-- b000547 | furniture | pages [36] -->
Page 36 of 51

<!-- b000548 | heading | pages [36] -->
14 Appendix B: Source Code

<!-- b000549 | heading | pages [36] -->
“Bender” Snaking Model:

<!-- b000550 | prose | pages [36, 37, 38, 39, 40, 41, 42] -->
load 'C:\Users\*****\Desktop\MCM 2011\townsdata3.txt'; 1 sepdist = 10; %seperation distance 2 plsepdist =1; %Private line seperation distance 3 xcor = townsdata3(:,2); 4 ycor = townsdata3(:,3); 5 totalnum = zeros(2000,2); 6 connected = 0; 7 n=zeros(2000,5); 8 inrange = zeros(360); 9 ply = zeros(360,1); 10 plx = zeros(360,1); 11 ind = 0; 12 openchannels=0; 13 ∆f = .025; 14 cover = 0; 15 it = 1; 16 plit =0; 17 rep=zeros(50,2); 18 population = length(xcor); 19 iteration=0; 20 concat=horzcat(xcor,ycor); 21 notcovered=zeros(population,2); 22 numclus=10; 23 [clusid,clusters]=kmeans(concat,numclus); 24 clusscr=zeros(numclus); 25 26 27 for i = 1:population 28 for n = 1:numclus 29 if clusid(i) == n 30 clusscr(n) = clusscr(n) + 1; 31 end 32 end 33 end 34 35 %Plot Users and clusters 36 plot(concat(:,1),concat(:,2),'.','MarkerSize',1); 37 hold on 38 plot(clusters(:,1),clusters(:,2),'kx',... 39 'MarkerSize',20,'LineWidth',2); 40 hold on 41 plot(clusters(:,1),clusters(:,2),'ko',... 42 'MarkerSize',20,'LineWidth',2); 43 hold off 44 45 46 47 48 %Find inital repeater location 49 for i=1:5, 50 for j=1:population, 51 n(i,j)=sqrt(((clusters(i,1)-xcor(j))ˆ2)+((clusters(i,2)-ycor(j))ˆ2)); 52 if n(i,j)≤sepdist 53 totalnum(i,1)=totalnum(i,1)+1; 54 end 55 end 56 end 57 58 [C,I]=max(totalnum); 59 index=I(1); 60 rep(1,1)=clusters(index,1); 61 rep(1,2)=clusters(index,1); 62 openchannels =3/∆f; 63 64 for i=1:population, 65 if sqrt(((rep(1,1)-xcor(i))ˆ2)+((rep(1,2)-ycor(i))ˆ2))>sepdist 66 ind = ind +1; 67 notcovered(ind,1)=xcor(i); 68 notcovered(ind,2)=ycor(i); 69 end 70 end 71 72 cover = totalnum(index,1); 73 population = population-cover; 74 connected = min(totalnum(index,1),openchannels); 75 deficit = max(totalnum(index,1) - connected,0); 76 77 78 79 disp('the first repeater will be placed at'),disp('x='),disp(rep(1,1)),disp('y='), disp(rep 80 disp('number connected'),disp(connected); 81 disp('deficit'),disp(deficit); 82 disp('under cover'),disp(cover); 83 disp('open channels'),disp(openchannels); 84 disp('population'),disp(population); 85 dlmwrite('C:\Users\*****\Desktop\MCM 2011\winner.txt',I,'\t'); 86 dlmwrite('C:\Users\*****\Desktop\MCM 2011\distances.txt',n,'\t'); 87 dlmwrite('C:\Users\*****\Desktop\MCM 2011\proximity.txt',totalnum,'\t') 88 89 while connected<1000, 90 iteration=iteration+1; 91 inrange=zeros(1000); 92 onrange=zeros(1000); 93 if deficit >0 94 plit=plit+1; 95 for theta=1:360, 96 plx(theta) = rep(it,1)+plsepdist*cos((3.14159*theta)/180); 97 ply(theta) = rep(it,2)+plsepdist*sin((3.14159*theta)/180); 98 if ((plx(theta)≥-40) && (plx(theta)≤40)) 99 if ((ply(theta)≥-40) && (ply(theta)≤40)) 100 for i=1:population, 101 dist(i,1)=sqrt((plx(theta)-notcovered(i,2*iteration-1))ˆ2+(ply 102 if dist(i,1)≤sepdist 103 inrange(theta) = inrange(theta) +1; 104 end 105 end 106 end 107 end 108 end 109 [C,I] = max(inrange); 110 angle = I(1); 111 reppl(plit,1)= rep(it,1)+plsepdist*cos((3.14159*angle)/180); 112 reppl(plit,2)= rep(it,2)+plsepdist*sin((3.14159*angle)/180); 113 added=0; 114 115 openchannels = openchannels +(3/∆f); 116 117 %%REMOVE ENTRIES WHICH HAVE BEEN USED 118 ind=0; 119 for i=1:population, 120 if sqrt(((rep(it,1)-notcovered(i,2*iteration-1))ˆ2)+((rep(it,2)-notcovered 121 ind = ind +1; 122 notcovered(ind,2*iteration+1)=notcovered(i,2*iteration-1); 123 notcovered(ind,2*iteration+2)=notcovered(i,2*iteration); 124 else 125 added=added+1; 126 end 127 end 128 129 cover = cover + added; 130 population = population - added; 131 connected = min(cover,openchannels); 132 deficit = max(cover - connected,0); 133 134 disp('the PL repeater will be placed at'),disp('x='),disp(reppl(plit,1)),disp( 135 disp('added'),disp(added); 136 disp('cover'),disp(cover); 137 disp('people connected:'),disp(connected); 138 disp('deficit'),disp(deficit); 139 disp('open channels'),disp(openchannels); 140 disp('population'),disp(population); 141 end 142 143 if deficit==0 144 it = it+1; 145 inrange=zeros(5); 146 onrange = zeros(5); 147 d = zeros(5); 148 for clusterno=1:5, 149 150 d(clusterno)=sqrt((rep(it-1,1)-clusters(clusterno,1))ˆ2+(rep(it-1,2)-cluste 151 if ((rep(it-1,1)≥clusters(clusterno,1))&&(rep(it-1,2)≤clusters(clusterno,2) 152 ang(clusterno)= acos((clusters(clusterno,1)-rep(it-1,1))/d(clusterno)); 153 elseif ((rep(it-1,1)>clusters(clusterno,1))&&(rep(it-1,2)≥clusters(clustern 154 ang(clusterno)=2*pi-acos((clusters(clusterno,1)-rep(it-1,1))/d(clustern 155 elseif ((rep(it-1,1)≤clusters(clusterno,1))&&(rep(it-1,2)≥clusters(clustern 156 ang(clusterno)=2*pi-acos((clusters(clusterno,1)-rep(it-1,1))/d(clustern 157 else 158 ang(clusterno)=acos((clusters(clusterno,1)-rep(1,1))/d(clusterno)); 159 end 160 161 162 %% 163 %{ 164 165 if ((rep(it-1,1)≥clusters(clusterno,1))&&(rep(it-1,2)≤clusters(clusterno,2) 166 ang(clusterno)=pi-asin((clusters(clusterno,2)-rep(it-1,2))/d(clusterno) 167 elseif ((rep(it-1,1)≥clusters(clusterno,1))&&(rep(it-1,2)≥clusters(clustern 168 ang(clusterno)=pi+asin((rep(it-1,2)-clusters(clusterno,2))/d(clusterno) 169 elseif ((rep(it-1,1)≤clusters(clusterno,1))&&(rep(it-1,2)≥clusters(clustern 170 ang(clusterno)=2*pi-asin((rep(it-1,2)-clusters(clusterno,2))/d(clustern 171 else 172 ang(clusterno)=asin((clusters(clusterno,2)-rep(it-1,2))/d(clusterno)) 173 end 174 175 %} 176 %% 177 x(clusterno)=rep(it-1,1)+sepdist*1.5*cos(ang(clusterno)); 178 y(clusterno)=rep(it-1,2)+sepdist*1.5*sin(ang(clusterno)); 179 if ((x(clusterno)≥-40) && (x(clusterno)≤40)&&(y(clusterno)≥-40)&&(y(cluster 180 for i=1:population, 181 if sqrt((x(clusterno)-notcovered(i,2*iteration-1))ˆ2+(y(cluster 182 inrange(clusterno) = inrange(clusterno) +1; 183 end 184 end 185 for i=1:population, 186 if sqrt((clusters(clusterno,1)-notcovered(i,2*iteration-1))ˆ2+ 187 onrange(clusterno) = onrange(clusterno) +1; 188 end 189 end 190 else 191 inrange(clusterno)=-100; 192 end 193 194 end 195 196 [C,I] = max(inrange); 197 198 angleid = I(1); 199 rep(it,1)=rep(it-1,1)+sepdist*1.5*cos(ang(angleid)); 200 rep(it,2)=rep(it-1,2)+sepdist*1.5*sin(ang(angleid)); 201 202 if ((rep(it,1)≥-40)&&(rep(it,1)≤40)&&(rep(it,2)≥-40)&&(rep(it,2)≤40)) 203 ind=0; 204 added=0; 205 for i=1:population, 206 if sqrt(((rep(it,1)-notcovered(i,2*iteration-1))ˆ2)+((rep(it,2)-notcove 207 ind = ind +1; 208 notcovered(ind,2*iteration+1)=notcovered(i,2*iteration-1); 209 notcovered(ind,2*iteration+2)=notcovered(i,2*iteration); 210 else 211 added=added+1; 212 end 213 end 214 else 215 theid=1; 216 217 while ((rep(it,1)<-40)||(rep(it,1)>40)||(rep(it,2)<-40)||(rep(it,2)>40)) 218 rep(it,1)=rep(it-1,1)+sepdist*1.5*cos(ang(theid)); 219 rep(it,2)=rep(it-1,2)+sepdist*1.5*sin(ang(theid)); 220 theid =theid +1; 221 end 222 223 ind=0; 224 added=0; 225 for i=1:population, 226 if sqrt(((rep(it,1)-notcovered(i,2*iteration-1))ˆ2)+((rep(it,2)-notcove 227 ind = ind +1; 228 notcovered(ind,2*iteration+1)=notcovered(i,2*iteration-1); 229 notcovered(ind,2*iteration+2)=notcovered(i,2*iteration); 230 else 231 added=added+1; 232 end 233 end 234 end 235 236 cover = cover + added; 237 population = population - added; 238 connected = min(cover,openchannels); 239 deficit = max(cover - connected,0); 240 241 disp('the open repeater will be placed at'),disp('x='),disp(rep(it,1)),disp('y= 242 disp('added'),disp(added); 243 disp('cover'),disp(cover); 244 disp('open channels'),disp(openchannels); 245 disp('people connected:'),disp(connected); 246 disp('deficit'),disp(deficit); 247 disp('population'),disp(population); 248 end 249 end 250 251 disp('number of open repeaters'),disp(it); 252 disp('number of PL repeaters'),disp(plit); 253 254 xplot=zeros(it,1); 255 yplot=zeros(it,1); 256 for i=1:it 257 xplot(i,1)=rep(i,1); 258 yplot(i,1)=rep(i,2); 259 end 260 261 xplotpl=zeros(plit,1); 262 yplotpl=zeros(plit,1); 263 for i=1:plit 264 xplotpl(i,1)=reppl(i,1); 265 yplotpl(i,1)=reppl(i,2); 266 end 267 268 %} 269 270 plot(xcor,ycor,'s','MarkerSize',4,'MarkerEdgeColor',[1 1 1]); 271 xlabel('Miles'); 272 ylabel('Miles'); 273 title('Snaking Method Repeater Placement'); 274 hold on 275 276 plot(xplot,yplot,'o','MarkerFaceColor','r','MarkerEdgeColor','r','MarkerSize',10,'LineWidth 277 hold on 278 279 280 plot(xplotpl,yplotpl,'o','MarkerFaceColor','g','MarkerEdgeColor','g','MarkerSize',10,'LineW 281 hold on 282 283 plot(clusters(:,1),clusters(:,2),'v',... 284 'MarkerSize',10,'LineWidth',2,'MarkerEdgeColor','k'); 285 hold on 286 287 288 289 290 291 for i=1:it, 292 h=rep(i,1); k=rep(i,2); r=15; N=256; 293 t=(0:N)*2*pi/N; 294 plot(r*cos(t)+h,r*sin(t)+k,'Color','r','LineStyle','--'); 295 hold on 296 end 297 298 299 for i=1:it, 300 h=rep(i,1); k=rep(i,2); r=10; N=256; 301 t=(0:N)*2*pi/N; 302 plot(r*cos(t)+h,r*sin(t)+k,'Color','c','LineStyle',':'); 303 hold on 304 end 305 306 for i=1:plit, 307 h=reppl(i,1); k=reppl(i,2); r=15; N=256; 308 t=(0:N)*2*pi/N; 309 plot(r*cos(t)+h,r*sin(t)+k,'Color','g','LineStyle','-'); 310 hold on 311 end 312 313 314 axis([-40 40 -40 40]); 315 axis('square') 316 317 318 hold off 319

<!-- b000551 | furniture | pages [37] -->
Control Number: 11759

<!-- b000552 | furniture | pages [37] -->
Page 37 of 51

<!-- b000554 | furniture | pages [38] -->
Control Number: 11759

<!-- b000555 | furniture | pages [38] -->
Page 38 of 51

<!-- b000557 | furniture | pages [39] -->
Control Number: 11759

<!-- b000558 | furniture | pages [39] -->
Page 39 of 51

<!-- b000560 | furniture | pages [40] -->
Control Number: 11759

<!-- b000561 | furniture | pages [40] -->
Page 40 of 51

<!-- b000563 | furniture | pages [41] -->
Control Number: 11759

<!-- b000564 | furniture | pages [41] -->
Page 41 of 51

<!-- b000566 | furniture | pages [42] -->
Control Number: 11759

<!-- b000567 | furniture | pages [42] -->
Page 42 of 51

<!-- b000569 | heading | pages [42] -->
Branching Model:

<!-- b000570 | prose | pages [42, 43, 44, 45, 46, 47, 48, 49, 50, 51] -->
load 'C:\Users\*****\Desktop\MCM 2011\newtestdata2.txt'; 1 newx = newtestdata2(:,2); %x cor of data 2 newy = newtestdata2(:,3); %y cor of data 3 notcovered = horzcat(newx,newy); 4 surfsens=2; %distance from point to include in surfscr 5 sepdist = 10; %seperation distance of repeaters 6 scr=zeros(length(newx),1); %how many points are within surfsens 7 rep=zeros(40,2); %repeater locations 8 numclus=5; %number of clusters 9 clusscr=zeros(numclus,3); %how many points are within sepdist of cluster point 10 iteration=0; 11 clf; 12 numuncov=length(newx); 13 it=0; 14 connected = 0; 15 newrepang = 0; 16 numlongdist=10; 17 actlongdist=5; 18 plsepdist=15; 19 numberoflongdistancelines=3; 20 ∆f=.025; 21 perline=3/∆f; 22 openchannels=perline; 23 24 for i=1:length(newx), 25 for j=1:length(newx) 26 if sqrt((newx(i)-newx(j))ˆ2+(newy(i)-newy(j))ˆ2)≤surfsens 27 scr(i)=scr(i)+1; 28 end 29 end 30 end 31 32 concat = horzcat(newx,newy,scr); %% (xcor,ycor,zcor) 33 34 [¬,clusters]=kmeans(concat,numclus); 35 36 disp('initial uncovered'),disp(numuncov); 37 38 39 %{ 40 %Plot Users and clusters 41 plot(concat(:,1),concat(:,2),'.'); 42 hold on 43 plot(clusters(:,1),clusters(:,2),'kx',... 44 'MarkerSize',20,'LineWidth',2); 45 hold on 46 plot(clusters(:,1),clusters(:,2),'ko',... 47 'MarkerSize',20,'LineWidth',2); 48 hold off 49 %} 50 51 52 %Set first repeater locations 53 for i=1:numclus, 54 reptemp(i,1)=clusters(i,1); 55 reptemp(i,2)=clusters(i,2); 56 end 57 58 %Calculate score of each cluster and order by score 59 for i=1:numclus, 60 for j=1:length(newx), 61 if sqrt((reptemp(i,1)-newx(j))ˆ2+(reptemp(i,2)-newy(j))ˆ2)≤sepdist 62 clusscr(i,1)=reptemp(i,1); 63 clusscr(i,2)=reptemp(i,2); 64 clusscr(i,3)=clusscr(i,3)+1; 65 end 66 end 67 end 68 69 srtclus = sortrows(clusscr,-3); %sorted clusters 70 71 %Set first repeater locations 72 rep(1,1)=srtclus(1,1); 73 rep(1,2)=srtclus(1,2); 74 75 added=0; 76 i=0; 77 78 %Calculate added and remove covered entries 79 for j=1:numuncov, 80 if sqrt((rep(1,1)-notcovered(j,1))ˆ2+(rep(1,2)-notcovered(j,2))ˆ2)≤sepdist 81 added=added+1; 82 else 83 i=i+1; 84 notcovered(i,3)=notcovered(j,1); 85 notcovered(i,4)=notcovered(j,2); 86 end 87 end 88 89 repcoverage(1)=added; 90 numuncov=numuncov-added; 91 connected = connected+added; 92 93 targetloc(1)=srtclus(2,1); 94 targetloc(2)=srtclus(2,2); 95 96 newrepdist = sqrt((rep(1,1)-targetloc(1))ˆ2+(rep(1,2)-targetloc(2))ˆ2); %Distance from curr 97 98 99 100 if ((rep(1,1)≥targetloc(1))&&(rep(1,2)≤targetloc(2))) 101 newrepang= acos((targetloc(1)-rep(1,1))/newrepdist); 102 elseif ((rep(1,1)≥targetloc(1))&&(rep(1,2)≥targetloc(2))) 103 newrepang=2*pi-acos((targetloc(1)-rep(1,1))/newrepdist); 104 elseif ((rep(1,1)≤targetloc(1))&&(rep(1,2)≥targetloc(2))) 105 newrepang=2*pi-acos((targetloc(1)-rep(1,1))/newrepdist); 106 else 107 newrepang=acos((targetloc(1)-rep(1,1))/newrepdist); 108 end 109 110 repno=1; 111 112 iteration=0; 113 lastplaced=1; 114 115 %add repeater to make connection 116 while connected<1000, 117 118 iteration=iteration+1; 119 while newrepdist>sepdist, 120 it=it+1; 121 repno = repno+1; 122 rep(repno,1)=rep(lastplaced,1)+sepdist*cos(newrepang); 123 rep(repno,2)=rep(lastplaced,2)+sepdist*sin(newrepang); 124 lastplaced=repno; %set the last placed to the current repeater 125 newrepdist=sqrt((targetloc(1)-rep(repno,1))ˆ2+(targetloc(2)-rep(repno,2))ˆ2); 126 127 %Count covered and remove from dataset 128 added=0; 129 i=0; 130 for j=1:numuncov, 131 if sqrt((rep(repno,1)-notcovered(j,2*it+1))ˆ2+(rep(repno,2)-notcovered(j,2*it+2 132 added=added+1; 133 else 134 i=i+1; 135 notcovered(i,2*it+3)=notcovered(j,2*it+1); 136 notcovered(i,2*it+4)=notcovered(j,2*it+2); 137 end 138 end 139 140 coveragestat=0; 141 for j=1:length(newx), 142 if sqrt((rep(repno,1)-newx(j))ˆ2+(rep(repno,2)-newy(j))ˆ2)≤sepdist 143 coveragestat=coveragestat+1; 144 end 145 end 146 repcoverage(repno)=coveragestat; 147 numuncov=numuncov-added; 148 connected = connected + added; 149 disp('added'),disp(added); 150 disp('adding another'); 151 end 152 disp('iteration'),disp(iteration); 153 154 155 156 157 %New targetloc 158 concat = zeros(numuncov,2); 159 for i=1:numuncov; 160 concat(i,1) = notcovered(i,2*it+3); 161 concat(i,2) = notcovered(i,2*it+4); 162 end 163 164 [clusid,clusters]=kmeans(concat,numclus); 165 166 clusscr=zeros(numclus,3); 167 168 169 170 %Set temp repeater locations 171 for i=1:numclus, 172 reptemp(i,1)=clusters(i,1); 173 reptemp(i,2)=clusters(i,2); 174 end 175 %Calculate score of each cluster and order by score 176 for i=1:numclus, 177 clusscr(i,1)=reptemp(i,1); 178 clusscr(i,2)=reptemp(i,2); 179 for j=1:numuncov, 180 if sqrt((reptemp(i,1)-concat(j,1))ˆ2+(reptemp(i,2)-concat(j,2))ˆ2)≤sepdist 181 clusscr(i,3)=clusscr(i,3)+1; 182 end 183 end 184 end 185 186 srtclus = sortrows(clusscr,-3); %sorted clusters 187 188 %Set new target location 189 targetloc(1)=srtclus(1,1); 190 targetloc(2)=srtclus(1,2); 191 repdist=zeros(repno,1); 192 for i=1:repno, 193 repdist(i,1)=sqrt((targetloc(1)-rep(i,1))ˆ2+(targetloc(2)-rep(i,2))ˆ2); 194 end 195 196 [C,I]=min(repdist); 197 lastplaced=I(1); 198 newrepdist = sqrt((rep(lastplaced,1)-targetloc(1))ˆ2+(rep(lastplaced,2)-targetloc(2))ˆ2 199 200 201 if ((rep(lastplaced,1)≥targetloc(1))&&(rep(lastplaced,2)≤targetloc(2))) 202 newrepang= acos((targetloc(1)-rep(lastplaced,1))/newrepdist); 203 elseif ((rep(lastplaced,1)≥targetloc(1))&&(rep(lastplaced,2)≥targetloc(2))) 204 newrepang=2*pi-acos((targetloc(1)-rep(lastplaced,1))/newrepdist); 205 elseif ((rep(lastplaced,1)≤targetloc(1))&&(rep(lastplaced,2)≥targetloc(2))) 206 newrepang=2*pi-acos((targetloc(1)-rep(lastplaced,1))/newrepdist); 207 else 208 newrepang=acos((targetloc(1)-rep(lastplaced,1))/newrepdist); 209 end 210 211 disp('connected'),disp(connected); 212 213 214 end 215 216 disp('number uncovered'),disp(numuncov); 217 218 219 %%Plot Data 220 xplot=zeros(repno,1); 221 yplot=zeros(repno,1); 222 for i=1:repno, 223 xplot(i)=rep(i,1); 224 yplot(i)=rep(i,2); 225 end 226 227 228 229 %% 230 concat = zeros(length(newx),2); 231 for i=1:length(newx); 232 concat(i,1) = newx(i); 233 concat(i,2) = newy(i); 234 end 235 236 concat=horzcat(newx,newy); 237 [clusid,clusters]=kmeans(concat,numlongdist); 238 239 cluslongscr=zeros(numclus,2); 240 241 for i=1:length(clusters), 242 for j=1:length(newx) 243 if sqrt((clusters(i,1)-newx(j))ˆ2+(clusters(i,2)-newy(j))ˆ2)≤sepdist; 244 cluslongscr(i,1)=i; 245 cluslongscr(i,2)=cluslongscr(i,2)+1; 246 end 247 end 248 end 249 250 cluslongsrt=sortrows(cluslongscr,-2); 251 plplots=zeros(actlongdist,2); 252 253 for i=1:actlongdist, 254 plplots(i,1)=clusters(cluslongsrt(i),1); 255 plplots(i,2)=clusters(cluslongsrt(i),2); 256 end 257 258 plrep=zeros(100,2); 259 260 longdistmat=zeros(actlongdist,2); 261 currentlong=1; 262 plrep(1,1)=plplots(1,1); 263 plrep(1,2)=plplots(1,2); 264 plrep(1,3)=1; 265 266 for j=1:actlongdist, 267 longdistmat(j,1)=j; 268 longdistmat(j,2)=sqrt((plrep(1,1)-plplots(j,1))ˆ2+(plrep(1,2)-plplots(j,2))ˆ2); 269 end 270 271 272 ldsort=sortrows(longdistmat,2); 273 tar(1,1)=plplots(ldsort(2,1),1); 274 tar(1,2)=plplots(ldsort(2,1),2); 275 prevtarget=ldsort(2,1); 276 d2tar=longdistmat(ldsort(2,1),2); 277 278 if ((plrep(1,1)≥tar(1,1))&&(plrep(1,2)≤tar(1,2))) 279 angletotarget= acos((tar(1,1)-plrep(1,1))/d2tar); 280 elseif ((plrep(1,1)≥tar(1,1))&&(plrep(1,2)≥tar(1,2))) 281 angletotarget=2*pi-acos((tar(1,1)-plrep(1,1))/d2tar); 282 elseif ((plrep(1,1)≤tar(1,1))&&(plrep(1,2)≥tar(1,2))) 283 angletotarget=2*pi-acos((tar(1,1)-plrep(1,1))/d2tar); 284 else 285 angletotarget=acos((tar(1,1)-plrep(1,1))/d2tar); 286 end 287 288 while d2tar>plsepdist, 289 currentlong=currentlong+1; 290 plrep(currentlong,1)=plrep(currentlong-1,1)+plsepdist*cos(angletotarget); 291 plrep(currentlong,2)=plrep(currentlong-1,2)+plsepdist*sin(angletotarget); 292 plrep(currentlong,3)=1; 293 d2tar=sqrt((plrep(currentlong,1)-tar(1,1))ˆ2+(plrep(currentlong,2)-tar(1,2))ˆ2); 294 end 295 296 for i=1:actlongdist, 297 newzones(i,1)=plplots(i,1); 298 newzones(i,2)=plplots(i,2); 299 end 300 newzones(prevtarget,:)=[]; 301 newzones(1,:)=[]; 302 303 counter=1; 304 while counter<actlongdist-1; 305 counter=counter+1; 306 307 longdistmat=zeros(actlongdist-counter,2); 308 for i=1:actlongdist-counter, 309 longdistmat(i,1)=i; 310 longdistmat(i,2)=sqrt((plrep(currentlong,1)-newzones(i,1))ˆ2+(plrep(currentlong,2)- 311 end 312 313 ldsort=sortrows(longdistmat,2); 314 315 prevtarget=ldsort(1,1); 316 tar(1,1)=newzones(prevtarget,1); 317 tar(1,2)=newzones(prevtarget,2); 318 319 d2tar=longdistmat(prevtarget,2); 320 321 322 if ((plrep(currentlong,1)≥tar(1,1))&&(plrep(currentlong,2)≤tar(1,2))) 323 angletotarget= acos((tar(1,1)-plrep(currentlong,1))/d2tar); 324 elseif ((plrep(currentlong,1)≥tar(1,1))&&(plrep(currentlong,2)≥tar(1,2))) 325 angletotarget=2*pi-acos((tar(1,1)-plrep(currentlong,1))/d2tar); 326 elseif ((plrep(currentlong,1)≤tar(1,1))&&(plrep(currentlong,2)≥tar(1,2))) 327 angletotarget=2*pi-acos((tar(1,1)-plrep(currentlong,1))/d2tar); 328 else 329 angletotarget=acos((tar(1,1)-plrep(currentlong,1))/d2tar); 330 end 331 332 while d2tar>plsepdist, 333 currentlong=currentlong+1; 334 plrep(currentlong,1)=plrep(currentlong-1,1)+plsepdist*cos(angletotarget); 335 plrep(currentlong,2)=plrep(currentlong-1,2)+plsepdist*sin(angletotarget); 336 plrep(currentlong,3)=1; 337 d2tar=sqrt((plrep(currentlong,1)-tar(1,1))ˆ2+(plrep(currentlong,2)-tar(1,2))ˆ2); 338 end 339 340 newzones(prevtarget,:)=[]; 341 342 343 end 344 345 346 noplrep=currentlong; 347 openchannels=openchannels+numberoflongdistancelines*perline; 348 deficit=max(connected-openchannels,0); 349 350 indexnum=0; 351 indexnum2=0; 352 channelnumber=numberoflongdistancelines; 353 plcolor(1:currentlong,1)=51; 354 plcolor(1:currentlong,2)=51; 355 plcolor(1:currentlong,3)=255; 356 pluncovered=horzcat(newx,newy); 357 numuncovered=length(newx); 358 while deficit>0 359 channelnumber=channelnumber+1; 360 currentlong=currentlong+1; 361 indexnum=indexnum+1; 362 if indexnum==actlongdist 363 indexnum=1; 364 concat = zeros(numuncovered,2); 365 for i=1:numuncovered; 366 concat(i,1) = pluncovered(i,1); 367 concat(i,2) = pluncovered(i,2); 368 end 369 370 [clusid,clusters]=kmeans(pluncovered,numlongdist); 371 372 cluslongscr=zeros(numlongdist,2); 373 374 for i=1:length(clusters), 375 for j=1:length(pluncovered) 376 if sqrt((clusters(i,1)-pluncovered(j,1))ˆ2+(clusters(i,2)-pluncovered(j,2)) 377 cluslongscr(i,1)=i; 378 cluslongscr(i,2)=cluslongscr(i,2)+1; 379 end 380 end 381 end 382 383 cluslongsrt=sortrows(cluslongscr,-2); 384 plplots=zeros(actlongdist,2); 385 386 for i=1:actlongdist, 387 plplots(i,1)=clusters(cluslongsrt(i),1); 388 plplots(i,2)=clusters(cluslongsrt(i),2); 389 end 390 end 391 plrep(currentlong,1)=plplots(indexnum,1); 392 plrep(currentlong,2)=plplots(indexnum,2); 393 plrep(currentlong,3)=channelnumber; 394 index1=1; 395 for i=1:numuncovered, 396 if sqrt((plrep(currentlong,1)-pluncovered(i))ˆ2+(plrep(currentlong,2)-pluncovered(i)) 397 pluncovered(index1,1)=pluncovered(i,1); 398 pluncovered(index1,2)=pluncovered(i,2); 399 index1=index1+1; 400 else 401 numuncovered=numuncovered-1; 402 end 403 end 404 plcolor(currentlong,1)=255-indexnum2*20; 405 plcolor(currentlong,2)=40+indexnum2*20; 406 plcolor(currentlong,3)=0; 407 noplrep=noplrep+1; 408 openchannels=openchannels+perline; 409 deficit=max(connected-openchannels,0); 410 indexnum2=indexnum2+1; 411 end 412 413 plrepplot=zeros(currentlong,2); 414 for i=1:currentlong, 415 plrepplot(i,1)=plrep(i,1); 416 plrepplot(i,2)=plrep(i,2); 417 end 418 419 420 %} 421 %% 422 plot(newx,newy,'s','MarkerSize',2,'MarkerEdgeColor',[1 1 1]); 423 424 hold on 425 xlabel('Miles'); 426 ylabel('Miles'); 427 title('Random User Data'); 428 hold on 429 430 plot(xplot,yplot,'.','MarkerFaceColor','none','MarkerEdgeColor',[1 0 0],'MarkerSize',20,'Li 431 hold on 432 433 %} 434 435 %{ 436 plot(plplots(:,1),plplots(:,2),'o','MarkerFaceColor','g','MarkerEdgeColor',g,'MarkerSize',1 437 %} 438 439 for i=1:noplrep, 440 plot(plrepplot(i,1),plrepplot(i,2),'.','MarkerFaceColor','g','MarkerEdgeColor','g','Mar 441 hold on 442 end 443 444 445 for i=1:repno, 446 h=rep(i,1); k=rep(i,2); r=10; N=256; 447 t=(0:N)*2*pi/N; 448 plot(r*cos(t)+h,r*sin(t)+k,'Color','r','LineStyle','--'); 449 hold on 450 end 451 452 453 454 455 for i=1:repno, 456 h=rep(i,1); k=rep(i,2); r=10; N=256; 457 t=(0:N)*2*pi/N; 458 plot(r*cos(t)+h,r*sin(t)+k,'Color',[43/255 129/255 86/255],'LineStyle',':'); 459 hold on 460 end 461 %} 462 %{ 463 for i=1:noplrep, 464 h=plrep(i,1); k=plrep(i,2); r=15; N=256; 465 t=(0:N)*2*pi/N; 466 plot(r*cos(t)+h,r*sin(t)+k,'Color',[plcolor(i,1)/255 plcolor(i,2)/255 plcolor(i,3)/255] 467 hold on 468 end 469 470 471 472 for i=1:currentlong, 473 if i==7, 474 text(plrep(i,1)-2,plrep(i,2),num2str(plrep(i,3))); 475 elseif i==8, 476 text(plrep(i,1)+.5,plrep(i,2),num2str(plrep(i,3))); 477 elseif i==12, 478 else 479 text(plrep(i,1)+.5,plrep(i,2),num2str(plrep(i,3))); 480 end 481 end 482 %} 483 484 485 %{ 486 h=plot(clusters(:,1),clusters(:,2),'v',... 487 'MarkerSize',10,'LineWidth',2,'MarkerEdgeColor','k'); 488 axis([-40 40 -40 40]); 489 set(h, 'Color', [.8 .8 .8]); 490 get(h); 491 %} 492 493 axis([-40 40 -40 40]); 494 axis('square') 495 hold off 496 disp('number of repeaters'),disp(repno); 497 498 disp('number of PL repeaters'),disp(noplrep); 499 disp('number of channels'),disp(openchannels); 500

<!-- b000571 | furniture | pages [43] -->
Control Number: 11759

<!-- b000572 | furniture | pages [43] -->
Page 43 of 51

<!-- b000574 | furniture | pages [44] -->
Control Number: 11759

<!-- b000575 | furniture | pages [44] -->
Page 44 of 51

<!-- b000577 | furniture | pages [45] -->
Control Number: 11759

<!-- b000578 | furniture | pages [45] -->
Page 45 of 51

<!-- b000580 | furniture | pages [46] -->
Control Number: 11759

<!-- b000581 | furniture | pages [46] -->
Page 46 of 51

<!-- b000583 | furniture | pages [47] -->
Control Number: 11759

<!-- b000584 | furniture | pages [47] -->
Page 47 of 51

<!-- b000586 | furniture | pages [48] -->
Control Number: 11759

<!-- b000587 | furniture | pages [48] -->
Page 48 of 51

<!-- b000589 | furniture | pages [49] -->
Control Number: 11759

<!-- b000590 | furniture | pages [49] -->
Page 49 of 51

<!-- b000592 | furniture | pages [50] -->
Control Number: 11759

<!-- b000593 | furniture | pages [50] -->
Page 50 of 51

<!-- b000595 | furniture | pages [51] -->
Control Number: 11759

<!-- b000596 | furniture | pages [51] -->
Page 51 of 51
