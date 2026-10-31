For office use only For office use only 77238 T1 F1 T2 F2 Problem Chosen T3 F3 B F4 T4

2018 MCM/ICM

Summary Sheet

Summary

Thousands of languages are spoken around on the Earth, and over 40% of people take one of the top ten most spoken language as their mother tongue. Meanwhile, more and more people are learning a second language to meet the rapid development of economy and globalization.

Aimed to predict the distribution of widespread language speakers over the next 50 years, we build a Language Development Model, and apply it to countries with a population over 10 million to describe the possibility of the new generation in a certain country studying a certain second language. We employ the Analytical Hierarchy Process (AHP) to determine the specific parameters, and carry out stochastic simulation on Python to produce the results, which shows that mild change takes place on the list of popular languages – only two of the top-10 languages are replaced, while the total number of speakers of several languages gains an impressive increase.

Based on the language distribution model we obtain, we develop a Location Determination Model. The dual-solution model further provide a recommendation for a large multinational service company to select the location of their new international office. One of the solution is oriented by language structure, and the other by geographic condition. Taking language distribution as well as economic development of different countries into account, the model suggests that new offices should be located in Nigeria, India, Germany, Italy, Brazil, Australia for short-term interest, and Nigeria, Russia, Germany, Poland, Brazil, Australia for long-term development.

The sensitivity analysis shows the strong robustness of our model. Variation of key parameters causes moderate changes to the computing result. When we test the sensitivity, we indirectly validate our model’s conformance with reality that the direction of fluctuation of the result matches situations in real world. Meanwhile, we further discuss the impact of reducing the number of new office, and provide practicable advice on location determination of new offices.

1. Introduction

Language is the most important communication tool for human beings. Today, over 6000 languages are spoken on Earth, which help preserve and inherit human civilization and achievements. While everyone has his/her own native language which seldom changes all over his/her life, the number of people speaking a second language keeps increasing not only because of domestic factors such as school studying or governmental promotion, but also international factors including growing migration, booming global tourism and close communication online. Considering both native and second language speakers, great changes take place in language distribution and the number of speakers.

To investigate how the commonly used languages scatter worldwide, we develop a Language Development Model to forecast the future development of the 16 most spoken languages counted in 2017. Based on the original distribution of different languages and the Net Birth Rate of these countries, we build the model to simulate how language distribution changes over the next 50 years.

After obtaining the result from the Language Development Model, we build a Location Determination Model using two different solutions. For the former one, we group the countries based on their language structure. For the latter one, they are separated according to their geographic condition. After the grouping process, we set two goals to filter an optimal location for the new office in each group, namely GDP distribution and distance from other countries in the same group. Besides, we give recommended spoken language in these new offices.

2. Assumptions and Justification

We make some general assumptions to simplify our model. These assumptions together with corresponding justification are listed below:

All people take a certain language as their native language, but not every of them speaks  a second language.

Language is an indispensable tool for every person, so all people can speak at least one language, either commonly or rarely used. However, whether one speaks an additional second language depends on multiple reasons, for example, the developmental level of his/her country.

All existing people won’t change their native and second language.  People usually speak the same native language through his/her life. We do not consider change in native language caused by migration or other factors in the simplified model. The influence of migration will be discussed in 4.1.1.

The new generation all take their parents’ native language as their own native language.  However, their choice of the second language varies for several reasons discussed in 4.1.1.

Few families are composed of members speaking different native language. Meanwhile, the specific data is hard to derive. So, we ignore the influence of the multi-composed families and assume that children all take their parents’ native language as their own nativelanguage. More detailed assumptions will be listed if needed.

3. Notation

4. Model

4.1 Language Development Model

To discuss the changes of the top-ten language list, we analyze 16 currently most spoken languages. We gather the characteristics of language distribution of different countries to produce a global language distribution. To reduce the amount of calculation, we only consider countries with a population over 10 million, since they have contributed about 92% of total population on Earth as shown in Appendix 1. To simplify our model, we suggest the language with the most speakers represent the native language of a certain country. For each country, we acquire its population data from 2007 to 2017 on the United Nation Database [1], and obtain its Net Birth Rate to calculate its newly-born population every year. Meanwhile, the percentage of different language speakers is acquired [1,2] so that we can know the current language structure of the country. Through careful analysis of every country we take into account, we seek to obtain the language distribution all over the world.

4.1.1 Judgment Process

Weassumed that the existing people won’t make a change on their native and second language, and the newly-born population all take their parents’ native language as their own native language. Therefore, the numerical development of a certain language is completely determined by the newly increased population. However, not all of them will speak a second language, and which language they will take as their second language varies for economic, social, political and other reasons. So, we divide the judgment process into two steps – first to judge whether one will speak a second language, and then which language he/she will take. The judgment process of our Language Development Model is shown in Figure 1.

No

Chinese Which language? English Speak various Newly-born Speak a second language? (communication, Yes Pij second language population French (Communication and economy) geography, economy, (Ai) knowledge, diplomacy) ……

(1-Ai)

Speak only one language To quantify various reasons that affect the second language, we first take communicative and economic factors to determine if one speaks a second language in our analysis. Both two factors weigh 0.5 when calculating the possibility.

Communicative factor is measured by diversity, which equals to number of language that is spoken by over 100,000 people to 16 (the number of commonly used language we discuss in the paper). For example, if there are 10 languages spoken by over 100,000 people in that country, the score of communicative factor equals to 10/16 (0.625). So, the higher the diversity of language, the higher the percentage Ai for newly-born generation to speak a second language.

However, when considering economic factors, the economic development level may not have positive correlation to the percentage Ai. As far as we are concerned, people in developed countries may lack the motivation to study a second language although they have sufficient resources, while people in backwardcountries lack resources to learn. Therefore, people in developing countries who have moderate resources and highest passion have the highest likelihood to study. The level of economic development is divided into 3 groups according to the GDP per capita of the country. In the meantime, GDP per capita increases at different rate for countries in different development level, which is listed in

a second language for every country we discussed above.

Second Language Percentage (SLP)

50% 50% Communicative Communicative factor factor

Diversity GDP per capita Score=number/16

Developed Developing Backward Score=0.4 Score=0.6 Score=0.2 Developed Developing Backward Countries Rate +2% +7% +3%

As for the choice of the second language, we take five factors into consideration – communication[3], geography, economy, knowledge[4] and diplomacy[5]. Each of the five factors contains some measurable parameters, for example, number of countries that speak the language (NOCS) and number of people that speak the language (NOPS) in geography section, GDP and number of top 10 economics in economy section. Among these parameters, some are global and have the same value for every country, such as NOCS and NOPS, while others are internal and differ from country to country, such as local GDP and domestic language distribution. This means people in different countries have different possibility to speak the same second language (ܲ 1݆1 ≠ Pi2j1), and people in the same country have different possibility to speak different second language 1݆1 ≠ܲ (ܲ 1݆2).

To determine the weights of each of the five sections, we use Analytical Hierarchy Process (AHP) to determine the weights. This method helps to convert our subjective preference to measurable weights to evaluate the importance of different factors.

We first build a 5*5 comparison matrix, each element of which shows the extent of preference between factor i and j. Since daily communication is important for people, and studying a second language usually have a close relationship to business and trade, we give them special preference, and obtain the following matrix.

Kno Dip Com Geo Eco 1 2 1 5 6 Com Geo 1 1/2 1 3 5 Eco 1 2 1 5 6 Kno 1/5 1/3 1/5 1 2 1/2 1 1/6 1/5 1/6 Dip Calculating the maximum eigenvalue and normalizing the corresponding eigenvector, we obtain the weights of each section, and divide them equally for the measurable subsections. The sections we consider together with their weight is shown in Figure 4 below.

Second language selection index

34.16% 19.67% 34.16% 7.32% 4.69%

Communication Geography Knowledge Diplomacy Economy

9.84% 9.84% 17.08% 17.08% 2.34% 2.34% 17.08% 17.08% 7.32%

Top 10 Official Internet Academi International Regional GDP NOCS NOPS c language

5. Sensitivity Analysis

5.1 Sensitivity Analysis on Language Development Model

In the Language Development Model, the Net Birth Rate, GDP growth rate and migration rate will have an impact on the results. Therefore, it is necessary to analyze the impact of these three factors on the simulation results.

5.1.1 Net Birth Rate Impact

The Net Birth Rate in each country is the main motivation behind the language development, here we reduce and increase the net birth rate of all countries by 20% and 10%, and use the Language Development Model to calculate the total number of 16 languages speakers after 50 years. The relative changes are shown in the following table.

Change of Net -20% -10% +10% +20% Birth Rate Chinese -13.60% -6.50% 10.53% 20.22% English -13.84% -5.41% 13.07% 24.76% Hindi -0.05% -0.55% 0.85% 0.73% Urdu 0.75% -0.84% -0.16% -1.03% Spanish -18.45% -9.99% 10.34% 23.82% Arabic 3.20% -3.05% 2.41% 2.30% Malay -1.56% -1.53% 1.53% 1.50% Russian -1.89% -1.91% -1.01% -0.78% Bengali -0.72% -0.76% 0.73% 0.74% Portuguese -4.66% -4.42% 4.29% 3.87% French -24.35% -13.02% 14.00% 27.69% Hausa -0.26% -0.04% 0.02% -0.19% Punjabi -1.28% 0.88% 1.07% 0.93% Japanese -28.38% -13.96% 17.91% 34.08% German -25.32% -14.07% 16.50% 36.66% Persian -5.90% -5.69% 5.39% 5.27% As can be seen from the above table, for most languages, the number of language speakers is positively correlated with the Net Birth Rate. In other words, as the Net Birth Rate rises, the number of language speakers increases, and as the Net Birth Rate decreases, the number of language speakers drops. This result is consistent with common sense. From this perspective, we can say that this model accurately simulates the reality situation. In addition, all the changes in this table are less than 40%. Therefore, the model can be considered as a robust one.

5.1.2 GDP Growth Rate Impact

The growth rate of GDP used in the Language Development Model was 2% in developed countries, 7% in developing countries and 3% in backward countries. Now we change these three numbers by -50%, -10%, +10%, +100%, and use the Language Development Model to calculate the total number of 16 languages speakers after 50 years. The relative changes are shown in the following table.

GDP increase rate -50% -10% +10% +100% Chinese -0.51% -0.49% 1.45% 2.49% English -2.88% -2.15% 3.62% 1.52% Hindi 0.32% 0.69% 0.24% 1.40% Urdu -0.28% -0.30% -0.07% 0.05% Spanish -0.20% -1.44% -2.20% 0.99% Arabic -2.47% -2.71% 2.82% 2.16% Malay -1.58% -1.58% 1.58% 1.58% Russian -0.62% -0.45% -0.65% 0.84% -0.75% -0.75% 0.75% 0.75% Bengali Portuguese -4.32% -4.34% 4.30% 4.39% French -1.64% -1.92% 0.62% 0.27% -0.13% -0.13% -0.13% -0.13% Hausa -1.96% -0.73% 0.85% 1.56% Punjabi Japanese -1.18% -0.80% 1.68% 3.66% German -2.38% 0.38% 0.30% 1.71% Persian 5.50% 5.58% 5.58% 5.50%

As can be seen from the above table, the increase in GDP growth rate will cause an increase in the number of most languages. However, even in the case of GDP growth rate increases by 100%, the total population of languages will not change much (the maximum is only 3.66%). Therefore, the change in the GDP growth rate has little effect on the result of the population after 50 years.

5.1.3 Migration Rate Impact

By increasing and decreasing the migration rate in each country, we calculate the total population change of each language after 50 years.

Migration Rate -20% -10% +10% +20% Chinese 3.16% -0.81% -3.51% -8.30% English -4.23% -2.18% 3.40% 5.27% Hindi 1.14% 0.00% -5.20% -6.86% 0.00% 0.00% 0.19% 0.00% Urdu -0.12% -0.08% 1.10% 1.42% Spanish 0.15% 0.40% -1.34% -1.77% Arabic -3.80% -6.94% -9.11% -23.48% Malay 0.20% -0.01% -0.40% -0.34% Russian 0.08% 0.06% 0.03% -0.01% Bengali -0.17% -0.15% -0.07% -0.05% Portuguese -1.00% 0.09% -0.60% -0.23% French Hausa -0.11% -0.15% -0.13% -0.07% Punjabi 0.06% -0.02% 0.04% 0.01% Japanese -0.10% -1.44% 8.51% 3.59% German -0.51% -0.32% -1.12% 4.30% Persian -0.68% -0.44% -0.59% 0.17%

From this table, we can see that the number of Chinese, Hindi and Malay speakers are negatively correlated with migration rate, while the total number of speakers of English and Japanese are positive correlated with it. This is because people speaking Chinese, Malay and Hindi have stronger tendency to migrate and lots of them choose English-speaking countries as their second hometown.

5.2 Sensitivity Analysis on Location Determination Model

As is shown in 4.2, three factors contribute to the final locations for the new offices – geographic position, language structure and economic condition measured by GDP.

In our model, the impact of a country’s geographic position is expressed by distance. As the position of a country is not likely to change over time, we do not pay much attention to the sensitivity of this factor. Language structure, which is affected by net birth rate, migration and GDP growth, plays a significant role when deciding what language should be spoken in the new offices, but it is less important in the position-determining step. Consequently, in the sensitivity analysis section, we mainly focus on the fluctuation of GDP growth and its influences.

Similar as what we have done in section 5.1.2, we again apply a -50%, -10%, +10% and +100% variation to the GDP growth rate, and record the recommending countries for new offices under each circumstance, respectively. Wespot notable changes.

Table 15 Sensitivity Analysis of Location Determination Model Group Group Group Group Recommanded Recommanded Recommanded Recommanded members members members members Country Country Country Country Variation Variation Variation Variation GDP growth rate -50% -10% +10% +100% variation Africa +0 Nigeria +0 Nigeria +2 South Africa +4 Botswana +0 Russia +0 Russia +0 Russia +0 Russia Asia +0 China +0 China +0 China +0 China +0 Germany +0 Germany +0 Germany -2 Germany Europe +0 Poland +0 Poland -1 Poland -1 Poland North America +0 USA +0 USA +0 Mexico +0 Mexico Oceanic +0 Australia +0 Australia -1 Australia -1 Australia South America +0 Brazil +0 Brazil +0 Brazil +0 Brazil From the table above we can conclude that:

If the GDP growth rate decreases, neither the group members nor the recommended country  changes.

If the GDP growth rate increases, there tends to be more group members for Africa and less  members for Europe and Oceanic. Meanwhile, the recommended countries alter.

This phenomenon can be explained by the difference of GDP growing speed between developing and developed countries. When GDP growth rate increases, the difference broadens, meaning that more developing countries will take the place of the developed ones. It is natural that Africa attracts more attention, and we have more developing countries in the recommend list.

6. Further Discussion

Because the Location Determination Model produces just passable result through the solution oriented by language structure, we apply the latter solution oriented by geographic condition to further discuss whether 5 or even less offices to open can be applicable.

Since this solution does not make any restriction on the number of new office, the company can choose to open any arbitrary number of office based on its actual financial condition. As long as the company has a preliminary planning of how many new offices to open and which continent they are located at, we can provide the exact location of each office immediately.

For example, suggest the company decides to cut an office in Europe and open 5 offices in total, it won’t affect the location of other offices in other continents, but may change the location of Europe. Calculating this situation on Matlab program, we get the result of short-term andlong- term decision shown in the following figure.

Therefore, we can say that our model with the geographic-condition-oriented solution has strong adaptability to various situations and is a simple but also feasible method to provide advice on selection of new offices location.

7. Strengths and Weaknesses

7.1 Strengths

Based on the AHP method, the Language Development Model fully considers the influence  of many possible factors on language development, including communication, geography, economy, academy and diplomacy. Therefore, the result of the model is highly credible.

The Language Development Model takes country rather than language as the unit of  simulation. So, it can not only model the development of a certain language over time, but also model the linguistic structure of any given country over time.

We looked into the location determination problem from two different aspects: the similarity  of linguistic structure and the geographic distance between countries. We made a judgement on the priority of these two factors and improved our model.

The Location Determination Model can reflect the economic consideration of a modern  international company as GDP plays an important role when determining the location for new offices.

Flexibility and adaptability are also advantages of the Location Determination Model. When  the company change its strategy, new decisions can be quickly derived without modifying the algorithm.

7.2 Weaknesses

In our model, to simplify our model, only the language with the largest number of speakers is  considered as the native language of a country. But in fact, there might be two or even more native languages in a country.

The objective function to optimize the position of new offices is determined with a certain  degree of arbitrariness. It can be further improved to meet different actual needs.

The correctness of our conclusions relies heavily on the accuracy of the data collected and the  estimates of GDP, language and population development.

The recommendation provided by our model remains at the stage of countries (capitals).  Further analyses are required in order to determine the specific cities.

7. Conclusion

To predict the future distribution of commonly used languages, we build a Language Development Model, setting up 2 criteria to estimate the percentage of speaking a second language, 5 factors to evaluate which second language to speak. Then we simulate the model on Python, using data of population, GDP, language structure and etc. of over 50 countries we collected on the Internet. We conclude that only moderate changes occur to top ten language list, and most of the 16 languages we discuss gain a growth in their total speaker number.

To further provide advice to the multinational service company, we build a Location Determination Model, applying two solutions to figure out the suitable locations for establishment of new offices. The first solution oriented by language structure produced just passable result without comprehensive consideration on economic condition. The second solution, if provided initial number of office on each continent, produces generally ideal locations, and new decisions can be quickly derived if the company change its strategy.

Memo to the Service Company

Dear Chief Operating Officer, We are glad to hear your recent plan about opening six new international offices, which will definitely be an important milestone for your company to become truly international. For such a significant plan, it is necessary to carry out some research before making the final decision. To assist you to decide the location of new offices and determine the languages spoken in the offices, we performed investigations using mathematical modelling.

Firstly, we build up a Language Development model to investigate the distribution ofvarious language speakers over time. In this model, we consider many possible influencing factors, including economy, geography, communication, knowledge and diplomacy. This model is based on data from the United Nation (UN). Through our calculations and tests, we found that this model can really help us to predict the future of language development. It is indicated in this model that over the next 50 years, two original most spoken languages (Russian and Portuguese) will be replaced (by German and Japanese), while the total number of speakers of most languages will gain an impressive increase.

Based on the model of language distribution, combined with Algorithm for Fuzzy Clustering method and P-Center method, we develop a Location Determination Model using two solutions to further provide a recommendation for your company to select the location of your new international office and its working language. One of the solution is oriented by language structure, and the other by geographic condition. Taking language distribution as well as economic development of different countries into account, we suggest to locate new offices in the capitals of Nigeria, India, Germany, Italy, Brazil, Australia for short-term interest. These six locations as well as the languages to be used in the new offices are as the following:

Recommended Location for New Offices Language(s) to be Used New York, America Spanish Shanghai, China Chinese and Japanese Moscow, Russia Russian and Hindustani Warsaw, Poland German Berlin, Germany German, French and Spanish Abuja, Nigeria Arabic Brasilia, Brazil Spanish Canberra, Australia Malay

Considering from long-term perspective, your company should build these six new offices in

the capitals of Nigeria, Russia, Germany, Poland, Brazil and Australia. Moreover, since our model

makes no restriction on number of new office, you can set arbitrary number of offices based on

your actual financial condition. As long as you make a preliminary planning of how many new

offices to open and which continents they are located at, we can provide the exact location of each

office immediately.

We hope that our suggestion can provide useful information for you.

Yours sincerely,
