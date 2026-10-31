# P-B-2021-2116496-6a60d0e7

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | furniture | pages [1] -->
2021

<!-- b000003 | prose | pages [1] -->
Problem Chosen

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
B

<!-- b000007 | furniture | pages [1] -->
2116496

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | title | pages [1] -->
Drone System  VS  Wildfire

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
The 2019-2020 fire season in Australia has a huge impact on New South Wales and Eastern Victoria, forcing people to seek urgent solutions. However, in recent years, drones are used to assist in the observation and communication of rescuing fires. To better improve the rescue efficiency of drones, a Drone Arrangement Model is proposed to solve the current dilemma.

<!-- b000013 | prose | pages [1] -->
For problem 1, we establish a drone system consisting of EOCs, front-line personnel, SSA and repeater drones. Step I: To better predict the fire situation, we firstly pre-deploy the front-liners according to the known or possible fire locations which are estimated by the Gaussian Mixed Model (GMM). Step II: Using the k-means algorithm, we determine the locations of EOCs, ensuring the maximum safety and observation of front-line personnel and fires. Step III: In order to solve the problem of communication between personnel and EOCs, as well as minimize the economic cost, we obtain the minimum spanning tree near each EOC, which provides the

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
shortest signal transmission channel for repeaters, and solve the problem of minimizing the number of repeaters. Step IV: We propose two different cruise strategies for SSA drones to minimize the economic costs and reduce the risk of fires. Finally, an effectiveness function considering capability, safety, economics, and observation is determined, where the coefficients between the various indicators are determined by the AHP model.

<!-- b000016 | prose | pages [1] -->
For step I, our personnel distribution is based on the size and frequency of fires in a period of time, which can reflect the capability of a fire rescue to a certain extent. For step II, the location of the EOC creates unsafety and unobservability of personnel and fires, and the construction cost of EOC also needs to be taken into consideration. For step III, the establishment of the minimum spanning tree determines the economic effect brought by the repeaters, and the communication is well guaranteed. For step IV, the number of SSA is determined by a parameter about the minimum fire tolerance time in this step, where this parameter also affects the safety of fire and the economy brought by SSA. We optimize the data of two different months, and get optimal results: the numbers of the repeaters and SSA are 73, 80 and 80, 104 for November and December in 2019, respectively.

<!-- b000017 | prose | pages [1] -->
For problem 2, in order to investigate the effect of extreme fire events, we introduce the GM model to predict the environment condition over the next decade by the temperature and precipitation data from 2011-2020. The prediction shows that year 2030 owns the worst situation. Based on it, we analyze the extreme fire events with three types: Widespread fires occurring at higher probability cause a huge change in EOC costs increasing by 46.15%; Small fires with high frequency affect SSA costs increasing by 98.08% dramatically; Explosive fires in an unpredictable manner have a strong effect on Repeater costs increasing by 53.75%.

<!-- b000018 | prose | pages [1] -->
For problem 3, we introduce altitude data to simulate different terrains, which extends our model to the three- dimension space. The result shows that both SSA drones and repeater drones are limited by varied terrains. The distributions in a two-dimension plane and three-dimensional arrangement are shown to illustrate the optimal locations of repeater drones. The result shows that the repeater drones at high altitude are more intensive.

<!-- b000019 | prose | pages [1] -->
Sensitivity analysis shows the strong robustness under the impact of the changing fire size and observation time (tolerance time), and we obtain the optimal solutions about the number of EOC. Although we get comprehensive and multifaceted optimization results, the efficiency of counter to the extreme fire events still need to be improved.

<!-- b000020 | keywords | pages [1] -->
Keywords:; Drone Arrangement Model; K-means Model; Minimum Spanning Tree Model; GM Model;

<!-- b000021 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000022 | furniture | pages [1] -->
关注数学模型

<!-- b000023 | furniture | pages [1] -->
2

<!-- b000024 | furniture | pages [1] -->
MATHmodels

<!-- b000025 | furniture | pages [1] -->
获取更多资讯

<!-- b000026 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000027 | furniture | pages [2] -->
Team # 2116496                                                              Page 1 of  24

<!-- b000028 | furniture | pages [2] -->


<!-- b000029 | heading | pages [2] -->
Contents

<!-- b000030 | heading | pages [2] -->
1. Introduction ········································································································ 2

<!-- b000031 | prose | pages [2] -->
1.1 Background ····································································································· 2

<!-- b000032 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000033 | prose | pages [2] -->
1.2 Restatement of the Problem ··················································································· 2 1.3 Our Work ········································································································ 2

<!-- b000034 | heading | pages [2] -->
2. Assumptions and Justifications ················································································· 2

<!-- b000035 | heading | pages [2] -->
3. Notations ············································································································ 3

<!-- b000036 | heading | pages [2] -->
4. Model I: Drone Arrangement Model ·········································································· 4

<!-- b000037 | prose | pages [2] -->
4.1 Local Assumptions ····························································································· 4 4.2 Basic ideas and Method ······················································································· 4 4.2.1 Basic Ideas ··································································································································· 4 4.2.2 Method ········································································································································· 4 4.3 Data Processing ································································································· 5

<!-- b000038 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000039 | prose | pages [2] -->
4.4 Step I: Forecast Deployment of Front-line Personnel ······················································ 6 4.5 Step II: Decision on the Locations of the EOCs ···························································· 7 4.6 Step III: Deployment of Hovering Repeaters ······························································· 8 4.6.1 Channel Plan ································································································································ 9 4.6.2 Repeater Plan ······························································································································· 9 4.7 Step IV: Design of SSA Monitor Strategy ································································· 10 4.8 Rescue Effectiveness ·························································································· 12 4.8.1 Effectiveness Indicators ············································································································· 12 4.8.2 Effectiveness Function ··············································································································· 12 4.9 Results ·········································································································· 12 4.9.1 Estimation of Weights ················································································································ 12 4.9.2 Calculation Results ···················································································································· 13

<!-- b000040 | heading | pages [2] -->
5. Model II: Extreme Condition Arrangement Model ························································ 14

<!-- b000041 | prose | pages [2] -->
5.1 Prediction of Fire Conditions ················································································ 14 5.2 Extreme Fire Events ·························································································· 15 5.3 Calculation Results ···························································································· 16

<!-- b000042 | heading | pages [2] -->
6. Model III: Repeater Location Optimization Model ························································ 17

<!-- b000043 | prose | pages [2] -->
6.1 Analysis of Terrain Impact ··················································································· 17 6.2 Calculation Results ···························································································· 18

<!-- b000044 | heading | pages [2] -->
7. Sensitivity Analysis ······························································································· 20

<!-- b000045 | heading | pages [2] -->
8. Strengths and Weaknesses ······················································································ 22

<!-- b000046 | prose | pages [2] -->
8.1 Strengths ········································································································ 22 8.2 Weakness ······································································································· 22

<!-- b000047 | heading | pages [2] -->
9. Conclusion ········································································································· 22

<!-- b000048 | heading | pages [2] -->
10. Continue to Work ······························································································· 23

<!-- b000049 | heading | pages [2] -->
11. Reference ········································································································· 23

<!-- b000050 | heading | pages [2] -->
12. Budget Request ·································································································· 24

<!-- b000051 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000052 | furniture | pages [2] -->
关注数学模型

<!-- b000053 | furniture | pages [2] -->
2

<!-- b000054 | furniture | pages [2] -->
MATHmodels

<!-- b000055 | furniture | pages [2] -->
获取更多资讯

<!-- b000056 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000057 | furniture | pages [3] -->
Team # 2116496                                                              Page 2 of  24

<!-- b000058 | furniture | pages [3] -->


<!-- b000059 | furniture | pages [3] -->


<!-- b000060 | heading | pages [3] -->
1. Introduction

<!-- b000061 | heading | pages [3] -->
1.1 Background

<!-- b000062 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000063 | prose | pages [3] -->
The 2019-2020 season has been one of the worst fire seasons in Australia on record, especially for New South Wales and Eastern Victoria. By 2019, the combination of long-term warming, insufficient rainfall and abnormal ocean circulation made Australia’s ground conditions extremely susceptible to fires. Not only a large number of forests were burnt down, but the ecological diversity was also severely damaged. Therefore, it is very necessary for Australia to take effective measures and actions for fighting wildfires. However, for the time being, the use of drones is a common means of monitoring fire, and in conjunction with other equipment. In order to balance the relationship between the efficiency of firefighting and the cost, it is significant to arrange the drone system reasonably and effectively [1].

<!-- b000064 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000065 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000066 | prose | pages [3] -->
Our specific tasks include the following:

<!-- b000067 | prose | pages [3] -->
(1) Build a model to determine the optimal numbers and the proportion of assigned number of

<!-- b000068 | prose | pages [3] -->
SSA drones and Radio Repeater drones for “Rapid Bushfire Response”.

<!-- b000069 | prose | pages [3] -->
(2) Illustrate the adaptability of our model to extreme situations and predict the increased costs

<!-- b000070 | prose | pages [3] -->
when the changing likelihood of extreme fire events occurs over the next decade.

<!-- b000071 | prose | pages [3] -->
(3) Optimize the locations of hovering VHF/UHF radio-repeater drones for different terrains and

<!-- b000072 | prose | pages [3] -->
different sizes of fires in the Victorian region.

<!-- b000073 | heading | pages [3] -->
1.3 Our Work

<!-- b000074 | prose | pages [3] -->
The topic requires us to determine the rational optimization of drones in different situations. Our work mainly includes the following:

<!-- b000075 | prose | pages [3] -->
Based on the terrains of Eastern Victoria and South Wales, a dual internal and external ⚫ optimization model for drone arrangement is established;

<!-- b000076 | prose | pages [3] -->
In the face of extreme cases of fire, we characterize the flexible adaptability of our model and ⚫ give relevant results, and calculate the future cost increase;

<!-- b000077 | prose | pages [3] -->
Based on the previous model, a more general and stable model is developed to optimize the ⚫ location of the repeaters on East Victoria and show the specific locations vividly and clearly;

<!-- b000078 | prose | pages [3] -->
Prepare an one page annotated Budget Request for CFA to submit to the Victoria State Govern- ⚫ ment.

<!-- b000079 | heading | pages [3] -->
2. Assumptions and Justifications

<!-- b000080 | prose | pages [3] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified. Other assumptions may not be as follows, but will be put forward in the model later.

<!-- b000081 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000082 | furniture | pages [3] -->
关注数学模型

<!-- b000083 | furniture | pages [3] -->
2

<!-- b000084 | furniture | pages [3] -->
MATHmodels

<!-- b000085 | furniture | pages [3] -->
获取更多资讯

<!-- b000086 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000087 | furniture | pages [4] -->
Team # 2116496                                                              Page 3 of  24

<!-- b000088 | furniture | pages [4] -->


<!-- b000089 | prose | pages [4] -->
Assumption 1: The occurrence of a fire is predictable. ⚫  Justification: Although the occurrence of forest fires is random, we assume the possible fire

<!-- b000090 | prose | pages [4] -->
location can be predicted by the weather conditions and locations of frequent outbreaks in the past.

<!-- b000091 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000092 | prose | pages [4] -->
Assumption 2: More than one EOC is located in the southeast corner of Australia. ⚫  Justification: Since the given range of the southeast corner of Australia is from 140.8°E  to

<!-- b000093 | prose | pages [4] -->
153.6°E, where the horizontal span is too large for a single EOC to support. So we assume that multiple EOCs can be built to meet the support requirements.

<!-- b000094 | prose | pages [4] -->
Assumption 3: Fire caused by malicious destruction is not considered during the wildfires in ⚫ the scope of research.  Justification: In addition to the known fire points, our model is also suitable for predictable

<!-- b000095 | prose | pages [4] -->
fire locations, and rely on the analyzed location for deployment arrangements in a way. Therefore, unpredictable malicious fire causes can be ignored.

<!-- b000096 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000097 | prose | pages [4] -->
Assumption 4: All drones & equipment and EOC are reliable for fire rescue without con- ⚫ sidering biological death and injury.  Justification: Since forest rescue is an urgent issue, which determines the safety of the

<!-- b000098 | prose | pages [4] -->
ecology and economy, and some serious losses are immeasurable. Therefore, we believe that our drones & equipment and EOC are completely reliable in our model and the loss of life is not as a measure of the effectiveness in our response.

<!-- b000099 | prose | pages [4] -->
Assumption 5: Assume the research data is accurate. ⚫  Justification: We assume that economic costs for EOCs and drones do not show obvious

<!-- b000100 | prose | pages [4] -->
measurable deviation, so we can establish a more reasonable model based on it.

<!-- b000101 | heading | pages [4] -->
3. Notations

<!-- b000102 | prose | pages [4] -->
For convenience, we introduce some important notations below.

<!-- b000103 | heading | pages [4] -->
Notations

<!-- b000104 | prose | pages [4] -->
Explanations

<!-- b000105 | prose | pages [4] -->
The number of equipment or personnel 𝑁𝑖

<!-- b000106 | prose | pages [4] -->
The coefficient of personnel deployment 𝑘𝑖

<!-- b000107 | prose | pages [4] -->
The size of each fire point 𝐴𝑖

<!-- b000108 | prose | pages [4] -->
The frequency of fires 𝑓

<!-- b000109 | prose | pages [4] -->
The fairness frequency expected 𝑝𝑖

<!-- b000110 | prose | pages [4] -->
The total cost of equipment 𝑊𝑖

<!-- b000111 | prose | pages [4] -->
The effectiveness function 𝐸

<!-- b000112 | furniture | pages [4] -->


<!-- b000113 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000114 | furniture | pages [4] -->
关注数学模型

<!-- b000115 | furniture | pages [4] -->
2

<!-- b000116 | furniture | pages [4] -->
MATHmodels

<!-- b000117 | furniture | pages [4] -->
获取更多资讯

<!-- b000118 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000119 | furniture | pages [5] -->
Team # 2116496                                                              Page 4 of  24

<!-- b000120 | furniture | pages [5] -->


<!-- b000121 | heading | pages [5] -->
4. Model I: Drone Arrangement Model

<!-- b000122 | heading | pages [5] -->
4.1 Local Assumptions

<!-- b000123 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000124 | prose | pages [5] -->
VHF/UHF signals can be continuously amplified by two repeaters (or more, of course, one is ⚫ perfectly fine too), and the energy loss between these two can be ignored. In other words, as long as any repeater receives electromagnetic waves, it can amplify and propagate the signal according to its own unique propagation range.

<!-- b000125 | prose | pages [5] -->
As most of the front-line personnel are highly qualified and experienced, it can be assumed ⚫ that they are in the vicinity of areas where fires have occurred or are likely to occur. This allows for a faster response to fire-fighting rescue and thus reduces ecological and economic damage.

<!-- b000126 | heading | pages [5] -->
4.2 Basic ideas and Method

<!-- b000127 | heading | pages [5] -->
4.2.1 Basic Ideas

<!-- b000128 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000129 | prose | pages [5] -->
According to the various equipment and places, as well as their functions given in the problem, we make the following explanations:

<!-- b000130 | prose | pages [5] -->
(1) EOC: A place that can launch SSA drones and receive their signals instantaneously, and can

<!-- b000131 | prose | pages [5] -->
also communicate with the front-line personnel through a repeater;

<!-- b000132 | prose | pages [5] -->
(2) Front-line personnel: Personnel with the device detectable for SSA drone(s) near the EOC;

<!-- b000133 | prose | pages [5] -->
(3) SSA: A kind of drone that extrapolate the nearby situation around the personnel who wear the

<!-- b000134 | prose | pages [5] -->
detectable devices, and then feedback to the EOC;

<!-- b000135 | prose | pages [5] -->
(4) Repeater: A kind of hovering drone that maintain communication between personnel and EOC

<!-- b000136 | prose | pages [5] -->
by amplifying the signal.

<!-- b000137 | heading | pages [5] -->
4.2.2 Method

<!-- b000138 | prose | pages [5] -->
Once the above ideas are fully made sense, the problem becomes how to efficiently and rationally deploy EOCs and drones in such a fire-prone environment. The exact mechanism can be shown in the following figure.

<!-- b000139 | furniture | pages [5] -->


<!-- b000140 | caption | pages [5] -->
Figure 1  Mechanistic map of the problem

<!-- b000141 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000142 | furniture | pages [5] -->
关注数学模型

<!-- b000143 | furniture | pages [5] -->
2

<!-- b000144 | furniture | pages [5] -->
MATHmodels

<!-- b000145 | furniture | pages [5] -->
获取更多资讯

<!-- b000146 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000147 | furniture | pages [6] -->
Team # 2116496                                                              Page 5 of  24

<!-- b000148 | furniture | pages [6] -->


<!-- b000149 | prose | pages [6] -->
Step I: Forecast Deployment of Front-line Personnel ⚫ According to the local assumption II, the location of frontline personnel can be determined according to the known (or possible) fire locations, so that we can obtain the deployment of front- line personnel over the entire map. In this way, the front-line personnel and the wildfire can be

<!-- b000150 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000151 | prose | pages [6] -->
seen together ‘as a whole’.

<!-- b000152 | prose | pages [6] -->
Step II: Decision on the Locations of the EOCs ⚫ Determine the locations of the EOCs based on the known deployment map of the current front- line personnel. The principle of the determination is to have the front-line personnel covered as much as possible. Based on step I , it is easy to conclude that covering the front-line personnel is approximately the same as including the wildfire in the monitoring.

<!-- b000153 | prose | pages [6] -->
Step III: Deployment of Hovering Repeaters ⚫ After the EOCs’ position have been determined, the repeater position also needs to be considered. Since front-line personnel must communicate with the EOC via a repeater to ensure

<!-- b000154 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000155 | prose | pages [6] -->
safety, which is a mandatory constraint, there must be an optimal arrangement for the locations of the repeaters that maximize the safety of personnel and the timeliness of rescue.

<!-- b000156 | heading | pages [6] -->
Step IV (Internal model): Design of SSA Monitor Strategy

<!-- b000157 | prose | pages [6] -->
⚫ As there is still a link between the EOC and the SSA drone to ensure the non-delay and safety of the wildfire (or arguably the personnel) within the flight range of the SSA drone. Since this step is separate from the others and does not affect each other, we can consider this step separately.

<!-- b000158 | prose | pages [6] -->
However, during these steps, unforeseen circumstances may occur, such as the limited cruise capability of the drone making this fire fighter's timeliness or observation ability limited, or unexpected circumstances that necessitate the addition of new EOC locations or the moving of EOCs resulting in additional financial losses. From the combined metrics of these constraints a relatively optimal drone arrangement can be determined, which is what we need.

<!-- b000159 | heading | pages [6] -->
4.3 Data Processing

<!-- b000160 | prose | pages [6] -->
Fire Conditions ⚫

<!-- b000161 | prose | pages [6] -->
As our problem is based on the period 2019-2020, we investigate the occurrence of wildfires regarding this period in the south-eastern Australia and obtain the data of four months of fires [2]. In the subsequent article, we will select two of them for calculation.

<!-- b000162 | prose | pages [6] -->
Altitude and Topography ⚫ As the signals from both handheld radios carried by front-line personnel and repeaters are affected by the topography, which can be approximately represented by the altitude in south- eastern Australia, we segment the altitude to represent a certain topography within each segment [3]. The elevation map of south-eastern Australia and the distribution of the topography can be processed as the following two figures.

<!-- b000163 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000164 | furniture | pages [6] -->
关注数学模型

<!-- b000165 | furniture | pages [6] -->
2

<!-- b000166 | furniture | pages [6] -->
MATHmodels

<!-- b000167 | furniture | pages [6] -->
获取更多资讯

<!-- b000168 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000169 | furniture | pages [7] -->
Team # 2116496                                                              Page 6 of  24

<!-- b000170 | furniture | pages [7] -->


<!-- b000171 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000172 | caption | pages [7] -->
Figure 2  Altitude distribution and its topographical divisions

<!-- b000173 | prose | pages [7] -->
Signal Range ⚫

<!-- b000174 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000175 | prose | pages [7] -->
Based on previous literature, we find that the propagation of radio is very much influenced by distance and topography, and different power transmitters are affected in different ways [4]. The relevant data are shown in the table below.

<!-- b000176 | caption | pages [7] -->
Table 1  Signal propagation range

<!-- b000177 | prose | pages [7] -->
Power (W) Plain Range Urban Range Mountain Range

<!-- b000178 | prose | pages [7] -->
5 5 km 10 20 km

<!-- b000179 | prose | pages [7] -->
The Cost ⚫

<!-- b000180 | prose | pages [7] -->
2 km 1 km 7 km 3 km

<!-- b000181 | prose | pages [7] -->
Based on previous research and experience, we believe that the cost of building an EOC and maintaining a drone for each rescue is as follows [5]:

<!-- b000182 | caption | pages [7] -->
Table 2  Economic Cost

<!-- b000183 | prose | pages [7] -->
EOC

<!-- b000184 | furniture | pages [7] -->


<!-- b000185 | prose | pages [7] -->
Drone $50,000 Cost (AUD) $50

<!-- b000186 | heading | pages [7] -->
4.4 Step I: Forecast Deployment of Front-line Personnel

<!-- b000187 | prose | pages [7] -->
Our drone system will not only rescue existing fires that have already occurred, but can also predict locations that have not yet occurred and are likely to do so. Therefore the two need to be discussed separately.

<!-- b000188 | prose | pages [7] -->
Although fires are somewhat predictable, there is a high probability of sudden outbreaks in occasional areas. Since the spread of fire is continuous, we can assume that the fire is continuous in the vicinity of the fire, that is to say, the probability of a fire in the vicinity of fire-occurred location can be expressed as:

<!-- b000189 | prose | pages [7] -->
𝑃1 = 1                                                                             (1)

<!-- b000190 | prose | pages [7] -->
For possible chance scenarios, we can predict the probability of a possible fire based on the

<!-- b000191 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000192 | furniture | pages [7] -->
关注数学模型

<!-- b000193 | furniture | pages [7] -->
2

<!-- b000194 | furniture | pages [7] -->
MATHmodels

<!-- b000195 | furniture | pages [7] -->
获取更多资讯

<!-- b000196 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000197 | furniture | pages [8] -->
Team # 2116496                                                              Page 7 of  24

<!-- b000198 | furniture | pages [8] -->


<!-- b000199 | prose | pages [8] -->
frequency of fires at that location over the years. Since the occurrence of chance generally satisfies the Gaussian distribution and this applies to any location, we can use the GMM model to describe the probability of fire occurrence of a location:

<!-- b000200 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000201 | prose | pages [8] -->
𝑃2(𝑋) = 1

<!-- b000202 | prose | pages [8] -->
(𝑋−𝜇)𝑇(𝑋−𝜇)

<!-- b000203 | prose | pages [8] -->
]                                        (2)

<!-- b000204 | prose | pages [8] -->
2𝜋𝑒𝑥𝑝[−

<!-- b000205 | prose | pages [8] -->
2

<!-- b000206 | prose | pages [8] -->
Where 𝑋 represents any of the possible fire points to be estimated and 𝜇 represents the locations of all the statistically obtained fire points over time.

<!-- b000207 | prose | pages [8] -->
According to local assumption II, front-line personnel are in the area near the location of the (possible) fire. In general, as the size of the fire increases, the more front-line personnel need to be deployed to ensure that the fire is controllable. Therefore, the number of personnel deployed around a (possible) fire point can be written as the following expression:

<!-- b000208 | prose | pages [8] -->
𝑁𝑖= 𝑘𝑖∙𝐴𝑖∙𝑃𝑖                        (3)

<!-- b000209 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000210 | prose | pages [8] -->
𝑓

<!-- b000211 | prose | pages [8] -->
(4)

<!-- b000212 | prose | pages [8] -->
𝑁= ∑𝑁𝑖

<!-- b000213 | prose | pages [8] -->
𝑖=1

<!-- b000214 | prose | pages [8] -->
Where 𝑁𝑖 represents the number of front-line personnel deployed in different locations, thus 𝑁 corresponds to the total number of front-line personnel counted at all fire locations, 𝑓  is statistical frequency of fires over a period of time, 𝐴𝑖 represents the size of the fire, 𝑘𝑖 is the coefficient of

<!-- b000215 | caption | pages [8] -->
Figure 3  Principle of Step I             the number of frontline personnel to be deployed per

<!-- b000216 | prose | pages [8] -->
unit area of fire location.

<!-- b000217 | heading | pages [8] -->
4.5 Step II: Decision on the Locations of the EOCs

<!-- b000218 | prose | pages [8] -->
As front-line personnel and the wildfire can be seen ‘as a whole’, based on the previous deployment of personnel, the locations of the EOCs need to be determined to ensure maximum observability of personnel and safety of the fire.

<!-- b000219 | prose | pages [8] -->
As the SSA drone is required to be in the vicinity of the EOC for cruise reporting and has a flight range of 30km, so that the locations of the EOCs can be framed as a circle with a radius of 30 km which moves as the EOC moves.

<!-- b000220 | prose | pages [8] -->
In addition, the cost of building an EOC should also be taken into account, so our aim is to build the minimum number of EOCs to allow more personnel (as well as the fires) to be covered in its circle. This minimizes costs and maximizes the safety and observability of personnel and fires.

<!-- b000221 | prose | pages [8] -->
Based on this, we introduce the K-means algorithm, which allows for maximum coverage of personnel and wildfires with the proper number of EOCs. By iterating given a proper number

<!-- b000222 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000223 | furniture | pages [8] -->
关注数学模型

<!-- b000224 | furniture | pages [8] -->
2

<!-- b000225 | furniture | pages [8] -->
MATHmodels

<!-- b000226 | furniture | pages [8] -->
获取更多资讯

<!-- b000227 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000228 | furniture | pages [9] -->
Team # 2116496                                                              Page 8 of  24

<!-- b000229 | furniture | pages [9] -->


<!-- b000230 | prose | pages [9] -->
of clusters 𝐾, the entire area can be initially divided into 𝐾 clusters, then optimize the distance to the centroid each time, the distance can be expressed as:

<!-- b000231 | prose | pages [9] -->
𝑑= √(𝑥−𝑥𝑖)2 + (𝑦−𝑦𝑖)2                                                       (5)

<!-- b000232 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000233 | prose | pages [9] -->
Where (𝑥𝑖 , 𝑦𝑖) represents the coordinates of the centroid of each iteration. After combining the distances of all points to the corresponding centers, we can obtain the following indicators for each time:

<!-- b000234 | prose | pages [9] -->
𝑀

<!-- b000235 | prose | pages [9] -->
𝑆𝑆𝐸= ∑∑𝑑(𝐶𝑖, 𝑥)2

<!-- b000236 | prose | pages [9] -->
𝑖=1

<!-- b000237 | prose | pages [9] -->
(6)

<!-- b000238 | prose | pages [9] -->
𝑥∈𝐶𝑖

<!-- b000239 | prose | pages [9] -->
By optimizing the centroids of the area at each iteration, we can end up with an optimal cluster that minimizes the sum of the distances 𝑆𝑆𝐸 from all points 𝑥 in the area to the centroids of the clusters 𝐶𝑖 to which they belong. In our model, this means that the distance from the personnel and the fire to the EOC is minimized, thus ensuring that as many personnel and fires as possible are covered within the nearest EOC.

<!-- b000240 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000241 | prose | pages [9] -->
With the K-means model, we can obtain the optimal centroid coordinates (𝑥𝑀 , 𝑦𝑀), which is also our optimal EOCs’ positions. However, such a result would also produce some out-of-range front-line personnel and fire points at a rate of

<!-- b000242 | prose | pages [9] -->
𝑝𝑖= ∆𝑁𝑖

<!-- b000243 | prose | pages [9] -->
(7)

<!-- b000244 | prose | pages [9] -->
𝑁𝑖

<!-- b000245 | prose | pages [9] -->
Where ∆𝑁𝑖  is the number of uncovered personnel or fire points,  𝑝𝑖 is the rate of uncovered personnel or fire points, both of which may result in

<!-- b000246 | caption | pages [9] -->
Figure 4  Principle of Step II            reduced safety and observability.

<!-- b000247 | prose | pages [9] -->
Another effect that arises in this step is the construction cost 𝑊𝐸𝑂𝐶 of the EOC:

<!-- b000248 | prose | pages [9] -->
𝑊𝐸𝑂𝐶= 𝑁𝐸𝑂𝐶∙𝑤𝐸𝑂𝐶                                                             (8)

<!-- b000249 | prose | pages [9] -->
Where 𝑤𝐸𝑂𝐶 represents the construction cost per EOC, 𝑁𝐸𝑂𝐶 is the number of EOCs.

<!-- b000250 | heading | pages [9] -->
4.6 Step III: Deployment of Hovering Repeaters

<!-- b000251 | prose | pages [9] -->
Front-line personnel must communicate with the EOC via repeater to ensure the safety of personnel and the timely observation of the fire. The radio equipment used to communicate with the front-line personnel and the EOCs is also affected by distance and topography, so we should deploy the repeater at a reasonable distance to ensure that all front-line personnel can communicate with the EOC, so that our communication efficiency is 100% guaranteed to be optimal.

<!-- b000252 | prose | pages [9] -->
From an economic perspective, the fewer repeaters consume the less economic cost, so our goal is to make it possible to meet all personnel locations connected to the EOCs with the minimal repeaters. In this section, we split the two parts of the communication channel and the repeater

<!-- b000253 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000254 | furniture | pages [9] -->
关注数学模型

<!-- b000255 | furniture | pages [9] -->
2

<!-- b000256 | furniture | pages [9] -->
MATHmodels

<!-- b000257 | furniture | pages [9] -->
获取更多资讯

<!-- b000258 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000259 | furniture | pages [10] -->
Team # 2116496                                                              Page 9 of  24

<!-- b000260 | furniture | pages [10] -->


<!-- b000261 | prose | pages [10] -->
deployment.

<!-- b000262 | heading | pages [10] -->
4.6.1 Channel Plan

<!-- b000263 | prose | pages [10] -->
As repeaters have a limited signal propagation range, fewer repeaters means building shorter

<!-- b000264 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000265 | heading | pages [10] -->
communication channels. We introduce the Kruskal algorithm to obtain a minimum spanning

<!-- b000266 | prose | pages [10] -->
tree (MST) to guarantee the shortest channel. The process can be represented in the following flow -chart.

<!-- b000267 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000268 | furniture | pages [10] -->


<!-- b000269 | caption | pages [10] -->
Figure 5  Flow chart of the Kruskal algorithm and principle of Step III (a)

<!-- b000270 | prose | pages [10] -->
Using this algorithm, the optimal path can be determined, thus providing a channel for sub- sequent repeaters scheduling.

<!-- b000271 | heading | pages [10] -->
4.6.2 Repeater Plan

<!-- b000272 | prose | pages [10] -->
The optimum channel has been obtained in the previous section, which means that the sum of the distances from each group of front-line personnel to the EOC has been minimized so that lining up the repeaters on each channel minimizes the number of repeaters used.

<!-- b000273 | furniture | pages [10] -->


<!-- b000274 | prose | pages [10] -->
According to Table 1 and Figure 6, we can see that the signal transmission range varies in different topography. According to the propagation range, deploying repeaters on the channel limits gives the following equation:

<!-- b000275 | caption | pages [10] -->
Figure 6  Principle of Step III (b)

<!-- b000276 | prose | pages [10] -->
𝑁𝑟𝑒𝑝

<!-- b000277 | prose | pages [10] -->
(9)

<!-- b000278 | prose | pages [10] -->
𝐿 𝑖,𝑖+1 = ∑𝑙𝑗+ max (  𝑙𝑗=1   , 𝑙𝑗=𝑁𝑟𝑒𝑝 )

<!-- b000279 | prose | pages [10] -->
𝑗=1

<!-- b000280 | furniture | pages [10] -->


<!-- b000281 | prose | pages [10] -->
Where 𝐿 𝑖,𝑖+1 is the sum of the maximum distances propagated by repeaters on one channel, 𝑙𝑗 is the distance propagated a repeater at a particular location, 𝑁𝑟𝑒𝑝 represents the total number

<!-- b000282 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000283 | furniture | pages [10] -->
关注数学模型

<!-- b000284 | furniture | pages [10] -->
2

<!-- b000285 | furniture | pages [10] -->
MATHmodels

<!-- b000286 | furniture | pages [10] -->
获取更多资讯

<!-- b000287 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000288 | furniture | pages [11] -->
Team # 2116496                                                              Page 10 of  24

<!-- b000289 | furniture | pages [11] -->


<!-- b000290 | prose | pages [11] -->
of repeaters on one channel,  𝑙𝑗=1 and  𝑙𝑗=𝑁𝑟𝑒𝑝 represent the propagation distance of the first and last repeater respectively.

<!-- b000291 | prose | pages [11] -->
Then the constraint can be written as the following expression:

<!-- b000292 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000293 | prose | pages [11] -->
𝐿 𝑖,𝑖+1 ≥∆𝑑 𝑖,𝑖+1                                                                  (10)

<!-- b000294 | prose | pages [11] -->
Similar to step II, this step also incurs an economic cost 𝑊𝑟𝑒𝑝:

<!-- b000295 | prose | pages [11] -->
′ )                                                  (11)

<!-- b000296 | prose | pages [11] -->
𝑊𝑟𝑒𝑝= ∑𝑁𝑟𝑒𝑝∙(𝑤𝑟𝑒𝑝+ 𝑤𝑟𝑒𝑝

<!-- b000297 | prose | pages [11] -->
Where 𝑤𝑟𝑒𝑝 represents the construction cost per repeater, which equals to $10,000

<!-- b000298 | prose | pages [11] -->
′ is the additional maintenance costs.

<!-- b000299 | prose | pages [11] -->
(AUD),  𝑤𝑟𝑒𝑝

<!-- b000300 | heading | pages [11] -->
4.7 Step IV: Design of SSA Monitor Strategy

<!-- b000301 | prose | pages [11] -->
Since SSA drones are cruising in the vicinity of the EOC and has a radius of 30 km, the EOC

<!-- b000302 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000303 | prose | pages [11] -->
and SSA drones can be seen as an integrated system, which we call the EOC-UAV cruise system. Thinking further we can analyze that the factors that affect the number of SSA are the fire situation within the EOC-UAV system and its own capabilities.

<!-- b000304 | prose | pages [11] -->
For a fire, an untimely rescue is very dangerous, so we can define a limit tolerance time 𝑡 which represents the maximum time a fire can withstand being unmonitored, which can be a further indication of the safety of the fire. Then we can think about the number of SSA drones and their cruising strategy. We propose the following two cruising strategies:

<!-- b000305 | prose | pages [11] -->
Strategy A: Multiple SSA circular cruise ⚫

<!-- b000306 | prose | pages [11] -->
Principle: 𝑃  SSA drones monitor each fire

<!-- b000307 | prose | pages [11] -->
point in a periodic cycle with the EOC-UAV system.

<!-- b000308 | prose | pages [11] -->
To maximize fire-fighting efficiency, we consider that all SSA's maintain maximum speed during cruise, which is 𝑣=20 m/s. The mechanism of this cruising strategy can be represented in the right figure. Multiple SSAs cruise on the path between two points in a certain order.

<!-- b000309 | furniture | pages [11] -->


<!-- b000310 | caption | pages [11] -->
Figure 7  Principle of Step IV (A)

<!-- b000311 | prose | pages [11] -->
With this strategy, without taking into account the need for charging, it may happen that a particular fire point is not monitored by any of the drones for a period of time, which corresponds to the limit tolerance time 𝑡 we mentioned above.

<!-- b000312 | prose | pages [11] -->
For a timely fire, we then get the following constraint:

<!-- b000313 | prose | pages [11] -->
∆𝑡𝑖≤𝑡                                                                          (12)

<!-- b000314 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000315 | furniture | pages [11] -->
关注数学模型

<!-- b000316 | furniture | pages [11] -->
2

<!-- b000317 | furniture | pages [11] -->
MATHmodels

<!-- b000318 | furniture | pages [11] -->
获取更多资讯

<!-- b000319 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000320 | furniture | pages [12] -->
Team # 2116496                                                              Page 11 of  24

<!-- b000321 | furniture | pages [12] -->


<!-- b000322 | prose | pages [12] -->
Where ∆𝑡𝑖 represents the minimum time interval in an EOC-UAV system that is not moni- tored. We use the following expression to calculate ∆𝑡𝑖:

<!-- b000323 | prose | pages [12] -->
∆𝑡𝑖=

<!-- b000324 | prose | pages [12] -->
∑𝐷 𝑖,𝑖+1

<!-- b000325 | prose | pages [12] -->
2 ∙𝑣                                                               (13)

<!-- b000326 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000327 | prose | pages [12] -->
𝑁𝑆𝑆𝐴 ,  1

<!-- b000328 | prose | pages [12] -->
Where 𝐷 𝑖,𝑖+1 is the distance between each group of front-liners, 𝑁𝑆𝑆𝐴 , 1/2 is the number of SSA drones without taking into account the charging situation, 𝑣 is the maximum speed, which is 20 m/s. Using equation (12), we can obtain the following expression:

<!-- b000329 | prose | pages [12] -->
𝑁𝑆𝑆𝐴 ,  1

<!-- b000330 | prose | pages [12] -->
2 ≥ ∑𝐷 𝑖,𝑖+1

<!-- b000331 | prose | pages [12] -->
(14) 𝑣∙𝑡

<!-- b000332 | prose | pages [12] -->
In order to reduce the unobservability of the fire over a period of time, the front and back groups of drones should remain perfectly connected, which means that there is no time gap between the two groups of drones ‘at the handover’, with the first group ready to recharge and return just as the second group reaches the first drone.

<!-- b000333 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000334 | prose | pages [12] -->
Then the total number of drones can be written as:

<!-- b000335 | prose | pages [12] -->
2 ≥2 × ∑𝐷 𝑖,𝑖+1 (15)

<!-- b000336 | prose | pages [12] -->
𝑁𝑆𝑆𝐴= 2 × 𝑁𝑆𝑆𝐴 ,  1

<!-- b000337 | prose | pages [12] -->
𝑣∙𝑡

<!-- b000338 | prose | pages [12] -->
However, there may also be a case that 𝑁𝑆𝑆𝐴 ,  1/2 is so large that it exceeds the number of cruising sections when 𝑡 is too small, so strategy A can be further improved.

<!-- b000339 | prose | pages [12] -->
Strategy B: SSA fixed-point cruise ⚫

<!-- b000340 | prose | pages [12] -->
Principle: Point-to-point monitoring of fire points in the EOC-UAV system by 𝑃 drones, i.e. 𝑃 drones for 𝑃 fire points.

<!-- b000341 | prose | pages [12] -->
This situation corresponds to the fact that the 𝑁𝑆𝑆𝐴 ,  1/2 calculated for strategy A is too large that:

<!-- b000342 | prose | pages [12] -->
2 ≥𝑁 𝑓𝑖𝑟𝑒                     (16)

<!-- b000343 | prose | pages [12] -->
𝑁𝑆𝑆𝐴 ,  1

<!-- b000344 | prose | pages [12] -->
Where 𝑁 𝑓𝑖𝑟𝑒  is the number of fire points within an EOC-UAV system. Thus the cruise strate- gy A creates an unnecessary unmonitored time inter       Figure 8   Principle of Step IV (B) -val ∆𝑡𝑖 for each fire point. However, using strategy B can obtain the following equations:

<!-- b000345 | prose | pages [12] -->
∆𝑡𝑖= 0                                                                        (17)

<!-- b000346 | prose | pages [12] -->
2 = 𝑁 𝑓𝑖𝑟𝑒                                                                 (18)

<!-- b000347 | prose | pages [12] -->
𝑁𝑆𝑆𝐴 ,  1

<!-- b000348 | prose | pages [12] -->
Whether to choose strategy A or strategy B, it will incur economic cost:

<!-- b000349 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000350 | furniture | pages [12] -->
关注数学模型

<!-- b000351 | furniture | pages [12] -->
2

<!-- b000352 | furniture | pages [12] -->
MATHmodels

<!-- b000353 | furniture | pages [12] -->
获取更多资讯

<!-- b000354 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000355 | furniture | pages [13] -->
Team # 2116496                                                              Page 12 of  24

<!-- b000356 | furniture | pages [13] -->


<!-- b000357 | prose | pages [13] -->
′ )                                               (19)

<!-- b000358 | prose | pages [13] -->
𝑊𝑆𝑆𝐴= ∑𝑁𝑆𝑆𝐴∙(𝑤𝑆𝑆𝐴+ 𝑤𝑆𝑆𝐴

<!-- b000359 | prose | pages [13] -->
Where 𝑤𝑆𝑆𝐴 represents the construction cost per SSA drone, which equals to $10,000

<!-- b000360 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000361 | prose | pages [13] -->
′ is the additional maintenance costs.

<!-- b000362 | prose | pages [13] -->
(AUD),  𝑤𝑆𝑆𝐴

<!-- b000363 | heading | pages [13] -->
4.8 Rescue Effectiveness

<!-- b000364 | heading | pages [13] -->
4.8.1 Effectiveness Indicators

<!-- b000365 | prose | pages [13] -->
In the analysis of the four steps above, the indicators on the impact of rescue effectiveness are obtained. The corresponding indicator in each step is shown in the table below:

<!-- b000366 | caption | pages [13] -->
Table 3  Effectiveness indicators

<!-- b000367 | prose | pages [13] -->
Economics

<!-- b000368 | furniture | pages [13] -->


<!-- b000369 | prose | pages [13] -->
Capability Safety : 𝑁𝑝𝑒𝑟𝑠𝑜𝑛 Step I

<!-- b000370 | furniture | pages [13] -->


<!-- b000371 | prose | pages [13] -->
Step II

<!-- b000372 | furniture | pages [13] -->


<!-- b000373 | prose | pages [13] -->
Observation Communication

<!-- b000374 | furniture | pages [13] -->


<!-- b000375 | furniture | pages [13] -->


<!-- b000376 | furniture | pages [13] -->


<!-- b000377 | furniture | pages [13] -->


<!-- b000378 | prose | pages [13] -->
: 𝑊𝐸𝑂𝐶 : 𝑝𝑖 : 𝑝𝑖

<!-- b000379 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000380 | prose | pages [13] -->
Step III

<!-- b000381 | furniture | pages [13] -->


<!-- b000382 | furniture | pages [13] -->


<!-- b000383 | prose | pages [13] -->
Step IV

<!-- b000384 | furniture | pages [13] -->


<!-- b000385 | prose | pages [13] -->
: 𝑡 : 𝑊𝑟𝑒𝑝

<!-- b000386 | furniture | pages [13] -->


<!-- b000387 | prose | pages [13] -->
: 100%

<!-- b000388 | furniture | pages [13] -->


<!-- b000389 | furniture | pages [13] -->


<!-- b000390 | prose | pages [13] -->
: 𝑊𝑆𝑆𝐴

<!-- b000391 | prose | pages [13] -->
In the previous section, we ensure that all front-line personnel are able to communicate with the EOCs in both directions, so the communication effectiveness is 100%, so it can be ignored when discussing the final effectiveness function.

<!-- b000392 | heading | pages [13] -->
4.8.2 Effectiveness Function

<!-- b000393 | prose | pages [13] -->
In evaluating the effectiveness of the rescue, we ignore those immeasurable values because the value of human or biological life cannot in fact be estimated numerically. The specific effect- iveness function is shown as below:

<!-- b000394 | prose | pages [13] -->
𝐸= 𝛼∙∑𝑁𝑝𝑒𝑟𝑠𝑜𝑛̿̿̿̿̿̿̿̿̿̿̿̿̿̿ + 𝛽∙(∑𝑝𝑖̿̿̿̿̿̿̿ + 𝑡̿̿̿̿̿̿̿̿̿̿̿̿̿) + 𝛾∙(𝑊𝐸𝑂𝐶+ 𝑊𝑟𝑒𝑝+ 𝑊𝑆𝑆𝐴̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿̿) + 𝛿∙∑𝑝𝑖̿̿̿̿̿̿̿   (20)

<!-- b000395 | prose | pages [13] -->
Where 𝛼 ,  𝛽 ,  𝛾 , 𝛿 are the weights of the capability, safety, economics and observation, respectively. The parameters with      ̿̿̿̿ above represent the normalized result, and the positive and negative correlation of each indicator to effectiveness are also processed. Based on this effectiveness function, we can optimize different EOC-UAV system for different situations.

<!-- b000396 | heading | pages [13] -->
4.9 Results

<!-- b000397 | heading | pages [13] -->
4.9.1 Estimation of Weights

<!-- b000398 | prose | pages [13] -->
In order to further explore the impact of the above four factors on the effectiveness, we choose to use Analytic Hierarchy Process (AHP) to calculate the weights of different factors when they react on the wildfire rescue effectiveness. We use MATLAB to get the weight vector matrix as follows:

<!-- b000399 | prose | pages [13] -->
𝑊= [0.4918    0.2459    0.1639    0.0984]                                        (21)

<!-- b000400 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000401 | furniture | pages [13] -->
关注数学模型

<!-- b000402 | furniture | pages [13] -->
2

<!-- b000403 | furniture | pages [13] -->
MATHmodels

<!-- b000404 | furniture | pages [13] -->
获取更多资讯

<!-- b000405 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000406 | furniture | pages [14] -->
Team # 2116496                                                              Page 13 of  24

<!-- b000407 | furniture | pages [14] -->


<!-- b000408 | prose | pages [14] -->
According to the order, the four factors are safety, capability, economics and observation.

<!-- b000409 | heading | pages [14] -->
4.9.2 Calculation Results

<!-- b000410 | prose | pages [14] -->
Based on the optimization results, we perform calculations for two consecutive months in No-

<!-- b000411 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000412 | prose | pages [14] -->
vember and December 2019, and obtain the following drones arrangement solutions as follows:

<!-- b000413 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000414 | furniture | pages [14] -->


<!-- b000415 | caption | pages [14] -->
Figure 9  The drone solution in November

<!-- b000416 | furniture | pages [14] -->


<!-- b000417 | caption | pages [14] -->
Figure 10  The drone solution in December

<!-- b000418 | prose | pages [14] -->
Both blue and red points represent fire locations within a month. The small orange triangle represents the location of a possible fire based on our predictions. Most importantly, the specific optimal number and the ratio of the two drones, as well as the budget costs (for Victoria)are

<!-- b000419 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000420 | furniture | pages [14] -->
关注数学模型

<!-- b000421 | furniture | pages [14] -->
2

<!-- b000422 | furniture | pages [14] -->
MATHmodels

<!-- b000423 | furniture | pages [14] -->
获取更多资讯

<!-- b000424 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000425 | furniture | pages [15] -->
Team # 2116496                                                              Page 14 of  24

<!-- b000426 | furniture | pages [15] -->


<!-- b000427 | prose | pages [15] -->
given in the upper left corner of the figure. From an overall perspective, we can clearly see that the total number of drones deployed is higher in areas with more severe fires, which in part explains the important role played by the parameter 𝑨(size) and 𝒇(frequency) included in our model.

<!-- b000428 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000429 | heading | pages [15] -->
5. Model II: Extreme Condition Arrangement Model

<!-- b000430 | prose | pages [15] -->
Considering the extreme fire events over the next decades, we first need to make projections over a ten-year period.

<!-- b000431 | heading | pages [15] -->
5.1 Prediction of Fire Conditions

<!-- b000432 | prose | pages [15] -->
Since fires often occur in locations with higher temperatures and less precipitation, these two factors can be approximated as an estimate of the likelihood of fire. By reviewing the literature we obtain data on temperature and precipitation over the last ten years, as shown in the following table [6]:

<!-- b000433 | caption | pages [15] -->
Table 4  Data on temperature and precipitation for 2011-2020

<!-- b000434 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000435 | prose | pages [15] -->
2013 2014 2015 Year 2011 2012 2016 2017 2018 2019 2020 24.1 23.4 24 25.2 24.9 T ℃ 25.4 25.6 25.9 26.1 24.4 935.8 821.2 702.3 568.3 481.2 777.1 P 𝑚𝑚 724.9 877.8 829.9 692

<!-- b000436 | prose | pages [15] -->
Since only 10 temperature and precipitation data are collected, we need to predict the con- dition for 10 years. GM(1,1) can help us to get a valid prediction result.

<!-- b000437 | prose | pages [15] -->
The calculation process of GM (1,1) is shown as follows. The original sequence is:

<!-- b000438 | prose | pages [15] -->
𝑥(0) = (𝑥(0)(1), 𝑥(0)(2), ⋯, 𝑥(0)(10))                                           (22)

<!-- b000439 | prose | pages [15] -->
, 𝑘= 1,2, ⋯,10, 𝑥(1) = (𝑥(1)(1), 𝑥(1)(2), ⋯, 𝑥(1)(10)). Let 𝑥(1)(𝑘) = ∑ 𝑘 𝑥(0)(𝑖) 𝑖=1

<!-- b000440 | prose | pages [15] -->
Thus the AGO sequence 𝑥(1) of 𝑥(0) can be obtained. Then the regression equation of GM(1,1) is :

<!-- b000441 | prose | pages [15] -->
𝑥(0)(𝑘) + 𝑎𝑥(1)(𝑘) = 𝑏                                                          (23)

<!-- b000442 | prose | pages [15] -->
The matric vector notation is:

<!-- b000443 | prose | pages [15] -->
𝑋= [𝑎 𝑏]𝑇                                                                    (24)

<!-- b000444 | prose | pages [15] -->
𝑇                                          (25)

<!-- b000445 | prose | pages [15] -->
𝑥(0)(10)] 𝑥(0)(3) 𝐵= [𝑥(0)(2) ⋯

<!-- b000446 | prose | pages [15] -->
−𝑥(1)(2)

<!-- b000447 | prose | pages [15] -->
1

<!-- b000448 | prose | pages [15] -->
−𝑥(1)(3)

<!-- b000449 | prose | pages [15] -->
𝐴= [

<!-- b000450 | prose | pages [15] -->
1⋯ ]                                                           (26)

<!-- b000451 | prose | pages [15] -->
⋯ ⋯

<!-- b000452 | prose | pages [15] -->
1

<!-- b000453 | prose | pages [15] -->
−𝑥(1)(10)

<!-- b000454 | prose | pages [15] -->
Then GM(1,1) is to be:

<!-- b000455 | prose | pages [15] -->
𝐵= 𝐴𝑋                                                                        (27) Then using least square method to solve a and b:

<!-- b000456 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000457 | furniture | pages [15] -->
关注数学模型

<!-- b000458 | furniture | pages [15] -->
2

<!-- b000459 | furniture | pages [15] -->
MATHmodels

<!-- b000460 | furniture | pages [15] -->
获取更多资讯

<!-- b000461 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000462 | furniture | pages [16] -->
Team # 2116496                                                              Page 15 of  24

<!-- b000463 | furniture | pages [16] -->


<!-- b000464 | prose | pages [16] -->
𝑏]𝑇= (𝐴𝑇𝐴)−1𝐴𝑇𝐵                                                    (28) 𝑋= [𝑎

<!-- b000465 | prose | pages [16] -->
The final prediction of temperatures and precipitations are shown in the figure below:

<!-- b000466 | furniture | pages [16] -->


<!-- b000467 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000468 | furniture | pages [16] -->


<!-- b000469 | furniture | pages [16] -->


<!-- b000470 | prose | pages [16] -->
Year 2021 2022 2023 2024 2025 25.72 25.85 25.98 26.12 26.25 T ℃ P 𝑚𝑚 594.00 568.76 544.58 521.44 499.27

<!-- b000471 | prose | pages [16] -->
Year 2026 2027 2028 2029 2030 26.38 26.52 26.66 26.79 26.93 T ℃ P 𝑚𝑚 478.05 457.73 438.27 419.65 401.81

<!-- b000472 | caption | pages [16] -->
Figure 11  Prediction data for 2021-2030

<!-- b000473 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000474 | prose | pages [16] -->
From the predictions we can see that 2030 will have the highest temperature and the least precipitation, which most likely causes fires. So we analyze the extreme fire events based on the projected data for 2030.

<!-- b000475 | heading | pages [16] -->
5.2 Extreme Fire Events

<!-- b000476 | prose | pages [16] -->
We categorize the extreme fire events as follows:

<!-- b000477 | prose | pages [16] -->
Type I: Fires generally occur at a higher probability each location ⚫ As the temperature and precipitation conditions become worse, we assume that the probability of fire at each location increases. Applying equation (2) from model 1 to this situation, we lower the probability threshold for the occurrence of fire so that the probability of fire at each location after superimposing the Gaussian distribution increases, causing widespread fire throughout the whole area. Due to the larger extent of fire points, the economic impact of EOCs may be more significant.

<!-- b000478 | prose | pages [16] -->
Type II: Fires become smaller in size but occur more often ⚫ This situation can be likened to the frequent and concentrated occurrence of fires due to the harsher climatic conditions in one location. One of the parameters mentioned in the model 1 regarding fire size 𝐴𝑖 and frequency 𝑓𝑖 can be adjusted to be larger and smaller respectively, to suit the situation. As the fire points are concentrated in the area covered by the EOC, the number of SSAs sent should be significantly higher, which will result in more SSAs’ cost.

<!-- b000479 | prose | pages [16] -->
Type III: Fires erupt in an unpredictable manner, with a large area and low frequency ⚫ It is also common for a fire to erupt suddenly due to some factors, and this situation is usually characterized by a wide area of outbreak and low predictability. In other words, this type of fire is a sudden outbreak that is large in area and very infrequent in occurrence. Due to the unpredictable nature of this situation, the pre-deployed personnel cannot anticipate well, and may be more dispersed throughout the whole area. This makes communication between personnel and the EOC difficult and leads to more repeaters being deployed, resulting in greater economic costs.

<!-- b000480 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000481 | furniture | pages [16] -->
关注数学模型

<!-- b000482 | furniture | pages [16] -->
2

<!-- b000483 | furniture | pages [16] -->
MATHmodels

<!-- b000484 | furniture | pages [16] -->
获取更多资讯

<!-- b000485 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000486 | furniture | pages [17] -->
Team # 2116496                                                              Page 16 of  24

<!-- b000487 | furniture | pages [17] -->


<!-- b000488 | heading | pages [17] -->
5.3 Calculation Results

<!-- b000489 | prose | pages [17] -->
Based on the survey, the closest data to 2030 is obtained [7]. Based on this data, model 1 is applied to obtain results corresponding to three types of extreme cases above.

<!-- b000490 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000491 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000492 | furniture | pages [17] -->


<!-- b000493 | caption | pages [17] -->
Figure 12  The drone arrangement solution of Type I

<!-- b000494 | prose | pages [17] -->
The result corresponding to type I is shown above. As we know, a high probability of fire inevitably leads to a large number of fires across the whole area, accompanied by an increase in equipment costs. Compared to the data of Victoria from the December fire in 2019, the budget costs for repeater and SSA drone increase by $ 402,000 and $ 804,000, and the increased con- struction costs for the EOC are $ 300,000.

<!-- b000495 | furniture | pages [17] -->


<!-- b000496 | furniture | pages [17] -->


<!-- b000497 | caption | pages [17] -->
Figure 13  The drone system solution of Type II

<!-- b000498 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000499 | furniture | pages [17] -->
关注数学模型

<!-- b000500 | furniture | pages [17] -->
2

<!-- b000501 | furniture | pages [17] -->
MATHmodels

<!-- b000502 | furniture | pages [17] -->
获取更多资讯

<!-- b000503 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000504 | furniture | pages [18] -->
Team # 2116496                                                              Page 17 of  24

<!-- b000505 | furniture | pages [18] -->


<!-- b000506 | prose | pages [18] -->
The result corresponding to type II is shown above. For small but frequent fires, the number of EOCs required is reduced, however, the number of personnel deployed near the fire point is increased. Overall, the combined effect of the emergency response is significant. The increased costs for repeater, SSA are $ 281,400, $ 1,025,100. EOCs’ budget costs reduce $100,000.

<!-- b000507 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000508 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000509 | caption | pages [18] -->
Figure 14  The drone system solution of Type III

<!-- b000510 | prose | pages [18] -->
Unlike the second type of fire, for the sudden fire of type III, the number of personnel and fires left outside the range is very much, which increases the number of repeaters and extends the communication channel. For the change in costs for this type, we obtain the following data: for repeater and SSA are $ 432,150 and $ 763,800 respectively; for EOC, the reduction cost is $100,000.

<!-- b000511 | prose | pages [18] -->
The changes in the costs are shown in the table below:

<!-- b000512 | caption | pages [18] -->
Table 5  Changes in costs in 3 types of extreme cases

<!-- b000513 | prose | pages [18] -->
SSA Type Repeater Type I EOC Total +$ 804,000 +$ 402,000 Type II +$ 300,000 +$ 1,506,000 +$ 1,025,100 +$ 281,400 Type III −$ 100,000 +$ 1,206,500 +$ 763,800 +$ 432,150 −$ 100,000 +$ 1,095,950

<!-- b000514 | prose | pages [18] -->
The three different colored blocks represent the most significant part of the equipment cost corresponding to each type of extreme fire event. The results shown are coincide with our perceptions and predictions, and to a certain extent, it also reflects the reasonableness of our model.

<!-- b000515 | heading | pages [18] -->
6. Model III: Repeater Location Optimization Model

<!-- b000516 | heading | pages [18] -->
6.1 Analysis of Terrain Impact

<!-- b000517 | prose | pages [18] -->
The terrain will affect each step of the model we built earlier, as analyzed below.

<!-- b000518 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000519 | furniture | pages [18] -->
关注数学模型

<!-- b000520 | furniture | pages [18] -->
2

<!-- b000521 | furniture | pages [18] -->
MATHmodels

<!-- b000522 | furniture | pages [18] -->
获取更多资讯

<!-- b000523 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000524 | furniture | pages [19] -->
Team # 2116496                                                              Page 18 of  24

<!-- b000525 | furniture | pages [19] -->


<!-- b000526 | prose | pages [19] -->
(1) The pre-deployment of personnel in step I changes due to the different levels of urgency in

<!-- b000527 | prose | pages [19] -->
case of fire in different terrains. The direct parameter affecting the number of personnel is 𝑘𝑖 in equation (3), which reflects the capability to rescue a particular fire point.

<!-- b000528 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000529 | prose | pages [19] -->
(2) In step II, changes in personnel may lead to movement of the location and number of EOC

<!-- b000530 | prose | pages [19] -->
after processing the k-means algorithm, which directly affects the construction cost of the EOCs and also directly links to the economics. In addition, the proportion of personnel left out of range may also be affected, corresponding to the parameter 𝑝 in equation (7), where the resulting safety and observability are further compromised.

<!-- b000531 | prose | pages [19] -->
(3) Most importantly, step III is affected by the difference in terrain，resulting in a change in the

<!-- b000532 | prose | pages [19] -->
distance between two points, where the distance between personnel and EOC and the distance between the two fire points are both included. Considering the limitation of the transmission range caused by terrain factors, the number of repeaters will change accordingly, resulting in a change in economy.

<!-- b000533 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000534 | prose | pages [19] -->
(4) In the last step, the tolerance time 𝑡  for some ignition fire points may become shorter due to

<!-- b000535 | prose | pages [19] -->
some rough terrain, corresponding to the safety indicator in the effectiveness function. Further- more, the change of 𝑡  may also cause a change in the cruising strategy of the SSA, accompanied by a change in the number of SSA and thus the economy.

<!-- b000536 | heading | pages [19] -->
6.2 Calculation Results

<!-- b000537 | prose | pages [19] -->
Taking the terrain into account, the flight range of the SSA drones changes from a two- dimensional flat circle to a three-dimensional sphere, and the fact that the signal cannot cross mountains should also be taken into consideration. Based on this, we optimize the locations of the repeaters and obtain the following results.

<!-- b000538 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000539 | furniture | pages [19] -->


<!-- b000540 | furniture | pages [19] -->
关注数学模型

<!-- b000541 | furniture | pages [19] -->
2

<!-- b000542 | furniture | pages [19] -->
MATHmodels

<!-- b000543 | furniture | pages [19] -->
获取更多资讯

<!-- b000544 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000545 | furniture | pages [20] -->
Team # 2116496                                                              Page 19 of  24

<!-- b000546 | furniture | pages [20] -->


<!-- b000547 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000548 | furniture | pages [20] -->


<!-- b000549 | caption | pages [20] -->
Figure 15  The repeater location solution in November considering terrains

<!-- b000550 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000551 | furniture | pages [20] -->


<!-- b000552 | furniture | pages [20] -->


<!-- b000553 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000554 | furniture | pages [20] -->
关注数学模型

<!-- b000555 | furniture | pages [20] -->
2

<!-- b000556 | furniture | pages [20] -->
MATHmodels

<!-- b000557 | furniture | pages [20] -->
获取更多资讯

<!-- b000558 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000559 | furniture | pages [21] -->
Team # 2116496                                                              Page 20 of  24

<!-- b000560 | furniture | pages [21] -->


<!-- b000561 | caption | pages [21] -->
Figure 16  The repeater location solution in December considering terrains

<!-- b000562 | prose | pages [21] -->
For the above two groups of figures, the first figure of each group represents the two- dimensional plane location of the repeaters, the white × in the figure represents the optimized repeater location; the second figure of each group represents the detailed three-dimensional

<!-- b000563 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000564 | prose | pages [21] -->
information of the repeaters near each EOC.

<!-- b000565 | heading | pages [21] -->
7. Sensitivity Analysis

<!-- b000566 | prose | pages [21] -->
In our previous model, there are three parameters that can be varied depending on the situation:

<!-- b000567 | prose | pages [21] -->
𝒌: the parameter that directly affect the number of personnel deployed in the vicinity of a fire ⚫

<!-- b000568 | prose | pages [21] -->
𝑵𝑬𝑶𝑪: the parameter that continuously influence subsequent model from step II ⚫

<!-- b000569 | prose | pages [21] -->
𝒕: the parameter that directly decides the acceptable limit time a fire point not monitored. ⚫

<!-- b000570 | furniture | pages [21] -->


<!-- b000571 | prose | pages [21] -->
Based on this, we adjust these three parameters to test the sensitivity and robustness of our model.

<!-- b000572 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000573 | prose | pages [21] -->
i.  Impact of 𝑘:

<!-- b000574 | prose | pages [21] -->
We set 𝑘 to a number of values and the resulting indicators are shown below: (PS: Through normalization and unification of positive and negative correlations (a part of TOPSIS), the smaller the effectiveness value, the better the effect.)

<!-- b000575 | furniture | pages [21] -->


<!-- b000576 | furniture | pages [21] -->


<!-- b000577 | caption | pages [21] -->
Figure 17  Changes in various indicators under the influence of 𝑘

<!-- b000578 | prose | pages [21] -->
As the value of 𝑘 varies, there is a minimum value of the effectiveness value 𝐸 (𝑘= 1.3). It is clear from the changing trend that the overall value of 𝐸 does not vary much around the optimum value, which means changes in the 𝑘 value have a small effect on our model. Therefore, we can assume that 𝑘 and 𝐴 have the same effect on our model according to equation (3), which means that our model is stable and adapts to fire situations with different sizes.

<!-- b000579 | prose | pages [21] -->
ii.  Impact of 𝑁𝐸𝑂𝐶:

<!-- b000580 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000581 | furniture | pages [21] -->
关注数学模型

<!-- b000582 | furniture | pages [21] -->
2

<!-- b000583 | furniture | pages [21] -->
MATHmodels

<!-- b000584 | furniture | pages [21] -->
获取更多资讯

<!-- b000585 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000586 | furniture | pages [22] -->
Team # 2116496                                                              Page 21 of  24

<!-- b000587 | furniture | pages [22] -->


<!-- b000588 | prose | pages [22] -->
Varying the value of 𝑁𝐸𝑂𝐶 can bring about the following changes:

<!-- b000589 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000590 | furniture | pages [22] -->


<!-- b000591 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000592 | caption | pages [22] -->
Figure 18  Changes in various indicators under the influence of 𝑁𝐸𝑂𝐶

<!-- b000593 | prose | pages [22] -->
During the discrete changes of 𝑁𝐸𝑂𝐶 , the effectiveness indicator 𝐸  decreases and then increases, with the inflection point around 8. Before the inflection point, all indicators are in a better direction, however, when 𝑁𝐸𝑂𝐶 continues to increase, the economic indicators become worse, resulting in worse efficiency. Corresponding to the actual rescue system, too many and too few emergency rescue centers are both unscientific. From this perspective, our model can be considered reasonable.

<!-- b000594 | prose | pages [22] -->
iii.  Impact of 𝑡:

<!-- b000595 | furniture | pages [22] -->


<!-- b000596 | caption | pages [22] -->
Figure 19  Changes in various indicators under the influence of 𝑡

<!-- b000597 | prose | pages [22] -->
The impact of tolerance time 𝑡 on each indicator is more complex, but in general, as the tolerance time increases, the effectiveness value gradually tends to stable, maintaining a high level of effectiveness, and only at very small 𝑡 does the effectiveness show slightly weaker. From this

<!-- b000598 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000599 | furniture | pages [22] -->
关注数学模型

<!-- b000600 | furniture | pages [22] -->
2

<!-- b000601 | furniture | pages [22] -->
MATHmodels

<!-- b000602 | furniture | pages [22] -->
获取更多资讯

<!-- b000603 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000604 | furniture | pages [23] -->
Team # 2116496                                                              Page 22 of  24

<!-- b000605 | furniture | pages [23] -->


<!-- b000606 | prose | pages [23] -->
law, we can conclude that when the fire is very urgent or very severe, some indicators need to be sacrificed, such as increasing some economic costs in exchange for the effectiveness of the rescue.

<!-- b000607 | heading | pages [23] -->
8. Strengths and Weaknesses

<!-- b000608 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000609 | heading | pages [23] -->
8.1 Strengths

<!-- b000610 | prose | pages [23] -->
Our model combines many factors to obtain a universal situation and allows for a rapid ⚫ response and prevention of a fire situation, depending on the size and frequency of the area.

<!-- b000611 | prose | pages [23] -->
We apply a number of models and algorithms, optimize them several times to achieve optimal ⚫ results. More satisfyingly, we do not over-emphasis the process of these algorithms, but describe modelling ideas in vivid that each principle is illustrated with a figure to make it easier to clarify problem solving ideas.

<!-- b000612 | prose | pages [23] -->
For the extreme events, we categorize them and analyze the problem in a comprehensive and ⚫ multifaceted way, obtaining different results as well as adaptations.

<!-- b000613 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000614 | prose | pages [23] -->
Our models are not only able to rescue fires that have already occurred, but also to prevent ⚫ and warn of fires in locations that may possible occur, allowing for optimal rapid rescue and reducing economic losses.

<!-- b000615 | prose | pages [23] -->
The pictures in our works are beautiful, which can better show our modeling results. ⚫

<!-- b000616 | heading | pages [23] -->
8.2 Weakness

<!-- b000617 | prose | pages [23] -->
Some of the unpredictable and unmeasured effects are ignored on our discussed elements, and ⚫ may bias the effectiveness function of our model, thus affecting our optimal solution.

<!-- b000618 | prose | pages [23] -->
For the effect of topography, we ignore the effect of economic costs due to differences in ⚫ topography, which may lead to changes in economic indicators.

<!-- b000619 | prose | pages [23] -->
There may be some other factors that affect our model, however, we pay less attention to these ⚫ factors and some biases may be caused.

<!-- b000620 | heading | pages [23] -->
9. Conclusion

<!-- b000621 | prose | pages [23] -->
In our article, we design models for the deployment of drones and use several algorithms in the modelling process to optimize our results. We develop our modelling in four steps: Forecast Deployment of Front-line Personnel, Decision on the Locations of the EOCs, Deployment of Hovering Repeaters, Design of SSA Monitor Strategy. In each step, we analyze indicators that may affect effectiveness and obtain effectiveness indicators that take into account safety, capacity, economy, observability and communication. By optimizing the effectiveness indicators, we obtain scenarios of drones arrangements that satisfy different situations, each in line with common sense and experience of people. In addition, we classify and analyze extreme fire situations and obtain significant economic elements for different types of extreme fires. Further, we analyze the fire situation for different sizes in different terrains, optimize the 3D spatial locations of the repeaters in Victoria and give clear visualization results. Last but not least, we do sensitivity analysis on three parameters, verify the stability of the model and get practical guidance significance. However,

<!-- b000622 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000623 | furniture | pages [23] -->
关注数学模型

<!-- b000624 | furniture | pages [23] -->
2

<!-- b000625 | furniture | pages [23] -->
MATHmodels

<!-- b000626 | furniture | pages [23] -->
获取更多资讯

<!-- b000627 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000628 | furniture | pages [24] -->
Team # 2116496                                                              Page 23 of  24

<!-- b000629 | furniture | pages [24] -->


<!-- b000630 | prose | pages [24] -->
due to some assumptions in our model may cause the idealization of the model to a certain extent, there is still a certain gap with the reality. In the future, we still have the chance to continue to optimize our model.

<!-- b000631 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000632 | heading | pages [24] -->
10. Continue to Work

<!-- b000633 | prose | pages [24] -->
According to our analysis, our model can adapt well to the majority of fires, and has good rapidity and efficient anticipation for wildfire rescue. However, our model for the type III of extreme wildfire may not work as well, with less effectiveness and more economical cost. A further analysis of the suddenness of the fire situation can be improved in the follow-up. In addition, some of the algorithms in our model can be further optimized, where better results and applicability may emerge in subsequent optimization process.

<!-- b000634 | heading | pages [24] -->
11. Reference

<!-- b000635 | prose | pages [24] -->
[1] M.N.H. Khan, C. Neustaedter, M. Assoc Comp, An Exploratory Study of the Use of Drones for Assisting Firefighters During Emergency Situations, 2019.

<!-- b000636 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000637 | prose | pages [24] -->
[2] https://storymaps.arcgis.com/stories/9ebbe1b54dc847f2a7dd01917c9f3071 [3] https://search.earthdata.nasa.gov/search?m=0!0.140625!2!1!0!0%2C2&fst0=Solid%20Earth &fsm0=Earth%20Gases/Liquids [4] T.K. Sarkar, M.N. Abdallah, M. Salazar-Palma, Survey of Available Experimental Data of Radio Wave Propagation for Wireless Transmission, Ieee Transactions on Antennas and Propagation, 66 (2018) 6665-6672. [5] https://www.sonystyle.com.cn/search.html?q=%E5%85%85%E7%94%B5%E7%94%B5%E 6%B1%A0 [6] http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=136&p_display_type= dailyDataFile&p_startYear=1939&p_c=-898361640&p_stn_num=067021\ [7] https://phys.org/news/2020-01-qa-climate-factors-stoke-australia.html

<!-- b000638 | furniture | pages [24] -->


<!-- b000639 | furniture | pages [24] -->


<!-- b000640 | furniture | pages [24] -->


<!-- b000641 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000642 | furniture | pages [24] -->
关注数学模型

<!-- b000643 | furniture | pages [24] -->
2

<!-- b000644 | furniture | pages [24] -->
MATHmodels

<!-- b000645 | furniture | pages [24] -->
获取更多资讯

<!-- b000646 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000647 | furniture | pages [25] -->
Team # 2116496                                                              Page 24 of  24

<!-- b000648 | furniture | pages [25] -->


<!-- b000649 | heading | pages [25] -->
12. Budget Request

<!-- b000650 | prose | pages [25] -->
To: Victoria State Government From: Victoria’s Country Fire Authority

<!-- b000651 | prose | pages [25] -->
微信公众号：数学模型

<!-- b000652 | prose | pages [25] -->
Date: February 8, 2021

<!-- b000653 | prose | pages [25] -->
Dear Victoria State Government:

<!-- b000654 | prose | pages [25] -->
I am reporting to you the budget for emergency rescue of wildfires, we will give our reasons in the following report.

<!-- b000655 | prose | pages [25] -->
According to the National Weather Service, many places in the eastern part of our country have fallen into prolonged droughts, including our state of Victoria. As for 2019, Australia was the hottest and driest year on record, with average annual temperature 2.7 degrees. However, this long-term trend of high temperature and drought has no intention of going away. The forest fires in the months of 2019 are not the end, but just the beginning. For us CFA, we need more firefighting equipment to deal with this coming terrible crisis.

<!-- b000656 | prose | pages [25] -->
With the rapid development of automation technology, more and more areas adopt drone monitoring and prevention

<!-- b000657 | prose | pages [25] -->
微信号：MATHmodels

<!-- b000658 | prose | pages [25] -->
systems for emergency fire-fighting, especially for forest wildfires, where the terrain is complex, and it is almost impossible to fight fires solely by humans. Therefore, we intend to combine the UAV monitoring system and field visits by front-line personnel to give full play to the advantages of both.

<!-- b000659 | prose | pages [25] -->
Specific UAV systems mainly include several types of equipment: radio handheld equipment, radio repeaters, situational awareness equipment (SSA), EOC signal receiving equipment, and UAV maintenance equipment. The specific mechanism and the limits between them are shown in the right figure:

<!-- b000660 | prose | pages [25] -->
We hire a professional team to conduct a budget analysis for our drone system, the specific budget is shown in the tables below:

<!-- b000661 | prose | pages [25] -->
This table report is based on the forest wildfire in December 2019. The specific payment items are used for the following purposes:  An EOC is deployed in all eight areas of Victoria. The construction cost of each EOC is $50,000, so our infrastructure cost is $ 400,000.  The remaining costs are mainly used for drone deployment in each EOC area. The form on the right has detailed total number of drones in each area. The unit price of the drone is $ 10,000 and the maintenance cost of each is $ 50. It is predicted that 184 drones will be needed, so the cost of drones plus maintenance costs totals $ 1,849,200.  For some other handheld equipment, battery requirements and EOC signal receiving equipment, we also estimate $ 250,000 as a budget.

<!-- b000662 | prose | pages [25] -->
Add up the above three parts, the final total demand is approximately $ 2,500,000 (AUD) as the total equipment budget for the next year. We hope that the government department will approve our budget to prevent future accidents. We will do our best to build our drone monitoring system to protect our home from fire to the greatest extent.

<!-- b000663 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000664 | furniture | pages [25] -->
关注数学模型

<!-- b000665 | furniture | pages [25] -->
2

<!-- b000666 | furniture | pages [25] -->
MATHmodels

<!-- b000667 | furniture | pages [25] -->
获取更多资讯
