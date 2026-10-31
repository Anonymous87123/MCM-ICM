# P-E-2019-1902029-f44b44ca

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
1902029

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
F1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
T3

<!-- b000010 | prose | pages [1] -->
F3

<!-- b000011 | prose | pages [1] -->
Problem Chosen

<!-- b000012 | prose | pages [1] -->
T4

<!-- b000013 | prose | pages [1] -->
F4

<!-- b000014 | prose | pages [1] -->
E

<!-- b000015 | heading | pages [1] -->
2019 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000016 | prose | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000017 | title | pages [1] -->
Land counts! Better Use & Lower Cost

<!-- b000018 | heading | pages [1] -->
Summary

<!-- b000019 | prose | pages [1] -->
Land use change is a mirror of human-land relationship, which most directly reﬂect- s the impact of human activities on the environment. Estimation of ecosystem service value based on land use/cover change has become the focus of environmental economic- s research.Our paper selects developing countries, which have more land use changes and covers a wide area, as the research object.A land ecosystem service value evalua- tion model based on the unit area value equivalent factor method is constructed, and a dynamic comprehensive assessment of the value of 14 ecosystem types and 11 types of ecological service functions on a spatial scale is realized.

<!-- b000020 | prose | pages [1] -->
We use the model to calculate the ecosystem service value of 14 regions in China, and to verify the validity of the model by comparing with the expert data. After that, we se- lect China’s Yangtze River Delta and Huangguoshu Natural Scenic Spots as examples to analyze the changes in their ecosystem service value over time. According to the cal- culated ecological cost, a cost-beneﬁt analysis model is introduced to study the changes in real economic costs.

<!-- b000021 | prose | pages [1] -->
In order to give more reference to policy makers, we introduce a multi-objective nonlin- ear programming model to study the optimization of land use options under different regional development principles. Taking Jiangsu Province and Heilongjiang Province as examples, we study the sensitivity of ESV and GDP to various land use area changes.

<!-- b000022 | prose | pages [1] -->
The trend of the model changes with time is explored. The seasonal variation of the model is analyzed on the monthly scale during the year. The grey prediction model is established on the scale of the year during the year, and the trend of the short-term model is explored.

<!-- b000023 | prose | pages [1] -->
In general, although further improvements are needed, the evaluation system construct- ed by the thesis provides a relatively comprehensive evaluation plan for the spatial and temporal dynamic assessment of ecosystem service value, thus providing a scientiﬁc ba- sis for natural asset assessment and ecological compensation.

<!-- b000024 | keywords | pages [1] -->
Key words: ecosystem services; value methods; value equivalence factors; dynamic as-

<!-- b000025 | prose | pages [1] -->
sessment.

<!-- b000026 | furniture | pages [2] -->
Team # 1902029

<!-- b000027 | furniture | pages [2] -->
Page 2 of 25

<!-- b000028 | heading | pages [2] -->
Contents

<!-- b000029 | contents | pages [2] -->
1

<!-- b000030 | heading | pages [2] -->
Introduction

<!-- b000031 | prose | pages [2] -->
1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Background 1 Our work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 1 notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3

<!-- b000032 | prose | pages [2] -->
2

<!-- b000033 | heading | pages [2] -->
Assumptions and Justiﬁcations

<!-- b000034 | prose | pages [2] -->
2

<!-- b000035 | prose | pages [2] -->
2

<!-- b000036 | heading | pages [2] -->
A model for ecological services valuation

<!-- b000037 | prose | pages [2] -->
3 3 Basic valuation method . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 Computing VC 4 The Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 4 Ecosystem classiﬁcation . . . . . . . . . . . . . . . . . . . . . 3.3.1 4 Evaluation framework . . . . . . . . . . . . . . . . . . . . . . 3.3.2 4 Standard Equivalent and Base Equivalent . . . . . . . . . . . 3.3.3 6 Sensitivity Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 7 Implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.5 7 Calculation and results . . . . . . . . . . . . . . . . . . . . . . 3.5.1 7 Consistency test . . . . . . . . . . . . . . . . . . . . . . . . . . 3.5.2 8 Evaluation of ecological service value . . . . . . . . . . . . . 3.5.3 9

<!-- b000038 | prose | pages [2] -->
The environmental costs of land use projects 4 11 Large Project - Yangtze River Delta . . . . . . . . . . . . . . . . . . . 4.1 11 Project Description . . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 11 Adjustment of the value of ecological services . . . . . . . . 4.1.2 11 Calculating ESV . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.3 11 Sensitivity analysis . . . . . . . . . . . . . . . . . . . . . . . . 4.1.4 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.5 Advices 13 Small project - Huangguoshu Scenic Area . . . . . . . . . . . . . . . 4.2 13 Project Description . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 13 Adjustment of the value of ecological services . . . . . . . . 4.2.2 13 Calculating ESV . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.3 14 Sensitivity analysis . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4 14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.5 Advices 14 A cost beneﬁt analysis of land use development projects 4.3

<!-- b000039 | prose | pages [2] -->
5 Land Use Project Plan Assessment

<!-- b000040 | prose | pages [2] -->
. . . . . .

<!-- b000041 | prose | pages [2] -->
14

<!-- b000042 | prose | pages [2] -->
15 Multi-objective nonlinear programming model . . . . . . . . . . . . 5.1 15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 Plan Assessment 17 Impact of area change . . . . . . . . . . . . . . . . . . . . . . 5.2.1 17 Policy evaluation . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.2

<!-- b000043 | prose | pages [2] -->
6 Change of time

<!-- b000044 | prose | pages [2] -->
17

<!-- b000045 | prose | pages [2] -->
18 Seasonal change . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 Annual change 19

<!-- b000046 | prose | pages [3] -->
7

<!-- b000047 | heading | pages [3] -->
Strengths and Weaknesses

<!-- b000048 | prose | pages [3] -->
20 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 20 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Weaknesses

<!-- b000049 | prose | pages [3] -->
8

<!-- b000050 | heading | pages [3] -->
Appendix

<!-- b000051 | heading | pages [3] -->
References

<!-- b000052 | references | pages [3] -->
20

<!-- b000053 | references | pages [3] -->
21

<!-- b000054 | references | pages [3] -->
24

<!-- b000055 | furniture | pages [4] -->
Team # 1902029

<!-- b000056 | furniture | pages [4] -->
Page 1 of 25

<!-- b000057 | references | pages [4] -->
1

<!-- b000058 | heading | pages [4] -->
Introduction

<!-- b000059 | prose | pages [4] -->
1.1

<!-- b000060 | heading | pages [4] -->
Background

<!-- b000061 | prose | pages [4] -->
With population growth and economic development, the superposition of human factors and natural factors has caused rapid changes of ecology, depletion of re- sources, shortage of lands, and degradation of environment. One of the legitimate reasons for the above problems is that people do not have a deep understanding of the ecological value of land use.

<!-- b000062 | prose | pages [4] -->
In 1995, the International Geosphere and Biosphere Initiative (IGBP) and the ’Hu- man Areas Program for Global Environmental Change’ (HDP) jointly proposed the ’Land Use/Cover Change’ Research Program (LUCC). So far, the ecological impact of land use change has begun to be widely recognized. Land use change is the result of the continuous adjustment of the purpose of land use. Therefore, it is of great signiﬁcance to study the value of land ecosystem services, to explore the economic beneﬁts of ecosystems from the perspective of value, and to provide scientiﬁc decisions for the planning of social development. Among the various methods of measuring estimates, ecosystem service value assessment is an effec- tive method to measure the environmental impact of land use.

<!-- b000063 | prose | pages [4] -->
Ecosystem service functions are the utility provided by ecosystems to meet and sustain human life needs. Costanza (1997) et al. divided ecosystem services into 17 types and estimated them in monetary terms [1] ; the 2005 Millennium Ecosys- tem Assessment Report divides it into four categories. [2] On this basis, this paper proposes an evaluation method for the value of ecosystem services and conducts a series of empirical studies.

<!-- b000064 | prose | pages [4] -->
1.2 Our work

<!-- b000065 | prose | pages [4] -->
First, based on the ecosystem service value accounting model proposed by Costan- za, we constructed a new ESV accounting model to measure the economic value of ecosystem services, and proposed how to use ESV to analyze its ecosystem service functions in combination with local GDP and area. Using the construct- ed ESV index, we selected 14 regions in China to calculate their ESV levels, and compared the results with the data measured by experts. The results show that our model is effective for measuring land use projects of different scales.

<!-- b000066 | prose | pages [4] -->
Based on the model, we conducted a case study. We selected China’s Yangtze River Delta as a representative of large-scale projects and Huangguoshu Natural Scenic Area as a representative of small-scale projects, to analyze the changes in their ecosystem service value with land use and conducted sensitivity tests. Then, taking into account the ecological costs, we carry out a cost-beneﬁt analysis of the project. Compare the real cost of the project with the economic cost and propose criteria for project evaluation.

<!-- b000067 | furniture | pages [5] -->
Team # 1902029

<!-- b000068 | furniture | pages [5] -->
Page 2 of 25

<!-- b000069 | prose | pages [5] -->
In order to give more reference to policy makers, we have further introduced a multi-objective nonlinear programming model to study the optimization of land use options under different regional development principles. We use Jiangsu Province and Heilongjiang Province as examples to illustrate how policy maker- s should weigh the relationship between economic development and ecological well-being.

<!-- b000070 | prose | pages [5] -->
Finally, since our model is calculated on a yearly basis, we incorporate time changes into the model. In response to seasonal differences in ecosystem ser- vice functions over the course of a year, we introduced dynamic equivalents that changed with the month. In view of the future trends of different ecosystem ser- vices over time, we use the GM (1,1) model to predict short-term development and prospect for long-term development.

<!-- b000071 | prose | pages [5] -->
1.3

<!-- b000072 | heading | pages [5] -->
notation

<!-- b000073 | caption | pages [5] -->
Table 1: List of Notations

<!-- b000074 | prose | pages [5] -->
Symbol Deﬁnition

<!-- b000075 | prose | pages [5] -->
ESV Ecosystem service value Ak Area of ecosystem k V Ck Ecological value coefﬁcient per unit area of ecosystem k Eak Ecological density coefﬁcient of ecosystem k in region a D A standard equivalent factor of ecosystem service value CS Coefﬁcient of Sensitivity(ESV sensitivity to VC) ESC Ecological service capacity GDP Gross Domestic Product Iij The value of land type j in all land types in the year i

<!-- b000076 | prose | pages [5] -->
2

<!-- b000077 | heading | pages [5] -->
Assumptions and Justiﬁcations

<!-- b000078 | prose | pages [5] -->
• Ecosystem services are effective for humans and ecosystem services are scarce. Ecosystem services have become a scarce resource due to the de- struction of the ecological environment by human economic development. At the same time, more and more people recognize the important role that ecosystem services play in human survival. Based on this assumption, e- cosystem services have utility value.

<!-- b000079 | prose | pages [5] -->
• Each unit area of ecosystem serves as a functional unit to provide ecosys- tem services and products. Natural disasters, bad weather and other fac- tors can affect normal ecological functions and reduce ecological value. S- ince this cost of destruction is difﬁcult to measure, this article does not con- sider the damage to the ecology caused by major disasters. Therefore, such

<!-- b000080 | furniture | pages [6] -->
Team # 1902029

<!-- b000081 | furniture | pages [6] -->
Page 3 of 25

<!-- b000082 | prose | pages [6] -->
assumption provides a simplistic but commercial approach for ecosystem service valuation.

<!-- b000083 | prose | pages [6] -->
• The basic model uses a static assessment method that does not take into account the temporal changes in the ecosystem. In the short term, the ecology is basically in balance and the value of ecological services is stable. In an improved model that considers time, this assumption will no longer be valid. The changes in ecological values within a year and between years will be analyzed separately later in this paper.

<!-- b000084 | prose | pages [6] -->
• The ecosystems in the study area are well developed. In the normal evolu- tion of nature, regional ecology is diverse. Based on this assumption, there are enough land types in the study area to provide a basis for our estimation of the value equivalent table.

<!-- b000085 | prose | pages [6] -->
3

<!-- b000086 | heading | pages [6] -->
A model for ecological services valuation

<!-- b000087 | prose | pages [6] -->
3.1 Basic valuation method

<!-- b000088 | prose | pages [6] -->
The human socioeconomic system and natural ecosystems co-exist everywhere. To accurately assess the total economic products and services provided by all human activities, a large and complex statistical system has been established to estimate the gross domestic product (GDP). [3]

<!-- b000089 | prose | pages [6] -->
The ecosystem service value accounting model proposed by Costanza et al. [1] is still the most widely used ecosystem value accounting method. The ecosystem service value evaluation method of this paper is also based on this model and partially improved. The calculation method is based on an equivalent factor. If the monetary value of different ecosystem services from per unit land area can be identiﬁed, the total ESV will be quantiﬁed for the certain ecosystems and regions with the land area of different ecosystems. The formula is as follows:

<!-- b000090 | prose | pages [6] -->
X

<!-- b000091 | prose | pages [6] -->
Ak · V Ck

<!-- b000092 | prose | pages [6] -->
ESV =

<!-- b000093 | prose | pages [6] -->
(1)

<!-- b000094 | prose | pages [6] -->
where ESV is the value of ecological services; Ak is the area of ecosystem k; V Ck is the ecological value coefﬁcient per unit area of ecosystem k.

<!-- b000095 | prose | pages [6] -->
In order to make the ecosystem service value equivalence suitable in different regions and more accurately estimate the value of regional ecosystem services, we introduce the ecological service value equivalent correction coefﬁcient Eak :

<!-- b000096 | prose | pages [6] -->
Eak = Nak/Nk (2)

<!-- b000097 | prose | pages [6] -->
where Nak refers to the eco-environmental quality index of ecosystem type k in re- gion a, and Nk represents the annual average ecology of such ecosystems nation- wide. (The eco-environmental quality index refers to ISO Environmental Quality

<!-- b000098 | furniture | pages [7] -->
Team # 1902029

<!-- b000099 | prose | pages [7] -->
Manual[4].) Thus the model is adjusted:

<!-- b000100 | prose | pages [7] -->
X

<!-- b000101 | prose | pages [7] -->
ESVa =

<!-- b000102 | prose | pages [7] -->
3.2 Computing VC

<!-- b000103 | furniture | pages [7] -->
Page 4 of 25

<!-- b000104 | prose | pages [7] -->
Ak · V Ck · Eak (3)

<!-- b000105 | prose | pages [7] -->
With reference to the research of natural capital by Costanza et al.[1], the Equiva- lent Factor Method is based on the differentiation of different types of ecosystem services, based on quantiﬁable criteria to construct the value equivalence of var- ious service functions of different types of ecosystems, and then combined with the distribution area of the ecosystem to assess [6].

<!-- b000106 | prose | pages [7] -->
V Ck =

<!-- b000107 | prose | pages [7] -->
X

<!-- b000108 | prose | pages [7] -->
V Cki (4)

<!-- b000109 | prose | pages [7] -->
V Cki denotes the ecological value coefﬁcient per unit area of the i-th service type of ecosystem k.

<!-- b000110 | prose | pages [7] -->
In this paper, the equivalent factor method is improved from the horizontal axis index and the vertical axis index. On the basis of the existing equivalent factor table, the classiﬁcation of land use types is enriched (horizontal axis index).Also, the value classiﬁcation equivalent factor method (vertical axis index) based on the service value of different classiﬁcation ecosystems is proposed:

<!-- b000111 | prose | pages [7] -->
V Ck =

<!-- b000112 | prose | pages [7] -->
X

<!-- b000113 | prose | pages [7] -->
V Ckj (5)

<!-- b000114 | prose | pages [7] -->
V Ckj denotes the ecological value coefﬁcient per unit area of the j-th value type of ecosystem k.

<!-- b000115 | prose | pages [7] -->
3.3

<!-- b000116 | heading | pages [7] -->
The Model

<!-- b000117 | prose | pages [7] -->
3.3.1 Ecosystem classiﬁcation

<!-- b000118 | prose | pages [7] -->
Ecosystem refers to the natural complex formed by the interaction and inter- dependence between biomes and their living environment within a certain ge- ographical area. Based on the classiﬁcation of land use and vegetation types, this study identiﬁed six types of ﬁrst-level ecosystems (cultivated land, forest land, grassland, water area, residential construction land, unused land) and 14 types of secondary ecosystems.To comprehensively cover major ecosystem types. Ma- rine ecosystems have not been included in this study due to the lack of systematic research data on the functions and values of marine ecosystem services.

<!-- b000119 | prose | pages [7] -->
3.3.2 Evaluation framework

<!-- b000120 | prose | pages [7] -->
Based on MA’s ecosystem service value assessment framework, integrating the research of Costanza, Turner, de Groot, Dai Junhu, etc., we build the assessment

<!-- b000121 | furniture | pages [8] -->
Team # 1902029

<!-- b000122 | furniture | pages [8] -->
Page 5 of 25

<!-- b000123 | prose | pages [8] -->
framework as shown in ﬁgure 1. The main workﬂow involved consists of four steps:

<!-- b000124 | caption | pages [8] -->
Figure 1: Evaluation framework

<!-- b000125 | heading | pages [8] -->
1. Determination of assess target and the scope of study

<!-- b000126 | prose | pages [8] -->
According to the MA report,ecosystem services are in short abbreviations of ecosystem products and services, referring to all the beneﬁts that human derive from various ecosystems.[7] Ecosystem services and functions do not necessarily present a one-to-one correspondence[1].

<!-- b000127 | heading | pages [8] -->
2. Determination of ecosystem service classiﬁcation system

<!-- b000128 | prose | pages [8] -->
MA divides ecosystem services into four categories:

<!-- b000129 | prose | pages [8] -->
• Support Services (services essential for the production of all other eco- logical services)

<!-- b000130 | prose | pages [8] -->
• Supply Services (from products in the ecosystem)

<!-- b000131 | prose | pages [8] -->
• Regulation Services (obtained from the regulation of ecosystem pro- cesses) Various beneﬁts)

<!-- b000132 | prose | pages [8] -->
• Cultural Services (various non-material gains from ecosystems)

<!-- b000133 | heading | pages [8] -->
3. Value assessment of various ecosystem services

<!-- b000134 | prose | pages [8] -->
Supply services, regulation services, and cultural services often have a rel- atively direct short-term impact on humans. Support services are the back- bone of these three types of ecosystem services. Therefore, we recommend not evaluating support services to avoid double the value of ecosystem ser- vices.

<!-- b000135 | heading | pages [8] -->
4. Classiﬁcation and aggregation of values

<!-- b000136 | prose | pages [8] -->
Considering the research results of Qing Yang, Gengyuan Liu,etc.[5], ac- cording to the principle of non-repetition, we divide the value into three

<!-- b000137 | furniture | pages [9] -->
Team # 1902029

<!-- b000138 | furniture | pages [9] -->
Page 6 of 25

<!-- b000139 | prose | pages [9] -->
categories, and the total value of the ecosystem is the sum of the three val- ues.

<!-- b000140 | prose | pages [9] -->
(a) Direct value represents a product or service in an ecosystem that can

<!-- b000141 | prose | pages [9] -->
be directly consumed by human consumption, including food supply, water supply, and raw material/energy supply.

<!-- b000142 | prose | pages [9] -->
(b) Indirect value represents the value of the ecosystem that does not di-

<!-- b000143 | prose | pages [9] -->
rectly enter the production and consumption process, but provides the necessary conditions for the normal production and consumption, in- cluding gas regulation, hydrological regulation, soil conditioning and puriﬁcation of the environment.

<!-- b000144 | prose | pages [9] -->
(c) Existing value represent indirect services brought about by the exis-

<!-- b000145 | prose | pages [9] -->
tence of ecosystems, including biodiversity, climate regulation, aes- thetic landscapes and cultural education.

<!-- b000146 | prose | pages [9] -->
3.3.3 Standard Equivalent and Base Equivalent

<!-- b000147 | prose | pages [9] -->
Standard Equivalent The standard equivalent (D) is the equivalent factor of the ecosystem service val- ue of a standard unit ecosystem. This paper refers to the calculation method of Xie Gaodi et al. [8], and takes the net proﬁt of grain production per unit area of farmland ecosystem as the standard equivalent. The grain yield value of farm- land ecosystems is mainly calculated based on the three main food products of rice, wheat and corn. The formula is as follows:

<!-- b000148 | prose | pages [9] -->
D = Sr × Fr + Sw × Fw + Sc × Fc (6)

<!-- b000149 | prose | pages [9] -->
Sr,SwandSc respectively represent the percentage of planted area of rice, wheat and corn as a percentage of the total area of the three crops. Fr,FwandFc respec- tively represent the average net proﬁt per unit area of rice, wheat and corn in a country.

<!-- b000150 | prose | pages [9] -->
According to China Statistical Yearbook 2016 [9] and formula (6), the standard equivalent value applicable to China in 2014 is 1827.62 yuan/hm2.

<!-- b000151 | prose | pages [9] -->
Base Equivalent Base equivalent refers to the value coefﬁcient of various service functions per u- nit area of different types of ecosystems, and reﬂects the annual average value level of various ecosystem service functions of different ecosystems. Based on the research results of Zhang Xingyu et al. [6] and the China Statistical Yearbook 2016 [9], we constructed the basic equivalents of different ecosystem types and different value categories, and obtained the following ﬁgure.

<!-- b000152 | furniture | pages [10] -->
Team # 1902029

<!-- b000153 | furniture | pages [10] -->
Page 7 of 25

<!-- b000154 | caption | pages [10] -->
Figure 2: The basic equivalents of different ecosystem types and different value categories

<!-- b000155 | prose | pages [10] -->
3.4

<!-- b000156 | heading | pages [10] -->
Sensitivity Index

<!-- b000157 | prose | pages [10] -->
The Sensitivity Index (CS) was used to determine the sensitivity of the ESV to VC, to test whether the Ecosystem Service Value Factor per Ecosystem is suitable for the ecosystem being assessed. The meaning of CS refers to the change of ESV caused by one percent change of VC. If CS > 1, it indicates that ESV is sensitive and ﬂexible to VC; if CS < 1, it indicates that ESV is inelastic to VC. The greater the ratio, the more critical the accuracy of the VC is for the estimated ESV. CS can be calculated as follows:

<!-- b000158 | prose | pages [10] -->
CS = (ESVj −ESVi)/ESVi

<!-- b000159 | prose | pages [10] -->
(7)

<!-- b000160 | prose | pages [10] -->
(V Cjk −V Cik)/V Cik

<!-- b000161 | prose | pages [10] -->
where VC is the amount of ecological service value per unit area of land, i rep- resents the initial state, j represents the adjusted state, and k is the ecosystem type.

<!-- b000162 | prose | pages [10] -->
3.5 Implementation

<!-- b000163 | prose | pages [10] -->
In this section, we will use the above model to measure the value of ecological services in 14 regions of China, and compare the calculated results with author- itative data to test the validity of the model. In addition, we will measure and analyze the ecological service capacity of different provinces in two ways.

<!-- b000164 | prose | pages [10] -->
3.5.1

<!-- b000165 | heading | pages [10] -->
Calculation and results

<!-- b000166 | prose | pages [10] -->
According to the above standard equivalent and basic equivalent table, the unit area value table of different land use types can be calculated, wherein the total ecological service value of the ﬁrst-level land use type is taken as the average val- ue of the secondary land type value.

<!-- b000167 | prose | pages [10] -->
Among the 14 regions analyzed, the value of ecological services varies greatly among different provinces. Among them, Inner Mongolia Autonomous Region,

<!-- b000168 | furniture | pages [11] -->
Team # 1902029

<!-- b000169 | furniture | pages [11] -->
Page 8 of 25

<!-- b000170 | caption | pages [11] -->
Figure 3: the ESV of 14 provinces in China (Billion yuan)

<!-- b000171 | prose | pages [11] -->
Heilongjiang Province, and Sichuan Province have higher ecological service val- ues, and the ecological value measured by currency amount exceeds 100 billion yuan, mainly because The land use of cultivated land, woodland and grassland in these three provinces is relatively large.

<!-- b000172 | prose | pages [11] -->
In Jiangsu Province, although the cultivated land occupation area is at a medi- um level in 14 provinces and cities, the scarcity of forest land and grassland re- sources makes Jiangsu Province have more than 70 % ESV farmland contribution rate. According to the collected data, the forest land area and grassland area of Jiangsu Province were both among the lowest in the 14 provinces analyzed.

<!-- b000173 | prose | pages [11] -->
3.5.2 Consistency test

<!-- b000174 | prose | pages [11] -->
The article "Costanza model based on the evaluation of the ecological service val- ue of China’s major grain-producing areas" uses the Costanza model to measure the ecological service value of the above 14 provinces. Compare our calculation results with authoritative data to get a scatter plot in ﬁgure 4.

<!-- b000175 | prose | pages [11] -->
Among the provinces we selected, the area varies from 167,000 square kilometers to 1.18 million square kilometers.It can be seen from the ﬁgure that the trends of ESV levels calculated by the two methods are consistent, indicating that our models are suitable for both small and large areas.Therefore, it can be concluded that our model can effectively and objectively assess the value of an ecosystem’s service value.

<!-- b000176 | furniture | pages [12] -->
Team # 1902029

<!-- b000177 | furniture | pages [12] -->
Page 9 of 25

<!-- b000178 | caption | pages [12] -->
Figure 4: Scatter plot comparing the results of two calculations

<!-- b000179 | prose | pages [12] -->
3.5.3 Evaluation of ecological service value

<!-- b000180 | prose | pages [12] -->
In 3.4.1, the value of ecological services in different provinces is quite different, mainly caused by the large difference in land area between different provinces. In order to more objectively evaluate the service capacity of an ecosystem, This paper proposes two ways to eliminate the impact of total area on ecological value assessment.

<!-- b000181 | heading | pages [12] -->
1 Dividing the value of the ecological services in each province by the area of the

<!-- b000182 | prose | pages [12] -->
province gives the value of the ecological services per unit area.

<!-- b000183 | prose | pages [12] -->
ESCi = ESVi/Ai (8)

<!-- b000184 | heading | pages [12] -->
2 Dividing the value of the ecological services in each province by the province’s

<!-- b000185 | prose | pages [12] -->
GDP, the value of the ecological services per unit of GDP per province is obtained.

<!-- b000186 | prose | pages [12] -->
ESCi = ESVi/GDPi (9)

<!-- b000187 | prose | pages [12] -->
By Area

<!-- b000188 | prose | pages [12] -->
The ecological service value per unit area of Jiangsu Province and Shandong Province is less than 1 million yuan/km2, which has weak ecological service ca- pacity.In the future development, the two provinces should increase the empha- sis on the environmental cost of project construction and promote the sustain- able development of the region. The ecological service value per unit area of Jiangxi Province, Hunan Province and Sichuan Province is higher than 3.5 million yuan/km2, indicating that the ecological service capacity is strong. It ˛a´rs Suitable

<!-- b000189 | furniture | pages [13] -->
Team # 1902029

<!-- b000190 | furniture | pages [13] -->
Page 10 of 25

<!-- b000191 | caption | pages [13] -->
Figure 5: Ecological service capacity calculated by unit area

<!-- b000192 | caption | pages [13] -->
Figure 6: Ecological service capability classiﬁcation

<!-- b000193 | prose | pages [13] -->
for people to live, and is conducive to ecological balance and sustainable devel- opment.

<!-- b000194 | prose | pages [13] -->
By GDP

<!-- b000195 | prose | pages [13] -->
Inner Mongolia Autonomous Region and Heilongjiang Province have the high-

<!-- b000196 | caption | pages [13] -->
Figure 7: Ecological service capacity calculated by unit GDP

<!-- b000197 | prose | pages [13] -->
est ecological service capacity, with values of 2.00 and 0.99 respectively, but their corresponding GDP is relatively low.

<!-- b000198 | prose | pages [13] -->
The lowest ecological service capacity is in Jiangsu Province, Beijing Municipali- ty and Shandong Province, and the ecological service capacity accounting values are 0.01, 0.02 and 0.02 respectively. Among them, the GDP level of Shandong Province and Jiangsu Province is very high, and the level of economic develop- ment is at the forefront of the country. In the process of economic construction, the ecology is inevitably damaged. The two provinces should deal with economic value and ecological value in the future development. Weighed and restored the

<!-- b000199 | furniture | pages [14] -->
Team # 1902029

<!-- b000200 | furniture | pages [14] -->
Page 11 of 25

<!-- b000201 | prose | pages [14] -->
service function of the ecosystem and improved the environment on the basis of maintaining a certain level of economic development.

<!-- b000202 | prose | pages [14] -->
Beijing’s ecological service capacity and GDP are at a relatively low level. The possible reason is that Beijing, as a political and cultural center of China, has cer- tain peculiarities. In terms of resource allocation, more consideration should be given to political law and cultural education .As a result, investment in ecological input and economic development is relatively insufﬁcient.

<!-- b000203 | prose | pages [14] -->
The environmental costs of land use projects 4

<!-- b000204 | prose | pages [14] -->
Large Project - Yangtze River Delta 4.1

<!-- b000205 | prose | pages [14] -->
4.1.1 Project Description

<!-- b000206 | prose | pages [14] -->
Yangtze River Delta is located on the eastern coast of the Chinese mainland and has diverse surface cover. The artiﬁcial urban construction land expansion and rapid urbanization lead to rapid changes in land type. [11] Therefore, it is impor- tant to study the environmental costs brought about by land use change here.

<!-- b000207 | prose | pages [14] -->
We obtained land use data of the region from 2010 to 2015 from the Ministry of Natural Resources website. (See Appendix) In the past ﬁve years, the area of forest land, grassland, waters and cultivated land in the Yangtze River Delta has been decreasing, and construction land has increased signiﬁcantly.

<!-- b000208 | prose | pages [14] -->
Adjustment of the value of ecological services 4.1.2

<!-- b000209 | prose | pages [14] -->
In combination with local geography and existing land types, we have made the following adjustments.

<!-- b000210 | caption | pages [14] -->
Table 2: Ecosystem Service Value(yuan/hm2) of Land Use Type in Yangtze River Delta

<!-- b000211 | prose | pages [14] -->
Woodland Grassland Farmland

<!-- b000212 | prose | pages [14] -->
37979.23 12584.42 12000.82

<!-- b000213 | prose | pages [14] -->
4.1.3 Calculating ESV

<!-- b000214 | prose | pages [14] -->
Wetland Waters Unutilized land

<!-- b000215 | prose | pages [14] -->
108001.3 79956.43 734.44

<!-- b000216 | prose | pages [14] -->
Then we calculate ESV of the Yangtze River Delta from 2010 to 2015.(See Ap- pendix)In the past ﬁve years, the ESV of the Yangtze River Delta has decreased year by year, from 560.3 billion yuan in 2010 to 542.7 billion yuan in 2015. Ac- cording to the results, we carry out the following analysis.

<!-- b000217 | furniture | pages [15] -->
Team # 1902029

<!-- b000218 | furniture | pages [15] -->
Page 12 of 25

<!-- b000219 | prose | pages [15] -->
• Analysis by value The Yangtze River Delta has a complex ecosystem and a large population density. We take into account the direct value, indirect value and existence value of all ecosystems in the calculation, and obtain the changes of the three types of values over time. (See Appendix) According to the results, all three values show a downward trend, and the reduction ratio of indirect value and existential value is greater.

<!-- b000220 | prose | pages [15] -->
We can see from ﬁgure 8 that although the expansion of urban construction leads to the simultaneous reduction of the three types of values, in contrast, the indirect value and the existence value of environmental degradation are reduced at a faster rate. However, in real-world decision-making, land man- agers often only consider the decline of direct value, ignoring more serious changes in the indirect value and existing value.

<!-- b000221 | prose | pages [15] -->
• Analysis by various ecosystems Using the ratio of the various ecosystem ESV in 2015 and 2010, the radar map is drawn in ﬁgure 9.

<!-- b000222 | prose | pages [15] -->
The ESV of the aquatic ecosystem is the highest, and the ESV of the grass- land ecosystem is second. In the ﬁve years, the ESV of the waters and wood- land ecosystems has the largest decline. The reason may be that the waters and forests in the Yangtze River Delta are vast in area and have high eco- logical conservation functions, which is of great signiﬁcance for regulating the ecology of the region. As a result, the dramatic reduction in waters and woodlands has led to a signiﬁcant decline in ecosystem services across the region.

<!-- b000223 | prose | pages [15] -->
4.1.4

<!-- b000224 | heading | pages [15] -->
Sensitivity analysis

<!-- b000225 | prose | pages [15] -->
The ecological value coefﬁcient of the land use type is mobilized by 50 % to an- alyze the change of the ecosystem service value and the sensitivity to the value coefﬁcient. The calculation results are shown in the appendix.According to the results, the sensitivity index of the waters is about 0.59; the second is the forest land, the sensitivity index is 0.40. The rest are between 0.1 and 0.4. Taken togeth-

<!-- b000226 | caption | pages [15] -->
Figure 8: Rate of Decline of Three Values Figure 9: The Ratio of ESV of Various E-

<!-- b000227 | prose | pages [15] -->
cosystems

<!-- b000228 | furniture | pages [16] -->
Team # 1902029

<!-- b000229 | furniture | pages [16] -->
Page 13 of 25

<!-- b000230 | prose | pages [16] -->
er, the sensitivity index of ESV to VC is less than 1, indicating that our model is valid.

<!-- b000231 | prose | pages [16] -->
4.1.5 Advices

<!-- b000232 | prose | pages [16] -->
• From the perspective of the type of value It is necessary for us to adopt a more scientiﬁc approach to quantify the indirect value and existential value of losses in urban expansion and to in- corporate them into the assessment system for land-use projects.

<!-- b000233 | prose | pages [16] -->
• From the perspective of the type of ecosystem Land use planners should increase the density of artiﬁcial ditches, while paying attention to the protection of existing water areas and strengthening pollution control.

<!-- b000234 | prose | pages [16] -->
4.2 Small project - Huangguoshu Scenic Area

<!-- b000235 | prose | pages [16] -->
4.2.1 Project Description

<!-- b000236 | prose | pages [16] -->
The Huangguoshu Scenic Area is located in Anshun City, Guizhou Province. From 2009 to 2012, the Huangguoshu Scenic Area was reconstructed and has changed the service value of the ecosystem within a small geographical scope. The ArcGIS 9.2 software was used to export and sort out the land use dynamic data of Huangguoshu Scenic Area from 2009 to 2012 (See Appendix).

<!-- b000237 | prose | pages [16] -->
4.2.2 Adjustment of the value of ecological services

<!-- b000238 | prose | pages [16] -->
The ecological service value of the construction land in Huangguoshu Scenic Area is small, so the value of its ecosystem service function is not estimated. The changes in land use types have an impact on ecosystems only in a small geo- graphical area, and have little impact on the function of ecosystems to regulate climate and maintain biodiversity, so the value of climate regulation and biodi- versity services are not considered. Based on the above adjustment methods, the ecological value equivalents of each land use type in Huangguoshu Scenic Area are obtained.(see in ﬁgure 10)

<!-- b000239 | caption | pages [16] -->
Figure 10: Ecosystem services value unit area of different land types in Huangguosh

<!-- b000240 | furniture | pages [17] -->
Team # 1902029

<!-- b000241 | furniture | pages [17] -->
Page 14 of 25

<!-- b000242 | prose | pages [17] -->
4.2.3 Calculating ESV

<!-- b000243 | prose | pages [17] -->
Using the adjusted ecological value equivalent table and the data of the land use area in each year, the value of the ecosystem service function of the Huangguoshu Scenic Area from 2009 to 2012 is calculated, and the ecological cost of the scenic area reconstruction project is obtained.(See Appendix)

<!-- b000244 | prose | pages [17] -->
It can be seen that the ecological service value of the forest land in Huangguoshu Scenic Area is the largest, accounting for nearly 70% of the total value, followed by cultivated land, waters and gardens. The scenic area renovation project of Huangguoshu caused the total value of its ecological service value to drop by 323,300 yuan in four years, which is the total ecological cost of the scenic area reconstruction project.

<!-- b000245 | prose | pages [17] -->
4.2.4

<!-- b000246 | heading | pages [17] -->
Sensitivity analysis

<!-- b000247 | prose | pages [17] -->
The sensitivity index in Huangguoshu project are calculated (see Appendix). The sensitivity index of various land use types is less than 1, from high to low, fol- lowed by forest land, cultivated land, pasture, water, garden, marsh and tidal ﬂat, and other land, indicating that the ecological service value is inelastic to the change of the ecosystem service value coefﬁcient. The results of this study are credible.

<!-- b000248 | prose | pages [17] -->
4.2.5 Advices

<!-- b000249 | prose | pages [17] -->
The ecological cost of the Huangguoshu scenic area reconstruction project cal- culated by our model is about 323,300 yuan. Considering that forest land con- tributes the most to the value of ecosystem services in scenic spots, Huanggu- oshu Scenic Area should pay attention to the protection of forest land, pasture and other ecological land in future development and improve the overall func- tion of regional land ecosystem services.

<!-- b000250 | prose | pages [17] -->
4.3 A cost beneﬁt analysis of land use development projects

<!-- b000251 | prose | pages [17] -->
From the perspective of cost-beneﬁt analysis, we study the level of beneﬁts before and after considering ecological costs. If ecological costs are not considered, then

<!-- b000252 | prose | pages [17] -->
Totalcost = constructioncost + operatingcost (10)

<!-- b000253 | prose | pages [17] -->
where construction costs are paid in one lump sum at an early stage, and operat- ing costs occur annually.[12] If considering ecological costs, then

<!-- b000254 | prose | pages [17] -->
Totalcost = constructioncost + operatingcost + ecologicalcost

<!-- b000255 | furniture | pages [18] -->
Team # 1902029

<!-- b000256 | furniture | pages [18] -->
Page 15 of 25

<!-- b000257 | prose | pages [18] -->
where the ecological cost is the loss value of the ESV in each year. The total beneﬁt of the land use project is

<!-- b000258 | prose | pages [18] -->
Totalbenefit = economicbenefit + socialbenefit + ecologicalbenefit (12)

<!-- b000259 | prose | pages [18] -->
As shows in ﬁgure 11 and ﬁgure 12:

<!-- b000260 | prose | pages [18] -->
• If the ecological cost is not considered, as time changes, at T1, the total cost and the total beneﬁt curve intersect at point A. In the view of policy mak- ers, all investments are compensated at this time, and the project becomes proﬁtable after T1.

<!-- b000261 | prose | pages [18] -->
• If the ecological cost is considered, the slope and intercept of the total cost curve increase simultaneously.

<!-- b000262 | prose | pages [18] -->
5 Land Use Project Plan Assessment

<!-- b000263 | prose | pages [18] -->
In this section, a multi-objective nonlinear programming model is used to analyze land use scenarios under different priority objectives. Based on the evaluation re- sults in Section 3.5, two typical provinces were selected to evaluate their existing land use policies.

<!-- b000264 | prose | pages [18] -->
5.1

<!-- b000265 | heading | pages [18] -->
Multi-objective nonlinear programming model

<!-- b000266 | prose | pages [18] -->
The land use is the way of using and using the land by humans. [13] Basically, there are four land use principles:(1)Natural growth. (2)Economic de- velopment. (3)Ecological protection. (4)ECO development. Assuming that:

<!-- b000267 | prose | pages [18] -->
1. Land use projects mainly change the number of ecosystem types and types of ecosystems.

<!-- b000268 | prose | pages [18] -->
2. The land use plan of a certain area is not adjusted in a short period of time, and the land use is highly efﬁcient. The ecosystem type of different projects

<!-- b000269 | caption | pages [18] -->
Figure 11: Cost-beneﬁt curve(a)

<!-- b000270 | caption | pages [18] -->
Figure 12: Cost-beneﬁt curve(b)

<!-- b000271 | furniture | pages [19] -->
Team # 1902029

<!-- b000272 | furniture | pages [19] -->
Page 16 of 25

<!-- b000273 | prose | pages [19] -->
has a consistent direction of change, that is, all land use projects in the area are assumed to be of the same direction of inﬂuence to the ecosystem type. (Increase or decrease in area).

<!-- b000274 | prose | pages [19] -->
3. Select the target in the short term, only considering the value change before and after the project.

<!-- b000275 | prose | pages [19] -->
The area of each ecosystem type after the implementation of the land use project can be expressed as Ak + ∇Ak. The calculation method of analogy ESV proposes the accounting method of economic value GDP:

<!-- b000276 | prose | pages [19] -->
X

<!-- b000277 | prose | pages [19] -->
ESV =

<!-- b000278 | prose | pages [19] -->
X

<!-- b000279 | prose | pages [19] -->
GDP =

<!-- b000280 | prose | pages [19] -->
Ak · LV Ck (13)

<!-- b000281 | prose | pages [19] -->
Ak · NV Ck (14)

<!-- b000282 | prose | pages [19] -->
Where:LV Ck indicates Ecological value coefﬁcient per unit area for ecosystem type k(same as V Ck above)ˇc˙zNV Ck indicates Economic value coefﬁcient per unit area for ecosystem type k. Under the ecological protection principle, the model can be constructed as fol- lows:

<!-- b000283 | prose | pages [19] -->
1 + P2 · d−

<!-- b000284 | prose | pages [19] -->
P1 · d+ min

<!-- b000285 | prose | pages [19] -->
2

<!-- b000286 | prose | pages [19] -->
X

<!-- b000287 | prose | pages [19] -->
∇Ak = 0

<!-- b000288 | prose | pages [19] -->
s.t

<!-- b000289 | prose | pages [19] -->
Ak + ∇Ak ≥MinNeedk X

<!-- b000290 | prose | pages [19] -->
X

<!-- b000291 | prose | pages [19] -->
∇Ak · I(∇Ak > 0) · (PCCk + POCk)+

<!-- b000292 | prose | pages [19] -->
∇Ak · I(∇Ak < 0) · ERCk

<!-- b000293 | prose | pages [19] -->
≤min{Budget, Resource}

<!-- b000294 | prose | pages [19] -->
X

<!-- b000295 | prose | pages [19] -->
X

<!-- b000296 | prose | pages [19] -->
∇Ak · I(∇Ak > 0) · PIk ≥

<!-- b000297 | prose | pages [19] -->
X

<!-- b000298 | prose | pages [19] -->
(Ak + ∇Ak) · LV Ck + d−

<!-- b000299 | prose | pages [19] -->
∇Ak · I(∇Ak > 0) · (PCCk + POCk)

<!-- b000300 | prose | pages [19] -->
1 −d+ X

<!-- b000301 | prose | pages [19] -->
(Ak + ∇Ak) · NV Ck + d−

<!-- b000302 | prose | pages [19] -->
1 = MinNeedESV

<!-- b000303 | prose | pages [19] -->
2 −d+ 2 = MinNeedGDP

<!-- b000304 | prose | pages [19] -->
Where:I(∇Ak > 0) and I(∇Ak < 0) are characteristic functions of ∇Ak. d+

<!-- b000305 | prose | pages [19] -->
d− i and

<!-- b000306 | prose | pages [19] -->
i are positive and negative deviation variables.

<!-- b000307 | prose | pages [19] -->
In the above constraints, the ﬁrst formula indicates that the total land area is constant, and the increased land area and the reduced land area cancel each other out. The second formula indicates that the area of each land type after the project is implemented is not less than the minimum need for the land. The capital or resource input in the soil utilization project in a certain area can be divided in- to three parts: project construction investment, ecological restoration investment and project operation input, and the third formula is introduced. The sum of project construction and operating costs for each additional land and the ecolog- ical restoration cost of each reduced land is limited by the amount of budget and resources. The fourth formula indicates that the sum of project beneﬁts from in- creased land is greater than the sum of project construction and operating costs. The last two formulas indicate that ESV and GDP meet the minimum require- ments for them.

<!-- b000308 | furniture | pages [20] -->
Team # 1902029

<!-- b000309 | furniture | pages [20] -->
Page 17 of 25

<!-- b000310 | prose | pages [20] -->
5.2 Plan Assessment

<!-- b000311 | prose | pages [20] -->
5.2.1 Impact of area change

<!-- b000312 | heading | pages [20] -->
According to the previous evaluation results , take Heilongjiang Province and

<!-- b000313 | prose | pages [20] -->
Jiangsu Province as study subject.Through Monte Carlo simulation, take the number of tests N = 200 times, and results go as follow:

<!-- b000314 | prose | pages [20] -->
For Heilongjiang (A1 means forest land and A2 means residential construction land). The impact of forest area change on ESV and GDP is moderate. When the forest area in- creases by more than 2.1%, the forest area elasticity of ecological service value approaches 0. At this time, the forest area approximates a saturation level, and even if the forest area increases signiﬁcantly, it will not contribute to the increase of ecological value.

<!-- b000315 | prose | pages [20] -->
For Jiangsu (A2 means residential construction land and A3 means cultivated land) The ﬁg- ure shows that the percentage change of cultivated land area has a great impact on ecological value and economic value, and the marginal ecological value and marginal economic cost brought by the increase of area show a decreasing trend. The change in the area of residential construction land has a greater impact on GDP and ESV within a certain range. When the percentage change exceeds 0.8% or is lower than -2.4%, the impact on GDP is no longer obvious.

<!-- b000316 | prose | pages [20] -->
5.2.2 Policy evaluation

<!-- b000317 | prose | pages [20] -->
• Heilongjiang Province began to implement the ecological construction s- trategy in 2001. [14] We compare and analyze the value of ecosystem ser- vice function before and after the implementation of land use policy in Hei- longjiang Province. The results show that the various measures of the policy are basically reasonable and can take into account the environmental ben-

<!-- b000318 | caption | pages [20] -->
Figure 13: the impact of area change in Hei-

<!-- b000319 | caption | pages [20] -->
Figure 14:

<!-- b000320 | prose | pages [20] -->
the impact of area change in

<!-- b000321 | prose | pages [20] -->
longjiang

<!-- b000322 | prose | pages [20] -->
Jiangsu

<!-- b000323 | furniture | pages [21] -->
Team # 1902029

<!-- b000324 | furniture | pages [21] -->
Page 18 of 25

<!-- b000325 | prose | pages [21] -->
eﬁts while developing the economy, while efﬁciency of land use should be emphasized in land use policies.

<!-- b000326 | prose | pages [21] -->
• Under the dual role of economic development and land resource manage- ment policies, Jiangsu Province has strengthened the protection of agricul- tural land.However, the results of data analysis show that the economic ag- gregate of Jiangsu Province has expanded rapidly and there is a problem of insufﬁcient applicability of current planning.

<!-- b000327 | prose | pages [21] -->
6 Change of time

<!-- b000328 | prose | pages [21] -->
6.1 Seasonal change

<!-- b000329 | prose | pages [21] -->
During the year, due to changes in climate, temperature and other factors, the val- ue of V Ck is also changing. According to the published statistical documents[15][16], we sort out the amount of ecosystem value according to different months. The changes in the value of ecological services for various ecosystems during the pe- riod from January to December are shown in the ﬁgure15. Among them, the an-

<!-- b000330 | caption | pages [21] -->
Figure 15: Ecosystem value change chart during the year

<!-- b000331 | prose | pages [21] -->
nual service value of residential construction land, desert, bare land and glacial snow is extremely small, and the trend of other ecosystem service value changes is generally the same, with July as the highest point, gradually decreasing to the adjacent months on both sides, January and The lowest point was reached in De- cember.

<!-- b000332 | prose | pages [21] -->
The reason is analyzed. From winter to summer, the temperature rises, the rain- fall increases gradually, the growth of vegetation accelerates, the biomass accu-

<!-- b000333 | furniture | pages [22] -->
Team # 1902029

<!-- b000334 | furniture | pages [22] -->
Page 19 of 25

<!-- b000335 | prose | pages [22] -->
mulation rate of the ecosystem reaches the fastest, and the functions of various ecosystems gradually increase. Therefore, the ecosystems provide the value of ecological services has gradually increased.

<!-- b000336 | prose | pages [22] -->
6.2 Annual change

<!-- b000337 | prose | pages [22] -->
According to the data of different ecosystems in China in 2004, 2008, 2012 and 2016 [17][18][19][20],using gray forecasting analysis, we have predicted future short-term data while long-term changes are expected.As the annual volume u- nits change, we use the importance to measure the proportion of different ecosys- tems in the total ecosystem value in each year. The importance is calculated ac- cording to the following formula:

<!-- b000338 | prose | pages [22] -->
Iij = Vij/Vi (15)

<!-- b000339 | prose | pages [22] -->
Where: The importance level Iij indicates the value of the ecosystem type j in all ecosystem types in the i-th year, Vij represents the value of the ecosystem type in the i-th year, and Vi represents the sum of the values of various ecosystem types in the i-th year.Then, gray prediction and normalization are performed on different ecosystem types to obtain the importance level table.

<!-- b000340 | caption | pages [22] -->
Figure 16: The table of Different ecosystem importance levels

<!-- b000341 | heading | pages [22] -->
The impact of short-term interannual changes on the model

<!-- b000342 | prose | pages [22] -->
With the development of science and technology, technological advancement, and more scientiﬁc planting, the value of cultivated land ecosystems has been enhanced, and there has been no signiﬁcant change in the value of other types of land. The impact of long-term interannual changes on the model The value of short- term cultivated land ecosystems continues to increase, ultimately, due to the re- source constraints of cultivated land ecosystems, the value of cultivated land area will not increase so signiﬁcantly. Also,though the ecological environment value

<!-- b000343 | furniture | pages [23] -->
Team # 1902029

<!-- b000344 | furniture | pages [23] -->
Page 20 of 25

<!-- b000345 | prose | pages [23] -->
of residential construction land ecosystem is minimal or even negative in current study,in the future, with the development of green economy, the implementation of the environmental protection will increase its value by a large margin.

<!-- b000346 | prose | pages [23] -->
7

<!-- b000347 | heading | pages [23] -->
Strengths and Weaknesses

<!-- b000348 | prose | pages [23] -->
7.1

<!-- b000349 | heading | pages [23] -->
Strengths

<!-- b000350 | heading | pages [23] -->
1. Introducing the ecological service value equivalent correction coefﬁcient.

<!-- b000351 | prose | pages [23] -->
The ecological value base equivalent table adopts the national average level. When the ecological value of a certain area is speciﬁcally analyzed, the basic equivalent table can be adjusted according to the local speciﬁc conditions to make the ﬁnal result more accurate.

<!-- b000352 | heading | pages [23] -->
2. Classiﬁcation of ecological service values. When conducting ecological

<!-- b000353 | prose | pages [23] -->
value assessment, the value of ecological services is divided into three cat- egories, thus the scale structure and change trend of various values more intuitively can be analysed.

<!-- b000354 | heading | pages [23] -->
3. Analysis of ecological service capabilities. Dividing the value of regional

<!-- b000355 | prose | pages [23] -->
ecological services by regional area and GDP is conducive to a more com- prehensive evaluation of the stability of the ecosystem, and also to a more intuitive discussion of the relationship between ecological protection and economic development.

<!-- b000356 | heading | pages [23] -->
4. Introduce the concept of a saturated area of value. As the value of marginal

<!-- b000357 | prose | pages [23] -->
utility declines and the land area of a certain type reaches a certain level, its continued growth has almost zero impact on ecological value. This has a good reference for regional land use planning.

<!-- b000358 | prose | pages [23] -->
7.2

<!-- b000359 | heading | pages [23] -->
Weaknesses

<!-- b000360 | heading | pages [23] -->
1. The base equivalent has a certain timeliness. The basis value is judged

<!-- b000361 | prose | pages [23] -->
by the willingness to pay the questionnaire survey, and the resulting value equivalent table can evaluate the ecological value in a short period of time.

<!-- b000362 | heading | pages [23] -->
2. There is a problem of double counting in value. For example, there is

<!-- b000363 | prose | pages [23] -->
a certain cross-value between biodiversity and aesthetic landscape, culture and education, which makes the ﬁnal evaluation value large.

<!-- b000364 | heading | pages [23] -->
3. Part of the value is difﬁcult to quantify or the accuracy may not be high

<!-- b000365 | prose | pages [23] -->
after quantiﬁcation. For example, the value of genetic inheritance, human disease regulation and other functions is difﬁcult to quantify, which will lead to bias in the ﬁnal evaluation results.

<!-- b000366 | furniture | pages [24] -->
Team # 1902029

<!-- b000367 | furniture | pages [24] -->
Page 21 of 25

<!-- b000368 | prose | pages [24] -->
8

<!-- b000369 | heading | pages [24] -->
Appendix

<!-- b000370 | caption | pages [24] -->
Figure 17: Land Use Changes of Yangtze River Delta,2010-2015

<!-- b000371 | caption | pages [24] -->
Figure 18: Changes of Ecosystem Service Value of Yangtze River Delta,2010-2015

<!-- b000372 | furniture | pages [25] -->
Team # 1902029

<!-- b000373 | furniture | pages [25] -->
Page 22 of 25

<!-- b000374 | caption | pages [25] -->
Figure 19: Changes of Three Values of Yangtze River Delta,2010-2015

<!-- b000375 | caption | pages [25] -->
Figure 20: Coefﬁcient of Sensitivity of Yangtze River Delta,2010-2015

<!-- b000376 | caption | pages [25] -->
Figure 21: The dynamic change of land use in Huangguoshu from 2009 to 2012

<!-- b000377 | furniture | pages [26] -->
Team # 1902029

<!-- b000378 | furniture | pages [26] -->
Page 23 of 25

<!-- b000379 | caption | pages [26] -->
Figure 22: The total ESV of different land types in Huangguoshu

<!-- b000380 | caption | pages [26] -->
Figure 23: CS of ecosystem services value of different land types in Huangguoshu

<!-- b000381 | furniture | pages [27] -->
Team # 1902029

<!-- b000382 | furniture | pages [27] -->
Page 24 of 25

<!-- b000383 | heading | pages [27] -->
References

<!-- b000384 | references | pages [27] -->
[1] Costanza R, d ˛a´rArge R, de Groot R, et al. The value of the world ˛a´rs ecosys-

<!-- b000385 | references | pages [27] -->
tem services and natural capital.Nature,1997,387:235-260

<!-- b000386 | references | pages [27] -->
[2] Millennium Ecosystem Assessment (MEA). Ecosystems and HumanWell-

<!-- b000387 | references | pages [27] -->
Being: Synthesis[M]. Washington DC: Island Press, 2005:1-13

<!-- b000388 | references | pages [27] -->
[3] Xie G D,Zhang C X,Zhen L.et al.Dynamic changes in the value of China”s

<!-- b000389 | references | pages [27] -->
ecosystem services[J].Ecosystem Services.2017,26,:146-154.

<!-- b000390 | references | pages [27] -->
[4] ISO Environmental Quality Manual

<!-- b000391 | references | pages [27] -->
[5] Yang, Q., Liu, G., Casazza, M., Campbell, E., Giannettia, B., Brown, M., De-

<!-- b000392 | references | pages [27] -->
cember 2018. Development of a new framework for non-monetary account-

<!-- b000393 | references | pages [27] -->
ing on ecosystem services valuation. Ecosystem Services 34A, 37-54.

<!-- b000394 | references | pages [27] -->
[6] XIE Gao-di, ZHEN Lin, LU Chun-xia, et al. Expert knowledge based valu-

<!-- b000395 | references | pages [27] -->
ation method of ecosystem services in China. Journal of Natural Resources,

<!-- b000396 | references | pages [27] -->
2008, 23(5): 911-919.

<!-- b000397 | references | pages [27] -->
[7] Ecosystem services:

<!-- b000398 | references | pages [27] -->
From eye-opening metaphor to complexity blinder

<!-- b000399 | references | pages [27] -->
Richard B. Norgaard Energy and Resources Group, University of California,

<!-- b000400 | references | pages [27] -->
Berkeley, United States

<!-- b000401 | references | pages [27] -->
[8] XIE Gao-di, LU Chun-xia, LENG Yun-fa, et al. Ecological assets valuation of

<!-- b000402 | references | pages [27] -->
the Tibetan Plateau. Journal of Natural Resources, 2003, 18(2): 189-196.

<!-- b000403 | references | pages [27] -->
[9] National Bureau of Statistics. China Statistical Yearbook 2016 [EB/OL].2016.

<!-- b000404 | references | pages [27] -->
[10] National Bureau of Statistics. China Statistical Yearbook 2017 [EB/OL].2017.

<!-- b000405 | references | pages [27] -->
[11] Liu Guilin, Zhang Luocheng, Zhang Qian. The Impact of Spatial and Tempo-

<!-- b000406 | references | pages [27] -->
ral Changes of Land Use on the Value of Ecosystem Services in the Yangtze

<!-- b000407 | references | pages [27] -->
River Delta[J]. Chinese Journal of Ecology, 2014, 34(12):3311-3319

<!-- b000408 | references | pages [27] -->
[12] Yin Qi. Economic Analysis of Land Use Planning [D]. Zhejiang University,

<!-- b000409 | references | pages [27] -->
2006.

<!-- b000410 | references | pages [27] -->
[13] Wang Xiulan, Bao Yuhai. Discussion on Research Methods of Land Use Dy-

<!-- b000411 | references | pages [27] -->
namic Change[J].Progress in Geography,1999,18(1):81-87.

<!-- b000412 | references | pages [27] -->
[14] Ran Shenghong, Lv Changhe, Jia Kejing, et al. Environmental Impact As-

<!-- b000413 | references | pages [27] -->
sessment of Land Use Change in China Based on Ecological Service Value[J].

<!-- b000414 | references | pages [27] -->
Environmental Science,2006,27(10): 2139-2144.

<!-- b000415 | references | pages [27] -->
[15] National Bureau of Statistics of the People ˛a´rs Republic of China. Chinese

<!-- b000416 | references | pages [27] -->
Statistical Yearbook. Beijing: China Statistics Press, 2011.

<!-- b000417 | references | pages [27] -->
[16] State Forestry Administration of the People ˛a´rs Republic of China. China

<!-- b000418 | references | pages [27] -->
Forestry Statistical Yearbook. Beijing: China Forestry Publishing House,

<!-- b000419 | references | pages [27] -->
2010.

<!-- b000420 | furniture | pages [28] -->
Team # 1902029

<!-- b000421 | furniture | pages [28] -->
Page 25 of 25

<!-- b000422 | references | pages [28] -->
[17] WANG Zong-ming, ZHANG Shu-qing, ZHANG Bai. Effects of land use

<!-- b000423 | references | pages [28] -->
change on the ecosystem service value of Sanjiang Plain[J]. China Environ-

<!-- b000424 | references | pages [28] -->
mental Science, 2004, 24(1): 0-0.

<!-- b000425 | references | pages [28] -->
[18] Xu Xu, Li Xiaobing, Fu Na, et al. Application of Ecosystem Service Value

<!-- b000426 | references | pages [28] -->
Accounting in Strategic Environmental Assessment of Land Use Planning:

<!-- b000427 | references | pages [28] -->
A Case Study of Beijing[J]. Resources Science, 2008, 30(9): 1382-1388 .

<!-- b000428 | references | pages [28] -->
[19] Ouyang Zhiyun, Wang Xiaoke. Preliminary Study on the Service Function

<!-- b000429 | references | pages [28] -->
and Ecological Economic Value of Terrestrial Ecosystem in China[J]. Chinese

<!-- b000430 | references | pages [28] -->
Journal of Ecology, 1999, 19(5): 607-613.

<!-- b000431 | references | pages [28] -->
[20] ZHANG Xing-yi, HUANG Xian-jin, ZHAO Xiao-feng. Accounting of e-

<!-- b000432 | references | pages [28] -->
cosystem service value of land use change in coastal areas of Jiangsu

<!-- b000433 | references | pages [28] -->
Province[J]. Soil and Water Conservation Research, 2015, 22(1): 252-256.
