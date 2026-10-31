# P-E-2022-2223495-07272032

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2022

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
E

<!-- b000006 | title | pages [1] -->
2223495

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
Letting "Carbon" Stay: Forest Management for Ecological-Economic

<!-- b000009 | prose | pages [1] -->
Balance in the Perspective of Carbon Sequestration

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
Forests play an important role in both nature and human society. In the context of "car- bon peaking and carbon neutral", how to balance the economic and ecological values of forests has become an academic focus. We used differential equations, multi-objective planning, evolutionary games and simulation to find scientific management strategies for forests in different climates and to guide practice and development.

<!-- b000012 | prose | pages [1] -->
First, we constructed a forest carbon sequestration model. Based on the differential equation, we investigated the carbon sequestration level under different forest management strategies, taking into account the forest area, tree age, climate environment, wood use and depreciation, and found that moderate harvesting helps to increase the carbon sequestration of the whole system. In addition, we simulated the adjustment of the harvesting rate to find the best forest management strategy for carbon sequestration and calculated that

<!-- b000013 | prose | pages [1] -->
. Second, in order to balance the multiple values such as economic value and ecological value of the forest system, we constructed six value systems based on the TEV model. Based on this, we constructed a value system balance model using multivariate objectives pro- gramming and solved the maximum total forest ecosystem value (TTF) with the help of simulated annealing (SA) algorithm. Thus, the optimal benefit is achieved with balancing the interests of multiple parties, and the TTF is obtained from the experiment in northern China category: 27283~40924.5$/km2/year.

<!-- b000014 | prose | pages [1] -->
Third, the development of scientific forest management strategies is necessary to achieve the balance and optimum of forest values. The inverse mapping function is con- structed based on the value system balance model to analyze the optimal forest management strategy under the corresponding state. Forest management strategies for general and special conditions are developed based on 4 medium forest harvesting strategies simulated for each of the 4 major types of climatic environments. We used a subtropical forest in China as an example, and validated that the 100-year 𝐶𝑂2 uptake for a harvest rate of 41.5% ~ 55% for near-mature trees and 80% for mature trees is found to be 442.2 ~ 820.8𝑘𝑡.

<!-- b000015 | prose | pages [1] -->
Finally, the problem of adaptation to the transition phase of the optimal forest manage- ment strategy is addressed. This paper introduced game theory to complement the model and used an evolutionary game approach to explore the behavioral decisions of forest man- agers. Moderate deforestation is found to be the optimal outcome that satisfies the demand sensitivity of all parties. The simulation approach is then used to enable the above strategy to be validated in a variety of forest environments.

<!-- b000016 | prose | pages [1] -->
In conclusion, moderate harvesting of forests is the optimal solution to enhance their ecological and economic values. Extending the harvesting cycle will help the current recov- ery of over-harvested forests. However, it should be noted that for polar regions we still need to prohibit logging in order to protect them well.

<!-- b000017 | keywords | pages [1] -->
Keywords:Differential Equations ; Multiple Objective Planning ; TEV ; Evolutionary Game

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | furniture | pages [2] -->


<!-- b000020 | contents | pages [2] -->
1 Introduction ...................................................................................................... 3

<!-- b000021 | contents | pages [2] -->
1.1 Problem Background ....................................................................................................... 3

<!-- b000022 | contents | pages [2] -->
1.2 Restatement of the Problem and Our works. ................................................................... 3

<!-- b000023 | contents | pages [2] -->
1.3 Literature Review ............................................................................................................. 3

<!-- b000024 | contents | pages [2] -->
1.4 Our Work .......................................................................................................................... 4

<!-- b000025 | contents | pages [2] -->
2 Assumptions & Reasonals ............................................................................... 4

<!-- b000026 | contents | pages [2] -->
3 Notations ........................................................................................................... 4

<!-- b000027 | contents | pages [2] -->
4 Whole Process Carbon Sequestration Model for Trees. ............................... 5

<!-- b000028 | contents | pages [2] -->
4.1 Tree Age Stage Classification Model ............................................................................... 6

<!-- b000029 | contents | pages [2] -->
4.2 Forest Ecology Model ...................................................................................................... 7

<!-- b000030 | contents | pages [2] -->
4.3 Whole Process Forest Wood Model ................................................................................. 8

<!-- b000031 | contents | pages [2] -->
4.4 Steady-state Equilibrium Model ...................................................................................... 9

<!-- b000032 | contents | pages [2] -->
4.5 Total Carbon Sequestration Measurement Model .......................................................... 10

<!-- b000033 | contents | pages [2] -->
5 Forest System Value Balance Model ............................................................ 11

<!-- b000034 | contents | pages [2] -->
5.1 TEV: Multiple Value Systems Within and Outside the Forest System .......................... 11

<!-- b000035 | contents | pages [2] -->
5.2 Value Balance Planning Model ...................................................................................... 14

<!-- b000036 | contents | pages [2] -->
5.3 SA : Solution of Multivariate Objective Programming ................................................. 15

<!-- b000037 | contents | pages [2] -->
6 Forest Management Strategy Model ............................................................ 15

<!-- b000038 | contents | pages [2] -->
6.1 Mapping Model of Felling Rate ..................................................................................... 16

<!-- b000039 | contents | pages [2] -->
6.2 Management Strategies and Climate Types ................................................................... 16

<!-- b000040 | contents | pages [2] -->
6.3 Example of Subtropical Forest Management and Decision Making ............................. 18

<!-- b000041 | contents | pages [2] -->
7 Demand-sensitive Management Strategy Game ......................................... 19

<!-- b000042 | contents | pages [2] -->
7.1 The Game of Forest Management Strategies ................................................................. 19

<!-- b000043 | contents | pages [2] -->
7.2 Evolutionary game simulation for managing plan transitions ....................................... 20

<!-- b000044 | contents | pages [2] -->
8 Sensitivity Analysis ......................................................................................... 21

<!-- b000045 | contents | pages [2] -->
9 Model Evaluation and Further Discussion .................................................. 21

<!-- b000046 | contents | pages [2] -->
9.1 Strengths ........................................................................................................................ 21

<!-- b000047 | contents | pages [2] -->
9.2 Weaknesses .................................................................................................................... 21

<!-- b000048 | contents | pages [2] -->
9.3 Further Discussion ......................................................................................................... 21

<!-- b000049 | contents | pages [2] -->
10 Conclusion ..................................................................................................... 21

<!-- b000050 | contents | pages [2] -->
References .................................................................................................... 22

<!-- b000051 | contents | pages [2] -->
11 Forest Carbon Sequestration Science Articles .......................................... 22

<!-- b000052 | contents | pages [2] -->
Appendix ............................................................................................................ 25

<!-- b000053 | furniture | pages [2] -->


<!-- b000054 | heading | pages [3] -->
1 Introduction

<!-- b000055 | heading | pages [3] -->
1.1 Problem Background

<!-- b000056 | prose | pages [3] -->
Climate change is one of the central issues in international public affairs. Reduction of greenhouse gases is important. Carbon sequestration is considered as an effective method to reduce emissions [1]. Carbon sequestration is the safe capture and storage of carbon in the air [2]. Forests are an effective way to sequester carbon [3]. Forests and forest products are affected by the climatic environment and human disturbances [4]. It has been argued that scientific harvest management can improve the carbon sequestration capacity of forest systems. However, forest managers often need to balance ecological, economic and social values when making decisions.

<!-- b000057 | heading | pages [3] -->
1.2 Restatement of the Problem and Our works.

<!-- b000058 | prose | pages [3] -->
Considering the information identified in the problem statement, we need to address the following questions and perform the following tasks ⚫ Develop a carbon sequestration model to quantify the amount of carbon sequestration in

<!-- b000059 | prose | pages [3] -->
forests and their products, and use this model to design the most effective carbon-seques- tration forest management plans. ⚫ Build a decision model to help forest managers choose the best forest management plan

<!-- b000060 | prose | pages [3] -->
and balance multiple value objectives. The model needs to consider the coverage of forest management plans, discuss the conditions under which forests will not be cut down, tran- sition points between forest management plans, and characteristics of forests in different locations in the world regarding transition points of management plans. ⚫ Apply the model practically to all kinds of forests, identify and select the forest that should

<!-- b000061 | prose | pages [3] -->
adopts a forest management plan that includes a harvesting plan. Project carbon sequestra- tion 100 years from now, identify the best forest management plan and argue its rationale, and develop a transition strategy that takes into account the sensitivity of forest managers' needs. ⚫ Write a non-technical essay explaining the need for deforestation and convincing local

<!-- b000062 | prose | pages [3] -->
residents that our management plan is the best decision to develop the forest.

<!-- b000063 | heading | pages [3] -->
1.3 Literature Review

<!-- b000064 | prose | pages [3] -->
Forests play a crucial role in the carbon cycle [5,6]. According to the Kyoto Protocol and the United Nations Framework Convention on Climate Change (UNFCCC), carbon sequestra- tion in forest ecosystems makes carbon management a promising solution to combat climate change [7,8]. The use of forest resources has entered the stage of multi-value sustainable use of managed forests [9,10]. Currently, maintaining and enhancing carbon sinks and carbon stor- age (CSS) in forest ecosystems is becoming a fundamental goal of sustainable forest manage- ment [10]. Adaptive silvicultural practices, such as reducing intensive harvesting, may be one of the strategies to increase the long-term CSS of ecosystem HWP [11,12]. It has been sug- gested that the carbon sink capacity of planted forests can be maximized by extending crop rotation and taking appropriate measures [13].

<!-- b000065 | furniture | pages [3] -->


<!-- b000066 | heading | pages [4] -->
1.4 Our Work

<!-- b000067 | prose | pages [4] -->
Ecological Types

<!-- b000068 | prose | pages [4] -->
Multiple Objectives Mapping Of

<!-- b000069 | prose | pages [4] -->
Programming

<!-- b000070 | prose | pages [4] -->
Data Prepare

<!-- b000071 | prose | pages [4] -->
Literature

<!-- b000072 | prose | pages [4] -->
Research

<!-- b000073 | prose | pages [4] -->
Best Carbon Sealing Strategy

<!-- b000074 | prose | pages [4] -->
Forest System Value

<!-- b000075 | heading | pages [4] -->
Balance Model

<!-- b000076 | prose | pages [4] -->
Harvesting Rates

<!-- b000077 | prose | pages [4] -->
Optimization Management

<!-- b000078 | prose | pages [4] -->
Evolutionary

<!-- b000079 | prose | pages [4] -->
Balance Value

<!-- b000080 | prose | pages [4] -->
Gaming

<!-- b000081 | prose | pages [4] -->
Strategy Transition

<!-- b000082 | prose | pages [4] -->
Forest Management

<!-- b000083 | prose | pages [4] -->
Simulation

<!-- b000084 | heading | pages [4] -->
Strategy Model

<!-- b000085 | prose | pages [4] -->
Application and Transition of Strategies

<!-- b000086 | prose | pages [4] -->
Appropriate harvesting

<!-- b000087 | prose | pages [4] -->
Optimal harvesting

<!-- b000088 | prose | pages [4] -->
strategy

<!-- b000089 | prose | pages [4] -->
strategies

<!-- b000090 | prose | pages [4] -->
Ecological Benefits

<!-- b000091 | prose | pages [4] -->
Practice

<!-- b000092 | prose | pages [4] -->
Economic Benefits

<!-- b000093 | prose | pages [4] -->
Guidance

<!-- b000094 | furniture | pages [4] -->


<!-- b000095 | heading | pages [4] -->
Figue 1: The structure and process of the full text modeling

<!-- b000096 | heading | pages [4] -->
2 Assumptions & Reasonals

<!-- b000097 | prose | pages [4] -->
⚫ There are no large emergencies in forest ecology. Large-scale emergencies are stochastic

<!-- b000098 | prose | pages [4] -->
in nature and cannot be modeled. Therefore the effects of natural disasters, such as sudden mudslides, forest fires, pests and diseases, and volcanic eruptions, are not considered. ⚫ The forest areas involved are all operable in terms of management. Some remote for-

<!-- b000099 | prose | pages [4] -->
ests that cannot be used by human activities are outside the scope of this model. This is because it is neither "economic" nor "environmentally friendly" to manage them. ⚫ All wood produced by the forest is fully accessible to the market. According to Say's

<!-- b000100 | prose | pages [4] -->
law, in a free market, the total demand of society is always equal to the total supply . Our model defaults to all timber being available for sale.

<!-- b000101 | heading | pages [4] -->
3 Notations

<!-- b000102 | prose | pages [4] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000103 | caption | pages [4] -->
Table 1: Notations used in this paper

<!-- b000104 | prose | pages [4] -->
Description

<!-- b000105 | heading | pages [4] -->
Symbol

<!-- b000106 | prose | pages [4] -->
Unit Carbon sequestration by trees in the i stage s(i)

<!-- b000107 | furniture | pages [4] -->


<!-- b000108 | prose | pages [4] -->
Ktons Carbon fixation factor Unit Km2 Area of forest in the i stage x(i)

<!-- b000109 | furniture | pages [5] -->


<!-- b000110 | prose | pages [5] -->
Growth factor

<!-- b000111 | furniture | pages [5] -->


<!-- b000112 | prose | pages [5] -->
Unit Natural rate of death in the i stage

<!-- b000113 | furniture | pages [5] -->


<!-- b000114 | prose | pages [5] -->
Unit Deforestation rate in the i stage

<!-- b000115 | furniture | pages [5] -->


<!-- b000116 | prose | pages [5] -->
Unit Carbon transfer coefficient

<!-- b000117 | furniture | pages [5] -->


<!-- b000118 | prose | pages [5] -->
Unit Carbon tax price

<!-- b000119 | furniture | pages [5] -->


<!-- b000120 | prose | pages [5] -->
$/ton Biodiversity coefficient Unit Rhizome ratio R Unit

<!-- b000121 | prose | pages [5] -->
Where we define the main parameters while specific value of those parameters will be given later.

<!-- b000122 | heading | pages [5] -->
4 Whole Process Carbon Sequestration Model for Trees.

<!-- b000123 | prose | pages [5] -->
In order to construct a full-cycle carbon sequestration model for forest trees, two system levels need to be considered: the forest carbon flow system and the wood product carbon flow system. For the forest system, we need to consider the age of trees, their carbon sequestration capacity, natural growth rate and natural mortality rate under different geographical and envi- ronmental conditions. For the wood products carbon flow system, we need to consider the ef- ficiency of wood utilization, the depreciation rate and the end-of-life time of the products.

<!-- b000124 | prose | pages [5] -->
We developed a differential equation-based decision optimization model for the sustaina- ble development of the forest, which takes into account the regeneration continuity and the optimal carbon dioxide sequestration in the forest, so as to achieve the highest level of carbon sequestration for both native ecological and economic products under the premise of "sustain- able development" of the forest. In the process of analysis, we use the Volterra model and ex- pand the original model by using the tree growth environment, the environmental and economic values of forest products and the cutting plan of the forest to balance the harvesting strategy with the restoration strategy and the selection of high-quality and low-quality products, and finally solve the differential equation to calculate the CO2 sequestration of the whole system under different cutting conditions.

<!-- b000125 | prose | pages [5] -->
Forest Carbon Flow System

<!-- b000126 | prose | pages [5] -->
Environment

<!-- b000127 | prose | pages [5] -->
Ecology

<!-- b000128 | prose | pages [5] -->
Age class

<!-- b000129 | prose | pages [5] -->
CSC

<!-- b000130 | prose | pages [5] -->
Forest age stage classification model

<!-- b000131 | prose | pages [5] -->
Forest Environment Model

<!-- b000132 | prose | pages [5] -->
Documents

<!-- b000133 | prose | pages [5] -->
Growth

<!-- b000134 | prose | pages [5] -->
Mortality

<!-- b000135 | prose | pages [5] -->
rate

<!-- b000136 | prose | pages [5] -->
rate

<!-- b000137 | prose | pages [5] -->
*CSC:Carbon sequestration capacity

<!-- b000138 | prose | pages [5] -->
Depreciat

<!-- b000139 | prose | pages [5] -->
Utilization

<!-- b000140 | prose | pages [5] -->
Wooden Material Carbon Flow System

<!-- b000141 | prose | pages [5] -->
Steady-state equilibrium model [ Differential equation models ]

<!-- b000142 | prose | pages [5] -->
ion rates

<!-- b000143 | prose | pages [5] -->
efficiency

<!-- b000144 | prose | pages [5] -->
CSC Incoming

<!-- b000145 | prose | pages [5] -->
Total Carbon sequestration measurement model

<!-- b000146 | prose | pages [5] -->
[ Based on Standard carbon fixation level ]

<!-- b000147 | prose | pages [5] -->
(   )

<!-- b000148 | furniture | pages [5] -->


<!-- b000149 | heading | pages [5] -->
Figue 2: Whole process carbon sequestration model

<!-- b000150 | prose | pages [5] -->
When the above two systems reach steady-state equilibrium, the total carbon sequestration

<!-- b000151 | prose | pages [6] -->
of the two systems is calculated by referring to the standard unit area of forest land sequestra- tion level, and the sum is the carbon sequestration level of the whole process of forest trees.

<!-- b000152 | heading | pages [6] -->
4.1 Tree Age Stage Classification Model

<!-- b000153 | prose | pages [6] -->
Different types of trees have different growth cycles and rotation periods, which are ana- lyzed through the papers of the biological model of trees, while the species of trees are different and the geographical variability is significant. Therefore models need to be constructed to deal with this relationship.

<!-- b000154 | prose | pages [6] -->
Generally, the growth stages of trees are divided into four stages: young stage, middle stage, near-mature stage, and mature stage. In order to make the model more universal and robust, we fuzzify the years of tree growth and construct the following tree age stage division model with one growth stage of the tree as the minimum time unit t. (It is known from consulting the data that each growth stage of most exploited forest trees is about 10-15 years and the whole life cycle is 40-60 years).

<!-- b000155 | prose | pages [6] -->
(E)Over-aged stage(0.01%)

<!-- b000156 | prose | pages [6] -->
Type

<!-- b000157 | prose | pages [6] -->
The tall growth and diameter growth of the trees

<!-- b000158 | prose | pages [6] -->
×

<!-- b000159 | prose | pages [6] -->
are extremely insignificant, the life activity is

<!-- b000160 | prose | pages [6] -->
Unavailable

<!-- b000161 | prose | pages [6] -->
gradually weakened, and the ability to adapt to the environment is greatly reduced.

<!-- b000162 | prose | pages [6] -->
Harvestable

<!-- b000163 | prose | pages [6] -->
Unharvestable

<!-- b000164 | prose | pages [6] -->
×

<!-- b000165 | prose | pages [6] -->
E

<!-- b000166 | prose | pages [6] -->
D

<!-- b000167 | prose | pages [6] -->
10~15Years

<!-- b000168 | prose | pages [6] -->
C

<!-- b000169 | prose | pages [6] -->
10~15Years

<!-- b000170 | prose | pages [6] -->
B

<!-- b000171 | prose | pages [6] -->
10~15Years

<!-- b000172 | prose | pages [6] -->
A

<!-- b000173 | prose | pages [6] -->
10~15Years

<!-- b000174 | prose | pages [6] -->
(A)Juvenile stage(27.0%) Trees in the young stage grow slowly at the beginning and gradually increase in speed later, during which they are often affected by competition from weeds, miscellaneous, shrubs, etc. It is the most unstable period for tree growth.

<!-- b000175 | prose | pages [6] -->
(D)Mature age stage(23.1%) Trees move from robust to mature age. The growth gradually slows down, especially the tall growth is not significant, and the magnitude of the longitudinal and lateral growth of its underground roots and above- ground crown parts approaches or reaches its maximum.

<!-- b000176 | prose | pages [6] -->
(C)Near-Maturity Stage(24.3%) At this time the trees grow vigorously, branches and leaves flourish, flowering and fruiting appear and increase year by year, the diameter growth accelerate- s, but the tree height growth gradually slows down, roots and crowns expand rapidly in all directions.

<!-- b000177 | prose | pages [6] -->
(B)Middle age stage(25.6%) The proportion of dry wood biomass increased rapidly while the proportion of leaf biomass decreased relatively in the biomass of the forest community.

<!-- b000178 | furniture | pages [6] -->


<!-- b000179 | prose | pages [6] -->
Figue 3: Tree age stage classification For plantations, the over-ripe stage accounts for almost a small percentage due to the presence of management and can be ignored. For natural stands, the number of trees in the mature stage is limited by competition due to the presence of natural competition, and again the proportion is small and negligible. The model was constructed for four age stages, A, B, C, and D.

<!-- b000180 | prose | pages [7] -->
The trees in stages A and B are in the fast growth stage and the timber stock is small, so cutting will not bring more economic value, so it is assumed not to harvest trees in stages A and B here. For stage C trees, moderate harvesting can be done, and for stage D, more har- vesting can be done.

<!-- b000181 | heading | pages [7] -->
4.2 Forest Ecology Model

<!-- b000182 | heading | pages [7] -->
4.2.1 Climate Impact on Forests

<!-- b000183 | prose | pages [7] -->
The growth rate and natural mortality of trees are related to the climate and environment in which they live. Drawing on the regularization of the world's major forest area categories in the literature study published by Derrahmane Ameray et al. in 2021, we visualized the forest area characteristics, climatic characteristics of the three major categories and derived the growth coefficient λ and natural mortality rate 𝜌 differently in different forest area types through a comprehensive assessment, as shown in the following Table.

<!-- b000184 | prose | pages [7] -->
Boreal Forest

<!-- b000185 | prose | pages [7] -->
Max.leaf area 53°59’N,105°7’W Coordinates

<!-- b000186 | prose | pages [7] -->
index

<!-- b000187 | prose | pages [7] -->
Nearest

<!-- b000188 | prose | pages [7] -->
Average canopy Prince Albert, Canada town

<!-- b000189 | prose | pages [7] -->
height(m)

<!-- b000190 | prose | pages [7] -->
Basal area(m2ha-1) Forest type Evergreen coniferous

<!-- b000191 | prose | pages [7] -->
Temperate Forest

<!-- b000192 | prose | pages [7] -->
Max.leaf area 35°57’N,84°17’W Coordinates

<!-- b000193 | prose | pages [7] -->
index

<!-- b000194 | prose | pages [7] -->
Nearest

<!-- b000195 | prose | pages [7] -->
Average canopy Oak Ridge, USA town

<!-- b000196 | prose | pages [7] -->
height(m)

<!-- b000197 | prose | pages [7] -->
Winter deciduous

<!-- b000198 | prose | pages [7] -->
Basal area(m2ha-1)

<!-- b000199 | prose | pages [7] -->
Forest type

<!-- b000200 | prose | pages [7] -->
broadleaved

<!-- b000201 | prose | pages [7] -->
Tropical Forest

<!-- b000202 | prose | pages [7] -->
Max.leaf area 2°35’S,50°06’W Coordinates

<!-- b000203 | prose | pages [7] -->
index

<!-- b000204 | prose | pages [7] -->
Average canopy Nearest town Manaus, Brazil

<!-- b000205 | prose | pages [7] -->
height(m)

<!-- b000206 | prose | pages [7] -->
Evergreen broadleaf

<!-- b000207 | prose | pages [7] -->
Basal area(m2ha-1)

<!-- b000208 | prose | pages [7] -->
Forest type

<!-- b000209 | prose | pages [7] -->
terra firme

<!-- b000210 | prose | pages [7] -->
A B

<!-- b000211 | prose | pages [7] -->
Average summer

<!-- b000212 | prose | pages [7] -->
Average winter

<!-- b000213 | prose | pages [7] -->
Boreal Forest Index

<!-- b000214 | prose | pages [7] -->
Parameters

<!-- b000215 | prose | pages [7] -->
100 A

<!-- b000216 | prose | pages [7] -->
50

<!-- b000217 | prose | pages [7] -->
3×3

<!-- b000218 | prose | pages [7] -->
0

<!-- b000219 | prose | pages [7] -->
E

<!-- b000220 | prose | pages [7] -->
B

<!-- b000221 | prose | pages [7] -->
-50

<!-- b000222 | prose | pages [7] -->
9

<!-- b000223 | prose | pages [7] -->
D C

<!-- b000224 | prose | pages [7] -->
31×5

<!-- b000225 | prose | pages [7] -->
Boreal Forest

<!-- b000226 | prose | pages [7] -->
Temperate Forest Index

<!-- b000227 | prose | pages [7] -->
Parameters

<!-- b000228 | prose | pages [7] -->
200 A

<!-- b000229 | prose | pages [7] -->
4×9

<!-- b000230 | prose | pages [7] -->
100

<!-- b000231 | prose | pages [7] -->
E

<!-- b000232 | prose | pages [7] -->
B

<!-- b000233 | prose | pages [7] -->
0

<!-- b000234 | prose | pages [7] -->
26

<!-- b000235 | prose | pages [7] -->
D C

<!-- b000236 | prose | pages [7] -->
20×1

<!-- b000237 | prose | pages [7] -->
Temperate Forest

<!-- b000238 | prose | pages [7] -->
Tropical Forest Index

<!-- b000239 | prose | pages [7] -->
Parameters

<!-- b000240 | prose | pages [7] -->
400 A

<!-- b000241 | prose | pages [7] -->
5-6

<!-- b000242 | prose | pages [7] -->
200

<!-- b000243 | prose | pages [7] -->
E

<!-- b000244 | prose | pages [7] -->
B

<!-- b000245 | prose | pages [7] -->
0

<!-- b000246 | prose | pages [7] -->
30

<!-- b000247 | prose | pages [7] -->
D C

<!-- b000248 | prose | pages [7] -->
29

<!-- b000249 | prose | pages [7] -->
Tropical Forest

<!-- b000250 | prose | pages [7] -->
C C D E

<!-- b000251 | prose | pages [7] -->
Precipitation(cm)

<!-- b000252 | prose | pages [7] -->
temperature(°C)

<!-- b000253 | prose | pages [7] -->
temperature(°C) ‘Growing’ season (d) Dry period(month)

<!-- b000254 | furniture | pages [7] -->


<!-- b000255 | prose | pages [7] -->
Figue 4: Basic information of the three major forest species

<!-- b000256 | heading | pages [7] -->
4.2.2 General Forest Properties

<!-- b000257 | prose | pages [7] -->
In order to make the model usable and robust even in the absence of data, the attributes of the forest in general state are measured. The percentage of each tree age stage in the natural forest. Checking the relevant data, we know that the retention rate of saplings growing to ma- turity in the forest is 85%. The natural mortality rate at each stage can be set as 𝜌 and can be . It can be obtained that 𝜌 is approximately equal to 5%. Set up the set to equation:

<!-- b000258 | furniture | pages [8] -->


<!-- b000259 | prose | pages [8] -->
(1)

<!-- b000260 | prose | pages [8] -->
The percentage of trees in their natural state at each age stage can be calculated from Equa-

<!-- b000261 | furniture | pages [8] -->


<!-- b000262 | prose | pages [8] -->
tion (1). For each tree age, the carbon sequestration level was set. The carbon sequestration level of larch plantation in northern China measured by Jia Yanlong based on CO2FIX model was set as 25𝑘𝑡𝑜𝑛 𝑘𝑚2. Meanwhile, the carbon sequestration level of different tree ages was weighted according to the CO2FIX measurement method, and the summary results are as fol- lows table.

<!-- b000263 | caption | pages [8] -->
Table 2: Carbon fixation coefficient value

<!-- b000264 | prose | pages [8] -->
Forest age class

<!-- b000265 | prose | pages [8] -->
Percent (      )

<!-- b000266 | prose | pages [8] -->
(A,B,C,D)

<!-- b000267 | prose | pages [8] -->
(A)Juvenile 27.0%

<!-- b000268 | prose | pages [8] -->
(B)Mid-age 25.6%

<!-- b000269 | prose | pages [8] -->
(C)Near-Maturity 24.3%

<!-- b000270 | prose | pages [8] -->
(D)Mature age 23.1%

<!-- b000271 | heading | pages [8] -->
4.3 Whole Process Forest Wood Model

<!-- b000272 | prose | pages [8] -->
Carbon sequestration level

<!-- b000273 | prose | pages [8] -->
(   )

<!-- b000274 | furniture | pages [8] -->


<!-- b000275 | furniture | pages [8] -->


<!-- b000276 | furniture | pages [8] -->


<!-- b000277 | furniture | pages [8] -->


<!-- b000278 | furniture | pages [8] -->


<!-- b000279 | prose | pages [8] -->
For the wood of the forest, it can be divided into two parts:

<!-- b000280 | prose | pages [8] -->
Carbon sequestration in forests

<!-- b000281 | prose | pages [8] -->
(a) Initial state of the forest.

<!-- b000282 | prose | pages [8] -->
Carbon sequestration in wood products

<!-- b000283 | prose | pages [8] -->
(I) The harveste d trees become ti -mber, which pl ays a role in carb -on sequestratio n to some extent.

<!-- b000284 | prose | pages [8] -->
(I)

<!-- b000285 | prose | pages [8] -->
(b) Selective harvesting cycle.

<!-- b000286 | prose | pages [8] -->
Juvenile Mid-aged

<!-- b000287 | prose | pages [8] -->
A B

<!-- b000288 | prose | pages [8] -->
Near-Mature Mature

<!-- b000289 | prose | pages [8] -->
D C

<!-- b000290 | prose | pages [8] -->
(a) Four cycle types of trees exist.

<!-- b000291 | prose | pages [8] -->
(b) Selective harvesting of categ

<!-- b000292 | prose | pages [8] -->
-ory C and D trees.

<!-- b000293 | prose | pages [8] -->
(c) The harvested areas are repl

<!-- b000294 | prose | pages [8] -->
-anted, waiting for the forest to grow and recover.

<!-- b000295 | prose | pages [8] -->
(II) Wooden furnitu -re and building ma

<!-- b000296 | prose | pages [8] -->
(II)

<!-- b000297 | prose | pages [8] -->
terials can stabilize carbon sequestratio n over a long period of time.

<!-- b000298 | prose | pages [8] -->
(III)Depreciation.The

<!-- b000299 | prose | pages [8] -->
(III)

<!-- b000300 | prose | pages [8] -->
carbon in used wood furniture re-enters the carbon cycle.

<!-- b000301 | prose | pages [8] -->
(c) Growth and recovery cycle.

<!-- b000302 | furniture | pages [8] -->


<!-- b000303 | prose | pages [8] -->
Figue 4: Whole process forest wood

<!-- b000304 | prose | pages [9] -->
Forest trees and wood products. Both of these parts have carbon sequestration. In order to study the flow of carbon in both parts, the following flow chart of the whole process of forest wood was drawn. The first part, forest carbon sequestration: the model is divided according to the age stage by rasterizing and classifying the area of trees in each age stage of the forest. The specific process is shown in Fig. The second part, wood carbon sequestration, wood is pro- cessed, used and finally scrapped.

<!-- b000305 | heading | pages [9] -->
4.4 Steady-state Equilibrium Model

<!-- b000306 | prose | pages [9] -->
For the forest carbon sequestration system: set 𝑋𝑖 to be the area(km2) of trees in growth stage i and 𝛽𝑖 to be the ecological carbon sequestration per square kilometer of trees in age stage i. The constraints and parameters to be considered are as follows:

<!-- b000307 | prose | pages [9] -->
a) Limitations on the quantity of each tree age. b) The maximum area stock 𝑁 of tree age stages cannot exceed the maximum value in

<!-- b000308 | prose | pages [9] -->
the natural state and at the same time will not exceed the area of its previous tree age stages. Constraints were set for 𝑁3, 𝑁4 as follows:

<!-- b000309 | furniture | pages [9] -->


<!-- b000310 | prose | pages [9] -->
(2)

<!-- b000311 | prose | pages [9] -->
c) Introduction of growth rate and natural mortality. The parameters lam and rou were

<!-- b000312 | prose | pages [9] -->
introduced to take into account the variability in age, geography and climate. The were introduced. parameters and is the growth rate.

<!-- b000313 | prose | pages [9] -->
is the natural mortality rate. The values are taken according to the forest ecological model con- structed above. d) Set the carbon sequestration coefficient 𝛽. For the wood carbon sequestration system,

<!-- b000314 | prose | pages [9] -->
the following limitations were assumed:  Wood conversion rate, from trees to wood is 90%: 

<!-- b000315 | furniture | pages [9] -->


<!-- b000316 | prose | pages [9] -->
Depreciation rate of wood products, set the average depreciation of all types of wood products 20% when scrapped, then can be calculated for each tree age stage (about 10-15 years) wood products average depreciation of about 10%.

<!-- b000317 | furniture | pages [9] -->


<!-- b000318 | prose | pages [9] -->
(3) Using the modified Volterra model, we construct a set of differential equations for the amount of carbon sequestered by trees and wood products at stage C age and stage D age. The equations (4) are as follows:

<!-- b000319 | prose | pages [9] -->
(a)

<!-- b000320 | prose | pages [9] -->
(4)

<!-- b000321 | prose | pages [9] -->
(b)

<!-- b000322 | furniture | pages [9] -->


<!-- b000323 | prose | pages [10] -->
The initial state of the area of each tree stage is set as the area distribution in the natural state, and the initial amount of carbon sequestered by wood products is 0. The equation is solved with the help of Scipy. Let the solution of the differential equation ob- tained be .

<!-- b000324 | heading | pages [10] -->
4.5 Total Carbon Sequestration Measurement Model

<!-- b000325 | prose | pages [10] -->
Referring to the above setting, the following formula can be derived:

<!-- b000326 | furniture | pages [10] -->


<!-- b000327 | prose | pages [10] -->
(5)

<!-- b000328 | prose | pages [10] -->
The model was experimented with a larch plantation ecosystem in northern China by tak- ing a 100𝑘𝑚2 area stand in natural state, and the trees' carbon sequestration capacity beta referred to the settings in the tree age stage classification model. The total amount of carbon sequestered when the system reached stability was calculated in three ways, respectively.

<!-- b000329 | prose | pages [10] -->
Experiment with the model. Taking the 100𝑘𝑚2 area of larch plantation ecosystem in northern China as an example, the tree carbon sequestration capacity 𝛽 refers to the setting in the tree age stage division model. The total amount of carbon sequestration when the system reaches stability is calculated in the following three ways：

<!-- b000330 | prose | pages [10] -->
a) Moderate deforestation and exploitation of forests. When the forest is reasonably

<!-- b000331 | prose | pages [10] -->
felled, take 𝜇𝑎=0.3, 𝜇𝑏 =1. The total carbon sequestration of the system S=1360.3 kilotons of carbon dioxide. b) No deforestation of the forest. When there is no harvesting of any age stage of the

<!-- b000332 | prose | pages [10] -->
forest, i.e., 𝜇𝑎 𝜇𝑏 0, the solution yields the amount of carbon sequestered by the system at stabilization S=1242.7 kt CO2. c) Excessive deforestation in general. 𝜇𝑎=0.6, 𝜇𝑏 =1, S=1123.6 kilotons of CO2.

<!-- b000333 | prose | pages [10] -->
Kton(𝐶𝑂2)

<!-- b000334 | prose | pages [10] -->
(a)

<!-- b000335 | prose | pages [10] -->
(b)

<!-- b000336 | prose | pages [10] -->
(c)

<!-- b000337 | prose | pages [10] -->
The carbon sequestration system reaches a relatively st- eady-state stage, where

<!-- b000338 | prose | pages [10] -->
Kton(𝐶𝑂2)

<!-- b000339 | prose | pages [10] -->
the amount of carbon sequest- ered by each subject be-gins to vary little or not at all.

<!-- b000340 | prose | pages [10] -->
(a)Moderate deforestation. Mature trees are cut down. Only 30% of nearly mature trees are cut.

<!-- b000341 | prose | pages [10] -->
Kton(𝐶𝑂2)

<!-- b000342 | prose | pages [10] -->
(b)No logging of the forest, the forest grows naturally.

<!-- b000343 | prose | pages [10] -->
No logging of the forest, the fore

<!-- b000344 | prose | pages [10] -->
(c)Over-harvesting. 60% of all t-

<!-- b000345 | prose | pages [10] -->
st grows naturally.

<!-- b000346 | prose | pages [10] -->
rees near mature age were harv-

<!-- b000347 | prose | pages [10] -->
Kton(𝐶𝑂2)

<!-- b000348 | prose | pages [10] -->
ested, and all mature trees were harvested.

<!-- b000349 | prose | pages [10] -->
t

<!-- b000350 | prose | pages [10] -->
Based on a model of forest age classificationTime phase

<!-- b000351 | prose | pages [10] -->
Carbon sequestration level

<!-- b000352 | furniture | pages [10] -->


<!-- b000353 | prose | pages [10] -->
Figue 5: Simulation of harvesting strategies under three values of

<!-- b000354 | furniture | pages [10] -->


<!-- b000355 | prose | pages [11] -->
Note: Simulations were performed with 100 𝑘𝑚2of forest in its natural state. t indicates the number of tree age stages experienced.

<!-- b000356 | prose | pages [11] -->
The analysis of the figure shows that. First, at the beginning of the system, any degree of deforestation will lead to a small decrease in the amount of carbon sequestered by the system, and then the amount of carbon sequestered will be increased in a short period of time. Second, when the system reaches equilibrium: (a) moderate harvesting of forest land helps to increase the total carbon sequestration; (b) no harvesting of forest will not change the carbon sequestra- tion of forest; (c) excessive harvesting of forest land will lead to a decrease in the total carbon sequestration.

<!-- b000357 | prose | pages [11] -->
Based on the above analysis, the system was simulated separately for different 𝜇𝑎 to cal- culate the carbon sequestration level under each C tree felling rate, and the final results are shown in Fig 6.

<!-- b000358 | prose | pages [11] -->
Three steady-state phases

<!-- b000359 | prose | pages [11] -->
Stage 1(0%~25%) Increased cutting rate. Increased carbon sequestration. Stage 2(30%~50%) Increase cutting rate. No change in carbon sequestration.

<!-- b000360 | prose | pages [11] -->
Stage 3 (55%~100%) Increased cutting rate Reduced carbon sequestration.

<!-- b000361 | furniture | pages [11] -->


<!-- b000362 | prose | pages [11] -->
Figue 6: Carbon sequestration levels of forest trees under different values

<!-- b000363 | prose | pages [11] -->
From the above figure, it can be seen that the optimal level of carbon sequestration is reached when the felling rate is about 37.48% for trees of category C age.

<!-- b000364 | heading | pages [11] -->
5 Forest System Value Balance Model

<!-- b000365 | prose | pages [11] -->
TEV model proposed by American economist and environmentalist A Freeman in 2022. We use the idea of TEV model to measure the multiple benefits of forest ecosystem through multi-objective planning (MOP), and use Python to simulate differential equations, SA optimi- zation algorithm and game theory to solve the model, so as to get Pareto solution, which is the better strategy after measuring the interests of all parties.

<!-- b000366 | heading | pages [11] -->
5.1 TEV: Multiple Value Systems Within and Outside the Forest System

<!-- b000367 | prose | pages [11] -->
Total forest ecosystem values can be roughly divided into six categories: output values (EF), carbon tax transfer (MF), tourism values (LF), ecological values (GEP), biomass values (CF), and other values (OF). Among them, the ecological value has a more complete account- ing system and values in the academic community, so we will not repeat them here.

<!-- b000368 | prose | pages [12] -->
LF

<!-- b000369 | prose | pages [12] -->
CF

<!-- b000370 | prose | pages [12] -->
Domestic Tourism

<!-- b000371 | prose | pages [12] -->
Biomass value(CF)

<!-- b000372 | prose | pages [12] -->
MF

<!-- b000373 | prose | pages [12] -->
Ecological Value (GEP)

<!-- b000374 | prose | pages [12] -->
Carbon Tax

<!-- b000375 | prose | pages [12] -->
• Neutralizing CO2

<!-- b000376 | prose | pages [12] -->
Revenue International Tourism

<!-- b000377 | prose | pages [12] -->
Tourism Value (LF)

<!-- b000378 | prose | pages [12] -->
Carbon Allowances

<!-- b000379 | prose | pages [12] -->
Revenue

<!-- b000380 | prose | pages [12] -->
TTF

<!-- b000381 | prose | pages [12] -->
Forest Froduct Profit

<!-- b000382 | prose | pages [12] -->
• Water Conservation

<!-- b000383 | prose | pages [12] -->
GEP EF

<!-- b000384 | prose | pages [12] -->
Economic Value (EF)

<!-- b000385 | prose | pages [12] -->
Scientific Research

<!-- b000386 | prose | pages [12] -->
Potential Bequest

<!-- b000387 | prose | pages [12] -->
Carbon tax transfer(MF)

<!-- b000388 | prose | pages [12] -->
OF

<!-- b000389 | prose | pages [12] -->
Other Values (OF)

<!-- b000390 | furniture | pages [12] -->


<!-- b000391 | prose | pages [12] -->
Figue 7: The value composition system of TTF

<!-- b000392 | heading | pages [12] -->
5.1.1 Output Value (EF)

<!-- b000393 | prose | pages [12] -->
We confine the output value of forest trees to the market purchase and sale of forest prod- ucts, and take up the previous section on the harvesting of forest resources to establish the following set of equations:

<!-- b000394 | furniture | pages [12] -->


<!-- b000395 | prose | pages [12] -->
(6)

<!-- b000396 | prose | pages [12] -->
Consider the fluctuation of timber prices with time and market conditions. where 𝑃𝑡is the average of the market purchase and sale prices of timber in period 𝑡. Based on the actual situ- ation in felling, we constrain the equation as follows:

<!-- b000397 | heading | pages [12] -->
5.1.2 Carbon Tax Transfer (MF)

<!-- b000398 | prose | pages [12] -->
(7)

<!-- b000399 | furniture | pages [12] -->


<!-- b000400 | prose | pages [12] -->
The World Bank gives value transfers to areas that maintain forest ecology to absorb car- bon.. The following is how the carbon tax value is calculated:

<!-- b000401 | prose | pages [12] -->
In the first step, the carbon dioxide uptake capacity of the forest system is analyzed. The carbon dioxide uptake per unit time t is given by the equation :

<!-- b000402 | furniture | pages [12] -->


<!-- b000403 | prose | pages [12] -->
(8) When the system enters steady state, there are limits:

<!-- b000404 | prose | pages [12] -->
The formula (8) can be simplified as:

<!-- b000405 | furniture | pages [12] -->


<!-- b000406 | prose | pages [12] -->
(9)

<!-- b000407 | furniture | pages [12] -->


<!-- b000408 | prose | pages [12] -->
(10)

<!-- b000409 | prose | pages [12] -->
In the second step, we economically compensate the forest land according to the objectives depicted in Copenhagen Accord. Due to the inconsistency of carbon trading and carbon tax policies in each country, we adopt a fuzzy treatment and estimate the amount of carbon seques- tered on forest land in the previous paper based on the following equation：

<!-- b000410 | furniture | pages [12] -->


<!-- b000411 | prose | pages [12] -->
(11)

<!-- b000412 | prose | pages [12] -->
is the carbon sequestration on forest land in period 𝑡 of the first problem;

<!-- b000413 | furniture | pages [12] -->


<!-- b000414 | prose | pages [12] -->
is the price per tonne for carbon trading, the specific values are shown below (for some coun- tries) By weighting the recent U.S. carbon price, =51.2$/ton (CO2), and checking the recent

<!-- b000415 | prose | pages [12] -->
news in 2022, we know that the CO2 price in the U.S. carbon trading market is about 50$/ton, which means the calculation is verified.

<!-- b000416 | furniture | pages [12] -->


<!-- b000417 | prose | pages [13] -->
• Average world carbon tax price of 60$ • World carbon trading (ETS) average price of 2$

<!-- b000418 | prose | pages [13] -->
The 2022 Carbon Price Corridor

<!-- b000419 | prose | pages [13] -->
2020 Talking Price Price Corridor: Recommendations from the World Bank's 2017 High Level Committee on Carbon Prices report.

<!-- b000420 | furniture | pages [13] -->


<!-- b000421 | prose | pages [13] -->
Figue 8: Carbon price trends by country

<!-- b000422 | heading | pages [13] -->
5.1.3 Biomass Value Equation (CF)

<!-- b000423 | prose | pages [13] -->
For the establishment of the biomass value equation, we mainly examine the aggregation of the biomass value of the forest ecology itself. We borrowed the TEV model and set up the following equation for forest ecology as follows.

<!-- b000424 | furniture | pages [13] -->


<!-- b000425 | prose | pages [13] -->
(12)

<!-- b000426 | prose | pages [13] -->
In the equation, BEF is the conversion factor of stand biomass to wood volume, and the reference value of IPCC biomass expansion factor (BEF) is shown below.

<!-- b000427 | caption | pages [13] -->
Table 3: BEF value range of different forest species

<!-- b000428 | prose | pages [13] -->
BEF Forest type Climate zone Average Scope

<!-- b000429 | prose | pages [13] -->
Pine Tropical 1.3 1.2~4.0 Broad-leaved 3.4 2.0~9.0

<!-- b000430 | prose | pages [13] -->
Spruce Temperate 1.3 1.15~4.2 Pine 1.3 1.15~3.4

<!-- b000431 | prose | pages [13] -->
Broad-leaved 1.4 1.15~3.2 Coniferous

<!-- b000432 | prose | pages [13] -->
Cold

<!-- b000433 | prose | pages [13] -->
1.35 1.15~3.8 Broad-leaved

<!-- b000434 | furniture | pages [13] -->


<!-- b000435 | prose | pages [13] -->


<!-- b000436 | prose | pages [13] -->
1.3 1.15~4.2

<!-- b000437 | furniture | pages [13] -->


<!-- b000438 | prose | pages [13] -->
𝜑 is the carbon transfer coefficient in the TEV model, which generally takes the value of 0.5.  𝑆𝑡 is the area of the stand at period t, while C is the stand density at period t.  𝑅 is the root-to-stem ratio, which is assigned a value of roughly 0.42 in the IPCC. The above equation constitutes the biomass of the forest ecosystem in the area, and the following equation is constructed to account for the biomass value based on the market value method and analogy method. Where 𝑃𝑡 can refer to the price per ton of dry wood.

<!-- b000439 | heading | pages [13] -->
5.1.4 Tourism Value (LF)

<!-- b000440 | prose | pages [13] -->
(13)

<!-- b000441 | furniture | pages [13] -->


<!-- b000442 | prose | pages [13] -->
Tourism values are mostly divided into human and natural values, and forests are mainly dominated by natural values. The indicators for measuring tourism value vary from place to place, and here the indicators in the literature by Nino Fonseca et al. are used and extended to

<!-- b000443 | prose | pages [14] -->
link tourism value with related factors to construct the following equation.

<!-- b000444 | furniture | pages [14] -->


<!-- b000445 | prose | pages [14] -->
(14)

<!-- b000446 | prose | pages [14] -->
𝐴 in the equation is the local security factor, which is related to the number of local crim- inal violence and social unrest; 𝐼𝑓 is the influence of the scenic area, which is determined by international organizations or national governments; 𝐼 is the reception capacity of the forest area, which is a function of local GDP.

<!-- b000447 | heading | pages [14] -->
5.1.5 Other Values (OF)

<!-- b000448 | prose | pages [14] -->
The natural conditions of forest formation, the composition of forest tree species, and biological resources are all of scientific value. For this, we measure the ecological diversity value of the forest in terms of the distribution of different age classes, taking into account the correlation between the values, and set the following formula.

<!-- b000449 | prose | pages [14] -->
Then the other values are:

<!-- b000450 | furniture | pages [14] -->


<!-- b000451 | prose | pages [14] -->
(15)

<!-- b000452 | furniture | pages [14] -->


<!-- b000453 | prose | pages [14] -->
(16)

<!-- b000454 | prose | pages [14] -->
is the biodiversity coefficient of the forest area, which is determined by the Definition

<!-- b000455 | prose | pages [14] -->
ratio of biological species in the forest area to biological species in the area. Since the next stage of thinning in the near-mature age stage will become the main force of logging in the forest area, it is more reserved for them, so the following constraints are in place.

<!-- b000456 | heading | pages [14] -->
5.2 Value Balance Planning Model

<!-- b000457 | prose | pages [14] -->
(17)

<!-- b000458 | furniture | pages [14] -->


<!-- b000459 | prose | pages [14] -->
Based on the above analysis, a function of the total value of the forest TTF is constructed:

<!-- b000460 | furniture | pages [14] -->


<!-- b000461 | prose | pages [14] -->
(18)

<!-- b000462 | prose | pages [14] -->
Since the main duty of forest area is its biomass value and ecological value, output value and tourism value are its subsidiary values, while other values and carbon tax transfer are non- essential values, so to some extent, their weights can be assigned from high downward, and for general cases, do average weight treatment, and establish the following multi-objective norma- tive equation.

<!-- b000463 | furniture | pages [14] -->


<!-- b000464 | prose | pages [14] -->
(19)

<!-- b000465 | heading | pages [15] -->
5.3 SA : Solution of Multivariate Objective Programming

<!-- b000466 | prose | pages [15] -->
The simulated annealing algorithm benefits from the results of research in statistical me- chanics of materials and has been applied to find the global optimal solution to the NP-hard combinatorial optimization problem The algorithmic procedure is described as follows.

<!-- b000467 | prose | pages [15] -->
i.

<!-- b000468 | prose | pages [15] -->
Solution space. The solution space can be represented as the set of all cyclic arrangements of starting and target points of {1,2...n}, i.e:

<!-- b000469 | prose | pages [15] -->
ii.

<!-- b000470 | furniture | pages [15] -->


<!-- b000471 | prose | pages [15] -->
(20)

<!-- b000472 | prose | pages [15] -->
objective function. In the equation that is MaxTTF.

<!-- b000473 | prose | pages [15] -->
iii.

<!-- b000474 | prose | pages [15] -->
Generation of new solutions. Let the solution of the previous strip be :

<!-- b000475 | prose | pages [15] -->
iv.

<!-- b000476 | furniture | pages [15] -->


<!-- b000477 | prose | pages [15] -->
(21)

<!-- b000478 | prose | pages [15] -->
The difference of the substitution function. The difference between the starting point and the target point can be expressed as:

<!-- b000479 | prose | pages [15] -->
v.

<!-- b000480 | furniture | pages [15] -->


<!-- b000481 | prose | pages [15] -->
(22)

<!-- b000482 | prose | pages [15] -->
,then receive the new cooling path; otherwise, re- Accept the criterion. If ceive the new path with probability , i.e., use the computer to gen- erate a random number rand uniformly distributed on the interval [0,1], if

<!-- b000483 | prose | pages [15] -->
then: vi.

<!-- b000484 | prose | pages [15] -->
Cooling. The cooling is performed using the selected cooling factor α. The de-novo temperature T is αT (here T is the temperature of the previous iteration), and here α = 0.85 is selected. vii.

<!-- b000485 | prose | pages [15] -->
Ending conditions. Use the selected growing temperature e=10-30,to determine whether the annealing process is finished. If T<e, the algorithm ends and the cur- rent state is output. The model was solved by taking larch plantation in northern China as an example, and taking the unit time 𝑡  as 10~15 years. The TTF value was calculated as 27283~40924.5$/km2/year.

<!-- b000486 | heading | pages [15] -->
6 Forest Management Strategy Model

<!-- b000487 | prose | pages [15] -->
This forest value balance model solves the problem of the optimal value balance point.

<!-- b000488 | prose | pages [15] -->
Data

<!-- b000489 | prose | pages [15] -->
Special conditions

<!-- b000490 | prose | pages [15] -->
Prepare

<!-- b000491 | prose | pages [15] -->
Literature

<!-- b000492 | prose | pages [15] -->
General conditions

<!-- b000493 | prose | pages [15] -->
Research

<!-- b000494 | prose | pages [15] -->
（According to climate ）

<!-- b000495 | prose | pages [15] -->
Climate types

<!-- b000496 | prose | pages [15] -->
E2 Temperate E1 Tropical

<!-- b000497 | prose | pages [15] -->
Subtropical

<!-- b000498 | prose | pages [15] -->
E4 Polar E3 Boreal

<!-- b000499 | prose | pages [15] -->
Highland

<!-- b000500 | prose | pages [15] -->
Management Strategies (Selection according to climate and environment)

<!-- b000501 | prose | pages [15] -->
General logging strategy

<!-- b000502 | prose | pages [15] -->
Forest System Value

<!-- b000503 | prose | pages [15] -->
Balance Model

<!-- b000504 | prose | pages [15] -->
Soft logging strategy.

<!-- b000505 | prose | pages [15] -->
Over logging strategy Natural development strategy

<!-- b000506 | prose | pages [15] -->
Mapping Of Felling Rates

<!-- b000507 | furniture | pages [15] -->


<!-- b000508 | heading | pages [15] -->
Figue 9: Forest management strategy model

<!-- b000509 | prose | pages [16] -->
In order to achieve forest value balance, forest management strategies need to be analyzed. The managed deforestation of the forest is obtained by constructing a carbon sink mapping function. Meanwhile, experiments with different logging strategies are conducted for different forest environments in different regions to analyze the transition point of forest management strategy transformation. The specific process is as follows.

<!-- b000510 | heading | pages [16] -->
6.1 Mapping Model of Felling Rate

<!-- b000511 | furniture | pages [16] -->


<!-- b000512 | prose | pages [16] -->
The value of carbon tax transfer (ME) solved by using the value equilibrium point is de- rived by inverse derivation of the tree felling rate 𝜇𝑎for tree age class C. Considering the avail- ability of the model and the realistic situation, the CF,EF,LF,OF of the forest system will not produce large changes in the short term, so the values of the general case calculated above can be maintained.

<!-- b000513 | prose | pages [16] -->
Then based on the above planning model the following functions can be set:

<!-- b000514 | furniture | pages [16] -->


<!-- b000515 | prose | pages [16] -->
(23)

<!-- b000516 | prose | pages [16] -->
TTF0 is the equilibrium point of maximum value of forest use solved based on the above linear programming. This function reflects the CO2 uptake per unit time t (one tree age stage, about 10-15 years) for the specified carbon trading price under the forest maximum value condition. Considering that the above planning is based on the simulation of a 100km2 forest

<!-- b000517 | prose | pages [16] -->
is the mass of CO2 that can be absorbed per square kilometer therefore dividing by 100, of forest at each time stage 𝑡 at the time of deforestation.

<!-- b000518 | heading | pages [16] -->
6.2 Management Strategies and Climate Types

<!-- b000519 | prose | pages [16] -->
In order to analyze the effectiveness of various management strategies on forest ecology in different climates. We should analyze the wood output that the forest can carry when the system reaches steady state. Because

<!-- b000520 | heading | pages [16] -->
6.2.1 General Forest Management Strategy

<!-- b000521 | prose | pages [16] -->
, the analysis of is also valid.

<!-- b000522 | prose | pages [16] -->
Using the felling rate mapping model constructed above, we designed four management strategies :(a) general felling strategy,(b) gentle felling strategy,(c) natural development strat- egy, and (d) excessive felling strategy. The four strategies were applied to four categories of ecological climate :(E1) tropical climate; (E2) Subtropical climate and temperate climate; (E3) Cold zone climate; (E4) Polar climate; Plateau and alpine climate.

<!-- b000523 | prose | pages [16] -->
Based on the forest ecological model in the forest whole-process carbon sequestration model (Model 1), the growth rates of trees living in various climates were divided into sections. The range divided by the red dotted line in Fig. 10 can be obtained. We calculate at differ- ent growth rates of class C and D aged trees by step of 0.1. Based on Sufer, Natural Neighbor interpolation was used to grid the data, and the results are shown in the figure.

<!-- b000524 | prose | pages [16] -->
The wood output that can be carried by forests largely reflects the health of forest systems.

<!-- b000525 | prose | pages [16] -->
related to the load-bearing use of wood in each environment was studied. The variable Based on relevant research Settings:

<!-- b000526 | prose | pages [16] -->
 >500, it indicates that ecological wood output is normal and has no impact In stage

<!-- b000527 | prose | pages [17] -->
on forest ecology, so there is no need to reduce logging rate.  >100, the output of ecological wood is poor, which has a certain neg- In stage 500> ative impact on forest ecology, and the logging rate should be reduced moderately.  >0, the output of ecological wood is extremely poor, and forest man- In stage 100> agement strategy has a strong negative impact on the ecosystem, so logging should be stopped in time.

<!-- b000528 | prose | pages [17] -->
E2 E3

<!-- b000529 | prose | pages [17] -->
E2 E1 E3

<!-- b000530 | prose | pages [17] -->
E4

<!-- b000531 | prose | pages [17] -->
E4

<!-- b000532 | prose | pages [17] -->
(a) (b)

<!-- b000533 | prose | pages [17] -->
E2 E1

<!-- b000534 | prose | pages [17] -->
E2

<!-- b000535 | prose | pages [17] -->
E3

<!-- b000536 | prose | pages [17] -->
E3

<!-- b000537 | prose | pages [17] -->
E4

<!-- b000538 | prose | pages [17] -->
E4

<!-- b000539 | prose | pages [17] -->
(c) (d)

<!-- b000540 | prose | pages [17] -->
E1 E1

<!-- b000541 | prose | pages [17] -->
(a) General logging strategy

<!-- b000542 | prose | pages [17] -->
(b) Soft logging strategy.

<!-- b000543 | prose | pages [17] -->
(c) Natural development strategy

<!-- b000544 | prose | pages [17] -->
(d) Over logging strategy

<!-- b000545 | prose | pages [17] -->
Climate Type

<!-- b000546 | prose | pages [17] -->
E1 E1

<!-- b000547 | prose | pages [17] -->
E1 Tropical Climate

<!-- b000548 | prose | pages [17] -->
E2 Temperate climate

<!-- b000549 | prose | pages [17] -->
Subtropical climate

<!-- b000550 | prose | pages [17] -->
E3 Boreal climate E4 Polar climate

<!-- b000551 | prose | pages [17] -->
Highland climates

<!-- b000552 | prose | pages [17] -->
*Classification of climate types based on wood carbon output in (a)

<!-- b000553 | furniture | pages [17] -->


<!-- b000554 | prose | pages [17] -->
Figue 10: Simulation of different strategies under different environmental conditions

<!-- b000555 | prose | pages [17] -->
Analyze the above figure and summarize the following management strategies for various types of forests:

<!-- b000556 | prose | pages [17] -->
(a) General logging strategies. Under this forest management strategy, the output of wood

<!-- b000557 | prose | pages [17] -->
that can be carried by the forest in E1 climate is normal. Part of E2 needs to adjust the strategy to reduce the felling rate. E3 and E4 cannot adapt to this logging strategy. (b)  Soft logging strategies. Under this forest management strategy, the output of wood

<!-- b000558 | prose | pages [17] -->
that can be carried by the forest in E1 and E2 climate is normal. Part of E3 requires a strategy adjustment to reduce the rate of logging. E4 cannot adapt to this logging strat- egy. (c) Natural development strategies. The forest is not deliberately felled, and the output of

<!-- b000559 | prose | pages [17] -->
wood that can be carried by the forest is normal in E1,E2 and E3 climate under this strategy. E4 some conditions need policy adjustment, and some conditions cannot

<!-- b000560 | prose | pages [17] -->
adapt to the logging strategy. (d) Excessive logging strategies. Under this logging strategy, only the timber output in

<!-- b000561 | prose | pages [17] -->
part of E1 was normal. E2,E3 and E4 could not adapt to this logging strategy.

<!-- b000562 | prose | pages [18] -->
The analysis shows that for tropical, subtropical, and boreal climates, there are appropriate forest harvest management strategies, and harvesting strategies can be selected accordingly. However, for polar climates, any logging strategy would exceed the carrying capacity of eco- logical wood. The ecology can only partially adapt to natural development strategies (c), and therefore deforestation should not occur in these areas.

<!-- b000563 | heading | pages [18] -->
6.2.2 Forest Management Strategies In Special Situations

<!-- b000564 | prose | pages [18] -->
Some forest areas bear important ecological conservation tasks, and the governments of the countries concerned also regard the conservation of forest areas as the primary goal of forest area development, such as Ratanakiri Forest Reserve in Cambodia, Parsar Forest Reserve in Myanmar, and Jiufeng Forest Reserve in China, etc. Such areas rest and conservation The policy of rest and conservation is the mainstream of such forests. At this time

<!-- b000565 | prose | pages [18] -->
, so the existence of this situation makes the forest almost not deforested.

<!-- b000566 | heading | pages [18] -->
6.3 Example of Subtropical Forest Management and Decision Making

<!-- b000567 | prose | pages [18] -->
Using the above mapping model and management strategies, a subtropical forest in south- ern China is used as an example to find the forest management strategy under optimal value. The effective value interval under timber price change is also estimated while constructing the effective value interval.

<!-- b000568 | prose | pages [18] -->
It was found that a 20% reduction in logging of mature trees (D trees) could shift the

<!-- b000569 | prose | pages [18] -->
effective value range to the left due to the increase in forest ecological diversity, but a greater reduction in logging of mature trees would lead to an ineffective value range. This suggests that the effect of ecosystem diversity on the effective range of values is limited, and that the effective range for logging D trees is . , the effective interval of value is plotted when the Under the condition of felling rate of fully mature trees is 80%. In the current world carbon trading price fluctuation market: as the carbon trading price increases, the felling rate for C-aged trees also gets de- creased, with the minimum felling rate being 41.5% for C-aged trees and the maximum felling rate being 83%. As shown in the blue area of the figure.

<!-- b000570 | prose | pages [18] -->
（60$)

<!-- b000571 | prose | pages [18] -->
Total Carbon Sequestration Wood Materials Carbon Sequestration

<!-- b000572 | prose | pages [18] -->
Interval division

<!-- b000573 | prose | pages [18] -->
Value inefficient (0%~25%; 83%~100%) No viable forest value management strategy at this stage. Carbon sequestration effective(25%~50%)

<!-- b000574 | prose | pages [18] -->
(2$)

<!-- b000575 | prose | pages [18] -->
Total steady-state carbon sequestration in the system reaches its maximum at this stage. Value effective (42%~83%)  2$~60$ Depending on the carbon tax price, it is possible to achieve value efficient.

<!-- b000576 | furniture | pages [18] -->


<!-- b000577 | prose | pages [18] -->
Figue 11: Scope of management strategy under value balance Considering carbon sequestration, the proposed plan for this forest is to log only 80% of the mature trees (category D) in each time period t (10-15 years) and retain 20% to maintain ecosystem diversity. For near-mature trees (category C), the logging rate is controlled within

<!-- b000578 | prose | pages [19] -->
the range of 41.5% to 55% according to the carbon trading price, which is a value effective and carbon sequestration enhancement.

<!-- b000579 | prose | pages [19] -->
It is calculated that every 100𝑘𝑚2 of forest in 100 years can absorb 442.2~820.8 kilotons of carbon dioxide from the natural state and implement relevant management strategies. The net increase of carbon retention in the system is 68~88 kilotons.

<!-- b000580 | heading | pages [19] -->
7 Demand-sensitive Management Strategy Game

<!-- b000581 | prose | pages [19] -->
Ignoring the influence of extreme cases such as policies, for a general forest area, it bal- ances ecological, economic and social benefits. Inspired by game theory in sociology and eco- nomics, we divide the managers of forest land and local residents into two game subjects. For non-extreme climate forests, we analyze the impact of the change in management strategy on both.

<!-- b000582 | heading | pages [19] -->
7.1 The Game of Forest Management Strategies

<!-- b000583 | prose | pages [19] -->
The following is the payment matrix for both based on multiple objective planning.

<!-- b000584 | caption | pages [19] -->
Table 4: Payment matrix between forest managers and local residents

<!-- b000585 | prose | pages [19] -->
Local residents (B)

<!-- b000586 | furniture | pages [19] -->


<!-- b000587 | furniture | pages [19] -->


<!-- b000588 | prose | pages [19] -->
Value Support (𝛽)

<!-- b000589 | prose | pages [19] -->
Harvesting

<!-- b000590 | prose | pages [19] -->
Against (1 −𝛽)

<!-- b000591 | prose | pages [19] -->
𝐶𝐹𝑚𝑎𝑥+ 𝐺𝐸𝑃−𝑀𝐹0 + 𝐶𝐹𝑚𝑎𝑥+ 𝐺𝐸𝑃+ 𝐸𝐹, 𝐸𝐹−𝑀𝐹0 (𝛼)

<!-- b000592 | prose | pages [19] -->
Forest Manager

<!-- b000593 | prose | pages [19] -->
(A)

<!-- b000594 | prose | pages [19] -->
Self-cultivation

<!-- b000595 | prose | pages [19] -->
𝐶𝐹+𝐺𝐸𝑃

<!-- b000596 | prose | pages [19] -->
𝐸𝐹, 𝐿𝐹𝑚𝑖𝑛+ 𝑀𝐹0

<!-- b000597 | prose | pages [19] -->
𝐶𝐹

<!-- b000598 | prose | pages [19] -->
+ 𝑀𝐹0, 𝑀𝐹𝑚𝑎𝑥+ 𝐿𝐹0

<!-- b000599 | prose | pages [19] -->
(1 −𝛼)

<!-- b000600 | prose | pages [19] -->
2

<!-- b000601 | furniture | pages [19] -->


<!-- b000602 | prose | pages [19] -->
2 + 𝐺𝐸𝑃0 + 𝑀𝐹0, 𝐿𝐹𝑚𝑎𝑥−𝑀𝐹0

<!-- b000603 | furniture | pages [19] -->


<!-- b000604 | prose | pages [19] -->
In the matrix, if the forest manager chooses intermittent logging, he can get a maximum carbon value gain and also economic gain regardless of whether the local residents support it or not, the difference is that the government is influenced by public opinion and it is difficult to give the interest of carbon tax transfer to the forest manager normally; while the forest man- ager chooses restoration and conservation, he does not get the full carbon due to the represen- tation in the gain curve proved above The forest manager who chooses conservation does not get the full carbon value and ecological value, but will definitely get a certain amount of carbon tax compensation. Therefore, for the forest manager, the expectation function is:

<!-- b000605 | prose | pages [19] -->
(24)

<!-- b000606 | prose | pages [19] -->
If the residents choose to support any of the actions of the forest, the economic compensa- tion will be different depending on the strategy of the forest; if the residents choose to defend their interests and not to support the forest, the strategy of the forest will have a different impact on the residents, which is expressed in the fluctuation of the tourism income and the carbon tax transfer will be given to the forest or the residents, depending on the situation. Therefore, for the local residents, the expectation function is:

<!-- b000607 | furniture | pages [20] -->


<!-- b000608 | prose | pages [20] -->
(25)

<!-- b000609 | furniture | pages [20] -->


<!-- b000610 | caption | pages [20] -->
Figure 12: Evolutionary game of policy preference

<!-- b000611 | prose | pages [20] -->
The MATLAB program was used to perform a dynamic evolutionary game between the two subjects to obtain the results of the final deforestation strategy adopted when using the strategy designed above, under the pressure of support or non-support of the population. It can be found that forest management subjects with the strongest restoration policy tendencies (1 - α = 0.8) and when restoration and deforestation strategies are insensitive (at α = 0.5) also even- tually tend to adopt the optimized deforestation strategy gradually in the course of the game.

<!-- b000612 | heading | pages [20] -->
7.2 Evolutionary game simulation for managing plan transitions

<!-- b000613 | prose | pages [20] -->
It has been demonstrated above that for non-extreme climate forests, there is no strategy for forest managers to choose not to cut the forest in general. Strategy 1 is the utility of the original management policy (excessive deforestation tendency) and Strategy 2 is the optimized forest management policy: moderate deforestation tendency, i.e., by extending the deforesta

<!-- b000614 | caption | pages [20] -->
Figure 13: Simulation of optimization policy application from the perspective of game

<!-- b000615 | prose | pages [21] -->
tion cycle t (10 years longer recovery than the original cycle), the forest is allowed to grow for a longer period of time. In order to analyze the value game situation of the two management strategies in the transition process. In the following, we will continue to simulate the applica- tion of the management policies using the evolutionary game approach. In the simulation pro- cess the management policy utility is simulated with the original management utility of the six major forest species over time to observe the process and results of the game, as shown in the following figure.

<!-- b000616 | prose | pages [21] -->
In all simulated scenarios, the new optimized policy has an intersection with the original policy after application and gradually reaches the maximum benefit afterwards; while even the extreme protection case has an intersection with the original policy in the process of benefit decline. Therefore, the new forest management policies constructed above are substitutes for different types of old policies within a certain period.

<!-- b000617 | heading | pages [21] -->
8 Sensitivity Analysis

<!-- b000618 | prose | pages [21] -->
Since many adjustments have been made to the forest ecological and economic manage- ment model by changing the coefficients above, and different types of simulations have been carried out according to the actual situation, the range of sensitivity to changes in controllable system parameters or surrounding conditions has been obtained. better output results. There- fore, we will not continue to observe the changes of the model results repeatedly here.

<!-- b000619 | heading | pages [21] -->
9 Model Evaluation and Further Discussion

<!-- b000620 | heading | pages [21] -->
9.1 Strengths

<!-- b000621 | prose | pages [21] -->
 The model incorporates economic, ecological and social factors, and examines the sustainable development of forest resources from different subjects, positions and perspectives, responding to the goal of "carbon peaking and carbon neutrality".  The model considers not only the general adaptive case but also the consequences of using the policy in extreme cases, and gives corresponding guidance with high practical value of the model.  Reasonable and easy-to-practice evaluation of importance level instructs the re- connaissance effectively.

<!-- b000622 | heading | pages [21] -->
9.2 Weaknesses

<!-- b000623 | prose | pages [21] -->
The overall framework of the model is relatively large, spanning many fields such as eco- nomics, operations research, biology, and geography, and the relationships among the sub- models are complex, which is not conducive to linkage analysis and improvement.

<!-- b000624 | heading | pages [21] -->
9.3 Further Discussion

<!-- b000625 | prose | pages [21] -->
At the international level, we hope to achieve a win-win situation for both ecological and economic values of forest ecosystems through international cooperation rather than single for- est management.

<!-- b000626 | heading | pages [21] -->
10 Conclusion

<!-- b000627 | prose | pages [21] -->
1) Single-minded environmentalism can sometimes hinder the sustainability of forest resources, and sound management policies can achieve enhanced forest carbon se- questration and benefits, tapping into the potential value of forest systems.

<!-- b000628 | prose | pages [22] -->
2) For different regions and ecologies, it is necessary to find their adapted forest man- agement strategies to better protect and develop the forests. 3) A moderate rate of logging and policy preference can guide the application of differ- ent types of forest management strategies so as to balance economic, ecological and social benefits, and to ensure sufficient ecological value while making the best use of things to achieve the highest social and economic value. Finally, we hope that local forest managers can take a longer-term view of forest values, improve operation and management methods, strengthen cooperation and communication with other entities, and learn from advanced management experiences to make forests play a better role in carbon sequestration and truly achieve sustainable development.

<!-- b000629 | furniture | pages [22] -->


<!-- b000630 | heading | pages [22] -->
References

<!-- b000631 | references | pages [22] -->
CHENG Susu, YI Yongxi, LI Shoude. A differential game of transboundary pollution for carbon capture and storage [J].

<!-- b000632 | references | pages [22] -->
[1]

<!-- b000633 | references | pages [22] -->
Journal of Systems & Management,2019,28(05):864-872.

<!-- b000634 | references | pages [22] -->
ZHANG Shuwei, LIU Deshun. Status and development of carbon sequestration technology [J]. Environmental Science

<!-- b000635 | references | pages [22] -->
[2]

<!-- b000636 | references | pages [22] -->
Trends,2005(04):27-29.

<!-- b000637 | references | pages [22] -->
WANG Wei-feng, DUAN Yu-xi, ZHANG Li-xing, WANG Bo, LI Xiao-jing. Effects of different rotations on carbon

<!-- b000638 | references | pages [22] -->
[3]

<!-- b000639 | references | pages [22] -->
sequestration in Chinese fir plantations [J]. Chinese Journal of Plant Ecology,2016,40(07):669-678.

<!-- b000640 | references | pages [22] -->
WANG Wei-feng, DUAN Yu-xi, ZHANG Li-xing, WANG Bo, LI Xiao-jing. Review on Forest carbon sequestration

<!-- b000641 | references | pages [22] -->
[4]

<!-- b000642 | references | pages [22] -->
counting methodology under global Climate change [J]. Journal of Nanjing Forestry University (Natural Sciences Edi-

<!-- b000643 | references | pages [22] -->
tion),2016,40(03):170-176.

<!-- b000644 | references | pages [22] -->
[5]

<!-- b000645 | references | pages [22] -->
Pan, Yude, et al. "A large and persistent carbon sink in the world’s forests." science 333.6045 (2011): 988-993.

<!-- b000646 | references | pages [22] -->
[6]

<!-- b000647 | references | pages [22] -->
Boyd, Philip W., et al. "Multi-faceted particle pumps drive carbon sequestration in the ocean." Nature 568.7752 (2019):

<!-- b000648 | references | pages [22] -->
327-335.

<!-- b000649 | references | pages [22] -->
[7]

<!-- b000650 | references | pages [22] -->
Ontl, Todd A., et al. "Forest management for carbon sequestration and climate adaptation." Journal of Forestry 118.1

<!-- b000651 | references | pages [22] -->
(2020): 86-101.

<!-- b000652 | references | pages [22] -->
[8]

<!-- b000653 | references | pages [22] -->
Noormets, Asko, et al. "Effects of forest management on productivity and carbon sequestration: A review and hypothe-

<!-- b000654 | references | pages [22] -->
sis." Forest Ecology and Management 355 (2015): 124-140.

<!-- b000655 | references | pages [22] -->
[9]

<!-- b000656 | references | pages [22] -->
Mayer, Mathias, et al. "Tamm Review: Influence of forest management activities on soil organic carbon stocks: A

<!-- b000657 | references | pages [22] -->
knowledge synthesis." Forest Ecology and Management 466 (2020): 118127.

<!-- b000658 | references | pages [22] -->
[10] Kurz, Werner A., et al. "Carbon in Canada’s boreal forest—a synthesis." Environmental Reviews 21.4 (2013): 260-292.

<!-- b000659 | references | pages [22] -->
[11] Sahoo, Gyanaranjan, and Afaq Majid Wani. "Forest biotechnology: current trends and future prospects." Int J Curr Mi-

<!-- b000660 | references | pages [22] -->
crobiol Appl Sci 11 (2020): 74-85.

<!-- b000661 | references | pages [22] -->
[12] Pretzsch, Hans, et al. "Changes of forest stand dynamics in Europe. Facts from long-term observational plots and their

<!-- b000662 | references | pages [22] -->
relevance for forest ecology and management." Forest Ecology and Management 316 (2014): 65-77.

<!-- b000663 | references | pages [22] -->
[13] Vogt K A, Gordon J C, Wargo J P, et al. Ecosystems: Balancing Science with Management [M]. New York: Springer,

<!-- b000664 | references | pages [22] -->
1997.

<!-- b000665 | furniture | pages [22] -->


<!-- b000666 | furniture | pages [22] -->


<!-- b000667 | heading | pages [22] -->
11 Forest Carbon Sequestration Science Articles

<!-- b000668 | furniture | pages [22] -->


<!-- b000669 | prose | pages [23] -->
New discoveries in carbon sequestration

<!-- b000670 | furniture | pages [23] -->


<!-- b000671 | prose | pages [23] -->
Shouldn't Any Trees Be Cut Down? Forest management: moderate

<!-- b000672 | furniture | pages [23] -->


<!-- b000673 | prose | pages [23] -->
tree harvesting helps carbon sequestration.

<!-- b000674 | furniture | pages [23] -->


<!-- b000675 | furniture | pages [23] -->


<!-- b000676 | prose | pages [23] -->
Forest Management(2022) MCM/ICM

<!-- b000677 | furniture | pages [23] -->


<!-- b000678 | furniture | pages [23] -->


<!-- b000679 | heading | pages [23] -->
I. Introduction

<!-- b000680 | furniture | pages [23] -->


<!-- b000681 | prose | pages [23] -->
orests are the largest carbon reservoir in terrestrial ecosy-

<!-- b000682 | prose | pages [23] -->
F

<!-- b000683 | furniture | pages [23] -->


<!-- b000684 | prose | pages [23] -->
stems and have a very important and unique role in red-

<!-- b000685 | furniture | pages [23] -->


<!-- b000686 | prose | pages [23] -->
ucing the concentration of greenhouse gases in the atmosp-

<!-- b000687 | furniture | pages [23] -->


<!-- b000688 | prose | pages [23] -->
here and mitigating global warming. Expanding forest

<!-- b000689 | furniture | pages [23] -->


<!-- b000690 | prose | pages [23] -->
Forest Management

<!-- b000691 | prose | pages [23] -->
cover is an important mitigation measure that is economica

<!-- b000692 | furniture | pages [23] -->


<!-- b000693 | prose | pages [23] -->
-lly feasible and less costly in the next 30-50 years. Many

<!-- b000694 | furniture | pages [23] -->


<!-- b000695 | prose | pages [23] -->
countries and international organizations are actively using

<!-- b000696 | furniture | pages [23] -->


<!-- b000697 | prose | pages [23] -->
forest carbon sinks to combat climate change.

<!-- b000698 | furniture | pages [23] -->


<!-- b000699 | prose | pages [23] -->
Shouldn't Any Trees Be Cut Down? Forest management:

<!-- b000700 | prose | pages [23] -->
We have always believed that the best way to protect and

<!-- b000701 | furniture | pages [23] -->


<!-- b000702 | prose | pages [23] -->
moderate tree harvesting

<!-- b000703 | prose | pages [23] -->
manage forests is to "not cut down trees" and so on.

<!-- b000704 | furniture | pages [23] -->


<!-- b000705 | prose | pages [23] -->
helps carbon sequestration.

<!-- b000706 | prose | pages [23] -->
However, recent scientific research has found that the best

<!-- b000707 | furniture | pages [23] -->


<!-- b000708 | heading | pages [23] -->
Table of Contents

<!-- b000709 | contents | pages [23] -->
way to manage forests is to harvest them wisely, and that

<!-- b000710 | furniture | pages [23] -->


<!-- b000711 | contents | pages [23] -->
1

<!-- b000712 | contents | pages [23] -->
Introduction

<!-- b000713 | contents | pages [23] -->
moderate use of wood can, in part, increase the amount of

<!-- b000714 | furniture | pages [23] -->


<!-- b000715 | contents | pages [23] -->
Full Process Carbon Flow       1

<!-- b000716 | contents | pages [23] -->
carbon sequestered by the broader forest ecosystem and its

<!-- b000717 | furniture | pages [23] -->


<!-- b000718 | contents | pages [23] -->
Impact Of Tree Felling On

<!-- b000719 | contents | pages [23] -->
subsequent wood flow. This article will help you to

<!-- b000720 | furniture | pages [23] -->


<!-- b000721 | contents | pages [23] -->
Carbon Sequestration            2

<!-- b000722 | contents | pages [23] -->
understand this by looking at the "whole process of wood

<!-- b000723 | contents | pages [23] -->
Eliminate Subjective Bias       2

<!-- b000724 | contents | pages [23] -->
movement" and "carbon sequestration systems".

<!-- b000725 | furniture | pages [23] -->


<!-- b000726 | furniture | pages [23] -->


<!-- b000727 | heading | pages [23] -->
II. Full Process Carbon Flow

<!-- b000728 | furniture | pages [23] -->


<!-- b000729 | furniture | pages [23] -->


<!-- b000730 | furniture | pages [23] -->


<!-- b000731 | furniture | pages [23] -->


<!-- b000732 | furniture | pages [23] -->


<!-- b000733 | furniture | pages [23] -->


<!-- b000734 | furniture | pages [23] -->


<!-- b000735 | furniture | pages [23] -->


<!-- b000736 | furniture | pages [23] -->


<!-- b000737 | furniture | pages [23] -->


<!-- b000738 | furniture | pages [23] -->


<!-- b000739 | furniture | pages [23] -->


<!-- b000740 | furniture | pages [23] -->


<!-- b000741 | furniture | pages [23] -->


<!-- b000742 | furniture | pages [23] -->


<!-- b000743 | furniture | pages [23] -->


<!-- b000744 | furniture | pages [23] -->


<!-- b000745 | furniture | pages [23] -->


<!-- b000746 | heading | pages [23] -->
Abstract

<!-- b000747 | prose | pages [23] -->
Reducing CO2 in the atm- osphere requires protecti- ng forests and not cutting- g down trees. This is what we usually used to think. However, Shouldn't Any Trees Be Cut Down? is the best way to manage fores- ts to reduce greenhouse gases? The answer is no. By dismantling and analyz- ing the whole process of wood carbon sequestrate- on system, we found that the real situation is that the rational harvesting and utilization of wood is ben- eficial to the total carbon sequestration of the syste- m.

<!-- b000748 | caption | pages [23] -->
Fig. 1 Forest Carbon Flow System And Wood Products Carbon Flow System

<!-- b000749 | prose | pages [23] -->
[The diagram describes the process of carbon sequestration circulation in wood.]

<!-- b000750 | prose | pages [23] -->
Page1

<!-- b000751 | prose | pages [24] -->
New discoveries in carbon sequestration

<!-- b000752 | furniture | pages [24] -->


<!-- b000753 | furniture | pages [24] -->


<!-- b000754 | prose | pages [24] -->
Shouldn't Any Trees Be Cut Down? Forest management: moderate tree harvesting helps carbon sequestration.

<!-- b000755 | furniture | pages [24] -->


<!-- b000756 | furniture | pages [24] -->


<!-- b000757 | prose | pages [24] -->
Forest Management(2022) MCM/ICM

<!-- b000758 | furniture | pages [24] -->


<!-- b000759 | furniture | pages [24] -->


<!-- b000760 | heading | pages [24] -->
III. Impact Of Tree Felling On Carbon Sequestration .

<!-- b000761 | furniture | pages [24] -->


<!-- b000762 | prose | pages [24] -->
A scientific study has developed a complete scientific and mathematical model that can

<!-- b000763 | furniture | pages [24] -->


<!-- b000764 | prose | pages [24] -->
simulate the carbon sequestration system described above. The simulated carbon seque-

<!-- b000765 | furniture | pages [24] -->


<!-- b000766 | prose | pages [24] -->
stration effect of the system is shown in Figure 2. It was found that, from the long-term

<!-- b000767 | furniture | pages [24] -->


<!-- b000768 | prose | pages [24] -->
development perspective, compared with the carbon sequestration level in the natural

<!-- b000769 | furniture | pages [24] -->


<!-- b000770 | prose | pages [24] -->
state without deforestation: the carbon sequestration level of the whole system was

<!-- b000771 | furniture | pages [24] -->


<!-- b000772 | prose | pages [24] -->
enhanced by moderate cutting of trees in each cycle (30% for under-mature trees and

<!-- b000773 | furniture | pages [24] -->


<!-- b000774 | prose | pages [24] -->
100% for fully mature trees); the carbon sequestration level of the whole system was

<!-- b000775 | furniture | pages [24] -->


<!-- b000776 | prose | pages [24] -->
enhanced by excessive cutting in each cycle (60% for under-mature trees and 100% for

<!-- b000777 | furniture | pages [24] -->


<!-- b000778 | prose | pages [24] -->
fully For each cycle of overcutting (60% for under-mature trees and 100% for mature

<!-- b000779 | furniture | pages [24] -->


<!-- b000780 | prose | pages [24] -->
trees), the carbon sequestration level of the whole system was increased only at the

<!-- b000781 | furniture | pages [24] -->


<!-- b000782 | prose | pages [24] -->
initial stage, but decreased significantly in the long term.

<!-- b000783 | furniture | pages [24] -->


<!-- b000784 | furniture | pages [24] -->


<!-- b000785 | prose | pages [24] -->
Kton(𝐶𝑂2)

<!-- b000786 | furniture | pages [24] -->


<!-- b000787 | prose | pages [24] -->
(a)

<!-- b000788 | furniture | pages [24] -->


<!-- b000789 | furniture | pages [24] -->


<!-- b000790 | furniture | pages [24] -->


<!-- b000791 | furniture | pages [24] -->


<!-- b000792 | furniture | pages [24] -->


<!-- b000793 | prose | pages [24] -->
(b)

<!-- b000794 | furniture | pages [24] -->


<!-- b000795 | furniture | pages [24] -->


<!-- b000796 | furniture | pages [24] -->


<!-- b000797 | furniture | pages [24] -->


<!-- b000798 | prose | pages [24] -->
(c)

<!-- b000799 | furniture | pages [24] -->


<!-- b000800 | furniture | pages [24] -->


<!-- b000801 | furniture | pages [24] -->


<!-- b000802 | prose | pages [24] -->
The carbon sequestration system reaches a relatively steady-state stage, where the amount of carbon sequ

<!-- b000803 | prose | pages [24] -->
Kton(𝐶𝑂2)

<!-- b000804 | prose | pages [24] -->
estered by each subject be- gins to vary little or not at all.

<!-- b000805 | prose | pages [24] -->
(a)Moderate deforestation. Mature trees are cut down. Only 30% of nearly mature t

<!-- b000806 | prose | pages [24] -->
Kton(𝐶𝑂2)

<!-- b000807 | prose | pages [24] -->
rees are cut.

<!-- b000808 | prose | pages [24] -->
(b)No logging of the forest, the forest grows naturally.

<!-- b000809 | prose | pages [24] -->
No logging of the forest, the fore (c)Over-harvesting. 60% of a st grows naturally. ll t-rees near mature age wer

<!-- b000810 | prose | pages [24] -->
Kton(𝐶𝑂2)

<!-- b000811 | prose | pages [24] -->
e harv-ested, and all mature

<!-- b000812 | prose | pages [24] -->
t

<!-- b000813 | prose | pages [24] -->
Based on a model of forest age classificationTime phase

<!-- b000814 | furniture | pages [24] -->


<!-- b000815 | prose | pages [24] -->
Carbon sequestration level

<!-- b000816 | furniture | pages [24] -->


<!-- b000817 | prose | pages [24] -->
trees were harvested.

<!-- b000818 | caption | pages [24] -->
Fig. 2 Carbon Sequestration System Simulation(                )

<!-- b000819 | furniture | pages [24] -->


<!-- b000820 | prose | pages [24] -->
[The simulation results reflect the different impacts on different levels of deforestation.]

<!-- b000821 | furniture | pages [24] -->


<!-- b000822 | heading | pages [24] -->
IV. Eliminate subjective bias but be vigilant.

<!-- b000823 | furniture | pages [24] -->


<!-- b000824 | prose | pages [24] -->
An understanding of forest carbon flux and sequestration provides a better underst-

<!-- b000825 | furniture | pages [24] -->


<!-- b000826 | prose | pages [24] -->
anding of forest management and use. Moderate deforestation and full use of wood

<!-- b000827 | furniture | pages [24] -->


<!-- b000828 | prose | pages [24] -->
can enhance carbon sequestration. On the other hand, excessive deforestation can

<!-- b000829 | furniture | pages [24] -->


<!-- b000830 | prose | pages [24] -->
reduce carbon sequestration in the long run and destroy much of the potential value

<!-- b000831 | furniture | pages [24] -->


<!-- b000832 | prose | pages [24] -->
of forest ecology, something we need to be wary of. We need to remember that forests

<!-- b000833 | furniture | pages [24] -->


<!-- b000834 | prose | pages [24] -->
are a precious asset to humanity.

<!-- b000835 | prose | pages [24] -->
Page2

<!-- b000836 | heading | pages [25] -->
Appendix

<!-- b000837 | prose | pages [25] -->
Model Evaluation

<!-- b000838 | furniture | pages [25] -->


<!-- b000839 | furniture | pages [25] -->


<!-- b000840 | prose | pages [25] -->
Software & Tools Matlab; Python; Sufer; Tableau; PowerPoint ;Origin

<!-- b000841 | furniture | pages [25] -->


<!-- b000842 | prose | pages [25] -->
Core algorithms and Procedures def best_carbon(miu_a): t = np.arange(0, 60, 0.05)

<!-- b000843 | furniture | pages [25] -->


<!-- b000844 | prose | pages [25] -->
track1 = odeint(lorenz, (24*22.5,23*30 , 0), t, args=(22.5, 30.0,miu_a,1)) return np.sum(track1,axis=1).reshape(-1,1)[-1]+27*7.5+25.6*15 def result(i,j): t = np.arange(0, 60, 0.0005) track = odeint(carbon_z, (24*22.5,23*30 , 0), t, args=(22.5, 30.0,i,j)) rt=track[:, 2].reshape(-1,1)[-1][0] return [i,j,rt] set(gca,&apos;XTick&apos;,[0:1:5],&apos;YTick&apos;,[0:0.2:1]) xlabel(&apos;&apos;, &apos;interpreter&apos;,&apos;latex&apos;); ylabel(&apos;Strategy&apos;,&apos;interpreter&apos;,&apos;la- tex&apos;)% 5&apos;rotation&apos;,360); title(&apos;northern broadleaf forest&apos;); legend(&apos;Strategy 1 &apos;,&apos;Strategy 2&apos;);

<!-- b000845 | furniture | pages [25] -->

