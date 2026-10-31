# P-C-2014-30221-7af27341

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Who Is the Hidden Champion in a Network?

<!-- b000002 | title | pages [1] -->
February 10, 2014

<!-- b000003 | heading | pages [1] -->
1 Summary

<!-- b000004 | prose | pages [1] -->
Network science is essential in many civil and military applications due to its great help to complex systems with network-based structures. Since the co-author relationship as well as the citation relationship forms a network structure in research areas, network science can be utilized to do some data-mining works in this network, e.g. seeking inﬂuential researchers and important research papers.

<!-- b000005 | prose | pages [1] -->
In this paper, we extract useful data from given large datasets and establish the required co- author and citation networks. For visual clarity of the network, we propose and implement the stress majorization algorithm based on the minimal-energy principle in physics, which provides a proper 2-D layout for complex networks. Then we develop four different centrality measures based on the perspectives of trivial sum, weighted sum, geographic control and informational control, respectively, for undirected graph and three centrality measures for directed graph, in which both the non-parametric and parametric methodologies are involved. Furthermore, we propose several methods to transform a directed graph into an undirected one. We show that these measures generate consistent results for both the most inﬂuential researcher and the most important paper.

<!-- b000006 | prose | pages [1] -->
Then we extend our model from research areas to other areas of society, and show that our model still yields convincing results for top singers, songwriters and movie stars, even when a bipartite graph is used instead. Moreover, we conclude that a crude criterion for a real problem to be solved by network science in essence is that there is a network structure and something in interest transmitting through the network, with all real experiments conforming to this s- tatement. In addition, it is proved theoretically and veriﬁed numerically that our parametric approach guarantees its convergence, hence there are only loose requirements for parameters.

<!-- b000007 | prose | pages [1] -->
In summary, our model is practical and reliable for handling network-based problems in real- ity. Nevertheless, there are some existing problems such as computational complexity and lack of automatic adaptation preventing our model from convenient implementation, and certain phenomenon such as information cascade lies beyond the scope of our modelling.

<!-- b000008 | keywords | pages [1] -->
Key Words: network science, co-author, citation, centrality, stress majorization

<!-- b000009 | prose | pages [1] -->
1

<!-- b000010 | furniture | pages [2] -->
Team # 30221

<!-- b000011 | furniture | pages [2] -->
Page 2 of 20

<!-- b000012 | heading | pages [2] -->
Contents

<!-- b000013 | contents | pages [2] -->
1

<!-- b000014 | contents | pages [2] -->
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000015 | contents | pages [2] -->
1

<!-- b000016 | contents | pages [2] -->
2

<!-- b000017 | contents | pages [2] -->
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000018 | contents | pages [2] -->
3

<!-- b000019 | contents | pages [2] -->
3

<!-- b000020 | contents | pages [2] -->
Task 1: Co-author Network of the Erdos1 Author . . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
4

<!-- b000023 | contents | pages [2] -->
Task 2: Centrality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
5

<!-- b000025 | contents | pages [2] -->
4.1

<!-- b000026 | contents | pages [2] -->
Degree Centrality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
5

<!-- b000028 | contents | pages [2] -->
4.2

<!-- b000029 | contents | pages [2] -->
Eigenvector Centrality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
6

<!-- b000031 | contents | pages [2] -->
4.3

<!-- b000032 | contents | pages [2] -->
Closeness Centrality

<!-- b000033 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
7

<!-- b000035 | contents | pages [2] -->
4.4

<!-- b000036 | contents | pages [2] -->
Betweenness Centrality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
8

<!-- b000038 | contents | pages [2] -->
4.5

<!-- b000039 | contents | pages [2] -->
Summary of Centrality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
9

<!-- b000041 | contents | pages [2] -->
5

<!-- b000042 | contents | pages [2] -->
Task 3: The Citation Network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
9

<!-- b000044 | contents | pages [2] -->
5.1

<!-- b000045 | contents | pages [2] -->
Undirected Graph Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
10

<!-- b000047 | contents | pages [2] -->
5.2

<!-- b000048 | contents | pages [2] -->
Directed Graph Method

<!-- b000049 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
11

<!-- b000051 | contents | pages [2] -->
5.3

<!-- b000052 | contents | pages [2] -->
Extensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
12

<!-- b000054 | contents | pages [2] -->
6 Task 4: Applications in Singers and Movie Actors

<!-- b000055 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
13

<!-- b000057 | contents | pages [2] -->
6.1

<!-- b000058 | contents | pages [2] -->
Basic Model

<!-- b000059 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
13

<!-- b000061 | contents | pages [2] -->
6.2

<!-- b000062 | contents | pages [2] -->
Bipartite Graph Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
14

<!-- b000064 | contents | pages [2] -->
6.3

<!-- b000065 | contents | pages [2] -->
Analysis

<!-- b000066 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
15

<!-- b000068 | contents | pages [2] -->
7

<!-- b000069 | contents | pages [2] -->
Task 5: Heuristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [2] -->
16

<!-- b000071 | contents | pages [2] -->
8 Sensitivity Analysis

<!-- b000072 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [2] -->
17

<!-- b000074 | contents | pages [2] -->
8.1

<!-- b000075 | contents | pages [2] -->
Non-parametric Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [2] -->
17

<!-- b000077 | contents | pages [2] -->
8.2

<!-- b000078 | contents | pages [2] -->
Parametric Models

<!-- b000079 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
18

<!-- b000081 | contents | pages [2] -->
9 Strengths and Weaknesses

<!-- b000082 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
18

<!-- b000084 | contents | pages [2] -->
9.1

<!-- b000085 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
18

<!-- b000087 | contents | pages [2] -->
9.2

<!-- b000088 | contents | pages [2] -->
Weaknesses

<!-- b000089 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
19

<!-- b000091 | contents | pages [2] -->
10 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [2] -->
19

<!-- b000093 | contents | pages [2] -->
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
20

<!-- b000095 | furniture | pages [3] -->
Team # 30221

<!-- b000096 | furniture | pages [3] -->
Page 3 of 20

<!-- b000097 | heading | pages [3] -->
2 Introduction

<!-- b000098 | prose | pages [3] -->
Network science has gained its popularity recently due to the considerable network struc- tures emerging in reality, which can be of great help to data mining, dynamic systems, etc. In academic ﬁelds, we can establish the corresponding network structures for both citation and co- authoring relationships, and then the data mining work within these networks is of great interest and signiﬁcance. Some simple questions are raised: how to measure the inﬂuence of a researcher, or how to evaluate the importance of a research paper?

<!-- b000099 | prose | pages [3] -->
To answer this question, there are network-based evaluation tools that use co-author and citation data to determine the impact factor of researchers, publications and journals, such as Science Citation Index (SCI), H-factor, Impact factor, Eigenfactor, etc. Our goal is to design effective measures to analyze inﬂuence in research networks, and then extend it to other areas of society. Speciﬁcally, we will do the following things in this paper:

<!-- b000100 | prose | pages [3] -->
• Establish a co-author network using given data and plot it on a 2-D plane, then propose several measures to determine who is the most inﬂuential researcher.

<!-- b000101 | prose | pages [3] -->
• Propose models to evaluate the importance of research papers using co-author and citation data.

<!-- b000102 | prose | pages [3] -->
• Extend the models to other areas in society or other entities in research areas, then test and analyze its performances.

<!-- b000103 | prose | pages [3] -->
• Gain heuristics from this model and discuss how individuals can learn from it in reality.

<!-- b000104 | prose | pages [3] -->
• Implement the sensitivity test and analyze its strengths and weaknesses, as well as the potential research directions.

<!-- b000105 | heading | pages [3] -->
3 Task 1: Co-author Network of the Erdos1 Author

<!-- b000106 | prose | pages [3] -->
First of all, we build the co-author network of the Erdos1 authors from the source provid- ed by the problem. Due to the symmetry of the pairwise co-author relationship, it is natural to utilize graph theory to fully characterize it, where we establish a simple undirected graph and regard researchers as vertices and the co-authoring relationship as edges. For computational sim- plicity, we use an adjacency matrix A = (aij)N×N to store this relationship, where N = 511 is the number of researchers who have co-authored with Erd¨os, and the entry aij is an indicator of the relationship:

<!-- b000107 | prose | pages [3] -->
( 1 researcher i has co-authored with researcher j aij = (1) 0 elsewhere

<!-- b000108 | prose | pages [3] -->
In particular, since this graph is undirected, A is symmetric.

<!-- b000109 | prose | pages [3] -->
Observing that the dataset is large (with 511 researchers and over 18,000 raw lines), we use programming to accomplish data extraction. Speciﬁcally, we just write a simple string matching algorithm by Ruby codes, which exports the corresponding adjacency matrix (excluding Erd¨os) for further use1. Once we obtain the adjacency matrix A, some of its properties such as transitiv- ity ratio2 are listed as follows.

<!-- b000110 | prose | pages [3] -->
1Note that the resulting matrix is not symmetric due to some minor errors in source data, and we force its symmetry by assigning aij ←max(aij, aji).

<!-- b000111 | prose | pages [3, 4] -->
2The transitivity ratio describes how vertices tend to cluster and is deﬁned as trace(A3) 3 × number of triangles C ≜ number of connected triples of vertices = sum(A2 −A) Number of vertices Number of edges Average degree Transitivity ratio

<!-- b000112 | furniture | pages [4] -->
Team # 30221

<!-- b000113 | furniture | pages [4] -->
Page 4 of 20

<!-- b000114 | caption | pages [4] -->
Table 1: Basic Properties for Co-authoring Relationship

<!-- b000116 | prose | pages [4] -->
511 1713 6.70 0.2238

<!-- b000117 | prose | pages [4] -->
Since the average degree 6.70 ≪511, we observe that this graph is sparse. Moreover, accord- ing to the transitivity ratio, this co-authoring relationship is moderately transitive. These results meet our intuition that researchers often co-authored with those who they are familiar with, but there are also some restrictions on pairwise cooperation, e.g. time limitation. To see deeper into this graph, we summarize its degree distribution in Table 2.

<!-- b000118 | caption | pages [4] -->
Table 2: Degree Distribution

<!-- b000119 | prose | pages [4] -->
[31,dmax=52] Range of degree 0 [1,2] [3,5] [6,10] [11,20] [21,30]

<!-- b000120 | prose | pages [4] -->
Number of vertices 37 150 122 114 51 23 14

<!-- b000121 | prose | pages [4] -->
As is illustrated in the table, majority of vertices have small degrees, while a fraction (16%) of researchers are somewhat well-known who have co-authored with many researchers (more than 10) in this list. This fact could also be illustrated by the network plotted on a 2-D plane, while it is a challenging task owing to the obvious difﬁculties in designing a proper and visible layout. It is quite complicated to deﬁne visible here, but intuitively, it is better to place two linked vertices to be close, and place the distance of those which there is no edge connecting them to be relatively far.

<!-- b000122 | prose | pages [4] -->
Using the heuristics above, Gansner et al.[1] developed a graph-drawing method called stress majorization. Assume that there exists an optimal distance between each pair (this distance is set according to certain criteria, such as the one discussed above), then we can approach this optimal state by setting the vertices properly. We consider a metric to measure the so-called approaching as follows.

<!-- b000123 | prose | pages [4] -->
X stress(X) ≜ wij(∥Xi −Xj∥−dij)2 (2) i<j where Xi ∈R2 is the 2-D position for vertex i, dij, wij’s are optimal distances and corresponding weights, respectively, and ∥· ∥is the Euclidean distance. [1] suggests:

<!-- b000124 | prose | pages [4] -->
• dij is the overall length of the shortest path connecting i and j (is computed using Floyd Shortest-Path Algorithm[2]), with each edge (i, j) assigning a length

<!-- b000125 | prose | pages [4] -->
lij = #{k : exactly one of (k, i) and (k, j) is an edge} (3)

<!-- b000126 | prose | pages [4] -->
• wij = d−2 ij is the corresponding weight.

<!-- b000127 | prose | pages [4] -->
We can imagine that there is a mechanic spring with equilibrium length dij and stiffness coefﬁcient wij between each pair of vertices, then physical force will drive the system into a state with minimal energy regardless of the initial state. This motivates us to use iterative methods, where each iteration is an optimization step. Consider ij + trace(XT LX) −2 · trace(XT LY Y ) X F(X, Y ) ≜ wijd2 (4) i<j

<!-- b000128 | prose | pages [4, 5] -->
where  i̸ = j, Yi = Yj 0 (  −wij i̸ = j  Lij ≜ ij ≜ LY i = j , −dijwij/∥Yi −Yj∥ i̸ = j, Yi̸ = Yj (5) P k̸=i wik k̸=i LY  −P i = j  ik Then by using Cauchy-Schwarz Inequality we can obtain that F(X, Y ) ≥stress(X) with equal- ity iff X = Y . In addition, we have L†LY Y = arg min

<!-- b000129 | furniture | pages [5] -->
Team # 30221

<!-- b000130 | furniture | pages [5] -->
Page 5 of 20

<!-- b000132 | heading | pages [5] -->
X F(X, Y )

<!-- b000133 | prose | pages [5] -->
(6)

<!-- b000134 | prose | pages [5] -->
where L† is the pseudo-inverse of L. Hence, consider the following algorithm:

<!-- b000135 | prose | pages [5] -->
• Choose X(1) at random;

<!-- b000136 | prose | pages [5] -->
• Do iterations X(k+1) ←L†LX(k)X(k) until stress(X(k)) −stress(X(k+1)) < ϵ (a predetermined threshold) (7) stress(X(k))

<!-- b000137 | prose | pages [5] -->
• Return X(k) as the ﬁnal position for vertices.

<!-- b000138 | prose | pages [5] -->
Then according to (5) and (6), we have

<!-- b000139 | prose | pages [5] -->
stress(X(k+1)) ≤F(X(k+1), X(k)) ≤F(X(k), X(k)) = stress(X(k)) (8) thus the energy is non-increasing during iterations. Furthermore, X(k) will approach a minimal- energy state with a convergence rate close to unity[3]. Hence, this iterative algorithm guarantees the minimization of (2).

<!-- b000140 | prose | pages [5] -->
We accomplish this algorithm and run it using Matlab®2011a while setting ϵ = 10−5 in (7), and the resulting graph layout is shown in Figure 1, where red hollow triangles represent vertices and blue lines represent edges. As is shown in the ﬁgure, there are 42 connected com- ponents in total, where the largest one consists of 466 vertices. Although still to be improved, it outperforms the random plotting signiﬁcantly, e.g. the layout for small-degree vertices is quite clear. In addition, we may attribute the unclear large-degree vertices in Figure 1 to the original 2-D plotting problem itself, i.e. it is difﬁcult to draw in essence. For example, it is always hard to draw a complete graph of n vertices clearly in a 2-D plane when n is large. Hence, despite its drawbacks, Figure 1 is a good characterization for co-authoring relationship.

<!-- b000141 | heading | pages [5] -->
4 Task 2: Centrality

<!-- b000142 | prose | pages [5] -->
Since we have known the structure of the co-author network, we want to develop a variety of measures to capture noteworthy features of the network topology. There are several methods in the ﬁeld of social science to analyze the inﬂuence and impact of vertices in a network[4]. Here we choose four measures which we think are effective to determine which vertices are the most important.

<!-- b000143 | heading | pages [5] -->
4.1 Degree Centrality

<!-- b000144 | prose | pages [5] -->
Degree centrality is the simplest centrality measure in which the centrality of a vertex is deﬁned to be equal to its degree, i.e., the number of edges connected to it. To some extent, it seems reasonable to think that individuals who have more connections with others would have more impact, higher reputation, or more information sources, for co-authoring a manuscript usually connotes a strong inﬂuential connection between researchers. In the co-author network, the number of co-authors that an individual network researcher has connection with gives us a rough measure of whether the researcher is inﬂuential. Based on this idea, we calculate the centrality of all vertices and sort them in descending order, where the ”centrality” here is exactly its degree. Here, we count the degree of each vertices and list the top-10 authors in Table 3.

<!-- b000145 | furniture | pages [6] -->
Team # 30221

<!-- b000146 | furniture | pages [6] -->
Page 6 of 20

<!-- b000147 | caption | pages [6] -->
Figure 1: The Graph Layout

<!-- b000148 | caption | pages [6] -->
Table 3: Degree Centrality

<!-- b000149 | prose | pages [6] -->
Rank Name Centrality

<!-- b000150 | prose | pages [6] -->
1 ALON, NOGA M. 52 2 GRAHAM, RONALD LEWIS 44 2 HARARY, FRANK* 44 4 RODL, VOJTECH 43 4 BOLLOBAS, BELA 43 6 TUZA, ZSOLT 40 7 FUREDI, ZOLTAN 39 8 SOS, VERA TURAN 38 9 SPENCER, JOEL HAROLD 35 10 GYARFAS, ANDRAS 32 10 PACH, JANOS 32

<!-- b000151 | heading | pages [6] -->
4.2 Eigenvector Centrality

<!-- b000152 | prose | pages [6] -->
Eigenvector centrality, proposed by Bonacich in 1987[4], is a natural extension of the degree centrality. In the previous method, we award one ”centrality point” for each network neighbor a vertex has. But in fact, different neighbors are not equivalent. In many circumstances, an inﬂuential researcher can spill over the inﬂuence to his co-authors. Based on these ideas, in eigenvector centrality every vertex is given a centrality proportional to the sum of the centralities of its neighbors, i.e.

<!-- b000153 | prose | pages [6, 7] -->
wn+1 = C · Awn (9) Note that we obtain a sequence {wn} from a dynamic perspective, where w0̸ = 0 with all com- ponents non-negative is chosen at random. According to the essence of the power method[5], under some regularity conditions we have

<!-- b000154 | furniture | pages [7] -->
Team # 30221

<!-- b000155 | furniture | pages [7] -->
Page 7 of 20

<!-- b000157 | prose | pages [7] -->
n→+∞wn = w ⇔(C = λ−1 lim and w = x1) (10) 1

<!-- b000158 | prose | pages [7] -->
where λ1 is the unique principal eigenvalue of A, and x1 is the corresponding eigenvector, from which the name ”eigenvector centrality” originates. Here, we omit the simple implementation and list top-10 authors in Table 4.

<!-- b000159 | caption | pages [7] -->
Table 4: Eigenvector Centrality

<!-- b000160 | prose | pages [7] -->
Rank Name Centrality

<!-- b000161 | prose | pages [7] -->
1 ALON, NOGA M. 0.2599 2 RODL, VOJTECH 0.2343 3 BOLLOBAS, BELA 0.2089 4 GRAHAM, RONALD LEWIS 0.2041 5 FUREDI, ZOLTAN 0.2006 6 TUZA, ZSOLT 0.1870 7 SPENCER, JOEL HAROLD 0.1793 8 GYARFAS, ANDRAS 0.1760 9 SZEMEREDI, ENDRE 0.1725 10 FAUDREE, RALPH JASPER, JR. 0.1614

<!-- b000162 | heading | pages [7] -->
4.3 Closeness Centrality

<!-- b000163 | prose | pages [7] -->
Closeness centrality provides a totally different method in which the importance of a vertex is measured by the average distance from itself to other vertices. Based on the theory of the geodesic path, we can calculate the distance between two vertices which is the length of the geodesic path (shortest path). For a vertex i, the average distance li is deﬁned as follows:

<!-- b000164 | prose | pages [7] -->
li = 1 X dij (11) n j

<!-- b000165 | prose | pages [7] -->
where dij is the length of the shortest path from i to j, or equivalently, the minimal number of edges along this path, n is the number of vertices.

<!-- b000166 | prose | pages [7] -->
Intuitively, a small li indicates that vertex i is close to others on average and thus has more access to information. Furthermore, it’s easier for ”close” vertices to communicate with each other and convey their opinions, which results in their larger direct inﬂuence on others. Unlike our preference for large degree centrality and eigenvector centrality, the mean distance gives lower value for more central node[4]. Hence, we can compute the reciprocal of li instead, which is called the closeness centrality:

<!-- b000167 | prose | pages [7] -->
Ci ≜1 (12) li

<!-- b000168 | prose | pages [7] -->
Here, we list the top-10 authors in terms of the closeness centrality.

<!-- b000169 | furniture | pages [8] -->
Team # 30221

<!-- b000170 | furniture | pages [8] -->
Page 8 of 20

<!-- b000171 | caption | pages [8] -->
Table 5: Closeness Centrality

<!-- b000172 | prose | pages [8] -->
Rank Name Centrality

<!-- b000173 | prose | pages [8] -->
1 ALON, NOGA M. 0.020192 2 GRAHAM, RONALD LEWIS 0.020189 3 BOLLOBAS, BELA 0.020186 4 FUREDI, ZOLTAN 0.020184 5 SOS, VERA TURAN 0.020173 6 TUZA, ZSOLT 0.020154 7 RODL, VOJTECH 0.020148 8 LOVASZ, LASZLO 0.020147 9 STRAUS, ERNST GABOR* 0.020145 10 SPENCER, JOEL HAROLD 0.020144

<!-- b000174 | heading | pages [8] -->
4.4 Betweenness Centrality

<!-- b000175 | prose | pages [8] -->
A different concept is provided by betweenness centrality, which measures the extent to which a vertex lies on paths between other vertices. Speciﬁcally, we ﬁrst suppose that there is some- thing ﬂowing around the network from one person to another, e.g., information, news and mes- sages pass from one person to another in the social network, where the co-author network is a particular example. Then we make the following assumptions:

<!-- b000176 | prose | pages [8] -->
• Each pair of connected vertices is selected from the graph equiprobably per unit time, and the selected pair exchanges messages.

<!-- b000177 | prose | pages [8] -->
• Messages always take the geodesic path. If there are several shortest paths, one is chosen at random.

<!-- b000178 | prose | pages [8] -->
In a suitably long time, messages pass down every geodesic path with equal probability. Hence, we can conclude that the number of messages passing through every vertex should be propor- tional to the number of geodesic paths it lies on. Formally, we express the betweenness centrality xi of vertex i as

<!-- b000179 | prose | pages [8] -->
ni s,t X xi = (13) gs,t s,t

<!-- b000180 | prose | pages [8] -->
where ni s,t is the number of geodesic path from s to t passing i and gs,t is the total number of geodesic paths from s to t, and we deﬁne 0/0 = 0.

<!-- b000181 | prose | pages [8] -->
Nonetheless, due to computational power limitation of our server, we can modify the com- putational process of calculating betweenness centrality without loss of its attribute [4]. Denote Ii s,t as the indicator function of the event that the geodesic path from s to t passes through vertex i, then we redeﬁne the new betweenness centrality xi as follows:

<!-- b000182 | prose | pages [8] -->
X Ii xi = (14) s,t s,t

<!-- b000183 | prose | pages [8, 9] -->
Betweenness centrality conforms to common sense. On one hand, individuals with high be- tweenness centrality might have more control on messages passing between others and thus could derive more power from their position. On the other hand, if the vertices with high betweenness are removed from the network, plenty of communications would be disrupted between other vertices. A simple example is a unique vertex linking two large groups like a bridge, while its degree can be small. Although these strong assumptions may not hold in reali- ty, betweenness centrality still provides a crude measure for the inﬂuential vertices in charge of message ﬂow.

<!-- b000184 | furniture | pages [9] -->
Team # 30221

<!-- b000185 | furniture | pages [9] -->
Page 9 of 20

<!-- b000187 | prose | pages [9] -->
We list the top-10 authors in terms of betweenness centrality in Table 6.

<!-- b000188 | caption | pages [9] -->
Table 6: Betweenness Centrality

<!-- b000189 | prose | pages [9] -->
Rank Name Centrality

<!-- b000190 | prose | pages [9] -->
1 ALON, NOGA M. 43603 2 GRAHAM, RONALD LEWIS 40694 3 SOS, VERA TURAN 40269 4 BOLLOBAS, BELA 38808 5 FUREDI, ZOLTAN 38361 6 HARARY, FRANK* 37471 7 STRAUS, ERNST GABOR* 36333 8 TUZA, ZSOLT 33560 9 POMERANCE, CARL BERNARD 30341 10 RUBEL, LEE ALBERT* 28357

<!-- b000191 | heading | pages [9] -->
4.5 Summary of Centrality

<!-- b000192 | prose | pages [9] -->
We summarize some inﬂuential researchers in terms of all four measures in Table 7. Since these measures give the same top inﬂuential researcher, we are conﬁdent that ALON, NOGA M. has the most signiﬁcant inﬂuence within the network.

<!-- b000193 | caption | pages [9] -->
Table 7: Most Inﬂuential Authors

<!-- b000194 | prose | pages [9] -->
Name Rank of DC Rank of EC Rank of CC Rank of BC

<!-- b000195 | prose | pages [9] -->
ALON, NOGA M. 1 1 1 1 GRAHAM, RONALD LEWIS 2 4 2 2 BOLLOBAS, BELA 4 3 3 4 RODL, VOJTECH 4 2 7 11 FUREDI, ZOLTAN 7 5 4 5 TUZA, ZSOLT 6 6 6 8 SOS, VERA TURAN 8 19 5 3

<!-- b000196 | heading | pages [9] -->
5 Task 3: The Citation Network

<!-- b000197 | prose | pages [9] -->
The preceding co-author network deals with the evaluation for inﬂuential researchers. As for the inﬂuence evaluation for research paper, there is another type of measure associated with citation, which is a globally used criterion in academic ﬁelds. Motivated by the spirit of network science, we also build a citation network consisting of 16 papers provided by the ICM problem3.

<!-- b000198 | prose | pages [9] -->
3Note: we delete the ﬁfth and the seventh paper from the original list for their weak citation relationships with others, and add two books [6, 7] instead.

<!-- b000199 | furniture | pages [10] -->
Team # 30221

<!-- b000200 | furniture | pages [10] -->
Page 10 of 20

<!-- b000201 | prose | pages [10] -->
Similar to the previous tasks, we use an adjacency matrix C = (cij)M×M for the network repre- sentation, where M = 16 is the paper number, and

<!-- b000202 | prose | pages [10] -->
( 1 paper j is cited by paper i cij ≜ (15) 0 elsewhere

<!-- b000203 | prose | pages [10] -->
Note that the citation relationship is anti-symmetric, then the symmetry property of C no longer holds. In particular, we have cij + cji = 1 −δij (Dirac function).

<!-- b000204 | prose | pages [10] -->
The citation network can be plotted by the biograph toolbox in Matlab®2011a as shown in Figure 2, where we abbreviate each paper into its ﬁrst author followed by its years of publica- tion4 and citation times5 in parentheses. Note that i →j in Figure 2 means cij = 1, or equiv- alently, j is cited by i. Compared with the co-author network plotted in Figure 1, the citation network is also sparse and looks more clear due to its small size.

<!-- b000205 | prose | pages [10] -->
Snijders2011(Cite:33)

<!-- b000206 | prose | pages [10] -->
Watts2007(Cite:680) Newman2003(Cite:10616) Valente1996(Cite:498) Borgatti2000(Cite:763)

<!-- b000207 | prose | pages [10] -->
Watts2002(Cite:835) Albert2002(Cite:13250) Bonacich1987(Cite:1956)

<!-- b000208 | prose | pages [10] -->
Kleinberg2000(Cite:1246) Newman2001(2)(Cite:2748) Newman2001(Cite:1523)

<!-- b000209 | prose | pages [10] -->
Barabasi1999(Cite:18843) Bollobas2001(Cite:5957) Erdos1959(Cite:4531) Ahuja1993(Cite:9153)

<!-- b000210 | prose | pages [10] -->
Watts1998(Cite:21688)

<!-- b000211 | caption | pages [10] -->
Figure 2: Illustration for the Citation Network

<!-- b000212 | prose | pages [10] -->
The network in Figure 2 is directed, while we can also establish undirected graphs for analysis, both of which are to be discussed in the following subsections. In addition, since the co-author relationship here is too sparse, we abandon it in this task.

<!-- b000213 | heading | pages [10] -->
5.1 Undirected Graph Method

<!-- b000214 | prose | pages [10] -->
To form an undirected graph, we need to seek symmetric relationships deriving from the adjacency matrix C. Note that CT C and CCT are both symmetric matrices, we try to interpret their meanings as follows.

<!-- b000215 | prose | pages [10] -->
• CT C: since its (i, j) entry P k ckickj is exactly the number of papers citing i and j altogether in its bibliography, we call it co-bibliography relationship

<!-- b000216 | prose | pages [10] -->
• CCT : since its (i, j) entry P k cikcjk is exactly the number of papers cited by both i and j, we call it co-citation relationship

<!-- b000217 | prose | pages [10] -->
Since these relationships are both symmetric, all the centrality measures used in Task 2 can apply here. We list all top-3 results in Table 8 and Table 96.

<!-- b000218 | prose | pages [10] -->
From these tables, we have the following observations. Firstly, compared with the citation order shown in the last column, the co-bibliography method gives closer orders. Secondly, the

<!-- b000219 | prose | pages [10] -->
4Since there are two papers written by M. Neuman in 2001, we add the symbol ”(2)” to the latter one (the eleventh) in the paper list.

<!-- b000220 | prose | pages [10] -->
5We obtain the citation times from Google Scholar with deadline Feb. 10th, 2014.

<!-- b000221 | prose | pages [10] -->
6In both tables, ”Citation” means ranking paper according to its citation times in descending order.

<!-- b000222 | furniture | pages [11] -->
Team # 30221

<!-- b000223 | furniture | pages [11] -->
Page 11 of 20

<!-- b000224 | caption | pages [11] -->
Table 8: Most Inﬂuential Papers Using Co-bibliography Relationship

<!-- b000225 | prose | pages [11] -->
Rank DC EC CC BC Citation

<!-- b000226 | prose | pages [11] -->
1 Barab´asi1999 Barab´asi1999 Barab´asi1999 Barab´asi1999 Watts1998 Barab´asi1999 2 Watts2002 Watts1998 Watts1998 Watts2002 3 Watts1998 Kleinberg2000 Erd¨os1959 Erd¨os1959 Albert2002

<!-- b000227 | caption | pages [11] -->
Table 9: Most Inﬂuential Papers Using Co-citation Relationship

<!-- b000228 | prose | pages [11] -->
Rank DC EC CC BC Citation

<!-- b000229 | prose | pages [11] -->
1 Newman2003 Newman2003 Newman2003 Newman2003 Watts1998 Barab´asi1999 2 Albert2002 Albert2002 Albert2002 Albert2002 3 Newman2001(2) Watts2002 Watts2002 Newman2001(2) Albert2002

<!-- b000230 | prose | pages [11] -->
years of publishing in Table 8 are earlier than those in Table 9 in general. Finally, according to Figure 2, papers in Table 8 tend to be cited by others while those in Table 9 tend to cite others. In fact, all these properties can be explained by the relationships themselves. In co-bibliography relationship, (i, j) is a high-weight edge when paper i, j are often cited simultaneously by oth- ers, while in the co-citation relationship, (i, j) is a high-weight edge when paper i, j cite many identical papers. Hence, papers in Table 8 tend to be cited by others and be published earlier accordingly, and vice versa.

<!-- b000231 | prose | pages [11] -->
As for the ﬁrst observation, we need keep in mind a widely-accepted principle that the cited work is more inﬂuential and valuable in general. Hence, the co-bibliography relationship guarantees the connected papers to be cited by others, while papers with co-citation relationship may be new papers to be evaluated. Hence, the co-bibliography method is more reliable, and it ﬁts the order of overall citation times well. In conclusion, the paper Barab´asi1999 is the most inﬂuential one within the list in this undirected graph method.

<!-- b000232 | heading | pages [11] -->
5.2 Directed Graph Method

<!-- b000233 | prose | pages [11] -->
Now we turn to the original directed graph described in adjacency matrix C. Unlike the interpersonal relation in co-author network, the citation network deals with papers, thus the message transmission model used in closeness centrality and betweenness centrality makes little sense here. However, our expectation that an inﬂuential paper is cited many times and by oth- er important papers still conforms to common sense, which results in the validity for degree centrality and eigenvector centrality. Hence, we adopt the following measures:

<!-- b000234 | prose | pages [11] -->
• Citation: count citation times in Google Scholar as in previous subsection;

<!-- b000235 | prose | pages [11] -->
• Degree centrality: count the in-degree for each vertex;

<!-- b000236 | prose | pages [11] -->
• Eigenvector centrality: compute the principal eigenvector for CT ;

<!-- b000237 | prose | pages [11] -->
• Modiﬁed Katz centrality: to be introduced below.

<!-- b000238 | prose | pages [11, 12] -->
As is stated before, the eigenvector centrality is designed to characterize the spill-over prop- erty for inﬂuence through edges, which means being cited by an important paper leads to a growing inﬂuence in this citation network. However, the citation has diminishing returns to in- ﬂuences especially for research papers, for the universal over-citation phenomena in academic ﬁelds. Hence, still from a dynamic perspective of view, we modify (9) as

<!-- b000239 | furniture | pages [12] -->
Team # 30221

<!-- b000240 | furniture | pages [12] -->
Page 12 of 20

<!-- b000242 | prose | pages [12] -->
−p     w(n+1) w(n) X X ∝ cji (16)   i j j j:cji=1

<!-- b000243 | prose | pages [12] -->
where P j cji is the cited times for paper j, and parameter p ∈[0, 1] characterizes the diminishing property. Note that in (16) we set the inﬂuence of all new papers, i.e. papers not cited by others, to be zero, which is to be improved. Hence, we add another term to (16):

<!-- b000244 | prose | pages [12] -->
−p     w(n+1) w(n) X X ∝ cji + b (17) i  j j j:cji=1

<!-- b000245 | prose | pages [12] -->
Hence, the parameter b ≥0 is the default inﬂuence of each new paper. It can be easily derived that (17) can be written in matrix form:

<!-- b000246 | prose | pages [12] -->
w(n+1) = normalize(Rw(n) + b · 1) (18)

<!-- b000247 | prose | pages [12] -->
for certain deterministic matrix R, where normalization means scaling the maximal component to unit, and 1 is the column vector for all 1’s. Hence, (18) is an iterative method to calculate the steady-state w with w(1) = 0, which is the Katz centrality [4] adding an extra normalization step. Actually, the Page-rank method that Google uses to sort webpages is also an extension of Katz centrality[8]. As for the impact of parameter selection, we refer all interested readers to later section ”Sensitivity Analysis”.

<!-- b000248 | prose | pages [12] -->
We summarize the top-3 inﬂuential papers under these measures in Table 10.

<!-- b000249 | caption | pages [12] -->
Table 10: Most Inﬂuential Papers Using Directed Graph

<!-- b000250 | prose | pages [12] -->
MKC(p = 1/2, b = 0.2) Rank DC EC Citation

<!-- b000251 | prose | pages [12] -->
1 Watts1998 Watts1998 Watts1998 Watts1998 2 Barab´asi1999 Barab´asi1999 Barab´asi1999 Barab´asi1999 3 Erd¨os1959, etc. Bollobus2001 Erd¨os1959 Albert2002

<!-- b000252 | prose | pages [12] -->
Hence, all results in Table 10 are close to each other, indicating the robustness of direct con- sideration of the original citation network, and note that Albert2002 which is recommended by overall citation times does not outperform others in our analysis due to its few citations in this small paper list. In conclusion, we recommend Watts1998 to be the most inﬂuential paper.

<!-- b000253 | heading | pages [12] -->
5.3 Extensions

<!-- b000254 | prose | pages [12] -->
So far we have handled the evaluation for inﬂuences of researchers and papers, and our framework and the network essence can be extended for judgment of individuals, universities, departments, journals, etc. In the academic ﬁeld, all these terms are mainly comprised of re- search papers, thus we can continue to adopt the paper-level network spirit. Speciﬁcally, we regard individuals/universities/departments/journals as vertices, and establish a directed ci- tation graph where i →j means paper from vertex j is cited by some papers from vertex i. Note that in this case, weights (e.g. number of citations) can be assigned to edges, and self-loop is permitted here. Furthermore, we can also build the individual-level network, in which some interpersonal relationships (e.g. co-authoring) play the main role. These citation or co-authoring data can be obtained from Google Scholar or university websites.

<!-- b000255 | furniture | pages [13] -->
Team # 30221

<!-- b000256 | furniture | pages [13] -->
Page 13 of 20

<!-- b000257 | prose | pages [13] -->
Once the network is built, we can use the preceding approaches to deal with either directed or undirected graphs, and the role as well as the inﬂuence of a certain vertex can be obtained from different measures. For example, for an individual with large betweenness centrality, he plays a signiﬁcant role in message transmission. Hence, the preceding models can apply to varieties of circumstances, as long as there is a network structure and something in interest transmitting through the network (e.g. inﬂuence, information, messages, etc.).

<!-- b000258 | heading | pages [13] -->
6 Task 4: Applications in Singers and Movie Actors

<!-- b000259 | prose | pages [13] -->
As is described before, the previous models and measures are concerned about groups with the essence of the network, where authors and papers have been tested. In this section, we apply our model to completely different sets, i.e. singers or movie actors, and then evaluate and analyze the performance.

<!-- b000260 | heading | pages [13] -->
6.1 Basic Model

<!-- b000261 | prose | pages [13] -->
We ﬁrst apply our models and measures to singers. We collect the information of all pop singers in China who have released new songs from 2011 to 2013, and then establish a simple undirected graph as before. Here we are encountered with the deﬁnition for the relationship between singers, where the adjacency matrix will be extremely sparse when only cooperation between singers is counted. To settle this problem, we take songwriters into account and adopt the co-singer relationship analogous to the undirected graph method in Task 3, i.e. we place an edge between singers iff they sing songs written by the same songwriter. As the result, we obtain a graph with 195 vertices and 4929 edges.

<!-- b000262 | prose | pages [13] -->
We apply the four measures in Task 2 to this dataset, and the top-5 singers are listed in Table 11.

<!-- b000263 | caption | pages [13] -->
Table 11: Top-5 Singers in 2011-2013 Using Basic Model

<!-- b000264 | prose | pages [13] -->
Rank DC EC CC BC

<!-- b000265 | prose | pages [13] -->
1 Bibi Chou Eason Chan Bibi Chou Jane Zhang 2 Leung Jasmine Bibi Chou Leung Jasmine Bibi Chou 3 Eason Chan Leung Jasmine Eason Chan Leung Jasmine 4 Jane Zhang Andy Hui Jane Zhang Eason Chan 5 Angela Chang A Mei Angela Chang Angela Chang

<!-- b000266 | prose | pages [13] -->
Note that these measures yield credible results because those ranking in the top-5 in all meth- ods (Eason Chan, BiBi Chou, Leung Jasmine) are actually Chinese super-stars who are extremely popular in recent years.

<!-- b000267 | prose | pages [13] -->
Analogously, we collect ﬁlms (excluding cartoon) in mainland China from 2011 to 2013 with more than 2,000 ﬁlm reviews7, whose main actors (of size 3) are placed in the network, and vertices are connected pairwise indicating their cooperation in a ﬁlm. Then we obtain a graph with 453 vertices and 743 edges, and top-5 movie actors are listed in Table 12.

<!-- b000268 | prose | pages [13] -->
The results seem reasonable because Bo Huang, Louis Koo and Aaron Kwok have performed in many inﬂuential movies recently and are believed to generate the highest box ofﬁce revenue among movie stars.

<!-- b000269 | prose | pages [13] -->
7Data source: www.douban.com, which is a popular platform for commenting on movies, books, music, etc.

<!-- b000270 | furniture | pages [14] -->
Team # 30221

<!-- b000271 | furniture | pages [14] -->
Page 14 of 20

<!-- b000272 | caption | pages [14] -->
Table 12: Top-5 Movie Actors in 2011-2013 Using Basic Model

<!-- b000273 | prose | pages [14] -->
Rank DC EC CC BC

<!-- b000274 | prose | pages [14] -->
1 Bo Huang Louis Koo Bo Huang Bo Huang 2 Aaron Kwok Bo Huang Louis Koo Aaron Kwok 3 Ye Liu Ye Liu Aaron Kwok Louis Koo 4 Louis Koo Aaron Kwok Nick Cheung Ye Liu 5 Willian Feng Yuanyuan Gao Angelababy Angelababy

<!-- b000275 | heading | pages [14] -->
6.2 Bipartite Graph Model

<!-- b000276 | prose | pages [14] -->
Recall that the graphs we deal with in the previous subsection are both simple undirected graphs, which are the same as those in Task 1-2. However, a bipartite graph can also be established due to some special structures, i.e. interactions between two different sets. In our example, the bipartite graph can consist of singers and songwriters, or actors and ﬁlms, while edges represent the trivial song-writing or performing relationships, respectively. We consider singers (together with songwriters) and movie actors (together with ﬁlms) separately as follows.

<!-- b000277 | prose | pages [14] -->
When evaluating singers, we pick only 29 songwriters who have more than 20 cooperating singers for computational simplicity, and then apply the algorithms in Task 2 directly to this bipartite graph. The ranking of top singers as well as songwriters are given in Table 13 and 14, respectively.

<!-- b000278 | caption | pages [14] -->
Table 13: Top-5 Singers in 2011-2013 Using Bipartite Graph Model

<!-- b000279 | prose | pages [14] -->
Rank DC EC CC BC

<!-- b000280 | prose | pages [14] -->
1 Jane Zhang Eason Chan Bibi Chou Jane Zhang 2 Leung Jasmine Leung Jasmine Leung Jasmine Leung Jasmine 3 Eason Chan Bibi Chou Eason Chan Bibi Chou 4 Bibi Chou Andy Hui Jane Zhang Eason Chan 5 Andy Hui A Mei Angela Chang Angela Chang

<!-- b000281 | caption | pages [14] -->
Table 14: Top-5 Songwriters in 2011-2013 Using Bipartite Graph Model

<!-- b000282 | prose | pages [14] -->
Rank DC EC CC BC

<!-- b000283 | prose | pages [14] -->
1 Ruolong Yao Ruolong Yao Ruolong Yao Ruolong Yao 2 Albert Leung Qian Yao Albert Leung Albert Leung 3 Francis Lee Albert Leung Francis Lee Qian Yao 4 Qian Yao Francis Lee Qian Yao Francis Lee 5 Vincent Fang Vincent Fang Vincent Fang Vincent Fang

<!-- b000284 | prose | pages [14] -->
Hence, we can draw the observations that ranks for singers is close to those in the basic mod- el, and ranks for songwriters meet people’s intuition and coincide in contents in four different methods. Thus, we ﬁnd it feasible to use bipartite graph model in such a singer-songwriter network.

<!-- b000285 | prose | pages [14] -->
As for the results in the actor-ﬁlm bipartite graph, we refer readers to Table 15 and 16 below8.

<!-- b000286 | prose | pages [14] -->
8Note: there is no ranking result in terms of the degree centrality in Table 16, for degrees of all ﬁlms are 3 due to our speciﬁc selection strategy.

<!-- b000287 | furniture | pages [15] -->
Team # 30221

<!-- b000288 | furniture | pages [15] -->
Page 15 of 20

<!-- b000289 | caption | pages [15] -->
Table 15: Top-5 Movie Actors in 2011-2013 Using Bipartite Graph Model

<!-- b000290 | prose | pages [15] -->
Rank DC EC CC BC

<!-- b000291 | prose | pages [15] -->
1 Bo Huang Louis Koo Bo Huang Bo Huang 2 Louis Koo Sean Andy Louis Koo Aaron Kwok 3 Aaron Kwok Daniel Wu Nick Cheung Louis Koo 4 Ye Liu Bo Huang Aaron Kwok Ye Liu 5 Willian Feng Yuanyuan Gao Angelababy Angelababy

<!-- b000292 | caption | pages [15] -->
Table 16: Top-5 Movie Actors in 2011-2013 Using Bipartite Graph Model

<!-- b000293 | prose | pages [15] -->
Rank EC CC BC

<!-- b000294 | prose | pages [15] -->
1 Overheard 2 Black & White Episode Black & White Episode 2 Dont Go Breaking My Heart Conspirators Conspirators 3 The White Storm Drug War Drug War 4 Inferno 3D The Pretending Lovers Better and better 5 All’s Well, Ends Well Lost in Thailand Silent Witness

<!-- b000295 | prose | pages [15] -->
The results for movie actors are a little messy, and William Feng, Sean Andy and Yuanyuan Gao are not considered to be that popular. Ranks for movies also look confusing and vary with different measures. Hence we can roughly say that the bipartite graph does not work well when handling movies and movie actors.

<!-- b000296 | heading | pages [15] -->
6.3 Analysis

<!-- b000297 | prose | pages [15] -->
Before we analyze the performances of these two models, recall our previous unveriﬁed statement that our previous models work when there is a network structure and something in interest transmitting through the network. Now we apply this statement to see its consistency with the above results.

<!-- b000298 | prose | pages [15] -->
In China, singers and songwriters are a lot in common, e.g. singers and songwriters can both become famous with the rising popularity of a song. In addition, one can utilize the reputation of the other to appeal to music fans. Hence, not only is there a network structure, but also the popularity can transmit through the network in the bipartite graph model. As for the basic mod- el, since there are many examples that an ordinary singer become well-known rapidly simply because one of his songs is sang by a famous singer, we also manage to verify the popularity transmission accordingly. These are reasonable explanations for the success when dealing with singers and songwriters.

<!-- b000299 | prose | pages [15] -->
Nevertheless, movie stars and movies interact differently in China. The plot of the movie rather than the popularity of its movie actors plays a larger role when contemporary Chinese ﬁlm lovers decide to watch it, while the plot quality has weak connections with movie actors. Hence, although performing in a successful movie will raise popularity, it is difﬁcult for movie actors to transmit his popularity conversely. This is a reasonable explanation for the failure of the bipartite graph model. As for the basic model, the popularity transmission between two actors exists in reality, which is supported by many real cases. Hence, the performance of the basic model is not so bad.

<!-- b000300 | prose | pages [15, 16] -->
To summarize, although there is a network structure in every model, it is whether there is something in interest transmitting through the network that determines whether the previous model based on network science could apply or not. This is also a useful criterion for the intu- itive prediction about whether these models can provide convincing results.

<!-- b000301 | furniture | pages [16] -->
Team # 30221

<!-- b000302 | furniture | pages [16] -->
Page 16 of 20

<!-- b000304 | heading | pages [16] -->
7 Task 5: Heuristics

<!-- b000305 | prose | pages [16] -->
Having set up several different measures to evaluate the impact of vertices in a given net- work, we now apply our methodologies to help us gain heuristics, e.g. make wise decisions. At the individual level, we wonder how one can boost my mathematical inﬂuence as soon as possible. Let’s come back to the co-author network established in Task 1. To be more concise and intuitive, we consider the following scenario: a newcomer can choose only one author to cooperate, what is the optimal option for that new entrant? In network terminology, there is one new-come node which can choose to add an undirected edge to connect with exactly one node in the original network. There are 511 choices, but which one provides the new-come vertex with highest centrality? As for the type of centrality, we have the following observations:

<!-- b000306 | prose | pages [16] -->
• The degree centrality of newcomer is always 1.

<!-- b000307 | prose | pages [16] -->
• The newcomer lies on no geodesic path unless either s or t in (13) is the newcomer itself.

<!-- b000308 | prose | pages [16] -->
Hence, we only need to focus on eigenvector centrality and closeness centrality. We write anoth- er Ruby program to compute them by a six-hour simulation, which is the product of 511 options and 40-second running time for each. The simulation results are summarized in Table 17 and 18.

<!-- b000309 | caption | pages [16] -->
Table 17: Best Choices to Boost Eigenvector Centrality

<!-- b000310 | prose | pages [16] -->
Rank Co-author’s Name Newcomer’s Centrality

<!-- b000311 | prose | pages [16] -->
1 ALON, NOGA M. 0.2605 2 RODL, VOJTECH 0.2348 3 BOLLOBAS, BELA 0.2094 4 GRAHAM, RONALD LEWIS 0.2045 5 FUREDI, ZOLTAN 0.2011 6 TUZA, ZSOLT 0.1874 7 SPENCER, JOEL HAROLD 0.1797 8 GYARFAS, ANDRAS 0.1764 9 SZEMEREDI, ENDRE 0.1729 10 FAUDREE, RALPH JASPER, JR. 0.1617

<!-- b000312 | prose | pages [16] -->
We have an interesting observation. In either eigenvector or closeness centrality case, the top- 10 choices simulated by our Ruby program is exactly the top-10 researchers in original network with unchanged orders. This phenomenon can be proved theoretically, but we only give the intuitive explanations due to space limitations. The eigenvector centrality for each vertex is determined by that of its neighbors, thus the new-comer should choose the most inﬂuential one for it can only have 1 neighbor. The explanation in closeness centrality is analogous upon observing that the newcomer’s shortest path must pass through its unique neighbor.

<!-- b000313 | prose | pages [16] -->
That is to say, the newcomer should cooperate with the most inﬂuential author, i.e., an ex- isting researcher with highest centrality, which conforms to common sense: co-authoring with a more inﬂuential one makes himself more inﬂuential. Nevertheless, due to some factors such as cut throat competitions, the more inﬂuential the author is, the harder he is to co-author with. The neophyte faces a trade-off and must incorporate both beneﬁts and costs, and ﬁnal results vary from people to people.

<!-- b000314 | furniture | pages [17] -->
Team # 30221

<!-- b000315 | furniture | pages [17] -->
Page 17 of 20

<!-- b000316 | caption | pages [17] -->
Table 18: Best Choices to Boost Closeness Centrality

<!-- b000317 | prose | pages [17] -->
Rank Co-author’s Name Newcomer’s Centrality

<!-- b000318 | prose | pages [17] -->
1 ALON, NOGA M. 0.020193 2 GRAHAM, RONALD LEWIS 0.020190 3 BOLLOBAS, BELA 0.020187 4 FUREDI, ZOLTAN 0.020186 5 SOS, VERA TURAN 0.020175 6 TUZA, ZSOLT 0.020155 7 RODL, VOJTECH 0.020149 8 LOVASZ, LASZLO 0.020148 9 STRAUS, ERNST GABOR* 0.020146 10 SPENCER, JOEL HAROLD 0.020145

<!-- b000319 | prose | pages [17] -->
We also consider other scenarios, for instance, a newcomer can choose two authors (e.g. the ﬁrst one may be his former supervisor in his undergraduate school, and the second is a well-known professor to whom he wants to apply for a Ph.D. degree) to cooperate, what is his optimal option now? Although it is estimated to require 4 months for simulation, which is far beyond the time limitation, it is a more realistic modelling with considerable new implications. For example, it is not necessarily optimal for such a newcomer to choose the researcher with highest centrality in terms of closeness or betweenness, for the new vertex has another neighbor and becomes able to connect two separate groups now. In a word, despite the lack of a closed- form formula, our model provides individuals with the key heuristics of the essential tradeoff they are faced with; and if all individuals are instructed in this way, then game theory can also be applied here to study individuals’ incentives and best strategies. Hence, both the graduate school decision and thesis advisor selection can be attributed to this general problem.

<!-- b000320 | heading | pages [17] -->
8 Sensitivity Analysis

<!-- b000321 | prose | pages [17] -->
In this section we implement the sensitivity test for our models. Note that there are both non-parametric (e.g. four measures introduced in Task 2) and parametric (e.g. the modiﬁed Katz centrality) models, we treat them differently as follows.

<!-- b000322 | heading | pages [17] -->
8.1 Non-parametric Models

<!-- b000323 | prose | pages [17] -->
For the sake of simplicity, we restrict our non-parametric models within the four centrality measures, while other models are natural extensions from them. First of all, note that there are two types of sensitivity altogether, both types of which concern about the availability of the model to other similar datasets. Speciﬁcally, the ﬁrst type uses an alternative dataset of another attribute (e.g. in non-academic ﬁelds), and we have handled this problem in Task 4 and claim that these models are not sensitive to attribute of data. The second type checks the sensitivity to minor errors using a slightly adjusted dataset, which is to be explored here.

<!-- b000324 | prose | pages [17] -->
Based on the co-author network in Task 1, we implement random experiments for 10 times, where we add and delete 5 edges simultaneously in the original graph at random in each ex- periment. We rank the researchers in each resulting graph using all four measures, and list the largest deviation9 of corresponding top-5 researchers compared with Table 3-6 in Table 19.

<!-- b000325 | prose | pages [17] -->
9Note: the deviation for a researcher is deﬁned as the absolute value of the difference in his ranking.

<!-- b000326 | furniture | pages [18] -->
Team # 30221

<!-- b000327 | furniture | pages [18] -->
Page 18 of 20

<!-- b000328 | caption | pages [18] -->
Table 19: Deviation Times for All Four Measures

<!-- b000329 | prose | pages [18] -->
Largest Deviation DC EC CC BC

<!-- b000330 | prose | pages [18] -->
0 4 8 7 3 1 3 1 3 5 2 3 1 0 2

<!-- b000331 | prose | pages [18] -->
Since the largest deviation is always no more than 2, minor changes in original network only result in minor changes in ranking. Furthermore, since the degrees for top-5 vertices in Table 3 are close to each other, it is reasonable that the degree centrality will deviate. In addition, adding or deleting edges may destruct the original topological structure severely, which results in the changes of geodesic paths accordingly. Hence, the betweenness centrality model is veriﬁed to be moderately sensitive, whose extent decreases in closeness centrality due to taking average. Fi- nally, since the set of inﬂuential vertices does not change signiﬁcantly, the eigenvector centrality is not sensitive.

<!-- b000332 | prose | pages [18] -->
In conclusion, all four measures are not sensitive to minor changes in network, while some of which will have slightly different ranking orders.

<!-- b000333 | heading | pages [18] -->
8.2 Parametric Models

<!-- b000334 | prose | pages [18] -->
The only parametric model used in this paper is the modiﬁed Katz centrality (MKC) model deﬁned in (16)-(18). First of all, based on the recursive formula, it is easy to show that {wn} is a Cauchy sequence in terms of the ℓ1 norm, and all components for each wn are non-negative. Hence due to the completeness of Rn, the sequence {wn} converges for sure. Hence, the conver- gence is not sensitive to parameters p, b as long as b > 0.

<!-- b000335 | prose | pages [18] -->
Now we consider the impacts for choosing p, b. As is stated before, large p means it is more important to be cited by inﬂuential works (e.g. Bollobas2001, where there is no new paper in its neighborhood) rather than more works (e.g. Watts1998, whose degree is the largest). Hence, a large p and small b means that the citation of a new paper is of little help, where Bollobas2001 is more likely to be more inﬂuential, and vice versa. In particular, the MKC method degenerates to the eigenvector centrality method when p = 0.

<!-- b000336 | prose | pages [18] -->
A numerical experiment is implemented to verify the preceding results. When ﬁxing b = 0.01, then the threshold for p is 0.993, where Bollobas2001 will dominate when p > 0.993 and Watts1998 will dominate conversely. Analogously, when p = 1 is ﬁxed, then the threshold for b is 0.09, where a smaller b is preferred by Bollobas2001. Hence, the result of this experiment is consistent with our intuition. Hence, we can adjust p, b accordingly to seek a balance between quality and quantity.

<!-- b000337 | heading | pages [18] -->
9 Strengths and Weaknesses

<!-- b000338 | heading | pages [18] -->
9.1 Strengths

<!-- b000339 | prose | pages [18] -->
• Simplicity. Our measures are based on easily understood principles and there are simple ways to compute them. In addition, our results are simply scores or ranks.

<!-- b000340 | prose | pages [18] -->
• Parameters. Most of our models are non-parametric, and our parametric models guarantee the convergence. Hence, there is no need to worry too much about the parameters.

<!-- b000341 | furniture | pages [19] -->
Team # 30221

<!-- b000342 | furniture | pages [19] -->
Page 19 of 20

<!-- b000343 | prose | pages [19] -->
• Different values and perspectives involved. The deﬁnition for ”inﬂuential” is subject to different personal values or perspectives. However, we propose several measures based on distinct viewpoints/assumptions, e.g. the spilling-over property for inﬂuences, mes- sage transmission, the balance between quality and quantity, etc., which can meet users’ different demands.

<!-- b000344 | prose | pages [19] -->
• Capability. Our models and measures are capable of solving problems associated with many types of graphs, including a directed or undirected graph with vertices belonging to one attribute, as well as a bipartite graph with vertices belonging to two attributes.

<!-- b000345 | prose | pages [19] -->
• Coverage. Our models and measures can cover considerable real problems where there is a network structure and something in interest transmitting through the network.

<!-- b000346 | prose | pages [19] -->
• Heuristics. Individuals and groups can gain considerable heuristics from our paper, e.g.

<!-- b000347 | prose | pages [19] -->
when to utilize network science and how to do corresponding cost-beneﬁt analysis.

<!-- b000348 | heading | pages [19] -->
9.2 Weaknesses

<!-- b000349 | prose | pages [19] -->
• Computational complexity. Although there are well-known algorithms to compute all measures, the computational complexity may be high, e.g. the time-consuming simulation in Task 5.

<!-- b000350 | prose | pages [19] -->
• Automatic adaptation. There are several non-parametric measures, which are chosen by users according to their own demands. Furthermore, we can only estimate the impact of parameters roughly. In short, there is no automatic parameter/measure-selection scheme.

<!-- b000351 | prose | pages [19] -->
• Inconsistency. The results generated by different measures are subject to the underlying personal values or perspectives, thus they may be inconsistent and there is no criterion for selecting the most appropriate one.

<!-- b000352 | prose | pages [19] -->
• Unrealistic assumptions. Some of our measures are based on unrealistic foundations, e.g.

<!-- b000353 | prose | pages [19] -->
eigenvector centrality only considers the giant connected component, the equiprobable property for message transmission usually does not hold in reality, etc., which results in imperfect characterization for the corresponding property.

<!-- b000354 | prose | pages [19] -->
• Incomplete assumptions. There are also some other perspectives where we cannot mea- sure the inﬂuence, such as reaching a given balance in terms of the degree centrality and the closeness centrality. Moreover, our model cannot resolve the existence of information cascade (go with the ﬂow, i.e. the most inﬂuential one is not always the best one) phenom- ena.

<!-- b000355 | heading | pages [19] -->
10 Conclusion

<!-- b000356 | prose | pages [19] -->
In this paper, we propose a complete process for handling network-based problems in reality. To start with, we roughly conclude that the condition for a real problem to be solved by network science in essence is that there is a network structure and something in interest transmitting through the network, and our real experiments conform to this statement. Then we can model the reality into directed/undirected graphs with vertices belonging to one/multi attribute(s), while the 2-D plotting of these graphs can be effectively handled by the stress majorization method. To follow next, we can adopt several insensitive non-parametric and parametric methods to evaluate the role, inﬂuence or importance for certain vertex from different perspectives.

<!-- b000357 | furniture | pages [20] -->
Team # 30221

<!-- b000358 | furniture | pages [20] -->
Page 20 of 20

<!-- b000359 | prose | pages [20] -->
Our simulation results show that the most inﬂuential co-author with Erd¨os generated by dif- ferent algorithms is consistent, no matter we focus on message transmission or the spilling-over inﬂuences. However, the co-bibliography method and directed graph method give differen- t important research papers, which are both supported according to the overall citation times provided by Google Scholar. Furthermore, our models and measures have nice performances when predicting the top singers and movie stars. Hence, this paper provides practical method- ologies for handling real network-based problems with moderately robust outputs, although deal them with caution due to its potential drawbacks.

<!-- b000360 | heading | pages [20] -->
References

<!-- b000361 | references | pages [20] -->
[1] E. R. Gansner, Y. Koren, S. North. Graph drawing by stress majorization. Graph Drawing.

<!-- b000362 | references | pages [20] -->
Springer Berlin Heidelberg, 2005: 239-250.

<!-- b000363 | references | pages [20] -->
[2] R. W. Floyd. Algorithm 97: shortest path. Communications of the ACM, 1962, 5(6): 345.

<!-- b000364 | references | pages [20] -->
[3] J. D. Leeuw. Convergence of the majorization method for multidimensional scaling. Journal

<!-- b000365 | references | pages [20] -->
of classiﬁcation, 1988, 5(2): 163-180.

<!-- b000366 | references | pages [20] -->
[4] M. E. Newman. Networks: an introduction. Oxford University Press, 2009.

<!-- b000367 | references | pages [20] -->
[5] R. Burden, and J. Faires. Numerical analysis. Cengage Learning, 2010.

<!-- b000368 | references | pages [20] -->
[6] R. K. Ahuja, T. L. Magnanti, J. B. Orlin. Network ﬂows: theory, algorithms, and applications.

<!-- b000369 | references | pages [20] -->
1993.

<!-- b000370 | references | pages [20] -->
[7] B. Bollob´as. Random graphs. Vol. 73. Cambridge university press, 2001.

<!-- b000371 | references | pages [20] -->
[8] L. Page, S. Brin, R. Motwani, et al. The PageRank citation ranking: bringing order to the

<!-- b000372 | references | pages [20] -->
web. 1999.
