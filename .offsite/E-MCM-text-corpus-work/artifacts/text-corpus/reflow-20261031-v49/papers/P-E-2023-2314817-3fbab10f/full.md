# P-E-2023-2314817-3fbab10f

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2023

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
E

<!-- b000005 | title | pages [1] -->
2314817

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Turn off the lights, Turn on the stars!

<!-- b000008 | prose | pages [1] -->
“On the earth, even in the darkest night, the light never wholly abandons his rule.“ ——— Jules Verne, Journey to the Center of the Earth.

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
With the rapid development of modern technology and excessive use of artificial lights, light pollution has resulted in increasingly severe problems. Therefore, the proper design and implementation of intervention strategies to address these problems deserve our attention. This report aims to build a light pollution risk level evaluating model and provide credible suggestions on how to effectively reduce the negative impacts of light pollution.

<!-- b000011 | prose | pages [1] -->
Three models are established: Model I: Ecologic-Social-Ecologic(ESE) Model; Model II: Light Pollution Risk Assessment(LPRA) Model and Model III: Interconnected-ESE Model(I-ESE) Model.

<!-- b000012 | prose | pages [1] -->
For ESE Model (Model I), we first abstract the risk of light pollution into three subsystems : Economic, Social and Ecological Subsystem and construct the ESE model. For economic subsystem, wecalculate the population growth by thelogistics equationand measure the light pollution in economic systems. For social subsystem, we take five types of land together with the brightness threshold into account and obtain the proportion of light-pollution-affected land. For ecological subsystem, we set a formula with the number of organisms together with light intensity value to calculate the number of affected organisms.

<!-- b000013 | prose | pages [1] -->
For LPRA Model(Model II), we use Analytic Hierarchy Process(AHP) based on Google search index to quantify the light pollution risk level(RL) of a certain region, then apply our model to 284 regions. After that, we use K-means algorithm to create a metric system for the risk levels and constructed four ranks: Slight(0.0443 ∼0.1678), Moderate(0.1705 ∼0.2542), Serious(0.2568 ∼ 0.3698), and Severe(0.3976 ∼0.6186). To apply our model to specific locations, we selected Ordos as protected land, Zhaotong as rural community, Qingyuan as suburban community, and Guangzhou as the urban community and obtained their RL scores: 0.1332, 0.1778, 0.2574 and 0.5154, while their risk levels are slight, moderate, serious and severe respectively.

<!-- b000014 | prose | pages [1] -->
For I-ESE Model(Model III), by establishing a link between every two subsystems, we constructed the Interconnected (I)-ESE Model on the basis of the ESE Model, and obtain quantitative relationships between ECL and SCL, ECL and ENL using nonlinear fitting. Based on I-ESE Model, we propose three effective intervention strategies to address the light situation: I. Reduce light intensity, II. Reduce the impact on society, and III. Delimit dark night protection areas and their actions correspondingly.

<!-- b000015 | prose | pages [1] -->
More specifically, we select Guangzhou and Zhaotong for further discussion and determine their optimal strategy: strategy I and II for Guangzhou and strategy II and III for Zhaotong. Then we measure the impacts of these strategies in general and particularly in Guangzhou and Zhaotong using I-ESE Model and visualize the impact with GE cube. The risk level in Guangzhou decreased from 0.5153 to 0.0309 while Zhaotong decreased from 0.1678 to 0.0885 after 20 years of implementing the optimal strategy.

<!-- b000016 | prose | pages [1] -->
Finally, the sensitivity and robustness of our model are tested. When we set the cost to be raw data, increase or reduce by 50%, the overall trend of risk level has little difference as the curve remains similar, verifying the sensitivity and robustness of our model.

<!-- b000017 | keywords | pages [1] -->
Keywords: Light Pollution, ESE Model, LPRA Model, AHP, K-means algorithm, GE Cube

<!-- b000018 | furniture | pages [2] -->
Team 2314817

<!-- b000019 | furniture | pages [2] -->
Page 2 of 25

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1

<!-- b000022 | contents | pages [2] -->
introduction

<!-- b000023 | contents | pages [2] -->
3

<!-- b000024 | contents | pages [2] -->
1.1

<!-- b000025 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
3

<!-- b000027 | contents | pages [2] -->
1.2

<!-- b000028 | contents | pages [2] -->
Problem Restatement & Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [2] -->
3

<!-- b000030 | contents | pages [2] -->
2 Assumptions and Justifications

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
3 Notations

<!-- b000033 | contents | pages [2] -->
5

<!-- b000034 | contents | pages [2] -->
4 Establishing the ESE Model

<!-- b000035 | contents | pages [2] -->
5

<!-- b000036 | contents | pages [2] -->
4.1

<!-- b000037 | contents | pages [2] -->
Pre-processing of lighting data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
5

<!-- b000039 | contents | pages [2] -->
4.2

<!-- b000040 | contents | pages [2] -->
Evaluation in economic subsystem . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
6

<!-- b000042 | contents | pages [2] -->
4.3

<!-- b000043 | contents | pages [2] -->
Evaluation in social subsystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
7

<!-- b000045 | contents | pages [2] -->
4.4

<!-- b000046 | contents | pages [2] -->
Evaluation in ecologic subsystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
8

<!-- b000048 | contents | pages [2] -->
5 Light Pollution Risk Assessment (LPRA) Model

<!-- b000049 | contents | pages [2] -->
10

<!-- b000050 | contents | pages [2] -->
5.1

<!-- b000051 | contents | pages [2] -->
Data proccessing

<!-- b000052 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
10

<!-- b000054 | contents | pages [2] -->
5.2

<!-- b000055 | contents | pages [2] -->
Analytic Hierarchy Process(AHP) Model based on Google search index . . . . . . . .

<!-- b000056 | contents | pages [2] -->
10

<!-- b000057 | contents | pages [2] -->
5.3

<!-- b000058 | contents | pages [2] -->
Light Pollution Risk Level Severity Scale

<!-- b000059 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
11

<!-- b000061 | contents | pages [2] -->
6 Application of LPRA Model

<!-- b000062 | contents | pages [2] -->
12

<!-- b000063 | contents | pages [2] -->
6.1

<!-- b000064 | contents | pages [2] -->
Application in 284 regions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
12

<!-- b000066 | contents | pages [2] -->
6.2

<!-- b000067 | contents | pages [2] -->
Application in Four Locations

<!-- b000068 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
13

<!-- b000070 | contents | pages [2] -->
7 Intervention Strategies Based on I-ESE Model

<!-- b000071 | contents | pages [2] -->
14

<!-- b000072 | contents | pages [2] -->
7.1

<!-- b000073 | contents | pages [2] -->
Establishing the Interconnected-ESE (I-ESE) Model . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
14

<!-- b000075 | contents | pages [2] -->
7.2

<!-- b000076 | contents | pages [2] -->
Quantitative Impact Assessment . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
15

<!-- b000078 | contents | pages [2] -->
7.3

<!-- b000079 | contents | pages [2] -->
Strategy I: Reduce light intensity . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
16

<!-- b000081 | contents | pages [2] -->
7.4

<!-- b000082 | contents | pages [2] -->
Strategy II: Reduce the impact of light pollution on society . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
17

<!-- b000084 | contents | pages [2] -->
7.5

<!-- b000085 | contents | pages [2] -->
Strategy III: Delimit dark night protection areas . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
18

<!-- b000087 | contents | pages [2] -->
8 Case Study: Zhaotong and Guangzhou

<!-- b000088 | contents | pages [2] -->
19

<!-- b000089 | contents | pages [2] -->
8.1

<!-- b000090 | contents | pages [2] -->
Analysis of Effectiveness: Strategy I . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
19

<!-- b000092 | contents | pages [2] -->
8.2

<!-- b000093 | contents | pages [2] -->
Analysis of Effectiveness: Strategy II . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
20

<!-- b000095 | contents | pages [2] -->
8.3

<!-- b000096 | contents | pages [2] -->
Analysis of Effectiveness: Strategy III . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
21

<!-- b000098 | contents | pages [2] -->
8.4

<!-- b000099 | contents | pages [2] -->
Selection of the Optimal Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
21

<!-- b000101 | contents | pages [2] -->
9 Sensitivity analysis

<!-- b000102 | contents | pages [2] -->
22

<!-- b000103 | contents | pages [2] -->
10 Strengths and Weaknesses

<!-- b000104 | contents | pages [2] -->
23

<!-- b000105 | contents | pages [2] -->
10.1 Strengths

<!-- b000106 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000107 | contents | pages [2] -->
23

<!-- b000108 | contents | pages [2] -->
10.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
23

<!-- b000110 | contents | pages [2] -->
11 Strategy-promoting flyer

<!-- b000111 | contents | pages [2] -->
23

<!-- b000112 | furniture | pages [3] -->
Team 2314817

<!-- b000113 | furniture | pages [3] -->
Page 3 of 25

<!-- b000114 | contents | pages [3] -->
1

<!-- b000115 | heading | pages [3] -->
introduction

<!-- b000116 | heading | pages [3] -->
1.1 Problem Background

<!-- b000117 | prose | pages [3] -->
Estimates suggest that more than one-tenth of the planet’s land area experiences artificial light at night - and that rises to 23% if skyglow is included. [1] Artificial lights have revolutionized the way humans live their day-to-day lives, resulting in increasingly severe problems along with their benefits. More than ever, human and environmental health is suffering from this boom of artificial lighting. Unfortunately, we are now faced with what scientists call “light pollution”, which poses a great threat to the ecosystem, economy and our society in several aspects.

<!-- b000118 | prose | pages [3] -->
To tackle this problem, the methodology to measure the influence of light pollution in a certain location, as well as the design of a proper intervention strategy deserve our attention. Some major cities have been aware of the seriousness of light pollution and take the lead in the exploration of governance, but problems regarding lack of legal basis and public awareness have been revealed. Challenged by ICM, we decide to build a model to evaluate light pollution as well as determine corresponding intervention strategies.

<!-- b000119 | heading | pages [3] -->
1.2 Problem Restatement & Our Work

<!-- b000120 | prose | pages [3] -->
Considering the background information and restricted conditions identified, we need to take several measures to solve the following problems:

<!-- b000121 | prose | pages [3] -->
• Problem Restatement: Develop a metric to identify and evaluate the light pollution risk level of a certain location.

<!-- b000122 | prose | pages [3] -->
- Our work: We first abstract the risk of light pollution into three subsystems, and calculated the light pollution risks concerning economic, social and ecological subsystems.

<!-- b000123 | prose | pages [3] -->
• Problem Restatement: Apply our metric to four diverse types of locations: a protected land location, a rural community, a suburban community and an urban community.

<!-- b000124 | prose | pages [3] -->
- Our work: Using AHP based on google search index, we quantify the light pollution risk level of a certain region. Then, we selected Ordos, Zhaotong, Qingyuan and Guangzhou for further discussions.

<!-- b000125 | prose | pages [3] -->
• Problem Restatement: Describe three possible intervention strategies and their corresponding actions and their potential impacts on light pollution.

<!-- b000126 | prose | pages [3] -->
- Our work: We propose three effective intervention strategies in three different aspects and their specific actions correspondingly. To evaluate the impact of these strategies, we obtain the quantitative relationships between risk levels in different aspects.

<!-- b000127 | prose | pages [3] -->
• Problem Restatement: Choose two of our locations and determine the most effective interven- tion strategy in certain locations, as well as their impacts specifically.

<!-- b000128 | prose | pages [3] -->
- Our work: We choose Guangzhou and Zhaotong to determine their optimal strategy through I-ESE Model and evaluated their impacts in GE cube.

<!-- b000129 | furniture | pages [4] -->
Team 2314817

<!-- b000130 | furniture | pages [4] -->
Page 4 of 25

<!-- b000131 | caption | pages [4] -->
Figure 1: Flowchart of our study

<!-- b000132 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000133 | prose | pages [4] -->
• Assumptions: The population density of organisms remains stable and constant. - Justifications: The environment maintains stability because natural disasters are infrequent while the birth and mortality rates are typically similar.

<!-- b000134 | prose | pages [4] -->
• Assumptions: The industrial structure of primary, secondary and tertiary industries remains unchanged. - Justifications: As the economy of the locations we study are well-developed, the industrial upgrading of these nations is practically complete, thus the changes in proportions of primary, secondary, and tertiary industries are negligible.

<!-- b000135 | prose | pages [4] -->
• Assumptions: The application of artificial light in agricultural production is not considered - Justifications: Compared with those in the secondary industry and tertiary industry, artificial lights in agriculture are not widely used. Thus, the proportion of artificial light used in primary industry is relatively small, and the negative impacts are negligible.

<!-- b000136 | prose | pages [4] -->
• Assumptions: When considering the scoring in our LPRA model, only the selected area is considered, without considering its internal influence and the interaction between regions. - Justifications: As all aspects of risk level are not reflected by a certain indicator only, it can be the result of many factors working together.

<!-- b000137 | furniture | pages [5] -->
Team 2314817

<!-- b000138 | furniture | pages [5] -->
Page 5 of 25

<!-- b000139 | heading | pages [5] -->
3 Notations

<!-- b000140 | prose | pages [5] -->
Symbol Definition

<!-- b000141 | prose | pages [5] -->
EC Total amount of light pollution produced in the economic system SC The rate of light-pollution-risked land EN Total number of organisms affected by light pollution in an area RL Light pollution risk level of a certain location ECL The light pollution risk level in economy SCL The light pollution risk level in society ENL The light pollution risk level in ecologic system

<!-- b000142 | heading | pages [5] -->
4 Establishing the ESE Model

<!-- b000143 | prose | pages [5] -->
Light pollution is the presence of unwanted, inappropriate, or excessive artificial lighting.[2] Too much light pollution washes out the view of the universe, increasing energy consumption, interfering with astronomical research, disrupts ecosystems while affecting the health and safety of both humans and wildlife. Thus, we must evaluate the risk of these different aspects we’re currently facing because of light pollution.

<!-- b000144 | prose | pages [5] -->
Based on research by National Geographic [3], the main effects of light pollution can be broken down into three aspects, thus we identify the light pollution risk level in Economic System, Social System and Ecological System respectively. Then, we can establish our light pollution risk evaluation model: Economic-Social-Ecological System Model, we shall call it ESE Model in the following paper for short. To this end, our ESE Model is the combination of three submodels, which will be introduced respectively in the following paragraph, both shown in Figure 2:

<!-- b000145 | caption | pages [5] -->
Figure 2: Breakdown of light pollution risk

<!-- b000146 | heading | pages [5] -->
4.1 Pre-processing of lighting data

<!-- b000147 | prose | pages [5, 6] -->
Data preprocessing is a way of converting this raw data into a much-desired form so that useful information can be derived from it, which is fed into our model in evaluating the light pollution risk level in a certain area. We obtain data on grayscale values of the original impact of nighttime lighting (DN) from LPSTI[8], then we eliminate DN values that are less than zero. Then, we radio-metrically correct the nightlight data for the area, the radiation correction equation is as follows:

<!-- b000148 | furniture | pages [6] -->
Team 2314817

<!-- b000149 | furniture | pages [6] -->
Page 6 of 25

<!-- b000151 | prose | pages [6] -->
2 3 × 10−10 L = DN (1)

<!-- b000152 | prose | pages [6] -->
where L represents the corrected radiation brightness value and DN represents the original grayscale value.

<!-- b000153 | heading | pages [6] -->
4.2 Evaluation in economic subsystem

<!-- b000154 | prose | pages [6] -->
Light pollution generates significant costs, which in the U.S. amounts to nearly 7 billion dollars annually. [4] To evaluate the risk level regarding light pollution in the economic system, we consider the phenomenon of the accumulation of population in an economic system. As the economic system is a complicated, interrelated system, an initial impact on the population will lead to an exponentially higher consequential impact on risk levels. Inspired by a population dynamics method [5], we formulate the N as a logistic growth function in the following Equation 2:

<!-- b000155 | prose | pages [6] -->
dN dt = r × N × (1 −N ) (2) Nm

<!-- b000156 | prose | pages [6] -->
where N represents the population in a certain location and Nm represents the maximization of the population. r represents the natural growth rate of the population. Then we can solve the logistic equation by separating variables, integrating and rearranging to get the analytical solution of the N value: Nm N(t) = (3) N0 −1)e−rt + 1 (Nm

<!-- b000157 | prose | pages [6] -->
When considering the compositional structure in an economic system, industries are categorized into primary, secondary, and tertiary sectors. We reasonably assume that the ratio of the three industries remains unchanged during the research period. After calculating the projected value of population growth, we can define the total amount of light pollution produced in the economic system(EC) by the following Equation 4:

<!-- b000158 | prose | pages [6] -->
3 X N × PCi × PLPi × tmi EC = (4) i=1 where PCi represents the proportion of primary, secondary and tertiary industries in an economic system respectively and PLPi represents the light pollution per capita in primary, secondary and tertiary industries. tmi represents the length of time that the industry uses artificial light.

<!-- b000159 | prose | pages [6] -->
Based on data from UN Data[9], we visualized the data on the total population and population growth rate in the past decade in the world, where: WRL represents world data, LMC represents low-middle income countries, UMC represents middle-high income countries and HIC represents high-income countries, shown in Figure 3. Then, Figure4 shows the percentage of primary, secondary and tertiary industries respectively. It can be easily concluded that during the past decade, the proportion of different economic sectors remains unchanged, which reflects the rationality of our assumption.

<!-- b000160 | furniture | pages [7] -->
Team 2314817

<!-- b000161 | furniture | pages [7] -->
Page 7 of 25

<!-- b000162 | caption | pages [7] -->
Figure 4: Proportion of industries

<!-- b000163 | caption | pages [7] -->
Figure 3: Total population and growth rate

<!-- b000164 | prose | pages [7] -->
To this end, we have obtained the equation to calculate the total amount of light pollution produced in the economic system, thus the light pollution risk level depends on how the economic system is affected by light pollution, which can be represented by EN.

<!-- b000165 | heading | pages [7] -->
4.3 Evaluation in social subsystem

<!-- b000166 | prose | pages [7] -->
Other than economic effects, the influence of light pollution on social aspects can’t be denied. Low levels of artificial lights might lead to a higher rate of crime, thus there has been a trade-off between the positive and negative effects impacting a specific location.

<!-- b000167 | prose | pages [7] -->
Considering the fact that the levels and pathways of light pollution vary with different land-use purposes, we divided the land in a certain location into four types: Commercial land, residential land, administrative land, green land and others. To better represent the different effects on the social environment when the light intensity is too high or too low, we set the threshold interval as follows:

<!-- b000168 | prose | pages [7] -->
• Light intensity is less than the left endpoint of the threshold interval – high potential risks in crime issues

<!-- b000169 | prose | pages [7] -->
• Light intensity is more than the right endpoint of the threshold interval – high potential risks in traffic accidents

<!-- b000170 | prose | pages [7] -->
Based on related research in night lighting design[8], we made distinctions between different land uses and their respective characteristics, thus calculating corresponding threshold intervals respectively. Results are shown in Table 1.

<!-- b000171 | furniture | pages [8] -->
Team 2314817

<!-- b000172 | furniture | pages [8] -->
Page 8 of 25

<!-- b000173 | caption | pages [8] -->
Table 1: Threshold intervals for different land types

<!-- b000174 | prose | pages [8] -->
Classification Characteristics Threshold intervals

<!-- b000175 | prose | pages [8] -->
10∼20 commercial land used for the sale of goods and services 3∼6 residential land used for housing 15∼25 administrative office land for non-profit facilities ≤3 green land main existential form to improve urban ecology 2∼5 others /

<!-- b000176 | prose | pages [8] -->
Based on data from The night sky in the World[9], we obtained the area of each land type in the requested area that falls out of the threshold interval. Thus, we can calculate the rate of light- pollution-risked land(SC) by the proportion of the sum of area outside the threshold to the total area of all types, as Equation 5 shows:

<!-- b000177 | prose | pages [8] -->
SC = Areaco + Areare + Areagr + Areaad + Areaot (5) Areatotal where Areaco, Areare, Areagr, Areaad, Areaot represents the area that falls out of the threshold interval in commercial land, residential land, administrative land, green land and others. Areatotal represents the total area of all types. Through the calculation of SC, we can obtain the proportion of light- pollution-risked land, thus evaluating the light pollution risk level in a certain area.

<!-- b000178 | heading | pages [8] -->
4.4 Evaluation in ecologic subsystem

<!-- b000179 | prose | pages [8] -->
Light pollution at night above a certain level may affect the normal survival of nocturnally active biological species, such as migration patterns, wake-sleep habits, and habitat formation. Therefore, we suppose that the light pollution risk level lies in the degree to of animals and plants are affected by light pollution.

<!-- b000180 | prose | pages [8] -->
A study of about 3,000 urban sites around the U.S.[10] found that trees and other woody plants exposed to constant artificial light at night began leafing out several days earlier than those that didn’t have nighttime lights. The evident difference across temperatures is shown in Figure 5.

<!-- b000181 | caption | pages [8] -->
Figure 5: Day of year when leaf buds break

<!-- b000182 | caption | pages [8] -->
Figure 6: Proportion of species

<!-- b000183 | furniture | pages [9] -->
Team 2314817

<!-- b000184 | furniture | pages [9] -->
Page 9 of 25

<!-- b000185 | prose | pages [9] -->
For the evaluation of the ecologic system, we selected seven target subjects: Rodents, Birds, Com- mon Fish, Tropical Fish, Trees, ordinary human and Photosensitive human, while the proportion of some species is listed in Figure 6. Then we classify them into three categories – Aquatics(common fish and tropical fish), terrestrials(rodents, birds and trees) and human(ordinary and photosensitive). The following Table 2 shows the illumination thresholds for the effect of light on animal and human rhythms. [6]

<!-- b000186 | caption | pages [9] -->
Table 2: illumination thresholds for the effect of light

<!-- b000187 | prose | pages [9] -->
Classification Illumination suppression threshold(lx)

<!-- b000188 | prose | pages [9] -->
Rodents 0.03 0.3 ∼1 Birds Tree 0 Common Fish 1 Tropical fish 0.3 Human(Photosensitive) 6 40 ∼350 Human(ordinary)

<!-- b000189 | prose | pages [9] -->
The first four threshold values come from a study by Yun, Hee-Kyung [7] while the threshold value of trees is based on a study on how urban lights at night influence the growing season. A study of about 3,000 urban sites around the U.S. found that trees and other woody plants exposed to constant artificial light at night began leafing out several days earlier than those that didn’t have nighttime lights. The difference was evident across temperatures, thus we take the threshold value of trees to be 0.

<!-- b000190 | prose | pages [9] -->
It can be concluded that once the light intensity is greater than the threshold, light pollution will affect the normal survival of living species. Therefore, we use the following equations to calculate the total number of organisms affected by light pollution in an area (EN). Based on the former three categories, we calculated their EN respectively.

<!-- b000191 | prose | pages [9] -->
For terrestrials:

<!-- b000192 | prose | pages [9] -->
3 X typei × pl1 × 1A(lg ≥lmi) × R ENt = (6) i=1 Then, for aquatics:

<!-- b000193 | prose | pages [9] -->
5 X typei × pl2 × 1A(lg ≥lmi) × R ENa = (7) i=4 Lastly, for humans:

<!-- b000194 | prose | pages [9] -->
7 X typei × 1A(lg ≥lmi) × R ENh = (8) i=6 where:

<!-- b000195 | prose | pages [9] -->
• typei represents the population density of rodents, birds, trees, common fish, tropical fish, ordinary humans and photosensitive humans respectively.

<!-- b000196 | prose | pages [9] -->
• pli represents proportion of surface area covered by land (i=1) and water (i=2).

<!-- b000197 | furniture | pages [10] -->
Team 2314817

<!-- b000198 | furniture | pages [10] -->
Page 10 of 25

<!-- b000199 | prose | pages [10] -->
• lmi represents the suppression of melatonin secretion threshold of rodents, birds, common fish and tropical fish, shown in Table 2.

<!-- b000200 | prose | pages [10] -->
• R represents the total surface area at a certain location.

<!-- b000201 | prose | pages [10] -->
• lg represents the light levels in the area. It should be noticed that the instruction functions 1A(lg ≥lmi) equals 1 when the light level is larger than the threshold and vice versa equals 0.

<!-- b000202 | prose | pages [10] -->
Thus, we obtain the equation to calculate the total number of organisms affected by light pollution in an area(EN) in Equation 9:

<!-- b000203 | prose | pages [10] -->
EN = ENt + ENa + ENh (9)

<!-- b000204 | prose | pages [10] -->
Higher EN represents more organisms would be affected by light pollution in a certain area and more damage to the biosphere, thus it means a higher light pollution risk in the ecologic system. To this end, we develop an ecological risk model and use EN to evaluate the light pollution risk of the ecological system.

<!-- b000205 | prose | pages [10] -->
To this end, we have established three interlocking submodels - Economic-Social-Ecological System Model - that evaluates the light pollution risk level in three aspects respectively. Through the three indicators EC, SC and EN, we can use the AHP model introduced later to evaluate the light pollution risk level specifically in a certain area.

<!-- b000206 | heading | pages [10] -->
5 Light Pollution Risk Assessment (LPRA) Model

<!-- b000207 | heading | pages [10] -->
5.1 Data proccessing

<!-- b000208 | prose | pages [10] -->
The three subsystems of the ESE Model have different dimensions of score indicators. To eliminate the impact of data due to different dimensions, we first normalize the data for each metric, which means the scores we measure are limited in the range of 0 to 1. Since the level of risk posed by the three subsystems is a positive indicator, we use the following equation to normalize:

<!-- b000209 | prose | pages [10] -->
xi −xmin xnew = (10) i xmax −xmin

<!-- b000210 | prose | pages [10] -->
xnew indicates the data normalized, xi indicates the initial data and n indicates the number of the data. i

<!-- b000211 | heading | pages [10] -->
5.2 Analytic Hierarchy Process(AHP) Model based on Google search index

<!-- b000212 | prose | pages [10] -->
To measure and assess the level of light pollution risk in a region, we consider its three economic, social and ecological aspects of risk. Therefore, we need to combine the scores of the three subsystems of the standardized ESE Model: ECL SCL, and ENL, to form the indicator RL.

<!-- b000213 | prose | pages [10] -->
The risk level of economic, social and ecological risk. were considered. Then We establish the initial Comparative Matrix.

<!-- b000214 | prose | pages [10] -->
M = (aij)3×3

<!-- b000215 | prose | pages [10, 11] -->
The aij represents the relative importance of index i to index j. The search index can reflect a certain extent the hotness of people’s attention at a specific time and can be used to circumvent the subjectivity of the hierarchical analysis method. The search indexes of the three sections are shown in Figure 7. The search index we obtain is 63.41 for ”economy”, 65.46 for ”society”, and 68.47 for ”ecology”. So we get the relative importance of each index in the matrix:

<!-- b000216 | furniture | pages [11] -->
Team 2314817

<!-- b000217 | furniture | pages [11] -->
Page 11 of 25

<!-- b000219 | prose | pages [11] -->
  1 63/65 63/68 65/63 1 65/68 M0 =   68/63 68/65 1

<!-- b000220 | prose | pages [11] -->
The normalized eigenvector is (0.3214, 0.3316, 0.3469), which is shown in Figure 8.

<!-- b000221 | prose | pages [11] -->
Therefore, W = (0.3214, 0.3316, 0.3469) is taken as the weight vector among ECL SCL, and ENL.

<!-- b000222 | caption | pages [11] -->
Figure 7: Google Search Index

<!-- b000223 | caption | pages [11] -->
Figure 8: Proportion of each component

<!-- b000224 | prose | pages [11] -->
After the consistency test, we can complete the quantification of the risk level. Based on the weight vectorsW0, we calculate the score of the risk level in Equation 11.

<!-- b000225 | prose | pages [11] -->
RL = W1 × ECL + W2 × SCL + W3 × ENL (11)

<!-- b000226 | prose | pages [11] -->
where RL represents the risk level of light pollution. ECL, SCL and ENL represent the economic, social and ecological risk levels respectively.

<!-- b000227 | heading | pages [11] -->
5.3 Light Pollution Risk Level Severity Scale

<!-- b000228 | prose | pages [11] -->
We classified all 284 regions in China into four levels of severity of plastic waste. Slight, Moderate, Serious and Severe, by clustering the dataset into three using the K-means algorithm to divide the dataset into four clusters in Table 3.

<!-- b000229 | caption | pages [11] -->
Table 3: Classification based on K-means

<!-- b000230 | prose | pages [11] -->
Degree Slight Moderate Serious Severe

<!-- b000231 | prose | pages [11] -->
Maximum Value 0.17050261270 0.25424527533 0.39769974082 0.61860669274 Minimum Value 0.04432992940 0.17050261270 0.25424527533 0.39769974082 Cluster Center 0.12108674 0.215758722 0.293293568 0.484986811 Number of regions 64 159 46 15

<!-- b000232 | furniture | pages [12] -->
Team 2314817

<!-- b000233 | furniture | pages [12] -->
Page 12 of 25

<!-- b000234 | heading | pages [12] -->
6 Application of LPRA Model

<!-- b000235 | heading | pages [12] -->
6.1 Application in 284 regions

<!-- b000236 | prose | pages [12] -->
We calculated the scores for all 284 regions using LPRA Model. Specific risk levels can be found in Appendix A. What’s more, We created Figure 9 to analyze the distribution of light pollution levels and selected four categories from which to analyze the patterns.

<!-- b000237 | caption | pages [12] -->
Figure 9: Risk level of light pollution in 284 regions

<!-- b000238 | prose | pages [12] -->
It can be seen that the distribution of light pollution risk levels shows more in the middle and less in the ends. It shows the balanced development of these areas, and the high-risk level is mostly concentrated in less prosperous cities, while the number of villages with low risk is also less.

<!-- b000239 | prose | pages [12] -->
Meanwhile, we made a heat map of light pollution risk in each region of China according to the provincial risk level in Figure 10. Four different types of areas - a protected land location, a rural community, a suburban community, and an urban community - were selected to measure and estimate the risk level.

<!-- b000240 | caption | pages [12] -->
Figure 10: Heat map of light pollution risk levels in China, mainland

<!-- b000241 | furniture | pages [13] -->
Team 2314817

<!-- b000242 | furniture | pages [13] -->
Page 13 of 25

<!-- b000243 | heading | pages [13] -->
6.2 Application in Four Locations

<!-- b000244 | prose | pages [13] -->
To make the result more representative without losing adaptability, we selected four different cities in China: Ordos, Zhaotong, Qingyuan and Guangzhou as location of protected land, rural community, suburban community and urban community respectively.

<!-- b000245 | prose | pages [13] -->
For each location, we collected basic data such as its population, area, climate.etc. from National Bureau of Statistics[11], along with data used in ESE Model mentioned above. Then, the LPRA Model is used to analyze the light pollution risk level of each location while The value of each indicator (EC, EN, SC) is represented by radar charts. The comparison results are shown in Figure 11.

<!-- b000246 | caption | pages [13] -->
Figure 11: Information of the four locations

<!-- b000247 | prose | pages [13] -->
• Protected Land

<!-- b000248 | prose | pages [13] -->
Located at the eastern edge of the Asian-African desert, Ordos Relic Gull National Nature Reserve was promoted to a national nature reserve in 2001, which the main objects of protection being wildlife birds including relic gulls and desert ecosystems[12]. Thus, we selected Ordos to evaluate the light pollution risk in a protected land location.

<!-- b000249 | caption | pages [13] -->
Figure 11 shows that ENL value in Ordos is remarkably higher than the other three locations

<!-- b000250 | prose | pages [13] -->
while SCL value is significantly lower. It is consistent with the objective facts of the nature reserve that they mainly serve as a habitat for different species and help protect endangered species, while economic and social aspects are usually not a primary consideration when it comes to a nature reserve. This result fully justifies the validity of our model.

<!-- b000251 | furniture | pages [14] -->
Team 2314817

<!-- b000252 | furniture | pages [14] -->
Page 14 of 25

<!-- b000253 | prose | pages [14] -->
• Rural Community

<!-- b000254 | prose | pages [14] -->
Zhaotong is located in the hinterland of the Wumeng Mountains in Yunnan Province, 96.3% of whose territory is a mountainous area with severe stone desertification. With poor transportation and low technical level, people deep in the mountains have difficulties in survival. Thus, we consider Zhaotong as a rural community to assess its light pollution risk level.

<!-- b000255 | caption | pages [14] -->
Figure 11 shows that both ECL and SCL in Zhaotong is relatively low among the four

<!-- b000256 | prose | pages [14] -->
locations, indicating that the economic system in Zhaotong suffers least from light pollution in the case. The result is consistent with our assumption as well as real-life circumstances as economic production in Zhaotong mainly depends on agriculture whose light pollution is slight.

<!-- b000257 | prose | pages [14] -->
However, relatively backward social development level as well as extremely inconvenient traffic led to relatively vulnerable social aspects.

<!-- b000258 | prose | pages [14] -->
• Suburban Community

<!-- b000259 | prose | pages [14] -->
Located on the periphery of the Pearl River Delta Economic Zone, Qingyuan has a vast territory and uneven development in many aspects. In terms of geographical location, Qingyuan is the most livable city in Guangdong with beautiful scenery. In a sense, it has become the back garden of Guangdong, thus we consider Qingyuan as a suburban community and apply our model.

<!-- b000260 | prose | pages [14] -->
According to our results, Qingyuan has a relatively high SCL and low ENL due to its low biological reserve and high population.

<!-- b000261 | prose | pages [14] -->
• Urban Community

<!-- b000262 | prose | pages [14] -->
Guangzhou is the capital of Guangdong Province as well as an international trade center and comprehensive transportation hub in China. Thus, it’s rational for us to consider Guangzhou as an urban community and apply our model.

<!-- b000263 | prose | pages [14] -->
We can see from Figure 11 that Guangzhou has the highest SCL and ECL while the ENL is lowest, which confirms our model setting as light pollution gross domestic product and social development level in Guangzhou are high in reality.

<!-- b000264 | heading | pages [14] -->
7 Intervention Strategies Based on I-ESE Model

<!-- b000265 | heading | pages [14] -->
7.1 Establishing the Interconnected-ESE (I-ESE) Model

<!-- b000266 | prose | pages [14] -->
The economy, society and ecosystems are interdependent and inextricably linked. No policy can act on just one part of them. Changing the level of risk in one has potential impacts on other systems.

<!-- b000267 | prose | pages [14] -->
During the process of establishing the ESE Model(Model I), we identified the light pollution risk level in Economic System, Social System and Ecological System respectively and build three models based on this breakdown respectively. To determine the overall impact of different strategies on the risk of light pollution at a site and to assess their potential impact in the three subsystems, it is necessary to establish correlations between ECL, SCL and ENL.

<!-- b000268 | prose | pages [14] -->
After determining the connection between the three subsystems, we need to test the correlation between the two. Among them, ECL has a significant negative correlation with ENL and ECL has a significant negative correlation with SCL. Therefore, we obtained the observed values and fitted curves by constructing nonlinear regressions for the variables with correlations as in Figure 12.

<!-- b000269 | furniture | pages [15] -->
Team 2314817

<!-- b000270 | furniture | pages [15] -->
Page 15 of 25

<!-- b000271 | caption | pages [15] -->
Figure 12: Fitting curves of the three subsystems

<!-- b000272 | prose | pages [15] -->
Meanwhile, we give the quantitative relationship between two and two in Table 4.

<!-- b000273 | caption | pages [15] -->
Table 4: Quantitative relationships between subsystems

<!-- b000274 | prose | pages [15] -->
Serial No. Curve Type Equation

<!-- b000275 | prose | pages [15] -->
ECL = 0.279 −1.774 × ENL + 2.686 × ENL2; A Quadratic curve ECL = 0.044 × 9.472SCL B Composite curve ENL = 0.171 −0.634 × ECL + 0.556 × ECL2 C Quadratic curve SCL = log9.472(ECL) D Logarithmic curve

<!-- b000276 | prose | pages [15] -->
At this point, the I-ESE Model, a risk assessment system for the interaction of three subsystems, is constructed.

<!-- b000277 | heading | pages [15] -->
7.2 Quantitative Impact Assessment

<!-- b000278 | prose | pages [15] -->
To assess the impact of the strategy on the risk of systems, we need to consider the reduced value of the risk assessment(∆X).

<!-- b000279 | prose | pages [15] -->
To evaluate the impact of each strategy on risk level reduction, we need to introduce the light pollution investment cost(Cost). The impact is estimated with a constant investment cost. Considering the differences in the development level of each region, we obtain the cost of environmental pollution treatment as about 8.43‱ of GDP based on the Annual Report of Ecological and Environmental Statistics 2021, as Cost = 0.000843 × GDP.

<!-- b000280 | prose | pages [15] -->
Having obtained the reduction in risk for systems, we can then obtain the new subsystem risk level(XL) in Equation 12.

<!-- b000281 | prose | pages [15] -->
XLnew = (X −∆X) −Xmin (12) Xmax −Xmin where X represents the risk of the three subsystems, taking the values EC, SC, and EN.

<!-- b000282 | furniture | pages [16] -->
Team 2314817

<!-- b000283 | furniture | pages [16] -->
Page 16 of 25

<!-- b000284 | prose | pages [16] -->
The level of risk in one of the subsystems is influenced by strategies, and the level of risk in the other two systems is influenced by the I-ESE model. From this, we obtain three indicators-ECL, SCL, and ENL.

<!-- b000285 | prose | pages [16] -->
After obtaining the risk level of the three subsystems, we substitute it into Equation 11 of Model II (LPRA) to obtain the risk level after implementing(RLnew) the strategy.

<!-- b000286 | prose | pages [16] -->
Based on the three interconnected subsystems, we propose specific strategies in three aspects in

<!-- b000287 | caption | pages [16] -->
Figure 13.

<!-- b000288 | caption | pages [16] -->
Figure 13: Overview of Intervention Strategies

<!-- b000289 | heading | pages [16] -->
7.3 Strategy I: Reduce light intensity

<!-- b000290 | prose | pages [16] -->
The International Dark-Sky Association estimates that 1/3 of all lighting is wasted at an annual cost of 2.2 billion dollars. [14] Measures to reduce light intensity mainly lies in economical aspects as the economic effects of light pollution can be just as tragic as ecological aspects.

<!-- b000291 | prose | pages [16] -->
• Specific Actions

<!-- b000292 | prose | pages [16] -->
- Reasonably limit the production and operation time of enterprises at night

<!-- b000293 | prose | pages [16] -->
Switching off unnecessary lights during non-production time can hugely help in reducing light pollution. Appropriately limiting the production and operation time for some high light-pollution industries can hugely help in reducing light intensity in economic aspects.

<!-- b000294 | prose | pages [16] -->
- Use shades or covers that force the light downward

<!-- b000295 | prose | pages [16] -->
Using shades or covers to help the light better focus on the intended lighting area during production is an effective way. Their usage produces less spillover which can be part of the original light fixture or can be purchased separately.

<!-- b000296 | prose | pages [16, 17] -->
- Use light pollution control devices These days, there are many ways to automatically limit light usage with lighting controls. Examples are: using dimmers to reduce the intensity of the light, motion sensors so that lights only turn on when someone is in the area and timers to control when lights turn on and off.

<!-- b000297 | furniture | pages [17] -->
Team 2314817

<!-- b000298 | furniture | pages [17] -->
Page 17 of 25

<!-- b000300 | prose | pages [17] -->
• Potential Impacts

<!-- b000301 | prose | pages [17] -->
The strategy functions mainly by limiting the production and operation time at night. Therefore, the formula for the reduction of production and operation time (∆t) for the firm is obtained in Equation 13.

<!-- b000302 | prose | pages [17] -->
Cost ∆t = tinitial −tlimit = (13) P2 + P3

<!-- b000303 | prose | pages [17] -->
- where tinitial represents the prescribed time for enterprises to stop production and operation, tlimit represents the original production and operation stopping time without intervention, P2 represents the average production value per hour in the secondary industry and P3 represents the average turnover per hour in the service sector. Using ∆t and the population (N), we then obtain the reduction in EC(∆EC) in Equation 14.

<!-- b000304 | prose | pages [17] -->
∆EC = N × (PC2 × PLP2 + PC3 × PLP3) × ∆t + Σδ (14)

<!-- b000305 | prose | pages [17] -->
- where PLP2 represents light pollution from the secondary industry, PLP3 represents light pollution from the tertiary industry, and Σδ represents the reduction of light pollution by the remaining measures.

<!-- b000306 | prose | pages [17] -->
After calculating the ∆EC, it is substituted into Equation 12 to calculate the economic risk level (ECLnew) after implementing the strategy. The new social (SCLnew) and environmental (ENLnew) risk levels are then derived by bringing in Equations C and D based on I-ESE model.

<!-- b000307 | prose | pages [17] -->
To this end, the light pollution risk level (RLnew ) is calculated by Equation 11. 1 Thus, we measured the potential impact in terms of the change in SCLnew and ENLnew after changing the strategy while the change in risk level(RLnew) indicating the overall impact.

<!-- b000308 | prose | pages [17] -->
In conclusion, without losing universality on the basis of the simplified model, we consider reasonably limiting the production and operation time of enterprises at night as the main action taken to reduce light intensity and evaluate its impacts on ECL.

<!-- b000309 | heading | pages [17] -->
7.4 Strategy II: Reduce the impact of light pollution on society

<!-- b000310 | prose | pages [17] -->
Excess artificial light at night disrupts the cycle, suppressing melatonin production and negatively affecting human health. Also, safety-related dangers that come with poor visibility at night are caused by glaring lights and result in more light pollution risks in our society.

<!-- b000311 | prose | pages [17] -->
• Specific Actions

<!-- b000312 | prose | pages [17] -->
- Use of smart lighting devices

<!-- b000313 | prose | pages [17] -->
LED light technology has evolved rapidly over the past few years, which is the best type of light to help reduce light pollution because their beams are more focused than other types such as fluorescent or metal halide. Thus, switching to LED lighting reduces brightness without affecting visibility and is able to effectively eliminate social risks.

<!-- b000314 | furniture | pages [18] -->
Team 2314817

<!-- b000315 | furniture | pages [18] -->
Page 18 of 25

<!-- b000316 | prose | pages [18] -->
- Refrain from light trespassing The use of bright outdoor lights directed toward neighboring houses is likely to increase the risk of sleep disorders. Therefore, it must be ensured that outdoor lights do not trespass into residential houses. For example, light shields offer many benefits, including reduced glare and improved night vision.

<!-- b000317 | prose | pages [18] -->
- Glare-free lighting for vehicles driven at night Dim lighting while driving at night is just enough for streets and highways already lit with artificial lighting. Thus, outdoor lights with glare should be replaced with low-glare alternatives.

<!-- b000318 | prose | pages [18] -->
• Potential Impacts

<!-- b000319 | prose | pages [18] -->
The implementation of this measure is mainly through the use and extension of smart devices, thus it is necessary to calculate the number of street lights that need to be replaced, given in Equation 15.

<!-- b000320 | prose | pages [18] -->
Cost Num = (15) P + Pwork - where Num represents the number of smart lighting devices that need to be placed, P represents the price of smart devices, and Pwork represents the construction price.

<!-- b000321 | prose | pages [18] -->
After obtaining the number of streetlights that need to be replaced given a certain amount of cost, we can calculate the reduction of SC(∆SC) in Equation 16 by the difference between street lighting brightness before and after the replacement.

<!-- b000322 | prose | pages [18] -->
∆SC = (lightintial −lightsmart) × Num + Σδ (16)

<!-- b000323 | prose | pages [18] -->
- where lightinitial represents the brightness of the original streetlight, lightlimit represents the brightness after using the smart street light, and Σδ represents the reduction of light pollution by the remaining measures.

<!-- b000324 | prose | pages [18] -->
As ∆SC is obtained, it is substituted into Equation 12 to calculate the social risk level (SCLnew) after implementing strategy two. The new economic risk levels(ECLnew) are then derived by bringing in Equation B in our I-ESE model. Then, the light pollution risk level (RLnew ) is 1 obtained by bringing into Equation 11.

<!-- b000325 | prose | pages [18] -->
Thus, we measured the potential impact by evaluating the change in SCLnew after implementing the strategy, with the change in risk level(RLnew) indicating the overall impact.

<!-- b000326 | heading | pages [18] -->
7.5 Strategy III: Delimit dark night protection areas

<!-- b000327 | prose | pages [18] -->
The conflict between ecological systems and light pollution has become more and more prominent in recent years. Thus, industrial transformation is a key way to coordinate economic development and environmental protection to achieve sustainable development and reduce light pollution risks.

<!-- b000328 | prose | pages [18] -->
• Specific Actions

<!-- b000329 | prose | pages [18] -->
- Delimit dark night protection areas

<!-- b000330 | prose | pages [18] -->
According to China Biodiversity Conservation and Green Development Foundation, locations with a certain biological density size are encouraged to designate dark night protection zones and make strict control of the use of lights in and around protected areas.

<!-- b000331 | furniture | pages [19] -->
Team 2314817

<!-- b000332 | furniture | pages [19] -->
Page 19 of 25

<!-- b000333 | prose | pages [19] -->
- Relocation of enterprises with high light pollution

<!-- b000334 | prose | pages [19] -->
• Potential Impacts To make a better understanding as well as fully implement strategy three, it is optimal for us to set up protected areas for specific species. Therefore, it is particularly significant to calculate the extent of implementation of the protected area, and we obtained Equation 17 to establish the area of the protected area.

<!-- b000335 | prose | pages [19] -->
Cost Sqprotect = (17) Cprotect

<!-- b000336 | prose | pages [19] -->
- Sqprotect represents the area of ecologic reserve in a location. After obtaining Sqprotect, we can make improvements to the equation in the ecologic system. Since only plants and animals need to be considered for the establishment of light pollution protection zones. Then the reduction of EN(∆EN) can be calculated, shown in Equation 18.

<!-- b000337 | prose | pages [19] -->
3 5 X X typei×pl1×1A(lg ≥lmi)×Sqprotect+ typei×pl2×1A(lg ≥lmi)×Sqprotect+Σδ ∆EN = i=1 i=4 (18) - where Σδ represents the reduction of light pollution by the remaining measures.

<!-- b000338 | prose | pages [19] -->
After calculating the ∆EN, it is substituted into Equation 12 to calculate the ecological risk level (ENLnew) after implementing the strategy. The new economic risk levels(ECLnew) are then derived by bringing in Equation A based on the I-ESE model. Thereafter, the light pollution risk level (RLnew ) is obtained by bringing into Equation 11. 1 Thus, we measured the potential impact in terms of the change in ENLnew after changing the strategy, while the change in risk level(RLnew) indicated the overall impact.

<!-- b000339 | heading | pages [19] -->
8 Case Study: Zhaotong and Guangzhou

<!-- b000340 | prose | pages [19] -->
To verify our I-ESE model and determine the most effective strategy, we chose two typical locations to apply our model: Zhaotong and Guangzhou.

<!-- b000341 | heading | pages [19] -->
8.1 Analysis of Effectiveness: Strategy I

<!-- b000342 | prose | pages [19, 20] -->
With further implementation of strategy one, the value of ECL decreases as the prescribed time for enterprises to stop production and service tlimit is ahead. Based on the Logistic Model in our ESE Model(Model 1), the population of both cities shows a growing trend, thus ECL will rise continuously with the population growth. To show the impact of strategy intervention more intuitively, we use d-value to represent the difference between risk levels with and without implementing strategy One Based on data from China Statistical Yearbook[12] in 2021, we calculated the difference between the ECLT new, ENLnew, SCLnew and RLnew value with strategy one implemented and the value of ECL, ENL, SCL and RL without interventions, as both of the d-values are shown in Figure 14 and It is obvious to see that the d-value of SCL, ECL and RL are increasing at a growing rate after 20 years of implementing strategy one in Guangzhou, reaching 0.0197 of d-value in ECL, 0.0083 of d-value in SCL and 0.0123 of d-value in RL. The lines have an upward growth trend with a positive slope except for ENL, indicating that strategy one is relatively efficient in Guangzhou when it comes to social and economic aspects. We believe that the large population and huge economic volume of Guangzhou mainly lead to greater scope for eliminating light pollution risk levels.

<!-- b000343 | caption | pages [19] -->
Figure 15.

<!-- b000344 | furniture | pages [20] -->
Team 2314817

<!-- b000345 | furniture | pages [20] -->
Page 20 of 25

<!-- b000346 | caption | pages [20] -->
Figure 14: D-value of strategy one in GZ

<!-- b000347 | caption | pages [20] -->
Figure 15: D-value of strategy one in ZT

<!-- b000349 | prose | pages [20] -->
When it comes to Zhaotong, more improvements can be seen in ENL as its d-value reaches 0.0178 in 2041 while impacts in SCL and ECL are relatively small with 0.0004 of d-value in ECL. By the year 2023, the d-value in both reaches a relatively high level with 0.0181 in ENL and 0.0063 in RL. Since then, the d-value remains stable, representing the impacts of strategy one on three aspects in Zhaotong is stabilized. It is consistent with the fact that the impacts of strategy one on economic and social aspects are relatively not efficiently transmitted, due to its poor transportation and low technical level.

<!-- b000350 | heading | pages [20] -->
8.2 Analysis of Effectiveness: Strategy II

<!-- b000351 | prose | pages [20] -->
With more measures taken regarding the use and extension of smart devices, improvement in social aspects is reflected in the change in SCLnew after implementing the strategy. Thus, the value of ECLnew, ENLnew, SCLnew and RLnew and the original levels are shown in Figure 16.

<!-- b000352 | caption | pages [20] -->
Figure 16: Impacts of Strategy Two

<!-- b000353 | furniture | pages [21] -->
Team 2314817

<!-- b000354 | furniture | pages [21] -->
Page 21 of 25

<!-- b000355 | prose | pages [21] -->
It can be seen that Guangzhou’s SCL and ECL have been greatly reduced due to the intervention of strategy two, with ECL decreases from 0.5264 in 2022 to 0.0440 in 2041 and SCL decreases from 1 to 0.0229, indicating that the intervention of smart lighting devices has greatly improved not only social aspects but also ecological aspects. Meanwhile, data in Zhaotong shows that in the year 2030, SCL and RL reaches its relatively low positions of 0.0100 and 0.0885 and stays stable since then, while other risk levels stay relatively the same. The results in Zhaotong are consistent with the reality that with the low residential density and travel frequency of residents are likely to reduce the impact of strategic interventions.

<!-- b000356 | heading | pages [21] -->
8.3 Analysis of Effectiveness: Strategy III

<!-- b000357 | prose | pages [21] -->
For strategy three, we determined a set of actions to transfer industries with serious light pollution to low-biological-density areas and the improvements will be mostly shown in the decrease of ECL in both cities.

<!-- b000358 | caption | pages [21] -->
Figure 17: Impacts of Strategy Three in GZ

<!-- b000359 | caption | pages [21] -->
Figure 18: Impacts of Strategy Three in ZT

<!-- b000360 | caption | pages [21] -->
Figure 17 shows that with interventions regarding the protected area and relocation of specific

<!-- b000361 | prose | pages [21] -->
industries, risk levels in Guangzhou show no obvious trend of change, indicating strategy three has limited influence on the light pollution risk level in Guangzhou, partly due to the relatively low biological density in Guangzhou. As for Zhaotong, the ENL has a downward sloping trend before it reaches its relatively low position 0.1695 in 2032 while others stay stable as well.

<!-- b000362 | heading | pages [21] -->
8.4 Selection of the Optimal Strategy

<!-- b000363 | prose | pages [21] -->
Based on the impact analysis and our I-ESE Model, we can now evaluate and compare the effective- ness between the three strategies, thus determining the optimal strategy for Guangzhou and Zhaotong. Instead of conducting a parallel comparison between different risk levels, we set up a GE Cube to more intuitively show the changes of ECL, SCL, ENL and Rl before and after the implementation of the strategies. We set up the GE Cube of Guangzhou and Zhaotong in the three-dimensional rectangular coordinate system respectively, while red dots represent the risk level location with and without strat- egy one, blue dots represent the risk level location with and without strategy two and yellow dots for strategy three, shown in Figure 19 and 20.

<!-- b000364 | furniture | pages [22] -->
Team 2314817

<!-- b000365 | furniture | pages [22] -->
Page 22 of 25

<!-- b000366 | caption | pages [22] -->
Figure 19: GE Cube of Guangzhou

<!-- b000367 | caption | pages [22] -->
Figure 20: GE cube of Zhaotong

<!-- b000368 | prose | pages [22] -->
It is obvious to see that for Guangzhou, strategy two makes huge improvements in eliminating the negative aspects of light pollution while it makes a huge difference in Zhaotong as well. Comparing the difference between the two locations, we draw a GE Cube, where the x-axis represents ECL, y-axis represents SCL and z-axis represents ENL. OP ∗represents the optimal point where the light pollution risks are minimized Therefore, we propose the optimal strategies for the two cities respectively:

<!-- b000369 | prose | pages [22] -->
• Guangzhou: Strategy II + Strategy I

<!-- b000370 | prose | pages [22] -->
We choose strategy two - reducing the impact of light pollution on society - as the main strategy to implement and strategy one - reducing light intensity - as the secondary strategy. This inspired policy-makers in Guangzhou to promote the use of smart lighting devices without losing attention to economic considerations.

<!-- b000371 | prose | pages [22] -->
Once the strategies are implemented, positive changes will be seen in all aspects, especially in the reduction of SCL and ECL, which are evaluated in the analysis of the effectiveness and shown in Figure 19.

<!-- b000372 | prose | pages [22] -->
• Zhaotong: Strategy II + Strategy III

<!-- b000373 | prose | pages [22] -->
As for Zhaotong, we believe strategy Two should be the main strategy while the second strategy is strategy three - delimiting night protection areas. Attention should be paid especially in the use of smart lighting devices and refraining from light trespassing while the production and operation time of enterprises at night should be carefully limited as well.

<!-- b000374 | prose | pages [22] -->
Efforts will be seen in ecological and social aspects clearly while the general light pollution risk level would be lower as we analyzed in the former part just now.

<!-- b000375 | heading | pages [22] -->
9 Sensitivity analysis

<!-- b000376 | prose | pages [22] -->
Since the investment value used for light pollution varies greatly from place to place, we test the impact of the change of risk level of different investment amounts on RL. By adjusting Cost, we can directly or indirectly affect ECL, SCL and ENL through different strategies, thus affecting RL.

<!-- b000377 | prose | pages [22, 23] -->
We set Cost to increase by 50%, raw data and reduce by 50%, and plot our result of sensitivity analysis of cases in Guangzhou and Zhaotong. As can be seen from Figure 21 and Figure 22, the overall trend of the risk level curve of the three strategies remains unchanged after changing the investment. This verifies the sensitivity and robustness of our model.

<!-- b000378 | furniture | pages [23] -->
Team 2314817

<!-- b000379 | furniture | pages [23] -->
Page 23 of 25

<!-- b000381 | caption | pages [23] -->
Figure 21: Sensitivity Analysis of Guangzhou

<!-- b000382 | caption | pages [23] -->
Figure 22: Sensitivity Analysis of Zhaotong

<!-- b000383 | heading | pages [23] -->
10 Strengths and Weaknesses

<!-- b000384 | heading | pages [23] -->
10.1 Strengths

<!-- b000385 | prose | pages [23] -->
• In our ESE Model, we design simulation algorithms to simulate the light pollution risk level in the economy, society and ecologic aspects of a certain location, which is close to real life and has certain reference significance.

<!-- b000386 | prose | pages [23] -->
• We have established a multi-level indicator system in our LPRA model, the first-level indicators cover a wide range, and the second-level indicators are more detailed, so the model we built is comprehensive and detailed.

<!-- b000387 | prose | pages [23] -->
• After simulation, we find that our model has significant progress on four main indicators(ENL, SCL, ECL and RL) after implementing the optimal strategy, indicating that our model is effective.

<!-- b000388 | prose | pages [23] -->
• We consider various indicators in economic, social and ecological aspects, making our model relatively comprehensive and objective.

<!-- b000389 | heading | pages [23] -->
10.2 Weaknesses

<!-- b000390 | prose | pages [23] -->
• Some of our parameters are based on a semi-educated guess because some data are unavailable.

<!-- b000391 | prose | pages [23] -->
• Even though our model considers the problem indicators extremely comprehensive, due to some indicator data missing, we can only choose the indicators that can be considered while the data is true and complete to analyze.

<!-- b000392 | heading | pages [23] -->
11 Strategy-promoting flyer

<!-- b000393 | prose | pages [24] -->
Turn off the LIGHTS ICM Zhaotong

<!-- b000394 | furniture | pages [24] -->
Team:2314817

<!-- b000395 | prose | pages [24] -->
Turn on the STARS

<!-- b000396 | prose | pages [24] -->
!!! Better Zhaotong with Smart lighting !!!

<!-- b000397 | prose | pages [24] -->
ACTION 1: Using covered bulbs Streets and highways lighting must be properly designed such that too much light is not reflected in the sky. The solution for this is using covered bulbs that light facing downwards.

<!-- b000398 | prose | pages [24] -->
ACTION 2: Using LED lights LEDs and compact fluorescents (CFLs) can help reduce energy use and protect the environment. Switching to LED lighting allows for reduced luminance without compromising visibility.

<!-- b000399 | prose | pages [24] -->
ACTION 3: Glare-free lighting Dim lighting while driving at night is just enough for streets and highways already lit with artificial lighting. In areas without artificial lighting in Zhaotong, medium lighting is more than enough.

<!-- b000400 | prose | pages [24] -->
LIGHT POLLUTION BETTER SLEEP SAFER DRIVING RISK REDUCED

<!-- b000401 | prose | pages [24] -->
After implementing Reduce impact of Eliminate serious glare the actions light trespassing that reduce your vision

<!-- b000402 | prose | pages [24] -->
FOLLOW US & DO NOT MAKE ZHAOTONG BLINDED BY THE LIGHT

<!-- b000403 | furniture | pages [25] -->
Team 2314817

<!-- b000404 | furniture | pages [25] -->
Page 25 of 25

<!-- b000405 | heading | pages [25] -->
References

<!-- b000406 | references | pages [25] -->
[1] Gaston, K.J., Duffy, J.P., Gaston, S. et al. Human alteration of natural light cycles: causes and

<!-- b000407 | references | pages [25] -->
ecological consequences. Oecologia 176, 917–931 (2014).

<!-- b000408 | references | pages [25] -->
[2] https://en.wikipedia.org/wiki/Light_pollution

<!-- b000409 | references | pages [25] -->
[3] https://education.nationalgeographic.org/resource/light-pollution/

<!-- b000410 | references | pages [25] -->
[4] Terrel Gallaway, Reed N. Olsen, David M. Mitchell, The economics of global light pollution,

<!-- b000411 | references | pages [25] -->
Ecological Economics, Volume 69, Issue 3,2010,Pages 658-665,ISSN 0921-8009

<!-- b000412 | references | pages [25] -->
[5] https://mathworld.wolfram.com/LogisticEquation.html

<!-- b000413 | references | pages [25] -->
[6] Grubisic M,Haim A,Bhusal P,et al.Light pollution,circadian photoreception,and melatonin in

<!-- b000414 | references | pages [25] -->
vertebrates[J].Sustainability,2019,11:1-51.

<!-- b000415 | references | pages [25] -->
[7] https://doi.org/10.14249/eia.2019.28.1.63

<!-- b000416 | references | pages [25] -->
[8] http://www.ldhyw.com/zcfg/csyjzmsjgf.asp

<!-- b000417 | references | pages [25] -->
[9] https://data.un.org

<!-- b000418 | references | pages [25] -->
[10] https://academic.oup.com/pnasnexus/article/1/2/pgac046/6569705

<!-- b000419 | references | pages [25] -->
[11] http://www.stats.gov.cn/tjsj/ndsj/

<!-- b000420 | references | pages [25] -->
[12] https://www.cma.gov.cn

<!-- b000421 | references | pages [25] -->
[13] http://www.inquinamentoluminoso.it/dmsp/index.html

<!-- b000422 | references | pages [25] -->
[14] InternationalDark-SkyAssociation.PracticalGuidetoLightPollution.Tucson,

<!-- b000423 | references | pages [25] -->
Arizona:InternationalDark-SkyAssociation,2011.

<!-- b000424 | references | pages [25] -->
[15] https://www.darksky.org/light-pollution/wildlife/

<!-- b000425 | heading | pages [25] -->
Appendix A
