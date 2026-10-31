# P-F-2016-44348-d3da2a69

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
44348

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
T1 ________________

<!-- b000005 | prose | pages [1] -->
T2 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T3 ________________

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
F1 ________________

<!-- b000010 | prose | pages [1] -->
F2 ________________

<!-- b000011 | prose | pages [1] -->
F3 ________________

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T4 ________________

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | title | pages [1] -->
F

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | heading | pages [1] -->
2016 MCM/ICM Summary Sheet

<!-- b000019 | title | pages [1] -->
Towards A Hopeful Journey

<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | prose | pages [1] -->
The world is witnessing the largest refugee crisis since the horrors of World War II. Modeling refugee immigration, which is crucial to tackle the problem, is an intricate issue that should embrace the sophistication of social interrelated systems, and take into the consideration of refugee crisis on local conditions. Concerning the structure of refugee crisis and the routes of migration, with the official data in 2014, we construct a refugee migration model and build a feedback system using network analysis methodology and Cellular automaton to make precise simulation aiming to help figure out a set of efficient policies.

<!-- b000023 | prose | pages [1] -->
In the first place, we establish a set of metrics to consider the determinant factors in refugee migrations so that we define our measures and indexes, after which we set the start points of six given routes as six nodes, and choose 14 countries where most refugees gather to be the nodes in Africa and Central East. With the assumption that the refugees migrate nearer and nearer to Europe, we divide the nodes into 4 layers based on the distances from node to node using cluster analysis. In that way, the refugees migrate within the layers.

<!-- b000024 | prose | pages [1] -->
After that, we assume that refugees get limited information and initially build a random migration model to determine the migrating factors between 2 nodes. And by Matlab simulation we get result indicating the main routes reaching Europe, but the numerical data is inconsistent with real data. Hence, we adjust our presumptions and revise our model.

<!-- b000025 | prose | pages [1] -->
xt, inspired by Gravity Model, we analyze the factors that affect the migration of refugees and integrate hem into a comprehensive attraction index. By collecting and calculating the statistics, we figure out the

<!-- b000026 | prose | pages [1] -->
eight between two nodes and the ratios of population distribution at the six start points 0.07:0.101:0.41:0.369:0.05), whose correlation coefficient with real data R=0.98. So we go on with revised model to unravel the optimal flow distribution under different conditions and the measurement of weight

<!-- b000027 | prose | pages [1] -->
om node to node backed by single-period simulation.

<!-- b000028 | prose | pages [1] -->
In addition, we expand the scale of nodes. Given that the feedback information of refugees in different periods and the maximum capacity in each node, we simulate the migration progress of refugees with Cellular Automaton and C++, and the ratios of 3 nodes are 0.0362:0.537:0.427, R=1. Therefore, we get to know about the influences of government and non-government organizations on refugee migration.

<!-- b000029 | prose | pages [1] -->
As for the policy, we attach significant importance to the empathy that the receiving population of each country must fit the present refugee condition. By scaling up our model, we find that the routes get saturated except for routes in North Africa and Central East, which may trigger the detention of refugees and eventually lead to illegal immigration. Meanwhile, we work out the relations between the stability and capacity of nodes by building a Cobweb Model. We find that the refugee flows tend to be more and more stable in nodes with bigger capacity. So we also propose to stabilize the flows, which contributes to better resource allocation and aid from GO and NGO.

<!-- b000030 | prose | pages [1] -->
Finally, we test the sensitivity of our model and conclude the strengths and weakness. The model is quite reliable in small scale but still needs advancement for larger and more precise simulation.

<!-- b000031 | furniture | pages [2] -->
Team #44348

<!-- b000032 | heading | pages [2] -->
Contents

<!-- b000033 | contents | pages [2] -->
1

<!-- b000034 | heading | pages [2] -->
Introduction

<!-- b000035 | furniture | pages [2] -->
page 1 of 18

<!-- b000036 | prose | pages [2] -->
2 Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Our work

<!-- b000037 | prose | pages [2] -->
2 Metrics

<!-- b000038 | prose | pages [2] -->
3

<!-- b000039 | heading | pages [2] -->
Notations and Descriptions

<!-- b000040 | prose | pages [2] -->
4

<!-- b000041 | heading | pages [2] -->
Fundamental Assumptions

<!-- b000042 | prose | pages [2] -->
5

<!-- b000043 | heading | pages [2] -->
The Gravitational Refugee Movement Model

<!-- b000044 | prose | pages [2] -->
2

<!-- b000045 | prose | pages [2] -->
2

<!-- b000046 | prose | pages [2] -->
3

<!-- b000047 | prose | pages [2] -->
4

<!-- b000048 | prose | pages [2] -->
5 Initial Nodal weight analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 5 Modiﬁed model added with gravitation theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 8 The relationship among the 6 routes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 8 Weight reanalysis and remodeling based on Gravity model . . . . . . . . . . . . . . . . . . . . . 5.2.2 8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.3 Analysis on each factor 8 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.4 An optimal route 10 Preposition Resource . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.5

<!-- b000049 | prose | pages [2] -->
6 Dynamic changes and Refugees

<!-- b000050 | prose | pages [2] -->
12

<!-- b000051 | prose | pages [2] -->
12 Dynamic simulation model of refugee migration based on Cellular Automaton . . . . . . . . . . . . . . 6.1 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 Non-paroxysmal factors 13 Accidental and irregular factors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.3

<!-- b000052 | prose | pages [2] -->
7 Scalability

<!-- b000053 | prose | pages [2] -->
8

<!-- b000054 | heading | pages [2] -->
The Policy Strategy with Cobweb Model

<!-- b000055 | prose | pages [2] -->
9 Inﬂuence of Exogenous Events

<!-- b000056 | prose | pages [2] -->
14

<!-- b000057 | prose | pages [2] -->
15

<!-- b000058 | prose | pages [2] -->
15

<!-- b000059 | prose | pages [2] -->
16 The outbreak of the diseases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.1 16 Terrorist attack . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9.2 16 How can our policy be resilient to Exogenous Events 9.3

<!-- b000060 | heading | pages [2] -->
10 Sensitivity Analysis

<!-- b000061 | heading | pages [2] -->
11 Evaluation of the Model

<!-- b000062 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | prose | pages [2] -->
16

<!-- b000064 | prose | pages [2] -->
17

<!-- b000065 | prose | pages [2] -->
17 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11.1 Strengths 17 11.2 Weakness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | heading | pages [2] -->
12 Future Work

<!-- b000067 | heading | pages [2] -->
References

<!-- b000068 | references | pages [2] -->
17

<!-- b000069 | references | pages [2] -->
17

<!-- b000070 | references | pages [2] -->
18

<!-- b000071 | furniture | pages [3] -->
Team #44348

<!-- b000072 | furniture | pages [3] -->
page 2 of 18

<!-- b000073 | references | pages [3] -->
1

<!-- b000074 | heading | pages [3] -->
Introduction

<!-- b000075 | prose | pages [3] -->
1.1

<!-- b000076 | heading | pages [3] -->
Background

<!-- b000077 | prose | pages [3] -->
One of the most stressful and potentially destabilizing social challenges facing Europe, or in a wider scope the whole world is the contemporary massive inﬂux of refugees and migrants, which sparks tremendous pressure in the receiving societies. One in every 122 people in the world is currently either a refugee, internally displaced or seeking asylum because the ”world is a mess”[1], according to the head of the UN’s refugee agency. Despite the restrictive policies of border control, the ﬂows and volumes of international migrants via various routines keep on scaling up and arriving in Europe disproportionately, as war, persecution and poverty continue to drive people away from their homes[2].

<!-- b000078 | caption | pages [3] -->
Figure 1: Total number of asylum applicants in European countries[3]

<!-- b000079 | prose | pages [3] -->
From the charts we can see that the asylum applicants in European countries are increasing strikingly over the past 5 years, leaving pressing concern.

<!-- b000080 | prose | pages [3] -->
Worse still, dozens of men, women and children have been killed especially while walking on railway lines on the long trek through Macedonia, Serbia, Croatia and Hungary as well as taking perilous voyages over the Mediterranean and Aegean seas in their desperation to ﬂee ravage and reach safety. , thus the true number of arrivals is a lot smaller than that of originals. According to the IOM (the International Organization for Migration), more than 3, 695 migrants are reported to have died trying to make the crossing in 2015[4]. Besides, among those who make way to their destinations, only a scarce proportion of requests are granted (32% in 2014)[5]

<!-- b000081 | prose | pages [3] -->
It has become strikingly crucial to deal well with the sophisticated refugee migration, which is a social process well structured and organized as a socio-spatial system[6, 7].

<!-- b000082 | prose | pages [3] -->
1.2 Our work

<!-- b000083 | prose | pages [3] -->
• We ﬁrst elaborate reasonable metrics on various factors that aﬀect the movement of refugees with statistics and graphs from FRAN and UNHCR Online database, then we design our own evaluation system to measure the factors that have been taken into consideration using clustering methodology. • And we devise a comprehensive migration model based on the Gravity model and I. S. Lawry model to look for an optimum refugee movement taking account the factors listed as well as dynamically adjusting with changing refugee conditions so that they can possibly move from their countries of origin into safe haven countries, which is validated by data from Eurostat Media and 2014 Statistical Yearbook. • Besides, we present a policy to prioritize the optimal migration using fuzzy comprehensive evaluation method. • Finally, we make a sensitivity analysis and discuss the merits and demerits of our model including an evaluation on the scalability.

<!-- b000084 | prose | pages [3] -->
2 Metrics

<!-- b000085 | prose | pages [3] -->
Herein are the main factors inﬂuencing the refugee ﬂows we take into consideration in our model.

<!-- b000086 | prose | pages [3] -->
• Safety index

<!-- b000087 | prose | pages [3] -->
Safety comes the ﬁrst in terms of migration. The recent surge of popular interest in and increasing public awareness of migrant deaths in the Mediterranean has turned the question of routine-related deaths into an

<!-- b000088 | furniture | pages [4] -->
Team #44348

<!-- b000089 | furniture | pages [4] -->
page 3 of 18

<!-- b000090 | prose | pages [4] -->
urgent matter. Reports of migrants threatened by smugglers, forcibly held by police or killed by criminals were rare in the past but have been increasingly heard in the last few years. This rise appears to have coincided with the growth in traﬃcking and smuggling , so too the wider use of guns.The increased instability on the way to haven countries make many migrants panicked and threatened. On the other side, the war condition in migratory place also contributes to this index. To propose a safety index becomes crucial.And the measurement of this index deﬁned as St

<!-- b000091 | prose | pages [4] -->
ij (from place i to place j) is calculated by our model in the following. • Environmental acceptance

<!-- b000092 | prose | pages [4] -->
The environmental acceptance Cij is undoubtedly signiﬁcant as refugees whom we assume to be sensible will compare the environment of the destination with that of the origin district i. Here, the environment acceptance is not merely referred to living environment or maximum capacity in country j but also include three main factors: (1) Resource Abundance. Food supply and water availability is the basis of living. Besides,access to primary health-care, referral systems, specialized health services, psychosocial-medical units and child health support are all in need to cope with wound and trauma in a desired destination. (2) Economic condition. The economic development level also determines whether the migrants can sur- vive on.Education and communications systems, commercial installations are needed for the functioning of a community. Many indicators such as social well-being of people, job opportunity and so on are considered. As economist Amartya Sen points out, ”economic growth is one aspect of the process of economic development.” In our model, we take GDP as the main indicator of economic condition. (3) Religious and culture acceptance. Diﬀerent communities have varied beliefs, which may lead to mis- understandings, conﬂicts and discrimination. Whether a culture is inclusive plays a role. In addition, as oﬃcial languages, customs, ceremonies etc. vary from place to place, which might be a burden for communication between migrants and local people, thus cultural acceptance Migration groups especially vulnerable ones, like children, unaccompanied and separated minors, pregnant and lactating mothers, the elderly, disabled and people look for a place of environmental acceptance, which has been limited due to the desire by refugees and migrants to continue on with their journey and an unwillingness to remain in unrest.

<!-- b000093 | prose | pages [4] -->
• Transportation index

<!-- b000094 | prose | pages [4] -->
To transport from place i to place j, one needs to balance a comprehensive transportation cost with regard of time, distance and traﬃc condition related to the type of transportation etc..Thus a transportation index Convi is deﬁned.

<!-- b000095 | prose | pages [4] -->
• Ratio of repatriation in period T

<!-- b000096 | prose | pages [4] -->
The quantity of refugees who get granted is limited in an entry point, thus the proportion of repatriates or rejectees are relatively too high, then refugees are less likely to take on a routine head for that node. Therefore, we also give a notation of Bt representing the ratio of repatriation in a certain period T in order to better solve the refugee crisis problem.

<!-- b000097 | prose | pages [4] -->
• Quantity of nodes

<!-- b000098 | prose | pages [4] -->
We premise that the quantity of refugees allowed to pass through an entry point is a constant, in this way, the total number of people who get granted is determined by the number of entry points (node in model). P ointj

<!-- b000099 | prose | pages [4] -->
i is the ith entry point in place j. Evidently, the larger the number i, the larger pass probability will be for a certain group, which aﬀects the choice of refugees.

<!-- b000100 | prose | pages [4] -->
Taking all those parameters and measures into account, we can step further to deﬁne a set of notations in designing a mathematical model.

<!-- b000101 | prose | pages [4] -->
3

<!-- b000102 | heading | pages [4] -->
Notations and Descriptions

<!-- b000103 | caption | pages [4] -->
Table 1.Notations and Descriptions we deﬁne in our model

<!-- b000104 | furniture | pages [5] -->
Team #44348

<!-- b000105 | furniture | pages [5] -->
page 4 of 18

<!-- b000106 | heading | pages [5] -->
Notations

<!-- b000107 | prose | pages [5] -->
Descriptions

<!-- b000108 | prose | pages [5] -->
P t

<!-- b000109 | prose | pages [5] -->
Probability to migrate from node i to node j of refugees in year t ij Ret

<!-- b000110 | prose | pages [5] -->
Ratio of regional acceptance of group i in place j in year t ij Rt

<!-- b000111 | prose | pages [5] -->
Routine chosen by group i in year t i St

<!-- b000112 | prose | pages [5] -->
Index of safety dead from place i to place j in year t ij Capt

<!-- b000113 | prose | pages [5] -->
Ratio of refugees in place i in year t ij Ret

<!-- b000114 | prose | pages [5] -->
Index of the resource given to group i in year t i Number of Entry points in place j Pj Required time for refugees to migrate from place i to place j Tij T rT

<!-- b000115 | prose | pages [5] -->
Transportation taken by refugees from place i to place j in period T ij N T

<!-- b000116 | prose | pages [5] -->
Quantity of refugees migrating from place i in period T i BT Ratio of refugees sent back in period T LT

<!-- b000117 | prose | pages [5] -->
Distance on land from place i to place j ij Distance on the sea from place i to place j Oij Economic condition in place i Ei Population density in place i Pij Ratio of environmental acceptance in place i compared with place j Cij Quantity of refugees on routine i Fi Convenience index to transport from place i to place j Convi Mortality of refugees migrating from place i to place j Moi Ratio of oﬃcial acceptance in place j(mainly customs) for group i Offii No. i entry point in place j P ointij M T

<!-- b000118 | prose | pages [5] -->
Comprehensive weight index of place j to attract group i in period T ij

<!-- b000119 | prose | pages [5] -->
4

<!-- b000120 | heading | pages [5] -->
Fundamental Assumptions

<!-- b000121 | prose | pages [5] -->
• Refugees migrate in groups, and each group is a unit with ﬁxed number of individuals, whose physical, psychological and economic conditions are the same but vary from group to group. Given that the refugees are large in quantity, which burdens a lot to investigate their behaviour individually; refugees often take on a routine chosen by a leader within a group, and migrate together with family or community; besides, the migration of refugees is generally regional. Thus it is pragmatic to make such an assumption.

<!-- b000122 | prose | pages [5] -->
• The migration of refugees is irreversible and there will be no ideal shield before arriving their destinations.

<!-- b000123 | prose | pages [5] -->
That is to say, leave out the condition that a unit go back from where it has reached to, and take no account of those who stay halfway.

<!-- b000124 | prose | pages [5] -->
• Refugees are sensible who can adjust their routines as well as the weight value according to diﬀerent conditions at current node.

<!-- b000125 | prose | pages [5] -->
Refugees are able to judge reasonably on veriﬁed routines with changing factors and decide on the probability based on the weight value of certain routine.

<!-- b000126 | prose | pages [5] -->
• The migration of refugees is progressed step by step. Not all the refugees locate on coastlines, thus the routines head for coast are subroutines of main 6 routines.

<!-- b000127 | prose | pages [5] -->
• The mortality is a constant on land and another on the sea.

<!-- b000128 | prose | pages [5] -->
On the three routines across the west, central and east Mediterranean Ocean, the refugees migrate on the sea while on other routines on land, and the two transport diﬀer with each other in risk coeﬃcient.

<!-- b000129 | prose | pages [5] -->
• Those who get their immigration granted are no longer refugees while those who enter Europe but are sent back for a lack of entrance permit are new refugees.

<!-- b000130 | prose | pages [5] -->
• Migration occurs quarterly.

<!-- b000131 | prose | pages [5] -->
FRONTEX-FRAN Quarterly provides a regular overview of irregular mi- gration at the EU external borders, based on the irregular migration data exchanged among Member State border-control authorities[8]. So here we consider the migration as quarterly and one quarter deﬁned as period T to picture out an irregular migration at EU level and to discuss on the trends and patterns.

<!-- b000132 | prose | pages [5] -->
• The quantity of passed refugees are constant per node per period. The nodes vary from place to place, but the capacity for refugees of each node is same so that the total capacity for refugees in a place is only decided by the quantity of nodes.

<!-- b000133 | furniture | pages [6] -->
Team #44348

<!-- b000134 | furniture | pages [6] -->
page 5 of 18

<!-- b000135 | prose | pages [6] -->
• The quantity of entry points, distance on land and on the sea, the time needed to migrate with diﬀerent transportation and convenience index to transport from one place to another, the ratio of oﬃcial acceptance and that of environmental acceptance all remain as constants.

<!-- b000136 | prose | pages [6] -->
This is basis of our model, the parameters listed above are not sensitive to time, if not so, the problem would possibly be a dead end.

<!-- b000137 | prose | pages [6] -->
Given those preconditions, we can set out to construct our model so as to ﬁgure out a safe and eﬃcient routine for the refugees.

<!-- b000138 | prose | pages [6] -->
5

<!-- b000139 | heading | pages [6] -->
The Gravitational Refugee Movement Model

<!-- b000140 | prose | pages [6] -->
5.1 Initial Nodal weight analysis

<!-- b000141 | prose | pages [6] -->
• Node deﬁnition An abstraction of geographic division on earth, representing diﬀerent countries, whose area share analogous trait, and whose trait is assumed to be the same regardless of the nuance within the area. And the metrics and assumptions apply to those nodes.

<!-- b000142 | prose | pages [6] -->
The resolution of a node can be modiﬁed according to the policy maker’s jurisdiction level, such as county, state and nation, etc. The 6 routines that refugees take locate between node and node. Each node has two states, which are saturated and unsaturated. The distinction between the two states is that the saturated nodes have passed the tipping point (threshold) and cannot receive any more refugees. People cannot stay in saturated nodes. These issues have been taken into consideration in the nodal weight analysis.

<!-- b000143 | prose | pages [6] -->
• Node selection Based on the statistics from Eurostat Database and UNHCR Historical Refugee Data we have selected and ranked the top 13 countries in Africa and Middle East where most refugees start their migration, as is shown in Figure2, and we choose them as representing nodes to make weight analysis.

<!-- b000144 | prose | pages [6] -->
Two things should be noted that the resource statistics we choose are all from 2014. For one thing, most of the data in 2015 is incomplete and for another, the latest complete oﬃcial statistics is up to ﬁrst half 2015, so we decide to use 2014 data, which has been veriﬁed oﬃcially by IOM, UNHCR and Eurostat etc. . Another is that as Uganda and Kenya, Pakistan and Afghanistan, Lebanon and Jordan are very close to each other on geologically, also smaller in territories, so we respectively consider those neighbouring countries as three nodes. In other words, we have altogether 11 nodes in our initial model, as is marked out in Figure3.

<!-- b000145 | prose | pages [6] -->
• Migratory Routes

<!-- b000146 | prose | pages [6] -->
(1)Western Mediterranean Route (WM)

<!-- b000147 | prose | pages [6] -->
From Algeria and Morocco to Spain, France and Italy

<!-- b000148 | prose | pages [6] -->
(2)Central Mediterranean Route (CM)

<!-- b000149 | prose | pages [6] -->
From Tunisia and Libya to Italy and Malta

<!-- b000150 | prose | pages [6] -->
(3)Eastern Mediterranean Route (EM)

<!-- b000151 | prose | pages [6] -->
From Turkey to the European Union via Greece, southern Bulgaria or Cyprus

<!-- b000152 | prose | pages [6] -->
(4)Western Balkan Route (WB)

<!-- b000153 | prose | pages [6] -->
From Greek-Turkish land or sea borders into Hungary

<!-- b000154 | prose | pages [6] -->
(5)Eastern Borders Route (EB)

<!-- b000155 | prose | pages [6] -->
From Ukraine to its European Union neighbours (Hungary, Poland, Slovakia)

<!-- b000156 | prose | pages [6] -->
(6)Circular Route (CAG)

<!-- b000157 | prose | pages [6] -->
From Albania to Greece

<!-- b000158 | prose | pages [6] -->
Given the six main migrating routes mapped out on BBC website, we assume those routes are the ﬁnal routes that the 11 nodes eventually head for. And we choose western Mediterranean, central Mediterranean, Eastern Mediterranean, East Balkan, Albania, and border land between Lithuania and Poland as the starting points of those 6 routes, as is shown in Figure3.

<!-- b000159 | furniture | pages [7] -->
Team #44348

<!-- b000160 | caption | pages [7] -->
Figure 2: Top 13 Refugee Origins

<!-- b000161 | furniture | pages [7] -->
page 6 of 18

<!-- b000162 | caption | pages [7] -->
Figure 3: Routes and Nodes

<!-- b000163 | prose | pages [7] -->
• Classifying the distance using clustering analysis

<!-- b000164 | prose | pages [7] -->
We presume that the refugees in Africa tend to ﬂee persecution, so as to say, within the emigration centers in a country, the refugees always head for the regions or centers within a circle area closer to Europe.

<!-- b000165 | prose | pages [7] -->
We collected route distance data from FRAN and ICMPD (see in ﬁgure4), then we divide the 11 nodes into 3 layers based on clustering methodology principles, in which the initial layer includes 3 nodes (Pak- istan/Afghanistan, Uganda/Kenya and Yemen); the propagation layer includes 4 nodes (Turkey, Iran, Ethiopia and South Sudan); the terminal layer includes 4 nodes (South Sudan, Lebanon/Jordan, Chad and Iraq). Refugees migrate layer by layer, eventually they get to the 6 start points of the main routes reaching to Europe.

<!-- b000166 | prose | pages [7] -->
We calculate the average distance from 11 nodes to start points to get the approximate distance di, respectively, but it should be noted that as EB route is far away from the location of refugees in our model, and it is very diﬃcult for them to take on EB route and enter Europe, so we leave out EB route and it’s nodes as well. The formula is:

<!-- b000167 | prose | pages [7] -->
5

<!-- b000168 | prose | pages [7] -->
di = 1

<!-- b000169 | prose | pages [7] -->
X

<!-- b000170 | prose | pages [7] -->
5

<!-- b000171 | prose | pages [7] -->
k=1

<!-- b000172 | prose | pages [7] -->
Then we make a matrix with all the distances:

<!-- b000173 | prose | pages [7] -->
  4630 4060 3470 2840 2880

<!-- b000174 | prose | pages [7] -->
D =

<!-- b000175 | prose | pages [7] -->
xk, i = 1, 2, ...11

<!-- b000176 | prose | pages [7] -->
2340  3520 3222 1410 2370 2333

<!-- b000177 | prose | pages [7] -->
The units are integrated into a whole cluster, whose height value are all zero, that is:

<!-- b000178 | prose | pages [7] -->
  4630 4060 3470 2840 2880

<!-- b000179 | prose | pages [7] -->
Hi =

<!-- b000180 | prose | pages [7] -->
2340  3520 3222 1410 2370 2333

<!-- b000181 | prose | pages [7] -->
Set height value as K1, and pick out the units, forming the ﬁrst cluster:

<!-- b000182 | prose | pages [7] -->
  4630

<!-- b000183 | prose | pages [7] -->
H1 =

<!-- b000184 | prose | pages [7] -->
3470  4060

<!-- b000185 | prose | pages [7] -->
Set height value as K2, and pick out the units, forming the second cluster:

<!-- b000186 | prose | pages [7] -->
  2840

<!-- b000187 | prose | pages [7] -->
H2 =

<!-- b000188 | prose | pages [7] -->
3222  2880 3520

<!-- b000189 | prose | pages [7] -->
Set height value as K3, and pick out the units, forming the third cluster:

<!-- b000190 | prose | pages [7] -->
  1410

<!-- b000191 | prose | pages [7] -->
H3 =

<!-- b000192 | prose | pages [7] -->
Thus the 11 nodes are classiﬁed into 3 clusters.

<!-- b000193 | prose | pages [7] -->
• Network of Nodes Analysis

<!-- b000194 | prose | pages [7] -->
Now we can get a network of the nodes analysis:

<!-- b000195 | prose | pages [7] -->
2340  2370 2333

<!-- b000196 | furniture | pages [8] -->
Team #44348

<!-- b000197 | furniture | pages [8] -->
page 7 of 18

<!-- b000198 | caption | pages [8] -->
Figure 4: Network of nodes

<!-- b000199 | prose | pages [8] -->
Suppose that in a period circle T of a node, the original quantity of refugees starting out from that node is N T

<!-- b000200 | prose | pages [8] -->
j−1, and the formula comes as:

<!-- b000201 | prose | pages [8] -->
N T

<!-- b000202 | prose | pages [8] -->
j = N T

<!-- b000203 | prose | pages [8] -->
Kj−1 X

<!-- b000204 | prose | pages [8] -->
N T

<!-- b000205 | prose | pages [8] -->
j−1 +

<!-- b000206 | prose | pages [8] -->
i

<!-- b000207 | prose | pages [8] -->
i=1

<!-- b000208 | prose | pages [8] -->
That is, the total refugees starting out from a node is the original quantity plus the quantity of refugees from the former layer.

<!-- b000209 | prose | pages [8] -->
• Initial direct simulation

<!-- b000210 | prose | pages [8] -->
Based on the network of nodes, we simulate the refugee ﬂows directly using Matlab with the assumption that the weight values of migrating towards the nodes in the next layer are all the same for refugees located in the nodes within the ﬁrst layer. Besides, the at the nodes within the last layer the refugees only choose three routines where the transportation and distance are optimums instead of taking on a long and tiring journey. The statistics are shown below.

<!-- b000211 | caption | pages [8] -->
Figure 5: Distances from the nodes to 6 start points

<!-- b000212 | caption | pages [8] -->
Figure 6: Initial Result

<!-- b000213 | prose | pages [8] -->
 1.0000

<!-- b000214 | prose | pages [8] -->
R =

<!-- b000215 | prose | pages [8] -->


<!-- b000216 | prose | pages [8] -->
0.6543 0.6543 1.0000

<!-- b000217 | prose | pages [8] -->
 1.0000

<!-- b000218 | prose | pages [8] -->
P =

<!-- b000219 | prose | pages [8] -->


<!-- b000220 | prose | pages [8] -->
0.1586 0.1586 1.0000

<!-- b000221 | prose | pages [8] -->
After analyze R and P. We ﬁnd that p>0.05 and R=0.6543. The result of initial model is inconsistent with our data, so we adjusted the routes using weighted approach, then we analyze the weighted value which is demonstrated as percentage. The nearer to 1 the percentage is, the better the result is. Therefore, our initial model doesn’t work well, and we right away modify it.

<!-- b000222 | furniture | pages [9] -->
Team #44348

<!-- b000223 | furniture | pages [9] -->
page 8 of 18

<!-- b000224 | heading | pages [9] -->
Modiﬁed model added with gravitation theory

<!-- b000225 | prose | pages [9] -->
5.2

<!-- b000226 | prose | pages [9] -->
5.2.1 The relationship among the 6 routes

<!-- b000227 | prose | pages [9] -->
We presume that the the refugees on the route to Greece include those who have already entered Greece. According to real data on IOM and Eurostat, the total refugees on route to Greece should have added with those on other routes which combine into the main Greece route.

<!-- b000228 | prose | pages [9] -->
R5 = a1R1 + a2R2 + a3R3 + a4R4

<!-- b000229 | prose | pages [9] -->
From the data before, we can estimate the number of refugees ﬂowing into WB route.

<!-- b000230 | prose | pages [9] -->
Route EM Value 0.24316 CM WB CAG 0.39523 1 0.5

<!-- b000231 | heading | pages [9] -->
Weight reanalysis and remodeling based on Gravity model

<!-- b000232 | prose | pages [9] -->
5.2.2

<!-- b000233 | prose | pages [9] -->
Gravity model originates from the Gravity Theory, indicating the attraction between two related subjects. The basic formula is:

<!-- b000234 | prose | pages [9] -->
Mij = PiPj

<!-- b000235 | prose | pages [9] -->
Da

<!-- b000236 | prose | pages [9] -->
, (a > 0)

<!-- b000237 | prose | pages [9] -->
ij ij

<!-- b000238 | prose | pages [9] -->
I is the interaction indicator, PiPj is the product of populations of two cities, representing the mass product of two cities, D is the distance between two cities. This model is widely applied to measure the economic and ﬁnancial attraction. I. S. Lowry also developed a regression model (Lowery, 1996) which shows that job opportunity attracts people to migrate from one place to another. Now we are to measure the weight for the nodes inspired by those models to help refugees make better decision on migration. However, we revise our model by ﬁguring out a comprehensive weight indicator to represent the attraction to people. To calculate the extent of immigration between the two areas, we apply the metrics developed above, including safety, environmental acceptance, transportation, resources, repatriation ratio and quantity of entry points. We take the logarithm on both sides of the equation, here comes the expression:

<!-- b000239 | prose | pages [9] -->
ln Mij = ln Pi + ln Pj −ln Da

<!-- b000240 | prose | pages [9] -->
ij + Ka, (Kaisaconstant)

<!-- b000241 | prose | pages [9] -->
The distance data from layer to layer in diﬀerent nodes is illustrated as below, to which we refer to calculate Da

<!-- b000242 | caption | pages [9] -->
Figure 7: Distance Layer1 to Layer2

<!-- b000243 | prose | pages [9] -->
ij

<!-- b000244 | caption | pages [9] -->
Figure 8: Distance Layer2 to Layer3

<!-- b000245 | prose | pages [9] -->
Now add the variables derived from the metrics and notated above to Mij, we get

<!-- b000246 | prose | pages [9] -->
M t

<!-- b000247 | prose | pages [9] -->
ij = f(St

<!-- b000248 | prose | pages [9] -->
ij, Convt

<!-- b000249 | prose | pages [9] -->
5.2.3 Analysis on each factor

<!-- b000250 | prose | pages [9] -->
(1)St

<!-- b000251 | prose | pages [9] -->
ij, Bt, Cij, Pointj

<!-- b000252 | prose | pages [9] -->
i)

<!-- b000253 | prose | pages [9] -->
ij = 1 −x2c1

<!-- b000254 | prose | pages [9] -->
ij:Safety index St

<!-- b000255 | prose | pages [9] -->
(

<!-- b000256 | prose | pages [9] -->
+ c2x1

<!-- b000257 | prose | pages [9] -->
Lij

<!-- b000258 | prose | pages [9] -->
route crosses oceans 1

<!-- b000259 | prose | pages [9] -->
x1 =

<!-- b000260 | prose | pages [9] -->
route doesn’t cross oceans 0

<!-- b000261 | prose | pages [9] -->
(

<!-- b000262 | prose | pages [9] -->
route crosses land 1

<!-- b000263 | prose | pages [9] -->
x2 =

<!-- b000264 | prose | pages [9] -->
route doesn’t cross land 0

<!-- b000265 | prose | pages [9] -->
*c1 is danger coeﬃcient, normally refers mortality on land routes and c2 is on sea’s

<!-- b000266 | furniture | pages [10] -->
Team #44348

<!-- b000267 | furniture | pages [10] -->
page 9 of 18

<!-- b000268 | prose | pages [10] -->
Mortality With FRAN and IOM (Fatal Journeys Tracking Lives lost in Migration, 2014), we collect the deaths data on 6 routes of refugees, here we give the mortality on the sea, which is c2

<!-- b000269 | caption | pages [10] -->
Figure 9: Mortality on the sea

<!-- b000270 | prose | pages [10] -->
And c1 is ﬁgured out in a same way. (2)Convt

<!-- b000271 | prose | pages [10] -->
ij:transportation convenience index

<!-- b000272 | prose | pages [10] -->
Convt

<!-- b000273 | prose | pages [10] -->
ij = c3E1E2Trij

<!-- b000274 | prose | pages [10] -->


<!-- b000275 | prose | pages [10] -->
one kind of transportation 1

<!-- b000276 | prose | pages [10] -->
 

<!-- b000277 | prose | pages [10] -->
Trij =

<!-- b000278 | prose | pages [10] -->
two kinds of transportation 2

<!-- b000279 | prose | pages [10] -->


<!-- b000280 | prose | pages [10] -->
three kinds of transportation 3

<!-- b000281 | prose | pages [10] -->


<!-- b000282 | prose | pages [10] -->
*c3is adjusting coeﬃcient (3)Bt

<!-- b000283 | prose | pages [10] -->
i: repatriation index This indicator is determined by the ratio between the repatriated refugees and total migrating refugees of a country in a certain year t, the larger the ratio is, the lager Bt

<!-- b000284 | prose | pages [10] -->
i is. (4)Ct

<!-- b000285 | prose | pages [10] -->
ij: Environmental acceptance index

<!-- b000286 | prose | pages [10] -->
Cijt = c4

<!-- b000287 | prose | pages [10] -->
(5)Pointj

<!-- b000288 | prose | pages [10] -->
i: Entry point quantity

<!-- b000289 | prose | pages [10] -->
Rej

<!-- b000290 | prose | pages [10] -->
Relt

<!-- b000291 | prose | pages [10] -->
ij

<!-- b000292 | prose | pages [10] -->
Rei

<!-- b000293 | prose | pages [10] -->
We suppose that the probability of receiving a refugee unit of each node is p, within a period T the quantity of granted refugees of each node is a constant. Once a node passes the tipping point (threshold), it reaches a saturated state and closes automatically. Now we test 6 countries whose receiving nodes diﬀer with each other, but the maximum of granted migrants is the same for each node. Set the maximum as M, then the probability for a group to be received can be simpliﬁed as a Bernoulli Distribution:

<!-- b000294 | prose | pages [10] -->
(

<!-- b000295 | prose | pages [10] -->
p

<!-- b000296 | prose | pages [10] -->
P =

<!-- b000297 | prose | pages [10] -->
0

<!-- b000298 | prose | pages [10] -->
If ni units of refugees pass through the node, then

<!-- b000299 | prose | pages [10] -->


<!-- b000300 | prose | pages [10] -->
0

<!-- b000301 | prose | pages [10] -->
 

<!-- b000302 | furniture | pages [10] -->


<!-- b000303 | prose | pages [10] -->
P(x = ni) =

<!-- b000304 | prose | pages [10] -->
 

<!-- b000305 | prose | pages [10] -->
n > KL n < KL

<!-- b000306 | prose | pages [10] -->
ni > KL

<!-- b000307 | prose | pages [10] -->
!

<!-- b000308 | prose | pages [10] -->
ni

<!-- b000309 | prose | pages [10] -->
ni < KL

<!-- b000310 | prose | pages [10] -->
KL

<!-- b000311 | prose | pages [10] -->
Taking our analysis of variables into serious consideration, we get a comprehensive formula:

<!-- b000312 | prose | pages [10] -->
ij + ln Convt

<!-- b000313 | prose | pages [10] -->
ln M t

<!-- b000314 | prose | pages [10] -->
ij = ln St

<!-- b000315 | prose | pages [10] -->
ij −ln Bt

<!-- b000316 | prose | pages [10] -->
a + Ka

<!-- b000317 | prose | pages [10] -->
*Mijis the weight index for a refugee group’s attraction to a node. Meanwhile, the migrating refugees on each node in a period T is determined by the formula:

<!-- b000318 | prose | pages [10] -->
Kj−1

<!-- b000319 | prose | pages [10] -->
N T

<!-- b000320 | prose | pages [10] -->
j = N T

<!-- b000321 | prose | pages [10] -->
j−1 +

<!-- b000322 | prose | pages [10] -->
X X

<!-- b000323 | prose | pages [10] -->
N T

<!-- b000324 | prose | pages [10] -->
i (1 −MoT

<!-- b000325 | prose | pages [10] -->
ij)

<!-- b000326 | prose | pages [10] -->
i=1 i=1

<!-- b000327 | prose | pages [10] -->
Now we can ﬁgure out a revised network of nodes, marking the weight beside each route.

<!-- b000328 | caption | pages [10] -->
Figure 10: Revised network of nodes

<!-- b000329 | furniture | pages [11] -->
Team #44348

<!-- b000330 | furniture | pages [11] -->
page 10 of 18

<!-- b000331 | prose | pages [11] -->
Again we use Matlab calculation to see how the refugees can migrate from node to node, layer by layer. And Figure 11 and 12 is the propagation of refugees from node to node, the y axes stands for the proportion of population that one layer receive from the former layer.

<!-- b000332 | caption | pages [11] -->
Figure 11: Propagation L1 to L2

<!-- b000333 | caption | pages [11] -->
Figure 12: Propagation L2 to L3

<!-- b000334 | prose | pages [11] -->
And Figure 13 is the propagation of refugees from the third layer to the start points head for Europe.

<!-- b000335 | caption | pages [11] -->
Figure 13: The ratio of refugees migrating from the third layer to the start points

<!-- b000336 | prose | pages [11] -->
Comparing the two groups of data, we ﬁnd that the Correlation R equals to 0.9914 and P equals to 0.00001<0.05. So we think this group of data is valid. we found that this time the model copes well with real data, shown in Figure 14.The result is demonstrated below, line1 is the real data, line2 is revised modeling result, and line3 is the initial result. The y label is ratio between refugees at a node and total number, x label is 6 routes. Evidently, line1 and line2 coincide with each other well. So we think that the improved gravity model can calculate the weight between the nodes more close to the real condition.And next we search for an optimal route of migration.

<!-- b000337 | caption | pages [11] -->
Figure 14: The results and comparison

<!-- b000338 | prose | pages [11] -->
5.2.4 An optimal route

<!-- b000339 | prose | pages [11] -->
• Aimed route

<!-- b000340 | prose | pages [11] -->
(1)High safety index, low mortality

<!-- b000341 | prose | pages [11] -->
(2)High resource abundance index

<!-- b000342 | prose | pages [11] -->
(3)High transportation convenience index, low cost

<!-- b000343 | prose | pages [11] -->
(4)High match with environmental acceptance index of receiving country

<!-- b000344 | prose | pages [11] -->
• Multi-objective into single-objective

<!-- b000345 | furniture | pages [12] -->
Team #44348

<!-- b000346 | furniture | pages [12] -->
page 11 of 18

<!-- b000347 | prose | pages [12] -->
• Always choosing the nearest routes With safety ensured, refugees choose the nearest two routes so as to reduce the cost in the third layer, and in this case we calculate the weight of routes.

<!-- b000348 | prose | pages [12] -->
• Weight of the importance of each aim In multi-objective planning, we set the safety index as ϑ1, and distance index as ϑ2, so

<!-- b000349 | prose | pages [12] -->
ϑ2(1 −St

<!-- b000350 | prose | pages [12] -->
• Quantitative analysis

<!-- b000351 | prose | pages [12] -->
ij) = ϑ2c2x1

<!-- b000352 | prose | pages [12] -->
Then we make quantitative analysis of the attitudes of receiving countries according to the actual received refugees in each country.

<!-- b000353 | prose | pages [12] -->
  σ1

<!-- b000354 | prose | pages [12] -->


<!-- b000355 | prose | pages [12] -->
σ2 σ3 σ4 σ5

<!-- b000356 | prose | pages [12] -->
And the distance of each route is:

<!-- b000357 | prose | pages [12] -->


<!-- b000358 | prose | pages [12] -->
0 0 0 3700

<!-- b000359 | prose | pages [12] -->


<!-- b000360 | prose | pages [12] -->
Lij =

<!-- b000361 | prose | pages [12] -->


<!-- b000362 | prose | pages [12] -->
0 0

<!-- b000363 | prose | pages [12] -->


<!-- b000364 | prose | pages [12] -->
0 2000

<!-- b000365 | prose | pages [12] -->
  1.5 1.30  2.0 5.0 4.75

<!-- b000366 | prose | pages [12] -->
= =

<!-- b000367 | prose | pages [12] -->


<!-- b000368 | prose | pages [12] -->
650 1200 0 0 3400 0 0 0

<!-- b000369 | prose | pages [12] -->
 

<!-- b000370 | prose | pages [12] -->
2150 2000 0 0

<!-- b000371 | prose | pages [12] -->


<!-- b000372 | prose | pages [12] -->
1600 0 0 0

<!-- b000373 | prose | pages [12] -->
Finally, all the factors related to route planning can be seen as:

<!-- b000374 | prose | pages [12] -->
η1 = ϑ2

<!-- b000375 | prose | pages [12] -->
Lij

<!-- b000376 | prose | pages [12] -->
With the analysis and our revised model we can choose the weight of last four nodes in the third layer to conﬁrm the best route.

<!-- b000377 | prose | pages [12] -->
• Diﬀerences resulting from diﬀerent choices

<!-- b000378 | prose | pages [12] -->
Here we choose

<!-- b000379 | prose | pages [12] -->
(1)ϑ1 = ϑ2 = 0.5

<!-- b000380 | prose | pages [12] -->
(2)ϑ1 = 0.4, ϑ2 = 0.6

<!-- b000381 | prose | pages [12] -->
(3)ϑ1 = 0.6, ϑ2 = 0.4

<!-- b000382 | prose | pages [12] -->
(4)ϑ1 = 0.3, ϑ2 = 0.7

<!-- b000383 | prose | pages [12] -->
(5)ϑ1 = 0.7, ϑ2 = 0.3

<!-- b000384 | prose | pages [12] -->
Make weight analysis for those values and compare the results.

<!-- b000385 | prose | pages [12] -->
If taking safety ﬁrst, and meeting the policies of every country, then choose the largest ϑ1 = 0.7 and we ﬁnd out the best distribution of refugees on each route as Figure 15

<!-- b000386 | caption | pages [12] -->
Figure 15: ϑ1 = 0.7, ϑ2 = 0.3 the ratios of refugees on 6 routes

<!-- b000387 | prose | pages [12] -->
We ﬁnd that in this case, the ratios of refugees on the six routes are 0.01, 0.07, 0.43, 0.48, 0.01, 0.00, indicating that the refugees tend to choose land routes. But as there are only 2 nodes among the last 4 nodes near to EB route, those choosing WM are large in quantity. According to IOM statistics, the mortality on WM, CM, EM route goes up by sequence, so it is safer for people to take WM and EB route.

<!-- b000388 | furniture | pages [13] -->
Team #44348

<!-- b000389 | furniture | pages [13] -->
page 12 of 18

<!-- b000390 | caption | pages [13] -->
Figure 16: ϑ1 = 0.3, ϑ2 = 0.7 the ratios of refugees on 6 routes

<!-- b000391 | prose | pages [13] -->
(Line1 is real data and line2 is the modeling result. )

<!-- b000392 | prose | pages [13] -->
If taking transportation convenience ﬁrst, and meeting the policies of every country, then choose the largest ϑ2 = 0.7 and we ﬁnd out the best distribution of refugees on each route in Figure 16.

<!-- b000393 | prose | pages [13] -->
We ﬁnd that in this case, the ratios of refugees on the six routes are 0.20, 0.17, 0.30, 0.31, 0.01, 0.01, indicating that more people might take WM route. But as Spanish government has a strict control in migrants with low receiving quantity each year, hence not so many migrants take WM. CM takers increase because EM and WB route is relatively far away from the node.

<!-- b000394 | prose | pages [13] -->
5.2.5 Preposition Resource

<!-- b000395 | prose | pages [13] -->
So after considering these two kinds of condition,we think that plenty of resource prepared for the refugees and enough residence should be placed in Center Mediterranean route,West Mediterranean route and West Balkan route.Because whatever the condition is, there will still be huge number of people travelling through this route to their ﬁnal destination.

<!-- b000396 | prose | pages [13] -->
6 Dynamic changes and Refugees

<!-- b000397 | prose | pages [13] -->
6.1

<!-- b000398 | heading | pages [13] -->
Dynamic simulation model of refugee migration based on Cellular Automaton

<!-- b000399 | prose | pages [13] -->
In the very beginning we have assumed that the ﬂow of refugees occurs periodically. So suppose that there are nperiods every year, and the migration ﬂow is a community of certain number of refugees. Thus each quarter the migration population is 1

<!-- b000400 | prose | pages [13] -->
n%, and the migrating people inﬂuence the remaining ones. The model is shown as below:

<!-- b000401 | caption | pages [13] -->
Figure 17: Dynamic Model

<!-- b000402 | prose | pages [13] -->
As is seen in the ﬁgure, node 1, 2, 3, 4 represents the area where refugees gather and start migration in Africa and Central East, and we can get the weight between diﬀerent nodes with our model. Suppose that during the ﬁrst quarter, the migration route is chosen by the weight values and the refugees migrate only from one node to another i in a period. We add a coeﬃcient δ = Lij to unitize the distance between two nodes considering weight impact.

<!-- b000403 | prose | pages [13] -->
nN t0 1 Therefore, in the ﬁrst period the migration population at the ﬁrst node is

<!-- b000404 | prose | pages [13] -->
1 , and the migration population nN t0 1 towards other three nodes is

<!-- b000405 | prose | pages [13] -->
1 w1i, (i = 1, 2, 3), now the refugee population from the ﬁrst node towards the second node is deﬁned as:

<!-- b000406 | furniture | pages [14] -->
Team #44348

<!-- b000407 | prose | pages [14] -->
k

<!-- b000408 | prose | pages [14] -->
1

<!-- b000409 | prose | pages [14] -->
X

<!-- b000410 | furniture | pages [14] -->
page 13 of 18

<!-- b000411 | prose | pages [14] -->
i wi2 + 3

<!-- b000412 | prose | pages [14] -->
nN t0

<!-- b000413 | prose | pages [14] -->
N t1

<!-- b000414 | prose | pages [14] -->
2 =

<!-- b000415 | prose | pages [14] -->
i=1

<!-- b000416 | prose | pages [14] -->
4N t0 2

<!-- b000417 | prose | pages [14] -->
So in the second period we can estimate the refugee population at the second node. But due to the changing factors and indexes, the weight mat change from node 1 to node 2 as the population, capacity of refugees and the average available resource may change. We divide those changing factors into two categories:

<!-- b000418 | prose | pages [14] -->
6.2 Non-paroxysmal factors

<!-- b000419 | prose | pages [14] -->
• Change in capacity and resources

<!-- b000420 | prose | pages [14] -->
Evidently, the resources and capability of a node is limited, the outs and ins of refugees aﬀect the weight of other nodes where the people head for this node in next period. Take node 1 and 2 as an example, the population of node 2 in period t0 is N t0

<!-- b000421 | prose | pages [14] -->
2 , and now as the change of population leads to the change of inﬂow weight of other nodes, we set the comparative coeﬃcient as π, the expression is:

<!-- b000422 | prose | pages [14] -->
• Changed weight

<!-- b000423 | prose | pages [14] -->
So the weight after change is

<!-- b000424 | prose | pages [14] -->
π = N t1

<!-- b000425 | prose | pages [14] -->
2 N t0

<!-- b000426 | prose | pages [14] -->
2

<!-- b000427 | prose | pages [14] -->
1

<!-- b000428 | prose | pages [14] -->
i2 = πWi2W t1

<!-- b000429 | prose | pages [14] -->
w′

<!-- b000430 | prose | pages [14] -->
i2 = w′

<!-- b000431 | prose | pages [14] -->
i2

<!-- b000432 | prose | pages [14] -->
kP

<!-- b000433 | prose | pages [14] -->
w′

<!-- b000434 | prose | pages [14] -->
i2

<!-- b000435 | prose | pages [14] -->
i=1

<!-- b000436 | prose | pages [14] -->
Suppose that there are saturated and unsaturated states at each node, and the saturated receiving population 1 nof the population have migrated out, the node closes, only is NL, if the refugees are more than NL after allowing out. That is:

<!-- b000437 | prose | pages [14] -->
n −1

<!-- b000438 | prose | pages [14] -->
= n −1

<!-- b000439 | prose | pages [14] -->
(n −1

<!-- b000440 | prose | pages [14] -->
N tj

<!-- b000441 | prose | pages [14] -->
i

<!-- b000442 | prose | pages [14] -->
n

<!-- b000443 | prose | pages [14] -->
n

<!-- b000444 | prose | pages [14] -->
n

<!-- b000445 | prose | pages [14] -->
t

<!-- b000446 | prose | pages [14] -->
W tj−1

<!-- b000447 | prose | pages [14] -->
N tj−1

<!-- b000448 | prose | pages [14] -->
N tj−1

<!-- b000449 | prose | pages [14] -->
X

<!-- b000450 | prose | pages [14] -->
) > N i

<!-- b000451 | prose | pages [14] -->
ki

<!-- b000452 | prose | pages [14] -->
+

<!-- b000453 | prose | pages [14] -->
L

<!-- b000454 | prose | pages [14] -->
i

<!-- b000455 | prose | pages [14] -->
k

<!-- b000456 | prose | pages [14] -->
n

<!-- b000457 | prose | pages [14] -->
k=1

<!-- b000458 | prose | pages [14] -->
In this way, we can foresee the change of population at a node in the next period when it is near tipping point.

<!-- b000459 | prose | pages [14] -->
• Simulation of the refugee migration

<!-- b000460 | prose | pages [14] -->
Based on the formula, we simulate the process of migration with C++ only with non-paroxysmal factors, and we map the process out with JavaScript, from left to right, up to down, we can see the changing paths of refugees from Africa and Central East to Europe within same space of time and the change in population, which is indicated by change of size of the circle area.

<!-- b000461 | caption | pages [14] -->
Figure 18: Simulation of Refugee Migration only with non-paroxysmal factors

<!-- b000462 | prose | pages [14] -->
We suppose that the ﬁnal destination of EM and CM route is Italy, the one of WM route is Spain and the one of WB is Greece and other European countries. By certain algorithm and data comparison we get the ratios as (0.00362, 0.537, 0.427), and the real data is (0.013, 0.545, 0.422), through computer calculation we ﬁnd the correlation coeﬃcient value is R = 1.0000

<!-- b000463 | furniture | pages [15] -->
Team #44348

<!-- b000464 | prose | pages [15] -->
6.3 Accidental and irregular factors

<!-- b000465 | prose | pages [15] -->
• The change in safety index on route

<!-- b000466 | furniture | pages [15] -->
page 14 of 18

<!-- b000467 | prose | pages [15] -->
Environmental, military factors all make sense. The change in safety index can be adjusted by adding war factor β and environmental factor γ

<!-- b000468 | prose | pages [15] -->
(

<!-- b000469 | prose | pages [15] -->
0

<!-- b000470 | prose | pages [15] -->
Bij =

<!-- b000471 | prose | pages [15] -->
1

<!-- b000472 | prose | pages [15] -->
In this case, the safety index is aﬀected

<!-- b000473 | prose | pages [15] -->
no war on the route war on the route

<!-- b000474 | prose | pages [15] -->
ij = (x2c1 1 −St

<!-- b000475 | prose | pages [15] -->
+ c2x1 + βijc4)

<!-- b000476 | prose | pages [15] -->
Lij Lij

<!-- b000477 | prose | pages [15] -->
Here we neglect the intensity and scale of the war, and c4 is related to the mortality in war. The deﬁnition of environmental factor is

<!-- b000478 | prose | pages [15] -->


<!-- b000479 | prose | pages [15] -->
normal weather 0

<!-- b000480 | prose | pages [15] -->
  

<!-- b000481 | prose | pages [15] -->
fair weather c

<!-- b000482 | prose | pages [15] -->


<!-- b000483 | prose | pages [15] -->
γij =

<!-- b000484 | prose | pages [15] -->
−c windy and rainy weather

<!-- b000485 | prose | pages [15] -->
  

<!-- b000486 | prose | pages [15] -->
−2c snowy and freezing weather

<!-- b000487 | prose | pages [15] -->


<!-- b000488 | prose | pages [15] -->
ij = (x2c1 This also aﬀects the safety index 1 −St

<!-- b000489 | prose | pages [15] -->
• The inﬂuence of GO and NGO

<!-- b000490 | prose | pages [15] -->
+ x1c2 + βijc4)

<!-- b000491 | prose | pages [15] -->
Lij Lij

<!-- b000492 | prose | pages [15] -->
The funds and policies of governments can aﬀect the capacity and resources of a node. NGO also provides humanistic help and medical-health aid.

<!-- b000493 | prose | pages [15] -->
(1)As for node i, the inﬂuence of GO policies is measured when Np refugees migrate in or out and there are initially N tj

<!-- b000494 | prose | pages [15] -->
refugees who meet the condition that : i

<!-- b000495 | prose | pages [15] -->
n −1

<!-- b000496 | prose | pages [15] -->
(N tj n

<!-- b000497 | prose | pages [15] -->
i + NP ) > N i

<!-- b000498 | prose | pages [15] -->
L

<!-- b000499 | prose | pages [15] -->
(2)If the condition is not met, the population migrating into a node impacts other refugees:

<!-- b000500 | prose | pages [15] -->
N tj

<!-- b000501 | prose | pages [15] -->
i

<!-- b000502 | prose | pages [15] -->
tj

<!-- b000503 | prose | pages [15] -->
N Thus the comparative coeﬃcient is:π =

<!-- b000504 | prose | pages [15] -->
i

<!-- b000505 | prose | pages [15] -->
tj−1

<!-- b000506 | prose | pages [15] -->
N

<!-- b000507 | prose | pages [15] -->
i

<!-- b000508 | prose | pages [15] -->
= N tj

<!-- b000509 | prose | pages [15] -->
i + NP

<!-- b000510 | prose | pages [15] -->
As for NGO and GO involvement which might mitigate the refugee crisis, reducing the refugee population with NNGO unchanged, so the weight of nodes change accordingly. And the actual population at each node is deﬁned as:

<!-- b000511 | prose | pages [15] -->
= N tj

<!-- b000512 | prose | pages [15] -->
N tj

<!-- b000513 | prose | pages [15] -->
i

<!-- b000514 | prose | pages [15] -->
i −NNGO

<!-- b000515 | prose | pages [15] -->
Other algorithms are same alike, we also assume that the inﬂuence on capacity of refugees from local gov- ernmental policies ranges from -0.2 to +0.2. We focus on the accidental factors and also simulate the migration as follows.

<!-- b000516 | caption | pages [15] -->
Figure 19: Simulation of Refugee Migration only with accidental factors

<!-- b000517 | prose | pages [15] -->
The left ﬁgure: ∆N

<!-- b000518 | prose | pages [15] -->
= 20%, βij = 0, γij = c N The ratio of three nodes are (0.0307, 0.475, 0.494), so when the capacity of Greece increases by 20%, and the weather is ﬁne, then the migration ﬂow will change by 15.9%, indicating that the change in capacity can change the migration inﬂows. The right ﬁgure: ∆N

<!-- b000519 | prose | pages [15] -->
= −20%, βij = 1, γij = 0 N The ratio of three nodes are (0.0374, 0.562, 0.4006), so when the capacity of Greece decreases by 20%, and there are wars on the routes, the migration ﬂow will change by 6.18%, the ﬂows still increase because there are other migrants coming from other nodes who make up for the decrease.

<!-- b000520 | furniture | pages [16] -->
Team #44348

<!-- b000521 | furniture | pages [16] -->
page 15 of 18

<!-- b000522 | prose | pages [16] -->
7 Scalability

<!-- b000523 | prose | pages [16] -->
We apply our model to to Canada, America, and China to forecast the migration ﬂows and check the scalability of our work. We add the nodes of Canada, America and China and some other nodes linked with them to the modeling system. Based on data from I-Map we estimate the value of the route between the nodes of China, Canada, America and other nodes. The initial distribution of the refugee is shown in the graph.

<!-- b000524 | caption | pages [16] -->
Figure 20: Simulation of Refugee Migration on a Larger Scale

<!-- b000525 | prose | pages [16] -->
According to the result, we ﬁnd that there will be so many of refugees from Central East ﬂowing into China while few heading for America and Canada (only 7 for Canada, and 51 for America). So we ﬁnd that our model can not illustrate the ﬂow of the refugees well. Because:

<!-- b000526 | prose | pages [16] -->
• The Himalayas Because of the Himalayas mountains standing at the border of China, it will be much harder for the refugees to come into China.

<!-- b000527 | prose | pages [16] -->
So when weighing the value of these nodes, we should take the topography into consideration.

<!-- b000528 | prose | pages [16] -->
• The Atlantic Ocean we know that America and Canada is far from Northern Africa and Mid-east, and meanwhile the danger index also increases. So based on our revised Gravity model, the weight between the nodes of Africa, Mid-east and the nodes of America and Canada can be almost entirely ignored.

<!-- b000529 | prose | pages [16] -->
8

<!-- b000530 | heading | pages [16] -->
The Policy Strategy with Cobweb Model

<!-- b000531 | prose | pages [16] -->
• Enlarge the capacity and increase the resources in receiving countries We expand the crisis to a large scale(by a factor of 10), and ﬁnd that that our model can’t predict the ﬂow of the actual migration very well. Now the population of refugee on each route is almost the same, and we add the six route to our modeling, but in vain. We realize that we have presumed that the node stops working one it get saturated, and in our model the modes of EM and WB stop ﬁrst. And the left refugees pour into other 4 nodes until all the nodes become saturated. Thus there will be lots of refugees tarried in neighbouring countries. That may help to explain the increasing illegal migration. Many refugees may stay around for the limited resources, leading extra refugee inﬂow. So when the scale expands up, the restricting factors we have listed can be useless, as the nodes always stay saturated, resulting in detention and the breakdown of the system layer by layer.

<!-- b000532 | prose | pages [16] -->
• Enlarge the capacity according to current situation to stabilize the population of migration ﬂow We need stable migration ﬂow to quantify the distribution of resources for refugees. However, according to Cobweb Model, we ﬁnd that change of capacity in a period will make the population change at each node. A large capacity of a node will actually make the ﬂow of refugees through the node stable while a relatively small capacity of the node might cause the ﬂow become more and more unstable

<!-- b000533 | furniture | pages [17] -->
Team #44348

<!-- b000534 | furniture | pages [17] -->
page 16 of 18

<!-- b000535 | caption | pages [17] -->
Figure 21: Cobweb Model 1 NP=B

<!-- b000536 | caption | pages [17] -->
Figure 22: Cobweb Model 2 NP=A (B>A)

<!-- b000537 | caption | pages [17] -->
Figure 21 and Figure 22 presents the relationship between the pass rate P and the pass refugee population N

<!-- b000538 | prose | pages [17] -->
• Enhance and promote international partnership and cooperation When simulating the migration progress with our model, we ﬁnd that some of the nodes may become saturated while other not, so enhancing international cooperation and partnership, distributing refugees after receiving them may be acceptable and reasonable.

<!-- b000539 | prose | pages [17] -->
• Indicate an oﬃcial migration route As all of us are searching for an optimal migrating route pattern that beneﬁts both migrants and receivers, an oﬃcial migration route should be announced to guide the migrants, leading to a better and safer journey.

<!-- b000540 | prose | pages [17] -->
9 Inﬂuence of Exogenous Events

<!-- b000541 | prose | pages [17] -->
9.1 The outbreak of the diseases

<!-- b000542 | prose | pages [17] -->
The outbreak of the illness like the newly found Zika virus will shut down some nodes, thus causing some changes in the weight between the nodes involved in the disease. As a result, the refugees will not only consider distance, the economic conditions etc. , but also the distribution situation of the disease, which will decrease the capacity of the nodes as well.

<!-- b000543 | prose | pages [17] -->
9.2 Terrorist attack

<!-- b000544 | prose | pages [17] -->
Terrorist attack generated from the increase of refugees will directly impart the receiving index of European countries, thus the resources provided for migrants and refugees will be in short and receiving population will soon decrease. In this case, there is a cascading eﬀect which refers to the fact that a change in refugee policy of a country will aﬀect the migration ﬂow and the attitude towards refugees of its neighbouring countries as well as the inter-relationship among diﬀerent nodes, leading to the change of refugee inﬂows in the whole node system.

<!-- b000545 | prose | pages [17] -->
9.3 How can our policy be resilient to Exogenous Events

<!-- b000546 | prose | pages [17] -->
In the ﬁrst place, if we increase the capacity of refugees of diﬀerent nodes according to present condition, we can ensure that there will be no sharp closing of node whenever it is emergency or not so that the migration of refugees at other nodes will not be aﬀected.

<!-- b000547 | prose | pages [17] -->
Besides, when the cost on route is cut down, the migration population on CM or EU route increases so that the migration ﬂows on 6 routes can be equalized. In this way, the weight of route choice can be placed mostly on destination, thus avoiding the capacity saturation of the nodes.

<!-- b000548 | prose | pages [17] -->
Lastly, enhancing international cooperation and partnership as well as adding oﬃcial routes can help to create a better world and give guidance to refugees, which is beneﬁcial for resource allocation and optimization of all kinds of resources.

<!-- b000549 | furniture | pages [18] -->
Team #44348

<!-- b000550 | furniture | pages [18] -->
page 17 of 18

<!-- b000551 | prose | pages [18] -->
As a whole, our policy can adjust to the current situation to some extent.

<!-- b000552 | prose | pages [18] -->
10

<!-- b000553 | heading | pages [18] -->
Sensitivity Analysis

<!-- b000554 | prose | pages [18] -->
The migration of refugees not only relates to the countries we selected into our model but also involved with the other countries. Additionally, the migration of refugees involves quite a lot accidents and emergencies, which might lead to the change in refugee ﬂows. Here we have taken the increase and decrease of nodes into consideration, but for we have also assigned weight to the migration on every route and established a feedback system based on our model, the change in node quantity only have eﬀects on the population of initial refugees going on migration but not making big diﬀerence on the proportion of people heading for the ﬁnal 6 routes. At the same time, when we balance the inﬂuences of various factors we tend to neglect the impact of certain incidents. For example, we assume that the safety index has little sensitivity to weather, capacity of some nodes wwill not change a lot regardless of policy change or NGO aid or emergencies during migration because we also build feedback system of refugee and as all the 6 routes eventually converge into EB route, the real time modeling result is not like to change a lot.

<!-- b000555 | prose | pages [18] -->
We also think about the inﬂuence of capacity of each node on our model, ﬁnding that when the capacity changes by a small maigin ±5%, then the result of our model change by ±2%, but when the capacity changes beyond ±10%, then the result will deviate by larger than 4.7%.

<!-- b000556 | prose | pages [18] -->
11

<!-- b000557 | heading | pages [18] -->
Evaluation of the Model

<!-- b000558 | prose | pages [18] -->
11.1

<!-- b000559 | heading | pages [18] -->
Strengths

<!-- b000560 | prose | pages [18] -->
• We make cluster analysis and analytic hierarchy process on each sample country based on the distances between the country and the ﬁnal destination, and we presume that the migration of refugees progresses from far way to nearby, which simpliﬁes our calculation and coincides with real data.

<!-- b000561 | prose | pages [18] -->
• We make random simulation model initially because we are not sure whether the refugees lack of information about routes, and we ﬁnd it does not match real data, so we are sure that the migration is not random and we soon make reﬁnement on our model.

<!-- b000562 | prose | pages [18] -->
• We construct our basic model based upon the Gravity model, but we also make creative reﬁnement about the attraction, and the result has been veriﬁed by real data, indicating that our model does have its value.

<!-- b000563 | prose | pages [18] -->
• The basis of our third model is that the second revised Gravity Model simulates the refugee ﬂows among diﬀerent nodes well, which backs up our reliability. And we add the feedback ﬂows in each node and simulates the real migration.

<!-- b000564 | prose | pages [18] -->
• We use Cobweb Model to make our recommendation, and we ﬁgure out the relationship between the pass rate of the node and its capacity, thus our policy can be more convincing.

<!-- b000565 | prose | pages [18] -->
11.2

<!-- b000566 | heading | pages [18] -->
Weakness

<!-- b000567 | prose | pages [18] -->
• All the samples we choose are from Africa and Central East, so we almost leave out the refugee ﬂow on EB route, but actually there must be some refugees taking EB route.

<!-- b000568 | prose | pages [18] -->
• The distances in our model are approximated to be straight lines. We ignore the geological barriers on the routes, so there are some errors in calculating the distances.

<!-- b000569 | prose | pages [18] -->
• We leave out the redistribution of refugee ﬂows after they enter Europe, but only determine the acceptance ratio according to the receiving data of the countries.

<!-- b000570 | prose | pages [18] -->
• We haven’t thought of the stowaways who enter Europe illegally as refugees, because we do not have the oﬃcal data source.

<!-- b000571 | prose | pages [18] -->
12

<!-- b000572 | heading | pages [18] -->
Future Work

<!-- b000573 | prose | pages [18] -->
Uncontrovertibly, there are many drawbacks in our model, such as the incomplete collection of relevant data and inaccurate estimation of the weight values, etc., we have to do a lot more to improve our work. Firstly, we do not get the eﬀective distance between two nodes. So we use linear distance instead, which can be misleading to some extent. For example, when we apply our model to predict the population of refugees ﬂowing into China, we just get the wrong one because of the existence of Himalaya Mountains, whose geological features are almost covered up when we look on a planimetric map. The same goes with Canada and America. So we need to take more impact factors into consideration to get a better simulation.

<!-- b000574 | furniture | pages [19] -->
Team #44348

<!-- b000575 | furniture | pages [19] -->
page 18 of 18

<!-- b000576 | prose | pages [19] -->
Secondly, we do not get enough data in terms of testing our model with concerning the refugee crisis breaking out in Europe during 2014 and 2015. Hence it is hard for us to use eﬀective data to back up our model as it is no doubt that the more real statistics we have, the more helpful and reliable it can be in creating a better model. Finally, we should try to get more information about the policy implemented by the countries involved in this crisis and the cascade eﬀect that spread across the continent of Europe.And hopefully when we know exactly what the politicians are planning to do, we can propose more feasible strategies.

<!-- b000577 | heading | pages [19] -->
References

<!-- b000578 | references | pages [19] -->
[1] Number displaced worldwide hits record high - UN report

<!-- b000579 | references | pages [19] -->
http://www. bbc. com/

<!-- b000580 | references | pages [19] -->
[2] Charity appeals for help aiding desperate refugees

<!-- b000581 | references | pages [19] -->
http://www. dailyecho. co. uk/

<!-- b000582 | references | pages [19] -->
[3] Countries Under the Most Strain in the European Migration Crisis

<!-- b000583 | references | pages [19] -->
http://www. nytimes. com/

<!-- b000584 | references | pages [19] -->
[4] Six charts and a map that show where Europe’s refugees are coming from - and the perilous journeys they are taking

<!-- b000585 | references | pages [19] -->
http://www. independent. co. uk/

<!-- b000586 | references | pages [19] -->
[5] Migrant crisis: Migration to Europe explained in graphics

<!-- b000587 | references | pages [19] -->
http://www. bbc. com/

<!-- b000588 | references | pages [19] -->
[6] Kritz, Mary M. , and Hania Zlotnik. ”Global interactions: migration systems processes and policies. ”International

<!-- b000589 | references | pages [19] -->
migration systems, a global approach. Clarendon Press, Oxford, UK.1992.

<!-- b000590 | references | pages [19] -->
[7] Massey, D. , J. Arango, G. Hugo and A. Kouaouci, Worlds in motion, understanding international migration at the end

<!-- b000591 | references | pages [19] -->
of the millennium. Clarendon, Oxford, UK.1998.

<!-- b000592 | references | pages [19] -->
[8] Frontex Risk Analysis Network Quarterly Report

<!-- b000593 | references | pages [19] -->
http://frontex. europa. eu/publications/

<!-- b000594 | heading | pages [20] -->
A Letter to UN: A Policy Recommendation For The World Concern

<!-- b000595 | prose | pages [20] -->
Dear Sir,

<!-- b000596 | prose | pages [20] -->
Upon hearing that the UN Commission is holding a policy strategy meeting to collect insights

<!-- b000597 | prose | pages [20] -->
aiming to figure out a set of policies that ensures an optimal migration pattern for the refugees,

<!-- b000598 | prose | pages [20] -->
I and my fellow colleagues are honored to engage in clearly communicating our role and scope

<!-- b000599 | prose | pages [20] -->
of engagement in the refugee crisis response as an aspiration of the whole human race. We have

<!-- b000600 | prose | pages [20] -->
been working with painstaking efforts so as to do something for the world concern of refugee

<!-- b000601 | prose | pages [20] -->
crisis, and we do have some outcome by researching day and night these days, which we hope

<!-- b000602 | prose | pages [20] -->
can be of help in providing a two way communication with the refugees and migrants already

<!-- b000603 | prose | pages [20] -->
arrived as well as with the host communities will be essential to maintain social peace and

<!-- b000604 | prose | pages [20] -->
ensuring mutual understanding in Europe.

<!-- b000605 | prose | pages [20] -->
Inspired by Gravity model, we provide a smart migration model that simulates the random flow

<!-- b000606 | prose | pages [20] -->
of refugees, coinciding with real statistics and suiting the dynamic and sophisticated features of

<!-- b000607 | prose | pages [20] -->
migrants in Europe. Based on the results of our model, we recommend some feasible policies

<!-- b000608 | prose | pages [20] -->
for your reference.

<!-- b000609 | prose | pages [20] -->
The policy strategy and priorities will be based humanitarian needs for refugees and migrants

<!-- b000610 | prose | pages [20] -->
arriving Europe. However, it also takes into account the increasing restrictions being placed on

<!-- b000611 | prose | pages [20] -->
people entering Europe. As is shown in our modeling results, the oversaturation of refugees

<!-- b000612 | prose | pages [20] -->
may lead to the problem of detention and illegal immigration as the receiving number in each

<!-- b000613 | prose | pages [20] -->
European countries is limited. Once locked out, the resources and supplies will soon run out,

<!-- b000614 | prose | pages [20] -->
thus triggering the extra inflow or illegal stay of refugees. So we strongly suggest that the

<!-- b000615 | prose | pages [20] -->
humanitarian response and longer term accommodation, resources and services for migrants

<!-- b000616 | prose | pages [20] -->
and refugees should be in abundance. Both GOs and NGOs ought to set a plan for providing

<!-- b000617 | prose | pages [20] -->
certain kind of humanistic response such as basic material resources, health-care, and shelters.

<!-- b000618 | prose | pages [20] -->
Another determinant in refugee crisis is Partnership and  Coordination between GO and GO,

<!-- b000619 | prose | pages [20] -->
NGO and NGO, NGO and GO. Both groups are involved through advocacy activities,

<!-- b000620 | prose | pages [20] -->
collection of donations and volunteering. Daily coordination meetings with the participation of

<!-- b000621 | prose | pages [20] -->
UNHCR are taking place at the main border entry and exit points, and we highly recommend

<!-- b000622 | prose | pages [20] -->
that other organizations follow the example

<!-- b000623 | prose | pages [20] -->
The proposed partnership and lead coordination role of different organizations will further

<!-- b000624 | prose | pages [20] -->
enhance coordination to provide more thorough background information and break the culture

<!-- b000625 | prose | pages [20] -->
division to an extent.

<!-- b000626 | prose | pages [20] -->
Best regards，

<!-- b000627 | prose | pages [20] -->
Sincerely
