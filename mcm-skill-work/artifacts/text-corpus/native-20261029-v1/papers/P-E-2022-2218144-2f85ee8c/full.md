# P-E-2022-2218144-2f85ee8c

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
2218144

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Chasing Better Forest Management Strategies

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
“Gabon is one of the world’s leading producers of wood. It enforces selective logging: not more than one tree every hectare.” This occurs in Yann Arthus-Bertrand’s 2009 ﬁlm Home. In reality, indiscriminate logging can increase soil erosion, reduce biodiversity, etc. But cutting down trees and making them into woody forest products can be economically beneﬁcial and can absorb carbon dioxide. Therefore, it is necessary to make a reasonable forest management plan to plan the number of trees to be cut and planted to achieve a stable and balanced forest.

<!-- b000011 | prose | pages [1] -->
First, we propose a Forest-Harvested Wood Products (HWP) Carbon Sequestration (FHWP) model and measure the amount of carbon sequestered by forests and HWP. First, the forest is divided into trees, understory plants, and woodlands, and their carbon conversion co- efﬁcients are calculated, and the forest carbon stock is solved by combining the forest area and carbon density. Second, the carbon sequestration of HWP was divided into two parts, including the carbon stock contained in wood and the amount of carbon entering the HWP pool in year i. The HWP is divided into four types, such as round wood, charcoal, and wood panel, and the carbon conversion factors of the four products are considered to predict the stock entering the HWP in year i. Then, we add up the carbon sequestration of both to construct the FHWP model. Finally, the model is applied to Russia and solved using an improved bat algorithm to derive the carbon sequestration in Russian forests, e.g., 1.39×1013t of carbon sequestration in Russian forests in 2020.

<!-- b000012 | prose | pages [1] -->
Second, we construct Carbon Sequestration-Economic Value-Ecological Protection (CEE) model to make forest management optimal in three dimensions: carbon sequestration (CS), eco- nomic value (EV), and environmental protection (EP). First, 12 indicators in the three dimensions of CS, EV, and EP are selected, and the indicators are calculated using the current market price and forest land revenue, and the data are normalized. Secondly, the entropy weight method is applied to calculate the weight of each indicator. |C| indicates the overall level achieved by this forest management plan under the three dimensions, and then CEE model is constructed. Finally, the model is applied to China considering the 5-year transition period of the plan. Under the con- dition of no deforestation, the transformation at 0.162% planting rate can reach the overall level of 2020 in 2025, corresponding to a carbon sequestration of 3.0411×1011t.

<!-- b000013 | prose | pages [1] -->
Third, the model was applied to Sudanese forests to derive the best forest management plan after 10 years of transition. First, Sudan’s forests from 2011-2020 was evaluated using CEE model. Second, based on FHWP model, the current amount of carbon sequestered by forests and their derivatives is calculated, and the amount of carbon sequestered after 100 years is predicted, starting from 2020. Next, we optimized the management plan based on the best management guideline-making the amount of carbon sequestered in 2030 as large as possible and scoring the forest state higher. The optimized production ratio for Sudan was estimated with reference to the production ratio of high level woody products in Australia. Finally, FHWP model is used to ﬁnd the maximum carbon sequestration in 2030 and its corresponding optimal forest manage- ment plan, and conclusions are drawn. The amount of carbon sequestered by the existing forest management plan after 100 years is: 4.1384×1013t The optimized best management plan has a deforestation rate of 0.21% and a planting rate of 2.33%, which expands the carbon seques- tration in 100 years by 42.09 times compared to the pre-optimized forest management plan.

<!-- b000014 | keywords | pages [1] -->
Keywords: Forest Management; FHWP Model; CEE Model; Bat Algorithm

<!-- b000015 | furniture | pages [2] -->
Team # 2218144

<!-- b000016 | furniture | pages [2] -->
Page 2 of 25

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1

<!-- b000019 | heading | pages [2] -->
Introduction

<!-- b000020 | prose | pages [2] -->
3 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000021 | prose | pages [2] -->
2

<!-- b000022 | heading | pages [2] -->
Symbol Table and Assumption

<!-- b000023 | prose | pages [2] -->
4

<!-- b000024 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 Symbol table 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000025 | heading | pages [2] -->
Assumptions

<!-- b000026 | prose | pages [2] -->
5

<!-- b000027 | prose | pages [2] -->
Forest-Harvested Wood Products Carbon Sequestration (FHWP) 3 3.1 Forest Carbon Sequestration Model 5 . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | prose | pages [2] -->
5 Calculating carbon density . . . . . . . . . . . . . . . . . . . . . 3.1.1 6 Calculating forest area . . . . . . . . . . . . . . . . . . . . . . . 3.1.2 6 Calculating forest carbon sequestration 3.1.3 . . . . . . . . . . . . . .

<!-- b000029 | prose | pages [2] -->
6 Harvested Wood Products Carbon Sequestration . . . . . . . . . . . . . . 3.2 6 Calculation of carbon conversion factors . . . . . . . . . . . . . . 3.2.1 7 Calculating carbon content entering HWP pool in year i 3.2.2 . . . . .

<!-- b000030 | prose | pages [2] -->
7 Calculating HWP sequestration 3.2.3 . . . . . . . . . . . . . . . . . .

<!-- b000031 | prose | pages [2] -->
8 Calculation of total carbon sequestration 3.3 . . . . . . . . . . . . . . . . .

<!-- b000032 | prose | pages [2] -->
8 Solving the FHWP model by using the improved bat algorithm . . . . . . 3.4 9 Application of FHWP model: Russia . . . . . . . . . . . . . . . . . . . . 3.5 10

<!-- b000033 | heading | pages [2] -->
Carbon Sequestration-Economic Value-Ecological Protection Model(CEE)

<!-- b000034 | prose | pages [2] -->
4 12 . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Overview of CEE model 12 Indices description and Data Normalization . . . . . . . . . . . . . . . . 4.2 12 Indicator Description and Calculation . . . . . . . . . . . . . . . 4.2.1 12 Data normalization . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 15 Calculation of weights by EWM . . . . . . . . . . . . . . . . . . . . . . 4.3 16 . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.1 Steps of EWM 16 Weight calculation results by EWM . . . . . . . . . . . . . . . . 4.3.2 17 Establishment of CEE Model . . . . . . . . . . . . . . . . . . . . . . . . 4.4 17 Application of CEE model: China . . . . . . . . . . . . . . . . . . . . . 4.5 18

<!-- b000035 | prose | pages [2] -->
Case Study: Find out better forest management strategies 5 19 Problems caused by mismanagement of Sudan’s forests . . . . . . . . . . 5.1 19 Results of applying CEE and HHWP model to Sudan . . . . . . . . . . . 5.2 20 Best forest management plan in Sudan . . . . . . . . . . . . . . . . . . . 5.3

<!-- b000036 | prose | pages [2] -->
6

<!-- b000037 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000038 | prose | pages [2] -->
7

<!-- b000039 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000040 | prose | pages [2] -->
8 Article

<!-- b000041 | heading | pages [2] -->
References

<!-- b000042 | references | pages [2] -->
20

<!-- b000043 | references | pages [2] -->
22

<!-- b000044 | references | pages [2] -->
22

<!-- b000045 | references | pages [2] -->
24

<!-- b000046 | references | pages [2] -->
25

<!-- b000047 | furniture | pages [3] -->
Team # 2218144

<!-- b000048 | furniture | pages [3] -->
Page 3 of 25

<!-- b000049 | references | pages [3] -->
1

<!-- b000050 | heading | pages [3] -->
Introduction

<!-- b000051 | prose | pages [3] -->
1.1

<!-- b000052 | heading | pages [3] -->
Background

<!-- b000053 | prose | pages [3] -->
With the continuous development of modern industry, large amounts of coal, oil and natural gas are burned, emitting greenhouse gases such as carbon dioxide and methane. The greenhouse gases in the atmosphere contribute to global warming and even threaten the survival of human beings. As the largest organic carbon reservoir in terrestrial sys- tems, with 56% of the entire terrestrial carbon pool, forests play an important role in mitigating climate change. Meanwhile, woody forest products, as an extension of for- est resource utilization, can transfer the carbon ﬁxed by forests into products through forest harvesting and product use. Thus, maximizing the use of forests allows for the sequestration of large amounts of carbon dioxide, which is necessary to mitigate climate warming.

<!-- b000054 | prose | pages [3] -->
However, an optimal forest management plan does not mean no cutting of trees at all. Considering the carbon sequestration capacity of forest products and the longevity of some of these products, appropriate cutting of trees and processing into forest products can be more beneﬁcial for carbon sequestration.

<!-- b000055 | caption | pages [3] -->
Figure 1: Global forest resources distribution(sq.km)

<!-- b000056 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000057 | prose | pages [3] -->
• Develop a carbon sequestration model to measure the amount of carbon sequestered by the forest and its products.

<!-- b000058 | prose | pages [3] -->
• Develop a decision model to determine the management plan that makes the best use of the forest.

<!-- b000059 | prose | pages [3] -->
• Apply the model to a forest and ﬁnd the amount of carbon dioxide sequestered by the forest and its products, the optimal management plan for the forest, and the transition strategy.

<!-- b000060 | prose | pages [3] -->
• Write a short persuasive essay explaining the reasons for including deforestation in the forest plan.

<!-- b000061 | furniture | pages [4] -->
Team # 2218144

<!-- b000062 | furniture | pages [4] -->
Page 4 of 25

<!-- b000063 | prose | pages [4] -->
1.3 Our Work

<!-- b000064 | prose | pages [4] -->
For the calculation of carbon sequestration, FHWP model is established, and the forest carbon sequestration is divided into three parts, and HWP is divided into two parts, and the total carbon sequestration is obtained by summing. For the evaluation of forest management strategies, we build a CEE model based on three dimensions, and evaluate the management strategies in terms of carbon sequestration, economic value and ecolog- ical protection, and the vector modulus length represents the total evaluation score. In order to ﬁnd a better forest management strategy, we combined FHWP model and CEE model with Sudan as the research object to maximize the amount of carbon sequestered and the overall score, so as to give the corresponding improvement plan. The overall idea of the study is shown in Figure 2.

<!-- b000065 | caption | pages [4] -->
Figure 2: Our Work

<!-- b000066 | prose | pages [4] -->
2

<!-- b000067 | heading | pages [4] -->
Symbol Table and Assumption

<!-- b000068 | prose | pages [4] -->
2.1 Symbol table

<!-- b000069 | prose | pages [4] -->
Note: Symbols are listed in the order of the ﬁrst occurrence in the text. Other nonefrequent-used symbols will be introduced once they are used.

<!-- b000070 | furniture | pages [5] -->
Team # 2218144

<!-- b000071 | furniture | pages [5] -->
Page 5 of 25

<!-- b000072 | caption | pages [5] -->
Table 1: Symbol table

<!-- b000073 | prose | pages [5] -->
Symbol

<!-- b000074 | prose | pages [5] -->
V

<!-- b000075 | prose | pages [5] -->
Deﬁnition

<!-- b000076 | prose | pages [5] -->
Volume per unit area Carbon conversion coefﬁcient of understory plants α Forest carbon conversion coefﬁcient β δ ρ γ C Biomass expansion coefﬁcient Volume coefﬁcient Carbon content Biomass carbon density Russian forest area in the year i Sti n m Wi k Cutting rate Planting rate HWP carbon reserves in year i Annual ﬁrst-order attenuation variable H Conversion of unit wood production Carbon conversion factor of forest products j Φj

<!-- b000077 | prose | pages [5] -->
2.2

<!-- b000078 | heading | pages [5] -->
Assumptions

<!-- b000079 | prose | pages [5] -->
Forest management plans are a complex issue of international importance. The re- lated issues involve many areas such as politics, economics, culture, and ecology. All possible scenarios of the relevant existence cannot be modeled in their entirety. There- fore, we make some plausibility assumptions and simplify the problem.

<!-- b000080 | prose | pages [5] -->
Assumption 1 We assume that the speciﬁc forest growth conditions in the speciﬁc areas selected for calculation are consistent, free from disturbances by intrinsic and ex- trinsic factors, and are of natural growth.

<!-- b000081 | heading | pages [5] -->
Assumption 2 Our data collected from online databases and related websites are

<!-- b000082 | prose | pages [5] -->
accurate, reliable and consistent with each other. Because our data sources are databases and websites of international organizations, it is reasonable to assume that their data are of high quality.

<!-- b000083 | prose | pages [5] -->
Assumption 3 In the model calculations, the indicator data that we ignore have little effect on the calculation of weights and results.

<!-- b000084 | prose | pages [5] -->
Forest-Harvested Wood Products Carbon Sequestra- 3 tion (FHWP)

<!-- b000085 | heading | pages [5] -->
Forest Carbon Sequestration Model

<!-- b000086 | prose | pages [5] -->
3.1

<!-- b000087 | prose | pages [5] -->
There are several methods to calculate forest carbon stock, such as CO2FIX model method, carbon balance F-CORBON model method, vortex correlation method, box method, etc[1]. From the perspective of social science research, the forest stock conver-

<!-- b000088 | furniture | pages [6] -->
Team # 2218144

<!-- b000089 | furniture | pages [6] -->
Page 6 of 25

<!-- b000090 | prose | pages [6] -->
sion factor method is the most suitable method to measure forest carbon stock from the perspective of operability, economy, long-term and accuracy of measurement, etc. Forest carbon storage is equal to the sum of tree biomass carbon sequestration, understory plant carbon sequestration and forest carbon sequestration.

<!-- b000091 | prose | pages [6] -->
3.1.1 Calculating carbon density

<!-- b000092 | prose | pages [6] -->
Carbon density is the storage of organic matter produced by plants through photo- synthetic ﬁxation of CO2 in a unit area.

<!-- b000093 | prose | pages [6] -->
C = V ×δ ×ρ ×γ (1)

<!-- b000094 | prose | pages [6] -->
Where C is the carbon density of biomass, δ is the coefﬁcient of biological expan- sion, ρ is the volume coefﬁcient, γ is the carbon content.

<!-- b000095 | prose | pages [6] -->
3.1.2 Calculating forest area

<!-- b000096 | prose | pages [6] -->
Forests play a very important role in the global carbon cycle, with logging causing 18% of the total global CO2 release, while the total amount of CO2 absorbed through photosynthesis accounts for 2/3 of all terrestrial ecosystems[2]. Therefore, forest area plays a decisive role in its carbon stock. Here, we predict the forest area for each year based on the forest area in the initial year, considering its deforestation and plantation rates.

<!-- b000097 | prose | pages [6] -->
Si = S0 ×(1−n+m)i (2)

<!-- b000098 | prose | pages [6] -->
Where Si is the forest area in thousands of hectares in year i, n is the harvesting rate, and m is the planting rate.

<!-- b000099 | prose | pages [6] -->
Calculating forest carbon sequestration 3.1.3

<!-- b000100 | prose | pages [6] -->
According to the formula of forest stock conversion factor method, we can know that the forest carbon stock depends on the sum of carbon sequestration by tree biomass and carbon sequestration by understory plants and forest land. Therefore, we add to the carbon sequestration formula is the carbon conversion coefﬁcient of understory plants, is the carbon conversion coefﬁcient of forest land and the carbon conversion coefﬁcient of trees. Meanwhile, based on the previously derived equation of carbon density and forest area, the equation of forest carbon sequestration is derived as follows

<!-- b000101 | prose | pages [6] -->
CF = Si ×C(1+α +β)

<!-- b000102 | prose | pages [6] -->
(3) 1000

<!-- b000103 | prose | pages [6] -->
Where i is the year, V is the forest storage volume per unit area in m3/ha, and CF is the forest carbon sequestration volume.

<!-- b000104 | prose | pages [6] -->
Harvested Wood Products Carbon Sequestration 3.2

<!-- b000105 | prose | pages [6] -->
Wood forest products are products provided by forests in the form of wood, mainly including logs, sawn timber, pulpwood, and man-made panels. As an extension of for-

<!-- b000106 | furniture | pages [7] -->
Team # 2218144

<!-- b000107 | furniture | pages [7] -->
Page 7 of 25

<!-- b000108 | prose | pages [7] -->
est resources, woody forest products can store carbon for a long time and play the role of carbon dioxide buffer, and its durable woody forest products have carbon emission lagging effect, which can store carbon in the products for a long time. It is estimated that the global carbon stock of woody forest products grows by about 139 hectares per year, offsetting 14% of the carbon emissions from forest harvesting. Therefore, the role of woody forest products as a huge carbon pool in mitigating climate change deserves attention.

<!-- b000109 | prose | pages [7] -->
In addition, the carbon stock function of woody forest products can effectively re- duce the concentration of carbon dioxide in the atmosphere, and its carbon stock account- ing has been included in the greenhouse gas inventory report of climate change Parties. The controversies and coordination among countries based on CBDR principles for car- bon stock measurement and trade ﬂow accounting methodology of woody forest products at the national level are related to the allocation of emission reduction responsibilities and beneﬁt sharing in climate change negotiations in the future.

<!-- b000110 | prose | pages [7] -->
Calculation of carbon conversion factors 3.2.1

<!-- b000111 | prose | pages [7] -->
HWP is divided into two categories: hardwood products, including sawn wood, wood panels and other industrial roundwood, and paper products, including paper and paperboard excluding other ﬁbrous paper products. In calculating the HWP carbon con- version factor Φj, all wood-based materials were included, including roundwood, hard- wood products, paper, waste paper, etc. The resulting carbon factor values are shown in the Table 2[3].

<!-- b000112 | caption | pages [7] -->
Table 2: HWP Carbon conversion factor

<!-- b000113 | prose | pages [7] -->
Industrial logs and related

<!-- b000114 | prose | pages [7] -->
Carbon factor 0.225

<!-- b000115 | prose | pages [7] -->
charcoal Board mean Paper and related

<!-- b000116 | prose | pages [7] -->
0.765 0.294 0.45

<!-- b000117 | prose | pages [7] -->
Calculating carbon content entering HWP pool in year i 3.2.2

<!-- b000118 | prose | pages [7] -->
According to the idea of reserve change method provided by the Intergovernmental Panel on climate change, we draw the change process of carbon sequestration of HWP as

<!-- b000119 | caption | pages [7] -->
Figure 3.

<!-- b000120 | prose | pages [7] -->
Firstly, the number of trees cut down can be obtained by multiplying the projected area of the forest with the cutting rate, and secondly, the number of trees cut down mul- tiplied by the conversion amount per unit of wood production gives the amount of trees cut down converted to forest products. Then, based on the analysis of speciﬁc types of HWP above, we divide HWP into four types: roundwood, charcoal, board mean, paper and its related, and assign them the ratio of roundwood : paper : board : charcoal =

<!-- b000121 | prose | pages [7] -->
p1 : p2 : p3 : p4. Based on the overall proportion of each type of HWP and its carbon factor amount, the amount of carbon entering the HWP carbon pool is ﬁnally derived.

<!-- b000122 | prose | pages [7] -->
U = Si ×(1−n+m)(r−1) (4)

<!-- b000123 | furniture | pages [8] -->
Team # 2218144

<!-- b000124 | furniture | pages [8] -->
Page 8 of 25

<!-- b000125 | caption | pages [8] -->
Figure 3: The Schematic of Stock-change approach

<!-- b000126 | prose | pages [8] -->
 p1

<!-- b000127 | prose | pages [8] -->


<!-- b000128 | prose | pages [8] -->
Inflow(i) = U ×n×H ×

<!-- b000129 | prose | pages [8] -->
Φ1 +

<!-- b000130 | prose | pages [8] -->
Q

<!-- b000131 | prose | pages [8] -->
 p2

<!-- b000132 | prose | pages [8] -->
 p3

<!-- b000133 | prose | pages [8] -->
 p4

<!-- b000134 | prose | pages [8] -->


<!-- b000135 | prose | pages [8] -->


<!-- b000136 | prose | pages [8] -->


<!-- b000137 | prose | pages [8] -->


<!-- b000138 | prose | pages [8] -->
Φ2 +

<!-- b000139 | prose | pages [8] -->
Φ3 +

<!-- b000140 | prose | pages [8] -->
(5)

<!-- b000141 | prose | pages [8] -->
Φ4

<!-- b000142 | prose | pages [8] -->
Q

<!-- b000143 | prose | pages [8] -->
Q

<!-- b000144 | prose | pages [8] -->
Q

<!-- b000145 | prose | pages [8] -->
Where p1, p2, p3, p4 are four HWP production ratios, Q is the total production of HWP, Ui is the estimated forest area in year (i−1), H is the conversion amount per unit of wood production, j is the carbon conversion factor of forest products, j products include four types, and In flow(i) is the amount of carbon entering the HWP carbon pool in year i.

<!-- b000146 | prose | pages [8] -->
3.2.3 Calculating HWP sequestration

<!-- b000147 | prose | pages [8] -->
There are two main sources of carbon sequestration for HWP, one is the carbon stock contained in wood and the other is the amount of carbon newly entering the HWP carbon pool in year i. Based on the coefﬁcients of the two sources, the total carbon sequestration of wood products is ﬁnally derived[4].

<!-- b000148 | prose | pages [8] -->
 

<!-- b000149 | prose | pages [8] -->
CT = e−k ×C0 +

<!-- b000150 | prose | pages [8] -->
!

<!-- b000151 | prose | pages [8] -->
1−e−k

<!-- b000152 | prose | pages [8] -->
×In folw(i) (6)

<!-- b000153 | prose | pages [8] -->
k

<!-- b000154 | prose | pages [8] -->
Where k is the ﬁrst-order decay variable for each year, C0 is the HWP carbon stock in 2000, whose value is 10,530 kilotons, Wi is the HWP carbon stock in year i, and CT is the carbon sequestration of HWP.

<!-- b000155 | prose | pages [8] -->
Calculation of total carbon sequestration 3.3

<!-- b000156 | prose | pages [8] -->
The forest carbon pool is a natural carbon dioxide reservoir, accounting for more than 86% of the global vegetation carbon pool, and the soil carbon pool it maintains ac- counts for 73% of the global soil carbon pool. HWP is a buffer for the greenhouse effect, which can store carbon for a long time and thus bufferCO2 emissions. Since March 1996, the United Nations Framework Convention on Climate Change (UNFCCC) included car- bon stock assessment of HWP as an important issue for the ﬁrst time, which formally

<!-- b000157 | furniture | pages [9] -->
Team # 2218144

<!-- b000158 | furniture | pages [9] -->
Page 9 of 25

<!-- b000159 | prose | pages [9] -->
conﬁrmed the research value of HWP carbon storage function. In addition, forestry car- bon pools in a narrow sense mainly refer to forest carbon pools, while forestry carbon pools in a broad sense include two categories of forest carbon pools and HWP carbon pools. Based on the broad classiﬁcation, forest carbon pools are speciﬁcally subdivided into biomass carbon pools, i.e., forest trees, underground vegetation, etc. Therefore, this paper considers that the total carbon sequestration has two sources, one is from the forest carbon pool and the other is from the HWP carbon pool. The forest carbon pool can be subdivided into tree biomass carbon sequestration, understory vegetation carbon seques- tration, and forest land carbon sequestration, and the HWP carbon pool can be subdivided into round wood, charcoal, wood panel mean, paper and its related four types. The ﬁ- nal total carbon sequestration is the sum of forest carbon sequestration and HWP carbon sequestration.

<!-- b000160 | prose | pages [9] -->
Z = CF +CT (7)

<!-- b000161 | prose | pages [9] -->
Where Z is the total of carbon sequestration, CT is the HWP sequestration and CF is the forest carbon sequestration.

<!-- b000162 | heading | pages [9] -->
Solving the FHWP model by using the improved bat algorithm

<!-- b000163 | prose | pages [9] -->
3.4

<!-- b000164 | prose | pages [9] -->
The bat algorithm is mainly used for objective function ﬁnding, based on the feature that bat populations use the generated acoustic waves to search for prey and control the ﬂight direction to achieve function ﬁnding. A bat is used as the basic unit and each bat has an adaptation value to optimize the function solution space. Each bat can adjust the loudness and frequency of its own emitted sound waves to search the space, so that the activity of the whole population gradually changes from disorder to order[5].

<!-- b000165 | prose | pages [9] -->
However, the bat algorithm is prone to fall into local extremes at the end of the optimization search. In this paper, we introduce a variable velocity weighting factor correction coefﬁcient to avoid the dilemma of local extremes as much as possible, so as to achieve the effect of global optimization search.

<!-- b000166 | prose | pages [9] -->
Step 1: Initialization of relevant parameters. The position of the bat is Xi, the ﬂight speed Vi, the sound loudness Ai, and the frequency yi range, with the objective function of F (xi)(i = 1,2,...,n).

<!-- b000167 | prose | pages [9] -->
Step 2: Change the solution generated by the pulse frequency and change the bat position and ﬂight speed. The position and ﬂight speed of bat i at (t −1) are ex- pressed as Xt−1

<!-- b000168 | prose | pages [9] -->
and Vt−1

<!-- b000169 | prose | pages [9] -->
. and the optimal position currently found by the group is X∗.

<!-- b000170 | prose | pages [9] -->
i

<!-- b000171 | prose | pages [9] -->
i Then, the prey is searched according to its own sound, and the position xi and ﬂight speed v(i) are adjusted by receiving feedback information. Its ﬂight speed change formula is as follows.

<!-- b000172 | prose | pages [9] -->
2

<!-- b000173 | prose | pages [9] -->


<!-- b000174 | prose | pages [9] -->
−ρ( t

<!-- b000175 | prose | pages [9] -->
T )

<!-- b000176 | prose | pages [9] -->
w(t) = wmin +(wmax −wmin)e

<!-- b000177 | prose | pages [9] -->
(8)

<!-- b000178 | prose | pages [9] -->
y(i) = y(i)min +[y(i)max −y(i)min]β

<!-- b000179 | prose | pages [9] -->
i = w(t)Vt−1

<!-- b000180 | prose | pages [9] -->
Vt

<!-- b000181 | prose | pages [9] -->
+Ai i

<!-- b000182 | prose | pages [9] -->
(9)

<!-- b000183 | prose | pages [9] -->
Xt−1

<!-- b000184 | prose | pages [9] -->
−X∗

<!-- b000185 | prose | pages [9] -->
 

<!-- b000186 | prose | pages [9] -->
y(i) (10)

<!-- b000187 | prose | pages [9] -->
i

<!-- b000188 | prose | pages [9] -->
Where w(t) which is the moment variable speed inertia weighting factor, the role is to make the bat’s pre-search to provide reference to the later search, wmax for the maximum value of w(t), wmin for the minimum value of w (t); 1 ⩽ρ ⩽Tmax, Tmax for the

<!-- b000189 | furniture | pages [10] -->
Team # 2218144

<!-- b000190 | furniture | pages [10] -->
Page 10 of 25

<!-- b000191 | prose | pages [10] -->
maximum number of iterations; picture for the current location of the optimal solution; y(i) is a random number whose frequency satisﬁes a normal uniform distribution, β is a random variable, and β ∈[0,1]. When the operation starts, the bats are randomly assigned

<!-- b000192 | prose | pages [10] -->


<!-- b000193 | prose | pages [10] -->


<!-- b000194 | prose | pages [10] -->
ymin,ymax

<!-- b000195 | prose | pages [10] -->
frequencies at the

<!-- b000196 | prose | pages [10] -->
.

<!-- b000197 | prose | pages [10] -->
i = X∗+Vt

<!-- b000198 | prose | pages [10] -->
Xt

<!-- b000199 | prose | pages [10] -->
(11) i

<!-- b000200 | prose | pages [10] -->
In order to control the position of the bat in the range of the independent variable, this paper sets a boundary rule for the case: if the position of the next movement is outside the range of the independent variable, then the position of the next ﬂight is the position on the boundary of the projection.

<!-- b000201 | prose | pages [10] -->


<!-- b000202 | prose | pages [10] -->


<!-- b000203 | prose | pages [10] -->
′

<!-- b000204 | heading | pages [10] -->
Step 3: Search for local optimal solutions F

<!-- b000205 | prose | pages [10] -->
X

<!-- b000206 | prose | pages [10] -->
.

<!-- b000207 | prose | pages [10] -->
i

<!-- b000208 | heading | pages [10] -->
Step 4: Generate multiple new solutions through multiple ﬂights of bats, con-

<!-- b000209 | heading | pages [10] -->
duct a global search. And if the new solution F′ 

<!-- b000210 | prose | pages [10] -->
the solution.

<!-- b000211 | prose | pages [10] -->


<!-- b000212 | prose | pages [10] -->


<!-- b000213 | prose | pages [10] -->


<!-- b000214 | prose | pages [10] -->
′

<!-- b000215 | prose | pages [10] -->
′

<!-- b000216 | prose | pages [10] -->
> F

<!-- b000217 | prose | pages [10] -->
X

<!-- b000218 | prose | pages [10] -->
X

<!-- b000219 | prose | pages [10] -->
is obtained, then accept

<!-- b000220 | prose | pages [10] -->
i

<!-- b000221 | prose | pages [10] -->
i

<!-- b000222 | prose | pages [10] -->
Step 5: Arrange the positions of all bats and ﬁnd the current optimal value F′ 

<!-- b000223 | prose | pages [10] -->


<!-- b000224 | prose | pages [10] -->
′

<!-- b000225 | prose | pages [10] -->
X

<!-- b000226 | prose | pages [10] -->
and the corresponding position.

<!-- b000227 | prose | pages [10] -->
i

<!-- b000228 | prose | pages [10] -->
Step 6: Set the current optimal solution to the F∗. And then make all bats con- tinue to move to the next moment and return to Step 2 to recalculate.

<!-- b000229 | prose | pages [10] -->
Step 7: End of the moment, output the optimal solution.

<!-- b000230 | heading | pages [10] -->
Algorithm 1 The Improved Bat Algorithm

<!-- b000231 | prose | pages [10] -->
objective function F (x),x = (x1,...,xd)T ; Initialize the bat population xi (i = 1,2,...,n)and yi; Define pulse frequency yi at xi; Initialize pulse rates wi and the loudness Ai; while do(t < Max number o f iterations)

<!-- b000232 | prose | pages [10] -->
Generate new solutions by ad justing frequency,; and updating velocities and locations/solutions[equations (10) to (11)] ; if rand > wi then

<!-- b000233 | prose | pages [10] -->
select a solution among the best solutions; Generate a local solution around the selected best solution; end if Generate a new solution by flying randomly; if (rand < Ai &F (xi) < F (x∗)) then

<!-- b000234 | prose | pages [10] -->
Accept the new solutions; Increase wi and reduceAi end if Rank the bats and find the current bestX∗; end while Postprocess results and visualization;

<!-- b000235 | heading | pages [10] -->
Application of FHWP model: Russia

<!-- b000236 | prose | pages [10] -->
3.5

<!-- b000237 | prose | pages [10] -->
To validate the model In order to verify the rationality of the model, we apply the model to Russia. It is well known that Russia is extremely rich in forest resources;

<!-- b000238 | furniture | pages [11] -->
Team # 2218144

<!-- b000239 | furniture | pages [11] -->
Page 11 of 25

<!-- b000240 | prose | pages [11] -->
according to the FAO 2020 statistics, Russia has 815 million hectares of forests, about 20% of the world, the ﬁrst in the world in terms of forest area[6].

<!-- b000241 | prose | pages [11] -->
The forest accumulation is 81.488 billion cubic meters, which is about 21% of the world, and the second in the world. Russian forests are unevenly distributed, mainly in sparsely populated and economically underdeveloped remote areas such as Siberia and the Far East. The forest area of Siberia and the Far East of Russia is 558 million hectares, accounting for about 72% of the total forest area in Russia, as shown in Figure 4.

<!-- b000242 | prose | pages [11] -->
Russia divides forest resources into three categories and implements classiﬁed man- agement and management. Russia’s forest management methods mainly include forest management, forest regeneration and afforestation, forest land use, forest harvesting, and forest protection. The Russian government attaches great importance to the effective management of its own forest resources, continuously increases capital investment, and modernizes forest management departments. The implementation of forest management in Russia has largely avoided the destruction of forests by urban construction and human development.

<!-- b000243 | caption | pages [11] -->
Figure 4: Tree species distribution in Russia

<!-- b000244 | prose | pages [11] -->
We consider three types of trees, larch, oak, and mountain poplar, in our model for the following reasons. Russian forests are dominated by coniferous forests, which cover 526 million hectares, mainly in Siberia and the Far East. The dominant species of Russian coniferous forests is larch, whose area is almost more than the total area of other coniferous trees. Russia’s hard broadleaf forests cover 18,183,800 hectares, mainly in the Far East, the Volga region and the Southern region. The dominant species of hard broad-leaved forests is oak, of which about 55% is distributed in the European part of Russia, while the rest of oak forests are mostly distributed in the Far East. Russia’s soft broad-leaved forests cover 227 million hectares, and their dominant species is sorrel[7].

<!-- b000245 | prose | pages [11] -->
The model results show that the value of the parameter that makes the forest and its HWP sequester the maximum amount of carbon is: n = 0.000105, m = 0.003. Therefore, we give a forest management scenario of cutting 0.0105% of trees per year for making derivatives, and the ratio of production of four derivatives is, industrial roundwood : charcoal : wood panel : paper = 1 : 4: 3 : 0.3. At the same time, Russia should plant trees equivalent to 0.3% of the national forest area per year. The amount of carbon sequestration in Russia for the period 2001-2020 is shown in Figure 5.

<!-- b000246 | furniture | pages [12] -->
Team # 2218144

<!-- b000247 | furniture | pages [12] -->
Page 12 of 25

<!-- b000248 | caption | pages [12] -->
Figure 5: Total carbon sequestration of Russia in different years(Billiontons)

<!-- b000249 | prose | pages [12] -->
4 Carbon Sequestration-Economic Value-Ecological Pro-

<!-- b000250 | heading | pages [12] -->
tection Model(CEE)

<!-- b000251 | prose | pages [12] -->
4.1

<!-- b000252 | heading | pages [12] -->
Overview of CEE model

<!-- b000253 | prose | pages [12] -->
We developed CEE model to comprehensively evaluate forest management plans. The model is evaluated through three dimensions: carbon sequestration (CS), economic value (EV), and ecological protection (EP), and each dimension will have several sub- factors. Then we will apply the entropy weighting method (EWM) to identify the twelve subfactors and the weights of the three dimensions. Finally, the ﬁnal C criteria are ob- tained to evaluate the merits of the forest management plan. The modulus and direction of C have exact meanings, and their detailed meanings will be provided later in the section

<!-- b000254 | prose | pages [12] -->
on constructing the model.

<!-- b000255 | prose | pages [12] -->
4.2 Indices description and Data Normalization

<!-- b000256 | prose | pages [12] -->
4.2.1 Indicator Description and Calculation

<!-- b000257 | prose | pages [12] -->
There are many factors that affect forest management. In order to facilitate the later research and calculation, we ﬁnally integrate the 12 most decisive indicators through 20 sets of data and divide them into three dimensions of CS, EV, and EP of C, as shown in

<!-- b000258 | caption | pages [12] -->
Figure 6.

<!-- b000259 | prose | pages [12] -->
▶Carbon Sequestration(CS)

<!-- b000260 | prose | pages [12] -->
The four indicators of CS are calculated using the method of CS model, which is not repeated here.

<!-- b000261 | prose | pages [12] -->
Tree biomass (TR): Forest biomass or standing biomass is the accumulation of dry matter produced by forest plant communities during their life cycle, and it is most impor- tant to measure tree biomass. Also, biomass affects the amount of carbon sequestered by

<!-- b000262 | furniture | pages [13] -->
Team # 2218144

<!-- b000263 | furniture | pages [13] -->
Page 13 of 25

<!-- b000264 | caption | pages [13] -->
Figure 6: Three-dimensional indicators on CEE

<!-- b000265 | prose | pages [13] -->
trees, which in turn affects the total amount of carbon sequestered.

<!-- b000266 | prose | pages [13] -->
Underground plants(UP): Understory plants are an important part of forest re- sources,which are organisms other than trees in the forest, and therefore they can also absorb and sequester carbon dioxide through photosynthesis. The larger the value of this indicator, the better it is, and it has a positive correlation with dimensionality.

<!-- b000267 | prose | pages [13] -->
Forest(FT): The above-ground carbon stock in forest ecosystem is 4.52 × 1010 t, accounting for 86% of the total above-ground carbon stock of global terrestrial plants, which is important for global carbon balance and climate change [2,3], and forest vege- tation has obvious carbon sequestration function and large carbon sink potential.

<!-- b000268 | prose | pages [13] -->
Wooden products(WP): WP are products made of wood, which are processed and produced from wood. As a derivative of forests, wood products have strong carbon se- questration capacity and can store carbon for a long time, playing the role of a carbon dioxide buffer. ▶Economic Value(EV)

<!-- b000269 | prose | pages [13] -->
Crude wood(CW): CW is a kind of wood, which is generally used to make furni- ture, and the furniture made of crude wood is not only fashionable but also very healthy, retaining the natural wood color. Therefore, the sales are very high and have a strong economic value.

<!-- b000270 | prose | pages [13] -->
Forest food(FF): FF is a variety of food products made from plants, microorganisms and animals grown in the forest ecosystem. The germicides secreted in the trees can kill the germs and microorganisms in the air, thus effectively ensuring the quality of pure, natural,healthy and nutritious food. Therefore, it has a high economic value.

<!-- b000271 | prose | pages [13] -->
Medicinial herb(MH): MH is a kind of herbal medicine that can be used as medicine. It usually grows in the forest. It not only has high medical value, but also can be sold as drugs, and has economic value that can not be underestimated. The higher the herb index, the better.

<!-- b000272 | prose | pages [13] -->
The current market price method uses the transaction prices of similar tree species or forest food or herbs that have been traded in the market as a reference base, and obtains a reasonable and fair value of forest trees based on the regional differences in geography and policy orientation, combined with local price indices, and then based on growth index conditions, etc.

<!-- b000273 | furniture | pages [14] -->
Team # 2218144

<!-- b000274 | furniture | pages [14] -->
Page 14 of 25

<!-- b000275 | prose | pages [14] -->
En = K ×Kb ×Gn ×Mn (12)

<!-- b000276 | prose | pages [14] -->
Where En is the asset appraisal value, n = 1,2,3, n = 1 represents the asset appraisal value of logs, n = 2 represents the asset appraisal value of forest foods, n = 3 represents the asset appraisal value of herbs. k is the quality adjustment factor, kb is the price index adjustment factor. Gn is the transaction price per unit of accumulation in U.S.dollar/m3, n has the same meaning as before. Mn is the amount of stockpile of the appraised asset. n has the same meaning as before.

<!-- b000277 | prose | pages [14] -->
Forest land (FL): Forest land is the carrier of forest, the source of material produc- tion and ecological services, and an important part of forest resource assets. The area of each type of forest land and its value are the main factors for assessing its economic beneﬁts.

<!-- b000278 | prose | pages [14] -->
The present value of return method of forest land is to base the evaluation of forest land on the growth of forest trees on the forest land, combine the value of forest land with the future return of forest trees, and take the long-term return in the future growth stage as the premise of measurement, and discount it all in the current period measurement. We use the proportional coefﬁcient method in the present value of earnings method with the following formula.

<!-- b000279 | prose | pages [14] -->
Au Au (1+P)n −V Bu =

<!-- b000280 | prose | pages [14] -->
(13) P

<!-- b000281 | prose | pages [14] -->
B = Bu ×K (14)

<!-- b000282 | prose | pages [14] -->
K = k1 ×k2 ×k3 (15)

<!-- b000283 | prose | pages [14] -->
Where, Bu is the present value of revenue, Au is the revenue of logging selection, V is the management fee, P is the interest rate, n is the logging selection period, k adjust- ment coefﬁcient, k1 is the coefﬁcient of stand quality, k2 is the adjustment coefﬁcient of location grade, k3 is the price index. ▶Ecological Protection (EP)

<!-- b000284 | prose | pages [14] -->
Adjusting the amount of water (AAW): The amount of water stored in the forest itself is related to forest type, geographic structure, mechanical composition and parent rock structure. It is also related to precipitation conditions and seasons. Therefore, we need to adjust the amount of water in the forest to bring it to a balanced state.

<!-- b000285 | prose | pages [14] -->
Adjustment of water value

<!-- b000286 | prose | pages [14] -->
Ut = 10×Ck ×A×(P−E −C) (16)

<!-- b000287 | prose | pages [14] -->
WhereUt is the annual adjustment of water value of the stand, the unit is dollar/year, Ck is the reservoir construction unit capacity investment (land demolition compensation,

<!-- b000288 | prose | pages [14] -->
engineering costs, maintenance costs, etc.), the unit is dollar/m3, A is the area of the stand, the unit is hm2, p is the precipitation, the unit is mm/year, E is the stand evap- otranspiration, the unit is mm/year, C is the surface runoff, the unit is mm/year. The inﬁltration capacity of soil in forest area is strong, and the surface runoff is negligible.

<!-- b000289 | prose | pages [14] -->
Purifying water (PW): PW is the ability of forest to purify water, but if too much wastewater is discharged into the forest, it may lead to the depletion of forest trees. There- fore, we need to purify sewage and wastewater to protect forests from damage.

<!-- b000290 | furniture | pages [15] -->
Team # 2218144

<!-- b000291 | prose | pages [15] -->
Value of water puriﬁcation

<!-- b000292 | furniture | pages [15] -->
Page 15 of 25

<!-- b000293 | prose | pages [15] -->
Us = 10×K ×A×(P−E −C) (17)

<!-- b000294 | prose | pages [15] -->
Where, Us indicates the annual value of water puriﬁcation in forest stands, unit is dollar/year, K is the cost of water puriﬁcation, unit is dollar/ton.

<!-- b000295 | prose | pages [15] -->
Reinforcing soil (RS): RS is one of the soil improvement techniques. Reinforcing soil is a process to improve soil properties, improve soil fertility, increase crop yields, and improve the soil environment for human survival, thereby protecting the soil and trees.

<!-- b000296 | prose | pages [15] -->
Soil consolidation volume

<!-- b000297 | prose | pages [15] -->
Gg = A×(X2 −X1) (18)

<!-- b000298 | prose | pages [15] -->
Where Gg is the annual soil consolidation in forest stands in t/year, X2 is the soil erosion modulus of non-forested land in t/hm2a, and X1 is the soil erosion modulus of forested land in t/hm2a.

<!-- b000299 | prose | pages [15] -->
Absorbing sulfur dioxide (ASD): High concentration of SO2 gas will greatly ex- ceed the tree’s ability to withstand, so that the tree in a short period of time to occur in the leaf scorch off, growth and development is seriously hampered, until withered and dead. Therefore, the absorption of SO2 is necessary to protect the growth of trees.

<!-- b000300 | prose | pages [15] -->
The value of SO2 uptake by the forest.

<!-- b000301 | prose | pages [15] -->
Uso2 = V ×Qt ×P (19)

<!-- b000302 | prose | pages [15] -->
where Uso2 is the value of forest absorption of SO2 in dollar/year, V is the forest area in hm2. Qt is the annual absorption capacity of trees for SO2 in km/hm2a, and P is the investment and treatment cost of SO2 in dollar/year.

<!-- b000303 | prose | pages [15] -->
4.2.2 Data normalization

<!-- b000304 | prose | pages [15] -->
In order to unify the data, we normalize it to get all the data with values between 0 and 1. There are three types of indices, a beneﬁt type index (the larger the better), a cost type index (the smaller the better) and a medium type index (the closer to an exact value, the better). Therefore, we provide three methods for each of them. For the beneﬁt type index, the normalization is

<!-- b000305 | prose | pages [15] -->
ri −rmin ′ i =

<!-- b000306 | prose | pages [15] -->
r

<!-- b000307 | prose | pages [15] -->
(20)

<!-- b000308 | prose | pages [15] -->
rmax −rmin

<!-- b000309 | prose | pages [15] -->
For the cost type index, the normalization method is

<!-- b000310 | prose | pages [15] -->
i = rmax −ri ′

<!-- b000311 | prose | pages [15] -->
r

<!-- b000312 | prose | pages [15] -->
(21)

<!-- b000313 | prose | pages [15] -->
rmax −rmin

<!-- b000314 | prose | pages [15] -->
For medium type indexes with medium intervals [a, b], the normalization is

<!-- b000315 | prose | pages [15] -->
1−a−ri

<!-- b000316 | prose | pages [15] -->
  

<!-- b000317 | prose | pages [15] -->
′

<!-- b000318 | prose | pages [15] -->
M ,ri < a 1,a ⩽ri ⩽b

<!-- b000319 | prose | pages [15] -->
ri =

<!-- b000320 | prose | pages [15] -->
(22)

<!-- b000321 | prose | pages [15] -->
1−ri−b

<!-- b000322 | prose | pages [15] -->
 

<!-- b000323 | prose | pages [15] -->
M ,ri > b

<!-- b000324 | furniture | pages [16] -->
Team # 2218144

<!-- b000325 | furniture | pages [16] -->
Page 16 of 25

<!-- b000326 | prose | pages [16] -->
Where M is determined by the minimum and maximum values of the indices for multiple countries, as shown below.

<!-- b000327 | prose | pages [16] -->
M = max{a−min{ri},max{ri}−b} (23)

<!-- b000328 | prose | pages [16] -->
Calculation of weights by EWM 4.3

<!-- b000329 | prose | pages [16] -->
Among the 12 indicators in the three dimensions, it is clear that different factors have different effects on their dimensions, which also play different roles in our ﬁnal results. Therefore, we will apply the entropy weighting method (EWM) to conﬁrm the weight of each indicator.

<!-- b000330 | prose | pages [16] -->
The basic idea of entropy weighting method is to determine the objective weight ac- cording to the size of the variability of indicators. Generally speaking, if the information entropy of an indicator is smaller, it indicates that the greater the variability of the indica- tor, the more information it provides, the greater the role it can play in the comprehensive evaluation, and the greater its weight. On the contrary, if the information entropy of an indicator is larger, it means that the degree of variation of the indicator is smaller, and the amount of information provided is also smaller, and the role it plays in the comprehensive evaluation is also smaller, and its weight is also smaller.

<!-- b000331 | prose | pages [16] -->
4.3.1 Steps of EWM

<!-- b000332 | prose | pages [16] -->
Firstly, each index is de-normalized. X1,X2,..., Suppose that m indicators are given as

<!-- b000333 | prose | pages [16] -->
Xm , where Xi = {x1,x2,...,xm}. Assume that the value after normalizing the data of each indicator is Y1,Y2,...,Ym.

<!-- b000334 | prose | pages [16] -->
Find the ratio of each indicator under each program. That is, the weight of the jth indicator in the ith program for that indicator, which is actually to calculate the size of the variation of the indicator.

<!-- b000335 | prose | pages [16] -->
Yij pi j =

<!-- b000336 | prose | pages [16] -->
,i = 1,...,n, j = 1,...,m

<!-- b000337 | prose | pages [16] -->
∑n

<!-- b000338 | prose | pages [16] -->
i=1Yij

<!-- b000339 | prose | pages [16] -->
(24)

<!-- b000340 | prose | pages [16] -->
To ﬁnd the information entropy of each indicator. According to the deﬁnition of information entropy in information theory, the information entropy of a set of data is

<!-- b000341 | prose | pages [16] -->
n

<!-- b000342 | prose | pages [16] -->
Ej = −ln(n)−1

<!-- b000343 | prose | pages [16] -->
∑pij ln pij (25)

<!-- b000344 | prose | pages [16] -->
Where Ej ⩾0. If Pi j = 0, deﬁne Ej = 0. Determine the weights of each index. Ac- cording to the formula of information entropy, the information entropy of each indicator is calculated as E1,E2,...,Em. Calculate the weights of each indicator by information entropy.

<!-- b000345 | prose | pages [16] -->
wj = 1−Ej

<!-- b000346 | prose | pages [16] -->
k −∑Ej

<!-- b000347 | prose | pages [16] -->
(j = 1,2,...,m) (26)

<!-- b000348 | prose | pages [16] -->
Here k refers to the number of indicators, i.e. k = m. The weights can also be

<!-- b000349 | furniture | pages [17] -->
Team # 2218144

<!-- b000350 | furniture | pages [17] -->
Page 17 of 25

<!-- b000351 | prose | pages [17] -->
calculated by calculating the information redundancy.

<!-- b000352 | prose | pages [17] -->
Dj = 1−Ej

<!-- b000353 | prose | pages [17] -->
Then calculate the indicator weights.

<!-- b000354 | prose | pages [17] -->
wj =

<!-- b000355 | prose | pages [17] -->
(27)

<!-- b000356 | prose | pages [17] -->
Dj

<!-- b000357 | prose | pages [17] -->
(28)

<!-- b000358 | prose | pages [17] -->
∑m

<!-- b000359 | prose | pages [17] -->
j=1 Dj

<!-- b000360 | prose | pages [17] -->
Finally, the overall score of each solution is calculated.

<!-- b000361 | prose | pages [17] -->
m

<!-- b000362 | prose | pages [17] -->
si =

<!-- b000363 | prose | pages [17] -->
∑ j=1

<!-- b000364 | prose | pages [17] -->
4.3.2

<!-- b000365 | heading | pages [17] -->
Weight calculation results by EWM

<!-- b000366 | prose | pages [17] -->
wj · pij (29)

<!-- b000367 | prose | pages [17] -->
The CS,EV,EP weights calculated by EWM are shown below.

<!-- b000368 | prose | pages [17] -->
WCS = (0.19 0.18 0.18 0.45)T

<!-- b000369 | prose | pages [17] -->
WEV = (0.47 0.12 0.13 0.26)T

<!-- b000370 | prose | pages [17] -->
WEP = (0.13 0.20 0.33 0.16)T

<!-- b000371 | prose | pages [17] -->
The ﬁnal integral weights are shown in Figure 7.

<!-- b000372 | caption | pages [17] -->
Figure 7: Weight for 3 Dimensions

<!-- b000373 | prose | pages [17] -->
From the above Figure 7, we know that WP has a high weight in the amount of carbon sequestration, and its share is 45%. In the economic value dimension, CW plays an important role with 47%, and the importance of FF and MH is very similar. In the EP dimension, both PW and AAW are important indicators.

<!-- b000374 | prose | pages [17] -->
4.4

<!-- b000375 | heading | pages [17] -->
Establishment of CEE Model

<!-- b000376 | prose | pages [17] -->
Based on the above discussion, we obtained the ﬁnal evaluation scores for each country for the three dimensions, which are expressed as

<!-- b000377 | prose | pages [17] -->


<!-- b000378 | prose | pages [17] -->
CS = Q1 ·W1

<!-- b000379 | prose | pages [17] -->
 

<!-- b000380 | prose | pages [17] -->
(30)

<!-- b000381 | prose | pages [17] -->
EP = Q2 ·W2

<!-- b000382 | prose | pages [17] -->


<!-- b000383 | prose | pages [17] -->
EV = Q3 ·W3

<!-- b000384 | prose | pages [17] -->


<!-- b000385 | furniture | pages [18] -->
Team # 2218144

<!-- b000386 | furniture | pages [18] -->
Page 18 of 25

<!-- b000387 | caption | pages [18] -->
Figure 8: CEE model vector diagram

<!-- b000388 | prose | pages [18] -->
Where Qi is a row vector of one-dimensional index values for a country. Then we combine them into a three-dimensional vector C. Its components are the three values of CS, EV, and EP, respectively, whose ranges range are in [0,1], as shown in Figure 8.

<!-- b000389 | prose | pages [18] -->
In this case, the vector C0 = (1,1,1) is the criterion of the forest management plan. The modulus of C0 indicates that the forest management plan reaches the optimal level in the three dimensions of economic value, environmental protection, and carbon seques- tration, showing the best state of forest management. The direction of C0 represents the ideal equilibrium condition of the forest management plan, showing the sustainability of this management plan. Also, the excellent modulus will promote its sustainability.

<!-- b000390 | prose | pages [18] -->
|C| is the modulus of C, which represents the degree of development of forest man- agement. It is more concerned with describing the current level of forest management plan. When |C| is too small, the forest management plan is unbalanced.

<!-- b000391 | prose | pages [18] -->
4.5

<!-- b000392 | heading | pages [18] -->
Application of CEE model: China

<!-- b000393 | prose | pages [18] -->
The question asks for the conditions that keep the forest from being deforested and also gives the transition points for the different management plans. The idea is to set the transition period between the two forest plans to 5 years, and to establish the new forest plan with a deforestation rate of 0 and a planting rate of k, so as to solve for the average annual planting rate needed to reach the amount of carbon sequestered by the forest plan before the change. In this process, every effort should be made to keep the overall state of the three evaluation dimensions of the forest constant or slightly decreasing (expressed as a non-signiﬁcant change in the mode length of the vector in the CEE model). We take China as an example to answer the above questions using the developed model.

<!-- b000394 | prose | pages [18] -->
The CEE model is solved to derive the scores for the three dimensions of the forest in China in 2020 in the presence of deforestation, as well as the overall score. At this point, the deforestation rate, the planting rate, and the carbon sequestration in tons. If there is no deforestation and no planting in 2020, the amount of carbon sequestered decreases to 10,000 tons. Using 2021 as the starting point, the FHWP model yields that the average planting rate during the transition period should be. At the end of 2025 (the transition period), the forest is evaluated with an overall score. Compared to the year before the transition period begins (2020), the dimensional score decreases signiﬁcantly, while the remaining two dimensions show a small increase. The reason for the signiﬁcant drop in scores is that no new wood derivatives will be produced if no tree cutting takes place,

<!-- b000395 | furniture | pages [19] -->
Team # 2218144

<!-- b000396 | furniture | pages [19] -->
Page 19 of 25

<!-- b000397 | prose | pages [19] -->
while at the same time, the amount of carbon sequestered by HWP will decrease year by year due to the existence of a half-life, and the weighting of the dimension scores is large. Due to the signiﬁcant decrease in the scores, the overall scores also show a decrease.

<!-- b000398 | prose | pages [19] -->
To make the above process more clearly shown, we will graphically demonstrate the following.

<!-- b000399 | caption | pages [19] -->
Figure 9: 2020 bisector surface

<!-- b000400 | caption | pages [19] -->
Figure 10: 2025 bisector surface

<!-- b000401 | prose | pages [19] -->
In Figure 9, we introduce the isoscore surface γ, where all points on the surface have an overall score of 0.9689. It can be seen that the vector Z2020 ends on the departing surface and Z2025 does not reach the surface. Similarly, in Figure 10, we introduce an isosurface η based on Figure 10, where all points on the surface η have the same overall score of Z2025,0.8716. It is clear that the surface η is closer to the origin than the surface γ, Z2025 on the surface η, and Z2020 exceeds η the reach γ, meaning that the overall state of the forest of Z2020 is better than Z2025.

<!-- b000402 | prose | pages [19] -->
5 Case Study: Find out better forest management strate- gies

<!-- b000403 | prose | pages [19] -->
5.1 Problems caused by mismanagement of Sudan’s forests

<!-- b000404 | prose | pages [19] -->
Sudan, a Nile riparian country in transition from desert to steppe. Charcoal, which is known as oil in Sudan, has become one of the livelihoods of Sudanese people. Sudanese families cut down trees, burn charcoal and sell it at low prices to make ends meet. At the same time, the Sudanese government exports large quantities of charcoal to foreign countries every year to earn foreign currency. However, due to Sudan’s technological limitations, only 20% of the wood is used for charcoal burning, while the remaining 80% is wasted. The annual deforestation rate is close to 504,000 hectares, but only 30,000 hectares of land are reforested[8].

<!-- b000405 | prose | pages [19] -->
In the past two decades, due to overgrazing and logging, some trees and plants have disappeared, forest resources have been greatly damaged, and the ecological environment is strongly threatened, as shown in Figure 11.

<!-- b000406 | furniture | pages [20] -->
Team # 2218144

<!-- b000407 | furniture | pages [20] -->
Page 20 of 25

<!-- b000408 | caption | pages [20] -->
Figure 11: Problems caused by the sharp decline of forests in Sudan

<!-- b000409 | prose | pages [20] -->
5.2

<!-- b000410 | heading | pages [20] -->
Results of applying CEE and HHWP model to Sudan

<!-- b000411 | prose | pages [20] -->
Using CEE model, we evaluated the state of Sudan’s forests from 2011-2020 in three dimensions, and the evaluation results are shown in the Figure 12.

<!-- b000412 | prose | pages [20] -->
Due to the poor forest management status, the individual scores of CS, EV, and EP as well as the total evaluation scores of Sudan show a decreasing trend. the CS decreases from 0.5861 to 0.3708, a decrease of 36.73%; the EV decreases from 0.5673 to 0.3991, a decrease of 29.65%; the EP decreases from 0.5592 to 0.3874, a decrease of 30.72%; and cut from 0.9935 to 0.6753, a decrease of 32.03%. It is foreseeable that if Sudan does not adjust to the current situation, its forest condition will further deteriorate and the negative environmental effects will be more serious.

<!-- b000413 | prose | pages [20] -->
According to the relevant reports of the United Nations Environment Program, Su- dan has an average annual deforestation rate of 2.25% and almost no afforestation activi- ties. Using the FHWP measurement model, we calculate the present carbon sequestration of forests and their derivatives in Sudan and predict the carbon sequestration in 100 years, and the results show that in 2020, the forest area in Sudan is 1.83595×107 hectares and the total carbon sequestration is 2.0226 × 1010 tons. Under Sudan’s current forest man- agement scenario, which involves deforestation without planting, its forest area decreases to 1.886×106 hectares and total carbon sequestration is cut to 4.1384×109 tons in 2120.

<!-- b000414 | prose | pages [20] -->
5.3 Best forest management plan in Sudan

<!-- b000415 | prose | pages [20] -->
Next, we will optimize Sudan’s forest management plan based on the principle that after a 10-year adjustment period, Sudan’s carbon sequestration in 2030 will be as large as possible, while ensuring a higher score for its forest status.

<!-- b000416 | prose | pages [20] -->
From the Food and Agriculture Organization of the United Nations(FAO), we know that Australia’s forest management is among the best in the world. The country vigor- ously develops planted forests and carries out intensive management to give full play to their economic beneﬁts, while taking into account the ecological and social beneﬁts. At the same time, it focuses on protecting and developing natural forests to give full play

<!-- b000417 | furniture | pages [21] -->
Team # 2218144

<!-- b000418 | furniture | pages [21] -->
Page 21 of 25

<!-- b000419 | prose | pages [21] -->
to their ecological and social beneﬁts, while taking into account their economic bene- ﬁts. Referring to the data on the production of wood derivatives in the country, we were able to determine the production ratios of four wood products (industrial roundwood, charcoal, wood panels and paper). Further, we used FHWP model to ﬁnd the maxi- mum carbon sequestration in Sudan in 2030 and its corresponding forest management plan. Speciﬁcally, the forest area in 2030 is 2.2645×107 hectares, the maximum carbon sequestration is 2.8013 × 1010 tons, the deforestation rate n = 0.21%, and the planting rate m = 2.33%. If Sudan implements this improved forest management plan, it will have sequestered 1.7419 × 1011 tons of carbon by 2120 years after 100 years, which is a 42.09-fold increase in carbon sequestration compared to the predicted value without optimization.

<!-- b000420 | prose | pages [21] -->
To more clearly demonstrate the effect of the optimization strategy, the predicted values of CS, EV, EP, forest area and |C| and Z, and carbon sequestration for both the unoptimized and optimized scenarios from 2030 to 2120 are compared in images and tables forms, as shown in and Figure 13 and Table 3.

<!-- b000421 | caption | pages [21] -->
Figure 12: Strategy score before

<!-- b000422 | prose | pages [21] -->
optimization

<!-- b000423 | caption | pages [21] -->
Figure 13: Strategy score after

<!-- b000424 | prose | pages [21] -->
optimization

<!-- b000425 | caption | pages [21] -->
Table 3: Preditive valus in 2120 years before and after aptimization

<!-- b000426 | prose | pages [21] -->
Scores

<!-- b000427 | prose | pages [21] -->
CS EV EP

<!-- b000428 | prose | pages [21] -->
Estimate

<!-- b000429 | prose | pages [21] -->
|C| Z Forest area

<!-- b000430 | prose | pages [21] -->
0.040998 Before 0.075671 0.040998 0.095329502 4130 18900 0.9583 After 0.9534 0.9431 1.648256066 17400 1500000

<!-- b000431 | prose | pages [21] -->
As can be seen in Figure 13, the sub-scores of CS, EV, and EP, as well as the overall score, have improved signiﬁcantly after the optimization of the forest management plan. Without the forest plan reform, the state of Sudan’s forests would have gradually deterio- rated, as shown in the graph by the yearly decrease in sub-scores and overall scores. After optimizing the management plan, Sudan was able to reverse the dangerous situation, and the performance of the forest in the three areas of carbon sequestration, economy, and ecology gradually improved, leading to an overall improvement in the status. Table 3

<!-- b000432 | furniture | pages [22] -->
Team # 2218144

<!-- b000433 | furniture | pages [22] -->
Page 22 of 25

<!-- b000434 | prose | pages [22] -->
shows that by 2120 years after 100 years, the optimized plan has signiﬁcantly improved the CS, EV, EP, carbon sequestration, and forest area compared to the unoptimized plan. In summary, our proposed improved forest management plan is effective in practice.

<!-- b000435 | prose | pages [22] -->
6

<!-- b000436 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000437 | prose | pages [22] -->
In the full paper, we complete the solution of carbon sequestration, forest area, and plan score by F-HWP model for a speciﬁc area forest, and calculate the corresponding optimal cutting rate n and planting rate m to complete the forest management plan. Two parameters in the model, corresponding to the cutting rate n and planting rate m, are important for the development of the forest plan. The two parameters are crucial to the structure of the model. They are estimated by us with the help of the model and partially dependable data, so we analyze their sensitivity to the model.

<!-- b000438 | caption | pages [22] -->
Figure 14: Change of Z under different

<!-- b000439 | caption | pages [22] -->
Figure 15: Change of Z under different

<!-- b000440 | prose | pages [22] -->
n under m = 0.0233

<!-- b000441 | prose | pages [22] -->
m under n = 0.0021

<!-- b000442 | prose | pages [22] -->
In Figures 14 and 15, we analyze the variation of carbon sequestration under differ- ent n taken at m = 0.0233 and under different m taken at n = 0.0021 for the Sudanese optimal forest management plan with the developed cutting rate and planting rate (n,m) as an example. The analysis showed that the amount of carbon sequestration Z was sen- sitive to n and m in FHWP model. The optimal forest plans under (0.0021, 0.0233) all corresponded to greater carbon sequestration than the forest management plans under (0.0021, 0.0230), (0.0015, 0.0233), and (0.0021, 0.0220).

<!-- b000443 | prose | pages [22] -->
7

<!-- b000444 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b000445 | heading | pages [22] -->
Strengths

<!-- b000446 | prose | pages [22] -->
• In solving the FHWP model, we introduce variable velocity weighting factor cor- rection coefﬁcients to improve the bat algorithm, which makes solving the FHWP model avoid local extremes and thus achieve a global optimal solution.

<!-- b000447 | prose | pages [22] -->
• We establish a multi-level indicator system based on 3D vectors, and give the vector modulus actual meaning, so that the performance of the evaluation object in each

<!-- b000448 | furniture | pages [23] -->
Team # 2218144

<!-- b000449 | furniture | pages [23] -->
Page 23 of 25

<!-- b000450 | prose | pages [23] -->
dimension can be displayed in 3D vector images. And the ﬁrst-level indicators of the model cover multiple dimensions and the second-level indicators are more detailed, which ensures the comprehensiveness and applicability of the evaluation model.

<!-- b000451 | prose | pages [23] -->
• Our proposed improved forest management strategy not only improves the carbon sequestration of forests and wood products, but also enhances the performance of forests in terms of economic value and ecological protection.

<!-- b000452 | heading | pages [23] -->
Weaknesses

<!-- b000453 | prose | pages [23] -->
• The study on carbon sequestration of HWP in this paper only considered the in-use HWP and did not consider the case of landﬁlls. The life span of wood products under anoxic conditions like landﬁlls is very long, and the important component of wood material, lignin, does not decay or decays extremely slowly. If the amount of HWP carbon in the landﬁll pond is taken into account, the estimated carbon stock value is bound to be enhanced and the model results will be more accurate.

<!-- b000454 | prose | pages [23] -->
• CEE cannot reduce the dimensionality of the evaluation index. Meanwhile, the entropy weighting method obtains weights based only on the degree of ﬂuctuation of data, or the amount of information, without considering the actual meaning of the data, and is likely to yield results that are contrary to reality. 1. In solving the FHWP model, we introduce variable velocity weighting factor correction coefﬁ- cients to improve the bat algorithm, which makes solving the FHWP model avoid local extremes and thus achieve a global optimal solution.

<!-- b000455 | furniture | pages [25] -->
Team # 2218144

<!-- b000456 | furniture | pages [25] -->
Page 25 of 25

<!-- b000457 | heading | pages [25] -->
References

<!-- b000458 | references | pages [25] -->
[1] IPCC., IPCC Guidelines for National Greenhouse Gas Inventories, Intergovernmen-

<!-- b000459 | references | pages [25] -->
tal Panel on Climate Change 2006 Chapter 12: Harvested Wood Products., Cam-

<!-- b000460 | references | pages [25] -->
bridge, New York: Cambridge University Press, 2006.

<!-- b000461 | references | pages [25] -->
[2] Dixon R K, Brown S, Houghton R A, et al,. Carbon pools and ﬂux of global forest

<!-- b000462 | references | pages [25] -->
ecosystems, Science, 1994.

<!-- b000463 | references | pages [25] -->
[3] Winjum J K, Brown S, Schlamadinger B., Forest harvests and wood products:

<!-- b000464 | references | pages [25] -->
Sources and sinks of atmospheric carbon dioxide, Forest Science, 1998.

<!-- b000465 | references | pages [25] -->
[4] Yang, X. S.,Nature-Inspired Metaheuristic Algoirthms, 2nd Edition, Luniver Press,

<!-- b000466 | references | pages [25] -->
2010.

<!-- b000467 | references | pages [25] -->
[5] Yang X., A new metaheuristic bat-inspired algorithm. Nature Inspired Cooperative

<!-- b000468 | references | pages [25] -->
Strategies for Optimization, 2010.

<!-- b000469 | references | pages [25] -->
[6] Yang H Q , Chun-Yi J I , Yang H , et al. Global Climate Change and China’s Con-

<!-- b000470 | references | pages [25] -->
tribution to Carbon Reduction:Based on Carbon Storage Accounting of Chinese

<!-- b000471 | references | pages [25] -->
Harvested Wood Products, Journal of Natural Resources, 2013.

<!-- b000472 | references | pages [25] -->
[7] Olga N Krankina, Mark E Harmon, Jack K Winjum, Carbon storage and sequestra-

<!-- b000473 | references | pages [25] -->
tion in the russian forest sector, AMBIO, 1996.

<!-- b000474 | references | pages [25] -->
[8] Moghraby A., State of the environment in Sudan, 2003.
