# P-E-2022-2202838-75410db9

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2022

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
E

<!-- b000005 | title | pages [1] -->
2202838

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
What a Forest Management Plan!

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
"Trees are unguilty. You destroy them. You are guilty!" Some argue that we should not cut down trees at all to mitigate climate change, but in fact, proper logging is necessary and beneficial. Through establishing models, we demonstrate that forest management plans including harvesting can balance the carbon sequestration (CS) and the realization of other values.

<!-- b000010 | prose | pages [1] -->
First, we establish a Carbon Sequestration Model to obtain the amount of CS including forest and forest products. In the calculation, we use the Conversion Factor Method (CFM) of forest stock volume, comprehensively considering trees, understory plants and wood soil. And we use a logical growth model to express the CS capacity and tree age to obtain a more real value. By adding the CS of forests and forest products, we can obtain the total amount of CS in year .

<!-- b000011 | prose | pages [1] -->
Then, we establish a Forest Management Model for Carbon Sequestration combining the idea of Dynamic Objective Programming. We divide the forest into regions, using , and to store information about cut or not, tree age, and death or not respectively. These variables affect each other. Combined with them and the CS model, we can obtain the amount of CS in statistical time, which is our objective function. Then, we get the optimal management plan by searching the optimal solution to the function.

<!-- b000012 | prose | pages [1] -->
To comprehensively consider other forest values, we establish a Forest Management Model for Society. And we create a three-level evaluation indicator system, including four second-level indicators (carbon sequestration, biodiversity, cultural and recreational value) and 10 third-level indicators. We determine the weight of each third-level indicator by Entropy Weight Method. Considering different characteristics and geographical location of each forest, we use the Analytic Hierarchy Process to get the value score by weighting the secondary indicators to make the score closer to the real situation. Meanwhile, we use GE Matrix to evaluate the forest management plan based on the cost of realizing the value, and get transition points of different plans. By optimizing the distance between the plan and the optimal point in GE matrix, we obtain the optimal forest management plan for society, which may vary for different forest managers.

<!-- b000013 | prose | pages [1] -->
Next, we apply our models to the Greater Khingan Mountains. And we obtain that the total CS of forest and its products after 100 years is 4.264 billion tons, among which the CS of forest is 2.724 billion tons and that of its products is 1.540 billion tons. Then we establish a Nonlinear Programming Model and use Genetic Algorithm to get the best forest management plan: the ratio of the four regions realizing the value is 58.95%, 11.20%, 11.41% and 18.37%, respectively. Allowing logging 10 years longer than current practices, we modify the management plan to provide forest managers and all those who use forests with strategies to meet their needs.

<!-- b000014 | prose | pages [1] -->
In the end, we write a newspaper article to explain our optimal forest management plan.

<!-- b000015 | keywords | pages [1] -->
Keywords: Carbon Sequestration, Forest Management Model for Carbon Sequestration or Society,

<!-- b000016 | prose | pages [1] -->
Objective Programming, GE Matrix

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1 Introduction ................................................................................................................................. 3

<!-- b000019 | contents | pages [2] -->
1.1 Background ......................................................................................................................... 3

<!-- b000020 | contents | pages [2] -->
1.2 Problem Restatement .......................................................................................................... 3

<!-- b000021 | contents | pages [2] -->
1.3 Our Work ............................................................................................................................ 4

<!-- b000022 | contents | pages [2] -->
2 Assumption and Justifications ................................................................................................... 4

<!-- b000023 | contents | pages [2] -->
3 Notation ........................................................................................................................................ 4

<!-- b000024 | contents | pages [2] -->
4 Carbon Sequestration Model ..................................................................................................... 5

<!-- b000025 | contents | pages [2] -->
4.1 The Carbon Sequestration of Forests .................................................................................. 6

<!-- b000026 | contents | pages [2] -->
4.2 The Carbon Sequestration of Forest Products .................................................................... 7

<!-- b000027 | contents | pages [2] -->
4.3 Carbon Sequestration Capacity Factor ................................................................................ 7

<!-- b000028 | contents | pages [2] -->
5 Forest Management Model for Carbon Sequestration ............................................................ 9

<!-- b000029 | contents | pages [2] -->
5.1 Parameter Settings .............................................................................................................. 9

<!-- b000030 | contents | pages [2] -->
5.2 Construction of Objective Function .................................................................................. 10

<!-- b000031 | contents | pages [2] -->
6 Forest Management Model for Society ................................................................................... 11

<!-- b000032 | contents | pages [2] -->
6.1 Overview ........................................................................................................................... 11

<!-- b000033 | contents | pages [2] -->
6.2 The Value of Forests ......................................................................................................... 12

<!-- b000034 | contents | pages [2] -->
6.3 Forest Management Evaluation Model ............................................................................. 15

<!-- b000035 | contents | pages [2] -->
7 Case study: Greater Khingan Mountains ............................................................................... 17

<!-- b000036 | contents | pages [2] -->
7.1 The Current Situation of Greater Khingan Mountains ..................................................... 17

<!-- b000037 | contents | pages [2] -->
7.2 Analysis of Carbon Sequestration after 100 Years ........................................................... 18

<!-- b000038 | contents | pages [2] -->
7.3 The Optimal Forest Management Plan ............................................................................. 19

<!-- b000039 | contents | pages [2] -->
7.4 The Modification of the Optimal Plan .............................................................................. 20

<!-- b000040 | contents | pages [2] -->
8 Sensitivity Analysis .................................................................................................................... 21

<!-- b000041 | contents | pages [2] -->
9 Strengths and Weaknesses........................................................................................................ 22

<!-- b000042 | contents | pages [2] -->
9.1 Strengths ........................................................................................................................... 22

<!-- b000043 | contents | pages [2] -->
9.2 Weaknesses ....................................................................................................................... 22

<!-- b000044 | contents | pages [2] -->
10 A Newspaper Article ............................................................................................................... 22

<!-- b000045 | contents | pages [2] -->
References ..................................................................................................................................... 24

<!-- b000046 | heading | pages [3] -->
1 Introduction

<!-- b000047 | heading | pages [3] -->
1.1 Background

<!-- b000048 | prose | pages [3] -->
Global warming is bringing alarming consequences around the world, including more extreme events, the rise of sea levels and the increased threat of extinction of plant and animal species. In order to slow climate change and protect human environment, it is not enough to reduce carbon emissions. We should also consider how to increase the amount of carbon dioxide sequestered from the atmosphere, known as carbon sequestration.[1] As the main body of terrestrial ecosystems, forests store more than 45% of all terrestrial organic carbon, and their annual absorption of 𝐶𝑂2 through photosynthesis accounts for 2/3 of all terrestrial ecosystems. Forests play a very important role in the global carbon cycle. Through logging, fixed carbon in forests can be transferred to wood forest products, which can store carbon in the whole life cycle of forest products. The disturbance of human activities to the global carbon cycle in the 20th century is an unprecedented phenomenon in history. Understanding the global carbon cycle and its impact on human activities is important for developing viable climate change mitigation strategies.

<!-- b000049 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000050 | prose | pages [3] -->
In order to develop guidelines for forest managers around the world to try to figure out how to use and manage their forests, our group undertook the following work: ⚫ Design a carbon sequestration model to determine the amount of 𝐶𝑂2 that a forest and its forest products can sequester over time, and determine which forest management plans are most effective. ⚫ Develop a decision model to determine a forest management plan. Consider the following questions: what are the conditions that would prevent a forest from being cut down; whether there are transition points between management plans applicable to all forests; how to use the characteristics of a particular forest and its location to determine transition points between management plans. ⚫ Apply the model to a variety of forests. Determine how much 𝐶𝑂2 a forest and its products will absorb over a period of 100 years. Discuss what forest management plans should be adopted for the forest and strategies to achieve them, supposing the best management plan includes a time between harvests that is 10 years longer than current practices in the forest. ⚫ Write a non-technical newspaper article explaining the forest management plan.

<!-- b000051 | heading | pages [4] -->
1.3 Our Work

<!-- b000052 | caption | pages [4] -->
Figure 1: Our work

<!-- b000053 | heading | pages [4] -->
2 Assumption and Justifications

<!-- b000054 | prose | pages [4] -->
Assumption 1: We assume that the accumulated carbon sequestration of trees follows the logical growth model.

<!-- b000055 | prose | pages [4] -->
Justification: The CS capacity of trees is different with ages. Based on the literature [2], the capacity shows a trend of first increasing and then decreasing. We can conclude the accumulated amount of CS will increase rapidly first, then slow down, and finally reach a stable value, which is in line with the logical growth model.

<!-- b000056 | prose | pages [4] -->
Assumption 2: We divide the forest into small areas, and each area only plants one tree. If trees are cut down in one area, seedlings of the same type will be planted in the same area in the same year.

<!-- b000057 | prose | pages [4] -->
Justification: Because the number of areas with different ages and species of trees will change dynamically when trees are felled and new trees are planted. We make this assumption to simplify the model.

<!-- b000058 | prose | pages [4] -->
Assumption 3: When trees die, part of their CS is transferred to the land. And the CS of forest products returns to the atmosphere when they reach their lifespan.

<!-- b000059 | prose | pages [4] -->
Justification: A part of the organic carbon produced by photosynthesis of trees is fixed in the soil. This amount of CS is unaffected by the death of trees and remains still. To simplify the model, we assume forest products will release all to the atmosphere at the end of their life.

<!-- b000060 | heading | pages [4] -->
3 Notation

<!-- b000061 | prose | pages [4] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000062 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000063 | heading | pages [5] -->
Symbol

<!-- b000064 | prose | pages [5] -->
Description the total amount of carbon sequestration in year the carbon sequestration of forests in year the carbon sequestration of forest products in year the amount of forest carbon sequestration used for the p-type product in year the carbon sequestration of forest trees in year the carbon sequestration of understory plants in year .

<!-- b000065 | prose | pages [5] -->
the carbon sequestration of the wood soil in year the carbon sequestration capacity factor carbon sequestration value biodiversity value cultural value recreational value the cost per unit area needed to realize the h-type value of the selected forest

<!-- b000066 | heading | pages [5] -->
4 Carbon Sequestration Model

<!-- b000067 | prose | pages [5] -->
Before establishing carbon sequestration model, we need to understand the main approaches to sequestering carbon. It is reported that soils and plants sequester three times as much carbon as the atmosphere, with forests accounting for 45%. The world's forests absorbed more than a quarter of global carbon emissions between 2006 and 2015. Forest sequestration of carbon dioxide is dynamic: trees absorb 𝐶𝑂2 from the atmosphere through photosynthesis and convert it into biomass stored in different parts of the plant body [3].

<!-- b000068 | prose | pages [5] -->
Meanwhile, forest carbon sequestration continuously transfers among carbon pools. Natural disturbances, decay of dead wood, and forest respiration contribute to the release of 𝐶𝑂2 into the atmosphere. The carbon fixed by trees will be transferred to forest products due to logging, which will lead to the change of forest carbon sink. We can store the fixed carbon in wood forest products for different lengths of time depending on the end use. Therefore, forests and wood forest products are therefore an important component of the

<!-- b000069 | caption | pages [5] -->
Figure 2: The roles of forests and forest

<!-- b000070 | prose | pages [5] -->
global carbon cycle. Figure 2 shows the role products in the global carbon cycle of forests and forest products in the global carbon cycle.

<!-- b000071 | prose | pages [5, 6] -->
And we can define the total amount of carbon sequestration in year  as (1) where is the carbon sequestration of forests in year . is the carbon sequestration of forest products in year .

<!-- b000073 | heading | pages [6] -->
4.1 The Carbon Sequestration of Forests

<!-- b000074 | prose | pages [6] -->
There are many accounting formulas for forest carbon sequestration, such as 𝐶𝑂2 FIX model method, Carbon balance F-Corron model method, biomass conversion method, vortex correlation method and box method [4]. Based on previous studies, we adopt the conversion factor method of forest stock to calculate forest carbon sequestration by integrating operability, economy, long-term measurement and accuracy.

<!-- b000075 | prose | pages [6] -->
Forest trees, understory plants and the wood soil can all play a role in carbon sequestration. If investigating the carbon sequestration and sequestration effect of forests from the perspective of natural science, then we should integrate the sequestration effect of the three. Therefore, we can define the total carbon sequestration of forests in year 𝑡 as (2) where represents the carbon sequestration of forest trees in year . represents the carbon sequestration of understory plants in year . represents the carbon sequestration of the wood soil in year .

<!-- b000076 | heading | pages [6] -->
4.1.1 The Carbon Sequestration of Trees

<!-- b000077 | prose | pages [6] -->
Trees mainly perform photosynthesis and absorb 𝐶𝑂2 from the atmosphere through canopy leaves and convert it into biomass stored in different parts of the plant body. Therefore, we define the total carbon sequestration of trees in year  as

<!-- b000078 | prose | pages [6] -->
(3)

<!-- b000079 | prose | pages [6] -->
where represents the carbon sequestration of forest trees in region 𝑖 in year . represents the area in region 𝑖 in year . represents the carbon density of biomass in region 𝑖 in year .

<!-- b000080 | heading | pages [6] -->
4.1.2 The Carbon Sequestration of Understory Plants

<!-- b000081 | prose | pages [6] -->
Understory plants can also sequester carbon. On the other hand, they can also sequester carbon by absorbing organic matter from the soil. We define the total carbon sequestration of understory plants in year  as

<!-- b000082 | prose | pages [6] -->
(4)

<!-- b000083 | prose | pages [6] -->
where represents the carbon sequestration of understory plants in region 𝑖 in year . represents the effective area of understory plants in region 𝑖 in year . The formular is , where is the carbon conversion coefficient of understory plants. According to the default common values of the Intergovernmental Panel on Climate Change (IPCC), we take .

<!-- b000084 | heading | pages [7] -->
4.1.3 The Carbon Sequestration of the Wood Soil

<!-- b000085 | prose | pages [7] -->
Some of the organic carbon produced by photosynthesis in trees gets stuck in the soil. In addition. Therefore, soil carbon sequestration is also considerable. We define the total carbon sequestration of the wood soil in year t as

<!-- b000086 | prose | pages [7] -->
(5)

<!-- b000087 | prose | pages [7] -->
where represents the carbon sequestration of understory plants in region 𝑖 in year . represents the effective area of the wood soil in region 𝑖 in year . The formular is , where is the carbon conversion coefficient of the wood soil. According to IPCC, we take .

<!-- b000088 | heading | pages [7] -->
4.1.4 The Biomass Carbon Density

<!-- b000089 | prose | pages [7] -->
Forests store large amounts of carbon in their vast biomass. Measuring the forest community biomass and further estimating the biomass carbon density can measure the level of community productivity, which is the basis of studying the carbon cycle of forest ecosystem. We define the biomass carbon density of forest 𝑗 in region 𝑖 in year  as

<!-- b000090 | prose | pages [7] -->
(6) where represents the stock volume per unit area in region 𝑖 in year .  represents the biomass expansion coefficient, which can convert the tree stock volume into the biological stock volume of trees as the main body.  represents the volume coefficient, which can convert the total forest biomass into dry weight. represents carbon content, which can convert dry weight of the biomass into carbon sequestration. is the carbon sequestration capacity factor. We will further discuss it later. According to IPCC, we take .

<!-- b000091 | heading | pages [7] -->
4.2 The Carbon Sequestration of Forest Products

<!-- b000092 | prose | pages [7] -->
According to the life cycle theory, compared with concrete and steel, not only wood consumes less energy and emits less carbon during production and processing, but also its growth plays a role of carbon sequestration. Through logging, the carbon fixed in the forest can be transferred to wood forest products, which mainly include logs, sawn wood, pulp wood, wood-based panels and so on. Forest products can store carbon though the whole life cycle. We define the total carbon sequestration of forest products in year  as

<!-- b000093 | prose | pages [7] -->
(7)

<!-- b000094 | prose | pages [7] -->
where represents the amount of forest carbon sequestration used for the p-type forest product. The calculation formula is same to . is the processing loss rate in the production of the p-type forest product. is the number of forest product types.

<!-- b000095 | heading | pages [7] -->
4.3 Carbon Sequestration Capacity Factor

<!-- b000096 | prose | pages [7, 8] -->
In order to clarify the impact of tree age on carbon sequestration capacity, and then affect the carbon sequestration amount of the whole forest, we should consider the change of carbon sequestration amount with tree age. According to our assumption, the carbon sequestration capacity of trees first increases and then decreases, and the carbon sequestration amount finally tends to a stable value. Inspired by the population dynamic growth model [5], we express the relationship between carbon sequestration capacity and tree age as a logical growth function.

<!-- b000098 | prose | pages [8] -->
(8)

<!-- b000099 | prose | pages [8] -->
We define in Formula (9) as the amount of carbon sequestration at the maximum age of trees per unit area . Multiply it by and we can get the amount of carbon sequestration in year  per unit area. We can solve its differential equation by separating variables, and finally obtain the expression of as

<!-- b000100 | prose | pages [8] -->
(9)

<!-- b000101 | prose | pages [8] -->
where is the increasing rate of a tree’s carbon sequestration capacity. It is related to the size and type of the tree, which reflects the variation of carbon sequestration levels of different trees with tree age. is the carrying capacity, and we set . If the tree reaches full maturity (maximum tree age), then , representing that the maximum accumulated carbon sequestration. If the tree is first planted (the tree age is 0), then , and there is no carbon sequestration. is a constant. Based on the growth level of most trees, we take it 500.

<!-- b000102 | prose | pages [8] -->
According to the actual situation, we can determine the coefficients of different kinds of trees in differential equations. We can understand as accumulated carbon sequestration capacity, which we will use in subsequent model.

<!-- b000103 | prose | pages [8] -->
We take Greater Khingan Mountains to do case study of this model. Table 2 lists the main tree species, tree age and coefficient corresponding to the logical growth function of the forest.

<!-- b000104 | caption | pages [8] -->
Table 2: The related data of Forests of Greater Khingan Mountains

<!-- b000105 | prose | pages [8] -->
Cutting age Overmature age

<!-- b000106 | prose | pages [8] -->
Mongolian oak 60 120 0.1036 Xing’an larch 30 60 0.2072 White birch 15 30 0.4143 And Figure 3 shows the comparison of the carbon sequestration capacity and accumulated carbon sequestration capacity of various trees.

<!-- b000107 | prose | pages [8] -->
(a)                                                                                  (b)

<!-- b000108 | caption | pages [8] -->
Figure 3: The comparison of various trees

<!-- b000109 | heading | pages [9] -->
5 Forest Management Model for Carbon Sequestration

<!-- b000110 | heading | pages [9] -->
5.1 Parameter Settings

<!-- b000111 | prose | pages [9] -->
Carbon sequestration includes forest carbon sequestration and forest products carbon sequestration. Because some forest products may outlive the trees that produced them. The combination of sequestrated carbon in some forest products with sequestrated carbon due to the regeneration of young forests has the potential to allow more sequestration over time than the sequestration benefits of not cutting forests at all. So, we need to explore how we can plan to properly cut down the trees in the forest and make the right forest products. The life of forest products should be longer than the life of the trees themselves in order to effectively increase carbon

<!-- b000112 | caption | pages [9] -->
Figure 4: Forest carbon sequestration destination

<!-- b000113 | prose | pages [9] -->
sequestration.

<!-- b000114 | prose | pages [9] -->
In this model, we optimize the carbon sequestration model. During the growth of trees, carbon sequestration is transferred from trees to soil, and this part of carbon sequestration will not be decomposed back into carbon dioxide after the tree dies. As shown in Figure 4. It still contributes to the total carbon sequestration of forests. Therefore, we add the contribution to carbon sequestration after the death of trees in statistical time into the model to make the result closer to the real situation.

<!-- b000115 | prose | pages [9] -->
In order to determine the optimal forest management plan over time, we establish the optimal forest management model for carbon sequestration. And we search for the optimal plan through dynamic programming method. The specific steps are as follows:

<!-- b000116 | prose | pages [9] -->
First, we divide the selected forest into unit areas and number them. We classify the areas with same tree species into consecutive numbers, and record the corresponding numbering ranges of different species. In this way, we can determine the type of trees in the unit area by the size of . For example, indicates that A-type trees grow in this area; indicates that B-type trees grow in that area, and so on.

<!-- b000117 | prose | pages [9] -->
The area number of trees with different ages and types in the forest changes dynamically due to the felling of trees and the planting of new trees. To simplify the model, we assume that after cutting down trees in a certain year, seedlings of the same type of trees will be planted in the original area in the same year.

<!-- b000118 | prose | pages [9] -->
Before deciding on the harvest plan for the trees in region , we should first decide whether the trees can be cut down. We define the age of trees in region  in year  as . And we use to store information about the age at which trees are felled. And the age of trees in region in year is . If is greater than the longest life of trees in this region, then the trees in this region have died in year  and we cannot cut them down. At this time, the death of trees in region  in year is , and make .

<!-- b000119 | prose | pages [9] -->
If is still within the survival range of trees in this area, then and make the subsequent judgment. We define the time required for the j-type tree to grow to the felling stage as . When is larger than the cutting age of a specific type of trees in the region, that is , trees in the region can be felled in year ; if , then they cannot be felled.

<!-- b000120 | prose | pages [10] -->
We define whether the unit region  is felled in year  as . Its definition is where indicates that trees are not cut, and indicates that trees are cut.

<!-- b000121 | prose | pages [10] -->
(10)

<!-- b000122 | prose | pages [10] -->
If trees in region  are cut in year , that is , then make to store the age of trees in region  in year  at the time of cutting, then set , and start the calculation again. Otherwise , then and is not required to be zero.

<!-- b000123 | heading | pages [10] -->
5.2 Construction of Objective Function

<!-- b000124 | prose | pages [10] -->
At the end of the last year of the statistical period, we can obtain the value of and in each year for each region in the period. Figure 5 shows the overall process.

<!-- b000125 | caption | pages [10] -->
Figure 5: The overall process

<!-- b000126 | prose | pages [10] -->
In order to optimize the solving process of the total carbon sequestration in the statistical period, we integrate the Formula (9) to obtain the expression of the total carbon sequestration in the growth year of trees in region .

<!-- b000127 | prose | pages [10] -->
(11) Using , we can calculate the contribution of dead trees to carbon sequestration during the statistical time. The formula is

<!-- b000128 | prose | pages [10] -->
(12)

<!-- b000129 | prose | pages [10] -->
where is the part that still contributes to carbon sequestration after tree death in the statistical time.

<!-- b000130 | prose | pages [10] -->
is the carbon density accumulated at the maximum age of the trees in region . is the year number of the statistical time.  is the proportion of the part still contributing to carbon sequestration after the death of trees to that before the death of trees, which is related to climate.

<!-- b000131 | prose | pages [11] -->
According to the , we use the optimized Formula (13) to calculate the carbon density accumulated in their growth years in region  in year , and we analogy the Formula (2) (3) (4) (5) of carbon sequestration model to calculate , which is the forest carbon sequestration live in year . By adding the contribution of dead trees to the carbon sequestration in the statistic time (excluding the amount that had been felled and converted into forest products in previous years), we can calculate the total carbon sequestration of the forest. The formula is (13) After obtaining , we also need to calculate the carbon sequestration amount of forest products in statistical time. We consider that forest products whose product life has exceeded in the statistical time do not contribute to the carbon sequestration, so we only need to calculate the total carbon sequestration of forest products whose product life has not exceeded in the last year of the statistical time. The calculation formula is

<!-- b000132 | prose | pages [11] -->
(14)

<!-- b000133 | prose | pages [11] -->
(15)

<!-- b000134 | prose | pages [11] -->
(16) where is the set of region  corresponding to trees producing the p-type forest product. is the carbon density accumulated during the growth years of the felled trees. is the age at which trees are cut.

<!-- b000135 | prose | pages [11] -->
Therefore, it is necessary to find the objective function that maximizes the total carbon sequestration of forests and forest products with the optimal plan. We can get the total carbon sequestration of forests and forest products in the statistical time is (17) where is the total carbon sequestration of forest in statistical time. is the total carbon sequestration of forest products that do not exceed the product life in the last year of the statistical time.

<!-- b000136 | prose | pages [11] -->
By solving the objective function, we can obtain the optimal forest management plan, that is, the annual cutting amount of trees in each region, the plan of making forest products and so on. The plan enables selected forests and their forest products to achieve the maximum amount of carbon sequestration over statistical time.

<!-- b000137 | heading | pages [11] -->
6 Forest Management Model for Society

<!-- b000138 | heading | pages [11] -->
6.1 Overview

<!-- b000139 | prose | pages [11] -->
The forest management plans that are most conducive to carbon sequestration are not necessarily the best for society. To make better decisions about managing forests, we need to understand the value of forests. Then we define indicators to quantify it.

<!-- b000140 | prose | pages [12] -->
The United Nations economic commission for Europe and FAO (UNECE/FAO) published the report "forest non-wood forest products and services", which takes "social and cultural service" as a whole to start research, and refine the forest value as hunting and fishing, leisure and tourism value, the aesthetics and landscape value and historical value, cultural and spiritual values, and science. [6] In the previous section, we discussed the carbon sequestration value of forest. Combined with the UN research, we mainly consider the following three aspects: biodiversity value, cultural value and recreational value.

<!-- b000141 | caption | pages [12] -->
Figure 6: Indicators of forest value

<!-- b000142 | heading | pages [12] -->
6.2 The Value of Forests

<!-- b000143 | heading | pages [12] -->
6.2.1 Carbon Sequestration Value (CSV)

<!-- b000144 | prose | pages [12] -->
As discussed in our previous model, forests are an integral part of climate change mitigation and have significant carbon sequestration value. We use the maximum carbon sequestration of selected forests obtained from the optimal carbon sequestration forest management model to calculate the annual maximum carbon sequestration. And then we can measure the carbon sequestration value of a forest as

<!-- b000145 | prose | pages [12] -->
(18)

<!-- b000146 | prose | pages [12] -->
where is the total carbon sequestration in the statistic time.

<!-- b000147 | heading | pages [12] -->
6.2.2 Biodiversity Value (BV)

<!-- b000148 | prose | pages [12] -->
Biodiversity includes genetic, species and ecosystem diversity. Based on the above theory, when calculating the value of biodiversity, we consider the population richness and population density in a forest area and the complexity of the ecosystem in which all creatures live.

<!-- b000149 | prose | pages [12] -->
Species Richness (SR) When describing the richness of biodiversity in an area, the most commonly used indicator is regional species diversity. A measure of regional species diversity can be expressed in terms of species richness. [7] Edward Hugh Simpson, a British statistician, proposed Simpson's diversity index [8]. The greater the Simpson diversity index, the more species, the higher the species richness. The formula is

<!-- b000150 | prose | pages [12] -->
(19)

<!-- b000151 | prose | pages [12] -->
where is the number of entities belonging to the m-type in the selected forest. is the total number of entities in the selected forest.

<!-- b000152 | prose | pages [13] -->
Biomass Density (BD) It is a measure of the richness of organisms in an area. We can get the biomass density directly by dividing the total number of plants and animals in a selected forest by the total area of the forest.

<!-- b000153 | prose | pages [13] -->
(20)

<!-- b000154 | prose | pages [13] -->
where is the total number of plants and animals. is the total area of the forest.

<!-- b000155 | prose | pages [13] -->
Ecosystem Complexity (EC) Any creature has to live in a certain environment, leaving the appropriate environment, it is difficult for the creature to adapt. So only a diversity of ecosystems can ensure the survival of various life in those ecosystems. Here, we use absolute ecosystem richness to measure ecosystem complexity.

<!-- b000156 | prose | pages [13] -->
(21) where is the number of ecosystem types, which is classified according to vegetation subtypes in the vegetation classification system.

<!-- b000157 | prose | pages [13] -->
Finally, we can obtain biodiversity value through the weighted combination of these indicators:

<!-- b000158 | prose | pages [13] -->
(22) where is the weight of three indicators respectively.

<!-- b000159 | heading | pages [13] -->
6.2.3 Cultural Value (CV)

<!-- b000160 | prose | pages [13] -->
Forest cultural value is an important part of total forest values. David Edwards proposed “key indicators for the sustainability of social and cultural values of Forests in Europe” and selected typical regions in Europe for empirical analysis. The five themes of the indicator system, including recreation and tourism, education and learning, health and welfare, landscape and aesthetics, culture and heritage, are closely related to the cultural values of forests [9]. Therefore, we measure the cultural value of the selected forest in terms of education, health and cultural heritage.

<!-- b000161 | prose | pages [13] -->
Education Input (EI) The more money a region invests in education, the higher its education level will be. Here, we use the percentage of GDP invested in education of the country where we select forest to express it. The higher the level of education, the stronger people's understanding of the forest, the more easily the cultural value of a forest can be reflected.

<!-- b000162 | prose | pages [13] -->
Health Level (HL) We measure health level by life expectancy in the country where we select forest, and the shorter the life expectancy, the lower the health level. The cultural value that forests bring can promote physical activity and significantly improve the health of people in areas with low health level. As for countries with high health level, people may have good living habits at ordinary times, so forest cultural values do not contribute much to their health.

<!-- b000163 | prose | pages [13] -->
Cultural Heritage (CH) The higher the proportion of heritage of cultural and spiritual value in the forest, the more areas of the forest that can be used for the development of cultural resources, the higher the cultural value.

<!-- b000164 | prose | pages [13] -->
Also, we can obtain the cultural value indicator by the weighted combination of these three indicators:

<!-- b000165 | prose | pages [14] -->
(23) where is the weight of three indicators respectively.

<!-- b000166 | heading | pages [14] -->
6.2.4 Recreational Value (RV)

<!-- b000167 | prose | pages [14] -->
According to economic demand theory and related research results, we can consider the factors affecting forest recreational value from both supply and demand. Demand factors mainly include: population density of local residents, regional urbanization rate, the income level of residents in this area. Supply factors mainly include: the level of tourism resources in this region, density of forest parks in the region, transportation convenience, forest environmental quality; degree of capitalization, human resources [10]. We select two indicators of demand and supply respectively to measure recreational value.

<!-- b000168 | prose | pages [14] -->
Population Density (PD) Population is the basis of tourism market. Due to the spatial mobility of tourism, tourism demand shows an obvious spatial distance attenuation law. In particular, people's demand for forest parks is mainly from tourists inside the province [11]. The greater the population density of a country, the greater the demand for forest parks.

<!-- b000169 | prose | pages [14] -->
Income Level (IL) We use GDP per capita of the country where the forest is located. Studies have proved that income level affects forest tourism demand [12]. The higher the income level, the greater the demand for forest parks in the region.

<!-- b000170 | prose | pages [14] -->
Transportation Convenience (TC) The convenience of transportation is an important factor affecting tourists, which plays a decisive role in tourists' choice of traveling psychologically. Without safe and convenient transportation, it is impossible to have large-scale and long-term development of tourism economy. Then it will not be able to play its advantages, no matter how big the potential of tourism resources is. According to research [13], we define the calculation formula of transportation convenience as

<!-- b000171 | prose | pages [14] -->
(24)

<!-- b000172 | prose | pages [14] -->
where is various modes of transportation. is the speed of all modes of transportation. is the passenger capacity of all modes of transportation. is the holding of various means of transportation.

<!-- b000173 | prose | pages [14] -->
Environmental Quality (EQ) As people pay increasing attention to health, the forest environment of forest park is becoming more and more important factor to attract people to choose forest park. We measure the environmental quality of the forest by the annual air quality index (AQI) of the selected forest.

<!-- b000174 | prose | pages [14] -->
Thus, the calculation formula of recreational value is (25) where is the weight of four indicators respectively.

<!-- b000175 | heading | pages [15] -->
6.2.5 Data Processing and Weight Determination

<!-- b000176 | prose | pages [15] -->
To eliminate the effects of dimensions and dimensions, we need to normalize the indicators. However, since not every indicator is bigger, the better, we also need to carry out forward processing for indicators at the same time. Below we give different data processing methods.

<!-- b000177 | prose | pages [15] -->
For higher-is-better indicators, we take:

<!-- b000178 | prose | pages [15] -->
(26)

<!-- b000179 | prose | pages [15] -->
where 𝑦𝑚,𝑛 represents the original value of item 𝑛 in region . 𝑟𝑚𝑖𝑛 represents the minimum value of item n in all years. 𝑟𝑚𝑎𝑥 represents the maximum value of item n in all years.

<!-- b000180 | prose | pages [15] -->
For smaller-is-better indicators, which are opposite to above one, positive transformation is required:

<!-- b000181 | prose | pages [15] -->
(27)

<!-- b000182 | prose | pages [15] -->
The determination of indicator weight plays an important role, which directly affects the accuracy of evaluation results. Entropy weight method (EWM) is an objective weighting method. We use it to determine the weight of indicators. We select 10 forests in the world and get the data from the forestry bureau of each country and related survey reports. Then, we calculate the weight of each indicator by MATLAB. Table 3 shows the results.

<!-- b000183 | caption | pages [15] -->
Table 3: The weight of each indicator

<!-- b000184 | prose | pages [15] -->
Carbon sequestration value Carbon sequestration 1.0000 Species richness 0.4992 Biodiversity value Species density 0.1879 Ecosystem complexity 0.3129 Education input 0.0715 The Value of Cultural value Health level 0.2792 Forests Cultural heritage 0.6439 Population density 0.5220 Income level 0.1485 Recreational value Transportation 0.2076 convenience Environmental quality 0.1219

<!-- b000185 | heading | pages [15] -->
6.3 Forest Management Evaluation Model

<!-- b000186 | heading | pages [15] -->
6.3.1 Scoring Method of Forest Management Value Realization

<!-- b000187 | prose | pages [15] -->
In order to balance the various value methods of forests and enable forest managers to make the best use of forests, we weighted the above four values and measured the merits and demerits of forest management methods through the total score. What we get above is the total value of each forest in the selected forest, and our forest management plan should include the percentage of area that the forest is used to realize each value. Therefore, after the implementation of the management plan, the value of each value really realized in the selected forest should be:

<!-- b000188 | prose | pages [15, 16] -->
(28) where represents the true realization part of the h-type value. is the calculation results of the h-type value. is the ratio of forest area for realizing the value of h-type to the total forest area In order to make the score closer to the real situation, we use analytic hierarchy process (AHP) to analyze the importance of these four values and then get the weight of each value.

<!-- b000190 | prose | pages [16] -->
We can express the final total score as (29) Except for carbon sequestration value, the order of the deforestation degree caused by the realization of the other three values is generally . Regardless of the daily care of the forest, if and the rest is 0, then the whole forest is used for biodiversity conservation and we do not cut trees. Conversely, if , the forest will suffer severe damage and many trees will be cut down. But obviously the occurrence of these two extremes is not conducive to the utilization of forests. We need to construct a personalized judgment matrix according to the characteristics and geographical location of different forests and their importance to get the weight of different values of selected forests.

<!-- b000191 | heading | pages [16] -->
6.3.2 The Cost of Realizing Value

<!-- b000192 | prose | pages [16] -->
When realizing the value mentioned above, certain capital investment is necessary, that is, cost. The cost calculation method is relatively simple. We need to collect , the cost per unit area needed to realize the h-type value of the selected forest. After collecting the data, we can normalize it by

<!-- b000193 | prose | pages [16] -->
(30)

<!-- b000194 | prose | pages [16] -->
To calculate the cost score of the implementation plan, we sum the product of the area ratio and capital . The larger the score is, the higher the cost will be.

<!-- b000195 | prose | pages [16] -->
(31)

<!-- b000196 | heading | pages [16] -->
6.3.3 Transition Points for Different Management Plans

<!-- b000197 | prose | pages [16] -->
What kind of management plan is best? It is not enough to only consider the realization of value. For different forest managers, they need to make trade-offs between the value and the cost. There are transition points for different plans according to the recommended degree of plans.

<!-- b000198 | prose | pages [16] -->
In order to show the relationship between value and cost vividly, we use GE matrix to evaluate the plan. GE matrix is initially used for planning and analysis of the business portfolio of strategic public institutions. The vertical axis is industrial attraction, and the horizontal axis is business strength. The evaluation is based on the competitive strength of specific business modules and the attractiveness in the market. We use the horizontal axis as value score and the vertical axis as cost score to evaluate management plan from these two dimensions.

<!-- b000199 | prose | pages [16] -->
Since each forest can realize different maximum value score and maximum cost score, we set the maximum and minimum of the horizontal axis as , and for the vertical axis, they are . Then we divide Value and Cost into three levels respectively, as shown in Table.

<!-- b000200 | caption | pages [17] -->
Table 4: Level classification of Value and Cost

<!-- b000201 | prose | pages [17] -->
Value Level Cost Level Low Low Medium Medium High High We can divide the GE matrix into nine regions, and we use can coordinates to represent the plan, which have different meanings when they fall in different regions. In theory, the point with the lowest cost and highest value (point in Figure 7) is the best. If classifying simply, we can divide them into three types: high value cost ratio (blue area), medium value cost ratio (gray area) and low value cost ratio (red area). The plan falling in the blue zone is the best, with less input and more output. And we should not adopt the plan falling in the red zone with high cost and low forest value.

<!-- b000202 | prose | pages [17] -->
There are transition points for forest management plans applicable to various forests.

<!-- b000203 | caption | pages [17] -->
Figure 7: The GE matrix

<!-- b000204 | prose | pages [17] -->
When determine a forest management plan, its coordinates should fall in the blue zone. When we adjust the proportion of various values in the plan, the realized value and cost of the plan will also change, and its coordinates will move in the GE matrix. In the process of change, the plan may move from a blue zone to a gray zone, or even to a red zone. It means that the plan changes from enforceable to unenforceable. And this situation is the same for every forest.

<!-- b000205 | prose | pages [17] -->
The characteristics of different forests and their location influence the transition points of forest management plans. For different forests, their characteristics and location will significantly affect the weight obtained by AHP, which can be understood as different advantages of different forest to develop values. Similarly, each forest requires different value development costs. Therefore, the transition points between the calculated value and cost are different in each forest. Every forest has a personalized GE matrix to judge the feasibility of the plan.

<!-- b000206 | prose | pages [17] -->
Different forest managers may make different decisions. Forest managers can be individuals, governments, enterprises or other organizations. Different managers may value different things. For example, when making decisions, the government pays more attention to the social benefits brought by the management plan, so the government will stress the importance of the value, even if the cost is higher. However, enterprises may pay more attention to cost and want to maximize profits with the least cost.

<!-- b000207 | heading | pages [17] -->
7 Case study: Greater Khingan Mountains

<!-- b000208 | heading | pages [17] -->
7.1 The Current Situation of Greater Khingan Mountains

<!-- b000209 | prose | pages [17] -->
Greater Khingan Mountains is one of China's most important forestry bases, covering an area of 327,200 square kilometers. The main trees are Xing’an larch, Mongolian oak, white birch, etc. According to statistics, the total amount of forest carbon sequestration in Greater Khingan Mountains is about 1.72 billion tons. The vast virgin forest is home to a wealth of species.

<!-- b000210 | prose | pages [18] -->
According to the survey, there are 56 species of mammals and 250 species of bird resources in the forest, as well as 1,069 plant species in the forest. We can see that the forest has a large number of species, including many rare species, which has a high value of species diversity. Apart from this, the biomass density also reached 59.92 . What’s more, according to the relevant investigation report, there are 13 types of vegetation in it, which can meet the specific living conditions of different organisms.

<!-- b000211 | heading | pages [18] -->
7.2 Analysis of Carbon Sequestration after 100 Years

<!-- b000212 | prose | pages [18] -->
The stock volume per unit area of Xing’an larch, white birch and Mongolian oak are 83.755, 87.29 and 37.34, respectively [14]. Table 5 shows forest products’ raw materials and lifespans[15].

<!-- b000213 | caption | pages [18] -->
Table 5: Forest products made from its main trees and their lifespans

<!-- b000214 | prose | pages [18] -->
The type of trees Forest products Lifespan (year) Building materials 80 Mongolian oak Furniture 25 Building materials 65 Xing’an larch House 50 Pillow 20 Bed 50 White birch Desk and chair 40 Paper 10 The age distribution of trees in Greater Khingan Mountains shows that the number of trees in the middle age is the largest, while others are less. We take this age distribution as the initial age distribution of trees in the forest, and number unit area according to the differences in age and species of trees in different areas. In the calculation, we choose Xing’an larch, white birch and Mongolian oak to calculate. Figure 8(a) shows the corresponding relationship between tree species and initial age and region .

<!-- b000215 | prose | pages [18] -->
Using the collected data, we calculate the optimal management plan for carbon sequestration in the next 100 years and calculate the final carbon sequestration amount. There is no unique optimal plan to achieve the maximum carbon sequestration. The difference between them is the area  selected by felling trees of the same type and age in the same year, which has no influence on the results. We choose one of the plans, and the results are as follows. Figure8(b) shows the corresponding relationship between area  and the ages of trees surviving after 100 years.

<!-- b000216 | prose | pages [18, 19] -->
(a)Start (b)End According to the age, we can calculate the carbon sequestration accumulation of the surviving forest after the 100 years . Then, based on the obtained value of , and , we can get the contribution to carbon sequestration after the death of trees and the total carbon sequestration of forest products within the last year . Thus, we can obtain the total carbon sequestration after 100. Table 6 shows the results.

<!-- b000217 | caption | pages [18] -->
Figure 8: The relationship between area  and the ages of trees

<!-- b000219 | caption | pages [19] -->
Table 6: Carbon sequestration after 100 years

<!-- b000220 | prose | pages [19] -->
19.9513 7.2873 15.402 42.6406

<!-- b000221 | heading | pages [19] -->
7.3 The Optimal Forest Management Plan

<!-- b000222 | prose | pages [19] -->
Based on the best Forest Management model, we collect data from the China Forestry Administration and the World Bank on Greater Khingan Mountains, and we calculate the values of , , , are 0.7533, 0.8124, 0.3736, 0.4962 respectively.

<!-- b000223 | prose | pages [19] -->
Then, we obtain the superiority of various forest values in Greater Khingan Mountains by referring to relevant data. Through AHP, we obtain the weights of secondary indicators , , , are 0.3214, 0.2857, 0.25, 0.1429 respectively. The large weight of and probably because that China is implementing "carbon neutrality" and "carbon peak" strategy, which attaches great importance to the reduction of carbon emissions. Carbon sequestration can effectively alleviate this problem. As mentioned above, Greater Khingan Mountains is rich in biological species and has significant biodiversity value.

<!-- b000224 | prose | pages [19] -->
According to the studies on the development costs of forest values in China [16,17,18,19], we can obtain that the of realizing , , , are 0.07, 0.58, 0.26 and 0.09, respectively.

<!-- b000225 | prose | pages [19] -->
Then we set up different plans for forest utilization in Greater Khingan Mountains. By calculating the and of different plans and marking them in GE matrix, the plan closest to point is the best management plan. In order to make full use of the various forest values, we make the proportion of the implementation area of each value less than 10% of the total area. Based on the above conditions, we can build a nonlinear programming model and use genetic algorithm to search for the global optimal solution.

<!-- b000226 | prose | pages [19] -->
Figure 9(a) shows the results of the genetic algorithm. Therefore, the optimal plan finally obtained is that 58.95% area is for sequestering carbon, 11.20% area is for biodiversity, 11.41% area is for cultural industry and 18.37% area is for entertainment industry. The and are 0.1924 and 0.1524 respectively, and their positions on GE matrix are shown in Figure 9(b). We can see that this plan falls in the blue area and is very close to the point . It is a highly feasible plan and can obtain the highest value with the lowest investment cost.

<!-- b000227 | prose | pages [20] -->
(a) (b)

<!-- b000228 | caption | pages [20] -->
Figure 9: The optimal forest management plan to greater khingan mountains

<!-- b000229 | prose | pages [20] -->
Based on the above results, we propose the following recommendations for forest managers.

<!-- b000230 | prose | pages [20] -->
First, forest managers should focus on the protection of forest trees by classifying more than half of the forest area as forbidden zones to achieve the carbon sequestration function of forests. We learned that commercial logging of natural forests has been suspended in the Greater Khingan Mountains since 2015. The aim is to strengthen forest management, protect forest vegetation and improve forest carbon sequestration capacity. According to our analysis of carbon sequestration in 100 years, we should cut down the corresponding proportion of trees to make forest products in Greater Khingan Mountains to further improve its carbon sequestration capacity.

<!-- b000231 | prose | pages [20] -->
Second, make use of its recreational value and properly develop ecological tourism. There are five types of monopolistic tourism resources in Greater Khingan Mountains, including alpine snow and ice, northern lights and other characteristic landscapes [20]. These distinctive tourism resources are the best carriers for developing forest eco-tourism. When developing, focus on the protection, combining protection and reasonable development. Besides, improve the surrounding traffic network and increase publicity to attract more tourists.

<!-- b000232 | prose | pages [20] -->
In addition, part of the area is devoted to protecting biodiversity and developing cultural industries. For biodiversity conservation, forest managers can strengthen advocacy and raise public awareness of biodiversity; If the manager is the government, it should strengthen legislation and law enforcement, improve the protection system, and strengthen the construction of nature reserves. For cultural value, Oroqen culture is unique to the Greater Khingan Mountains [21], and it should be protected. We can combine it with tourism development, plan and develop cultural tourism resources to propagate and inherit the excellent traditional culture.

<!-- b000233 | heading | pages [20] -->
7.4 The Modification of the Optimal Plan

<!-- b000234 | prose | pages [20] -->
According to the problem restatement, we will allow logging for 10 years longer than the current practice, that is to add 10 to the on the original basis. So, we need to modify our optimal plan. The limitation of this condition will lead to the change of , which is 0.6511 after recalculation. The proportion of and in modified plan is 55.87%, 10.23%, 10.11% and 23.71%, respectively. The calculated and is 0.1667 and 0.1461, respectively, which is still in the blue region of the GE matrix.

<!-- b000235 | prose | pages [21] -->
(a)                                                                       (b)

<!-- b000236 | caption | pages [21] -->
Figure 10: The modification of the optimal plan

<!-- b000237 | prose | pages [21] -->
We can find that the big change between the old and new management plans is the proportion of and . The calculated is not as much as before. In order to make the forest realize more value, the proportion of is reduced and is increased.

<!-- b000238 | prose | pages [21] -->
To make forest managers and people who use forests adapt this change, we will discuss a sensitive strategy for them to satisfy their needs. They may be governments, enterprises and individuals. For the government, as the area of decreases and the reduced area is used to develop tourism industry, it is necessary to strengthen the protection of undeveloped forest areas. It can issue relevant laws to regulate the development behavior to avoid the impact of tourism development on the surrounding environment. For enterprises, they may be the developers of . As the tourism area becomes larger, enterprises should adopt more effective publicity means, give consumers various preferential policies, highlight the regional characteristics of the forest to attract more tourists. Individuals should develop a good sense of environmental protection. When playing in the forest park, do not destroy the trees in the park, consciously protect the environment.

<!-- b000239 | heading | pages [21] -->
8 Sensitivity Analysis

<!-- b000240 | prose | pages [21] -->
To verify the robustness and validity of our model, we do sensitivity analysis on our model.

<!-- b000241 | prose | pages [21] -->
First, we conduct sensitivity analysis on the value. Greater Khingan Mountains is rich in biodiversity, so we artificially raise the from 0.81 to 0.99 with a step of 0.02, and observe the change of forest management plan. Figure 11(a) shows the results. We can see that as the goes up, the optimal plan changes, goes up, and there will be more areas of the forest dedicated to biodiversity conservation. So, our model can make different decisions as the value changes. However, due to the high cost of conservation, the small fluctuation range of biodiversity value, and the low cost of carbon sequestration value, the plan is mainly based on carbon sequestration value. The plan changes within a small overall range, and the model is robust.

<!-- b000242 | prose | pages [21] -->
Next, we also conduct sensitivity analysis on cost. As mentioned above, the low cost of carbon sequestration value causes the plan to remain basically unchanged. Therefore, we increase the from 0.07 to 0.23 with a step of 0.02, and change the remaining costs as the original proportion. Figure 11(b) shows the results. We find that in the early rise stage of , the plan basically does not change. However, when it rises to the 0.13, the plan changes significantly: rises, falls, and the other two basically remains the same. In the later period, even surpasses and become the dominant value. We also conduct similar analysis on other costs and got similar results. Therefore, we can see that our model has strong effectiveness and high credibility, which can timely modify the plan and always make the value and cost reach an optimal value.

<!-- b000243 | prose | pages [22] -->
(a) (b)

<!-- b000244 | caption | pages [22] -->
Figure 11: Sensitivity analysis

<!-- b000245 | heading | pages [22] -->
9 Strengths and Weaknesses

<!-- b000246 | heading | pages [22] -->
9.1 Strengths

<!-- b000247 | prose | pages [22] -->
⚫ The carbon sequestration model is scientific and comprehensive. We use the conversion factor method of forest stock volume to calculate carbon sequestration, which not only considers the contributions of trees and forest products, but also understory plants and soil, fitting the reality. ⚫ The forest management model for carbon sequestration can simulate the dynamic change process of forest management and obtain the reliable optimal plan. Indicators influence and constrain each other. The simulation process is close to the reality, and the factors we considered are comprehensive. ⚫ The forest management model for society fully considers the value of forests. We select multiple indicators from three aspects to quantify it, which is conducive to analyze and develop personalized forest management plan more effectively. It is objective to assign weight to indicators by entropy weight method. ⚫ The use of GE matrix, considering both value and cost dimensions, is beneficial to provide different decision-making suggestions for different forest managers. Meanwhile, we can easily obtain the transition points of different plans from GE matrix and intuitively judge the feasibility of the plan. ⚫ We conduct sensitivity analysis on the model, and find that our model has good robustness in a small fluctuation range. It also can make different forest management plans according to the changes in value and cost, which is highly effective and practical.

<!-- b000248 | heading | pages [22] -->
9.2 Weaknesses

<!-- b000249 | prose | pages [22] -->
⚫ We believe that fixed in forest products will return to the atmosphere after they reach their life span, regardless of their specific treatment methods, such as landfill and combustion.

<!-- b000250 | prose | pages [22] -->
Different treatment methods may lead to different remaining carbon sequestration amount of forest products after their lifespan. For example, may soil can absorb part of the carbon from landfill, and the carbon fixed by forest products will not completely disappear. ⚫ The forest management model only considers the development cost without the maintenance cost after development.

<!-- b000251 | heading | pages [22] -->
10 A Newspaper Article

<!-- b000252 | prose | pages [23] -->
A child went into the garden and saw his grandfather on the ladder cutting off some branches of the tree. The child picked up a branch and said, "Grandpa, it’s a pity to cut them off!" "Silly boy," said the grandfather, "thus the tree will grow better." Some people think that deforestation is harmful, but in fact, like pruning, appropriate deforestation is beneficial to ecology and society.

<!-- b000253 | prose | pages [23] -->
The proper logging here refers to forest ecological logging. Simply speaking, it is a targeted and selective logging activity that strictly follows the law of ecological development. Through logging, carbon sequestration in forests can be transferred to forest products throughout their life cycle. Based on this, our team developed the forest management model for carbon sequestration. We used this model to study the Greater Khingan Range.

<!-- b000254 | prose | pages [23] -->
After 100 years, its carbon sequestration of forest is 2.724 billion tons, and that of forest products is 1.540 billion tons, indicating that forest products can sequester a large part of the carbon. This is because some forest products may last longer than trees, and the carbon sequestered in some forest products coupled with the regeneration of young forests has the potential to sequester more carbon over time. So, cutting down trees properly is a sensible choice for carbon sequestration.

<!-- b000255 | prose | pages [23] -->
Apart from this, forests also have many other use values, such as biodiversity value, cultural value and recreational value. The best forest management plan for carbon sequestration is not necessarily the best one for society. We should balance the values of forests and make full use of their advantages. Our team also built a forest management model for society that considered four values, balancing both value and cost. We also applied this model to the Greater Khingan Range and developed a management plan: 55.87%, 10.23%, 10.11% and 23.71% for carbon sequestration, biodiversity, cultural and recreational value, respectively. It can be seen that our management plan can not only bring ecological benefits to the local area, but also bring huge economic and cultural benefits, which is conducive to the development of the region and has great potential for the improvement of living standards and cultural standards. Of course, a proper cutting down of trees is also a necessary condition to achieve this goal. We should believe that logging a small number of trees can indeed bring great benefits!

<!-- b000256 | prose | pages [23] -->
You may have disagreed with the idea of cutting down trees, but after reading this report, you will have a better understanding of the benefits of cutting down trees properly.

<!-- b000257 | heading | pages [24] -->
References

<!-- b000258 | references | pages [24] -->
[1] A large and persistent carbon sink in the world's forests[J]. Science, 2011, 333(Aug.19

<!-- b000259 | references | pages [24] -->
TN.6045):988-993.

<!-- b000260 | references | pages [24] -->
[2] Wang Li, Wang Haiyang, Chang Xin. Garden tree species common carbon sequestration

<!-- b000261 | references | pages [24] -->
ability to release oxygen makes analysis [J]. Journal of southern agriculture, 2012, 6 (05) : 54-56

<!-- b000262 | references | pages [24] -->
[3] J  Chen,  Yang H . Advances and frontiers in global forest and harvested wood products

<!-- b000263 | references | pages [24] -->
carbon science[J]. Journal of Nanjing Forestry University (Natural Sciences Edition),

<!-- b000264 | references | pages [24] -->
2018,42(04):1-8.

<!-- b000265 | references | pages [24] -->
[4] Wang D C, Zhang Z K, Yang Q, Cun D Z, Guo D Y, Zhao G L. Forest carbon sequestration

<!-- b000266 | references | pages [24] -->
and its change in Dehong County, China from 2016 to 2019 [J]. Green science and technology,

<!-- b000267 | references | pages [24] -->
2020 (22) : 261-263.

<!-- b000268 | references | pages [24] -->
[5] Cramer J S . The Origins and development of the Logit Model[M].  2003.

<!-- b000269 | references | pages [24] -->
[6] FAO. Global forest resources assessment 2005.progress towards sustainable forest

<!-- b000270 | references | pages [24] -->
management[R].Rome: Food and Agriculture Organization,2006:129-154

<!-- b000271 | references | pages [24] -->
[7] ” The main components of biodiversity” [OL]. Available: http://www.greentimes.com/gr

<!-- b000272 | references | pages [24] -->
een/swdyx/2012-02/06/content_165721.htm

<!-- b000273 | references | pages [24] -->
[8] Simpson, e. Measurement of diversity[J]. Nature 163, 688 (1949).

<!-- b000274 | references | pages [24] -->
[9] Edwards D. Social and cultural values associated with European forests in relation to key

<!-- b000275 | references | pages [24] -->
indicators of sustainability[R]. Joensuu, Finland: European Forest Institute ,2011:26-54.

<!-- b000276 | references | pages [24] -->
[10] Huang Xiujuan, Lin Xiuzhi. Chinese forest park tourism efficiency and its influencing

<!-- b000277 | references | pages [24] -->
factors [J]. Scientia silvae sinicae,2015,51(02):137-146.

<!-- b000278 | references | pages [24] -->
[11] Song Chen, Jiyue Li, Jinpu Jiang, Dawei Chen. Simulate tourist market and tourist

<!-- b000279 | references | pages [24] -->
behavior characteristics [J]. Hebei Forest and Fruit Research,2007(01):111-116.

<!-- b000280 | references | pages [24] -->
[12] Luo M C ,  Luo J ,  Zhong Y D , et al. A comparative study of visitor characteristics in

<!-- b000281 | references | pages [24] -->
different types of forest parks[J]. Journal of Central South Forestry University, 2005.

<!-- b000282 | references | pages [24] -->
[13] Haibin Xia, Xiaoye Dai, Ying Wang, Zheng Wang. Transportation convenience analysis

<!-- b000283 | references | pages [24] -->
at county level in China based on GIS [J]. Areal Research and Development,2006(03):120-

<!-- b000284 | references | pages [24] -->
124+130.

<!-- b000285 | references | pages [24] -->
[14] Wang Wenbo, Jiang Xilin, Zhao Pengwu. Estimation of forest carbon storage based on

<!-- b000286 | references | pages [24] -->
continuous forest inventory: A case study of Hulunbuir Region, Inner Mongolia [J]. Journal of

<!-- b000287 | references | pages [24] -->
northeast forestry university,2015,43(07):116-119.

<!-- b000288 | references | pages [25] -->
[15] Bai Y F. Carbon storage of wood forest products in China [D]. Chinese Academy of

<!-- b000289 | references | pages [25] -->
Forestry,2010.

<!-- b000290 | references | pages [25] -->
[16] Gu Rong, Gao Jun, Zhang Songhe, et al. Cost-effectiveness of Coastal wetland Nature

<!-- b000291 | references | pages [25] -->
Reserve -- A case study of Yancheng Wetland Rare Birds National Nature Reserve in Jiangsu

<!-- b000292 | references | pages [25] -->
Province [J]. Journal of ecology and rural environment,2014,30(1):32-37.

<!-- b000293 | references | pages [25] -->
[17] Wu Jing. Study on cost and benefit of eco-tourism in Qinling Mountains [D]. Beijing

<!-- b000294 | references | pages [25] -->
Forestry University,2015.

<!-- b000295 | references | pages [25] -->
[18] Zhou Ying. Research on economic value evaluation of cultural heritage tourism resources

<!-- b000296 | references | pages [25] -->
[D]. Dalian University of Technology,2014.

<!-- b000297 | references | pages [25] -->
[19] Liu H ,  Wu S ,  Yu T . Methodology study of forest conservation carbon sequestration

<!-- b000298 | references | pages [25] -->
projects[J]. World Forestry Research, 2018.

<!-- b000299 | references | pages [25] -->
[20] Li Gengxin, LI Siqiu, Wang Zao. Development of forest tourism industry in Greater

<!-- b000300 | references | pages [25] -->
Khingan Range [J]. China Forestry Enterprises,2005(02):34-36.

<!-- b000301 | references | pages [25] -->
[21] LI Yuanyuan, YU Huimin. Research on Oroqen cultural tourism resources development

<!-- b000302 | references | pages [25] -->
in Greater Khingan Range [J]. China Ethnic Expo,2019(02):57-58.
