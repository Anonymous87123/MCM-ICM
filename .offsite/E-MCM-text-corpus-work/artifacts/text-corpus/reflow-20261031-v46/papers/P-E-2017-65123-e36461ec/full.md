# P-E-2017-65123-e36461ec

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
65123

<!-- b000003 | prose | pages [1] -->
For office use only For office use only T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000004 | front_matter | pages [1] -->
E

<!-- b000005 | prose | pages [1] -->
Smart Growth Theories in City Design

<!-- b000006 | heading | pages [1] -->
Summary

<!-- b000007 | prose | pages [1] -->
With the development of global urbanization, urban planning has been a hot spot of most concern. Since the traditional urban sprawl plan has been gradually unable to meet the development needs of the city, smart growth is proposed in 1990’s. In this paper, a series of methods are developed to help to implement smart growth theories into city de- sign.

<!-- b000008 | prose | pages [1] -->
In task 1, based on the gathered abundant data about smart growth of city, 25 indi- cators are selected by principal component analysis. Then we construct a new three-level indicator system, where the first level has 1 indicator, the second level has 5 indicators and the third level has 25 indicators to evaluate the success degree of the smart growth. Moreover, we use the entropy weight method (EWM) to get weight vector of the indica- tors in the third level and the group decision making method (GDM) to get the weight vector of indicators in the second-class. Meanwhile, the standard of the success of the smart growth is obtained through K-means algorithm. A metric system which include the intensity of land, social equity degree, traffic quality, coordination degree and economic development level, is eventually built to measure the success of smart growth of a city.

<!-- b000009 | prose | pages [1] -->
In task2, Pittsburgh and Ningguo are selected to research their current growth plan. Through the metric proposed in Task 1, the strengths and weaknesses of the current growth plan of selected cities is measured.

<!-- b000010 | prose | pages [1] -->
In task3, our smart growth plan is developed based on the index value of the cities. Then the support vector machine (SVM) and weighted moving average method(WMAM) are adopted to predict the change of indicators. The combined prediction model is subse- quently adopted to minimize the prediction error. Eventually, by comparing the indicator between current city plan and our smart growth plan, we can see the success of our smart growth plan.

<!-- b000011 | prose | pages [1] -->
In task4, the single effect of the individual initiatives is evaluated by our metric to rank the potential. The result shows that the most potential to the success degree of the smart growth is the initiative of the economic development in Ningguo, while in Pitts- burgh is the initiative of improving land intensive rate.

<!-- b000012 | prose | pages [1] -->
In task5, since the population structure between the two cites is different, two dif- ferent population growth models(PGM) are adopted to predict the change of the popula- tion. The growth rate calculated by PGM demonstrates that our plan can adjust adaptively to satisfied the increasing need of population.

<!-- b000013 | prose | pages [1] -->
Finally, we analyze the strengths and weaknesses of the methods we proposed in this paper. The research can also satisfy the need of the ICM and make reasonable growth theories into city design.

<!-- b000014 | heading | pages [2] -->
Contents

<!-- b000015 | contents | pages [2] -->
1

<!-- b000016 | contents | pages [2] -->
Introduction .................................................................................................................. 3

<!-- b000017 | contents | pages [2] -->
1.1 Background ........................................................................................................................................... 3

<!-- b000018 | contents | pages [2] -->
1.2 Problem Statement and Analysis .......................................................................................................... 3

<!-- b000019 | contents | pages [2] -->
2. Assumption and Symbol Explanation ........................................................................... 4

<!-- b000020 | contents | pages [2] -->
2.1 Assumption ........................................................................................................................................... 4

<!-- b000021 | contents | pages [2] -->
2.2 Symbol Explanation.............................................................................................................................. 4

<!-- b000022 | contents | pages [2] -->
3.Task 1 ................................................................................................................................ 4

<!-- b000023 | contents | pages [2] -->
3.1 Data Pre-processing ................................................................................................................................ 4

<!-- b000024 | contents | pages [2] -->
3.2 Primary Indicator System ........................................................................................................................ 5

<!-- b000025 | contents | pages [2] -->
3.3 Weighting Models of Evaluation Indicators ............................................................................................. 7

<!-- b000026 | contents | pages [2] -->
3.4 Comprehensive Evaluation Index ...........................................................................................................10

<!-- b000027 | contents | pages [2] -->
3.5 Metric of Smart Growth .......................................................................................................................12

<!-- b000028 | contents | pages [2] -->
4 Task 2 ............................................................................................................................. 13

<!-- b000029 | contents | pages [2] -->
4.1 Growth Plan of Selected Cities ............................................................................................................13

<!-- b000030 | contents | pages [2] -->
4.2 City Index Evaluation ..........................................................................................................................14

<!-- b000031 | contents | pages [2] -->
4.3 Analysis of Current Growth Plan .........................................................................................................14

<!-- b000032 | contents | pages [2] -->
5 Task 3 ............................................................................................................................. 14

<!-- b000033 | contents | pages [2] -->
5.1 Our Smart Growth Plan(SGP) .............................................................................................................14

<!-- b000034 | contents | pages [2] -->
5.2 The Prediction Models for Evaluation .................................................................................................15

<!-- b000035 | contents | pages [2] -->
5.3 The Evaluation of Our Smart Growth Plan ..........................................................................................16

<!-- b000036 | contents | pages [2] -->
6 Task 4 ............................................................................................................................. 17

<!-- b000037 | contents | pages [2] -->
6.1 Ranking the Individual Initiatives ........................................................................................................17

<!-- b000038 | contents | pages [2] -->
6.2 Comparing the Initiatives of Two Cities ..............................................................................................18

<!-- b000039 | contents | pages [2] -->
7 Task 5 ............................................................................................................................. 18

<!-- b000040 | contents | pages [2] -->
7.1 The Adaptable Plan For Pittsburgh ......................................................................................................19

<!-- b000041 | contents | pages [2] -->
7.2 The Adaptable Plan For Ningguo ........................................................................................................19

<!-- b000042 | contents | pages [2] -->
8. Sensitivity Analysis ....................................................................................................... 20

<!-- b000043 | contents | pages [2] -->
9. Strengths and Weaknesses ........................................................................................... 21

<!-- b000044 | contents | pages [2] -->
9.1 Strengths ..............................................................................................................................................21

<!-- b000045 | contents | pages [2] -->
9.2 Weaknesses ..........................................................................................................................................21

<!-- b000046 | contents | pages [2] -->
References .......................................................................................................................... 21

<!-- b000047 | contents | pages [2] -->
Appendix ............................................................................................................................ 22

<!-- b000048 | furniture | pages [3] -->
Team # 65123

<!-- b000049 | furniture | pages [3] -->
Page 3 of 23

<!-- b000050 | heading | pages [3] -->
1 Introduction

<!-- b000051 | heading | pages [3] -->
1.1 Background

<!-- b000052 | prose | pages [3] -->
In recent years, urbanization has become an inevitable trend. It has been predicted that by 2050, about 66 percent of the world's population will be added to the city. [1] Consequently, formulating suitable urban plans have become a concern of governments. At an earlier time, some cities chose ‘urban sprawl’ strategy, namely, just like standing pancake. Urban sprawl is a special form of suburbanization. It includes the marginal expansion of the existing urbanization areas with very low population density, occupy- ing land that has never been developed. Gradually, many problems were exposed when urban sprawl was carried out, such as environmental pollution, the land in excess con- sumption, High-cost infrastructure construction, etc.

<!-- b000053 | prose | pages [3] -->
In view of those problems, the concept of smart growth was proposed by Geoff Allderson. Ten principles for smart growth are proposed subsequently in [2]. SG is a means to curb continued urban sprawl and reduce the loss of farmland surrounding ur- ban centers. It will make the town or city approach a more economically prosperous, socially equitable, and environmentally sustainable place.

<!-- b000054 | heading | pages [3] -->
1.2 Problem Statement and Analysis

<!-- b000055 | prose | pages [3] -->
Since smart growth is essential to urban construction, it is significant to propose an efficient method to give plans to meet the principle for smart growth in this problem. Therefore, index system is needed to evaluate the success of smart growth of a city firstly. Two specific cities are selected to evaluate the effect of their growth plans through index system. Then we have to propose feasible plans to help the growth of our selected cities. To measure the success of our plans, the index system is needed in a second time. Moreover, the potential of the individual initiatives should be ranked in this problem. Eventually, we need to explain in what ways our plan supports this level of growth if the population will increase by an additional 50% by 2050.

<!-- b000056 | prose | pages [3] -->
Through the above analysis, the flow chart of this paper is shown in fig.1 as fel- lows.

<!-- b000057 | caption | pages [3] -->
Fig.1 The flow chart in this paper

<!-- b000058 | furniture | pages [4] -->
Team # 65123

<!-- b000059 | furniture | pages [4] -->
Page 4 of 23

<!-- b000060 | heading | pages [4] -->
2. Assumption and Symbol Explanation

<!-- b000061 | heading | pages [4] -->
2.1 Assumption

<!-- b000062 | prose | pages [4] -->
 The government policy will not change in the short term.

<!-- b000063 | prose | pages [4] -->
 The data source is actual and reliable.

<!-- b000064 | prose | pages [4] -->
 Neglect the explosive changes when forecasting over the few decades.

<!-- b000065 | prose | pages [4] -->
 Score matrix given by experts is not affected by subjective factors.

<!-- b000066 | heading | pages [4] -->
2.2 Symbol Explanation

<!-- b000067 | heading | pages [4] -->
Symbol

<!-- b000068 | prose | pages [4] -->
Definition SDSG the success degree of smart growth of a city

<!-- b000069 | prose | pages [4] -->
IOL The intensity of land

<!-- b000070 | prose | pages [4] -->
SED The social equity degree

<!-- b000071 | prose | pages [4] -->
EDL The economic development level

<!-- b000072 | prose | pages [4] -->
TQ The traffic quality

<!-- b000073 | prose | pages [4] -->
CD The coordination degree

<!-- b000074 | prose | pages [4] -->
the sum of squares of the distances from the sort center J (c ) k The weight of the -i th secondary indicator iw

<!-- b000075 | prose | pages [4] -->
3.Task 1

<!-- b000076 | heading | pages [4] -->
3.1 Data Pre-processing

<!-- b000077 | heading | pages [4] -->
3.1.1 Data Collection

<!-- b000078 | prose | pages [4] -->
Collecting sufficient data is the basis of developing a complete index system. We searched the database and found 88 indicators of two cities firstly. The data of Pitts- burgh in Pa is from city data 1 and the data of Ningguo which is located in Anhui, Chi- na are from National Bureau of Statistics of the People's Republic of China 2. Then we searched the data of the ten cities which is used to set standards by clustering.

<!-- b000079 | heading | pages [4] -->
3.1.2 Data Filling

<!-- b000080 | prose | pages [4] -->
The availability of data is an essential issue. No measures, regardless of its value, can provide efficient assessments if based on unreliable or untruthful data. Consequent- ly, it is essential to ensure the continuity and authenticity of the research data. Never- theless, some data is missing because not all data is provided in the website.

<!-- b000081 | prose | pages [4] -->
To ameliorate this situation, four methods are proposed to complete the data, which are as follows,  If the indicator values are smooth, previous data can be adopted to replace it.

<!-- b000082 | prose | pages [4] -->
 If the data before and after can be obtained, the average value can be taken as the missing.

<!-- b000083 | prose | pages [4] -->
 If two groups are similar, then the missing data in one group can be replaced by the value of the same location in the other group.

<!-- b000084 | prose | pages [4] -->
1  http://www.city-data.com/ 2  http://data.stats.gov.cn/.

<!-- b000085 | furniture | pages [5] -->
Team # 65123

<!-- b000086 | furniture | pages [5] -->
Page 5 of 23

<!-- b000087 | prose | pages [5] -->
 The interpolation method is used in data fitting.

<!-- b000088 | heading | pages [5] -->
3.2 Primary Indicator System

<!-- b000089 | heading | pages [5] -->
3.2.1 Select primary indicators by PCA

<!-- b000090 | prose | pages [5] -->
88 initial indicators are selected firstly to represent the smart growth of cities. Be- cause there are a great deal of indicators related to smart growth, the method of PCA (Principal Component Analysis) is adopted to reduce the number of primary indicators. The selection of the initial 88 indicators for smart growth is based on 3E’s principles and 10 principles.

<!-- b000091 | prose | pages [5] -->
3E’s principles refers to Economically prosperous(EP), socially Equitable(SEQ), and Environmentally sustainable(ESU). Namely, keep economy sustained and steady, guarantee the right to fair and ensure environmental protection if the government adopt smart growth strategy.

<!-- b000092 | prose | pages [5] -->
Since the smart growth was presented in 1990’s, the ten principles for smart growth (SGP) have been proposed [2]. The SGP is also adopted as reference principles in our index selection. The SGP is mainly as follows:

<!-- b000093 | prose | pages [5] -->
(1) Mix land uses.

<!-- b000094 | prose | pages [5] -->
(2) Take advantage of compact building design.

<!-- b000095 | prose | pages [5] -->
(3) Create a range of housing opportunities and choices.

<!-- b000096 | prose | pages [5] -->
(4) Create walkable neighborhoods.

<!-- b000097 | prose | pages [5] -->
(5) Foster distinctive, attractive communities with a strong sense of place.

<!-- b000098 | prose | pages [5] -->
(6) Keep open space, farmland, natural beauty, and critical environmental areas.

<!-- b000099 | prose | pages [5] -->
(7) Strengthen and direct development towards existing communities.

<!-- b000100 | prose | pages [5] -->
(8) Provide a variety of transportation choices.

<!-- b000101 | prose | pages [5] -->
(9) Make development decisions predictable, fair, and cost effective.

<!-- b000102 | prose | pages [5] -->
(10) Encourage community and stakeholder collaboration in development deci- sions.

<!-- b000103 | prose | pages [5] -->
From the aforementioned selections, the initial selection of the primary indicators is selected. Then the method of PCA is adopted to reduce the number of the indicator. Eventually, 25 indicators are obtained as our primary indicators. Primary indicators are shown as in Tab. 1.

<!-- b000104 | prose | pages [5] -->
Tab.1 Framework of sustainability indicators Indicator Unit Explanation Type It represents the structure of the land use. 1 ,6 - 1x Diversity of land use:

<!-- b000105 | prose | pages [5] -->
Percent Building density is appeared in this indicate. 2 2x Floor area ratio:

<!-- b000106 | prose | pages [5] -->
Percent It reflects the quantity of land use degree. 2 3x Land-use ratio:

<!-- b000107 | prose | pages [5] -->
It represents the characteristics of the city in - 5 4x Urban Characteristics: culture, nature, and history etc.

<!-- b000108 | prose | pages [5] -->
It denotes the groups of green belt such as Sq. M 6 5x Public green space: residential area, parks etc.

<!-- b000109 | prose | pages [5] -->
It denotes the actual control of the land area of Sq. M ESU 6x Land occupation: the city. Per capita water consump- It refers to the average daily water consump- Ton ESU tion of each people. 7x tion:

<!-- b000110 | prose | pages [5, 6] -->
ppm It presents the gas emissions from the factory. ESU Industrial waste gas emis- 8x sion:

<!-- b000111 | furniture | pages [6] -->
Team # 65123

<!-- b000112 | furniture | pages [6] -->
Page 6 of 23

<!-- b000114 | prose | pages [6] -->
Industrial solid waste emis- Kilo- It presents the solid emissions from the facto- ESU tons ry. 9x sion:

<!-- b000115 | prose | pages [6] -->
Wastewater It is defined as an indicator to evaluate the Ton/day ESU quantity of wastewater. x discharge: 10 Collaboration in It reflects the collaboration in developing de- - 7 ,10 cisions. development:CID It represents the degree of fairness in the in- - SEQ Gini Coefficient:G come distribution. Employment rate of male and It reflects the different employment opportuni- Percent SEQ ties that result from gender x female: 11 Education equity is represented by this indica- Percent SEQ x School attendance Rate: tor. 12 It denotes the amount of housing grants for Dollar SEQ ,3 x Housing subsidy: low-income people. 13 It represents the ratio of the perpetrators to the Percent SEQ, 5 x Crimes rate: total population. 14

<!-- b000116 | prose | pages [6] -->
Economic efficient It reflects the effectiveness of urban economic - EP development index: EEI

<!-- b000117 | prose | pages [6] -->
Economic structure The economic structure of city is presented in - EP this indicator. index: ESI

<!-- b000118 | prose | pages [6] -->
Economic cost It reflects the cost of economic development - EP in cities. index: ECI

<!-- b000119 | prose | pages [6] -->
Gross Domestic It is the core indicator of city economic ac- Dollar EP counting. Product:GDP

<!-- b000120 | prose | pages [6] -->
Per capita fiscal Dollar Assessing government administration cost EP 9 x expenditure： 15 It indicates whether people have the suitable Sq. M 4 x Pedestrian street area: footpath. 16 It refers to the average level of ownership of unit 8 x Per capita amount of cars: vehicles in cities. 17

<!-- b000121 | prose | pages [6] -->
Transportation It represents the diversity of urban transport. 8 - x diversity: 18 Density of road It reflects the development level of urban km 1 8 transportation. x network: 19 In this table, the Type value between 1-10 represents this indicator which reflects SGP. EP reflects the economically prosperous in 3E’s principle, while SEQ means so- cially Equitable. And ESU means environmentally sustainable.

<!-- b000122 | heading | pages [6] -->
3.2.2 Data normalization

<!-- b000123 | prose | pages [6] -->
Since the dimensions of the 25 indicators are different, the data can’t be directly compared. To normalized the data, all the data is converted to number between 0 and 1.

<!-- b000124 | prose | pages [6, 7] -->
Comparing these 25 indicators, the indexes can be classified as three types, cost- type index, benefit-type index and moderate-type index. Among the three classes of in- dexes, the smaller the cost-type index is, the better the success degree of smart growth is. The benefit-type index is opposite. Moderate-type index is better when it closer to a specific value. Due to the different contribution of the indexes, the three types of data are normalized in different ways as follows.

<!-- b000125 | furniture | pages [7] -->
Team # 65123

<!-- b000126 | furniture | pages [7] -->
Page 7 of 23

<!-- b000128 | prose | pages [7] -->
 Q  cost-type index j   x denote the j th index of the i th Let city, it can be expressed as [3] ij

<!-- b000129 | prose | pages [7] -->
 max x x j ij    x min , i 1, ,25; j 1,2 ij  max x x j j

<!-- b000130 | prose | pages [7] -->
where    max jx max x x , 1 2    min jx min x x , 1 2

<!-- b000131 | prose | pages [7] -->
and is the largest value of Q , is the smallest value of Q . max min jx jx j j

<!-- b000132 | prose | pages [7] -->
 Q  benefit-type index j

<!-- b000133 | prose | pages [7] -->
 min x x ij j    x min , i 1,2, 23; j 1,2 ij  max x x j j

<!-- b000134 | prose | pages [7] -->
 Q  Moderate-type index j

<!-- b000135 | prose | pages [7] -->
  s d 1 ij   1 d s    ij 1   min max max s d , d s  1 j j 2    x 1 d s  ij ij 1   d s  ij 2  1 d s    ij 1   min min max s d , d s  2 j j 2

<!-- b000136 | prose | pages [7] -->
where 1s is the best value of the indicator Q .

<!-- b000137 | heading | pages [7] -->
3.2.3 Quantification of qualitative indicators

<!-- b000138 | prose | pages [7] -->
Some qualitative indicators are used in our primarily indicators. Therefore, it is es- sential to propose a suitable metric to quantify indicators. Fuzzy evaluation [4] is adopted to solve this problem. In this model, we letu denote evaluation set. And A is weight set, which is obtained by AHP. W is a set of comments made up of comments such as good, worse and etc. The relationship betweenW andU is described by fuzzy evaluation ma- trix R . The comprehensive evaluation model P is given by     P A R p , p , p p 1 2 3 n   . ijr is calculated byW . represents the mini-    Note that p a r j 1,2, n n i ij ija and ijr .Andrepresents the maximum in   mum between a r . ij ij Let F denote the set of score, the evaluation score Z is calculated ultimately by the following formula.

<!-- b000139 | prose | pages [7] -->
  Z P F

<!-- b000140 | heading | pages [7] -->
3.3 Weighting Models of Evaluation Indicators

<!-- b000141 | prose | pages [7] -->
Weighting models is essential to evaluate the different contribution of the indicators. Consequently, two weighting models are adopted to calculated the weight vector in this section.

<!-- b000142 | heading | pages [7] -->
3.3.1 Weighting Model Based on Entropy Weight Method(EWM)

<!-- b000143 | furniture | pages [8] -->
Team # 65123

<!-- b000144 | furniture | pages [8] -->
Page 8 of 23

<!-- b000145 | prose | pages [8] -->
Since the current indicators are not uniformed, the target treatment is needed to re- duce the dimension of indicators firstly. In this paper, we adopt the entropy weight meth- od based on correlation coefficient to solve this problem. The detailed algorithm is shown as follows in fig.2.

<!-- b000146 | caption | pages [8] -->
Fig.2 The flow of calculation weights of indicators using EWM

<!-- b000147 | prose | pages [8] -->
For the data of indicator involved in the table, we first get a matrix as follow:

<!-- b000148 | prose | pages [8] -->
  index I X X X 1 11 12 1 n   index I X X X    2 21 22 2 n X   ij   index I X X X   m m 1 m 2 mn

<!-- b000149 | prose | pages [8] -->
Step Ⅰ： The indicators of participation in the evaluation of the LB-type3 and the SB-type. For the different index values we use the following two formulas for normalization.

<!-- b000150 | prose | pages [8] -->
 X / max X for LB ij ij  * X ij min X / X for SB  ij ij

<!-- b000151 | prose | pages [8] -->
Step Ⅱ：

<!-- b000152 | prose | pages [8] -->
Let ijP denote the ratio of each indicator, it can be calculated by the following formu- la:

<!-- b000153 | prose | pages [8] -->
X  ij P ij m  x ij  j 1

<!-- b000154 | prose | pages [8] -->
ie is obtained by the following formula: where the entropy value

<!-- b000155 | prose | pages [8] -->
m  e k p ln p i ij ij  j 1

<!-- b000156 | prose | pages [8] -->
Step Ⅲ： The correlation coefficient is calculated as

<!-- b000157 | prose | pages [8] -->
n       e e s s i i   i 1 r E S ( , ) n n       2 2   e e s s i i   i 1 i 1

<!-- b000158 | prose | pages [8] -->
where S denotes the standard index entropy obtained by clustering a large amount of data.

<!-- b000159 | heading | pages [8] -->
3 LB: the lager the better, SB: the smarter the better

<!-- b000160 | furniture | pages [9] -->
Team # 65123

<!-- b000161 | furniture | pages [9] -->
Page 9 of 23

<!-- b000162 | prose | pages [9] -->
Step Ⅳ： Through this step, an optimization model, which is shown as below, is used to make the entropy weight.

<!-- b000163 | prose | pages [9] -->
m   max r W k k  k 1  m   W 1  k s t . .  k 1    0, k 1.. m W k

<!-- b000164 | prose | pages [9] -->
W . According to the optimization model aforementioned, we can get the final weight k Since the correlation entropy is proportional to the weight, the final determined weight has a good positive correlation with the entropy in the modified optimization model.

<!-- b000165 | prose | pages [9] -->
The specific indicator weight based on the data will be presented in Section 4.1.

<!-- b000166 | heading | pages [9] -->
3.3.2 Weighting Model Based on Group Decision Making Method

<!-- b000167 | prose | pages [9] -->
In order to complete the synthesis of indicators, we use consistent judgment matrix (GDM) for each primary indicators for weighting. We get the indicators in the above text and the GDM for this evaluation is given as below (cf. Fig.3):

<!-- b000168 | caption | pages [9] -->
Fig.3. The GDM for determine planning scheme of city

<!-- b000169 | prose | pages [9] -->
For each expert, we obtain a consistent complementary judgment matrix, which is scored according to the expert's experience with the indicator according to the scoring table. Matrixes are shown as below:

<!-- b000170 | prose | pages [9, 10] -->
C 1 C 2 C 3 C 4 C 5 C 1 C 2 C 3 C 4 C 5     C 1 0.5 0.1 0.2 0.7 0.3 C 1 0.5 0.2 0.1 0.6 0.3     C 2 0.9 0.5 0.4 0.6 0.2 C 2 0.8 0.5 0.2 0.8 0.2           ( ) ( ) Ⅰ Ⅱ E C 3 0.8 0.6 0.5 0.3 0.1 E C 3 0.9 0.8 0.5 0.4 0.1     C 4 0.3 0.4 0.7 0.5 0.2 C 4 0.4 0.2 0.6 0.5 0.2         C 5 0.7 0.8 0.9 0.8 0.5 C 5 0.7 0.8 0.9 0.8 0.5         C 1 0.5 0.6 0.4 0.2 0.4 C 1 0.5 0.2 0.4 0.6 0.2     C 2 0.4 0.5 0.1 0.3 0.1 C 2 0.8 0.5 0.1 0.3 0.4           ( ) ( ) Ⅲ Ⅳ E C 3 0.6 0.9 0.5 0.4 0.2 E C 3 0.6 0.9 0.5 0.3 0.1     C 4 0.8 0.7 0.6 0.5 0.2 C 4 0.4 0.7 0.7 0.5 0.2         C 5 0.6 0.9 0.8 0.8 0.5 C 5 0.8 0.6 0.9 0.8 0.5     We can obtain the weights by solving the eigenvectors of the above matrix.

<!-- b000171 | furniture | pages [10] -->
Team # 65123

<!-- b000172 | furniture | pages [10] -->
Page 10 of 23

<!-- b000173 | furniture | pages [10] -->
C

<!-- b000174 | furniture | pages [10] -->
1

<!-- b000175 | furniture | pages [10] -->
C

<!-- b000176 | furniture | pages [10] -->
2

<!-- b000177 | furniture | pages [10] -->
C

<!-- b000178 | furniture | pages [10] -->
3

<!-- b000179 | furniture | pages [10] -->
C

<!-- b000180 | furniture | pages [10] -->
4

<!-- b000181 | furniture | pages [10] -->
C

<!-- b000182 | furniture | pages [10] -->
5

<!-- b000183 | furniture | pages [10] -->
C

<!-- b000184 | furniture | pages [10] -->
1

<!-- b000185 | furniture | pages [10] -->
C

<!-- b000186 | furniture | pages [10] -->
2

<!-- b000187 | furniture | pages [10] -->
C

<!-- b000188 | furniture | pages [10] -->
3

<!-- b000189 | furniture | pages [10] -->
C

<!-- b000190 | furniture | pages [10] -->
4

<!-- b000191 | furniture | pages [10] -->
C

<!-- b000192 | furniture | pages [10] -->
5

<!-- b000194 | prose | pages [10] -->
According to the group decision-making method, the final weight can be obtained by combining the weight of experts and the weight of judgment matrix using the fol- lowing equation：   * ( ) i W W i  i 1..4

<!-- b000195 | prose | pages [10] -->
where the result of the W can be seen in the fellows.

<!-- b000196 | prose | pages [10] -->
, ,   ( ) T ( ) T Ⅰ Ⅱ W (0.1049 0.15027 0.2137 0.2675 0.2635) W (0.1370 0.2638 0.1381 0.1944 0.2667) ,   ( ) T ( ) T Ⅲ Ⅳ W (0.1000 0.1481 0.1496 0.2885 0.3137) W (0.1260 0.2346 0.2283 0.2017 0.2094)

<!-- b000197 | prose | pages [10] -->
The reliability of the weight is checked by the following method：

<!-- b000198 | prose | pages [10] -->
 Through the consistency test, the consistency index value which should tend to ze-     CI ( n ) / ( n 1) ro is . max  We calculated the consistency ratio  , When ,the value of RI n  CR CI / RI 1,..., 20 is given as 0(1), 0(2), 0.52(3), 0.89(4),1.12(5)...1.63(19),1.64(20) ,where the numbers in brackets indicate n .

<!-- b000199 | prose | pages [10] -->
Through the method aforementioned, the weight vector of second-class indicator is eventually calculated. The specific value of the weight vector is shown in section 3.4.2.

<!-- b000200 | heading | pages [10] -->
3.4 Comprehensive Evaluation Index

<!-- b000201 | heading | pages [10] -->
3.4.1 Determination of Second-class index

<!-- b000202 | prose | pages [10] -->
Five second-class indicators are identified after selecting a set of comprehensive and effective primary indicators and determining the reasonable weights, including The Inten- sity of land (IOL), Coordination degree(CD), Social equity degree (SED), Economic de- velopment level (EDL) and Traffic Quality (TQ). Especially, these five second-class indi- cators will be used to evaluate five dimensions of the smart growth city.

<!-- b000203 | prose | pages [10] -->
The Intensity of land (IOL), is the most important index of smart growth. IOL main- ly contains five primary indicators. It’s mainly used to reflect the efficiency of land using, the diversity of land using and the rationality of land planning, etc.  Coordination degree(CD)is consisted of resource coordination degree, ecological co- ordination degree, cooperation and coordination degree. On the one hand, it reflects the resources and ecological carrying capacity. On the other hand, it mirrors commu- nication and cooperation between governments and stakeholders.  Social equity degree (SED) considers the gap between the rich and poor, protection of socially vulnerable groups (e.g. women, children, the poor). Moreover, it also takes the safety into account.  Economic development level (EDL) is related to the quality of and the number of economic development. What’s more, per capita fiscal expenditure also is consid- ered.it can measure cost effective degree.  Traffic Quality (TQ) expresses the regional level of patency. At the same time, TQ contains streets that People can walk freely.

<!-- b000204 | prose | pages [10, 11] -->
The composition of the second-class indicators and the weight composition are shown as below.

<!-- b000205 | furniture | pages [11] -->
Team # 65123

<!-- b000206 | furniture | pages [11] -->
Page 11 of 23

<!-- b000208 | prose | pages [11] -->
Tab.2 The weight of second-class indicator

<!-- b000209 | prose | pages [11] -->
Second- Primary indicator and Primary indicator and Second-class class indica- weight weight indicator tor Diversity of land use (10%) Pedestrian street area (23%)

<!-- b000210 | prose | pages [11] -->
Per capita amount of cars Traffic The Floor area ratio (15%) Intensity (24%) Quality Of land (IOL)(26.7% (TQ)(10.5%) Land-use ratio (15%) Transportation diversity (27%) ) Urban Characteristics (29%) Density of road network (26%)

<!-- b000211 | prose | pages [11] -->
Public green space (31%) Land occupation (10%)

<!-- b000212 | prose | pages [11] -->
Per capita water consumption Gini Coefficient (13%) (15%)

<!-- b000213 | prose | pages [11] -->
Employment rate of male Industrial waste gas emission Coordination Social and female (23%) (18%) Degree equity School attendance Rate Industrial solid waste emission (CD)(26.4%) degree (13%) (23%) (SED)(15.0%) Housing subsidy (20%) Wastewater discharge (16%)

<!-- b000214 | prose | pages [11] -->
Collaboration in development Crimes rate (21%) (28%)

<!-- b000215 | prose | pages [11] -->
Economic efficient index Gross Domestic Product (19%) Economic (14%) Development Economic structure index level (EDL)(21.4%) (26%) Per capita fiscal expenditure (27%) Economic cost index (14%)

<!-- b000216 | heading | pages [11] -->
3.4.2 Determination of First-Class Index

<!-- b000217 | prose | pages [11] -->
Based on the indicator system and weight method aforementioned, a comprehensive index is proposed to measure the success degree of smart growth (SDSG) of a city. The indicator system is used to provide the essential second-class indicators, while the  weight method is adopted to evaluate the weights w of the SGSD. Let SGSD denote the success degree of smart growth. The function of SGSD can be represented by      SDSG w * IOL w * SED w * TQ w * CD w * EDL 1 2 3 4 5 iw is the weight of  i th second-class indicator. The specific weights are as where follows.

<!-- b000218 | prose | pages [11, 12] -->
  w  0.267 0.150 0.105 0.264 0.214 Through the above analysis, a three-level comprehensive evaluation system is estab- lished. The three levels of evaluation indicators are shown in Fig.4 .

<!-- b000219 | furniture | pages [12] -->
Team # 65123

<!-- b000220 | furniture | pages [12] -->
Page 12 of 23

<!-- b000222 | caption | pages [12] -->
Fig.4. Three-level indicator system diagram

<!-- b000223 | prose | pages [12] -->
From the fig.4, we can see that the indicator of our system diagram is divided into three levels. Through the indicator system we established, the efficient metric is set up to measure the success of the smart growth degree.

<!-- b000224 | heading | pages [12] -->
3.5 Metric of Smart Growth

<!-- b000225 | heading | pages [12] -->
3.5.1 Standard Setting Based on K-means Algorithm(KA)

<!-- b000226 | prose | pages [12] -->
Although three-levels of evaluation has been established aforementioned, a suitable standard is still needed to assess the success degree of smart growth in cites. Consequent- ly, KA (K-means Clustering Algorithm) is adopted to make a reasonable standard. In this algorithm, the data set X includes 25 second-class indicators. And K denotes the number of the data subset, which is 3 in our method. The data objects are organized into 3 parti-  denote the sort center of the partitions, the sum of squares of the dis- tions by KA. Let k tances from the sort center is represented by    2    J c x k i k  x C i k where   J c denotes the sum of squares of the distances from the sort center. The k goal of the PCA is to solve the following optimization problem.

<!-- b000227 | prose | pages [12] -->
2 3 10     min d x ki i k    k 1 i 1  1 x c  s t d . . i i  0 x c ki i i

<!-- b000228 | heading | pages [12] -->
3.5.2 The Standard of Smart Growth(SG)

<!-- b000229 | prose | pages [12] -->
According to the KA aforementioned, the standard of SG is obtained eventually in this section. For each index, two class centers are calculated by clustering ten cities data firstly. Then the mean of the indicator centers is used as the standard boundary. The standard of smart growth is shown in fig.4.

<!-- b000230 | furniture | pages [13] -->
Team # 65123

<!-- b000231 | furniture | pages [13] -->
Page 13 of 23

<!-- b000232 | caption | pages [13] -->
Fig.5. The Standard of Smart Growth

<!-- b000233 | prose | pages [13] -->
The standard of each index is described in bar chart, which can evaluate the second- class indicator qualitatively through interval. We use qualitative descriptions such as normal, good and excellent to measure the success of the city in an indicator. Normal means that the city has not realized smart growth in this area. And good means that the city has some success of SG in this area. Excellent is used to describe when city has great success of SG. Combining five second-class indexes, the radar diagram is adopted to de- scribe the overall success of city in smart growth. The standard line is also shown in the

<!-- b000234 | caption | pages [13] -->
fig.5.

<!-- b000235 | heading | pages [13] -->
4 Task 2

<!-- b000236 | heading | pages [13] -->
4.1 Growth Plan of Selected Cities

<!-- b000237 | prose | pages [13] -->
In this paper, Pittsburgh in Pa, US and Ningguo in Anhui, China are selected as ex- amples to analyze the smart growth problem. There are about 322,450 people living in Pittsburgh. It is known as both "the Steel City" for its more than 300 steel-related busi- nesses, and as the "City of Bridges" for its 446 bridges. The total population of Ningguo are 383,800 people. The area is 2487 square kilometers. As shown in fig.6, the left is Pittsburgh and Ningguo is on the right.

<!-- b000238 | caption | pages [13] -->
Fig.6. The satellite map of the selected city

<!-- b000239 | prose | pages [13] -->
The governments of two cities both have developed growth plans.

<!-- b000240 | prose | pages [13] -->
The plan of Ningguo is as follows.

<!-- b000241 | prose | pages [13] -->
 Develop special industries and high-tech enterprises.

<!-- b000242 | furniture | pages [14] -->
Team # 65123

<!-- b000243 | furniture | pages [14] -->
Page 14 of 23

<!-- b000244 | prose | pages [14] -->
 Promote agricultural industrialization, specialization.

<!-- b000245 | prose | pages [14] -->
 Strengthen the construction of transport facilities.

<!-- b000246 | prose | pages [14] -->
 Make every citizen has the right to equal access to education.

<!-- b000247 | prose | pages [14] -->
 Enhance the city characteristics.

<!-- b000248 | prose | pages [14] -->
And the below is the plan of Pittsburgh.

<!-- b000249 | prose | pages [14] -->
 Let people live in renovated homes and enjoy its parks, shops, and churches.

<!-- b000250 | prose | pages [14] -->
 Protect and restore the ecological environment.

<!-- b000251 | prose | pages [14] -->
 Reduce air pollution, water pollution, solid pollution.

<!-- b000252 | prose | pages [14] -->
 Maintain economic prosperity and development.

<!-- b000253 | heading | pages [14] -->
4.2 City Index Evaluation

<!-- b000254 | prose | pages [14] -->
Based on the index system in section3.4 and the proposed standards in section3.5, the indexes which can reflect five dimensions of the city is calculated. The result is shown in fig.7 as fellows.

<!-- b000255 | caption | pages [14] -->
Fig.7. The index value of the selected city

<!-- b000256 | prose | pages [14] -->
The specific analysis associated with the diagram is described in section4.3. The brown line in radar means the second-level indicator of Pittsburgh, while the blue line means the second-level indicator of Ningguo. Moreover, the bottom line means the pass line of the indicator, while the super line means the excellent line of the indicators.

<!-- b000257 | heading | pages [14] -->
4.3 Analysis of Current Growth Plan

<!-- b000258 | prose | pages [14] -->
After grasping the plan we searched in section4.1 and the result in section4.2, we can have a detailed analysis about our selected cities.

<!-- b000259 | prose | pages [14] -->
Firstly, as we can see from fig.7. In general, the indicator values of Pitts-burgh are larger than the Ningguo. The reason is that Pittsburgh is more developed than Ningguo. It’s economy and Society is more prosperous and equitable. Apart from this, the environment and Transport of Pittsburgh are more sustainable and convenient.

<!-- b000260 | prose | pages [14] -->
Specifically speaking, the values of five indicators of Ningguo are generally small, especially in coordination degree and economic development level. Its social equity de- gree (SED) and traffic quality (TQ) is at an average level.  The intensity of land is just on the bottom line. Although the government of Ningguo developed a growth plan, it is not very perfect. It’s growth plan includes developing industry, agriculture, tertiary industry, ensuring fairness, keeping the city characteristics. It not involve with environmental pro- tection, intensive use of urban land, infrastructure construction and so on.  All these lead to the low level of smart growth of Ningguo.

<!-- b000261 | prose | pages [14] -->
Pittsburgh 's indicator values are relatively high. Social equity degree (SED)and traf- fic quality (TQ) are outstanding. This is largely related to its growth policy. Pittsburgh pays more attention to human, the ecological environment and economy. scientific plan makes Pittsburgh meet the smart growth principles relatively successfully.

<!-- b000262 | heading | pages [14] -->
5 Task 3

<!-- b000263 | heading | pages [14] -->
5.1 Our Smart Growth Plan(SGP)

<!-- b000264 | furniture | pages [15] -->
Team # 65123

<!-- b000265 | furniture | pages [15] -->
Page 15 of 23

<!-- b000266 | prose | pages [15] -->
Considering current growth plans of two cities still have room for improvement, we develop a series of smart growth plans for the two cities.

<!-- b000267 | prose | pages [15] -->
The growth plan includes in Pittsburgh is shown as following.

<!-- b000268 | prose | pages [15] -->
1. Improve the land intensive rate to achieve an annual land use growth of 1%.

<!-- b000269 | prose | pages [15] -->
2. Optimize the economic development structure, so that the economic efficiency index increases per year by 2%.

<!-- b000270 | prose | pages [15] -->
3. Encourage community and stakeholder collaboration in development decisions.

<!-- b000271 | prose | pages [15] -->
For Ningguo, due to its low level of smart growth, we proposed a more detailed plan.

<!-- b000272 | prose | pages [15] -->
The plan for Ningguo is as following.

<!-- b000273 | prose | pages [15] -->
1. To improve the intensity of land, the Ningguo government should encourage the construction of high-rise residential. it can increase the floor area ratio and im- prove space utilization efficiency.

<!-- b000274 | prose | pages [15] -->
2. To increase coordination degree, the Ningguo government should strengthen the control of the factory and cultivate environmental awareness of residents.

<!-- b000275 | prose | pages [15] -->
3. To push on the economic development, we recommend the Ningguo government to expand investment, encourage the development of small and medium enter- prises.

<!-- b000276 | prose | pages [15] -->
4. To promote the social equity, the Ningguo government should increase protection of vulnerable groups, such as increase child welfare.

<!-- b000277 | prose | pages [15] -->
5. To ameliorate traffic quality, the government should improve road network densi- ty appropriately and ensure the smooth flow of roads.

<!-- b000278 | heading | pages [15] -->
5.2 The Prediction Models for Evaluation

<!-- b000279 | heading | pages [15] -->
5.2.1 Prediction Model Based On Support Vector Machine(SVM)

<!-- b000280 | prose | pages [15] -->
SVM is a new machine learning algorithm proposed by V.Vapnik et.al. of AT&TBell Lab. This method is used to estimate the relationship between input and out- put of a system according to a given sample, which can be used to forecast the change time of the index.

<!-- b000281 | prose | pages [15] -->
There are many subprograms in SVM. And SVR learning method is adopted to find the mapping function between time and indicator firstly, for this problem is a prediction problem. Similarly, there are multiple SVR methods in machine learning algorithm. Since epsilon-SVR has remarkable performance, it is selected to predict the change of indica- tors. The procedure of our epsilon-SVR is as follows.

<!-- b000282 | prose | pages [15] -->
Firstly, let time set it denote the time of the i th year, then let ix denote the index value  for i th year. SVR is designed to find a function that gives reasonable prediction ’ x =f t i i ix and index value. The error between ix is in an acceptable threshold through SVR algo- '

<!-- b000283 | prose | pages [15] -->
rithm. The function to be determined is as follows:

<!-- b000284 | prose | pages [15] -->
       ' T ix f t w t  In this formula, is a kernel function of the feature vector, w is a weighting vector  x andmeans the bias term. In our method, Radial Basis Function(RBF) is adopted as our kernel, for it has outstanding performances in the vast majority of occasions. Year infor- mation data of two cities is inputted as train data in SVR, while the indicator value is used as train label. Then the SVR system is employed to predictw andin the formula above. The cross-validation will be adopted to validate the effect of our train model.

<!-- b000285 | prose | pages [15] -->
There are many parameters in SVR system, which can affect the performance of the prediction. The cost parameter C, which default value is 1, is used in C-SVC, epsilon- SVR, and nu-SVR. And the gamma parameter g set gamma in kernel function. The RBF kernel is determined as fellows 

<!-- b000286 | furniture | pages [15] -->
2

<!-- b000287 | prose | pages [15, 16] -->
  g u v *   x e Grid search algorithm is adopted to find the best parameters in predict model. After determined the ranges and the steps of the gird search, the best parameters will be tested to find the best combination. In our method, the search ranges are in steps   -8 8 2 2  of 2 for both parameter C and parameter g. In our method, Libsvm[5] is used to realize 0.8 the algorithm of the SVM. The result of grid search is shown in fig.8.

<!-- b000288 | furniture | pages [16] -->
Team # 65123

<!-- b000289 | furniture | pages [16] -->
Page 16 of 23

<!-- b000291 | caption | pages [16] -->
Fig.8. The result of the grid search method on SVM

<!-- b000292 | prose | pages [16] -->
From the fig.8, we can see that the train model has outstanding performance when 2 c   4 3 the parameter and . 2 g

<!-- b000293 | heading | pages [16] -->
5.2.2 Prediction Model Based On Time Series Forecasting

<!-- b000294 | prose | pages [16] -->
Owing to most of data we selected is aged, and future data is unknown. It’s neces- sary to establish a suitable forecasting model. In there, time series forecasting model is selected. It is based on weighted moving average method (WMAM). The function of WMAM can be represented by        ˆ x x x x      t 1 0 t 1 t 1 N 1 t N 1   N 1    1  i s t .  i 0           0 , i 0,1, N 1   0 1 N 1 where i is the weight of statistical data x . t i

<!-- b000295 | heading | pages [16] -->
5.2.3 Combination of Prediction Model(CPM)

<!-- b000296 | prose | pages [16] -->
To combine the advantage of SVM and WMAM in prediction, CPM is adopted to predict the future index value. Let il denote the weighting factor of i th predict model. The value of il can be estimated by solving the following optimization N m m  min J = l l e e , i j it jt    t 1 i 1 j 1 m   s t . . l 1. i  i 1 where J denotes the combining quadratic sum of predict of error, ite denotes the predict error of the i th predict model.

<!-- b000297 | heading | pages [16] -->
5.3 The Evaluation of Our Smart Growth Plan

<!-- b000298 | prose | pages [16] -->
According to our combined prediction model, we can predict the success degree of smart growth the future of the two cities under the current and our plan. The results are shown below.

<!-- b000299 | furniture | pages [17] -->
Team # 65123

<!-- b000300 | furniture | pages [17] -->
Page 17 of 23

<!-- b000301 | caption | pages [17] -->
Fig.9 The evaluation diagram of smart growth plan

<!-- b000302 | prose | pages [17] -->
The values of horizontal axis respect time, and the values of vertical axis respect the degree of smart growth. The yellow solid line is new plan for Pittsburgh. The black solid line is the current plan for Pittsburgh. The yellow dotted line is new plan for Ningguo. The black dotted line is current plan for Ningguo.

<!-- b000303 | prose | pages [17] -->
From fig.9 we can see that our plan is more successful to achieving smart growth in general. Due to the degree of smart growth (SDSG) in Pittsburgh is very high, it is diffi- cult to have a higher rate of increase. Therefore, our plan for Pittsburgh is better than its current plan. But the effect is not so obvious. The effect of our plan in Ningguo is appar- ent. Although the degree of smart growth (SDSG) is not very high, its rate of rise is very fast. This reflects our plan for Ningguo is very effective. In the first few years, Pittsburgh is in rapid growth period. The degree of SGDG increases very rapidly. This is because investment intensity in the first year.

<!-- b000304 | heading | pages [17] -->
6 Task 4

<!-- b000305 | heading | pages [17] -->
6.1 Ranking the Individual Initiatives

<!-- b000306 | prose | pages [17] -->
Owing to many aspects of two cities are needed to be improved and the governments does not have so much money to implement each initiatives. So we must rank the indi- vidual initiatives within our redesigned smart growth plan as the most potential to the least potential. There, we still adopt combined forecasting model to evaluate the success of the individual initiatives for each cities. With this method, forecasting results are ob- tained in fig 10 and fig.11.

<!-- b000307 | caption | pages [17] -->
Fig.10 The evaluation diagram of smart growth plan in Pittsburgh

<!-- b000308 | furniture | pages [18] -->
Team # 65123

<!-- b000309 | furniture | pages [18] -->
Page 18 of 23

<!-- b000310 | caption | pages [18] -->
Fig.11 The evaluation diagram of smart growth plan in Ningguo

<!-- b000311 | prose | pages [18] -->
As we can see from the fig.10 and fig.11, the values of horizontal axis respect time, and the values of vertical axis respect the degree of smart growth (SDSG). Considering every individual initiative alone, the line values respect SDSG of three individual initia- tives. The values of histogram respect difference between every individual initiative and the current plan.

<!-- b000312 | prose | pages [18] -->
We consider every individual initiative alone. If the difference of SDSG of each in- dividual initiative is lager, the better is the plan’s improvement. It means this plan is ef- fective. Fig.10 is the result of ranking the individual initiatives in Pittsburgh. We can find 3-th initiative (improve the land intensive rate) is the most potential. The 2-th initiative (optimize the economic development structure) is the least potential. The 1-th initiative is second potential.

<!-- b000313 | caption | pages [18] -->
Fig.11 is the result of ranking the individual initiatives in Ningguo. The 3-th initia-

<!-- b000314 | prose | pages [18] -->
tive (push on the economic development) is the most potential. The 2-th initiative (strengthen the control of the factory and cultivate environmental awareness of residents.) is the second potential. The 1-th initiative (increase the floor area ratio and Improve space utilization efficiency.) is the third potential. The 4-th initiative (protect vulnerable groups, such as increase child welfare.) is the fourth potential. The 5-th initiative (improve road network density appropriately and ensure the smooth flow of roads.) is the fifth potential.

<!-- b000315 | heading | pages [18] -->
6.2 Comparing the Initiatives of Two Cities

<!-- b000316 | prose | pages [18] -->
Different cities have different surroundings. Therefore not only the plans of Pitts- burgh and Ningguo are different, but also the rankings are not the same. We put the eco- nomic development in the first place in Ningguo. While improving the land intensive rate is the most potential in Pittsburgh. The least potential is also not the same. The least po- tential of Ningguo is improve road network density appropriately and ensure the smooth flow of roads. The least potential of Pittsburgh optimize the economic development struc- ture.

<!-- b000317 | heading | pages [18] -->
7 Task 5

<!-- b000318 | prose | pages [18] -->
Considering that different cities have different urban population growth pattern, dif- ferent population growth models are made for cities like Pittsburgh and Ningguo. Then different measures are made to improve our plan when the population growth rate is in- creasing . The prediction of population growth are shown in fig.12 as follows.

<!-- b000319 | furniture | pages [19] -->
Team # 65123

<!-- b000320 | furniture | pages [19] -->
Page 19 of 23

<!-- b000321 | caption | pages [19] -->
Fig.12. The population growth of two cities

<!-- b000322 | heading | pages [19] -->
7.1 The Adaptable Plan For Pittsburgh

<!-- b000323 | prose | pages [19] -->
Pittsburgh is a city with a smart growth plan. It has a suitable population growth mode. Population growth rate is an essential factor for the smart growth of a city. The function that predict the population growth model can then be presented by   )t P t ( ) P (0)(1 r P t means -t th year population of this city, and r is the rate of popula- ( ) where the tion growth. For Pittsburgh, as the population increase to 50% in 2050, which means the population of Pittsburgh is 450,000.

<!-- b000324 | prose | pages [19] -->
The calculation can be obtained for our scheme, along with the change in the growth rate. By planning the rule adaptively, SDSG can maintain a good growth trend like the

<!-- b000325 | caption | pages [19] -->
fig.13.

<!-- b000326 | prose | pages [19] -->
Considering the method aforementioned, the plan is proposed as follows.

<!-- b000327 | prose | pages [19] -->
 Limit the expansion of cities building. And make Coordination Degree (CD) add a scalar 0.3% on the basis of the original amount  Improve the economic structure, an increase of 1% on the original basis  Strict control of land occupation rate, making the value of an annual rate of 1.2% increase According to the data shown in the graph, we can see that in the next few decades, the impact of population growth on the indicators of Pittsburgh city is not significant. And we assert that our plans are well suited to this type of city like Pittsburgh city.

<!-- b000328 | prose | pages [19] -->
Fig 13. Dynamic change of SDSG in decades with 50% population till 2050 in Pittsburgh City

<!-- b000329 | heading | pages [19] -->
7.2 The Adaptable Plan For Ningguo

<!-- b000330 | prose | pages [19, 20] -->
Ningguo is a city with a large population and a rapid population growth (see in the Fig.8). Considering the fact of Ningguo, a population growth model (PGM) is proposed to meet the problem as below.

<!-- b000331 | furniture | pages [20] -->
Team # 65123

<!-- b000332 | furniture | pages [20] -->
Page 20 of 23

<!-- b000334 | prose | pages [20] -->
1 1   b ln t p t ( ) P 0 Where the b is a parameter who depends on the population of  recent years. And we get it 0.32. So, we can adjust the plan for the next 40 years according to this parameter in order to adapt to the increasing population.

<!-- b000335 | prose | pages [20] -->
Then considering the plan mentioned above. We propose the following strategy.

<!-- b000336 | prose | pages [20] -->
 Increase the intensity of economic control, on the basis of an increase of 1.05%  Improve traffic, increase the density of road network, the TQ index value in- creased by 0.32%  Improve the coordination between the government and enterprises, promote social equity, so that the degree of coordination indicators to some extent, an increase of 0.11% Then 4 decades of Ningguo indicators change figure as shown below, we can see that through make a tendency to improve for some of the guidelines of Ningguo plan, can effectively improve the rapid growth of the population defects. At the same time we can assert that our plan can be well suited to the type of city like Ningguo city with very high rate of population growth .

<!-- b000337 | prose | pages [20] -->
Fig 14. Dynamic change of SDSG in decades with 50% population till 2050 in Ningguo City In conclusion, the growth rate calculated by PGM demonstrates that our plan can ad- just adaptively to satisfied the increasing need of population.

<!-- b000338 | heading | pages [20] -->
8. Sensitivity Analysis

<!-- b000339 | prose | pages [20] -->
In this section, we make the sensitivity analysis about the parameter c and g , which is based on support vector machine(SVM) prediction model. The sensitivity analysis of the SVM is shown as fellows in fig.15.

<!-- b000340 | caption | pages [20] -->
Fig.15 The sensitivity analysis of SVM predict model

<!-- b000341 | furniture | pages [21] -->
Team # 65123

<!-- b000342 | furniture | pages [21] -->
Page 21 of 23

<!-- b000343 | prose | pages [21] -->
In there, MSE denotes the mean square error, which reflects the accuracy of the train mod- log g means the logarithm of the parameter g and log c means the logarithm of the parame- el, 2 2 ter g. As is shown in figure, the accuracy of the train model is changed by c and g.

<!-- b000344 | heading | pages [21] -->
9. Strengths and Weaknesses

<!-- b000345 | heading | pages [21] -->
9.1 Strengths

<!-- b000346 | prose | pages [21] -->
 Adopt objective weighting method (entropy weight method) and the subjective (group decision making method). More effective weights are obtained.

<!-- b000347 | prose | pages [21] -->
 Employing combined prediction model combines the advantages of two prediction models, eliminates shortcomings in a certain extent and improves prediction accuracy.

<!-- b000348 | prose | pages [21] -->
 Using radar diagram reflects advantages and disadvantages of a city in the devel- opment process. The results are displayed more vividly.

<!-- b000349 | heading | pages [21] -->
9.2 Weaknesses

<!-- b000350 | prose | pages [21] -->
 Although we have try our best. Time is finite, and some data are missed. As a re- sult, the missing data can still bring the errors in evaluation.

<!-- b000351 | prose | pages [21] -->
 Some of the parameters are based on common sense because few data are availa- ble.

<!-- b000352 | heading | pages [21] -->
References

<!-- b000353 | references | pages [21] -->
[1] COMAP. (2017). ICM Problems.zip.

<!-- b000354 | references | pages [21] -->
http://www.comap.com/undergraduate/contests/mcm/contests/2017/problems/2017_

<!-- b000355 | references | pages [21] -->
MCM-ICM_Problems.zip

<!-- b000356 | references | pages [21] -->
[2] EPA, “Smart Growth: A Guide to Developing and Implementing Greenhouse Gas Reductions

<!-- b000357 | references | pages [21] -->
Programs.” 2011.

<!-- b000358 | references | pages [21] -->
http://www.sustainablecitiesinstitute.org/Documents/SCI/Report_Guide/Guide_EPA_SmartGrowth

<!-- b000359 | references | pages [21] -->
GHGReduction_2011.pdf

<!-- b000360 | references | pages [21] -->
[3] Wei-Xiang XU, Quan-shou ZHANG. An Algorithm of Meta-Synthesis Based on the Grey The-

<!-- b000361 | references | pages [21] -->
ory and Fuzzy Mathematics [J].Systems engineering theory and practice, 2001,(4): 114-119

<!-- b000362 | references | pages [21] -->
[4] Zhang Lingying. A Fuzzy Evaluation method for Subjective Index Appraisal[J]. Systems Engi-

<!-- b000363 | references | pages [21] -->
neering Theory & Practice.

<!-- b000364 | references | pages [21] -->
[5] Libsvm: the code of SVR from http://www.csie.ntu.edu.tw/~cjlin/libsvm/ for machine learning.

<!-- b000365 | references | pages [21] -->
[6] Chuanglin Fang, Deli Wang.The Comprehensive Measurement and Promotion Path of Urbani-

<!-- b000366 | references | pages [21] -->
zation Development Quality in China[J].Institute of Geographic Sciences and Natural Resources

<!-- b000367 | references | pages [21] -->
Research, Chinese Academy of Sciences. Geographical Research.2011.11:1931-1946.

<!-- b000368 | references | pages [21] -->
[7] Altas, Nur Esin., & Ozsoy, A. (1998). Spatial Adaptability and Flexibility as Parameters of User

<!-- b000369 | references | pages [21] -->
Satisfaction for Quality Housing. Building and Environment, 33, 315-323.

<!-- b000370 | references | pages [21] -->
[8] Angelidou, Margarita . (2014). Smart city policies: A spatial approach. Cities, 41, S3–S11.

<!-- b000371 | references | pages [21] -->
[9] Belanche, Daniel., Casaló, Luis V., & Orús, Carlos .(2016). City attachment and use of urban

<!-- b000372 | references | pages [21] -->
services: Benefits for smart cities. Cities, 50, 75–81.

<!-- b000373 | references | pages [21] -->
[10]Budde.P.,  Rassia,  S.Th.,  &  Pardalos.,  P.M.  (eds.).  (2014).  Cities  for  Smart  Environmen-

<!-- b000374 | references | pages [21] -->
tal  and  Energy  Futures.  Energy  Systems.  Heildeberg: Springer

<!-- b000375 | references | pages [21] -->
[11] Heng, Chye Kiang., & Malone-Lee, L.C. (2010) Density and Urban Sustainability: An Explo-

<!-- b000376 | references | pages [21] -->
ration of Critical Issues. In Ng, Edward. Designing High-Density Cities for Social and Environmen-

<!-- b000377 | references | pages [21] -->
tal Sustainability (pp.41-52). UK and USA: Earthscan.

<!-- b000378 | furniture | pages [22] -->
Team # 65123

<!-- b000379 | furniture | pages [22] -->
Page 22 of 23

<!-- b000380 | references | pages [22] -->
[12] Smith, Carl., Clayden, A., & Dunnet, N. (2008). Residential Landscape Sustainability. Oxford

<!-- b000381 | references | pages [22] -->
UK: Blackwell Publishing.

<!-- b000382 | references | pages [22] -->
[13] Song, Yan.(2005). Smart Growth and Urban Development Pattern: A Comparative Study. In-

<!-- b000383 | references | pages [22] -->
ternational Regional Science Review, 28, 239.

<!-- b000384 | references | pages [22] -->
[14] Spreiregen, Paul D, 1965, Urban Design: The Architecture of Towns and Cities, Mc-Graw,Hill,

<!-- b000385 | references | pages [22] -->
New York.

<!-- b000386 | references | pages [22] -->
[15] Thomas, Randall, 2003, Sustainable Urban Design- an Environmental Approach, Spon

<!-- b000387 | references | pages [22] -->
Press,New York

<!-- b000388 | references | pages [22] -->
[16] Turner, Matthew A.,(2007). A simple theory of smart growth and sprawl. Journal of Urban

<!-- b000389 | references | pages [22] -->
Economics, 61, 21–44.

<!-- b000390 | references | pages [22] -->
[17] Udy, John, 2004, Man Makes the City, Urban Development and Planning, Trafford Publishing,

<!-- b000391 | references | pages [22] -->
Canada.

<!-- b000392 | references | pages [22] -->
[18] Zahnd, Markus, 1999, Perancangan Kota Secara Terpadu, Penerbit Kanisius, Yogyakarta.

<!-- b000393 | references | pages [22] -->
[19] Hodgkinson, Steve. (2011). Is Your City Smart Enough?. Reference Code: OI00130-007.,

<!-- b000394 | references | pages [22] -->
Ovum.

<!-- b000395 | references | pages [22] -->
[20] Johnson, Matthew, 1993, Housing Culture, Traditional Architecture in an English Landscape,

<!-- b000396 | references | pages [22] -->
UCL Press, London

<!-- b000397 | references | pages [22] -->
[21] Jucevicius, Robertas., Patašiene, I., & Patašius, M. (2014).Digital dimension of smart city:

<!-- b000398 | references | pages [22] -->
critical analysis. Procedia - Social and Behavioral Sciences, 156, 146–150.

<!-- b000399 | references | pages [22] -->
[22] Kostof, Spiro. (1991). The City Shaped, Urban Patterns and Meanings Through Histo-

<!-- b000400 | references | pages [22] -->
ry.London: Thames and Hudson.

<!-- b000401 | references | pages [22] -->
[23] Lawson, Bryan. (2010). The Social and Psychological Issues of High-Density City Space. In

<!-- b000402 | references | pages [22] -->
Ng, Edward.Designing High-Density Cities for Social and Environmental Sustainability (pp.282-

<!-- b000403 | references | pages [22] -->
292). UK and USA: Earthscan.

<!-- b000404 | heading | pages [22] -->
Appendix

<!-- b000405 | prose | pages [22] -->
The code of the grid search in SVM

<!-- b000406 | prose | pages [22] -->
gridsearch.m function[mse,bestc,bestg]=gridsearch(train_label,train,cmin,cmax,gmin,gmax,v,cstep,gstep,msestep)

<!-- b000407 | prose | pages [22] -->
%% about the parameters of SVM

<!-- b000408 | prose | pages [22] -->
if nargin < 10

<!-- b000409 | prose | pages [22] -->
msestep = 0.06;

<!-- b000410 | prose | pages [22] -->
end

<!-- b000411 | prose | pages [22] -->
if nargin < 8

<!-- b000412 | prose | pages [22] -->
cstep = 0.8;gstep = 0.8;

<!-- b000413 | prose | pages [22] -->
end

<!-- b000414 | prose | pages [22] -->
if nargin < 7

<!-- b000415 | prose | pages [22] -->
v = 5;

<!-- b000416 | prose | pages [22] -->
end

<!-- b000417 | prose | pages [22] -->
if nargin < 5

<!-- b000418 | prose | pages [22] -->
gmax = 8;gmin = -8;

<!-- b000419 | furniture | pages [23] -->
Team # 65123

<!-- b000420 | furniture | pages [23] -->
Page 23 of 23

<!-- b000421 | prose | pages [23] -->
end

<!-- b000422 | prose | pages [23] -->
if nargin < 3

<!-- b000423 | prose | pages [23] -->
cmax = 8;cmin = -8;

<!-- b000424 | prose | pages [23] -->
end

<!-- b000425 | prose | pages [23] -->
%% X:c Y:g cg:acc

<!-- b000426 | prose | pages [23] -->
[X,Y] = meshgrid(cmin:cstep:cmax,gmin:gstep:gmax);

<!-- b000427 | prose | pages [23] -->
[m,n] = size(X);cg = zeros(m,n);eps = 10^(-4);

<!-- b000428 | prose | pages [23] -->
%% record acc with different c & g,and find the bestacc with the smallest c

<!-- b000429 | prose | pages [23] -->
bestc = 0;bestg = 0;mse = Inf;basenum = 2;

<!-- b000430 | prose | pages [23] -->
h=waitbar(0,'please wait...');

<!-- b000431 | prose | pages [23] -->
for i = 1:m

<!-- b000432 | prose | pages [23] -->
for j = 1:n

<!-- b000433 | prose | pages [23] -->
cmd = ['-v ',num2str(v),' -c ',num2str( basenum^X(i,j) ),' -g ',num2str( basenum^Y(i,j) ),' -s 3 -p 0.01'];

<!-- b000434 | prose | pages [23] -->
cg(i,j) = svmtrain(train_label, train, cmd);

<!-- b000435 | prose | pages [23] -->
if cg(i,j) < mse

<!-- b000436 | prose | pages [23] -->
mse = cg(i,j);bestc = basenum^X(i,j);bestg = basenum^Y(i,j);

<!-- b000437 | prose | pages [23] -->
end

<!-- b000438 | prose | pages [23] -->
if abs( cg(i,j)-mse )<=eps && bestc > basenum^X(i,j)

<!-- b000439 | prose | pages [23] -->
mse = cg(i,j);bestc = basenum^X(i,j);bestg = basenum^Y(i,j);

<!-- b000440 | prose | pages [23] -->
end

<!-- b000441 | prose | pages [23] -->
waitbar(((i-1)*m+j)/(m*n));

<!-- b000442 | prose | pages [23] -->
end

<!-- b000443 | prose | pages [23] -->
end
