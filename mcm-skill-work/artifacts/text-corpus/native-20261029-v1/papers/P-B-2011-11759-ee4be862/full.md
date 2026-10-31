# P-B-2011-11759-ee4be862

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Control Number: 11759

<!-- b000002 | furniture | pages [1] -->
Page 1 of 51

<!-- b000003 | heading | pages [1] -->
Abstract

<!-- b000004 | prose | pages [1] -->
We propose and evaluate two models to determine the minimum number of very high frequency (VHF) repeaters necessary to accomodate a given geographic distru- biton of users. By utilizing cluster analysis, each model uniquely designs a network of open and “continuous tone-coded squelch system” (CTCSS) repeaters to simulta- neously accomodate the desired user load.

<!-- b000005 | prose | pages [1] -->
In addition, the models are mindful of connectivity issues and seek to establish the best connectivity for the set of users. Through the comparison of these two models, we seek to establish the minimum num- ber of repeaters required.

<!-- b000006 | prose | pages [1] -->
In the “Bender” Snaking Model, a network is established by creating a “snake” or chain of open repeaters across the area. The model determines the most eﬀective placement for each open repeater and is mindful to maintain channel availability cy placing CTCSS repeaters when necessary.

<!-- b000007 | prose | pages [1] -->
In the Branching Model, a backbone network is established between the two most populous areas and branch networks are subsequentially added to existing network. After the branched network has been completed, CTCSS lines are placed to both mitigate channel saturation and establish dedicated long-distance lines. This model seeks to create the best connectivity for the users in the area with the minimum number of repeaters used.

<!-- b000008 | prose | pages [1] -->
We test our models on two likely area distrubitions: a city/suburban-like user distribution and a rural-like user distribution. We compare the results and propose the minimum number of repeaters necessary for each scenario. By comparing the two models, we are able to decide if the number is realistic and what the beneﬁts of a diﬀerent network design may correlate to for the users.

<!-- b000009 | prose | pages [1] -->
Finally, we stress-test our models with 10,000 users in the same area and discuss the defects of line-of-sight propagation caused by mountains in the area.

<!-- b000010 | prose | pages [2] -->
Optimizing VHF Repeater Coordination Using Cluster

<!-- b000011 | prose | pages [2] -->
Analysis

<!-- b000012 | prose | pages [2] -->
MCM Competition Problem B

<!-- b000013 | prose | pages [2] -->
Control Number: 11759

<!-- b000014 | heading | pages [2] -->
Contents

<!-- b000015 | contents | pages [2] -->
1

<!-- b000016 | heading | pages [2] -->
Problem Restatement

<!-- b000017 | prose | pages [2] -->
2

<!-- b000018 | heading | pages [2] -->
Assumptions and Justiﬁcations

<!-- b000019 | prose | pages [2] -->
3 Available Technology

<!-- b000020 | prose | pages [2] -->
4

<!-- b000021 | prose | pages [2] -->
4

<!-- b000022 | prose | pages [2] -->
5

<!-- b000023 | prose | pages [2] -->
Repeaters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 5

<!-- b000024 | prose | pages [2] -->
Continuous Tone-Coded Squelch System 3.2

<!-- b000025 | prose | pages [2] -->
4

<!-- b000026 | heading | pages [2] -->
The “Bender” Snake Model

<!-- b000027 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000028 | prose | pages [2] -->
6

<!-- b000029 | prose | pages [2] -->
6

<!-- b000030 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Description 7

<!-- b000031 | prose | pages [2] -->
Mathematical Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2

<!-- b000032 | prose | pages [2] -->
5

<!-- b000033 | heading | pages [2] -->
The Branching Model

<!-- b000034 | prose | pages [2] -->
7

<!-- b000035 | prose | pages [2] -->
11

<!-- b000036 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Description 11

<!-- b000037 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 Mathematical Intepretation

<!-- b000038 | prose | pages [2] -->
6

<!-- b000039 | heading | pages [2] -->
Model Comparison Summary

<!-- b000040 | prose | pages [2] -->
12

<!-- b000041 | prose | pages [2] -->
14

<!-- b000042 | prose | pages [2] -->
2 2

<!-- b000043 | furniture | pages [3] -->
Control Number: 11759

<!-- b000044 | prose | pages [3] -->
7 Case Studies

<!-- b000045 | furniture | pages [3] -->
Page 3 of 51

<!-- b000046 | prose | pages [3] -->
15

<!-- b000047 | prose | pages [3] -->
City Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 15

<!-- b000048 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Rural Distrubition

<!-- b000049 | prose | pages [3] -->
8 10,000 Simultaneous Users

<!-- b000050 | prose | pages [3] -->
9 Mountainous Terrain

<!-- b000051 | heading | pages [3] -->
10 Sensitivity to Parameters

<!-- b000052 | heading | pages [3] -->
11 Strengths & Weaknesses

<!-- b000053 | heading | pages [3] -->
12 Conclusion

<!-- b000054 | heading | pages [3] -->
13 Appendix A: Full-Page Plots

<!-- b000055 | heading | pages [3] -->
14 Appendix B: Source Code

<!-- b000056 | prose | pages [3] -->
19

<!-- b000057 | prose | pages [3] -->
22

<!-- b000058 | prose | pages [3] -->
23

<!-- b000059 | prose | pages [3] -->
24

<!-- b000060 | prose | pages [3] -->
25

<!-- b000061 | prose | pages [3] -->
26

<!-- b000062 | prose | pages [3] -->
29

<!-- b000063 | prose | pages [3] -->
36

<!-- b000064 | furniture | pages [4] -->
Control Number: 11759

<!-- b000065 | furniture | pages [4] -->
Page 4 of 51

<!-- b000066 | prose | pages [4] -->
1

<!-- b000067 | heading | pages [4] -->
Problem Restatement

<!-- b000068 | prose | pages [4] -->
Without the aid of repeaters, VHF radio would only permit low-power users to commu- nicate when direct line-of-sight could be established between the transmitter and receiver. Repeaters alleviate this restriction by amplifying and rebroadcasting these signals in order to make them available to a larger geographical area. By accounting for mutual repeater interference due to geographical proximity and utilizing a “continuous tone-coded squelch system” (CTCSS) or “private line” (PL), we seek to ﬁnd the minimal number of repeaters required to support 1,000 simultaneous users. The users inhabit a 40 mile radius ﬂat cir- cular area and are permitted to broadcast between 145-148 MHz. The repeaters transmit frequency is 600 kHz above or below the received frequency and 54 diﬀerent CTCSS tones are available. We then examine how our model adapts to accommodate 10,000 users and consider the potential defects of line-of-sight propagation in the presence of mountainous areas.

<!-- b000069 | prose | pages [4] -->
2

<!-- b000070 | heading | pages [4] -->
Assumptions and Justiﬁcations

<!-- b000071 | prose | pages [4] -->
• Geometry is Euclidean. Since the area is given to be ﬂat, we assume that Euclidean geometry may be used.

<!-- b000072 | prose | pages [4] -->
• The system is closed. We assume that all signals originate from within our system. We also assume that there will be no outside interference in the system.

<!-- b000073 | prose | pages [4] -->
• Antennas are isotropic. Because the eﬀective transmission area of each user and each antenna is relatively small compared to the whole area, we assume that antennas operate isotropically.

<!-- b000074 | prose | pages [4] -->
This is a fundamental assumption made in modern network design [4].

<!-- b000075 | prose | pages [4] -->
• Each user is a “low-power” user. Typical VHF radio transmitters are eﬀective across small towns without repeater support [8]. Since the area being considered is over 5000 square miles, the area of a small town is negligible and we can assume that users will not be able to communicate with one another without repeater support, i.e. each user is a low-power user.

<!-- b000076 | prose | pages [4] -->
• Each user “plays nice.” In order to avoid users purposefully or accidentally drown- ing out the signals of others, we require that all users have the same equipment, e.g. all users broadcast at the same intensity and all users have the same range limitations. As a result, the requirements to connect a single user will be static. Speciﬁcally, each users will have to be within some ﬁxed maximum distance from a repeater to connect to the network.

<!-- b000077 | prose | pages [4] -->
• There are more than 1,000 (or 10,000) potential users. It would be unrealistic for any company or group of individuals to place an appreciable number of repeaters in

<!-- b000078 | furniture | pages [5] -->
Control Number: 11759

<!-- b000079 | furniture | pages [5] -->
Page 5 of 51

<!-- b000080 | prose | pages [5] -->
order to accommodate one individual. We assume that the number of potential users in the area exceeds the number that must be simultaneously accomodated.

<!-- b000081 | prose | pages [5] -->
• The geographic distribution of users is known. The geographical distribution of users must be a known constraint before repeater requirements can be determined. The demand for network connectivity will not exist unless there is a preexisting community present.

<!-- b000082 | prose | pages [5] -->
• Users and repeaters are distinct entities. In reality, most VHF radio repeaters are maintained by individual users or a localized group of users. These repeaters are openly available and are typically not used as mobile stations [9]. Thus we assume that users are not broadcasting from repeaters and that they may be treated as two distinct entities.

<!-- b000083 | prose | pages [5] -->
• VHF signals are not aﬀected by physical entities in the area. The physical presence of users and antennas will not interfere with the propagation of waves in the VHF spectrum. However, land features such as mountains will aﬀect propagation [11].

<!-- b000084 | prose | pages [5] -->
3 Available Technology

<!-- b000085 | prose | pages [5] -->
The problem statement makes two diﬀerent pieces of technology available: repeaters and continuous tone-coded squelch systems. We will now outline these technologies.

<!-- b000086 | prose | pages [5] -->
3.1 Repeaters

<!-- b000087 | prose | pages [5] -->
Repeaters are stationary devices that pick up weak signals (i.e. signals from users), amplify them, and retransmit them on a diﬀerent frequency. This allows users to circumvent the line- of-sight limitation of VHF and broadcast their signal greater distances. To avoid inteference with the incoming (weak) signal, the repeater rebroadcasts the new (strong) signal 600 kHz above or below the received signal.

<!-- b000088 | prose | pages [5] -->
To avoid repeaters interfering with one another the Metropolitan Coordination Association states that repeaters must be at least 10 miles apart [1]. Overlapping repeater “zones” will allow signals to pass from one repeater to another, allowing signals to travel signiﬁcant distances.

<!-- b000089 | prose | pages [5] -->
Note that the range of a repeater is directly correlated to its height.

<!-- b000090 | prose | pages [5] -->
The line-of-sight

<!-- b000091 | prose | pages [5] -->
p

<!-- b000092 | prose | pages [5] -->
calculation to determine the eﬀectve distance is given by disance in miles =

<!-- b000093 | prose | pages [5] -->
1.5Af, where Af is the height of the antenna in feet [11].

<!-- b000094 | furniture | pages [6] -->
Control Number: 11759

<!-- b000095 | furniture | pages [6] -->
Page 6 of 51

<!-- b000096 | prose | pages [6] -->
Continuous Tone-Coded Squelch System 3.2

<!-- b000097 | prose | pages [6] -->
Continuous Tone-Coded Squelch Systems (CTCSS), often called Private Lines (PL), further mitigates interference by associating a subaudible tone with signals being received/transmit- ted by the repeater. In order to communicate through a private line repeater, users must also broadcast this tone. This allows users in a densely populated area to communicate on the same channel with minimal interference. Private line repeaters are not necessarily closed [2] as these CTCSS tones are often published. Since it is our intention to increase the number of available channels, CTCSS tones will be common knowledge to all users.

<!-- b000098 | heading | pages [6] -->
The “Bender” Snake Model

<!-- b000099 | prose | pages [6] -->
4

<!-- b000100 | prose | pages [6] -->
The “Bender1” Snake Model seeks to maximize the number of connected users by eﬃciently creating a snake-like chain of open repeaters across the area.

<!-- b000101 | caption | pages [6] -->
Figure 1 describes this model without reclustering.

<!-- b000102 | prose | pages [6] -->
Create and Score

<!-- b000103 | prose | pages [6] -->
Clusters

<!-- b000104 | prose | pages [6] -->
Place 1st Repeater

<!-- b000105 | prose | pages [6] -->
(Open)

<!-- b000106 | prose | pages [6] -->
Enough

<!-- b000107 | prose | pages [6] -->
yes

<!-- b000108 | prose | pages [6] -->
End of

<!-- b000109 | prose | pages [6] -->
Users &

<!-- b000110 | prose | pages [6] -->
Method

<!-- b000111 | prose | pages [6] -->
Channels?

<!-- b000112 | prose | pages [6] -->
Add

<!-- b000113 | prose | pages [6] -->
no

<!-- b000114 | prose | pages [6] -->
Place New

<!-- b000115 | prose | pages [6] -->
Enough

<!-- b000116 | prose | pages [6] -->
Repeater

<!-- b000117 | prose | pages [6] -->
no

<!-- b000118 | prose | pages [6] -->
Repeater

<!-- b000119 | prose | pages [6] -->
Channels?

<!-- b000120 | prose | pages [6] -->
(PL)

<!-- b000121 | prose | pages [6] -->
(Open)

<!-- b000122 | prose | pages [6] -->
yes

<!-- b000123 | prose | pages [6] -->
Find Optimal Direction

<!-- b000124 | caption | pages [6] -->
Figure 1: Flow Chart for “Bender” Snake Model

<!-- b000125 | prose | pages [6] -->
1Named after Bender, a team member’s dog who has a habit of snaking around doors, corners and furniture.

<!-- b000126 | furniture | pages [7] -->
Control Number: 11759

<!-- b000127 | furniture | pages [7] -->
Page 7 of 51

<!-- b000128 | prose | pages [7] -->
4.1 Description

<!-- b000129 | prose | pages [7] -->
Using k-means clustering[10], we establish clusters of users to deterrmine the optimal initial open repeater placement. Optimal placement is determined by the greatest number of users we can cover when placing a single open repeater. This may also be referred to as “scoring” a cluster where a higher score correlates to coverage for more users. A second open repeater is optimally placed along the perimeter of the newly established network area. This process is repeated iteravely by placing a new open repeater along the permitter of the most recently established open repeater.

<!-- b000130 | prose | pages [7] -->
The placement of the second open repeater is always in the direction of a cluster point, i.e. other high density locations. This ensures that a network is established between the most users using the least number of repeaters. The model is mindful of ensuring that enough channels are available to users by placing CTCSS repeaters accordingly.

<!-- b000131 | prose | pages [7] -->
By design, network growth tends toward establishing connectivity near and between cluster points. As more users around each cluster are accomodated, the score associated with their respective cluster should reﬂect that change. To account for this, cluster scores may be reevaluated to encourage intelligent networking in the model. This is known as reclustering.

<!-- b000132 | prose | pages [7] -->
4.2 Mathematical Interpretation

<!-- b000133 | prose | pages [7] -->
The model is designed to be highly versatile and supports a number of diﬀerent parameters that may be changed based on a given situation. They are:

<!-- b000134 | prose | pages [7] -->
Parameter Description n Number of users within 40 miles k Number of k-means cluster points ds Maximum distance for user-to-repeater communication hr Height of repeater towers dh Repeater output distance ∆f Frequency separation / channel width

<!-- b000135 | prose | pages [7] -->
Before we begin, we must deﬁne a few additional terms. Let Nc be the number of people with network connectivity (i.e. within range of an open repeater) and let Nf be the number of people with access to an available frequency range. Let O denote the number of available channels. Initially, we will have Nc = 0, Nf = 0 and O = 0.

<!-- b000136 | prose | pages [7] -->
So let n be the number of users within the 40 mile radius. For user i with 1 ≤i ≤n, let (xi, yi) denote the user’s location in Cartesian coordinates. We arrange these coordinates into an n × 2 matrix M where

<!-- b000137 | prose | pages [7] -->
Mj,1 = xj and Mj,2 = yj for all integers j ∈[1, n].

<!-- b000138 | furniture | pages [8] -->
Control Number: 11759

<!-- b000139 | furniture | pages [8] -->
Page 8 of 51

<!-- b000140 | prose | pages [8] -->
For each user, determine the number of users within the seperation distance ds. Recall that we are using Euclidean geometry, so when considering the jth user if

<!-- b000141 | prose | pages [8] -->
q

<!-- b000142 | prose | pages [8] -->
(Mj,1 −Mk,1)2 −(Mj,2 −Mk,2)2

<!-- b000143 | prose | pages [8] -->
ds ≥

<!-- b000144 | prose | pages [8] -->
then the kth user is within range of the jth user. We denote the user with the greatest number of additional users in range as the pth user.

<!-- b000145 | prose | pages [8] -->
We place an open repeater at the location of the pth user and set R1 = (Mp,1, Mp,2). The allowable frequency range is 3 MHz so there will be 3/∆f channels available. The action of placing the ﬁrst repeater makes this many channels available. Now O = 3/∆f.

<!-- b000146 | prose | pages [8] -->
Let N1 be the number of people who are within range of our ﬁrst repeater. We must update our Nc and Nf values accordingly. Thus

<!-- b000147 | prose | pages [8] -->
Nc = N1 and Nf = min(Nc, O)

<!-- b000148 | prose | pages [8] -->
Now we calculate the metric by which this model determines Private Line (CTCSS) repeater placement. Let

<!-- b000149 | prose | pages [8] -->
D = max(Nc −O, 0)

<!-- b000150 | prose | pages [8] -->
be the deﬁcit of available channels (i.e. the number of users who do not have access to a repeater channel). We update our matrix M by removing the users who are within range of the repeater. Now M is a (n −Nc) × 2 matrix. From here, if D > 0 we add CTCSS repeaters to mitigate this deﬁcit and if D = 0, we continue to place open repeaters and expand the network.

<!-- b000151 | prose | pages [8] -->
If D > 0, we will add a Private (CTCSS) Line. We calculate the optimal angle to place the CTCSS line a distance of dp from our ﬁrst repeater. We then determine the location to place the CTCSS repeater.

<!-- b000152 | prose | pages [8] -->
The explicit CTCSS algorithm is given below.

<!-- b000153 | furniture | pages [9] -->
Control Number: 11759

<!-- b000154 | furniture | pages [9] -->
Page 9 of 51

<!-- b000155 | prose | pages [9] -->
Data: Previously placed open repeater location, Ri−1 Result: The optimal location to place a new CTCSS Line Ri = (xi, yi) Let P be a partition of [0, 360] (in our case studies |P| = 360); for θ ∈P do

<!-- b000156 | prose | pages [9] -->
Rθ = (xθ, yθ) = Ri−1 + (dp cos(θ), dp sin(θ)); for j ∈[1, n −Nc] do

<!-- b000157 | prose | pages [9] -->
Let xj = Mj,1 and yj = Mj,2;

<!-- b000158 | prose | pages [9] -->
(xθ −xj)2 + (yθ −yj)2 ≤ds then

<!-- b000159 | prose | pages [9] -->
p

<!-- b000160 | prose | pages [9] -->
if

<!-- b000161 | prose | pages [9] -->
uθ = uθ + 1; end end end Let θc be the θ for which uθ is maximum. Then Ri = Ri−1 + ( dp cos(θc), dp sin(θc) ) is the optimal location for the new repeater.

<!-- b000162 | heading | pages [9] -->
Algorithm 1: Finding CTCSS Repeater Location

<!-- b000163 | prose | pages [9] -->
The addition of a CTCSS line corresponds to an additional 3/∆f channels. Therefore our new value for O is O = O′ + 3/∆f where O′ is the previous value of O. Now we recalculate Nc, Nf, and our deﬁcit D using our updated matrix M (which does not include points already covered by repeaters).

<!-- b000164 | prose | pages [9] -->
If D = 0 then all users who desire access have access. To increase the number of supported users, we will add an open repeater to expand our network. We use “k-means” cluster analysis to determine the most densly populated areas. After the cluster points are determined, we collect their locations and let {c1, ..., ck} be that collection of coordinates. The model snakes around the map by adding repeaters to include more users in the network.

<!-- b000165 | prose | pages [9] -->
The explicit open repeater placement algorithm is given below.

<!-- b000166 | prose | pages [9] -->
Data: Previously placed open repeater location, Ri−1 Result: The optimal location to place a new open repeater Ri = (xi, yi) for t ∈[0, k] do

<!-- b000167 | prose | pages [9] -->
Let θt be the angle from the current repeater Ri−1 to ct; Rt = (xt, yt) = Ri−1 + (dh cos(θt), dh sin(θt)); for j ∈[0, n −Nc] do

<!-- b000168 | prose | pages [9] -->
Let xj = Mj,1 and yj = Mj,2;

<!-- b000169 | prose | pages [9] -->
(xt −xj)2 + (yt −yj)2 ≤ds then

<!-- b000170 | prose | pages [9] -->
p

<!-- b000171 | prose | pages [9] -->
if

<!-- b000172 | prose | pages [9] -->
ut = ut + 1; end end end Let tc be the t for which ut is maximum. Then Ri = Ri−1 + (dh cos(θtc), dh sin(θtc)) is the optimal location for the new repeater.

<!-- b000173 | heading | pages [9] -->
Algorithm 2: Finding Open Repeater Location

<!-- b000174 | furniture | pages [10] -->
Control Number: 11759

<!-- b000175 | furniture | pages [10] -->
Page 10 of 51

<!-- b000176 | prose | pages [10] -->
The action of adding an open line did not add any new channels. We have, however, added new users to the network and must recalculate Nc, Nf, and our deﬁcit D using our updated matrix M (which does not include points already covered by repeaters). If D > 0, then we apply Algorithm 1 again and if D = 0, we apply Algorithm 2.

<!-- b000177 | prose | pages [10] -->
We repeat this process until Nf ≥1000. This would mean that there are at least 1,000 simultaneously supported users on our network.

<!-- b000178 | furniture | pages [11] -->
Control Number: 11759

<!-- b000179 | prose | pages [11] -->
5

<!-- b000180 | heading | pages [11] -->
The Branching Model

<!-- b000181 | furniture | pages [11] -->
Page 11 of 51

<!-- b000182 | prose | pages [11] -->
The aptly named Branching Model creates a backbone network of open repeaters that sup- ports a number of branch connections. All open repeater branches are designed along the shortest distance possible. This model provides us with a point of comparison for the ﬁrst model.

<!-- b000183 | caption | pages [11] -->
Figure 2 describes the creation of the backbone and branches.

<!-- b000184 | prose | pages [11] -->
Create and Score

<!-- b000185 | prose | pages [11] -->
Clusters

<!-- b000186 | prose | pages [11] -->
Create Backbone

<!-- b000187 | prose | pages [11] -->
Network

<!-- b000188 | prose | pages [11] -->
(Open)

<!-- b000189 | prose | pages [11] -->
Recreate

<!-- b000190 | prose | pages [11] -->
and Rescore Clusters

<!-- b000191 | prose | pages [11] -->
no

<!-- b000192 | prose | pages [11] -->
Connect

<!-- b000193 | prose | pages [11] -->
Highest

<!-- b000194 | prose | pages [11] -->
Enough

<!-- b000195 | prose | pages [11] -->
Score

<!-- b000196 | prose | pages [11] -->
Users?

<!-- b000197 | prose | pages [11] -->
Cluster

<!-- b000198 | prose | pages [11] -->
Add

<!-- b000199 | prose | pages [11] -->
yes

<!-- b000200 | prose | pages [11] -->
yes

<!-- b000201 | prose | pages [11] -->
End of

<!-- b000202 | prose | pages [11] -->
Enough

<!-- b000203 | prose | pages [11] -->
Repeater

<!-- b000204 | prose | pages [11] -->
no

<!-- b000205 | prose | pages [11] -->
Method

<!-- b000206 | prose | pages [11] -->
Channels?

<!-- b000207 | prose | pages [11] -->
(PL)

<!-- b000208 | caption | pages [11] -->
Figure 2: Flow Chart for Branching Model

<!-- b000209 | prose | pages [11] -->
5.1 Description

<!-- b000210 | prose | pages [11] -->
Akin to the ﬁrst model, the Branching Method uses k-means cluster analysis and scoring to determine the optimal placement of repeaters. The diﬀerence, however, is the process in which this model creates the network. The model creates a backbone network of open repeaters between the two highest scoring clusters.

<!-- b000211 | prose | pages [11] -->
After the backbone has been estab- lished, the model reclusters and rescores the remaining users and creates a branch of open repeaters between the existing network and the highest scoring cluster. This ensures that the fewest repeaters are used in branching out the network to high density locations. After the entire network has been established, the model places CTCSS repeaters to ensure chan-

<!-- b000212 | furniture | pages [12] -->
Control Number: 11759

<!-- b000213 | furniture | pages [12] -->
Page 12 of 51

<!-- b000214 | prose | pages [12] -->
nel availability is not a concern in user-dense locations so that all users may be supported simultaneously.

<!-- b000215 | prose | pages [12] -->
This model requires reclustering after every iteration.

<!-- b000216 | prose | pages [12] -->
5.2 Mathematical Intepretation

<!-- b000217 | prose | pages [12] -->
The Branching Model supports even more customization than the ﬁrst model. The param- eters relevant to this model are listed below.

<!-- b000218 | prose | pages [12] -->
Parameter Description n Number of users within 40 miles k Number of k-means cluster points ds Maximum distance for user-to-repeater communication hr Height of repeater towers dh Repeater output distance ∆f Frequency separation/ channel width ln Number of Long Distance Lines lc Number of Locations in Long Distance Connections

<!-- b000219 | prose | pages [12] -->
We will review a few deﬁnitions for consistency. Let Nc be the number of people with network connectivity (i.e. within range of a repeater) and Nf be the number of people with access to an available frequency range. The number of channels available will be denoted again by O. Initially, Nc = 0, Nf = 0 and O = 0.

<!-- b000220 | prose | pages [12] -->
Let n be the number of users within a 40 mile radius. With k-means clustering, we identify and score clusters of users.. Letting {c1, ..., ck} be the locations of the k cluster points, the model creates a backbone of repeaters between the two highest scoring cluster locations.

<!-- b000221 | prose | pages [12] -->
For each cluster point ci, we calculate how many users are within ds of ci, i.e. how many users will beneﬁt from the placement of a repeater there. We set R1 = ci for whichever i has the most people within range. Now calculate Nc as before. The algorithm continues until the desired number of users have been added (in our case this is 1000 users). This only means that users are within range of a repeater. This does not ensure that all users have available channels. This will be resolved after the branched network has been established.

<!-- b000222 | prose | pages [12] -->
The explicit open repeater branching algorithm is given below.

<!-- b000223 | furniture | pages [13] -->
Control Number: 11759

<!-- b000224 | furniture | pages [13] -->
Page 13 of 51

<!-- b000225 | prose | pages [13] -->
Data: First open repeater location, R1 = (x, y)

<!-- b000226 | heading | pages [13] -->
Result: The locations of the repeaters

<!-- b000227 | prose | pages [13] -->
for i ∈[1, k] do

<!-- b000228 | prose | pages [13] -->
Let (xi, yi) = ci;

<!-- b000229 | prose | pages [13] -->
(x −xi)2 + (y −yi)2;

<!-- b000230 | prose | pages [13] -->
p

<!-- b000231 | prose | pages [13] -->
φ(i) =

<!-- b000232 | prose | pages [13] -->
end Then T = (xi, yi) st φ(i) = max(φ([1, k])); θ = angle between R1,T; s = distance between R1, T; Set j = 2; while s > dh do

<!-- b000233 | prose | pages [13] -->
Rj = Rj−1 + (dh cos(θ), dh sin(θ)); Recalculate s; j = j + 1; end while Nc < 1000 do

<!-- b000234 | prose | pages [13] -->
Rerun “k-means” cluster analysis to obtain new {c1, ..., ck}; T = ci st ci has the most users in range; Choose i st Ri is the existing repeater closest to T; Let s be the distance between RT and T; Let θ be the distance between RT and T; while s > dh do

<!-- b000235 | prose | pages [13] -->
Rj = Rj−1 + (dh cos(θ), dh sin(θ)); Recalculate s; j = j + 1; end end

<!-- b000236 | heading | pages [13] -->
Algorithm 3: Branching Method Open Repeater Placement

<!-- b000237 | prose | pages [13] -->
With the open network established, we must resolve the issue of channel availability. This is easily accomplished by placement of CTCSS repeaters in high user density areas.

<!-- b000238 | prose | pages [13] -->
In our opinion, the method in which this model establishes long-distance CTCSS lines is out- standing. By specifying a diﬀerent value for ln, one can change the number of CTCSS lines connecting the most highly populated areas. While this potentially increases the number of repeaters, it oﬀers greater connectivity between regions. This is accomplished by ﬁrst running k-means cluster analysis on the user data and choosing the lc clusters with the most users in range. Starting from the cluster with the most users, we create a chain of repeaters with a particular CTCSS channel, a distance of dh apart, until the next closest repeater is in range (similar to the second half of Algorithm 3). This creates a long distance connection on a speciﬁc CTCSS channel. This allows long distance users to communicate with more densely populated areas (e.g. rural or sub-urban users communicating with an urban user) without wasting an open frequency in the dense location.

<!-- b000239 | furniture | pages [14] -->
Control Number: 11759

<!-- b000240 | furniture | pages [14] -->
Page 14 of 51

<!-- b000241 | prose | pages [14] -->
Once the speciﬁed number of long distance connections have been made, any deﬁcits in channel demand are mitigated by placing local CTCSS repeaters in highly populated areas (again by k-means clustering).

<!-- b000242 | prose | pages [14] -->
6

<!-- b000243 | heading | pages [14] -->
Model Comparison Summary

<!-- b000244 | prose | pages [14] -->
The fundamental similarities and diﬀerences between the models are:

<!-- b000245 | prose | pages [14] -->
Similarities

<!-- b000246 | prose | pages [14] -->
• k-means clustering is prevalant in both models. Both models make use of k- means cluster analysis to identify large groups of users. By ranking these clusters in terms of potential connected users, both models attempt to provide the most eﬃcient connectivity scheme possible.

<!-- b000247 | heading | pages [14] -->
• Variable-strength repeaters may be employed in both models. By accounting

<!-- b000248 | prose | pages [14] -->
for variable broadcasting strength, isolated users may be accomodated without fear of channel interference or an inordinate use of additional repeaters in both models.

<!-- b000249 | prose | pages [14] -->
• The change of frequency from a repeater (±600 kHz) is resolved last in both

<!-- b000250 | heading | pages [14] -->
models. After the repeaters are conﬁgured, the “up” and “down” repeater broadcast

<!-- b000251 | prose | pages [14] -->
assignments may be made in both models to ﬁt the speciﬁc conﬁguration of the network.

<!-- b000252 | prose | pages [14] -->
Diﬀerences

<!-- b000253 | heading | pages [14] -->
• The models generate the network diﬀerently. The “Bender” Snake Model places

<!-- b000254 | prose | pages [14] -->
open repeaters along a continuous trajectory as determined by cluster points. In con- trast, The Branching Model creates a single backbone and allows for growth in any direction toward a cluster point.

<!-- b000255 | prose | pages [14] -->
• Reclustering is required for the Branching Model. In order for branching to occur, the optimum target location must be determined after every iteration. The other model may utilize reclustering but does not require it.

<!-- b000256 | prose | pages [14] -->
• The method in which private lines are introduced diﬀers between the mod- els. The “Bender” Snake Model places private line repeaters as is necessary whereas the Branching Model places private line repeaters after the entire network has been established.

<!-- b000257 | furniture | pages [15] -->
Control Number: 11759

<!-- b000258 | furniture | pages [15] -->
Page 15 of 51

<!-- b000259 | prose | pages [15] -->
7 Case Studies

<!-- b000260 | prose | pages [15] -->
We developed two population distributions to test our models on. The two cases are: a city- like user distribution and a rural distribution with small towns of users. When we discuss “parity,” we refer to the ±600 kHz diﬀerence in the recieving and broadcast frequencies of the repeaters. The graphs that show these assignments represent each open line repeater as a node, each labeled with “+” or “-” accordingly. We assign parity to each repeater such that no one repeater is connected to the rest of the network solely through another repeater with identical parity. This prevents a signal being either stepped up or stepped down repeatedly such that it eventually falls outside the available frequency range and cannot be recieved.

<!-- b000261 | prose | pages [15] -->
The parameters for these case studies were set to values we deemed reasonable based on our research from our referenced sources.

<!-- b000262 | prose | pages [15] -->
7.1 City Distribution

<!-- b000263 | prose | pages [15] -->
This distribution represents a city (located at the center of the area) with surrounding suburbs/neighborhoods.

<!-- b000264 | caption | pages [15] -->
Figure 3: Surface Plot of Users

<!-- b000265 | furniture | pages [16] -->
Control Number: 11759

<!-- b000266 | heading | pages [16] -->
Snaking Model

<!-- b000267 | prose | pages [16] -->
Parameter

<!-- b000268 | furniture | pages [16] -->
Page 16 of 51

<!-- b000269 | prose | pages [16] -->
Description The number of users within 40mi n = 1400 Number of k-means cluster points k = 5 Maximum distance for user to repeater communication ds = 10mi Height of repeater towers to be placed hr = 150ft Repeater output distance2) dh = 15mi Frequency seperation ∆f = .025 Number of Long Distance Lines ln = 3 Number of Locations in Long Distance Connections lc = 5

<!-- b000270 | prose | pages [16] -->
The model places the ﬁrst open repeater slightly north of the city to cover most of the users located there. This creates a large channel deﬁcit and the model places two CTCSS repeaters on this iteration to compensate. Next, a repeater is placed to the northwest and the simulation proceeds to spiral counterclockwise around the city, placing CTCSS repeaters as necessary. The model also places two CTCSS repeaters on the fourth iteration. There are 9 open line repeaters and 8 CTCSS repeaters for a total of 17 repeaters.

<!-- b000271 | prose | pages [16] -->
"Bender" Snaking Method Repeater Placement

<!-- b000272 | prose | pages [16] -->
40

<!-- b000273 | prose | pages [16] -->
30

<!-- b000274 | prose | pages [16] -->
20

<!-- b000275 | prose | pages [16] -->
10

<!-- b000276 | prose | pages [16] -->
Miles

<!-- b000277 | prose | pages [16] -->
0

<!-- b000278 | prose | pages [16] -->
−10

<!-- b000279 | prose | pages [16] -->
−20

<!-- b000280 | prose | pages [16] -->
−30

<!-- b000281 | prose | pages [16] -->
Potential User Open Repeater

<!-- b000282 | prose | pages [16] -->
−40 −40 −30 −20 −10

<!-- b000283 | prose | pages [16] -->
CTCSS Repeater Cluster Pt

<!-- b000284 | prose | pages [16] -->
0 0 10 20 30 40

<!-- b000285 | prose | pages [16] -->
Miles Miles

<!-- b000286 | caption | pages [16] -->
Figure 4: Repeater Placement (Snaking Model)

<!-- b000287 | prose | pages [16] -->
The model creates a closed loop of 9 open line repeaters. Since this number is odd, the parity does not work bi-directionally around the loop. There will be some signal leakage when the two step-up repeaters communicate directly but the signal will travel in the opposite direction around the entire network and be recieved.

<!-- b000288 | furniture | pages [17] -->
Control Number: 11759

<!-- b000289 | prose | pages [17] -->
+

<!-- b000290 | prose | pages [17] -->
-

<!-- b000291 | prose | pages [17] -->
+

<!-- b000292 | furniture | pages [17] -->
Page 17 of 51

<!-- b000293 | prose | pages [17] -->
+

<!-- b000294 | prose | pages [17] -->
- -

<!-- b000295 | prose | pages [17] -->
-

<!-- b000296 | prose | pages [17] -->
+ +

<!-- b000297 | prose | pages [17] -->
+

<!-- b000298 | prose | pages [17] -->
-

<!-- b000299 | caption | pages [17] -->
Figure 5: Repeater Parity (Snaking Model)

<!-- b000300 | prose | pages [17] -->
The model places the ﬁrst open repeater in the city and creates three

<!-- b000301 | heading | pages [17] -->
Branching Model

<!-- b000302 | prose | pages [17] -->
main branches to cover the surrounding suburbia. This web structure is highlighed with the black lines. The branching structure of open line repeaters is designed to eﬃciently cover the surface area rather than simply rushing from one population center to the next linearly. This structure is created ﬁrst, and CTCSS lines are placed afterwords.

<!-- b000303 | prose | pages [17] -->
Branching Method Repeater Placement

<!-- b000304 | prose | pages [17] -->
40

<!-- b000305 | prose | pages [17] -->
30

<!-- b000306 | prose | pages [17] -->
20

<!-- b000307 | prose | pages [17] -->
10

<!-- b000308 | prose | pages [17] -->
Miles

<!-- b000309 | prose | pages [17] -->
0

<!-- b000310 | prose | pages [17] -->
−10

<!-- b000311 | prose | pages [17] -->
−20

<!-- b000312 | prose | pages [17] -->
−30

<!-- b000313 | prose | pages [17] -->
Potential User

<!-- b000314 | prose | pages [17] -->
−40 −40 −30 −20 −10

<!-- b000315 | prose | pages [17] -->
Open Repeater CTCSS Repeater

<!-- b000316 | prose | pages [17] -->
0 0 10 20 30 40

<!-- b000317 | prose | pages [17] -->
Miles

<!-- b000318 | caption | pages [17] -->
Figure 6: Repeater Placement (Branching Model)

<!-- b000319 | prose | pages [17] -->
The process of CTCSS repeater placement is designed to create higher connectivity than the Snaking model. In the Snaking model, CTCSS repeaters are used to provide more channels locally, but when the network is loaded to capacity not all users will be able to talk long- distance. In the Branching model, we assign one squelch tone as long distance, here denoted by 1 (blue circles). Each of these points has 3 CTCSS repeaters, denoted as types 1,2 and 3. Tones 4-8 provide local lines in a manner similar to Snaking. This model creates 8 open

<!-- b000320 | furniture | pages [18] -->
Control Number: 11759

<!-- b000321 | furniture | pages [18] -->
Page 18 of 51

<!-- b000322 | prose | pages [18] -->
Branching Method CTCSS Repeater Subaudible Channel Arrangment

<!-- b000323 | prose | pages [18] -->
40

<!-- b000324 | prose | pages [18] -->
30

<!-- b000325 | prose | pages [18] -->
7

<!-- b000326 | prose | pages [18] -->
20

<!-- b000327 | prose | pages [18] -->
1

<!-- b000328 | prose | pages [18] -->
10

<!-- b000329 | prose | pages [18] -->
Miles

<!-- b000330 | prose | pages [18] -->
0

<!-- b000331 | prose | pages [18] -->
1

<!-- b000332 | prose | pages [18] -->
4

<!-- b000333 | prose | pages [18] -->
−10

<!-- b000334 | prose | pages [18] -->
−20

<!-- b000335 | prose | pages [18] -->
−30

<!-- b000336 | prose | pages [18] -->
Potential User

<!-- b000337 | prose | pages [18] -->
−40 −40 −30 −20 −10

<!-- b000338 | prose | pages [18] -->
5

<!-- b000339 | prose | pages [18] -->
1 1

<!-- b000340 | prose | pages [18] -->
8

<!-- b000341 | prose | pages [18] -->
6

<!-- b000342 | prose | pages [18] -->
1

<!-- b000343 | prose | pages [18] -->
1

<!-- b000344 | prose | pages [18] -->
CTCSS Repeater

<!-- b000345 | prose | pages [18] -->
0 0 10 20 30 40

<!-- b000346 | prose | pages [18] -->
Miles Miles

<!-- b000347 | caption | pages [18] -->
Figure 7: CTCSS Line Placement (Branching Model)

<!-- b000348 | prose | pages [18] -->
repeaters and 17 CTCSS repeaters for a total of 26. This number is substantually higher than the “minimum number” of 17 that the Snaking model produced. These extra lines are necessitated by the long distance backbone. The aim of this model is to provide both the best connectivity with the fewest number of repeaters.

<!-- b000349 | prose | pages [18] -->
The parity assignment is quite simple here.

<!-- b000350 | prose | pages [18] -->
+

<!-- b000351 | prose | pages [18] -->
-

<!-- b000352 | prose | pages [18] -->
-

<!-- b000353 | prose | pages [18] -->
+

<!-- b000354 | prose | pages [18] -->
+ -

<!-- b000355 | prose | pages [18] -->
+ +

<!-- b000356 | prose | pages [18] -->
-

<!-- b000357 | prose | pages [18] -->
-

<!-- b000358 | caption | pages [18] -->
Figure 8: Repeater Parity (Branching Model)

<!-- b000359 | furniture | pages [19] -->
Control Number: 11759

<!-- b000360 | furniture | pages [19] -->
Page 19 of 51

<!-- b000361 | prose | pages [19] -->
7.2 Rural Distrubition

<!-- b000362 | prose | pages [19] -->
This distribution represents a rural area with eight small towns of concentrated population with approximately 100 people spread randomly throughout the area. The total user popu- lation is 1400. We attempt to provide connectivity to 1000 people using both the Snaking and Branching models.

<!-- b000363 | caption | pages [19] -->
Figure 9: Surface Plot of Users

<!-- b000364 | heading | pages [19] -->
Snaking Model

<!-- b000365 | prose | pages [19] -->
The model starts near the northwestern-most town. We note that it places the open-line repeater so that it covers all of the targeted town but approximately half of the population in the second town. This coverage is optimal, however a connectivity deﬁcit is created since more than 120 people lie within range and channel availability becomes an issue. The model then places a CTCSS repeater near the open repeater to provide more channels locally. This is not suﬃcient to cover the deﬁcit, so the model places an additional CTCSS repeater on the same spot, this one with a diﬀerent squelch tone. This resolves the deﬁcit so it resumes placing open-line repeaters. The next placement is essentially due south of the previous, as it gravitates towards the two southern clusters that represent the two towns in the area. The placement of this new repeater does not create a channel deﬁcit so there is no need for another CTCSS repeater. The model proceeds south again on the next iteration, then snakes around towards the southeastern town, and ﬁnally turns north, placing CTCSS repeaters as needed along the way. The open line repeater near the middle is placed last. Note that the 6th iteration (the southeastern most group) also places two CTCSS repeaters on the same spot for a total of 8 CTCSS repeaters and 10 open repeaters. The model uses 18 total repeaters to create a network that accomodates 1080 users.

<!-- b000366 | furniture | pages [20] -->
Control Number: 11759

<!-- b000367 | furniture | pages [20] -->
Page 20 of 51

<!-- b000368 | prose | pages [20] -->
"Bender" Snaking Method Repeater Placement

<!-- b000369 | prose | pages [20] -->
40

<!-- b000370 | prose | pages [20] -->
30

<!-- b000371 | prose | pages [20] -->
20

<!-- b000372 | prose | pages [20] -->
10

<!-- b000373 | prose | pages [20] -->
Miles

<!-- b000374 | prose | pages [20] -->
0

<!-- b000375 | prose | pages [20] -->
−10

<!-- b000376 | prose | pages [20] -->
−20

<!-- b000377 | prose | pages [20] -->
−30

<!-- b000378 | prose | pages [20] -->
Potential User Open Repeater

<!-- b000379 | prose | pages [20] -->
−40 −40 −30 −20 −10

<!-- b000380 | prose | pages [20] -->
CTCSS Repeater Cluster Pt

<!-- b000381 | prose | pages [20] -->
0 0 10 20 30 40

<!-- b000382 | prose | pages [20] -->
Miles

<!-- b000383 | caption | pages [20] -->
Figure 10: Repeater Placement (Snaking Model)

<!-- b000384 | prose | pages [20] -->
Repeater parity is assigned after the simulation is complete.

<!-- b000385 | prose | pages [20] -->
This is generally a simple process for the Snaking model. However, note the southeastern node group where there are two step up repeaters connected. While this will result in some signal leakage outside of the available spectrum, the path that involves the step down node allows these two step up nodes to communicate without signal loss.

<!-- b000386 | prose | pages [20] -->
+

<!-- b000387 | prose | pages [20] -->
-

<!-- b000388 | prose | pages [20] -->
+

<!-- b000389 | prose | pages [20] -->
+

<!-- b000390 | prose | pages [20] -->
-

<!-- b000391 | prose | pages [20] -->
+

<!-- b000392 | prose | pages [20] -->
-

<!-- b000393 | prose | pages [20] -->
+

<!-- b000394 | prose | pages [20] -->
+

<!-- b000395 | prose | pages [20] -->
-

<!-- b000396 | caption | pages [20] -->
Figure 11: Repeater Parity (Snaking Model)

<!-- b000397 | furniture | pages [21] -->
Control Number: 11759

<!-- b000398 | furniture | pages [21] -->
Page 21 of 51

<!-- b000399 | prose | pages [21] -->
The branching structure is highlighted with the black lines. The Branching Method four-long node line that connects the two biggest towns is the main spine, and all other node structures branch oﬀof this. The branching structure of open line repeaters is designed to eﬃciently cover the surface area rather than simply rushing from one population center to the next linearly. This structure is created ﬁrst, and CTCSS lines are placed afterwords.

<!-- b000400 | prose | pages [21] -->
Branching Method Repeater Placement

<!-- b000401 | prose | pages [21] -->
40

<!-- b000402 | prose | pages [21] -->
30

<!-- b000403 | prose | pages [21] -->
20

<!-- b000404 | prose | pages [21] -->
10

<!-- b000405 | prose | pages [21] -->
Miles

<!-- b000406 | prose | pages [21] -->
0

<!-- b000407 | prose | pages [21] -->
−10

<!-- b000408 | prose | pages [21] -->
−20

<!-- b000409 | prose | pages [21] -->
−30

<!-- b000410 | prose | pages [21] -->
Potential User

<!-- b000411 | prose | pages [21] -->
−40 −40 −30 −20 −10

<!-- b000412 | prose | pages [21] -->
Open Repeater CTCSS Repeater

<!-- b000413 | prose | pages [21] -->
0 10 20 30 40

<!-- b000414 | prose | pages [21] -->
Miles

<!-- b000415 | caption | pages [21] -->
Figure 12: Repeater Placement (Branching Model)

<!-- b000416 | prose | pages [21] -->
CTCSS Subaudible Channel Arrangement

<!-- b000417 | prose | pages [21] -->
40

<!-- b000418 | prose | pages [21] -->
30

<!-- b000419 | prose | pages [21] -->
20

<!-- b000420 | prose | pages [21] -->
7 6

<!-- b000421 | prose | pages [21] -->
1

<!-- b000422 | prose | pages [21] -->
10

<!-- b000423 | prose | pages [21] -->
1

<!-- b000424 | prose | pages [21] -->
Miles

<!-- b000425 | prose | pages [21] -->
0

<!-- b000426 | prose | pages [21] -->
−10

<!-- b000427 | prose | pages [21] -->
−20

<!-- b000428 | prose | pages [21] -->
−30

<!-- b000429 | prose | pages [21] -->
5

<!-- b000430 | prose | pages [21] -->
1

<!-- b000431 | prose | pages [21] -->
1

<!-- b000432 | prose | pages [21] -->
8

<!-- b000433 | prose | pages [21] -->
1

<!-- b000434 | prose | pages [21] -->
4

<!-- b000435 | prose | pages [21] -->
Open Repeater Potential User

<!-- b000436 | prose | pages [21] -->
−40 −40 −30 −20 −10

<!-- b000437 | prose | pages [21] -->
CTCSS Repeater

<!-- b000438 | prose | pages [21] -->
0 0 10 20 30 40

<!-- b000439 | prose | pages [21] -->
Miles Miles

<!-- b000440 | caption | pages [21] -->
Figure 13: CTCSS Line Placement (Branching Model)

<!-- b000441 | furniture | pages [22] -->
Control Number: 11759

<!-- b000442 | furniture | pages [22] -->
Page 22 of 51

<!-- b000443 | prose | pages [22] -->
The process of CTCSS repeater placement is designed to create higher connectivity than the Snaking model. In the Snaking model, CTCSS repeaters are used to provide more channels locally, but when the network is loaded to capacity not all users will be able to talk long- distance. In the Branching model, we assign one squelch tone as long distance, here denoted by 1 (blue circles). Each of these points has 3 CTCSS repeaters, one each of types: 1, 2 and 3. Tones 4-8 provide local lines in a manner similar to the Snaking method. This model creates 8 open repeaters and 17 CTCSS repeaters for a total of 25. This number is substantually higher than the “minimum number” of 18 that the Snaking model produces. These extra lines are necessitated by the building of the long distance backbone. The aim of this model is to provide better connectivity, and not provide an absolute minimum repeater number.

<!-- b000444 | prose | pages [22] -->
+

<!-- b000445 | prose | pages [22] -->
+

<!-- b000446 | prose | pages [22] -->
+

<!-- b000447 | prose | pages [22] -->
-

<!-- b000448 | prose | pages [22] -->
-

<!-- b000449 | prose | pages [22] -->
+

<!-- b000450 | prose | pages [22] -->
- +

<!-- b000451 | caption | pages [22] -->
Figure 14: Repeater Parity (Branching Model)

<!-- b000452 | prose | pages [22] -->
Parity assignment for this model is fairly trivial.

<!-- b000453 | prose | pages [22] -->
8 10,000 Simultaneous Users

<!-- b000454 | prose | pages [22] -->
Our model is highly adaptable to varying situations and stresses. As such, when considering repeater placement for a network capable of simulateously supporting 10,000 users, we simply run our models against a data set with a little over 10,000 users (we use 12,000). Our models work exactly as before when trying to support 1,000 users. An important point to note however, is that the frequency seperation must be lowered to accomodate more users. We choose the frequency separation to be 10 kHz for 10,000 users (whereas before we chose 25 kHz for 1,000 users).

<!-- b000455 | prose | pages [22] -->
The minimum number of repeaters necessary to simulateously support 10,000 users is 19 open repeaters and 33 CTCSS repeaters all running on a diﬀerent CTCSS tone for a total of 42 repeaters. We conclude that even with 10,000 users, an eﬃcient network can be established within the constaints of the problem.

<!-- b000456 | furniture | pages [23] -->
Control Number: 11759

<!-- b000457 | furniture | pages [23] -->
Page 23 of 51

<!-- b000458 | prose | pages [23] -->
Snaking Method Repeater Placement (10k users)

<!-- b000459 | prose | pages [23] -->
40

<!-- b000460 | prose | pages [23] -->
30

<!-- b000461 | prose | pages [23] -->
20

<!-- b000462 | prose | pages [23] -->
10

<!-- b000463 | prose | pages [23] -->
Miles

<!-- b000464 | prose | pages [23] -->
0

<!-- b000465 | prose | pages [23] -->
−10

<!-- b000466 | prose | pages [23] -->
−20

<!-- b000467 | prose | pages [23] -->
−30

<!-- b000468 | prose | pages [23] -->
−40 −40 −30 −20 −10 0 0 10 20 30 40

<!-- b000469 | prose | pages [23] -->
Miles Miles

<!-- b000470 | caption | pages [23] -->
Figure 15: Results for 10,000 Simultaneous Users

<!-- b000471 | prose | pages [23] -->
9 Mountainous Terrain

<!-- b000472 | prose | pages [23] -->
While VHF radio signals are blocked by large land structures, the line-of-sight propagation method also permits an increased eﬀective range when the height of the antenna is increased. As a result, the mountains could be used to our advantage by placing repeaters on top of them rather than around them. This is not a completely trivial ﬁx, however, as the new eﬀective distance is proportional to the square root of the antenna’s height. This would provide diminishing returns.

<!-- b000473 | prose | pages [23] -->
In the case where there is one large topographical peak (i.e. one large mountain peak), the obvious solution is to place one strong repeater on the mountain peak to provide the most coverage. However, now consider the case where this mountain does not have one discernable, well-deﬁned peak and the area containing these peaks is relatively large and wide-spread (i.e. a mountain range). These numerous peaks may block the signal from a single repeater on the mountain and may not be accessible from all surrounding areas. The strength of the signal may vary with the angle due to an uneven distribution of peaks and valleys in the mountain range. In this situation, we would use a multiple-repeater network conﬁgured around the base and valleys that naturally occur in the mountain range. This would circumvent the mountain range and allow for connectivity. However, this also eliminates the line-of-sight advantage that the mountain could provide. There would most likely be ways to leverage the height advantage the mountains provide on a case-by-case basis.

<!-- b000474 | furniture | pages [24] -->
Control Number: 11759

<!-- b000475 | furniture | pages [24] -->
Page 24 of 51

<!-- b000476 | heading | pages [24] -->
Sensitivity to Parameters

<!-- b000477 | prose | pages [24] -->
10

<!-- b000478 | prose | pages [24] -->
Since our model so heavily relies upon k-means cluster anal- Number of Cluster Points ysis, it is natural to wonder how the number of cluster points aﬀects model performance. By running our model with variable inital cluster points (k = 5, 10, 20) we are able to gauge whether this has a signiﬁcant impact on performance. We chose to use the rural population distrubition since it provided a more interesting analysis.

<!-- b000479 | prose | pages [24] -->
"Bender" Snaking Method Repeater Placement (k=10)

<!-- b000480 | prose | pages [24] -->
40

<!-- b000481 | prose | pages [24] -->
30

<!-- b000482 | prose | pages [24] -->
20

<!-- b000483 | prose | pages [24] -->
10

<!-- b000484 | prose | pages [24] -->
Miles

<!-- b000485 | prose | pages [24] -->
0

<!-- b000486 | prose | pages [24] -->
−10

<!-- b000487 | prose | pages [24] -->
−20

<!-- b000488 | prose | pages [24] -->
−30

<!-- b000489 | prose | pages [24] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000490 | prose | pages [24] -->
Miles

<!-- b000491 | prose | pages [24] -->
(a) k = 10

<!-- b000492 | prose | pages [24] -->
"Bender" Snaking Method Repeater Placement (k=20)

<!-- b000493 | prose | pages [24] -->
40

<!-- b000494 | prose | pages [24] -->
30

<!-- b000495 | prose | pages [24] -->
20

<!-- b000496 | prose | pages [24] -->
10

<!-- b000497 | prose | pages [24] -->
Miles

<!-- b000498 | prose | pages [24] -->
0

<!-- b000499 | prose | pages [24] -->
−10

<!-- b000500 | prose | pages [24] -->
−20

<!-- b000501 | prose | pages [24] -->
−30

<!-- b000502 | prose | pages [24] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000503 | prose | pages [24] -->
Miles

<!-- b000504 | prose | pages [24] -->
(b) k = 20

<!-- b000505 | caption | pages [24] -->
Figure 16: “Bender” Snaking Model Cluster Point Sensitivity Rural Case

<!-- b000506 | prose | pages [24] -->
When k = 5 or k = 10, the model determines that nine open line repeaters and eight CTCSS lines are necessary. When k = 20, the model requires eight open lines and eight CTCSS lines be available. We conclude that our model does not seem to be very sensitive to changes in the number of initial cluster points.

<!-- b000507 | prose | pages [24] -->
When determining optimal placement for repeaters, our model Seperation Distance places each repeater a distance of dh apart so that repeater connectivity and communi- cation is guaranteed. The value we use for dh will have a large inﬂuence on the performance of the model. In our case studies, we set dh = 15. This is the distance that a 150 ft repeater would be able to transmit its signal. For dh = 10 and dh = 20, the height of the necessary repeater is 66 ft. 8 in. and 266 ft. 8 in. respectively.

<!-- b000508 | prose | pages [24] -->
Tower Height (ft) dh 10 66’ 15 150’ 20 266’ Open 10 8 7

<!-- b000509 | prose | pages [24] -->
Clearly, tower height (and hence seperation distance) has a signiﬁcant impact on model performance. However, while increasing the tower height does decrease the minimum number

<!-- b000510 | furniture | pages [25] -->
Control Number: 11759

<!-- b000511 | prose | pages [25] -->
Branching Method Repeater Placement (d=10)

<!-- b000512 | prose | pages [25] -->
40

<!-- b000513 | prose | pages [25] -->
30

<!-- b000514 | prose | pages [25] -->
20

<!-- b000515 | prose | pages [25] -->
10

<!-- b000516 | prose | pages [25] -->
Miles

<!-- b000517 | prose | pages [25] -->
0

<!-- b000518 | prose | pages [25] -->
−10

<!-- b000519 | prose | pages [25] -->
−20

<!-- b000520 | prose | pages [25] -->
−30

<!-- b000521 | prose | pages [25] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000522 | prose | pages [25] -->
Miles

<!-- b000523 | prose | pages [25] -->
(a) d = 10

<!-- b000524 | furniture | pages [25] -->
Page 25 of 51

<!-- b000525 | prose | pages [25] -->
Branching Method Repeater Placement (d=20)

<!-- b000526 | prose | pages [25] -->
40

<!-- b000527 | prose | pages [25] -->
30

<!-- b000528 | prose | pages [25] -->
20

<!-- b000529 | prose | pages [25] -->
10

<!-- b000530 | prose | pages [25] -->
Miles

<!-- b000531 | prose | pages [25] -->
0

<!-- b000532 | prose | pages [25] -->
−10

<!-- b000533 | prose | pages [25] -->
−20

<!-- b000534 | prose | pages [25] -->
−30

<!-- b000535 | prose | pages [25] -->
−40 −40 −30 −20 −10 0 10 20 30 40

<!-- b000536 | prose | pages [25] -->
Miles

<!-- b000537 | prose | pages [25] -->
(b) d = 20

<!-- b000538 | caption | pages [25] -->
Figure 17: Branching Model Seperation Distance Sensitivity Rural Case

<!-- b000539 | prose | pages [25] -->
of repeaters necessary, it will increase the cost of each repeater. This is a choice the user will have to make.

<!-- b000540 | prose | pages [25] -->
Our algorithms run until the desired number of people are Initial Number of People connected to the network and there are enough channels available to those people. Changing the starting population of users drastically impacts model performance. This is not surprising as a higher population would allow our model to capture the desired number of people faster.

<!-- b000541 | prose | pages [25] -->
Open dh 1400 10 3000 10000 CTCSS 8 3 3 8 1 1 8

<!-- b000542 | prose | pages [25] -->
Therefore, the higher the initial number of potential users, the fewer repeaters are necessary to sustain 1000 simulateous users.

<!-- b000543 | heading | pages [25] -->
Strengths & Weaknesses

<!-- b000544 | prose | pages [25] -->
11

<!-- b000545 | heading | pages [25] -->
Strengths

<!-- b000546 | prose | pages [25] -->
• Versatility of the models. Both models are highly versatile and can account for We were very impressed that our model accomodates many changing parameters. 10,000 users under the established requirements.

<!-- b000547 | furniture | pages [26] -->
Control Number: 11759

<!-- b000548 | furniture | pages [26] -->
Page 26 of 51

<!-- b000549 | prose | pages [26] -->
• Smart clustering. The fact that reclustering can be implemented (or is required) in the models creates a smarter algorithm that targets the highest priority targets at that moment. This allows for the “best” decision possible to be made at any given iteration.

<!-- b000550 | prose | pages [26] -->
• Eﬃcient use of CTCSS Lines. Both models, even with 10,000 users, do not exhaust the use of private lines. These unused lines could accomodate more traﬃc if it were desired.

<!-- b000551 | heading | pages [26] -->
Weaknesses

<!-- b000552 | prose | pages [26] -->
• Large reliance on k-cluster analysis.

<!-- b000553 | prose | pages [26] -->
Other clustering methods exist and our choice to exclusively use k-clustering limits our model.

<!-- b000554 | prose | pages [26] -->
Running the models with diﬀerent clustering methods would have been more illuminating to see if there were more eﬃcient ways to network and support the users.

<!-- b000555 | prose | pages [26] -->
• No use of Quality Threshold.

<!-- b000556 | prose | pages [26] -->
Quality Threshold (QT) is a clustering method for which a distance treshhold, not the number of clusters, is set. Implenenting this method of clustering could have improved eﬃciency.

<!-- b000557 | prose | pages [26] -->
• Diﬃculty with populations close to target. We found that if only 1000 users were present, the algorithm would circle around itself trying to hunt down the last remaining user. We supplanted this concern with the assumption that there were more users than we desired to connect. We felt this was a realistic liberty to take as the problem did not state that there were precisely 1000 potential users in the area.

<!-- b000558 | prose | pages [26] -->
12

<!-- b000559 | heading | pages [26] -->
Conclusion

<!-- b000560 | prose | pages [26] -->
The absolute fewest number of repeaters required to support 1,000 users is 17. This number was created by the “Bender” Snaking Model with the city distribution of users. We felt this number was reasonable for the given area and user population. The Branching Model yielded a network of 26 repeaters but established connectivty for a signiﬁcantly larger area.

<!-- b000561 | prose | pages [26] -->
When considering the rural distribution, the “Bender” Snaking Model reported 18 necessary repeaters while the Branching Model reported 25. The diﬀerence in required repeaters (7) was consistent with the diﬀerence in repeaters for the city distribution (9).

<!-- b000562 | prose | pages [26] -->
By comparing the two models, we were able to make a few fundamental conclusions:

<!-- b000563 | prose | pages [26] -->
• Better connectivity requires more repeaters. We can’t argue with the minimum number of repreaters reported by our model but we did note that better connectivity

<!-- b000564 | furniture | pages [27] -->
Control Number: 11759

<!-- b000565 | furniture | pages [27] -->
Page 27 of 51

<!-- b000566 | prose | pages [27] -->
(which potentially correlates into better service) for the users required more repeaters. This seems true to life as a more robust networks of any kind can support a greater load.

<!-- b000567 | prose | pages [27] -->
• 54 CTCSS lines are not necessary. We never exhausted our pool of CTCSS lines. Even with the 10,000 user load, 12 CTCSS tones were still available to use.

<!-- b000568 | prose | pages [27] -->
• CTCSS lines have multiple applications. While CTCSS lines are primarily used to reduce interference problems in densely populated areas, they also may be used to establish dedicated long-distance communication lines.

<!-- b000569 | furniture | pages [28] -->
Control Number: 11759

<!-- b000570 | heading | pages [28] -->
References

<!-- b000571 | furniture | pages [28] -->
Page 28 of 51

<!-- b000572 | references | pages [28] -->
[1] Metropolitan Coordination Association, Inc. Coordination Guidelines, February 2011.

<!-- b000573 | references | pages [28] -->
http://www.metrocor.net/coordination guidelines.htm.

<!-- b000574 | references | pages [28] -->
[2] Metropolitan Coordination Association, Inc. CTCSS (PL) Tones Frequencies, February

<!-- b000575 | references | pages [28] -->
2011. http://www.metrocor.net/ctcss.htm.

<!-- b000576 | references | pages [28] -->
[3] Institute for Telecommunication Sciences. High Frequency Propegation Models, Febru-

<!-- b000577 | references | pages [28] -->
ary 2011. http://elbert.its.bldrdoc.gov/hf.html.

<!-- b000578 | references | pages [28] -->
[4] Adrian W. Graham, Nicholas C. Kirkman, and Peter M. Paul. Mobile Radio Network

<!-- b000579 | references | pages [28] -->
Design in the VHF and UHF Bands. John Wily & Sons, Ltd, West Sussex, England,

<!-- b000580 | references | pages [28] -->
2007.

<!-- b000581 | references | pages [28] -->
[5] Leif J. Harcke, Kenneth S. Dueker, and David B. Leeson. Frequency Coordination in

<!-- b000582 | references | pages [28] -->
the Amateur Radio Emergency Service. ECJ, 1(1):31–36, 2004.

<!-- b000583 | references | pages [28] -->
[6] Barry LcLarnon. Vhf/Uhf/Microwave Radio Propagation: A Primer for Digital Ex-

<!-- b000584 | references | pages [28] -->
A workship given at the 1997 TAPR/ARRL Digital Communications

<!-- b000585 | references | pages [28] -->
perimenters.

<!-- b000586 | references | pages [28] -->
Conference, February 2011. http://www.tapr.org/ve3jf.dcc97.html.

<!-- b000587 | references | pages [28] -->
League.

<!-- b000588 | references | pages [28] -->
[7] The

<!-- b000589 | references | pages [28] -->
American

<!-- b000590 | references | pages [28] -->
Radio

<!-- b000591 | references | pages [28] -->
Relay

<!-- b000592 | references | pages [28] -->
http://www.arrl.org/band-plan-1#2m.

<!-- b000593 | references | pages [28] -->
Band

<!-- b000594 | references | pages [28] -->
Plan,

<!-- b000595 | references | pages [28] -->
February

<!-- b000596 | references | pages [28] -->
2011.

<!-- b000597 | references | pages [28] -->
[8] Wikipedia. 2-Meter Band, February 2011. http://en.wikipedia.org/wiki/2-meter band.

<!-- b000598 | references | pages [28] -->
[9] Wikipedia.

<!-- b000599 | references | pages [28] -->
Amateur

<!-- b000600 | references | pages [28] -->
Radio

<!-- b000601 | references | pages [28] -->
Repeater,

<!-- b000602 | references | pages [28] -->
February

<!-- b000603 | references | pages [28] -->
2011.

<!-- b000604 | references | pages [28] -->
http://en.wikipedia.org/wiki/Amateur radio repeater.

<!-- b000605 | references | pages [28] -->
[10] Wikipedia.

<!-- b000606 | references | pages [28] -->
k-means

<!-- b000607 | references | pages [28] -->
Clustering,

<!-- b000608 | references | pages [28] -->
February

<!-- b000609 | references | pages [28] -->
2011.

<!-- b000610 | references | pages [28] -->
http://en.wikipedia.org/wiki/K-means clustering.

<!-- b000611 | references | pages [28] -->
High

<!-- b000612 | references | pages [28] -->
[11] Wikipedia.

<!-- b000613 | references | pages [28] -->
Very

<!-- b000614 | references | pages [28] -->
Frequency,

<!-- b000615 | references | pages [28] -->
February

<!-- b000616 | references | pages [28] -->
2011.

<!-- b000617 | references | pages [28] -->
http://en.wikipedia.org/wiki/Very high frequency.

<!-- b000618 | furniture | pages [29] -->
Control Number: 11759

<!-- b000619 | furniture | pages [29] -->
Page 29 of 51

<!-- b000620 | heading | pages [29] -->
Appendix A: Full-Page Plots

<!-- b000621 | prose | pages [29] -->
13

<!-- b000622 | prose | pages [29] -->
"Bender" Snaking Method Repeater Placement

<!-- b000623 | prose | pages [29] -->
40

<!-- b000624 | prose | pages [29] -->
30

<!-- b000625 | prose | pages [29] -->
20

<!-- b000626 | prose | pages [29] -->
10

<!-- b000627 | prose | pages [29] -->
Miles

<!-- b000628 | prose | pages [29] -->
0

<!-- b000629 | prose | pages [29] -->
−10

<!-- b000630 | prose | pages [29] -->
−20

<!-- b000631 | prose | pages [29] -->
−30

<!-- b000632 | prose | pages [29] -->
Open Repeater Potential User

<!-- b000633 | prose | pages [29] -->
−40 −40 −30 −20 −10

<!-- b000634 | prose | pages [29] -->
CTCSS Repeater Cluster Pt

<!-- b000635 | prose | pages [29] -->
0 0 10 20 30 40

<!-- b000636 | prose | pages [29] -->
Miles

<!-- b000637 | caption | pages [29] -->
Figure 18: Repeater Placement (Snaking Model)

<!-- b000638 | furniture | pages [30] -->
Control Number: 11759

<!-- b000639 | furniture | pages [30] -->
Page 30 of 51

<!-- b000640 | prose | pages [30] -->
Branching Method Repeater Placement

<!-- b000641 | prose | pages [30] -->
40

<!-- b000642 | prose | pages [30] -->
30

<!-- b000643 | prose | pages [30] -->
20

<!-- b000644 | prose | pages [30] -->
10

<!-- b000645 | prose | pages [30] -->
Miles

<!-- b000646 | prose | pages [30] -->
0

<!-- b000647 | prose | pages [30] -->
−10

<!-- b000648 | prose | pages [30] -->
−20

<!-- b000649 | prose | pages [30] -->
−30

<!-- b000650 | prose | pages [30] -->
Open Repeater Potential User

<!-- b000651 | prose | pages [30] -->
−40 −40 −30 −20 −10

<!-- b000652 | prose | pages [30] -->
CTCSS Repeater

<!-- b000653 | prose | pages [30] -->
0 10 20 30 40

<!-- b000654 | prose | pages [30] -->
Miles

<!-- b000655 | caption | pages [30] -->
Figure 19: Repeater Placement (Branching Model)

<!-- b000656 | furniture | pages [31] -->
Control Number: 11759

<!-- b000657 | furniture | pages [31] -->
Page 31 of 51

<!-- b000658 | prose | pages [31] -->
Branching Method CTCSS Repeater Subaudible Channel Arrangment

<!-- b000659 | prose | pages [31] -->
40

<!-- b000660 | prose | pages [31] -->
30

<!-- b000661 | prose | pages [31] -->
7

<!-- b000662 | prose | pages [31] -->
20

<!-- b000663 | prose | pages [31] -->
1

<!-- b000664 | prose | pages [31] -->
10

<!-- b000665 | prose | pages [31] -->
Miles

<!-- b000666 | prose | pages [31] -->
0

<!-- b000667 | prose | pages [31] -->
1

<!-- b000668 | prose | pages [31] -->
4

<!-- b000669 | prose | pages [31] -->
−10

<!-- b000670 | prose | pages [31] -->
−20

<!-- b000671 | prose | pages [31] -->
−30

<!-- b000672 | prose | pages [31] -->
Potential User

<!-- b000673 | prose | pages [31] -->
−40 −40 −30 −20 −10

<!-- b000674 | prose | pages [31] -->
5

<!-- b000675 | prose | pages [31] -->
1

<!-- b000676 | prose | pages [31] -->
8

<!-- b000677 | prose | pages [31] -->
6

<!-- b000678 | prose | pages [31] -->
1

<!-- b000679 | prose | pages [31] -->
1

<!-- b000680 | prose | pages [31] -->
CTCSS Repeater

<!-- b000681 | prose | pages [31] -->
0 0 10 20 30 40

<!-- b000682 | prose | pages [31] -->
Miles

<!-- b000683 | caption | pages [31] -->
Figure 20: CTCSS Line Placement (Branching Model)

<!-- b000684 | furniture | pages [32] -->
Control Number: 11759

<!-- b000685 | furniture | pages [32] -->
Page 32 of 51

<!-- b000686 | prose | pages [32] -->
"Bender" Snaking Method Repeater Placement

<!-- b000687 | prose | pages [32] -->
40

<!-- b000688 | prose | pages [32] -->
30

<!-- b000689 | prose | pages [32] -->
20

<!-- b000690 | prose | pages [32] -->
10

<!-- b000691 | prose | pages [32] -->
Miles

<!-- b000692 | prose | pages [32] -->
0

<!-- b000693 | prose | pages [32] -->
−10

<!-- b000694 | prose | pages [32] -->
−20

<!-- b000695 | prose | pages [32] -->
−30

<!-- b000696 | prose | pages [32] -->
Open Repeater Potential User

<!-- b000697 | prose | pages [32] -->
−40 −40 −30 −20 −10

<!-- b000698 | prose | pages [32] -->
CTCSS Repeater Cluster Pt

<!-- b000699 | prose | pages [32] -->
0 10 20 30 40

<!-- b000700 | prose | pages [32] -->
Miles

<!-- b000701 | caption | pages [32] -->
Figure 21: Repeater Placement (Snaking Model)

<!-- b000702 | furniture | pages [33] -->
Control Number: 11759

<!-- b000703 | furniture | pages [33] -->
Page 33 of 51

<!-- b000704 | prose | pages [33] -->
Branching Method Repeater Placement

<!-- b000705 | prose | pages [33] -->
40

<!-- b000706 | prose | pages [33] -->
30

<!-- b000707 | prose | pages [33] -->
20

<!-- b000708 | prose | pages [33] -->
10

<!-- b000709 | prose | pages [33] -->
Miles

<!-- b000710 | prose | pages [33] -->
0

<!-- b000711 | prose | pages [33] -->
−10

<!-- b000712 | prose | pages [33] -->
−20

<!-- b000713 | prose | pages [33] -->
−30

<!-- b000714 | prose | pages [33] -->
Open Repeater Potential User

<!-- b000715 | prose | pages [33] -->
−40 −40 −30 −20 −10

<!-- b000716 | prose | pages [33] -->
CTCSS Repeater

<!-- b000717 | prose | pages [33] -->
0 10 20 30 40

<!-- b000718 | prose | pages [33] -->
Miles

<!-- b000719 | caption | pages [33] -->
Figure 22: Repeater Placement (Branching Model)

<!-- b000720 | furniture | pages [34] -->
Control Number: 11759

<!-- b000721 | furniture | pages [34] -->
Page 34 of 51

<!-- b000722 | prose | pages [34] -->
CTCSS Subaudible Channel Arrangement

<!-- b000723 | prose | pages [34] -->
40

<!-- b000724 | prose | pages [34] -->
30

<!-- b000725 | prose | pages [34] -->
20

<!-- b000726 | prose | pages [34] -->
7 6

<!-- b000727 | prose | pages [34] -->
1

<!-- b000728 | prose | pages [34] -->
10

<!-- b000729 | prose | pages [34] -->
1

<!-- b000730 | prose | pages [34] -->
Miles

<!-- b000731 | prose | pages [34] -->
0

<!-- b000732 | prose | pages [34] -->
−10

<!-- b000733 | prose | pages [34] -->
−20

<!-- b000734 | prose | pages [34] -->
−30

<!-- b000735 | prose | pages [34] -->
5

<!-- b000736 | prose | pages [34] -->
1

<!-- b000737 | prose | pages [34] -->
1

<!-- b000738 | prose | pages [34] -->
8

<!-- b000739 | prose | pages [34] -->
1

<!-- b000740 | prose | pages [34] -->
4

<!-- b000741 | prose | pages [34] -->
Open Repeater Potential User

<!-- b000742 | prose | pages [34] -->
−40 −40 −30 −20 −10

<!-- b000743 | prose | pages [34] -->
CTCSS Repeater

<!-- b000744 | prose | pages [34] -->
0 0 10 20 30 40

<!-- b000745 | prose | pages [34] -->
Miles

<!-- b000746 | caption | pages [34] -->
Figure 23: CTCSS Line Placement (Branching Model)

<!-- b000747 | furniture | pages [35] -->
Control Number: 11759

<!-- b000748 | furniture | pages [35] -->
Page 35 of 51

<!-- b000749 | prose | pages [35] -->
Snaking Method Repeater Placement (10k users)

<!-- b000750 | prose | pages [35] -->
40

<!-- b000751 | prose | pages [35] -->
30

<!-- b000752 | prose | pages [35] -->
20

<!-- b000753 | prose | pages [35] -->
10

<!-- b000754 | prose | pages [35] -->
Miles

<!-- b000755 | prose | pages [35] -->
0

<!-- b000756 | prose | pages [35] -->
−10

<!-- b000757 | prose | pages [35] -->
−20

<!-- b000758 | prose | pages [35] -->
−30

<!-- b000759 | prose | pages [35] -->
−40 −40 −30 −20 −10

<!-- b000760 | prose | pages [35] -->
Miles

<!-- b000761 | prose | pages [35] -->
0 0 10 20 30 40

<!-- b000762 | caption | pages [35] -->
Figure 24: Results for 10,000 Simultaneous Users

<!-- b000763 | furniture | pages [36] -->
Control Number: 11759

<!-- b000764 | furniture | pages [36] -->
Page 36 of 51

<!-- b000765 | prose | pages [36] -->
14

<!-- b000766 | heading | pages [36] -->
Appendix B: Source Code

<!-- b000767 | heading | pages [36] -->
“Bender” Snaking Model:

<!-- b000768 | prose | pages [36] -->
load 'C:\Users\*****\Desktop\MCM 2011\townsdata3.txt'; 1

<!-- b000769 | prose | pages [36] -->
sepdist = 10; %seperation distance 2

<!-- b000770 | prose | pages [36] -->
plsepdist =1; %Private line seperation distance 3

<!-- b000771 | prose | pages [36] -->
xcor = townsdata3(:,2); 4

<!-- b000772 | prose | pages [36] -->
ycor = townsdata3(:,3); 5

<!-- b000773 | prose | pages [36] -->
totalnum = zeros(2000,2); 6

<!-- b000774 | prose | pages [36] -->
connected = 0; 7

<!-- b000775 | prose | pages [36] -->
n=zeros(2000,5); 8

<!-- b000776 | prose | pages [36] -->
inrange = zeros(360); 9

<!-- b000777 | prose | pages [36] -->
ply = zeros(360,1); 10

<!-- b000778 | prose | pages [36] -->
plx = zeros(360,1); 11

<!-- b000779 | prose | pages [36] -->
ind = 0; 12

<!-- b000780 | prose | pages [36] -->
openchannels=0; 13

<!-- b000781 | prose | pages [36] -->
∆f = .025; 14

<!-- b000782 | prose | pages [36] -->
cover = 0; 15

<!-- b000783 | prose | pages [36] -->
it = 1; 16

<!-- b000784 | prose | pages [36] -->
plit =0; 17

<!-- b000785 | prose | pages [36] -->
rep=zeros(50,2); 18

<!-- b000786 | prose | pages [36] -->
population = length(xcor); 19

<!-- b000787 | prose | pages [36] -->
iteration=0; 20

<!-- b000788 | prose | pages [36] -->
concat=horzcat(xcor,ycor); 21

<!-- b000789 | prose | pages [36] -->
notcovered=zeros(population,2); 22

<!-- b000790 | prose | pages [36] -->
numclus=10; 23

<!-- b000791 | prose | pages [36] -->
[clusid,clusters]=kmeans(concat,numclus); 24

<!-- b000792 | prose | pages [36] -->
clusscr=zeros(numclus); 25

<!-- b000793 | prose | pages [36] -->
26

<!-- b000794 | prose | pages [36] -->
27

<!-- b000795 | prose | pages [36] -->
for i = 1:population 28

<!-- b000796 | prose | pages [36] -->
for n = 1:numclus 29

<!-- b000797 | prose | pages [36] -->
if clusid(i) == n 30

<!-- b000798 | prose | pages [36] -->
clusscr(n) = clusscr(n) + 1; 31

<!-- b000799 | prose | pages [36] -->
end 32

<!-- b000800 | prose | pages [36] -->
end 33

<!-- b000801 | prose | pages [36] -->
end 34

<!-- b000802 | prose | pages [36] -->
35

<!-- b000803 | prose | pages [36] -->
%Plot Users and clusters 36

<!-- b000804 | prose | pages [36] -->
plot(concat(:,1),concat(:,2),'.','MarkerSize',1); 37

<!-- b000805 | prose | pages [36] -->
hold on 38

<!-- b000806 | prose | pages [36] -->
plot(clusters(:,1),clusters(:,2),'kx',... 39

<!-- b000807 | prose | pages [36] -->
'MarkerSize',20,'LineWidth',2); 40

<!-- b000808 | prose | pages [36] -->
hold on 41

<!-- b000809 | prose | pages [36] -->
plot(clusters(:,1),clusters(:,2),'ko',... 42

<!-- b000810 | prose | pages [36] -->
'MarkerSize',20,'LineWidth',2); 43

<!-- b000811 | prose | pages [36] -->
hold off 44

<!-- b000812 | prose | pages [36] -->
45

<!-- b000813 | prose | pages [36] -->
46

<!-- b000814 | prose | pages [36] -->
47

<!-- b000815 | prose | pages [36] -->
48

<!-- b000816 | furniture | pages [37] -->
Control Number: 11759

<!-- b000817 | furniture | pages [37] -->
Page 37 of 51

<!-- b000818 | prose | pages [37] -->
%Find inital repeater location 49

<!-- b000819 | prose | pages [37] -->
for i=1:5, 50

<!-- b000820 | prose | pages [37] -->
for j=1:population, 51

<!-- b000821 | prose | pages [37] -->
n(i,j)=sqrt(((clusters(i,1)-xcor(j))ˆ2)+((clusters(i,2)-ycor(j))ˆ2)); 52

<!-- b000822 | prose | pages [37] -->
if n(i,j)≤sepdist 53

<!-- b000823 | prose | pages [37] -->
totalnum(i,1)=totalnum(i,1)+1; 54

<!-- b000824 | prose | pages [37] -->
end 55

<!-- b000825 | prose | pages [37] -->
end 56

<!-- b000826 | prose | pages [37] -->
end 57

<!-- b000827 | prose | pages [37] -->
58

<!-- b000828 | prose | pages [37] -->
[C,I]=max(totalnum); 59

<!-- b000829 | prose | pages [37] -->
index=I(1); 60

<!-- b000830 | prose | pages [37] -->
rep(1,1)=clusters(index,1); 61

<!-- b000831 | prose | pages [37] -->
rep(1,2)=clusters(index,1); 62

<!-- b000832 | prose | pages [37] -->
openchannels =3/∆f; 63

<!-- b000833 | prose | pages [37] -->
64

<!-- b000834 | prose | pages [37] -->
for i=1:population, 65

<!-- b000835 | prose | pages [37] -->
if sqrt(((rep(1,1)-xcor(i))ˆ2)+((rep(1,2)-ycor(i))ˆ2))>sepdist 66

<!-- b000836 | prose | pages [37] -->
ind = ind +1; 67

<!-- b000837 | prose | pages [37] -->
notcovered(ind,1)=xcor(i); 68

<!-- b000838 | prose | pages [37] -->
notcovered(ind,2)=ycor(i); 69

<!-- b000839 | prose | pages [37] -->
end 70

<!-- b000840 | prose | pages [37] -->
end 71

<!-- b000841 | prose | pages [37] -->
72

<!-- b000842 | prose | pages [37] -->
cover = totalnum(index,1); 73

<!-- b000843 | prose | pages [37] -->
population = population-cover; 74

<!-- b000844 | prose | pages [37] -->
connected = min(totalnum(index,1),openchannels); 75

<!-- b000845 | prose | pages [37] -->
deficit = max(totalnum(index,1) - connected,0); 76

<!-- b000846 | prose | pages [37] -->
77

<!-- b000847 | prose | pages [37] -->
78

<!-- b000848 | prose | pages [37] -->
79

<!-- b000849 | prose | pages [37] -->
disp('the first repeater will be placed at'),disp('x='),disp(rep(1,1)),disp('y='), disp(rep 80

<!-- b000850 | prose | pages [37] -->
disp('number connected'),disp(connected); 81

<!-- b000851 | prose | pages [37] -->
disp('deficit'),disp(deficit); 82

<!-- b000852 | prose | pages [37] -->
disp('under cover'),disp(cover); 83

<!-- b000853 | prose | pages [37] -->
disp('open channels'),disp(openchannels); 84

<!-- b000854 | prose | pages [37] -->
disp('population'),disp(population); 85

<!-- b000855 | prose | pages [37] -->
dlmwrite('C:\Users\*****\Desktop\MCM 2011\winner.txt',I,'\t'); 86

<!-- b000856 | prose | pages [37] -->
dlmwrite('C:\Users\*****\Desktop\MCM 2011\distances.txt',n,'\t'); 87

<!-- b000857 | prose | pages [37] -->
dlmwrite('C:\Users\*****\Desktop\MCM 2011\proximity.txt',totalnum,'\t') 88

<!-- b000858 | prose | pages [37] -->
89

<!-- b000859 | prose | pages [37] -->
while connected<1000, 90

<!-- b000860 | prose | pages [37] -->
iteration=iteration+1; 91

<!-- b000861 | prose | pages [37] -->
inrange=zeros(1000); 92

<!-- b000862 | prose | pages [37] -->
onrange=zeros(1000); 93

<!-- b000863 | prose | pages [37] -->
if deficit >0 94

<!-- b000864 | prose | pages [37] -->
plit=plit+1; 95

<!-- b000865 | prose | pages [37] -->
for theta=1:360, 96

<!-- b000866 | prose | pages [37] -->
plx(theta) = rep(it,1)+plsepdist*cos((3.14159*theta)/180); 97

<!-- b000867 | prose | pages [37] -->
ply(theta) = rep(it,2)+plsepdist*sin((3.14159*theta)/180); 98

<!-- b000868 | prose | pages [37] -->
if ((plx(theta)≥-40) && (plx(theta)≤40)) 99

<!-- b000869 | prose | pages [37] -->
if ((ply(theta)≥-40) && (ply(theta)≤40)) 100

<!-- b000870 | prose | pages [37] -->
for i=1:population, 101

<!-- b000871 | prose | pages [37] -->
dist(i,1)=sqrt((plx(theta)-notcovered(i,2*iteration-1))ˆ2+(ply 102

<!-- b000872 | furniture | pages [38] -->
Control Number: 11759

<!-- b000873 | furniture | pages [38] -->
Page 38 of 51

<!-- b000874 | prose | pages [38] -->
if dist(i,1)≤sepdist 103

<!-- b000875 | prose | pages [38] -->
inrange(theta) = inrange(theta) +1; 104

<!-- b000876 | prose | pages [38] -->
end 105

<!-- b000877 | prose | pages [38] -->
end 106

<!-- b000878 | prose | pages [38] -->
end 107

<!-- b000879 | prose | pages [38] -->
end 108

<!-- b000880 | prose | pages [38] -->
end 109

<!-- b000881 | prose | pages [38] -->
[C,I] = max(inrange); 110

<!-- b000882 | prose | pages [38] -->
angle = I(1); 111

<!-- b000883 | prose | pages [38] -->
reppl(plit,1)= rep(it,1)+plsepdist*cos((3.14159*angle)/180); 112

<!-- b000884 | prose | pages [38] -->
reppl(plit,2)= rep(it,2)+plsepdist*sin((3.14159*angle)/180); 113

<!-- b000885 | prose | pages [38] -->
added=0; 114

<!-- b000886 | prose | pages [38] -->
115

<!-- b000887 | prose | pages [38] -->
openchannels = openchannels +(3/∆f); 116

<!-- b000888 | prose | pages [38] -->
117

<!-- b000889 | prose | pages [38] -->
%%REMOVE ENTRIES WHICH HAVE BEEN USED 118

<!-- b000890 | prose | pages [38] -->
ind=0; 119

<!-- b000891 | prose | pages [38] -->
for i=1:population, 120

<!-- b000892 | prose | pages [38] -->
if sqrt(((rep(it,1)-notcovered(i,2*iteration-1))ˆ2)+((rep(it,2)-notcovered 121

<!-- b000893 | prose | pages [38] -->
ind = ind +1; 122

<!-- b000894 | prose | pages [38] -->
notcovered(ind,2*iteration+1)=notcovered(i,2*iteration-1); 123

<!-- b000895 | prose | pages [38] -->
notcovered(ind,2*iteration+2)=notcovered(i,2*iteration); 124

<!-- b000896 | prose | pages [38] -->
else 125

<!-- b000897 | prose | pages [38] -->
added=added+1; 126

<!-- b000898 | prose | pages [38] -->
end 127

<!-- b000899 | prose | pages [38] -->
end 128

<!-- b000900 | prose | pages [38] -->
129

<!-- b000901 | prose | pages [38] -->
cover = cover + added; 130

<!-- b000902 | prose | pages [38] -->
population = population - added; 131

<!-- b000903 | prose | pages [38] -->
connected = min(cover,openchannels); 132

<!-- b000904 | prose | pages [38] -->
deficit = max(cover - connected,0); 133

<!-- b000905 | prose | pages [38] -->
134

<!-- b000906 | prose | pages [38] -->
disp('the PL repeater will be placed at'),disp('x='),disp(reppl(plit,1)),disp( 135

<!-- b000907 | prose | pages [38] -->
disp('added'),disp(added); 136

<!-- b000908 | prose | pages [38] -->
disp('cover'),disp(cover); 137

<!-- b000909 | prose | pages [38] -->
disp('people connected:'),disp(connected); 138

<!-- b000910 | prose | pages [38] -->
disp('deficit'),disp(deficit); 139

<!-- b000911 | prose | pages [38] -->
disp('open channels'),disp(openchannels); 140

<!-- b000912 | prose | pages [38] -->
disp('population'),disp(population); 141

<!-- b000913 | prose | pages [38] -->
end 142

<!-- b000914 | prose | pages [38] -->
143

<!-- b000915 | prose | pages [38] -->
if deficit==0 144

<!-- b000916 | prose | pages [38] -->
it = it+1; 145

<!-- b000917 | prose | pages [38] -->
inrange=zeros(5); 146

<!-- b000918 | prose | pages [38] -->
onrange = zeros(5); 147

<!-- b000919 | prose | pages [38] -->
d = zeros(5); 148

<!-- b000920 | prose | pages [38] -->
for clusterno=1:5, 149

<!-- b000921 | prose | pages [38] -->
150

<!-- b000922 | prose | pages [38] -->
d(clusterno)=sqrt((rep(it-1,1)-clusters(clusterno,1))ˆ2+(rep(it-1,2)-cluste 151

<!-- b000923 | prose | pages [38] -->
if ((rep(it-1,1)≥clusters(clusterno,1))&&(rep(it-1,2)≤clusters(clusterno,2) 152

<!-- b000924 | prose | pages [38] -->
ang(clusterno)= acos((clusters(clusterno,1)-rep(it-1,1))/d(clusterno)); 153

<!-- b000925 | prose | pages [38] -->
elseif ((rep(it-1,1)>clusters(clusterno,1))&&(rep(it-1,2)≥clusters(clustern 154

<!-- b000926 | prose | pages [38] -->
ang(clusterno)=2*pi-acos((clusters(clusterno,1)-rep(it-1,1))/d(clustern 155

<!-- b000927 | prose | pages [38] -->
elseif ((rep(it-1,1)≤clusters(clusterno,1))&&(rep(it-1,2)≥clusters(clustern 156

<!-- b000928 | furniture | pages [39] -->
Control Number: 11759

<!-- b000929 | furniture | pages [39] -->
Page 39 of 51

<!-- b000930 | prose | pages [39] -->
ang(clusterno)=2*pi-acos((clusters(clusterno,1)-rep(it-1,1))/d(clustern 157

<!-- b000931 | prose | pages [39] -->
else 158

<!-- b000932 | prose | pages [39] -->
ang(clusterno)=acos((clusters(clusterno,1)-rep(1,1))/d(clusterno)); 159

<!-- b000933 | prose | pages [39] -->
end 160

<!-- b000934 | prose | pages [39] -->
161

<!-- b000935 | prose | pages [39] -->
162

<!-- b000936 | prose | pages [39] -->
%% 163

<!-- b000937 | prose | pages [39] -->
%{ 164

<!-- b000938 | prose | pages [39] -->
165

<!-- b000939 | prose | pages [39] -->
if ((rep(it-1,1)≥clusters(clusterno,1))&&(rep(it-1,2)≤clusters(clusterno,2) 166

<!-- b000940 | prose | pages [39] -->
ang(clusterno)=pi-asin((clusters(clusterno,2)-rep(it-1,2))/d(clusterno) 167

<!-- b000941 | prose | pages [39] -->
elseif ((rep(it-1,1)≥clusters(clusterno,1))&&(rep(it-1,2)≥clusters(clustern 168

<!-- b000942 | prose | pages [39] -->
ang(clusterno)=pi+asin((rep(it-1,2)-clusters(clusterno,2))/d(clusterno) 169

<!-- b000943 | prose | pages [39] -->
elseif ((rep(it-1,1)≤clusters(clusterno,1))&&(rep(it-1,2)≥clusters(clustern 170

<!-- b000944 | prose | pages [39] -->
ang(clusterno)=2*pi-asin((rep(it-1,2)-clusters(clusterno,2))/d(clustern 171

<!-- b000945 | prose | pages [39] -->
else 172

<!-- b000946 | prose | pages [39] -->
ang(clusterno)=asin((clusters(clusterno,2)-rep(it-1,2))/d(clusterno)) 173

<!-- b000947 | prose | pages [39] -->
end 174

<!-- b000948 | prose | pages [39] -->
175

<!-- b000949 | prose | pages [39] -->
%} 176

<!-- b000950 | prose | pages [39] -->
%% 177

<!-- b000951 | prose | pages [39] -->
x(clusterno)=rep(it-1,1)+sepdist*1.5*cos(ang(clusterno)); 178

<!-- b000952 | prose | pages [39] -->
y(clusterno)=rep(it-1,2)+sepdist*1.5*sin(ang(clusterno)); 179

<!-- b000953 | prose | pages [39] -->
if ((x(clusterno)≥-40) && (x(clusterno)≤40)&&(y(clusterno)≥-40)&&(y(cluster 180

<!-- b000954 | prose | pages [39] -->
for i=1:population, 181

<!-- b000955 | prose | pages [39] -->
if sqrt((x(clusterno)-notcovered(i,2*iteration-1))ˆ2+(y(cluster 182

<!-- b000956 | prose | pages [39] -->
inrange(clusterno) = inrange(clusterno) +1; 183

<!-- b000957 | prose | pages [39] -->
end 184

<!-- b000958 | prose | pages [39] -->
end 185

<!-- b000959 | prose | pages [39] -->
for i=1:population, 186

<!-- b000960 | prose | pages [39] -->
if sqrt((clusters(clusterno,1)-notcovered(i,2*iteration-1))ˆ2+ 187

<!-- b000961 | prose | pages [39] -->
onrange(clusterno) = onrange(clusterno) +1; 188

<!-- b000962 | prose | pages [39] -->
end 189

<!-- b000963 | prose | pages [39] -->
end 190

<!-- b000964 | prose | pages [39] -->
else 191

<!-- b000965 | prose | pages [39] -->
inrange(clusterno)=-100; 192

<!-- b000966 | prose | pages [39] -->
end 193

<!-- b000967 | prose | pages [39] -->
194

<!-- b000968 | prose | pages [39] -->
end 195

<!-- b000969 | prose | pages [39] -->
196

<!-- b000970 | prose | pages [39] -->
[C,I] = max(inrange); 197

<!-- b000971 | prose | pages [39] -->
198

<!-- b000972 | prose | pages [39] -->
angleid = I(1); 199

<!-- b000973 | prose | pages [39] -->
rep(it,1)=rep(it-1,1)+sepdist*1.5*cos(ang(angleid)); 200

<!-- b000974 | prose | pages [39] -->
rep(it,2)=rep(it-1,2)+sepdist*1.5*sin(ang(angleid)); 201

<!-- b000975 | prose | pages [39] -->
202

<!-- b000976 | prose | pages [39] -->
if ((rep(it,1)≥-40)&&(rep(it,1)≤40)&&(rep(it,2)≥-40)&&(rep(it,2)≤40)) 203

<!-- b000977 | prose | pages [39] -->
ind=0; 204

<!-- b000978 | prose | pages [39] -->
added=0; 205

<!-- b000979 | prose | pages [39] -->
for i=1:population, 206

<!-- b000980 | prose | pages [39] -->
if sqrt(((rep(it,1)-notcovered(i,2*iteration-1))ˆ2)+((rep(it,2)-notcove 207

<!-- b000981 | prose | pages [39] -->
ind = ind +1; 208

<!-- b000982 | prose | pages [39] -->
notcovered(ind,2*iteration+1)=notcovered(i,2*iteration-1); 209

<!-- b000983 | prose | pages [39] -->
notcovered(ind,2*iteration+2)=notcovered(i,2*iteration); 210

<!-- b000984 | furniture | pages [40] -->
Control Number: 11759

<!-- b000985 | furniture | pages [40] -->
Page 40 of 51

<!-- b000986 | prose | pages [40] -->
else 211

<!-- b000987 | prose | pages [40] -->
added=added+1; 212

<!-- b000988 | prose | pages [40] -->
end 213

<!-- b000989 | prose | pages [40] -->
end 214

<!-- b000990 | prose | pages [40] -->
else 215

<!-- b000991 | prose | pages [40] -->
theid=1; 216

<!-- b000992 | prose | pages [40] -->
217

<!-- b000993 | prose | pages [40] -->
while ((rep(it,1)<-40)||(rep(it,1)>40)||(rep(it,2)<-40)||(rep(it,2)>40)) 218

<!-- b000994 | prose | pages [40] -->
rep(it,1)=rep(it-1,1)+sepdist*1.5*cos(ang(theid)); 219

<!-- b000995 | prose | pages [40] -->
rep(it,2)=rep(it-1,2)+sepdist*1.5*sin(ang(theid)); 220

<!-- b000996 | prose | pages [40] -->
theid =theid +1; 221

<!-- b000997 | prose | pages [40] -->
end 222

<!-- b000998 | prose | pages [40] -->
223

<!-- b000999 | prose | pages [40] -->
ind=0; 224

<!-- b001000 | prose | pages [40] -->
added=0; 225

<!-- b001001 | prose | pages [40] -->
for i=1:population, 226

<!-- b001002 | prose | pages [40] -->
if sqrt(((rep(it,1)-notcovered(i,2*iteration-1))ˆ2)+((rep(it,2)-notcove 227

<!-- b001003 | prose | pages [40] -->
ind = ind +1; 228

<!-- b001004 | prose | pages [40] -->
notcovered(ind,2*iteration+1)=notcovered(i,2*iteration-1); 229

<!-- b001005 | prose | pages [40] -->
notcovered(ind,2*iteration+2)=notcovered(i,2*iteration); 230

<!-- b001006 | prose | pages [40] -->
else 231

<!-- b001007 | prose | pages [40] -->
added=added+1; 232

<!-- b001008 | prose | pages [40] -->
end 233

<!-- b001009 | prose | pages [40] -->
end 234

<!-- b001010 | prose | pages [40] -->
end 235

<!-- b001011 | prose | pages [40] -->
236

<!-- b001012 | prose | pages [40] -->
cover = cover + added; 237

<!-- b001013 | prose | pages [40] -->
population = population - added; 238

<!-- b001014 | prose | pages [40] -->
connected = min(cover,openchannels); 239

<!-- b001015 | prose | pages [40] -->
deficit = max(cover - connected,0); 240

<!-- b001016 | prose | pages [40] -->
241

<!-- b001017 | prose | pages [40] -->
disp('the open repeater will be placed at'),disp('x='),disp(rep(it,1)),disp('y= 242

<!-- b001018 | prose | pages [40] -->
disp('added'),disp(added); 243

<!-- b001019 | prose | pages [40] -->
disp('cover'),disp(cover); 244

<!-- b001020 | prose | pages [40] -->
disp('open channels'),disp(openchannels); 245

<!-- b001021 | prose | pages [40] -->
disp('people connected:'),disp(connected); 246

<!-- b001022 | prose | pages [40] -->
disp('deficit'),disp(deficit); 247

<!-- b001023 | prose | pages [40] -->
disp('population'),disp(population); 248

<!-- b001024 | prose | pages [40] -->
end 249

<!-- b001025 | prose | pages [40] -->
end 250

<!-- b001026 | prose | pages [40] -->
251

<!-- b001027 | prose | pages [40] -->
disp('number of open repeaters'),disp(it); 252

<!-- b001028 | prose | pages [40] -->
disp('number of PL repeaters'),disp(plit); 253

<!-- b001029 | prose | pages [40] -->
254

<!-- b001030 | prose | pages [40] -->
xplot=zeros(it,1); 255

<!-- b001031 | prose | pages [40] -->
yplot=zeros(it,1); 256

<!-- b001032 | prose | pages [40] -->
for i=1:it 257

<!-- b001033 | prose | pages [40] -->
xplot(i,1)=rep(i,1); 258

<!-- b001034 | prose | pages [40] -->
yplot(i,1)=rep(i,2); 259

<!-- b001035 | prose | pages [40] -->
end 260

<!-- b001036 | prose | pages [40] -->
261

<!-- b001037 | prose | pages [40] -->
xplotpl=zeros(plit,1); 262

<!-- b001038 | prose | pages [40] -->
yplotpl=zeros(plit,1); 263

<!-- b001039 | prose | pages [40] -->
for i=1:plit 264

<!-- b001040 | furniture | pages [41] -->
Control Number: 11759

<!-- b001041 | furniture | pages [41] -->
Page 41 of 51

<!-- b001042 | prose | pages [41] -->
xplotpl(i,1)=reppl(i,1); 265

<!-- b001043 | prose | pages [41] -->
yplotpl(i,1)=reppl(i,2); 266

<!-- b001044 | prose | pages [41] -->
end 267

<!-- b001045 | prose | pages [41] -->
268

<!-- b001046 | prose | pages [41] -->
%} 269

<!-- b001047 | prose | pages [41] -->
270

<!-- b001048 | prose | pages [41] -->
plot(xcor,ycor,'s','MarkerSize',4,'MarkerEdgeColor',[1 1 1]); 271

<!-- b001049 | prose | pages [41] -->
xlabel('Miles'); 272

<!-- b001050 | prose | pages [41] -->
ylabel('Miles'); 273

<!-- b001051 | prose | pages [41] -->
title('Snaking Method Repeater Placement'); 274

<!-- b001052 | prose | pages [41] -->
hold on 275

<!-- b001053 | prose | pages [41] -->
276

<!-- b001054 | prose | pages [41] -->
plot(xplot,yplot,'o','MarkerFaceColor','r','MarkerEdgeColor','r','MarkerSize',10,'LineWidth 277

<!-- b001055 | prose | pages [41] -->
hold on 278

<!-- b001056 | prose | pages [41] -->
279

<!-- b001057 | prose | pages [41] -->
280

<!-- b001058 | prose | pages [41] -->
plot(xplotpl,yplotpl,'o','MarkerFaceColor','g','MarkerEdgeColor','g','MarkerSize',10,'LineW 281

<!-- b001059 | prose | pages [41] -->
hold on 282

<!-- b001060 | prose | pages [41] -->
283

<!-- b001061 | prose | pages [41] -->
plot(clusters(:,1),clusters(:,2),'v',... 284

<!-- b001062 | prose | pages [41] -->
'MarkerSize',10,'LineWidth',2,'MarkerEdgeColor','k'); 285

<!-- b001063 | prose | pages [41] -->
hold on 286

<!-- b001064 | prose | pages [41] -->
287

<!-- b001065 | prose | pages [41] -->
288

<!-- b001066 | prose | pages [41] -->
289

<!-- b001067 | prose | pages [41] -->
290

<!-- b001068 | prose | pages [41] -->
291

<!-- b001069 | prose | pages [41] -->
for i=1:it, 292

<!-- b001070 | prose | pages [41] -->
h=rep(i,1); k=rep(i,2); r=15; N=256; 293

<!-- b001071 | prose | pages [41] -->
t=(0:N)*2*pi/N; 294

<!-- b001072 | prose | pages [41] -->
plot(r*cos(t)+h,r*sin(t)+k,'Color','r','LineStyle','--'); 295

<!-- b001073 | prose | pages [41] -->
hold on 296

<!-- b001074 | prose | pages [41] -->
end 297

<!-- b001075 | prose | pages [41] -->
298

<!-- b001076 | prose | pages [41] -->
299

<!-- b001077 | prose | pages [41] -->
for i=1:it, 300

<!-- b001078 | prose | pages [41] -->
h=rep(i,1); k=rep(i,2); r=10; N=256; 301

<!-- b001079 | prose | pages [41] -->
t=(0:N)*2*pi/N; 302

<!-- b001080 | prose | pages [41] -->
plot(r*cos(t)+h,r*sin(t)+k,'Color','c','LineStyle',':'); 303

<!-- b001081 | prose | pages [41] -->
hold on 304

<!-- b001082 | prose | pages [41] -->
end 305

<!-- b001083 | prose | pages [41] -->
306

<!-- b001084 | prose | pages [41] -->
for i=1:plit, 307

<!-- b001085 | prose | pages [41] -->
h=reppl(i,1); k=reppl(i,2); r=15; N=256; 308

<!-- b001086 | prose | pages [41] -->
t=(0:N)*2*pi/N; 309

<!-- b001087 | prose | pages [41] -->
plot(r*cos(t)+h,r*sin(t)+k,'Color','g','LineStyle','-'); 310

<!-- b001088 | prose | pages [41] -->
hold on 311

<!-- b001089 | prose | pages [41] -->
end 312

<!-- b001090 | prose | pages [41] -->
313

<!-- b001091 | prose | pages [41] -->
314

<!-- b001092 | prose | pages [41] -->
axis([-40 40 -40 40]); 315

<!-- b001093 | prose | pages [41] -->
axis('square') 316

<!-- b001094 | prose | pages [41] -->
317

<!-- b001095 | prose | pages [41] -->
318

<!-- b001096 | furniture | pages [42] -->
Control Number: 11759

<!-- b001097 | furniture | pages [42] -->
Page 42 of 51

<!-- b001098 | prose | pages [42] -->
hold off 319

<!-- b001099 | heading | pages [42] -->
Branching Model:

<!-- b001100 | prose | pages [42] -->
load 'C:\Users\*****\Desktop\MCM 2011\newtestdata2.txt'; 1

<!-- b001101 | prose | pages [42] -->
newx = newtestdata2(:,2); %x cor of data 2

<!-- b001102 | prose | pages [42] -->
newy = newtestdata2(:,3); %y cor of data 3

<!-- b001103 | prose | pages [42] -->
notcovered = horzcat(newx,newy); 4

<!-- b001104 | prose | pages [42] -->
surfsens=2;

<!-- b001105 | prose | pages [42] -->
%distance from point to include in surfscr 5

<!-- b001106 | prose | pages [42] -->
sepdist = 10;

<!-- b001107 | prose | pages [42] -->
%seperation distance of repeaters 6

<!-- b001108 | prose | pages [42] -->
scr=zeros(length(newx),1); %how many points are within surfsens 7

<!-- b001109 | prose | pages [42] -->
rep=zeros(40,2);

<!-- b001110 | prose | pages [42] -->
%repeater locations 8

<!-- b001111 | prose | pages [42] -->
numclus=5;

<!-- b001112 | prose | pages [42] -->
%number of clusters 9

<!-- b001113 | prose | pages [42] -->
clusscr=zeros(numclus,3); %how many points are within sepdist of cluster point 10

<!-- b001114 | prose | pages [42] -->
iteration=0; 11

<!-- b001115 | prose | pages [42] -->
clf; 12

<!-- b001116 | prose | pages [42] -->
numuncov=length(newx); 13

<!-- b001117 | prose | pages [42] -->
it=0; 14

<!-- b001118 | prose | pages [42] -->
connected = 0; 15

<!-- b001119 | prose | pages [42] -->
newrepang = 0; 16

<!-- b001120 | prose | pages [42] -->
numlongdist=10; 17

<!-- b001121 | prose | pages [42] -->
actlongdist=5; 18

<!-- b001122 | prose | pages [42] -->
plsepdist=15; 19

<!-- b001123 | prose | pages [42] -->
numberoflongdistancelines=3; 20

<!-- b001124 | prose | pages [42] -->
∆f=.025; 21

<!-- b001125 | prose | pages [42] -->
perline=3/∆f; 22

<!-- b001126 | prose | pages [42] -->
openchannels=perline; 23

<!-- b001127 | prose | pages [42] -->
24

<!-- b001128 | prose | pages [42] -->
for i=1:length(newx), 25

<!-- b001129 | prose | pages [42] -->
for j=1:length(newx) 26

<!-- b001130 | prose | pages [42] -->
if sqrt((newx(i)-newx(j))ˆ2+(newy(i)-newy(j))ˆ2)≤surfsens 27

<!-- b001131 | prose | pages [42] -->
scr(i)=scr(i)+1; 28

<!-- b001132 | prose | pages [42] -->
end 29

<!-- b001133 | prose | pages [42] -->
end 30

<!-- b001134 | prose | pages [42] -->
end 31

<!-- b001135 | prose | pages [42] -->
32

<!-- b001136 | prose | pages [42] -->
concat = horzcat(newx,newy,scr); %% (xcor,ycor,zcor) 33

<!-- b001137 | prose | pages [42] -->
34

<!-- b001138 | prose | pages [42] -->
[¬,clusters]=kmeans(concat,numclus); 35

<!-- b001139 | prose | pages [42] -->
36

<!-- b001140 | prose | pages [42] -->
disp('initial uncovered'),disp(numuncov); 37

<!-- b001141 | prose | pages [42] -->
38

<!-- b001142 | prose | pages [42] -->
39

<!-- b001143 | prose | pages [42] -->
%{ 40

<!-- b001144 | prose | pages [42] -->
%Plot Users and clusters 41

<!-- b001145 | prose | pages [42] -->
plot(concat(:,1),concat(:,2),'.'); 42

<!-- b001146 | prose | pages [42] -->
hold on 43

<!-- b001147 | prose | pages [42] -->
plot(clusters(:,1),clusters(:,2),'kx',... 44

<!-- b001148 | prose | pages [42] -->
'MarkerSize',20,'LineWidth',2); 45

<!-- b001149 | prose | pages [42] -->
hold on 46

<!-- b001150 | prose | pages [42] -->
plot(clusters(:,1),clusters(:,2),'ko',... 47

<!-- b001151 | prose | pages [42] -->
'MarkerSize',20,'LineWidth',2); 48

<!-- b001152 | furniture | pages [43] -->
Control Number: 11759

<!-- b001153 | furniture | pages [43] -->
Page 43 of 51

<!-- b001154 | prose | pages [43] -->
hold off 49

<!-- b001155 | prose | pages [43] -->
%} 50

<!-- b001156 | prose | pages [43] -->
51

<!-- b001157 | prose | pages [43] -->
52

<!-- b001158 | prose | pages [43] -->
%Set first repeater locations 53

<!-- b001159 | prose | pages [43] -->
for i=1:numclus, 54

<!-- b001160 | prose | pages [43] -->
reptemp(i,1)=clusters(i,1); 55

<!-- b001161 | prose | pages [43] -->
reptemp(i,2)=clusters(i,2); 56

<!-- b001162 | prose | pages [43] -->
end 57

<!-- b001163 | prose | pages [43] -->
58

<!-- b001164 | prose | pages [43] -->
%Calculate score of each cluster and order by score 59

<!-- b001165 | prose | pages [43] -->
for i=1:numclus, 60

<!-- b001166 | prose | pages [43] -->
for j=1:length(newx), 61

<!-- b001167 | prose | pages [43] -->
if sqrt((reptemp(i,1)-newx(j))ˆ2+(reptemp(i,2)-newy(j))ˆ2)≤sepdist 62

<!-- b001168 | prose | pages [43] -->
clusscr(i,1)=reptemp(i,1); 63

<!-- b001169 | prose | pages [43] -->
clusscr(i,2)=reptemp(i,2); 64

<!-- b001170 | prose | pages [43] -->
clusscr(i,3)=clusscr(i,3)+1; 65

<!-- b001171 | prose | pages [43] -->
end 66

<!-- b001172 | prose | pages [43] -->
end 67

<!-- b001173 | prose | pages [43] -->
end 68

<!-- b001174 | prose | pages [43] -->
69

<!-- b001175 | prose | pages [43] -->
srtclus = sortrows(clusscr,-3); %sorted clusters 70

<!-- b001176 | prose | pages [43] -->
71

<!-- b001177 | prose | pages [43] -->
%Set first repeater locations 72

<!-- b001178 | prose | pages [43] -->
rep(1,1)=srtclus(1,1); 73

<!-- b001179 | prose | pages [43] -->
rep(1,2)=srtclus(1,2); 74

<!-- b001180 | prose | pages [43] -->
75

<!-- b001181 | prose | pages [43] -->
added=0; 76

<!-- b001182 | prose | pages [43] -->
i=0; 77

<!-- b001183 | prose | pages [43] -->
78

<!-- b001184 | prose | pages [43] -->
%Calculate added and remove covered entries 79

<!-- b001185 | prose | pages [43] -->
for j=1:numuncov, 80

<!-- b001186 | prose | pages [43] -->
if sqrt((rep(1,1)-notcovered(j,1))ˆ2+(rep(1,2)-notcovered(j,2))ˆ2)≤sepdist 81

<!-- b001187 | prose | pages [43] -->
added=added+1; 82

<!-- b001188 | prose | pages [43] -->
else 83

<!-- b001189 | prose | pages [43] -->
i=i+1; 84

<!-- b001190 | prose | pages [43] -->
notcovered(i,3)=notcovered(j,1); 85

<!-- b001191 | prose | pages [43] -->
notcovered(i,4)=notcovered(j,2); 86

<!-- b001192 | prose | pages [43] -->
end 87

<!-- b001193 | prose | pages [43] -->
end 88

<!-- b001194 | prose | pages [43] -->
89

<!-- b001195 | prose | pages [43] -->
repcoverage(1)=added; 90

<!-- b001196 | prose | pages [43] -->
numuncov=numuncov-added; 91

<!-- b001197 | prose | pages [43] -->
connected = connected+added; 92

<!-- b001198 | prose | pages [43] -->
93

<!-- b001199 | prose | pages [43] -->
targetloc(1)=srtclus(2,1); 94

<!-- b001200 | prose | pages [43] -->
targetloc(2)=srtclus(2,2); 95

<!-- b001201 | prose | pages [43] -->
96

<!-- b001202 | prose | pages [43] -->
newrepdist = sqrt((rep(1,1)-targetloc(1))ˆ2+(rep(1,2)-targetloc(2))ˆ2); %Distance from curr 97

<!-- b001203 | prose | pages [43] -->
98

<!-- b001204 | prose | pages [43] -->
99

<!-- b001205 | prose | pages [43] -->
100

<!-- b001206 | prose | pages [43] -->
if ((rep(1,1)≥targetloc(1))&&(rep(1,2)≤targetloc(2))) 101

<!-- b001207 | prose | pages [43] -->
newrepang= acos((targetloc(1)-rep(1,1))/newrepdist); 102

<!-- b001208 | furniture | pages [44] -->
Control Number: 11759

<!-- b001209 | furniture | pages [44] -->
Page 44 of 51

<!-- b001210 | prose | pages [44] -->
elseif ((rep(1,1)≥targetloc(1))&&(rep(1,2)≥targetloc(2))) 103

<!-- b001211 | prose | pages [44] -->
newrepang=2*pi-acos((targetloc(1)-rep(1,1))/newrepdist); 104

<!-- b001212 | prose | pages [44] -->
elseif ((rep(1,1)≤targetloc(1))&&(rep(1,2)≥targetloc(2))) 105

<!-- b001213 | prose | pages [44] -->
newrepang=2*pi-acos((targetloc(1)-rep(1,1))/newrepdist); 106

<!-- b001214 | prose | pages [44] -->
else 107

<!-- b001215 | prose | pages [44] -->
newrepang=acos((targetloc(1)-rep(1,1))/newrepdist); 108

<!-- b001216 | prose | pages [44] -->
end 109

<!-- b001217 | prose | pages [44] -->
110

<!-- b001218 | prose | pages [44] -->
repno=1; 111

<!-- b001219 | prose | pages [44] -->
112

<!-- b001220 | prose | pages [44] -->
iteration=0; 113

<!-- b001221 | prose | pages [44] -->
lastplaced=1; 114

<!-- b001222 | prose | pages [44] -->
115

<!-- b001223 | prose | pages [44] -->
%add repeater to make connection 116

<!-- b001224 | prose | pages [44] -->
while connected<1000, 117

<!-- b001225 | prose | pages [44] -->
118

<!-- b001226 | prose | pages [44] -->
iteration=iteration+1; 119

<!-- b001227 | prose | pages [44] -->
while newrepdist>sepdist, 120

<!-- b001228 | prose | pages [44] -->
it=it+1; 121

<!-- b001229 | prose | pages [44] -->
repno = repno+1; 122

<!-- b001230 | prose | pages [44] -->
rep(repno,1)=rep(lastplaced,1)+sepdist*cos(newrepang); 123

<!-- b001231 | prose | pages [44] -->
rep(repno,2)=rep(lastplaced,2)+sepdist*sin(newrepang); 124

<!-- b001232 | prose | pages [44] -->
lastplaced=repno; %set the last placed to the current repeater 125

<!-- b001233 | prose | pages [44] -->
newrepdist=sqrt((targetloc(1)-rep(repno,1))ˆ2+(targetloc(2)-rep(repno,2))ˆ2); 126

<!-- b001234 | prose | pages [44] -->
127

<!-- b001235 | prose | pages [44] -->
%Count covered and remove from dataset 128

<!-- b001236 | prose | pages [44] -->
added=0; 129

<!-- b001237 | prose | pages [44] -->
i=0; 130

<!-- b001238 | prose | pages [44] -->
for j=1:numuncov, 131

<!-- b001239 | prose | pages [44] -->
if sqrt((rep(repno,1)-notcovered(j,2*it+1))ˆ2+(rep(repno,2)-notcovered(j,2*it+2 132

<!-- b001240 | prose | pages [44] -->
added=added+1; 133

<!-- b001241 | prose | pages [44] -->
else 134

<!-- b001242 | prose | pages [44] -->
i=i+1; 135

<!-- b001243 | prose | pages [44] -->
notcovered(i,2*it+3)=notcovered(j,2*it+1); 136

<!-- b001244 | prose | pages [44] -->
notcovered(i,2*it+4)=notcovered(j,2*it+2); 137

<!-- b001245 | prose | pages [44] -->
end 138

<!-- b001246 | prose | pages [44] -->
end 139

<!-- b001247 | prose | pages [44] -->
140

<!-- b001248 | prose | pages [44] -->
coveragestat=0; 141

<!-- b001249 | prose | pages [44] -->
for j=1:length(newx), 142

<!-- b001250 | prose | pages [44] -->
if sqrt((rep(repno,1)-newx(j))ˆ2+(rep(repno,2)-newy(j))ˆ2)≤sepdist 143

<!-- b001251 | prose | pages [44] -->
coveragestat=coveragestat+1; 144

<!-- b001252 | prose | pages [44] -->
end 145

<!-- b001253 | prose | pages [44] -->
end 146

<!-- b001254 | prose | pages [44] -->
repcoverage(repno)=coveragestat; 147

<!-- b001255 | prose | pages [44] -->
numuncov=numuncov-added; 148

<!-- b001256 | prose | pages [44] -->
connected = connected + added; 149

<!-- b001257 | prose | pages [44] -->
disp('added'),disp(added); 150

<!-- b001258 | prose | pages [44] -->
disp('adding another'); 151

<!-- b001259 | prose | pages [44] -->
end 152

<!-- b001260 | prose | pages [44] -->
disp('iteration'),disp(iteration); 153

<!-- b001261 | prose | pages [44] -->
154

<!-- b001262 | prose | pages [44] -->
155

<!-- b001263 | prose | pages [44] -->
156

<!-- b001264 | furniture | pages [45] -->
Control Number: 11759

<!-- b001265 | furniture | pages [45] -->
Page 45 of 51

<!-- b001266 | prose | pages [45] -->
157

<!-- b001267 | prose | pages [45] -->
%New targetloc 158

<!-- b001268 | prose | pages [45] -->
concat = zeros(numuncov,2); 159

<!-- b001269 | prose | pages [45] -->
for i=1:numuncov; 160

<!-- b001270 | prose | pages [45] -->
concat(i,1) = notcovered(i,2*it+3); 161

<!-- b001271 | prose | pages [45] -->
concat(i,2) = notcovered(i,2*it+4); 162

<!-- b001272 | prose | pages [45] -->
end 163

<!-- b001273 | prose | pages [45] -->
164

<!-- b001274 | prose | pages [45] -->
[clusid,clusters]=kmeans(concat,numclus); 165

<!-- b001275 | prose | pages [45] -->
166

<!-- b001276 | prose | pages [45] -->
clusscr=zeros(numclus,3); 167

<!-- b001277 | prose | pages [45] -->
168

<!-- b001278 | prose | pages [45] -->
169

<!-- b001279 | prose | pages [45] -->
170

<!-- b001280 | prose | pages [45] -->
%Set temp repeater locations 171

<!-- b001281 | prose | pages [45] -->
for i=1:numclus, 172

<!-- b001282 | prose | pages [45] -->
reptemp(i,1)=clusters(i,1); 173

<!-- b001283 | prose | pages [45] -->
reptemp(i,2)=clusters(i,2); 174

<!-- b001284 | prose | pages [45] -->
end 175

<!-- b001285 | prose | pages [45] -->
%Calculate score of each cluster and order by score 176

<!-- b001286 | prose | pages [45] -->
for i=1:numclus, 177

<!-- b001287 | prose | pages [45] -->
clusscr(i,1)=reptemp(i,1); 178

<!-- b001288 | prose | pages [45] -->
clusscr(i,2)=reptemp(i,2); 179

<!-- b001289 | prose | pages [45] -->
for j=1:numuncov, 180

<!-- b001290 | prose | pages [45] -->
if sqrt((reptemp(i,1)-concat(j,1))ˆ2+(reptemp(i,2)-concat(j,2))ˆ2)≤sepdist 181

<!-- b001291 | prose | pages [45] -->
clusscr(i,3)=clusscr(i,3)+1; 182

<!-- b001292 | prose | pages [45] -->
end 183

<!-- b001293 | prose | pages [45] -->
end 184

<!-- b001294 | prose | pages [45] -->
end 185

<!-- b001295 | prose | pages [45] -->
186

<!-- b001296 | prose | pages [45] -->
srtclus = sortrows(clusscr,-3); %sorted clusters 187

<!-- b001297 | prose | pages [45] -->
188

<!-- b001298 | prose | pages [45] -->
%Set new target location 189

<!-- b001299 | prose | pages [45] -->
targetloc(1)=srtclus(1,1); 190

<!-- b001300 | prose | pages [45] -->
targetloc(2)=srtclus(1,2); 191

<!-- b001301 | prose | pages [45] -->
repdist=zeros(repno,1); 192

<!-- b001302 | prose | pages [45] -->
for i=1:repno, 193

<!-- b001303 | prose | pages [45] -->
repdist(i,1)=sqrt((targetloc(1)-rep(i,1))ˆ2+(targetloc(2)-rep(i,2))ˆ2); 194

<!-- b001304 | prose | pages [45] -->
end 195

<!-- b001305 | prose | pages [45] -->
196

<!-- b001306 | prose | pages [45] -->
[C,I]=min(repdist); 197

<!-- b001307 | prose | pages [45] -->
lastplaced=I(1); 198

<!-- b001308 | prose | pages [45] -->
newrepdist = sqrt((rep(lastplaced,1)-targetloc(1))ˆ2+(rep(lastplaced,2)-targetloc(2))ˆ2 199

<!-- b001309 | prose | pages [45] -->
200

<!-- b001310 | prose | pages [45] -->
201

<!-- b001311 | prose | pages [45] -->
if ((rep(lastplaced,1)≥targetloc(1))&&(rep(lastplaced,2)≤targetloc(2))) 202

<!-- b001312 | prose | pages [45] -->
newrepang= acos((targetloc(1)-rep(lastplaced,1))/newrepdist); 203

<!-- b001313 | prose | pages [45] -->
elseif ((rep(lastplaced,1)≥targetloc(1))&&(rep(lastplaced,2)≥targetloc(2))) 204

<!-- b001314 | prose | pages [45] -->
newrepang=2*pi-acos((targetloc(1)-rep(lastplaced,1))/newrepdist); 205

<!-- b001315 | prose | pages [45] -->
elseif ((rep(lastplaced,1)≤targetloc(1))&&(rep(lastplaced,2)≥targetloc(2))) 206

<!-- b001316 | prose | pages [45] -->
newrepang=2*pi-acos((targetloc(1)-rep(lastplaced,1))/newrepdist); 207

<!-- b001317 | prose | pages [45] -->
else 208

<!-- b001318 | prose | pages [45] -->
newrepang=acos((targetloc(1)-rep(lastplaced,1))/newrepdist); 209

<!-- b001319 | prose | pages [45] -->
end 210

<!-- b001320 | furniture | pages [46] -->
Control Number: 11759

<!-- b001321 | furniture | pages [46] -->
Page 46 of 51

<!-- b001322 | prose | pages [46] -->
211

<!-- b001323 | prose | pages [46] -->
disp('connected'),disp(connected); 212

<!-- b001324 | prose | pages [46] -->
213

<!-- b001325 | prose | pages [46] -->
214

<!-- b001326 | prose | pages [46] -->
end 215

<!-- b001327 | prose | pages [46] -->
216

<!-- b001328 | prose | pages [46] -->
disp('number uncovered'),disp(numuncov); 217

<!-- b001329 | prose | pages [46] -->
218

<!-- b001330 | prose | pages [46] -->
219

<!-- b001331 | prose | pages [46] -->
%%Plot Data 220

<!-- b001332 | prose | pages [46] -->
xplot=zeros(repno,1); 221

<!-- b001333 | prose | pages [46] -->
yplot=zeros(repno,1); 222

<!-- b001334 | prose | pages [46] -->
for i=1:repno, 223

<!-- b001335 | prose | pages [46] -->
xplot(i)=rep(i,1); 224

<!-- b001336 | prose | pages [46] -->
yplot(i)=rep(i,2); 225

<!-- b001337 | prose | pages [46] -->
end 226

<!-- b001338 | prose | pages [46] -->
227

<!-- b001339 | prose | pages [46] -->
228

<!-- b001340 | prose | pages [46] -->
229

<!-- b001341 | prose | pages [46] -->
%% 230

<!-- b001342 | prose | pages [46] -->
concat = zeros(length(newx),2); 231

<!-- b001343 | prose | pages [46] -->
for i=1:length(newx); 232

<!-- b001344 | prose | pages [46] -->
concat(i,1) = newx(i); 233

<!-- b001345 | prose | pages [46] -->
concat(i,2) = newy(i); 234

<!-- b001346 | prose | pages [46] -->
end 235

<!-- b001347 | prose | pages [46] -->
236

<!-- b001348 | prose | pages [46] -->
concat=horzcat(newx,newy); 237

<!-- b001349 | prose | pages [46] -->
[clusid,clusters]=kmeans(concat,numlongdist); 238

<!-- b001350 | prose | pages [46] -->
239

<!-- b001351 | prose | pages [46] -->
cluslongscr=zeros(numclus,2); 240

<!-- b001352 | prose | pages [46] -->
241

<!-- b001353 | prose | pages [46] -->
for i=1:length(clusters), 242

<!-- b001354 | prose | pages [46] -->
for j=1:length(newx) 243

<!-- b001355 | prose | pages [46] -->
if sqrt((clusters(i,1)-newx(j))ˆ2+(clusters(i,2)-newy(j))ˆ2)≤sepdist; 244

<!-- b001356 | prose | pages [46] -->
cluslongscr(i,1)=i; 245

<!-- b001357 | prose | pages [46] -->
cluslongscr(i,2)=cluslongscr(i,2)+1; 246

<!-- b001358 | prose | pages [46] -->
end 247

<!-- b001359 | prose | pages [46] -->
end 248

<!-- b001360 | prose | pages [46] -->
end 249

<!-- b001361 | prose | pages [46] -->
250

<!-- b001362 | prose | pages [46] -->
cluslongsrt=sortrows(cluslongscr,-2); 251

<!-- b001363 | prose | pages [46] -->
plplots=zeros(actlongdist,2); 252

<!-- b001364 | prose | pages [46] -->
253

<!-- b001365 | prose | pages [46] -->
for i=1:actlongdist, 254

<!-- b001366 | prose | pages [46] -->
plplots(i,1)=clusters(cluslongsrt(i),1); 255

<!-- b001367 | prose | pages [46] -->
plplots(i,2)=clusters(cluslongsrt(i),2); 256

<!-- b001368 | prose | pages [46] -->
end 257

<!-- b001369 | prose | pages [46] -->
258

<!-- b001370 | prose | pages [46] -->
plrep=zeros(100,2); 259

<!-- b001371 | prose | pages [46] -->
260

<!-- b001372 | prose | pages [46] -->
longdistmat=zeros(actlongdist,2); 261

<!-- b001373 | prose | pages [46] -->
currentlong=1; 262

<!-- b001374 | prose | pages [46] -->
plrep(1,1)=plplots(1,1); 263

<!-- b001375 | prose | pages [46] -->
plrep(1,2)=plplots(1,2); 264

<!-- b001376 | furniture | pages [47] -->
Control Number: 11759

<!-- b001377 | furniture | pages [47] -->
Page 47 of 51

<!-- b001378 | prose | pages [47] -->
plrep(1,3)=1; 265

<!-- b001379 | prose | pages [47] -->
266

<!-- b001380 | prose | pages [47] -->
for j=1:actlongdist, 267

<!-- b001381 | prose | pages [47] -->
longdistmat(j,1)=j; 268

<!-- b001382 | prose | pages [47] -->
longdistmat(j,2)=sqrt((plrep(1,1)-plplots(j,1))ˆ2+(plrep(1,2)-plplots(j,2))ˆ2); 269

<!-- b001383 | prose | pages [47] -->
end 270

<!-- b001384 | prose | pages [47] -->
271

<!-- b001385 | prose | pages [47] -->
272

<!-- b001386 | prose | pages [47] -->
ldsort=sortrows(longdistmat,2); 273

<!-- b001387 | prose | pages [47] -->
tar(1,1)=plplots(ldsort(2,1),1); 274

<!-- b001388 | prose | pages [47] -->
tar(1,2)=plplots(ldsort(2,1),2); 275

<!-- b001389 | prose | pages [47] -->
prevtarget=ldsort(2,1); 276

<!-- b001390 | prose | pages [47] -->
d2tar=longdistmat(ldsort(2,1),2); 277

<!-- b001391 | prose | pages [47] -->
278

<!-- b001392 | prose | pages [47] -->
if ((plrep(1,1)≥tar(1,1))&&(plrep(1,2)≤tar(1,2))) 279

<!-- b001393 | prose | pages [47] -->
angletotarget= acos((tar(1,1)-plrep(1,1))/d2tar); 280

<!-- b001394 | prose | pages [47] -->
elseif ((plrep(1,1)≥tar(1,1))&&(plrep(1,2)≥tar(1,2))) 281

<!-- b001395 | prose | pages [47] -->
angletotarget=2*pi-acos((tar(1,1)-plrep(1,1))/d2tar); 282

<!-- b001396 | prose | pages [47] -->
elseif ((plrep(1,1)≤tar(1,1))&&(plrep(1,2)≥tar(1,2))) 283

<!-- b001397 | prose | pages [47] -->
angletotarget=2*pi-acos((tar(1,1)-plrep(1,1))/d2tar); 284

<!-- b001398 | prose | pages [47] -->
else 285

<!-- b001399 | prose | pages [47] -->
angletotarget=acos((tar(1,1)-plrep(1,1))/d2tar); 286

<!-- b001400 | prose | pages [47] -->
end 287

<!-- b001401 | prose | pages [47] -->
288

<!-- b001402 | prose | pages [47] -->
while d2tar>plsepdist, 289

<!-- b001403 | prose | pages [47] -->
currentlong=currentlong+1; 290

<!-- b001404 | prose | pages [47] -->
plrep(currentlong,1)=plrep(currentlong-1,1)+plsepdist*cos(angletotarget); 291

<!-- b001405 | prose | pages [47] -->
plrep(currentlong,2)=plrep(currentlong-1,2)+plsepdist*sin(angletotarget); 292

<!-- b001406 | prose | pages [47] -->
plrep(currentlong,3)=1; 293

<!-- b001407 | prose | pages [47] -->
d2tar=sqrt((plrep(currentlong,1)-tar(1,1))ˆ2+(plrep(currentlong,2)-tar(1,2))ˆ2); 294

<!-- b001408 | prose | pages [47] -->
end 295

<!-- b001409 | prose | pages [47] -->
296

<!-- b001410 | prose | pages [47] -->
for i=1:actlongdist, 297

<!-- b001411 | prose | pages [47] -->
newzones(i,1)=plplots(i,1); 298

<!-- b001412 | prose | pages [47] -->
newzones(i,2)=plplots(i,2); 299

<!-- b001413 | prose | pages [47] -->
end 300

<!-- b001414 | prose | pages [47] -->
newzones(prevtarget,:)=[]; 301

<!-- b001415 | prose | pages [47] -->
newzones(1,:)=[]; 302

<!-- b001416 | prose | pages [47] -->
303

<!-- b001417 | prose | pages [47] -->
counter=1; 304

<!-- b001418 | prose | pages [47] -->
while counter<actlongdist-1; 305

<!-- b001419 | prose | pages [47] -->
counter=counter+1; 306

<!-- b001420 | prose | pages [47] -->
307

<!-- b001421 | prose | pages [47] -->
longdistmat=zeros(actlongdist-counter,2); 308

<!-- b001422 | prose | pages [47] -->
for i=1:actlongdist-counter, 309

<!-- b001423 | prose | pages [47] -->
longdistmat(i,1)=i; 310

<!-- b001424 | prose | pages [47] -->
longdistmat(i,2)=sqrt((plrep(currentlong,1)-newzones(i,1))ˆ2+(plrep(currentlong,2)- 311

<!-- b001425 | prose | pages [47] -->
end 312

<!-- b001426 | prose | pages [47] -->
313

<!-- b001427 | prose | pages [47] -->
ldsort=sortrows(longdistmat,2); 314

<!-- b001428 | prose | pages [47] -->
315

<!-- b001429 | prose | pages [47] -->
prevtarget=ldsort(1,1); 316

<!-- b001430 | prose | pages [47] -->
tar(1,1)=newzones(prevtarget,1); 317

<!-- b001431 | prose | pages [47] -->
tar(1,2)=newzones(prevtarget,2); 318

<!-- b001432 | furniture | pages [48] -->
Control Number: 11759

<!-- b001433 | furniture | pages [48] -->
Page 48 of 51

<!-- b001434 | prose | pages [48] -->
319

<!-- b001435 | prose | pages [48] -->
d2tar=longdistmat(prevtarget,2); 320

<!-- b001436 | prose | pages [48] -->
321

<!-- b001437 | prose | pages [48] -->
322

<!-- b001438 | prose | pages [48] -->
if ((plrep(currentlong,1)≥tar(1,1))&&(plrep(currentlong,2)≤tar(1,2))) 323

<!-- b001439 | prose | pages [48] -->
angletotarget= acos((tar(1,1)-plrep(currentlong,1))/d2tar); 324

<!-- b001440 | prose | pages [48] -->
elseif ((plrep(currentlong,1)≥tar(1,1))&&(plrep(currentlong,2)≥tar(1,2))) 325

<!-- b001441 | prose | pages [48] -->
angletotarget=2*pi-acos((tar(1,1)-plrep(currentlong,1))/d2tar); 326

<!-- b001442 | prose | pages [48] -->
elseif ((plrep(currentlong,1)≤tar(1,1))&&(plrep(currentlong,2)≥tar(1,2))) 327

<!-- b001443 | prose | pages [48] -->
angletotarget=2*pi-acos((tar(1,1)-plrep(currentlong,1))/d2tar); 328

<!-- b001444 | prose | pages [48] -->
else 329

<!-- b001445 | prose | pages [48] -->
angletotarget=acos((tar(1,1)-plrep(currentlong,1))/d2tar); 330

<!-- b001446 | prose | pages [48] -->
end 331

<!-- b001447 | prose | pages [48] -->
332

<!-- b001448 | prose | pages [48] -->
while d2tar>plsepdist, 333

<!-- b001449 | prose | pages [48] -->
currentlong=currentlong+1; 334

<!-- b001450 | prose | pages [48] -->
plrep(currentlong,1)=plrep(currentlong-1,1)+plsepdist*cos(angletotarget); 335

<!-- b001451 | prose | pages [48] -->
plrep(currentlong,2)=plrep(currentlong-1,2)+plsepdist*sin(angletotarget); 336

<!-- b001452 | prose | pages [48] -->
plrep(currentlong,3)=1; 337

<!-- b001453 | prose | pages [48] -->
d2tar=sqrt((plrep(currentlong,1)-tar(1,1))ˆ2+(plrep(currentlong,2)-tar(1,2))ˆ2); 338

<!-- b001454 | prose | pages [48] -->
end 339

<!-- b001455 | prose | pages [48] -->
340

<!-- b001456 | prose | pages [48] -->
newzones(prevtarget,:)=[]; 341

<!-- b001457 | prose | pages [48] -->
342

<!-- b001458 | prose | pages [48] -->
343

<!-- b001459 | prose | pages [48] -->
end 344

<!-- b001460 | prose | pages [48] -->
345

<!-- b001461 | prose | pages [48] -->
346

<!-- b001462 | prose | pages [48] -->
noplrep=currentlong; 347

<!-- b001463 | prose | pages [48] -->
openchannels=openchannels+numberoflongdistancelines*perline; 348

<!-- b001464 | prose | pages [48] -->
deficit=max(connected-openchannels,0); 349

<!-- b001465 | prose | pages [48] -->
350

<!-- b001466 | prose | pages [48] -->
indexnum=0; 351

<!-- b001467 | prose | pages [48] -->
indexnum2=0; 352

<!-- b001468 | prose | pages [48] -->
channelnumber=numberoflongdistancelines; 353

<!-- b001469 | prose | pages [48] -->
plcolor(1:currentlong,1)=51; 354

<!-- b001470 | prose | pages [48] -->
plcolor(1:currentlong,2)=51; 355

<!-- b001471 | prose | pages [48] -->
plcolor(1:currentlong,3)=255; 356

<!-- b001472 | prose | pages [48] -->
pluncovered=horzcat(newx,newy); 357

<!-- b001473 | prose | pages [48] -->
numuncovered=length(newx); 358

<!-- b001474 | prose | pages [48] -->
while deficit>0 359

<!-- b001475 | prose | pages [48] -->
channelnumber=channelnumber+1; 360

<!-- b001476 | prose | pages [48] -->
currentlong=currentlong+1; 361

<!-- b001477 | prose | pages [48] -->
indexnum=indexnum+1; 362

<!-- b001478 | prose | pages [48] -->
if indexnum==actlongdist 363

<!-- b001479 | prose | pages [48] -->
indexnum=1; 364

<!-- b001480 | prose | pages [48] -->
concat = zeros(numuncovered,2); 365

<!-- b001481 | prose | pages [48] -->
for i=1:numuncovered; 366

<!-- b001482 | prose | pages [48] -->
concat(i,1) = pluncovered(i,1); 367

<!-- b001483 | prose | pages [48] -->
concat(i,2) = pluncovered(i,2); 368

<!-- b001484 | prose | pages [48] -->
end 369

<!-- b001485 | prose | pages [48] -->
370

<!-- b001486 | prose | pages [48] -->
[clusid,clusters]=kmeans(pluncovered,numlongdist); 371

<!-- b001487 | prose | pages [48] -->
372

<!-- b001488 | furniture | pages [49] -->
Control Number: 11759

<!-- b001489 | furniture | pages [49] -->
Page 49 of 51

<!-- b001490 | prose | pages [49] -->
cluslongscr=zeros(numlongdist,2); 373

<!-- b001491 | prose | pages [49] -->
374

<!-- b001492 | prose | pages [49] -->
for i=1:length(clusters), 375

<!-- b001493 | prose | pages [49] -->
for j=1:length(pluncovered) 376

<!-- b001494 | prose | pages [49] -->
if sqrt((clusters(i,1)-pluncovered(j,1))ˆ2+(clusters(i,2)-pluncovered(j,2)) 377

<!-- b001495 | prose | pages [49] -->
cluslongscr(i,1)=i; 378

<!-- b001496 | prose | pages [49] -->
cluslongscr(i,2)=cluslongscr(i,2)+1; 379

<!-- b001497 | prose | pages [49] -->
end 380

<!-- b001498 | prose | pages [49] -->
end 381

<!-- b001499 | prose | pages [49] -->
end 382

<!-- b001500 | prose | pages [49] -->
383

<!-- b001501 | prose | pages [49] -->
cluslongsrt=sortrows(cluslongscr,-2); 384

<!-- b001502 | prose | pages [49] -->
plplots=zeros(actlongdist,2); 385

<!-- b001503 | prose | pages [49] -->
386

<!-- b001504 | prose | pages [49] -->
for i=1:actlongdist, 387

<!-- b001505 | prose | pages [49] -->
plplots(i,1)=clusters(cluslongsrt(i),1); 388

<!-- b001506 | prose | pages [49] -->
plplots(i,2)=clusters(cluslongsrt(i),2); 389

<!-- b001507 | prose | pages [49] -->
end 390

<!-- b001508 | prose | pages [49] -->
end 391

<!-- b001509 | prose | pages [49] -->
plrep(currentlong,1)=plplots(indexnum,1); 392

<!-- b001510 | prose | pages [49] -->
plrep(currentlong,2)=plplots(indexnum,2); 393

<!-- b001511 | prose | pages [49] -->
plrep(currentlong,3)=channelnumber; 394

<!-- b001512 | prose | pages [49] -->
index1=1; 395

<!-- b001513 | prose | pages [49] -->
for i=1:numuncovered, 396

<!-- b001514 | prose | pages [49] -->
if sqrt((plrep(currentlong,1)-pluncovered(i))ˆ2+(plrep(currentlong,2)-pluncovered(i)) 397

<!-- b001515 | prose | pages [49] -->
pluncovered(index1,1)=pluncovered(i,1); 398

<!-- b001516 | prose | pages [49] -->
pluncovered(index1,2)=pluncovered(i,2); 399

<!-- b001517 | prose | pages [49] -->
index1=index1+1; 400

<!-- b001518 | prose | pages [49] -->
else 401

<!-- b001519 | prose | pages [49] -->
numuncovered=numuncovered-1; 402

<!-- b001520 | prose | pages [49] -->
end 403

<!-- b001521 | prose | pages [49] -->
end 404

<!-- b001522 | prose | pages [49] -->
plcolor(currentlong,1)=255-indexnum2*20; 405

<!-- b001523 | prose | pages [49] -->
plcolor(currentlong,2)=40+indexnum2*20; 406

<!-- b001524 | prose | pages [49] -->
plcolor(currentlong,3)=0; 407

<!-- b001525 | prose | pages [49] -->
noplrep=noplrep+1; 408

<!-- b001526 | prose | pages [49] -->
openchannels=openchannels+perline; 409

<!-- b001527 | prose | pages [49] -->
deficit=max(connected-openchannels,0); 410

<!-- b001528 | prose | pages [49] -->
indexnum2=indexnum2+1; 411

<!-- b001529 | prose | pages [49] -->
end 412

<!-- b001530 | prose | pages [49] -->
413

<!-- b001531 | prose | pages [49] -->
plrepplot=zeros(currentlong,2); 414

<!-- b001532 | prose | pages [49] -->
for i=1:currentlong, 415

<!-- b001533 | prose | pages [49] -->
plrepplot(i,1)=plrep(i,1); 416

<!-- b001534 | prose | pages [49] -->
plrepplot(i,2)=plrep(i,2); 417

<!-- b001535 | prose | pages [49] -->
end 418

<!-- b001536 | prose | pages [49] -->
419

<!-- b001537 | prose | pages [49] -->
420

<!-- b001538 | prose | pages [49] -->
%} 421

<!-- b001539 | prose | pages [49] -->
%% 422

<!-- b001540 | prose | pages [49] -->
plot(newx,newy,'s','MarkerSize',2,'MarkerEdgeColor',[1 1 1]); 423

<!-- b001541 | prose | pages [49] -->
424

<!-- b001542 | prose | pages [49] -->
hold on 425

<!-- b001543 | prose | pages [49] -->
xlabel('Miles'); 426

<!-- b001544 | furniture | pages [50] -->
Control Number: 11759

<!-- b001545 | furniture | pages [50] -->
Page 50 of 51

<!-- b001546 | prose | pages [50] -->
ylabel('Miles'); 427

<!-- b001547 | prose | pages [50] -->
title('Random User Data'); 428

<!-- b001548 | prose | pages [50] -->
hold on 429

<!-- b001549 | prose | pages [50] -->
430

<!-- b001550 | prose | pages [50] -->
plot(xplot,yplot,'.','MarkerFaceColor','none','MarkerEdgeColor',[1 0 0],'MarkerSize',20,'Li 431

<!-- b001551 | prose | pages [50] -->
hold on 432

<!-- b001552 | prose | pages [50] -->
433

<!-- b001553 | prose | pages [50] -->
%} 434

<!-- b001554 | prose | pages [50] -->
435

<!-- b001555 | prose | pages [50] -->
%{ 436

<!-- b001556 | prose | pages [50] -->
plot(plplots(:,1),plplots(:,2),'o','MarkerFaceColor','g','MarkerEdgeColor',g,'MarkerSize',1 437

<!-- b001557 | prose | pages [50] -->
%} 438

<!-- b001558 | prose | pages [50] -->
439

<!-- b001559 | prose | pages [50] -->
for i=1:noplrep, 440

<!-- b001560 | prose | pages [50] -->
plot(plrepplot(i,1),plrepplot(i,2),'.','MarkerFaceColor','g','MarkerEdgeColor','g','Mar 441

<!-- b001561 | prose | pages [50] -->
hold on 442

<!-- b001562 | prose | pages [50] -->
end 443

<!-- b001563 | prose | pages [50] -->
444

<!-- b001564 | prose | pages [50] -->
445

<!-- b001565 | prose | pages [50] -->
for i=1:repno, 446

<!-- b001566 | prose | pages [50] -->
h=rep(i,1); k=rep(i,2); r=10; N=256; 447

<!-- b001567 | prose | pages [50] -->
t=(0:N)*2*pi/N; 448

<!-- b001568 | prose | pages [50] -->
plot(r*cos(t)+h,r*sin(t)+k,'Color','r','LineStyle','--'); 449

<!-- b001569 | prose | pages [50] -->
hold on 450

<!-- b001570 | prose | pages [50] -->
end 451

<!-- b001571 | prose | pages [50] -->
452

<!-- b001572 | prose | pages [50] -->
453

<!-- b001573 | prose | pages [50] -->
454

<!-- b001574 | prose | pages [50] -->
455

<!-- b001575 | prose | pages [50] -->
for i=1:repno, 456

<!-- b001576 | prose | pages [50] -->
h=rep(i,1); k=rep(i,2); r=10; N=256; 457

<!-- b001577 | prose | pages [50] -->
t=(0:N)*2*pi/N; 458

<!-- b001578 | prose | pages [50] -->
plot(r*cos(t)+h,r*sin(t)+k,'Color',[43/255 129/255 86/255],'LineStyle',':'); 459

<!-- b001579 | prose | pages [50] -->
hold on 460

<!-- b001580 | prose | pages [50] -->
end 461

<!-- b001581 | prose | pages [50] -->
%} 462

<!-- b001582 | prose | pages [50] -->
%{ 463

<!-- b001583 | prose | pages [50] -->
for i=1:noplrep, 464

<!-- b001584 | prose | pages [50] -->
h=plrep(i,1); k=plrep(i,2); r=15; N=256; 465

<!-- b001585 | prose | pages [50] -->
t=(0:N)*2*pi/N; 466

<!-- b001586 | prose | pages [50] -->
plot(r*cos(t)+h,r*sin(t)+k,'Color',[plcolor(i,1)/255 plcolor(i,2)/255 plcolor(i,3)/255] 467

<!-- b001587 | prose | pages [50] -->
hold on 468

<!-- b001588 | prose | pages [50] -->
end 469

<!-- b001589 | prose | pages [50] -->
470

<!-- b001590 | prose | pages [50] -->
471

<!-- b001591 | prose | pages [50] -->
472

<!-- b001592 | prose | pages [50] -->
for i=1:currentlong, 473

<!-- b001593 | prose | pages [50] -->
if i==7, 474

<!-- b001594 | prose | pages [50] -->
text(plrep(i,1)-2,plrep(i,2),num2str(plrep(i,3))); 475

<!-- b001595 | prose | pages [50] -->
elseif i==8, 476

<!-- b001596 | prose | pages [50] -->
text(plrep(i,1)+.5,plrep(i,2),num2str(plrep(i,3))); 477

<!-- b001597 | prose | pages [50] -->
elseif i==12, 478

<!-- b001598 | prose | pages [50] -->
else 479

<!-- b001599 | prose | pages [50] -->
text(plrep(i,1)+.5,plrep(i,2),num2str(plrep(i,3))); 480

<!-- b001600 | furniture | pages [51] -->
Control Number: 11759

<!-- b001601 | furniture | pages [51] -->
Page 51 of 51

<!-- b001602 | prose | pages [51] -->
end 481

<!-- b001603 | prose | pages [51] -->
end 482

<!-- b001604 | prose | pages [51] -->
%} 483

<!-- b001605 | prose | pages [51] -->
484

<!-- b001606 | prose | pages [51] -->
485

<!-- b001607 | prose | pages [51] -->
%{ 486

<!-- b001608 | prose | pages [51] -->
h=plot(clusters(:,1),clusters(:,2),'v',... 487

<!-- b001609 | prose | pages [51] -->
'MarkerSize',10,'LineWidth',2,'MarkerEdgeColor','k'); 488

<!-- b001610 | prose | pages [51] -->
axis([-40 40 -40 40]); 489

<!-- b001611 | prose | pages [51] -->
set(h, 'Color', [.8 .8 .8]); 490

<!-- b001612 | prose | pages [51] -->
get(h); 491

<!-- b001613 | prose | pages [51] -->
%} 492

<!-- b001614 | prose | pages [51] -->
493

<!-- b001615 | prose | pages [51] -->
axis([-40 40 -40 40]); 494

<!-- b001616 | prose | pages [51] -->
axis('square') 495

<!-- b001617 | prose | pages [51] -->
hold off 496

<!-- b001618 | prose | pages [51] -->
disp('number of repeaters'),disp(repno); 497

<!-- b001619 | prose | pages [51] -->
498

<!-- b001620 | prose | pages [51] -->
disp('number of PL repeaters'),disp(noplrep); 499

<!-- b001621 | prose | pages [51] -->
disp('number of channels'),disp(openchannels); 500
