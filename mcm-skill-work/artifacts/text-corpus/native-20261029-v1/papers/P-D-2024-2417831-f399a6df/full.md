# P-D-2024-2417831-f399a6df

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | furniture | pages [1] -->
2024

<!-- b000003 | prose | pages [1] -->
Problem Chosen

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
D

<!-- b000006 | furniture | pages [1] -->
2417831

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Harmony of the Great Lakes: A Water Level Balance

<!-- b000009 | title | pages [1] -->
Approach

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
The Great Lakes represent 20% of the world’s freshwater resources, making their management, especially in water level, critically important. Fluctuations in their water levels are influenced by a myriad of natural factors and involve a diverse group of stakeholders. Consequently, developing a management plan and controlling the water levels of these lakes present a challenge.

<!-- b000013 | prose | pages [1] -->
For Task1: A genetic algorithm model is established considering coastal protection costs, hydro-power generation, leisure satisfaction, shipping benefits, and ecological impacts. By utilizing benefit functions and the Analytic Hierarchy Process (AHP), this model efficiently assesses the interests of stakeholders. Besides, the model particular focuses on coastal protection costs and hydroelectric power generation. It ultimately

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
establishes the optimal water level for the Great Lakes on a monthly basis.

<!-- b000016 | prose | pages [1] -->
For Task2: We develop a hydrodynamic model tailored to the Great Lakes, account- ing for both the flow dynamics within the lake chain and external variables affecting it. Following this, we craft distinct water level control algorithms for the Compensating Works and the Moses-Saunders Dam. These algorithms integrate a mode-switchable feedback controller with a prediction module, enhancing the controller’s responsive- ness by optimizing feedback gains for superior performance amidst environmental fluctuations. Simulations conducted using our model confirm the efficacy of these al- gorithms.

<!-- b000017 | prose | pages [1] -->
For Task 3: By increasing the outflow at the Soo Locks (upstream) and the Moses-

<!-- b000018 | heading | pages [1] -->
Saunders Dam (downstream), we evaluated their sensitivity to water level manage-

<!-- b000019 | prose | pages [1] -->
ment. Our analysis reveals that the upstream dam predominantly affects Lake Supe- rior, Lake Michigan, Lake Huron, and Lake Erie, whereas the downstream dam has a more significant impact on the remaining lakes. When compared to water levels in 2017, our model demonstrates improved performance in numerous aspects.

<!-- b000020 | prose | pages [1] -->
For Task 4: We introduce dynamic scenarios into the simulation, including heavy precipitation and ice jams, to assess the sensitivity and resilience of our model against environmental changes. The results show that our algorithms are more effective in preventing significant increases in water levels following heavy rainfall events than natural regulatory methods. Furthermore, when ice jam occurs, the time needed to recover water levels decreases through enhanced upstream discharge.

<!-- b000021 | prose | pages [1] -->
For Task 5: Focusing on the key factors and stakeholders affecting Lake Ontario, we identified the water flow from the Ottawa River and the protection of coastal residents in Montreal as significant influences.The analysis emphasizes that to reach an effective regulation requires seasonal adjustments and collaborative efforts to protect coastal communities and maintain ecological balance.

<!-- b000022 | prose | pages [1] -->
In conclusion, our model has the strength of robustness and comprehensiveness. This provides scientific guidance and support for the regulation of the Great Lakes in the future.

<!-- b000023 | keywords | pages [1] -->
Keywords: Prediction-based feedback control, Lake chain simulation, Multi-objective

<!-- b000024 | prose | pages [1] -->
optimization, Genetic algorithm 关注数学模型

<!-- b000025 | furniture | pages [1] -->
2

<!-- b000026 | furniture | pages [1] -->
MATHmodels

<!-- b000027 | furniture | pages [1] -->
获取更多资讯

<!-- b000028 | furniture | pages [2] -->
Team # 2417831

<!-- b000029 | furniture | pages [2] -->
Page 2 of 25

<!-- b000030 | heading | pages [2] -->
Contents

<!-- b000031 | contents | pages [2] -->
1

<!-- b000032 | heading | pages [2] -->
Introduction

<!-- b000033 | prose | pages [2] -->
3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Background 3

<!-- b000034 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000035 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Assumptions and Justifications . . . . . . . . . . . . . . . . . . . . . . . . 1.3 3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4 4 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.5 4

<!-- b000036 | prose | pages [2] -->
Task 1: Determination of the Optimal Water Level 2 5 Introducing Genetic Algorithm . . . . . . . . . . . . . . . . . . . . . . . . 2.1 5 Determination of the Benefit Function . . . . . . . . . . . . . . . . . . . . 2.2 5 Analysis of Weights . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 7 Presentation of Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4 8

<!-- b000037 | heading | pages [2] -->
Task2: Establishment of Algorithms for Water Level Control

<!-- b000038 | prose | pages [2] -->
3 9 Hydrodynamic Model of the Lake Chain 3.1 . . . . . . . . . . . . . . . . . .

<!-- b000039 | prose | pages [2] -->
9

<!-- b000040 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000041 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1 Internal Water Flow 10 External Factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2 12 Control Algorithm Design . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 13 Classical Control Algorithms Synthesis . . . . . . . . . . . . . . . 3.2.1 13 Controller Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.2 13 Mode-switchable Feedback Control module 3.2.3 . . . . . . . . . . . .

<!-- b000042 | prose | pages [2] -->
14 Prediction Module . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.4 15 Algorithm Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 16

<!-- b000043 | heading | pages [2] -->
Task 3: Sensitivity Analysis on Outflow of the Two Dam Controllers

<!-- b000044 | prose | pages [2] -->
4 17 System Sensitivity on Control Output 4.1 . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | prose | pages [2] -->
17 A Comparison with Water Level in 2017 . . . . . . . . . . . . . . . . . . . 4.2 18

<!-- b000046 | heading | pages [2] -->
Task 4: Sensitivity analysis to environmental changes

<!-- b000047 | prose | pages [2] -->
5 18 Algorithm Sensitivity to Heavy Precipitation . . . . . . . . . . . . . . . . 5.1 18 Algorithm Sensitivity to Ice Jam . . . . . . . . . . . . . . . . . . . . . . . . 5.2

<!-- b000048 | prose | pages [2] -->
6 Task 5: Focusing on Lake Ontario

<!-- b000049 | prose | pages [2] -->
20

<!-- b000050 | prose | pages [2] -->
21 Social and Physical Geographical Analysis 6.1 . . . . . . . . . . . . . . . . .

<!-- b000051 | prose | pages [2] -->
21 . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 Reanalysis of Stakeholders 22

<!-- b000052 | heading | pages [2] -->
Model Evaluation and Further Discussion

<!-- b000053 | prose | pages [2] -->
7 23 Model Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 23 Model Weaknesses and Further Discussion . . . . . . . . . . . . . . . . . 7.2

<!-- b000054 | prose | pages [2] -->
A Memo to IJC Leadership

<!-- b000055 | heading | pages [2] -->
References

<!-- b000056 | references | pages [2] -->
23

<!-- b000057 | references | pages [2] -->
24

<!-- b000058 | references | pages [2] -->
25

<!-- b000059 | references | pages [2] -->
关注数学模型

<!-- b000060 | furniture | pages [2] -->
2

<!-- b000061 | furniture | pages [2] -->
MATHmodels

<!-- b000062 | furniture | pages [2] -->
获取更多资讯

<!-- b000063 | furniture | pages [3] -->
Team # 2417831

<!-- b000064 | references | pages [3] -->
1

<!-- b000065 | heading | pages [3] -->
Introduction

<!-- b000066 | prose | pages [3] -->
1.1

<!-- b000067 | heading | pages [3] -->
Background

<!-- b000068 | furniture | pages [3] -->
Page 3 of 25

<!-- b000069 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000070 | prose | pages [3] -->
The Great Lakes, spanning the United States and Canada, constitute the world’s Vital for fishing, recreation, power generation, and largest freshwater lake group. more, these interconnected lakes pose complex challenges in water management. Bal- ancing the needs of diverse stakeholders, including urban areas, is crucial. Factors like temperature, wind, precipitation, and human-controlled mechanisms impact wa- ter levels. The central role in this balance is played by two primary control mecha- nisms: the Soo Locks and Moses-Saunders Dam.

<!-- b000071 | prose | pages [3] -->
Despite human control over certain elements, natural occurrences such as rain, evaporation, and ice jams remain beyond manipulation. Local policies and environ- mental changes can yield unexpected effects, impacting the ecosystem and residents. Even slight deviations from normal water levels significantly affect stakeholders. This

<!-- b000072 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000073 | prose | pages [3] -->
"wicked" dynamic network flow problem embodies exceptional complexity, marked by interdependencies, intricate requirements, and inherent uncertainties. Effective man- agement is essential to sustain the ecological health of the region and the well-being of its inhabitants.

<!-- b000074 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000075 | prose | pages [3] -->
In light of the background information and constraints highlighted in the problem statement, we need to tackle the following tasks:

<!-- b000076 | prose | pages [3] -->
1. Balance the interests of all parties in determining the optimal level of the Great Lakes for each month of the year.

<!-- b000077 | prose | pages [3] -->
2. Create algorithms to maintain optimal water levels in five lakes according to in- flow and outflow data of the lakes.

<!-- b000078 | prose | pages [3] -->
3. Analyze the sensitivity of the control algorithms to the two control dams using data from 2017 and test whether the control algorithm satisfies or outperforms the actual water level for each stakeholder.

<!-- b000079 | prose | pages [3] -->
4. Examine the sensitivity of control algorithms to environmental changes.

<!-- b000080 | prose | pages [3] -->
5. Focus the analysis on Lake Ontario and analyze the stakeholders and factors af- fecting the lake.

<!-- b000081 | heading | pages [3] -->
Assumptions and Justifications

<!-- b000082 | prose | pages [3] -->
1.3

<!-- b000083 | prose | pages [3] -->
To streamline the problem and facilitate the simulation of real-life conditions, we have made several fundamental assumptions. These assumptions have been carefully justi- fied.

<!-- b000084 | heading | pages [3] -->
• Assumption: The water flow between Lake Michigan and Lake Huron does

<!-- b000085 | heading | pages [3] -->
not influence our model

<!-- b000086 | prose | pages [3] -->
• Justification: According to the data given in the Addendum, the water level of Lake Michigan and that of Lake Huron are the same.

<!-- b000087 | prose | pages [3] -->
关注数学模型

<!-- b000088 | furniture | pages [3] -->
2

<!-- b000089 | furniture | pages [3] -->
MATHmodels

<!-- b000090 | furniture | pages [3] -->
获取更多资讯

<!-- b000091 | furniture | pages [4] -->
Team # 2417831

<!-- b000092 | furniture | pages [4] -->
Page 4 of 25

<!-- b000093 | prose | pages [4] -->
• Assumption: Consider the average water level of historical data as the initial value for the optimal water level, then iterate to seek an improved solution. • Justification: Manually controlled water level variations are much lower than normal lake depths or natural lake levels, so the optimum level must be near the

<!-- b000094 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000095 | prose | pages [4] -->
average level given by historical data.

<!-- b000096 | prose | pages [4] -->
1.4 Our Work

<!-- b000097 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000098 | caption | pages [4] -->
Figure 1: Our Work

<!-- b000099 | prose | pages [4] -->
1.5

<!-- b000100 | heading | pages [4] -->
Notation

<!-- b000101 | caption | pages [4] -->
Table 1: Notation

<!-- b000102 | prose | pages [4] -->
Meaning Glossary

<!-- b000103 | prose | pages [4] -->
S

<!-- b000104 | prose | pages [4] -->
Unit

<!-- b000105 | prose | pages [4] -->
Benefit Function hi / m The Water Level of Lakes hi0 m The Historical Average Water Level of Lakes B1 Global Temperature B2 / Environmental Pollution Degree B3 / The Balance of the Ecosystem A / km2 Area of the lake

<!-- b000106 | prose | pages [4] -->
Outflow of the ith Lake Qout(i) m3/s Inflow of the ith Lake Qin(i) m3/s

<!-- b000107 | prose | pages [4] -->
Note: Some variables are not listed in Table 1 and will be discussed in detail in each section.

<!-- b000108 | prose | pages [4] -->
关注数学模型

<!-- b000109 | furniture | pages [4] -->
2

<!-- b000110 | furniture | pages [4] -->
MATHmodels

<!-- b000111 | furniture | pages [4] -->
获取更多资讯

<!-- b000112 | furniture | pages [5] -->
Team # 2417831

<!-- b000113 | furniture | pages [5] -->
Page 5 of 25

<!-- b000114 | prose | pages [5] -->
Task 1: Determination of the Optimal Water Level 2

<!-- b000115 | heading | pages [5] -->
Introducing Genetic Algorithm

<!-- b000116 | prose | pages [5] -->
2.1

<!-- b000117 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000118 | prose | pages [5] -->
A genetic algorithm is an optimization algorithm that mimics the natural selection and hereditary mechanism and is mainly used to solve optimization problems. It sim- ulates the process of inheritance, crossover, and mutation in the process of biological evolution, and gradually searches for the globally optimal solution by continuously evolving excellent individuals.

<!-- b000119 | prose | pages [5] -->
Determination of the Benefit Function 2.2

<!-- b000120 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000121 | caption | pages [5] -->
Figure 2: Stakeholders of the Great Lakes

<!-- b000122 | prose | pages [5] -->
The Great Lakes involve a diverse range of stakeholders, including property own- ers, hydro-power generation companies, recreational boaters, shipping companies, and fishers, as shown in Figure 2.

<!-- b000123 | prose | pages [5] -->
(1) Cost of Protecting Coastal Residents

<!-- b000124 | prose | pages [5] -->
As outlined in Plan 2014, the risks associated with increasing lake and river lev- els for residents encompass flooding of lakeside or waterfront residences, along with road damage, necessitating the elevation and fortification of shorelines. The cost is di- rectly proportional to the water level, with higher water levels incurring higher costs. Conversely, lower water levels allow the original protection measures to suffice. This situation can be aptly described using a step function

<!-- b000125 | prose | pages [5] -->
y = ϵ(x) =

<!-- b000126 | prose | pages [5] -->
(

<!-- b000127 | prose | pages [5] -->
0 x < 0 (1) x ≥0 1

<!-- b000128 | prose | pages [5] -->
As the level ascends, it can be postulated that the associated costs are directly pro- portional to the fluctuations in water level, the extent of the lake shoreline, and the density of the neighboring population. It is evident that in sparsely populated re- gions, the apprehension regarding the perils of rising water levels on residential prop- erties diminishes.

<!-- b000129 | prose | pages [5] -->
关注数学模型

<!-- b000130 | furniture | pages [5] -->
2

<!-- b000131 | furniture | pages [5] -->
MATHmodels

<!-- b000132 | furniture | pages [5] -->
获取更多资讯

<!-- b000133 | furniture | pages [6] -->
Team # 2417831

<!-- b000134 | furniture | pages [6] -->
Page 6 of 25

<!-- b000135 | prose | pages [6] -->
Therefore, we can conclude the cost function of protecting coastal residents:

<!-- b000136 | prose | pages [6] -->
5

<!-- b000137 | prose | pages [6] -->
hi −hi0

<!-- b000138 | prose | pages [6] -->
X

<!-- b000139 | prose | pages [6] -->
S =

<!-- b000140 | prose | pages [6] -->
hi0

<!-- b000141 | prose | pages [6] -->
· ϵ(hi −hi0) · Li · Di (2)

<!-- b000142 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000143 | prose | pages [6] -->
i=1

<!-- b000144 | prose | pages [6] -->
where the subscript i is indicative of each specific lake. Furthermore, Li is the coeffi- cient about the length of the lake shoreline, and Di signifies the coefficient associated with residential density. Evidently, when under manual control, a more favorable out- come is achieved with a smaller value for S.

<!-- b000145 | prose | pages [6] -->
(2) Revenue of Hydro-power Plant

<!-- b000146 | prose | pages [6] -->
Undoubtedly, the power generation of a hydro-power plant exhibits a positive cor- relation with the height of the waterfall. To elaborate further, this relationship can be mathematically expressed as power difference ∝altitude potential energy capacity ∝kinetic energy ∝ generation difference. Thus, the benefits derived from alterations in water level are as follows:

<!-- b000147 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000148 | prose | pages [6] -->
3

<!-- b000149 | prose | pages [6] -->
Qi × hi·up −hi·down

<!-- b000150 | prose | pages [6] -->
X

<!-- b000151 | prose | pages [6] -->
S =

<!-- b000152 | prose | pages [6] -->
i=1

<!-- b000153 | prose | pages [6] -->
(3)

<!-- b000154 | prose | pages [6] -->
hi0·up −hi0·down

<!-- b000155 | prose | pages [6] -->
where the subscripts i denote the three major hydro-power plants. Qi represents the power generation of each respective hydro-power plant.

<!-- b000156 | prose | pages [6] -->
(3) Leisure Satisfaction

<!-- b000157 | prose | pages [6] -->
Recreational boaters have expressed a preference for consistent periodic water flows, dictated by the conditions of both upstream and downstream lakes. They observed that increased variability in water levels throughout the twelve months leads to less stability in the flow, while minimal fluctuations result in a more stable flow. Con- sequently, higher levels of recreational satisfaction are associated with a more stable flow.

<!-- b000158 | prose | pages [6] -->
The assessment of the magnitude of water level changes throughout the year is conducted through the calculation of the standard deviation for each lake. It can be visualized by the equation:

<!-- b000159 | prose | pages [6] -->
sP12

<!-- b000160 | prose | pages [6] -->


<!-- b000161 | prose | pages [6] -->
5 X

<!-- b000162 | prose | pages [6] -->
ki ·

<!-- b000163 | prose | pages [6] -->
S =

<!-- b000164 | prose | pages [6] -->
i=1

<!-- b000165 | prose | pages [6] -->


<!-- b000166 | prose | pages [6] -->
j=1(hi −µ)2

<!-- b000167 | prose | pages [6] -->
(4) 

<!-- b000168 | prose | pages [6] -->
12

<!-- b000169 | prose | pages [6] -->
where µ is the average water level throughout the year. ki is the proportionality coeffi- cient of the function.

<!-- b000170 | prose | pages [6] -->
(4) Shipping Revenue

<!-- b000171 | prose | pages [6] -->
As lake depths typically exceed ship drafts significantly, fluctuations in lake levels have a limited impact on shipping operations. Shipping concerns are predominantly centered around river levels. When river levels drop too low, it can impede the proper passage of ships. The water level in the river is directly proportional to the river’s flow, and this flow is intricately connected to the levels of lakes both upstream and down- stream. Therefore, the primary metric utilized to characterize this benefit revolves around the disparity between the upstream and downstream lake levels.

<!-- b000172 | prose | pages [6] -->
(5)关注数学模型

<!-- b000173 | prose | pages [6] -->
p

<!-- b000174 | prose | pages [6] -->
Q = ρ · hriver · w ·

<!-- b000175 | prose | pages [6] -->
hup −hdown

<!-- b000176 | furniture | pages [6] -->
2

<!-- b000177 | furniture | pages [6] -->
MATHmodels

<!-- b000178 | furniture | pages [6] -->
获取更多资讯

<!-- b000179 | furniture | pages [7] -->
Team # 2417831

<!-- b000180 | furniture | pages [7] -->
Page 7 of 25

<!-- b000181 | prose | pages [7] -->
Nevertheless, when the lake water level stabilizes in a micro-dynamic equilibrium state, the flow exhibits minimal variation with changes in the water level. The river

<!-- b000182 | prose | pages [7] -->
p

<!-- b000183 | prose | pages [7] -->
water level is inversely proportional to

<!-- b000184 | prose | pages [7] -->
ping revenue can be expressed by:

<!-- b000185 | prose | pages [7] -->
hup −hdown . The benefit function of ship-

<!-- b000186 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000187 | prose | pages [7] -->
5

<!-- b000188 | prose | pages [7] -->
1

<!-- b000189 | prose | pages [7] -->
X

<!-- b000190 | prose | pages [7] -->
Qi,i+1 ·

<!-- b000191 | prose | pages [7] -->
S =

<!-- b000192 | prose | pages [7] -->
p

<!-- b000193 | prose | pages [7] -->
1 ÷

<!-- b000194 | prose | pages [7] -->
(6)

<!-- b000195 | prose | pages [7] -->
p

<!-- b000196 | prose | pages [7] -->
hi·up −hi·down

<!-- b000197 | prose | pages [7] -->
i=1

<!-- b000198 | prose | pages [7] -->
hi0·up −hi0·down

<!-- b000199 | prose | pages [7] -->
where Qi,i+1 represents the water flow between the two lakes and is related to the difference in lake levels and lake water capacity.

<!-- b000200 | prose | pages [7] -->
(5) Ecological Effect

<!-- b000201 | prose | pages [7] -->
The ecological consequences of lake and river water levels are primarily tied to the preservation and disruption of species diversity. To streamline the evaluation of their water level impacts on ecosystems, assessments can be made using the disparity between water level fluctuations, using the average of high water levels and the aver- age of low water levels. A smaller discrepancy between the two is considered a more

<!-- b000202 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000203 | prose | pages [7] -->
favorable benefit function:

<!-- b000204 | prose | pages [7] -->
5

<!-- b000205 | prose | pages [7] -->
ˆ max(hi) − ˆ

<!-- b000206 | prose | pages [7] -->
X

<!-- b000207 | prose | pages [7] -->
S =

<!-- b000208 | prose | pages [7] -->
min(hi)

<!-- b000209 | prose | pages [7] -->
· Ai (7)

<!-- b000210 | prose | pages [7] -->
ˆ max(hi0) − ˆ

<!-- b000211 | prose | pages [7] -->
i=1

<!-- b000212 | prose | pages [7] -->
min(hi0)

<!-- b000213 | prose | pages [7] -->
where Ai represents the impact factor of the lake, which is proportional to the lake area.

<!-- b000214 | prose | pages [7] -->
2.3 Analysis of Weights

<!-- b000215 | prose | pages [7] -->
By employing the Analytic Hierarchy Process (AHP) to evaluate the aforemen- tioned potential factors, we can ascertain the relative weights of the corresponding benefit functions.

<!-- b000216 | prose | pages [7] -->
P H L S E

<!-- b000217 | caption | pages [7] -->
Figure 3: Weight matrix

<!-- b000218 | prose | pages [7] -->
As a result, the total benefit function is:

<!-- b000219 | prose | pages [7] -->
X

<!-- b000220 | prose | pages [7] -->
S = |

<!-- b000221 | prose | pages [7] -->
i=1

<!-- b000222 | caption | pages [7] -->
Table 2: Weight of each factor

<!-- b000223 | prose | pages [7] -->
Stands For Weight

<!-- b000224 | prose | pages [7] -->
Protection for Coastal Infrastructures 0.31 Hydro-power Plant Revenue 0.10 Leisure Satisfaction 0.22 Shipping Revenue 0.10 Ecological Effect 0.27

<!-- b000225 | prose | pages [7] -->
5 5

<!-- b000226 | prose | pages [7] -->
ϵi · Si| (8)

<!-- b000227 | prose | pages [7] -->
where ϵi signifies the weight assigned to each parameter. It’s crucial to emphasize that the aim of the protection cost, life satisfaction, and ecological impact is to minimize the benefit function. Therefore, the weights associated with these aspects should be converted into negative values. Additionally, given the substantial influence of these关注数学模型

<!-- b000228 | furniture | pages [7] -->
2

<!-- b000229 | furniture | pages [7] -->
MATHmodels

<!-- b000230 | furniture | pages [7] -->
获取更多资讯

<!-- b000231 | furniture | pages [8] -->
Team # 2417831

<!-- b000232 | furniture | pages [8] -->
Page 8 of 25

<!-- b000233 | prose | pages [8] -->
three items in the overall weight distribution, it becomes necessary to consider the absolute value of the total benefit function within the fitness function of the genetic model. This approach is essential for determining the probability of selection in the genetic model.

<!-- b000234 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000235 | prose | pages [8] -->
2.4

<!-- b000236 | heading | pages [8] -->
Presentation of Results

<!-- b000237 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000238 | caption | pages [8] -->
Figure 4: Optimal water level V.S. historical mean level

<!-- b000239 | caption | pages [8] -->
Figure 5: Historical average and optimal water level radar chart

<!-- b000240 | prose | pages [8] -->
As shown in Figure 4, the colored lines indicate the optimal water levels for each lake. It is evident that the predicted optimal water levels for all lakes, except for Lake Ontario, are lower than the average of previous years. The observed discrepancy may be attributed to the prioritization of resident safety in the AHP method, as residents generally prefer lower water levels. By examining the radar chart, the benefits of ship- ping and hydro-power plants are already high, with marginal improvements. The关注数学模型

<!-- b000241 | furniture | pages [8] -->
2

<!-- b000242 | furniture | pages [8] -->
MATHmodels

<!-- b000243 | furniture | pages [8] -->
获取更多资讯

<!-- b000244 | furniture | pages [9] -->
Team # 2417831

<!-- b000245 | furniture | pages [9] -->
Page 9 of 25

<!-- b000246 | prose | pages [9] -->
model excels in enhancing resident safety and leisure satisfaction, ensuring readiness for various situations through subsequent control algorithms.

<!-- b000247 | prose | pages [9] -->
However, the improvement in ecosystem benefits is not evident under the optimal

<!-- b000248 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000249 | prose | pages [9] -->
water level. The reason is that after fulfilling the requirements of coastal residents for stable water levels, the cyclic changes in water levels may not reach historical averages, potentially causing disturbances to the ecosystem. Nevertheless, these disturbances are expected to be within the normal self-regulation capacity of the ecosystem.

<!-- b000250 | prose | pages [9] -->
In summary, considering protection for residents, hydro-power revenue, leisure satisfaction, shipping revenue, and ecosystem impacts, the model provides a monthly average optimal water level for the Great Lakes.

<!-- b000251 | heading | pages [9] -->
Task2: Establishment of Algorithms for Water Level

<!-- b000252 | prose | pages [9] -->
3 Control

<!-- b000253 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000254 | prose | pages [9] -->
This task includes model building and an algorithm designed to control the water level of the Great Lakes.

<!-- b000255 | heading | pages [9] -->
Hydrodynamic Model of the Lake Chain

<!-- b000256 | prose | pages [9] -->
3.1

<!-- b000257 | prose | pages [9] -->
This section introduces the hydrodynamic model we established, to simulate the in- terconnected lake system which is simplified and approximated in the following ways:

<!-- b000258 | prose | pages [9] -->
(1) The Great Lakes are modeled as a chain, as shown in Figure 6.

<!-- b000259 | caption | pages [9] -->
Figure 6: Lake chain model schema

<!-- b000260 | prose | pages [9] -->
(2) Inter-lake flow rate equations are derived from Manning’s formula, in which We considered the lake basin shape, the lakes’ relative positions ,and the river channel. Besides, Lake St.Clair is specialized in the model.

<!-- b000261 | prose | pages [9] -->
(3) External factors, including precipitation, evaporation, snow-melt water, and in- dustrial and agricultural water consumption are considered.

<!-- b000262 | prose | pages [9] -->
As illustrated in Figure 7, the general modeling process for the lake chain can be described as follows: external runoff enters Lake Superior, initiating a directional flow through the lake chain shown above, reaching the Atlantic Ocean ultimately. In this se- quential progression, each lake within the lake chain not only receives inflow from the preceding lake but also takes into account external runoff, evaporation, precipitation, snow-melt water, and human factors.

<!-- b000263 | prose | pages [9] -->
During this process, the change in the water level of each lake can be expressed as:

<!-- b000264 | prose | pages [9] -->
dt = Qin(i) −Qout(i)

<!-- b000265 | prose | pages [9] -->
dhi

<!-- b000266 | prose | pages [9] -->
(9)关注数学模型

<!-- b000267 | furniture | pages [9] -->
2

<!-- b000268 | prose | pages [9] -->
Ai

<!-- b000269 | furniture | pages [9] -->
MATHmodels

<!-- b000270 | furniture | pages [9] -->
获取更多资讯

<!-- b000271 | furniture | pages [10] -->
Team # 2417831

<!-- b000272 | furniture | pages [10] -->
Page 10 of 25

<!-- b000273 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000274 | caption | pages [10] -->
Figure 7: Flow directions of the Great Lakes

<!-- b000275 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000276 | prose | pages [10] -->
In the forthcoming sections, we will delineate the parameterization process of our lake chain model, focusing on both the internal water flow within the chain and the exter- nal factors influencing the chain.

<!-- b000277 | prose | pages [10] -->
3.1.1 Internal Water Flow

<!-- b000278 | prose | pages [10] -->
Water flow between lakes stands out as a crucial factor influencing the respective changes in lake water levels. It is influenced by factors including the relative height difference, the characteristics of the river channel connecting the lakes, and the nature of the lake basin. These factors are introduced to our model for precise emulation of the real dynamics of water flow within the lake system.

<!-- b000279 | prose | pages [10] -->
Topography of the lake basin:

<!-- b000280 | prose | pages [10] -->
The presence of lakes exerts a decelerating influence on water flow. Distinct to- pographies of lake basins impart varying capacities to buffer water flow, and features such as irregularities in the lake bottom can impact the flow dynamics. Depressions on the lake bottom may give rise to grooves, introducing friction and resistance to water flow.

<!-- b000281 | caption | pages [10] -->
Table 3: Geographic information of the Great Lakes

<!-- b000282 | prose | pages [10] -->
Michigan+Huron Superior

<!-- b000283 | prose | pages [10] -->
Area (m2) 82103 Mean Depth (m) 147 Annual Precipitation (mm) 760 Evaporation(mm) 596 Elevation (m) 183

<!-- b000284 | prose | pages [10] -->
St. Clair Erie Ontario

<!-- b000285 | prose | pages [10] -->
117620 1100 25874 19000 72 3.4 19 86 787 1720.5 864 914 639 902 697 650 176 173 173 74

<!-- b000286 | prose | pages [10] -->
Geomorphic characteristics of the Great Lakes basins are depicted in Figure 8 and

<!-- b000287 | caption | pages [10] -->
Table 3 with the Lake Erie basin identified as the shallowest and flattest, resulting in the

<!-- b000288 | prose | pages [10] -->
least hindrance to water flow. Conversely, the Lake Superior basin displays a complex geomorphology, leading to a more pronounced impedance to water flow – a facet that 关注数学模型 will be evident in the subsequent modeling process.

<!-- b000289 | furniture | pages [10] -->
2

<!-- b000290 | furniture | pages [10] -->
MATHmodels

<!-- b000291 | furniture | pages [10] -->
获取更多资讯

<!-- b000292 | furniture | pages [11] -->
Team # 2417831

<!-- b000293 | furniture | pages [11] -->
Page 11 of 25

<!-- b000294 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000295 | caption | pages [11] -->
Figure 8: Topography of the Great Lakes

<!-- b000296 | caption | pages [11] -->
Table 4: Geographic information of the rivers

<!-- b000297 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000298 | prose | pages [11] -->
Detroit St. Mary’s

<!-- b000299 | prose | pages [11] -->
Mean Flow Rate (m3/s) 2135 Mean Width (m) 64 Mean Depth (m) 6

<!-- b000300 | prose | pages [11] -->
River channel:

<!-- b000301 | prose | pages [11] -->
Niagara Ottawa St. Lawrence

<!-- b000302 | prose | pages [11] -->
5300 5796 1950 10400 2000 800 2500 3000 12 7 90 11

<!-- b000303 | prose | pages [11] -->
The Manning-Strickler formula characterizes the connection between the flow of unconfined water within a channel and various factors such as channel geometry, bed friction, and current velocity.I t can be expressed as:

<!-- b000304 | prose | pages [11] -->
2 1 3 · E

<!-- b000305 | prose | pages [11] -->
Q = S · R

<!-- b000306 | prose | pages [11] -->
2 (10) n

<!-- b000307 | prose | pages [11] -->
where Q represents the river’s flow rate between the lakes. R denotes the length of the wetted perimeter length along the cross-section of the flow and S represents the cross- sectional area of the river, while the former is positively correlated with the width of the river and the latter with the square of that. n stands for Manning’s friction coefficient, reflecting the resistance on the riverbed. The energy gradient drop E is mainly associated with the river slope which is determined by utilizing the difference in mean heights of the two lakes from Table 3. Given this analysis, the internal flow equations employed in the model for the lake chain can be rewritten as:

<!-- b000308 | prose | pages [11] -->
2 = N0 · w2 · w 2 1 2 1 3 · (g(hi −hi+1) −fi,i+1 · di,i+1) 3 · E

<!-- b000309 | prose | pages [11] -->
S · R

<!-- b000310 | prose | pages [11] -->
8

<!-- b000311 | prose | pages [11] -->
(11) 2

<!-- b000312 | prose | pages [11] -->
1 3 · (g(hi −hi+1) −fi,i+1 · di,i+1)

<!-- b000313 | prose | pages [11] -->
Qout(i) = N · w

<!-- b000314 | prose | pages [11] -->
(12) 2

<!-- b000315 | prose | pages [11] -->
Here, N0 and N are constant coefficients, di,i+1 signifies the distance between the ith

<!-- b000316 | prose | pages [11] -->
and the (i + 1)th lake, and w stands for the river width. fi,i+1 denotes the flow friction cost parameter between the two lakes, which is rimarily influenced by the topography and geomorphology of the lake basin and the friction coefficient of the riverbed. Due to the difficulty in accurately determining these parameters, initial approximations are provided during the simulation process based on varying lake basin geomorphologies,关注数学模型

<!-- b000317 | furniture | pages [11] -->
2

<!-- b000318 | furniture | pages [11] -->
MATHmodels

<!-- b000319 | furniture | pages [11] -->
获取更多资讯

<!-- b000320 | furniture | pages [12] -->
Team # 2417831

<!-- b000321 | furniture | pages [12] -->
Page 12 of 25

<!-- b000322 | prose | pages [12] -->
channel lengths, and depths as presented in Figure 8 and Table 4. Further refinements are carried out through iterative adjustments in the simulation process.

<!-- b000323 | prose | pages [12] -->
The Lake St. Clair:

<!-- b000324 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000325 | prose | pages [12] -->
According to Table 3, Lake St. Clair is notably smaller in area when compared to the Great Lakes. To streamline the model regulation process, we opt to treat it as a distinctive river entity rather than as a node within the lake chain.

<!-- b000326 | prose | pages [12] -->
Recognizing that lakes possess a significantly greater water storage capacity than rivers, implying a pronounced hysteresis effect on water, we introduced a hysteresis parameter τ, as shown in (11), between Lake Huron and Lake Erie which requires to be manually adjusted during the modeling process.

<!-- b000327 | prose | pages [12] -->
8

<!-- b000328 | prose | pages [12] -->
Qout(i) = N · ((hi · (t −τ) −hi+1) −fi,i+1 · di,i+1) · w

<!-- b000329 | prose | pages [12] -->
3.1.2 External Factors

<!-- b000330 | prose | pages [12] -->
(13) 3

<!-- b000331 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000332 | prose | pages [12] -->
External runoff inflow:

<!-- b000333 | prose | pages [12] -->
Lake Superior receives contributions from over two hundred streams. For the rest of the lakes, the primary sources of external runoff are the rivers upstream. We desig- nate the external runoff inflow to Lake Superior as the largest, while the external runoff inflow to the other lakes (excluding inter-chain inflows) is comparatively smaller.

<!-- b000334 | prose | pages [12] -->
Evaporation:

<!-- b000335 | prose | pages [12] -->
Evaporation from lakes is primarily influenced by factors such as lake area, tem- perature, wind, and air humidity. As noted by D. Lenters, B. Anderton, D. Blanken,et al., lakes exhibit seasonally significant variations in evaporation, reaching a maximum of 0.4 ft/day in the fall when evaporation is at its peak. Our estimation of the seasonal variation in evaporation for the Great Lakes is derived from the information presented in Table 3.

<!-- b000336 | prose | pages [12] -->
Precipitation:

<!-- b000337 | prose | pages [12] -->
Annual precipitation in the Great Lakes approximately varies between 750mm and 950 mm, with an increase from Lake Superior to Lake Ontario.

<!-- b000338 | prose | pages [12] -->
Upon analyzing the meteorological data of the Great Lakes region, we can refine the model by adjusting evaporation and precipitation settings based on seasonal vari- ations. This enhancement allows for a more accurate simulation of seasonal changes within the model. The inflow rate for the ith lake in the chain is expressed as:

<!-- b000339 | prose | pages [12] -->
Qin(i) = Qout(i −1) + Qrain(i) −Qev(i) (14)

<!-- b000340 | prose | pages [12] -->
Qrain,i is the precipitation of the ith lake, and Qev,i is the evaporation of the ith lake.

<!-- b000341 | prose | pages [12] -->
Ultimately, to identify the parameters in the model that require manual adjustment, we make these adjustments based on observed river flows within the lake chain. This careful calibration ensures that the model’s inflows and outflows between the lakes are closely aligned with actual values.

<!-- b000342 | prose | pages [12] -->
关注数学模型

<!-- b000343 | furniture | pages [12] -->
2

<!-- b000344 | furniture | pages [12] -->
MATHmodels

<!-- b000345 | furniture | pages [12] -->
获取更多资讯

<!-- b000346 | furniture | pages [13] -->
Team # 2417831

<!-- b000347 | prose | pages [13] -->
3.2

<!-- b000348 | heading | pages [13] -->
Control Algorithm Design

<!-- b000349 | furniture | pages [13] -->
Page 13 of 25

<!-- b000350 | heading | pages [13] -->
Classical Control Algorithms Synthesis

<!-- b000351 | prose | pages [13] -->
3.2.1

<!-- b000352 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000353 | prose | pages [13] -->
(1) PID controller is a classical feedback control algorithm aimed to achieve stable and accurate control. The output of the controller is the weighted sum of these three control terms:

<!-- b000354 | prose | pages [13] -->
u(t) = Kpe(t) + Ki

<!-- b000355 | prose | pages [13] -->
Z t

<!-- b000356 | prose | pages [13] -->
de(t)

<!-- b000357 | prose | pages [13] -->
e(τ)dτ + Kd

<!-- b000358 | prose | pages [13] -->
(15) dt

<!-- b000359 | prose | pages [13] -->
0 0

<!-- b000360 | prose | pages [13] -->
where Kp represents the proportional gain, and e(t) denotes the current error of the

<!-- b000361 | prose | pages [13] -->
R t

<!-- b000362 | prose | pages [13] -->
system. The integral gain is represented by Ki, and

<!-- b000363 | prose | pages [13] -->
0 e(τ)dτ represents the cumulative error over time. Kd stands for the differential gain, and de(t)

<!-- b000364 | prose | pages [13] -->
dt is the rate of change of the error. By adjusting the proportional, integral, and differential gains, precise control of the system can be achieved across various applications.

<!-- b000365 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000366 | prose | pages [13] -->
(2) Model predictive control (MPC) is an advanced method of process control based on a system model, optimizing the current control inputs by predicting the future be- havior of the system. Ts working principle involves:

<!-- b000367 | prose | pages [13] -->
▷Establishing a dynamic model of the system to predict its evolution over a future time horizon

<!-- b000368 | prose | pages [13] -->
▷Choosing the optimal control strategy at each time step by solving an optimiza- tion problem.

<!-- b000369 | prose | pages [13] -->
MPC excels in handling complex, nonlinear systems, and dynamic environments. Through real-time iterative updates, MPC can promptly adjust to changes in system states, achieving efficient control of the system.

<!-- b000370 | prose | pages [13] -->
3.2.2 Controller Design

<!-- b000371 | prose | pages [13] -->
In the context of the Great Lakes water flow control problem, the regulation of water volume within the Great Lakes is limited to interventions through the upstream compensation project and the Moses-Saunders Dam.

<!-- b000372 | prose | pages [13] -->
The application of PID solely for the upstream water flow control of the dams is suitable for straightforward scenarios. However, it is anticipated to encounter the fol- lowing issues in a complex circumstance:

<!-- b000373 | prose | pages [13] -->
▷Achieving water flow control across the entire lake chain is challenging when only having regulatory control over two dams. The number of systems that require control exceeds the available number of controllers, posing a complexity in managing the overall water flow dynamics.

<!-- b000374 | prose | pages [13] -->
▷Fixed coefficients in the controller, leading to limited adaptability to dynamic en- vironmental changes. The controller’s ability to adapt to a changing environment, including evaporation and rainfall, is relatively low.

<!-- b000375 | prose | pages [13] -->
▷The controller is highly sensitive to parameters. In a complex and dynamic en- vironment, even small changes in parameters can significantly impact the regulation effect. If the manually determined parameters are not optimal, the entire system may face an out-of-control situation over time.

<!-- b000376 | prose | pages [13] -->
关注数学模型

<!-- b000377 | furniture | pages [13] -->
2

<!-- b000378 | furniture | pages [13] -->
MATHmodels

<!-- b000379 | furniture | pages [13] -->
获取更多资讯

<!-- b000380 | furniture | pages [14] -->
Team # 2417831

<!-- b000381 | furniture | pages [14] -->
Page 14 of 25

<!-- b000382 | prose | pages [14] -->
Our proposed solution is graphed in Figure 9. The compensating work utilizes a mode-switchable P+PI control as the primary real-time feedback controller while the other one can switch between flood-releasing mode and PI control. Besides, a pre- diction module is used for optimizing the feedback control parameters. The structure

<!-- b000383 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000384 | prose | pages [14] -->
addresses the issues mentioned above.

<!-- b000385 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000386 | caption | pages [14] -->
Figure 9: Controller schema

<!-- b000387 | prose | pages [14] -->
Mode-switchable Feedback Control module 3.2.3

<!-- b000388 | prose | pages [14] -->
Typically, controllers for compensating engineered dams usually operate in the sim- ple P mode. It means they deploy proportional control based on the difference between the Lake Superior water level and the target level. As shown in Equation 15.

<!-- b000389 | prose | pages [14] -->
However, solely focusing on the lakes upstream of the dam does not guarantee effective regulation of Lake Huron, Lake Michigan, as well as Lake Erie.

<!-- b000390 | prose | pages [14] -->
Therefore, we modified the integral control of the controller which takes the cumu- lative error information of the water level in the lakes downstream into account. When the cumulative error of the water level of Lake Huron and Lake Michigan exceeds the control threshold I0, the controller switches from P mode to PI mode as Equation 16:

<!-- b000391 | prose | pages [14] -->
Q(t) = Kp1 · (htarget −h) · A

<!-- b000392 | prose | pages [14] -->


<!-- b000393 | prose | pages [14] -->
(16)

<!-- b000394 | prose | pages [14] -->


<!-- b000395 | prose | pages [14] -->
Z

<!-- b000396 | prose | pages [14] -->
Kp1 · (htarget −h) + Ki1 ·

<!-- b000397 | prose | pages [14] -->
Q(t) =

<!-- b000398 | prose | pages [14] -->
· A

<!-- b000399 | prose | pages [14] -->
te(τ)dτ

<!-- b000400 | prose | pages [14] -->
(17)

<!-- b000401 | prose | pages [14] -->
Here, Q(t) represents the current control variable, which is the discharge of the compensation project. K1 and K2 are the proportional and integral gains, respectively.

<!-- b000402 | prose | pages [14] -->
R

<!-- b000403 | prose | pages [14] -->
te(τ)dτ is the cumulative water level error of Lake Huron-Lake

<!-- b000404 | prose | pages [14] -->
A is the lake area, and

<!-- b000405 | prose | pages [14] -->
Michigan. The controller indicates that when the water level error of Lake Huron- Lake Michigan reaches a certain threshold, the controller will balance the water level downstream.

<!-- b000406 | prose | pages [14] -->
It is important to note that:

<!-- b000407 | prose | pages [14] -->
(1) The P+PI controller is made to better achieve the decoupling of water level con- trol between the two lakes. In comparison to using a P controller to alternately switch关注数学模型

<!-- b000408 | furniture | pages [14] -->
2

<!-- b000409 | furniture | pages [14] -->
MATHmodels

<!-- b000410 | furniture | pages [14] -->
获取更多资讯

<!-- b000411 | furniture | pages [15] -->
Team # 2417831

<!-- b000412 | furniture | pages [15] -->
Page 15 of 25

<!-- b000413 | prose | pages [15] -->
control between the two lakes or concentrating the PI controller solely on the upper lake, this method shows greater stability and comprehensiveness for controlling the entire lake chain.

<!-- b000414 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000415 | prose | pages [15] -->
(2) The differential controller has been omitted for the reason that in the practical regulation of reservoirs, the volume of water in the lakes is significantly larger than the maximum discharge capacity of the controlled dams. As a result, the control process is relatively slow. making the role of the differential controller minimized.

<!-- b000416 | prose | pages [15] -->
As for the Moses-Saunders Dam, a switchable PI+flood-releasing controller is em- ployed. The decision to not adopt the P+PI control mode as in the Compensating Work is based on the consideration that the mode is not well-suited for controlling upstream water flow.

<!-- b000417 | prose | pages [15] -->
The purpose of the switchable controller is to align with upstream hydrological conditions: when the water level of a lake upstreams on Lake Ontario exceeds the threshold value hcontrol, the flood-releasing mode is activated to maximize discharge while ensuring the stability of Lake Ontario’s water level. This is achieved by selecting

<!-- b000418 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000419 | prose | pages [15] -->
the minimum value between the maximum release from the dam and the estimated external inflow.

<!-- b000420 | prose | pages [15] -->
Qout = min {Qmax, (Qin + Qrain −Qev)} (18)

<!-- b000421 | prose | pages [15] -->
When upstream hydrological conditions are relatively stable, the Moses-Saunders Dam is primarily utilized to ensure the stability of Lake Ontario’s water level. In this scenario, PI mode is employed, with corresponding parameters for the proportional control Kp2 and Ki2.

<!-- b000422 | prose | pages [15] -->
3.2.4 Prediction Module

<!-- b000423 | prose | pages [15] -->
The primary goal of the prediction module is to dynamically adjust the parameters of the compensating project dam controller and the Moses-Sanders dam controller. The process involves:

<!-- b000424 | prose | pages [15] -->
(1) Predict the future change in the lake level in the lake chain for the next 200 hours with the current controller parameters.

<!-- b000425 | prose | pages [15] -->
(2) Optimize the parameters, by using gradient descent, based on an object function manually set.

<!-- b000426 | prose | pages [15] -->
Regarding the parameters of the two controllers, we express them using a vector formulation:

<!-- b000427 | prose | pages [15] -->
c = (Kp1, Ki1, I0, hcontrol, Kp2, Ki2) (19)

<!-- b000428 | prose | pages [15] -->
The error function is defined as: E(i, t, c) = (hi(t) −hi,target(t))2. Subsequently, the objective function J(c) is set to the sum of squares of the errors within this prediction time domain:

<!-- b000429 | prose | pages [15] -->
4 X

<!-- b000430 | prose | pages [15] -->
J(c) =

<!-- b000431 | prose | pages [15] -->
i=1

<!-- b000432 | prose | pages [15] -->
200 X

<!-- b000433 | prose | pages [15] -->
E(i, t, c) (20)

<!-- b000434 | prose | pages [15] -->
t=0

<!-- b000435 | prose | pages [15] -->
During the deployment phase, we discovered that the determination of the optimal关注数学模型

<!-- b000436 | furniture | pages [15] -->
2

<!-- b000437 | furniture | pages [15] -->
MATHmodels

<!-- b000438 | furniture | pages [15] -->
获取更多资讯

<!-- b000439 | furniture | pages [16] -->
Team # 2417831

<!-- b000440 | furniture | pages [16] -->
Page 16 of 25

<!-- b000441 | prose | pages [16] -->
controller parameters, denoted as copt, through the application of a gradient descent algorithm is time-consuming, also necessities to fine-tune a multitude of parameters. Given the complexity and the resource-intensive nature of this optimization process, a strategic decision was made to narrow the focus of our optimization efforts. Specifi-

<!-- b000442 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000443 | prose | pages [16] -->
cally, we opted to concentrate on Kp2 and KI2 as the key parameters for optimization.

<!-- b000444 | prose | pages [16] -->
3.3

<!-- b000445 | heading | pages [16] -->
Algorithm Verification

<!-- b000446 | prose | pages [16] -->
To initially assess the control performance of our controller, we established distinct target water levels for each lake in the chain. In the simulation, we observed the water level changes in the lakes along with the water outflow from each lake, as illustrated in

<!-- b000447 | caption | pages [16] -->
Figure 10. The dotted lines represent the target water levels set for each lake, featuring

<!-- b000448 | prose | pages [16] -->
a water level difference of 0.5 m-1 m from the current water level.

<!-- b000449 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000450 | caption | pages [16] -->
Figure 10: Effect of controller regulation under natural conditions

<!-- b000451 | prose | pages [16] -->
The Compensating Works:

<!-- b000452 | prose | pages [16] -->
As Lake Superior consistently maintained a water level above the target and down- stream Lake Huron and Lake Michigan remained below the target throughout the sim- ulation period, the Compensating Works consistently utilized a discharge close to the maximum flow.

<!-- b000453 | prose | pages [16] -->
The Moses-Saunders Dam:

<!-- b000454 | prose | pages [16] -->
As Lake Ontario exceeded the target level, Moses-Saunders Dam employed a strat- egy of larger discharges to stabilize Lake Ontario’s levels. Subsequently, as the Lake Ontario level approached the target, the dam reduced its discharge and adjusted it to align with the incoming flow. This approach facilitated Lake Ontario in reaching a more stable level.

<!-- b000455 | prose | pages [16] -->
关注数学模型

<!-- b000456 | furniture | pages [16] -->
2

<!-- b000457 | furniture | pages [16] -->
MATHmodels

<!-- b000458 | furniture | pages [16] -->
获取更多资讯

<!-- b000459 | furniture | pages [17] -->
Team # 2417831

<!-- b000460 | furniture | pages [17] -->
Page 17 of 25

<!-- b000461 | prose | pages [17] -->
4

<!-- b000462 | heading | pages [17] -->
Task 3: Sensitivity Analysis on Outflow of the Two

<!-- b000463 | prose | pages [17] -->
Dam Controllers

<!-- b000464 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000465 | prose | pages [17] -->
4.1

<!-- b000466 | heading | pages [17] -->
System Sensitivity on Control Output

<!-- b000467 | prose | pages [17] -->
The impacts of increasing the outflows from the two dams are illustrated below, where ’-L’ is denoted as a large flow rate and ’-S’ is a small flow rate. In Figure 11, the regulation pertains to the Soo Locks (upstream), while in Figure 12, it corresponds to the regulation of the Moses-Saunders Dam (downstream).

<!-- b000468 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000469 | caption | pages [17] -->
Figure 11: Effects of the Soo Locks flow rate on water levels

<!-- b000470 | caption | pages [17] -->
Figure 12: Effects of the Moses-Saunders Dam flow rate on water levels

<!-- b000471 | prose | pages [17] -->
Comparing the two figures reveals that Lake Ontario’s water level is predominantly influenced by the operation of the Moses-Saunders Dam, whereas the water levels of the four upstream lakes are more significantly impacted by the Soo Locks. This distinction is largely due to Niagara Falls, which introduces a dramatic elevation drop of approximately one hundred meters between Lake Erie and Lake Ontario, resulting in unidirectional flow between these lakes. The primary driving force for the water movement is this substantial topographic descent, rather than the usual differential in water levels. Consequently, normal variations in lake levels exert minimal effect on the关注数学模型

<!-- b000472 | furniture | pages [17] -->
2

<!-- b000473 | furniture | pages [17] -->
MATHmodels

<!-- b000474 | furniture | pages [17] -->
获取更多资讯

<!-- b000475 | furniture | pages [18] -->
Team # 2417831

<!-- b000476 | furniture | pages [18] -->
Page 18 of 25

<!-- b000477 | prose | pages [18] -->
flow between these two lakes. Additionally, the water level of the lake is particularly sensitive to adjustments in dam flow; a change of about 2000 cubic meters per second can cause a water level variation of around 0.2 meters in just 10 days, facilitating rapid response to emergency conditions.

<!-- b000478 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000479 | prose | pages [18] -->
A Comparison with Water Level in 2017 4.2

<!-- b000480 | prose | pages [18] -->
To better assess the efficacy of our water level control model, we compare the 2017 water level data with the upper and lower boundary water levels under optimal con- ditions.

<!-- b000481 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000482 | caption | pages [18] -->
Figure 13: Optimal water level V.S. water level in 2017

<!-- b000483 | prose | pages [18] -->
Visualized in Figure 13, it is evident that while the control algorithm may not en- sure the water level aligns perfectly with the optimal level, its performance remains excellent relative to the 2017 water conditions, particularly in terms of ’Protection’ and ’Hydro-power’.

<!-- b000484 | heading | pages [18] -->
Task 4: Sensitivity analysis to environmental changes

<!-- b000485 | prose | pages [18] -->
5

<!-- b000486 | prose | pages [18] -->
The control effect of the dams is assessed in the presence of dynamic changes in the environment. Among the environmental changes, heavy rainfall, and ice jams are the two largest impacts on the lake’s water level. In this section, the simulation system is run under both circumstances, the system without dams is used as a baseline to demonstrate the effectiveness and stability of our algorithms.

<!-- b000487 | heading | pages [18] -->
Algorithm Sensitivity to Heavy Precipitation

<!-- b000488 | prose | pages [18] -->
5.1

<!-- b000489 | prose | pages [18] -->
Firstly, we analyzed the simulation system after substantial precipitation occurred on Lake Huron and Lake Michigan without dam control as illustrated in Figure 14.

<!-- b000490 | prose | pages [18] -->
关注数学模型

<!-- b000491 | furniture | pages [18] -->
2

<!-- b000492 | furniture | pages [18] -->
MATHmodels

<!-- b000493 | furniture | pages [18] -->
获取更多资讯

<!-- b000494 | furniture | pages [19] -->
Team # 2417831

<!-- b000495 | furniture | pages [19] -->
Page 19 of 25

<!-- b000496 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000497 | caption | pages [19] -->
Figure 14: Control system’s response to heavy precipitation without dam

<!-- b000498 | prose | pages [19] -->
After heavy precipitation, the water level in Lake Huron and Lake Michigan rises rapidly, leading to a rapid increase in outflow due to the significant water level differ-

<!-- b000499 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000500 | prose | pages [19] -->
ence with downstream lakes.

<!-- b000501 | prose | pages [19] -->
10-200h: Lake levels in Lakes Huron and Lake Michigan decrease after precipita- tion ceases. The water level of Lake Superior begins to rise due to the increased down- stream level in Lake Huron, causing a reduction in flow between Lake Superior and Lake Huron. Lake St.Clair introduces a blocking effect between Lake Huron and Lake Erie, resulting in Lake Erie’s water level experiencing a gradual rise instead of drastic changes. Lake Ontario’s water level exhibits a downward trend during this period, primarily due to Lake Erie’s pronounced retardation effect. The outflow induces slow growth in water level, without a direct and conspicuous impact on Lake Ontario.

<!-- b000502 | prose | pages [19] -->
200-1500h: As the levels of Lake Huron and Lake Michigan decline, the upward trend in Lake Superior starts to decelerate and eventually stabilizes. Lake Erie’s lev- els begin to decrease with the reduction of the Lake Huron’s outflow. While Lake Ontario’s levels experience a significant lag and remain well above the target due to hysteresis.

<!-- b000503 | prose | pages [19] -->
Then we incorporate the dam controller into the model as shown in Figure 15.

<!-- b000504 | caption | pages [19] -->
Figure 15: Control system’s response to heavy precipitation with dam controller

<!-- b000505 | prose | pages [19] -->
10-200h: The cumulative error in downstream lake levels triggers the PI mode of the Compensating dams. The rising water levels in the three lakes also activate the flood-关注数学模型

<!-- b000506 | furniture | pages [19] -->
2

<!-- b000507 | furniture | pages [19] -->
MATHmodels

<!-- b000508 | furniture | pages [19] -->
获取更多资讯

<!-- b000509 | furniture | pages [20] -->
Team # 2417831

<!-- b000510 | furniture | pages [20] -->
Page 20 of 25

<!-- b000511 | prose | pages [20] -->
release mode of the downstream Moses-Saunders Dam. Lake Superior’s water level rises faster compared to the no-dam scenario. Accordingly, Lake Ontario returns to a safe water level faster. Lake Huron and Lake Michigan experience a more pronounced water level drop, with the dam-regulated condition showing a water level about 0.25m

<!-- b000512 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000513 | prose | pages [20] -->
lower than the no-dam condition at 200h.

<!-- b000514 | prose | pages [20] -->
200h-1500h: After the substantial drop in water levels in Lakes Huron and Lake Michigan, Lake Superior resumes some drainage to prevent further increases in water levels. Lake Ontario is very close to the optimal level during this period.

<!-- b000515 | heading | pages [20] -->
Algorithm Sensitivity to Ice Jam

<!-- b000516 | prose | pages [20] -->
5.2

<!-- b000517 | prose | pages [20] -->
The controller’s regulation during ice jams in Lake Michigan and Lake Huron with- out a dam is shown in Figure 16.

<!-- b000518 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000519 | caption | pages [20] -->
Figure 16: Control system’s response to ice jams without dam controller

<!-- b000520 | prose | pages [20] -->
0-500h: The outflow from Lake Huron and Lake Michigan is minimal, causing a rise in water levels. This leads to a decrease in inflow between Lakes Superior and Lake Huron, resulting in an increase in Lake Superior’s water level. Lake Erie experiences a decrease in water level and outflow due to lower inflow.

<!-- b000521 | prose | pages [20] -->
500h-1500h: Lower water levels in downstream lakes enable an increase in flow between Lake Huron and Lake Erie. The ice jam eases, allowing the outflow from Lake Huron to gradually recover, and the upward trend in water levels slows down.

<!-- b000522 | prose | pages [20] -->
The result control system’s response to ice jam changes is shown in Figure 17.

<!-- b000523 | prose | pages [20] -->
0-500h: The outflow from Lake Huron and Lake Michigan is minimal, causing a rise in water levels. This leads to a decrease in inflow between Lakes Superior and Lake Huron, resulting in an increase in Lake Superior’s water level. Lake Erie experiences a decrease in water level and outflow due to lower inflow.

<!-- b000524 | prose | pages [20] -->
500h-1500h: Lower water levels in downstream lakes enable an increase in flow between Lake Huron and Lake Erie. The ice jam eases, allowing the outflow from Lake Huron to gradually recover, and the upward trend in water levels slows down.

<!-- b000525 | prose | pages [20] -->
This section verifies the robustness of our control algorithms toward environmental changes. However, the results also indicate that the dams’ control abilities are limited in the face of rapid changes.

<!-- b000526 | prose | pages [20] -->
关注数学模型

<!-- b000527 | furniture | pages [20] -->
2

<!-- b000528 | furniture | pages [20] -->
MATHmodels

<!-- b000529 | furniture | pages [20] -->
获取更多资讯

<!-- b000530 | furniture | pages [21] -->
Team # 2417831

<!-- b000531 | furniture | pages [21] -->
Page 21 of 25

<!-- b000532 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000533 | caption | pages [21] -->
Figure 17: Control system’s response to ice jams with dam controller

<!-- b000534 | prose | pages [21] -->
6 Task 5: Focusing on Lake Ontario

<!-- b000535 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000536 | prose | pages [21] -->
6.1 Social and Physical Geographical Analysis

<!-- b000537 | prose | pages [21] -->
The St. Lawrence River, situated downstream from Lake Ontario, converges with the Ottawa River in Montreal. The combined runoff from these two rivers, along with the water level of Lake Ontario, exerts a substantial impact on the safety of coastal cities and the well-being of relevant stakeholders.

<!-- b000538 | caption | pages [21] -->
Figure 18: Focusing on the local area of Lake Ontario and Ottawa River

<!-- b000539 | prose | pages [21] -->
The regulation of the Ottawa River’s runoff is intricately tied to the management of numerous upstream reservoirs. Meanwhile, control over Lake Ontario’s water level predominantly hinges on the operations of the Moses-Saunders Dam. When imple- menting these regulations, it is imperative to consider a myriad of social and physical geographical factors:

<!-- b000540 | prose | pages [21] -->
(1) Economic Activities: Balancing the needs of economic endeavors like shipping, hydro-power plants, and leisure activities.

<!-- b000541 | prose | pages [21] -->
(2) flood protection: Prioritizing the flood protection requirements of communities and residents, especially ensuring the safety of downstream areas such as Montreal.

<!-- b000542 | prose | pages [21] -->
(3) Upstream and Downstream Dynamics: Taking into account the conditions of upstream and downstream water levels and flows, notably those of the Ottawa River关注数学模型

<!-- b000543 | furniture | pages [21] -->
2

<!-- b000544 | furniture | pages [21] -->
MATHmodels

<!-- b000545 | furniture | pages [21] -->
获取更多资讯

<!-- b000546 | furniture | pages [22] -->
Team # 2417831

<!-- b000547 | prose | pages [22] -->
and the four Great Lakes upstream.

<!-- b000548 | furniture | pages [22] -->
Page 22 of 25

<!-- b000549 | prose | pages [22] -->
(4) Climate Change Impact: Preparing for extreme weather events induced by cli- mate change, and acknowledging their potential influence on the regulation process.

<!-- b000550 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000551 | prose | pages [22] -->
(5) Seasonal Changes: Adapting to seasonal changes, including heightened flows due to spring snowmelt. Considering the broader impacts of climate change on pre- cipitation, evaporation, and overall water dynamics.

<!-- b000552 | prose | pages [22] -->
(6) Environmental Considerations: Addressing environmental and ecosystem re- quirements, ensuring the maintenance of water quality, and promoting biodiversity in regulated areas.

<!-- b000553 | prose | pages [22] -->
Assigning appropriate weights to the factors based on seasonal characteristics and real-time hydrological conditions is essential for effective dam regulation using the established algorithm. The primary challenges in this endeavor include:

<!-- b000554 | prose | pages [22] -->
(1) The historical data reveals a significant correlation between elevated water lev- els in Lake Ontario and increased snowmelt in the Ottawa and upstream regions from

<!-- b000555 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000556 | prose | pages [22] -->
April to August. During this period, augmenting flood releases from the Moses Saun- ders Dam to align with the heightened runoff from the Ottawa River poses a risk of flooding in Montreal. Therefore, there is a crucial necessity to collaboratively regulate the runoff from both rivers, ensuring the safety not only of Montreal but also of the shoreline of Lake Ontario.

<!-- b000557 | prose | pages [22] -->
(2) Establishment of a sensible stakeholder weighting is essential (and it should vary seasonally). For instance, during the spring and summer months, a higher weight- ing is necessary to prioritize and emphasize resident safety.

<!-- b000558 | prose | pages [22] -->
6.2 Reanalysis of Stakeholders

<!-- b000559 | caption | pages [22] -->
Figure 19: Stakeholders reanalysis radar chart

<!-- b000560 | prose | pages [22] -->
In the previous section, we developed optimal water level control in the Great Lakes When focusing on the local area of Lake Ontario-Ottawa River-Montreal, system. we can fine-tune the weights of individual benefit functions for different seasons or 关注数学模型 months by conducting a more detailed examination, as Equation 8.

<!-- b000561 | furniture | pages [22] -->
2

<!-- b000562 | furniture | pages [22] -->
MATHmodels

<!-- b000563 | furniture | pages [22] -->
获取更多资讯

<!-- b000564 | furniture | pages [23] -->
Team # 2417831

<!-- b000565 | furniture | pages [23] -->
Page 23 of 25

<!-- b000566 | prose | pages [23] -->
(1) Residents’ Safety: During the early spring snowmelt and increased summer rainfall, the potential for elevated water levels in Lake Ontario and the Ottawa River rises. Hence, it is imperative to amplify the weighting factor during this period to ensure the safety of residents and protect coastal properties.

<!-- b000567 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000568 | prose | pages [23] -->
(2) Shipping Efficiency: Winter brings varying degrees of ice cover to different waterways, adversely affecting shipping efficiency. Consequently, during this period, it becomes essential to decrease the weight assigned to shipping considerations.

<!-- b000569 | prose | pages [23] -->
(3) Hydro-power Plant: The majority of power stations currently in construction are resilient to icing, minimizing the impact. However, during periods of substantial water flow, a slight increase in weight may be warranted.

<!-- b000570 | prose | pages [23] -->
(4) Leisure: Water recreation options are available in every season, emphasizing the need for a balanced consideration across the year.

<!-- b000571 | prose | pages [23] -->
(5) Ecological Effects: The ecological effects are contingent on local climatic condi- tions at any given time, with potential variations during abnormal climates. Weighting may be adjusted accordingly, placing a greater emphasis on ecological impacts during

<!-- b000572 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000573 | prose | pages [23] -->
unusual climatic conditions.

<!-- b000574 | heading | pages [23] -->
Model Evaluation and Further Discussion

<!-- b000575 | prose | pages [23] -->
7

<!-- b000576 | prose | pages [23] -->
7.1

<!-- b000577 | heading | pages [23] -->
Model Strengths

<!-- b000578 | prose | pages [23] -->
• The model selects the environmental factors comprehensively and scientifically.

<!-- b000579 | prose | pages [23] -->
It truly simulates the hydrological environment of the Great Lakes including in- ternal flow within the lakes-chain and external factors. It assures the reliability of our research. • Our model is relatively robust with respect to its configuration parameters, i.e., demonstrates stability after changing river channel parameters, evaporation rate, etc. • The control algorithm combines a prediction module with feedback control, which performs well under dynamic changes.

<!-- b000580 | heading | pages [23] -->
Model Weaknesses and Further Discussion

<!-- b000581 | prose | pages [23] -->
7.2

<!-- b000582 | prose | pages [23] -->
• Stakeholders are not considered comprehensively enough, and the determination of relative weights can also be based on more professional opinions. • The dam control algorithm can generally consider the hydrological conditions across the entire basin, facilitating a more coordinated regulation with the up- stream reservoirs of the Ottawa River.

<!-- b000583 | prose | pages [23] -->
关注数学模型

<!-- b000584 | furniture | pages [23] -->
2

<!-- b000585 | furniture | pages [23] -->
MATHmodels

<!-- b000586 | furniture | pages [23] -->
获取更多资讯

<!-- b000587 | furniture | pages [24] -->
Team # 2417831

<!-- b000588 | prose | pages [24] -->
A Memo to IJC Leadership

<!-- b000589 | prose | pages [24] -->
To whom it may concern,

<!-- b000590 | furniture | pages [24] -->
Page 24 of 25

<!-- b000591 | prose | pages [24] -->
微信公众号：数学模型

<!-- b000592 | prose | pages [24] -->
We are writing to present an overview of our model, emphasizing our utilization of historical data to refine the model’s parameters and overall effectiveness. This model is crafted to simulate the fluctuations in the Great Lakes water levels, incorporating the hydrodynamic relations within the lake chain and the impact of external variables.

<!-- b000593 | prose | pages [24] -->
To fortify the model’s reliability and precision, we have harnessed an extensive collection of historical data. This includes hydrologic information, such as historical records of water level variations and the data of river flow. We also examined the temporal relationship between the water level fluctuations in lakes and rivers to fine- tune the model’s representation of the hysteresis effect of lakes on rivers.

<!-- b000594 | prose | pages [24] -->
Additionally, we utilized meteorological data, including precipitation and evapo- ration across the Great Lakes, to accurately model external influences such as evapo-

<!-- b000595 | prose | pages [24] -->
微信号：MATHmodels

<!-- b000596 | prose | pages [24] -->
ration and rainfall. Detailed topographic data of the lake basin were integrated to en- hance the hydrodynamic equations within the model. We also considered the depth, width, and length of connecting river channels to refine our understanding of lake inflow and outflow capacities and the associated flow friction losses. Moreover, the seasonal melting snow contributions to the lakes were considered, capturing the sea- sonal runoff variations effectively.

<!-- b000597 | prose | pages [24] -->
Our model features a determination of the optimal water level on a monthly basis, balancing considerations such as resident safety, hydro-power revenue, navigation, ecological impacts, and overall resident satisfaction. This serves as a guideline for our control mechanisms. The model boasts sophisticated equations for internal flows, considering the lake basin’s topography, the frictional flow costs, lake sizes, and the hysteresis effect of the lake basin’s geomorphology. External influences such as runoff, evaporation, and precipitation have been meticulously modeled, with optimizations drawn from historical data insights.

<!-- b000598 | prose | pages [24] -->
For control strategies, a prediction module is used to forecast water level within the observed time domain, continuously updating model parameters through optimiza- tion. This bolsters the controller model’s robustness. Our control strategy includes adaptive controller modes for dams, which is designed to respond to environmental fluctuations and extreme conditions efficiently. It ensures safety across the lake system.

<!-- b000599 | prose | pages [24] -->
In conclusion, our lake system model integrates historical data comprehensively, offering a precise depiction of the dynamic interplay in the lake chain. We are confi- dent that our methodology will provide valuable perspectives for the IJC, fostering the ongoing enhancement of lake system management.

<!-- b000600 | prose | pages [24] -->
We anticipate the opportunity to delve deeper into our model with you and address any inquiries or concerns you might have.

<!-- b000601 | prose | pages [24] -->
Yours Sincerely,

<!-- b000602 | furniture | pages [24] -->
Team #2417831

<!-- b000603 | prose | pages [24] -->
关注数学模型

<!-- b000604 | furniture | pages [24] -->
2

<!-- b000605 | furniture | pages [24] -->
MATHmodels

<!-- b000606 | furniture | pages [24] -->
获取更多资讯

<!-- b000607 | furniture | pages [25] -->
Team # 2417831

<!-- b000608 | furniture | pages [25] -->
Page 25 of 25

<!-- b000609 | heading | pages [25] -->
References

<!-- b000610 | references | pages [25] -->
[1] https://en.wikipedia.org/wiki/Lake_Superior

<!-- b000611 | references | pages [25] -->
微信公众号：数学模型

<!-- b000612 | references | pages [25] -->
[2] https://glisaclimate.org/media/GLISA_Lake_Evaporation.pdf

<!-- b000613 | references | pages [25] -->
[3] https://www.fs.usda.gov/ccrc/topics/regional-example-western-great-lakes

<!-- b000614 | references | pages [25] -->
[4] https://en.wikipedia.org/wiki/Moses-Saunders_Power_Dam

<!-- b000615 | references | pages [25] -->
[5] https://en.wikipedia.org/wiki/Robert_Moses_Niagara_Power_Plant

<!-- b000616 | references | pages [25] -->
[6] https://en.wikipedia.org/wiki/Moses-Saunders_Power_Dam

<!-- b000617 | references | pages [25] -->
[7] https://en.wikipedia.org/wiki/Saint_Marys_Falls_Hydropower_Plant

<!-- b000618 | references | pages [25] -->
[8] https://greatlakes-seaway.com/en/the-seaway/facts-figures/tonnage/

<!-- b000619 | references | pages [25] -->
微信号：MATHmodels

<!-- b000620 | references | pages [25] -->
[9] Lake Ontario-St.Lawrence River Plan 2014, https://ijc.org/sites/default/files/IJC_

<!-- b000621 | references | pages [25] -->
LOSR_EN_Web.pdf

<!-- b000622 | references | pages [25] -->
[10] Myers, D. T., Ficklin, D. L., and Robeson, S. M.: Hydrologic implications of pro-

<!-- b000623 | references | pages [25] -->
jected changes in rain-on-snow melt for Great Lakes Basin watersheds, Hydrol.

<!-- b000624 | references | pages [25] -->
Earth Syst. Sci., 27, 1755–1770, https://doi.org/10.5194/hess-27-1755-2023, 2023.

<!-- b000625 | references | pages [25] -->
关注数学模型

<!-- b000626 | furniture | pages [25] -->
2

<!-- b000627 | furniture | pages [25] -->
MATHmodels

<!-- b000628 | furniture | pages [25] -->
获取更多资讯
