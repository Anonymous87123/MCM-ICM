# P-E-2018-73119-79c4dde3

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For office use only For office use only

<!-- b000004 | furniture | pages [1] -->
73119

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
T2

<!-- b000007 | prose | pages [1] -->
F1

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
Problem Chosen T3

<!-- b000010 | title | pages [1] -->
E

<!-- b000011 | prose | pages [1] -->
T4

<!-- b000012 | prose | pages [1] -->
F3

<!-- b000013 | prose | pages [1] -->
F4

<!-- b000014 | title | pages [1] -->
2018

<!-- b000015 | prose | pages [1] -->
MCM/ICM

<!-- b000016 | heading | pages [1] -->
Summary Sheet

<!-- b000017 | prose | pages [1] -->
In the past two decades, regional instability caused by some fragile state(s) has become more and more concerned by the whole world. Among the various factors, climate changes usually lead to high frequency of extreme weather events, which significantly exacerbate the fragility of a certain state. How to mitigate the impact of climate changes and prevent a state from becoming a fragile one has been widely recognized as a very important and urgent issue.

<!-- b000018 | prose | pages [1] -->
As a response, in order to predict a state’s fragility accurately, we develop a

<!-- b000019 | heading | pages [1] -->
nov-el model called PSA (Pressure Sensitivity Adaptability), which is significantly

<!-- b000020 | prose | pages [1] -->
PSR ex-tended from the well-known (Pressure State Response) model. Specifically, our model contains three dimensions whose weights are obtained by combining AHP (Analytic Hierarchy Process) and EWM (Entropy Weight Method). Notice that FI (Fragile Index) is a weighted sum of the three dimensions denoting the fragility of a certain state. In our empirical studies, we verify the effectiveness of our model via the ground truth of the public fragile state index. Meanwhile, we use a regression analysis method to get functional relationship between non- climatic indicators and climatic indicators. We choose DRC (Democratic Republic of the Congo) and BD (Bangladesh) in our case studies. Specifically, we use the values of the indicators of a decade as the input data fed to our model, and obtain the FI curve. For DRC, the FI curve without the effect of climate changes is modeled by keep the values of the corresponding climate indicators constant. For BD, we use GM (1,1) to draw the prediction curve of FI and find that the time that BD is likely to become a stable state is around 2076.

<!-- b000021 | prose | pages [1] -->
Furthermore, we study six major intervention policies of BD for climate changes. We find that natural disasters in BD are serious and suggest investing more fiscal expenditure in intervention2 (intervention2: Comprehensive Disaster Managemen-t). It is estimated that this expenditure will increase by 35% every 5 years. We can then get other policies’ fiscal expenditures through GM (1, 1), and finally get the total expenditure in 5 years, 10 years and even 20 years.

<!-- b000022 | prose | pages [1] -->
We select Asia, Europe and Africa so as to study the portability of our proposed model. For continents, the fragile indexes of several representative countries are selected and averaged in order to estimate the continent fragile index. The result-s are very promising, which clearly showcases the effectiveness of our model on continents.

<!-- b000023 | prose | pages [1] -->
Finally, we conduct a sensitivity analysis in order to gain some deep under- standing of our model, and conclude the report via discussing the strengths and weaknesses of our proposed model.

<!-- b000024 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000025 | keywords | pages [2] -->
Keywords: Fragile State, Climate Change, PSA, GM (1,1)

<!-- b000026 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000027 | furniture | pages [3] -->
Team # 73119

<!-- b000028 | furniture | pages [3] -->
Page 1 of 22

<!-- b000029 | heading | pages [3] -->
Contents

<!-- b000030 | heading | pages [3] -->
1 Introduction

<!-- b000031 | prose | pages [3] -->
2 1.1 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | prose | pages [3] -->
2 1.2 Restatement of Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | prose | pages [3] -->
2 1.3 Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | heading | pages [3] -->
2 Assumptions and Symbol Table

<!-- b000035 | prose | pages [3] -->
3

<!-- b000036 | prose | pages [3] -->
3 Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 3 Symbol Table . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000037 | prose | pages [3] -->
3

<!-- b000038 | heading | pages [3] -->
Model PSA

<!-- b000039 | prose | pages [3] -->
4

<!-- b000040 | prose | pages [3] -->
4 PSR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4 PSA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 4 Identify indicators . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1 5 Data Pre-processing . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.2 6 Data Normalization . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.3 6 Calculate weight by AHP . . . . . . . . . . . . . . . . . . . . . . . 3.2.4 7 Calculate weight by EWM . . . . . . . . . . . . . . . . . . . . . . . 3.2.5 7 Weighted average . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.6 8 Analyze direct and indirect impacts of climate change . . . . . . . . . . . 3.3 8 Test PSA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4

<!-- b000041 | prose | pages [3] -->
4 Case Study

<!-- b000042 | prose | pages [3] -->
10

<!-- b000043 | prose | pages [3] -->
12 Study 1: Democratic Republic Of the Congo . . . . . . . . . . . . . . . . . 4.1 12 4.1.1 Climate change effects of Congo . . . . . . . . . . . . . . . . . . .

<!-- b000044 | prose | pages [3] -->
12 4.1.2 The FI without climate change effects . . . . . . . . . . . . . . . .

<!-- b000045 | prose | pages [3] -->
12 Study 2: People’s Republic of Bangladesh . . . . . . . . . . . . . . . . . . 4.2 13 Climate change effects of Bangladesh . . . . . . . . . . . . . . . . 4.2.1 13 Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 15 Effect of Human Intervention . . . . . . . . . . . . . . . . . . . . . 4.2.3 15 Total cost . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.4

<!-- b000046 | prose | pages [3] -->
5 Further Exploration

<!-- b000047 | prose | pages [3] -->
6

<!-- b000048 | heading | pages [3] -->
Sensitivity Analysis

<!-- b000049 | prose | pages [3] -->
7

<!-- b000050 | heading | pages [3] -->
Strengths and Weaknesses

<!-- b000051 | prose | pages [3] -->
16

<!-- b000052 | prose | pages [3] -->
17

<!-- b000053 | prose | pages [3] -->
17

<!-- b000054 | prose | pages [3] -->
18 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 18 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2

<!-- b000055 | prose | pages [3] -->
8

<!-- b000056 | heading | pages [3] -->
Conclusions

<!-- b000057 | heading | pages [3] -->
Appendices

<!-- b000058 | heading | pages [3] -->
Appendix A FI of Country

<!-- b000059 | prose | pages [3] -->
19

<!-- b000060 | prose | pages [3] -->
19

<!-- b000061 | prose | pages [3] -->
21

<!-- b000062 | prose | pages [3] -->
21

<!-- b000063 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000064 | heading | pages [4] -->
Appendix B Climate expenditure of Bangladesh

<!-- b000065 | furniture | pages [4] -->
22

<!-- b000066 | furniture | pages [4] -->
Team # 73119

<!-- b000067 | furniture | pages [4] -->
Page 2 of 22

<!-- b000068 | heading | pages [4] -->
Introduction

<!-- b000069 | prose | pages [4] -->
1

<!-- b000070 | prose | pages [4] -->
1.1

<!-- b000071 | heading | pages [4] -->
Background

<!-- b000072 | prose | pages [4] -->
In the past 20 years, there have been local wars and conflicts in the world and the fragile states have been a threat to the world security. Therefore, fragile states become a major issue for the world’s development. OECD (Organization for Economic Co-operation and Development) defines "States are fragile when state structures lack political will and/or capacity to provide the basic functions needed for poverty reduction, develop-ment and to safeguard the security and human rights of their populations."[1] Many universities and research institutes start to research centers to specialize in problems of fragile states. To measure fragility of a state, many evaluation indexes have been put forward, such as World Bank’s Country Policy and Institutional Assessment (CPIA) [2], Carton University’s Country Indicators for Foreign Policy Fragility Index (CIFP)[3]and The Fund for Peace’s Fragile States Index (FSI)[4]. Nowadays, due to the rapid devel-opment of industries and the rapid increase of population, large amount of energy consumption and greenhouse gases emission like carbon dioxide cause global warm-ing, then the frequent extreme weather and even the more extreme phenomena like a colder winter and a hotter summer. The climate change leads to more frequent and more serious drought, flood, storm, coldness and hotness, and leads to decline of wa-ter, food and energy[5], and then even leads to the wide spread of famine and diseases. If the government is unable to solve the problem of famine and diseases for people, there will be local violent conflicts. If the foreign government interferes in internal af-fairs, there will be wars and regional instability. Without effective measures to solve these problems, there will be disasters which bring threats to the world’s peace and de-velopment. Hence, reducing the fragility of a state has its unprecedented significance in today’s world.

<!-- b000073 | prose | pages [4] -->
1.2 Restatement of Problems

<!-- b000074 | prose | pages [4] -->
To create a more stable world, fragile state should be studied first and the following tasks are to be accomplished:

<!-- b000075 | prose | pages [4] -->
An evaluation index system to evaluate a state’s fragility and measure the influ- ences of climate change on fragility is needed. By considering various factors like economy, society, politics and local climate, the model should clearly extin- guish the state is fragile, vulnerable or stable. Meanwhile the model can identify how climate change increases fragility through direct means or indirectly as it influences other indicators. (Refer to Task1)

<!-- b000076 | prose | pages [4] -->
The influence of climate change on state should be evaluated, which help find out some definitive indicators. (Refer to Task2 and Task 3)

<!-- b000077 | prose | pages [4] -->
The risks of current national policies about reducing climate change, the effect of protecting the state from being fragile as well as the total cost should be evaluat-ed. (Refer to Task4)

<!-- b000078 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000079 | prose | pages [5] -->
Adjust the model and make it adaptable to cities and continents.(Refer to Task5)

<!-- b000080 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000081 | furniture | pages [6] -->
Team # 73119

<!-- b000082 | furniture | pages [6] -->
Page 3 of 22

<!-- b000083 | heading | pages [6] -->
1.3 Our Work

<!-- b000084 | prose | pages [6] -->
First we build our basic model PSA(Pressure Sensitivity Adaptability) based on PSR Model. Then we utilize its FI(Fragility Index)to measure a state’s fragility. Afterwards, we compare the result with the FSI’s ranking and discover that our model is rational. Moreover, we show the relations between indexes through regression analysis.

<!-- b000085 | prose | pages [6] -->
We choose Democratic Republic of the Congo in our case study, and analyze how cli-mate change influences its fragility in details. By adjusting the model appropriately, we simulate the state without fragility. Next we analyze Bangladesh through several aspects: fragility, influences of climate change on fragility and related indicators. Ac- cording to range in task 1, we define a tipping point 0.6 and forecast the time taken for Bangladesh’s fragility to reach that point using GM (1, 1).

<!-- b000086 | prose | pages [6] -->
In task 4, we continue to discuss about Bangladesh further. We collect Bangladesh policies about climate change and fiscal expenditure data in recent years. Through analysis of the data and events about climate change, we can show the influences of these human interventions on this state’s fragility. Finally, the fiscal expenditure in 5 years will be estimated based on the current one.

<!-- b000087 | prose | pages [6] -->
Then we expend the PSA and analyze other regions. After respective analysis on c- ities and continents, we find that our model is portable.

<!-- b000088 | prose | pages [6] -->
Finally we do sensitivity analysis on related parameters of our model, and discuss strengths and weaknesses.

<!-- b000089 | heading | pages [6] -->
Assumptions and Symbol Table

<!-- b000090 | prose | pages [6] -->
2

<!-- b000091 | prose | pages [6] -->
2.1

<!-- b000092 | heading | pages [6] -->
Assumptions

<!-- b000093 | prose | pages [6] -->
We assume the countries we studied are regular.

<!-- b000094 | prose | pages [6] -->
Almost every country’ development conforms to certain regular patterns, which is based on facts.

<!-- b000095 | prose | pages [6] -->
We assume the countries we studied are stable.

<!-- b000096 | prose | pages [6] -->
Though countries’ political stabilities are different, we focus more on climate change. Thus, this assumption is reasonable and helps avoid unnecessary trou-bles when building the model.

<!-- b000097 | prose | pages [6] -->
We assume that indicators except those we have studied have few influences on the system. In the model, we consider several crucial indicators. However, there are large numbers of indicators. Thus, we assume that other indicators except those men-tioned above are uninfluential.

<!-- b000098 | prose | pages [6] -->
We assume that the statistics we captured from websites are precise and reli-able.

<!-- b000099 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000100 | furniture | pages [7] -->
Team # 73119

<!-- b000101 | furniture | pages [7] -->
Page 4 of 22

<!-- b000102 | prose | pages [7] -->
The statistics we collected are from different websites which are authoritative. Therefore, this assumption is reasonable.

<!-- b000103 | prose | pages [7] -->
2.2 Symbol Table

<!-- b000104 | prose | pages [7] -->
Symbol that we use in the model are shown in the following table :

<!-- b000105 | caption | pages [7] -->
Table 1: Symbol table

<!-- b000106 | prose | pages [7] -->
Symbol Description

<!-- b000107 | prose | pages [7] -->
Fragile Index FI P S A Pressure Sensitivity Adaptability Democratic Republic of the Congo DRC BD xi Bangladesh The i-th indicator

<!-- b000108 | prose | pages [7] -->
Note:Pi means the i-th indicator, e.g.temperature anomalies is the first indicator. Hence, it can be denoted as x1.

<!-- b000109 | heading | pages [7] -->
Model PSA

<!-- b000110 | prose | pages [7] -->
3

<!-- b000111 | prose | pages [7] -->
According to previous work, we are going to build our model base on the PSR model.

<!-- b000112 | prose | pages [7] -->
3.1 PSR

<!-- b000113 | prose | pages [7] -->
Currently the PSR model (Pressure S- tate Response) are frequently applied among research on fragility.

<!-- b000114 | prose | pages [7] -->
In P- SR, ‘P’ represents the pressure dimen- sion, which indicates the pressure that are brought to the system. Here, we suppose that climate change and hu- man activites are the ‘pressure’. More- over, ‘S’ represents the state dimen- sion, which shows the states that are influenced by the pressure. ‘R’ repre- sents the Response dimension, which reflects the response of the system.

<!-- b000115 | prose | pages [7] -->
3.2 PSA

<!-- b000116 | caption | pages [7] -->
Figure 1: PSR Model

<!-- b000117 | prose | pages [7] -->
We will do the following steps to build our PSA model.

<!-- b000118 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000119 | furniture | pages [8] -->
Team # 73119

<!-- b000120 | furniture | pages [8] -->
Page 5 of 22

<!-- b000121 | heading | pages [8] -->
3.2.1 Identify indicators

<!-- b000122 | prose | pages [8] -->
After carefully analyzing the relevant information, we determine the indicators shown in the figure below:

<!-- b000123 | caption | pages [8] -->
Figure 2: Indicators

<!-- b000124 | prose | pages [8] -->
In line with the characteristics of PSR, we first divide fragility into three aspect-s:

<!-- b000125 | heading | pages [8] -->
Pressure, Sensitivity, Adaptation. Then as for Pressure, we assume that there are

<!-- b000126 | prose | pages [8] -->
pressure from the climate and the one from human activities. As for Sensitivity, we determine indicators according to Xu’s work[16]. Finally, we choose indicators for Adaptation referring to Fragile State Index(FSI).

<!-- b000127 | prose | pages [8] -->
Pressure

<!-- b000128 | prose | pages [8] -->
– Temperature departure value: it reflects the difference between the

<!-- b000129 | prose | pages [8] -->
temper-ature this year and the usual average temperature.

<!-- b000130 | prose | pages [8] -->
– Average altitude: the higher the average altitude is, the less influences by

<!-- b000131 | prose | pages [8] -->
rise of sea level.

<!-- b000132 | prose | pages [8] -->
– Natural disaster risk index: it is to measure the degree of being

<!-- b000133 | prose | pages [8] -->
endangered of a state confronted earthquake, rainstorm, flood, drought and other natu-ral disasters. (Refer to Wikipedia’s natural disaster risk index: as a result of vulnerability and natural hazards such as earthquakes, volcanic eruptions, storms, floods, droughts and sea level)

<!-- b000134 | prose | pages [8] -->
– Population density: the higher the population density, the heavier the bur-

<!-- b000135 | prose | pages [8] -->
den to different kinds of national resources like water, food and energy, and to national public infrastructures.

<!-- b000136 | prose | pages [8] -->
– CO2 emissions: it reflects the pollution. The larger it is, the more serious

<!-- b000137 | prose | pages [8] -->
the pollution and the more powerful the pressure to environment.

<!-- b000138 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000139 | furniture | pages [9] -->
Team # 73119

<!-- b000140 | furniture | pages [9] -->
Page 6 of 22

<!-- b000141 | prose | pages [9] -->
– Energy consumption per capita: it indirectly reflects the abundance of a

<!-- b000142 | prose | pages [9] -->
state’s energy.

<!-- b000143 | heading | pages [9] -->
Sensitivity

<!-- b000144 | prose | pages [9] -->
– Forest cover rate: the larger the forest cover rate is, the less sensitive to

<!-- b000145 | prose | pages [9] -->
climate change.

<!-- b000146 | prose | pages [9] -->
– Crop production index: the more the food production and store, and

<!-- b000147 | prose | pages [9] -->
people will not starve, and in some way avoid unrests, the less sensitive to deal with foreign interference and domestic conflicts.

<!-- b000148 | prose | pages [9] -->
– Percentage of people using basic drinking water services: many

<!-- b000149 | prose | pages [9] -->
conflicts in the world result from water shortage.

<!-- b000150 | prose | pages [9] -->
– Health index: the healthier the people are, the less the diseases are, the

<!-- b000151 | prose | pages [9] -->
less sensitive to influences of climate change.

<!-- b000152 | prose | pages [9] -->
– GDP unit energy consumption: it reflects the economic efficiency of a

<!-- b000153 | prose | pages [9] -->
state. The higher the efficiency is, the more prosperous the economy is.

<!-- b000154 | prose | pages [9] -->
Adaptability

<!-- b000155 | prose | pages [9] -->
– GDP per capita: economy can reflect the degree of prosperity of a state e-

<!-- b000156 | prose | pages [9] -->
prosperous conomy.

<!-- b000157 | prose | pages [9] -->
The more the economy is, the better the infrastructure is, the stronger the ability to deal with climate change is.

<!-- b000158 | prose | pages [9] -->
– Gini coefficient: Gini coefficient reflects the status of a state’s gap

<!-- b000159 | prose | pages [9] -->
between the rich and the poor. The larger the gap is, the greater the conflicts, the weaker the ability to adapt to the external threats.

<!-- b000160 | prose | pages [9] -->
– Public service: it means public financing and community service, and the

<!-- b000161 | prose | pages [9] -->
basic guarantee to public health. The better the public welfare is, the better the adaptability is.

<!-- b000162 | prose | pages [9] -->
– Democracy index: being undemocratic will leads to social unrest and re-

<!-- b000163 | prose | pages [9] -->
gional instability.

<!-- b000164 | prose | pages [9] -->
– Human right: Guarantee the human right and make humans’ basic right

<!-- b000165 | prose | pages [9] -->
guaranteed to make people happier and society more stable.

<!-- b000166 | heading | pages [9] -->
3.2.2 Data Pre-processing

<!-- b000167 | prose | pages [9] -->
We searched some websites like WorldBank,The Economist and Fragile State Index and find 16 indicators of 20 countries firstly. Some statistics of indicators are missing for not all statistics can be searched on Internet. We utilize SPSS’s multiple imputation to fill the missing values to ensure smooth data processing and analysis.

<!-- b000168 | heading | pages [9] -->
3.2.3 Data Normalization

<!-- b000169 | prose | pages [9] -->
While analyzing all the indicators, we find that they can be divided into three types. Symbol ‘+’ means that for the indicator, bigger is better. Similarly, symbol ‘-’ means smaller is better and symbol ‘*’ means that the value is better when it is closer to the specific value.

<!-- b000170 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000171 | furniture | pages [10] -->
Team # 73119

<!-- b000172 | furniture | pages [10] -->
Page 7 of 22

<!-- b000173 | prose | pages [10] -->
Therefore, for those bigger is better, the equation should be

<!-- b000174 | prose | pages [10] -->
ri =

<!-- b000175 | prose | pages [10] -->
ir

<!-- b000176 | prose | pages [10] -->
r r

<!-- b000177 | prose | pages [10] -->
min (1) r r

<!-- b000178 | prose | pages [10] -->
maxr

<!-- b000179 | prose | pages [10] -->
min As for the smaller is better, the equation should be

<!-- b000180 | prose | pages [10] -->
ri =

<!-- b000181 | prose | pages [10] -->
maxr

<!-- b000182 | prose | pages [10] -->
r r

<!-- b000183 | prose | pages [10] -->
i (2)

<!-- b000184 | prose | pages [10] -->
maxr

<!-- b000185 | prose | pages [10] -->
r r

<!-- b000186 | prose | pages [10] -->
min As for the special type, such as the temperature anomalies here, we define the equation as follow:

<!-- b000187 | prose | pages [10] -->
(3)

<!-- b000188 | prose | pages [10] -->
where jtaj means the original absolute value of temperature anomalies, and jtajmax means the maximum absolute value.

<!-- b000189 | heading | pages [10] -->
3.2.4 Calculate weight by AHP

<!-- b000190 | prose | pages [10] -->
To calculate weights of indicators of PSA, we intend to use AHP. Firstly, we define the expressions as follow:

<!-- b000191 | prose | pages [10] -->
F I = !1P + !2S + !3A (4) n n Xi Xi

<!-- b000192 | prose | pages [10] -->
P =iPi (5)

<!-- b000193 | prose | pages [10] -->
=1 where n means the number of indicators and Pi represents the indicators of Pressure.

<!-- b000194 | prose | pages [10] -->
Similarly, we have

<!-- b000195 | prose | pages [10] -->
where Si and Ai represents indicators of Sensitivity and Adaptability respectively.

<!-- b000196 | prose | pages [10] -->
Afterwards, we construct the score matrices and calculate the weight of each indicator.

<!-- b000197 | heading | pages [10] -->
3.2.5 Calculate weight by EWM

<!-- b000198 | prose | pages [10] -->
As we all know, AHP has some subjectivity due to the score matrices. Hence, we cal- culate the weights using Entropy Weight Method(EWM)[15]

<!-- b000199 | prose | pages [10] -->
Firstly, we calculate the proportion of the jth indicator of the ith country.

<!-- b000200 | prose | pages [10] -->
rij

<!-- b000201 | prose | pages [10] -->
pij = Pm (8) i=1r

<!-- b000202 | prose | pages [10] -->
ij

<!-- b000203 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000204 | prose | pages [11] -->
where rij means the value of the corresponding indicator, and m represents the number of the countries.

<!-- b000205 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000206 | furniture | pages [12] -->
Team # 73119

<!-- b000207 | furniture | pages [12] -->
Page 8 of 22

<!-- b000208 | prose | pages [12] -->
Then we get the entropy value of the jth indicator:

<!-- b000209 | prose | pages [12] -->
m

<!-- b000210 | prose | pages [12] -->
Ej = k (pij

<!-- b000211 | prose | pages [12] -->
where k = ln m Finally, we get the weight of the jth indicator:

<!-- b000212 | prose | pages [12] -->
Xi Xi

<!-- b000213 | prose | pages [12] -->
ln pij ) (9) =1 =1

<!-- b000214 | prose | pages [12] -->
Since we want to reduce the subjectivity of AHP, which can be supplemented by EWM, we get the final weight by calculating the weighted average of the results calculated above.

<!-- b000215 | prose | pages [12] -->
We define the equation as follows,

<!-- b000216 | prose | pages [12] -->
W

<!-- b000217 | prose | pages [12] -->
i=

<!-- b000218 | prose | pages [12] -->
1W ai+

<!-- b000219 | prose | pages [12] -->
2W (11) ei where Wai represents the weight of the ith indicator calculated by AHP and Wei repre- sents the one calculated be EWM. Here we suppose 1 = 0:8 and 2 = 0:2

<!-- b000220 | prose | pages [12] -->
Finally we get the weights of all the indicators.

<!-- b000221 | prose | pages [12] -->
3.3 Analyze direct and indirect impacts of climate change

<!-- b000222 | prose | pages [12] -->
In task 1, we are required to identify how climate change increases fragility directly and indirectly.

<!-- b000223 | caption | pages [12] -->
Figure 3: Relationship between indicators

<!-- b000224 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000225 | furniture | pages [13] -->
Team # 73119

<!-- b000226 | furniture | pages [13] -->
Page 9 of 22

<!-- b000227 | prose | pages [13] -->
Through regression analysis, we can give a more specific relationship among the indicators.Some examples are listed in Table 2:

<!-- b000228 | prose | pages [13] -->
Climate Indicators

<!-- b000229 | prose | pages [13] -->
Temperature t

<!-- b000230 | prose | pages [13] -->
Relationship

<!-- b000231 | prose | pages [13] -->
W ater = 1:099 t + 42:15

<!-- b000232 | prose | pages [13] -->
Crop P roduction = 3:551 t + 114

<!-- b000233 | prose | pages [13] -->
Elevation e

<!-- b000234 | prose | pages [13] -->
Human Right = 30:25 e 17:29 Democracy Rate = 20:12 e + 19:97

<!-- b000235 | caption | pages [13] -->
Table 2: Examples of Relationship

<!-- b000236 | prose | pages [13] -->
Through direct means

<!-- b000237 | prose | pages [13] -->
– Temperature anomalies: the characteristic of significant climate change is

<!-- b000238 | prose | pages [13] -->
influences of temperature. Temperature of current year is different from usual like the rise or drop of temperature. The most direct influence index is to increase the absolute value of temperature anomalies, which directly makes a state more fragile.

<!-- b000239 | prose | pages [13] -->
– Average elevation: the global warming causes the sea level rise. For

<!-- b000240 | prose | pages [13] -->
some low-lying countries, they will be confronted with being submerged, which directly makes a state more fragile.

<!-- b000241 | prose | pages [13] -->
– Natural disaster risk index: climate change is likely to bring hot weather

<!-- b000242 | prose | pages [13] -->
and then the hurricane, rainstorm, flood, drought and other natural disas- ters.

<!-- b000243 | prose | pages [13] -->
Through indirect means

<!-- b000244 | prose | pages [13] -->
– Forest cover rate: climate change probably causes rainstorm and

<!-- b000245 | prose | pages [13] -->
mountain torrents which erode soil and destroy the forests and villages, and probably causes drought which makes trees wither. Therefore, it indirectly causes the decrease of forest cover rate.

<!-- b000246 | prose | pages [13] -->
– Crop production index: climate change is likely to cause more intense

<!-- b000247 | prose | pages [13] -->
rain-fall, longer dry periods or increased temperature. More intense rainfall will result in crop stopping growing due to water shortage and decline of pro-duction. The increased temperature will result in reduction of output for some crops’ inadaptability, insects calamity or some viral pathogens which will infect crops and livestock and then cause death in batches. What’s worse, there will be no harvest at all. The increased temperature will also fishery. in-fluence the output of The increased temperature helps phycophyta grow up rapidly, then dissolved oxygen declines, and the nutrition neces-sary for fish upwells, which is bad for survival of fish. Finally the output of fish declines.

<!-- b000248 | prose | pages [13] -->
– Percentage of people using basic drinking water service: increased tem-

<!-- b000249 | prose | pages [13] -->
perature will lead to more evaporation of the open shallow groundwater

<!-- b000250 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000251 | furniture | pages [14] -->
Team # 73119

<!-- b000252 | furniture | pages [14] -->
Page 10 of 22

<!-- b000253 | prose | pages [14] -->
sources. Flood and rainstorm will cause death of livestock, breeding of bac-teria, water infection of virus, then water pollution, degradation of water quality, and reduction of clear drinking water.

<!-- b000254 | prose | pages [14] -->
– Health Index:

<!-- b000255 | prose | pages [14] -->
1. Climate change influences the supply of food nutrition. Some research reports show that, global warming and increasing concentration of carbon dioxide will cause the decrease of protein synthetized by crops. Higher car- bon dioxide concentrations will drain the protein contents of barely(14.6 per- cent), rice(7.6 percent), wheat(7.8 percent), and potatoes(6.4 percent).[6] oth-er key nutrition like zinc and iron are threated for the same reasons. This is more serious than the influence on human health of lack of protein.

<!-- b000256 | prose | pages [14] -->
2. Climate change will make diseases spread more easily and as a result, people are easier to get sick. Climate change induces some new infectious diseases, such as HIV, SARS and Ebola disease.[7]Rainstorm and flood create a humid and warm environment which is suitable for breeding for mosquitoes pathogens, which causes the wide spread of infectious diseases. Through touching or drink the polluted water, people will suffer from water- borne diseases like diarrhea and so on, which greatly undermines human health.

<!-- b000257 | prose | pages [14] -->
– GDP per capita: for tropical countries, increased temperature will reduce

<!-- b000258 | prose | pages [14] -->
workers’ productivity. In contrary, for northern countries in cold areas, in- creased temperature probably increase productivity and then the average GDP.

<!-- b000259 | prose | pages [14] -->
– Human right: the negative influences of climate change result in high fre-

<!-- b000260 | prose | pages [14] -->
quency of extreme weather and natural disasters, which directly or indi- rectly brings threats to human’s basic rights including water drinking and hygiene, food, health, housing, culture and development , and influences fragility.

<!-- b000261 | prose | pages [14] -->
3.4 Test PSA

<!-- b000262 | prose | pages [14] -->
After building the basic model PSA, we are going to test it. By analyzing the ranking of FSI, we select 20 countries from different level. We compare the FI calculated by PSA and the ranking of FSI, and then analyze the result.

<!-- b000263 | prose | pages [14] -->
Furthermore, we set up thresholds according to the relevant report.

<!-- b000264 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000265 | furniture | pages [15] -->
Team # 73119

<!-- b000266 | furniture | pages [15] -->
Page 11 of 22

<!-- b000267 | prose | pages [15] -->
We can see the results on the figure below, which makes comparison easily.

<!-- b000268 | caption | pages [15] -->
Figure 4: Fragility Index:Blue circles represent the results of PSA, and red crosses

<!-- b000269 | prose | pages [15] -->
rep-resent the results of FSI

<!-- b000270 | prose | pages [15] -->
The corresponding contries are listed in the Appendix A. From Figure 4, we can clearly see that the result is relatively consistent with the trend of the ranking. For this reason, we believe that PSA is resonable.

<!-- b000271 | prose | pages [15] -->
For task 1, we are required to identify when a state is fragile,vulnerable, or stable. In PSA we can identify a state by Equation 12. For example, when the FI of a state satisfy the inequality F I 0:6, we can draw a conclusion that the state is stable.

<!-- b000272 | caption | pages [15] -->
Table 3: Classification of 20 states

<!-- b000273 | prose | pages [15] -->
PSA Country Code Fragile DRC,EG,BD,HT,KE Vulnerable JM,TR,PH,IN,CN,ZA,MY,BR,MX Stable AR,US,UK,FR,NZ,GR FSI Country Code Fragile DRC,EG,BD,PH,HT,KE

<!-- b000274 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000275 | prose | pages [16] -->
Vulnerable JM,TR,IN,CN,ZA,BR,NZ,MY,BR Stable AR,US,UK,FR,MX

<!-- b000276 | prose | pages [16] -->
From Table 3,Our model’s classification results are mostly consistent with FSI, which proves that our model is valid.

<!-- b000277 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000278 | furniture | pages [17] -->
Team # 73119

<!-- b000279 | furniture | pages [17] -->
Page 12 of 22

<!-- b000280 | prose | pages [17] -->
Case Study 4

<!-- b000281 | prose | pages [17] -->
4.1 Study 1: Democratic Republic Of the Congo

<!-- b000282 | prose | pages [17] -->
We choose the Democratic Republic Of the Congo as our research object. The reason is that this country is top10 in Fragile State Index, with distinct climate change, clear dry and rainy seasons. Climate change has great influences on this state’s fragility.

<!-- b000283 | heading | pages [17] -->
4.1.1 Climate change effects of Congo

<!-- b000284 | prose | pages [17] -->
We collect ten years data of Congo and draw the curve as follow:

<!-- b000285 | caption | pages [17] -->
Figure 5: FI of Congo

<!-- b000286 | prose | pages [17] -->
The reason for the decrease of its fragile index during 2009 to 2010 is the cholera at the end of 2008, which causes 1million people at risk for water-borne diseases.[9] The reason for occurrence of cholera is that the heavy rainstorm created an environment of high temperature and high humidity, and water was polluted by stools.

<!-- b000287 | prose | pages [17] -->
Then the Bacillus comma bred rapidly and people drank the polluted water without any sanitization. At last, cholera broke out and further caught local riots and wars and the state became more fragile. In 2012, Congo suffered the severe drought in 60 years.[10] In some regions, not only rivers, grass dried up but also some basic food like cassava and vegetables were in shortage.[11] It destroyed public service and human right and hence the state became more fragile.

<!-- b000288 | heading | pages [17] -->
4.1.2 The FI without climate change effects

<!-- b000289 | prose | pages [17] -->
According to Task 2, we are required to analyze the situation without considering cli- mate change.

<!-- b000290 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000291 | furniture | pages [18] -->
Team # 73119

<!-- b000292 | furniture | pages [18] -->
Page 13 of 22

<!-- b000293 | caption | pages [18] -->
Figure 6: Comparison of Congo’s FI with and without climate change’s effect

<!-- b000294 | prose | pages [18] -->
According to Task 2, we are required to analyze DRC’s situation without consider- ing climate change. Details are as followed:

<!-- b000295 | prose | pages [18] -->
In the Figure 6, the red curve represents the FI curve without effects of climate change and is denoted as FI-1; the blue curve represents the FI curve with effects of climate change and is denoted as FI-2.

<!-- b000296 | prose | pages [18] -->
We adjust the climate indicator value (temperature anomalies and average elevation) to be consistent to that in 2006, then calculate the values of other non-climatic indica-tors without effects of climate change through regression equation, and finally gain the FI-1 curve through PSR model. The FI-1 curve shows a slow uptrend, which suggest that DRC will be less fragile without effects of climate change. However, without con-sidering the heavy rainstorm during 2008 to 2010, fragile index still rises slowly and even stagnates. It is possible that DRC is affected by other factors like earthquake and refugees.

<!-- b000297 | prose | pages [18] -->
4.2 Study 2: People’s Republic of Bangladesh

<!-- b000298 | heading | pages [18] -->
4.2.1 Climate change effects of Bangladesh

<!-- b000299 | prose | pages [18] -->
As for Task 3, we select Bangladesh as our study state. Reasons are as followed: BD is a fragile state. Occasional climate change in some years makes it more fragile. Nonethe-less, with political stability and government’s interventions to deal with threats of cli-mate change, BD is gradually becoming stable for development.

<!-- b000300 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000301 | furniture | pages [19] -->
Team # 73119

<!-- b000302 | furniture | pages [19] -->
Page 14 of 22

<!-- b000303 | caption | pages [19] -->
Figure 7: FI of Bangladesh

<!-- b000304 | prose | pages [19] -->
As the chart above shows, the general trend of BD is upward. It is mainly the priva-tization policy that BD’s government actively promotes that helps infrastructure con-struction, investment environment’s improvement and economic development. How-ever, the sharp decline of fragile index in 2008 is mainly caused by the Cyclone Sidr in November, 2007, which attacked the southeast coast of BD and badly affected about 1 million families’ life. It was estimated 3406 deaths, 1001 missing and over 55,000 injuries.[12]

<!-- b000305 | prose | pages [19] -->
Gale and flood destroyed housing and infrastructure including roads and bridges. Tide water made water polluted by salt sea water and sanitary fixture was destroyed, which directly gave rise to the soar of natural disaster risk index and sharp decline of public service. In the following years the government took active measures of disaster recov-ery and reconstruction. It is not until 2010 that the country recovered from the hit of Cyclone Sidr in 2007.

<!-- b000306 | prose | pages [19] -->
In June, 2012, rainstorm gave rise to flood and landslide, caught deaths and destruc- tion, and seriously influenced ten regions in norther and southeastern BD.[13]In De- cember, a cold wave once in 40 years hit the northern BD. Hospital reports in affected areas showed larger numbers of people suffered from the relative diseases. The weath-er also caught loss of crops and other natural resources. [14]Climate change in these regions makes BD more fragile.

<!-- b000307 | prose | pages [19] -->
As the BD fragile index curve show, there is obvious decline from 2007 to 2009 and from 2011 to 2012. According to the original statistics, the increases of temperature anoma-lies and natural disaster risk index suggest that both of them (temperature anomalies and natural disaster risk index) are key identify definitive indicators that influence BD’s fragility.

<!-- b000308 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000309 | furniture | pages [20] -->
Team # 73119

<!-- b000310 | furniture | pages [20] -->
Page 15 of 22

<!-- b000311 | heading | pages [20] -->
4.2.2 Prediction

<!-- b000312 | prose | pages [20] -->
We referred to FSI’s ranking and define the three c: stable, vulnerable, fragile, when validating our model in Section 3. BD is in the interval of Frafile.

<!-- b000313 | caption | pages [20] -->
Figure 8: Prediction of Bangladesh

<!-- b000314 | prose | pages [20] -->
According to definition of intervals of fragility in Task 1, BD’s FI is 0.38, meaning it is fragile. Based on the trend of BD’s FI in recent years, we predict its FI predict curve in 80 years through Gray Prediction Model (GM(1,1),Gray Prediction Model). As Figure 8 shows, BD will be stable in 60 years, namely 2076.

<!-- b000315 | heading | pages [20] -->
4.2.3 Effect of Human Intervention

<!-- b000316 | prose | pages [20] -->
We continue to take Bangladesh as our research target. According to the report of the Bangladesh government on climate security and development over the past few years[], they have made some countermeasures against climate change and can be broadly classified into six categories:

<!-- b000317 | prose | pages [20] -->
Intervention1:Food Security Social Protection and Health

<!-- b000318 | prose | pages [20] -->
Intervention2:Comprehensive Disaster Management

<!-- b000319 | prose | pages [20] -->
Intervention3:Climate Resilient Infrastructure

<!-- b000320 | prose | pages [20] -->
Intervention4:Research and Knowledge Management

<!-- b000321 | prose | pages [20] -->
Intervention5:Mitigation and Low Carbon Development

<!-- b000322 | prose | pages [20] -->
Intervention6:Capacity Building and Institutional Strengthening

<!-- b000323 | prose | pages [20] -->
We analyzed the impact of these interventions on our model, as shown in the following table:

<!-- b000324 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000325 | furniture | pages [21] -->
Team # 73119

<!-- b000326 | prose | pages [21] -->
Intervention

<!-- b000327 | furniture | pages [21] -->
Page 16 of 22

<!-- b000328 | prose | pages [21] -->
Impact indicators

<!-- b000329 | prose | pages [21] -->
health index,Gini coefficient Intervention1

<!-- b000330 | prose | pages [21] -->
natural disaster risk index crop production index, Intervention2 percentage of people using basic drinking water services

<!-- b000331 | prose | pages [21] -->
forest cover rate public service,Gini coefficient Intervention3 GDP per capita,Gini coefficient Intervention4 Intervention5 CO2 emission population density,democracy index,human right Intervention6

<!-- b000332 | heading | pages [21] -->
4.2.4 Total cost

<!-- b000333 | prose | pages [21] -->
To predict the total cost of intervention in climate change, first of all we look up the budget allocation for expenditure and total coast of six interventions from 2014 to 2017.

<!-- b000334 | prose | pages [21] -->
From 2014 to 2017, with budgets of other intervention except Intervention2 Compre- hensive Disaster Management increasing relatively steadily, budgets in Intervention2 Comprehensive Disaster Management decreases, which results in the decline of fragili-ty index and better fragility.

<!-- b000335 | prose | pages [21] -->
Therefore, we set up constraint conditions when predicting total cost of BD govern- ment’s interventions:

<!-- b000336 | prose | pages [21] -->
Over the next few years, BD government’s total cost of interventions in climate change will only increase at the growth rate of those in recent years rather than increasing unlimitedly

<!-- b000337 | prose | pages [21] -->
Except Intervention2 Comprehensive Disaster Management, other budgets for expenditure will be predicted according to status quo through Gray Prediction Model

<!-- b000338 | prose | pages [21] -->
The fiscal expenditure of Intervention2: Comprehensive Disaster Management will increase by 35% every five years

<!-- b000339 | prose | pages [21] -->
Total expenditure and budget allocations for expenditure estimated in 5 years, 10 years and 20 years are as followed:

<!-- b000340 | prose | pages [21] -->
in 5 years program Current in 10 years in 20years

<!-- b000341 | prose | pages [21] -->
2076.4 Intervention1 1735.9 2487.5 3570 4680.72 Intervention2 3467.2 6318.972 8530.6122 2890.4 Intervention3 2474.39 3378.4 4615.2 522.7 Intervention4 365.87 786.9 1783.2 185.95 Intervention5 169.92 205.58 251.3 8230 Intervention6 6420.84 10443 16813

<!-- b000342 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000343 | furniture | pages [22] -->
18586.17

<!-- b000344 | prose | pages [22] -->
Total

<!-- b000345 | furniture | pages [22] -->
14633.61

<!-- b000346 | furniture | pages [22] -->
Team # 73119

<!-- b000347 | prose | pages [22] -->
Further Exploration 5

<!-- b000348 | furniture | pages [22] -->
23620.352

<!-- b000349 | furniture | pages [22] -->
35563.3122

<!-- b000350 | furniture | pages [22] -->
Page 17 of 22

<!-- b000351 | prose | pages [22] -->
According to Task 5, we are required to extend our model to a wider range. First of all, we use PSA to analyze the fragility of the continents. We choose Asia, Europe and Africa. Since continent is made up of countries, we are going to take an average of statistics of all the counties. Here, we select several typical countries of every continent and do the analysis.

<!-- b000352 | prose | pages [22] -->
Results calculated by PSA are shown in the table below:

<!-- b000353 | prose | pages [22] -->
Europe Continents Asia Africa 0.8176 FI 0.3218 0.2849

<!-- b000354 | caption | pages [22] -->
Table 4: FI of different continents

<!-- b000355 | prose | pages [22] -->
Frome Table 4, we can clearly see that Europe get the highest score and Africa get the lowest one. By analyzing the FSI map, we can see that our result is reasonable. Almost all the European countries are stable while most of those in Africa are fragile. As a result, we can draw a conclusion that our model works well on continents.

<!-- b000356 | prose | pages [22] -->
Next, we apply our model to analyze the cities. We find that several indicators, such as CO2 emission and crop production index, are hard to be obtained for a specific city. Therefore, we need to modify PSA to make it work on cities.

<!-- b000357 | prose | pages [22] -->
The solution is to replace those indicators that are not suitable for the cities with the similar ones.

<!-- b000358 | prose | pages [22] -->
For example,it is difficult to evaluate the forest cover rate of many cities, we can use greenland rate instead. Besides, crop production index may be another barrier, we can replace it with the local food safety index.

<!-- b000359 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000360 | prose | pages [22] -->
6

<!-- b000361 | prose | pages [22] -->
While we combine the results of AHP and EWM to get the final weight of each indica- tor, we set 1 = 0:8 and 2 = 0:2. Here, we will analyze the sensitivity of 1 and 2.

<!-- b000362 | prose | pages [22] -->
We set 1 = 0:2; 0:3; 0:5; 0:7; 0:8 respectively and get the results as follows:

<!-- b000363 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000364 | furniture | pages [23] -->
Team # 73119

<!-- b000365 | furniture | pages [23] -->
Page 18 of 22

<!-- b000366 | caption | pages [23] -->
Figure 9: Analysis of 1

<!-- b000367 | caption | pages [23] -->
Figure 9 indicates that when the value of 1 is changing, the trend does not change

<!-- b000368 | prose | pages [23] -->
a lot, which means that PSA is stable.

<!-- b000369 | heading | pages [23] -->
Strengths and Weaknesses

<!-- b000370 | prose | pages [23] -->
7

<!-- b000371 | prose | pages [23] -->
7.1

<!-- b000372 | heading | pages [23] -->
Strengths

<!-- b000373 | prose | pages [23] -->
Our model inherits the advantages of AHP (AHP, Analytic Hierarchy Process) and EWM (EWM, Entropy Weight Method).

<!-- b000374 | prose | pages [23] -->
When weighing the indicators, we utilize weight average method combining the AHP (AHP, Analytic Hierarchy Process) with (EWM, Entropy Weight Mothed). To some extent, this method not only provides a supplement of indicators’ hori- zontal comparison with EWM, but also covers the shortages that indicator weight under EWM vary with samples and is even overwhelmingly dependent on sam-ples. Moreover, this method reduces subjectivity of AHP.

<!-- b000375 | prose | pages [23] -->
Our model is effective through validation.

<!-- b000376 | prose | pages [23] -->
Fragile State Index’s result serves as a benchmark to verify our model. We find the results of our model are close to the truth no matter the classification of state fragility or state ranking, which shows that our model is rational.

<!-- b000377 | prose | pages [23] -->
The model we build has good adapability.

<!-- b000378 | prose | pages [23] -->
Experienced studies show that, our model can be adapted to larger states (conti-nents) for effective analysis on fragility.

<!-- b000379 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000380 | furniture | pages [24] -->
Team # 73119

<!-- b000381 | furniture | pages [24] -->
Page 19 of 22

<!-- b000382 | prose | pages [24] -->
7.2

<!-- b000383 | heading | pages [24] -->
Weaknesses

<!-- b000384 | prose | pages [24] -->
In our model, due to time constraints, we just choose the average fragile index of some states to represent the continent’s fragile index during calculation of conti-nent index. Thus, there will be some deviation.

<!-- b000385 | prose | pages [24] -->
In our model, regional instability and violent conflicts are excluded. We don’t take riots and wars into consideration. Therefore, our model is not reliable when facing states with large-scale wars.

<!-- b000386 | heading | pages [24] -->
Conclusions

<!-- b000387 | prose | pages [24] -->
8

<!-- b000388 | prose | pages [24] -->
By building up an indicator system, we select a leading indicator FI to measure a re- gion’s fragility. Our PSA model is reasonable after validation. We analyze Congo and Bangladesh respectively combining climate change. According to our model, we estimate a state’s fiscal expenditure on climate change interference. Afterwards, we expend the application of PSA model to analyze cities and continents our model is testified to be extensible.Finally, by sensitivity analysis, we can see that our model is stable.

<!-- b000389 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000390 | furniture | pages [25] -->
Team # 73119

<!-- b000391 | furniture | pages [25] -->
Page 20 of 22

<!-- b000392 | heading | pages [25] -->
References

<!-- b000393 | references | pages [25] -->
[1] Mcloughlin, C.. Topic guide on fragile states. Birmingham:University of Birming-

<!-- b000394 | references | pages [25] -->
ham, UK. 2012: 5

<!-- b000395 | references | pages [25] -->
[2] CPIA: https://data.worldbank.org/data-catalog/CPIA

<!-- b000396 | references | pages [25] -->
[3] CIFP: https://carleton.ca/cifp/

<!-- b000397 | references | pages [25] -->
[4] FSI: http://fundforpeace.org/fsi/

<!-- b000398 | references | pages [25] -->
[5] Schwartz, P. and Randall, D. ‘An Abrupt Climate Change Scenario and Its Impli-

<!-- b000399 | references | pages [25] -->
cations for United States National Security’, October 2003.

<!-- b000400 | references | pages [25] -->
[6] Climate Change Is Draining Protein Out Of Staple Crops:

<!-- b000401 | references | pages [25] -->
http://www.iflscience.com/environment/climate-change-draining-protein-

<!-- b000402 | references | pages [25] -->
staple-crops/

<!-- b000403 | references | pages [25] -->
[7] Climate Change And Infectious Diseases - World Health Organization

<!-- b000404 | references | pages [25] -->
http://www.who.int/globalchange/publications/climatechangechap6.pdf

<!-- b000405 | references | pages [25] -->
[8] Human Rights and Climate Change

<!-- b000406 | references | pages [25] -->
http://www.ohchr.org/EN/Issues/HRAndClimate-

<!-- b000407 | references | pages [25] -->
Change/Pages/HRClimateChangeIndex.aspx

<!-- b000408 | references | pages [25] -->
[9] Cholera in the Congo: Fighting could cause disease outbreak

<!-- b000409 | references | pages [25] -->
https://blogs.scientificamerican.com/news-blog/cholera-in-the-congo-fighting-

<!-- b000410 | references | pages [25] -->
could-2008-11-11/

<!-- b000411 | references | pages [25] -->
[10] Horn of Africa sees ’worst drought in 60 years’

<!-- b000412 | references | pages [25] -->
http://www.bbc.com/news/world-africa-13944550

<!-- b000413 | references | pages [25] -->
[11] Parts of DR Congo hit by unusual drought

<!-- b000414 | references | pages [25] -->
http://www.africareview.com/news/Unusual-drought-hits-parts-of-

<!-- b000415 | references | pages [25] -->
DRC/979180-1104984-ovfxcqz/index.html

<!-- b000416 | references | pages [25] -->
[12] de Bangladesh G. Cyclone Sidr in Bangladesh: Damage, Loss and Needs

<!-- b000417 | references | pages [25] -->
Assess-ment for Disaster Recovery and Reconstruction[J]. 2008.

<!-- b000418 | references | pages [25] -->
[13] Bangladesh: Floods and Landslides Emergency appeal n MDRBD010 Operation

<!-- b000419 | references | pages [25] -->
update n2 https://reliefweb.int/report/bangladesh/bangladesh-floods-and-

<!-- b000420 | references | pages [25] -->
landslides-emergency-appeal-n%C2%B0-mdrbd010-operation-update-

<!-- b000421 | references | pages [25] -->
n%C2%B02

<!-- b000422 | references | pages [25] -->
[14] Bangladesh: Cold Wave - Dec 2012

<!-- b000423 | references | pages [25] -->
https://reliefweb.int/disaster/cw-2013-000001-bgd

<!-- b000424 | references | pages [25] -->
[15] Liu Zhi, et al. "Application of Entropy Weight Method in Comprehensive Eval-

<!-- b000425 | references | pages [25] -->
uation of Enterprise Performance" Journal of Sinopec Management Institute

<!-- b000426 | references | pages [25] -->
10.4 (2008): 63-65.

<!-- b000427 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000428 | furniture | pages [26] -->
Team # 73119

<!-- b000429 | furniture | pages [26] -->
Page 21 of 22

<!-- b000430 | references | pages [26] -->
[16] Xu Ting-ting, et al. Research on Shanghai Comprehensive Vulnerability

<!-- b000431 | references | pages [26] -->
Assess-ment of Climate Change – Based on PSR Model[J]. Resource

<!-- b000432 | references | pages [26] -->
Development & Mar-ket 2015, 31(3): 288-292.

<!-- b000433 | references | pages [26] -->
[17] Climate Protection and Development Budget Report 2017-18.Finance Divi-

<!-- b000434 | references | pages [26] -->
Government

<!-- b000435 | references | pages [26] -->
sion,Ministry

<!-- b000436 | references | pages [26] -->
of

<!-- b000437 | references | pages [26] -->
Finance

<!-- b000438 | references | pages [26] -->
Bangladesh

<!-- b000439 | heading | pages [26] -->
Appendices

<!-- b000440 | heading | pages [26] -->
Appendix A

<!-- b000441 | prose | pages [26] -->
FI of Country

<!-- b000442 | prose | pages [26] -->
No.

<!-- b000443 | prose | pages [26] -->
Country 1 Congo, Dem. Rep. 2 Egypt 3 Bangladesh 4 Jamaica 5 Turkey 6 Philippines 7 India 8 Haiti 9 China 10 South Africa 11 Malaysia 12 Brazil 13 Argentina 14 Kenya 15 United States 16 United Kingdom 17 France 18 New Zealand 19 Mexico 20 Greece

<!-- b000444 | prose | pages [26] -->
Country Code DRC EG BD

<!-- b000445 | prose | pages [26] -->
of the People’s Republic of

<!-- b000446 | prose | pages [26] -->
FI FSI Ranking 0.3366 7 0.3762 36 0.4047 39 0.5416 117 0.4788 64 0.4454 54 0.5504 72 0.3099 11 0.5288 85 0.5244 96 0.544 116 0.5649 110 0.619 140 0.3746 22 0.7602 158 0.7666 160 0.7842 159 0.8472 170 0.5376 88 0.6615 127

<!-- b000447 | prose | pages [26] -->
JM TR PH IN HT CN ZA 0.542 PSA 0.337 0.376 0.396 Rank 19 17 16 0.479 0.445 0.550 0.310 0.529 0.524 10 10 14 15 8 20 12 13 0.594 FSI 0.1839 0.348 0.365 Rank 20 17 16 Country Code MY BR AR 0.456 0.399 0.501 0.207 0.525 0.537 7 7 14 15 13 19 12 11 KE US UK FR NZ MX GR 0.375 PSA 0.544 0.565 0.619 Rank 9 7 6 0.760 0.767 0.784 0.847 0.538 0.662 18 18 4 3 2 1 11 5

<!-- b000448 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000449 | prose | pages [27] -->
FSI

<!-- b000450 | furniture | pages [27] -->
0.590

<!-- b000451 | furniture | pages [27] -->
0.566

<!-- b000452 | furniture | pages [27] -->
0.685

<!-- b000453 | furniture | pages [27] -->
0.269

<!-- b000454 | furniture | pages [27] -->
0.787

<!-- b000455 | furniture | pages [27] -->
0.798

<!-- b000456 | furniture | pages [27] -->
0.793

<!-- b000457 | furniture | pages [27] -->
0.855

<!-- b000458 | furniture | pages [27] -->
0.542

<!-- b000459 | furniture | pages [27] -->
0.612

<!-- b000460 | prose | pages [27] -->
Rank

<!-- b000461 | furniture | pages [27] -->
8

<!-- b000462 | furniture | pages [27] -->
9

<!-- b000463 | furniture | pages [27] -->
5

<!-- b000464 | furniture | pages [27] -->
18

<!-- b000465 | furniture | pages [27] -->
4

<!-- b000466 | furniture | pages [27] -->
2

<!-- b000467 | furniture | pages [27] -->
3

<!-- b000468 | furniture | pages [27] -->
1

<!-- b000469 | furniture | pages [27] -->
10

<!-- b000470 | furniture | pages [27] -->
6

<!-- b000471 | furniture | pages [27] -->
Team # 73119

<!-- b000472 | furniture | pages [27] -->
Page 22 of 22

<!-- b000473 | heading | pages [27] -->
Appendix B

<!-- b000474 | prose | pages [27] -->
Climate expenditure of Bangladesh

<!-- b000475 | caption | pages [27] -->
Figure 10: Climate Expenditure: 2011-2014

<!-- b000476 | caption | pages [27] -->
Figure 11: Climate Expenditure: 2015-2017
