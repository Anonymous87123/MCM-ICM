# P-B-2023-2315379-42733c7a

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2023

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | title | pages [1] -->
B

<!-- b000004 | title | pages [1] -->
2315379

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | prose | pages [1] -->
Build a common paradise for humans and wildlife in the Maasai Mara

<!-- b000008 | heading | pages [1] -->
Summary

<!-- b000009 | prose | pages [1] -->
Each year, the world's most spectacular wildlife migration, known by word of mouth as the "Mara River Crossing," takes place in Kenya's Maasai Mara Reserve. The reserve was originally established to protect wildlife and natural resources. However, the interests of the people living in the area cannot be ignored as well. Before all the models are established, we clean and visualize a large amount of data with high reliability,which is of great help to our subsequent indicator selection work.In addition, we precisely defined the vague concepts of "lost opportunities" and "negative interactions". For problem 1, we divided the Maasai Mara roughly equally into 36 grids in order to facilitate modeling, taking into account its current distribution of natural resources and wildlife. For each grid, we choose to establish one of 4 functional areas: wildlife sanctuary, agricultural area, hunting area, or tourism area. In order to balance the interests of wildlife and humans in the area, we proposed the concept and calculation method of ecological and economic benefits, and took their maximum value as the objective function.We established Model I: Maasai Mara Resource Allocation Strategy Model based on dual-goal planning. The constraints are:(1)The size of the ecological benefit constrains the type of functional area;(2) the limitation of the number of tourists; (3) the guarantee of residents' income, etc. Using Lingo, 3 seanarios are calculated. Take scenario 2 as an example: establish 13 wildlife sanctuaries, 13 agricultural areas, 2 hunting areas, and 9 tourist areas. For problem 2, in order to determine the management solution that would produce the best results, we developed Model II: a minimal interaction model based on Dijkstra and an economic impact evaluation model. We specify four types of interactions, analogous to the influence relationships between the four functional areas, and determine the weights of the paths in the directed graph.Based on the 3 scenarios obtained from the solution of problem 1, we use the improved Dijkstra algorithm to measure the interaction impact of each scenario by calculating its shortest path separately. Meanwhile, the economic benefits of the three scenarios were calculated as $141,274.438, $154,948.974, and $130,180.760 (unit:million) respectively, taking into account the economic development level of the Masai Mara region. The results show that scenario 2 has the best interaction and economic efficiency. Therefore, scenario 2 is the best.

<!-- b000010 | prose | pages [1] -->
For problem 3, we developed Model Ⅲ: A long-term trend forecasting model for the Masai Mara region. We first predicted the increase in tourists that might result from a decrease in negative human-animal interactions. We then fitted a quadratic nonlinear regression equation to predict the relationship between tourism revenue and the number of tourists in Kenya from 2010-2019, which in turn predicted changes in tourism revenue. Using the COVID-19 pandemic as an example, in testing the accuracy of the long-term prediction results, we used a t-test and calculated a p-value of less than 0.05, indicating that tourism revenue in Kenya before and after the COVID-19 pandemic was significantly different.The COVID-19 pandemic was considered to have affected tourism. Our model is highly adaptable due to the rich set of influencing factors and special cases discussed. We examined its application in Yellowstone National Park.

<!-- b000011 | prose | pages [1] -->
Finally, sensitivity analysis of the index weight shows that our model is not sensitive to changes in them.After discussing the advantages and improvements of the model, a two-page non-technical report on resource redistribution plan in the Maasai Mara and its value has been written for the Kenyan Tourism and Wildlife Committee.

<!-- b000012 | keywords | pages [1] -->
Key Words：Grid method; Dual-goal planning; Dijkstra's algorithm;Non-linear regression

<!-- b000013 | furniture | pages [2] -->
Page 2 of 25

<!-- b000014 | furniture | pages [2] -->
Team#2315379

<!-- b000015 | heading | pages [2] -->
Content

<!-- b000016 | contents | pages [2] -->
1.Introduction................................................................................................................................ 3

<!-- b000017 | contents | pages [2] -->
1.1 Background....................................................................................................................... 3

<!-- b000018 | contents | pages [2] -->
1.2 Restatement of the problem...............................................................................................3

<!-- b000019 | contents | pages [2] -->
1.3 Literature review............................................................................................................... 3

<!-- b000020 | contents | pages [2] -->
1.4 Our work............................................................................................................................3

<!-- b000021 | contents | pages [2] -->
2.Assumption and Justification....................................................................................................4

<!-- b000022 | contents | pages [2] -->
3.Notations and Definitions.......................................................................................................... 5

<!-- b000023 | contents | pages [2] -->
3.1 Notations........................................................................................................................... 5

<!-- b000024 | contents | pages [2] -->
3.2 Definitions.........................................................................................................................5

<!-- b000025 | contents | pages [2] -->
4.Data..............................................................................................................................................6

<!-- b000026 | contents | pages [2] -->
4.1 Data Overview...................................................................................................................6

<!-- b000027 | contents | pages [2] -->
4.2 Data Collection..................................................................................................................6

<!-- b000028 | contents | pages [2] -->
4.3 Data Screening & Visualization........................................................................................6

<!-- b000029 | contents | pages [2] -->
5.Problem 1.................................................................................................................................... 7

<!-- b000030 | contents | pages [2] -->
5.1 Problem analysis................................................................................................................7

<!-- b000031 | contents | pages [2] -->
5.2 Preparation of the model................................................................................................... 7

<!-- b000032 | contents | pages [2] -->
5.3 Establishment of the model............................................................................................... 8

<!-- b000033 | contents | pages [2] -->
5.3.1 Zoning according to wildlife distribution status.....................................................8

<!-- b000034 | contents | pages [2] -->
5.3.2 Determination of decision variables and constraints..............................................9

<!-- b000035 | contents | pages [2] -->
5.3.3 Determination of objective function.....................................................................11

<!-- b000036 | contents | pages [2] -->
5.4 Solution of the model...................................................................................................... 11

<!-- b000037 | contents | pages [2] -->
6.Problem 2.................................................................................................................................. 12

<!-- b000038 | contents | pages [2] -->
6.1 Problem analysis..............................................................................................................12

<!-- b000039 | contents | pages [2] -->
6.2 Preparation of the model................................................................................................. 12

<!-- b000040 | contents | pages [2] -->
6.2.2 Establishment of the model.................................................................................. 13

<!-- b000041 | contents | pages [2] -->
6.2.3 Solution of the model........................................................................................... 15

<!-- b000042 | contents | pages [2] -->
6.3 Economic impact evaluation model........................................................................ 15

<!-- b000043 | contents | pages [2] -->
7.Problem 3.................................................................................................................................. 16

<!-- b000044 | contents | pages [2] -->
7.1 Problem analysis..............................................................................................................16

<!-- b000045 | contents | pages [2] -->
7.2.1 Changes in tourism revenue................................................................................. 16

<!-- b000046 | contents | pages [2] -->
7.2.2 Changes in agriculture..........................................................................................17

<!-- b000047 | contents | pages [2] -->
7.2.3 Impact of the COVID-19 pandemic on tourism...................................................17

<!-- b000048 | contents | pages [2] -->
7.2.4 Long-term impact of policy implementation........................................................17

<!-- b000049 | contents | pages [2] -->
7.3 Model Migration: Yellowstone National Park................................................................ 18

<!-- b000050 | contents | pages [2] -->
7.3.1 Feasibility analysis of model migration............................................................... 18

<!-- b000051 | contents | pages [2] -->
7.3.2 Model improvement and solution.........................................................................19

<!-- b000052 | contents | pages [2] -->
8.Problem 4.................................................................................................................................. 20

<!-- b000053 | contents | pages [2] -->
9. Sensitivity analysis of the model.............................................................................................23

<!-- b000054 | contents | pages [2] -->
10.Evaluation and extension of the model.................................................................................23

<!-- b000055 | contents | pages [2] -->
10.1 Advantages.................................................................................................................... 23

<!-- b000056 | contents | pages [2] -->
10.2 Limitations and Extension of the model........................................................................24

<!-- b000057 | contents | pages [2] -->
11.Reference.................................................................................................................................24

<!-- b000058 | contents | pages [2] -->
12.Appendix................................................................................................................................. 25

<!-- b000059 | furniture | pages [3] -->
Page 3 of 25

<!-- b000060 | furniture | pages [3] -->
Team#2315379

<!-- b000061 | contents | pages [3] -->
1.Introduction

<!-- b000062 | heading | pages [3] -->
1.1 Background

<!-- b000063 | prose | pages [3] -->
Kenya, as an economically underdeveloped African country, spends a large amount of its fiscal revenue on building protected areas. At the same time, Kenya's tourism industry, which focuses on wildlife viewing, is a major source of national finance. Masai Mara, as one of the most famous wildlife reserves in Kenya, is famous for its magnificent grasslands and rich wildlife species. How to develop policies related to different areas of the reserve, making it possible to balance the interests of the residents of the area while protecting wildlife and other natural resources, has become an issue for the government to consider.

<!-- b000064 | heading | pages [3] -->
1.2 Restatement of the problem

<!-- b000065 | prose | pages [3] -->
For problem1, we need to consider whether to improve specific policies and management strategies for different areas of the current protected area. In considering new policies and management strategies, we need to balance the ecological benefits with the economic benefits, while avoiding negative impacts on the people attracted to the reserve by tourism.

<!-- b000066 | prose | pages [3] -->
For problem2, we need to determine which policies and management strategies work best. We need to build a model to rank and compare the results from task1. The principles of ranking and comparing include whether animal-human interactions under this policy are mostly positive, and whether they have a positive impact on the economy in and around the reserve.

<!-- b000067 | prose | pages [3] -->
For problem3, we need to predict the impact of the plan proposed in task1 on future development. We need to analyze the results of the corresponding policies and management strategies, and how these management strategies should be applied to other nature reserves.

<!-- b000068 | prose | pages [3] -->
For problem4, we need to provide a non-technical report for the Kenya Tourism and Wildlife Commission. In the report, we need to describe our proposed plan and analyze the impact and value of the plan for the Masai Mara Reserve.

<!-- b000069 | heading | pages [3] -->
1.3 Literature review

<!-- b000070 | prose | pages [3] -->
Scholars have conducted numerous studies on the zoning of nature reserves and the development of industries in the vicinity of the Masai Mara Nature Reserve.Bob E.L. Wishitemi et al. studied the linkages between poverty, environment, and ecotourism development in areas near the Masai Mara Reserve in Kenya [1].Kathleen Krafte Hollanda et al. analyzed the impact of tourism on conservation support, local livelihoods, and community resilience around the Masai Mara National Reserve in Kenya [2]. J. O. Ogutu1 et al. analyzed changes in wildlife populations in the Mara region of Kenya between 1977 and 2009 [3].Xue Fan analyzed network selection algorithms for nature reserve planning and design using the Daiyunshan National Nature Reserve as an example [4].

<!-- b000071 | heading | pages [3] -->
1.4 Our work

<!-- b000072 | prose | pages [3, 4] -->
To avoid complicated description , intuitively reflect our work process, the flow chart is show as the following Figure 1： 2.Assumption and Justification To simplify the problem, we make the following basic assumptions, each of which is properly justified.

<!-- b000073 | furniture | pages [4] -->
Page 4 of 25

<!-- b000074 | furniture | pages [4] -->
Team#2315379

<!-- b000075 | caption | pages [4] -->
Figure 1. Our work

<!-- b000077 | prose | pages [4] -->
Assumption 1: All data sources in this paper are true and reliable.  Justification: We need to rely on historical data from the Masai Mara and the surrounding area to analyze its trends in terms of economy, climate, and biodiversity. Therefore, the reliability of data is very important.

<!-- b000078 | prose | pages [4] -->
Assumption 2: No major natural disasters will occur in the Masai Mara and the  surrounding area in the next 50 years.

<!-- b000079 | prose | pages [4] -->
Justification: Earthquakes, mudslides, tsunamis, and other natural hazards are force majeure factors, and we cannot accurately predict or quantify their impact on model stability.

<!-- b000080 | prose | pages [4] -->
Assumption 3: The human-nature balance in the Masai Mara region is not governed  by factors other than the influences we have discussed.

<!-- b000081 | prose | pages [4] -->
Justification: We have envisioned as far as possible the relevant factors that may influence the problem and given reasons why the influence of other factors is almost absent. Therefore, in order to simplify the model, we can make the assumptions as above.

<!-- b000082 | furniture | pages [5] -->
Page 5 of 25

<!-- b000083 | furniture | pages [5] -->
Team#2315379

<!-- b000084 | prose | pages [5] -->
Assumption 4: For the 36 regions divided by the Maasai Mara, it can be assumed that  environmental, economic and other conditions are the same within each small region.

<!-- b000085 | prose | pages [5] -->
Justification: A reasonable idealization of the zoning of the Masai Mara region. Assuming the same conditions within the region helps us to calculate the associated benefits and costs.

<!-- b000086 | heading | pages [5] -->
Assumption 5: For the partially difficult-to-obtain data for the Masai Mara region,

<!-- b000087 | prose | pages [5] -->
 data from Kenya can be substituted.

<!-- b000088 | prose | pages [5] -->
Justification: Due to the difficulty of obtaining data for parts of the Masai Mara, we had to substitute relevant data from Kenya, however, based on the similarity of the known data, we can conclude that the effect of this practice on the accuracy of our model is within a reasonable error. ·Note：Relevant assumptions of game theory model will be shown below.

<!-- b000089 | prose | pages [5] -->
3.Notations and Definitions

<!-- b000090 | heading | pages [5] -->
3.1 Notations

<!-- b000091 | caption | pages [5] -->
Table 1. Notations

<!-- b000092 | heading | pages [5] -->
Notations

<!-- b000093 | prose | pages [5] -->
Descriptions �� Whether to build a nature reserve in the j-th geographical area �� Ecological benefit value �� Power generation of the i-th hydropower station �� Number of people in the j-th geographic area � The intensity of human-animal interaction ��� Construction of protected areas when implementing the i-th program ·Note：Some variables are not listed. Their specific meanings will be introduced below.

<!-- b000094 | heading | pages [5] -->
3.2 Definitions

<!-- b000095 | prose | pages [5] -->
Some vague concepts appear in the description of the topic. We define precisely those words or sentences that may be ambiguous. ✧Resources: Original text mentions that the resources within and outside the current boundaries of the park, we consider resources here as the ecological value of wildlife (biodiversity), vegetation resources, water resources, land resources, etc. ✧Lost Opportunities: Original text mentions that the impacts of lost opportunities experienced by the people who live near the preserve. We consider lost opportunity here to mean that people have to lose some of their arable land due to the presence of the reserve. Livestock raised and their own lives might be safe from some dangerous large wild animals. ✧The people attracted to the preserve :Original text mentions that minimize negative interactions between animals and the people attracted to the preserve, We consider the people attracted to the preserve here as domestic and foreign tourists from Kenya to the Masai Mara(excluding local residents). ✧Negative interactions: We group the negative interactions here into two categories. Category 1(People →Wildlife):Some visitors may feed unclean food to wildlife. In addition, there may also be some illegal poachers. Category 2(Wildlife →People):Some visitors may be injured by dangerous large wild animals, such as elephants and lions, during their visit.

<!-- b000096 | furniture | pages [6] -->
Page 6 of 25

<!-- b000097 | furniture | pages [6] -->
Team#2315379

<!-- b000098 | prose | pages [6] -->
4.Data

<!-- b000099 | heading | pages [6] -->
4.1 Data Overview

<!-- b000100 | prose | pages [6] -->
The question did not provide us with data directly, so we need to consider which data to collect in the model building. Through the analysis of the problem, we need to collect the data on the Masai Mara, such as information on animal species, geological conditions, climatic conditions, hydrological conditions, etc. In addition to that, we should collect the economic conditions and living standards of the people living in the area, etc.

<!-- b000101 | prose | pages [6] -->
Due to the large amount of data, it is not convenient to list them all, so visualizing the data for display is a good method.

<!-- b000102 | heading | pages [6] -->
4.2 Data Collection

<!-- b000103 | prose | pages [6] -->
We collected a lot of useful data from the references. And other data sources are shown in

<!-- b000104 | caption | pages [6] -->
Table 2.

<!-- b000105 | caption | pages [6] -->
Table 2. Data and Database Websites

<!-- b000106 | prose | pages [6] -->
Database Names Database Websites GDP&Employment https://insights.ceicdata.com/Untitled-insight/views Laws http://kenyalaw.org/kl/index.php?id=3329 Terrain and species https://www.masaimara.travel/maps.php#concervancy-map Climate & Weather https://zh.weatherspark.com/ https://www.bea.gov/data/income-saving/personal-income-by-state;

<!-- b000107 | prose | pages [6] -->
http://data.un.org/Default.aspx; Toursim http://data.un.org/DocumentData.aspx?id=481 ·Note：Data sources that are not listed will be marked when referenced.

<!-- b000108 | heading | pages [6] -->
4.3 Data Screening & Visualization

<!-- b000109 | prose | pages [6] -->
We made statistical analysis on the collected data and eliminated the outliers. The following figures show our visualization of boring data.

<!-- b000110 | caption | pages [6] -->
Figure 2. Data visualization

<!-- b000111 | prose | pages [6] -->
The visualization of other data will be shown below.

<!-- b000112 | furniture | pages [7] -->
Page 7 of 25

<!-- b000113 | furniture | pages [7] -->
Team#2315379

<!-- b000114 | prose | pages [7] -->
5.Problem 1

<!-- b000115 | heading | pages [7] -->
5.1 Problem analysis

<!-- b000116 | prose | pages [7] -->
In problem 1, we need to identify specific policies and management strategies that target the conservation of natural resources and wildlife in protected areas, and the economic interests of nearby residents.We plan to develop a dual-goal planning model to zone the Masai Mara Nature Reserve and establish a series of constraints to achieve this goal.

<!-- b000117 | heading | pages [7] -->
5.2 Preparation of the model

<!-- b000118 | prose | pages [7] -->
In our model, the calculation of ecological and economic benefits is involved, as follows： （1）Calculation of economic benefits For tourism revenue, we can calculate it by considering the number of visitors, the duration of the tour, the cost of the tour, and other factors.

<!-- b000119 | prose | pages [7] -->
Tr = Nt * Als * Ads * Lts (1) Where,Tr:Tourism revenue;Nt:Number of tourists;Als ：Average length of stay; Ads ： Average daily spending;;Lts: Length of tourist season.

<!-- b000120 | prose | pages [7] -->
For the economic benefits brought by other geographic areas, we estimated the approximate production value mainly by finding the data of the corresponding production value for the whole country, and then based on the area covered by the area. The interpretation of the corresponding indicators and data sources are as follows:

<!-- b000121 | prose | pages [7] -->
①Capture industry output：Even nature reserves need to set up hunting areas to maintain the ecological balance, such as African elephants in Kenya have largely lost their natural predators, which may destroy the ecological balance if not hunted artificially[7].For the state, the production value of the hunting industry is mainly legal hunting income, and people need to pay the appropriate taxes to the state after hunting wildlife.

<!-- b000122 | prose | pages [7] -->
②Agricultural output：Agricultural output here refers mainly to the economic returns from the production of crops. We can get this by looking at the contribution of agriculture to Kenya's GDP in recent years.

<!-- b000123 | prose | pages [7] -->
③Tourism output: This refers mainly to Kenya's revenue through tourism, which we obtained by reviewing information from the Kenya Tourism Board and the Kenya Tourism Report.

<!-- b000124 | prose | pages [7] -->
·Note：Specific data values are detailed in the Appendix.

<!-- b000125 | prose | pages [7] -->
（2）Calculation of ecological benefits To facilitate the comparison of these ecological indicators on the same scale, we normalize these data. For vegetation cover, we can normalize it to the range [0,1]. Specifically, we can first determine the minimum and maximum values and then normalize them using the following equation： Nvc = (Vc - MinVc) / ( MaxVc - MinVc) (2) Where,Nvc:Normalized vegetation cover;Vc:Vegetationcover;

<!-- b000126 | prose | pages [7] -->
MinVc/MaxVc:Minimum/Maximum vegetation cover.

<!-- b000127 | prose | pages [7] -->
For animal species and numbers, we can consider weighting different species of animals according to their rarity so that they can be compared on the same scale. For example, we can set the weight of lions to 1, elephants to 0.8, zebras to 0.5, antelopes to -0.3, and giraffes to 0.4. Then, we can normalize using the following formula.

<!-- b000128 | furniture | pages [8] -->
Page 8 of 25

<!-- b000129 | furniture | pages [8] -->
Team#2315379

<!-- b000130 | prose | pages [8] -->
Nai = (Asw * Na) / Sta (3) Where,Nai:Normalized animal index; Asw:Animal species weight; Na:Number of animals; Sta:Sum of total animals.

<!-- b000131 | prose | pages [8] -->
Then for the ecological benefits are calculated as follows： (4) * * V B A B P   1 2 x x x Where,��:Ecological benefits in protected areas;

<!-- b000132 | prose | pages [8] -->
�1:Animal weights;�2:Plant weights;

<!-- b000133 | prose | pages [8] -->
��:Normalized animal indices for protected areas;

<!-- b000134 | prose | pages [8] -->
��:Normalized vegetation cover in the protected area.

<!-- b000135 | prose | pages [8] -->
For the calculations in this paper, we assume that each vegetation cover is approximately the same because the Masai Mara Nature Reserve is located on grassland. In calculating the normalized faunal indices for different areas, we refer to the approximate faunal distribution in the Masai Mara National Reserve, as shown in Figure 3.

<!-- b000136 | caption | pages [8] -->
Figure 3.Distribution of wildlife in Masai Mara National Park

<!-- b000137 | heading | pages [8] -->
5.3 Establishment of the model

<!-- b000138 | heading | pages [8] -->
5.3.1 Zoning according to wildlife distribution status

<!-- b000139 | prose | pages [8] -->
To facilitate the subsequent classification and analysis of different areas and simplify calculations, based on the information consulted[5], we divided the Masai Mara reserve into 36 isometric grids, and the area of each grid can be obtained by dividing the total area of the Masai Mara National Park by 36, i.e., 50 km2, as shown in Figure 4.

<!-- b000140 | furniture | pages [9] -->
Page 9 of 25

<!-- b000141 | furniture | pages [9] -->
Team#2315379

<!-- b000142 | caption | pages [9] -->
Figure 4.Grid partitioning

<!-- b000143 | heading | pages [9] -->
5.3.2 Determination of decision variables and constraints

<!-- b000144 | prose | pages [9] -->
In section 5.2.1, we have divided 36 areas according to the distribution of wild animals.

<!-- b000145 | prose | pages [9] -->
(1)First, we need to construct a 0-1 planning model to determine the building use of these 36 areas. Set the decision variables as follows:

<!-- b000146 | caption | pages [9] -->
Table 3. Decision variables and their meanings

<!-- b000147 | prose | pages [9] -->
Decision variables Definitions Conservation measures for the wildlife species in the j-th geographic area. When ��=1, it means that the i-th species takes conservation measures in the j-th region, and when ��=0, ( 0, 1) X X or  j j it means that the ith species does not take conservation measures in the j-th region. The following decision variables��, ��and ��are the same.

<!-- b000148 | prose | pages [9] -->
( 0, 1) Y Y or  Whether to build a hunting and gathering restricted area in the j-th geographical area. j j ( 0, 1) Z Z or  Whether to build a tourism development zone in the j-th geographical area. j j Whether to establish an agricultural expansion area in the j-th region. If an agricultural ( 0, 1) W W or  expansion area is built on this site, it should occupy no more than 50% of the area in order j j to ensure sufficient area for animals to survive.

<!-- b000149 | prose | pages [9] -->
In different geographical areas, only one construction use can be selected, e.g. If an area is used to build a protected area, then it cannot also be used to build a hunting area, for any equal j,that is:

<!-- b000150 | prose | pages [9] -->
(5) 1 X Y Z W     j j j j Since the main purpose of the Maasai Mara National Park is to protect wildlife, the number of protected areas should be greater than the number of other areas, that is:

<!-- b000151 | prose | pages [9, 10] -->
 36 36   X Y   j j  1 1 j j    36 36   (6) X Z   j j  1 1 j j    36 36   X W   j j  1 1 j j   (2)First we need to calculate the approximate ecological value ��of different areas in Figure 4 according to the calculation method of ecological benefits in section 5.2, and then determine which building use is suitable for that geographical area according to the value of ��.Specifically, when ��in the jth area is greater than 0.5, it means that this area has a high animal density and is suitable for the construction of a protected area;When 0.4 ≤��≤0.5 , the animal density is slightly lower and suitable for building tourist areas for people to enjoy;When ��< 0.2 , a portion of the area in this region is then considered for expansion agriculture.Translate this into the constraint that, for any equal j, that is.

<!-- b000152 | furniture | pages [10] -->
Page 10 of 25

<!-- b000153 | furniture | pages [10] -->
Team#2315379

<!-- b000155 | prose | pages [10] -->
When : 0.5 V  x 1 X  j (7) , , 0 Y Z W  j j j When 0.4 : 0.5 V   x 1 X Y   j j (8) , 0 Z W  j j When 0.2 : 0.4 V   x 1 X Y Z    j j j (9) 0 W  j When : 0.2 V  x 1 X Y Z W (10)     j j j j (3) In addition, the number of tourists in the tourist area should be limited to avoid excessive numbers disturbing the wildlife habitat. Kenya Tourism Board data shows that the number of tourists visiting the Masai Mara is about 150,000 per year [6], about 410 people per day. And about 40 people stay in the hotel every day. Assuming that the hotels are evenly distributed across the tourist areas, we can assume that 40 people visit each tourist area. Based on the above data, we can obtain the following constraint on the number of people in the tourist areas:

<!-- b000156 | prose | pages [10] -->
36  (11) *40 410 Z  j 1 j  (4) At the same time, we also need to balance the interests of local residents, so we need to set the relevant variables as follows:

<!-- b000157 | caption | pages [10] -->
Table 4. Variable and its meaning

<!-- b000158 | prose | pages [10] -->
Variables Definitions Ecological benefit from building the j-th protected areas V jx Economic value from building hunting areas, tourist areas, V , V , V y z w agricultural expansion areas According to the description in (2), ��will be different for different regions. To simplify the calculation, we assume that ��, ��, and ��are the same for the remaining regions of the same construction type. Where ��, ��, and ��(economic benefits) are calculated as described in detail in section 5.2.Substituting the relevant data for Kenya 2022, the value per unit area of agricultural area is calculated to be $4,786,900/year, the value per unit area of hunting area is $151,000/year and the daily consumption per capita is $364,.Combining the daily number of visitors per tourist area and the area of the different areas, we can calculate that:

<!-- b000159 | furniture | pages [11] -->
Page 11 of 25

<!-- b000160 | furniture | pages [11] -->
Team#2315379

<!-- b000161 | prose | pages [11] -->
��= $7.55 million per year,��= $13.286 million per year,��= $11,967.25 million per year Considering that some of ��, ��, ��will be allocated to the government and some to the local residents, we assume that �1�, �1�, �1�are the profits allocated to the government and �2�, �2�, �2�are the profits allocated to the local residents,that is:

<!-- b000162 | prose | pages [11] -->
* V V r  1 1 * V V r  (12) 2 2 1 r r   1 2 Where, �1, �2 are the ratio of profit distribution received by the government and the ratio of profit distribution received by the residents, respectively. Referring to the local tax rate, �1, is about 0.2 and �2 is about 0.8. In order to balance the interests of the local residents, we need to keep the income of the residents no less than the per capita income level. Searching for information[6], we got that the per capita income in Kenya is about $2082 per year, that is.  V 2 i , , i y z w  (13) 2082  36  P j 1 j  Where, ��is the number of people in the j-th geographic area, which is obtained by referring to the local population distribution.

<!-- b000163 | heading | pages [11] -->
5.3.3 Determination of objective function

<!-- b000164 | prose | pages [11] -->
The nature reserve was established to protect the animals and natural resources of the area, so we set up an objective function to maximize the ecological benefits, that is:

<!-- b000165 | prose | pages [11] -->
36  (14) max X V j jx 1 j Furthermore, in order to balance the interests of the inhabitants of the area, we should also make the economic benefits of the protected area and its surroundings as large as possible. We assume that the cost of building different subdivisions is the same, that is:

<!-- b000166 | prose | pages [11] -->
36  (15) max ( ) Y V Z V W V   j y j z j w 1 j 

<!-- b000167 | heading | pages [11] -->
5.4 Solution of the model

<!-- b000168 | prose | pages [11] -->
We used lingo for solving, the specific solution algorithm is as follows： Since we set up a dual-goal planning model, the solution results show that there is no optimal solution, and the better solution has three options, which are (the numbers indicate the number of subdivisions used for the corresponding construction purposes)：

<!-- b000169 | caption | pages [11] -->
Table 5. The optimal solution obtained by solving

<!-- b000170 | prose | pages [11, 12] -->
Construction use / Quantity Scenario1 Scenario2 Scenario3 Tourist area 8 9 10 Agricultural expansion areas 11 12 10 Hunting area 6 2 4 Wildlife Sanctuary 11 13 12 6.Problem 2

<!-- b000171 | furniture | pages [12] -->
Page 12 of 25

<!-- b000172 | furniture | pages [12] -->
Team#2315379

<!-- b000174 | heading | pages [12] -->
6.1 Problem analysis

<!-- b000175 | prose | pages [12] -->
In this question, we need to build a comprehensive evaluation model to determine which zoning strategy is best. We need to analyze which strategy has the lowest possible human-animal interaction and the greatest possible economic benefits within the reserve and surrounding area.6.2. Minimum interaction model based on Dijkstra's algorithm.

<!-- b000176 | heading | pages [12] -->
6.2 Preparation of the model

<!-- b000177 | prose | pages [12] -->
First, we need to determine what specific types of interactions with animals there are. In this paper, the types of animal-human interactions that we need to consider are shown in the following table：

<!-- b000178 | caption | pages [12] -->
Table 6. Four kinds of interaction between humans and animals

<!-- b000179 | prose | pages [12] -->
Behavior Explanation

<!-- b000180 | prose | pages [12] -->
Tourist Excessive disturbance by tourists can also have a negative impact on the ornamental animals, for example by disturbing their rhythm of life or causing them to animals become frightened. In addition, attacks by animals on people staying or / Animal attacks camping near the reserve have been known to occur. on tourists Some sanctuaries may raise or feed animals in captivity to ensure their Artificial rearing health and survival in order to facilitate visitors' viewing of animals. and feeding However, such practices may also lead to animals becoming dependent on humans and losing their natural survival instincts. Animal attacks on In the Masai Mara, there are often cases of animal attacks causing crop humans or damage, livestock loss and human casualties in the Masai Mara National domesticated Park. livestock

<!-- b000181 | prose | pages [12] -->
Hunting and Some illegal hunting, poaching, and vandalism can cause wildlife poaching populations to plummet.

<!-- b000182 | prose | pages [12] -->
From the above table, when animal habitats are too close to where people live, there may be a range of negative impacts. Therefore, we used the distance assessment method to measure the impact of human-animal interactions. We use the relative distances of these four zones to calculate human-animal interactions and use Dijkstra's algorithm to build a model to find the zoning scheme with the greatest total distance between each animal protection area and each human activity area (i.e., the least possibility of interaction), thus reducing the possibility of wild animals attacking humans as well as domestic animals.

<!-- b000183 | prose | pages [12] -->
As an example, the shortest distance between a wildlife sanctuary and a tourist area is defined as follows.

<!-- b000184 | prose | pages [12, 13] -->
minDistance = min dpq(pWildlife Sanctuary & qTourist Area) (16) Where,p is a point on the boundary of Wildlife Sanctuary and q is a point on the boundary of Tourist Area.Referring to Scenario 1, the shortest distances between the wildlife sanctuary and the tourism area before and after the rezoning of the Masai Mara Nature Reserve are shown in Figures 5 and 6.

<!-- b000185 | furniture | pages [13] -->
Page 13 of 25

<!-- b000186 | furniture | pages [13] -->
Team#2315379

<!-- b000188 | caption | pages [13] -->
Figure 5. Initial state minimum distance

<!-- b000189 | caption | pages [13] -->
Figure 6. Scenario 1 shortest distance

<!-- b000190 | prose | pages [13] -->
When the minimum distance between Wildlife Sanctuary and Tourist Area is increased, the chances of contact between visitors and some dangerous large wildlife are reduced.The likelihood of these animals attacking visitors is subsequently reduced, and the impact of negative wildlife and visitor interactions is mitigated to some extent.

<!-- b000191 | heading | pages [13] -->
6.2.2 Establishment of the model

<!-- b000192 | prose | pages [13] -->
First, we abstract protected areas as an undirected graph, with each type of protected area as a node in the graph and the grid edge length d denoting the distance between adjacent protected areas. Then, the distance between different protected areas is measured by calculating the shortest path length between nodes, and thus assessing the impact of human-animal interactions between different protected areas. The specific modeling process is as follows.

<!-- b000193 | prose | pages [13] -->
(1) Construction of undirected graphs.

<!-- b000194 | prose | pages [13] -->
Suppose the protected areas are divided into four types: nature reserve (��), hunting area (��), agricultural area (��) and tourist area (��), which can be represented as nodes in the undirected graph G(V, E), V = { ��，��，��，��} ，and E denotes the set of edges, indicating the connection relationship between nodes. The weights of edges can represent the distance between nodes, which can be determined according to the actual situation. For the convenience of modeling, we assume that the edge lengths between adjacent nodes are the same, and it’s d.

<!-- b000195 | prose | pages [13] -->
(2) Consider the impact of interaction.

<!-- b000196 | prose | pages [13] -->
Considering the influence of human-animal interaction, different weights can be assigned to the edges between different nodes, and the weights can indicate the intensity of human-animal interaction. According to some information we have reviewed, we set the weights between each type of zones as shown in the table. The larger the weight, the farther the distance between these two zones is.

<!-- b000197 | furniture | pages [14] -->
Page 14 of 25

<!-- b000198 | furniture | pages [14] -->
Team#2315379

<!-- b000199 | caption | pages [14] -->
Table 7. Weights between different regions

<!-- b000200 | prose | pages [14] -->
Nature Reserves Hunting area Agricultural area Tourist area Nature Reserves 1 0.5 0.8 Hunting area 1 0.2 0.4 Agricultural area 0.5 0.2 0.6 Tourist area 0.8 0.4 0.6 (3) Modeling of human-animal interactions.

<!-- b000201 | prose | pages [14] -->
Considering that the intensity of human-animal interaction may be influenced by several factors, a linear regression model can be used to model human-animal interaction, and the lower the intensity of the interaction, the better. The equation is as follows.

<!-- b000202 | prose | pages [14] -->
3   d w b w P    (17) ij ij n n i j E  （，） n 1  Where, P denotes the intensity of human-animal interaction, E denotes the set of edges of the undirected graph composed of protected areas, i, j denote two adjacent nodes in the undirected graph, respectively, d(i, j) denotes the distance between node i and node j, which can be expressed using the shortest path length, w(i, j) denotes the weight between node i and node j, which is used to reflect the influence of human-animal interaction. b1 ~ b3 denote coefficients of other factors, and w1 ~ w3 denote the weights of other factors. These other factors include environmental factors, climatic factors, and population density.

<!-- b000203 | prose | pages [14] -->
(4) Calculate the shortest path We use Dijkstra's algorithm to calculate the shortest path length between different nodes by the following procedure.

<!-- b000204 | heading | pages [14] -->
Algorithm 2: Dijkstra’s Algorithm

<!-- b000205 | prose | pages [14] -->
Input：u; v; s; S; V

<!-- b000206 | prose | pages [14] -->
Output：new_d(v)&d(v’)

<!-- b000207 | prose | pages [14] -->
1.Let S be the set of explored nodels. do For each uS,we store a distance d(u) 2.

<!-- b000208 | prose | pages [14] -->
3.Initially S = {s} and d(s) = 0 4.While S V

<!-- b000209 | prose | pages [14] -->
Select a node vS with at least one edge from S for which 5.

<!-- b000210 | prose | pages [14] -->
6. d’(v) = mine = (u,v):uS d(u)+le is as small as possible

<!-- b000211 | prose | pages [14] -->
7. Add v to S and define d(v) = d(v’)

<!-- b000212 | heading | pages [14] -->
8. EndWhile

<!-- b000213 | prose | pages [14] -->
Repeat steps 4 and 5 until all nodes are marked as visited, or the target node is found.

<!-- b000214 | furniture | pages [15] -->
Page 15 of 25

<!-- b000215 | furniture | pages [15] -->
Team#2315379

<!-- b000216 | heading | pages [15] -->
6.2.3 Solution of the model

<!-- b000217 | prose | pages [15] -->
We used MATLAB to solve the solution, and the results showed that scenario2 resulted in the least interaction between humans and animals, at which point the specific partition is shown in Figure 7.

<!-- b000218 | caption | pages [15] -->
Figure7.The zoning situation of scenario 2

<!-- b000219 | heading | pages [15] -->
6.3 Economic impact evaluation model

<!-- b000220 | prose | pages [15] -->
According to the calculation of 5.3.2, it is obtained that economic value from building hunting areas, tourist areas, agricultural expansion areas is： ��= $7.55 million per year,��= $13.286 million per year,��= $11,967.25 million per year Then we substitute the data for Kenya 2022 to get the value of a unit area of a nature reserve (1km2) of $17,242,130,000, that is, the ecological value (as distinguished from the ecological benefits) of a reserve ��is $862.1 million.

<!-- b000221 | prose | pages [15] -->
The formula for calculating the total economic value ��for different scenarios is as follows:

<!-- b000222 | prose | pages [15] -->
(18) * * * * E Q V Q V Q V Q V     i ix X iy y iz z iw w Where,���,���,���,���are the number of different partitions to be built when implementing different scenarios, respectively.

<!-- b000223 | prose | pages [15] -->
Substituting the results of Problem 1, the economic values obtained for the different scenarios are obtained as follows.

<!-- b000224 | caption | pages [15] -->
Table 8. The economic value of different schemes

<!-- b000225 | prose | pages [15] -->
Plan Economic Value Scenario1 141274.438million Scenario2 154948.974million Scenario3 130180.760million In terms of results, option 2 causes the greatest economic gain. And from the calculations in 6.2, it is concluded that scenario II causes the least negative human-animal interaction. Therefore, Option 2 is the best policy.

<!-- b000226 | furniture | pages [16] -->
Page 16 of 25

<!-- b000227 | furniture | pages [16] -->
Team#2315379

<!-- b000228 | prose | pages [16] -->
7.Problem 3

<!-- b000229 | heading | pages [16] -->
7.1 Problem analysis

<!-- b000230 | prose | pages [16] -->
In this problem, we need to measure the change in the Maasai Mara Park as a result of the change in policy. First, we need to determine the general situation of some industries before the implementation of the policy and then, based on that, predict the changes brought by the policy implementation. Then, we also need to analyze the impact of some factors, such as the uncertainty that the new crown epidemic may bring. Finally, we will analyze the possible impact on the whole national economy brought by the policy implementation.7.2 Long-term development of protected areas under optimal policy.

<!-- b000231 | heading | pages [16] -->
7.2.1 Changes in tourism revenue

<!-- b000232 | prose | pages [16] -->
Following the implementation of the policy, the different areas of the Masai Mara will function differently than before. As we mentioned in 6.3.2, the increased distance between the core reserve and areas where tourism is developing, including some tourist accommodation hotel sites, will lead to a reduction in some possible wildlife attacks on tourists, which will, in turn, attract more people to the area to some extent. The most intuitive manifestation of this increase in visitors is the increase in tourism revenue. To describe the relationship more accurately between the number of tourists and tourism revenue, we collected data from 2010-2019 (we will conduct further analysis in the next section as tourism is affected by the COVID-19 pandemic in 2020), and these specific data are presented in the Appendix. We ran linear regressions with the number of tourists as the independent variable x and tourism revenue as the dependent variable y, and non-linear regressions fitted with quadratic curves, respectively.

<!-- b000233 | caption | pages [16] -->
Figure 8. The fitting effect of different equations

<!-- b000234 | prose | pages [16] -->
The fitting results show that the R-squared of the quadratic curve fitting equation is 0.926 and the R-squared of the univariate linear regression equation is 0.912, which shows that the quadratic nonlinear regression is better. In addition, the results of the parameter test showed that the coefficients of the regression equations all passed the test. The result of the fit is.

<!-- b000235 | prose | pages [16, 17] -->
2 (19) 2979420 37718 122.9 y x x    The Kenya Tourism Board reports that the Maasai Mara, Kenya's most well-known national park, is the number one destination for all people traveling to Kenya, so we assume that the number of people traveling to Kenya after the policy is implemented will increase by 1% compared to previous years (previously it increased by about 0.3% per year) Using 2019 figures (1.762 million visitors and $167.8 million in tourism revenue) as the baseline, without the impact of the COVID-19 pandemic, is approximately 1.78 million, 1.797 million, and 1.815 million tourists in the next three years. Substituting into the regression equation, the tourism revenue at this point is $159.79 million, $170.193 million, and $182.205 million, respectively. Compared to the tourism revenue in 2019, a relatively large increase was achieved.

<!-- b000236 | furniture | pages [17] -->
Page 17 of 25

<!-- b000237 | furniture | pages [17] -->
Team#2315379

<!-- b000239 | heading | pages [17] -->
7.2.2 Changes in agriculture

<!-- b000240 | prose | pages [17] -->
Agriculture in this context is broadly defined as agriculture (including livestock farming). Animal attacks resulting in crop damage, livestock losses and human casualties are not uncommon in the Masai Mara National Park. With the implementation of the policy, the distance between agricultural areas and protected areas will be reduced to some extent, thus reducing losses due to situations such as wildlife attacks on livestock.

<!-- b000241 | heading | pages [17] -->
7.2.3 Impact of the COVID-19 pandemic on tourism

<!-- b000242 | prose | pages [17] -->
We collected data on the number of travelers to Kenya in the three years prior to the new crown epidemic (2017-2019) and the three years of the COVID-19 pandemic (2020-2022), as shown in the table 9.

<!-- b000243 | caption | pages [17] -->
Table 9. The number of travelers in Kenya before and after the COVID-19 pandemic

<!-- b000244 | prose | pages [17] -->
Number of visitors Number of visitors Year Year (million) (million) 2017 2020 177.8 77.4 2018 2021 178.4 65.2 2019 2022 176.2 130 We conducted t-tests on the data before and after the New Crown outbreak and the results were as follows.

<!-- b000245 | caption | pages [17] -->
Table 10. T-test result

<!-- b000246 | prose | pages [17] -->
Group (mean±standard deviation) t p Pre-covid-19 (n=3) After the covid-19 (n=3) Number of 177.47±1.14 90.87±34.44 4.354 0.049* tourists * p<0.05 ** p<0.01 The test results show that the COVID-19 pandemic shows a 0.05 level of significance for the number of tourists (t=4.354, p=0.049), as well as specific comparative differences that show that the mean value before the COVID-19 pandemic (177.47), will be significantly higher than the mean value after the new crown epidemic (90.87).

<!-- b000247 | prose | pages [17] -->
This shows that some force majeure factors can cause some impact on the results of our long-term trend prediction, such as the withering of tourism due to pandemic diseases.

<!-- b000248 | heading | pages [17] -->
7.2.4 Long-term impact of policy implementation

<!-- b000249 | prose | pages [17, 18] -->
Our proposal guarantees the ecological benefit of the area, the economic benefit of the local population and at the same time minimizes the negative interaction between humans and animals. Once the number of animal attacks on people decreases, it means that the surrounding agriculture and animal husbandry will develop faster, the number of tourists coming to the area will increase, and the income from tourism will increase. The increased value of these industries will drive the country's economy, which in turn will generate more money to invest in wildlife conservation, creating a virtuous cycle.

<!-- b000250 | furniture | pages [18] -->
Page 18 of 25

<!-- b000251 | furniture | pages [18] -->
Team#2315379

<!-- b000253 | caption | pages [18] -->
Figure 9. The long-term impact of the policy

<!-- b000254 | heading | pages [18] -->
7.3 Model Migration: Yellowstone National Park

<!-- b000255 | heading | pages [18] -->
7.3.1 Feasibility analysis of model migration

<!-- b000256 | prose | pages [18] -->
We targeted Yellowstone National Park, the world's first national park, for migration in our model.By collecting relevant data from Yellowstone National Park and the Masai Mara, we could then determine the feasibility of model migration.

<!-- b000257 | caption | pages [18] -->
Table 11. Yellowstone National Park & Masai Mara

<!-- b000258 | prose | pages [18, 19] -->
Yellowstone National Park Masai Mara Land area Approx. 8983.49 km2 Approx. 1800 km2 The border of Wyoming, Oloomimutiek Gate Location Montana and Idaho, USA Masai Mara,Narok Establishment time 1972.3.1 ----- Climate Highland mountain climate Tropical grassland climate Level National level World Natural Heritage, U.S. National Parks Ticket Price $25/car, $12/person 1400Ksh/person Opening time Open basically all year round Open year-round, all day 69 species of mammals, inhabited by The five beasts of Africa: American bison, white-tailed deer, elephant,lion,leopard,rhinoceros gray wolves, brown bears, moose, Resources andbuffalo.The uncountable horse deer,bighorn sheep, antelope,antelope,North American antelopes,giraffes, hippos, grizzly bears, cougars and other baboons and wolves. wildlife. ·Data Source：https://yellowstone.net/ & www.maasaimara.com/ As we can see from the table above, Yellowstone National Park and the Masai Mara have many similarities in many ways. And they have their own characteristics. This lays the foundation for our migration model.

<!-- b000259 | furniture | pages [19] -->
Page 19 of 25

<!-- b000260 | furniture | pages [19] -->
Team#2315379

<!-- b000262 | heading | pages [19] -->
7.3.2 Model improvement and solution

<!-- b000263 | prose | pages [19] -->
Through the above analysis, we verified the feasibility of applying our model in Yellowstone National Park.The topographic conditions and species distribution in the area are shown in Figures 10 and 11.

<!-- b000264 | caption | pages [19] -->
Figure 10. Yellowstone National Park Wildlife Distribution(Left)

<!-- b000265 | caption | pages [19] -->
Figure 11. Topography of Yellowstone National Park(Right)

<!-- b000266 | prose | pages [19] -->
Given the differences in economy, environment, and biodiversity between Yellowstone National Park and the Masai Mara region, we modified the constraints in question 1 as follows.

<!-- b000267 | prose | pages [19] -->
(1) For constraint (3), we should consider the average income of U.S. citizens near the location of Yellowstone National Park. Since Yellowstone National Park is located mainly in Wyoming and partly in Montana and Idaho. We consulted to obtain the 2020-2021 per capita incomes for these three states：

<!-- b000268 | caption | pages [19] -->
Table 12. 2020-2021 per capita incomes

<!-- b000269 | prose | pages [19] -->
State 2020 2021 Wyoming $61855 $65627 Montana $53361 $56672 Idaho $48759 $51379 ·Data Source：https://www.bea.gov/data/income-saving/personal-income-by-state;

<!-- b000270 | prose | pages [19] -->
http://data.un.org/Default.aspx;

<!-- b000271 | prose | pages [19, 20] -->
In addition, the U.S. per capita income in 2021 is $65,133.7, given that approximately 96% of the land area of Yellowstone National Park is located within Wyoming ($65,627). Therefore, constraint (3) is modified to become：  V 2 i , , i y z w  (20) 65627  36  P j 1 j  （2）For constraint (4), we reconsider the number of visitors to Yellowstone National Park. 2018-2020, Yellowstone National Park receives 4.11 million, 4.02 million, and 4.08 million visitors for the year, respectively. Taking the average value, the calculation yields an average daily reception of 10,904 people in Yellowstone National Park. Based on the above analysis, we obtain： 36  *40 10904 (21) Z  j 1 j  In this way, we have developed a model on the integrated use of natural resources in Yellowstone National Park.The final partition of Yellowstone National Park is shown in Figure.13, using the same method.

<!-- b000272 | furniture | pages [20] -->
Page 20 of 25

<!-- b000273 | furniture | pages [20] -->
Team#2315379

<!-- b000275 | caption | pages [20] -->
Figure 13. Yellowstone National Park Zoning

<!-- b000276 | prose | pages [20] -->
We have divided Yellowstone National Park into five districts, which are：Mammoth Hot Spring District ；Geyser Fountain District ；Yellowstone Lake District ；Canyon District ； Roosevelt District.

<!-- b000277 | prose | pages [20] -->
In response to the differences in management policies between Yellowstone National Park and the Masai Mara, we have analyzed the following possible reasons. ✧Great Animal Migration ：Every year from June to October, the Masai Mara and the Serengeti Savannah in Tanzania undergo the Great Migration of animals.Similar mass migrations do not occur in Yellowstone National Park due to its closed nature. ✧Economic Development：According to the latest statistics released by the World Bank 2022, Kenya's GDP in 2021 will be $110.347 billion, an increase of 9.62% from 2020, placing it 61st in the world rankings. The U.S. ranks first with a GDP of $22.94 trillion, up 6 percent year-on- year.As a result, Yellowstone National Park can focus more attention on wildlife conservation. ✧Historical origins：Yellowstone National Park, the world's first national park, was officially named on March 1, 1872.The Masai Mara Reserve was established in 1961.In contrast, Yellowstone National Park, with its long history, has relatively more mature laws and regulations and management experience. 8.Problem 4 We wrote a non-technical report for the Kenyan Tourism and Wildlife Committee.

<!-- b000278 | furniture | pages [21] -->
Page 21 of 25

<!-- b000279 | furniture | pages [21] -->
Team#2315379

<!-- b000280 | prose | pages [21] -->
Dear Kenyan Tourism and Wildlife Committee：

<!-- b000281 | prose | pages [21] -->
Kenya is recognized as the world's best country to see African wildlife, in the Masai Mara Game Reserve, Africa's five hegemon — African elephants, rhinoceros, bison, lions and cheetahs can be seen everywhere; in Lake Nakuru National Park, red flamingos soar in flocks in the blue sky and blue water; in Amboseli National Park, Hemingway's Mount Kilimanjaro is reflected in the land of green grass ...... which is most famous for the annual animal migration from mid-June to September.

<!-- b000282 | prose | pages [21] -->
In addition to the annual animal migration, Kenya is home to majestic mountains, white sandy beaches, colorful equatorial nature and customs, and a pleasant spring-like climate that attracts visitors from all over the world.

<!-- b000283 | prose | pages [21] -->
The Masai Mara, one of Kenya's most famous wildlife reserves, is famous for its magnificent grasslands and rich variety of wildlife. Making full use of the resources of the nature reserve and developing tourism while protecting wildlife and at the same time avoiding damage to the interests of people in the surrounding areas are issues that need to be considered.

<!-- b000284 | prose | pages [21] -->
We first divided the different geographical areas according to the current distribution of wildlife in the Maasai Mara Reserve. We divided these geographic areas into four uses, which are：

<!-- b000285 | prose | pages [21] -->
Type.1 For the construction of nature reserves.

<!-- b000286 | prose | pages [21] -->
Type.2 For the construction of hunting and gathering areas.

<!-- b000287 | prose | pages [21] -->
Type.3For the construction of tourist development areas.

<!-- b000288 | prose | pages [21] -->
Type.4For the construction of agricultural expansion areas.

<!-- b000289 | prose | pages [21] -->
A model was developed and calculations were made to derive construction plans for different geographical areas. It was finally obtained that the resources of Masai Mara are fully utilized when the following scheme is adopted. That is, the number of blocks of the four types mentioned above are: 13,2,9,12.

<!-- b000290 | furniture | pages [22] -->
Page 22 of 25

<!-- b000291 | furniture | pages [22] -->
Team#2315379

<!-- b000292 | prose | pages [22] -->
The scenario is extremely valuable as it takes into account the original pattern of the Masai Mara and the level of economic development of the area.The specific implementation of the program is referenced in the following chart.

<!-- b000293 | prose | pages [22] -->
The economic value of wildlife conservation ecological value can be maximized under this plan, which takes into account the ecological value of wildlife conservation.

<!-- b000294 | prose | pages [22] -->
Based on the construction plan, we propose the following recommendations to help better balance the interests between humans and animals：

<!-- b000295 | prose | pages [22] -->
1.Increase community cooperation and participation with local people to ensure that they derive more economic and social benefits from the resources and tourism of the reserve.

<!-- b000296 | prose | pages [22] -->
2.Develop tourism planning and management strategies to ensure that visitors adhere to the visitor code of conduct and that appropriate safety measures are taken to protect wildlife and the visitors themselves.

<!-- b000297 | prose | pages [22] -->
3.The policies and management strategies adopted must be in line with the relevant regulations and policies of the protected areas, such as no deforestation of primary forests, no exploitation of mineral resources, etc.

<!-- b000298 | prose | pages [22] -->
4.The policies and management strategies adopted must balance wildlife and natural resource conservation with the livelihoods of the inhabitants, e.g. no total closure and no total opening.

<!-- b000299 | prose | pages [22] -->
Yours sincerely #2315379 2023.2.20

<!-- b000300 | furniture | pages [23] -->
Page 23 of 25

<!-- b000301 | furniture | pages [23] -->
Team#2315379

<!-- b000302 | heading | pages [23] -->
9. Sensitivity analysis of the model

<!-- b000303 | prose | pages [23] -->
The minimum interaction model and economic impact evaluation model based on Dijkstra’s algorithm in this paper is established in an extremely ideal situation. Since reality is often less than ideal, especially in Africa, in order to ensure that the evaluation model is more objective, relevant, independent, practical and scientific, it is necessary to consider the occurrence of special cases. We integrated the frequency of each special case in the continent and chose to consider the impact of the four cases of food crisis, natural disaster, policy change and financial crisis on the model, and we need to discuss the impact of the relevant weight vectors on the feasibility of establishing hydropower plants.

<!-- b000304 | prose | pages [23] -->
We made a total of four special cases for comparison, and we only need to change the weights of the relevant factors appropriately, and to ensure the fairness of the experiment, we only change them in a small way (no more than 0.1 up or down). Here, we test by adjusting up 0.1 weight group of agricultural value, adjusting down 0.1 weight group of natural value, adjusting down 0.1 weight group of hunting value, and adjusting down 0.1 weight group of tourism value, and the results are shown in Table 13.

<!-- b000305 | caption | pages [23] -->
Table 13. The economic value of each scheme after reducing the weight

<!-- b000306 | prose | pages [23] -->
Special Events Scenario 1 Scenario 2 Scenario3 Food crisis 1169270.29 1341207.52 1235496.24 Natural Disasters 1064894.04 1220047.77 1126019.24 Policy Change 1146495.89 1315332.72 1214462.64 Financial crisis 1136358.51 1305004.51 1202584.02 From the table above, it can be seen that the economic value of Scenario 2 is the largest regardless of which special case occurs, and at the same time, we find the model fit superiority of Option 2 for each special case, and the results are shown in the Table 14.

<!-- b000307 | caption | pages [23] -->
Table 14. Model goodness of fit of Scheme 2 in different special cases

<!-- b000308 | prose | pages [23] -->
Food crisis Natural Disasters Policy Change Financial crisis 0.879086 0.979658 0.999959 0.955990 R2 We can see that the R2 for each case is greater than 0.8 , the model fit is good and our model is stable. Conclusion: The influence of the weights of these factors on our model is small, and our model is stable without being affected by special cases. 10.Evaluation and extension of the model

<!-- b000309 | heading | pages [23] -->
10.1 Advantages

<!-- b000310 | prose | pages [23] -->
After careful examination, our model has the following advantages： ✧Our models effectively achieved all of the goals.An comprehensive model has been established for reallocating resources in the Masai Mara that balances the interests of wildlife and people. ✧Its main advantage is its tremendous scalability and the incorporation of all factors into a unified, robust framework. ✧The visualization work is done very well by us, such as the distribution of resources in the Masai Mara region and some structured schematics. Boring data may be able to reflect the law, but not as intuitive as so many images.

<!-- b000311 | furniture | pages [24] -->
Page 24 of 25

<!-- b000312 | furniture | pages [24] -->
Team#2315379

<!-- b000313 | prose | pages [24] -->
✧In addition, our model takes into account the time dimension and has good scalability.

<!-- b000314 | heading | pages [24] -->
10.2 Limitations and Extension of the model

<!-- b000315 | prose | pages [24, 25] -->
Our model has the following limitations and related improvements： ✧The collection of data for part of the Masai Mara region was very difficult and we had to use data from Kenyan countries as a proxy, which reduced the accuracy of the model to some extent. ✧Our model is extremely relevant and can be widely used in large wildlife reserves around the world. In addition, we have applied the model to the Yellowstone Park in the United States with good results in Problem 3. 11.Reference [1] Wishitemi B E , Momanyi S O , Ombati B G , et al. The link between poverty, environment and ecotourism development in areas adjacent to Maasai Mara and Amboseli protected areas, Kenya[J]. Tourism Management Perspectives, 2015. [2] Holland K K , Larson L R , Powell R B , et al. Impacts of tourism on support for conservation, local livelihoods, and community resilience around Maasai Mara National Reserve, Kenya[J]. Journal of Sustainable Tourism. [3] Ogutu J O , Owen-Smith N , Piepho H P , et al. Continuing wildlife population declines and range contraction in the Mara region of Kenya during 1977–2009[J]. Journal of Zoology, 2011, 285(2):99-109. [4] XUE F. Network selection algorithm for nature reserve planning and design [D]. Fujian Agriculture and Forestry University, 2014. (in Chinese with English abstract) [5]Tu W H. Study on static and dynamic optimization model of Quanzhou Bay Reserve [D]. Fujian Agriculture and Forestry University,2019. [6]Li, W., Buitenwerf, R., Munk, M., Bøcher, P. K., & Svenning, J. C. (2020).Deeplearning base d highresolution mapping shows woody vegetation densification in greater Maasai Mara ecosyst em. Remote Sensing of Environment, 247, 111953. [7] The Wildlife Conservation and Management Act, 2013. Republic of Kenya, Kenya Gazette Supplement No. 181 (Acts No. 47), 2013. [8] The Wildlife Conservation and Management Act (No. 47 of 2013). Legal Notice No. 155. Republic of Kenya, Kenya Gazette Supplement No 141 (Acts No. 47), 2020 12.Appendix

<!-- b000316 | furniture | pages [25] -->
Page 25 of 25

<!-- b000317 | furniture | pages [25] -->
Team#2315379

<!-- b000319 | heading | pages [25] -->
Appendix 1

<!-- b000320 | prose | pages [25] -->
Introduce: Tools and software Paper written and generated via Office 2019. Graph generated and calculation using MATLAB R2021b & Python 3.8. & Lingo17.0

<!-- b000321 | heading | pages [25] -->
Appendix 2

<!-- b000322 | prose | pages [25] -->
Introduce: Data_Industries(Unit: $ million, 10,000 people) Year Agricultural output Hunting output Tourism revenue Ecological output TouristsNumber 2010 200120 3892 96006 876483 162 2011 200730 3902 102359 862563 165 2012 205045 4056 122187 886616 170.1 2013 193612 4079 133560 891854 173.5 2014 185804 4088 134231 906923 174.2 2015 218125 4102 146124 907231 175.6 2016 230072 4123 145670 917559 176.2 2017 249057 4251 158720 917826 177.8 2018 248506 4198 159231 928042 178.4 2019 256200 4362 167800 938231 176.2 2020 263280 4532 83500 948317 77.4

<!-- b000323 | heading | pages [25] -->
Appendix 3

<!-- b000324 | heading | pages [25] -->
Introduce: ModelⅠ: Dijkstra Algorithm

<!-- b000325 | prose | pages [25] -->
function if i==s(j) [min,path]=dijkstra(w,start,terminal) ins=1; n=size(w,1); label(start)=0; f(start)=start; end for i=1:n end if i~=start end label(i)=inf; %Determine if there are relay vertices that end make the distance between them shorter, if end so update the distance and update the %sThe array holds the set of vertices precursor node already searched, initialized with only start if ins==0 s(1)=start; u=start; v=i; while length(s)<n if label(v)>(label(u)+w(u,v)) for i=1:n label(v)=(label(u)+w(u,v));

<!-- b000326 | prose | pages [25] -->
ins=0; f(v)=u;

<!-- b000327 | prose | pages [25] -->
for j=1:length(s) end if i==s(j) end ins=1; end
