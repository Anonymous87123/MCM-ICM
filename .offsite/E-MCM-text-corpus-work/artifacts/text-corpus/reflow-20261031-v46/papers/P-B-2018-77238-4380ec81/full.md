# P-B-2018-77238-4380ec81

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | front_matter | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For office use only For office use only 77238 T1 F1 T2 F2 Problem Chosen T3 F3 B F4 T4

<!-- b000004 | prose | pages [1] -->
2018 MCM/ICM

<!-- b000005 | heading | pages [1] -->
Summary Sheet

<!-- b000006 | heading | pages [1] -->
Summary

<!-- b000007 | prose | pages [1] -->
Thousands of languages are spoken around on the Earth, and over 40% of people take one of the top ten most spoken language as their mother tongue. Meanwhile, more and more people are learning a second language to meet the rapid development of economy and globalization.

<!-- b000008 | prose | pages [1] -->
Aimed to predict the distribution of widespread language speakers over the next 50 years, we build a Language Development Model, and apply it to countries with a population over 10 million to describe the possibility of the new generation in a certain country studying a certain second language. We employ the Analytical Hierarchy Process (AHP) to determine the specific parameters, and carry out stochastic simulation on Python to produce the results, which shows that mild change takes place on the list of popular languages – only two of the top-10 languages are replaced, while the total number of speakers of several languages gains an impressive increase.

<!-- b000009 | prose | pages [1] -->
Based on the language distribution model we obtain, we develop a Location Determination Model. The dual-solution model further provide a recommendation for a large multinational service company to select the location of their new international office. One of the solution is oriented by language structure, and the other by geographic condition. Taking language distribution as well as economic development of different countries into account, the model suggests that new offices should be located in Nigeria, India, Germany, Italy, Brazil, Australia for short-term interest, and Nigeria, Russia, Germany, Poland, Brazil, Australia for long-term development.

<!-- b000010 | prose | pages [1] -->
The sensitivity analysis shows the strong robustness of our model. Variation of key parameters causes moderate changes to the computing result. When we test the sensitivity, we indirectly validate our model’s conformance with reality that the direction of fluctuation of the result matches situations in real world. Meanwhile, we further discuss the impact of reducing the number of new office, and provide practicable advice on location determination of new offices.

<!-- b000011 | keywords | pages [1] -->
Key Words: Language Development Model, AHP, Fuzzy Clustering, P-Center Model

<!-- b000012 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000013 | furniture | pages [2] -->
# Team

<!-- b000014 | furniture | pages [2] -->
Page 2 of 23

<!-- b000015 | heading | pages [2] -->
Content

<!-- b000016 | contents | pages [2] -->
1.

<!-- b000017 | contents | pages [2] -->
Introduction...............................................................................................................................3

<!-- b000018 | contents | pages [2] -->
2.

<!-- b000019 | contents | pages [2] -->
Assumptions and Justification..................................................................................................3

<!-- b000020 | contents | pages [2] -->
3.

<!-- b000021 | contents | pages [2] -->
Notation.................................................................................................................................... 4

<!-- b000022 | contents | pages [2] -->
4.

<!-- b000023 | contents | pages [2] -->
Model........................................................................................................................................4

<!-- b000024 | contents | pages [2] -->
4.1 Language Development Model..........................................................................................4

<!-- b000025 | contents | pages [2] -->
4.1.1 Judgment Process....................................................................................................4

<!-- b000026 | contents | pages [2] -->
4.1.2 Stochastic Simulation Process................................................................................7

<!-- b000027 | contents | pages [2] -->
4.2 Location Determination Model........................................................................................11

<!-- b000028 | contents | pages [2] -->
4.2.1 Solution Oriented by Language Structure............................................................ 11

<!-- b000029 | contents | pages [2] -->
4.2.2 Solution Oriented by Geographic Condition........................................................13

<!-- b000030 | contents | pages [2] -->
5.

<!-- b000031 | contents | pages [2] -->
Sensitivity Analysis................................................................................................................ 17

<!-- b000032 | contents | pages [2] -->
5.1 Sensitivity Analysis on Language Development Model..................................................17

<!-- b000033 | contents | pages [2] -->
5.1.1 Net Birth Rate Impact...........................................................................................17

<!-- b000034 | contents | pages [2] -->
5.1.2 GDP Growth Rate Impact.....................................................................................17

<!-- b000035 | contents | pages [2] -->
5.1.3 Migration Rate Impact..........................................................................................18

<!-- b000036 | contents | pages [2] -->
5.2 Sensitivity Analysis on Location Determination Model..................................................19

<!-- b000037 | contents | pages [2] -->
6.

<!-- b000038 | contents | pages [2] -->
Further Discussion..................................................................................................................20

<!-- b000039 | contents | pages [2] -->
7.

<!-- b000040 | contents | pages [2] -->
Strengths and Weaknesses...................................................................................................... 20

<!-- b000041 | contents | pages [2] -->
7.1 Strengths.......................................................................................................................... 20

<!-- b000042 | contents | pages [2] -->
7.2 Weaknesses...................................................................................................................... 21

<!-- b000043 | contents | pages [2] -->
7.

<!-- b000044 | contents | pages [2] -->
Conclusion..............................................................................................................................21

<!-- b000045 | contents | pages [2] -->
Reference.......................................................................................................................................21

<!-- b000046 | contents | pages [2] -->
Memo to the Service Company..................................................................................................... 22

<!-- b000047 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000048 | furniture | pages [3] -->
# Team

<!-- b000049 | furniture | pages [3] -->
Page 3 of 23

<!-- b000050 | heading | pages [3] -->
1. Introduction

<!-- b000051 | prose | pages [3] -->
Language is the most important communication tool for human beings. Today, over 6000 languages are spoken on Earth, which help preserve and inherit human civilization and achievements. While everyone has his/her own native language which seldom changes all over his/her life, the number of people speaking a second language keeps increasing not only because of domestic factors such as school studying or governmental promotion, but also international factors including growing migration, booming global tourism and close communication online. Considering both native and second language speakers, great changes take place in language distribution and the number of speakers.

<!-- b000052 | prose | pages [3] -->
To investigate how the commonly used languages scatter worldwide, we develop a Language Development Model to forecast the future development of the 16 most spoken languages counted in 2017. Based on the original distribution of different languages and the Net Birth Rate of these countries, we build the model to simulate how language distribution changes over the next 50 years.

<!-- b000053 | prose | pages [3] -->
After obtaining the result from the Language Development Model, we build a Location Determination Model using two different solutions. For the former one, we group the countries based on their language structure. For the latter one, they are separated according to their geographic condition. After the grouping process, we set two goals to filter an optimal location for the new office in each group, namely GDP distribution and distance from other countries in the same group. Besides, we give recommended spoken language in these new offices.

<!-- b000054 | heading | pages [3] -->
2. Assumptions and Justification

<!-- b000055 | prose | pages [3] -->
We make some general assumptions to simplify our model. These assumptions together with corresponding justification are listed below:

<!-- b000056 | prose | pages [3] -->
All people take a certain language as their native language, but not every of them speaks  a second language.

<!-- b000057 | prose | pages [3] -->
Language is an indispensable tool for every person, so all people can speak at least one language, either commonly or rarely used. However, whether one speaks an additional second language depends on multiple reasons, for example, the developmental level of his/her country.

<!-- b000058 | prose | pages [3] -->
All existing people won’t change their native and second language.  People usually speak the same native language through his/her life. We do not consider change in native language caused by migration or other factors in the simplified model. The influence of migration will be discussed in 4.1.1.

<!-- b000059 | prose | pages [3] -->
The new generation all take their parents’ native language as their own native language.  However, their choice of the second language varies for several reasons discussed in 4.1.1.

<!-- b000060 | prose | pages [3] -->
Few families are composed of members speaking different native language. Meanwhile, the specific data is hard to derive. So, we ignore the influence of the multi-composed families and assume that children all take their parents’ native language as their own nativelanguage. More detailed assumptions will be listed if needed.

<!-- b000061 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000062 | furniture | pages [4] -->
# Team

<!-- b000063 | furniture | pages [4] -->
Page 4 of 23

<!-- b000064 | heading | pages [4] -->
3. Notation

<!-- b000065 | heading | pages [4] -->
4. Model

<!-- b000066 | heading | pages [4] -->
4.1 Language Development Model

<!-- b000067 | prose | pages [4] -->
To discuss the changes of the top-ten language list, we analyze 16 currently most spoken languages. We gather the characteristics of language distribution of different countries to produce a global language distribution. To reduce the amount of calculation, we only consider countries with a population over 10 million, since they have contributed about 92% of total population on Earth as shown in Appendix 1. To simplify our model, we suggest the language with the most speakers represent the native language of a certain country. For each country, we acquire its population data from 2007 to 2017 on the United Nation Database [1], and obtain its Net Birth Rate to calculate its newly-born population every year. Meanwhile, the percentage of different language speakers is acquired [1,2] so that we can know the current language structure of the country. Through careful analysis of every country we take into account, we seek to obtain the language distribution all over the world.

<!-- b000068 | heading | pages [4] -->
4.1.1 Judgment Process

<!-- b000069 | prose | pages [4] -->
Weassumed that the existing people won’t make a change on their native and second language, and the newly-born population all take their parents’ native language as their own native language. Therefore, the numerical development of a certain language is completely determined by the newly increased population. However, not all of them will speak a second language, and which language they will take as their second language varies for economic, social, political and other reasons. So, we divide the judgment process into two steps – first to judge whether one will speak a second language, and then which language he/she will take. The judgment process of our Language Development Model is shown in Figure 1.

<!-- b000070 | prose | pages [4] -->
No

<!-- b000071 | prose | pages [4] -->
Chinese Which language? English Speak various Newly-born Speak a second language? (communication, Yes Pij second language population French (Communication and economy) geography, economy, (Ai) knowledge, diplomacy) ……

<!-- b000072 | prose | pages [4] -->
(1-Ai)

<!-- b000073 | prose | pages [4, 5] -->
Speak only one language To quantify various reasons that affect the second language, we first take communicative and economic factors to determine if one speaks a second language in our analysis. Both two factors weigh 0.5 when calculating the possibility.

<!-- b000074 | caption | pages [4] -->
Figure 1 Judgment process of Language Development Model

<!-- b000075 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000076 | furniture | pages [5] -->
# Team

<!-- b000077 | furniture | pages [5] -->
Page 5 of 23

<!-- b000079 | prose | pages [5] -->
Communicative factor is measured by diversity, which equals to number of language that is spoken by over 100,000 people to 16 (the number of commonly used language we discuss in the paper). For example, if there are 10 languages spoken by over 100,000 people in that country, the score of communicative factor equals to 10/16 (0.625). So, the higher the diversity of language, the higher the percentage Ai for newly-born generation to speak a second language.

<!-- b000080 | prose | pages [5] -->
However, when considering economic factors, the economic development level may not have positive correlation to the percentage Ai. As far as we are concerned, people in developed countries may lack the motivation to study a second language although they have sufficient resources, while people in backwardcountries lack resources to learn. Therefore, people in developing countries who have moderate resources and highest passion have the highest likelihood to study. The level of economic development is divided into 3 groups according to the GDP per capita of the country. In the meantime, GDP per capita increases at different rate for countries in different development level, which is listed in

<!-- b000081 | caption | pages [5] -->
Table 1 below. Taking all these factors considered, we give a covering possibility of speaking

<!-- b000082 | prose | pages [5] -->
a second language for every country we discussed above.

<!-- b000083 | prose | pages [5] -->
Second Language Percentage (SLP)

<!-- b000084 | prose | pages [5] -->
50% 50% Communicative Communicative factor factor

<!-- b000085 | prose | pages [5] -->
Diversity GDP per capita Score=number/16

<!-- b000086 | prose | pages [5, 6] -->
Developed Developing Backward Score=0.4 Score=0.6 Score=0.2 Developed Developing Backward Countries Rate +2% +7% +3%

<!-- b000087 | caption | pages [5] -->
Figure 2 Principle to determine whether one speaks a second language

<!-- b000088 | caption | pages [5] -->
Figure 3 Classification of countries according to GDP per capita

<!-- b000089 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000090 | furniture | pages [6] -->
# Team

<!-- b000091 | furniture | pages [6] -->
Page 6 of 23

<!-- b000092 | caption | pages [6] -->
Table 1 Increasing rate of GDP per capita for countries in different development level

<!-- b000094 | prose | pages [6] -->
As for the choice of the second language, we take five factors into consideration – communication[3], geography, economy, knowledge[4] and diplomacy[5]. Each of the five factors contains some measurable parameters, for example, number of countries that speak the language (NOCS) and number of people that speak the language (NOPS) in geography section, GDP and number of top 10 economics in economy section. Among these parameters, some are global and have the same value for every country, such as NOCS and NOPS, while others are internal and differ from country to country, such as local GDP and domestic language distribution. This means people in different countries have different possibility to speak the same second language (ܲ 1݆1 ≠ Pi2j1), and people in the same country have different possibility to speak different second language 1݆1 ≠ܲ (ܲ 1݆2).

<!-- b000095 | prose | pages [6] -->
To determine the weights of each of the five sections, we use Analytical Hierarchy Process (AHP) to determine the weights. This method helps to convert our subjective preference to measurable weights to evaluate the importance of different factors.

<!-- b000096 | prose | pages [6] -->
We first build a 5*5 comparison matrix, each element of which shows the extent of preference between factor i and j. Since daily communication is important for people, and studying a second language usually have a close relationship to business and trade, we give them special preference, and obtain the following matrix.

<!-- b000097 | prose | pages [6] -->
Kno Dip Com Geo Eco 1 2 1 5 6 Com Geo 1 1/2 1 3 5 Eco 1 2 1 5 6 Kno 1/5 1/3 1/5 1 2 1/2 1 1/6 1/5 1/6 Dip Calculating the maximum eigenvalue and normalizing the corresponding eigenvector, we obtain the weights of each section, and divide them equally for the measurable subsections. The sections we consider together with their weight is shown in Figure 4 below.

<!-- b000098 | prose | pages [6] -->
Second language selection index

<!-- b000099 | prose | pages [6] -->
34.16% 19.67% 34.16% 7.32% 4.69%

<!-- b000100 | prose | pages [6] -->
Communication Geography Knowledge Diplomacy Economy

<!-- b000101 | prose | pages [6] -->
9.84% 9.84% 17.08% 17.08% 2.34% 2.34% 17.08% 17.08% 7.32%

<!-- b000102 | prose | pages [6] -->
Top 10 Official Internet Academi International Regional GDP NOCS NOPS c language

<!-- b000103 | heading | pages [6] -->
content

<!-- b000104 | contents | pages [6] -->
institution

<!-- b000105 | contents | pages [6] -->
institution

<!-- b000106 | contents | pages [6] -->
economics

<!-- b000107 | caption | pages [6] -->
Figure 4 Sections and their weight when determining which second language to speak

<!-- b000108 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000109 | furniture | pages [7] -->
# Team

<!-- b000110 | furniture | pages [7] -->
Page 7 of 23

<!-- b000111 | contents | pages [7] -->
To test the consistency of the matrix, we calculate the Consistency Ratio (CR), which is

<!-- b000112 | contents | pages [7] -->
defined as the ratio of Consistency Index (CI) to Average Random Consistency Index (RI).

<!-- b000113 | contents | pages [7] -->
ߣ

<!-- b000114 | contents | pages [7] -->
Since

<!-- b000115 | contents | pages [7] -->
R = 1.12 , and ܥR =

<!-- b000116 | contents | pages [7] -->
Ro−݊= 0.0115 , we get ܥR = 0.0103 < 0.1 , so the

<!-- b000117 | contents | pages [7] -->
= 5 ,

<!-- b000118 | contents | pages [7] -->
−1

<!-- b000119 | contents | pages [7] -->
consistency of the matrix is confirmed.

<!-- b000120 | heading | pages [7] -->
4.1.2 Stochastic Simulation Process

<!-- b000121 | prose | pages [7] -->
At the initial phase, we simply simulate the total number of speakers (TNOSi ) to simplify our model. Meanwhile, we take the dominant language to represent the native language of a certain country, and ignore the influence of migration. Therefore, the change of TNOSi is simply determined by the newly-born generation. When simulating the model on Python, we first calculate the product of Second Language Percentage (SLP) and the newly-born population of the country to determine the increased number of second language learner. Then we assign a random value between 0 and 1 to every 10,000 second language learners to determine which second language to learn. If the random value falls within the interval of a certain language, all people in the group are regarded to study the specific language.

<!-- b000122 | caption | pages [7] -->
Figure 5 Determination of which second language to speak

<!-- b000123 | prose | pages [7] -->
The first simulation result shows that moderate changes occur to the top ten list of total number of speakers. Two languages – Portuguese and Russian, are replaced by German and Japanese. The rank of the eight languages listed both in 2017 and 2067 also shows a slight difference.

<!-- b000124 | prose | pages [7] -->
As for the total number of speakers, most of the languages we analyze gain growth. The number of German speakers increases the fastest, up to 805.11%. The number of French and Japanese speakers also increases by over 500%. This is mainly because countries which speak these languages have high GDP, so people around the world tend to study these languages for economic reasons. Meanwhile, the original population base of these languages is not so high as Chinese/English speaking countries. The combination of the two aspects leads to this stunning result. If the threshold is reduced to 100%, up to 6 languages are included. But the language which develops the worst, the Russian, only record a -0.51% drop. This is due to the negative Net Birth Rate in Russia and few countries speaking Russian, which lead to decrease in domestic population and lack of new learners for communicative factors.

<!-- b000125 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000126 | furniture | pages [8] -->
# Team

<!-- b000127 | furniture | pages [8] -->
Page 8 of 23

<!-- b000128 | caption | pages [8] -->
Table 2 First simulation result

<!-- b000129 | prose | pages [8] -->
Rank in Rank in Population Population Increased Increased Language 2017 2067 in 2017 in 2067 rate (%) number English 1 1 1255857851 3172666602 152.63 1916808751 Chinese 2 2 1096961483 2278106986 107.67 1181145503 Spanish 3 3 520236718 1482532068 184.97 962295350 Hindi 4 7 449573687 480031690 6.77 30458003 Arabic 5 8 334611664 345470847 3.25 10859183 Malay 6 9 292434196 296957189 1.55 4522993 Bengali 7 10 246276800 248034947 0.71 1758147 French 8 4 242897420 1471076958 505.64 1228179538 Portuguese 9 11 229370143 238969091 4.18 9598948 Russian 10 12 207790825 206735561 -0.51 -1055264 Hausa 11 13 150021627 149734135 -0.19 -287492 Punjabi 12 14 147803740 149154483 0.91 1350743 Japanese 13 6 133972338 1135657916 747.68 1001685578 14 5 136642027 1236759996 805.11 1100117969 German 15 15 119207805 125462681 5.25 6254876 Persian 16 16 69081313 69250144 0.24 168831 Urdu

<!-- b000130 | caption | pages [8] -->
Figure 6 Change of total number and rank of the 16 languages over 50 years

<!-- b000131 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000132 | furniture | pages [9] -->
# Team

<!-- b000133 | furniture | pages [9] -->
Page 9 of 23

<!-- b000134 | caption | pages [9] -->
Figure 7 Change of language distribution around the world

<!-- b000135 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000136 | furniture | pages [10] -->
# Team

<!-- b000137 | furniture | pages [10] -->
Page 10 of 23

<!-- b000138 | prose | pages [10] -->
by subtraction. We get the following results:

<!-- b000139 | caption | pages [10] -->
Figure 8 Change of number of native speakers and rank of 16 languages over 50 years

<!-- b000140 | prose | pages [10] -->
Compared with the result of total speakers, we can see that the initial number of native Chinese speakers is more than that of English. However, native English speakers increase much faster than Chinese ones, and surpass Chinese in 2049. The number of other native language speakers also have a small difference from the total number. Meanwhile, we can see that the curve of native speakers is not so smooth as the total speakers one. This is the result of our simplification that we only take the dominant language to represent the native language of a country, so there may be sudden growth or drop of the number when the prevailing language of a country changes.

<!-- b000141 | prose | pages [10] -->
To better simulate the reality situation, we further consider the influence of migration. We assume that the moment the migration happens, all the immigrants instantly change their native language from their original one to the new one. The emigrant country subtracts thesame number of native language speakers as emigrant number, and immigrant country adds the number to their native language speakers. Meanwhile, immigrants’ original native language is counted into the second language of the new country.

<!-- b000142 | prose | pages [10] -->
Taking the influence of migration into account, little change occurs in the total number and native language speaker number of all these 16 languages. The development trend and speed are all similar to the former one without consideration of migration. This is attributed to the inconspicuous rate of migration, which is approximately one tenth of the average Net Birth Rate. Simulation result is shown in the following figure:

<!-- b000143 | caption | pages [10] -->
Figure 9 Simulation result when take migration into account

<!-- b000144 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000145 | furniture | pages [11] -->
# Team

<!-- b000146 | furniture | pages [11] -->
Page 11 of 23

<!-- b000147 | heading | pages [11] -->
4.2 Location Determination Model

<!-- b000148 | heading | pages [11] -->
4.2.1 Solution Oriented by Language Structure

<!-- b000149 | prose | pages [11] -->
To determine the location of the new offices, we build a Location Determination Model, using the results obtained from the Stochastic Language Development Model. Since international branch offices are usually set in well developed country, we simply focus on countries with GDP over 100 billion dollars, which helps reduce the number of country to 52. In the meantime, the capital of a country is usually the economic, political and transportation center, so we adopt the capital as the only candidate city for each country.

<!-- b000150 | prose | pages [11] -->
For these 52 countries (or you can say, their capitals), we employ Algorithms for Fuzzy Clustering (AFFZ) to separate them into 6 groups according to their similarity in language structure[6]. For each country, it generates a vector, each element of which stands for the total number of people speaking the specific language. The correlation between every two countries can be calculated through Angle Cosine Method:

<!-- b000151 | prose | pages [11] -->
With the correlation value, we create a Fuzzy Similar Matrix, and then generate a Fuzzy Equivalent Matrix to divide these 52 countries into 6 groups. For each group, we choose 1-3 languages to represent the characteristics of it.

<!-- b000152 | prose | pages [11] -->
The purpose of establishing an international new office is to get tight connection with economically developed countries and regions, so there are two objectives that we are concerned about most, namely the distance from the candidate country (or capital) to other countries, and the GDP distribution in the group. We hope that the office is built somewhere close to the well- developed countries, and we get the following expression for country j

<!-- b000153 | prose | pages [11] -->
In the expression, subscript i refers to country i, and݀ refers to the distance between country i and j. We square the GDP since we think that GDP is a more important factor compared with distance. The first section of the expression represents the effect of distance as well as GDP of other countries. When considering domestic condition, we also use the data of GDP and distance to keep the dimension coherent to the former. However, the distance can’t be 0, so we replace it with half of the distance from its closest country, which makes the value a minimum and not to be 0.

<!-- b000154 | prose | pages [11, 12] -->
The larger the value of the expression, the better a country to set the office in. So, we need to search for the maximum value in each group to determine the location. That means, the objective function is Running the solution program on Matlab using the current (2017) language structure of each country, we obtain the members of each group as the following table shows:

<!-- b000155 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000156 | furniture | pages [12] -->
# Team

<!-- b000157 | furniture | pages [12] -->
Page 12 of 23

<!-- b000159 | caption | pages [12] -->
Table 3 Current grouping result (solution 1)

<!-- b000160 | prose | pages [12] -->
Group Language Countries Number 1 Arabic Morocco, Algeria, Egypt, Iraq, Saudi Arabia 5 South Africa, Nigeria, Armenia, Kazakhstan, Kyrgyzstan, Vietnam, Singapore, Philippine, Spanish Thailand, South Korea, Japan, Romania, Greece, + Czechia, Finland, Austria, Belgium, Poland, French 2 38 Switzerland, Netherland, Spain, Russia, Italy, + France, Britain, Germany, Mexico, Puerto Rica, Russian Canada, New Zealand, Australia, Peru, Chile, Colombia, Venezuela, Argentina, China, America 3 Bengali Bangladesh 1 4 Malay Malaysia, Indonesia 2 Hindustani 5 India, Pakistan 2 Portuguese 6 Portugal, Brazil 2

<!-- b000161 | prose | pages [12] -->
Based on the latitude and longitude data of each country, we calculate the distance among them with simple Matlab program. Then we can get the value of the criterion expression of each country, therefore determine the countries for new offices. Final result of locations and the languages used in each office is shown in Table 4.

<!-- b000162 | caption | pages [12] -->
Table 4 Current locations and languages for each office

<!-- b000163 | prose | pages [12] -->
Saudi Arabia Germany Bangladesh Indonesia India Brazil Country (Riyadh) (Berlin) (Dhaka) (Jakarta) (New Delhi) (Brasilia) (Capital) Spanish, French, Language Arabic Bengali Malay Hindustani Portuguese Russia If we substitute the data of language structure and GDP with the future one in 2067 (GDP is regarded to increase at a constant speed as shown in Table 1), the grouping result and the locations as well as spoken languages will change as

<!-- b000164 | caption | pages [12] -->
Table 5 and Table 6 show below:

<!-- b000165 | caption | pages [12] -->
Table 5 Future grouping result

<!-- b000166 | prose | pages [12, 13] -->
Group Language Countries Number Arabic 1 Morocco, Algeria, Egypt, Iraq, Saudi Arabia 5 Brazil, Russia, Poland, India, Germany, Malaysia, Hindustani Britain, Kazakhstan, Indonesia, Canada, South + Korea, Australia, Netherland, Iran, Thailand, 2 29 Malay Switzerland, Nigeria, Philippine, South Africa, + Pakistan, Austria, Vietnam, Singapore, Finland, German Czechia, New Zealand, Botswana, China, America 3 Bangladesh 1 Bengali Mexico, Argentina, Venezuela, Chile, Peru, 4 Spanish 13 Romania, Italy, Spain, Ecuador, Cuba, Dominican Republic, Colombia, Portugal Japanese 5 Japan 1 6 French France, Belgium 2

<!-- b000167 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000168 | furniture | pages [13] -->
# Team

<!-- b000169 | furniture | pages [13] -->
Page 13 of 23

<!-- b000171 | caption | pages [13] -->
Table 6 Future locations and languages for each office

<!-- b000172 | prose | pages [13] -->
Saudi Arabia Poland Bangladesh Japan France Argentina Country (Riyadh) (Warsaw) (Dhaka) (Tokyo) (Paris) (Buenos Aires) (Capital) Hindustani, Language Arabic Malay, Bengali Japanese French Portuguese German

<!-- b000173 | heading | pages [13] -->
4.2.2 Solution Oriented by Geographic Condition

<!-- b000174 | prose | pages [13] -->
As we can see, the result produced by solution oriented by language structure can hardly be regarded as the ideal locations for new office. In fact, although relatively little languages are considered such as Arabic and Bengali and it is easy to determine what languages to speak in each new office, the locations are unsatisfactory from the economic point of view. This can be stem from the huge difference of the 6 groups, one of which contains 38 countries spreading on almost every continent, covering nearly 75% of the total countries we discuss. The remaining 14 countries are all relatively small or medium countries, and have mediocre economic level, which are not suitable locations for international business.

<!-- b000175 | prose | pages [13] -->
Since then, we shift our way of thinking, and first decide how many offices to build on each continent (totally 6 worldwide) according to the economic development. For continents with n (n> 1) offices, we divide them into n parts based on the geographic location of each country, applying P Center Method while grouping. That means, if there are two offices in Europe, we randomly take two countries of it, and sum up the smaller value of the distance between anther country and these two. After traversing all cases, we select two countries with the minimum value as the reference countries, marked as A, B. Then we add other countries into the group of country A or B on the basis of their distance from these countries. For example, another country C has shorter distance to country B than country A, then it is added to the second group.

<!-- b000176 | caption | pages [13] -->
Figure 10 The grouping process

<!-- b000177 | prose | pages [13, 14] -->
After the grouping process, we use the same criterion expression as the solution oriented by language structure to determine the optimal office location for each group. Algorithms for Fuzzy Clustering (AFFZ) is applied to finally decide what language to speak in the office. We observe the characteristics of language structure of clustered group with most countries, and choose 1-3 languages that have great amount of speakers.

<!-- b000178 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000179 | furniture | pages [14] -->
# Team

<!-- b000180 | furniture | pages [14] -->
Page 14 of 23

<!-- b000182 | prose | pages [14] -->
Determine which Provide the initial Determine what More than 1 country toestablish office number of office languages to speak No the new office on a continent? on eachcontinent in the office (Objective function)

<!-- b000183 | prose | pages [14] -->
Yes Divide the countries into n groups (P Center Method)

<!-- b000184 | caption | pages [14] -->
Figure 11 Process of solution oriented

<!-- b000185 | prose | pages [14] -->
When simulating the solution on Matlab program, we take the original two offices in Shanghai and New York into consideration since they also contribute to connection with other countries around them, which may influence the location selection. That means, we suggest originally there is no office anywhere on Earth, and we need to distribute 8 offices around the world, and see if the results include companies in China and the United States. The number of offices distributed around the world is initially set as the following table:

<!-- b000186 | caption | pages [14] -->
Table 7 Initial distribution of office number

<!-- b000187 | prose | pages [14] -->
Continent Asia Europe North America South America Oceania Africa Number 2 2 1 1 1 1

<!-- b000188 | prose | pages [14] -->
For Asia and Europe, two offices are set, so P Center Method is applied to separate their countries into two groups. For other continents, only one office is set, so the grouping process is skipped. Russia is regarded as an Asian country because geographically most of its territory locates in Asia.

<!-- b000189 | prose | pages [14] -->
We discuss the current and future situation separately. The result of the 8 groups for current situation is shown as following:

<!-- b000190 | caption | pages [14] -->
Table 8 Current grouping result (Solution 2)

<!-- b000191 | prose | pages [14, 15] -->
Group Continent Members Vietnam Bangladesh Singapore Thailand South Korea Asia 1 Japan China Malaysia Philippines Indonesia India Pakistan Armenia Kazakhstan Kyrgyzstan Asia 2 Iraq Iran Saudi Arabia Russia Hungary Greece Austria Poland Romania 3 Europe Czechia Finland Italy Belgium Switzerland Netherlands France Britain 4 Europe Germany Portugal Spain North 5 Puerto Rico Mexico Canada America America Peru Chile Colombia Venezuela Argentina South 6 America Brazil 7 New Zealand Australia Oceania 8 Morocco Algeria South Africa Egypt Nigeria Africa Using the objective function mentioned above to evaluate the suitability of each country in a group, we obtain the optimal location for the new offices in 2017. The result also validate that China and the United States of America are ideal locations to set offices in. Figure 12 distinctly shows the location of offices and corresponding relative members in the same group on the map of the world.

<!-- b000192 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000193 | furniture | pages [15] -->
# Team

<!-- b000194 | furniture | pages [15] -->
Page 15 of 23

<!-- b000196 | caption | pages [15] -->
Figure 12 Location of offices worldwide in 2017

<!-- b000197 | prose | pages [15] -->
The languages spoken in each country are shown in the table below:

<!-- b000198 | caption | pages [15] -->
Table 9 Languages spoken in each office in 2017

<!-- b000199 | prose | pages [15] -->
India America Country Nigeria China Italy Germany Brazil Australia (New (New (Capital) (Abuja) (Shanghai) (Rome) (Berlin) (Brasilia) (Canberra) Delhi) York) Russian, German, Chinese, Spanish, Language Arabic Hindistani, German French, Spanish Spanish Japanese French Punjabi Spanish

<!-- b000200 | prose | pages [15] -->
If the data is replaced by the one in 2067, Italy and India are replaced by Poland and Russia. China and America still exist in the list, once again validating their suitability to be the location for international offices. Meanwhile, small changes occur in languages spoken because of different develop speed of different languages. The grouping result, the final locations of offices and the languages spoken are shown below.

<!-- b000201 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000202 | furniture | pages [16] -->
# Team

<!-- b000203 | furniture | pages [16] -->
Page 16 of 23

<!-- b000204 | prose | pages [16] -->
Table 10 Future grouping result (solution 2) Group Continent Members Vietnam Bangladesh Singapore Thailand South Korea 1 Asia Japan China Malaysia Philippines Indonesia India Pakistan Saudi Arabia Kazakhstan Russia 2 Asia Iraq Iran Hungary Greece Austria Poland Romania 3 Europe Czechia Finland Italy Croatia Belgium Switzerland Netherlands France Britain 4 Europe Germany Portugal Spain North Dominican 5 Cuba Mexico Canada America Republic America Peru Chile Colombia Venezuela Argentina South 6 America Brazil Ecuador Oceania 7 New Zealand Australia South 8 Africa Algeria Egypt Nigeria Africa

<!-- b000205 | caption | pages [16] -->
Figure 13 Location of offices worldwide in 2067

<!-- b000206 | caption | pages [16] -->
Table 11 Languages spoken in each office in 2067

<!-- b000207 | prose | pages [16] -->
Nigeria Russia China Poland Germany America Brazil Australia Country (Abuja) (Moscow) (Shanghai) (Warsaw) (Berlin) (New York) (Brasilia) (Canberra) (Capital) German, Russian, Chinese, Language Arabic German French, Spanish Spanish Malay Hindistani Japanese Spanish

<!-- b000208 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000209 | furniture | pages [17] -->
# Team

<!-- b000210 | furniture | pages [17] -->
Page 17 of 23

<!-- b000211 | heading | pages [17] -->
5. Sensitivity Analysis

<!-- b000212 | heading | pages [17] -->
5.1 Sensitivity Analysis on Language Development Model

<!-- b000213 | prose | pages [17] -->
In the Language Development Model, the Net Birth Rate, GDP growth rate and migration rate will have an impact on the results. Therefore, it is necessary to analyze the impact of these three factors on the simulation results.

<!-- b000214 | heading | pages [17] -->
5.1.1 Net Birth Rate Impact

<!-- b000215 | prose | pages [17] -->
The Net Birth Rate in each country is the main motivation behind the language development, here we reduce and increase the net birth rate of all countries by 20% and 10%, and use the Language Development Model to calculate the total number of 16 languages speakers after 50 years. The relative changes are shown in the following table.

<!-- b000216 | caption | pages [17] -->
Table 12 Analytical result of Net Birth Rate impact

<!-- b000217 | prose | pages [17] -->
Change of Net -20% -10% +10% +20% Birth Rate Chinese -13.60% -6.50% 10.53% 20.22% English -13.84% -5.41% 13.07% 24.76% Hindi -0.05% -0.55% 0.85% 0.73% Urdu 0.75% -0.84% -0.16% -1.03% Spanish -18.45% -9.99% 10.34% 23.82% Arabic 3.20% -3.05% 2.41% 2.30% Malay -1.56% -1.53% 1.53% 1.50% Russian -1.89% -1.91% -1.01% -0.78% Bengali -0.72% -0.76% 0.73% 0.74% Portuguese -4.66% -4.42% 4.29% 3.87% French -24.35% -13.02% 14.00% 27.69% Hausa -0.26% -0.04% 0.02% -0.19% Punjabi -1.28% 0.88% 1.07% 0.93% Japanese -28.38% -13.96% 17.91% 34.08% German -25.32% -14.07% 16.50% 36.66% Persian -5.90% -5.69% 5.39% 5.27% As can be seen from the above table, for most languages, the number of language speakers is positively correlated with the Net Birth Rate. In other words, as the Net Birth Rate rises, the number of language speakers increases, and as the Net Birth Rate decreases, the number of language speakers drops. This result is consistent with common sense. From this perspective, we can say that this model accurately simulates the reality situation. In addition, all the changes in this table are less than 40%. Therefore, the model can be considered as a robust one.

<!-- b000218 | heading | pages [17] -->
5.1.2 GDP Growth Rate Impact

<!-- b000219 | prose | pages [17, 18] -->
The growth rate of GDP used in the Language Development Model was 2% in developed countries, 7% in developing countries and 3% in backward countries. Now we change these three numbers by -50%, -10%, +10%, +100%, and use the Language Development Model to calculate the total number of 16 languages speakers after 50 years. The relative changes are shown in the following table.

<!-- b000220 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000221 | furniture | pages [18] -->
# Team

<!-- b000222 | furniture | pages [18] -->
Page 18 of 23

<!-- b000224 | caption | pages [18] -->
Table 13 Analytical result of GDP Growth Rate impact

<!-- b000225 | prose | pages [18] -->
GDP increase rate -50% -10% +10% +100% Chinese -0.51% -0.49% 1.45% 2.49% English -2.88% -2.15% 3.62% 1.52% Hindi 0.32% 0.69% 0.24% 1.40% Urdu -0.28% -0.30% -0.07% 0.05% Spanish -0.20% -1.44% -2.20% 0.99% Arabic -2.47% -2.71% 2.82% 2.16% Malay -1.58% -1.58% 1.58% 1.58% Russian -0.62% -0.45% -0.65% 0.84% -0.75% -0.75% 0.75% 0.75% Bengali Portuguese -4.32% -4.34% 4.30% 4.39% French -1.64% -1.92% 0.62% 0.27% -0.13% -0.13% -0.13% -0.13% Hausa -1.96% -0.73% 0.85% 1.56% Punjabi Japanese -1.18% -0.80% 1.68% 3.66% German -2.38% 0.38% 0.30% 1.71% Persian 5.50% 5.58% 5.58% 5.50%

<!-- b000226 | prose | pages [18] -->
As can be seen from the above table, the increase in GDP growth rate will cause an increase in the number of most languages. However, even in the case of GDP growth rate increases by 100%, the total population of languages will not change much (the maximum is only 3.66%). Therefore, the change in the GDP growth rate has little effect on the result of the population after 50 years.

<!-- b000227 | heading | pages [18] -->
5.1.3 Migration Rate Impact

<!-- b000228 | prose | pages [18] -->
By increasing and decreasing the migration rate in each country, we calculate the total population change of each language after 50 years.

<!-- b000229 | caption | pages [18] -->
Table 14 Analytical result of Migration Rate impact

<!-- b000230 | prose | pages [18, 19] -->
Migration Rate -20% -10% +10% +20% Chinese 3.16% -0.81% -3.51% -8.30% English -4.23% -2.18% 3.40% 5.27% Hindi 1.14% 0.00% -5.20% -6.86% 0.00% 0.00% 0.19% 0.00% Urdu -0.12% -0.08% 1.10% 1.42% Spanish 0.15% 0.40% -1.34% -1.77% Arabic -3.80% -6.94% -9.11% -23.48% Malay 0.20% -0.01% -0.40% -0.34% Russian 0.08% 0.06% 0.03% -0.01% Bengali -0.17% -0.15% -0.07% -0.05% Portuguese -1.00% 0.09% -0.60% -0.23% French Hausa -0.11% -0.15% -0.13% -0.07% Punjabi 0.06% -0.02% 0.04% 0.01% Japanese -0.10% -1.44% 8.51% 3.59% German -0.51% -0.32% -1.12% 4.30% Persian -0.68% -0.44% -0.59% 0.17%

<!-- b000231 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000232 | furniture | pages [19] -->
# Team

<!-- b000233 | furniture | pages [19] -->
Page 19 of 23

<!-- b000235 | prose | pages [19] -->
From this table, we can see that the number of Chinese, Hindi and Malay speakers are negatively correlated with migration rate, while the total number of speakers of English and Japanese are positive correlated with it. This is because people speaking Chinese, Malay and Hindi have stronger tendency to migrate and lots of them choose English-speaking countries as their second hometown.

<!-- b000236 | heading | pages [19] -->
5.2 Sensitivity Analysis on Location Determination Model

<!-- b000237 | prose | pages [19] -->
As is shown in 4.2, three factors contribute to the final locations for the new offices – geographic position, language structure and economic condition measured by GDP.

<!-- b000238 | prose | pages [19] -->
In our model, the impact of a country’s geographic position is expressed by distance. As the position of a country is not likely to change over time, we do not pay much attention to the sensitivity of this factor. Language structure, which is affected by net birth rate, migration and GDP growth, plays a significant role when deciding what language should be spoken in the new offices, but it is less important in the position-determining step. Consequently, in the sensitivity analysis section, we mainly focus on the fluctuation of GDP growth and its influences.

<!-- b000239 | prose | pages [19] -->
Similar as what we have done in section 5.1.2, we again apply a -50%, -10%, +10% and +100% variation to the GDP growth rate, and record the recommending countries for new offices under each circumstance, respectively. Wespot notable changes.

<!-- b000240 | prose | pages [19] -->
Table 15 Sensitivity Analysis of Location Determination Model Group Group Group Group Recommanded Recommanded Recommanded Recommanded members members members members Country Country Country Country Variation Variation Variation Variation GDP growth rate -50% -10% +10% +100% variation Africa +0 Nigeria +0 Nigeria +2 South Africa +4 Botswana +0 Russia +0 Russia +0 Russia +0 Russia Asia +0 China +0 China +0 China +0 China +0 Germany +0 Germany +0 Germany -2 Germany Europe +0 Poland +0 Poland -1 Poland -1 Poland North America +0 USA +0 USA +0 Mexico +0 Mexico Oceanic +0 Australia +0 Australia -1 Australia -1 Australia South America +0 Brazil +0 Brazil +0 Brazil +0 Brazil From the table above we can conclude that:

<!-- b000241 | prose | pages [19] -->
If the GDP growth rate decreases, neither the group members nor the recommended country  changes.

<!-- b000242 | prose | pages [19] -->
If the GDP growth rate increases, there tends to be more group members for Africa and less  members for Europe and Oceanic. Meanwhile, the recommended countries alter.

<!-- b000243 | prose | pages [19] -->
This phenomenon can be explained by the difference of GDP growing speed between developing and developed countries. When GDP growth rate increases, the difference broadens, meaning that more developing countries will take the place of the developed ones. It is natural that Africa attracts more attention, and we have more developing countries in the recommend list.

<!-- b000244 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000245 | furniture | pages [20] -->
# Team

<!-- b000246 | furniture | pages [20] -->
Page 20 of 23

<!-- b000247 | heading | pages [20] -->
6. Further Discussion

<!-- b000248 | prose | pages [20] -->
Because the Location Determination Model produces just passable result through the solution oriented by language structure, we apply the latter solution oriented by geographic condition to further discuss whether 5 or even less offices to open can be applicable.

<!-- b000249 | prose | pages [20] -->
Since this solution does not make any restriction on the number of new office, the company can choose to open any arbitrary number of office based on its actual financial condition. As long as the company has a preliminary planning of how many new offices to open and which continent they are located at, we can provide the exact location of each office immediately.

<!-- b000250 | prose | pages [20] -->
For example, suggest the company decides to cut an office in Europe and open 5 offices in total, it won’t affect the location of other offices in other continents, but may change the location of Europe. Calculating this situation on Matlab program, we get the result of short-term andlong- term decision shown in the following figure.

<!-- b000251 | caption | pages [20] -->
Figure 14 Changes in the location of Europe continent

<!-- b000252 | prose | pages [20] -->
Therefore, we can say that our model with the geographic-condition-oriented solution has strong adaptability to various situations and is a simple but also feasible method to provide advice on selection of new offices location.

<!-- b000253 | heading | pages [20] -->
7. Strengths and Weaknesses

<!-- b000254 | heading | pages [20] -->
7.1 Strengths

<!-- b000255 | prose | pages [20] -->
Based on the AHP method, the Language Development Model fully considers the influence  of many possible factors on language development, including communication, geography, economy, academy and diplomacy. Therefore, the result of the model is highly credible.

<!-- b000256 | prose | pages [20] -->
The Language Development Model takes country rather than language as the unit of  simulation. So, it can not only model the development of a certain language over time, but also model the linguistic structure of any given country over time.

<!-- b000257 | prose | pages [20] -->
We looked into the location determination problem from two different aspects: the similarity  of linguistic structure and the geographic distance between countries. We made a judgement on the priority of these two factors and improved our model.

<!-- b000258 | prose | pages [20, 21] -->
The Location Determination Model can reflect the economic consideration of a modern  international company as GDP plays an important role when determining the location for new offices.

<!-- b000259 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000260 | furniture | pages [21] -->
# Team

<!-- b000261 | furniture | pages [21] -->
Page 21 of 23

<!-- b000263 | prose | pages [21] -->
Flexibility and adaptability are also advantages of the Location Determination Model. When  the company change its strategy, new decisions can be quickly derived without modifying the algorithm.

<!-- b000264 | heading | pages [21] -->
7.2 Weaknesses

<!-- b000265 | prose | pages [21] -->
In our model, to simplify our model, only the language with the largest number of speakers is  considered as the native language of a country. But in fact, there might be two or even more native languages in a country.

<!-- b000266 | prose | pages [21] -->
The objective function to optimize the position of new offices is determined with a certain  degree of arbitrariness. It can be further improved to meet different actual needs.

<!-- b000267 | prose | pages [21] -->
The correctness of our conclusions relies heavily on the accuracy of the data collected and the  estimates of GDP, language and population development.

<!-- b000268 | prose | pages [21] -->
The recommendation provided by our model remains at the stage of countries (capitals).  Further analyses are required in order to determine the specific cities.

<!-- b000269 | heading | pages [21] -->
7. Conclusion

<!-- b000270 | prose | pages [21] -->
To predict the future distribution of commonly used languages, we build a Language Development Model, setting up 2 criteria to estimate the percentage of speaking a second language, 5 factors to evaluate which second language to speak. Then we simulate the model on Python, using data of population, GDP, language structure and etc. of over 50 countries we collected on the Internet. We conclude that only moderate changes occur to top ten language list, and most of the 16 languages we discuss gain a growth in their total speaker number.

<!-- b000271 | prose | pages [21] -->
To further provide advice to the multinational service company, we build a Location Determination Model, applying two solutions to figure out the suitable locations for establishment of new offices. The first solution oriented by language structure produced just passable result without comprehensive consideration on economic condition. The second solution, if provided initial number of office on each continent, produces generally ideal locations, and new decisions can be quickly derived if the company change its strategy.

<!-- b000272 | heading | pages [21] -->
Reference

<!-- b000273 | references | pages [21] -->
[1] http://data.un.org/Data.aspx

<!-- b000274 | references | pages [21] -->
[2] https://www.cia.gov/library/publications/resources

<!-- b000275 | references | pages [21] -->
[3] https://w3techs.com/technologies/overview/content_language/all

<!-- b000276 | references | pages [21] -->
[4] http://akarlin.com/2011/05/top-10-most-useful-languages/

<!-- b000277 | references | pages [21] -->
[5] Kai L. Chan, PhD, POWER LANGUAGE INDEX, May 2016

<!-- b000278 | references | pages [21] -->
[6] Gustafson, D. E. (1979). Fuzzy clustering with a fuzzy covariance matrix. Proc of IEEE Cdc

<!-- b000279 | references | pages [21] -->
San Diago Ca, 2, 761-766.

<!-- b000280 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000281 | furniture | pages [22] -->
# Team

<!-- b000282 | furniture | pages [22] -->
Page 22 of 23

<!-- b000283 | heading | pages [22] -->
Memo to the Service Company

<!-- b000284 | prose | pages [22] -->
Dear Chief Operating Officer, We are glad to hear your recent plan about opening six new international offices, which will definitely be an important milestone for your company to become truly international. For such a significant plan, it is necessary to carry out some research before making the final decision. To assist you to decide the location of new offices and determine the languages spoken in the offices, we performed investigations using mathematical modelling.

<!-- b000285 | prose | pages [22] -->
Firstly, we build up a Language Development model to investigate the distribution ofvarious language speakers over time. In this model, we consider many possible influencing factors, including economy, geography, communication, knowledge and diplomacy. This model is based on data from the United Nation (UN). Through our calculations and tests, we found that this model can really help us to predict the future of language development. It is indicated in this model that over the next 50 years, two original most spoken languages (Russian and Portuguese) will be replaced (by German and Japanese), while the total number of speakers of most languages will gain an impressive increase.

<!-- b000286 | prose | pages [22] -->
Based on the model of language distribution, combined with Algorithm for Fuzzy Clustering method and P-Center method, we develop a Location Determination Model using two solutions to further provide a recommendation for your company to select the location of your new international office and its working language. One of the solution is oriented by language structure, and the other by geographic condition. Taking language distribution as well as economic development of different countries into account, we suggest to locate new offices in the capitals of Nigeria, India, Germany, Italy, Brazil, Australia for short-term interest. These six locations as well as the languages to be used in the new offices are as the following:

<!-- b000287 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000288 | furniture | pages [23] -->
# Team

<!-- b000289 | furniture | pages [23] -->
Page 23 of 23

<!-- b000290 | prose | pages [23] -->
Recommended Location for New Offices Language(s) to be Used New York, America Spanish Shanghai, China Chinese and Japanese Moscow, Russia Russian and Hindustani Warsaw, Poland German Berlin, Germany German, French and Spanish Abuja, Nigeria Arabic Brasilia, Brazil Spanish Canberra, Australia Malay

<!-- b000291 | prose | pages [23] -->
Considering from long-term perspective, your company should build these six new offices in

<!-- b000292 | prose | pages [23] -->
the capitals of Nigeria, Russia, Germany, Poland, Brazil and Australia. Moreover, since our model

<!-- b000293 | prose | pages [23] -->
makes no restriction on number of new office, you can set arbitrary number of offices based on

<!-- b000294 | prose | pages [23] -->
your actual financial condition. As long as you make a preliminary planning of how many new

<!-- b000295 | prose | pages [23] -->
offices to open and which continents they are located at, we can provide the exact location of each

<!-- b000296 | prose | pages [23] -->
office immediately.

<!-- b000297 | prose | pages [23] -->
We hope that our suggestion can provide useful information for you.

<!-- b000298 | prose | pages [23] -->
Yours sincerely,

<!-- b000299 | furniture | pages [23] -->
Team #77238
