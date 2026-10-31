# P-D-2023-2303967-354e9177

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen 2023

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | prose | pages [1] -->
MCM/ICM

<!-- b000004 | title | pages [1] -->
D

<!-- b000005 | title | pages [1] -->
2303967

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
DIGNP: Dynamic Indicator-Goal Network for

<!-- b000008 | title | pages [1] -->
Prioritization

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
The UN has established 17 Sustainable Development Goals (SDGs) to address global challenges related to economic, technological, and environmental issues, among others. To make the world a better place, in order to grasp the priority relationship of SDG, we develop the Dynamics Indicator-Goal Network for Prioritization (DIGNP).

<!-- b000011 | prose | pages [1] -->
First of all, to create a network of the SDGs that can capture the complex and dynamic relationships between the different goals and their linkages over time, we utilized System Dynamics modeling. To begin with our model, we first select several most influential indicators of each SDG using correlation. Then we lay out the Indicator Network and the correspondent Goal Network. The relationships between the goals are assessed by comprehensively analyzing the correlations between indicators and the impact of indicators on the goals.

<!-- b000012 | prose | pages [1] -->
Next, we establish a priority evaluation system that prioritizes SDGs and predicts their impact and achievement over the next decade following the initiation of priority. Based on the topology of the constructed SDG Network, we have developed five key indicators for measuring the priority of each goal. Using the Entropy Weight Method, we then develop our SDG Priority Ranking System. The first five SDGs are SDG 17, SDG 3, SDG 1, SDG 4, SDG 13, ranked by priority. Based on the priority, we forecast the future evolution of the SDGs by Auto Regressive Integrated Moving Average (ARIMA). Our analysis indicates that if our priorities are initiated, SDGs will improve faster by a priority term.

<!-- b000013 | prose | pages [1] -->
Furthermore, considering the goal adjustment, our dynamic SDG Network automatically adjusts its topology and priority rankings based on changes in any indicator or goal nodes. Goal accomplishment cause subtraction of the node in our networks, which alter edge weight and the priority score. Goal addition lead to addition of the node in our networks. Our results show that incorporating Access to Information and Communication Technologies as a new SDG is critical to enhancing the connection between SDGs and advancing their achievement.

<!-- b000014 | prose | pages [1] -->
Meanwhile, the network topology and priority of the SDGs can also be significantly impacted by various international crises, influencing the progress of UN. In the case of forest fires, SDG 13, SDG 15, SDG 11 are underlined, and they call UN to implement SDG-aligned initiatives that foster resilience and sustainable development. It is crucial for the UN to recognize these potential impacts and adjust its strategy to address the most urgent challenges as they emerge.

<!-- b000015 | prose | pages [1] -->
Finally, we promote the construction of our SDG Network and prioritization to a general model Dynamics Indicator-Goal Network for Prioritization. With reasonable data input, a global, dynamic and automatic Indicator and Goal Network can be constructed and priorities can be figure out. What’s more, we design a User Interface for those who utilize our DIGNP model.

<!-- b000016 | keywords | pages [1] -->
Keywords: Sustainable Development Goals, System Dynamics, Dynamic Network, Priority Evaluation,

<!-- b000017 | prose | pages [1] -->
Correlation Coefficient, CVM, EWM, ARIMA

<!-- b000018 | furniture | pages [2] -->
Team 2303967

<!-- b000019 | furniture | pages [2] -->
Page 1 of 24

<!-- b000020 | heading | pages [2] -->
Contents

<!-- b000021 | contents | pages [2] -->
1 Introduction

<!-- b000022 | contents | pages [2] -->
2

<!-- b000023 | contents | pages [2] -->
1.1

<!-- b000024 | contents | pages [2] -->
Background and Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
1.2

<!-- b000027 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
2 Definitions, Assumptions and Notations

<!-- b000030 | contents | pages [2] -->
2

<!-- b000031 | contents | pages [2] -->
3 SDG Network Construction by System Dynamics

<!-- b000032 | contents | pages [2] -->
4

<!-- b000033 | contents | pages [2] -->
3.1

<!-- b000034 | contents | pages [2] -->
Data Pre-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
5

<!-- b000036 | contents | pages [2] -->
3.2

<!-- b000037 | contents | pages [2] -->
Selection of Indicators by Correlation

<!-- b000038 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5

<!-- b000040 | contents | pages [2] -->
3.3

<!-- b000041 | contents | pages [2] -->
Indicators and SDGs Interactivity

<!-- b000042 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
7

<!-- b000044 | contents | pages [2] -->
3.4

<!-- b000045 | contents | pages [2] -->
Section Summary: from Indicator Network to Goal Network . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
9

<!-- b000047 | contents | pages [2] -->
4 Dynamic SDG Network with Priority-oriented and Time-based Development

<!-- b000048 | contents | pages [2] -->
10

<!-- b000049 | contents | pages [2] -->
4.1

<!-- b000050 | contents | pages [2] -->
SDG Priority Evaluation System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
10

<!-- b000052 | contents | pages [2] -->
4.2

<!-- b000053 | contents | pages [2] -->
Priority-Oriented Development Prediction by ARIMA . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
13

<!-- b000055 | contents | pages [2] -->
5 Dynamic SDG Network with Goal Adjustment

<!-- b000056 | contents | pages [2] -->
15

<!-- b000057 | contents | pages [2] -->
5.1

<!-- b000058 | contents | pages [2] -->
Subtraction of the Node: Goal Accomplishment . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
15

<!-- b000060 | contents | pages [2] -->
5.2

<!-- b000061 | contents | pages [2] -->
Addition of the Node: Goal Inclusion

<!-- b000062 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
17

<!-- b000064 | contents | pages [2] -->
6 Dynamic SDG Network with by Global Crises

<!-- b000065 | contents | pages [2] -->
18

<!-- b000066 | contents | pages [2] -->
6.1

<!-- b000067 | contents | pages [2] -->
The Impact of International Crises on Dynamic SDG Network . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
18

<!-- b000069 | contents | pages [2] -->
6.2

<!-- b000070 | contents | pages [2] -->
Effect on the Progress of UN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
20

<!-- b000072 | contents | pages [2] -->
7 Generalized Priority Network: DIGNP

<!-- b000073 | contents | pages [2] -->
21

<!-- b000074 | contents | pages [2] -->
8 Sensitivity Analysis

<!-- b000075 | contents | pages [2] -->
22

<!-- b000076 | contents | pages [2] -->
9 Strength and Weakness

<!-- b000077 | contents | pages [2] -->
22

<!-- b000078 | contents | pages [2] -->
10 References

<!-- b000079 | contents | pages [2] -->
23

<!-- b000080 | contents | pages [2] -->
11 Appendix

<!-- b000081 | contents | pages [2] -->
24

<!-- b000082 | furniture | pages [3] -->
Team 2303967

<!-- b000083 | furniture | pages [3] -->
Page 2 of 24

<!-- b000084 | heading | pages [3] -->
1 Introduction

<!-- b000085 | heading | pages [3] -->
1.1 Background and Problem Restatement

<!-- b000086 | prose | pages [3] -->
The United Nations (UN) has identified 17 Sustainable Development Goals (SDGs) to enhance the lives of people worldwide. These goals address pressing global challenges related to economics, technology, the environment,etc., and are interdependent, meaning progress in one area can affect others in positive or negative ways.[1] Achieving all SDGs is a dynamic process subject to limitations in funding and other resources, as well as global events such as climate change.

<!-- b000087 | prose | pages [3] -->
Therefore, setting priorities for these goals is urgent for the UN and other global institutes. To help with this, our team proposes the following tasks:

<!-- b000088 | heading | pages [3] -->
1. First, construct a network involving 17 SDGs to shown their relationship.

<!-- b000089 | heading | pages [3] -->
2. Next, establish priority evaluation system to prioritize SDGs and move the UN’s work forward.

<!-- b000090 | prose | pages [3] -->
Then predict the impact and achievement for the next 10 years after priority initiation.

<!-- b000091 | prose | pages [3] -->
3. Furthermore, analyze the impact of achieving one SDG on the network structure and priorities, and propose additional SDGs to the UN with their possible impact.

<!-- b000092 | prose | pages [3] -->
4. Meanwhile, discuss the effects of global crises such as technological advances, global pandemics, climate change, regional wars, and refugee movements on our network and priority. From this point, summarize their effects on UN.

<!-- b000093 | prose | pages [3] -->
5. Finally, generalize the SDG network approach to other circumstance, so as to help other organiza- tions set priorities for their goals.

<!-- b000094 | heading | pages [3] -->
1.2 Our Work

<!-- b000095 | prose | pages [3] -->
Our work flow of this paper is shown in Figure 1 on Page 3.

<!-- b000096 | heading | pages [3] -->
2 Definitions, Assumptions and Notations

<!-- b000097 | prose | pages [3] -->
To help our reader better grasp the idea of our network, some basic definitions are listed below.

<!-- b000098 | prose | pages [3] -->
• Indicator: Indicators for the SDGs are specific and measurable targets that are used to track progress towards achieving the goals

<!-- b000099 | prose | pages [3] -->
• Goal Node: Nodes representing 17 SDGs

<!-- b000100 | prose | pages [3] -->
• Indicator Node: Nodes representing indicators of each SDG

<!-- b000101 | prose | pages [3, 4] -->
• Indicator Network: A weighted oriented graph, with all indicator nodes as vertexes, and each indicator node connected to one goal node • Goal Network: A weighted oriented graph, with all goal node as vertexes

<!-- b000102 | furniture | pages [4] -->
Team 2303967

<!-- b000103 | furniture | pages [4] -->
Page 3 of 24

<!-- b000104 | caption | pages [4] -->
Figure 1: Our Work: Dynamic Indicator-Goal Network for Prioritization

<!-- b000106 | prose | pages [4] -->
• Edge Weight (of Indicator Network or Goal Network): Weight of each edge connecting indicator nodes in Indicator Network or connecting goal nodes in SDG Network, whose value tells the strength of influence between the indicators or between the SDGs

<!-- b000107 | prose | pages [4] -->
We make the following major assumptions to build our model.

<!-- b000108 | prose | pages [4] -->
• Assumption 1: When the officially-given indicators of a SDG reach their optimal value and stay optimal for a certain period, we say that the SDG is achieved.

<!-- b000109 | prose | pages [4] -->
Justification: Fluctuation above and below the target line implies instability. What we expect is time-durable improvement of each goal.

<!-- b000110 | prose | pages [4] -->
• Assumption 2: We assume that the nodes in the network stay connected and impact each other in a relatively fast speed (within several months or a year).

<!-- b000111 | furniture | pages [5] -->
Team 2303967

<!-- b000112 | furniture | pages [5] -->
Page 4 of 24

<!-- b000113 | prose | pages [5] -->
Justification: With the impact of UN, different departments will be closely linked, and the progress of one SDG will impact the others in a relatively fast speed.

<!-- b000114 | prose | pages [5] -->
• Assumption 3: Statistical properties of the network such as the indicators’ data will not change abruptly and stays predictable.

<!-- b000115 | prose | pages [5] -->
Justification: Major influence factors are continuous and relatively stable within a short term.

<!-- b000116 | prose | pages [5] -->
In this paper, some important notations are listed in Table 1.

<!-- b000117 | caption | pages [5] -->
Table 1: Definitions of the Model Variable Parameters

<!-- b000118 | prose | pages [5] -->
Symbol Definition

<!-- b000119 | prose | pages [5] -->
INet The graph of Indicator Network GNet The graph of Goal Network The ith Goal of SDGs, i = 1, · · · , 17 Gi Ii(j) The jth indicator of the ith Goal of SDGs Wind(Ii(j) →Ii′(j′)) The edge weight in the Indicator Network Wgoal(Gi →Gj) The edge weight in the SDG Network λ((Ii(j)) The contribution(weight) of Ii(j) to Gi µ1, · · · , µ5 The weight of 5 priority indicators Y Number of years that we collect data of each Ii(j) PS(Gi) Priority score of Gi PFm(n) Priority factor from priority Gm to affected Gm

<!-- b000120 | heading | pages [5] -->
3 SDG Network Construction by System Dynamics

<!-- b000121 | caption | pages [5] -->
Figure 2: Flow Chart of the SDG Network Construction

<!-- b000122 | furniture | pages [6] -->
Team 2303967

<!-- b000123 | furniture | pages [6] -->
Page 5 of 24

<!-- b000124 | heading | pages [6] -->
3.1 Data Pre-processing

<!-- b000125 | heading | pages [6] -->
3.1.1 Data Collection

<!-- b000126 | prose | pages [6] -->
First, data for the 17 SDGs and their indicators are collected. To guarantee the accuracy and authority of our data, we choose the following official database. Data of 241 officially given indicators [1] of 17 SDGs, from 2000 to 2022, are collected. In the following analysis, Y = 23.

<!-- b000127 | caption | pages [6] -->
Table 2: Data Sources

<!-- b000128 | prose | pages [6] -->
Data Source Website

<!-- b000129 | prose | pages [6] -->
UN Statistics https://unstats.un.org/sdgs/dataportal SDG DATA GATEWAY Explorer https://dataexplorer.unescap.org/ Food and Agriculture Organization of UN https://www.fao.org/home/en/

<!-- b000130 | heading | pages [6] -->
3.1.2 Data Normalization

<!-- b000131 | prose | pages [6] -->
In order to eliminate the influence of different units and dimensions, we normalize the data of each indicators as xnor, according to their optimal value xopt.

<!-- b000132 | prose | pages [6] -->
• For “cost-minimized” indicators: x −xopt xnor = (1) xmax −xopt

<!-- b000133 | prose | pages [6] -->
• For “benefit-maximized” indicators:

<!-- b000134 | prose | pages [6] -->
xopt −x xnor = (2) xopt −xmin

<!-- b000135 | prose | pages [6] -->
If xnor = 0, the corresponding indicator is noted as “achieved”. All negative value of xnor will be recorded as zero, which indicates “over-achievement”. When all the indicators of one SDG are “achieved” for a period of time, we can view this SDG as “achieved”.

<!-- b000136 | heading | pages [6] -->
3.2 Selection of Indicators by Correlation

<!-- b000137 | prose | pages [6] -->
To increase the efficiency of our model, we use correlation analysis to select the most influential indicators for each SDG.

<!-- b000138 | prose | pages [6] -->
Take the indicator selection process of SDG 7 Affordable and Clean Energyas an example. There are six indicators for SDG 7, we denote them as follows.1

<!-- b000139 | prose | pages [6, 7] -->
1Full name of six indicators are: 1.Proportion of population with access to electricity; 2.Proportion of population with primary reliance on clean fuels and technology; 3.Renewable energy share in the total final energy consumption; 4.Energy intensity measured in terms of primary energy and GDP; 5.International financial flows to developing countries for clean energy research and development and renewable energy production; 6.Installed renewable energy-generating capacity in developing countries.[1] Official Code Indicator Official Code Indicator Official Code Indicator

<!-- b000140 | furniture | pages [7] -->
Team 2303967

<!-- b000141 | furniture | pages [7] -->
Page 6 of 24

<!-- b000142 | caption | pages [7] -->
Table 3: Six Official Indicators of SDG 7

<!-- b000144 | prose | pages [7] -->
C070101 PPAE C070102 PPCFT C070201 RESEC C070301 EIGDP C070a01 IntAid C200208 IREGC

<!-- b000145 | prose | pages [7] -->
We calculate the correlation coefficient between two indicators by:

<!-- b000146 | prose | pages [7] -->
PY y=1(xyi −¯xi)(xyj −¯xj) rij = (3) qPY y=1(xyi −¯xi)2 PY y=1(xyj −¯xj)2

<!-- b000147 | prose | pages [7] -->
Considering positive and negative correlation, we use the absolute value of each rij to develop the correlation matrix. Heat-map the correlation between six indicators are shown in Figure 3.

<!-- b000148 | caption | pages [7] -->
Figure 3: Correlation between Six Indicators of SDG 7

<!-- b000149 | prose | pages [7] -->
We define the total correlation within this group of jth indicator to be:

<!-- b000150 | prose | pages [7] -->
n X |rij| ri,total = (4) j=1

<!-- b000151 | prose | pages [7] -->
ri,total evaluates the capability of the ith indicator to interpret other indicators’ trend. The higher the ri,total, the more trend of other indicators can be reflected by the ith indicator’s pattern.

<!-- b000152 | caption | pages [7] -->
Table 4 shows each indicator’s ri,total in descend order.

<!-- b000153 | caption | pages [7] -->
Table 4: Rank of Six Indicators of SDG 7

<!-- b000154 | prose | pages [7] -->
Indicator Total Correlation Rank Indicator Total Correlation Rank

<!-- b000155 | prose | pages [7] -->
IREGC 5.505261807 1 EIGDP 5.409986028 4 PPCFT 5.488285432 2 IntAid 4.911156508 5 PPAE 5.431849345 3 RESEC 4.186710177 6

<!-- b000156 | prose | pages [7] -->
Accordingly, we select two indicators for SDG 7:

<!-- b000157 | furniture | pages [8] -->
Team 2303967

<!-- b000158 | furniture | pages [8] -->
Page 7 of 24

<!-- b000159 | prose | pages [8] -->
1. Installed renewable energy-generating capacity in developing countries (in watts per capita)

<!-- b000160 | prose | pages [8] -->
2. Proportion of population with primary reliance on clean fuels and technology

<!-- b000161 | prose | pages [8] -->
A full list of selected indicators for other 16 SDGs can be found in Appendix.

<!-- b000162 | heading | pages [8] -->
3.3 Indicators and SDGs Interactivity

<!-- b000163 | heading | pages [8] -->
3.3.1 Analyze Edge Weight between Indicators with Correlation

<!-- b000164 | prose | pages [8] -->
Next, we look into the relationship between indicators between SDGs, with which we determine the edge weight of Indicator Network.

<!-- b000165 | prose | pages [8] -->
Given two SDG Gm and Gn, we construct the matrix using indicator vector of Y years, where xyj stands for the yth year jth factors in the sequence (Im(1), · · · , In(1), · · · ). we calculate the correlation coefficient between any two indicators by

<!-- b000166 | prose | pages [8] -->
PY y=1(xyi −¯xi)(xyj −¯xj) rij = (5) qPY y=1(xyi −¯xi)2 PY y=1(xyj −¯xj)2

<!-- b000167 | prose | pages [8] -->
 44  = 946 correlation coefficients of each indicators, we obtain a fully-connected By computing 2 indicator network. The weight of each edge is

<!-- b000168 | prose | pages [8] -->
Wind(Im(i) →In(j)) = Wind(In(j) →Im(i)) = rij = rji (6)

<!-- b000169 | caption | pages [8] -->
Figure 4 shows an example of a local indicator network. Here, the width of each edge represent its

<!-- b000170 | prose | pages [8] -->
weight.

<!-- b000171 | caption | pages [8] -->
Figure 4: a Local Indicator Network between SDG 3 and SDG 6

<!-- b000172 | heading | pages [8] -->
3.3.2 Analyze Edge Weight between SDGs with CVM

<!-- b000173 | prose | pages [8, 9] -->
The basic idea of Coefficient of Variation Method(CVM) is to assign a weight to each index according to the degree of variation between the current value and the target value. Larger gap means that the index is harder to reach the target value, so a greater weight should be assigned.

<!-- b000174 | furniture | pages [9] -->
Team 2303967

<!-- b000175 | furniture | pages [9] -->
Page 8 of 24

<!-- b000177 | prose | pages [9] -->
Firstly, average value and standard deviation of indicator In(j) of Gn are

<!-- b000178 | prose | pages [9] -->
v Y Y u ¯x(In(j)) = 1 1 X X u [xy(In(j)) −¯x(In(j))] xy(In(j)) S(In(j)) = (7) t Y −1 Y y=1 y=1

<!-- b000179 | prose | pages [9] -->
Second, the variation coefficient and weight of each indicator In(j) of Gn are

<!-- b000180 | prose | pages [9] -->
V (In(j)) = S(In(j)) V (In(j)) λ(In(j)) = (8) P ¯x(In(j)) j=1 V (In(j))

<!-- b000181 | prose | pages [9] -->
Next, for Goals Gm and Gn, m, n ∈[1, 17], we define the interactivity from Gm to In(j) of Gn to be

<!-- b000182 | prose | pages [9] -->
X λ(In(j)) · W(Im(i) →In(j)) InactGm→In(j) = (9) Im(i)∈INet

<!-- b000183 | prose | pages [9] -->
Finally, we obtain interactivity from Gm to Gn, calculated by

<!-- b000184 | prose | pages [9] -->
X InactGm→Gn = InactGm→In(j) (10) In(j)∈INet

<!-- b000185 | prose | pages [9] -->
which is the edge weight from Gm to Gn. That is

<!-- b000186 | prose | pages [9] -->
Wgoal(Gm →Gn) = InactGm→Gn (11)

<!-- b000187 | caption | pages [9] -->
Figure 5 and Figure 6 graphically illustrate the calculation of interactivity.

<!-- b000188 | caption | pages [9] -->
Figure 5: Illustration of Interactivity

<!-- b000189 | caption | pages [9] -->
Figure 6: Illustration of Interactivity

<!-- b000190 | prose | pages [9] -->
from G3 to I6(1) from G3 to G6

<!-- b000191 | prose | pages [9, 10] -->
For convenience of later analysis, we normalize the weight of all edges to the range [0,10] and round them to 2 decimals. In the SDG Network in Figure 72, larger edge weight stands for higher influence of the source node SDG to the target node SDG. Connections between SDG 17 and other SDGs are highlighted.

<!-- b000192 | furniture | pages [10] -->
Team 2303967

<!-- b000193 | furniture | pages [10] -->
Page 9 of 24

<!-- b000195 | caption | pages [10] -->
Figure 7: SDG Network (with Edge of SDG 17 Highlighted)

<!-- b000196 | heading | pages [10] -->
3.4 Section Summary: from Indicator Network to Goal Network

<!-- b000197 | prose | pages [10] -->
To create a network of the SDGs that allows us to model the complex, dynamic relationships between the different goals and their interlinkages over time, we build the model based on System Dynamics modeling. System Dynamics modeling is a powerful tool to identify the dynamic nature of problems and analyze the interactions between different variables of a system.[2]

<!-- b000198 | prose | pages [10] -->
The SDGs are interconnected. Progress in one SDG can affects progress in other SDGs. System Dynamics provides a framework for understanding these interconnections and feedback loops and for simulating the impacts of different policies and interventions on the SDGs. By modeling the system as a whole, rather than just focusing on individual SDGs in isolation, we can better understand the potential unintended consequences of different policies and identify more effective strategies for achieving the SDGs.

<!-- b000199 | prose | pages [10] -->
Our innovative idea is the mapping relationship between Indicator Network and Goal Network. Once we construct network among indicators with their correlation, a correspondent Goal Network is automatically generated. This thought is illustrated in Figure 8.

<!-- b000200 | prose | pages [10, 11] -->
2Icons from https://www.dreamstime.com In the SDG Network, all goal nodes are interconnected. This feature stands in line with the reality. For instance, SDG 5 (Gender Equality) is closely linked to SDG 8 (Decent Work and Economic Growth), as empowering women and girls is vital to creating a more inclusive and equitable economy. SDG 16 (Peace, Justice and Strong Institutions) is dependent on the achievement of many other SDGs as it is difficult to achieve peaceful and just societies without addressing issues such as poverty, inequality, and lack of access to education and healthcare. Therefore, it is important to view the SDGs as a whole and to work towards achieving them in an integrated and coordinated manner.

<!-- b000201 | furniture | pages [11] -->
Team 2303967

<!-- b000202 | furniture | pages [11] -->
Page 10 of 24

<!-- b000203 | caption | pages [11] -->
Figure 8: Mapping relationship between Indicator Network and Goal Network

<!-- b000205 | heading | pages [11] -->
4 Dynamic SDG Network with Priority-oriented and Time-based

<!-- b000206 | prose | pages [11] -->
Development

<!-- b000207 | heading | pages [11] -->
4.1 SDG Priority Evaluation System

<!-- b000208 | heading | pages [11] -->
4.1.1 Priority Indicators

<!-- b000209 | prose | pages [11] -->
Based on the topology of the constructed SDG Network, we mainly develop 5 indicators for priority measurement of each goal. We also give the calculation methods of these indicators in the following paragraphs.

<!-- b000210 | heading | pages [11] -->
1. Node Efficiency (NE)[3]

<!-- b000211 | prose | pages [11] -->
Node Efficiency evaluates how difficult can we reach other nodes in the graph starting from the source node. Usually, edge weight is used as an index of accessibility: the greater the weight, the easier to travel.

<!-- b000212 | prose | pages [11] -->
When we apply it to SDG Network, it tells how much UN can achieve in other SDGs while focusing and working hard on one SDG. It is formulated as:

<!-- b000213 | prose | pages [11] -->
n 1 X Wgoal(Gi →Gj) NE(Gi) = (12) n −1 Gj∈GNet

<!-- b000214 | furniture | pages [12] -->
Team 2303967

<!-- b000215 | furniture | pages [12] -->
Page 11 of 24

<!-- b000216 | heading | pages [12] -->
2. Weighted Eigenvector Centrality (WEC)[4]

<!-- b000217 | prose | pages [12] -->
Eigenvector Centrality accounts for the significance of a node’s neighbours. The more influential the neighbouring node is, the higher the eigenvector centrality.

<!-- b000218 | prose | pages [12] -->
That is to say, if a SDG is tied to some other SDG with high priority, this SDG is bound to have a relatively high priority. However, since our SDG Network is a complete graph, all vertexes are linked, we modify traditional eigenvector centrality as weighted eigenvector centrality.

<!-- b000219 | prose | pages [12] -->
To calculate WEC, we define the weighted adjacency matrix to be A = (aij), such that

<!-- b000220 | prose | pages [12] -->
( aij = 0, i = j (13) i̸ = j aij = wij,

<!-- b000221 | prose | pages [12] -->
WEC is formulated as WEC(Gi) = 1 X aijWEC(Gj) (14) λ Gj∈GNet

<!-- b000222 | prose | pages [12] -->
where λ is the largest eigenvalue of matrix A = (aij).

<!-- b000223 | heading | pages [12] -->
3. Betweenness Centrality (BC)[5]

<!-- b000224 | prose | pages [12] -->
Betweenness centrality refers to the frequency with which a node lies on the shortest path between two other nodes in a network. In reality, if a SDG situated in the shortest path between other two SDGs frequently, it must have higher priority to be initiated, since it acts as a bridge between the interaction of other goals.

<!-- b000225 | prose | pages [12] -->
Since greater weight in SDG Network represents greater interactivity, it is negatively proportional to the path length between SDGs. Thus we define the path length of each edge as

<!-- b000226 | prose | pages [12] -->
1 d(Gi →Gj) = (15) W(Gi →Gj)

<!-- b000227 | prose | pages [12] -->
and apply Dijkstra Algorithm to calculate the shortest paths.

<!-- b000228 | prose | pages [12] -->
Then the Betweenness Centrality of Gi should be

<!-- b000229 | prose | pages [12] -->
σGj→Gk(Gi) X BC(Gi) = (16) σGj→Gk Gi̸=Gj̸=Gk

<!-- b000230 | prose | pages [12] -->
where σGj→Gk(Gi) equals to the number of times that shortest paths between other nodes bypass Gi, while σGj→Gk equals to total shortest path counts.

<!-- b000231 | heading | pages [12] -->
4. Sum of Relative Influence Intensity (SRI)[3]

<!-- b000232 | prose | pages [12] -->
Noticeably, the priority of each goal is not only determined by how much it interacts with its neighbouring goal, but also how drastically other goals affect its neighbour. That is, the proportion it takes on other goals’ “received impact”.

<!-- b000233 | furniture | pages [13] -->
Team 2303967

<!-- b000234 | furniture | pages [13] -->
Page 12 of 24

<!-- b000235 | prose | pages [13] -->
We numerically measure such proportion by Relative Influence Intensity RI.

<!-- b000236 | prose | pages [13] -->
W(Gi →Gj) RI(Gi →Gj) = (17) P k̸=j W(Gk →Gj)

<!-- b000237 | prose | pages [13] -->
Then, Sum of Relative Influence Intensity is

<!-- b000238 | prose | pages [13] -->
X RI(Gi →Gj) SRI(Gi) = (18) j̸=i

<!-- b000239 | heading | pages [13] -->
5. Sum of Maximum Network Flow (SMNF)

<!-- b000240 | prose | pages [13] -->
If we view each weighted edge as a flow container, maximum network flow from source node Gi to terminal node Gj show how much output of the jth SDG can be earned from input in the ithe SDG. In order to attain SMNF(Gi), we first solve the maximum network flow problem below.

<!-- b000241 | prose | pages [13] -->
MNF(Gi →Gj) = max NF(Gi →Gj) i̸ = j   NF(Gi →Gj), p = i  P flow(Gp →Gq) −P flow(Gq →Gp) =     −NF(Gi →Gj), p = j   (19)    s.t. 0, k̸ = i, j   0 ≤flow(Gp →Gq) ≤W(Gp →Gq)      0 ≤flow(Gq →Gp) ≤W(Gq →Gp) 

<!-- b000242 | prose | pages [13] -->
With the aid of Ford-Fulkerson algorithm, we get MNF(Gi →Gj) for all j. Then sum of maximum network flow of Gi is:

<!-- b000243 | prose | pages [13] -->
X MNF(Gi →Gj) SMNF(Gi) = (20) i̸=j

<!-- b000244 | heading | pages [13] -->
4.1.2 Evaluate Priority Score by EWM

<!-- b000245 | prose | pages [13] -->
Now we can develop our SDG Priority Ranking System with the aid of 5 priority indicators. Entropy Weight Method (EWM) is an objective weighting method. It gives larger weight to the indicators that provide more information, so that we can distinguish data with more ease. From this point, we set the Priority Score of Gi to be

<!-- b000246 | prose | pages [13] -->
PS(Gi) = µ1 · NE(Gi) + µ2 · WEC(Gi) + µ3 · BC(Gi) + µ4 · SRI(Gi) + µ5 · SMNF(Gi) (21)

<!-- b000247 | prose | pages [13] -->
where weight index µ1, · · · , µ5 is calculated by EWM.

<!-- b000248 | prose | pages [13] -->
The result of each weight and the priority ranking result is shown in Table 5 and Table 6.

<!-- b000249 | furniture | pages [14] -->
Team 2303967

<!-- b000250 | furniture | pages [14] -->
Page 13 of 24

<!-- b000251 | caption | pages [14] -->
Table 5: EWM Weight of Priority Indicators

<!-- b000252 | prose | pages [14] -->
NE WEC BC SRI SMNF

<!-- b000253 | prose | pages [14] -->
0.1058 0.2470 0.1085 0.3218 0.2169

<!-- b000254 | caption | pages [14] -->
Table 6: Top 5 Priority Ranking Result by Descending Order

<!-- b000255 | prose | pages [14] -->
Priority Rank SDG Priority Score

<!-- b000256 | prose | pages [14] -->
1 SDG17: Partnerships to achieve the Goal 6.2875 2 SDG3: Good Health and Well-being 5.9972 3 SDG1: No proverty 5.9725 4 SDG4: Quality Education 5.8123 5 SDG13: Climate Action 5.4183

<!-- b000257 | prose | pages [14] -->
Compared with the SDG priority proposed by the Copenhagen Consensus Center [8], our priority ranking is reasonable and applicable to real-world development. It’s not surprising that SDG17: Part- nerships to achieve the Goal is the top priority ranks first, as only if all countries collaborate under the guidance of UN can we achieve other goals efficiently.

<!-- b000258 | heading | pages [14] -->
4.2 Priority-Oriented Development Prediction by ARIMA

<!-- b000259 | heading | pages [14] -->
4.2.1 Combination of ARIMA and Priority Factor

<!-- b000260 | prose | pages [14] -->
With the advancement of science and technology, and with the increasing focus on sustainable development, human development, and collaboration, it is expected that progress towards achieving SDGs [6] will continue. However, the degree of progress made will depend on various factors such as economic development, technological innovation, political stability, and environmental sustainability [7]. To forecast the future trends, we can use the auto regressive integrated moving average (ARIMA), which is a quantitative prediction tool that combines historical trend data with assumptions about future trends and scenarios.

<!-- b000261 | prose | pages [14] -->
If our priorities are initiated, the improvement of SDGs will be positively influenced. Therefore, we add priority term to the ARIMA result. Combining priority influence with ARIMA prediction, we can better estimate the impact of one SDG on another.

<!-- b000262 | prose | pages [14] -->
First, we forecast the trend of each indicator by ARIMA.

<!-- b000263 | prose | pages [14] -->
Next, we define the priority factor PFm(n) as follow.

<!-- b000264 | prose | pages [14] -->
PFm(n) = PS(Gm) · PS(Gn) (22) (PS(Gi))]2 [max i

<!-- b000265 | prose | pages [14] -->
If Gm is set as the priority in the next period, PFm(n) times of Gm advance will be added to Gn advance.

<!-- b000266 | furniture | pages [15] -->
Team 2303967

<!-- b000267 | furniture | pages [15] -->
Page 14 of 24

<!-- b000268 | caption | pages [15] -->
Figure 9: Flow Chart of the ARIMA Prediction with Priority Term

<!-- b000269 | prose | pages [15] -->
Finally, we add priority term to ARIMA result and visualize the reasonable achievement.

<!-- b000270 | prose | pages [15] -->
Prediction Result(Gn) = ARIMA result(Gn) + PFm(n) · ARIMA result(Gm) (23)

<!-- b000271 | heading | pages [15] -->
4.2.2 Achievement in 2023 under Priority initiation

<!-- b000272 | caption | pages [15] -->
Figure 10 and 11 show the result of adding correlation impact in the network. We can see that when

<!-- b000273 | prose | pages [15] -->
we consider the impact of the dynamic network and the priority, the SDGs will be driven by each other.

<!-- b000274 | prose | pages [15] -->
For example, achieving SDG 1 (No Poverty) could be a driver for achieving SDG 3 (Good Health and Well-Being), as poverty can lead to poor health outcomes. In turn, achieving SDG 3 could be a driver for achieving SDG 4 (Quality Education), as healthier children may be more likely to attend and perform well in school.

<!-- b000275 | prose | pages [15] -->
By placing SDG17(Partnership to achieve the Goal) in the first priority, reasonable promotion of SDG 1 and 3 are shown in Figure 10 and 11.

<!-- b000276 | caption | pages [15] -->
Figure 10: Prediction of the Proportion of the

<!-- b000277 | caption | pages [15] -->
Figure 11: Prediction of World Life Expectancy

<!-- b000278 | prose | pages [15, 16] -->
Population Living below the International (indicator of SDG 3) Poverty Line (indicator of SDG 1) By estimating the 17 SDGs’ progress, we can see from the figure that SDG 1 (No poverty) is reasonable to be achieved in the next 10 years, and it is likely that 95% people can have access to affordable and clean energy.

<!-- b000279 | furniture | pages [16] -->
Team 2303967

<!-- b000280 | furniture | pages [16] -->
Page 15 of 24

<!-- b000282 | prose | pages [16] -->
In the next 10 years, it is reasonable to achieve significant progress towards these priorities if sufficient resources and support are provided by solid global partnership. For example, progress can be made towards reducing greenhouse gas emissions and increasing renewable energy adoption, expanding access to quality education, promoting healthy lifestyles, and investing in sustainable urban planning. While it may not be possible to achieve all SDGs completely, significant progress can be made towards creating a more sustainable and equitable world.

<!-- b000283 | heading | pages [16] -->
5 Dynamic SDG Network with Goal Adjustment

<!-- b000284 | prose | pages [16] -->
Our dynamic SDG Network will adjust its topology as well as priority rank automatically in accordance with the modification of any indicator node and goal node.

<!-- b000285 | heading | pages [16] -->
5.1 Subtraction of the Node: Goal Accomplishment

<!-- b000286 | caption | pages [16] -->
Figure 12: Illustration: Cutting off Indicators of SDG 1 from the Indicator Network

<!-- b000287 | caption | pages [16] -->
Figure 13: Illustration: Cutting off SDG 1 from the SDG Network

<!-- b000288 | furniture | pages [17] -->
Team 2303967

<!-- b000289 | furniture | pages [17] -->
Page 16 of 24

<!-- b000290 | heading | pages [17] -->
5.1.1 Dynamic Resulting Network and Priority

<!-- b000291 | prose | pages [17] -->
According to Assumption 1, if a SDG Gi is achieved, all of Ii(j) data for several years stays zero. Consequently, the correlation coefficients between Ii(j) and Ii′(j′) (indicators from other SDG) vanish. In the resulting Indicator Network, all edge weight coming out from Ii(j) collapse to zero. This is illustrated in Figure 12.

<!-- b000292 | prose | pages [17] -->
Because the edge weight in Goal Network is calculated by those in Indicator Network, the corre- sponding edge weight in resulting SDG Network will vanish as well. This process is like dragging SDG 1 out of the SDG Network, which is illustrated in Figure 13.

<!-- b000293 | prose | pages [17] -->
Our dynamic SDG network will automatically transform based on Algorithm 1.

<!-- b000294 | heading | pages [17] -->
Algorithm 1: Dynamic Resulting Network and Priority with Goal Accomplishment

<!-- b000295 | prose | pages [17] -->
Input: GNet, INet, achieved goal Gachieve Output: Resulting SDG Network ^ GNet and priority ranking for all indicator node I connected to Iachieve(j) do Wind(I →Iachieve(j)) ←0;

<!-- b000296 | prose | pages [17] -->
end for all goal node Gi ∈GNet except Gachieve do Wgoal(Gi →Gachieve) and W(Gachieve →Gi) ←0;

<!-- b000297 | prose | pages [17] -->
Calculate all other Wgoal by Equation (7) to (11);

<!-- b000298 | prose | pages [17] -->
end for all goal node Gi ∈GNet except Gachieve do Calculate priority score PS(Gi) by Equation (12) to (21);

<!-- b000299 | prose | pages [17] -->
end Return ranking result based on PS(Gi);

<!-- b000300 | heading | pages [17] -->
5.1.2 Case Analysis

<!-- b000301 | prose | pages [17] -->
If SDG 1 (No Poverty is achieved), the resulting network is shown in Figure 14 and the top five priorities after this achievement are listed in Table 7.

<!-- b000302 | caption | pages [17] -->
Table 7: Priority Result by Descending Order after Eliminating Porverty

<!-- b000303 | prose | pages [17] -->
Priority Rank SDG Priority Score

<!-- b000304 | prose | pages [17] -->
1 SDG17: Partnerships to achieve the Goal 6.3825 2 SDG6: Clean Water and Sanitation 6.2041 3 SDG4: Quality Education 5.9201 4 SDG3: Good Health and Well-being 5.5672 5 SDG10: Reduced Inequality 5.5629

<!-- b000305 | furniture | pages [18] -->
Team 2303967

<!-- b000306 | furniture | pages [18] -->
Page 17 of 24

<!-- b000307 | caption | pages [18] -->
Figure 14: Resulting Network after SDG 1 Achievement

<!-- b000308 | heading | pages [18] -->
5.2 Addition of the Node: Goal Inclusion

<!-- b000309 | prose | pages [18] -->
In today’s digital age, Access to Information and Communication Technologies (ICTs) should also be proposed to UN for the inclusion [9]. Though its slightly mentioned in SDG 9, it is playing an more and more critical role. It varies from groups to groups, such as developed and developing countries, rural and urban areas, and different socioeconomic classes. The lack of access to ICTs can limit individuals and communities’ opportunities for education, health, and economic growth, and block the SDGs development.

<!-- b000310 | prose | pages [18] -->
To illustrate how a new SDG impacts the Dynamic SDG Network, the method is similar to that in Section 3. The selected indicators are

<!-- b000311 | prose | pages [18] -->
1. proportion of the population that uses the Internet

<!-- b000312 | prose | pages [18] -->
2. mobile broadband subscriptions per 100 inhabitants

<!-- b000313 | prose | pages [18] -->
3. proportion of individuals using the Internet who have basic digital skills

<!-- b000314 | prose | pages [18] -->
After adding the SDG18: Access to Information and Communication Technologies (ICTs), the result SDG network is visualized as Figure 15.

<!-- b000315 | prose | pages [18, 19] -->
Promoting access to ICTs in developing countries is critical for achieving many of the existing SDGs, including quality education, gender equality, decent work and economic growth, industry, innovation and infrastructure, and reduced inequalities. For instance, providing access to educational resources can improve quality education, while promoting digital skills can enhance employment opportunities and contribute to economic growth. Access to information and communication can also help to reduce inequalities by providing equal opportunities for underrepresented groups, such as women, minorities, and marginalized communities. Additionally, ICTs can facilitate access to healthcare services, promote environmental sustainability, and support peacebuilding efforts. Therefore, including Access to Informa- tion and Communication Technologies as a new SDG is significant to enhance the connection between SDGs, advancing their accomplishment.

<!-- b000316 | furniture | pages [19] -->
Team 2303967

<!-- b000317 | furniture | pages [19] -->
Page 18 of 24

<!-- b000318 | caption | pages [19] -->
Figure 15: The SDG Network with a New SDG

<!-- b000320 | heading | pages [19] -->
Algorithm 2: Dynamic Resulting Network and Priority with Goal Inclusion

<!-- b000321 | prose | pages [19] -->
Input: GNet, INet, goal Gadd and its indicators {Iadd(1), · · · } to be added, Y year data for those indicators Output: Resulting SDG Network ^ GNet and priority ranking

<!-- b000322 | prose | pages [19] -->
for all indicator node I ∈INet do Calculate Wind(I →IADD(j)) by Equation 5 to 6;

<!-- b000323 | prose | pages [19] -->
end for all goal node Gi ∈GNet do Calculate all Wgoal by Equation 7 to 11;

<!-- b000324 | prose | pages [19] -->
end for all goal node Gi ∈GNet do Calculate priority score PS(Gi) by Equation 12 to 21;

<!-- b000325 | prose | pages [19] -->
end Return ranking result based on PS(Gi);

<!-- b000326 | heading | pages [19] -->
6 Dynamic SDG Network with by Global Crises

<!-- b000327 | heading | pages [19] -->
6.1 The Impact of International Crises on Dynamic SDG Network

<!-- b000328 | prose | pages [19] -->
The progress towards the SDGs can be significantly impacted by various international crises, including technological advances, global pandemics, climate change, regional wars, and refugee movements.

<!-- b000329 | furniture | pages [20] -->
Team 2303967

<!-- b000330 | furniture | pages [20] -->
Page 19 of 24

<!-- b000331 | prose | pages [20] -->
For example, forest fires can have a significant impact on the SDG network. They can result in environmental degradation, economic instability, and social unrest, which can hinder progress towards achieving the SDGs. The effects of forest fires can be linked to several SDGs, such as SDG 13 (Climate Action), SDG 15 (Life on Land), and SDG 11 (Sustainable Cities and Communities).

<!-- b000332 | caption | pages [20] -->
Figure 16: The flow chart of the impact of forest fires on SDG Network

<!-- b000333 | prose | pages [20] -->
The 2019-2020 Australian bushfires, which burned over 18 million hectares of land, destroyed over 5,900 buildings, and caused numerous fatalities, can have a ripple effect on the network of SDGs. The steps of the impact of forest fires on SDG Network are shown in Figure 16. The contribution of fire to climate change by releasing large amounts of carbon dioxide into the atmosphere can exacerbate the effects of SDG 13 (Climate Action). A preliminary estimation of net emissions for the 2020 fire season has been made by the National Greenhouse Accounts, which is approximately 830 million tonnes of carbon dioxide equivalent [12]. The impact of fires on environmental degradation and loss of biodiversity can affect SDG 15 (Life on Land). Additionally, the destruction of homes, infrastructure, and livelihoods call for progress towards achieving SDG 11 (Sustainable Cities and Communities).

<!-- b000334 | prose | pages [20] -->
The SDG Network’s response to the Australian bushfires is demonstrated by Figure 17.

<!-- b000335 | prose | pages [20] -->
Other global crises impact the SDG network in the following ways.

<!-- b000336 | prose | pages [20] -->
• Technological advance: Enhance correlation between SDG 12 (Responsible Consumption and Production) and SDG 11 (Sustainable Cities and Communities), since rational utility of technology stimulates health growth of human settlement.

<!-- b000337 | prose | pages [20] -->
• Global pandemics: Enhance correlation between SDG 3 (Good Health and Well-being) and SDG 8 (Decent Work and Economic Growth), SDG 12 (Responsible Consumption and Production).

<!-- b000338 | prose | pages [20] -->
Large-scale infection drastically depress the social productivity. Therefore, substantial medical system play crucial role in guarding economy growth.

<!-- b000339 | prose | pages [20, 21] -->
• Regional war: Enhance correlation between SDG 16 (Peace and Justice Strong Institute) and SDG 1 (No Poverty), SDG 3 (Good Health and Well-being), etc. That’s because people’s livelihood depend more on their government and international relationship.

<!-- b000340 | furniture | pages [21] -->
Team 2303967

<!-- b000341 | furniture | pages [21] -->
Page 20 of 24

<!-- b000343 | caption | pages [21] -->
Figure 17: The SDG Network Affected by Forest Fires

<!-- b000344 | prose | pages [21] -->
• Refugee movement: Enhance correlation between SDG 16 (Peace and Justice Strong Institute) and SDG 10 (Reduced Inequality), SDG 11 (Sustainable Cities and Communities), etc. From refugees’ perspective, identity as “refugee” impede their equal opportunity of development. From receiver countries’ point of view, social stability may be affected and they need balance between humanistic protection and social stability.

<!-- b000345 | heading | pages [21] -->
6.2 Effect on the Progress of UN

<!-- b000346 | prose | pages [21] -->
From the network perspective, after forest fire, several SDGs are prioritized according to Figure 17. The rebuilding process presents an opportunity for the country to prioritize and implement SDG-aligned initiatives that foster resilience and sustainable development. These initiatives can include supporting clean energy, enhancing biodiversity and ecosystem restoration, and investing in sustainable infrastructure, which can bring the world closer to achieving all the SDGs [10].

<!-- b000347 | prose | pages [21] -->
Extending case study to a wider range of global crises, global crises can disrupt the global economy, social stability, and environmental sustainability, which can in turn affect progress towards achieving the SDGs. Moreover, crises can bring attention to previously overlooked or under-prioritized issues, highlighting the need for action and leading to the better priority of goals or targets within the UN’s framework.

<!-- b000348 | prose | pages [21] -->
Overall, global crises can have a significant impact on the network of SDGs and their priorities, which in turn can affect the UN’s ability to achieve its goals. It is important for UN to be aware of these potential effects and to adapt its approach to prioritize the most pressing challenges as they arise.

<!-- b000349 | furniture | pages [22] -->
Team 2303967

<!-- b000350 | furniture | pages [22] -->
Page 21 of 24

<!-- b000351 | heading | pages [22] -->
7 Generalized Priority Network: DIGNP

<!-- b000352 | prose | pages [22] -->
Our Dynamic SDG Network and prioritization evaluation have high generalizability. We formulate the general step of its establishment as Dynamic Indicator-Goal Network for Prioritization (DIGNP). With enough data, any other company or organization can figure out their Indicator and Goal Network, as well as goal priority with the assistance of DIGNP model. The general steps of DIGNP establishment are

<!-- b000353 | prose | pages [22] -->
1. Preparation: collect data set of all indicators of each goal, as well as the optimal value of indicators

<!-- b000354 | heading | pages [22] -->
2. Data Pre-processing: normalize data with optimal value

<!-- b000355 | heading | pages [22] -->
3. Establish Indicator Network: figure out edge weight by Equation (5) to (6)

<!-- b000356 | prose | pages [22] -->
4. Map Indicator Network to Goal Network: figure out edge weight by Equation (7) to (11)

<!-- b000357 | prose | pages [22] -->
5. Generate Priorities: calculate priority score by Equation (12) to (21), then sort goals in priority order. If prediction after prioritization is needed for reference, carry it out by Equation (22) to (23)

<!-- b000358 | prose | pages [22] -->
6. Update: Add new data to the database and go back to step 2, repeat for each update

<!-- b000359 | prose | pages [22] -->
Furthermore, we design the User Interface of DIGNP in Figure 18, with which customers can grasp the network and priority information concretely.

<!-- b000360 | caption | pages [22] -->
Figure 18: User Interface of DIGNP

<!-- b000361 | furniture | pages [23] -->
Team 2303967

<!-- b000362 | furniture | pages [23] -->
Page 22 of 24

<!-- b000363 | heading | pages [23] -->
8 Sensitivity Analysis

<!-- b000364 | prose | pages [23] -->
In the prediction model of the SDGs progress, we use the time series model ARIMA. The ARIMA model has three hyper-parameters

<!-- b000365 | prose | pages [23] -->
• p: number of autoregressive terms, namely number of past values used to predict

<!-- b000366 | prose | pages [23] -->
• d: number of differencing required to make the time series stationary

<!-- b000367 | prose | pages [23] -->
• q: the number of moving average terms, namely number of past errors used to predict

<!-- b000368 | prose | pages [23] -->
We use the data from 2000-2015 to predict the data from 2016-2020 and judge its accuracy. By conducting the sensitivity test, we notice slight error with p variation. This show that a suitable choice of hyper-parameter is crucial to our prediction.

<!-- b000369 | caption | pages [23] -->
Figure 19: Sensitivity Analysis of p

<!-- b000370 | caption | pages [23] -->
Figure 19 shows the accuracy of the estimation when p varies, we can see that when p = 4, the general

<!-- b000371 | prose | pages [23] -->
result is relatively close to the real value. Similarly, we obtain d = 1 and q = 2.

<!-- b000372 | heading | pages [23] -->
9 Strength and Weakness

<!-- b000373 | heading | pages [23] -->
Strength

<!-- b000374 | prose | pages [23] -->
• Globality: In our DIGNP, all indicators and goals are connected to each other. With the idea of “Human Community with a Shared Future”, variation of one factor echoes response from others, improving an aspect in our life makes a difference to our mutual development.

<!-- b000375 | prose | pages [23] -->
• Dynamics: The strength of a dynamic network model lies in its ability to capture complex interactions between various variables, as well as changes in those interactions over time.

<!-- b000376 | prose | pages [23] -->
• Automation: With a solid algorithm, our DIGNP will auto-adjust the network topology and priority result in response to internal and external variation. All math works are done behind the UI, with which customers can enjoy smart and in-time network & priority management.

<!-- b000377 | furniture | pages [24] -->
Team 2303967

<!-- b000378 | furniture | pages [24] -->
Page 23 of 24

<!-- b000379 | heading | pages [24] -->
Weakness

<!-- b000380 | prose | pages [24] -->
• Data Dependency: To build up a DIGNP, one needs data from bunches of indicators over a long period. High accuracy priority and prediction even require more data.

<!-- b000381 | prose | pages [24] -->
• Indicator & Goal Input Dependency: UN has proposed SDG after rational consideration, which guarantees the overall viability of our SDG network. However, we cannot guarantee that all users of DIGNP have a full understanding of their goals and indicators. Input lacking in comprehensiveness causes deviation in network & priority output.

<!-- b000382 | heading | pages [24] -->
10 References

<!-- b000383 | references | pages [24] -->
[1] United Nations Statistics Division. (2021). Global indicator framework for the Sustainable De-

<!-- b000384 | references | pages [24] -->
velopment Goals and targets of the 2030 Agenda for Sustainable Development. Retrieved from

<!-- b000385 | references | pages [24] -->
https://unstats.un.org/sdgs/indicators/indicators-list/

<!-- b000386 | references | pages [24] -->
[2] Ghaffarianhoseini, A., Berardi, U., & Ghaffarianhoseini, A. (2019). System Dynamics Modeling for

<!-- b000387 | references | pages [24] -->
Sustainable Energy and Environmental Management: A Critical Review. IEEE Access, 7, 21995-

<!-- b000388 | references | pages [24] -->
22007. doi: 10.1109/ACCESS.2019.2897064

<!-- b000389 | references | pages [24] -->
[3] Wang, Xue-Qi, Zhang, Jie, & Liu, Jing-Bo. (2017). Node importance evaluation method of directed

<!-- b000390 | references | pages [24] -->
weighted network based on multiple influence matrices. Acta Physica Sinica, 66(5), 050201. doi:

<!-- b000391 | references | pages [24] -->
10.7498/aps.66.050201

<!-- b000392 | references | pages [24] -->
[4] Ruhnau, B. (2000). Eigenvector-centrality — a node-centrality? Social Networks, 22(4), 357-365.

<!-- b000393 | references | pages [24] -->
[5] Freeman, L., Borgatti, S., & White, D. (1991). Centrality in valued graphs: A measure of between-

<!-- b000394 | references | pages [24] -->
ness based on network flow. Social Networks, 13(2), 141-154.

<!-- b000395 | references | pages [24] -->
[6] Sachs, J. (2015). Goal-based development and the SDGs: Implications for development finance.

<!-- b000396 | references | pages [24] -->
Oxford Review of Economic Policy, 31(3/4), 268-278.

<!-- b000397 | references | pages [24] -->
[7] Rassanjani, S. (2018). Ending Poverty: Factors That Might Influence the Achievement of Sustainable

<!-- b000398 | references | pages [24] -->
Development Goals (SDGs) in Indonesia. Journal of Public Administration and Governance, 8(3),

<!-- b000399 | references | pages [24] -->
114.

<!-- b000400 | references | pages [24] -->
[8] SDGs in Order. (n.d.). Copenhagen Consensus Center. Retrieved February 17, 2023, from

<!-- b000401 | references | pages [24] -->
https://www.sdgsinorder.org/

<!-- b000402 | references | pages [24] -->
[9] Haenssgen, Marco J. (2018). The struggle for digital inclusion: Phones, healthcare, and marginali-

<!-- b000403 | references | pages [24] -->
sation in rural India. World Development, 104, 358-374. doi: 10.1016/j.worlddev.2017.12.022

<!-- b000404 | references | pages [24] -->
[10] Abram, N., Henley, B., Gupta, A., Lippmann, T., Clarke, H., Dowdy, A., . . . Boer, M. (2021).

<!-- b000405 | references | pages [24] -->
Connections of climate change and variability to large and extreme forest fires in southeast Australia.

<!-- b000406 | references | pages [24] -->
Communications Earth & Environment, 2(1), 1-17.

<!-- b000407 | furniture | pages [25] -->
Team 2303967

<!-- b000408 | furniture | pages [25] -->
Page 24 of 24

<!-- b000409 | references | pages [25] -->
[11] Tariq, A., Shu, H., Li, Q., Altan, O., Khan, M.R., Baqa, M.F., & Lu, L. (2019). Quantitative

<!-- b000410 | references | pages [25] -->
Analysis of Forest Fires in Southeastern Australia Using SAR Data. Remote Sensing, 11(19), 2282.

<!-- b000411 | references | pages [25] -->
https://doi.org/10.3390/rs11192282

<!-- b000412 | references | pages [25] -->
[12] Storey, M., & Price, O. (2022). Statistical modelling of air quality impacts from individual forest fires

<!-- b000413 | references | pages [25] -->
in New South Wales, Australia. Natural Hazards and Earth System Sciences, 22(12), 4039-4062.

<!-- b000414 | heading | pages [25] -->
11 Appendix

<!-- b000415 | prose | pages [25] -->
The serial number of indicators below are that of the official-given number[1].

<!-- b000416 | caption | pages [25] -->
Table 8: Selected Indicators for SDGs

<!-- b000417 | prose | pages [25] -->
SDGs Indicators

<!-- b000418 | prose | pages [25] -->
SDG1: No proverty C010101, C010301, C010a02 SDG2: Zero Hunger C020101, C020301, C020b02 SDG3: Good Health and Well-being C030201, C030402, C030b01, C030c01 SDG4: Quality Education C040102, C200306 SDG5: Gender Equity C050201, C050502 SDG6: Clean Water and Sanitation C060101, C060201, C060b01 SDG7: Affordable and Clean Energy C070102, C200208 SDG8: Decent Work and Economic Growth C080501, C080502, C080802 SDG9: Industry, Innovation and Infrastructure C090201, C090501, C090c01 SDG10: Reduced Inequality C100501, C200205 SDG11: Sustainable Cities and Communities C110101, C110401, C110702 SDG12: Responsible Consumption and Production C200202, C120501 SDG13: Climate Action C200305, C130202 SDG14: Life below Water C140101, C140701 SDG15: Life on Land C150101, C200210 SDG16: Peace and Justice Strong Institutions C160102, C200205, C160a01 SDG17: Partnerships to achieve the Goals C170101, C170801, C171101
