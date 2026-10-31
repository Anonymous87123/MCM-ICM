# P-A-2023-2303950-5f87464b

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2023

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
A

<!-- b000005 | title | pages [1] -->
2303950

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
A Methodology to Simulate Drought-Stricken Plant Communities

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
The study of plant communities in arid areas is an indispensable part of environmental protection. In these regions, annual plants are important components of vegetation, by virtue of their unique characteristics. This paper presents a method of simulation for the growth, competition, and facilitation of annual plants, which can be applied to various circumstances.

<!-- b000010 | prose | pages [1] -->
To begin with, we establish the Growth Model of annual plants. At first, we determine the relationship between soil water content and the natural growth rate in Logistic Model. Then, we build the differential equation of soil water content, based on the stochastic rainfall model. Finally, we establish the law of annual plant reproduction. To estimate the statistical parameters in the stochastic rainfall model, we use Normal Equation to get the optimal parameters according to Least Square Method.

<!-- b000011 | prose | pages [1] -->
Based on the Growth Model, we establish the Competition Model of various plants to simulate their root competition. For the competition coefficient in Lotka-Volterra Model, we innovatively determine its relationship with root growth and water-utilizing capacity of plants. Considering the structure of root system, we estimate the parameters in the model reasonably.

<!-- b000012 | prose | pages [1] -->
Based on the Competition Model, we further establish the Facilitation Model of shrub plants to herbaceous plants. Given the water-lifting action of shrub plants, we modify the water absorption rate in the Competition Model. So far, our models have been elaborated and the parameters have been estimated properly.

<!-- b000013 | prose | pages [1] -->
After that, we use the fourth order Runge-Kutta algorithm to give numerical solutions to the differential equations. And the problems in the Requirement have been solved as follows:

<!-- b000014 | prose | pages [1] -->
⚫ Based on the results from our TOPSIS model, at least eight plant species are required to provide overall benefits for the community. As the number of plant species grows, the scale of the community will decrease, while the community will embrace better stability.

<!-- b000015 | prose | pages [1] -->
⚫ By improving the water absorption efficiency of herbaceous plants, shrubs can reduce the interspecific competition, make the average biomass of different herbaceous plants close to each other, and improve the stability of biodiversity.

<!-- b000016 | prose | pages [1] -->
⚫ Under more severe drought conditions provided in Section 5.4, the scale of the community will be decreased by over 67% and the fluctuation of the evolution will be enlarged by over 36%. But these indexes still follow the similar trend in Section 5.2 as the number of species grows regardless of different weather cycles.

<!-- b000017 | prose | pages [1] -->
⚫ The effects of two typical types of pollutants are compared. The results show that pollutants such as acid rain are more dangerous because it can decrease the scale by 14.6% and increase the fluctuation by 14.4% at the same time. Also, the diminishment of habitat by 50% will cause the system to lose 22.9% of its scale but reduce 8.7% of its fluctuation.

<!-- b000018 | prose | pages [1] -->
⚫ Based on our model and analysis, our strategies are expressed from two main aspects： the Preservation and Modification of the ecosystem.

<!-- b000019 | prose | pages [1] -->
Finally, the sensitivity and stability of the model are fully analyzed.

<!-- b000020 | keywords | pages [1] -->
Keywords: Growth Model; Competition model; Facilitation model; 4th Runge-Kutta; TOPSIS

<!-- b000021 | furniture | pages [2] -->
Team # 2303950

<!-- b000022 | furniture | pages [2] -->
Page 2 of 25

<!-- b000023 | heading | pages [2] -->
Content

<!-- b000024 | contents | pages [2] -->
1 Introduction ...................................................................................................... 3

<!-- b000025 | contents | pages [2] -->
1.1 Background ...................................................................................................................... 3

<!-- b000026 | contents | pages [2] -->
1.2 Restatement of the Problem ............................................................................................. 3

<!-- b000027 | contents | pages [2] -->
1.3 Our Work .......................................................................................................................... 4

<!-- b000028 | contents | pages [2] -->
2 Assumptions and Justifications ....................................................................... 4

<!-- b000029 | contents | pages [2] -->
3 Notations ........................................................................................................... 5

<!-- b000030 | contents | pages [2] -->
4 Model Establishment ....................................................................................... 6

<!-- b000031 | contents | pages [2] -->
4.1 The Growth Model of One Species in Drought Circumstances....................................... 6

<!-- b000032 | contents | pages [2] -->
4.2 The Competition Model of Multiple Species ................................................................... 9

<!-- b000033 | contents | pages [2] -->
4.3 The Facilitation Model of Shrub Plants to Herbaceous Plants ...................................... 12

<!-- b000034 | contents | pages [2] -->
4.4 Reasonable Estimation of Essential Parameters ............................................................ 13

<!-- b000035 | contents | pages [2] -->
5 Model Computed and Results Analysis ....................................................... 15

<!-- b000036 | contents | pages [2] -->
5.1 Model Computed Algorithm .......................................................................................... 15

<!-- b000037 | contents | pages [2] -->
5.2 Evaluation of the Benefit for a Multi-Plants Community .............................................. 16

<!-- b000038 | contents | pages [2] -->
5.3 The Effect of Different Types of Species in the Community ......................................... 17

<!-- b000039 | contents | pages [2] -->
5.4 The Effect of Fluctuant Frequency of Drought .............................................................. 18

<!-- b000040 | contents | pages [2] -->
5.5 The Impact of Other Factors on Plant Community ........................................................ 19

<!-- b000041 | contents | pages [2] -->
5.6 Measures Needed for Long-Term Viability ................................................................... 20

<!-- b000042 | contents | pages [2] -->
6 Sensitivity Analysis and Stability Analysis .................................................. 21

<!-- b000043 | contents | pages [2] -->
6.1 Sensitivity Analysis ........................................................................................................ 21

<!-- b000044 | contents | pages [2] -->
6.2 Stability Analysis ........................................................................................................... 22

<!-- b000045 | contents | pages [2] -->
7 Strengths and Weaknesses ............................................................................. 24

<!-- b000046 | contents | pages [2] -->
7.1 Strengths ........................................................................................................................ 24

<!-- b000047 | contents | pages [2] -->
7.2 Weaknesses .................................................................................................................... 24

<!-- b000048 | contents | pages [2] -->
References .......................................................................................................... 25

<!-- b000049 | furniture | pages [3] -->
Team # 2303950

<!-- b000050 | furniture | pages [3] -->
Page 3 of 25

<!-- b000051 | heading | pages [3] -->
1 Introduction

<!-- b000052 | heading | pages [3] -->
1.1 Background

<!-- b000053 | prose | pages [3] -->
Arid environments are characterized by limited and variable rainfall that supplies resources in pulses. And grasslands, mostly covered by herbages and shrubs, are quite sensitive to the shortage of water. Plenty of observations reveal that the number of different species has essential effects on how a plant community adapts to droughts which may take place at changeable frequencies and wide range of severity. To be specific, plants are better adapted to drought conditions in communities with several species, rather than in those with only one species. Therefore, this phenomenon, which is a consequence of localized biodiversity, is of great research value.

<!-- b000054 | caption | pages [3] -->
Figure 1: A Plant Community in Arid Environment

<!-- b000055 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000056 | prose | pages [3] -->
Considering the background information and limiting conditions identified in the problem statement, we are supposed to address the following issues: ⚫ Build a mathematical model to describe drought adaptability with regard to the number of species in a plant community. Notably, we need to predict what changes will take place when a plant community is exposed to variable weather cycles. And our model should account for interactions between different species in this process. ⚫ Find out the minimal number of species necessary for a plant community to benefit from localized biodiversity. And forecast what will happen when the number of species increases. What is more, we should analyze the sensitivity of the model by changing the types of species in the plant community.

<!-- b000057 | furniture | pages [4] -->
Team # 2303950

<!-- b000058 | furniture | pages [4] -->
Page 4 of 25

<!-- b000059 | prose | pages [4] -->
⚫ Discuss whether the number of species have the same impact on the overall population if the occurrence of droughts has fluctuant frequency and greater variation. Meanwhile, we should also take other factors such as pollution and habitat reduction into consideration. ⚫ Illustrate what measures should be taken to ensure the long-term viability of a plant community. Conclude the impacts of this phenomenon on the larger environment.

<!-- b000060 | heading | pages [4] -->
1.3 Our Work

<!-- b000061 | prose | pages [4] -->
In this paper, we establish three mathematical models progressively and address six problems, which are listed below:

<!-- b000062 | caption | pages [4] -->
Figure 2: Models and Problems

<!-- b000063 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000064 | prose | pages [4] -->
To simplify the problems, we make the following assumptions, each of which is justified. ⚫ Assumption 1: The research object of this paper is mainly summer-type annual plants, whose life cycle is from spring to autumn. The biomass of these plants will be converted into the biomass of seed banks in winter.

<!-- b000065 | prose | pages [4] -->
→Justification: According to [1], annual plants have the characteristics of fast growth, strong reproductive ability and short life cycle. These plants are an important part of vegetation in arid areas, with high research value. ⚫ Assumption 2: Rainfall is completed instantaneously in arid areas, and there is no additional water supply between two rains.

<!-- b000066 | prose | pages [4] -->
→Justification: The duration of each rainfall in arid areas is far shorter than the time- scale in years which we want to study. At the same time, the vast majority of arid areas are short of surface water resources, such as rivers and lakes. So, we can consider that the only way for water supply is rainfall. ⚫ Assumption 3: Water evaporation is directly proportional to the total water amount in the soil in arid areas.

<!-- b000067 | furniture | pages [5] -->
Team # 2303950

<!-- b000068 | furniture | pages [5] -->
Page 5 of 25

<!-- b000069 | prose | pages [5] -->
→Justification: The evaporation effect of water in arid areas is significant throughout the year. In addition, the soil in arid areas is usually loose. Therefore, the water in the soil is exposed to air uniformly, so we can infer that the water evaporation is proportional to the total water amount. ⚫ Assumption 4: Annual plants have a regular period of flowering and fruiting, and the duration of flowering is short.

<!-- b000070 | prose | pages [5] -->
→Justification: Annual plants have fixed life cycle and regular flowering period. Due to the influence of arid environment, the flowering period of plants is generally short, often within several days. This span is also far shorter than the time-scale in years which we want to study. ⚫ Assumption 5: The average biomass (or average mass) of plants is directly proportional to the volume of the root system.

<!-- b000071 | prose | pages [5] -->
→Justification: It can be seen that a plant needs more resources if its biomass is larger.

<!-- b000072 | prose | pages [5] -->
And the main limitation of plants is the shortage of water in arid areas. Considering that the root system is the main way for plants to absorb water, it is plausible to assume that the average biomass of plants is directly proportional to the volume covered by roots. ⚫ Assumption 6: In the experimental area, the plants distribute evenly.

<!-- b000073 | prose | pages [5] -->
→Justification: In order to reduce the competition for resources, the plants tend to distribute evenly all over the area. ⚫ Assumption 7: In the process of plant growth (between germination and flowering), the death of the whole plant is not considered.

<!-- b000074 | prose | pages [5] -->
→Justification: In our model, environmental restricts and interspecific competitions are considered to have an impact on the average biomass of the plants. We ignore the possibility that the above factors may lead to the death of the whole plant.

<!-- b000075 | heading | pages [5] -->
3 Notations

<!-- b000076 | prose | pages [5] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000077 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000078 | prose | pages [5, 6] -->
Symbol Definition Unit inherent growth rate the average biomass of species the maximum average biomass of species  within environmental limit resource availability (soil water content) the rate of resource uptake per unit biomass the conversion efficiency from water to biomass increment the loss rate of plants per unit time to what extent water absorption rate changes with resource availability the upper limit of water absorption rage controls the variation trend of the uptake curve the biomass of seed bank of species the conversion ratio from the total biomass into seeds the water resources consumed by unit biomass of plant  is times of that of plant , in which plant is located the average diameter of root extension of plant the relative water-utilizing capacity the average root coverage of plant the average overlapping area of plant and other plants the volume of the root system of a plant scale factor of to the number of plants the upper limit of water absorption rage with competition the water-lift capacity of shrubs per unit biomass the root length in total the average length of a root root coefficient the total weight of the plant species in the year the average total weight the yearly fluctuation of the total weight (variance of the data)

<!-- b000079 | furniture | pages [6] -->
Team # 2303950

<!-- b000080 | furniture | pages [6] -->
Page 6 of 25

<!-- b000082 | heading | pages [6] -->
4 Model Establishment

<!-- b000083 | heading | pages [6] -->
4.1 The Growth Model of One Species in Drought Circumstances

<!-- b000084 | prose | pages [6] -->
This section establishes the growth model of only one species in drought circumstances. In this case, there is only one species in a certain area. We define as the average biomass of species , which will increase according to Logistic Model. We have

<!-- b000085 | prose | pages [6] -->
(1)

<!-- b000086 | prose | pages [6] -->
where is inherent growth rate, is the maximum average biomass of species within environmental limit.

<!-- b000087 | prose | pages [6] -->
In arid and semi-arid regions, plants have relatively unique growth laws, and the extreme climate conditions and water resource constraints have a serious impact on the normal growth of plants [2][3]. Therefore, it is necessary to modify formula (1) according to the environmental characteristics of arid regions. ⚫ Natural growth rate against drought conditions According to the research on the growth of plants in arid regions [4], the inherent growth rate of plants is related to the characteristics of themselves and soil water content of the local land, which can be expressed as follows:

<!-- b000088 | prose | pages [6] -->
(2)

<!-- b000089 | prose | pages [6, 7] -->
where is the inherent growth rate, is resource availability (soil water content), is the rate of resource uptake per unit biomass as a function of resource availability, represents the conversion efficiency of plants to convert absorbed water into biomass increment, and is the loss rate of plants per unit time, which is caused by the metabolism, natural death and the destruction from other creatures.

<!-- b000090 | furniture | pages [7] -->
Team # 2303950

<!-- b000091 | furniture | pages [7] -->
Page 7 of 25

<!-- b000093 | prose | pages [7] -->
In particular, here can be formulated as

<!-- b000094 | prose | pages [7] -->
(3)

<!-- b000095 | prose | pages [7] -->
where denotes to what extent water absorption rate changes with resource availability, controls the upper limit of water absorption rage, and controls the variation trend of the uptake curve.

<!-- b000096 | heading | pages [7] -->
⚫ The stochastic rainfall model

<!-- b000097 | prose | pages [7] -->
As is mentioned in Assumption 2, the raining in drought areas can be treated as an instantaneous impulse of water. Therefore, we need two variables to determine a specific rainfall. Specifically, denotes the relative time of the rainfall within a year, and denotes the total volume of the rain.

<!-- b000098 | prose | pages [7] -->
In literature [3], the author provides a model to predict the timing of the rain impulse in a year and the amount of rain in drought areas. At first, the timing of the rainfall is a random draw from the Beta Distribution with parameters and . It can be written as [5]

<!-- b000099 | prose | pages [7] -->
(4)

<!-- b000100 | prose | pages [7] -->
where is the Gamma Function, and is the probability density of the timing in a year.

<!-- b000101 | prose | pages [7] -->
The amount of rain is also treated as a random draw from the log-natural distribution, in which parameters and are respectively the mean and variance of the natural log of the amount of rainfall. Hence, can be obtained as

<!-- b000102 | prose | pages [7] -->
(5)

<!-- b000103 | prose | pages [7] -->
⚫ The law of water content changing in the soil According to Assumption 2, there is no additional water supply between two rains. Therefore, the water in the soil continues decreasing, mainly due to the absorption of plants and evaporation. In particular, as is mentioned in Assumption 3, water evaporation is directly proportional to the total water amount. Setting the scale factor as , we have

<!-- b000104 | prose | pages [7] -->
(6)

<!-- b000105 | prose | pages [7] -->
Meanwhile, we mark the instant of rainfall as . According to Assumption 2, the water stored in the soil changes instantaneously

<!-- b000106 | prose | pages [7, 8] -->
(7) ⚫ The law of plant life and the evolution of seed bank According to Assumption 4, summer-type annual plants have a regular period of flowering. In this process, plants complete flowering, mating and fruiting. In general, annual plants wither and die after the period of flowering, but their seeds will grow next year at a ratio (marked as ). At the same time, a certain proportion of the total biomass is converted into new seeds and added to the seed bank (marked as ). Assuming the conversion ratio from the total biomass into seeds as , we can infer the seed bank of species  changes as follows:

<!-- b000107 | furniture | pages [8] -->
Team # 2303950

<!-- b000108 | furniture | pages [8] -->
Page 8 of 25

<!-- b000110 | prose | pages [8] -->
(8)

<!-- b000111 | prose | pages [8] -->
To sum up, we obtain the evolution model of species in arid environments without competition with other species. Specifically, the evolution rules are as follows: (i) In the process of growth, the average biomass and soil water content follow the differential equations below

<!-- b000112 | prose | pages [8] -->
(9)

<!-- b000113 | prose | pages [8] -->
(ii) When the rain occurs in , soil water content will change instantaneously

<!-- b000114 | prose | pages [8] -->
(10)

<!-- b000115 | prose | pages [8] -->
(iii) After the period of flowering, plant population generates seed. So, the total biomass and the seed bank are described by the following equations

<!-- b000116 | prose | pages [8] -->
(11)

<!-- b000117 | prose | pages [8] -->
(iv) After the period of flowering, all summer-type annual plants will die. And in the spring of the next year, some seeds germinate and start to grow at a ratio , which means

<!-- b000118 | prose | pages [8] -->
(12)

<!-- b000119 | caption | pages [8] -->
Figure 3: One Species Changes in One Year and 30 Years

<!-- b000120 | furniture | pages [9] -->
Team # 2303950

<!-- b000121 | furniture | pages [9] -->
Page 9 of 25

<!-- b000122 | heading | pages [9] -->
4.2 The Competition Model of Multiple Species

<!-- b000123 | prose | pages [9] -->
As is mentioned earlier, we established the growth model of one species against irregular climate change. In this section, we take the competition among multiple species into account. We consider the competition between two species first. Based on Lotka-Volterra Model, we introduce the influence factor [6] to express the competition on the basis of formula (9)

<!-- b000124 | prose | pages [9] -->
(13)

<!-- b000125 | prose | pages [9] -->
where represent the competition between two populations. Considering that in arid environments, the main resource for competition is water, we define as follows:  indicates that the water resources consumed by unit biomass of plant  is times of that of plant , in which plant is located.

<!-- b000126 | prose | pages [9] -->
We deduce the values of and from the perspective of root growth [7]. Assuming that the average diameter of root extension of plant  is , we get the average radius as . Thus, the root coverage area is . If the root coverage between plant 1 and plant 2 overlaps, we can infer that there is competition for water resources between these two plants.

<!-- b000127 | caption | pages [9] -->
Figure 4: The Battlefield between Two Plants

<!-- b000128 | prose | pages [9] -->
First, normalize the water-utilizing capacity parameters , and obtain the relative water-utilizing capacity , which satisfy

<!-- b000129 | prose | pages [9] -->
(14)

<!-- b000130 | prose | pages [9] -->
According to the definition of , we can deduce that

<!-- b000131 | prose | pages [9, 10] -->
(15) where indicates the average overlapping area of plant 1 and other plants, indicates the average overlapping area of plant 2 and other plants, , which is the average root coverage of plant 1, , which is the average root coverage of plant 2.

<!-- b000132 | furniture | pages [10] -->
Team # 2303950

<!-- b000133 | furniture | pages [10] -->
Page 10 of 25

<!-- b000135 | prose | pages [10] -->
As for the root coverage and average overlapping area , we can estimate them based on the number and average biomass of plants in the experimental area.

<!-- b000136 | prose | pages [10] -->
According to Assumption 5, we can figure out the volume of the root system from the average biomass of plants by

<!-- b000137 | prose | pages [10] -->
(16)

<!-- b000138 | prose | pages [10] -->
where is a scale factor, and is the volume of the root system of a plant , which can be estimated from the growth data of plants. Specifically, we can collect the data of root length and plant biomass during the plant growth and thus determine the scale factor.

<!-- b000139 | prose | pages [10] -->
From the volume of the root system, we can further obtain the root coverage area by

<!-- b000140 | prose | pages [10] -->
(17)

<!-- b000141 | prose | pages [10] -->
As is mentioned in Assumption 7, we assume the number of plants (marked as ) remain constant in the process of growth (between germination and flowering). Thus, based on

<!-- b000142 | heading | pages [10] -->
Assumption 6, we estimate the average overlapping area of various plants by

<!-- b000143 | prose | pages [10] -->
(18)

<!-- b000144 | prose | pages [10] -->
It is worth noting that if the result of the average overlapping area is less than 0. We infer that there is no competition between this plant and other plants. Then, we sort out the differential equations model of two plant populations competing during the growth period in a year, which can be described as

<!-- b000145 | prose | pages [10, 11] -->
(19) The parameters in formula (19) can be determined by the following rules:

<!-- b000146 | furniture | pages [11] -->
Team # 2303950

<!-- b000147 | furniture | pages [11] -->
Page 11 of 25

<!-- b000149 | prose | pages [11] -->
(20)

<!-- b000150 | prose | pages [11] -->
Finally, we get the differential equations model of plant populations competing with each other in the growth period in a year, which can be described as

<!-- b000151 | prose | pages [11] -->
(21)

<!-- b000152 | prose | pages [11] -->
The parameters in formula (21) can be determined by the following rules:

<!-- b000153 | prose | pages [11] -->
(22)

<!-- b000154 | prose | pages [11] -->
Based on the differential equations above, the final model can be obtained by considering formula (10~12) comprehensively.

<!-- b000155 | caption | pages [11] -->
Figure 5: A Plant Community Changes in One Year and 30 Years

<!-- b000156 | furniture | pages [12] -->
Team # 2303950

<!-- b000157 | furniture | pages [12] -->
Page 12 of 25

<!-- b000158 | heading | pages [12] -->
4.3 The Facilitation Model of Shrub Plants to Herbaceous Plants

<!-- b000159 | prose | pages [12] -->
In Sec. 4.2, we established the interspecific competition model of plants during circles of drought from the perspective of root competition of water. This model applies to all plants. However, against drought stress, shrub plants play a unique role in facilitating the growth of herbaceous plants [8]. This facilitation is mainly reflected in the fact that shrub plants can improve the survival and growth of herbaceous plants. Considering that the introduction of shrub plants cannot boost the soil water content directly, we infer that shrub plants can improve the limiting factor of the water absorption rate (which is marked as ). According to formula (3), we see that is affected by and . Due to the reason that denotes to what extent water absorption rate changes with resource availability, it is an inherent attribute of a plant. We regard that would not change with the introduction of shrubs. Thus, we speculate that shrubs can affect by influencing . Based on the competition model in Sec. 4.2, we further modify the parameter to .

<!-- b000160 | prose | pages [12] -->
According to the research of Richards team [9] and Prieto team [10], we find that shrub roots can lift water from the deep soil onto the shallow soil. This process can improve the environment of shallow soil and facilitate other plants to absorb water. Considering the smaller , the higher the water absorption rate of plants, we infer that

<!-- b000161 | prose | pages [12] -->
(23)

<!-- b000162 | prose | pages [12] -->
where is a scale factor, which reflects the water-lift capacity of shrubs per unit biomass,

<!-- b000163 | prose | pages [12] -->
The analysis of formula (23) shows that when there are no shrubs around plant , is equal to . When shrubs exist, the more biomass of shrubs, the smaller is. Therefore, the water absorption rate will raise if there are shrubs around plant .

<!-- b000164 | prose | pages [12] -->
Meanwhile, according to the research of Butterfield team [11], the facilitating effect of shrubs on soil moisture will decrease with the increase of drought. Considering that soil water content is one of the criteria to measure the degree of drought, we further modify formula (23):

<!-- b000165 | prose | pages [12] -->
(24)

<!-- b000166 | prose | pages [12] -->
where is resource availability (soil water content). With the increase of the soil water content, decreases monotonically. Thus, increases, which means the plant absorbs water at a higher rate.

<!-- b000167 | prose | pages [12, 13] -->
Because the facilitation mechanism of shrubs on herbaceous plants is complex and uncertain, there is no relatively consistent research results at present [8]. Therefore, we establish the model above according to the analysis of specific situations. And we will give our own estimation of the parameters in the simulation.

<!-- b000168 | furniture | pages [13] -->
Team # 2303950

<!-- b000169 | furniture | pages [13] -->
Page 13 of 25

<!-- b000171 | heading | pages [13] -->
4.4 Reasonable Estimation of Essential Parameters

<!-- b000172 | prose | pages [13] -->
In this section, we make reasonable estimations of the parameters in the previous model.

<!-- b000173 | heading | pages [13] -->
⚫ Statistical parameters in the stochastic rainfall model

<!-- b000174 | prose | pages [13] -->
According to the stochastic rainfall model established in Sec. 4.1, the average amount of rain in a year can be obtained as . Since , we need determine the mean and variation .

<!-- b000175 | prose | pages [13] -->
We looked up the annual precipitation in areas of different degrees of drought. We find the average annual precipitation in severe drought areas is only 32.5mm [12], such as the southern edge of the Taklimakan Desert. The average annual precipitation in moderately arid areas is about 113.2mm [13], like the primitive desert in the middle of the Hexi Corridor in China. And this data is about 360mm for semi-arid areas [14], like the Sandi Cypress Nature Reserve in Wushen Banner, Inner Mongolia, China.

<!-- b000176 | prose | pages [13] -->
Considering that our experimental area is 10000 m2, the average annual precipitation mass is 325kg, 1132kg and 3600kg against the different drought degrees above. According to the rule in statistics, there is a probability of 95% that . We have

<!-- b000177 | prose | pages [13] -->
(25)

<!-- b000178 | prose | pages [13] -->
The equations about and above are overdetermined. According to normal equations, we obtain the optimal parameter values based on Least Square Method

<!-- b000179 | prose | pages [13] -->
(26)

<!-- b000180 | prose | pages [13] -->
where A is the coefficient matrix of in formula (25), B is .

<!-- b000181 | prose | pages [13] -->
Finally, we obtain that . ⚫ Scale factor between the volume of the root system and the biomass of plant In arid environments, plant roots cover a wider area as much as possible. According to the discussion on the topological structure of root system [13], an ideal model is binary branching.

<!-- b000182 | caption | pages [13] -->
Figure 6: Binary Branching Model of Plant Roots

<!-- b000183 | furniture | pages [14] -->
Team # 2303950

<!-- b000184 | furniture | pages [14] -->
Page 14 of 25

<!-- b000185 | prose | pages [14] -->
For further discussion, we introduce the concept of root and root connection length, shown in Figure 6. Reaumuria soongorica (RS) and Nitraria tangutorum (NT) are two common populations in desert areas. According to [12], the average root length in total of RS is 3185.5cm, with an average root connection length of 29.8cm. While the average root length in total of NT is 4802.5cm, and the average root connection length is 49.0cm.

<!-- b000186 | prose | pages [14] -->
By analyzing the characteristic of binary branching, we have

<!-- b000187 | prose | pages [14] -->
(27)

<!-- b000188 | prose | pages [14] -->
where is the root length in total, is the average length of a root and is a root coefficient, which reflects how many branches are there in the root system.

<!-- b000189 | prose | pages [14] -->
Next, we plug the average root length in total and the average root connection length into formula (27). We obtain

<!-- b000190 | prose | pages [14] -->
(28)

<!-- b000191 | prose | pages [14] -->
Then, we consider that plant roots will extend around in spherical shape in order to absorb water. So, we estimate the diameter of root system as follows:

<!-- b000192 | prose | pages [14] -->
(29)

<!-- b000193 | prose | pages [14] -->
We simplify the root system as half a sphere, so we can also obtain the volume of roots.

<!-- b000194 | prose | pages [14] -->
Taking the mass of a single plant of two populations into account, we determine and by formula (16). Since these two populations are representative in arid areas, we estimate the universal scale factor according to the average of the two values, which derives

<!-- b000195 | prose | pages [14] -->
(30)

<!-- b000196 | prose | pages [14] -->
Since is a scale factor between the volume of roots and the biomass of plant, it reflects a universal law. Therefore, we regard that this scale factors of different plants are approximately equal. In the simulation, we substitute the scale factor of different species by . ⚫ Estimation of other parameters Besides the above two parameters, we also need determine , and .

<!-- b000197 | prose | pages [14] -->
As is mentioned in the previous description (Sec. 4.1), represents the conversion efficiency of plants to convert absorbed water into biomass increment and denotes to what extent water absorption rate changes with resource availability. According to [4], the reasonable range of is , while the range of is . When considering different plant species, we take values within the above range to ensure the rationality of the final results.

<!-- b000198 | prose | pages [14] -->
According to the early analysis in Sec. 4.1, is the maximum average biomass of species  within environmental limit. It is obvious that should be unequal for different species. However, as for summer-type annual plants which are studied in our paper, is generally less than 0.5kg [7]. So, it is rational to set the value around .

<!-- b000199 | furniture | pages [15] -->
Team # 2303950

<!-- b000200 | furniture | pages [15] -->
Page 15 of 25

<!-- b000201 | heading | pages [15] -->
5 Model Computed and Results Analysis

<!-- b000202 | heading | pages [15] -->
5.1 Model Computed Algorithm

<!-- b000203 | prose | pages [15] -->
Considering the high accuracy and strong stability of the fourth order Runge-Kutta algorithm, we apply this method for computing the differential equations listed in formula (21). At first, we sort the differential equations into the form of , where . Then, we construct the following differential iteration scheme to compute the first order differential equations:

<!-- b000204 | prose | pages [15] -->
(31)

<!-- b000205 | prose | pages [15] -->
where is the time step of the computing process.

<!-- b000206 | prose | pages [15] -->
The details of computing are shown as follows:

<!-- b000207 | caption | pages [15] -->
Table 2: Illustration of the MATLAB Simulation

<!-- b000208 | prose | pages [15] -->
Input:

<!-- b000209 | prose | pages [15] -->
(1) The characteristics of various species, the initial condition of the community (2) The simulation time period

<!-- b000210 | heading | pages [15] -->
(3) The timing of rainfall based on the beta distribution model

<!-- b000211 | prose | pages [15] -->
(4) The amount of water of each rainfall based on the log-normal distribution model While:

<!-- b000212 | prose | pages [15] -->
(1) If: at the beginning of a year A specific proportion of the seed in seedbank will germinate End (2) Calculate the increase of the biomass of respective species and the total underground water storage at the moment using R-K method (3) If: the rainfall is encountered increase the water storage by the water amount End (4) If: the flowering period in the year has been over ⚫ convert of the biomass to the increase of the seed bank ⚫ all annual plants die End (5) record the evolution of the community End

<!-- b000213 | furniture | pages [16] -->
Team # 2303950

<!-- b000214 | furniture | pages [16] -->
Page 16 of 25

<!-- b000215 | heading | pages [16] -->
5.2 Evaluation of the Benefit for a Multi-Plants Community

<!-- b000216 | prose | pages [16] -->
For a community of plants, there are two aspects to evaluate its performance facing the irregular weather conditions. One is the weight of all plants, which should be as high as possible. Another is that extreme fluctuations should be avoided to ensure the stability of the ecosystem. To conclude, an ideal ecosystem is supposed to reach the balance between its scale and stability.

<!-- b000217 | prose | pages [16] -->
The scale of the community in the year can be modeled as the total weight of the plant species (marked as ), which can be written as：

<!-- b000218 | prose | pages [16] -->
(32)

<!-- b000219 | prose | pages [16] -->
where is the average biomass of plant  in the year, and is the total number of the plant species in this year. To simplify the analysis of the problem, we limit the time within a period of years.

<!-- b000220 | prose | pages [16] -->
Considering the total weight of plant of each year, we can calculate the average total weight in this period (marked as ), which is:

<!-- b000221 | prose | pages [16] -->
(33)

<!-- b000222 | prose | pages [16] -->
The yearly fluctuation of the total weight can be treated as the variance of the data (marked as ), which is expressed as:

<!-- b000223 | prose | pages [16] -->
(34)

<!-- b000224 | prose | pages [16] -->
If biodiversity actually brings benefits to the plant community, it can be reflected by higher scale or lower fluctuation. To evaluate the balance between these two aspects, we employ the method of TOPSIS. TOPSIS (Technique for Order Preference by Similarity to an ideal solution) is a commonly used method in multi-objective decision analysis. Hence, we employ this model to evaluate the performance of the evolution of a plant community. If the performance of the evaluation is better than the case where there is only one plant species, it means the plant community has benefited from the biodiversity. Therefore, we are able to determine how many species are required to benefit the community. The results are shown as follows:

<!-- b000225 | caption | pages [16] -->
Figure 7: Evaluation of the Community’s Scale and Stability Using TOPSIS

<!-- b000226 | furniture | pages [17] -->
Team # 2303950

<!-- b000227 | furniture | pages [17] -->
Page 17 of 25

<!-- b000228 | prose | pages [17] -->
Meanwhile, this model also helps reveal what will happen as the number of species grows. What we need to do is enlarge the species number as the input of the simulation program.

<!-- b000229 | prose | pages [17] -->
The more species there are in the region, the lower the total weight of plants and the smaller the fluctuation the community has to experience against irregular weather conditions. This phenomenon can be explained intuitively by the differential equation model given in formula (21). As the number of species grows, the growth of the plant community will be subjected to more friction due to the more intense competition for the limited water resources. In this community of severe competition, any type of species is inhibited to grow to an extreme large scale within a short time. Therefore, the relative proportion of different species can be maintained, which results in higher stability of the plant community.

<!-- b000230 | prose | pages [17] -->
The benefit evaluation index deduced with TOPSIS (Figure 7) shows that when the number of species are more than eight, the index will be larger than that of one species. Therefore, over eight types of species are required for the community to gain overall benefit with respect to both the scale and stability of the community.

<!-- b000231 | heading | pages [17] -->
5.3 The Effect of Different Types of Species in the Community

<!-- b000232 | prose | pages [17] -->
This section presents the impacts of different types of species on the evolution of the plant community. Based on the competition model in Sec.4.2, we find that the greater the difference in between different species in a plant community, the greater the total biomass, but the lower its stability. We further consider the contribution of shrub plants to other plants in the above environment according to the model in Sec.4.3. Specifically, we simulate two types of plant communities and compare their differences.

<!-- b000233 | prose | pages [17] -->
In the first case, there are three types of different herbages and one type of shrub. As is mentioned in Sec. 4.3, the shrub is able to facilitate the growth of herbages by improving their water absorption rate. Therefore, aside from the competition among species, the cooperation also exists. In the second case, the plant community is constituted by three types of herbages without the shrubs. In other words, there is only competition among species. These two plant communities are put in the same weather circumstances, and the simulation shows their evolution results are as follows:

<!-- b000234 | caption | pages [17] -->
Figure 8: The Effect of Shrubs on the Biomass of Plant Community

<!-- b000235 | furniture | pages [18] -->
Team # 2303950

<!-- b000236 | furniture | pages [18] -->
Page 18 of 25

<!-- b000237 | prose | pages [18] -->
According to the analysis of evolution data, the first community (Dotted line in Figure 8) shows a relatively lower average total weight and a much smaller variance than that of the second community (Solid line in Figure 8). This difference indicates that the addition of shrub leads to a relatively lower scale of the community, due to the root competition. However, the plant community has a much higher stability facing the irregular weather conditions. More importantly, as can be seen from the figure above, shrubs can reduce the competition between different herbages, which is conducive to the maintenance of biodiversity.

<!-- b000238 | heading | pages [18] -->
5.4 The Effect of Fluctuant Frequency of Drought

<!-- b000239 | prose | pages [18] -->
The drought weather conditions usually come in the form of less rainfall amount each time and lower raining frequency. In order to simulate the impact of various frequency and occurrence of droughts on the plant community, it is a good idea to accordingly alter the time distribution and water amount of each rainfall. When the drought occurs, the rainfall will have less probability to have the same frequency (There is even likely to be no rainfall in the whole year!). This requires a new random variable to control the raining times. Besides, the water amount of each rainfall will also be lower and suffer from more fluctuations, indicating a smaller and a higher . The rainfall against different circumstances is depicted as follows:

<!-- b000240 | prose | pages [18] -->
600 2000 1800 500 1600 Rainfall amount kg Rainfall amount kg 1400 400 1200 300 1000 800 200 600 400 100 200 0 0 0 2 4 6 8 10 0 2 4 6 8 10 Simulation Time year Simulation Time year

<!-- b000241 | caption | pages [18] -->
Figure 9: The Rainfall Distribution under Severe and Less Frequent Drought

<!-- b000242 | prose | pages [18] -->
In our simulations, we suppose that corresponds to the Poisson Distribution with the parameter . Meanwhile, the and are also changed to create more severe drought conditions. The simulation results are shown as follows:

<!-- b000243 | prose | pages [18] -->
Evolution of The Total Weight of Species in The Community Evolution of The Individual Biomass of Species in The Community 700 0.25 normal normal severe severe 600 0.2 Individual Biomass kg 500 Total Weight kg 0.15 400

<!-- b000244 | prose | pages [18] -->
300 0.1

<!-- b000245 | prose | pages [18] -->
200 0.05 100

<!-- b000246 | prose | pages [18, 19] -->
0 0 20 25 30 35 40 45 50 55 60 20 25 30 35 40 45 50 55 60 Simulation Time year Simulation Time year Against severe drought conditions, the overall water resource availability will be furthermore limited. Therefore, it is understandable that the evolution of plant species will bring out not only lower scale, but also lower stability. Besides, our model shows that the scale and stability of the plant community follow the similar trend (mentioned in the Sec. 5.2) as the number of species grows, which is shown in the following table:

<!-- b000247 | caption | pages [18] -->
Figure 10: Evolution of The Plant Community under Normal and Severe Drought

<!-- b000248 | furniture | pages [19] -->
Team # 2303950

<!-- b000249 | furniture | pages [19] -->
Page 19 of 25

<!-- b000251 | caption | pages [19] -->
Table 3: The Community’s Scale and Stability Indexes of Less Frequent Drought

<!-- b000252 | prose | pages [19] -->
Type Number 4 6 8 10 12 24 Average 209.06 184.75 162.48 153.6 147.22 117.14 Variance 26346 15428 13606 12569 7277.6 3986.1

<!-- b000253 | heading | pages [19] -->
5.5 The Impact of Other Factors on Plant Community

<!-- b000254 | prose | pages [19] -->
⚫ The impact of different types of pollution Generally speaking, pollutants alter plants’ metabolism and make them vulnerable to disease or pest infestation. In this section, we study the impacts of two typical kinds of pollutants on the plant community, which are the photochemical smog and the acid rain. Their specific damages on the plants are presented as follows [15]:  Photochemical smog occurs due to chemical reactions among nitrous oxides from industry activities and VOCs. The resulting products are ground level ozone and peroxyacetyl nitrate. Plants exposed to these contaminants are weaker and have lower chances of survival. Hence, the impact of Photochemical smog can be modeled as in increase of loss rate of plants (marked as ).  Acid rain arises from the chemical reactions among Sulphur and nitrogen dioxide with other materials in the atmosphere. Direct exposure of acid rain makes it harder for plants to photosynthesize. Hence, the impact of Acid rain can be treated as a decrease of the conversion efficiency (marked as ).

<!-- b000255 | prose | pages [19] -->
To simulate the impact of pollution on the plant community, the loss rate of plants and the conversion efficiency should be modified accordingly. The simulation results of the growth of the plant community with contaminants are shown as follows:

<!-- b000256 | prose | pages [19] -->
Evolution of The Total Weight of The Community Exposed to Pollution Evolution of The Total Weight of The Community Exposed to Pollution Acid Rain(c is diminished by 10%) Photochemical Smog(m is increased by 10%) 600 600 normal normal polluted polluted 550 550 500 Total Weight kg Total Weight kg 500 450

<!-- b000257 | prose | pages [19] -->
400 450 350 400 300

<!-- b000258 | prose | pages [19, 20] -->
250 350 60 62 64 66 68 70 60 62 64 66 68 70 Simulation Time year Simulation Time year Compared with the non-polluted cases, the plant community exposed to pollution turn out to achieve lower scale. Besides, it is also notable that different types of contaminants influence the system’s stability in different ways. For the contaminants which increase the loss rate of biomass, such as photochemical smog, it doesn’t impose too much negative influences on the stability. However, this is not the same case when the plants are exposed to the acid rain, which reduces the conversion efficiency. When exposed to these pollutants, the plants community will bring out a much lower stability than that in the non-polluted cases. This phenomenon can be illustrated by the significance of water usage in drought regions. ⚫ The impact of habitat reduction Similarly, our model can also be utilized to explore the impact of habitat reduction on the growth of species. And the simulation results are shown as follows:

<!-- b000259 | caption | pages [19] -->
Figure 11: The Evolution of Community Exposed to Various Pollutants

<!-- b000260 | furniture | pages [20] -->
Team # 2303950

<!-- b000261 | furniture | pages [20] -->
Page 20 of 25

<!-- b000263 | caption | pages [20] -->
Figure 12: The Results of Habitat Reduction

<!-- b000264 | prose | pages [20] -->
It shows that the smaller the habitat is, the smaller the scale is. Since there are less space for the plant species to grow, there will be more intersections of the roots of different plants.

<!-- b000265 | heading | pages [20] -->
5.6 Measures Needed for Long-Term Viability

<!-- b000266 | prose | pages [20] -->
Based on the simulation results, we obtain a series of strategies to ensure the long-term viability of the plant communities. Our ideas are expressed from two aspects, the Preservation and Modification of the ecosystem. ⚫ Preservation The ecosystems of plant communities have survived in arid areas for millions of years, indicating its intrinsic robustness facing severe conditions. Therefore, actions should be taken to preserve the naturalness of the communities. Specific strategies are as follows: (1) Preserve the biodiversity of the plant community. From the simulation of our model in Sec. 4.2 and Sec. 4.3, we found that the competition and facilitation between multiple plant species both guarantee the stability of the system facing severe natural conditions. (2) Protect the water resources in drought regions. If water is over exploited, it will add to the shortage of water, reducing the scale and stability of plant communities. (3) Prevent and control the pollution. From our analysis in Sec. 5.5, pollutants, especially those like acid rain, have been proved to damage the scale and stability of plant community.

<!-- b000267 | furniture | pages [21] -->
Team # 2303950

<!-- b000268 | furniture | pages [21] -->
Page 21 of 25

<!-- b000269 | prose | pages [21] -->
(4) Maintain the habitat of plants. A large enough habitat can leave sufficient living space for the individuals, which helps avoid the severe competition between species. ⚫ Modifications Despite all these advantages of natural grass communities, they are still vulnerable to severe drought conditions. And modifications can be made to improve the viability of plant communities. Specific strategies are as follows: (1) Introduce new species. We found that species such as shrub can bring facilitation to other species and add more stability to the ecosystem, which is consistent with the literature.

<!-- b000270 | prose | pages [21] -->
Therefore, some suitable species can be introduced. (2) Build irrigation facilities. Some irrigation facilities, such as the Karez in Iran, can gather and preserve the water from the rainfall with less evaporation. So, increasing the soil water availability through artificial facilities is also worth consideration.

<!-- b000271 | heading | pages [21] -->
6 Sensitivity Analysis and Stability Analysis

<!-- b000272 | heading | pages [21] -->
6.1 Sensitivity Analysis

<!-- b000273 | prose | pages [21] -->
In Sec. 4, we established three models, which include many parameters. In Sec. 4.4, we make reasonable estimations of most parameters. However, it is still difficult to estimate some values through calculation, and the only way for us is to refer to literatures. In this Section, we conduct sensitivity analysis for the parameters got from literatures.

<!-- b000274 | prose | pages [21] -->
First of all, is the maximum average biomass of species , which reflects the restriction of environment on plant growth. Considering that what we study are mostly annual plants in arid environments, the maximum average biomass of different species should not differ a lot. Therefore, in the previous simulation, we assume that different species have the same .By adjusting the value of , we get the sensitivity analysis curve (taking the competition of three species as an example):

<!-- b000275 | prose | pages [21, 22] -->
Average Biomass of Species 1 Total Biomass Average Biomass of Species 3 Average Biomass of Species 2

<!-- b000276 | furniture | pages [22] -->
Team # 2303950

<!-- b000277 | furniture | pages [22] -->
Page 22 of 25

<!-- b000279 | caption | pages [22] -->
Figure 13: Effect of Different Values of

<!-- b000280 | prose | pages [22] -->
Then, we analyze the sensitivity of (which controls the variation trend of the uptake curve) and (which is the conversion ratio from plant biomass into seeds).

<!-- b000281 | caption | pages [22] -->
Figure 14: Effect of Different Values of

<!-- b000282 | caption | pages [22] -->
Figure 15: Effect of Different Values of

<!-- b000283 | prose | pages [22] -->
It can be seen that our models perform well in sensitivity analysis of various parameters. With the reproduction of plants from generation to generation, the fluctuation of parameter values has less impact on the results. This shows that our model has good long-term stability.

<!-- b000284 | heading | pages [22] -->
6.2 Stability Analysis

<!-- b000285 | heading | pages [22] -->
⚫ Influence of initial value on the results

<!-- b000286 | prose | pages [22] -->
We choose two initial values of the model ( which is the initial average biomass and which is the initial number). We perturb the two values randomly, with a disturbance variable follows uniform distribution.

<!-- b000287 | prose | pages [22] -->
The mean of disturbance variable is , and the variation is

<!-- b000288 | prose | pages [22, 23] -->
(35) Next, we observe the effect of disturbance on long-term results:

<!-- b000289 | furniture | pages [23] -->
Team # 2303950

<!-- b000290 | furniture | pages [23] -->
Page 23 of 25

<!-- b000292 | caption | pages [23] -->
Figure 16: Influence of Random Disturbance on Long-Term Stability of Model

<!-- b000293 | prose | pages [23] -->
In the figure above, the value of total biomass of plants is the maximum biomass of annual plants (before death). It can be seen that the long-term stability of the model is satisfying.

<!-- b000294 | heading | pages [23] -->
⚫ Relationship between the parameters and stability of the results

<!-- b000295 | prose | pages [23] -->
When we discuss the stability of the equilibrium point of differential equations, we often determine the possible equilibrium point by calculating the partial derivative. Then, we study the characteristic equation of the coefficient matrix and analyze the phase trajectory. And finally, we determine the conditions for the equation to be stable at a reasonable equilibrium point [6].

<!-- b000296 | prose | pages [23] -->
Based on the competition model established in Sec. 4.2, we consider the competition between two species. And now we just consider the growth within a year, that is, we ignore the process of flowering, fruiting and death. According to formula (19, 20), we can obtain the possible equilibrium point of the two species:

<!-- b000297 | prose | pages [23] -->
(36)

<!-- b000298 | prose | pages [23] -->
If the average biomass of two species are expected to meet at , we can obtain the requirements of the parameter values by the method above:

<!-- b000299 | prose | pages [23] -->
(37)

<!-- b000300 | prose | pages [23] -->
According to the definition and formula (18), the average root coverage is significantly larger than the average overlapping area in general. At the same time, for the drought-tolerant annual plants, there is no distinct different in their relative water absorption capacity , which can be described as Therefore, formula (37) is reasonable and easy to meet in our model.

<!-- b000301 | furniture | pages [24] -->
Team # 2303950

<!-- b000302 | furniture | pages [24] -->
Page 24 of 25

<!-- b000303 | heading | pages [24] -->
7 Strengths and Weaknesses

<!-- b000304 | heading | pages [24] -->
7.1 Strengths

<!-- b000305 | prose | pages [24] -->
⚫ With full considerations on the complexity of the evolution of annual plant species, our model takes the form of differential equations on the basis of the Logistic Model.

<!-- b000306 | prose | pages [24] -->
Meanwhile, the instantaneous jumps of the plant communities due to the reproduction and death of the plants are also included. Theoretically, our model is able to predict the state of community at any given time. ⚫ We consider the impact of water availability on the plant communities in our model using the relationship between the natural growth rate and the soil water content. So, our model is able to simulate the evolution of plant communities against various drought conditions. ⚫ The facilitation and competition between different species are modeled based on the previous study of Botany and Lotka-Volterra Model. Therefore, our model is able to simulate the evolution of various communities in which the interactions between species are different. ⚫ Using fourth order Runge-Kutta algorithm to calculate the numerical solutions of the differential equations, our model features computational accuracy and strong stability. ⚫ TOPSIS is employed to evaluate the evolutions of different plant communities. By virtue of both simplicity and comprehensibility, this method efficiently measures the overall performance of a specific plant community with respect to both the scale and the stability.

<!-- b000307 | heading | pages [24] -->
7.2 Weaknesses

<!-- b000308 | prose | pages [24] -->
⚫ In our model, soil water only comes from rainfall, and decreases only due to the evaporation and consumptions of species. Whereas the actual development of groundwater is much more complicated than that, as the factors such as underground rivers are not negligible. ⚫ Various types of droughts are defined with different frequencies and precipitations of rainfall. However, drought varies in many other aspects, such as the local temperature, wind circulation, and so forth. Therefore, more dimensions should be included to better describe the drought. ⚫ Although the multiple parameters in our model ensure the flexibility of the model, some of which are difficult to calculate precisely, so we give a proper estimation based on our references. However, we have rigorous derivation and analysis of the key parameters in the model.

<!-- b000309 | furniture | pages [25] -->
Team # 2303950

<!-- b000310 | furniture | pages [25] -->
Page 25 of 25

<!-- b000311 | heading | pages [25] -->
References

<!-- b000312 | references | pages [25] -->
[1] Floristic composition, distribution, and resource types of desert annual plants in Xinjiang

<!-- b000313 | references | pages [25] -->
DU Jiaqian [J]. Arid Zone Research,2022,39(01): 185-209.

<!-- b000314 | references | pages [25] -->
[2] Leopold, A. C. (1964). Plant growth and development. Plant growth and development.

<!-- b000315 | references | pages [25] -->
[3] Seleiman, M. F., Al-Suhaibani, N., Ali, N., Akmal, M., Alotaibi, M., Refay, Y., ... &

<!-- b000316 | references | pages [25] -->
Battaglia, M. L. (2021). Drought stress impacts on plants and different approaches to

<!-- b000317 | references | pages [25] -->
alleviate its adverse effects. Plants, 10(2), 259.

<!-- b000318 | references | pages [25] -->
[4] Chesson, P., Gebauer, R. L., Schwinning, S., Huntly, N., Wiegand, K., Ernest, M. S., ... &

<!-- b000319 | references | pages [25] -->
Weltzin, J. F. (2004). Resource pulses, species interactions, and diversity maintenance in

<!-- b000320 | references | pages [25] -->
arid and semi-arid environments. Oecologia, 141, 236-253.

<!-- b000321 | references | pages [25] -->
[5] Johnson NL, Kotz S, Balakrishnan N (1995) Continuous univariate distributions, vol 2,

<!-- b000322 | references | pages [25] -->
2nd edn. Wiley, New York

<!-- b000323 | references | pages [25] -->
[6] JIANG Qi-yuan (2011). Mathmatical model. Higher Education Press.

<!-- b000324 | references | pages [25] -->
[7] Fan, L., & Zizhen, L. (2003). Interspecific competition model and application of plants in

<!-- b000325 | references | pages [25] -->
sandy area. Acta Botanica Boreali-occidentalia Sinica, 23(1), 138-140.

<!-- b000326 | references | pages [25] -->
[8] LUO, G. S. C. T. X., & Zhang, E. L. L. (2022). Advances in the study of shrub facilitation

<!-- b000327 | references | pages [25] -->
on herbs in arid and semi-arid regions. Chinese Journal of Plant Ecology, 46(11):1321-

<!-- b000328 | references | pages [25] -->
1333.

<!-- b000329 | references | pages [25] -->
[9] Richards JH, Caldwell MM (1987). Hydraulic lift: substantial nocturnal water transport

<!-- b000330 | references | pages [25] -->
between soil layers by Artemisia tridentata roots. Oecologia, 73, 486-489.

<!-- b000331 | references | pages [25] -->
[10] Prieto I, Padilla FM, Armas C, Pugnaire FI (2011). The role of hydraulic lift on seedling

<!-- b000332 | references | pages [25] -->
establishment under a nurse plant species in a semi-arid environment. Perspectives in Plant

<!-- b000333 | references | pages [25] -->
Ecology Evolution and Systematics, 13, 181-187.

<!-- b000334 | references | pages [25] -->
[11] Butterfield BJ, Bradford JB, Armas C, Prieto I, Pugnaire FI (2016). Does the stress-

<!-- b000335 | references | pages [25] -->
gradient hypothesis hold water? Disentangling spatial and temporal variation in plant

<!-- b000336 | references | pages [25] -->
effects on soil moisture in dryland systems. Functional Ecology, 30, 10-19.

<!-- b000337 | references | pages [25] -->
[12] GUO, J. H., ZENG, F. J., LI, C. J., & Zhang, B. (2014). Root architecture and ecological

<!-- b000338 | references | pages [25] -->
adaptation strategies in three shelterbelt plant species in the southern Taklimakan

<!-- b000339 | references | pages [25] -->
Desert. Chinese Journal of Plant Ecology, 38(1), 36.

<!-- b000340 | references | pages [25] -->
[13] Li-shan, S. H. A. N., Yi, L. I., Wei, R. E. N., Shi-ping, S. U., Qiu-lian, D. O. N. G., &

<!-- b000341 | references | pages [25] -->
Dong-mei, G. E. N. G. (2013). Root architecture of two desert plants in central Hexi

<!-- b000342 | references | pages [25] -->
Corridor of Northwest China. Yingyong Shengtai Xuebao, 24(1).

<!-- b000343 | references | pages [25] -->
[14] He Weiming. Distribution Characteristic of Root Area of Sabina Vulgaris under Different

<!-- b000344 | references | pages [25] -->
Habitats. Scientia Silvae Sinicae, 2000, 36(5): 17-21.

<!-- b000345 | references | pages [25] -->
[15] "Greentumble."[online].Available: https://greentumble.com/effect-of-pollution-on-plants/
