# P-E-2019-1903455-a52f7980

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only For office use only 1903455 T1 ________________ F1 ________________

<!-- b000003 | prose | pages [1] -->
T2 ________________ F2 ________________

<!-- b000004 | prose | pages [1] -->
T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________ E

<!-- b000005 | prose | pages [1] -->
2019 MCM/ICM

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Ecosystem services matters! Sustainability is necessary

<!-- b000008 | prose | pages [1] -->
Ecosystem services(ES) are the conditions and processes through which natural ecosystems and the species that make them up, sustain and fulfil human life (Daily, 1997). However, whenever humans alter the ecosystem, we potentially limit or remove ecosystem services. The impact of these projects of varying sizes may seem negligible to the total ability of the biosphere’s functioning potential, cumulatively they are directly impacting the biodiversity and causing environmental degradation. In order to understand the true economic costs of land use projects and propose sustainable development factor, we establish an Ecological Services Valuation Model.

<!-- b000009 | prose | pages [1] -->
To begin with, in order to measure the impact of ES numerically, we introduce MA classification method to make up the ecosystem services index(ESI). Furthermore, 11 indicators are selected from four aspects primarily, and then they are integrated into ESI by using entropy weight method (EWM) and coefficient of variation method (CVM). In addition, hierarchical clustering analysis(HCA) is applied to divide the ecosystem service intensity of the project into three categories: weak, moderate and strong. As a result, we found that private enterprise relocation project and house construction belongs to weak, factory construction project is determined to be moderate and national pipeline engineering has strong ecosystem service intensity.

<!-- b000010 | prose | pages [1] -->
Next, to calculate the true economic cost of land use projects, an Ecological Services Valuation Model is established. First, we analyze the impact of original cost on ES when the cost of ES is not taken into account. Then, we analyze the benefit and cost of land use project, on this basis, we find that the cost of ES has an important influence to the life cycle of a project. We also use support vector machine (SVM) to forecast the benefit-cost ratio of land use, the result shows that considering the cost of ES of project has the accumulation of a long life cycle and high efficiency. For private enterprise relocation project, without considering ES, we calculate that it reaches the maximum benefit-cost ratio in 2013, and predict that it will stop making profits in 2033. When ES is taken into account, the cost-benefit ratio of land use projects will gradually increase.

<!-- b000011 | prose | pages [1] -->
At last, for the sake of exploring the impact of sustainable development measures on ecosystem benefits, we divide the 11 three-level indicators into two categories: sustainable development indicators and unsustainable development indicators. After that, we introduce sustainable development factors  to describe the impact of different ecosystem service measures on the final development status of projects. Eventually, the values of  for four different size projects are PA =87.31, PB =88.4, PC =101.4, PD=11.98, it is obvious that  increases as the size of the project increases.

<!-- b000012 | prose | pages [1] -->
To conclude, We first construct the ecosystem service system, establish the Ecological Services Valuation Model and conduct the cost benefit analysis to four projects of varying sizes. What’s more, introduce the sustainable development factor to evaluate the development of land use projects and propose our suggestion for developing land use projects.

<!-- b000013 | keywords | pages [1] -->
Key words: Ecosystem services, ESVM, SVM, sustainable development factor

<!-- b000014 | furniture | pages [1] -->
关注数学模型

<!-- b000015 | furniture | pages [1] -->
2

<!-- b000016 | furniture | pages [1] -->
MATHmodels

<!-- b000017 | furniture | pages [1] -->
获取更多资讯

<!-- b000018 | heading | pages [2] -->
Content

<!-- b000019 | contents | pages [2] -->
1. Introduction ..................................................................................................... 1

<!-- b000020 | contents | pages [2] -->
1.1 Background ................................................................................................ 1

<!-- b000021 | contents | pages [2] -->
1.2 Our work .................................................................................................... 1

<!-- b000022 | contents | pages [2] -->
2. Assumptions and Justification .......................................................................... 2

<!-- b000023 | contents | pages [2] -->
3. Notations ......................................................................................................... 2

<!-- b000024 | contents | pages [2] -->
4. Ecological Services Analysis ........................................................................... 3

<!-- b000025 | contents | pages [2] -->
4.1 Ecological Services System(ESS) ............................................................... 3

<!-- b000026 | contents | pages [2] -->
4.2 Intensity evaluation .................................................................................... 7

<!-- b000027 | contents | pages [2] -->
5. Ecosystem Service Valuation Model ................................................................ 9

<!-- b000028 | contents | pages [2] -->
5.1 Cost-benefit analysis .................................................................................. 9

<!-- b000029 | contents | pages [2] -->
5.2 Prediction of Benefit-cost radio with SVM regression method .................. 12

<!-- b000030 | contents | pages [2] -->
5.3 Result analysis ......................................................................................... 14

<!-- b000031 | contents | pages [2] -->
6. Sustainable development analysis .................................................................. 15

<!-- b000032 | contents | pages [2] -->
6.1 Analysis of ecosystem services measures ................................................. 15

<!-- b000033 | contents | pages [2] -->
6.2 Influence of Sustainability on benefit-cost ratio ........................................ 16

<!-- b000034 | contents | pages [2] -->
7. Sensitivity Analysis ....................................................................................... 18

<!-- b000035 | contents | pages [2] -->
8. Advice on project planning and management ................................................. 19

<!-- b000036 | contents | pages [2] -->
9. Conclusion..................................................................................................... 20

<!-- b000037 | contents | pages [2] -->
9.1 Strengths .................................................................................................. 20

<!-- b000038 | contents | pages [2] -->
9.2 Weaknesses .............................................................................................. 20

<!-- b000039 | contents | pages [2] -->
References ......................................................................................................... 21

<!-- b000040 | furniture | pages [2] -->
关注数学模型

<!-- b000041 | furniture | pages [2] -->
2

<!-- b000042 | furniture | pages [2] -->
MATHmodels

<!-- b000043 | furniture | pages [2] -->
获取更多资讯

<!-- b000044 | furniture | pages [3] -->
Team#1903455                                                 Page 1 of 21

<!-- b000045 | heading | pages [3] -->
1. Introduction

<!-- b000046 | heading | pages [3] -->
1.1 Background

<!-- b000047 | prose | pages [3] -->
Ecosystem is the foundation of human survival and development. It not only provides space for human survival, but also provides various resources needed for human development, and absorbs waste generated by human production and life. Land resources are the main component of natural resources, and its position in production determines that land development and utilization is a major project. However, most land use projects do not consider the impact of ecosystem services. Although these activities may seem inconsequential to the total ability of the biosphere, they cumulatively directly affect the biodiversity and lead to environmental degradation. Therefore, how to evaluate the environmental cost of land use development projects and determine the real valuation of projects is worth our consideration

<!-- b000048 | heading | pages [3] -->
1.2 Our work

<!-- b000049 | prose | pages [3] -->
For the sake of understanding the real economic costs of land use projects in ecosystem services, we are required to establish an ecological services valuation model which determines a project’s quality. By selecting appropriate evaluation indicators, we endow target weights and combine those low indicators to realize a comprehensive index. Subsequently, the established model will be applied to various projects to test its applicability and modifications will be proposed to improve it.

<!-- b000050 | prose | pages [3] -->
We will proceed as follows to tackle these problems:  First, create the ecosystem service system. We use the entropy weight method to determine the weights of 11 third-level indicators and apply the coefficient of variation method to determine the weight of four second-level indicators.

<!-- b000051 | prose | pages [3] -->
Eventually, obtain the calculation equation of the ecosystem service index. After that, through the hierarchical clustering method, the land use projects are divided into three categories.  Second, construct an ecological services valuation model. We conduct an benefit cost analysis of land use projects. Considering the importance of ecosystem service costs to the development of land use projects, we make a comparative analysis on the benefit-cost ratio of whether the cost of ecosystem services is considered in land use projects.  Finally. create We divide the 11 three-level indicators into sustainable de-velopment indicators and unsustainable development indicators. At the same time, the sustainable development factor  is introduced to describe the long-term impact of adopting sustainable development measures on project development.

<!-- b000052 | furniture | pages [3] -->
关注数学模型

<!-- b000053 | furniture | pages [3] -->
2

<!-- b000054 | furniture | pages [3] -->
MATHmodels

<!-- b000055 | furniture | pages [3] -->
获取更多资讯

<!-- b000056 | furniture | pages [4] -->
Team#1903455                                                 Page 2 of 21

<!-- b000057 | prose | pages [4] -->
The whole modeling process can be shown as follows:

<!-- b000058 | prose | pages [4] -->
Figure.1 Framework of ESVM

<!-- b000059 | heading | pages [4] -->
2. Assumptions and Justification

<!-- b000060 | prose | pages [4] -->
To simplify the problem and make it convenient for us to simulate real-life conditions, we make the following basic assumptions, each of which is properly justified.  We assume that the cost and benefits of land use projects are not affected by regional policies and other factors that are not related to ecology and the project itself.  We assume that the relative importance of various indicators doesn’t change over time.  We assume all data we obtain are trustworthy since all of sources are reliable. Thus, we are confident that our metrics can reflect the accurate condition.

<!-- b000061 | heading | pages [4] -->
3. Notations

<!-- b000062 | prose | pages [4] -->
We list the symbols and notations used in this paper in Table 1.

<!-- b000063 | caption | pages [4] -->
Table 1 Notations

<!-- b000064 | prose | pages [4] -->
Symbols Definition PSI Provisioning services index

<!-- b000065 | prose | pages [4, 5] -->
RSI Regulating services index BSI Biotope services index CSI Cultural services index ESVM Ecological services valuation model ESS Ecological services system ESI Ecosystem service index BCAM Benefit-cost analysis method BCR Benefit-cost ratio ESC Ecosystem services cost SDF Sustainable development factor

<!-- b000066 | furniture | pages [4] -->
关注数学模型

<!-- b000067 | furniture | pages [4] -->
2

<!-- b000068 | furniture | pages [4] -->
MATHmodels

<!-- b000069 | furniture | pages [4] -->
获取更多资讯

<!-- b000070 | furniture | pages [5] -->
Team#1903455                                                 Page 3 of 21

<!-- b000072 | heading | pages [5] -->
4. Ecological Services Analysis

<!-- b000073 | prose | pages [5] -->
In this section, in order to measure the impact of ecosystem services, we make up the ecosystem services index ESI. First, 11 three-level indicators are selected from four aspects primarily, and then they are integrated into ecosystem service index(ESI) by using entropy weight method (EWM) and coefficient of variation method (CVM). In addition, hierarchical clustering analysis (HCA) is applied to divide the ecosystem service intensity of the project into three categories: weak, moderate and strong. Eventually, we use four projects of varying sizes to verify our evaluation system.

<!-- b000074 | heading | pages [5] -->
4.1 Ecological Services System(ESS)

<!-- b000075 | prose | pages [5] -->
Figure.2 Ecological Services System.

<!-- b000076 | prose | pages [5, 6] -->
According to the classification method of Millennium Ecosystem Assess- ment(MA)[1], the classification framework of MA combines ecosystem services with human well-being, and the classification system is more systematic. By using MA, the ecosystem service is divided into 4 service types: Provisioning services, Regulating services, Biotope services and Cultural services. Summarizing the generally accepted classification result[2] referring to the existing research[3]. Combined with the characteristics of ecosystem characteristics, structure and ecological process, the ecosystem service is subdivided into 11 functional types.

<!-- b000077 | furniture | pages [5] -->
关注数学模型

<!-- b000078 | furniture | pages [5] -->
2

<!-- b000079 | furniture | pages [5] -->
MATHmodels

<!-- b000080 | furniture | pages [5] -->
获取更多资讯

<!-- b000081 | furniture | pages [6] -->
Team#1903455                                                 Page 4 of 21

<!-- b000083 | heading | pages [6] -->
4.1.1 Indicator description

<!-- b000084 | prose | pages [6] -->
(1) Provisioning services X (ton per year). Food is the main component of the a) Food production 1 ecosystem, and its status in agricultural production determines that its development and utilization is a significant agricultural engineering design. Therefore, we introduce the ratio of food production to reflect the development and utilization of ecosystem.

<!-- b000085 | prose | pages [6] -->
X (ton per year). Taking into account changes in b) Raw material production 2 ecosystem services and assessing the environmental costs of land-use development projects, we have introduced the concept of raw material production including the production of wood, rubber, lacquer and rosin.

<!-- b000086 | prose | pages [6] -->
X (ha per year). Water supply is an important part of ecosystem c) Water supply 3 services and has a significant impact on mitigating the negative consequences of land use change caused by river pollution and improper wastewater treatment. We hence introduce the water supply ha per year to describe its reflection to ecosystem services.

<!-- b000087 | prose | pages [6] -->
(2) Regulating services X (million dollars per year). Gas regulation is mainly used to a) Gas regulation 4 improve poor air quality, thus indirectly having a positive impact on climate change. The main measure we take is to convert the waste gas into usable gas and express it in X . terms of a 4 X (million dollars per year).Solid regulation mainly refers b) Solid regulation 5 to a series of treatment of waste residues and wastes generated in the process of human production activities, which can be converted into solid materials that can be used by people, which has an important impact on improving environmental quality and improving biodiversity.

<!-- b000088 | prose | pages [6] -->
X (million dollars per year).Water regulation includes c) Water regulation 6 purify-cation and regulation, and water purification primarily helps to filter out and break down organic waste into inland waters and coastal and marine ecosystems to obtain available water. Water regulation reduces the impact of land cover changes on runoff, floods and aquifers.

<!-- b000089 | prose | pages [6, 7] -->
(3) Biotope services X (ha per year). Quality soil protected by natural a) Soil conservation 7 vegetation and litters maintains fertility, prevents dangerous landslides, protects coasts and riverbanks, and prevents silting. Through afforestation and planting grass to protect the soil, achieve sustainable development of food production, gradually improve soil productivity and the ecological situation X (ha per year). In order to reduce or prevent the harmful effects b) Pest control 8 of pathogenic microorganisms and pests on crops, people and livestock, we artificially adopt certain measures for prevention and control X (ha per year).Genetic diversity, species diversity c) Biodiversity protection 9 and ecosystem diversity are important components of biodiversity. We should not only focus on the protection of the wild populations of the species involved, but also protect their habitats, maintain the balance of the food chain and improve the ecological environment

<!-- b000090 | furniture | pages [6] -->
关注数学模型

<!-- b000091 | furniture | pages [6] -->
2

<!-- b000092 | furniture | pages [6] -->
MATHmodels

<!-- b000093 | furniture | pages [6] -->
获取更多资讯

<!-- b000094 | furniture | pages [7] -->
Team#1903455                                                 Page 5 of 21

<!-- b000096 | prose | pages [7] -->
(4) Cultural services X a) Recreation & tourism ( million dollars per year). Under the condition of 10 not destroying the natural environment, people use different ways of using biological resources to carry out recreational activities, which is called ecotourism X ( time per year).The performing arts usually include b) Performance & art 11 dance, music, drama, folk art, acrobatics, magic and so on. Therefore, we determine the time of performance & art per year as one of the influence of cultural services.

<!-- b000097 | heading | pages [7] -->
4.1.2 Weight of indicators

<!-- b000098 | prose | pages [7] -->
(1) Entropy weight method In this section, with the evaluation indicators defined above, we further determine the weights of these eleven indicators, resulting in the combination of primary indicators. We first use the entropy weight method(EWM) to eliminate the data incommensurability caused by the inconsistency of data dimensions, based on the attribute type of the original indicators, we use the standard 0-1 transformation and the given optimal interval method to do non dimensional and normalization. Therefore, it is convenient to judge the merits of the evaluation indicators directly from the numerical value, and facilitate the evaluation of multi-attribute decision-making.

<!-- b000099 | prose | pages [7] -->
   X x , x ,...,x X , X , X ,..., X , where These 11 indicators of , describe the i i 1 i 2 in 1 2 3 11 impact of ecosystem services and assess the environmental costs of land-use development projects. For the cost index, ecosystem services are proportional to the value of the index, while for the efficiency index, ecosystem services decrease with the increase of the value of the index. Thus, we have   x min( ) x ij i  y  ij  max( ) x min( ) x  i i  (1) j 1,2,..., n   max( ) x x  i ij  y  ij  max( ) x min( ) x  i i

<!-- b000100 | prose | pages [7, 8] -->
ijy is the standardized value of each evaluation indicator of each size, max( ) ix where and min( ) ix are the maximum and minimum value of the evaluation indicator X . i ijy instead of ijx to describe ecosystem After data standardization, we can use services, and then we have y ij  q (2) j n y ij  j 1 According to the concept of self-information and entropy in information theory, the ie of each evaluation index can be calculated, and thus information entropy

<!-- b000101 | furniture | pages [7] -->
关注数学模型

<!-- b000102 | furniture | pages [7] -->
2

<!-- b000103 | furniture | pages [7] -->
MATHmodels

<!-- b000104 | furniture | pages [7] -->
获取更多资讯

<!-- b000105 | furniture | pages [8] -->
Team#1903455                                                 Page 6 of 21

<!-- b000107 | prose | pages [8] -->
n    1 (3) e ln( ) n q ln( q ) i ij ij  j 1

<!-- b000108 | prose | pages [8] -->
Based on the information entropy, we will further calculate the weight of each evaluation indicator we defined before..

<!-- b000109 | prose | pages [8] -->
 1 e   w i i 1,2,..., k (4)  i k e i i

<!-- b000110 | prose | pages [8] -->
Furthermore, four comprehensive evaluation indicators of provisioning services, regulating services, biotope services, cultural services are obtained. This article will be abbreviated as PSI , RSI ，BSI and CSI based on the weight of these calculations, we have     PSI w y w y w y j 1 1 j 2 2 j 3 3 j     RSI w y w y w y  j 4 4 j 5 5 j 6 6 j (5)    BSI w y w y w y  j 7 7 j 8 8 j 9 9 j   CSI w y + w y  j 10 10 j 11 11 j

<!-- b000111 | prose | pages [8] -->
PSI , RSI , BSI and CSI represent the secondary indicators of the size of j. where j j j j

<!-- b000112 | prose | pages [8] -->
The weight of these indexes are determined by EWM and the expression of these indexes are finally described.

<!-- b000113 | prose | pages [8] -->
(2)Coefficient of variation method After representing 11 indicators as four comprehensive variables, we need to further aggregate the four indicators into a comprehensive indicator to directly assess ecosystem services, laying the foundation for rational and effective use of natural resources and protection of the ecological environment.

<!-- b000114 | prose | pages [8] -->
The coefficient of variation method(CVM) is a method of directly using the information contained in each indicator and calculating the weight of the indicator by calculation. Considering the difference between the units and the mean of the four comprehensive indicators, the standard deviation cannot be used to compare the degree of variation, but the ratio of the standard deviation to the mean is used to compare. The equation for each exponent can be expressed as

<!-- b000115 | prose | pages [8] -->
   i (6) CV . i 1,2,3,4 i x i

<!-- b000116 | prose | pages [8] -->
CV is the coefficient of variation of PSI , RSI , BSI , CSI , which are also . i where  is the the standard deviation of the index i . ix known as the standard deviation. i means the average of the index i . After that, we can calculate the weight of four comprehensive index:

<!-- b000117 | furniture | pages [8] -->
关注数学模型

<!-- b000118 | furniture | pages [8] -->
2

<!-- b000119 | furniture | pages [8] -->
MATHmodels

<!-- b000120 | furniture | pages [8] -->
获取更多资讯

<!-- b000121 | furniture | pages [9] -->
Team#1903455                                                 Page 7 of 21

<!-- b000122 | prose | pages [9] -->
CV .   i W i 1,2,3,4 (7)  i n CV . i  i 1

<!-- b000123 | prose | pages [9] -->
Subsequently, on the basis of those calculated weights, we can derive the ecosystem services indicators, which is abbreviated as ESI            (8) ESI W PSI W RSI W BSI W CSI 100 1 2 3 4

<!-- b000124 | prose | pages [9] -->
Since the specific value of those indicators have been given in Table 2, hence we can calculate the ESI of our selected projects. As can be seen from table 2 below, for the 11 evaluation indicators, the weight difference between them is not big, which is generally around 0.1. Recreation & tourism has the largest weight of 0.1293. For the four comprehensive indicators, cultural services ranks the first with the weight of 0.2862 in our final criterion, with regulating services following behind, while provisioning services ranks the third and biotope services is at the bottom.

<!-- b000125 | caption | pages [9] -->
Table 2 Weight values of the indicators

<!-- b000126 | prose | pages [9] -->
Indicators(I) Indicators(II) Weights Indicators(III) Weights Food production 0.0705 Provisioning services 0.2591 Raw material production 0.1038 Water supply 0.1063 Gas regulation 0.1157 Regulating services 0.2647 Solid regulation 0.0743 Water regulation 0.1089 Intensity Soil conservation 0.1189 Biotope services 0.1900 Pest control 0.0348 Biodiversity protection 0.0438 Recreation & tourism 0.1293 Cultural services 0.2862 Performance & art 0.0937

<!-- b000127 | heading | pages [9] -->
4.2 Intensity evaluation

<!-- b000128 | prose | pages [9] -->
We first divide the ecosystem services of land use projects into three levels through hierarchical clustering. Then, we use our ecosystem services system to conduct an assessment of ecosystem services on four different size land use project examples to verify the effectiveness of our evaluation system.

<!-- b000129 | heading | pages [9] -->
4.2.1 Hierarchical clustering

<!-- b000130 | prose | pages [9, 10] -->
Combined with the comprehensive ecosystem index we established before, we imported the project data of different sizes and calculated their values. Euclidean distance is used as similarity measurement method to divide the ecosystem intensity into weak, moderate and strong, and hierarchical clustering was used to cluster the projects of ten sizes Hierarchical clustering algorithm is just like building a branching tree from bottom up[], with leaves as individual documents and the centers (clusters) as the roots[4]. The strategy of aggregation clustering is to firstly cluster each object as an atom, and then cluster these atoms layer by layer until certain termination conditions are met. The 2 O n ( ) hierarchical clustering algorithm has a computational complexity of , which is suitable for the classification of small data sets[5].

<!-- b000131 | furniture | pages [9] -->
关注数学模型

<!-- b000132 | furniture | pages [9] -->
2

<!-- b000133 | furniture | pages [9] -->
MATHmodels

<!-- b000134 | furniture | pages [9] -->
获取更多资讯

<!-- b000135 | furniture | pages [10] -->
Team#1903455                                                 Page 8 of 21

<!-- b000137 | prose | pages [10] -->
After calculating the ESI of our selected projects, then we apply hierarchical clustering algorithm to clarify these projects into three groups: weak, moderate and strong. The higher the value is, the stronger the project is. The results of clustering are shown as follows.

<!-- b000138 | prose | pages [10] -->
After calculating the value of PSI , RSI ，BSI , CSI and ESI , we can evaluate the ecosystem service intensity of specific projects. As shown in Figure.4, we assign different colors to the different ecosystem service intensity levels of weak, moderate and strong, so as to intuitively display the ecosystem service intensity.

<!-- b000139 | prose | pages [10] -->
Figure.3 Classification standards of varying ecosystem service index, which is classified as weak, moderate and strong.

<!-- b000140 | prose | pages [10] -->
As shown in Figure.3, the classification standards of the four combined indicators and the comprehensive metric vary a little. Take comprehensive index of ecosystem services for an example, when the score of ESI is less than 29.45, it is a weak project. While the score of ESI is between 29.45 and 68.37, it is a moderate project. In the condition that ESI is more than 68.37, it is regarded as strong.

<!-- b000141 | heading | pages [10] -->
4.2.2 The result of intensity evaluation

<!-- b000142 | prose | pages [10] -->
As is vividly shown in Figure.5, we use the ecological services valuation system to evaluate four types of projects which will be listed later and rank them.

<!-- b000143 | caption | pages [10] -->
Table 3 Description of practical project of varying sizes

<!-- b000144 | prose | pages [10, 11] -->
Project Name Size Intensity PA Private enterprise relocation project medium weak PB Factory construction project medium moderate PC National pipeline engineering large strong PD House construction small weak From the above Table 3 we can see that PA, PB, PC, and PD are land use projects of different sizes, respectively, national pipeline engineering has the largest scale as a national project.

<!-- b000145 | furniture | pages [10] -->
关注数学模型

<!-- b000146 | furniture | pages [10] -->
2

<!-- b000147 | furniture | pages [10] -->
MATHmodels

<!-- b000148 | furniture | pages [10] -->
获取更多资讯

<!-- b000149 | furniture | pages [11] -->
Team#1903455                                                 Page 9 of 21

<!-- b000151 | prose | pages [11] -->
Figure.4 Comparison of ESI original ranking and intensity valuation indicators.

<!-- b000152 | prose | pages [11] -->
Considering that PC involves pipeline protection structure engineering, pipeline crossing engineering and line subsidiary engineering, the project construction is very complex, with a long construction period and high technical requirements, therefore, it has the greatest impact on the environment and the intensity of ecosystem service is strong which is in line with reality. As for project of PD, it mainly involves house construction. Its impact on the environment is relatively small, so the intensity of ecosystem services is weak which corresponds to reality.

<!-- b000153 | heading | pages [11] -->
5. Ecosystem Service Valuation Model

<!-- b000154 | prose | pages [11] -->
In the process of economic development, the initial construction projects mainly rely on extensive economic growth mode of increasing investment and material input, and the contradiction between economic development and resource environment is very sharp. While individually these activities may seem inconsequential to the total ability of the biosphere’s functioning potential, cumulatively they are directly impacting the biodiversity and causing environmental degradation.

<!-- b000155 | heading | pages [11] -->
5.1 Cost-benefit analysis

<!-- b000156 | prose | pages [11] -->
For the sake of understanding the true economic costs of land use projects, we create an ecological services valuation model to perform a cost benefit analysis of land use development projects of varying sizes based on the cost-benefit analysis method(CBA), which mainly includes the following steps[6].

<!-- b000157 | heading | pages [11] -->
5.1.1 Cost analysis

<!-- b000158 | prose | pages [11, 12] -->
Cost analysis[7] includes internal cost and external cost. Internal cost refers to the direct expenses incurred by the developer in land development and utilization including land costs, infrastructure costs, ancillary facilities costs, financing costs, indirect costs borne by the development of land, which can be obtained from statistics and accounting data. The external cost is not directly reflected in the expenditure of land development and utilization itself, but in the monetary estimate of other environmental losses (i.e. negative external effects) caused by the development of land. When other productive resources associated with land are damaged by the exploitation of land, external costs are best estimated through the loss of productivity of that resource. Thus, we have:

<!-- b000159 | furniture | pages [11] -->
关注数学模型

<!-- b000160 | furniture | pages [11] -->
2

<!-- b000161 | furniture | pages [11] -->
MATHmodels

<!-- b000162 | furniture | pages [11] -->
获取更多资讯

<!-- b000163 | furniture | pages [12] -->
Team#1903455                                                 Page 10 of 21

<!-- b000165 | prose | pages [12] -->
 

<!-- b000166 | heading | pages [12] -->
C C

<!-- b000167 | prose | pages [12] -->
C (10) r o e

<!-- b000168 | prose | pages [12] -->
  C = q ESI q l C (11) e o

<!-- b000169 | prose | pages [12] -->
C is real economic costs of land use projects, C is the cost of building a where r o C is the economic cost of project without considering the cost of ecosystem services, e improving the negative consequences of land use change, that is, the cost of ecosystem services. q represents a constant, l is ecosystem service cost index.

<!-- b000170 | prose | pages [12] -->
C , we calculate In order to explore the functional relationship between ESI and o the ecosystem service index of project A over time through equation (8). To explore the C , we make the cost of project PA and the discrete points relationship between ESI and o of ESI and fit it with Gaussian method, such as Figure.5 shows.

<!-- b000171 | prose | pages [12] -->
Figure.5 The relationship curve between original costs and ESI .

<!-- b000172 | prose | pages [12] -->
From the above Figure.5, we can see that ecosystem services and original costs match the tendency of logistic growth curve approximately and the result of the fitting also proves this by equation (8). In the original cost accumulation stage, because the cost required at this time is small, the overall operational capacity of the biosphere is irrelevant, so ESI is increasing slowly. As the original cost continues to increase, when the ecosystem itself exceeds the range, the original cost will increase rapidly due to the impact on biodiversity and environmental degradation. When the original cost increases to a certain extent, at this time the ecosystem has a certain adaptability to the already existing impact, so the ecosystem service changes tend to be slow at this time.

<!-- b000173 | prose | pages [12] -->
0.9462 ESI = (12)     C  1+exp 0.000072 312654 o

<!-- b000174 | furniture | pages [12] -->
关注数学模型

<!-- b000175 | furniture | pages [12] -->
2

<!-- b000176 | furniture | pages [12] -->
MATHmodels

<!-- b000177 | furniture | pages [12] -->
获取更多资讯

<!-- b000178 | furniture | pages [13] -->
Team#1903455                                                 Page 11 of 21

<!-- b000179 | heading | pages [13] -->
5.1.2 Benefit analysis

<!-- b000180 | prose | pages [13] -->
Generally, two benefits can be obtained through the development and utilization of land resources: internal and external benefits. The internal benefit is the benefit which can be estimated by the market price directly after the land development and utilization, and is the direct result of the land utilization plan. External benefits refer to the beneficial effects of land development and utilization activities on surrounding resources, environment and economic activities.

<!-- b000181 | prose | pages [13] -->
   B B C + (13) r o e

<!-- b000182 | prose | pages [13] -->
 B = B C (14) o b o

<!-- b000183 | prose | pages [13] -->
rB is true economic benefits of land use projects, B is the benefit of building a where o project without considering the cost of ecosystem services and it can be obtained from the statistics,  is a variable related to policy, subsidies, etc. B is the total benefit of b a project when the cost of ecosystem services is not taken into account.

<!-- b000184 | heading | pages [13] -->
5.1.3 The ratio of benefit-cost analysis

<!-- b000185 | prose | pages [13] -->
In order to explore the real benefit-cost situation of land use projects, we use bene- fit-cost ratio to describe the impact of whether or not to consider the ecological ser- vices on the project. We take project PA as an example.

<!-- b000186 | heading | pages [13] -->
I B C                            (15)

<!-- b000187 | prose | pages [13] -->
= r r

<!-- b000188 | prose | pages [13] -->
where I is the ratio of benefit-cost.

<!-- b000189 | prose | pages [13] -->
Figure.6 The practical value (1995~2019) of benefit. (a) scatter plot of benefit-cost rate over time not taking into account the cost of ecosystem services; (b) scatter plot of benefit- cost rate over time taking into account the cost of ecosystem services.

<!-- b000190 | prose | pages [13, 14] -->
As can be seen from Figure.6, without considering the cost of ecosystem services, the benefit of an existing project tends to increase first and then decrease. That is, as the life cycle increases, a project experiences entrepreneurship, growth, and maturity, and then quickly declines after reaching a peak. However, if the enterprise takes ecosystem services into consideration, although the growth trend is relatively slow in the early stage, the benefits of the project will gradually increase over time, and the trend of growth will continue for a long time.

<!-- b000191 | furniture | pages [13] -->
关注数学模型

<!-- b000192 | furniture | pages [13] -->
2

<!-- b000193 | furniture | pages [13] -->
MATHmodels

<!-- b000194 | furniture | pages [13] -->
获取更多资讯

<!-- b000195 | furniture | pages [14] -->
Team#1903455                                                 Page 12 of 21

<!-- b000197 | heading | pages [14] -->
5.2 Prediction of Benefit-cost radio with SVM regression method

<!-- b000198 | prose | pages [14] -->
In order to predict the change trend of the curve quantitatively and describe the impact of ecosystem services on project benefits intuitively, we perform support vector machine(SVM) regression on the data of the two curves we just got.

<!-- b000199 | prose | pages [14] -->
Support vector machines are a core machine learning technology. They have strong theoretical foundations and excellent empirical successes. SVM follows the principle of structural risk minimization and is good at solving small sample and nonlinear problems[8]. Unlike traditional machine learning methods such as artificial neural networks that follow the principle of empirical risk minimization, SVM avoids problems such as overfitting, difficult parameter adjustment and slow convergence [9,10].

<!-- b000200 | prose | pages [14] -->
  u  We are given training data M 1,2,3, ,b that are vectors in some space u     u  v v M R Y R .We are also given their labels uY 1,2,3, ,b where .In their u simplest form, SVMs are hyperplanes that separate the training data by a maximal margin. The training instances that lie closest to the hyperplane are called support vectors. More generally, SVMs allow us to project the original training data in space M to a higher dimensional feature space F via a Mercer kernel operator K . The form of the optimal hyperplane is expressed as follows:

<!-- b000201 | prose | pages [14] -->
        Y f m M p (16)

<!-- b000202 | prose | pages [14] -->
       ,  is the weight vector, p is the T T T where Y Y Y , , , Y , M M , M , , M 1 2 b 1 2 b    threshold value, M is the mapping from the input space to the higher-dimensional space Introduce the insensitive loss function , and use the dispersion analysis to solve the optimal hyperplane. When  is greater than the error value, the error is small and  are introduced to prevent individual data negligible; the relaxation variables and  from affecting the model deviation. The penalty factor D  is introduced, and the sample data deviating from the model is penalized, so the optimal hyperplane can be converted into equations (17) and (18) to solve the minimum problem:

<!-- b000203 | prose | pages [14] -->
    b b 1   2     min + D (17)     i i 2       i 1 i 1

<!-- b000204 | prose | pages [14] -->
        f M Y  i i i (18)        Y f M  i i i

<!-- b000205 | prose | pages [14] -->
We introduce the Lagrange function to solve the above equations (17) and (18), i are Lagrange multipliers, so the equation is transformed into the i and where following equation (19).

<!-- b000206 | furniture | pages [14] -->
关注数学模型

<!-- b000207 | furniture | pages [14] -->
2

<!-- b000208 | furniture | pages [14] -->
MATHmodels

<!-- b000209 | furniture | pages [14] -->
获取更多资讯

<!-- b000210 | furniture | pages [15] -->
Team#1903455                                                 Page 13 of 21

<!-- b000211 | prose | pages [15] -->
b b 1         2                 L , , , a D + Y M + a i i i 2   i 1 i 1 (19) b              Y M + a i i i i  i 1

<!-- b000212 | prose | pages [15] -->
  , i.     ,  i , , , , 0; i 1,2, , b where i i i i  of the function  , , a , The minimum value can be obtained by deflecting the i i L , respectively, as follows:

<!-- b000213 | prose | pages [15] -->
       L , , , a  L    0 =0             L , , , a  L    0 =0    a a (20)       L , , , a   L   0 =0      i i        L , , , a  L    0 =0        i i     h   Two commonly used kernels are the polynomial kernel K u v , u v 1 , which induces polynomial boundaries of degree h in the original space M , and the radial            u v u v  basis function kernel , which induces boundaries by placing K u v , e weighted Gaussians upon key training instances. In the remainder of this paper we will adopt the first polynomial kernel function to build a prediction model.

<!-- b000214 | prose | pages [15] -->
Combining equations (20) and polynomial kernel, the final form of the optimal hyperplane is determined as shown in equation (21).

<!-- b000215 | prose | pages [15] -->
b                  f X M a K u v , a (21) i  u 1   K u v is the polynomial kernel. , where We conduct regression analysis based on support vector machine. Given the data of 1995-2019 as the training samples, we predict the changes over 2019-2035 years and got the change curve as shown in the Figure.7.

<!-- b000216 | prose | pages [15] -->
As can be seen from the Figure.8(a), the benefit-cost ratio of the project PA without considering ecosystem services increases firstly and then decreases with time. In other words, although the profit rate of such projects is relatively fast at the beginning, the benefit starts to decline sharply with time.

<!-- b000217 | furniture | pages [15] -->
关注数学模型

<!-- b000218 | furniture | pages [15] -->
2

<!-- b000219 | furniture | pages [15] -->
MATHmodels

<!-- b000220 | furniture | pages [15] -->
获取更多资讯

<!-- b000221 | furniture | pages [16] -->
Team#1903455                                                 Page 14 of 21

<!-- b000222 | prose | pages [16] -->
Figure.7 The practical value (1995~2019) and predicted value(2019~2035) of benefit-cost rate of project PA. The blue line is made by the method of support vector machine regression, and the red dotted line is a fitting curve with a confidence interval of 0.95.(a) fitting curve of available benefit data over time; (b) fitting curve of benefit data over time taking into account the cost of ecosystem services.

<!-- b000223 | prose | pages [16] -->
As for the Figure.7(b), the project PA is based on the consideration of the cost of ecosystem services, that is, the external cost. Even if the rate of profit growth at the beginning is slow, the benefits have been slowly increasing with time. In the predicted nearly two decades, the benefit does not show a declining trend, but steadily increases. It can be seen that considering ecosystem services can effectively increase the life cycle of the project, consolidate the existing status, and delay the arrival of the recession.

<!-- b000224 | heading | pages [16] -->
5.3 Result analysis

<!-- b000225 | prose | pages [16] -->
In order to compare more intuitively the impact of the availability of ecosystem services on the benefit-cost ratio of land-use projects, we have combined the two maps of Fiugre.8 to facilitate comparative analysis.

<!-- b000226 | prose | pages [16] -->
Figure.8 The practical value (1995-2019) and predicted value of benefit-cost ratio of project PA(2019-2035).

<!-- b000227 | furniture | pages [16] -->
关注数学模型

<!-- b000228 | furniture | pages [16] -->
2

<!-- b000229 | furniture | pages [16] -->
MATHmodels

<!-- b000230 | furniture | pages [16] -->
获取更多资讯

<!-- b000231 | furniture | pages [17] -->
Team#1903455                                                 Page 15 of 21

<!-- b000232 | prose | pages [17] -->
As can be seen from the Figure.8, in 2013, when the benefit cost ratio reached the peak of the project. The project that does not consider ecosystem services is not implemented in an appropriate environment due to the damage to the ecological environment beyond its capacity. As a result, efficiency decreases gradually and benefit decreases rapidly with time. In 2026, the two curves intersect, indicating whether the benefit-cost of the ecological cost service is equivalent at this time. After that (shaded area), the benefits brought about by the ecological service should be greater than the benefits brought by ecological services from that on. When reaching 2033, do not consider the ecological services will lead to the destruction of the ecological environment seriously affecting the project operation, so that the cost-effectiveness ratio reach to 0.

<!-- b000233 | caption | pages [17] -->
Table 4 shows the specific values and descriptions of some special information

<!-- b000234 | prose | pages [17] -->
points in Figure 8. Among them, N represents the absence of ecosystem services, Y represents the adoption of ecosystem services. We use the same model for cost-benefit analysis of PB, PC and PD. The specific results are shown in Appendix 1，2，3.

<!-- b000235 | caption | pages [17] -->
Table 4 BCR of the project PA according to Figure.8

<!-- b000236 | prose | pages [17] -->
Year 1995 2013 2019 2026 2030 2033 BCR 1.06 11.38 10.48 6.13 2.26 0 N PA Description Highest Intersection Zero ↗ ↘ ↘ BCR 0.73 6.03 6.10 6.13 6.24 6.39 Y Description ↗ ↗ ↗ ↗ ↗ ↗

<!-- b000237 | heading | pages [17] -->
6. Sustainable development analysis

<!-- b000238 | prose | pages [17] -->
From the above analysis, we can see that considering the cost of ecosystem services can increase the life cycle of land-use projects and increase cumulative benefits. In this section, we will explore the impact of specific ecological service measures on land use projects.

<!-- b000239 | heading | pages [17] -->
6.1 Analysis of ecosystem services measures

<!-- b000240 | prose | pages [17] -->
The ecosystem service measures are broadly divided into two categories by us: sustainable development measures and unsustainable development measures. Statistics on the ecosystem services about projects PA, PB, PC and PD are carried out.

<!-- b000241 | prose | pages [17] -->
From the pie chart shown in Figure.9, we can see land use projects of different scales PA, PB, PC, and PD. As the scale of the project increases, the proportion of projects adopting sustainable development measures is also increasing. For example, for national pipeline projects, projects taking sustainable development measures accounted for 91% of the total measures, and only non-sustainable development measures accounted for only 9%. Therefore, it is not difficult to find that the importance of sustainable development measures is valued on almost all scales.

<!-- b000242 | furniture | pages [17] -->
关注数学模型

<!-- b000243 | furniture | pages [17] -->
2

<!-- b000244 | furniture | pages [17] -->
MATHmodels

<!-- b000245 | furniture | pages [17] -->
获取更多资讯

<!-- b000246 | furniture | pages [18] -->
Team#1903455                                                 Page 16 of 21

<!-- b000247 | prose | pages [18] -->
Figure.9 Statistical results of four projects (a)project PA; (b)project PB; (c) project PC; (d) project PD

<!-- b000248 | prose | pages [18] -->
From the ecosystem service system established in the fourth part, it is not difficult to find that 11 indicators are divided into 6 sustainable development indicators and 5 unsustainable development indicators, and the sustainable development indicators are shown in Figure.10.

<!-- b000249 | prose | pages [18] -->
Figure.10 The schematic diagram of the six sustainable development indicators

<!-- b000250 | heading | pages [18] -->
6.2 Influence of Sustainability on benefit-cost ratio

<!-- b000251 | prose | pages [18] -->
In order to more clearly reflect the impact of sustainable development measures on the benefits of land-use projects, we use project PA, PB, PC, and PD as research objects. The ecosystem service evaluation model established in Section 5 is used to analyze and predict the benefit-cost ratio which influenced by sustainable development measures for 2004-2018. The results are shown in Figure.11.

<!-- b000252 | furniture | pages [18] -->
关注数学模型

<!-- b000253 | furniture | pages [18] -->
2

<!-- b000254 | furniture | pages [18] -->
MATHmodels

<!-- b000255 | furniture | pages [18] -->
获取更多资讯

<!-- b000256 | furniture | pages [19] -->
Team#1903455                                                 Page 17 of 21

<!-- b000257 | prose | pages [19] -->
Figure.11 Benefit-cost ratio curve of four projects which influenced by sustainable development measures only

<!-- b000258 | prose | pages [19] -->
As can be seen from the above Figure.11, for large-scale national pipeline engineering, the benefits of adopting sustainable development measures will grow exponentially over time, and the gap between medium and small scale will increase. It can be seen that the adoption of sustainable development measures has a significant impact on the long-term development of the project, and can significantly increase the cumulative benefits of the project in the later stages of project maturity.

<!-- b000259 | prose | pages [19] -->
From the Figure.11, we fitted the relationship expression between the benefit brought by sustainable development index and index weight. The fitting results are shown in Table 5.

<!-- b000260 | caption | pages [19] -->
Table 5 Result of fitting according to Figure.11

<!-- b000261 | prose | pages [19] -->
Project Equation

<!-- b000262 | prose | pages [19] -->
   B =87.31 exp(0.1056 t ) 0.0014 PA P A

<!-- b000263 | prose | pages [19] -->
   B =88.4 exp(0.1098 t ) 0.0014 PB P B

<!-- b000264 | prose | pages [19] -->
   B =101.4 exp(0.1198 t ) 0.0014 PC cP

<!-- b000265 | prose | pages [19] -->
   B =11.98 exp(0.1033 t ) 0.0013 PD P D

<!-- b000266 | prose | pages [19] -->
From Table 5, we can summarize the relationship between sustainable development and benefit-cost radio of land-use projects of any size. We portray their relationship as equation(22).

<!-- b000267 | prose | pages [19, 20] -->
h         m t B = w x e c (22)  i s t ,  s 1 h        w x , = w x (23)   i s t ,  s 1

<!-- b000268 | furniture | pages [19] -->
关注数学模型

<!-- b000269 | furniture | pages [19] -->
2

<!-- b000270 | furniture | pages [19] -->
MATHmodels

<!-- b000271 | furniture | pages [19] -->
获取更多资讯

<!-- b000272 | furniture | pages [20] -->
Team#1903455                                                 Page 18 of 21

<!-- b000274 | prose | pages [20] -->
where B is the benefit brought by sustainable development indicators;  and c is a iw is the weight of indicator s we defined before; h is the number of constant;

<!-- b000275 | prose | pages [20] -->
x is the value of the indicator s in year sustainable development indicators, h =6 ;   ,s t is the time that land use projects have t ; m is related to the size of the project; t    w x , is a function of w and x . existed;

<!-- b000276 | prose | pages [20] -->
   w x , Subsequently, we define as the sustainable development factor(SDF), which is closely related to the weight of sustainable development index and sustainable development index.

<!-- b000277 | prose | pages [20] -->
Taking into account the uncertainty  in our benefit-cost radio equation when calculating the benefit-cost radio, through the above analysis, we clearly see that a large part of the benefits generated by uncertain factors is due to the benefit brought by the adoption of sustainable development measures. Thus, we get equation(24).

<!-- b000278 | prose | pages [20] -->
   =B (24) where B is the benefit brought by sustainable development indicators;   is the benefits associated with policies, subsidies, etc.

<!-- b000279 | prose | pages [20] -->
The adoption of sustainable development measures has important practical significance for extending the life cycle of enterprises, delaying the arrival of recession and increasing the cumulative benefits of projects. The introduction of SDF to describe the level of sustainable development is of great significance for the long-term development of projects.

<!-- b000280 | heading | pages [20] -->
7. Sensitivity Analysis

<!-- b000281 | prose | pages [20] -->
Based on the sustainable development factors calculated from the above four projects, we calculate their real benefit-cost ratio, as shown in Figure 12.

<!-- b000282 | prose | pages [20] -->
Figure.12 The curve of benefit-cost ratio over time of four project.

<!-- b000283 | prose | pages [20, 21] -->
To test the robustness of our model, in this section, by assigning different values to , we conducted a regression analysis on the data of benefit over time from 1995 to 2018, and predicted the data from 2019 to 2035. The final result is shown in Figure.13.

<!-- b000284 | furniture | pages [20] -->
关注数学模型

<!-- b000285 | furniture | pages [20] -->
2

<!-- b000286 | furniture | pages [20] -->
MATHmodels

<!-- b000287 | furniture | pages [20] -->
获取更多资讯

<!-- b000288 | furniture | pages [21] -->
Team#1903455                                                 Page 19 of 21

<!-- b000290 | prose | pages [21] -->
To quantitatively characterize the impact of SDF on a specific project, we have depicted the change curve of benefit-cost radio over time for project PA. As can be seen from the figure above, with the increase of, the benefit-cost radio of the same project grows increasingly slowly, that is, the area between two adjacent curves gradually shrinks. This means that the value of  is not the larger the better, but there is an optimal value. When  is greater than this optimal value, the environmental damage caused by the project has been alleviated. If  continues to increase at this time, it will not get the significant benefits it deserves, so the distance between adjacent curves is gradually narrowing which also accord with the development law of natural thing. This shows the stability of our model, which can solve practical problems in real life.

<!-- b000291 | prose | pages [21] -->
Figure.13 The curve of benefit-cost ratio over time with different (project PA).

<!-- b000292 | heading | pages [21] -->
8. Advice on project planning and management

<!-- b000293 | prose | pages [21] -->
The real economic cost of the land use project is assessed by establishing an ecological services valuation model. We introduce sustainability assessment factors to characterize the factors that influence the effectiveness of their ecosystem services.

<!-- b000294 | prose | pages [21] -->
From the results of Figure.11, we can see that adopting sustainable development measures will make the long-term BCR of the project grow steadily, Although considering ecosystem services increases the cost of land use projects, in the long run, it will increase the project life cycle and cumulative benefits. Therefore, we suggest that in the planning of future land use projects, the emphasis on sustainable development factors will contribute to the long-term development of the projects.

<!-- b000295 | prose | pages [21, 22] -->
As for the influence of land use project planners and managers[12], first of all, we should take the workload of the existing land use projects as the benchmark, taking into account the stable transition of the business, and consider the efficiency improvement after concentration. Secondly, in the initial stage of introducing sustainable development measures, changes in business models will have a certain impact on the efficiency of the project staff. Therefore, it should be configured according to the familiarity of personnel with the posts. Finally, after the project is running stably, with the improvement of staff efficiency, post adjustment can be made according to personnel and business conditions.

<!-- b000296 | furniture | pages [21] -->
关注数学模型

<!-- b000297 | furniture | pages [21] -->
2

<!-- b000298 | furniture | pages [21] -->
MATHmodels

<!-- b000299 | furniture | pages [21] -->
获取更多资讯

<!-- b000300 | furniture | pages [22] -->
Team#1903455                                                 Page 20 of 21

<!-- b000302 | heading | pages [22] -->
9. Conclusion

<!-- b000303 | prose | pages [22] -->
To conclude, we first establish an ecological services valuation system based on the entropy weight method and coefficient of variation method so as to represent the ecosystem service index. Furthermore, we apply hierarchical clustering to determine the range of intensity for weak, moderate and strong respectively. Test of 4 projects of varying sizes shows that our model is robust and correct.

<!-- b000304 | prose | pages [22] -->
Thereafter, in order to perform a cost benefit analysis of land use development projects of varying sizes, we first analyzed the correlation between original costs and ecosystem services, and found that ecosystem services had a significant effect on the increase of benefit-cost ratio. Then, we use support vector machines to predict the data in 2019-2035. It can be illustrated from the results that after considering the cost of ecosystem services, land use projects will continue to develop in a stable trend, although the projects without considering the cost of ecosystem services have more benefits in the short term, it will develop unsteadily in the long term. For the sake of further explore the factors affecting the benefit-cost ratio of a project, we introduce the sustainable development factor . when a project takes into account , its life cycle and cumulative benefits will be greater.

<!-- b000305 | prose | pages [22] -->
Finally, we put forward suggestions for the development of land-use projects and modify our model to be applicable to small community-based projects and large national projects better through substituting indicator of  while maintaining the framework.

<!-- b000306 | heading | pages [22] -->
9.1 Strengths

<!-- b000307 | prose | pages [22] -->
 We use the entropy weight method and the coefficient of variation method to determine the weight of ecosystem service indicators, avoiding the negative effects of a single method.

<!-- b000308 | prose | pages [22] -->
 The experimental results show that our model can be applied to the long-term cost-benefit analysis of land use projects of different scales.

<!-- b000309 | prose | pages [22] -->
 We validate our model through real land use project cases and find that our model is highly effective.

<!-- b000310 | prose | pages [22] -->
 We use our model to discover the importance of sustainable development services for land use projects and to quantify the importance.

<!-- b000311 | heading | pages [22] -->
9.2 Weaknesses

<!-- b000312 | prose | pages [22] -->
 Due to the limited search data, the indicators used cannot completely describe the actual ecosystem services, which may reduce the accuracy of our model.

<!-- b000313 | prose | pages [22] -->
 Our model does not take into account the possible costs of policies, natural disasters, etc., so there is a bias in cost-benefit analysis.

<!-- b000314 | furniture | pages [22] -->
关注数学模型

<!-- b000315 | furniture | pages [22] -->
2

<!-- b000316 | furniture | pages [22] -->
MATHmodels

<!-- b000317 | furniture | pages [22] -->
获取更多资讯

<!-- b000318 | furniture | pages [23] -->
Team#1903455                                                 Page 21 of 21

<!-- b000319 | heading | pages [23] -->
References

<!-- b000320 | references | pages [23] -->
[1]  de GROOT R S, ALKEMADE R, BRAAT L, et al. Challenges in integrating the concept of

<!-- b000321 | references | pages [23] -->
ecosystem services and values in landscape planning, management and decision making [J].

<!-- b000322 | references | pages [23] -->
Ecol Complexity, 2010, 7(3): 260-272.

<!-- b000323 | references | pages [23] -->
[2] BRAAT L C, de GROOT R. The ecosystem services agenda: bridging the worlds of natural

<!-- b000324 | references | pages [23] -->
science and economics, conservation and development, and public and private policy [J].

<!-- b000325 | references | pages [23] -->
Ecosyst Serv, 2012, 1(1):4-15.

<!-- b000326 | references | pages [23] -->
[3] CHENG Min, ZHANG Liyun, CUI Lijuan, et al. Progress in ecosystem services value

<!-- b000327 | references | pages [23] -->
valuation of coastal wetlands[J]. Acta Ecol Sin, 2016, 36(23): 7509-7518.

<!-- b000328 | references | pages [23] -->
[4]  Sambasivam S, Theodosopoulos N. Advanced data clustering methods of mining Web

<!-- b000329 | references | pages [23] -->
documents. Issues in Informing Science and Information Technology, 2006,(3):563-579

<!-- b000330 | references | pages [23] -->
[5] Sun JG, Liu J, Zhao LY. Clustering algorithms research.  Journal of Software,

<!-- b000331 | references | pages [23] -->
2008,19(1):48-61

<!-- b000332 | references | pages [23] -->
[6]  Pandey M D, Nathwani J S. Canada Wide Standard for Particulate Matter and Ozone: Cost-

<!-- b000333 | references | pages [23] -->
Benefit Analysis Using a Life Quality Index[J]. Risk Analysis.2003 .23(1):55-67.

<!-- b000334 | references | pages [23] -->
[7]  Fan Mingtian; Zhang Zuping; Su Aoxue. Cost-benefit analysis of integration DER into

<!-- b000335 | references | pages [23] -->
distribution network[C] Workshop 2012 //Integration of Renewables into the Distribution Grid.

<!-- b000336 | references | pages [23] -->
Lisbon,Portugal: CIRED, 2012:1-4

<!-- b000337 | references | pages [23] -->
[8]  Vapnik V N. The Nature of Statistic Learning Theory [M]. New York: Springer, 2000. 17-34.

<!-- b000338 | references | pages [23] -->
[9]  García Nieto P J, Combarro E F, Montañés E, et al. A SVM-based regression model to study

<!-- b000339 | references | pages [23] -->
the air quality at local scale in Oviedo urban area (Northern Spain): A case study [J]. Applied

<!-- b000340 | references | pages [23] -->
Mathematics and Computation, 2013, 219(17): 8923- 8937.

<!-- b000341 | references | pages [23] -->
[l0]  Lu W Z, Wang W J. Potential assessment of the ‘support vector machine’ method in forecasting

<!-- b000342 | references | pages [23] -->
ambient air pollutant trends [J]. Chemosphere, 2005, 59(5): 693-701.

<!-- b000343 | references | pages [23] -->
[11] Greg Kats, Capital E. The Costs and Financial Benefits of Green Buildings, A Report to

<!-- b000344 | references | pages [23] -->
Califonnia’s Sustainable Building Task Force, 2003.

<!-- b000345 | references | pages [23] -->
[12] Pina V, Torres L. Analysis of the efficiency of local government services delivery. An

<!-- b000346 | references | pages [23] -->
application to urban public transport [J]. Transportation Research Part A, 2001, 35(10): 929-

<!-- b000347 | references | pages [23] -->
944.

<!-- b000348 | furniture | pages [23] -->
关注数学模型

<!-- b000349 | furniture | pages [23] -->
2

<!-- b000350 | furniture | pages [23] -->
MATHmodels

<!-- b000351 | furniture | pages [23] -->
获取更多资讯

<!-- b000352 | furniture | pages [24] -->
关注数学模型

<!-- b000353 | furniture | pages [24] -->
2

<!-- b000354 | furniture | pages [24] -->
MATHmodels

<!-- b000355 | furniture | pages [24] -->
获取更多资讯

<!-- b000356 | heading | pages [25] -->
Appendix 1: ESVM result of project PB

<!-- b000357 | prose | pages [25] -->
Year 1995 2012 2015 2020 2025 2028 ICR 2.38 12.52 10.26 6.32 2.18 0 N PB Description Highest Intersection Zero ↗ ↘ ↘ ICR 1.29 3.68 5.81 6.32 7.24 7.89 Y Description ↗ ↗ ↗ ↗ ↗ ↗

<!-- b000358 | heading | pages [25] -->
Appendix 2: ESVM result of project PC

<!-- b000359 | prose | pages [25] -->
Year 1995 2010 2013 2016 2018 2020 N ICR 4.92 20.16 16.24 11.72 4.37 0 PC Description Highest Intersection Zero ↗ ↘ ↘ Y ICR 2.67 6.27 9.19 11.72 12.46 13.25 Description ↗ ↗ ↗ ↗ ↗ ↗

<!-- b000360 | heading | pages [25] -->
Appendix 3: ESVM result of project PD

<!-- b000361 | prose | pages [25] -->
Year 1995 2026 2035 2043 2050 2056 N ICR 1.06 6.33 5.49 3.87 1.75 0 PD Description Highest Intersection Zero ↗ ↘ ↘ Y ICR 0.73 2.26 3.15 3.87 4.26 4.82 ↗ ↗ ↗ Description ↗ ↗ ↗

<!-- b000362 | furniture | pages [25] -->
关注数学模型

<!-- b000363 | furniture | pages [25] -->
2

<!-- b000364 | furniture | pages [25] -->
MATHmodels

<!-- b000365 | furniture | pages [25] -->
获取更多资讯
