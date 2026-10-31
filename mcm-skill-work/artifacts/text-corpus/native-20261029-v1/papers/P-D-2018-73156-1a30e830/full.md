# P-D-2018-73156-1a30e830

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
73156

<!-- b000006 | prose | pages [1] -->
T1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
T3

<!-- b000009 | prose | pages [1] -->
F1

<!-- b000010 | prose | pages [1] -->
F2

<!-- b000011 | prose | pages [1] -->
F3

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T4

<!-- b000014 | prose | pages [1] -->
F4

<!-- b000015 | prose | pages [1] -->
D D

<!-- b000016 | prose | pages [1] -->
2018 MCM/ICM Summary Sheet Construct all-electric network

<!-- b000017 | prose | pages [1] -->
The transformation from gas vehicles to electric vehicles becomes a hot topic all overthe world. In order to get the schedule of the location of charging stations and predict the process of transformation tendency, we establish several models to solve the questions.

<!-- b000018 | prose | pages [1] -->
For question 1, we firstly establish a model based on queuing theory. Furthermore, we construct a multi-objective programming model based on information of the current Tesla charging network in the US. With the help of Matlab, we find that Tesla is on track to allow a complete switch to all-electric in the US. We obtain that the number of charging stations needed is about 1.7million when all gas vehicles transform to electric vehicles, and the distribution proportions of charging stations in urban, suburban and rural areas are 67:23:10.

<!-- b000019 | prose | pages [1] -->
For question 2, we establish the site selection models of charging station for urban, suburban and rural areas of South Korea, separately. Combining with the programming model which we established in problem 1, we obtain the number, location and distribution of charging stations in Korea. We get the key factors that affect our plan are the building cost of chargers and the government investment. By considering six indexes, we establish a logistic model. Using this model, we firstly give the timeline of the full evolution to electric vehicles. We find that the key factor for this situation is policy orientation. Then we further predict the number of the electric vehicles of urban and rural areas in South Korea separately. Through the logistic model, we obtain that South Korea should give preference to build charging station in cities. Similarly, we find that the two key factors which influent our model most are wealth distribution and government investment. Additionally, we introduce a concept called lag index to measure the relationship between the car and the charging station.

<!-- b000020 | prose | pages [1] -->
For question 3, we establish a classification system through Q-type clustering model. According to different national conditions, we divide the countries into three categories. Through some analysis of the Q-type clustering model, we find out that the key factors that trigger the selection of different approaches to growing the network are policy orientation, wealth distribution and government investment. According to these factors, a targeted electric network development plan has been proposed.

<!-- b000021 | prose | pages [1] -->
For question 4, to study the influence of various new technologies, we set several indicators to establish our models, such as GDP and OPH. By analyzing our evaluation model, we find that these technologies impact the growth rate of electric vehicles, which contributes to the growing popularity of electric vehicles. Besides, the population of electric vehicles will be driven by these technologies.

<!-- b000022 | prose | pages [1] -->
For question 5, we prepare a one-page handout for the leaders identifying the key factors which they should consider as they return to their home country to develop a national plan to migrate personal transportation towards all-electric cars and set a gas vehicle-ban date for different countries.

<!-- b000023 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000024 | prose | pages [2] -->
数模乐园整理提供，更多数学建模资源请关注微信公众平台“数模乐园”或官方网站www.smlyor.com获取

<!-- b000025 | heading | pages [2] -->
Key words: site selection model, logistic model, Q-type clustering model, electric network

<!-- b000026 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000027 | furniture | pages [3] -->
Team#73156

<!-- b000028 | furniture | pages [3] -->
Page 1 of 27

<!-- b000029 | prose | pages [3] -->
Content

<!-- b000030 | prose | pages [3] -->
1 Introduction.................................................................................................................... 2 1.1 Background..........................................................................................................2 1.2. Restatement of the Problem................................................................................3 1.2 Literature Review................................................................................................ 3 1.3 Our Work.............................................................................................................4 2 Assumptions and Justifications...................................................................................... 4 3 Distribute the charging stations in the US......................................................................4 3.1 Concepts introduction..........................................................................................5 3.2 All-electric evaluation model.............................................................................. 6 3.2.1 The model construction............................................................................ 6 3.2.2 Model solution and analysis..................................................................... 7 3.3 Distribution optimization model..........................................................................8 3.3.1 The model construction............................................................................ 8 3.3.2 Model solution and analysis..................................................................... 9 4 Study on South Korea.....................................................................................................9 4.1 Urban charging station location model..............................................................10 4.2 Suburban charging station location model........................................................ 12 4.3 Rural charging station location model...............................................................12 4.4 Logistic model...................................................................................................13 4.4.1 Index definition.......................................................................................13 4.4.2 The model construction.......................................................................... 13 4.4.3 Model solution and analysis................................................................... 14 4.5 Answers of the Questions..................................................................................14 5 Create a classification system.......................................................................................16 5.1 The model construction..................................................................................... 17 5.2 Model solution and analysis.............................................................................. 17 6 Comment on the effect of new technologies................................................................ 18 6.1 The model construction..................................................................................... 18 6.2 Model analysis...................................................................................................18 7 Sensitivity Analysis...................................................................................................... 19 8 Conclusions.................................................................................................................. 20 8.1 Strengths............................................................................................................20 8.2 Weaknesses........................................................................................................20 8.3 Model extension................................................................................................ 20 9 A Handout to the Leaders.............................................................................................20 10 Reference....................................................................................................................21 11 Appendix.................................................................................................................... 22

<!-- b000031 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000032 | furniture | pages [4] -->
Team#73156

<!-- b000033 | furniture | pages [4] -->
Page 2 of 27

<!-- b000034 | heading | pages [4] -->
1 Introduction

<!-- b000035 | heading | pages [4] -->
1.1 Background

<!-- b000036 | prose | pages [4] -->
Nowadays, fossil fuel and the environment protection have become the hottest issues in the world [1]. The main transportations all over the world are based on fossil oil, which has caused serious environmental pollutions. Since the resource of fossil fuels is limited and it always leads to the pollution, the transition of it to more clean energy is inevitable. In order to realize this aim, electric vehicles which are the representatives of new energy vehicles, have been recognized as the main development direction of the transformation in the automotive industry in the 21st century [2].

<!-- b000037 | prose | pages [4] -->
It is well established that electric vehicles are high efficiency, low noise and nearly zero pollution [3]. The advantages of electric vehicles are obvious. Hence, they have been widely used all over the world. To promote the large-scale development of electric vehicles, it is necessary to improve the corresponding infrastructure. As an important part of the construction of electric vehicle facilities, charging stations are crucial to the development of the entire electric vehicle industry. Where and how many do we need to construct the charging stations? Selecting the correct location and estimating the number of charging stations are very important.

<!-- b000038 | heading | pages [4] -->
1.2. Restatement of the Problem

<!-- b000039 | prose | pages [4] -->
When we transform the gasoline and fossil fuel cars to electric vehicles, we need to consider the network of charging stations and the growth of them over time. In order to make a development schedule of the charging stations for a country, we are required to answer the following questions.

<!-- b000040 | prose | pages [4] -->
1. Build a model to judge whether or not Tesla can switch to all-electric all over US. Distribute the charging stations in case of full electric.

<!-- b000041 | prose | pages [4] -->
2. Select a country to determine the number and location of charging stations. Make a timeline for the full evolution and find out the key factors that matter your model most.

<!-- b000042 | prose | pages [4] -->
3. Consider whether the model is suitable for the countries with different geographies, population density distributions, and wealth distributions situations, and discuss the feasibility of creating a classification system.

<!-- b000043 | prose | pages [4] -->
4. Consider that how new technologies affect the analysis of the increasing use of electric vehicles.

<!-- b000044 | prose | pages [4] -->
5. Write a one-page handout for the leaders to identify the key factors they should consider and set a gas vehicle-ban date.

<!-- b000045 | heading | pages [4] -->
1.2 Literature Review

<!-- b000046 | prose | pages [4] -->
Under the pressure of energy conservation and low carbon, the research on the electric vehicles and the construction of charging station network have made great progress.In the planning of charging facilities, some researchers point out that the layout of charging stations are affected by the number of electric vehicles [4]. The construction of power stations needs to meet the requirements of traffic density. Only in this way can they develop in harmony. Taking California for example, we know that there are one million new energy vehicles in existence [5]. By combining the supply and demand of

<!-- b000047 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000048 | furniture | pages [5] -->
Team#73156

<!-- b000049 | furniture | pages [5] -->
Page 3 of 27

<!-- b000050 | prose | pages [5] -->
California electricity, they build linear and nonlinear models, aiming at saving energy and reducing emissions. Wang [6] proposed a new method for the layout of charging station. In [6], they considered several influential factors such as technical level, holding capacity and charging behavior of electric vehicles. However, the proposed load-shedding space segment prediction method does not take into the driving features, using mode and charging mode into account. The weight of the method is subjective and the prediction error is large.

<!-- b000051 | prose | pages [5] -->
For selecting the location of charging stations, Holzman [7] aimed at minimizing the square distance of user-to-facility locations, and constructed the location selection model based on network planning. Then he discussed and expanded the model with specific conditions. Additionally, the authors [8] build the optimization model, whose algorithm was based on game theory. Hakimi [9] conducted a systematic study of the selection of facility location. He considers the location of one or more facilities within a network, providing that the total distance or the maximum distance between the facility and the point is minimized. The theory makes the selection of charging station furtherdeveloped on the basis of the original theory.

<!-- b000052 | prose | pages [5] -->
However, the development of electric vehicles are still at the initial stage. The layout planning theory of charging facility is also under exploration and there are still very little studies about the network of charging stations. Although some achievements have been made, we still have lots of the uncertainties to study. In this paper, we propose a brand- new model to imply the location of charging stations. Furthermore, we extend our models to suit different circumstances.

<!-- b000053 | heading | pages [5] -->
1.3 Our Work

<!-- b000054 | prose | pages [5] -->
Firstly, we establish a multi-objective programming model to calculate the number of charging stations. Besides, we establish a site selection model to determine the distribution in urban, suburban and rural areas. Then we choose six indexes which affect the number of the electric vehicles. According these indexes, we establish a logistic model to predict the number of the electric vehicles. We can find out the key factors through the predicted data. Furthermore, we can analyze the relationship among the different key factors. Next, we expand our model. We establish a classification system through Q-type clustering model to analyze the electric network development plan for countries in different categories. We also consider the effect of various new technologies, and analyze the status of each technology and the trend of future development. Finally, we write a handout for the leaders to offer them some effective advice on the development of electric network.

<!-- b000055 | heading | pages [5] -->
2 Assumptions and Justifications

<!-- b000056 | prose | pages [5] -->
The charging station which has been built cannot be removed. Since the  construction of charging station costs a lot of manpower and financial resources, the demolition of it will cause greater losses. The candidate points of charging station are obtained through reasonable  analysis and rigorous demonstration. Because if the charging station is built in an area with poor or unsafe conditions, it will lead to fewer cars to be charged.

<!-- b000057 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000058 | furniture | pages [6] -->
Team#73156

<!-- b000059 | furniture | pages [6] -->
Page 4 of 27

<!-- b000060 | prose | pages [6] -->
Each charging station will not break down during charging process. Because the  charging station network will be regularly maintained. Vehicle arrival obeys to Poisson distribution. It is demonstrated in statistics. 

<!-- b000061 | heading | pages [6] -->
3 Distribute the charging stations in the US

<!-- b000062 | prose | pages [6] -->
Task one requires us to determine whether Tesla is on track to allow a full switch to all-electric in the US, and give the distribution of charging stations based on all-electric condition. Firstly, we searching the population density and car ownership per capita of different states of America. According to population density, we divided the United States into urban, suburban and rural areas. Secondly, the total amount of cars in each area is determined by the amount of car ownership per capita. According to queuing theory, we calculate the average waiting time for car charging. Then, we can get the number of supercharging stations theoretically needed. We compare it with the actual number of charging stations, determine whether or not the US can go all-electric. Finally, with the goal of minimum cost and minimum waiting time, we build a multi-objective optimization model to calculate the number of charging stations required in each region.

<!-- b000063 | heading | pages [6] -->
3.1 Concepts introduction

<!-- b000064 | prose | pages [6] -->
Population density  Let ρidenote the population density, i.e. the number of people per square kilometer. The population distributions in the US are obtained from the US Census Bureau [10]. We divide the United States into three regions based on the intensity of the population.

<!-- b000065 | prose | pages [6] -->
When the population density is greater than 150, the area is the urban. Similarly, when the population density is between 50 and 150, the area is suburban. Otherwise, the area is the rural. The dividing results are as follows.

<!-- b000066 | caption | pages [6] -->
Figure 1: The population density distribution in the US

<!-- b000067 | prose | pages [6] -->
Car ownership per capita  Let Hi denote the car ownership per capita, which means the average number of cars owned by each individual. According to the U.S. official statistic [11], the overall car ownership per capita is 0.8. Wherein the car ownership per capita in urban, suburban, rural areas are 0.94, 0.83, 0.60 respectively.

<!-- b000068 | prose | pages [6] -->
Connectivity rate  The distance between two adjacent electric vehicle charging stations has a great influence on the convenience of charging. The closer the charging station is, the higher the charging convenience will be. In general, a supercharging station can provide up to 170 miles of power. If the distance between two charging stations is less than or equal to this value, then the car can provide an endless stream of electricity. That is to say, the

<!-- b000069 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000070 | furniture | pages [7] -->
Team#73156

<!-- b000071 | furniture | pages [7] -->
Page 5 of 27

<!-- b000072 | prose | pages [7] -->
distribution of charging station is reasonable to satisfy the charging needs. Therefore, we define the connectivity rate to reflect the rationality of charging station distribution.

<!-- b000073 | prose | pages [7] -->
connectivity rate = number of adjacent stations < 170 miles away

<!-- b000074 | prose | pages [7] -->
number of all adjacent stations /2 We find the locations of all the charging stations built and to be built from the Tesla website, and mark them on the US map. Then we connect all adjacent charging stations whose distance is less than 170 miles. The road map is shown as below.

<!-- b000075 | caption | pages [7] -->
Figure 2: Connectivity diagram

<!-- b000076 | prose | pages [7] -->
As shown in figure 2, the coverage of the charging stations has basically covered the entire United States, especially in areas with a high population density. After calculation, we find that the connectivity rate has reached 71%. Therefore, we have initially judged that Tesla is making the United States on an all-electric track. Next, we will analyze in detail through modeling.

<!-- b000077 | heading | pages [7] -->
3.2 All-electric evaluation model

<!-- b000078 | prose | pages [7] -->
3.2.1

<!-- b000079 | heading | pages [7] -->
The model construction

<!-- b000080 | heading | pages [7] -->
1) Actual number of electric vehicles

<!-- b000081 | prose | pages [7] -->
The total number of electric vehicles in a region will be affected by many factors. The macroscopic parameter of rangeis Siwhich stands for the acreage of ith area. The parameter Pi represents the percentage of electric vehicles in ith area. Hence, we can get the equation between the total number of electric vehicles and the various factors.

<!-- b000082 | prose | pages [7] -->
ni i Si Hi Pi

<!-- b000083 | heading | pages [7] -->
2) Theoretical number of electric vehicles

<!-- b000084 | prose | pages [7] -->
When the number of electric vehicles reaches a certain level, there needs to be enough charging stations to serve it. Because the supercharging station is much more expensive than the destination charging station, we first consider the number of super charging station. According to the survey data of General Motors in the United States, the utilization rate α of a public charging station is 35%. The electric vehicle can run T miles when charging once at a supercharging station. According to the average annual driving distance L of the car and the average number of driving days D , we can calculate the number of times ( Nsc ) a car is charged on the supercharging station every day.

<!-- b000085 | prose | pages [7] -->
αL Nsc = DT Through multiplying the total number of electric vehicles in each area by the average number of charging times each day, we can get the total number of times all the vehicles in the area needs to be recharged daily. For the charging stations, these are the number

<!-- b000086 | prose | pages [7] -->
Nitotal of charging vehicles they need to service each day,

<!-- b000087 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000088 | furniture | pages [8] -->
Team#73156

<!-- b000089 | furniture | pages [8] -->
Page 6 of 27

<!-- b000090 | prose | pages [8] -->
Nitotal=Nsc× ni. Vehicle arrival is a typical Poisson distribution event [12]. The average service time of a supercharging station are t hours every day. There are λ vehicles arriving at charging station every hour. Poisson distribution is expressed as follows,

<!-- b000091 | prose | pages [8] -->
e- λt (λt)J PJ(t) = J !

<!-- b000092 | prose | pages [8] -->
(J = 0,1,2,...).

<!-- b000093 | prose | pages [8] -->
A supercharging station can be viewed as a single service desk model M/M/1. The average service time per car is μ . When the vehicle arrives at the charging station at a Poisson distribution, if at this time there are a number of vehicles are charging, then the vehicle must wait in line,

<!-- b000094 | prose | pages [8] -->
λ2 Lq=μ( μ-λ) If the average number of arrivals is greater than a certain degree, cars that arrive later cannot be fully charged in time. Under the condition of stable system, the average waiting time will increase first, and then close to a stable value. That is the average waiting time

<!-- b000095 | prose | pages [8] -->
TqSC =

<!-- b000096 | prose | pages [8] -->
Lq.

<!-- b000097 | prose | pages [8] -->
λ Given a waiting time, we can calculate the total number of cars that a supercharging station can service nsc= λt .

<!-- b000098 | heading | pages [8] -->
3.2.2 Model solution and analysis

<!-- b000099 | prose | pages [8] -->
In a charging station, waiting time is generated when more vehicles are queued for charging. The longer the waiting time, the lower the quality of service. In order to make electric vehicles more convenient to charge, we have to shorten the waiting time for the car. Therefore, the number of charging stations need to be increased. The convenience index CIi is defined to reflect the ease of charging in each area.

<!-- b000100 | prose | pages [8] -->
CI = Nitotal i n × r

<!-- b000101 | prose | pages [8] -->
sc i ridenotes the actual number of supercharging stations.

<!-- b000102 | prose | pages [8] -->
Where

<!-- b000103 | prose | pages [8] -->
When the actual number of vehicles needed to be charged is less than themaximum number of vehicles that the charging station can supply, the charging station is considered to be convenient. It can be attributed to the following formula.

<!-- b000104 | prose | pages [8] -->
type convenient

<!-- b000105 | prose | pages [8] -->


<!-- b000106 | prose | pages [8] -->
,CIi 1

<!-- b000107 | prose | pages [8] -->
inconvenient

<!-- b000108 | prose | pages [8] -->
,CIi 1 All the convenient areas are marked with dark blue, and shown as below.

<!-- b000109 | caption | pages [8] -->
Figure 3: Convenient area

<!-- b000110 | prose | pages [8] -->
From Figure 3, we can clearly see that the convenient area has a wide coverage and basically covers the entire United States. Based on the previous connectivity map in the United States and the connectivity rate of 71%, we have reason to believe that Tesla is expected to achieve full electrification in the United States.

<!-- b000111 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000112 | furniture | pages [9] -->
Team#73156

<!-- b000113 | furniture | pages [9] -->
Page 7 of 27

<!-- b000114 | heading | pages [9] -->
3.3 Distribution optimization model

<!-- b000115 | heading | pages [9] -->
3.3.1 The model construction

<!-- b000116 | prose | pages [9] -->
The distribution of charging stations need to consider many aspects, while at the same time it is subject to economy, time and other factors. In order to obtain the optimal distribution program, we establish a multi-objective model with flexible constraints.

<!-- b000117 | prose | pages [9] -->
Goal of minimum cost: On the basis of ensuring a rational distribution of charging stations, we should minimize the cost of our program. Since the prices of supercharging stations and destination charging stations (CSC and CDC) are different, we need to consider the total building cost of them. The number of them are that

<!-- b000118 | prose | pages [9] -->
rSC and rDC respectively. So, we get

<!-- b000119 | prose | pages [9] -->
min Zi rDCCDCrSCCSC.

<!-- b000120 | prose | pages [9] -->
Goal of minimum waiting time: The purpose of building a number of charging stations is to shorten the waiting time for the car to be charged, thereby improving service convenience. We consider the average waiting time of the supercharging station and the destination charging station simultaneously, and take their respective number as a weighting factor. The totalwaiting time obtained should be as small as possible

<!-- b000121 | prose | pages [9] -->
TqDCrDCTqSCrSC minT i q r

<!-- b000122 | prose | pages [9] -->
DC

<!-- b000123 | prose | pages [9] -->
Constraint of distance:

<!-- b000124 | prose | pages [9] -->
, i 1, 2,3 . r r

<!-- b000125 | prose | pages [9] -->
SC

<!-- b000126 | prose | pages [9] -->
When the vehicle travels a long trip, it needs enough power to support it. According to the average annual driving distance L of the car and the average number of driving days D , we can calculate the charging miles the car needs every day

<!-- b000127 | prose | pages [9] -->
A= L .

<!-- b000128 | prose | pages [9] -->
D Wherein α is the utilization rate of a public charging station Hence, the total charging miles required in each area can be obtained from the following formula

<!-- b000129 | prose | pages [9] -->
Ai total Aini When the distribution of charging stations is reasonable, the power provided by the charging station should be greater than the power actually needed. Thus the vehicle can travel a long distance without consuming all the electric. So, the constraint is:

<!-- b000130 | prose | pages [9] -->
2 Ai total lk nk rk

<!-- b000131 | prose | pages [9] -->
k

<!-- b000132 | prose | pages [9] -->
Constraint of convenience

<!-- b000133 | prose | pages [9] -->
k DC,SC

<!-- b000134 | prose | pages [9] -->
When the total number of vehicles that the charging station can serve is greater than the actual number of vehicles, the charging station can satisfy the daily needs. According to convenience index defined before, we should increase the number of charging stations while reducing the waiting time at the same time. Therefore, the convenience index should be less than or equal to 1.

<!-- b000135 | prose | pages [9] -->
CIin

<!-- b000136 | prose | pages [9] -->
r DC DC ni 1 n r SC SC

<!-- b000137 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000138 | furniture | pages [10] -->
Team#73156

<!-- b000139 | prose | pages [10] -->
Constraint of vehicles

<!-- b000140 | furniture | pages [10] -->
Page 8 of 27

<!-- b000141 | prose | pages [10] -->
The biggest difference between destination charging (DC) and supercharging (SC) lies in the charging efficiency. The former costs a long time to charge, thus providing a long trip. The latter costs a short time to charge, but providing a relatively long trip. Hence, the latter one has a higher charging efficiency. Now we assume that TDC represents the daily power supply time ofDC, tDC denotes a fully charged time,while lDC stands for the length of trip one charge can provide. So, the charging efficiency ratio between DC and SC is as follows

<!-- b000142 | prose | pages [10] -->
Pefficiency EFDC  EFSC

<!-- b000143 | prose | pages [10] -->
TDC lDC TSClSC

<!-- b000144 | prose | pages [10] -->
.

<!-- b000145 | prose | pages [10] -->
tDC tSC

<!-- b000146 | prose | pages [10] -->
Therefore, under the condition of the same electricity supply, the relationship between the number of DC stations and SC stations is rSCrDCPefficiency.

<!-- b000147 | prose | pages [10] -->
In addition, the required number of charging stations should be greater than or equal to the actual number of charging stations. So, the constraint is:

<!-- b000148 | prose | pages [10] -->
rSC ni

<!-- b000149 | prose | pages [10] -->
nSC To sum up, the whole optimization model is as follows

<!-- b000150 | heading | pages [10] -->
3.3.2 Model solution and analysis

<!-- b000151 | prose | pages [10] -->
According to data statistics, a charging station consists of 8.8 chargers in general. By using MATBLA to solve the optimization model above, we obtain that the US needs about 15 million chargers in all. Therefore, 1,704,500 charge stations are required. After calculation, we get that urban area needs 1,142,015 charge stations, suburban area needs 392,035 charge stations, rural area needs 170,450 charge stations.

<!-- b000152 | caption | pages [10] -->
Table 1: Distribution results

<!-- b000153 | prose | pages [10] -->
Area Urban area Suburban area Rural area The whole US Number of charging stations 1,142,015 392,035 170450 1,704,500

<!-- b000154 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000155 | furniture | pages [11] -->
Team#73156

<!-- b000156 | furniture | pages [11] -->
Page 9 of 27

<!-- b000157 | heading | pages [11] -->
4 Study on South Korea

<!-- b000158 | prose | pages [11] -->
South Korea is a typical developed country in Northeast of Asia. It has obvious urban-suburban-rural divisions. The population density distribution is as follows. Wherein the blue area is the densely populated area.

<!-- b000159 | caption | pages [11] -->
Figure 4: The population density distribution in South Korea

<!-- b000160 | prose | pages [11] -->
According to the difference in population density, we divide South Korea into three parts: urban area, suburban area, rural area. For different areas, we will build different charging station site selection model.

<!-- b000161 | heading | pages [11] -->
4.1 Urban charging station location model

<!-- b000162 | prose | pages [11] -->
Since there are many electric cars in the city, it is necessary to build a large number of charging stations. On the one hand, there are many restaurants, hotels and shopping malls in the city, most of which have paring lots. Hence, the construction of charging station can rely on the parking lots of these consumption places. On the other hand, according to the location of gas station, the charging stations can also be centrally located next to the main arterial roads with relatively large traffic volumes. We take Seoul as an example to distribute the charging stations.

<!-- b000163 | heading | pages [11] -->
1) Total construction cost and average waiting time

<!-- b000164 | prose | pages [11] -->
The following analysis is similar to task one, so we will not elaborate in detail. The total electric vehicles in Seoul is

<!-- b000165 | prose | pages [11] -->
nseoulseoulSseoulHseoulP . The number of charging times for a car every day is:

<!-- b000166 | prose | pages [11] -->
N = L .

<!-- b000167 | prose | pages [11] -->
DY The number of vehicles needed to charge every day is:

<!-- b000168 | prose | pages [11] -->
Ntotal=N ×nseoul. The average charging miles of public charging station every day is:

<!-- b000169 | prose | pages [11] -->
A= L .

<!-- b000170 | prose | pages [11] -->
D The total charging miles required every day is:

<!-- b000171 | prose | pages [11] -->
Atotal Anseoul . According to the driving data of Ministry of Land, Infrastructure and Transport of Korea, South Korean residents mainly drive out from 9:00 to 17:00. Hence, the charging time of the public charging station is T 8 hours. Besides, most drivers tend to choose

<!-- b000172 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000173 | furniture | pages [12] -->
Team#73156

<!-- b000174 | furniture | pages [12] -->
Page 10 of 27

<!-- b000175 | prose | pages [12] -->
supercharging when going out. So, let the charging time be t 30 min and the mileage be Y 170 miles. The average waiting time of charging is Tq seoul.

<!-- b000176 | prose | pages [12] -->
The total cost of constructing charging stations in Seoul is

<!-- b000177 | prose | pages [12] -->
Zseoul rseoul C .

<!-- b000178 | heading | pages [12] -->
2) Location of charging stations

<!-- b000179 | prose | pages [12] -->
Our goal is to select a plurality of consumption places or gas stations in a city to install charging stations. A charging station should meet the charging needs of allnearby vehicles. If we employthe traditional shortest path location model, the selected locations are concentrated in the city center, which will heaven the traffic pressure. On the contrary, if the charging stations are located on the edge of the city, it will be time-consuming for the vehicles to charge. Therefore, the location should take the distance, time and traffic factors into account.

<!-- b000180 | prose | pages [12] -->
We determine the city center based on the electronic map, and then constructa nn weighted network map according to the size of the city. The innermost four squares are the first level and the outward twelve squares are the second level. There are

<!-- b000181 | prose | pages [12] -->
n /2 levels in all. The length of each square, that is, the initial weight is 1. If the actual position corresponding to the side length appears lakes, rivers, oceans and deserts, the default value of the side length is .

<!-- b000182 | prose | pages [12] -->
In order to reduce the impact on the traffic pressure, we introduce congestion index jk of sidelength vjvk . For the side length at the ith level, we need to update the weight

<!-- b000183 | prose | pages [12] -->
at the time of the mth calculation wjk of vjvk

<!-- b000184 | prose | pages [12] -->
n , . m 1

<!-- b000185 | prose | pages [12] -->
n

<!-- b000186 | prose | pages [12] -->
wjk 1(m i) ,i 1 2

<!-- b000187 | prose | pages [12] -->
2

<!-- b000188 | prose | pages [12] -->
Therefore, the sum of shortest path from one point to any other point is:

<!-- b000189 | prose | pages [12] -->
wjk xjk

<!-- b000190 | prose | pages [12] -->
indicates whether or not to choose vjvk , The 0-1 variable xjk

<!-- b000191 | prose | pages [12] -->
x jk = 1 choose vjvk

<!-- b000192 | prose | pages [12] -->
0

<!-- b000193 | prose | pages [12] -->


<!-- b000194 | prose | pages [12] -->
not

<!-- b000195 | prose | pages [12] -->
Based on the optimization model of task one, we add a new goal of shortest path. It will make the distance to the charging station as short as possible.

<!-- b000196 | prose | pages [12] -->
So, the new added goal is

<!-- b000197 | prose | pages [12] -->
min wjk xjk . The determination of the shortest path needs to be within the nn the new constraint is

<!-- b000198 | prose | pages [12] -->
n

<!-- b000199 | prose | pages [12] -->
n

<!-- b000200 | prose | pages [12] -->


<!-- b000201 | prose | pages [12] -->


<!-- b000202 | prose | pages [12] -->
xjk

<!-- b000203 | prose | pages [12] -->
xkj

<!-- b000204 | prose | pages [12] -->
k 1

<!-- b000205 | prose | pages [12] -->
k1

<!-- b000206 | prose | pages [12] -->
grid range. So,

<!-- b000207 | prose | pages [12] -->
1 

<!-- b000208 | prose | pages [12] -->
j 1

<!-- b000209 | prose | pages [12] -->
1

<!-- b000210 | prose | pages [12] -->
j n

<!-- b000211 | prose | pages [12] -->
 

<!-- b000212 | prose | pages [12] -->


<!-- b000213 | prose | pages [12] -->


<!-- b000214 | prose | pages [12] -->
0

<!-- b000215 | prose | pages [12] -->
j 1, n

<!-- b000216 | prose | pages [12] -->


<!-- b000217 | prose | pages [12] -->
To sum up, the whole model is as follows

<!-- b000218 | prose | pages [12] -->
min Zseoul rseoul C ,

<!-- b000219 | prose | pages [12] -->
min Tq seoul ,

<!-- b000220 | prose | pages [12] -->
min wjk xjk .

<!-- b000221 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000222 | furniture | pages [13] -->
Team#73156

<!-- b000223 | furniture | pages [13] -->
Page 11 of 27

<!-- b000224 | prose | pages [13] -->
Chargers should be dispersed to the city first. Then, according to the characteristics of urban construction, charging stations are formed. They are distributed near the consumption places and gas stations.

<!-- b000225 | heading | pages [13] -->
4.2 Suburban charging station location model

<!-- b000226 | prose | pages [13] -->
We consider that the area between cities are suburbs. Since the suburbs are mainly located on both sides of the road with large traffic flow, we simplify the question to the highway charging station selection question.

<!-- b000227 | prose | pages [13] -->
The macroscopic parameter VFih is the traffic volume in h hours at the ith road. The total number of suburban electric vehicles is:

<!-- b000228 | prose | pages [13] -->
24 n n nsub PVFih

<!-- b000229 | prose | pages [13] -->
i1 h1 The average number of vehicles needed to charge every day is

<!-- b000230 | prose | pages [13] -->
Ntotal=N × nsub. The total charging miles required every day is

<!-- b000231 | prose | pages [13] -->
Atotal Ansub .

<!-- b000232 | prose | pages [13] -->
Therefore, the total cost of suburban charging station construction is

<!-- b000233 | prose | pages [13] -->
Zsub rsub C . The specific location along the highway does not affect the optimization objectives and constraints. So, we can get the optimization model directly.

<!-- b000234 | prose | pages [13] -->
Since the distance between adjacent charging stations does not exceed 170 miles, we can combine several chargers to form a charging station. The charging stations can be built along the road.

<!-- b000235 | heading | pages [13] -->
4.3 Rural charging station location model

<!-- b000236 | prose | pages [13] -->
The rural areas have low density of population, which results in low charging needs. Therefore, we can ignore the waiting time. If the mileage of one charge is larger than the distance between two adjacent charging stations, the charging network can be regarded to cover the entire rural area.

<!-- b000237 | prose | pages [13] -->
We take the location of charging station as the center and the mileage Y as the radius of service circle. The square of the circle is the range that the electric vehicles can reach after charging. To achieve full coverage, there must be another charging station in the circle. From the view of geometric point, that is to make two circles intersect. After

<!-- b000238 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000239 | furniture | pages [14] -->
Team#73156

<!-- b000240 | furniture | pages [14] -->
Page 12 of 27

<!-- b000241 | prose | pages [14] -->
simplification, the full triangular mesh model can be used to achieve full coverage in rural areas.

<!-- b000242 | prose | pages [14] -->
Generally, the charging station is built at the side of the road. Hence, the triangle structure will be destroyed. We assume that the three sides of the triangle formed by the adjacent three chargers are a, b, c respectively. According the Helen formula:

<!-- b000243 | prose | pages [14] -->
p( p a)( p b)( p c)

<!-- b000244 | prose | pages [14] -->
S  We can calculate the area of the triangle. In addition, the economic costs are considered. Hence, the only goal is to minimize the total cost.

<!-- b000245 | prose | pages [14] -->
min Zurban rurban C

<!-- b000246 | prose | pages [14] -->
S Surban

<!-- b000247 | prose | pages [14] -->


<!-- b000248 | prose | pages [14] -->


<!-- b000249 | prose | pages [14] -->
1

<!-- b000250 | prose | pages [14] -->
s.t p 

<!-- b000251 | prose | pages [14] -->
2

<!-- b000252 | prose | pages [14] -->
 (a b c)

<!-- b000253 | prose | pages [14] -->
ac,ab,bc 0

<!-- b000254 | heading | pages [14] -->
4.4 Logistic model

<!-- b000255 | heading | pages [14] -->
4.4.1 Index definition

<!-- b000256 | heading | pages [14] -->
1) Electric vehicle price (EVP)

<!-- b000257 | prose | pages [14] -->
The price of electric cars has a great impact on the sales of electric vehicles. The decrease in the car prices will result in more people buying cars. Hence, we define the electric car price as the average price of all the electric cars sold on the current market.

<!-- b000258 | heading | pages [14] -->
2) Density of population (DP)

<!-- b000259 | prose | pages [14] -->
There will be more electric cars in places with large population density. According to the population density, we divide the US into three parts: urban, suburban and rural.

<!-- b000260 | heading | pages [14] -->
3) Wealth distribution (WD)

<!-- b000261 | prose | pages [14] -->
At present, electric cars are new products, and their prices are relatively high. Hence, there are more electric cars in rich places. We use the GDP value of a certain area to represent the wealth of the region.

<!-- b000262 | heading | pages [14] -->
4) Environmental awareness (EA)

<!-- b000263 | prose | pages [14] -->
environmental-friendly Electric vehicles are products.

<!-- b000264 | prose | pages [14] -->
With the increasing awareness of environmental protection, the sales of electric vehicles will become higher. We define the environmental awareness as:

<!-- b000265 | prose | pages [14] -->
EA=the number of people buying electric cars / the number of people buying cars

<!-- b000266 | heading | pages [14] -->
5) Policy orientation (PO)

<!-- b000267 | prose | pages [14] -->
Policy orientation can guide the purchasing direction of people to a certain extent. We define the amount of subsidies of buying an electric car as policy orientation.

<!-- b000268 | heading | pages [14] -->
6) Government investment (GI)

<!-- b000269 | prose | pages [14] -->
The improvement of supporting services and facilities will largely affect the enthusiasm of consumers purchasing electric cars. So we use the amount of investment in supporting facilities to measure this index.

<!-- b000270 | heading | pages [14] -->
4.4.2 The model construction

<!-- b000271 | prose | pages [14] -->
Logistic regression is a generalized linear regression analysis model, which is commonly used in the fields of data mining and economic forecasting. Therefore, it is

<!-- b000272 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000273 | furniture | pages [15] -->
Team#73156

<!-- b000274 | furniture | pages [15] -->
Page 13 of 27

<!-- b000275 | prose | pages [15] -->
suitable for the question. We select the six indicators defined above as influencing factors, and establish the Logistic regression model to do the prediction

<!-- b000276 | heading | pages [15] -->
4.4.3 Model solution and analysis

<!-- b000277 | prose | pages [15] -->
We use SAS to test the model, and the test results are shown in the appendix. After analysis, we find that only WD, PO and GI pass the test. Therefore, we get the logistic regression equation for these three indicators.

<!-- b000278 | prose | pages [15] -->
For cities, the regression equation is

<!-- b000279 | prose | pages [15] -->
p ln

<!-- b000280 | prose | pages [15] -->
0.2176 1.7258WD 0.2987 PO 1.3291GI . 1p

<!-- b000281 | prose | pages [15] -->
For rural areas, the regression equation is

<!-- b000282 | prose | pages [15] -->
p ln

<!-- b000283 | prose | pages [15] -->
0.1082 0.9652 WD 1.6549 PO 0.3472 GI . 1p

<!-- b000284 | prose | pages [15] -->
For the whole country, the regression equation is

<!-- b000285 | prose | pages [15] -->
p ln

<!-- b000286 | prose | pages [15] -->
0.1110 1.7137 WD 1.5000PO 1.614GI . 1p

<!-- b000287 | heading | pages [15] -->
4.5 Answers of the Questions

<!-- b000288 | prose | pages [15] -->
(a) After calculation, the optimal number of charging stations in South Korea is about 270,000. The distribution is mainly concentrated in the Seoul Metropolitan Area and the Busan Metropolitan Area. The remaining areas are relatively sparsely distributed. Their general location is shown as following figure.

<!-- b000289 | caption | pages [15] -->
Figure 5: Distribution of charging stations in South Korea

<!-- b000290 | prose | pages [15] -->
The model we constructed above aims to minimize the total cost and the average waiting time. While the cost of the chargers will have a direct impact on the total cost. In addition, the number of chargers affect the total cost and average waiting time as well. The number of chargers is affected by the investment. In conclusion, the key factors that shape the development of our plan are the building cost of chargers and government investment.

<!-- b000291 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000292 | furniture | pages [16] -->
Team#73156

<!-- b000293 | furniture | pages [16] -->
Page 14 of 27

<!-- b000294 | prose | pages [16] -->
(b) It is well known that the number of chargers and the number of electric vehicles interact and influence each other. In order to facilitate the study, we define a lag index which is .

<!-- b000295 | prose | pages [16] -->
The macroscopic parameter is defined as lag cardinality. Therefore, for the f (x) , the lag index at point x is function

<!-- b000296 | prose | pages [16] -->


<!-- b000297 | prose | pages [16] -->
x y

<!-- b000298 | prose | pages [16] -->
. 

<!-- b000299 | caption | pages [16] -->
Figure 6: Lag index

<!-- b000300 | prose | pages [16] -->
Now we have an exponential function: (x) axx200.05

<!-- b000301 | prose | pages [16] -->
x

<!-- b000302 | prose | pages [16] -->
Let ( y) (x x) axx , we can get the lag index at point x as

<!-- b000303 | prose | pages [16] -->
y x .  

<!-- b000304 | prose | pages [16] -->
Since (y) can be obtained from the translation of (x) , we regard this lag as synchronous lag. It has been observed that for the phenomenon of synchronous lag, the larger x is, the smaller x is. That is x x . Based on the growth forecast of supercharging stations [13], we obtain the sales growth forecast curve (x) of Tesla while meeting the service conditions. The curveis exponential. Then, we let 20 and obtain a new Tesla sales growth forecast curve (x) and (x) , when 0.05 (after one year). However, we find that for the curves of

<!-- b000305 | prose | pages [16] -->
x x is not established. As the year grows, the relationship is

<!-- b000306 | prose | pages [16] -->
the relationship of established.

<!-- b000307 | caption | pages [16] -->
Figure 7: Change of lag index

<!-- b000308 | prose | pages [16] -->
We can regard the sales growth forecast curve as an exponential curve. If the number of chargers has no effect on the sales volume of Tesla, the overall construction of chargers will be delayed by one year. The new sales growth forecast curve should appear synchronized lag phenomenon and the relationship of x x should be established all the time. However, there is no synchronous lag in the actual forecast situation, and the relationship of xx even appears. It shows that the construction lag makes the sales of Tesla decline. And the evaporation situation of sales will increase as year grows, thus showing a vicious cycle. Similarly, we use Tesla sales growth to predict the growth of chargers. Then, we put a whole lag into the sales growth curve and analyze the relevant index.

<!-- b000309 | prose | pages [16] -->
According to the conclusion obtained, the investment distribution of chargers is shown as follows.

<!-- b000310 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000311 | furniture | pages [17] -->
Team#73156

<!-- b000312 | furniture | pages [17] -->
Page 15 of 27

<!-- b000313 | caption | pages [17] -->
Figure 8: Investment distribution of chargers

<!-- b000314 | prose | pages [17] -->
The whole process is divided into three stages: early, middle and late stage. In the early stage, we need to increase investment in the construction of chargers to ensure that the early owners can get the most basic charging service. Therefore, the number of people buying electric cars will increase.

<!-- b000315 | prose | pages [17] -->
In the middle stage, since the early construction of the chargers is sufficient to deal with the growth of electric vehicles, we can use part of the investment for subsidies. Thus, it can stimulate the new energy automotive industry.

<!-- b000316 | prose | pages [17] -->
In the late stage, the number of vehicles close to a stable condition. So, we need to constantly improve the charging facilities services.

<!-- b000317 | prose | pages [17] -->
To sum up, the country should build all city-based chargers first. Through the curves of urban and rural areas, we can find that the growth rate of Tesla in urban area is always greater than that of the rural area.

<!-- b000318 | prose | pages [17] -->
In the initial stage of construction, we should build charging stations first to promote the purchase of cars. In the later stage of construction, the charging stations are built to cope with the purchase of cars. In conclusion, chargers should be built first.

<!-- b000319 | prose | pages [17] -->
From the test result of Logistic model, we can filter out the key factors. Hence, the key factors that affect our proposed charging station plan are wealth distribution and government investment.

<!-- b000320 | prose | pages [17] -->
(c) From the Logistic model established above, we have drawn a trend graph of market share of electric vehicles and the corresponding timeline. The result is as follows.

<!-- b000321 | caption | pages [17] -->
Figure 9: Trend of market share of electric vehicles

<!-- b000322 | prose | pages [17] -->
From the table below, we can clearly see the corresponding years of each degree of full electrification. It is notable that when the market share of electric vehicles reaches 90%, it close to a stable condition. At this time, the government needs to intervene to impose a moratorium on the use of oil and gas, which will eventually lead to real full electrification.

<!-- b000323 | caption | pages [17] -->
Table 2: Timeline of full evolution to electric vehicles

<!-- b000324 | prose | pages [17] -->
Degree 10% 20% 30% 40%

<!-- b000325 | prose | pages [17] -->
Year 2024 2027 2031 2033

<!-- b000326 | prose | pages [17] -->
50% 60% 70% 80% 90%~100%

<!-- b000327 | prose | pages [17] -->
2035 2037 2040 2043 2069

<!-- b000328 | prose | pages [17] -->
In 2016, Tesla entered South Korea officially. Besides, there are fewer subsidies to buy electric vehicles in South Korea. It shows that the policy orientation has an important influence on the electrification conversion. Therefore, the key factor that shapes our proposed growth plan timeline is policy orientation.

<!-- b000329 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000330 | furniture | pages [18] -->
Team#73156

<!-- b000331 | furniture | pages [18] -->
Page 16 of 27

<!-- b000332 | heading | pages [18] -->
5 Create a classification system

<!-- b000333 | prose | pages [18] -->
Since countries with different geography, population and wealth distributions have different overall patterns of growth, the network of chargers we proposed earlier does not apply to every country. To help a country determine the overall growth model that it should follow, we establish a Q-based clustering model for each country. Therefore, it can deploy its coverage plan of charging station network better.

<!-- b000334 | heading | pages [18] -->
5.1 The model construction

<!-- b000335 | prose | pages [18] -->
To classify different types of countries, it is necessary to describe the similarities between different countries quantitatively. While a country contains many indicators,we can treat each country as a point in space, where p is the number of indicators contained in each country. In order to classify countries more accurately, we selected five different indicators: population density (DP), gross domestic product (GDP), country area (CA), government investment (GI), electric vehicle price (EVP). Next, we characterize the similarities between two countries.

<!-- b000336 | prose | pages [18] -->
In cluster analysis, the Minkowski distance is the most commonly used method.

<!-- b000337 | prose | pages [18] -->
However, when using the Min-style distance, the information will overlap due to the correlation between national indicators. It will emphasize the correlation between some indicators unilaterally. Therefore, we consider to employ Mahilanobis distance to measure the similarity.

<!-- b000338 | prose | pages [18] -->
d (x, y) 

<!-- b000339 | prose | pages [18] -->
T(xy) .

<!-- b000340 | prose | pages [18] -->
(x y)

<!-- b000341 | prose | pages [18] -->
Mahalanobis distance of all linear transformation is invariable, so it is not affected by the dimension. Since we have a measure of the similarity between countries, we then measure the similarity between classes.

<!-- b000342 | prose | pages [18] -->
Under this circumstance, the Nearest Neighbor or Single Linkage Method is adopted.

<!-- b000343 | prose | pages [18] -->
D(G1, G2)  min {d (xi, y j)} . xi G1 ,x j G2 We can simply assume that this is the shortest distance between the nearest two points in the two classes.

<!-- b000344 | heading | pages [18] -->
5.2 Model solution and analysis

<!-- b000345 | prose | pages [18] -->
In order to make our classification more representative, we have chosen eight countries in different parts of the world. The information is shown as below.

<!-- b000346 | caption | pages [18] -->
Table 3: Eight countries

<!-- b000347 | prose | pages [18] -->
Index 1 2

<!-- b000348 | prose | pages [18] -->
Country Australia Indonesia

<!-- b000349 | prose | pages [18] -->
Index 5 6

<!-- b000350 | prose | pages [18] -->
Country Korea Saudi Arabia

<!-- b000351 | prose | pages [18] -->
3 4

<!-- b000352 | prose | pages [18] -->
United States Singapore

<!-- b000353 | prose | pages [18] -->
7 8

<!-- b000354 | prose | pages [18] -->
China Uruguay

<!-- b000355 | prose | pages [18] -->
Using the classification system we set up above, we can draw the following cluster map.

<!-- b000356 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000357 | furniture | pages [19] -->
Team#73156

<!-- b000358 | furniture | pages [19] -->
Page 17 of 27

<!-- b000359 | caption | pages [19] -->
Figure 10: Cluster diagram

<!-- b000360 | prose | pages [19] -->
According to this classification system, we can divide these countries into three categories.

<!-- b000361 | prose | pages [19] -->
The first category is the developed countries led by the United States. They have invested heavily in the construction of charging stations and will soon enter the saturation period of growth. The key factor for their growth in these countries is investment.

<!-- b000362 | prose | pages [19] -->
The second category is the developing countries led by China. Charging stations in these countries are at an early stage of construction. In the next few years, under the influence of investment, they will usher in an explosion of growth. The key factors of the growth of network are the investment and public awareness of environmental protection.

<!-- b000363 | prose | pages [19] -->
The third category is underdeveloped countries led by Indonesia. These countries have not yet built their charging networks and will grow slowly under the influence of policies and investments in the future. Therefore, the key factors for their growth in these countries are policies and investments.

<!-- b000364 | heading | pages [19] -->
6 Comment on the effect of new technologies

<!-- b000365 | prose | pages [19] -->
Super-cycle trains use solar energy for rapid transit between cities, and electric vehicles can improve the quality of the environment. But only aiming at protecting the environment does not mean that electric vehicles can be truly universal. In this regard, we establish an evaluation model to investigate whether these technologies can promote the popularity of electric vehicles.

<!-- b000366 | heading | pages [19] -->
6.1 The model construction

<!-- b000367 | prose | pages [19] -->
To investigate whether the electric vehicles are popular, we need to know their growth rate, which is related to the country's GDP, URP and OPH. The general law of things shows that the development of electric vehicles will close to a stable condition, so we use the logistic curve to predict the impact of different technologies on the growth rate

<!-- b000368 | prose | pages [19] -->
r and to determine whether it can contribute to the popularity of electric vehicles.

<!-- b000369 | prose | pages [19] -->
First of all, in order to eliminate the dimensional effect of the above three variables and make each variable have equal expressive force, we standardize the data of GDP, URP and OPH indicators. The formula is as follows.

<!-- b000370 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000371 | furniture | pages [20] -->
Team#73156

<!-- b000372 | furniture | pages [20] -->
Page 18 of 27

<!-- b000373 | prose | pages [20] -->
Therefore, we can get the expression of the growth rate of electric vehicles. In addition, we can also infer whether these technologies have a catalytic role to promote the popularity of electric vehicles

<!-- b000374 | heading | pages [20] -->
6.2 Model analysis

<!-- b000375 | heading | pages [20] -->
The popularity of electric vehicles results from the construction of the fast-

<!-- b000376 | prose | pages [20] -->
changing power station. At present, electric vehicles use liquid lithium batteries, but the biggest problem with liquid lithium batteries is their short life. This is also the key reason that prevents electric vehicles from becoming mainstream. If drivers charge the car regularly or each charging time is too long, it will affect the mind position in the public about electric car. Fortunately, various countries in the world are stepping up the construction of fast-changing electric vehicles. In particular, Tesla has invested heavily in the construction of charging stations (including super-charging stations and destination charging stations), which lays the foundation for the popularity of electric vehicles.

<!-- b000377 | prose | pages [20] -->
The development of autopilot technology has increased the ownership of electric vehicles. Nowadays, Artificial Intelligence (AI) has made breakthrough progress in areas such as machine learning and computer vision fields, thus making autopilot technology possible. Because the cost of maintaining the electric vehicles is lower. The prospect of autonomous driving technology is very broad. On the one hand, most of the two types of people are facing mobility restrictions from the aging and the disabled market, and the development of this technology makes their free passage possible. On the other hand, traffic congestion in cities is a problem that every metropolitan area faces. Autonomous driving on-board sensors can be used in conjunction with intelligent transportation systems to optimize traffic flow at intersections. The green or red-light time interval is dynamic. According to the changes of real-time traffic, we alleviate congestion by increasing the efficiency of traffic flow. This provides a powerful driving force for the popularity of electric vehicles.

<!-- b000378 | prose | pages [20] -->
The development of super-ring trains and flying cars will also contribute to the popularity of electric vehicles. Super Loop trains are solar-powered electric vehicles that can reach 1,223 kilometers per hour at speeds of 340 meters per second. It is apparently faster than any other commercial train traveling on Earth, in terms of future intercity traffic. Revolutionary breakthrough and its construction costs will be lower than the cost of the general high-speed rail construction, under the premise of ignoring the impact of the weather more secure. The demand of public is transferred from flight to the electric vehicles, which improves the ownership of electric vehicles and provides a potential driver for the popularity of electric vehicles.

<!-- b000379 | prose | pages [20] -->
Therefore, we believe that the popularity of electric vehicles will continue to rise. In the near future, the overall popularity of electric vehicles will surely be realized.

<!-- b000380 | heading | pages [20] -->
7 Sensitivity Analysis

<!-- b000381 | prose | pages [20] -->
The number of chargers in each charging station has a direct impact on the waiting time of driver. From the model above, we can see that our solution is obtained under the condition that each charging station has 8.8 chargers. In addition, the average waiting time is also affected by the daily charging time and fully charging time. Since the population distribution and economic conditions vary from country to country, the average supplying, there is a slight difference between the daily power supply time and the number of chargers per charging station. To test the robustness of the model and make the model more applicable, we will change the parameters that affect the latency and conduct sensitivity analysis.

<!-- b000382 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000383 | furniture | pages [21] -->
Team#73156

<!-- b000384 | furniture | pages [21] -->
Page 19 of 27

<!-- b000385 | prose | pages [21] -->
We still take the United States as an example. From an intuitive point of view, we can see that when the waiting time for charging is reduced, all-electric charging requires less charging stations on the original basis. The government can save money to invest in other fields. Next, we mainly consider the number of average chargers (NAV) and the daily supply time (AST). Through the model established before, we calculate the results under different values.

<!-- b000386 | caption | pages [21] -->
Table 4: Sensitivity analysis

<!-- b000387 | prose | pages [21] -->
NAV 8.6 8.7

<!-- b000388 | prose | pages [21] -->
NCS 1708680 1707530

<!-- b000389 | prose | pages [21] -->
AST 6 7

<!-- b000390 | prose | pages [21] -->
NSC 1968320 1839860

<!-- b000391 | prose | pages [21] -->
8.8 8.9 9.0

<!-- b000392 | prose | pages [21] -->
1704500 1703750 1701980

<!-- b000393 | prose | pages [21] -->
8 8 9 10

<!-- b000394 | prose | pages [21] -->
1704500 1639670 1542390

<!-- b000395 | prose | pages [21] -->
Here NSC is the number of charging stations. Through the table above, we find that the change of these factors does affect the waiting time, thus affecting the number of charging stations required for the full scale. This shows that our model has good stability and strong adaptability.

<!-- b000396 | heading | pages [21] -->
8 Conclusions

<!-- b000397 | heading | pages [21] -->
8.1 Strengths

<!-- b000398 | prose | pages [21] -->
1) The site-selection model takes the idea of clustering. And it splits the whole network into small cells. Not only effectively solve the distribution problems of charging stations, and simplify the complexity of distribution.

<!-- b000399 | prose | pages [21] -->
2) The site-selection model has improved the traditional model. The shortest sumof the traditional shortest path location model will make the site concentrated in the central area. In our model, we introduce the concept of congestion index. After multiple calculations, the weight of each side is updated every time. In the end, the scattered distribution is achieved. The results obtained is convicing.

<!-- b000400 | prose | pages [21] -->
3) We use the custom indicator "lag index" to analyze the relationship between variables. This idea is very innovative

<!-- b000401 | prose | pages [21] -->
4) Sensitivity analysis shows that our model is robust and reliable.

<!-- b000402 | heading | pages [21] -->
8.2 Weaknesses

<!-- b000403 | prose | pages [21] -->
1) There are some restrictions on the use of the model. Thus, this model is a bit rough. If we want to improve the model, we should consider more aspects.

<!-- b000404 | prose | pages [21] -->
2) We do not take the transition time into account, which weakens the accuracy.

<!-- b000405 | heading | pages [21] -->
8.3 Model extension

<!-- b000406 | prose | pages [21] -->
The model can be extended to many industries, such as the courier industry, the medical industry, the retail industry.

<!-- b000407 | prose | pages [21] -->
Take the courier industry as an example, we can compare a courier point to a charging station. Courier service range corresponds to the mileage of the electric car after charging, while the average delivery time corresponds to the average waiting time for electric car charging. Moreover, the demand for expressing delivery is very different in cities, suburbs and villages. Therefore, it is completely possible to use the charging station model to distribute the courier points.

<!-- b000408 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000409 | furniture | pages [22] -->
Team#73156

<!-- b000410 | furniture | pages [22] -->
Page 20 of 27

<!-- b000411 | heading | pages [22] -->
9 A Handout to the Leaders

<!-- b000412 | prose | pages [22] -->
To reduce the use of fossil fuels and look for cleaner energy sources, we examine the current status of electric vehicle ownership in most countries, as well as the distribution and size of the corresponding charging stations.

<!-- b000413 | prose | pages [22] -->
First of all, we analyze the present Tesla charging station network. Currently, the United States has 4,200 charging stations at all,550 of which are super charging stations, making it the world's most advanced charging station construction country. In order to explore whether Tesla can be fully galvanized in the United States, we divide the United States into cities, suburbs and rural areas according to the density of population. For different regions, the charging station location planning mode are different. Inparticular, we collect the location of all existing charging stations in the United States and the blueprint for building charging stations in the future. Based on these data, we map out the connectivity network for charging stations in the United States, which shows that the connectivity network has basically achieved the coverage of the whole country. Only a small part of the countryside has not been covered. In fact, this is similar to most of the developed countries in the world, such as Britain, Germany and France. For developed countries, the key factor which should be considered is investment.

<!-- b000414 | prose | pages [22] -->
Secondly, we analyze the construction of the charging station network in more developed countries such as Korea and China. There are currently 131 charging stations in Korea, 22 of which are super charging stations. Similar to the United States, South Korea also has obvious divisions of the urban, suburban and rural areas, in which cities with densely populated areas are mainly located in coastal areas. Popular cities such as Seoul, for example, has basically covered the network of charging stations, while some ordinary cities have not yet built relevant infrastructure and only a handful of rural residents have charging stations. The car ownership per capita and coverage of electric vehicles in South Korea are all obviously lower than that in United States and other developed countries. For those countries that have just begun to develop electric vehicles, the key factors should be considered are investment and environmental awareness. The charging station should be built first. Because city is the core of a country and it has occupied the majority of the population in these countries. Besides, when employing the strategy of encircling the rural areas from the cities, we should not forget the development of environmental protection.

<!-- b000415 | prose | pages [22] -->
Finally, we have analyzed how underdeveloped countries such as Uruguay and Indonesia build a charging stations network. Due to economic, policy or other reasons, these countries have not yet carried out the construction of related infrastructure, or related construction is extremely small to ignore. It is wise to make a plan to transform personal transport to all-electric vehicles. For those countries that have not developed electric vehicles yet, we suggest that the government should focus on policy and investment. On the one hand, they should encourage citizens to buy electric vehicles and give them considerable subsidies to increase the recognition of electric vehicles among citizens.

<!-- b000416 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000417 | furniture | pages [23] -->
Team#73156

<!-- b000418 | furniture | pages [23] -->
Page 21 of 27

<!-- b000419 | heading | pages [23] -->
10 Reference

<!-- b000420 | prose | pages [23] -->
[1] Gao Jianping. Electric vehicle charging station network planning and optimization

<!-- b000421 | prose | pages [23] -->
[D]. Shandong University, 2012. [2] Etezadi-amoli M, Choma K, Stefani J. Rapid-charge Electric-vehicle Stations[J].

<!-- b000422 | prose | pages [23] -->
IEEE Trans on Power Delivery, 2010, 25(3): 1883-1887. [3] Zhou Hongchao, Li Haifeng. Study on Location Optimization Model of Electric

<!-- b000423 | prose | pages [23] -->
Vehicle Charging Station Based on Game Theory [J]. Science and Technology, 2011,11 (02): 51-54. [4] Xu Fan, Yu Guoqin, Gu Linfeng. Electric vehicle charging station layout planning [J]

<!-- b000424 | prose | pages [23] -->
East China Electric Power, 2009,17 (10): 1678-1682. [5] Ahmed Yousuf Saber, Ganesh Kumar Venayagamoorthy. One million plug-in electric

<!-- b000425 | prose | pages [23] -->
vehicles on the road by2015[C]. IEEE Conference on Intelligent Transportation Systems, St.Louis, MO, USA, 2009. [6] Hengsong Wang, Qi Huang. A novel approach for the layout of electric vehicle

<!-- b000426 | prose | pages [23] -->
charging station[A]. IEEE Conferences, 2010. [7] Holzman. An Association Between Air Pollution and Mortality in six US Cities[M].

<!-- b000427 | prose | pages [23] -->
New England J. Med. 1993, 173-175. [8] Zhou Hongchao, Li Haifeng. Research on Location Optimization of Electric Vehicle

<!-- b000428 | prose | pages [23] -->
Charging Station Based on Game Theory[J]. Science and Industry, 2011,11 (2): 51- 54. [9] Hakimi. New direction in economical practice[M]. Edward Elgar Publishing Limited,

<!-- b000429 | prose | pages [23] -->
1997. [10] http://www.qiwen.org/renkou/shijierenkou/7769.html [11] http://auto.163.com/18/0125/07/D8VRECD1000884MM.html [12] Zhao Ying. Poisson distribution and its application [J]. Journal of Liaoning Jiaotong

<!-- b000430 | prose | pages [23] -->
University, 2009. [13] http://supercharge.info

<!-- b000431 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000432 | furniture | pages [24] -->
Team#73156

<!-- b000433 | heading | pages [24] -->
11 Appendix

<!-- b000434 | furniture | pages [24] -->
Page 22 of 27

<!-- b000435 | caption | pages [24] -->
Table 5: Test results of the urban

<!-- b000436 | prose | pages [24] -->
Deviations and Pearson Goodness-of-Fit Statistics

<!-- b000437 | prose | pages [24] -->
Degree of freedom Principle Value

<!-- b000438 | prose | pages [24] -->
Deviation 1.9697 35

<!-- b000439 | prose | pages [24] -->
Pearson 38.1268 35

<!-- b000440 | prose | pages [24] -->
Value/degree of freedom Pr>Chi

<!-- b000441 | prose | pages [24] -->
1.1991 0.0024

<!-- b000442 | prose | pages [24] -->
1.0893 0.4278

<!-- b000443 | prose | pages [24] -->
Maximum likelihood estimation

<!-- b000444 | prose | pages [24] -->
Estimation Parameter Degree of freedom Error Chi-Wald Pr>Chi

<!-- b000445 | prose | pages [24] -->
0.2176 Intercept 1 0.5357 0.0414 0.0150

<!-- b000446 | prose | pages [24] -->
-1.2326 EVP 1 0.7627 4.3827 0.8290

<!-- b000447 | prose | pages [24] -->
2.3297 DP 1 0.6576 4.8723 0.9802

<!-- b000448 | prose | pages [24] -->
1.7258 WD 1 0.4294 5.1284 0.0300

<!-- b000449 | prose | pages [24] -->
-0.9624 EA 1 0.5876 3.8527 0.7248

<!-- b000450 | prose | pages [24] -->
0.2987 PO 1 0.8423 4.7426 0.0186

<!-- b000451 | prose | pages [24] -->
1.3291 GI 1 0.2343 3.2973 0.0236

<!-- b000452 | caption | pages [24] -->
Table 6: Test results of the rural

<!-- b000453 | prose | pages [24] -->
Deviations and Pearson Goodness-of-Fit Statistics

<!-- b000454 | prose | pages [24] -->
Degree of freedom Principle Value

<!-- b000455 | prose | pages [24] -->
Deviation 1.1837 35

<!-- b000456 | prose | pages [24] -->
Pearson 43.1245 35

<!-- b000457 | prose | pages [24] -->
Value/degree of freedom Pr>Chi

<!-- b000458 | prose | pages [24] -->
1.1837 0.0013

<!-- b000459 | prose | pages [24] -->
1.8537 0.3867

<!-- b000460 | prose | pages [24] -->
Maximum likelihood estimation

<!-- b000461 | prose | pages [24] -->
Estimation Parameter Degree of freedom Error Chi-Wald Pr>Chi

<!-- b000462 | prose | pages [24] -->
0.1082 Intercept 1 0.2635 0.4826 0.0150

<!-- b000463 | prose | pages [24] -->
-1.9238 EVP 1 0.4264 5.3742 0.9868

<!-- b000464 | prose | pages [24] -->
2.1924 DP 1 0.6336 7.2742 0.6967

<!-- b000465 | prose | pages [24] -->
0.9652 WD 1 0.2743 4.7358 0.0283

<!-- b000466 | prose | pages [24] -->
1.2731 EA 1 0.8443 6.8648 0.7242

<!-- b000467 | prose | pages [24] -->
1.6549 PO 1 0.9535 5.8368 0.0320

<!-- b000468 | prose | pages [24] -->
0.3472 GI 1 0.4537 3.9586 0.0153

<!-- b000469 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000470 | furniture | pages [25] -->
Team#73156

<!-- b000471 | prose | pages [25] -->
Main Program

<!-- b000472 | prose | pages [25] -->
%% Initialization environment clc clear close all

<!-- b000473 | prose | pages [25] -->
landcolor = [0.98 0.97 0.97]; lakescolor = [0.71 0.84 0.92]; %% Read and process tesla data data = importdata('WebData.txt'); data = data{1, 1}; %initial data

<!-- b000474 | prose | pages [25] -->
flag1 = 'type":["'; flag2 = '"],"open';

<!-- b000475 | prose | pages [25] -->
flag3 = 'soon":"'; flag4 = '","la'; flag5 = 'latitude":"'; flag6 = '","long';

<!-- b000476 | prose | pages [25] -->
flag7 = 'ngitude":"';

<!-- b000477 | prose | pages [25] -->
index1 = strfind(data, flag1); index2 = strfind(data, flag2); index3 = strfind(data, flag3); index4 = strfind(data, flag4); index5 = strfind(data, flag5); index6 = strfind(data, flag6); index7 = strfind(data, flag7);

<!-- b000478 | prose | pages [25] -->
for i = 1:length(index1)

<!-- b000479 | prose | pages [25] -->
pdata{i, 1} = data(index1(i)+length(flag1):index2(i)- 1 ); %location_type pdata{i, 2} = data(index3(i)+length(flag3):index4(i)- 1 ); %open_soon pdata{i, 3} = data(index5(i)+length(flag5):index6(i)- 1 ); %latitude pdata{i, 4} = data(index7(i) + length(flag7):index7(i) + length(flag7)+10); %longitude

<!-- b000480 | furniture | pages [25] -->
Page 23 of 27

<!-- b000481 | prose | pages [25] -->
end %% Map of the Tesla charging station in the United States [m, n] = size(pdata); rest = zeros(m, n);

<!-- b000482 | prose | pages [25] -->
for i = 1:m

<!-- b000483 | prose | pages [25] -->
rest(i, 3) = str2num( pdata{i, 2}); %Will it open in the future

<!-- b000484 | prose | pages [25] -->
if ~isempty( strfind(pdata{i, 1}, 'charge'))

<!-- b000485 | prose | pages [25] -->
rest(i, 4) = 1; %Is it an effective charging station

<!-- b000486 | prose | pages [25] -->
end if ~isempty( strfind(pdata{i, 1}, 'super'))

<!-- b000487 | prose | pages [25] -->
rest(i, 5) = 1; %Is it a super charging station

<!-- b000488 | prose | pages [25] -->
end

<!-- b000489 | prose | pages [25] -->
rest(i, 1) = str2num( pdata{i, 3}); %latitude rest(i, 2) = str2num( pdata{i, 4}); %longitude end

<!-- b000490 | prose | pages [25] -->
limit = [26 48 -130 -60];

<!-- b000491 | prose | pages [25] -->
res = []; for i = 1:m

<!-- b000492 | prose | pages [25] -->
if rest(i, 1) > limit(1) && rest(i, 1) < limit(2) && rest(i, 2) > limit(3) && rest(i, 2) < limit(4) && rest(i, 4) == 1

<!-- b000493 | prose | pages [25] -->
res = [res; rest(i, :)]; end

<!-- b000494 | prose | pages [25] -->
end

<!-- b000495 | prose | pages [25] -->
mcolor = [249 222 239; 255 86 0; 236 165

<!-- b000496 | prose | pages [25] -->
201; 47 70 150]; mcolor = mcolor ./255;

<!-- b000497 | prose | pages [25] -->
for i = 1:size(res, 1)

<!-- b000498 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000499 | furniture | pages [26] -->
Team#73156

<!-- b000500 | prose | pages [26] -->
curpoint(i).Geometry = 'Point'; nextpoint(i).Geometry = 'Point'; if res(i, 3) == 0

<!-- b000501 | prose | pages [26] -->
curpoint(i).Lon = res(i, 2); curpoint(i).Lat = res(i, 1); curpoint(i).Name = ''; end if res(i, 3) == 1

<!-- b000502 | prose | pages [26] -->
nextpoint(i).Lon = res(i, 2); nextpoint(i).Lat = res(i, 1); nextpoint(i).Name = '';

<!-- b000503 | prose | pages [26] -->
end

<!-- b000504 | prose | pages [26] -->
end

<!-- b000505 | prose | pages [26] -->
figure ax = worldmap('World'); ax = worldmap([25, 55], [230, 300]); land = shaperead('landareas', 'UseGeoCoords', true); geoshow(ax, land, 'FaceColor', landcolor) lakes = shaperead('worldlakes', 'UseGeoCoords', true); geoshow(lakes, 'FaceColor', lakescolor) states = shaperead('usastatelo', 'UseGeoCoords', true); scolor = []; for i = 1:size(states, 1)

<!-- b000506 | prose | pages [26] -->
if states(i).PopDens2000 >= 150

<!-- b000507 | prose | pages [26] -->
scolor = [scolor; mcolor(4, :)]; elseif states(i).PopDens2000 >= 50

<!-- b000508 | prose | pages [26] -->
scolor = [scolor; mcolor(3, :)]; else

<!-- b000509 | prose | pages [26] -->
scolor = [scolor; mcolor(1, :)]; end end index = find(scolor(:, 1) >= 1); for i = 1:size(index, 1)

<!-- b000510 | prose | pages [26] -->
scolor(index(i), :) = [1 0 0];

<!-- b000511 | prose | pages [26] -->
end faceColors = makesymbolspec('Polygon',...

<!-- b000512 | prose | pages [26] -->
{'INDEX', [1 numel(states)], 'FaceColor', ...

<!-- b000513 | furniture | pages [26] -->
Page 24 of 27

<!-- b000514 | prose | pages [26] -->
scolor}); %repmat(landcolor, numel(states), 1) geoshow(ax, states, 'DisplayType', 'polygon', ...

<!-- b000515 | prose | pages [26] -->
'SymbolSpec', faceColors) rivers = shaperead('worldrivers', 'UseGeoCoords', true); geoshow(rivers, 'Color', 'blue') geoshow(nextpoint, 'MarkerEdgeColor','r','Marker', '.', 'MarkerSize',10)

<!-- b000516 | prose | pages [26] -->
geoshow(curpoint,'MarkerEdgeColor', 'r', 'Marker', '.', 'MarkerSize',10 ) set(gcf, 'Position', [100, 100, 800, 400])

<!-- b000517 | prose | pages [26] -->
%% Reading the data of Super filling piles in the United States [~, ~, data] = xlsread('SuperChargeData.xlsx'); count = 1; for i = 1:size(data, 1)

<!-- b000518 | prose | pages [26] -->
if mod(i, 13) == 8

<!-- b000519 | prose | pages [26] -->
sdata = data{i, 1}; index = strfind(sdata, ', '); superCharge(count, 1) = str2num(sdata(1:index-1));

<!-- b000520 | prose | pages [26] -->
superCharge(count, 2) = str2num(sdata(index+2:end));

<!-- b000521 | prose | pages [26] -->
superCharge(count, 3) = data{i-1,

<!-- b000522 | prose | pages [26] -->
1};

<!-- b000523 | prose | pages [26] -->
SuperChargeStatus{count, 1} =

<!-- b000524 | prose | pages [26] -->
data{i+2, 1};

<!-- b000525 | prose | pages [26] -->
count = count + 1;

<!-- b000526 | prose | pages [26] -->
end end %% Drawing the data of Super-filling piles in the United States count = 1; superpoint = []; chargeline = []; for i = 1:size(res, 1)

<!-- b000527 | prose | pages [26] -->
if res(i, 3) == 1 && res(i, 5) == 1

<!-- b000528 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000529 | furniture | pages [27] -->
Team#73156

<!-- b000530 | prose | pages [27] -->
superpoint(count).Geometry = 'Point'; superpoint(count).Lon = res(i, 2); superpoint(count).Lat = res(i, 1); superpoint(count).Name = '';

<!-- b000531 | prose | pages [27] -->
count = count + 1;

<!-- b000532 | prose | pages [27] -->
end

<!-- b000533 | prose | pages [27] -->
end

<!-- b000534 | prose | pages [27] -->
for i = 1:size(superCharge, 1)

<!-- b000535 | prose | pages [27] -->
superpoint(count).Geometry = 'Point'; superpoint(count).Lon = superCharge(i, 2); superpoint(count).Lat = superCharge(i, 1); superpoint(count).Name = '';

<!-- b000536 | prose | pages [27] -->
count = count + 1; end

<!-- b000537 | prose | pages [27] -->
figure ax = worldmap('World');

<!-- b000538 | prose | pages [27] -->
ax = worldmap([25, 55], [230, 300]); land = shaperead('landareas', 'UseGeoCoords', true); geoshow(ax, land, 'FaceColor', landcolor) lakes = shaperead('worldlakes',

<!-- b000539 | prose | pages [27] -->
'UseGeoCoords', true); geoshow(lakes, 'FaceColor', lakescolor) states = shaperead('usastatelo', 'UseGeoCoords', true); faceColors = makesymbolspec('Polygon',...

<!-- b000540 | prose | pages [27] -->
{'INDEX', [1 numel(states)], 'FaceColor', ...

<!-- b000541 | prose | pages [27] -->
repmat(landcolor, numel(states), 1)}); geoshow(ax, states, 'DisplayType', 'polygon', ...

<!-- b000542 | prose | pages [27] -->
'SymbolSpec', faceColors) rivers = shaperead('worldrivers', 'UseGeoCoords', true); geoshow(rivers, 'Color', 'blue')

<!-- b000543 | prose | pages [27] -->
count = 1; for i = 1:length(superpoint)

<!-- b000544 | prose | pages [27] -->
count1 = 0; count2 = 0;

<!-- b000545 | prose | pages [27] -->
for j = 1:length(superpoint)

<!-- b000546 | furniture | pages [27] -->
Page 25 of 27

<!-- b000547 | prose | pages [27] -->
dis = calDis(superpoint(i).Lon, superpoint(i).Lat, superpoint(j).Lon, superpoint(j).Lat);

<!-- b000548 | prose | pages [27] -->
if dis <= 170*1.6

<!-- b000549 | prose | pages [27] -->
chargeline(count).Geometry = 'Line';

<!-- b000550 | prose | pages [27] -->
chargeline(count).Lon =

<!-- b000551 | prose | pages [27] -->
[superpoint(i).Lon superpoint(j).Lon NaN];

<!-- b000552 | prose | pages [27] -->
chargeline(count).Lat = [superpoint(i).Lat superpoint(j).Lat NaN];

<!-- b000553 | prose | pages [27] -->
count = count + 1; count1 = count1 + 1; end if dis <= 220*1.6

<!-- b000554 | prose | pages [27] -->
count2 = count2 + 1;

<!-- b000555 | prose | pages [27] -->
end

<!-- b000556 | prose | pages [27] -->
end

<!-- b000557 | prose | pages [27] -->
if count2 ~= 0

<!-- b000558 | prose | pages [27] -->
superrate(i) = count1 / count2; end

<!-- b000559 | prose | pages [27] -->
end

<!-- b000560 | prose | pages [27] -->
geoshow(chargeline, 'Color', 'red', 'LineWidth',1) geoshow(superpoint,'Marker', 'o','MarkerEdgeColor','green', 'MarkerSize', 10, 'MarkerFaceColor','green', 'LineWidth',1.5)

<!-- b000561 | prose | pages [27] -->
superratem = mean(superrate); set(gcf, 'Position', [100, 100, 800, 400]) %% Mapping the trend of Super Quick filling piles in the United States figure datax = 2013:0.5:2018; datay = [7, 10, 63, 126, 308, 417, 556, 639, 767, 873, 1135]; x = 2013:0.01:2018; y=interp1(datax,datay,x,'v5cubic'); hold on xr = 2013 + rand(1, 400) * 5; yr = interp1(datax,datay,xr,'v5cubic'); xp = 2018:0.01:2019;

<!-- b000562 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000563 | furniture | pages [28] -->
Team#73156

<!-- b000564 | prose | pages [28] -->
poly = polyfit(datax, datay, 4); yp = polyval(poly, xp);

<!-- b000565 | prose | pages [28] -->
plot(xp, yp, 'LineWidth',2, 'LineStyle','--

<!-- b000566 | prose | pages [28] -->
','color','g'); plot(x, y, 'r'); set(gca, 'YGrid', 'on') set(gcf, 'Position', [100, 100, 600, 300]) set(gca, 'xtick', 2013:1:2019) xlabel('Years') ylabel('Open Supercharges') legend('Future Supercharges', 'Current Supercharges')

<!-- b000567 | prose | pages [28] -->
scatter(datax, datay, 10, 'filled', 'MarkerFaceColor', 'r'); scatter(xr, yr, 10, 'filled', 'MarkerFaceColor', 'r'); %% Mapping urban traffic in the United States figure ax = worldmap('World'); ax = worldmap([25, 55], [230, 300]); land = shaperead('landareas', 'UseGeoCoords', true); geoshow(ax, land, 'FaceColor', landcolor) states = shaperead('usastatelo', 'UseGeoCoords', true); faceColors = makesymbolspec('Polygon',...

<!-- b000568 | prose | pages [28] -->
{'INDEX', [1 numel(states)], 'FaceColor', ...

<!-- b000569 | prose | pages [28] -->
repmat(landcolor, numel(states), 1)}); geoshow(ax, states, 'DisplayType', 'polygon', ...

<!-- b000570 | prose | pages [28] -->
'SymbolSpec', faceColors) cities = shaperead('worldcities', 'UseGeoCoords', true);

<!-- b000571 | prose | pages [28] -->
count = 1; for i = 1:size(cities)

<!-- b000572 | prose | pages [28] -->
lat = cities(i).Lat; lon = cities(i).Lon; if lat > limit(1) && lat < limit(2) && lon > limit(3) && lon < limit(4)

<!-- b000573 | prose | pages [28] -->
uscities(count) = cities(i);

<!-- b000574 | furniture | pages [28] -->
Page 26 of 27

<!-- b000575 | prose | pages [28] -->
count = count + 1;

<!-- b000576 | prose | pages [28] -->
end

<!-- b000577 | prose | pages [28] -->
end

<!-- b000578 | prose | pages [28] -->
count = 1; cityline = []; for i = 1:size(uscities, 2)

<!-- b000579 | prose | pages [28] -->
temp = randperm(size(uscities, 2)); temp = temp(1:3);

<!-- b000580 | prose | pages [28] -->
for j = 1:size(temp)

<!-- b000581 | prose | pages [28] -->
cityline(count).Geometry = 'Line'; cityline(count).Lon = [uscities(i).Lon uscities(temp).Lon NaN];

<!-- b000582 | prose | pages [28] -->
cityline(count).Lat = [uscities(i).Lat uscities(temp).Lat NaN];

<!-- b000583 | prose | pages [28] -->
count = count + 1; end end cityline(1).Name = '';

<!-- b000584 | prose | pages [28] -->
geoshow(cityline, 'Color', 'red', 'LineWidth',1.5) geoshow(uscities, 'Marker', 'o', 'MarkerEdgeColor', 'black', 'MarkerSize',10, 'LineWidth',1.5, 'MarkerFaceColor', 'red') set(gcf, 'Position', [100, 100, 800, 400]) %% Drawing the percentage chart of Tesla in the United States endyear = 2050; x = 2013:2017; x = [x 2017:0.01:endyear]; y1 = [17.1 29 34 55 87];

<!-- b000585 | prose | pages [28] -->
y2 = [10.3 13.4 15.7 19.4 26.7]; poly1 = polyfit(x(1:5), y1, 6); poly2 = polyfit(x(1:5), y2, 6); yp1 = polyval(poly1, x(6:end)); yp2 = polyval(poly2, x(6:end)); y1 = [y1 yp1];

<!-- b000586 | prose | pages [28] -->
y2 = [y2 yp2]; index = find(x >= 2020); for i = index(1):length(x)

<!-- b000587 | furniture | pages [29] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000588 | furniture | pages [29] -->
Team#73156

<!-- b000589 | prose | pages [29] -->
len = abs(x(i) - x(index(1))); y2(i) = y2(i) - len*len*1.6; y1(i) = y1(i) + len*len*1400;

<!-- b000590 | prose | pages [29] -->
end

<!-- b000591 | prose | pages [29] -->
t = []; for i = index(1):length(x)

<!-- b000592 | prose | pages [29] -->
t(i) = 2020 + 6*(x(i) - 2020);

<!-- b000593 | prose | pages [29] -->
end x(index(1):i) = t(index(1):i); index = find(x >= 2053); [hAx,hLine1,hLine2] = plotyy(x(1:index(1)), y1(1:index(1)), x(1:index(1)), y2(1:index(1))); hLine1.LineWidth = 2;

<!-- b000594 | prose | pages [29] -->
hLine2.LineWidth = 2; hold on

<!-- b000595 | prose | pages [29] -->
legend('U.S. tesla holdings', 'Tesla market share') set(gcf, 'Position', [100, 100, 700, 300]) set(gca, 'YGrid', 'on') ylabel(hAx(1),'Ten Thousand') % left y-axis ylabel(hAx(2),'percentage') % right y-axis

<!-- b000596 | prose | pages [29] -->
ylb = get(hAx(2), 'YTickLabel');

<!-- b000597 | prose | pages [29] -->
for i = 1:size(ylb, 1)

<!-- b000598 | prose | pages [29] -->
ylb{i, 1} = strcat( ylb{i, 1}, '%'); end set(hAx(2), 'YTickLabel',ylb) set(gca, 'xtick', 2013:10:2053) %% Mapping the convenience of the major states figure

<!-- b000599 | prose | pages [29] -->
Logistic model

<!-- b000600 | prose | pages [29] -->
data a; input x1-x7 y@@; cards; ... ;

<!-- b000601 | prose | pages [29] -->
proc logistic descending order=data; model y = x1-x7/scale=none aggregate; run;

<!-- b000602 | furniture | pages [29] -->
Page 27 of 27

<!-- b000603 | prose | pages [29] -->
load index1 load index2 load indexdouble color1 = [94 141 193]./255;

<!-- b000604 | prose | pages [29] -->
color2 = [201 221 241]./255; ax = worldmap('World'); ax = worldmap([25, 55], [230, 300]);

<!-- b000605 | prose | pages [29] -->
land = shaperead('landareas', 'UseGeoCoords', true); geoshow(ax, land, 'FaceColor', landcolor) states = shaperead('usastatelo', 'UseGeoCoords', true);

<!-- b000606 | prose | pages [29] -->
for i = 1:length(index22)

<!-- b000607 | prose | pages [29] -->
scolor(index22(i), :) = color2;

<!-- b000608 | prose | pages [29] -->
end for i = 1:length(index11)

<!-- b000609 | prose | pages [29] -->
scolor(index11(i), :) = color1; end faceColors = makesymbolspec('Polygon',...

<!-- b000610 | prose | pages [29] -->
{'INDEX', [1 numel(states)], 'FaceColor', ...

<!-- b000611 | prose | pages [29] -->
scolor}); geoshow(ax, states, 'DisplayType', 'polygon', ...

<!-- b000612 | prose | pages [29] -->
'SymbolSpec', faceColors) cities = shaperead('worldcities', 'UseGeoCoords', true); set(gcf, 'Position', [100, 100, 800, 400])
