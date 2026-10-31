# P-B-2022-2211922-6aa59818

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2021

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
B

<!-- b000005 | title | pages [1] -->
2211922

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | prose | pages [1] -->
Reservoir Management: The Art of Proper Allocation

<!-- b000008 | prose | pages [1] -->
People have long used dams to store water to facilitate their lives. Reservoirs not only provide people with water for production and living, but also make contributions to hydropower generation. In recent days, the hot and dry weather with little rainfalls strongly affects the water level in reservoirs. The passage mainly solves the problem encountered in the 2 dams – the Glen Canyon dam and the Hoover dam along the Colorado River. By studying their water level and suggest operations, the passage gets some results that can finally facilitate people’s lives, and can ensure their basic demand by arranging the water scheduling operations in the reservoirs rationally.

<!-- b000009 | prose | pages [1] -->
For the first task, a "Double-Dam" system is abtracted, then we build a difference equation model to simulate the water flows inside and outside from the system and an optimization model that fits the demand well. Firstly, we collect relevant data in terms of agriculture, industry, population and electricity utility respectively, then convert the data into the demand for water, which can better relate to the water volume of the two dams. Then, two sequences respectively represent the water level of the two dams in the model play important parts in the indication that how long will the supply miss the demand. The model subtly simulates the water flows between the "Double-Dam" system and external environment, and the relationship of the two dams can be incorporated as well.

<!-- b000010 | prose | pages [1] -->
The result shows that under given condition, the water should be drawn from Lake Powell is about 430 million m3, and 225 million m3 drawn from Lake Mead (on average). If the additional water only comes from the upstream, after 61 days, the demand and the lower bound of electricity generation would no longer meet. To deal with such a problem, about 40.7 million m3 is needed daily to guarantee the need. Besides, the result also shows that there exists periodic fluctuation of the water storage volume in the reservoirs with a macro downtrend. Therefore, the model should re-run every 100 days according to such a period.

<!-- b000011 | prose | pages [1] -->
For the second task, in order to deal with the competitive relationship of electricity production, a multi-objective model is built and the genetic algorithm is used to find the best allocation plan for general usage and power production. As an extension of the model in Task 1, the algorithm helps find the best distribution ratio in the five states. The result shows that California is allocated the most water sources, with a proportion for nearly 50%. Besides, the proportion of water for electricity generation in California and Arizona states is slightly more than that for general usage, and the situation is opposite in the rest three states.

<!-- b000012 | prose | pages [1] -->
The third task asks for solutions when reservoir resources are scarce. When the water really cannot meet the demand, the distribution method is changed by evaluating the importance of the 5 states in each aspect. Using the principal component analysis (PCA) method, we evaluate the importance of the 5 states in each aspect, then rearrange the proportion for each state and each usage. California takes up the majority of water usage since its advanced development. In terms of the usage, electricity production takes up for slightly over 50%.

<!-- b000013 | prose | pages [1] -->
Finally, sensitivity analysis is performed. The model output is analyzed by adjusting parameters of water volume, taking measures on water-saving, development in renewable energy technologies, growth and shrinkage on population, agriculture scale, industry and power generation, and finally the suppliment of the water inflows from upstream. The model is robust and self-adjustable according to the results. The concrete information is shown in Section 7.

<!-- b000014 | keywords | pages [1] -->
Key words: "Double-Dam" System, Management, Difference Equation Model, Optimization Model,

<!-- b000015 | prose | pages [1] -->
Multi-objective Programming, Genetic Algorithm, Principal Component Analysis

<!-- b000016 | furniture | pages [2] -->
Team 2211922

<!-- b000017 | furniture | pages [2] -->
Page 1

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
1 Introduction

<!-- b000020 | contents | pages [2] -->
2

<!-- b000021 | contents | pages [2] -->
1.1

<!-- b000022 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [2] -->
2

<!-- b000024 | contents | pages [2] -->
1.2

<!-- b000025 | contents | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
2

<!-- b000027 | contents | pages [2] -->
1.3

<!-- b000028 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [2] -->
3

<!-- b000030 | contents | pages [2] -->
2 Assumptions and Explanations

<!-- b000031 | contents | pages [2] -->
3

<!-- b000032 | contents | pages [2] -->
3 Abbreviations and Symbol Notations

<!-- b000033 | contents | pages [2] -->
4

<!-- b000034 | contents | pages [2] -->
4 Arrangements and Changes of Water Supply and Demand

<!-- b000035 | contents | pages [2] -->
5

<!-- b000036 | contents | pages [2] -->
4.1

<!-- b000037 | contents | pages [2] -->
Overview: The Data for Each Aspect . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
5

<!-- b000039 | contents | pages [2] -->
4.2

<!-- b000040 | contents | pages [2] -->
Analysis: The "In and Out" of Water in the Reservoirs . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
7

<!-- b000042 | contents | pages [2] -->
4.3

<!-- b000043 | contents | pages [2] -->
Construction: The Double-Dam System . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
7

<!-- b000045 | contents | pages [2] -->
4.4

<!-- b000046 | contents | pages [2] -->
Result: The Allocation and Changes . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
9

<!-- b000048 | contents | pages [2] -->
5 Balance of Water Distribution for Two Opposite Usages

<!-- b000049 | contents | pages [2] -->
10

<!-- b000050 | contents | pages [2] -->
5.1

<!-- b000051 | contents | pages [2] -->
Analyzing – The Distribution for Different Utilities . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
10

<!-- b000053 | contents | pages [2] -->
5.2

<!-- b000054 | contents | pages [2] -->
Extending – The Distribution Model Based on the Double-Dam System . . . . . . . .

<!-- b000055 | contents | pages [2] -->
11

<!-- b000056 | contents | pages [2] -->
5.3

<!-- b000057 | contents | pages [2] -->
Solving – The Arrangement for Competitive Demands

<!-- b000058 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
12

<!-- b000060 | contents | pages [2] -->
5.3.1

<!-- b000061 | contents | pages [2] -->
The Genetic Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
12

<!-- b000063 | contents | pages [2] -->
5.3.2

<!-- b000064 | contents | pages [2] -->
The Model Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
14

<!-- b000066 | contents | pages [2] -->
6 Thoughts on Water Shortage in Reservoirs

<!-- b000067 | contents | pages [2] -->
14

<!-- b000068 | contents | pages [2] -->
6.1

<!-- b000069 | contents | pages [2] -->
Method Development: The Proper Distribution with Focuses . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
14

<!-- b000071 | contents | pages [2] -->
6.2

<!-- b000072 | contents | pages [2] -->
The Evaluation of the Importance for Each State . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
14

<!-- b000074 | contents | pages [2] -->
6.3

<!-- b000075 | contents | pages [2] -->
Result Statement: The Actual Distribution of Water . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
16

<!-- b000077 | contents | pages [2] -->
7 Sensitivity and Robustness Analysis of the Model

<!-- b000078 | contents | pages [2] -->
16

<!-- b000079 | contents | pages [2] -->
8 Model Advantages and Drawbacks

<!-- b000080 | contents | pages [2] -->
18

<!-- b000081 | contents | pages [2] -->
8.1

<!-- b000082 | contents | pages [2] -->
Advantages

<!-- b000083 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
18

<!-- b000085 | contents | pages [2] -->
8.2

<!-- b000086 | contents | pages [2] -->
Drawbacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
18

<!-- b000088 | contents | pages [2] -->
9 Appendix

<!-- b000089 | contents | pages [2] -->
21

<!-- b000090 | contents | pages [2] -->
9.1

<!-- b000091 | contents | pages [2] -->
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [2] -->
21

<!-- b000093 | contents | pages [2] -->
9.2

<!-- b000094 | contents | pages [2] -->
The Method of Solving the Water Volume Changes . . . . . . . . . . . . . . . . . . .

<!-- b000095 | contents | pages [2] -->
21

<!-- b000096 | contents | pages [2] -->
9.3

<!-- b000097 | contents | pages [2] -->
Part of Data and Results

<!-- b000098 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
22

<!-- b000100 | contents | pages [2] -->
9.3.1

<!-- b000101 | contents | pages [2] -->
Data in Section 4.1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000102 | contents | pages [2] -->
22

<!-- b000103 | contents | pages [2] -->
9.3.2

<!-- b000104 | contents | pages [2] -->
The result in Task 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [2] -->
22

<!-- b000106 | contents | pages [2] -->
9.3.3

<!-- b000107 | contents | pages [2] -->
The result in Task 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
22

<!-- b000109 | contents | pages [2] -->
9.4

<!-- b000110 | contents | pages [2] -->
Code for the Optimization Function of Task 1 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000111 | contents | pages [2] -->
22

<!-- b000112 | contents | pages [2] -->
9.5

<!-- b000113 | contents | pages [2] -->
Code of the Genetic Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000114 | contents | pages [2] -->
23

<!-- b000115 | furniture | pages [3] -->
Team 2211922

<!-- b000116 | furniture | pages [3] -->
Page 2

<!-- b000117 | heading | pages [3] -->
1 Introduction

<!-- b000118 | heading | pages [3] -->
1.1 Problem Background

<!-- b000119 | prose | pages [3] -->
Humans have been using water for a long time to facilitate their lives. There is no doubt that dams are one of the most general water conservancy infrastructures throughout the world. By intercepting rivers and forming reservoirs, dams can not only be used to prevent floods, provide water for production and domestic use, but more importantly, can also be used to generate electricity, which can give support for people’s daily life in surrounding districts.

<!-- b000120 | prose | pages [3] -->
Along the Colorado River in the western part of the United States, there are two famous dams that cross it. They are the Glen Canyon dam and the Hoover dam. The Glen Canyon dam plays a crucial role in storing the water resources and providing the need in surrounding communities since the dam is located in the arid southwestern region. The Hoover dam, built in 1936, also plays an important rule in flood prevention, irrigation, power generation, shipping and water supply.

<!-- b000121 | caption | pages [3] -->
Figure 1: The Glen Canyon Dam (left) and the Hoover Dam (right), from Microsoft Bing

<!-- b000122 | prose | pages [3] -->
However, as the climate change evolves, water storage in these dams is decreasing. The reduction of the water volume of these dams will not only affect the water demand for production and living, but simultaneously, will also affect the electricity generation, so that the comprehensive benefit of the dams will gradually decline. Therefore, in order to help the 5 states – Arizona (AZ), California (CA), Wyoming (WY), New Mexico (NM) and Colorado (CO) better use the water resource which derives from the Glen Canyon dam and the Hoover dam, a proper water distribution plan is badly required.

<!-- b000123 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000124 | prose | pages [3] -->
For the requirements given, we restate them to help better position the focus of our work.

<!-- b000125 | prose | pages [3, 4] -->
• Assume that the water level in Lake Mead is 𝑀, and in Lake Powell is 𝑃, and part of water inflows to Lake Mead from Lake Powell. Task 1 firstly asks for the arrangement of water drawn from each lake to meet the demands. Then, it is also required to estimate how long it will take until the demands are not met under the circumstance that no additional water is supplied and the demand is fixed. After that, it is required to make discussions on the supply amount of additional water under the condition formerly mentioned with the interests of Mexico incorporated. Finally, it would be advisible to address how long should the model to re-run to adapt to changes of condition.

<!-- b000126 | furniture | pages [4] -->
Team 2211922

<!-- b000127 | furniture | pages [4] -->
Page 3

<!-- b000129 | prose | pages [4] -->
• Since there exists a competing relationship between general usage and electricity production of water in the reservoirs, Task 2 demands to come up with the best means to balance the different utilities of water and state the criteria in an explicit way. Note that there exists a lower bound for electricity generation.

<!-- b000130 | prose | pages [4] -->
• Task 3 requires to suggest approaches to tackle with the shortage of water which cannot meet all the demands of electricity production and general usages (including agricultural, industrial and residential usages).

<!-- b000131 | prose | pages [4] -->
• Finally, a sensitivity analysis is required to perfom. When fluctuations of usage of water in agriculture, industry and population, and the changes in the electricity use appear, the response of the model should be revealed.

<!-- b000132 | heading | pages [4] -->
1.3 Our Work

<!-- b000133 | prose | pages [4] -->
Based on the restatement of requirements, our work can be concluded as follows:

<!-- b000134 | prose | pages [4] -->
(1) Analyze the demand of water in 5 states – AZ, CA, WY, NM and CO. Then build a difference equation model and a optimization model for water distribution of reservoirs that not only meets various demands (ariculture, industry, resident and electricity generation) but also takes the water level of 2 dams into account. Except that, analyze the supply and demand when additional water resources are scarce according to the detailed condition given by Task 1 The water that outflows to Mexico should also be addressed.

<!-- b000135 | prose | pages [4] -->
(2) Suggest a multi-objective programming model to balance the usage of water for general approach and electricity production, since they have competitive interests.

<!-- b000136 | prose | pages [4] -->
(3) Based on the demand for each state in each usage, reallocate the water distribution by evaluating the importance of them using principal component analysis (PCA) method.

<!-- b000137 | heading | pages [4] -->
(4) Make sensitivity analysis when parameters like population, agricultural and industrial grows

<!-- b000138 | prose | pages [4] -->
or shrinks. Moreover, the impact of increased use of renewable energy and water & electricity saving measures on the model output also needs to be taken into consideration.

<!-- b000139 | prose | pages [4] -->
The flow chart of our work is presented by Figure 2.

<!-- b000140 | heading | pages [4] -->
2 Assumptions and Explanations

<!-- b000141 | prose | pages [4] -->
In actual practice, there are many complicated conditions that may affect the output of the model. In order to make model more stable and less complex, the following assumptions and their explanations are incorporated.

<!-- b000142 | prose | pages [4] -->
• The water level of the reservoir is proportional to the water volume. Since the dams are built according to the terrain, the relationship between the actual water level and water volume is difficult to analyze. Therefore, this assumption is aiming to simplify the problem.

<!-- b000143 | prose | pages [4] -->
• The inflow of water from upstream remains unchanged within a short period of time. In actual, the water inflows from upstream may vary over time. However, to better abstract the model, we assume the inflow amount is relatively fixed.

<!-- b000144 | furniture | pages [5] -->
Team 2211922

<!-- b000145 | furniture | pages [5] -->
Page 4

<!-- b000146 | prose | pages [5] -->
Simulation Difference Equation for 𝑈𝐸𝛿1,𝛿1∗. 𝑈𝐺𝛿2,𝛿2∗ Single Objective Programming Model Storage of Dam

<!-- b000147 | prose | pages [5] -->
The daily moisture content The daily moisture content GA Algorithm 𝐹𝑖𝑡(𝑥) = 𝑓(𝑥) + 𝜁𝑝(∑𝐶𝑜𝑛𝑠𝑡𝑟𝑎𝑖𝑛𝑡) of of Glen Canyon 𝒂𝒏 Hoover 𝒃𝒏 Electricity Use General Use AZ AZ

<!-- b000148 | prose | pages [5] -->
𝑉𝑜𝑙𝑢𝑚𝑒 CA CO CA Electricity Use CO The Period of Water Addition General Use WY WY NM NM 𝑇

<!-- b000149 | prose | pages [5] -->
Sensitivity AZ CA NM CO WY and E 𝑏1 The distribution of each purpose Robustness Analysis A PCA I 𝑏2 The distribution ratio of each state P

<!-- b000150 | caption | pages [5] -->
Figure 2: The Flow Chart of Our Work

<!-- b000151 | prose | pages [5] -->
• The proportion of power generation usages of water is fixed to a constant in every state, so as other usages. In order to finely estimate the water distribution amount for each state, we assume that the water usage for every aspect is the same in different states.

<!-- b000152 | prose | pages [5] -->
• Rainfall is omitted to solve the model. Because the officials speculate that there will be no rainfall appear in the near future, so the solution of the model only take the inflows of water from upstream of Colorado river into consideration.

<!-- b000153 | heading | pages [5] -->
3 Abbreviations and Symbol Notations

<!-- b000154 | prose | pages [5] -->
In order to make fomula and equations more intuitive and to present our article in a concise manner, we use these abbreviations or notations to represent different entities.

<!-- b000155 | prose | pages [5, 6] -->
Abbreviations Description 𝐷𝑔 Water demand for general usage 𝐷𝑒 Water demand for power generation 𝐷𝑎 Water demand for agriculture 𝐷𝑖 Water demand for power generation 𝐷𝑟 Water demand for daily life {𝑎𝑛} The water volume of the Glen Canyon Dam on n’th day after water shortage {𝑏𝑛} The water volume of the Hoover Dam on n’th day after water shortage 𝑈𝐴 Coordination level of water resource utilization 𝐹𝑖𝑡(𝑥) Fitness function in the genetic function A Water demand matrix 𝚺 Covariance matrix of A after standardization b The distribution ratio for each usage /each state

<!-- b000156 | furniture | pages [6] -->
Team 2211922

<!-- b000157 | furniture | pages [6] -->
Page 5

<!-- b000159 | heading | pages [6] -->
4 Arrangements and Changes of Water Supply and Demand

<!-- b000160 | heading | pages [6] -->
4.1 Overview: The Data for Each Aspect

<!-- b000161 | prose | pages [6] -->
In order to better define the demand for water, it is essentially important to get related data. Since there’re no direct data given, we get several data such as electricity consumption, cultivated land area, population and the number of laborers in the 5 states (the data source is attached in the Reference in Appendix 9.1).

<!-- b000162 | prose | pages [6] -->
• Electricity Generation: We collect data of the electricity consumption per capita in these 5 states from 1960 to 2019, by assuming that the usage of the electricity is generally increasing with time going by, we take the electricity consumption in 2019 as our target of analysis. Figure 3 gives an intuitive way to represent them by visualization.

<!-- b000163 | prose | pages [6] -->
The Electricity Consumption Per Capita in the 5 States 30000

<!-- b000164 | prose | pages [6] -->
Electricity Consumption: Kw·h 25000

<!-- b000165 | prose | pages [6] -->
20000

<!-- b000166 | prose | pages [6] -->
15000

<!-- b000167 | prose | pages [6] -->
10000

<!-- b000168 | prose | pages [6] -->
5000

<!-- b000169 | prose | pages [6] -->
0 AZ CA WY NM CO States

<!-- b000170 | caption | pages [6] -->
Figure 3: The Electricity Consumption Per Capita in the 5 States

<!-- b000171 | prose | pages [6, 7] -->
The usage of electricity is relevant to the amount of the hydropower generation. Since the hy- dropower takes up 6.98% of the total amount of the electricity usage in the U.S. annually, we regard the generation of hydroelectric power by the Glen Canyon dam and the Hoover dam takes up the same ratio in people’s daily use of power in the 5 states. We also get information from the Internet that about 3.67m3 of water can produce 1kW· h of power, therefore, the daily water demand of electricity generation can be described as:

<!-- b000172 | furniture | pages [7] -->
Team 2211922

<!-- b000173 | furniture | pages [7] -->
Page 6

<!-- b000175 | prose | pages [7] -->
5   ∑︁ 𝐷𝑒= 𝐶𝑒× 𝑃𝑜𝑝 × 6.98% × 3.67 ÷ 365 𝑖=1

<!-- b000176 | prose | pages [7] -->
Where 𝐷𝑒stands for the water demand for power generation, 𝐶𝑒represents the electricity consump- tion in the surrounding communities per capita, and 𝑃𝑜𝑝stands for the population of that state.

<!-- b000177 | prose | pages [7] -->
• General Usage of Water: For agriculture, industry and family usage of the water, we also collected relevant data. The visualization of this part of data is shown in Figure 4.

<!-- b000178 | prose | pages [7] -->
Area of Farm Land in the 5 States 42,000,000

<!-- b000179 | prose | pages [7] -->
32,000,000 Area: acres 22,000,000

<!-- b000180 | prose | pages [7] -->
12,000,000

<!-- b000181 | prose | pages [7] -->
2,000,000 AZ CA WY NM CO -8,000,000 States Number of Laborers in the 5 States Population in the 5 States 40000000 18000000 Number of Laborers 16000000 35000000 14000000 30000000 Population 12000000 25000000 10000000 20000000 8000000 15000000 6000000 10000000 4000000 5000000 2000000 0 0 AZ CA WY NM CO AZ CA WY NM CO States States

<!-- b000182 | caption | pages [7] -->
Figure 4: The Condition of Agriculture, Industry and Population in the 5 States

<!-- b000183 | prose | pages [7] -->
With respect to agriculture, the area of farm land is collected (unit: acre). By assuming that the water in need for every farmland is fixed, we can easily estimate the water demand 𝐷𝑎for agricultural usage by mutiplying the farmland area 𝐶𝑎with the average demand for a unit area annually, which is 364.50m3/acre.

<!-- b000184 | prose | pages [7] -->
𝐷𝑎= 𝐶𝑎× 364.50 ÷ 365

<!-- b000185 | prose | pages [7] -->
For industry, we collect the number of laborers and project water expenses annually in each state. Through the calculation of these two data items and water tariff per unit, the water demand required by industry can be estimated as:

<!-- b000186 | prose | pages [7] -->
5   ∑︁ 𝐷𝑖= 𝐶𝑖× 𝐿𝑏𝑠 ÷ 𝐶𝑤÷ 365 𝑖=1 Where 𝐷𝑖indicates the water demand for industry, 𝐶𝑖stands for the water expense in industry per capita annually, 𝐿𝑏𝑠is the number of laborers for a certain state, and 𝐶𝑤is the water tariff per unit. Relevant data is attached to the Appendix 9.3.1.

<!-- b000187 | prose | pages [7, 8] -->
Finally for residential usage, we collect data from the Internet about the water consumption per capita, which is 0.54m3. By timing this item with the population, the water demand for families 𝐷𝑟 can be easily estimated as 5   ∑︁ 𝐷𝑟= 𝑃𝑜𝑝 × 0.54 𝑖=1 Add four demands together, the water demand 𝐷𝑔for general use can be calculated, which is:

<!-- b000188 | furniture | pages [8] -->
Team 2211922

<!-- b000189 | furniture | pages [8] -->
Page 7

<!-- b000191 | prose | pages [8] -->
𝐷𝑔= 𝐷𝑎+ 𝐷𝑖+ 𝐷𝑟

<!-- b000192 | heading | pages [8] -->
4.2 Analysis: The "In and Out" of Water in the Reservoirs

<!-- b000193 | prose | pages [8] -->
The Glen Canyon dam and the Hoover dam provide water and hydropower to surrounding states together. What’s more, part of the water in the Glen Canyon dam flows into the Hoover dam, making the two dams more closely linked. When the water level and the demand are fixed, how much water to draw from each dam is the problem.

<!-- b000194 | prose | pages [8] -->
For the Glen Canyon dam, it not only supplies water for general use and power generation, but part of water from it outflows into the Hoover dam. In contrast, the Hoover dam mainly support the general and power-generate usage and has no concern about the outflow. But in order to take the river environment and the interests of Mexico into consideration, apparently the water in the Hoover dam shouldn’t be totally drawn. The process of water flow in Colorado river between the 2 dams are described in the picture shown as Figure 5, which is the basis of the model.

<!-- b000195 | prose | pages [8] -->
The Glen Canyon Dam The Hoover Dam

<!-- b000196 | prose | pages [8] -->
General Use Power Generation

<!-- b000197 | caption | pages [8] -->
Figure 5: The Relationship between Two Dams (The arrows stand for water flows)

<!-- b000198 | prose | pages [8] -->
As no additional water is available but only comes from the upstream, the water in the reservoir gradually dwindles to the point where it cannot supply the demand. Besides, to ensure the generation of electricity, the lower bound of the water volume is calculated, which is about 19.4 billion.

<!-- b000199 | prose | pages [8] -->
Under such a condition, a rational estimation ought to be addressed, so that relevant departments can perform certain operations to fulfill the water volume to satisfy the demand. Moreover, an estimation of the additional water volume is also needed.

<!-- b000200 | heading | pages [8] -->
4.3 Construction: The Double-Dam System

<!-- b000201 | prose | pages [8] -->
Based on the analysis in Section 4.1, we build a difference equation model to simulate changes of the two dams, and a optimization model to offer suggestions to negotiators to help them better perform the water distribution process.

<!-- b000202 | furniture | pages [9] -->
Team 2211922

<!-- b000203 | furniture | pages [9] -->
Page 8

<!-- b000204 | prose | pages [9] -->
Firstly, we abstract the two dams into two nodes as a system. Since part of the water from the Glen Canyon dam flows along the Colorado River into the Hoover dam, we use a one-directional arrow between the two nodes to represent the flow of water. From the perspective of such a system, there is extra water inflows into it (only from upstreams of the river), and water should be drawn out of it. What’s more, there will be part of water left to go down to satisfy the need for other regions (e.g. for Mexico). The flowchart of the system with several parameters is shown in Figure 6.

<!-- b000205 | prose | pages [9] -->
Life  & Production 𝐹1

<!-- b000206 | prose | pages [9] -->
Electricity 𝐹2

<!-- b000207 | prose | pages [9] -->
𝑘13 𝑘23 𝑘14 𝑘24

<!-- b000208 | prose | pages [9] -->
𝐷𝑎𝑚2 𝐸𝑥𝑡𝑟𝑎 𝐷𝑎𝑚1 Mexico 𝑎𝑛 𝑏𝑛

<!-- b000209 | prose | pages [9] -->
𝑇𝑘13 𝑇𝑘14 𝑎𝑛 𝑎𝑛 𝐹1 𝐹2 𝑏𝑛 𝑏𝑛 𝑘23 𝑘24

<!-- b000210 | caption | pages [9] -->
Figure 6: The Double-Dam System and the Water Flows

<!-- b000211 | prose | pages [9] -->
There are several parameters in the diagram, 𝑎𝑛and 𝑏𝑛represents the water level (which is directly connected to the water volume) in the two dams in n’th day after additional water shortage under the assumption that 𝑎0 = 𝑉𝑝and 𝑏0 = 𝑉𝑚, 𝑉𝑝and 𝑉𝑚is proportional to the given water level 𝑃and 𝑀. The 𝐷𝑎𝑚1 stands for the Glen Canyon dam while the 𝐷𝑎𝑚2 stands for the Hoover dam. Specifically, parameters 𝑘𝑖𝑗are coefficients which is the ratio of water that outflows from its original dam. For the total outflows of the water, 2 major usages are seperated – the general use (agricultural, industrial and residential) which is represented by 𝐹1 and the power generation represented by 𝐹2.

<!-- b000212 | prose | pages [9] -->
When additional water shortage occurs, the volume will gradually shrink within a certain period of time. Therefore, the numbers of elements in the two sequences will change over time as 𝑛increases. So when the total water volume is too low to feed the demand, the 𝑛is the number of days that need to be solved. The {𝑎𝑛} and {𝑏𝑛} can be described as the difference equation below:

<!-- b000213 | prose | pages [9] -->
𝑎𝑛−𝑎𝑛−1 = −𝑘13𝑎𝑛−1 −𝑘14𝑎𝑛−1 + 𝑒 𝑏𝑛−𝑏𝑛−1 = 𝑘14𝑎𝑛−1 −𝑘23𝑏𝑛−1 −𝑘24𝑏𝑛−1 In the fomula above, the items in both sides of equation represent the increment of water volume in the dam. What’s more, 𝑒is the extra volume of water that inflows from upstream of the Colorado River, which is regarded as a constant within a certain period. Besides, {𝑎𝑛} and {𝑏𝑛} are internally correlated. The method of solving the general formula of {𝑎𝑛} and {𝑏𝑛} is attached to the Appendix in 9.2. We solve the equation and find the concrete form of {𝑎𝑛} and {𝑏𝑛} as:

<!-- b000214 | furniture | pages [10] -->
Team 2211922

<!-- b000215 | furniture | pages [10] -->
Page 9

<!-- b000216 | prose | pages [10] -->
𝑒 𝑒 𝑎𝑛= (1 −𝑘13 −𝑘14)𝑛  𝑉𝑝− + 𝑘13 + 𝑘14 𝑘13 + 𝑘14

<!-- b000217 | prose | pages [10] -->
𝑏𝑛= 𝑘14(1 −𝑘13 −𝑘14)[(1 −𝑘23 −𝑘24)𝑛−(1 −𝑘13 −𝑘14)𝑛] 𝑒   𝑉𝑝− 𝑘13 + 𝑘14 −𝑘23 −𝑘24 𝑘13 + 𝑘14 𝑒𝑘14 𝑒𝑘14 + (1 −𝑘23 −𝑘24)𝑛h i 𝑉𝑚− + (𝑘23 + 𝑘24)(𝑘13 + 𝑘14) (𝑘23 + 𝑘24)(𝑘13 + 𝑘14)

<!-- b000218 | prose | pages [10] -->
In order to meet both the general demand and power generation demand, we construct the following optimization model to optimize the deployment of the water resource from the two dams:

<!-- b000219 | prose | pages [10] -->
𝑚𝑖𝑛 𝐷𝑔−𝑎𝑛𝑘13 −𝑏𝑛𝑘23 𝑘13,𝑘23 𝑘14,𝑘24 |𝐷𝑒−𝑎𝑛𝑘14 −𝑏𝑛𝑘24| 𝑚𝑖𝑛

<!-- b000220 | prose | pages [10] -->
𝑠.𝑡. 𝐷𝑒+ 𝐷𝑔< 𝑉𝑚+ 𝑉𝑝 0 < 𝑘13 + 𝑘23 < 1 0 < 𝑘14 + 𝑘24 < 1

<!-- b000221 | prose | pages [10] -->
The 2 objective functions represent the absolute difference between the demand and the water usage for general use and electricity generation respectively. In practice, the water drawn from reservoirs should bestly fit the demand, or else the waste of water will occur. The objective functions above ensure the water drawn from the two dams generates a minimum amount of waste on the basis of meet the fundamental demands. In order to minimize the objective function, a few constraint conditions is added, which includes that the demand should less than the total volume of the two reservoirs, and the sum of nonnegative coefficients 𝑘13, 𝑘23 and 𝑘14, 𝑘24 be less than 1 to limit the extraction of water. The general term of {𝑎𝑛} and {𝑏𝑛} is used to optimize the objective function. The model perfectly abstracts the "in and out" water flow problem in the 2 dams.

<!-- b000222 | heading | pages [10] -->
4.4 Result: The Allocation and Changes

<!-- b000223 | prose | pages [10] -->
By defining the value of parameters according to previous data, we solve the water volume which should be extracted from each dam, the time interval between the occurence of additional water shortage and the shortage for demand, and the additional water volume that should be supplied.

<!-- b000224 | prose | pages [10] -->
When the water storage of the Glen Canyon dam is about 24.1 billion m3, and the storage of the Hoover dam is 25.6 billion m3 (which corresponds to a fixed set of 𝑃and 𝑀), the water that should be drawn from Lake Powell is about 430 million m3 while the water drawn from Lake Mead is about 225 million m3 (Unit: per day, on average). The concrete data is shown in the Appendix. Mention that since we consider the water inflows to Lake Mead from Lake Powell over time, the actual result may fluctuate according to the situation.

<!-- b000225 | prose | pages [10, 11] -->
When the additional water is no longer available, the model shows that the water can supply the demand until the 61st day. Until then, additional water should be suppplied, with a relatively stable volume at 40.7 million m3 per day (about 2 trillion m3 within 61 days) What’s more, a special pattern occurs along with the outcome of the result – the water storage shows a periodic rebound in the overall declining trend like the trend shown in Figure 7. This is based

<!-- b000226 | furniture | pages [11] -->
Team 2211922

<!-- b000227 | furniture | pages [11] -->
Page 10

<!-- b000229 | prose | pages [11] -->
𝑉𝑜𝑙𝑢𝑚𝑒 When the dam is in the recovery period (the 7.00E+08 diagram on the left), the in-time replenish- ment of water during this period can prevent the shortage of water for later periods. 6.00E+08 𝑇

<!-- b000230 | prose | pages [11] -->
5.00E+08

<!-- b000231 | prose | pages [11] -->
4.00E+08

<!-- b000232 | prose | pages [11] -->
3.00E+08

<!-- b000233 | prose | pages [11] -->
2.00E+08

<!-- b000234 | prose | pages [11] -->
1.00E+08

<!-- b000235 | prose | pages [11] -->
0.00E+00 1 31 61 91 121 151 181 211 241 271 301 331 361 Actual Demand Sum of Water Supply Supplement Cycle

<!-- b000236 | caption | pages [11] -->
Figure 7: Result of the Periodic Decrease for Water Storage

<!-- b000237 | prose | pages [11] -->
on the assumption that the extra water inflows the double-dam system is a constant – the flow volume of the Colorado river, which coincides with the objective phenomenon that the system has the ability of self-regulation. Of course, in terms of the overall trend, the storage is always decreasing over time.

<!-- b000238 | prose | pages [11] -->
We also get from this pattern that the time in a phase is about 100 days (over 3 months). If the negotiators want to make the model more accurate, the parameters should be redefined and the model should re-run every 100 days. Certainly, if the additional water is supplied by water transfer projects or other policies, the restart of the model is also needed. Finally, since part of the water outflows from the Glen Canyon dam supply the input to the Hoover dam, about 150 million m3 of water should be operated to flow from the Glen Canyon dam to the Hoover dam.

<!-- b000239 | prose | pages [11] -->
Ultimately, in order to take the interests of Mexico into consideration, the rest of water volume should be at a proper level. In our model, this can be represented as 𝑏𝑛· 𝑘24 at most. That is because the water used for power generation of the Hoover dam outflows to the downstram, and there are some losses along the way.

<!-- b000240 | heading | pages [11] -->
5 Balance of Water Distribution for Two Opposite Usages

<!-- b000241 | heading | pages [11] -->
5.1 Analyzing – The Distribution for Different Utilities

<!-- b000242 | prose | pages [11, 12] -->
The Glen Canyon dam and the Hoover dam provide the surrounding areas with water for production, living and electricity generation. However, with climate change, the water in the dam needs to be distributed more rationally to make it most effective. The water in reservoirs, in general, can be seperated into 4 major utilities: agricultural, industrial, residential usage (we call it "general usage") and electricity generation. Therefore, rational allocation of water resources requires an fully understanding of how water in the dams affects these activities. The content of this part is described below.

<!-- b000243 | furniture | pages [12] -->
Team 2211922

<!-- b000244 | furniture | pages [12] -->
Page 11

<!-- b000246 | prose | pages [12] -->
Firstly, the water is mainly for general usage and electricity production. Besides, in the general usage, the water in the reservoir is also partially converted into electricity for agriculture, industry and families. Therefore, the effects of water in the reservoir on general and power generation usages are interrelated and can be intuitively presented using the diagram in Figure 8.

<!-- b000247 | prose | pages [12] -->
Water in the Reservoirs

<!-- b000248 | prose | pages [12] -->
Agriculture Industry Family

<!-- b000249 | prose | pages [12] -->
Electricity

<!-- b000250 | caption | pages [12] -->
Figure 8: The Utilities of Water in Reservoirs

<!-- b000251 | prose | pages [12] -->
The above analysis shows that ideal results can be produced as long as the water allocation process is clarified. What’s more, the demand of water for general usage and power generation are competitive. That is to say, when the usage of one demand increases, another usage will decrease correspondingly. Therefore, a rational plan should be established to balance them reasonably.

<!-- b000252 | heading | pages [12] -->
5.2 Extending – The Distribution Model Based on the Double-Dam System

<!-- b000253 | prose | pages [12] -->
We extend the model in Task 1 – study the distribution of water for the demand (𝐷𝑒and 𝐷𝑔), with the aim of using the water in a more proper and rational way.

<!-- b000254 | prose | pages [12] -->
For a fixed demand, 4 mainly usages can be seperated: agricultural, industrial, residential and power generation. The main conflicting parties for water allocation, in short, are power generation and other utilities which are called "general usage".

<!-- b000255 | prose | pages [12] -->
In order to combine the scheduling and actual use of water resources, coordination level of water resource utilization for utility A is defined in a functional manner as 𝑈𝐴(𝛿, 𝛿∗):

<!-- b000256 | prose | pages [12, 13] -->
𝛿≥𝛿∗ ( 1 𝑈𝐴= 𝑒𝑥𝑝[−(𝛿−𝛿∗)2/𝑆2 𝛿< 𝛿∗ 𝐴] In the formula above, the parameter 𝛿stands for the ratio of water allocation for a certain usage, for instance, the ratio of water used for power generation. It can be calculated as

<!-- b000257 | furniture | pages [13] -->
Team 2211922

<!-- b000258 | furniture | pages [13] -->
Page 12

<!-- b000260 | prose | pages [13] -->
𝛿= 𝑢𝑠𝑒𝑓𝑜𝑟𝐴 𝛿∗= 𝑑𝑒𝑚𝑎𝑛𝑑𝑓𝑜𝑟𝐴 𝑡𝑜𝑡𝑎𝑙𝑢𝑠𝑒 𝑡𝑜𝑡𝑎𝑙𝑑𝑒𝑚𝑎𝑛𝑑

<!-- b000261 | prose | pages [13] -->
The constant 𝛿∗stands for the demand ratio. Besides, the 𝑆2 𝐴stands for the variance of the difference between the demand 𝐷𝑘and the supply of water 𝑥𝑘in this usage among different subregions in the district: 𝑛 𝐴= 1 ∑︁ 𝑆2 (𝐷𝑘−𝑥𝑘)2 𝑛 𝑘=0 The inequality 𝛿≥𝛿∗represents that when the allocation ratio is no less than the demand, the demand is well satisfied. Therefore, the coordination level can be defined to 1, which is the highest value. When 𝛿≤𝛿∗, which means the supply cannot meet the demand. Under such circumstance, the Gaussian Distribution function is used to represent the difference between them.

<!-- b000262 | prose | pages [13] -->
The main contradiction of the water distribution – the distribution for general and power generation, should firstly be considered. According to the definition of coordination level of water resource utilization above, for these two utilities, we define two functions: 𝑈𝐸(𝛿1, 𝛿∗ 1) which is related to the electricity generation and 𝑈𝐺(𝛿2, 𝛿∗ 2) represents for the general usage. To best coordinate the distribution of the water in the reservoir, 𝑈𝐸and 𝑈𝐺should both be maximized:

<!-- b000263 | prose | pages [13] -->
√︃ 𝑚𝑎𝑥𝑓(𝑥) = 𝑈𝐸(𝛿1, 𝛿∗ 1) · 𝑈𝐺(𝛿2, 𝛿∗ 2)

<!-- b000264 | heading | pages [13] -->
5.3 Solving – The Arrangement for Competitive Demands

<!-- b000265 | heading | pages [13] -->
5.3.1 The Genetic Algorithm

<!-- b000266 | prose | pages [13] -->
To solve such a problem, genetic algorithm is used. From the beginning, we define a vector x with 10 dimensions with 𝑥1 to 𝑥5 respectively represent the water demand for electricity generation for each state while 𝑥6 to 𝑥10 represent the demand for general usages.

<!-- b000267 | prose | pages [13] -->
Step 1 First, we initialize the number of population to 200, for each individual within the population, the formula below (which is called "mutation operator" later) can help initialize elements for each individual randomly:

<!-- b000268 | prose | pages [13] -->
𝑥𝑖= 𝑟𝑎𝑛𝑑𝑜𝑚(𝑙𝑏, 𝑢𝑏) Where 𝑙𝑏is the predefined lower bound value and 𝑢𝑏is the upper bound value, which are restricted by the situation of the problem. The function 𝑟𝑎𝑛𝑑𝑜𝑚(𝑎, 𝑏) generates a random value in interval [𝑎, 𝑏].

<!-- b000269 | prose | pages [13] -->
Step 2 On the basis of our objective function, we reconfigure it into the adaption function to judge the strengths and weaknesses of individuals. The adaption function can be defined as:

<!-- b000270 | prose | pages [13] -->
5 10 h i ∑︁ ∑︁ 𝐹𝑖𝑡(𝑥) = 𝑓(𝑥) + 𝜁𝑝 (𝐸𝑐𝑜𝑠𝑡𝑖−𝑥𝑖) + (𝐺𝑐𝑜𝑠𝑡𝑖−𝑥𝑖) 𝑖=1 𝑖=6

<!-- b000271 | prose | pages [13, 14] -->
𝐸𝑐𝑜𝑠𝑡and 𝐺𝑐𝑜𝑠𝑡represent the demand for electricity generation and general usage in each state. The difference between the distributed water and the demand reflects the adaption level for a certain individual. The penalty factor 𝜁𝑝decreases the function value when constraint is not satisfied, which makes it more accurate for evaluating the adaption level of that individual.

<!-- b000272 | furniture | pages [14] -->
Team 2211922

<!-- b000273 | furniture | pages [14] -->
Page 13

<!-- b000275 | prose | pages [14] -->
Step 3 Evaluate each initialized population individual by means of the adaptation function.

<!-- b000276 | prose | pages [14] -->
Step 4 Use Roulette Selection Method to select individuals in random. That is, if the adaption level for each individual is 𝑎𝑘(𝑘= 1, 2, ..., 200), then for a certain individual, it’s probability to be chosen can be calculated as: 𝑎𝑖 𝑃(𝑎𝑖) = 𝑘=1 𝑎𝑘 Í200

<!-- b000277 | prose | pages [14] -->
Step 5 Define crossover and mutation operators to update the elements for individuals by imitating the cross-exchange and variation of genes in nature. In crossover operation, 2 individuals are randomly chosen as 𝑥1 and 𝑥2, and perform the operations presented in pseudocode below:

<!-- b000278 | prose | pages [14] -->
Crossover Operation r = random(0, 1);

<!-- b000279 | prose | pages [14] -->
𝑡𝑒𝑚𝑝1 = 𝑟𝑥1 + (1 −𝑟)𝑥2;

<!-- b000280 | prose | pages [14] -->
𝑡𝑒𝑚𝑝2 = 𝑟𝑥2 + (1 −𝑟)𝑥1;

<!-- b000281 | prose | pages [14] -->
𝑥1 = 𝑡𝑒𝑚𝑝1;

<!-- b000282 | prose | pages [14] -->
𝑥2 = 𝑡𝑒𝑚𝑝2;

<!-- b000283 | prose | pages [14] -->
Step 6 Select best individuals that can fit the situation well Step 7 Repeat from Step 4 to Step 6 several times, then get the individuals remain as the result.

<!-- b000284 | prose | pages [14] -->
Origin Population

<!-- b000285 | prose | pages [14] -->
Roulette Wheel … AZ

<!-- b000286 | heading | pages [14] -->
Best Solutions

<!-- b000287 | prose | pages [14] -->
EU Solutions 𝑖 CO CA GU Solutions 𝑗 Fit function with … Roulette Wheel Selection WY NM

<!-- b000288 | prose | pages [14] -->
Origin AZ Crossover Population Mutation … … … … CO CA … … … … … …

<!-- b000289 | prose | pages [14] -->
WY NM Yes GN<N ?

<!-- b000290 | prose | pages [14] -->
No 5 10 𝐹𝑖𝑡(𝑥) = 𝑓(𝑥) + 𝜁𝑝( ෍ (𝐸𝑐𝑜𝑠𝑡𝑖−𝑥𝑖) + ෍ (𝐺𝑐𝑜𝑠𝑡𝑖−𝑥𝑖) )

<!-- b000291 | heading | pages [14] -->
Best Solutions

<!-- b000292 | prose | pages [14] -->
𝑖= 1 𝑖=6

<!-- b000293 | caption | pages [14] -->
Figure 9: The Flow Chart of Genetic Algorithm

<!-- b000294 | prose | pages [14] -->
The code of implementing such an algorithm is attached to the Appendix 9.4.

<!-- b000295 | furniture | pages [15] -->
Team 2211922

<!-- b000296 | furniture | pages [15] -->
Page 14

<!-- b000297 | heading | pages [15] -->
5.3.2 The Model Result

<!-- b000298 | prose | pages [15] -->
The result solved by the model is shown in the Figure 10.

<!-- b000299 | prose | pages [15] -->
The Allocation of Water Unit: million 100 90 80 70 60 50 40 30 20 10 0 California Arizona New Mexico Colorado Wyoming Electricity Generation General Usage

<!-- b000300 | caption | pages [15] -->
Figure 10: The Allocation of Water for Each State

<!-- b000301 | prose | pages [15] -->
From the figure, California takes most of the water supply, and the water supply for general use in the New Mexico, Colorado and Wyoming States are relatively greater than the generation of electricity. This may result from the fact that California is relatively more developed than other states, and the source of electricity in California are mainly from hydropower than other powers. The concrete data is presented in the Appendix 9.3.2.

<!-- b000302 | heading | pages [15] -->
6 Thoughts on Water Shortage in Reservoirs

<!-- b000303 | heading | pages [15] -->
6.1 Method Development: The Proper Distribution with Focuses

<!-- b000304 | prose | pages [15] -->
When water shortage occurs, relevant personnel must change water operations from reservoirs in time to suit the current situation. Since the water tranfer projects can not be constructed within a short period of time to supply the need, and the water in the reservoirs cannot meet all the demands of the five states, a proper allocation plan with focuses is needed to ensure maximum economic benefits. That is to say, the water can be bestly utilized.

<!-- b000305 | heading | pages [15] -->
6.2 The Evaluation of the Importance for Each State

<!-- b000306 | prose | pages [15] -->
When the water shortage appears, it is advisible to reallocate the water with focuses according to the water demand in each aspects for the 5 states. The principal component analysis (PCA) method is used to evaluate the allocation ratio, and the allocation ratio can be used to reflect the importance for each state. The main steps are describe below.

<!-- b000307 | prose | pages [15, 16] -->
• With respect to the 4 aspects descibed in section 4.1 for each state, we represent them in the table below, where 𝑥𝑖𝑗stands for the water demand of state 𝑗in aspect 𝑖 CA AZ NM CO WY 𝑥11 𝑥12 𝑥13 𝑥14 𝑥15 Electricity 𝑥21 𝑥22 𝑥23 𝑥24 𝑥25 Agriculture 𝑥31 𝑥32 𝑥33 𝑥34 𝑥35 Industry 𝑥41 𝑥42 𝑥43 𝑥44 𝑥45 Daily Life

<!-- b000308 | furniture | pages [16] -->
Team 2211922

<!-- b000309 | furniture | pages [16] -->
Page 15

<!-- b000311 | prose | pages [16] -->
Therefore, we define a matrix to represent the table above as:

<!-- b000312 | prose | pages [16] -->
A4×5 = A(𝑥𝑖𝑗), 𝑖= 1, 2, 3, 4; 𝑗= 1, 2, 3, 4, 5

<!-- b000313 | prose | pages [16] -->
• Standardization: Firstly, solve the average and the sample variance for each row:

<!-- b000314 | prose | pages [16] -->
5 5 𝑥𝑖= 1 1 ∑︁ ∑︁ 𝑥𝑖𝑗, 𝑠2 (𝑥𝑖𝑗−𝑥𝑖)2 𝑖= 5 −1 5 𝑗=1 𝑗=1

<!-- b000315 | prose | pages [16] -->
Then, standardize A and let the matrix after standardization to be A′, that is: A′4×5 = A′(𝑥′ 𝑖𝑗). For each element in matrix A, there is: 𝑖𝑗= 𝑥𝑖𝑗−𝑥𝑖 𝑥′ 𝑠𝑖

<!-- b000316 | prose | pages [16] -->
• Represent A′ as (a1 a2 a3 a4 a5), and an is regarded as a column vector. Then solve the covariance matrix 𝚺of matrix A′ with respect to these column vectors.

<!-- b000317 | prose | pages [16] -->
𝚺= 𝐶𝑜𝑣(a1 a2 a3 a4 a5) 𝐶𝑜𝑣(a1, a1) 𝐶𝑜𝑣(a1, a2) 𝐶𝑜𝑣(a1, a5) · · · 𝐶𝑜𝑣(a2, a1) 𝐶𝑜𝑣(a2, a2) 𝐶𝑜𝑣(a2, a5) · · · ©­­­­ ª®®®® ... ... ... = ...

<!-- b000318 | prose | pages [16] -->
𝐶𝑜𝑣(a5, a1) 𝐶𝑜𝑣(a5, a2) 𝐶𝑜𝑣(a5, a5) · · · « ¬ Where 4 𝐶𝑜𝑣(an, am) = 1 ∑︁ (𝑥′ 𝑖𝑛−𝑥′𝑛)(𝑥′ 𝑖𝑚−𝑥′𝑚) .   4 𝑖=1 4 4 𝑥′𝑛= 1 𝑥′𝑚= 1 ∑︁ ∑︁ 𝑥′ 𝑥′ 𝑖𝑛, 𝑖𝑚 4 4 𝑖=1 𝑖=1

<!-- b000319 | prose | pages [16] -->
• Find the 5 eigenvalues of the matrix 𝚺, select eigenvectors v with relatively larger eigenvalues than others.

<!-- b000320 | prose | pages [16] -->
• Let b = Av, then normalize every element of the column vector b. The element of b after normalization is the proportion ratio of the water distribution for each usage.

<!-- b000321 | prose | pages [16] -->
• Exchange the rows and columns of A, find the water distribution proportion for each state using the same approach.

<!-- b000322 | prose | pages [16] -->
• Multiple the total amount of water to the distribution ratio for each state, then time it by the ratio for a sepcific usage. Finally the concrete distribution amount of this usage in that state is solved.

<!-- b000323 | furniture | pages [17] -->
Team 2211922

<!-- b000324 | furniture | pages [17] -->
Page 16

<!-- b000325 | heading | pages [17] -->
6.3 Result Statement: The Actual Distribution of Water

<!-- b000326 | prose | pages [17] -->
The result shows that when the water shortage really occurs, the distribution plan should be rearranged. Most of the water supply is allocated to California with a ratio for more than 50% since its strength in almost every aspect including agriculture, industry, etc. While in terms of usages, about a half of the water is allocated to the generation of electricity. The charts are shown in Figure 11 to make intuitive visualizations, while the concrete data are attached to the Appendix.

<!-- b000327 | prose | pages [17] -->
Distribution Ratio of Water for Each Purpose Distribution Ratio of Water for Each State Colorado 0.69%

<!-- b000328 | prose | pages [17] -->
13.31%

<!-- b000329 | caption | pages [17] -->
Figure 11: The Overview of the Result When Water Shortage Occurs

<!-- b000330 | prose | pages [17] -->
The concrete data is shown in the Appendix 9.3.3.

<!-- b000331 | heading | pages [17] -->
7 Sensitivity and Robustness Analysis of the Model

<!-- b000332 | prose | pages [17] -->
When fluctuations in the parameters occurs, for instance, the water demand for agriculture increases or decreases over time, what will happen to the output of the model is crucial in a large sense, which may result in direct changes in operation of the two dams. Therefore, sensitivity analysis is performed to evaluate the model. Firstly, the satisfaction rate is defined to represent the satisfaction level of water ( 𝑆𝑢𝑝𝑝𝑙𝑦 𝐷𝑒𝑚𝑎𝑛𝑑) supply under a certain circumstance. From the upper left diagram of Figure 12, we can see that when the demand multiplies as shown in the horizontal axis, the water storage gradually decreases over time. However, the storage value will ultimately approach a constant. This phenomenon is originated from the constraint of the lower bound of water volume in the two dams. The result shows that the robustness of model can satisfy the expectation that it can not only meet the demand but can also function normally.

<!-- b000333 | prose | pages [17, 18] -->
After that, the upper right diagram of Figure 12 shows the model output when water-saving measures are taken and the proportion of renewable technologies is increasing. We define the day 𝑛= 65, which indicates that the reservoir can no longer meet the demand. Under such a circumstance, Gap S Rate Satisfaction Rate Demand and Distribution Gap 1.21 5.00E+08 1.2 0.00E+00 1.19 -5.00E+08 1.18 -1.00E+09 1.17 -1.50E+09 1.16 1.15 -2.00E+09 1.14 -2.50E+09 1.13 T -3.00E+09 1.12 Multiple 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 1.11 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 Normal Condition Water Saving = 0.8 n = 15 n = 10 n = 5 New Energy Using = 0.8

<!-- b000334 | furniture | pages [18] -->
Team 2211922

<!-- b000335 | furniture | pages [18] -->
Page 17

<!-- b000337 | prose | pages [18] -->
Extra Increase Changes of Demands Accompanied with Growth in Different Usages Usage 1.20E+09 Usage 3.00E+09 1.00E+09 2.50E+09 8.00E+08 2.00E+09 6.00E+08 1.50E+09 4.00E+08 1.00E+09 5.00E+08 2.00E+08 Multiple Multiple 0.00E+00 0.00E+00 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 1 1.5 2 2.5 3 3.5 4 4.5 5 Population Agriculture Electricity Industry n = 30 n = 65 n = 85

<!-- b000338 | caption | pages [18] -->
Figure 12: The Result of Sensitivity Analysis

<!-- b000339 | prose | pages [18] -->
to take measures may offer help to the lack of supply. So we make the dams work for 20 days to see the results.

<!-- b000340 | prose | pages [18] -->
After water-saving measures are taken, the supply can meet 80% of demand (shown in red dotted line) for 11 days. Nonetheless, the result will sharply decrease in later days, so that the demand can not be well satisfied. Moreover, when renewable energy usage increases, similar situation also occurrs – the supply can meet about 80% for 11 days but decreases afterwards, but not as badly as the result of taking water-saving measures. The result also displays that the implementation of water makes little contribution to the increase of the water level in reservoirs Then, the relationship between the growth and shrinkage of population, agriculture, industry and power generation and the water level is presented at the lower left diagram of the Figure. By increasing the demand for each aspect and raise the value through 7 times of the original ones, we can see that the electricity generation aspect has a maximum slope, and population aspect has a minimum one. In general, water demand for electricity generation should be firstly satisfied, then the industrial one, then agriculture. Fianlly, the influence on the water level in the dams brought by "ups and downs" of population is relatively small.

<!-- b000341 | prose | pages [18] -->
When we shift our target to the water inflows from the upstream, the result is shown in the lower right diagram of the Figure. Similarly to the first diagram, the 𝑛represents the extent of water shortage. When the water volume is sufficient, the allocation varies little because the current water volume can already meet the demand. But when the water is scarce in the reservoir, the allocation will gradually increase, and will approach the allocation amount ultimately, which shows that the model can adjuct itself when external conditions are proper.

<!-- b000342 | furniture | pages [19] -->
Team 2211922

<!-- b000343 | furniture | pages [19] -->
Page 18

<!-- b000344 | heading | pages [19] -->
8 Model Advantages and Drawbacks

<!-- b000345 | prose | pages [19] -->
Finally, to have a more comprehensive perspective of our model, we make conclusions about the advantages and drawbacks of it.

<!-- b000346 | heading | pages [19] -->
8.1 Advantages

<!-- b000347 | prose | pages [19] -->
The model based on the "Double-Dam" system well abstracts the operations of the Glen Canyon and the Hoover dams. And the difference equation model inside the system natually take the inflows and outflows of water to each whereabouts. What’s more, the original water level (water storage) of the two dams 𝑀and 𝑃is incorporated by 𝑎0 and 𝑏0. Therefore, the model comprehensively simulates the working process and for reservoir managers, it can be easier to make rapid decisions on relevant allocation changes. What’s more, the model can be easily calculated by programming, no complicated theorems or theories are used. Last, when rainfall comes, constants can be added to the difference model (see constants 𝐶and 𝐹in the Appendix 10.1) so that more complex situations can be fully embraced.

<!-- b000348 | heading | pages [19] -->
8.2 Drawbacks

<!-- b000349 | prose | pages [19] -->
Even though the model functions and simulates the situation well, there are a few drawbacks. At first, the approach the model uses may call for complicated calculation condition. Besides, the model cannot always fit the actual changes of situation. It should re-run for every 100 days routinely. Especially, when some new policies that can affect the water volume in reservoirs, the parameters in the model should be modified to fit the new situation.

<!-- b000350 | prose | pages [20] -->
Drought and Thirst February 2022

<!-- b000351 | prose | pages [20] -->
Should Dams Be Condemned?

<!-- b000352 | heading | pages [20] -->
—Discussion about the Colorado river dams

<!-- b000353 | prose | pages [20] -->
A s the most important river in the southwestern part of the United States, the Colorado river offers various functions like po- wer generating, fishing, irrigating to satisfy surrounding dis- tricts. However, The Colorado River has been drying up in recent years. Most people believe that the reason why water level of the river is lowering is because the dams have drained too much water. Is that so? This article will answer such a question by taking the Glen Canyon dam and the Hoover dam as example.

<!-- b000354 | prose | pages [20] -->
The Drying Colorado River Dams should be cautiously extended. tion of water can inevitably result The Colorado River, with a total Because this part of water can be in the accelerated drying of rivers. length of 1,450 miles, derives from used to generate power. Recently, researchers have built a the North Central part of Colorado. Occurrence of Water Shortage – model to simulate the operation of Two famous dams go across the What Will Happen Exactly? the two dams, called the “Double- river – the Glen Canyon Dam and The shortage of rainfalls and the Dam System”. The system mainly the Hoover Dam, both of whom persistent high temperature doe- analyzes the operation of the water have a history for over 80 years. sn’t seem like to change within a extraction for power generation, However, in recent years, the short period of time. Thus, many agriculture, industry and domestic water in the dam shrinks so rapid use. that the basic demand can no people in the southwestern part of the U.S. are concerned about their When the water level of the dams longer meet. Is the construction of demand, which will no longer be maintains normally, about 2.1% of dams that to be condemned? met if such weather continues. The water should be drawn from Lake Actually, proper distribution of “Double-Dam” system. Powell and nearly 1% of water water plays an important role in The researchers use the model to should be drawn from Lake Mead. the water conservation. simulate the drought by assuming Such an extraction calls for accurate Dam Operations – The Secret of that the additional water like rainfall operation of reservoir staffs. For Proper Distribution and water transferred from other them, the water outflows from Lake Undoubtedly, too much extrac- reservoirs is no longer available. The Powell, which flows to Lake Mead, model  indi- cates  that

<!-- b000355 | prose | pages [20, 21] -->
1 Drought and Thirst February 2022

<!-- b000357 | prose | pages [21] -->
service communities of the two after approximately 2 months, the dams – the California, Arizona, water supply will be inadequate.

<!-- b000358 | prose | pages [21] -->
New Mexico, Colorado and Wyo- Moreover, the model also indi- ming states, as their subject. As a cates an interesting phenomenon:

<!-- b000359 | prose | pages [21] -->
result, the water should pre- the water in the Glen Canyon dam ferentially delivered to California, and the Hoover dam periodically fluctuates (see in Figure), which is whose economic development takes up a dominant place among 5 opposite to our common sense. The states. In volume, over 60% of periodic fluctuation may result water should be drawn to Cali- from the self-adjustment of the Figure: The Periodic Fluctuation Schematic fornia state according to the model. reservoir based on the assumptions With respect to utilities, the elec- that there are a certain extra water Should Dams Be Condemned? tricity generation and other general inflows from the upstream of the Ostensibly, the construction of usages both take up for about 50%, Colorado River. water dams does account for the which indicates the importance of Method to Tackle with Water drying process of the Colorado water in power generation. Shortage – What Should We Do? river in a way. However, in an ob- Future Trends – What If Other When the water shortage in jective perspective, it is the climate Measures Are Taken? reservoirs happens, reservoir wor- change that really needs to be con- Nowadays, many environment- kers should respond rapidly to demned, rather than the cons- tally-friendly measures or policies deal with such a situation. truction of reservoirs. are taken. Such as power saving The water is used mainly for Therefore, to bring the water policy, measures for developing agriculture, industry, people’s dai- ly life and power generation. In a new energies, etc. level of Colorado River back up, not only the efforts of reservoir With respect to the researcher’s word, the utility of water is mostly managers make sense. Actually, it model, the result is rather negative for economic growth. When shor- is the efforts of the whole society to – the predicted demand won’t in- tage occurs, to ensure the normal protect the environment.  ◼ crease significantly under these function of the economics is of methods unless these measures are essential importance. Based on this (Editor: Team #2211922) implemented with extreme force. purpose, researchers take the main

<!-- b000360 | prose | pages [21] -->
2

<!-- b000361 | furniture | pages [22] -->
Team 2211922

<!-- b000362 | furniture | pages [22] -->
Page 21

<!-- b000363 | heading | pages [22] -->
9 Appendix

<!-- b000364 | heading | pages [22] -->
9.1 References

<!-- b000365 | references | pages [22] -->
[1] Manli H., Jian Z., Dafa D., et al. Research on the optimal allocation of regional water resources

<!-- b000366 | references | pages [22] -->
based on genetic algorithm [J]. People’s Yangtze River, 2008, 39(6):4.

<!-- b000367 | references | pages [22] -->
[2] SEDS, EIA, U.S. Energy Information Administration, https://www.eia.gov/

<!-- b000368 | references | pages [22] -->
[3] USDA National Agricultural Statistics Service Information, https://www.nass.usda.gov/

<!-- b000369 | references | pages [22] -->
[4] Data USA, https://datausa.io/

<!-- b000370 | references | pages [22] -->
[5] Xuemin. C. Glen Canyon Hydropower Station in the United States[J]. Water Conservancy and

<!-- b000371 | references | pages [22] -->
Hydropower Technology, 1960(3):59-60.

<!-- b000372 | references | pages [22] -->
[6] Zhenghua.

<!-- b000373 | references | pages [22] -->
L. The Hoover Dam in the United States [J].

<!-- b000374 | references | pages [22] -->
Management and Management,

<!-- b000375 | references | pages [22] -->
1999(10):46.

<!-- b000376 | heading | pages [22] -->
9.2 The Method of Solving the Water Volume Changes

<!-- b000377 | prose | pages [22] -->
The original equations can be abstracted into the following problem:

<!-- b000378 | prose | pages [22] -->
𝑎𝑛= 𝐴𝑎𝑛−1 + 𝐵𝑏𝑛−1 + 𝐶 𝑏𝑛= 𝐷𝑎𝑛−1 + 𝐸𝑏𝑛−1 + 𝐹 Objective: Given 𝑎0, 𝑏0 and 𝐴𝐸−𝐵𝐷≠0, and 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸≠0 Find the general formula of {𝑎𝑛} and {𝑏𝑛}.

<!-- b000379 | prose | pages [22] -->
Homogenize the original equation 𝐶𝐸−𝐵𝐹 𝐶𝐸−𝐵𝐹 𝑏𝑛−1 + 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹     𝑎𝑛+ 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸= 𝐴 𝑎𝑛−1 + + 𝐵  𝐴𝐸−𝐵𝐷+ 𝐵−𝐸 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸 𝑏𝑛+ 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹 𝐶𝐸−𝐵𝐹 𝑏𝑛−1 + 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹     𝐴𝐸−𝐵𝐷+ 𝐵−𝐸= 𝐷 𝑎𝑛−1 + + 𝐸  𝐴𝐸−𝐵𝐷+ 𝐵−𝐸 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸 𝐴𝐸−𝐵𝐷+𝐵−𝐸, 𝑦𝑛= 𝑏𝑛+ 𝐴𝐹−𝐶𝐷+𝐶−𝐹 𝐶𝐸−𝐵𝐹 Let 𝑥𝑛= 𝑎𝑛+ 𝐴𝐸−𝐵𝐷+𝐵−𝐸, then  𝐴  𝐴 𝑛𝑥0 𝑥𝑛 𝐵  𝑥𝑛−1 𝐵    = ... = = 𝑦𝑛 𝐷 𝐸 𝑦𝑛−1 𝐷 𝐸 𝑦0  𝐴 𝐵  Let M = , then there exists an invertible matrix P, such that: 𝐷 𝐸

<!-- b000380 | prose | pages [22] -->
𝛼  0 𝑃−1𝑀𝑃= 𝛽 0  −𝐵 𝐸−𝛽  Apparently, 𝛼and 𝛽are the 2 eigenvalues of M, and P = , Therefore 𝐴−𝛼 −𝐷

<!-- b000381 | prose | pages [22, 23] -->
𝑛 𝛼 0 M𝑛= 𝑃 𝑃−1 𝛽 0 (𝐴−𝛼)(𝐸−𝛽)𝛽𝑛−𝐵𝐷𝛼𝑛 (𝐸−𝛽)𝐵(𝛼𝑛−𝛽𝑛)  1 = (𝐴−𝑎)𝐷(𝛼𝑛−𝛽𝑛) (𝐴−𝛼)(𝐸−𝛽)𝛼𝑛−𝐵𝐷𝛽𝑛 (𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷 Bring 𝑎𝑛and 𝑏𝑛back to the original fomula, we can get the general formula of {𝑎𝑛} and {𝑏𝑛}

<!-- b000382 | furniture | pages [23] -->
Team 2211922

<!-- b000383 | furniture | pages [23] -->
Page 22

<!-- b000385 | prose | pages [23] -->
𝑎𝑛= (𝐴−𝛼)(𝐸−𝛽)𝛽𝑛−𝐵𝐷𝛼𝑛 𝐶𝐸−𝐵𝐹   𝑎0 + + (𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸 (𝐸−𝛽)𝐵(𝛼𝑛−𝛽𝑛) 𝑏0 + 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹 𝐶𝐸−𝐵𝐹   − (𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000386 | prose | pages [23] -->
(𝐴−𝛼)𝐷(𝛼𝑛−𝛽𝑛) 𝐶𝐸−𝐵𝐹   𝑏𝑛= 𝑎0 + + (𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸 (𝐴−𝛼)(𝐸−𝛽)𝛼𝑛−𝐵𝐷𝛽𝑛 𝑏0 + 𝐴𝐹−𝐶𝐷+ 𝐶−𝐹 −𝐴𝐹−𝐶𝐷+ 𝐶−𝐹   (𝐴−𝛼)(𝐸−𝛽) −𝐵𝐷 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸 𝐴𝐸−𝐵𝐷+ 𝐵−𝐸

<!-- b000387 | heading | pages [23] -->
9.3 Part of Data and Results

<!-- b000388 | heading | pages [23] -->
9.3.1 Data in Section 4.1

<!-- b000389 | prose | pages [23] -->
𝐶𝑖: $56000 𝐶𝑤: $1.21/𝑚3

<!-- b000390 | heading | pages [23] -->
9.3.2 The result in Task 2

<!-- b000391 | prose | pages [23] -->
CA AZ NM CO WY Electricity Generation 88255883 27379684 8757475 19895462 5885614 General Usage 85325544 25959557 23937562 27590832 15559389

<!-- b000392 | heading | pages [23] -->
9.3.3 The result in Task 3

<!-- b000393 | prose | pages [23] -->
The table below represents the water distribution ratio for each state in several aspects.

<!-- b000394 | prose | pages [23] -->
CA AZ NM CO WY Electricity 0.345354 0.042054 0.068108 0.003527 0.052510 Agriculture 0.032067 0.003905 0.006324 0.000327 0.004876 Industry 0.254182 0.030952 0.050128 0.002596 0.038648 Population 0.043506 0.005298 0.008579 0.000444 0.006615

<!-- b000395 | heading | pages [23] -->
9.4 Code for the Optimization Function of Task 1

<!-- b000396 | prose | pages [23, 24] -->
function f = fun1(x,n,A,B,P,M,C) 1 w1 = 0.5; 2 w2 = 1 - w1; 3 an = (P - C./( x(1)+x(2))) .* (1 - x(1) - x(2)).^n + C./(x(1)+x(2)); 4 bn = (x(2).*(1 - x(1) - x(2)).*( (1- x(3) -x(4) ).^n - (1 - x(1) - x(2)).^n 5 )).*(P - C./(x(1)+x(2)))./(x(1) + x(2) - x(3) -x(4)) + (M - (C.*x(2))./( (x(3)+x(4)).*(x(1) + x(2)) )).*(1 - x(3) -x(4) ).^n + (C.*x(2))./((x(3)+x(4)).*(x(1)+x(2)));

<!-- b000397 | furniture | pages [24] -->
Team 2211922

<!-- b000398 | furniture | pages [24] -->
Page 23

<!-- b000400 | prose | pages [24] -->
f1 = abs( A - (an.*x(1) + bn.* x(3)) ) ; 6 f2 = abs( B - (an.*x(2) + bn.* x(4)) ) ; 7 f = w1.*f1 + w2.*f2; 8 end 9

<!-- b000401 | heading | pages [24] -->
9.5 Code of the Genetic Algorithm

<!-- b000402 | prose | pages [24, 25] -->
NP = 200; %% The number of the population which is an even number 1 L = 10; %% Length of genes 2 Pc = 0.8; %% Crossover probability: 0.25 ~ 1 3 Pm = 0.1; %% Mutation probability: 0.001 ~ -5.9 4 G = 1000; %% Inheritance index 5 Xs = ub .* 0.9; %% Upper bound of feasible solution 6 Xx = lb; %% Lower bound of feasible solution 7 f = randi([0,1],NP,L); %% Initialization 8 for i = 1:NP 9 for j = 1:10 10 f(i,j) = Xx(1,j) + (Xs(1,j) - Xx(1,j)).*rand; 11 end 12 end 13 for k = 1:G 14 for i = 1:NP 15 Fit(i) = fun1(f(i,1:10)); 16 end 17 maxFit = max(Fit); 18 minFit = min(Fit); 19 rr = find(Fit == maxFit); 20 fBest = f(rr(1,1),:); % Best gene type for each generation 21 Fit = (Fit - minFit)/(maxFit - minFit); 22 %%%%%The Copy Opration of the Roulette Selection Method%%%%% 23 sum_Fit = sum(Fit); 24 fitvalue = Fit./sum_Fit; 25 fitvalue = cumsum(fitvalue); 26 ms = sort(rand(NP,1)); 27 fiti = 1; 28 newi = 1; 29 while newi <= NP 30 if(ms(newi) < fitvalue(fiti)) 31 nf(newi,:) = f(fiti,:); 32 newi = newi+1; 33 else 34 fiti = fiti+1; 35 end 36 end 37 %%%%Crossover based on probability%%%%% 38 for i = 1:2:NP 39 p = rand; 40 if p <Pc 41 q = rand(1,L); 42 for j = 1:L 43 %%Arith Crossover Algorithm 44 Cross_Temp_1 = nf(i,j).* q(j) + nf(i+1,j) .* (1 - q(j)); 45 Cross_Temp_2 = nf(i+1,j).* q(j) + nf(i,j) .* (1 - q(j)); 46 nf(i,j) = Cross_Temp_1; 47 nf(i+1,j) = Cross_Temp_2; 48 end 49 end 50 end 51 i = 1; 52 while i<=round(NP*Pm) 53 h = randi([1,NP],1,1); 54 for j = 1:round(L*Pc) 55 g = randi([1,L],1,1); 56 nf(h,g) = lb(1,g) + (nf(h,g) - lb(1,g)).*rand; 57 end 58 i = i+1; 59 end 60 f = nf; 61 f(1,:) = fBest; % Find the best individual 62 trace(k) = maxFit; 63 end 64

<!-- b000403 | furniture | pages [25] -->
Team 2211922

<!-- b000404 | furniture | pages [25] -->
Page 24
