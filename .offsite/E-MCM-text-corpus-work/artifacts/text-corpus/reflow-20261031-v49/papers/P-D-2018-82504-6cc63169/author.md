For office use only For office use only T2 F2 T1 F1

T3 F3 Problem Chosen T4 F4

2018 MCM/ICM Summary Sheet

Our team is asked to build an assessing and construction system for the growing electric charging network. The model is related to several factors ranging from economic levels to consumer psychology. Among all these factors, we choose GDP per capita, vehicle density and population density as the key components of the main evaluation indexes. In addition, we also apply our model to the real situation, such as the network in the U.S, South Korea and other countries. Besides, we also take the influences of other quantifiable factors and non-quantifiable factors into consideration and give the analysis.

The first thing we do is to quantify the key factors’ influences on the charging net- work.We redefine the concept of urban, suburban and rural areas. And we establish a functional relationship between the charger density and our chosen factors. Then we use the method of K-Means Clustering to determine the chargers’ optimal location in different areas. Furthermore, taking the U.S and South Korea as example, we give out the amount of charging stations in different areas. Considering the actual situation, we adjust the distribution and improve our model.

The next thing we do is using Markov method to determine the relationship between charging stations and the road network. We verify that the flow rate controlled by the charging station is only related to the probability of the total flow of the node and has no relevance with the output of the node, which is the basis of our model. Then we give the recommended site position in Seoul. We also analyze how a country should invest in charging network according to customer psychology, economic level, publicity needs and other factors.

Then we establish a logistic model to calculate the number and the distribution of charging stations in the next following years. We give the quantified relationship between time, the ownership of electric vehicles and other vital factors. By applying the model to South Korea, we give the time it will take for electric vehicles to reach different percentage of all the motor vehicles.

We also consider other possible factors related to the network, such as geographies, population density distributions and wealth distributions. By applying sociological theo-ry in addition to mathematical method, we establish a classification system based on GDP per capita, population density and Gini coefficient and some quantified factors used to determine whether the country is qualified to develop charging network. We also discuss the new technology’s impacts on our model.

Finally, based on all the above analysis, we conclude and give reliable evaluation in-dexes, scientific evaluation methods, completed classification system and detailed anal-ysis about the design of charging network.

Gini coefficient

1 Introduction

1.1 Problem Statement

Motivated by demands of the environment and economy, there are increasing interests in the development of electric vehicles. The network of charging stations for electric vehicles will have a great impact on the expansion of electric vehicles. There exist several factors such as vehicle density, economic level, population density influencing the site selection of electric stations. Based on the official data offered by Tesla and governments, we will:

Build several models as to deliver construction plans under diverse situa- tions.

Determine the total number of electric vehicles and major influencing fac- tors if the country replaces all the traditional vehicles with electric vehicles.

Determine the timetable and construction order.

Analyze the influences of other factors on the network of charging stations.

Deliver a handout including suggestions for different nations and key fac- tors.

1.2 Related Work

The stochastic flow-capturing model(SFCLM) is a model which conduct inte-ger programming on traffic capture. It can be used for building large-scale charg-ing network. It’s based on the shortest distance, drivers’ anxiety range and the assumption that every driver only charges no more than once per day. The input data source can be generated randomly.[1]

By comparing the SFCLM to a deterministic model, in which EV flows are set equal to their expected values. Researches show that if a limited number of charging stations are to be built, the SFCLM outperforms the deterministic model. As the number of stations to be built increases, the SFCLM and deterministic model select very similar station locations.

2 Preparation of the Models

2.1 Assumptions

1. (Shortest-path) Each vehicle go to the station with the shortest distance to get charged. 2. (Range-anxiety threshold) An electric vehicle driver will only seek to recharge his or her vehicle if its state of charge (Soc) falls below 10% 3. Only public charging stations are considered in this essay.

2.2 Notations

The primary notations used in this paper are listed in the table below.

Symbol Definition sample point in K-Means clustering x(i) the cluster centroid to which x(i) is assigned c(i) ru the maximum radius of capturing areas of urban stations rs the maximum radius of capturing areas of suburban stations the number of charging stations in an 40 40 mile2 square n0 v average number of vehicles per capita density of population GDP per capita G cu a constant used in calculating ru cs a constant used in calculating rs l total length of expressways n total number of villages v n number of charging stations nu number of charging stations in urban area ns number of charging stations in suburban area nr number of charging stations in rural area Su total area of urban area Ss total area of suburban area R the ratio of Tesla num to all motor vehicle num t year k an index concerning about population density and economic level

3 Exploring Tesla Network in the United States

3.1 Tesla’s Objective

In recent years, Tesla has built more than 2500 charging stations around the United States, which is a quite impressive number. From the official system called Find Us[2], it is obvious that there have been Tesla’s charging stations along most of the big cities and main expressways in the United States, even in Alaska and Hawaii.

Apparently, although, there are still many areas not covered by built charging stations, the number of charging stations has exceeded 1% of the number of gas stations, which is smaller than 200 thousand[3]. While the total number of sold Tesla is only around 300 thousand[4], which is only around 0:1% of the number of cars[5]. Tesla is building charging stations much more than it is supposed to build, which reflects its long-term plan of developing electric vehicles.

Furthermore, Tesla is generally known and accepted by more people. It is also investing more and more in construction of charging stations, research and technical development. Although electric cars can still not complete long distance travel because of the limit of battery, superchargers can partly solve this problem if a complete charging network is completed. Except those who need to drive long distance at a daily frequency, which are only a small part of drivers, most people’s daily need for vehicles can be satisfied by existing technology provided by Tesla.

Certainly, it is not an easy task to replace millions of vehicles on the road, but Tesla is on the right track, and we have strong confidence that Tesla can complete the switch to all-electric in the U.S.

3.2 Charging Network in Urban and Suburban Areas

In big cities like New York or Los Angles, we need many charging station-s to garuantee that electric vehicle drivers can get their cars charged whenever their cars are lack of power. Therefore, considering the cost of building charging stations, the proper number and distribution of the charging stations become an essential problem.

3.2.1 Optimal Number of Charging Stations

To calculate the number of charging stations, especially in the suburban ar-eas, based on the assumptions of shortest-path and range-anxiety threshold men-tioned in 2.1, our goal is to make sure that a driver can go to the nearest charging station with at most 5% of a charge so that they can arrive the stations with at least 5% power, which can protect the battery from the damage of too little power left. Based on the data given in the official website[6], most Tesla cars can cover around 300 miles with a charge. Thus we set the maximum radius of the cap-turing area of a charging station is 15 miles. However, 15 miles is not a distance easy to cover in the complex urban traffic. Considering the negative correlation between r and the economical condition, density of people and average number of vehicle per capita, we can calculate r more accurately by

where cu, cs are constants unrelated with areas. In practice, we use the completed charging network in Manhattan to estimate cu, and cs is calculated by cu and the ratio of urban size and suburban size, urban residents and suburban residents.

Without loss of generality, we can divide the urban area to several squares, and consider the distribution of stations in each square. Empirically, we think the shape of capturing area is close to a square when the cars in the urban and suburban areas are evenly distributed, which is evidenced by using advanced K-Means clustering algorithm. Thus, the estimation of the optimal number of charging stations in a square with length of 40 miles can be estimated by 402 r2e n0 = d (3) where r is defined by the above equation.

3.2.2 Optimal Location: K-Means Clustering and Our Improvements

Traditionally, K-Means clustering is a popular algorithm used in data mining. Since our model assumes the cars are evenly distributed in urban and suburban areas, we can also use K-Means in choosing the optimal locations of the charging stations after some original improvements.

By the above improvements of K-Means clustering, we can regard the cen- troids generated by our algorithm as the optimal placements of charging stations, since our definition of distance and distortion function can garuantee that the car can always find the nearest station within r miles if J(c; ) < r.

Below is an example of capturing areas and optimal placement of charging stations chosen by K-Means clustering.

Clustering

3.3 Charging Network in Rural Areas

The U.S. Department of Health and Human Service defines the word rural as encompassing "...all population, housing, and territory not included within an urban area. Whatever is not urban is considered rural. "[8] Thus, we can divide the rural areas which need charging stations construction to two parts: villages and public roads.

In most cases, the radius of a village will be smaller than 4 miles, so there needs to be only one charging stations in a village.

When considering the charging stations on public roads, since there will be no gas station if everyone switched to all-electric personal passenger vehicles, an im-portant function of charging stations is to offer a place to rest for drivers. Besides, there will be congestion in charging stations if everyone needs to charge in the same charging station. Therefore, we need to construct stations at relatively high frequency. Compared to the distribution of gas stations, considering the longer time of charging, constructing a charging station every 20 miles is an acceptable frequency.

Therefore, we have

In practice, since the difference between town, county and village are not very clear, we regard the cities with population fewer than 10,000 as villages[9].

3.4 Distribution of Charging Stations

To make it more accurately, we calculate it state by state, and here are the results.

Area Type Station Number Percentage(%) Urban 58739 45.0 Suburban 42533 32.6 Rural[11] 29161 22.4 Total 130433 100 As for the ratio of destination charging and superchargers, we need to take user needs into consideration. On expressways, most chargers are used to give electric vehicles power to keep going in a short time, so most chargers located on expressways should be superchargers. In contrast, chargers in urban and sub-urban area or villages are mostly used by residents or residents, thus we can put more destination charging in these stations. Based on this analysis, we rec-ommend 90% of the chargers in the stations located on expressways should be superchargers, and 70% of the chargers in the stations located in urban, suburban areas or villages should be destination charging.

4 Exploring Charging Network in South Korea

Based on the first task, we set some more indexes to assess the amount of charging stations, their locations and other details.

4.1 Switch to All-electric in South Korea

Korea is one of the typical country in the world which have the ability to complete the plan of replacing motor vehicles with electric cars.

4.1.1 Amount of Two Types of Charging Stations

Destination Charging Stations

First, We divide South Korea into three parts of rural cities and suburbs based on the population density in Korea. According to the table, we classify Seoul, Bu-

Population Density Type 4000+ Urban 1000-4000 Suburb 0-1000 Rural

san as urban. Gwangju, Daejeon, Daegu, Incheon, Gyeonggi-do, Ulsan, Sejong-si as suburban. Jeju-do, Gyeongsangnam-do, Chungcheongnam-do, Jeollabuk-do, Chungcheongbuk-do, eollanam-do, Gyeongsangbuk-do, Gangwon-do as rural.

Next, we conduct cluster analysis of different areas and quantify the influence of population density on charger density. Meanwhile, the GDP data and popula-tion data will also have an impact on the amount of charging stations. For data obtained, we use direct least square fitting method and conclude the simulation results.

Then, we substitute the conclusion into the equations listed in task1 and con- clude that the capturing radius for destination chargers in South Korea is The

Area Type Capturing radius(km) Urban 5 Suburban 10 Rural 15

connection between capturing area and charging station density is displayed in the picture below.

Supercharging Stations

When it comes to the position selection of supercharging stations, especially on highways, we should pay attention to other factors besides the basic needs of charging. Today’s dense gas stations take the responsibility for ensuring drivers’ rest time, which is what we think the most important factor when designing the network. Therefore, we set the distance between two charging station on nation-al highway to about 20-50km, 50-170km for other roads. Finally, by calculation based on the road length and the coverage area of road network,we reach the total num of supercharging station.

The num is 30343.

4.1.2 The placement of charging stations in South Korea

We use two methods to select the site for stations and compare them with each other. For displaying our work clearer, we will only show the detailed results of Seoul.

Through verification, the two methods can be applied to most cities.

Markov method First, we assume that the flow rate controlled by the charging station is only related to the probability of the total flow of the node, which has no relevance with the output of the node.

Next, we verified the assumption as listed below. In general, we consider the situation of three nodes. For node A, B, C, define their opposite side as a, b, c. Its corresponding Markov transition matrix is

results. For any diagram, we can block it to several small pieces and apply our method to it.

Thus, our assumption is verified. The flow chart in the actual situation is

Algorithm 1 Markov method

for e in E do Define H(e) as the sum of all e’s adjacent edges’ weight while J contain more than n 1 edges do J 1 + H(e) in E Delete e f rom E end while end for

SFCLM method

In the relate work of the article, we made a brief introduction of SFCLM. When it comes to the verification, we apply Seoul road data into it and get a comparable solution.

Using these two methods, we draw the picture of charger network we recom-mend for Seoul. As in the pictures shown below, the distribution is similar to each other, verifying our model’s reliability.

4.2 A proposal for evolving South Korea from zero chargers

to a full electric-vehicle system

In a formed charging network, there is a mutually beneficial relationship be- tween the construction of new charging stations and the sales of electric vehicles. However, in the early stage of network construction, since the charging stations are scarce, most of the users’ needs have not yet been met. For this reason, most customers tend to take a wait-and-see attitude. Therefore, in the beginning, the construction should give priority to those areas with the most potential customer- s. Building all-city based chargers will dispel potential customers’ worries as well as play the role of propaganda.

As Ona Egbue and Suzanna Long stated in their article, "Consumer accep- tance is important as it is key to the commercial success (or failure) of EVs[10]" . The construction of charging station should aim at arousing the customers’ inter- ests. Considering customers’ worries, in the early construction, we recommend building chargers first to attract customers. We define this period as ’extension period’. After the user of electric vehicle reaches a certain ratio of all the users, the speed of construction can slow down. In this ’stationary period’, the con-struction has less relevance with the car purchases, but the population density or other possible factors. As construction continues, the charging stations tend to saturate. To avoid the waste of resources, we need to aim at customers’ needs. In this ’mature period’, we suggest building chargers in response to car purchases.

The key factors that shaped our proposed charging station plan includes pop-ulation density, GDP per capita and vehicle density, which have something to do with purchase desire.

4.3 Timeline

To calculate the number and the distribution of charging station.We establish a model of logistic model.

The high market proportion of Tesla in a region tends to have positive feed- back on the local Tesla ownership.Therefore, we have

dR = kR (11) dt Since the ratio can’t reach 1, we can change our model to

dR dt = kR(1 R) (12) Then solve the equation Cekt 1 + Cekt R = (13) In 2018, the market proportion of Tesla cars is estimated about 1%.Then we con-clude that C=0.01. New technology tends to spread the fastest in urban areas, then in suburban areas, the slowest in rural areas.Besides, the amount of Tesla cars in an area has a strong connection with the economic level.If we set k in urban areas equaling to 0.3, in suburban areas equaling to 0.26, in rural areas equaling to 0.22.

Based on our model, we estimate that by the end of 2026, 10% motor vehicles in South Korea will be driven by pure electricity, 30% by the end of 2031, 50% by the end of 2034, and 90% by the end of 2042. We can also conclude from the simulation results that in the recent years, the increasing rate will reach its maximum. In 2035, the increasing rate in suburban areas will catch up with that in urban areas. In 2038, the increasing rate in rural areas will catch up with that in suburban areas.

Here are the visualized simulation results of the variation trend of Tesla’s mar-ket share and its increasing rate.

Based on the car ownership data provided by Statistics Korea[11], we build the growth model of motor vehicles in South Korea.

dy dt = 2:2 10 0:4 (5000 y) (14) The current population of South Korea is fifty million. The ownership of vehicles will gradually saturate while approaching the population. At the present stage, the increasing rate is estimated to be about 10%.Then we conclude the num of electric vehicles in South Korea when the proportion differs. The electric vehicle density by province in South Korea in different period is as the chart shown.

proportion 10% 30% 50% 90% year 2026 2031 2034 2042 num(million) 2.246 2.250 2.253 2.276

5 Model Migration to Different Countries

Nowadays, there are more than 200 countries in the world. Different countries have different geometrical, economical, political and cultural differences, which will all impact the promotion of electric vehicles. Next, we will present our clas-sification pattern and growth model for some typical types of countries.

5.1 Classification of Countries

In short, GDP per capita and density of population are two essential factors in this classification model because GDP per capita can reflect the purchasing ability, which will influence the switch speed, and denity of population can reflect geometrical features of the country, which will influce the construction process of charging stations.

Besides these factors, we also introduce Gini coefficient to classification since GDP per capita and density of population can not reflects the actual situation in some unbalanced countries, and Gini coefficient is a well-accepted measure of inequality.

In practice, we divide both the GDP per capita and density of population[12] to three degrees named low, medium and high. For the country with low degree of GDP per capita, we do not recommend them migrate to electric cars at present since there will be unignorable expenses. To the left 6 types of countries, we have different growth models based on their varied backgrounds. Below are the standards of classification and some typical examples

Factors GDP per capita (USD) Medium High Standard 3000 and 10000 10000 Low Russia Australia 100 2 Density (=mi ) Medium Bulgaria Korean 100 and 300 High Indonesia Singapore 300 As for the countries larger than 1000 square mile whose Gini coefficient is higher than 0.6, we think them have problems of imbalanced regional develop- ment, which make the above classification model not suitable. In this condition, we will seperate them to several parts with each part having more similar back- ground, then we can regard these parts as "small countries", classify them to d- ifferent types defined in the above model and apply different growth models to them.

Take China as example. In our classification, China has medium GDP per capita and high density of population. However, in eastern provinces like Zhe- jiang, the GDP per capita is higher than 10000 USD and the density of population is higher than 1000=mi2, which meet the standards of countries with high GDP per capita and high density of population. Meanwhile, Tibet’s condition is totally different. With density of population of 1000=mi2 and GDP per capita of 4500 USD, it should be regarded as medium GDP per capita and low density of pop-ulation. Obviously, applying different growth models to them is a more reliable choice.

5.2 Assessment of Feasibility

5.2.1 Some Non-quantifiable Factors

There exist several factors which may influence the feasibility of the charging network’s expansion. We choose some typical ones to conduct further discus-sions. It is remarkable that according to the model we build before, the number of charging stations in a country should be positively associated with GDP per capita and vehicle density. For some certain reasons like political restriction, some countries like Russian or Singapore is against the conclusion. This situation is not discussed in our assessing system in detail.

5.2.2 Geography

The picture below is the distribution of destination charging stations in Saudi Arabia, China and Australia. Intuitively, we can see that the stations are much denser along coastal areas and the most economically developed areas. There are two reasons resulting in the situation. On the one hand, these areas are opener to the outer world and new technology. On the other hand, the GDP per capita in these areas are higher, so there exist more potential customers with stronger purchasing ability than other areas.

5.2.3 Combined Index

However, to migrate to electric vehicles completely, it’s far from enough to just set charging stations in these areas. To determine whether an area is qualified to construct charging network, we set some indexes to quantify it.

Profit function: (x) = ax + e. a means the profit per vehicle. x means the number of electric vehicles. e means the network construction fee which the area can afford.

Consumption function: g(x) = p ce kt. p means the saturated number of charging stations. c equals to price (p station_num_at_present). k is in proportion to the increasing rate of electric vehicles in the area/country. In the beginning, the amount of charging stations is nearly in proportion to the num of electric vehicles. When traditional vehicles no longer exist, the needs for charging will always be satisfied no matter how the num of electric vehicles changes. The cost will be a relatively number.

g(x) = ax + b p + ce kx Evaluation function: f(x) = (x)

When g(x) > (x), we think the area’s comprehensive ability is not enough to construct large-scale charging network and recommend developing economy at 1 a . The solution is the year when the first. The stagnation point of f(x) is kln(ck ) area is able to build large-scale charging network.

We verify the model by applying several countries’ data into it. For example, China is able to conduct the construction while Indonesia is not. The results of other countries also match the reality.

6 Impact from Advanced Technologies

6.1 Batteries

The development of battery technology will influence the charging network in two ways.

On the one hand, the battery capacity determines electric vehicles’ maximum distance once charged, which is the major basis for capturing area defined in our model, as to change the network.

On the other hand, in addition to charging station, several companies used to consider the possibilities of replacing batteries when it’s out of energy. However, the labor and time cost is much higher for customers than charging in the stations. Therefore, most people choose to charge in the station nowadays. Once batteries can be replaced easily, the number of people who use charging station is sure to decrease sharply, which will also influence the capturing area defined in our model, further changing the network, or even replacing all the charging stations.

6.2 Construction Technology of Charging Piles

The construction of a charging station has demands in many areas, such as the ground situation, wires availability, etc. Today’s technology may not be able to install charging stations in all the places our model planned for. The real net- work may not be the idealized network. Meanwhile, in the large-scale installa- tion process, designers must take installation costs into account. The high costs of charging station are against the expansion of charging stations, further slowing down the replacement of traditional vehicles. With the development of the man-ufacturing technology of charging piles, network designers are able to no more considerate these social restrictions and adapt the network to a more optimized one. In our model, these changes will reflect on the percentage of electric vehicles among all the vehicles, which can also be quantified and are similar to the results in task 2a.

6.3 Types of Vehicles

From the present perspective, replacing traditional vehicles with electric ones is the best choice for human development. However, vehicles change rapidly. Electricity has never been the only choice. In the near future, vehicles driven by other energy or hybrids may attract customers’ interests. Charging stations will face fiercer competition and increasing requirements. Other factors, such as the convenient access, energy types or quality, may play a more important role in network planning. Under this situation, we plan to add more influence factors to the evaluation index in our model, as to understand the demands more precisely.

7

Strengths and Weaknesses

Our model takes economic level, population density, vehicle density, regional differences into consideration when forming the model. Based on the modeling process, we make some comments on our model as listed below.

7.1 Strengths

Reliablity: The factors we choose to form the evaluation system are typical, which perform well in real testings. The data sources include authorities and several national statistical agencies, ensuring the data quality. Besides, during the process of modeling, we try to quantify the indexes as far as possible, which ˘ ´ avoid the interference originating from the researchersâAZ individual social ten-dencies, thus strengthening the reliability.

Extensibility: Every test index used is relatively independent. Therefore, it’s easy to adapt test indexes to different testing situations. Since all the indexes used in our model are easily available, we can extend our model to multiple types of countries with various background without many adjustments.

Universality: Our model uses the formula(1)(2) to describe the relationship be-tween the vehicle density and the density of the station, which is universal. It has high universality for different population density in different areas. For the growth mode of Tesla electric vehicle, we adopt the logistic growth model, which reflects the development trend of Tesla EV in the future decades. It can be ref-erences for the government’s decisions. When it comes to the site selection, we use Markov chain model and SFCLM model. The former is convenient and easy to operate, and the latter has precise characteristics. Both have a complementary role in the construction of government investment. At the same time, our model has made a specific classification for different types of countries, and predicted the construction of the Tesla charging station in Korea.

7.2 Weaknesses

Construction fee ignored: Construction fee of charging stations is always uncer-tain and varies from regions, and it is nearly impossible to estimate when we are dealing with the model designed for many countries. Thus, we haven’t taken the factor into consideration of our general model. If we need to build a charging station distribution model for a certain region, then it would be quite easier to introduce the influence of construction fee to our model.

Data Limitation: Because of the limit of data availability, we are not able to predict exactly where is unsuitable for construction. At the same time, we do not consider political factors and other non-quantified indexes so that the model may not be applied in some special countries where there are political or regional constraints on electric vehicles. Meanwhile, since Tesla is the latest technology, we may not consider the effect of alternative factors like other power resources which can replace electricity.

7.3 Future Work

In the process of future development of charging stations, we may face more influence factors which are hard to quantify, such as some additional functions of the charging station. Our team suggests conducting fuzzy classification of these factors to provide more practical design for the network. We hope to apply more theories of different subjects to make contributions to the betterment of charging network construction and human’s future.

8 Handout for International Energy Summit

To whom it may concern,

It’s a great honor for us to present you our research results of the migration towards electric vehicles. We sincerely hope that it will provide some references for you while making policies and plans. We also hope our suggestions could play a part in the development of electric vehicles and the betterment of human development. In the next part of the handout, we will describe our modeling concepts and advice to you in detail.

The key factors of our model include: economic level, user density and de- velopment potential, which can be quantified precisely. Other factors include geographies, consumer psychology or other factors that are hard to quantify. The components and functions are listed in our article in detail. You can refer to them while formulating policies.

In our assessing system, there are four steps to design the charging network. First, use the assessing function to determine whether the economic level in your country or area is enough to sustain the cost of construction. The function has been verified to be effective.

Next, calculate the number of charging stations in different areas. By using the functions we provide, you can get the suggested charging station density in different areas. Some special situations, such as stations on the highway are also taken into consideration.

Then, determine the exact position. Based on the Markov method, you can determine the relationship between the charger station and the road network. Finally, add other functions to the network. Besides the indxes and functions we provide, you can also add national characteristic data to the assessing system. The construction and usage of private chargers may affect the network in the future.

By using the methods we provide, you can also estimate the exact time when electric vehicles is in certain proportion to traditional vehicles. According to the timetable, a gas vehicle-ban date can be decided scientifically.

The migration to all electric-vehicles is a long-term process. However, sparks of fire can start a prairie fire. We hope to see the rapid expansion of charging stations, for future, and for human.

Your sincerely, #82504
