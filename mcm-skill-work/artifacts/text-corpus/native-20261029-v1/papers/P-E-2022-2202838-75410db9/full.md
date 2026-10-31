# P-E-2022-2202838-75410db9

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
2022

<!-- b000002 | prose | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
E

<!-- b000006 | title | pages [1] -->
2202838

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | title | pages [1] -->
What a Forest Management Plan!

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | furniture | pages [1] -->


<!-- b000014 | prose | pages [1] -->
"Trees are unguilty. You destroy them. You are guilty!" Some argue that we should not cut down trees at all to mitigate climate change, but in fact, proper logging is necessary and beneficial. Through establishing models, we demonstrate that forest management plans including harvesting can balance the carbon sequestration (CS) and the realization of other values.

<!-- b000015 | prose | pages [1] -->
First, we establish a Carbon Sequestration Model to obtain the amount of CS including forest and forest products. In the calculation, we use the Conversion Factor Method (CFM) of forest stock volume, comprehensively considering trees, understory plants and wood soil. And we use a logical growth model to express the CS capacity and tree age to obtain a more real value. By adding the CS of forests and forest products, we can obtain the total amount of CS in year .

<!-- b000016 | prose | pages [1] -->
Then, we establish a Forest Management Model for Carbon Sequestration combining the idea of Dynamic Objective Programming. We divide the forest into regions, using ,

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | prose | pages [1] -->
to store information about cut or not, tree age, and death or not respectively. These and variables affect each other. Combined with them and the CS model, we can obtain the amount of CS in statistical time, which is our objective function. Then, we get the optimal management plan by searching the optimal solution to the function.

<!-- b000019 | prose | pages [1] -->
To comprehensively consider other forest values, we establish a Forest Management Model for Society. And we create a three-level evaluation indicator system, including four second-level indicators (carbon sequestration, biodiversity, cultural and recreational value) and 10 third-level indicators. We determine the weight of each third-level indicator by Entropy Weight Method. Considering different characteristics and geographical location of each forest, we use the Analytic Hierarchy Process to get the value score by weighting the secondary indicators to make the score closer to the real situation. Meanwhile, we use GE Matrix to evaluate the forest management plan based on the cost of realizing the value, and get transition points of different plans. By optimizing the distance between the plan and the optimal point in GE matrix, we obtain the optimal forest management plan for society, which may vary for different forest managers.

<!-- b000020 | prose | pages [1] -->
Next, we apply our models to the Greater Khingan Mountains. And we obtain that the total CS of forest and its products after 100 years is 4.264 billion tons, among which the CS of forest is

<!-- b000021 | heading | pages [1] -->
2.724 billion tons and that of its products is 1.540 billion tons. Then we establish a Nonlinear

<!-- b000022 | prose | pages [1] -->
Programming Model and use Genetic Algorithm to get the best forest management plan: the ratio of the four regions realizing the value is 58.95%, 11.20%, 11.41% and 18.37%, respectively. Allowing logging 10 years longer than current practices, we modify the management plan to provide forest managers and all those who use forests with strategies to meet their needs.

<!-- b000023 | prose | pages [1] -->
In the end, we write a newspaper article to explain our optimal forest management plan.

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | keywords | pages [1] -->
Keywords: Carbon Sequestration, Forest Management Model for Carbon Sequestration or Society,

<!-- b000027 | prose | pages [1] -->
Objective Programming, GE Matrix

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | furniture | pages [1] -->


<!-- b000030 | heading | pages [2] -->
Contents

<!-- b000031 | furniture | pages [2] -->


<!-- b000032 | contents | pages [2] -->
1 Introduction ................................................................................................................................. 3

<!-- b000033 | contents | pages [2] -->
1.1 Background ......................................................................................................................... 3

<!-- b000034 | contents | pages [2] -->
1.2 Problem Restatement .......................................................................................................... 3

<!-- b000035 | contents | pages [2] -->
1.3 Our Work ............................................................................................................................ 4

<!-- b000036 | contents | pages [2] -->
2 Assumption and Justifications ................................................................................................... 4

<!-- b000037 | contents | pages [2] -->
3 Notation ........................................................................................................................................ 4

<!-- b000038 | contents | pages [2] -->
4 Carbon Sequestration Model ..................................................................................................... 5

<!-- b000039 | contents | pages [2] -->
4.1 The Carbon Sequestration of Forests .................................................................................. 6

<!-- b000040 | contents | pages [2] -->
4.2 The Carbon Sequestration of Forest Products .................................................................... 7

<!-- b000041 | contents | pages [2] -->
4.3 Carbon Sequestration Capacity Factor ................................................................................ 7

<!-- b000042 | contents | pages [2] -->
5 Forest Management Model for Carbon Sequestration ............................................................ 9

<!-- b000043 | contents | pages [2] -->
5.1 Parameter Settings .............................................................................................................. 9

<!-- b000044 | contents | pages [2] -->
5.2 Construction of Objective Function .................................................................................. 10

<!-- b000045 | contents | pages [2] -->
6 Forest Management Model for Society ................................................................................... 11

<!-- b000046 | contents | pages [2] -->
6.1 Overview ........................................................................................................................... 11

<!-- b000047 | contents | pages [2] -->
6.2 The Value of Forests ......................................................................................................... 12

<!-- b000048 | contents | pages [2] -->
6.3 Forest Management Evaluation Model ............................................................................. 15

<!-- b000049 | contents | pages [2] -->
7 Case study: Greater Khingan Mountains ............................................................................... 17

<!-- b000050 | contents | pages [2] -->
7.1 The Current Situation of Greater Khingan Mountains ..................................................... 17

<!-- b000051 | contents | pages [2] -->
7.2 Analysis of Carbon Sequestration after 100 Years ........................................................... 18

<!-- b000052 | contents | pages [2] -->
7.3 The Optimal Forest Management Plan ............................................................................. 19

<!-- b000053 | contents | pages [2] -->
7.4 The Modification of the Optimal Plan .............................................................................. 20

<!-- b000054 | contents | pages [2] -->
8 Sensitivity Analysis .................................................................................................................... 21

<!-- b000055 | contents | pages [2] -->
9 Strengths and Weaknesses........................................................................................................ 22

<!-- b000056 | contents | pages [2] -->
9.1 Strengths ........................................................................................................................... 22

<!-- b000057 | contents | pages [2] -->
9.2 Weaknesses ....................................................................................................................... 22

<!-- b000058 | contents | pages [2] -->
10 A Newspaper Article ............................................................................................................... 22

<!-- b000059 | contents | pages [2] -->
References ..................................................................................................................................... 24

<!-- b000060 | furniture | pages [2] -->


<!-- b000061 | furniture | pages [2] -->


<!-- b000062 | furniture | pages [2] -->


<!-- b000063 | heading | pages [3] -->
1 Introduction

<!-- b000064 | heading | pages [3] -->
1.1 Background

<!-- b000065 | prose | pages [3] -->
Global warming is bringing alarming consequences around the world, including more extreme events, the rise of sea levels and the increased threat of extinction of plant and animal species. In order to slow climate change and protect human environment, it is not enough to reduce carbon emissions. We should also consider how to increase the amount of carbon dioxide sequestered from the atmosphere, known as carbon sequestration.[1]

<!-- b000066 | prose | pages [3] -->
As the main body of terrestrial ecosystems, forests store more than 45% of all terrestrial organic carbon, and their annual absorption of 𝐶𝑂2 through photosynthesis accounts for 2/3 of all terrestrial ecosystems. Forests play a very important role in the global carbon cycle. Through logging, fixed carbon in forests can be transferred to wood forest products, which can store carbon in the whole life cycle of forest products. The disturbance of human activities to the global carbon cycle in the 20th century is an unprecedented phenomenon in history. Understanding the global carbon cycle and its impact on human activities is important for developing viable climate change mitigation strategies.

<!-- b000067 | furniture | pages [3] -->


<!-- b000068 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000069 | prose | pages [3] -->
In order to develop guidelines for forest managers around the world to try to figure out how to use and manage their forests, our group undertook the following work: ⚫ Design a carbon sequestration model to determine the amount of 𝐶𝑂2 that a forest and its forest

<!-- b000070 | prose | pages [3] -->
products can sequester over time, and determine which forest management plans are most effective. ⚫ Develop a decision model to determine a forest management plan. Consider the following

<!-- b000071 | prose | pages [3] -->
questions: what are the conditions that would prevent a forest from being cut down; whether there are transition points between management plans applicable to all forests; how to use the characteristics of a particular forest and its location to determine transition points between management plans. ⚫ Apply the model to a variety of forests. Determine how much 𝐶𝑂2 a forest and its products

<!-- b000072 | prose | pages [3] -->
will absorb over a period of 100 years. Discuss what forest management plans should be adopted for the forest and strategies to achieve them, supposing the best management plan includes a time between harvests that is 10 years longer than current practices in the forest. ⚫ Write a non-technical newspaper article explaining the forest management plan.

<!-- b000073 | furniture | pages [3] -->


<!-- b000074 | furniture | pages [3] -->


<!-- b000075 | furniture | pages [3] -->


<!-- b000076 | furniture | pages [3] -->


<!-- b000077 | furniture | pages [3] -->


<!-- b000078 | furniture | pages [3] -->


<!-- b000079 | furniture | pages [3] -->


<!-- b000080 | furniture | pages [3] -->


<!-- b000081 | furniture | pages [3] -->


<!-- b000082 | furniture | pages [3] -->


<!-- b000083 | furniture | pages [3] -->


<!-- b000084 | furniture | pages [3] -->


<!-- b000085 | heading | pages [4] -->
1.3 Our Work

<!-- b000086 | furniture | pages [4] -->


<!-- b000087 | caption | pages [4] -->
Figure 1: Our work

<!-- b000088 | furniture | pages [4] -->


<!-- b000089 | heading | pages [4] -->
2 Assumption and Justifications

<!-- b000090 | furniture | pages [4] -->


<!-- b000091 | prose | pages [4] -->
Assumption 1: We assume that the accumulated carbon sequestration of trees follows the logical growth model.

<!-- b000092 | prose | pages [4] -->
Justification: The CS capacity of trees is different with ages. Based on the literature [2], the capacity shows a trend of first increasing and then decreasing. We can conclude the accumulated amount of CS will increase rapidly first, then slow down, and finally reach a stable value, which is in line with the logical growth model.

<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | prose | pages [4] -->
Assumption 2: We divide the forest into small areas, and each area only plants one tree. If trees are cut down in one area, seedlings of the same type will be planted in the same area in the same year.

<!-- b000095 | prose | pages [4] -->
Justification: Because the number of areas with different ages and species of trees will change dynamically when trees are felled and new trees are planted. We make this assumption to simplify the model.

<!-- b000096 | furniture | pages [4] -->


<!-- b000097 | prose | pages [4] -->
Assumption 3: When trees die, part of their CS is transferred to the land. And the CS of forest products returns to the atmosphere when they reach their lifespan.

<!-- b000098 | prose | pages [4] -->
Justification: A part of the organic carbon produced by photosynthesis of trees is fixed in the soil. This amount of CS is unaffected by the death of trees and remains still. To simplify the model, we assume forest products will release all to the atmosphere at the end of their life.

<!-- b000099 | furniture | pages [4] -->


<!-- b000100 | heading | pages [4] -->
3 Notation

<!-- b000101 | prose | pages [4] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000102 | furniture | pages [4] -->


<!-- b000103 | furniture | pages [4] -->


<!-- b000104 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000105 | heading | pages [5] -->
Symbol

<!-- b000106 | furniture | pages [5] -->


<!-- b000107 | prose | pages [5] -->
Description the total amount of carbon sequestration in year

<!-- b000108 | furniture | pages [5] -->


<!-- b000109 | prose | pages [5] -->
the carbon sequestration of forests in year

<!-- b000110 | furniture | pages [5] -->


<!-- b000111 | prose | pages [5] -->
the carbon sequestration of forest products in year

<!-- b000112 | furniture | pages [5] -->


<!-- b000113 | prose | pages [5] -->
the amount of forest carbon sequestration used for the p-type product in year

<!-- b000114 | furniture | pages [5] -->


<!-- b000115 | prose | pages [5] -->
the carbon sequestration of forest trees in year

<!-- b000116 | furniture | pages [5] -->


<!-- b000117 | prose | pages [5] -->
the carbon sequestration of understory plants in year .

<!-- b000118 | furniture | pages [5] -->


<!-- b000119 | prose | pages [5] -->
the carbon sequestration of the wood soil in year

<!-- b000120 | furniture | pages [5] -->


<!-- b000121 | prose | pages [5] -->
the carbon sequestration capacity factor

<!-- b000122 | furniture | pages [5] -->


<!-- b000123 | prose | pages [5] -->
carbon sequestration value

<!-- b000124 | furniture | pages [5] -->


<!-- b000125 | prose | pages [5] -->
biodiversity value

<!-- b000126 | furniture | pages [5] -->


<!-- b000127 | furniture | pages [5] -->


<!-- b000128 | prose | pages [5] -->
cultural value recreational value

<!-- b000129 | furniture | pages [5] -->


<!-- b000130 | prose | pages [5] -->
the cost per unit area needed to realize the h-type value of the selected forest

<!-- b000131 | furniture | pages [5] -->


<!-- b000132 | heading | pages [5] -->
4 Carbon Sequestration Model

<!-- b000133 | prose | pages [5] -->
Before establishing carbon sequestration model, we need to understand the main approaches to sequestering carbon. It is reported that soils and plants sequester three times as much carbon as the atmosphere, with forests accounting for 45%. The world's forests absorbed more than a quarter of global carbon emissions between 2006 and 2015. Forest sequestration of carbon dioxide is dynamic: trees absorb 𝐶𝑂2 from the atmosphere through photosynthesis and convert it into biomass stored in different parts of the plant body [3].

<!-- b000134 | prose | pages [5] -->
Meanwhile, forest carbon sequestration continuously transfers among carbon pools. Natural disturbances, decay of dead wood, and forest respiration contribute to the release of 𝐶𝑂2 into the atmosphere. The carbon fixed by trees will be transferred to forest products due to logging, which will lead to the change of forest carbon sink. We can store the fixed carbon in wood forest products for different lengths of time depending on the end use. Therefore, forests and wood forest products are therefore an important component of the global carbon cycle. Figure 2 shows the role of forests and forest products in the global carbon cycle.

<!-- b000135 | furniture | pages [5] -->


<!-- b000136 | caption | pages [5] -->
Figure 2: The roles of forests and forest

<!-- b000137 | prose | pages [5] -->
products in the global carbon cycle

<!-- b000138 | prose | pages [5] -->
And we can define the total amount of carbon sequestration in year  as

<!-- b000139 | furniture | pages [5] -->


<!-- b000140 | furniture | pages [5] -->


<!-- b000141 | prose | pages [5] -->
(1)

<!-- b000142 | prose | pages [6] -->
where

<!-- b000143 | prose | pages [6] -->
is the carbon sequestration of forests in year .

<!-- b000144 | prose | pages [6] -->
forest products in year .

<!-- b000145 | prose | pages [6] -->
is the carbon sequestration of

<!-- b000146 | heading | pages [6] -->
4.1 The Carbon Sequestration of Forests

<!-- b000147 | prose | pages [6] -->
There are many accounting formulas for forest carbon sequestration, such as 𝐶𝑂2 FIX model method, Carbon balance F-Corron model method, biomass conversion method, vortex correlation method and box method [4]. Based on previous studies, we adopt the conversion factor method of forest stock to calculate forest carbon sequestration by integrating operability, economy, long-term measurement and accuracy.

<!-- b000148 | prose | pages [6] -->
Forest trees, understory plants and the wood soil can all play a role in carbon sequestration. If investigating the carbon sequestration and sequestration effect of forests from the perspective of natural science, then we should integrate the sequestration effect of the three. Therefore, we can define the total carbon sequestration of forests in year 𝑡 as

<!-- b000149 | prose | pages [6] -->
where

<!-- b000150 | furniture | pages [6] -->


<!-- b000151 | prose | pages [6] -->
(2)

<!-- b000152 | prose | pages [6] -->
represents the carbon sequestration of forest trees in year .

<!-- b000153 | prose | pages [6] -->
sequestration of understory plants in year .

<!-- b000154 | prose | pages [6] -->
soil in year .

<!-- b000155 | prose | pages [6] -->
represents the carbon

<!-- b000156 | prose | pages [6] -->
represents the carbon sequestration of the wood

<!-- b000157 | heading | pages [6] -->
4.1.1 The Carbon Sequestration of Trees

<!-- b000158 | prose | pages [6] -->
Trees mainly perform photosynthesis and absorb 𝐶𝑂2 from the atmosphere through canopy leaves and convert it into biomass stored in different parts of the plant body. Therefore, we define the total carbon sequestration of trees in year  as

<!-- b000159 | prose | pages [6] -->
where

<!-- b000160 | furniture | pages [6] -->


<!-- b000161 | prose | pages [6] -->
(3)

<!-- b000162 | prose | pages [6] -->
represents the carbon sequestration of forest trees in region 𝑖 in year .

<!-- b000163 | prose | pages [6] -->
represents

<!-- b000164 | prose | pages [6] -->
represents the carbon density of biomass in region 𝑖 in year . the area in region 𝑖 in year .

<!-- b000165 | heading | pages [6] -->
4.1.2 The Carbon Sequestration of Understory Plants

<!-- b000166 | prose | pages [6] -->
Understory plants can also sequester carbon. On the other hand, they can also sequester carbon by absorbing organic matter from the soil. We define the total carbon sequestration of understory plants in year  as

<!-- b000167 | prose | pages [6] -->
where

<!-- b000168 | prose | pages [6] -->
(4)

<!-- b000169 | furniture | pages [6] -->


<!-- b000170 | prose | pages [6] -->
represents the carbon sequestration of understory plants in region 𝑖 in year .

<!-- b000171 | furniture | pages [6] -->


<!-- b000172 | prose | pages [6] -->
represents the effective area of understory plants in region 𝑖 in year . The formular is is the carbon conversion coefficient of understory plants. According to , where the default common values of the Intergovernmental Panel on Climate Change (IPCC), we take

<!-- b000173 | prose | pages [6] -->
.

<!-- b000174 | furniture | pages [6] -->


<!-- b000175 | heading | pages [7] -->
4.1.3 The Carbon Sequestration of the Wood Soil

<!-- b000176 | prose | pages [7] -->
Some of the organic carbon produced by photosynthesis in trees gets stuck in the soil. In addition. Therefore, soil carbon sequestration is also considerable. We define the total carbon sequestration of the wood soil in year t as

<!-- b000177 | prose | pages [7] -->
where

<!-- b000178 | furniture | pages [7] -->


<!-- b000179 | prose | pages [7] -->
(5)

<!-- b000180 | prose | pages [7] -->
represents the carbon sequestration of understory plants in region 𝑖 in year .

<!-- b000181 | furniture | pages [7] -->


<!-- b000182 | prose | pages [7] -->
represents the effective area of the wood soil in region 𝑖 in year . The formular is , is the carbon conversion coefficient of the wood soil. According to IPCC, we take where

<!-- b000183 | prose | pages [7] -->
.

<!-- b000184 | heading | pages [7] -->
4.1.4 The Biomass Carbon Density

<!-- b000185 | prose | pages [7] -->
Forests store large amounts of carbon in their vast biomass. Measuring the forest community biomass and further estimating the biomass carbon density can measure the level of community productivity, which is the basis of studying the carbon cycle of forest ecosystem. We define the biomass carbon density of forest 𝑗 in region 𝑖 in year  as

<!-- b000186 | prose | pages [7] -->
where

<!-- b000187 | furniture | pages [7] -->


<!-- b000188 | prose | pages [7] -->
(6)

<!-- b000189 | prose | pages [7] -->
represents the stock volume per unit area in region 𝑖 in year .  represents the biomass expansion coefficient, which can convert the tree stock volume into the biological stock volume of trees as the main body.  represents the volume coefficient, which can convert the total forest represents carbon content, which can convert dry weight of the biomass biomass into dry weight.

<!-- b000190 | prose | pages [7] -->
is the carbon sequestration capacity factor. We will further into carbon sequestration. discuss it later. According to IPCC, we take .

<!-- b000191 | heading | pages [7] -->
4.2 The Carbon Sequestration of Forest Products

<!-- b000192 | prose | pages [7] -->
According to the life cycle theory, compared with concrete and steel, not only wood consumes less energy and emits less carbon during production and processing, but also its growth plays a role of carbon sequestration. Through logging, the carbon fixed in the forest can be transferred to wood forest products, which mainly include logs, sawn wood, pulp wood, wood-based panels and so on. Forest products can store carbon though the whole life cycle. We define the total carbon sequestration of forest products in year  as

<!-- b000193 | prose | pages [7] -->
where

<!-- b000194 | furniture | pages [7] -->


<!-- b000195 | prose | pages [7] -->
(7)

<!-- b000196 | prose | pages [7] -->
represents the amount of forest carbon sequestration used for the p-type forest product. The calculation formula is same to .

<!-- b000197 | prose | pages [7] -->
is the processing loss rate in the production is the number of forest product types. of the p-type forest product.

<!-- b000198 | heading | pages [7] -->
4.3 Carbon Sequestration Capacity Factor

<!-- b000199 | prose | pages [7] -->
In order to clarify the impact of tree age on carbon sequestration capacity, and then affect the carbon sequestration amount of the whole forest, we should consider the change of carbon sequestration amount with tree age. According to our assumption, the carbon sequestration capacity

<!-- b000200 | prose | pages [8] -->
of trees first increases and then decreases, and the carbon sequestration amount finally tends to a stable value. Inspired by the population dynamic growth model [5], we express the relationship between carbon sequestration capacity and tree age as a logical growth function.

<!-- b000201 | furniture | pages [8] -->


<!-- b000202 | prose | pages [8] -->
(8)

<!-- b000203 | prose | pages [8] -->
in Formula (9) as the amount of carbon sequestration at the We define . Multiply it by maximum age of trees per unit area and we can get the amount of carbon sequestration in year  per unit area. We can solve its differential equation by separating variables, and finally obtain the expression of

<!-- b000204 | prose | pages [8] -->
where

<!-- b000205 | prose | pages [8] -->
as

<!-- b000206 | furniture | pages [8] -->


<!-- b000207 | prose | pages [8] -->
(9)

<!-- b000208 | prose | pages [8] -->
is the increasing rate of a tree’s carbon sequestration capacity. It is related to the size and type of the tree, which reflects the variation of carbon sequestration levels of different trees with tree age.

<!-- b000209 | prose | pages [8] -->
is the carrying capacity, and we set . If the tree reaches full maturity (maximum , representing that the maximum accumulated carbon sequestration. tree age), then If the tree is first planted (the tree age is 0), then , and there is no carbon is a constant. Based on the growth level of most trees, we take it 500. sequestration.

<!-- b000210 | prose | pages [8] -->
According to the actual situation, we can determine the coefficients of different kinds of trees in differential equations. We can understand capacity, which we will use in subsequent model.

<!-- b000211 | prose | pages [8] -->
as accumulated carbon sequestration

<!-- b000212 | prose | pages [8] -->
We take Greater Khingan Mountains to do case study of this model. Table 2 lists the main tree species, tree age and coefficient corresponding to the logical growth function of the forest.

<!-- b000213 | caption | pages [8] -->
Table 2: The related data of Forests of Greater Khingan Mountains

<!-- b000214 | furniture | pages [8] -->


<!-- b000215 | prose | pages [8] -->
Cutting age Overmature age

<!-- b000216 | furniture | pages [8] -->


<!-- b000217 | prose | pages [8] -->
Mongolian oak 60 Xing’an larch 30 White birch 15 120 0.1036 60 0.2072 30 0.4143 And Figure 3 shows the comparison of the carbon sequestration capacity and accumulated carbon sequestration capacity of various trees.

<!-- b000218 | furniture | pages [8] -->


<!-- b000219 | prose | pages [8] -->
(a)                                                                                  (b)

<!-- b000220 | caption | pages [8] -->
Figure 3: The comparison of various trees

<!-- b000221 | heading | pages [9] -->
5 Forest Management Model for Carbon Sequestration

<!-- b000222 | heading | pages [9] -->
5.1 Parameter Settings

<!-- b000223 | prose | pages [9] -->
Carbon sequestration includes forest carbon sequestration and forest products carbon sequestration. Because some forest products may outlive the trees that produced them. The combination of sequestrated carbon in some forest products with sequestrated carbon due to the regeneration of young forests has the potential to allow more sequestration over time than the sequestration benefits of not cutting forests at all. So, we need to explore how we can plan to properly cut down the trees in the forest and make the right forest products. The life of forest products should be longer than the life of the trees themselves in order to effectively increase carbon sequestration.

<!-- b000224 | caption | pages [9] -->
Figure 4: Forest carbon sequestration destination

<!-- b000225 | prose | pages [9] -->
In this model, we optimize the carbon sequestration model. During the growth of trees, carbon sequestration is transferred from trees to soil, and this part of carbon sequestration will not be decomposed back into carbon dioxide after the tree dies. As shown in Figure 4. It still contributes to the total carbon sequestration of forests. Therefore, we add the contribution to carbon sequestration after the death of trees in statistical time into the model to make the result closer to the real situation.

<!-- b000226 | prose | pages [9] -->
In order to determine the optimal forest management plan over time, we establish the optimal forest management model for carbon sequestration. And we search for the optimal plan through dynamic programming method. The specific steps are as follows:

<!-- b000227 | prose | pages [9] -->
unit areas and number them. We classify the areas First, we divide the selected forest into with same tree species into consecutive numbers, and record the corresponding numbering ranges of different species. In this way, we can determine the type of trees in the unit area by the size of

<!-- b000228 | prose | pages [9] -->
indicates that A-type trees grow in this area; . For example, B-type trees grow in that area, and so on.

<!-- b000229 | prose | pages [9] -->
indicates that

<!-- b000230 | prose | pages [9] -->
The area number of trees with different ages and types in the forest changes dynamically due to the felling of trees and the planting of new trees. To simplify the model, we assume that after cutting down trees in a certain year, seedlings of the same type of trees will be planted in the original area in the same year.

<!-- b000231 | prose | pages [9] -->
Before deciding on the harvest plan for the trees in region , we should first decide whether the trees can be cut down. We define the age of trees in region  in year  as . And we use to store information about the age at which trees are felled. And the age of trees in region is greater than the longest life of trees in this region, in year is . If then the trees in this region have died in year  and we cannot cut them down. At this time, the death of trees in region  in year is , and make . is still within the survival range of trees in this area, then If and make the subsequent judgment. We define the time required for the j-type tree to grow to the felling stage as

<!-- b000232 | prose | pages [9] -->
is larger than the cutting age of a specific type of trees in the region, that is . When , trees in the region can be felled in year ; if , then they cannot be felled.

<!-- b000233 | prose | pages [10] -->
We define whether the unit region  is felled in year  as . Its definition is where

<!-- b000234 | furniture | pages [10] -->


<!-- b000235 | prose | pages [10] -->
indicates that trees are cut. indicates that trees are not cut, and

<!-- b000236 | prose | pages [10] -->
If trees in region  are cut in year , that is

<!-- b000237 | furniture | pages [10] -->


<!-- b000238 | prose | pages [10] -->
(10)

<!-- b000239 | prose | pages [10] -->
, then make to store the age of trees in region  in year  at the time of cutting, then set again. Otherwise , then and

<!-- b000240 | furniture | pages [10] -->


<!-- b000241 | prose | pages [10] -->
, and start the calculation is not required to be zero.

<!-- b000242 | heading | pages [10] -->
5.2 Construction of Objective Function

<!-- b000243 | prose | pages [10] -->
At the end of the last year of the statistical period, we can obtain the value of and in each year for each region in the period. Figure 5 shows the overall process.

<!-- b000244 | furniture | pages [10] -->


<!-- b000245 | caption | pages [10] -->
Figure 5: The overall process

<!-- b000246 | prose | pages [10] -->
In order to optimize the solving process of the total carbon sequestration in the statistical period, we integrate the Formula (9) to obtain the expression of the total carbon sequestration in the growth year of trees in region .

<!-- b000247 | furniture | pages [10] -->


<!-- b000248 | prose | pages [10] -->
(11) , we can calculate the contribution of dead trees to carbon sequestration during Using the statistical time. The formula is

<!-- b000249 | prose | pages [10] -->
where

<!-- b000250 | prose | pages [10] -->
(12)

<!-- b000251 | furniture | pages [10] -->


<!-- b000252 | prose | pages [10] -->
is the part that still contributes to carbon sequestration after tree death in the statistical time.

<!-- b000253 | prose | pages [10] -->
is the carbon density accumulated at the maximum age of the trees in region .

<!-- b000254 | prose | pages [10] -->
is the year number of the statistical time.  is the proportion of the part still contributing to carbon sequestration after the death of trees to that before the death of trees, which is related to climate.

<!-- b000255 | prose | pages [11] -->
, we use the optimized Formula (13) to calculate the carbon density According to the accumulated in their growth years in region  in year (4) (5) of carbon sequestration model to calculate , and we analogy the Formula (2) (3) , which is the forest carbon sequestration . By adding the contribution of dead trees to the carbon sequestration in the live in year statistic time (excluding the amount that had been felled and converted into forest products in previous years), we can calculate the total carbon sequestration of the forest. The formula is

<!-- b000256 | furniture | pages [11] -->


<!-- b000257 | prose | pages [11] -->
(13) , we also need to calculate the carbon sequestration amount of forest After obtaining products in statistical time. We consider that forest products whose product life has exceeded in the statistical time do not contribute to the carbon sequestration, so we only need to calculate the total carbon sequestration of forest products whose product life has not exceeded in the last year of the statistical time. The calculation formula is

<!-- b000258 | prose | pages [11] -->
where

<!-- b000259 | furniture | pages [11] -->


<!-- b000260 | prose | pages [11] -->
(14)

<!-- b000261 | furniture | pages [11] -->


<!-- b000262 | prose | pages [11] -->
(15)

<!-- b000263 | furniture | pages [11] -->


<!-- b000264 | prose | pages [11] -->
(16)

<!-- b000265 | prose | pages [11] -->
is the set of region  corresponding to trees producing the p-type forest product.

<!-- b000266 | prose | pages [11] -->
is the carbon density accumulated during the growth years of the felled trees. trees are cut.

<!-- b000267 | prose | pages [11] -->
is the age at which

<!-- b000268 | prose | pages [11] -->
Therefore, it is necessary to find the objective function that maximizes the total carbon sequestration of forests and forest products with the optimal plan. We can get the total carbon sequestration of forests and forest products in the statistical time is

<!-- b000269 | prose | pages [11] -->
where

<!-- b000270 | furniture | pages [11] -->


<!-- b000271 | prose | pages [11] -->
(17)

<!-- b000272 | prose | pages [11] -->
is the total carbon sequestration of forest in statistical time.

<!-- b000273 | prose | pages [11] -->
is the total carbon sequestration of forest products that do not exceed the product life in the last year of the statistical time.

<!-- b000274 | prose | pages [11] -->
By solving the objective function, we can obtain the optimal forest management plan, that is, the annual cutting amount of trees in each region, the plan of making forest products and so on. The plan enables selected forests and their forest products to achieve the maximum amount of carbon sequestration over statistical time.

<!-- b000275 | furniture | pages [11] -->


<!-- b000276 | heading | pages [11] -->
6 Forest Management Model for Society

<!-- b000277 | heading | pages [11] -->
6.1 Overview

<!-- b000278 | prose | pages [11] -->
The forest management plans that are most conducive to carbon sequestration are not necessarily the best for society. To make better decisions about managing forests, we need to understand the value of forests. Then we define indicators to quantify it.

<!-- b000279 | prose | pages [12] -->
The United Nations economic commission for Europe and FAO (UNECE/FAO) published the report "forest non-wood forest products and services", which takes "social and cultural service" as a whole to start research, and refine the forest value as hunting and fishing, leisure and tourism value, the aesthetics and landscape value and historical value, cultural and spiritual values, and science. [6] In the previous section, we discussed the carbon sequestration value of forest. Combined with the UN research, we mainly consider the following three aspects: biodiversity value, cultural value and recreational value.

<!-- b000280 | furniture | pages [12] -->


<!-- b000281 | heading | pages [12] -->
6.2 The Value of Forests

<!-- b000282 | caption | pages [12] -->
Figure 6: Indicators of forest value

<!-- b000283 | heading | pages [12] -->
6.2.1 Carbon Sequestration Value (CSV)

<!-- b000284 | prose | pages [12] -->
As discussed in our previous model, forests are an integral part of climate change mitigation and have significant carbon sequestration value. We use the maximum carbon sequestration of selected forests obtained from the optimal carbon sequestration forest management model to calculate the annual maximum carbon sequestration. And then we can measure the carbon sequestration value of a forest as

<!-- b000285 | prose | pages [12] -->
where

<!-- b000286 | furniture | pages [12] -->


<!-- b000287 | prose | pages [12] -->
(18)

<!-- b000288 | prose | pages [12] -->
is the total carbon sequestration in the statistic time.

<!-- b000289 | heading | pages [12] -->
6.2.2 Biodiversity Value (BV)

<!-- b000290 | prose | pages [12] -->
Biodiversity includes genetic, species and ecosystem diversity. Based on the above theory, when calculating the value of biodiversity, we consider the population richness and population density in a forest area and the complexity of the ecosystem in which all creatures live.

<!-- b000291 | prose | pages [12] -->
Species Richness (SR) When describing the richness of biodiversity in an area, the most commonly used indicator is regional species diversity. A measure of regional species diversity can be expressed in terms of species richness. [7] Edward Hugh Simpson, a British statistician, proposed Simpson's diversity index [8]. The greater the Simpson diversity index, the more species, the higher the species richness. The formula is

<!-- b000292 | prose | pages [12] -->
where

<!-- b000293 | prose | pages [12] -->
(19)

<!-- b000294 | furniture | pages [12] -->


<!-- b000295 | prose | pages [12] -->
is the number of entities belonging to the m-type in the selected forest. number of entities in the selected forest.

<!-- b000296 | prose | pages [12] -->
is the total

<!-- b000297 | prose | pages [13] -->
Biomass Density (BD) It is a measure of the richness of organisms in an area. We can get the biomass density directly by dividing the total number of plants and animals in a selected forest by the total area of the forest.

<!-- b000298 | prose | pages [13] -->
where

<!-- b000299 | prose | pages [13] -->
(20)

<!-- b000300 | furniture | pages [13] -->


<!-- b000301 | prose | pages [13] -->
is the total number of plants and animals. Ecosystem Complexity (EC) is the total area of the forest.

<!-- b000302 | prose | pages [13] -->
Any creature has to live in a certain environment, leaving the appropriate environment, it is difficult for the creature to adapt. So only a diversity of ecosystems can ensure the survival of various life in those ecosystems. Here, we use absolute ecosystem richness to measure ecosystem complexity.

<!-- b000303 | prose | pages [13] -->
where

<!-- b000304 | furniture | pages [13] -->


<!-- b000305 | prose | pages [13] -->
(21)

<!-- b000306 | prose | pages [13] -->
is the number of ecosystem types, which is classified according to vegetation subtypes in the vegetation classification system.

<!-- b000307 | prose | pages [13] -->
Finally, we can obtain biodiversity value through the weighted combination of these indicators:

<!-- b000308 | prose | pages [13] -->
where

<!-- b000309 | furniture | pages [13] -->


<!-- b000310 | prose | pages [13] -->
(22)

<!-- b000311 | prose | pages [13] -->
is the weight of three indicators respectively.

<!-- b000312 | heading | pages [13] -->
6.2.3 Cultural Value (CV)

<!-- b000313 | prose | pages [13] -->
Forest cultural value is an important part of total forest values. David Edwards proposed “key indicators for the sustainability of social and cultural values of Forests in Europe” and selected typical regions in Europe for empirical analysis. The five themes of the indicator system, including recreation and tourism, education and learning, health and welfare, landscape and aesthetics, culture and heritage, are closely related to the cultural values of forests [9]. Therefore, we measure the cultural value of the selected forest in terms of education, health and cultural heritage.

<!-- b000314 | prose | pages [13] -->
Education Input (EI) The more money a region invests in education, the higher its education level will be. Here, we use the percentage of GDP invested in education of the country where we select forest to express it. The higher the level of education, the stronger people's understanding of the forest, the more easily the cultural value of a forest can be reflected.

<!-- b000315 | prose | pages [13] -->
Health Level (HL) We measure health level by life expectancy in the country where we select forest, and the shorter the life expectancy, the lower the health level. The cultural value that forests bring can promote physical activity and significantly improve the health of people in areas with low health level. As for countries with high health level, people may have good living habits at ordinary times, so forest cultural values do not contribute much to their health.

<!-- b000316 | prose | pages [13] -->
Cultural Heritage (CH) The higher the proportion of heritage of cultural and spiritual value in the forest, the more areas of the forest that can be used for the development of cultural resources, the higher the cultural value.

<!-- b000317 | prose | pages [13] -->
Also, we can obtain the cultural value indicator by the weighted combination of these three indicators:

<!-- b000318 | prose | pages [14] -->
where

<!-- b000319 | furniture | pages [14] -->


<!-- b000320 | prose | pages [14] -->
(23)

<!-- b000321 | prose | pages [14] -->
is the weight of three indicators respectively.

<!-- b000322 | heading | pages [14] -->
6.2.4 Recreational Value (RV)

<!-- b000323 | prose | pages [14] -->
According to economic demand theory and related research results, we can consider the factors affecting forest recreational value from both supply and demand. Demand factors mainly include: population density of local residents, regional urbanization rate, the income level of residents in this area. Supply factors mainly include: the level of tourism resources in this region, density of forest parks in the region, transportation convenience, forest environmental quality; degree of capitalization, human resources [10]. We select two indicators of demand and supply respectively to measure recreational value.

<!-- b000324 | prose | pages [14] -->
Population Density (PD) Population is the basis of tourism market. Due to the spatial mobility of tourism, tourism demand shows an obvious spatial distance attenuation law. In particular, people's demand for forest parks is mainly from tourists inside the province [11]. The greater the population density of a country, the greater the demand for forest parks.

<!-- b000325 | prose | pages [14] -->
Income Level (IL) We use GDP per capita of the country where the forest is located. Studies have proved that income level affects forest tourism demand [12]. The higher the income level, the greater the demand for forest parks in the region.

<!-- b000326 | prose | pages [14] -->
Transportation Convenience (TC) The convenience of transportation is an important factor affecting tourists, which plays a decisive role in tourists' choice of traveling psychologically. Without safe and convenient transportation, it is impossible to have large-scale and long-term development of tourism economy. Then it will not be able to play its advantages, no matter how big the potential of tourism resources is. According to research [13], we define the calculation formula of transportation convenience as

<!-- b000327 | prose | pages [14] -->
where

<!-- b000328 | prose | pages [14] -->
(24)

<!-- b000329 | furniture | pages [14] -->


<!-- b000330 | prose | pages [14] -->
is the speed of all modes of transportation. is various modes of transportation.

<!-- b000331 | prose | pages [14] -->
is the passenger capacity of all modes of transportation. transportation.

<!-- b000332 | prose | pages [14] -->
Environmental Quality (EQ)

<!-- b000333 | prose | pages [14] -->
is the holding of various means of

<!-- b000334 | prose | pages [14] -->
As people pay increasing attention to health, the forest environment of forest park is becoming more and more important factor to attract people to choose forest park. We measure the environmental quality of the forest by the annual air quality index (AQI) of the selected forest.

<!-- b000335 | furniture | pages [14] -->


<!-- b000336 | prose | pages [14] -->
Thus, the calculation formula of recreational value is

<!-- b000337 | prose | pages [14] -->
where

<!-- b000338 | furniture | pages [14] -->


<!-- b000339 | prose | pages [14] -->
(25)

<!-- b000340 | prose | pages [14] -->
is the weight of four indicators respectively.

<!-- b000341 | furniture | pages [14] -->


<!-- b000342 | furniture | pages [14] -->


<!-- b000343 | heading | pages [15] -->
6.2.5 Data Processing and Weight Determination

<!-- b000344 | prose | pages [15] -->
To eliminate the effects of dimensions and dimensions, we need to normalize the indicators. However, since not every indicator is bigger, the better, we also need to carry out forward processing for indicators at the same time. Below we give different data processing methods.

<!-- b000345 | prose | pages [15] -->
For higher-is-better indicators, we take:

<!-- b000346 | prose | pages [15] -->
where

<!-- b000347 | furniture | pages [15] -->


<!-- b000348 | prose | pages [15] -->
(26)

<!-- b000349 | prose | pages [15] -->
𝑦𝑚,𝑛 represents the original value of item 𝑛 in region . 𝑟𝑚𝑖𝑛 represents the minimum value of item n in all years. 𝑟𝑚𝑎𝑥 represents the maximum value of item n in all years.

<!-- b000350 | prose | pages [15] -->
For smaller-is-better indicators, which are opposite to above one, positive transformation is required:

<!-- b000351 | furniture | pages [15] -->


<!-- b000352 | prose | pages [15] -->
(27)

<!-- b000353 | prose | pages [15] -->
The determination of indicator weight plays an important role, which directly affects the accuracy of evaluation results. Entropy weight method (EWM) is an objective weighting method. We use it to determine the weight of indicators. We select 10 forests in the world and get the data from the forestry bureau of each country and related survey reports. Then, we calculate the weight of each indicator by MATLAB. Table 3 shows the results.

<!-- b000354 | caption | pages [15] -->
Table 3: The weight of each indicator

<!-- b000355 | furniture | pages [15] -->


<!-- b000356 | prose | pages [15] -->
Carbon sequestration value

<!-- b000357 | prose | pages [15] -->
Biodiversity value

<!-- b000358 | prose | pages [15] -->
The Value of

<!-- b000359 | prose | pages [15] -->
Cultural value

<!-- b000360 | prose | pages [15] -->
Forests

<!-- b000361 | prose | pages [15] -->
Recreational value

<!-- b000362 | furniture | pages [15] -->


<!-- b000363 | furniture | pages [15] -->


<!-- b000364 | prose | pages [15] -->
Carbon sequestration 1.0000

<!-- b000365 | prose | pages [15] -->
Species richness 0.4992

<!-- b000366 | furniture | pages [15] -->


<!-- b000367 | prose | pages [15] -->
Species density 0.1879 Ecosystem complexity 0.3129

<!-- b000368 | prose | pages [15] -->
Education input 0.0715

<!-- b000369 | furniture | pages [15] -->


<!-- b000370 | prose | pages [15] -->
Health level 0.2792 Cultural heritage 0.6439

<!-- b000371 | prose | pages [15] -->
Population density 0.5220 Income level 0.1485

<!-- b000372 | furniture | pages [15] -->


<!-- b000373 | prose | pages [15] -->
Transportation

<!-- b000374 | prose | pages [15] -->
0.2076 convenience

<!-- b000375 | prose | pages [15] -->
Environmental quality 0.1219

<!-- b000376 | heading | pages [15] -->
6.3 Forest Management Evaluation Model

<!-- b000377 | heading | pages [15] -->
6.3.1 Scoring Method of Forest Management Value Realization

<!-- b000378 | prose | pages [15] -->
In order to balance the various value methods of forests and enable forest managers to make the best use of forests, we weighted the above four values and measured the merits and demerits of forest management methods through the total score. What we get above is the total value of each forest in the selected forest, and our forest management plan should include the percentage of area that the forest is used to realize each value. Therefore, after the implementation of the management plan, the value of each value really realized in the selected forest should be:

<!-- b000379 | prose | pages [15] -->
(28)

<!-- b000380 | furniture | pages [15] -->


<!-- b000381 | prose | pages [16] -->
where

<!-- b000382 | prose | pages [16] -->
represents the true realization part of the h-type value.

<!-- b000383 | prose | pages [16] -->
is the calculation is the ratio of forest area for realizing the value of h-type to the total results of the h-type value. forest area

<!-- b000384 | prose | pages [16] -->
In order to make the score closer to the real situation, we use analytic hierarchy process (AHP) to analyze the importance of these four values and then get the weight of each value.

<!-- b000385 | prose | pages [16] -->
We can express the final total score as

<!-- b000386 | prose | pages [16] -->
(29)

<!-- b000387 | furniture | pages [16] -->


<!-- b000388 | prose | pages [16] -->
Except for carbon sequestration value, the order of the deforestation degree caused by the realization of the other three values is generally . Regardless of the daily care of and the rest is 0, then the whole forest is used for biodiversity conservation the forest, if , the forest will suffer severe damage and many trees and we do not cut trees. Conversely, if will be cut down. But obviously the occurrence of these two extremes is not conducive to the utilization of forests. We need to construct a personalized judgment matrix according to the characteristics and geographical location of different forests and their importance to get the weight of different values of selected forests.

<!-- b000389 | furniture | pages [16] -->


<!-- b000390 | heading | pages [16] -->
6.3.2 The Cost of Realizing Value

<!-- b000391 | prose | pages [16] -->
When realizing the value mentioned above, certain capital investment is necessary, that is, cost. The cost calculation method is relatively simple. We need to collect , the cost per unit area needed to realize the h-type value of the selected forest. After collecting the data, we can normalize it by

<!-- b000392 | furniture | pages [16] -->


<!-- b000393 | prose | pages [16] -->
(30)

<!-- b000394 | prose | pages [16] -->
To calculate the cost score of the implementation plan, we sum the product of the area ratio . The larger the score is, the higher the cost will be. and capital

<!-- b000395 | furniture | pages [16] -->


<!-- b000396 | furniture | pages [16] -->


<!-- b000397 | prose | pages [16] -->
(31)

<!-- b000398 | heading | pages [16] -->
6.3.3 Transition Points for Different Management Plans

<!-- b000399 | prose | pages [16] -->
What kind of management plan is best? It is not enough to only consider the realization of value. For different forest managers, they need to make trade-offs between the value and the cost. There are transition points for different plans according to the recommended degree of plans.

<!-- b000400 | prose | pages [16] -->
In order to show the relationship between value and cost vividly, we use GE matrix to evaluate the plan. GE matrix is initially used for planning and analysis of the business portfolio of strategic public institutions. The vertical axis is industrial attraction, and the horizontal axis is business strength. The evaluation is based on the competitive strength of specific business modules and the attractiveness in the market. We use the horizontal axis as value score and the vertical axis as cost score to evaluate management plan from these two dimensions.

<!-- b000401 | prose | pages [16] -->
Since each forest can realize different maximum value score and maximum cost score, we set the maximum and minimum of the horizontal axis as and for the vertical axis, they are into three levels respectively, as shown in Table.

<!-- b000402 | prose | pages [16] -->
, . Then we divide Value and Cost

<!-- b000403 | caption | pages [17] -->
Table 4: Level classification of Value and Cost

<!-- b000404 | prose | pages [17] -->
Value Level

<!-- b000405 | furniture | pages [17] -->


<!-- b000406 | prose | pages [17] -->
Low

<!-- b000407 | prose | pages [17] -->
Medium

<!-- b000408 | furniture | pages [17] -->


<!-- b000409 | prose | pages [17] -->
High

<!-- b000410 | prose | pages [17] -->
Cost Level Low

<!-- b000411 | furniture | pages [17] -->


<!-- b000412 | prose | pages [17] -->
Medium

<!-- b000413 | prose | pages [17] -->
High

<!-- b000414 | furniture | pages [17] -->


<!-- b000415 | prose | pages [17] -->
We can divide the GE matrix into nine regions, and we use can coordinates to represent the plan, which have different meanings when they fall in different regions. In theory, the point with the lowest in Figure 7) is the best. cost and highest value (point If classifying simply, we can divide them into three types: high value cost ratio (blue area), medium value cost ratio (gray area) and low value cost ratio (red area). The plan falling in the blue zone is the best, with less input and more output. And we should not adopt the plan falling in the red zone with high cost and low forest value.

<!-- b000416 | prose | pages [17] -->
There are transition points for forest management plans applicable to various forests.

<!-- b000417 | caption | pages [17] -->
Figure 7: The GE matrix

<!-- b000418 | prose | pages [17] -->
When determine a forest management plan, its coordinates should fall in the blue zone. When we adjust the proportion of various values in the plan, the realized value and cost of the plan will also change, and its coordinates will move in the GE matrix. In the process of change, the plan may move from a blue zone to a gray zone, or even to a red zone. It means that the plan changes from enforceable to unenforceable. And this situation is the same for every forest.

<!-- b000419 | prose | pages [17] -->
The characteristics of different forests and their location influence the transition points of forest management plans. For different forests, their characteristics and location will significantly affect the weight obtained by AHP, which can be understood as different advantages of different forest to develop values. Similarly, each forest requires different value development costs. Therefore, the transition points between the calculated value and cost are different in each forest. Every forest has a personalized GE matrix to judge the feasibility of the plan.

<!-- b000420 | prose | pages [17] -->
Different forest managers may make different decisions. Forest managers can be individuals, governments, enterprises or other organizations. Different managers may value different things. For example, when making decisions, the government pays more attention to the social benefits brought by the management plan, so the government will stress the importance of the value, even if the cost is higher. However, enterprises may pay more attention to cost and want to maximize profits with the least cost.

<!-- b000421 | furniture | pages [17] -->


<!-- b000422 | heading | pages [17] -->
7 Case study: Greater Khingan Mountains

<!-- b000423 | heading | pages [17] -->
7.1 The Current Situation of Greater Khingan Mountains

<!-- b000424 | prose | pages [17] -->
Greater Khingan Mountains is one of China's most important forestry bases, covering an area of 327,200 square kilometers. The main trees are Xing’an larch, Mongolian oak, white birch, etc. According to statistics, the total amount of forest carbon sequestration in Greater Khingan Mountains is about 1.72 billion tons. The vast virgin forest is home to a wealth of species.

<!-- b000425 | prose | pages [18] -->
According to the survey, there are 56 species of mammals and 250 species of bird resources in the forest, as well as 1,069 plant species in the forest. We can see that the forest has a large number of species, including many rare species, which has a high value of species diversity. Apart from this, the biomass density also reached 59.92 . What’s more, according to the relevant investigation report, there are 13 types of vegetation in it, which can meet the specific living conditions of different organisms.

<!-- b000426 | heading | pages [18] -->
7.2 Analysis of Carbon Sequestration after 100 Years

<!-- b000427 | prose | pages [18] -->
of Xing’an larch, white birch and Mongolian oak are 83.755, The stock volume per unit area 87.29 and 37.34, respectively [14]. Table 5 shows forest products’ raw materials and lifespans[15].

<!-- b000428 | caption | pages [18] -->
Table 5: Forest products made from its main trees and their lifespans

<!-- b000429 | prose | pages [18] -->
Forest products The type of trees Lifespan (year)

<!-- b000430 | prose | pages [18] -->
Building materials Mongolian oak 80 Furniture 25

<!-- b000431 | prose | pages [18] -->
Building materials 65 House

<!-- b000432 | prose | pages [18] -->
Xing’an larch

<!-- b000433 | prose | pages [18] -->
50 Pillow 20

<!-- b000434 | prose | pages [18] -->
Bed 50 Desk and chair

<!-- b000435 | prose | pages [18] -->
White birch

<!-- b000436 | prose | pages [18] -->
40 Paper 10 The age distribution of trees in Greater Khingan Mountains shows that the number of trees in the middle age is the largest, while others are less. We take this age distribution as the initial age distribution of trees in the forest, and number unit area according to the differences in age and species of trees in different areas. In the calculation, we choose Xing’an larch, white birch and Mongolian oak to calculate. Figure 8(a) shows the corresponding relationship between tree species and initial age and region . Using the collected data, we calculate the optimal management plan for carbon sequestration in the next 100 years and calculate the final carbon sequestration amount. There is no unique optimal plan to achieve the maximum carbon sequestration. The difference between them is the area  selected by felling trees of the same type and age in the same year, which has no influence on the results. We choose one of the plans, and the results are as follows. Figure8(b) shows the corresponding relationship between area  and the ages of trees surviving after 100 years.

<!-- b000437 | prose | pages [18] -->
(a)Start

<!-- b000438 | furniture | pages [18] -->


<!-- b000439 | furniture | pages [18] -->


<!-- b000440 | furniture | pages [18] -->


<!-- b000441 | prose | pages [18] -->
(b)End

<!-- b000442 | caption | pages [18] -->
Figure 8: The relationship between area  and the ages of trees

<!-- b000443 | prose | pages [19] -->
According to the age, we can calculate the carbon sequestration accumulation of the surviving . Then, based on the obtained value of forest after the 100 years , and , we can get the contribution to carbon sequestration after the death of trees and the total carbon sequestration of forest products within the last year . Thus, we can obtain the total carbon sequestration after 100. Table 6 shows the results.

<!-- b000444 | furniture | pages [19] -->


<!-- b000445 | caption | pages [19] -->
Table 6: Carbon sequestration after 100 years

<!-- b000446 | furniture | pages [19] -->


<!-- b000447 | prose | pages [19] -->
19.9513 7.2873

<!-- b000448 | furniture | pages [19] -->


<!-- b000449 | furniture | pages [19] -->


<!-- b000450 | furniture | pages [19] -->


<!-- b000451 | furniture | pages [19] -->


<!-- b000452 | furniture | pages [19] -->


<!-- b000453 | prose | pages [19] -->
15.402 42.6406

<!-- b000454 | heading | pages [19] -->
7.3 The Optimal Forest Management Plan

<!-- b000455 | prose | pages [19] -->
Based on the best Forest Management model, we collect data from the China Forestry Administration and the World Bank on Greater Khingan Mountains, and we calculate the values are 0.7533, 0.8124, 0.3736, 0.4962 respectively. of , , , Then, we obtain the superiority of various forest values in Greater Khingan Mountains by referring to relevant data. Through AHP, we obtain the weights of secondary indicators , , are 0.3214, 0.2857, 0.25, 0.1429 respectively. The large weight of , and probably because that China is implementing "carbon neutrality" and "carbon peak" strategy, which attaches great importance to the reduction of carbon emissions. Carbon sequestration can effectively alleviate this problem. As mentioned above, Greater Khingan Mountains is rich in biological species and has significant biodiversity value.

<!-- b000456 | prose | pages [19] -->
According to the studies on the development costs of forest values in China [16,17,18,19], we can obtain that the of realizing , , , , are 0.07, 0.58, 0.26 and 0.09, respectively. Then we set up different plans for forest utilization in Greater Khingan Mountains. By of different plans and marking them in GE matrix, the plan closest calculating the and is the best management plan. In order to make full use of the various forest values, we to point make the proportion of the implementation area of each value less than 10% of the total area. Based on the above conditions, we can build a nonlinear programming model and use genetic algorithm to search for the global optimal solution.

<!-- b000457 | prose | pages [19] -->
Figure 9(a) shows the results of the genetic algorithm. Therefore, the optimal plan finally obtained is that 58.95% area is for sequestering carbon, 11.20% area is for biodiversity, 11.41% area is for cultural industry and 18.37% area is for entertainment industry. The and

<!-- b000458 | furniture | pages [19] -->


<!-- b000459 | prose | pages [19] -->
are 0.1924 and 0.1524 respectively, and their positions on GE matrix are shown in Figure 9(b). We can see that this plan falls in the blue area and is very close to the point . It is a highly feasible plan and can obtain the highest value with the lowest investment cost.

<!-- b000460 | prose | pages [20] -->
(a)

<!-- b000461 | furniture | pages [20] -->


<!-- b000462 | furniture | pages [20] -->


<!-- b000463 | furniture | pages [20] -->


<!-- b000464 | prose | pages [20] -->
(b)

<!-- b000465 | caption | pages [20] -->
Figure 9: The optimal forest management plan to greater khingan mountains

<!-- b000466 | prose | pages [20] -->
Based on the above results, we propose the following recommendations for forest managers. First, forest managers should focus on the protection of forest trees by classifying more than half of the forest area as forbidden zones to achieve the carbon sequestration function of forests. We learned that commercial logging of natural forests has been suspended in the Greater Khingan Mountains since 2015. The aim is to strengthen forest management, protect forest vegetation and improve forest carbon sequestration capacity. According to our analysis of carbon sequestration in 100 years, we should cut down the corresponding proportion of trees to make forest products in Greater Khingan Mountains to further improve its carbon sequestration capacity.

<!-- b000467 | prose | pages [20] -->
Second, make use of its recreational value and properly develop ecological tourism. There are five types of monopolistic tourism resources in Greater Khingan Mountains, including alpine snow and ice, northern lights and other characteristic landscapes [20]. These distinctive tourism resources are the best carriers for developing forest eco-tourism. When developing, focus on the protection, combining protection and reasonable development. Besides, improve the surrounding traffic network and increase publicity to attract more tourists.

<!-- b000468 | prose | pages [20] -->
In addition, part of the area is devoted to protecting biodiversity and developing cultural industries. For biodiversity conservation, forest managers can strengthen advocacy and raise public awareness of biodiversity; If the manager is the government, it should strengthen legislation and law enforcement, improve the protection system, and strengthen the construction of nature reserves. For cultural value, Oroqen culture is unique to the Greater Khingan Mountains [21], and it should be protected. We can combine it with tourism development, plan and develop cultural tourism resources to propagate and inherit the excellent traditional culture.

<!-- b000469 | heading | pages [20] -->
7.4 The Modification of the Optimal Plan

<!-- b000470 | prose | pages [20] -->
According to the problem restatement, we will allow logging for 10 years longer than the on the original basis. So, we need to modify our optimal current practice, that is to add 10 to the plan. The limitation of this condition will lead to the change of recalculation. The proportion of , which is 0.6511 after and in modified plan is 55.87%, 10.23%, 10.11% and 23.71%, respectively. The calculated and is 0.1667 and 0.1461, respectively, which is still in the blue region of the GE matrix.

<!-- b000471 | furniture | pages [20] -->


<!-- b000472 | furniture | pages [20] -->


<!-- b000473 | furniture | pages [21] -->


<!-- b000474 | furniture | pages [21] -->


<!-- b000475 | prose | pages [21] -->
(a)                                                                       (b)

<!-- b000476 | caption | pages [21] -->
Figure 10: The modification of the optimal plan

<!-- b000477 | prose | pages [21] -->
We can find that the big change between the old and new management plans is the proportion is not as much as before. In order to make the forest realize of and . The calculated is reduced and more value, the proportion of is increased. To make forest managers and people who use forests adapt this change, we will discuss a sensitive strategy for them to satisfy their needs. They may be governments, enterprises and individuals. For the government, as the area of decreases and the reduced area is used to develop tourism industry, it is necessary to strengthen the protection of undeveloped forest areas. It can issue relevant laws to regulate the development behavior to avoid the impact of tourism development on the surrounding environment. For enterprises, they may be the developers of . As the tourism area becomes larger, enterprises should adopt more effective publicity means, give consumers various preferential policies, highlight the regional characteristics of the forest to attract more tourists. Individuals should develop a good sense of environmental protection. When playing in the forest park, do not destroy the trees in the park, consciously protect the environment.

<!-- b000478 | furniture | pages [21] -->


<!-- b000479 | heading | pages [21] -->
8 Sensitivity Analysis

<!-- b000480 | prose | pages [21] -->
To verify the robustness and validity of our model, we do sensitivity analysis on our model. First, we conduct sensitivity analysis on the value. Greater Khingan Mountains is rich in from 0.81 to 0.99 with a step of 0.02, and observe the biodiversity, so we artificially raise the change of forest management plan. Figure 11(a) shows the results. We can see that as the goes goes up, and there will be more areas of the forest dedicated to up, the optimal plan changes, biodiversity conservation. So, our model can make different decisions as the value changes. However, due to the high cost of conservation, the small fluctuation range of biodiversity value, and the low cost of carbon sequestration value, the plan is mainly based on carbon sequestration value. The plan changes within a small overall range, and the model is robust.

<!-- b000481 | prose | pages [21] -->
Next, we also conduct sensitivity analysis on cost. As mentioned above, the low cost of carbon sequestration value causes the plan to remain basically unchanged. Therefore, we increase the

<!-- b000482 | prose | pages [21] -->
from 0.07 to 0.23 with a step of 0.02, and change the remaining costs as the original proportion. Figure 11(b) shows the results. We find that in the early rise stage of , the plan basically does not change. However, when it rises to the 0.13, the plan changes significantly:

<!-- b000483 | furniture | pages [21] -->


<!-- b000484 | prose | pages [21] -->
falls, and the other two basically remains the same. In the later period, rises, even surpasses and become the dominant value. We also conduct similar analysis on other costs and got similar results. Therefore, we can see that our model has strong effectiveness and high credibility, which can timely modify the plan and always make the value and cost reach an optimal value.

<!-- b000485 | furniture | pages [22] -->


<!-- b000486 | furniture | pages [22] -->


<!-- b000487 | prose | pages [22] -->
(a) (b)

<!-- b000488 | caption | pages [22] -->
Figure 11: Sensitivity analysis

<!-- b000489 | furniture | pages [22] -->


<!-- b000490 | heading | pages [22] -->
9 Strengths and Weaknesses

<!-- b000491 | heading | pages [22] -->
9.1 Strengths

<!-- b000492 | prose | pages [22] -->
⚫ The carbon sequestration model is scientific and comprehensive. We use the conversion factor

<!-- b000493 | prose | pages [22] -->
method of forest stock volume to calculate carbon sequestration, which not only considers the contributions of trees and forest products, but also understory plants and soil, fitting the reality. ⚫ The forest management model for carbon sequestration can simulate the dynamic change

<!-- b000494 | prose | pages [22] -->
process of forest management and obtain the reliable optimal plan. Indicators influence and constrain each other. The simulation process is close to the reality, and the factors we considered are comprehensive. ⚫ The forest management model for society fully considers the value of forests. We select

<!-- b000495 | prose | pages [22] -->
multiple indicators from three aspects to quantify it, which is conducive to analyze and develop personalized forest management plan more effectively. It is objective to assign weight to indicators by entropy weight method. ⚫ The use of GE matrix, considering both value and cost dimensions, is beneficial to provide

<!-- b000496 | prose | pages [22] -->
different decision-making suggestions for different forest managers. Meanwhile, we can easily obtain the transition points of different plans from GE matrix and intuitively judge the feasibility of the plan. ⚫ We conduct sensitivity analysis on the model, and find that our model has good robustness in

<!-- b000497 | prose | pages [22] -->
a small fluctuation range. It also can make different forest management plans according to the changes in value and cost, which is highly effective and practical.

<!-- b000498 | heading | pages [22] -->
9.2 Weaknesses

<!-- b000499 | prose | pages [22] -->
⚫ We believe that fixed in forest products will return to the atmosphere after they reach their life span, regardless of their specific treatment methods, such as landfill and combustion. Different treatment methods may lead to different remaining carbon sequestration amount of forest products after their lifespan. For example, may soil can absorb part of the carbon from landfill, and the carbon fixed by forest products will not completely disappear. ⚫ The forest management model only considers the development cost without the maintenance

<!-- b000500 | prose | pages [22] -->
cost after development.

<!-- b000501 | furniture | pages [22] -->


<!-- b000502 | heading | pages [22] -->
10 A Newspaper Article

<!-- b000503 | furniture | pages [23] -->


<!-- b000504 | furniture | pages [23] -->


<!-- b000505 | prose | pages [23] -->
A

<!-- b000506 | prose | pages [23] -->
child went into the garden and saw his grandfather on the ladder cutting off some branches of the tree. The child picked up a branch and said, "Grandpa, it’s a pity to cut them off!" "Silly boy," said the grandfather, "thus the tree will grow better." Some people think that deforestation is harmful, but in fact, like pruning, appropriate deforestation is beneficial to ecology and society.

<!-- b000507 | prose | pages [23] -->
The proper logging here refers to forest ecological logging.

<!-- b000508 | prose | pages [23] -->
Simply speaking, it is a targeted and selective logging activity that strictly follows the law of ecological development. Through logging, carbon sequestration in forests can be transferred to forest products throughout their life cycle. Based on this, our team developed the forest management model for carbon sequestration. We used this model to study the Greater Khingan Range.

<!-- b000509 | prose | pages [23] -->
After 100 years, its carbon sequestration of forest is 2.724 billion tons, and that of forest products is 1.540 billion tons, indicating that forest products can sequester a large part of the carbon. This is because some forest

<!-- b000510 | furniture | pages [23] -->


<!-- b000511 | prose | pages [23] -->
products may last longer than trees, and the carbon sequestered in some forest products coupled with the regeneration of young forests has the potential to sequester more carbon over time. So, cutting down trees properly is a sensible choice for carbon sequestration.

<!-- b000512 | prose | pages [23] -->
Apart from this, forests also have many other use values, such as biodiversity value, cultural value and recreational value. The best forest management plan for carbon sequestration is not necessarily the best one for society. We should balance the values of forests and make full use of their advantages. Our team also built a forest management model for society that considered four values, balancing both value and cost. We also applied this model to the Greater Khingan Range and developed a management plan: 55.87%, 10.23%, 10.11% and 23.71% for carbon sequestration, biodiversity, cultural and recreational value, respectively. It can be seen that our management plan can not only bring ecological benefits to the local area, but also bring huge economic and cultural benefits, which is conducive to the development of the region and has great potential for the improvement of living standards and cultural standards. Of course, a proper cutting down of trees is also a necessary condition to achieve this goal. We should believe that logging a small number of trees can indeed bring great benefits!

<!-- b000513 | prose | pages [23] -->
You may have disagreed with the idea of cutting down trees, but after reading this report, you will have a better understanding of the benefits of cutting down trees properly.

<!-- b000514 | heading | pages [24] -->
References

<!-- b000515 | references | pages [24] -->
[1] A large and persistent carbon sink in the world's forests[J]. Science, 2011, 333(Aug.19

<!-- b000516 | references | pages [24] -->
TN.6045):988-993.

<!-- b000517 | references | pages [24] -->
[2] Wang Li, Wang Haiyang, Chang Xin. Garden tree species common carbon sequestration

<!-- b000518 | references | pages [24] -->
ability to release oxygen makes analysis [J]. Journal of southern agriculture, 2012, 6 (05) : 54-56

<!-- b000519 | references | pages [24] -->
[3] J  Chen,  Yang H . Advances and frontiers in global forest and harvested wood products

<!-- b000520 | references | pages [24] -->
carbon science[J]. Journal of Nanjing Forestry University (Natural Sciences Edition),

<!-- b000521 | references | pages [24] -->
2018,42(04):1-8.

<!-- b000522 | references | pages [24] -->
[4] Wang D C, Zhang Z K, Yang Q, Cun D Z, Guo D Y, Zhao G L. Forest carbon sequestration

<!-- b000523 | references | pages [24] -->
and its change in Dehong County, China from 2016 to 2019 [J]. Green science and technology,

<!-- b000524 | references | pages [24] -->
2020 (22) : 261-263.

<!-- b000525 | references | pages [24] -->
[5] Cramer J S . The Origins and development of the Logit Model[M].  2003.

<!-- b000526 | references | pages [24] -->
[6] FAO. Global forest resources assessment 2005.progress towards sustainable forest

<!-- b000527 | references | pages [24] -->
management[R].Rome: Food and Agriculture Organization,2006:129-154

<!-- b000528 | references | pages [24] -->
[7] ” The main components of biodiversity” [OL]. Available: http://www.greentimes.com/gr

<!-- b000529 | references | pages [24] -->
een/swdyx/2012-02/06/content_165721.htm

<!-- b000530 | references | pages [24] -->
[8] Simpson, e. Measurement of diversity[J]. Nature 163, 688 (1949).

<!-- b000531 | references | pages [24] -->
[9] Edwards D. Social and cultural values associated with European forests in relation to key

<!-- b000532 | references | pages [24] -->
indicators of sustainability[R]. Joensuu, Finland: European Forest Institute ,2011:26-54.

<!-- b000533 | references | pages [24] -->
[10] Huang Xiujuan, Lin Xiuzhi. Chinese forest park tourism efficiency and its influencing

<!-- b000534 | references | pages [24] -->
factors [J]. Scientia silvae sinicae,2015,51(02):137-146.

<!-- b000535 | references | pages [24] -->
[11] Song Chen, Jiyue Li, Jinpu Jiang, Dawei Chen. Simulate tourist market and tourist

<!-- b000536 | references | pages [24] -->
behavior characteristics [J]. Hebei Forest and Fruit Research,2007(01):111-116.

<!-- b000537 | references | pages [24] -->
[12] Luo M C ,  Luo J ,  Zhong Y D , et al. A comparative study of visitor characteristics in

<!-- b000538 | references | pages [24] -->
different types of forest parks[J]. Journal of Central South Forestry University, 2005.

<!-- b000539 | references | pages [24] -->
[13] Haibin Xia, Xiaoye Dai, Ying Wang, Zheng Wang. Transportation convenience analysis

<!-- b000540 | references | pages [24] -->
at county level in China based on GIS [J]. Areal Research and Development,2006(03):120-

<!-- b000541 | references | pages [24] -->
124+130.

<!-- b000542 | references | pages [24] -->
[14] Wang Wenbo, Jiang Xilin, Zhao Pengwu. Estimation of forest carbon storage based on

<!-- b000543 | references | pages [24] -->
continuous forest inventory: A case study of Hulunbuir Region, Inner Mongolia [J]. Journal of

<!-- b000544 | references | pages [24] -->
northeast forestry university,2015,43(07):116-119.

<!-- b000545 | references | pages [25] -->
[15] Bai Y F. Carbon storage of wood forest products in China [D]. Chinese Academy of

<!-- b000546 | references | pages [25] -->
Forestry,2010.

<!-- b000547 | references | pages [25] -->
[16] Gu Rong, Gao Jun, Zhang Songhe, et al. Cost-effectiveness of Coastal wetland Nature

<!-- b000548 | references | pages [25] -->
Reserve -- A case study of Yancheng Wetland Rare Birds National Nature Reserve in Jiangsu

<!-- b000549 | references | pages [25] -->
Province [J]. Journal of ecology and rural environment,2014,30(1):32-37.

<!-- b000550 | references | pages [25] -->
[17] Wu Jing. Study on cost and benefit of eco-tourism in Qinling Mountains [D]. Beijing

<!-- b000551 | references | pages [25] -->
Forestry University,2015.

<!-- b000552 | references | pages [25] -->
[18] Zhou Ying. Research on economic value evaluation of cultural heritage tourism resources

<!-- b000553 | references | pages [25] -->
[D]. Dalian University of Technology,2014.

<!-- b000554 | references | pages [25] -->
[19] Liu H ,  Wu S ,  Yu T . Methodology study of forest conservation carbon sequestration

<!-- b000555 | references | pages [25] -->
projects[J]. World Forestry Research, 2018.

<!-- b000556 | references | pages [25] -->
[20] Li Gengxin, LI Siqiu, Wang Zao. Development of forest tourism industry in Greater

<!-- b000557 | references | pages [25] -->
Khingan Range [J]. China Forestry Enterprises,2005(02):34-36.

<!-- b000558 | references | pages [25] -->
[21] LI Yuanyuan, YU Huimin. Research on Oroqen cultural tourism resources development

<!-- b000559 | references | pages [25] -->
in Greater Khingan Range [J]. China Ethnic Expo,2019(02):57-58.

<!-- b000560 | furniture | pages [25] -->

