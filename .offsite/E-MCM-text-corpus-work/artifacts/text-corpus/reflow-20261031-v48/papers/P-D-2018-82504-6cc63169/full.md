# P-D-2018-82504-6cc63169

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | front_matter | pages [1] -->
Team Control Number

<!-- b000003 | front_matter | pages [1] -->
82504

<!-- b000004 | prose | pages [1] -->
For office use only For office use only T2 F2 T1 F1

<!-- b000005 | prose | pages [1] -->
T3 F3 Problem Chosen T4 F4

<!-- b000006 | front_matter | pages [1] -->
D

<!-- b000007 | prose | pages [1] -->
2018 MCM/ICM Summary Sheet

<!-- b000008 | front_matter | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000009 | prose | pages [1] -->
Our team is asked to build an assessing and construction system for the growing electric charging network. The model is related to several factors ranging from economic levels to consumer psychology. Among all these factors, we choose GDP per capita, vehicle density and population density as the key components of the main evaluation indexes. In addition, we also apply our model to the real situation, such as the network in the U.S, South Korea and other countries. Besides, we also take the influences of other quantifiable factors and non-quantifiable factors into consideration and give the analysis.

<!-- b000010 | prose | pages [1] -->
The first thing we do is to quantify the key factors’ influences on the charging net- work.We redefine the concept of urban, suburban and rural areas. And we establish a functional relationship between the charger density and our chosen factors. Then we use the method of K-Means Clustering to determine the chargers’ optimal location in different areas. Furthermore, taking the U.S and South Korea as example, we give out the amount of charging stations in different areas. Considering the actual situation, we adjust the distribution and improve our model.

<!-- b000011 | prose | pages [1] -->
The next thing we do is using Markov method to determine the relationship between charging stations and the road network. We verify that the flow rate controlled by the charging station is only related to the probability of the total flow of the node and has no relevance with the output of the node, which is the basis of our model. Then we give the recommended site position in Seoul. We also analyze how a country should invest in charging network according to customer psychology, economic level, publicity needs and other factors.

<!-- b000012 | prose | pages [1] -->
Then we establish a logistic model to calculate the number and the distribution of charging stations in the next following years. We give the quantified relationship between time, the ownership of electric vehicles and other vital factors. By applying the model to South Korea, we give the time it will take for electric vehicles to reach different percentage of all the motor vehicles.

<!-- b000013 | prose | pages [1] -->
We also consider other possible factors related to the network, such as geographies, population density distributions and wealth distributions. By applying sociological theo-ry in addition to mathematical method, we establish a classification system based on GDP per capita, population density and Gini coefficient and some quantified factors used to determine whether the country is qualified to develop charging network. We also discuss the new technology’s impacts on our model.

<!-- b000014 | prose | pages [1] -->
Finally, based on all the above analysis, we conclude and give reliable evaluation in-dexes, scientific evaluation methods, completed classification system and detailed anal-ysis about the design of charging network.

<!-- b000015 | keywords | pages [1] -->
Keywords: K-Means clustering, Markov method, GDP per capita, population density,

<!-- b000016 | prose | pages [1] -->
Gini coefficient

<!-- b000017 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000018 | furniture | pages [2] -->
Team # 82504

<!-- b000019 | furniture | pages [2] -->
Page 1 of 25

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1 Introduction

<!-- b000022 | contents | pages [2] -->
2

<!-- b000023 | contents | pages [2] -->
1.1

<!-- b000024 | contents | pages [2] -->
Problem Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
1.2

<!-- b000027 | contents | pages [2] -->
Related Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
2 Preparation of the Models

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
2.1

<!-- b000032 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
3

<!-- b000034 | contents | pages [2] -->
2.2

<!-- b000035 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
3

<!-- b000037 | contents | pages [2] -->
3 Exploring Tesla Network in the United States

<!-- b000038 | contents | pages [2] -->
4

<!-- b000039 | contents | pages [2] -->
3.1

<!-- b000040 | contents | pages [2] -->
Tesla’s Objective . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
4

<!-- b000042 | contents | pages [2] -->
3.2

<!-- b000043 | contents | pages [2] -->
Charging Network in Urban and Suburban Areas . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
4

<!-- b000045 | contents | pages [2] -->
3.3

<!-- b000046 | contents | pages [2] -->
Charging Network in Rural Areas . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
7

<!-- b000048 | contents | pages [2] -->
3.4

<!-- b000049 | contents | pages [2] -->
Distribution of Charging Stations . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
7

<!-- b000051 | contents | pages [2] -->
4 Exploring Charging Network in South Korea

<!-- b000052 | contents | pages [2] -->
8

<!-- b000053 | contents | pages [2] -->
4.1

<!-- b000054 | contents | pages [2] -->
Switch to All-electric in South Korea . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
8

<!-- b000056 | contents | pages [2] -->
4.2

<!-- b000057 | contents | pages [2] -->
A proposal for evolving South Korea from zero chargers to a full

<!-- b000058 | contents | pages [2] -->
electric-vehicle system . . . . . . . . . . . . . . . . . . . . . . . . . . 12

<!-- b000059 | contents | pages [2] -->
4.3 Timeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

<!-- b000060 | contents | pages [2] -->
5 Model Migration to Different Countries

<!-- b000061 | contents | pages [2] -->
15

<!-- b000062 | contents | pages [2] -->
5.1

<!-- b000063 | contents | pages [2] -->
Classification of Countries . . . . . . . . . . . . . . . . . . . . . . . . 15

<!-- b000064 | contents | pages [2] -->
5.2

<!-- b000065 | contents | pages [2] -->
Assessment of Feasibility . . . . . . . . . . . . . . . . . . . . . . . . . 16

<!-- b000066 | contents | pages [2] -->
6 Impact from Advanced Technologies

<!-- b000067 | contents | pages [2] -->
17

<!-- b000068 | contents | pages [2] -->
6.1

<!-- b000069 | contents | pages [2] -->
Batteries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
17

<!-- b000071 | contents | pages [2] -->
6.2

<!-- b000072 | contents | pages [2] -->
Construction Technology of Charging Piles . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
18

<!-- b000074 | contents | pages [2] -->
6.3

<!-- b000075 | contents | pages [2] -->
Types of Vehicles . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
18

<!-- b000077 | contents | pages [2] -->
7 Strengths and Weaknesses

<!-- b000078 | contents | pages [2] -->
18

<!-- b000079 | contents | pages [2] -->
7.1

<!-- b000080 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

<!-- b000081 | contents | pages [2] -->
7.2

<!-- b000082 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
19

<!-- b000084 | contents | pages [2] -->
7.3

<!-- b000085 | contents | pages [2] -->
Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
19

<!-- b000087 | contents | pages [2] -->
8 Handout for International Energy Summit

<!-- b000088 | contents | pages [2] -->
20

<!-- b000089 | contents | pages [2] -->
Reference

<!-- b000090 | contents | pages [2] -->
21

<!-- b000091 | contents | pages [2] -->
A K-Means Clustering (Python)

<!-- b000092 | contents | pages [2] -->
22

<!-- b000093 | contents | pages [2] -->
B Matlab Codes

<!-- b000094 | contents | pages [2] -->
23

<!-- b000095 | furniture | pages [2] -->
Team # 82504

<!-- b000096 | furniture | pages [2] -->
Page 2 of 25

<!-- b000097 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000098 | contents | pages [3] -->
Design of Charging Network

<!-- b000099 | heading | pages [3] -->
1 Introduction

<!-- b000100 | heading | pages [3] -->
1.1 Problem Statement

<!-- b000101 | prose | pages [3] -->
Motivated by demands of the environment and economy, there are increasing interests in the development of electric vehicles. The network of charging stations for electric vehicles will have a great impact on the expansion of electric vehicles. There exist several factors such as vehicle density, economic level, population density influencing the site selection of electric stations. Based on the official data offered by Tesla and governments, we will:

<!-- b000102 | prose | pages [3] -->
Build several models as to deliver construction plans under diverse situa- tions.

<!-- b000103 | prose | pages [3] -->
Determine the total number of electric vehicles and major influencing fac- tors if the country replaces all the traditional vehicles with electric vehicles.

<!-- b000104 | prose | pages [3] -->
Determine the timetable and construction order.

<!-- b000105 | prose | pages [3] -->
Analyze the influences of other factors on the network of charging stations.

<!-- b000106 | prose | pages [3] -->
Deliver a handout including suggestions for different nations and key fac- tors.

<!-- b000107 | heading | pages [3] -->
1.2 Related Work

<!-- b000108 | prose | pages [3] -->
The stochastic flow-capturing model(SFCLM) is a model which conduct inte-ger programming on traffic capture. It can be used for building large-scale charg-ing network. It’s based on the shortest distance, drivers’ anxiety range and the assumption that every driver only charges no more than once per day. The input data source can be generated randomly.[1]

<!-- b000109 | prose | pages [3] -->
By comparing the SFCLM to a deterministic model, in which EV flows are set equal to their expected values. Researches show that if a limited number of charging stations are to be built, the SFCLM outperforms the deterministic model. As the number of stations to be built increases, the SFCLM and deterministic model select very similar station locations.

<!-- b000110 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000111 | furniture | pages [4] -->
Team # 82504

<!-- b000112 | furniture | pages [4] -->
Page 3 of 25

<!-- b000113 | heading | pages [4] -->
2 Preparation of the Models

<!-- b000114 | heading | pages [4] -->
2.1 Assumptions

<!-- b000115 | prose | pages [4] -->
1. (Shortest-path) Each vehicle go to the station with the shortest distance to get charged. 2. (Range-anxiety threshold) An electric vehicle driver will only seek to recharge his or her vehicle if its state of charge (Soc) falls below 10% 3. Only public charging stations are considered in this essay.

<!-- b000116 | heading | pages [4] -->
2.2 Notations

<!-- b000117 | prose | pages [4] -->
The primary notations used in this paper are listed in the table below.

<!-- b000118 | caption | pages [4] -->
Table 1: Notations

<!-- b000119 | prose | pages [4] -->
Symbol Definition sample point in K-Means clustering x(i) the cluster centroid to which x(i) is assigned c(i) ru the maximum radius of capturing areas of urban stations rs the maximum radius of capturing areas of suburban stations the number of charging stations in an 40 40 mile2 square n0 v average number of vehicles per capita density of population GDP per capita G cu a constant used in calculating ru cs a constant used in calculating rs l total length of expressways n total number of villages v n number of charging stations nu number of charging stations in urban area ns number of charging stations in suburban area nr number of charging stations in rural area Su total area of urban area Ss total area of suburban area R the ratio of Tesla num to all motor vehicle num t year k an index concerning about population density and economic level

<!-- b000120 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000121 | furniture | pages [5] -->
Team # 82504

<!-- b000122 | furniture | pages [5] -->
Page 4 of 25

<!-- b000123 | heading | pages [5] -->
3 Exploring Tesla Network in the United States

<!-- b000124 | heading | pages [5] -->
3.1 Tesla’s Objective

<!-- b000125 | prose | pages [5] -->
In recent years, Tesla has built more than 2500 charging stations around the United States, which is a quite impressive number. From the official system called Find Us[2], it is obvious that there have been Tesla’s charging stations along most of the big cities and main expressways in the United States, even in Alaska and Hawaii.

<!-- b000126 | prose | pages [5] -->
Apparently, although, there are still many areas not covered by built charging stations, the number of charging stations has exceeded 1% of the number of gas stations, which is smaller than 200 thousand[3]. While the total number of sold Tesla is only around 300 thousand[4], which is only around 0:1% of the number of cars[5]. Tesla is building charging stations much more than it is supposed to build, which reflects its long-term plan of developing electric vehicles.

<!-- b000127 | prose | pages [5] -->
Furthermore, Tesla is generally known and accepted by more people. It is also investing more and more in construction of charging stations, research and technical development. Although electric cars can still not complete long distance travel because of the limit of battery, superchargers can partly solve this problem if a complete charging network is completed. Except those who need to drive long distance at a daily frequency, which are only a small part of drivers, most people’s daily need for vehicles can be satisfied by existing technology provided by Tesla.

<!-- b000128 | prose | pages [5] -->
Certainly, it is not an easy task to replace millions of vehicles on the road, but Tesla is on the right track, and we have strong confidence that Tesla can complete the switch to all-electric in the U.S.

<!-- b000129 | heading | pages [5] -->
3.2 Charging Network in Urban and Suburban Areas

<!-- b000130 | prose | pages [5] -->
In big cities like New York or Los Angles, we need many charging station-s to garuantee that electric vehicle drivers can get their cars charged whenever their cars are lack of power. Therefore, considering the cost of building charging stations, the proper number and distribution of the charging stations become an essential problem.

<!-- b000131 | heading | pages [5] -->
3.2.1 Optimal Number of Charging Stations

<!-- b000132 | prose | pages [5, 6, 7] -->
To calculate the number of charging stations, especially in the suburban ar-eas, based on the assumptions of shortest-path and range-anxiety threshold men-tioned in 2.1, our goal is to make sure that a driver can go to the nearest charging station with at most 5% of a charge so that they can arrive the stations with at least 5% power, which can protect the battery from the damage of too little power left. Based on the data given in the official website[6], most Tesla cars can cover around 300 miles with a charge. Thus we set the maximum radius of the cap-turing area of a charging station is 15 miles. However, 15 miles is not a distance easy to cover in the complex urban traffic. Considering the negative correlation between r and the economical condition, density of people and average number of vehicle per capita, we can calculate r more accurately by

<!-- b000133 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000135 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000136 | furniture | pages [7] -->
Team # 82504

<!-- b000137 | furniture | pages [7] -->
Page 5 of 25

<!-- b000139 | prose | pages [7] -->
where cu, cs are constants unrelated with areas. In practice, we use the completed charging network in Manhattan to estimate cu, and cs is calculated by cu and the ratio of urban size and suburban size, urban residents and suburban residents.

<!-- b000140 | prose | pages [7] -->
Without loss of generality, we can divide the urban area to several squares, and consider the distribution of stations in each square. Empirically, we think the shape of capturing area is close to a square when the cars in the urban and suburban areas are evenly distributed, which is evidenced by using advanced K-Means clustering algorithm. Thus, the estimation of the optimal number of charging stations in a square with length of 40 miles can be estimated by 402 r2e n0 = d (3) where r is defined by the above equation.

<!-- b000141 | caption | pages [7] -->
Figure 1: Radius of Capturing Area of Charging Stations by State

<!-- b000142 | heading | pages [7] -->
3.2.2 Optimal Location: K-Means Clustering and Our Improvements

<!-- b000143 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000144 | prose | pages [8, 9] -->
Traditionally, K-Means clustering is a popular algorithm used in data mining. Since our model assumes the cars are evenly distributed in urban and suburban areas, we can also use K-Means in choosing the optimal locations of the charging stations after some original improvements.

<!-- b000145 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000146 | furniture | pages [9] -->
Team # 82504

<!-- b000147 | furniture | pages [9] -->
Page 6 of 25

<!-- b000149 | prose | pages [9] -->
By the above improvements of K-Means clustering, we can regard the cen- troids generated by our algorithm as the optimal placements of charging stations, since our definition of distance and distortion function can garuantee that the car can always find the nearest station within r miles if J(c; ) < r.

<!-- b000150 | prose | pages [9] -->
Below is an example of capturing areas and optimal placement of charging stations chosen by K-Means clustering.

<!-- b000151 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000152 | caption | pages [10] -->
Figure 2: Optimal Locations by K-Means

<!-- b000153 | prose | pages [10] -->
Clustering

<!-- b000154 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000155 | furniture | pages [11] -->
Team # 82504

<!-- b000156 | furniture | pages [11] -->
Page 7 of 25

<!-- b000157 | heading | pages [11] -->
3.3 Charging Network in Rural Areas

<!-- b000158 | prose | pages [11] -->
The U.S. Department of Health and Human Service defines the word rural as encompassing "...all population, housing, and territory not included within an urban area. Whatever is not urban is considered rural. "[8] Thus, we can divide the rural areas which need charging stations construction to two parts: villages and public roads.

<!-- b000159 | prose | pages [11] -->
In most cases, the radius of a village will be smaller than 4 miles, so there needs to be only one charging stations in a village.

<!-- b000160 | prose | pages [11] -->
When considering the charging stations on public roads, since there will be no gas station if everyone switched to all-electric personal passenger vehicles, an im-portant function of charging stations is to offer a place to rest for drivers. Besides, there will be congestion in charging stations if everyone needs to charge in the same charging station. Therefore, we need to construct stations at relatively high frequency. Compared to the distribution of gas stations, considering the longer time of charging, constructing a charging station every 20 miles is an acceptable frequency.

<!-- b000161 | prose | pages [11] -->
Therefore, we have

<!-- b000162 | prose | pages [11] -->
In practice, since the difference between town, county and village are not very clear, we regard the cities with population fewer than 10,000 as villages[9].

<!-- b000163 | heading | pages [11] -->
3.4 Distribution of Charging Stations

<!-- b000164 | prose | pages [11] -->
To make it more accurately, we calculate it state by state, and here are the results.

<!-- b000165 | caption | pages [11] -->
Table 2: Distribution of Charging Stations in the United States[10]

<!-- b000166 | prose | pages [11, 12, 13] -->
Area Type Station Number Percentage(%) Urban 58739 45.0 Suburban 42533 32.6 Rural[11] 29161 22.4 Total 130433 100 As for the ratio of destination charging and superchargers, we need to take user needs into consideration. On expressways, most chargers are used to give electric vehicles power to keep going in a short time, so most chargers located on expressways should be superchargers. In contrast, chargers in urban and sub-urban area or villages are mostly used by residents or residents, thus we can put more destination charging in these stations. Based on this analysis, we rec-ommend 90% of the chargers in the stations located on expressways should be superchargers, and 70% of the chargers in the stations located in urban, suburban areas or villages should be destination charging.

<!-- b000167 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000169 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000170 | furniture | pages [13] -->
Team # 82504

<!-- b000171 | furniture | pages [13] -->
Page 8 of 25

<!-- b000173 | heading | pages [13] -->
4 Exploring Charging Network in South Korea

<!-- b000174 | prose | pages [13] -->
Based on the first task, we set some more indexes to assess the amount of charging stations, their locations and other details.

<!-- b000175 | heading | pages [13] -->
4.1 Switch to All-electric in South Korea

<!-- b000176 | prose | pages [13] -->
Korea is one of the typical country in the world which have the ability to complete the plan of replacing motor vehicles with electric cars.

<!-- b000177 | heading | pages [13] -->
4.1.1 Amount of Two Types of Charging Stations

<!-- b000178 | prose | pages [13] -->
Destination Charging Stations

<!-- b000179 | prose | pages [13] -->
First, We divide South Korea into three parts of rural cities and suburbs based on the population density in Korea. According to the table, we classify Seoul, Bu-

<!-- b000180 | caption | pages [13] -->
Table 3: Classification of different regions by Population density

<!-- b000181 | prose | pages [13] -->
Population Density Type 4000+ Urban 1000-4000 Suburb 0-1000 Rural

<!-- b000182 | prose | pages [13] -->
san as urban. Gwangju, Daejeon, Daegu, Incheon, Gyeonggi-do, Ulsan, Sejong-si as suburban. Jeju-do, Gyeongsangnam-do, Chungcheongnam-do, Jeollabuk-do, Chungcheongbuk-do, eollanam-do, Gyeongsangbuk-do, Gangwon-do as rural.

<!-- b000183 | prose | pages [13, 14] -->
Next, we conduct cluster analysis of different areas and quantify the influence of population density on charger density. Meanwhile, the GDP data and popula-tion data will also have an impact on the amount of charging stations. For data obtained, we use direct least square fitting method and conclude the simulation results.

<!-- b000184 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000186 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000187 | furniture | pages [15] -->
Team # 82504

<!-- b000188 | furniture | pages [15] -->
Page 9 of 25

<!-- b000189 | caption | pages [15] -->
Figure 3: Verification of the fitting results

<!-- b000190 | prose | pages [15] -->
Then, we substitute the conclusion into the equations listed in task1 and con- clude that the capturing radius for destination chargers in South Korea is The

<!-- b000191 | caption | pages [15] -->
Table 4: Capturing radius of Destination chargers in South Korea

<!-- b000192 | prose | pages [15] -->
Area Type Capturing radius(km) Urban 5 Suburban 10 Rural 15

<!-- b000193 | prose | pages [15] -->
connection between capturing area and charging station density is displayed in the picture below.

<!-- b000194 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000195 | furniture | pages [16] -->
Team # 82504

<!-- b000196 | furniture | pages [16] -->
Page 10 of 25

<!-- b000197 | caption | pages [16] -->
Figure 4: The relationship between capturing radius and charging station density

<!-- b000198 | prose | pages [16] -->
Supercharging Stations

<!-- b000199 | prose | pages [16] -->
When it comes to the position selection of supercharging stations, especially on highways, we should pay attention to other factors besides the basic needs of charging. Today’s dense gas stations take the responsibility for ensuring drivers’ rest time, which is what we think the most important factor when designing the network. Therefore, we set the distance between two charging station on nation-al highway to about 20-50km, 50-170km for other roads. Finally, by calculation based on the road length and the coverage area of road network,we reach the total num of supercharging station.

<!-- b000200 | prose | pages [16] -->
The num is 30343.

<!-- b000201 | heading | pages [16] -->
4.1.2 The placement of charging stations in South Korea

<!-- b000202 | prose | pages [16] -->
We use two methods to select the site for stations and compare them with each other. For displaying our work clearer, we will only show the detailed results of Seoul.

<!-- b000203 | prose | pages [16] -->
Through verification, the two methods can be applied to most cities.

<!-- b000204 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000205 | prose | pages [17, 18] -->
Markov method First, we assume that the flow rate controlled by the charging station is only related to the probability of the total flow of the node, which has no relevance with the output of the node.

<!-- b000206 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000207 | furniture | pages [18] -->
Team # 82504

<!-- b000208 | furniture | pages [18] -->
Page 11 of 25

<!-- b000210 | prose | pages [18] -->
Next, we verified the assumption as listed below. In general, we consider the situation of three nodes. For node A, B, C, define their opposite side as a, b, c. Its corresponding Markov transition matrix is

<!-- b000211 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000212 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000213 | furniture | pages [20] -->
Team # 82504

<!-- b000214 | furniture | pages [20] -->
Page 12 of 25

<!-- b000215 | prose | pages [20] -->
results. For any diagram, we can block it to several small pieces and apply our method to it.

<!-- b000216 | prose | pages [20] -->
Thus, our assumption is verified. The flow chart in the actual situation is

<!-- b000217 | heading | pages [20] -->
Algorithm 1 Markov method

<!-- b000218 | prose | pages [20] -->
for e in E do Define H(e) as the sum of all e’s adjacent edges’ weight while J contain more than n 1 edges do J 1 + H(e) in E Delete e f rom E end while end for

<!-- b000219 | prose | pages [20] -->
SFCLM method

<!-- b000220 | prose | pages [20] -->
In the relate work of the article, we made a brief introduction of SFCLM. When it comes to the verification, we apply Seoul road data into it and get a comparable solution.

<!-- b000221 | prose | pages [20] -->
Using these two methods, we draw the picture of charger network we recom-mend for Seoul. As in the pictures shown below, the distribution is similar to each other, verifying our model’s reliability.

<!-- b000222 | caption | pages [20] -->
Figure 5: Plan by Markov method

<!-- b000223 | caption | pages [20] -->
Figure 6: Plan by SFCLM method

<!-- b000224 | heading | pages [20] -->
4.2 A proposal for evolving South Korea from zero chargers

<!-- b000225 | prose | pages [20] -->
to a full electric-vehicle system

<!-- b000226 | prose | pages [20, 21, 22] -->
In a formed charging network, there is a mutually beneficial relationship be- tween the construction of new charging stations and the sales of electric vehicles. However, in the early stage of network construction, since the charging stations are scarce, most of the users’ needs have not yet been met. For this reason, most customers tend to take a wait-and-see attitude. Therefore, in the beginning, the construction should give priority to those areas with the most potential customer- s. Building all-city based chargers will dispel potential customers’ worries as well as play the role of propaganda.

<!-- b000227 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000229 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000230 | furniture | pages [22] -->
Team # 82504

<!-- b000231 | furniture | pages [22] -->
Page 13 of 25

<!-- b000233 | prose | pages [22] -->
As Ona Egbue and Suzanna Long stated in their article, "Consumer accep- tance is important as it is key to the commercial success (or failure) of EVs[10]" . The construction of charging station should aim at arousing the customers’ inter- ests. Considering customers’ worries, in the early construction, we recommend building chargers first to attract customers. We define this period as ’extension period’. After the user of electric vehicle reaches a certain ratio of all the users, the speed of construction can slow down. In this ’stationary period’, the con-struction has less relevance with the car purchases, but the population density or other possible factors. As construction continues, the charging stations tend to saturate. To avoid the waste of resources, we need to aim at customers’ needs. In this ’mature period’, we suggest building chargers in response to car purchases.

<!-- b000234 | prose | pages [22] -->
The key factors that shaped our proposed charging station plan includes pop-ulation density, GDP per capita and vehicle density, which have something to do with purchase desire.

<!-- b000235 | heading | pages [22] -->
4.3 Timeline

<!-- b000236 | prose | pages [22] -->
To calculate the number and the distribution of charging station.We establish a model of logistic model.

<!-- b000237 | prose | pages [22] -->
The high market proportion of Tesla in a region tends to have positive feed- back on the local Tesla ownership.Therefore, we have

<!-- b000238 | prose | pages [22] -->
dR = kR (11) dt Since the ratio can’t reach 1, we can change our model to

<!-- b000239 | prose | pages [22] -->
dR dt = kR(1 R) (12) Then solve the equation Cekt 1 + Cekt R = (13) In 2018, the market proportion of Tesla cars is estimated about 1%.Then we con-clude that C=0.01. New technology tends to spread the fastest in urban areas, then in suburban areas, the slowest in rural areas.Besides, the amount of Tesla cars in an area has a strong connection with the economic level.If we set k in urban areas equaling to 0.3, in suburban areas equaling to 0.26, in rural areas equaling to 0.22.

<!-- b000240 | prose | pages [22, 23, 24] -->
Based on our model, we estimate that by the end of 2026, 10% motor vehicles in South Korea will be driven by pure electricity, 30% by the end of 2031, 50% by the end of 2034, and 90% by the end of 2042. We can also conclude from the simulation results that in the recent years, the increasing rate will reach its maximum. In 2035, the increasing rate in suburban areas will catch up with that in urban areas. In 2038, the increasing rate in rural areas will catch up with that in suburban areas.

<!-- b000241 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000243 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000244 | furniture | pages [24] -->
Team # 82504

<!-- b000245 | furniture | pages [24] -->
Page 14 of 25

<!-- b000247 | prose | pages [24] -->
Here are the visualized simulation results of the variation trend of Tesla’s mar-ket share and its increasing rate.

<!-- b000248 | caption | pages [24] -->
Figure 7: Variation Trend of Market Share

<!-- b000249 | caption | pages [24] -->
Figure 8: The Incresing Rate of Tesla

<!-- b000250 | prose | pages [24] -->
Based on the car ownership data provided by Statistics Korea[11], we build the growth model of motor vehicles in South Korea.

<!-- b000251 | prose | pages [24] -->
dy dt = 2:2 10 0:4 (5000 y) (14) The current population of South Korea is fifty million. The ownership of vehicles will gradually saturate while approaching the population. At the present stage, the increasing rate is estimated to be about 10%.Then we conclude the num of electric vehicles in South Korea when the proportion differs. The electric vehicle density by province in South Korea in different period is as the chart shown.

<!-- b000252 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000253 | caption | pages [25] -->
Figure 9: Electric vehicle density by province in South Korea in 2026, 2031, 2034, 2042

<!-- b000254 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000255 | furniture | pages [26] -->
Team # 82504

<!-- b000256 | furniture | pages [26] -->
Page 15 of 25

<!-- b000257 | caption | pages [26] -->
Table 5: Electric vehicle num in different period

<!-- b000258 | prose | pages [26] -->
proportion 10% 30% 50% 90% year 2026 2031 2034 2042 num(million) 2.246 2.250 2.253 2.276

<!-- b000259 | heading | pages [26] -->
5 Model Migration to Different Countries

<!-- b000260 | prose | pages [26] -->
Nowadays, there are more than 200 countries in the world. Different countries have different geometrical, economical, political and cultural differences, which will all impact the promotion of electric vehicles. Next, we will present our clas-sification pattern and growth model for some typical types of countries.

<!-- b000261 | heading | pages [26] -->
5.1 Classification of Countries

<!-- b000262 | prose | pages [26] -->
In short, GDP per capita and density of population are two essential factors in this classification model because GDP per capita can reflect the purchasing ability, which will influence the switch speed, and denity of population can reflect geometrical features of the country, which will influce the construction process of charging stations.

<!-- b000263 | prose | pages [26] -->
Besides these factors, we also introduce Gini coefficient to classification since GDP per capita and density of population can not reflects the actual situation in some unbalanced countries, and Gini coefficient is a well-accepted measure of inequality.

<!-- b000264 | prose | pages [26] -->
In practice, we divide both the GDP per capita and density of population[12] to three degrees named low, medium and high. For the country with low degree of GDP per capita, we do not recommend them migrate to electric cars at present since there will be unignorable expenses. To the left 6 types of countries, we have different growth models based on their varied backgrounds. Below are the standards of classification and some typical examples

<!-- b000265 | caption | pages [26] -->
Table 6: Classification Standards of Countries

<!-- b000266 | prose | pages [26, 27, 28] -->
Factors GDP per capita (USD) Medium High Standard 3000 and 10000 10000 Low Russia Australia 100 2 Density (=mi ) Medium Bulgaria Korean 100 and 300 High Indonesia Singapore 300 As for the countries larger than 1000 square mile whose Gini coefficient is higher than 0.6, we think them have problems of imbalanced regional develop- ment, which make the above classification model not suitable. In this condition, we will seperate them to several parts with each part having more similar back- ground, then we can regard these parts as "small countries", classify them to d- ifferent types defined in the above model and apply different growth models to them.

<!-- b000267 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000269 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000270 | furniture | pages [28] -->
Team # 82504

<!-- b000271 | furniture | pages [28] -->
Page 16 of 25

<!-- b000273 | prose | pages [28] -->
Take China as example. In our classification, China has medium GDP per capita and high density of population. However, in eastern provinces like Zhe- jiang, the GDP per capita is higher than 10000 USD and the density of population is higher than 1000=mi2, which meet the standards of countries with high GDP per capita and high density of population. Meanwhile, Tibet’s condition is totally different. With density of population of 1000=mi2 and GDP per capita of 4500 USD, it should be regarded as medium GDP per capita and low density of pop-ulation. Obviously, applying different growth models to them is a more reliable choice.

<!-- b000274 | heading | pages [28] -->
5.2 Assessment of Feasibility

<!-- b000275 | heading | pages [28] -->
5.2.1 Some Non-quantifiable Factors

<!-- b000276 | prose | pages [28] -->
There exist several factors which may influence the feasibility of the charging network’s expansion. We choose some typical ones to conduct further discus-sions. It is remarkable that according to the model we build before, the number of charging stations in a country should be positively associated with GDP per capita and vehicle density. For some certain reasons like political restriction, some countries like Russian or Singapore is against the conclusion. This situation is not discussed in our assessing system in detail.

<!-- b000277 | heading | pages [28] -->
5.2.2 Geography

<!-- b000278 | prose | pages [28] -->
The picture below is the distribution of destination charging stations in Saudi Arabia, China and Australia. Intuitively, we can see that the stations are much denser along coastal areas and the most economically developed areas. There are two reasons resulting in the situation. On the one hand, these areas are opener to the outer world and new technology. On the other hand, the GDP per capita in these areas are higher, so there exist more potential customers with stronger purchasing ability than other areas.

<!-- b000279 | furniture | pages [29] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000280 | caption | pages [29] -->
Figure 10: Destination chargers in Saudi Arabia, China and Australia

<!-- b000281 | furniture | pages [30] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000282 | furniture | pages [30] -->
Team # 82504

<!-- b000283 | furniture | pages [30] -->
Page 17 of 25

<!-- b000284 | heading | pages [30] -->
5.2.3 Combined Index

<!-- b000285 | prose | pages [30] -->
However, to migrate to electric vehicles completely, it’s far from enough to just set charging stations in these areas. To determine whether an area is qualified to construct charging network, we set some indexes to quantify it.

<!-- b000286 | prose | pages [30] -->
Profit function: (x) = ax + e. a means the profit per vehicle. x means the number of electric vehicles. e means the network construction fee which the area can afford.

<!-- b000287 | prose | pages [30] -->
Consumption function: g(x) = p ce kt. p means the saturated number of charging stations. c equals to price (p station_num_at_present). k is in proportion to the increasing rate of electric vehicles in the area/country. In the beginning, the amount of charging stations is nearly in proportion to the num of electric vehicles. When traditional vehicles no longer exist, the needs for charging will always be satisfied no matter how the num of electric vehicles changes. The cost will be a relatively number.

<!-- b000288 | prose | pages [30] -->
g(x) = ax + b p + ce kx Evaluation function: f(x) = (x)

<!-- b000289 | prose | pages [30] -->
When g(x) > (x), we think the area’s comprehensive ability is not enough to construct large-scale charging network and recommend developing economy at 1 a . The solution is the year when the first. The stagnation point of f(x) is kln(ck ) area is able to build large-scale charging network.

<!-- b000290 | prose | pages [30] -->
We verify the model by applying several countries’ data into it. For example, China is able to conduct the construction while Indonesia is not. The results of other countries also match the reality.

<!-- b000291 | prose | pages [30] -->
6 Impact from Advanced Technologies

<!-- b000292 | heading | pages [30] -->
6.1 Batteries

<!-- b000293 | prose | pages [30] -->
The development of battery technology will influence the charging network in two ways.

<!-- b000294 | prose | pages [30] -->
On the one hand, the battery capacity determines electric vehicles’ maximum distance once charged, which is the major basis for capturing area defined in our model, as to change the network.

<!-- b000295 | prose | pages [30, 31, 32] -->
On the other hand, in addition to charging station, several companies used to consider the possibilities of replacing batteries when it’s out of energy. However, the labor and time cost is much higher for customers than charging in the stations. Therefore, most people choose to charge in the station nowadays. Once batteries can be replaced easily, the number of people who use charging station is sure to decrease sharply, which will also influence the capturing area defined in our model, further changing the network, or even replacing all the charging stations.

<!-- b000296 | furniture | pages [31] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000298 | furniture | pages [32] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000299 | furniture | pages [32] -->
Team # 82504

<!-- b000300 | furniture | pages [32] -->
Page 18 of 25

<!-- b000302 | heading | pages [32] -->
6.2 Construction Technology of Charging Piles

<!-- b000303 | prose | pages [32] -->
The construction of a charging station has demands in many areas, such as the ground situation, wires availability, etc. Today’s technology may not be able to install charging stations in all the places our model planned for. The real net- work may not be the idealized network. Meanwhile, in the large-scale installa- tion process, designers must take installation costs into account. The high costs of charging station are against the expansion of charging stations, further slowing down the replacement of traditional vehicles. With the development of the man-ufacturing technology of charging piles, network designers are able to no more considerate these social restrictions and adapt the network to a more optimized one. In our model, these changes will reflect on the percentage of electric vehicles among all the vehicles, which can also be quantified and are similar to the results in task 2a.

<!-- b000304 | heading | pages [32] -->
6.3 Types of Vehicles

<!-- b000305 | prose | pages [32] -->
From the present perspective, replacing traditional vehicles with electric ones is the best choice for human development. However, vehicles change rapidly. Electricity has never been the only choice. In the near future, vehicles driven by other energy or hybrids may attract customers’ interests. Charging stations will face fiercer competition and increasing requirements. Other factors, such as the convenient access, energy types or quality, may play a more important role in network planning. Under this situation, we plan to add more influence factors to the evaluation index in our model, as to understand the demands more precisely.

<!-- b000306 | prose | pages [32] -->
7

<!-- b000307 | heading | pages [32] -->
Strengths and Weaknesses

<!-- b000308 | prose | pages [32] -->
Our model takes economic level, population density, vehicle density, regional differences into consideration when forming the model. Based on the modeling process, we make some comments on our model as listed below.

<!-- b000309 | heading | pages [32] -->
7.1 Strengths

<!-- b000310 | furniture | pages [33] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000311 | prose | pages [33, 34] -->
Reliablity: The factors we choose to form the evaluation system are typical, which perform well in real testings. The data sources include authorities and several national statistical agencies, ensuring the data quality. Besides, during the process of modeling, we try to quantify the indexes as far as possible, which ˘ ´ avoid the interference originating from the researchersâAZ individual social ten-dencies, thus strengthening the reliability.

<!-- b000312 | furniture | pages [34] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000313 | furniture | pages [34] -->
Team # 82504

<!-- b000314 | furniture | pages [34] -->
Page 19 of 25

<!-- b000316 | prose | pages [34] -->
Extensibility: Every test index used is relatively independent. Therefore, it’s easy to adapt test indexes to different testing situations. Since all the indexes used in our model are easily available, we can extend our model to multiple types of countries with various background without many adjustments.

<!-- b000317 | prose | pages [34] -->
Universality: Our model uses the formula(1)(2) to describe the relationship be-tween the vehicle density and the density of the station, which is universal. It has high universality for different population density in different areas. For the growth mode of Tesla electric vehicle, we adopt the logistic growth model, which reflects the development trend of Tesla EV in the future decades. It can be ref-erences for the government’s decisions. When it comes to the site selection, we use Markov chain model and SFCLM model. The former is convenient and easy to operate, and the latter has precise characteristics. Both have a complementary role in the construction of government investment. At the same time, our model has made a specific classification for different types of countries, and predicted the construction of the Tesla charging station in Korea.

<!-- b000318 | heading | pages [34] -->
7.2 Weaknesses

<!-- b000319 | prose | pages [34] -->
Construction fee ignored: Construction fee of charging stations is always uncer-tain and varies from regions, and it is nearly impossible to estimate when we are dealing with the model designed for many countries. Thus, we haven’t taken the factor into consideration of our general model. If we need to build a charging station distribution model for a certain region, then it would be quite easier to introduce the influence of construction fee to our model.

<!-- b000320 | prose | pages [34] -->
Data Limitation: Because of the limit of data availability, we are not able to predict exactly where is unsuitable for construction. At the same time, we do not consider political factors and other non-quantified indexes so that the model may not be applied in some special countries where there are political or regional constraints on electric vehicles. Meanwhile, since Tesla is the latest technology, we may not consider the effect of alternative factors like other power resources which can replace electricity.

<!-- b000321 | heading | pages [34] -->
7.3 Future Work

<!-- b000322 | prose | pages [34] -->
In the process of future development of charging stations, we may face more influence factors which are hard to quantify, such as some additional functions of the charging station. Our team suggests conducting fuzzy classification of these factors to provide more practical design for the network. We hope to apply more theories of different subjects to make contributions to the betterment of charging network construction and human’s future.

<!-- b000323 | furniture | pages [35] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000324 | furniture | pages [35] -->
Team # 82504

<!-- b000325 | furniture | pages [35] -->
Page 20 of 25

<!-- b000326 | heading | pages [35] -->
8 Handout for International Energy Summit

<!-- b000327 | prose | pages [35] -->
To whom it may concern,

<!-- b000328 | prose | pages [35] -->
It’s a great honor for us to present you our research results of the migration towards electric vehicles. We sincerely hope that it will provide some references for you while making policies and plans. We also hope our suggestions could play a part in the development of electric vehicles and the betterment of human development. In the next part of the handout, we will describe our modeling concepts and advice to you in detail.

<!-- b000329 | prose | pages [35] -->
The key factors of our model include: economic level, user density and de- velopment potential, which can be quantified precisely. Other factors include geographies, consumer psychology or other factors that are hard to quantify. The components and functions are listed in our article in detail. You can refer to them while formulating policies.

<!-- b000330 | prose | pages [35] -->
In our assessing system, there are four steps to design the charging network. First, use the assessing function to determine whether the economic level in your country or area is enough to sustain the cost of construction. The function has been verified to be effective.

<!-- b000331 | prose | pages [35] -->
Next, calculate the number of charging stations in different areas. By using the functions we provide, you can get the suggested charging station density in different areas. Some special situations, such as stations on the highway are also taken into consideration.

<!-- b000332 | prose | pages [35] -->
Then, determine the exact position. Based on the Markov method, you can determine the relationship between the charger station and the road network. Finally, add other functions to the network. Besides the indxes and functions we provide, you can also add national characteristic data to the assessing system. The construction and usage of private chargers may affect the network in the future.

<!-- b000333 | prose | pages [35] -->
By using the methods we provide, you can also estimate the exact time when electric vehicles is in certain proportion to traditional vehicles. According to the timetable, a gas vehicle-ban date can be decided scientifically.

<!-- b000334 | prose | pages [35] -->
The migration to all electric-vehicles is a long-term process. However, sparks of fire can start a prairie fire. We hope to see the rapid expansion of charging stations, for future, and for human.

<!-- b000335 | prose | pages [35] -->
Your sincerely, #82504

<!-- b000336 | furniture | pages [36] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000337 | furniture | pages [36] -->
Team # 82504

<!-- b000338 | furniture | pages [36] -->
Page 21 of 25

<!-- b000339 | heading | pages [36] -->
References

<!-- b000340 | references | pages [36] -->
[1] Fei Wu, Ramteen Sioshansi. A stochastic flow-capturing model to optimize

<!-- b000341 | references | pages [36] -->
the location of fast-charging stations with uncertain electric vehicle flows.[J]

<!-- b000342 | references | pages [36] -->
Transportation Research Part D: Transport and Environment. 2012.

<!-- b000343 | references | pages [36] -->
[2] Find Us, Tesla: https://www.tesla.com/findus#/

<!-- b000344 | references | pages [36] -->
[3] How many gas stations are there in the U.S?:

<!-- b000345 | references | pages [36] -->
https://www.fueleconomy.gov/feg/quizzes/answerQuiz16.shtml

<!-- b000346 | references | pages [36] -->
[4] Tesla Sales: https://en.wikipedia.org/wiki/Tesla,_Inc.#Production_and_sales

<!-- b000347 | references | pages [36] -->
[5] Number of registered vehicles: https://www.statista.com/statistics/183505/number-of-

<!-- b000348 | references | pages [36] -->
vehicles-in-the-united-states-since-1990/

<!-- b000349 | references | pages [36] -->
[6] Tesla Model S: https://www.tesla.com/model-s

<!-- b000350 | references | pages [36] -->
Tesla Model X: https://www.tesla.com/model-x

<!-- b000351 | references | pages [36] -->
Tesla Model 3: https://www.tesla.com/model3

<!-- b000352 | references | pages [36] -->
[7] K-Means clustering: http://cs229.stanford.edu/notes/cs229-notes7a.pdf

<!-- b000353 | references | pages [36] -->
[8] Rural Area: https://en.wikipedia.org/wiki/Rural_area

<!-- b000354 | references | pages [36] -->
[9] Number of cities, towns, villages by population size:

<!-- b000355 | references | pages [36] -->
https://www.statista.com/statistics/241695/number-of-us-cities-towns-

<!-- b000356 | references | pages [36] -->
villages-by-population-size/

<!-- b000357 | references | pages [36] -->
[10] Ona Egbue, SuzannaLong, 2012. Barriers to widespread adoption of

<!-- b000358 | references | pages [36] -->
electric vehicles: An analysis of consumer attitudes and perceptions

<!-- b000359 | references | pages [36] -->
[11] http://kostat.go.kr/portal/eng/index.action

<!-- b000360 | references | pages [36] -->
[12] All the data in this subsection is from Wikipedia

<!-- b000361 | furniture | pages [37] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000362 | furniture | pages [37] -->
Team # 82504

<!-- b000363 | furniture | pages [37] -->
Page 22 of 25

<!-- b000364 | references | pages [37] -->
K-Means Clustering (Python)

<!-- b000365 | references | pages [37] -->
A

<!-- b000366 | references | pages [37] -->
import numpy as np

<!-- b000367 | references | pages [37] -->
import matplotlib.pyplot as plt

<!-- b000368 | references | pages [37] -->
def kmeans(data,k=2):

<!-- b000369 | references | pages [37] -->
def _euclidDistance(p1,p2):

<!-- b000370 | references | pages [37] -->
return np.sqrt(np.sum((p1-p2)**2))

<!-- b000371 | references | pages [37] -->
def

<!-- b000372 | references | pages [37] -->
_manhattanDistance(p1,p2): return

<!-- b000373 | references | pages [37] -->
np.sum(np.abs(p1-p2))

<!-- b000374 | references | pages [37] -->
def _randCenter(data,k):

<!-- b000375 | references | pages [37] -->
n = data.shape[1] # features

<!-- b000376 | references | pages [37] -->
centroids = np.zeros((k,n)) # init with (0,0)....

<!-- b000377 | references | pages [37] -->
for i in range(n):

<!-- b000378 | references | pages [37] -->
dmin, dmax = np.min(data[:,i]), np.max(data[:,i]) centroids[:,i] = dmin + (dmax -

<!-- b000379 | references | pages [37] -->
dmin) * np.random.rand(k)

<!-- b000380 | references | pages [37] -->
return centroids

<!-- b000381 | references | pages [37] -->
def _converged(centroids1, centroids2):

<!-- b000382 | references | pages [37] -->
for

<!-- b000383 | references | pages [37] -->
in

<!-- b000384 | references | pages [37] -->
set1

<!-- b000385 | references | pages [37] -->
=

<!-- b000386 | references | pages [37] -->
set([tuple(c)

<!-- b000387 | references | pages [37] -->
c

<!-- b000388 | references | pages [37] -->
centroids1])

<!-- b000389 | references | pages [37] -->
set2

<!-- b000390 | references | pages [37] -->
=

<!-- b000391 | references | pages [37] -->
set([tuple(c) for c in centroids2]) return (set1 == set2)

<!-- b000392 | references | pages [37] -->
n = data.shape[0] # number of entries centroids =

<!-- b000393 | references | pages [37] -->
_randCenter(data,k)

<!-- b000394 | references | pages [37] -->
label = np.zeros(n,dtype=np.int) # track the nearest centroid assement =

<!-- b000395 | references | pages [37] -->
np.zeros(n) # for the assement of our model converged = False

<!-- b000396 | references | pages [37] -->
while not converged:

<!-- b000397 | references | pages [37] -->
old_centroids = np.copy(centroids) for i in

<!-- b000398 | references | pages [37] -->
range(n):

<!-- b000399 | references | pages [37] -->
# determine the nearest centroid and track it with label min_dist, min_index

<!-- b000400 | references | pages [37] -->
= np.inf, -1

<!-- b000401 | references | pages [37] -->
for j in range(k):

<!-- b000402 | references | pages [37] -->
dist = _manhattanDistance(data[i],centroids[j]) if dist < min_dist:

<!-- b000403 | references | pages [37] -->
min_dist, min_index = dist, j label[i] = j

<!-- b000404 | references | pages [37] -->
assement[i] = _manhattanDistance(data[i],centroids[label[i]])

<!-- b000405 | references | pages [37] -->
# update centroid for m

<!-- b000406 | references | pages [37] -->
in range(k):

<!-- b000407 | references | pages [37] -->
if data[label==m].size!=0:

<!-- b000408 | references | pages [37] -->
centroids[m] = np.mean(data[label==m],axis=0) converged =

<!-- b000409 | references | pages [37] -->
_converged(old_centroids,centroids)

<!-- b000410 | references | pages [37] -->
return centroids, label, np.max(assement)

<!-- b000411 | references | pages [37] -->
data = np.random.uniform(0,30,(10000,2))

<!-- b000412 | references | pages [37] -->
best_assement = np.inf

<!-- b000413 | references | pages [37] -->
best_centroids = None

<!-- b000414 | references | pages [37] -->
best_label = None

<!-- b000415 | references | pages [37] -->
max_r=15

<!-- b000416 | furniture | pages [38] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000417 | references | pages [38] -->
k=25

<!-- b000418 | furniture | pages [39] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000419 | furniture | pages [39] -->
Team # 82504

<!-- b000420 | furniture | pages [39] -->
Page 23 of 25

<!-- b000421 | references | pages [39] -->
for i in range(10):

<!-- b000422 | references | pages [39] -->
centroids, label, assement = kmeans(data,k) if assement

<!-- b000423 | references | pages [39] -->
< best_assement:

<!-- b000424 | references | pages [39] -->
best_assement = assement

<!-- b000425 | references | pages [39] -->
best_centroids = centroids

<!-- b000426 | references | pages [39] -->
best_label = label

<!-- b000427 | references | pages [39] -->
print (best_assement)

<!-- b000428 | references | pages [39] -->
data0 = data[best_label==0] data1 =

<!-- b000429 | references | pages [39] -->
data[best_label==1]

<!-- b000430 | references | pages [39] -->
data2

<!-- b000431 | references | pages [39] -->
=

<!-- b000432 | references | pages [39] -->
data[best_label==2]

<!-- b000433 | references | pages [39] -->
fig, ax2 = plt.subplots(figsize=(12,12)) for i in

<!-- b000434 | references | pages [39] -->
range(k):

<!-- b000435 | references | pages [39] -->
ax2.scatter(data[best_label==i][:,0],data[best_label==i][:,1])

<!-- b000436 | references | pages [39] -->
ax2.scatter(best_centroids[:,0],best_centroids[:,1],

<!-- b000437 | references | pages [39] -->
c=’b’,s=120,marker=’o’)

<!-- b000438 | references | pages [39] -->
plt.show()

<!-- b000439 | references | pages [39] -->
Matlab Codes

<!-- b000440 | references | pages [39] -->
B

<!-- b000441 | references | pages [39] -->
function y = logisticmodel(year,type) if type==1;

<!-- b000442 | references | pages [39] -->
y = (0.01*exp(0.3*(year-2017)))/(1+(0.01*exp(0.3*(year-2017))));

<!-- b000443 | references | pages [39] -->
end

<!-- b000444 | references | pages [39] -->
if type==2;

<!-- b000445 | references | pages [39] -->
y = (0.01*exp(0.26*(year-2017)))/(1+(0.01*exp(0.26*(year-2017))));

<!-- b000446 | references | pages [39] -->
end

<!-- b000447 | references | pages [39] -->
if type==3;

<!-- b000448 | references | pages [39] -->
y = (0.01*exp(0.22*(year-2017)))/(1+(0.01*exp(0.22*(year-2017))));

<!-- b000449 | references | pages [39] -->
end

<!-- b000450 | references | pages [39] -->
end

<!-- b000451 | references | pages [39] -->
function y = KoreaTesla(year)

<!-- b000452 | references | pages [39] -->
y = 0.7 *logisticmodel(year,1) + 0.2*logisticmodel(year,2) + 0.1*logisticmodel(year,3);

<!-- b000453 | references | pages [39] -->
[a,b,txt] = xlsread(’South Korea.xlsx’,’sheet1’); newtxt = {};

<!-- b000454 | references | pages [39] -->
newtxt(1,1) = txt(1,1); newtxt(2,1) =

<!-- b000455 | references | pages [39] -->
mat2cell(0.1); newtxt(3,1) =

<!-- b000456 | references | pages [39] -->
mat2cell(0.3); newtxt(4,1) =

<!-- b000457 | references | pages [39] -->
mat2cell(0.5); newtxt(5,1) =

<!-- b000458 | references | pages [39] -->
mat2cell(0.9); for i=2:length(txt)

<!-- b000459 | references | pages [39] -->
newtxt{i,1} = txt{i,1};

<!-- b000460 | references | pages [39] -->
if strcmp(txt{3,5},’urban’)

<!-- b000461 | references | pages [39] -->
= logisticmodel(divSolution(0.1),1) * txt{i,4} * 2246 /2237 *1600/10000;

<!-- b000462 | references | pages [39] -->
newtxt{i,2}

<!-- b000463 | references | pages [39] -->
= logisticmodel(divSolution(0.3),1) * txt{i,4} * 2250 /2237*1600/10000;

<!-- b000464 | references | pages [39] -->
newtxt{i,3}

<!-- b000465 | furniture | pages [40] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000466 | references | pages [40] -->
= logisticmodel(divSolution(0.5),1) * txt{i,4} * 2253 /2237*1600/10000;

<!-- b000467 | references | pages [40] -->
newtxt{i,4}

<!-- b000468 | furniture | pages [41] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000469 | furniture | pages [41] -->
Team # 82504

<!-- b000470 | furniture | pages [41] -->
Page 24 of 25

<!-- b000471 | references | pages [41] -->
= logisticmodel(divSolution(0.9),1) * txt{i,4} * 2276

<!-- b000472 | references | pages [41] -->
newtxt{i,5}

<!-- b000473 | references | pages [41] -->
/2237*1600/10000;

<!-- b000474 | references | pages [41] -->
end;

<!-- b000475 | references | pages [41] -->
if strcmp(txt{3,5},’suburban’)

<!-- b000476 | references | pages [41] -->
= logisticmodel(divSolution(0.1),2) * txt{i,4} * 2246 /2237*1600/10000;

<!-- b000477 | references | pages [41] -->
newtxt{i,2}

<!-- b000478 | references | pages [41] -->
= logisticmodel(divSolution(0.3),2) * txt{i,4} * 2250 /2237*1600/10000;

<!-- b000479 | references | pages [41] -->
newtxt{i,3}

<!-- b000480 | references | pages [41] -->
= logisticmodel(divSolution(0.5),2) * txt{i,4} * 2253 /2237*1600/10000;

<!-- b000481 | references | pages [41] -->
newtxt{i,4}

<!-- b000482 | references | pages [41] -->
= logisticmodel(divSolution(0.9),2) * txt{i,4} * 2276 /2237*1600/10000;

<!-- b000483 | references | pages [41] -->
newtxt{i,5}

<!-- b000484 | references | pages [41] -->
end;

<!-- b000485 | references | pages [41] -->
if strcmp(txt{3,5},’rural’)

<!-- b000486 | references | pages [41] -->
= logisticmodel(divSolution(0.1),3) * txt{i,4} * 2246 /2237*1600/10000;

<!-- b000487 | references | pages [41] -->
newtxt{i,2}

<!-- b000488 | references | pages [41] -->
= logisticmodel(divSolution(0.3),3) * txt{i,4} * 2250 /2237*1600/10000;

<!-- b000489 | references | pages [41] -->
newtxt{i,3}

<!-- b000490 | references | pages [41] -->
= logisticmodel(divSolution(0.5),3) * txt{i,4} * 2253 /2237*1600/10000;

<!-- b000491 | references | pages [41] -->
newtxt{i,4}

<!-- b000492 | references | pages [41] -->
= logisticmodel(divSolution(0.9),3) * txt{i,4} * 2276 /2237*1600/10000;

<!-- b000493 | references | pages [41] -->
newtxt{i,5}

<!-- b000494 | references | pages [41] -->
end;

<!-- b000495 | references | pages [41] -->
end

<!-- b000496 | references | pages [41] -->
initial = 0.01; r1 =

<!-- b000497 | references | pages [41] -->
0.3;%urban r2 =

<!-- b000498 | references | pages [41] -->
0.26;%suburb r3 =

<!-- b000499 | references | pages [41] -->
0.22;%rur

<!-- b000500 | references | pages [41] -->
year = linspace(2017,2067,200);

<!-- b000501 | references | pages [41] -->
urban = (initial * exp(r1*(year-2017)))./

<!-- b000502 | references | pages [41] -->
(1 + (initial * exp(r1*(year-2017)))); suburb = (initial *

<!-- b000503 | references | pages [41] -->
exp(r2*(year-2017)))./

<!-- b000504 | references | pages [41] -->
(1 + (initial * exp(r2*(year-2017)))); rur = (initial * exp(r3*(year-

<!-- b000505 | references | pages [41] -->
2017)))./

<!-- b000506 | references | pages [41] -->
(1 + (initial * exp(r3*(year-2017)))); plot(year,urban,’r-’,year,suburb,’b-

<!-- b000507 | references | pages [41] -->
’,year,rur,’g-’);

<!-- b000508 | references | pages [41] -->
legend(’urban’,’suburb’,’rural’); grid on;

<!-- b000509 | references | pages [41] -->
title(’the rate of tesla among all car’); xlabel(’year’);

<!-- b000510 | references | pages [41] -->
figure;

<!-- b000511 | references | pages [41] -->
plot(year(1:199),diff(urban),’r-’,year(1:199),diff(suburb),’b-’, year(1:199),diff(rur),’g-

<!-- b000512 | references | pages [41] -->
’);legend(’urban’,’suburb’,’rural’);

<!-- b000513 | references | pages [41] -->
grid on;

<!-- b000514 | references | pages [41] -->
title(’the acceleration of tesla rate among all car’); xlabel(’year’);

<!-- b000515 | references | pages [41] -->
load(’data.mat’);

<!-- b000516 | references | pages [41] -->
num = cell2mat(data(2:52,2:7)); X =

<!-- b000517 | references | pages [41] -->
num(:,2:4);

<!-- b000518 | references | pages [41] -->
Y = num(:,5);

<!-- b000519 | references | pages [41] -->
beta = inv(X’*X)*X’*Y;

<!-- b000520 | furniture | pages [42] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000521 | references | pages [42] -->
function y = divSolution(num) y0 =

<!-- b000522 | references | pages [42] -->
2017;

<!-- b000523 | references | pages [42] -->
y2 = 2067;

<!-- b000524 | furniture | pages [43] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000525 | furniture | pages [43] -->
Team # 82504

<!-- b000526 | furniture | pages [43] -->
Page 25 of 25

<!-- b000527 | references | pages [43] -->
tmp = (y0 + y2)/2;

<!-- b000528 | references | pages [43] -->
while abs(KoreaTesla(tmp) - num)>=1e-4 if

<!-- b000529 | references | pages [43] -->
KoreaTesla(tmp)>num

<!-- b000530 | references | pages [43] -->
y2 = tmp;

<!-- b000531 | references | pages [43] -->
tmp = (y0 + y2)/2;

<!-- b000532 | references | pages [43] -->
else

<!-- b000533 | references | pages [43] -->
y0 = tmp;

<!-- b000534 | references | pages [43] -->
tmp = (y0 + y2)/2;

<!-- b000535 | references | pages [43] -->
end

<!-- b000536 | references | pages [43] -->
end

<!-- b000537 | references | pages [43] -->
y = ceil(tmp);

<!-- b000538 | references | pages [43] -->
load(’data.mat’);

<!-- b000539 | references | pages [43] -->
X = cell2mat(data(2:length(data),3:5));

<!-- b000540 | references | pages [43] -->
Y = cell2mat(data(2:length(data),6)); beta =

<!-- b000541 | references | pages [43] -->
inv(X’*X)*X’*Y;

<!-- b000542 | references | pages [43] -->
state = 2:length(data);

<!-- b000543 | references | pages [43] -->
plot(state,Y,state,X*beta);legend(’charging station’,’fitted value’); xlabel(’state’);

<!-- b000544 | references | pages [43] -->
ylabel(’number’);

<!-- b000545 | references | pages [43] -->
grid on;
