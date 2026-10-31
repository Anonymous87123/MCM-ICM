# P-D-2023-2300229-f57e1b5d

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Problem Chosen

<!-- b000002 | prose | pages [1] -->
2023

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
D

<!-- b000006 | title | pages [1] -->
2300229

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | title | pages [1] -->
Methods of Measuring Priority via Graph Models: Who Is the

<!-- b000010 | title | pages [1] -->
Top 1?

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
In 2015, the United Nations set 17 Sustainable Development Goals (SDGs). If these goals are

<!-- b000013 | prose | pages [1] -->
achieved, we could ultimately improve life of people all over the world. The 17 SDGs are not inde-

<!-- b000014 | prose | pages [1] -->
pendent of each other. Their connections make the achievement of all goals much easier. In this paper,

<!-- b000015 | prose | pages [1] -->
we construct three distinctive models to study how to prioritize the SDGs.

<!-- b000016 | prose | pages [1] -->
First, to find out relationships and priorities between the 17 SDGs, we propose Relationship

<!-- b000017 | prose | pages [1] -->
Graph Model. In the model, we build a graph between 17 SDGs. Vertexes of the graph are the 17

<!-- b000018 | prose | pages [1] -->
goals. Edges of the graph are correlations between goals via Spearman Correlation Analysis Algo-

<!-- b000019 | prose | pages [1] -->
rithm. To measure the graph, we use Betweenness Centrality, Closeness Centrality and Eigenvector

<!-- b000020 | prose | pages [1] -->
Centrality. We respectively calculate centralities of positive edges and negative edges. Hence, each

<!-- b000021 | prose | pages [1] -->
goal has 6 indexes. We use Entropy Weight Method to calculate weights of the 6 indexes. Then we

<!-- b000022 | prose | pages [1] -->
use Weighted TOPSIS to get the priorities of the 17 goals. Goal 3 and Goal4 rank in top 5 priority list

<!-- b000023 | prose | pages [1] -->
for all three countries we study. This means most countries should put health and education on the

<!-- b000024 | prose | pages [1] -->
priority list of development.

<!-- b000025 | prose | pages [1] -->
Then, we study the development of the 17 SDGs in next 10 years. We propose Temporal Cham-

<!-- b000026 | prose | pages [1] -->
pagne Tower Model. This model not only considers resource allocation based on priorities, but also

<!-- b000027 | prose | pages [1] -->
the synergistic and trade-off relationships between goals. We use Time Series Algorithm to predict

<!-- b000028 | prose | pages [1] -->
the development of SDGs in next 10 years. We allocate resources according to the method of first

<!-- b000029 | prose | pages [1] -->
satisfying the higher priority goal. When a goal is achieved, we raise its priority to the highest priority

<!-- b000030 | prose | pages [1] -->
queue (complete goal queue) to preferentially maintain the complete goal. We do simulation on Indo-

<!-- b000031 | prose | pages [1] -->
nesia. In the next 10 years, Indonesia can achieve 5 goals. It can achieve 82% of SDGs, which is 4%

<!-- b000032 | prose | pages [1] -->
higher than the result of its current plan.

<!-- b000033 | prose | pages [1] -->
Moreover, to study the impact of unexpected events like COVID-19, we make some adjustment

<!-- b000034 | prose | pages [1] -->
to our models. We add two parameters to measure the impacts. Models which are about the priorities

<!-- b000035 | prose | pages [1] -->
and allocated resources are adjusted based on the two parameters. We rerun our models. According

<!-- b000036 | prose | pages [1] -->
to the simulation, in the next 10 years, Indonesia can only achieve 3 goals. It can achieve 78% of

<!-- b000037 | prose | pages [1] -->
SDGs, which is 4% lower than the previous result.

<!-- b000038 | prose | pages [1] -->
Finally, we perform sensitivity analysis on the hyperparameters and in Temporal Cham-

<!-- b000039 | prose | pages [1] -->
pagne Tower Model. The maximum variation ranges of the model results caused by the changes of

<!-- b000040 | prose | pages [1] -->
and are 0.041 and 0.028, respectively, which indicates that our model has a strong robustness.

<!-- b000041 | keywords | pages [1] -->
Key words: sustainable development goals, graph centrality, topsis, entropy weight method

<!-- b000042 | furniture | pages [1] -->


<!-- b000043 | furniture | pages [2] -->
Team # 2300229                                                       page 2 of 25

<!-- b000044 | heading | pages [2] -->
Contents

<!-- b000045 | furniture | pages [2] -->


<!-- b000046 | contents | pages [2] -->
1 Introduction .............................................................................................................................. 3

<!-- b000047 | contents | pages [2] -->
1.1 Problem Background ..................................................................................................... 3

<!-- b000048 | contents | pages [2] -->
1.2 Literature Review .......................................................................................................... 3

<!-- b000049 | contents | pages [2] -->
1.3 Our Work ....................................................................................................................... 4

<!-- b000050 | contents | pages [2] -->
2 Assumptions and Justifications ................................................................................................ 4

<!-- b000051 | contents | pages [2] -->
3 Notations .................................................................................................................................. 5

<!-- b000052 | contents | pages [2] -->
4 Relationship Graph Model ....................................................................................................... 5

<!-- b000053 | contents | pages [2] -->
4.1 The Data ........................................................................................................................ 5

<!-- b000054 | contents | pages [2] -->
4.2 Graph Construction ....................................................................................................... 6

<!-- b000055 | contents | pages [2] -->
4.3 Graph Measurement based on Graph Theory ................................................................ 8

<!-- b000056 | contents | pages [2] -->
4.4 Results and Analysis ...................................................................................................... 8

<!-- b000057 | contents | pages [2] -->
5 Priority Model ........................................................................................................................ 11

<!-- b000058 | contents | pages [2] -->
5.1 Establishment of the Model ......................................................................................... 11

<!-- b000059 | contents | pages [2] -->
5.2 Results and Analysis .................................................................................................... 13

<!-- b000060 | contents | pages [2] -->
6 Temporal Champagne Tower Model for Future Development .............................................. 14

<!-- b000061 | contents | pages [2] -->
6.1 Mathematical Establishment of the Model .................................................................. 15

<!-- b000062 | contents | pages [2] -->
6.2 Temporal Champagne Tower Model ........................................................................... 16

<!-- b000063 | contents | pages [2] -->
6.3 Model Solutions based on Time Series Algorithms .................................................... 17

<!-- b000064 | contents | pages [2] -->
6.4 One Goal Being Achieved ........................................................................................... 17

<!-- b000065 | contents | pages [2] -->
6.5 Results and Analysis .................................................................................................... 18

<!-- b000066 | contents | pages [2] -->
7 Analysis on the Impacts ......................................................................................................... 19

<!-- b000067 | contents | pages [2] -->
7.1 COVID-19 Impact on Models ..................................................................................... 19

<!-- b000068 | contents | pages [2] -->
7.2 Results and Analysis .................................................................................................... 20

<!-- b000069 | contents | pages [2] -->
7.3 Model Impact on Companies and Organizations ........................................................ 21

<!-- b000070 | contents | pages [2] -->
8 Sensitivity Analysis ................................................................................................................ 22

<!-- b000071 | contents | pages [2] -->
9 Model Evaluation and Further Discussion ............................................................................. 23

<!-- b000072 | contents | pages [2] -->
9.1 Strengths of the Model ................................................................................................ 23

<!-- b000073 | contents | pages [2] -->
9.2 Weaknesses of the Model ............................................................................................ 23

<!-- b000074 | contents | pages [2] -->
References .................................................................................................................................... 24

<!-- b000075 | contents | pages [2] -->
Appendix ...................................................................................................................................... 25

<!-- b000076 | furniture | pages [2] -->


<!-- b000077 | furniture | pages [2] -->


<!-- b000078 | furniture | pages [2] -->


<!-- b000079 | furniture | pages [2] -->


<!-- b000080 | furniture | pages [2] -->


<!-- b000081 | furniture | pages [3] -->
Team # 2300229                                                       page 3 of 25

<!-- b000082 | contents | pages [3] -->
1

<!-- b000083 | heading | pages [3] -->
Introduction

<!-- b000084 | heading | pages [3] -->
1.1 Problem Background

<!-- b000085 | prose | pages [3] -->
In 1987, the Brundtland report proposed the most recognized definition of sustainable develop-

<!-- b000086 | prose | pages [3] -->
ment, which is: “Sustainable development is able to meet the requirements of the current generation

<!-- b000087 | prose | pages [3] -->
and does not have to consume the capability of the future generations”[1]. Ever since then, a number

<!-- b000088 | prose | pages [3] -->
of attempts at this goal have been made[2]. In 2015, the United Nations set 17 Sustainable Develop-

<!-- b000089 | prose | pages [3] -->
ment Goals (SDGs)[3]. If achieved, these goals could ultimately lead to an improved life of people all

<!-- b000090 | prose | pages [3] -->
over the world.

<!-- b000091 | prose | pages [3] -->
The 17 SDGs are not independent of each other. Their connections make the achievement of all

<!-- b000092 | prose | pages [3] -->
goals much easier. Hence, we establish models to study their relationships as well as completing the

<!-- b000093 | prose | pages [3] -->
following problems.

<!-- b000094 | prose | pages [3] -->
⚫ Create a network to reveal relationships between the 17 SDGs. The key to this problem

<!-- b000095 | prose | pages [3] -->
is to measure the relationships in a mathematical way.

<!-- b000096 | prose | pages [3] -->
⚫ Set priorities for the 17 SDGs. The key to this problem is to find a reasonable standard and

<!-- b000097 | prose | pages [3] -->
sort all goals under this standard.

<!-- b000098 | prose | pages [3] -->
⚫ Study the development of SDGs in next 10 years with priorities set. Study the impact

<!-- b000099 | prose | pages [3] -->
from achievement of one goal. The key to this problem is to find a plan which considers the

<!-- b000100 | prose | pages [3] -->
priority and the relationships between goals.

<!-- b000101 | prose | pages [3] -->
⚫ Discuss the impact of unexpected events. The key to this problem is to quantify the impacts

<!-- b000102 | prose | pages [3] -->
and adjust our models based on the impacts.

<!-- b000103 | prose | pages [3] -->
⚫ Discuss the use of models in other fields. The key to this problem is to find relations be-

<!-- b000104 | prose | pages [3] -->
tween SDGs and goals of companies and organizations.

<!-- b000105 | heading | pages [3] -->
1.2 Literature Review

<!-- b000106 | prose | pages [3] -->
Relationships between SDGs have been extensively studied. David Le Blanc proposed the SDG

<!-- b000107 | prose | pages [3] -->
relationship graph based on the relationships between indicators and goals[4]. He concluded that some

<!-- b000108 | prose | pages [3] -->
SDGs are closely related. Ranjula Bali Swain et al. used the correlation between SDG target variables

<!-- b000109 | prose | pages [3] -->
to model the edges in the correlation networks[5]. They used centrality measures and community de-

<!-- b000110 | prose | pages [3] -->
tection to analyze the networks. Their conclusion is that it may be effective to identify a specific com-

<!-- b000111 | prose | pages [3] -->
munity of SDG targets for a specific region. Pradhan P, Costa L, Rybski D, et al. calculated the Spear-

<!-- b000112 | prose | pages [3] -->
man’s correlation between the indicators, and classified correlations as synergy and trade-off. They

<!-- b000113 | prose | pages [3] -->
emphasized the role of synergy in the realization of SDGs[6]. All works mentioned above used corre-

<!-- b000114 | prose | pages [3] -->
lation to measure the relationship between SDGs and achieved good effects.

<!-- b000115 | prose | pages [3] -->
There are also some researches on the impact of international crises on SDGs. Naidoo R, Fisher

<!-- b000116 | furniture | pages [3] -->


<!-- b000117 | furniture | pages [4] -->
Team # 2300229                                                       page 4 of 25

<!-- b000118 | prose | pages [4] -->
B discussed the threat of COVID-19 to SDGs and expressed their expectations on the United Na-

<!-- b000119 | prose | pages [4] -->
tions[7]. Mukarram M described socio-economic impacts of COVID-19, which can be mitigated via

<!-- b000120 | prose | pages [4] -->
his methods[8]. Both works have good assessments of the impact of global pandemics. We discuss

<!-- b000121 | prose | pages [4] -->
further based on their researches.

<!-- b000122 | heading | pages [4] -->
1.3 Our Work

<!-- b000123 | prose | pages [4] -->
Based on the problem analysis, we construct three distinctive models—Relationship Graph Model,

<!-- b000124 | prose | pages [4] -->
Priority Model and Temporal Champagne Model. Then we study the impact from COVID-19 on our

<!-- b000125 | prose | pages [4] -->
models. Finally, we conduct sensitivity to test the robustness of our models. The work we have done

<!-- b000126 | prose | pages [4] -->
is mainly shown in Figure 1.

<!-- b000127 | furniture | pages [4] -->


<!-- b000128 | caption | pages [4] -->
Figure 1 The Framework of Our Work

<!-- b000129 | prose | pages [4] -->
2

<!-- b000130 | heading | pages [4] -->
Assumptions and Justifications

<!-- b000131 | prose | pages [4] -->
Through a complete analysis of the problem, in order to make our model more practical and rea-

<!-- b000132 | prose | pages [4] -->
sonable, we make the following reasonable assumptions.

<!-- b000133 | prose | pages [4] -->
Assumption 1: All data from the datasets are authentic.

<!-- b000134 | prose | pages [4] -->
It is meaningless to study fake datasets. We believe the datasets we get are authentic and accurate.

<!-- b000135 | prose | pages [4] -->
No malicious modification has ever occurred.

<!-- b000136 | prose | pages [4] -->
Assumption 2: The completion difficulties of all 17 SDGs are the same.

<!-- b000137 | prose | pages [4] -->
Since it is hard to measure the completion difficulty of each goal and no specific data describing

<!-- b000138 | prose | pages [4] -->
difficulties are found, we assume completion difficulties of them are all the same.

<!-- b000139 | furniture | pages [4] -->


<!-- b000140 | furniture | pages [5] -->
Team # 2300229                                                       page 5 of 25

<!-- b000141 | prose | pages [5] -->
3

<!-- b000142 | heading | pages [5] -->
Notations

<!-- b000143 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000144 | caption | pages [5] -->
Table 1 Notations Used in This Paper

<!-- b000145 | heading | pages [5] -->
Symbol

<!-- b000146 | prose | pages [5] -->
Definition

<!-- b000147 | prose | pages [5] -->
The undirected relationship graph of 17 SGDs.

<!-- b000148 | prose | pages [5] -->
The betweenness centrality of node

<!-- b000149 | furniture | pages [5] -->


<!-- b000150 | prose | pages [5] -->
.

<!-- b000151 | prose | pages [5] -->
The closeness centrality of node

<!-- b000152 | furniture | pages [5] -->


<!-- b000153 | prose | pages [5] -->
.

<!-- b000154 | prose | pages [5] -->
The eigenvector centrality of node

<!-- b000155 | furniture | pages [5] -->


<!-- b000156 | prose | pages [5] -->
.

<!-- b000157 | prose | pages [5] -->
The score of the ith goal from TOPSIS Model.

<!-- b000158 | furniture | pages [5] -->


<!-- b000159 | prose | pages [5] -->
Change of percentage complete from correlation.

<!-- b000160 | furniture | pages [5] -->


<!-- b000161 | prose | pages [5] -->
Resources allocated to the ith goal.

<!-- b000162 | furniture | pages [5] -->


<!-- b000163 | prose | pages [5] -->
Percentage complete of the ith goal in year

<!-- b000164 | furniture | pages [5] -->


<!-- b000165 | prose | pages [5] -->
.

<!-- b000166 | prose | pages [5] -->
The threat level of the goal

<!-- b000167 | furniture | pages [5] -->


<!-- b000168 | prose | pages [5] -->
.

<!-- b000169 | prose | pages [5] -->
The mitigation or aggravating level of the goal

<!-- b000170 | furniture | pages [5] -->


<!-- b000171 | prose | pages [5] -->
.

<!-- b000172 | prose | pages [5] -->
Note: There are some variables not listed here and will be discussed in detail in each section.

<!-- b000173 | prose | pages [5] -->
4

<!-- b000174 | heading | pages [5] -->
Relationship Graph Model

<!-- b000175 | prose | pages [5] -->
To reveal the relationships between 17 SDGs, we create a graph based on graph theory. After-

<!-- b000176 | prose | pages [5] -->
wards, we want to measure the importance of each node in the graph, which plays an important role in

<!-- b000177 | prose | pages [5] -->
studying priorities of the 17 goals. Hence, we use three types of centrality measures as the parameters

<!-- b000178 | prose | pages [5] -->
of our graph model, which are commonly used to tell the importance of nodes.

<!-- b000179 | heading | pages [5] -->
4.1 The Data

<!-- b000180 | prose | pages [5] -->
Before the establishment of the model, we get data in need at first. Then we do some preprocessing

<!-- b000181 | prose | pages [5] -->
on the data for better analysis.

<!-- b000182 | heading | pages [5] -->
4.1.1 Data Selection

<!-- b000183 | prose | pages [5] -->
We get our data from the United Nations Global SDG Database[9]. This database owns compre-

<!-- b000184 | prose | pages [5] -->
hensive datasets tracking 17 SDGs. The 17 SDGs each has several targets. Each target also has several

<!-- b000185 | prose | pages [5] -->
indicators. Each indicator consists of many series.

<!-- b000186 | prose | pages [5] -->
In order to make our model more reliable and robust, we make a balance between maximizing

<!-- b000187 | prose | pages [5] -->
the years of samples and the numbers of series. We also have to make sure all the SDGs are covered.

<!-- b000188 | prose | pages [5] -->
Finally, we select 95 series in total. We choose data from Turkey, Mexico and Indonesia, which repre-

<!-- b000189 | prose | pages [5] -->
sent three different continents. Years of the data are from 2003 to 2018.

<!-- b000190 | furniture | pages [5] -->


<!-- b000191 | furniture | pages [6] -->
Team # 2300229                                                       page 6 of 25

<!-- b000192 | heading | pages [6] -->
4.1.2 Data Processing

<!-- b000193 | prose | pages [6] -->
Data Cleaning: Some values are missing from the dataset. We use linear regression to supple-

<!-- b000194 | prose | pages [6] -->
ment the missing values. This method can make use of the information in the original data set as much

<!-- b000195 | prose | pages [6] -->
as possible. Its calculation method is

<!-- b000196 | furniture | pages [6] -->


<!-- b000197 | furniture | pages [6] -->


<!-- b000198 | prose | pages [6] -->
(1)

<!-- b000199 | prose | pages [6] -->
is the supplementary value of the missing item, where is the year of the missing item, and

<!-- b000200 | prose | pages [6] -->
are two parameters. For some values that cannot be negative, we use 0 to supplement the missing

<!-- b000201 | prose | pages [6] -->
. item when

<!-- b000202 | prose | pages [6] -->
Data Normalization: We do normalization to make the data be limited within , so as to

<!-- b000203 | prose | pages [6] -->
reduce the adverse effects caused by the singular sample data. For indicators which are the larger the

<!-- b000204 | prose | pages [6] -->
better, we do normalization in this way:

<!-- b000205 | furniture | pages [6] -->


<!-- b000206 | prose | pages [6] -->
where is the matrix of series of country

<!-- b000207 | prose | pages [6] -->
malization.

<!-- b000208 | furniture | pages [6] -->


<!-- b000209 | prose | pages [6] -->
(2)

<!-- b000210 | prose | pages [6] -->
in period and is the value after nor-

<!-- b000211 | prose | pages [6] -->
For indicators which are the smaller the better, we do normalization in this way:

<!-- b000212 | furniture | pages [6] -->


<!-- b000213 | furniture | pages [6] -->


<!-- b000214 | prose | pages [6] -->
(3)

<!-- b000215 | prose | pages [6] -->
After normalization, we make all indicators the larger the better and restricted to . This

<!-- b000216 | prose | pages [6] -->
makes it more reasonable when calculating correlation of the data.

<!-- b000217 | heading | pages [6] -->
4.2 Graph Construction

<!-- b000218 | prose | pages [6] -->
to denote the undirected relationship graph of 17 goals, where We use is the set

<!-- b000219 | prose | pages [6] -->
is the ith node, which repre- is the weight matrix . of all nodes, is the set of all edges and

<!-- b000220 | prose | pages [6] -->
sents the ith goal.

<!-- b000221 | prose | pages [6] -->
is the undirected edge between node

<!-- b000222 | prose | pages [6] -->
nection between two goals.

<!-- b000223 | prose | pages [6] -->
is the weight of

<!-- b000224 | prose | pages [6] -->
and node , which represents the con-

<!-- b000225 | prose | pages [6] -->
. Based on the structure of the data and the re-

<!-- b000226 | prose | pages [6] -->
quirement of problem 1, we make “goals” directly concerned with “series”. Then we use to de-

<!-- b000227 | prose | pages [6] -->
to denote the vector of the kth series of the ith goal. It note the kth series of the ith goal. We use

<!-- b000228 | prose | pages [6] -->
can be described as consists data from 2003 to 2018. Vector

<!-- b000229 | furniture | pages [6] -->


<!-- b000230 | furniture | pages [7] -->
Team # 2300229                                                       page 7 of 25

<!-- b000231 | furniture | pages [7] -->


<!-- b000232 | furniture | pages [7] -->


<!-- b000233 | prose | pages [7] -->
(4)

<!-- b000234 | prose | pages [7] -->
are the statistic values of the kth series of the ith goal from year 2003 to year where

<!-- b000235 | prose | pages [7] -->
2018. They are from the datasets we find.

<!-- b000236 | prose | pages [7] -->
We use Spearman’s analysis to construct edges of the graph. This is because compared to Pear-

<!-- b000237 | prose | pages [7] -->
son’s correlation analysis, Spearman’s analysis is better at capturing non-linear correlation and is less

<!-- b000238 | prose | pages [7] -->
to denote the Spearman correlation coefficient between the kth sensible to outliers[10]. We use

<!-- b000239 | prose | pages [7] -->
series of the ith goal and the pth series of the jth goal. Before calculation, we need to convert and

<!-- b000240 | prose | pages [7] -->
(The grade of a number is the position of the number after sorting into grade vector and

<!-- b000241 | prose | pages [7] -->
its vector from small to large). Then we calculate the correlation coefficient. The calculation method

<!-- b000242 | prose | pages [7] -->
of is

<!-- b000243 | furniture | pages [7] -->


<!-- b000244 | prose | pages [7] -->
and are the mean values of all where

<!-- b000245 | furniture | pages [7] -->


<!-- b000246 | prose | pages [7] -->
(5)

<!-- b000247 | prose | pages [7] -->
and , respectively.

<!-- b000248 | prose | pages [7] -->
Connections between series can mainly be divided into three types, which are positive correlation,

<!-- b000249 | prose | pages [7] -->
negative correlation and none correlation. All connections between series of the ith goal and series of

<!-- b000250 | prose | pages [7] -->
the jth goal may not belong to the same type. Hence, we respectively take the three types of connection

<!-- b000251 | prose | pages [7] -->
to measure the connection between the ith goal and the jth goal. into consideration. We use vector

<!-- b000252 | prose | pages [7] -->
measures positive correlation. The second dimension of the vector The first dimension of vector

<!-- b000253 | prose | pages [7] -->
measures negative correlation and the third dimension of the vector measures none correlation. The

<!-- b000254 | prose | pages [7] -->
is calculation method of

<!-- b000255 | furniture | pages [7] -->


<!-- b000256 | furniture | pages [7] -->


<!-- b000257 | prose | pages [7] -->
(6)

<!-- b000258 | prose | pages [7] -->
is the total number of connections between series of the ith goal and series of the jth goal. where

<!-- b000259 | prose | pages [7] -->
, the edge between node i and node j will be removed. Because the correlation is not reli- If

<!-- b000260 | prose | pages [7] -->
able[6].

<!-- b000261 | prose | pages [7] -->
is calculated by Finally, the weight of edge

<!-- b000262 | furniture | pages [7] -->


<!-- b000263 | furniture | pages [7] -->


<!-- b000264 | furniture | pages [7] -->


<!-- b000265 | prose | pages [7] -->
(7)

<!-- b000266 | furniture | pages [8] -->
Team # 2300229                                                       page 8 of 25

<!-- b000267 | prose | pages [8] -->
, then the ith goal has a positive correlation with the jth goal. If If

<!-- b000268 | prose | pages [8] -->
a negative correlation with the jth goal. The bigger

<!-- b000269 | prose | pages [8] -->
, then the ith goal has

<!-- b000270 | prose | pages [8] -->
, the stronger the correlation is.

<!-- b000271 | heading | pages [8] -->
4.3 Graph Measurement based on Graph Theory

<!-- b000272 | prose | pages [8] -->
There are mainly three methods to measure the influence of nodes. Hence parameters of our model

<!-- b000273 | prose | pages [8] -->
come from these three methods, which are Betweenness Centrality, Closeness Centrality and Eigen-

<!-- b000274 | prose | pages [8] -->
vector Centrality. Here we respectively take positive edges and negative edges into consideration.

<!-- b000275 | prose | pages [8] -->
⚫ Betweenness Centrality

<!-- b000276 | prose | pages [8] -->
Betweenness centrality measures how often a node lies on the path of other nodes[11]. We use

<!-- b000277 | prose | pages [8] -->
to denote the betweenness centrality of the ith node. Its calculation method is

<!-- b000278 | furniture | pages [8] -->


<!-- b000279 | furniture | pages [8] -->


<!-- b000280 | prose | pages [8] -->
(8)

<!-- b000281 | prose | pages [8] -->
is the number of shortest paths from node where

<!-- b000282 | prose | pages [8] -->
. of such paths that pass through node

<!-- b000283 | prose | pages [8] -->
⚫ Closeness Centrality

<!-- b000284 | prose | pages [8] -->
to node and is the number

<!-- b000285 | prose | pages [8] -->
A node is close to others if the sum of minimal distances from others is small[12]. Closeness

<!-- b000286 | prose | pages [8] -->
centrality is a path-based method of centrality[5]. We use

<!-- b000287 | prose | pages [8] -->
the ith node. Its calculation method is

<!-- b000288 | furniture | pages [8] -->


<!-- b000289 | prose | pages [8] -->
to denote the closeness centrality of

<!-- b000290 | furniture | pages [8] -->


<!-- b000291 | prose | pages [8] -->
(9)

<!-- b000292 | prose | pages [8] -->
is the minimal distance between node where

<!-- b000293 | prose | pages [8] -->
⚫ Eigenvector Centrality

<!-- b000294 | prose | pages [8] -->
and node .

<!-- b000295 | prose | pages [8] -->
Eigenvector centrality is a common algorithm to measure the importance of a node[13]. It con-

<!-- b000296 | prose | pages [8] -->
to denote the siders the number of neighbors and the importance of the neighbors. We use

<!-- b000297 | prose | pages [8] -->
eigenvector centrality of the ith node. Its calculation method is

<!-- b000298 | furniture | pages [8] -->


<!-- b000299 | furniture | pages [8] -->


<!-- b000300 | prose | pages [8] -->
(10)

<!-- b000301 | prose | pages [8] -->
is the largest eigenvalue of the adjacency matrix where

<!-- b000302 | heading | pages [8] -->
4.4 Results and Analysis

<!-- b000303 | prose | pages [8] -->
.

<!-- b000304 | heading | pages [8] -->
4.4.1 Results and Analysis from the Graph

<!-- b000305 | caption | pages [8] -->
Figure 2 are relationship graphs between 17 goals of three countries. In Figure 2, the red line

<!-- b000306 | prose | pages [8] -->
represents positive correlation, while the blue line represents negative correlation. The thicker the line

<!-- b000307 | furniture | pages [8] -->


<!-- b000308 | furniture | pages [9] -->
Team # 2300229                                                       page 9 of 25

<!-- b000309 | prose | pages [9] -->
is, the stronger is the correlation. According to Figure 2, we have some discoveries:

<!-- b000310 | prose | pages [9] -->
⚫ In general, the majority of the 17 goals have positive correlations with each other. Posi-

<!-- b000311 | prose | pages [9] -->
tive correlations represent synergistic relationship, while negative correlation represent

<!-- b000312 | prose | pages [9] -->
tradeoff relationship. According to the United Nation, the seventeen goals own the same pur-

<!-- b000313 | prose | pages [9] -->
pose, which is to end poverty, protect the planet and ensure prosperity for all. In this way, the

<!-- b000314 | prose | pages [9] -->
17 goals should have synergistic relationship with each other.

<!-- b000315 | prose | pages [9] -->
⚫ Some negative correlation does exist, which means the two goals are trade-offs. This is

<!-- b000316 | prose | pages [9] -->
mainly because these two goals are competing resources.

<!-- b000317 | furniture | pages [9] -->


<!-- b000318 | furniture | pages [9] -->


<!-- b000319 | furniture | pages [9] -->


<!-- b000320 | prose | pages [9] -->
a) Turkey

<!-- b000321 | prose | pages [9] -->
b) Indonesia

<!-- b000322 | prose | pages [9] -->
c) Mexico

<!-- b000323 | caption | pages [9] -->
Figure 2 Graph of the Relationships between 17 Goals

<!-- b000324 | caption | pages [9] -->
Figure 3 shows the synergies and trade-offs within and between 17 SDGs in Indonesia. The left

<!-- b000325 | prose | pages [9] -->
part shows the synergies and trade-offs within goals. The middle part shows the synergies and trade-

<!-- b000326 | prose | pages [9] -->
offs between goals. The right part shows the color bars and legends of the figure. The lower triangle

<!-- b000327 | prose | pages [9] -->
part of the figure are several pie charts. These pie charts describe the percentage of positive correlations,

<!-- b000328 | prose | pages [9] -->
negative correlations and non-correlations between two goals. This is because each goal has many

<!-- b000329 | prose | pages [9] -->
series. All connections between series of goals may not belong to the same type. The upper triangle

<!-- b000330 | prose | pages [9] -->
part of the figure are weights between two goals. According to Figure 3, we have some discoveries:

<!-- b000331 | prose | pages [9] -->
⚫ Within each goal, positive correlations outweigh negative correlations. The series of each

<!-- b000332 | prose | pages [9] -->
goal are synergies. This means targets set for each goal are reasonable.

<!-- b000333 | prose | pages [9] -->
⚫ Goal 7 has negative correlations with all other goals. Goal 7 is “affordable and clean en-

<!-- b000334 | prose | pages [9] -->
ergy”. The cost of clean energy is much higher than fossil energy. And it needs a lot of in-

<!-- b000335 | prose | pages [9] -->
vestment for technological improvement. It also occupies a lot of human and material re-

<!-- b000336 | prose | pages [9] -->
sources. It makes sense that goal 7 and other goals are trade-offs.

<!-- b000337 | prose | pages [9] -->
Advice for the United Nation. We suggest that the UN should lower the standard of goal 7 for

<!-- b000338 | furniture | pages [9] -->


<!-- b000339 | furniture | pages [10] -->
Team # 2300229                                                       page 10 of 25

<!-- b000340 | prose | pages [10] -->
countries like Indonesia, whose synthetic national power is not strong. We also recommend these coun-

<!-- b000341 | prose | pages [10] -->
tries to put goal 7 in low priority. Moreover, it is a good idea to have some developed countries help

<!-- b000342 | prose | pages [10] -->
these countries develop the technologies of affordable and clean energy.

<!-- b000343 | furniture | pages [10] -->


<!-- b000344 | caption | pages [10] -->
Figure 3 Synergies and Trade-offs within and between Goals

<!-- b000345 | heading | pages [10] -->
4.4.2 Results and Analysis from Graph Parameters

<!-- b000346 | prose | pages [10] -->
Since we respectively take positive edges and negative edges into consideration, we have two

<!-- b000347 | prose | pages [10] -->
, , kinds of centralities. We use to denote betweenness centrality, closeness cen-

<!-- b000348 | prose | pages [10] -->
trality and eigenvector centrality of positive edges, respectively. We use , , to de-

<!-- b000349 | prose | pages [10] -->
note betweenness centrality, closeness centrality and eigenvector centrality of negative edges, respec-

<!-- b000350 | prose | pages [10] -->
tively. Parameters for graph of Mexico is shown in Table 2. Parameters for graph of Indonesia and

<!-- b000351 | prose | pages [10] -->
Turkey are shown in Appendix. According to the table, we find that Goal 3 has the highest value of

<!-- b000352 | prose | pages [10] -->
. We preliminarily estimate Goal 3 has the highest priority. Further study on , and

<!-- b000353 | prose | pages [10] -->
priorities will be conducted in section 5.

<!-- b000354 | caption | pages [10] -->
Table 2 Parameters for Graph of Mexico

<!-- b000355 | prose | pages [10] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8

<!-- b000356 | furniture | pages [10] -->


<!-- b000357 | prose | pages [10] -->
0.004

<!-- b000358 | furniture | pages [10] -->


<!-- b000359 | prose | pages [10] -->
0.000 0.004 0.162 0.000 0.004 0.000 0.004

<!-- b000360 | prose | pages [10] -->
0.556

<!-- b000361 | furniture | pages [10] -->


<!-- b000362 | prose | pages [10] -->
0.444 0.556 0.606 0.333 0.556 0.000 0.556

<!-- b000363 | prose | pages [10] -->
0.036

<!-- b000364 | furniture | pages [10] -->


<!-- b000365 | prose | pages [10] -->
0.340 0.313 0.340

<!-- b000366 | furniture | pages [10] -->


<!-- b000367 | prose | pages [10] -->
0.340 0.000 0.340 0.000

<!-- b000368 | prose | pages [10] -->
0.000 0.022 0.196 0.252

<!-- b000369 | furniture | pages [10] -->


<!-- b000370 | prose | pages [10] -->
0.000 0.000 0.046 0.000

<!-- b000371 | prose | pages [10] -->
0.464 0.520 0.722 0.619

<!-- b000372 | furniture | pages [10] -->


<!-- b000373 | prose | pages [10] -->
0.394 0.481 0.481 0.481

<!-- b000374 | prose | pages [10] -->
0.108 0.257 0.472 0.294

<!-- b000375 | furniture | pages [10] -->


<!-- b000376 | prose | pages [10] -->
0.062 0.209 0.226 0.209

<!-- b000377 | furniture | pages [11] -->
Team # 2300229                                                       page 11 of 25

<!-- b000378 | caption | pages [11] -->
Table 2 Parameters for Graph of Mexico(continued)

<!-- b000379 | prose | pages [11] -->
Goal 9 Goal 10 Goal 11 Goal 12 Goal 13 Goal 14 Goal 15 Goal 16 Goal 17

<!-- b000380 | prose | pages [11] -->
0.004 0.029 0.004 0.000 0.000 0.000 0.004 0.000 0.000

<!-- b000381 | prose | pages [11] -->
0.556 0.200 0.556 0.000 0.120

<!-- b000382 | prose | pages [11] -->
0.340 0.000 0.000

<!-- b000383 | prose | pages [11] -->
0.333 0.556 0.120 0.120

<!-- b000384 | prose | pages [11] -->
0.036 0.340

<!-- b000385 | prose | pages [11] -->
0.000

<!-- b000386 | prose | pages [11] -->
0.340 0.000 0.000 0.340

<!-- b000387 | prose | pages [11] -->
0.022 0.054 0.491 0.010

<!-- b000388 | prose | pages [11] -->
0.000

<!-- b000389 | prose | pages [11] -->
0.000 0.022 0.000 0.000

<!-- b000390 | prose | pages [11] -->
0.520 0.520 0.813 0.419

<!-- b000391 | prose | pages [11] -->
0.000

<!-- b000392 | prose | pages [11] -->
0.000 0.520 0.000 0.464

<!-- b000393 | prose | pages [11] -->
0.257 0.232 0.510 0.112

<!-- b000394 | prose | pages [11] -->
5

<!-- b000395 | heading | pages [11] -->
Priority Model

<!-- b000396 | prose | pages [11] -->
0.000 0.257 0.000 0.108

<!-- b000397 | prose | pages [11] -->
As Figure 4 shows, based on the results of section 4.4, each goal now has three attributes, which

<!-- b000398 | prose | pages [11] -->
are the three centrality measures of the node. Since we respectively take positive edges and negative

<!-- b000399 | prose | pages [11] -->
edges into consideration, each attribute has 2 indexes. Hence, each goal has 6 indexes. Then we use

<!-- b000400 | prose | pages [11] -->
Entropy Weight Method (EWM) to get the weight of each index. Afterwards, we use weighted TOP-

<!-- b000401 | prose | pages [11] -->
SIS[14] to get scores for all 17 goals. Priorities of the 17 goals are based on these scores. The higher

<!-- b000402 | prose | pages [11] -->
scores, the higher priority.

<!-- b000403 | prose | pages [11] -->
In graph theory, the centrality measure is used to assess the “centrality” status of nodes in a graph.

<!-- b000404 | prose | pages [11] -->
It helps understand the importance and influence of nodes in the graph. In our Relationship Graph

<!-- b000405 | prose | pages [11] -->
Model, a goal with higher centrality means it is more important and owns larger influence. Hence, this

<!-- b000406 | prose | pages [11] -->
goal should have higher priority. After Entropy Weight Method and TOPSIS, we can get a more reliable

<!-- b000407 | prose | pages [11] -->
and comprehensive measure of centrality. Thus, priority based on our model can be effective.

<!-- b000408 | furniture | pages [11] -->


<!-- b000409 | caption | pages [11] -->
Figure 4 Overview of the Priority Model

<!-- b000410 | heading | pages [11] -->
5.1 Establishment of the Model

<!-- b000411 | prose | pages [11] -->
We first do positive management on vector

<!-- b000412 | prose | pages [11] -->
of negative edges.

<!-- b000413 | prose | pages [11] -->
, and due to they are centralities

<!-- b000414 | prose | pages [11] -->
Then, we combine the six indexes of the ith goal into a vector

<!-- b000415 | furniture | pages [11] -->


<!-- b000416 | prose | pages [11] -->
. It can be described as

<!-- b000417 | furniture | pages [12] -->
Team # 2300229                                                       page 12 of 25

<!-- b000418 | furniture | pages [12] -->


<!-- b000419 | furniture | pages [12] -->


<!-- b000420 | prose | pages [12] -->
(11)

<!-- b000421 | prose | pages [12] -->
of all 17 goals into a Afterwards, we combine

<!-- b000422 | furniture | pages [12] -->


<!-- b000423 | prose | pages [12] -->
matrix . Hence, is

<!-- b000424 | furniture | pages [12] -->


<!-- b000425 | prose | pages [12] -->
(12)

<!-- b000426 | heading | pages [12] -->
5.1.1 Sub-Model 1: Weight Entropy Method Model

<!-- b000427 | prose | pages [12] -->
Step1: Normalize the matrix .The standardized formula is

<!-- b000428 | furniture | pages [12] -->


<!-- b000429 | furniture | pages [12] -->


<!-- b000430 | prose | pages [12] -->
(13)

<!-- b000431 | prose | pages [12] -->
Step2: Calculate the proportion of the ith goal in the jth index, which is regarded as the probability

<!-- b000432 | prose | pages [12] -->
used in the calculation of relative entropy later. The calculation method is

<!-- b000433 | furniture | pages [12] -->


<!-- b000434 | furniture | pages [12] -->


<!-- b000435 | prose | pages [12] -->
(14)

<!-- b000436 | prose | pages [12] -->
Step3: Calculate the information entropy and the information utility value of each attribute.

<!-- b000437 | prose | pages [12] -->
For the jth attribute, the formula for calculating its information entropy is

<!-- b000438 | furniture | pages [12] -->


<!-- b000439 | furniture | pages [12] -->


<!-- b000440 | prose | pages [12] -->
(15)

<!-- b000441 | prose | pages [12] -->
For the jth attribute, the calculation method of its information utility value is

<!-- b000442 | furniture | pages [12] -->


<!-- b000443 | furniture | pages [12] -->


<!-- b000444 | prose | pages [12] -->
(16)

<!-- b000445 | prose | pages [12] -->
Step4: Calculate the entropy weight of each attribute. The entropy weight of each attribute is the

<!-- b000446 | prose | pages [12] -->
normalized information utility value. Its calculation method is

<!-- b000447 | furniture | pages [12] -->


<!-- b000448 | heading | pages [12] -->
5.1.2 Sub-Model 2: TOPSIS Model

<!-- b000449 | furniture | pages [12] -->


<!-- b000450 | prose | pages [12] -->
(17)

<!-- b000451 | prose | pages [12] -->
to eliminate the influence of different index dimensions. The Step1: Standardize the matrix

<!-- b000452 | prose | pages [12] -->
and each element in normalized matrix is denoted as

<!-- b000453 | furniture | pages [12] -->


<!-- b000454 | prose | pages [12] -->
And the standardized matrix is

<!-- b000455 | furniture | pages [12] -->


<!-- b000456 | prose | pages [12] -->
is

<!-- b000457 | furniture | pages [12] -->


<!-- b000458 | prose | pages [12] -->
(18)

<!-- b000459 | furniture | pages [13] -->
Team # 2300229                                                       page 13 of 25

<!-- b000460 | furniture | pages [13] -->


<!-- b000461 | furniture | pages [13] -->


<!-- b000462 | prose | pages [13] -->
(19)

<!-- b000463 | prose | pages [13] -->
Step2: Define the optimal vector and the worst vector. We use

<!-- b000464 | prose | pages [13] -->
and use to denote the worst vector. Hence,

<!-- b000465 | furniture | pages [13] -->


<!-- b000466 | prose | pages [13] -->
And is

<!-- b000467 | furniture | pages [13] -->


<!-- b000468 | prose | pages [13] -->
to denote the optimal vector

<!-- b000469 | prose | pages [13] -->
is

<!-- b000470 | furniture | pages [13] -->


<!-- b000471 | prose | pages [13] -->
(20)

<!-- b000472 | furniture | pages [13] -->


<!-- b000473 | prose | pages [13] -->
(21)

<!-- b000474 | prose | pages [13] -->
Step3: Calculate the weighted Euclidean distance between the indexes of goals and the optimal

<!-- b000475 | prose | pages [13] -->
vector:

<!-- b000476 | furniture | pages [13] -->


<!-- b000477 | furniture | pages [13] -->


<!-- b000478 | prose | pages [13] -->
(22)

<!-- b000479 | prose | pages [13] -->
Step4: Calculate the weighted Euclidean distance between the indexes of goals and the worst

<!-- b000480 | prose | pages [13] -->
vector:

<!-- b000481 | furniture | pages [13] -->


<!-- b000482 | prose | pages [13] -->
Step5: Calculate the scores of goals:

<!-- b000483 | furniture | pages [13] -->


<!-- b000484 | furniture | pages [13] -->


<!-- b000485 | prose | pages [13] -->
(23)

<!-- b000486 | furniture | pages [13] -->


<!-- b000487 | prose | pages [13] -->
(24)

<!-- b000488 | prose | pages [13] -->
The priority of each goal is ordered by the score from TOPSIS Model. The higher score

<!-- b000489 | prose | pages [13] -->
higher priority.

<!-- b000490 | heading | pages [13] -->
5.2 Results and Analysis

<!-- b000491 | prose | pages [13] -->
, the

<!-- b000492 | caption | pages [13] -->
Figure 5 shows priorities of the 17 goals of the three countries. For Turkey, priorities of Goal 17

<!-- b000493 | prose | pages [13] -->
and Goal 9 outweigh priorities of others. For Indonesia and Mexico, the priority of Goal 3 is largely

<!-- b000494 | prose | pages [13] -->
higher than other goals. Differences of priorities are mainly due to different situations of each country.

<!-- b000495 | furniture | pages [13] -->


<!-- b000496 | furniture | pages [13] -->


<!-- b000497 | furniture | pages [13] -->


<!-- b000498 | caption | pages [13] -->
Figure 5 Radar Map of the Normalization TOPSIS Scores

<!-- b000499 | furniture | pages [13] -->


<!-- b000500 | furniture | pages [14] -->
Team # 2300229                                                       page 14 of 25

<!-- b000501 | prose | pages [14] -->
Results presented in Table 3 shows the top five priority goals of the three countries. We have some

<!-- b000502 | prose | pages [14] -->
discoveries from the table. We find that Goal 3 and Goal 4 are in the top5 lists of all countries. Goal 3

<!-- b000503 | prose | pages [14] -->
is about health, while goal 4 is about education. In reality, health and education are great concerns of

<!-- b000504 | prose | pages [14] -->
all countries. They are closely related to the economic and social development of a country. They have

<!-- b000505 | prose | pages [14] -->
important impacts on the welfare of the people and the long-term development of the country.

<!-- b000506 | caption | pages [14] -->
Table 3 Top 5 priority goals

<!-- b000507 | prose | pages [14] -->
Indonesia Turkey Mexico

<!-- b000508 | prose | pages [14] -->
Goal Score Goal Score Goal Score

<!-- b000509 | prose | pages [14] -->
17 0.160 3

<!-- b000510 | prose | pages [14] -->
9 0.156 9

<!-- b000511 | prose | pages [14] -->
7 0.094 6

<!-- b000512 | prose | pages [14] -->
3 0.088 10

<!-- b000513 | prose | pages [14] -->
4 0.050 4

<!-- b000514 | prose | pages [14] -->
0.275 3 0.250

<!-- b000515 | prose | pages [14] -->
0.137 10 0.061

<!-- b000516 | prose | pages [14] -->
0.053 4 0.060

<!-- b000517 | prose | pages [14] -->
0.046 6 0.060

<!-- b000518 | prose | pages [14] -->
0.046 8 0.058

<!-- b000519 | prose | pages [14] -->
Advice for the United Nation: Generally, Goal 3 and Goal 4 are high priority goals of all coun-

<!-- b000520 | prose | pages [14] -->
tries, which are about health and education respectively. We suggest the United Nation organize some

<!-- b000521 | prose | pages [14] -->
cooperation plans on health and education. With concerted efforts from all of us, we can accomplish

<!-- b000522 | prose | pages [14] -->
the health and education goal more efficiently and effectively. Besides, priorities of goals differ from

<!-- b000523 | prose | pages [14] -->
country to country. Hence, we suggest the United Nation offer more free choice to countries. We think

<!-- b000524 | prose | pages [14] -->
it a good idea to enable the country to decide priorities on their own.

<!-- b000525 | prose | pages [14] -->
6

<!-- b000526 | heading | pages [14] -->
Temporal Champagne Tower Model for Future Development

<!-- b000527 | prose | pages [14] -->
When we pour champagne for a tower which is composed of wine cups, only when the upper cup

<!-- b000528 | prose | pages [14] -->
is filled, the lower cup can get champagne. This phenomenon inspires us to propose Temporal Cham-

<!-- b000529 | prose | pages [14] -->
pagne Tower Model.

<!-- b000530 | prose | pages [14] -->
We want to measure completion status of the 17 goals. We use Temporal Champagne Tower

<!-- b000531 | prose | pages [14] -->
Model to measure the completion status of the 17 goals if they are in the priority order we set. The

<!-- b000532 | prose | pages [14] -->
model is based on Assumption 2, which is the completion difficulties of all 17 SDGs are the same.

<!-- b000533 | prose | pages [14] -->
This means one percent completion of Goal i equals that of Goal j.

<!-- b000534 | prose | pages [14] -->
As Figure 6 shows, since our priorities are initiated, all the resources will be allocated to the top

<!-- b000535 | prose | pages [14] -->
priority goal. Supposing we have 4 goals in total. The priorities of the 4 goals are

<!-- b000536 | prose | pages [14] -->
Goal1>Goal2>Goal3>Goal4, as the shade of green color shows. Goal 1 is correlated to Goal 2. Goal

<!-- b000537 | prose | pages [14] -->
3 is correlated to Goal 2 and Goal 4. Of course, each goal is correlated to itself. In year , Goal 1 will

<!-- b000538 | prose | pages [14] -->
be allocated all resources, as the dark blue arrow shows. Goal 2 has synergistic or tradeoff relationships

<!-- b000539 | prose | pages [14] -->
), Goal 2 will benefit synergistic resources from Goal1 or it will with Goal 1. So, next year (

<!-- b000540 | prose | pages [14] -->
compete resources with Goal 1, as denoted by orange arrow. Next year (

<!-- b000541 | furniture | pages [14] -->


<!-- b000542 | prose | pages [14] -->
), Goal 3 is added to the

<!-- b000543 | furniture | pages [15] -->
Team # 2300229                                                       page 15 of 25

<!-- b000544 | prose | pages [15] -->
development queue due to its relationship with Goal 2. We assume Goal 1 is complete this year before

<!-- b000545 | prose | pages [15] -->
all the allocated resources are used up. As shown in light blue arrow, some remaining resources will

<!-- b000546 | prose | pages [15] -->
be allocated to Goal 2, which is just one level lower in priority of Goal 1. Then next year ( ), Goal

<!-- b000547 | prose | pages [15] -->
1 will be put in complete queue, with no resources allocated. Goal 2 will be allocated all resources,

<!-- b000548 | prose | pages [15] -->
which owns the highest priority among the rest. The mathematical expression of the model will be

<!-- b000549 | prose | pages [15] -->
discussed in the subsection below.

<!-- b000550 | furniture | pages [15] -->


<!-- b000551 | caption | pages [15] -->
Figure 6 Overview of Temporal Champagne Tower Model

<!-- b000552 | heading | pages [15] -->
6.1 Mathematical Establishment of the Model

<!-- b000553 | prose | pages [15] -->
to denote the percentage complete To measure the completion status of the 17 SDGs, we use

<!-- b000554 | prose | pages [15] -->
of 17 SDGs of year . Hence, we have

<!-- b000555 | furniture | pages [15] -->


<!-- b000556 | furniture | pages [15] -->


<!-- b000557 | prose | pages [15] -->
(25)

<!-- b000558 | prose | pages [15] -->
is the percentage complete of the ith goal of the year where .

<!-- b000559 | prose | pages [15] -->
to denote the development queue for the 17 SDGs in year We use . Since our priority is

<!-- b000560 | prose | pages [15] -->
, where initiated, we have is the priority score of goal from section

<!-- b000561 | prose | pages [15] -->
5.2. Then some goals are positively or negatively correlated to goals in . We use to represent

<!-- b000562 | prose | pages [15] -->
the set for all these correlated goals. Hence, we have

<!-- b000563 | furniture | pages [15] -->


<!-- b000564 | prose | pages [15] -->
where is the weight between two goals. If

<!-- b000565 | prose | pages [15] -->
Then we update for year to

<!-- b000566 | prose | pages [15] -->
basis of . Hence, we have

<!-- b000567 | furniture | pages [15] -->


<!-- b000568 | furniture | pages [15] -->


<!-- b000569 | furniture | pages [15] -->


<!-- b000570 | prose | pages [15] -->
(26)

<!-- b000571 | prose | pages [15] -->
, then these two goals are not correlated.

<!-- b000572 | prose | pages [15] -->
. .

<!-- b000573 | prose | pages [15] -->
should include all correlated goals on the

<!-- b000574 | furniture | pages [15] -->


<!-- b000575 | prose | pages [15] -->
(27)

<!-- b000576 | furniture | pages [16] -->
Team # 2300229                                                       page 16 of 25

<!-- b000577 | prose | pages [16] -->
to denote total resources allocated for 17 SDGs in each year. Then the allocated re- We use

<!-- b000578 | prose | pages [16] -->
sources for the ith goal is . We assume total accumulated resources comply a linear relationship

<!-- b000579 | prose | pages [16] -->
with the year. Then total resources for each year is 17 times the slope of the linear regression.

<!-- b000580 | prose | pages [16] -->
to denote the change of percentage complete of the ith goal in year We use exclusively

<!-- b000581 | prose | pages [16] -->
from the correlation with other goals and itself. Hence, we have

<!-- b000582 | furniture | pages [16] -->


<!-- b000583 | furniture | pages [16] -->


<!-- b000584 | prose | pages [16] -->
(28)

<!-- b000585 | prose | pages [16] -->
is a constant to measure the efficiency of the correlation impact, where is the weight between

<!-- b000586 | prose | pages [16] -->
represents the total resources the jth goal gets in two goals and

<!-- b000587 | prose | pages [16] -->
equal to 5 inspired by Pareto's principle.

<!-- b000588 | prose | pages [16] -->
year. We set

<!-- b000589 | prose | pages [16] -->
to denote the resources allocated from We use

<!-- b000590 | prose | pages [16] -->
method is

<!-- b000591 | furniture | pages [16] -->


<!-- b000592 | prose | pages [16] -->
to goal in year . Its calculation

<!-- b000593 | prose | pages [16] -->
(29)

<!-- b000594 | prose | pages [16] -->
, this means the goal is already complete at the moment If , then we don’t need

<!-- b000595 | prose | pages [16] -->
to allocate resources to it any more. Otherwise, it will be allocated resources which are remaining

<!-- b000596 | prose | pages [16] -->
resources after higher priority goals are allocated.

<!-- b000597 | prose | pages [16] -->
for goal Hence, the percentage complete

<!-- b000598 | furniture | pages [16] -->


<!-- b000599 | prose | pages [16] -->
in year is

<!-- b000600 | furniture | pages [16] -->


<!-- b000601 | prose | pages [16] -->
(30)

<!-- b000602 | heading | pages [16] -->
6.2 Temporal Champagne Tower Model

<!-- b000603 | prose | pages [16] -->
Based on the above analysis, our Temporal Champagne Tower Model can be concluded as:

<!-- b000604 | furniture | pages [16] -->


<!-- b000605 | furniture | pages [16] -->


<!-- b000606 | prose | pages [16] -->
(31)

<!-- b000607 | furniture | pages [17] -->
Team # 2300229                                                       page 17 of 25

<!-- b000608 | heading | pages [17] -->
6.3 Model Solutions based on Time Series Algorithms

<!-- b000609 | prose | pages [17] -->
The algorithm corresponding to Temporal Champagne Tower Model is described as Table 4. Via

<!-- b000610 | prose | pages [17] -->
the algorithm, we can predict the percentage complete of each goal in the next 10 years.

<!-- b000611 | caption | pages [17] -->
Table 4 The Algorithm corresponding to the Model

<!-- b000612 | heading | pages [17] -->
Algorithm: Solutions of Cooperation Strategy Model

<!-- b000613 | prose | pages [17] -->
Input:

<!-- b000614 | prose | pages [17] -->
, ,

<!-- b000615 | furniture | pages [17] -->


<!-- b000616 | prose | pages [17] -->
Output:

<!-- b000617 | furniture | pages [17] -->


<!-- b000618 | prose | pages [17] -->
1: for

<!-- b000619 | furniture | pages [17] -->


<!-- b000620 | prose | pages [17] -->
2:   Initialize ,

<!-- b000621 | furniture | pages [17] -->


<!-- b000622 | prose | pages [17] -->
3: Initialize

<!-- b000623 | furniture | pages [17] -->


<!-- b000624 | prose | pages [17] -->
4: for

<!-- b000625 | furniture | pages [17] -->


<!-- b000626 | prose | pages [17] -->
5:   for

<!-- b000627 | furniture | pages [17] -->


<!-- b000628 | prose | pages [17] -->
6:     Update via equation (28)

<!-- b000629 | prose | pages [17] -->
7:     Update via equation (29)

<!-- b000630 | prose | pages [17] -->
8:     Update via equation (30)

<!-- b000631 | prose | pages [17] -->
9:   end

<!-- b000632 | prose | pages [17] -->
10:   Update via equation (26)

<!-- b000633 | prose | pages [17] -->
11:   if

<!-- b000634 | furniture | pages [17] -->


<!-- b000635 | prose | pages [17] -->
12:     Update via equation (27)

<!-- b000636 | prose | pages [17] -->
13:   end

<!-- b000637 | prose | pages [17] -->
14: end

<!-- b000638 | heading | pages [17] -->
6.4 One Goal Being Achieved

<!-- b000639 | prose | pages [17] -->
As Figure 7 shows, we assume Goal 3 is achieved in year . Then Goal 3 will be put in complete

<!-- b000640 | prose | pages [17] -->
queue, as the bubble in the figure shows. No change on priorities will occur to goals which are not

<!-- b000641 | prose | pages [17] -->
complete. This is because determination of priority is based on solid analysis on data from a long

<!-- b000642 | prose | pages [17] -->
period of time. We think it inappropriate to change the priority due to some unexpected events. There-

<!-- b000643 | prose | pages [17] -->
fore, in year , the resources will be allocated to Goal 1, which owns the highest priority in develop-

<!-- b000644 | prose | pages [17] -->
ment list. Some goals may compete resources with Goal 3. Therefore, Goal 3 may back to uncomplete

<!-- b000645 | prose | pages [17] -->
status. This is quite common in our daily life. A farmer may get rid of poverty last year, but return to

<!-- b000646 | prose | pages [17] -->
poverty next year, due to some factors like bad weather, etc. So, Goal 3 returns to development list,

<!-- b000647 | furniture | pages [17] -->


<!-- b000648 | furniture | pages [18] -->
Team # 2300229                                                       page 18 of 25

<!-- b000649 | prose | pages [18] -->
but now it owns the highest priority. This is because, although back to uncomplete, Goal 3 is still very

<!-- b000650 | prose | pages [18] -->
close to complete status. Hence, it is reasonable to set Goal 3 the highest priority. After being allocated,

<!-- b000651 | prose | pages [18] -->
there will be some remaining resources, as the light blue arrow shows. The remaining resources can

<!-- b000652 | prose | pages [18] -->
be allocated to Goal 1, which has the highest priority among the rest. It can also be allocated to other

<!-- b000653 | prose | pages [18] -->
goals which are close related to Goal 3 and should be added to SGDs. As for multiple complete goals,

<!-- b000654 | prose | pages [18] -->
the priorities among them are sorted according to the priority orders obtained by the Priority Model.

<!-- b000655 | prose | pages [18] -->
Priority of any complete goal is greater than uncomplete ones.

<!-- b000656 | furniture | pages [18] -->


<!-- b000657 | caption | pages [18] -->
Figure 7 Overview of Temporal Champagne Tower Model When a Goal Achieved

<!-- b000658 | heading | pages [18] -->
6.5 Results and Analysis

<!-- b000659 | prose | pages [18] -->
To do simulation, we get some data from an authoritative website[15]. Since, each country has a

<!-- b000660 | prose | pages [18] -->
different situation, we choose Indonesia as an example. As shown in Table 5, by 2033, Indonesia can

<!-- b000661 | prose | pages [18] -->
achieve Goal 3, Goal 4, Goal6, Goal 9 and Goal 13. The first 4 goals are generally about people’s

<!-- b000662 | prose | pages [18] -->
livelihood. The fifth achieved goal is about the climate. In total, Indonesia achieves 13% of increase

<!-- b000663 | prose | pages [18] -->
of overall goals within the 10 years.

<!-- b000664 | caption | pages [18] -->
Figure 8.a shows the percentage complete of each goal change over time. From 2025 to 2026,

<!-- b000665 | prose | pages [18] -->
Goal 3 is achieved, and the remaining resources are allocated to Goal 9. Hence, we can notice a huge

<!-- b000666 | prose | pages [18] -->
leap of Goal 9 between 2025 and 2026, as the orange line shows. Afterwards, the structure of network

<!-- b000667 | prose | pages [18] -->
in Temporal Champagne Tower Model is changed. Goals which are positively correlated to Goal 9

<!-- b000668 | prose | pages [18] -->
increase faster. This impact comes from the achievement of Goal 3. Similar impacts occur when other

<!-- b000669 | prose | pages [18] -->
goals are achieved. Considering that when a goal has been completed, although it can’t exceed 100%,

<!-- b000670 | prose | pages [18] -->
its correlation benefits can affect other counties. Therefore, we propose Goal 18: International Coop-

<!-- b000671 | prose | pages [18] -->
eration. Help other countries achieve their goals with the correlation benefits of complete goals. For

<!-- b000672 | furniture | pages [18] -->


<!-- b000673 | furniture | pages [19] -->
Team # 2300229                                                       page 19 of 25

<!-- b000674 | prose | pages [19] -->
example, since Goal 3 is achieved, we emphasize international cooperation on health.

<!-- b000675 | prose | pages [19] -->
As shown in Figure 8.b, the orange line shows the change of percentage complete for overall goal

<!-- b000676 | prose | pages [19] -->
from Temporal Champagne Tower Model. The blue line shows the result of linear regression and its

<!-- b000677 | prose | pages [19] -->
prediction. By 2033, Indonesia can achieve 82 percent of SDGs, according to our model. However, it

<!-- b000678 | prose | pages [19] -->
can achieve 78 percent of SDGs, according to its current plan. Therefore, our model can enable Indo-

<!-- b000679 | prose | pages [19] -->
nesia to achieve 4 more percent of SDGs, which shows the superiority of our model.

<!-- b000680 | heading | pages [19] -->
Advice for the United Nation: Temporal Champagne Tower Model enables Indonesia achieve

<!-- b000681 | prose | pages [19] -->
82% of SDGs by 2033, which is 4% higher than the predicted result of its current plan. We would

<!-- b000682 | prose | pages [19] -->
appreciate it if the United Nation could recommend our model to other countries. Our model can pro-

<!-- b000683 | prose | pages [19] -->
mote the speed of SDG development. In addition, Goal 7, Goal 11 and Goal 17 are less than 60%

<!-- b000684 | prose | pages [19] -->
complete by 2033. The cost of achieving these goals is too high for countries like Indonesia. Hence,

<!-- b000685 | prose | pages [19] -->
we suggest the United Nation lower the standard on these three goals for countries like Indonesia. We

<!-- b000686 | prose | pages [19] -->
also recommend the United Nation appeal some developed countries offering some help to these coun-

<!-- b000687 | prose | pages [19] -->
tries.

<!-- b000688 | prose | pages [19] -->
a) Predictions for 17 Goals b) Predictions for Total Goals

<!-- b000689 | caption | pages [19] -->
Figure 8 Predictions for Next 10 Years

<!-- b000690 | caption | pages [19] -->
Table 5 Percentage Complete Comparison

<!-- b000691 | furniture | pages [19] -->


<!-- b000692 | prose | pages [19] -->
Goal 1 Goal 2 Goal 3

<!-- b000693 | prose | pages [19] -->
2022/2033 81/96 66/78 66/100

<!-- b000694 | prose | pages [19] -->
Goal 4 Goal 5 Goal 6 Goal 7 Goal 8

<!-- b000695 | prose | pages [19] -->
93/100 64/81 70/100 73/54 73/91

<!-- b000696 | caption | pages [19] -->
Table 5 Percentage Complete Comparison(continued)

<!-- b000697 | prose | pages [19] -->
Goal 9 Goal10 Goal11 Goal12 Goal13

<!-- b000698 | prose | pages [19] -->
44/100 56/81 71/57 93/76 93/100

<!-- b000699 | prose | pages [19] -->
7 Analysis on the Impacts

<!-- b000700 | heading | pages [19] -->
7.1 COVID-19 Impact on Models

<!-- b000701 | prose | pages [19] -->
Goal14 Goal15 Goal16 Goal17 Total

<!-- b000702 | prose | pages [19] -->
65/82 51/66 71/72 51/59 69/82

<!-- b000703 | prose | pages [19] -->
Impacts of COVID-19 are complicated. Some goals are threatened by the epidemic. Some goals

<!-- b000704 | furniture | pages [19] -->


<!-- b000705 | furniture | pages [20] -->
Team # 2300229                                                       page 20 of 25

<!-- b000706 | prose | pages [20] -->
may mitigate or aggravate its impacts. Based on the study of Robin Naidoo[7], we get some adjustment

<!-- b000707 | prose | pages [20] -->
to measure the threat level of the goal to our model. We use coefficient . If one goal is threatened,

<!-- b000708 | prose | pages [20] -->
its allocated resources will be affected. Hence, we update equation (29) into

<!-- b000709 | furniture | pages [20] -->


<!-- b000710 | prose | pages [20] -->
(32)

<!-- b000711 | prose | pages [20] -->
Some goals may mitigate or aggravate the impact of COVID-19, which means their priority may

<!-- b000712 | prose | pages [20] -->
to measure the mitigation or aggravating level of the goal be changed. We use parameter

<!-- b000713 | prose | pages [20] -->
Then we update equation (11) to

<!-- b000714 | furniture | pages [20] -->


<!-- b000715 | prose | pages [20] -->
.

<!-- b000716 | furniture | pages [20] -->


<!-- b000717 | prose | pages [20] -->
(33)

<!-- b000718 | prose | pages [20] -->
After the adjustment, we rerun Priority Model and Temporal Champagne Tower Model to study

<!-- b000719 | prose | pages [20] -->
the impact of COVID-19.

<!-- b000720 | heading | pages [20] -->
7.2 Results and Analysis

<!-- b000721 | prose | pages [20] -->
As shown in Table 6, by 2033, Indonesia can achieve Goal 3, Goal 4 and Goal 9. Two goals were

<!-- b000722 | prose | pages [20] -->
missed compared to previous result without the effect of COVID-19. In total, Indonesia achieves 9

<!-- b000723 | prose | pages [20] -->
percent of increase of overall goals within the 10 years, which is 4 percent less than previous result.

<!-- b000724 | caption | pages [20] -->
Figure 9.a shows the percentage complete of each goal change over time. Compared to Figure 8.a,

<!-- b000725 | prose | pages [20] -->
all goals are achieved later due to the effects of COVID-19.

<!-- b000726 | prose | pages [20] -->
As shown in Figure 9.b, the orange line shows the change of percentage complete without the

<!-- b000727 | prose | pages [20] -->
effect of COVID-19. The green line shows the change with the effect of COVID-19. The blue line

<!-- b000728 | prose | pages [20] -->
shows the result of linear regression and its prediction. By 2033, Indonesia can achieve 82 percent of

<!-- b000729 | prose | pages [20] -->
SDGs without the effect of COVID-19. However, it can only achieve 78 percent of SDGs with the

<!-- b000730 | prose | pages [20] -->
effect. The speed of SDG development also becomes lower after the epidemic.

<!-- b000731 | caption | pages [20] -->
Figure 9 Predictions for Next 10 Years Affected by COVID-19

<!-- b000732 | furniture | pages [20] -->


<!-- b000733 | furniture | pages [21] -->
Team # 2300229                                                       page 21 of 25

<!-- b000734 | caption | pages [21] -->
Table 6 Percentage Complete Comparison on the Effect of COVID-19

<!-- b000735 | furniture | pages [21] -->


<!-- b000736 | prose | pages [21] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8

<!-- b000737 | prose | pages [21] -->
100/100 100/100 Without/With 96/91 78/70 81/77 100/77 54/60 91/83

<!-- b000738 | caption | pages [21] -->
Table 6 Percentage Complete Comparison on the Effect of COVID-19(continued)

<!-- b000739 | prose | pages [21] -->
Goal 9 Goal10 Goal11 Goal12 Goal13 Goal14 Goal15 Goal16 Goal17 Total

<!-- b000740 | prose | pages [21] -->
100/100 81/69 57/60 76/80 100/98 82/78 66/60 72/72 59/57 82/78

<!-- b000741 | prose | pages [21] -->
Advice for the United Nation: Unexpected events like COVID-19 have huge impacts on the

<!-- b000742 | prose | pages [21] -->
speed of SDG development. Hence, we recommend the United Nation prolong the deadline for the

<!-- b000743 | prose | pages [21] -->
achievement of SDGs appropriately. Besides, priorities of some goals may also be affected. This means

<!-- b000744 | prose | pages [21] -->
the United Nation may need to adjust the focus of their work. Some plans are recommended to made

<!-- b000745 | prose | pages [21] -->
which could alleviate the impact of these unexpected events.

<!-- b000746 | heading | pages [21] -->
7.3 Model Impact on Companies and Organizations

<!-- b000747 | prose | pages [21] -->
The sustainable development framework including 17 SDGs can provide guiding directions and

<!-- b000748 | prose | pages [21] -->
even strategies for companies or organizations. Our previous work is based on country-level data.

<!-- b000749 | prose | pages [21] -->
Different strategies are needed for different sizes of companies or organizations. The total amount of

<!-- b000750 | prose | pages [21] -->
social resources that a company or organization can provide is often smaller than those of a country.

<!-- b000751 | prose | pages [21] -->
Companies or organizations need to consider the priorities of different goals more carefully.

<!-- b000752 | prose | pages [21] -->
The first thing to point out is that the higher the priority of the goal at the national level, the greater

<!-- b000753 | prose | pages [21] -->
the demand and the investment for the goal. Therefore, smaller companies or organizations can derive

<!-- b000754 | prose | pages [21] -->
enterprise- or organization-level priorities based on their own business or positioning, combined with

<!-- b000755 | prose | pages [21] -->
country-level priorities obtained from our network. Companies or organizations that use this priority

<!-- b000756 | prose | pages [21] -->
to guide their development may more easily obtain investment or donations to maintain a long-term

<!-- b000757 | prose | pages [21] -->
sustainable development.

<!-- b000758 | prose | pages [21] -->
For larger companies or organizations, they have easier access to investment or donations than

<!-- b000759 | prose | pages [21] -->
smaller ones. So, they can consider multiple priorities or synergies between multiple goals within the

<!-- b000760 | prose | pages [21] -->
global common framework provided by the SDGs. Synergies between multiple SDG goals can be

<!-- b000761 | prose | pages [21] -->
obtained through our Priority Model. If a company or organization needs a longer-term perspective, it

<!-- b000762 | prose | pages [21] -->
can use our Temporal Champagne Tower Model with some data to adjust the priority of its goals.

<!-- b000763 | prose | pages [21] -->
It is worth noting that our model will reflect the impact of certain international crises, such as

<!-- b000764 | prose | pages [21] -->
COVID-19, which requires companies or organizations to adapt to the times and focus on the selected

<!-- b000765 | prose | pages [21] -->
SDG goals.

<!-- b000766 | prose | pages [21] -->
The usage of our models for companies or organizations can be concluded as Figure 10.

<!-- b000767 | furniture | pages [21] -->


<!-- b000768 | furniture | pages [22] -->
Team # 2300229                                                       page 22 of 25

<!-- b000769 | furniture | pages [22] -->


<!-- b000770 | caption | pages [22] -->
Figure 10 How Companies or Organizations Use Our Model

<!-- b000771 | prose | pages [22] -->
8

<!-- b000772 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000773 | prose | pages [22] -->
In order to evaluate the sensitivity and robustness of the Temporal Champagne Tower Model, we

<!-- b000774 | prose | pages [22] -->
perform two sensitivity tests on the hyperparameters and in the Temporal Champagne Tower

<!-- b000775 | prose | pages [22] -->
Model, respectively. 𝐶 is a constant to measure the efficiency of the synergy and 𝐷 denotes total

<!-- b000776 | prose | pages [22] -->
resources allocated for 17 SDGs in each year.

<!-- b000777 | prose | pages [22] -->
In Section 6, we performed a linear regression on Indonesia's overall score from 2012 to 2022

<!-- b000778 | prose | pages [22] -->
with year as the independent variable and the overall score as the dependent variable. Here we do the

<!-- b000779 | prose | pages [22] -->
same for Turkey and Mexico. The 𝑅2 and p-values of the linear regression for Turkey and Mexico

<!-- b000780 | prose | pages [22] -->
are 0.767, 4.13 × 10−4 and 0.882, 1.78 × 10−5, respectively, which demonstrates the validity of the

<!-- b000781 | prose | pages [22] -->
linear regression.

<!-- b000782 | prose | pages [22] -->
The 95% confidence intervals for the value of 𝐷 are determined for the two countries separately

<!-- b000783 | prose | pages [22] -->
by linear regression. We choose the 17 times of midpoint of the interval as an estimate of 𝐷 and obtain

<!-- b000784 | prose | pages [22] -->
𝐷 of 0.036 and 0.071 for Turkey and Mexico, respectively. In section 6, we have determined that D

<!-- b000785 | prose | pages [22] -->
for Indonesia is 0.102.

<!-- b000786 | prose | pages [22] -->
When performing the sensitivity test on 𝐶, we traverse the values of 𝐶 from 4 to 6 with a step

<!-- b000787 | prose | pages [22] -->
size of 0.1, and run the Temporal Champagne Tower Model separately for each value of C. We show

<!-- b000788 | prose | pages [22] -->
the results in Figure 11.a. The intersection of the two red dotted lines in the figure represents our 𝐶

<!-- b000789 | prose | pages [22] -->
value and the final overall score in Section 6.

<!-- b000790 | prose | pages [22] -->
When conducting the sensitivity test on 𝐷, we fix 𝐶 to 5, traverse the value of 𝐷 from 0.102

<!-- b000791 | prose | pages [22] -->
to 0.136 with a step size of 1.62 × 10−3, and display the results in Figure 11.b. The intersection of

<!-- b000792 | prose | pages [22] -->
the two red dotted lines in the figure represents our 𝐷 value and the final result in Section 6.

<!-- b000793 | prose | pages [22] -->
From the result of sensitivity analysis for 𝐶, we can see that the change trends of the three lines

<!-- b000794 | prose | pages [22] -->
are relatively flat. The difference between the maximum and minimum overall score for Indonesia,

<!-- b000795 | furniture | pages [22] -->


<!-- b000796 | furniture | pages [23] -->
Team # 2300229                                                       page 23 of 25

<!-- b000797 | prose | pages [23] -->
Turkey, and Mexico is 0.041, 0.007, and 0.006, respectively.

<!-- b000798 | prose | pages [23] -->
From Figure 11.b, we can see that the change in overall score caused by the change of 𝐷 is very

<!-- b000799 | prose | pages [23] -->
small. The difference between the maximum and minimum overall score for Indonesia is 0.028.

<!-- b000800 | prose | pages [23] -->
The above analysis shows that our Temporal Champagne Tower Model is insensitive to both hy-

<!-- b000801 | prose | pages [23] -->
perparameters and , and thus is robust.

<!-- b000802 | prose | pages [23] -->
a) Result of Sensitivity Analysis for

<!-- b000803 | furniture | pages [23] -->


<!-- b000804 | furniture | pages [23] -->


<!-- b000805 | furniture | pages [23] -->


<!-- b000806 | furniture | pages [23] -->


<!-- b000807 | prose | pages [23] -->
b) Result of Sensitivity Analysis for

<!-- b000808 | furniture | pages [23] -->


<!-- b000809 | caption | pages [23] -->
Figure 11 Results of Sensitivity Analysis for C and D

<!-- b000810 | prose | pages [23] -->
9

<!-- b000811 | heading | pages [23] -->
Model Evaluation and Further Discussion

<!-- b000812 | heading | pages [23] -->
9.1 Strengths of the Model

<!-- b000813 | prose | pages [23] -->
⚫ Comprehensiveness

<!-- b000814 | prose | pages [23] -->
In Relationship Graph Model and Priority Model, we considered both positive and negative

<!-- b000815 | prose | pages [23] -->
correlation effects. In Temporal Champagne Tower Model, we discussed as many factors as

<!-- b000816 | prose | pages [23] -->
possible, including the proposal of new goals and the consolidation of completed goals.

<!-- b000817 | prose | pages [23] -->
⚫ Robustness

<!-- b000818 | prose | pages [23] -->
Our model can get reasonable results for different countries with different constant.

<!-- b000819 | prose | pages [23] -->
⚫ Innovation

<!-- b000820 | prose | pages [23] -->
We are inspired by Champagne Tower and build our TCTM based on temporal network.

<!-- b000821 | prose | pages [23] -->
Through the results of the simulation, our model explains the requirements well and puts

<!-- b000822 | prose | pages [23] -->
forward more meaningful suggestions.

<!-- b000823 | heading | pages [23] -->
9.2 Weaknesses of the Model

<!-- b000824 | prose | pages [23] -->
⚫ Hyperparameters are difficult to estimate

<!-- b000825 | prose | pages [23] -->
In Section 7, we estimated the hyperparameters in the modified TCTM using expert data

<!-- b000826 | prose | pages [23] -->
from a paper in Nature (we corrected the TCTM to reflect the impact of the pandemic). How-

<!-- b000827 | prose | pages [23] -->
ever, such expert data is not readily available, so the hyperparameters of our modified model

<!-- b000828 | prose | pages [23] -->
are also difficult to estimate.

<!-- b000829 | furniture | pages [23] -->


<!-- b000830 | furniture | pages [23] -->


<!-- b000831 | furniture | pages [24] -->
Team # 2300229                                                       page 24 of 25

<!-- b000832 | heading | pages [24] -->
References

<!-- b000833 | references | pages [24] -->
[1]. G. H. Brundtland, “World commission on environment and development,” Environmental

<!-- b000834 | references | pages [24] -->
policy and law, vol. 14, no. 1, pp. 26–30, 1985.

<!-- b000835 | references | pages [24] -->
[2]. Wu J, Guo S, Huang H, et al. Information and communications technologies for sustainable

<!-- b000836 | references | pages [24] -->
development goals: state-of-the-art, needs and perspectives[J]. IEEE Communications Sur-

<!-- b000837 | references | pages [24] -->
veys & Tutorials, 2018, 20(3): 2389-2406.

<!-- b000838 | references | pages [24] -->
[3]. “Transforming our world: the 2030 agenda for sustainable development,” UN General As-

<!-- b000839 | references | pages [24] -->
sembly, New York: United Nations, 2015.

<!-- b000840 | references | pages [24] -->
[4]. Le Blanc D. Towards integration at last? The sustainable development goals as a network of

<!-- b000841 | references | pages [24] -->
targets[J]. Sustainable Development, 2015, 23(3): 176-187.

<!-- b000842 | references | pages [24] -->
[5]. Swain R B, Ranganathan S. Modeling interlinkages between sustainable development goals

<!-- b000843 | references | pages [24] -->
using network analysis[J]. World Development, 2021, 138: 105136.

<!-- b000844 | references | pages [24] -->
[6]. Pradhan P, Costa L, Rybski D, et al. A systematic study of sustainable development goal (SDG)

<!-- b000845 | references | pages [24] -->
interactions[J]. Earth's Future, 2017, 5(11): 1169-1179.

<!-- b000846 | references | pages [24] -->
[7]. Naidoo R, Fisher B. Reset sustainable development goals for a pandemic world[J]. Nature,

<!-- b000847 | references | pages [24] -->
2020, 583(7815): 198-201.

<!-- b000848 | references | pages [24] -->
[8]. Mukarram M. Impact of COVID-19 on the UN sustainable development goals (SDGs)[J].

<!-- b000849 | references | pages [24] -->
Strategic Analysis, 2020, 44(3): 253-258.

<!-- b000850 | references | pages [24] -->
[9]. United Nations Statistics Division, United Nations Global SDG Database, 2016. https://un-

<!-- b000851 | references | pages [24] -->
stats.un.org/sdgs/indicators/database.

<!-- b000852 | references | pages [24] -->
[10]. Hauke J, Kossowski T. Comparison of values of Pearson's and Spearman's correlation coeffi-

<!-- b000853 | references | pages [24] -->
cients on the same sets of data[J]. Quaestiones geographicae, 2011, 30(2): 87-93.

<!-- b000854 | references | pages [24] -->
[11]. Freeman L. A Set of measures of centrality based on betweenness. Sociometry,1977,40(1):35-

<!-- b000855 | references | pages [24] -->
41.

<!-- b000856 | references | pages [24] -->
[12]. Sabidussi G. The centrality index of a graph. Psychometrika, 1966, 31(4): 581-603

<!-- b000857 | references | pages [24] -->
[13]. Bonacich P. Power and centrality: A family of measures. American Journal of Sociology, 1987,

<!-- b000858 | references | pages [24] -->
92(5): 1170-1182.

<!-- b000859 | references | pages [24] -->
[14]. Hwang C L, Yoon K, Hwang C L, et al. Methods for multiple attribute decision making[J].

<!-- b000860 | references | pages [24] -->
Multiple attribute decision making: methods and applications a state-of-the-art survey, 1981:

<!-- b000861 | references | pages [24] -->
58-191.

<!-- b000862 | references | pages [24] -->
[15]. https://dashboards.sdgindex.org.

<!-- b000863 | furniture | pages [24] -->


<!-- b000864 | furniture | pages [24] -->


<!-- b000865 | furniture | pages [24] -->


<!-- b000866 | furniture | pages [25] -->
Team # 2300229                                                       page 25 of 25

<!-- b000867 | heading | pages [25] -->
Appendix

<!-- b000868 | caption | pages [25] -->
Table 7 Parameters for Graph of Indonesia

<!-- b000869 | prose | pages [25] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8

<!-- b000870 | furniture | pages [25] -->


<!-- b000871 | prose | pages [25] -->
0.001

<!-- b000872 | furniture | pages [25] -->


<!-- b000873 | prose | pages [25] -->
0.001 0.001 0.237 0.000 0.001 0.000 0.001

<!-- b000874 | prose | pages [25] -->
0.754

<!-- b000875 | furniture | pages [25] -->


<!-- b000876 | prose | pages [25] -->
0.754 0.754 0.929 0.503 0.754 0.000 0.754

<!-- b000877 | prose | pages [25] -->
0.303

<!-- b000878 | furniture | pages [25] -->


<!-- b000879 | prose | pages [25] -->
0.303 0.303 0.316

<!-- b000880 | furniture | pages [25] -->


<!-- b000881 | prose | pages [25] -->
0.058 0.303 0.000 0.303

<!-- b000882 | prose | pages [25] -->
0.000 0.000 0.000 0.144

<!-- b000883 | furniture | pages [25] -->


<!-- b000884 | prose | pages [25] -->
0.000 0.000 0.914 0.000

<!-- b000885 | prose | pages [25] -->
0.480 0.480 0.480 0.571

<!-- b000886 | furniture | pages [25] -->


<!-- b000887 | prose | pages [25] -->
0.000 0.000 0.857 0.480

<!-- b000888 | prose | pages [25] -->
0.197 0.197 0.197 0.308 0.000 0.000 0.657 0.197

<!-- b000889 | caption | pages [25] -->
Table 8 Parameters for Graph of Indonesia(continued)

<!-- b000890 | prose | pages [25] -->
Goal 9 Goal 10 Goal 11 Goal 12 Goal 13 Goal 14 Goal 15 Goal 16 Goal 17

<!-- b000891 | prose | pages [25] -->
0.000 0.106 0.001 0.000 0.000 0.000 0.001 0.000 0.000

<!-- b000892 | prose | pages [25] -->
0.710 0.862 0.754 0.000 0.000 0.503 0.754 0.483 0.710

<!-- b000893 | prose | pages [25] -->
0.277 0.313 0.303 0.000 0.000

<!-- b000894 | prose | pages [25] -->
0.005

<!-- b000895 | prose | pages [25] -->
0.058 0.303 0.029 0.277

<!-- b000896 | prose | pages [25] -->
0.000 0.144 0.000 0.005

<!-- b000897 | prose | pages [25] -->
0.400

<!-- b000898 | prose | pages [25] -->
0.000 0.000 0.000 0.000

<!-- b000899 | prose | pages [25] -->
0.480 0.571 0.480 0.400

<!-- b000900 | prose | pages [25] -->
0.185

<!-- b000901 | prose | pages [25] -->
0.000 0.480 0.000 0.480

<!-- b000902 | prose | pages [25] -->
0.197 0.308 0.197 0.185 0.000 0.197 0.000 0.197

<!-- b000903 | caption | pages [25] -->
Table 9 Parameters for Graph of Turkey

<!-- b000904 | prose | pages [25] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8

<!-- b000905 | furniture | pages [25] -->


<!-- b000906 | prose | pages [25] -->
0.000

<!-- b000907 | furniture | pages [25] -->


<!-- b000908 | prose | pages [25] -->
0.000 0.000 0.104 0.000 0.000 0.132 0.000

<!-- b000909 | prose | pages [25] -->
0.635

<!-- b000910 | furniture | pages [25] -->


<!-- b000911 | prose | pages [25] -->
0.635 0.310 0.710 0.431 0.635 0.447 0.635

<!-- b000912 | prose | pages [25] -->
0.326

<!-- b000913 | furniture | pages [25] -->


<!-- b000914 | prose | pages [25] -->
0.326 0.005 0.343

<!-- b000915 | furniture | pages [25] -->


<!-- b000916 | prose | pages [25] -->
0.038 0.326 0.041 0.326

<!-- b000917 | prose | pages [25] -->
0.000 0.022 0.196 0.252

<!-- b000918 | furniture | pages [25] -->


<!-- b000919 | prose | pages [25] -->
0.000 0.000 0.046 0.000

<!-- b000920 | prose | pages [25] -->
0.464 0.520 0.722 0.619

<!-- b000921 | furniture | pages [25] -->


<!-- b000922 | prose | pages [25] -->
0.394 0.481 0.481 0.481

<!-- b000923 | prose | pages [25] -->
0.108 0.257 0.472 0.294 0.062 0.209 0.226 0.209

<!-- b000924 | caption | pages [25] -->
Table 10 Parameters for Graph of Turkey(continued)

<!-- b000925 | prose | pages [25] -->
Goal 9 Goal 10 Goal 11 Goal 12 Goal 13 Goal 14 Goal 15 Goal 16 Goal 17

<!-- b000926 | prose | pages [25] -->
0.000 0.236 0.000 0.000 0.000 0.000 0.000 0.000 0.242

<!-- b000927 | prose | pages [25] -->
0.635 0.754 0.000 0.447 0.000 0.000 0.635 0.447 0.710

<!-- b000928 | prose | pages [25] -->
0.326 0.347 0.000 0.076 0.000

<!-- b000929 | prose | pages [25] -->
0.000

<!-- b000930 | prose | pages [25] -->
0.000 0.326 0.076 0.331

<!-- b000931 | prose | pages [25] -->
0.022 0.054 0.491 0.010

<!-- b000932 | prose | pages [25] -->
0.000

<!-- b000933 | prose | pages [25] -->
0.000 0.022 0.000 0.000

<!-- b000934 | prose | pages [25] -->
0.520 0.520 0.813 0.419

<!-- b000935 | prose | pages [25] -->
0.000

<!-- b000936 | prose | pages [25] -->
0.000 0.520 0.000 0.464

<!-- b000937 | prose | pages [25] -->
0.257 0.232 0.510 0.112

<!-- b000938 | furniture | pages [25] -->


<!-- b000939 | prose | pages [25] -->
0.000 0.257 0.000 0.108
