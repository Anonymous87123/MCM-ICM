# P-B-2018-79002-238b850f

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
79002

<!-- b000006 | prose | pages [1] -->
T1

<!-- b000007 | prose | pages [1] -->
F1

<!-- b000008 | prose | pages [1] -->
T2

<!-- b000009 | prose | pages [1] -->
F2

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3

<!-- b000012 | prose | pages [1] -->
F3

<!-- b000013 | title | pages [1] -->
B

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
T4

<!-- b000016 | prose | pages [1] -->
2018

<!-- b000017 | prose | pages [1] -->
MCM/ICM How many languages? To predict the number of the one language, we assume that native speakers are related to natural growth rate of its native speaker and number of the its second speakers. Based on the data we collected, we use time series languages speakers difference equation model to describe the dynamic change of both native and second language speakers, considering the influence of foreign language taught in school, social media, economics, cultural communication and so on.

<!-- b000018 | prose | pages [1] -->
The difference equation model can apply our collected indicators to the prediction of change of language distribution over time. 50 years later, top 10 languages in order of total speakers change from [Mandarin, English, Hindustani, Spanish, Arabic, Malay,Russian, Bengali, Portuguese French] to [Mandarin ,English, Spanish, Hindustani,Arabic, Bengali, Portuguese, Malay, Russian, French]; the rank of top 10 native languages speakers changes from [Mandarin, Spanish, English, Hindustani,Arabic, Bengali, Portuguese, Russian, Punjabi, Japanese] to [Mandarin, Spanish, English, Hindustani, Arabic, Bengali, Portuguese, Punjabi, Russian and Hausa]. By analyzing these changes, we find some reasonable explanations, such as the rapid natural growth rate of some developing countries and some languages’ increasingspeaking-power.

<!-- b000019 | prose | pages [1] -->
Given the global population growth and migration pattern, we establish geographical distribution of difference equation model, to predict the geographical distribution of different languages. Through the establishment of the difference equation, we consider the relationship between the distribution of languages on different continents and main migration routes. We use MATLAB to calculate language proportion changes on each continent over the next 50 years, finding some reasonable predictions. For example, Mandarin will become the No.2 native language in North America and Australia. The proportion of Mandarin and Arabic speakers in Europe will increase significantly.

<!-- b000020 | prose | pages [1] -->
In Part II, based on the requirement and the feature of service company, we choose six suitable cities based on our prediction of language speakers. Also, we find that the cities are different depending on whether the company is long-term oriented (6 suggested cities: Shanghai, New York, Calcutta, Madrid, Dubai, and Rio de Janeiro) or short-term oriented (6 cities: Shanghai, New York, Calcutta, Madrid, Dubai, and Singapore).

<!-- b000021 | prose | pages [1] -->
Moreover, we build the cost-benefit analysis model to calculate the suitable number of offices that this company should build. Given the level of company’s profitability and cost, we set a new parameter, cost-profitability ratio. If the value of c- p ratio is less than 281, we think 6 offices should be built. If the value of this ratio is between 281 and 422, we think 5 offices should be built. If the value is between 422-527, 4 offices are best; if it is between 527 and 544, 3 office should be built; if> 544, we should only maintain two offices.

<!-- b000022 | prose | pages [1] -->
Finally, we analyze the performance of our model and the sensitivity of our model, proving that our model is relatively stable for different parameters.

<!-- b000023 | keywords | pages [1] -->
Key words: Language distribution, Time Series Difference Equation Model, Dynamic simulation, site selection

<!-- b000024 | prose | pages [1] -->
Cost-profit analysis

<!-- b000025 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000026 | furniture | pages [2] -->
Team # 79002

<!-- b000027 | furniture | pages [2] -->
Page 1 of 29

<!-- b000028 | prose | pages [2] -->
CONTENT

<!-- b000029 | prose | pages [2] -->
1 Introduction................................................................................................................................................. 2 1.1 Problem Background....................................................................................................................2 1.2 Our work.......................................................................................................................................2

<!-- b000030 | prose | pages [2] -->
2 Assumptions and Symbols.......................................................................................................................... 2 2.1 Assumptions of the initial data.....................................................................................................2 2.2 Symbols and definitions............................................................................................................... 3

<!-- b000031 | prose | pages [2] -->
3 Part I Models and Results...........................................................................................................................4 3.1 Model I: Various Languages Speakers Difference Equation Model............................................4

<!-- b000032 | prose | pages [2] -->
3.1.1 The increase of the native speakers................................................................................................4

<!-- b000033 | prose | pages [2] -->
3.1.2 The increase of the second language speakers............................................................................... 5

<!-- b000034 | prose | pages [2] -->
3.1.3 The total difference equation of model I........................................................................................8 3.2 Model I Results & Analysis......................................................................................................... 8

<!-- b000035 | prose | pages [2] -->
3.2.1 Initial rank and parameter setting...................................................................................................8

<!-- b000036 | prose | pages [2] -->
3.2.2 Results & Analysis......................................................................................................................... 9 3.3 Model II: Geographical Distribution Difference Model............................................................ 10 3.4 Population growth fitting and current migration pattern............................................................11 3.5 The increase speakers of each language on each continent........................................................12 3.6 Result and Analysis....................................................................................................................13

<!-- b000037 | prose | pages [2] -->
4 Part II Models & Results.......................................................................................................................... 15 4.1 Assumptions about the service company................................................................................... 15 4.2 Explanation about our choices................................................................................................... 15

<!-- b000038 | prose | pages [2] -->
5 Sensitivity Analysis....................................................................................................................................17 5.1 sensitivity analysis of Model I....................................................................................................17 5.2 sensitivity analysis of model II...................................................................................................19

<!-- b000039 | prose | pages [2] -->
6 Strength and Weakness.............................................................................................................................20

<!-- b000040 | prose | pages [2] -->
7 Memo.......................................................................................................................................................... 21

<!-- b000041 | prose | pages [2] -->
8 Appendix.................................................................................................................................................... 22 8.1 data............................................................................................................................................. 22 8.2 program...................................................................................................................................... 24

<!-- b000042 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000043 | furniture | pages [3] -->
Team # 79002

<!-- b000044 | furniture | pages [3] -->
Page 2 of 29

<!-- b000045 | prose | pages [3] -->
1

<!-- b000046 | heading | pages [3] -->
Introduction

<!-- b000047 | heading | pages [3] -->
1.1 Problem Background

<!-- b000048 | prose | pages [3] -->
In the world of globalization, number of native speakers and L2 speakers of a certain language increase or decrease over time. There are many factors that affect the increase or decrease of a certain language, including the foreign language taught in school, cultural communication and assimilation, Economic Factor, technology, social media and so on.

<!-- b000049 | prose | pages [3] -->
Our first task is to establish a model of the distribution of various language speakers over time, in which we should consider the factor listed above.

<!-- b000050 | prose | pages [3] -->
Besides, our second task is the establish a model to predict the geographic distributions of these languages over time based on the given globe population and human migration patterns for the next 50 years.

<!-- b000051 | prose | pages [3] -->
In the part II, a large multinational service company hire our team to give location options for new offices. So our third task is to consider where we should locate these offices and if opening less than six offices better.

<!-- b000052 | heading | pages [3] -->
1.2 Our work

<!-- b000053 | prose | pages [3] -->
Language is such an important topic due to its role in cultural communication, international business, migration issue and so on. Under the circumstance that we are consulted to give out 6 most suitable sites to build new office by a service company, our main work is as follows:

<!-- b000054 | prose | pages [3] -->
Firstly, based on the data we collected, we use time series languages speakers difference equation model to describe the dynamic change of both native and second language speakers, considering the influence of foreign language taught in school, social media, economics, cultural communication and so on.

<!-- b000055 | prose | pages [3] -->
Secondly, considering the global population growth model and migration patterns, we establish geographical distribution difference model, presenting the change of languages’ distribution in 6 main continents over 50 years.

<!-- b000056 | prose | pages [3] -->
Thirdly, we choose the six suitable cities based on our prediction of language speakers. Also, we find that the cities are different depending on whether the company is long-term oriented or short-term oriented.

<!-- b000057 | prose | pages [3] -->
Moreover, we build the cost-benefit analysis model to calculate the suitable number of offices that this company should build.

<!-- b000058 | prose | pages [3] -->
Finally, we analyze the performance of our model and the sensitivity of our model.

<!-- b000059 | prose | pages [3] -->
2

<!-- b000060 | heading | pages [3] -->
Assumptions and Symbols

<!-- b000061 | prose | pages [3] -->
2.1

<!-- b000062 | heading | pages [3] -->
Assumptions of the initial data

<!-- b000063 | heading | pages [3] -->
1. Those languages whose current total speakers are less than 100 million won’t become the top 10

<!-- b000064 | prose | pages [3] -->
languages. Thus, according to the list of languages by total number of speakers, we only use the data of top 16 languages, since they are the only languages that are used by more than 100 million people.[1]

<!-- b000065 | prose | pages [3] -->
Reason: The French ranked 10th in 2017 with a total number of 228million speakers. According to common sense, total number of Language speakers have a small possibility to decrease. So, those languages with fewer than 100million speakers are less likely to become Top10 in 50 years. At the same time, we also do this to reduce our computational load and to reduce our programming difficulty.

<!-- b000066 | heading | pages [3] -->
2. For some Languages L2 speakers number ‘?’in the [1], we assume it is zero.

<!-- b000067 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000068 | furniture | pages [4] -->
Team # 79002

<!-- b000069 | furniture | pages [4] -->
Page 3 of 29

<!-- b000070 | prose | pages [4] -->
Reason: We speculate there may be two reasons for the coming of ‘?’. One is because the data is too small, not good statistics. The other reason is that it is controversial to define who can be the second foreign language speakers. For both reasons, we can all assume the number is zero.

<!-- b000071 | heading | pages [4] -->
3. We think native speaker's growth is only related to its own natural growth rate and second language

<!-- b000072 | prose | pages [4] -->
population

<!-- b000073 | prose | pages [4] -->
Reason: According to our common sense, the growth of native speakers is often associated with changes in the local population. Local population grow, native speakers also will grow. Foreigners migrate in, and the foreign language native speakers increase. Therefore, native speaker changes and population changes are very relevant. And in order to simply our model, we think native speaker's growth is only related to its own natural growth rate and second language population.[2]

<!-- b000074 | prose | pages [4] -->
4.We think L2 speaker’s growth is only affected by its own feature (the languages learned in school, cultural communication) and the global situation (economics, development of technology, media use). And the relationship between them is directly proportional.

<!-- b000075 | prose | pages [4] -->
Reason: According to common sense, these factors positively affects the L2 speaker’s growth. Although we are not quite sure whether the relationship between them is linear or not, in order to simplify the problem, we may think that the relationship between them is linear, and therefore,proportional.

<!-- b000076 | heading | pages [4] -->
2.2 Symbols and definitions

<!-- b000077 | caption | pages [4] -->
Table 2 codes for top 16 languages

<!-- b000078 | prose | pages [4] -->
i 1 2 3

<!-- b000079 | prose | pages [4] -->
Languages Mandarin English Hindustani

<!-- b000080 | prose | pages [4] -->
i 9 10 11

<!-- b000081 | prose | pages [4] -->
Languages Portuguese French Hausa

<!-- b000082 | prose | pages [4] -->
4 4 5 6 7 8

<!-- b000083 | prose | pages [4] -->
Spanish Arabic Malay Russian Bengali

<!-- b000084 | prose | pages [4] -->
12 12 13 14 15 16

<!-- b000085 | prose | pages [4] -->
Punjabi German Japanese Persian Swahili

<!-- b000086 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000087 | furniture | pages [5] -->
Team # 79002

<!-- b000088 | prose | pages [5] -->
3

<!-- b000089 | heading | pages [5] -->
Part I Models and Results

<!-- b000090 | furniture | pages [5] -->
Page 4 of 29

<!-- b000091 | heading | pages [5] -->
3.1 Model I: Various Languages Speakers Difference Equation Model

<!-- b000092 | prose | pages [5] -->
How to quantify the relationship between language growth and the various factors is a difficult problem? There are a variety of time series models we could use. If we have enough data, we can regress the functional relationship between the number of languages on various factors. But the truth is, we can’t find enough credible data online. There are two reasons for this. One is because it is vague to judge whether a person has a second foreign language ability. For this reason, different data sources may not come from the same criterion. So the data between the two will be very different. In addition, the two data whose sources are the same, while years are different are still not credible. This is because the dates of the censuses vary from country to country. This makes a lot of data does not have time continuity. For these two reasons, we can’t and will not use those methods of fitting forecasts.

<!-- b000093 | prose | pages [5] -->
Difference equation model can consider the impact of different factors on the size of the independent variables. Moreover, the difference equation model only requires the initial data on it. These two characteristics fit very well with our problem. The time step in which we set in the difference equation is one year. We denote that the number of native speakers of language i in next period depends on the current number of its native speakers and the current number of its 2nd language speakers. Therefore, we can construct a difference equation model to describe the change of 2 types speakers for the 16 languages.

<!-- b000094 | prose | pages [5] -->
3.1.1 The increase of the native speakers

<!-- b000095 | prose | pages [5] -->
According to our common sense, the growth of native speakers is often associated with changes in the local population. Local population grow, and native speakers also will grow. Foreigners migrate in, and the foreign language native speakers increase. Therefore, native speaker changes and population changes are very relevant. So, we assume that native speaker's growth is only related to its natural growth and the number of second language speakers. We choose the weighted average of natural growth rate of countries whose official language is the language i as the increase of the native speakers of language i.

<!-- b000096 | prose | pages [5] -->
However, the world population growth pattern varies from countries. The most significant difference is the difference between the population growth patterns in developing and developed countries. Therefore, we divide these languages into two group. One type is mainly spoken in developed countries, and the other is mainly spoken in the developing countries. Developed countries usually have low natural population growth rates and high immigration rate while developing countries usually have higher natural population growth rates. To take this difference into consideration, we divide all 16 languages into 2 types, according to their main speakers’ types—developed or developing.

<!-- b000097 | prose | pages [5] -->
types of languages Table 3

<!-- b000098 | prose | pages [5] -->
types

<!-- b000099 | prose | pages [5] -->
Type I: most spoken in developed countries

<!-- b000100 | prose | pages [5] -->
Type II: most spoken in developing countries

<!-- b000101 | prose | pages [5] -->
languages

<!-- b000102 | prose | pages [5] -->
English, Spanish, French, German, Japanese,

<!-- b000103 | prose | pages [5] -->
Mandarin

<!-- b000104 | prose | pages [5] -->
Hindustani, Arabic, Malay, Portuguese, Hausa,

<!-- b000105 | prose | pages [5] -->
Punjabi, Persian, Swahili

<!-- b000106 | heading | pages [5] -->
Type I languages’ speakers’ growth model: Malthusian growth model

<!-- b000107 | prose | pages [5] -->
Type I languages are mainly spoken in developed countries, whose population usually have a very low natural

<!-- b000108 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000109 | furniture | pages [6] -->
Team # 79002

<!-- b000110 | furniture | pages [6] -->
Page 5 of 29

<!-- b000111 | prose | pages [6] -->
growth rate, such as 0.5%, or even a negative value. Its population growth rate mainly depends on the immigration, while the next generation of those immigrants usually have to learn the local language as their mother tongue.

<!-- b000112 | prose | pages [6] -->
For this type countries, we can consider it as a constant rate, r, over the next 50 years. So we use the Malthusian growth model to measure the number of native speakers[4]. According to Malthusian growth model, the

<!-- b000113 | prose | pages [6] -->
ݔ݅(ݐ+ 1) −ݔ݅(ݐ) = ݔ݅(ݐ)ݎ݅+ ∙ݕ݅(ݐ)

<!-- b000114 | prose | pages [6] -->
population growth rate, r, does not change over time. Therefore, the population in year t+1 could be writtenas:

<!-- b000115 | prose | pages [6] -->
xi (t) denotes the number of native speakers of language i in year t; ri denotes the natural speaker growth rate

<!-- b000116 | prose | pages [6] -->
（1 ）

<!-- b000117 | prose | pages [6] -->
of language i; R denotes a coefficient that explains the proportion of 2nd speakers of this language in year t that turns into native speaker in year t+1. Later, we will do sensitivity analysis for this coefficient R.

<!-- b000118 | heading | pages [6] -->
Type II languages’ speakers’ growth model: Logistic Growth Model

<!-- b000119 | prose | pages [6] -->
Type II languages are mainly spoken in developing countries, whose population usually have a relatively higher natural growth rate, such as 2%. Nevertheless, we cannot use this number for the next 50 years, since their population cannot maintain growing so fast. To make a more realistic analysis, we use Logistic Growth Model. Logistic Growth Model is a slight modification of Malthus’s model. It points that the population growth rate is not constant—there is a limited carrying capacity of the environment, resulting in a stable population over time[5].

<!-- b000120 | prose | pages [6] -->
According to Logistic Growth Model, the population in year t+1 could be written as:

<!-- b000121 | prose | pages [6] -->
3.1.2 The increase of the second language speakers

<!-- b000122 | prose | pages [6] -->
When discussing the change of 2nd language speakers, we believe it is mainly affected by two major factors. Firstly, it is affected by its own feature, such as region, difficulty, promotion by the government, cultural communication, etc. Secondly, it is affected by the global situation, such as economics, development of technology, etc.

<!-- b000123 | prose | pages [6] -->
3.1.2.1 Effect of the language own features

<!-- b000124 | prose | pages [6] -->
the foreign language taught in school [3] 

<!-- b000125 | prose | pages [6] -->
We assume that the language promoted by the government is the foreign language taught in school. For example, English is taught in many countries as students’main foreign language because of English’s wide spread and use in the world. Although statistics are incomplete in some developing countries, we only found data of some developed countries. However, we think this promotion of language in education is related to the power of the language itself, which means the number of L2 speakers. Therefore, we use available data to make up for the missing data.

<!-- b000126 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000127 | furniture | pages [7] -->
Team # 79002

<!-- b000128 | furniture | pages [7] -->
Page 6 of 29

<!-- b000129 | prose | pages [7] -->
For example, when i refers to French and j refers to English, langTijis the percentage of French taught in school as a foreign language in English-speaking countries. k1 is the coefficient to measure how much i. Later we will do sensitivity analysis for k1. this factor (the language taught in school) will influence the increase of 2nd language speakers of language

<!-- b000130 | caption | pages [7] -->
Figure 1 The foreign language studied in school, taking U.S. for example[6]

<!-- b000131 | prose | pages [7] -->
Cultural communication & assimilation 

<!-- b000132 | prose | pages [7] -->
Many reports state that cultural communication and assimilation play a significant role in the increase of 2nd language learners. However, how to quantify cultural exchange is a very difficult issue. In order to solve this problem, we propose two factors that will affect cultural communication. The following are two effects:

<!-- b000133 | prose | pages [7] -->
Neighborhood Effect: If the speakers of two language live near to each other, it is more likely for them to have cultural communication. And therefore, they would become more likely to learn neighbors’ language as their 2nd language.

<!-- b000134 | caption | pages [7] -->
Figure 2 The neighborhood effect among the top 16 languages

<!-- b000135 | prose | pages [7] -->
( the two language having a line linked means there will be Neighborhood effect between them )

<!-- b000136 | prose | pages [7] -->
Policy-led Effect: When the home country of language speakers is strongly promoting the country's relations with some special countries, the likelihood of those languages learning from each other's languages will also increase, such as China's the Belt and Road Policy making it more motivated for the people along the policy to learn Chinese. For example, Pakistan uses Chinese as its second language.

<!-- b000137 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000138 | furniture | pages [8] -->
Team # 79002

<!-- b000139 | furniture | pages [8] -->
Page 7 of 29

<!-- b000140 | prose | pages [8] -->
The power of these two effect is positively related to the population of language speakers, xi(ݐ) ∙ݔ݆(ݐ), and the cultural communication between two languages. We get the following equation:

<!-- b000141 | prose | pages [8] -->
16 Δi,cult = k2 ∙∑퐶ｸ⎋ݐ݅,݆∙ݔ݅(ݐ) ∙ݔ݆(ݐ)

<!-- b000142 | prose | pages [8] -->
j=1

<!-- b000143 | prose | pages [8] -->
culti,j describes the extent of cultural exchange between language i and language j; k2 is the coefficient increase of 2nd language speakers of language i. Later we will do sensitivity analysis for k2. to measure how much this factor (the extent of cultural communication and assimilation) will influence the

<!-- b000144 | prose | pages [8] -->
3.1.2.2 Effect of the global situation

<!-- b000145 | prose | pages [8] -->
Economic Factor 

<!-- b000146 | prose | pages [8] -->
Different languages have different speaking power in the global business environment. The more powerit has, the more persons choose to learn it. Through the GDP contributed by different languages [See Figure Δi,Eco = 푘3 ∙퐸th 3], we give different weight to the top 16 language.

<!-- b000147 | prose | pages [8] -->
Ecoi is the economic power of language i. k3 describes how much the economic factor motivates people to learn language i as their 2nd language. Later we will do sensitivity analysis for k3.

<!-- b000148 | caption | pages [8] -->
Figure 4 GDP contributed by language [7]

<!-- b000149 | prose | pages [8] -->
the update of translation software technology 

<!-- b000150 | prose | pages [8] -->
The development of technology will make it easier and faster to translate different languages. Weassume

<!-- b000151 | prose | pages [8] -->
the velocity of translation software’s update rate is constant. Therefore, it will have a negative impact on

<!-- b000152 | prose | pages [8] -->
Δi,Tech = k4c (c > 0, k4 < 0)

<!-- b000153 | prose | pages [8] -->
the number of 2nd language learners. This factor will influence the increase of L2 speakers of language i as:

<!-- b000154 | prose | pages [8] -->
C is the velocity of technology development. k4 describes the change of 2nd language learner influenced by the development of translation software. Later we will do sensitivity analysis for k4.

<!-- b000155 | prose | pages [8] -->
the push of network and social media 

<!-- b000156 | prose | pages [8] -->
Though there are thousands of languages all over the world, only 5% of them are used widely in the internet. 54.5% of all web content is still in English despite huge growth in users that do not understand English or who prefer to access content in their native languages. Due to analysis of the most popular 10 million websites by W3techs, after English, the most common languages are Russian (5.9%), German (5.7%), Japanese (5.0%), and Spanish (4.7%).[8]

<!-- b000157 | prose | pages [8] -->
Data also show us that the number of languages used by mainstream social medias, such as Facebook, Twitter and LinkedIn is limited to few languages.

<!-- b000158 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000159 | furniture | pages [9] -->
Team # 79002

<!-- b000160 | furniture | pages [9] -->
Page 8 of 29

<!-- b000161 | caption | pages [9] -->
Figure 5 languages in the internet (left) [9] & the pressure of mainstream website(right)[8]

<!-- b000162 | prose | pages [9] -->
Δi,Net = 푘5 ∙푁‸ݐ

<!-- b000163 | prose | pages [9] -->
We can express the power of language in the network as follows:

<!-- b000164 | prose | pages [9] -->
describes the power of language i in the internet. k5 describes the change of 2nd language learner influenced by the push of internet and social media. Later we will do sensitivity analysis for k5.

<!-- b000165 | prose | pages [9] -->
3.1.3

<!-- b000166 | heading | pages [9] -->
The total difference equation of model I

<!-- b000167 | heading | pages [9] -->
3.2 Model I Results & Analysis

<!-- b000168 | prose | pages [9] -->
3.2.1 Initial rank and parameter setting

<!-- b000169 | prose | pages [9] -->
In the section above, we build a difference equation model, which could predict the number of native speakers and second language speakers in the following years. We get the initial rank by total language speaker[1]. It represents the numbers of native speakers and second language speakers of different languages in 2017. And

<!-- b000170 | caption | pages [9] -->
Table 4 The initial rank by language size [1]

<!-- b000171 | prose | pages [9] -->
here is the initial data:

<!-- b000172 | prose | pages [9] -->
Rank Language L1speakers L1Rank

<!-- b000173 | prose | pages [9] -->
1 Mandarin 897 1

<!-- b000174 | prose | pages [9] -->
2 English 371 3

<!-- b000175 | prose | pages [9] -->
L2speakers L2Rank Total

<!-- b000176 | prose | pages [9] -->
193 4 1090

<!-- b000177 | prose | pages [9] -->
611 1 982

<!-- b000178 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000179 | furniture | pages [10] -->
Team # 79002

<!-- b000180 | prose | pages [10] -->
3 Hindustani 329 4

<!-- b000181 | prose | pages [10] -->
4 Spanish 436 2

<!-- b000182 | prose | pages [10] -->
5 Arabic 290 5

<!-- b000183 | prose | pages [10] -->
6 Malay 77 15

<!-- b000184 | prose | pages [10] -->
7 Russian 153 8

<!-- b000185 | prose | pages [10] -->
8 Bengali 242 6

<!-- b000186 | prose | pages [10] -->
9 Portuguese 218 7

<!-- b000187 | prose | pages [10] -->
10 French 76 17

<!-- b000188 | prose | pages [10] -->
11 Hausa 85 11

<!-- b000189 | prose | pages [10] -->
12 Punjabi 148 9

<!-- b000190 | prose | pages [10] -->
13 German 76 18

<!-- b000191 | prose | pages [10] -->
14 Japanese 128 10

<!-- b000192 | prose | pages [10] -->
15 Persian 60 25

<!-- b000193 | prose | pages [10] -->
16 Swahili 16 26

<!-- b000194 | furniture | pages [10] -->
Page 9 of 29

<!-- b000195 | prose | pages [10] -->
215 2 544

<!-- b000196 | prose | pages [10] -->
91 8 527

<!-- b000197 | prose | pages [10] -->
132 6 422

<!-- b000198 | prose | pages [10] -->
204 3 281

<!-- b000199 | prose | pages [10] -->
113 7 267

<!-- b000200 | prose | pages [10] -->
19 13 261

<!-- b000201 | prose | pages [10] -->
11 15 229

<!-- b000202 | prose | pages [10] -->
153 5 229

<!-- b000203 | prose | pages [10] -->
65 10 150

<!-- b000204 | prose | pages [10] -->
?

<!-- b000205 | prose | pages [10] -->
?

<!-- b000206 | prose | pages [10] -->
148

<!-- b000207 | prose | pages [10] -->
52 12 129

<!-- b000208 | prose | pages [10] -->
1 19 129

<!-- b000209 | prose | pages [10] -->
61 11 121

<!-- b000210 | prose | pages [10] -->
91 8 107

<!-- b000211 | prose | pages [10] -->
According to the data we collected in [1, 4-7, 9], we can set indices in the formula (4) and formula (5). The

<!-- b000212 | caption | pages [10] -->
Table 5 Indices setting

<!-- b000213 | prose | pages [10] -->
indices are given as follows:

<!-- b000214 | prose | pages [10] -->
k1 k2

<!-- b000215 | prose | pages [10] -->
1 1

<!-- b000216 | prose | pages [10] -->
Index

<!-- b000217 | prose | pages [10] -->
300 90000 value

<!-- b000218 | prose | pages [10] -->
L2 learner

<!-- b000219 | prose | pages [10] -->
Cultural

<!-- b000220 | prose | pages [10] -->
Explanation

<!-- b000221 | prose | pages [10] -->
condition

<!-- b000222 | prose | pages [10] -->
communication

<!-- b000223 | prose | pages [10] -->
k3 k4 k5

<!-- b000224 | prose | pages [10] -->
0.2 -0.3 0.2

<!-- b000225 | prose | pages [10] -->
Language’s

<!-- b000226 | prose | pages [10] -->
Language’s

<!-- b000227 | prose | pages [10] -->
Technology

<!-- b000228 | prose | pages [10] -->
power in

<!-- b000229 | prose | pages [10] -->
power in

<!-- b000230 | prose | pages [10] -->
factor

<!-- b000231 | prose | pages [10] -->
business

<!-- b000232 | prose | pages [10] -->
internet

<!-- b000233 | prose | pages [10] -->
These parameters in our various languages speakers difference equation model are given by our estimate. We will do sensitivity analysis for them to judge if the change of L2 speakers will be sensitive to these indices.

<!-- b000234 | prose | pages [10] -->
3.2.2

<!-- b000235 | heading | pages [10] -->
Results & Analysis

<!-- b000236 | caption | pages [10] -->
Table 6 The predicted rank by language size after 50 years, Unit: million

<!-- b000237 | prose | pages [10] -->
After inputting the initial value and indices in MATLAB, we got the new rank:

<!-- b000238 | prose | pages [10] -->
L1 rank rank Languages L1speakers

<!-- b000239 | prose | pages [10] -->
1 Mandarin 1119.9556

<!-- b000240 | prose | pages [10] -->
2 English 625.07569

<!-- b000241 | prose | pages [10] -->
3 Spanish 714.54914

<!-- b000242 | prose | pages [10] -->
4 Hindustani 437.73828

<!-- b000243 | prose | pages [10] -->
5 Arabic 410.4004

<!-- b000244 | prose | pages [10] -->
6 Bengali 337.48877

<!-- b000245 | prose | pages [10] -->
7 Portuguese 306.72269

<!-- b000246 | prose | pages [10] -->
8 Malay 121.75222

<!-- b000247 | prose | pages [10] -->
9 Russian 159.65859

<!-- b000248 | prose | pages [10] -->
10 French 109.24506

<!-- b000249 | prose | pages [10] -->
L2speakers L2 rank Total

<!-- b000250 | prose | pages [10] -->
1 1 397.2715 2 1517.227

<!-- b000251 | prose | pages [10] -->
3 3 752.60658 1 1377.682

<!-- b000252 | prose | pages [10] -->
2 2 232.09149 7 946.6406

<!-- b000253 | prose | pages [10] -->
4 4 322.65571 3 760.394

<!-- b000254 | prose | pages [10] -->
5 5 235.69087 5 646.0913

<!-- b000255 | prose | pages [10] -->
6 6 112.72084 13 450.2096

<!-- b000256 | prose | pages [10] -->
7 7 101.83735 14 408.56

<!-- b000257 | prose | pages [10] -->
11 11 269.89281 4 391.645

<!-- b000258 | prose | pages [10] -->
9 9 187.58738 8 347.246

<!-- b000259 | prose | pages [10] -->
13 13 234.28833 6 343.5334

<!-- b000260 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000261 | furniture | pages [11] -->
Team # 79002

<!-- b000262 | prose | pages [11] -->
11 Punjabi 226.42109

<!-- b000263 | prose | pages [11] -->
12 Hausa 133.98132

<!-- b000264 | prose | pages [11] -->
13 Persian 87.30792

<!-- b000265 | prose | pages [11] -->
14 German 81.926176

<!-- b000266 | prose | pages [11] -->
15 Japanese 121.48183

<!-- b000267 | prose | pages [11] -->
16 Swahili 26.054248

<!-- b000268 | furniture | pages [11] -->
Page 10 of 29

<!-- b000269 | prose | pages [11] -->
8 8 78.858666 15 305.2798

<!-- b000270 | prose | pages [11] -->
10 10 132.39229 10 266.3736

<!-- b000271 | prose | pages [11] -->
14 14 122.95997 12 210.2679

<!-- b000272 | prose | pages [11] -->
15 15 125.04862 11 206.9748

<!-- b000273 | prose | pages [11] -->
12 12 71.268763 16 192.7506

<!-- b000274 | prose | pages [11] -->
16 16 145.23578 9 171.29

<!-- b000275 | prose | pages [11] -->
The top ten of total speakers vary from Mandarin、English、Hindustani、Spanish、Arabic、Malay、Russian、 Bengali、Portuguese、French to Mandarin、English、Spanish、Hindustani、Arabic、Bengali、Portuguese、 Malay、Russian、French.

<!-- b000276 | prose | pages [11] -->
The top ten of native speakers vary from Mandarin、Spanish、English、Hindustani、Arabic、Bengali、Portuguese、 Russian、Punjabi、Japanese to Mandarin、Spanish、English、Hindustani、Arabic、Bengali、Portuguese、 Punjabi、Russian、Hausa.

<!-- b000277 | prose | pages [11] -->
Comparing the two rankings, we can draw 5 main conclusions:

<!-- b000278 | prose | pages [11] -->
The fast increase of Mandarin L2 speakers: As the official language of China, a typical representative of the fast-growing countries, Mandarin has attracted many people to choose it as their second language. At the same time, China has also adopted a series of exchange policies with other countries, such as the aid to Africa and the Belt and Road Policy, which has also enhanced the attractiveness of Chinese.

<!-- b000279 | prose | pages [11] -->
Russian total rank declines: due to the very low natural growth rate in Russia, Russian native speakers’ rank declines, directly leading the decline in Russian’s total rank.

<!-- b000280 | prose | pages [11] -->
Bengali total rank increase: Bangladesh has a large national population base and a high natural increase rate, resulting in a rapid increase in Bengali native speakers and its rank.

<!-- b000281 | prose | pages [11] -->
The list of top 10 languages only have an intra-group change: Because there is a huge gap between the 10th

<!-- b000282 | prose | pages [11] -->
language (French, total speakers:229 million) and the 11th language (Hausa, total speaker: 150 million). The gap doesn’t disappear completely over time. But we can see from Table 7 that the top 16 list changes during 50 years.

<!-- b000283 | prose | pages [11] -->
Native speaker of Japanese decline from the top 10 list: This is mainly because Japan's natural growth rate has been negative recently. In addition, Hausa in Africa has become the 10th largest native language speaker due to its rapid rate of natural increase

<!-- b000284 | heading | pages [11] -->
3.3 Model II: Geographical Distribution Difference Model

<!-- b000285 | prose | pages [11] -->
As the model above established, we have established a model to measure the speakers’ numbers of different languages over time. The model above quantifies the relationship between the trend of native speakers and second language speakers and School, migration of cultural group, economics, the use of translation technology and social media. But obviously, we did not consider the impact of geographical distribution on the language. The following model specifically addresses this issue.

<!-- b000286 | prose | pages [11] -->
However, how to put the geographical distribution into our model is a huge challenge. We did not know at the outset what amount of language should be used to measure the geographic distribution of languages. But as we looked up the data, we found that the language distribution across all continents varied greatly. Below is the language distribution in 2017:

<!-- b000287 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000288 | furniture | pages [12] -->
Team # 79002

<!-- b000289 | furniture | pages [12] -->
Page 11 of 29

<!-- b000290 | caption | pages [12] -->
Figure 6 Language distribution in 2017

<!-- b000291 | prose | pages [12] -->
Therefore, we divide Earth language data into six continents, and each different continent has a different language distribution. Then, based on the modeling ideas of the above model, we consider the natural increase of population on all continents on the one hand, and population migration across the other continents on the other hand. Then we create a difference equation for each language of each continent over time. This equation can consider the impact of the annual immigrant population on the local language and the local language's own internal growth, which is what we want.

<!-- b000292 | prose | pages [12] -->
The following section considers assumptions about the world's population growth and the pattern of migration.

<!-- b000293 | heading | pages [12] -->
3.4 Population growth fitting and current migration pattern

<!-- b000294 | prose | pages [12] -->
In the following section, we will fit the world's population data and find the main migration path of the world's population.

<!-- b000295 | prose | pages [12] -->
Although we can easily find the world demographic data from the World Bank[10] from 1960 to 2016, how to fit the 56-year data to make their errors smaller is still a problem. Wetried exponential fitting, polynomial fitting, logistic equation fitting and so on, and finally found that Gaussian function fitting the best. Below is our fitting effect and function expression.

<!-- b000296 | caption | pages [12] -->
Figure 7 The regression on the world demographic data

<!-- b000297 | prose | pages [12] -->
(ݐ−2069)⁄ N(t) = 1.058 ∗1011 ∗‸(

<!-- b000298 | prose | pages [12] -->
2

<!-- b000299 | prose | pages [12] -->
97.67)

<!-- b000300 | prose | pages [12] -->
N(t) denotes the world population in t years.

<!-- b000301 | prose | pages [12] -->
Current global migration model is very complicated. If we focus on the population transfer data in various

<!-- b000302 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000303 | furniture | pages [13] -->
Team # 79002

<!-- b000304 | furniture | pages [13] -->
Page 12 of 29

<!-- b000305 | prose | pages [13] -->
countries, we can easily fall into too many data and can’t get the result. So, in order to simplify the world migration pattern, we may wish to consider only major migration routes in the current world. Then we look for the main migration patterns, and the image below shows some of the routes we found.

<!-- b000306 | caption | pages [13] -->
Figure 8 Some main routes of global migration[11]

<!-- b000307 | prose | pages [13] -->
Based on the current global migration patterns, we propose to assume the following seven major migration routes. These seven migration routes are the most promising migration path we believe will be in the next 50 years. Based on the average annual data and our understanding of these routes, we make the following

<!-- b000308 | prose | pages [13] -->
7 main migration routes Table 8

<!-- b000309 | prose | pages [13] -->
assumptions as to the proportion of these seven routes in all the routes.

<!-- b000310 | prose | pages [13] -->
route details

<!-- b000311 | prose | pages [13] -->
1 China to US and Canada

<!-- b000312 | prose | pages [13] -->
2 China to EU

<!-- b000313 | prose | pages [13] -->
3 India to EU

<!-- b000314 | prose | pages [13] -->
4 West Asia to EU

<!-- b000315 | prose | pages [13] -->
5 north Africa to EU

<!-- b000316 | prose | pages [13] -->
proportion

<!-- b000317 | prose | pages [13] -->
20%

<!-- b000318 | prose | pages [13] -->
15%

<!-- b000319 | prose | pages [13] -->
15%

<!-- b000320 | prose | pages [13] -->
15%

<!-- b000321 | prose | pages [13] -->
15%

<!-- b000322 | prose | pages [13] -->
Latin America to US and Canada 6

<!-- b000323 | prose | pages [13] -->
7 China to Australia

<!-- b000324 | prose | pages [13] -->
15%

<!-- b000325 | prose | pages [13] -->
5%

<!-- b000326 | heading | pages [13] -->
3.5 The increase speakers of each language on each continent

<!-- b000327 | prose | pages [13] -->
Besides, the population of immigrants will have the next generation in the destination country. Because it is

<!-- b000328 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000329 | furniture | pages [14] -->
Team # 79002

<!-- b000330 | furniture | pages [14] -->
Page 13 of 29

<!-- b000331 | prose | pages [14] -->
difficult to measure the impact of this factor on the number of native speakers in that country, we assume that immigrants, and we set the index is k6. the annual growth of native speakers in local languages because of migration is proportional to the number of

<!-- b000332 | prose | pages [14] -->
Thus, we have the following difference equation:

<!-- b000333 | heading | pages [14] -->
3.6 Result and Analysis

<!-- b000334 | prose | pages [14] -->
We use MATLAB to calculate that difference equations. And the chart below is our result. In order to easily differentiate data changes on all continents, we specialized in converting data of different continents to pie charts.

<!-- b000335 | caption | pages [14] -->
Figure 9 The distribution of languages in 6 main continents in 2017.

<!-- b000336 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000337 | furniture | pages [15] -->
Team # 79002

<!-- b000338 | furniture | pages [15] -->
Page 14 of 29

<!-- b000339 | caption | pages [15] -->
Figure 10 The distribution of languages in 6 main continents in 2037

<!-- b000340 | caption | pages [15] -->
Figure 11 The distribution of languages in 6 main continents in2067

<!-- b000341 | prose | pages [15] -->
According to the above changes show, we could find:

<!-- b000342 | prose | pages [15] -->
1.

<!-- b000343 | prose | pages [15] -->
The distribution of languages in Africa, Australia, Asia and Latin America did not change much. This is because the linguistic changes in these two continents are mainly determined by the natural population growth. The mode of population migration has little effect on these two continents. (Although Africa is one of the immigrants’ exit points and Australia is one of the destinations for immigrants).

<!-- b000344 | prose | pages [15] -->
2.

<!-- b000345 | prose | pages [15] -->
The proportion of Mandarin and Spanish in the United States and Canada is on the rise. Portuguese native speakers appear and account for a certain percentage. This is because Route 1 brings a large number of Mandarin speakers to the United States and Canada, and Route 6 brings a large number of

<!-- b000346 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000347 | furniture | pages [16] -->
Team # 79002

<!-- b000348 | furniture | pages [16] -->
Page 15 of 29

<!-- b000349 | prose | pages [16] -->
Spanish and Portuguese speakers.

<!-- b000350 | prose | pages [16] -->
3.

<!-- b000351 | prose | pages [16] -->
Native speakers of Arabic, Mandarin, Hindi appear in Europe and continue to increase. However, due to the small number of immigrants, the proportion is still low. The language of Europe still contains a lot of varieties.

<!-- b000352 | prose | pages [16] -->
4

<!-- b000353 | heading | pages [16] -->
Part II Models & Results

<!-- b000354 | heading | pages [16] -->
4.1 Assumptions about the service company

<!-- b000355 | prose | pages [16] -->
Aservice company is a business that generates income by providing services instead of selling physical products. A good example of a service company is a public accounting firm. They earn revenues by preparing income tax returns, performing audit and asset services, and even doing bookkeeping work.[12]

<!-- b000356 | prose | pages [16] -->
Based on our understanding of the service company, we make the following assumptions about the location of the new international offices.

<!-- b000357 | prose | pages [16] -->
1.

<!-- b000358 | prose | pages [16] -->
The service company's profit is in direct proportion to the total number of languages it serves. The more languages it serves, the higher the profit it earns. This is also the main profit pattern of this service company.

<!-- b000359 | prose | pages [16] -->
2.

<!-- b000360 | prose | pages [16] -->
The offices should be located in the places where English is widely used , in consideration of the crucial role English plays in the communication between different branch offices.

<!-- b000361 | prose | pages [16] -->
3.

<!-- b000362 | prose | pages [16] -->
The offices tend to be located in a densely populated and easily accessible metropolitan area. That is, if there are two cities in the same language area, we prefer to choose a city with a large population and convenient traffic.

<!-- b000363 | heading | pages [16] -->
4.2 Explanation about our choices

<!-- b000364 | prose | pages [16] -->
There will not be major changes in language population in the short term. So, we refer to the number of language speakers in 2017 when considering the short-term site selection. The top-six used languages are Mandarin, English, Hindustani, Spanish, Arabic and Malay. The six locations are correspondingly Shanghai, New York, Calcutta, Madrid, Dubai, Singapore. The population density map and the locations of offices are shownbelow:

<!-- b000365 | caption | pages [16] -->
Figure 12 population density map and locations of 6 offices based on data in 2017

<!-- b000366 | prose | pages [16] -->
However, when we consider the site selection in the long term, we refer to the results of our model I. At this point, the top-six used languages have changed. They are Mandarin, English, Spanish, Hindustani, Arabid and

<!-- b000367 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000368 | furniture | pages [17] -->
Team # 79002

<!-- b000369 | furniture | pages [17] -->
Page 16 of 29

<!-- b000370 | prose | pages [17] -->
Bengali. However, due to its large population but underdeveloped economy in Bangladesh, the company's service projects lack local consumer groups. So, we consider the seventh language in the projected languages rankings –Portuguese. Therefore, we choose Shanghai, New York, Madrid, Calcutta, Dubai, and Rio de Janeiro to locate these offices, arranged in order.

<!-- b000371 | caption | pages [17] -->
Figure 13 population density map and locations of 6 offices based on data in 2067

<!-- b000372 | prose | pages [17] -->
As we can see in Figure 14, Singapore is replaced by Rio de Janeiro since the rapid growth of Portuguese speakers.

<!-- b000373 | prose | pages [17] -->
Based on our model from Part I, here are our results:

<!-- b000374 | prose | pages [17] -->
In the short term, we choose Shanghai, New York, Calcutta, Madrid, Dubai and Singapore to locate these international offices. The top-six used languages-- Mandarin, English, Hindustani, Spanish, Arabic and Malay would be spoken correspondingly in these offices.

<!-- b000375 | prose | pages [17] -->
In the long term, we choose Shanghai, New York, Madrid, Calcutta, Dubai, and Rio de Janeiro. Mandarin, English, Spanish, Hindustani, Arabid and Portuguese would be spoken correspondingly in these offices. Cost- Benefit Analysis Model

<!-- b000376 | prose | pages [17] -->
Whenever establishing a new office in a new location, the company will have a wider range of consumer groups, Benefit = Revenue −Cost equation, we need to clarify the source of company’s revenue R and cost C. and thus more revenue. But at the same time, building a new office also costs a lot. According to the general

<!-- b000377 | prose | pages [17] -->
Since English is a necessary language, we used the number of the most popular language speakers except English in that region, to judge the company's profitability when we set up our Cost-Benefit Analysis model. Here we give some Assumptions as follows:

<!-- b000378 | prose | pages [17] -->
R (Total Revenue) is positively related to the company’s profitability, which is α C (Total Cost) is a fix  number in each place. Weassume the cost of building a new office is a constant C.

<!-- b000379 | prose | pages [17] -->
Profit (cityi) = α ∙pop(cityi) −퐶

<!-- b000380 | prose | pages [17] -->
So, we have the equation:

<!-- b000381 | prose | pages [17] -->
Pop(cityi) is the number of speakers of top 10 languages except English in cityi. Because we use pop(cityi) to describe the power and popularity of language i, we could let the number of total speakers to roughly represent it.

<!-- b000382 | caption | pages [17] -->
Table 10 The most suitable cities

<!-- b000383 | prose | pages [17] -->
We have calculated the most suitable cities in 4.1. The rank is in Table 9

<!-- b000384 | prose | pages [17] -->
Rank 1 2 3 4 5 6

<!-- b000385 | prose | pages [17] -->
Madrid City Shanghai New York Calcutta Dubai Singapore

<!-- b000386 | prose | pages [17] -->
Note: 1. Shanghai and New York is the two office we already have.

<!-- b000387 | prose | pages [17] -->
2. Weuse the data collected in 2017 rather than the predicted value for 50 years later, because the company will construct the 6 new office now but not 50 years later.

<!-- b000388 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000389 | furniture | pages [18] -->
Team # 79002

<!-- b000390 | furniture | pages [18] -->
Page 17 of 29

<!-- b000391 | prose | pages [18] -->
company, which is the exact value of α and C, from the company to measure its profitability. To calculate the profit-maximize office amount, we need to ask some additional information from our client

<!-- b000392 | prose | pages [18] -->
For cityi, we have a judgement to determine whether we should set up an office here:

<!-- b000393 | prose | pages [18] -->
C/α measures the company’s ability to turn the cost into profit, we call it cost-profitability ratio, or c-p ratio

<!-- b000394 | prose | pages [18] -->
Given different value of C/α, we can give the following suggestions:

<!-- b000395 | prose | pages [18] -->
in short.

<!-- b000396 | caption | pages [18] -->
Table 11 How many offices should the company set up?

<!-- b000397 | prose | pages [18] -->
C-p ratio (unit: million) Number of offices

<!-- b000398 | prose | pages [18] -->
[544.982) 2

<!-- b000399 | prose | pages [18] -->
[527,544) 3

<!-- b000400 | prose | pages [18] -->
[422,527) 4

<!-- b000401 | prose | pages [18] -->
[281, 422) 5

<!-- b000402 | prose | pages [18] -->
[0, 281) 6

<!-- b000403 | prose | pages [18] -->
City

<!-- b000404 | prose | pages [18] -->
Shanghai, New York

<!-- b000405 | prose | pages [18] -->
Shanghai, New York, Madrid,

<!-- b000406 | prose | pages [18] -->
Shanghai, New York, Madrid, Calcutta

<!-- b000407 | prose | pages [18] -->
Shanghai, New York, Madrid, Calcutta, Dubai

<!-- b000408 | prose | pages [18] -->
Shanghai, New York, Madrid, Calcutta, Dubai,

<!-- b000409 | prose | pages [18] -->
Therefore, given the additional information of α and C, we can help the company to decide how many offices they should build.

<!-- b000410 | prose | pages [18] -->
5

<!-- b000411 | heading | pages [18] -->
Sensitivity Analysis

<!-- b000412 | heading | pages [18] -->
5.1 sensitivity analysis of Model I

<!-- b000413 | prose | pages [18] -->
Singapore

<!-- b000414 | prose | pages [18] -->
The purpose of our Model I was to get the change of Top10 language of the most native speakers and total speakers for the next 50 years. But if you use rankings as the dependent variable for our sensitivity analysis, we think the result we got must be insensitive, and the rank remain the same, because the Independent variables change little, and the rank is a discrete data. So we want to choose one of the model I’s result data as our other dependent variable. For example, we choose the number of Mandarin second language speakers in 50 years later as our observed variables. The following analysis is to consider the sensitivity of this variable under small changes in below parameters.

<!-- b000415 | heading | pages [18] -->
1. natural increase rate

<!-- b000416 | prose | pages [18] -->
Weenter different natural growth rates of Mandarin into the program, and we get different Mandarin L2 speakers

<!-- b000417 | caption | pages [18] -->
Table 12 Sensitivity analysis on natural increase rate

<!-- b000418 | prose | pages [18] -->
number. Here is the result:

<!-- b000419 | prose | pages [18] -->
natural increase rate of Mandarin

<!-- b000420 | prose | pages [18] -->
the number of Mandarin L2 speakers

<!-- b000421 | prose | pages [18] -->
sensitivity

<!-- b000422 | prose | pages [18] -->
0.34 0.44 0.54

<!-- b000423 | prose | pages [18] -->
386.34 397.27 403.18

<!-- b000424 | prose | pages [18] -->
0.093256475

<!-- b000425 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000426 | furniture | pages [19] -->
Team # 79002

<!-- b000427 | furniture | pages [19] -->
Page 18 of 29

<!-- b000428 | prose | pages [19] -->
The Sensitivity Index shown above means that when the natural increase rate increased by 1%, the number of Mandarin L2 speakers will in turn increase by 0.09%. So the variation of this index has minor influence on the

<!-- b000429 | heading | pages [19] -->
2. k1

<!-- b000430 | prose | pages [19] -->
results. k1 is the proportional coefficient of the second language growth rate and school learning rate. We enter different k1 into the program, and we get different Mandarin L2 speakers number. Here is the result:

<!-- b000431 | caption | pages [19] -->
Table 13 Sensitivity analysis on k1

<!-- b000432 | prose | pages [19] -->
k1

<!-- b000433 | prose | pages [19] -->
the number of Mandarin L2 speakers

<!-- b000434 | prose | pages [19] -->
sensitivity

<!-- b000435 | prose | pages [19] -->
0.0025 0.003333 0.005

<!-- b000436 | prose | pages [19] -->
383.14 397.27 410.5

<!-- b000437 | prose | pages [19] -->
0.104437788

<!-- b000438 | prose | pages [19] -->
The Sensitivity Index shown above means that when the k1 increased by 1%, the number of Mandarin L2

<!-- b000439 | prose | pages [19] -->
k2

<!-- b000440 | prose | pages [19] -->
speakers will in turn increase by 0.10%. So the variation of this index has minor influence on the results.

<!-- b000441 | prose | pages [19] -->
k2 is the proportional coefficient of the second language growth rate and cultural communication. we enter 3. different k2 into the program, and we get different Mandarin L2 speakers number. Here is the result:

<!-- b000442 | caption | pages [19] -->
Table 14 Sensitivity analysis on k2

<!-- b000443 | prose | pages [19] -->
k2

<!-- b000444 | prose | pages [19] -->
the number of Mandarin L2 speakers

<!-- b000445 | prose | pages [19] -->
0.00001 0.0000111 0.0000125

<!-- b000446 | prose | pages [19] -->
393.11 397.27 401.38

<!-- b000447 | prose | pages [19] -->
The Sensitivity Index shown above means that when the k2 increased by 1%, the number of Mandarin L2

<!-- b000448 | prose | pages [19] -->
sensitivity

<!-- b000449 | heading | pages [19] -->
4. k3

<!-- b000450 | prose | pages [19] -->
0.093739774

<!-- b000451 | prose | pages [19] -->
speakers will in turn increase by 0.09%. So the variation of this index has minor influence on the results.

<!-- b000452 | prose | pages [19] -->
k3 is the proportional coefficient of the second language growth rate and economics. we enter different k3

<!-- b000453 | caption | pages [19] -->
Table 15 Sensitivity analysis on k3

<!-- b000454 | prose | pages [19] -->
into the program, and we get different Mandarin L2 speakers number. Here is the result:

<!-- b000455 | prose | pages [19] -->
k3

<!-- b000456 | prose | pages [19] -->
the number of Mandarin L2 speakers

<!-- b000457 | prose | pages [19] -->
0.2 0.3 0.4

<!-- b000458 | prose | pages [19] -->
387.12 397.27 408.2

<!-- b000459 | prose | pages [19] -->
The Sensitivity Index shown above means that when the k3 increased by 1%, the number of Mandarin L2

<!-- b000460 | prose | pages [19] -->
sensitivity

<!-- b000461 | heading | pages [19] -->
5. k4

<!-- b000462 | prose | pages [19] -->
0.079593224

<!-- b000463 | prose | pages [19] -->
speakers will in turn increase by 0.079%. So the variation of this index has minor influence on the results.

<!-- b000464 | prose | pages [19] -->
k4 is the proportional coefficient of the second language growth rate and technology. we enter different k4

<!-- b000465 | caption | pages [19] -->
Table 16 Sensitivity analysis on k4

<!-- b000466 | prose | pages [19] -->
into the program, and we get different Mandarin L2 speakers number. Here is the result:

<!-- b000467 | prose | pages [19] -->
k4

<!-- b000468 | prose | pages [19] -->
the number of Mandarin L2 speakers

<!-- b000469 | prose | pages [19] -->
0.1 0.2 0.3

<!-- b000470 | prose | pages [19] -->
391.82 397.27 403.1

<!-- b000471 | prose | pages [19] -->
The Sensitivity Index shown above means that when the k4 increased by 1%, the number of Mandarin L2

<!-- b000472 | prose | pages [19] -->
sensitivity

<!-- b000473 | heading | pages [19] -->
6. k5

<!-- b000474 | prose | pages [19] -->
0.028393788

<!-- b000475 | prose | pages [19] -->
speakers will in turn increase by 0.028%. So, the variation of this index has minor influence on the results.

<!-- b000476 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000477 | furniture | pages [20] -->
Team # 79002

<!-- b000478 | furniture | pages [20] -->
Page 19 of 29

<!-- b000479 | prose | pages [20] -->
k5 is the proportional coefficient of the second language growth rate and media. we enter different k5 into the

<!-- b000480 | caption | pages [20] -->
Table 17 Sensitivity analysis on k5

<!-- b000481 | prose | pages [20] -->
program, and we get different Mandarin L2 speakers number. Here is the result:

<!-- b000482 | prose | pages [20] -->
k5

<!-- b000483 | prose | pages [20] -->
the number of Mandarin L2 speakers

<!-- b000484 | prose | pages [20] -->
0.1 0.2 0.3

<!-- b000485 | prose | pages [20] -->
394.88 397.27 400.12

<!-- b000486 | prose | pages [20] -->
The Sensitivity Index shown above means that when the k5 increased by 1%, the number of Mandarin L2

<!-- b000487 | prose | pages [20] -->
sensitivity 0.013190022

<!-- b000488 | prose | pages [20] -->
speakers will in turn increase by 0.013%. So, the variation of this index has minor influence on the results.

<!-- b000489 | heading | pages [20] -->
5.2 sensitivity analysis of model II

<!-- b000490 | prose | pages [20] -->
The purpose of Model II is to show the relationship between the change in the geographical distribution of k6. Below we will conduct a sensitivity analysis of these two parameters. Wewill use different result to measure language and the immigrants over time. The man-made parameters in model II are the natural increase rates and

<!-- b000491 | prose | pages [20] -->
the change of the two indices.

<!-- b000492 | heading | pages [20] -->
7. Natural growth rate

<!-- b000493 | prose | pages [20] -->
In our model II, we set a very large number of natural growth rates. Almost every continent has its ownnatural rate of growth in every language. But we can’t analysis every parameter. Therefore, we only change the natural growth rate of Hindi in Asia to see what changes it will bring.

<!-- b000494 | caption | pages [20] -->
Figure 15 Sensitivity analysis on the natural growth rate

<!-- b000495 | prose | pages [20] -->
the given Hindi growth rate is 0.8%(right) and 1.2%(left) As the pie chart shows, subtle changes in the rate of natural increase do not change the distribution in Asia.

<!-- b000496 | prose | pages [20] -->
k6

<!-- b000497 | prose | pages [20] -->
Therefore, we say that the selection of our natural growth rate is insensitive to the result.

<!-- b000498 | prose | pages [20] -->
k6 is the proportional coefficient of migration to the growth of native language speakers. If we change the 8. number of k6, all results may change. The k6 we set first is 0.5%. Then we slightly lower this value to 0.3% to see what changes it will produce.

<!-- b000499 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000500 | furniture | pages [21] -->
Team # 79002

<!-- b000501 | furniture | pages [21] -->
Page 20 of 29

<!-- b000502 | caption | pages [21] -->
Figure 16 The sensitivity analysis on migration coefficient

<!-- b000503 | prose | pages [21] -->
6 We now have a slight difference between this result and in Figure 17 the original result in Figure 18. English and French speakers in the U.S. and Canada dropped slightly. Besides, Australian English users dropped slightly. We can see that these changes are very small and do not affect the overall situation. So, we think the change of this parameter has little effect on the result.

<!-- b000504 | prose | pages [21] -->
6

<!-- b000505 | heading | pages [21] -->
Strength and Weakness

<!-- b000506 | heading | pages [21] -->
Strengths:

<!-- b000507 | prose | pages [21] -->
(1) We do plenty of research, and collect plenty of data which make our model close to reality.

<!-- b000508 | prose | pages [21] -->
(2) We consider various factors in terms of second language increase, such as school teaching, cultural

<!-- b000509 | prose | pages [21] -->
migration and assimilation, the use of technology, social media and economics.

<!-- b000510 | prose | pages [21] -->
(3) We do a full sensitivity analysis.

<!-- b000511 | heading | pages [21] -->
Weakness:

<!-- b000512 | prose | pages [21] -->
(1) We do not include all influence to the total number of speakers of a language, such as the use of electronic

<!-- b000513 | prose | pages [21] -->
communication for lack of data.

<!-- b000514 | prose | pages [21] -->
(2) We assume the second language speakers is in direct proportion to its influences. But the fact may be not.

<!-- b000515 | prose | pages [21] -->
For example, we assume the second language speakers is in direct proportion to school teaching, but the fact may be exponential relationship or paternity relationship.

<!-- b000516 | prose | pages [21] -->
(3) Our model II does not consider age and sex ratio.

<!-- b000517 | prose | pages [21] -->
(4) We do not consider the second language in respect of geographic distributions of these languages. Because

<!-- b000518 | prose | pages [21] -->
we do not find efficient data to analyze this.

<!-- b000519 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000520 | furniture | pages [22] -->
Team # 79002

<!-- b000521 | furniture | pages [22] -->
Page 21 of 29

<!-- b000522 | prose | pages [22] -->
7

<!-- b000523 | heading | pages [22] -->
Memo

<!-- b000524 | heading | pages [22] -->
MEMORANDUM

<!-- b000525 | prose | pages [22] -->
TO: Chief Operating Officer FROM: Team#79002

<!-- b000526 | prose | pages [22] -->
About half the world’s total population are saying that one of the top 10 languages (in order of most speakers) as their mother tongue. In addition, many people learn a language as their second language because of government promotion, schooling, neighborhood effect, social media trends, international business and immigration. Therefore, the number of native speakers and 2nd language speakers in each language is dynamically changing over time.

<!-- b000527 | prose | pages [22] -->
Prediction of top 10 languages over 50 years:

<!-- b000528 | prose | pages [22] -->
Based on the various data collected from Ethnologue, World Bank and many other resources, our team has taken into account the factors mentioned above and has built a model of the number of speakers of each language over time to predict the change in language rank over the 50-year period.

<!-- b000529 | prose | pages [22] -->
Wefound the top 10 languages’ranks change from Mandarin、English、Hindustani、Spanish、Arabic、Malay、 Russian、Bengali、Portuguese、Frenchin2017toMandarin、English、Spanish、Hindustani、Arabic、Bengali、 Portuguese、Malay、Russian、French in 2067.

<!-- b000530 | prose | pages [22] -->
As a service company, when choosing whether to set up local branches, your company should focus on how many potential local clients, and then to conduct a wide range of professional service, to achieve higher profitability.

<!-- b000531 | prose | pages [22] -->
In the meantime, a large percentage of these cities are either native or second foreign languages, and employees of more than two languages are easily admitted to the company's branch office.

<!-- b000532 | prose | pages [22] -->
Six office sites:

<!-- b000533 | prose | pages [22] -->
Our recommendations are different in the short term versus the long term because the rapid growth in both population and economic of Portuguese speaker.

<!-- b000534 | prose | pages [22] -->
In the short term, the six office sites recommended are: Shanghai, New York, Calcutta, Madrid, Dubai, and Singapore. While in the long term, the six offices sites recommended are: Shanghai, New York, Calcutta, Madrid, Dubai, and Rio de Janeiro.

<!-- b000535 | prose | pages [22] -->
As we can see, the Malay speakers’ growth is slightly slower than the growth of Portuguese speakers.

<!-- b000536 | prose | pages [22] -->
The best number of offices:

<!-- b000537 | prose | pages [22] -->
To determine the best number of offices, we set up a cost-benefit analysis model, and when your company has provided us with your profitability and office-building costs, we can figure out the suitable company number. When the company's profitability and cost levels are different, the number of plants best suited for construction is different.

<!-- b000538 | prose | pages [22] -->
If the value of c-p ratio is less than 281, we think 6 offices should be built. If the value of this ratio is between 281 and 422, we think 5 offices should be built. If the value is between 422-527, 4 offices are best; if it is between 527 and 544, 3 office should be built; if> 544, we should only maintain two original offices.

<!-- b000539 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000540 | furniture | pages [23] -->
Team # 79002

<!-- b000541 | furniture | pages [23] -->
Page 22 of 29

<!-- b000542 | prose | pages [23] -->
Thank you for your consultation.

<!-- b000543 | prose | pages [23] -->
Best,

<!-- b000544 | furniture | pages [23] -->
Team#79002

<!-- b000545 | heading | pages [23] -->
References:

<!-- b000546 | references | pages [23] -->
[1]. https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers.

<!-- b000547 | references | pages [23] -->
[2]. Languages for the future. 2013: British Council.

<!-- b000548 | references | pages [23] -->
[3]. Sarah Elaine Eaton, P.D., global trends in language learning in 21st century. 2010.

<!-- b000549 | references | pages [23] -->
[4]. https://en.wikipedia.org/wiki/Malthusian_growth_model.

<!-- b000550 | references | pages [23] -->
[5]. http://www.stolaf.edu/people/mckelvey/envision.dir/logistic.html.

<!-- b000551 | references | pages [23] -->
[6]. https://en.wikipedia.org/wiki/List_of_most_commonly_learned_foreign_languages_in_the_United_States.

<!-- b000552 | references | pages [23] -->
[7]. http://unicode.org/notes/tn13/.

<!-- b000553 | references | pages [23] -->
[8]. https://www.weforum.org/agenda/2015/10/is-the-internet-killing-off-the-worlds-languages/.

<!-- b000554 | references | pages [23] -->
[9]. http://www.internetworldstats.com/stats7.html.

<!-- b000555 | references | pages [23] -->
[10]. https://data.worldbank.org.cn/indicator/SP.POP.TOTL.

<!-- b000556 | references | pages [23] -->
[11]. https://faculty.washington.edu/sis/.

<!-- b000557 | references | pages [23] -->
[12]. https://www.myaccountingcourse.com/accounting-dictionary/service-company.

<!-- b000558 | references | pages [23] -->
[13]. https://en.wikipedia.org/wiki/List_of_most_commonly_learned_foreign_languages_in_the_United_States.

<!-- b000559 | references | pages [23] -->
8

<!-- b000560 | heading | pages [23] -->
Appendix

<!-- b000561 | heading | pages [23] -->
8.1 data

<!-- b000562 | prose | pages [23] -->
(1) language distribution of various continents:

<!-- b000563 | prose | pages [23] -->
Source:

<!-- b000564 | prose | pages [23] -->
https://www.worldatlas.com/articles/the-most-spoken-languages-in-america.html

<!-- b000565 | prose | pages [23] -->
https://en.wikipedia.org/wiki/Teaching_English_as_a_second_or_foreign_language#Asia

<!-- b000566 | prose | pages [23] -->
https://en.wikipedia.org/wiki/List_of_countries_by_natural_increase

<!-- b000567 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000568 | furniture | pages [24] -->
Team # 79002

<!-- b000569 | furniture | pages [24] -->
Page 23 of 29

<!-- b000570 | prose | pages [24] -->
http://www.myeses.com/news/view.asp?id=3457

<!-- b000571 | prose | pages [24] -->
https://www.douban.com/note/635706471/

<!-- b000572 | prose | pages [24] -->
https://en.wikipedia.org/wiki/List_of_countries_by_population_growth_rate

<!-- b000573 | prose | pages [24] -->
https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population

<!-- b000574 | prose | pages [24] -->
(2) languages On the Internet[9]

<!-- b000575 | prose | pages [24] -->
(3) GDP

<!-- b000576 | prose | pages [24] -->
[7]

<!-- b000577 | prose | pages [24] -->
(4) foreigh language taught in school:[13]

<!-- b000578 | prose | pages [24] -->
Source:

<!-- b000579 | prose | pages [24] -->
https://en.wikipedia.org/wiki/List_of_most_commonly_learned_foreign_languages_in_the_United_States http://ec.europa.eu/eurostat/statistics- explained/index.php/File:Foreign_languages_learnt_per_pupil_in_upper_secondary_education_(general),_20 10_and_2015_(%25)_ET2017.png

<!-- b000580 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000581 | furniture | pages [25] -->
Team # 79002

<!-- b000582 | furniture | pages [25] -->
Page 24 of 29

<!-- b000583 | prose | pages [25] -->
(5)natural growth rate:

<!-- b000584 | prose | pages [25] -->
Source:

<!-- b000585 | prose | pages [25] -->
https://en.wikipedia.org/wiki/List_of_countries_by_natural_increase

<!-- b000586 | heading | pages [25] -->
8.2 program

<!-- b000587 | prose | pages [25] -->
1.module I

<!-- b000588 | prose | pages [25] -->
%r1 average natural popurlation of people

<!-- b000589 | prose | pages [25] -->
z=xlsread('data.xlsx');

<!-- b000590 | prose | pages [25] -->
x0=z(:,1);

<!-- b000591 | prose | pages [25] -->
y0=z(:,2);

<!-- b000592 | prose | pages [25] -->
r1=z(:,3);

<!-- b000593 | prose | pages [25] -->
c=[1;1;0;1;0;0;1;0;0;1;0;0;1;1;0;0];%developed or not

<!-- b000594 | prose | pages [25] -->
n=length(x0);

<!-- b000595 | prose | pages [25] -->
x=zeros(n,60);

<!-- b000596 | prose | pages [25] -->
y=zeros(n,60);

<!-- b000597 | prose | pages [25] -->
x(:,1)=x0;

<!-- b000598 | prose | pages [25] -->
y(:,1)=y0;

<!-- b000599 | prose | pages [25] -->
r2=0.0005;% increase contributed by the second language speakers

<!-- b000600 | prose | pages [25] -->
k1=1/300;% school factor

<!-- b000601 | prose | pages [25] -->
k2=1/90000;% cultural communication

<!-- b000602 | prose | pages [25] -->
k3=0.3;% international bussiness

<!-- b000603 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000604 | furniture | pages [26] -->
Team # 79002

<!-- b000605 | furniture | pages [26] -->
Page 25 of 29

<!-- b000606 | prose | pages [26] -->
k4=0.2;% the use of translation technology

<!-- b000607 | prose | pages [26] -->
k5=0.3;% socia media

<!-- b000608 | prose | pages [26] -->
a=xlsread('a.xlsx');%different language use percentage in school of differentregion

<!-- b000609 | prose | pages [26] -->
b=xlsread('b.xlsx');%comunacation percentage

<!-- b000610 | prose | pages [26] -->
q=xlsread('q.xlsx');%GDP communicated bylanguages

<!-- b000611 | prose | pages [26] -->
p=xlsread('p.xlsx');%language used in internet

<!-- b000612 | prose | pages [26] -->
for i=2:60

<!-- b000613 | prose | pages [26] -->
%the next year native speakers

<!-- b000614 | prose | pages [26] -->
x(:,i)=x(:,i-1)+native1(x(:,i-1).*c,y(:,i-1).*c,r1,r2)+native2(x(:,i-1).*(c==0),r1,2*x0);

<!-- b000615 | prose | pages [26] -->
%the increase of second language speakers because of school use

<!-- b000616 | prose | pages [26] -->
delta1=school(x(:,i-1),a,k1);

<!-- b000617 | prose | pages [26] -->
%the increase of second language speakers because of cultural communication

<!-- b000618 | prose | pages [26] -->
delta2=culturecom(x(:,i-1),b,k2);

<!-- b000619 | prose | pages [26] -->
%the increase because of international bussiness

<!-- b000620 | prose | pages [26] -->
delta3=interbussiness(q,k3);

<!-- b000621 | prose | pages [26] -->
%the decrease because of the use of translation technology

<!-- b000622 | prose | pages [26] -->
delta4=technology(k4);

<!-- b000623 | prose | pages [26] -->
%the increase because of socia media

<!-- b000624 | prose | pages [26] -->
delta5=media(p,k5);

<!-- b000625 | prose | pages [26] -->
y(:,i)=y(:,i-1)+delta1+delta2+delta3+delta4+delta5;

<!-- b000626 | prose | pages [26] -->
end

<!-- b000627 | prose | pages [26] -->
xlswrite('answer.xlsx',[x(:,50),y(:,50)]);

<!-- b000628 | prose | pages [26] -->
function z=native1(x,y,r1,r2)

<!-- b000629 | prose | pages [26] -->
% the increase of native speaker in developed countries

<!-- b000630 | prose | pages [26] -->
z=r1.*x/100+r2.*y;

<!-- b000631 | prose | pages [26] -->
end

<!-- b000632 | prose | pages [26] -->
function z=native2(x,r,s)

<!-- b000633 | prose | pages [26] -->
% the increase of native speaker in developing countries

<!-- b000634 | prose | pages [26] -->
z=r/100.*(1-x./s).*x;

<!-- b000635 | prose | pages [26] -->
end

<!-- b000636 | prose | pages [26] -->
function z=school(x,a,k)

<!-- b000637 | prose | pages [26] -->
%the increase of second language speakers because of school use

<!-- b000638 | prose | pages [26] -->
%k is a properation index

<!-- b000639 | prose | pages [26] -->
n=length(x); z=zeros(n,1);

<!-- b000640 | prose | pages [26] -->
for i=1:n

<!-- b000641 | prose | pages [26] -->
z(i)=k*a(i,:)*x;

<!-- b000642 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000643 | furniture | pages [27] -->
Team # 79002

<!-- b000644 | furniture | pages [27] -->
Page 26 of 29

<!-- b000645 | prose | pages [27] -->
end

<!-- b000646 | prose | pages [27] -->
end

<!-- b000647 | prose | pages [27] -->
function z=technology(k)

<!-- b000648 | prose | pages [27] -->
% the increase because of the use of translation technology

<!-- b000649 | prose | pages [27] -->
z=-k;

<!-- b000650 | prose | pages [27] -->
end

<!-- b000651 | prose | pages [27] -->
function z=media(p,k)

<!-- b000652 | prose | pages [27] -->
z=k*p;

<!-- b000653 | prose | pages [27] -->
end

<!-- b000654 | prose | pages [27] -->
function z=culturecom(x,b,k)

<!-- b000655 | prose | pages [27] -->
%the increase of second language speakers because of cultural communication

<!-- b000656 | prose | pages [27] -->
n=length(x);

<!-- b000657 | prose | pages [27] -->
z=zeros(n,1);

<!-- b000658 | prose | pages [27] -->
for i=1:n

<!-- b000659 | prose | pages [27] -->
z(i)=k*x(i)*b(i,:)*x;

<!-- b000660 | prose | pages [27] -->
end

<!-- b000661 | prose | pages [27] -->
end

<!-- b000662 | prose | pages [27] -->
2. module II

<!-- b000663 | prose | pages [27] -->
#include<stdio.h>

<!-- b000664 | prose | pages [27] -->
#include<math.h>

<!-- b000665 | prose | pages [27] -->
#include<cstring>

<!-- b000666 | prose | pages [27] -->
#include<iostream>

<!-- b000667 | prose | pages [27] -->
#include<algorithm>

<!-- b000668 | prose | pages [27] -->
using namespace std;

<!-- b000669 | prose | pages [27] -->
float r[50][50],sum[50];

<!-- b000670 | prose | pages [27] -->
float x[50][50],y[50],ry[50],p[50][50];

<!-- b000671 | prose | pages [27] -->
struct node{

<!-- b000672 | prose | pages [27] -->
float people;

<!-- b000673 | prose | pages [27] -->
int language;

<!-- b000674 | prose | pages [27] -->
}aa[50];

<!-- b000675 | prose | pages [27] -->
bool cmp(node a,node

<!-- b000676 | prose | pages [27] -->
b){ return

<!-- b000677 | prose | pages [27] -->
a.people>b.people;

<!-- b000678 | prose | pages [27] -->
}

<!-- b000679 | prose | pages [27] -->
int T=50;

<!-- b000680 | prose | pages [27] -->
float k=0.003;

<!-- b000681 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000682 | furniture | pages [28] -->
Team # 79002

<!-- b000683 | furniture | pages [28] -->
Page 27 of 29

<!-- b000684 | prose | pages [28] -->
int main()

<!-- b000685 | prose | pages [28] -->
{

<!-- b000686 | prose | pages [28] -->
//x[i][j]第i 洲说j 语言人数

<!-- b000687 | prose | pages [28] -->
//r[i][j]表示第i 洲说语言j 的自然增长率

<!-- b000688 | prose | pages [28] -->
//y[i]第i 洲others 的人数

<!-- b000689 | prose | pages [28] -->
//ry[i]第i 洲others 的自然增长率

<!-- b000690 | prose | pages [28] -->
//p[i][j]第i 洲说j 语言的比例

<!-- b000691 | prose | pages [28] -->
x[1][1]=150,x[1][2]=56,x[1][3]=34,x[1][4]=28,x[1][5]=26;y[1]=289.25692;

<!-- b000692 | prose | pages [28] -->
x[2][6]=897,x[2][7]=550,x[2][8]=301.625412,x[2][9]=260,x[2][10]=240,x[2][1]=230,x[2][11]=230,x[2][12]= 120;

<!-- b000693 | prose | pages [28] -->
y[2]=1377.734272;

<!-- b000694 | prose | pages [28] -->
x[3][8]=18.175,x[3][6]=0.625,x[3][1]=0.35,y[3]=5.85;

<!-- b000695 | prose | pages [28] -->
x[4][9]=106,x[4][13]=97,x[4][14]=66,x[4][15]=65,x[4][8]=60,x[4][16]=38.5,x[4][17]=38,y[4]=304.382487;

<!-- b000696 | prose | pages [28] -->
x[5][17]=383.4,x[5][18]=217.26,y[5]=38.34;

<!-- b000697 | prose | pages [28] -->
x[6][8]=43.240855,x[6][17]=4.508850,x[6][6]=0.932035,x[6][18]=0.601385,x[6][19]=0.30643,x[6][1]=0.539 895,x[6][14]=7.2867;

<!-- b000698 | prose | pages [28] -->
y[6]=9.9511;

<!-- b000699 | prose | pages [28] -->
r[1][1]=0.015;r[1][3]=0.02;for(int i=1;i<=19;i++)if(r[1][i]==0)r[1][i]=0.016;

<!-- b000700 | prose | pages [28] -->
r[2][6]=0.005;r[2][7]=0.012;r[2][8]=0.009;r[2][9]=0.002;for(int i=1;i<=19;i++)if(r[2][i]==0)r[2][i]=0.01;

<!-- b000701 | prose | pages [28] -->
for(int i=1;i<=19;i++)r[5][i]=0.01,r[6][i]=0.004,r[3][i]=0.008;

<!-- b000702 | prose | pages [28] -->
ry[1]=0.016;ry[2]=0.001;ry[3]=0.008;ry[5]=0.001;ry[6]=0.004;

<!-- b000703 | prose | pages [28] -->
printf("time continent language people(million) others(million)\n");

<!-- b000704 | prose | pages [28] -->
for(int t=1;t<=T;t++){

<!-- b000705 | prose | pages [28] -->
for(int

<!-- b000706 | prose | pages [28] -->
i=1;i<=6;i++){ sum[

<!-- b000707 | prose | pages [28] -->
i]=0;

<!-- b000708 | prose | pages [28] -->
for(int j=1;j<=19;j++)

<!-- b000709 | prose | pages [28] -->
sum[i]=sum[i]+x[i][j];

<!-- b000710 | prose | pages [28] -->
sum[i]+=y[i];

<!-- b000711 | prose | pages [28] -->
for(int j=1;j<=19;j++)

<!-- b000712 | prose | pages [28] -->
p[i][j]=x[i][j]/sum[i];

<!-- b000713 | prose | pages [28] -->
}

<!-- b000714 | prose | pages [28] -->
for(int

<!-- b000715 | prose | pages [28] -->
i=1;i<=6;i++){ for(int

<!-- b000716 | prose | pages [28] -->
j=1;j<=19;j++)

<!-- b000717 | prose | pages [28] -->
x[i][j]=x[i][j]*(1+r[i][j]);

<!-- b000718 | prose | pages [28] -->
y[i]=y[i]*(1+ry[i]);

<!-- b000719 | prose | pages [28] -->
}

<!-- b000720 | furniture | pages [29] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000721 | furniture | pages [29] -->
Team # 79002

<!-- b000722 | furniture | pages [29] -->
Page 28 of 29

<!-- b000723 | prose | pages [29] -->
x[4][6]+=0.36+0.36*k*p[4][6];x[4][1]+=0.72*(1+k*p[4][1]);

<!-- b000724 | prose | pages [29] -->
x[4][7]+=0.18*(1+k*p[4][7]);x[4][8]+=0.18*(1+k*p[4][8]);

<!-- b000725 | prose | pages [29] -->
x[6][6]+=0.48*(1+k*p[6][6]);x[6][17]+=0.24*(1+k*p[6][17]);

<!-- b000726 | prose | pages [29] -->
x[6][18]+=0.12*(1+k*p[6][18]);x[3][6]+=0.12*(1+k*p[3][6]);

<!-- b000727 | prose | pages [29] -->
// x[2][6]-=8.4;x[2][1]-=3.6;

<!-- b000728 | prose | pages [29] -->
// x[2][7]-=1.8;x[2][8]-=1.8;

<!-- b000729 | prose | pages [29] -->
// x[5][17]-=2.4;x[5][18]-=1.2;

<!-- b000730 | prose | pages [29] -->
// x[1][1]-=4.8;

<!-- b000731 | prose | pages [29] -->
for(int

<!-- b000732 | prose | pages [29] -->
i=1;i<=6;i++){ for(int

<!-- b000733 | prose | pages [29] -->
j=1;j<=19;j++){

<!-- b000734 | prose | pages [29] -->
aa[j].people=x[i][j];aa[j].language=j;

<!-- b000735 | prose | pages [29] -->
}

<!-- b000736 | prose | pages [29] -->
sort(aa+1,aa+20,cmp);

<!-- b000737 | prose | pages [29] -->
if(t==20||t==50){

<!-- b000738 | prose | pages [29] -->
for(int j=1;j<=19;j++)

<!-- b000739 | prose | pages [29] -->
printf("%d %d %d %lf %lf\n",t,i,aa[j].language,aa[j].peopl e,y[i]);

<!-- b000740 | prose | pages [29] -->
printf("\n");

<!-- b000741 | prose | pages [29] -->
}

<!-- b000742 | prose | pages [29] -->
}

<!-- b000743 | prose | pages [29] -->
}

<!-- b000744 | prose | pages [29] -->
return 0;

<!-- b000745 | prose | pages [29] -->
}
