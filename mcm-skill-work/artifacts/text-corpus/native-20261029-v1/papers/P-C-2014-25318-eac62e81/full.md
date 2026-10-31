# P-C-2014-25318-eac62e81

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
25318

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T2 ________________

<!-- b000008 | prose | pages [1] -->
F1 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | title | pages [1] -->
C

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | prose | pages [1] -->
F4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | prose | pages [1] -->
2014 Mathematical Contest in Modeling (MCM/ICM) Summary Sheet

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | prose | pages [1] -->
Who are the 20%?

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | prose | pages [1] -->
The famous ‘80-20’ rule states that the 80% influence is caused by the 20% for many events. This principle also applies to the network science: only few nodes have a significant influence and impact to the whole network. In our paper, A Relation Distance Model and an Authority-Popularity Evaluation Model are employed to measure of the 20% and analysis of its influence.

<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | prose | pages [1] -->
For requirement 1 & 2, we construct the undirected co-author network based on the 511 order relationship matrix. A Relation Distance Model is proposed on the basis of SNA technique. It combines three centrality indexes as a measure vector to calculate the ‘distance’ with the most influential node. Another measure (Eigenvector centrality) which takes both degree and the influence of co-authors into consideration outputs a new rank. Validation of the model is discussed by comparing the two ranking of the top 15 authors in Erdos1 network, we find ALON, NOGA M. is the most influential person in the Erdos1 network. The degree distribution of the Erdos1 network is proved to approximately be power-law distribution, which indicates it is a scale-free network.

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | prose | pages [1] -->
For requirement 3, an Authority-Popularity Evaluation Model is established to analyze the depth and the width of the influence of nodes. An Authority Index is calculated by our Modified PageRank Algorithm (including two steps: initialization and iteration) to measure the depth of impact. A Popularity Index is defined as citation per year to reflect the width of influence. A set of 24 papers citation directed network with weight added to nodes is constructed to implement the algorithm. The final ranking of the papers is obtained by combining Authority-Popularity Indexes. For requirement 4, a set of 15 actors’ co-star bidirectional network with co-star movie as links is constructed. The iteration process is refined as the weight added to links instead of nodes.

<!-- b000030 | furniture | pages [1] -->


<!-- b000031 | prose | pages [1] -->
For requirement 5, we discuss two characteristics of scale-free network: Growth and Preferential attachment. The philosophy of dynamics of scale-free network is revealed as the 'Matthew effect'. The prior method to boost influence is proposed: finding the shortest links to the most influential author. Cooperating with the 80% (more approachable relatively) with low closeness centrality step by step and finally co-author with the key figure in the field.

<!-- b000032 | furniture | pages [1] -->


<!-- b000033 | prose | pages [1] -->
A sensitivity analysis is conducted to study the robustness of our algorithm to Damp Coefficient and the result shows a good stability.  Strength and weakness of our models is also discussed.

<!-- b000034 | furniture | pages [1] -->


<!-- b000035 | furniture | pages [2] -->
Team # 25318

<!-- b000036 | furniture | pages [2] -->
Page 1 of 20

<!-- b000037 | prose | pages [2] -->
Who are the 20% ?

<!-- b000038 | prose | pages [2] -->
1.

<!-- b000039 | heading | pages [2] -->
Introduction

<!-- b000040 | prose | pages [2] -->
In this paper, we will introduce two proper methods to analyze inﬂuence and impact in research networks and other areas of society.

<!-- b000041 | prose | pages [2] -->
The Relation Distance Model is proposed based on SNA technique. It is a combination of three centrality indexes. Another measure (Eigenvector central- ity) which takes both degree and the inﬂuence of co-authors into consideration outputs a new rank. Validation of the model is discussed by comparing the two ranking of the top 15 authors in Erdos1 network.

<!-- b000042 | prose | pages [2] -->
The Authority-Popularity Evaluation Model is established in section 5 to an- alyze the depth and the width of the inﬂuence of important nodes. The Authori- ty Index reﬂects the depth of impact and the Popularity Index reﬂects the width of inﬂuence. A set of 24 papers citation network with weight is constructed to implement the algorithm and the results are discussed. In order to analyze a co- star network for Requirement 4 , a reﬁnement to the model based on Modiﬁed PageRank Algorithm is proposed in subsection 5.3.

<!-- b000043 | prose | pages [2] -->
The philosophy of the scale-free network is revealed and the shortcut to boost inﬂuence based on our model is proposed in section 6.

<!-- b000044 | prose | pages [2] -->
2.

<!-- b000045 | heading | pages [2] -->
Basic Assumptions

<!-- b000046 | prose | pages [2] -->
In this section, we discuss several assumptions we have made and rationale for making these assumptions.

<!-- b000047 | heading | pages [2] -->
Assumption 1. We assume that the strength of co-authorship between two

<!-- b000048 | prose | pages [2] -->
arbitrary Erdos1 authors is the same.

<!-- b000049 | prose | pages [2] -->
We believe that the accurate strength level of co-authorship between two ar- bitrary Erdos1 authors is hard to be measured by some criterion. For the sake of simpliﬁcation, in our case, if two authors co-author a paper , then the co- authorship index is ’1’, if not , it is ’0’.

<!-- b000050 | prose | pages [2] -->
Assumption 2. We assume that the signiﬁcance of a research paper is deter- mined by both its citations and publishing date , also, the inﬂuence of the journal should be considered.

<!-- b000051 | furniture | pages [3] -->
Team # 25318

<!-- b000052 | furniture | pages [3] -->
Page 2 of 20

<!-- b000053 | prose | pages [3] -->
We believe that the more often a paper is cited or the earlier a paper is pub- lished, the more inﬂuential it is. And also, a high inﬂuential journal contributes more to the inﬂuence of a paper.

<!-- b000054 | prose | pages [3] -->
Assumption 3. We assume that the quality of a movie is determined by its IMDb rating[1] . The popularity of a movie star is measured by the number of Google search results.

<!-- b000055 | prose | pages [3] -->
3.

<!-- b000056 | prose | pages [3] -->
Deﬁnitions

<!-- b000057 | prose | pages [3] -->
Deﬁnitions of symbols employed in this paper are listed in Table 1.

<!-- b000058 | caption | pages [3] -->
Table 1: Symbol table.

<!-- b000059 | prose | pages [3] -->
Variable Description

<!-- b000060 | heading | pages [3] -->
Relation Distance Model

<!-- b000061 | prose | pages [3] -->
x The index of member nodes aix Relation strength dix Relation distance Cd(x) The degree centrality of node x Cb(x) The betweenness centrality of nodex Cc(x) The closeness centrality of node x gij(x) The shortest path between two other nodes i and j passes through the nodex lix The length of the shortest path connecting node i and x n The total number of nodes in a network −→ Ax The vector contains the three centrality measures −→ AC The ideal vector of the node which has the most signiﬁcant inﬂuence within the network DC(x) The Euclid distance deﬁned to measure the inﬂuence and impact of node x

<!-- b000062 | prose | pages [3] -->
Eigenvector centrality Ex The eigenvector centrality value of node x B = (bij) Adjacent matrix of a network c Proportional constant

<!-- b000063 | heading | pages [3] -->
Revised PageRank Algorithm

<!-- b000064 | prose | pages [3] -->
PRx(0) Initial PageRank value of node x s Scale constant for the Revised Algorithm Gij The relationship matrix D The coefﬁcient matrix

<!-- b000065 | furniture | pages [4] -->
Team # 25318

<!-- b000066 | furniture | pages [4] -->
Page 3 of 20

<!-- b000067 | prose | pages [4] -->
4.

<!-- b000068 | heading | pages [4] -->
Models for Requirement 1 and 2

<!-- b000069 | prose | pages [4] -->
4.1 Data Preprocessing

<!-- b000070 | prose | pages [4] -->
Before presenting our models, we would like to address the preprocessing work we have done to the data.

<!-- b000071 | prose | pages [4] -->
Step 1. We extract the 511 Erdos1 authors from over 18,000 lines of raw data in Erdos1 ﬁle , which is a easy task by eliminating names without a date followed by in Microsoft Excel 2010.

<!-- b000072 | prose | pages [4] -->
Step 2. In order to obtain the relationship among the 511 Erdos1, we leave out the Erdos2 from the list of co-authors of the 511 Erdos1 by using library function ’countif()’ in Microsoft Excel 2010.

<!-- b000073 | prose | pages [4] -->
Step 3. We construct a 511 order co-authorship matrix by executing a pro- gram in MATLAB@2012b. For the sake of description, we give each Erdos1 au- thor an ID number by the rule:

<!-- b000074 | prose | pages [4] -->
’1’ stands for ABBOTT, HARVEY LESLIE

<!-- b000075 | prose | pages [4] -->
’2’ stands for ACZEL, JANOS D.

<!-- b000076 | prose | pages [4] -->
. . .

<!-- b000077 | prose | pages [4] -->
’511’ stands for ZIV, ABRAHAM

<!-- b000078 | prose | pages [4] -->
4.2

<!-- b000079 | heading | pages [4] -->
Relation Distance Model based on SNA

<!-- b000080 | prose | pages [4] -->
4.2.1 Overview

<!-- b000081 | prose | pages [4] -->
In order to build the Erdos1 network and analyze its properties, the social network analysis (SNA) technique is employed. Social Network Analysis refers to methods used to analyze social networks structures made up of individu- als called ’nodes’, which are tied (connected) by one or more speciﬁc types of interdependency. In our case, the Erdos1 authors are viewed as nodes and co- authorship (obtained from subsection 4.1) as links among them.

<!-- b000082 | furniture | pages [5] -->
Team # 25318

<!-- b000083 | furniture | pages [5] -->
Page 4 of 20

<!-- b000084 | caption | pages [5] -->
Figure 1: The co-author network of the Erdos1. For the sake of observability, we choose the

<!-- b000085 | prose | pages [5] -->
top 50 Erdos1 authors in the priority list in subsection 4.2.2.

<!-- b000086 | prose | pages [5] -->
4.2.2 Methodology

<!-- b000087 | prose | pages [5] -->
In the following, we will ﬁnish the steps to build up and validate the model.

<!-- b000088 | prose | pages [5] -->
Step 1. Calculate the centrality measure vector −→ work.

<!-- b000089 | prose | pages [5] -->
Ax of the nodes in the net-

<!-- b000090 | prose | pages [5] -->
According to Freeman’s research[1979], there are three popular centrality measures- degree centrality Cd(x), betweenness centrality Cb(x) and closeness centrality Cc(x) . What’s more, they can be used to identify ’masters’ who have signiﬁcant inﬂuence or impact in a network. These values are deﬁned as below:

<!-- b000091 | prose | pages [5] -->
Degree centrality is deﬁned as:

<!-- b000092 | prose | pages [5] -->
nP

<!-- b000093 | prose | pages [5] -->
Cd(x) =

<!-- b000094 | prose | pages [5] -->
aix

<!-- b000095 | prose | pages [5] -->
i=1

<!-- b000096 | prose | pages [5] -->
where n is the total number of nodes in a network, and aix is a variable indicat- ing the weighted number of co-authorship between nodes x and i. According to Assumption 1, in our Erdos1 network, aix = 1 or 0 , for all i.

<!-- b000097 | prose | pages [5] -->
Betweenness centrality is deﬁned as:

<!-- b000098 | furniture | pages [6] -->
Team # 25318

<!-- b000099 | prose | pages [6] -->
Cb(x) =

<!-- b000100 | furniture | pages [6] -->
Page 5 of 20

<!-- b000101 | prose | pages [6] -->
nP

<!-- b000102 | prose | pages [6] -->
nP

<!-- b000103 | prose | pages [6] -->
gij(x)

<!-- b000104 | prose | pages [6] -->
x

<!-- b000105 | prose | pages [6] -->
j

<!-- b000106 | prose | pages [6] -->
where gij(x) indicates whether the shortest path between two other nodes i and j passes through the node x.

<!-- b000107 | prose | pages [6] -->
Closeness centrality is deﬁned as:

<!-- b000108 | prose | pages [6] -->
Cc(x) =

<!-- b000109 | prose | pages [6] -->
nP

<!-- b000110 | prose | pages [6] -->
lix

<!-- b000111 | prose | pages [6] -->
i=1

<!-- b000112 | prose | pages [6] -->
where lix is the length of the shortest path connecting nodes i and x. The shortest paths are calculated based on the Floyd algorithm.

<!-- b000113 | prose | pages [6] -->
The centralities above describe different characters of nodes in a network.

<!-- b000114 | prose | pages [6] -->
• Degree centrality shows the number of nodes’ connections, which also re- ﬂects connectivity of nodes in a network. Nodes with high connectivity can be viewed as more inﬂuential.

<!-- b000115 | prose | pages [6] -->
• Betweenness centrality shows the number of the shortest paths that pass- ing by certain node. It also reveals the dependency of a node from other nodes. Obviously, if a node is dependent by other nodes quite much, the node must be very important for the whole network, That is, large be- tweenness centrality value of a node is equivalent to its high importance in the network.

<!-- b000116 | prose | pages [6] -->
• Closeness centrality actually measures how far away one node is from oth- er nodes. Apparently that small closeness value of a node reﬂects its high importance.

<!-- b000117 | prose | pages [6] -->
According to the above, we deﬁne a vector which contains the three measures as the form below:

<!-- b000118 | prose | pages [6] -->
−→ Cd(x) Cb(x) Cc(x) maxCb(x), maxCd(x), Ax = (

<!-- b000119 | prose | pages [6] -->
−→

<!-- b000120 | prose | pages [6] -->
maxCc(x))

<!-- b000121 | prose | pages [6] -->
Ax is called ’measure vector’. It can also be represented in another from below:

<!-- b000122 | prose | pages [6] -->
−→ Ax = (Ax1, Ax2, Ax3)

<!-- b000123 | prose | pages [6] -->
where Axi (i=1,2,3) stands for element i in the vector −→ Ax. The three elements are all divided by their maximum values to be normalized, separately. According to the deﬁnition of three centralities , it is obvious that Ax will get its optimal value when degree(Ax1) and betweenness (Ax2) get to their largest value 1 and closeness (Ax3) gets to its smallest value 0.

<!-- b000124 | furniture | pages [7] -->
Team # 25318

<!-- b000125 | furniture | pages [7] -->
Page 6 of 20

<!-- b000126 | prose | pages [7] -->
Therefore, the ideal model of an author who has the most signiﬁcant inﬂu- ence within the network will have his/her own measure vector −→

<!-- b000127 | prose | pages [7] -->
−→ AC:

<!-- b000128 | prose | pages [7] -->
The ideal vector will be deﬁned as

<!-- b000129 | prose | pages [7] -->
−→ AC = (AC

<!-- b000130 | prose | pages [7] -->
Ax as (1, 1, 0).

<!-- b000131 | prose | pages [7] -->
2 , AC 1 , AC 3 ) = (1, 1, 0)

<!-- b000132 | prose | pages [7] -->
Step 2. Calculate the ’distance’ among the member nodes.

<!-- b000133 | prose | pages [7] -->
The measure vector −→ Ax can be used to calculate the ’distance’ among the member nodes. We deﬁne the Euclid distance of −→

<!-- b000134 | prose | pages [7] -->
−→

<!-- b000135 | prose | pages [7] -->
Ax from the node x to the ideal

<!-- b000136 | prose | pages [7] -->
AC as DC(x). Based on the idea of ranking method from TOPSIS algo-

<!-- b000137 | prose | pages [7] -->
vector

<!-- b000138 | prose | pages [7] -->
rithm [ S. Mahmoodzadeh 2007 ], we call the ’distance’ as Inﬂuence and Impact Distance, which is deﬁned as below:

<!-- b000139 | prose | pages [7] -->
q

<!-- b000140 | prose | pages [7] -->
1 )2 + (Ax2 −AC

<!-- b000141 | prose | pages [7] -->
(Ax1 −AC

<!-- b000142 | prose | pages [7] -->
DC(x) =

<!-- b000143 | prose | pages [7] -->
2 )2 + (Ax3 −AC 3 )2

<!-- b000144 | prose | pages [7] -->
Step 3. Generate the inﬂuence priority list.

<!-- b000145 | prose | pages [7] -->
This distance is the key to determine who in the Erdos1 network has signif- icant inﬂuence within the network. A further distance apparently indicates a lower possibility of being an author who has signiﬁcant inﬂuence. The Erdos1 authors will be arranged into an Inﬂuence and Impact priority list. The order of the list is arranged according to the value of DC(x). Node with smaller DC(x) value will rank higher in the priority list since DC(x) is the distance from the node to an ideal ’most signiﬁcant’ node.

<!-- b000146 | prose | pages [7] -->
4.2.3

<!-- b000147 | heading | pages [7] -->
Results and Analysis

<!-- b000148 | prose | pages [7] -->
The three-dimensional graph is shown in Figure 2 , in which 511 points stand for 511 Erdos1 authors’ measure vectors correspondingly .

<!-- b000149 | prose | pages [7] -->
The top 15 authors of the Inﬂuence and Impact priority list are shown below in Table 2. For the sake of observability, we choose the top 50 Erdos1 authors in the impact priority list to draw the network in UCINET, as is shown in Figure 1.

<!-- b000150 | prose | pages [7] -->
We can see from Table 2 that HARARY, FRANK* has the most signiﬁcant inﬂuence within the co-author network. When it comes to a speciﬁc university, department, or a journal, the relationship matrix data should be collected for the network. The centrality index can be calculated and a ranking can be obtained from our model. Weight of nodes or links may be added if necessary, and we will discuss these network in section 5.

<!-- b000151 | furniture | pages [8] -->
Team # 25318

<!-- b000152 | furniture | pages [8] -->
Page 7 of 20

<!-- b000153 | caption | pages [8] -->
Figure 2: Measure vectors of 511 Erdos1 authors, the big red point(1,1,0) stands for the ideal

<!-- b000154 | prose | pages [8] -->
vector of the most crucial one.

<!-- b000155 | caption | pages [8] -->
Table 2: Top 15 most inﬂuential authors within the Erdos1 network.

<!-- b000156 | prose | pages [8] -->
DC(x) Ranking ID Name of authors

<!-- b000157 | prose | pages [8] -->
1 0.1798 187 HARARY, FRANK* 2 0.2927 438 SOS,VERA TURAN 3 0.2962 10 ALON,NOGA M. 4 0.3400 165 GRAHAM,RONALD LEWIS 5 0.3557 148 FUREDI,ZOLTAN 6 0.3587 44 BOLLOBAS,BELA 7 0.4793 479 TUZA,ZSOLT 8 0.5022 355 POMERANCE,CARL BERNARD 9 0.5259 449 STRAUS,ERNST GABOR* 10 0.5394 341 PACH,JANOS 11 0.5778 180 HAJNAL,ANDRAS 12 0.6531 378 RODL,VOJTECH 13 0.6998 440 SPENCER,JOEL HAROLD 14 0.7440 249 KLEITMAN,DANIEL J. 15 0.7653 399 SARKOZY,ANDRAS

<!-- b000158 | prose | pages [8] -->
Eigenvector centrality

<!-- b000159 | prose | pages [8] -->
For the second question in Requirement 2 ,now we consider who has pub- lished important works or connects important researchers within Erdos1.

<!-- b000160 | prose | pages [8] -->
The importance of a node is both determined by the number of its neighbor nodes (its degree) and the importance of its neighbor nodes.In graph theory and network analysis, centrality of a vertex measures its relative importance within a graph[4].

<!-- b000161 | furniture | pages [9] -->
Team # 25318

<!-- b000162 | furniture | pages [9] -->
Page 8 of 20

<!-- b000163 | prose | pages [9] -->
The deﬁnition of eigenvector centrality is :

<!-- b000164 | prose | pages [9] -->
Ei = c

<!-- b000165 | prose | pages [9] -->
n n X

<!-- b000166 | prose | pages [9] -->
bijEj

<!-- b000167 | prose | pages [9] -->
j=1

<!-- b000168 | prose | pages [9] -->
where c is the proportional constant, B = (bij) is the adjacent matrix of the network.

<!-- b000169 | prose | pages [9] -->
Calculate the 511 nodes’ eigenvector centrality value in UCINET , we get the top 15 nodes as is shown below in Table 3.

<!-- b000170 | caption | pages [9] -->
Table 3: Top 15 connecting important researchers within Erdos1.

<!-- b000171 | prose | pages [9] -->
Name of authors Ranking E value ID

<!-- b000172 | prose | pages [9] -->
ALON, NOGA M. 1 0.26 10 RODL, VOJTECH 2 0.234 378 BOLLOBAS, BELA 3 0.209 44 GRAHAM,RONALD LEWIS 4 0.204 165 FUREDI,ZOLTAN 5 0.201 148 TUZA,ZSOLT 6 0.187 479 SPENCER, JOEL HAROLD 7 0.179 440 GYARFAS, ANDRAS 8 0.176 177 SZEMEREDI, ENDRE 9 0.173 462 FAUDREE, RALPH JASPER, JR. 10 0.161 128 LOVASZ, LASZLO 11 0.158 287 CHUNG,FAN RONG KING(GRAHAM) 12 0.151 78 PACH, JANOS 13 0.151 341 KOSTOCHKA, ALEXANDR V. 14 0.146 261 NESETRIL, JAROSLAV 15 0.146 326

<!-- b000173 | prose | pages [9] -->
We can see from Table 3 that ALON, NOGA M. is the person who connects more important researchers within Erdos1 than others .

<!-- b000174 | prose | pages [9] -->
4.3

<!-- b000175 | heading | pages [9] -->
Validation of the Model

<!-- b000176 | prose | pages [9] -->
Comparing the two kinds of ranking methods, the majority of the authors in the ﬁrst table are also in the second table. However, some ’speciﬁc’ authors in the ﬁrst table cannot ﬁnd their name in the second top list. Why? Next, we will focus our discussion on the problem by the case of HARARY, FRANK*.

<!-- b000177 | prose | pages [9] -->
The degree of HARARY, FRANK* is the maximum 44, which means he coau- thored with 44 other Erdos1 authors. When we study the relatively most inﬂu- ential authors in the network, we discover that only 30 authors are the ’master’ within the network. That is to say, most of the co-authors of HARARY, FRANK*

<!-- b000178 | furniture | pages [10] -->
Team # 25318

<!-- b000179 | furniture | pages [10] -->
Page 9 of 20

<!-- b000180 | prose | pages [10] -->
are not high inﬂuential authors. So, when we consider both degree and the in- ﬂuence of his/her co-authors, authors whose degree ranks high may not be the ’master’ within the network. So, the weakness of the Relation Distance Model is being susceptible to large degree value.

<!-- b000181 | prose | pages [10] -->
4.4 Properties of the Erdos1 network

<!-- b000182 | prose | pages [10] -->
In subsection 4.2, we have got each node’s degree centrality. So, the degree distribution of the network can be obtained. Now, we focus our discussion on the degree distribution of the Erdos1 network. According to an algorithm com- bined maximum-likelihood ﬁtting methods with goodness-of-ﬁt tests proposed by Clauset [2007] , we discover that the distribution of degree centrality k in the Erdos1 network is approximate a power-law distribution, the power-law expo- nent is estimated as 1.6.

<!-- b000183 | prose | pages [10] -->
P(K > k) ∼k−1.6

<!-- b000184 | prose | pages [10] -->
The degree distribution of the Erdos1 network and the approximative power- law distribution is shown below in Figure 3.

<!-- b000185 | caption | pages [10] -->
Figure 3: The degree distribution of the Erdos1 network and the approximative power-law

<!-- b000186 | prose | pages [10] -->
distribution.

<!-- b000187 | prose | pages [10] -->
According to the idea of Barabsi [1999], we consider the Erdos1 co-authoring network as a scale-free network. In the scale-free network, most nodes have small degree value , only very few nodes have large degree value, the degree

<!-- b000188 | furniture | pages [11] -->
Team # 25318

<!-- b000189 | furniture | pages [11] -->
Page 10 of 20

<!-- b000190 | prose | pages [11] -->
distribution of the scale-free network appears to be approximately power-law distribution.

<!-- b000191 | prose | pages [11] -->
Some other properties are shown below:

<!-- b000192 | prose | pages [11] -->
• Overall graph clustering coefﬁcient of the network is 0.343

<!-- b000193 | prose | pages [11] -->
• Average distance (among reachable pairs) of the network is 3.825

<!-- b000194 | prose | pages [11] -->
5.

<!-- b000195 | heading | pages [11] -->
Authority-Popularity Evaluation Model

<!-- b000196 | prose | pages [11] -->
5.1 The Citation Network for Requirement 3

<!-- b000197 | prose | pages [11] -->
In Requirement 3,we construct a directed network connection graph with weight. The 16 foundational papers listed in the attached list (NetSciFounda- tion.pdf) and 8 additional paper we discover are considered as the nodes in the Citation network, and the citation relationship as the links. The Citation net- work is shown as Figure 4. The additional papers we discover are listed as below:

<!-- b000198 | prose | pages [11] -->
No.17: Newman, M. E. J., Strogatz, S. H., and Watts, D. J. Random graphs with arbitrary degree distributions and their applications, Phys. Rev. E 64, 026118 ,2001.

<!-- b000199 | prose | pages [11] -->
No.18: Bollob’as, B., Random Graphs, Academic Press, New York, 2nd ed.,2001.

<!-- b000200 | prose | pages [11] -->
No.19: Holland, P. W. and S. Leinhardt . An exponential family of probability distributions for directed graphs. Journal of the American Statistical Association 76, 33-65 ,1981.

<!-- b000201 | prose | pages [11] -->
No.20: Snijders, T. A. B. Markov chain Monte Carlo estimation of exponential random graph models. Journal of Social Structure 3(2), 2002.

<!-- b000202 | prose | pages [11] -->
No.21: Watts, D. J., Small Worlds , Princeton University Press, Princeton ,1999.

<!-- b000203 | prose | pages [11] -->
No.22: M.Barthlmy, The architecture of complex weighted networks, Proceedings of the National Academy of Sciences, 2004.

<!-- b000204 | prose | pages [11] -->
No.23: Luis A Nunes Amaral, Antonio Scala, Marc Barthlmy, H Eugene Stanley. Classes of small-world networks, Proceedings of the National Academy of Sciences,2000.

<!-- b000205 | prose | pages [11] -->
No.24: M. Barthlmy, Small-world networks: Evidence for a crossover picture Physical Re- view Letters, 1999.

<!-- b000206 | prose | pages [11] -->
• Explanation 1: Let paper A is cited by paper B, then the direction of the link between them is from B to A (for the implementing of PageRank Al- gorithm).

<!-- b000207 | furniture | pages [12] -->
Team # 25318

<!-- b000208 | furniture | pages [12] -->
Page 11 of 20

<!-- b000209 | caption | pages [12] -->
Figure 4: The directed citation network with weight added to nodes.

<!-- b000210 | prose | pages [12] -->
• Explanation 2: According to Assumption 2, we deﬁne the weight of a node as the impact factor of the journal [7] in which the paper published.

<!-- b000211 | prose | pages [12] -->
• Explanation 3: For the sake of description, we give each paper an ID. ’1’ for the ﬁrst paper in NetSciFoundation.pdf, ’2’ for the second ,’17’ for the ﬁrst paper in the additional list, etc.

<!-- b000212 | prose | pages [12] -->
5.2

<!-- b000213 | heading | pages [12] -->
Authority-Popularity Evaluation Model based on the revised

<!-- b000214 | heading | pages [12] -->
PageRank Algorithm

<!-- b000215 | prose | pages [12] -->
The aim of Requirement 3 is to determine the relative inﬂuence of the papers. In this task, we develop an Authority-Popularity Evaluation Model which is a combination of the revised PageRank Algorithm and Normalized Inﬂuence Factor. In our model, the PageRank value and the Inﬂuence Factor reﬂects the depth and the width of the impact, respectively.

<!-- b000216 | heading | pages [12] -->
The Modiﬁed PageRank Algorithm

<!-- b000217 | prose | pages [12] -->
The basic idea of the PageRank Algorithm is that the importance of a node is determined by the quantities and the quality of other nodes pointing to it. The original PageRank Algorithm is effective for common directed network in ana- lyzing the importance and impact of the nodes within the network. But when it comes to Dangling node (node whose out-degree is 0), the Random surﬁng will fail as it will be ’trapped’ in the Dangling node forever. We discover that there is 3 Dangling nodes the Citation Network in subsection 5.2, so a Modiﬁed PageRank Algorithm is proposed to measure the authority of papers in the net-

<!-- b000218 | furniture | pages [13] -->
Team # 25318

<!-- b000219 | furniture | pages [13] -->
Page 12 of 20

<!-- b000220 | prose | pages [13] -->
work. The Modiﬁed PageRank Algorithm includes two steps: Initialization and Iteration.

<!-- b000221 | prose | pages [13] -->
Step 1: Initialization

<!-- b000222 | prose | pages [13] -->
An initial PageRank value (PR value) PRx(0), x = 1, 2, . . . , n is given to all nodes in the network, satisﬁed with

<!-- b000223 | prose | pages [13] -->
n X

<!-- b000224 | prose | pages [13] -->
PRx(0) = 1

<!-- b000225 | prose | pages [13] -->
x=1

<!-- b000226 | prose | pages [13] -->
In our citation network, the initial PR value of each paper is deﬁned as the nor- malized impact factor of the journal in which the paper is published. The abso- lute impact factors value (collected from the web [6] ) with ID of each paper are listed in Table 4. For instance, the weight of paper No.4 ’Emergence of scaling in random networks’ published in Science is equal to the Impact Factor of Science 31.027.

<!-- b000227 | caption | pages [13] -->
Table 4: ID of papers and their Weight

<!-- b000228 | prose | pages [13] -->
No.1 No.2 No.3 No.4 0.322 44.982 0.539 31.027

<!-- b000229 | prose | pages [13] -->
No.9 No.10 No.11 No.12 2.313 9.737 5.952 3.542

<!-- b000230 | prose | pages [13] -->
No.17 No.18 No.19 No.20 2.313 39.265 1.834 2.542

<!-- b000231 | prose | pages [13] -->
No.5 No.6 No.7 No.8 0.424 3.381 4.375 38.597

<!-- b000232 | prose | pages [13] -->
No.13 No.14 No.15 No.16 31.027 38.597 5.019 3.381

<!-- b000233 | prose | pages [13] -->
No.21 No.22 No.23 No.24 40.664 9.737 9.737 7.943

<!-- b000234 | prose | pages [13] -->
A 24 order relationship matrix G is constructed by the rule if paper j is cited by paper i, Gij = 1. Otherwise , Gij = 0. Another matrix is coefﬁcient matrix D, which is also a 24 order matrix.

<!-- b000235 | prose | pages [13] -->
1

<!-- b000236 | prose | pages [13] -->


<!-- b000237 | prose | pages [13] -->


<!-- b000238 | prose | pages [13] -->


<!-- b000239 | prose | pages [13] -->
1

<!-- b000240 | prose | pages [13] -->
P(1)

<!-- b000241 | prose | pages [13] -->
1

<!-- b000242 | prose | pages [13] -->


<!-- b000243 | prose | pages [13] -->


<!-- b000244 | prose | pages [13] -->


<!-- b000245 | prose | pages [13] -->


<!-- b000246 | prose | pages [13] -->


<!-- b000247 | prose | pages [13] -->


<!-- b000248 | prose | pages [13] -->
. . .

<!-- b000249 | prose | pages [13] -->
D =

<!-- b000250 | prose | pages [13] -->


<!-- b000251 | prose | pages [13] -->


<!-- b000252 | prose | pages [13] -->


<!-- b000253 | prose | pages [13] -->


<!-- b000254 | prose | pages [13] -->


<!-- b000255 | prose | pages [13] -->


<!-- b000256 | prose | pages [13] -->
1

<!-- b000257 | prose | pages [13] -->


<!-- b000258 | prose | pages [13] -->


<!-- b000259 | prose | pages [13] -->


<!-- b000260 | prose | pages [13] -->


<!-- b000261 | prose | pages [13] -->
1

<!-- b000262 | prose | pages [13] -->
24

<!-- b000263 | prose | pages [13] -->
where P(i) =

<!-- b000264 | prose | pages [13] -->
P

<!-- b000265 | prose | pages [13] -->
Gji

<!-- b000266 | prose | pages [13] -->
j=1

<!-- b000267 | prose | pages [13] -->
Step 2: Iteration

<!-- b000268 | prose | pages [13] -->


<!-- b000269 | prose | pages [13] -->
1

<!-- b000270 | prose | pages [13] -->


<!-- b000271 | prose | pages [13] -->
P(2)

<!-- b000272 | prose | pages [13] -->


<!-- b000273 | prose | pages [13] -->
. . .

<!-- b000274 | prose | pages [13] -->
 

<!-- b000275 | prose | pages [13] -->
1

<!-- b000276 | prose | pages [13] -->


<!-- b000277 | prose | pages [13] -->
P(23)

<!-- b000278 | prose | pages [13] -->


<!-- b000279 | prose | pages [13] -->
1 P(24)

<!-- b000280 | prose | pages [13] -->
After k times iteration, we get the the PageRank value:

<!-- b000281 | furniture | pages [14] -->
Team # 25318

<!-- b000282 | furniture | pages [14] -->
Page 13 of 20

<!-- b000283 | caption | pages [14] -->
Figure 5: The ﬂow chart of iteration process

<!-- b000284 | prose | pages [14] -->
+ 1 −q

<!-- b000285 | prose | pages [14] -->
PRj(k)

<!-- b000286 | prose | pages [14] -->
X

<!-- b000287 | prose | pages [14] -->
PRi(k) = q

<!-- b000288 | prose | pages [14] -->
L(j)

<!-- b000289 | prose | pages [14] -->
j

<!-- b000290 | prose | pages [14] -->
i = 1, 2, . . . , n n

<!-- b000291 | prose | pages [14] -->
where j represent all nodes that point to node i. q is a constant, defaulted to be 0.85. We implement the iteration based on the equation above until the change of PageRank is small enough in one step. We set this threshold as 0.0001. We exe- cute a program for this process in MATLAB@2012b and get the stable PageRank value PR(k) as is shown in Table 5.

<!-- b000292 | caption | pages [14] -->
Table 5: The rank of papers by the stable PageRank value.

<!-- b000293 | prose | pages [14] -->
PRi(k) Ranking ID

<!-- b000294 | prose | pages [14] -->
1 0.01575 No.18 2 0.01217 No.14 3 0.00937 No.4 4 0.00784 No.2 5 0.00493 No.1 6 0.00278 No.17 7 0.00183 No.21 8 0.00150 No.3 9 0.00142 No.10 10 0.00142 No.9 11 0.00142 No.8 12 0.00111 No.6

<!-- b000295 | prose | pages [14] -->
PRi(k) Ranking ID

<!-- b000296 | prose | pages [14] -->
13 0.00094 No.19 14 0.00060 No.11 15 0.00060 No.23 16 0.00051 No.24 17 0.00051 No.20 18 0.00051 No.13 19 0.00047 No.22 20 0.00047 No.16 21 0.00047 No.15 22 0.00047 No.12 0.00047 23 No.7 0.00047 24 No.5

<!-- b000297 | prose | pages [14] -->
The result shows that the No.18 paper: Random Graphs, wrote by Bollobs, has the highest PageRank. So it is the most authoritative paper among 24 paper- s. Authority reﬂects the depth of inﬂuence. To ﬁnd the most inﬂuential paper we have to get the width of the inﬂuence: popularity. We consider to use cited quantities to inﬂect the popularity in the citation network. Since the cited quan- tities related to the years that paper were published, so we set cited quantities per year as the parameter, which is shown in Table 6 .

<!-- b000298 | prose | pages [14] -->
To judge which is the most inﬂuential paper, we draw a picture of 24 nodes (as is shown in Figure 6). For the sake of observability, we set log10(106 ∗PRi(k))

<!-- b000299 | furniture | pages [15] -->
Team # 25318

<!-- b000300 | furniture | pages [15] -->
Page 14 of 20

<!-- b000301 | caption | pages [15] -->
Table 6: Cited quantities per year of each paper.

<!-- b000302 | prose | pages [15] -->
ID cited quantities/year

<!-- b000303 | prose | pages [15] -->
No.14 1355.5 No.4 1256.2 No.2 1104.2 No.11 965.1 No.18 458.2 No.21 281.8 No.10 211.4 No.17 178.2 No.23 170.6 No.22 142.3 No.9 117.2 No.12 97.1

<!-- b000304 | prose | pages [15] -->
ID cited quantities/year

<!-- b000305 | prose | pages [15] -->
No.8 89 No.1 82.4 No.3 72.4 No.13 69.6 No.6 54.5 No.20 34.6 No.16 27.7 No.24 19.5 No.19 16.9 No.15 11.0 No.7 0.5 No.5 3.125

<!-- b000306 | prose | pages [15] -->
as ordinate and log10(10 ∗citedquantitiesperyear) as abscissa.

<!-- b000307 | caption | pages [15] -->
Figure 6: Authority-Popularity Diagram for the citation network

<!-- b000308 | heading | pages [15] -->
In our Authority-Popularity Evaluation Model, we divided Figure 6 into four

<!-- b000309 | prose | pages [15] -->
regions: (1) high authority, more popular; (2) high authority, less popular; (3) low authority, more popular and (4) low authority, less popular. It is clear that the node on the upper right corner is the most inﬂuential paper as it is both the most authoritative and the most popular one. The most inﬂuential paper within the Citation Network in subsection 5.1 is No.14: Collective dynamics of ‘small-world’ networks, wrote by Watts, D. and Strogatz, S.

<!-- b000310 | furniture | pages [16] -->
Team # 25318

<!-- b000311 | furniture | pages [16] -->
Page 15 of 20

<!-- b000312 | prose | pages [16] -->
5.3 The Co-star Network for Requirement 4

<!-- b000313 | prose | pages [16] -->
Similar to Erdos number in mathematics, a Bacon number[7] in the ﬁlm in- dustry is popular in the late 1990’s. The ’Game of Kevin Bacon’ measures the shortest path to connect an arbitrary actor/actress with Bacon. Inspired by the game, we collect a set of 15 famous Hollywood movie stars as nodes and the co-star movies as links to construct a co-star network(as is shown in Figure 7). This is also a directed network connection graph with weight, but the difference is that the weight value is added to the link instead of the node.

<!-- b000314 | prose | pages [16] -->
• Explanation 1: Let A is the leading actor who is supported by actor B in a movie, then the direction of the link between them is from B to A.

<!-- b000315 | prose | pages [16] -->
• Explanation 2: According to Assumption 3, we deﬁne the weight of the link between two stars as the IMDb rating[1] of the movie they co-starred.

<!-- b000316 | caption | pages [16] -->
Figure 7: The directed citation network with weight added to links.

<!-- b000317 | prose | pages [16] -->
Since the weight value is added to the link instead of node in co-star net- work, the PageRank algorithm here has to be improved. By the origin PageR- ank algorithm, the PageRank value of node i will be distributed to nodes which are pointed to from i evenly in every step of the iteration. In our improved PageRank algorithm, how much PageRank value that node i distribute to nodes that i point to is determined by the weight (IMDb rating[1] of the movie) of the link. The weight is proportional to PageRank value that is distributed. This is reasonable because excellent movie can make movie stars more inﬂuential. For example, the weight of the link(i to k) is 3, the weight of the link(i to n) is 4.

<!-- b000318 | prose | pages [16] -->
3 3+4 × 1 and the PageRank that i So the PageRank value that i distribute to k is 4 3+4 × 1, as is shown in Figure 8. distribute to n is

<!-- b000319 | furniture | pages [17] -->
Team # 25318

<!-- b000320 | furniture | pages [17] -->
Page 16 of 20

<!-- b000321 | caption | pages [17] -->
Figure 8: The diagram for modiﬁed algorithm.

<!-- b000322 | prose | pages [17] -->
So iteration for this algorithm is different. The relationship matrix G in it- eration for the citation network should be revised to G’ in the co-star network. We set column j of G as Gj, G′

<!-- b000323 | prose | pages [17] -->
j is deﬁned similarly. It is clearly that if Gij̸ = 0,

<!-- b000324 | prose | pages [17] -->
ij represents a movie. The elements in G′

<!-- b000325 | prose | pages [17] -->
then G′

<!-- b000326 | prose | pages [17] -->
rating of the movie in G′ j should be proportional to IMDb

<!-- b000327 | prose | pages [17] -->
j. For example, We assumed that the movie G2j’s IMDb rating is 3, G4j’s IMDb rating is 4. And

<!-- b000328 | prose | pages [17] -->
Gj = [0 1 0 1 0]T

<!-- b000329 | prose | pages [17] -->
So we get

<!-- b000330 | prose | pages [17] -->
3 + 4(1 + 1) = 6 3

<!-- b000331 | prose | pages [17] -->
G′

<!-- b000332 | prose | pages [17] -->
2j = 7

<!-- b000333 | prose | pages [17] -->
j = [0 6

<!-- b000334 | prose | pages [17] -->
G′

<!-- b000335 | prose | pages [17] -->
3 + 4(1 + 1) = 8 4

<!-- b000336 | prose | pages [17] -->
G′

<!-- b000337 | prose | pages [17] -->
4j = 7

<!-- b000338 | prose | pages [17] -->
7 0 8 7 0]T

<!-- b000339 | prose | pages [17] -->
Other steps are same as in subsection 5.2. We also implement the improved PageRank algorithm in MATLAB@2012b and result is as below in Table 7.

<!-- b000340 | prose | pages [17] -->
As is in subsection 5.2, we draw a picture for 15 nodes in the co-star network. In Figure 9 , we set log10(the number of Google search results) as abscissa and the stable PageRank value as ordinate. It is clear that Angelina Jolie is the most inﬂuential movie star in this network.

<!-- b000341 | prose | pages [17] -->
5.4

<!-- b000342 | heading | pages [17] -->
Sensitivity Analysis

<!-- b000343 | prose | pages [17] -->
To analysis the robustness of our model, we perform a sensitivity analysis on our approach.In the PageRank algorithm, there is an equation:

<!-- b000344 | furniture | pages [18] -->
Team # 25318

<!-- b000345 | furniture | pages [18] -->
Page 17 of 20

<!-- b000346 | caption | pages [18] -->
Table 7: PR value and number of Google search results for each star.

<!-- b000347 | prose | pages [18] -->
Name

<!-- b000348 | prose | pages [18] -->
Angelina Jolie Tom Cruise Brad Pitt Morgan Freeman Matt Damon Tom Hanks Nicole Kidman Leonardo DiCaprio George Clooney Nicolas Cage Sandra Bullock Joseph Gordon-Levitt Anne Hathaway Kirsten Dunst Tobey Maguire PR value Google search

<!-- b000349 | heading | pages [18] -->
results(million)

<!-- b000350 | prose | pages [18] -->
0.140634 242 0.117486 238 0.096786 198 0.091811 60.6 0.087352 85.1 0.075816 122 0.073816 86.5 0.070141 149 0.062742 58.1 0.044374 34.8 0.044015 49.5 0.032107 19.7 0.032107 85.5 0.016211 15.9 0.014601 7.44

<!-- b000351 | caption | pages [18] -->
Figure 9: Authority-Popularity Diagram for the co-star network

<!-- b000352 | prose | pages [18] -->
+ 1 −q

<!-- b000353 | prose | pages [18] -->
PRj(k)

<!-- b000354 | prose | pages [18] -->
X

<!-- b000355 | prose | pages [18] -->
PRi(k) = q

<!-- b000356 | prose | pages [18] -->
L(j)

<!-- b000357 | prose | pages [18] -->
j

<!-- b000358 | prose | pages [18] -->
i = 1, 2, . . . , n n

<!-- b000359 | prose | pages [18] -->
where q is a constant, generally be called Damp Coefﬁcient. The meaning of q is: There is a Possibility, which equal to (1-q), that all of the nodes in the network have the same PageRank value :1/N. If coefﬁcient q is not used, the ’strong’ nodes will be so strong that other nodes are hard to ’survive’. For the co-star network, this is also make sense. The PageRank value of a movie star reﬂects the authority, it can also be seen as the possibility that a movie wants him to

<!-- b000360 | furniture | pages [19] -->
Team # 25318

<!-- b000361 | furniture | pages [19] -->
Page 18 of 20

<!-- b000362 | prose | pages [19] -->
star. But there are always some movies do not need the most famous actor, the movie stars all have the opportunity to be the starring. This situation is reﬂected by coefﬁcient q. So value of q can inﬂuence the PageRank of the network. q is de- faulted be 0.85, we set the PageRank for q = 0.85 as standard. With q changes, we get the corresponding PageRank and analyze the similarity between this PageR- ank and the standard. The results were shown in Figure 10.

<!-- b000363 | caption | pages [19] -->
Figure 10: Sensitivity to Damp Coefﬁcient q

<!-- b000364 | prose | pages [19] -->
The results show that in a certain range, the PageRank change slowly with the change of q. So we can see that our model has high stability.

<!-- b000365 | prose | pages [19] -->
5.5

<!-- b000366 | heading | pages [19] -->
Strengths and Weaknesses

<!-- b000367 | heading | pages [19] -->
Strengths

<!-- b000368 | prose | pages [19] -->
• Comprehensiveness: From the perspective of both depth and width, we determine the importance based on a variety of indexes.

<!-- b000369 | heading | pages [19] -->
• Adaptability and Practicability: The model we build has good portability,

<!-- b000370 | prose | pages [19] -->
it is suitable for most network analysis.

<!-- b000371 | prose | pages [19] -->
• Simplicity and Accuracy: The programs of the model are easy to under- stand, and the calculations are precise.

<!-- b000372 | prose | pages [19] -->
• Flexibility: No matter whether the weight is added to the nodes or links, and whether there are dangling nodes in the network, the model is able to tackle it.

<!-- b000373 | furniture | pages [20] -->
Team # 25318

<!-- b000374 | furniture | pages [20] -->
Page 19 of 20

<!-- b000375 | heading | pages [20] -->
Weaknesses

<!-- b000376 | prose | pages [20] -->
• Data Limitations: The model is applicable to large volumes of data net- work. Unfortunately, if the data of a network is limited, the error is large.

<!-- b000377 | prose | pages [20] -->
6.

<!-- b000378 | prose | pages [20] -->
The philosophy of the scale-free network

<!-- b000379 | prose | pages [20] -->
Barabsi and Albert [1999] pointed out that ER random graph and WS small world model neglect two important characteristics of actual network.

<!-- b000380 | prose | pages [20] -->
• Growth: The scale of actual network is growing. For instance, a large number of papers will be published every month. However, in ER random graph and WS small world model, the number of nodes in the network is ﬁxed.

<!-- b000381 | prose | pages [20] -->
• Preferential attachment: New nodes tend to connect with those nodes with high connectivity. This phenomenon is also known as ’Rich get rich- er’ or ’Matthew effect’. We can note that new papers tend to cite those important and inﬂuential papers which have been widely quoted. And also, actors always try their best to cooperate with those movie stars.

<!-- b000382 | prose | pages [20] -->
The dynamics in the scale-free network is the philosophy behind the famous Pareto principle[9] (also known as the 80-20 rule), which states that, for many events, roughly 80% of the effects come from 20% of the causes.

<!-- b000383 | prose | pages [20] -->
Shortcut to boost inﬂuence

<!-- b000384 | prose | pages [20] -->
As is proposed above, new nodes tend to connect with important nodes in the network. However, in the real world, the ’important nodes’ are hard to be ap- proached by the ordinary one. For instance, for an ordinary network researcher, it is hard to believe he can have the chance to co-author with a leading ﬁgure in the ﬁeld of network research as the important ones also tend to cooperate with other inﬂuential people. So, how can we boost our inﬂuence as quickly as possible? The solution we propose by our model is shown as below:

<!-- b000385 | prose | pages [20] -->
• Determine the ’20%’ in the network according to our Relation Distance Model or Authority-Popularity Evaluation Model

<!-- b000386 | prose | pages [20] -->
• Calculate the closeness centrality of the ’80%’ to ’20%’

<!-- b000387 | prose | pages [20] -->
• Cooperating with the 80% (more approachable relatively) with low close- ness centrality step by step and ﬁnally co-author with the key ﬁgure in the ﬁeld

<!-- b000388 | furniture | pages [21] -->
Team # 25318

<!-- b000389 | furniture | pages [21] -->
Page 20 of 20

<!-- b000390 | caption | pages [21] -->
Figure 11: The shortcut to boost inﬂuence

<!-- b000391 | heading | pages [21] -->
References

<!-- b000392 | references | pages [21] -->
[1] http://www.imdb.com/

<!-- b000393 | references | pages [21] -->
[2] Freeman, L. C. (1979). Centrality in social networks: Conceptual clariﬁca-

<!-- b000394 | references | pages [21] -->
tion. Social Networks, 1(3), 215239.

<!-- b000395 | references | pages [21] -->
[3] S. Mahmoodzadeh, J. Shahrabi, M. Pariazar, and M. S. Zaeri, Project Se-

<!-- b000396 | references | pages [21] -->
lection by Using Fuzzy AHP and TOPSIS Technique, World Academy of

<!-- b000397 | references | pages [21] -->
Science, Engineering and Technology 30 2007, 333-338.

<!-- b000398 | references | pages [21] -->
[4] http://en.wikipedia.org/wiki/Centrality

<!-- b000399 | references | pages [21] -->
[5] Aaron Clauset, Cosma Rohilla Shalizi and M. E. J. Newman,Power-Law

<!-- b000400 | references | pages [21] -->
Distributions in Empirical Data,2007,arXiv: 0706.1062v1.

<!-- b000401 | references | pages [21] -->
[6] Barabsi, A-L, and Albert, R. Emergence of scaling in random networks. Sci-

<!-- b000402 | references | pages [21] -->
ence, 286:509-512, 1999.

<!-- b000403 | references | pages [21] -->
[7] http://www.impactfactorsearch.com

<!-- b000404 | references | pages [21] -->
[8] http://www.cs.virginia.edu/oracle/

<!-- b000405 | references | pages [21] -->
[9] http://en.wikipedia.org/wiki/Pareto_principle
