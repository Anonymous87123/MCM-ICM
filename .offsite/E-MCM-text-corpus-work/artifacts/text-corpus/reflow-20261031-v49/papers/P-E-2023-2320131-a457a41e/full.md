# P-E-2023-2320131-a457a41e

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
2320131

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Less Light Pollution & Brighter Starry Sky

<!-- b000008 | prose | pages [1] -->
How long has it been since you saw a spectacular starry night sky? Nowadays, 80 percent of the world’s population lives under skyglow. As light pollution continues to grow, more and more people are taking this issue seriously. In this paper, we established a light pollution assessment model and proposed three strategies to combat light pollution.

<!-- b000009 | prose | pages [1] -->
In task 1, we divided the area to be evaluated into eight grids according to the city plan map, and used the entropy weight method (EWM) to integrate three factors related to light pollution into a total attributional index. Then, considering the interaction of light pollution between adjacent areas, we innovatively use the Raster method and this index to introduce the concept of light pollution index (LPI). Light pollution index has a direct impact on the economy, ecology, and human health, leading to the light pollution risk. We use AHP to obtain the light pollution risk level (LPRL) and use it to identify the light pollution risk level of a location.

<!-- b000010 | prose | pages [1] -->
In task 2, we apply the model in Task 1 to Saskatoon in Canada. By calculation, we obtained the average LPRI for a protected land location, a rural community, a suburban community, and an urban community. The result is 0.0665, 0.1529, 0.2726 and 0.3397, meaning that the suburban community and the urban community have a higher risk. Then we plotted the heat map of LPRI as shown in Figure 8 to accurately reflect the circumstances of each grid. Finally, we utilize K-means Algorithm to classify the LPRI of each grid in the suburban community and the urban communities. We divide the grid into five groups and determine which grids are in extreme risk areas.

<!-- b000011 | prose | pages [1] -->
In task 3, we propose three possible intervention strategies to address light pollution. The grid movement strategy optimizes the layout of the city by moving the grid, thus reducing LPRI. The regulatory strategy eliminates light pollution at the source by reducing light luminance and illumination time. The compensation Strategy chooses to achieve LPRI decline through a certain economic cost.

<!-- b000012 | prose | pages [1] -->
In task 4, we applied three strategies to the suburban community and the urban community of Saskatoon. By calculation, the grid movement strategy can effectively reduce LPRL. However, we need to consider the high cost of city relocation. To compare compensation strategies with regulatory strategies, we introduce the concept of the strategy intensity factor. The level of LPRI reduction by the two policies for the same strategy intensity factor is shown in figure 15. Ultimately, we conclude that the regulatory strategy is more effective for these two areas.

<!-- b000013 | prose | pages [1] -->
In addition, we conducted a sensitivity analysis of the model, adjusted the parameters of the constraint conditions with a fixed step length, evaluated the optimization effect. The advantages and disadvantages of the model are also analyzed. We also write a flyer to promote the regulatory strategy for Saskatoon.

<!-- b000014 | keywords | pages [1] -->
Keywords: Light Pollution; Raster Method; K-means Algorithm; Strategy Intensity Factor

<!-- b000015 | furniture | pages [2] -->
Page 1 of 23

<!-- b000016 | furniture | pages [2] -->
Team # 2320131

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1 Introduction.......................................................................................................2

<!-- b000019 | contents | pages [2] -->
1.1 Problem Background....................................................................................................... 2

<!-- b000020 | contents | pages [2] -->
1.2 Our work..........................................................................................................................2

<!-- b000021 | contents | pages [2] -->
2 Assumptions and Justifications.......................................................................3

<!-- b000022 | contents | pages [2] -->
3 Notations............................................................................................................3

<!-- b000023 | contents | pages [2] -->
4 Data Collection..................................................................................................3

<!-- b000024 | contents | pages [2] -->
5 Light Pollution Risk Level Evaluation Model...............................................4

<!-- b000025 | contents | pages [2] -->
5.1 Rasterization of Regions..................................................................................................4

<!-- b000026 | contents | pages [2] -->
5.2 Exponential Analysis and Modeling................................................................................5

<!-- b000027 | contents | pages [2] -->
5.3 Light Pollution Composite Index.....................................................................................7

<!-- b000028 | contents | pages [2] -->
5.4 Light Pollution Risk Assessment Model..........................................................................9

<!-- b000029 | contents | pages [2] -->
6 Model Application and Validation................................................................13

<!-- b000030 | contents | pages [2] -->
6.1 Risk levels in Urban and Suburban............................................................................... 14

<!-- b000031 | contents | pages [2] -->
6.2 Risk Levels in Protected Land and Rural Community.................................................. 15

<!-- b000032 | contents | pages [2] -->
6.3 Analysis of Light Pollution Risk Level Based on K-means Clustering.........................16

<!-- b000033 | contents | pages [2] -->
7 Three Types of Strategies to Intervene in Light Pollution.........................17

<!-- b000034 | contents | pages [2] -->
7.1 Strategy I: Grid Movement Strategy Based on Simulated Annealing Algorithm..........17

<!-- b000035 | contents | pages [2] -->
7.2 Strategy II: Regulatory Strategy Based on Intensity Factors.........................................18

<!-- b000036 | contents | pages [2] -->
7.3 Strategy III: Compensation Strategy Based on Intensity Factors..................................19

<!-- b000037 | contents | pages [2] -->
8 Intervention Strategies For Saskatoon.........................................................20

<!-- b000038 | contents | pages [2] -->
8.1 Moving Saskatoon's Grid...............................................................................................20

<!-- b000039 | contents | pages [2] -->
8.2 Regulation or Compensation......................................................................................... 21

<!-- b000040 | contents | pages [2] -->
9 Sensitivity Analysis.........................................................................................22

<!-- b000041 | contents | pages [2] -->
10 Strengths and Weaknesses...........................................................................22

<!-- b000042 | contents | pages [2] -->
10.1 Strengths...................................................................................................................... 22

<!-- b000043 | contents | pages [2] -->
10.2 Weaknesses.................................................................................................................. 23

<!-- b000044 | contents | pages [2] -->
References...........................................................................................................23

<!-- b000045 | furniture | pages [3] -->
Page 2 of 23

<!-- b000046 | furniture | pages [3] -->
Team # 2320131

<!-- b000047 | heading | pages [3] -->
1 Introduction

<!-- b000048 | heading | pages [3] -->
1.1 Problem Background

<!-- b000049 | prose | pages [3] -->
I have outwalked the furthest city light, which ends the first stanza of Robert Frost’s poem ‘Acquainted with the Night’. For the majority of contemporary people, especially contemporary urban dwellers, such a feat is becoming exceedingly difficult in our electrified, 24h societies. Although artificial night lighting has brought many advances and possibilities for social development, the light pollution caused by its misuse has brought negative impacts on the ecological environment, physical and mental health, etc. that cannot be ignored.

<!-- b000050 | caption | pages [3] -->
Figure 1: How does light pollution change our perception of the night sky?

<!-- b000051 | prose | pages [3] -->
However, light pollution has received relatively little attention compared to other environmental issues and remains in the scientific and cultural "dark". Equally importantly, the environmental problems caused by artificial night lighting have received little attention through the concept of light pollution. Therefore, it is imperative to establish a mathematical model to measure and mitigate light pollution in a place.

<!-- b000052 | heading | pages [3] -->
1.2 Our work

<!-- b000053 | caption | pages [3] -->
Figure 2: Work Overview

<!-- b000054 | furniture | pages [4] -->
Page 3 of 23

<!-- b000055 | furniture | pages [4] -->
Team # 2320131

<!-- b000056 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000057 | prose | pages [4] -->
We made the following assumptions to help us with our modeling. These assumptions are the promise of our subsequent analysis.

<!-- b000058 | prose | pages [4] -->
These factors that we did not mention have a small impact on the system. This is  because in reality, there are too many factors that affect the risk level of light pollution to consider all of them. Therefore, this assumption is reasonable and helps to avoid unnecessary troubles in constructing the model.

<!-- b000059 | prose | pages [4] -->
The data we collect from online databases is accurate, reliable and mutually  consistent. Because our data sources are all websites of international organizations, it’s reasonable to assume the high quality of their data.

<!-- b000060 | prose | pages [4] -->
When dividing the grid, the grid at the junction of different kinds of areas is divided  into the kinds that occupy the largest area in the grid species. We ignore the errors caused by doing so for the assessment of light pollution risk levels.

<!-- b000061 | heading | pages [4] -->
3 Notations

<!-- b000062 | prose | pages [4] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000063 | caption | pages [4] -->
Table 1: Notations used in this paper

<!-- b000064 | heading | pages [4] -->
Symbol

<!-- b000065 | prose | pages [4] -->
Description The horizontal sequence value of a grid, as an integer The vertical sequence value of a grid, as an integer The light damage degree at The brightness balance index at Scores for evaluating the illumination time at Light pollution composite index Economic index Ecological diversity index Human health index The index to evaluate Light pollution risk level Strategy implementation intensity factor

<!-- b000066 | heading | pages [4] -->
4 Data Collection

<!-- b000067 | prose | pages [4] -->
The data we used mainly include satellite images and brightness values of global lights, information on light pollution and environmental protection, population density and other indicators, etc. The data sources are summarized in Table 2.

<!-- b000068 | caption | pages [4] -->
Table 2: Data source collation

<!-- b000069 | prose | pages [4, 5] -->
Database Names Database Websites Data NASA https://www.nightlights.io/ IDA https://www.darksky.org/ Maps © 2021 Mapbox © OpenStreetMap Light Pollution Map www.lightpollutionmap.info/ Google Scholar https://scholar.google.com/

<!-- b000070 | furniture | pages [5] -->
Page 4 of 23

<!-- b000071 | furniture | pages [5] -->
Team # 2320131

<!-- b000073 | heading | pages [5] -->
5 Light Pollution Risk Level Evaluation Model

<!-- b000074 | prose | pages [5] -->
Before developing a light pollution risk level evaluation index that can be widely tested, it is necessary to establish a comprehensive index to evaluate the light pollution level of a site. To this end, we first determined a spatial model to rasterize the area, selected the core indicators closely related to light pollution for analysis and calculation, and refined the rasterized grid to establish a more rigorous light pollution composite index. After that, we evaluate the risk level of light pollution in an area from four aspects through data research.

<!-- b000075 | caption | pages [5] -->
Figure 3: Visualization of the model building process

<!-- b000076 | heading | pages [5] -->
5.1 Rasterization of Regions

<!-- b000077 | prose | pages [5] -->
The work of the predecessors has given us some inspiration. The utilization of artificial illumination exhibits significant variation across distinct regions within the city. For instance, the commercial areas of the city display considerably higher levels of luminance in comparison to the residential areas, attributable to regional functions. Hence, to investigate the spatial distribution issue, the present study employs the grid method.

<!-- b000078 | prose | pages [5] -->
In accordance with the division regulations of the urban planning network, the grid is categorized into four distinct types, namely, commercial grid, residential grid, industrial grid, and depopulated zone. The specific introduction is as follows:

<!-- b000079 | furniture | pages [6] -->
Page 5 of 23

<!-- b000080 | furniture | pages [6] -->
Team # 2320131

<!-- b000081 | prose | pages [6] -->
Commercial grid: This type of grid is mainly composed of commercial areas and commercial centers with high level of economic activities, mainly concentrated in cities, but also a small number of distribution in towns and rural areas. Many commercial areas frequently use spotlights, floodlights, neon lights, light boxes, LED advertising screens and other lighting equipment to achieve the role of publicity and attract crowds, but the improper application of artificial light will have the opposite effect, causing a serious waste of power resources and light pollution problems.

<!-- b000082 | prose | pages [6] -->
Residential grid: The residential grid primarily comprises residential areas, encompassing apartment buildings and single-family houses, which are the most susceptible to light pollution due to functional reasons. In recent years, light pollution in residential areas has become progressively more severe in various regions, attributed to urbanization, as indicated by light trespass and inappropriate internal lighting.

<!-- b000083 | prose | pages [6] -->
Industrial grid: The industrial grid comprises areas dedicated to industrial activities, such as manufacturing, logistics, and warehousing. It is mainly concentrated in urban and suburban areas, etc., where light pollution has less impact.

<!-- b000084 | prose | pages [6] -->
Depopulated zone ：As the name implies, it is a special area that is sparsely populated, such as wilderness, protected area, etc.

<!-- b000085 | prose | pages [6] -->
These grids can be easily visualized in Figure 4:

<!-- b000086 | caption | pages [6] -->
Figure 4: Four types of grids in different areas

<!-- b000087 | heading | pages [6] -->
5.2 Exponential Analysis and Modeling

<!-- b000088 | prose | pages [6] -->
, we have established three indicators for evaluation: For the different regions light damage degree , brightness balance index and illumination time index .

<!-- b000089 | furniture | pages [7] -->
Page 6 of 23

<!-- b000090 | furniture | pages [7] -->
Team # 2320131

<!-- b000091 | heading | pages [7] -->
5.2.1 Indicator Establishment

<!-- b000092 | prose | pages [7] -->
(1) Light Damage Degree

<!-- b000093 | prose | pages [7] -->
The light damage degree is an assessment metric that centers on the harm caused by light to the human body, which is closely linked to the intensity of light, specifically the brightness of the nighttime sky. Studies have indicated that artificial light-induced damage to the human body varies across regions, with the degree of damage increasing with rising brightness until it reaches a peak level. To simplify the calculation, a differential equation for the degree of light damage with respect to light luminance is constructed based on the structural form of the Volterra model:

<!-- b000094 | prose | pages [7] -->
(1)

<!-- b000095 | prose | pages [7] -->
Where , are the light damage degree and light luminance with coordinates respectively, is the maximum value of brightness in the grid.

<!-- b000096 | prose | pages [7] -->
Neon lights in the city, red, green, blue and other saturated light boxes and other such forms of too much light, too much color, easy to cause light clutter, that is, excessive combination of light; advertising screens in shopping malls, LED lights in the square often occur in the naked eye imperceptible strobe, easy to trigger headaches, human eye discrimination decline and other undesirable phenomena. Considering the harmonization and sustainability of the city at night, the light damage should take the light chromaticity and light stroboscopic flicker into account. Therefore, the final modified expression can be obtained:

<!-- b000097 | prose | pages [7] -->
(2)

<!-- b000098 | prose | pages [7] -->
where , are the correction factors of light chromaticity and light strobe respectively.

<!-- b000099 | prose | pages [7] -->
Since the effects of light chromaticity and light strobe may vary across different regions, the correction factors should also be classified accordingly. Table 3 presents an estimation of the relevant parameters.

<!-- b000100 | caption | pages [7] -->
Table 3: Parameter estimation for different regions

<!-- b000101 | prose | pages [7] -->
categories

<!-- b000102 | prose | pages [7] -->
Commercial grid 0.1645 0.1623 Urban Residential grid 0.1061 0.1053 community Industrial grid 0.0815 0.0727 Residential grid Suburban 0.0546 0.0527 community Industrial grid 0.0325 0.0303 others 0 0

<!-- b000103 | prose | pages [7, 8] -->
(2) Brightness Balance Index In many studies, the severity of light pollution is characterized by the ratio of the nighttime sky brightness affected by artificial light sources to its natural brightness (i.e., contrast). Therefore, when evaluating the nighttime light environment, not only the illumination level but also the spatial distribution of light should be taken into account. To address the inhomogeneity of luminance in space, this paper proposes a brightness balance index based on light distribution uniformity and luminance contrast, which can be used to assess the impact of light pollution.

<!-- b000104 | furniture | pages [8] -->
Page 7 of 23

<!-- b000105 | furniture | pages [8] -->
Team # 2320131

<!-- b000107 | prose | pages [8] -->
(3)

<!-- b000108 | prose | pages [8] -->
Where is the brightness balance index, and are the maximum and minimum values of luminance in the grid, respectively.

<!-- b000109 | prose | pages [8] -->
(3) Illumination Time At a certain light intensity, the longer the exposure time, the more serious the cumulative effect of light pollution. Conversely, when the light is very strong but the duration is very short, according to classical physical theory, this does not cause light pollution. Therefore, the irradiation time is a factor that cannot be ignored in the control of light pollution. In order to simplify the calculation, we have selected some critical values for the following division.

<!-- b000110 | caption | pages [8] -->
Table 4: A three-way score table

<!-- b000111 | prose | pages [8] -->
Illumination Time(h) Score 1 0.67 0.33

<!-- b000112 | heading | pages [8] -->
5.3 Light Pollution Composite Index

<!-- b000113 | heading | pages [8] -->
5.3.1 Narrow Light Pollution Composite Index Based on EWM

<!-- b000114 | prose | pages [8] -->
The weight assigned to each index in the EWM calculation is determined by its information entropy, which reflects the degree of variability of the index. The higher the information entropy, the more significant the index is in the assessment. Thus, utilizing EWM to determine the weight of each index in the calculation of the index of light pollution is an objective approach.

<!-- b000115 | prose | pages [8] -->
After preprocessing the data, we obtained data for the last three years from 15 regions. As these indicators are all positive, we standardized the data:

<!-- b000116 | prose | pages [8] -->
(1)

<!-- b000117 | prose | pages [8, 9] -->
where represents the original data of the -th indicator value of the -th grid, while and represents the minimum and maximum data in the -th indicator of the -th grid.

<!-- b000118 | furniture | pages [9] -->
Page 8 of 23

<!-- b000119 | furniture | pages [9] -->
Team # 2320131

<!-- b000121 | prose | pages [9] -->
The information entropy can be obtained from Eq.5.

<!-- b000122 | prose | pages [9] -->
(2)

<!-- b000123 | prose | pages [9] -->
If ，plug Eq.6 into Eq.5:

<!-- b000124 | prose | pages [9] -->
(3)

<!-- b000125 | prose | pages [9] -->
Based on the information entropy , the weight of each indicator could be calculated by Eq.7.

<!-- b000126 | prose | pages [9] -->
(4)

<!-- b000127 | prose | pages [9] -->
Based on the above discussion, we assigned weights to each indicator and the weighting results are as follows: Light Damage Degree (85.73%), Brightness Balance Index (4.82%), Irradiation Time (9.45%). On the basis of those calculated weights, we have

<!-- b000128 | prose | pages [9] -->
(5)

<!-- b000129 | prose | pages [9] -->
It should be noted that this calculation overlooks the influence of light pollution between areas and their surroundings. However, in real-world situations, the impact of light pollution between regions is also a crucial factor that cannot be ignored. For instance, the hazards of light trespass in residential areas often stem from commercial areas. Therefore, is merely a narrow light pollution indicator that requires further optimization.

<!-- b000130 | heading | pages [9] -->
5.3.2 Convolution Kernel

<!-- b000131 | prose | pages [9] -->
When considering the extent to which an area is affected by artificial light, it is important to take into account not only the integrated light pollution index of that area but also the light pollution index of its neighboring areas. Therefore, we introduce the light pollution coefficient , which represents the influence of different areas on their surrounding regions. As shown in Eq.9, we convolve nine using a convolution kernel.

<!-- b000132 | furniture | pages [10] -->
Page 9 of 23

<!-- b000133 | furniture | pages [10] -->
Team # 2320131

<!-- b000134 | prose | pages [10] -->
(1)

<!-- b000135 | prose | pages [10] -->
where is the center factor, and can be calculated by the following equation.

<!-- b000136 | prose | pages [10] -->
(2)

<!-- b000137 | prose | pages [10] -->
It should be noted that i and j cannot be 0 at the same time.

<!-- b000138 | prose | pages [10] -->
With this calculation, we can guarantee that all elements in the matrix after the convolution sign in Eq.9 sum to 1. The value of is determined by the type of region that is in the coordinates, as shown in table 5.

<!-- b000139 | caption | pages [10] -->
Table 5: Values of LF in different regions

<!-- b000140 | prose | pages [10] -->
region LF region LF Urban Commercial Suburban 0.02 0.05 District residential District Urban residential Suburban Industry 0.04 0.01 District District Urban Industry Countryside and 0.03 0 District Protected land

<!-- b000141 | heading | pages [10] -->
5.4 Light Pollution Risk Assessment Model

<!-- b000142 | prose | pages [10] -->
To comprehensively evaluate the cumulative effect of light pollution on a region, it is essential to assess it from multiple perspectives. Considering the topic's background and objectives, we chose to evaluate the grid’s risk level comprehensively using four criteria: economic impact, biodiversity, human health and social stability.

<!-- b000143 | heading | pages [10] -->
5.4.1 Economic Index(EI)

<!-- b000144 | prose | pages [10] -->
The development and utilization of artificial light sources have brought significant economic benefits. However, the overuse of light has led to light pollution, which incurs significant social costs, including adverse impacts on biodiversity, human health, astronomical observations, and energy consumption. It is estimated that in the United States alone, light pollution wastes nearly $7 billion worth of energy annually. Therefore, it is essential to establish a more reasonable evaluation model to measure the relationship between light pollution and the economy, which would enable us to better manage the associated economic problems and effectively mitigate them.

<!-- b000145 | prose | pages [10, 11] -->
Given the basic theory and assumptions of the Douglas function, we developed a coupled light-economy function (considering only the night economy to simplify the model):

<!-- b000146 | furniture | pages [11] -->
Page 10 of 23

<!-- b000147 | furniture | pages [11] -->
Team # 2320131

<!-- b000149 | prose | pages [11] -->
(1)

<!-- b000150 | prose | pages [11] -->
where , denote the nightly economic benefits and population of -th grid respectively, and is a function to be determined. To seek the functional form of , we make the following assumptions.

<!-- b000151 | prose | pages [11] -->
Each individual possesses a certain level of economic benefits, and the night  economy output generated by each individual increases as the intensity of their exposure to light increases, but the rate of increase decreases over time.

<!-- b000152 | prose | pages [11] -->
We introduce the role of technology, but do not consider the effect of technology  versus time, i.e., the role of technology is essentially constant

<!-- b000153 | prose | pages [11] -->
We simplify that the economic cost caused by light pollution is roughly linearly  related to the degree of light pollution.

<!-- b000154 | prose | pages [11] -->
Thus, we can derive the expression for the economic indicator for a region as:

<!-- b000155 | prose | pages [11] -->
(2)

<!-- b000156 | prose | pages [11] -->
Where:

<!-- b000157 | prose | pages [11] -->
is the technology impact factor, which varies somewhat from country to country  and region to region.

<!-- b000158 | prose | pages [11] -->
In the context of economic output, represents the proportion of brightness, while  1- represents the proportion of population. Thus, the magnitude of directly reflects the weight of brightness and population in creating economic growth.

<!-- b000159 | prose | pages [11] -->
is a linear factor to fit the parameters of economic loss and light pollution index. 

<!-- b000160 | prose | pages [11] -->
We employ maximum likelihood estimation to fit the parameters and perform calculations using MATLAB. The estimates for the relevant parameters are presented in Table 6.

<!-- b000161 | caption | pages [11] -->
Table 6: Parameter estimation results

<!-- b000162 | prose | pages [11] -->
Parameter Value 0.4356 345.4 -5.007

<!-- b000163 | heading | pages [11] -->
5.4.2 Ecological Diversity Index(BDI)

<!-- b000164 | prose | pages [11] -->
Over the past century, the scope and intensity of artificial nighttime lighting have increased significantly, resulting in significant impacts on the biology and ecology of wildlife.

<!-- b000165 | furniture | pages [12] -->
Page 11 of 23

<!-- b000166 | furniture | pages [12] -->
Team # 2320131

<!-- b000167 | prose | pages [12] -->
For example, artificial lighting at night can cause bird collisions and fatalities, disrupt bird migration, and suppress amphibian reproduction, among other effects.

<!-- b000168 | prose | pages [12] -->
Gleason (1922) has proposed a mathematical formula to measure ecological diversity:

<!-- b000169 | prose | pages [12] -->
, where A is the unit area of the selected area and S is the number of species in the community. We use this equation to quantify the initial ecological diversity of an area.

<!-- b000170 | prose | pages [12] -->
In our model, an increase in the light pollution index suppresses the number of species and populations, and the degree of impact is basically in line with an s-shaped curve. Therefore, after fitting the data, we considered the biodiversity index BDI as shown in Eq.13.

<!-- b000171 | prose | pages [12] -->
(1)

<!-- b000172 | prose | pages [12] -->
We believe that the main reason for the differences between biodiversity index curves in different regions is that the number of species S in the communities in different regions is different, which leads to differences in B. In general, within the same area, the ranking is from largest to smallest: Protected Land > Rural Community > Suburban Community > Urban Community.

<!-- b000173 | prose | pages [12] -->
Taking the protected area and suburban areas as examples, Figure 5 displays the difference between the biodiversity indexes curves of the two regions. Fortunately, regions with higher BDI generally exhibit lower levels of light pollution. However, this underscores the need to pay attention to the impact of light pollution on rural and protected areas, as the same LPI can cause greater ecological damage. Moreover, since the BDI calculation formula differs only by a multiplier across different regions, their fast decrease point exhibits the same LPI intensity.

<!-- b000174 | heading | pages [12] -->
5.4.3 Human Health Index(HHI)

<!-- b000175 | prose | pages [12, 13] -->
The common forms of light pollution in night lighting are light trespass, glare zone, and light clutter. Long-term exposure to light trespass and intense glare increases the risk of developing eye diseases such as cataracts and macular degeneration. According to data from the Centers for Disease Control and Prevention in the United States, light trespass and glare contribute to nearly half of all cases of blindness.

<!-- b000176 | furniture | pages [13] -->
Page 12 of 23

<!-- b000177 | furniture | pages [13] -->
Team # 2320131

<!-- b000179 | caption | pages [13] -->
Figure 6 visualizes the common forms and relationships of light pollution.

<!-- b000180 | prose | pages [13] -->
We assume that the probability of disease caused by light pollution is linearly related to the severity of light pollution, so we have:

<!-- b000181 | prose | pages [13] -->
(1)

<!-- b000182 | prose | pages [13] -->
Where:

<!-- b000183 | prose | pages [13] -->
is the area correction factor, when the area calculated is a residential area,  and in other cases.

<!-- b000184 | prose | pages [13] -->
is the population density of the region. 

<!-- b000185 | heading | pages [13] -->
5.4.4 Social Stability

<!-- b000186 | prose | pages [13] -->
Many people believe that inadequate lighting at night makes them less safe, as criminals tend to target poorly-lit areas. As a result, rising crime rates have been used to promote increased outdoor lighting. However, Kurt W. Riegel argues that such studies have been limited to a few small areas. Taking a broader view, considering entire cities or the nation as a whole, reveals inconsistencies. For instance, a study conducted by the Federal Bureau of Investigation found that total crime rates and outdoor lighting luminosity increase together. Based on this study, we can conclude that there is no necessary correlation between artificial light and crime rates. As a result, we ultimately decided to disregard this indicator.

<!-- b000187 | heading | pages [13] -->
5.4.5 Light Pollution Risk Level(LPRI)

<!-- b000188 | prose | pages [13] -->
In evaluating the level of light pollution risk in a region, it is necessary to first normalize the indicator values of all grids within the region for calculation. We first assume that there are n grids in a region, and we use i to denote the number of a particular grid. As discussed in the previous section, economic indicators (EI) and ecological diversity indicators(BDI) are negative indicators for assessing light pollution risk level, while the human health index(HHI) is a positive indicator. Therefore, all data should be equally and initially normalized, resulting in the following formula:

<!-- b000189 | prose | pages [13] -->
(1)

<!-- b000190 | prose | pages [13, 14] -->
When evaluating the weights, the methodology that we exploit here, AHP, is most widely adopted. Practically, subjective method preserves more scientific rationality as objective method cannot realize certain criteria. Using this method can reflect the relative significance among the three indexes in spite of the essence of each and define the weights naturally. As a result, we take the subjective AHP as our main approach rather than other more objective models when deciding the weights. By establishing a judgment matrix and calculating the consistency ratio, we obtained the weight coefficients of the three factors, which enabled us to establish the light pollution risk level model.

<!-- b000191 | furniture | pages [14] -->
Page 13 of 23

<!-- b000192 | furniture | pages [14] -->
Team # 2320131

<!-- b000194 | prose | pages [14] -->
(2)

<!-- b000195 | prose | pages [14] -->
In Eq.16,

<!-- b000196 | prose | pages [14] -->
By utilizing weighted averages, we can roughly estimate the level of light pollution risk in a particular area.

<!-- b000197 | prose | pages [14] -->
(3)

<!-- b000198 | prose | pages [14] -->
We can estimate the level of light pollution risk in a particular area by utilizing weighted averages. However, it is important to note that using averages to estimate the risk level of a region is not a comprehensive or rigorous calculation method. Given the geographic environment, climate, spatial distribution, and other factors of a region, we recommend that evaluators conduct a detailed analysis of the internal level of light pollution when assessing the risk level of a particular area.

<!-- b000199 | heading | pages [14] -->
6 Model Application and Validation

<!-- b000200 | prose | pages [14] -->
In this section, we selected Saskatoon, a medium-sized city in Canada, as the object of our study. Based on the urban plan of Saskatoon, we grid the city and the suburb of Saskatoon. A rural community and a protected land around the city were also selected and the same operation was performed. The specific division is shown in Figure 7.

<!-- b000201 | caption | pages [14] -->
Figure 7: Gridding Saskatoon

<!-- b000202 | furniture | pages [15] -->
Page 14 of 23

<!-- b000203 | furniture | pages [15] -->
Team # 2320131

<!-- b000204 | heading | pages [15] -->
6.1 Risk levels in Urban and Suburban

<!-- b000205 | prose | pages [15] -->
In general, cities and suburbs are the most serious places for light pollution, and therefore often serve as the focus of light pollution studies. We solve the LPRI heat map of light pollution risk levels in urban and suburban areas by using the established evaluation model with MATLAB. The results are shown in Fig. 8.

<!-- b000206 | caption | pages [15] -->
Figure 8: LPRI heat map

<!-- b000207 | prose | pages [15] -->
From the figure 7, it can be seen:

<!-- b000208 | heading | pages [15] -->
1. The most serious areas of light pollution correspond to the commercial and some

<!-- b000209 | prose | pages [15] -->
residential areas in the center of the city, and at the edge of the city there is generally less light pollution. This is consistent with what we already know. 2. At the same time, it can be observed that some areas close to the city center also have less light pollution. By comparing the light pollution risk level map and the population density map, we believe that these areas arise mainly due to two aspects:

<!-- b000210 | prose | pages [15] -->
(1) The existence of areas with less population density in the location close to the city center due to some external factors. In these areas, the impact of light pollution on human health index will be reduced, which leads to the light pollution risk level to remain at a relatively low level.

<!-- b000211 | prose | pages [15] -->
(2) There are a small number of industrial areas in the location close to the city center, according to the model's method of evaluating human health index, the industrial areas will cause less health damage due to light pollution compared to residential areas, so the light pollution risk level will also be reduced.

<!-- b000212 | prose | pages [15] -->
In order to evaluate the light pollution risk level for each type of area, we calculated the average light pollution risk level for each type of area and the results are shown in Fig. 9.

<!-- b000213 | prose | pages [15] -->
From the figure 8, we can see: 1. the light pollution risk level in cities is overall higher than that in suburban areas, which is in line with expectations, because the lightness level in cities will be higher than that in suburban areas.

<!-- b000214 | prose | pages [15, 16] -->
2. The light pollution risk level is significantly higher in commercial areas than in other areas, mainly because there will be a strong interaction between commercial areas.

<!-- b000215 | furniture | pages [16] -->
Page 15 of 23

<!-- b000216 | furniture | pages [16] -->
Team # 2320131

<!-- b000218 | prose | pages [16] -->
3. The risk level of light pollution in residential areas is higher than that in industrial areas, because industrial areas are generally far away from the city center according to the requirements of urban planning, and the level of light pollution on health is relatively lower compared to residential areas.

<!-- b000219 | caption | pages [16] -->
Figure 9: The risk level in different regions

<!-- b000220 | heading | pages [16] -->
6.2 Risk Levels in Protected Land and Rural Community

<!-- b000221 | prose | pages [16] -->
Due to the relatively simple grid type, small area, and limited data in rural and protected areas, we will not delve into the spatial distribution of light pollution inside them, but instead evaluate it roughly using Eq.(17).

<!-- b000222 | prose | pages [16] -->
(1)

<!-- b000223 | prose | pages [16] -->
The average level of light pollution risk in rural and protected areas is relatively low compared to urban and suburban communities. However, this finding is specific to the Canadian context where there is a significant buffer zone between rural and protected areas and cities due to the country's large territory and small population. As a result, rural and protected areas are less impacted by urban light pollution. Nonetheless, in some countries with higher population densities, the risk of light pollution in rural and protected areas closer to cities may approach or even exceed the risk in suburban areas. This is due to the greater sensitivity of the biodiversity index of rural communitys to light pollution. Despite the limited number of studies on light pollution in rural and protected areas, it is crucial to pay sufficient attention to the risk of light pollution as its levels increase. However, we do not discuss this issue further here due to space constraints.

<!-- b000224 | furniture | pages [17] -->
Page 16 of 23

<!-- b000225 | furniture | pages [17] -->
Team # 2320131

<!-- b000226 | heading | pages [17] -->
6.3 Analysis of Light Pollution Risk Level Based on K-means Clustering.

<!-- b000227 | prose | pages [17] -->
We have obtained the light pollution risk level for each grid earlier and plotted the heat map. But we also need to determine the classification of light pollution risk levels for each grid to facilitate further analysis.

<!-- b000228 | prose | pages [17] -->
The focus of our study in this article is on light pollution in urban and suburban areas, so we will discuss these two regions here. We classified the light pollution risk levels of the grids in these two regions into five categories using the K-means clustering method: Extreme risk area, High-risk area, Moderate-risk area, Low-risk area, and Safe area. The classification standards obtained are shown in Figure 10.

<!-- b000229 | prose | pages [17] -->
Based on the above classification criteria, we obtained the percentage distribution of each type of grid among these five groups by calculating the risk level of light pollution for each type of grid visually. The obtained results are shown in Fig.11.

<!-- b000230 | caption | pages [17] -->
Figure 11: Percentage statistics of various types

<!-- b000231 | prose | pages [17] -->
From the figure 10, it can be seen that:

<!-- b000232 | prose | pages [17] -->
1. The most of the commercial areas are Extreme risk area and High-risk area, and the Extreme risk areas are basically concentrated in the commercial areas.

<!-- b000233 | prose | pages [17] -->
2. The problem of light pollution in residential areas of the city is also prominent, and the distribution of High-risk area and Moderate-risk area is very common.

<!-- b000234 | prose | pages [17] -->
3. At the same time, considering the special characteristics of residential areas, a good environment of residential areas has an important role in improving people's sense of well-being. Therefore, the light pollution in residential areas must be taken seriously.

<!-- b000235 | furniture | pages [18] -->
Page 17 of 23

<!-- b000236 | furniture | pages [18] -->
Team # 2320131

<!-- b000237 | prose | pages [18] -->
4. The suburban area is relatively low in light pollution, and there is no Extreme risk area and High-risk area, which is consistent with the previous analysis.

<!-- b000238 | prose | pages [18] -->
5. For the whole urban and suburban areas, High-risk area and moderate-risk area only account for a small portion, which is consistent with the Pareto principle.

<!-- b000239 | heading | pages [18] -->
7 Three Types of Strategies to Intervene in Light Pollution

<!-- b000240 | prose | pages [18] -->
Based on the establishment and application of the light pollution risk assessment model, we have formulated three intervention strategies from different perspectives. In the following, We will discuss the specific implementation of the three strategies and their potential impact on light pollution below.

<!-- b000241 | heading | pages [18] -->
7.1 Strategy I: Grid Movement Strategy Based on Simulated Annealing

<!-- b000242 | heading | pages [18] -->
Algorithm

<!-- b000243 | prose | pages [18] -->
In this section, We will discuss how to reduce the overall level of light pollution by implementing reasonable urban planning. Simply put, this can be achieved through the use of "mobile grids". There are some additional assumptions to simplify analysis for the question.

<!-- b000244 | prose | pages [18] -->
Hypothesis 1: The feature parameters of the grid "move" as the grid "moves". The  characteristic parameters of a grid are the parameters that differ between each grid in light pollution risk assessment model, like night sky brightness, population density, brightness balance index, etc. This may be a bit difficult to understand, so we decided to explain this Hypothesis intuitively by using a figure.

<!-- b000245 | caption | pages [18] -->
Figure 12: The indicators will change with the changes of the grid

<!-- b000246 | prose | pages [18] -->
Hypothesis 2: When we "move" the grid, we should minimize the impact on the  other functions of the city, so we added the following restriction: each grid must be surrounded by 8 grids of the same type as the grid, so that the grids can coordinate with each other and improve the efficiency of the city.

<!-- b000247 | prose | pages [18, 19] -->
Based on the above two Hypothesis, we choose to use the simulated annealing algorithm to solve this optimization problem. Our goal is to minimize the sum of light pollution risk levels in the selected area. The calculation method of is as follows:

<!-- b000248 | furniture | pages [19] -->
Page 18 of 23

<!-- b000249 | furniture | pages [19] -->
Team # 2320131

<!-- b000251 | prose | pages [19] -->
(1)

<!-- b000252 | prose | pages [19] -->
is out selected region.

<!-- b000253 | prose | pages [19] -->
For convenience, the initial state of the grid is denoted as S. This state contains not only the coordinate distribution of the grid, but also the parameter information corresponding to each grid. When the grid is swapped, S changes to the new state S’, denoted as The pseudocode is as follows:

<!-- b000254 | heading | pages [19] -->
Algorithm : Simulated annealing algorithm for optimal grid distribution

<!-- b000255 | prose | pages [19] -->
Input: Output:

<!-- b000256 | prose | pages [19] -->
for do to Randomly select two grids for exchange Calculate the value of on the equation If

<!-- b000257 | prose | pages [19] -->
else

<!-- b000258 | prose | pages [19] -->
If

<!-- b000259 | prose | pages [19] -->
else

<!-- b000260 | prose | pages [19] -->
end

<!-- b000261 | heading | pages [19] -->
7.2 Strategy II: Regulatory Strategy Based on Intensity Factors

<!-- b000262 | prose | pages [19] -->
In response to the problem of light pollution, the International Dark Sky Organization has proposed "Five Principles for Responsible Outdoor Lighting":

<!-- b000263 | furniture | pages [20] -->
Page 19 of 23

<!-- b000264 | furniture | pages [20] -->
Team # 2320131

<!-- b000265 | caption | pages [20] -->
Figure 13: Five Principles for Responsible Outdoor Lighting

<!-- b000266 | prose | pages [20] -->
However, in production and daily life, most enterprises and individuals cannot consciously abide by these principles. Therefore, it is necessary for the government to establish and enforce relevant laws and regulations to supervise the implementation of these principles. we developed the strategy implementation intensity factor , and specified its value as {1,2,3,4,5}, which indicates the intensity of {weak, weaker, medium, stronger, strong} five levels, respectively.

<!-- b000267 | prose | pages [20] -->
Through this regulatory approach, the five principles of outdoor lighting can be better implemented. Corresponding to our model, it will reduce the light luminance L, light chromaticity correction factor , light strobe correction factor , brightness balance index and illumination time t.

<!-- b000268 | prose | pages [20] -->
Since the reduction of luminosity is subject to many restrictions, we consider the reduction of luminosity to be more difficult. Therefore, we set the luminosity to decrease by 1% for each level of increase in strategy intensity factor , and the other parameters to decrease by 3%. We use to denote the above parameters that vary under the action of the intensity factor, and obtain the following equation.

<!-- b000269 | prose | pages [20] -->
(1)

<!-- b000270 | caption | pages [20] -->
Table 7:

<!-- b000271 | prose | pages [20] -->
The relationship between and

<!-- b000272 | prose | pages [20] -->
3 3 1 3 3

<!-- b000273 | heading | pages [20] -->
7.3 Strategy III: Compensation Strategy Based on Intensity Factors

<!-- b000274 | prose | pages [20] -->
In addition to directly regulating the use of light, we can also compensate for the harm caused by light pollution through governmental macro-regulation, for example, by taxing enterprises and factories that produce light pollution and using the tax revenue for infrastructure development as well as the development of technology and new materials which is related to light pollution reduction to reduce the impact of light pollution on health, biodiversity.

<!-- b000275 | prose | pages [20] -->
As described in Section 7.2, we specify intensity factors with values {1,2,3,4,5} to represent the factors of the five strategy implementation intensity levels {weak, weak, moderate, strong, strong}.

<!-- b000276 | prose | pages [20] -->
Since the implementation of taxation strategy is to compensate the harm of light pollution on health and biodiversity at the expense of certain economic benefits. Considering the effect of the intensity factor on the magnitude of the parameters in the model, the effect of each increase in strategy intensity is specified as follows:

<!-- b000277 | prose | pages [20] -->
The parameter related to economic indicators technical impact factor decreases  3 , and the linear factor increases 3 , i.e., the economic benefit decreases and the cost increases.

<!-- b000278 | furniture | pages [21] -->
Page 20 of 23

<!-- b000279 | furniture | pages [21] -->
Team # 2320131

<!-- b000280 | prose | pages [21] -->
The impact factor related to the biodiversity indicators and the linear factor  increases 3 , i.e., the economic benefit decreases and the cost increases. The impact factors related to biodiversity parameter 10(recorded as ) and 6.5(recorded as ) are decreases 3 , and the parameter related to human health indicators are increased 3 , i.e., the light pollution is less harmful to biodiversity and health.

<!-- b000281 | prose | pages [21] -->
Accordingly, we obtain the following expressions:

<!-- b000282 | prose | pages [21] -->
(1)

<!-- b000283 | caption | pages [21] -->
Table 8: The relationship between

<!-- b000284 | prose | pages [21] -->
and

<!-- b000285 | prose | pages [21] -->
3 -3 3 3 -3

<!-- b000286 | heading | pages [21] -->
8 Intervention Strategies For Saskatoon

<!-- b000287 | prose | pages [21] -->
We have applied the developed intervention strategies to urban and suburban communities in Saskatoon and conducted simulations of light pollution levels to obtain the most effective intervention strategies by analyzing the changes in light pollution levels after the intervention

<!-- b000288 | heading | pages [21] -->
8.1 Moving Saskatoon's Grid

<!-- b000289 | prose | pages [21] -->
For the layout of a city, we are most concerned with two locations:

<!-- b000290 | prose | pages [21] -->
(1) the city center, where the commercial district can have a significant impact on the surrounding area, and a reasonable arrangement of the commercial district can effectively reduce light pollution at this location.

<!-- b000291 | prose | pages [21] -->
(2) the boundary between the city and suburbs, where the biodiversity indicators of the suburbs are greatly affected by light pollution, and an unreasonable layout at this location can lead to an overall increase in light pollution levels

<!-- b000292 | prose | pages [21] -->
Due to space limitations, we only optimized calculations for certain regions of the above two locations. The final layout is shown in the figure 14.

<!-- b000293 | furniture | pages [22] -->
Page 21 of 23

<!-- b000294 | furniture | pages [22] -->
Team # 2320131

<!-- b000295 | caption | pages [22] -->
Figure 14: Changes in the grid set after the intervention

<!-- b000296 | prose | pages [22] -->
We can observe that the commercial districts tend to cluster together in the downtown area. Subjectively speaking, this can reduce the impact of commercial areas on the surrounding environment, indicating the rationality of this optimization result. Similarly, in the transition zone between the city and the suburbs, the urban grids also tend to cluster together, which can reduce the ecological impact of the city on the suburbs. In addition, it is commonly believed that a reasonable city layout should consist of commercial areas, residential areas, and industrial areas in sequence from the center to the outskirts. Our optimization results are consistent with this layout, thus demonstrating practicality.

<!-- b000297 | prose | pages [22] -->
However, in practice, such optimization often faces great external resistance and requires significant costs. Therefore, we do not recommend using this method for optimization in a well-developed city. Nevertheless, we believe that this approach can be a reference for planning new cities.

<!-- b000298 | heading | pages [22] -->
8.2 Regulation or Compensation

<!-- b000299 | prose | pages [22] -->
By developing different strategy intensity factors, we can calculate different and . Using the Light Pollution Risk Assessment Model, we can calculate the and for different areas under the two strategies. The calculation results are shown in Fig.15.

<!-- b000300 | caption | pages [22] -->
Figure 15: Changes in various indicators across different regions under the influence of

<!-- b000301 | prose | pages [22] -->
different strategy factors

<!-- b000302 | prose | pages [22, 23] -->
It can be seen that the higher the intensity of the implementation of strategy II, the lower the risk level of light pollution in each region, i.e., the implementation of strategy II reduces the risk level of light pollution. With the increase of the intensity of the implementation of strategy III, the risk level of light pollution in each region decreases when the strategy intensity is small, but the decrease is much smaller than the decrease of the risk level caused by strategy II under the same strategy intensity. As the intensity of strategy III continues to increase, although the risk level in all other regions decreases, the risk level in urban commercial areas and suburban industrial areas rebounded. The specific analysis of the changes of each indicator reveals that this is due to the excessive taxation that hinder the economic development of some enterprises and factories in urban commercial areas and suburban industrial areas, and too much falling of the economic indicators makes the risk level of light pollution rebound in our model instead, which shows that the implementation intensity of strategy III should not be too high, but moderate.

<!-- b000303 | furniture | pages [23] -->
Page 22 of 23

<!-- b000304 | furniture | pages [23] -->
Team # 2320131

<!-- b000306 | prose | pages [23] -->
In short, strategy II has a greater impact on the level of risk of light pollution, while the impact of it is relatively large and positive all the time. The impact of strategy III on the level of risk of light pollution is mainly positive, but smaller than strategy II. And the excessive intensity will hinder economic development so it has a certain negative impact. Therefore, the supervision of the "principles of responsible outdoor lighting" the stronger the better, while the tax should be moderate, not too small and not too large. This is also consistent with our common sense of life, indicating that our model has a great deal of rationality.

<!-- b000307 | heading | pages [23] -->
9 Sensitivity Analysis

<!-- b000308 | prose | pages [23] -->
Since the weighting factors in the convolution kernel are chosen subjectively by reviewing the literature, and inappropriate parameter choices can affect the correctness of the model, we analyze the sensitivity of the light pollution coefficient of the urban commercial area to the surrounding raster. The light pollution coefficient of the urban commercial area used in the model is 0.05, so it is specified to vary between 0.04 and 0.06 in steps of 0.002 to analyze the effect of this variation on the level of light pollution risk.

<!-- b000309 | prose | pages [23] -->
Therefore, the calculation results are shown in Figure 16.

<!-- b000310 | prose | pages [23] -->
It can be seen that with the change of light pollution coefficient in the urban commercial area, the change of light pollution risk level is not obvious. In other words, the change of the subjectively selected coefficient in the model does not cause drastic changes in the model, which indicates that our model is stable. This also reflects the fact that the risk level of each grid depends mainly on its own indicators, instead of the surrounding grid. This result is consistent with our general perception.

<!-- b000311 | heading | pages [23] -->
10 Strengths and Weaknesses

<!-- b000312 | heading | pages [23] -->
10.1 Strengths

<!-- b000313 | prose | pages [23, 24] -->
The model divides the city into commercial, residential, and industrial areas based  on the city planning map, and separates suburban and rural areas into residential and industrial areas, fully considering the differences between various regions. The research results are widely applicable and can be used to evaluate the light pollution risk levels in various regions.

<!-- b000314 | furniture | pages [24] -->
Page 23 of 23

<!-- b000315 | furniture | pages [24] -->
Team # 2320131

<!-- b000317 | prose | pages [24] -->
The model adopts a grid-based approach to classify different regions, accurately  obtaining the light pollution risk level of each small area by calculating the indicators of each grid, making the model more accurate and targeted. Through convolutional calculations, the model quantifies the influence of each grid on its surrounding grids, taking into account that grids belonging to different types of regions have different impacts on the surrounding grids, making the model more comprehensive.

<!-- b000318 | prose | pages [24] -->
The model innovatively proposes urban layout planning strategies, providing new  ideas for future urban construction. Specific measures to reduce light pollution risk levels are provided from the perspectives of prevention and compensation, and the evaluation of strategies is in line with expectations.

<!-- b000319 | heading | pages [24] -->
10.2 Weaknesses

<!-- b000320 | prose | pages [24] -->
Due to the lack of data in the dataset, all indicators have been simplified, and the  influencing factors of the indicators need to be supplemented based on a more complete dataset. Only one region was specifically evaluated for light pollution risk, and the case studies are not sufficient.

<!-- b000321 | prose | pages [24] -->
The model is relatively complex and requires the collection of a large amount of  data from various sources. Moreover, due to the gridding process, the algorithm requires a large amount of computational resources, requiring significant human and material resources to implement.

<!-- b000322 | heading | pages [24] -->
References

<!-- b000323 | references | pages [24] -->
[1] Liu Ming, Zhang Baogang, Pan Xiaohan, et al. Research on Evaluation Indicators and

<!-- b000324 | references | pages [24] -->
Methods for Light Pollution in Urban Lighting Planning[J]. Journal of Illuminating

<!-- b000325 | references | pages [24] -->
Engineering, 2012, 23(4): 22-27.

<!-- b000326 | references | pages [24] -->
[2] Hu Jiayu. Evaluation and Prevention of Light Pollution in Night Scenery Lighting of

<!-- b000327 | references | pages [24] -->
Xi'an Main Urban Area [D]. Xi'an University of Architecture and Technology, 2015.

<!-- b000328 | references | pages [24] -->
[3] Riegel K W. Light Pollution: Outdoor lighting is a growing threat to astronomy[J].

<!-- b000329 | references | pages [24] -->
Science, 1973, 179(4080): 1285-1291.

<!-- b000330 | references | pages [24] -->
[4] Stone T. Light pollution: A case study in framing an environmental problem[J]. Ethics,

<!-- b000331 | references | pages [24] -->
Policy & Environment, 2017, 20(3): 279-293.

<!-- b000332 | references | pages [24] -->
[5] Gallaway T, Olsen R N, Mitchell D M. The economics of global light pollution[J].

<!-- b000333 | references | pages [24] -->
Ecological economics, 2010, 69(3): 658-665.

<!-- b000334 | references | pages [24] -->
[6] Centers for Disease Control and Prevention https://www.cdc.gov/

<!-- b000335 | references | pages [25] -->
2

<!-- b000336 | references | pages [25] -->
Restore the Starry Sky

<!-- b000337 | heading | pages [25] -->
Background

<!-- b000338 | prose | pages [25] -->
Less than 100 years ago, everyone could look up and see a spectacular starry night sky. Now, due to the light pollution, millions of children across the globe will never experience the Milky Way where they live. 80 percent of the world's population lives under skyglow. In the United States and Europe 99 percent of the public can't experience a natural night!

<!-- b000339 | prose | pages [25] -->
What is light pollution?

<!-- b000340 | prose | pages [25] -->
The inappropriate or excessive use of artificial light – known as light Pollution . Components of it include : glare , skyglow, light trespass Liglt eraepoze Giare zone and clutter . The definition of them are show in the figure beside. Diract gicra isok1 kghe A

<!-- b000341 | prose | pages [25] -->
How Bad is Light Pollution?

<!-- b000342 | prose | pages [25] -->
According to research, light pollution has caused :

<!-- b000343 | prose | pages [25] -->
Effecting crime and safety Disrupting the ecosystem

<!-- b000344 | prose | pages [25] -->
Increasing energy consumption Harming human health

<!-- b000345 | prose | pages [25] -->
Take Action ! In order to restore the disappearing stars, we have developed mathematical models and made case studies to come up with fruitful policy recommendations , which can reduce light pollution by approximately 23.17% at the source. Therefore, we are now calling on everyone to act together to support the implementation of these following measures!

<!-- b000346 | prose | pages [25] -->
All light should have a clear purpose. Before installing or replacing a light, determine if light is really needed and think more about the ecological, health and energy impacts of this light. Preventing light pollution starts with small daily tasks.

<!-- b000347 | prose | pages [25] -->
Consider using reflective paints or self-luminous markers for signs, curbs, and steps to reduce the need for permanently installed outdoor lighting as well as save energy.

<!-- b000348 | prose | pages [25] -->
We recommend that the government urge companies to use controls such as timers or motion detectors to ensure that light is available when it is needed, dimmed when possible, and turned off when not needed.

<!-- b000349 | prose | pages [25] -->
Limit the amount of shorter wavelength (blue-violet) light to the least amount needed.

<!-- b000350 | prose | pages [25] -->
Light where you need it, when you need it, in the amount needed, and no more.

<!-- b000351 | prose | pages [25] -->
The government also needs to regulate everyone to use shielding and careful aiming to target the direction of the light beam so that it points downward and does not spill beyond where it is needed.
