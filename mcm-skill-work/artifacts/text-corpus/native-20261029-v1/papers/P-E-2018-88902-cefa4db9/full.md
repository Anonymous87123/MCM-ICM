# P-E-2018-88902-cefa4db9

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | title | pages [1] -->
88902

<!-- b000006 | prose | pages [1] -->
T1

<!-- b000007 | prose | pages [1] -->
F1

<!-- b000008 | prose | pages [1] -->
T2

<!-- b000009 | prose | pages [1] -->
F2

<!-- b000010 | prose | pages [1] -->
T3

<!-- b000011 | prose | pages [1] -->
F3

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | title | pages [1] -->
E

<!-- b000014 | prose | pages [1] -->
T4

<!-- b000015 | prose | pages [1] -->
F4

<!-- b000016 | heading | pages [1] -->
2018 MCM/ICM Summary Sheet

<!-- b000017 | title | pages [1] -->
A Probabilistic Model of the Relationships between Countries and

<!-- b000018 | title | pages [1] -->
Climate Change

<!-- b000019 | heading | pages [1] -->
Summary

<!-- b000020 | prose | pages [1] -->
Background Under the effects of climate change, a series of economic, environmental and social problem have emerged from region to region, especially in fragile states. It becomes more and more imperative to develop a sophisticated but easy-to-understand model of the relationships between a country’s fragility and the impact of climate change over it as a guide for the decision and policy makers.

<!-- b000021 | prose | pages [1] -->
Objective The objective of this paper is to propose a probability and machine learning based model called 2THN(2-Time-slice Hybrid Network), as well as two new metrics to measure the fragility(WFSI(Weighted Frag- ile State Index)) and climate change’s impact of the country(CCIC(Climate Change Index by Country)). The whole paper can be divided into five main parts: data collection and pre-process; model representation; param- eter estimation; model analysis; case study and problem solution.

<!-- b000022 | prose | pages [1] -->
Firstly, we identify all the data we would like to use in an ideal situation. But since we cannot get access to some subset of the ideal data, we have to construct our model using a different dataset other than the ex- pected one. Incomplete as it is, it’s sufficient for the purpose of illustrating the main points of our model. Data augmentation, classification, and several normalization methods are also introduced in thispart.

<!-- b000023 | prose | pages [1] -->
Secondly, trying to make the paper easy to read and understand, we then concentrate only on the representa- tions and semantics of our models, leaving out the esoteric mathematical details. We first define our firstmetric - Climate Change Index(CCI), which is a global metric to quantize the degree of climate change. Later on, Cli- mate change vulnerability(CCV) is introduced, which is a state-level metric. We then define the Climate Change Index by Country(CCIC) using CCI and CCV as our second metric. Then Weighted Fragile State Index(WFSI), a revised version of FSI utilizing Analytical Hierarchy Process(AHP) and Entropy Method(EM) is defined, after which we introduce the novel 2-Time-slice Hybrid Network(2THN) to connect the two dots(CCIC and WFSI) and establish an easy-to-understand relationship, where the rationales of our choice of a probabilistic model, as well as other concerns are thoroughly discussed.

<!-- b000024 | prose | pages [1] -->
Thirdly, the details of how the parameters are derived are introduced, including the details of Entropy Method(EM) and the learning and inference of 2THN. Meanwhile, the reasons for our choice to learn both the structure and parameters are discussed.

<!-- b000025 | prose | pages [1] -->
Fourthly, we analyze the properties and characteristics of our model using Mean Value Analysis, correlation analysis, information-theoretical analysis and other analysis to better understand the trained model, where we make our hypothesis of the dynamics of the Climate-Fragility system and justify them by reasoning through the evidence. Furthermore, the notion of Warning Zone(WZ) is introduced, indicating that the latent effects of climate change are invisible to people outside a specific range.

<!-- b000026 | prose | pages [1] -->
Eventually, we come back to the 5 tasks assigned to us in the first place and tackle them using our model one by

<!-- b000027 | prose | pages [1] -->
one. We use K-Means to define the standard line of one country’s fragility state. We take Sudan and Greece

<!-- b000028 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000029 | prose | pages [2] -->
as examples to apply our model in practice, after which we identify some possible strategies taking Sudan’s example again. Finally, we scale our model to the level of continents and discuss the feasibility of scaling it to even cities.

<!-- b000030 | prose | pages [2] -->
Conclusion In general, the models of WFSI-CCIC and 2THN fit well to reality and therefore pragmatic. The fact that the parameters are calculated by analyzing the data instead of fixed gives our model enormous flexibility, making it easy to be applied widely. But meanwhile, its strong dependence on data makes it useless when facing extreme situations such as countries in large scale wars.

<!-- b000031 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000032 | heading | pages [3] -->
Contents

<!-- b000033 | contents | pages [3] -->
1 Introduction············································································································ 1

<!-- b000034 | contents | pages [3] -->
1.1 Background······································································································1

<!-- b000035 | contents | pages [3] -->
1.2 Our Methods···································································································· 1

<!-- b000036 | contents | pages [3] -->
2 Assumption and Acronyms·························································································2

<!-- b000037 | contents | pages [3] -->
2.1 Assumption······································································································2

<!-- b000038 | contents | pages [3] -->
2.2 Acronyms········································································································ 2

<!-- b000039 | contents | pages [3] -->
3 Data·······················································································································2

<!-- b000040 | contents | pages [3] -->
3.1 Data Collection and Augmentation········································································2

<!-- b000041 | contents | pages [3] -->
3.2 Data Classification····························································································· 3

<!-- b000042 | contents | pages [3] -->
3.3 Data Normalization····························································································3

<!-- b000043 | contents | pages [3] -->
3.4 Data Discretization·····························································································3

<!-- b000044 | contents | pages [3] -->
4 Model···················································································································· 3

<!-- b000045 | contents | pages [3] -->
4.1 Climate Change Index by Country(CCIC)······························································· 3

<!-- b000046 | contents | pages [3] -->
4.1.1 Climate Change Index(CCI)········································································· 4

<!-- b000047 | contents | pages [3] -->
4.1.2 Climate Change Vulnerability(CCV)······························································ 4

<!-- b000048 | contents | pages [3] -->
4.2 Weighted Fragile State Index(WFSI)······································································· 5

<!-- b000049 | contents | pages [3] -->
4.3 2-Time-Slice Hybrid Network···············································································5

<!-- b000050 | contents | pages [3] -->
4.3.1 Overview·································································································5

<!-- b000051 | contents | pages [3] -->
4.3.2 Assumptions···························································································· 6

<!-- b000052 | contents | pages [3] -->
4.3.3 Precautions······························································································ 7

<!-- b000053 | contents | pages [3] -->
4.3.4 Inner Structure - Markov Network································································ 7

<!-- b000054 | contents | pages [3] -->
4.3.5 Intra Structure - Bayesian Network································································8

<!-- b000055 | contents | pages [3] -->
5 Parameter Estimation································································································ 9

<!-- b000056 | contents | pages [3] -->
5.1 Weight Calculation·····························································································9

<!-- b000057 | contents | pages [3] -->
5.1.1 Formation Of indicator eigenvalue matrix C······································································ 9

<!-- b000058 | contents | pages [3] -->
5.1.2 Calculating the entorpy of indicators······························································9

<!-- b000059 | contents | pages [3] -->
5.1.3 The coefficient of variation of indicators························································ 10

<!-- b000060 | contents | pages [3] -->
5.1.4 Calculating the weight of entropy································································ 10

<!-- b000061 | contents | pages [3] -->
5.1.5 Normalization of indicator eigenvalue matrix·················································10

<!-- b000062 | contents | pages [3] -->
5.1.6 Fuzzy Comprehensive Entropy Weight Medol················································ 10

<!-- b000063 | contents | pages [3] -->
5.2 Parameters of 2THN························································································· 10

<!-- b000064 | contents | pages [3] -->
5.2.1 Learning································································································ 11

<!-- b000065 | contents | pages [3] -->
5.2.2 Inference································································································ 12

<!-- b000066 | contents | pages [3] -->
6 Analysis················································································································ 12

<!-- b000067 | contents | pages [3] -->
6.1 Intuition·········································································································12

<!-- b000068 | contents | pages [3] -->
6.2 Posterior Mean Value Analysis············································································ 12

<!-- b000069 | contents | pages [3] -->
6.3 Other Analysis·································································································13

<!-- b000070 | contents | pages [3] -->
7 Task 1: Models and Standard Lines··············································································13

<!-- b000071 | contents | pages [3] -->
7.1 Determine the standard line by K-Means Clustering Algorithm··································13

<!-- b000072 | contents | pages [3] -->
7.2 Identifying the Impact of Climate Change······························································14

<!-- b000073 | contents | pages [3] -->
8 Task 2: Case Study - Sudan························································································ 14

<!-- b000074 | contents | pages [3] -->
9 Task 3: Case Study - Greece······················································································· 15

<!-- b000075 | contents | pages [3] -->
9.1 WFSI and CCIC for Greece················································································· 15

<!-- b000076 | contents | pages [3] -->
9.2 Prediction for Greece·························································································16

<!-- b000077 | contents | pages [3] -->
10 Task 4: Possible Strategies························································································ 17

<!-- b000078 | contents | pages [3] -->
11 Task 5: Scalability Analysis·······················································································17

<!-- b000079 | contents | pages [3] -->
12 Strengths and weaknesses························································································19

<!-- b000080 | contents | pages [3] -->
12.1 Strengths·······································································································19

<!-- b000081 | contents | pages [3] -->
12.2 Weaknesses··································································································· 19

<!-- b000082 | contents | pages [3] -->
Reference·················································································································20

<!-- b000083 | contents | pages [3] -->
Appendices·············································································································· 23

<!-- b000084 | furniture | pages [4] -->
Team # 88902

<!-- b000085 | furniture | pages [4] -->
Page 1 of 24

<!-- b000086 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000087 | contents | pages [4] -->
1

<!-- b000088 | heading | pages [4] -->
Introduction

<!-- b000089 | prose | pages [4] -->
1.1

<!-- b000090 | heading | pages [4] -->
Background

<!-- b000091 | prose | pages [4] -->
In 2007, the Intergovernmental Panel on Climate Change (IPCC) first associated the fragile state with climate change. They state that developing countries are particularly vulnerable to the socio- economic impacts of climate change for their dependence on agriculture and high population growth as well as weak infrastructure. The close to 80 percent of the world population that lives in the de- veloping world faces 90 percent of the disasters[1]. Efforts to help fragile states move onto a path toward stability and sustainability continue to face enormous challenges. Climate change is one of these challenges[2]. There is a growing consensus among researchers and policy-makers that cli- mate change represents a real threat to peace and security. Dabelko stated in Climate Change and Fragile States Workshop[3] that climate change can act as a "threat multiplier" and a stressor on state capacities, on communities and on existing conflict dynamics.

<!-- b000092 | prose | pages [4] -->
In order to solve this problem, we have to construct a model with high enough fidelity of the dynamics regarding the whole system. However, we have two main challenges before us:

<!-- b000093 | heading | pages [4] -->
1. It is within these fragile countries that climate information is often the weakest if it exists at

<!-- b000094 | prose | pages [4] -->
all[4]. Attempting to solve this problem, we make effective use of the data by combining multiple data source, conducting sophisticated data preprocessing and augmentation, adding weight control as well as utilizing the expert knowledge. But still, we are suffering from the lack of data.

<!-- b000095 | heading | pages [4] -->
2. The impacts of climate change could be obscured while passing through the fuzzy physical

<!-- b000096 | prose | pages [4] -->
channels for its interconnectedness with development, resource use, health, livelihoods, and economies[3], making it extremely hard to get deep insight of thesystem. To better model the interconnected and uncertain nature of the system, we propose a proba-

<!-- b000097 | heading | pages [4] -->
bilistic model called 2THN(2-Time-slice Hybrid Network), combined with the information and

<!-- b000098 | prose | pages [4] -->
probabilistic theory as well as the most advanced machine learningapproach.

<!-- b000099 | prose | pages [4] -->
1.2 Our Methods

<!-- b000100 | prose | pages [4] -->
The overall objectives of our model is listed as follows:

<!-- b000101 | prose | pages [4] -->
1. Design a comprehensible and pragmatic metric as well a clearly defined standard for the mea- surements of the fragility of and climate change impact over onecountry.

<!-- b000102 | prose | pages [4] -->
2. Establish a probabilistic network with reasonably fidelity to analyze the simultaneous and tem- poral relationships of the five most crucial elements and therefore provide referential sugges- tions for decision and policy makers.

<!-- b000103 | prose | pages [4] -->
x (1 - CCV)

<!-- b000104 | prose | pages [4] -->
CCI

<!-- b000105 | prose | pages [4] -->
CCIC

<!-- b000106 | prose | pages [4] -->
SOCIAL COHESION

<!-- b000107 | prose | pages [4] -->
WFSI

<!-- b000108 | prose | pages [4] -->
POLITICAL ECONOMIC

<!-- b000109 | caption | pages [4] -->
Figure 1: The structure of our model.

<!-- b000110 | furniture | pages [5] -->
Team # 88902

<!-- b000111 | furniture | pages [5] -->
Page 2 of 24

<!-- b000112 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000113 | caption | pages [5] -->
Figure 1 shows the structure of our model.

<!-- b000114 | prose | pages [5] -->
First, we define Climate Change Index(CCI) as a quantified measurement of the global climate change. Second, we manipulate it with Climate Change Vulnerability(CCV) to narrow the global effect of climate change down to a single coun- try, resulting in a new index called Climate Change Index by Country(CCIC). Third, we establish a probabilistic network between CCIC and Weighted Fragile State Index(WFSI), disassembling CCIC into four dimensional sub-indicators, combined with sophisticated weightingmethods.

<!-- b000115 | prose | pages [5] -->
2

<!-- b000116 | heading | pages [5] -->
Assumption and Acronyms

<!-- b000117 | prose | pages [5] -->
2.1

<!-- b000118 | heading | pages [5] -->
Assumption

<!-- b000119 | prose | pages [5] -->
1. The data source is reliable.

<!-- b000120 | prose | pages [5] -->
2. The domestic political situation is relatively stable and large-scale war does not break out in the country while applying our model.

<!-- b000121 | prose | pages [5] -->
3. The main productive forces and social structure won’t change in recentyears.

<!-- b000122 | prose | pages [5] -->
2.2 Acronyms

<!-- b000123 | prose | pages [5] -->
Abbreviation Full Name

<!-- b000124 | prose | pages [5] -->
CI Cohesion Index EI Economic Index PI Policy Index SI Social Index CCI Climate Change Index

<!-- b000125 | prose | pages [5] -->
Abbreviation Full Name

<!-- b000126 | prose | pages [5] -->
C1 Security Apparatus C2 Factionalized Elites C3 Group Grievance E1 Economy E2 Economic Inequality Climate Change Idnex of Country CCIC WFSI Weighted Fragile State Index 2THN 2-Time-slic Hybird Network P3 Human Rights WZ Warning zone S2 Refugees and IDPs FI Factor Indicator E3 Human Flight and Brain Drain P1 State Legitimacy P2 Public Services S1 Demographic Pressures CCV Climate Change Vulnerability X1 External Intervention RI Result Indicator Environmental Performance Index EPI

<!-- b000127 | prose | pages [5] -->
3 Data

<!-- b000128 | prose | pages [5] -->
3.1

<!-- b000129 | heading | pages [5] -->
Data Collection and Augmentation

<!-- b000130 | prose | pages [5] -->
KA K-means Clustering Algorithm

<!-- b000131 | prose | pages [5] -->
To determine a state’s fragility, we use 12 indicators(C1, C2, C3, E1, E2, E3, P1, P2, P3, S1, S2, X1) provided by THE FUND FOR PEACE[30].

<!-- b000132 | prose | pages [5] -->
Annual Average Temperature[31] and Precipitation[32], CO2 Emissions[33], Arable Land[34], Envi- roment Performance Index[35] are used to calculate Climate Change Index of a state.

<!-- b000133 | prose | pages [5] -->
For the first 12 indicators, we download data of 12 years(2006-2017) on 178 countries. To get sufficient data for calculation of CCI, we can only find data of 13 years(2000-2012) on 111 countries. Luckily, the 111 countries are all included in the former 178 countries. So, we finally get data of 7 years(2006-2012) on 111 countries.

<!-- b000134 | prose | pages [5] -->
We didn’t manage to find EPI data of year 2011, so, for the sake of continuity and authenticity of the data, we use the mean value of the year of 2010 and 2012 to fill the blank because the indicator values are comparatively smooth.

<!-- b000135 | furniture | pages [6] -->
Team # 88902

<!-- b000136 | furniture | pages [6] -->
Page 3 of 24

<!-- b000137 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000138 | prose | pages [6] -->
3.2 Data Classification

<!-- b000139 | prose | pages [6] -->
Same as THE FUND FOR PEACE[30], we divide these 12 indicators into four categories(Cohesion Index, Economic Index, Political Index, Social Index) as shown in Figure 3. The reasons to adopt such a hierarchical structure are listed as follows:

<!-- b000140 | prose | pages [6] -->
1. There is a significant knowledge gap among key decision and policy makers around the climate change and environmental risks in fragile states and their impact on the security environment[26]. Toprovide the decision makers with more acceptable instructions, we have to make our model easy to understand.

<!-- b000141 | prose | pages [6] -->
2. Toavoid the extensive computational cost when implementing the algorithms, which will be introduced later.

<!-- b000142 | prose | pages [6] -->
3.3 Data Normalization

<!-- b000143 | prose | pages [6] -->
Accounting for the different scales of the indicators, all our data has been normalized before used in our models.

<!-- b000144 | prose | pages [6] -->
All the 17 indicators can be classified into three types: positive indicators to which the bigger the better, negative indicators to which the smaller the better, and special indicators of which the best value is a fixed value. Suppose there are evaluating indicators counted m, evaluating objects counted n.Inthefollowingequations,cij representstheoriginalvalueofindicatoriforsamplestatej,where i = 1, 2, . . . , n and j = 1, 2, . . . , m. rij is the normalized value of xij.

<!-- b000145 | prose | pages [6] -->
For the positive indicators, there are

<!-- b000146 | prose | pages [6] -->
=

<!-- b000147 | prose | pages [6] -->
rij

<!-- b000148 | prose | pages [6] -->
cij

<!-- b000149 | prose | pages [6] -->
(1)

<!-- b000150 | prose | pages [6] -->
max {cij}

<!-- b000151 | prose | pages [6] -->
For the negative indicators, thereare

<!-- b000152 | prose | pages [6] -->
j j

<!-- b000153 | prose | pages [6] -->
min{cij}

<!-- b000154 | prose | pages [6] -->
rij =

<!-- b000155 | prose | pages [6] -->
j j

<!-- b000156 | prose | pages [6] -->
(2)

<!-- b000157 | prose | pages [6] -->
cij

<!-- b000158 | prose | pages [6] -->
For the special indicator, we must choose a best-fixed value. In our model, PRI, TASI and ALI belong to this kind. We calculate the average value of each country as the best value for that country due to different national conditions. The normalization equation is:

<!-- b000159 | prose | pages [6] -->
−.

<!-- b000160 | prose | pages [6] -->
rij = 1 cij−Aij

<!-- b000161 | prose | pages [6] -->
(3)

<!-- b000162 | prose | pages [6] -->
.max{|cij −Aij|}.

<!-- b000163 | prose | pages [6] -->
j .

<!-- b000164 | prose | pages [6] -->
where, Aij is the best value for the jth indicator on the ith country. If rij equals to 0, we reassign it to 0.0001.

<!-- b000165 | prose | pages [6] -->
3.4 Data Discretization

<!-- b000166 | prose | pages [6] -->
In order to utilize the computer to simulate our model and to make our model more comprehen- sive, we discretize our results into 10 intervals using the K-means algorithm.

<!-- b000167 | prose | pages [6] -->
4

<!-- b000168 | heading | pages [6] -->
Model

<!-- b000169 | prose | pages [6] -->
Climate Change Index by Country(CCIC) 4.1

<!-- b000170 | furniture | pages [7] -->
Team # 88902

<!-- b000171 | furniture | pages [7] -->
Page 4 of 24

<!-- b000172 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000173 | prose | pages [7] -->
To establish the network between climate change and fragility of a country, we first de- sign a metric to quantize the impact of climate change on different countries. There are two steps as follows:

<!-- b000174 | heading | pages [7] -->
1. Define CCI(Climate Change Index).

<!-- b000175 | heading | pages [7] -->
2. Multiply CCI with CCV(Climate Change

<!-- b000176 | prose | pages [7] -->
Vulnerability) to get CCIC.

<!-- b000177 | prose | pages [7] -->
4.1.1 Climate Change Index(CCI)

<!-- b000178 | prose | pages [7] -->
According to the IPCC(Intergovernmental Panel on Climate Change), climate change refers to "a change in the state of the climate that can be identified .. . by changes in the mean and/or the variability of its properties, and that per-

<!-- b000179 | caption | pages [7] -->
Figure 2: Climate Change Index(CCI)

<!-- b000180 | prose | pages [7] -->
sists for an extended period, typically decades or longer"[5].

<!-- b000181 | prose | pages [7] -->
There are many related professional indexes used to measure climate change, but most of them include high weights of unnatural indica-

<!-- b000182 | prose | pages [7] -->
tors(e.g., CCPI(Climate Change Performance Index) weights climate policy as 20%[7]), which are not desired in our case for the presence of CCV(Climate Change Vulnerability). Therefore, we establish a new metric ourselves by combining two categories consisting of only natural indicators and weight them: factor indicator and result indicator as shown in Figure 2.

<!-- b000183 | prose | pages [7] -->
Factor indicators(FI) are variables which directly influence the climate, such as temperature, solar radiation intensity, precipitation and carbon emission. Result indicator(RI) is on the opposite, which is the natural phenomenon, which indicates the degree of climate change reversely. It includes biodi- versity, arable land, sea level change, natural disasters and so on. Here, we only gained the access to complete historical metadata for three FI and one RI by country due to the access right and time limitation. Hence, we turned to a processed data index which is so-called Environmental Performance Index(EPI). According to the Yale Center for Environmental Law & Policy (2018), EPI consists of many RIs like forest(5%), biodiversity(12.5%), water resource(12.5%) and so on.

<!-- b000184 | prose | pages [7] -->
CCI = WT × Indexnorm

<!-- b000185 | prose | pages [7] -->
where WT means the weight vector and Indexnorm is the normalized value vector of a country.

<!-- b000186 | prose | pages [7] -->
The equation above is processed to grade the degree of climate change, which we will discuss in detail later in Parameter Estimation Section. That is, if a country gets a high score, which is approaching 1, this country doesn’t suffer much from climate change.

<!-- b000187 | prose | pages [7] -->
4.1.2 Climate Change Vulnerability(CCV)

<!-- b000188 | prose | pages [7] -->
Due to geographical location or socio-economic condition, some countries are more vulnerable to the impacts of climate change than others. ND-GAIN[6] assesses the vulnerability of a country by considering six life-supporting sectors: food, water, health, ecosystem services, human habitat and infrastructure, which can be quantized respectively by a real number between 0 to 1. The higher the number, the more likely the country will suffer from the impact of climate change. Wetake this metric as climate change vulnerability(CCV), and multiplied the processed CCI to getCCIC:

<!-- b000189 | prose | pages [7] -->
CCIC = CCI × (1 −CCV )

<!-- b000190 | prose | pages [7] -->
where the CCIC will become fairly large when CCI is approaches 1 or CCV is approaches 0.

<!-- b000191 | furniture | pages [8] -->
Team # 88902

<!-- b000192 | furniture | pages [8] -->
Page 5 of 24

<!-- b000193 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000194 | prose | pages [8] -->
4.2 Weighted Fragile State Index(WFSI)

<!-- b000195 | prose | pages [8] -->
Weighting model is essential to evaluate the different contribution of the indicators, especially in our case. Here, we assume that the four categories (cohesion, economic, political and social) have the same importance for the time being. However, if expert knowledge is accessible, we can use AHP(Analytical Hierarchy Process) to give a more sophisticated overall weighting strategy while we use EM(Entropy Method)(details will be discussed later in Parameter Estimation Section) to weight the 12 sub-factors based on the historical data.

<!-- b000196 | caption | pages [8] -->
Figure 3: Weighted Fragile State Index(WFSI)

<!-- b000197 | prose | pages [8] -->
We respectively apply EM to the four indicators, each of which consists of another three sub- factors, which is shown in Figure 3.

<!-- b000198 | prose | pages [8] -->
Once we get the result from EM, we then multiply it by the FSI we already have, whose result is exactly what we need.

<!-- b000199 | prose | pages [8] -->
4.3 2-Time-Slice Hybrid Network

<!-- b000200 | prose | pages [8] -->
4.3.1 Overview

<!-- b000201 | prose | pages [8] -->
We now have the normalized measurements of the four most crucial indicators we obtained by utilizing EM. To better study the interactions between these four indicators, we then formulate its inner structure and the temporal effects across them into a 2-Time-slice Hybrid Network(2THN).

<!-- b000202 | heading | pages [8] -->
Specifically, we combine the undirected Markov Network(MN) model with the directed Bayesian

<!-- b000203 | prose | pages [8] -->
Network(BN) model, which can be illustrated by figure 4.

<!-- b000204 | prose | pages [8] -->
But why probabilistic models? Although determinism is indeed a very valuable property in mod- eling, taking the massive uncertainty and noises into consideration, for even a modest problem, giv- ing an exact answer is often infeasible [14], leave alone such a complicated one. Furthermore, accord- ing to Dan Smith and Janani Vivekananda [15], there is at least three dimensions’ uncertainty under the context of climate change’s effects:

<!-- b000205 | prose | pages [8] -->
1. The precise physical effects are uncertain, including their scale andgeography.

<!-- b000206 | prose | pages [8] -->
2. The knock-on social consequences are uncertain.

<!-- b000207 | furniture | pages [9] -->
Team # 88902

<!-- b000208 | furniture | pages [9] -->
Page 6 of 24

<!-- b000209 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000210 | prose | pages [9] -->
3. The third dimension uncertainty lies in the lack of clear and tested policy prescriptions to guide the response.

<!-- b000211 | prose | pages [9] -->
Probabilistic networks(PNs), also known as Bayesian networks(BNs), are already well established as representations of domains involving such uncertain relations among a group of random vari- ables [10], therefore becomes an eligible candidate. Another reason is that the data is seldom complete in real life, which is also well supported by probabilistic models both in theory and in practice. More- over, the separation of knowledge and reasoning [12] in probabilistic models decouples the system’s overall complexity.

<!-- b000212 | caption | pages [9] -->
Figure 4: Overview of the 2THN model.

<!-- b000213 | prose | pages [9] -->
During our research, we found most of the models are either pure Bayesian networks or pure Markov networks but rarely both. So we feel it necessary to defend our choice of such a hybrid sys- tem. We have known that the impact between the indicators are mutual and intricate and the inner structure can even be cyclic. Hence, the impact one indicator imposes on the others will eventually and inevitably affect itself, which makes this problem problematic. Neither Bayesian networks nor Markov networks alone can model the pairwise relationships and the temporal dynamics simultane- ously, which leads to our hybrid system - 2THN.

<!-- b000214 | prose | pages [9] -->
In our model of 2THN, the dashed-lined area represents the template part, whose structure will be replicated to other adjacent time slices. The original inspiration is the so-called 2-time-slice bayesian network(2TBN), where all the links are directed and acyclic. In order to capture more traits of the interconnected nature of such a fuzzy system, we combine it with another probabilistic graph- ical model, Markov network, which is undirected. The whole model can be taken into two parts -

<!-- b000215 | heading | pages [9] -->
inner-time-slice model and intra-time-slice model. The inner-time-slice model is used to analyze

<!-- b000216 | prose | pages [9] -->
the instant effects and the simultaneous relationships within our four-indicator fragility model while the intra-time-slice model is used to analyze the temporal effect among the four different indicators.

<!-- b000217 | prose | pages [9] -->
4.3.2

<!-- b000218 | heading | pages [9] -->
Assumptions

<!-- b000219 | prose | pages [9] -->
To simplify our model, we make the following two assumptions for the directed intra-time-slice

<!-- b000220 | heading | pages [9] -->
model:

<!-- b000221 | heading | pages [9] -->
1. Markov Assumption

<!-- b000222 | prose | pages [9] -->
Because we decide to use a template model to make the model more general, we assume the conditional probability distribution of future states of the process depends only upon the present state, not on the sequence of events that preceded it [13]. That is to say, once you know the current state, you don’t care about the past anymore, therefore you forget about the past. Specifically, the fragility of the next year only depends on the environments of the current year instead of a trajectory of the past years. This assumption can be expressed precisely using the following mathematical expressions:

<!-- b000223 | prose | pages [9] -->
Given:

<!-- b000224 | prose | pages [9] -->
(X(t+1) ⊥X(0:t−1)|X(t))

<!-- b000225 | furniture | pages [10] -->
Team # 88902

<!-- b000226 | furniture | pages [10] -->
Page 7 of 24

<!-- b000227 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000228 | prose | pages [10] -->
Then:

<!-- b000229 | prose | pages [10] -->
where Xt is the random variables(nodes) in time slice t.

<!-- b000230 | heading | pages [10] -->
2. Time Invariance

<!-- b000231 | prose | pages [10] -->
We further assume the dynamics of the system don’t depend on the time in our model, which is to say, for all given t, we have:

<!-- b000232 | prose | pages [10] -->
P(X(t+1)|X(t)) = P(X

<!-- b000233 | prose | pages [10] -->
|X)

<!-- b000234 | prose | pages [10] -->
j

<!-- b000235 | prose | pages [10] -->
j denotes the next time slice and X denotes the current time slice, therefore we can

<!-- b000236 | prose | pages [10] -->
where X

<!-- b000237 | prose | pages [10] -->
replicate the same model to every transition instead of creating one for each of them.

<!-- b000238 | prose | pages [10] -->
4.3.3 Precautions

<!-- b000239 | prose | pages [10] -->
An important parameter of our model is the time granularity ∆T . We set it to one year for the time being in order to make it easier to get valid data. But this interval can be reset to a smaller value if enough data becomes available in the future.

<!-- b000240 | prose | pages [10] -->
Another very important point worth caution is that the inner-time-slice model and the intra-time- slice model should never be mixed up remissly. These two pieces are designed for different dynamics and different purposes. All models are wrong, but some are useful [9]. If you are mixing them up, you are risking confusing the map with the territory. As Lee states in Plato and theNerd:

<!-- b000241 | prose | pages [10] -->
Models are human constructions. Modeling paradigms are also human constructions. Therefore, both are subject to creativity. They are invented not discovered[8].

<!-- b000242 | prose | pages [10] -->
Therefore, models are also subject to the context of the concrete problem. Hence, we would like to restate the subtlety here although mentioned previously:

<!-- b000243 | heading | pages [10] -->
1. Inner Structure - Markov Network

<!-- b000244 | prose | pages [10] -->
In our model, it captures the intricate pairwise and simultaneous relationships between the four indicators. It can be used to analyze the integrative node-node interactions without the notion of time, therefore to better understand the whole system.

<!-- b000245 | heading | pages [10] -->
2. Intra Structure - Dynamic Bayesian Network

<!-- b000246 | prose | pages [10] -->
In our model, it models the dynamics of the system over a time series. It enables us to monitor and update the overall system as time proceeds, and make future predictions, which is the central model of the following discussion.

<!-- b000247 | prose | pages [10] -->
4.3.4 Inner Structure - Markov Network

<!-- b000248 | prose | pages [10] -->
We learned the following Markov network from data, representing the pairwise relationships between the five indicators. The lines between the nodes denote the mutual interactions of these indicators.

<!-- b000249 | prose | pages [10] -->
For each edge between two of the five indicators(Economic E, Cohesion C, Political P , Social S and CCIC CCIC) X, Y , there is an associated factor(aka. affinity function, compatibility function, soft constraints) φij(X, Y ), which is a replacement of the conditional probability in a Bayesian net- work. The factor represents the local happiness of the variable [12] X and Y to take a particular joint assignment. We can get such factors through some particular algorithms which will be introduced in parameter estimation.

<!-- b000250 | prose | pages [10] -->
Having all the factors in our model, we are able to calculate the product of factors P˜Φ:

<!-- b000251 | furniture | pages [11] -->
Team # 88902

<!-- b000252 | furniture | pages [11] -->
Page 8 of 24

<!-- b000253 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000254 | caption | pages [11] -->
Figure 5: The inner structure of 2THN.

<!-- b000255 | prose | pages [11] -->
(4)

<!-- b000256 | prose | pages [11] -->
whereω isthe coefficient,f isthe feature function andDi isthe jth factor,e.g. (C,P),(S,E). Then we can normalize it using:

<!-- b000257 | prose | pages [11] -->
P(E, C, P, S, CCIC) = 1 P˜ (E, C, P, S, CCIC)

<!-- b000258 | prose | pages [11] -->
where Z is called the partition function:

<!-- b000259 | prose | pages [11] -->
Σ

<!-- b000260 | prose | pages [11] -->
(5) Φ Z

<!-- b000261 | prose | pages [11] -->
P˜Φ(E, C, P, S, CCIC) Z = (6)

<!-- b000262 | prose | pages [11] -->
A relatively subtle point of the Markov network model is that there isn’t a natural mapping be- tween the probability distribution and the factors. This means we have to explicitly specify the fac- torizations. Here, we claim this network to be a pairwise network in order to do so. Note further, the pairwise factor is commutative in our model, so there are 7 factors in total in this network, listed as follows:

<!-- b000263 | prose | pages [11] -->
(P, C); (C, S); (S, E); (E, CCI).

<!-- b000264 | prose | pages [11] -->
4.3.5 Intra Structure - Bayesian Network

<!-- b000265 | prose | pages [11] -->
Tovisualize the conditionaldependencies across time slice, we use the directed acyclic graph(DAG), shown as Figure 6:

<!-- b000266 | caption | pages [11] -->
Figure 6: The intra structure of 2THN.

<!-- b000267 | prose | pages [11] -->
For each node in the DAG, there exists a probability distribution function(pdf), whose dimension and definition depends on the edges leading to that node. In our example, the dashed line denotes

<!-- b000268 | furniture | pages [12] -->
Team # 88902

<!-- b000269 | furniture | pages [12] -->
Page 9 of 24

<!-- b000270 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000271 | prose | pages [12] -->
so-called "persistence link", which links the same node from t to t + 1(the unprimed node to the primed node). The solid link denotes the other dependencies between different nodes. This structure is replicated for all the given time ti to ti + 1 while in this graph we only show 2 steps. So for a trajectory over 0, 1, ..., T , we can then unroll the template network to a flattened ground network. That is to say, we can, therefore, make predictions over an arbitrarily long time series using some inference algorithms, which enables us to get insights of the deep causal relationships among the 5 elements.

<!-- b000272 | prose | pages [12] -->
The joint probability distributions can then be calculated using the chain rule according to Equa- tion 7.

<!-- b000273 | prose | pages [12] -->
j is the set of random variables in the next time slice, X is the random variables in the

<!-- b000274 | prose | pages [12] -->
where X

<!-- b000275 | prose | pages [12] -->
j .

<!-- b000276 | prose | pages [12] -->
current time slice, and PaXj is all the parents of X

<!-- b000277 | prose | pages [12] -->
i i

<!-- b000278 | prose | pages [12] -->
5 Parameter Estimation

<!-- b000279 | prose | pages [12] -->
In this section, how to determine the weight of the 12 fragility indicators as well as how the structure and parameters of 2THN model are determined are introduced.

<!-- b000280 | prose | pages [12] -->
5.1 Weight Calculation

<!-- b000281 | prose | pages [12] -->
5.1.1 Formation Of indicator eigenvalue matrix C

<!-- b000282 | prose | pages [12] -->
Suppose there are evaluating indicators counted m, evaluating objects counted n, then forms the indicator eigenvalue matrix C = (cij)m×n

<!-- b000283 | prose | pages [12] -->
where cij is the data of the jth evaluating object on the ith indicator

<!-- b000284 | prose | pages [12] -->
5.1.2 Calculating the entorpy of indicators

<!-- b000285 | prose | pages [12] -->
Information entropy is the measurement of the disorder degree of a system[28]. When the differ- ence of the value among the evaluating objects on the same indicator is high, while the entropy is small, it illustrates that this indicator provides more useful information. On the other hand, if the difference is smaller and the entropy is higher, the indicator provides less useful information.[29]

<!-- b000286 | prose | pages [12] -->
(9)

<!-- b000287 | prose | pages [12] -->
In which,

<!-- b000288 | prose | pages [12] -->
where ei is the entropy of the ith indicator, ei>0.

<!-- b000289 | furniture | pages [13] -->
Team # 88902

<!-- b000290 | furniture | pages [13] -->
Page 10 of 24

<!-- b000291 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000292 | prose | pages [13] -->
5.1.3 The coefficient of variation of indicators

<!-- b000293 | prose | pages [13] -->
gi = 1 −ei where gi is coefficient of variation. The larger the gi is, the more significant the ith indicator is to the model.

<!-- b000294 | prose | pages [13] -->
5.1.4 Calculating the weight ofentropy

<!-- b000295 | prose | pages [13] -->
where wi is the weight of the ith indicator.

<!-- b000296 | prose | pages [13] -->
If each evaluating object on the ith evaluation indicator is exactly the same, the entropy reaches the maximum value of 1 and the corresponding weight is 0, which means this indicator provides nothing useful for the decision maker, that is to say, it can be ignored. In contrast, if each evaluating object varies on one indicator, then the entropy of the indicator is small and the weight is high, indicating that the indicator provides more useful information and should be focused on.

<!-- b000297 | prose | pages [13] -->
Normalization of indicator eigenvalue matrix 5.1.5

<!-- b000298 | prose | pages [13] -->
According to aforementioned three methods of data normalization, normalize equation (8) to get equation (11)

<!-- b000299 | prose | pages [13] -->
where rij is the data of the jth evaluating object on the ith indicator, and rij ∈[0, 1].

<!-- b000300 | prose | pages [13] -->
Fuzzy Comprehensive Entropy Weight Medol 5.1.6

<!-- b000301 | prose | pages [13] -->
According to the definition of membership matrix, the relative optimal membership degree vec- tors of inferior and superior ones are respectively:

<!-- b000302 | prose | pages [13] -->
b = (0 0

<!-- b000303 | prose | pages [13] -->
h = (1 1

<!-- b000304 | prose | pages [13] -->
··· 0)T 0 0

<!-- b000305 | prose | pages [13] -->
··· 1)T 1 1

<!-- b000306 | prose | pages [13] -->
The optimal membership degree of the evaluating object is:

<!-- b000307 | prose | pages [13] -->
5.2 Parameters of 2THN

<!-- b000308 | prose | pages [13] -->
(12)

<!-- b000309 | prose | pages [13] -->
Recall that previously we have introduced the representation of the 2THN model. but we haven’t dived into the details of how to apply such model yet. One essential work of constructing probability

<!-- b000310 | furniture | pages [14] -->
Team # 88902

<!-- b000311 | furniture | pages [14] -->
Page 11 of 24

<!-- b000312 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000313 | prose | pages [14] -->
networks is to learn its parameters, including its structure and conditional probability distributions, after which we can then conduct inference on the unknown data or updating the existing model. Here we will briefly introduce the mechanisms of such process using the intra-time-slice Bayesian network(figure 6 ) as an example, leaving out the Markov network to avoidduplicates.

<!-- b000314 | furniture | pages [15] -->
Team # 88902

<!-- b000315 | furniture | pages [15] -->
Page 12 of 24

<!-- b000316 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000317 | prose | pages [15] -->
5.2.1 Learning

<!-- b000318 | prose | pages [15] -->
Although extensive researches have been done upon the relationships among the four indicators and the impact of climate change[17, 18, 19, 20], none of them considered all of the five as a whole.Fur- thermore, according to the report of the Climate Change and Fragile States Workshop held on September 28 and 29, 2011[3], perfect knowledge is not available, especially in contexts of fragility and it’s essen- tial to step back from our understandings and assumptions and think openly and holistically.

<!-- b000319 | prose | pages [15] -->
Learning the structure of the Bayesian network model that represents a domain can reveal in- sights into its underlying causal structure[21] while learning the parameters can reveal the details of how the nodes are connected, which exactly embodies the concepts addressed above - to think openly and holistically. Another benefit we can get from utilizing this strategy is that continuously updating both the structure and the parameters becomes easy, making it possible for the model to evolve over time with more and more data fed in. Hence, both the structure and parameters of our model are learned from data, concretely, we use the pgmpy python library[23] for the implementation.

<!-- b000320 | prose | pages [15] -->
Tosummarize, the overall strategy is to use a score function to rate each net- Structure Learning work and choose the one with the best score. Given the data set D, the structure G’s score is:

<!-- b000321 | prose | pages [15] -->
Score(D, G) = P (G|D) = P (D|G)P (G)

<!-- b000322 | prose | pages [15] -->
P(D)

<!-- b000323 | prose | pages [15] -->
which is the posterior probability of G given data D. Note that the denominator is fixed for a given data set, so our task reduces to maximize the numerator P(D|G)P(G). To further simplify the problem, we assume a uniform prior distribution over P(G)(see Heckerman[22] for other discussions), therefore P(D|G) is the only one left:

<!-- b000324 | prose | pages [15] -->
where p is the weight by the posterior probability of all the possible parameters. For multinomial PDFs[16]:

<!-- b000325 | prose | pages [15] -->
where αijk and Nijk are the hyperparameters, which counts for the probability distribution func- tion of Xi for parent configuration j.

<!-- b000326 | prose | pages [15] -->
This process can be complicated for two main reasons:

<!-- b000327 | prose | pages [15] -->
(1) Difficulties in inferring causality.

<!-- b000328 | prose | pages [15] -->
(2) The exponential number of directed edges that are possible for a givendataset.

<!-- b000329 | prose | pages [15] -->
To tackle these problems, we choose to use Greedy Hill Climbing algorithm with a reduced factor set(keep only 5 elements). But while we gained better performance through this approach, we are also faced with the risk of getting stuck in a local optimum, which can be well solved by applying random restarts.

<!-- b000330 | prose | pages [15] -->
Parameter Learning Parameter learning is relatively less problematic than structure learning, it is similar to many common parameter training algorithms in the field of machine learning. We use the normalized data as input, then train the previously constructed network using Maximum Likelihood Estimation(MLE[24]) to get the conditional probability distributions of every random variable.

<!-- b000331 | furniture | pages [16] -->
Team # 88902

<!-- b000332 | furniture | pages [16] -->
Page 13 of 24

<!-- b000333 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000334 | prose | pages [16] -->
5.2.2 Inference

<!-- b000335 | prose | pages [16] -->
In general, a computation of a probability of interest given a model is known as probabilistic infer- ence[22]. Having the joint distribution of X, in principle, we can compute any probability of interest about X. Typically, we will be in a situation where some evidence is observed so that we can infer something else about other variables. Generally, the queries can be expressed using the following

<!-- b000336 | prose | pages [16] -->
|

<!-- b000337 | prose | pages [16] -->
question: "What is the whole probability distribution over variable X given evidence e, P (X e)?[25]" Con- cretely, given the query variables X, observed evidence E = e and unobserved variables Y:

<!-- b000338 | prose | pages [16] -->
which means to simply sum over all the variables not involved in the query. For other more sophisticated inference methods, see Butz, et al[27].

<!-- b000339 | prose | pages [16] -->
6 Analysis

<!-- b000340 | prose | pages [16] -->
6.1 Intuition

<!-- b000341 | prose | pages [16] -->
We can easily draw the following intuitive conclusions from both Figure 5 and Figure 6:

<!-- b000342 | heading | pages [16] -->
1. CCIC can affect economic directly since they are connected directly in bothgraph.

<!-- b000343 | heading | pages [16] -->
2. CCIC can affect all the other three elements indirectly through the flow ofinfluence.

<!-- b000344 | prose | pages [16] -->
These conclusions are rather intuitive, hence easy to understand. We will then try to justify the above intuitions using some formal methods and gain further understanding of the dynamics of this system.

<!-- b000345 | prose | pages [16] -->
6.2 Posterior Mean Value Analysis

<!-- b000346 | prose | pages [16] -->
The most direct way to understand how one element may affect the other is to visualize it. Since we already considered the country’s vulnerability in CCIC, we can then synthesize all the 111 coun- tries’ data to conduct the posterior mean analysis.

<!-- b000347 | prose | pages [16] -->
The results of the four indicators are rather similar(Figure 8). From the four wired curves caused by CCIC, we can see that CCIC is not al- ways linearly correlated with the other four in- dicators(recall that CCIC is considered to be the larger the better). Weinterpret this phenomenon by the following hypothesis:

<!-- b000348 | prose | pages [16] -->
(1) Within a reasonable range, concretely (0,

<!-- b000349 | heading | pages [16] -->
0.2) in our model(we call it the Warn- ing

<!-- b000350 | prose | pages [16] -->
Zone(WZ)), CCIC can effectively pro- mote or diminish all the other four indica- tors, whose impact can be approximately considered as positively linear.

<!-- b000351 | prose | pages [16] -->
(2) After WZ, CCIC’s impact gradually re-

<!-- b000352 | prose | pages [16] -->
cedes, ultimately exercises no or even neg- ative impacts on the other four dimen- sions’ performance.

<!-- b000353 | prose | pages [16] -->
CCIC Mean

<!-- b000354 | prose | pages [16] -->
Variables

<!-- b000355 | prose | pages [16] -->
0.240

<!-- b000356 | prose | pages [16] -->
• Economic • Social

<!-- b000357 | prose | pages [16] -->
0.230

<!-- b000358 | prose | pages [16] -->
• Political • Cohesion

<!-- b000359 | prose | pages [16] -->
0.220

<!-- b000360 | prose | pages [16] -->
0.210

<!-- b000361 | prose | pages [16] -->
0.200

<!-- b000362 | prose | pages [16] -->
0.190

<!-- b000363 | prose | pages [16] -->
0.180

<!-- b000364 | prose | pages [16] -->
0.170

<!-- b000365 | prose | pages [16] -->
0.160

<!-- b000366 | prose | pages [16] -->
0.150

<!-- b000367 | prose | pages [16] -->
0.140

<!-- b000368 | prose | pages [16] -->
0.130 -+----,------.------.---r----,------.----,---呸 ----------, 0.10 0.20 0.30 0.40 0.50 0.60 0.70 0.80 0.90 1.00

<!-- b000369 | prose | pages [16] -->
Variable Means

<!-- b000370 | caption | pages [16] -->
Figure 7: Posterior mean analysis for CCIC.

<!-- b000371 | furniture | pages [17] -->
Team # 88902

<!-- b000372 | furniture | pages [17] -->
Page 14 of 24

<!-- b000373 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000374 | prose | pages [17] -->
We further postulate that when global cli- mate change deteriorates to a certain extent, its influence will gradually emerge. Until then, the impact is invisible to people. Hence, we must be aware of its presence and get ready to properly handle it. Another interesting point(the red outlier line) lies in Figure 7, where the red line(economic) becomes an outlier. Its slope is slightly higher than the others, which can be explained by the direct connection between CCIC and economic.

<!-- b000375 | prose | pages [17] -->
Cohesion Mean

<!-- b000376 | prose | pages [17] -->
0.80

<!-- b000377 | prose | pages [17] -->
• Social

<!-- b000378 | prose | pages [17] -->
0.75

<!-- b000379 | prose | pages [17] -->
• Political • Economic

<!-- b000380 | prose | pages [17] -->
0.70

<!-- b000381 | prose | pages [17] -->
• CCIC

<!-- b000382 | prose | pages [17] -->
0.65

<!-- b000383 | prose | pages [17] -->
0.60

<!-- b000384 | prose | pages [17] -->
0.55

<!-- b000385 | prose | pages [17] -->
0.50

<!-- b000386 | prose | pages [17] -->
0.45

<!-- b000387 | prose | pages [17] -->
0.40

<!-- b000388 | prose | pages [17] -->
0.35

<!-- b000389 | prose | pages [17] -->
0.30

<!-- b000390 | prose | pages [17] -->
0.25

<!-- b000391 | prose | pages [17] -->
0.20

<!-- b000392 | prose | pages [17] -->
0.15

<!-- b000393 | prose | pages [17] -->
0.104---呸----呸呸-呸--呸--呸----r--- ------- --, 0.00 0.10 0.20 0.30 0.40 0.50 0.60 0.70 0.80 0.90 1.00 Variable Means

<!-- b000394 | prose | pages [17] -->
Political Mean

<!-- b000395 | prose | pages [17] -->
0.90 • Economic

<!-- b000396 | prose | pages [17] -->
• Cohesion • CCIC

<!-- b000397 | prose | pages [17] -->
0.80

<!-- b000398 | prose | pages [17] -->
• Social

<!-- b000399 | prose | pages [17] -->
0.70

<!-- b000400 | prose | pages [17] -->
0.60

<!-- b000401 | prose | pages [17] -->
0.50

<!-- b000402 | prose | pages [17] -->
0.40

<!-- b000403 | prose | pages [17] -->
0.30

<!-- b000404 | prose | pages [17] -->
0.20

<!-- b000405 | prose | pages [17] -->
0.104---呸----呸呸-呸--呸--呸----r--- ---------, 0.00 0.10 0.50 1.00 0.20 0.30 0.40 0.60 0.70 0.80 0.90 Variable Means

<!-- b000406 | prose | pages [17] -->
Economic Mean

<!-- b000407 | prose | pages [17] -->
0.80

<!-- b000408 | prose | pages [17] -->
• CCIC

<!-- b000409 | prose | pages [17] -->
0.75

<!-- b000410 | prose | pages [17] -->
• Political • Cohesion • Social

<!-- b000411 | prose | pages [17] -->
0.70

<!-- b000412 | prose | pages [17] -->
0.65

<!-- b000413 | prose | pages [17] -->
0.60

<!-- b000414 | prose | pages [17] -->
0.55

<!-- b000415 | prose | pages [17] -->
0.50

<!-- b000416 | prose | pages [17] -->
0.45

<!-- b000417 | prose | pages [17] -->
0.40

<!-- b000418 | prose | pages [17] -->
0.35

<!-- b000419 | prose | pages [17] -->
0.30

<!-- b000420 | prose | pages [17] -->
0.25

<!-- b000421 | prose | pages [17] -->
-4------..---- -᪽ --᪽ --᪽ ----.----,----..------, 0.20 0.00 0.10 0.20 0.30 0.40 0.50 0.60 0.70 0.80 0.90 1.00 Variable Means

<!-- b000422 | prose | pages [17] -->
Social Mean

<!-- b000423 | prose | pages [17] -->
0.70 • Cohesion

<!-- b000424 | prose | pages [17] -->
• CCIC

<!-- b000425 | prose | pages [17] -->
0.65

<!-- b000426 | prose | pages [17] -->
• Political • Economic

<!-- b000427 | prose | pages [17] -->
0.60

<!-- b000428 | prose | pages [17] -->
0.55

<!-- b000429 | prose | pages [17] -->
0.50

<!-- b000430 | prose | pages [17] -->
0.45

<!-- b000431 | prose | pages [17] -->
0.40

<!-- b000432 | prose | pages [17] -->
0.35

<!-- b000433 | prose | pages [17] -->
0.30

<!-- b000434 | prose | pages [17] -->
0.25

<!-- b000435 | prose | pages [17] -->
0.20

<!-- b000436 | prose | pages [17] -->
0.15-+---呸--呸-呸呸-呸--呸--呸--呸--呸--呸-呸

<!-- b000437 | prose | pages [17] -->
0.00 0.10 0.20 0.30 0.40 0.50 0.60 0.70 0.80 0.90 1.00 Variable Means

<!-- b000438 | caption | pages [17] -->
Figure 8: Posterior mean analysis for the 4 indicators.

<!-- b000439 | prose | pages [17] -->
6.3 Other Analysis

<!-- b000440 | prose | pages [17] -->
We also conducted other analysis to our model, including both statistical methods(correlation, etc.) and information-theoretical methods(mutual information, Entropy, etc.), shown in Table 1, Ta- ble 2, from which we can see that the bond between CCIC and economic is weaker than the others. This is reasonable to some extent. But it may also indicate that not enough evidences are provided to convince ourselves that climate change can actually have a great impact on a country’s economic system. With more data, the actual bond may gradually emerge, and presumably become strong than the current one. Moreover, other bonds other than the current set are also possible to emerge in the future.

<!-- b000441 | prose | pages [17] -->
7

<!-- b000442 | heading | pages [17] -->
Task 1: Models and Standard Lines

<!-- b000443 | heading | pages [17] -->
Determine the standard line by K-Means Clustering Algorithm

<!-- b000444 | prose | pages [17] -->
7.1

<!-- b000445 | prose | pages [17] -->
After all the four indicators of WFSI for a country have been calculated, we still don’t have a qualitative concept about the country’s current state. Fragile? Vulnerable? Or stable? Therefore, K- Means clustering algorithm[36] is adopted to set a standard.

<!-- b000446 | furniture | pages [18] -->
Team # 88902

<!-- b000447 | furniture | pages [18] -->
Page 15 of 24

<!-- b000448 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000449 | prose | pages [18] -->
KL

<!-- b000450 | prose | pages [18] -->
Mutual

<!-- b000451 | prose | pages [18] -->
Consistency

<!-- b000452 | prose | pages [18] -->
information

<!-- b000453 | prose | pages [18] -->
Estimate

<!-- b000454 | prose | pages [18] -->
Divergence

<!-- b000455 | prose | pages [18] -->
Sum 3.3175

<!-- b000456 | prose | pages [18] -->
Mean

<!-- b000457 | prose | pages [18] -->
3.3175 3.3175

<!-- b000458 | prose | pages [18] -->
0.8294

<!-- b000459 | prose | pages [18] -->
Standard Deviation

<!-- b000460 | prose | pages [18] -->
0.8294 0.8294

<!-- b000461 | prose | pages [18] -->
0.3377 0.3377 0.3377

<!-- b000462 | caption | pages [18] -->
Table 1: Overall metrics.

<!-- b000463 | prose | pages [18] -->
KL

<!-- b000464 | prose | pages [18] -->
Relative

<!-- b000465 | prose | pages [18] -->
Overall

<!-- b000466 | prose | pages [18] -->
Mutual

<!-- b000467 | prose | pages [18] -->
Parent Child

<!-- b000468 | prose | pages [18] -->
Symmetric

<!-- b000469 | prose | pages [18] -->
Symmetric

<!-- b000470 | prose | pages [18] -->
Normalized

<!-- b000471 | prose | pages [18] -->
Relative

<!-- b000472 | prose | pages [18] -->
G-test

<!-- b000473 | prose | pages [18] -->
Pearson's

<!-- b000474 | prose | pages [18] -->
GKL-test

<!-- b000475 | prose | pages [18] -->
Mutual

<!-- b000476 | prose | pages [18] -->
Mutual

<!-- b000477 | prose | pages [18] -->
information

<!-- b000478 | prose | pages [18] -->
Divergence

<!-- b000479 | prose | pages [18] -->
Weight

<!-- b000480 | prose | pages [18] -->
Contribution

<!-- b000481 | prose | pages [18] -->
Political Cohesion 1.1556 1.0000 34.8327%

<!-- b000482 | prose | pages [18] -->
Economic Political 0.9829 0.8506 29.6288%

<!-- b000483 | prose | pages [18] -->
Cohesion Social 0.9143 0.7912 27.5612%

<!-- b000484 | prose | pages [18] -->
CCIC Economic 0.2646 0.2290 7.9774%

<!-- b000485 | prose | pages [18] -->
(Data)

<!-- b000486 | prose | pages [18] -->
Correlation

<!-- b000487 | prose | pages [18] -->
Information

<!-- b000488 | prose | pages [18] -->
Information

<!-- b000489 | prose | pages [18] -->
1.1556 34.7862% 40.9864% 983.6067 983.6067 0.9053

<!-- b000490 | prose | pages [18] -->
0.9829 29.5893% 34.3695% 836.6590 836.6590 0.8754

<!-- b000491 | prose | pages [18] -->
0.9143 27.5244% 31.2598% 778.2728 778.2728 0.8142

<!-- b000492 | prose | pages [18] -->
0.2646 7.9667% 9.0010% 225.2653 225.2653 0.2602

<!-- b000493 | caption | pages [18] -->
Table 2: Metrics for node-node relationship.

<!-- b000494 | prose | pages [18] -->
One drawback[37] to the algorithm occurs when it is applied to datasets with m data points in

<!-- b000495 | prose | pages [18] -->
≥ ≥

<!-- b000496 | prose | pages [18] -->
n 10 dimensional real space Rn and the number of desired clusters is k 20. In this situation, the K- Means algorithm often converges with one or more clusters which are either empty or summarize very few data points (i.e. one data point). However, our model has only four dimensions and K, which denotes the number of clusters, is 3 in our model. So, KA is suitable for ourmodel.

<!-- b000497 | prose | pages [18] -->
Given a datasets D of m points in Rn and cluster centers C1,t, C2,t, . . . , Ck,t at iteration t, compute C1,t+1, C2,t+1, . . . , Ck,t+1 at iteration t + 1 in the following 2 steps:

<!-- b000498 | prose | pages [18] -->
∈

<!-- b000499 | prose | pages [18] -->
D, assign xi to cluster h(i) such that center

<!-- b000500 | heading | pages [18] -->
1. Cluster Assignment. For each data record xi

<!-- b000501 | prose | pages [18] -->
Ch(i),t is nearest to xi in the 2-norm.

<!-- b000502 | heading | pages [18] -->
2. Cluster Update. Compute Ch,t+1 as the mean of all points assigned to clusterh.

<!-- b000503 | prose | pages [18] -->
Stop when Ch,t+1 = Ch,t, h = 1, . . . , k, else increment t by 1 and go to step 1.

<!-- b000504 | prose | pages [18] -->
After training a K-Means model using the data we have, we find it performs well as is shown in

<!-- b000505 | caption | pages [18] -->
Figure 9.

<!-- b000506 | prose | pages [18] -->
Because we have four dimensions, which can’t be shown in only one figure. Hence, we draw each three of them for one time in a figure, after which we get these fourfigures.

<!-- b000507 | prose | pages [18] -->
Identifying the Impact of Climate Change 7.2

<!-- b000508 | prose | pages [18] -->
Please see 6.1 and 6.2.

<!-- b000509 | prose | pages [18] -->
8 Task 2: Case Study - Sudan

<!-- b000510 | prose | pages [18] -->
Among all of the top 10 most fragile states, we can only get the data of Iraque and Sudan. Con- sidering the extensive chaos and wars in Iraque, we finally chose Sudan.

<!-- b000511 | prose | pages [18] -->
Conducting causality inference in probabilistic models are rather easy. According to our data, we provide our model with a new piece of evidence:

<!-- b000512 | prose | pages [18] -->
P (0.067 ≤CCIC ≤0.091) = 1

<!-- b000513 | prose | pages [18] -->
We then calculate the probability of other variables accordingly, the original and post-evidence results are shown in the same graph(Figure 10) for the purpose of comparison. It is obvious that CCIC can result in a high probability of low score in all the other four variables without other ex- ternal intervention, especially economic. Hence, we can conclude that climate change can make the

<!-- b000514 | furniture | pages [19] -->
Team # 88902

<!-- b000515 | furniture | pages [19] -->
Page 16 of 24

<!-- b000516 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000517 | caption | pages [19] -->
Figure 9: K-Means Model Results

<!-- b000518 | prose | pages [19] -->
bad situation even worse, through directly weaken one country’s economic system and indirectly influence all the other variables.

<!-- b000519 | prose | pages [19] -->
Therefore, if we conversely set CCIC to be greater than 0.38, it would result in a higher probability of high score in all the other variables, therefore leading to a less fragile state. For more concrete strategies in order to ease the fragility of Sudan, see section 10.

<!-- b000520 | caption | pages [19] -->
Figure 10: Impact of CCIC.

<!-- b000521 | prose | pages [19] -->
9 Task 3: Case Study - Greece

<!-- b000522 | prose | pages [19] -->
9.1 WFSI and CCIC for Greece

<!-- b000523 | prose | pages [19] -->
Greece is chosen to be evaluated by our model. Firstly, we get the WFSI and CCIC scores for Greece from 2008 to 2012 as shown below in Figure 11. Note that each score of Greece is below 0.35

<!-- b000524 | furniture | pages [20] -->
Team # 88902

<!-- b000525 | furniture | pages [20] -->
Page 17 of 24

<!-- b000526 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000527 | prose | pages [20] -->
and the changes between years are small, so we set the radar chart boundary to 0.35 to better show the trend of the changes.

<!-- b000528 | caption | pages [20] -->
Figure 11: WFSI and CCIC for Greece from 2008 to 2012

<!-- b000529 | prose | pages [20] -->
The details for each year is shown in Table 3. In these five years, Greece stays in the vulnerable state.

<!-- b000530 | prose | pages [20] -->
Year CI EI PI SI CCIC Category

<!-- b000531 | prose | pages [20] -->
0.32482785 2008 0.34311201 0.30068317 0.33128552 0.110295 vulnerable 0.3052545 2009 0.33108916 0.28565486 0.28280523 0.119507 vulnerable 0.27146437 2010 0.3177221 0.31542998 0.30181049 0.081737 vulnerable 0.27657189 2011 0.32430351 0.3477323 0.26598385 0.086050 vulnerable 0.29347285 2012 0.30322494 0.29910825 0.32876026 0.095530 vulnerable

<!-- b000532 | caption | pages [20] -->
Table 3: WFSI and CCIC for Greece from 2008 to 2012.

<!-- b000533 | prose | pages [20] -->
The data above suggests that, although the current status of Greece is acceptable, the FSI scores of it is gradually reducing. Especially, the cohesion index and policy index decline obviously. Although in 2008 the Greek economy was regarded as the 27th largest economy[38] of the world by nominal Gross Domestic Product (GDP) with 32,100 USD GDP per capita[39], as a corollary of the international fi- nancial crisis and the local unrelenting spending, Greek citizens started facing serious socioeconomic turmoil. In 2009, the economic crisis impinged on a greater proportion of the population, whereas in 2010 a Memorandum of Economic and Financial Policies was signed in order to avert Greece’s default. The same year, national estimates showed that GDP dropped to -3.5%, while unemployment rates reached as high as 14.2%, with 180,000 people losing their jobs[40]. In 2011, the profile of the Greek economy appears the gloomiest of the decade: GDP further declined to -6.1%, whereas unem- ployment rates increased from 6.6% in May 2008 to 16.6% in May 2011. Concomitantly, throughout the same period, the debt has grown from 105.4% in 2007 to 160.9% of GDP in 2011 (239.4 billion euros to 328.6 billion euros)[41].

<!-- b000534 | prose | pages [20] -->
9.2 Prediction for Greece

<!-- b000535 | prose | pages [20] -->
Using the model 2THN, we predict the future status of Greece, shown in Figure 12. The detail predicting data from 2013 to 2017 is shown in Table 4.

<!-- b000536 | prose | pages [20] -->
Year CI EI PI SI Category

<!-- b000537 | prose | pages [20] -->
0.30632332 2013 0.32372539 0.27658597 0.34520463 vulnerable 0.25672303 2014 0.27213682 0.23103887 0.38824761 vulnerable 0.25412672 2015 0.27160032 0.26766136 2016 0.24880141 0.24614655 0.46719683 vulnerable 0.2126675 0.444723410 fragile 0.18593567 2017 0.27053746 0.26077977 0.24906261 fragile

<!-- b000538 | caption | pages [20] -->
Table 4: WFSI C for Greece from 2013 to 2017.

<!-- b000539 | furniture | pages [21] -->
Team # 88902

<!-- b000540 | furniture | pages [21] -->
Page 18 of 24

<!-- b000541 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000542 | caption | pages [21] -->
Figure 12: WFSI for Greece from 2008 to 2017

<!-- b000543 | prose | pages [21] -->
Frankly speaking, the wired peak in our prediction results are not very easy to interpret. Presum- ably, the reasons may lie inside the complex black box implementation of our model, which forms a weak point of our model.

<!-- b000544 | prose | pages [21] -->
Despite the absence of the full understand of the result, in order to get the tipping point, we retrieve the center of the three cluster calculated by KA(see section 7.1 for more information), which respectively are:

<!-- b000545 | prose | pages [21] -->
[0.7146366, 1.48168573, 2.62917114]

<!-- b000546 | prose | pages [21] -->
Then we calculate the mean of the two smaller values as the tipping point. We can then draw the conclusion from Table 4 that Greece may turn to fragile state in 2016. Among the four index, the policy index and social index fluctuate wildly while the social index even plays a decisive role of Greece’s turning back to fragile state.

<!-- b000547 | prose | pages [21] -->
10 Task 4: Possible Strategies

<!-- b000548 | prose | pages [21] -->
Climate change is a global issue (fixed CCI), which is hard to be adjusted by only one country’s efforts. However, we can find a breakout according to our model - CCV can differ from country to country, which makes it possible to mitigate the risk of climate change by launching particular policies on a state level. Based on the indicators that form CCV, we can reduce CCV from six equally weighted dimensions according to NG-GAIN: food, water, health, ecosystem services, human habitat and infrastructure.

<!-- b000549 | prose | pages [21] -->
We again take Sudan as an example, the proposed state driven interventions in Table 5 may help to increase its resilience to climate change, therefore help to prevent it from becoming a even more fragile state under the severe climate change.

<!-- b000550 | prose | pages [21] -->
Note that it is impossible for us to diminish CCV down to zero. So in order to set a realistic goal, we roughly recommend some percentages based on the current speed of development[43]. And the estimated costs of the interventions are given by consulting the Expenditure Review of Sudan[42], combined with the goals of interventions as percentages.

<!-- b000551 | prose | pages [21] -->
11 Task 5: Scalability Analysis

<!-- b000552 | prose | pages [21] -->
Our models are originally based on national level, which are relatively independent entities. We find that continents are more similar to countries than cities from the perspective of independence level. So we postulate that our model can be scaled to continents under some adjustments butprob- ably not cities.

<!-- b000553 | prose | pages [21] -->
To simplify the problem, we simply average the WFCIs for all countries on a single (modi- fied)continent directly to get the new WFCIs(Weighted Fragile Continent Index) and then visualize them, as shown in Figure 13(The gray area means that we have no data of it).

<!-- b000554 | furniture | pages [22] -->
Team # 88902

<!-- b000555 | furniture | pages [22] -->
Page 19 of 24

<!-- b000556 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000557 | prose | pages [22] -->
Sub Indicators Value Interventions Estimated Cost

<!-- b000558 | prose | pages [22] -->
Provide farmers with support on Fertilizer, Irrigation, Pesticide,

<!-- b000559 | prose | pages [22] -->
Food 0.739

<!-- b000560 | prose | pages [22] -->
$8 million/year Tractor use to increase yield by 10 every three year.

<!-- b000561 | prose | pages [22] -->
Introduce technology to build dam or amplify dam capacity. Water 0.691

<!-- b000562 | prose | pages [22] -->
$3 million/year Increase clean water storage by 6 every three year.

<!-- b000563 | prose | pages [22] -->
Spend more budget on medical staffs to reduce the deaths from Health 0.709

<!-- b000564 | prose | pages [22] -->
$2 million/year climate change induced diseases by 8 every three year.

<!-- b000565 | prose | pages [22] -->
Enact more strict policies to protect biomes and reduce the Ecosystem 0.661

<!-- b000566 | prose | pages [22] -->
$80,000/year vulnerability score in terms of ecosystem by 1 every year.

<!-- b000567 | prose | pages [22] -->
Improve the quality of trade and transport especially paved Habitat 0.547

<!-- b000568 | prose | pages [22] -->
$500,000/year roads to reduce the habitat index by 2 every three year.

<!-- b000569 | prose | pages [22] -->
Put more effort into disaster preparedness to reduce the Infrastructure 0.337

<!-- b000570 | prose | pages [22] -->
$600,000/year damage of disaster by 1 every three year.

<!-- b000571 | prose | pages [22] -->
All interventions above try to reduce CCV to improve the CCV 0.620

<!-- b000572 | prose | pages [22] -->
$14.18million/year climate change resilience of SDN (CCIC = (1-CCV) *CCI)

<!-- b000573 | caption | pages [22] -->
Table 5: Proposed solutions to Sudan’s case.

<!-- b000574 | prose | pages [22] -->
(a) Climate Change Indexby Country.

<!-- b000575 | prose | pages [22] -->
(b) Weighted Fragile ContinentIndex.

<!-- b000576 | caption | pages [22] -->
Figure 13: Results with continents.

<!-- b000577 | prose | pages [22] -->
Note that we didn’t use the geographical "continent" as defined in Wikipedia. Instead, we made some adjustments to the "structure of the world", notably we put the area in the south of the U.S. as a whole(Latin America). This is because that the economic and social environment of these countries differ too much from the U.S. and Canada despite the fact that they are in the same continent. For a counterexample, please find Australia in both graphs and make a comparison. The modeling result is not very ideal since Australia should have had a very healthy score. The problem lies in theweak cluster strategy, which could be solved by splitting countries like Papua New Guinea to the Southeast Asia. After further research, we eventually draw the following conclusions:

<!-- b000578 | prose | pages [22] -->
1. Our model can be applied to continents if proper adjustments(such as re-clustering) over the definition of the term "continent" are made. Concretely, the adjustments should take the eco- nomic, social and political difference among the clustered countries into consideration.

<!-- b000579 | prose | pages [22] -->
2. The probability of our model’s application on cities is remote unless we substitute the 5 major indicators with some re-designed indicators and re-weight them accordingly. The reasons lie in the shrink of the "granularity" of the problem, making it harder to predict the overallsystem’s performance. As a result, more sophisticated models are required instead of a simple 5-element network.

<!-- b000580 | furniture | pages [23] -->
Team # 88902

<!-- b000581 | furniture | pages [23] -->
Page 20 of 24

<!-- b000582 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000583 | prose | pages [23] -->
12

<!-- b000584 | heading | pages [23] -->
Strengths and weaknesses

<!-- b000585 | prose | pages [23] -->
Generally speaking, our model is designed for average countries. One country can use this model to guide its direction of development by conducting inference on the trainednetwork.

<!-- b000586 | prose | pages [23] -->
12.1

<!-- b000587 | heading | pages [23] -->
Strengths

<!-- b000588 | heading | pages [23] -->
1. Robustness and flexibility.

<!-- b000589 | prose | pages [23] -->
The fundamental strength of our model comes from its enormous flexibility, where none of the parameters in our model is fixed, even the structure of the network. And since that all the parameters are learned from data, our model is very easy to be customized, therefore could be applied widely. Our model also incorporates the idea of big data. That is to say, with more and more data(evidence), our model can give more and more precise predictions. Furthermore, our model has the notion of time, which is omitted in most mathematicalmodels.

<!-- b000590 | heading | pages [23] -->
2. Combination of data and expert knowledge.

<!-- b000591 | prose | pages [23] -->
Besides effectively utilizing the data, our model also takes advantage of the expert knowledge when determining the weights(AHP) and constructing the network. This gives our model a second dimension’s insight.

<!-- b000592 | heading | pages [23] -->
3. Easy to understand.

<!-- b000593 | prose | pages [23] -->
Adopting a hierarchical structure, our model can be easily understood with a single graph and several lines of explanation, see Figure 1. Hence, our model is more likely to be understood by the decision and policy makers with the presence of their knowledge gap in the complex interconnected system.

<!-- b000594 | prose | pages [23] -->
12.2

<!-- b000595 | heading | pages [23] -->
Weaknesses

<!-- b000596 | heading | pages [23] -->
1. Potential vulnerability due to the lack of data.

<!-- b000597 | prose | pages [23] -->
The fundamental weakness of our model also comes from data. Since our model is so depen- dent on data, it is likely to be useless when considering countries in abnormal situations, such as large-scale wars and natural disasters.

<!-- b000598 | heading | pages [23] -->
2. Potential invalid assumptions.

<!-- b000599 | prose | pages [23] -->
Another obstacle that may hold back our model’s performance is that the assumptions made to simplify the model may be invalid, therefore leading to a less useful model. For example, the fragility of one country may depend on other factors other than the 4 factors identified by us. Our model may also fail to give reasonable results when encountering some abnormal cases.

<!-- b000600 | heading | pages [23] -->
3. Potential abnormal phenomenons.

<!-- b000601 | prose | pages [23] -->
Due to the internal complexity of the inherent structure of 2THN, some outcomes of our model may be hard to interpret(see section 9.2), which is also the drawback of many other machine learning approaches such as neural networks. (Note that the internal complexity doesn’t neces- sarily conflict with its comprehensibility for that it can be treated as a blackbox.)

<!-- b000602 | furniture | pages [24] -->
Team # 88902

<!-- b000603 | furniture | pages [24] -->
Page 21 of 24

<!-- b000604 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000605 | heading | pages [24] -->
References

<!-- b000606 | references | pages [24] -->
[1] Wijeyaratne, S. (2009). Fragile environment, fragile state: Conflict, crisis and climatechange.

<!-- b000607 | references | pages [24] -->
[2] Crawford, A., DazÃl’, A., Hammill, A., Parry, J., & Zamudio, N. (2015). Promoting climate-

<!-- b000608 | references | pages [24] -->
resilient peacebuilding in fragile states. Geneva: International Institute for Sustainable Develop-

<!-- b000609 | references | pages [24] -->
ment (IISD).

<!-- b000610 | references | pages [24] -->
[3] Climate Change and Fragile States Workshop report. (n.d)

<!-- b000611 | references | pages [24] -->
from

<!-- b000612 | references | pages [24] -->
Retrieved

<!-- b000613 | references | pages [24] -->
Feb

<!-- b000614 | references | pages [24] -->
10,

<!-- b000615 | references | pages [24] -->
2018,

<!-- b000616 | references | pages [24] -->
https://reliefweb.int/sites/reliefweb.int/files/resources/Climate_

<!-- b000617 | references | pages [24] -->
Change_and_Fragile_States_Workshop_Report.pdf

<!-- b000618 | references | pages [24] -->
[4] Mason, S., Kruczkiewicz, A., Ceccato, P., & Crawford, A. (2015). Accessing and using climate

<!-- b000619 | references | pages [24] -->
data and information in fragile, data-poor states. International Institute for Sustainable Devel-

<!-- b000620 | references | pages [24] -->
opment: Winnipeg, MB, Canada.

<!-- b000621 | references | pages [24] -->
[5] Edenhofer, O., & Seyboth, K. (2013). Intergovernmental panel on climate change(IPCC).

<!-- b000622 | references | pages [24] -->
[6] Chen, C., Noble, I., Hellmann, J., Coffee, J., Murillo, M., & Chawla, N. (2015). University of

<!-- b000623 | references | pages [24] -->
Notre Dame Global Adaptation Index Country Index Technical Report. ND-GAIN: South Bend,

<!-- b000624 | references | pages [24] -->
IN, USA.

<!-- b000625 | references | pages [24] -->
[7] Burck, J., Bals, C., & Ackermann, S. (2009). The climate change performance index:background

<!-- b000626 | references | pages [24] -->
and methodology. Germanwatch.

<!-- b000627 | references | pages [24] -->
[8] Lee, E. A. (2017). Plato and the nerd: the creative partnership of humans andtechnology.

<!-- b000628 | references | pages [24] -->
[9] Box, George E. P.; Norman R. Draper (1987). Empirical Model-Building and Response Surfaces,

<!-- b000629 | references | pages [24] -->
p. 424, Wiley. ISBN 0471810339.

<!-- b000630 | references | pages [24] -->
[10] Mihajlovic, V.,& Petkovic, M. (2001). Dynamic bayesian networks: a state of the art. Epl.

<!-- b000631 | references | pages [24] -->
[11] Simon. (2011). Probabilistic graphical models: principles and techniques by daphne koller and

<!-- b000632 | references | pages [24] -->
nir friedman, mit press, 1231 pp. $95.00, isbn 0-262-01319-3. Knowledge Engineering Review,

<!-- b000633 | references | pages [24] -->
26(2), 237-238.

<!-- b000634 | references | pages [24] -->
[12] Koller, D., & Friedman, N. (2009). Probabilistic graphical models. Probabilistic Graphical Mod-

<!-- b000635 | references | pages [24] -->
els. Springer International Publishing.

<!-- b000636 | references | pages [24] -->
[13] Markov property. (n.d.) In Wikipedia. Retrieved Feb 10, 2018, from https://en.wikipedia.

<!-- b000637 | references | pages [24] -->
org/wiki/Markov_property

<!-- b000638 | references | pages [24] -->
[14] Jaimovich, A. (2010). Understanding Protein-protein Interaction Networks (Doctoral disserta-

<!-- b000639 | references | pages [24] -->
tion, Hebrew University).

<!-- b000640 | references | pages [24] -->
[15] Dan, S., & Vivekananda, J. (2009). Climate change, conflict and fragility.

<!-- b000641 | references | pages [24] -->
[16] Cooper, G. F., & Herskovits, E. (1992). A bayesian method for the induction of probabilistic

<!-- b000642 | references | pages [24] -->
networks from data. Machine Learning, 9(4), 309-347.

<!-- b000643 | references | pages [24] -->
[17] Woolcock, M., & Ritzen, J. (2010). Social cohesion, public policy and economic, growth: impli-

<!-- b000644 | references | pages [24] -->
cations for countries. The Contribution of Human and Social Capital to Sustained Economic

<!-- b000645 | references | pages [24] -->
Growth and Well-being: International Symposium Report, Human Resources Development

<!-- b000646 | references | pages [24] -->
Canada and OECD.

<!-- b000647 | references | pages [24] -->
[18] Carvajal, L. (2007). Impacts of climate change on human development. (49).

<!-- b000648 | references | pages [24] -->
[19] Gelsdorf, & Kirsten. (2010). Global challenges and their impact on international humanitarian

<!-- b000649 | references | pages [24] -->
action.

<!-- b000650 | furniture | pages [25] -->
Team # 88902

<!-- b000651 | furniture | pages [25] -->
Page 22 of 24

<!-- b000652 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000653 | references | pages [25] -->
[20] Dziembala, Malgorzata. (2016). Some considerations on the relationship between economic and

<!-- b000654 | references | pages [25] -->
social cohesion and implementation of the cohesion policy. Perspectives on Federalism, 8(1),

<!-- b000655 | references | pages [25] -->
53-80.

<!-- b000656 | references | pages [25] -->
[21] Margaritis, D. (2003). Learning bayesian network model structure from data /. Learning

<!-- b000657 | references | pages [25] -->
Bayesian Network Model Structure from Data.

<!-- b000658 | references | pages [25] -->
[22] Heckerman, D. (1995). A tutorial on learning with bayesian networks. Learning in Graphical

<!-- b000659 | references | pages [25] -->
Models, 25(4), 33-82.

<!-- b000660 | references | pages [25] -->
[23] Ankan, A., & Panda, A. (2015). Mastering Probabilistic Graphical Models using Python. Packt

<!-- b000661 | references | pages [25] -->
Publishing.

<!-- b000662 | references | pages [25] -->
[24] Edgeworth, Francis Y. (Sep 1908). "On the probable errors of frequency-constants". Journal of

<!-- b000663 | references | pages [25] -->
the Royal Statistical Society. 71 (3): 499-512. doi:10.2307/2339293. JSTOR 2339293.

<!-- b000664 | references | pages [25] -->
[25] Inference

<!-- b000665 | references | pages [25] -->
in

<!-- b000666 | references | pages [25] -->
Bayesian

<!-- b000667 | references | pages [25] -->
Networks.

<!-- b000668 | references | pages [25] -->
(n.d.)

<!-- b000669 | references | pages [25] -->
Retrieved

<!-- b000670 | references | pages [25] -->
Feb

<!-- b000671 | references | pages [25] -->
10,

<!-- b000672 | references | pages [25] -->
2018,

<!-- b000673 | references | pages [25] -->
from

<!-- b000674 | references | pages [25] -->
https:

<!-- b000675 | references | pages [25] -->
//ocw.mit.edu/courses/electrical-engineering-and-computer-science/ 6-

<!-- b000676 | references | pages [25] -->
825-techniques-in-artificial-intelligence-sma-5504-fall-2002/

<!-- b000677 | references | pages [25] -->
lecture-notes/Lecture16FinalPart1.pdf

<!-- b000678 | references | pages [25] -->
[26] Climate change, fragility and conflict. (n.d.) Retrieved Feb 10, 201, from http://www.

<!-- b000679 | references | pages [25] -->
international-alert.org/projects/13624.

<!-- b000680 | references | pages [25] -->
[27] Butz, C. J., Oliveira, J. D. S., & Madsen, A. L. (2014). Bayesian Network Inference Using Marginal

<!-- b000681 | references | pages [25] -->
Trees. Probabilistic Graphical Models. Springer International Publishing.

<!-- b000682 | references | pages [25] -->
[28] Meng Q S, 1989. Information theory [M]. Xi’An: Xi’An Jiaotong University Press. 19-36.

<!-- b000683 | references | pages [25] -->
[29] Zou, Z. H., Yi, Y., & Sun, J. N. (2006). Entropy method for determination of weight of evaluating

<!-- b000684 | references | pages [25] -->
indicators in fuzzy synthetic evaluation for water quality assessment. Journal of Environmental

<!-- b000685 | references | pages [25] -->
Sciences, 18(5), 1020-1023.

<!-- b000686 | references | pages [25] -->
[30] Global Data | Fragile States Index. Retrieved Feb 9, 2018, form http://fundforpeace.org/

<!-- b000687 | references | pages [25] -->
fsi/data/

<!-- b000688 | references | pages [25] -->
[31] World Bank, 2018. Retrieved Feb 9, 2018, form http://climatedataapi.worldbank.org/

<!-- b000689 | references | pages [25] -->
climateweb/rest/v1/country/cru/tas/year/ISO3.csv

<!-- b000690 | references | pages [25] -->
[32] World Bank, 2018. Retrieved Feb 9, 2018, form http://climatedataapi.worldbank.org/

<!-- b000691 | references | pages [25] -->
climateweb/rest/v1/country/cru/pr/year/ISO3.csv

<!-- b000692 | references | pages [25] -->
[33] World

<!-- b000693 | references | pages [25] -->
Development

<!-- b000694 | references | pages [25] -->
Indicators,

<!-- b000695 | references | pages [25] -->
2018.

<!-- b000696 | references | pages [25] -->
emissions

<!-- b000697 | references | pages [25] -->
(metric

<!-- b000698 | references | pages [25] -->
tons

<!-- b000699 | references | pages [25] -->
per

<!-- b000700 | references | pages [25] -->
capita)

<!-- b000701 | references | pages [25] -->
CO2

<!-- b000702 | references | pages [25] -->
(EN.ATM.CO2E.PC). Retrieved Feb 9, 2018, form http://databank.worldbank.org/

<!-- b000703 | references | pages [25] -->
data/reports.aspx?source=world-development-indicators&preview=on

<!-- b000704 | references | pages [25] -->
[34] World Development Indicators, 2018. Arable land (% of land area)(AG.LND.ARBL.ZS). Re-

<!-- b000705 | references | pages [25] -->
trieved Feb 9, 2018, form http://databank.worldbank.org/data/reports.aspx?

<!-- b000706 | references | pages [25] -->
source=world-development-indicators&preview=on

<!-- b000707 | references | pages [25] -->
[35] Enviroment Performance Index, 2018. Retrieved Feb 9, 2018, form http://archive.epi.

<!-- b000708 | references | pages [25] -->
yale.edu/downloads

<!-- b000709 | references | pages [25] -->
[36] Duda, R. O., Hart, P.E., & Stork, D. G. (1995). Pattern classification and scene analysis 2nd ed.

<!-- b000710 | references | pages [25] -->
ed: Wiley Interscience.

<!-- b000711 | references | pages [25] -->
[37] Bradley, P. S., Bennett, K. P., & Demiriz, A. (2000). Constrained k-means clustering. Microsoft

<!-- b000712 | references | pages [25] -->
Research, Redmond, 1-8.

<!-- b000713 | furniture | pages [26] -->
Team # 88902

<!-- b000714 | furniture | pages [26] -->
Page 23 of 24

<!-- b000715 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000716 | references | pages [26] -->
[38] Economou, M., Madianos, M., Peppou, L. E., Patelakis, A., & Stefanis, C. N. (2013). Major de-

<!-- b000717 | references | pages [26] -->
pression in the era of economic crisis: a replication of a cross-sectional study across Greece.

<!-- b000718 | references | pages [26] -->
Journal of affective disorders, 145(3), 308-314.

<!-- b000719 | references | pages [26] -->
[39] Eurostat, 2010. Report of the revision of the Greek Government deficit and debt figures. http:

<!-- b000720 | references | pages [26] -->
//epp.eurostat.e.c.europa.eu/cache/ITY.

<!-- b000721 | references | pages [26] -->
[40] Bank of Greece, 2010. Annual Reports. B.G. Printing Office, Athens.

<!-- b000722 | references | pages [26] -->
[41] Eurostat, 2011. Euro Area and EU27 Government Deficit at 6.0% and 6.4% of GDP, reespec-

<!-- b000723 | references | pages [26] -->
tively. Eurostat, Luxembourg.

<!-- b000724 | references | pages [26] -->
[42] SUDAN State-level Public Expenditure Review,

<!-- b000725 | references | pages [26] -->
(May 2014),

<!-- b000726 | references | pages [26] -->
Retrived Feb 11,

<!-- b000727 | references | pages [26] -->
from

<!-- b000728 | references | pages [26] -->
https://openknowledge.worldbank.org/bitstream/handle/10986/23505/

<!-- b000729 | references | pages [26] -->
Synthesis0repo0ary0for0policymakers.pdf?sequence=1&isAllowed=y

<!-- b000730 | references | pages [26] -->
[43] Sudan: The Land and the People, (n.d.), Retrived Feb 11, from http://www.sd.undp.org/

<!-- b000731 | references | pages [26] -->
content/sudan/en/home/countryinfo.html#Human

<!-- b000732 | furniture | pages [27] -->
Team # 88902

<!-- b000733 | furniture | pages [27] -->
Page 24 of 24

<!-- b000734 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000735 | heading | pages [27] -->
Appendices

<!-- b000736 | prose | pages [27] -->
import numpy as np import pandas as pd

<!-- b000737 | prose | pages [27] -->
class Data:

<!-- b000738 | prose | pages [27] -->
def init (self, data_filepath, from_year=2006, to_year=2012,

<!-- b000739 | prose | pages [27] -->
reassign_value=0.0001): self.data_filepath = data_filepath self.from_year = from_year self.to_year = to_year self.reassign_value = reassign_value

<!-- b000740 | prose | pages [27] -->
@staticmethod def _entropy_method(C):

<!-- b000741 | prose | pages [27] -->
P = C / np.sum(C, axis=0) e_i = - (1.0 / np.log(C.shape[0])) * np.sum(P * np.log(P), axis=0) g_i = 1 - e_i w_i = g_i / np.sum(g_i) R_i = np.min(C, axis=0) / C return np.sum(w_i * R_i, axis=1)

<!-- b000742 | prose | pages [27] -->
def _CCI_entropy_method(self, C): C[:,

<!-- b000743 | prose | pages [27] -->
0] = np.min(C[:, 0]) / C[:, 0] C[:, -1] = C[:, -1] / np.max(C[:, -1]) # reassign zero value to reassign_value for k in range(C.shape[0]):

<!-- b000744 | prose | pages [27] -->
for j in range(C.shape[1]):

<!-- b000745 | prose | pages [27] -->
if C[k, j] == 0:

<!-- b000746 | prose | pages [27] -->
C[k, j] = self.reassign_value P = C / np.sum(C, axis=0) e_i = - (1.0 / np.log(C.shape[0])) * np.sum(P * np.log(P), axis=0) g_i = 1 - e_i w_i = g_i / np.sum(g_i) return np.sum(w_i * C, axis=1)

<!-- b000747 | prose | pages [27] -->
def get_data(self, norm=False):

<!-- b000748 | prose | pages [27] -->
country_data = {} data = [] fsi_file_path = self.data_filepath + "fsi-{}.xlsx" df = pd.read_excel(fsi_file_path.format(2017)) countries = set(df["Country"]) for i in range(6, 13):

<!-- b000749 | prose | pages [27] -->
year = 2000 + i file path = fsi file path.format(year) df = pd.read_excel(file_path, index_col=0) before_keys = list(df.keys()) temp = np.array(df.iloc[:, 3:]) cohesion_index = self._entropy_method(temp[:, 0:3]) economic_index = self._entropy_method(temp[:, 3:6]) political_index = self._entropy_method(temp[:, 6:9]) social_index = self._entropy_method(temp[:, 9:12]) df["cohesion_index"] = cohesion_index df["economic_index"] = economic_index df["political_index"] = political_index df["social_index"] = social_index df = df.drop(before_keys, axis=1) data.append(df)

<!-- b000750 | furniture | pages [28] -->
Team # 88902

<!-- b000751 | furniture | pages [28] -->
Page 25 of 24

<!-- b000752 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000753 | prose | pages [28] -->
for country in countries:

<!-- b000754 | prose | pages [28] -->
country_data[country] = [] for year_data in data:

<!-- b000755 | prose | pages [28] -->
if country in year_data.index:

<!-- b000756 | prose | pages [28] -->
country_data[country].append(list(year_data.ix[country])) country data[country] = np.array(country data[country])

<!-- b000757 | prose | pages [28] -->
df = None for i in range(6, 13):

<!-- b000758 | prose | pages [28] -->
year = 2000 + i file_path = self.data_filepath + "CCI-" + str(year) + "-normalized.csv" if df is None:

<!-- b000759 | prose | pages [28] -->
df = pd.read_csv(file_path) else:

<!-- b000760 | prose | pages [28] -->
df = df.append(pd.read csv(file path), ignore index=True)

<!-- b000761 | prose | pages [28] -->
temp = np.array(df.iloc[:, 1:]) CCI = self._CCI_entropy_method(temp) CCI_country_name = set(df.iloc[:, 0]) df["CCI"] = CCI df = df[["Country", "CCI"]] df_vulnerability = pd.read_csv(self.data_filepath + "vulnerability.csv",

<!-- b000762 | prose | pages [28] -->
index_col=1) result = [] for country, C in country_data.items():

<!-- b000763 | prose | pages [28] -->
if country in CCI_country_name:

<!-- b000764 | prose | pages [28] -->
N = np.array(df vulnerability.loc[country])[-11:-4] M = np.array(df[df["Country"] == country].iloc[:, -1]) # compute CCIC M = M * (1 - N) for j in range(0, C.shape[0] - 1):

<!-- b000765 | prose | pages [28] -->
before_year = list(C[j, :]) now_year = list(C[j + 1, :]) before_year.append(M[j]) before_year.extend(now_year) before_year.append(M[j + 1]) result.append(before_year)

<!-- b000766 | prose | pages [28] -->
# data discretization result = np.array(result) * 20 X = np.array(result, dtype=np.int)

<!-- b000767 | prose | pages [28] -->
if norm:

<!-- b000768 | prose | pages [28] -->
return X / np.max(X, axis=0) else:

<!-- b000769 | prose | pages [28] -->
return X
