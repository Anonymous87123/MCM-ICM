# P-B-2024-2425792-696128a0

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

<!-- b000006 | furniture | pages [1] -->
2425792

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Save the Submersible: An Combined Method

<!-- b000009 | title | pages [1] -->
of Computational Fluid Dynamics and Kalman

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | title | pages [1] -->
Filter

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
Exploration of shipwrecks on the seabed by submersibles represents a blue ocean for tourism development. Yet presently there’s an absence of procedures to ensure the safekeeping of sub- mersibles in case of an incident. In an effort to bridge the gap, our team construct the following model to realize more accurate localization and prompt search.

<!-- b000014 | prose | pages [1] -->
First, to locate. We collected data of ocean currents, seawater density, and seafloor geography which are the main uncertainties affecting the submersible’s motion. Then, we established the

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
Computational Fluid Dynamics equation via simplified Fossen’s Six Degrees of Freedom model. With the prerequisites of Kalman Filter all met, we can safely adopt the computationally efficient Kalman Filtering. Utilizing the ”update-predict” recursive mechanism embedded in Kalman filtering, inaccuracies engendered by cumulative errors are mitigated, thereby realizing the trajectory correction. Moreover, upon calculation of the submersible’s probability distribution in space, we found the trajectory that the defective submersible would most likely to follow.

<!-- b000017 | prose | pages [1] -->
Then, to prepare. To enhance rescue efficiency, we assembled data of rescue equipment available on the market and their corresponding parameters. Predicated upon 14 indicators, we used the Principle Component Analysis to construct and selected the three primary components with the highest contribution rate. This analysis thus afforded a composite score for each item of equipment, thereby determining three devices for the host ship and three for the rescue vessels.

<!-- b000018 | prose | pages [1] -->
Next, to search. We employed further the predicted estimate covariance matrix from the Kalman filter results. Combined with the probability density function of a multivariate normal distribution, a standard statistical 95% confidence 3D Space is computed and then interpreted as the feasible zone for search. As discussed in the previous section, we deploy multi-beam sonar, combined bathymetry and side scan sonar on the host ship for an Along-Isobath Search.

<!-- b000019 | prose | pages [1] -->
Furthermore, to extrapolate. We’ve done 2 extrapolations to the model. For one thing, we examined our model in different ocean environments. The validation of employing our model for location prediction is thus established. For another, on superimposing the concept of the Voronoi Diagram, we derived a model to assure that multiple submersibles cooperate without collisions, and effectuate the most rapid monitoring of the defective submersible in an incident.

<!-- b000020 | prose | pages [1] -->
Finally, in our sensitivity and error analysis, we found that seawater density and external environmental disturbances significantly impact submersible path prediction accuracy, with high sensitivity and larger prediction errors (RMSE values 1.55 m and 2.10 m, respectively). Pro- peller rotation speed and submersible mass showed lower impacts on model accuracy, with lower sensitivity(RMSE values 1.12 m and 1.17 m, respectively).

<!-- b000021 | keywords | pages [1] -->
Keywords: Kalman Filter

<!-- b000022 | prose | pages [1] -->
Inertial Navigation Computational Fluid Dynamics Principle Components Analysis Voronoi Diagram

<!-- b000023 | prose | pages [1] -->
关注数学模型

<!-- b000024 | furniture | pages [1] -->
2

<!-- b000025 | furniture | pages [1] -->
MATHmodels

<!-- b000026 | furniture | pages [1] -->
获取更多资讯

<!-- b000027 | furniture | pages [2] -->
Team 2425792

<!-- b000028 | furniture | pages [2] -->
Page 1 of 24

<!-- b000029 | heading | pages [2] -->
Contents

<!-- b000030 | contents | pages [2] -->
1 Introduction

<!-- b000031 | contents | pages [2] -->
2

<!-- b000032 | contents | pages [2] -->
1.1

<!-- b000033 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
2

<!-- b000035 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000036 | contents | pages [2] -->
1.2

<!-- b000037 | contents | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
3

<!-- b000039 | contents | pages [2] -->
1.3

<!-- b000040 | contents | pages [2] -->
Our Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
2 Model Preparation

<!-- b000043 | contents | pages [2] -->
4

<!-- b000044 | contents | pages [2] -->
2.1

<!-- b000045 | contents | pages [2] -->
Assumptions and Justifications . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
4

<!-- b000047 | contents | pages [2] -->
2.2

<!-- b000048 | contents | pages [2] -->
Notations

<!-- b000049 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
5

<!-- b000051 | contents | pages [2] -->
3 Task 1: Location Prediction Model Incorporating the Kalman Filter

<!-- b000052 | contents | pages [2] -->
6

<!-- b000053 | contents | pages [2] -->
3.1

<!-- b000054 | contents | pages [2] -->
Consideration for Uncertainties and Equipping the Submersible . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
6

<!-- b000056 | contents | pages [2] -->
3.2

<!-- b000057 | contents | pages [2] -->
Computational Fluid Dynamics Analysis . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
6

<!-- b000059 | contents | pages [2] -->
3.3

<!-- b000060 | contents | pages [2] -->
Mechanism of Kalman Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
8

<!-- b000062 | contents | pages [2] -->
3.4

<!-- b000063 | contents | pages [2] -->
Model establishment

<!-- b000064 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
9

<!-- b000066 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000067 | contents | pages [2] -->
3.5

<!-- b000068 | contents | pages [2] -->
Fine-tuning Kalman Filter

<!-- b000069 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
10

<!-- b000071 | contents | pages [2] -->
3.6

<!-- b000072 | contents | pages [2] -->
Results and Analysis

<!-- b000073 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
10

<!-- b000075 | contents | pages [2] -->
4 Task 2: Equipment Preparation for Host Ship and Rescue Vessel

<!-- b000076 | contents | pages [2] -->
11

<!-- b000077 | contents | pages [2] -->
4.1

<!-- b000078 | contents | pages [2] -->
Equipment Selection by Principal Component Analysis . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
11

<!-- b000080 | contents | pages [2] -->
4.2

<!-- b000081 | contents | pages [2] -->
Results and Analysis

<!-- b000082 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
12

<!-- b000084 | contents | pages [2] -->
5 Task 3: Feasible Zone and Search Pattern

<!-- b000085 | contents | pages [2] -->
14

<!-- b000086 | contents | pages [2] -->
5.1

<!-- b000087 | contents | pages [2] -->
Determination of Feasible Zone for Search . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
14

<!-- b000089 | contents | pages [2] -->
5.2

<!-- b000090 | contents | pages [2] -->
Cumulative Distribution Function of Probability . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
15

<!-- b000092 | contents | pages [2] -->
5.3

<!-- b000093 | contents | pages [2] -->
Search Pattern Based on Sonar Scanning . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
15

<!-- b000095 | contents | pages [2] -->
5.4

<!-- b000096 | contents | pages [2] -->
Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
16

<!-- b000098 | contents | pages [2] -->
5.5

<!-- b000099 | contents | pages [2] -->
Analysis of the Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
18

<!-- b000101 | contents | pages [2] -->
6 Task 4: Model extrapolation

<!-- b000102 | contents | pages [2] -->
18

<!-- b000103 | contents | pages [2] -->
6.1

<!-- b000104 | contents | pages [2] -->
Caribbean Sea . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [2] -->
18

<!-- b000106 | contents | pages [2] -->
6.2

<!-- b000107 | contents | pages [2] -->
Coorporation strategy between multiple submersibles . . . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
19

<!-- b000109 | contents | pages [2] -->
7 Sensitivity Analysis and Error Analysis

<!-- b000110 | contents | pages [2] -->
20

<!-- b000111 | contents | pages [2] -->
8 Evaluation and Promotion of Model

<!-- b000112 | contents | pages [2] -->
21

<!-- b000113 | contents | pages [2] -->
8.1

<!-- b000114 | contents | pages [2] -->
Strengths

<!-- b000115 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [2] -->
21

<!-- b000117 | contents | pages [2] -->
8.2

<!-- b000118 | contents | pages [2] -->
Weaknesses and Possible Improvements . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
21

<!-- b000120 | contents | pages [2] -->
References

<!-- b000121 | contents | pages [2] -->
21

<!-- b000122 | contents | pages [2] -->
Memo for the Greek Government

<!-- b000123 | contents | pages [2] -->
23

<!-- b000124 | contents | pages [2] -->
关注数学模型

<!-- b000125 | furniture | pages [2] -->
2

<!-- b000126 | furniture | pages [2] -->
MATHmodels

<!-- b000127 | furniture | pages [2] -->
获取更多资讯

<!-- b000128 | furniture | pages [3] -->
Team 2425792

<!-- b000129 | furniture | pages [3] -->
Page 2 of 24

<!-- b000130 | heading | pages [3] -->
1 Introduction

<!-- b000131 | heading | pages [3] -->
1.1 Background

<!-- b000132 | prose | pages [3] -->
微信公众号：数学模型 Submersibles represent cutting-edge technology designed to explore the depths of our oceans.[1] Different from submarines that are capable of independent operations, submersibles is typically tethered or assisted by a host ship. Notably, manned submersibles that carries humans to ar- rive at complex deep sea environments quickly and accurately, have recently witnessed global advancements.[2] This progress has spurred Maritime Cruises Mini-Submarines (MCMS) to envision the inte- gration of submersibles into underwater tourism in the the Ionian Sea, a region known for its rich history and myriad sunken shipwrecks.

<!-- b000133 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000134 | caption | pages [3] -->
Figure 1: Background

<!-- b000135 | prose | pages [3] -->
The prospect of offering tourists exhilarating ventures to the ocean’s depths, however, faces challenges in the wake of the 2023 Titan submersible incident, [3] a catastrophic underwater im- plosion resulting in no survivors due to inherent defects. The fundamental cause of the mishap was the inability to swiftly pinpoint and search the submersible, thereby profoundly decelerating the rescue. The incident has sparked widespread concerns regarding the localization and rescuing speed of submersibles after it was defected underwater.

<!-- b000136 | prose | pages [3] -->
Generally, two types of defect of a submersible can occur.(Fig.2)

<!-- b000137 | caption | pages [3] -->
Figure 2: Submersible’s defects and consequences

<!-- b000138 | prose | pages [3, 4] -->
关注数学模型 Once a defective submersible lose its propulsion, it might end up situated on the seafloor or at a level of neutral buoyancy, where it neither descends nor ascends. However, in the complex and dynamic deep water environments, the submersible can be drifted away by currents and difference of seawater density. Once a defective submersible lose its communication to the host ship, it is 微信公众号：数学模型 hardly possible for the host ship to locate the submersible. Therefore, enhancing the accuracy of localization before the rescue is the first challenge. Moreover, once the area where the submersible might be situated is determined, the search pattern for rescue is to be improved.

<!-- b000139 | furniture | pages [3] -->
2

<!-- b000140 | furniture | pages [3] -->
MATHmodels

<!-- b000141 | furniture | pages [3] -->
获取更多资讯

<!-- b000142 | furniture | pages [4] -->
Team 2425792

<!-- b000143 | furniture | pages [4] -->
Page 3 of 24

<!-- b000145 | prose | pages [4] -->
In order to relieve public concerns and obtain approval for submersible tourism from regulators, MCMS requires our team to construct models for better locating the submersible over time and developing search patterns for the rescue. Furthermore, our model aims to shed light on innovative methodologies to equip the host ship and rescue vessels and minimize the rescue time.

<!-- b000146 | heading | pages [4] -->
1.2 Problem Restatement

<!-- b000147 | prose | pages [4] -->
In reaction to MCMS requirements, we have been assigned to develop models for the purposes of: 微信号：MATHmodels

<!-- b000148 | prose | pages [4] -->
• Localization

<!-- b000149 | prose | pages [4] -->
- Construct models to accurately forecast the submersible’s location over time.

<!-- b000150 | prose | pages [4] -->
- Take into account uncertainties such as currents, varying sea densities, and the geographical features of the Ionian Sea.

<!-- b000151 | prose | pages [4] -->
- Design the information the submersible can intermittently relay back to the host ship to minimize these uncertainties.

<!-- b000152 | prose | pages [4] -->
- Determine the equipment needed for an effective transmission of this information.

<!-- b000153 | prose | pages [4] -->
• Equipment Recommendation

<!-- b000154 | prose | pages [4] -->
- Propose additional search equipment that MCMS should employ on the host ship.

<!-- b000155 | prose | pages [4] -->
- Consider myriad indicators affecting the performance of the equipment.

<!-- b000156 | prose | pages [4] -->
- Evaluate and choose the most proper equipment for the search of submersible.

<!-- b000157 | prose | pages [4] -->
- Derive what extra equipment a rescue vessel might necessitate.

<!-- b000158 | prose | pages [4] -->
• Search

<!-- b000159 | prose | pages [4] -->
- Develop a model that utilizes data from the localization models to suggest initial deployment points for the rescue equipment.

<!-- b000160 | prose | pages [4] -->
- Minimize the duration required to find a lost submersible by constructing a model of the search strategy.

<!-- b000161 | prose | pages [4] -->
- Express the probability of finding the submersible as a function of time and cumulative search results.

<!-- b000162 | prose | pages [4] -->
• Adaptation

<!-- b000163 | prose | pages [4] -->
- Explore the potential to broaden the applicability of the constructed model to incorporate other oceanic tourist destinations.

<!-- b000164 | prose | pages [4] -->
- Identify necessary adjustments to the model to accommodate multiple submersibles moving within a similar vicinity.

<!-- b000165 | prose | pages [4] -->
关注数学模型

<!-- b000166 | furniture | pages [4] -->
2

<!-- b000167 | furniture | pages [4] -->
MATHmodels

<!-- b000168 | furniture | pages [4] -->
获取更多资讯

<!-- b000169 | furniture | pages [5] -->
Team 2425792

<!-- b000170 | furniture | pages [5] -->
Page 4 of 24

<!-- b000171 | heading | pages [5] -->
1.3 Our Approach

<!-- b000172 | prose | pages [5] -->
The approach of our model is as follows:

<!-- b000173 | prose | pages [5] -->
• Establish Computational Fluid Dynamics (CFD) equations taking into account the uncer- 微信公众号：数学模型 tainties.

<!-- b000174 | prose | pages [5] -->
• Employ the Kalman filter to correct inaccuracies and improve trajectory estimation through the ”update-predict” recursive algorithm.

<!-- b000175 | prose | pages [5] -->
• Utilize the probability distribution of the submersible’s position to fit a trajectory of higher confidence for more precise localization.

<!-- b000176 | prose | pages [5] -->
• Analyze and select rescue equipment based on Principle Component Analysis for the host ship and rescue vessels.

<!-- b000177 | prose | pages [5] -->
• Use the probability density function to compute a 95% confidence 3D space and deploy the Along-Isobath Search Strategy within this space to reduce the searching time.

<!-- b000178 | prose | pages [5] -->
• Discuss the extrapolation of the model in the Caribbean sea.

<!-- b000179 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000180 | prose | pages [5] -->
• Combine the Voronoi Diagram with our Search Model to actualize the cooperation between submersibles.

<!-- b000181 | caption | pages [5] -->
Figure 3: Our Approach

<!-- b000182 | heading | pages [5] -->
2 Model Preparation

<!-- b000183 | heading | pages [5] -->
2.1 Assumptions and Justifications

<!-- b000184 | prose | pages [5] -->
• Assumption 1: The submersible is a spherical rigid body.

<!-- b000185 | prose | pages [5] -->
- Justification: The choice of spherical shape is based on the principle of isotropy, which means that the submersible exhibits the same properties and behavior in every direction, allowing us to

<!-- b000186 | prose | pages [5, 6] -->
关注数学模型 simplify the fluid dynamics analysis by eliminating the need to consider the impacts of roll, pitch and yaw motions.

<!-- b000187 | furniture | pages [5] -->
2

<!-- b000188 | furniture | pages [5] -->
MATHmodels

<!-- b000189 | furniture | pages [5] -->
获取更多资讯

<!-- b000190 | furniture | pages [6] -->
Team 2425792

<!-- b000191 | furniture | pages [6] -->
Page 5 of 24

<!-- b000193 | prose | pages [6] -->
• Assumption 2: The submersible operates generally at the neutral buoyancy level.

<!-- b000194 | prose | pages [6] -->
微信公众号：数学模型 - Justification: By maintaining neutral buoyancy, the submersible remains at a desired depth without continuous adjustments. This reduces the complexity and energy requirements of the submersible’s operations.

<!-- b000195 | prose | pages [6] -->
• Assumption 3: The submersible retains an invariant density after an incident.

<!-- b000196 | prose | pages [6] -->
- Justification: In the absence of consideration of other disturbances (initial velocity, ocean currents, etc.), this assumption ensures that the submersible remains at the neutral buoyancy level after an incident, which reduces the factors requisite for localization.

<!-- b000197 | prose | pages [6] -->
• Assumption 4: Lost of communication and lost of propulsion of the submersible (the two types of defects shown in Fig. 2) takes place simultaneously.

<!-- b000198 | prose | pages [6] -->
- Justification: Should the submersible merely detect its disconnection, it would then power down its propulsion systems so as to introduce less deviations. Should the submersible solely lose power, the submersible could simply send a signal to the host ship to instigate rescue operations, 微信号：MATHmodels which falls out of consideration.

<!-- b000199 | heading | pages [6] -->
2.2 Notations

<!-- b000200 | caption | pages [6] -->
Table 1: Definition of Symbols

<!-- b000201 | prose | pages [6] -->
Symbol Definition Unit

<!-- b000202 | prose | pages [6] -->
kg · m2 M inertia matrix of the rigid body C kg Coriolis-centripetal force matrix D kg/s fluid damping matrix g(η) N restoring forces under static conditions Fprop N thrust force of the propellers τ N external environmental disturbances (such as currents) m kg mass of the submersible m3 V volume of the submersible v m/s speed matrix of submersible relative to earth kg/m3 ρ density of water n rad/s propeller rotation speed u m/s vehicle’s speed d m propeller diameter KT thrust coefficient - − ν vector of linear and angular velocities

<!-- b000203 | prose | pages [6] -->
The main variables and parameters while specific value of those parameters will be given later are defined in Tbl. 1.

<!-- b000204 | prose | pages [6] -->
关注数学模型

<!-- b000205 | furniture | pages [6] -->
2

<!-- b000206 | furniture | pages [6] -->
MATHmodels

<!-- b000207 | furniture | pages [6] -->
获取更多资讯

<!-- b000208 | furniture | pages [7] -->
Team 2425792

<!-- b000209 | furniture | pages [7] -->
Page 6 of 24

<!-- b000210 | heading | pages [7] -->
3 Task 1:

<!-- b000211 | heading | pages [7] -->
Location Prediction Model Incorporating the

<!-- b000212 | prose | pages [7] -->
Kalman Filter

<!-- b000213 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000214 | heading | pages [7] -->
3.1 Consideration for Uncertainties and Equipping the Submersible

<!-- b000215 | prose | pages [7] -->
In the deep-ocean environments, there exists myriad uncertainties that could hinder the accu- racy of our prediction.(Fig. 4)

<!-- b000216 | caption | pages [7] -->
Figure 4: Uncertainties of Localization Prediction

<!-- b000217 | prose | pages [7] -->
微信号：MATHmodels In order to decrease the uncertainties, it is necessary for the submersible to periodically transmit a plethora of data collected by various sensors equipped onboard to the host ship, including the velocity data collected by the Inertial Measurement Unit (IMU), salinity collected by environmental sensors, the force exerted by the water flow measured by pressure sensors, and so forth.

<!-- b000218 | prose | pages [7] -->
Accordingly, we adopt the Inertial Navigation System (INS) to localize the submersible, which necessitates motion sensors such as accelerometer, gyroscope, and magnetometer and a computer to continuously calculate the position of the submersible in motion without the need for [4] In addition, we can equip the submersible with environmental sensors to external references. capture further information.

<!-- b000219 | prose | pages [7] -->
Correspondingly, the submersible should periodically send the following data back to the host ship:

<!-- b000220 | heading | pages [7] -->
1. Position Updates: The calculated latitude, longitude, and depth.

<!-- b000221 | heading | pages [7] -->
2. Velocity Data: The velocity of the submersible in 6 dimensions.

<!-- b000222 | heading | pages [7] -->
3. Sensor Readings: Processed sensor data from the accelerometer, gyroscope, and magnetometer.

<!-- b000223 | heading | pages [7] -->
4. Health and Status: The operational status of the submersible, such as the remaining propulsion.

<!-- b000224 | heading | pages [7] -->
5. Environmental Data: Temperature, salinity, or water density that might affect INS performance.

<!-- b000225 | prose | pages [7] -->
The host ship can use this information to apply corrections to INS data and ensure the the accuracy of submersible’s localization. Additionally, the periodic communication helps in case of an emergency, conducting search and rescue operations.

<!-- b000226 | heading | pages [7] -->
3.2 Computational Fluid Dynamics Analysis

<!-- b000227 | prose | pages [7] -->
We established the motion equations for the submersible, employing data collected by sensors on the submersible, to calculate its trajectory.

<!-- b000228 | prose | pages [7] -->
The dynamics of the submersibles are primarily influenced by hydrodynamic forces, static forces(gravity and buoyancy), thrust of propellers, environmental disturbance(such as ocean currents and density differences). In the work of Fossen 1994, [5] the dynamics of an Autonomous Underwater

<!-- b000229 | prose | pages [7, 8] -->
关注数学模型 Vehicle (AUV) are captured by a comprehensive six degrees of freedom (6DOF) model. The generic form of the model is given by:

<!-- b000230 | furniture | pages [7] -->
2

<!-- b000231 | furniture | pages [7] -->
MATHmodels

<!-- b000232 | furniture | pages [7] -->
获取更多资讯

<!-- b000233 | furniture | pages [8] -->
Team 2425792

<!-- b000234 | furniture | pages [8] -->
Page 7 of 24

<!-- b000236 | prose | pages [8] -->
M ˙ν + C(ν)ν + D(ν)ν + g(η) = τ + Fprop (1) 微信公众号：数学模型 See also Table 1 for definition of symbols.

<!-- b000237 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000238 | caption | pages [8] -->
Figure 5: Computational fluid dynamics(CFD) analysis

<!-- b000239 | prose | pages [8] -->
This relative velocity vsub is used in the drag force equation to account for the effect of the stochastic ocean current on the submersible’s dynamics.

<!-- b000240 | prose | pages [8] -->
vsub = v −ucurrent (2)

<!-- b000241 | prose | pages [8] -->
  u sin(θ) cos(ϕ) u sin(θ) sin(ϕ) ucurrent =   u cos(θ)

<!-- b000242 | prose | pages [8] -->
In the course of thermodynamics, [6] we learned that the force exerted by the propeller and the currents are:

<!-- b000243 | prose | pages [8] -->
||Fprop||2 = (1 −t)ρn2d2KT (3)

<!-- b000244 | prose | pages [8] -->
  ||Fprop||2 sin(θ) cos(ϕ) ||Fprop||2 sin(θ) sin(ϕ) Fprop = (4)   ||Fprop||2 cos(θ) Fcurrent = −1 2ρCdA||vsub||2vsub (5)

<!-- b000245 | prose | pages [8] -->
where || · ||2 stands for the Euclidean norm (also known as the L2 norm) In order to simplify Fossen’s model, we made these assumptions: The submersible operates at a relatively constant depth, and the influence of heave, roll, and pitch motions are negligible over the time scale of interest. Consequently, the dynamic effects associated with these motions are omitted for the sake of model parsimony and computational efficiency.

<!-- b000246 | prose | pages [8, 9] -->
关注数学模型 Therefore, in this case(in the form of matrix), we have:

<!-- b000247 | furniture | pages [8] -->
2

<!-- b000248 | furniture | pages [8] -->
MATHmodels

<!-- b000249 | furniture | pages [8] -->
获取更多资讯

<!-- b000250 | furniture | pages [9] -->
Team 2425792

<!-- b000251 | furniture | pages [9] -->
Page 8 of 24

<!-- b000253 | prose | pages [9] -->
mdv dt = Fcurrent + Fprop (6)

<!-- b000254 | prose | pages [9] -->
微信公众号：数学模型 Particularly, when the submersible malfunctioned, Fprop = 0. This CFD(Computational Fluid Dynamics) is the foundation of the following parts.

<!-- b000255 | heading | pages [9] -->
3.3 Mechanism of Kalman Filter

<!-- b000256 | prose | pages [9] -->
The former model is based on differential equations and sensor data, specifically from an IMU(Inertial Measurement Unit). Both the model and the IMU data satisfy the conditions of a Markov chain, where the state vector at any given moment is related to that in the previous timeframe. This is possible due to the deterministic nature of classical Newtonian mechanics.

<!-- b000257 | prose | pages [9] -->
For statistics and control theory, Kalman Filtering is a computationally efficient algorithm that uses a series of measurements observed over time, including statistical noise and other inaccuracies, 微信号：MATHmodels and produces estimates of unknown variables that tend to be more accurate than those based on a single measurement alone, by estimating a joint probability distribution over the variables for each timeframe. It recursively estimates the system states through prediction and update steps.

<!-- b000258 | prose | pages [9] -->
Now, we apply Kalman Filter to the differential equations. We assume that all sensor measure- ment errors (systematic errors) and process errors of the real environment (random errors) have a mean of zero, follow a normal distribution, and are independent with respect to time. Under these conditions, the Kalman Filter emerges as the most appropriate model for estimating the states of a dynamic system from a series of incomplete and noisy measurements.

<!-- b000259 | caption | pages [9] -->
Figure 6: How Kalman Filter works: Predict & Update

<!-- b000260 | prose | pages [9] -->
• Prediction steps

<!-- b000261 | prose | pages [9] -->
Predicted state estimate:

<!-- b000262 | prose | pages [9] -->
ˆxk|k−1 = Fkˆxk−1|k−1 + Bkuk (7)

<!-- b000263 | prose | pages [9] -->
Predicted error covariance: Pk|k−1 = FkPk−1|k−1F ⊤ k + Qk

<!-- b000264 | prose | pages [9] -->
• Update steps Observation residual: yk = zk −Hkˆxk|k−1 Residual covariance: Sk = HkPk|k−1H⊤ k + Rk k S−1 Optimal Kalman gain: Kk = Pk|k−1H⊤ k Updated state estimate: ˆxk|k = ˆxk|k−1 + Kkyk Updated error covariance: Pk|k = (I −KkHk)Pk|k−1

<!-- b000265 | prose | pages [9] -->
关注数学模型

<!-- b000266 | furniture | pages [9] -->
2

<!-- b000267 | furniture | pages [9] -->
MATHmodels

<!-- b000268 | furniture | pages [9] -->
获取更多资讯

<!-- b000269 | furniture | pages [10] -->
Team 2425792

<!-- b000270 | furniture | pages [10] -->
Page 9 of 24

<!-- b000271 | heading | pages [10] -->
3.4 Model establishment

<!-- b000272 | prose | pages [10] -->
The state vector of the Kalman Filter is defined as:

<!-- b000273 | prose | pages [10] -->
x = [xsub, ysub, zsub, ˙xsub, ˙ysub, ˙zsub, ¨xsub, ¨ysub, ¨zsub]⊤ 微信公众号：数学模型 (8)

<!-- b000274 | prose | pages [10] -->
where xsub, ysub, zsub are the coordinates of the submersible’s center of mass relative to the initial zero position of the submersible’s IMU (Inertial Measurement Unit).

<!-- b000275 | prose | pages [10] -->
We choose the IMU reference frame for its stability - it remains fixed and doesn’t move along with the submersible, which in turn allows for more precise global positioning. The adoption of this frame provides a stationary point-of-reference, enabling us to accurately measure changes in the position and velocity of the submersible over time. Furthermore, the data generated by the IMU inherently aligns with this coordinate framework, which greatly facilitates future calculations.

<!-- b000276 | prose | pages [10] -->
Next, based on data provided by various sensors, we select the following observation vector:

<!-- b000277 | prose | pages [10] -->
z = [ ˙xsub, ˙ysub, ˙zsub, ¨xsub, ¨ysub, ¨zsub, Ftot,x, Ftot,y, Ftot,z]⊤ 微信号：MATHmodels where we make full use of the velocity terms provided by the submersible’s IMU and we can calculate the acceleration terms using the CFD in the mean while.

<!-- b000278 | prose | pages [10] -->
We rewrite the two vectors above in a more compact form. Let⃗xsub = [xsub, ysub, zsub] be the three-dimensional coordinates of the submersible,⃗Ftot be the composition of forces. Thus, the state vector and the observation vector become:

<!-- b000279 | prose | pages [10] -->
i⊤ i⊤ h h xsub, ˙⃗xsub, ¨⃗xsub xsub, ¨ ˙ x = z = xsub,⃗Ftot

<!-- b000280 | prose | pages [10] -->
Now, let’s write the state transition equation, which is the matrix equivalent to the following mapping f : xk−1|k−1 7→xk|k−1. Generally, the transition matrix is equal to the Jacobian matrix of the transition equation, as shown in Eq. 7. In our case, this mapping is linear, so the Jacobian matrix turns out to be the coefficient matrix. Based on the compact state representation, we can express it using matrix block form.

<!-- b000281 | prose | pages [10] -->
For the convenience of expression, we define:

<!-- b000282 | prose | pages [10] -->
    1 0 0 0 0 0 not not 0 1 0 0 0 0 I3 = , 0 =    0 0 1 0 0 0

<!-- b000283 | prose | pages [10] -->
Thus, the state transition matrix derived from the predicted state estimate is:

<!-- b000284 | prose | pages [10] -->
2dt2 · I3 1   dt · I3 I3 dt · I3 F = 0 I3   0 0 I3

<!-- b000285 | prose | pages [10] -->
In the submersible model, no quantity can be known precisely or measured accurately. There- fore, we forego the opportunity to provide known external inputs to the Kalman model via the control vector, thus preventing these noisy and uncertain factors from directly affecting the state. In other words:

<!-- b000286 | prose | pages [10] -->
⊤, u = [0]  0 0 0 0 0 0 0 0 0 B =

<!-- b000287 | prose | pages [10, 11] -->
关注数学模型 Finally, we express the observation matrix H, which maps the observation space to the real space:

<!-- b000288 | furniture | pages [10] -->
2

<!-- b000289 | furniture | pages [10] -->
MATHmodels

<!-- b000290 | furniture | pages [10] -->
获取更多资讯

<!-- b000291 | furniture | pages [11] -->
Team 2425792

<!-- b000292 | furniture | pages [11] -->
Page 10 of 24

<!-- b000294 | prose | pages [11] -->
  0 I3 0 0 0 I3 subject to z = H · x H =  微信公众号：数学模型 0 0 I3/m where m denotes the mass of the submersible.

<!-- b000295 | prose | pages [11] -->
Thus, we fully integrate the data collected by the sensor installed on the submersible into the model for data fusion, and jointly reduce the prediction error. Specifically, we can extract real-time IMU data and obtain the pose quaternion of the submersible from the industrial high-precision gyroscope as well as the three-axis acceleration from the accelerometer. Using the gyroscope’s quaternion, we convert the acceleration calculated by CFD to the IMU’s fixed coordinate system before updating the observation vector. The extensibility of this observation matrix is high. If we have additional sensors, such as a Doppler velocimeter, we can also include the velocity prediction in the observations.

<!-- b000296 | prose | pages [11] -->
It’s also worth mentioning that in the case of a communication loss, we will prune the sensor- based observation from the matrices, and the filter can continue working smoothly. 微信号：MATHmodels

<!-- b000297 | heading | pages [11] -->
3.5 Fine-tuning Kalman Filter

<!-- b000298 | prose | pages [11] -->
The efficacy of the Kalman filter is significantly influenced by the accurate modeling of the process noise covariance matrix Q and the measurement noise covariance matrix R. These matrices represent the expected uncertainty in our process model and measurement sensors, respectively. An iterative process of testing and refinement is typically employed to adjust Q and R until the filter’s performance meets the desired criteria for accuracy and reliability. This tuning process is crucial for achieving optimal filter performance and is often the difference between a good estimation and a great one. According to our extensive empirical testing, we eventually adopted the parameters that add some extent of uncertainty to the output of CFD while giving credit to the data directly gained from accessible high-precision sensors.

<!-- b000299 | prose | pages [11] -->
    2 · I3 5 · I3 0 0 0 0 0.5 · I3 3 · I3 0 0 0 0 R = , Q =    5 · I3 0 0 0 0 I3

<!-- b000300 | heading | pages [11] -->
3.6 Results and Analysis

<!-- b000301 | prose | pages [11] -->
In the MATLAB environment, we have simulated the trajectory after the malfunction of the submersible takes place based on our localization model.

<!-- b000302 | caption | pages [11] -->
Figure 7: Simulated Trajectory in MATLAB (a)(b)(c) Evolution of the trajectory (d) Bottom view of the trajectory

<!-- b000303 | prose | pages [11, 12] -->
关注数学模型 As shown in Fig.7, the submersible without propulsion is drifted by the currents. The red dots on the surface of the ocean signify the current density. The trajectory manifests a spiraling pattern, which is a consequence of the vortex-like ocean current disturbances. Moreover, due to the initial downward direction of velocity at the commencement of the incident, the spiral path displays a 微信公众号：数学模型 trend of downward divergence. The result is as expected.

<!-- b000304 | furniture | pages [11] -->
2

<!-- b000305 | furniture | pages [11] -->
MATHmodels

<!-- b000306 | furniture | pages [11] -->
获取更多资讯

<!-- b000307 | furniture | pages [12] -->
Team 2425792

<!-- b000308 | furniture | pages [12] -->
Page 11 of 24

<!-- b000310 | prose | pages [12] -->
Beyond potential impacts from the underwater currents, our simulation takes into account potential collisions imparted by the seabed geography. Within geography featuring protruding submarine mountain bridges, the collision detection module embodied in the model can identify abrupt velocity alterations and modify the trajectory prediction accordingly.(Fig.8)

<!-- b000311 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000312 | caption | pages [12] -->
Figure 8: Spacial case: underwater landscape

<!-- b000313 | caption | pages [12] -->
Figure 9: Spatial probability distribution of

<!-- b000314 | prose | pages [12] -->
blocked the route of the submersible the defective submersible

<!-- b000315 | prose | pages [12] -->
Further elaborating, Fig.9 provides a display of the probable area of occurrence of the sub- mersible deduced through Kalman Filter prediction in the aftermath of an incident. The blue trajectory reflects the bona fide path of the submersible, while the red scatter points portray the spactial probability distribution computed by the model.

<!-- b000316 | heading | pages [12] -->
4 Task 2: Equipment Preparation for Host Ship and Rescue

<!-- b000317 | prose | pages [12] -->
Vessel

<!-- b000318 | heading | pages [12] -->
4.1 Equipment Selection by Principal Component Analysis

<!-- b000319 | prose | pages [12] -->
In order to improve communication between the submersible and the host ship to achieve more accurate positioning and rapid search and rescue operations, we recommend equipping the host ship with additional search devices. The market offers a diverse array of devices designed for this purpose, each distinguishable by various performance indicators. To analyze and compare the indicators and select the most suitable devices, we propose employing the Principal Component Analysis (PCA), which allows us to to screen out key variables and reduce the complexity of the situation.

<!-- b000320 | prose | pages [12] -->
The main modeling steps are described below.

<!-- b000321 | prose | pages [12] -->
• Sample matrix: 14 representative devices available on the market are chosen and 13

<!-- b000322 | prose | pages [12, 13] -->
关注数学模型 performance indicators denoted by ai are established. Each device is then conceptualized as a vector xn = (xn1, . . . , xn13). Thus, we construct the sample matrix X14×13 to represent all the data we collected from the manufacturer.

<!-- b000323 | furniture | pages [12] -->
2

<!-- b000324 | furniture | pages [12] -->
MATHmodels

<!-- b000325 | furniture | pages [12] -->
获取更多资讯

<!-- b000326 | furniture | pages [13] -->
Team 2425792

<!-- b000327 | furniture | pages [13] -->
Page 12 of 24

<!-- b000329 | prose | pages [13] -->
• Standardization: We standardize X by subtracting the mean from each row and dividing 微信公众号：数学模型 each row by its standard deviation.

<!-- b000330 | prose | pages [13] -->
• Covariance matrix: The element cij of the covariance matrix C represents the covariance between indicators ai and aj and is given by:

<!-- b000331 | prose | pages [13] -->
n 1 X (xki −¯xi)(xkj −¯xj) cij = n −1 k=1

<!-- b000332 | prose | pages [13] -->
where xki and xkj are the standardized values of variables i and j for the k-th observation, and ¯xi and ¯xj are their respective means.

<!-- b000333 | prose | pages [13] -->
• Eigendecomposition and contribution rate: We calculate eigenvalues and corresponding eigenvectors of C. On the basis of the eigenvalues, we can solve the contribution rate and the accumulative contribution rate of the parameters. 微信号：MATHmodels

<!-- b000334 | caption | pages [13] -->
Table 2: Eigenvectors and contribution rate corresponding to the 3 principal components

<!-- b000335 | prose | pages [13] -->
Indicator PC1 PC2 PC3

<!-- b000336 | prose | pages [13] -->
0.3839593 -0.1153862 Cost 0.0901579 Workforce 0.3467707 0.0078141 0.3145092 -0.3274316 Availability 0.0775631 -0.2925692 Maintenance 0.3120141 0.2352130 0.3001698 0.5512866 Readiness -0.1001557 -0.0502958 Energy Consumption 0.3824945 -0.0713404 -0.1810475 Detection Distance 0.2562031 0.2695921 -0.0706944 -0.3954241 Resolution 0.2663515 0.1367001 -0.3388978 Detection Speed 0.3297991 -0.0073919 0.5167477 Adaptability -0.0286098 0.1725088 Anti-Interference Capability 0.2460527 0.1149641 -0.2996652 Ease of Operation -0.2363936 0.4295668 -0.1816506 0.5453001 Failure Rate 0.0939937 0.1261542 Variance Contribution Rate 0.4779 0.2267 0.1520 0.8566 Cumulative Contribution Rate 0.4779 0.7046

<!-- b000337 | prose | pages [13] -->
According to Tbl. 2, We selected the first three components as the three principle components PC1, PC2, PC3, representing respectively the cost-effectiveness, the operational reliability, and the human resource aspects.

<!-- b000338 | heading | pages [13] -->
4.2 Results and Analysis

<!-- b000339 | prose | pages [13] -->
Multiplying the contribution rate with the value of corresponding principle components, we can obtain the composite scores of our 14 devices as shown in Tbl. 3.

<!-- b000340 | prose | pages [13, 14] -->
关注数学模型 Equipment Composite Score

<!-- b000341 | furniture | pages [13] -->
2

<!-- b000342 | furniture | pages [13] -->
MATHmodels

<!-- b000343 | furniture | pages [13] -->
获取更多资讯

<!-- b000344 | furniture | pages [14] -->
Team 2425792

<!-- b000345 | furniture | pages [14] -->
Page 13 of 24

<!-- b000346 | caption | pages [14] -->
Table 3: Composite Scores by Equipment

<!-- b000348 | prose | pages [14] -->
Perry Slingsby Multi-Beam 0.8313 微信公众号：数学模型 Deep Trekker DTX2 -0.905 Teledyne BlueView Multi-Beam Sonar 1.8536 Deep Trekker Side Scan Sonar -0.7821 Edgetech Combined Bathymetry and Side Scan Sonar 1.5798 Divex AUV-1000 -2.6028 Deep Trekker DTX2 AUV -0.4873 James Fisher JF-AUV 1.0914 Perry Slingsby Explorer AUV 0.285 Divex ROV-1000 -0.0834 Soil Machine Dynamics Quantum EV 1.3665 James Fisher Innovator -1.0597 Kystdesign Seaglider -1.2779 Perry Slingsby Triton 0.1904 微信号：MATHmodels From the result above, we find that Perry Slingsby Multi-Beam, Perry Slingsby Side Scan Sonar and Divex AUV-1000 are the most suitable devices to be equipped on the host ship.(Fig. 10) Following is a brief introduction of the 3 devices:

<!-- b000349 | prose | pages [14] -->
• Teledyne BlueView Multi-Beam Sonar: a type of active sonar system that propels a series of sound pulses underwater to a plethora of angles and manifests a 3D depiction of the ocean floor.

<!-- b000350 | prose | pages [14] -->
• Edgetech Combined Bathymetry and Side Scan Sonar: a sonar combining bathymetry and broad detection that projects sound pulses toward both sides underwater while receiving their echoes subsequently, thereby generating a 2D image of large areas of the seabed.

<!-- b000351 | prose | pages [14] -->
• Soil Machine Dynamics Quantum EV: a Remotely Operated Vehicle (ROV) that has commendable tool/instrument carriage capacity, enabling operations reaching depths of up to 6000 meters.

<!-- b000352 | caption | pages [14] -->
Figure 10: Equipment for the host ship and rescue vessels (a)Teledyne BlueView Multi-Beam Sonar (b)Edgetech

<!-- b000353 | prose | pages [14] -->
Combined Bathymetry and Side Scan Sonar (c)Soil Machine Dynamics Quantum EV (d)Impact Subsea ISS360 Sonar (e)Imenco Cameras and Lights (f)Allied Luffing Arm Rescue Boat Davit System

<!-- b000354 | prose | pages [14, 15] -->
关注数学模型 Concurrently, we choose the Soil Machine Dynamics ROV as our rescue vessel. Similarly, using the same PCA method, we conclude that the following equipment can be equipped for the rescue vessel: Impact Subsea ISS360 Sonar, Imenco Cameras and Lights and Allied Luffing Arm Rescue Boat Davit System.(Fig. 10) 微信公众号：数学模型

<!-- b000355 | furniture | pages [14] -->
2

<!-- b000356 | furniture | pages [14] -->
MATHmodels

<!-- b000357 | furniture | pages [14] -->
获取更多资讯

<!-- b000358 | furniture | pages [15] -->
Team 2425792

<!-- b000359 | furniture | pages [15] -->
Page 14 of 24

<!-- b000361 | heading | pages [15] -->
5 Task 3: Feasible Zone and Search Pattern

<!-- b000362 | prose | pages [15] -->
By further exploiting the Kalman Filter, establishing more effective searching patterns and utilizing appropriate equipment, our model can reduce the searching time of a defective submersible with the help of a high localization accuracy, even without direct communication of the submersible with respect to the host ship.

<!-- b000363 | heading | pages [15] -->
5.1 Determination of Feasible Zone for Search

<!-- b000364 | prose | pages [15] -->
Previously, we have only utilized the predictive information from the Kalman filter for the 微信号：MATHmodels temporary location of the submersible. However, we can further exploit other useful properties of the Kalman filter. With this intuition, we considered using the predicted estimate covariance matrix Pk|k−1 maintained by Kalman to calculate the probability distribution of the submersible’s potential locations.

<!-- b000365 | prose | pages [15] -->
Let’s assume that the errors in the x-y-z axes are independent of each other. This assumption allows us to conveniently use a multivariate Gaussian distribution to represent the distribution of the submersible’s position at the current moment, which is the first three dimensions predicted by the Kalman filter (as defined in the state vector of the Kalman filter, in Eq.8). Consider the probability density function of a multivariate normal distribution:

<!-- b000366 | prose | pages [15] -->
  1 −1 2(x −µ)⊤Σ−1(x −µ) f(x; µ, Σ) = exp (9) p (2π)k|Σ|

<!-- b000367 | prose | pages [15] -->
where, in our Kalman filter results, k is taken to be 3

<!-- b000368 | prose | pages [15] -->
• µ is the 3-dimensional position prediction given by the Kalman filter.

<!-- b000369 | prose | pages [15] -->
• Σ is a 3 × 3 matrix representing the covariance between x-y-z coordinates.

<!-- b000370 | prose | pages [15] -->
• |Σ| is the determinant of the predicted covariance matrix Pk|k−1.

<!-- b000371 | prose | pages [15] -->
• Σ−1 is the inverse of the covariance matrix.

<!-- b000372 | prose | pages [15] -->
By leveraging the probability density function in conjunction with Kalman filtering predictions, we can accurately ascertain the likelihood of the submersible’s presence at any given point in space. To estimate the search area with the highest probability, we employ a standard statistical 95% confidence region in three-dimensional space, which represents the zone where the submersible is most likely to be found. The concept of the 95% confidence region is depicted in Fig.11, where we have simplified the representation to consider only the x-y plane, thereby enhancing the diagram’s clarity for demonstrative purposes.

<!-- b000373 | prose | pages [15, 16] -->
关注数学模型 微信公众号：数学模型

<!-- b000374 | furniture | pages [15] -->
2

<!-- b000375 | furniture | pages [15] -->
MATHmodels

<!-- b000376 | furniture | pages [15] -->
获取更多资讯

<!-- b000377 | furniture | pages [16] -->
Team 2425792

<!-- b000378 | furniture | pages [16] -->
Page 15 of 24

<!-- b000380 | caption | pages [16] -->
Figure 11: feasible zone of possible appearance, enclosed by red ellipse

<!-- b000381 | prose | pages [16] -->
Hereby, we define this three-dimensional 95% confidence region as the feasible zone, and subsequent search and rescue operations can be considered within this feasible zone.

<!-- b000382 | prose | pages [16] -->
To more accurately reflect the intricate dynamics of the ocean environment, it would be 微信号：MATHmodels advantageous to extend our model to encompass a multi-particle dispersion simulation. This would entail employing the Kalman filter to track the paths of several hypothetical particles simultaneously, thereby improving the model’s relevance and effectiveness.

<!-- b000383 | heading | pages [16] -->
5.2 Cumulative Distribution Function of Probability

<!-- b000384 | prose | pages [16] -->
To determine the probability of locating the submersible as a function of time and amassed search results, we must consider the nonlinear dynamics of our physical model and the inherent [7] For instance, in the most basic scenario where the system chaotic behavior it introduces. could undergo bifurcation, the computational model is unable to discern such occurrences. At any moment, a new potential trajectory could split from the current predicted one. Therefore, the probability of finding the submersible after time t is

<!-- b000385 | prose | pages [16] -->
P(found|t) = 1 αt

<!-- b000386 | prose | pages [16] -->
where α is a decay coefficient proportional to the entropy of the natural seabed environment.

<!-- b000387 | prose | pages [16] -->
Our model suggests that using past search results to predict a submersible’s future location is ineffective, as the submersible’s position is subject to change over time due to factors like ocean currents. The fact that the submersible wasn’t found in a given area before doesn’t mean it won’t be there later. Search failures can also stem from the limited detection capabilities of equipment in a complex underwater environment. Incorporating a time-sensitive probability model based on past searches could lead to overfitting and obscure the actual location. Hence, in line with Occam’s razor, we exclude such complex factors for a simpler, more effective model.

<!-- b000388 | heading | pages [16] -->
5.3 Search Pattern Based on Sonar Scanning

<!-- b000389 | prose | pages [16] -->
Rather than relying on an uncertain probability model to ascertain the precise probability of the submersible’s presence at various locations, a more pragmatic approach involves strategizing an effective search trajectory. Utilizing the feasible zone outlined by the Kalman filter, a comprehensive search within this boundary is efficient.

<!-- b000390 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型

<!-- b000391 | furniture | pages [16] -->
2

<!-- b000392 | furniture | pages [16] -->
MATHmodels

<!-- b000393 | furniture | pages [16] -->
获取更多资讯

<!-- b000394 | furniture | pages [17] -->
Team 2425792

<!-- b000395 | furniture | pages [17] -->
Page 16 of 24

<!-- b000397 | caption | pages [17] -->
Figure 12: Sonar-based Isobath Search Strategy

<!-- b000398 | prose | pages [17] -->
After confirming the search area, it is practical to employ more effective search techniques, such as sonar scanning. Based on the specifications referenced, [8] the previously selected Teledyne Marine Sonar is capable of operating at depths up to 6000 meters, which is suitable for the intended marine environment. The sonar emits a conical acoustic beam with a maximum single-beam width of 3°. This presents an important strategic consideration: optimizing the navigation routes of rescue vessels to maximize the surveyed area per unit time, thus minimizing the total time required for the search.

<!-- b000399 | prose | pages [17] -->
微信号：MATHmodels Given a marine environment with a uniform slope, similar to a flattened incline, we need to consider the geometry of the sonar’s conical detection beam for efficient coverage. As the sonar sweeps across the seabed, its detection beam forms an elliptical projection on the ocean floor (Fig. 12). The maximum coverage width can be achieved as the major axis of the elliptical projection coincides with the sonar’s horizontal beam spread.

<!-- b000400 | prose | pages [17] -->
The key observation is that when a search ship equipped with sonar moves perpendicular to the geographical gradient (along isobath), the coverage width will reach its maximum and will form the largest coverage area during the movement, thus saving the most time. The aforementioned searching pattern is visualized in Fig.14 As the search progresses, paths with lower likelihoods are eliminated, and the corresponding particles are excluded from further consideration by the Kalman filter. Then, based on the current distribution of particles, a corresponding number of new particles are generated in high-probability zones to participate in further iterations of the model.

<!-- b000401 | heading | pages [17] -->
5.4 Results

<!-- b000402 | prose | pages [17] -->
Based on the predictions from the Kalman filter, we can calculate the current feasible zone, as shown in Fig. 13.

<!-- b000403 | caption | pages [17] -->
Figure 13: Temporal distribution probability heatmap of the defective submersible

<!-- b000404 | prose | pages [17, 18] -->
关注数学模型 The initial deployment of the rescue vessel should be where the defective submersible transmit its last signal.

<!-- b000405 | furniture | pages [17] -->
2

<!-- b000406 | furniture | pages [17] -->
MATHmodels

<!-- b000407 | furniture | pages [17] -->
获取更多资讯

<!-- b000408 | furniture | pages [18] -->
Team 2425792

<!-- b000409 | furniture | pages [18] -->
Page 17 of 24

<!-- b000411 | prose | pages [18] -->
Subsequently, search and rescue vessels equipped with the Teledyne Marine Sonar system are dispatched to the potential feasible zones to conduct isobath searches. 微信公众号：数学模型 微信号：MATHmodels

<!-- b000412 | caption | pages [18] -->
Figure 14: Isobath Search strategy

<!-- b000413 | prose | pages [18] -->
Furthermore, we refine the model by implementing supplementary Kalman filters that account for particle dispersion, resulting in the identification of multiple probable search areas. It is advisable to deploy a number of search and rescue vessels to these areas and, depending on their respective probabilities, methodically inspect the regions along isopath. Presented below is a heatmap that accurately tracks three such particles:

<!-- b000414 | caption | pages [18] -->
Figure 15: Heatmap of Three-Particle Dispersion Based on the Kalman filter

<!-- b000415 | prose | pages [18] -->
关注数学模型

<!-- b000416 | furniture | pages [18] -->
2

<!-- b000417 | furniture | pages [18] -->
MATHmodels

<!-- b000418 | furniture | pages [18] -->
获取更多资讯

<!-- b000419 | furniture | pages [19] -->
Team 2425792

<!-- b000420 | furniture | pages [19] -->
Page 18 of 24

<!-- b000421 | heading | pages [19] -->
5.5 Analysis of the Results

<!-- b000422 | prose | pages [19] -->
The utilization of the Kalman filter for predicting the feasible zone has proven to be an effective method in determining the probable location of the drifting submersible over time. The temporal 微信公众号：数学模型 probability heatmap (Fig. 13) provides a visual representation of the distribution of probabilities, indicating where the submersible is most likely to be found at different times.

<!-- b000423 | prose | pages [19] -->
As depicted in Fig. 14, the methodical positioning of search and rescue vessels leverages the maximization of sonar swath width to optimize the coverage of the designated search zone. This strategic approach serves to decrease the length of the search path, thereby diminishing the duration necessary to thoroughly survey the area.

<!-- b000424 | heading | pages [19] -->
6 Task 4: Model extrapolation

<!-- b000425 | heading | pages [19] -->
6.1 Caribbean Sea

<!-- b000426 | prose | pages [19] -->
微信号：MATHmodels In the former case, we have already examined the Ionian Sea. Our analysis revealed three significant characteristics of the sea that markedly influence the trajectory of a malfunctioning submersible: ocean currents, seafloor landscape, and variations in seawater density.

<!-- b000427 | prose | pages [19] -->
Therefore, as we transition our model to the case of the Caribbean Sea, our initial step entails modeling the marine environment of the Caribbean Sea.

<!-- b000428 | prose | pages [19] -->
Currents: The Caribbean Sea experiences a range of currents and turbulence, influenced by wind patterns and the interaction of water with underwater topography. Strong currents can challenge the submersible’s propulsion system and dramatically affect its path, requiring more sophisticated navigation algorithms to compensate for drift. Turbulence can introduce noise to sensor measurements, particularly for IMUs, complicating the task of accurate state estimation.

<!-- b000429 | caption | pages [19] -->
Figure 16: Ocean current maps: Caribbean Sea(Left) and Ionian Sea(right)

<!-- b000430 | prose | pages [19] -->
Landscape: The Caribbean Sea’s bathymetry, marked by sharp gradients and diversity, includes features like abyssal plains and coral reefs, affecting hydrodynamics and complicating navigation. In contrast, the Ionian Sea’s uniform bathymetry offers a predictable setting for submersible activities. In the Caribbean, submersibles are at greater risk of seabed collision due to the intricate topography and active currents, increasing the chances of entrapment when malfunctioning.

<!-- b000431 | prose | pages [19, 20] -->
关注数学模型 微信公众号：数学模型

<!-- b000432 | furniture | pages [19] -->
2

<!-- b000433 | furniture | pages [19] -->
MATHmodels

<!-- b000434 | furniture | pages [19] -->
获取更多资讯

<!-- b000435 | furniture | pages [20] -->
Team 2425792

<!-- b000436 | furniture | pages [20] -->
Page 19 of 24

<!-- b000438 | caption | pages [20] -->
Figure 17: Underwater geography maps: Caribbean Sea(Left) and Ionian Sea(right)

<!-- b000439 | prose | pages [20] -->
For submersible deployment in the Caribbean, it is imperative to integrate advanced fault management protocols and terrain-following algorithms to navigate this intricate landscape. sub- mersibles should be equipped with precise bathymetric mapping capabilities and sensors for real- time terrain assessment to circumvent topographic obstacles. Implementing contingency strategies for system failures is also vital to minimize the risks associated with the Caribbean’s challenging underwater conditions.

<!-- b000440 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000441 | heading | pages [20] -->
6.2 Coorporation strategy between multiple submersibles

<!-- b000442 | prose | pages [20] -->
Voronoi diagrams are a mathematical concept used to divide a space into regions such that each point in a region is closer to its designated seed point than to any other. In the context of cooperative submarine drones, each drone can be considered a seed point, and any location in the space is associated with the drone closest to it. This method allows for the effective management of the distances between drones, ensuring they are evenly distributed across the operational area.

<!-- b000443 | prose | pages [20] -->
Submarines move according to the following rules to maintain an optimal distance:

<!-- b000444 | prose | pages [20] -->
• Every submersibles stay in its own zone.

<!-- b000445 | prose | pages [20] -->
• If the submarine detects that neighboring submarines are too close, it will adjust its position to increase the distance.

<!-- b000446 | prose | pages [20] -->
Detection and Response to Drone Failures once a drone goes offline (i.e., beyond communica- tion range), its neighboring drones are immediately notified. These drones then:

<!-- b000447 | prose | pages [20] -->
• Initiate the previous searching model, using sonar to scan for the possible location of the disconnected drone.

<!-- b000448 | prose | pages [20] -->
• Upon locating the disconnected drone, approach and establish a temporary communication link.

<!-- b000449 | prose | pages [20] -->
• Continuously report the position and status of the malfunctioning drone to the main vessel.

<!-- b000450 | caption | pages [20] -->
Figure 18: Neighbouring submersibles(green) approaching to monitor the power-failed one(red)

<!-- b000451 | prose | pages [20] -->
关注数学模型

<!-- b000452 | furniture | pages [20] -->
2

<!-- b000453 | furniture | pages [20] -->
MATHmodels

<!-- b000454 | furniture | pages [20] -->
获取更多资讯

<!-- b000455 | furniture | pages [21] -->
Team 2425792

<!-- b000456 | furniture | pages [21] -->
Page 20 of 24

<!-- b000457 | heading | pages [21] -->
7 Sensitivity Analysis and Error Analysis

<!-- b000458 | prose | pages [21] -->
In order to analyze the impact of various factors on the submersible’s position prediction model, we have adopted a comprehensive approach: evaluating sensitivity by comparing the cosine 微信公众号：数学模型 similarity of the submersible’s path before and after variable perturbations, and quantifying the prediction error. We consider the following varying parameters: seawater density (ρ), external environmental disturbances represented by current force (Fcurrent), propeller rotation speed (n), and the mass of the submersible (m). The ultimate goal is to minimize prediction error, thereby enhancing the accuracy of the path prediction.

<!-- b000459 | prose | pages [21] -->
Cosine similarity, a metric ranging from -1 to 1, quantifies the directional similarity between two vectors. Prediction error is quantified as the root mean square error (RMSE) between the predicted and actual paths. We conducted the simulation in MATLAB over 1000 iterations with a step size of 0.1 second. Cosine similarity measures the alignment between the actual path and the predicted path of the submersible, while the RMSE provides a scalar value of the average deviation magnitude from the actual path.

<!-- b000460 | prose | pages [21] -->
Variable ID Perturbed Similarity Similarity Change Sensitivity Prediction Error (RMSE) 微信号：MATHmodels ρ 0.94 -0.06 High 1.55 m Fcurrent 0.93 -0.07 High 2.10 m n 0.98 -0.02 Low 1.12 m m 0.95 -0.05 Medium 1.17 m

<!-- b000461 | caption | pages [21] -->
Table 4: Path cosine similarity and prediction error after model parameter perturbations

<!-- b000462 | prose | pages [21] -->
The results suggest that seawater density and external environmental disturbances significantly affect the submersible’s path prediction accuracy, as indicated by high sensitivity and large prediction errors, while propeller rotation speed and submersible mass have a lower impact.

<!-- b000463 | prose | pages [21] -->
To visually represent the influence of parameter variability on the accuracy of the submersible’s path prediction, we have plotted the actual versus predicted trajectories in a 3D MATLAB sim- ulation. This graphical depiction serves as an alternative method to convey the sensitivity and error metrics, with deviations between the trajectories directly corresponding to the magnitude of prediction error and sensitivity to parameter changes.

<!-- b000464 | caption | pages [21] -->
Figure 19: A comparison of predicted (green) and actual (blue) locations under different levels of

<!-- b000465 | prose | pages [21] -->
environmental turbulence, as modulated by the variance parameter α.

<!-- b000466 | prose | pages [21] -->
From the visualization, it’s apparent that despite significant increases in turbulence, our model maintains a smooth prediction trajectory, demonstrating a relatively high degree of robustness against uncertainty.

<!-- b000467 | prose | pages [21] -->
关注数学模型

<!-- b000468 | furniture | pages [21] -->
2

<!-- b000469 | furniture | pages [21] -->
MATHmodels

<!-- b000470 | furniture | pages [21] -->
获取更多资讯

<!-- b000471 | furniture | pages [22] -->
Team 2425792

<!-- b000472 | furniture | pages [22] -->
Page 21 of 24

<!-- b000473 | heading | pages [22] -->
8 Evaluation and Promotion of Model

<!-- b000474 | heading | pages [22] -->
8.1 Strengths

<!-- b000475 | prose | pages [22] -->
微信公众号：数学模型 1. The model is well-designed to accommodate varying geographic and environmental factors, thus ensuring applicability across regions with diverse terrains beyond just the Ionian Sea.

<!-- b000476 | prose | pages [22] -->
2. Demonstrating high scalability, our fundamental assumptions do not restrict possible enhancements. As such, our model serves as an asset providing foundational structure for further advanced adaptations.

<!-- b000477 | prose | pages [22] -->
3. The user-friendly nature of our model demands only minimal fine-tuning of a few hyper- parameters.

<!-- b000478 | prose | pages [22] -->
4. The close-to-reality design of our model derives from comprehensive data fusion utiliz- ing various sensors in conjunction with the sophisticated Computational Fluid Dynamics (CFD) equation.

<!-- b000479 | prose | pages [22] -->
5. We consider an extensive and versatile array of measuring instruments contributing to the 微信号：MATHmodels completeness of our approach.

<!-- b000480 | prose | pages [22] -->
6. To effectively address the inherent non-linearity of dynamics, the Kalman Filter simultane- ously maintains multiple possible trajectories rather than only one possibility.

<!-- b000481 | heading | pages [22] -->
8.2 Weaknesses and Possible Improvements

<!-- b000482 | prose | pages [22] -->
1. Given the inherently chaotic characteristics of CFD, there’s a requirement for establishing a more judicious method concerning the generation and exclusion of unlikely trajectories.

<!-- b000483 | prose | pages [22] -->
2. It may be beneficial to adopt a probability-based strategy instead of deterministic searching. This could potentially maximize the utilization of accumulated search results, which in turn would open up scopes for overall improvement [9].

<!-- b000484 | heading | pages [22] -->
References

<!-- b000485 | references | pages [22] -->
[1] Cui, W. An Overview of Submersible Research and Development in China. J. Marine. Sci.

<!-- b000486 | references | pages [22] -->
Appl. 17, 459–470 (2018). https://doi.org/10.1007/s11804-018-00062-6

<!-- b000487 | references | pages [22] -->
[2] Kohnen,

<!-- b000488 | references | pages [22] -->
W.

<!-- b000489 | references | pages [22] -->
2007

<!-- b000490 | references | pages [22] -->
MTS

<!-- b000491 | references | pages [22] -->
Overview

<!-- b000492 | references | pages [22] -->
of

<!-- b000493 | references | pages [22] -->
Manned

<!-- b000494 | references | pages [22] -->
Underwater

<!-- b000495 | references | pages [22] -->
Vehicle

<!-- b000496 | references | pages [22] -->
Activity.”

<!-- b000497 | references | pages [22] -->
Marine

<!-- b000498 | references | pages [22] -->
Technology

<!-- b000499 | references | pages [22] -->
Society

<!-- b000500 | references | pages [22] -->
Journal

<!-- b000501 | references | pages [22] -->
42,

<!-- b000502 | references | pages [22] -->
no.

<!-- b000503 | references | pages [22] -->
1

<!-- b000504 | references | pages [22] -->
(March

<!-- b000505 | references | pages [22] -->
1,

<!-- b000506 | references | pages [22] -->
2008):

<!-- b000507 | references | pages [22] -->
26–37.

<!-- b000508 | references | pages [22] -->
https://doi.org/10.4031/002533208786861236.

<!-- b000509 | references | pages [22] -->
[3] Wikipedia contributors. Titan submersible implosion. https://en.wikipedia.org/wiki/

<!-- b000510 | references | pages [22] -->
Titan_submersible_implosion

<!-- b000511 | references | pages [22] -->
[4] Basic Principles of Inertial Navigation Seminar on inertial navigation systems. AeroStu-

<!-- b000512 | references | pages [22] -->
dents.com. Tampere University of Technology, page 5

<!-- b000513 | references | pages [22] -->
[5] Fossen T I. Handbook of marine craft hydrodynamics and motion control [M]. John Wiley

<!-- b000514 | references | pages [22] -->
and Sons, 2011.

<!-- b000515 | references | pages [22] -->
关注数学模型

<!-- b000516 | furniture | pages [22] -->
2

<!-- b000517 | furniture | pages [22] -->
MATHmodels

<!-- b000518 | furniture | pages [22] -->
获取更多资讯

<!-- b000519 | furniture | pages [23] -->
Team 2425792

<!-- b000520 | furniture | pages [23] -->
Page 22 of 24

<!-- b000521 | references | pages [23] -->
[6] C¸ engel, Y. A.; Boles, M. A. Instructor Solutions Manual for Thermodynamics: An Engineer-

<!-- b000522 | references | pages [23] -->
ing Approach; [John Wiley and Sons]: [2015]

<!-- b000523 | references | pages [23] -->
[7] S. Neil Rasband, Chaotic Dynamics of Nonlinear Systems Dover Books on Physics, Courier

<!-- b000524 | references | pages [23] -->
微信公众号：数学模型

<!-- b000525 | references | pages [23] -->
Dover Publications, 2015, ISBN 978-0486795997.

<!-- b000526 | references | pages [23] -->
Deep

<!-- b000527 | references | pages [23] -->
Water

<!-- b000528 | references | pages [23] -->
Echosounder,

<!-- b000529 | references | pages [23] -->
[8] Teledyne

<!-- b000530 | references | pages [23] -->
Marine,

<!-- b000531 | references | pages [23] -->
Teledyne

<!-- b000532 | references | pages [23] -->
Marine,

<!-- b000533 | references | pages [23] -->
Available:

<!-- b000534 | references | pages [23] -->
https://www.teledynemarine.com/en-us/products/product-line/Pages/

<!-- b000535 | references | pages [23] -->
Deep-Water-Echosounder.aspx.

<!-- b000536 | references | pages [23] -->
[9] D. Agbissoh OTOTE, B. Li, B. Ai, S. Gao, J. Xu, X. Chen, and G. Lv, ”A Decision-Making

<!-- b000537 | references | pages [23] -->
Algorithm for Maritime Search and Rescue Plan,” Sustainability, vol. 11, no. 7, p. 2084, 2019.

<!-- b000538 | references | pages [23] -->
[Online]. Available: https://doi.org/10.3390/su11072084

<!-- b000539 | references | pages [23] -->
微信号：MATHmodels

<!-- b000540 | references | pages [23] -->
关注数学模型

<!-- b000541 | furniture | pages [23] -->
2

<!-- b000542 | furniture | pages [23] -->
MATHmodels

<!-- b000543 | furniture | pages [23] -->
获取更多资讯

<!-- b000544 | furniture | pages [24] -->
Team 2425792

<!-- b000545 | furniture | pages [24] -->
Page 23 of 24

<!-- b000546 | heading | pages [24] -->
Memo for the Greek Government

<!-- b000547 | prose | pages [24] -->
TO: Myron Flouris - Secretary General for Tourism Policy and Development 微信公众号：数学模型 CC: Olga Kefalogianni - Minister of Tourism, Ministry of Tourism (Greece) FROM: MCM Team 2425792 DATE: February 5, 2024 SUBJECT: Locate

<!-- b000548 | prose | pages [24] -->
Dear officials,

<!-- b000549 | prose | pages [24] -->
It is with distinct honor that I introduce to you our meticulously crafted model specifi- cally designed for the Maritime Cruises Mini-Submarines (MCMS). This esteemed corpo- ration displays a profound interest in the maritime relics located in the depths of the Ionian Sea—a priceless cultural heritage. These submerged vestiges stand as silent testaments 微信号：MATHmodels to seafaring undertakings spanning across various epochs of history, which inclues naval vessels from the ancient Roman and Greek eras, mercantile ships hailing from the medieval period, in addition to military and commercial maritime craft that met their watery demise amidst the throes of WWI and WWII. For this reason, MCMS envisions these historical remnants as focal points of intrigue for the submersible tourists, thereby initiating plans to develop tourism via submersibles.

<!-- b000550 | prose | pages [24] -->
Nevertheless, the pursuit of these submerged archaeological riches carries its fair share of complications. The situation is of high complexity as these relics are nestled deep within the oceanic abyss where there could be potential risks encompassing dynamic currents, poor communication signals, and intricate sea floor geography.

<!-- b000551 | prose | pages [24] -->
As a result, in an effort to secure the safety of tourists, a thorough study of submersible localizing and searching within the depths of the ocean is necessitated, so as to promptly perform rescue operations in case of an incident. MCMS has entrusted our team with the task of modelling the process of submersible localization and search.

<!-- b000552 | heading | pages [24] -->
Modelling

<!-- b000553 | prose | pages [24] -->
Localization—Uncertainty Reduc-

<!-- b000554 | heading | pages [24] -->
The core concept of our model consists of:

<!-- b000555 | prose | pages [24] -->
tion—Search and Rescue.

<!-- b000556 | prose | pages [24] -->
Localization: Given that the Ionian Sea reaches depths of up to 5267 meters, traditional methods of tracking submersibles become impracticable. Thus, we opt to employ an Inertial Localization System for positioning. With certain adjustments to Fossen’s Six Degrees of Freedom model, a Computational Fluid Dynamics equation is established to represent the dynamics of submersible in the complex marine environment, with which the submersible’s trajectory could be calculated.

<!-- b000557 | prose | pages [24] -->
Uncertainty Reduction: However, inherent cumulative errors in the Inertial Measure- ment Unit (IMU) and the localization model necessitate further refinement. Therefore, we employ the Kalman filter for corrections of the submersible’s location and predictions in

<!-- b000558 | prose | pages [24, 25] -->
关注数学模型 case of lost connectivity.

<!-- b000559 | furniture | pages [24] -->
2

<!-- b000560 | furniture | pages [24] -->
MATHmodels

<!-- b000561 | furniture | pages [24] -->
获取更多资讯

<!-- b000562 | furniture | pages [25] -->
Team 2425792

<!-- b000563 | furniture | pages [25] -->
Page 24 of 24

<!-- b000565 | prose | pages [25] -->
Search and Rescue: Should the submersible lose contact and cease to transmit signs, it will autonomously shut down its power system. The host ship will then utilize the ongoing 微信公众号：数学模型 predictions generated by the Kalman filter to determine the probability of the submersible to appear at various points in the ocean. Rescues will consequently be initiated by the rescue vessels sent by the host ship based on the method of isobathic searching, a common marine rescue procedure.

<!-- b000566 | prose | pages [25] -->
Proposal for the Equipment Onboard

<!-- b000567 | prose | pages [25] -->
In order to enhance the capacity and efficiency of our localization and search operations, it is incumbent upon us to equip advanced equipment onboard. A comprehensive study and analysis of available equipment in the marine sector is conducted, employing the robust method of Principal Component Analysis (PCA), a process allowing the evaluation and selection of the equipment most suitable for deployment based upon a variety of performance parameters. 微信号：MATHmodels Included among the recommended equipment to be onboard the host ship are the Perry Slingsby Multi-Beam, Perry Slingsby Side Scan Sonar, and Divex AUV-1000. Each device has been selected based on its particular strengths, spanning from high-resolution, three- dimensional sonographic visualization to wide-area detection coverage and autonomous operations at considerable depths.

<!-- b000568 | heading | pages [25] -->
Extrapolation of the Model

<!-- b000569 | prose | pages [25] -->
Our model boasts a high degree of portability, enabling it to perform localization and search operations across diverse marine environments. The allocation of surface work zones is designed to maximize the rapid response of nearby submarines to an incident site, while maintaining safe distances between them. This approach ensures that in an accident, support submarines can quickly reach the scene and continuously monitor the signal from the defective vessel.

<!-- b000570 | prose | pages [25] -->
In conclusion, our model presents a comprehensive solution for securing the safety of tourists on the submersible. By embracing this model, the government can pave the way for the development of submersible tourism, enabling visitors to witness the rich history and cultural significance preserved beneath the ocean’s surface.

<!-- b000571 | prose | pages [25] -->
We humbly request the government’s support and approval for the implementation of this solution, as it will not only safeguard the lives of submersible tourists, but also contribute to the preservation and exploration of the priceless cultural heritage submerged in the Ionian Sea.

<!-- b000572 | prose | pages [25] -->
关注数学模型

<!-- b000573 | furniture | pages [25] -->
2

<!-- b000574 | furniture | pages [25] -->
MATHmodels

<!-- b000575 | furniture | pages [25] -->
获取更多资讯
