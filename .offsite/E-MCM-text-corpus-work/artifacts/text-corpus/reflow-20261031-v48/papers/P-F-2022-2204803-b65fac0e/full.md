# P-F-2022-2204803-b65fac0e

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2022

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
F

<!-- b000005 | title | pages [1] -->
2204803

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Space For Global Equity

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
The Outer Space Treaty is the main international treaty that is widely accepted to regulate the exploitation of space resources. However, it only makes the provisions in principle but cannot provide speciﬁc guidance. Given the possibility of asteroid mining, there are still many open questions. Therefore, a reasonable solution is needed to deﬁne "global equity". Based on it, we further explore the impacts of asteroid mining and propose policies to promote global equity.

<!-- b000010 | prose | pages [1] -->
To measure the global equity issues, we establish an evaluation model to quantify the developing degree of countries and the degree of global equity. We ﬁrst apply the McKinsey logic tree analysis to ﬁnd out all necessary indicators. After that, Entropy Weight Method is used to calculate the weights. And the National Development Level Index(NDI) can be calculated by weighted summation. We then apply K-Means to cluster countries into three categories by their NDI. Finally, we use the average NDI of the ﬁrst and the last category to measure the Global Equity Index(GEI). To validate the model, we ground this model in reality and get convicing results.

<!-- b000011 | prose | pages [1] -->
In the second part, we conceive the development of asteroid mining in the future. We assume that asteroid mining is an international exchange funded by national gov- ernments. Based on the model in the previous section that measures global equity, we use the Fuzzy Comprehensive Evaluation Method to get the possible impact of the industry, whose factor set is the inﬂuencing factor of global equity, evaluation set is EWM results. We set points for the factors, ﬁnally got the impact value, IM, of more- and less-developed countries under this kind of situation. Then we changed the con- ditions we chose, turning the funder into private enterprises. Using the same analysis method, we also obtained the impact value IM of more- and less-developed countries. The four impact values obtained are compared and analyzed to explore how asteroid mining will affect global equity under different conditions. We analyze the difference of impacts of the two scenarios and propose possible policies from different perspec- tives.

<!-- b000012 | prose | pages [1] -->
Finally, we make model sensitivity analysis by changing the variance of important parameters, then evaluate the strengths and weaknesses of the model, and put forward improvement schemes.

<!-- b000013 | heading | pages [2] -->
Contents

<!-- b000014 | contents | pages [2] -->
1 Introduction

<!-- b000015 | contents | pages [2] -->
2

<!-- b000016 | contents | pages [2] -->
1.1

<!-- b000017 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000018 | contents | pages [2] -->
2

<!-- b000019 | contents | pages [2] -->
1.2

<!-- b000020 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | contents | pages [2] -->
2

<!-- b000022 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000023 | contents | pages [2] -->
3

<!-- b000024 | contents | pages [2] -->
2.1

<!-- b000025 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
3

<!-- b000027 | contents | pages [2] -->
2.1.1

<!-- b000028 | contents | pages [2] -->
Overall Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000029 | contents | pages [2] -->
3

<!-- b000030 | contents | pages [2] -->
2.1.2

<!-- b000031 | contents | pages [2] -->
Assumptions for Task 1

<!-- b000032 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
3

<!-- b000034 | contents | pages [2] -->
2.1.3

<!-- b000035 | contents | pages [2] -->
Assumptions for Task 2&3 . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
3

<!-- b000037 | contents | pages [2] -->
2.2

<!-- b000038 | contents | pages [2] -->
Symbol Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
3

<!-- b000040 | contents | pages [2] -->
3 National Development Level Index Model

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
3.1

<!-- b000043 | contents | pages [2] -->
Indicator Selection

<!-- b000044 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
5

<!-- b000046 | contents | pages [2] -->
3.1.1

<!-- b000047 | contents | pages [2] -->
Economic Indicators . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
5

<!-- b000049 | contents | pages [2] -->
3.1.2

<!-- b000050 | contents | pages [2] -->
Social Indicators

<!-- b000051 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
6

<!-- b000053 | contents | pages [2] -->
3.1.3

<!-- b000054 | contents | pages [2] -->
Environmental Indicators . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
6

<!-- b000056 | contents | pages [2] -->
3.1.4

<!-- b000057 | contents | pages [2] -->
Civilization Indicators . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
7

<!-- b000059 | contents | pages [2] -->
3.1.5

<!-- b000060 | contents | pages [2] -->
Political Indicators . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
7

<!-- b000062 | contents | pages [2] -->
3.2

<!-- b000063 | contents | pages [2] -->
Weight Determination

<!-- b000064 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
7

<!-- b000066 | contents | pages [2] -->
3.3

<!-- b000067 | contents | pages [2] -->
Nation Classiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
8

<!-- b000069 | contents | pages [2] -->
3.4

<!-- b000070 | contents | pages [2] -->
Global Equity Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
10

<!-- b000072 | contents | pages [2] -->
3.5

<!-- b000073 | contents | pages [2] -->
Model Validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
11

<!-- b000075 | contents | pages [2] -->
4 Impact of Asteroid Mining on Future Global Equity

<!-- b000076 | contents | pages [2] -->
12

<!-- b000077 | contents | pages [2] -->
4.1

<!-- b000078 | contents | pages [2] -->
Funded by Nation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [2] -->
13

<!-- b000080 | contents | pages [2] -->
4.2

<!-- b000081 | contents | pages [2] -->
Funded by Private Enterprise . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
15

<!-- b000083 | contents | pages [2] -->
4.3

<!-- b000084 | contents | pages [2] -->
Impacts Asteroid Mining Brings to Global Equity

<!-- b000085 | contents | pages [2] -->
. . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
17

<!-- b000087 | contents | pages [2] -->
5 Policies Could Be Implemented

<!-- b000088 | contents | pages [2] -->
18

<!-- b000089 | contents | pages [2] -->
5.1

<!-- b000090 | contents | pages [2] -->
Economic Aspects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
19

<!-- b000092 | contents | pages [2] -->
5.2

<!-- b000093 | contents | pages [2] -->
Civilization Aspects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
19

<!-- b000095 | contents | pages [2] -->
5.3

<!-- b000096 | contents | pages [2] -->
Industry Aspects

<!-- b000097 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000098 | contents | pages [2] -->
20

<!-- b000099 | contents | pages [2] -->
6 Sensitive Analysis

<!-- b000100 | contents | pages [2] -->
21

<!-- b000101 | contents | pages [2] -->
7 Strengths and Weaknesses

<!-- b000102 | contents | pages [2] -->
21

<!-- b000103 | contents | pages [2] -->
7.1

<!-- b000104 | contents | pages [2] -->
Strengths and Importance . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000105 | contents | pages [2] -->
21

<!-- b000106 | contents | pages [2] -->
7.2

<!-- b000107 | contents | pages [2] -->
Weaknesses and Improvements . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000108 | contents | pages [2] -->
22

<!-- b000109 | contents | pages [2] -->
8 Conclusion

<!-- b000110 | contents | pages [2] -->
22

<!-- b000111 | contents | pages [2] -->
References

<!-- b000112 | contents | pages [2] -->
22

<!-- b000113 | furniture | pages [3] -->
Team # 2204803

<!-- b000114 | furniture | pages [3] -->
Page 2 of 22

<!-- b000115 | heading | pages [3] -->
1 Introduction

<!-- b000116 | heading | pages [3] -->
1.1 Problem Background

<!-- b000117 | prose | pages [3] -->
To meet the needs of survival and development, people constantly seek and de- velop available resources. The rapid development of science and technology has made space a virgin land for resource development. The Outer Space Treaty signed in 1967 is currently the main international treaty regulating space resource development activ- ities. It stipulates that "the exploration and use of outer space (including the Moon and other celestial bodies) should seek the welfare and interests of all countries, regardless of the degree of economic or scientiﬁc development, and should be the scope of de- velopment for all mankind." [1] It provides a legal basis for many countries to explore space resources and has positive signiﬁcance in regulating the development of space resources.

<!-- b000118 | prose | pages [3] -->
However, the "Outer Space Treaty" only makes a principled provision, which can- not provide speciﬁc guidance for human development activities. Taking asteroid min- ing, which is considered to be the most accessible and potential in the current research on the development of space resources as an example, the topics to be discussed are: is mining technically feasible? Can we beneﬁt enough from it? Who should take the main role, private enterprises, countries, or international organizations? In addition, the current global development is extremely unequal, and there is a huge gap in scien- tiﬁc, technological, and economic forces between countries. In this way, small countries will not be able to obtain any beneﬁts in the competition for space resources, and will the gap become larger and larger? There are still many problems to be solved.

<!-- b000119 | prose | pages [3] -->
Therefore, a reasonable solution is needed to deﬁne what is ’global equity’, and based on this deﬁnition, the possible impacts on asteroid mining on it are discussed, and corresponding policies are put forward to promote global equity.

<!-- b000120 | heading | pages [3] -->
1.2 Our Work

<!-- b000121 | prose | pages [3] -->
We are required to develop a model to give measurement standards on how to de- ﬁne global equity. Based on this model, the future developments of asteroid mining are predicted and demonstrated, the possible impacts of mining on global equity and the conditions under which changes relate to these impacts are identiﬁed, and corre- sponding policies for global equity development are proposed.

<!-- b000122 | prose | pages [3] -->
To solve this problem, we have done the following work:

<!-- b000123 | prose | pages [3] -->
• We give several basic assumptions to simplify the model and deﬁne symbols as different indexes.

<!-- b000124 | prose | pages [3] -->
• For the deﬁnition of global equity, we propose different indicators from economic and social aspects, calculate the corresponding weights by using the entropy weight method, and rank countries. They are divided into three categories by using the k-means clustering analysis method, and the degree of inequity is de- termined by the difference value.

<!-- b000125 | prose | pages [3, 4] -->
• We discuss the possible impact on two different situations in which mining activ- ities are carried out by the State and private enterprises and use Fuzzy Compre- hensive Evaluation Method to evaluate and analyze the changes in global equity in the future.

<!-- b000126 | furniture | pages [4] -->
Team # 2204803

<!-- b000127 | furniture | pages [4] -->
Page 3 of 22

<!-- b000129 | prose | pages [4] -->
• Make our policy recommendations in response to these possible implications.

<!-- b000130 | prose | pages [4] -->
• Analyze and evaluate the model and make recommendations for improvement.

<!-- b000131 | heading | pages [4] -->
2 Preparation of the Models

<!-- b000132 | heading | pages [4] -->
2.1 Assumptions

<!-- b000133 | heading | pages [4] -->
2.1.1 Overall Assumptions

<!-- b000134 | prose | pages [4] -->
1. The data we collect from online databases is accurate, reliable and mutually con- sistent. Since our data sources are all websites of international organizations, it’s reasonable to assume the high quality of their data.

<!-- b000135 | prose | pages [4] -->
2. In model veriﬁcation, the indicator data from countries that we neglect has little impact on the calculation of the weights and the results.

<!-- b000136 | prose | pages [4] -->
3. We assume the country as an overall unit without considering the differences of regions within the country.

<!-- b000137 | heading | pages [4] -->
2.1.2 Assumptions for Task 1

<!-- b000138 | prose | pages [4] -->
1. We do not take into account the cultural inﬂuence of a country, such as the degree to which its entertainment industry and literary works inﬂuence the world.

<!-- b000139 | prose | pages [4] -->
2. We choose the relative value instead of absolute value.

<!-- b000140 | prose | pages [4] -->
3. We consider the per capita level of the country, not the overall level, as a measure.

<!-- b000141 | heading | pages [4] -->
2.1.3 Assumptions for Task 2&3

<!-- b000142 | prose | pages [4] -->
1. We assume that the classiﬁcation of countries in task 1 does not change in task 2 and 3, that is, we assume that there will be no signiﬁcant change in the relative level of development of the country (that is, the level of development compared to other countries) when we do asteroid mining in the future.

<!-- b000143 | prose | pages [4] -->
2. We assume that asteroid mining is an industry with high-threshold and that fu- ture technologies are not advanced enough for individuals or small companies to enter the market.

<!-- b000144 | prose | pages [4] -->
3. We do not consider asteroid mining projects funded only by individual govern- ments, but by cooperation among governments and multinational corporations

<!-- b000145 | prose | pages [4] -->
4. We do not take Sudden change into consideration.

<!-- b000146 | heading | pages [4] -->
2.2 Symbol Description

<!-- b000147 | prose | pages [4] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000148 | furniture | pages [5] -->
Team # 2204803

<!-- b000149 | furniture | pages [5] -->
Page 4 of 22

<!-- b000150 | caption | pages [5] -->
Table 1: Notations

<!-- b000151 | prose | pages [5] -->
Symbol Deﬁnition

<!-- b000152 | prose | pages [5] -->
t time i The name of the country Eco1,i(t) Capital formation per capita of country I at time T Eco2 National income per capita of country I at time T, adjusted for purchasing power levels Eco3 Proportion of people living in absolute poverty in country I at time T (measured by daily income of $1.9) Eco4 National income per capita of country I at time T, adjusted for purchasing power levels Civ1 Country I’s share of R&D spending at time T Civ2 Higher education enrolment rate for country I at time T Gov1 Military spending for country I at time T (% of GDP) Gov2 Strength of legal rights index for country I at time T Env1 Nitrous oxide emissions of country I at time T Env2 Share of renewable energy generation for country I at time T Soc2 Intentional homicide victims for country I at time T Soc3 Out-of-pocket expenditure per capita for country I at time T Soc4 Proportion of urban population in country I at time T Soc5 Residents’ average lifespan for country I at time T NDI National development level index of country I at time T GEI(t) Global equity index at time T REI(t) Regional equity index at time T IM Impact value of country I at time T

<!-- b000153 | heading | pages [5] -->
3 National Development Level Index Model

<!-- b000154 | prose | pages [5] -->
Global equity, which is the opposite of global inequity, is deﬁned as the degree to which development levels and opportunities are similar across countries and regions in comprehensive dimensions.

<!-- b000155 | prose | pages [5] -->
We tried to deﬁne an index, Global Equity Index(GEI), to measure global equity. To come up with the index, we ﬁrst need to measure the level of development and the potential for future development of all countries. By comparing the development and potential of different countries, we can measure the degree of equity globally.

<!-- b000156 | prose | pages [5] -->
To make a clear and correct understanding of the equity issues of the world, we establish an evaluation model to quantify the developing degree of countries and the degree of global equity. We ﬁrst apply the McKinsey logic tree analysis to thoroughly ﬁnd out all necessary indicators. After that, Entropy Weight Method(EWM) is used to calculate the importance of each indicator. Knowing the weight of each indicator, the National Development Level Index(NDI) can be calculated by weighted summation. We then apply K-Means to cluster countries into three categories by their NDI. Finally, we use the average NDI of the ﬁrst and the last category to measure the GEI which measures the level of global equity.

<!-- b000157 | furniture | pages [6] -->
Team # 2204803

<!-- b000158 | furniture | pages [6] -->
Page 5 of 22

<!-- b000159 | heading | pages [6] -->
3.1 Indicator Selection

<!-- b000160 | prose | pages [6] -->
The development level of a country is mainly reﬂected in ﬁve aspects: economy, society, environment, civilization, and politics. And there are many factors and indica- tors in these ﬁve areas. In our model, we use the McKinsey logic tree analysis to select several important indicators to estimate the extent of a country’s development and its potential for future development. The selected indicators are shown in Fig.1.

<!-- b000161 | caption | pages [6] -->
Figure 1: Indicators selected by McKinsey logic tree analysis

<!-- b000162 | heading | pages [6] -->
3.1.1 Economic Indicators

<!-- b000163 | prose | pages [6] -->
In terms of economy, income per capita adjusted according to the purchasing power parity can better compare the actual consumption capacity of residents in different countries and regions, reﬂecting the degree of economic development of a country.

<!-- b000164 | prose | pages [6] -->
At the same time, the percentage of the ﬁrst and second industry to the overall industry can reﬂect a country’s industry advanced level. For those countries with a high percentage of the ﬁrst and second industries, their dominant industries, such as agriculture and manufacturing do not contain many technical skills, which are also named as labor-intensive industries. Thus, the whole industry system has a large way to go. They need some industrial upgrading.

<!-- b000165 | prose | pages [6] -->
Capital formation per capita shows the scale of a country’s net capital investment. The higher the index is, the stronger the country’s capacity to expand production in the future and the greater the potential of future economic development.

<!-- b000166 | prose | pages [6, 7] -->
Absolute poverty population proportion, according to the daily income of $1.9 as a measure, embodies a nation’s population in extreme poverty. The higher the index, the more backward development of a country is. If there are lots of residents who are difﬁcult to maintain basic existence, the stability of society as a whole will decline, and its potential for future development will also be affected.

<!-- b000167 | furniture | pages [7] -->
Team # 2204803

<!-- b000168 | furniture | pages [7] -->
Page 6 of 22

<!-- b000170 | heading | pages [7] -->
3.1.2 Social Indicators

<!-- b000171 | prose | pages [7] -->
In terms of society, the average lifespan of residents can reﬂect the overall physical condition of residents and the social medical level. We tend to believe that a country with a longer average lifespan has a healthier living environment, a more developed medical system, and more abundant medical resources. Infants death rate is also a good reﬂection of a country’s medical level. The lower the infants death rate, the higher the level of medical development and the higher the overall social development.

<!-- b000172 | prose | pages [7] -->
The proportion of the urban population shows the level of urbanization and mod- ernization of a country. Generally speaking, cities have better infrastructure than rural areas and residents have better living standards. Therefore, it is believed that a country with a higher proportion of the urban population has a higher level of modernization and social development.

<!-- b000173 | prose | pages [7] -->
Out-of-pocket expenditure per capita, which measures the medical expenses paid by residents themselves instead of insurance companies or government, reﬂects the overall social welfare level of a country. The expense reveals a country’s level of so- cial insurance and social welfare. The higher the expenditure, the lower level of social welfare a country owns. The lower the level of social welfare, the more uncertain res- idents future is, the greater the possibility of being in poverty caused by great shocks, and the greater the possibility of class dropping. Therefore, we believe that the less out-of-pocket expenditure, the higher the level of social development of the country.

<!-- b000174 | prose | pages [7] -->
Intentional homicide victims reﬂect the level of social security. The more homicide victims, the lower the overall level of social security, the lower the degree of social development.

<!-- b000175 | heading | pages [7] -->
3.1.3 Environmental Indicators

<!-- b000176 | prose | pages [7] -->
In terms of the environment, nitrous oxide emissions can, to some extent, reﬂect the number of harmful gases emitted by a country. Nitrous oxide not only has nega- tive effects on residents health, including a decrease in intelligence, hearing and visual ability, and practical ability but also has extremely adverse effects on the environment. Nitrous oxide removes ozone from the stratosphere, increasing the hole in the ozone layer. Therefore, we believe that the more nitrous oxide a country emits, the worse its environmental development status is.

<!-- b000177 | prose | pages [7] -->
The other environmental indicator is the proportion of electricity generated from nonrenewable sources. At present, nonrenewable energy used for power generation mainly includes oil, coal, natural, gas, and so on. Compared with renewable energy such as hydropower and wind power, these energy sources usually produce more pol- lutants. Also, considering that nonrenewable resource has limited quantity, the more nonrenewable energy is used, the less favorable it is to future development. There- fore, we believe that the greater the proportion of nonrenewable energy generation in a country, the worse its environmental status, and the less conducive to future devel- opment.

<!-- b000178 | furniture | pages [8] -->
Team # 2204803

<!-- b000179 | furniture | pages [8] -->
Page 7 of 22

<!-- b000180 | heading | pages [8] -->
3.1.4 Civilization Indicators

<!-- b000181 | prose | pages [8] -->
In terms of civilization, a higher education enrollment rate can well reﬂect the edu- cational level of a country’s residents and indicates that there are sufﬁcient educational resources. The labor force with higher education usually has more advanced technical skills and has more advantages in the accumulation of human resources, which will play an important role in promoting social development. The higher the proportion of people with higher education in a country, the more abundant human resources per capita, the more conducive to industrial upgrading in the future. Therefore, we be- lieve that the higher the enrollment rate of higher education in a country, the higher its cultural development level and the greater its future development potential.

<!-- b000182 | prose | pages [8] -->
The proportion of R&D spending reﬂects the importance a country places on sci- ence and technology development, as well as the amount of research carried out at the time. The development of science and technology needs a lot of investment, and the initial investment is essential. Given the great role that scientiﬁc and technologi- cal progress plays in promoting national development, it is generally believed that the more a country attaches importance to the development of science and technology, the greater its potential for future development.

<!-- b000183 | heading | pages [8] -->
3.1.5 Political Indicators

<!-- b000184 | prose | pages [8] -->
In politics, the proportion of military spending reﬂects how much a country at- taches importance to its national defense and how powerful it is. For the residents of a country, the stronger the national army is, the more it can protect itself from inva- sion by other countries. Also, the need for security in the second layer of Maslow’s hierarchy of needs can be satisﬁed by a strong army. At the same time, for a country, the strength of the military is usually related to its international status. Therefore, we believe that countries with a low proportion of national military expenditure have a lower level of social security, political inﬂuence, and development.

<!-- b000185 | prose | pages [8] -->
The strength of legal rights reﬂects the extent to which people are encouraged to take credit at the legal level. We generally think that the more a country encourages credit, the more dynamic its society is, the more positive the business climate is, the more productive its citizens are, and therefore the higher its overall growth potential.

<!-- b000186 | heading | pages [8] -->
3.2 Weight Determination

<!-- b000187 | prose | pages [8] -->
The weight calculated by EWM is determined by the information entropy of the index which implies the variation degree of the index. The larger the information en- tropy is, the more signiﬁcant it is in the evaluation. Therefore, it is objective to use EWM to determine the weight of the f index when calculating NDI.[9]

<!-- b000188 | prose | pages [8, 9] -->
Our data used to estimate the indicators comes from multiple databases, including World Bank [5], UNdata[7], etc. When data vacancy occurs too often, we take the coun- try out of our evaluation list. For tolerable data missing, we use the average value of nearby terms or the data of a similar country to ﬁll the blanks. In this way, we can get relatively accurate results and keep sufﬁcient messages as well. After data processing, we obtained data from 115 countries and regions for ﬁve separate years. Indicators could be divided into positive ones and negative ones. The increase of positive indica- tors represents the increase of the developing index while the negative indicators work oppositely. To equally normalize all data, we ﬁrst apply Eq.1 on all negative indicators.

<!-- b000189 | furniture | pages [9] -->
Team # 2204803

<!-- b000190 | furniture | pages [9] -->
Page 8 of 22

<!-- b000192 | prose | pages [9] -->
Xij = max(Xi) −Xij (1)

<!-- b000193 | prose | pages [9] -->
Then we normalize all data by Eq.2.

<!-- b000194 | prose | pages [9] -->
Xij −min(Xi) Yij = (2) max(Xi) −min(Xi)

<!-- b000195 | prose | pages [9] -->
where Xij represents the original data of the ith indicator value of countryj, while min(Xi) and max(Xi) represents the minimum and maximum data in the ith indica- tor of countryj.

<!-- b000196 | prose | pages [9] -->
The information entropy can be obtained from Eq.3 and Eq.4

<!-- b000197 | prose | pages [9] -->
Yij Pij = (3) ∑n i=1 Yi

<!-- b000198 | prose | pages [9] -->
n Ej = −1 ∑ Pij ln Pij (4) ln n i=1

<!-- b000199 | prose | pages [9] -->
If Pij = 0, plug Eq.5 into Eq.4.

<!-- b000200 | prose | pages [9] -->
Pij→0 Pij ln Pij = 0 lim (5)

<!-- b000201 | prose | pages [9] -->
Based on the information entropy Ej, the weight of each indicator could be calcu- lated by Eq.6 Wi = 1 −Ei (i = 1, 2, ..., k) (6) k −ΣEi

<!-- b000202 | prose | pages [9] -->
We assign weights to each indicator based on the discussion above, and the weight results are as follows: Capital formation per capita (25.40%), National income per capita (15.57%), Proportion of people living in absolute poverty (2.40%), Proportion of the primary and secondary industries (1.48%), R&D spending (15.81%), Higher ed- ucation enrolment rate (10.11%), Military spending (6.32%), Strength of legal rights index (3.68%) Residents average lifespan 3.44% Proportion of urban population 4.80% Infants deaths rate 2.60% Out-of-pocket expenditure per capita0.60% Intentional homi- cide victims0.65% Share of renewable energy generation6.78% and Nitrous oxide emis- sions (0.37%). And the weight of all 15 indicators is shown in Fig.2.

<!-- b000203 | prose | pages [9] -->
To better analyze the result, brief statistics are made. The economic indicators to- gether weigh 44.85%, the civilization indicators weigh 25.92%, the political indicators weigh 10.00%, the environmental indicators weigh 7.15%, and the weight of society indicators add up to 12.08%. We can ﬁnd that economic and cultural factors have the greatest inﬂuence on the level of development, while political, environmental, and so- cial factors are almost the same weight.

<!-- b000204 | heading | pages [9] -->
3.3 Nation Classiﬁcation

<!-- b000205 | prose | pages [9] -->
After the weight of each indicator is obtained, we can calculate the NDI of each country by weighted summation. Part of the results is shown in Table 2.

<!-- b000206 | furniture | pages [10] -->
Team # 2204803

<!-- b000207 | furniture | pages [10] -->
Page 9 of 22

<!-- b000208 | caption | pages [10] -->
Figure 2: Weights of indicators calculated by EWM

<!-- b000209 | caption | pages [10] -->
Table 2: NDI of 12 countries in 2020

<!-- b000210 | prose | pages [10, 11] -->
Australia Canada Chile China Germany France 11373.89 9805.329 4453.337 5837.792 11395.91 9948.838 UK India Russia US Zimbabwe Kenya 9010.635 2104.981 5398.976 14424.82 589.7691 870.7451 The level of development of countries around the world reﬂected by NDI is shown in Fig.3. The more bright the red is, the more developed the country is.

<!-- b000211 | caption | pages [10] -->
Figure 3: Global development level in 2020

<!-- b000212 | furniture | pages [11] -->
Team # 2204803

<!-- b000213 | furniture | pages [11] -->
Page 10 of 22

<!-- b000215 | prose | pages [11] -->
We work out the data of 115 countries for ﬁve consecutive years (2016-2020) and clustered them into three development level groups through K-Means: High, Medium, and Low. The distribution of the NDI of the countries is shown in Fig.4.

<!-- b000216 | caption | pages [11] -->
Figure 4: NDI distribution

<!-- b000217 | prose | pages [11] -->
All countries are divided into 3 categories based on their NDI. To better ﬁnd out the characteristic of NDI distribution and to understand current global equity situation, a brief statistic analysis is made. Statistic data of all categories shows in Table 3.

<!-- b000218 | caption | pages [11] -->
Table 3: Categories’ information based on K-Means

<!-- b000219 | prose | pages [11] -->
Development level High Medium Low Number of countries 29 39 47 Maximum NDI 19954.2108 6604.2307 1536.5082 Average NDI 11249.3064 4005.7011 747.11192 Minimum NDI 6781.3563 1894.3348 274.00511

<!-- b000220 | heading | pages [11] -->
3.4 Global Equity Index

<!-- b000221 | prose | pages [11] -->
After dividing all countries into three development levels according to NDI, the av- erage value of the Group High and Group Low can be calculated. GEI is calculated by Eq.7. GEI calculated by the data of 115 countries in 2020 is 14.06, indicating signiﬁcant global inequity.

<!-- b000222 | prose | pages [11] -->
GEI(t) = avg(NDIHigh(t)) −avg(NDILow(t)) (7) avg(NDILow(t))

<!-- b000223 | prose | pages [11] -->
It can be observed that the countries with High and Medium development degree mainly distribute in North America and Europe, while the countries with Low devel- opment degree in South America, Asia, and Africa. And African countries have the lowest average level in Group Low. We can tell that global inequity is regional and the differences within regions are rather small.

<!-- b000224 | furniture | pages [12] -->
Team # 2204803

<!-- b000225 | furniture | pages [12] -->
Page 11 of 22

<!-- b000226 | prose | pages [12] -->
In addition, 29 countries NDI is considered High, 39 Medium, and 47 Low. There- fore, quite a lot of countries lack the resources and opportunities of developing. If effective measures are not taken, global inequity will go worsen.

<!-- b000227 | prose | pages [12] -->
The NDI of countries in Group High and Group Low has an enormous difference. The average NDI of Group High is hundreds of times more than the average NDI of Group Low. It is worth noting that the indicators we selected are percentages and per capita, so NDI is not affected by the size of the country. It is an assessment of the level of development and potential regardless of magnitude. So the disparity is remarkable.

<!-- b000228 | heading | pages [12] -->
3.5 Model Validation

<!-- b000229 | prose | pages [12] -->
By studying the level of income per capita growth in the past ﬁve years, we can see that the outstanding development degree countries have nearly ten times the average income gap to the poor development degree countries. The difference in per capita income of categories separated by the K-Means obtained a good result. However, it is worth mentioning that there is no signiﬁcant difference in income growth between developed countries and poor countries. But under the impact of COVID-19 in 2020, developed countries showed better risk resistance. Most countries only appear a small decline in income or even show an upward trend. Meanwhile, the poor countries have generally seen a marked drop in income per capita, with average incomes falling by around 3% compared with 2019. The growing trend is shown in Fig.5.

<!-- b000230 | caption | pages [12] -->
Figure 5: The growing trend of income per capita

<!-- b000231 | prose | pages [12] -->
To test the validity of the model, we selected major European Union countries and evaluated their Regional Equity Index(REI) in 1990 and 2015. There are three reasons for choosing EU countries: ﬁrst, the data of EU countries are relatively complete; sec- ond, the EU was established in 1993, so we can observe the changes of REI over a long period; third, the NDI of EU countries is relatively different and there are different categories of countries. We have chosen a total of 25 EU countries, ignoring the entry and exit of some countries. Because there aren’t so many countries, we only divide countries into two categories, High and Low.

<!-- b000232 | prose | pages [12, 13] -->
In 1990, the average NDI of countries in Group High was 5714.66, and that of coun- tries in Group Low was 1567.36. It can be observed that the former was 3.65 times that of the latter. And the REI of EU nations in 1990 is 2.65. After 25 years of development, the countries in two groups have barely changed, with only two countries changing groups. However, in 2015, the average NDI of countries in Group High is 11330.54, and that of countries in Group Low is 5948.52. So the former was 1.90 times the lat- ter. And the REI of EU nations in 2015 decreased to 0.90. Therefore, the European countries joining the EU keep developing while regional inequity among them also gradually decreases. This is a logical tendency so the validity of the model has been veriﬁed.

<!-- b000233 | furniture | pages [13] -->
Team # 2204803

<!-- b000234 | furniture | pages [13] -->
Page 12 of 22

<!-- b000236 | heading | pages [13] -->
4 Impact of Asteroid Mining on Future Global Equity

<!-- b000237 | prose | pages [13] -->
Now we have got a model to measure the development equity among countries around the world. This model contains many factors, and undoubtedly the asteroid mining industry will have varying degrees of impact on some of them, thus chang- ing the pattern of global equity in the future. In this section, we will further discuss how much the mining industry will have an impact on what factors. Here, we assume that asteroid mining is an international exchange and cooperation project, funded and led by the national government, with technology and labor coming from the partner countries and the proﬁts distributed by the partner countries for respective social con- struction. We will focus on the different impacts of this emerging industry on more developed and rich countries and on less developed countries in two cases.

<!-- b000238 | prose | pages [13] -->
We use the Fuzzy Comprehensive Evaluation Method (FCE) to estimate the possi- ble impact. We stipulate that the factor set is the inﬂuencing factor of global equity in the previous part:

<!-- b000239 | prose | pages [13] -->
U = {Civ1, Civ2, Eco1, Eco2, Eco3, Eco4, Env1, Env2, Gov1, Gov2, Sco1, Sco2, Sco3, Sco4, Sco5} (8)

<!-- b000240 | prose | pages [13] -->
We set the evaluation set as possible results, and we set it as "signiﬁcant impact", "moderate impact", "barely impact", moderate negative impact" and "signiﬁcant nega- tive impact":

<!-- b000241 | prose | pages [13] -->
V = {”signi f icant impact”, ”moderate impact”, ”barely impact”, ”moderate negative impact”, ”signi f icant negative impact”} (9)

<!-- b000242 | prose | pages [13] -->
The weight is the weight of each factor analyzed in the previous part :

<!-- b000243 | prose | pages [13] -->
A = {0.15568, 0.25402, 0.10114, 0.15807, 0.06324, 0.03681, 0.03437, 0.04799, 0.02395, 0.01481, 0.06775, 0.00372, 0.00645, 0.00599, 0.02603} (10)

<!-- b000244 | prose | pages [13] -->
We will estimate the probability of each factor being affected, "very likely to occur" as 0.7, "very likely to occur" as 0.3, and "almost unlikely" as 0 to form a single-factor fuzzy evaluation matrix, and ﬁnally, the coefﬁcient of each factor in the evaluation set is obtained, that is, the weight.

<!-- b000245 | prose | pages [13] -->
We assign each element in the evaluation set a score of {5, 2, 1, −2, −5}, with the positive number representing the positive impact and the negative number represent- ing the negative impact. The ﬁnal impact value of asteroid mining, I, can be obtained by multiplying the score by the weight. The larger I is, the greater the positive inﬂu- ence will be. The larger the I difference between the more developed countries and the less developed countries, the more serious the inequity.

<!-- b000246 | furniture | pages [14] -->
Team # 2204803

<!-- b000247 | furniture | pages [14] -->
Page 13 of 22

<!-- b000248 | heading | pages [14] -->
4.1 Funded by Nation

<!-- b000249 | prose | pages [14] -->
Asteroid mining is a cooperative economic activity between countries. Labour needed for mining and production is mainly provided by less-developed countries, while more-developed ones provide mainly ﬁnancial and technical support. After that, rough processing is carried out in less developed countries with lower technical difﬁ- culty, and then it is transported to more developed countries for further processing and sales, and the proﬁts from sales are divided between the two countries. The interests of both parties will be used for national construction, and there will be no monopoly or oligopoly concentrating most resources in this industry. Social construction will get better development, and the overall economic level and living standard of the people will be improved.

<!-- b000250 | prose | pages [14] -->
• National income per capita (Civ1): The development of asteroid mining could affect per capita income by opening up a completely different new market, cre- ating more new jobs, and transforming more related industries. But at the same time, while the new industry brings opportunities, it also brings risks, and it is based on an existing mining industry rather than a completely new one, so it will not raise the industry ceiling much. So we think big and small countries will both get "moderate impact", but there is still the potential for "signiﬁcant impact".

<!-- b000251 | prose | pages [14] -->
• R&D spending (Civ2): Spending on research and development will be signiﬁ- cantly affected in larger, more-developed countries that have the technology to conduct asteroid mining operations and then do much more science than less developed countries. Less-developed countries are mostly unable to carry out space exploration activities and lack follow-up scientiﬁc research capacity, but research in related ﬁelds will also be carried out, so they are moderately affected.

<!-- b000252 | prose | pages [14] -->
• Capital formation per capita (Eco1): An increase in per capita income causes an increase in assets held per capita, so capital per capita is affected roughly as much as income per capita. Capital formation per capita: An increase in per capita in- come causes an increase in assets held per capita, so capital per capita is affected roughly as much as income per capita.

<!-- b000253 | prose | pages [14] -->
• National income per capita (Eco2): The development of asteroid mining could affect per capita income by opening up a completely different new market, cre- ating more new jobs, and transforming more related industries. But at the same time, while the new industry brings opportunities, it also brings risks, and it is based on an existing mining industry rather than a completely new one, so it will not raise the industry ceiling much. So we think big and small countries will both get "moderate impact", but there is still the potential for "signiﬁcant impact".

<!-- b000254 | prose | pages [14] -->
• Proportion of people living in absolutely poverty (Eco3): More-developed coun- tries have less poverty and are therefore less affected. Asteroid mining has been able to reduce poverty to some extent by driving economic development and providing jobs for more people, but it has not been able to make a big difference, so smaller, less developed countries get "moderate impact".

<!-- b000255 | prose | pages [14] -->
• Proportion of the primary and secondary industries (Eco4): Similar to the above, the achievements of asteroid mining will impact the development of existing tra- ditional primary and secondary industries, but will not cause a huge change.

<!-- b000256 | furniture | pages [15] -->
Team # 2204803

<!-- b000257 | furniture | pages [15] -->
Page 14 of 22

<!-- b000258 | prose | pages [15] -->
Those in more developed countries are already more mature and will not be af- fected much, and the less developed countries will be affected moderately.

<!-- b000259 | prose | pages [15] -->
• Nitrous oxide emission s(Env1): The resources derived from asteroid mining are likely to revolutionize the energy industry, but cannot replace existing energy sources on a large scale, so the resulting ﬂuctuations are limited and we charac- terize them as "moderate impact".

<!-- b000260 | prose | pages [15] -->
• Share of nonrenewable energy generation (Env2): Resources derived from as- teroid mining are likely to drive innovation in the energy industry, but we con- sider it a "moderate impact" because of the high transport and development costs, and the long time required to move from research to large-scale deployment.

<!-- b000261 | prose | pages [15] -->
• Proportion of urban population (Soc4): Because more developed countries al- ready have high levels of urbanization, they are less affected. For less developed countries, asteroid mining drives the development of a series of related indus- tries, which will improve the level of national industrialization, thus affecting the degree of urbanization and increasing urban population. However, as pri- vate enterprises lead the development, we believe that the impact is limited, so it is deﬁned as having a moderate impact.

<!-- b000262 | prose | pages [15] -->
• Other indicators: Including Military spending (Gov1), Strength of legal rights Index (Gov2), Infants’ death rate (Soc1), Intentional homicide victims (Soc2), Out- of-pocket expenditure per capita (Soc3), Residents’ average lifespan (Soc5). We don’t think the mining industry has much to do with those above, so it has almost no impact on them.

<!-- b000263 | prose | pages [15] -->
In summary, the single-factor fuzzy evaluation matrix R1 for more-developed coun- tries is matrix 11 and R2 for less-developed countries is 12:

<!-- b000264 | prose | pages [15, 16] -->
  0.7 0.3 0 0 0   0.3 0.7 0 0 0 0 0.3 0.7 0 0 0.3 0.7 0 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 R1 = 0.7 0.3 0 0 0 (11) 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0 0 0 0.7 0.3 0 0 0 0.7 0.3 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0   0.3 0.7 0 0 0   0.3 0.7 0 0 0 0 0.3 0.7 0 0 0.7 0.3 0 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 R2 = 0 0.7 0.3 0 0 (12) 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0 0 0.7 0.3 0 0 0 0.7 0.3 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0

<!-- b000265 | furniture | pages [16] -->
Team # 2204803

<!-- b000266 | furniture | pages [16] -->
Page 15 of 22

<!-- b000268 | prose | pages [16] -->
Selecting the trapezoidal distribution as membership function, we can get the ﬁnal comprehensive evaluation matrix Bi = A · Ri : [ ] B1 = A · R1 = 0.234 0.462 0.233 0.050 0.021 [ ] B2 = A · R2 = 0.237 0.571 0.192 0.050 0.021

<!-- b000269 | prose | pages [16] -->
Assigning a score to B1 and B2, we can ﬁnally get the impact value of more- and less-developed countries under the condition of state funding IM1 = 2.332, IM2 = 2.312.

<!-- b000270 | heading | pages [16] -->
4.2 Funded by Private Enterprise

<!-- b000271 | prose | pages [16] -->
Next, we will change the conditions and discuss the global equity implications of privately funded asteroid mining. The private enterprise here is multinational, which means it produces and processes in less developed countries and uses local labor, so it does not provide many jobs in more developed countries, but accounts for most of the proﬁts. Unlike government investment, private companies tend to concentrate the majority’s wealth by a few people, pay less attention to social construction and public interests, and have little technical support.

<!-- b000272 | prose | pages [16] -->
• National income per capita (Civ1): Similar to state funding, new resources can increase national income by opening up new markets and creating new jobs.

<!-- b000273 | prose | pages [16] -->
However, it does not produce disruptive changes, so they are deﬁned as "moder- ate impact".

<!-- b000274 | prose | pages [16] -->
• R&D spending (Civ2): Since it is run by private enterprises, we believe that the scale of their research will be smaller than that funded by the state, and the in- vestment will also be less, so we think it will have a moderate impact on R&D expenditure in more developed countries. In less developed countries, the pri- vate sector is weak and it is not easy to carry out large-scale, high-level research, so we think the impact is small.

<!-- b000275 | prose | pages [16] -->
• Capital formation per capita (Eco1): An increase in per capita income causes an increase in assets held per capita, so capital per capita is affected roughly as much as income per capita.

<!-- b000276 | furniture | pages [17] -->
Team # 2204803

<!-- b000277 | furniture | pages [17] -->
Page 16 of 22

<!-- b000278 | prose | pages [17] -->
• National income per capita (Eco2): Similar to state funding, new resources can increase national income by opening up new markets and creating new jobs.

<!-- b000279 | prose | pages [17] -->
However, it does not produce disruptive changes, so they are deﬁned as "moder- ate impact".

<!-- b000280 | prose | pages [17] -->
• Proportion of people living in absolutely poverty (Eco3): Similar to state fund- ing, more-developed countries have relatively little poverty and are therefore less affected. The economic impact of asteroid mining can reduce poverty to some ex- tent, but not dramatically, so less-developed countries get a "moderate impact".

<!-- b000281 | prose | pages [17] -->
• Proportion of the primary and secondary industries (Eco4): Similar to the state funding situation, the primary and secondary industries of the more developed countries, which are already mature, will not be affected much, while the less developed countries will be moderately affected.

<!-- b000282 | prose | pages [17] -->
• Nitrous oxide emissions (Env1): The resources derived from asteroid mining are likely to stimulate innovation in the energy industry, but cannot replace existing energy sources on a large scale, so the impact on the more developed countries is limited and we characterize it as a "moderate impact". Less developed countries bear the burden of pollution from the production lines of big countries, so we think the impact on them will be greater.

<!-- b000283 | prose | pages [17] -->
• Share of nonrenewable energy generation (Env2): Resources derived from as- teroid mining are likely to drive innovation in the energy industry, but we con- sider it a "moderate impact" because of the high transport and development costs, and the long time required to move from research to large-scale deployment.

<!-- b000284 | prose | pages [17] -->
• Proportion of urban population (Soc4): Because more developed countries al- ready have high levels of urbanization, they are less affected. For less developed countries, asteroid mining drives the development of a series of related indus- tries, which will improve the level of national industrialization, thus affecting the degree of urbanization and increasing urban population. However, as pri- vate enterprises lead the development, we believe that the impact is limited, so it is deﬁned as having a moderate impact.

<!-- b000285 | prose | pages [17] -->
• Other indicators: Including Military spending (Gov1), Strength of legal rights Index (Gov2), Infants’ death rate (Soc1), Intentional homicide victims (Soc2), Out- of-pocket expenditure per capita (Soc3), Residents’ average lifespan (Soc5). We don’t think the mining industry has much to do with those above, so it has almost no impact on them.

<!-- b000286 | prose | pages [17, 18] -->
In summary, the single-factor fuzzy evaluation matrix for more-developed coun- tries is matrix 13 and for less-developed countries is 14:

<!-- b000287 | furniture | pages [18] -->
Team # 2204803

<!-- b000288 | furniture | pages [18] -->
Page 17 of 22

<!-- b000290 | prose | pages [18] -->
  0.3 0.7 0 0 0   0.3 0.7 0 0 0 0 0.3 0.7 0 0 0.3 0.7 0 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 R3 = 0 0.3 0.7 0 0 (13) 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0 0 0.7 0.3 0 0 0 0.7 0.3 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0

<!-- b000291 | prose | pages [18] -->
  0.3 0.7 0 0 0   0.3 0.7 0 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0 R4 = 0.3 0.7 0 0 0 (14) 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0.3 0.7 0 0 0 0.3 0.7 0 0 0 0.3 0.7 0 0

<!-- b000292 | prose | pages [18] -->
Selecting the trapezoidal distribution as membership function, we can get the ﬁnal comprehensive evaluation matrix Bi = A · Ri : [ ] B3 = A · R3 = 0.202 0.474 0.253 0.050 0.021 [ ] B4 = A · R4 = 0.149 0.477 0.302 0.021 0.050

<!-- b000293 | prose | pages [18] -->
Assigning a score to B3 and B4, we can ﬁnally get the inﬂuence value of developed and less developed countries under the condition of state funding IM3 = 2.003, IM4 = 1.708.

<!-- b000294 | heading | pages [18] -->
4.3 Impacts Asteroid Mining Brings to Global Equity

<!-- b000295 | prose | pages [18] -->
Through the above calculation, we can draw the following two conclusions:

<!-- b000296 | heading | pages [18] -->
1. IM1 > IM3,

<!-- b000297 | prose | pages [18] -->
IM2 > IM4 It shows that state-funded asteroid mining activities bring more beneﬁts to both more- and less-developed countries than those funded by private enterprises.

<!-- b000298 | furniture | pages [19] -->
Team # 2204803

<!-- b000299 | furniture | pages [19] -->
Page 18 of 22

<!-- b000300 | heading | pages [19] -->
2. IM1 −IM2 = ∆IM12,

<!-- b000301 | prose | pages [19] -->
IM3 −IM4 = ∆IM34, ∆IM12 > ∆IM34 It shows that the gap between more-developed and less-developed countries caused by state-funded asteroid mining activities is smaller than that caused by private enterprises.

<!-- b000302 | prose | pages [19] -->
From conclusion 1 and 2, we can get that state-sponsored asteroid mining can pro- mote global equity, which is consistent with what we know to be true.

<!-- b000303 | prose | pages [19] -->
State-funded projects focus more on aid, with strong countries providing techni- cal assistance and leading less-developed countries in development. When asteroid mining is jointly funded by multiple countries, it will be like a planned economy. The output is regulated by the government’s macro-control. Following production and re- search will be according to the contract signed by governments before the cooperation. Most of the revenue earned from the sale of raw minerals and goods made of them is gained by the government and then redistributed. Therefore, in both countries, jobs and development opportunities for the working class and small producers can be pro- vided. It will also reduce the unemployment rate effectively, directly promote domestic consumption and enhance economic vitality. During the cooperation, less-developed countries will also get a share of the proﬁts from mining, be paid for their labor, and be able to import productions at cheaper prices.

<!-- b000304 | prose | pages [19] -->
In addition to the economic boost, government-funded asteroid mining will at- tend greater signiﬁcance to scientiﬁc research on asteroid minerals, from which less- developed countries can also beneﬁt in the aspect of science technology.

<!-- b000305 | prose | pages [19] -->
Meanwhile, when the asteroid mining industry is funded by multinational compa- nies, considering the technology and cost required by asteroid mining, only a few large multinational companies are capable of mining and subsequent production. Thus the market will be an imperfect competitive market, either an oligopolistic or a monopo- listic competition market, thus weak countries won’t be able to share technology or get project results. The private companies will put corporate proﬁts in the ﬁrst place. In order to save costs, companies will locate plant and equipment in countries with low labor costs. Consequently, the development of asteroid-mining will not boost employ- ment domestically. At the same time, the characteristics of high-threshold provokes suppress the entry of small enterprises. Thus, asteroid mining proﬁts will be most oc- cupied by oligopoly or monopoly. Although it is true that the industry development will improve the overall GDP and income per capita, the growth is primarily caused by making the rich richer, having little impact on the others, thus the social gap between rich and poor will be enlarged.

<!-- b000306 | heading | pages [19] -->
5 Policies Could Be Implemented

<!-- b000307 | prose | pages [19] -->
Considering that in task 1, economy and civilization have greater impact on global equity, and that the development of science and technology is the main part of the civi- lization, we pay more attention to promoting equity in these two areas when formulat- ing policies. We highly recommend that the United Nation should establish a relevant asteroid mining department to supervise asteroid mining and subsequent production.

<!-- b000308 | furniture | pages [20] -->
Team # 2204803

<!-- b000309 | furniture | pages [20] -->
Page 19 of 22

<!-- b000310 | heading | pages [20] -->
5.1 Economic Aspects

<!-- b000311 | prose | pages [20] -->
Asteroids should not become new colonies for a few countries, and any attempt to colonize them should be severely condemned and stopped.

<!-- b000312 | prose | pages [20] -->
We encourage cooperation between technologically advanced countries and less advanced countries, and stipulates that a certain proportion of mining conducted by technologically advanced countries should be cooperated with developing countries. The policy aims to ensure that poor countries have a certain degree of participation in the asteroid mining project and get certain beneﬁts, which is conducive to promoting the economic development of both developed and poor countries, and can also pre- vent the gap between the rich and the poor country from widening by restraining the monopoly of developing countries.

<!-- b000313 | prose | pages [20] -->
In international cooperation, the country providing labor should be counted as a partner, instead of just an employee, that is to say, it should participate in the dis- tribution of the end beneﬁts. This policy aims to protect the legitimate interests of weak countries in international cooperation and reduce the possibility of exploitation to labor-intense country.

<!-- b000314 | prose | pages [20] -->
Countries are allowed to license certain mining projects to private companies, but the amount of license should be limited. In view of the different impacts on global equity by different investors in task 2 and 3, the asteroid mining project with national fund as the dominant part and with international cooperation is more conducive to promoting global equity. Therefore, we suggest that relevant work be led by the gov- ernment. However, in view of the disadvantages that fully planned economy may have as mentioned above, enterprise participation, to some extents, is necessary.

<!-- b000315 | prose | pages [20] -->
In order to facilitate the efﬁciency of international trade markets, countries involved should reduce tariffs on asteroid mining related industries. The trade of raw, reﬁned minerals and subsequent products should be unlimited and unimpeded. Countries should not restrict or hinder the international trade of products on the grounds of trade protection. The policy aims to provide a larger scale of market for the countries involved and promote the prosperity and development of the whole asteroid mining industry.

<!-- b000316 | prose | pages [20] -->
Asteroid mining should be based on the premise of peace, and all economic losses caused by violent acts should be borne by the country that starts the violence, and compensation should be made for the losses. The policy is intended to allow asteroid mining to proceed without the threat of violence. A peaceful and stable environment will promote cooperation between countries and guarantee the stable development of relevant industries.

<!-- b000317 | heading | pages [20] -->
5.2 Civilization Aspects

<!-- b000318 | prose | pages [20] -->
Some of the resources from asteroid mining should be used for scientiﬁc research. Considering the important role of science and technology in social progress, mineral resources for research should be guaranteed to promote the continuous progress of the industry as a whole.

<!-- b000319 | prose | pages [20, 21] -->
In cooperation, technologically advanced countries are obliged to provide certain technical support to poor countries, and technological communications between coun- tries are encouraged. The policy aims to reduce the gap between countries due to sci- entiﬁc and technological gaps, and to a certain extent provides convenient conditions for technological progress in poor countries. At the same time, advances in technology in poor countries could increase the efﬁciency of international cooperation and boost the asteroid mining industry.

<!-- b000320 | furniture | pages [21] -->
Team # 2204803

<!-- b000321 | furniture | pages [21] -->
Page 20 of 22

<!-- b000323 | prose | pages [21] -->
Any actions that limit the free mobility of visiting scholars or students among coun- tries for reasons of protecting core skills is not supported. Technology monopolies are serious impediment to global equity and reinforce development gaps among coun- tries. In order to prevent the emergence of technology monopoly, we should prohibit the occurrence of detention of talents.

<!-- b000324 | prose | pages [21] -->
In principle, there should be some concessions for the use of new intellectual prop- erty generated by the development of the asteroid mining industry. The policy aims to promote the communications of knowledge among countries and promotes common progress. At the same time, according to EWM model, the reduction of intellectual property royalties will effectively promote development of civilization and global eq- uity.

<!-- b000325 | prose | pages [21] -->
In all mining and subsequent production processes, the accident rate needs to be controlled. The technology-providing country is obligated to guarantee the safety of the overall project. All safety incidents caused by technical immaturity shall be borne by the technology-providing country. This policy is designed to protect the safety of workers and reduce the occurrence of accidents.

<!-- b000326 | prose | pages [21] -->
Space debris generated during asteroid mining should be properly disposed of. Asteroids belong to the common property of mankind, and any country or company should pay attention to relevant environmental protection and ensure their sustainable development when mining them.

<!-- b000327 | heading | pages [21] -->
5.3 Industry Aspects

<!-- b000328 | prose | pages [21] -->
Mineral industry chain mainly consists of four parts: basic geology and theoretical work research; prospecting; mining; raw ore processing. The content of the ﬁrst two sectors will be mainly carried out by countries with mature technology. Next step will not be taken until sufﬁcient preliminary studies have been carried out in these countries to conﬁrm the feasibility of mining operations.

<!-- b000329 | prose | pages [21] -->
The previous policy requires the government to guarantee a certain amount of in- ternational cooperation. If the government chose not to do so, the mining project would either funded by the government or by private companies that have bought the mining right from the government. If the government chooses international co- operation, it will choose partners among treaty-involved countries, usually countries with relatively less advanced technology but abundant labors.

<!-- b000330 | prose | pages [21] -->
The speciﬁc mining process is divided into two parts: transportation and space mining. The technical support needed for transportation and mining will be provided by technologically advanced countries, and the labor needed for asteroid mining will be provided by countries with abundant labor resources. It is a similar story for private companies. Considering cost issues, companies choose to hire workers in countries where labor costs are relatively low. In the case of investment by a single national government, both technology and labor are provided domestically.

<!-- b000331 | prose | pages [21, 22] -->
Raw ore processing is entrusted by countries with abundant technology or capital to countries or regions with abundant energy and labor. By investing in factories and employing labor in those countries and regions, it can not only help developed coun- tries reduce production costs, but also promote the development of local economy. The concentrate produced, in addition to those transport back to developed countries for following production, other will directly ﬂow into the international trade market.

<!-- b000332 | furniture | pages [22] -->
Team # 2204803

<!-- b000333 | furniture | pages [22] -->
Page 21 of 22

<!-- b000335 | heading | pages [22] -->
6 Sensitive Analysis

<!-- b000336 | caption | pages [22] -->
Figure 6: Sensitive Analysis

<!-- b000337 | prose | pages [22] -->
In this sector, we tested the sensitivity of the model in task 1 mainly by changing the variance of important indicators.

<!-- b000338 | prose | pages [22] -->
When we increased the variance of military spending, capital formation per capita, R&D spending, national income per capita and higher education enrollment rate re- spectively, we could get the weight change rate of these indicators by re-using EWM model mentioned in task 1. We could ﬁnd that, among these important indicators, only the weight of military spending decreases with the increase of variance. For the other four indicators, the greater the difference among countries, the greater the explanatory power for development level.

<!-- b000339 | heading | pages [22] -->
7 Strengths and Weaknesses

<!-- b000340 | heading | pages [22] -->
7.1 Strengths and Importance

<!-- b000341 | prose | pages [22] -->
• Close to reality. We have divided the factors that may affect the development degree and future development potential of a country into ﬁve categories, and selected more than two important indicators for each sector. Therefore, it can be considered that our model better simulates the reality. At the same time, we have selected more than 100 countries and regions from all over the world, which is a good reﬂection of equity at the global level.

<!-- b000342 | prose | pages [22] -->
• The possibility of data inaccuracy has been considered. In the sensitivity analysis, we took into account that the data may have some discrepancies, and tested some most important indicators.

<!-- b000343 | prose | pages [22] -->
• We assumed not only possible mineral production chains in the future and make policy recommendations in this regard, but also the situation of the production chain integrally, and put forward relevant suggestions for each part.

<!-- b000344 | furniture | pages [23] -->
Team # 2204803

<!-- b000345 | furniture | pages [23] -->
Page 22 of 22

<!-- b000346 | prose | pages [23] -->
• The model explained the fact well. We examine the trend towards equity in Eu- rope over the past 30 years and ﬁnd it consistent with reality. At the same time, by studying the trends of different indicators, conclusions consistent with intu- ition and common sense are also drawn.

<!-- b000347 | heading | pages [23] -->
7.2 Weaknesses and Improvements

<!-- b000348 | prose | pages [23] -->
• Although we try our best to collect data from all countries in the world, there are still a number of data missing in some countries and regions due to the limita- tions of databases, which has a certain negative impact on the accuracy of global results.

<!-- b000349 | prose | pages [23] -->
• At present, there is not enough information about the possible impact of future asteroid mining on various indicators, and the following calculation of relevant indicators need to wait for the veriﬁcation of future practice.

<!-- b000350 | heading | pages [23] -->
8 Conclusion

<!-- b000351 | prose | pages [23] -->
We present a model for measuring global equity that takes into account all aspects of a country. At the same time, we analyze and predict what impacts asteroid min- ing will have on the global equity pattern under the conditions of different funding entities, demonstrate the difference of impacts brought by state-led and private-led enterprises, and put forward feasible policies from different aspects.

<!-- b000352 | heading | pages [23] -->
References

<!-- b000353 | references | pages [23] -->
[1] The Treaty on Principles Governing the Activities of States in the Exploration and

<!-- b000354 | references | pages [23] -->
Use of Outer Space, including the Moon and other Celestial Bodies, of 27 January

<!-- b000355 | references | pages [23] -->
1967, United Nations RES 2222 (XXI).

<!-- b000356 | references | pages [23] -->
[2] Mining - Wikipedia, from https://en.m.wikipedia.org/wiki/Mining#Industry

<!-- b000357 | references | pages [23] -->
[3] Monopoly - Wikipedia, from https://en.m.wikipedia.org/wiki/Monopoly

<!-- b000358 | references | pages [23] -->
[4] Oligopoly - Wikipedia, from https://en.m.wikipedia.org/wiki/Oligopoly

<!-- b000359 | references | pages [23] -->
[5] World Bank Open Data | Data, from https://data.worldbank.org.cn/

<!-- b000360 | references | pages [23] -->
[6] Our World in Data, from https://ourworldindata.org/

<!-- b000361 | references | pages [23] -->
[7] UNdata, from https://data.un.org/

<!-- b000362 | references | pages [23] -->
[8] Nincic, Miroslav, and Thomas R. Cusack. "The political economy of US military

<!-- b000363 | references | pages [23] -->
spending." Journal of Peace research 16.2 (1979): 101-115.

<!-- b000364 | references | pages [23] -->
[9] Delgado A, Romero I. Environmental conﬂict analysis using an integrated grey

<!-- b000365 | references | pages [23] -->
clustering and entropy-weight method: A case study of a mining project in

<!-- b000366 | references | pages [23] -->
Peru[J]. Environmental Modelling Software, 2016, 77: 108-121.
