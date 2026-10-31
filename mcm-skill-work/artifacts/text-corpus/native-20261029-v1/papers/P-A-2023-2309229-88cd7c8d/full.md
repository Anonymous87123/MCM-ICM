# P-A-2023-2309229-88cd7c8d

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2023

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
A

<!-- b000006 | title | pages [1] -->
2309229

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
The Warriors against Drought: Plant Communities

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
As the severe drought increases since the global warming, many plant communities die out for lack of water, while others can recover after drought. To explore this phenomenon, we develop GIID model to describe the response of communities to drought and analyse whether species diversity can help communities withstand drought.

<!-- b000011 | prose | pages [1] -->
Before all the models are established, we select ﬁve typical plant species and classiﬁy them into three categories, according to their inherent growth rate and optimum soil moisture. In addition, we estimate the parameters used in our models.

<!-- b000012 | prose | pages [1] -->
For Task 1: To simulate plant growth and interspeciﬁc competition, we ﬁrst developed the Lotka-Volterra competition model. Then, considering optimum soil moisture of each species, we set the environmental capacity of them as a function of soil moisture. Finally, we modeled the soil moisture variation to describe the interaction between plants and the en- vironment. We consider the water absorption by plants, irregular rainfall, and other factors. We summarize these analysis and devise our GIID model. Then, we verify the correctness of model. The results are shown in Figure 7.

<!-- b000013 | prose | pages [1] -->
For Task 2: First, we do the qualitative analysis and ﬁnd that the Five Species Community is more stable in drought. To quantify how the community beneﬁts from the species diversity, we calculate total biomass, coefﬁcient of variation of total biomass, and S-W index to evaluate

<!-- b000014 | heading | pages [1] -->
the vigor, stability, and evenness of the ecosystem respectively. The experimental results

<!-- b000015 | prose | pages [1] -->
show that as the number of species increases, the total biomass of the community increases and then decreases, while the stability and evenness keep increasing. Besides, two species are required for the community to beneﬁt. The results are shown in Figure 10 to 13.

<!-- b000016 | prose | pages [1] -->
For Task 3: To explore the effect of species type, we choose three typical species com- binations and each combination is simulated separately. We ﬁnd that combinations with moderate differences in optimum soil moisture increase the total biomass and stability of the community. And if the differences in optimum soil moisture of species are too small or too large, the community would not beneﬁt.

<!-- b000017 | prose | pages [1] -->
For task 4: We adjust the magnitude and frequency of droughts, and the experiment

<!-- b000018 | heading | pages [1] -->
results show that: when droughts become stronger and more frequent, the complementary

<!-- b000019 | prose | pages [1] -->
effect among species also becomes stronger. And the biomass of the community increases as the number of species increases. When droughts are less frequent, the competition among species is stronger, and the increase in the number of species lead to decrease in total biomass. The increase in the number of species always enhances community stability.

<!-- b000020 | prose | pages [1] -->
For Tasks 5 and 6: We attributed the effects of habitat loss and environmental pollu- tion to the decrease in environmental capacity. So we set up a step function to simulate this process. We ﬁnd that habitat loss and environmental pollution will lead to decrease in total community biomass, while multi species community will still have high stability in this pro- cess. Next, we illustrate the measures to ensure the long-term viability of the community. We also describe the impact of the community on the environment based on above ﬁndings.

<!-- b000021 | prose | pages [1] -->
Finally, we change the plant competition intensity, water absorption rate and climate pat- terns in order to perform sensitivity analysis on these parameters. We ﬁnd that our model is sensitive to all of them. We also analyze the strengths and weaknesses of the model and discuss how to improve it.

<!-- b000022 | keywords | pages [1] -->
Keywords: Lotka-Volterra Model, Biodiversity, Irregular Drought, Complementary Effect

<!-- b000023 | furniture | pages [2] -->
Team # 2309229

<!-- b000024 | furniture | pages [2] -->
Page 2 of 25

<!-- b000025 | heading | pages [2] -->
Contents

<!-- b000026 | contents | pages [2] -->
1

<!-- b000027 | heading | pages [2] -->
Introduction

<!-- b000028 | prose | pages [2] -->
3 Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 3 Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 3 Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 4 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4

<!-- b000029 | prose | pages [2] -->
2

<!-- b000030 | heading | pages [2] -->
Model Preparation

<!-- b000031 | prose | pages [2] -->
4

<!-- b000032 | prose | pages [2] -->
4 Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 5 Classiﬁcation of Plants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 6 Data Collection and Parameter Estimation . . . . . . . . . . . . . . . . . . . . . . 2.4

<!-- b000033 | prose | pages [2] -->
3

<!-- b000034 | heading | pages [2] -->
Task1 : The GIID Model

<!-- b000035 | prose | pages [2] -->
6

<!-- b000036 | prose | pages [2] -->
7 The Growth and Compete of Plants . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 8 The Interaction between Plants and Water . . . . . . . . . . . . . . . . . . . . . . 3.2 9 Relationship Between Water and Environmental Capacity . . . . . . . . 3.2.1 9 Variation of Soil Moisture . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.2 9 The Simulation of Irregular Weather . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 10 Model Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 3.4.1 Single Species Community 10 . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | prose | pages [2] -->
11 . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4.2 Five Species Community

<!-- b000038 | prose | pages [2] -->
4 Task 2 and 3 : Effect of Species Diversity

<!-- b000039 | prose | pages [2] -->
11

<!-- b000040 | prose | pages [2] -->
12 Task 2 : Effect of the Number of Species . . . . . . . . . . . . . . . . . . . . . . . 4.1 12 Qualitative Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.2 Quantitative Analysis 13 Model Implementation and Validation . . . . . . . . . . . . . . . . . . . . 4.1.3 4.2 Task 3 : Effect of the Type of Species 14 . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | prose | pages [2] -->
16 Three Representative Species Combinations 4.2.1 . . . . . . . . . . . . . . . .

<!-- b000042 | prose | pages [2] -->
16 Our Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 17

<!-- b000043 | prose | pages [2] -->
Task 4,5 and 6 : Impacts of Environmental Change on Species 5 18 Task 4 : Changes in the Magnitude and Frequency of Drought . . . . . . . . . . 5.1 18 Task 5 : Impacts from Habitat Reduction and Environmental Pollution . . . . . 5.2 20 Task 6 : Further Discussion on Community Viability . . . . . . . . . . . . . . . . 5.3 21 Ensuring Community Viability . . . . . . . . . . . . . . . . . . . . . . . . 5.3.1 21 The Impact of Communities on the Larger Environment 5.3.2

<!-- b000044 | prose | pages [2] -->
6

<!-- b000045 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000046 | prose | pages [2] -->
Plant Water Absorption Rate β

<!-- b000047 | prose | pages [2] -->
. . . . . . . . .

<!-- b000048 | prose | pages [2] -->
22

<!-- b000049 | prose | pages [2] -->
22 . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 22 Plant Competition Intensity α . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 23 Climate Conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3

<!-- b000050 | prose | pages [2] -->
7

<!-- b000051 | heading | pages [2] -->
Model Evaluation

<!-- b000052 | prose | pages [2] -->
23

<!-- b000053 | prose | pages [2] -->
24 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 24 Weaknesses and Possible Improvements . . . . . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000054 | heading | pages [2] -->
References

<!-- b000055 | references | pages [2] -->
25

<!-- b000056 | references | pages [2] -->
25

<!-- b000057 | furniture | pages [3] -->
Team # 2309229

<!-- b000058 | furniture | pages [3] -->
Page 3 of 25

<!-- b000059 | references | pages [3] -->
1

<!-- b000060 | heading | pages [3] -->
Introduction

<!-- b000061 | prose | pages [3] -->
1.1 Problem Background

<!-- b000062 | prose | pages [3] -->
In recent years, the frequency of extreme weather events has increased dramatically around the world because of the global warming. Drought is one of the extreme weather events that will have a huge impact on our lives. The image shown below is collected from the U.S. drought monitoring website Drought. gov. It reﬂects the drought conditions in the U.S. be- tween 8 Feb. 2023 and 14 Feb. 2023.

<!-- b000063 | caption | pages [3] -->
Figure 1: Distribution of drought in the United States

<!-- b000064 | prose | pages [3] -->
https://www.drought.gov/current-conditions Source :

<!-- b000065 | prose | pages [3] -->
As we can see from the graph, 34.55% of U.S. territory is exposed to drought, which affects 252.9 million acres of crops and 74.3 million people. During the extreme droughts, we can easily discover that different plant communities behave differently. Plants in grassland and farmland are almost dead, while multi-species communities are less affected and thrive after drought. Based on the above analysis, it is essential and urgent to study how plants respond to drought and how the diversity of species in a plant community helps the plants withstand drought.

<!-- b000066 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000067 | prose | pages [3] -->
• According to the requirements, we should ﬁrstly develop a mathematical model to pre- dict how a plant community changes over time as it is exposed to various irregular weather cycles. And we are required to consider the interaction between different plant species during the cycles of drought.

<!-- b000068 | prose | pages [3] -->
• Secondly, we should extend our model to a long-term time and a larger environment.

<!-- b000069 | prose | pages [3] -->
• Thirdly, we need to do a further discussion on the relationships between the number of plant species and the beneﬁts of the plant community gets, and to explore what happens when the number of species increases. Besides, we should pay attention to the impact of the type of species on the results we obtained previously.

<!-- b000070 | prose | pages [3] -->
• We are also required to study whether the number of species will have the same effect on the total plant population under the drought with higher or lower frequency and wider variation. Then we should take other factors like pollution and habitat reduction, etc. into account.

<!-- b000071 | prose | pages [3] -->
• Finally, based on all results above, we should ﬁgure out what need to be done to ensure the viability of the community and what the impacts of the plant community on the larger environment are.

<!-- b000072 | furniture | pages [4] -->
Team # 2309229

<!-- b000073 | furniture | pages [4] -->
Page 4 of 25

<!-- b000074 | prose | pages [4] -->
1.3 Literature Review

<!-- b000075 | prose | pages [4] -->
In order to study the plant communities in drought, we need to know the existing meth- ods to simulate plant communities and the corresponding ecological principals. According to the literature [1, 2, 3, 4], for the simulation, there are mainly three methods and for the principles, there are mainly two principles we need to use. As the following ﬁgure shows:

<!-- b000076 | caption | pages [4] -->
Figure 2: Literature Review

<!-- b000077 | prose | pages [4] -->
1.4 Our Work

<!-- b000078 | prose | pages [4] -->
The problem requires us to explore interactions between plants and enviroments, and measure the effects of species diversity. We mainly carry out the following work.

<!-- b000079 | prose | pages [4] -->
• Based on the analysis of several factors such as plant growth, interspeciﬁc competition, and the competition for water resources, a GIID model was developed. • Explore the effects of number of species and type of species • Explore the effects of other factors such as changes in drought frequency, habitat reduc- tion, and environmental pollution. In order to avoid complex textual descriptions, we use ﬂowcharts to show our work, which is shown in Figure 3.

<!-- b000080 | prose | pages [4] -->
2

<!-- b000081 | heading | pages [4] -->
Model Preparation

<!-- b000082 | prose | pages [4] -->
2.1

<!-- b000083 | heading | pages [4] -->
Assumptions and Justiﬁcations

<!-- b000084 | prose | pages [4] -->
To simplify the given problems, we make the following basic assumptions:

<!-- b000085 | prose | pages [4] -->
Assumption 1: The water absorption rate of each plant is proportional to its biomass.

<!-- b000086 | prose | pages [4] -->
Justiﬁcation: According to literature[7], When intense competition between plants occurs, each resource obtained by a plant is proportional to its biomass.

<!-- b000087 | prose | pages [4] -->
Assumption 2: The main factor affecting plant growth is the soil moisture. And there’s

<!-- b000088 | prose | pages [4] -->
different optimum soil moisture for different plants to grow.

<!-- b000089 | furniture | pages [5] -->
Team # 2309229

<!-- b000090 | furniture | pages [5] -->
Page 5 of 25

<!-- b000091 | caption | pages [5] -->
Figure 3: Our Work

<!-- b000092 | prose | pages [5] -->
Justiﬁcation: The factors affecting plant growth such as temperature, mois- ture, and sunshine are coupled in the real world. However, we just focus on the growth of plant community under extreme drought. Therefore, to sim- plify our models, we ignore other factors, and only take the soil moisture into consideration. When a plant grows under moderate soil moisture, it will grow fast, but it can not grow when it is lack of water or ﬂooded. So there’s a optimum soil moisture.

<!-- b000093 | heading | pages [5] -->
Assumption 3: Under the appropriate conditions, all plants share a common environmen-

<!-- b000094 | prose | pages [5] -->
tal capacity. Justiﬁcation: Most of plants are producers and obtain energy in the same way (all from photosynthesis). Under the appropriate conditions, they all have the opportunity to absorb all solar energy in the habitat. So they can reach the same maximum biomass, which means they share a same environmental capacity.

<!-- b000095 | prose | pages [5] -->
Assumption 4: During our study, the effects of accidental events such as plant invasion

<!-- b000096 | prose | pages [5] -->
and sudden changes in climate patterns are not considered. Justiﬁcation: Although the plants grow in a natural environment, to simplify our model, we assume that the plant community is in a relatively closed en- vironment. So there is no invasive species and no large, rapid changes in climate patterns.

<!-- b000097 | prose | pages [5] -->
Assumption 5: In plant communities, the only source of water is precipitation.

<!-- b000098 | prose | pages [5] -->
Justiﬁcation: There may be various ways for communities to get water, such as dew, fog and precipitation. Since dew and fog carry little water, we ignore their effects, and only consider the precipitation.

<!-- b000099 | prose | pages [5] -->
2.2

<!-- b000100 | heading | pages [5] -->
Notations

<!-- b000101 | prose | pages [5] -->
The key notations are shown in Table 1.

<!-- b000102 | furniture | pages [6] -->
Team # 2309229

<!-- b000103 | furniture | pages [6] -->
Page 6 of 25

<!-- b000104 | caption | pages [6] -->
Table 1: Notation

<!-- b000105 | heading | pages [6] -->
Symbol

<!-- b000106 | prose | pages [6] -->
Unit

<!-- b000107 | prose | pages [6] -->
day−1

<!-- b000108 | prose | pages [6] -->
Description

<!-- b000109 | prose | pages [6] -->
the inherent growth rate of the i-th plant ri xi kg the biomass of the i-th plant the environmental capacity of the i-th plant Envi kg − W − the soil moisture the optimum soil moisture of the i-th plant bestWi − α − β

<!-- b000110 | prose | pages [6] -->
2.3 Classiﬁcation of Plants

<!-- b000111 | prose | pages [6] -->
the intensity of competition the intensity of water absorption

<!-- b000112 | prose | pages [6] -->
We are required to study the relationship between species diversity in plant communi- ties and the response of plant communities to drought, so we must include several different plants in our models. However, it is difﬁcult to solve models for changes of multiple plants population over time because these models consist of several coupled differential equations and a bunch of parameters. To balance the computational efﬁciency and the accuracy of our models, we classify plants into three categories based on their different strategies for coping with drought, and selected one or two plants in each category as representatives.

<!-- b000113 | prose | pages [6] -->
Based on the study by Gao xiaoyan [4], we classiﬁed plants into three categories as fol- lows:

<!-- b000114 | prose | pages [6] -->
• Drought-Escape Plant: These plants have a high inherent growth rate, which gives them the ability to complete their life cycle before drought occurs. As a price for rapid growth, these plants are not good at coping with droughts. And once a drought ar- rives, their aboveground parts will wither rapidly to reduce water consumption. Typi- cal drought-escape plants are Hedera nepalensis and Ligustrum quihoui Carr.. • Drought-Avoiding Plant: These plants have a moderate inherent growth rate, however, they usually have the ability to withstand droughts. When soil moisture drops, these plants can reduce water loss by closing stomata or other ways [7], so that they can grow in droughts for a period of time. Typical drought-avoiding plants include Pinus massoniana Lamb and Populus alba. • Drought-Tolerant Plant: These plants have a quite low inherent growth rate. Some of them even grow only a few centimetres within a whole year. Such plants often have spe- cial structures in their bodies to store water, which allows them to absorb large amounts of water from few rainfalls in a year, so that they can maintain their growth. We choose Artemisia desertorum as the representative species.

<!-- b000115 | prose | pages [6] -->
Based on the above analysis, we found there’s a trade-off between plant growth rate and the ability to withstand drought. Then We can distinguish these plants by their inherent growth rate and optimum soil moisture. Using the inherent growth rate as the horizontal axis and the optimum soil moisture as the vertical axis, we can mark the positions of the three types of plants as shown in Figure 4.

<!-- b000116 | heading | pages [6] -->
Data Collection and Parameter Estimation

<!-- b000117 | prose | pages [6] -->
2.4

<!-- b000118 | prose | pages [6] -->
In the above, We classiﬁed plants species into three categories and selected ﬁve represen- tative plants. In order to simulate their growth at different soil moisture, we need to collect or estimate their inherent growth rate and the optimum soil moisture for them. Through the study of [5], we can get the relevant data, which are shown in the Table 2.

<!-- b000119 | furniture | pages [7] -->
Team # 2309229

<!-- b000120 | furniture | pages [7] -->
Page 7 of 25

<!-- b000121 | caption | pages [7] -->
Figure 4: Trade off between inherent growth rate and optimum humidity

<!-- b000122 | caption | pages [7] -->
Table 2: Inherent Growth Rate and Optimum Survival Humidity

<!-- b000123 | prose | pages [7] -->
Optimum Soil Moisture Species

<!-- b000124 | prose | pages [7] -->
Hedera nepalensis

<!-- b000125 | prose | pages [7] -->
Ligustrum quihoui Carr.

<!-- b000126 | prose | pages [7] -->
Pinus massoniana Lamb

<!-- b000127 | prose | pages [7] -->
Populus alba

<!-- b000128 | prose | pages [7] -->
Artemisia desertorum

<!-- b000129 | prose | pages [7] -->
Inherent Growth Rate

<!-- b000130 | prose | pages [7] -->
4.57 × 10−3day−1 69%

<!-- b000131 | prose | pages [7] -->
3.79 × 10−3day−1 62%

<!-- b000132 | prose | pages [7] -->
9.33 × 10−4day−1 45%

<!-- b000133 | prose | pages [7] -->
1.15 × 10−3day−1 53%

<!-- b000134 | prose | pages [7] -->
3.15 × 10−4day−1 25%

<!-- b000135 | prose | pages [7] -->
We can’t get the inherent growth rates directly from literature so we need to estimate them. In the following, we choose the Pinus massoniana Lamb as an example to clarify the estimation process and discuss the reasonableness of the results. literature [6] showed that this tree with a height of 2.5m and a trunk radius of 0.09m grew 7cm tall in one month without any change in the radius of the trunk. Considering that the density of wood is a constant, the inherent growth rate of the Pinus massoniana Lamb can be estimated using the following equation:

<!-- b000136 | prose | pages [7] -->
Increased Volume Increased Biomass 7 250 × 30 = 9.33 × 10−4day−1 Initial Volume × 30days = Initial Biomass × 30days = rpop.al. =

<!-- b000137 | prose | pages [7] -->
(1)

<!-- b000138 | prose | pages [7] -->
The inherent growth rate and the optimum soil moisture of these ﬁve plants in the Table 2 are consistent with the characteristics we elaborated in Section 3.2: drought-tolerant plants grow the slowest and drought-escape plants grow the fastest. And the higher the inherent growth rate, the lower the tolerance for the drought. This indicates that the parameters we estimated are reasonable.

<!-- b000139 | prose | pages [7] -->
3

<!-- b000140 | heading | pages [7] -->
Task1 : The GIID Model

<!-- b000141 | prose | pages [7] -->
In this section, we will establish the GIID Model, in order to describe the Growth of plants, the Interactions between plants and enviroment, and the inﬂuence of Irregular Drought.

<!-- b000142 | furniture | pages [8] -->
Team # 2309229

<!-- b000143 | furniture | pages [8] -->
Page 8 of 25

<!-- b000144 | prose | pages [8] -->
The Growth and Compete of Plants 3.1

<!-- b000145 | prose | pages [8] -->
Considering that the plant populations are often difﬁcult to be directly counted, it is better to choose the plant biomass to develop the plant growth equations.

<!-- b000146 | prose | pages [8] -->
Firstly, we consider the ideal situation, where the plant can grow endlessly in the case of unlimited space and other resources. Let ri denote the inherent growth rate of the i-th plant, then it’s biomass xi should satisfy the following equation:

<!-- b000147 | prose | pages [8] -->
dxi(t)

<!-- b000148 | prose | pages [8] -->
dt = xi(t)ri (2)

<!-- b000149 | prose | pages [8] -->
Due to the limited growth environment and according to the Assumption 3, all plants share a common environmental capacity Env , so the inherent growth rate will decrease lin- early, i.e., ri(t) = ri −xi/Env. Thus, we introduce the Logistic Growth Model then the plant growth equation should be rewritten as follows:

<!-- b000150 | prose | pages [8] -->
= xi(t)ri(1 −xi(t)

<!-- b000151 | prose | pages [8] -->
dxi(t)

<!-- b000152 | prose | pages [8] -->
dt

<!-- b000153 | prose | pages [8] -->
Env ) (3)

<!-- b000154 | prose | pages [8] -->
In addition, we should choose the initial biomass of plants. We assume that the initial biomass of all kinds of plants is the same, which is the x0:

<!-- b000155 | prose | pages [8] -->
xi(0) = x0 (4)

<!-- b000156 | prose | pages [8] -->
Finally, we obtain the following ﬁrst-order nonlinear differential equation :

<!-- b000157 | prose | pages [8] -->
(

<!-- b000158 | prose | pages [8] -->
= xi(t)ri(1 −xi(t)

<!-- b000159 | prose | pages [8] -->
dxi(t)

<!-- b000160 | prose | pages [8] -->
dt

<!-- b000161 | prose | pages [8] -->
xi(0) = x0 Env )

<!-- b000162 | prose | pages [8] -->
(5)

<!-- b000163 | prose | pages [8] -->
By solving the above differential equation, we can get the relationship between the plant biomass and time.

<!-- b000164 | prose | pages [8] -->
xi(t) = 1 + ( Env Env (6) xi(0) −1) exp(−rit)

<!-- b000165 | prose | pages [8] -->
When various species of plants live in the same area, the interaction between different species is inevitable. This is because there is an overlap in the ecological niches of multiple plants. They compete for natural resources like nutrients and sunlight. In this case, the growth and reproduction of one plant is then inﬂuenced by the others.

<!-- b000166 | prose | pages [8] -->
The Lotka-Volterra model is useful in dealing with the problem of competition between species. The basic idea is that one species (the ith plant) will be subject to resistance from all other species as it grows. Suppose that there are n species of plants growing on a piece of land, then the equation describes the biomass of the i-th of plant will be rewritten as:

<!-- b000167 | prose | pages [8] -->
dxi(t)

<!-- b000168 | prose | pages [8] -->
n X

<!-- b000169 | prose | pages [8] -->
= xi(t)ri(1 −xi(t) dt

<!-- b000170 | prose | pages [8] -->
cj

<!-- b000171 | prose | pages [8] -->
Env −α

<!-- b000172 | prose | pages [8] -->
xj(t)) (7)

<!-- b000173 | prose | pages [8] -->
ci

<!-- b000174 | prose | pages [8] -->
j=1,j̸=i

<!-- b000175 | prose | pages [8] -->
where α is the intensity of competition. And ci is the competitive ability of the i-th plant, which is a constant normalized to the range of [0, 1]. The cj/ci term in the equation represents the inﬂuence exerted by j-th plant on i-th plant. Therefore, The higher the competitive ability of the plant, the more likely it is to win in the competition.

<!-- b000176 | furniture | pages [9] -->
Team # 2309229

<!-- b000177 | furniture | pages [9] -->
Page 9 of 25

<!-- b000178 | prose | pages [9] -->
The Interaction between Plants and Water 3.2

<!-- b000179 | prose | pages [9] -->
Relationship Between Water and Environmental Capacity 3.2.1

<!-- b000180 | prose | pages [9] -->
Above, we designed the models to describe the plant growth under the environment con- straints, and the interactions between species. However, interactions between plants and the larger environment also have an important role on the competition. According to Assump- tion 2, under the drought, soil moisture is the most important factor determines whether a plant will live or die.

<!-- b000181 | prose | pages [9] -->
Assuming that W is the soil moisture, and bestWi represents the optimum soil moisture of the ith plant. Then We use Envi to denote the environmental capacity of the ith plant affected by soil moisture.

<!-- b000182 | prose | pages [9] -->
Envi has several important features:

<!-- b000183 | prose | pages [9] -->
• when W equals to bestWi, Envi will equal to Env; • when there is a huge difference between W and bestWi, which means |W −bestWi| → +∞, Envi will approaches to zero.

<!-- b000184 | prose | pages [9] -->
According to the central limit theorem, the environmental capacity of each plant should follow the Normal Distribution when the number of plant species tends to inﬁnity, so we can express the environmental capacity as follows:

<!-- b000185 | prose | pages [9] -->
Envi = Env × exp(−(W −bestWi)2

<!-- b000186 | prose | pages [9] -->
) (8)

<!-- b000187 | prose | pages [9] -->
MNWi

<!-- b000188 | prose | pages [9] -->
where MNWi is the constant controlling the decay rate, which is called moisture niche breadth of i-th plant in ecology. According to the study [5], the plant can hardly survive when the soil moisture drops to 20% of its optimum. So when W = 0.2bestWi, we assume that the biomass of the ith plant can only reach to 0.01Env:

<!-- b000189 | prose | pages [9] -->
0.01Env = Env × exp(−(0.8bestWi)2

<!-- b000190 | prose | pages [9] -->
) (9)

<!-- b000191 | prose | pages [9] -->
MNWi

<!-- b000192 | prose | pages [9] -->
By solving the above equation, we can get MNWi = 0.14bestWi

<!-- b000193 | prose | pages [9] -->
3.2.2 Variation of Soil Moisture

<!-- b000194 | prose | pages [9] -->
The soil moisture is not a constant during the growth of plants. Due to the combined effect of plant absorption, rainfall and evaporation, the soil moisture W will change with time. The variation of W is related to the water absorbed by each plant, and it is also inﬂuenced by the precipitation p(t) and the rate of evaporation. Therefore, we can use the following differential equation to describe the change of soil moisture:

<!-- b000195 | prose | pages [9] -->
X

<!-- b000196 | prose | pages [9] -->
dW(t)

<!-- b000197 | prose | pages [9] -->
xi(t)W(t) −γW(t) + p(t)

<!-- b000198 | prose | pages [9] -->
= −β dt

<!-- b000199 | prose | pages [9] -->
i

<!-- b000200 | prose | pages [9] -->
Where

<!-- b000201 | prose | pages [9] -->
(10)

<!-- b000202 | prose | pages [9] -->
• βW(t)xi(t) is the water absorption rate of the i-th plant.

<!-- b000203 | prose | pages [9] -->
According to the Assumption 1, the water absorbed by each plant is proportional to its biomass. In addition, related studies [7] showed that the water absorption rate of plant will increase when the soil moisture become higher. To simplify the model, we assume that the water absorption rate is also proportional to the soil moisture W(t). So the

<!-- b000204 | furniture | pages [10] -->
Team # 2309229

<!-- b000205 | furniture | pages [10] -->
Page 10 of 25

<!-- b000206 | prose | pages [10] -->
water absorption rate of the i-th plant can be written as βW(t)xi(t), and β is the water absorption intensity. • γW(t) is the evaporation rate.

<!-- b000207 | prose | pages [10] -->
literature [7] showed that the evaporation rate of soil in subtropical or temperate regions is proportional to the soil moisture. Therefore, the evaporation rate can be expressed as γW, and γ is a constant to describe the evaporation intensity. Based on the monitored data for the evaporation rate of grassland, we can estimate that γ = 0.12day−1

<!-- b000208 | prose | pages [10] -->
• p(t) represents the precipitation According to the Assumption 3, this is the only way to supply water for the plant com- munity. It can be obtained from weather records.

<!-- b000209 | prose | pages [10] -->
The Simulation of Irregular Weather 3.3

<!-- b000210 | prose | pages [10] -->
In order to predict how species change when the plant community is exposed to various irregular weather cycles and time of droughts when precipitation should be abundant, we need to simulate weather conditions. Therefore, we devise a function to describe periodic and non-periodic precipitation in plant communities as below:

<!-- b000211 | prose | pages [10] -->
sin( π

<!-- b000212 | prose | pages [10] -->
h

<!-- b000213 | prose | pages [10] -->
A0 + A1 ·

<!-- b000214 | prose | pages [10] -->
p(t) =

<!-- b000215 | prose | pages [10] -->
T t)

<!-- b000216 | prose | pages [10] -->
Where

<!-- b000217 | prose | pages [10] -->
+ A2 · δ(t −t0)

<!-- b000218 | prose | pages [10] -->
i

<!-- b000219 | prose | pages [10] -->
× 1 + I

<!-- b000220 | prose | pages [10] -->
(11) 2

<!-- b000221 | prose | pages [10] -->
• A0 is the minimum precipitation in the whole year, and also represents the precipita- tion in the dry season.

<!-- b000222 | prose | pages [10] -->
is a function with the period of T, which represents the periodic variation

<!-- b000223 | prose | pages [10] -->
sin( 2π • A1·

<!-- b000224 | prose | pages [10] -->
T t)

<!-- b000225 | prose | pages [10] -->
of the precipitation. To make the simulation more realistic, we set T = 1year. • A2 · δ(t −t0) represents the extreme weather occurring randomly. t0 is the time when extreme weather occurs. • (1+I)/2 represents the droughts occurring randomly. In one year, I can only be set to 0 or 1. When I takes 0, the precipitation of this year is half of the normal year. That means the occurrence of the severe droughts. And we assume that the probability of drought occurrence in each year is 30%.

<!-- b000226 | prose | pages [10] -->
3.4

<!-- b000227 | heading | pages [10] -->
Model Implementation

<!-- b000228 | prose | pages [10] -->
Based on the models described above for plant biomass growth, competition, and the interactions between plant and larger environment, we can ﬁnally obtain the universal dif- ferential equations of the model:

<!-- b000229 | prose | pages [10] -->
(

<!-- b000230 | prose | pages [10] -->
Env −α Pn

<!-- b000231 | prose | pages [10] -->
= xi(t)ri(1 −xi(t)

<!-- b000232 | prose | pages [10] -->
dxi(t)

<!-- b000233 | prose | pages [10] -->
dt

<!-- b000234 | prose | pages [10] -->
= −β P

<!-- b000235 | prose | pages [10] -->
dW(t) cj ci xj(t))

<!-- b000236 | prose | pages [10] -->
j=1,j̸=i

<!-- b000237 | prose | pages [10] -->
(12) i xi(t)W(t) −γW(t) + p(t)

<!-- b000238 | prose | pages [10] -->
dt

<!-- b000239 | prose | pages [10] -->
Because we cannot get the analytical solution of the equations directly, we need to use some numerical methods. However, This equation set is not suitable to use the 4th-5th order Runge-Kutta solver in Matlab, because the p(t) term is affected by some random factors. Considering this is only an 1-order system, we discretize it by converting the differential equation into the difference equation. Next, we solve it recursively with a time interval of ∆t = 5days. Consequently, the result is as follows:

<!-- b000240 | furniture | pages [11] -->
Team # 2309229

<!-- b000241 | furniture | pages [11] -->
Page 11 of 25

<!-- b000242 | prose | pages [11] -->
3.4.1 Single Species Community

<!-- b000243 | prose | pages [11] -->
To observe the changes in biomass of various plants over time under the periodic weather ﬂuctuations and non-periodic drought, we ﬁrst select the Pinus massoniana Lab from the drought-avoiding type and the Hedera nepalensis from the drought-escape type. Then we plant them individually without considering their competition with other plants. Finally, the results are as below:

<!-- b000244 | caption | pages [11] -->
Figure 5: Biomass of Pinus massoniana Lab

<!-- b000245 | caption | pages [11] -->
Figure 6: Biomass of Hedera nepalensis

<!-- b000246 | prose | pages [11] -->
With results in both ﬁgures, we can identify several remarkable phenomena:

<!-- b000247 | prose | pages [11] -->
• The biomass of both plants are inﬂuenced by the periodic weather change, resulting in ﬂuctuations. However, the ﬂuctuation of the P.massoniana.L is less compared to the H.nepalensis. This is mainly because the P.massoniana.L is a drought-avoiding plant, On the contrary, the H.nepalensis, as a which is less sensitive to the soil moisture. drought-escape plant, can grow only with high soil moisture. Therefore, when drought occurs, the H.nepalensis is more susceptible. • During the recovery process of the drought, the H.nepalensis recovers relatively quickly.

<!-- b000248 | prose | pages [11] -->
Because it has a large inherent growth rate, which allows it to recover its biomass quickly when the soil moisture is suitable for its growth.

<!-- b000249 | prose | pages [11] -->
As stated above, the changes of the biomass of these two plants with time differ obviously. Besides, they are consistent with the plants’ own optimum soil moisture and inherent growth rates. This indicates that our model is reasonable.

<!-- b000250 | prose | pages [11] -->
3.4.2 Five Species Community

<!-- b000251 | prose | pages [11] -->
To investigate how a multiple plant community copes with drought, we simulated the changes in biomass over time as ﬁve species interacted with each other.

<!-- b000252 | prose | pages [11] -->
From the Figure 7, we can draw the following conclusions:

<!-- b000253 | prose | pages [11] -->
• Under the conditions we set, the two drought-avoiding plants (H.nepalensis and L.quihoui.C) became the dominant species of the community. However, the drought-tolerant plants (A.desertorum) had little biomass and could grow only when drought appeared and the population of others declined. This is mainly due to the very low inherent growth rate of the drought-tolerant plants and their weak competitive ability. • The changes of biomass over time are similar for plants belonging to the same type, while there are large differences for plants belonging to different types.

<!-- b000254 | furniture | pages [12] -->
Team # 2309229

<!-- b000255 | furniture | pages [12] -->
Page 12 of 25

<!-- b000256 | caption | pages [12] -->
Figure 7: Changes in biomass of the ﬁve species over time

<!-- b000257 | prose | pages [12] -->
• During our simulation, this plant community underwent succession: at the beginning, the biomass of two drought-escape plants grew rapidly and prevailed; however, with the growth of the drought-avoiding plants(P.alba and P.massoniana.L), the biomass of the drought-escape plants gradually declined. This is because the drought-escape plants have weak competitive ability and high soil moisture requirements. • In a Five plants community, the total biomass is much less volatile than a Single plant community.

<!-- b000258 | prose | pages [12] -->
4 Task 2 and 3 : Effect of Species Diversity

<!-- b000259 | prose | pages [12] -->
Through the modeling of plant communities above, we have found that both periodical changes in climate and irregular droughts lead to changes of the biomass of plants. From the Figures 6 and 7 above, we can conclude that the variation of biomass is much narrower when ﬁve species coexist than when only one species survives. Therefore, it is important to explore the impact of species diversity.

<!-- b000260 | prose | pages [12] -->
4.1 Task 2 : Effect of the Number of Species

<!-- b000261 | prose | pages [12] -->
4.1.1 Qualitative Analysis

<!-- b000262 | prose | pages [12] -->
In order to qualitatively analyze the effect of the number of species, we simulated a Single Plant Community and a Five Plants Community. Then we observe the biomass of each species in these communities. To make our simulation more effectively in describing the long-term variation of the community, we set the simulation time to 50 years. And the results are as follows:

<!-- b000263 | prose | pages [12] -->
From the Figure 8 and 9, we can clearly see the impact of the climate cycles and the occur- rence of irregular droughts on different communities.

<!-- b000264 | prose | pages [12] -->
• Both periodic climate and irregular droughts bring ﬂuctuation to biomass: periodic cli- mate brings small ﬂuctuations to the biomass of various plants, while irregular droughts bring greater ﬂuctuations because it last longer.

<!-- b000265 | furniture | pages [13] -->
Team # 2309229

<!-- b000266 | caption | pages [13] -->
Figure 8: biomass of Single Plant Community

<!-- b000267 | furniture | pages [13] -->
Page 13 of 25

<!-- b000268 | caption | pages [13] -->
Figure 9: biomass of Five Plants Community

<!-- b000269 | prose | pages [13] -->
• The total biomass in Five Plants Community is lower than Single Plant Community, due to the competition among species for water and other resources. • The total biomass ﬂuctuated less when the ﬁve species coexisted, which indicates that the Five Plants Community has greater stability than Single Plant Community.

<!-- b000270 | prose | pages [13] -->
4.1.2 Quantitative Analysis

<!-- b000271 | prose | pages [13] -->
In order to To verify the community is actually beneﬁting from the coexisting of plants, we should quantitatively describe its characteristics. Inspired by a study of communities in northwest China, we will use several representative indicators which can be easily calculated to evaluate the community.

<!-- b000272 | prose | pages [13] -->
The most important indicator for a community is the total biomass, which reﬂects whether the plants in the community are growing prosperously. If the biomass of the i-th plant is denoted as xi, the total biomass TB in the community is the sum of the biomass of all plants. Since the total biomass of the community changes continuously over time, we take the mean of the total biomass as a measure of the community’s prosperity.

<!-- b000273 | prose | pages [13] -->
Z Tmax

<!-- b000274 | prose | pages [13] -->
1 TB = Tmax

<!-- b000275 | prose | pages [13] -->
n X

<!-- b000276 | prose | pages [13] -->
xi(t)dt (13)

<!-- b000277 | prose | pages [13] -->
0 0

<!-- b000278 | prose | pages [13] -->
i=1

<!-- b000279 | prose | pages [13] -->
where the Tmax in the equation is the total time needed to run the simulation program.

<!-- b000280 | prose | pages [13] -->
We know that the variation in total community biomass over time is related to the stability of the community. The smaller the variation of total biomass, the smaller the loss of biomass when the community is facing an irregular drought, which means that the community is more stable. In general, we can use the standard deviation of total biomass to measure its variation, but the standard deviation is inﬂuenced by the mean value and the dimension (the measurement unit) of the data. To eliminate this effect, we deﬁne a dimensionless indicator: the coefﬁcient of variation (CoV) of total biomass. We can divide the standard deviation of the total biomass by the mean value to calculate this indicator:

<!-- b000281 | prose | pages [13] -->
qR Tmax

<!-- b000282 | prose | pages [13] -->
CoV = std(TB)

<!-- b000283 | prose | pages [13] -->
= TB

<!-- b000284 | prose | pages [13] -->
(TB(t) −TB)2dt 0

<!-- b000285 | prose | pages [13] -->
(14) TB

<!-- b000286 | prose | pages [13] -->
In physics, we usually use "entropy" to measure the degree of disorder of a system.

<!-- b000287 | furniture | pages [14] -->
Team # 2309229

<!-- b000288 | furniture | pages [14] -->
Page 14 of 25

<!-- b000289 | prose | pages [14] -->
Shannon-Wiener index [9] is a measure of species evenness inspired by the concept of en-

<!-- b000290 | prose | pages [14] -->
R Tmax

<!-- b000291 | prose | pages [14] -->
tropy: in a community, the average number of each species is ¯xi =

<!-- b000292 | prose | pages [14] -->
xi(t)/Tmaxdt and the 0 total average biomass, already deﬁned above, is TB. Then the proportion of the i-th species is ¯xi/TB. The Shannon-Wiener index (S-W index) is deﬁned as:

<!-- b000293 | prose | pages [14] -->
n X

<!-- b000294 | prose | pages [14] -->
−¯xi

<!-- b000295 | prose | pages [14] -->
H =

<!-- b000296 | prose | pages [14] -->
i=1

<!-- b000297 | prose | pages [14] -->
TB log ¯xi

<!-- b000298 | prose | pages [14] -->
(15) TB

<!-- b000299 | prose | pages [14] -->
According to its expression, we can ﬁnd that the S-W index will reach its maximum when the proportion of each species gets same, i.e., ¯xi = ¯ TB/n. And the more uneven the distribu- tion of each species is, the smaller the S-W index is.

<!-- b000300 | prose | pages [14] -->
The S-W index measures the absolute evenness of the community, and since its maximum value is log n, Pielou index is deﬁned to measure the relative evenness of the communities :

<!-- b000301 | prose | pages [14] -->
J = H (16) log n

<!-- b000302 | prose | pages [14] -->
The Pielou index is a value between [0, 1] that measures the relationship between the cur- rent evenness of the community and the maximum evenness that the community can achieve.

<!-- b000303 | prose | pages [14] -->
4.1.3

<!-- b000304 | heading | pages [14] -->
Model Implementation and Validation

<!-- b000305 | prose | pages [14] -->
We collected data on ﬁve plant species in Section 2.4, two of which are drought-escape plants, two of which are drought-avoiding plants, and one of which is drought-tolerant plant. Now, we will change the number of plants in the community by planting one to ﬁve species into the community separately. Then we will simulate the changes of biomass of various plants over time, and use the results to calculate indicators deﬁned above. We will try all possible combinations of plants, for example, when the number of species n = 2, there are a total of C2

<!-- b000306 | prose | pages [14] -->
5 = 10 combinations.

<!-- b000307 | prose | pages [14] -->
We ﬁrst identiﬁed the relationship between the total biomass and the number of species, as the Figure 10 suggests. And then we observed the relationship between the community stability(measured by the CoV of biomass), as the Figure 11 shows. Each point in the ﬁgure represents a species combination. And straight lines connect the mean values of indicators for each species combinations with different numbers of species in the community.

<!-- b000308 | prose | pages [14] -->
From these graphs, we can notice two remarkable phenomena:

<!-- b000309 | prose | pages [14] -->
• With the increasing number of species, the mean value of total biomass increased and then decreased. When the number of species was two, the total biomass was the greatest. Further, when the number of species increased from one to two, the total biomass became higher. This is because of the complementary effect among certain species, whose mechanism will be discussed below. And when the number of species increased from two to ﬁve, the total biomass became lower. This is because there were so many species in the communitywhich strengthened the competition for water and other resources, and this competition narrowed the living space of each plant species. • The CoV of the total biomass tended to decrease as the number of species continued to increase. This indicates that the communities with more species have lower ﬂuctuations in the total biomass. That is, they are more stable and more resistant to drought.

<!-- b000310 | furniture | pages [15] -->
Team # 2309229

<!-- b000311 | caption | pages [15] -->
Figure 10: The relationship between total biomass

<!-- b000312 | prose | pages [15] -->
and number of species

<!-- b000313 | furniture | pages [15] -->
Page 15 of 25

<!-- b000314 | caption | pages [15] -->
Figure 11: The relationship between CoV of total

<!-- b000315 | prose | pages [15] -->
biomass and number of species

<!-- b000316 | prose | pages [15] -->
The following Figure 12 shows the relationship between the S-W index and the number of species. And the Figure 13 shows the relationship between the Pielou index and the number of species:

<!-- b000317 | caption | pages [15] -->
Figure 12: Relationship between S-W index and

<!-- b000318 | prose | pages [15] -->
number of species

<!-- b000319 | caption | pages [15] -->
Figure 13: Relationship between Pielou index and

<!-- b000320 | prose | pages [15] -->
number of species

<!-- b000321 | prose | pages [15] -->
From these ﬁgure, we can ﬁnd that the values of S-W index and Pielou index were in- creasing as the number of species increased. The Pielou index reached 0.87 when the number of species reached 5. This suggests that the distribution of species in the community was al- ready very close to the even distribution. Therefore, we conclude that the higher the number of species in the community, the better the balanced development of each species. This is because when the number of species is higher, the interspeciﬁc competition increases, which makes it difﬁcult for any one plant to have a biomass that far exceeds that of the others.

<!-- b000322 | prose | pages [15] -->
According to our conclusion, although a higher number of species may lead to a decrease in the total biomass of the community, the variation of total biomass will be reduced. Besides, the community’s ability to resist drought will increase. At the same time, the distribution of the species in the community will be more even, and each plant will have enough space to survive and develop. They are consistent with the results of related studies, so it reﬂects the reasonableness of our model. Compared with the case of Single plant community, the total biomass increased slightly when there were two plants, and the drought resistance increased signiﬁcantly, so that at least two different plants could make the community beneﬁt.

<!-- b000323 | furniture | pages [16] -->
Team # 2309229

<!-- b000324 | furniture | pages [16] -->
Page 16 of 25

<!-- b000325 | prose | pages [16] -->
4.2 Task 3 : Effect of the Type of Species

<!-- b000326 | prose | pages [16] -->
Above, we explored the relationship between number of species and total biomass, we also described the relationship between number of species and stability. However, it is also evident from Figure 10 and Figure 11 that the total biomass and CoV are signiﬁcantly differ- ent for different species combinations. For example, if there are two different species in the community, the lowest total biomass is 200kg and the highest total biomass is 400kg. Thus, the type of species can also have a large impact on our model. To analyze this effect, we chose three typical species combinations, each consisting of two different species, and we will simulate each species combination separately.

<!-- b000327 | prose | pages [16] -->
4.2.1 Three Representative Species Combinations

<!-- b000328 | prose | pages [16] -->
If two species in a community have the same inherent growth rate, tolerance to drought, and competitive ability, then the biomass of them will vary with the same pattern. It is the different attributes of the two species that lead to the differences in their biomass trends. With this in mind, we selected three representative species combinations: (a) H.nepalensis and L.quihoui.C, which all belong to the drought-escape plant and differ little in various at- tributes; (b) H.nepalensis and P.alba which respectively belong to drought-escape plant and drought-avoiding plant. And there is a moderate different in their optimum soil moisture. (c) H.nepalensis and A.desertorum, which belong to drought-escape and drought-tolerant plants respectively, and differ greatly in their optimum soil moisture. Figure 14 shows the pattern of variation in biomass with time for each of these species combinations:

<!-- b000329 | prose | pages [16] -->
(a) (b) (c)

<!-- b000330 | caption | pages [16] -->
Figure 14: Biomass Comparison between different combinations

<!-- b000331 | prose | pages [16] -->
From the Figure 14, we can conclude the growth pattern of these three different species combinations.

<!-- b000332 | prose | pages [16] -->
• In the community (a) formed by the combination of two drought-avoiding plant, the biomass of the two plants changed synchronously: both dropped sharply when the drought came and recovered rapidly after the end of the drought. This is because both plants have similar optimum soil moisture, so both of them are signiﬁcantly affected by drought. • In the community (b) formed by the combination of drought-escape plant and drought- avoiding plant, the biomass of both plants was also signiﬁcantly affected by drought. But the biomass of the two plants showed opposite trends. This is because during the period of sufﬁcient precipitation, the soil moisture was high and suitable for the growth of drought-escape plant, and it could become the dominant species, while drought- avoiding plant grew very slowly because of the limitation of competition. During the period of drought, the environment was not suitable for the growth of drought-escape plant, so its biomass decreased signiﬁcantly, which reduced the competitive pressure

<!-- b000333 | furniture | pages [17] -->
Team # 2309229

<!-- b000334 | furniture | pages [17] -->
Page 17 of 25

<!-- b000335 | prose | pages [17] -->
faced by drought-avoiding plant, so the drought-avoiding plant could grow during the drought. • In the community (c) formed by the combination of drought-escape plant and drought- tolerant plant, almost only drought-escape plant was growing. And drought-tolerant plant was nearly extinct in this community. This may because the conditions require for the growth of the two plants are so different that their coexistence in the same com- munity is very difﬁcult. And the compete ability of drought-tolerant plant is lower, which leads to the its extinct.

<!-- b000336 | prose | pages [17] -->
The variation trends of the total biomass of the three species combinations over time are shown in Figure 15. And we also calculated the total biomass and CoV of the biomass of the three combinations respectively, as shown in Table 3.

<!-- b000337 | prose | pages [17] -->
(a) (b) (c)

<!-- b000338 | caption | pages [17] -->
Figure 15: Total Biomass of different species combinations

<!-- b000339 | caption | pages [17] -->
Table 3: Total Biomass and Coefﬁcient of Variation

<!-- b000340 | prose | pages [17] -->
Total Biomass(kg) Combination

<!-- b000341 | prose | pages [17] -->
(a) 206.5 (b) 250.3 (c) 220.8

<!-- b000342 | prose | pages [17] -->
4.2.2 Our Conclusion

<!-- b000343 | prose | pages [17] -->
CoV of Biomass

<!-- b000344 | prose | pages [17] -->
0.1526 0.0632 0.1051

<!-- b000345 | prose | pages [17] -->
From the Figure 15 and the Table 3 we can ﬁnd that the biomass of species combinations (a) and (c) ﬂuctuated quite a lot and they even lost nearly half of their total biomass when the drought occurred. On the contrary, the biomass of species combination (b) ﬂuctuated less and the total biomass was also higher than the other two species combinations. This is because the species combination (b) is consist of drought-escape plant and drought-avoiding plant, and their optimum soil moisture are different, so that the advantages of these two species can complement each other. In the period of sufﬁcient precipitation and the period of drought, there are different dominant species in the community, resulting in the total biomass of the community relatively stable. By contrast, in species combination (c), the two plants were so different that they could not coexist. Therefore, we conclude that species combination has a great inﬂuence on both the total biomass and the stability of the community. In general, the more signiﬁcant the differences in soil moisture between plants in the community are, the easier it is for the plant community to survive in a drastically changing environment. The stability and the total biomass of the community are generally higher as well. Of course, the difference between each plant should not be too large, since the difference which is too large can lead to the extinct of one of the species.

<!-- b000346 | furniture | pages [18] -->
Team # 2309229

<!-- b000347 | furniture | pages [18] -->
Page 18 of 25

<!-- b000348 | prose | pages [18] -->
5 Task 4,5 and 6 : Impacts of Environmental Change on Species

<!-- b000349 | prose | pages [18] -->
In this section, we will discuss the effects on communities caused by external environmen- tal changes that can manifest as changes in the frequency or magnitude of droughts, habitat encroachment, environmental contamination, and so on.

<!-- b000350 | prose | pages [18] -->
5.1 Task 4 : Changes in the Magnitude and Frequency of Drought

<!-- b000351 | prose | pages [18] -->
Now, we discuss the effects of changes in drought magnitude and frequency on the com- munity. In the Equation 11 used to simulate precipitation above, we set the probability of drought to 30% and set the precipitation in a drought year to 1/2 of a normal year. When the frequency of drought increases, we adjust the probability of drought to 50%; when the magnitude of drought increases, we change the precipitation in a drought year to 1/3 of a normal year. After varying the frequency and magnitude of drought, we simulated the change in biomass of each species over time within a Five Plants Community and plotted the total biomass curve of the community;

<!-- b000352 | caption | pages [18] -->
Figure 16: Biomass of each plants during more se-

<!-- b000353 | caption | pages [18] -->
Figure 17: Total biomass of the community

<!-- b000354 | prose | pages [18] -->
vere drought

<!-- b000355 | prose | pages [18] -->
It can be seen that the communities suffering from more severe drought are very different from the previous ones. From the Figure 16 and the Figure 17, we can draw two conclusions:

<!-- b000356 | prose | pages [18] -->
• The increase in the magnitude and frequency of drought causes changes in the dis- tribution of species in the community the biomass of both drought-avoiding and drought-tolerant plants decreases, while their decrease leaves space for the survival of drought-tolerant plants. So the biomass of drought-tolerant plants increases signiﬁcantly during drought. • The ﬂuctuations in the biomass of the community remained small (no more than 10%) in the extreme drought climate. That is due to the growth of drought-tolerant plants during the drought, which indi- cates the strong stability of the Five Plants Community.

<!-- b000357 | prose | pages [18] -->
Then, we are supposed to quantify how the increase in drought magnitude and frequency actually affects the total biomass and stability of the community, and whether the increase in species diversity can actually help the community withstand drought. So we vary the num- ber of plants in the community, put one to ﬁve species into the community respectively. We calculate the total biomass to measure the vigor of the community, and the CoV of the total

<!-- b000358 | furniture | pages [19] -->
Team # 2309229

<!-- b000359 | furniture | pages [19] -->
Page 19 of 25

<!-- b000360 | prose | pages [19] -->
biomass to describe the stability. The following Figure 18 and Figure 19 show our calculation results. In this simulation, we also tried all species combinations, each point represents a species combination, and the straight line connects the mean values of all species combina- tions.

<!-- b000361 | caption | pages [19] -->
Figure 19: CoV of total biomass under different

<!-- b000362 | caption | pages [19] -->
Figure 18: Total biomass under different drought

<!-- b000363 | prose | pages [19] -->
drought conditions

<!-- b000364 | prose | pages [19] -->
conditions

<!-- b000365 | prose | pages [19] -->
From the ﬁgures above, we can ﬁnd that:

<!-- b000366 | prose | pages [19] -->
• The total biomass of the community is bound to decrease as the drought increases.

<!-- b000367 | prose | pages [19] -->
The total biomass of the community was maximum when the drought conditions took the initial value (drought probability 30% and precipitation in drought years decreased to 1/2); when increasing the frequency of drought, the total biomass of the commu- nity decreased; when increasing both the frequency of drought and the magnitude of drought, the total biomass of the community decreased further. This is because the drought environment is not suitable for the growth of most of the plants and may in- crease competition for water resources within the community. • The more severe the drought, the greater the contribution of species diversity to the community. From the trend of the total biomass curve, when the drought condition takes the initial value, the total biomass increases and then decreases as the number of species increases. When the drought frequency increases, the total biomass still increases and then de- creases, but the increase becomes bigger and the decrease becomes smaller. When the drought frequency and drought magnitude increase simultaneously, the total biomass increases as the number of species increases. This can be explained by the complemen- tary effect mentioned above: during the occurrence of drought, drought-tolerant plants can grow to compensate for the biomass loss of other plants, and the more intense the drought is, the more signiﬁcant this complementary effect becomes. • Drought increases the ﬂuctuation of biomass in communities, but increases in num- ber of species can always reduce this ﬂuctuation. From the trend of the CoV of total biomass, the more intense the drought is, the higher the CoV is. This is because severe drought is usually accompanied by rapid changes in rainfall, which will cause the biomass of the community to change rapidly as well. Regardless of the degree of drought, the CoV always decreases with the increase in the number of species in the community. That is, the increase in the number of species always leads to higher stability of the community.

<!-- b000368 | prose | pages [19] -->
In addition, to simulate the decrease of drought frequency, we set the probability of drought occurrence to 10% and the precipitation in drought years is still set to 50% of nor-

<!-- b000369 | furniture | pages [20] -->
Team # 2309229

<!-- b000370 | furniture | pages [20] -->
Page 20 of 25

<!-- b000371 | prose | pages [20] -->
mal years. We plotted the variation of the total biomass of the community with the number of species as follows:

<!-- b000372 | caption | pages [20] -->
Figure 20: Relationship between total biomass and number of species

<!-- b000373 | prose | pages [20] -->
At this time, the biomass of the community declined continuously with the increase in the number of species, because drought occurred less at this time and the complementary effect in multiple species community was not signiﬁcant. On the contrary, the competition among multiple species limited the increase of total biomass.

<!-- b000374 | prose | pages [20] -->
5.2 Task 5 : Impacts from Habitat Reduction and Environmental Pollution

<!-- b000375 | prose | pages [20] -->
In this section, we will study the effects of habitat reduction and pollution. The total land available for plant to survive has been squeezing by the logging and consequently and caused a decrease in the environmental capacity of the community. In addition, due to the excessive emission, some lands are polluted, which makes it difﬁcult for plants to survive. So the actual land available for plants in the community will be reduced, which will also lead to the reduction of environmental capacity. Thus, the consequences of habitat reduction and pollution can be attributed to the reduction of environmental capacity.

<!-- b000376 | prose | pages [20] -->
Therefore, we will gradually reduce the environmental capacity of the plant community and observe the changes in plant biomass during this process. We set the environmental capacity as a step function to simulate the gradual habitat reduction or environmental pollu- tion:

<!-- b000377 | prose | pages [20] -->
 

<!-- b000378 | prose | pages [20] -->
t ∈[0, 10](years) 1000

<!-- b000379 | prose | pages [20] -->
    

<!-- b000380 | prose | pages [20] -->
t ∈[10, 20](years) 600

<!-- b000381 | prose | pages [20] -->


<!-- b000382 | prose | pages [20] -->
Env =

<!-- b000383 | prose | pages [20] -->
t ∈[20, 30](years) 500

<!-- b000384 | prose | pages [20] -->
(17)

<!-- b000385 | prose | pages [20] -->
  

<!-- b000386 | prose | pages [20] -->
t ∈[30, 40](years) 400

<!-- b000387 | prose | pages [20] -->
   

<!-- b000388 | prose | pages [20] -->
t ∈[40, 50](years) 300

<!-- b000389 | prose | pages [20] -->
This function represents that in [0, 10] years, the habitat is not reduced and the environ- ment is not polluted, while in [10, 20] years, the environmental capacity decreases to 60% of the original, and so on. Finally, in [40, 50] years, the environmental capacity decreases to 30% of the original. We simulated the changes in biomass of various plants over time in a Single Plant Community and in a Five Plant Community, and compared the average biomass of the lat- ter four stages with the average biomass when the environmental capacity was Env = 1000

<!-- b000390 | furniture | pages [21] -->
Team # 2309229

<!-- b000391 | furniture | pages [21] -->
Page 21 of 25

<!-- b000392 | prose | pages [21] -->
(the environment was not polluted and the habitat was not reduced) . We calculate the rate of biomass loss, and the results are shown in Figure 21 and Figure 22.

<!-- b000393 | caption | pages [21] -->
Figure 21: biomass of Single Plant Community

<!-- b000394 | caption | pages [21] -->
Figure 22: biomass of Five Plant Community

<!-- b000395 | prose | pages [21] -->
From these ﬁgures, we can draw three remarkable conclusions:

<!-- b000396 | prose | pages [21] -->
• The total biomass of an ecosystem decreases when the environmental capacity de- creases. When environmental capacity decreased to 70% of the original, the Single Plant Commu- nity and the Five Plant Community lost 72.45% and 18.16%of their biomass respectively. • Species diversity can help communities resist environmental pollution Single Plant Community is vulnerable to environmental pollution or habitat reduction. By the time the environmental capacity was reduced to 40% of the original, the biomass had already lost 60%. When the community was exposed to drought, the biomass re- mained at a low level and the community almost lost its ability to recover from the effects of drought. On the Contrary, Five Plant Community only lost 19% of biomass when the environmental capacity was reduced to 30% of the initial, and the biomass of each species still recovered after the community was affected by drought. This indicates that the coexistence of multiple species gave the community better resistance not only to drought, but also to environmental pollution and habitat reduction.

<!-- b000397 | prose | pages [21] -->
5.3

<!-- b000398 | heading | pages [21] -->
Task 6 : Further Discussion on Community Viability

<!-- b000399 | prose | pages [21] -->
5.3.1 Ensuring Community Viability

<!-- b000400 | prose | pages [21] -->
In the above analysis, we obtained differential equation models to describe the changes in plant biomass, considering the effects of drought and irregular weather cycles. Based on all the conclusions, we found that the long-term viability of a plant community mainly depends on three levels: population level, community level and ecosystem level.

<!-- b000401 | prose | pages [21] -->
• Population Level We found that the drought resistance of various plants are different.

<!-- b000402 | prose | pages [21] -->
Considering that droughts will inevitably increase in the future, to ensure the viabil- ity of plant communities, we’d better choose plants with relatively low optimum soil moisture, such as drought-tolerant plants. Under different soil moisture, the dominant species varies from drought-escape plant to drought-tolerant plant. Therefore, drought- tolerant plants can be moderately planted to improve the stability of the communities when the drought arrives.

<!-- b000403 | furniture | pages [22] -->
Team # 2309229

<!-- b000404 | furniture | pages [22] -->
Page 22 of 25

<!-- b000405 | prose | pages [22] -->
• Community level We found that multi-species communities are more stable than single- species communities. Therefore, we should ensure the presence of at least two different plants in a plant community. At the same time, we found that there are differences in the characteristics of different plants so we should pay extra attention when we select species. We should select plants with relatively large differences that can provide eco- logical niche complementarity for the plant community and make it resilient in the face of adverse weather such as drought. However, we should avoid making the difference between two species too large to prevent one of the plants from becoming extinct in competition. • Ecosystem level We found that pollution and the reduction of habitats can have a greater impact on plant communities, so we should call on people to protect the en- vironment, reduce pollution emissions, and be wary of factors such as invasive species which can damage the habitats of plants.

<!-- b000406 | prose | pages [22] -->
5.3.2 The Impact of Communities on the Larger Environment

<!-- b000407 | prose | pages [22] -->
• Plant communities are part of the ecosystem, and the number and types of species in them can also affect the stability of the ecosystem. • Because many plants have a large root system, when they thrive they can act as a soil consolidator, thus preventing and controlling soil desertiﬁcation. • Plants are the producers of the ecosystem, so a stable plant community can provide the necessary energy for the region, thus sustaining the survival of various organisms under drought.

<!-- b000408 | prose | pages [22] -->
Therefore, the impact of plant communities on the environment cannot be ignored.

<!-- b000409 | prose | pages [22] -->
6

<!-- b000410 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000411 | prose | pages [22] -->
In the above, several unknown parameters are not obtained from estimation, and we set them manually. To illustrate how changes in these parameters affect the simulation results, we perform a sensitivity analysis by varying the values of these parameters and observing the changes in the simulation results.

<!-- b000412 | prose | pages [22] -->
Plant Water Absorption Rate β 6.1

<!-- b000413 | prose | pages [22] -->
We vary the value of the plant water absorption rate β and plot the change in biomass of each species in the community over time as follows:

<!-- b000414 | prose | pages [22] -->
It can be seen from the Figure 23: as β increases, the plant community has two signiﬁcant changes:

<!-- b000415 | prose | pages [22] -->
• The total biomass in the community keeps decreasing.

<!-- b000416 | prose | pages [22] -->
In the process of β changing from 10−3 to 2 × 10−2, the total biomass decreases by about 32%. This is because as β increases, the more intense the competition for water resources is, and the less water resources are available in the environment, so the environmental capacity of plants keeps decreasing. • The higher the β, the stronger the response of plants to drought.

<!-- b000417 | prose | pages [22] -->
This is because the higher the water absorption rate of plants, the less soil moisture during drought. Then, the drought will exert a larger inﬂuence on the environmental capacity of plants.

<!-- b000418 | furniture | pages [23] -->
Team # 2309229

<!-- b000419 | prose | pages [23] -->
(a) (b)

<!-- b000420 | furniture | pages [23] -->
Page 23 of 25

<!-- b000421 | prose | pages [23] -->
(c)

<!-- b000422 | prose | pages [23] -->
(b)β = 10−2

<!-- b000423 | caption | pages [23] -->
Figure 23: (a)β = 10−3

<!-- b000424 | prose | pages [23] -->
Plant Competition Intensity α 6.2

<!-- b000425 | prose | pages [23] -->
(c)β = 2 × 10−2

<!-- b000426 | prose | pages [23] -->
The competition intensity α is an important factor affecting the relationships of plants. We varied the value of α and plotted the change curve of biomass of each species in the community as follows:

<!-- b000427 | prose | pages [23] -->
(a) (b)

<!-- b000428 | caption | pages [23] -->
Figure 24: (a)α = 10−4

<!-- b000429 | prose | pages [23] -->
(c)

<!-- b000430 | prose | pages [23] -->
(b)α = 10−3 (c)α = 10−2

<!-- b000431 | prose | pages [23] -->
From the Figure 24, it can be seen that as α increases, the plant community also has two signiﬁcant changes:

<!-- b000432 | prose | pages [23] -->
• The increase of α lead to a signiﬁcant decrease in biomass.

<!-- b000433 | prose | pages [23] -->
This is because the larger α, the stronger the competition among plants, and the plants will Suppress each other. This leads to the decrease of biomass. • As α increases, some plants will not be able to survive in the community.

<!-- b000434 | prose | pages [23] -->
At α = 10−3, the plants that cannot survive are drought-tolerant plants; at α = 10−2, drought-avoiding plants cannot survive either. This is the competitive exclusion prin- ciple in biology. When the intensity of competition is small, species can coexist, while when the intensity of competition increases, species that are not adapted to the envi- ronment will gradually be excluded from the current community until only one or two "the strongest" are left in the community.

<!-- b000435 | prose | pages [23] -->
6.3 Climate Conditions

<!-- b000436 | prose | pages [23] -->
During all the above simulations, we used climate conditions of a typical subtropical re- gions, so we set A1 = 30, A2 = 98. In fact, the values of precipitation parameters may substan- tially affect the distribution of populations in the community. Here, we change the values of A1, A2 and plot the variation of biomass in the community over time as follows:

<!-- b000437 | furniture | pages [24] -->
Team # 2309229

<!-- b000438 | furniture | pages [24] -->
Page 24 of 25

<!-- b000439 | prose | pages [24] -->
(a) (b) (c)

<!-- b000440 | caption | pages [24] -->
Figure 25: (a)A1 = 30, A2 = 98

<!-- b000441 | prose | pages [24] -->
(b)A1 = 150, A2 = 30 (c)A1 = 10, A2 = 28

<!-- b000442 | prose | pages [24] -->
• Figure 25(a) represents an initial subtropical climate; • Figure 25(b) represents a typical tropical rainforest climate with greater precipitation and smaller ﬂuctuations, in which drought-escape plants are dominant because of their extremely high growth rates; • Figure 25(c) represents a typical tropical desert climate. The total biomass of this com- munity is signiﬁcantly reduced, and drought-tolerant plants are dominant because they can survive in environments with low soil humidity.

<!-- b000443 | prose | pages [24] -->
In summary, the competition intensity among species, the water absorption rate of plants, and the climate pattern are all key factors affecting the growth of plants in the commu- nity. These parameters must be estimated and measured more accurately when applying the model to practice.

<!-- b000444 | prose | pages [24] -->
7

<!-- b000445 | heading | pages [24] -->
Model Evaluation

<!-- b000446 | prose | pages [24] -->
7.1

<!-- b000447 | heading | pages [24] -->
Strengths

<!-- b000448 | prose | pages [24] -->
• We described the mechanics of the interaction between plant and environment in detail. Instead of making the too crude assumption that plant growth rates are directly propor- tional to precipitation, we modeled the interaction by assuming different plants absorb water from the soil at different rates, causing the soil moisture to decrease. And the soil moisture affects plant growth. This makes our model more realistic and more convinc- ing. • Our analysis of plant communities is carried out at both qualitative and quantitative levels. We not only used the curves of biomass for a qualitative analysis of the plant growth process, but also calculated various indicators, such as the total biomass of the plant communities and the CoV of the total biomass to quantitatively measure the stability of the plant communities. These analysis made us easier to explain why the communities beneﬁt from diversity. • Our interpretation of the experimental results is very detailed.

<!-- b000449 | prose | pages [24] -->
For each of the simulations we carried out, we not only described the results, but also tried to trace the reasons behind the intuitive results. Besides, we use some biological theories to explain our conclusions.

<!-- b000450 | furniture | pages [25] -->
Team # 2309229

<!-- b000451 | furniture | pages [25] -->
Page 25 of 25

<!-- b000452 | prose | pages [25] -->
7.2

<!-- b000453 | heading | pages [25] -->
Weaknesses and Possible Improvements

<!-- b000454 | prose | pages [25] -->
• Our description of changes in soil moisture is too simple.

<!-- b000455 | prose | pages [25] -->
we assume that the absorption rate of plants is proportional to soil moisture and that the rate of evaporation of water is also proportional to soil moisture, and these assumptions may not be very reasonable. In practice, these relationships may need to be further discussed with more experiment or research results. • We used a self-created precipitation function to simulate weather change and did not use real climate data. Our self-created precipitation function cannot simulate the full details of realistic weather changes, which may make our model biased. In the practical application of the model, historical precipitation data can be found directly. • We ignored all factors other except precipitation.

<!-- b000456 | prose | pages [25] -->
In reality, plant growth may also be affected by other factors such as temperature and sunshine, and we need to carefully consider variations in these factors if we wish to further improve the accuracy of our models.

<!-- b000457 | heading | pages [25] -->
References

<!-- b000458 | references | pages [25] -->
[1] H. J. W. MUTSAERS, A Dynamic Equation for Plant Interaction and Application to

<!-- b000459 | references | pages [25] -->
Yield-density-time Relations, Annals of Botany, Volume 64, Issue 5, November 1989,

<!-- b000460 | references | pages [25] -->
Pages 521531.

<!-- b000461 | references | pages [25] -->
[2] Ehleringer, J.R., Phillips, S.L., Schuster, W.S.F. et al. Differential utilization of summer

<!-- b000462 | references | pages [25] -->
rains by desert plants. Oecologia 88, 430434 (1991).

<!-- b000463 | references | pages [25] -->
[3] SARAH E. PARK, LAURENCE R. BENJAMIN, ANDREW R. WATKINSON, The Theory

<!-- b000464 | references | pages [25] -->
and Application of Plant Competition Models: an Agronomic Perspective, Annals of

<!-- b000465 | references | pages [25] -->
Botany, Volume 92, Issue 6, December 2003, Pages 741748.

<!-- b000466 | references | pages [25] -->
[4] Gao Xiaoyan. Study on drought resistance and its physiological mechanism in several

<!-- b000467 | references | pages [25] -->
species of Sedum[D]. Inner Mongolia Agricultural University, 2009.

<!-- b000468 | references | pages [25] -->
[5] Zhao Xuelin,Wang Taitan,Meng Wenting et al. Soil moisture status and water quantity

<!-- b000469 | references | pages [25] -->
monitoring of Yang Chai and Black Sagebrush in Mao Wu Su sandy area[J]. Xinjiang

<!-- b000470 | references | pages [25] -->
Agricultural Science,2021,58(05):937-946.

<!-- b000471 | references | pages [25] -->
[6] Li XL,Liu YJ,Sun Fei et al. Spatial and temporal patterns of soil moisture and its response

<!-- b000472 | references | pages [25] -->
to rainfall variation in the clay layer of the interdune mound of white thorn scrub in the

<!-- b000473 | references | pages [25] -->
Ulaanbaatar Desert[J]. Soil and Water Conservation Bulletin,2022,42(06):39-46.

<!-- b000474 | references | pages [25] -->
[7] Kirschner GK, Xiao TT, Blilou I. Rooting in the Desert: A Developmental Overview on

<!-- b000475 | references | pages [25] -->
Desert Plants. Genes. 2021; 12(5):709.

<!-- b000476 | references | pages [25] -->
[8] Yang XG, Liu CHH, Wang L et al. Ecological restoration and reconstruction of desert

<!-- b000477 | references | pages [25] -->
grasslands: water-mediated system response, ecological thresholds and reciprocal feed-

<!-- b000478 | references | pages [25] -->
backs driven by artiﬁcial vegetation[J]. Journal of Ecology,2023,43(01):95-104.

<!-- b000479 | references | pages [25] -->
[9] Zhang JC, Zhang JX, Yuan HB et al. Plant community types and their diversity in Kum-

<!-- b000480 | references | pages [25] -->
tag Desert[J]. Grassland Science,2012,29(10):1581-1588.
