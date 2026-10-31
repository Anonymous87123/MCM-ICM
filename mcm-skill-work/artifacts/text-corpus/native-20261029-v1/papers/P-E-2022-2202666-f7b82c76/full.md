# P-E-2022-2202666-f7b82c76

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
2202666

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | prose | pages [1] -->
To Cut or not to Cut, that is the Question

<!-- b000009 | prose | pages [1] -->
The issue of climate change has been a matter of international importance in recent dec- ades. Among them, the reduction of greenhouse gases in the atmosphere, especially carbon dioxide, has been the center of discussion and efforts. There is an urgent challenge to balance the need to harvest trees for forest products to sequester carbon and the need to preserve forests to generate their social value. In this paper, we have developed two models. One is the Forestry Carbon Sequestration model and the other is the Forest Value Evaluation Model.

<!-- b000010 | prose | pages [1] -->
Firstly, in the Forestry Carbon Sequestration model, we calculate the total amount of carbon sequestration of a forest which is an important indicator of ecological value. By calcu- lating the carbon sequestration of living trees and the carbon sequestration of forest products, we measure the forest carbon sequestration separately in part 1 and part 2. In part 1, we con- structed a model of carbon sequestration in living trees with harvesting rate using the idea of area, carbon sequestration capacity of different tree species, and tree age using time series.

<!-- b000011 | prose | pages [1] -->
Secondly, in part 2, we divide forest products into two categories: "in use" and "landfill", and calculate the carbon sequestration of forest products according to their different carbon sequestration characteristics and lifespan using the Dynamic Optimization Programming. Afterwards, we get the maximum carbon sequestration of 𝟖. 𝟔𝟐× 𝟏𝟎𝟗𝐤𝐠.

<!-- b000012 | prose | pages [1] -->
Thirdly, in Forest Value Evaluation Model, we design a three-dimension evaluation sys- tem of forest value – ESE Model and offer various forest management plans fitted for different forest conditions. We choose three indexes, including six indicators, and then calculate their value using real data – a sample of 186 forests worldwide. Next, we use the metric formula to non-dimensionalize them into a consistent evaluation criterion.

<!-- b000013 | prose | pages [1] -->
Next, by applying the AHP method and K-means Algorithm, we determine all parame- ters in the model and propose evaluation criteria for the final score. In order to making the appropriate program, we use the GE matrix. In this model, we also offer a series of forest management plans which is a criterion of decision making as well. Based on the final resulting scores, we determine an appropriate harvesting program for the forest.

<!-- b000014 | prose | pages [1] -->
Finally, we choose Beijing as the target forest and employ our model in the case study. The total amount of carbon sequestration in 100 years is 𝟏. 𝟎𝟖× 𝟏𝟎𝟏𝟎𝐤𝐠. The actual score of Bei- jing Forest was calculated to be 4.0677. Thus, we obtain the result that Beijing needs the best harvesting rate of 0.06% and the interval of 30 years. This has implications for Beijing's forests, which have no fixed harvesting cycle in recent decades.

<!-- b000015 | prose | pages [1] -->
At the end of our paper, we evaluate our model by analyze the sensitivity and determine its strength and weakness.

<!-- b000016 | furniture | pages [1] -->


<!-- b000017 | keywords | pages [1] -->
Keywords: Carbon Sequestration; Forestry Carbon Sequestration Model；Forest Value Evalu-

<!-- b000018 | prose | pages [1] -->
ation Model; Forest management

<!-- b000019 | heading | pages [2] -->
Contents

<!-- b000020 | contents | pages [2] -->
1 Introduction ............................................................................................ 3

<!-- b000021 | contents | pages [2] -->
1.1 Problem Background ........................................................................................... 3

<!-- b000022 | contents | pages [2] -->
1.2 Our Work .............................................................................................................. 3

<!-- b000023 | contents | pages [2] -->
2 Assumptions and Justifications ............................................................ 4

<!-- b000024 | contents | pages [2] -->
3 Notations ................................................................................................. 5

<!-- b000025 | contents | pages [2] -->
4 Forestry Carbon Sequestration Model ................................................ 5

<!-- b000026 | contents | pages [2] -->
4.1 Part 1: Carbon Sequestration of Living Wood ..................................................... 6

<!-- b000027 | contents | pages [2] -->
4.2 Part 2: Carbon Sequestration of Forest Products ................................................. 8

<!-- b000028 | contents | pages [2] -->
4.3 Dynamic Optimization Process ............................................................................ 9

<!-- b000029 | contents | pages [2] -->
5 Forest Value Evaluation Model .......................................................... 10

<!-- b000030 | contents | pages [2] -->
5.1 ESE Model ......................................................................................................... 11

<!-- b000031 | contents | pages [2] -->
5.1.1 Ecological Values ..................................................................................... 11

<!-- b000032 | contents | pages [2] -->
5.1.2 Social Values............................................................................................. 12

<!-- b000033 | contents | pages [2] -->
5.1.3 Economic Values ...................................................................................... 12

<!-- b000034 | contents | pages [2] -->
5.2 Assessment Process ............................................................................................ 12

<!-- b000035 | contents | pages [2] -->
5.3 Decision-making analysis .................................................................................. 14

<!-- b000036 | contents | pages [2] -->
6 Case Study: Beijing .............................................................................. 15

<!-- b000037 | contents | pages [2] -->
6.1 Forestry Carbon Sequestration Model ............................................................... 15

<!-- b000038 | contents | pages [2] -->
6.2 Forest Value Evaluation Model .......................................................................... 16

<!-- b000039 | contents | pages [2] -->
7 Model Evaluation ................................................................................. 17

<!-- b000040 | contents | pages [2] -->
7.1 Sensitivity Analysis ............................................................................................ 17

<!-- b000041 | contents | pages [2] -->
7.2 Strengths and Weaknesses ................................................................................. 18

<!-- b000042 | contents | pages [2] -->
8 Conclusion ............................................................................................ 18

<!-- b000043 | contents | pages [2] -->
9 Newspaper Article ................................................................................ 19

<!-- b000044 | contents | pages [2] -->
References ................................................................................................ 21

<!-- b000045 | furniture | pages [2] -->


<!-- b000046 | heading | pages [3] -->
1 Introduction

<!-- b000047 | heading | pages [3] -->
1.1 Problem Background

<!-- b000048 | prose | pages [3] -->
Climate change has long been recognized by the international community as one of the major global environmental issues. Greenhouse gases produced by human activ- ities, such as carbon dioxide (CO2) and methane (CH4), have seriously affected the chemical composition of the atmosphere. With their strong ability to absorb infrared radiation, they have caused the rise both in the average temperature of the earth's sur- face and in sea level year by year, inducing incalculable damage to mankind. Therefore, using forests, especially forest products, to absorb and sequestrate atmospheric carbon dioxide is an effective and practical way to reduce greenhouse gases. In a forest eco- system, the carbon cycle can be divided into four stages [1], as shown in the figure below.

<!-- b000049 | furniture | pages [3] -->


<!-- b000050 | furniture | pages [3] -->


<!-- b000051 | furniture | pages [3] -->


<!-- b000052 | furniture | pages [3] -->


<!-- b000053 | furniture | pages [3] -->


<!-- b000054 | furniture | pages [3] -->


<!-- b000055 | furniture | pages [3] -->


<!-- b000056 | furniture | pages [3] -->


<!-- b000057 | furniture | pages [3] -->


<!-- b000058 | furniture | pages [3] -->


<!-- b000059 | furniture | pages [3] -->


<!-- b000060 | furniture | pages [3] -->


<!-- b000061 | furniture | pages [3] -->


<!-- b000062 | furniture | pages [3] -->


<!-- b000063 | caption | pages [3] -->
Figure 1: The carbon cycle

<!-- b000064 | furniture | pages [3] -->


<!-- b000065 | prose | pages [3] -->
The first stage is the absorption of carbon dioxide by the forest through photosyn- thesis. The second stage is tree cutting, where part of it becomes logs to be used for the production of HWP (harvested wood products) and the remainder will rot or burn to release the organic carbon in it. The third stage is the wood use stage, where the amount of carbon sequestered by logs in the production of HWP is also lost in the form of carbon dioxide, but the HWP represented by durable wood products will slowly release its stored organic carbon over a longer period of time. The fourth stage is the disposal stage of HWP, when the discarded HWP enters the landfill and the carbon sequestration will be permanently maintained.

<!-- b000066 | furniture | pages [3] -->


<!-- b000067 | heading | pages [3] -->
1.2 Our Work

<!-- b000068 | prose | pages [3] -->
It is possible to achieve more carbon sequestration over time attributable to the sum

<!-- b000069 | prose | pages [4] -->
of carbon sequestration in forest products derived from deforestation and carbon se- questration generated by the young forests. We have developed a forest management decision model based on an eco-environmental conservation perspective which con- tains the social value of forests while ensuring that forests and forest products sequester as much carbon as possible.

<!-- b000070 | prose | pages [4] -->
First, as forest managers, we decide to transform the forest by means of controlling the rate of cutting trees. In model 1, we construct a model for calculating the carbon sequestration. The amount of carbon sequestered in a defined forest is determined by the living trees and the forest products made from the harvested trees.

<!-- b000071 | prose | pages [4] -->
Then, we design a three-dimension evaluation system of forest value – ESE Model. We classify forest values into the following three dimensions: ecological values, social values and economic values, and six subsets in detail. We quantify the qualitative indi- cators first and then process the dataset. Using K-means Algorithm, we obtain the weight of every indicator. After assigning scores to each of them, we get GE matrix for the ESE Model.

<!-- b000072 | prose | pages [4] -->
Finally, we introduce Beijing as a real case to derive suitable forest management scenarios with the help of Model 1, Model 2 and real data, and discuss the selection of scenarios in the case of increasing harvest intervals.

<!-- b000073 | furniture | pages [4] -->


<!-- b000074 | caption | pages [4] -->
Figure 2: Structure of our paper

<!-- b000075 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000076 | prose | pages [4] -->
To simplify the problem, we make the following basic assumptions, each of which is properly justified. Other assumptions based on different models will be listed in the following model-related sections.

<!-- b000077 | furniture | pages [4] -->


<!-- b000078 | prose | pages [4] -->
Assumption 1: All woods in the topic are primary forests. Justification: Planted forests are those who have been artificially selected and culti- vated for profitable purposes. They are subject to high anthropogenic interference and cannot be used for carbon sequestration. Therefore, we only consider primary forests.

<!-- b000079 | furniture | pages [5] -->


<!-- b000080 | prose | pages [5] -->
Assumption 2: Different tree species depends on their geographical locations. Justification: The geographical location of the forest determines the light, rainfall, soil, temperature, and other environmental characteristics of the area, which determine the species of native plants.

<!-- b000081 | furniture | pages [5] -->


<!-- b000082 | prose | pages [5] -->
Assumption 3: The age of trees in primary forests shows a uniform distribution and the age distributions of all forests are the same. Justification: In the absence of extreme climatic and geological conditions changes, the birth and death rates of trees remain at constant levels. Because of the high surviv- ability, we assume that in general trees do not die unexpectedly in the middle of their life cycle or have negligibly low unexpected rates of mortality.

<!-- b000083 | furniture | pages [5] -->


<!-- b000084 | prose | pages [5] -->
Assumption 4: Only the age of the tree is considered when cutting down trees, not the type or location of the tree, and the maturity threshold is constant for all tree species. Justification: Trees will strike a balance between respiration and photosynthesis at ma- turity, when the net production of organic carbon is zero. Mature trees are unable to provide more carbon sequestration as living trees and are therefore cut down. Forest maturity thresholds are usually in the range of 80 to 100 years.[2] To simplify the cal- culation process, we reckon a fixed maturity threshold for all types of trees.

<!-- b000085 | furniture | pages [5] -->


<!-- b000086 | heading | pages [5] -->
3 Notations

<!-- b000087 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000088 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000089 | heading | pages [5] -->
Symbol

<!-- b000090 | prose | pages [5] -->
Definition i Time (year) The harvesting rate 𝛼 t The age of trees j The type of trees The amount of carbon sequestration C(𝑖) Living forest surface area LFS(𝑖) Harvested forest surface area HFS(𝑖) Total forest surface area TFS(𝑖) The carbon sequestration capacity 𝐷(𝑡) The probability distribution of age 𝑎𝑔𝑒(𝑡) The conversion factor 𝛾 The actual value 𝐼𝑚 The metric values 𝐸𝑚

<!-- b000091 | furniture | pages [5] -->


<!-- b000092 | heading | pages [5] -->
4 Forestry Carbon Sequestration Model

<!-- b000093 | prose | pages [5] -->
For ecological conservation purposes, our primary goal in forest management is

<!-- b000094 | prose | pages [6] -->
to ensure that carbon sequestration is maximized. The amount of carbon sequestered in a defined forest is determined by the living trees and the forest products made from the harvested trees. We measure the forest carbon sequestration by calculating the carbon sequestration of living trees and the carbon sequestration of forest products separately, and then find the forest management plan with the largest carbon sequestration.

<!-- b000095 | prose | pages [6] -->
We separate the model of total carbon sequestration into two parts, the first part is the living wood carbon sequestration and the second part is the forest product carbon sequestration. Total carbon sequestration amount in year i can be expressed as

<!-- b000096 | prose | pages [6] -->
𝐶𝑡(𝑖) = 𝐶𝑙(𝑖) + 𝐶𝑝(𝑖) (1) Where 𝐶𝑡(𝑖) represents the total amount of carbon sequestration, 𝐶𝑙(𝑖) repre- sents the carbon sequestration amount of living wood and 𝐶𝑝(𝑖) represents the car- bon sequestration amount of forest products.

<!-- b000097 | prose | pages [6] -->
The diagram below demonstrates the frame of the Forestry Carbon Sequestration Model. The total amount of carbon sequestered in year i is given by the living wood carbon sequestration and the forest product carbon sequestration in that year. The young trees will continue to grow in the following years, while the mature trees will be harvested to manufacture forest products. Forest products are generally classified into four categories based on their carbon sequestration forms, which are in use, land- fill, energy and emission.[3] Since the carbon stored in the parts of energy and emis- sion will be released in the short term as carbon dioxide, we do not count it in the car- bon sequestration amount of forest products. The life cycle of carbon in forest prod- ucts in use follows the half-life while the amount of carbon in landfill maintains in the long time.

<!-- b000098 | furniture | pages [6] -->


<!-- b000099 | caption | pages [6] -->
Figure 3: The flow chart of Forestry Carbon Sequestration Model

<!-- b000100 | furniture | pages [6] -->


<!-- b000101 | heading | pages [6] -->
4.1 Part 1: Carbon Sequestration of Living Wood

<!-- b000102 | prose | pages [6] -->
In the first part of the model, we consider that the amount of carbon sequestered by existing wood is determined by the living forest surface area (𝐿𝐹𝑆(𝑖)), the carbon

<!-- b000103 | prose | pages [7] -->
sequestration capacity of trees (𝐷(𝑡)), and the probability distribution of trees at differ- ent age in the forest (𝑎𝑔𝑒(𝑡)).

<!-- b000104 | prose | pages [7] -->
The area of forest remaining in year i is determined by the current year's harvesting rate and the area of forest remaining in the previous years. The harvested forest surface area (HFS) equals to the product of the harvesting rate (𝛼) and the total forest surface area (TFS) for the year. The total forest area of next year is equal to the living forest surface area (LFS) of the current year.

<!-- b000105 | prose | pages [7] -->
Here, all the above areas as projected areas. Since trees can be planted on slopes, and it has been proved that the larger the angle of a slope is, the greater the carbon sequestration capacity is.[4] Therefore, we divide the existing area data by 𝑐𝑜𝑠𝜃 to obtain the slope area, 𝜃 is the degree of the slope. The slope can be divided into five levels, which are flat, gentle, slant, steep, sharp and extreme slope, corresponding to 0- 5°, 6°-15°, 16°-25°, 26°-35° and 36°-45°.

<!-- b000106 | prose | pages [7] -->
They can be expressed respectively as

<!-- b000107 | prose | pages [7] -->
𝐻𝐹𝑆(𝑖) = 𝛼× 𝑇𝐹𝑆(𝑖)

<!-- b000108 | prose | pages [7] -->
(2)

<!-- b000109 | furniture | pages [7] -->


<!-- b000110 | prose | pages [7] -->
𝑐𝑜𝑠𝜃

<!-- b000111 | furniture | pages [7] -->


<!-- b000112 | prose | pages [7] -->
𝐿𝐹𝑆(𝑖) = (1 −𝑎) × 𝑇𝐹𝑆(𝑖)

<!-- b000113 | furniture | pages [7] -->


<!-- b000114 | prose | pages [7] -->
(3) 𝑐𝑜𝑠𝜃

<!-- b000115 | prose | pages [7] -->
Our study begins with only one tree type: aspen. Now, we define the carbon content

<!-- b000116 | furniture | pages [7] -->


<!-- b000117 | prose | pages [7] -->
in living trees per unit area as the carbon sequestration capacity (𝐷(𝑡)). Figure 4 depicts the change of 𝐷(𝑡) over five different phases. It can be clear seen that the carbon se- questration capacity increases at the beginning and reaches the peak in mature period approximately, and then begins to fall considerably. Therefore, in order to sequester as much carbon as possible, we fell only overmature trees and the cutting age is 81. The fitted curve of carbon sequestration capacity of tree age is expressed as

<!-- b000118 | prose | pages [7] -->
(4)

<!-- b000119 | prose | pages [7] -->
𝐷(𝑡) = 𝑎𝑒(−(𝑡−𝑏

<!-- b000120 | prose | pages [7] -->
𝑐)2)

<!-- b000121 | prose | pages [7] -->
among this, a, b, c are parameters of the fitted function.

<!-- b000122 | furniture | pages [7] -->


<!-- b000123 | furniture | pages [7] -->


<!-- b000124 | furniture | pages [7] -->


<!-- b000125 | caption | pages [7] -->
Figure 4: The relationship between age and carbon sequestration capacity

<!-- b000126 | furniture | pages [7] -->


<!-- b000127 | prose | pages [8] -->
According to assumption 3 and 4, the age of trees in primary forests shows a con-

<!-- b000128 | furniture | pages [8] -->


<!-- b000129 | prose | pages [8] -->
stant uniform distribution in observation period. This indicates that the number of trees in the immature stage of the forest is constant and the number of trees in the ma- ture stage is influenced only by the harvesting rate. We define 𝛽 as the maturation rate and thus the proportion of the immature trees in the current year equals to 1 −𝛽. We can obtain that the probability distribution of age can be expressed as

<!-- b000130 | prose | pages [8] -->
𝑎𝑔𝑒(𝑡) =

<!-- b000131 | prose | pages [8] -->
(5)

<!-- b000132 | prose | pages [8] -->
1

<!-- b000133 | furniture | pages [8] -->


<!-- b000134 | prose | pages [8] -->
(1 −𝛼

<!-- b000135 | prose | pages [8] -->
𝛽)𝑡𝛽+ (1 −𝛽)

<!-- b000136 | prose | pages [8] -->
Tree species vary from forest to forest, so we introduce j as the type of trees. Meanwhile, we set the time horizon range to 100 years. In this way, we can express the amount of carbon sequestered by living trees and harvested trees in the forest in year i as

<!-- b000137 | prose | pages [8] -->
100

<!-- b000138 | prose | pages [8] -->
𝑛

<!-- b000139 | furniture | pages [8] -->


<!-- b000140 | prose | pages [8] -->
(6)

<!-- b000141 | prose | pages [8] -->
𝑎𝑔𝑒(𝑡)

<!-- b000142 | prose | pages [8] -->
𝐶𝑙(𝑖) = ∑∑𝐷𝑗(𝑡)𝐿𝐹𝑆𝑗(𝑖)

<!-- b000143 | prose | pages [8] -->
𝑡=1

<!-- b000144 | prose | pages [8] -->
𝑗=1

<!-- b000145 | prose | pages [8] -->
100

<!-- b000146 | prose | pages [8] -->
𝑛

<!-- b000147 | furniture | pages [8] -->


<!-- b000148 | prose | pages [8] -->
(7)

<!-- b000149 | prose | pages [8] -->
𝑎𝑔𝑒(𝑡)

<!-- b000150 | prose | pages [8] -->
𝐶ℎ(𝑖) = ∑∑𝐷𝑗(𝑡)𝐻𝐹𝑆𝑗(𝑖)

<!-- b000151 | prose | pages [8] -->
𝑡=81

<!-- b000152 | prose | pages [8] -->
𝑗=1

<!-- b000153 | prose | pages [8] -->
Substituting equation (3), (4) and (5) into (6), we get equation (8)

<!-- b000154 | furniture | pages [8] -->


<!-- b000155 | furniture | pages [8] -->


<!-- b000156 | prose | pages [8] -->
100

<!-- b000157 | prose | pages [8] -->
𝑛

<!-- b000158 | prose | pages [8] -->
𝐶𝑙(𝑖) = ∑∑𝐷𝑗(𝑡)

<!-- b000159 | prose | pages [8] -->
𝑡=1

<!-- b000160 | prose | pages [8] -->
𝑗=1

<!-- b000161 | furniture | pages [8] -->


<!-- b000162 | prose | pages [8] -->
(1 −𝑎) × 𝑇𝐹𝑆𝑗(𝑖)

<!-- b000163 | prose | pages [8] -->
(8)

<!-- b000164 | furniture | pages [8] -->


<!-- b000165 | prose | pages [8] -->
𝑐𝑜𝑠𝜃[(1 −𝛼

<!-- b000166 | prose | pages [8] -->
𝛽)𝑡𝛽+ (1 −𝛽)]

<!-- b000167 | prose | pages [8] -->
Equation (8) is the amount of carbon sequestration of living wood.

<!-- b000168 | furniture | pages [8] -->


<!-- b000169 | furniture | pages [8] -->


<!-- b000170 | heading | pages [8] -->
4.2 Part 2: Carbon Sequestration of Forest Products

<!-- b000171 | prose | pages [8] -->
In the second part of ModelⅠ, we study the carbon sequestration of forest prod- ucts. In our model, we assume that the forest cut in the specific year becomes products currently.

<!-- b000172 | prose | pages [8] -->
The amount of carbon sequestered by forest products in year i consists of the

<!-- b000173 | furniture | pages [8] -->


<!-- b000174 | prose | pages [8] -->
amount of carbon sequestered by currently produced forest products in that year and the amount of carbon sequestered by the accumulation of retained forest products in previous years, which can be expressed as

<!-- b000175 | prose | pages [8] -->
𝐶𝑝(𝑖) = 𝐶𝑐𝑢𝑟𝑟𝑒𝑛𝑡(𝑖) + 𝐶𝑢𝑠𝑒(𝑖) + 𝐶𝑙𝑎𝑛𝑑𝑓𝑖𝑙𝑙(𝑖) (9)

<!-- b000176 | prose | pages [8] -->
where 𝐶𝑢𝑠𝑒(𝑖) represents the accumulated carbon sequestration of forest products in use in previous years and 𝐶𝑙𝑎𝑛𝑑𝑓𝑖𝑙𝑙(𝑖) represents the accumulated carbon sequestration of discarded forest products in previous years.

<!-- b000177 | prose | pages [8] -->
Define k as the productivity of using logged wood to produce forest products. We

<!-- b000178 | furniture | pages [8] -->


<!-- b000179 | prose | pages [8] -->
use the equation (7) in part 1 derive the amount of carbon sequestered by currently produced forest products, which can be expressed as

<!-- b000180 | prose | pages [8] -->
(10) 𝐶𝑐𝑢𝑟𝑟𝑒𝑛𝑡(𝑖) = 𝑘× 𝐶ℎ(𝑖)

<!-- b000181 | prose | pages [8] -->
Since all of the harvested wood will be processed into forest products, we set two

<!-- b000182 | furniture | pages [8] -->


<!-- b000183 | prose | pages [8] -->
weight coefficients 𝜔1 and 𝜔2 for products in use and in landfill separately, where

<!-- b000184 | prose | pages [9] -->
the sum of 𝜔1 and 𝜔2 equals to 1.

<!-- b000185 | prose | pages [9] -->
For the accumulated carbon sequestration of forest products in use in previous years, the lifetime of carbon in forest products follows the half-life (T). The rate of carbon emission is related to the use and service life of the product. Forest products are divided into hardwood products and paper products, which have the half-life of 30 years and 2 years, respectively.

<!-- b000186 | furniture | pages [9] -->


<!-- b000187 | prose | pages [9] -->
𝑖−1

<!-- b000188 | prose | pages [9] -->
𝐶𝑢𝑠𝑒(𝑖) = ∑𝜔1𝐶𝑐𝑢𝑟𝑟𝑒𝑛𝑡(𝑟−1) × (1

<!-- b000189 | prose | pages [9] -->
𝑟=1

<!-- b000190 | prose | pages [9] -->
[𝑖−(𝑟−1)]

<!-- b000191 | prose | pages [9] -->
(11)

<!-- b000192 | furniture | pages [9] -->


<!-- b000193 | prose | pages [9] -->
2)

<!-- b000194 | prose | pages [9] -->
𝑇

<!-- b000195 | prose | pages [9] -->
Carbon in landfill can be preserved over a long period of time, hence the accumu-

<!-- b000196 | furniture | pages [9] -->


<!-- b000197 | prose | pages [9] -->
lated carbon sequestration of discarded forest products in previous years can be ex- pressed as

<!-- b000198 | prose | pages [9] -->
𝑖 𝑖

<!-- b000199 | prose | pages [9] -->
(12)

<!-- b000200 | furniture | pages [9] -->


<!-- b000201 | prose | pages [9] -->
𝐶𝑙𝑎𝑛𝑑𝑓𝑖𝑙𝑙(𝑖) = ∑𝜔2𝐶𝑐𝑢𝑟𝑟𝑒𝑛𝑡(𝑟−1)

<!-- b000202 | prose | pages [9] -->
𝑟=1

<!-- b000203 | furniture | pages [9] -->


<!-- b000204 | heading | pages [9] -->
4.3 Dynamic Optimization Process

<!-- b000205 | prose | pages [9] -->
The solution to the problem is dynamic optimization, taking a particular forest as an example (The parameters of an ideal forest are generated by random numbers [5]). The range of strategies for forest cutting plans includes the harvesting rate (𝛼) of 0.1%, 0.3%, 0.5%, 0.7%, 0.9%. Setting the time horizon range to 100 years, we consider the forest cutting decision for each of these years. Since our 𝛼 is small, the ideal solution in this problem does not include the harvesting interval.

<!-- b000206 | prose | pages [9] -->
Using the curve in equation (4), fitted result is as a = 17.86, b = 69.65, c = 67.76. According to the announcement published by China Forestry Administration, since the average harvesting intensity of commercial forests is no more than 35% and the average harvesting intensity of public welfare forests is no more than 20% while the rotation cycle is about 49 years. We set the total harvesting rate for 100 years not to exceed 50%.

<!-- b000207 | prose | pages [9] -->
We set the initial forest area as 17.98 × 104 hm2 (area of primary forest in Bei- jing, 2014), with 𝑘= 0.6, 𝜔1 = 0.7 and 𝜔2 = 0.3. Our purpose is to maximize the carbon sequestration in year i. Thus, we get

<!-- b000208 | prose | pages [9] -->
max 𝐶𝑡(𝑖) = 𝐶𝑙(𝑖) + 𝐶𝑝(𝑖)

<!-- b000209 | prose | pages [9] -->
100

<!-- b000210 | prose | pages [9] -->
(13)

<!-- b000211 | furniture | pages [9] -->


<!-- b000212 | prose | pages [9] -->
s. t. ∑𝛼𝑖≤50%

<!-- b000213 | prose | pages [9] -->
i=1

<!-- b000214 | prose | pages [9] -->
𝛼𝑖 = 0.1%, 0.3%, 0.5%, 0.7%, 0.9%

<!-- b000215 | prose | pages [9] -->
Each year of harvesting rate selection 𝛼𝑖  will change the carbon sequestration

<!-- b000216 | furniture | pages [9] -->


<!-- b000217 | prose | pages [9] -->
𝐶𝑡(𝑖) in that year and each stage of 𝐶𝑡(𝑖) depends on the state variable 𝐶𝑡(𝑖) in the previous period and the decision variable 𝛼𝑖 in the current period.

<!-- b000218 | furniture | pages [10] -->


<!-- b000219 | furniture | pages [10] -->


<!-- b000220 | furniture | pages [10] -->


<!-- b000221 | furniture | pages [10] -->


<!-- b000222 | furniture | pages [10] -->


<!-- b000223 | caption | pages [10] -->
Figure 5: Solving process of the maximum carbon sequestration

<!-- b000224 | furniture | pages [10] -->


<!-- b000225 | prose | pages [10] -->
The annual harvesting plan is as below. Figure 5 shows the harvesting rate in the particular forest over a period of 100 years. Each dot represents The results of Mode l present the cyclical nature of the harvesting rate. The model embodies the ideal har- vesting schedule for a harvesting cycle of approximately 20 years with alternating high and low harvesting rates.

<!-- b000226 | furniture | pages [10] -->


<!-- b000227 | caption | pages [10] -->
Figure 6: Annual harvesting plan

<!-- b000228 | furniture | pages [10] -->


<!-- b000229 | prose | pages [10] -->
We use the algorithm of dynamic programming to solve for the maximum carbon sequestration in 100 years, and the process of the solution is sketched out in Figure 4. The maximum carbon sequestration is 8.62 × 109kg.

<!-- b000230 | furniture | pages [10] -->


<!-- b000231 | heading | pages [10] -->
5 Forest Value Evaluation Model

<!-- b000232 | prose | pages [10] -->
The value of the forest goes beyond the absorption of carbon dioxide and has an impact on various aspects of the lives of the people around it. With a high percentage of the world's forest area, its added value cannot be ignored.

<!-- b000233 | furniture | pages [10] -->


<!-- b000234 | furniture | pages [11] -->


<!-- b000235 | furniture | pages [11] -->


<!-- b000236 | caption | pages [11] -->
Figure 7: Global Forest Distribution

<!-- b000237 | furniture | pages [11] -->


<!-- b000238 | prose | pages [11] -->
In the second model, we include multiple forms of forest values, including carbon sequestration, in an attempt to determine the best management plan for a forest by find- ing a ubiquitously applicable evaluation mechanism.

<!-- b000239 | furniture | pages [11] -->


<!-- b000240 | heading | pages [11] -->
5.1 ESE Model

<!-- b000241 | prose | pages [11] -->
To better measure the form of forest values in different dimensions, we choose Analytical Hierar- chy Process. It assigns separate scores to the subjec- tive indicators and then weights them to arrive at a composite score of a forest, and finally determines the management plan to be selected for the forest based on the composite score. We classify the value of forests into three dimensions, namely ecological values, social values and economic values.

<!-- b000242 | caption | pages [11] -->
Figure 8: ESE Model

<!-- b000243 | furniture | pages [11] -->


<!-- b000244 | prose | pages [11] -->
We define VI (Value Index) as ten-point system value index obtained by cluster analysis. In order to quantify the metrics of different dimensions as scores under the same criteria, we introduce conversion factor 𝛾. The highest value index in the value type is the maximum value index for that value type. They indicate the importance of different values, and the higher the value, the greater the VI.

<!-- b000245 | furniture | pages [11] -->


<!-- b000246 | heading | pages [11] -->
5.1.1 Ecological Values

<!-- b000247 | prose | pages [11] -->
Ecological values include the value of carbon sequestration and the value of biodi- versity. Carbon sequestration value index measures the importance of total carbon se- questration which derives from real data. The higher scores of ecological values we get, the more we have to protect the forest, rather than felling the trees. In addition, we select the average biomass in a forest as measurement of biodiversity value. They can be ex- pressed as follows.

<!-- b000248 | prose | pages [12] -->
𝑉𝐼𝐶= 𝛾1 × 𝐶𝑡

<!-- b000249 | prose | pages [12] -->
(14) TFS

<!-- b000250 | prose | pages [12] -->
(15)

<!-- b000251 | prose | pages [12] -->
𝑉𝐼𝑏𝑖𝑜𝑑𝑖𝑣𝑒𝑟𝑠𝑖𝑡𝑦= 𝛾2 × 𝑏𝑖𝑜𝑚𝑎𝑠𝑠

<!-- b000252 | furniture | pages [12] -->


<!-- b000253 | heading | pages [12] -->
5.1.2 Social Values

<!-- b000254 | furniture | pages [12] -->


<!-- b000255 | prose | pages [12] -->
TFS

<!-- b000256 | prose | pages [12] -->
Social values include recreational value, cultural value and therapeutic value, which is the positive emotional value that the forest brings to the people in the sur- rounding area. The higher the social values, the more the forest should be protected. Recreational value, cultural value and therapeutic value can be expressed as below.

<!-- b000257 | prose | pages [12] -->
(16) 𝑉𝐼𝑟𝑒𝑐𝑟𝑒𝑎𝑡𝑖𝑜𝑛= 𝛾3 × 𝑎𝑛𝑛𝑢𝑎𝑙 𝑣𝑖𝑠𝑖𝑡𝑠 𝑡𝑜 𝑡ℎ𝑒 𝑓𝑜𝑟𝑒𝑠𝑡

<!-- b000258 | prose | pages [12] -->
𝑉𝐼𝑐𝑢𝑙𝑡𝑢𝑟𝑒= 𝛾4 × 𝑝𝑒𝑟 𝑐𝑎𝑝𝑖𝑡𝑎 𝑒𝑥𝑝𝑒𝑛𝑑𝑖𝑡𝑢𝑟𝑒 𝑜𝑓 𝑟𝑒𝑠𝑖𝑑𝑒𝑛𝑡𝑠 𝑜𝑛 𝑐𝑢𝑙𝑡𝑢𝑟𝑎𝑙 𝑐𝑜𝑛𝑠𝑢𝑚𝑝𝑡𝑖𝑜𝑛 (17)

<!-- b000259 | prose | pages [12] -->
(18) 𝑉𝐼𝑡ℎ𝑒𝑟𝑎𝑝𝑦= 𝛾5 × 𝑎𝑣𝑒𝑟𝑎𝑔𝑒 𝑙𝑖𝑓𝑒 𝑒𝑥𝑝𝑒𝑐𝑡𝑎𝑛𝑐𝑦 𝑜𝑓 𝑟𝑒𝑠𝑖𝑑𝑒𝑛𝑡𝑠

<!-- b000260 | furniture | pages [12] -->


<!-- b000261 | heading | pages [12] -->
5.1.3 Economic Values

<!-- b000262 | prose | pages [12] -->
Economic values include forest product value and tourism value which together are called profitable value. The economic values of forests refer to the monetarily meas- urable wealth that forests can create for people. Since the value of tourism is difficult to measure, we introduce the concept of opportunity cost in economics. In this case, the opportunity cost paid to achieve the profits of tourism is the revenue of forest products derived from the same area of the forest.

<!-- b000263 | furniture | pages [12] -->


<!-- b000264 | prose | pages [12] -->
𝑉𝐼𝑝𝑟𝑜𝑓𝑖𝑡= 𝛾6 × (𝑡𝑜𝑡𝑎𝑙 𝑎𝑛𝑛𝑢𝑎𝑙 𝑟𝑒𝑣𝑒𝑛𝑢𝑒 𝑓𝑟𝑜𝑚 𝑡𝑜𝑢𝑟𝑖𝑠𝑚 𝑖𝑛𝑑𝑢𝑠𝑡𝑟𝑦

<!-- b000265 | prose | pages [12] -->
(19)

<!-- b000266 | prose | pages [12] -->
− 𝑡𝑜𝑡𝑎𝑙 𝑎𝑛𝑛𝑢𝑎𝑙 𝑟𝑒𝑣𝑒𝑛𝑢𝑒 𝑓𝑟𝑜𝑚 𝑓𝑜𝑟𝑒𝑠𝑡 𝑝𝑟𝑜𝑑𝑢𝑐𝑡𝑠)

<!-- b000267 | furniture | pages [12] -->


<!-- b000268 | heading | pages [12] -->
5.2 Assessment Process

<!-- b000269 | prose | pages [12] -->
For the six indicators in the above three dimensions, we use the metric formula to non-dimensionalize them into a consistent evaluation criterion,

<!-- b000270 | prose | pages [12] -->
𝐼𝑚

<!-- b000271 | prose | pages [12] -->
𝐸𝑚=

<!-- b000272 | prose | pages [12] -->
(19) 𝐼× 100 [6]

<!-- b000273 | prose | pages [12] -->
where 𝐼𝑚 represents the actual value of factor m and 𝐼 represents the value of factor m in the whole area. For instance, recreational value is the annual visitation of the se- lected forest divided by the total annual visitation of the local area and so as remain ones.

<!-- b000274 | prose | pages [12] -->
We select a representative country A for the study because of its large span. Each factor is categorized into 10 classes, by clustering the dataset[7] into ten clusters using the K-means Algorithm. Here we output six scatter plots of different factors (Figure 7) and list the metric values of cluster centers corresponding to each VI (Table 2).

<!-- b000275 | furniture | pages [13] -->


<!-- b000276 | furniture | pages [13] -->


<!-- b000277 | caption | pages [13] -->
Figure 9: The scatter plots with clusters

<!-- b000278 | furniture | pages [13] -->


<!-- b000279 | caption | pages [13] -->
Table 2: VI information based on K-means Algorithm

<!-- b000280 | prose | pages [13] -->
Em

<!-- b000281 | prose | pages [13] -->
carbon biodiversity recreation

<!-- b000282 | prose | pages [13] -->
VI

<!-- b000283 | prose | pages [13] -->
sequestration

<!-- b000284 | prose | pages [13] -->
1 18.61 35.13 2 36.08 75.80 3 44.94 97.97 4 65.93 111.97 5 82.36 153.38 6 119.42 184.33 7 130.25 203.57

<!-- b000285 | prose | pages [13] -->
culture therapy profit

<!-- b000286 | prose | pages [13] -->
4.16 8.81 24.67 3.11 15.56 11.17 48.33 14.00 20.66 18.84 71.57 22.72 29.97 28.78 82.42 30.40 43.22 29.31 110.06 40.98 57.85 33.08 138.87 47.20 63.46 43.71 151.43 53.23

<!-- b000287 | prose | pages [14] -->
8 135.67 257.93 9 147.95 274.74 10 154.26 298.64

<!-- b000288 | furniture | pages [14] -->


<!-- b000289 | furniture | pages [14] -->


<!-- b000290 | prose | pages [14] -->
74.58 47.60 175.75 65.43 81.04 55.00 186.40 71.74 97.63 59.02 196.53 85.96

<!-- b000291 | prose | pages [14] -->
Using AHP, we obtain the weights of each factor in the relative indexes as well as the weights of each of the three indexes. We can calculate the final VI and construct a comprehensive evaluation model. It presents as below.

<!-- b000292 | furniture | pages [14] -->


<!-- b000293 | caption | pages [14] -->
Table 3: Weights of factors determined by AHP

<!-- b000294 | prose | pages [14] -->
Dimension Weight Factor Weight (dimension) Weight

<!-- b000295 | prose | pages [14] -->
carbon sequestration ecology 0.5816 biodiversity

<!-- b000296 | prose | pages [14] -->
recreation

<!-- b000297 | prose | pages [14] -->
society

<!-- b000298 | prose | pages [14] -->
0.1095

<!-- b000299 | prose | pages [14] -->
culture

<!-- b000300 | furniture | pages [14] -->


<!-- b000301 | furniture | pages [14] -->


<!-- b000302 | prose | pages [14] -->
therapy economy 0.3090 profit

<!-- b000303 | prose | pages [14] -->
0.6667 0.3878 0.3333 0.1938

<!-- b000304 | prose | pages [14] -->
0.1283 0.0140 0.2764 0.0303 0.5954 0.0652 1 0.309

<!-- b000305 | furniture | pages [14] -->


<!-- b000306 | prose | pages [14] -->
It was tested that all CRs were <0.10, so the consistency of the judgment matrix A

<!-- b000307 | furniture | pages [14] -->


<!-- b000308 | prose | pages [14] -->
was acceptable. The forest value index can be expressed as

<!-- b000309 | prose | pages [14] -->
𝑉𝐼= 0.5816 × 𝑉𝐼𝑒𝑐𝑜𝑙𝑜𝑔𝑦+ 0.1095 × 𝑉𝐼𝑠𝑜𝑐𝑖𝑒𝑡𝑦+ 0.3090 × 𝑉𝐼𝑒𝑐𝑜𝑛𝑜𝑚𝑦

<!-- b000310 | furniture | pages [14] -->


<!-- b000311 | heading | pages [14] -->
5.3 Decision-making analysis

<!-- b000312 | prose | pages [14] -->
(20)

<!-- b000313 | prose | pages [14] -->
Combining existing forest management measures and the above assumptions, we propose five forest harvesting scenarios for different VI levels. Our harvesting pro- grams include different harvesting rates and harvesting intervals (Δ𝑖) in the case of se- lection cutting.

<!-- b000314 | prose | pages [14] -->
What is worth mentioning is that there is a slight change compared to modelⅠ. To work out the harvesting programs, we regard the cutting process as a cutting cycle that is the time it takes to cut mature trees and keep the remaining trees growing until the total area of the forest returns to the state before cutting. On the basis of cutting cycle, we develop

<!-- b000315 | prose | pages [14] -->
(21) TFS × (1 −𝛼)(1 + 𝑔)Δ𝑖= 𝑇𝐹𝑆

<!-- b000316 | prose | pages [14] -->
After rearrange the formula, we have

<!-- b000317 | prose | pages [14] -->
Δ𝑖= −log (1 −𝛼)

<!-- b000318 | prose | pages [14] -->
(22) log (1 + g)

<!-- b000319 | prose | pages [14] -->
where g represents the annual growth rate of the forests.

<!-- b000320 | prose | pages [14] -->
In order to making the appropriate program, we use the GE (McKinsey Matrix) matrix. Here, we consider using the GE matrix to describe the degree of programs. On the one hand, the value index indicates the comprehensive value of the designated for-

<!-- b000321 | prose | pages [15] -->
est. On the other hand, the harvesting rate reflects the status quo of the forest. There- fore, the GE matrix is introduced here, shown in Figure 8 and two related indicators are defined according to the actual situation.

<!-- b000322 | furniture | pages [15] -->


<!-- b000323 | furniture | pages [15] -->


<!-- b000324 | furniture | pages [15] -->


<!-- b000325 | furniture | pages [15] -->


<!-- b000326 | furniture | pages [15] -->


<!-- b000327 | furniture | pages [15] -->


<!-- b000328 | furniture | pages [15] -->


<!-- b000329 | furniture | pages [15] -->


<!-- b000330 | furniture | pages [15] -->


<!-- b000331 | furniture | pages [15] -->


<!-- b000332 | furniture | pages [15] -->


<!-- b000333 | furniture | pages [15] -->


<!-- b000334 | caption | pages [15] -->
Figure 10: GE metrix of harvesting programs

<!-- b000335 | furniture | pages [15] -->


<!-- b000336 | prose | pages [15] -->
As a result, we find the corresponding 𝛼 and Δ𝑖 listed in Table 3.

<!-- b000337 | furniture | pages [15] -->


<!-- b000338 | caption | pages [15] -->
Table 4: The harvesting programs

<!-- b000339 | prose | pages [15] -->
Ⅱ Program Ⅰ 0.10% 0.08% 𝛼 10 20 Δ𝑖

<!-- b000340 | furniture | pages [15] -->


<!-- b000341 | heading | pages [15] -->
6 Case Study: Beijing

<!-- b000342 | prose | pages [15] -->
Ⅲ Ⅳ Ⅴ 0.06% 0.04% 0.02% 30 40 50

<!-- b000343 | prose | pages [15] -->
We chose Beijing as the first target area because it is the capital of China and has a large forest area with good statistical status. Since Beijing has sacrificed a good eco- logical environment for industrial development in the past decades, in recent years, the government has introduced many relevant forest protection policies to restrict forest harvesting. It is of considerable relevance to study the harvesting strategy of Beijing's forests.

<!-- b000344 | prose | pages [15] -->
In the following subsections, we use our model to predict the total amount of car- bon sequestration and then to improve Beijing’s Forest management plans. After the simulation of our model, we illustrate our modification of Beijing’s current forest policy.

<!-- b000345 | furniture | pages [15] -->


<!-- b000346 | heading | pages [15] -->
6.1 Forestry Carbon Sequestration Model

<!-- b000347 | prose | pages [15] -->
Based on Beijing's forest and forest product manufacturing data, we determined the values of parameters which k = 0.6, 𝜔1 = 0.65, 𝜔2 = 0.35 and TFS =1.79 ∗104 hm2 . Bring the data into the first part for regression, and the fitted pa- rameters for different tree species are shown below.

<!-- b000348 | furniture | pages [15] -->


<!-- b000349 | furniture | pages [15] -->


<!-- b000350 | furniture | pages [15] -->


<!-- b000351 | caption | pages [16] -->
Table 5: Fitted parameters

<!-- b000352 | prose | pages [16] -->
𝑫𝒋(𝒕) a

<!-- b000353 | prose | pages [16] -->
Quercus spp 18.04 Other broadleaved forest 15.32 Broadleaved mixed forest 19.03 Platycladus orientalist 12.18 Populus spp 19.17 Betula spp 11.62 Coniferous and Broadleaved

<!-- b000354 | prose | pages [16] -->
13.45 mixed forest

<!-- b000355 | prose | pages [16] -->
Pinus tabuliformis 10.12

<!-- b000356 | furniture | pages [16] -->


<!-- b000357 | prose | pages [16] -->
b c

<!-- b000358 | prose | pages [16] -->
67.23 62.35 49.26 68.43 58.96 58.37 73.44 55.28 52.43 64.48 68.32 54.82

<!-- b000359 | prose | pages [16] -->
63.43 65.59

<!-- b000360 | prose | pages [16] -->
71.79 63.47

<!-- b000361 | prose | pages [16] -->
We get the carbon sequestration of this forest 𝐶𝑡(𝑖) = 1.08 × 1010kg.

<!-- b000362 | furniture | pages [16] -->


<!-- b000363 | furniture | pages [16] -->


<!-- b000364 | heading | pages [16] -->
6.2 Forest Value Evaluation Model

<!-- b000365 | prose | pages [16] -->
We performed cluster analysis on the forest data in Beijing and derived the weights of different indicators and value indexes. There are as the table below.

<!-- b000366 | furniture | pages [16] -->


<!-- b000367 | caption | pages [16] -->
Table 6: Indicator values

<!-- b000368 | prose | pages [16] -->
carbon biodiversity

<!-- b000369 | furniture | pages [16] -->


<!-- b000370 | prose | pages [16] -->
sequestration

<!-- b000371 | prose | pages [16] -->
104.32 136.83 Actual value 5 4 VI 0.3878 0.1938 Weight

<!-- b000372 | prose | pages [16] -->
1.939 0.7752 Standardized value

<!-- b000373 | furniture | pages [16] -->


<!-- b000374 | prose | pages [16] -->
recreation culture Therapy Profit

<!-- b000375 | prose | pages [16] -->
59.67 43.98 62.37 26.29 6 7 2 3 0.0140 0.0303 0.0652 0.3090

<!-- b000376 | prose | pages [16] -->
0.084 0.2121 0.1304 0.927

<!-- b000377 | prose | pages [16] -->
The actual score of Beijing Forest was calculated to be 4.0677. According to Table 3, the best forest management plan is number three, which means its best harvesting rate is 0.06% and the interval is 30 years.

<!-- b000378 | prose | pages [16] -->
The optimal harvesting scenario for a given forest for carbon sequestration in the first question shows the cyclical nature of harvesting, so in the second question we add the cutting cycle as a factor. By bringing the Beijing Forest data into our model, we evaluate its current implementation plan and conclude that it should adopt Option 3, which suggests a larger cutting rate and a smaller harvesting interval than the actual value of this forest. If we set the future logging interval to be ten years longer than the current one, then the Beijing Forest should be located at this point on the GE matrix. Therefore, considering the values of this forest and balancing the complementarity of the values, we believe that we need to increase the harvest rate to 0.09% to achieve this goal.

<!-- b000379 | furniture | pages [16] -->


<!-- b000380 | furniture | pages [16] -->


<!-- b000381 | furniture | pages [17] -->


<!-- b000382 | furniture | pages [17] -->


<!-- b000383 | furniture | pages [17] -->


<!-- b000384 | caption | pages [17] -->
Figure 11: Decision change

<!-- b000385 | furniture | pages [17] -->


<!-- b000386 | heading | pages [17] -->
7 Model Evaluation

<!-- b000387 | heading | pages [17] -->
7.1 Sensitivity Analysis

<!-- b000388 | prose | pages [17] -->
Finally, we perform sensitivity analysis on the key models related to our work through changing parameters and comparing the difference between the original results and changed results. As for the Forestry Carbon Sequestration Model, we set 𝛼= 1% first and then assign the arithmetic progression from 10% to 100% to the three param- eters respectively: 𝛽, 𝑘 and 𝜔2 . Turning to the cutting cycle, we focus on the annual growth rate of the forests while assigning 10% to 𝛼. The changes are delineated in line graphs below.

<!-- b000389 | furniture | pages [17] -->


<!-- b000390 | caption | pages [17] -->
Figure 12: Sensitivity analysis

<!-- b000391 | furniture | pages [17] -->


<!-- b000392 | prose | pages [17] -->
The graph on the left side witnesses an upward trend of carbon sequestration amount when the parameter values go up. The difference of the sensitivity in three pa- rameters is not obvious. However, we can still conclude that 𝛽 has the largest impact on the result, following by 𝑘 and 𝜔2 .

<!-- b000393 | prose | pages [17] -->
The graph on the right side gives information about the influence of growth rate on the harvesting interval. As is observed, there is a negative relationship between g and

<!-- b000394 | prose | pages [18] -->
Δ𝑖. Δ𝑖 drops rapidly at around 20% and then the decrease rate becomes slow.

<!-- b000395 | prose | pages [18] -->
The results demonstrate that our models can still keep their high effectiveness. In other words, our models have high stability, high error-tolerant rate and extensive ap- plicability.

<!-- b000396 | furniture | pages [18] -->


<!-- b000397 | heading | pages [18] -->
7.2 Strengths and Weaknesses

<!-- b000398 | heading | pages [18] -->
Strengths

<!-- b000399 | prose | pages [18] -->
 The premise of the model is based on the real situation therefore the results

<!-- b000400 | prose | pages [18] -->
obtained are compellent and consistent with the common sense.  When weighing the indicators, we choose AHP weight average method

<!-- b000401 | prose | pages [18] -->
whose indicator weights are less dependent on the sample.  The factors selected for all of our models are all objective factors. With

<!-- b000402 | prose | pages [18] -->
subjective factors excluded, the model is more stable in the evaluation pro- gress.

<!-- b000403 | furniture | pages [18] -->


<!-- b000404 | heading | pages [18] -->
Weaknesses

<!-- b000405 | prose | pages [18] -->
 Since the previous forest manager also harvested trees according to his

<!-- b000406 | prose | pages [18] -->
own preferences, the assumption that tree ages follow a uniform distribu- tion is not robust enough.  The definition of forest products varies from region to region, which

<!-- b000407 | prose | pages [18] -->
causes bias in the data and deviations of the results.

<!-- b000408 | heading | pages [18] -->
8 Conclusion

<!-- b000409 | prose | pages [18] -->
In summary, forest harvesting decisions are related to a variety of factors, includ- ing ecological, economic, and social factors. In this paper we develop a model that contributes to climate change mitigation by regulating forest management plans so that a forest can balance various values while maximizing its ecological role.

<!-- b000410 | prose | pages [18] -->
In this paper, we developed a forest value assessment model combining different forms of values. The indicators include ecological values, social values and economic values of the forest (ESE Model), of which carbon sequestration is classified as eco- logical value. By weighted average of the different value indexes, a composite score for a particular forest can be derived. We offer different forest management solutions for different scores.

<!-- b000411 | prose | pages [18] -->
Although our model is relatively well developed, there is still room for improve- ment in some extent. They are as follows：

<!-- b000412 | prose | pages [18] -->
 Set the harvesting function 𝐻𝑗 to figure out the structure of the species of

<!-- b000413 | prose | pages [18] -->
harvested trees.  Add restriction conditions, in reality, different types of forest have different

<!-- b000414 | prose | pages [18] -->
harvesting intensity restrictions.  Consider the depreciation of the HWP values, by measuring the net present

<!-- b000415 | prose | pages [18] -->
value of HWP.

<!-- b000416 | furniture | pages [18] -->


<!-- b000417 | furniture | pages [18] -->


<!-- b000418 | heading | pages [19] -->
9 Newspaper Article

<!-- b000419 | furniture | pages [19] -->


<!-- b000420 | prose | pages [19] -->
More Harvesting, Huger Benefits

<!-- b000421 | furniture | pages [19] -->


<!-- b000422 | prose | pages [19] -->
P

<!-- b000423 | prose | pages [19] -->
eople around the world may feel that the climate has been getting steadily warmer and warmer in recent years. Places which used to be abundant in snowfall have frequently experienced snow free win- ters, drought lasts longer in some dry areas and people find that without air conditioners they could hardly survive in hotter summer days. The impact of carbon dioxide emissions on the planet is more severe than we thought.

<!-- b000424 | furniture | pages [19] -->


<!-- b000425 | prose | pages [19] -->
While countries around the world are taking measures to limit carbon emissions, we should not ignore the strong carbon seques- tration capacity of the ecological system. A 14-hectare forest in the temperate zone holds 4.83 × 109 KG of carbon sequestration, which is about 1/5 times the world's average annual carbon emissions. To maximize the amount of carbon sequestration, the conven- tional wisdom is to reduce deforestation in order to preserve as much forest as possible. However, #2202666 research team has devel- oped an ESE (Ecosystem - Society - Eco- nomic) model and found that the appropriate choice of harvesting option will benefit the increase of carbon sequestration.

<!-- b000426 | furniture | pages [19] -->


<!-- b000427 | prose | pages [19] -->
ESE model emphasizes ecological, social and economic values and covers 6 factors includ- ing carbon sequestration, biodiversity, recre- ation, culture, therapy and profit in the mean- while.

<!-- b000428 | furniture | pages [19] -->


<!-- b000429 | prose | pages [19] -->
The increase in forest value from harvesting mainly comes from HWP (Harvested woods products). The amount of carbon sequestra- tion will not increase after the forest grows into mature forest. After the mature trees are cut down and made into HWP, HWP will se- questrate carbon in a certain period. From the ecological dimension, new trees con- tinue to sequester carbon, and forests rely on their self-healing ability to compensate for bi-

<!-- b000430 | prose | pages [20] -->
odiversity during this time. From the eco- nomic perspective, HWP will bring more profits. Last but not least, an appropriate rate of harvesting will have little impact on social values in the short term and the value will gradually recover as the forest grows.

<!-- b000431 | furniture | pages [20] -->


<!-- b000432 | prose | pages [20] -->
“Innovation sometimes requires going off the beaten track, diving into the forest, and you're sure to discover things you've never seen before”，it’s time to think outside the stereotype and add some creative ideas of harvesting to the forest, which is the best for- est, and our common forest.

<!-- b000433 | heading | pages [21] -->
References

<!-- b000434 | references | pages [21] -->
[1]Yang , Y. hong-qiang H., Ji, J. chun-yi C., Li, Y. hui F., Nie, N. ying Y., & Chen, C. xing-

<!-- b000435 | references | pages [21] -->
liang X. (2013). Global Climate Change and China’s Contribution to Carbon Reduction:

<!-- b000436 | references | pages [21] -->
Based on Carbon Storage Accounting of Chinese Harvested Wood Products. Journal of

<!-- b000437 | references | pages [21] -->
Natural Resources, 28(12), 2023–2033.

<!-- b000438 | references | pages [21] -->
[2]Hillier b, & Murphy r. (2000). Life Cycle Assessment of Forest Products—A Good Story to

<!-- b000439 | references | pages [21] -->
Tell. Journal of the Institute of Wood Science, 15(3), 221–232.

<!-- b000440 | references | pages [21] -->
[3]Colombo stephen j, chen, chen jiaxin  jiaxin, Ter-mikaelian michael t, & Heath linda s.

<!-- b000441 | references | pages [21] -->
(2008). Future Carbon Storage in Harvested Wood Products from Ontario’s Crown Forests.

<!-- b000442 | references | pages [21] -->
Canadian Journal of Forest, 38(7).

<!-- b000443 | references | pages [21] -->
[4]Li, L. chenyu C., Zhu, Z. jianhua J., Zhang, Z. feng F., Li, L. qi Q., Tian, T. yu  yu, Xiao,

<!-- b000444 | references | pages [21] -->
X. wenfa W., & Chen, C. weiqiang W. (2021). Factors Affecting Forest Carbon Sequestra-

<!-- b000445 | references | pages [21] -->
tion. Forestry and Ecology, 3, 40–41.

<!-- b000446 | references | pages [21] -->
[5]Li, L. chenyu C., Zhu, Z. jianhua J., Zhang, Z. feng F., Li, L. qi Q., Tian, T. yu  yu, Xiao,

<!-- b000447 | references | pages [21] -->
X. wenfa W., & Chen, C. weiqiang W. (2021). Carbon Sequestration Capacity of Beijing

<!-- b000448 | references | pages [21] -->
Arbor Forest Based on NbS. Journal of Beijing Forestry University, 43(6), 13–22.

<!-- b000449 | references | pages [21] -->
[6]Jiang, J. peng P., Li , H. li H., & Zhou, Z. liandi L. (2012). Application of Analytic Hierarchy

<!-- b000450 | references | pages [21] -->
Process in Social Value Evaluation of Forest Resource Assets. Forestry Economics, 12,

<!-- b000451 | references | pages [21] -->
88–91.

<!-- b000452 | references | pages [21] -->
[7]Zhang, Z. hui-ru H., Lei, L. xiang-dong X., & Li, L. feng-ri F. (2020). Research Progress

<!-- b000453 | references | pages [21] -->
and Prospects of Forest Management Science in China. Scientia Silvae Sinicae, 56(9),

<!-- b000454 | references | pages [21] -->
130–142.

<!-- b000455 | furniture | pages [21] -->


<!-- b000456 | furniture | pages [21] -->

