# P-D-2018-81402-e1ca1921

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
81402

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
D

<!-- b000014 | prose | pages [1] -->
T4

<!-- b000015 | prose | pages [1] -->
F4

<!-- b000016 | prose | pages [1] -->
2018 MCM/ICM

<!-- b000017 | heading | pages [1] -->
Summary Sheet

<!-- b000018 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000019 | prose | pages [1] -->
Forecast, Blueprint, Strategy, for EV's Future

<!-- b000020 | prose | pages [1] -->
Since 21th century, electric vehicles(EV) has grown from a sprout in vehicles industries as for its environmental benefits. Many people wonder that if one day electric vehicles could replace fuel vehicles completely. Considering the inconvenience of charging, a critical problem of electric vehicles is about the charging system construction.

<!-- b000021 | prose | pages [1] -->
To maximize profit and minimize cost, the EV industries are overcoming three facets: 1) the mapping distribution of a specific area; 2) a time-domain evolution model for market prediction/forecast; 3) A standard classification of worldwide marketing. To reduce the Carbon Dioxide pollution, the government also concerns about the policy design for EV market.

<!-- b000022 | prose | pages [1] -->
In this essay, we will start from an approach to the charger location and allocation problem, and then dig deep into the forecast of EV market in different countries. To solve 5 tasks, we proposed several models in the cross-science of Network Science, Operations Research, Economics, Statistics, Environmental Science, Graph Theory, Cybernetics and Game Theory.

<!-- b000023 | prose | pages [1] -->
For task 1), we first took a data pre-processing, transforming address/zip code to Geodetic Coordinate System. We aim to make an approach to the maximum coverage problem. We defined 892 supercharger locations, 3,048 charger locations and 492 urban cities/clusters as “nodes”. For the simplicity, an undirected graph model representing the whole charging network was established, in which every node denotes a potential position for building chargers. After the graph was connected, we applied SPFA algorithm to calculate the Shortest Path among each nodes pairs. We also developed a Demand Estimation Model to generalize Average Miles Driven data and Urbanization data, and proposed the demand of each node respectively. To obtain a best charger allocation scheme, we constructed a Linear Programming model, which could be not solved in affordable time. To reduce the computational complexity, we converted it into an equivalent

<!-- b000024 | heading | pages [1] -->
Minimum Cost Max-flow Network model. We showed our location and allocation results

<!-- b000025 | prose | pages [1] -->
in maps, graphs, contours and major city lists, respectively for U.S. and South Korea. For task 2b), we applied a Most Profit model based on Nash Equilibrium, to find the optimal strategy in a “chicken or the egg causality dilemma”: chargers lead vehicles market, or vehicles market lead chargers? For the former situation, we introduced a systematic dynamic model to demonstrate the process by cybernetics concepts; For the latter situation, we introduced a Market Evolution Model based on Bass Diffusion Model, to achieve a better understanding of high technology products’ adoption in economics. For task 2c), We proposed Bass Diffusion Model based on data analysis, predicted the market adopted timeline from a blank market. For task 3), we discussed the feasibility of our previous model, and proposed a Linear Regression Model to calculate the weight of each factors contributed to future EV industry evolution, i.e. GDP per Capita, PPI, Oil price, etc. For task 4), we proposed our perspective for high technology adoption in the future. For task 5), we proposed our hand out to decision makers in governments, briefly stating our results in EV market promotion.

<!-- b000026 | prose | pages [1] -->
Our work has many strengths and weaknesses. Our strengths were performed in interdisciplinary views, coding and mathematic skills, economics views and social responsibilities; our weakness were performed in the lack of sensitivity modification, and

<!-- b000027 | furniture | pages [2] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000028 | prose | pages [2] -->
the quantitative derivation of system dynamic model in investments.

<!-- b000029 | furniture | pages [3] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000030 | heading | pages [3] -->
Contents

<!-- b000031 | contents | pages [3] -->
1

<!-- b000032 | heading | pages [3] -->
Introduction

<!-- b000033 | prose | pages [3] -->
2

<!-- b000034 | heading | pages [3] -->
Modeling

<!-- b000035 | prose | pages [3] -->
2

<!-- b000036 | prose | pages [3] -->
2 Outline...........................................................................................................................2 2.1 Assumptions.................................................................................................................3 2.2 Location & Allocation Optimization Model............................................................ 3 2.3 Demand Estimation Model........................................................................................ 5 2.4 Shortest Path Model.................................................................................................... 6 2.5 Best Profit Strategy Model..........................................................................................7 2.6 Market Evolution Model............................................................................................ 8 2.7 Classification of Promoting EVs................................................................................9 2.8

<!-- b000037 | prose | pages [3] -->
3 Dataset & Toolkit

<!-- b000038 | prose | pages [3] -->
4

<!-- b000039 | heading | pages [3] -->
Results and Analysis

<!-- b000040 | prose | pages [3] -->
10

<!-- b000041 | prose | pages [3] -->
10 Task 1........................................................................................................................... 10 4.1 Task 2........................................................................................................................... 12 4.2 Task 2a............................................................................................................ 12 4.2.1 Task 2b............................................................................................................ 15 4.2.2 Task 2c.............................................................................................................16 4.2.3 Task 3........................................................................................................................... 17 4.3 Task 4........................................................................................................................... 18 4.4 Handout......................................................................................................................20 4.5

<!-- b000042 | heading | pages [3] -->
Appendices

<!-- b000043 | heading | pages [3] -->
Appendix A Code

<!-- b000044 | prose | pages [3] -->
22

<!-- b000045 | prose | pages [3] -->
22

<!-- b000046 | prose | pages [3] -->
1 1

<!-- b000047 | furniture | pages [4] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000048 | furniture | pages [4] -->
Team # 81402

<!-- b000049 | furniture | pages [4] -->
Page 2 of 27

<!-- b000050 | prose | pages [4] -->
1

<!-- b000051 | heading | pages [4] -->
Introduction

<!-- b000052 | prose | pages [4] -->
Having seen the environmental situation (greenhouse effect, etc.), an alternativeenergy to replace fossil fuels in vehicles industry is now becoming a hot issue. With the rapid technology development of electric vehicles and the encouragement of policies coopera- tion on international negotiations, electric vehicles(EV) is now a fashion in both labora- tory and commerce.

<!-- b000053 | prose | pages [4] -->
Since 2012, Tesla Corporation is standing out as a leading peer in electric vehicles in- dustries. Tesla improves its R & D investment, resulting in a solid foundation of electric vehicle engine and energy storage technology. It results in the excellent performance of sales in many products, such as Model S and Model X.

<!-- b000054 | prose | pages [4] -->
The power supply and charging networks are essential infrastructures in electric ve- hicles industry. Problem D in ICM 2018 provided a chance to see the insight of these infrastructures. By analyzing and predicting its consuming trend and the location of charging piles, it may be a good perspective for us to understand the expecting future.

<!-- b000055 | prose | pages [4] -->
2

<!-- b000056 | heading | pages [4] -->
Modeling

<!-- b000057 | prose | pages [4] -->
2.1 Outline

<!-- b000058 | prose | pages [4] -->
Tomaximize profit and minimize cost, the EV industries are overcoming three facets: 1) the mapping distribution of a specific area; 2) a time-domain evolution model for market prediction/forecast; 3) A standard classification of worldwidemarketing.

<!-- b000059 | prose | pages [4] -->
For the mapping chargers design, it includes: 1a) the calculation of demand chargers in numbers, according to Population, Urbanization, Household travel willingness, etc; 1b)the optimization of chargers design: sizing and placing.

<!-- b000060 | prose | pages [4] -->
1b) is a critical problem. The location of EV chargers should be both easily accessi- ble and widely spread. Hence, EVs can be charged easily in "neighborhood" for regular business/school/church, etc., and also able to cruise around a larger area upon being re-charged for long distance trips.(Lam et. al, 2014)[9] The ultimate goal to maximize the efficiency of chargers and the coverage of charging system.

<!-- b000061 | prose | pages [4] -->
Green energy industries like Tesla Corp. has been scheduling a long-term market- ing and planning blueprint to switch U.S./the world to an all electric vehicles society. This blueprint requires a systematic dynamic model to forecast the market evolution in the following decades. To expand Tesla Corp.’s global market, decision makers would run into a “chicken or the egg causality dilemma": 2a) Let chargers stimulate vehicles sales, or 2b), vehicles sales promote the charger system construction? This game theory problem would introduce two different marketing prediction and strategies.

<!-- b000062 | prose | pages [4] -->
Tosolve tasks stated in ICM 2018 Problem D, we apply multiple mathematical model- ing methods in the cross-science of Operation Researches, Network Sciences, Economics, Game Theory, Geography, Graph Theory, etc.

<!-- b000063 | prose | pages [4] -->
For facet 1), the mapping distribution of a specific area, the bottleneck is how to opti- mize the distribution under a certain charging demand.

<!-- b000064 | prose | pages [4] -->
It indicates a famous prob- lem in applied mathematics, Maximum Coverage Problem(or, Maximum Coverage Lo- cation Problem, Church & Revelle, 1974)[3]. We established a Linear Programming

<!-- b000065 | heading | pages [4] -->
Model(MLP Model, Hiller, 2012)[8] to solve this problem. To reduce the computational

<!-- b000066 | prose | pages [4] -->
complexity,we converted it into an equivalent Minimum CostMax-flowNetwork model.

<!-- b000067 | furniture | pages [5] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000068 | furniture | pages [5] -->
Team # 81402

<!-- b000069 | furniture | pages [5] -->
Page 3 of 27

<!-- b000070 | prose | pages [5] -->
In our MLP model, two parameters needed to be modified: i) the shortest path between two nodes; ii) the charging demand of each node. To find parameter i), we

<!-- b000071 | heading | pages [5] -->
developed a Shortest Path Model(Dijkstra, 1959)[5]. All the address/zip codes data

<!-- b000072 | prose | pages [5] -->
from Tesla.com were extracted, and transformed into Geodetic Coordinate Format. Af- ter pre-processing, we applied all the location data of existing chargers, superchargers, and largest 497 cities/clusters (definition of Urban, U.S. Census Bureau, 2010)[18][19] in U.S. to draw a graph. We identified that the current construction of Tesla chargers and superchargers is able to link 497 cities/clusters. Tomodify parameter ii), we introduced a Demand Estimation Model in a macro scope via statistics from geography, i.e. pop- ulation, urbanization, highway miles, etc. We calculate the demand per node(city) (di below) by Average Miles Driven per year by state (AMD)[17] and Urbanization Statis- tics, in urban, suburban and rural areas respectively.

<!-- b000073 | prose | pages [5] -->
For facet 2), the time-domain market evolution model, we need to clarify the difficultyof making a decision on which is the leading factor - between constructing charging piles and constructing EVs. For decision makers, we introduce a game theory model Best Profit Strategy Model - to find the optimal strategy.

<!-- b000074 | prose | pages [5] -->
For the case 2a), we introduced a Systematic Dynamic model, but not a quantitative one. we didn’t include this part in our Modeling section, only in the tasks.

<!-- b000075 | prose | pages [5] -->
For the case 2b), we proposed a Market Prediction Model - Bass diffusion model (Norton & Bass, 1987)[11] to estimate the future occupancy of future EV market. Bass diffusion model demonstrate how a high technology product run into the market and ultimately replace the old generation of products. Applying Tesla sales data and Korea EV sales data, Bass Diffusion Model performs well in our data fitting.

<!-- b000076 | prose | pages [5] -->
For facet 3), the standard classification of worldwide marketing, we promote a classifica- tion sample by Linear Regression.

<!-- b000077 | prose | pages [5] -->
2.2

<!-- b000078 | heading | pages [5] -->
Assumptions

<!-- b000079 | prose | pages [5] -->
In this model, the following items are out of our work scope: 1a) altitude of each cities/n- odes in calculating distances inshortest pathmodel; 1b) traffic jams; 1c)charging blueprint of Alaska and Hawaii, and Puerto Rico; 1d) the growth of the demand, in task 1;1e)home charging.

<!-- b000080 | prose | pages [5] -->
For the simplicity, we also simplify the following items in our modeling: 2a) We define geographical design of "urban" and "suburban" as a circle zone. Their area are extracted from Land Area in Urban areas of the United States of America (U.S. Census Bureau, 2010)[18][19].; 2b) The earth radius was set by 6,378 kilometers; 2c) We use su- perchargers construction to replace chargers in our blueprint(as superchargers are more efficient).

<!-- b000081 | prose | pages [5] -->
Other assumptions mention in a single task/model are also valid.

<!-- b000082 | prose | pages [5] -->
2.3

<!-- b000083 | heading | pages [5] -->
Location & Allocation Optimization Model

<!-- b000084 | heading | pages [5] -->
Tosolve the Maximal Coverage Problem, we developed a Linear Programming model to

<!-- b000085 | prose | pages [5] -->
find the maximal coverage solution in station location problem. We didn’t consider the capacity difference between a charger and a supercharger primarily; for an optimized blueprint in a large scale, we first regard them as "nodes", which means that we attach more importance to the location.

<!-- b000086 | prose | pages [5] -->
Objective Function:

<!-- b000087 | furniture | pages [6] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000088 | furniture | pages [6] -->
Team # 81402

<!-- b000089 | furniture | pages [6] -->
Page 4 of 27

<!-- b000090 | prose | pages [6] -->
∑∑

<!-- b000091 | prose | pages [6] -->
i∈V j∈V

<!-- b000092 | prose | pages [6] -->
minyij,ci, yijd(i, j) (1)

<!-- b000093 | prose | pages [6] -->
∀i ∈V, ∀j ∈V, yij ⩾0

<!-- b000094 | prose | pages [6] -->
subjected to

<!-- b000095 | prose | pages [6] -->
∑

<!-- b000096 | prose | pages [6] -->
∀i ∈V, j∈V

<!-- b000097 | prose | pages [6] -->
∑

<!-- b000098 | prose | pages [6] -->
∀i ∈V,

<!-- b000099 | prose | pages [6] -->
(2)

<!-- b000100 | prose | pages [6] -->
yij ⩾di (3)

<!-- b000101 | prose | pages [6] -->
yij ⩾αdi (4)

<!-- b000102 | prose | pages [6] -->
j∈V ∧dist(i,j)⩾minD

<!-- b000103 | prose | pages [6] -->
∀i ∈V, ci ⩾0

<!-- b000104 | prose | pages [6] -->
∑

<!-- b000105 | prose | pages [6] -->
∀j ∈V, i∈V

<!-- b000106 | prose | pages [6] -->
(5)

<!-- b000107 | prose | pages [6] -->
yij ⩽cj (6)

<!-- b000108 | prose | pages [6] -->
∀j ∈V, ci ⩽max C (7)

<!-- b000109 | prose | pages [6] -->
α: A Dimensionless Coefficient of long distance traveling. For example, αdi means Charging multiple alternatively. It demonstrate the charging demand of node i which has to be contributed by the "distant" nodes.

<!-- b000110 | prose | pages [6] -->
The neighborhood nodes is defined by a distance radius min D. We implement this to cases where people have long distance travel demands, they need to charge in another city.

<!-- b000111 | prose | pages [6] -->
maxC: A parameter. The Maximum charger capacity of a single node, depending on the charge technique.

<!-- b000112 | prose | pages [6] -->
Nevertheless, since there are more than V 2 variables in the above linear program-

<!-- b000113 | prose | pages [6] -->
| |

<!-- b000114 | prose | pages [6] -->
ming model, it is difficult to solve this large-scale LP model using standard algorithms like Simplex. Thus, the LP model is converted into an equivalent minimum cost max- flow model as follows.

<!-- b000115 | prose | pages [6] -->
• Assume that the source and sink of the network flow model is, respectively, Sand T;

<!-- b000116 | furniture | pages [7] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000117 | furniture | pages [7] -->
Team # 81402

<!-- b000118 | furniture | pages [7] -->
Page 5 of 27

<!-- b000119 | prose | pages [7] -->
2.4

<!-- b000120 | heading | pages [7] -->
Demand Estimation Model

<!-- b000121 | prose | pages [7] -->
The charging demand is also a complicated issue to be solved. Everyday, people travel back and forth, contributing the demand of each charger. Previous researches have pro- posed the (daytime, nighttime) demand of each community in a city by Linear Regres- sion, where various factors have been taken into consideration: neighborhood, popula- tion, community social structure, household traveling willingness, employment, daily activities, etc.(Chen et al., 2013;Frade et al.,2011)[2][7] Such estimations are feasible in a relative small scale, like Lisbon and Seattle in the literature. For such a large scale of United States, it would occur a large computational complexity if we divide the whole country into communities and apply linear regression to calculate the weight of each factors. Hence we only consider the impact factors in a macro scope, i.e. population and land area of cities (also called, urbanization), Average Miles Driven per year by state (AMD)[17].

<!-- b000122 | prose | pages [7] -->
We prepared a parsimonious estimation with the following model setting: a) We di- vide AMD data to urban, suburban and rural respectively. A vague definition of "sub- urban" were introduced. b) We regard a city (among 497 cities/clusters) as a node. The urban demand was contributed by its own population and its share of AMD. The urban share of AMD corresponds to inter-city traveling (employment, school, church, etc.) c) The demand of rural area was shared by the remained AMD per area. Considered the subnational travel, we distribute this demand equally to states. d) A definition of urban, suburban and rural should be clarified. Urban areas of the United States of America(U.S.

<!-- b000123 | furniture | pages [8] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000124 | furniture | pages [8] -->
Team # 81402

<!-- b000125 | furniture | pages [8] -->
Page 6 of 27

<!-- b000126 | prose | pages [8] -->
Census Bureau, 2010) [18][19] only defined “urban" in a broad sense: Urban included all population in urbanized areas and urban clusters (each with their own population size and density thresholds). This definition includes both urban and suburban. It has al- ways been an issue to clarify the geographic definition of urban suburban areas, in a narrow sense, we define urban as a node on the map and suburban as the cities’ large land area proposed in Urban areas of the United States of America data. For population distribution, we distribute 26% in urban, 53% in suburban, and 21% in rural.[22] e) We only considered the current population, demand, etc. The ultimate goal is to change the whole vehicles industry to an all-electric one. The aim of replacing fuel energy vehicles weights more than calculate the growth of vehicles. We didn’t propose a dynamic sys- tem, for task 1.

<!-- b000127 | prose | pages [8] -->
The notations reads i: node; j: state; R: rural area; SU :suburban area; U : urban area; di: demand per node; DR: demand except urban area; Pc: population of a city; Ps: populationofastate; mj: AMDwherethecitylocates;S: landareaofU.S.;ϵ: aparameter

<!-- b000128 | prose | pages [8] -->
∈

<!-- b000129 | prose | pages [8] -->
to adjust demand weight by the nodes density in an area; center(i): i SU , center(i) is

<!-- b000130 | prose | pages [8] -->
∈

<!-- b000131 | prose | pages [8] -->
the center city that suburban node i belongs to; size(i): i U, the number of suburban cities belonging to city i;.

<!-- b000132 | prose | pages [8] -->
2.5

<!-- b000133 | heading | pages [8] -->
Shortest Path Model

<!-- b000134 | prose | pages [8] -->
To run the Linear Programming model, the shortest path d(i, j) need to be calculated. We could simply tackle the problem employing a iterative algorithm(Dijkstra, 1959)[5]. This problem sets reads the tree of minimum total length between n nodes, and the path of minimum total length between two given nodes P and Q(Dijkstra, 1959)[5].

<!-- b000135 | prose | pages [8] -->
Our model setting aims to construct a graph connecting all nodes. Primary nodes were set by all the current superchargers in U.S. (892 nodes), chargers in U.S. (3,048 nodes) and 497 cities/clusters mentioned above. In total, we set 4,295 nodes covering 48 states and Washington D.C. in U.S.(Alaska, Hawaii and Puerto Rico are exceptions.)

<!-- b000136 | prose | pages [8] -->
A data pre-processing was applied as all the raw location data were performed in ad- dress/zip code format. In order to calculate the path, we applied a Google Geocode API[20] to transform the raw data into Geodetic Coordinate System(latitude, longitude). Hence, the shortest path could be calculated via distance calculation on a spherical sur- face. The earth radius was set by 6,378 kilometers for the simplicity. We here propose a general nodes map of applied nodes (figure1)

<!-- b000137 | prose | pages [8] -->
To reduce the calculation complexity, we apply the SPFA Algorithm (Duan, 1994)[6] to optimize shortest path calculation based on queue.

<!-- b000138 | furniture | pages [9] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000139 | furniture | pages [9] -->
Team # 81402

<!-- b000140 | furniture | pages [9] -->
Page 7 of 27

<!-- b000141 | caption | pages [9] -->
Figure 1: All nodes (superchargers, chargers and cities inclueded)

<!-- b000142 | caption | pages [9] -->
Figure 2: Nodes around Salt-Lake City

<!-- b000143 | prose | pages [9] -->
2.6

<!-- b000144 | heading | pages [9] -->
Best Profit Strategy Model

<!-- b000145 | prose | pages [9] -->
Marketing strategies should change dynamically regarding the development of EV tech- nology, the ability of charging piles (the charge of piles and how long can it add charge) and the instant international trade accumulating the acceleration of EV and charging piles.

<!-- b000146 | prose | pages [9] -->
We need to do is find the best profit between two situations : more EV and more charging piles. Between the two classifications, there are a best expectation that would happen so that we can get the most profit. We introduce a Best Profit Strategy Model based a Nash Equilibrium(Nash, 1951)[10] in Game Theory.

<!-- b000147 | prose | pages [9] -->
A plan needed to be drew, to predict a pattern in order to decide what we should weight more between constructing EV and constructing charging piles. Notations needs to be emphasized below:

<!-- b000148 | prose | pages [9] -->
P : the ratio of charging piles to EV;

<!-- b000149 | furniture | pages [10] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000150 | furniture | pages [10] -->
Team # 81402

<!-- b000151 | furniture | pages [10] -->
Page 8 of 27

<!-- b000152 | prose | pages [10] -->
P0: the standard ratio of charging piles to EV; Pc: the ratio of charging piles to standard charging piles; Pe: the ratio of EV to standard EV;

<!-- b000153 | prose | pages [10] -->
Hence we can write the following a game theory model, see table1 and 2. EX1 and

<!-- b000154 | prose | pages [10] -->
EX10 hold the same formulation, with different notations for probabilities.

<!-- b000155 | prose | pages [10] -->
This is a simple game theory model describing the optimal strategy. The meaning of the optimal strategy in which we choose is the representation of the relative degree of data. What we need to do is find a formal formula to correctly describe the data of the standard chargers and P0;

<!-- b000156 | prose | pages [10] -->
In order to maximize the interests, one should be in a positive or negative situation when our earnings are equal (or in this game, each other can change both the front and the probability that our expected revenue), so that we know that:

<!-- b000157 | prose | pages [10] -->
EX40 −EX20 P =

<!-- b000158 | prose | pages [10] -->
(17)

<!-- b000159 | prose | pages [10] -->
EX10 −EX20 −EX30 + EX40

<!-- b000160 | prose | pages [10] -->
e

<!-- b000161 | prose | pages [10] -->
Hence, the future strategy would made based on this model.

<!-- b000162 | prose | pages [10] -->
2.7

<!-- b000163 | heading | pages [10] -->
Market Evolution Model

<!-- b000164 | prose | pages [10] -->
To see the marketing performance of "chargers in response to car purchases", a fore- casting model is required to explain systematic dynamic market evolution of Electric Vehicles.

<!-- b000165 | caption | pages [10] -->
Table 1: Nash Equilibrium Model for chargers

<!-- b000166 | prose | pages [10] -->
P < P0 P > P0 Chargers EX1 Pc < 1 Pc > 1 EV EX2 EV EX3 Chargers EX4

<!-- b000167 | caption | pages [10] -->
Table 2: Nash Equilibrium Model for EVs

<!-- b000168 | prose | pages [10] -->
P < P0 P > P0 Chargers EX10 Pe < 1 EV EX20 Pe > 1 EV EX30 Chargers EX40

<!-- b000169 | furniture | pages [11] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000170 | furniture | pages [11] -->
Team # 81402

<!-- b000171 | furniture | pages [11] -->
Page 9 of 27

<!-- b000172 | prose | pages [11] -->
We intuitively notice the development of high technology products as a simple pos- itive feedback process. Such an explosive trend is unfeasible in fitting a linear model. Particularly, in United States, the growth economics index(e.g.GDP per capita, house- hold income) and population tend to be moderate. Thus, a linear regression cannot explain the boost or the expected boost in Electric Vehicles industry. However, anexpo- nential increase in the positive feedback is explosive. Comparing with the analogywith species reproduction in ecology, an exponential model ignores the limited antecedents of the environmental resources we live in. We also notice that although it is not completely identical, in some situations the model does reflect well at some point in time.

<!-- b000173 | prose | pages [11] -->
Although the initial assumption says that exponential growth is occurring in the same period, we can adjust the model by modifying the multiple of the exponential growth to avoid the blow up. By showing that growth multiples are affected by certain factors, such factors become the core of this model.

<!-- b000174 | prose | pages [11] -->
We here apply Bass diffusion model(Norton & Bass, 1987)[11] to estimate the future occupancy of the charging pile through the number of tesla electric cars. This model tends to form an s-shaped curve in the transition from positive feedback to negative feedback.

<!-- b000175 | prose | pages [11] -->
When considering the impact of multivariate factors on the problem, the logistic model reflects its key significance, which is also used by us in predicting the future trend of electric vehicles and the adding number of charging piles.

<!-- b000176 | prose | pages [11] -->
Bass Diffusion Model says that,

<!-- b000177 | prose | pages [11] -->
f(t)/[1 −F(t)] = p + qF(t).

<!-- b000178 | prose | pages [11] -->
(18)

<!-- b000179 | prose | pages [11] -->
It explains the if f (t) is defined as the probability of adoption at time t, (neglecting the hazard function), F(t) is the fraction of the ultimate potential has adopted by time t. p and q are parameters, respectively, the coefficient of innovation and the coefficient of imitation.

<!-- b000180 | prose | pages [11] -->
To solve this differential equation, an initial condition could be added as a zeroth point,F(0) = 0. Thus we will get the solution of F(t) and f(t):

<!-- b000181 | prose | pages [11] -->
F(t) = [1 −exp(−bt)]/[1 + aexp(−bt)] (19) f(t) = (b2/p)exp(−bt)/[1 + aexp(−bt)]2 (20)

<!-- b000182 | prose | pages [11] -->
where a = q/p and b = p + q. The peak of f(t) occurs at t∗= (1/b)ln(a). This differential equation could be solved numerically. In this essay, we will propose the market evolution of America and South Korea by fitting the existing sales data into Bass diffusion model.

<!-- b000183 | prose | pages [11] -->
2.8 Classification of Promoting EVs

<!-- b000184 | prose | pages [11] -->
When talking about the classification system, we need to think about such a question: how these factors affect the selection of different approaches to growing the network and how much? Maybe different countries have different situations and therefore selecting the factors seems important.

<!-- b000185 | prose | pages [11] -->
There are so many countries such as America, United Kingdom, China, Japan, South Korea and other countries and there are many factors, for instance, GDP, Engels coeffi- cient, degree of industrialization and agriculture, the degree of traffic network develop- ment, and so on.

<!-- b000186 | furniture | pages [12] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000187 | furniture | pages [12] -->
Team # 81402

<!-- b000188 | furniture | pages [12] -->
Page 10 of 27

<!-- b000189 | prose | pages [12] -->
Among these factors, some are possibly interacted and associated. What we might think most is find a master-slave relationship among these factors. However, in this model setting, we need to notice some important factors that we cannot ignore as there are some essential small factors such as the degree of electricity, industrialization and transportation. These may be a branch of some data such as GDP or PPI, but they are the same important.

<!-- b000190 | prose | pages [12] -->
Now we can set a function to mainly describe some necessary index. The Multiple Linear Regression formula reads:

<!-- b000191 | prose | pages [12] -->
a1 ttDP0 + a2 PPI

<!-- b000192 | prose | pages [12] -->
RN0 + a5 V PC

<!-- b000193 | prose | pages [12] -->
PPI0 + a3 ttI

<!-- b000194 | prose | pages [12] -->
ttI0 + a4 RN

<!-- b000195 | prose | pages [12] -->
ttDP

<!-- b000196 | prose | pages [12] -->
V PC0 + a6 OP

<!-- b000197 | prose | pages [12] -->
OP0 + a7 UB

<!-- b000198 | prose | pages [12] -->
UB0 = 1 (21)

<!-- b000199 | prose | pages [12] -->
Our notation reads: ttDP: Gross Domestic Product per Capita; PPI: Producer Price Index;ttI:GiniCoefficients;RN:Roadnetworktotalmiles;VPC: VehiclesperCapita(1000 people); OP : Oil Price; UB:Urbanization.

<!-- b000200 | prose | pages [12] -->
The EV weight were replaced by V PC and OP in our model as many countries haven’t promote EV.

<!-- b000201 | prose | pages [12] -->
3 Dataset & Toolkit

<!-- b000202 | prose | pages [12] -->
We have applied the following dataset and toolkit:

<!-- b000203 | prose | pages [12] -->
• For original Tesla chargers and superchargers, we applied address/zip code from official website[4] [14].

<!-- b000204 | prose | pages [12] -->
• For Shortest Path Model, we transformed address/zip code to Geodetic Coordinate System, and applied Google Geocode API[20]. We also used the Korea cities data to get latitudes and longitudes of Korea cities.[25]

<!-- b000205 | prose | pages [12] -->
• For Demand Estimation Model, we applied Average Miles Driven per year by state (AMD) [17],Urban areas of the United States of America(U.S. Census Bureau, 2010) [18][19].

<!-- b000206 | prose | pages [12] -->
• For Location & Allocation Optimization Model, we applied Google Costflow Toolkit to optimize Linear Programming calculation[21].

<!-- b000207 | prose | pages [12] -->
• For Market Evolution Model/Bass Diffusion Model, we referred the Tesla sales data[15][12] in America and EV sales data in South Korea[13][16] to predict the dynamic evolution of Tesla market.

<!-- b000208 | prose | pages [12] -->
• For classification between countries, we applied global data of GDP[27], PPI[29], GI[23], Road Network[24], Urbanization[30], OilPrice[26]andVehiclesperCapita[28].

<!-- b000209 | prose | pages [12] -->
4

<!-- b000210 | heading | pages [12] -->
Results and Analysis

<!-- b000211 | prose | pages [12] -->
4.1 Task 1

<!-- b000212 | prose | pages [12] -->
Our Simulation including 4,297 nodes have proposed a possible blueprint for Tesla’s charger construction. We suppose that the superchargers would replace the chargers

<!-- b000213 | furniture | pages [13] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000214 | furniture | pages [13] -->
Team # 81402

<!-- b000215 | furniture | pages [13] -->
Page 11 of 27

<!-- b000216 | prose | pages [13] -->
due to the advantages in charging power. For our distribution, allocation and capacity blueprint we only consider the superchargers.

<!-- b000217 | prose | pages [13] -->
Our Shortest Path Model demonstrate that all the chargers, superchargers and cities arefullyconnected.Parametermind=170(miles)accordingtothechargingcapacityof 30minutesinTeslasupercharger. Indeed,Teslaisontracktoallowacomplete switch to all-electric in the US. It might take a few decades to accomplish a complete switch, but Tesla is trying to draw theblueprint.

<!-- b000218 | prose | pages [13] -->
Our Demand Estimation Model provides a demand(in miles unit) for each node. We classified the demand of urban areas, suburban areas and rural areas respectively,and derivedparameterα = 0.25whichcouldbefittedintheweightofdistantmultiplealter- native charging. We set the parameters maxc = 50000(the upper limit superchargers for a node).

<!-- b000219 | prose | pages [13] -->
Our Location & Allocation Optimization Model provides a forecast of an all-electric U.S. It would require 873,869 to cover an all-electric U.S. The charger connections can be seen in Figure 4. An interesting thing occurred in our simulation: the current super- charger nodes would remain active, but most of the charger nodes are eliminated for the performance.

<!-- b000220 | prose | pages [13] -->
For the Allocation of chargers, the distribution map can be seen in Figure 3. Wealso print the superchargers design of 12 Cities/Clusters with largest population, in Table3. A contour figure are shown in Figure 5

<!-- b000221 | prose | pages [13] -->
We propose the urban, suburban and rural distribution of superchargers in Table 4.

<!-- b000222 | caption | pages [13] -->
Figure 3: Charger Distribution in U.S.

<!-- b000223 | furniture | pages [14] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000224 | furniture | pages [14] -->
Team # 81402

<!-- b000225 | furniture | pages [14] -->
Page 12 of 27

<!-- b000226 | caption | pages [14] -->
Figure 4: Charger Connections in U.S.

<!-- b000227 | caption | pages [14] -->
Figure 5: Chargers Distribution Contour Figure in U.S.

<!-- b000228 | prose | pages [14] -->
4.2 Task 2

<!-- b000229 | prose | pages [14] -->
4.2.1 Task 2a

<!-- b000230 | prose | pages [14] -->
Based on the models applied in task 1, we drew a graph of 135 Korea’s main cities[25]. Then we created a location and allocation blueprint if we replace Korea’s current vehicles to EVs.

<!-- b000231 | prose | pages [14] -->
Due to the lack of data, we calculated the demand of each node by the following estimation:

<!-- b000232 | prose | pages [14] -->
vehicles per capita of South Korea

<!-- b000233 | prose | pages [14] -->
di = di in U.S. ×

<!-- b000234 | prose | pages [14] -->
(22) vehicles per capita of U.S.

<!-- b000235 | furniture | pages [15] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000236 | furniture | pages [15] -->
Team # 81402

<!-- b000237 | furniture | pages [15] -->
Page 13 of 27

<!-- b000238 | caption | pages [15] -->
Table 3: Superchargers design of 12 Main Cities/Clusters

<!-- b000239 | prose | pages [15] -->
Location New York-Newark Los Angeles-Long Beach-Anaheim Chicago Miami Dallas-Fort Worth-Arlington Washington D.C.

<!-- b000240 | prose | pages [15] -->
Numbers Location Numbers 11667 Philadelphia 3634 8289 Huston 9609 5730 Atalanta 9680 6823 Detroit 3991 3798 Boston 2893 2715 Phoenix-Mesa 2342

<!-- b000241 | caption | pages [15] -->
Table 4: Charger Distribution Planning in Urban, Suburban andRural

<!-- b000242 | prose | pages [15] -->
Geography Urban Proportion 40.25% Suburban Rural 25.38% 34.36%

<!-- b000243 | prose | pages [15] -->
Our calculations showed that 56,953 superchargers required to be constructed in South Korea. Figure 6 shows the predicted superchargers location in South Korea. Fig- ure 7 shows the predicted superchargers distribution in South Korea. Similar to U.S., South Korea has well-constructed road, vehicles culture, high household income, and urbanization degree. Their difference mainly includes geography (land area, cities’net- work, population, etc.) Based on our model, key factors that shaped the development could be: geographic cities/road network, population and urbanization. From this per- spective, South Korea could be considered as a large land area of U.S., like Northeast.

<!-- b000244 | caption | pages [15] -->
Figure 6: Charger Connections in South Korea

<!-- b000245 | furniture | pages [16] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000246 | furniture | pages [16] -->
Team # 81402

<!-- b000247 | furniture | pages [16] -->
Page 14 of 27

<!-- b000248 | caption | pages [16] -->
Figure 7: Charger Distribution in South Korea

<!-- b000249 | caption | pages [16] -->
Figure 8: Chargers Distribution Contour Figure in South Korea

<!-- b000250 | furniture | pages [17] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000251 | furniture | pages [17] -->
Team # 81402

<!-- b000252 | prose | pages [17] -->
Location Seoul Pusan Numbers 11153 3777

<!-- b000253 | furniture | pages [17] -->
Page 15 of 27

<!-- b000254 | prose | pages [17] -->
Taegu Inch’on Taejon 2597 2479 1774 Sungnam Location Kwangju Numbers 1602 1264 Puch’n Suwon Ulsan 1147 1112 918

<!-- b000255 | caption | pages [17] -->
Table 5: Number of Chargers in 10 Major South Korean Cities

<!-- b000256 | prose | pages [17] -->
4.2.2 Task 2b

<!-- b000257 | prose | pages [17] -->
Speaking of investment to a blank market, we will propose several investment strategy. It always runs into a dilemma. We need chargers to make people who purchased EV more convenient; but the original market laws based on the technology promotion and lever principle are also important. Or we can say, both of them cannot be neglected, es- pecially in the expansion period.

<!-- b000258 | prose | pages [17] -->
Our Most Profit model in game theory has provided a future planning of probabili- ties in the two situations: chargers first, or market first? To find a general "behaviour", our game theory model applied EV and charging piles generations, to find an optimized solution(Table 6).

<!-- b000259 | prose | pages [17] -->
By linear regression, we can generally observe that when Pe is stable in the standard

<!-- b000260 | prose | pages [17] -->
Year 2012 2013 2014 2015 2016 2017 122438 EV Purchase 52607 97507 Chargers 11042 20198 Pe 0.11 0.20 P0 0.21 0.21 116099 158614 199826 25684 31674 44028 59167 0.26 0.31 0.44 0.59 0.21 0.27 0.28 0.30

<!-- b000261 | caption | pages [17] -->
Table 6: Best Profit Model Derivation

<!-- b000262 | prose | pages [17] -->
value of 0.375, the value of P0 should be stable at 0.275. The game theory valid test in U.S. corresponds our calculations of South Korea. Such a "behavior" could be considered as"the choice of customers and producers". Weapply the parameter P0 = 0.275 for our game theory case.

<!-- b000263 | prose | pages [17] -->
Thus, our proposal talks about the balance of constructing the ratio of charging piles and EV Build a charging system and electric vehicles proportionally in a scale basedon the standard ratio of 0.275. The investment proportion of the two projects is carried out according to the price of the charging system divided by the price of the chargers di- vided by the price of the electric vehicle, and the fluctuation limit is no more than 10 million. According to the game theory model, when the pile ratio is less than 0.275, it tends to pile the pile, and vice versa. The important factor is the ratio of pile to car and the saturation limit of pile and car. From the perspective of urban and rural areas, the mixed construction should be taken.

<!-- b000264 | prose | pages [17] -->
For the first situation, the chargers’ leading one, we can take a qualitative system dynamic approach. When we placed the angle of view in the process of attention to the improvement of the electric system, we find it exists as a system flow and it has a posi- tive feedback, which makes us able to use system dynamics model to solve the problem. In the analysis of the mutual promotion mechanism between charging piles and electric vehicles, we can realize that there is a considerable positive feedback incentive between the two situations. We can draw a brief system dynamics process(Figure 9) based on the existing positive feedback and system flow. Through the analysis of system dynamics model, we can get a preliminary answer that is to say, if you don’t appear under the mu-

<!-- b000265 | furniture | pages [18] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000266 | furniture | pages [18] -->
Team # 81402

<!-- b000267 | furniture | pages [18] -->
Page 16 of 27

<!-- b000268 | prose | pages [18] -->
tual promotion mechanism of overproduction, will be the trend of positive feedbackon the whole, in other words, that is to build one arbitrary will promote another production and construction.

<!-- b000269 | prose | pages [18] -->
For the second situation, we will let the market drive.

<!-- b000270 | caption | pages [18] -->
Figure 9: System Dynamic Process

<!-- b000271 | prose | pages [18] -->
4.2.3 Task 2c

<!-- b000272 | prose | pages [18] -->
As the task requires a "blank" market, our investment would firstly "build" chargers to stimulate the first 6 years of an EV market corresponding to the graph in task 1) and chargers’ growth in task 2b). For the simplicity, we adjusted our placing with current sales data of Korea EV market, and re-calculate the time scale. Then we put the market evolution model in our task solution.

<!-- b000273 | prose | pages [18] -->
The key factor of our Market Prediction Model is generally shaped by the relationship of high-technology production and the old generations of the production. Thisrelation- ship has it’s own parameters in p(innovations) and q(imitations). In South Korea case, the p and q were generally modified by it’s market evolution. Actually, South Korea is actually a leading peer in worldwide EV market. Domestic companies like Hyundai also promoted it’s own EV products. Statistics shows that Korea is the only country that up- graded its target in 2016, from 200 000 to 250 000 electric cars by 2020, as per the Special Plan for Fine Dust Management, released in June 2016[16].

<!-- b000274 | prose | pages [18] -->
We applied Bass Diffusion Model as our Market Prediction Model. We applied EV sales data of South Korea(since 2012), the competition in EV industry were neglected. We applied Bass Diffusion Model because it performs well in South Korea’s previous data, revealing a situation that South Korea is on the track of Bass Prediction.

<!-- b000275 | prose | pages [18] -->
Our simulation shows the EV market evolution in South Korea in Figure10 (Adop- tion at time t) and Figure11(Ultimate Potential adopted by time).

<!-- b000276 | prose | pages [18] -->
The ultimate adoption percentage is shown in table 7.

<!-- b000277 | caption | pages [18] -->
Table 7: Ultimate Adoption Percentage (zeroth point from2018)

<!-- b000278 | prose | pages [18] -->
Percentage 10% Year 2026 30% 50% 99.9% 2028 2029 2036

<!-- b000279 | furniture | pages [19] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000280 | furniture | pages [19] -->
Team # 81402

<!-- b000281 | furniture | pages [19] -->
Page 17 of 27

<!-- b000282 | caption | pages [19] -->
Figure 10: Adoption at time t

<!-- b000283 | caption | pages [19] -->
Figure 11: Ultimate Potential adopted by time

<!-- b000284 | prose | pages [19] -->
4.3 Task 3

<!-- b000285 | prose | pages [19] -->
Wedon’t have much confidence in the model’s feasibility of promoting EV into the five countries. As mentioned above, both U.S. and South Korea have well-constructed road, vehicles culture, high household income, and urbanization degree. We suppose that in some other developed countries, like Australia, with well-constructed roadnetwork, this might be feasible. In city countries like Singapore, we might face the hazard estima- tion of demand. The demand of a city must be carefully estimated, as mentioned above. In other developing countries, like China, India or Indonesia, the main problem would be the household income, urbanization. Thanks to the government’s policy in China, China’s EV market is now becoming a leading market worldwide. After applying data in seven aspects, we get the results of Linear Regression Model plotted in Figure 12.

<!-- b000286 | prose | pages [19] -->
By comparing these index, we can know which is more important in this country. The network in Saudi Arabia and Australia might be a problem, as the large occupa- tion of desert area. As for Singapore, over-promotion in Vehicles industry would leave a negative effect on it’s traffic. China needs to improve its urbanization. In Indonesia, it needs to improve its GDP per Capita, its gas price and urbanization. To expand the

<!-- b000287 | furniture | pages [20] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000288 | furniture | pages [20] -->
Team # 81402

<!-- b000289 | furniture | pages [20] -->
Page 18 of 27

<!-- b000290 | prose | pages [20] -->
vehicles industries, Saudi Arabia and U.S. needs to reduce it’s Gini Coefficients - make more people afford vehicles.

<!-- b000291 | prose | pages [20] -->
However, there are many aspects influencing a country’s market. A simple classifi- cation as we proposed above, might not gave an accurate, quantitative answer on the key factors that trigger the selection of different approaches. The following factors can be taken into consideration:

<!-- b000292 | prose | pages [20] -->
• GDP per Capita(weighted, can be replaced by household income or consumption data)

<!-- b000293 | prose | pages [20] -->
• PPI(weighted, can be replaced by domestic EV industries data)

<!-- b000294 | prose | pages [20] -->
• Gini Intex(weighted, or Engel’s coefficients)

<!-- b000295 | prose | pages [20] -->
• Road network total miles(weighted, but it’s constrained by the geography land scale of a country)

<!-- b000296 | prose | pages [20] -->
• Vehiclesper Capita and Oil Price (weighted, but this one should be the EV adoption weight in the future)

<!-- b000297 | prose | pages [20] -->
• Urbanization(weighted)

<!-- b000298 | prose | pages [20] -->
• Public Policy(support from government)

<!-- b000299 | prose | pages [20] -->
• Vehicles Culture and Public transportation

<!-- b000300 | prose | pages [20] -->
To summarize, EV market would have different evolution in different countries. Geog- raphy, economics, policy, culture...all of them can affect a market’s domestic evolution.

<!-- b000301 | caption | pages [20] -->
Figure 12: The Weight of 7 aspects in 6 countries

<!-- b000302 | prose | pages [20] -->
4.4 Task 4

<!-- b000303 | prose | pages [20] -->
Weare drifting such a technological world that we would never know what will happen in the next decade. What we havent dreamed up, like smart phones and ArtificialIntel- ligence, have come true. Relying on our limited knowledge about forecasting the future

<!-- b000304 | furniture | pages [21] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000305 | furniture | pages [21] -->
Team # 81402

<!-- b000306 | furniture | pages [21] -->
Page 19 of 27

<!-- b000307 | prose | pages [21] -->
world, what we need to deeply think is that whether or not it really has a profound im- pact on the energy structure.

<!-- b000308 | prose | pages [21] -->
Considering the energy structure nowadays, it is mainly dependent on fossil fuels such as coal, oil and natural gas. Other kinds of energy like wind, hydrogen and nuclear are not common in our daily life. Using the heat directly like the internal combustion engine for driving the car is constantly seen than others. As there are not enough technic for keeping the car motivated and full of charge, in terms of vehicle performance, there are some deficiencies in electric cars. Besides, the cost of electric vehicles is too high and there are lack of enough assistant from policy and country, leading to its slow develop- ment today.

<!-- b000309 | prose | pages [21] -->
The development of electric vehicles is mainly from climate international change in the world. As countries around the world have a great deal of concern about environ- mental issues, climate change and so on, new energy has become the focus of the worlds attention. A larger scale in developing the new energy such as wind and hydrogen to power generation seems mainstream. Electric vehicles are a fundamental basic in the development of using new energy. What we are concerned about is how chargers can supply enough impetus and reserve enough energy for a longdistance.

<!-- b000310 | prose | pages [21] -->
In a continuous period, we may think about a better way to supply enough impe- tus and reserve enough energy, for instance, developing new energy and making a for- mation of an alternative to electric vehicles. If the new technology cannot get enough improvement on doing so, I think that such an innovation cannot be revolutionary on todays power demand. Such a barrier cannot hold a big truck for lifting a heavy stone and delivering a high speed in todays fast life for a quick speed such as airplane and the high-speed rail. Imaging that there is a change that can greatly inspire the property of high-speed and enough power reservation in a modality of electricity, I think that it must leads to a huge decline about the cost of electric vehicles unless there is something necessary for supplying that is too expensive to cover the cost such as a pressurized gas tank for storing liquefied hydrogen gas. Maybe in a few decades we can see a spec- tacular situation that around the world there are countless electric vehicles crossing the road safely than before as there is no open flame for explosion. It must accumulate the development of electric vehicles in a positive feedback and thus gradually improves the number of holding EV and charging piles. In a few years it can replace fossil fuel cars around the world.

<!-- b000311 | prose | pages [21] -->
In another perspective, if the technological level has a great impact and even there exists a huge change so that it can replace electric vehicles such as nuclear energy which is portable and safe enough for not leaking. Maybe such technic has such a profound ef- fect on electric vehicles that is particularly exciting. Although electric cars have enough room to grow and update, a more efficient approach to energy use would make such progress negligible. So in such intense energy structure in the process of transformation, the vigorous development of electric vehicles, maybe over a period of time, will be much more efficient because of the new energy development and gradual reduction of its size, eventually leading to the most efficient means of energy use, such as nuclear energy or hydrogen, finally sustained application above to our way oftransportation.

<!-- b000312 | prose | pages [21] -->
In a word, the development of energy depends on the newest energy structure. We hopefullysee such a better transportation incar-share and ride-share services, self-driving cars, rapid battery-swap stations for electric cars, and even flying cars and Hyperloop.

<!-- b000313 | furniture | pages [22] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000314 | furniture | pages [22] -->
Team # 81402

<!-- b000315 | furniture | pages [22] -->
Page 20 of 27

<!-- b000316 | prose | pages [22] -->
4.5 Handout

<!-- b000317 | prose | pages [22] -->
As an international energy summit, we are very pleasant to be here with all of you in the diplomatic field. During these days of conferences, we will mainly discuss the develop- ment of energy structure and policy blueprint. We understand that different countries have different energy policies and energy technology development plans. We hopethat a forward-looking energy structure will be more suitable for a long-term planning, con- tributing to the future of our planet from every part.

<!-- b000318 | prose | pages [22] -->
The meeting to discuss the main content has the following aspects, also hoping that leaders can agree on agreement, for each national energy policy focus on targeted policy.

<!-- b000319 | prose | pages [22] -->
• Future use of new energy

<!-- b000320 | prose | pages [22] -->
• Structural contradictions in new energy development

<!-- b000321 | prose | pages [22] -->
• Development prospects and plans for new energy applications.

<!-- b000322 | prose | pages [22] -->
Our meeting attaches much importance to the specific implementation of the protocol after the end of the conference in domestic laws. Electric cars contributes a lot on the reduction of pollution. In the concrete of new energy development and popularization of electric cars, we propose several factors which could influence the policies for promoting electric vehicles.

<!-- b000323 | prose | pages [22] -->
These factors are listing as follows:

<!-- b000324 | prose | pages [22] -->
• The state of economic development

<!-- b000325 | prose | pages [22] -->
• The development of electric vehicles

<!-- b000326 | prose | pages [22] -->
• State power supply situation

<!-- b000327 | prose | pages [22] -->
• The development of electric vehicles

<!-- b000328 | prose | pages [22] -->
• State power supply situation

<!-- b000329 | prose | pages [22] -->
• National road traffic distribution planning

<!-- b000330 | prose | pages [22] -->
• Trasportation network

<!-- b000331 | prose | pages [22] -->
• Urbanization

<!-- b000332 | prose | pages [22] -->
• Engels coefficient

<!-- b000333 | prose | pages [22] -->
• The state finances tax on related areas

<!-- b000334 | prose | pages [22] -->
• International cooperation and trade

<!-- b000335 | prose | pages [22] -->
• Transformation of technological achievements

<!-- b000336 | prose | pages [22] -->
• International cooperation in the field of technology

<!-- b000337 | prose | pages [22] -->
Weaware that the factors above do not fully cover all fields of a country’s blueprint. Our hope is to initiate a trend with green, electric vehicles. We hope that stay touched in the summit of the differences and contradictions, participate in negotiations of the interna- tional framework, being committed to global governance and development, jointly set up a broader platform for the development of new energytechnologies.

<!-- b000338 | furniture | pages [23] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000339 | furniture | pages [23] -->
Team # 81402

<!-- b000340 | heading | pages [23] -->
References

<!-- b000341 | furniture | pages [23] -->
Page 21 of 27

<!-- b000342 | references | pages [23] -->
[1] Becker, T. A., Sidhu, I., & Tenderich, B. (2009). Electric vehicles in the United States:

<!-- b000343 | references | pages [23] -->
a new model with forecasts to 2030. Center for Entrepreneurship and Technology,

<!-- b000344 | references | pages [23] -->
University of California, Berkeley, 24.

<!-- b000345 | references | pages [23] -->
[2] Chen, T. D., Kockelman, K. M., & Khan, M. (2013, January). The electric vehicle

<!-- b000346 | references | pages [23] -->
charging station location problem: a parking-based assignment method for Seattle.

<!-- b000347 | references | pages [23] -->
In Transportation Research Board 92nd Annual Meeting (Vol. 340, pp. 13-1254).

<!-- b000348 | references | pages [23] -->
[3] Church, R., & ReVelle, C. (1974, December). The maximal covering location prob-

<!-- b000349 | references | pages [23] -->
lem. In Papers of the Regional Science Association (Vol. 32, No. 1, pp. 101-118).

<!-- b000350 | references | pages [23] -->
Springer-Verlag.

<!-- b000351 | references | pages [23] -->
[4] Destination Charging | Tesla. (2018). Tesla.com. Retrieved 10 February 2018, from

<!-- b000352 | references | pages [23] -->
https://www.tesla.com/destination-charging

<!-- b000353 | references | pages [23] -->
[5] Dijkstra, Edsger W. "A note on two problems in connexion with graphs." Nu-

<!-- b000354 | references | pages [23] -->
merische mathematik 1.1 (1959): 269-271.

<!-- b000355 | references | pages [23] -->
[6] Fanding, D. (1994). A Faster Algorithm for Shortest-Ptath SPFA[J]. Journal of South-

<!-- b000356 | references | pages [23] -->
west Jiaotong University, 2.

<!-- b000357 | references | pages [23] -->
[7] Frade, I., Ribeiro, A., Gonçalves, G., & Antunes, A. (2011). Optimal location of

<!-- b000358 | references | pages [23] -->
charging stations for electric vehicles in a neighborhood in Lisbon, Portugal. Trans-

<!-- b000359 | references | pages [23] -->
portation research record: journal of the transportation research board, (2252), 91-

<!-- b000360 | references | pages [23] -->
98.

<!-- b000361 | references | pages [23] -->
[8] Hillier, F. S. (2012). Introduction to operations research. Tata McGraw-Hill Educa-

<!-- b000362 | references | pages [23] -->
tion.

<!-- b000363 | references | pages [23] -->
[9] Lam, A. Y., Leung, Y. W., & Chu, X. (2014). Electric vehicle charging station place-

<!-- b000364 | references | pages [23] -->
ment: Formulation, complexity, and solutions. IEEE Transactions on Smart Grid,

<!-- b000365 | references | pages [23] -->
5(6), 2846-2856.

<!-- b000366 | references | pages [23] -->
[10] Nash, J. (1951). Non-cooperative games. Annals of mathematics, 286-295.

<!-- b000367 | references | pages [23] -->
[11] Norton, J. A., & Bass, F. M. (1987). A diffusion theory model of adoption and sub-

<!-- b000368 | references | pages [23] -->
stitution for successive generations of high-technology products. Management sci-

<!-- b000369 | references | pages [23] -->
ence, 33(9), 1069-1086.

<!-- b000370 | references | pages [23] -->
[12] Monthly Plug-In Sales Scorecard. (2018). Insideevs.com. Retrieved 10 February

<!-- b000371 | references | pages [23] -->
2018, from https://insideevs.com/monthly-plug-in-sales-scorecard/

<!-- b000372 | references | pages [23] -->
Co-operation

<!-- b000373 | references | pages [23] -->
[13] Organization

<!-- b000374 | references | pages [23] -->
for

<!-- b000375 | references | pages [23] -->
Economic

<!-- b000376 | references | pages [23] -->
and

<!-- b000377 | references | pages [23] -->
Development,

<!-- b000378 | references | pages [23] -->
Retail

<!-- b000379 | references | pages [23] -->
Registrations

<!-- b000380 | references | pages [23] -->
Trade

<!-- b000381 | references | pages [23] -->
Sales:

<!-- b000382 | references | pages [23] -->
Passenger

<!-- b000383 | references | pages [23] -->
Car

<!-- b000384 | references | pages [23] -->
for

<!-- b000385 | references | pages [23] -->
the

<!-- b000386 | references | pages [23] -->
Republic

<!-- b000387 | references | pages [23] -->
of

<!-- b000388 | references | pages [23] -->
Korea

<!-- b000389 | references | pages [23] -->
[SLRTCR03KRQ180S], retrieved from FRED, Federal Reserve Bank of St. Louis;

<!-- b000390 | references | pages [23] -->
https://fred.stlouisfed.org/series/SLRTCR03KRQ180S, February 10, 2018.

<!-- b000391 | references | pages [23] -->
[14] Supercharger | Tesla. (2018). Tesla.com. Retrieved 10 February 2018, from

<!-- b000392 | references | pages [23] -->
https://www.tesla.com/supercharger

<!-- b000393 | references | pages [23] -->
[15] U.S. vehicle sales 1977-2017 | Statistic. (2018). Statista. Retrieved 10 February 2018,

<!-- b000394 | references | pages [23] -->
from https://www.statista.com/statistics/199983/us-vehicle-sales-since-1951/

<!-- b000395 | furniture | pages [24] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000396 | furniture | pages [24] -->
Team # 81402

<!-- b000397 | furniture | pages [24] -->
Page 22 of 27

<!-- b000398 | references | pages [24] -->
[16] https://www.iea.org/publications/freepublications/publication/GlobalEVOutlook2017.pdf

<!-- b000399 | references | pages [24] -->
[17] https://www.carinsurance.com/Articles/average-miles-driven-per-year-by-

<!-- b000400 | references | pages [24] -->
state.aspx

<!-- b000401 | references | pages [24] -->
[18] https://en.wikipedia.org/wiki/List_of_United_States_urban_areas#cite_note-1

<!-- b000402 | references | pages [24] -->
[19] https://www.census.gov/geo/reference/ua/urban-rural-2010.html

<!-- b000403 | references | pages [24] -->
[20] https://developers.google.com/maps/documentation/geocoding/intro

<!-- b000404 | references | pages [24] -->
[21] https://developers.google.com/optimization/flow/mincostflow

<!-- b000405 | references | pages [24] -->
[22] https://fivethirtyeight.com/features/how-suburban-are-big-american-cities/

<!-- b000406 | references | pages [24] -->
[23] https://en.wikipedia.org/wiki/List_of_countries_by_income_equality

<!-- b000407 | references | pages [24] -->
[24] https://en.wikipedia.org/wiki/List_of_countries_by_road_network_size

<!-- b000408 | references | pages [24] -->
[25] http://www.tageo.com/index-e-ks-cities-KR.htm

<!-- b000409 | references | pages [24] -->
[26] https://www.bloomberg.com/graphics/gas-prices/#20173:Australia:USD:g

<!-- b000410 | references | pages [24] -->
[27] https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)_per_capita

<!-- b000411 | references | pages [24] -->
[28] https://en.wikipedia.org/wiki/List_of_countries_by_vehicles_per_capita

<!-- b000412 | references | pages [24] -->
[29] https://tradingeconomics.com/indonesia/producer-prices

<!-- b000413 | references | pages [24] -->
[30] https://en.wikipedia.org/wiki/Urbanization_by_country

<!-- b000414 | heading | pages [24] -->
Appendices

<!-- b000415 | heading | pages [24] -->
Appendix A

<!-- b000416 | prose | pages [24] -->
Code

<!-- b000417 | prose | pages [24] -->
Here are codes we used in our model as follows.

<!-- b000418 | prose | pages [24] -->
Build Graph

<!-- b000419 | prose | pages [24] -->
import csv import json import sys import matplotlib.pyplot as plt from utils import distance, calculate_shortest_path, is_connected,

<!-- b000420 | prose | pages [24] -->
calculate_shortest_path_dijkstra import math import numpy as np

<!-- b000421 | prose | pages [24] -->
vertex = []

<!-- b000422 | prose | pages [24] -->
print "processing data..." # plot the major cities cnt = 0 with open("./data/urban_data_with_state.json", "r") as f:

<!-- b000423 | furniture | pages [25] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000424 | furniture | pages [25] -->
Team # 81402

<!-- b000425 | furniture | pages [25] -->
Page 23 of 27

<!-- b000426 | prose | pages [25] -->
cities = json.load(f) city_x = [] city_y = [] city_no = [] for city in cities:

<!-- b000427 | prose | pages [25] -->
cnt += 1 if city["longtitude"] < -140:

<!-- b000428 | prose | pages [25] -->
continue if city["latitude"] < 20:

<!-- b000429 | prose | pages [25] -->
continue city_x.append(city["longtitude"]) city_y.append(city["latitude"]) city_no.append(cnt - 1) point = {} point["x"] = city["longtitude"] point["y"] = city["latitude"] point["type"] = "city" point["no"] = cnt - 1 point["state"] = city["state"] point["area"] = city["land_area"] point["name"] = city["name"] if len(point["state"]) > 2:

<!-- b000430 | prose | pages [25] -->
print "****** ERROR *********" point["population"] = city["population"] vertex.append(point)

<!-- b000431 | prose | pages [25] -->
print "major cities: ", len(city_x), "/", len(cities)

<!-- b000432 | prose | pages [25] -->
# plot the super chargers schargers x = [] schargers_y = [] schargers_no = [] cnt = 0 tot = 0 with open("./data/superchargers.csv", "r") as f:

<!-- b000433 | prose | pages [25] -->
lines = csv.reader(f) flag = True for line in lines:

<!-- b000434 | prose | pages [25] -->
if flag:

<!-- b000435 | prose | pages [25] -->
flag = False continue tot += 1 if float(line[2]) < -140 or float(line[2]) > -40:

<!-- b000436 | prose | pages [25] -->
continue schargers_x.append(float(line[2])) schargers_y.append(float(line[1])) schargers_no.append(tot - 1) point = {} point["x"] = float(line[2]) point["y"] = float(line[1]) point["type"] = "super_charger" point["no"] = tot - 1 vertex.append(point) print "super chargers: ", len(schargers_x), "/", tot

<!-- b000437 | prose | pages [25] -->
# plot the destination chargers chargers_x = [] chargers_y = [] chargers_no = [] cnt = 0 with open("./data/destinations.csv", "r") as f:

<!-- b000438 | furniture | pages [26] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000439 | furniture | pages [26] -->
Team # 81402

<!-- b000440 | furniture | pages [26] -->
Page 24 of 27

<!-- b000441 | prose | pages [26] -->
lines = csv.reader(f) flag = True for line in lines:

<!-- b000442 | prose | pages [26] -->
if flag:

<!-- b000443 | prose | pages [26] -->
flag = False continue cnt += 1 if float(line[2]) < -140 or float(line[2]) > -40:

<!-- b000444 | prose | pages [26] -->
continue x = float(line[2]) y = float(line[1]) if y < 20:

<!-- b000445 | prose | pages [26] -->
continue chargers_x.append(x) chargers_y.append(y) chargers_no.append(cnt - 1) point = {} point["x"] = x point["y"] = y point["type"] = "destination_charger" vertex.append(point) print "destination chargers: ", len(chargers_x), "/", cnt

<!-- b000446 | prose | pages [26] -->
print "" for i in range(len(vertex)):

<!-- b000447 | prose | pages [26] -->
sys.stdout.write("\033[F") #back to previous line sys.stdout.write("\033[K") #clear line print "classifying vertex into urban/suburban/rural: %.2f" % (float(i) /

<!-- b000448 | prose | pages [26] -->
float(len(vertex)) * 100.) + "%" if vertex[i]["type"] == "city":

<!-- b000449 | prose | pages [26] -->
vertex[i]["position"] = "urban" else:

<!-- b000450 | prose | pages [26] -->
is_suburban = False for j in range(len(vertex)):

<!-- b000451 | prose | pages [26] -->
if vertex[j]["type"] == "city":

<!-- b000452 | prose | pages [26] -->
if distance(vertex[i]["y"], vertex[i]["x"], vertex[j]["y"],

<!-- b000453 | prose | pages [26] -->
vertex[j]["x"]) < math.sqrt(vertex[j]["area"] / 2 / math. pi):

<!-- b000454 | prose | pages [26] -->
vertex[i]["position"] = "suburban" is_suburban = True break if is_suburban == False:

<!-- b000455 | prose | pages [26] -->
vertex[i]["position"] = "rural"

<!-- b000456 | prose | pages [26] -->
with open("./data/vertex.json", "w") as f:

<!-- b000457 | prose | pages [26] -->
json.dump(vertex, f, indent = 4, sort_keys = True)

<!-- b000458 | prose | pages [26] -->
a = plt.scatter(city_x, city_y, c = 'r', marker = 'o') b = plt.scatter(chargers_x, chargers_y, c = 'g', marker = '+') c = plt.scatter(schargers_x, schargers_y, c = 'b', marker = '+') plt.legend((a, b, c), ("major cities", "destination chargers", "super chargers

<!-- b000459 | prose | pages [26] -->
")) plt.xlabel("longtitude") plt.ylabel("latitude")

<!-- b000460 | prose | pages [26] -->
MaxD = 170 * 1.609344 x = city_x + schargers_x + chargers_x y = city_y + schargers_y + chargers_y edges = [] edge_table = []

<!-- b000461 | furniture | pages [27] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000462 | furniture | pages [27] -->
Team # 81402

<!-- b000463 | furniture | pages [27] -->
Page 25 of 27

<!-- b000464 | prose | pages [27] -->
sz = len(x) for i in range(sz):

<!-- b000465 | prose | pages [27] -->
edge_table.append([]) print "size of V: ", sz print "" for i in range(sz):

<!-- b000466 | prose | pages [27] -->
sys.stdout.write("\033[F") #back to previous line sys.stdout.write("\033[K") #clear line print "building graph: %.2f" % (float(i) / float(sz) * 100.) + "%" for j in range(i + 1, sz):

<!-- b000467 | prose | pages [27] -->
d = distance(x[i], y[i], x[j], y[j]) if d <= MaxD:

<!-- b000468 | prose | pages [27] -->
edges.append([i, j, d]) edge_table[i].append([j, d]) edge_table[j].append([i, d]) print "size of E: ", len(edges)

<!-- b000469 | prose | pages [27] -->
print "is connected: ", is_connected(sz, edge_table)

<!-- b000470 | prose | pages [27] -->
print "" total_dist = [] with open("data/spp.csv", "w") as f:

<!-- b000471 | prose | pages [27] -->
for i in range(sz):

<!-- b000472 | prose | pages [27] -->
sys.stdout.write("\033[F") #back to previous line sys.stdout.write("\033[K") #clear line print "calculating shortest path: %.2f" % (float(i + 1) / float(sz) *

<!-- b000473 | prose | pages [27] -->
100.) + "%" dist = calculate_shortest_path(i, sz, edge_table) total_dist = total_dist + dist for j in range(len(dist)):

<!-- b000474 | prose | pages [27] -->
if j > 0:

<!-- b000475 | prose | pages [27] -->
f.write(",") f.write(str(dist[j])) f.write("\n") print "MinD = %s" % np.mean(np.asarray(total_dist))

<!-- b000476 | prose | pages [27] -->
Linear Programming

<!-- b000477 | prose | pages [27] -->
import networkx as nx import random import sys from ortools.graph import pywrapgraph import timeit import csv import re import json

<!-- b000478 | prose | pages [27] -->
start = timeit.default_timer()

<!-- b000479 | prose | pages [27] -->
alpha = 0.25 minD = 500 min_cost_flow = pywrapgraph.SimpleMinCostFlow() maxC = 50000 base = 365 * 24 * 340 * 1.609344

<!-- b000480 | prose | pages [27] -->
ssp = [] sz = 0 print "" total = 0. with open("./data/ssp_new_1.csv", "r") as f:

<!-- b000481 | prose | pages [27] -->
while True:

<!-- b000482 | furniture | pages [28] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000483 | furniture | pages [28] -->
Team # 81402

<!-- b000484 | furniture | pages [28] -->
Page 26 of 27

<!-- b000485 | prose | pages [28] -->
line = f.readline() if line == None or len(line) == 0:

<!-- b000486 | prose | pages [28] -->
break sz += 1 sys.stdout.write("\033[F") #back to previous line sys.stdout.write("\033[K") #clear line print "retreiving ssp data: %.2f" % (float(sz) / 4295. * 100) + "%" line = re.sub(r"\n", '', line) line = line.split(r",") for i in range(len(line)):

<!-- b000487 | prose | pages [28] -->
line[i] = float(line[i]) ssp.append(line)

<!-- b000488 | prose | pages [28] -->
with open("./data/demand.json", "r") as f:

<!-- b000489 | prose | pages [28] -->
demand = json.load(f)

<!-- b000490 | prose | pages [28] -->
min_cost_flow = pywrapgraph.SimpleMinCostFlow() inf = 0x7fffffff

<!-- b000491 | prose | pages [28] -->
total_flow = 0 print "" for i in range(1, sz + 1):

<!-- b000492 | prose | pages [28] -->
sys.stdout.write("\033[F") #back to previous line sys.stdout.write("\033[K") #clear line print "building network: %.2f" % (float(i) / float(sz) * 100.0) + "%" total_flow += int(demand[i - 1] / base + 2) min_cost_flow.SetNodeSupply(i, int((1. - alpha) * demand[i - 1] / base +

<!-- b000493 | prose | pages [28] -->
1)) min_cost_flow.SetNodeSupply(sz + i, int(alpha * demand[i - 1] / base + 1)) min_cost_flow.SetNodeSupply(2 * sz + i, - maxC) for j in range(1, sz + 1):

<!-- b000494 | prose | pages [28] -->
min_cost_flow.AddArcWithCapacityAndUnitCost(i, 2 * sz + j, inf,

<!-- b000495 | prose | pages [28] -->
int( ssp[i - 1][j - 1])) if ssp[i - 1][j - 1] >= minD:

<!-- b000496 | prose | pages [28] -->
min_cost_flow.AddArcWithCapacityAndUnitCost(sz + i, 2 * sz + j,

<!-- b000497 | prose | pages [28] -->
inf, int(ssp[i - 1][j - 1]))

<!-- b000498 | prose | pages [28] -->
print "sz: %s" % sz print "total_flow: %s" % total_flow print "calculating..." min_cost_flow.SolveMaxFlowWithMinCost() print "min-cost: ", min_cost_flow.OptimalCost()

<!-- b000499 | prose | pages [28] -->
solution = [] num_of_arcs = min_cost_flow.NumArcs() max_flow = 0 flow = [0] * sz print "" for i in range(num_of_arcs):

<!-- b000500 | prose | pages [28] -->
sys.stdout.write("\033[F") #back to previous line sys.stdout.write("\033[K") #clear line print "retreiving optimal flow: %.2f" % (float(i + 1) / float(num_of_arcs)

<!-- b000501 | prose | pages [28] -->
* 100.0) + "%" flow[min_cost_flow.Head(i) - 2 * sz - 1] += min_cost_flow.Flow(i) max_flow += min_cost_flow.Flow(i) print "max-flow: ", max_flow

<!-- b000502 | prose | pages [28] -->
with open("./data/assignments.json", "w") as f:

<!-- b000503 | prose | pages [28] -->
json.dump(flow, f, indent = 4)

<!-- b000504 | prose | pages [28] -->
stop = timeit.default_timer()

<!-- b000505 | furniture | pages [29] -->
精品数模资料，各类比赛优秀论文、学习教程、写作模板与经验技巧、matlab程序代码资料等，尽在淘宝店铺：闵大荒工科男的杂货铺！

<!-- b000506 | furniture | pages [29] -->
Team # 81402

<!-- b000507 | furniture | pages [29] -->
Page 27 of 27

<!-- b000508 | prose | pages [29] -->
print "time consumed: %s s" % (stop - start)
