# P-B-2024-2419984-bb98b101

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2024

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | title | pages [1] -->
2419984

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
微信公众号：数学模型

<!-- b000009 | title | pages [1] -->
Time is Life: Precise Localization and Faster Search

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
After losing contact with the main ship, a suitable positioning model, search equipment, and search strategy for the submersible can signiﬁcantly reduce rescue time and increase the success rate of the rescue mission. In this paper, based on diﬀerent malfunction scenarios of the sub- mersible, a positioning model and search strategy for the submersible’s movement have been es- tablished, providing some suggestion for maritime rescue.

<!-- b000012 | prose | pages [1] -->
For Problem 1, ﬁrstly, we searched for the depth and ocean current information in the Ionian

<!-- b000013 | title | pages [1] -->
微信号：MATHmodels

<!-- b000014 | prose | pages [1] -->
Sea and ﬁtted the seaﬂoor topography. Then, a location model is conducted. Utilizing the fourth- order Runge-Kutta method, numerical solutions are obtained, and potential motion trajectories are plotted. The primary uncertainties in the model include the submersible’s initial state, ocean currents, and fault conditions. Therefore, the submersible should be equipped with sensors such as GPS and inertial navigation systems, regularly sending position information, depth, motion data, and surrounding ocean current data to the host ship.

<!-- b000015 | prose | pages [1] -->
For Problem 2, we used the entropy-weight method to calculate the weights of performance data and costs for the corresponding rescue devices. Employing a cost-beneﬁt model, scores are obtained.Considering the characteristics of each rescue device, we determined the following strat- egy: primarily using drones for surface search, sonar for underwater search, and purchasing a small quantity of AUVs for deeper regions.

<!-- b000016 | prose | pages [1] -->
For Problem 3, we ﬁrst discretize the search area into grids and added realistic disturbances to ocean currents and fault conditions. Using the Monte Carlo simulation method, we obtain the probability of the submersible appearing in each grid over time. Subsequently, utilizing the ant colony algorithm and continually updating the objective function based on the Bayesian probability model over time, we identify the most eﬃcient search path, achieving a 43% probability of ﬁnding the submersible within 10 hours. Finally, by setting diﬀerent search start times, we ﬁnd that starting later resulted in a lower probability of ﬁnding the submersible within 10 hours.

<!-- b000017 | prose | pages [1] -->
For Problem 4, the possible extensions of the model is discussed. For areas with more complex terrain and stronger ocean currents, such as the Caribbean Sea, relevant disturbances need to be increased. In cases with multiple submersibles, communication between them would facilitate search and rescue.

<!-- b000018 | prose | pages [1] -->
Finally, we analyze the impact of drag coeﬃcient errors on the model and evaluate the strengths and weaknesses of model.And a two-page Memo has been written for the Greek government.

<!-- b000019 | keywords | pages [1] -->
Keywords: Dynamics Model, Monte Carlo Simulation, Ant Colony Algorithm, Cost-Beneﬁt

<!-- b000020 | prose | pages [1] -->
Analysis based on EWM, Bayesian Detection

<!-- b000021 | furniture | pages [1] -->
关注数学模型

<!-- b000022 | furniture | pages [1] -->
2

<!-- b000023 | furniture | pages [1] -->
MATHmodels

<!-- b000024 | furniture | pages [1] -->
获取更多资讯

<!-- b000025 | furniture | pages [2] -->
Team # 2419984

<!-- b000026 | furniture | pages [2] -->
Page 2 of 25

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1 Introduction

<!-- b000029 | contents | pages [2] -->
3

<!-- b000030 | contents | pages [2] -->
1.1

<!-- b000031 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
3

<!-- b000033 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000034 | contents | pages [2] -->
1.2

<!-- b000035 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
3

<!-- b000037 | contents | pages [2] -->
1.3

<!-- b000038 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
4

<!-- b000040 | contents | pages [2] -->
2 Assumptions and Justiﬁcations

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
3 Notations

<!-- b000043 | contents | pages [2] -->
5

<!-- b000044 | contents | pages [2] -->
4 Model Preparation

<!-- b000045 | contents | pages [2] -->
5

<!-- b000046 | contents | pages [2] -->
4.1

<!-- b000047 | contents | pages [2] -->
Safety Strategy

<!-- b000048 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
5

<!-- b000050 | contents | pages [2] -->
4.2

<!-- b000051 | contents | pages [2] -->
Seaﬂoor Topography

<!-- b000052 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
6

<!-- b000054 | contents | pages [2] -->
4.3

<!-- b000055 | contents | pages [2] -->
The relevant parameters of the submersible

<!-- b000056 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
6

<!-- b000058 | contents | pages [2] -->
5 Models and Solutions of Problem 1

<!-- b000059 | contents | pages [2] -->
6

<!-- b000060 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000061 | contents | pages [2] -->
5.1

<!-- b000062 | contents | pages [2] -->
Location Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
6

<!-- b000064 | contents | pages [2] -->
5.2

<!-- b000065 | contents | pages [2] -->
Model Solving

<!-- b000066 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
9

<!-- b000068 | contents | pages [2] -->
5.3

<!-- b000069 | contents | pages [2] -->
Uncertainty of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
11

<!-- b000071 | contents | pages [2] -->
5.4

<!-- b000072 | contents | pages [2] -->
Measures and Equipment to Reduce Uncertainty . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
12

<!-- b000074 | contents | pages [2] -->
5.4.1

<!-- b000075 | contents | pages [2] -->
Measures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
12

<!-- b000077 | contents | pages [2] -->
5.4.2

<!-- b000078 | contents | pages [2] -->
Equipment

<!-- b000079 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
12

<!-- b000081 | contents | pages [2] -->
6 Models and Solutions of Problem 2

<!-- b000082 | contents | pages [2] -->
13

<!-- b000083 | contents | pages [2] -->
6.1

<!-- b000084 | contents | pages [2] -->
Rescue Equipment

<!-- b000085 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
13

<!-- b000087 | contents | pages [2] -->
6.2

<!-- b000088 | contents | pages [2] -->
Cost-Beneﬁt Model Based on Entropy Weight Method

<!-- b000089 | contents | pages [2] -->
. . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
13

<!-- b000091 | contents | pages [2] -->
6.3

<!-- b000092 | contents | pages [2] -->
Evaluation Results and Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
15

<!-- b000094 | contents | pages [2] -->
7 Models and Solutions of Problem 3

<!-- b000095 | contents | pages [2] -->
15

<!-- b000096 | contents | pages [2] -->
7.1

<!-- b000097 | contents | pages [2] -->
Model preparation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000098 | contents | pages [2] -->
15

<!-- b000099 | contents | pages [2] -->
7.2

<!-- b000100 | contents | pages [2] -->
Model for Searching

<!-- b000101 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [2] -->
17

<!-- b000103 | contents | pages [2] -->
7.2.1

<!-- b000104 | contents | pages [2] -->
Search Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [2] -->
17

<!-- b000106 | contents | pages [2] -->
7.2.2

<!-- b000107 | contents | pages [2] -->
Ant Colony Algorithm for Planning Search Paths . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
18

<!-- b000109 | contents | pages [2] -->
7.3

<!-- b000110 | contents | pages [2] -->
Results and Analysis

<!-- b000111 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [2] -->
19

<!-- b000113 | contents | pages [2] -->
7.3.1

<!-- b000114 | contents | pages [2] -->
Planning Results of Search Route

<!-- b000115 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [2] -->
19

<!-- b000117 | contents | pages [2] -->
7.3.2

<!-- b000118 | contents | pages [2] -->
The Impact of Start Time for Searching . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
20

<!-- b000120 | contents | pages [2] -->
8 Model Expansion and Promotion for Problem 4

<!-- b000121 | contents | pages [2] -->
20

<!-- b000122 | contents | pages [2] -->
Diﬀerent Maritime Regions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [2] -->
8.1

<!-- b000124 | contents | pages [2] -->
20

<!-- b000125 | contents | pages [2] -->
8.2

<!-- b000126 | contents | pages [2] -->
Multiple Submersibles

<!-- b000127 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000128 | contents | pages [2] -->
21

<!-- b000129 | contents | pages [2] -->
9 Sensitivity Analysis

<!-- b000130 | contents | pages [2] -->
22

<!-- b000131 | contents | pages [2] -->
10 Strengths and Weaknesses

<!-- b000132 | contents | pages [2] -->
22

<!-- b000133 | contents | pages [2] -->
10.1 Strengths

<!-- b000134 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000135 | contents | pages [2] -->
22

<!-- b000136 | contents | pages [2] -->
10.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000137 | contents | pages [2] -->
23

<!-- b000138 | contents | pages [2] -->
References

<!-- b000139 | contents | pages [2] -->
23

<!-- b000140 | furniture | pages [2] -->
关注数学模型

<!-- b000141 | furniture | pages [2] -->
2

<!-- b000142 | furniture | pages [2] -->
MATHmodels

<!-- b000143 | furniture | pages [2] -->
获取更多资讯

<!-- b000144 | furniture | pages [3] -->
Team # 2419984

<!-- b000145 | furniture | pages [3] -->
Page 3 of 25

<!-- b000146 | heading | pages [3] -->
1 Introduction

<!-- b000147 | heading | pages [3] -->
1.1 Problem Background

<!-- b000148 | prose | pages [3] -->
微信公众号：数学模型 With the development of diving technology, deep-sea diving has gradually found its way into the tourism industry and has become a favorite among many tourists. With the help of diving equipment such as submarines, tourists can explore the mysterious underwater world and enjoy the beauty of the ocean ﬂoor. A Greek company called "Maritime Cruises Mini-Submarines " (MCMS) manufactures submersibles capable of descending into the deep sea. MCMS now hopes to use their submersibles to lead tourists on an adventurous exploration of the sunken shipwrecks in the Ionian Sea.

<!-- b000149 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000150 | caption | pages [3] -->
Figure 1: Beautiful Deep Sea Bottom[1]

<!-- b000151 | prose | pages [3] -->
However, due to the current state of diving technology and submarine manufacturing tech- niques, there may be issues such as communication interruptions and loss of propulsion during the descent. When encountering such problems, it is crucial to quickly and accurately determine the approximate location of the submersible for subsequent rescue operations. This requires a compre- hensive consideration of factors such as underwater topography, seawater density, ocean currents, and other practical considerations.

<!-- b000152 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000153 | prose | pages [3] -->
For the requirements and tasks given, we restate them to help better position the focus of our work.

<!-- b000154 | prose | pages [3] -->
• Build a model to predict the underwater vehicle’s location over time after losing commu- nication with the host ship, and analyze the uncertain factors during the prediction process.

<!-- b000155 | prose | pages [3] -->
Based on this, determine the equipment that the underwater vehicle should be equipped with to reduce prediction uncertainty and the information that should be sent to the host ship before an incident.

<!-- b000156 | furniture | pages [3] -->
关注数学模型

<!-- b000157 | furniture | pages [3] -->
2

<!-- b000158 | furniture | pages [3] -->
MATHmodels

<!-- b000159 | furniture | pages [3] -->
获取更多资讯

<!-- b000160 | furniture | pages [4] -->
Team # 2419984

<!-- b000161 | furniture | pages [4] -->
Page 4 of 25

<!-- b000162 | prose | pages [4] -->
• Taking into account costs associated with availability, maintenance, readiness, and usage of this equipment, determine the additional search or rescue equipment that the host ship and rescue vessels should carry, if necessary.

<!-- b000163 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000164 | prose | pages [4] -->
• Develop a model based on the information from the location model in Task 1 to determine the initial deployment point and search pattern , in order to minimize the time it takes to ﬁnd a lost submersible. Then provide a probability function for ﬁnding the submersible.

<!-- b000165 | prose | pages [4] -->
• Extend the model established above to make it applicable in diﬀerent marine environments and with varying numbers of submersibles.

<!-- b000166 | heading | pages [4] -->
1.3 Our Work

<!-- b000167 | prose | pages [4] -->
To address the mentioned issues, our work can be illustrated with the following ﬂowchart:

<!-- b000168 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000169 | caption | pages [4] -->
Figure 2: The Framework of Our Work

<!-- b000170 | heading | pages [4] -->
2 Assumptions and Justiﬁcations

<!-- b000171 | prose | pages [4] -->
• During the time when the submersible loses contact, the weather at sea is stable, and signiﬁcant changes are unlikely to occur. In most cases, the ocean is calm. Moreover, abrupt weather changes are not the focus of the model study.

<!-- b000172 | furniture | pages [4] -->
关注数学模型

<!-- b000173 | furniture | pages [4] -->
2

<!-- b000174 | furniture | pages [4] -->
MATHmodels

<!-- b000175 | furniture | pages [4] -->
获取更多资讯

<!-- b000176 | furniture | pages [5] -->
Team # 2419984

<!-- b000177 | furniture | pages [5] -->
Page 5 of 25

<!-- b000178 | prose | pages [5] -->
• If a submersible touches the bottom during the descent process, it will be unable to move on its own. Due to the presence of abundant sediment on the seabed, the buoyancy will signiﬁcantly decrease, making it diﬃcult for the submersible to resurface on its own.

<!-- b000179 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000180 | prose | pages [5] -->
• All rescue equipment can be deployed within one hour after the submersible goes miss- ing. For maritime search and rescue, time is precious. One hour is suﬃcient if the rescue preparations are thorough.

<!-- b000181 | heading | pages [5] -->
3 Notations

<!-- b000182 | prose | pages [5] -->
symbol Deﬁnitions unit

<!-- b000183 | prose | pages [5] -->
M Kg The total mass of the submersible m3 V The volume of the submersible. 微信号：MATHmodels m/s2 a The acceleration of the submersible m/s2 g Gravity Acceleration m/s v The speed of the submersible m/s vc Ocean Current Velocity Kg/m3 ρ The density of seawater.

<!-- b000184 | prose | pages [5] -->
F f N The resistance experienced by the submersible FB N Buoyancy Coeﬃcient of Drag ∖ Cd ∖ Re Reynolds Number t h The time for search and rescue

<!-- b000185 | prose | pages [5] -->
Note: There are some notations that are not listed here and will be discussed in detail in each section.

<!-- b000186 | heading | pages [5] -->
4 Model Preparation

<!-- b000187 | heading | pages [5] -->
4.1 Safety Strategy

<!-- b000188 | prose | pages [5] -->
In the actual submersion process of a submersible, in the event of an accident, communication with the main ship may be lost. Based on the fundamental principles of search and rescue, to ensure safety, it is advisable to stay in place after losing contact with the main ship. Due to the diﬃculty of determining the submersible’s position in the deep sea and the main ship being unaware of the submersible’s status, it is recommended that, after losing contact with the main ship, the submersible, regardless of whether it still has propulsion, should immediately cease movement to avoid complicating the search and rescue eﬀorts.

<!-- b000189 | furniture | pages [5] -->
关注数学模型

<!-- b000190 | furniture | pages [5] -->
2

<!-- b000191 | furniture | pages [5] -->
MATHmodels

<!-- b000192 | furniture | pages [5] -->
获取更多资讯

<!-- b000193 | furniture | pages [6] -->
Team # 2419984

<!-- b000194 | furniture | pages [6] -->
Page 6 of 25

<!-- b000195 | heading | pages [6] -->
4.2 Seaﬂoor Topography

<!-- b000196 | prose | pages [6] -->
When the submersible loses propulsion, its movement may be inﬂuenced by the underwater topography. Therefore, we consulted relevant information[2] on the underwater topography of the 微信公众号：数学模型 Ionian Sea and ﬁtted the seaﬂoor terrain.

<!-- b000197 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000198 | caption | pages [6] -->
Figure 3: The topographic map of the Ionian Sea

<!-- b000199 | heading | pages [6] -->
4.3 The relevant parameters of the submersible

<!-- b000200 | prose | pages [6] -->
When establishing the model, obtaining appropriate parameters for the submersible is essential. The ﬁgure on the right illustrates one type of submersible, indicating rele- vant dimensions of the submersible. The maximum designed depth for the submersible in the right ﬁgure is 4000 meters, which corresponds to the maximum depth of the Ionian

<!-- b000201 | caption | pages [6] -->
Figure 4: The submersible[3]

<!-- b000202 | prose | pages [6] -->
Sea.

<!-- b000203 | heading | pages [6] -->
5 Models and Solutions of Problem 1

<!-- b000204 | heading | pages [6] -->
5.1 Location Model

<!-- b000205 | prose | pages [6] -->
For the convenience of model establishment and subsequent analytical calculations, we take the sea level as the xy-plane, with the vertical direction as the z-axis.

<!-- b000206 | prose | pages [6] -->
• Location model in the vertical direction

<!-- b000207 | prose | pages [6, 7] -->
Based on the previously mentioned safety strategy, after losing communication with the host ship, the submersible immediately ceases active movement, regardless of whether it still has propulsion, and ascends promptly. According to Newton’s second law, we have:

<!-- b000208 | furniture | pages [6] -->
关注数学模型

<!-- b000209 | furniture | pages [6] -->
2

<!-- b000210 | furniture | pages [6] -->
MATHmodels

<!-- b000211 | furniture | pages [6] -->
获取更多资讯

<!-- b000212 | furniture | pages [7] -->
Team # 2419984

<!-- b000213 | furniture | pages [7] -->
Page 7 of 25

<!-- b000215 | prose | pages [7] -->
Maz = −Mg + FB −F f (1) 微信公众号：数学模型 where az represents the vertical acceleration of the submersible, FB is the buoyancy it experiences, and F f is the resistance acting on the submersible in the vertical direction.

<!-- b000216 | prose | pages [7] -->
According to the working principle of the submersible, the ascent or descent of the submersible is determined by the amount of seawater in the submersible’s water tank. We can express the total mass of the submersible as follows:

<!-- b000217 | prose | pages [7] -->
M = m + mwater (2)

<!-- b000218 | prose | pages [7] -->
where m is the total mass of the submersible excluding the water tank, and mwater is the mass of the water tank. To simplify the model, we assume a constant rate of water inﬂow and outﬂow in the water tank until it is ﬁlled or emptied.

<!-- b000219 | prose | pages [7] -->
It is worth noting that after losing propulsion, other power systems of the submersible 微信号：MATHmodels may also fail. If the submersible’s other power systems have not failed, it can ascend normally. However, if the other power systems of the submersible fail, it will be unable to ascend by expelling water from the ballast tank. Instead, it may sink to the seabed or ascend to certain neutral buoyancy points under the inﬂuence of initial velocity and acceleration. At this point, the mass of water in the tank remains at its initial value. The impact of whether the submersible can drain and ascend normally will be discussed and validated in subsequent model solutions.

<!-- b000220 | prose | pages [7] -->
According to Archimedes’ principle of buoyancy[4], we have:

<!-- b000221 | prose | pages [7] -->
ρ ≈1.022 −0.01z 1500 (g/cm3) FB = ρgV (3)

<!-- b000222 | prose | pages [7] -->
where ρ is the density of seawater and V is the volume of the submersible.

<!-- b000223 | prose | pages [7] -->
Due to the relatively small ascent and descent speeds of the submersible, the water ﬂow around its surface is in a laminar state during motion.Therefore, the water ﬂow resistance acting on the submersible can be expressed as follows:

<!-- b000224 | prose | pages [7] -->
F f = 1 2Cd · ρAv2 (4)

<!-- b000225 | prose | pages [7] -->
where Cd is the drag coeﬃcient, A is the area of the submersible’s upper and lower surfaces, ρ is the density of water, and v is the speed of the submersible.Moreover, the direction of water ﬂow resistance is always opposite to the direction of the submersible’s movement.

<!-- b000226 | prose | pages [7] -->
According to ﬂuid dynamics knowledge, the drag coeﬃcient Cd in laminar ﬂow can be deter- mined by the Reynolds number Re:

<!-- b000227 | prose | pages [7] -->
Cd = 64 (5) Re At diﬀerent ﬂow rates, the Reynolds number varies. Since the relative velocity is time-varying, we assume a constant value for Re based on empirical values, and subsequently calculate the drag coeﬃcient Cd. The impact of the assumed Cd values on the model will be discussed in the subsequent sensitivity analysis.

<!-- b000228 | furniture | pages [7] -->
关注数学模型

<!-- b000229 | furniture | pages [7] -->
2

<!-- b000230 | furniture | pages [7] -->
MATHmodels

<!-- b000231 | furniture | pages [7] -->
获取更多资讯

<!-- b000232 | furniture | pages [8] -->
Team # 2419984

<!-- b000233 | furniture | pages [8] -->
Page 8 of 25

<!-- b000234 | prose | pages [8] -->
So far, by simultaneously combining equations (2), (3), (4), (5), and (6), the diﬀerential equa- tion for the vertical motion of the submersible can be obtained:

<!-- b000235 | prose | pages [8] -->
(m + mw(t)) · d2z Re · ρ(z) · A · (dz dt2 = −(m + mw(t)) · g + ρ(z) · gV −1 2 · 64 dt )2 微信公众号：数学模型 (6)

<!-- b000236 | prose | pages [8] -->
• Location model in the XY plane

<!-- b000237 | prose | pages [8] -->
Compared to the vertical direction, the movement of the submersible in the XY plane is not inﬂuenced by buoyancy but is signiﬁcantly aﬀected by ocean currents. According to the safety strategy mentioned earlier, the submersible’s propulsion force is considered to be 0. Firstly, we analyze the movement of the submersible in the x-direction. According to Newton’s second law, we have:

<!-- b000238 | prose | pages [8] -->
M · ax = Fcx (7)

<!-- b000239 | prose | pages [8] -->
At this point, the submersible is only inﬂuenced by ocean currents.

<!-- b000240 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000241 | caption | pages [8] -->
Figure 5: Currents in Ionian Sea[5]

<!-- b000242 | prose | pages [8] -->
The ﬁgure displays a schematic representation of the currents in a speciﬁc area of the Ionian Sea at a certain time. The diagram provides information about the general direction and average velocity of the currents[6] in the depicted region.

<!-- b000243 | prose | pages [8] -->
Since ocean currents generally have a relatively small and stable velocity, they can be consid- ered to be in a laminar ﬂow state.Therefore, Fcx can be expressed as follows:

<!-- b000244 | prose | pages [8] -->
 Fcx = 1 2Cdx · ρAx(v −vcx)2 (8) Cdx = 64 Re

<!-- b000245 | prose | pages [8] -->
where Ax represents the area of the submersible subjected to the action of ocean currents.

<!-- b000246 | furniture | pages [8] -->
关注数学模型

<!-- b000247 | furniture | pages [8] -->
2

<!-- b000248 | furniture | pages [8] -->
MATHmodels

<!-- b000249 | furniture | pages [8] -->
获取更多资讯

<!-- b000250 | furniture | pages [9] -->
Team # 2419984

<!-- b000251 | furniture | pages [9] -->
Page 9 of 25

<!-- b000252 | prose | pages [9] -->
Similarly, we can obtain a similar motion model for the submersible in the y-direction. Com- pared to the model in the vertical direction, the challenge in determining the coordinates of the submersible in the xy-plane lies in the uncertainty of ocean currents.

<!-- b000253 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000254 | heading | pages [9] -->
5.2 Model Solving

<!-- b000255 | prose | pages [9] -->
In the vertical direction, due to the complexity of equation (7), it is diﬃcult to obtain an analyti- cal solution through mathematical methods. Therefore, we use a numerical method —Runge-Kutta method for solving.

<!-- b000256 | prose | pages [9] -->
•The fourth-order Runge-Kutta method

<!-- b000257 | prose | pages [9] -->
When solving the model, we employ the fourth-order Runge-Kutta method with a higher pre- cision, and the truncation error is O(h5), where h is the chosen step size.

<!-- b000258 | prose | pages [9] -->
For the initial value problem of the ﬁrst-order ordinary diﬀerential equation given as follows:

<!-- b000259 | prose | pages [9] -->
 ˙z = f(t, z) 微信号：MATHmodels (9) z(t0) = z0

<!-- b000260 | prose | pages [9] -->
The recursive formula for solving using the fourth-order Runge-Kutta method is:

<!-- b000261 | prose | pages [9] -->
 tn+1 = tn + h k1 = f(zn, tn) k2 = f(zn + h 2 · k1, tn + h 2) (10) k3 = f(zn + h 2 · k2, tn + h 2) k4 = f(zn + h · k3, tn + h) zn+1 = zn + h 6 · (k1 + 2k2 + 2k3 + k4)

<!-- b000262 | prose | pages [9] -->
yn is determined by the sum of the current y(n −1) and the unit time change. The unit time change is the product of the time interval h and the approximate slope.

<!-- b000263 | prose | pages [9] -->
• Algorithm improvement and application

<!-- b000264 | prose | pages [9] -->
⋄Step1:Determination of Initial Conditions: The data such as the submersible’s velocity and acceleration can be obtained from corresponding sensors. The velocity and acceleration transmitted to the main ship at the last moment can be considered as the submersible’s initial velocity and acceleration.

<!-- b000265 | prose | pages [9] -->
⋄Step2:Diﬀerential Equation Processing: Since the established position model is a second- order diﬀerential equation, it needs to be transformed into a ﬁrst-order diﬀerential equation.

<!-- b000266 | prose | pages [9, 10] -->
Simultaneously, the ﬁrst-order derivative terms are moved to the left side of the equation, and the remaining terms are moved to the right side. The transformed equation is:

<!-- b000267 | furniture | pages [9] -->
关注数学模型

<!-- b000268 | furniture | pages [9] -->
2

<!-- b000269 | furniture | pages [9] -->
MATHmodels

<!-- b000270 | furniture | pages [9] -->
获取更多资讯

<!-- b000271 | furniture | pages [10] -->
Team # 2419984

<!-- b000272 | furniture | pages [10] -->
Page 10 of 25

<!-- b000274 | prose | pages [10] -->
 ′(t) = u(t) x ′(t) = v(t) y 微信公众号：数学模型 ′(t) = w(t) z 1 2Cdx · ρAx · (u(t) −vcx)2 ′(t) = u (11) (m + mw(t)) 1 2Cdy · ρAy · (v(t) −vcy)2 ′(t) = v (m + mw(t)) ′(t) = −(m + mw(t)) · g + ρ(z) · gV −1 2 · Fc · ρ(z) · A · (w(t))2 w (m + mw(t))

<!-- b000275 | prose | pages [10] -->
⋄Step3:Iterative solution of the algorithm: Set the step size h=1s, iterate over a length of 10 hours, calculate the values of k1, k2, k3, k4 corresponding to the two diﬀerential equations using the recursive formula, and then determine the next discrete value z(n + 1).

<!-- b000276 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000277 | prose | pages [10] -->
• Results and Analysis

<!-- b000278 | prose | pages [10] -->
To solve and validate the model we established, we randomly select a point in the deep sea as the initial position of the submersible, and provide initial velocity and acceleration values for the submersible.

<!-- b000279 | prose | pages [10] -->
⋄When the submersible can resurface normally:

<!-- b000280 | prose | pages [10] -->
At this point, the submersible’s water tank drains normally until it is empty. By substituting the initial velocity and acceleration of the submersible and iterating continuously, we can plot the trajectory of the submersible’s motion after losing contact with the host ship as follows:

<!-- b000281 | caption | pages [10] -->
Figure 6: Possible trajectories of the submersible’s movement

<!-- b000282 | furniture | pages [10] -->
关注数学模型

<!-- b000283 | furniture | pages [10] -->
2

<!-- b000284 | furniture | pages [10] -->
MATHmodels

<!-- b000285 | furniture | pages [10] -->
获取更多资讯

<!-- b000286 | furniture | pages [11] -->
Team # 2419984

<!-- b000287 | furniture | pages [11] -->
Page 11 of 25

<!-- b000288 | prose | pages [11] -->
The selected initial point in the ﬁgure is (18, 37, -3147) (where x and y coordinates represent longitude and latitude, and z is the depth). The submersible initially descends a short distance under the inﬂuence of the initial velocity and then begins to resurface. In the xy plane, due to the inﬂuence of ocean currents, the position continuously shifts over time. 微信公众号：数学模型 ⋄When the submersible cannot resurface normally:

<!-- b000289 | prose | pages [11] -->
At this point, there is a malfunction in the water tank. Considering real-world scenarios, we as- sume that after the water tank failure, its mass follows a uniform distribution between the minimum and maximum mass:

<!-- b000290 | prose | pages [11] -->
In this case, due to the uncertainty in the initial state and water tank mass, the submersible may either touch the bottom or reach the neutral buoyancy point. Through multiple simulations, we obtained trajectories where the submersible either hits the bottom or hovers, as shown below:

<!-- b000291 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000292 | caption | pages [11] -->
Figure 7: Possible trajectories of the submersible’s movement

<!-- b000293 | prose | pages [11] -->
In the left ﬁgure, due to a malfunction in the water tank, the submersible continuously sinks to the seabed as gravity exceeds buoyancy.

<!-- b000294 | prose | pages [11] -->
In the right ﬁgure, a portion of the water in the submersible’s water tank is discharged. Upon reaching a speciﬁc depth, the submersible remains in a suspended state due to the decreased density of seawater, experiencing slight oscillations above and below the neutral buoyancy point.

<!-- b000295 | heading | pages [11] -->
5.3 Uncertainty of the Model

<!-- b000296 | prose | pages [11] -->
During the process of model establishment and solving, we have identiﬁed that the position of the submersible can be inﬂuenced by the following uncertainties:

<!-- b000297 | prose | pages [11] -->
• Initial Position: The submersible’s location before losing contact varies, and the starting point for model establishment diﬀers. This leads to signiﬁcant diﬀerences in the subsequent movement trajectory of the submersible.

<!-- b000298 | furniture | pages [11] -->
关注数学模型

<!-- b000299 | furniture | pages [11] -->
2

<!-- b000300 | furniture | pages [11] -->
MATHmodels

<!-- b000301 | furniture | pages [11] -->
获取更多资讯

<!-- b000302 | furniture | pages [12] -->
Team # 2419984

<!-- b000303 | furniture | pages [12] -->
Page 12 of 25

<!-- b000304 | prose | pages [12] -->
• Initial Velocity and Acceleration: According to the safety strategy mentioned earlier, the submersible will immediately deactivate propulsion after losing contact with the main ship.

<!-- b000305 | prose | pages [12] -->
The submersible will then commence movement with initial velocity and acceleration. The initial conditions have a signiﬁcant impact on the predicted results of the model. 微信公众号：数学模型

<!-- b000306 | prose | pages [12] -->
• Ocean Currents: For a submersible that has lost propulsion, the force exerted by ocean currents is the primary reason for its continuous movement. Ocean currents vary with time, seasons, and the temperature of seawater, exhibiting signiﬁcant short-term randomness. This randomness is a crucial uncertainty factor in the model.

<!-- b000307 | prose | pages [12] -->
• Seabed Topography: As the exact underwater topography cannot be precisely determined in advance, the submersible’s movement may be constrained by the terrain, introducing un- certainty to the model.

<!-- b000308 | heading | pages [12] -->
5.4 Measures and Equipment to Reduce Uncertainty

<!-- b000309 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000310 | heading | pages [12] -->
5.4.1 Measures

<!-- b000311 | prose | pages [12] -->
For potential accidents, reducing uncertainty factors means improving safety. To minimize uncertainties in the model, enhance the likelihood and accuracy of predictions, the submersible should regularly transmit its position information, movement speed and acceleration, ocean current information, as well as data about the surrounding environment or terrain to the main ship before losing contact with the host ship.

<!-- b000312 | heading | pages [12] -->
5.4.2 Equipment

<!-- b000313 | prose | pages [12] -->
We recommend equipping the submersible with the following devices:

<!-- b000314 | prose | pages [12] -->
• GPS Positioning Device:GPS is a technology that determines location using satellite sig- nals. However, underwater, GPS signals cannot penetrate the water surface directly, so the submersible’s GPS positioning typically requires coordination with buoys or surface vessels.

<!-- b000315 | prose | pages [12] -->
• Inertial Navigation System:An inertial navigation system uses sensors such as accelerome- ters and gyroscopes to measure the submersible’s acceleration and angular velocity. Velocity can be obtained through integration.

<!-- b000316 | prose | pages [12] -->
• Underwater High-Deﬁnition Camera:Can be used to observe underwater environments, acquire seaﬂoor topography, thereby reducing the risk of encountering hazards.

<!-- b000317 | prose | pages [12] -->
• Pressure Sensor:As the water pressure in the deep sea is approximately linearly related to depth, the depth at which the submersible is located can be calculated based on the measured water pressure.

<!-- b000318 | prose | pages [12] -->
• Magnetometer:By measuring the Earth’s magnetic ﬁeld, the submersible’s orientation can be determined.

<!-- b000319 | prose | pages [12] -->
• Current Detection Sensors:By detecting the direction and speed of ocean currents, the impact of random currents on predictions can be reduced.

<!-- b000320 | furniture | pages [12] -->
关注数学模型

<!-- b000321 | furniture | pages [12] -->
2

<!-- b000322 | furniture | pages [12] -->
MATHmodels

<!-- b000323 | furniture | pages [12] -->
获取更多资讯

<!-- b000324 | furniture | pages [13] -->
Team # 2419984

<!-- b000325 | furniture | pages [13] -->
Page 13 of 25

<!-- b000326 | heading | pages [13] -->
6 Models and Solutions of Problem 2

<!-- b000327 | heading | pages [13] -->
6.1 Rescue Equipment

<!-- b000328 | prose | pages [13] -->
微信公众号：数学模型 According to the position model established in the previous section, when the submersible loses contact with the main ship, it may sink to the seaﬂoor, remain at certain neutral buoyancy points, or rise to the sea surface depending on diﬀerent failure scenarios. This presents varied requirements for search and rescue operations. We deﬁne regions with depths below 3000 meters as deep-water zones and those above 3000 meters as shallow-water zones. To address all possible situations, we have researched equipment designed for search and rescue in surface, shallow-water, and deep-water areas. The speciﬁcations and costs of these devices are presented in the table below:

<!-- b000329 | caption | pages [13] -->
Table 1: Equipment and Parameters[7]

<!-- b000330 | prose | pages [13] -->
Failure Rate Detection Maintenance Operating Precision(cm) Equipment and Parameters Accuracy(%) Price($) (%) Range Cost($) Cost($) Search and 18.4 × 106 1 7.8 92 1034 50 14 微信号：MATHmodels Rescue Drones Surface Maritime Search 6 × 106 0.5 11.6 94 3415 100 20 and Rescue Boats Side-scan Sonar 0.05 224 10.2 98 24995 200 90 Shallow-water Zone Autonomous Underwater 0.1 30 2.5 99.4 35248 900 87 Robot Autonomous Underwater 0.2 67 5 98.6 45652 1000 120 Vehicle Side-scan Sonar 0.2 400 40.8 95 24995 200 90 Deep-water Zone Autonomous Underwater 0.4 30 4.5 98.9 35248 900 87 Robot Autonomous Underwater 1.0 65 6 96 45652 1000 120 Vehicle

<!-- b000331 | prose | pages [13] -->
where, precision represents the minimum distance that the equipment can resolve.The smaller the value, the stronger the resolution capability of the device.

<!-- b000332 | prose | pages [13] -->
Taking into account the performance of the equipment and the associated costs of purchasing, maintaining, and using, we adopt a cost-beneﬁt model based on the entropy weight method to evaluate various rescue devices. This aims to achieve the optimal conﬁguration while ensuring rescue eﬃciency.

<!-- b000333 | heading | pages [13] -->
6.2 Cost-Beneﬁt Model Based on Entropy Weight Method

<!-- b000334 | prose | pages [13] -->
• Entropy weight method to determine weights Due to the diﬀerent working areas applicable to diﬀerent devices, and the performance of the same device varies at diﬀerent depths, it is necessary to determine the optimal devices separately for the surface, shallow water, and deep water areas. Taking the evaluation of the shallow water area as an example:

<!-- b000335 | prose | pages [13, 14] -->
(1) Standardize the performance parameters Input the various performance indicators and cost indicators of the three types of equipment in the shallow water area into the matrix. For the failure rate and minimum resolution ac- curacy in the beneﬁt indicators, since smaller values indicate better equipment performance, their reciprocals are written into the matrix.

<!-- b000336 | furniture | pages [13] -->
关注数学模型

<!-- b000337 | furniture | pages [13] -->
2

<!-- b000338 | furniture | pages [13] -->
MATHmodels

<!-- b000339 | furniture | pages [13] -->
获取更多资讯

<!-- b000340 | furniture | pages [14] -->
Team # 2419984

<!-- b000341 | furniture | pages [14] -->
Page 14 of 25

<!-- b000343 | prose | pages [14] -->
  · · · x11 x12 x14 · · · x21 x22 x24 微信公众号：数学模型 X0 = (12) ... ... ... ...

<!-- b000344 | prose | pages [14] -->
· · · xn1 xn2 xn4 As all evaluation indicators are non-negative, the standardization formula is used as follows:

<!-- b000345 | prose | pages [14] -->
xij zij = (13) √∑n i=1 x2 ij

<!-- b000346 | prose | pages [14] -->
Then we can get the standardized matrix Z0. (2) Entropy Calculating The matrix Z0 obtained through standardization can be further used to calculate the proba- bility matrix P, where the calculation formula for each element pi j in P is as follows:

<!-- b000347 | prose | pages [14] -->
zij 微信号：MATHmodels pij = ∑n (14) i=1 zij Then,the entropy value ej of the ith index can be deﬁned as:

<!-- b000348 | prose | pages [14] -->
∑ n e j = −1 pij ln(pi j)( j = 1, 2, · · · , 4) (15) ln n i=1 The range of entropy value ej is [0, 1].The larger the e j is,the greater the diﬀerentiation degree of index j is, and more information can be derived. Hence, higher weight should be given to the index. Therefore,the weight Wj is deﬁned as follows:

<!-- b000349 | prose | pages [14] -->
1 −e j Wj = ∑m j=1(1 −e j), j = 1, 2, · · · , 4 (16)

<!-- b000350 | prose | pages [14] -->
• Cost-beneﬁt evaluation model Multiplying the weights corresponding to various performance indicators of rescue equip- ment by the normalized data yields the weighted matrix. At this point, the beneﬁts and costs of each rescue device can be represented as follows:

<!-- b000351 | prose | pages [14] -->
 Ei = ∑m j=1 WjPij (17) Ci = Ctotal(i) ∑C Where Ei represents the beneﬁt indicator, and Ci represents the cost indicator. Ci includes the expenses for the purchase, maintenance, and single-use of the equipment. To achieve better visual representation, we have also normalized C. Then, the evaluation score (REC) for each device can be represented by the ratio of E to C as follows: Reci = Ei (18) Ci By comparing the scores, the superiority and inferiority of each rescue device can be deter- mined. A higher score indicates relatively better performance and relatively lower costs for the device.

<!-- b000352 | furniture | pages [14] -->
关注数学模型

<!-- b000353 | furniture | pages [14] -->
2

<!-- b000354 | furniture | pages [14] -->
MATHmodels

<!-- b000355 | furniture | pages [14] -->
获取更多资讯

<!-- b000356 | furniture | pages [15] -->
Team # 2419984

<!-- b000357 | furniture | pages [15] -->
Page 15 of 25

<!-- b000358 | heading | pages [15] -->
6.3 Evaluation Results and Analysis

<!-- b000359 | prose | pages [15] -->
Based on the evaluation model, combined with the relevant data in Table 2, we conducted eval- uations of rescue equipment in the sea surface, shallow water area, and deep water area, obtaining 微信公众号：数学模型 scores for ﬁve types of rescue equipment: Autonomous Underwater Vehicle (AUV), Autonomous Underwater Robot (AUR), Side-scan Sonar (SSS), Search and Rescue Drones (SRD), and Mar- itime Search and Rescue Boats (MSRB). The results are displayed as follows:

<!-- b000360 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000361 | caption | pages [15] -->
Figure 8: Evaluation Results

<!-- b000362 | prose | pages [15] -->
From the chart, it can be observed that in surface search and rescue, the score of Search and Rescue Drones (SRD) is signiﬁcantly higher than Maritime Search and Rescue Boats, demonstrat- ing higher search and rescue eﬃciency and lower costs. In shallow water and deep water areas, the score of Side-scan Sonar (SSS) is also signiﬁcantly higher than others. Therefore, the combination of Drones and Sonar as the main search and rescue equipment is reasonable.

<!-- b000363 | prose | pages [15] -->
It is worth noting that, although SSS has a high score, it is powerless in deeper depths. How- ever, AUVs can operate in deeper regions. And AUR has the highest exploration accuracy, making it advantageous in dealing with more complex seabed terrain. Therefore, we recommend the main search and rescue equipment to be Search and Rescue Drones and Side-scan Sonar, with a smaller number of AUVs and AURs. This approach can ensure search and rescue eﬃciency as much as possible within an acceptable cost range, preparing for any possible scenarios.

<!-- b000364 | heading | pages [15] -->
7 Models and Solutions of Problem 3

<!-- b000365 | heading | pages [15] -->
7.1 Model preparation

<!-- b000366 | prose | pages [15, 16] -->
Using the location model, we can determine the trajectory of the submersible if the initial position of the submersible, fault conditions, ocean current data, and seaﬂoor topography are all known.However, in reality, the fault conditions of the submersible, ocean current speed, and di- rection are subject to signiﬁcant randomness. Therefore, the submersible may appear in diﬀerent locations in the ocean with varying probabilities, and these probability distributions will change over time. To obtain the probability distribution of the submersible’s position over time, we employ Monte Carlo simulation.

<!-- b000367 | furniture | pages [15] -->
关注数学模型

<!-- b000368 | furniture | pages [15] -->
2

<!-- b000369 | furniture | pages [15] -->
MATHmodels

<!-- b000370 | furniture | pages [15] -->
获取更多资讯

<!-- b000371 | furniture | pages [16] -->
Team # 2419984

<!-- b000372 | furniture | pages [16] -->
Page 16 of 25

<!-- b000374 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000375 | prose | pages [16] -->
• Divide Search Area into Grids

<!-- b000376 | prose | pages [16] -->
As the submersible loses or shuts oﬀpropulsion, its speed gradually approaches the speed of ocean currents over time. Therefore, we calculated the maximum range the submersible could reach after 10 hours. We divided the area into grids with dimensions of 400m in length and width, resulting in a total of 30 × 75 grids. By discretizing the region, we can use numerical methods to simulate the probability of the submersible appearing at various points. This approach is helpful in actual search operations to avoid overlooking potential locations.

<!-- b000377 | prose | pages [16] -->
• Monte Carlo Simulation

<!-- b000378 | prose | pages [16] -->
To simulate the real movement of the submersible, we ﬁrst simulated the uncertainty of ocean currents. Over a short period, the stable speed and direction angle of ocean currents can be approx- 微信号：MATHmodels imated to follow a normal distribution:

<!-- b000379 | prose | pages [16] -->
 vc ∼N(vc, σ2 1) (19) θ ∼N(θ, σ2 2)

<!-- b000380 | prose | pages [16] -->
where vc and θ represent the average speed and average direction angle of the ocean currents, respectively.

<!-- b000381 | prose | pages [16] -->
Additionally, if the submersible can resurface normally, the rescue operation will be much easier. Therefore, we focus on analyzing the situation of a malfunction in the submersible’s water tank and assume that the mass of water in the tank follows a uniform distribution:

<!-- b000382 | prose | pages [16] -->
mw ∼U(mmin, mmax) (20)

<!-- b000383 | prose | pages [16] -->
We selected the same longitude and latitude as in Question 1 for the moment when the sub- mersible lost contact with the main ship, with a depth set at 1500 meters.Then, using Monte Carlo random number simulation, we generated 100,000 sets of possible states and substituted them into the positioning model to determine the coordinates of the submersible at 1, 2, ..., 10 hours later.

<!-- b000384 | prose | pages [16] -->
In Figure 9, we can observe the results simulated from these 100,000 initial state points.

<!-- b000385 | prose | pages [16] -->
• The left graph illustrates the distribution of these points after 10 hours. Due to the initial perturbations, among these points, 19.1% can reach the sea surface, 17.2% remain at depths between 0 to 1500 meters, 36% stay at depths between 1500 to 3000 meters, and 27.67% are at the seaﬂoor.As the number of simulations is suﬃcient, the proportion of occurrences in a speciﬁc area can approximate the probability of the submersible appearing there.

<!-- b000386 | prose | pages [16] -->
• In the diagram on the right, a top-down view of the trajectories of these simulated points within 10 hours is depicted. It can be observed from the diagram that the trajectories diverge outward along the average direction of the ocean currents, further highlighting the signiﬁcant impact of the uncertainty of the ocean currents on the submersible’s trajectory.

<!-- b000387 | furniture | pages [16] -->
关注数学模型

<!-- b000388 | furniture | pages [16] -->
2

<!-- b000389 | furniture | pages [16] -->
MATHmodels

<!-- b000390 | furniture | pages [16] -->
获取更多资讯

<!-- b000391 | furniture | pages [17] -->
Team # 2419984

<!-- b000392 | furniture | pages [17] -->
Page 17 of 25

<!-- b000393 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000394 | caption | pages [17] -->
Figure 9: Possible trajectories of the submersible’s movement

<!-- b000395 | prose | pages [17] -->
微信号：MATHmodels In the left of ﬁgure 10, we speciﬁcally depict the trajectories of points that sink to the seaﬂoor and those that resurface to the neutral buoyancy point over the course of 10 hours. The trajecto- ries of points resurfacing to the neutral buoyancy point are roughly similar to those described in Problem 1.

<!-- b000396 | prose | pages [17] -->
And the probability heatmap depicting the likelihood of the submersible resurfacing to the sea level over time is shown in the right in ﬁgure 10.From the heatmap, it can be observed that the water tanks capable of resurfacing normally can reach the sea surface in approximately 1 hour. With the increase in time, there is a slight increase in the number of submersibles capable of resurfacing to the sea surface. This aligns well with the actual scenario.

<!-- b000397 | caption | pages [17] -->
Figure 10: Some speciﬁc simulation points

<!-- b000398 | heading | pages [17] -->
7.2 Model for Searching

<!-- b000399 | heading | pages [17] -->
7.2.1 Search Strategy

<!-- b000400 | prose | pages [17, 18] -->
The equipment used for search and rescue varies depending on the location where the sub- mersible goes missing. In problem two, we identiﬁed Drones as the main maritime search equip- ment and sonar as the primary underwater search equipment. Maritime and underwater searches should be conducted simultaneously.

<!-- b000401 | furniture | pages [17] -->
关注数学模型

<!-- b000402 | furniture | pages [17] -->
2

<!-- b000403 | furniture | pages [17] -->
MATHmodels

<!-- b000404 | furniture | pages [17] -->
获取更多资讯

<!-- b000405 | furniture | pages [18] -->
Team # 2419984

<!-- b000406 | furniture | pages [18] -->
Page 18 of 25

<!-- b000408 | heading | pages [18] -->
7.2.2 Ant Colony Algorithm for Planning Search Paths

<!-- b000409 | prose | pages [18] -->
微信公众号：数学模型 Through Monte Carlo simulation, we can determine the probability of the submersible appear- ing in a speciﬁc grid at a certain moment and simulate the trajectory of the submersible over a period of time. For points that have already been searched, we can simulate their subsequent positions. These points will disappear from the subsequent search maps. Taking into account the time required for each set of equipment to search a grid, we set the search period T = 1h. Since T is relatively short, and the submersible’s position changes minimally, we assume its position remains unchanged within one search cycle and update the position at the beginning of the next search cycle.

<!-- b000410 | heading | pages [18] -->
▲Bayesian Probability Model

<!-- b000411 | prose | pages [18] -->
The probability of ﬁnding the submersible is time-varying and depends on the search results 微信号：MATHmodels of the previous cycle. Using the Bayesian probability model:

<!-- b000412 | prose | pages [18] -->
P(Ai) · P(B|Ai) P(Ai|B) = , i = 1, · · · , n (21) n∑ l=1 P(Al) · P(B|Al)

<!-- b000413 | prose | pages [18] -->
the probability within the current search cycle can be expressed as follows:

<!-- b000414 | prose | pages [18] -->
P(i) = P(i −1) + P(i −1) · Pi (22)

<!-- b000415 | prose | pages [18] -->
where: P(i) represents the probability of ﬁnding it until the i-th search, and Pi represents the probability of ﬁnding it in a single search.

<!-- b000416 | prose | pages [18] -->
▲Objective Function for Search The probability of ﬁnding the submersible after time t is denoted as P(t). In addition to being related to the choice of the search route, with the increase in search time, P(t) generally exhibits a trend of initially increasing and then decreasing[8]. To minimize the time required to locate the submersible, we have established the following objective function:

<!-- b000417 | prose | pages [18] -->
S (t) = e−kt · P(t) (23)

<!-- b000418 | prose | pages [18] -->
where the urgency level based on time is reﬂected in the parameter k.

<!-- b000419 | prose | pages [18] -->
▲Determine the starting point

<!-- b000420 | prose | pages [18] -->
Since all the uncertain factors in the simulation approximately follow a normal distribution, the probability is relatively large around the point of maximum probability. Therefore, to improve search eﬃciency and reduce search time, we choose the grid with the highest prob- ability as the starting point for the search.

<!-- b000421 | heading | pages [18] -->
▲Algorithm ﬂowchart

<!-- b000422 | prose | pages [18] -->
In order to visually represent the process of utilizing the ant colony algorithm, we have drawn the algorithm ﬂowchart as shown below:

<!-- b000423 | furniture | pages [18] -->
关注数学模型

<!-- b000424 | furniture | pages [18] -->
2

<!-- b000425 | furniture | pages [18] -->
MATHmodels

<!-- b000426 | furniture | pages [18] -->
获取更多资讯

<!-- b000427 | furniture | pages [19] -->
Team # 2419984

<!-- b000428 | furniture | pages [19] -->
Page 19 of 25

<!-- b000429 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000430 | caption | pages [19] -->
Figure 11: Flowchart for Ant Colony Algorithm

<!-- b000431 | heading | pages [19] -->
7.3 Results and Analysis

<!-- b000432 | heading | pages [19] -->
7.3.1 Planning Results of Search Route

<!-- b000433 | prose | pages [19] -->
One hour after the loss of contact, relevant equipment begins the search. The grid with the highest probability at 1 hour is selected as the initial deployment point. By applying the ant colony algorithm and periodically updating the search map, iterating until convergence, we can obtain the 微信号：MATHmodels search route as shown in the following diagram:

<!-- b000434 | prose | pages [19] -->
(a) Planning Route (b) Iteration Results

<!-- b000435 | caption | pages [19] -->
Figure 12: Diﬀerent probabilities with diﬀerent t

<!-- b000436 | prose | pages [19] -->
The diagram (a) provides a top-down view of 100,000 simulated points, with the black area indicating the initial point positions and the white area representing the stopping points after 10 hours of search. The light red bands cover 80% of the simulated points along the direction of the ocean currents.

<!-- b000437 | prose | pages [19] -->
It can be observed that most simulated points are distributed near the direction of the ocean currents, and the search path obtained through the ant colony algorithm also follows the direction of the currents. This result is reasonable as it aligns with the actual outcomes.

<!-- b000438 | prose | pages [19] -->
In (b) of ﬁgure 12, the probability of ﬁnding the submersible on the sea surface during each iteration of the ant colony algorithm is displayed. When the number of iterations reaches 40, the probability of ﬁnding the submersible on the sea surface within 10 hours converges to around 12%. As revealed by previous simulations, only 19% of the total number of submersibles can resurface to the sea surface within 10 hours. Therefore, the probability of ﬁnding the submersible on the sea surface within 10 hours is higher at 63%. Due to lower search eﬃciency, the success rate of ﬁnding the submersible underwater will be lower than on the sea surface .

<!-- b000439 | furniture | pages [19] -->
关注数学模型

<!-- b000440 | furniture | pages [19] -->
2

<!-- b000441 | furniture | pages [19] -->
MATHmodels

<!-- b000442 | furniture | pages [19] -->
获取更多资讯

<!-- b000443 | furniture | pages [20] -->
Team # 2419984

<!-- b000444 | furniture | pages [20] -->
Page 20 of 25

<!-- b000445 | heading | pages [20] -->
7.3.2 The Impact of Start Time for Searching

<!-- b000446 | prose | pages [20] -->
In the above model, we took t=1h. However, in reality, t is often greater than one hour due to various factors. Therefore, to study the impact of t on the 10-hour model, we obtained the time- 微信公众号：数学模型 dependent overall probability of ﬁnding the submersible within 10 hours of search initiation under the conditions of t=1h, 3h, and 5h, with the remaining parameters being the same, as shown in the following graph:

<!-- b000447 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000448 | caption | pages [20] -->
Figure 13: Planning Results of Search Route

<!-- b000449 | prose | pages [20] -->
From the graph, it can be observed that if the search starts at t=1h, the probability of ﬁnding the submersible within 10 hours reaches 43%. The later the search is initiated, the lower the probability of ﬁnding the submersible within 10 hours. If the search begins at t=5h, the probability of ﬁnding the submersible within 10 hours is only about 10%. This tells us that time is crucial for rescue operations. Therefore, after the submersible loses contact with the main ship, rescue eﬀorts should be deployed as soon as possible to increase the probability of ﬁnding it in a short time.

<!-- b000450 | heading | pages [20] -->
8 Model Expansion and Promotion for Problem 4

<!-- b000451 | prose | pages [20] -->
The model, being based on the actual parameters of the submersible and the ocean, possesses strong generalizability.

<!-- b000452 | heading | pages [20] -->
8.1 Diﬀerent Maritime Regions

<!-- b000453 | prose | pages [20] -->
When considering rescue operations in diﬀerent maritime regions, it is crucial to have a com- prehensive understanding of the local climate, topography, and ocean currents. Taking the Caribbean Sea as an example:

<!-- b000454 | prose | pages [20, 21] -->
• Climate and Ocean Currents The Caribbean Sea has a tropical oceanic climate, with highly unstable atmospheric condi- tions and the presence of tropical storms locally from June to November each year. There- fore, compared to the Mediterranean climate in the Ionian Sea, the surface ocean currents in the Caribbean Sea are more intense and complex. When simulating ocean current data in the relevant area, it is necessary to increase the perturbation values of local ocean currents over time. This will cause a submersible that loses power to quickly lose the inﬂuence of its initial velocity, resulting in a more divergent movement trajectory. 微信公众号：数学模型

<!-- b000455 | furniture | pages [20] -->
关注数学模型

<!-- b000456 | furniture | pages [20] -->
2

<!-- b000457 | furniture | pages [20] -->
MATHmodels

<!-- b000458 | furniture | pages [20] -->
获取更多资讯

<!-- b000459 | furniture | pages [21] -->
Team # 2419984

<!-- b000460 | furniture | pages [21] -->
Page 21 of 25

<!-- b000462 | prose | pages [21] -->
• Topography The terrain in the Ionian Sea is relatively ﬂat, but it is the opposite near the Caribbean Sea. The underwater terrain in the vicinity of the Caribbean Sea has large ﬂuctuations, with numerous reefs and rocks, contributing to numerous shipwrecks in the Caribbean Sea.

<!-- b000463 | prose | pages [21] -->
Therefore, when simulating, accidents caused by the submersible hitting rocks must be con- sidered. It is necessary to enhance the physical model to simulate the impact of collisions on the submersible’s path. After hitting a rock, the submersible immediately loses power and its original velocity, with a probability of mass loss. It should be able to drift with the ocean currents to prevent the simulation from mistakenly detecting it as being stuck at the bottom.

<!-- b000464 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000465 | caption | pages [21] -->
Figure 14: The Topography of Caribbean Sea

<!-- b000466 | prose | pages [21] -->
Combining these two factors makes search operations in the Caribbean more complex, placing higher demands on the accuracy of the model and simulated data.

<!-- b000467 | heading | pages [21] -->
8.2 Multiple Submersibles

<!-- b000468 | prose | pages [21] -->
In scenarios where there are multiple submersibles in a relatively small area, we analyze that, assuming normal communication with the mothership, simultaneous loss of communication or mechanical failure for multiple submersibles is rare and can be disregarded. Therefore, after the ﬁrst submersible loses contact, judgment needs to be made based on its last communication status.

<!-- b000469 | prose | pages [21] -->
In the event of a submersible loss, real-time ocean currents, atmospheric conditions, and the geographical status of the last known position before the loss should be checked.

<!-- b000470 | prose | pages [21] -->
• If there are local storms or severe marine activities: the mothership needs to immediately warn the remaining submersibles to leave or stay away from the relevant area.

<!-- b000471 | prose | pages [21, 22] -->
• If no danger is detected near the lost submersible: the remaining submersibles do not need to avoid it. Under favorable conditions, they can approach the missing submersible for timely deployment of subsequent search and rescue eﬀorts. According to the results of the third question, this signiﬁcantly increases the probability of locating the missing sub- mersible.

<!-- b000472 | furniture | pages [21] -->
关注数学模型

<!-- b000473 | furniture | pages [21] -->
2

<!-- b000474 | furniture | pages [21] -->
MATHmodels

<!-- b000475 | furniture | pages [21] -->
获取更多资讯

<!-- b000476 | furniture | pages [22] -->
Team # 2419984

<!-- b000477 | furniture | pages [22] -->
Page 22 of 25

<!-- b000479 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000480 | heading | pages [22] -->
9 Sensitivity Analysis

<!-- b000481 | prose | pages [22] -->
Due to the close relationship between the drag coeﬃcients of the submersible and the shape, size, and maritime conditions of the actual submersible, the drag coeﬃcients in all three direc- tions are estimated values. In this section, a sensitivity analysis is conducted on these three drag coeﬃcients. By varying them by ±1%, 2%,and 4%, while keeping other conditions constant, the trajectories for these six scenarios are simulated. A comparison is made between these simulated trajectories and the original trajectory, resulting in the two graphs presented below.

<!-- b000482 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000483 | caption | pages [22] -->
Figure 15: The impact of drag coeﬃcient errors

<!-- b000484 | prose | pages [22] -->
From the graph a, it can be observed that after 10 hours in the xy dimensions, the deviation of the trajectory does not exceed 400 meters in any direction. This is within an acceptable range, indicating that it does not signiﬁcantly aﬀect the main direction of the trajectory. Additionally, in the grid-based map used in the third question, such deviations also have no impact.Through extensive practical simulations, it has been observed that the position region in the z-direction of the submersible stabilizes after 3 hours. Therefore, a deviation value at 3 hours is considered. From the graph b, it can be seen that in the z dimension, the maximum deviation does not exceed 40 meters, which is still within an acceptable range.

<!-- b000485 | heading | pages [22] -->
10 Strengths and Weaknesses

<!-- b000486 | heading | pages [22] -->
10.1 Strengths

<!-- b000487 | prose | pages [22] -->
• This model, starting from a dynamics perspective, has established a relatively accurate pre- dictive model for the submersible, oﬀering high precision in its predictions.

<!-- b000488 | furniture | pages [22] -->
关注数学模型

<!-- b000489 | furniture | pages [22] -->
2

<!-- b000490 | furniture | pages [22] -->
MATHmodels

<!-- b000491 | furniture | pages [22] -->
获取更多资讯

<!-- b000492 | furniture | pages [23] -->
Team # 2419984

<!-- b000493 | furniture | pages [23] -->
Page 23 of 25

<!-- b000494 | prose | pages [23] -->
• The paper adopts a cost-beneﬁt model based on the entropy weighting method to evaluate sensors, ensuring more accurate assignment of weight values when calculating beneﬁts.

<!-- b000495 | prose | pages [23] -->
• The paper utilizes theories related to Bayesian detection and combines them with Ant Colony 微信公众号：数学模型 Optimization. It considers the impact of certain probabilities being tested ﬁrst on the subse- quent sample space during detection, aligning more closely with reality.

<!-- b000496 | heading | pages [23] -->
10.2 Weaknesses

<!-- b000497 | prose | pages [23] -->
• Due to the diﬃculty in calculating the drag coeﬃcient, this paper only estimates an ap- proximate value. Accurate measurement is required when extending the model to practical application scenarios.

<!-- b000498 | prose | pages [23] -->
• In the predictive model, a method of discretizing time is used to determine the ﬁnal probabil- ity of successful rescue. Due to the insuﬃcient level of discretization, there may be certain errors. 微信号：MATHmodels

<!-- b000499 | heading | pages [23] -->
References

<!-- b000500 | references | pages [23] -->
[1] https://pxhere.com/en/photo/1237494?utm_content=shareClip&utm_medium=

<!-- b000501 | references | pages [23] -->
referral&utm_source=pxhere

<!-- b000502 | references | pages [23] -->
[2] NOAA National Centers for Environmental Information. 2022: ETOPO 2022 15 Arc-Second

<!-- b000503 | references | pages [23] -->
Global Relief Model. NOAA National Centers for Environmental Information. https://

<!-- b000504 | references | pages [23] -->
doi.org/10.25921/fd45-gt74 Accessed [3 February,2024].

<!-- b000505 | references | pages [23] -->
[3] https://tritonsubs.com

<!-- b000506 | references | pages [23] -->
[4] Zeng Guanghui, Zang Haipeng, Gu Zezue. Study on the Longitudinal Motion Characteristics

<!-- b000507 | references | pages [23] -->
of a Powerless Submarine Underwater Drift [C]// Salvage and Rescue Committee of The

<!-- b000508 | references | pages [23] -->
China Institute of Navigation. Proceedings of the 8th China International Salvage Forum.

<!-- b000509 | references | pages [23] -->
Naval Submarine Academy, 2014: 3.

<!-- b000510 | references | pages [23] -->
[5] Gai,˘aM.,˘aG.

<!-- b000511 | references | pages [23] -->
Civitarese,˘aG.

<!-- b000512 | references | pages [23] -->
Borzelli,˘aV.

<!-- b000513 | references | pages [23] -->
Kovaevi,˘aP.-M.

<!-- b000514 | references | pages [23] -->
Poulain,˘aA.

<!-- b000515 | references | pages [23] -->
L.

<!-- b000516 | references | pages [23] -->
Eusebi

<!-- b000517 | references | pages [23] -->
Theocharis,˘aM. Menna,˘aA. Catucci, and˘aN. Zarokanellos˘a(2011),˘aOn the relationship

<!-- b000518 | references | pages [23] -->
between the decadal oscillations of the northern Ionian Sea and the salinity distributions in

<!-- b000519 | references | pages [23] -->
the eastern Mediterranean,˘aJ. Geophys. Res.,˘a116, C12002, doi:10.1029/2011JC007280.

<!-- b000520 | references | pages [23] -->
[6] ESR; Dohan, Kathleen. 2022. Ocean Surface Current Analyses Real-time (OSCAR) Sur-

<!-- b000521 | references | pages [23] -->
face Currents - Interim 0.25 Degree (Version 2.0). Ver. 2.0. PO.DAAC, CA, USA. Dataset

<!-- b000522 | references | pages [23] -->
accessed [2024-02-03] at˘ahttps://doi.org/10.5067/OSCAR-25I20

<!-- b000523 | references | pages [23] -->
[7] https://marinesonic.com/

<!-- b000524 | references | pages [23] -->
[8] Potomac Management Group, Inc. (2006). A Simple Guide to Conducting Ground Search

<!-- b000525 | references | pages [23] -->
and Rescue Detection Experiments. Washington, D.C.: United States Coast Guard Oﬃce of

<!-- b000526 | references | pages [23] -->
Search and Rescue.

<!-- b000527 | furniture | pages [23] -->
关注数学模型

<!-- b000528 | furniture | pages [23] -->
2

<!-- b000529 | furniture | pages [23] -->
MATHmodels

<!-- b000530 | furniture | pages [23] -->
获取更多资讯

<!-- b000531 | furniture | pages [24] -->
Team # 2419984

<!-- b000532 | furniture | pages [24] -->
Page 24 of 25

<!-- b000533 | heading | pages [24] -->
Memo

<!-- b000534 | prose | pages [24] -->
To: The Government of Greece From: MCM Team #2419984 微信公众号：数学模型 Date: Feb 5th,2024 Subject:Scientiﬁc positioning and rescue eﬀorts ensure the safety of deep-sea tourism.

<!-- b000535 | prose | pages [24] -->
Dear Oﬃcer of the Government of Greece,

<!-- b000536 | prose | pages [24] -->
It has come to our attention that a company in your country, MCMS, has developed a type of submersible suitable for tourists to explore the seabed. However, the potential for loss of commu- nication restricts its application and development. Therefore, we have established a dynamic and kinematic model of the submersible (see page ten), as well as a search and rescue strategy based on this model.

<!-- b000537 | prose | pages [24] -->
Firstly, after conducting a comprehensive force analysis on the submersible, we established a 微信号：MATHmodels kinematic model considering the impact of ocean currents in the Ionian Sea region on its move- ment. We found that once the submersible loses communication, its possible positions are greatly inﬂuenced by ocean currents. Worse still, we discovered that there are few ocean current mon- itoring points near the Ionian Sea, leading to inaccurate ocean current data and, consequently, excessive uncertainty in the submersible’s position. Installing more ocean current detection sta- tions in the Ionian Sea could signiﬁcantly improve the accuracy of determining the position of the lost submersible.

<!-- b000538 | prose | pages [24] -->
Secondly, through a comprehensive evaluation of the performance and cost indicators of var- ious search and rescue devices, we determined that the optimal equipment for surface and under- water searches are drones and sonar, respectively.

<!-- b000539 | prose | pages [24] -->
Thirdly, based on the kinematic model, using Monte Carlo simulation and ant colony algorithm, we found an optimal search and rescue solution that is most likely to locate the submersible as follows:

<!-- b000540 | furniture | pages [24] -->
关注数学模型

<!-- b000541 | furniture | pages [24] -->
2

<!-- b000542 | furniture | pages [24] -->
MATHmodels

<!-- b000543 | furniture | pages [24] -->
获取更多资讯

<!-- b000544 | furniture | pages [25] -->
Team # 2419984

<!-- b000545 | furniture | pages [25] -->
Page 25 of 25

<!-- b000546 | prose | pages [25] -->
The results suggest that the search path should be as perpendicular as possible to the curve predicted by the dynamic model, and the one-way search path should increase with time.

<!-- b000547 | prose | pages [25] -->
Additionally, for a lost submersible, time is of the essence, and the probability of successfully 微信公众号：数学模型 ﬁnding it decreases sharply with increasing time, as shown in the table below:

<!-- b000548 | prose | pages [25] -->
The search and rescue route should be as perpendicular as possible to the trajectory predicted by the dynamic model, and as time progresses, the length of each search path should also increase. Additionally, we have found that the probability of successfully detecting the submersible steeply decreases over time. The results are as follows in the table below:

<!-- b000549 | prose | pages [25] -->
微信号：MATHmodels Therefore, we recommend dispatching relevant detection equipment to the designated area as quickly as possible once the mothership loses communication with the submersible. Our model also indicates that deploying more detectors, with larger detection widths and higher accuracy, in- creases search eﬃciency and the probability of successfully detecting the submersible. Purchasing and stockpiling more advanced detection equipment (such as underwater detection vehicles, under- water robots, high-precision sonar, etc.) and strengthening cooperation with the MCMS company will signiﬁcantly increase the probability of ﬁnding the lost submersible.

<!-- b000550 | prose | pages [25] -->
In conclusion, with the use of advanced sensors and the position and search models we have established, there is a high probability of quickly locating the submersible after an accident, while ensuring the speed of rescue operations. We sincerely hope that the Greek government considers these suggestions to ensure the safety of tourists and promote the development of deep-sea tourism.

<!-- b000551 | prose | pages [25] -->
Thank you for considering this vital matter. I am available for any further discussion or clariﬁ- cation regarding the proposed model and technology.

<!-- b000552 | prose | pages [25] -->
Yours sincerely

<!-- b000553 | prose | pages [25] -->
#2419984

<!-- b000554 | furniture | pages [25] -->
关注数学模型

<!-- b000555 | furniture | pages [25] -->
2

<!-- b000556 | furniture | pages [25] -->
MATHmodels

<!-- b000557 | furniture | pages [25] -->
获取更多资讯
