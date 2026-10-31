# P-D-2021-2101855-c4682962

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
2021

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
D

<!-- b000007 | furniture | pages [1] -->
2101855

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
Measure of Inﬂuence and Similarity in Dynamic

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | title | pages [1] -->
Networks of Musicians

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
To measure the evolution and revolution of musicians’ community, our team intro- duces a model to quantify their identities across time based on the dynamic networks from interactions between musicians across time. The model contains three core parts: rescaled PageRank to measure inﬂuence, optimization of weighted cosine distance to measure similarity with time structure, and a comprehensive measure combing inﬂu- ence and similarity.

<!-- b000014 | prose | pages [1] -->
To measure importance of nodes in network more accurately, we improve the tradi- tional PageRank model by introducing a method of "rescaling". This is a method tak- ing corresponding nodes’ relative positions among contemporaries into account which

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
effectively solves the problem of time preference in the ordinary PageRank and allow us to compare inﬂuence of musicians vertically.

<!-- b000017 | prose | pages [1] -->
Then, based on musical characteristics of their works across time, we design a weighted cosine distance as the measure of similarity. And in order to determine the weight vector, we optimize the error function of MSE with its labels from the structure of networks by Stochastic Gradient Descent. Except from similarity of musical identi- ties from the same period, we also consider the potential lag effects of previous works in our model. This makes the similarity model precisely capture musicians within a same genre.

<!-- b000018 | prose | pages [1] -->
In addition, we conbime the similarity into rescaled PageRank model in order to making use of more information than indegree. With this update, our model can better overcome the problem of time-bias. Also, by the comparison of results between two measures, we are able to take a glimpse at the relationship between inﬂuence and simi- larity. And by evolution of inﬂuence and musical characteristics, we can also trace how a genre change over time with different positions in the network. Some cases studies are presented to show how it works.

<!-- b000019 | prose | pages [1] -->
Finally, we made some tests to check whether we can dig out more information from the graph structure by Graph Convolutional Network(GCN). Sensitivity analysis is also held to determine the width of average window in the process of rescaling. Strength and weakness of the model are also summarized for further imporving the measures.

<!-- b000020 | keywords | pages [1] -->
Keywords: Music classiﬁcation; Dynamic Social Networks; Rescaled PageRank;

<!-- b000021 | prose | pages [1] -->
Weight Cosine Similarity

<!-- b000022 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000023 | prose | pages [1] -->
关注数学模型

<!-- b000024 | furniture | pages [1] -->
2

<!-- b000025 | furniture | pages [1] -->
MATHmodels

<!-- b000026 | furniture | pages [1] -->
获取更多资讯

<!-- b000027 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000028 | heading | pages [2] -->
Contents

<!-- b000029 | contents | pages [2] -->
1 Introduction

<!-- b000030 | contents | pages [2] -->
4

<!-- b000031 | contents | pages [2] -->
1.1

<!-- b000032 | contents | pages [2] -->
Background

<!-- b000033 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
4

<!-- b000035 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000036 | contents | pages [2] -->
1.2

<!-- b000037 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
4

<!-- b000039 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000040 | contents | pages [2] -->
4

<!-- b000041 | contents | pages [2] -->
2.1

<!-- b000042 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
4

<!-- b000044 | contents | pages [2] -->
2.2

<!-- b000045 | contents | pages [2] -->
Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | contents | pages [2] -->
5

<!-- b000047 | contents | pages [2] -->
3 Benchmark Models and Overall Analysis

<!-- b000048 | contents | pages [2] -->
5

<!-- b000049 | contents | pages [2] -->
3.1

<!-- b000050 | contents | pages [2] -->
Framework of Musicians’ Social Network . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
5

<!-- b000052 | contents | pages [2] -->
3.1.1

<!-- b000053 | contents | pages [2] -->
Static Network

<!-- b000054 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
5

<!-- b000056 | contents | pages [2] -->
3.1.2

<!-- b000057 | contents | pages [2] -->
Dynamic Network . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
6

<!-- b000059 | contents | pages [2] -->
3.2

<!-- b000060 | contents | pages [2] -->
Measure of Inﬂuence: Time-Balanced Network Centrality . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
6

<!-- b000062 | contents | pages [2] -->
3.2.1

<!-- b000063 | contents | pages [2] -->
Model of Rescaled PageRank . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
6

<!-- b000065 | contents | pages [2] -->
3.2.2

<!-- b000066 | contents | pages [2] -->
Example from Subnetwork of the 80s

<!-- b000067 | contents | pages [2] -->
. . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
7

<!-- b000069 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000070 | contents | pages [2] -->
3.3

<!-- b000071 | contents | pages [2] -->
Measure of Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
8

<!-- b000073 | contents | pages [2] -->
3.3.1

<!-- b000074 | contents | pages [2] -->
Determine Weight Vector from Structure of Networks . . . . . . .

<!-- b000075 | contents | pages [2] -->
8

<!-- b000076 | contents | pages [2] -->
3.3.2

<!-- b000077 | contents | pages [2] -->
Time Structure of Similarity . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
9

<!-- b000079 | contents | pages [2] -->
3.3.3

<!-- b000080 | contents | pages [2] -->
Test of Validity of Similarity Metric . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
9

<!-- b000082 | contents | pages [2] -->
4 Relation between Inﬂuence and Similarity: Updated Rescaling PageRank

<!-- b000083 | contents | pages [2] -->
Model

<!-- b000084 | contents | pages [2] -->
9

<!-- b000085 | contents | pages [2] -->
4.1

<!-- b000086 | contents | pages [2] -->
Updated Rescaled PageRank Model

<!-- b000087 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
10

<!-- b000089 | contents | pages [2] -->
4.2

<!-- b000090 | contents | pages [2] -->
Relation between Similarity and Inﬂuence . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
10

<!-- b000092 | contents | pages [2] -->
4.2.1

<!-- b000093 | contents | pages [2] -->
Within Genres . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
10

<!-- b000095 | contents | pages [2] -->
4.2.2

<!-- b000096 | contents | pages [2] -->
Between Genres . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
11

<!-- b000098 | contents | pages [2] -->
4.3

<!-- b000099 | contents | pages [2] -->
A Case Study: Did Inﬂuencer Really Affect Followers?

<!-- b000100 | contents | pages [2] -->
. . . . . . . . . .

<!-- b000101 | contents | pages [2] -->
11

<!-- b000102 | contents | pages [2] -->
5 Evolution of Different Genres

<!-- b000103 | contents | pages [2] -->
12

<!-- b000104 | contents | pages [2] -->
5.1

<!-- b000105 | contents | pages [2] -->
Basis for Differentiating Genres . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
12

<!-- b000107 | contents | pages [2] -->
5.1.1

<!-- b000108 | contents | pages [2] -->
Size and Inﬂuence

<!-- b000109 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000110 | contents | pages [2] -->
12

<!-- b000111 | contents | pages [2] -->
5.1.2

<!-- b000112 | contents | pages [2] -->
Musical identity: Measure of Relationship between Genres . . . .

<!-- b000113 | contents | pages [2] -->
13

<!-- b000114 | contents | pages [2] -->
5.2

<!-- b000115 | contents | pages [2] -->
Identiﬁcation of Revolutions . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000116 | contents | pages [2] -->
14

<!-- b000117 | contents | pages [2] -->
5.2.1

<!-- b000118 | contents | pages [2] -->
Revolutions from Outer Part

<!-- b000119 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000120 | contents | pages [2] -->
14

<!-- b000121 | contents | pages [2] -->
5.2.2

<!-- b000122 | contents | pages [2] -->
Revolutions from Inner Part . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [2] -->
15

<!-- b000124 | contents | pages [2] -->
5.3

<!-- b000125 | contents | pages [2] -->
A Case Study: Evolution of Blue Music

<!-- b000126 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000127 | contents | pages [2] -->
16

<!-- b000128 | contents | pages [2] -->
6 Test and Sensitivity Analysis

<!-- b000129 | contents | pages [2] -->
17

<!-- b000130 | contents | pages [2] -->
6.1

<!-- b000131 | contents | pages [2] -->
Sensitivity Analysis on the Average Window of Rescaled PageRank . . .

<!-- b000132 | contents | pages [2] -->
17

<!-- b000133 | contents | pages [2] -->
6.2

<!-- b000134 | contents | pages [2] -->
Evidence from GCN: Can We Find More Information from the Structure

<!-- b000135 | contents | pages [2] -->
of Network? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000136 | contents | pages [2] -->
18

<!-- b000137 | contents | pages [2] -->
7 Strengths and Weaknesses

<!-- b000138 | contents | pages [2] -->
19

<!-- b000139 | contents | pages [2] -->
7.1

<!-- b000140 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000141 | contents | pages [2] -->
19

<!-- b000142 | contents | pages [2] -->
7.2

<!-- b000143 | contents | pages [2] -->
Weaknesses

<!-- b000144 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000145 | contents | pages [2] -->
20

<!-- b000146 | contents | pages [2] -->
8 Further Discussion

<!-- b000147 | contents | pages [2] -->
20

<!-- b000148 | contents | pages [2] -->
Letter

<!-- b000149 | contents | pages [2] -->
21

<!-- b000150 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000151 | contents | pages [2] -->
关注数学模型

<!-- b000152 | furniture | pages [2] -->
2

<!-- b000153 | furniture | pages [2] -->
MATHmodels

<!-- b000154 | furniture | pages [2] -->
获取更多资讯

<!-- b000155 | furniture | pages [2] -->
2

<!-- b000156 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000157 | furniture | pages [3] -->
Team # 2101855

<!-- b000158 | furniture | pages [3] -->
Page 3 of 23

<!-- b000159 | heading | pages [3] -->
References

<!-- b000160 | references | pages [3] -->
22

<!-- b000161 | heading | pages [3] -->
Appendix A: Information of Dynamic Networks

<!-- b000162 | prose | pages [3] -->
23

<!-- b000163 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000164 | heading | pages [3] -->
Appendix B: Namelist of "Benchmark" Artists in GCN

<!-- b000165 | prose | pages [3] -->
23

<!-- b000166 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000167 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000168 | prose | pages [3] -->
关注数学模型

<!-- b000169 | furniture | pages [3] -->
2

<!-- b000170 | furniture | pages [3] -->
MATHmodels

<!-- b000171 | furniture | pages [3] -->
获取更多资讯

<!-- b000172 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000173 | furniture | pages [4] -->
Team # 2101855

<!-- b000174 | furniture | pages [4] -->
Page 4 of 23

<!-- b000175 | heading | pages [4] -->
1 Introduction

<!-- b000176 | heading | pages [4] -->
1.1 Background

<!-- b000177 | prose | pages [4] -->
微信公众号：数学模型 Long been regarded as one of the most creative masterpieces of humankind, mu- sic plays an important role in every age with distinctly different genres and contents, while some masters’ works survived and inﬂuenced generations of musicians as well as listeners with their unique vitality.

<!-- b000178 | prose | pages [4] -->
Great works have their own identities, but beauty is their common denominator. New musicians learn from their predecessors, which could render some similarities between works across different times. But how musicians inﬂuenced each other? Did they learn more from those great artists or those more similar to their interest? Can we identify those revolutionary artists and events? These questions require us to discover the community structure of musicians for more information.

<!-- b000179 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000180 | heading | pages [4] -->
1.2 Restatement of the Problem

<!-- b000181 | heading | pages [4] -->
1. How to portray the dynamic community structure of musicians?

<!-- b000182 | heading | pages [4] -->
2. How to quantify the inﬂuence between different artists?

<!-- b000183 | heading | pages [4] -->
3. How to measure the similarity of creators by the characteristics of their works? How

<!-- b000184 | prose | pages [4] -->
to determine its relationship with inﬂuence?

<!-- b000185 | heading | pages [4] -->
4. What is the basis for distinguishing between genres?

<!-- b000186 | prose | pages [4] -->
5. With all the metrics above, how to trace the evolution and revolution of all the gen- res?

<!-- b000187 | heading | pages [4] -->
2 Assumptions and Notations

<!-- b000188 | heading | pages [4] -->
2.1 Assumptions

<!-- b000189 | prose | pages [4] -->
To simplify the analysis of our problem, we make the following assumptions, each of which is properly justiﬁed.

<!-- b000190 | heading | pages [4] -->
1. Assumed that for a connecting subgraph with less than 1% musicians compared to

<!-- b000191 | prose | pages [4] -->
the maximum connecting subgraph, it can be ignored during analysis due to its tiny contribution to the whole community of musicians.

<!-- b000192 | heading | pages [4] -->
2. Assumed that the interaction built up as soon as the follower got active.

<!-- b000193 | prose | pages [4] -->
3. Assumed that songs released in 1920s are classiﬁed into 1930s.

<!-- b000194 | heading | pages [4] -->
4. Assumed that songs released before the musicians active years make no difference

<!-- b000195 | prose | pages [4] -->
to the artist’s overall music style.

<!-- b000196 | heading | pages [4] -->
5. Assumed that one artist’s style can be represented by the average characteristics of

<!-- b000197 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000198 | prose | pages [4] -->
关注数学模型 his/her works every decade.

<!-- b000199 | furniture | pages [4] -->
2

<!-- b000200 | furniture | pages [4] -->
MATHmodels

<!-- b000201 | furniture | pages [4] -->
获取更多资讯

<!-- b000202 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000203 | furniture | pages [5] -->
Team # 2101855

<!-- b000204 | furniture | pages [5] -->
Page 5 of 23

<!-- b000205 | heading | pages [5] -->
6. Assumed that the inﬂuence of past works on the present musicians decays geomet-

<!-- b000206 | prose | pages [5] -->
rically.

<!-- b000207 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000208 | heading | pages [5] -->
2.2 Notations

<!-- b000209 | prose | pages [5] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000210 | caption | pages [5] -->
Table 1: Notations

<!-- b000211 | prose | pages [5] -->
Symbol Deﬁnition

<!-- b000212 | prose | pages [5] -->
nt Number of nodes in graph at period t mt Number of edges in graph at period t kt Average degree of graph at period t lt Average geodesic distance at period t d Diameter of graph N Set of nodes in the network 微信号：MATHmodels kin n,t, kout Indegree and outdegree of node n at period t n,t X Network data of the graph A Adjacency matrix of the graph Y Labels for musicians Sn Set of musician n’s works pn, Rn(p) PageRank Score and Rescaled PageRank score of musician n µn(p), σn(p) Mean and Standard Error of musician n in averaging window dis(n1, n2) Geodesic distance between n1 and n2 Sim(n1, n2) Similarity between n1 and n2 a Weight vector in determining similarity E Error term in training W(0), W(1) Weight matrices for hidden layers in GCN yL Set of node indices with labels in GCN γn Label for musician n from GCN

<!-- b000213 | heading | pages [5] -->
3 Benchmark Models and Overall Analysis

<!-- b000214 | heading | pages [5] -->
3.1 Framework of Musicians’ Social Network

<!-- b000215 | heading | pages [5] -->
3.1.1 Static Network

<!-- b000216 | prose | pages [5] -->
According to the data, it’s intuitively to build up a static social network by the existent interactions, which present many network identities that are common to other real social networks.Part of the network’s statistics are shown in Table 2.

<!-- b000217 | prose | pages [5] -->
During the data processing, we found that two pairs of musicians never built up any other relationships, while other 5599 musicians are on a connecting subgraph. Based on Assumption 1, these 4 musicians, Chuckii Booker and Mark Morrison with The Neptunes and Kaytranada are abandoned in our following analysis.

<!-- b000218 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000219 | prose | pages [5, 6] -->
关注数学模型 n m k l

<!-- b000220 | furniture | pages [5] -->
2

<!-- b000221 | furniture | pages [5] -->
MATHmodels

<!-- b000222 | furniture | pages [5] -->
获取更多资讯

<!-- b000223 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000224 | furniture | pages [6] -->
Team # 2101855

<!-- b000225 | furniture | pages [6] -->
Page 6 of 23

<!-- b000226 | caption | pages [6] -->
Table 2: Descriptive statistics of static network

<!-- b000228 | prose | pages [6] -->
Directed 5599 42768 7.639 1.333 微信公众号：数学模型 Undirected 5599 42729 7.632 3.724

<!-- b000229 | prose | pages [6] -->
Note: n is the Number of Nodes, m is the Num- ber of Edges, k is the Average Degree, l is the Mean Geodesic Distance.

<!-- b000230 | prose | pages [6] -->
Some very interesting phenomena can be observed. The difference between the number of edges is rather small, which shows that there is rather few two-way inﬂu- ence between musicians. At the same time, the average distance in directed graph is way shorter than that in undirected graph. The approaching-to-1 value represents that great stars often inﬂuenced others, while they weren’t inﬂuenced easily by his younger generations1. Contemporaries rarely inﬂuenced each other either.

<!-- b000231 | prose | pages [6] -->
微信号：MATHmodels This also shows the property of "small-world"[1]. Except from the small average distance, diameter of the undirected graph is 13 which is also relatively small com- pared to the scale of network.

<!-- b000232 | prose | pages [6] -->
This network can depict relationship between musicians in a way, though, it cares only about the relation of inﬂuence from the perspective of this decade, which is bound to aggrandize the importance of older generations. Also, it’s hard to observe the evo- lution of this community by a static network. All these reasons drive us to raise a dynamic network.

<!-- b000233 | heading | pages [6] -->
3.1.2 Dynamic Network

<!-- b000234 | prose | pages [6] -->
According to Assumption 3 as well as the characteristics of the data, all relation- ships built up at the beginning of each decade. Thus we can separate time between 1930-2010 into 9 periods. Remark 1930 as t0, the community can be regarded as a growing network with the continuous supplement of new musicians2. By the package of DyNext[3], such a network can be built up by Python. Figure 1 shows how the net- work evolved throuth t = 0, 1, 2. More information for each period is in the appendix.

<!-- b000235 | heading | pages [6] -->
3.2 Measure of Inﬂuence: Time-Balanced Network Centrality

<!-- b000236 | heading | pages [6] -->
3.2.1 Model of Rescaled PageRank

<!-- b000237 | prose | pages [6] -->
For a social network, it’s natural to gauge the inﬂuence of nodes by methods includ- ing centrality, Pagerank etc. However, traditional PageRank will meet several prob- lems in this question: 1. it ignores the time structure of the network, which could pro- duce unrealistic features[4]; 2. the redistribution of PageRank is temporally strongly biased towards old nodes[5], which makes the PageRank scores of new nodes from 10s

<!-- b000238 | prose | pages [6] -->
1All these phonomenon help explain the plausibility of Assumption 2, as there are very few young- sters affect older generations, it won’t make a big difference to the result.

<!-- b000239 | prose | pages [6] -->
2This can be checked by the data presented in the appendix and the pattern presented in [1] and [2], where edges grow faster than nodes, and bigger the network, smaller the diameter and average

<!-- b000240 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000241 | prose | pages [6] -->
关注数学模型 distance(In earlier period, most of musicians weren’t even on a same subgraph).

<!-- b000242 | furniture | pages [6] -->
2

<!-- b000243 | furniture | pages [6] -->
MATHmodels

<!-- b000244 | furniture | pages [6] -->
获取更多资讯

<!-- b000245 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000246 | furniture | pages [7] -->
Team # 2101855

<!-- b000247 | furniture | pages [7] -->
Page 7 of 23

<!-- b000248 | caption | pages [7] -->
Figure 1: Evolution of dynamic network

<!-- b000249 | prose | pages [7] -->
微信公众号：数学模型 (a) t=0 (b) t=1 (c) t=2

<!-- b000250 | prose | pages [7] -->
are all close to 0; 3. PageRank algorithm contains no more information than indegree of nodes[5], while in the adjacency matrix it simpliﬁes the inﬂuence from all inﬂuencers as the same( 1 kin), which doesn’t correspond to reality. For example, for a R&B singer like Terence Trent D’Arby who is inﬂuenced by Micheal Jackson and The Beatles at the same time, though, it’s hard to say they played an equal role in his process of growth. 微信号：MATHmodels Based on these ﬂaws, we raise a rescaled PageRank algorithm to capture the in- ﬂuence of music unbiasedly, which considers the relative position of corresponding musician among his/her contemporaries. By [6], it can be expressed in the following form: Rn(p) = pn −µn(p) (1) σn(p)

<!-- b000251 | prose | pages [7] -->
Here, p is calculated by ordinary PageRank algorithm from [7]. µn(p) and σn(p) are computed over musicians from the same genre j ∈[i −∆p/2, i + ∆p/2] in order to taking its relative position into account, where ∆p represents the scale of musicians in averaging window. Here, we take ∆p = 25 which is smaller than it used in [6] due to the smaller amount of musicians. However, it will meet some problem in processing artists from 10s, as there were very few musicians entering this community in the last decade. So when comparing the outcomes, it’s better to stick to the results before 2000s.

<!-- b000252 | heading | pages [7] -->
3.2.2 Example from Subnetwork of the 80s

<!-- b000253 | prose | pages [7] -->
As we’ve mentioned above, this network can be regarded as a growing network. So every period with t < 8 is a subnetwork of the ultimate one. Take 1980s as an example, the detailed information is in appendix A where t = 5. It’s a fast changing decade with a great many musicians entered the community and the interactions between musicians expanded at a surprising speed. These make it a good age for us to check our inﬂuence model.

<!-- b000254 | prose | pages [7] -->
Part of results from rescaled PageRank model are shown in Fig.2. From the dis- tribution of top 100 musicians, it’s clear that 80s is the time of pop music(like every decade) and black music(Jazz, R&B, Blues, Religious etc.). For other types of mu- sic, there appear lower proﬁles with great but less inﬂuential musicians including Kraftwerk(Electronic), Roy Acuff(Country) etc.

<!-- b000255 | prose | pages [7] -->
At the same time, the generations of these musicians are also evenly distributed. Artists from 40s were most actively affecting young musicians, where new generations and older generations all have their inﬂuence on their recipients. There is still pos-

<!-- b000256 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000257 | prose | pages [7, 8] -->
sibility of overestimating old nodes, but the overall results support the property of关注数学模型 time-balancing in rescaled PageRank.

<!-- b000258 | furniture | pages [7] -->
2

<!-- b000259 | furniture | pages [7] -->
MATHmodels

<!-- b000260 | furniture | pages [7] -->
获取更多资讯

<!-- b000261 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000262 | furniture | pages [8] -->
Team # 2101855

<!-- b000263 | furniture | pages [8] -->
Page 8 of 23

<!-- b000265 | caption | pages [8] -->
Figure 2: Distribution of Genres and Active Years for Top 100 Musicians in 1980s

<!-- b000266 | prose | pages [8] -->
微信公众号：数学模型 (a) Distribution of Genres (b) Distribution of Active Years

<!-- b000267 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000268 | heading | pages [8] -->
3.3 Measure of Similarity

<!-- b000269 | prose | pages [8] -->
To clarify the similarity between musicians by the charateristics of their works, it’s hard to process without genres as labels which disenables us to optimize the weight of different factors unless we simply regard they share same effects to different music genres. Therefore, to measure similarity, we need to ﬁgure out how music differs by all these identities ﬁrst.

<!-- b000270 | heading | pages [8] -->
3.3.1 Determine Weight Vector from Structure of Networks

<!-- b000271 | prose | pages [8] -->
Without extra information about labels, the structure of the dynamic networks ac- tually contains similarity. It’s natural to believe that musicians affected by similar mu- sicians and inﬂuenced similar musicians could have some common in their works.

<!-- b000272 | prose | pages [8] -->
Thus, from the information from networks, we build an adjusted weighted cosine distance to measure the similarity between musician n1 and n2:

<!-- b000273 | prose | pages [8] -->
Sim(n1, n2) = cos < axn1, axn2 > (2)

<!-- b000274 | prose | pages [8] -->
During training, we optimize weight vector a by minizing MSE in (3):

<!-- b000275 | prose | pages [8] -->
min E(a) = ∑ (ζ(n1, n2) −Sim(n1, n2))2 ∑ (3) n1∈N n2∈N,n2̸=n1

<!-- b000276 | prose | pages [8] -->
Where the label of samples are deﬁned by (2): { cos( dis(n1,n2) 1 ≤dis(n1, n2) ≤5 π) 12 ζ(n1, n2) = (4) dis(n1, n2) > 5 0

<!-- b000277 | prose | pages [8] -->
By the property of small-world, we consider the cosine similarity of nodes by its geodesic distance in the network. We don’t think for nodes whose distance above 5 still have similarities as it’s way bigger than the average distance even in the undirected network. So with geodesic distance below 6, we separate the space between [0, π 2 ] into 6 parts to get an "expected similarity". By minimizing the squared error between similarity and "expected similarity", we are able to ﬁgure out the optimized weight

<!-- b000278 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000279 | prose | pages [8] -->
关注数学模型 vector by stochastic gradient descent[8].

<!-- b000280 | furniture | pages [8] -->
2

<!-- b000281 | furniture | pages [8] -->
MATHmodels

<!-- b000282 | furniture | pages [8] -->
获取更多资讯

<!-- b000283 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000284 | furniture | pages [9] -->
Team # 2101855

<!-- b000285 | furniture | pages [9] -->
Page 9 of 23

<!-- b000286 | heading | pages [9] -->
3.3.2 Time Structure of Similarity

<!-- b000287 | prose | pages [9] -->
By Assumption 3 and 5, we are able to separate songs into different decades to analyze the transition of different elements. Based on data from "full_music_data.csv", 微信公众号：数学模型 we can express average characteristics of musician at period t by (5):

<!-- b000288 | prose | pages [9] -->
xnt = ∑snt∈Snt snt (5) |Snt|

<!-- b000289 | prose | pages [9] -->
, where snt represent the characteristics of his/her work in period t, and |Snt| is the amount of songs in the period(This process is headed on the basis of Assumption 4).

<!-- b000290 | prose | pages [9] -->
By model presented in (2)-(5), weight vector at can be ﬁgured out through each period again by stochastic gradient descent, from which the core features of music from different decades can be compared vertically by its importance represented in weight vector.

<!-- b000291 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000292 | heading | pages [9] -->
3.3.3 Test of Validity of Similarity Metric

<!-- b000293 | prose | pages [9] -->
It’s an exhausting work to check similarity between all pairs of musicians. To sim- plify it, we randomly pick 500 musicians every time from the network when t = 8. Then we compute similarity between each pairs and by their genres, we separately calculate the average similarity with genre and between genre.

<!-- b000294 | prose | pages [9] -->
By 10 rounds of iterations, it can be found from Fig.3 that almost in all samples, the average similarity within groups is all higher than that between groups for nearly 0.05. As the iterations have covered a great part of musicians, it substantiates that our metric of gauging similarity can distinguish between different genres of music.

<!-- b000295 | caption | pages [9] -->
Figure 3: Similarity within and between groups in ten iterations

<!-- b000296 | heading | pages [9] -->
4 Relation between Inﬂuence and Similarity: Updated

<!-- b000297 | heading | pages [9] -->
Rescaling PageRank Model

<!-- b000298 | prose | pages [9] -->
To check the relationship between inﬂuence and similarity among musicians, it’s hard to compare directly. At the same time, methods like regression analysis are not available due to the dynamic structure. So we need to optimize our PageRank model

<!-- b000299 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000300 | prose | pages [9] -->
关注数学模型 again with more information about similarity except from just rescaling it.

<!-- b000301 | furniture | pages [9] -->
2

<!-- b000302 | furniture | pages [9] -->
MATHmodels

<!-- b000303 | furniture | pages [9] -->
获取更多资讯

<!-- b000304 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000305 | furniture | pages [10] -->
Team # 2101855

<!-- b000306 | furniture | pages [10] -->
Page 10 of 23

<!-- b000307 | heading | pages [10] -->
4.1 Updated Rescaled PageRank Model

<!-- b000308 | prose | pages [10] -->
First, we’d like to check ordinary PageRank adjacency matrix. For a node n1 in network, its corresponding element in initial matrix with node n2 that inﬂuences is 微信公众号：数学模型 1 represented by An1,n2 = n1,t. kout

<!-- b000309 | prose | pages [10] -->
However, there is actually another assumption beneath in this network using inde- gree as the basis of inﬂuence: every musician is equally affected by all his inﬂuencers. And we don’t regard this true. So we use similarity to replace the degree. Here, we build a new adjacency matrix denoted by ¯A which goes like:

<!-- b000310 | prose | pages [10] -->
Sim(n1, n2) ¯An1,n2 = (6) ∑n i=2 Sim(n1, ni)

<!-- b000311 | prose | pages [10] -->
Here, adjacency matrix presented in (6) ﬁgures out the third problem discussed in ordinary PageRank. Also, as the similarity is time-varying in different decades, we’re able to consider the lag effects from inﬂuencers. Again, we can update this ¯A as: 微信号：MATHmodels t Simj(n1, n2) βt−j ¯Atn1,n2 = ∑ (7) ∑n i=2 Simj(n1, ni) j=0

<!-- b000312 | prose | pages [10] -->
Where β is the discount factor of decades from Assumption 6. Here, the matrix contains more information about similarity as well the inﬂuence from time. And by rescaled PageRank algorithm above with the updated adjacency matrix, we can get inﬂuence that considers similarity.

<!-- b000313 | prose | pages [10] -->
After processing, some of results are presented in 4 below. And by comparing it with results from 3.3.2, we can consider the effects from similarity and inﬂuence comprehensively.

<!-- b000314 | caption | pages [10] -->
Figure 4: Revised Distribution of Genres and Active Years for Top 100 Musicians in 1980s

<!-- b000315 | prose | pages [10] -->
(a) Distribution of Genres (b) Distribution of Active Years

<!-- b000316 | heading | pages [10] -->
4.2 Relation between Similarity and Inﬂuence

<!-- b000317 | heading | pages [10] -->
4.2.1 Within Genres

<!-- b000318 | prose | pages [10] -->
In the rescaling process, we’ve considered characteristics within the genre. The

<!-- b000319 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000320 | prose | pages [10, 11] -->
rescaled PageRank actually represents the relative position of musician in its genre in关注数学模型 a way. And by researching the distribution of the age of musicians can help ﬁnd their time-balancing effects within genres.

<!-- b000321 | furniture | pages [10] -->
2

<!-- b000322 | furniture | pages [10] -->
MATHmodels

<!-- b000323 | furniture | pages [10] -->
获取更多资讯

<!-- b000324 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000325 | furniture | pages [11] -->
Team # 2101855

<!-- b000326 | furniture | pages [11] -->
Page 11 of 23

<!-- b000328 | prose | pages [11] -->
From Fig.2b, where inﬂuence is represented by "the amount of juniors one inﬂu- ences", it can be observed that even under rescaled indicator, old musicians’ inﬂuence 微信公众号：数学模型 is tend to be bigger. This is natural – more experienced artists deserve higher status.

<!-- b000329 | prose | pages [11] -->
While after considering similarity, it concerns more about prevalence now. It’s hard to learn from works decades ago though, fad of the moment will be more often imi- tated. So similarity actually measures the degree of impact as shown in Fig.4b. More musicians that deﬁned styles at his/her time are emphasized in the updated model so younger musicians appear more in Top 100. This shows our measure contains both sides of inﬂuence.

<!-- b000330 | heading | pages [11] -->
4.2.2 Between Genres

<!-- b000331 | prose | pages [11] -->
The impact between genres can be shown in importance of different genres. Com- 微信号：MATHmodels paring genres presented in Fig.2a and Fig.4a, tiny increase in share of Pop/Rock and black music can be observed in updated model. Both model fail to capture those miche genres. So, though we can distinguish genres by similarity in a way, it doesn’t deter- mine difference between genres.

<!-- b000332 | prose | pages [11] -->
This shows the degree of mainstreaming of genre determines its inﬂuence. While similarity’s effect is less common. It may perform an essential role in creating though, listeners could prefer music that’s more mainstream and similar to mainstream music.

<!-- b000333 | prose | pages [11] -->
4.3 A Case Study: Did Inﬂuencer Really Affect Followers?

<!-- b000334 | prose | pages [11] -->
From observations presented in 4.2.1, it can be found that the similarity between musicians is not fully measured when only inﬂuence is considered in PageRank. In order to identify whether the musicians have actually inﬂuenced each other, we need to take a closer look at the similarities between different musicians.

<!-- b000335 | prose | pages [11] -->
Take John Williams(Stage & Screen) and Lambert, Hendricks & Ross(Jazz) as ex- amples, who were both inﬂuenced by many musicians across periods as well as contin- uously affected newcomers. In Table 3, we presented their average change on musical characteristics from t = 1 to 3 compared to those when t = 1, and their average differ- ence from their inﬂuencers to check if there existed some kind of correlation.

<!-- b000336 | caption | pages [11] -->
Table 3: Average Change in Percent of Identities for Musicians and Inﬂuencers in 40s

<!-- b000337 | prose | pages [11] -->
Char 1 2 3 4 5 6 7 8 9 10 11 12

<!-- b000338 | prose | pages [11] -->
John -3.3 50.2 13.9 -4.5 -23.6 150 50 -15.9 -25 28.3 0.3 -2.9 John’s 2.3 -32 18.5 -6 20.3 50 72.5 3.6 -0.9 -14.4 0.4 27 Inﬂ-er Ross 24 22.5 95.6 -27.5 -23.6 -33 + -18.9 + 32.7 91 1.5 Ross’s 18 6.3 102 -5.6 -23.1 0 + -2.3 + 96.2 27 -3.8 Inﬂ-er

<!-- b000339 | prose | pages [11] -->
Percent change of identities except from "Popularity" are presented above. "+"

<!-- b000340 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000341 | prose | pages [11, 12] -->
means that the element in the corresponding position is equal to or close to 0 in 40s. It关注数学模型 can be observed that between musicians and their inﬂuencers, musical characteristics tend to change in the same direction and scale, while for type of vocals, they don’t always change in unison.

<!-- b000342 | furniture | pages [11] -->
2

<!-- b000343 | furniture | pages [11] -->
MATHmodels

<!-- b000344 | furniture | pages [11] -->
获取更多资讯

<!-- b000345 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000346 | furniture | pages [12] -->
Team # 2101855

<!-- b000347 | furniture | pages [12] -->
Page 12 of 23

<!-- b000349 | prose | pages [12] -->
Besides, different genres emphasize different identities in mutually inﬂuencing. For 微信公众号：数学模型 example, bigger change had taken place in Valence and Tempo for Jazz compared to Stage & Screen music. This is also correlated to the evolution of music genres.

<!-- b000350 | prose | pages [12] -->
However, this kind of relation may not always exist. Though as we shown in Fig.3, in samples the average similarity is between 0.6-0.7. However, if we calculate all simi- larity between all pairs of musicians with inﬂuence relation, the average is about 0.802. And the distribution from 5 shows there are some relations whose similarity are ex- tremely low. Thus, in general this pattern holds, but there may be deviations in indi- vidual samples.

<!-- b000351 | caption | pages [12] -->
Figure 5: Overall Distribution of Similarities among Musicians

<!-- b000352 | prose | pages [12] -->
微信号：MATHmodels However, we can conclude from this case study, that inﬂuence really entered into force for followers especially on musical identities in most cases. And for different genres and periods, there existed totally different contagious characteristics. This asks us to analyze the overall muscial identities of genres across time.

<!-- b000353 | heading | pages [12] -->
5 Evolution of Different Genres

<!-- b000354 | heading | pages [12] -->
5.1 Basis for Differentiating Genres

<!-- b000355 | prose | pages [12] -->
To separate different genres, there are at least 3 factors to be considered: its size, inﬂuence and musical identities.

<!-- b000356 | heading | pages [12] -->
5.1.1 Size and Inﬂuence

<!-- b000357 | prose | pages [12] -->
By the updated rescaled PageRank discussed above, dynamic rank of musicians can be ﬁgured out. Combining information from the same genre, its size and average inﬂuence can be used to determine whether it’s a mainstream or a niche genre.

<!-- b000358 | prose | pages [12] -->
Some important features can be found in Fig.6: Blues music lost its proportion while at the same time it lost its inﬂuence. Pop/Rock gradually takes its dominating position. And during its process of expanding, its average inﬂuence rank increases. However, electronic music exploded from the end of 20th century with its inﬂuence

<!-- b000359 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000360 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型 dropped in a sudden due to its miche position and the newcomers diluted the average impact of it.

<!-- b000361 | furniture | pages [12] -->
2

<!-- b000362 | furniture | pages [12] -->
MATHmodels

<!-- b000363 | furniture | pages [12] -->
获取更多资讯

<!-- b000364 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000365 | furniture | pages [13] -->
Team # 2101855

<!-- b000366 | furniture | pages [13] -->
Page 13 of 23

<!-- b000367 | caption | pages [13] -->
Figure 6: Size and Inﬂuence of Pop/Rock, Blues and Electronic

<!-- b000369 | prose | pages [13] -->
微信号：MATHmodels So, comprehensively analyzing size and inﬂuence of a genre helps us determine the status of it from its scale and structure of musicians. But for creators, music character- istics are the core of distinguish.

<!-- b000370 | heading | pages [13] -->
5.1.2 Musical identity: Measure of Relationship between Genres

<!-- b000371 | prose | pages [13] -->
By different weight vector across different periods, we are able to calculate the aver- age cosine distance of one speciﬁc genre to represent whether the genre is more similar to others or is more common among genres by its average musical characteristics. The relationships can also be observed from the similarity path between two genres.

<!-- b000372 | prose | pages [13] -->
By vertically comparison of this indicator across periods, we can observe whether the corresponding musical forms have become more homogeneous or more distinctive. For example, the result of Pop/Rock music is shown in Fig.7:

<!-- b000373 | caption | pages [13] -->
Figure 7: Total Similarity between Pop/Rock and Other Genres

<!-- b000374 | prose | pages [13] -->
It can be found that during the process of Pop/Rock music getting popular in 40- 60s, it also got more similar to other genres rapidly. Causality may also be reversed, its pravalence could render other genres learning from it, so its assimilation could also come from its inﬂuence. But one thing is for sure that, the higher it’s status, the more

<!-- b000375 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000376 | prose | pages [13, 14] -->
similar it is also to other genres. 关注数学模型 Combining Fig.6 and 7, we can trace how genres change over time with its size, inﬂuence and its overall characteristics of music.

<!-- b000377 | furniture | pages [13] -->
2

<!-- b000378 | furniture | pages [13] -->
MATHmodels

<!-- b000379 | furniture | pages [13] -->
获取更多资讯

<!-- b000380 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000381 | furniture | pages [14] -->
Team # 2101855

<!-- b000382 | furniture | pages [14] -->
Page 14 of 23

<!-- b000384 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000385 | heading | pages [14] -->
5.2 Identiﬁcation of Revolutions

<!-- b000386 | prose | pages [14] -->
According to literatures [9] in terms of music history, we could ﬁnd two sources of revolution – the inner part and the outer part. For the inner part, new generations brought in new blood and spread inside the musician network. For the outer part, issues including social and political events, technology development, etc., emerged outside the network and resulted in exogenous inﬂuence.

<!-- b000387 | heading | pages [14] -->
5.2.1 Revolutions from Outer Part

<!-- b000388 | prose | pages [14] -->
Some of the exogenous shocks are so signiﬁcant that result in an overall change in music, which could be identiﬁed by the general trend from data_by_year.csv or the 微信号：MATHmodels weight vector we generated. We think the sharp change in overall music characteristics at a certain period could be a signal. And some main revolutions are listed below:

<!-- b000389 | prose | pages [14] -->
1. Acousticness & Instrumentness: The importance of acousticness was greatly weak- ened in 60s with the rise of electronic music, when the Columbia - Princeton Elec- tronic Music Lab was established in 50s. While at the same time instrumentness decreased which shows vocal played a more important role as the popularity of synthesizer technology actually endowed vocal with the property of instruments.

<!-- b000390 | prose | pages [14] -->
This observation is supported by the fact from Fig.8 that the average acousticness of electronic music is 0.233 while that of whole sample is 0.414. At the same time, genres that are not technologically sensitive(Classical, Vocal etc.) appeared more stable in the changing trend of acousticness.

<!-- b000391 | caption | pages [14] -->
Figure 8: Evolution of Acousticness of Genres

<!-- b000392 | heading | pages [14] -->
2. Energy & Valence: During more turbulent phases of the world, the valence of music

<!-- b000393 | prose | pages [14] -->
dropped. This can be observed through World Wars(30s-50s) and periods around 2008 Financial Crisis(00s-10s). While at a relatively peaceful period, music tended to be more energetic. That’s probably why Rock music expanded rapidly through 50s-70s as shown in Fig.6.

<!-- b000394 | heading | pages [14] -->
3. Duration: From the beginning of 21th century, the average duration of music dropped

<!-- b000395 | prose | pages [14] -->
faster than ever. This could be rendered by the rise of platforms including TikTok

<!-- b000396 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000397 | prose | pages [14] -->
关注数学模型 and so on which made people less patient for longer music.

<!-- b000398 | furniture | pages [14] -->
2

<!-- b000399 | furniture | pages [14] -->
MATHmodels

<!-- b000400 | furniture | pages [14] -->
获取更多资讯

<!-- b000401 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000402 | furniture | pages [15] -->
Team # 2101855

<!-- b000403 | furniture | pages [15] -->
Page 15 of 23

<!-- b000404 | heading | pages [15] -->
5.2.2 Revolutions from Inner Part

<!-- b000405 | prose | pages [15] -->
Sometimes, musicians beneﬁt from their innate ingenuity or personal experience, thus contributes or even reshaped the music world. They, correspondingly, might be- 微信公众号：数学模型 come legends whose masterpieces inspire future generations. According to our model and the given data, we believe a revolutionary should meet up with the following three standards:

<!-- b000406 | prose | pages [15] -->
1. He/She should be inﬂuential, having a high inﬂuence rank. Chances are a musician was claimed to be inﬂuential, but the followers actually don’t share many common features with him or her. The measure of inﬂuence take similarity into considera- tion, which indicates a more reliable impact. Musicians with higher inﬂuence rank include Muddy Waters, Billie Holiday, Lester Young, Elvis Presley, etc., which also correspond to our common sense.

<!-- b000407 | prose | pages [15] -->
2. He/She should deﬁne a style, that is, determine the developing direction of his or her genre in some period. According to the data, we may take notice of the trend 微信号：MATHmodels of a musician whose moving pattern is similar to that of the whole genre, especially leading it. This criteria is critical, since pieces of music might be signiﬁcantly differ- ent from its original genre, while seldom musicians follow those attempts. We won’t consider them to be revolutionary.(The trend of genre would exclude the musician itself)

<!-- b000408 | heading | pages [15] -->
3. He/She/They should be distinguishable, which means being different from his or

<!-- b000409 | prose | pages [15] -->
her pioneers. However, this criterion is not feasible out of two reasons. Firstly, we have some inefﬁcient musical identities for us to measure, such as melody. Thus, similarity in the given features including danceability, energy, etc., doesn’t neces- sarily mean similarity between two whole pieces of music. Secondly, proportion of inﬂuential musicians become active at the beginning of 30s and they dont have any pioneers in this data.

<!-- b000410 | prose | pages [15] -->
In consideration of his/her inﬂuence and the leading role of genres average trend, we mainly regard the top 5 musicians to be revolutionaries by characteristics shown in Fig.9, among them are Billie Holiday, Muddy Waters, Bob Dylan, The Beatles, and Little Richard.

<!-- b000411 | prose | pages [15] -->
For example, Billie Holiday has a second highest inﬂuence among all the musicians, and we can recognize an explicit similarity between the trend of her and other musi- cians in vocal. E.g. valence, tempo, key. We assume that she is especially revolutionary in 1930-40s, according to the Fig.9a .

<!-- b000412 | caption | pages [15] -->
Figure 9: Comparison of Characteristics between Revolutionaries and Average Trend

<!-- b000413 | prose | pages [15] -->
(a) Billie Holiday (b) Muddy Waters (c) Bob Dylan

<!-- b000414 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000415 | prose | pages [15, 16] -->
关注数学模型 微信公众号：数学模型 (a) The Beatles (b) Little Richard

<!-- b000416 | furniture | pages [15] -->
2

<!-- b000417 | furniture | pages [15] -->
MATHmodels

<!-- b000418 | furniture | pages [15] -->
获取更多资讯

<!-- b000419 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000420 | furniture | pages [16] -->
Team # 2101855

<!-- b000421 | furniture | pages [16] -->
Page 16 of 23

<!-- b000423 | heading | pages [16] -->
5.3 A Case Study: Evolution of Blue Music

<!-- b000424 | prose | pages [16] -->
Here we choose Blues for our case study based on the following reasons: (1)Its amount of musicians remains relatively stable which beneﬁts visualization; (2).A sig- niﬁcant number of inﬂuential musicians rose from it; (3)It has a deep cultural back- ground and is strong correlated with social campaigns.

<!-- b000425 | prose | pages [16] -->
微信号：MATHmodels Based on what we’ve discussed in 5.1, ﬁrst we take a look at its inﬂuence present in Fig.11. Its overall popularity, average inﬂuence of top 5 musicians were increasing through 40s-90s, which shows the old generations were getting more and more inﬂuen- tial which can also been observed in Fig.12.3 However, the number of active musicians didn’t increase much, while at the same time the average inﬂuence of all and last 5 musicians even decreased a bit. These shows Blues gradually lost its vitality without inﬂuential newcomers where the bottom right corner of the network had always been rather sparse.

<!-- b000426 | caption | pages [16] -->
Figure 11: Evolution of Inﬂuence and Popularity of Blues from 40s-90s

<!-- b000427 | caption | pages [16] -->
Figure 12: Social Network of Blues Musicians from 40s-90s

<!-- b000428 | prose | pages [16] -->
3We don’t discuss periods after 2000 here as there are few new Blues musicians then.

<!-- b000429 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000430 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型 While for the genre’s musical identities, based on discussion in 5.2, it can be found in Fig.14 as we predicted, its energy increased with the rise of Jumps Blues from Louis Jordan after 30s. Which inﬂuenced rockers including Chuck Berry in a way later.

<!-- b000431 | furniture | pages [16] -->
2

<!-- b000432 | furniture | pages [16] -->
MATHmodels

<!-- b000433 | furniture | pages [16] -->
获取更多资讯

<!-- b000434 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000435 | furniture | pages [17] -->
Team # 2101855

<!-- b000436 | furniture | pages [17] -->
Page 17 of 23

<!-- b000438 | prose | pages [17] -->
At the same time, its acousticness and sharply decreased after 50s. It’s the age of Chicago Blues(B.B.King). In 60s, Paul Butterﬁeld and British Blues rose with less in- strumental elements in music, which rendered sharp drop of instrumentness in 60s.[10]

<!-- b000439 | prose | pages [17] -->
However, the length of Blues music kept increasing. This is probably rendered 微信号：MATHmodels by the development of recording techniques that allowed more works to be recorded rather than only being performed live as it once was.

<!-- b000440 | caption | pages [17] -->
Figure 14: Evolution of Musical Identities of Blues from 40s-90s

<!-- b000441 | prose | pages [17] -->
From the case oF Blues above, we’ve shown how the music is changed with the external circumstances across time. Also, changes can be identiﬁed in the model by all means: social environment changed people’s aesthetic tastes, political factors inﬂu- enced the popularity of genres and the content of music, while technological improve- ments changed music in its propogation channels as well as its methods of creating. All these could be observed based on our inﬂuence and similarity indicators as well as the musicial characteristics of all genres.

<!-- b000442 | heading | pages [17] -->
6 Test and Sensitivity Analysis

<!-- b000443 | heading | pages [17] -->
6.1 Sensitivity Analysis on the Average Window of Rescaled PageR-

<!-- b000444 | prose | pages [17] -->
ank

<!-- b000445 | prose | pages [17] -->
As discussed above, due to the limitation of the amount of musicians, the average window is narrower in (1) that discussed in [6]. How to determine the value of ∆p is needed to be discussed. The best way to determine it is to research its effect to its property of "Time-Balanced". Therefore, we observe how the mean and standard

<!-- b000446 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000447 | prose | pages [17] -->
关注数学模型 deviation of R30s(p) change under different ∆p shown in Fig.15.

<!-- b000448 | furniture | pages [17] -->
2

<!-- b000449 | furniture | pages [17] -->
MATHmodels

<!-- b000450 | furniture | pages [17] -->
获取更多资讯

<!-- b000451 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000452 | furniture | pages [18] -->
Team # 2101855

<!-- b000453 | furniture | pages [18] -->
Page 18 of 23

<!-- b000454 | prose | pages [18] -->
As presented in Fig.15a, with the increase of ∆p, the mean is converging to 0 and this process of rescaled actually turns into standardization, this will make R(p) lose its ability of horizontally compared with musicians from the same age. At the same time, standard deviation of R(p) increases. When ∆p approaches 0, R(p) →p, the process 微信公众号：数学模型 can’t reverse the overestimation of old nodes.

<!-- b000455 | prose | pages [18] -->
So, a moderate value for ∆p is necessary. From the pattern of mean and standard deviation, we suppose that ∆p ∈[20, 35] may have a good time-balanced effect without weakening the ability of comparing horizontally.

<!-- b000456 | caption | pages [18] -->
Figure 15: Effect of Different ∆p

<!-- b000457 | prose | pages [18] -->
微信号：MATHmodels (a) Mean (b) Standard Deviation

<!-- b000458 | heading | pages [18] -->
6.2 Evidence from GCN: Can We Find More Information from the

<!-- b000459 | prose | pages [18] -->
Structure of Network?

<!-- b000460 | prose | pages [18] -->
In training process of getting weight vectors above, we discovered information from distance between nodes in the networks. However, with twenty types of music genres, in (4) we actually implicitly assumed that there only exists 6 different types in the real distribution of musicians. So we need to check if the structure of network itself contains enough information for us to separate it into twenty types. However, ordinary unsupervised learning methods including K-Means++, PCA and spectral decomposi- tion meet a failure to work due to the multiple of types, limited music characteristics and the property of small-world, which are even hard for us to ﬁnd clustering centers by all rules[11].

<!-- b000461 | prose | pages [18] -->
This drives us to raise a semi-supervised approach with model of neural networks which contains a little bit more information than our measure of similarity to check the idea. By the average PageRank score4 through their active years, twenty artists are picked out representing their genres. Among these musicians, there are The Beatles, T-Bones Walker, Roy Acuff etc. The full namelist is in the Table 5. With 20 labels, semi- supervised learning can be held based on analysis of graph structure to generate labels barely correlated with genres.

<!-- b000462 | prose | pages [18] -->
Based on [12], consider a two-layer GCN presented in forward model (8) and cross

<!-- b000463 | prose | pages [18] -->
4Though it’s not a better measure, it allows us to pick out musicians with great accumulative inﬂu- ence who are tend to affect more younger generations.

<!-- b000464 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000465 | prose | pages [18, 19] -->
关注数学模型 entropy error (9):

<!-- b000466 | furniture | pages [18] -->
2

<!-- b000467 | furniture | pages [18] -->
MATHmodels

<!-- b000468 | furniture | pages [18] -->
获取更多资讯

<!-- b000469 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000470 | furniture | pages [19] -->
Team # 2101855

<!-- b000471 | furniture | pages [19] -->
Page 19 of 23

<!-- b000473 | prose | pages [19] -->
Z = f (X, A) = so f tmax( ˆAReLU( ˆAXW(0))W(0)) (8)

<!-- b000474 | prose | pages [19] -->
微信公众号：数学模型 E = ∑ l∈yL ∑ FYl f ln Zl f (9) f =1

<!-- b000475 | prose | pages [19] -->
2. W(0) ∈RC×H is Where A is a symmetric adjacency matrix and ˆA = ˜D−1 2 ˜A ˜D−1 input-to-hidden weight matrix with H feature maps and W(1) ∈RH×F is hidden-to- output weight matrix. Some of principles are presented in Fig.16a. Again, by stochastic gradient descent, the weights matrices can be trained to ﬁnd the label.

<!-- b000476 | prose | pages [19] -->
By TensorFlow[13] we can calculate the labels for nodes in a relatively low time complexity. Some of clustering results are shown in Fig.16b. It can be found that the model has a relatively good recognition of mainstream genres, while it still can identify the genres with few musicians. This is probably because that most musicians were eas- 微信号：MATHmodels ily affected by pop stars even he/she had a different style. This endows the model with great ability of identifying Pop/Rock. Therefore, though it’s hard to determine miche music style in both models, less sample labels actually help reducing the misspeciﬁ- cation from overestimating the role of Pop/Rock music, as the network itself doesn’t contain enough information of doing so. This also supports the reasonableness of (4).

<!-- b000477 | caption | pages [19] -->
Figure 16: Principles and Results for GCN

<!-- b000478 | prose | pages [19] -->
(a) Graph Convolutional Network(Source:[12]) (b) Results from GCN

<!-- b000479 | heading | pages [19] -->
7 Strengths and Weaknesses

<!-- b000480 | heading | pages [19] -->
7.1 Strengths

<!-- b000481 | prose | pages [19] -->
• With a dynamic network, we consider a growing community of musicians which allows us to understand the evolution of musicians comprehensively.

<!-- b000482 | prose | pages [19] -->
• We measure the similarity from maximising the information in their community interactions, musical identities of works as well as the temporal characteristics which can make a good distinct between different genres overall.

<!-- b000483 | prose | pages [19] -->
• We modify the time-biased PageRank model and its measure of node importance was further optimised with a similarity metric that better represents the interplay

<!-- b000484 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000485 | prose | pages [19] -->
关注数学模型 between musicians.

<!-- b000486 | furniture | pages [19] -->
2

<!-- b000487 | furniture | pages [19] -->
MATHmodels

<!-- b000488 | furniture | pages [19] -->
获取更多资讯

<!-- b000489 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000490 | furniture | pages [20] -->
Team # 2101855

<!-- b000491 | furniture | pages [20] -->
Page 20 of 23

<!-- b000492 | prose | pages [20] -->
• We conducted detailed case studies, tests as well as sensitivity analysis to fully ensure the reasonableness and validity of our model.

<!-- b000493 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000494 | heading | pages [20] -->
7.2 Weaknesses

<!-- b000495 | prose | pages [20] -->
• Due to the limitation of data about musicians and their works, we can only mea- sure similarity and inﬂuence every decade, which may weaken the accuracy of the model without capturing more delicate dynamic information.

<!-- b000496 | prose | pages [20] -->
• Exogenous shock can be observed by outcomes presented by our model though, we don’t consider it in designing which could render bias in the ultimate rank of musicians across periods under different circumstances.

<!-- b000497 | heading | pages [20] -->
8 Further Discussion

<!-- b000498 | prose | pages [20] -->
微信号：MATHmodels In this project, we raised a measure of musicians’ inﬂuence by their importance in community and interactions between them. However, it should be noticed that based on the limitation of data, we had to make some assumptions that may not be too real- istic. They could reduce the credibility of our model. And provided with the following types of data, we can We can improve our model to better explore the patterns in the musician community:

<!-- b000499 | heading | pages [20] -->
1. Data of Lyrics: Though we traced the revolution of genres by its overall charac-

<!-- b000500 | prose | pages [20] -->
teristics, it’s hard to analyze its contents without lyrics especially for genres with relevance. Therefore, with data of lyrics, we can use methods including semantic analysis and sentiment analysis to show how ideas change in music, in order to bet- ter explore the relationship between musicians’ community inﬂuences and social inﬂuences.

<!-- b000501 | prose | pages [20] -->
2. Data of Audio: In the project, we are provided with overall indicators about charac- teristics of musicians’ works. However, it is difﬁcult to discover the true similarities between the works through these quantitative indicators. If we could have audio information about these songs, algorithms including MFCC[14] and so on could be used to explore interactions between musicians better.

<!-- b000502 | prose | pages [20] -->
Overall, however, this model closely matches the data provided, and we believe with more data, it is bound to play a greater role in the future of related analysis.

<!-- b000503 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000504 | prose | pages [20] -->
关注数学模型

<!-- b000505 | furniture | pages [20] -->
2

<!-- b000506 | furniture | pages [20] -->
MATHmodels

<!-- b000507 | furniture | pages [20] -->
获取更多资讯

<!-- b000508 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000509 | furniture | pages [21] -->
Team # 2101855

<!-- b000510 | furniture | pages [21] -->
Page 21 of 23

<!-- b000511 | heading | pages [21] -->
Letter

<!-- b000512 | prose | pages [21] -->
To: Integrative Collective Music Society 微信公众号：数学模型 From: Team 2101855 Date: February 8th, 2021 Subject: A better measure of music’s inﬂuence: updated rescaled PageRank

<!-- b000513 | prose | pages [21] -->
In the memo, we want to introduce you an alternate measure of music’s inﬂuence: updated rescaled PageRank. In fact, the PageRank has been used in measuring the importance of nodes in a network for long. However, it encounters some problem in tracing the evolution of music. Thus, we make the following imporvements to it.

<!-- b000514 | prose | pages [21] -->
Firstly, by taking corresponding nodes’ relative positions among contemporaries into account, we solve the problem of time-bias in growing networks including musi- cians’ community.

<!-- b000515 | prose | pages [21] -->
Secondly, we design a measure of similarity based on musical identities of musi- 微信号：MATHmodels cians’ works combining the structure of networks. And this measure has proven useful in ﬁnding musicians from the same genre.

<!-- b000516 | prose | pages [21] -->
Lastly, we replace the indegree in rescaled PageRank by similarity estimated above. This endows the model with more information from musical characteristics with a better effect of reversing time-bias.

<!-- b000517 | prose | pages [21] -->
By the measure above and corresponding tests, we’ve substantiated the effective- ness of our measure. Case studies are also held to illustrate the relationship between inﬂuence and similarity as well as how to trace the evolution and revolution of these genres by our approaches.

<!-- b000518 | prose | pages [21] -->
However, we admit that our method still have some ﬂaws more or less. The biggest problem among them is the limitation of data. Without data of new musicians, it’s hard to research into the network after 2000, which could also render bias in result from different periods.

<!-- b000519 | prose | pages [21] -->
In addition, the overview indicators of musical characteristics make it hard to ﬁnd more information from songs themselves. For example, it we have data about lyrics, we can trace the evolution of songs’ contents which reﬂect the trend of thoughts by algorithms for semantic analysis and sentiment analysis. And more detailed audio information about music can help more precisely compare similarities between genres with algorithms including MFCC etc.

<!-- b000520 | prose | pages [21] -->
After all, I believe that with our update, the rescaled PageRank algorithm is com- patible with the speciﬁcity of the musician community and captures the evolution of each genre effectively. We think it’s quite a useful tool for us to know about musi- cians as well the culture. So we wholeheartedly hope you consider our measure, and hopefully it will come in handy in real life applications.

<!-- b000521 | prose | pages [21] -->
Thank you!

<!-- b000522 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000523 | prose | pages [21] -->
关注数学模型

<!-- b000524 | furniture | pages [21] -->
2

<!-- b000525 | furniture | pages [21] -->
MATHmodels

<!-- b000526 | furniture | pages [21] -->
获取更多资讯

<!-- b000527 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000528 | furniture | pages [22] -->
Team # 2101855

<!-- b000529 | furniture | pages [22] -->
Page 22 of 23

<!-- b000530 | heading | pages [22] -->
References

<!-- b000531 | references | pages [22] -->
[1] Cano, P., Celma, O., Koppenberger, M., & Buldu, J. M. (2006). Topology of mu-

<!-- b000532 | references | pages [22] -->
微信公众号：数学模型

<!-- b000533 | references | pages [22] -->
sic recommendation networks. Chaos: An interdisciplinary journal of nonlinear

<!-- b000534 | references | pages [22] -->
science, 16(1), 013107.

<!-- b000535 | references | pages [22] -->
[2] Leskovec, J., Kleinberg, J., & Faloutsos, C. (2007). Graph evolution: Densiﬁcation

<!-- b000536 | references | pages [22] -->
and shrinking diameters. ACM transactions on Knowledge Discovery from Data

<!-- b000537 | references | pages [22] -->
(TKDD), 1(1), 2-es.

<!-- b000538 | references | pages [22] -->
[3] Rossetti, G. (2020) DyNetx: dynamic network analysis library, v0.2.1, Zenodo, doi:

<!-- b000539 | references | pages [22] -->
10.5281/zenodo.3953119.

<!-- b000540 | references | pages [22] -->
[4] Ren, Z. M., Mariani, M. S., Zhang, Y. C., & Medo, M. (2018). Randomizing growing

<!-- b000541 | references | pages [22] -->
networks with a time-respecting null model. Physical Review E, 97(5), 052311.

<!-- b000542 | references | pages [22] -->
[5] Mariani, M. S., Medo, M., & Zhang, Y. C. (2015). Ranking nodes in growing net-

<!-- b000543 | references | pages [22] -->
微信号：MATHmodels

<!-- b000544 | references | pages [22] -->
works: When PageRank fails. Scientiﬁc reports, 5(1), 1-10.

<!-- b000545 | references | pages [22] -->
[6] Mariani, M. S., Medo, M., & Zhang, Y. C. (2016). Identiﬁcation of milestone papers

<!-- b000546 | references | pages [22] -->
through time-balanced network centrality. Journal of Informetrics, 10(4), 1207-

<!-- b000547 | references | pages [22] -->
1223.

<!-- b000548 | references | pages [22] -->
[7] Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). The PageRank citation rank-

<!-- b000549 | references | pages [22] -->
ing: Bringing order to the web. Stanford InfoLab.

<!-- b000550 | references | pages [22] -->
[8] Bottou, L. (2012). Stochastic gradient descent tricks. In Neural networks: Tricks of

<!-- b000551 | references | pages [22] -->
the trade (pp. 421-436). Springer, Berlin, Heidelberg.

<!-- b000552 | references | pages [22] -->
[9] Burkholder, J. P., Grout, D. J., & Palisca, C. V. (2019). A History of Western Music:

<!-- b000553 | references | pages [22] -->
Tenth International Student Edition. WW Norton & Company.

<!-- b000554 | references | pages [22] -->
[10] Bromell, N. (2000). " The Blues and the Veil": the cultural work of musical form in

<!-- b000555 | references | pages [22] -->
blues and’60s rock. American Music, 193-221.

<!-- b000556 | references | pages [22] -->
[11] Kodinariya, T. M., & Makwana, P. R. (2013). Review on determining number of

<!-- b000557 | references | pages [22] -->
Cluster in K-Means Clustering. International Journal, 1(6), 90-95.

<!-- b000558 | references | pages [22] -->
[12] Kipf, T. N., & Welling, M. (2016). Semi-supervised classiﬁcation with graph con-

<!-- b000559 | references | pages [22] -->
volutional networks. arXiv preprint arXiv:1609.02907.

<!-- b000560 | references | pages [22] -->
[13] Abadi, M., Agarwal, A., Barham, P., Brevdo, E., Chen, Z., Citro, C., ... & Zheng,

<!-- b000561 | references | pages [22] -->
X. (2016). Tensorﬂow: Large-scale machine learning on heterogeneous distributed

<!-- b000562 | references | pages [22] -->
systems. arXiv preprint arXiv:1603.04467.

<!-- b000563 | references | pages [22] -->
[14] Logan, B. (2000, October). Mel frequency cepstral coefﬁcients for music modeling.

<!-- b000564 | references | pages [22] -->
In Ismir (Vol. 270, pp. 1-11).

<!-- b000565 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000566 | references | pages [22] -->
关注数学模型

<!-- b000567 | furniture | pages [22] -->
2

<!-- b000568 | furniture | pages [22] -->
MATHmodels

<!-- b000569 | furniture | pages [22] -->
获取更多资讯

<!-- b000570 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000571 | furniture | pages [23] -->
Team # 2101855

<!-- b000572 | furniture | pages [23] -->
Page 23 of 23

<!-- b000573 | heading | pages [23] -->
Appendix A: Information of Dynamic Networks

<!-- b000574 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000575 | caption | pages [23] -->
Table 4: Descriptive Statistics of Dynamic Networks

<!-- b000576 | prose | pages [23] -->
n m k t

<!-- b000577 | prose | pages [23] -->
0 246 129 0.524 1 625 826 1.322 2 1304 3506 2.609 3 2562 10149 3.961 4 3584 16962 4.733 5 4645 25448 5.474 6 5479 36446 6.647 7 5593 41956 7.496

<!-- b000578 | prose | pages [23] -->
Note: n is the Number of Nodes, m is the Number of Edges, k is the Average Degree. Note that diameter and mean geodesic distance can’t be calculated here as for early 微信号：MATHmodels times, the networks weren’t connected, which can also be seen in 1a.

<!-- b000579 | heading | pages [23] -->
Appendix B: Namelist of "Benchmark" Artists in GCN

<!-- b000580 | caption | pages [23] -->
Table 5: Benchmark Artists

<!-- b000581 | prose | pages [23] -->
Avant-Garde Blues Childrens Classical Terry Riley T-Bone Walker Alvin&The Chipmunks John Cage Comedy/Spoken Country Easy Listening Electronic Spike Jones Roy Acuff Bert Kaempfert Kraftwerk Folk International Jazz Latin Woody Guthrie Ravi Shankar Cab Calloway Lecuona Cuban Boys New Age Pop/Rock R&B Reggae Mike Oldﬁeld The Beatles Ray Charles Lord Invader Religious Stage&Screen Unknown Vocal Sister Rosetta Tharpe Harold Arlen The Bothy Band Billie Holiday

<!-- b000582 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000583 | prose | pages [23] -->
关注数学模型

<!-- b000584 | furniture | pages [23] -->
2

<!-- b000585 | furniture | pages [23] -->
MATHmodels

<!-- b000586 | furniture | pages [23] -->
获取更多资讯
