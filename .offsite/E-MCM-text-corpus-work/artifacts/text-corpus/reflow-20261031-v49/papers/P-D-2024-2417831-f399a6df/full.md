# P-D-2024-2417831-f399a6df

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型 微信号：MATHmodels 获取更多资讯 2 MATHmodels 关注数学模型

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen D 2024 MCM/ICM Summary Sheet Team Control Number 2417831

<!-- b000003 | title | pages [1] -->
Harmony of the Great Lakes: A Water Level Balance Approach

<!-- b000004 | heading | pages [1] -->
Summary

<!-- b000005 | prose | pages [1] -->
The Great Lakes represent 20% of the world’s freshwater resources, making their management, especially in water level, critically important. Fluctuations in their water levels are influenced by a myriad of natural factors and involve a diverse group of stakeholders. Consequently, developing a management plan and controlling the water levels of these lakes present a challenge.

<!-- b000006 | prose | pages [1] -->
For Task1: A genetic algorithm model is established considering coastal protection costs, hydro-power generation, leisure satisfaction, shipping benefits, and ecological impacts. By utilizing benefit functions and the Analytic Hierarchy Process (AHP), this model efficiently assesses the interests of stakeholders. Besides, the model particular focuses on coastal protection costs and hydroelectric power generation. It ultimately establishes the optimal water level for the Great Lakes on a monthly basis.

<!-- b000007 | prose | pages [1] -->
For Task2: We develop a hydrodynamic model tailored to the Great Lakes, accounting for both the flow dynamics within the lake chain and external variables affecting it. Following this, we craft distinct water level control algorithms for the Compensating Works and the Moses-Saunders Dam. These algorithms integrate a mode-switchable feedback controller with a prediction module, enhancing the controller’s responsiveness by optimizing feedback gains for superior performance amidst environmental fluctuations. Simulations conducted using our model confirm the efficacy of these algorithms.

<!-- b000008 | prose | pages [1] -->
For Task 3: By increasing the outflow at the Soo Locks (upstream) and the Moses-Saunders Dam (downstream), we evaluated their sensitivity to water level management. Our analysis reveals that the upstream dam predominantly affects Lake Superior, Lake Michigan, Lake Huron, and Lake Erie, whereas the downstream dam has a more significant impact on the remaining lakes. When compared to water levels in 2017, our model demonstrates improved performance in numerous aspects.

<!-- b000009 | prose | pages [1] -->
For Task 4: We introduce dynamic scenarios into the simulation, including heavy precipitation and ice jams, to assess the sensitivity and resilience of our model against environmental changes. The results show that our algorithms are more effective in preventing significant increases in water levels following heavy rainfall events than natural regulatory methods. Furthermore, when ice jam occurs, the time needed to recover water levels decreases through enhanced upstream discharge.

<!-- b000010 | prose | pages [1] -->
For Task 5: Focusing on the key factors and stakeholders affecting Lake Ontario, we identified the water flow from the Ottawa River and the protection of coastal residents in Montreal as significant influences.The analysis emphasizes that to reach an effective regulation requires seasonal adjustments and collaborative efforts to protect coastal communities and maintain ecological balance.

<!-- b000011 | prose | pages [1] -->
In conclusion, our model has the strength of robustness and comprehensiveness. This provides scientific guidance and support for the regulation of the Great Lakes in the future.

<!-- b000012 | keywords | pages [1] -->
Keywords: Prediction-based feedback control, Lake chain simulation, Multi-objective optimization, Genetic algorithm

<!-- b000013 | furniture | pages [2] -->
Team # 2417831

<!-- b000014 | furniture | pages [2] -->
Page 2 of 25

<!-- b000015 | heading | pages [2] -->
Contents

<!-- b000016 | contents | pages [2] -->
1 Introduction

<!-- b000017 | contents | pages [2] -->
3

<!-- b000018 | contents | pages [2] -->
1.1

<!-- b000019 | contents | pages [2] -->
Background

<!-- b000020 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000023 | contents | pages [2] -->
1.2

<!-- b000024 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
3

<!-- b000026 | contents | pages [2] -->
1.3

<!-- b000027 | contents | pages [2] -->
Assumptions and Justifications . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
3

<!-- b000029 | contents | pages [2] -->
1.4

<!-- b000030 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
1.5

<!-- b000033 | contents | pages [2] -->
Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
4

<!-- b000035 | contents | pages [2] -->
2 Task 1: Determination of the Optimal Water Level

<!-- b000036 | contents | pages [2] -->
5

<!-- b000037 | contents | pages [2] -->
2.1

<!-- b000038 | contents | pages [2] -->
Introducing Genetic Algorithm . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
2.2

<!-- b000041 | contents | pages [2] -->
Determination of the Benefit Function . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
5

<!-- b000043 | contents | pages [2] -->
2.3

<!-- b000044 | contents | pages [2] -->
Analysis of Weights . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
7

<!-- b000046 | contents | pages [2] -->
2.4

<!-- b000047 | contents | pages [2] -->
Presentation of Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
8

<!-- b000049 | contents | pages [2] -->
3 Task2: Establishment of Algorithms for Water Level Control

<!-- b000050 | contents | pages [2] -->
9

<!-- b000051 | contents | pages [2] -->
3.1

<!-- b000052 | contents | pages [2] -->
Hydrodynamic Model of the Lake Chain

<!-- b000053 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
9

<!-- b000055 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000056 | contents | pages [2] -->
3.1.1

<!-- b000057 | contents | pages [2] -->
Internal Water Flow

<!-- b000058 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
10

<!-- b000060 | contents | pages [2] -->
3.1.2

<!-- b000061 | contents | pages [2] -->
External Factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
12

<!-- b000063 | contents | pages [2] -->
3.2

<!-- b000064 | contents | pages [2] -->
Control Algorithm Design . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
13

<!-- b000066 | contents | pages [2] -->
3.2.1

<!-- b000067 | contents | pages [2] -->
Classical Control Algorithms Synthesis . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
13

<!-- b000069 | contents | pages [2] -->
3.2.2

<!-- b000070 | contents | pages [2] -->
Controller Design . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
13

<!-- b000072 | contents | pages [2] -->
3.2.3

<!-- b000073 | contents | pages [2] -->
Mode-switchable Feedback Control module

<!-- b000074 | contents | pages [2] -->
. . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
14

<!-- b000076 | contents | pages [2] -->
3.2.4

<!-- b000077 | contents | pages [2] -->
Prediction Module . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
15

<!-- b000079 | contents | pages [2] -->
3.3

<!-- b000080 | contents | pages [2] -->
Algorithm Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
16

<!-- b000082 | contents | pages [2] -->
4 Task 3: Sensitivity Analysis on Outflow of the Two Dam Controllers

<!-- b000083 | contents | pages [2] -->
17

<!-- b000084 | contents | pages [2] -->
4.1

<!-- b000085 | contents | pages [2] -->
System Sensitivity on Control Output

<!-- b000086 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
17

<!-- b000088 | contents | pages [2] -->
4.2

<!-- b000089 | contents | pages [2] -->
A Comparison with Water Level in 2017 . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
18

<!-- b000091 | contents | pages [2] -->
5 Task 4: Sensitivity analysis to environmental changes

<!-- b000092 | contents | pages [2] -->
18

<!-- b000093 | contents | pages [2] -->
5.1

<!-- b000094 | contents | pages [2] -->
Algorithm Sensitivity to Heavy Precipitation . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [2] -->
18

<!-- b000096 | contents | pages [2] -->
5.2

<!-- b000097 | contents | pages [2] -->
Algorithm Sensitivity to Ice Jam . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000098 | contents | pages [2] -->
20

<!-- b000099 | contents | pages [2] -->
6 Task 5: Focusing on Lake Ontario

<!-- b000100 | contents | pages [2] -->
21

<!-- b000101 | contents | pages [2] -->
6.1

<!-- b000102 | contents | pages [2] -->
Social and Physical Geographical Analysis

<!-- b000103 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000104 | contents | pages [2] -->
21

<!-- b000105 | contents | pages [2] -->
6.2

<!-- b000106 | contents | pages [2] -->
Reanalysis of Stakeholders

<!-- b000107 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
22

<!-- b000109 | contents | pages [2] -->
7 Model Evaluation and Further Discussion

<!-- b000110 | contents | pages [2] -->
23

<!-- b000111 | contents | pages [2] -->
7.1

<!-- b000112 | contents | pages [2] -->
Model Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000113 | contents | pages [2] -->
23

<!-- b000114 | contents | pages [2] -->
7.2

<!-- b000115 | contents | pages [2] -->
Model Weaknesses and Further Discussion . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [2] -->
23

<!-- b000117 | contents | pages [2] -->
A Memo to IJC Leadership

<!-- b000118 | contents | pages [2] -->
24

<!-- b000119 | contents | pages [2] -->
References

<!-- b000120 | contents | pages [2] -->
25

<!-- b000121 | contents | pages [2] -->
关注数学模型

<!-- b000122 | furniture | pages [2] -->
2

<!-- b000123 | furniture | pages [2] -->
MATHmodels

<!-- b000124 | furniture | pages [2] -->
获取更多资讯

<!-- b000125 | furniture | pages [3] -->
Team # 2417831

<!-- b000126 | furniture | pages [3] -->
Page 3 of 25

<!-- b000127 | heading | pages [3] -->
1 Introduction

<!-- b000128 | heading | pages [3] -->
1.1 Background

<!-- b000129 | prose | pages [3] -->
微信公众号：数学模型 The Great Lakes, spanning the United States and Canada, constitute the world’s largest freshwater lake group. Vital for fishing, recreation, power generation, and more, these interconnected lakes pose complex challenges in water management. Bal- ancing the needs of diverse stakeholders, including urban areas, is crucial. Factors like temperature, wind, precipitation, and human-controlled mechanisms impact wa- ter levels. The central role in this balance is played by two primary control mecha- nisms: the Soo Locks and Moses-Saunders Dam.

<!-- b000130 | prose | pages [3] -->
Despite human control over certain elements, natural occurrences such as rain, evaporation, and ice jams remain beyond manipulation. Local policies and environ- mental changes can yield unexpected effects, impacting the ecosystem and residents. Even slight deviations from normal water levels significantly affect stakeholders. This 微信号：MATHmodels "wicked" dynamic network flow problem embodies exceptional complexity, marked by interdependencies, intricate requirements, and inherent uncertainties. Effective man- agement is essential to sustain the ecological health of the region and the well-being of its inhabitants.

<!-- b000131 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000132 | prose | pages [3] -->
In light of the background information and constraints highlighted in the problem statement, we need to tackle the following tasks:

<!-- b000133 | prose | pages [3] -->
1. Balance the interests of all parties in determining the optimal level of the Great Lakes for each month of the year.

<!-- b000134 | prose | pages [3] -->
2. Create algorithms to maintain optimal water levels in five lakes according to in- flow and outflow data of the lakes.

<!-- b000135 | prose | pages [3] -->
3. Analyze the sensitivity of the control algorithms to the two control dams using data from 2017 and test whether the control algorithm satisfies or outperforms the actual water level for each stakeholder.

<!-- b000136 | prose | pages [3] -->
4. Examine the sensitivity of control algorithms to environmental changes.

<!-- b000137 | prose | pages [3] -->
5. Focus the analysis on Lake Ontario and analyze the stakeholders and factors af- fecting the lake.

<!-- b000138 | heading | pages [3] -->
1.3 Assumptions and Justifications

<!-- b000139 | prose | pages [3] -->
To streamline the problem and facilitate the simulation of real-life conditions, we have made several fundamental assumptions. These assumptions have been carefully justi- fied.

<!-- b000140 | prose | pages [3] -->
• Assumption: The water flow between Lake Michigan and Lake Huron does not influence our model

<!-- b000141 | prose | pages [3, 4] -->
• Justification: According to the data given in the Addendum, the water level of Lake Michigan and that of Lake Huron are the same. 关注数学模型 • Assumption: Consider the average water level of historical data as the initial value for the optimal water level, then iterate to seek an improved solution.

<!-- b000142 | furniture | pages [3] -->
2

<!-- b000143 | furniture | pages [3] -->
MATHmodels

<!-- b000144 | furniture | pages [3] -->
获取更多资讯

<!-- b000145 | furniture | pages [4] -->
Team # 2417831

<!-- b000146 | furniture | pages [4] -->
Page 4 of 25

<!-- b000148 | prose | pages [4] -->
• Justification: Manually controlled water level variations are much lower than normal lake depths or natural lake levels, so the optimum level must be near the 微信公众号：数学模型 average level given by historical data.

<!-- b000149 | heading | pages [4] -->
1.4 Our Work

<!-- b000150 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000151 | caption | pages [4] -->
Figure 1: Our Work

<!-- b000152 | heading | pages [4] -->
1.5 Notation

<!-- b000153 | caption | pages [4] -->
Table 1: Notation

<!-- b000154 | prose | pages [4] -->
Glossary Meaning Unit

<!-- b000155 | prose | pages [4] -->
S Benefit Function / hi m The Water Level of Lakes hi0 m The Historical Average Water Level of Lakes B1 Global Temperature / B2 Environmental Pollution Degree / B3 The Balance of the Ecosystem / km2 A Area of the lake Outflow of the ith Lake m3/s Qout(i) Inflow of the ith Lake m3/s Qin(i)

<!-- b000156 | prose | pages [4] -->
Note: Some variables are not listed in Table 1 and will be discussed in detail in each section.

<!-- b000157 | prose | pages [4] -->
关注数学模型

<!-- b000158 | furniture | pages [4] -->
2

<!-- b000159 | furniture | pages [4] -->
MATHmodels

<!-- b000160 | furniture | pages [4] -->
获取更多资讯

<!-- b000161 | furniture | pages [5] -->
Team # 2417831

<!-- b000162 | furniture | pages [5] -->
Page 5 of 25

<!-- b000163 | heading | pages [5] -->
2 Task 1: Determination of the Optimal Water Level

<!-- b000164 | heading | pages [5] -->
2.1 Introducing Genetic Algorithm

<!-- b000165 | prose | pages [5] -->
微信公众号：数学模型 A genetic algorithm is an optimization algorithm that mimics the natural selection and hereditary mechanism and is mainly used to solve optimization problems. It sim- ulates the process of inheritance, crossover, and mutation in the process of biological evolution, and gradually searches for the globally optimal solution by continuously evolving excellent individuals.

<!-- b000166 | heading | pages [5] -->
2.2 Determination of the Benefit Function

<!-- b000167 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000168 | caption | pages [5] -->
Figure 2: Stakeholders of the Great Lakes

<!-- b000169 | prose | pages [5] -->
The Great Lakes involve a diverse range of stakeholders, including property own- ers, hydro-power generation companies, recreational boaters, shipping companies, and fishers, as shown in Figure 2.

<!-- b000170 | prose | pages [5] -->
(1) Cost of Protecting Coastal Residents

<!-- b000171 | prose | pages [5] -->
As outlined in Plan 2014, the risks associated with increasing lake and river lev- els for residents encompass flooding of lakeside or waterfront residences, along with road damage, necessitating the elevation and fortification of shorelines. The cost is di- rectly proportional to the water level, with higher water levels incurring higher costs. Conversely, lower water levels allow the original protection measures to suffice. This situation can be aptly described using a step function

<!-- b000172 | prose | pages [5] -->
( 0 x < 0 y = ϵ(x) = (1) x ≥0 1

<!-- b000173 | prose | pages [5] -->
As the level ascends, it can be postulated that the associated costs are directly pro- portional to the fluctuations in water level, the extent of the lake shoreline, and the density of the neighboring population. It is evident that in sparsely populated re- gions, the apprehension regarding the perils of rising water levels on residential prop- erties diminishes.

<!-- b000174 | prose | pages [5, 6] -->
关注数学模型 Therefore, we can conclude the cost function of protecting coastal residents:

<!-- b000175 | furniture | pages [5] -->
2

<!-- b000176 | furniture | pages [5] -->
MATHmodels

<!-- b000177 | furniture | pages [5] -->
获取更多资讯

<!-- b000178 | furniture | pages [6] -->
Team # 2417831

<!-- b000179 | furniture | pages [6] -->
Page 6 of 25

<!-- b000181 | prose | pages [6] -->
5 hi −hi0 X · ϵ(hi −hi0) · Li · Di S = (2) hi0 微信公众号：数学模型 i=1

<!-- b000182 | prose | pages [6] -->
where the subscript i is indicative of each specific lake. Furthermore, Li is the coeffi- cient about the length of the lake shoreline, and Di signifies the coefficient associated with residential density. Evidently, when under manual control, a more favorable out- come is achieved with a smaller value for S.

<!-- b000183 | prose | pages [6] -->
(2) Revenue of Hydro-power Plant

<!-- b000184 | prose | pages [6] -->
Undoubtedly, the power generation of a hydro-power plant exhibits a positive cor- relation with the height of the waterfall. To elaborate further, this relationship can capacity ∝kinetic energy ∝ be mathematically expressed as power generation difference ∝altitude potential energy difference. Thus, the benefits derived from alterations in water level are as follows:

<!-- b000185 | prose | pages [6] -->
微信号：MATHmodels 3 Qi × hi·up −hi·down X S = (3) hi0·up −hi0·down i=1

<!-- b000186 | prose | pages [6] -->
where the subscripts i denote the three major hydro-power plants. Qi represents the power generation of each respective hydro-power plant.

<!-- b000187 | prose | pages [6] -->
(3) Leisure Satisfaction

<!-- b000188 | prose | pages [6] -->
Recreational boaters have expressed a preference for consistent periodic water flows, dictated by the conditions of both upstream and downstream lakes. They observed that increased variability in water levels throughout the twelve months leads to less stability in the flow, while minimal fluctuations result in a more stable flow. Con- sequently, higher levels of recreational satisfaction are associated with a more stable flow.

<!-- b000189 | prose | pages [6] -->
The assessment of the magnitude of water level changes throughout the year is conducted through the calculation of the standard deviation for each lake. It can be visualized by the equation:

<!-- b000190 | prose | pages [6] -->
sP12   5 j=1(hi −µ)2 X ki · S = (4)  12 i=1

<!-- b000191 | prose | pages [6] -->
where µ is the average water level throughout the year. ki is the proportionality coeffi- cient of the function.

<!-- b000192 | prose | pages [6] -->
(4) Shipping Revenue

<!-- b000193 | prose | pages [6] -->
As lake depths typically exceed ship drafts significantly, fluctuations in lake levels have a limited impact on shipping operations. Shipping concerns are predominantly centered around river levels. When river levels drop too low, it can impede the proper passage of ships. The water level in the river is directly proportional to the river’s flow, and this flow is intricately connected to the levels of lakes both upstream and down- stream. Therefore, the primary metric utilized to characterize this benefit revolves around the disparity between the upstream and downstream lake levels.

<!-- b000194 | prose | pages [6, 7] -->
(5)关注数学模型 p Q = ρ · hriver · w · hup −hdown Nevertheless, when the lake water level stabilizes in a micro-dynamic equilibrium state, the flow exhibits minimal variation with changes in the water level. The river p hup −hdown water level is inversely proportional to . The benefit function of ship- ping revenue can be expressed by: 微信公众号：数学模型 5 1 1 X Qi,i+1 · ÷ S = (6) p p hi·up −hi·down hi0·up −hi0·down i=1

<!-- b000195 | furniture | pages [6] -->
2

<!-- b000196 | furniture | pages [6] -->
MATHmodels

<!-- b000197 | furniture | pages [6] -->
获取更多资讯

<!-- b000198 | furniture | pages [7] -->
Team # 2417831

<!-- b000199 | furniture | pages [7] -->
Page 7 of 25

<!-- b000201 | prose | pages [7] -->
where Qi,i+1 represents the water flow between the two lakes and is related to the difference in lake levels and lake water capacity.

<!-- b000202 | prose | pages [7] -->
(5) Ecological Effect

<!-- b000203 | prose | pages [7] -->
The ecological consequences of lake and river water levels are primarily tied to the preservation and disruption of species diversity. To streamline the evaluation of their water level impacts on ecosystems, assessments can be made using the disparity between water level fluctuations, using the average of high water levels and the aver- age of low water levels. A smaller discrepancy between the two is considered a more 微信号：MATHmodels favorable benefit function:

<!-- b000204 | prose | pages [7] -->
5 ˆ max(hi) − ˆ min(hi) X · Ai S = (7) ˆ max(hi0) − ˆ min(hi0) i=1

<!-- b000205 | prose | pages [7] -->
where Ai represents the impact factor of the lake, which is proportional to the lake area.

<!-- b000206 | heading | pages [7] -->
2.3 Analysis of Weights

<!-- b000207 | prose | pages [7] -->
By employing the Analytic Hierarchy Process (AHP) to evaluate the aforemen- tioned potential factors, we can ascertain the relative weights of the corresponding benefit functions.

<!-- b000208 | caption | pages [7] -->
Table 2: Weight of each factor

<!-- b000209 | prose | pages [7] -->
Stands For Weight

<!-- b000210 | prose | pages [7] -->
P Protection for Coastal Infrastructures 0.31 H Hydro-power Plant Revenue 0.10 L Leisure Satisfaction 0.22 S Shipping Revenue 0.10 E Ecological Effect 0.27

<!-- b000211 | caption | pages [7] -->
Figure 3: Weight matrix

<!-- b000212 | prose | pages [7] -->
As a result, the total benefit function is:

<!-- b000213 | prose | pages [7] -->
5 X S = | ϵi · Si| (8) i=1

<!-- b000214 | prose | pages [7, 8] -->
where ϵi signifies the weight assigned to each parameter. It’s crucial to emphasize that the aim of the protection cost, life satisfaction, and ecological impact is to minimize the benefit function. Therefore, the weights associated with these aspects should be converted into negative values. Additionally, given the substantial influence of these关注数学模型 three items in the overall weight distribution, it becomes necessary to consider the absolute value of the total benefit function within the fitness function of the genetic model. This approach is essential for determining the probability of selection in the genetic model. 微信公众号：数学模型

<!-- b000215 | furniture | pages [7] -->
2

<!-- b000216 | furniture | pages [7] -->
MATHmodels

<!-- b000217 | furniture | pages [7] -->
获取更多资讯

<!-- b000218 | furniture | pages [8] -->
Team # 2417831

<!-- b000219 | furniture | pages [8] -->
Page 8 of 25

<!-- b000221 | heading | pages [8] -->
2.4 Presentation of Results

<!-- b000222 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000223 | caption | pages [8] -->
Figure 4: Optimal water level V.S. historical mean level

<!-- b000224 | caption | pages [8] -->
Figure 5: Historical average and optimal water level radar chart

<!-- b000225 | prose | pages [8, 9] -->
As shown in Figure 4, the colored lines indicate the optimal water levels for each lake. It is evident that the predicted optimal water levels for all lakes, except for Lake Ontario, are lower than the average of previous years. The observed discrepancy may be attributed to the prioritization of resident safety in the AHP method, as residents generally prefer lower water levels. By examining the radar chart, the benefits of ship- ping and hydro-power plants are already high, with marginal improvements. The关注数学模型 model excels in enhancing resident safety and leisure satisfaction, ensuring readiness for various situations through subsequent control algorithms.

<!-- b000226 | furniture | pages [8] -->
2

<!-- b000227 | furniture | pages [8] -->
MATHmodels

<!-- b000228 | furniture | pages [8] -->
获取更多资讯

<!-- b000229 | furniture | pages [9] -->
Team # 2417831

<!-- b000230 | furniture | pages [9] -->
Page 9 of 25

<!-- b000232 | prose | pages [9] -->
However, the improvement in ecosystem benefits is not evident under the optimal water level. The reason is that after fulfilling the requirements of coastal residents for 微信公众号：数学模型 stable water levels, the cyclic changes in water levels may not reach historical averages, potentially causing disturbances to the ecosystem. Nevertheless, these disturbances are expected to be within the normal self-regulation capacity of the ecosystem.

<!-- b000233 | prose | pages [9] -->
In summary, considering protection for residents, hydro-power revenue, leisure satisfaction, shipping revenue, and ecosystem impacts, the model provides a monthly average optimal water level for the Great Lakes.

<!-- b000234 | heading | pages [9] -->
3 Task2: Establishment of Algorithms for Water Level

<!-- b000235 | prose | pages [9] -->
Control

<!-- b000236 | prose | pages [9] -->
微信号：MATHmodels This task includes model building and an algorithm designed to control the water level of the Great Lakes.

<!-- b000237 | heading | pages [9] -->
3.1 Hydrodynamic Model of the Lake Chain

<!-- b000238 | prose | pages [9] -->
This section introduces the hydrodynamic model we established, to simulate the in- terconnected lake system which is simplified and approximated in the following ways:

<!-- b000239 | prose | pages [9] -->
(1) The Great Lakes are modeled as a chain, as shown in Figure 6.

<!-- b000240 | caption | pages [9] -->
Figure 6: Lake chain model schema

<!-- b000241 | prose | pages [9] -->
(2) Inter-lake flow rate equations are derived from Manning’s formula, in which We considered the lake basin shape, the lakes’ relative positions ,and the river channel. Besides, Lake St.Clair is specialized in the model.

<!-- b000242 | prose | pages [9] -->
(3) External factors, including precipitation, evaporation, snow-melt water, and in- dustrial and agricultural water consumption are considered.

<!-- b000243 | prose | pages [9] -->
As illustrated in Figure 7, the general modeling process for the lake chain can be described as follows: external runoff enters Lake Superior, initiating a directional flow through the lake chain shown above, reaching the Atlantic Ocean ultimately. In this se- quential progression, each lake within the lake chain not only receives inflow from the preceding lake but also takes into account external runoff, evaporation, precipitation, snow-melt water, and human factors.

<!-- b000244 | prose | pages [9] -->
During this process, the change in the water level of each lake can be expressed as:

<!-- b000245 | prose | pages [9] -->
dt = Qin(i) −Qout(i) dhi (9)关注数学模型

<!-- b000246 | furniture | pages [9] -->
2

<!-- b000247 | prose | pages [9, 10] -->
Ai 微信公众号：数学模型

<!-- b000248 | furniture | pages [9] -->
MATHmodels

<!-- b000249 | furniture | pages [9] -->
获取更多资讯

<!-- b000250 | furniture | pages [10] -->
Team # 2417831

<!-- b000251 | furniture | pages [10] -->
Page 10 of 25

<!-- b000253 | caption | pages [10] -->
Figure 7: Flow directions of the Great Lakes

<!-- b000254 | prose | pages [10] -->
微信号：MATHmodels In the forthcoming sections, we will delineate the parameterization process of our lake chain model, focusing on both the internal water flow within the chain and the exter- nal factors influencing the chain.

<!-- b000255 | heading | pages [10] -->
3.1.1 Internal Water Flow

<!-- b000256 | prose | pages [10] -->
Water flow between lakes stands out as a crucial factor influencing the respective changes in lake water levels. It is influenced by factors including the relative height difference, the characteristics of the river channel connecting the lakes, and the nature of the lake basin. These factors are introduced to our model for precise emulation of the real dynamics of water flow within the lake system.

<!-- b000257 | prose | pages [10] -->
Topography of the lake basin:

<!-- b000258 | prose | pages [10] -->
The presence of lakes exerts a decelerating influence on water flow. Distinct to- pographies of lake basins impart varying capacities to buffer water flow, and features such as irregularities in the lake bottom can impact the flow dynamics. Depressions on the lake bottom may give rise to grooves, introducing friction and resistance to water flow.

<!-- b000259 | caption | pages [10] -->
Table 3: Geographic information of the Great Lakes

<!-- b000260 | prose | pages [10] -->
Superior Michigan+Huron St. Clair Erie Ontario Area (m2) 82103 117620 1100 25874 19000 Mean Depth (m) 147 72 3.4 19 86 Annual Precipitation (mm) 760 787 1720.5 864 914 Evaporation(mm) 596 639 902 697 650 Elevation (m) 183 176 173 173 74

<!-- b000261 | prose | pages [10] -->
Geomorphic characteristics of the Great Lakes basins are depicted in Figure 8 and

<!-- b000262 | caption | pages [10] -->
Table 3 with the Lake Erie basin identified as the shallowest and flattest, resulting in the

<!-- b000263 | prose | pages [10] -->
least hindrance to water flow. Conversely, the Lake Superior basin displays a complex geomorphology, leading to a more pronounced impedance to water flow – a facet that 关注数学模型 will be evident in the subsequent modeling process.

<!-- b000264 | furniture | pages [10] -->
2

<!-- b000265 | furniture | pages [10] -->
MATHmodels

<!-- b000266 | furniture | pages [10] -->
获取更多资讯

<!-- b000267 | furniture | pages [11] -->
Team # 2417831

<!-- b000268 | furniture | pages [11] -->
Page 11 of 25

<!-- b000269 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000270 | caption | pages [11] -->
Figure 8: Topography of the Great Lakes

<!-- b000271 | caption | pages [11] -->
Table 4: Geographic information of the rivers

<!-- b000272 | prose | pages [11] -->
微信号：MATHmodels St. Mary’s Detroit Niagara Ottawa St. Lawrence Mean Flow Rate (m3/s) 2135 5300 5796 1950 10400 Mean Width (m) 64 2000 800 2500 3000 Mean Depth (m) 6 12 7 90 11

<!-- b000273 | prose | pages [11] -->
River channel:

<!-- b000274 | prose | pages [11] -->
The Manning-Strickler formula characterizes the connection between the flow of unconfined water within a channel and various factors such as channel geometry, bed friction, and current velocity.I t can be expressed as:

<!-- b000275 | prose | pages [11] -->
2 1 3 · E Q = S · R 2 (10) n

<!-- b000276 | prose | pages [11] -->
where Q represents the river’s flow rate between the lakes. R denotes the length of the wetted perimeter length along the cross-section of the flow and S represents the cross- sectional area of the river, while the former is positively correlated with the width of the river and the latter with the square of that. n stands for Manning’s friction coefficient, reflecting the resistance on the riverbed. The energy gradient drop E is mainly associated with the river slope which is determined by utilizing the difference in mean heights of the two lakes from Table 3. Given this analysis, the internal flow equations employed in the model for the lake chain can be rewritten as:

<!-- b000277 | prose | pages [11] -->
2 = N0 · w2 · w 2 1 2 1 3 · E 3 · (g(hi −hi+1) −fi,i+1 · di,i+1) S · R (11) 2

<!-- b000278 | prose | pages [11] -->
8 1 3 · (g(hi −hi+1) −fi,i+1 · di,i+1) Qout(i) = N · w (12) 2

<!-- b000279 | prose | pages [11, 12] -->
Here, N0 and N are constant coefficients, di,i+1 signifies the distance between the ith and the (i + 1)th lake, and w stands for the river width. fi,i+1 denotes the flow friction cost parameter between the two lakes, which is rimarily influenced by the topography and geomorphology of the lake basin and the friction coefficient of the riverbed. Due to the difficulty in accurately determining these parameters, initial approximations are provided during the simulation process based on varying lake basin geomorphologies,关注数学模型 channel lengths, and depths as presented in Figure 8 and Table 4. Further refinements are carried out through iterative adjustments in the simulation process.

<!-- b000280 | furniture | pages [11] -->
2

<!-- b000281 | furniture | pages [11] -->
MATHmodels

<!-- b000282 | furniture | pages [11] -->
获取更多资讯

<!-- b000283 | furniture | pages [12] -->
Team # 2417831

<!-- b000284 | furniture | pages [12] -->
Page 12 of 25

<!-- b000286 | prose | pages [12] -->
The Lake St. Clair:

<!-- b000287 | prose | pages [12] -->
微信公众号：数学模型 According to Table 3, Lake St. Clair is notably smaller in area when compared to the Great Lakes. To streamline the model regulation process, we opt to treat it as a distinctive river entity rather than as a node within the lake chain.

<!-- b000288 | prose | pages [12] -->
Recognizing that lakes possess a significantly greater water storage capacity than rivers, implying a pronounced hysteresis effect on water, we introduced a hysteresis parameter τ, as shown in (11), between Lake Huron and Lake Erie which requires to be manually adjusted during the modeling process.

<!-- b000289 | prose | pages [12] -->
8 Qout(i) = N · ((hi · (t −τ) −hi+1) −fi,i+1 · di,i+1) · w (13) 3

<!-- b000290 | heading | pages [12] -->
3.1.2 External Factors

<!-- b000291 | prose | pages [12] -->
微信号：MATHmodels External runoff inflow:

<!-- b000292 | prose | pages [12] -->
Lake Superior receives contributions from over two hundred streams. For the rest of the lakes, the primary sources of external runoff are the rivers upstream. We desig- nate the external runoff inflow to Lake Superior as the largest, while the external runoff inflow to the other lakes (excluding inter-chain inflows) is comparatively smaller.

<!-- b000293 | prose | pages [12] -->
Evaporation:

<!-- b000294 | prose | pages [12] -->
Evaporation from lakes is primarily influenced by factors such as lake area, tem- perature, wind, and air humidity. As noted by D. Lenters, B. Anderton, D. Blanken,et al., lakes exhibit seasonally significant variations in evaporation, reaching a maximum of 0.4 ft/day in the fall when evaporation is at its peak. Our estimation of the seasonal variation in evaporation for the Great Lakes is derived from the information presented in Table 3.

<!-- b000295 | prose | pages [12] -->
Precipitation:

<!-- b000296 | prose | pages [12] -->
Annual precipitation in the Great Lakes approximately varies between 750mm and 950 mm, with an increase from Lake Superior to Lake Ontario.

<!-- b000297 | prose | pages [12] -->
Upon analyzing the meteorological data of the Great Lakes region, we can refine the model by adjusting evaporation and precipitation settings based on seasonal vari- ations. This enhancement allows for a more accurate simulation of seasonal changes within the model. The inflow rate for the ith lake in the chain is expressed as:

<!-- b000298 | prose | pages [12] -->
Qin(i) = Qout(i −1) + Qrain(i) −Qev(i) (14) Qrain,i is the precipitation of the ith lake, and Qev,i is the evaporation of the ith lake.

<!-- b000299 | prose | pages [12] -->
Ultimately, to identify the parameters in the model that require manual adjustment, we make these adjustments based on observed river flows within the lake chain. This careful calibration ensures that the model’s inflows and outflows between the lakes are closely aligned with actual values.

<!-- b000300 | prose | pages [12] -->
关注数学模型

<!-- b000301 | furniture | pages [12] -->
2

<!-- b000302 | furniture | pages [12] -->
MATHmodels

<!-- b000303 | furniture | pages [12] -->
获取更多资讯

<!-- b000304 | furniture | pages [13] -->
Team # 2417831

<!-- b000305 | furniture | pages [13] -->
Page 13 of 25

<!-- b000306 | heading | pages [13] -->
3.2 Control Algorithm Design

<!-- b000307 | heading | pages [13] -->
3.2.1 Classical Control Algorithms Synthesis

<!-- b000308 | prose | pages [13] -->
微信公众号：数学模型 (1) PID controller is a classical feedback control algorithm aimed to achieve stable and accurate control. The output of the controller is the weighted sum of these three control terms:

<!-- b000309 | prose | pages [13] -->
Z t de(t) u(t) = Kpe(t) + Ki e(τ)dτ + Kd (15) dt 0

<!-- b000310 | prose | pages [13] -->
where Kp represents the proportional gain, and e(t) denotes the current error of the R t system. The integral gain is represented by Ki, and 0 e(τ)dτ represents the cumulative error over time. Kd stands for the differential gain, and de(t) dt is the rate of change of the error. By adjusting the proportional, integral, and differential gains, precise control of the system can be achieved across various applications.

<!-- b000311 | prose | pages [13] -->
微信号：MATHmodels (2) Model predictive control (MPC) is an advanced method of process control based on a system model, optimizing the current control inputs by predicting the future be- havior of the system. Ts working principle involves:

<!-- b000312 | prose | pages [13] -->
▷Establishing a dynamic model of the system to predict its evolution over a future time horizon ▷Choosing the optimal control strategy at each time step by solving an optimiza- tion problem.

<!-- b000313 | prose | pages [13] -->
MPC excels in handling complex, nonlinear systems, and dynamic environments. Through real-time iterative updates, MPC can promptly adjust to changes in system states, achieving efficient control of the system.

<!-- b000314 | heading | pages [13] -->
3.2.2 Controller Design

<!-- b000315 | prose | pages [13] -->
In the context of the Great Lakes water flow control problem, the regulation of water volume within the Great Lakes is limited to interventions through the upstream compensation project and the Moses-Saunders Dam.

<!-- b000316 | prose | pages [13] -->
The application of PID solely for the upstream water flow control of the dams is suitable for straightforward scenarios. However, it is anticipated to encounter the fol- lowing issues in a complex circumstance:

<!-- b000317 | prose | pages [13] -->
▷Achieving water flow control across the entire lake chain is challenging when only having regulatory control over two dams. The number of systems that require control exceeds the available number of controllers, posing a complexity in managing the overall water flow dynamics.

<!-- b000318 | prose | pages [13] -->
▷Fixed coefficients in the controller, leading to limited adaptability to dynamic en- vironmental changes. The controller’s ability to adapt to a changing environment, including evaporation and rainfall, is relatively low.

<!-- b000319 | prose | pages [13, 14] -->
▷The controller is highly sensitive to parameters. In a complex and dynamic en- vironment, even small changes in parameters can significantly impact the regulation effect. If the manually determined parameters are not optimal, the entire system may face an out-of-control situation over time. 关注数学模型 Our proposed solution is graphed in Figure 9. The compensating work utilizes a mode-switchable P+PI control as the primary real-time feedback controller while the other one can switch between flood-releasing mode and PI control. Besides, a pre- diction module is used for optimizing the feedback control parameters. The structure 微信公众号：数学模型 addresses the issues mentioned above.

<!-- b000320 | furniture | pages [13] -->
2

<!-- b000321 | furniture | pages [13] -->
MATHmodels

<!-- b000322 | furniture | pages [13] -->
获取更多资讯

<!-- b000323 | furniture | pages [14] -->
Team # 2417831

<!-- b000324 | furniture | pages [14] -->
Page 14 of 25

<!-- b000326 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000327 | caption | pages [14] -->
Figure 9: Controller schema

<!-- b000328 | heading | pages [14] -->
3.2.3 Mode-switchable Feedback Control module

<!-- b000329 | prose | pages [14] -->
Typically, controllers for compensating engineered dams usually operate in the sim- ple P mode. It means they deploy proportional control based on the difference between the Lake Superior water level and the target level. As shown in Equation 15.

<!-- b000330 | prose | pages [14] -->
However, solely focusing on the lakes upstream of the dam does not guarantee effective regulation of Lake Huron, Lake Michigan, as well as Lake Erie.

<!-- b000331 | prose | pages [14] -->
Therefore, we modified the integral control of the controller which takes the cumu- lative error information of the water level in the lakes downstream into account. When the cumulative error of the water level of Lake Huron and Lake Michigan exceeds the control threshold I0, the controller switches from P mode to PI mode as Equation 16:

<!-- b000332 | prose | pages [14] -->
Q(t) = Kp1 · (htarget −h) · A (16)   Z Kp1 · (htarget −h) + Ki1 · · A Q(t) = te(τ)dτ (17)

<!-- b000333 | prose | pages [14] -->
Here, Q(t) represents the current control variable, which is the discharge of the compensation project. K1 and K2 are the proportional and integral gains, respectively.

<!-- b000334 | prose | pages [14] -->
R A is the lake area, and te(τ)dτ is the cumulative water level error of Lake Huron-Lake Michigan. The controller indicates that when the water level error of Lake Huron- Lake Michigan reaches a certain threshold, the controller will balance the water level downstream.

<!-- b000335 | prose | pages [14] -->
It is important to note that:

<!-- b000336 | prose | pages [14, 15] -->
(1) The P+PI controller is made to better achieve the decoupling of water level con- trol between the two lakes. In comparison to using a P controller to alternately switch关注数学模型 control between the two lakes or concentrating the PI controller solely on the upper lake, this method shows greater stability and comprehensiveness for controlling the entire lake chain.

<!-- b000337 | furniture | pages [14] -->
2

<!-- b000338 | furniture | pages [14] -->
MATHmodels

<!-- b000339 | furniture | pages [14] -->
获取更多资讯

<!-- b000340 | furniture | pages [15] -->
Team # 2417831

<!-- b000341 | furniture | pages [15] -->
Page 15 of 25

<!-- b000343 | prose | pages [15] -->
微信公众号：数学模型 (2) The differential controller has been omitted for the reason that in the practical regulation of reservoirs, the volume of water in the lakes is significantly larger than the maximum discharge capacity of the controlled dams. As a result, the control process is relatively slow. making the role of the differential controller minimized.

<!-- b000344 | prose | pages [15] -->
As for the Moses-Saunders Dam, a switchable PI+flood-releasing controller is em- ployed. The decision to not adopt the P+PI control mode as in the Compensating Work is based on the consideration that the mode is not well-suited for controlling upstream water flow.

<!-- b000345 | prose | pages [15] -->
The purpose of the switchable controller is to align with upstream hydrological conditions: when the water level of a lake upstreams on Lake Ontario exceeds the threshold value hcontrol, the flood-releasing mode is activated to maximize discharge while ensuring the stability of Lake Ontario’s water level. This is achieved by selecting 微信号：MATHmodels the minimum value between the maximum release from the dam and the estimated external inflow.

<!-- b000346 | prose | pages [15] -->
Qout = min {Qmax, (Qin + Qrain −Qev)} (18)

<!-- b000347 | prose | pages [15] -->
When upstream hydrological conditions are relatively stable, the Moses-Saunders Dam is primarily utilized to ensure the stability of Lake Ontario’s water level. In this scenario, PI mode is employed, with corresponding parameters for the proportional control Kp2 and Ki2.

<!-- b000348 | heading | pages [15] -->
3.2.4 Prediction Module

<!-- b000349 | prose | pages [15] -->
The primary goal of the prediction module is to dynamically adjust the parameters of the compensating project dam controller and the Moses-Sanders dam controller. The process involves:

<!-- b000350 | prose | pages [15] -->
(1) Predict the future change in the lake level in the lake chain for the next 200 hours with the current controller parameters.

<!-- b000351 | prose | pages [15] -->
(2) Optimize the parameters, by using gradient descent, based on an object function manually set.

<!-- b000352 | prose | pages [15] -->
Regarding the parameters of the two controllers, we express them using a vector formulation:

<!-- b000353 | prose | pages [15] -->
c = (Kp1, Ki1, I0, hcontrol, Kp2, Ki2) (19)

<!-- b000354 | prose | pages [15] -->
The error function is defined as: E(i, t, c) = (hi(t) −hi,target(t))2. Subsequently, the objective function J(c) is set to the sum of squares of the errors within this prediction time domain:

<!-- b000355 | prose | pages [15, 16] -->
4 200 X X J(c) = E(i, t, c) (20) t=0 i=1 During the deployment phase, we discovered that the determination of the optimal关注数学模型 controller parameters, denoted as copt, through the application of a gradient descent algorithm is time-consuming, also necessities to fine-tune a multitude of parameters. Given the complexity and the resource-intensive nature of this optimization process, a strategic decision was made to narrow the focus of our optimization efforts. Specifi- 微信公众号：数学模型 cally, we opted to concentrate on Kp2 and KI2 as the key parameters for optimization.

<!-- b000356 | furniture | pages [15] -->
2

<!-- b000357 | furniture | pages [15] -->
MATHmodels

<!-- b000358 | furniture | pages [15] -->
获取更多资讯

<!-- b000359 | furniture | pages [16] -->
Team # 2417831

<!-- b000360 | furniture | pages [16] -->
Page 16 of 25

<!-- b000362 | heading | pages [16] -->
3.3 Algorithm Verification

<!-- b000363 | prose | pages [16] -->
To initially assess the control performance of our controller, we established distinct target water levels for each lake in the chain. In the simulation, we observed the water level changes in the lakes along with the water outflow from each lake, as illustrated in

<!-- b000364 | caption | pages [16] -->
Figure 10. The dotted lines represent the target water levels set for each lake, featuring

<!-- b000365 | prose | pages [16] -->
a water level difference of 0.5 m-1 m from the current water level.

<!-- b000366 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000367 | caption | pages [16] -->
Figure 10: Effect of controller regulation under natural conditions

<!-- b000368 | prose | pages [16] -->
The Compensating Works:

<!-- b000369 | prose | pages [16] -->
As Lake Superior consistently maintained a water level above the target and down- stream Lake Huron and Lake Michigan remained below the target throughout the sim- ulation period, the Compensating Works consistently utilized a discharge close to the maximum flow.

<!-- b000370 | prose | pages [16] -->
The Moses-Saunders Dam:

<!-- b000371 | prose | pages [16] -->
As Lake Ontario exceeded the target level, Moses-Saunders Dam employed a strat- egy of larger discharges to stabilize Lake Ontario’s levels. Subsequently, as the Lake Ontario level approached the target, the dam reduced its discharge and adjusted it to align with the incoming flow. This approach facilitated Lake Ontario in reaching a more stable level.

<!-- b000372 | prose | pages [16] -->
关注数学模型

<!-- b000373 | furniture | pages [16] -->
2

<!-- b000374 | furniture | pages [16] -->
MATHmodels

<!-- b000375 | furniture | pages [16] -->
获取更多资讯

<!-- b000376 | furniture | pages [17] -->
Team # 2417831

<!-- b000377 | furniture | pages [17] -->
Page 17 of 25

<!-- b000378 | heading | pages [17] -->
4 Task 3: Sensitivity Analysis on Outflow of the Two

<!-- b000379 | prose | pages [17] -->
Dam Controllers

<!-- b000380 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000381 | heading | pages [17] -->
4.1 System Sensitivity on Control Output

<!-- b000382 | prose | pages [17] -->
The impacts of increasing the outflows from the two dams are illustrated below, where ’-L’ is denoted as a large flow rate and ’-S’ is a small flow rate. In Figure 11, the regulation pertains to the Soo Locks (upstream), while in Figure 12, it corresponds to the regulation of the Moses-Saunders Dam (downstream).

<!-- b000383 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000384 | caption | pages [17] -->
Figure 11: Effects of the Soo Locks flow rate on water levels

<!-- b000385 | caption | pages [17] -->
Figure 12: Effects of the Moses-Saunders Dam flow rate on water levels

<!-- b000386 | prose | pages [17, 18] -->
Comparing the two figures reveals that Lake Ontario’s water level is predominantly influenced by the operation of the Moses-Saunders Dam, whereas the water levels of the four upstream lakes are more significantly impacted by the Soo Locks. This distinction is largely due to Niagara Falls, which introduces a dramatic elevation drop of approximately one hundred meters between Lake Erie and Lake Ontario, resulting in unidirectional flow between these lakes. The primary driving force for the water movement is this substantial topographic descent, rather than the usual differential in water levels. Consequently, normal variations in lake levels exert minimal effect on the关注数学模型 flow between these two lakes. Additionally, the water level of the lake is particularly sensitive to adjustments in dam flow; a change of about 2000 cubic meters per second can cause a water level variation of around 0.2 meters in just 10 days, facilitating rapid response to emergency conditions. 微信公众号：数学模型

<!-- b000387 | furniture | pages [17] -->
2

<!-- b000388 | furniture | pages [17] -->
MATHmodels

<!-- b000389 | furniture | pages [17] -->
获取更多资讯

<!-- b000390 | furniture | pages [18] -->
Team # 2417831

<!-- b000391 | furniture | pages [18] -->
Page 18 of 25

<!-- b000393 | heading | pages [18] -->
4.2 A Comparison with Water Level in 2017

<!-- b000394 | prose | pages [18] -->
To better assess the efficacy of our water level control model, we compare the 2017 water level data with the upper and lower boundary water levels under optimal con- ditions.

<!-- b000395 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000396 | caption | pages [18] -->
Figure 13: Optimal water level V.S. water level in 2017

<!-- b000397 | prose | pages [18] -->
Visualized in Figure 13, it is evident that while the control algorithm may not en- sure the water level aligns perfectly with the optimal level, its performance remains excellent relative to the 2017 water conditions, particularly in terms of ’Protection’ and ’Hydro-power’.

<!-- b000398 | heading | pages [18] -->
5 Task 4: Sensitivity analysis to environmental changes

<!-- b000399 | prose | pages [18] -->
The control effect of the dams is assessed in the presence of dynamic changes in the environment. Among the environmental changes, heavy rainfall, and ice jams are the two largest impacts on the lake’s water level. In this section, the simulation system is run under both circumstances, the system without dams is used as a baseline to demonstrate the effectiveness and stability of our algorithms.

<!-- b000400 | heading | pages [18] -->
5.1 Algorithm Sensitivity to Heavy Precipitation

<!-- b000401 | prose | pages [18] -->
Firstly, we analyzed the simulation system after substantial precipitation occurred on Lake Huron and Lake Michigan without dam control as illustrated in Figure 14.

<!-- b000402 | prose | pages [18, 19] -->
关注数学模型 微信公众号：数学模型

<!-- b000403 | furniture | pages [18] -->
2

<!-- b000404 | furniture | pages [18] -->
MATHmodels

<!-- b000405 | furniture | pages [18] -->
获取更多资讯

<!-- b000406 | furniture | pages [19] -->
Team # 2417831

<!-- b000407 | furniture | pages [19] -->
Page 19 of 25

<!-- b000409 | caption | pages [19] -->
Figure 14: Control system’s response to heavy precipitation without dam

<!-- b000410 | prose | pages [19] -->
After heavy precipitation, the water level in Lake Huron and Lake Michigan rises rapidly, leading to a rapid increase in outflow due to the significant water level differ- 微信号：MATHmodels ence with downstream lakes.

<!-- b000411 | prose | pages [19] -->
10-200h: Lake levels in Lakes Huron and Lake Michigan decrease after precipita- tion ceases. The water level of Lake Superior begins to rise due to the increased down- stream level in Lake Huron, causing a reduction in flow between Lake Superior and Lake Huron. Lake St.Clair introduces a blocking effect between Lake Huron and Lake Erie, resulting in Lake Erie’s water level experiencing a gradual rise instead of drastic changes. Lake Ontario’s water level exhibits a downward trend during this period, primarily due to Lake Erie’s pronounced retardation effect. The outflow induces slow growth in water level, without a direct and conspicuous impact on Lake Ontario.

<!-- b000412 | prose | pages [19] -->
200-1500h: As the levels of Lake Huron and Lake Michigan decline, the upward trend in Lake Superior starts to decelerate and eventually stabilizes. Lake Erie’s lev- els begin to decrease with the reduction of the Lake Huron’s outflow. While Lake Ontario’s levels experience a significant lag and remain well above the target due to hysteresis.

<!-- b000413 | prose | pages [19] -->
Then we incorporate the dam controller into the model as shown in Figure 15.

<!-- b000414 | caption | pages [19] -->
Figure 15: Control system’s response to heavy precipitation with dam controller

<!-- b000415 | prose | pages [19, 20] -->
10-200h: The cumulative error in downstream lake levels triggers the PI mode of the Compensating dams. The rising water levels in the three lakes also activate the flood-关注数学模型 release mode of the downstream Moses-Saunders Dam. Lake Superior’s water level rises faster compared to the no-dam scenario. Accordingly, Lake Ontario returns to a safe water level faster. Lake Huron and Lake Michigan experience a more pronounced water level drop, with the dam-regulated condition showing a water level about 0.25m 微信公众号：数学模型 lower than the no-dam condition at 200h.

<!-- b000416 | furniture | pages [19] -->
2

<!-- b000417 | furniture | pages [19] -->
MATHmodels

<!-- b000418 | furniture | pages [19] -->
获取更多资讯

<!-- b000419 | furniture | pages [20] -->
Team # 2417831

<!-- b000420 | furniture | pages [20] -->
Page 20 of 25

<!-- b000422 | prose | pages [20] -->
200h-1500h: After the substantial drop in water levels in Lakes Huron and Lake Michigan, Lake Superior resumes some drainage to prevent further increases in water levels. Lake Ontario is very close to the optimal level during this period.

<!-- b000423 | heading | pages [20] -->
5.2 Algorithm Sensitivity to Ice Jam

<!-- b000424 | prose | pages [20] -->
The controller’s regulation during ice jams in Lake Michigan and Lake Huron with- out a dam is shown in Figure 16.

<!-- b000425 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000426 | caption | pages [20] -->
Figure 16: Control system’s response to ice jams without dam controller

<!-- b000427 | prose | pages [20] -->
0-500h: The outflow from Lake Huron and Lake Michigan is minimal, causing a rise in water levels. This leads to a decrease in inflow between Lakes Superior and Lake Huron, resulting in an increase in Lake Superior’s water level. Lake Erie experiences a decrease in water level and outflow due to lower inflow.

<!-- b000428 | prose | pages [20] -->
500h-1500h: Lower water levels in downstream lakes enable an increase in flow between Lake Huron and Lake Erie. The ice jam eases, allowing the outflow from Lake Huron to gradually recover, and the upward trend in water levels slows down.

<!-- b000429 | prose | pages [20] -->
The result control system’s response to ice jam changes is shown in Figure 17.

<!-- b000430 | prose | pages [20] -->
0-500h: The outflow from Lake Huron and Lake Michigan is minimal, causing a rise in water levels. This leads to a decrease in inflow between Lakes Superior and Lake Huron, resulting in an increase in Lake Superior’s water level. Lake Erie experiences a decrease in water level and outflow due to lower inflow.

<!-- b000431 | prose | pages [20] -->
500h-1500h: Lower water levels in downstream lakes enable an increase in flow between Lake Huron and Lake Erie. The ice jam eases, allowing the outflow from Lake Huron to gradually recover, and the upward trend in water levels slows down.

<!-- b000432 | prose | pages [20] -->
This section verifies the robustness of our control algorithms toward environmental changes. However, the results also indicate that the dams’ control abilities are limited in the face of rapid changes.

<!-- b000433 | prose | pages [20, 21] -->
关注数学模型 微信公众号：数学模型

<!-- b000434 | furniture | pages [20] -->
2

<!-- b000435 | furniture | pages [20] -->
MATHmodels

<!-- b000436 | furniture | pages [20] -->
获取更多资讯

<!-- b000437 | furniture | pages [21] -->
Team # 2417831

<!-- b000438 | furniture | pages [21] -->
Page 21 of 25

<!-- b000440 | caption | pages [21] -->
Figure 17: Control system’s response to ice jams with dam controller

<!-- b000441 | heading | pages [21] -->
6 Task 5: Focusing on Lake Ontario

<!-- b000442 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000443 | heading | pages [21] -->
6.1 Social and Physical Geographical Analysis

<!-- b000444 | prose | pages [21] -->
The St. Lawrence River, situated downstream from Lake Ontario, converges with the Ottawa River in Montreal. The combined runoff from these two rivers, along with the water level of Lake Ontario, exerts a substantial impact on the safety of coastal cities and the well-being of relevant stakeholders.

<!-- b000445 | caption | pages [21] -->
Figure 18: Focusing on the local area of Lake Ontario and Ottawa River

<!-- b000446 | prose | pages [21] -->
The regulation of the Ottawa River’s runoff is intricately tied to the management of numerous upstream reservoirs. Meanwhile, control over Lake Ontario’s water level predominantly hinges on the operations of the Moses-Saunders Dam. When imple- menting these regulations, it is imperative to consider a myriad of social and physical geographical factors:

<!-- b000447 | prose | pages [21] -->
(1) Economic Activities: Balancing the needs of economic endeavors like shipping, hydro-power plants, and leisure activities.

<!-- b000448 | prose | pages [21] -->
(2) flood protection: Prioritizing the flood protection requirements of communities and residents, especially ensuring the safety of downstream areas such as Montreal.

<!-- b000449 | prose | pages [21, 22] -->
(3) Upstream and Downstream Dynamics: Taking into account the conditions of upstream and downstream water levels and flows, notably those of the Ottawa River关注数学模型 and the four Great Lakes upstream.

<!-- b000450 | furniture | pages [21] -->
2

<!-- b000451 | furniture | pages [21] -->
MATHmodels

<!-- b000452 | furniture | pages [21] -->
获取更多资讯

<!-- b000453 | furniture | pages [22] -->
Team # 2417831

<!-- b000454 | furniture | pages [22] -->
Page 22 of 25

<!-- b000456 | prose | pages [22] -->
(4) Climate Change Impact: Preparing for extreme weather events induced by cli- mate change, and acknowledging their potential influence on the regulation process.

<!-- b000457 | prose | pages [22] -->
微信公众号：数学模型 (5) Seasonal Changes: Adapting to seasonal changes, including heightened flows due to spring snowmelt. Considering the broader impacts of climate change on pre- cipitation, evaporation, and overall water dynamics.

<!-- b000458 | prose | pages [22] -->
(6) Environmental Considerations: Addressing environmental and ecosystem re- quirements, ensuring the maintenance of water quality, and promoting biodiversity in regulated areas.

<!-- b000459 | prose | pages [22] -->
Assigning appropriate weights to the factors based on seasonal characteristics and real-time hydrological conditions is essential for effective dam regulation using the established algorithm. The primary challenges in this endeavor include:

<!-- b000460 | prose | pages [22] -->
(1) The historical data reveals a significant correlation between elevated water lev- els in Lake Ontario and increased snowmelt in the Ottawa and upstream regions from April to August. During this period, augmenting flood releases from the Moses Saun- 微信号：MATHmodels ders Dam to align with the heightened runoff from the Ottawa River poses a risk of flooding in Montreal. Therefore, there is a crucial necessity to collaboratively regulate the runoff from both rivers, ensuring the safety not only of Montreal but also of the shoreline of Lake Ontario.

<!-- b000461 | prose | pages [22] -->
(2) Establishment of a sensible stakeholder weighting is essential (and it should vary seasonally). For instance, during the spring and summer months, a higher weight- ing is necessary to prioritize and emphasize resident safety.

<!-- b000462 | heading | pages [22] -->
6.2 Reanalysis of Stakeholders

<!-- b000463 | caption | pages [22] -->
Figure 19: Stakeholders reanalysis radar chart

<!-- b000464 | prose | pages [22] -->
In the previous section, we developed optimal water level control in the Great Lakes system. When focusing on the local area of Lake Ontario-Ottawa River-Montreal, we can fine-tune the weights of individual benefit functions for different seasons or 关注数学模型 months by conducting a more detailed examination, as Equation 8.

<!-- b000465 | furniture | pages [22] -->
2

<!-- b000466 | furniture | pages [22] -->
MATHmodels

<!-- b000467 | furniture | pages [22] -->
获取更多资讯

<!-- b000468 | furniture | pages [23] -->
Team # 2417831

<!-- b000469 | furniture | pages [23] -->
Page 23 of 25

<!-- b000470 | prose | pages [23] -->
(1) Residents’ Safety: During the early spring snowmelt and increased summer rainfall, the potential for elevated water levels in Lake Ontario and the Ottawa River rises. Hence, it is imperative to amplify the weighting factor during this period to ensure the safety of residents and protect coastal properties. 微信公众号：数学模型 (2) Shipping Efficiency: Winter brings varying degrees of ice cover to different waterways, adversely affecting shipping efficiency. Consequently, during this period, it becomes essential to decrease the weight assigned to shipping considerations.

<!-- b000471 | prose | pages [23] -->
(3) Hydro-power Plant: The majority of power stations currently in construction are resilient to icing, minimizing the impact. However, during periods of substantial water flow, a slight increase in weight may be warranted.

<!-- b000472 | prose | pages [23] -->
(4) Leisure: Water recreation options are available in every season, emphasizing the need for a balanced consideration across the year.

<!-- b000473 | prose | pages [23] -->
(5) Ecological Effects: The ecological effects are contingent on local climatic condi- tions at any given time, with potential variations during abnormal climates. Weighting may be adjusted accordingly, placing a greater emphasis on ecological impacts during 微信号：MATHmodels unusual climatic conditions.

<!-- b000474 | heading | pages [23] -->
7 Model Evaluation and Further Discussion

<!-- b000475 | heading | pages [23] -->
7.1 Model Strengths

<!-- b000476 | prose | pages [23] -->
• The model selects the environmental factors comprehensively and scientifically.

<!-- b000477 | prose | pages [23] -->
It truly simulates the hydrological environment of the Great Lakes including in- ternal flow within the lakes-chain and external factors. It assures the reliability of our research.

<!-- b000478 | prose | pages [23] -->
• Our model is relatively robust with respect to its configuration parameters, i.e., demonstrates stability after changing river channel parameters, evaporation rate, etc.

<!-- b000479 | prose | pages [23] -->
• The control algorithm combines a prediction module with feedback control, which performs well under dynamic changes.

<!-- b000480 | heading | pages [23] -->
7.2 Model Weaknesses and Further Discussion

<!-- b000481 | prose | pages [23] -->
• Stakeholders are not considered comprehensively enough, and the determination of relative weights can also be based on more professional opinions.

<!-- b000482 | prose | pages [23] -->
• The dam control algorithm can generally consider the hydrological conditions across the entire basin, facilitating a more coordinated regulation with the up- stream reservoirs of the Ottawa River.

<!-- b000483 | prose | pages [23, 24] -->
关注数学模型 A Memo to IJC Leadership

<!-- b000484 | furniture | pages [23] -->
2

<!-- b000485 | furniture | pages [23] -->
MATHmodels

<!-- b000486 | furniture | pages [23] -->
获取更多资讯

<!-- b000487 | furniture | pages [24] -->
Team # 2417831

<!-- b000488 | furniture | pages [24] -->
Page 24 of 25

<!-- b000490 | prose | pages [24] -->
To whom it may concern, 微信公众号：数学模型 We are writing to present an overview of our model, emphasizing our utilization of historical data to refine the model’s parameters and overall effectiveness. This model is crafted to simulate the fluctuations in the Great Lakes water levels, incorporating the hydrodynamic relations within the lake chain and the impact of external variables.

<!-- b000491 | prose | pages [24] -->
To fortify the model’s reliability and precision, we have harnessed an extensive collection of historical data. This includes hydrologic information, such as historical records of water level variations and the data of river flow. We also examined the temporal relationship between the water level fluctuations in lakes and rivers to fine- tune the model’s representation of the hysteresis effect of lakes on rivers.

<!-- b000492 | prose | pages [24] -->
Additionally, we utilized meteorological data, including precipitation and evapo- ration across the Great Lakes, to accurately model external influences such as evapo- 微信号：MATHmodels ration and rainfall. Detailed topographic data of the lake basin were integrated to en- hance the hydrodynamic equations within the model. We also considered the depth, width, and length of connecting river channels to refine our understanding of lake inflow and outflow capacities and the associated flow friction losses. Moreover, the seasonal melting snow contributions to the lakes were considered, capturing the sea- sonal runoff variations effectively.

<!-- b000493 | prose | pages [24] -->
Our model features a determination of the optimal water level on a monthly basis, balancing considerations such as resident safety, hydro-power revenue, navigation, ecological impacts, and overall resident satisfaction. This serves as a guideline for our control mechanisms. The model boasts sophisticated equations for internal flows, considering the lake basin’s topography, the frictional flow costs, lake sizes, and the hysteresis effect of the lake basin’s geomorphology. External influences such as runoff, evaporation, and precipitation have been meticulously modeled, with optimizations drawn from historical data insights.

<!-- b000494 | prose | pages [24] -->
For control strategies, a prediction module is used to forecast water level within the observed time domain, continuously updating model parameters through optimiza- tion. This bolsters the controller model’s robustness. Our control strategy includes adaptive controller modes for dams, which is designed to respond to environmental fluctuations and extreme conditions efficiently. It ensures safety across the lake system.

<!-- b000495 | prose | pages [24] -->
In conclusion, our lake system model integrates historical data comprehensively, offering a precise depiction of the dynamic interplay in the lake chain. We are confi- dent that our methodology will provide valuable perspectives for the IJC, fostering the ongoing enhancement of lake system management.

<!-- b000496 | prose | pages [24] -->
We anticipate the opportunity to delve deeper into our model with you and address any inquiries or concerns you might have.

<!-- b000497 | prose | pages [24] -->
Yours Sincerely,

<!-- b000498 | furniture | pages [24] -->
Team #2417831

<!-- b000499 | prose | pages [24] -->
关注数学模型

<!-- b000500 | furniture | pages [24] -->
2

<!-- b000501 | furniture | pages [24] -->
MATHmodels

<!-- b000502 | furniture | pages [24] -->
获取更多资讯

<!-- b000503 | furniture | pages [25] -->
Team # 2417831

<!-- b000504 | furniture | pages [25] -->
Page 25 of 25

<!-- b000505 | heading | pages [25] -->
References

<!-- b000506 | references | pages [25] -->
[1] https://en.wikipedia.org/wiki/Lake_Superior

<!-- b000507 | references | pages [25] -->
微信公众号：数学模型

<!-- b000508 | references | pages [25] -->
[2] https://glisaclimate.org/media/GLISA_Lake_Evaporation.pdf

<!-- b000509 | references | pages [25] -->
[3] https://www.fs.usda.gov/ccrc/topics/regional-example-western-great-lakes

<!-- b000510 | references | pages [25] -->
[4] https://en.wikipedia.org/wiki/Moses-Saunders_Power_Dam

<!-- b000511 | references | pages [25] -->
[5] https://en.wikipedia.org/wiki/Robert_Moses_Niagara_Power_Plant

<!-- b000512 | references | pages [25] -->
[6] https://en.wikipedia.org/wiki/Moses-Saunders_Power_Dam

<!-- b000513 | references | pages [25] -->
[7] https://en.wikipedia.org/wiki/Saint_Marys_Falls_Hydropower_Plant

<!-- b000514 | references | pages [25] -->
[8] https://greatlakes-seaway.com/en/the-seaway/facts-figures/tonnage/

<!-- b000515 | references | pages [25] -->
微信号：MATHmodels

<!-- b000516 | references | pages [25] -->
[9] Lake Ontario-St.Lawrence River Plan 2014, https://ijc.org/sites/default/files/IJC_

<!-- b000517 | references | pages [25] -->
LOSR_EN_Web.pdf

<!-- b000518 | references | pages [25] -->
[10] Myers, D. T., Ficklin, D. L., and Robeson, S. M.: Hydrologic implications of pro-

<!-- b000519 | references | pages [25] -->
jected changes in rain-on-snow melt for Great Lakes Basin watersheds, Hydrol.

<!-- b000520 | references | pages [25] -->
Earth Syst. Sci., 27, 1755–1770, https://doi.org/10.5194/hess-27-1755-2023, 2023.

<!-- b000521 | references | pages [25] -->
关注数学模型

<!-- b000522 | furniture | pages [25] -->
2

<!-- b000523 | furniture | pages [25] -->
MATHmodels

<!-- b000524 | furniture | pages [25] -->
获取更多资讯
