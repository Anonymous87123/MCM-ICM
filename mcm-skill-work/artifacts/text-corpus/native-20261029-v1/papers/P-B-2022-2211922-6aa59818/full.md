# P-B-2022-2211922-6aa59818

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2021

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
B

<!-- b000006 | title | pages [1] -->
2211922

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
Reservoir Management: The Art of Proper Allocation

<!-- b000009 | prose | pages [1] -->
People have long used dams to store water to facilitate their lives. Reservoirs not only provide people with water for production and living, but also make contributions to hydropower generation. In recent days, the hot and dry weather with little rainfalls strongly affects the water level in reservoirs. The passage mainly solves the problem encountered in the 2 dams – the Glen Canyon dam and the Hoover dam along the Colorado River. By studying their water level and suggest operations, the passage gets some results that can finally facilitate people’s lives, and can ensure their basic demand by arranging the water scheduling operations in the reservoirs rationally.

<!-- b000010 | prose | pages [1] -->
For the first task, a "Double-Dam" system is abtracted, then we build a difference equation model to simulate the water flows inside and outside from the system and an optimization model that fits the demand well. Firstly, we collect relevant data in terms of agriculture, industry, population and electricity utility respectively, then convert the data into the demand for water, which can better relate to the water volume of the two dams. Then, two sequences respectively represent the water level of the two dams in the model play important parts in the indication that how long will the supply miss the demand. The model subtly simulates the water flows between the "Double-Dam" system and external environment, and the relationship of the two dams can be incorporated as well.

<!-- b000011 | prose | pages [1] -->
The result shows that under given condition, the water should be drawn from Lake Powell is about

<!-- b000012 | heading | pages [1] -->
430 million m3, and 225 million m3 drawn from Lake Mead (on average). If the additional water only

<!-- b000013 | prose | pages [1] -->
comes from the upstream, after 61 days, the demand and the lower bound of electricity generation would no longer meet. To deal with such a problem, about 40.7 million m3 is needed daily to guarantee the need. Besides, the result also shows that there exists periodic fluctuation of the water storage volume in the reservoirs with a macro downtrend. Therefore, the model should re-run every 100 days according to such a period.

<!-- b000014 | prose | pages [1] -->
For the second task, in order to deal with the competitive relationship of electricity production, a multi-objective model is built and the genetic algorithm is used to find the best allocation plan for general usage and power production. As an extension of the model in Task 1, the algorithm helps find the best distribution ratio in the five states. The result shows that California is allocated the most water sources, with a proportion for nearly 50%. Besides, the proportion of water for electricity generation in California and Arizona states is slightly more than that for general usage, and the situation is opposite in the rest three states.

<!-- b000015 | prose | pages [1] -->
The third task asks for solutions when reservoir resources are scarce. When the water really cannot meet the demand, the distribution method is changed by evaluating the importance of the 5 states in each aspect. Using the principal component analysis (PCA) method, we evaluate the importance of the 5 states in each aspect, then rearrange the proportion for each state and each usage. California takes up the majority of water usage since its advanced development. In terms of the usage, electricity production takes up for slightly over 50%.

<!-- b000016 | prose | pages [1] -->
Finally, sensitivity analysis is performed. The model output is analyzed by adjusting parameters of water volume, taking measures on water-saving, development in renewable energy technologies, growth and shrinkage on population, agriculture scale, industry and power generation, and finally the suppliment of the water inflows from upstream. The model is robust and self-adjustable according to the results. The concrete information is shown in Section 7.

<!-- b000017 | keywords | pages [1] -->
Key words: "Double-Dam" System, Management, Difference Equation Model, Optimization Model,

<!-- b000018 | prose | pages [1] -->
Multi-objective Programming, Genetic Algorithm, Principal Component Analysis

<!-- b000019 | furniture | pages [2] -->
Team 2211922

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1

<!-- b000022 | heading | pages [2] -->
Introduction

<!-- b000023 | furniture | pages [2] -->
Page 1

<!-- b000024 | prose | pages [2] -->
2 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000025 | prose | pages [2] -->
2

<!-- b000026 | heading | pages [2] -->
Assumptions and Explanations

<!-- b000027 | prose | pages [2] -->
3

<!-- b000028 | heading | pages [2] -->
Abbreviations and Symbol Notations

<!-- b000029 | prose | pages [2] -->
3

<!-- b000030 | prose | pages [2] -->
3

<!-- b000031 | prose | pages [2] -->
4

<!-- b000032 | prose | pages [2] -->
Arrangements and Changes of Water Supply and Demand 4 5 Overview: The Data for Each Aspect . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 5 Analysis: The "In and Out" of Water in the Reservoirs . . . . . . . . . . . . . . . . . . 4.2 7 Construction: The Double-Dam System . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 7 Result: The Allocation and Changes . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 9

<!-- b000033 | prose | pages [2] -->
Balance of Water Distribution for Two Opposite Usages 5 10 Analyzing – The Distribution for Different Utilities . . . . . . . . . . . . . . . . . . . 5.1 10 Extending – The Distribution Model Based on the Double-Dam System . . . . . . . . 5.2 11 Solving – The Arrangement for Competitive Demands 5.3 . . . . . . . . . . . . . . . . .

<!-- b000034 | prose | pages [2] -->
12 The Genetic Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.1 12 The Model Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.2

<!-- b000035 | prose | pages [2] -->
6 Thoughts on Water Shortage in Reservoirs

<!-- b000036 | prose | pages [2] -->
14

<!-- b000037 | prose | pages [2] -->
14 Method Development: The Proper Distribution with Focuses . . . . . . . . . . . . . . 6.1 14 The Evaluation of the Importance for Each State . . . . . . . . . . . . . . . . . . . . . 6.2 14 Result Statement: The Actual Distribution of Water . . . . . . . . . . . . . . . . . . . 6.3 16

<!-- b000038 | heading | pages [2] -->
Sensitivity and Robustness Analysis of the Model

<!-- b000039 | prose | pages [2] -->
7

<!-- b000040 | prose | pages [2] -->
8

<!-- b000041 | heading | pages [2] -->
Model Advantages and Drawbacks

<!-- b000042 | prose | pages [2] -->
16

<!-- b000043 | prose | pages [2] -->
18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Advantages 18 Drawbacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000044 | prose | pages [2] -->
9

<!-- b000045 | heading | pages [2] -->
Appendix

<!-- b000046 | prose | pages [2] -->
18

<!-- b000047 | prose | pages [2] -->
21 References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 21 The Method of Solving the Water Volume Changes . . . . . . . . . . . . . . . . . . . 9.2 21 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3 Part of Data and Results 22 Data in Section 4.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3.1 22 The result in Task 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3.2 22 The result in Task 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.3.3 22 Code for the Optimization Function of Task 1 . . . . . . . . . . . . . . . . . . . . . . 9.4 22 Code of the Genetic Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.5 23

<!-- b000048 | furniture | pages [3] -->
Team 2211922

<!-- b000049 | furniture | pages [3] -->
Page 2

<!-- b000050 | prose | pages [3] -->
1

<!-- b000051 | heading | pages [3] -->
Introduction

<!-- b000052 | prose | pages [3] -->
1.1 Problem Background

<!-- b000053 | prose | pages [3] -->
Humans have been using water for a long time to facilitate their lives. There is no doubt that dams are one of the most general water conservancy infrastructures throughout the world. By intercepting rivers and forming reservoirs, dams can not only be used to prevent floods, provide water for production and domestic use, but more importantly, can also be used to generate electricity, which can give support for people’s daily life in surrounding districts.

<!-- b000054 | prose | pages [3] -->
Along the Colorado River in the western part of the United States, there are two famous dams that cross it. They are the Glen Canyon dam and the Hoover dam. The Glen Canyon dam plays a crucial role in storing the water resources and providing the need in surrounding communities since the dam is located in the arid southwestern region. The Hoover dam, built in 1936, also plays an important rule in flood prevention, irrigation, power generation, shipping and water supply.

<!-- b000055 | caption | pages [3] -->
Figure 1: The Glen Canyon Dam (left) and the Hoover Dam (right), from Microsoft Bing

<!-- b000056 | prose | pages [3] -->
However, as the climate change evolves, water storage in these dams is decreasing. The reduction of the water volume of these dams will not only affect the water demand for production and living, but simultaneously, will also affect the electricity generation, so that the comprehensive benefit of the dams will gradually decline. Therefore, in order to help the 5 states – Arizona (AZ), California (CA), Wyoming (WY), New Mexico (NM) and Colorado (CO) better use the water resource which derives from the Glen Canyon dam and the Hoover dam, a proper water distribution plan is badly required.

<!-- b000057 | prose | pages [3] -->
1.2

<!-- b000058 | heading | pages [3] -->
Problem Restatement

<!-- b000059 | prose | pages [3] -->
For the requirements given, we restate them to help better position the focus of our work.

<!-- b000060 | prose | pages [3] -->
• Assume that the water level in Lake Mead is 𝑀, and in Lake Powell is 𝑃, and part of water inflows to Lake Mead from Lake Powell. Task 1 firstly asks for the arrangement of water drawn from each lake to meet the demands. Then, it is also required to estimate how long it will take until the demands are not met under the circumstance that no additional water is supplied and the demand is fixed. After

<!-- b000061 | furniture | pages [4] -->
Team 2211922

<!-- b000062 | furniture | pages [4] -->
Page 3

<!-- b000063 | prose | pages [4] -->
that, it is required to make discussions on the supply amount of additional water under the condition formerly mentioned with the interests of Mexico incorporated. Finally, it would be advisible to address how long should the model to re-run to adapt to changes of condition.

<!-- b000064 | prose | pages [4] -->
• Since there exists a competing relationship between general usage and electricity production of water in the reservoirs, Task 2 demands to come up with the best means to balance the different utilities of water and state the criteria in an explicit way. Note that there exists a lower bound for electricity generation.

<!-- b000065 | prose | pages [4] -->
• Task 3 requires to suggest approaches to tackle with the shortage of water which cannot meet all the demands of electricity production and general usages (including agricultural, industrial and residential usages).

<!-- b000066 | prose | pages [4] -->
• Finally, a sensitivity analysis is required to perfom. When fluctuations of usage of water in agriculture, industry and population, and the changes in the electricity use appear, the response of the model should be revealed.

<!-- b000067 | prose | pages [4] -->
1.3 Our Work

<!-- b000068 | prose | pages [4] -->
Based on the restatement of requirements, our work can be concluded as follows:

<!-- b000069 | prose | pages [4] -->
(1) Analyze the demand of water in 5 states – AZ, CA, WY, NM and CO. Then build a difference equation model and a optimization model for water distribution of reservoirs that not only meets various demands (ariculture, industry, resident and electricity generation) but also takes the water level of 2 dams into account. Except that, analyze the supply and demand when additional water resources are scarce according to the detailed condition given by Task 1 The water that outflows to Mexico should also be addressed.

<!-- b000070 | prose | pages [4] -->
(2) Suggest a multi-objective programming model to balance the usage of water for general approach and electricity production, since they have competitive interests.

<!-- b000071 | prose | pages [4] -->
(3) Based on the demand for each state in each usage, reallocate the water distribution by evaluating the importance of them using principal component analysis (PCA) method.

<!-- b000072 | heading | pages [4] -->
(4) Make sensitivity analysis when parameters like population, agricultural and industrial grows

<!-- b000073 | prose | pages [4] -->
or shrinks. Moreover, the impact of increased use of renewable energy and water & electricity saving measures on the model output also needs to be taken into consideration.

<!-- b000074 | prose | pages [4] -->
The flow chart of our work is presented by Figure 2.

<!-- b000075 | prose | pages [4] -->
2

<!-- b000076 | heading | pages [4] -->
Assumptions and Explanations

<!-- b000077 | prose | pages [4] -->
In actual practice, there are many complicated conditions that may affect the output of the model. In order to make model more stable and less complex, the following assumptions and their explanations are incorporated.

<!-- b000078 | prose | pages [4] -->
• The water level of the reservoir is proportional to the water volume. Since the dams are built according to the terrain, the relationship between the actual water level and water volume is difficult to analyze. Therefore, this assumption is aiming to simplify the problem.

<!-- b000079 | prose | pages [4] -->
• The inflow of water from upstream remains unchanged within a short period of time. In actual, the water inflows from upstream may vary over time. However, to better abstract the model, we assume the inflow amount is relatively fixed.

<!-- b000080 | furniture | pages [5] -->
Team 2211922

<!-- b000081 | furniture | pages [5] -->
Page 4

<!-- b000082 | prose | pages [5] -->
Simulation

<!-- b000083 | prose | pages [5] -->
Difference Equation

<!-- b000084 | prose | pages [5] -->
for

<!-- b000085 | prose | pages [5] -->
Model

<!-- b000086 | prose | pages [5] -->
𝑈𝐸𝛿1,𝛿1∗. 𝑈𝐺𝛿2,𝛿2∗ Single Objective Programming

<!-- b000087 | prose | pages [5] -->
Storage of Dam

<!-- b000088 | prose | pages [5] -->
The daily moisture content

<!-- b000089 | prose | pages [5] -->
The daily moisture content

<!-- b000090 | prose | pages [5] -->
of

<!-- b000091 | prose | pages [5] -->
of

<!-- b000092 | prose | pages [5] -->
Glen Canyon 𝒂𝒏

<!-- b000093 | prose | pages [5] -->
Hoover 𝒃𝒏

<!-- b000094 | prose | pages [5] -->
𝑉𝑜𝑙𝑢𝑚𝑒

<!-- b000095 | prose | pages [5] -->
GA Algorithm 𝐹𝑖𝑡(𝑥) = 𝑓(𝑥) + 𝜁𝑝(∑𝐶𝑜𝑛𝑠𝑡𝑟𝑎𝑖𝑛𝑡)

<!-- b000096 | prose | pages [5] -->
Electricity Use

<!-- b000097 | prose | pages [5] -->
General Use

<!-- b000098 | prose | pages [5] -->
AZ

<!-- b000099 | prose | pages [5] -->
AZ

<!-- b000100 | prose | pages [5] -->
CA

<!-- b000101 | prose | pages [5] -->
CO CA

<!-- b000102 | prose | pages [5] -->
CO

<!-- b000103 | prose | pages [5] -->
Electricity Use The Period

<!-- b000104 | prose | pages [5] -->
of Water Addition

<!-- b000105 | prose | pages [5] -->
General

<!-- b000106 | prose | pages [5] -->
𝑇

<!-- b000107 | prose | pages [5] -->
Sensitivity

<!-- b000108 | prose | pages [5] -->
CA

<!-- b000109 | prose | pages [5] -->
and

<!-- b000110 | prose | pages [5] -->
E

<!-- b000111 | prose | pages [5] -->
Robustness Analysis

<!-- b000112 | prose | pages [5] -->
A

<!-- b000113 | prose | pages [5] -->
I

<!-- b000114 | prose | pages [5] -->
P

<!-- b000115 | prose | pages [5] -->
Use

<!-- b000116 | prose | pages [5] -->
WY

<!-- b000117 | prose | pages [5] -->
WY

<!-- b000118 | prose | pages [5] -->
NM

<!-- b000119 | prose | pages [5] -->
NM

<!-- b000120 | prose | pages [5] -->
AZ AZ NM CO WY

<!-- b000121 | prose | pages [5] -->
𝑏1 The distribution of each purpose

<!-- b000122 | prose | pages [5] -->
PCA

<!-- b000123 | prose | pages [5] -->
𝑏2 The distribution ratio of each state

<!-- b000124 | caption | pages [5] -->
Figure 2: The Flow Chart of Our Work

<!-- b000125 | prose | pages [5] -->
• The proportion of power generation usages of water is fixed to a constant in every state, so as other usages. In order to finely estimate the water distribution amount for each state, we assume that the water usage for every aspect is the same in different states.

<!-- b000126 | prose | pages [5] -->
• Rainfall is omitted to solve the model. Because the officials speculate that there will be no rainfall appear in the near future, so the solution of the model only take the inflows of water from upstream of Colorado river into consideration.

<!-- b000127 | heading | pages [5] -->
Abbreviations and Symbol Notations

<!-- b000128 | prose | pages [5] -->
3

<!-- b000129 | prose | pages [5] -->
In order to make fomula and equations more intuitive and to present our article in a concise manner, we use these abbreviations or notations to represent different entities.

<!-- b000130 | prose | pages [5] -->
Abbreviations Description 𝐷𝑔 Water demand for general usage 𝐷𝑒 Water demand for power generation 𝐷𝑎 Water demand for agriculture 𝐷𝑖 Water demand for power generation 𝐷𝑟 Water demand for daily life {𝑎𝑛} The water volume of the Glen Canyon Dam on n’th day after water shortage {𝑏𝑛} The water volume of the Hoover Dam on n’th day after water shortage

<!-- b000131 | furniture | pages [6] -->
Team 2211922

<!-- b000132 | prose | pages [6] -->
𝑈𝐴

<!-- b000133 | furniture | pages [6] -->
Page 5

<!-- b000134 | prose | pages [6] -->
Coordination level of water resource utilization 𝐹𝑖𝑡(𝑥) Fitness function in the genetic function A Water demand matrix 𝚺 Covariance matrix of A after standardization b The distribution ratio for each usage /each state

<!-- b000135 | prose | pages [6] -->
Arrangements and Changes of Water Supply and Demand 4

<!-- b000136 | prose | pages [6] -->
Overview: The Data for Each Aspect 4.1

<!-- b000137 | prose | pages [6] -->
In order to better define the demand for water, it is essentially important to get related data. Since there’re no direct data given, we get several data such as electricity consumption, cultivated land area, population and the number of laborers in the 5 states (the data source is attached in the Reference in Appendix 9.1).

<!-- b000138 | prose | pages [6] -->
• Electricity Generation: We collect data of the electricity consumption per capita in these 5 states from 1960 to 2019, by assuming that the usage of the electricity is generally increasing with time going by, we take the electricity consumption in 2019 as our target of analysis. Figure 3 gives an intuitive way to represent them by visualization.

<!-- b000139 | prose | pages [6] -->
The Electricity Consumption Per Capita in the 5 States

<!-- b000140 | prose | pages [6] -->
30000

<!-- b000141 | prose | pages [6] -->
Electricity Consumption: Kw·h

<!-- b000142 | prose | pages [6] -->
25000

<!-- b000143 | prose | pages [6] -->
20000

<!-- b000144 | prose | pages [6] -->
15000

<!-- b000145 | prose | pages [6] -->
10000

<!-- b000146 | prose | pages [6] -->
5000

<!-- b000147 | prose | pages [6] -->
0

<!-- b000148 | prose | pages [6] -->
AZ CA WY NM CO

<!-- b000149 | prose | pages [6] -->
States

<!-- b000150 | caption | pages [6] -->
Figure 3: The Electricity Consumption Per Capita in the 5 States

<!-- b000151 | prose | pages [6] -->
The usage of electricity is relevant to the amount of the hydropower generation. Since the hy- dropower takes up 6.98% of the total amount of the electricity usage in the U.S. annually, we regard the generation of hydroelectric power by the Glen Canyon dam and the Hoover dam takes up the same ratio in people’s daily use of power in the 5 states. We also get information from the Internet that about 3.67m3 of water can produce 1kW· h of power, therefore, the daily water demand of electricity

<!-- b000152 | furniture | pages [7] -->
Team 2211922

<!-- b000153 | prose | pages [7] -->
generation can be described as:

<!-- b000154 | prose | pages [7] -->
5  ∑︁

<!-- b000155 | prose | pages [7] -->
𝑃𝑜𝑝

<!-- b000156 | prose | pages [7] -->
𝐷𝑒= 𝐶𝑒×

<!-- b000157 | prose | pages [7] -->
𝑖=1

<!-- b000158 | furniture | pages [7] -->
Page 6

<!-- b000159 | prose | pages [7] -->
 

<!-- b000160 | prose | pages [7] -->
× 6.98% × 3.67 ÷ 365

<!-- b000161 | prose | pages [7] -->
Where 𝐷𝑒stands for the water demand for power generation, 𝐶𝑒represents the electricity consump- tion in the surrounding communities per capita, and 𝑃𝑜𝑝stands for the population of that state.

<!-- b000162 | prose | pages [7] -->
• General Usage of Water: For agriculture, industry and family usage of the water, we also collected relevant data. The visualization of this part of data is shown in Figure 4.

<!-- b000163 | prose | pages [7] -->
Area of Farm Land in the 5 States

<!-- b000164 | prose | pages [7] -->
42,000,000

<!-- b000165 | prose | pages [7] -->
32,000,000

<!-- b000166 | prose | pages [7] -->
Area: acres

<!-- b000167 | prose | pages [7] -->
22,000,000

<!-- b000168 | prose | pages [7] -->
12,000,000

<!-- b000169 | prose | pages [7] -->
2,000,000

<!-- b000170 | prose | pages [7] -->
AZ CA

<!-- b000171 | prose | pages [7] -->
-8,000,000

<!-- b000172 | prose | pages [7] -->
Number of Laborers in the 5 States

<!-- b000173 | prose | pages [7] -->
18000000

<!-- b000174 | prose | pages [7] -->
Number of Laborers

<!-- b000175 | prose | pages [7] -->
16000000 14000000 12000000 10000000 8000000 6000000 4000000 2000000 0

<!-- b000176 | prose | pages [7] -->
AZ CA WY NM CO

<!-- b000177 | prose | pages [7] -->
States

<!-- b000178 | prose | pages [7] -->
WY NM CO

<!-- b000179 | prose | pages [7] -->
States

<!-- b000180 | prose | pages [7] -->
Population in the 5 States

<!-- b000181 | prose | pages [7] -->
40000000

<!-- b000182 | prose | pages [7] -->
35000000

<!-- b000183 | prose | pages [7] -->
30000000

<!-- b000184 | prose | pages [7] -->
Population

<!-- b000185 | prose | pages [7] -->
25000000

<!-- b000186 | prose | pages [7] -->
20000000

<!-- b000187 | prose | pages [7] -->
15000000

<!-- b000188 | prose | pages [7] -->
10000000

<!-- b000189 | prose | pages [7] -->
5000000

<!-- b000190 | prose | pages [7] -->
0

<!-- b000191 | prose | pages [7] -->
AZ CA WY NM CO

<!-- b000192 | prose | pages [7] -->
States

<!-- b000193 | caption | pages [7] -->
Figure 4: The Condition of Agriculture, Industry and Population in the 5 States

<!-- b000194 | prose | pages [7] -->
With respect to agriculture, the area of farm land is collected (unit: acre). By assuming that the water in need for every farmland is fixed, we can easily estimate the water demand 𝐷𝑎for agricultural usage by mutiplying the farmland area 𝐶𝑎with the average demand for a unit area annually, which is 364.50m3/acre.

<!-- b000195 | prose | pages [7] -->
𝐷𝑎= 𝐶𝑎× 364.50 ÷ 365

<!-- b000196 | prose | pages [7] -->
For industry, we collect the number of laborers and project water expenses annually in each state. Through the calculation of these two data items and water tariff per unit, the water demand required by industry can be estimated as:

<!-- b000197 | prose | pages [7] -->
 ∑︁

<!-- b000198 | prose | pages [7] -->
𝐷𝑖= 𝐶𝑖×

<!-- b000199 | prose | pages [7] -->
𝑖=1

<!-- b000200 | prose | pages [7] -->
5 5

<!-- b000201 | prose | pages [7] -->


<!-- b000202 | prose | pages [7] -->
𝐿𝑏𝑠

<!-- b000203 | prose | pages [7] -->
÷ 𝐶𝑤÷ 365

<!-- b000204 | prose | pages [7] -->
Where 𝐷𝑖indicates the water demand for industry, 𝐶𝑖stands for the water expense in industry per capita annually, 𝐿𝑏𝑠is the number of laborers for a certain state, and 𝐶𝑤is the water tariff per unit. Relevant data is attached to the Appendix 9.3.1.

<!-- b000205 | prose | pages [7] -->
Finally for residential usage, we collect data from the Internet about the water consumption per capita, which is 0.54m3. By timing this item with the population, the water demand for families 𝐷𝑟

<!-- b000206 | furniture | pages [8] -->
Team 2211922

<!-- b000207 | prose | pages [8] -->
can be easily estimated as

<!-- b000208 | prose | pages [8] -->
 ∑︁

<!-- b000209 | prose | pages [8] -->
𝐷𝑟=

<!-- b000210 | prose | pages [8] -->
𝑖=1

<!-- b000211 | furniture | pages [8] -->
Page 7

<!-- b000212 | prose | pages [8] -->
5 5

<!-- b000213 | prose | pages [8] -->


<!-- b000214 | prose | pages [8] -->
𝑃𝑜𝑝

<!-- b000215 | prose | pages [8] -->
× 0.54

<!-- b000216 | prose | pages [8] -->
Add four demands together, the water demand 𝐷𝑔for general use can be calculated, which is:

<!-- b000217 | prose | pages [8] -->
𝐷𝑔= 𝐷𝑎+ 𝐷𝑖+ 𝐷𝑟

<!-- b000218 | prose | pages [8] -->
Analysis: The "In and Out" of Water in the Reservoirs 4.2

<!-- b000219 | prose | pages [8] -->
The Glen Canyon dam and the Hoover dam provide water and hydropower to surrounding states together. What’s more, part of the water in the Glen Canyon dam flows into the Hoover dam, making the two dams more closely linked. When the water level and the demand are fixed, how much water to draw from each dam is the problem.

<!-- b000220 | prose | pages [8] -->
For the Glen Canyon dam, it not only supplies water for general use and power generation, but part of water from it outflows into the Hoover dam. In contrast, the Hoover dam mainly support the general and power-generate usage and has no concern about the outflow. But in order to take the river environment and the interests of Mexico into consideration, apparently the water in the Hoover dam shouldn’t be totally drawn. The process of water flow in Colorado river between the 2 dams are described in the picture shown as Figure 5, which is the basis of the model.

<!-- b000221 | prose | pages [8] -->
The Glen Canyon Dam

<!-- b000222 | prose | pages [8] -->
General Use

<!-- b000223 | prose | pages [8] -->
The Hoover Dam

<!-- b000224 | prose | pages [8] -->
Power Generation

<!-- b000225 | caption | pages [8] -->
Figure 5: The Relationship between Two Dams (The arrows stand for water flows)

<!-- b000226 | prose | pages [8] -->
As no additional water is available but only comes from the upstream, the water in the reservoir gradually dwindles to the point where it cannot supply the demand. Besides, to ensure the generation of electricity, the lower bound of the water volume is calculated, which is about 19.4 billion.

<!-- b000227 | prose | pages [8] -->
Under such a condition, a rational estimation ought to be addressed, so that relevant departments can perform certain operations to fulfill the water volume to satisfy the demand. Moreover, an estimation of the additional water volume is also needed.

<!-- b000228 | prose | pages [8] -->
Construction: The Double-Dam System 4.3

<!-- b000229 | prose | pages [8] -->
Based on the analysis in Section 4.1, we build a difference equation model to simulate changes of the two dams, and a optimization model to offer suggestions to negotiators to help them better perform the water distribution process.

<!-- b000230 | furniture | pages [9] -->
Team 2211922

<!-- b000231 | furniture | pages [9] -->
Page 8

<!-- b000232 | prose | pages [9] -->
Firstly, we abstract the two dams into two nodes as a system. Since part of the water from the Glen Canyon dam flows along the Colorado River into the Hoover dam, we use a one-directional arrow between the two nodes to represent the flow of water. From the perspective of such a system, there is extra water inflows into it (only from upstreams of the river), and water should be drawn out of it. What’s more, there will be part of water left to go down to satisfy the need for other regions (e.g. for Mexico). The flowchart of the system with several parameters is shown in Figure 6.

<!-- b000233 | prose | pages [9] -->
𝑘13

<!-- b000234 | prose | pages [9] -->
𝑘14

<!-- b000235 | prose | pages [9] -->
𝐸𝑥𝑡𝑟𝑎 𝐷𝑎𝑚1

<!-- b000236 | prose | pages [9] -->
𝑎𝑛

<!-- b000237 | prose | pages [9] -->
𝑇𝑘13

<!-- b000238 | prose | pages [9] -->
𝑎𝑛

<!-- b000239 | prose | pages [9] -->
𝐹1

<!-- b000240 | prose | pages [9] -->
𝑏𝑛

<!-- b000241 | prose | pages [9] -->
𝑘23

<!-- b000242 | prose | pages [9] -->
Life  & Production

<!-- b000243 | prose | pages [9] -->
𝐹1

<!-- b000244 | prose | pages [9] -->
Electricity

<!-- b000245 | prose | pages [9] -->
𝐹2

<!-- b000246 | prose | pages [9] -->
𝑘23

<!-- b000247 | prose | pages [9] -->
𝑘24

<!-- b000248 | prose | pages [9] -->
𝐷𝑎𝑚2

<!-- b000249 | prose | pages [9] -->
Mexico

<!-- b000250 | prose | pages [9] -->
𝑏𝑛

<!-- b000251 | prose | pages [9] -->
𝑇𝑘14

<!-- b000252 | prose | pages [9] -->
𝑎𝑛

<!-- b000253 | prose | pages [9] -->
𝐹2

<!-- b000254 | prose | pages [9] -->
𝑏𝑛

<!-- b000255 | prose | pages [9] -->
𝑘24

<!-- b000256 | caption | pages [9] -->
Figure 6: The Double-Dam System and the Water Flows

<!-- b000257 | prose | pages [9] -->
There are several parameters in the diagram, 𝑎𝑛and 𝑏𝑛represents the water level (which is directly connected to the water volume) in the two dams in n’th day after additional water shortage under the assumption that 𝑎0 = 𝑉𝑝and 𝑏0 = 𝑉𝑚, 𝑉𝑝and 𝑉𝑚is proportional to the given water level 𝑃and 𝑀. The 𝐷𝑎𝑚1 stands for the Glen Canyon dam while the 𝐷𝑎𝑚2 stands for the Hoover dam. Specifically, parameters 𝑘𝑖𝑗are coefficients which is the ratio of water that outflows from its original dam. For the total outflows of the water, 2 major usages are seperated – the general use (agricultural, industrial and residential) which is represented by 𝐹1 and the power generation represented by 𝐹2.

<!-- b000258 | prose | pages [9] -->
When additional water shortage occurs, the volume will gradually shrink within a certain period of time. Therefore, the numbers of elements in the two sequences will change over time as 𝑛increases. So when the total water volume is too low to feed the demand, the 𝑛is the number of days that need to be solved. The {𝑎𝑛} and {𝑏𝑛} can be described as the difference equation below:

<!-- b000259 | prose | pages [9] -->
𝑎𝑛−𝑎𝑛−1 = −𝑘13𝑎𝑛−1 −𝑘14𝑎𝑛−1 + 𝑒

<!-- b000260 | prose | pages [9] -->
𝑏𝑛−𝑏𝑛−1 = 𝑘14𝑎𝑛−1 −𝑘23𝑏𝑛−1 −𝑘24𝑏𝑛−1 In the fomula above, the items in both sides of equation represent the increment of water volume in the dam. What’s more, 𝑒is the extra volume of water that inflows from upstream of the Colorado River, which is regarded as a constant within a certain period. Besides, {𝑎𝑛} and {𝑏𝑛} are internally correlated. The method of solving the general formula of {𝑎𝑛} and {𝑏𝑛} is attached to the Appendix in 9.2. We solve the equation and find the concrete form of {𝑎𝑛} and {𝑏𝑛} as:

<!-- b000261 | furniture | pages [10] -->
Team 2211922

<!-- b000262 | prose | pages [10] -->
𝑒

<!-- b000263 | prose | pages [10] -->
𝑎𝑛= (1 −𝑘13 −𝑘14)𝑛

<!-- b000264 | prose | pages [10] -->
𝑉𝑝− 𝑘13 + 𝑘14

<!-- b000265 | furniture | pages [10] -->
Page 9

<!-- b000266 | prose | pages [10] -->
𝑒

<!-- b000267 | prose | pages [10] -->
 

<!-- b000268 | prose | pages [10] -->
+ 𝑘13 + 𝑘14

<!-- b000269 | prose | pages [10] -->
𝑏𝑛= 𝑘14(1 −𝑘13 −𝑘14)[(1 −𝑘23 −𝑘24)𝑛−(1 −𝑘13 −𝑘14)𝑛]

<!-- b000270 | prose | pages [10] -->
𝑒

<!-- b000271 | prose | pages [10] -->


<!-- b000272 | prose | pages [10] -->


<!-- b000273 | prose | pages [10] -->
𝑉𝑝−

<!-- b000274 | prose | pages [10] -->
𝑘13 + 𝑘14 −𝑘23 −𝑘24

<!-- b000275 | prose | pages [10] -->
+ (1 −𝑘23 −𝑘24)𝑛h

<!-- b000276 | prose | pages [10] -->
𝑉𝑚−

<!-- b000277 | prose | pages [10] -->
𝑘13 + 𝑘14

<!-- b000278 | prose | pages [10] -->
𝑒𝑘14

<!-- b000279 | prose | pages [10] -->
𝑒𝑘14

<!-- b000280 | prose | pages [10] -->
i

<!-- b000281 | prose | pages [10] -->
+

<!-- b000282 | prose | pages [10] -->
(𝑘23 + 𝑘24)(𝑘13 + 𝑘14)

<!-- b000283 | prose | pages [10] -->
(𝑘23 + 𝑘24)(𝑘13 + 𝑘14)

<!-- b000284 | prose | pages [10] -->
In order to meet both the general demand and power generation demand, we construct the following optimization model to optimize the deployment of the water resource from the two dams:

<!-- b000285 | prose | pages [10] -->
𝐷𝑔−𝑎𝑛𝑘13 −𝑏𝑛𝑘23

<!-- b000286 | prose | pages [10] -->
𝑚𝑖𝑛 𝑘13,𝑘23

<!-- b000287 | furniture | pages [10] -->


<!-- b000288 | prose | pages [10] -->
𝑘14,𝑘24 |𝐷𝑒−𝑎𝑛𝑘14 −𝑏𝑛𝑘24| 𝑚𝑖𝑛

<!-- b000289 | prose | pages [10] -->
𝑠.𝑡. 𝐷𝑒+ 𝐷𝑔< 𝑉𝑚+ 𝑉𝑝

<!-- b000290 | prose | pages [10] -->
0 < 𝑘13 + 𝑘23 < 1 0 < 𝑘14 + 𝑘24 < 1

<!-- b000291 | prose | pages [10] -->
The 2 objective functions represent the absolute difference between the demand and the water usage for general use and electricity generation respectively. In practice, the water drawn from reservoirs should bestly fit the demand, or else the waste of water will occur. The objective functions above ensure the water drawn from the two dams generates a minimum amount of waste on the basis of meet the fundamental demands. In order to minimize the objective function, a few constraint conditions is added, which includes that the demand should less than the total volume of the two reservoirs, and the sum of nonnegative coefficients 𝑘13, 𝑘23 and 𝑘14, 𝑘24 be less than 1 to limit the extraction of water. The general term of {𝑎𝑛} and {𝑏𝑛} is used to optimize the objective function. The model perfectly abstracts the "in and out" water flow problem in the 2 dams.

<!-- b000292 | heading | pages [10] -->
Result: The Allocation and Changes

<!-- b000293 | prose | pages [10] -->
4.4

<!-- b000294 | prose | pages [10] -->
By defining the value of parameters according to previous data, we solve the water volume which should be extracted from each dam, the time interval between the occurence of additional water shortage and the shortage for demand, and the additional water volume that should be supplied.

<!-- b000295 | prose | pages [10] -->
When the water storage of the Glen Canyon dam is about 24.1 billion m3, and the storage of the Hoover dam is 25.6 billion m3 (which corresponds to a fixed set of 𝑃and 𝑀), the water that should be drawn from Lake Powell is about 430 million m3 while the water drawn from Lake Mead is about 225 million m3 (Unit: per day, on average). The concrete data is shown in the Appendix. Mention that since we consider the water inflows to Lake Mead from Lake Powell over time, the actual result may fluctuate according to the situation.

<!-- b000296 | prose | pages [10] -->
When the additional water is no longer available, the model shows that the water can supply the demand until the 61st day. Until then, additional water should be suppplied, with a relatively stable volume at 40.7 million m3 per day (about 2 trillion m3 within 61 days)

<!-- b000297 | furniture | pages [11] -->
Team 2211922

<!-- b000298 | furniture | pages [11] -->
Page 10

<!-- b000299 | prose | pages [11] -->
What’s more, a special pattern occurs along with the outcome of the result – the water storage shows a periodic rebound in the overall declining trend like the trend shown in Figure 7. This is based

<!-- b000300 | prose | pages [11] -->
𝑉𝑜𝑙𝑢𝑚𝑒

<!-- b000301 | prose | pages [11] -->
7.00E+08

<!-- b000302 | prose | pages [11] -->
6.00E+08

<!-- b000303 | prose | pages [11] -->
5.00E+08

<!-- b000304 | prose | pages [11] -->
4.00E+08

<!-- b000305 | prose | pages [11] -->
3.00E+08

<!-- b000306 | prose | pages [11] -->
2.00E+08

<!-- b000307 | prose | pages [11] -->
1.00E+08

<!-- b000308 | prose | pages [11] -->
0.00E+00

<!-- b000309 | prose | pages [11] -->
1 31 61 91 121 151

<!-- b000310 | prose | pages [11] -->
When the dam is in the recovery period (the diagram on the left), the in-time replenish- ment of water during this period can prevent the shortage of water for later periods. 𝑇

<!-- b000311 | prose | pages [11] -->
181 211 241 271 301 331 361

<!-- b000312 | prose | pages [11] -->
Sum of Water Supply Actual Demand Supplement Cycle

<!-- b000313 | caption | pages [11] -->
Figure 7: Result of the Periodic Decrease for Water Storage

<!-- b000314 | prose | pages [11] -->
on the assumption that the extra water inflows the double-dam system is a constant – the flow volume of the Colorado river, which coincides with the objective phenomenon that the system has the ability of self-regulation. Of course, in terms of the overall trend, the storage is always decreasing over time.

<!-- b000315 | prose | pages [11] -->
We also get from this pattern that the time in a phase is about 100 days (over 3 months). If the negotiators want to make the model more accurate, the parameters should be redefined and the model should re-run every 100 days. Certainly, if the additional water is supplied by water transfer projects or other policies, the restart of the model is also needed. Finally, since part of the water outflows from the Glen Canyon dam supply the input to the Hoover dam, about 150 million m3 of water should be operated to flow from the Glen Canyon dam to the Hoover dam.

<!-- b000316 | prose | pages [11] -->
Ultimately, in order to take the interests of Mexico into consideration, the rest of water volume should be at a proper level. In our model, this can be represented as 𝑏𝑛· 𝑘24 at most. That is because the water used for power generation of the Hoover dam outflows to the downstram, and there are some losses along the way.

<!-- b000317 | prose | pages [11] -->
Balance of Water Distribution for Two Opposite Usages 5

<!-- b000318 | prose | pages [11] -->
Analyzing – The Distribution for Different Utilities 5.1

<!-- b000319 | prose | pages [11] -->
The Glen Canyon dam and the Hoover dam provide the surrounding areas with water for production, However, with climate change, the water in the dam needs to living and electricity generation.

<!-- b000320 | furniture | pages [12] -->
Team 2211922

<!-- b000321 | furniture | pages [12] -->
Page 11

<!-- b000322 | prose | pages [12] -->
be distributed more rationally to make it most effective. The water in reservoirs, in general, can be seperated into 4 major utilities: agricultural, industrial, residential usage (we call it "general usage") and electricity generation. Therefore, rational allocation of water resources requires an fully understanding of how water in the dams affects these activities. The content of this part is described below.

<!-- b000323 | prose | pages [12] -->
Firstly, the water is mainly for general usage and electricity production. Besides, in the general usage, the water in the reservoir is also partially converted into electricity for agriculture, industry and families. Therefore, the effects of water in the reservoir on general and power generation usages are interrelated and can be intuitively presented using the diagram in Figure 8.

<!-- b000324 | prose | pages [12] -->
Water in the Reservoirs

<!-- b000325 | prose | pages [12] -->
Agriculture Industry Family

<!-- b000326 | prose | pages [12] -->
Electricity

<!-- b000327 | caption | pages [12] -->
Figure 8: The Utilities of Water in Reservoirs

<!-- b000328 | prose | pages [12] -->
The above analysis shows that ideal results can be produced as long as the water allocation process is clarified. What’s more, the demand of water for general usage and power generation are competitive. That is to say, when the usage of one demand increases, another usage will decrease correspondingly. Therefore, a rational plan should be established to balance them reasonably.

<!-- b000329 | heading | pages [12] -->
Extending – The Distribution Model Based on the Double-Dam System

<!-- b000330 | prose | pages [12] -->
5.2

<!-- b000331 | prose | pages [12] -->
We extend the model in Task 1 – study the distribution of water for the demand (𝐷𝑒and 𝐷𝑔), with the aim of using the water in a more proper and rational way.

<!-- b000332 | prose | pages [12] -->
For a fixed demand, 4 mainly usages can be seperated: agricultural, industrial, residential and power generation. The main conflicting parties for water allocation, in short, are power generation and other utilities which are called "general usage".

<!-- b000333 | prose | pages [12] -->
In order to combine the scheduling and actual use of water resources, coordination level of water resource utilization for utility A is defined in a functional manner as 𝑈𝐴(𝛿, 𝛿∗):

<!-- b000334 | prose | pages [12] -->
(

<!-- b000335 | prose | pages [12] -->
1

<!-- b000336 | prose | pages [12] -->
𝑈𝐴=

<!-- b000337 | prose | pages [12] -->
𝛿≥𝛿∗

<!-- b000338 | prose | pages [12] -->
𝑒𝑥𝑝[−(𝛿−𝛿∗)2/𝑆2

<!-- b000339 | prose | pages [12] -->
𝛿< 𝛿∗ 𝐴]

<!-- b000340 | furniture | pages [13] -->
Team 2211922

<!-- b000341 | furniture | pages [13] -->
Page 12

<!-- b000342 | prose | pages [13] -->
In the formula above, the parameter 𝛿stands for the ratio of water allocation for a certain usage, for instance, the ratio of water used for power generation. It can be calculated as

<!-- b000343 | prose | pages [13] -->
𝛿= 𝑢𝑠𝑒𝑓𝑜𝑟𝐴

<!-- b000344 | prose | pages [13] -->
𝑡𝑜𝑡𝑎𝑙𝑢𝑠𝑒 𝛿∗= 𝑑𝑒𝑚𝑎𝑛𝑑𝑓𝑜𝑟𝐴

<!-- b000345 | prose | pages [13] -->
𝑡𝑜𝑡𝑎𝑙𝑑𝑒𝑚𝑎𝑛𝑑

<!-- b000346 | prose | pages [13] -->
The constant 𝛿∗stands for the demand ratio. Besides, the 𝑆2

<!-- b000347 | prose | pages [13] -->
𝐴stands for the variance of the difference between the demand 𝐷𝑘and the supply of water 𝑥𝑘in this usage among different subregions in the district:

<!-- b000348 | prose | pages [13] -->
𝐴= 1

<!-- b000349 | prose | pages [13] -->
∑︁

<!-- b000350 | prose | pages [13] -->
𝑆2

<!-- b000351 | prose | pages [13] -->
𝑛

<!-- b000352 | prose | pages [13] -->
𝑛 𝑛

<!-- b000353 | prose | pages [13] -->
(𝐷𝑘−𝑥𝑘)2

<!-- b000354 | prose | pages [13] -->
𝑘=0 𝑘=0

<!-- b000355 | prose | pages [13] -->
The inequality 𝛿≥𝛿∗represents that when the allocation ratio is no less than the demand, the demand is well satisfied. Therefore, the coordination level can be defined to 1, which is the highest value. When 𝛿≤𝛿∗, which means the supply cannot meet the demand. Under such circumstance, the Gaussian Distribution function is used to represent the difference between them.

<!-- b000356 | prose | pages [13] -->
The main contradiction of the water distribution – the distribution for general and power generation, should firstly be considered. According to the definition of coordination level of water resource utilization above, for these two utilities, we define two functions: 𝑈𝐸(𝛿1, 𝛿∗

<!-- b000357 | prose | pages [13] -->
the electricity generation and 𝑈𝐺(𝛿2, 𝛿∗ 1) which is related to

<!-- b000358 | prose | pages [13] -->
2) represents for the general usage. To best coordinate the distribution of the water in the reservoir, 𝑈𝐸and 𝑈𝐺should both be maximized:

<!-- b000359 | prose | pages [13] -->
√︃

<!-- b000360 | prose | pages [13] -->
𝑚𝑎𝑥𝑓(𝑥) =

<!-- b000361 | prose | pages [13] -->
𝑈𝐸(𝛿1, 𝛿∗

<!-- b000362 | prose | pages [13] -->
1) · 𝑈𝐺(𝛿2, 𝛿∗ 2)

<!-- b000363 | prose | pages [13] -->
Solving – The Arrangement for Competitive Demands 5.3

<!-- b000364 | prose | pages [13] -->
5.3.1

<!-- b000365 | heading | pages [13] -->
The Genetic Algorithm

<!-- b000366 | prose | pages [13] -->
To solve such a problem, genetic algorithm is used. From the beginning, we define a vector x with 10 dimensions with 𝑥1 to 𝑥5 respectively represent the water demand for electricity generation for each state while 𝑥6 to 𝑥10 represent the demand for general usages.

<!-- b000367 | prose | pages [13] -->
Step 1 First, we initialize the number of population to 200, for each individual within the population, the formula below (which is called "mutation operator" later) can help initialize elements for each individual randomly:

<!-- b000368 | prose | pages [13] -->
𝑥𝑖= 𝑟𝑎𝑛𝑑𝑜𝑚(𝑙𝑏, 𝑢𝑏)

<!-- b000369 | prose | pages [13] -->
Where 𝑙𝑏is the predefined lower bound value and 𝑢𝑏is the upper bound value, which are restricted by the situation of the problem. The function 𝑟𝑎𝑛𝑑𝑜𝑚(𝑎, 𝑏) generates a random value in interval

<!-- b000370 | prose | pages [13] -->
[𝑎, 𝑏].

<!-- b000371 | prose | pages [13] -->
Step 2 On the basis of our objective function, we reconfigure it into the adaption function to judge the strengths and weaknesses of individuals. The adaption function can be defined as:

<!-- b000372 | prose | pages [13] -->
5 h ∑︁

<!-- b000373 | prose | pages [13] -->
10

<!-- b000374 | prose | pages [13] -->
i

<!-- b000375 | prose | pages [13] -->
∑︁

<!-- b000376 | prose | pages [13] -->
(𝐸𝑐𝑜𝑠𝑡𝑖−𝑥𝑖) +

<!-- b000377 | prose | pages [13] -->
𝐹𝑖𝑡(𝑥) = 𝑓(𝑥) + 𝜁𝑝

<!-- b000378 | prose | pages [13] -->
𝑖=1

<!-- b000379 | prose | pages [13] -->
(𝐺𝑐𝑜𝑠𝑡𝑖−𝑥𝑖)

<!-- b000380 | prose | pages [13] -->
𝑖=6

<!-- b000381 | prose | pages [13] -->
𝐸𝑐𝑜𝑠𝑡and 𝐺𝑐𝑜𝑠𝑡represent the demand for electricity generation and general usage in each state. The difference between the distributed water and the demand reflects the adaption level for a certain

<!-- b000382 | furniture | pages [14] -->
Team 2211922

<!-- b000383 | furniture | pages [14] -->
Page 13

<!-- b000384 | prose | pages [14] -->
individual. The penalty factor 𝜁𝑝decreases the function value when constraint is not satisfied, which makes it more accurate for evaluating the adaption level of that individual.

<!-- b000385 | prose | pages [14] -->
Step 3 Evaluate each initialized population individual by means of the adaptation function. Step 4 Use Roulette Selection Method to select individuals in random. That is, if the adaption level for each individual is 𝑎𝑘(𝑘= 1, 2, ..., 200), then for a certain individual, it’s probability to be chosen can be calculated as:

<!-- b000386 | prose | pages [14] -->
𝑃(𝑎𝑖) = 𝑎𝑖

<!-- b000387 | prose | pages [14] -->
𝑘=1 𝑎𝑘

<!-- b000388 | prose | pages [14] -->
Í200

<!-- b000389 | prose | pages [14] -->
Step 5 Define crossover and mutation operators to update the elements for individuals by imitating the cross-exchange and variation of genes in nature. In crossover operation, 2 individuals are randomly chosen as 𝑥1 and 𝑥2, and perform the operations presented in pseudocode below:

<!-- b000390 | prose | pages [14] -->
Crossover Operation r = random(0, 1); 𝑡𝑒𝑚𝑝1 = 𝑟𝑥1 + (1 −𝑟)𝑥2; 𝑡𝑒𝑚𝑝2 = 𝑟𝑥2 + (1 −𝑟)𝑥1; 𝑥1 = 𝑡𝑒𝑚𝑝1; 𝑥2 = 𝑡𝑒𝑚𝑝2;

<!-- b000391 | prose | pages [14] -->
Step 6 Select best individuals that can fit the situation well Step 7 Repeat from Step 4 to Step 6 several times, then get the individuals remain as the result.

<!-- b000392 | prose | pages [14] -->
AZ

<!-- b000393 | heading | pages [14] -->
Best Solutions

<!-- b000394 | prose | pages [14] -->
CO

<!-- b000395 | prose | pages [14] -->
Fit function with Roulette Wheel Selection

<!-- b000396 | prose | pages [14] -->
NM

<!-- b000397 | prose | pages [14] -->
Origin

<!-- b000398 | prose | pages [14] -->
AZ

<!-- b000399 | prose | pages [14] -->
Population

<!-- b000400 | prose | pages [14] -->
CO

<!-- b000401 | prose | pages [14] -->
CA

<!-- b000402 | prose | pages [14] -->
… …

<!-- b000403 | prose | pages [14] -->
WY NM

<!-- b000404 | prose | pages [14] -->
5

<!-- b000405 | prose | pages [14] -->
10

<!-- b000406 | prose | pages [14] -->
Origin Population

<!-- b000407 | prose | pages [14] -->
Roulette Wheel

<!-- b000408 | prose | pages [14] -->
…

<!-- b000409 | prose | pages [14] -->
EU

<!-- b000410 | prose | pages [14] -->
Solutions 𝑖

<!-- b000411 | prose | pages [14] -->
CA

<!-- b000412 | prose | pages [14] -->
GU

<!-- b000413 | prose | pages [14] -->
Solutions 𝑗

<!-- b000414 | prose | pages [14] -->
…

<!-- b000415 | prose | pages [14] -->
WY WY

<!-- b000416 | prose | pages [14] -->
Crossover Mutation

<!-- b000417 | prose | pages [14] -->
… …

<!-- b000418 | prose | pages [14] -->
…

<!-- b000419 | prose | pages [14] -->
…

<!-- b000420 | prose | pages [14] -->
…

<!-- b000421 | prose | pages [14] -->
…

<!-- b000422 | prose | pages [14] -->
…

<!-- b000423 | prose | pages [14] -->
…

<!-- b000424 | prose | pages [14] -->
Yes

<!-- b000425 | prose | pages [14] -->
GN<N ?

<!-- b000426 | prose | pages [14] -->
No

<!-- b000427 | prose | pages [14] -->
(𝐺𝑐𝑜𝑠𝑡𝑖−𝑥𝑖) )

<!-- b000428 | prose | pages [14] -->
𝐹𝑖𝑡(𝑥) = 𝑓(𝑥) + 𝜁𝑝( ෍

<!-- b000429 | prose | pages [14] -->
(𝐸𝑐𝑜𝑠𝑡𝑖−𝑥𝑖) + ෍

<!-- b000430 | prose | pages [14] -->
𝑖= 1

<!-- b000431 | prose | pages [14] -->
𝑖=6

<!-- b000432 | heading | pages [14] -->
Best Solutions

<!-- b000433 | caption | pages [14] -->
Figure 9: The Flow Chart of Genetic Algorithm

<!-- b000434 | prose | pages [14] -->
The code of implementing such an algorithm is attached to the Appendix 9.4.

<!-- b000435 | furniture | pages [15] -->
Team 2211922

<!-- b000436 | prose | pages [15] -->
5.3.2

<!-- b000437 | heading | pages [15] -->
The Model Result

<!-- b000438 | furniture | pages [15] -->
Page 14

<!-- b000439 | prose | pages [15] -->
The result solved by the model is shown in the Figure 10.

<!-- b000440 | prose | pages [15] -->
The Allocation of Water

<!-- b000441 | prose | pages [15] -->
Unit: million

<!-- b000442 | prose | pages [15] -->
100

<!-- b000443 | prose | pages [15] -->
90

<!-- b000444 | prose | pages [15] -->
80

<!-- b000445 | prose | pages [15] -->
70

<!-- b000446 | prose | pages [15] -->
60

<!-- b000447 | prose | pages [15] -->
50

<!-- b000448 | prose | pages [15] -->
40

<!-- b000449 | prose | pages [15] -->
30

<!-- b000450 | prose | pages [15] -->
20

<!-- b000451 | prose | pages [15] -->
10

<!-- b000452 | prose | pages [15] -->
0

<!-- b000453 | prose | pages [15] -->
California Arizona New Mexico Colorado Wyoming

<!-- b000454 | prose | pages [15] -->
Electricity Generation General Usage

<!-- b000455 | caption | pages [15] -->
Figure 10: The Allocation of Water for Each State

<!-- b000456 | prose | pages [15] -->
From the figure, California takes most of the water supply, and the water supply for general use in the New Mexico, Colorado and Wyoming States are relatively greater than the generation of electricity. This may result from the fact that California is relatively more developed than other states, and the source of electricity in California are mainly from hydropower than other powers. The concrete data is presented in the Appendix 9.3.2.

<!-- b000457 | prose | pages [15] -->
Thoughts on Water Shortage in Reservoirs 6

<!-- b000458 | prose | pages [15] -->
Method Development: The Proper Distribution with Focuses 6.1

<!-- b000459 | prose | pages [15] -->
When water shortage occurs, relevant personnel must change water operations from reservoirs in time to suit the current situation. Since the water tranfer projects can not be constructed within a short period of time to supply the need, and the water in the reservoirs cannot meet all the demands of the five states, a proper allocation plan with focuses is needed to ensure maximum economic benefits. That is to say, the water can be bestly utilized.

<!-- b000460 | prose | pages [15] -->
The Evaluation of the Importance for Each State 6.2

<!-- b000461 | prose | pages [15] -->
When the water shortage appears, it is advisible to reallocate the water with focuses according to the water demand in each aspects for the 5 states. The principal component analysis (PCA) method is used to evaluate the allocation ratio, and the allocation ratio can be used to reflect the importance for each state. The main steps are describe below.

<!-- b000462 | prose | pages [15] -->
• With respect to the 4 aspects descibed in section 4.1 for each state, we represent them in the table below, where 𝑥𝑖𝑗stands for the water demand of state 𝑗in aspect 𝑖

<!-- b000463 | furniture | pages [16] -->
Team 2211922

<!-- b000464 | prose | pages [16] -->
CA 𝑥11 Electricity 𝑥21 Agriculture 𝑥31 Industry 𝑥41 Daily Life

<!-- b000465 | furniture | pages [16] -->
Page 15

<!-- b000466 | prose | pages [16] -->
AZ NM CO WY 𝑥12 𝑥13 𝑥14 𝑥15 𝑥22 𝑥23 𝑥24 𝑥25 𝑥32 𝑥33 𝑥34 𝑥35 𝑥42 𝑥43 𝑥44 𝑥45

<!-- b000467 | prose | pages [16] -->
Therefore, we define a matrix to represent the table above as:

<!-- b000468 | prose | pages [16] -->
𝑖= 1, 2, 3, 4; 𝑗= 1, 2, 3, 4, 5 A4×5 = A(𝑥𝑖𝑗),

<!-- b000469 | prose | pages [16] -->
• Standardization: Firstly, solve the average and the sample variance for each row:

<!-- b000470 | prose | pages [16] -->
5

<!-- b000471 | prose | pages [16] -->
𝑥𝑖= 1

<!-- b000472 | prose | pages [16] -->
∑︁

<!-- b000473 | prose | pages [16] -->
𝑥𝑖𝑗,

<!-- b000474 | prose | pages [16] -->
5

<!-- b000475 | prose | pages [16] -->
𝑗=1

<!-- b000476 | prose | pages [16] -->
5

<!-- b000477 | prose | pages [16] -->
1

<!-- b000478 | prose | pages [16] -->
∑︁

<!-- b000479 | prose | pages [16] -->
𝑠2 𝑠2

<!-- b000480 | prose | pages [16] -->
(𝑥𝑖𝑗−𝑥𝑖)2

<!-- b000481 | prose | pages [16] -->
𝑖= 5 −1

<!-- b000482 | prose | pages [16] -->
𝑗=1

<!-- b000483 | prose | pages [16] -->
Then, standardize A and let the matrix after standardization to be A′, that is: A′4×5 = A′(𝑥′

<!-- b000484 | prose | pages [16] -->
each element in matrix A, there is:

<!-- b000485 | prose | pages [16] -->
𝑖𝑗). For

<!-- b000486 | prose | pages [16] -->
𝑖𝑗= 𝑥𝑖𝑗−𝑥𝑖

<!-- b000487 | prose | pages [16] -->
𝑥′

<!-- b000488 | prose | pages [16] -->
𝑠𝑖 • Represent A′ as (a1 a2 a3 a4 a5), and an is regarded as a column vector. Then solve the covariance matrix 𝚺of matrix A′ with respect to these column vectors.

<!-- b000489 | prose | pages [16] -->
𝚺= 𝐶𝑜𝑣(a1 a2 a3 a4 a5)

<!-- b000490 | prose | pages [16] -->
𝐶𝑜𝑣(a1, a2) 𝐶𝑜𝑣(a1, a1) 𝐶𝑜𝑣(a1, a5) · · · 𝐶𝑜𝑣(a2, a2) 𝐶𝑜𝑣(a2, a1)

<!-- b000491 | prose | pages [16] -->
©­­­­

<!-- b000492 | prose | pages [16] -->
...

<!-- b000493 | prose | pages [16] -->
=

<!-- b000494 | prose | pages [16] -->
𝐶𝑜𝑣(a2, a5) · · ·

<!-- b000495 | prose | pages [16] -->
ª®®®®

<!-- b000496 | prose | pages [16] -->
...

<!-- b000497 | prose | pages [16] -->
... ... 𝐶𝑜𝑣(a5, a2) 𝐶𝑜𝑣(a5, a1)

<!-- b000498 | prose | pages [16] -->
«

<!-- b000499 | prose | pages [16] -->
Where

<!-- b000500 | prose | pages [16] -->
𝐶𝑜𝑣(an, am) = 1

<!-- b000501 | prose | pages [16] -->
∑︁

<!-- b000502 | prose | pages [16] -->
4

<!-- b000503 | prose | pages [16] -->
𝑖=1

<!-- b000504 | prose | pages [16] -->
4

<!-- b000505 | prose | pages [16] -->
𝑥′𝑛= 1

<!-- b000506 | prose | pages [16] -->
∑︁

<!-- b000507 | prose | pages [16] -->
𝑥′

<!-- b000508 | prose | pages [16] -->
𝑖𝑛,

<!-- b000509 | prose | pages [16] -->
4

<!-- b000510 | prose | pages [16] -->
𝑖=1

<!-- b000511 | prose | pages [16] -->
𝐶𝑜𝑣(a5, a5) · · ·

<!-- b000512 | prose | pages [16] -->
¬

<!-- b000513 | prose | pages [16] -->
4 4

<!-- b000514 | prose | pages [16] -->
(𝑥′

<!-- b000515 | prose | pages [16] -->
𝑖𝑛−𝑥′𝑛)(𝑥′

<!-- b000516 | prose | pages [16] -->
𝑖𝑚−𝑥′𝑚)

<!-- b000517 | prose | pages [16] -->
.

<!-- b000518 | prose | pages [16] -->


<!-- b000519 | prose | pages [16] -->


<!-- b000520 | prose | pages [16] -->
4

<!-- b000521 | prose | pages [16] -->
𝑥′𝑚= 1

<!-- b000522 | prose | pages [16] -->
∑︁

<!-- b000523 | prose | pages [16] -->
𝑥′

<!-- b000524 | prose | pages [16] -->
𝑖𝑚

<!-- b000525 | prose | pages [16] -->
4

<!-- b000526 | prose | pages [16] -->
𝑖=1

<!-- b000527 | prose | pages [16] -->
• Find the 5 eigenvalues of the matrix 𝚺, select eigenvectors v with relatively larger eigenvalues than others.

<!-- b000528 | prose | pages [16] -->
• Let b = Av, then normalize every element of the column vector b. The element of b after normalization is the proportion ratio of the water distribution for each usage.

<!-- b000529 | prose | pages [16] -->
• Exchange the rows and columns of A, find the water distribution proportion for each state using the same approach.

<!-- b000530 | prose | pages [16] -->
• Multiple the total amount of water to the distribution ratio for each state, then time it by the ratio for a sepcific usage. Finally the concrete distribution amount of this usage in that state is solved.

<!-- b000531 | furniture | pages [17] -->
Team 2211922

<!-- b000532 | furniture | pages [17] -->
Page 16

<!-- b000533 | heading | pages [17] -->
Result Statement: The Actual Distribution of Water

<!-- b000534 | prose | pages [17] -->
6.3

<!-- b000535 | prose | pages [17] -->
The result shows that when the water shortage really occurs, the distribution plan should be rearranged. Most of the water supply is allocated to California with a ratio for more than 50% since its strength in almost every aspect including agriculture, industry, etc. While in terms of usages, about a half of the water is allocated to the generation of electricity. The charts are shown in Figure 11 to make intuitive visualizations, while the concrete data are attached to the Appendix.

<!-- b000536 | prose | pages [17] -->
Distribution Ratio of Water for Each Purpose Distribution Ratio of Water for Each State

<!-- b000537 | prose | pages [17] -->
Colorado 0.69%

<!-- b000538 | prose | pages [17] -->
13.31%

<!-- b000539 | caption | pages [17] -->
Figure 11: The Overview of the Result When Water Shortage Occurs

<!-- b000540 | prose | pages [17] -->
The concrete data is shown in the Appendix 9.3.3.

<!-- b000541 | heading | pages [17] -->
Sensitivity and Robustness Analysis of the Model

<!-- b000542 | prose | pages [17] -->
7

<!-- b000543 | prose | pages [17] -->
When fluctuations in the parameters occurs, for instance, the water demand for agriculture increases or decreases over time, what will happen to the output of the model is crucial in a large sense, which may result in direct changes in operation of the two dams. Therefore, sensitivity analysis is performed to evaluate the model.

<!-- b000544 | prose | pages [17] -->
Firstly, the satisfaction rate is defined to represent the satisfaction level of water ( 𝑆𝑢𝑝𝑝𝑙𝑦

<!-- b000545 | prose | pages [17] -->
𝐷𝑒𝑚𝑎𝑛𝑑) supply under a certain circumstance. From the upper left diagram of Figure 12, we can see that when the demand multiplies as shown in the horizontal axis, the water storage gradually decreases over time. However, the storage value will ultimately approach a constant. This phenomenon is originated from the constraint of the lower bound of water volume in the two dams. The result shows that the robustness of model can satisfy the expectation that it can not only meet the demand but can also function normally.

<!-- b000546 | prose | pages [17] -->
After that, the upper right diagram of Figure 12 shows the model output when water-saving measures are taken and the proportion of renewable technologies is increasing. We define the day 𝑛= 65, which indicates that the reservoir can no longer meet the demand. Under such a circumstance,

<!-- b000547 | furniture | pages [18] -->
Team 2211922

<!-- b000548 | prose | pages [18] -->
S Rate

<!-- b000549 | prose | pages [18] -->
Satisfaction Rate

<!-- b000550 | prose | pages [18] -->
1.21 1.2 1.19 1.18 1.17 1.16 1.15 1.14 1.13 1.12

<!-- b000551 | prose | pages [18] -->
Multiple

<!-- b000552 | prose | pages [18] -->
1.11

<!-- b000553 | prose | pages [18] -->
1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7

<!-- b000554 | prose | pages [18] -->
n = 15 n = 10 n = 5

<!-- b000555 | prose | pages [18] -->
Changes of Demands Accompanied with Growth

<!-- b000556 | prose | pages [18] -->
in Different Usages

<!-- b000557 | prose | pages [18] -->
Usage

<!-- b000558 | prose | pages [18] -->
3.00E+09

<!-- b000559 | prose | pages [18] -->
2.50E+09

<!-- b000560 | prose | pages [18] -->
2.00E+09

<!-- b000561 | prose | pages [18] -->
1.50E+09

<!-- b000562 | prose | pages [18] -->
1.00E+09

<!-- b000563 | prose | pages [18] -->
5.00E+08

<!-- b000564 | prose | pages [18] -->
Multiple

<!-- b000565 | prose | pages [18] -->
0.00E+00

<!-- b000566 | prose | pages [18] -->
1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7

<!-- b000567 | prose | pages [18] -->
Population Agriculture Electricity Industry

<!-- b000568 | furniture | pages [18] -->
Page 17

<!-- b000569 | prose | pages [18] -->
Gap

<!-- b000570 | prose | pages [18] -->
Demand and Distribution Gap

<!-- b000571 | prose | pages [18] -->
5.00E+08 0.00E+00

<!-- b000572 | prose | pages [18] -->
-5.00E+08 -1.00E+09 -1.50E+09 -2.00E+09 -2.50E+09

<!-- b000573 | prose | pages [18] -->
T

<!-- b000574 | prose | pages [18] -->
-3.00E+09

<!-- b000575 | prose | pages [18] -->
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

<!-- b000576 | prose | pages [18] -->
Normal Condition Water Saving = 0.8

<!-- b000577 | prose | pages [18] -->
New Energy Using = 0.8

<!-- b000578 | prose | pages [18] -->
Extra Increase

<!-- b000579 | prose | pages [18] -->
Usage

<!-- b000580 | prose | pages [18] -->
1.20E+09

<!-- b000581 | prose | pages [18] -->
1.00E+09

<!-- b000582 | prose | pages [18] -->
8.00E+08

<!-- b000583 | prose | pages [18] -->
6.00E+08

<!-- b000584 | prose | pages [18] -->
4.00E+08

<!-- b000585 | prose | pages [18] -->
2.00E+08

<!-- b000586 | prose | pages [18] -->
Multiple

<!-- b000587 | prose | pages [18] -->
0.00E+00

<!-- b000588 | prose | pages [18] -->
1 1.5 2 2.5 3 3.5 4 4.5 5

<!-- b000589 | prose | pages [18] -->
n = 30 n = 65 n = 85

<!-- b000590 | caption | pages [18] -->
Figure 12: The Result of Sensitivity Analysis

<!-- b000591 | prose | pages [18] -->
to take measures may offer help to the lack of supply. So we make the dams work for 20 days to see the results.

<!-- b000592 | prose | pages [18] -->
After water-saving measures are taken, the supply can meet 80% of demand (shown in red dotted line) for 11 days. Nonetheless, the result will sharply decrease in later days, so that the demand can not be well satisfied. Moreover, when renewable energy usage increases, similar situation also occurrs – the supply can meet about 80% for 11 days but decreases afterwards, but not as badly as the result of taking water-saving measures. The result also displays that the implementation of water makes little contribution to the increase of the water level in reservoirs

<!-- b000593 | prose | pages [18] -->
Then, the relationship between the growth and shrinkage of population, agriculture, industry and power generation and the water level is presented at the lower left diagram of the Figure. By increasing the demand for each aspect and raise the value through 7 times of the original ones, we can see that the electricity generation aspect has a maximum slope, and population aspect has a minimum one. In general, water demand for electricity generation should be firstly satisfied, then the industrial one, then agriculture. Fianlly, the influence on the water level in the dams brought by "ups and downs" of population is relatively small.

<!-- b000594 | prose | pages [18] -->
When we shift our target to the water inflows from the upstream, the result is shown in the lower right diagram of the Figure. Similarly to the first diagram, the 𝑛represents the extent of water shortage. When the water volume is sufficient, the allocation varies little because the current water volume can already meet the demand. But when the water is scarce in the reservoir, the allocation will gradually increase, and will approach the allocation amount ultimately, which shows that the model can adjuct itself when external conditions are proper.

<!-- b000595 | furniture | pages [19] -->
Team 2211922

<!-- b000596 | furniture | pages [19] -->
Page 18

<!-- b000597 | prose | pages [19] -->
8

<!-- b000598 | heading | pages [19] -->
Model Advantages and Drawbacks

<!-- b000599 | prose | pages [19] -->
Finally, to have a more comprehensive perspective of our model, we make conclusions about the advantages and drawbacks of it.

<!-- b000600 | prose | pages [19] -->
8.1 Advantages

<!-- b000601 | prose | pages [19] -->
The model based on the "Double-Dam" system well abstracts the operations of the Glen Canyon and the Hoover dams. And the difference equation model inside the system natually take the inflows and outflows of water to each whereabouts. What’s more, the original water level (water storage) of the two dams 𝑀and 𝑃is incorporated by 𝑎0 and 𝑏0. Therefore, the model comprehensively simulates the working process and for reservoir managers, it can be easier to make rapid decisions on relevant allocation changes. What’s more, the model can be easily calculated by programming, no complicated theorems or theories are used. Last, when rainfall comes, constants can be added to the difference model (see constants 𝐶and 𝐹in the Appendix 10.1) so that more complex situations can be fully embraced.

<!-- b000602 | prose | pages [19] -->
8.2 Drawbacks

<!-- b000603 | prose | pages [19] -->
Even though the model functions and simulates the situation well, there are a few drawbacks. At first, the approach the model uses may call for complicated calculation condition. Besides, the model cannot always fit the actual changes of situation. It should re-run for every 100 days routinely. Especially, when some new policies that can affect the water volume in reservoirs, the parameters in the model should be modified to fit the new situation.

<!-- b000604 | prose | pages [20] -->
Drought and Thirst

<!-- b000605 | furniture | pages [20] -->


<!-- b000606 | furniture | pages [20] -->


<!-- b000607 | furniture | pages [20] -->


<!-- b000608 | prose | pages [20] -->
February 2022

<!-- b000609 | furniture | pages [20] -->


<!-- b000610 | furniture | pages [20] -->


<!-- b000611 | prose | pages [20] -->
Should Dams Be Condemned?

<!-- b000612 | heading | pages [20] -->
—Discussion about the Colorado river dams

<!-- b000613 | prose | pages [20] -->
A

<!-- b000614 | prose | pages [20] -->
s the most important river in the southwestern part of the United States, the Colorado river offers various functions like po- wer generating, fishing, irrigating to satisfy surrounding dis- tricts. However, The Colorado River has been drying up in recent years. Most people believe that the reason why water level of the river is lowering is because the dams have drained too much water. Is that so? This article will answer such a question by taking the Glen Canyon dam and the Hoover dam as example.

<!-- b000615 | furniture | pages [20] -->


<!-- b000616 | prose | pages [20] -->
The Drying Colorado River Dams

<!-- b000617 | prose | pages [20] -->
should be cautiously extended.

<!-- b000618 | prose | pages [20] -->
tion of water can inevitably result

<!-- b000619 | prose | pages [20] -->
The Colorado River, with a total

<!-- b000620 | prose | pages [20] -->
Because this part of water can be

<!-- b000621 | prose | pages [20] -->
in the accelerated drying of rivers.

<!-- b000622 | prose | pages [20] -->
length of 1,450 miles, derives from

<!-- b000623 | prose | pages [20] -->
used to generate power.

<!-- b000624 | prose | pages [20] -->
Recently, researchers have built a

<!-- b000625 | prose | pages [20] -->
the North Central part of Colorado.

<!-- b000626 | prose | pages [20] -->
Occurrence of Water Shortage –

<!-- b000627 | prose | pages [20] -->
model to simulate the operation of

<!-- b000628 | prose | pages [20] -->
Two famous dams go across the

<!-- b000629 | prose | pages [20] -->
What Will Happen Exactly?

<!-- b000630 | prose | pages [20] -->
the two dams, called the “Double-

<!-- b000631 | prose | pages [20] -->
river – the Glen Canyon Dam and

<!-- b000632 | prose | pages [20] -->
The shortage of rainfalls and the

<!-- b000633 | prose | pages [20] -->
Dam System”. The system mainly

<!-- b000634 | prose | pages [20] -->
the Hoover Dam, both of whom

<!-- b000635 | prose | pages [20] -->
persistent high temperature doe-

<!-- b000636 | prose | pages [20] -->
analyzes the operation of the water

<!-- b000637 | prose | pages [20] -->
have a history for over 80 years.

<!-- b000638 | prose | pages [20] -->
sn’t seem like to change within a

<!-- b000639 | prose | pages [20] -->
extraction for power generation,

<!-- b000640 | prose | pages [20] -->
However, in recent years, the

<!-- b000641 | prose | pages [20] -->
short period of time. Thus, many

<!-- b000642 | prose | pages [20] -->
agriculture, industry and domestic

<!-- b000643 | prose | pages [20] -->
water in the dam shrinks so rapid

<!-- b000644 | prose | pages [20] -->
use.

<!-- b000645 | prose | pages [20] -->
that the basic demand can no

<!-- b000646 | prose | pages [20] -->
people in the southwestern part of the U.S. are concerned about their

<!-- b000647 | prose | pages [20] -->
When the water level of the dams

<!-- b000648 | prose | pages [20] -->
longer meet. Is the construction of

<!-- b000649 | prose | pages [20] -->
demand, which will no longer be

<!-- b000650 | prose | pages [20] -->
maintains normally, about 2.1% of

<!-- b000651 | prose | pages [20] -->
dams that to be condemned?

<!-- b000652 | prose | pages [20] -->
met if such weather continues. The

<!-- b000653 | prose | pages [20] -->
water should be drawn from Lake

<!-- b000654 | prose | pages [20] -->
Actually, proper distribution of

<!-- b000655 | prose | pages [20] -->
“Double-Dam” system.

<!-- b000656 | prose | pages [20] -->
Powell and nearly 1% of water

<!-- b000657 | prose | pages [20] -->
water plays an important role in

<!-- b000658 | prose | pages [20] -->
The researchers use the model to

<!-- b000659 | prose | pages [20] -->
should be drawn from Lake Mead.

<!-- b000660 | prose | pages [20] -->
the water conservation.

<!-- b000661 | prose | pages [20] -->
simulate the drought by assuming

<!-- b000662 | prose | pages [20] -->
Such an extraction calls for accurate

<!-- b000663 | prose | pages [20] -->
Dam Operations – The Secret of

<!-- b000664 | prose | pages [20] -->
that the additional water like rainfall

<!-- b000665 | prose | pages [20] -->
operation of reservoir staffs. For

<!-- b000666 | prose | pages [20] -->
Proper Distribution

<!-- b000667 | prose | pages [20] -->
and water transferred from other

<!-- b000668 | prose | pages [20] -->
them, the water outflows from Lake

<!-- b000669 | prose | pages [20] -->
Undoubtedly, too much extrac-

<!-- b000670 | prose | pages [20] -->
reservoirs is no longer available. The

<!-- b000671 | prose | pages [20] -->
Powell, which flows to Lake Mead,

<!-- b000672 | furniture | pages [20] -->


<!-- b000673 | furniture | pages [20] -->


<!-- b000674 | prose | pages [20] -->
model  indi-

<!-- b000675 | furniture | pages [20] -->


<!-- b000676 | furniture | pages [20] -->


<!-- b000677 | furniture | pages [20] -->


<!-- b000678 | furniture | pages [20] -->


<!-- b000679 | prose | pages [20] -->
cates  that

<!-- b000680 | prose | pages [20] -->
1

<!-- b000681 | prose | pages [21] -->
Drought and Thirst February 2022

<!-- b000682 | furniture | pages [21] -->


<!-- b000683 | furniture | pages [21] -->


<!-- b000684 | furniture | pages [21] -->


<!-- b000685 | prose | pages [21] -->
service communities of the two

<!-- b000686 | prose | pages [21] -->
after approximately 2 months, the

<!-- b000687 | prose | pages [21] -->
dams – the California, Arizona,

<!-- b000688 | prose | pages [21] -->
water supply will be inadequate.

<!-- b000689 | prose | pages [21] -->
New Mexico, Colorado and Wyo-

<!-- b000690 | prose | pages [21] -->
Moreover, the model also indi-

<!-- b000691 | prose | pages [21] -->
ming states, as their subject. As a

<!-- b000692 | prose | pages [21] -->
cates an interesting phenomenon:

<!-- b000693 | prose | pages [21] -->
result, the water should pre-

<!-- b000694 | prose | pages [21] -->
the water in the Glen Canyon dam

<!-- b000695 | prose | pages [21] -->
ferentially delivered to California,

<!-- b000696 | prose | pages [21] -->
and the Hoover dam periodically fluctuates (see in Figure), which is

<!-- b000697 | prose | pages [21] -->
whose economic development takes up a dominant place among 5

<!-- b000698 | prose | pages [21] -->
opposite to our common sense. The

<!-- b000699 | prose | pages [21] -->
states. In volume, over 60% of

<!-- b000700 | prose | pages [21] -->
periodic fluctuation may result

<!-- b000701 | prose | pages [21] -->
water should be drawn to Cali-

<!-- b000702 | prose | pages [21] -->
from the self-adjustment of the

<!-- b000703 | prose | pages [21] -->
Figure: The Periodic Fluctuation Schematic

<!-- b000704 | prose | pages [21] -->
fornia state according to the model.

<!-- b000705 | prose | pages [21] -->
reservoir based on the assumptions

<!-- b000706 | prose | pages [21] -->
With respect to utilities, the elec-

<!-- b000707 | prose | pages [21] -->
that there are a certain extra water

<!-- b000708 | prose | pages [21] -->
Should Dams Be Condemned?

<!-- b000709 | prose | pages [21] -->
tricity generation and other general

<!-- b000710 | prose | pages [21] -->
inflows from the upstream of the

<!-- b000711 | prose | pages [21] -->
Ostensibly, the construction of

<!-- b000712 | prose | pages [21] -->
usages both take up for about 50%,

<!-- b000713 | prose | pages [21] -->
Colorado River.

<!-- b000714 | prose | pages [21] -->
water dams does account for the

<!-- b000715 | prose | pages [21] -->
which indicates the importance of

<!-- b000716 | prose | pages [21] -->
Method to Tackle with Water

<!-- b000717 | prose | pages [21] -->
drying process of the Colorado

<!-- b000718 | prose | pages [21] -->
water in power generation.

<!-- b000719 | prose | pages [21] -->
Shortage – What Should We Do?

<!-- b000720 | prose | pages [21] -->
river in a way. However, in an ob-

<!-- b000721 | prose | pages [21] -->
Future Trends – What If Other

<!-- b000722 | prose | pages [21] -->
When the water shortage in

<!-- b000723 | prose | pages [21] -->
jective perspective, it is the climate

<!-- b000724 | prose | pages [21] -->
Measures Are Taken?

<!-- b000725 | prose | pages [21] -->
reservoirs happens, reservoir wor-

<!-- b000726 | prose | pages [21] -->
change that really needs to be con-

<!-- b000727 | prose | pages [21] -->
Nowadays, many environment-

<!-- b000728 | prose | pages [21] -->
kers should respond rapidly to

<!-- b000729 | prose | pages [21] -->
demned, rather than the cons-

<!-- b000730 | prose | pages [21] -->
tally-friendly measures or policies

<!-- b000731 | prose | pages [21] -->
deal with such a situation.

<!-- b000732 | prose | pages [21] -->
truction of reservoirs.

<!-- b000733 | prose | pages [21] -->
are taken. Such as power saving

<!-- b000734 | prose | pages [21] -->
The water is used mainly for

<!-- b000735 | prose | pages [21] -->
Therefore, to bring the water

<!-- b000736 | prose | pages [21] -->
policy, measures for developing

<!-- b000737 | prose | pages [21] -->
agriculture, industry, people’s dai- ly life and power generation. In a

<!-- b000738 | prose | pages [21] -->
new energies, etc.

<!-- b000739 | prose | pages [21] -->
level of Colorado River back up, not only the efforts of reservoir

<!-- b000740 | prose | pages [21] -->
With respect to the researcher’s

<!-- b000741 | prose | pages [21] -->
word, the utility of water is mostly

<!-- b000742 | prose | pages [21] -->
managers make sense. Actually, it

<!-- b000743 | prose | pages [21] -->
model, the result is rather negative

<!-- b000744 | prose | pages [21] -->
for economic growth. When shor-

<!-- b000745 | prose | pages [21] -->
is the efforts of the whole society to

<!-- b000746 | prose | pages [21] -->
– the predicted demand won’t in-

<!-- b000747 | prose | pages [21] -->
tage occurs, to ensure the normal

<!-- b000748 | prose | pages [21] -->
protect the environment.  ◼

<!-- b000749 | prose | pages [21] -->
crease significantly under these

<!-- b000750 | prose | pages [21] -->
function of the economics is of

<!-- b000751 | furniture | pages [21] -->


<!-- b000752 | prose | pages [21] -->
methods unless these measures are

<!-- b000753 | prose | pages [21] -->
essential importance. Based on this

<!-- b000754 | prose | pages [21] -->
(Editor: Team #2211922)

<!-- b000755 | prose | pages [21] -->
implemented with extreme force.

<!-- b000756 | prose | pages [21] -->
purpose, researchers take the main

<!-- b000757 | prose | pages [21] -->
2

<!-- b000758 | furniture | pages [21] -->


<!-- b000759 | furniture | pages [21] -->


<!-- b000760 | furniture | pages [22] -->
Team 2211922

<!-- b000761 | prose | pages [22] -->
9

<!-- b000762 | heading | pages [22] -->
Appendix

<!-- b000763 | prose | pages [22] -->
9.1

<!-- b000764 | heading | pages [22] -->
References

<!-- b000765 | furniture | pages [22] -->
Page 21

<!-- b000766 | references | pages [22] -->
[1] Manli H., Jian Z., Dafa D., et al. Research on the optimal allocation of regional water resources

<!-- b000767 | references | pages [22] -->
based on genetic algorithm [J]. People’s Yangtze River, 2008, 39(6):4.

<!-- b000768 | references | pages [22] -->
[2] SEDS, EIA, U.S. Energy Information Administration, https://www.eia.gov/

<!-- b000769 | references | pages [22] -->
[3] USDA National Agricultural Statistics Service Information, https://www.nass.usda.gov/

<!-- b000770 | references | pages [22] -->
[4] Data USA, https://datausa.io/

<!-- b000771 | references | pages [22] -->
[5] Xuemin. C. Glen Canyon Hydropower Station in the United States[J]. Water Conservancy and

<!-- b000772 | references | pages [22] -->
Hydropower Technology, 1960(3):59-60.

<!-- b000773 | references | pages [22] -->
L. The Hoover Dam in the United States [J].

<!-- b000774 | references | pages [22] -->
[6] Zhenghua.

<!-- b000775 | references | pages [22] -->
1999(10):46.

<!-- b000776 | references | pages [22] -->
Management and Management,

<!-- b000777 | references | pages [22] -->
The Method of Solving the Water Volume Changes

<!-- b000778 | references | pages [22] -->
9.2

<!-- b000779 | references | pages [22] -->
The original equations can be abstracted into the following problem:

<!-- b000780 | references | pages [22] -->
𝑎𝑛= 𝐴𝑎𝑛−1 + 𝐵𝑏𝑛−1 + 𝐶

<!-- b000781 | references | pages [22] -->
𝑏𝑛= 𝐷𝑎𝑛−1 + 𝐸𝑏𝑛−1 + 𝐹

<!-- b000782 | references | pages [22] -->
Objective: Given 𝑎0, 𝑏0 and 𝐴𝐸−𝐵𝐷≠0, and 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸≠0 Find the general formula of

<!-- b000783 | references | pages [22] -->
{𝑎𝑛} and {𝑏𝑛}.

<!-- b000784 | references | pages [22] -->
Homogenize the original equation

<!-- b000785 | references | pages [22] -->
𝐶𝐸−𝐵𝐹

<!-- b000786 | references | pages [22] -->


<!-- b000787 | references | pages [22] -->
𝑎𝑛+

<!-- b000788 | references | pages [22] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸= 𝐴

<!-- b000789 | references | pages [22] -->
𝑎𝑛−1 +

<!-- b000790 | references | pages [22] -->


<!-- b000791 | references | pages [22] -->
𝐶𝐸−𝐵𝐹

<!-- b000792 | references | pages [22] -->
𝑏𝑛−1 + 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹

<!-- b000793 | references | pages [22] -->


<!-- b000794 | references | pages [22] -->


<!-- b000795 | references | pages [22] -->


<!-- b000796 | references | pages [22] -->
+ 𝐵

<!-- b000797 | references | pages [22] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000798 | references | pages [22] -->
𝑏𝑛+ 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹

<!-- b000799 | references | pages [22] -->


<!-- b000800 | references | pages [22] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸= 𝐷

<!-- b000801 | references | pages [22] -->
𝑎𝑛−1 +

<!-- b000802 | references | pages [22] -->


<!-- b000803 | references | pages [22] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000804 | references | pages [22] -->
𝑏𝑛−1 + 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹

<!-- b000805 | references | pages [22] -->
𝐶𝐸−𝐵𝐹

<!-- b000806 | references | pages [22] -->


<!-- b000807 | references | pages [22] -->


<!-- b000808 | references | pages [22] -->


<!-- b000809 | references | pages [22] -->
+ 𝐸

<!-- b000810 | references | pages [22] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000811 | references | pages [22] -->
𝐶𝐸−𝐵𝐹

<!-- b000812 | references | pages [22] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000813 | references | pages [22] -->
𝐴𝐸−𝐵𝐷+𝐵−𝐸, 𝑦𝑛= 𝑏𝑛+ 𝐴𝐹−𝐶𝐷+𝐶−𝐹

<!-- b000814 | references | pages [22] -->
Let 𝑥𝑛= 𝑎𝑛+

<!-- b000815 | references | pages [22] -->
𝐴𝐸−𝐵𝐷+𝐵−𝐸, then

<!-- b000816 | references | pages [22] -->
 𝐴

<!-- b000817 | references | pages [22] -->
𝑥𝑛

<!-- b000818 | references | pages [22] -->
𝐵

<!-- b000819 | references | pages [22] -->
 𝑥𝑛−1

<!-- b000820 | references | pages [22] -->


<!-- b000821 | references | pages [22] -->
=

<!-- b000822 | references | pages [22] -->
𝑦𝑛

<!-- b000823 | references | pages [22] -->
𝐷

<!-- b000824 | references | pages [22] -->
𝐸

<!-- b000825 | references | pages [22] -->
𝑦𝑛−1

<!-- b000826 | references | pages [22] -->
 𝐴

<!-- b000827 | references | pages [22] -->
𝐵

<!-- b000828 | references | pages [22] -->


<!-- b000829 | references | pages [22] -->
Let M =

<!-- b000830 | references | pages [22] -->
 𝐴

<!-- b000831 | references | pages [22] -->
𝑛𝑥0

<!-- b000832 | references | pages [22] -->
𝐵

<!-- b000833 | references | pages [22] -->


<!-- b000834 | references | pages [22] -->


<!-- b000835 | references | pages [22] -->
= ... =

<!-- b000836 | references | pages [22] -->
𝐷

<!-- b000837 | references | pages [22] -->
𝐸

<!-- b000838 | references | pages [22] -->
𝑦0

<!-- b000839 | references | pages [22] -->
, then there exists an invertible matrix P, such that:

<!-- b000840 | references | pages [22] -->
𝐷

<!-- b000841 | references | pages [22] -->
𝐸

<!-- b000842 | references | pages [22] -->
𝛼

<!-- b000843 | references | pages [22] -->


<!-- b000844 | references | pages [22] -->
0

<!-- b000845 | references | pages [22] -->
𝑃−1𝑀𝑃=

<!-- b000846 | references | pages [22] -->
𝛽

<!-- b000847 | references | pages [22] -->
0

<!-- b000848 | references | pages [22] -->
 −𝐵

<!-- b000849 | references | pages [22] -->
𝐸−𝛽

<!-- b000850 | references | pages [22] -->


<!-- b000851 | references | pages [22] -->
Apparently, 𝛼and 𝛽are the 2 eigenvalues of M, and P =

<!-- b000852 | references | pages [22] -->
𝑛

<!-- b000853 | references | pages [22] -->
𝛼

<!-- b000854 | references | pages [22] -->
0

<!-- b000855 | references | pages [22] -->
M𝑛= 𝑃

<!-- b000856 | references | pages [22] -->
𝑃−1

<!-- b000857 | references | pages [22] -->
𝛽

<!-- b000858 | references | pages [22] -->
0

<!-- b000859 | references | pages [22] -->
, Therefore

<!-- b000860 | references | pages [22] -->
𝐴−𝛼

<!-- b000861 | references | pages [22] -->
−𝐷

<!-- b000862 | references | pages [22] -->
(𝐴−𝛼)(𝐸−𝛽)𝛽𝑛−𝐵𝐷𝛼𝑛

<!-- b000863 | references | pages [22] -->
1

<!-- b000864 | references | pages [22] -->
=

<!-- b000865 | references | pages [22] -->
(𝐸−𝛽)𝐵(𝛼𝑛−𝛽𝑛)

<!-- b000866 | references | pages [22] -->


<!-- b000867 | references | pages [22] -->
(𝐴−𝑎)𝐷(𝛼𝑛−𝛽𝑛)

<!-- b000868 | references | pages [22] -->
(𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷

<!-- b000869 | references | pages [22] -->
(𝐴−𝛼)(𝐸−𝛽)𝛼𝑛−𝐵𝐷𝛽𝑛

<!-- b000870 | furniture | pages [23] -->
Team 2211922

<!-- b000871 | furniture | pages [23] -->
Page 22

<!-- b000872 | references | pages [23] -->
Bring 𝑎𝑛and 𝑏𝑛back to the original fomula, we can get the general formula of {𝑎𝑛} and {𝑏𝑛}

<!-- b000873 | references | pages [23] -->
𝑎𝑛= (𝐴−𝛼)(𝐸−𝛽)𝛽𝑛−𝐵𝐷𝛼𝑛

<!-- b000874 | references | pages [23] -->


<!-- b000875 | references | pages [23] -->
𝑎0 +

<!-- b000876 | references | pages [23] -->
(𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷

<!-- b000877 | references | pages [23] -->
(𝐸−𝛽)𝐵(𝛼𝑛−𝛽𝑛)

<!-- b000878 | references | pages [23] -->
𝐶𝐸−𝐵𝐹

<!-- b000879 | references | pages [23] -->


<!-- b000880 | references | pages [23] -->
+

<!-- b000881 | references | pages [23] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000882 | references | pages [23] -->
𝑏0 + 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹

<!-- b000883 | references | pages [23] -->


<!-- b000884 | references | pages [23] -->
𝐶𝐸−𝐵𝐹

<!-- b000885 | references | pages [23] -->


<!-- b000886 | references | pages [23] -->
−

<!-- b000887 | references | pages [23] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000888 | references | pages [23] -->
(𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷

<!-- b000889 | references | pages [23] -->
(𝐴−𝛼)𝐷(𝛼𝑛−𝛽𝑛)

<!-- b000890 | references | pages [23] -->


<!-- b000891 | references | pages [23] -->
𝑏𝑛=

<!-- b000892 | references | pages [23] -->
𝑎0 +

<!-- b000893 | references | pages [23] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000894 | references | pages [23] -->
𝐶𝐸−𝐵𝐹

<!-- b000895 | references | pages [23] -->


<!-- b000896 | references | pages [23] -->
+

<!-- b000897 | references | pages [23] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000898 | references | pages [23] -->
(𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷

<!-- b000899 | references | pages [23] -->
(𝐴−𝛼)(𝐸−𝛽)𝛼𝑛−𝐵𝐷𝛽𝑛

<!-- b000900 | references | pages [23] -->
𝑏0 + 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹

<!-- b000901 | references | pages [23] -->


<!-- b000902 | references | pages [23] -->
(𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷

<!-- b000903 | references | pages [23] -->
9.3

<!-- b000904 | heading | pages [23] -->
Part of Data and Results

<!-- b000905 | prose | pages [23] -->
9.3.1 Data in Section 4.1

<!-- b000906 | prose | pages [23] -->
−𝐴𝐹−𝐶𝐷+ 𝐶−𝐹

<!-- b000907 | prose | pages [23] -->


<!-- b000908 | prose | pages [23] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000909 | prose | pages [23] -->
𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000910 | prose | pages [23] -->
𝐶𝑖: $56000

<!-- b000911 | prose | pages [23] -->
𝐶𝑤: $1.21/𝑚3

<!-- b000912 | prose | pages [23] -->
9.3.2

<!-- b000913 | heading | pages [23] -->
The result in Task 2

<!-- b000914 | prose | pages [23] -->
CA AZ NM CO WY 27379684 Electricity Generation 88255883 8757475 19895462 5885614 25959557 General Usage 85325544

<!-- b000915 | prose | pages [23] -->
9.3.3

<!-- b000916 | heading | pages [23] -->
The result in Task 3

<!-- b000917 | prose | pages [23] -->
23937562 27590832 15559389

<!-- b000918 | prose | pages [23] -->
The table below represents the water distribution ratio for each state in several aspects.

<!-- b000919 | prose | pages [23] -->
CA AZ NM CO WY 0.042054 Electricity 0.345354 0.068108 0.003527 0.052510 0.003905 Agriculture 0.032067 0.006324 0.000327 0.004876 0.030952 Industry 0.254182 0.050128 0.002596 0.038648 0.005298 Population 0.043506 0.008579 0.000444 0.006615

<!-- b000920 | prose | pages [23] -->
Code for the Optimization Function of Task 1 9.4

<!-- b000921 | prose | pages [23] -->
function f = fun1(x,n,A,B,P,M,C) 1

<!-- b000922 | prose | pages [23] -->
w1 = 0.5; 2

<!-- b000923 | prose | pages [23] -->
w2 = 1 - w1; 3

<!-- b000924 | prose | pages [23] -->
an = (P - C./( x(1)+x(2))) .* (1 - x(1) - x(2)).^n + C./(x(1)+x(2)); 4

<!-- b000925 | furniture | pages [24] -->
Team 2211922

<!-- b000926 | furniture | pages [24] -->
Page 23

<!-- b000927 | prose | pages [24] -->
bn = (x(2).*(1 - x(1) - x(2)).*( (1- x(3) -x(4) ).^n - (1 - x(1) - x(2)).^n 5

<!-- b000928 | prose | pages [24] -->
)).*(P - C./(x(1)+x(2)))./(x(1) + x(2) - x(3) -x(4)) + (M - (C.*x(2))./( (x(3)+x(4)).*(x(1) + x(2)) )).*(1 - x(3) -x(4) ).^n + (C.*x(2))./((x(3)+x(4)).*(x(1)+x(2)));

<!-- b000929 | prose | pages [24] -->
f1 = abs( A - (an.*x(1) + bn.* x(3)) ) ; 6

<!-- b000930 | prose | pages [24] -->
f2 = abs( B - (an.*x(2) + bn.* x(4)) ) ; 7

<!-- b000931 | prose | pages [24] -->
f = w1.*f1 + w2.*f2; 8

<!-- b000932 | prose | pages [24] -->
end 9

<!-- b000933 | prose | pages [24] -->
9.5

<!-- b000934 | heading | pages [24] -->
Code of the Genetic Algorithm

<!-- b000935 | prose | pages [24] -->
NP = 200; %% The number of the population which is an even number 1

<!-- b000936 | prose | pages [24] -->
L = 10; %% Length of genes 2

<!-- b000937 | prose | pages [24] -->
Pc = 0.8; %% Crossover probability: 0.25 ~ 1 3

<!-- b000938 | prose | pages [24] -->
Pm = 0.1; %% Mutation probability: 0.001 ~ -5.9 4

<!-- b000939 | prose | pages [24] -->
G = 1000; %% Inheritance index 5

<!-- b000940 | prose | pages [24] -->
Xs = ub .* 0.9; %% Upper bound of feasible solution 6

<!-- b000941 | prose | pages [24] -->
Xx = lb; %% Lower bound of feasible solution 7

<!-- b000942 | prose | pages [24] -->
f = randi([0,1],NP,L); %% Initialization 8

<!-- b000943 | prose | pages [24] -->
for i = 1:NP 9

<!-- b000944 | prose | pages [24] -->
for j = 1:10 10

<!-- b000945 | prose | pages [24] -->
f(i,j) = Xx(1,j) + (Xs(1,j) - Xx(1,j)).*rand; 11

<!-- b000946 | prose | pages [24] -->
end 12

<!-- b000947 | prose | pages [24] -->
end 13

<!-- b000948 | prose | pages [24] -->
for k = 1:G 14

<!-- b000949 | prose | pages [24] -->
for i = 1:NP 15

<!-- b000950 | prose | pages [24] -->
Fit(i) = fun1(f(i,1:10)); 16

<!-- b000951 | prose | pages [24] -->
end 17

<!-- b000952 | prose | pages [24] -->
maxFit = max(Fit); 18

<!-- b000953 | prose | pages [24] -->
minFit = min(Fit); 19

<!-- b000954 | prose | pages [24] -->
rr = find(Fit == maxFit); 20

<!-- b000955 | prose | pages [24] -->
fBest = f(rr(1,1),:); % Best gene type for each generation 21

<!-- b000956 | prose | pages [24] -->
Fit = (Fit - minFit)/(maxFit - minFit); 22

<!-- b000957 | prose | pages [24] -->
%%%%%The Copy Opration of the Roulette Selection Method%%%%% 23

<!-- b000958 | prose | pages [24] -->
sum_Fit = sum(Fit); 24

<!-- b000959 | prose | pages [24] -->
fitvalue = Fit./sum_Fit; 25

<!-- b000960 | prose | pages [24] -->
fitvalue = cumsum(fitvalue); 26

<!-- b000961 | prose | pages [24] -->
ms = sort(rand(NP,1)); 27

<!-- b000962 | prose | pages [24] -->
fiti = 1; 28

<!-- b000963 | prose | pages [24] -->
newi = 1; 29

<!-- b000964 | prose | pages [24] -->
while newi <= NP 30

<!-- b000965 | prose | pages [24] -->
if(ms(newi) < fitvalue(fiti)) 31

<!-- b000966 | prose | pages [24] -->
nf(newi,:) = f(fiti,:); 32

<!-- b000967 | prose | pages [24] -->
newi = newi+1; 33

<!-- b000968 | prose | pages [24] -->
else 34

<!-- b000969 | prose | pages [24] -->
fiti = fiti+1; 35

<!-- b000970 | furniture | pages [25] -->
Team 2211922

<!-- b000971 | furniture | pages [25] -->
Page 24

<!-- b000972 | prose | pages [25] -->
end 36

<!-- b000973 | prose | pages [25] -->
end 37

<!-- b000974 | prose | pages [25] -->
%%%%Crossover based on probability%%%%% 38

<!-- b000975 | prose | pages [25] -->
for i = 1:2:NP 39

<!-- b000976 | prose | pages [25] -->
p = rand; 40

<!-- b000977 | prose | pages [25] -->
if p <Pc 41

<!-- b000978 | prose | pages [25] -->
q = rand(1,L); 42

<!-- b000979 | prose | pages [25] -->
for j = 1:L 43

<!-- b000980 | prose | pages [25] -->
%%Arith Crossover Algorithm 44

<!-- b000981 | prose | pages [25] -->
Cross_Temp_1 = nf(i,j).* q(j) + nf(i+1,j) .* (1 - q(j)); 45

<!-- b000982 | prose | pages [25] -->
Cross_Temp_2 = nf(i+1,j).* q(j) + nf(i,j) .* (1 - q(j)); 46

<!-- b000983 | prose | pages [25] -->
nf(i,j) = Cross_Temp_1; 47

<!-- b000984 | prose | pages [25] -->
nf(i+1,j) = Cross_Temp_2; 48

<!-- b000985 | prose | pages [25] -->
end 49

<!-- b000986 | prose | pages [25] -->
end 50

<!-- b000987 | prose | pages [25] -->
end 51

<!-- b000988 | prose | pages [25] -->
i = 1; 52

<!-- b000989 | prose | pages [25] -->
while i<=round(NP*Pm) 53

<!-- b000990 | prose | pages [25] -->
h = randi([1,NP],1,1); 54

<!-- b000991 | prose | pages [25] -->
for j = 1:round(L*Pc) 55

<!-- b000992 | prose | pages [25] -->
g = randi([1,L],1,1); 56

<!-- b000993 | prose | pages [25] -->
nf(h,g) = lb(1,g) + (nf(h,g) - lb(1,g)).*rand; 57

<!-- b000994 | prose | pages [25] -->
end 58

<!-- b000995 | prose | pages [25] -->
i = i+1; 59

<!-- b000996 | prose | pages [25] -->
end 60

<!-- b000997 | prose | pages [25] -->
f = nf; 61

<!-- b000998 | prose | pages [25] -->
f(1,:) = fBest; % Find the best individual 62

<!-- b000999 | prose | pages [25] -->
trace(k) = maxFit; 63

<!-- b001000 | prose | pages [25] -->
end 64
