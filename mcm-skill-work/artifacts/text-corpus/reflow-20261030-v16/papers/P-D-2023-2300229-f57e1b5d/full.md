# P-D-2023-2300229-f57e1b5d

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
2300229

<!-- b000006 | heading | pages [1] -->
Summary Sheet

<!-- b000007 | title | pages [1] -->
Methods of Measuring Priority via Graph Models: Who Is the

<!-- b000008 | title | pages [1] -->
Top 1?

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In 2015, the United Nations set 17 Sustainable Development Goals (SDGs). If these goals are achieved, we could ultimately improve life of people all over the world. The 17 SDGs are not inde- pendent of each other. Their connections make the achievement of all goals much easier. In this paper, we construct three distinctive models to study how to prioritize the SDGs.

<!-- b000011 | prose | pages [1] -->
First, to find out relationships and priorities between the 17 SDGs, we propose Relationship Graph Model. In the model, we build a graph between 17 SDGs. Vertexes of the graph are the 17 goals. Edges of the graph are correlations between goals via Spearman Correlation Analysis Algo- rithm. To measure the graph, we use Betweenness Centrality, Closeness Centrality and Eigenvector Centrality. We respectively calculate centralities of positive edges and negative edges. Hence, each goal has 6 indexes. We use Entropy Weight Method to calculate weights of the 6 indexes. Then we use Weighted TOPSIS to get the priorities of the 17 goals. Goal 3 and Goal4 rank in top 5 priority list for all three countries we study. This means most countries should put health and education on the priority list of development.

<!-- b000012 | prose | pages [1] -->
Then, we study the development of the 17 SDGs in next 10 years. We propose Temporal Cham- pagne Tower Model. This model not only considers resource allocation based on priorities, but also the synergistic and trade-off relationships between goals. We use Time Series Algorithm to predict the development of SDGs in next 10 years. We allocate resources according to the method of first satisfying the higher priority goal. When a goal is achieved, we raise its priority to the highest priority queue (complete goal queue) to preferentially maintain the complete goal. We do simulation on Indo- nesia. In the next 10 years, Indonesia can achieve 5 goals. It can achieve 82% of SDGs, which is 4% higher than the result of its current plan.

<!-- b000013 | prose | pages [1] -->
Moreover, to study the impact of unexpected events like COVID-19, we make some adjustment to our models. We add two parameters to measure the impacts. Models which are about the priorities and allocated resources are adjusted based on the two parameters. We rerun our models. According to the simulation, in the next 10 years, Indonesia can only achieve 3 goals. It can achieve 78% of SDGs, which is 4% lower than the previous result.

<!-- b000014 | prose | pages [1] -->
Finally, we perform sensitivity analysis on the hyperparameters and in Temporal Cham- pagne Tower Model. The maximum variation ranges of the model results caused by the changes of and are 0.041 and 0.028, respectively, which indicates that our model has a strong robustness.

<!-- b000015 | keywords | pages [1] -->
Key words: sustainable development goals, graph centrality, topsis, entropy weight method

<!-- b000016 | furniture | pages [2] -->
Team # 2300229                                                       page 2 of 25

<!-- b000017 | heading | pages [2] -->
Contents

<!-- b000018 | contents | pages [2] -->
1 Introduction .............................................................................................................................. 3

<!-- b000019 | contents | pages [2] -->
1.1 Problem Background ..................................................................................................... 3

<!-- b000020 | contents | pages [2] -->
1.2 Literature Review .......................................................................................................... 3

<!-- b000021 | contents | pages [2] -->
1.3 Our Work ....................................................................................................................... 4

<!-- b000022 | contents | pages [2] -->
2 Assumptions and Justifications ................................................................................................ 4

<!-- b000023 | contents | pages [2] -->
3 Notations .................................................................................................................................. 5

<!-- b000024 | contents | pages [2] -->
4 Relationship Graph Model ....................................................................................................... 5

<!-- b000025 | contents | pages [2] -->
4.1 The Data ........................................................................................................................ 5

<!-- b000026 | contents | pages [2] -->
4.2 Graph Construction ....................................................................................................... 6

<!-- b000027 | contents | pages [2] -->
4.3 Graph Measurement based on Graph Theory ................................................................ 8

<!-- b000028 | contents | pages [2] -->
4.4 Results and Analysis ...................................................................................................... 8

<!-- b000029 | contents | pages [2] -->
5 Priority Model ........................................................................................................................ 11

<!-- b000030 | contents | pages [2] -->
5.1 Establishment of the Model ......................................................................................... 11

<!-- b000031 | contents | pages [2] -->
5.2 Results and Analysis .................................................................................................... 13

<!-- b000032 | contents | pages [2] -->
6 Temporal Champagne Tower Model for Future Development .............................................. 14

<!-- b000033 | contents | pages [2] -->
6.1 Mathematical Establishment of the Model .................................................................. 15

<!-- b000034 | contents | pages [2] -->
6.2 Temporal Champagne Tower Model ........................................................................... 16

<!-- b000035 | contents | pages [2] -->
6.3 Model Solutions based on Time Series Algorithms .................................................... 17

<!-- b000036 | contents | pages [2] -->
6.4 One Goal Being Achieved ........................................................................................... 17

<!-- b000037 | contents | pages [2] -->
6.5 Results and Analysis .................................................................................................... 18

<!-- b000038 | contents | pages [2] -->
7 Analysis on the Impacts ......................................................................................................... 19

<!-- b000039 | contents | pages [2] -->
7.1 COVID-19 Impact on Models ..................................................................................... 19

<!-- b000040 | contents | pages [2] -->
7.2 Results and Analysis .................................................................................................... 20

<!-- b000041 | contents | pages [2] -->
7.3 Model Impact on Companies and Organizations ........................................................ 21

<!-- b000042 | contents | pages [2] -->
8 Sensitivity Analysis ................................................................................................................ 22

<!-- b000043 | contents | pages [2] -->
9 Model Evaluation and Further Discussion ............................................................................. 23

<!-- b000044 | contents | pages [2] -->
9.1 Strengths of the Model ................................................................................................ 23

<!-- b000045 | contents | pages [2] -->
9.2 Weaknesses of the Model ............................................................................................ 23

<!-- b000046 | contents | pages [2] -->
References .................................................................................................................................... 24

<!-- b000047 | contents | pages [2] -->
Appendix ...................................................................................................................................... 25

<!-- b000048 | furniture | pages [3] -->
Team # 2300229                                                       page 3 of 25

<!-- b000049 | heading | pages [3] -->
1 Introduction

<!-- b000050 | heading | pages [3] -->
1.1 Problem Background

<!-- b000051 | prose | pages [3] -->
In 1987, the Brundtland report proposed the most recognized definition of sustainable develop- ment, which is: “Sustainable development is able to meet the requirements of the current generation and does not have to consume the capability of the future generations”[1]. Ever since then, a number of attempts at this goal have been made[2]. In 2015, the United Nations set 17 Sustainable Develop- ment Goals (SDGs)[3]. If achieved, these goals could ultimately lead to an improved life of people all over the world.

<!-- b000052 | prose | pages [3] -->
The 17 SDGs are not independent of each other. Their connections make the achievement of all goals much easier. Hence, we establish models to study their relationships as well as completing the following problems.

<!-- b000053 | prose | pages [3] -->
⚫ Create a network to reveal relationships between the 17 SDGs. The key to this problem is to measure the relationships in a mathematical way.

<!-- b000054 | prose | pages [3] -->
⚫ Set priorities for the 17 SDGs. The key to this problem is to find a reasonable standard and sort all goals under this standard.

<!-- b000055 | prose | pages [3] -->
⚫ Study the development of SDGs in next 10 years with priorities set. Study the impact from achievement of one goal. The key to this problem is to find a plan which considers the priority and the relationships between goals.

<!-- b000056 | prose | pages [3] -->
⚫ Discuss the impact of unexpected events. The key to this problem is to quantify the impacts and adjust our models based on the impacts.

<!-- b000057 | prose | pages [3] -->
⚫ Discuss the use of models in other fields. The key to this problem is to find relations be- tween SDGs and goals of companies and organizations.

<!-- b000058 | heading | pages [3] -->
1.2 Literature Review

<!-- b000059 | prose | pages [3] -->
Relationships between SDGs have been extensively studied. David Le Blanc proposed the SDG relationship graph based on the relationships between indicators and goals[4]. He concluded that some SDGs are closely related. Ranjula Bali Swain et al. used the correlation between SDG target variables to model the edges in the correlation networks[5]. They used centrality measures and community de- tection to analyze the networks. Their conclusion is that it may be effective to identify a specific com- munity of SDG targets for a specific region. Pradhan P, Costa L, Rybski D, et al. calculated the Spear- man’s correlation between the indicators, and classified correlations as synergy and trade-off. They emphasized the role of synergy in the realization of SDGs[6]. All works mentioned above used corre- lation to measure the relationship between SDGs and achieved good effects.

<!-- b000060 | prose | pages [3, 4] -->
There are also some researches on the impact of international crises on SDGs. Naidoo R, Fisher B discussed the threat of COVID-19 to SDGs and expressed their expectations on the United Na- tions[7]. Mukarram M described socio-economic impacts of COVID-19, which can be mitigated via his methods[8]. Both works have good assessments of the impact of global pandemics. We discuss further based on their researches.

<!-- b000061 | furniture | pages [4] -->
Team # 2300229                                                       page 4 of 25

<!-- b000063 | heading | pages [4] -->
1.3 Our Work

<!-- b000064 | prose | pages [4] -->
Based on the problem analysis, we construct three distinctive models—Relationship Graph Model, Priority Model and Temporal Champagne Model. Then we study the impact from COVID-19 on our models. Finally, we conduct sensitivity to test the robustness of our models. The work we have done is mainly shown in Figure 1.

<!-- b000065 | caption | pages [4] -->
Figure 1 The Framework of Our Work

<!-- b000066 | heading | pages [4] -->
2 Assumptions and Justifications

<!-- b000067 | prose | pages [4] -->
Through a complete analysis of the problem, in order to make our model more practical and rea- sonable, we make the following reasonable assumptions.

<!-- b000068 | prose | pages [4] -->
Assumption 1: All data from the datasets are authentic.

<!-- b000069 | prose | pages [4] -->
It is meaningless to study fake datasets. We believe the datasets we get are authentic and accurate. No malicious modification has ever occurred.

<!-- b000070 | prose | pages [4] -->
Assumption 2: The completion difficulties of all 17 SDGs are the same.

<!-- b000071 | prose | pages [4] -->
Since it is hard to measure the completion difficulty of each goal and no specific data describing difficulties are found, we assume completion difficulties of them are all the same.

<!-- b000072 | furniture | pages [5] -->
Team # 2300229                                                       page 5 of 25

<!-- b000073 | heading | pages [5] -->
3 Notations

<!-- b000074 | prose | pages [5] -->
The key mathematical notations used in this paper are listed in Table 1.

<!-- b000075 | caption | pages [5] -->
Table 1 Notations Used in This Paper

<!-- b000076 | heading | pages [5] -->
Symbol

<!-- b000077 | prose | pages [5] -->
Definition

<!-- b000078 | prose | pages [5] -->
The undirected relationship graph of 17 SGDs.

<!-- b000079 | prose | pages [5] -->
The betweenness centrality of node .

<!-- b000080 | prose | pages [5] -->
The closeness centrality of node .

<!-- b000081 | prose | pages [5] -->
The eigenvector centrality of node .

<!-- b000082 | prose | pages [5] -->
The score of the ith goal from TOPSIS Model.

<!-- b000083 | prose | pages [5] -->
Change of percentage complete from correlation.

<!-- b000084 | prose | pages [5] -->
Resources allocated to the ith goal.

<!-- b000085 | prose | pages [5] -->
Percentage complete of the ith goal in year .

<!-- b000086 | prose | pages [5] -->
The threat level of the goal .

<!-- b000087 | prose | pages [5] -->
The mitigation or aggravating level of the goal .

<!-- b000088 | prose | pages [5] -->
Note: There are some variables not listed here and will be discussed in detail in each section.

<!-- b000089 | heading | pages [5] -->
4 Relationship Graph Model

<!-- b000090 | prose | pages [5] -->
To reveal the relationships between 17 SDGs, we create a graph based on graph theory. After- wards, we want to measure the importance of each node in the graph, which plays an important role in studying priorities of the 17 goals. Hence, we use three types of centrality measures as the parameters of our graph model, which are commonly used to tell the importance of nodes.

<!-- b000091 | heading | pages [5] -->
4.1 The Data

<!-- b000092 | prose | pages [5] -->
Before the establishment of the model, we get data in need at first. Then we do some preprocessing on the data for better analysis.

<!-- b000093 | heading | pages [5] -->
4.1.1 Data Selection

<!-- b000094 | prose | pages [5] -->
We get our data from the United Nations Global SDG Database[9]. This database owns compre- hensive datasets tracking 17 SDGs. The 17 SDGs each has several targets. Each target also has several indicators. Each indicator consists of many series.

<!-- b000095 | prose | pages [5] -->
In order to make our model more reliable and robust, we make a balance between maximizing the years of samples and the numbers of series. We also have to make sure all the SDGs are covered. Finally, we select 95 series in total. We choose data from Turkey, Mexico and Indonesia, which repre- sent three different continents. Years of the data are from 2003 to 2018.

<!-- b000096 | furniture | pages [6] -->
Team # 2300229                                                       page 6 of 25

<!-- b000097 | heading | pages [6] -->
4.1.2 Data Processing

<!-- b000098 | prose | pages [6] -->
Data Cleaning: Some values are missing from the dataset. We use linear regression to supple- ment the missing values. This method can make use of the information in the original data set as much as possible. Its calculation method is

<!-- b000099 | prose | pages [6] -->
(1)

<!-- b000100 | prose | pages [6] -->
is the supplementary value of the missing item, where is the year of the missing item, and are two parameters. For some values that cannot be negative, we use 0 to supplement the missing . item when Data Normalization: We do normalization to make the data be limited within , so as to reduce the adverse effects caused by the singular sample data. For indicators which are the larger the better, we do normalization in this way:

<!-- b000101 | prose | pages [6] -->
where is the matrix of series of country malization. (2)

<!-- b000102 | prose | pages [6] -->
in period and is the value after nor-

<!-- b000103 | prose | pages [6] -->
For indicators which are the smaller the better, we do normalization in this way:

<!-- b000104 | prose | pages [6] -->
(3)

<!-- b000105 | prose | pages [6] -->
After normalization, we make all indicators the larger the better and restricted to . This makes it more reasonable when calculating correlation of the data.

<!-- b000106 | heading | pages [6] -->
4.2 Graph Construction

<!-- b000107 | prose | pages [6, 7] -->
to denote the undirected relationship graph of 17 goals, where We use is the set is the ith node, which repre- is the weight matrix . of all nodes, is the set of all edges and sents the ith goal. is the undirected edge between node nection between two goals. is the weight of and node , which represents the con- . Based on the structure of the data and the re- quirement of problem 1, we make “goals” directly concerned with “series”. Then we use to de- to denote the vector of the kth series of the ith goal. It note the kth series of the ith goal. We use can be described as consists data from 2003 to 2018. Vector (4)

<!-- b000108 | furniture | pages [7] -->
Team # 2300229                                                       page 7 of 25

<!-- b000110 | prose | pages [7] -->
are the statistic values of the kth series of the ith goal from year 2003 to year where 2018. They are from the datasets we find.

<!-- b000111 | prose | pages [7] -->
We use Spearman’s analysis to construct edges of the graph. This is because compared to Pear- son’s correlation analysis, Spearman’s analysis is better at capturing non-linear correlation and is less to denote the Spearman correlation coefficient between the kth sensible to outliers[10]. We use series of the ith goal and the pth series of the jth goal. Before calculation, we need to convert and into grade vector and (The grade of a number is the position of the number after sorting its vector from small to large). Then we calculate the correlation coefficient. The calculation method of is

<!-- b000112 | prose | pages [7] -->
(5)

<!-- b000113 | prose | pages [7] -->
where and are the mean values of all and , respectively.

<!-- b000114 | prose | pages [7] -->
Connections between series can mainly be divided into three types, which are positive correlation, negative correlation and none correlation. All connections between series of the ith goal and series of the jth goal may not belong to the same type. Hence, we respectively take the three types of connection to measure the connection between the ith goal and the jth goal. into consideration. We use vector The first dimension of vector measures positive correlation. The second dimension of the vector measures negative correlation and the third dimension of the vector measures none correlation. The calculation method of is

<!-- b000115 | prose | pages [7] -->
(6)

<!-- b000116 | prose | pages [7] -->
is the total number of connections between series of the ith goal and series of the jth goal. where If , the edge between node i and node j will be removed. Because the correlation is not reli- able[6].

<!-- b000117 | prose | pages [7] -->
Finally, the weight of edge is calculated by

<!-- b000118 | prose | pages [7, 8] -->
(7) , then the ith goal has a positive correlation with the jth goal. If , then the ith goal has If a negative correlation with the jth goal. The bigger , the stronger the correlation is.

<!-- b000119 | furniture | pages [8] -->
Team # 2300229                                                       page 8 of 25

<!-- b000121 | heading | pages [8] -->
4.3 Graph Measurement based on Graph Theory

<!-- b000122 | prose | pages [8] -->
There are mainly three methods to measure the influence of nodes. Hence parameters of our model come from these three methods, which are Betweenness Centrality, Closeness Centrality and Eigen- vector Centrality. Here we respectively take positive edges and negative edges into consideration. ⚫ Betweenness Centrality Betweenness centrality measures how often a node lies on the path of other nodes[11]. We use to denote the betweenness centrality of the ith node. Its calculation method is

<!-- b000123 | prose | pages [8] -->
(8)

<!-- b000124 | prose | pages [8] -->
where is the number of shortest paths from node to node and is the number of such paths that pass through node . ⚫ Closeness Centrality A node is close to others if the sum of minimal distances from others is small[12]. Closeness centrality is a path-based method of centrality[5]. We use to denote the closeness centrality of the ith node. Its calculation method is

<!-- b000125 | prose | pages [8] -->
(9)

<!-- b000126 | prose | pages [8] -->
where is the minimal distance between node and node . ⚫ Eigenvector Centrality Eigenvector centrality is a common algorithm to measure the importance of a node[13]. It con- siders the number of neighbors and the importance of the neighbors. We use to denote the eigenvector centrality of the ith node. Its calculation method is

<!-- b000127 | prose | pages [8] -->
(10)

<!-- b000128 | prose | pages [8] -->
where is the largest eigenvalue of the adjacency matrix .

<!-- b000129 | heading | pages [8] -->
4.4 Results and Analysis

<!-- b000130 | heading | pages [8] -->
4.4.1 Results and Analysis from the Graph

<!-- b000131 | caption | pages [8] -->
Figure 2 are relationship graphs between 17 goals of three countries. In Figure 2, the red line

<!-- b000132 | prose | pages [8, 9] -->
represents positive correlation, while the blue line represents negative correlation. The thicker the line is, the stronger is the correlation. According to Figure 2, we have some discoveries:

<!-- b000133 | furniture | pages [9] -->
Team # 2300229                                                       page 9 of 25

<!-- b000135 | prose | pages [9] -->
⚫ In general, the majority of the 17 goals have positive correlations with each other. Posi- tive correlations represent synergistic relationship, while negative correlation represent tradeoff relationship. According to the United Nation, the seventeen goals own the same pur- pose, which is to end poverty, protect the planet and ensure prosperity for all. In this way, the 17 goals should have synergistic relationship with each other.

<!-- b000136 | prose | pages [9] -->
⚫ Some negative correlation does exist, which means the two goals are trade-offs. This is mainly because these two goals are competing resources.

<!-- b000137 | prose | pages [9] -->
a) Turkey b) Indonesia c) Mexico

<!-- b000138 | caption | pages [9] -->
Figure 2 Graph of the Relationships between 17 Goals

<!-- b000139 | caption | pages [9] -->
Figure 3 shows the synergies and trade-offs within and between 17 SDGs in Indonesia. The left

<!-- b000140 | prose | pages [9] -->
part shows the synergies and trade-offs within goals. The middle part shows the synergies and trade- offs between goals. The right part shows the color bars and legends of the figure. The lower triangle part of the figure are several pie charts. These pie charts describe the percentage of positive correlations, negative correlations and non-correlations between two goals. This is because each goal has many series. All connections between series of goals may not belong to the same type. The upper triangle part of the figure are weights between two goals. According to Figure 3, we have some discoveries:

<!-- b000141 | prose | pages [9] -->
⚫ Within each goal, positive correlations outweigh negative correlations. The series of each goal are synergies. This means targets set for each goal are reasonable.

<!-- b000142 | prose | pages [9] -->
⚫ Goal 7 has negative correlations with all other goals. Goal 7 is “affordable and clean en- ergy”. The cost of clean energy is much higher than fossil energy. And it needs a lot of in- vestment for technological improvement. It also occupies a lot of human and material re- sources. It makes sense that goal 7 and other goals are trade-offs.

<!-- b000143 | prose | pages [9, 10] -->
Advice for the United Nation. We suggest that the UN should lower the standard of goal 7 for countries like Indonesia, whose synthetic national power is not strong. We also recommend these coun- tries to put goal 7 in low priority. Moreover, it is a good idea to have some developed countries help these countries develop the technologies of affordable and clean energy.

<!-- b000144 | furniture | pages [10] -->
Team # 2300229                                                       page 10 of 25

<!-- b000146 | caption | pages [10] -->
Figure 3 Synergies and Trade-offs within and between Goals

<!-- b000147 | heading | pages [10] -->
4.4.2 Results and Analysis from Graph Parameters

<!-- b000148 | prose | pages [10] -->
Since we respectively take positive edges and negative edges into consideration, we have two kinds of centralities. We use , , to denote betweenness centrality, closeness cen- trality and eigenvector centrality of positive edges, respectively. We use , , to de- note betweenness centrality, closeness centrality and eigenvector centrality of negative edges, respec- tively. Parameters for graph of Mexico is shown in Table 2. Parameters for graph of Indonesia and Turkey are shown in Appendix. According to the table, we find that Goal 3 has the highest value of , and . We preliminarily estimate Goal 3 has the highest priority. Further study on priorities will be conducted in section 5.

<!-- b000149 | caption | pages [10] -->
Table 2 Parameters for Graph of Mexico

<!-- b000150 | prose | pages [10] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8

<!-- b000151 | prose | pages [10] -->
0.000 0.004 0.162 0.004 0.000 0.004 0.000 0.004 0.444 0.556 0.606 0.556 0.333 0.556 0.000 0.556 0.340 0.313 0.340 0.036 0.340 0.000 0.340 0.000

<!-- b000152 | prose | pages [10] -->
0.022 0.196 0.252 0.000 0.000 0.000 0.046 0.000

<!-- b000153 | prose | pages [10] -->
0.520 0.722 0.619 0.464 0.394 0.481 0.481 0.481

<!-- b000154 | prose | pages [10, 11] -->
0.257 0.472 0.294 0.108 0.062 0.209 0.226 0.209 Goal 9 Goal 10 Goal 11 Goal 12 Goal 13 Goal 14 Goal 15 Goal 16 Goal 17

<!-- b000155 | furniture | pages [11] -->
Team # 2300229                                                       page 11 of 25

<!-- b000156 | caption | pages [11] -->
Table 2 Parameters for Graph of Mexico(continued)

<!-- b000158 | prose | pages [11] -->
0.029 0.004 0.000 0.000 0.004 0.000 0.004 0.000 0.000 0.200 0.556 0.000 0.120 0.556 0.333 0.556 0.120 0.120 0.340 0.000 0.000 0.340 0.036 0.340 0.000 0.000 0.340 0.000 0.054 0.491 0.010 0.022 0.000 0.022 0.000 0.000 0.000 0.520 0.813 0.419 0.520 0.000 0.520 0.000 0.464 0.000 0.232 0.510 0.112 0.257 0.000 0.257 0.000 0.108

<!-- b000159 | heading | pages [11] -->
5 Priority Model

<!-- b000160 | prose | pages [11] -->
As Figure 4 shows, based on the results of section 4.4, each goal now has three attributes, which are the three centrality measures of the node. Since we respectively take positive edges and negative edges into consideration, each attribute has 2 indexes. Hence, each goal has 6 indexes. Then we use Entropy Weight Method (EWM) to get the weight of each index. Afterwards, we use weighted TOP- SIS[14] to get scores for all 17 goals. Priorities of the 17 goals are based on these scores. The higher scores, the higher priority.

<!-- b000161 | prose | pages [11] -->
In graph theory, the centrality measure is used to assess the “centrality” status of nodes in a graph. It helps understand the importance and influence of nodes in the graph. In our Relationship Graph Model, a goal with higher centrality means it is more important and owns larger influence. Hence, this goal should have higher priority. After Entropy Weight Method and TOPSIS, we can get a more reliable and comprehensive measure of centrality. Thus, priority based on our model can be effective.

<!-- b000162 | caption | pages [11] -->
Figure 4 Overview of the Priority Model

<!-- b000163 | heading | pages [11] -->
5.1 Establishment of the Model

<!-- b000164 | prose | pages [11] -->
We first do positive management on vector , and due to they are centralities of negative edges.

<!-- b000165 | prose | pages [11, 12] -->
Then, we combine the six indexes of the ith goal into a vector . It can be described as (11)

<!-- b000166 | furniture | pages [12] -->
Team # 2300229                                                       page 12 of 25

<!-- b000168 | prose | pages [12] -->
Afterwards, we combine of all 17 goals into a matrix . Hence, is

<!-- b000169 | prose | pages [12] -->
(12)

<!-- b000170 | heading | pages [12] -->
5.1.1 Sub-Model 1: Weight Entropy Method Model

<!-- b000171 | prose | pages [12] -->
Step1: Normalize the matrix .The standardized formula is

<!-- b000172 | prose | pages [12] -->
(13)

<!-- b000173 | prose | pages [12] -->
Step2: Calculate the proportion of the ith goal in the jth index, which is regarded as the probability used in the calculation of relative entropy later. The calculation method is

<!-- b000174 | prose | pages [12] -->
(14)

<!-- b000175 | prose | pages [12] -->
Step3: Calculate the information entropy and the information utility value of each attribute.

<!-- b000176 | prose | pages [12] -->
For the jth attribute, the formula for calculating its information entropy is

<!-- b000177 | prose | pages [12] -->
(15)

<!-- b000178 | prose | pages [12] -->
For the jth attribute, the calculation method of its information utility value is

<!-- b000179 | prose | pages [12] -->
(16)

<!-- b000180 | prose | pages [12] -->
Step4: Calculate the entropy weight of each attribute. The entropy weight of each attribute is the normalized information utility value. Its calculation method is

<!-- b000181 | prose | pages [12] -->
(17)

<!-- b000182 | heading | pages [12] -->
5.1.2 Sub-Model 2: TOPSIS Model

<!-- b000183 | prose | pages [12] -->
Step1: Standardize the matrix to eliminate the influence of different index dimensions. The normalized matrix is denoted as and each element in is

<!-- b000184 | prose | pages [12] -->
(18)

<!-- b000185 | prose | pages [12, 13] -->
And the standardized matrix is (19)

<!-- b000186 | furniture | pages [13] -->
Team # 2300229                                                       page 13 of 25

<!-- b000188 | prose | pages [13] -->
Step2: Define the optimal vector and the worst vector. We use to denote the optimal vector and use to denote the worst vector. Hence, is (20) And is (21) Step3: Calculate the weighted Euclidean distance between the indexes of goals and the optimal vector:

<!-- b000189 | prose | pages [13] -->
(22)

<!-- b000190 | prose | pages [13] -->
Step4: Calculate the weighted Euclidean distance between the indexes of goals and the worst vector:

<!-- b000191 | prose | pages [13] -->
(23)

<!-- b000192 | prose | pages [13] -->
Step5: Calculate the scores of goals:

<!-- b000193 | prose | pages [13] -->
(24)

<!-- b000194 | prose | pages [13] -->
The priority of each goal is ordered by the score from TOPSIS Model. The higher score , the higher priority.

<!-- b000195 | heading | pages [13] -->
5.2 Results and Analysis

<!-- b000196 | caption | pages [13] -->
Figure 5 shows priorities of the 17 goals of the three countries. For Turkey, priorities of Goal 17

<!-- b000197 | prose | pages [13] -->
and Goal 9 outweigh priorities of others. For Indonesia and Mexico, the priority of Goal 3 is largely higher than other goals. Differences of priorities are mainly due to different situations of each country.

<!-- b000198 | caption | pages [13] -->
Figure 5 Radar Map of the Normalization TOPSIS Scores

<!-- b000199 | furniture | pages [14] -->
Team # 2300229                                                       page 14 of 25

<!-- b000200 | prose | pages [14] -->
Results presented in Table 3 shows the top five priority goals of the three countries. We have some discoveries from the table. We find that Goal 3 and Goal 4 are in the top5 lists of all countries. Goal 3 is about health, while goal 4 is about education. In reality, health and education are great concerns of all countries. They are closely related to the economic and social development of a country. They have important impacts on the welfare of the people and the long-term development of the country.

<!-- b000201 | caption | pages [14] -->
Table 3 Top 5 priority goals

<!-- b000202 | prose | pages [14] -->
Turkey Indonesia Mexico

<!-- b000203 | prose | pages [14] -->
Goal Score Goal Score Goal Score

<!-- b000204 | prose | pages [14] -->
17 0.160 3 0.275 3 0.250 9 0.156 9 0.137 10 0.061 7 0.094 6 0.053 4 0.060 3 0.088 10 0.046 6 0.060 4 0.050 4 0.046 8 0.058

<!-- b000205 | prose | pages [14] -->
Advice for the United Nation: Generally, Goal 3 and Goal 4 are high priority goals of all coun- tries, which are about health and education respectively. We suggest the United Nation organize some cooperation plans on health and education. With concerted efforts from all of us, we can accomplish the health and education goal more efficiently and effectively. Besides, priorities of goals differ from country to country. Hence, we suggest the United Nation offer more free choice to countries. We think it a good idea to enable the country to decide priorities on their own.

<!-- b000206 | heading | pages [14] -->
6 Temporal Champagne Tower Model for Future Development

<!-- b000207 | prose | pages [14] -->
When we pour champagne for a tower which is composed of wine cups, only when the upper cup is filled, the lower cup can get champagne. This phenomenon inspires us to propose Temporal Cham- pagne Tower Model.

<!-- b000208 | prose | pages [14] -->
We want to measure completion status of the 17 goals. We use Temporal Champagne Tower Model to measure the completion status of the 17 goals if they are in the priority order we set. The model is based on Assumption 2, which is the completion difficulties of all 17 SDGs are the same. This means one percent completion of Goal i equals that of Goal j.

<!-- b000209 | prose | pages [14, 15] -->
As Figure 6 shows, since our priorities are initiated, all the resources will be allocated to the top priority goal. Supposing we have 4 goals in total. The priorities of the 4 goals are Goal1>Goal2>Goal3>Goal4, as the shade of green color shows. Goal 1 is correlated to Goal 2. Goal 3 is correlated to Goal 2 and Goal 4. Of course, each goal is correlated to itself. In year , Goal 1 will be allocated all resources, as the dark blue arrow shows. Goal 2 has synergistic or tradeoff relationships with Goal 1. So, next year ( ), Goal 2 will benefit synergistic resources from Goal1 or it will compete resources with Goal 1, as denoted by orange arrow. Next year ( ), Goal 3 is added to the development queue due to its relationship with Goal 2. We assume Goal 1 is complete this year before all the allocated resources are used up. As shown in light blue arrow, some remaining resources will be allocated to Goal 2, which is just one level lower in priority of Goal 1. Then next year ( ), Goal 1 will be put in complete queue, with no resources allocated. Goal 2 will be allocated all resources, which owns the highest priority among the rest. The mathematical expression of the model will be discussed in the subsection below.

<!-- b000210 | furniture | pages [15] -->
Team # 2300229                                                       page 15 of 25

<!-- b000212 | caption | pages [15] -->
Figure 6 Overview of Temporal Champagne Tower Model

<!-- b000213 | heading | pages [15] -->
6.1 Mathematical Establishment of the Model

<!-- b000214 | prose | pages [15] -->
To measure the completion status of the 17 SDGs, we use to denote the percentage complete of 17 SDGs of year . Hence, we have

<!-- b000215 | prose | pages [15] -->
(25)

<!-- b000216 | prose | pages [15] -->
is the percentage complete of the ith goal of the year where .

<!-- b000217 | prose | pages [15] -->
We use to denote the development queue for the 17 SDGs in year . Since our priority is initiated, we have , where is the priority score of goal from section 5.2. Then some goals are positively or negatively correlated to goals in . We use to represent the set for all these correlated goals. Hence, we have

<!-- b000218 | prose | pages [15] -->
(26)

<!-- b000219 | prose | pages [15] -->
where is the weight between two goals. If , then these two goals are not correlated.

<!-- b000220 | prose | pages [15, 16] -->
Then we update for year to . should include all correlated goals on the basis of . Hence, we have (27) We use to denote total resources allocated for 17 SDGs in each year. Then the allocated re- sources for the ith goal is . We assume total accumulated resources comply a linear relationship with the year. Then total resources for each year is 17 times the slope of the linear regression.

<!-- b000221 | furniture | pages [16] -->
Team # 2300229                                                       page 16 of 25

<!-- b000223 | prose | pages [16] -->
to denote the change of percentage complete of the ith goal in year We use exclusively from the correlation with other goals and itself. Hence, we have

<!-- b000224 | prose | pages [16] -->
(28)

<!-- b000225 | prose | pages [16] -->
where is a constant to measure the efficiency of the correlation impact, is the weight between represents the total resources the jth goal gets in two goals and year. We set equal to 5 inspired by Pareto's principle.

<!-- b000226 | prose | pages [16] -->
We use to denote the resources allocated from to goal in year . Its calculation method is

<!-- b000227 | prose | pages [16] -->
(29)

<!-- b000228 | prose | pages [16] -->
If , this means the goal is already complete at the moment , then we don’t need to allocate resources to it any more. Otherwise, it will be allocated resources which are remaining resources after higher priority goals are allocated.

<!-- b000229 | prose | pages [16] -->
Hence, the percentage complete for goal in year is

<!-- b000230 | prose | pages [16] -->
(30)

<!-- b000231 | heading | pages [16] -->
6.2 Temporal Champagne Tower Model

<!-- b000232 | prose | pages [16] -->
Based on the above analysis, our Temporal Champagne Tower Model can be concluded as:

<!-- b000233 | prose | pages [16] -->
(31)

<!-- b000234 | furniture | pages [17] -->
Team # 2300229                                                       page 17 of 25

<!-- b000235 | heading | pages [17] -->
6.3 Model Solutions based on Time Series Algorithms

<!-- b000236 | prose | pages [17] -->
The algorithm corresponding to Temporal Champagne Tower Model is described as Table 4. Via the algorithm, we can predict the percentage complete of each goal in the next 10 years.

<!-- b000237 | caption | pages [17] -->
Table 4 The Algorithm corresponding to the Model

<!-- b000238 | heading | pages [17] -->
Algorithm: Solutions of Cooperation Strategy Model

<!-- b000239 | prose | pages [17] -->
Input: , ,

<!-- b000240 | prose | pages [17] -->
Output:

<!-- b000241 | prose | pages [17] -->
1: for

<!-- b000242 | prose | pages [17] -->
2:   Initialize ,

<!-- b000243 | prose | pages [17] -->
3: Initialize

<!-- b000244 | prose | pages [17] -->
4: for

<!-- b000245 | prose | pages [17] -->
5:   for

<!-- b000246 | prose | pages [17] -->
6:     Update via equation (28)

<!-- b000247 | prose | pages [17] -->
7:     Update via equation (29)

<!-- b000248 | prose | pages [17] -->
8:     Update via equation (30)

<!-- b000249 | prose | pages [17] -->
9:   end

<!-- b000250 | prose | pages [17] -->
10:   Update via equation (26)

<!-- b000251 | prose | pages [17] -->
11:   if

<!-- b000252 | prose | pages [17] -->
12:     Update via equation (27)

<!-- b000253 | prose | pages [17] -->
13:   end

<!-- b000254 | prose | pages [17] -->
14: end

<!-- b000255 | heading | pages [17] -->
6.4 One Goal Being Achieved

<!-- b000256 | prose | pages [17, 18] -->
As Figure 7 shows, we assume Goal 3 is achieved in year . Then Goal 3 will be put in complete queue, as the bubble in the figure shows. No change on priorities will occur to goals which are not complete. This is because determination of priority is based on solid analysis on data from a long period of time. We think it inappropriate to change the priority due to some unexpected events. There- fore, in year , the resources will be allocated to Goal 1, which owns the highest priority in develop- ment list. Some goals may compete resources with Goal 3. Therefore, Goal 3 may back to uncomplete status. This is quite common in our daily life. A farmer may get rid of poverty last year, but return to poverty next year, due to some factors like bad weather, etc. So, Goal 3 returns to development list, but now it owns the highest priority. This is because, although back to uncomplete, Goal 3 is still very close to complete status. Hence, it is reasonable to set Goal 3 the highest priority. After being allocated, there will be some remaining resources, as the light blue arrow shows. The remaining resources can be allocated to Goal 1, which has the highest priority among the rest. It can also be allocated to other goals which are close related to Goal 3 and should be added to SGDs. As for multiple complete goals, the priorities among them are sorted according to the priority orders obtained by the Priority Model. Priority of any complete goal is greater than uncomplete ones.

<!-- b000257 | furniture | pages [18] -->
Team # 2300229                                                       page 18 of 25

<!-- b000259 | caption | pages [18] -->
Figure 7 Overview of Temporal Champagne Tower Model When a Goal Achieved

<!-- b000260 | heading | pages [18] -->
6.5 Results and Analysis

<!-- b000261 | prose | pages [18] -->
To do simulation, we get some data from an authoritative website[15]. Since, each country has a different situation, we choose Indonesia as an example. As shown in Table 5, by 2033, Indonesia can achieve Goal 3, Goal 4, Goal6, Goal 9 and Goal 13. The first 4 goals are generally about people’s livelihood. The fifth achieved goal is about the climate. In total, Indonesia achieves 13% of increase of overall goals within the 10 years.

<!-- b000262 | caption | pages [18] -->
Figure 8.a shows the percentage complete of each goal change over time. From 2025 to 2026,

<!-- b000263 | prose | pages [18, 19] -->
Goal 3 is achieved, and the remaining resources are allocated to Goal 9. Hence, we can notice a huge leap of Goal 9 between 2025 and 2026, as the orange line shows. Afterwards, the structure of network in Temporal Champagne Tower Model is changed. Goals which are positively correlated to Goal 9 increase faster. This impact comes from the achievement of Goal 3. Similar impacts occur when other goals are achieved. Considering that when a goal has been completed, although it can’t exceed 100%, its correlation benefits can affect other counties. Therefore, we propose Goal 18: International Coop- eration. Help other countries achieve their goals with the correlation benefits of complete goals. For example, since Goal 3 is achieved, we emphasize international cooperation on health.

<!-- b000264 | furniture | pages [19] -->
Team # 2300229                                                       page 19 of 25

<!-- b000266 | prose | pages [19] -->
As shown in Figure 8.b, the orange line shows the change of percentage complete for overall goal from Temporal Champagne Tower Model. The blue line shows the result of linear regression and its prediction. By 2033, Indonesia can achieve 82 percent of SDGs, according to our model. However, it can achieve 78 percent of SDGs, according to its current plan. Therefore, our model can enable Indo- nesia to achieve 4 more percent of SDGs, which shows the superiority of our model.

<!-- b000267 | heading | pages [19] -->
Advice for the United Nation: Temporal Champagne Tower Model enables Indonesia achieve

<!-- b000268 | prose | pages [19] -->
82% of SDGs by 2033, which is 4% higher than the predicted result of its current plan. We would appreciate it if the United Nation could recommend our model to other countries. Our model can pro- mote the speed of SDG development. In addition, Goal 7, Goal 11 and Goal 17 are less than 60% complete by 2033. The cost of achieving these goals is too high for countries like Indonesia. Hence, we suggest the United Nation lower the standard on these three goals for countries like Indonesia. We also recommend the United Nation appeal some developed countries offering some help to these coun- tries.

<!-- b000269 | prose | pages [19] -->
a) Predictions for 17 Goals b) Predictions for Total Goals

<!-- b000270 | caption | pages [19] -->
Figure 8 Predictions for Next 10 Years

<!-- b000271 | caption | pages [19] -->
Table 5 Percentage Complete Comparison

<!-- b000272 | prose | pages [19] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8

<!-- b000273 | prose | pages [19] -->
2022/2033 81/96 66/78 66/100 93/100 64/81 70/100 73/54 73/91

<!-- b000274 | caption | pages [19] -->
Table 5 Percentage Complete Comparison(continued)

<!-- b000275 | prose | pages [19] -->
Goal 9 Goal10 Goal11 Goal12 Goal13 Goal14 Goal15 Goal16 Goal17 Total

<!-- b000276 | prose | pages [19] -->
44/100 56/81 71/57 93/76 93/100 65/82 51/66 71/72 51/59 69/82

<!-- b000277 | heading | pages [19] -->
7 Analysis on the Impacts

<!-- b000278 | heading | pages [19] -->
7.1 COVID-19 Impact on Models

<!-- b000279 | prose | pages [19, 20] -->
Impacts of COVID-19 are complicated. Some goals are threatened by the epidemic. Some goals may mitigate or aggravate its impacts. Based on the study of Robin Naidoo[7], we get some adjustment to our model. We use coefficient to measure the threat level of the goal . If one goal is threatened, its allocated resources will be affected. Hence, we update equation (29) into

<!-- b000280 | furniture | pages [20] -->
Team # 2300229                                                       page 20 of 25

<!-- b000282 | prose | pages [20] -->
(32)

<!-- b000283 | prose | pages [20] -->
Some goals may mitigate or aggravate the impact of COVID-19, which means their priority may be changed. We use parameter to measure the mitigation or aggravating level of the goal . Then we update equation (11) to

<!-- b000284 | prose | pages [20] -->
(33)

<!-- b000285 | prose | pages [20] -->
After the adjustment, we rerun Priority Model and Temporal Champagne Tower Model to study the impact of COVID-19.

<!-- b000286 | heading | pages [20] -->
7.2 Results and Analysis

<!-- b000287 | prose | pages [20] -->
As shown in Table 6, by 2033, Indonesia can achieve Goal 3, Goal 4 and Goal 9. Two goals were missed compared to previous result without the effect of COVID-19. In total, Indonesia achieves 9 percent of increase of overall goals within the 10 years, which is 4 percent less than previous result.

<!-- b000288 | caption | pages [20] -->
Figure 9.a shows the percentage complete of each goal change over time. Compared to Figure 8.a,

<!-- b000289 | prose | pages [20] -->
all goals are achieved later due to the effects of COVID-19.

<!-- b000290 | prose | pages [20] -->
As shown in Figure 9.b, the orange line shows the change of percentage complete without the effect of COVID-19. The green line shows the change with the effect of COVID-19. The blue line shows the result of linear regression and its prediction. By 2033, Indonesia can achieve 82 percent of SDGs without the effect of COVID-19. However, it can only achieve 78 percent of SDGs with the effect. The speed of SDG development also becomes lower after the epidemic.

<!-- b000291 | caption | pages [20] -->
Figure 9 Predictions for Next 10 Years Affected by COVID-19

<!-- b000292 | furniture | pages [21] -->
Team # 2300229                                                       page 21 of 25

<!-- b000293 | caption | pages [21] -->
Table 6 Percentage Complete Comparison on the Effect of COVID-19

<!-- b000294 | prose | pages [21] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8

<!-- b000295 | prose | pages [21] -->
Without/With 96/91 78/70 100/100 100/100 81/77 100/77 54/60 91/83

<!-- b000296 | caption | pages [21] -->
Table 6 Percentage Complete Comparison on the Effect of COVID-19(continued)

<!-- b000297 | prose | pages [21] -->
Goal 9 Goal10 Goal11 Goal12 Goal13 Goal14 Goal15 Goal16 Goal17 Total

<!-- b000298 | prose | pages [21] -->
100/100 81/69 57/60 76/80 100/98 82/78 66/60 72/72 59/57 82/78

<!-- b000299 | prose | pages [21] -->
Advice for the United Nation: Unexpected events like COVID-19 have huge impacts on the speed of SDG development. Hence, we recommend the United Nation prolong the deadline for the achievement of SDGs appropriately. Besides, priorities of some goals may also be affected. This means the United Nation may need to adjust the focus of their work. Some plans are recommended to made which could alleviate the impact of these unexpected events.

<!-- b000300 | heading | pages [21] -->
7.3 Model Impact on Companies and Organizations

<!-- b000301 | prose | pages [21] -->
The sustainable development framework including 17 SDGs can provide guiding directions and even strategies for companies or organizations. Our previous work is based on country-level data. Different strategies are needed for different sizes of companies or organizations. The total amount of social resources that a company or organization can provide is often smaller than those of a country. Companies or organizations need to consider the priorities of different goals more carefully.

<!-- b000302 | prose | pages [21] -->
The first thing to point out is that the higher the priority of the goal at the national level, the greater the demand and the investment for the goal. Therefore, smaller companies or organizations can derive enterprise- or organization-level priorities based on their own business or positioning, combined with country-level priorities obtained from our network. Companies or organizations that use this priority to guide their development may more easily obtain investment or donations to maintain a long-term sustainable development.

<!-- b000303 | prose | pages [21] -->
For larger companies or organizations, they have easier access to investment or donations than smaller ones. So, they can consider multiple priorities or synergies between multiple goals within the global common framework provided by the SDGs. Synergies between multiple SDG goals can be obtained through our Priority Model. If a company or organization needs a longer-term perspective, it can use our Temporal Champagne Tower Model with some data to adjust the priority of its goals.

<!-- b000304 | prose | pages [21] -->
It is worth noting that our model will reflect the impact of certain international crises, such as COVID-19, which requires companies or organizations to adapt to the times and focus on the selected SDG goals.

<!-- b000305 | prose | pages [21] -->
The usage of our models for companies or organizations can be concluded as Figure 10.

<!-- b000306 | furniture | pages [22] -->
Team # 2300229                                                       page 22 of 25

<!-- b000307 | caption | pages [22] -->
Figure 10 How Companies or Organizations Use Our Model

<!-- b000308 | heading | pages [22] -->
8 Sensitivity Analysis

<!-- b000309 | prose | pages [22] -->
In order to evaluate the sensitivity and robustness of the Temporal Champagne Tower Model, we perform two sensitivity tests on the hyperparameters and in the Temporal Champagne Tower Model, respectively. 𝐶 is a constant to measure the efficiency of the synergy and 𝐷 denotes total resources allocated for 17 SDGs in each year.

<!-- b000310 | prose | pages [22] -->
In Section 6, we performed a linear regression on Indonesia's overall score from 2012 to 2022 with year as the independent variable and the overall score as the dependent variable. Here we do the same for Turkey and Mexico. The 𝑅2 and p-values of the linear regression for Turkey and Mexico are 0.767, 4.13 × 10−4 and 0.882, 1.78 × 10−5, respectively, which demonstrates the validity of the linear regression.

<!-- b000311 | prose | pages [22] -->
The 95% confidence intervals for the value of 𝐷 are determined for the two countries separately by linear regression. We choose the 17 times of midpoint of the interval as an estimate of 𝐷 and obtain 𝐷 of 0.036 and 0.071 for Turkey and Mexico, respectively. In section 6, we have determined that D for Indonesia is 0.102.

<!-- b000312 | prose | pages [22] -->
When performing the sensitivity test on 𝐶, we traverse the values of 𝐶 from 4 to 6 with a step size of 0.1, and run the Temporal Champagne Tower Model separately for each value of C. We show the results in Figure 11.a. The intersection of the two red dotted lines in the figure represents our 𝐶 value and the final overall score in Section 6.

<!-- b000313 | prose | pages [22] -->
When conducting the sensitivity test on 𝐷, we fix 𝐶 to 5, traverse the value of 𝐷 from 0.102 to 0.136 with a step size of 1.62 × 10−3, and display the results in Figure 11.b. The intersection of the two red dotted lines in the figure represents our 𝐷 value and the final result in Section 6.

<!-- b000314 | prose | pages [22, 23] -->
From the result of sensitivity analysis for 𝐶, we can see that the change trends of the three lines are relatively flat. The difference between the maximum and minimum overall score for Indonesia, Turkey, and Mexico is 0.041, 0.007, and 0.006, respectively.

<!-- b000315 | furniture | pages [23] -->
Team # 2300229                                                       page 23 of 25

<!-- b000317 | prose | pages [23] -->
From Figure 11.b, we can see that the change in overall score caused by the change of 𝐷 is very small. The difference between the maximum and minimum overall score for Indonesia is 0.028.

<!-- b000318 | prose | pages [23] -->
The above analysis shows that our Temporal Champagne Tower Model is insensitive to both hy- perparameters and , and thus is robust.

<!-- b000319 | prose | pages [23] -->
a) Result of Sensitivity Analysis for b) Result of Sensitivity Analysis for

<!-- b000320 | caption | pages [23] -->
Figure 11 Results of Sensitivity Analysis for C and D

<!-- b000321 | heading | pages [23] -->
9 Model Evaluation and Further Discussion

<!-- b000322 | heading | pages [23] -->
9.1 Strengths of the Model

<!-- b000323 | prose | pages [23] -->
⚫ Comprehensiveness In Relationship Graph Model and Priority Model, we considered both positive and negative correlation effects. In Temporal Champagne Tower Model, we discussed as many factors as possible, including the proposal of new goals and the consolidation of completed goals.

<!-- b000324 | prose | pages [23] -->
⚫ Robustness Our model can get reasonable results for different countries with different constant.

<!-- b000325 | prose | pages [23] -->
⚫ Innovation We are inspired by Champagne Tower and build our TCTM based on temporal network.

<!-- b000326 | prose | pages [23] -->
Through the results of the simulation, our model explains the requirements well and puts forward more meaningful suggestions.

<!-- b000327 | heading | pages [23] -->
9.2 Weaknesses of the Model

<!-- b000328 | prose | pages [23] -->
⚫ Hyperparameters are difficult to estimate In Section 7, we estimated the hyperparameters in the modified TCTM using expert data from a paper in Nature (we corrected the TCTM to reflect the impact of the pandemic). How- ever, such expert data is not readily available, so the hyperparameters of our modified model are also difficult to estimate.

<!-- b000329 | furniture | pages [24] -->
Team # 2300229                                                       page 24 of 25

<!-- b000330 | heading | pages [24] -->
References

<!-- b000331 | references | pages [24] -->
[1]. G. H. Brundtland, “World commission on environment and development,” Environmental

<!-- b000332 | references | pages [24] -->
policy and law, vol. 14, no. 1, pp. 26–30, 1985.

<!-- b000333 | references | pages [24] -->
[2]. Wu J, Guo S, Huang H, et al. Information and communications technologies for sustainable

<!-- b000334 | references | pages [24] -->
development goals: state-of-the-art, needs and perspectives[J]. IEEE Communications Sur-

<!-- b000335 | references | pages [24] -->
veys & Tutorials, 2018, 20(3): 2389-2406.

<!-- b000336 | references | pages [24] -->
[3]. “Transforming our world: the 2030 agenda for sustainable development,” UN General As-

<!-- b000337 | references | pages [24] -->
sembly, New York: United Nations, 2015.

<!-- b000338 | references | pages [24] -->
[4]. Le Blanc D. Towards integration at last? The sustainable development goals as a network of

<!-- b000339 | references | pages [24] -->
targets[J]. Sustainable Development, 2015, 23(3): 176-187.

<!-- b000340 | references | pages [24] -->
[5]. Swain R B, Ranganathan S. Modeling interlinkages between sustainable development goals

<!-- b000341 | references | pages [24] -->
using network analysis[J]. World Development, 2021, 138: 105136.

<!-- b000342 | references | pages [24] -->
[6]. Pradhan P, Costa L, Rybski D, et al. A systematic study of sustainable development goal (SDG)

<!-- b000343 | references | pages [24] -->
interactions[J]. Earth's Future, 2017, 5(11): 1169-1179.

<!-- b000344 | references | pages [24] -->
[7]. Naidoo R, Fisher B. Reset sustainable development goals for a pandemic world[J]. Nature,

<!-- b000345 | references | pages [24] -->
2020, 583(7815): 198-201.

<!-- b000346 | references | pages [24] -->
[8]. Mukarram M. Impact of COVID-19 on the UN sustainable development goals (SDGs)[J].

<!-- b000347 | references | pages [24] -->
Strategic Analysis, 2020, 44(3): 253-258.

<!-- b000348 | references | pages [24] -->
[9]. United Nations Statistics Division, United Nations Global SDG Database, 2016. https://un-

<!-- b000349 | references | pages [24] -->
stats.un.org/sdgs/indicators/database.

<!-- b000350 | references | pages [24] -->
[10]. Hauke J, Kossowski T. Comparison of values of Pearson's and Spearman's correlation coeffi-

<!-- b000351 | references | pages [24] -->
cients on the same sets of data[J]. Quaestiones geographicae, 2011, 30(2): 87-93.

<!-- b000352 | references | pages [24] -->
[11]. Freeman L. A Set of measures of centrality based on betweenness. Sociometry,1977,40(1):35-

<!-- b000353 | references | pages [24] -->
41.

<!-- b000354 | references | pages [24] -->
[12]. Sabidussi G. The centrality index of a graph. Psychometrika, 1966, 31(4): 581-603

<!-- b000355 | references | pages [24] -->
[13]. Bonacich P. Power and centrality: A family of measures. American Journal of Sociology, 1987,

<!-- b000356 | references | pages [24] -->
92(5): 1170-1182.

<!-- b000357 | references | pages [24] -->
[14]. Hwang C L, Yoon K, Hwang C L, et al. Methods for multiple attribute decision making[J].

<!-- b000358 | references | pages [24] -->
Multiple attribute decision making: methods and applications a state-of-the-art survey, 1981:

<!-- b000359 | references | pages [24] -->
58-191.

<!-- b000360 | references | pages [24] -->
[15]. https://dashboards.sdgindex.org.

<!-- b000361 | furniture | pages [25] -->
Team # 2300229                                                       page 25 of 25

<!-- b000362 | heading | pages [25] -->
Appendix

<!-- b000363 | caption | pages [25] -->
Table 7 Parameters for Graph of Indonesia

<!-- b000364 | prose | pages [25] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8 0.001 0.001 0.237 0.001 0.000 0.001 0.000 0.001 0.754 0.754 0.929 0.754 0.503 0.754 0.000 0.754 0.303 0.303 0.316 0.303 0.058 0.303 0.000 0.303

<!-- b000365 | prose | pages [25] -->
0.000 0.000 0.144 0.000 0.000 0.000 0.914 0.000

<!-- b000366 | prose | pages [25] -->
0.480 0.480 0.571 0.480 0.000 0.000 0.857 0.480

<!-- b000367 | prose | pages [25] -->
0.197 0.197 0.308 0.197 0.000 0.000 0.657 0.197

<!-- b000368 | caption | pages [25] -->
Table 8 Parameters for Graph of Indonesia(continued)

<!-- b000369 | prose | pages [25] -->
Goal 9 Goal 10 Goal 11 Goal 12 Goal 13 Goal 14 Goal 15 Goal 16 Goal 17

<!-- b000370 | prose | pages [25] -->
0.106 0.001 0.000 0.000 0.000 0.000 0.001 0.000 0.000 0.862 0.754 0.000 0.000 0.710 0.503 0.754 0.483 0.710 0.313 0.303 0.000 0.000 0.277 0.058 0.303 0.029 0.277 0.005 0.144 0.000 0.005 0.000 0.000 0.000 0.000 0.000 0.400 0.571 0.480 0.400 0.480 0.000 0.480 0.000 0.480 0.185 0.308 0.197 0.185 0.197 0.000 0.197 0.000 0.197

<!-- b000371 | caption | pages [25] -->
Table 9 Parameters for Graph of Turkey

<!-- b000372 | prose | pages [25] -->
Goal 1 Goal 2 Goal 3 Goal 4 Goal 5 Goal 6 Goal 7 Goal 8 0.000 0.000 0.104 0.000 0.000 0.000 0.132 0.000 0.635 0.310 0.710 0.635 0.431 0.635 0.447 0.635 0.326 0.005 0.343 0.326 0.038 0.326 0.041 0.326

<!-- b000373 | prose | pages [25] -->
0.022 0.196 0.252 0.000 0.000 0.000 0.046 0.000

<!-- b000374 | prose | pages [25] -->
0.520 0.722 0.619 0.464 0.394 0.481 0.481 0.481

<!-- b000375 | prose | pages [25] -->
0.257 0.472 0.294 0.108 0.062 0.209 0.226 0.209

<!-- b000376 | caption | pages [25] -->
Table 10 Parameters for Graph of Turkey(continued)

<!-- b000377 | prose | pages [25] -->
Goal 9 Goal 10 Goal 11 Goal 12 Goal 13 Goal 14 Goal 15 Goal 16 Goal 17

<!-- b000378 | prose | pages [25] -->
0.236 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.242 0.754 0.000 0.447 0.000 0.635 0.000 0.635 0.447 0.710 0.347 0.000 0.076 0.000 0.326 0.000 0.326 0.076 0.331 0.000 0.054 0.491 0.010 0.022 0.000 0.022 0.000 0.000 0.000 0.520 0.813 0.419 0.520 0.000 0.520 0.000 0.464 0.000 0.232 0.510 0.112 0.257 0.000 0.257 0.000 0.108
