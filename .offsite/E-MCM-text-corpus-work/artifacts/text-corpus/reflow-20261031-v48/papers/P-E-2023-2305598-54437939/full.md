# P-E-2023-2305598-54437939

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
2305598

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Turn out the Lights, Turn up the Stars

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Light pollution is a type of environmental pollution caused by human activities, which has negative impacts on wildlife, plants, and human health. With the continuous development of urbanization and industrialization, the problem of light pollution is becoming increasingly se- vere. Therefore, the evaluation and improvement of the risk level of light pollution is particu- larly important.

<!-- b000010 | prose | pages [1] -->
Firstly, we collected data on ten indicators from 55 regions and divided these ten indicators into three areas: Light, Society, and Nature. Then we combined the analytic hierarchy process, entropy weight method, and coefficient of variation method to calculate the combined weights of these indicators to construct the formula of light pollution index (LPI) and then build the LSN evaluation model. Finally, we use fuzzy cluster analysis to classify all locations into four categories, thus dividing the light pollution level into four classes.

<!-- b000011 | prose | pages [1] -->
Secondly, we choose New York City, Bellevue, Sedona and Yellowstone National Park as a representative of each location type. Using the LSN evaluation model, their LPI were cal- culated to be 35.55, 41.33, 76.94, 84.18. Thus, their light pollution levels were obtained as Grade I, Grade II, Grade III, Grade IV respectively.

<!-- b000012 | prose | pages [1] -->
Thirdly, we proposed three intervention strategies and their specific actions, constructed a PIA-NN model, and studied the potential effects of concrete actions on light pollution effects. The three intervention strategies are: reduce artificial light intensity & strengthen publicity and education & expand vegetation area. We quantitatively reflected the "potential impact" of the three intervention strategies on the light pollution effect by combining Spielman's correlation coefficient and the BP neural network model.

<!-- b000013 | prose | pages [1] -->
Next, we selected two representative regions, Sedona and New York City, to explore the effects of three intervention strategies on light pollution levels in the two regions using the PIA-NN model and the LSN evaluation model. The results show that for both areas, reducing the intensity of artificial light is the most effective intervention strategy to reduce the risk level of light pollution.

<!-- b000014 | prose | pages [1] -->
Finally, we will choose New York City as the location for the campaign and design a beautiful flyer around its corresponding most effective intervention strategy.

<!-- b000015 | keywords | pages [1] -->
Keywords: LSN evaluation model; LPI; PIA-NN model; AHP

<!-- b000016 | furniture | pages [2] -->
Team # 2305598

<!-- b000017 | furniture | pages [2] -->
Page 2 of 24

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
1 Introduction ...................................................................................................... 3

<!-- b000020 | contents | pages [2] -->
1.1 Problem Background ....................................................................................................... 3

<!-- b000021 | contents | pages [2] -->
1.2 Our Work .......................................................................................................................... 3

<!-- b000022 | contents | pages [2] -->
2 Assumptions and Justifications ....................................................................... 4

<!-- b000023 | contents | pages [2] -->
3 Notations ........................................................................................................... 5

<!-- b000024 | contents | pages [2] -->
4 Light-Society-Nature (LSN)Evaluation Model ............................................. 5

<!-- b000025 | contents | pages [2] -->
4.1 Establishment of evaluation system ................................................................................. 6

<!-- b000026 | contents | pages [2] -->
4.2 Determination of the Weights for Indicators .................................................................... 9

<!-- b000027 | contents | pages [2] -->
4.3 The establishment of LSN Evaluation Model ................................................................ 12

<!-- b000028 | contents | pages [2] -->
4.4 The Application of LSN Evaluation Model ................................................................... 13

<!-- b000029 | contents | pages [2] -->
5 Possible intervention strategies ..................................................................... 16

<!-- b000030 | contents | pages [2] -->
5.1 Strategy proposal and specific actions ........................................................................... 16

<!-- b000031 | contents | pages [2] -->
5.2 Potential impact analysis- Neural Network (PIA-NN) Model ....................................... 17

<!-- b000032 | contents | pages [2] -->
6 Which strategy works best? .......................................................................... 19

<!-- b000033 | contents | pages [2] -->
6.1 The result of Sedona, Arizona ........................................................................................ 20

<!-- b000034 | contents | pages [2] -->
6.2 The result of New York City, New York ........................................................................ 20

<!-- b000035 | contents | pages [2] -->
6.3 Final result ..................................................................................................................... 21

<!-- b000036 | contents | pages [2] -->
7 Sensitivity Analysis ......................................................................................... 21

<!-- b000037 | contents | pages [2] -->
8 Model Evaluation and Further Discussion .................................................. 22

<!-- b000038 | contents | pages [2] -->
8.1 Strengths ........................................................................................................................ 22

<!-- b000039 | contents | pages [2] -->
8.2 Weaknesses .................................................................................................................... 23

<!-- b000040 | contents | pages [2] -->
8.3 Further Discussion ......................................................................................................... 23

<!-- b000041 | contents | pages [2] -->
9 Conclusion ....................................................................................................... 23

<!-- b000042 | contents | pages [2] -->
References .......................................................................................................... 24

<!-- b000043 | furniture | pages [3] -->
Team # 2305598

<!-- b000044 | furniture | pages [3] -->
Page 3 of 24

<!-- b000045 | heading | pages [3] -->
1 Introduction

<!-- b000046 | heading | pages [3] -->
1.1 Problem Background

<!-- b000047 | prose | pages [3] -->
Light pollution was first raised by astronomers in the 1950s.[1] With the acceleration of urbanization and economic development, the demand for night lighting gradually increased. At the same time, humans overuse or use artificial light sources unreasonably at night, which de- stroys the natural darkness. According to data from the International Dark-Sky Association, over 80% of the global population lives in areas affected by light pollution,[2] and about 99% of urban residents in Europe and the United States cannot observe the Milky Way at night.[3] In many large cities worldwide, the brightness at night can even reach the level of daytime.

<!-- b000048 | prose | pages [3] -->
The issue of light pollution is increasingly affecting people's daily lives, including work and leisure activities. It not only disrupts the beautiful view of our night sky but also has neg- ative impacts on human health, safety, and the ecological environment. According to astronom- ical studies, a clear sky free of light pollution can display around 7,000 stars, while only 20-60 stars are visible in large cities. Excessive artificial light at night can disturb the circadian rhythm of living organisms, leading to poor sleep quality and higher rates of insomnia. Moreover, ex- cessive light exposure to the human eye can damage the retina and iris, resulting in a sharp decline in vision. High beam lights on well-lit city streets can also cause transient "visual loss" to pedestrians or drivers on the opposite side of the street, contributing to a higher incidence of traffic accidents. Additionally, light pollution can also alter the growth cycle of plants and affect the migration patterns of wildlife.

<!-- b000049 | prose | pages [3] -->
Therefore, the issue of light pollution requires urgent attention and regulation globally

<!-- b000050 | heading | pages [3] -->
1.2 Our Work

<!-- b000051 | prose | pages [3] -->
First, we propose the Light-Society-Nature (LSN) Evaluation Model, which is used to evaluate the light pollution risk level of a location. Specifically, the model considers many indicators reflecting light pollution. Based on these indicators, we establish a secondary eval- uation system. Considering that different methods have their limitations, the weights of the indicators are determined by a combination of the Analytic Hierarchy Process (AHP), Entropy Weight Method (EWM), and Coefficient of Variation Method (CVM). We select 55 representa- tive locations worldwide and calculate their light pollution index based on relevant data, and the different levels of light pollution were determined by fuzzy clustering.

<!-- b000052 | furniture | pages [4] -->
Team # 2305598

<!-- b000053 | furniture | pages [4] -->
Page 4 of 24

<!-- b000054 | prose | pages [4] -->
Second, we selected four different types of locations in the US and used the LSN evalua- tion model to calculate the light pollution index for each location, and analyzed the reasona- bleness of the results with the actual local conditions.

<!-- b000055 | prose | pages [4] -->
Then, in our previously constructed indicators, we have proposed three intervention strat- egies while taking into account their feasibility. For each intervention strategy, specific actions have been provided. We also build a PIA-NN model to analyze the potential impact of these actions on light pollution effects. The results will be visualized and analyzed for rationality.

<!-- b000056 | prose | pages [4] -->
Thereafter, we select two locations from Task 2 as our study subjects and use the PIA-NN model and the LSN evaluation model to analyze the impact of three intervention strategies on their light pollution risk levels, and make corresponding analyses.

<!-- b000057 | prose | pages [4] -->
Finally, we will choose New York City as the location for the campaign and design a beautiful flyer around its corresponding most effective intervention strategy.

<!-- b000058 | prose | pages [4] -->
Figure 1：The structure of our paper

<!-- b000059 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000060 | prose | pages [4] -->
Assumption1: In this paper, LPI (Light Pollution Index) is defined as the score of the light environment of a region. The higher the LPI value, the lower the level of light pollution in the region.

<!-- b000061 | prose | pages [4] -->
Justification: The lower the level of light pollution in an area, the better the light envi- ronment in that place. Depending on people's usage habits, it is common for better condi- tions to correspond to higher scores. Assumption2: In the correlation analysis, only factors with strong correlation are retained and factors with small correlation are removed.

<!-- b000062 | furniture | pages [5] -->
Team # 2305598

<!-- b000063 | furniture | pages [5] -->
Page 5 of 24

<!-- b000064 | prose | pages [5] -->
Justification: The factors affecting light pollution are complex. If factors of lesser rele- vance are also taken into account, it will make the study results less significant and may even produce misleading conclusions. Assumption3: Assume the data collected from the internet is true and reliable.

<!-- b000065 | prose | pages [5] -->
Justification: In the process of studying light pollution, we select the most typical areas in the world, so the extensiveness of the data is guaranteed; all data are obtained from the official website, so the reliability of the data is guaranteed

<!-- b000066 | heading | pages [5] -->
3 Notations

<!-- b000067 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000068 | caption | pages [5] -->
Table 1: Notations used in this paper

<!-- b000069 | heading | pages [5] -->
Symbol

<!-- b000070 | prose | pages [5] -->
Description Unit Value of Light - Value of Society - Value of Nature - km2 Value of the area Atmospheric transparency m Atmospheric humidity % Altitude feet Sunshine duration h km2 Green area Species of wild animals - Indicators weight % LPI Light Pollution Index - *Other symbols instructions will be given in the text.

<!-- b000071 | heading | pages [5] -->
4 Light-Society-Nature (LSN)Evaluation Model

<!-- b000072 | prose | pages [5] -->
In this section, we establish the Light-Society-Nature (LSN) Evaluation Model to measure the light pollution risk level of a location in a region broadly. Firstly, after determining indica- tors of every level, we established a comprehensive evaluation system.[4] And then the weight of each indicator is determined by the combined weight method. Finally, we calculated the Light-Pollution Index (LPI), so as to identify the light pollution risk level of a location.

<!-- b000073 | prose | pages [5] -->
Considering that the risk level of light pollution varies greatly in different locations within a large range, we should choose as small a location as possible, such as a community or a residential district, when discussing the risk level of light pollution, rather than choosing a large area such as a country or a city. Therefore, we screened 55 representative sites around the world and used relevant data of these 55 sites as the database of this paper. Based on this, we estab- lished the Light-Society-Nature (LSN) Evaluation Model.

<!-- b000074 | prose | pages [6] -->
校苑 校苑数

<!-- b000075 | furniture | pages [6] -->
校苑数模

<!-- b000076 | furniture | pages [6] -->
Team # 2305598

<!-- b000077 | furniture | pages [6] -->
Page 6 of 24

<!-- b000078 | heading | pages [6] -->
4.1 Establishment of evaluation system

<!-- b000079 | prose | pages [6] -->
校苑数模 After referring to a large number of previous studies and relevant papers, we summarized three key factors reflecting the risk level of light pollution: light factor (L), social factor (S) and natural factor (N), which were taken as the first-level indicators in the evaluation system. After further thinking and induction, we concretized the indicators and selected 10 specific 校苑 indicators as the second-level indicators in the evaluation system.[5] The specific evaluation 校苑数模 system is as follows, as shown in the Figure 2.

<!-- b000080 | prose | pages [6] -->
校苑数模 校 校苑数模 校苑数模 模

<!-- b000081 | caption | pages [6] -->
Figure 2: Evaluation system diagram

<!-- b000082 | heading | pages [6] -->
4.1.1 Light

<!-- b000083 | prose | pages [6] -->
The light factor is the most important factor in determining the risk level of light pollution. After a lot of literature review and rigorous analysis, we finally determined that the specific 校苑数模 light factor include the following four points: 苑数模 . Artificial light intensity Artificial light intensity refers to the brightness of light generated by human activities. In light pollution research, artificial light intensity is an important indicator, which is used to measure the intensity and influence of artificial light on the surrounding environment at night. Artificial light intensity is usually measured using photometers or related measuring instru-

<!-- b000084 | furniture | pages [6] -->
校苑数模

<!-- b000085 | prose | pages [6] -->
ments, and it is measured in units of candela/square meter (μcd/m²), indicating the brightness of the light source per unit area. The data of artificial light intensity can be obtained through the official website of Light pollution map.

<!-- b000086 | prose | pages [6] -->
. Artificial light density Artificial light density refers to the number of artificial lights in a certain location, usually 苑数模 expressed by the number of lights per unit area, such as the number of street lamps per square kilometer. High artificial light density means that there are more lights in an area. These lights

<!-- b000087 | prose | pages [6, 7] -->
模 will produce more artificial light at night. Therefore, artificial light density is one of the im- portant factors affecting light pollution.

<!-- b000088 | furniture | pages [7] -->
Team # 2305598

<!-- b000089 | furniture | pages [7] -->
Page 7 of 24

<!-- b000091 | prose | pages [7] -->
In order to facilitate the determination of the specific value of the artificial light density, we define that the artificial light density of a location can be expressed as the ratio of the arti- ficial light intensity ( ) to the area ( ) according to the understanding of its definition. The definition formula of is as follows:

<!-- b000092 | prose | pages [7] -->
(1)

<!-- b000093 | prose | pages [7] -->
Where can be available through national statistical yearbooks.

<!-- b000094 | prose | pages [7] -->
. Sky brightness

<!-- b000095 | prose | pages [7] -->
Sky brightness refers to the level of brightness visible in a region of the sky, usually ex- pressed in terms of luminous flux per unit area, such as moonlight or starlight flux per square meter. It is closely related to the light pollution. The more severe the light pollution is, the higher the sky brightness will be, which can reduce nighttime air transparency and obstruct starlight and moonlight.

<!-- b000096 | prose | pages [7] -->
The increase in sky brightness can have a negative impact on the biological environment and ecosystems. For example, it can affect the behavior and migration of nocturnal animals, interfere with plant growth and species reproduction, disrupt human circadian rhythms and physiological rhythms, and even affect human health.

<!-- b000097 | prose | pages [7] -->
Sky brightness in different regions can be obtained by using the Light Pollution Map web- site.

<!-- b000098 | prose | pages [7] -->
. Glare Glare refers to a visual state where an extremely bright light source, contrasting with the background, causes discomfort and reduces visibility for the eyes.[6] Glare has a significant impact on the level of light pollution, with higher glare values indicating more severe light pollution in an area, and lower glare values indicating a lower level of light pollution.

<!-- b000099 | prose | pages [7] -->
Glare is the most common in outdoor, such as in the glass curtain walls of buildings, which can produce intense glare under sunlight, significantly impacting people's safety, damaging the urban living environment, and potentially causing traffic safety hazards.

<!-- b000100 | prose | pages [7] -->
According to the international common glare calculation formula, and combined with the understanding of the meaning of glare, the value of is determined by the following formula:

<!-- b000101 | prose | pages [7] -->
(2)

<!-- b000102 | heading | pages [7] -->
4.1.2 Society

<!-- b000103 | prose | pages [7] -->
Social factors are one of the important influencing factors of light pollution. Social factors include regional population, level of regional development, education, and publicity efforts, among many other aspects. These factors affect people's awareness and attitudes toward light pollution, thus influencing their behavior. When establishing an evaluation system for light pollution, social factors are essential part.

<!-- b000104 | prose | pages [7, 8] -->
. Population The population of an area refers to the number of people living in a particular region, which is closely related to light pollution. On one hand, as the population increases, the demand for lighting also increases. On the other hand, the population also determines the scope of light pollution. Generally, areas with a larger population have higher levels of artificial light source density and light pollution. Conversely, in areas with a smaller population, the degree of light pollution may be relatively lower.

<!-- b000105 | furniture | pages [8] -->
Team # 2305598

<!-- b000106 | furniture | pages [8] -->
Page 8 of 24

<!-- b000108 | prose | pages [8] -->
Population data for different areas can be obtained from national statistical yearbooks of various countries.

<!-- b000109 | prose | pages [8] -->
. Development The level of regional development usually refers to the economic, social, and environ- mental development level, which can be measured by indicators such as GDP.

<!-- b000110 | prose | pages [8] -->
The GDP of different regions can be obtained from the national statistical yearbooks of various countries.

<!-- b000111 | prose | pages [8] -->
However, it should be noted that increasing the level of regional development does not necessarily lead to a higher level of light pollution. Developed urban areas often have more artificial light sources and higher light intensity, but they also have more advanced technology and management methods, which can effectively control light pollution problems. On the other hand, regions with lower levels of development may lack sufficient technology and funding to control light pollution, which can lead to higher levels of light pollution.

<!-- b000112 | prose | pages [8] -->
. Propaganda and education An area's level of education and publicity regarding light pollution typically refers to the extent of promotion and education on light pollution in that area. This includes the dissemina- tion of knowledge on light pollution, its harmful effects, and prevention measures. Stronger promotion and education can increase public awareness of light pollution, increase attention to light pollution, and thus reduce light pollution in the area.

<!-- b000113 | prose | pages [8] -->
To quantitatively describe the extent of an area's education and publicity on light pollution, we use public attention to light pollution as a measure. This can be achieved by calculating the number of searches related to light pollution keywords on Google Trends in the area.

<!-- b000114 | heading | pages [8] -->
4.1.3 Nature

<!-- b000115 | prose | pages [8] -->
Natural factors have a close relationship with light pollution. The impact of natural factors on light pollution mainly includes aspects such as regional climate, geographical location, and biodiversity. When establishing an evaluation system for light pollution, it is necessary to con- sider the natural environmental characteristics of the region and quantify the impact of natural factors on light pollution.

<!-- b000116 | prose | pages [8] -->
. Climate Climate refers to the long-term average weather conditions in a particular region, includ- ing atmospheric transparency, humidity, temperature, and air pressure.[7] The impact of climate on light pollution is complex. We refer to previous research and select atmospheric transpar- ency ( ) and humidity ( ) as the main indicators for measuring the impact of climate factors on light pollution. The value of is determined by the following formula:

<!-- b000117 | prose | pages [8] -->
(3)

<!-- b000118 | prose | pages [8] -->
Where are obtained by standardizing the raw data obtained from the National Atmospheric Administration. The specific standardization formula is as follows:

<!-- b000119 | prose | pages [8, 9] -->
(4) (5)

<!-- b000120 | furniture | pages [9] -->
Team # 2305598

<!-- b000121 | furniture | pages [9] -->
Page 9 of 24

<!-- b000123 | prose | pages [9] -->
. Geography The geography of an area includes factors such as latitude, longitude, and altitude. These factors affect the local daylight hours, atmospheric density, topography, and other factors, which affect the local light pollution situation. For example, at high latitudes, the short daylight hours in winter require increased brightness and quantity of lighting facilities to maintain nor- mal production and living activities, which increases the risk of light pollution; while at higher altitudes, there are relatively fewer human activities and less artificial light at night, so the degree of light pollution is less. Accordingly, we selects altitude( ) and sunlight duration( ) as the main indicators to measure the influence of geographical location on the light pollution level. The value of is determined by the following formula:

<!-- b000124 | prose | pages [9] -->
(6)

<!-- b000125 | prose | pages [9] -->
Where are obtained by standardizing the raw data obtained from the Na- tional Atmospheric Administration. The specific standardization formula is as follows:

<!-- b000126 | prose | pages [9] -->
(7)

<!-- b000127 | prose | pages [9] -->
(8)

<!-- b000128 | prose | pages [9] -->
. Biodiversity Biodiversity refers to the variety of life forms in the area and is closely related to light pollution. Light pollution can cause damage to the ecosystem at night. At the same time, the loss of biodiversity can also exacerbate the effects of light pollution and lead to severe light pollution. Considering both animal and plant factors, we selected green areas ( ) and wildlife species ( ) as the main indicators of biodiversity. The value of is determined by the following formula:

<!-- b000129 | prose | pages [9] -->
(9)

<!-- b000130 | prose | pages [9] -->
Where and are available through the official website of the National For- estry Administration of each country.

<!-- b000131 | heading | pages [9] -->
4.2 Determination of the Weights for Indicators

<!-- b000132 | prose | pages [9] -->
There are many methods to determine the weight of indicators. To make our model more accurate, we decide to use the combination weighting method to calculate the weight of all indicators. Our combination weighting method combines Analytic Hierarchy Process (AHP) in the subjective weighting method and Entropy Weight Method (EWM) and the Coefficient of Variation Method (CVM) in the objective weighting method. Because the AHP judgment is more subjective, it is easy to change by the subjective influence of the decision maker. At the same time, because of the high sensitivity of the data, it may cause errors due to the data itself. Therefore, our combination weighting method synthesizes these methods to help us reduce errors and improve accuracy.

<!-- b000133 | prose | pages [10] -->
校苑 校苑数

<!-- b000134 | furniture | pages [10] -->
校苑数模

<!-- b000135 | furniture | pages [10] -->
Team # 2305598

<!-- b000136 | furniture | pages [10] -->
Page 10 of 24

<!-- b000137 | heading | pages [10] -->
4.2.1 Analytic Hierarchy Process

<!-- b000138 | prose | pages [10] -->
校苑数模 First, a hierarchy diagram is constructed based on the previously selected metrics, as shown in Figure 3 below.

<!-- b000139 | prose | pages [10] -->
校苑 校苑数模 校苑数模

<!-- b000140 | caption | pages [10] -->
Figure 3: Hierarchy diagram

<!-- b000141 | prose | pages [10] -->
校 Then we construct judgment matrices for the primary indicators and each set of secondary indicators separately:

<!-- b000142 | prose | pages [10] -->
校苑数模 Where represents the importance of relative to , while represent the quan- tity of indicators in each group. Because of the limited space, we will not show the judgment matrix.

<!-- b000143 | prose | pages [10] -->
Calculate the weight of each indicator and perform a consistency check. The weights of each indicator calculated by this method are denoted as . 校苑数模

<!-- b000144 | heading | pages [10] -->
4.2.2 Entropy Weight Method

<!-- b000145 | prose | pages [10] -->
First, the data of the indicators of 55 locations in the database are aggregated to form an 模 original matrix X. Because the types of indicators are different, we need to normalize the orig- inal matrix. Next, to eliminate the influence of dimensionality, we need to standardize the nor- malized matrix, and then we get the matrix Y. We combine the normalization and standardiza- 校苑数模 tion process of indicators in this paper, and the specific calculation formula is as follows:

<!-- b000146 | prose | pages [10] -->
苑数模 Positive indicators: (10)

<!-- b000147 | prose | pages [10] -->
Negative indicators: (11)

<!-- b000148 | prose | pages [10] -->
Where , represents the th indicator of the th region in the pre- vious evaluation system.

<!-- b000149 | furniture | pages [10] -->
校苑数模

<!-- b000150 | prose | pages [10] -->
Then, we use the Entropy Weight Method (EWM) to calculate the weight of the indicators.

<!-- b000151 | prose | pages [10] -->
We calculate the probability matrix .

<!-- b000152 | prose | pages [10] -->
According to the concepts of self-information and entropy in the information theory, we can calculate the information entropy of each evaluation indicator, hence we can obtain:

<!-- b000153 | prose | pages [10] -->
(12) 苑数模 Let , which is define as the information utility value. The entropy weight of

<!-- b000154 | prose | pages [10, 11] -->
模 校苑 校苑数

<!-- b000156 | furniture | pages [11] -->
校苑数模

<!-- b000157 | furniture | pages [11] -->
Team # 2305598

<!-- b000158 | furniture | pages [11] -->
Page 11 of 24

<!-- b000159 | prose | pages [11] -->
each indicator is given by normalizing the information utility value in the following. The nor- 校苑数模 malization is determined by the following equation:

<!-- b000160 | prose | pages [11] -->
(13)

<!-- b000161 | prose | pages [11] -->
The weights of each indicator calculated by this method are denoted as . 校苑 校苑数模

<!-- b000162 | heading | pages [11] -->
4.2.3 Coefficient of Variation Method

<!-- b000163 | prose | pages [11] -->
Furthermore, we apply Coefficient of Variation Method (CVM) to weight our indicators.

<!-- b000164 | prose | pages [11] -->
First, normalize the original matrix to obtain the matrix .

<!-- b000165 | prose | pages [11] -->
Then, based on the previous database, we find the mean and standard deviation for the 55 data of each index, so that the coefficient of variation can be calculated as follows:

<!-- b000166 | prose | pages [11] -->
校苑数模 (14)

<!-- b000167 | prose | pages [11] -->
Finally, normalize the coefficient of variation to get the weights of each index:

<!-- b000168 | prose | pages [11] -->
校 (15)

<!-- b000169 | prose | pages [11] -->
The weights of each indicator calculated by this method are denoted as .

<!-- b000170 | prose | pages [11] -->
校苑数模

<!-- b000171 | heading | pages [11] -->
4.2.4 Combination weight

<!-- b000172 | prose | pages [11] -->
By the above three methods, we calculated three different weights ( , , ) for each indicator. To make the model more accurate, we chose the mean value of the three weights as the final weights of each indicator to minimize the error.

<!-- b000173 | prose | pages [11] -->
(16) 校苑数模 The final results of the weights of each indicator are shown in Figure 4 below. 模 校苑数模 苑数模

<!-- b000174 | furniture | pages [11] -->
校苑数模

<!-- b000175 | prose | pages [11] -->
苑数模

<!-- b000176 | caption | pages [11] -->
Figure 4: The combination weight diagram of each indicator

<!-- b000177 | prose | pages [11] -->
模

<!-- b000178 | furniture | pages [12] -->
Team # 2305598

<!-- b000179 | furniture | pages [12] -->
Page 12 of 24

<!-- b000180 | heading | pages [12] -->
4.3 The establishment of LSN Evaluation Model

<!-- b000181 | prose | pages [12] -->
Considering the impact of Light, Society and Nature on light pollution, we developed the LSN Evaluation Model. In this model, we introduce LPI (Light Pollution Index) to quantita- tively describe the risk level of light pollution. In addition, according to the selected database, we divided the values of LPI into four intervals by fuzzy cluster analysis, in other words, the light pollution risk level is divided into four levels.

<!-- b000182 | heading | pages [12] -->
4.3.1 Calculation of Light Pollution Index（LPI）

<!-- b000183 | prose | pages [12] -->
After the previous efforts, we can know the data source of each indicator and its calcula- tion method. The weight of each indicator is obtained by the combination weighting method. The weights corresponding to indicators L, S, and N are regarded as the extent of the influence of these three indicators on LPI, that means, the greater the weight, the more serious the influ- ence of the corresponding indicator on LPI. Accordingly, this paper reasonably and extremely creatively constructs the formula for calculating LPI:

<!-- b000184 | prose | pages [12] -->
(17) Similarly, based on the same lines, we construct the formulae for L, S, and N:

<!-- b000185 | prose | pages [12] -->
(18)

<!-- b000186 | prose | pages [12] -->
Where are obtained by standardizing in the previous 4.1.1

<!-- b000187 | heading | pages [12] -->
4.3.2 Determination of light pollution risk levels

<!-- b000188 | prose | pages [12] -->
The data of 55 typical locations in the previous paper were put into the LSN model to calculate the LPI values of each location. Then, using fuzzy cluster analysis, all locations were divided into 4 categories, thus classifying the light pollution levels into 4 classes, defined as: Grade Ⅰ: Heavy pollution, Grade Ⅱ: Moderate pollution, Grade Ⅲ: Minimal pollution, and Grade Ⅳ: Unpolluted. The specific class classification is shown in the following table:

<!-- b000189 | caption | pages [12] -->
Table 2: Scale of light pollution

<!-- b000190 | prose | pages [12] -->
Grade Ⅰ Ⅱ Ⅲ Ⅳ Light pollution risk level Heavy pollution Moderate pollution Minimal pollution Unpolluted LPI <40 40~60 60~80 >80 As can be seen from the above table, according to the LPI value of a certain location, the risk level of light pollution at that location can be determined.

<!-- b000191 | prose | pages [12] -->
Grade I (Heavy pollution) locations have the most serious light pollution, and the intensity and density of artificial light are very high, such as the center of developed cities;

<!-- b000192 | prose | pages [12] -->
Grade II (Moderate pollution) locations have a moderate level of light pollution, such as the outskirts of cities industrial areas, and residential areas;

<!-- b000193 | prose | pages [12] -->
Grade III (Minimal pollution) locations have less light pollution phenomenon, such as the countryside or fields;

<!-- b000194 | prose | pages [12] -->
Grade IV(Unpolluted) locations, almost no light pollution phenomenon, and the area is mostly untouched by human activities, such as national parks and nature reserves.

<!-- b000195 | furniture | pages [13] -->
Team # 2305598

<!-- b000196 | furniture | pages [13] -->
Page 13 of 24

<!-- b000197 | heading | pages [13] -->
4.4 The Application of LSN Evaluation Model

<!-- b000198 | prose | pages [13] -->
In this section, we have selected four different types of locations within the United States based on the requirements of Task 2. We collected relevant indicator data and applied the es- tablished LSN model to determine the level of light pollution in each location.

<!-- b000199 | caption | pages [13] -->
Table 3: Location selection table

<!-- b000200 | prose | pages [13] -->
Type Location An urban community. New York City, New York A suburban community Bellevue, Washington A rural community Sedona, Arizona A protected land location Yellowstone National Park

<!-- b000201 | heading | pages [13] -->
4.4.1 Case Ⅰ：An urban community

<!-- b000202 | prose | pages [13] -->
Urban communities are densely populated areas with concentrated buildings and well- developed infrastructure, where people engage in economic activities and have a rich social life. We have selected New York City, New York as our research site and the relevant data are as follows:

<!-- b000203 | caption | pages [13] -->
Table 4: Data of New York City, New York

<!-- b000204 | prose | pages [13] -->
（km2） 1213.4 Artificial light intensity (μcd/m2) 11700 Sky brightness (mag./arc sec2) 17.4 Population 8336817 GDP ($) 95159 Wet (%) 65 Atmospheric transparency (miles) 6 Altitude (feet) 16 Sunshine time (h) 2055 (km2) 20 37

<!-- b000205 | prose | pages [13] -->
Put the above data into the LSN Evaluation Model, the LPI value for New York City is 35.55, which falls under Grade I, indicating a very severe level of light pollution.

<!-- b000206 | prose | pages [13] -->
New York City has high population density and urban infrastructure. High population den- sity means that there are many sources of artificial light in the city, including streetlights, build- ing lights, and illuminated signs. The tall buildings reflect and scatter light, creating a phenom- enon known as skyglow, which also increases the level of light pollution. Another factor con- tributing to light pollution in New York City is the city's role as a hub of economic and cultural activity. Many businesses, cultural institutions, and public spaces in the city are open late into the night, and the city's tourism industry also relies heavily on well-lit attractions and landmarks. This means that the city requires a lot of outdoor lighting, which can be a significant source of light pollution.

<!-- b000207 | heading | pages [13] -->
4.4.2 Case Ⅱ：A suburban community

<!-- b000208 | prose | pages [13, 14] -->
A suburban community is an area that is typically located on the outskirts of a larger urban area. It is a mix of residential and commercial development. Suburban communities often have low to moderate population density, single-family homes, and their proximity to larger urban areas. Therefore, they fall into the category of moderate brightness environment. We have cho- sen Bellevue, Washington as the study location, and its relevant data are as follows:

<!-- b000209 | furniture | pages [14] -->
Team # 2305598

<!-- b000210 | furniture | pages [14] -->
Page 14 of 24

<!-- b000212 | caption | pages [14] -->
Table 5: Data of Bellevue, Washington

<!-- b000213 | prose | pages [14] -->
（km2） 94.5 Artificial light intensity (μcd/m2) 3420 Sky brightness (mag./arc sec2) 18.7 Population 147599 GDP ($) 72357 Wet (%) 75 Atmospheric transparency (miles) 8 Altitude (feet) 62 Sunshine time (h) 1778 (km2) 53 57

<!-- b000214 | prose | pages [14] -->
By inputting the above data into the LSN Evaluation Model, the LPI value for Bellevue, Washington is 41.33, which corresponds to Grade II. That means Bellevue has moderate levels of light pollution.

<!-- b000215 | prose | pages [14] -->
Although suburban areas have located some distance from the city center, they are the best choice for people who want to move away from crowded urban areas. This has led to a rising population in the suburbs and an increasing amount of artificial lighting outdoors, which inev- itably leads to a degree of light pollution.

<!-- b000216 | heading | pages [14] -->
4.4.3 Case Ⅲ：A rural community

<!-- b000217 | prose | pages [14] -->
A rural community is an area outside of an urban or suburban area. It is typically charac- terized by open spaces, natural landscapes, and smaller population densities, and includes small towns, villages, and remote areas. Rural communities have limited access to modern infrastruc- ture and services and are therefore low luminance environmental zones. We selected Sedona, Arizona as the study area with the following relevant data:

<!-- b000218 | caption | pages [14] -->
Table 6: Data of Sedona, Arizona

<!-- b000219 | prose | pages [14, 15] -->
（km2） 49.7 Artificial light intensity (μcd/m2) 90.6 Sky brightness (mag./arc sec2) 21.54 Population 10356 GDP ($) 48385 Wet (%) 45 Atmospheric transparency (miles) 120 Altitude (feet) 1344 Sunshine time (h) 278 (km2) 58 35 Substituting the above data into the LSN Evaluation Model, we obtained the LPI value of 76.94 for Sedona, Arizona, which corresponds to Grade Ⅲ. That means Sedona has less light pollution.

<!-- b000220 | furniture | pages [15] -->
Team # 2305598

<!-- b000221 | furniture | pages [15] -->
Page 15 of 24

<!-- b000223 | prose | pages [15] -->
This is due to its distance from major cities and low population density. However, as cities expand and demand for outdoor lighting increases in rural areas, even rural communities are beginning to be affected by light pollution. Such as the proliferation of LED lighting in rural areas has contributed to an increase in light pollution and disrupt natural sleep patterns in hu- mans and wildlife.

<!-- b000224 | heading | pages [15] -->
4.4.4 Case Ⅳ：A protected land location

<!-- b000225 | prose | pages [15] -->
On protected lands, there is little to no permanent population, so the intensity and density of artificial light are low, and they are almost unaffected by light pollution. These are natural dark environments, such as national parks and nature reserves.

<!-- b000226 | prose | pages [15] -->
Yellowstone National Park is a national park in the western United States, primarily lo- cated in Wyoming. It was established in 1872 and is the world's first national park. Yellowstone National Park is a haven for outdoor enthusiasts and is also an International Dark Sky Park. Therefore, we have selected Yellowstone National Park as our study site, and the relevant data is as follows:

<!-- b000227 | caption | pages [15] -->
Table 7: Data of Yellowstone National Park

<!-- b000228 | prose | pages [15] -->
（km2） 8983 Artificial light intensity (μcd/m2) 1.46 Sky brightness (mag./arc sec2) 21.99 Population 0 GDP ($) 0 Wet (%) 65 Atmospheric transparency (miles) 150 Altitude (feet) 2546 Sunshine time (h) 250 (km2) 93 67

<!-- b000229 | prose | pages [15] -->
When we input the above data into the LSN Evaluation Model, we obtain an LPI value of 84.18 for Yellowstone National Park, which is a high value and corresponds to Grade IV. This indicates that the park enjoys a good light environment and is minimally affected by light pol- lution.

<!-- b000230 | prose | pages [15] -->
This is consistent with the fact that, as a key protected area, Yellowstone National Park has made many efforts to reduce light pollution in the park to protect the natural environment at night, such as turning off non-essential lights at night, encouraging visitors to use red-filtered flashlights, which are less disruptive to wildlife and humans. As a result, the park can maintain a natural nighttime environment.

<!-- b000231 | furniture | pages [16] -->
Team # 2305598

<!-- b000232 | furniture | pages [16] -->
Page 16 of 24

<!-- b000233 | heading | pages [16] -->
5 Possible intervention strategies

<!-- b000234 | prose | pages [16] -->
Light pollution is an increasingly severe problem that affects people's production and lives. Light pollution alters our view of the night sky, has environmental impacts and affects our health and safety. To mitigate the negative effects of light pollution, we propose three possible intervention strategies and indicates their specific actions. Then, we constructed the PIA-NN Model based on the Spearman correlation coefficient and BP neural network model, which is used to analyze the potential impact of these specific actions on the light pollution effect.

<!-- b000235 | heading | pages [16] -->
5.1 Strategy proposal and specific actions

<!-- b000236 | prose | pages [16] -->
From the evaluation system constructed in the previous paper, the most significant factors affecting light pollution levels are Light, Society, and Nature, which are divided into ten spe- cific indicators under them. We target three different indicators and consider their applicability. Finally, we propose three intervention strategies and their specific actions to address the light pollution problem.

<!-- b000237 | heading | pages [16] -->
5.1.1 Strategy Ⅰ: Reduce artificial light intensity

<!-- b000238 | prose | pages [16] -->
Too much artificial light intensity will make the sky bright at night. This not only affects human circadian rhythms and health but also impacts the feeding and migration of wildlife, thus disrupting the ecological balance. Therefore, reducing the artificial light intensity in a given area can greatly alleviate light pollution and mitigate its harmful effects.

<!-- b000239 | prose | pages [16] -->
To reduce artificial light intensity, specific actions can be taken:

<!-- b000240 | prose | pages [16] -->
⚫ Optimizing lighting equipment: Replace high-power lighting equipment with low- power LED lights; Use sound-activated sensor lights in residential areas and building corridors.

<!-- b000241 | prose | pages [16] -->
⚫ Regulating lighting usage: Restrict lighting equipment to necessary areas, such as indoor areas and areas that require night safety; Remove lighting equipment in sub- urban and rural areas where there are no residents.

<!-- b000242 | prose | pages [16] -->
⚫ Reducing nighttime activities: Try to minimize large-scale gatherings and celebra- tions at night, or reduce their scale and frequency.

<!-- b000243 | prose | pages [16] -->
⚫ Smart city planning: In urban planning, design lamps to be shielded and direct light only to the areas that require lighting, without dispersing light to the surrounding en- vironment..

<!-- b000244 | heading | pages [16] -->
5.1.2 Strategy Ⅱ：Strengthen publicity and education

<!-- b000245 | prose | pages [16] -->
We can increase public awareness of light pollution through education and promote con- cern for its harmful effects. This will encourage the public to participate in light pollution pre- vention, ultimately relieving the problem. To enhance our efforts, we can take the following actions:

<!-- b000246 | prose | pages [16] -->
⚫ Post informational posters: Display posters in public areas, communities, and schools to educate the public on light pollution and raise awareness.

<!-- b000247 | prose | pages [16] -->
⚫ Host community events: Conduct promotional events in the community, such as lec- tures, seminars, and exhibitions, to help the public understand the impact of artificial light pollution and ways to reduce it.

<!-- b000248 | prose | pages [16, 17] -->
⚫ Utilize media outreach: Use various media channels, such as TV, radio, newspapers, magazines, and the internet, to promote the importance of reducing light pollution and its harmful effects.

<!-- b000249 | furniture | pages [17] -->
Team # 2305598

<!-- b000250 | furniture | pages [17] -->
Page 17 of 24

<!-- b000252 | prose | pages [17] -->
⚫ Strengthen school education: Provide knowledge and methods on light pollution to students through school courses, campus bulletins, and instructional videos to encour- age them to be proactive participants and advocates for environmental protection.

<!-- b000253 | heading | pages [17] -->
5.1.3 Strategy Ⅲ：Expand vegetation area

<!-- b000254 | prose | pages [17] -->
Expanding vegetation area is an effective way to reduce light pollution, as vegetation can block and absorb it. Vegetation can absorb certain wavelengths of light pollution, as well as reflect and scatter light, thus reducing the degree of light pollution. The larger the leaf area and density of vegetation, the stronger the absorption and reflection of light pollution. Therefore, expanding vegetation area can address light pollution. Here are some specific actions for ex- panding vegetation coverage:

<!-- b000255 | prose | pages [17] -->
⚫ Tree planting: Planting various types of trees in urban and rural areas can increase vegetation coverage and ease light pollution.

<!-- b000256 | prose | pages [17] -->
⚫ Greening buildings: In urban areas, planting trees, lawns, and other green vegetation on buildings and roads can increase urban vegetation coverage and reduce light pol- lution through reflection and scattering by vegetation.

<!-- b000257 | prose | pages [17] -->
⚫ Protect existing vegetation: Protecting existing forests, grasslands, wetlands, etc., and preventing excessive development and destruction, can maintain vegetation's al- leviation of light pollution.

<!-- b000258 | heading | pages [17] -->
5.2 Potential impact analysis- Neural Network (PIA-NN) Model

<!-- b000259 | prose | pages [17] -->
First, we identified three direct influencing factors: artificial light intensity, propaganda and education, and biodiversity, which will be directly affected by three intervention strategies.

<!-- b000260 | prose | pages [17] -->
Next, we calculated the Spearman correlation coefficients between each of the three direct influencing factors and other factors, and identified the indirect influencing factors that are closely related to each of them.

<!-- b000261 | prose | pages [17] -->
To analyze the potential impact of specific actions on the effects of light pollution, under- standing the changing trends and degrees of these indirect influencing factors is crucial.

<!-- b000262 | prose | pages [17] -->
To achieve this, we developed the Potential Impact Analysis-Neural Network (PIA- NN) Model. By building a neural network, we obtained the changing trends and degrees of the indirect influencing factors in response to the corresponding direct influencing factors, and analyzed the potential impact of specific actions on the effects of light pollution.

<!-- b000263 | heading | pages [17] -->
5.2.1 Establishment of model

<!-- b000264 | prose | pages [17] -->
To investigate the potential impact of specific actions on light pollution effects, it is first necessary to determine the influence of three direct influences on other light pollution factors. For this purpose, combined with the database of this paper, we develop the PIA-NN model.

<!-- b000265 | prose | pages [17] -->
To explore the relationship between the factors, we tested the normality of the factors and found that only the sky brightness data were normal.[8] Therefore, we chose Spearman's corre- lation coefficient to measure the correlation between the factors.[9] The specific calculation of Spearman's correlation coefficient is as follows:

<!-- b000266 | furniture | pages [18] -->
Team # 2305598

<!-- b000267 | furniture | pages [18] -->
Page 18 of 24

<!-- b000268 | prose | pages [18] -->
(19)

<!-- b000269 | prose | pages [18] -->
where is the sample size, and in this paper; denotes the equivalence difference between the two factor data.

<!-- b000270 | prose | pages [18] -->
From the calculation of Spearman's correlation coefficient, it can be seen that there is a significant positive correlation between artificial light intensity and artificial light density, glare and sky brightness, and a significant negative correlation with biodiversity. In addition, propa- ganda and education have a significant negative correlation with artificial light intensity, sky brightness, and glare, and a significant positive correlation with biodiversity. Finally, biodiver- sity has a significant positive correlation with sky brightness and glare.

<!-- b000271 | prose | pages [18] -->
After obtaining the correlations between the above three groups of corresponding factors, we used the Neural Fitting app in Matlab to establish three neural networks based on the pre- vious database, which are:

<!-- b000272 | prose | pages [18] -->
1. The neural network between artificial light intensity and artificial light density, glare, sky brightness, and biodiversity. (Strategy I) 2. The neural network between propaganda and education and artificial light intensity, sky brightness, glare, and biodiversity. (Strategy II) 3. The neural network between biodiversity and sky brightness and glare. (Strategy III) Through these three neural networks, we can clearly see the trend and degree of change of the corresponding indirect influences as the three direct influences change.

<!-- b000273 | heading | pages [18] -->
5.2.2 Result and Analysis

<!-- b000274 | prose | pages [18] -->
According to the above PIA-NN model, we obtained the trends of three groups of indirect influences with their corresponding direct influences, which are as follows:

<!-- b000275 | prose | pages [18] -->
(Strategy I) The trends of artificial light density, glare, sky brightness and biodiversity with artificial light intensity.

<!-- b000276 | prose | pages [18] -->
(Strategy II) The trends of artificial light intensity, sky brightness, glare and biodiversity with propaganda and education (Strategy III) Trends of sky brightness and glare with biodiversity.

<!-- b000277 | prose | pages [18] -->
The results are visualized in the following figures:

<!-- b000278 | prose | pages [18, 19] -->
(b): Strategy Ⅱ (a): Strategy Ⅰ (c): Strategy Ⅲ

<!-- b000279 | furniture | pages [19] -->
Team # 2305598

<!-- b000280 | furniture | pages [19] -->
Page 19 of 24

<!-- b000282 | caption | pages [19] -->
Figure 5: The result of PIA-NN

<!-- b000283 | prose | pages [19] -->
From the above figure we can conclude that:

<!-- b000284 | prose | pages [19] -->
From Figure(a), it can be seen that as the intensity of artificial light decreases, artificial light density, sky brightness and glare all decrease, with the most obvious decrease in sky brightness, followed by glare, and the weakest decrease in artificial light density, while at the same time, the biodiversity increases significantly. This indicates that the specific action of the first strategy will lead to darker nights, which further responds to the circadian rhythm of or- ganisms and improves the quality of people's sleep while providing a better ecological envi- ronment for wildlife; in addition, glare will be reduced and road traffic will be safer at night; and biodiversity will increase, indicating that the ecological environment of the area has im- proved and is more suitable for human, animal and plant life.

<!-- b000285 | prose | pages [19] -->
From Figure(b), it can be seen that with the increase in light pollution awareness and education, the artificial light intensity, sky brightness, and glare are significantly reduced, and the biodiversity still increases. This indicates that the specific actions of the second strategy will raise people's consciousness and actively participate in light pollution prevention actions, thus reducing artificial light intensity and giving the city a night and a starry sky; the reduction of glare can effectively reduce the incidence of people's eye diseases and thus have a positive impact on people's health; the increase of biodiversity can provide a better living environment for human beings.

<!-- b000286 | prose | pages [19] -->
From Figure (c), it can be seen that with the increase of biodiversity, there is a clear trend of decreasing both sky brightness and glare, with the degree of decrease of sky brightness being more obvious. This indicates that the specific actions of the third strategy have a potential im- pact similar to the first two cases, improving people's impression of the sky, reducing the inci- dence of traffic accidents, and bringing a positive impact on people's physical and mental health.

<!-- b000287 | heading | pages [19] -->
6 Which strategy works best?

<!-- b000288 | prose | pages [19] -->
In this section, we investigate the different effects of implementing the three intervention strategies separately for different regions. Based on the evaluation of light pollution levels in four different regions in the previous section 4.4, we selected two representative regions con- sidering the feasibility of intervention strategies in different regions. One is Sedona, Arizona, a rural community with low light pollution, and the other is New York City, New York, a large city with high light pollution, and we simulate the implementation of three different interven- tion strategies in these two areas.

<!-- b000289 | prose | pages [20] -->
校苑 校苑数

<!-- b000290 | furniture | pages [20] -->
校苑数模

<!-- b000291 | furniture | pages [20] -->
Team # 2305598

<!-- b000292 | furniture | pages [20] -->
Page 20 of 24

<!-- b000293 | prose | pages [20] -->
The three intervention strategies proposed in this paper will directly affect the three indi- 校苑数模 cators of artificial light intensity, publicity and education efforts, and biodiversity, respectively, and since there is a correlation between these three direct impact indicators and certain other indicators, changes in these three direct impact indicators will lead to changes in the corre- sponding indirect impact indicators, and we apply the three neural networks established in the previous paper to predict the changes in each group of indirect impact indicators. 校苑 校苑数模 The PIA-NN Model allows us to obtain the values of the indicators of the area after the implementation of the strategy and the achievement of the target. Finally, by comparing the LPI of the area before and after the implementation of the strategy, we can clearly see the impact of the strategy on the level of light pollution risk in the area.

<!-- b000294 | prose | pages [20] -->
In order to exclude the effect of time and intensity on the effect of the strategy, we set the predefined target for each strategy as: the strategy increases or decreases the corresponding 校苑数模 direct impact indicator by the same degree, e.g., 10% increase or decrease. This is used as the basis to calculate the LPI of the region after the implementation of the strategy. 校

<!-- b000295 | heading | pages [20] -->
6.1 The result of Sedona, Arizona

<!-- b000296 | prose | pages [20] -->
The results of implementing three different intervention strategies for Sedona, Arizona are 校苑数模 as follows:

<!-- b000297 | prose | pages [20] -->
校苑数模 模 校苑数模 苑数模

<!-- b000298 | caption | pages [20] -->
Figure 6: The result of Sedona, Arizona

<!-- b000299 | prose | pages [20] -->
The above graph shows that Strategy I was the most effective intervention for Sedona, Arizona. The community's LPI increased significantly when the target of Strategy I was 90%, i.e., when the implementation of Strategy I reduced the artificial light intensity to 90%. How-

<!-- b000300 | furniture | pages [20] -->
校苑数模

<!-- b000301 | prose | pages [20] -->
ever, it is worth noting that once the artificial light intensity increases, e.g., to 110%, the LPI in the area also decreases rapidly. Strategy II and Strategy III both have an increase in LPI, but not as much as Strategy I.

<!-- b000302 | heading | pages [20] -->
6.2 The result of New York City, New York

<!-- b000303 | prose | pages [20] -->
苑数模 The results of implementing three different intervention strategies for New York City, New York are as follows:

<!-- b000304 | prose | pages [20, 21] -->
模 校苑 校苑数

<!-- b000306 | furniture | pages [21] -->
校苑数模

<!-- b000307 | furniture | pages [21] -->
Team # 2305598

<!-- b000308 | furniture | pages [21] -->
Page 21 of 24

<!-- b000309 | prose | pages [21] -->
校苑数模 校苑 校苑数模

<!-- b000310 | caption | pages [21] -->
Figure 7: The result of New York City, New York

<!-- b000311 | prose | pages [21] -->
From the above figure we can see that the LPI of New York City, New York is very low 校苑数模 and it is in the severe light pollution class. Although the implementation of the three interven- tion strategies proposed in this paper will improve the LPI of New York City, New York, the 校 implementation of the strategies still puts New York City, New York in the severe light pollu- tion class. The LPI improves the fastest with a predetermined target of 90% for Strategy I. The implementation of Strategy II and Strategy III has little effect on the LPI values in this area, 校苑数模 but in comparison Strategy II is more effective than Strategy III.

<!-- b000312 | heading | pages [21] -->
6.3 Final result

<!-- b000313 | prose | pages [21] -->
Comparing the previous two figures, we can conclude that the implementation of Strategy I is the most effective in reducing light pollution in Sedona, Arizona and New York City, New 校苑数模 York with the same intended goal, but the difference is that the impact of Strategy I on New York City, New York is more obvious. The difference is that Strategy I has a more pronounced 模 effect on New York City, New York.

<!-- b000314 | prose | pages [21] -->
Strategy I is to prevent light pollution at the source. From the previous analysis, we can see that artificial light intensity is closely related to artificial light density, glare, and sky bright- ness, which are the main factors affecting light pollution and take up a large weight in the LSN 校苑数模 evaluation system, so reducing artificial light intensity has a significant effect on improving 苑数模 the LPI in the LSN evaluation system.

<!-- b000315 | heading | pages [21] -->
7 Sensitivity Analysis

<!-- b000316 | prose | pages [21] -->
In constructing the PIA-NN model, we verified the correlations among artificial light in- tensity, publicity and education efforts, biodiversity, and other indicators separately, and

<!-- b000317 | furniture | pages [21] -->
校苑数模

<!-- b000318 | prose | pages [21] -->
screened the relevant indicators to build the neural network. It is possible that the incomplete- ness of the consideration of the problem led to the neglect of some indicators related to artificial light intensity, publicity and education efforts, and biodiversity, which could have an impact. To test this possible influence, we reconstructed the neural network of artificial light intensity with glare, biodiversity, and sky brightness, and observed the relationship between the original 苑数模 model and this model with glare, biodiversity, and sky brightness by changing artificial light intensity. The results are as follows.

<!-- b000319 | prose | pages [21, 22] -->
模 (b): Biodiversity - Artificial light intensity

<!-- b000320 | furniture | pages [22] -->
Team # 2305598

<!-- b000321 | furniture | pages [22] -->
Page 22 of 24

<!-- b000323 | prose | pages [22] -->
(c): Sky brightness - Artificial light intensity (a): Glare - Artificial light intensity

<!-- b000324 | caption | pages [22] -->
Figure 8: The result of PIA-NN

<!-- b000325 | prose | pages [22] -->
As can be seen from the figure, after changing the artificial light intensity, the values of the three metrics predicted using the two neural networks before and after are relatively close. It shows that removing the indicator of artificial light density has almost no effect on the anal- ysis of glare, biodiversity, and sky brightness. It also shows that the unconsidered factor does not affect the analysis of existing factors and the model is robust.

<!-- b000326 | heading | pages [22] -->
8 Model Evaluation and Further Discussion

<!-- b000327 | heading | pages [22] -->
8.1 Strengths

<!-- b000328 | prose | pages [22] -->
⚫ To ensure the reliability of the results, the data used in this paper are the most accurate and up-to-date data available on the official website. In addition, various factors have been considered in an attempt to synthesize the problem. Therefore, the results of this paper are of a high reference value.

<!-- b000329 | prose | pages [22] -->
⚫ We have considered various indicators of light, social and natural aspects to make our evaluation model more comprehensive, accurate, and objective.

<!-- b000330 | prose | pages [22] -->
⚫ In this paper, the PIA-NN model is constructed in combination with a neural network model. In finding the correlation between indicators, the neural network approximates a continuous function of arbitrary complexity and arbitrary accuracy by a hidden layer containing enough neurons. Compared to other linear models, the neural network model has superior performance, making its results more accurate.

<!-- b000331 | prose | pages [22] -->
⚫ The results of our model are also consistent with common sense and experience.

<!-- b000332 | furniture | pages [23] -->
Team # 2305598

<!-- b000333 | furniture | pages [23] -->
Page 23 of 24

<!-- b000334 | heading | pages [23] -->
8.2 Weaknesses

<!-- b000335 | prose | pages [23] -->
⚫ Due to the limited time, only the data of 55 regions are selected as our database in this paper, and the LNS evaluation system is established, and the light pollution is roughly divided into four categories by fuzzy cluster analysis, but it is not clear the range of LPI values.

<!-- b000336 | prose | pages [23] -->
⚫ The data used in the model is incomplete. For objective reasons, we cannot obtain all the data of the required indicators, and these data inevitably have missing values.

<!-- b000337 | prose | pages [23] -->
Although we have taken care of the missing values, the accuracy of the model fit is still affected to some extent

<!-- b000338 | heading | pages [23] -->
8.3 Further Discussion

<!-- b000339 | prose | pages [23] -->
Since the database in this paper has only 55 regions, the classification of light pollution risk levels based on this database may have bias. Therefore, we can collect more data from different regions to form a database for analysis, and get more accurate and reasonable criteria for classifying light pollution risk levels.

<!-- b000340 | heading | pages [23] -->
9 Conclusion

<!-- b000341 | prose | pages [23] -->
This paper developed a broadly applicable evaluation model to identify the light pollution risk level of a location. We select 55 representative locations around the world and use the relevant data of these locations as the database of this paper. Brought all the data into LSN Evaluation Model to calculate the LPI value of each area, and then the 55 areas were divided into four classes by fuzzy cluster analysis, thus dividing the light pollution level into four grades, defined as: Grade I: Heavy pollution, Grade II: Moderate pollution, Grade III: Minimal pollution, Grade IV: Unpolluted.

<!-- b000342 | prose | pages [23] -->
Based on the above model, we choose New York City, Bellevue, Sedona and Yellowstone National Park as a representative of each location type. Their LPI values were calculated to be 35.55, 41.33, 76.94, 84.18. Thus, their light pollution risk levels were obtained as Grade I, Grade II, Grade III, Grade IV respectively.

<!-- b000343 | prose | pages [23] -->
To effectively address light pollution, we propose three possible intervention strategies and indicate specific actions. Finally, we construct a PIA-NN Model to analyze the potential impact of these specific actions on the light pollution effect.

<!-- b000344 | prose | pages [23] -->
Based on the above model, we choose Sedona and New York City as research subjects. Three different intervention strategies were simulated for these two areas separately. It was concluded that the implementation of Strategy I was the most effective in reducing light pol- luion levels in both areas.

<!-- b000345 | furniture | pages [24] -->
Team # 2305598

<!-- b000346 | furniture | pages [24] -->
Page 24 of 24

<!-- b000347 | heading | pages [24] -->
References

<!-- b000348 | references | pages [24] -->
[1] Liu Ming, Li Weishan, Hao Qingli, Guo Xiaowei. Review on monitoring methods and mod-

<!-- b000349 | references | pages [24] -->
els of urban night sky brightness [J]. Journal of Lighting Engineering,2017,28(03):45-50.

<!-- b000350 | references | pages [24] -->
[2] Falchi, Fabio, et al. "The new world atlas of artificial night sky brightness." Science ad-

<!-- b000351 | references | pages [24] -->
vances 2.6 (2016): e1600377.

<!-- b000352 | references | pages [24] -->
[3] Falchi, Fabio, et al. "The new world atlas of artificial night sky brightness." Science ad-

<!-- b000353 | references | pages [24] -->
vances 2.6 (2016): e1600377.

<!-- b000354 | references | pages [24] -->
[4] Liu Ming, Zhang Baogang, Pan Xiaohan, et al. Research on evaluation index and method

<!-- b000355 | references | pages [24] -->
of light pollution in urban lighting planning [J]. Journal of Lighting Engineer-

<!-- b000356 | references | pages [24] -->
ing,2012,23(4):22-27,55. (in Chinese) DOI:10.3969/j.issn.1004-440X.2012.04.004.

<!-- b000357 | references | pages [24] -->
[5] Cao Meng.Study on evaluation system of night light pollution in residential areas of Tianjin

<!-- b000358 | references | pages [24] -->
[D]. Tianjin: Tianjin University,2008. DOI:10.7666/d.y1531280.

<!-- b000359 | references | pages [24] -->
[6] Xu Qiaoyun. Research on glare Pollution Evaluation of building Glass Curtain Wall [J].

<!-- b000360 | references | pages [24] -->
Daily Appliances,2019(08):26-29.

<!-- b000361 | references | pages [24] -->
[7] Cinzano, P., Falchi, F., & Elvidge, C. D. (2001). The first world atlas of the artificial night

<!-- b000362 | references | pages [24] -->
sky brightness. Monthly Notices of the Royal Astronomical Society, 328(3), 689-707.

<!-- b000363 | references | pages [24] -->
[8] Kline R , Kline R B , Kline R . Principles and Practice of Structural Equation Modelling[J].

<!-- b000364 | references | pages [24] -->
Journal of the American Statistical Association, 2011, 101(12).

<!-- b000365 | references | pages [24] -->
[9] Hauke J, Kossowski T. Comparison of Values of Pearson's and Spearman's Correlation Co-

<!-- b000366 | references | pages [24] -->
efficients on the Same Sets of Data[J]. Quaestiones Geographicae, 2011, 30(2):87-93.

<!-- b000367 | references | pages [25] -->
TURNOUTTHELIGHTS

<!-- b000368 | references | pages [25] -->
TURN UP THE STARS

<!-- b000369 | references | pages [25] -->
Last time you saw stars?

<!-- b000370 | references | pages [25] -->
Too much light pollution

<!-- b000371 | references | pages [25] -->
washes out our night sky

<!-- b000372 | references | pages [25] -->
Light pollution affects

<!-- b000373 | references | pages [25] -->
our health and safty

<!-- b000374 | references | pages [25] -->
More than 80% of the world

<!-- b000375 | references | pages [25] -->
lives uder light-połluted sķies

<!-- b000376 | references | pages [25] -->
Disrüpts sleep før 50% of

<!-- b000377 | references | pages [25] -->
city dwellers.

<!-- b000378 | references | pages [25] -->
Address light pollution,

<!-- b000379 | references | pages [25] -->
●

<!-- b000380 | heading | pages [25] -->
3 STEPS!

<!-- b000381 | prose | pages [25] -->
1.Only light: if needed, when needed,& where needed.

<!-- b000382 | prose | pages [25] -->
2.Prefer LED: use warm-white oramber LEDlights 3.Downlighting:

<!-- b000383 | prose | pages [25] -->
keepit low &shielded

<!-- b000384 | prose | pages [25] -->
COMAP'S ILLUMINATION CONTROL MISSION (ICM)
