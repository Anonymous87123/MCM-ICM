# P-D-2021-2101855-c4682962

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | furniture | pages [1] -->
2021

<!-- b000003 | prose | pages [1] -->
Problem Chosen

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
1

<!-- b000030 | heading | pages [2] -->
Introduction

<!-- b000031 | prose | pages [2] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Background 4

<!-- b000032 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000033 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000034 | prose | pages [2] -->
2

<!-- b000035 | heading | pages [2] -->
Assumptions and Notations

<!-- b000036 | prose | pages [2] -->
4

<!-- b000037 | prose | pages [2] -->
4 Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 5

<!-- b000038 | heading | pages [2] -->
Benchmark Models and Overall Analysis

<!-- b000039 | prose | pages [2] -->
3 5 Framework of Musicians’ Social Network . . . . . . . . . . . . . . . . . . 3.1 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.1 Static Network 5 Dynamic Network . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2 6 Measure of Inﬂuence: Time-Balanced Network Centrality . . . . . . . . . 3.2 6 Model of Rescaled PageRank . . . . . . . . . . . . . . . . . . . . . 3.2.1 6 Example from Subnetwork of the 80s 3.2.2 . . . . . . . . . . . . . . . .

<!-- b000040 | prose | pages [2] -->
7

<!-- b000041 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000042 | prose | pages [2] -->
Measure of Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 8 Determine Weight Vector from Structure of Networks . . . . . . . 3.3.1 8 Time Structure of Similarity . . . . . . . . . . . . . . . . . . . . . . 3.3.2 9 Test of Validity of Similarity Metric . . . . . . . . . . . . . . . . . . 3.3.3 9

<!-- b000043 | prose | pages [2] -->
Relation between Inﬂuence and Similarity: Updated Rescaling PageRank 4

<!-- b000044 | heading | pages [2] -->
Model

<!-- b000045 | prose | pages [2] -->
9 Updated Rescaled PageRank Model 4.1 . . . . . . . . . . . . . . . . . . . . .

<!-- b000046 | prose | pages [2] -->
10 Relation between Similarity and Inﬂuence . . . . . . . . . . . . . . . . . . 4.2 10 Within Genres . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 10 Between Genres . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 11 A Case Study: Did Inﬂuencer Really Affect Followers? 4.3

<!-- b000047 | prose | pages [2] -->
5 Evolution of Different Genres

<!-- b000048 | prose | pages [2] -->
. . . . . . . . . .

<!-- b000049 | prose | pages [2] -->
11

<!-- b000050 | prose | pages [2] -->
12 Basis for Differentiating Genres . . . . . . . . . . . . . . . . . . . . . . . . 5.1 12 . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.1 Size and Inﬂuence 12 Musical identity: Measure of Relationship between Genres . . . . 5.1.2 13 Identiﬁcation of Revolutions . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 5.2.1 Revolutions from Outer Part 14 . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | prose | pages [2] -->
14 Revolutions from Inner Part . . . . . . . . . . . . . . . . . . . . . . 5.2.2 15 A Case Study: Evolution of Blue Music 5.3

<!-- b000052 | prose | pages [2] -->
6

<!-- b000053 | heading | pages [2] -->
Test and Sensitivity Analysis

<!-- b000054 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000055 | prose | pages [2] -->
16

<!-- b000056 | prose | pages [2] -->
17 Sensitivity Analysis on the Average Window of Rescaled PageRank . . . 6.1 17 Evidence from GCN: Can We Find More Information from the Structure 6.2 of Network? . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | prose | pages [2] -->
7

<!-- b000058 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000059 | prose | pages [2] -->
18

<!-- b000060 | prose | pages [2] -->
19 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.1 19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7.2 Weaknesses

<!-- b000061 | prose | pages [2] -->
8

<!-- b000062 | heading | pages [2] -->
Further Discussion

<!-- b000063 | heading | pages [2] -->
Letter

<!-- b000064 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000065 | prose | pages [2] -->
20

<!-- b000066 | prose | pages [2] -->
20

<!-- b000067 | prose | pages [2] -->
21

<!-- b000068 | prose | pages [2] -->
关注数学模型

<!-- b000069 | furniture | pages [2] -->
2

<!-- b000070 | furniture | pages [2] -->
MATHmodels

<!-- b000071 | furniture | pages [2] -->
获取更多资讯

<!-- b000072 | furniture | pages [2] -->
2

<!-- b000073 | furniture | pages [2] -->
2

<!-- b000074 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000075 | furniture | pages [3] -->
Team # 2101855

<!-- b000076 | furniture | pages [3] -->
Page 3 of 23

<!-- b000077 | heading | pages [3] -->
References

<!-- b000078 | references | pages [3] -->
22

<!-- b000079 | heading | pages [3] -->
Appendix A: Information of Dynamic Networks

<!-- b000080 | prose | pages [3] -->
23

<!-- b000081 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000082 | heading | pages [3] -->
Appendix B: Namelist of "Benchmark" Artists in GCN

<!-- b000083 | prose | pages [3] -->
23

<!-- b000084 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000085 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000086 | prose | pages [3] -->
关注数学模型

<!-- b000087 | furniture | pages [3] -->
2

<!-- b000088 | furniture | pages [3] -->
MATHmodels

<!-- b000089 | furniture | pages [3] -->
获取更多资讯

<!-- b000090 | furniture | pages [4] -->
Team # 2101855

<!-- b000091 | prose | pages [4] -->
1

<!-- b000092 | heading | pages [4] -->
Introduction

<!-- b000093 | prose | pages [4] -->
1.1

<!-- b000094 | heading | pages [4] -->
Background

<!-- b000095 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000096 | furniture | pages [4] -->
Page 4 of 23

<!-- b000097 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000098 | prose | pages [4] -->
Long been regarded as one of the most creative masterpieces of humankind, mu- sic plays an important role in every age with distinctly different genres and contents, while some masters’ works survived and inﬂuenced generations of musicians as well as listeners with their unique vitality.

<!-- b000099 | prose | pages [4] -->
Great works have their own identities, but beauty is their common denominator. New musicians learn from their predecessors, which could render some similarities between works across different times. But how musicians inﬂuenced each other? Did they learn more from those great artists or those more similar to their interest? Can we identify those revolutionary artists and events? These questions require us to discover the community structure of musicians for more information.

<!-- b000100 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000101 | prose | pages [4] -->
1.2 Restatement of the Problem

<!-- b000102 | heading | pages [4] -->
1. How to portray the dynamic community structure of musicians?

<!-- b000103 | heading | pages [4] -->
2. How to quantify the inﬂuence between different artists?

<!-- b000104 | heading | pages [4] -->
3. How to measure the similarity of creators by the characteristics of their works? How

<!-- b000105 | prose | pages [4] -->
to determine its relationship with inﬂuence?

<!-- b000106 | heading | pages [4] -->
4. What is the basis for distinguishing between genres?

<!-- b000107 | heading | pages [4] -->
5. With all the metrics above, how to trace the evolution and revolution of all the gen-

<!-- b000108 | prose | pages [4] -->
res?

<!-- b000109 | heading | pages [4] -->
Assumptions and Notations

<!-- b000110 | prose | pages [4] -->
2

<!-- b000111 | prose | pages [4] -->
2.1

<!-- b000112 | heading | pages [4] -->
Assumptions

<!-- b000113 | prose | pages [4] -->
To simplify the analysis of our problem, we make the following assumptions, each of which is properly justiﬁed.

<!-- b000114 | heading | pages [4] -->
1. Assumed that for a connecting subgraph with less than 1% musicians compared to

<!-- b000115 | prose | pages [4] -->
the maximum connecting subgraph, it can be ignored during analysis due to its tiny contribution to the whole community of musicians.

<!-- b000116 | heading | pages [4] -->
2. Assumed that the interaction built up as soon as the follower got active.

<!-- b000117 | heading | pages [4] -->
3. Assumed that songs released in 1920s are classiﬁed into 1930s.

<!-- b000118 | heading | pages [4] -->
4. Assumed that songs released before the musicians active years make no difference

<!-- b000119 | prose | pages [4] -->
to the artist’s overall music style.

<!-- b000120 | heading | pages [4] -->
5. Assumed that one artist’s style can be represented by the average characteristics of

<!-- b000121 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000122 | prose | pages [4] -->
his/her works every decade.

<!-- b000123 | prose | pages [4] -->
关注数学模型

<!-- b000124 | furniture | pages [4] -->
2

<!-- b000125 | furniture | pages [4] -->
MATHmodels

<!-- b000126 | furniture | pages [4] -->
获取更多资讯

<!-- b000127 | furniture | pages [5] -->
Team # 2101855

<!-- b000128 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000129 | furniture | pages [5] -->
Page 5 of 23

<!-- b000130 | heading | pages [5] -->
6. Assumed that the inﬂuence of past works on the present musicians decays geomet-

<!-- b000131 | prose | pages [5] -->
rically.

<!-- b000132 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000133 | prose | pages [5] -->
2.2

<!-- b000134 | heading | pages [5] -->
Notations

<!-- b000135 | prose | pages [5] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000136 | caption | pages [5] -->
Table 1: Notations

<!-- b000137 | prose | pages [5] -->
Symbol

<!-- b000138 | prose | pages [5] -->
nt

<!-- b000139 | prose | pages [5] -->
Deﬁnition

<!-- b000140 | prose | pages [5] -->
Number of nodes in graph at period t mt Number of edges in graph at period t kt Average degree of graph at period t lt Average geodesic distance at period t d Diameter of graph N Set of nodes in the network

<!-- b000141 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000142 | prose | pages [5] -->
kin

<!-- b000143 | prose | pages [5] -->
n,t, kout

<!-- b000144 | prose | pages [5] -->
Indegree and outdegree of node n at period t n,t X Network data of the graph A Adjacency matrix of the graph Y Labels for musicians Sn Set of musician n’s works pn, Rn(p) PageRank Score and Rescaled PageRank score of musician n µn(p), σn(p) Mean and Standard Error of musician n in averaging window dis(n1, n2) Geodesic distance between n1 and n2 Sim(n1, n2) Similarity between n1 and n2 a Weight vector in determining similarity E Error term in training W(0), W(1) Weight matrices for hidden layers in GCN yL Set of node indices with labels in GCN γn Label for musician n from GCN

<!-- b000145 | heading | pages [5] -->
Benchmark Models and Overall Analysis

<!-- b000146 | prose | pages [5] -->
3

<!-- b000147 | prose | pages [5] -->
Framework of Musicians’ Social Network 3.1

<!-- b000148 | prose | pages [5] -->
3.1.1 Static Network

<!-- b000149 | prose | pages [5] -->
According to the data, it’s intuitively to build up a static social network by the existent interactions, which present many network identities that are common to other real social networks.Part of the network’s statistics are shown in Table 2.

<!-- b000150 | prose | pages [5] -->
During the data processing, we found that two pairs of musicians never built up any other relationships, while other 5599 musicians are on a connecting subgraph. Based on Assumption 1, these 4 musicians, Chuckii Booker and Mark Morrison with The Neptunes and Kaytranada are abandoned in our following analysis.

<!-- b000151 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000152 | prose | pages [5] -->
关注数学模型

<!-- b000153 | furniture | pages [5] -->
2

<!-- b000154 | furniture | pages [5] -->
MATHmodels

<!-- b000155 | furniture | pages [5] -->
获取更多资讯

<!-- b000156 | furniture | pages [6] -->
Team # 2101855

<!-- b000157 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000158 | furniture | pages [6] -->
Page 6 of 23

<!-- b000159 | caption | pages [6] -->
Table 2: Descriptive statistics of static network

<!-- b000160 | prose | pages [6] -->
n

<!-- b000161 | prose | pages [6] -->
Directed 5599

<!-- b000162 | prose | pages [6] -->
m k l

<!-- b000163 | prose | pages [6] -->
42768 7.639 1.333

<!-- b000164 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000165 | prose | pages [6] -->
Undirected 5599 42729 7.632 3.724

<!-- b000166 | prose | pages [6] -->
Note: n is the Number of Nodes, m is the Num- ber of Edges, k is the Average Degree, l is the Mean Geodesic Distance.

<!-- b000167 | prose | pages [6] -->
Some very interesting phenomena can be observed. The difference between the number of edges is rather small, which shows that there is rather few two-way inﬂu- ence between musicians. At the same time, the average distance in directed graph is way shorter than that in undirected graph. The approaching-to-1 value represents that great stars often inﬂuenced others, while they weren’t inﬂuenced easily by his younger generations1. Contemporaries rarely inﬂuenced each other either.

<!-- b000168 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000169 | prose | pages [6] -->
This also shows the property of "small-world"[1]. Except from the small average distance, diameter of the undirected graph is 13 which is also relatively small com- pared to the scale of network.

<!-- b000170 | prose | pages [6] -->
This network can depict relationship between musicians in a way, though, it cares only about the relation of inﬂuence from the perspective of this decade, which is bound to aggrandize the importance of older generations. Also, it’s hard to observe the evo- lution of this community by a static network. All these reasons drive us to raise a dynamic network.

<!-- b000171 | prose | pages [6] -->
3.1.2 Dynamic Network

<!-- b000172 | prose | pages [6] -->
According to Assumption 3 as well as the characteristics of the data, all relation- ships built up at the beginning of each decade. Thus we can separate time between 1930-2010 into 9 periods. Remark 1930 as t0, the community can be regarded as a growing network with the continuous supplement of new musicians2. By the package of DyNext[3], such a network can be built up by Python. Figure 1 shows how the net- work evolved throuth t = 0, 1, 2. More information for each period is in the appendix.

<!-- b000173 | prose | pages [6] -->
Measure of Inﬂuence: Time-Balanced Network Centrality 3.2

<!-- b000174 | prose | pages [6] -->
3.2.1

<!-- b000175 | heading | pages [6] -->
Model of Rescaled PageRank

<!-- b000176 | prose | pages [6] -->
For a social network, it’s natural to gauge the inﬂuence of nodes by methods includ- ing centrality, Pagerank etc. However, traditional PageRank will meet several prob- lems in this question: 1. it ignores the time structure of the network, which could pro- duce unrealistic features[4]; 2. the redistribution of PageRank is temporally strongly biased towards old nodes[5], which makes the PageRank scores of new nodes from 10s

<!-- b000177 | prose | pages [6] -->
1All these phonomenon help explain the plausibility of Assumption 2, as there are very few young- sters affect older generations, it won’t make a big difference to the result.

<!-- b000178 | prose | pages [6] -->
2This can be checked by the data presented in the appendix and the pattern presented in [1] and [2], where edges grow faster than nodes, and bigger the network, smaller the diameter and average

<!-- b000179 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000180 | prose | pages [6] -->
关注数学模型 distance(In earlier period, most of musicians weren’t even on a same subgraph).

<!-- b000181 | furniture | pages [6] -->
2

<!-- b000182 | furniture | pages [6] -->
MATHmodels

<!-- b000183 | furniture | pages [6] -->
获取更多资讯

<!-- b000184 | furniture | pages [7] -->
Team # 2101855

<!-- b000185 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000186 | furniture | pages [7] -->
Page 7 of 23

<!-- b000187 | caption | pages [7] -->
Figure 1: Evolution of dynamic network

<!-- b000188 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000189 | prose | pages [7] -->
(b) t=1 (a) t=0 (c) t=2

<!-- b000190 | prose | pages [7] -->
are all close to 0; 3. PageRank algorithm contains no more information than indegree of nodes[5], while in the adjacency matrix it simpliﬁes the inﬂuence from all inﬂuencers as the same( 1

<!-- b000191 | prose | pages [7] -->
kin), which doesn’t correspond to reality. For example, for a R&B singer like Terence Trent D’Arby who is inﬂuenced by Micheal Jackson and The Beatles at the same time, though, it’s hard to say they played an equal role in his process of growth.

<!-- b000192 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000193 | prose | pages [7] -->
Based on these ﬂaws, we raise a rescaled PageRank algorithm to capture the in- ﬂuence of music unbiasedly, which considers the relative position of corresponding musician among his/her contemporaries. By [6], it can be expressed in the following form:

<!-- b000194 | prose | pages [7] -->
Rn(p) = pn −µn(p)

<!-- b000195 | prose | pages [7] -->
(1) σn(p)

<!-- b000196 | prose | pages [7] -->
Here, p is calculated by ordinary PageRank algorithm from [7]. µn(p) and σn(p) are computed over musicians from the same genre j ∈[i −∆p/2, i + ∆p/2] in order to taking its relative position into account, where ∆p represents the scale of musicians in averaging window. Here, we take ∆p = 25 which is smaller than it used in [6] due to the smaller amount of musicians. However, it will meet some problem in processing artists from 10s, as there were very few musicians entering this community in the last decade. So when comparing the outcomes, it’s better to stick to the results before 2000s.

<!-- b000197 | prose | pages [7] -->
Example from Subnetwork of the 80s 3.2.2

<!-- b000198 | prose | pages [7] -->
As we’ve mentioned above, this network can be regarded as a growing network. So every period with t < 8 is a subnetwork of the ultimate one. Take 1980s as an example, the detailed information is in appendix A where t = 5. It’s a fast changing decade with a great many musicians entered the community and the interactions between musicians expanded at a surprising speed. These make it a good age for us to check our inﬂuence model.

<!-- b000199 | prose | pages [7] -->
Part of results from rescaled PageRank model are shown in Fig.2. From the dis- tribution of top 100 musicians, it’s clear that 80s is the time of pop music(like every decade) and black music(Jazz, R&B, Blues, Religious etc.). For other types of mu- sic, there appear lower proﬁles with great but less inﬂuential musicians including Kraftwerk(Electronic), Roy Acuff(Country) etc.

<!-- b000200 | prose | pages [7] -->
At the same time, the generations of these musicians are also evenly distributed. Artists from 40s were most actively affecting young musicians, where new generations and older generations all have their inﬂuence on their recipients. There is still pos-

<!-- b000201 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000202 | prose | pages [7] -->
sibility of overestimating old nodes, but the overall results support the property of关注数学模型

<!-- b000203 | furniture | pages [7] -->
2

<!-- b000204 | furniture | pages [7] -->
MATHmodels

<!-- b000205 | furniture | pages [7] -->
获取更多资讯

<!-- b000206 | furniture | pages [8] -->
Team # 2101855

<!-- b000207 | prose | pages [8] -->
time-balancing in rescaled PageRank.

<!-- b000208 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000209 | furniture | pages [8] -->
Page 8 of 23

<!-- b000210 | caption | pages [8] -->
Figure 2: Distribution of Genres and Active Years for Top 100 Musicians in 1980s

<!-- b000211 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000212 | prose | pages [8] -->
(a) Distribution of Genres (b) Distribution of Active Years

<!-- b000213 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000214 | prose | pages [8] -->
3.3 Measure of Similarity

<!-- b000215 | prose | pages [8] -->
To clarify the similarity between musicians by the charateristics of their works, it’s hard to process without genres as labels which disenables us to optimize the weight of different factors unless we simply regard they share same effects to different music genres. Therefore, to measure similarity, we need to ﬁgure out how music differs by all these identities ﬁrst.

<!-- b000216 | prose | pages [8] -->
Determine Weight Vector from Structure of Networks 3.3.1

<!-- b000217 | prose | pages [8] -->
Without extra information about labels, the structure of the dynamic networks ac- tually contains similarity. It’s natural to believe that musicians affected by similar mu- sicians and inﬂuenced similar musicians could have some common in their works.

<!-- b000218 | prose | pages [8] -->
Thus, from the information from networks, we build an adjusted weighted cosine distance to measure the similarity between musician n1 and n2:

<!-- b000219 | prose | pages [8] -->
Sim(n1, n2) = cos < axn1, axn2 > (2)

<!-- b000220 | prose | pages [8] -->
During training, we optimize weight vector a by minizing MSE in (3):

<!-- b000221 | prose | pages [8] -->
min E(a) = ∑

<!-- b000222 | prose | pages [8] -->
∑ n1∈N n2∈N,n2̸=n1

<!-- b000223 | prose | pages [8] -->
(ζ(n1, n2) −Sim(n1, n2))2 (3)

<!-- b000224 | prose | pages [8] -->
Where the label of samples are deﬁned by (2):

<!-- b000225 | prose | pages [8] -->
{

<!-- b000226 | prose | pages [8] -->
cos( dis(n1,n2)

<!-- b000227 | prose | pages [8] -->
12

<!-- b000228 | prose | pages [8] -->
ζ(n1, n2) =

<!-- b000229 | prose | pages [8] -->
0 1 ≤dis(n1, n2) ≤5 π)

<!-- b000230 | prose | pages [8] -->
(4)

<!-- b000231 | prose | pages [8] -->
dis(n1, n2) > 5

<!-- b000232 | prose | pages [8] -->
By the property of small-world, we consider the cosine similarity of nodes by its geodesic distance in the network. We don’t think for nodes whose distance above 5 still have similarities as it’s way bigger than the average distance even in the undirected network. So with geodesic distance below 6, we separate the space between [0, π

<!-- b000233 | prose | pages [8] -->
2 ] into 6 parts to get an "expected similarity". By minimizing the squared error between similarity and "expected similarity", we are able to ﬁgure out the optimized weight

<!-- b000234 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000235 | prose | pages [8] -->
vector by stochastic gradient descent[8].

<!-- b000236 | prose | pages [8] -->
关注数学模型

<!-- b000237 | furniture | pages [8] -->
2

<!-- b000238 | furniture | pages [8] -->
MATHmodels

<!-- b000239 | furniture | pages [8] -->
获取更多资讯

<!-- b000240 | furniture | pages [9] -->
Team # 2101855

<!-- b000241 | prose | pages [9] -->
3.3.2 Time Structure of Similarity

<!-- b000242 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000243 | furniture | pages [9] -->
Page 9 of 23

<!-- b000244 | prose | pages [9] -->
By Assumption 3 and 5, we are able to separate songs into different decades to analyze the transition of different elements. Based on data from "full_music_data.csv",

<!-- b000245 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000246 | prose | pages [9] -->
we can express average characteristics of musician at period t by (5):

<!-- b000247 | prose | pages [9] -->
xnt = ∑snt∈Snt snt

<!-- b000248 | prose | pages [9] -->
(5) |Snt|

<!-- b000249 | prose | pages [9] -->
, where snt represent the characteristics of his/her work in period t, and |Snt| is the amount of songs in the period(This process is headed on the basis of Assumption 4).

<!-- b000250 | prose | pages [9] -->
By model presented in (2)-(5), weight vector at can be ﬁgured out through each period again by stochastic gradient descent, from which the core features of music from different decades can be compared vertically by its importance represented in weight vector.

<!-- b000251 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000252 | prose | pages [9] -->
3.3.3 Test of Validity of Similarity Metric

<!-- b000253 | prose | pages [9] -->
It’s an exhausting work to check similarity between all pairs of musicians. To sim- plify it, we randomly pick 500 musicians every time from the network when t = 8. Then we compute similarity between each pairs and by their genres, we separately calculate the average similarity with genre and between genre.

<!-- b000254 | prose | pages [9] -->
By 10 rounds of iterations, it can be found from Fig.3 that almost in all samples, the average similarity within groups is all higher than that between groups for nearly 0.05. As the iterations have covered a great part of musicians, it substantiates that our metric of gauging similarity can distinguish between different genres of music.

<!-- b000255 | caption | pages [9] -->
Figure 3: Similarity within and between groups in ten iterations

<!-- b000256 | prose | pages [9] -->
Relation between Inﬂuence and Similarity: Updated 4

<!-- b000257 | heading | pages [9] -->
Rescaling PageRank Model

<!-- b000258 | prose | pages [9] -->
To check the relationship between inﬂuence and similarity among musicians, it’s hard to compare directly. At the same time, methods like regression analysis are not available due to the dynamic structure. So we need to optimize our PageRank model

<!-- b000259 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000260 | prose | pages [9] -->
关注数学模型 again with more information about similarity except from just rescaling it.

<!-- b000261 | furniture | pages [9] -->
2

<!-- b000262 | furniture | pages [9] -->
MATHmodels

<!-- b000263 | furniture | pages [9] -->
获取更多资讯

<!-- b000264 | furniture | pages [10] -->
Team # 2101855

<!-- b000265 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000266 | furniture | pages [10] -->
Page 10 of 23

<!-- b000267 | heading | pages [10] -->
Updated Rescaled PageRank Model

<!-- b000268 | prose | pages [10] -->
4.1

<!-- b000269 | prose | pages [10] -->
First, we’d like to check ordinary PageRank adjacency matrix. For a node n1 in network, its corresponding element in initial matrix with node n2 that inﬂuences is

<!-- b000270 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000271 | prose | pages [10] -->
1 represented by An1,n2 =

<!-- b000272 | prose | pages [10] -->
n1,t.

<!-- b000273 | prose | pages [10] -->
kout

<!-- b000274 | prose | pages [10] -->
However, there is actually another assumption beneath in this network using inde- gree as the basis of inﬂuence: every musician is equally affected by all his inﬂuencers. And we don’t regard this true. So we use similarity to replace the degree. Here, we build a new adjacency matrix denoted by ¯A which goes like:

<!-- b000275 | prose | pages [10] -->
¯An1,n2 = ∑n Sim(n1, n2)

<!-- b000276 | prose | pages [10] -->
(6) i=2 Sim(n1, ni)

<!-- b000277 | prose | pages [10] -->
Here, adjacency matrix presented in (6) ﬁgures out the third problem discussed in ordinary PageRank. Also, as the similarity is time-varying in different decades, we’re able to consider the lag effects from inﬂuencers. Again, we can update this ¯A as:

<!-- b000278 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000279 | prose | pages [10] -->
t

<!-- b000280 | prose | pages [10] -->
βt−j

<!-- b000281 | prose | pages [10] -->
¯Atn1,n2 =

<!-- b000282 | prose | pages [10] -->
∑ j=0

<!-- b000283 | prose | pages [10] -->
Simj(n1, n2)

<!-- b000284 | prose | pages [10] -->
(7)

<!-- b000285 | prose | pages [10] -->
∑n

<!-- b000286 | prose | pages [10] -->
i=2 Simj(n1, ni)

<!-- b000287 | prose | pages [10] -->
Where β is the discount factor of decades from Assumption 6. Here, the matrix contains more information about similarity as well the inﬂuence from time. And by rescaled PageRank algorithm above with the updated adjacency matrix, we can get inﬂuence that considers similarity.

<!-- b000288 | prose | pages [10] -->
After processing, some of results are presented in 4 below. And by comparing it with results from 3.3.2, we can consider the effects from similarity and inﬂuence comprehensively.

<!-- b000289 | caption | pages [10] -->
Figure 4: Revised Distribution of Genres and Active Years for Top 100 Musicians in 1980s

<!-- b000290 | prose | pages [10] -->
(a) Distribution of Genres (b) Distribution of Active Years

<!-- b000291 | prose | pages [10] -->
Relation between Similarity and Inﬂuence 4.2

<!-- b000292 | prose | pages [10] -->
4.2.1 Within Genres

<!-- b000293 | prose | pages [10] -->
In the rescaling process, we’ve considered characteristics within the genre. The

<!-- b000294 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000295 | prose | pages [10] -->
rescaled PageRank actually represents the relative position of musician in its genre in关注数学模型

<!-- b000296 | furniture | pages [10] -->
2

<!-- b000297 | furniture | pages [10] -->
MATHmodels

<!-- b000298 | furniture | pages [10] -->
获取更多资讯

<!-- b000299 | furniture | pages [11] -->
Team # 2101855

<!-- b000300 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000301 | furniture | pages [11] -->
Page 11 of 23

<!-- b000302 | prose | pages [11] -->
a way. And by researching the distribution of the age of musicians can help ﬁnd their time-balancing effects within genres.

<!-- b000303 | prose | pages [11] -->
From Fig.2b, where inﬂuence is represented by "the amount of juniors one inﬂu- ences", it can be observed that even under rescaled indicator, old musicians’ inﬂuence

<!-- b000304 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000305 | prose | pages [11] -->
is tend to be bigger. This is natural – more experienced artists deserve higher status.

<!-- b000306 | prose | pages [11] -->
While after considering similarity, it concerns more about prevalence now. It’s hard to learn from works decades ago though, fad of the moment will be more often imi- tated. So similarity actually measures the degree of impact as shown in Fig.4b. More musicians that deﬁned styles at his/her time are emphasized in the updated model so younger musicians appear more in Top 100. This shows our measure contains both sides of inﬂuence.

<!-- b000307 | prose | pages [11] -->
4.2.2 Between Genres

<!-- b000308 | prose | pages [11] -->
The impact between genres can be shown in importance of different genres. Com-

<!-- b000309 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000310 | prose | pages [11] -->
paring genres presented in Fig.2a and Fig.4a, tiny increase in share of Pop/Rock and black music can be observed in updated model. Both model fail to capture those miche genres. So, though we can distinguish genres by similarity in a way, it doesn’t deter- mine difference between genres.

<!-- b000311 | prose | pages [11] -->
This shows the degree of mainstreaming of genre determines its inﬂuence. While similarity’s effect is less common. It may perform an essential role in creating though, listeners could prefer music that’s more mainstream and similar to mainstream music.

<!-- b000312 | prose | pages [11] -->
A Case Study: Did Inﬂuencer Really Affect Followers? 4.3

<!-- b000313 | prose | pages [11] -->
From observations presented in 4.2.1, it can be found that the similarity between musicians is not fully measured when only inﬂuence is considered in PageRank. In order to identify whether the musicians have actually inﬂuenced each other, we need to take a closer look at the similarities between different musicians.

<!-- b000314 | prose | pages [11] -->
Take John Williams(Stage & Screen) and Lambert, Hendricks & Ross(Jazz) as ex- amples, who were both inﬂuenced by many musicians across periods as well as contin- uously affected newcomers. In Table 3, we presented their average change on musical characteristics from t = 1 to 3 compared to those when t = 1, and their average differ- ence from their inﬂuencers to check if there existed some kind of correlation.

<!-- b000315 | caption | pages [11] -->
Table 3: Average Change in Percent of Identities for Musicians and Inﬂuencers in 40s

<!-- b000316 | prose | pages [11] -->
Char 1 2 3 4 5

<!-- b000317 | prose | pages [11] -->
John -3.3 50.2 13.9 -4.5 -23.6 John’s 2.3 -32 18.5 -6 20.3 Inﬂ-er

<!-- b000318 | prose | pages [11] -->
Ross 24 22.5 95.6 -27.5 -23.6 Ross’s 18 6.3 102 -5.6 -23.1 Inﬂ-er

<!-- b000319 | prose | pages [11] -->
6 7 8 9 10 11 12

<!-- b000320 | prose | pages [11] -->
150 50 -15.9 -25 28.3 0.3 -2.9

<!-- b000321 | prose | pages [11] -->
50 72.5 3.6 -0.9 -14.4 0.4 27

<!-- b000322 | prose | pages [11] -->
-33 + -18.9 + 32.7 91 1.5

<!-- b000323 | prose | pages [11] -->
0 + -2.3 + 96.2 27 -3.8

<!-- b000324 | prose | pages [11] -->
Percent change of identities except from "Popularity" are presented above.

<!-- b000325 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000326 | prose | pages [11] -->
"+" means that the element in the corresponding position is equal to or close to 0 in 40s. It关注数学模型

<!-- b000327 | furniture | pages [11] -->
2

<!-- b000328 | furniture | pages [11] -->
MATHmodels

<!-- b000329 | furniture | pages [11] -->
获取更多资讯

<!-- b000330 | furniture | pages [12] -->
Team # 2101855

<!-- b000331 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000332 | furniture | pages [12] -->
Page 12 of 23

<!-- b000333 | prose | pages [12] -->
can be observed that between musicians and their inﬂuencers, musical characteristics tend to change in the same direction and scale, while for type of vocals, they don’t always change in unison.

<!-- b000334 | prose | pages [12] -->
Besides, different genres emphasize different identities in mutually inﬂuencing. For

<!-- b000335 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000336 | prose | pages [12] -->
example, bigger change had taken place in Valence and Tempo for Jazz compared to Stage & Screen music. This is also correlated to the evolution of music genres.

<!-- b000337 | prose | pages [12] -->
However, this kind of relation may not always exist. Though as we shown in Fig.3, in samples the average similarity is between 0.6-0.7. However, if we calculate all simi- larity between all pairs of musicians with inﬂuence relation, the average is about 0.802. And the distribution from 5 shows there are some relations whose similarity are ex- tremely low. Thus, in general this pattern holds, but there may be deviations in indi- vidual samples.

<!-- b000338 | caption | pages [12] -->
Figure 5: Overall Distribution of Similarities among Musicians

<!-- b000339 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000340 | prose | pages [12] -->
However, we can conclude from this case study, that inﬂuence really entered into force for followers especially on musical identities in most cases. And for different genres and periods, there existed totally different contagious characteristics. This asks us to analyze the overall muscial identities of genres across time.

<!-- b000341 | prose | pages [12] -->
Evolution of Different Genres 5

<!-- b000342 | prose | pages [12] -->
Basis for Differentiating Genres 5.1

<!-- b000343 | prose | pages [12] -->
To separate different genres, there are at least 3 factors to be considered: its size, inﬂuence and musical identities.

<!-- b000344 | prose | pages [12] -->
5.1.1 Size and Inﬂuence

<!-- b000345 | prose | pages [12] -->
By the updated rescaled PageRank discussed above, dynamic rank of musicians can be ﬁgured out. Combining information from the same genre, its size and average inﬂuence can be used to determine whether it’s a mainstream or a niche genre.

<!-- b000346 | prose | pages [12] -->
Some important features can be found in Fig.6: Blues music lost its proportion while at the same time it lost its inﬂuence. Pop/Rock gradually takes its dominating position. And during its process of expanding, its average inﬂuence rank increases. However, electronic music exploded from the end of 20th century with its inﬂuence

<!-- b000347 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000348 | prose | pages [12] -->
关注数学模型

<!-- b000349 | furniture | pages [12] -->
2

<!-- b000350 | furniture | pages [12] -->
MATHmodels

<!-- b000351 | furniture | pages [12] -->
获取更多资讯

<!-- b000352 | furniture | pages [13] -->
Team # 2101855

<!-- b000353 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000354 | furniture | pages [13] -->
Page 13 of 23

<!-- b000355 | caption | pages [13] -->
Figure 6: Size and Inﬂuence of Pop/Rock, Blues and Electronic

<!-- b000356 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000357 | prose | pages [13] -->
dropped in a sudden due to its miche position and the newcomers diluted the average impact of it.

<!-- b000358 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000359 | prose | pages [13] -->
So, comprehensively analyzing size and inﬂuence of a genre helps us determine the status of it from its scale and structure of musicians. But for creators, music character- istics are the core of distinguish.

<!-- b000360 | prose | pages [13] -->
Musical identity: Measure of Relationship between Genres 5.1.2

<!-- b000361 | prose | pages [13] -->
By different weight vector across different periods, we are able to calculate the aver- age cosine distance of one speciﬁc genre to represent whether the genre is more similar to others or is more common among genres by its average musical characteristics. The relationships can also be observed from the similarity path between two genres.

<!-- b000362 | prose | pages [13] -->
By vertically comparison of this indicator across periods, we can observe whether the corresponding musical forms have become more homogeneous or more distinctive. For example, the result of Pop/Rock music is shown in Fig.7:

<!-- b000363 | caption | pages [13] -->
Figure 7: Total Similarity between Pop/Rock and Other Genres

<!-- b000364 | prose | pages [13] -->
It can be found that during the process of Pop/Rock music getting popular in 40- 60s, it also got more similar to other genres rapidly. Causality may also be reversed, its pravalence could render other genres learning from it, so its assimilation could also come from its inﬂuence. But one thing is for sure that, the higher it’s status, the more

<!-- b000365 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000366 | prose | pages [13] -->
similar it is also to other genres.

<!-- b000367 | prose | pages [13] -->
关注数学模型

<!-- b000368 | furniture | pages [13] -->
2

<!-- b000369 | furniture | pages [13] -->
MATHmodels

<!-- b000370 | furniture | pages [13] -->
获取更多资讯

<!-- b000371 | furniture | pages [14] -->
Team # 2101855

<!-- b000372 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000373 | furniture | pages [14] -->
Page 14 of 23

<!-- b000374 | prose | pages [14] -->
Combining Fig.6 and 7, we can trace how genres change over time with its size, inﬂuence and its overall characteristics of music.

<!-- b000375 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000376 | prose | pages [14] -->
5.2 Identiﬁcation of Revolutions

<!-- b000377 | prose | pages [14] -->
According to literatures [9] in terms of music history, we could ﬁnd two sources of revolution – the inner part and the outer part. For the inner part, new generations brought in new blood and spread inside the musician network. For the outer part, issues including social and political events, technology development, etc., emerged outside the network and resulted in exogenous inﬂuence.

<!-- b000378 | prose | pages [14] -->
5.2.1 Revolutions from Outer Part

<!-- b000379 | prose | pages [14] -->
Some of the exogenous shocks are so signiﬁcant that result in an overall change in music, which could be identiﬁed by the general trend from data_by_year.csv or the

<!-- b000380 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000381 | prose | pages [14] -->
weight vector we generated. We think the sharp change in overall music characteristics at a certain period could be a signal. And some main revolutions are listed below:

<!-- b000382 | heading | pages [14] -->
1. Acousticness & Instrumentness: The importance of acousticness was greatly weak-

<!-- b000383 | prose | pages [14] -->
ened in 60s with the rise of electronic music, when the Columbia - Princeton Elec- tronic Music Lab was established in 50s. While at the same time instrumentness decreased which shows vocal played a more important role as the popularity of synthesizer technology actually endowed vocal with the property of instruments. This observation is supported by the fact from Fig.8 that the average acousticness of electronic music is 0.233 while that of whole sample is 0.414. At the same time, genres that are not technologically sensitive(Classical, Vocal etc.) appeared more stable in the changing trend of acousticness.

<!-- b000384 | caption | pages [14] -->
Figure 8: Evolution of Acousticness of Genres

<!-- b000385 | heading | pages [14] -->
2. Energy & Valence: During more turbulent phases of the world, the valence of music

<!-- b000386 | prose | pages [14] -->
dropped. This can be observed through World Wars(30s-50s) and periods around 2008 Financial Crisis(00s-10s). While at a relatively peaceful period, music tended to be more energetic. That’s probably why Rock music expanded rapidly through 50s-70s as shown in Fig.6.

<!-- b000387 | heading | pages [14] -->
3. Duration: From the beginning of 21th century, the average duration of music dropped

<!-- b000388 | prose | pages [14] -->
faster than ever. This could be rendered by the rise of platforms including TikTok

<!-- b000389 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000390 | prose | pages [14] -->
关注数学模型 and so on which made people less patient for longer music.

<!-- b000391 | furniture | pages [14] -->
2

<!-- b000392 | furniture | pages [14] -->
MATHmodels

<!-- b000393 | furniture | pages [14] -->
获取更多资讯

<!-- b000394 | furniture | pages [15] -->
Team # 2101855

<!-- b000395 | prose | pages [15] -->
5.2.2 Revolutions from Inner Part

<!-- b000396 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000397 | furniture | pages [15] -->
Page 15 of 23

<!-- b000398 | prose | pages [15] -->
Sometimes, musicians beneﬁt from their innate ingenuity or personal experience, thus contributes or even reshaped the music world. They, correspondingly, might be-

<!-- b000399 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000400 | prose | pages [15] -->
come legends whose masterpieces inspire future generations. According to our model and the given data, we believe a revolutionary should meet up with the following three standards:

<!-- b000401 | heading | pages [15] -->
1. He/She should be inﬂuential, having a high inﬂuence rank. Chances are a musician

<!-- b000402 | prose | pages [15] -->
was claimed to be inﬂuential, but the followers actually don’t share many common features with him or her. The measure of inﬂuence take similarity into considera- tion, which indicates a more reliable impact. Musicians with higher inﬂuence rank include Muddy Waters, Billie Holiday, Lester Young, Elvis Presley, etc., which also correspond to our common sense.

<!-- b000403 | heading | pages [15] -->
2. He/She should deﬁne a style, that is, determine the developing direction of his or

<!-- b000404 | prose | pages [15] -->
her genre in some period. According to the data, we may take notice of the trend

<!-- b000405 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000406 | prose | pages [15] -->
of a musician whose moving pattern is similar to that of the whole genre, especially leading it. This criteria is critical, since pieces of music might be signiﬁcantly differ- ent from its original genre, while seldom musicians follow those attempts. We won’t consider them to be revolutionary.(The trend of genre would exclude the musician itself)

<!-- b000407 | heading | pages [15] -->
3. He/She/They should be distinguishable, which means being different from his or

<!-- b000408 | prose | pages [15] -->
her pioneers. However, this criterion is not feasible out of two reasons. Firstly, we have some inefﬁcient musical identities for us to measure, such as melody. Thus, similarity in the given features including danceability, energy, etc., doesn’t neces- sarily mean similarity between two whole pieces of music. Secondly, proportion of inﬂuential musicians become active at the beginning of 30s and they dont have any pioneers in this data.

<!-- b000409 | prose | pages [15] -->
In consideration of his/her inﬂuence and the leading role of genres average trend, we mainly regard the top 5 musicians to be revolutionaries by characteristics shown in Fig.9, among them are Billie Holiday, Muddy Waters, Bob Dylan, The Beatles, and Little Richard.

<!-- b000410 | prose | pages [15] -->
For example, Billie Holiday has a second highest inﬂuence among all the musicians, and we can recognize an explicit similarity between the trend of her and other musi- cians in vocal. E.g. valence, tempo, key. We assume that she is especially revolutionary in 1930-40s, according to the Fig.9a .

<!-- b000411 | caption | pages [15] -->
Figure 9: Comparison of Characteristics between Revolutionaries and Average Trend

<!-- b000412 | prose | pages [15] -->
(b) Muddy Waters (a) Billie Holiday

<!-- b000413 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000414 | prose | pages [15] -->
(c) Bob Dylan

<!-- b000415 | prose | pages [15] -->
关注数学模型

<!-- b000416 | furniture | pages [15] -->
2

<!-- b000417 | furniture | pages [15] -->
MATHmodels

<!-- b000418 | furniture | pages [15] -->
获取更多资讯

<!-- b000419 | furniture | pages [16] -->
Team # 2101855

<!-- b000420 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000421 | furniture | pages [16] -->
Page 16 of 23

<!-- b000422 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000423 | prose | pages [16] -->
(a) The Beatles (b) Little Richard

<!-- b000424 | prose | pages [16] -->
A Case Study: Evolution of Blue Music 5.3

<!-- b000425 | prose | pages [16] -->
Here we choose Blues for our case study based on the following reasons: (1)Its amount of musicians remains relatively stable which beneﬁts visualization; (2).A sig- niﬁcant number of inﬂuential musicians rose from it; (3)It has a deep cultural back- ground and is strong correlated with social campaigns.

<!-- b000426 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000427 | prose | pages [16] -->
Based on what we’ve discussed in 5.1, ﬁrst we take a look at its inﬂuence present in Fig.11. Its overall popularity, average inﬂuence of top 5 musicians were increasing through 40s-90s, which shows the old generations were getting more and more inﬂuen- tial which can also been observed in Fig.12.3 However, the number of active musicians didn’t increase much, while at the same time the average inﬂuence of all and last 5 musicians even decreased a bit. These shows Blues gradually lost its vitality without inﬂuential newcomers where the bottom right corner of the network had always been rather sparse.

<!-- b000428 | caption | pages [16] -->
Figure 11: Evolution of Inﬂuence and Popularity of Blues from 40s-90s

<!-- b000429 | caption | pages [16] -->
Figure 12: Social Network of Blues Musicians from 40s-90s

<!-- b000430 | prose | pages [16] -->
3We don’t discuss periods after 2000 here as there are few new Blues musicians then.

<!-- b000431 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000432 | prose | pages [16] -->
关注数学模型

<!-- b000433 | furniture | pages [16] -->
2

<!-- b000434 | furniture | pages [16] -->
MATHmodels

<!-- b000435 | furniture | pages [16] -->
获取更多资讯

<!-- b000436 | furniture | pages [17] -->
Team # 2101855

<!-- b000437 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000438 | furniture | pages [17] -->
Page 17 of 23

<!-- b000439 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000440 | prose | pages [17] -->
While for the genre’s musical identities, based on discussion in 5.2, it can be found in Fig.14 as we predicted, its energy increased with the rise of Jumps Blues from Louis Jordan after 30s. Which inﬂuenced rockers including Chuck Berry in a way later.

<!-- b000441 | prose | pages [17] -->
At the same time, its acousticness and sharply decreased after 50s. It’s the age of Chicago Blues(B.B.King). In 60s, Paul Butterﬁeld and British Blues rose with less in- strumental elements in music, which rendered sharp drop of instrumentness in 60s.[10]

<!-- b000442 | prose | pages [17] -->
However, the length of Blues music kept increasing. This is probably rendered

<!-- b000443 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000444 | prose | pages [17] -->
by the development of recording techniques that allowed more works to be recorded rather than only being performed live as it once was.

<!-- b000445 | caption | pages [17] -->
Figure 14: Evolution of Musical Identities of Blues from 40s-90s

<!-- b000446 | prose | pages [17] -->
From the case oF Blues above, we’ve shown how the music is changed with the external circumstances across time. Also, changes can be identiﬁed in the model by all means: social environment changed people’s aesthetic tastes, political factors inﬂu- enced the popularity of genres and the content of music, while technological improve- ments changed music in its propogation channels as well as its methods of creating. All these could be observed based on our inﬂuence and similarity indicators as well as the musicial characteristics of all genres.

<!-- b000447 | heading | pages [17] -->
Test and Sensitivity Analysis

<!-- b000448 | prose | pages [17] -->
6

<!-- b000449 | heading | pages [17] -->
Sensitivity Analysis on the Average Window of Rescaled PageR-

<!-- b000450 | prose | pages [17] -->
6.1 ank

<!-- b000451 | prose | pages [17] -->
As discussed above, due to the limitation of the amount of musicians, the average window is narrower in (1) that discussed in [6]. How to determine the value of ∆p is needed to be discussed. The best way to determine it is to research its effect to its property of "Time-Balanced". Therefore, we observe how the mean and standard

<!-- b000452 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000453 | prose | pages [17] -->
关注数学模型 deviation of R30s(p) change under different ∆p shown in Fig.15.

<!-- b000454 | furniture | pages [17] -->
2

<!-- b000455 | furniture | pages [17] -->
MATHmodels

<!-- b000456 | furniture | pages [17] -->
获取更多资讯

<!-- b000457 | furniture | pages [18] -->
Team # 2101855

<!-- b000458 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000459 | furniture | pages [18] -->
Page 18 of 23

<!-- b000460 | prose | pages [18] -->
As presented in Fig.15a, with the increase of ∆p, the mean is converging to 0 and this process of rescaled actually turns into standardization, this will make R(p) lose its ability of horizontally compared with musicians from the same age. At the same time, standard deviation of R(p) increases. When ∆p approaches 0, R(p) →p, the process

<!-- b000461 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000462 | prose | pages [18] -->
can’t reverse the overestimation of old nodes.

<!-- b000463 | prose | pages [18] -->
So, a moderate value for ∆p is necessary. From the pattern of mean and standard deviation, we suppose that ∆p ∈[20, 35] may have a good time-balanced effect without weakening the ability of comparing horizontally.

<!-- b000464 | caption | pages [18] -->
Figure 15: Effect of Different ∆p

<!-- b000465 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000466 | prose | pages [18] -->
(a) Mean (b) Standard Deviation

<!-- b000467 | prose | pages [18] -->
Evidence from GCN: Can We Find More Information from the 6.2 Structure of Network?

<!-- b000468 | prose | pages [18] -->
In training process of getting weight vectors above, we discovered information from distance between nodes in the networks. However, with twenty types of music genres, in (4) we actually implicitly assumed that there only exists 6 different types in the real distribution of musicians. So we need to check if the structure of network itself contains enough information for us to separate it into twenty types. However, ordinary unsupervised learning methods including K-Means++, PCA and spectral decomposi- tion meet a failure to work due to the multiple of types, limited music characteristics and the property of small-world, which are even hard for us to ﬁnd clustering centers by all rules[11].

<!-- b000469 | prose | pages [18] -->
This drives us to raise a semi-supervised approach with model of neural networks which contains a little bit more information than our measure of similarity to check the idea. By the average PageRank score4 through their active years, twenty artists are picked out representing their genres. Among these musicians, there are The Beatles, T-Bones Walker, Roy Acuff etc. The full namelist is in the Table 5. With 20 labels, semi- supervised learning can be held based on analysis of graph structure to generate labels barely correlated with genres.

<!-- b000470 | prose | pages [18] -->
Based on [12], consider a two-layer GCN presented in forward model (8) and cross

<!-- b000471 | prose | pages [18] -->
4Though it’s not a better measure, it allows us to pick out musicians with great accumulative inﬂu- ence who are tend to affect more younger generations.

<!-- b000472 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000473 | prose | pages [18] -->
关注数学模型

<!-- b000474 | furniture | pages [18] -->
2

<!-- b000475 | furniture | pages [18] -->
MATHmodels

<!-- b000476 | furniture | pages [18] -->
获取更多资讯

<!-- b000477 | furniture | pages [19] -->
Team # 2101855

<!-- b000478 | prose | pages [19] -->
entropy error (9):

<!-- b000479 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000480 | furniture | pages [19] -->
Page 19 of 23

<!-- b000481 | prose | pages [19] -->
Z = f (X, A) = so f tmax( ˆAReLU( ˆAXW(0))W(0)) (8)

<!-- b000482 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000483 | prose | pages [19] -->
E = ∑

<!-- b000484 | prose | pages [19] -->
l∈yL ∑

<!-- b000485 | prose | pages [19] -->
f =1

<!-- b000486 | prose | pages [19] -->
FYl f ln Zl f (9)

<!-- b000487 | heading | pages [19] -->
2. W(0) ∈RC×H is

<!-- b000488 | prose | pages [19] -->
Where A is a symmetric adjacency matrix and ˆA = ˜D−1

<!-- b000489 | prose | pages [19] -->
2 ˜A ˜D−1 input-to-hidden weight matrix with H feature maps and W(1) ∈RH×F is hidden-to- output weight matrix. Some of principles are presented in Fig.16a. Again, by stochastic gradient descent, the weights matrices can be trained to ﬁnd the label.

<!-- b000490 | prose | pages [19] -->
By TensorFlow[13] we can calculate the labels for nodes in a relatively low time complexity. Some of clustering results are shown in Fig.16b. It can be found that the model has a relatively good recognition of mainstream genres, while it still can identify the genres with few musicians. This is probably because that most musicians were eas-

<!-- b000491 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000492 | prose | pages [19] -->
ily affected by pop stars even he/she had a different style. This endows the model with great ability of identifying Pop/Rock. Therefore, though it’s hard to determine miche music style in both models, less sample labels actually help reducing the misspeciﬁ- cation from overestimating the role of Pop/Rock music, as the network itself doesn’t contain enough information of doing so. This also supports the reasonableness of (4).

<!-- b000493 | caption | pages [19] -->
Figure 16: Principles and Results for GCN

<!-- b000494 | prose | pages [19] -->
(a) Graph Convolutional Network(Source:[12])

<!-- b000495 | prose | pages [19] -->
7

<!-- b000496 | heading | pages [19] -->
Strengths and Weaknesses

<!-- b000497 | prose | pages [19] -->
7.1

<!-- b000498 | heading | pages [19] -->
Strengths

<!-- b000499 | prose | pages [19] -->
(b) Results from GCN

<!-- b000500 | prose | pages [19] -->
• With a dynamic network, we consider a growing community of musicians which allows us to understand the evolution of musicians comprehensively.

<!-- b000501 | prose | pages [19] -->
• We measure the similarity from maximising the information in their community interactions, musical identities of works as well as the temporal characteristics which can make a good distinct between different genres overall.

<!-- b000502 | prose | pages [19] -->
• We modify the time-biased PageRank model and its measure of node importance was further optimised with a similarity metric that better represents the interplay

<!-- b000503 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000504 | prose | pages [19] -->
between musicians.

<!-- b000505 | prose | pages [19] -->
关注数学模型

<!-- b000506 | furniture | pages [19] -->
2

<!-- b000507 | furniture | pages [19] -->
MATHmodels

<!-- b000508 | furniture | pages [19] -->
获取更多资讯

<!-- b000509 | furniture | pages [20] -->
Team # 2101855

<!-- b000510 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000511 | furniture | pages [20] -->
Page 20 of 23

<!-- b000512 | prose | pages [20] -->
• We conducted detailed case studies, tests as well as sensitivity analysis to fully ensure the reasonableness and validity of our model.

<!-- b000513 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000514 | prose | pages [20] -->
7.2

<!-- b000515 | heading | pages [20] -->
Weaknesses

<!-- b000516 | prose | pages [20] -->
• Due to the limitation of data about musicians and their works, we can only mea- sure similarity and inﬂuence every decade, which may weaken the accuracy of the model without capturing more delicate dynamic information.

<!-- b000517 | prose | pages [20] -->
• Exogenous shock can be observed by outcomes presented by our model though, we don’t consider it in designing which could render bias in the ultimate rank of musicians across periods under different circumstances.

<!-- b000518 | prose | pages [20] -->
8

<!-- b000519 | heading | pages [20] -->
Further Discussion

<!-- b000520 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000521 | prose | pages [20] -->
In this project, we raised a measure of musicians’ inﬂuence by their importance in community and interactions between them. However, it should be noticed that based on the limitation of data, we had to make some assumptions that may not be too real- istic. They could reduce the credibility of our model. And provided with the following types of data, we can We can improve our model to better explore the patterns in the musician community:

<!-- b000522 | heading | pages [20] -->
1. Data of Lyrics: Though we traced the revolution of genres by its overall charac-

<!-- b000523 | prose | pages [20] -->
teristics, it’s hard to analyze its contents without lyrics especially for genres with relevance. Therefore, with data of lyrics, we can use methods including semantic analysis and sentiment analysis to show how ideas change in music, in order to bet- ter explore the relationship between musicians’ community inﬂuences and social inﬂuences.

<!-- b000524 | heading | pages [20] -->
2. Data of Audio: In the project, we are provided with overall indicators about charac-

<!-- b000525 | prose | pages [20] -->
teristics of musicians’ works. However, it is difﬁcult to discover the true similarities between the works through these quantitative indicators. If we could have audio information about these songs, algorithms including MFCC[14] and so on could be used to explore interactions between musicians better.

<!-- b000526 | prose | pages [20] -->
Overall, however, this model closely matches the data provided, and we believe with more data, it is bound to play a greater role in the future of related analysis.

<!-- b000527 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000528 | prose | pages [20] -->
关注数学模型

<!-- b000529 | furniture | pages [20] -->
2

<!-- b000530 | furniture | pages [20] -->
MATHmodels

<!-- b000531 | furniture | pages [20] -->
获取更多资讯

<!-- b000532 | furniture | pages [21] -->
Team # 2101855

<!-- b000533 | heading | pages [21] -->
Letter

<!-- b000534 | prose | pages [21] -->
To: Integrative Collective Music Society

<!-- b000535 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000536 | furniture | pages [21] -->
Page 21 of 23

<!-- b000537 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000538 | prose | pages [21] -->
From: Team 2101855 Date: February 8th, 2021 Subject: A better measure of music’s inﬂuence: updated rescaled PageRank

<!-- b000539 | prose | pages [21] -->
In the memo, we want to introduce you an alternate measure of music’s inﬂuence: updated rescaled PageRank. In fact, the PageRank has been used in measuring the importance of nodes in a network for long. However, it encounters some problem in tracing the evolution of music. Thus, we make the following imporvements to it.

<!-- b000540 | prose | pages [21] -->
Firstly, by taking corresponding nodes’ relative positions among contemporaries into account, we solve the problem of time-bias in growing networks including musi- cians’ community.

<!-- b000541 | prose | pages [21] -->
Secondly, we design a measure of similarity based on musical identities of musi-

<!-- b000542 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000543 | prose | pages [21] -->
cians’ works combining the structure of networks. And this measure has proven useful in ﬁnding musicians from the same genre.

<!-- b000544 | prose | pages [21] -->
Lastly, we replace the indegree in rescaled PageRank by similarity estimated above. This endows the model with more information from musical characteristics with a better effect of reversing time-bias.

<!-- b000545 | prose | pages [21] -->
By the measure above and corresponding tests, we’ve substantiated the effective- ness of our measure. Case studies are also held to illustrate the relationship between inﬂuence and similarity as well as how to trace the evolution and revolution of these genres by our approaches.

<!-- b000546 | prose | pages [21] -->
However, we admit that our method still have some ﬂaws more or less. The biggest problem among them is the limitation of data. Without data of new musicians, it’s hard to research into the network after 2000, which could also render bias in result from different periods.

<!-- b000547 | prose | pages [21] -->
In addition, the overview indicators of musical characteristics make it hard to ﬁnd more information from songs themselves. For example, it we have data about lyrics, we can trace the evolution of songs’ contents which reﬂect the trend of thoughts by algorithms for semantic analysis and sentiment analysis. And more detailed audio information about music can help more precisely compare similarities between genres with algorithms including MFCC etc.

<!-- b000548 | prose | pages [21] -->
After all, I believe that with our update, the rescaled PageRank algorithm is com- patible with the speciﬁcity of the musician community and captures the evolution of each genre effectively. We think it’s quite a useful tool for us to know about musi- cians as well the culture. So we wholeheartedly hope you consider our measure, and hopefully it will come in handy in real life applications.

<!-- b000549 | prose | pages [21] -->
Thank you!

<!-- b000550 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000551 | prose | pages [21] -->
关注数学模型

<!-- b000552 | furniture | pages [21] -->
2

<!-- b000553 | furniture | pages [21] -->
MATHmodels

<!-- b000554 | furniture | pages [21] -->
获取更多资讯

<!-- b000555 | furniture | pages [22] -->
Team # 2101855

<!-- b000556 | heading | pages [22] -->
References

<!-- b000557 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000558 | furniture | pages [22] -->
Page 22 of 23

<!-- b000559 | references | pages [22] -->
[1] Cano, P., Celma, O., Koppenberger, M., & Buldu, J. M. (2006). Topology of mu-

<!-- b000560 | references | pages [22] -->
微信公众号：数学模型

<!-- b000561 | references | pages [22] -->
sic recommendation networks. Chaos: An interdisciplinary journal of nonlinear

<!-- b000562 | references | pages [22] -->
science, 16(1), 013107.

<!-- b000563 | references | pages [22] -->
[2] Leskovec, J., Kleinberg, J., & Faloutsos, C. (2007). Graph evolution: Densiﬁcation

<!-- b000564 | references | pages [22] -->
and shrinking diameters. ACM transactions on Knowledge Discovery from Data

<!-- b000565 | references | pages [22] -->
(TKDD), 1(1), 2-es.

<!-- b000566 | references | pages [22] -->
[3] Rossetti, G. (2020) DyNetx: dynamic network analysis library, v0.2.1, Zenodo, doi:

<!-- b000567 | references | pages [22] -->
10.5281/zenodo.3953119.

<!-- b000568 | references | pages [22] -->
[4] Ren, Z. M., Mariani, M. S., Zhang, Y. C., & Medo, M. (2018). Randomizing growing

<!-- b000569 | references | pages [22] -->
networks with a time-respecting null model. Physical Review E, 97(5), 052311.

<!-- b000570 | references | pages [22] -->
[5] Mariani, M. S., Medo, M., & Zhang, Y. C. (2015). Ranking nodes in growing net-

<!-- b000571 | references | pages [22] -->
微信号：MATHmodels

<!-- b000572 | references | pages [22] -->
works: When PageRank fails. Scientiﬁc reports, 5(1), 1-10.

<!-- b000573 | references | pages [22] -->
[6] Mariani, M. S., Medo, M., & Zhang, Y. C. (2016). Identiﬁcation of milestone papers

<!-- b000574 | references | pages [22] -->
through time-balanced network centrality. Journal of Informetrics, 10(4), 1207-

<!-- b000575 | references | pages [22] -->
1223.

<!-- b000576 | references | pages [22] -->
[7] Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). The PageRank citation rank-

<!-- b000577 | references | pages [22] -->
ing: Bringing order to the web. Stanford InfoLab.

<!-- b000578 | references | pages [22] -->
[8] Bottou, L. (2012). Stochastic gradient descent tricks. In Neural networks: Tricks of

<!-- b000579 | references | pages [22] -->
the trade (pp. 421-436). Springer, Berlin, Heidelberg.

<!-- b000580 | references | pages [22] -->
[9] Burkholder, J. P., Grout, D. J., & Palisca, C. V. (2019). A History of Western Music:

<!-- b000581 | references | pages [22] -->
Tenth International Student Edition. WW Norton & Company.

<!-- b000582 | references | pages [22] -->
[10] Bromell, N. (2000). " The Blues and the Veil": the cultural work of musical form in

<!-- b000583 | references | pages [22] -->
blues and’60s rock. American Music, 193-221.

<!-- b000584 | references | pages [22] -->
[11] Kodinariya, T. M., & Makwana, P. R. (2013). Review on determining number of

<!-- b000585 | references | pages [22] -->
Cluster in K-Means Clustering. International Journal, 1(6), 90-95.

<!-- b000586 | references | pages [22] -->
[12] Kipf, T. N., & Welling, M. (2016). Semi-supervised classiﬁcation with graph con-

<!-- b000587 | references | pages [22] -->
volutional networks. arXiv preprint arXiv:1609.02907.

<!-- b000588 | references | pages [22] -->
[13] Abadi, M., Agarwal, A., Barham, P., Brevdo, E., Chen, Z., Citro, C., ... & Zheng,

<!-- b000589 | references | pages [22] -->
X. (2016). Tensorﬂow: Large-scale machine learning on heterogeneous distributed

<!-- b000590 | references | pages [22] -->
systems. arXiv preprint arXiv:1603.04467.

<!-- b000591 | references | pages [22] -->
[14] Logan, B. (2000, October). Mel frequency cepstral coefﬁcients for music modeling.

<!-- b000592 | references | pages [22] -->
In Ismir (Vol. 270, pp. 1-11).

<!-- b000593 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000594 | references | pages [22] -->
关注数学模型

<!-- b000595 | furniture | pages [22] -->
2

<!-- b000596 | furniture | pages [22] -->
MATHmodels

<!-- b000597 | furniture | pages [22] -->
获取更多资讯

<!-- b000598 | furniture | pages [23] -->
Team # 2101855

<!-- b000599 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000600 | furniture | pages [23] -->
Page 23 of 23

<!-- b000601 | heading | pages [23] -->
Appendix A: Information of Dynamic Networks

<!-- b000602 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000603 | caption | pages [23] -->
Table 4: Descriptive Statistics of Dynamic Networks

<!-- b000604 | prose | pages [23] -->
n t

<!-- b000605 | prose | pages [23] -->
0 246 1 625 2 1304 3 2562 4 3584 5 4645 6 5479 7 5593

<!-- b000606 | prose | pages [23] -->
m k

<!-- b000607 | prose | pages [23] -->
129 0.524 826 1.322 3506 2.609 10149 3.961 16962 4.733 25448 5.474 36446 6.647 41956 7.496

<!-- b000608 | prose | pages [23] -->
Note: n is the Number of Nodes, m is the Number of Edges, k is the Average Degree. Note that diameter and mean geodesic distance can’t be calculated here as for early

<!-- b000609 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000610 | prose | pages [23] -->
times, the networks weren’t connected, which can also be seen in 1a.

<!-- b000611 | heading | pages [23] -->
Appendix B: Namelist of "Benchmark" Artists in GCN

<!-- b000612 | caption | pages [23] -->
Table 5: Benchmark Artists

<!-- b000613 | prose | pages [23] -->
Avant-Garde Blues Terry Riley T-Bone Walker Comedy/Spoken Country Spike Jones Roy Acuff Folk International Woody Guthrie Ravi Shankar New Age Pop/Rock Mike Oldﬁeld The Beatles Stage&Screen Religious Sister Rosetta Tharpe Harold Arlen

<!-- b000614 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000615 | prose | pages [23] -->
Childrens Classical Alvin&The Chipmunks John Cage Easy Listening Electronic Bert Kaempfert Kraftwerk Jazz Latin Cab Calloway Lecuona Cuban Boys R&B Reggae Ray Charles Lord Invader Vocal Unknown The Bothy Band Billie Holiday

<!-- b000616 | prose | pages [23] -->
关注数学模型

<!-- b000617 | furniture | pages [23] -->
2

<!-- b000618 | furniture | pages [23] -->
MATHmodels

<!-- b000619 | furniture | pages [23] -->
获取更多资讯
