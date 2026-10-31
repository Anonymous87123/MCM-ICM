# P-B-2015-40612-8bcdc1a7

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Searching for a Lost Plane

<!-- b000002 | prose | pages [1] -->
February 10, 2015

<!-- b000003 | title | pages [1] -->
1

<!-- b000004 | heading | pages [1] -->
Summary

<!-- b000005 | prose | pages [1] -->
The year 2014 witnessed a series of air disasters that resulted in huge loss of life, among them is the mysterious disappearance of Malaysia Airlines Flight 370 (MH370) in the Indian Ocean. Although the related countries spent great efforts on the crucial task of ﬁnding the plane, considering the vast space to search and the paucity of information, the plane is still not found. In past experiences, mathematical models played a leading role in helping ﬁnd lost planes in open water. In this paper, we discuss mathematical models that can assist to ﬁnd aircrafts lost in sea.

<!-- b000006 | prose | pages [1] -->
In order to build a mathematical model to assist the planning of a search for a lost plane considered to have crashed in open water, we ﬁrst analyze the possi- ble scenarios and propose our assumptions and hypothesis. Then we establish a collision model to predict the number of drifters resulting from the crash accord- ing to the type of the plane we are searching for. For the main part, we set up a search model based on Bayes’ theorem, considering the behavior of the drifters resulted from the crash, the outcome of water surface search and underwater search sequentially to instruct further searching process. Moreover, the alloca- tion of search areas to diverse search planes use branch and bound algorithm to optimize the possible result of the search process, both on the water surface and underwater. A simulation module is built to test our model using both ﬁctional and real situations and to carry out the calculations.

<!-- b000007 | prose | pages [1] -->
Then we apply our model in the actual cases of Air France Flight 447 (AF447) and MH370, applying the real world data. Our recommended searching area for the AF447 case matches the location of the wreckage underwater, while for MH370 we predict its possible wreckage position based on accessible informa- tion.

<!-- b000008 | prose | pages [1] -->
Afterwards sensibility analysis is applied to our model, which shows that

<!-- b000009 | prose | pages [1] -->
1

<!-- b000010 | furniture | pages [2] -->
Team # 40612

<!-- b000011 | furniture | pages [2] -->
Page 2 of 34

<!-- b000012 | prose | pages [2] -->
our model is stable and robust while ready to adapt to different situations. Last but not least, we discuss the strengths and weaknesses of the model.

<!-- b000013 | prose | pages [2] -->
In summary, Our model excels in terms of accuracy, efﬁciency, its value of application and robustness, although we can still improve it considering the computational complexity, some unrealistic assumptions and how to determine some of the parameters of the model.

<!-- b000014 | keywords | pages [2] -->
Key Words:

<!-- b000015 | prose | pages [2] -->
Bayesian theorem, searching, lost plane, branch-and-bound algorithm

<!-- b000016 | furniture | pages [3] -->
Team # 40612

<!-- b000017 | furniture | pages [3] -->
Page 3 of 34

<!-- b000018 | heading | pages [3] -->
Contents

<!-- b000019 | contents | pages [3] -->
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | contents | pages [3] -->
1

<!-- b000021 | contents | pages [3] -->
1

<!-- b000022 | contents | pages [3] -->
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [3] -->
2

<!-- b000024 | contents | pages [3] -->
6

<!-- b000025 | contents | pages [3] -->
Base Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [3] -->
3

<!-- b000027 | contents | pages [3] -->
7

<!-- b000028 | contents | pages [3] -->
Type of Plane Crashed . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [3] -->
3.1

<!-- b000030 | contents | pages [3] -->
7

<!-- b000031 | contents | pages [3] -->
Type of Search Plane . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [3] -->
3.2

<!-- b000033 | contents | pages [3] -->
7

<!-- b000034 | contents | pages [3] -->
Assumption and Hypothesis . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [3] -->
4

<!-- b000036 | contents | pages [3] -->
8

<!-- b000037 | contents | pages [3] -->
Collision Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [3] -->
4.1

<!-- b000039 | contents | pages [3] -->
8

<!-- b000040 | contents | pages [3] -->
Simulation Module . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [3] -->
4.2

<!-- b000042 | contents | pages [3] -->
8

<!-- b000043 | contents | pages [3] -->
Water Surface Search Model . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [3] -->
4.3

<!-- b000045 | contents | pages [3] -->
9

<!-- b000046 | contents | pages [3] -->
Underwater Search Model . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [3] -->
4.4

<!-- b000048 | contents | pages [3] -->
9

<!-- b000049 | contents | pages [3] -->
Search Plan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [3] -->
4.5

<!-- b000051 | contents | pages [3] -->
9

<!-- b000052 | contents | pages [3] -->
Variable and Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [3] -->
5

<!-- b000054 | contents | pages [3] -->
6

<!-- b000055 | heading | pages [3] -->
Establishing and Solving of Model

<!-- b000056 | prose | pages [3] -->
10

<!-- b000057 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000058 | prose | pages [3] -->
10

<!-- b000059 | prose | pages [3] -->
Collision Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 10

<!-- b000060 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . 6.1.1 Air Disintegration 11

<!-- b000061 | prose | pages [3] -->
Water Disintegration . . . . . . . . . . . . . . . . . . . . . . 6.1.2 11

<!-- b000062 | prose | pages [3] -->
System Module . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 12

<!-- b000063 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . 6.3 Overview on Search Model 13

<!-- b000064 | prose | pages [3] -->
Review on Bayesian Filtering Algorithm 6.3.1 . . . . . . . . . .

<!-- b000065 | prose | pages [3] -->
13

<!-- b000066 | prose | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . 6.3.2 Steps of Search Plan 13

<!-- b000067 | prose | pages [3] -->
Water Surface Search Model . . . . . . . . . . . . . . . . . . . . . . 6.4 14

<!-- b000068 | prose | pages [3] -->
Surface Search Prior PDF for Impact Location 6.4.1 . . . . . . .

<!-- b000069 | prose | pages [3] -->
14

<!-- b000070 | prose | pages [3] -->
Surface Search Posterior PDF for Impact Location . . . . . 6.4.2 18

<!-- b000071 | prose | pages [3] -->
Underwater Search Model . . . . . . . . . . . . . . . . . . . . . . . 6.5 19

<!-- b000072 | furniture | pages [4] -->
Team # 40612

<!-- b000073 | furniture | pages [4] -->
Page 4 of 34

<!-- b000074 | prose | pages [4] -->
Underwater Search Prior PDF for Impact Location . . . . . 6.5.1 19

<!-- b000075 | prose | pages [4] -->
Phase I Searches . . . . . . . . . . . . . . . . . . . . . . . . . 6.5.2 19

<!-- b000076 | prose | pages [4] -->
Underwater Search Posterior PDF after Phase I . . . . . . . 6.5.3 19

<!-- b000077 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.5.4 Recursion 19

<!-- b000078 | prose | pages [4] -->
Allocation Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 21

<!-- b000079 | prose | pages [4] -->
Review on Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 21

<!-- b000080 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . 7.2 Allocation of Search Planes 21

<!-- b000081 | prose | pages [4] -->
Applying of Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8 22

<!-- b000082 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Application on AF447 22

<!-- b000083 | prose | pages [4] -->
Available Information . . . . . . . . . . . . . . . . . . . . . 8.1.1 23

<!-- b000084 | prose | pages [4] -->
Computation Process . . . . . . . . . . . . . . . . . . . . . . 8.1.2 23

<!-- b000085 | prose | pages [4] -->
Computation Result . . . . . . . . . . . . . . . . . . . . . . 8.1.3 23

<!-- b000086 | prose | pages [4] -->
Prediction on MH370 . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 24

<!-- b000087 | prose | pages [4] -->
Review on Established Models . . . . . . . . . . . . . . . . 8.2.1 24

<!-- b000088 | prose | pages [4] -->
Probability Distribution . . . . . . . . . . . . . . . . . . . . 8.2.2 26

<!-- b000089 | prose | pages [4] -->
Computation Process . . . . . . . . . . . . . . . . . . . . . . 8.2.3 26

<!-- b000090 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

<!-- b000091 | heading | pages [4] -->
Sensitivity Analysis

<!-- b000092 | prose | pages [4] -->
27

<!-- b000093 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . 9.1 The Number of Drifters 27

<!-- b000094 | prose | pages [4] -->
The Number of Search Planes . . . . . . . . . . . . . . . . . . . . . 9.2 28

<!-- b000095 | prose | pages [4] -->
The Types of Search Planes . . . . . . . . . . . . . . . . . . . . . . . 9.3 28

<!-- b000096 | prose | pages [4] -->
Weights in Computing Flight Dynamics PDF . . . . . . . . . . . . 9.4 29

<!-- b000097 | prose | pages [4] -->
Weights in Computing Surface Search Prior PDF . . . . . . . . . . 9.5 30

<!-- b000098 | prose | pages [4] -->
Weights in Computing Underwater Search Prior PDF . . . . . . . 9.6 30

<!-- b000099 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | heading | pages [4] -->
10 Strengths and Weaknesses

<!-- b000101 | prose | pages [4] -->
31

<!-- b000102 | prose | pages [4] -->
10.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | prose | pages [4] -->
31

<!-- b000104 | prose | pages [4] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10.2 Weaknesses 31

<!-- b000105 | furniture | pages [5] -->
Team # 40612

<!-- b000106 | furniture | pages [5] -->
Page 5 of 34

<!-- b000107 | heading | pages [5] -->
11 Non-technical Paper for Press Conference . . . . . . . . . . . . . . . .

<!-- b000108 | prose | pages [5] -->
32

<!-- b000109 | prose | pages [5] -->
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | prose | pages [5] -->
33

<!-- b000111 | furniture | pages [6] -->
Team # 40612

<!-- b000112 | furniture | pages [6] -->
Page 6 of 34

<!-- b000113 | prose | pages [6] -->
2

<!-- b000114 | heading | pages [6] -->
Introduction

<!-- b000115 | prose | pages [6] -->
Approaching its anniversary, the missing of Malaysia Airlines Flight 370 (MH370) on March 8, 2014 has become one of the mysteries in aviation his- tory. The dark riddle also reminds the public of the tragedy of Air France Flight 447 (AF447), which disappeared over the South Atlantic during a night ﬂight en route from Rio de Janeiro to Paris on June 1, 2009. It was nearly 2 years later when the plane wreckage was localized during the fourth phase of the sea searches.

<!-- b000116 | prose | pages [6] -->
With deepest condolences to the victims, authorities are pondering how to establish a more efﬁcient and accurate maritime search and rescue (SAR) simu- lation system. It is based on calculation and prediction of ﬂight dynamics, ocean models, substantial search consequence, etc. Currently, major difﬁculties lie in a paucity of data and scant knowledge of ocean geography (e.g. the largely un- charted bathymetry of the southern Indian Ocean’s sea ﬂoor hampers the rescue of MH370 [1]).

<!-- b000117 | prose | pages [6] -->
Our goal is to construct a generic and reliable mathematic model correspond- ing to a lost plane, which is feared to have crashed in open water in the way to point B from point A. Weighing the factors mentioned above, we propose a use- ful search plan to pinpoint the disappeared aircraft. Speciﬁcally, we will do the following things in this paper:

<!-- b000118 | prose | pages [6] -->
• Establish a collision model to determine the number of drifters resulting from the crash.

<!-- b000119 | prose | pages [6] -->
• Build simulation module to represent real movement of drifters in water.

<!-- b000120 | prose | pages [6] -->
• Propose a search model based on Bayes’ theorem, considering water sur- face search and underwater search sequentially to optimize on search ar- eas.

<!-- b000121 | prose | pages [6] -->
• Develop an allocation model to match search planes with search areas.

<!-- b000122 | prose | pages [6] -->
• Employ the preceding approach in the case of ﬁnding AF447 at the fourth attempt to verify the credibility of our model.

<!-- b000123 | prose | pages [6] -->
• Predict the possible location of MH370 wreckage with accessible data and offer advice to assist the further search effort.

<!-- b000124 | prose | pages [6] -->
• Analyze the strengths and weaknesses inherent in the model and conﬁrm the potential development direction.

<!-- b000125 | furniture | pages [7] -->
Team # 40612

<!-- b000126 | furniture | pages [7] -->
Page 7 of 34

<!-- b000127 | prose | pages [7] -->
3 Base Analysis

<!-- b000128 | prose | pages [7] -->
First of all, we will have an overall observation on the searching and dis- patching problem in reality. Noting that there are many different types of planes for which we might be searching and that there are many different types of search planes, often equipped with diverse electronics or sensors, it is of great interest and signiﬁcance to distinguish their inﬂuence on rescue.

<!-- b000129 | prose | pages [7] -->
3.1 Type of Plane Crashed

<!-- b000130 | prose | pages [7] -->
The type of the aircraft we are searching contributes to the number of drifters1

<!-- b000131 | prose | pages [7] -->
produced by a crash into the sea2. Intuitively, the more debris drifting on the water surface, the easier the rescue will be.

<!-- b000132 | prose | pages [7] -->
• Size. It conforms to common sense that large planes give rise to more aircraft debris than small ones under the same conditions.

<!-- b000133 | prose | pages [7] -->
• Passenger capacity. It is worth addressing that recovering bodies may be of more value. When we compute reverse drift (one of the key factors in the search plan), we do not have good models for the effect of leeway on certain type of aircraft debris, while bodies can be drifted back employing current estimates [3].

<!-- b000134 | prose | pages [7] -->
• Materials. Aircraft materials vary with different parts of a plane as well as different types of planes. Materials determine density and mechanical behaviors such as intensity, tenacity and impact resistance.

<!-- b000135 | prose | pages [7] -->
3.2 Type of Search Plane

<!-- b000136 | prose | pages [7] -->
Sorts of search aircrafts available are helicopters (H) and ﬁxed-wing aircrafts (F-W). They differ from each other mainly in search speed, voyage and search electronics and sensors. Speciﬁc examples are given to each type of search plane and their corresponding performances [4] are listed in Table 1 for comparison.

<!-- b000137 | prose | pages [7] -->
We gain heuristics from the table that we should employ distinguished air- crafts for distinct search areas and targets. Optimal control over search forces is required to develop an efﬁcient model. In addition, we note there are still subtle

<!-- b000138 | prose | pages [7] -->
1We deﬁne ’drifters’ as the generalization of bodies and aircraft debris. Aircraft debris are identiﬁed and classiﬁed by type: cabin, cargo, compartment, wing, belly fairing, LDMCR (Lower Deck Mobile Crew Rest) .[2])

<!-- b000139 | prose | pages [7] -->
2Other factors affecting the number of drifters include crash causes, ﬂight velocity and so on, which will be discussed about in details in 6.1.

<!-- b000140 | furniture | pages [8] -->
Team # 40612

<!-- b000141 | furniture | pages [8] -->
Page 8 of 34

<!-- b000142 | caption | pages [8] -->
Table 1: Comparison between Different Types of Search Planes

<!-- b000143 | prose | pages [8] -->
Example Type Search Speed (km/h)

<!-- b000144 | prose | pages [8] -->
SH-60B H 300

<!-- b000145 | prose | pages [8] -->
P-3C F-W 600

<!-- b000146 | prose | pages [8] -->
C-130H F-W 600

<!-- b000147 | prose | pages [8] -->
Voyage (km) Search Sensors

<!-- b000148 | prose | pages [8] -->
800 Sonar, Radar

<!-- b000149 | prose | pages [8] -->
Sonar, Radar, 4000 Magnetic anomaly detection,

<!-- b000150 | prose | pages [8] -->
Photographic equipment

<!-- b000151 | prose | pages [8] -->
3800 Radar

<!-- b000152 | prose | pages [8] -->
differences between speciﬁc aircraft models belonging to ﬁxed-wing aircrafts. However, for the simplicity of our model, we retain the classiﬁcation mentioned above.

<!-- b000153 | heading | pages [8] -->
Assumption and Hypothesis

<!-- b000154 | prose | pages [8] -->
4

<!-- b000155 | prose | pages [8] -->
For the feasibility of calculation and simulation, we make the following as- sumptions:

<!-- b000156 | prose | pages [8] -->
4.1

<!-- b000157 | heading | pages [8] -->
Collision Model

<!-- b000158 | prose | pages [8] -->
• The plane is full-loaded.

<!-- b000159 | prose | pages [8] -->
• The accidents can be classiﬁed into two situations according to disintegra- tion situations: Air Disintegration and Water Disintegration.

<!-- b000160 | prose | pages [8] -->
• In both disintegrations, the broken pieces are of the same size.

<!-- b000161 | prose | pages [8] -->
• In water disintegration, we regard it as an ideal collision process and the impulse suffered by the aircraft in horizontal direction can be omitted.

<!-- b000162 | prose | pages [8] -->
4.2 Simulation Module

<!-- b000163 | prose | pages [8] -->
• The drifters have the same initial position, which is the impact location.

<!-- b000164 | prose | pages [8] -->
• We do not distinguish drifters. That is, factors have equal impact on bodies and aircraft debris.

<!-- b000165 | prose | pages [8] -->
• On the surface of the water, the ﬂoating movement is simulated merely based on data on currents and random motion exerted by computer.

<!-- b000166 | furniture | pages [9] -->
Team # 40612

<!-- b000167 | furniture | pages [9] -->
Page 9 of 34

<!-- b000168 | prose | pages [9] -->
• Underwater parts are assumed to be static once they sink to the seaﬂoor.

<!-- b000169 | prose | pages [9] -->
4.3

<!-- b000170 | heading | pages [9] -->
Water Surface Search Model

<!-- b000171 | prose | pages [9] -->
• The drifters have the same initial position, which is the impact location.

<!-- b000172 | prose | pages [9] -->
• We do not distinguish drifters in aspect of their movement.

<!-- b000173 | prose | pages [9] -->
• We do not distinguish drifters in their detection probability.

<!-- b000174 | prose | pages [9] -->
• Drifters are assumed not to move during the search phase.

<!-- b000175 | prose | pages [9] -->
4.4

<!-- b000176 | heading | pages [9] -->
Underwater Search Model

<!-- b000177 | prose | pages [9] -->
• Underwater parts are assumed to be static once they sink to the seaﬂoor.

<!-- b000178 | prose | pages [9] -->
• Other assumptions are the same to those in water surface model.

<!-- b000179 | prose | pages [9] -->
4.5 Search Plan

<!-- b000180 | prose | pages [9] -->
• We cannot gather any signal from the crashed plane.

<!-- b000181 | prose | pages [9] -->
• Search vehicles are restricted to aircrafts.

<!-- b000182 | prose | pages [9] -->
• Different search capabilities of search planes are limited to search areas and detection rate.

<!-- b000183 | prose | pages [9] -->
• Search capability does not vary under different weather condition.

<!-- b000184 | prose | pages [9] -->
• Underwater detection capability is beyond the depth of seaﬂoor.

<!-- b000185 | prose | pages [9] -->
• The sensors are assumed to give no false target detection, while they may fail to call a detection when the target is present.

<!-- b000186 | prose | pages [9] -->
• We replace the constraint of voyage with the limit to search areas.

<!-- b000187 | furniture | pages [10] -->
Team # 40612

<!-- b000188 | furniture | pages [10] -->
Page 10 of 34

<!-- b000189 | prose | pages [10] -->
5 Variable and Deﬁnition

<!-- b000190 | caption | pages [10] -->
Table 2: Variable and Deﬁnition

<!-- b000191 | prose | pages [10] -->
N0 Maximum amount of drifters N Actual amount of drifters V Volume of the plane m Total weight of the plane α Ratio of N0 to V β Degree of disintegration of the plane v Flight velocity when colliding θ Contact angle between the plane and water surface I Impulse suffered by the plane Si,j Certain point on water surface D Distance from emergency to impact location F(D) Cumulative fraction as a function of distance PC(Si,j) Probability of Si,j as the impact location PD(Si,j) Probability of drifters at Si,j PW(Si,j) Probability of wreckage at Si,j PAkD(Si,j) Detecting Probability of drifters at Si,j PAkW(Si,j) Detecting Probability of wreckage at Si,j

<!-- b000192 | prose | pages [10] -->
6

<!-- b000193 | heading | pages [10] -->
Establishing and Solving of Model

<!-- b000194 | prose | pages [10] -->
Since we have formed an overall observation over the search problem, we strive to develop a series of models for a practical rescue plan.

<!-- b000195 | prose | pages [10] -->
6.1

<!-- b000196 | heading | pages [10] -->
Collision Model

<!-- b000197 | prose | pages [10] -->
We recognize that the total amount of drifters produced by the crash have large impact on the search difﬁculty. Hence, we deal with the counting of drifters in this subsection at ﬁrst.

<!-- b000198 | prose | pages [10] -->
Using N0 to represent the maximum amount of drifters resulting from plane crash3, it attributes to aircraft type, passengers onboard, etc. For rational simpli- ﬁcation, it is assumed that the aircraft is full-loaded. Hence, we suppose that N0 increases in direct proportion to the volume of the aircraft V , i.e.

<!-- b000199 | prose | pages [10] -->
N0 = αV (1)

<!-- b000200 | prose | pages [10] -->
3We can determine the accurate number by considering the amount of objects in the aircraft which are capable of ﬂoating in water.

<!-- b000201 | furniture | pages [11] -->
Team # 40612

<!-- b000202 | furniture | pages [11] -->
Page 11 of 34

<!-- b000203 | prose | pages [11] -->
where α is the ratio of N0 to V .

<!-- b000204 | prose | pages [11] -->
Using N to represent the actual amount of drifters resulting from plane crash, N is relevant to N0, ﬂight velocity (v), contact angle (θ), disintegration situations, etc.

<!-- b000205 | prose | pages [11] -->
Disintegration situations are classiﬁed into two categories in our paper: planes break apart in the air and planes collide with the water as a whole, which con- notes that the planes do not break apart until the interaction with water. For the convenience of expression, we name the former category as ’Air Disintegra- tion’, while the latter as ’Water Disintegration’. Then, the above situations are separately discussed about.

<!-- b000206 | prose | pages [11] -->
6.1.1 Air Disintegration

<!-- b000207 | prose | pages [11] -->
Assuming that degree of disintegration4 remains constant to the whole plane and N is in direct proportion to it, we have

<!-- b000208 | prose | pages [11] -->
N = βN0 (2)

<!-- b000209 | prose | pages [11] -->
where β is the degree of disintegration.

<!-- b000210 | prose | pages [11] -->
6.1.2 Water Disintegration

<!-- b000211 | prose | pages [11] -->
Above all, it is noted that β is determined by the impulse suffered by the plane when it crashes into the water.

<!-- b000212 | prose | pages [11] -->
Then, we consider the situation that plane crashes into the water with mass m, ﬂight velocity v and contact angle θ. The diagram of this situation is shown in Figure 1.

<!-- b000213 | prose | pages [11] -->
We have velocity expressions in vertical and horizontal direction as follows:

<!-- b000214 | prose | pages [11] -->
 vx = cos θ

<!-- b000215 | prose | pages [11] -->
(3) vy = sin θ

<!-- b000216 | prose | pages [11] -->
At the moment of collision, the time for vertical velocity reducing to zero is rather small when contrasting with that in horizontal direction. In this sense, the impulse suffered by the aircraft in horizontal direction can be omitted. Hence, we have:

<!-- b000217 | prose | pages [11] -->
I = mvy = mv sin θ (4)

<!-- b000218 | prose | pages [11] -->
where m is the total weight of the plane.

<!-- b000219 | prose | pages [11] -->
4We obtained the available currents date on February 8, 2015.

<!-- b000220 | furniture | pages [12] -->
Team # 40612

<!-- b000221 | furniture | pages [12] -->
Page 12 of 34

<!-- b000222 | caption | pages [12] -->
Figure 1: The Diagram for Water Disintegration

<!-- b000223 | prose | pages [12] -->
Intuitively, we can expect positive correlations between I and β. We provide a further description:

<!-- b000224 | prose | pages [12] -->
• β can be regarded as 0 when I is inadequate.

<!-- b000225 | prose | pages [12] -->
• There is a linear relationship between I and β when I increases to certain level.

<!-- b000226 | prose | pages [12] -->
• β remains to be 1 when I is large enough. In this situation, N equals to N0.

<!-- b000227 | prose | pages [12] -->
Formally, we express the relationship as:

<!-- b000228 | prose | pages [12] -->


<!-- b000229 | prose | pages [12] -->
0

<!-- b000230 | prose | pages [12] -->


<!-- b000231 | prose | pages [12] -->
γ(I −I0)

<!-- b000232 | prose | pages [12] -->
β =

<!-- b000233 | prose | pages [12] -->
1

<!-- b000234 | prose | pages [12] -->


<!-- b000235 | prose | pages [12] -->
I ⩽I0 I0 < I < I0 + 1/γ

<!-- b000236 | prose | pages [12] -->
(5)

<!-- b000237 | prose | pages [12] -->
I ⩾I0 + 1/γ

<!-- b000238 | prose | pages [12] -->
where γ can be obtained from practical data.

<!-- b000239 | prose | pages [12] -->
Consequently, the situation of water disintegration also conforms to (2), i.e.

<!-- b000240 | prose | pages [12] -->
N = βN0

<!-- b000241 | prose | pages [12] -->
6.2 System Module

<!-- b000242 | prose | pages [12] -->
This system is designed to generate real scenarios of the crashed plane, in- cluding debris distribution and their subsequent movements. It is used to mea- sure and correct our search model. In other words, it serves as the exact answer to the locations of the search targets from a dynamic perspective of view.

<!-- b000243 | prose | pages [12] -->
The assumptions are stated in 4.2. A critical point to be restated is that we utilize random motion given by computer, adverting self-consistent calculation.

<!-- b000244 | furniture | pages [13] -->
Team # 40612

<!-- b000245 | furniture | pages [13] -->
Page 13 of 34

<!-- b000246 | prose | pages [13] -->
6.3

<!-- b000247 | heading | pages [13] -->
Overview on Search Model

<!-- b000248 | prose | pages [13] -->
Our search model optimizes search areas, while the allocation of aircrafts is described in an independent allocation model.

<!-- b000249 | prose | pages [13] -->
6.3.1

<!-- b000250 | heading | pages [13] -->
Review on Bayesian Filtering Algorithm

<!-- b000251 | prose | pages [13] -->
The mathematical foundation of our model is rooted in classical Bayesian inference. The Bayesian approach is particularly suitable for combining in a rational manner heterogeneous non-Gaussian sensor observations with other sources of quantitative and qualitative information [6][7].

<!-- b000252 | prose | pages [13] -->
In Bayesian analysis any quantity that is not known is considered a random variable. The state of knowledge about such a random variable is expressed in the form of a probability density function (PDF). Any new information in the form of a probabilistic observation is combined with the prior PDF using the Bayes’ theorem in order to update the state of knowledge and form a new posterior PDF. That PDF forms the quantitative basis on which all inferences, or control decisions are made. [1]

<!-- b000253 | prose | pages [13] -->
In a general search problem, the unknown variable is the target location Si,j. The analysis starts from determining a prior PDF of Si,j, that is, PD(Si,j). The prior PDF incorporates accessible information (e.g. substantial search conse- quences). Detecting report gives the feedback of ’successful’ and ’unsuccessful’, characterized by B. Then, the posterior distribution PD(Si,j|B) can be estab- lished recursively based on observations made from detecting tools.

<!-- b000254 | prose | pages [13] -->
In summary, the recursive estimation is performed with prediction and up- date in sequence.

<!-- b000255 | prose | pages [13] -->
6.3.2 Steps of Search Plan

<!-- b000256 | prose | pages [13] -->
Speciﬁcally, in this search problem provided by MCM, our computation pro- cedure is summarized in the following ﬂowchart, where ’NM’ represents ’nauti- cal mile’).

<!-- b000257 | prose | pages [13] -->
As is illustrated in Figure 2, we can divide the search model into ’water surface search model’ and ’underwater search model’.

<!-- b000258 | furniture | pages [14] -->
Team # 40612

<!-- b000259 | furniture | pages [14] -->
Page 14 of 34

<!-- b000260 | caption | pages [14] -->
Figure 2: Summary of the Probability Distribution Computation

<!-- b000261 | prose | pages [14] -->
6.4

<!-- b000262 | heading | pages [14] -->
Water Surface Search Model

<!-- b000263 | prose | pages [14] -->
6.4.1 Surface Search Prior PDF for Impact Location

<!-- b000264 | prose | pages [14] -->
In this part, we aim to make out the prior PDF for impact location. The PDF comprises of ﬂight dynamics prior and reverse drift prior.

<!-- b000265 | heading | pages [14] -->
6.4.1.1 Flight Dynamics Prior PDF

<!-- b000266 | prose | pages [14] -->
It is as well the combination of two distributions.

<!-- b000267 | prose | pages [14] -->
The ﬁrst distribution is inferred from the aircraft’s last known position (LKP). It is based on purely ﬂight dynamics considerations about the maximum dis- tance the aircraft could have feasibly traveled from the time of its last reported position to the time when a scheduled response from the Aircraft Communica- tions Addressing and Reporting System (ACARS) was not received [3]. Then, we get a circular area. Additionally, we suppose each point with the circle has equivalent probability to serve as the impact location.

<!-- b000268 | prose | pages [14] -->
The foundation of the second distribution is an analysis on the collected data from nine commercial aircraft accidents including loss of control. It is conducted

<!-- b000269 | furniture | pages [15] -->
Team # 40612

<!-- b000270 | furniture | pages [15] -->
Page 15 of 34

<!-- b000271 | prose | pages [15] -->
by the Russian Interstate Aviation Group [8]. Using the data, the cumulative distribution of distance traveled from the beginning of emergency to the impact location is plotted in Figure 3. In addition, we ﬁt the function to be

<!-- b000272 | prose | pages [15] -->
22 F(D) = 1 − (6) D2 + 22

<!-- b000273 | caption | pages [15] -->
Figure 3: Cumulative Distribution of Distance from Beginning of Emergency to

<!-- b000274 | prose | pages [15] -->
Impact Location

<!-- b000275 | prose | pages [15] -->
When constructing the ﬂight dynamic prior, we chose a mixture weighted by 50% for each distribution [3]. The distribution is shown in Figure 4.

<!-- b000276 | caption | pages [15] -->
Figure 4: Flight Dynamics Prior PDF

<!-- b000277 | furniture | pages [16] -->
Team # 40612

<!-- b000278 | furniture | pages [16] -->
Page 16 of 34

<!-- b000279 | heading | pages [16] -->
6.4.1.2 Reverse Drift Prior PDF

<!-- b000280 | prose | pages [16] -->
The reverse drift prior is based on data describing marine geography. Surface currents and winds are the primary factors.

<!-- b000281 | prose | pages [16] -->
We establish our model mainly on the simulation of currents. We utilize data collected from Ocean Surface Current Analyses - Real time (OSCAR) Project Ofﬁce [9]. Accessible data includes mean currents condition (with a minimum period of 5 days) for each longitude and latitude, dating from 15 October, 1992 to 5 February, 20155.

<!-- b000282 | prose | pages [16] -->
To compute reverse drift in certain areas for a certain period of time, we use linear interpolation to process the data.

<!-- b000283 | prose | pages [16] -->
In addition to ﬂoating due to surface current, leeway (drift caused by wind) is accounted for. However, faced with scant data on winds, we are deterred to accomplish theoretical calculations (e.g. those presented in the Drift Group Report [10]). Noting that winds spill over their inﬂuence on currents, we assume that they affect the drifters’ movements through currents.

<!-- b000284 | prose | pages [16] -->
The actual speed of the drifters is given as a quarter of the currents speed. The coefﬁcient 0.25 is chosen in consideration of currents, winds, temperature, etc. In following this approach, the positions of the drifters can be drifted back to the initial crashing moment.

<!-- b000285 | prose | pages [16] -->
Thus, the total reverse probability distribution is the sum of the distributions produced from each position of spotted drifters.

<!-- b000286 | heading | pages [16] -->
6.4.1.3 Surface Search Prior PDF

<!-- b000287 | prose | pages [16] -->
To generate a rational surface search prior PDF, it is critical to carefully weigh the priors above. Our model recognize that the complexity of ocean geography and lack of data contribute to a high uncertainty inherent in the estimates of re- verse drift prior PDF. We can give a further evidence of the difﬁculty in predict- ing the movement with currents, Figure 5 is depicted according to our system simulation. The trajectories of the hypothetical drifters are rather diverging.

<!-- b000288 | prose | pages [16] -->
In light of this uncertainty, we give a comparatively lower weight to esti- mates based on reverse drift.

<!-- b000289 | prose | pages [16] -->
The prior distribution before practical surface search is made to be a mixture of 70% of the ﬂight dynamics prior PDF given in 6.4.1.1 and 30% of the reverse drift prior given in 6.4.1.2 [3]. The result of the calculation is shown in Figure 6.

<!-- b000290 | prose | pages [16] -->
5We obtained the available currents date on 8 February, 2015.

<!-- b000291 | furniture | pages [17] -->
Team # 40612

<!-- b000292 | furniture | pages [17] -->
Page 17 of 34

<!-- b000293 | caption | pages [17] -->
Figure 5: Imagined Trajectories in System Simulation in Two Days

<!-- b000294 | caption | pages [17] -->
Figure 6: Surface Search Prior PDF for Impact Location

<!-- b000295 | furniture | pages [18] -->
Team # 40612

<!-- b000296 | furniture | pages [18] -->
Page 18 of 34

<!-- b000297 | prose | pages [18] -->
6.4.2 Surface Search Posterior PDF for Impact Location

<!-- b000298 | prose | pages [18] -->
After the release of the prior PDF given in 6.4.1, authorities are scheduled to assign and allocate aircraft to accomplish the ﬁrst search phase. The substantial efforts provide information of the targets’ location. In this part, we will calculate the posterior PDF in the surface search period through the application of Bayes’ rule.

<!-- b000299 | prose | pages [18] -->
We have mentioned in 6.1 that the crash generates N drifters. Cells are di- vided in the search area with equal size.

<!-- b000300 | prose | pages [18] -->
According to the prior PDF, PD(Si,j) gives the probability that certain drifters are located in the search cell Si,j. Detecting report gives the feedback of ’success- ful’ and ’unsuccessful’, characterized by B. Here, we assumed that there are at most one drifter inside a cell. PAkD(Si,j) gives the probability that the object would have be detected by search aircraft Ak if it is located there.

<!-- b000301 | prose | pages [18] -->
Then, we compute the posterior probability PD(Si,j|B):

<!-- b000302 | prose | pages [18] -->
P(B|Si,j)PD(Si,j) PD(Si,j|B) =

<!-- b000303 | prose | pages [18] -->
(7)

<!-- b000304 | prose | pages [18] -->
P

<!-- b000305 | prose | pages [18] -->
P(B|Sm,n)PD(Sm,n)

<!-- b000306 | prose | pages [18] -->
Sm,n∈S

<!-- b000307 | prose | pages [18] -->
where S is the whole search area in contemporary search phase.

<!-- b000308 | prose | pages [18] -->
A posterior PDF for the impact point is calculated in this fashion and the result is depicted in Figure 7.

<!-- b000309 | caption | pages [18] -->
Figure 7: Surface Search Posterior PDF for Impact Location

<!-- b000310 | furniture | pages [19] -->
Team # 40612

<!-- b000311 | furniture | pages [19] -->
Page 19 of 34

<!-- b000312 | prose | pages [19] -->
6.5

<!-- b000313 | heading | pages [19] -->
Underwater Search Model

<!-- b000314 | prose | pages [19] -->
Underwater search acts as the most valuable portion in the whole plan be- cause it directly targets at the aircraft wreckage. Based on Bayes’ theorem, the model turns to be a recursion, ended by the spot of wreckage.

<!-- b000315 | prose | pages [19] -->
6.5.1 Underwater Search Prior PDF for Impact Location

<!-- b000316 | prose | pages [19] -->
We form the underwater search prior through a mixture of 30% of the surface search posterior in Figure 7 and 70% of the ﬂight dynamics prior in Figure 3 according to the Final Report. The surface search posterior is allocated a lower weight accounting for the uncertainty of currents. The PDF is plotted in Figure 8.

<!-- b000317 | prose | pages [19] -->
6.5.2 Phase I Searches

<!-- b000318 | prose | pages [19] -->
In this phase of search, underwater detections are performed in accordance to the prior PDF in 6.5.1. Moreover, we assume that water surface searches are not conducted any more. It is because the uncertainty caused by ocean geogra- phy is rather high and the location estimate will grow even more uncertain as time goes by.

<!-- b000319 | prose | pages [19] -->
It is expected that the aircraft wreckage can be localized in the ﬁrst triage of underwater search. However, this strong expectation may not hold in reality. In this sense, we go on to compute posterior after phase I.

<!-- b000320 | prose | pages [19] -->
6.5.3 Underwater Search Posterior PDF after Phase I

<!-- b000321 | prose | pages [19] -->
PC(Si,j) is the probability Si,j is the impact location. Analogous to surface water search posterior PDF, we just replace PD(Si,j), PAkD(Si,j) with PW(Si,j), PAkW(Si,j) in (7).

<!-- b000322 | prose | pages [19] -->
The posterior PDF is plotted in Figure 9.

<!-- b000323 | prose | pages [19] -->
6.5.4 Recursion

<!-- b000324 | prose | pages [19] -->
Then, the PDF in 6.5.3 function as the prior PDF for Phase II searches. If the search ends up unsuccessful, posterior PDF after Phase II is required. The recur- sion continues until the wreckage is pinpointed or the procedure is suspended intentionally.

<!-- b000325 | furniture | pages [20] -->
Team # 40612

<!-- b000326 | furniture | pages [20] -->
Page 20 of 34

<!-- b000327 | caption | pages [20] -->
Figure 8: Underwater Search Prior PDF for Impact Location

<!-- b000328 | caption | pages [20] -->
Figure 9: Underwater Search Posterior PDF for Impact Location

<!-- b000329 | furniture | pages [21] -->
Team # 40612

<!-- b000330 | furniture | pages [21] -->
Page 21 of 34

<!-- b000331 | prose | pages [21] -->
7

<!-- b000332 | heading | pages [21] -->
Allocation Model

<!-- b000333 | prose | pages [21] -->
Taking all data available as well as associated uncertainties into considera- tion, we have formed an analytic prediction of the debris distribution for next increment of search effort. Then, we are scheduled to deal with the allocation of search forces in this subsection.

<!-- b000334 | prose | pages [21] -->
On the foundation of Quicksort algorithm and branch-and-bound algorithm, our goal is to develop a method matching search planes with search cells.

<!-- b000335 | prose | pages [21] -->
7.1

<!-- b000336 | heading | pages [21] -->
Review on Algorithms

<!-- b000337 | prose | pages [21] -->
Quicksort is a sorting algorithm with the time complexity of O(n lg n). It is an efﬁcient divide and conquer algorithm, rearranging an array in ascending or descending order by recursive partition.

<!-- b000338 | prose | pages [21] -->
Branch-and-bound algorithm is a widely used algorithm for solving large scale NP-hard combinatorial optimization problems [14]. For a maximization problem, the key idea of the branch-and-bound algorithm is:

<!-- b000339 | prose | pages [21] -->
• The maximum lower bound seen among all candidates examined so far are recorded.

<!-- b000340 | prose | pages [21] -->
• If the upper bound for certain set of candidates (A) is smaller than the upper bound for some other set (B), then A may be safely discarded from the search.

<!-- b000341 | prose | pages [21] -->
• The recursion stops when the current candidate set S increases to a single element, or when the upper bound for set S matches the lower bound. Either way, any element of S will be a maximum of the function within S. [15]

<!-- b000342 | prose | pages [21] -->
7.2 Allocation of Search Planes

<!-- b000343 | prose | pages [21] -->
We implement the task of allocating planes to certain search cells with the following steps:

<!-- b000344 | prose | pages [21] -->
• Match planes with search areas. Rank the search areas based on updated PDF applying the Quicksort Algorithm in descending order. Meanwhile, rank the available search aircrafts based on their search capability also in descending order. Thus, search cells with larger PDFs will be allocated to better with a higher priority, which helps us to ﬁnd a better solution earlier, instead of wasting time on inferior ones.

<!-- b000345 | furniture | pages [22] -->
Team # 40612

<!-- b000346 | furniture | pages [22] -->
Page 22 of 34

<!-- b000347 | prose | pages [22] -->
• Optimize the allocating plan. Compute the cumulative probability of de- tection which is the sum of probabilities at each point and make it the objective function. Apply the branch-and-bound algorithm to fulﬁll the maximization task.

<!-- b000348 | prose | pages [22] -->
Take the water surface search as an example. The accessible search aircrafts are generally classiﬁed as of better detection capability and of minor detection capability. Figure 10 is depicted to show the allocation plan. (In the upper left corner, the larger rectangle accords with the better planes.)

<!-- b000349 | caption | pages [22] -->
Figure 10: Allocation Plan of the Search Aircrafts

<!-- b000350 | prose | pages [22] -->
8

<!-- b000351 | heading | pages [22] -->
Applying of Model

<!-- b000352 | prose | pages [22] -->
As is described before, the previous model is concerned about the entire pro- cess of searching for a disappeared plane. In the former part of this section, we apply our model to the case of AF447, evaluating and analyzing the per- formance. Then, we propose a possible search plan for the further detection of MH370 on the basis of our model and accessible data.

<!-- b000353 | prose | pages [22] -->
8.1 Application on AF447

<!-- b000354 | prose | pages [22] -->
As is described before, the previous model is concerned about the entire pro- cess of searching for a disappeared plane. In the former part of this section,

<!-- b000355 | furniture | pages [23] -->
Team # 40612

<!-- b000356 | furniture | pages [23] -->
Page 23 of 34

<!-- b000357 | prose | pages [23] -->
we apply our model to the case of AF447, evaluating and analyzing the per- formance. Then, we propose a possible search plan for the further detection of MH370 on the basis of our model and accessible data.

<!-- b000358 | prose | pages [23] -->
8.1.1 Available Information

<!-- b000359 | prose | pages [23] -->
The rescue work began on June 1, 2009. However, the aeroplane wreckage was ﬁnally localized on April 2, 2011. It was found about 6.5 NM from the last known position, at a depth of 3,900 meters, slightly to the left of the planned route [16].

<!-- b000360 | prose | pages [23] -->
The position, date and recovery time data can be referenced in the Final Re- port by BEA [16]. In light of the uncertainty caused by ocean geography (as is stated in 6.4.1.3), the location estimate will grow even more uncertain as time goes by. Hence, we employ the data gathered from the initial search phase.

<!-- b000361 | prose | pages [23] -->
8.1.2 Computation Process

<!-- b000362 | prose | pages [23] -->
The process conforms to the procedure in Figure 1.

<!-- b000363 | prose | pages [23] -->
Flight Dynamics Prior has been worked out in 6.4.1.1. The distribution of the drifters obtained from Table 3 can be assumed as surface search posterior PDF. Then, we form the underwater search prior through a mixture of 70% of the ﬂight dynamics prior and 30% of the surface search posterior, as it is in 6.5.1.

<!-- b000364 | prose | pages [23] -->
8.1.3

<!-- b000365 | heading | pages [23] -->
Computation Result

<!-- b000366 | prose | pages [23] -->
The underwater search prior PDF for the case of AF447 is shown in Figure 11. The point with the highest probability is selected as the ’predicted’ impact location. In addition, the exact impact location is pointed out by the spot in the ﬁgure for comparison.

<!-- b000367 | prose | pages [23] -->
We can observe from the ﬁgure that the impact location is located in our suggestive area.

<!-- b000368 | furniture | pages [24] -->
Team # 40612

<!-- b000369 | furniture | pages [24] -->
Page 24 of 34

<!-- b000370 | caption | pages [24] -->
Figure 11: Underwater Search Prior PDF for AF447

<!-- b000371 | prose | pages [24] -->
8.2 Prediction on MH370

<!-- b000372 | prose | pages [24] -->
8.2.1

<!-- b000373 | heading | pages [24] -->
Review on Established Models

<!-- b000374 | prose | pages [24] -->
The ﬁrst difﬁculty in the MH370 search problem is that the last known po- sition (LKP) cannot be absolutely determined. Hence, it could not enter the process in Figure 1.

<!-- b000375 | prose | pages [24] -->
A diversity of models have been established by experts to determine the ﬂight path of MH370. However, their prediction outcomes prove to be quite diverging. Moreover, the robustness is poor.

<!-- b000376 | prose | pages [24] -->
The models are based on data from radar and satellite. Radar data suggests that the ﬂight path of MH370 was rather erratic. Satellite data presents seven records on the position of MH370. Considering the principles of how the dis- tance of the aeroplane from the satellite is established, the measuring results are actually seven circles on Earth surface.

<!-- b000377 | prose | pages [24] -->
With the uncertainty of ﬂight path, search areas are experiencing violent changes. Besides, each suggestive plan tends to cover a vast area. As is shown in Figure 12 [17], different models proposed on different dates gives different search areas while each search covers a considerably large arching area.

<!-- b000378 | furniture | pages [25] -->
Team # 40612

<!-- b000379 | furniture | pages [25] -->
Page 25 of 34

<!-- b000380 | caption | pages [25] -->
Figure 12: The Search for MH370

<!-- b000381 | prose | pages [25] -->
A critical question is to be raised: why are the search areas changing? In- depth analyses are performed on these models and we suppose the reasons to be:

<!-- b000382 | prose | pages [25] -->
• Besides of ping arc data, burst frequency offset (BFO) must be considered.

<!-- b000383 | prose | pages [25] -->
• Data are excessively analyzed with sophisticated methods.

<!-- b000384 | prose | pages [25] -->
• The scopes of application are restricted by the advanced models and algo- rithms.

<!-- b000385 | furniture | pages [26] -->
Team # 40612

<!-- b000386 | furniture | pages [26] -->
Page 26 of 34

<!-- b000387 | prose | pages [26] -->
8.2.2 Probability Distribution

<!-- b000388 | prose | pages [26] -->
In this part, we present a probability distribution based on constrained au- topilot dynamics and data error optimization. The representation is shown in

<!-- b000389 | caption | pages [26] -->
Figure 13.

<!-- b000390 | caption | pages [26] -->
Figure 13: Representation of Probability Distribution

<!-- b000391 | prose | pages [26] -->
The above ﬁgure concerns about 0011 arc for constrained data error opti- mization (green) and autopilot dynamics (red), which are more probable. Area of interest on 0019 arc covers 80% of probable paths from the two analyses at 0011 and consideration of the MRC approximate southern boundary. [18]

<!-- b000392 | prose | pages [26] -->
This analysis indicates that the total probability areas overlap between ap- proximately 35 ◦S and 39 ◦S at 0011. The 6th arc between latitudes 32.5 ◦S and 38.1 ◦S covers 80% of the highest probability paths for both analyses. Extrapo- lating paths and limiting the southern boundary by the MRC intersection with the 7th arc provides an area between approximately 33.5 ◦S and 38.3 ◦S at 0019 (7th arc). [19]

<!-- b000393 | prose | pages [26] -->
8.2.3 Computation Process

<!-- b000394 | prose | pages [26] -->
To get access to the procedure described in Figure 1, we identify our ﬂight dynamics prior PDF to be the probability distribution depicted in Figure 13. It is worth noting that these two distributions have common foundations to some extent.

<!-- b000395 | prose | pages [26] -->
With a paucity of data from substantial searches, we assume that search planes have no detection during the phase of surface search and underwater search. Thus, analogous to the steps in the preceding part this paper, we can get the prior PDF for underwater search. The PDF for each search is shown in

<!-- b000396 | caption | pages [26] -->
Figure 14.

<!-- b000397 | furniture | pages [27] -->
Team # 40612

<!-- b000398 | furniture | pages [27] -->
Page 27 of 34

<!-- b000399 | prose | pages [27] -->
(a)Water Surface Search Prior PDF (b)Water Surface Search Posterior PDF

<!-- b000400 | caption | pages [27] -->
Figure 14: PDFs for MH370

<!-- b000401 | prose | pages [27] -->
(c)Underwater Search Prior PDF (d)Underwater Search Posterior PDF

<!-- b000402 | prose | pages [27] -->
9

<!-- b000403 | heading | pages [27] -->
Sensitivity Analysis

<!-- b000404 | prose | pages [27] -->
In this section, we implement the sensitivity test for our models. Noting that the model is mostly dependent on the planes we are searching and the search planes accessible, we conduct three tests separately on the number of drifters (N), the total number of search planes, the types of search planes and the weights given to each prior.

<!-- b000405 | prose | pages [27] -->
The standard utilized to measure the robustness of our model is the probabil- ity that the aircraft wreckage can be localized (cumulative probability P PAkW(Si,j)).

<!-- b000406 | prose | pages [27] -->
9.1 The Number of Drifters

<!-- b000407 | prose | pages [27] -->
The actual number of drifters (N) is directly relevant to the planes we are searching. We default N for three different numbers and list the value of P PAkW(Si,j) in Table 3.

<!-- b000408 | furniture | pages [28] -->
Team # 40612

<!-- b000409 | furniture | pages [28] -->
Page 28 of 34

<!-- b000410 | caption | pages [28] -->
Table 3: Sensitivity Tests on the Number of Drifters

<!-- b000411 | prose | pages [28] -->
P PAkW(Si,j) N

<!-- b000412 | prose | pages [28] -->
200 100 50 0.619 0.583 0.545

<!-- b000413 | prose | pages [28] -->
The Number of Search Planes 9.2

<!-- b000414 | prose | pages [28] -->
We give an increasing amount of search planes while supposing that they are of the same search capability. The corresponding parameters are assigned as: N = 200, limit of search areas are 10 cells (the area of per cell equals to 3.244NM 2, i.e. 11.128km2), PAkD(Si,j) = 0.8, PAkW(Si,j) = 0.4

<!-- b000415 | prose | pages [28] -->
Then the value of P PAkW(Si,j) is presented in Table 4.

<!-- b000416 | caption | pages [28] -->
Table 4: Sensitivity Tests on the Number of Search Planes

<!-- b000417 | prose | pages [28] -->
P PAkW(Si,j) Number of Search Planes

<!-- b000418 | prose | pages [28] -->
2 3 4

<!-- b000419 | prose | pages [28] -->
9.3 The Types of Search Planes

<!-- b000420 | prose | pages [28] -->
0.340 0.354 0.368

<!-- b000421 | prose | pages [28] -->
We assign different properties concerning on the capabilities of search planes. Nine sorts of aircrafts are tested and enumerated. The detailed setting is pre- sented in Table 5.

<!-- b000422 | prose | pages [28] -->
As we dispatch two planes to conduct a phase of search task, we give some combinations of different planes to test our model. Accordingly, the value of P PAkW(Si,j) is listed in Table 6.

<!-- b000423 | prose | pages [28] -->
We can observe from Table 3, Table 4 and Table 6 that with more drifters and more advanced search planes, the wreckage of the crashed plane tends to be pinpointed easier. Hence, the result of this experiment is consistent with our intuition.

<!-- b000424 | furniture | pages [29] -->
Team # 40612

<!-- b000425 | furniture | pages [29] -->
Page 29 of 34

<!-- b000426 | caption | pages [29] -->
Table 5: Types of Search Planes according to Search Capabilities

<!-- b000427 | prose | pages [29] -->
PAkD(Si,j) PAkW(Si,j) Limit of Search Area in cells Serial Number

<!-- b000428 | prose | pages [29] -->
1 4 2 4 3 4 4 8 5 8 6 8 7 8 8 3 9 4 0.9 0.8 0.75 0.8 0.9 0.6 0.7 0.5 0.55 0.5 0.7 0.3 0.9 0.8 0.7 0.5 0.7 0.5

<!-- b000429 | caption | pages [29] -->
Table 6: Sensitivity Tests on the Types of Search Planes

<!-- b000430 | prose | pages [29] -->
P PAkW(Si,j) The Combinations of Types

<!-- b000431 | prose | pages [29] -->
1 4 2 4 3 4 1 5 1 6 7 4 1 8 7 9 7 9 0.517 0.501 0.434 0.517 0.442 0.554 0.486 0.531 0.531

<!-- b000432 | prose | pages [29] -->
Weights in Computing Flight Dynamics PDF 9.4

<!-- b000433 | prose | pages [29] -->
In the previous part in this paper, we chose a mixture weighted by 50% for both the distribution based on LKP and the cumulative distribution of distance when constructing the ﬂight dynamic prior. Here, we perform a test on the weights allocated for each distribution.

<!-- b000434 | prose | pages [29] -->
The value of P PAkW(Si,j) is listed in Table 7.

<!-- b000435 | caption | pages [29] -->
Table 7: Sensitivity Tests on the Weights in Computing Flight Dynamics PDF

<!-- b000436 | prose | pages [29] -->
P PAkW(Si,j) Cumulative Distribution of Distance Distribution based on LKP

<!-- b000437 | prose | pages [29] -->
30% 50% 70% 70% 0.520 50% 0.516 30% 0.508

<!-- b000438 | furniture | pages [30] -->
Team # 40612

<!-- b000439 | furniture | pages [30] -->
Page 30 of 34

<!-- b000440 | prose | pages [30] -->
Weights in Computing Surface Search Prior PDF 9.5

<!-- b000441 | prose | pages [30] -->
The prior distribution before practical surface search is made to be a mixture of 70% of the ﬂight dynamics prior PDF and 30% of the reverse drift prior in 6.4.1. In this portion, we change the weights allocated, and calculate P PAkW(Si,j).

<!-- b000442 | prose | pages [30] -->
The calculation results are shown in Table 8.

<!-- b000443 | caption | pages [30] -->
Table 8: Sensitivity Tests on the Weights in Computing Surface Search Prior PDF

<!-- b000444 | prose | pages [30] -->
P PAkW(Si,j) Reverse Drift Prior Flight Dynamics Prior

<!-- b000445 | prose | pages [30] -->
70% 50% 30% 30% 0.518 50% 0.518 70% 0.520

<!-- b000446 | prose | pages [30] -->
Weights in Computing Underwater Search Prior PDF 9.6

<!-- b000447 | prose | pages [30] -->
In 6.5.1, we form the underwater search prior through a mixture of 30% of the surface search posterior and 70% of the ﬂight dynamics prior. Then, we will test the sensitivity of our model on the weight allocation.

<!-- b000448 | prose | pages [30] -->
The results are shown in Table 9.

<!-- b000449 | caption | pages [30] -->
Table 9: Sensitivity Tests on the Weights in Computing Underwater Search Prior

<!-- b000450 | prose | pages [30] -->
PDF

<!-- b000451 | prose | pages [30] -->
P PAkW(Si,j) Flight Dynamics Prior Surface Search Posterior

<!-- b000452 | prose | pages [30] -->
30% 50% 70% 70% 0.516 50% 0.518 30% 0.519

<!-- b000453 | prose | pages [30] -->
From Table 7, 8, and 9, we can conclude that our model is insensitive to the weights allocated to each prior. It is an appreciated conclusion that our model has good ﬂexibility and reliability.

<!-- b000454 | prose | pages [30] -->
To sum, a series of experiments have been implemented to verify the credi- bility and universality of our model.

<!-- b000455 | furniture | pages [31] -->
Team # 40612

<!-- b000456 | furniture | pages [31] -->
Page 31 of 34

<!-- b000457 | prose | pages [31] -->
10

<!-- b000458 | heading | pages [31] -->
Strengths and Weaknesses

<!-- b000459 | prose | pages [31] -->
10.1

<!-- b000460 | heading | pages [31] -->
Strengths

<!-- b000461 | prose | pages [31] -->
• Accuracy. Our model can precisely predict the location of AF447 in a single underwater search. Comparing with the practical three phases of search, our model prove to be much more precise.

<!-- b000462 | prose | pages [31] -->
• Efﬁciency. Besides of accuracy, our model deals with the problem in a relatively shorter period of time.

<!-- b000463 | prose | pages [31] -->
• Application Value. As the model is prepared for actual rescue, we have to incorporate time and expense. With shorter decision time and less sub- stantial searches, our model is of comparably higher practical value.

<!-- b000464 | prose | pages [31] -->
• Robustness. It is shown in section 8 that the weights set in prior have little impact on the model. Hence, we need not worry about the divergence of the results with different parameters.

<!-- b000465 | prose | pages [31] -->
10.2

<!-- b000466 | heading | pages [31] -->
Weaknesses

<!-- b000467 | prose | pages [31] -->
• Computational complexity. If we default smaller area to a search cell or dispatch more search planes, the computation may beyond the ability of our computers.

<!-- b000468 | heading | pages [31] -->
• Unrealistic assumptions. Some of our measures are based on unrealistic

<!-- b000469 | prose | pages [31] -->
foundations, e.g. we do not distinguish drifters, however, in reality, bodies are used more to assist search.

<!-- b000470 | prose | pages [31] -->
• Parameters. Some of our parameters are hard to determine such as the search ability. Moreover, the default of a few parameters is not in accor- dance with real conditions. For example, we will not just have two planes to complete the search.

<!-- b000471 | furniture | pages [32] -->
Team # 40612

<!-- b000472 | furniture | pages [32] -->
Page 32 of 34

<!-- b000473 | prose | pages [32] -->
11 Non-technical Paper for Press Conference

<!-- b000474 | prose | pages [32] -->
March 8, 2014 has become one of the darkest days in aviation history due to the missing of Malaysia Airlines Flight 370 (MH370). Approaching its anniver- sary, the mystery is still stretching, so is the grief. It is always sad to think about aircraft accidents. However, we should nerve ourselves to face the tragedies and ponder how to avert future aviation disappearing acts.

<!-- b000475 | prose | pages [32] -->
For a speciﬁc marine search problem, we have learnt sobering lessons from past accidents. Above all, scant knowledge of ocean geography often stymies efforts to conduct the search, especially for certain water areas. In the case of MH370, the largely uncharted bathymetry of the southern Indian Ocean’s sea ﬂoor hampers the rescue. Hence, the primary task is to perform in-depth analy- ses on the natural conditions of targeted areas. Currents and leeway should be focused on.

<!-- b000476 | prose | pages [32] -->
Contemporarily, a few coastal ocean models have been developed, such as Global Navy Coastal Ocean Model (G-NCOM), HYbrid Coordinate Ocean Model (HYCOM) and Finite Volume Coastal Ocean Model (FVCOM). They have proved their advantages in certain cases. However, to obtain a more generic model, we base our model on precise data of currents incorporating various impact factors. It is proved to be quite precise in our veriﬁcation process.

<!-- b000477 | prose | pages [32] -->
It is well worth noting that the location estimate will grow even more uncer- tain as time goes by. This leads to our resolution that the response and dispatch to the accidents should be acted in a timely fashion. On one hand the real-time track of the planes should function well and emergency plans should be care- fully prepared. On the other hand, the search plan should be as efﬁcient as possible.

<!-- b000478 | prose | pages [32] -->
Our modiﬁed search and rescue plan comprises of two parts: search plan and allocation plan. The former one targets at the optimization of search areas while the latter demonstrates the most proper allocation of search planes.

<!-- b000479 | prose | pages [32] -->
Our search plan is an application of the Bayesian decentralized data fusion algorithm which deals with tracking problems. The primary period of it is to conduct water surface search, that is, to detect bodies and aircraft debris. The search areas are determined by combining accessible ﬂight velocity information at the last minutes and prediction made in accordance to past accidents. Our planes will rocket to the destination. It is a sorrowful task while it contributes a lot to the whole search. We can obtain possibility distribution from the position data of those drifters, which assists to work out the initial predicting position of the aircraft wreckage.

<!-- b000480 | prose | pages [32] -->
Then it comes to the period of underwater search. We dispatch aircrafts to probe the wreckage of the crashed plane which usually lies on the deep seaﬂoor.

<!-- b000481 | furniture | pages [33] -->
Team # 40612

<!-- b000482 | furniture | pages [33] -->
Page 33 of 34

<!-- b000483 | prose | pages [33] -->
We have a dream that the wreckage can be localized at the ﬁrst phase of search. However, if unfortunately, this strong expectation do not hold true in reality, we will correct and update our search project for further detection attempts.

<!-- b000484 | prose | pages [33] -->
Our allocation plan aims to match the most advanced search planes to those areas with the largest probabilities. We are grateful that we can get aid from other countries to conduct the rescue. Actually, the difﬁculties of search vary with different types of planes we are searching for. However, accessible to a diversity of search aircrafts equipped with various electronics and sensors, we can do the search with greater efﬁciency and accuracy.

<!-- b000485 | prose | pages [33] -->
Despite the fact that there are some assumptions and simpliﬁcations em- ployed in the process of designing the plan, we have conﬁdence on our plan. It is because we have verify it in the case of Air France Flight 447 ((AF447). It is known to the public that the ﬂight disappeared on its way from Bio de Janeiro to Paris on June 1, 2009. It was not until April 2, 2011 when it was ﬁnally lo- calized. Three phases of underwater search had been performed before the last successful assignment. It is really a long and painful time for both the relatives to the victims and the authorities. Nonetheless, using our modiﬁed plan, we could have achieved the ultimate goal in merely one search. In this sense, we have to apologize for our plan coming late.

<!-- b000486 | prose | pages [33] -->
We are dedicated to accomplish the search task as speedily as possible. Maybe this is the best way to rescue the survivors as well as to offer our guilty and con- dolence to those grieving relatives. No matter how the reality may upset us, we have the resolution to ﬁght to the last. Only when the wreckage is pinpointed will we terminate our search efforts.

<!-- b000487 | prose | pages [33] -->
We must express our thanks for your past trust on our airlines. Our sorrow and guilty for the tragedy is beyond expressions. In addition to rescue plan, we will attach importance and devote resources to reﬁne our preventive measures. It is our sincere hope that our search and rescue plan will never be put into practice as there no longer to be such tragedies.

<!-- b000488 | heading | pages [33] -->
References

<!-- b000489 | references | pages [33] -->
[1] Normile D. Lost at sea[J]. Science, 2014, 344(6187): 963-965.

<!-- b000490 | references | pages [33] -->
[2] et d’Analyses B E. Final report on the accident on 1st June 2009 to the Airbus

<!-- b000491 | references | pages [33] -->
A330-203 registered F-GZCP operated by Air France ﬂight AF 447 Rio de

<!-- b000492 | references | pages [33] -->
Janeiro-Paris[J]. Ministere de l’Ecologie. du Developpement durable, des

<!-- b000493 | references | pages [33] -->
Transports et du Logement, Paris, 2012.

<!-- b000494 | references | pages [33] -->
[3] Stone L D, Keller C, Kratzke T M, et al. Search analysis for the location of

<!-- b000495 | references | pages [33] -->
the AF447 underwater wreckage[J]. METRON, report to BEA, 2011.

<!-- b000496 | furniture | pages [34] -->
Team # 40612

<!-- b000497 | furniture | pages [34] -->
Page 34 of 34

<!-- b000498 | references | pages [34] -->
[4] http://www.baike.com/wiki/MH370+%E8%88%AA%E7%8F%AD

<!-- b000499 | references | pages [34] -->
[5] Bourgault F, Furukawa T, Durrant-Whyte H F. Coordinated decentralized

<!-- b000500 | references | pages [34] -->
search for a lost target in a Bayesian world[C]//Intelligent Robots and Sys-

<!-- b000501 | references | pages [34] -->
tems, 2003.(IROS 2003). Proceedings. 2003 IEEE/RSJ International Confer-

<!-- b000502 | references | pages [34] -->
ence on. IEEE, 2003, 1: 48-53.

<!-- b000503 | references | pages [34] -->
[6] Stone L D, Streit R L, Corwin T L, et al. Bayesian multiple target track-

<!-- b000504 | references | pages [34] -->
ing[M]. Artech House, 2013.

<!-- b000505 | references | pages [34] -->
[7] Statistical decision theory and Bayesian analysis[M]. Springer Science &

<!-- b000506 | references | pages [34] -->
Business Media, 1985.

<!-- b000507 | references | pages [34] -->
[8] Presentation MAK AF447 Brieﬁng, Russian Interstate Aviation Group, 16

<!-- b000508 | references | pages [34] -->
October 2009.

<!-- b000509 | references | pages [34] -->
[9] Data Download for Ocean Surface Currents.

<!-- b000510 | references | pages [34] -->
[10] Ollitrault M, Blanke B, Chen C, et al. Estimating the wreckage location of

<!-- b000511 | references | pages [34] -->
the Rio-Paris AF447[J]. 2010.

<!-- b000512 | references | pages [34] -->
[11] Quicksort. Wikipedia. http://en.wikipedia.org/wiki/Quicksort 8.

<!-- b000513 | references | pages [34] -->
[12] Sedgewick R. Implementing quicksort programs[J]. Communications of the

<!-- b000514 | references | pages [34] -->
ACM, 1978, 21(10): 847-857.

<!-- b000515 | references | pages [34] -->
[13] Skiena S S. The algorithm design manual: Text[M]. Springer Science & Busi-

<!-- b000516 | references | pages [34] -->
ness Media, 1998.

<!-- b000517 | references | pages [34] -->
[14] Clausen J. Branch and bound algorithms-principles and examples[J]. De-

<!-- b000518 | references | pages [34] -->
partment of Computer Science, University of Copenhagen, 1999: 1-30.

<!-- b000519 | references | pages [34] -->
[15] Branch-and-Bounds. Wikipedia. http://en.wikipedia.org/wiki/Branch and bound

<!-- b000520 | references | pages [34] -->
February 2015.

<!-- b000521 | references | pages [34] -->
[16] et d’Analyses B E. Final report on the accident on 1st June 2009 to the Airbus

<!-- b000522 | references | pages [34] -->
A330-203 registered F-GZCP operated by Air France ﬂight AF 447 Rio de

<!-- b000523 | references | pages [34] -->
Janeiro-Paris[J]. Ministere de l’Ecologie. du Developpement durable, des

<!-- b000524 | references | pages [34] -->
Transports et du Logement, Paris, 2012.

<!-- b000525 | references | pages [34] -->
[17] Malaysia Airlines Flight 370. http://en.wikipedia.org/wiki/Malaysia Airlines Flight 370.

<!-- b000526 | references | pages [34] -->
[18] Google Earth/ Flight path reconstruction group

<!-- b000527 | references | pages [34] -->
[19] Australian Transport Safety Bureau. 8 October 2014. Retrieved 15 Novem-

<!-- b000528 | references | pages [34] -->
ber 2014.
