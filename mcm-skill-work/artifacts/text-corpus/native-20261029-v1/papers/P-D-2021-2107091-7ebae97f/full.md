# P-D-2021-2107091-7ebae97f

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
2107091

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
How Does Musical Inﬂuence Lead to Musical Revolution?

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
During the revolution of music, interactions within and between genres can have a critical impact on the direction of musical change. In this paper, we develop models to analyze the inﬂuence between musicians, measure the degree of similarity between music, and reveal the changes in genres over time, as well as the inﬂuence of social, cultural, and historical aspects.

<!-- b000013 | prose | pages [1] -->
In TASK 1: First, we take each musician as a node and calculate the directed inﬂuence be- tween musicians as weights by considering the factors of time span and genre span to build a directed music inﬂuence network. Then we use social network analysis (SNA) to ana- lyze the inﬂuence network. The Degree Centrality of musicians in the network is calculated, and the Pagerank-modiﬁed eigenvector centrality is further used to measure the inﬂuence of musicians(MI), obtaining that Bob Dylan, The Rolling Stones, Chuck Berry, and Elvis Presley have the highest inﬂuence. We also ﬁnd that MI obeys power-law distribution, implying that

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
the inﬂuence network between inﬂuencers and followers is a scale-free network. Finally, we explore the sub-network to analyze the meaning of the subset of MI.

<!-- b000016 | prose | pages [1] -->
In TASK 2 & 3: First, we use Cosine similarity and Euclidean similarity to measure global similarity Sglobal and local similarity Spart in two aspects of music, and consider the inﬂuence of popular trends to build Multi-dimensional music similarity evaluation model to measure the similarity of music (MS). Music within genres is found to be more similar than between genres. Then, to investigate the distinguishing features of genres, we combine different features and built the Discrimination evaluation model of feature combination to select the feature combinations that better distinguish genres from each other. Finally, we analyze changes in genres over time.

<!-- b000017 | prose | pages [1] -->
In TASK 4: To investigate whether the inﬂuencers actually inﬂuence the followers’ music, we develop a Long-short term inﬂuence model based on sliding window to calculate the inﬂuence degree score (IDS), considering the time sequence of release of the followers’ music and the inﬂuencers’ music, and determine the inﬂuence threshold. The result shows that follow- ers are indeed inﬂuenced by the inﬂuencers. Subsequently, to determine the "contagiousness" of speciﬁc musical characteristics to musicians, we also consider speciﬁc musical characteristics, analyze the degree of closeness (DC) of characteristics of followers’ and inﬂuencers’ music, and establish the Contagious evaluation model of musical characteristics to ﬁnd the most contagious musical characteristics for different followers.

<!-- b000018 | prose | pages [1] -->
In TASK 5 & 6 & 7: First we establish constraint equations to identify musical revolution points based on the musical characteristics of the genre and the number of musicians in the genre. And based on the popularity before and after the musical revolution point to identify the main inﬂuencers in the musical revolution. Then we take 10 years as the examination period to calculate the IDS of the analyzed object to everyone within the genre based on the IDS in Task 4, and weight the sum to get the dynamic inﬂuencer index (DII) for identifying the leading ﬁgures within the genre in different generations. Ultimately, we analyze the relationship between music and politics, culture, and society.

<!-- b000019 | prose | pages [1] -->
Finally, we perform a sensitivity analysis of the model and investigate the effect of changes in the variable parameters of the model on the results.

<!-- b000020 | keywords | pages [1] -->
Keywords: SNA, Slide Window, Scale-free Network, Pareto’s Principle, PageRank, Combina-

<!-- b000021 | prose | pages [1] -->
tion of Features

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
3 Background and Problem Statement . . . . . . . . . . . . . . . . . . . . . . . 1.1 3

<!-- b000032 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000033 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Our work

<!-- b000034 | prose | pages [2] -->
2

<!-- b000035 | heading | pages [2] -->
Preparation of the Models

<!-- b000036 | prose | pages [2] -->
3

<!-- b000037 | prose | pages [2] -->
3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1

<!-- b000038 | heading | pages [2] -->
Assumptions

<!-- b000039 | prose | pages [2] -->
3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2

<!-- b000040 | heading | pages [2] -->
Notations

<!-- b000041 | prose | pages [2] -->
4

<!-- b000042 | prose | pages [2] -->
TASK 1: Musical Inﬂuence Network Analysis Based on SNA 3 4 Data Processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 Model Overview 4 Musical Inﬂuence Network Analysis Based on SNA . . . . . . . . . . . . . . . 3.3 5 Establishment of Musical Inﬂuence Network and Analysis Using SNA . 3.3.1 5 Model Test on Musical Inﬂuence Network . . . . . . . . . . . . . . . . 3.3.2 7 Analysis of The Result . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 7

<!-- b000043 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000044 | prose | pages [2] -->
Analysis of Musical Inﬂuence Sub-network . . . . . . . . . . . . . . . . . . . 3.5 8

<!-- b000045 | heading | pages [2] -->
TASK 2 & 3: Multi-dimensional Music Similarity Evaluation Model

<!-- b000046 | prose | pages [2] -->
4 9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Model Overview 9 Establishment of Multi-dimensional Music Similarity Evaluation Model . . . . 4.2 10 Global Similarity of Music . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 10 Partial Similarity of Music . . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 10 Fashion Trends Impact Factor . . . . . . . . . . . . . . . . . . . . . . 4.2.3 11 Evaluation of Music Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 11 Analysis of the Musical Discrimination and Inﬂuences of Genres . . . . . . . . 4.4 13 Discrimination Evaluation Model of Feature Combination . . . . . . . 4.4.1 13 Analysis of Genre Changes Over Time 4.4.2 . . . . . . . . . . . . . . . . .

<!-- b000047 | prose | pages [2] -->
15

<!-- b000048 | heading | pages [2] -->
Task 4 :Long-Short Term Inﬂuence Evaluation Model Based on Sliding Window

<!-- b000049 | prose | pages [2] -->
5 16 Establishment of Sliding Window Model . . . . . . . . . . . . . . . . . . . . . 5.1 16 Test of the Established Model . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 17 Contagious Evaluation of Musical Characteristics . . . . . . . . . . . . . . . . 5.3 18

<!-- b000050 | prose | pages [2] -->
Task 5 & 6 & 7: Analysis of Music Revolution Over Time 6 18 The Identiﬁcation of the Musical revolution . . . . . . . . . . . . . . . . . . . 6.1 18 . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 Major Inﬂuencers of Revolution 20 Dynamic Inﬂuencer Evaluation Indicator . . . . . . . . . . . . . . . . . . . . . 6.3 20 Inﬂuence from Social, Political and Cultural Aspects 6.4

<!-- b000051 | prose | pages [2] -->
7 Sensitive Analysis 7.1 Sensitive Analysis of Model in TASK 2 7.2 Sensitive Analysis of Model in TASK 4

<!-- b000052 | prose | pages [2] -->
8

<!-- b000053 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000054 | prose | pages [2] -->
. . . . . . . . . . . . . .

<!-- b000055 | prose | pages [2] -->
21

<!-- b000056 | prose | pages [2] -->
22 . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | prose | pages [2] -->
22 . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | prose | pages [2] -->
22

<!-- b000059 | prose | pages [2] -->
24 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 Strengths 24 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2

<!-- b000060 | heading | pages [2] -->
References

<!-- b000061 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000062 | heading | pages [2] -->
MEMO

<!-- b000063 | prose | pages [2] -->
24

<!-- b000064 | prose | pages [2] -->
24

<!-- b000065 | prose | pages [2] -->
25关注数学模型

<!-- b000066 | furniture | pages [2] -->
2

<!-- b000067 | furniture | pages [2] -->
MATHmodels

<!-- b000068 | furniture | pages [2] -->
获取更多资讯

<!-- b000069 | furniture | pages [3] -->
Team # 2107091

<!-- b000070 | prose | pages [3] -->
1

<!-- b000071 | heading | pages [3] -->
Introduction

<!-- b000072 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000073 | furniture | pages [3] -->
Page 3 of 25

<!-- b000074 | heading | pages [3] -->
Background and Problem Statement

<!-- b000075 | prose | pages [3] -->
1.1

<!-- b000076 | prose | pages [3] -->
Music is a cultural product that people use to express their emotions and relax their bod-

<!-- b000077 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000078 | prose | pages [3] -->
ies and minds. The inﬂuence of musicians on each other has a very important impact on the development and evolution of music. The development of computer technology allows us un- precedented access to data and computing power to analyze the network of inﬂuences between musicians, from which we can extract and analyze the key factors that inﬂuence the process of musical development, which will also help us understand the meaning of music better. In this problem, we need to accomplish the following objectives:

<!-- b000079 | prose | pages [3] -->
• Create a music inﬂuence network to analyze the inﬂuence between musicians and capture the music inﬂuence parameters in the inﬂuence network.

<!-- b000080 | prose | pages [3] -->
• Develop similarity evaluation model to explore the degree of inﬂuence and similarity between or within genres and between musicians.

<!-- b000081 | prose | pages [3] -->
• Identify indicators of revolution in genres and analyze the interplay between them in

<!-- b000082 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000083 | prose | pages [3] -->
relation to society, politics, and culture.

<!-- b000084 | prose | pages [3] -->
• Applying a dynamic analysis of the similarities and inﬂuences between and within genres of musicians over time.

<!-- b000085 | prose | pages [3] -->
1.2 Our work

<!-- b000086 | prose | pages [3] -->
The work we have done in this problem is mainly shown in the following Figure(1).

<!-- b000087 | prose | pages [3] -->
Musical Influence Network Analysis based on SNA

<!-- b000088 | prose | pages [3] -->
Influence Type

<!-- b000089 | prose | pages [3] -->
Time Span Influence

<!-- b000090 | prose | pages [3] -->
Genre Span influence

<!-- b000091 | prose | pages [3] -->
Data Processing

<!-- b000092 | prose | pages [3] -->
SNA Network Analysis

<!-- b000093 | prose | pages [3] -->
Multi-dimensional Music Similarity

<!-- b000094 | prose | pages [3] -->
What Distinguishes a Genre

<!-- b000095 | prose | pages [3] -->
influence_data

<!-- b000096 | prose | pages [3] -->
Genre Changes Over Time

<!-- b000097 | prose | pages [3] -->
Degree Centrality

<!-- b000098 | prose | pages [3] -->
data_by_artist

<!-- b000099 | prose | pages [3] -->
Moditied Eigenvector Centrality

<!-- b000100 | prose | pages [3] -->
+

<!-- b000101 | prose | pages [3] -->
Degree CentraPareto Principle

<!-- b000102 | prose | pages [3] -->
data_by_year

<!-- b000103 | prose | pages [3] -->
Power-law Distribution

<!-- b000104 | prose | pages [3] -->
+

<!-- b000105 | prose | pages [3] -->
Analysis Sub-Network

<!-- b000106 | prose | pages [3] -->
full_music_data

<!-- b000107 | prose | pages [3] -->
Music Similarity

<!-- b000108 | prose | pages [3] -->
Global Similarity

<!-- b000109 | prose | pages [3] -->
Data Processing

<!-- b000110 | prose | pages [3] -->
Partial Similarity

<!-- b000111 | heading | pages [3] -->
Long-Short Term Influence Evaluation Model based on Sliding Window

<!-- b000112 | prose | pages [3] -->
Influencers Actually Affect Followers’ Music Musical Characteristics’ Contagious

<!-- b000113 | prose | pages [3] -->
Musical Revolution Music Evolution Dynamic Influencer  Indicator

<!-- b000114 | prose | pages [3] -->
Influence of Social, Politics or Technology

<!-- b000115 | caption | pages [3] -->
Figure 1: Our Work

<!-- b000116 | prose | pages [3] -->
2

<!-- b000117 | heading | pages [3] -->
Preparation of the Models

<!-- b000118 | prose | pages [3] -->
2.1

<!-- b000119 | heading | pages [3] -->
Assumptions

<!-- b000120 | prose | pages [3] -->
We made the following assumptions to help us with our modeling. These assumptions are the promise of our subsequent analysis.

<!-- b000121 | prose | pages [3] -->
• Assuming that the data is accurate and there is no falsiﬁed data: This means our analysis accords with the truth.

<!-- b000122 | prose | pages [3] -->
• Assuming that followers can only be inﬂuenced by songs released before the current year, and that songs after the current year have no effect on the follower’s for that year: this is done

<!-- b000123 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000124 | prose | pages [3] -->
关注数学模型 to measure the true inﬂuenceability of the inﬂuencers in a sliding window model.

<!-- b000125 | furniture | pages [3] -->
2

<!-- b000126 | furniture | pages [3] -->
MATHmodels

<!-- b000127 | furniture | pages [3] -->
获取更多资讯

<!-- b000128 | furniture | pages [4] -->
Team # 2107091

<!-- b000129 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000130 | furniture | pages [4] -->
Page 4 of 25

<!-- b000131 | prose | pages [4] -->
• Assuming that the decade when the musician begin his carrer is the year when they debut, because the accurate years when the musicians debut are not given.

<!-- b000132 | prose | pages [4] -->
• Assuming that the musician’s genre is limited to the genre provided by the data, and have no genre changes, that all his/her songs are in the style of his or her genre

<!-- b000133 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000134 | prose | pages [4] -->
2.2

<!-- b000135 | heading | pages [4] -->
Notations

<!-- b000136 | prose | pages [4] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000137 | caption | pages [4] -->
Table 1: Parameter Settings

<!-- b000138 | prose | pages [4] -->
parameter

<!-- b000139 | prose | pages [4] -->
T DCi ECi MI Sglobal Spart

<!-- b000140 | prose | pages [4] -->
description

<!-- b000141 | prose | pages [4] -->
time-span inﬂuence factor degree centrality eigenvector centrality music inﬂuence global similarity partial similarity

<!-- b000142 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000143 | prose | pages [4] -->
V (i) MS SMS LMS IDS DC DII music feature vector multi-similarity short-term similarity long-term similarity inﬂuence degree score degree of closeness dynamic inﬂuencer indicator

<!-- b000144 | prose | pages [4] -->
TASK 1: Musical Inﬂuence Network Analysis Based on 3 SNA

<!-- b000145 | prose | pages [4] -->
3.1

<!-- b000146 | heading | pages [4] -->
Data Processing

<!-- b000147 | prose | pages [4] -->
An overview of the given data shows that some songs are sung by more than one person (e.g. It Can’t Happen Here and I Wonder If I Take You Home), and such songs cannot reﬂect the characteristics of a single musician, so to avoid disturbing the model, we remove the data of a total of 4410 chorus songs (4.4% of the original data). Since there are singers with only choral music, they have no music data after the deletion of choral music, which are invalid data. We remove these people, including those who are not shared between two dataset, to prevent any effect on the model. The data processing is shown in the Figure(2).

<!-- b000148 | prose | pages [4] -->
Data processing

<!-- b000149 | prose | pages [4] -->
•Removing the chorus song: 4410 songs(4% of the dateset) •(songs cannot reflect the characteristics of a single musician)

<!-- b000150 | prose | pages [4] -->
step1

<!-- b000151 | prose | pages [4] -->
• Removing 174 musicians not shared between two datasets

<!-- b000152 | prose | pages [4] -->
step2

<!-- b000153 | caption | pages [4] -->
Figure 2: Data Processing

<!-- b000154 | prose | pages [4] -->
3.2

<!-- b000155 | heading | pages [4] -->
Model Overview

<!-- b000156 | prose | pages [4] -->
To analyze the musical inﬂuences among musicians, we establish a directed network of

<!-- b000157 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000158 | prose | pages [4] -->
musical inﬂuences with each musician as a node and directional inﬂuences among musicians as关注数学模型

<!-- b000159 | furniture | pages [4] -->
2

<!-- b000160 | furniture | pages [4] -->
MATHmodels

<!-- b000161 | furniture | pages [4] -->
获取更多资讯

<!-- b000162 | furniture | pages [5] -->
Team # 2107091

<!-- b000163 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000164 | furniture | pages [5] -->
Page 5 of 25

<!-- b000165 | prose | pages [5] -->
weights. We then further explore the inﬂuence among musicians using social network analysis (SNA) to capture the music inﬂuence in the network to measure the inﬂuence of each musician. Finally, we explore the sub-networks of the inﬂuence network and explore the signiﬁcance of music inﬂuence in the sub-networks.

<!-- b000166 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000167 | prose | pages [5] -->
Musical Inﬂuence Network Analysis Based on SNA 3.3

<!-- b000168 | prose | pages [5] -->
Establishment of Musical Inﬂuence Network and Analysis Using SNA 3.3.1

<!-- b000169 | prose | pages [5] -->
▶Establishment of Musical Inﬂuence Network

<!-- b000170 | prose | pages [5] -->
The directed graph can be well used to describe the mutual inﬂuence relationship among musicians. Based on the relationship between inﬂuencers and followers among musicians given by inﬂuence_data, we build a directed network of musical inﬂuence among musicians with each musician as a node and the directed inﬂuence among musicians as a weight.

<!-- b000171 | prose | pages [5] -->
Exploring the data reveals that the types of inﬂuence between musicians are divided into two categories: inﬂuence within the same genre and inﬂuence among different genres. Inﬂuence

<!-- b000172 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000173 | prose | pages [5] -->
among musicians exists not only that a predecessor inﬂuences a junior, but also that a junior inﬂuences a predecessor. Therefore, we classify the types of inter-musician inﬂuence as follows.

<!-- b000174 | prose | pages [5] -->
From genre span: Inﬂuence occurs within the same genre and between different genres.

<!-- b000175 | prose | pages [5] -->
From time span: Junior inﬂuences predecessor and predecessor inﬂuences junior.

<!-- b000176 | prose | pages [5] -->
Fully considering the difference between the span of genres and the span of time in which the inﬂuence occurs, we deﬁne the weight of each side of the music inﬂuence network:

<!-- b000177 | prose | pages [5] -->
• Time span impact factor

<!-- b000178 | prose | pages [5] -->
Assuming that existing musician i inﬂuences musician j, the time difference ∆t is deﬁned as follows:

<!-- b000179 | prose | pages [5] -->
∆t = t j −ti (1)

<!-- b000180 | prose | pages [5] -->
where ti and tj are the debut times of musician i and musician j, respectively.

<!-- b000181 | prose | pages [5] -->
In general, juniors are more likely to be inﬂuenced by predecessors as they grow up, while predecessors are less likely to be inﬂuenced by juniors. Therefore, we can conclude that the probability of the older generation being inﬂuenced by the younger generation is lower. And if this happens, it means the inﬂuence of the younger generation is very strong. Compared to predecessors inﬂuencing juniors, juniors inﬂuencing predecessors should be considered that the juniors have a stronger inﬂuence. We therefore deﬁne the time-span inﬂuence factor T as follows

<!-- b000182 | prose | pages [5] -->
{

<!-- b000183 | prose | pages [5] -->
−β∆t,

<!-- b000184 | prose | pages [5] -->
T =

<!-- b000185 | prose | pages [5] -->
∆t, if ∆t < 0 (2) if ∆t ≥0

<!-- b000186 | prose | pages [5] -->
In equation(2), β is a set parameter and β > 1, indicating the difference in the effect of the two inﬂuence categories.

<!-- b000187 | prose | pages [5] -->
• Genre span impact factor

<!-- b000188 | prose | pages [5] -->
Generally speaking, musicians in the same genre are more likely to inﬂuence each other because they share the same direction and research areas. In contrast, musicians from different genres are less likely to inﬂuence each other because their work styles rarely overlap. There- fore, we argue that cross-genre inﬂuencers have stronger inﬂuence compared to within-genre inﬂuencers. The genre-spanning inﬂuence factor aij between inﬂuencer i and follower j is given as follows:

<!-- b000189 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000190 | prose | pages [5] -->
关注数学模型

<!-- b000191 | furniture | pages [5] -->
2

<!-- b000192 | furniture | pages [5] -->
MATHmodels

<!-- b000193 | furniture | pages [5] -->
获取更多资讯

<!-- b000194 | furniture | pages [6] -->
Team # 2107091

<!-- b000195 | prose | pages [6] -->
{

<!-- b000196 | prose | pages [6] -->
1,

<!-- b000197 | prose | pages [6] -->
aij =

<!-- b000198 | prose | pages [6] -->
0,

<!-- b000199 | prose | pages [6] -->
• Edge weights of a directed graph

<!-- b000200 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000201 | furniture | pages [6] -->
Page 6 of 25

<!-- b000202 | prose | pages [6] -->
cross-genre (3) within-genre

<!-- b000203 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000204 | prose | pages [6] -->
Combining the above analysis on the time span and genre span impact factors, we give the formula for the directed graph weights wi j as follows:

<!-- b000205 | prose | pages [6] -->
T

<!-- b000206 | prose | pages [6] -->
wij = (1+aij)·e

<!-- b000207 | prose | pages [6] -->
(4) 80

<!-- b000208 | prose | pages [6] -->
In equation(4), wij is the weight of the directed edge between musician nodes i to j. The time interval |∆t| between the inﬂuencer and the inﬂuenced is at most 80, so T is normalized using T

<!-- b000209 | prose | pages [6] -->
80. wij also represents the intensity of the inﬂuence of musician i on musician j. The larger the value of wij, the stronger the intensity of musician i’s inﬂuence.

<!-- b000210 | prose | pages [6] -->
▶SNA Network Analysis Method

<!-- b000211 | prose | pages [6] -->
In order to capture the musical inﬂuence in the established musical inﬂuence directed net- work, we analyze the directed network using social network analysis (SNA) method[1]. The inﬂuence of each musician is measured and analyzed by calculating the Degree Centrality of

<!-- b000212 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000213 | prose | pages [6] -->
each musician in the musical inﬂuence directed network and further calculating the Eigenvector Centrality modiﬁed by the PageRank idea. The speciﬁc steps are as follows:

<!-- b000214 | prose | pages [6] -->
Step 1: Calculating Degree Centrality

<!-- b000215 | prose | pages [6] -->
In an undirected network, the degree of a node can be used to measure the centrality of that point. Analogously, in the music inﬂuence directed network we built, we can use the sum of the out-degree weights of a node to measure the importance of a node’s inﬂuence at the microscopic level. The assumption behind this metric is that nodes with many connections are important nodes, which means that musicians who have an impact on more people have a stronger inﬂuence. We therefore give the deﬁnition of degree centrality (DCi) for point i as shown in the equation(5)

<!-- b000216 | prose | pages [6] -->
DCi =

<!-- b000217 | prose | pages [6] -->
n n ∑ ∑

<!-- b000218 | prose | pages [6] -->
wijdij (5)

<!-- b000219 | prose | pages [6] -->
j=1

<!-- b000220 | prose | pages [6] -->
In equation(5) n represents the total number of nodes in the network and di j denotes the existence of directed edges between node i to node j. And di j is deﬁned as follows:

<!-- b000221 | prose | pages [6] -->
{

<!-- b000222 | prose | pages [6] -->
1, no directed edge from i to j

<!-- b000223 | prose | pages [6] -->
di j =

<!-- b000224 | prose | pages [6] -->
0, (6) there is directed edge from i to j

<!-- b000225 | prose | pages [6] -->
Step 2: Calculating Eigenvector Centrality

<!-- b000226 | prose | pages [6] -->
The importance of a node depends both on the number of its neighboring nodes and on the importance of its neighboring nodes. This means that the more important the nodes connected to node i, the more important node i will be. We deﬁne the eigenvector centrality ECi to measure the importance of node i at the macro level, as shown in the iterative equation(7)

<!-- b000227 | prose | pages [6] -->
iterative equation:

<!-- b000228 | prose | pages [6] -->
n ∑

<!-- b000229 | prose | pages [6] -->
ECi = λ

<!-- b000230 | prose | pages [6] -->
di jEC j (7)

<!-- b000231 | prose | pages [6] -->
j=1

<!-- b000232 | prose | pages [6] -->
where lambda is a scaling constant and the initial value of the iteration is set in the equa- tion(8) j = 1 ∼n EC j = DC j, initial value:

<!-- b000233 | prose | pages [6] -->
(8) However, for the directed network we build, the above analysis process only takes the im- portance of neighboring nodes into account. To increase the inﬂuence of the nodes themselves on the outside, we modify the equation based on the PageRank idea.

<!-- b000234 | prose | pages [6] -->
PageRank[2] is an algorithm proposed by Sergey Brin and Lawrence Page to rank the im-

<!-- b000235 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000236 | prose | pages [6] -->
portance of nodes in a network. The PageRank algorithm assumes that a node exerts inﬂuence关注数学模型

<!-- b000237 | furniture | pages [6] -->
2

<!-- b000238 | furniture | pages [6] -->
MATHmodels

<!-- b000239 | furniture | pages [6] -->
获取更多资讯

<!-- b000240 | furniture | pages [7] -->
Team # 2107091

<!-- b000241 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000242 | furniture | pages [7] -->
Page 7 of 25

<!-- b000243 | prose | pages [7] -->
on the system is the result of its own inﬂuence combining with the results of its followers’ inﬂu- ences. Therefore, we modify the model shown in the following equation: Therefore, we modify the model shown in the following equation:

<!-- b000244 | prose | pages [7] -->
n

<!-- b000245 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000246 | prose | pages [7] -->
∑

<!-- b000247 | prose | pages [7] -->
ECi = λ iterative equation:

<!-- b000248 | prose | pages [7] -->
di jEC j +(1−λ)ECi (9)

<!-- b000249 | prose | pages [7] -->
j=1

<!-- b000250 | prose | pages [7] -->
After several iterations, ECi converges to a ﬁxed value E′

<!-- b000251 | prose | pages [7] -->
(MIi) of musician i as follows:

<!-- b000252 | prose | pages [7] -->
MIi =

<!-- b000253 | prose | pages [7] -->
max{E′

<!-- b000254 | prose | pages [7] -->
Ci. We deﬁne the musical inﬂuence

<!-- b000255 | prose | pages [7] -->
E′

<!-- b000256 | prose | pages [7] -->
Ci

<!-- b000257 | prose | pages [7] -->
(10) C j, j = 1,2,··· ,n}

<!-- b000258 | heading | pages [7] -->
Model Test on Musical Inﬂuence Network

<!-- b000259 | prose | pages [7] -->
3.3.2 Using all data given in the inﬂuence_data, the musical inﬂuence (MI) of each musician is calculated, and the MI of somes musician are shown in the Table(2).

<!-- b000260 | caption | pages [7] -->
Table 2: MI of Musicians

<!-- b000261 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000262 | prose | pages [7] -->
MI Musician The Beatles 1 The Rolling Stones 0.546 Hank Williams 0.424 Jimi Hendrix 0.397 MI Musician Bob Dylan 0.738 Chuck Berry 0.5 Elvis Presley 0.424 Little Richard 0.39 The Velvet Underground James Brown 0.387 0.356

<!-- b000263 | prose | pages [7] -->
As can be seen from the above table, The Beatles has the highest MI, followed by Bob Dylan, The Rolling Stones, Chuck Berry, Elvis Presley and so on. The similarity between the most inﬂuential musicians we analyzed and The 20 Most Representative Musicians in the World Jointly selected by CNN and Songlines[3] (a world-class music publication) is relatively high. We can conclude that the establishment and analysis process of the model is accurate, reasonable and feasible.

<!-- b000264 | prose | pages [7] -->
3.4

<!-- b000265 | heading | pages [7] -->
Analysis of The Result

<!-- b000266 | prose | pages [7] -->
Most real-world networks are not random networks, and a few nodes tend to have a large number of connections, while most nodes have only a small number of connections, generally obeying the Pareto Principle law[4]. Complex networks with degree distribution conforming to power-law distribution are usually called scale-free networks[5].

<!-- b000267 | prose | pages [7] -->
In section 3.2.3, we calculated the musical inﬂuence (MI) of each musician. A line graph of the frequency distribution of MI is plotted as shown in the blue solid line in the Figure(3).

<!-- b000268 | caption | pages [7] -->
Figure 3: The Frequency Distribution of MI

<!-- b000269 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000270 | prose | pages [7] -->
关注数学模型

<!-- b000271 | furniture | pages [7] -->
2

<!-- b000272 | furniture | pages [7] -->
MATHmodels

<!-- b000273 | furniture | pages [7] -->
获取更多资讯

<!-- b000274 | furniture | pages [8] -->
Team # 2107091

<!-- b000275 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000276 | furniture | pages [8] -->
Page 8 of 25

<!-- b000277 | prose | pages [8] -->
To investigate the nature of the MI distribution, we ﬁt the frequency distribution curve of MI. Observe that the distribution of MI in the ﬁgure resembles a power-law distribution, so the complementary cumulative distribution function of the power-law distribution is deﬁned as equation(11)

<!-- b000278 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000279 | prose | pages [8] -->
P(X|X > x) = cx−a, c > 0,a > 0 (11)

<!-- b000280 | prose | pages [8] -->
We solve for the power-law distribution parameters using the maximum likelihood estima- tion, and the distribution parameters at a conﬁdence level of 95% are shown in the Table(3).

<!-- b000281 | caption | pages [8] -->
Table 3: Distribution Parameters

<!-- b000282 | prose | pages [8] -->
estimated value distribution parameter c 95% Conﬁdence interval 0.001173 α (0.0009809, 0.001366) -1.526 (-1.565, -1.488)

<!-- b000283 | prose | pages [8] -->
With the goodness of ﬁt R2 = 0.9931, we can consider that the Musical Inﬂuence Network

<!-- b000284 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000285 | prose | pages [8] -->
is a scale-free network. Musical inﬂuence network obeys the law of Pareto Principle, i.e., only a small number of musicians inﬂuence many other musicians, while most musicians do not inﬂuence other musicians. This also means that a small number of highly inﬂuential musicians will have an impact on the music world. And this will be analyzed in detail in the subsequent analysis.

<!-- b000286 | prose | pages [8] -->
Analysis of Musical Inﬂuence Sub-network 3.5

<!-- b000287 | prose | pages [8] -->
In the model building process, we categorize time span and genre span: inﬂuence within genre, inﬂuence across genre, inﬂuence of predecessors on juniors, and inﬂuence of juniors on predecessors. We build independent sub-networks on genre and time span separately and use SNA analysis to explore each musician’s inﬂuence on predecessors and on juniors EIpre & EIjun, inﬂuence within and across genres EIwit & EIout. EIpre, EIjun, EIwit, and EIout are all subsets of the total inﬂuence EI.

<!-- b000288 | prose | pages [8] -->
The cross-genre inﬂuence data, within-genre inﬂuence data, predecessor inﬂuence data, and juniors inﬂuence data are selected from inﬂuence_data, respectively, to establish the musical inﬂuence sub network. Then the musical inﬂuences are calculated separately and normalized. The results of the calculation of each type of inﬂuence and the musical inﬂuence sub-network are shown in the Figure(4).

<!-- b000289 | prose | pages [8] -->
In the Figure(4), the size of nodes in each subnetwork represents the MI of the correspond- ing type of singer, while the thickness of the directed curve represents the weight of inﬂuence. As can be seen from the Figure(4), the occurrence frequency of inﬂuence within genres is higher than that between genres, and the occurrence frequency of inﬂuence of predecessors on their successors is higher than that of the latter on their predecessors. It can be concluded that in the interaction of musicians, musicians are more likely to inﬂuence musicians in the same genre, and musicians are more likely to inﬂuence younger generations rather than predecessors. It can also be seen from The MI subseries that The Beatles and Bob Dylan have a huge inﬂuence on musicians both in and out of The genre, and Bob Dylan goes one step further and has a strong inﬂuence on his predecessors as well.

<!-- b000290 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000291 | prose | pages [8] -->
关注数学模型

<!-- b000292 | furniture | pages [8] -->
2

<!-- b000293 | furniture | pages [8] -->
MATHmodels

<!-- b000294 | furniture | pages [8] -->
获取更多资讯

<!-- b000295 | furniture | pages [9] -->
Team # 2107091

<!-- b000296 | furniture | pages [9] -->


<!-- b000297 | furniture | pages [9] -->


<!-- b000298 | prose | pages [9] -->
e

<!-- b000299 | furniture | pages [9] -->


<!-- b000300 | furniture | pages [9] -->


<!-- b000301 | furniture | pages [9] -->


<!-- b000302 | furniture | pages [9] -->


<!-- b000303 | furniture | pages [9] -->


<!-- b000304 | furniture | pages [9] -->


<!-- b000305 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000306 | furniture | pages [9] -->
Page 9 of 25

<!-- b000307 | furniture | pages [9] -->


<!-- b000308 | furniture | pages [9] -->


<!-- b000309 | furniture | pages [9] -->


<!-- b000310 | furniture | pages [9] -->


<!-- b000311 | furniture | pages [9] -->


<!-- b000312 | prose | pages [9] -->
s

<!-- b000313 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000314 | furniture | pages [9] -->


<!-- b000315 | prose | pages [9] -->
Michael

<!-- b000316 | furniture | pages [9] -->


<!-- b000317 | furniture | pages [9] -->


<!-- b000318 | furniture | pages [9] -->


<!-- b000319 | furniture | pages [9] -->


<!-- b000320 | furniture | pages [9] -->


<!-- b000321 | prose | pages [9] -->
Mile

<!-- b000322 | furniture | pages [9] -->


<!-- b000323 | furniture | pages [9] -->


<!-- b000324 | furniture | pages [9] -->


<!-- b000325 | furniture | pages [9] -->


<!-- b000326 | furniture | pages [9] -->


<!-- b000327 | furniture | pages [9] -->


<!-- b000328 | furniture | pages [9] -->


<!-- b000329 | furniture | pages [9] -->


<!-- b000330 | furniture | pages [9] -->


<!-- b000331 | furniture | pages [9] -->


<!-- b000332 | prose | pages [9] -->
Cross-genre influence

<!-- b000333 | furniture | pages [9] -->


<!-- b000334 | furniture | pages [9] -->


<!-- b000335 | prose | pages [9] -->
T

<!-- b000336 | furniture | pages [9] -->


<!-- b000337 | furniture | pages [9] -->


<!-- b000338 | furniture | pages [9] -->


<!-- b000339 | furniture | pages [9] -->


<!-- b000340 | furniture | pages [9] -->


<!-- b000341 | furniture | pages [9] -->


<!-- b000342 | prose | pages [9] -->
Th

<!-- b000343 | furniture | pages [9] -->


<!-- b000344 | furniture | pages [9] -->


<!-- b000345 | prose | pages [9] -->
elin

<!-- b000346 | furniture | pages [9] -->


<!-- b000347 | prose | pages [9] -->
Se

<!-- b000348 | furniture | pages [9] -->


<!-- b000349 | prose | pages [9] -->
g

<!-- b000350 | furniture | pages [9] -->


<!-- b000351 | furniture | pages [9] -->


<!-- b000352 | furniture | pages [9] -->


<!-- b000353 | furniture | pages [9] -->


<!-- b000354 | furniture | pages [9] -->


<!-- b000355 | prose | pages [9] -->
nes

<!-- b000356 | furniture | pages [9] -->


<!-- b000357 | furniture | pages [9] -->


<!-- b000358 | prose | pages [9] -->
Intra-genre influence

<!-- b000359 | furniture | pages [9] -->


<!-- b000360 | furniture | pages [9] -->


<!-- b000361 | furniture | pages [9] -->


<!-- b000362 | furniture | pages [9] -->


<!-- b000363 | furniture | pages [9] -->


<!-- b000364 | prose | pages [9] -->
G

<!-- b000365 | furniture | pages [9] -->


<!-- b000366 | furniture | pages [9] -->


<!-- b000367 | furniture | pages [9] -->


<!-- b000368 | furniture | pages [9] -->


<!-- b000369 | prose | pages [9] -->
erk

<!-- b000370 | prose | pages [9] -->
W

<!-- b000371 | furniture | pages [9] -->


<!-- b000372 | furniture | pages [9] -->


<!-- b000373 | furniture | pages [9] -->


<!-- b000374 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000375 | furniture | pages [9] -->


<!-- b000376 | prose | pages [9] -->
g Stones

<!-- b000377 | prose | pages [9] -->
Jimi H

<!-- b000378 | furniture | pages [9] -->


<!-- b000379 | furniture | pages [9] -->


<!-- b000380 | furniture | pages [9] -->


<!-- b000381 | furniture | pages [9] -->


<!-- b000382 | furniture | pages [9] -->


<!-- b000383 | prose | pages [9] -->
h Boys

<!-- b000384 | prose | pages [9] -->
E

<!-- b000385 | furniture | pages [9] -->


<!-- b000386 | furniture | pages [9] -->


<!-- b000387 | furniture | pages [9] -->


<!-- b000388 | furniture | pages [9] -->


<!-- b000389 | prose | pages [9] -->
Predecessor influence junior

<!-- b000390 | furniture | pages [9] -->


<!-- b000391 | furniture | pages [9] -->


<!-- b000392 | prose | pages [9] -->
nton

<!-- b000393 | furniture | pages [9] -->


<!-- b000394 | prose | pages [9] -->
Gordon

<!-- b000395 | furniture | pages [9] -->


<!-- b000396 | furniture | pages [9] -->


<!-- b000397 | furniture | pages [9] -->


<!-- b000398 | furniture | pages [9] -->


<!-- b000399 | furniture | pages [9] -->


<!-- b000400 | prose | pages [9] -->
one

<!-- b000401 | furniture | pages [9] -->


<!-- b000402 | prose | pages [9] -->
Si

<!-- b000403 | furniture | pages [9] -->


<!-- b000404 | furniture | pages [9] -->


<!-- b000405 | furniture | pages [9] -->


<!-- b000406 | furniture | pages [9] -->


<!-- b000407 | furniture | pages [9] -->


<!-- b000408 | prose | pages [9] -->
Junior  influence Predecessor

<!-- b000409 | caption | pages [9] -->
Figure 4: Sub-network of Musical Inﬂuence

<!-- b000410 | prose | pages [9] -->
TASK 2 & 3: Multi-dimensional Music Similarity Evalua- 4

<!-- b000411 | heading | pages [9] -->
tion Model

<!-- b000412 | prose | pages [9] -->
4.1

<!-- b000413 | heading | pages [9] -->
Model Overview

<!-- b000414 | prose | pages [9] -->
To adequately measure the similarity between the music, we evaluate the similarity between the music using cosine similarity and Euclidean similarity, respectively. The global similarity Sglobal between the music is ﬁrst calculated. We further explore the partial similarity Spart between music. Finally, the trend of the year when the music was released is considered to inﬂuence Stime. The multidimensional similarity evaluation between music is constructed to obtain the similarity between music. An overview of the model is shown in the Figure(5).

<!-- b000415 | prose | pages [9] -->
Multi-dimensional Similarity Evaluation

<!-- b000416 | prose | pages [9] -->
S global

<!-- b000417 | prose | pages [9] -->
S time S part

<!-- b000418 | prose | pages [9] -->
Euclidean Metric Cosine similarity

<!-- b000419 | prose | pages [9] -->
Cosine similarity

<!-- b000420 | prose | pages [9] -->
Songs feature vector element

<!-- b000421 | prose | pages [9] -->
Cosine similarity+Euclidean Metric

<!-- b000422 | prose | pages [9] -->
Years feature vector element

<!-- b000423 | caption | pages [9] -->
Figure 5: Multi-dimensional Music Similarity Evaluation Model

<!-- b000424 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000425 | prose | pages [9] -->
关注数学模型

<!-- b000426 | furniture | pages [9] -->
2

<!-- b000427 | furniture | pages [9] -->
MATHmodels

<!-- b000428 | furniture | pages [9] -->
获取更多资讯

<!-- b000429 | furniture | pages [10] -->
Team # 2107091

<!-- b000430 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000431 | furniture | pages [10] -->
Page 10 of 25

<!-- b000432 | heading | pages [10] -->
Establishment of Multi-dimensional Music Similarity Evaluation Model

<!-- b000433 | prose | pages [10] -->
4.2

<!-- b000434 | prose | pages [10] -->
4.2.1 Global Similarity of Music

<!-- b000435 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000436 | prose | pages [10] -->
• Euclidean similarity

<!-- b000437 | prose | pages [10] -->
The Euclidean similarity measure is based on the absolute distance between the feature vectors and is used to reﬂect the absolute difference in the feature values between the two songs. Then the distance between the eigenvectors of music A and music B distanceAB is deﬁned as follows:

<!-- b000438 | prose | pages [10] -->
distanceAB =

<!-- b000439 | prose | pages [10] -->
√

<!-- b000440 | prose | pages [10] -->
n ∑

<!-- b000441 | prose | pages [10] -->
(Ai −Bi)2 (12)

<!-- b000442 | prose | pages [10] -->
i=1

<!-- b000443 | prose | pages [10] -->
Then the Euclidean similarity between music AB SE(A,B) is deﬁned by the following equa- tion:

<!-- b000444 | prose | pages [10] -->
SE(A,B) =

<!-- b000445 | prose | pages [10] -->
• Cosine similarity

<!-- b000446 | prose | pages [10] -->
1 (13) 1+distanceAB

<!-- b000447 | prose | pages [10] -->
Different from Euclidean similarity, cosine similarity uses the cosine of the angle between

<!-- b000448 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000449 | prose | pages [10] -->
two vectors in vector space to measure the similarity between two vectors. The cosine similarity focuses more on the difference between the two vectors in terms of direction rather than the difference between the values. The cosine similarity between the eigenvectors of music A and music B Scos(A,B) is deﬁned by the following equation(14)

<!-- b000450 | prose | pages [10] -->
A·B

<!-- b000451 | prose | pages [10] -->
Scos(A,B) = 1+ cosθ

<!-- b000452 | prose | pages [10] -->
n

<!-- b000453 | prose | pages [10] -->
Ai ·Bi

<!-- b000454 | prose | pages [10] -->
∑

<!-- b000455 | prose | pages [10] -->
2·||A||·||B|| = 1+ 1 = 1+ 2

<!-- b000456 | prose | pages [10] -->
i=1

<!-- b000457 | prose | pages [10] -->
√n

<!-- b000458 | prose | pages [10] -->
√n

<!-- b000459 | prose | pages [10] -->
2 ·

<!-- b000460 | prose | pages [10] -->
(14)

<!-- b000461 | prose | pages [10] -->
(A2

<!-- b000462 | prose | pages [10] -->
(B2

<!-- b000463 | prose | pages [10] -->
i )+

<!-- b000464 | prose | pages [10] -->
i )

<!-- b000465 | prose | pages [10] -->
∑

<!-- b000466 | prose | pages [10] -->
∑

<!-- b000467 | prose | pages [10] -->
i=1

<!-- b000468 | prose | pages [10] -->
i=1

<!-- b000469 | prose | pages [10] -->
The ﬁnal global similarity Sglobal between music A and B is deﬁned by the following equa- tion(15)

<!-- b000470 | prose | pages [10] -->
Sglobal(A,B) = SE(A,B)+Scos(A,B)

<!-- b000471 | prose | pages [10] -->
4.2.2 Partial Similarity of Music

<!-- b000472 | prose | pages [10] -->
(15)

<!-- b000473 | prose | pages [10] -->
The global similarity measure between music is deﬁned above, and the high-latitude feature vectors containing all the music features are considered. But this does not fully reﬂect the sim- ilarities between the music. The similarity measurement of music should be multi-dimensional and separate measurements should be made between different characteristic dimensions of mu- sic. In fact, in life, music can be considered similar if it is similar in some aspects such as rhythm, emotional tendencies, and instrumentation, but not in all characteristics. At the same time, songs from the same genre are not similar in all characteristics but may be similar only in certain aspects. To weigh the similarity between the whole dimension and the partial dimension of music, we explore the local similarity of music from the micro point of view, in terms of each feature.

<!-- b000474 | prose | pages [10] -->
We randomly select two, three, and four features from the key features of music to form different feature vectors V. There are a total of N new feature vectors composed of the extracted features.

<!-- b000475 | prose | pages [10] -->
12 +C4

<!-- b000476 | prose | pages [10] -->
N = C2

<!-- b000477 | prose | pages [10] -->
12 +C3 12 +C5 12 = 1573

<!-- b000478 | prose | pages [10] -->
The new feature vectors are V (1),V (2),··· ,V (1573), respectively. For music i and music j, we

<!-- b000479 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000480 | prose | pages [10] -->
关注数学模型

<!-- b000481 | prose | pages [10] -->
ﬁrst calculate the Sglobal of each combination of their features and select the highest 50 Sglobal

<!-- b000482 | furniture | pages [10] -->
2

<!-- b000483 | furniture | pages [10] -->
MATHmodels

<!-- b000484 | furniture | pages [10] -->
获取更多资讯

<!-- b000485 | furniture | pages [11] -->
Team # 2107091

<!-- b000486 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000487 | furniture | pages [11] -->
Page 11 of 25

<!-- b000488 | prose | pages [11] -->
to calculate the average value as the partial similarity (Spart(i, j)) between music i and music j. Spart(i, j) is deﬁned in the equation(16).

<!-- b000489 | prose | pages [11] -->
50 ∑

<!-- b000490 | prose | pages [11] -->
Sglobal(V(k)

<!-- b000491 | prose | pages [11] -->
,V(k)

<!-- b000492 | prose | pages [11] -->
j )

<!-- b000493 | prose | pages [11] -->
i

<!-- b000494 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000495 | prose | pages [11] -->
k=1

<!-- b000496 | prose | pages [11] -->
Spart(i, j) =

<!-- b000497 | prose | pages [11] -->
4.2.3 Fashion Trends Impact Factor

<!-- b000498 | prose | pages [11] -->
(16) 50

<!-- b000499 | prose | pages [11] -->
Considering that music is a literary and artistic product with strong social and cultural at- tributes, we should also consider the inﬂuence of the popular trend in the year of music release when analyzing the similarity of two pieces of music. Usually, the style of the song will evolve in the direction of the popular trend of the year. If there is a big difference in the popularity of the two songs in the year of their release, then the difference in melody and vocals between the two songs will change with the pop trends of the two songs in the year of their release.

<!-- b000500 | prose | pages [11] -->
Therefore, when measuring music similarity, the inﬂuence of pop trends on the music itself

<!-- b000501 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000502 | prose | pages [11] -->
should be reduced, so as to explore the intrinsic similarity of songs after stripping away the impact of pop trends. For the two songs released in year a and year b, we deﬁned the trend impact factor Stime as:

<!-- b000503 | prose | pages [11] -->
Stime = Sglobal(Yeara,Yearb) (17)

<!-- b000504 | prose | pages [11] -->
Where Yeara and Yearb are the music style attribute vectors of year a and b, respectively.

<!-- b000505 | prose | pages [11] -->
In summary, we establish a multidimensional music similarity (MS) evaluation model con- sidering the inﬂuence of popular trends, deﬁned as follows, β is a parameter deﬁned later (0<δ<1).

<!-- b000506 | prose | pages [11] -->
MS = ((1−δ)Sglobal +δSpart)·(1+ 0.1

<!-- b000507 | prose | pages [11] -->
4.3 Evaluation of Music Similarity

<!-- b000508 | prose | pages [11] -->
) (18)

<!-- b000509 | prose | pages [11] -->
Stime

<!-- b000510 | prose | pages [11] -->
We count the number of genres to which all inﬂuencers and followers belonged, and plot the following Figure(6) for each type of musician’s genre.

<!-- b000511 | prose | pages [11] -->
Influencer number of Main Genre

<!-- b000512 | prose | pages [11] -->
Folk

<!-- b000513 | prose | pages [11] -->
Blues

<!-- b000514 | prose | pages [11] -->
81 85

<!-- b000515 | prose | pages [11] -->
1,779

<!-- b000516 | prose | pages [11] -->
Reggae

<!-- b000517 | prose | pages [11] -->
111

<!-- b000518 | prose | pages [11] -->
Electronic

<!-- b000519 | prose | pages [11] -->
128

<!-- b000520 | prose | pages [11] -->
Vocal

<!-- b000521 | prose | pages [11] -->
135

<!-- b000522 | prose | pages [11] -->
Latin

<!-- b000523 | prose | pages [11] -->
164

<!-- b000524 | prose | pages [11] -->
Country

<!-- b000525 | prose | pages [11] -->
Jazz

<!-- b000526 | prose | pages [11] -->
273

<!-- b000527 | prose | pages [11] -->
R&B;

<!-- b000528 | prose | pages [11] -->
292 470

<!-- b000529 | prose | pages [11] -->
Pop/Rock

<!-- b000530 | prose | pages [11] -->
Follower  number of Main Genre

<!-- b000531 | prose | pages [11] -->
Folk

<!-- b000532 | prose | pages [11] -->
Blues

<!-- b000533 | prose | pages [11] -->
79 88

<!-- b000534 | prose | pages [11] -->
2,676

<!-- b000535 | prose | pages [11] -->
Reggae

<!-- b000536 | prose | pages [11] -->
114125

<!-- b000537 | prose | pages [11] -->
Vocal

<!-- b000538 | prose | pages [11] -->
147

<!-- b000539 | prose | pages [11] -->
Latin

<!-- b000540 | prose | pages [11] -->
182

<!-- b000541 | prose | pages [11] -->
Electroni

<!-- b000542 | prose | pages [11] -->
351

<!-- b000543 | prose | pages [11] -->
c Jazz

<!-- b000544 | prose | pages [11] -->
378

<!-- b000545 | prose | pages [11] -->
597

<!-- b000546 | caption | pages [11] -->
Figure 6: Statistics of Musicians by Genre

<!-- b000547 | prose | pages [11] -->
As can be seen from the Figure(6), Pop/Rock, R&B, and Jazz have the largest number of inﬂuencers, accounting for nearly 75% of all musicians. Therefore the subsequent analysis is based mainly on songs and musicians from these three genres.

<!-- b000548 | prose | pages [11] -->
• Similarity of Songs

<!-- b000549 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000550 | prose | pages [11] -->
关注数学模型

<!-- b000551 | furniture | pages [11] -->
2

<!-- b000552 | furniture | pages [11] -->
MATHmodels

<!-- b000553 | furniture | pages [11] -->
获取更多资讯

<!-- b000554 | furniture | pages [12] -->
Team # 2107091

<!-- b000555 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000556 | furniture | pages [12] -->
Page 12 of 25

<!-- b000557 | caption | pages [12] -->
Table 4: The Music Chosen from Pop/Rock, R&B, and Jazz

<!-- b000558 | prose | pages [12] -->
Pop/Rock Blind Faith So Alone Africa Long Cool Woman

<!-- b000559 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000560 | prose | pages [12] -->
R&B Don’t Stop ’Til You ··· Who’s Loving You Thinking of You Long Way Go Jazz **** ’N Boogie What’s New Floatin Summer Breeze

<!-- b000561 | prose | pages [12] -->
We select four songs from Pop/Rock, R&B, and Jazz as shown in the Table(4) and then analyzed their similarity.

<!-- b000562 | prose | pages [12] -->
The established Multi-dimensional Music Similarity Evaluation Model is used to calculate the overall similarity Sglobal between each song and the similarity MS after adding the partial similarity Spart. Set δ = 0.5, the calculation results of Sglobal and MS are shown in the Figure(7)

<!-- b000563 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000564 | prose | pages [12] -->
and (8).

<!-- b000565 | prose | pages [12] -->
Pop/Rock R&B Jazz

<!-- b000566 | prose | pages [12] -->
1.00 0.39 0.30 0.49 0.52 0.60 0.32 0.47 0.28 0.17 0.45 0.34

<!-- b000567 | prose | pages [12] -->
0.39 1.00 0.23 0.33 0.33 0.37 0.24 0.41 0.23 0.15 0.29 0.29

<!-- b000568 | prose | pages [12] -->
0.30 0.23 1.00 0.38 0.36 0.34 0.63 0.26 0.47 0.27 0.36 0.37

<!-- b000569 | prose | pages [12] -->
0.49 0.33 0.38 1.00 0.62 0.63 0.39 0.42 0.33 0.19 0.47 0.39

<!-- b000570 | prose | pages [12] -->
0.52 0.33 0.36 0.62 1.00 0.64 0.38 0.44 0.32 0.18 0.48 0.38

<!-- b000571 | prose | pages [12] -->
0.60 0.37 0.34 0.63 0.64 1.00 0.36 0.47 0.30 0.18 0.45 0.37

<!-- b000572 | prose | pages [12] -->
0.32 0.24 0.63 0.39 0.38 0.36 1.00 0.26 0.48 0.26 0.40 0.37

<!-- b000573 | prose | pages [12] -->
0.47 0.41 0.26 0.42 0.44 0.47 0.26 1.00 0.24 0.15 0.34 0.30

<!-- b000574 | prose | pages [12] -->
0.28 0.23 0.47 0.33 0.32 0.30 0.48 0.24 1.00 0.26 0.34 0.39

<!-- b000575 | prose | pages [12] -->
0.17 0.15 0.27 0.19 0.18 0.18 0.26 0.15 0.26 1.00 0.19 0.21

<!-- b000576 | prose | pages [12] -->
0.45 0.29 0.36 0.47 0.48 0.45 0.40 0.34 0.34 0.19 1.00 0.35

<!-- b000577 | prose | pages [12] -->
0.34 0.29 0.37 0.39 0.38 0.37 0.37 0.30 0.39 0.21 0.35 1.00

<!-- b000578 | caption | pages [12] -->
Figure 7: Global Similarity

<!-- b000579 | prose | pages [12] -->
Pop/Rock R&B Jazz

<!-- b000580 | prose | pages [12] -->
1 0.58 0.55 0.69 0.57 0.64 0.47 0.5 0.33 0.27 0.43 0.36

<!-- b000581 | prose | pages [12] -->
0.58 1 0.4 0.58 0.46 0.46 0.35 0.49 0.23 0.22 0.29 0.28

<!-- b000582 | prose | pages [12] -->
0.55 0.4 1 0.59 0.46 0.47 0.66 0.38 0.47 0.34 0.41 0.4

<!-- b000583 | prose | pages [12] -->
0.69 0.58 0.59 1 0.64 0.5 0.46 0.52 0.33 0.27 0.42 0.37

<!-- b000584 | prose | pages [12] -->
0.57 0.46 0.46 0.64 1 0.75 0.55 0.65 0.31 0.26 0.41 0.36

<!-- b000585 | prose | pages [12] -->
0.64 0.46 0.47 0.5 0.75 1 0.56 0.7 0.33 0.27 0.41 0.37

<!-- b000586 | prose | pages [12] -->
0.47 0.35 0.66 0.46 0.55 0.56 1 0.46 0.48 0.34 0.45 0.38

<!-- b000587 | prose | pages [12] -->
0.5 0.49 0.38 0.52 0.65 0.7 0.46 1 0.24 0.23 0.31 0.3

<!-- b000588 | prose | pages [12] -->
0.33 0.23 0.47 0.33 0.31 0.33 0.48 0.24 1 0.46 0.53 0.49

<!-- b000589 | prose | pages [12] -->
0.27 0.22 0.34 0.27 0.26 0.27 0.34 0.23 0.46 1 0.41 0.38

<!-- b000590 | prose | pages [12] -->
0.43 0.29 0.41 0.42 0.41 0.41 0.45 0.31 0.53 0.41 1 0.48

<!-- b000591 | prose | pages [12] -->
0.36 0.28 0.4 0.37 0.36 0.37 0.38 0.3 0.49 0.38 0.48 1

<!-- b000592 | caption | pages [12] -->
Figure 8: Multi–Similarity

<!-- b000593 | prose | pages [12] -->
Figure(7) shows the similarity between songs in each genre without the addition of Spart, and Figure(8) shows the similarity between songs in each genre with the addition of Spart. As can be seen from the ﬁgure that songs within the same genre have higher similarity scores between them. Comparing Figure(7) and Figure(8) with the part circled by the box (i.e., the similarity scores between songs and songs within the same genre), it can be found that: the similarity scores between songs of the same genre have increased after the introduction of the parital similarity of songs (Spart), while the similarity between songs of different genres has decreased. The addition of local similarity makes the measurement of musical similarity more accurate and reasonable.

<!-- b000594 | prose | pages [12] -->
Thus we can consider the discussion about local similarity in 4.2.2 to be accurate: that is, songs in the same genre may have high similarity in the characteristics of several di- mensions. Songs within the same genre can be distinguished from songs in other genres by a combination of several features.

<!-- b000595 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000596 | prose | pages [12] -->
关注数学模型

<!-- b000597 | furniture | pages [12] -->
2

<!-- b000598 | furniture | pages [12] -->
MATHmodels

<!-- b000599 | furniture | pages [12] -->
获取更多资讯

<!-- b000600 | furniture | pages [13] -->
Team # 2107091

<!-- b000601 | prose | pages [13] -->
• Similarity of Musicians

<!-- b000602 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000603 | furniture | pages [13] -->
Page 13 of 25

<!-- b000604 | prose | pages [13] -->
We used the established Multi-dimensional Music Similarity Evaluation Model to calculate the similarity of Pop/Rock, R&B, and Jazz musicians within and between genres. The speciﬁc values are shown in the Table(5).

<!-- b000605 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000606 | caption | pages [13] -->
Table 5: Similarity of Musicians from Pop/Rock, R&B, and Jazz

<!-- b000607 | prose | pages [13] -->
Within genres Between genres Pop and R&B Genres Pop/ROCK R&B Jazz Average 0.659 0.683 0.627 Min 0.399 0.439 0.382 Max 0.917 0.906 0.916 Pop and Jazz R&B and Jazz 0.647 0.560 0.592 0.309 0.374 0.359 0.949 0.869 0.898

<!-- b000608 | prose | pages [13] -->
Observing the Table(5), we can learn that the intra-genre artists of each genre are more similar than the similarity with the artists of other genres. Therefore we can assume that the artists within each genre are more similar than the artists between genres. At the same time, we can also see that the average similarity between POP and R&B artists reached 0.647, which is

<!-- b000609 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000610 | prose | pages [13] -->
very close to the average similarity within Pop. From this, it can be concluded that there may be more similarities between genres. To visualize the relationship between genres, we used PCA to downscale the characteristics of Pop/Rock, R&B, Jazz and plot the distribution of their musicians in three dimensions, as shown in the Figure(9).

<!-- b000611 | prose | pages [13] -->
Pop

<!-- b000612 | prose | pages [13] -->
Pop/Roc

<!-- b000613 | prose | pages [13] -->
R&B

<!-- b000614 | prose | pages [13] -->
kR&B

<!-- b000615 | prose | pages [13] -->
Jazz

<!-- b000616 | prose | pages [13] -->
Jazz

<!-- b000617 | caption | pages [13] -->
Figure 9: Statistics of Musicians by Genre

<!-- b000618 | prose | pages [13] -->
As can be seen from the Figure(9), the artists in the genres are more similar, but there is no clear line of distinction between genres. This coincides with the conclusion of our analysis of the Table(5).

<!-- b000619 | prose | pages [13] -->
Analysis of the Musical Discrimination and Inﬂuences of Genres 4.4

<!-- b000620 | heading | pages [13] -->
Discrimination Evaluation Model of Feature Combination

<!-- b000621 | prose | pages [13] -->
4.4.1

<!-- b000622 | prose | pages [13] -->
Combining with the discussion of partial similarity in music in 4.2.2 and 4.3: songs between similar genres may do not share a high degree of similarity in all features, while the combination of several particular features may give music in the same genre a very high degree of similarity and thus distinguish it from music in other genres. Similarly, there may be a high similarity between different genres in the combination of certain characteristics.

<!-- b000623 | prose | pages [13] -->
To analyze what combination of features distinguishes a genre, we arrange and combine the

<!-- b000624 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000625 | heading | pages [13] -->
12 musical features except popularity in two-two, three-three, four-four, and ﬁve-ﬁve combina-关注数学模型

<!-- b000626 | furniture | pages [13] -->
2

<!-- b000627 | furniture | pages [13] -->
MATHmodels

<!-- b000628 | furniture | pages [13] -->
获取更多资讯

<!-- b000629 | furniture | pages [14] -->
Team # 2107091

<!-- b000630 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000631 | furniture | pages [14] -->
Page 14 of 25

<!-- b000632 | prose | pages [14] -->
tions to obtain a total of N′ types of new feature combinations: V (1),V (2),··· ,V (1573)

<!-- b000633 | prose | pages [14] -->
N′ = C2

<!-- b000634 | prose | pages [14] -->
12 +C4 12 +C3 12 +C5 12 = 1573 (19)

<!-- b000635 | prose | pages [14] -->
Based on the new combination V, the partial similarity Spart deﬁned by the equation(16) in 4.2.2 between the genres and the other genres is calculated. The minimum value of Spart is

<!-- b000636 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000637 | prose | pages [14] -->
1 2, which represents the minimum local similarity. For the ith new feature combination V (i), a metric vector Spart I = [Spart 1,Spart 2,··· ,Spart 18]T is obtained by the partial similarity between the genre to be evaluated and other genres, as shown in the Figure(10).

<!-- b000638 | prose | pages [14] -->
Pop/Rock

<!-- b000639 | prose | pages [14] -->
Blue

<!-- b000640 | prose | pages [14] -->
Jazz

<!-- b000641 | prose | pages [14] -->
. . .

<!-- b000642 | prose | pages [14] -->
. . .

<!-- b000643 | prose | pages [14] -->
Folk

<!-- b000644 | prose | pages [14] -->
. . .

<!-- b000645 | prose | pages [14] -->
. . .

<!-- b000646 | prose | pages [14] -->
. . .

<!-- b000647 | prose | pages [14] -->
Country

<!-- b000648 | prose | pages [14] -->
Vocal

<!-- b000649 | prose | pages [14] -->
. . .

<!-- b000650 | prose | pages [14] -->
. . .

<!-- b000651 | prose | pages [14] -->
. . .

<!-- b000652 | prose | pages [14] -->
. . .

<!-- b000653 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000654 | prose | pages [14] -->
Valence & tempo

<!-- b000655 | prose | pages [14] -->
Muti-Similarity between Pop and Vocal by [mode,key]

<!-- b000656 | prose | pages [14] -->
Mode & energy & key

<!-- b000657 | prose | pages [14] -->
mode & key

<!-- b000658 | caption | pages [14] -->
Figure 10: Partial Similarity Evaluation Vector

<!-- b000659 | prose | pages [14] -->
Spart i reﬂects the similarity of the genre between other genres when only the features con- tained within V (i) are considered. If the features contained within V (i) can well distinguish the genre from other genres, then these features can be considered as the signiﬁcant differences between the music of the genre and other genres. Ideally, if the combination of features cho- sen can completely distinguish the genre from other genres, then the optimal partial similarity

<!-- b000660 | prose | pages [14] -->
2]T is deﬁned. 2, 1 2,··· , 1

<!-- b000661 | prose | pages [14] -->
part = [1

<!-- b000662 | prose | pages [14] -->
vector S′

<!-- b000663 | prose | pages [14] -->
Cosine similarity and Euclidean similarity are used to measure the discriminationi of feature combination vector V (i)

<!-- b000664 | prose | pages [14] -->
part,Spart i)+SE(S′

<!-- b000665 | prose | pages [14] -->
discriminationi = Scos(S′

<!-- b000666 | prose | pages [14] -->
part,Spart i) (20)

<!-- b000667 | prose | pages [14] -->
We selected two genres, Electronic and Latin, for analysis, and obtained the top three dis- crimination scores as shown in the Table(6).

<!-- b000668 | caption | pages [14] -->
Table 6: Feature Combination Discrimination

<!-- b000669 | prose | pages [14] -->
Feature combination Discrimination [acousticness, instrumentalness, speechiness]* 1.1588 [energy, acousticness, instrumentalness, speechiness]*

<!-- b000670 | prose | pages [14] -->
Electronic

<!-- b000671 | prose | pages [14] -->
1.1588 [energy, acousticness, instrumentalness, liveness, speechiness] 1.1586

<!-- b000672 | prose | pages [14] -->
Feature combination Discrimination [energy, valence, tempo, danceability]* 1.1474 [energy, valence, loudness, danceability]

<!-- b000673 | prose | pages [14] -->
Latin

<!-- b000674 | prose | pages [14] -->
1.1473 [energy, valence, tempo, danceability, liveness]

<!-- b000675 | prose | pages [14] -->
As can be seen from the Table(6):

<!-- b000676 | prose | pages [14] -->
1.1470

<!-- b000677 | prose | pages [14] -->
• For Electronic: Electronic is different from other genres in four aspects, including acous- ticness, instrumentalness, speechiness, and energy. These characteristics are in line with those of electronic-synth music, which has a strong sense of rhythm and is more likely to evoke the desire to dance.

<!-- b000678 | prose | pages [14] -->
• For Latin: Its concentrated characteristics are embodied in energy, valence, tempo,

<!-- b000679 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000680 | prose | pages [14] -->
关注数学模型

<!-- b000681 | prose | pages [14] -->
danceability, which coincide with the energetic, dynamic, rhythm-centered characteristics of Latin music.

<!-- b000682 | furniture | pages [14] -->
2

<!-- b000683 | furniture | pages [14] -->
MATHmodels

<!-- b000684 | furniture | pages [14] -->
获取更多资讯

<!-- b000685 | furniture | pages [15] -->
Team # 2107091

<!-- b000686 | prose | pages [15] -->
4.4.2 Analysis of Genre Changes Over Time

<!-- b000687 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000688 | furniture | pages [15] -->
Page 15 of 25

<!-- b000689 | prose | pages [15] -->
• Analysis of single genre changes over time

<!-- b000690 | prose | pages [15] -->
Take Electronic’s music characteristics change as an example. The analysis process is shown

<!-- b000691 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000692 | prose | pages [15] -->
below:

<!-- b000693 | prose | pages [15] -->
Step 1: Data visualization

<!-- b000694 | prose | pages [15] -->
We use the four most distinguishing attributes of Electronic: acousticness, instrumentalness, speechiness, and energy, which are analyzed in 4.4.1. We add the number of musicians within the genre and the popularity to obtain six variables. The curves of these six variables over time are plotted as Figure(11).

<!-- b000695 | prose | pages [15] -->
1.2 1 0.8 0.6

<!-- b000696 | prose | pages [15] -->
value

<!-- b000697 | prose | pages [15] -->
0.4 0.2

<!-- b000698 | prose | pages [15] -->
energy

<!-- b000699 | prose | pages [15] -->
acousticness

<!-- b000700 | prose | pages [15] -->
instrumentalness

<!-- b000701 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000702 | prose | pages [15] -->
0

<!-- b000703 | prose | pages [15] -->
1930 1940 1950 1960 1970 1980

<!-- b000704 | prose | pages [15] -->
Year

<!-- b000705 | prose | pages [15] -->
250

<!-- b000706 | prose | pages [15] -->
200

<!-- b000707 | prose | pages [15] -->
150

<!-- b000708 | prose | pages [15] -->
value

<!-- b000709 | prose | pages [15] -->
100

<!-- b000710 | prose | pages [15] -->
50

<!-- b000711 | prose | pages [15] -->
0

<!-- b000712 | prose | pages [15] -->
1930 1940 1950 1960 1970 1980

<!-- b000713 | prose | pages [15] -->
Year

<!-- b000714 | prose | pages [15] -->
speechiness

<!-- b000715 | prose | pages [15] -->
1990 2000 2010 2020

<!-- b000716 | prose | pages [15] -->
artist number

<!-- b000717 | prose | pages [15] -->
popularity

<!-- b000718 | prose | pages [15] -->
1990 2000 2010 2020

<!-- b000719 | caption | pages [15] -->
Figure 11: Changes of Electronic Over Time

<!-- b000720 | prose | pages [15] -->
Step 2: Identiﬁcation of mutation points

<!-- b000721 | prose | pages [15] -->
From the Figure(11), we can see that electronic music mutated in the 1950s and character- istics changed from 1970 to 1980. In total, it can be divided into three development stages: in the 1950s, 1970∼1980, and after the 1980s.

<!-- b000722 | prose | pages [15] -->
Step 3: Analysis with historical facts

<!-- b000723 | prose | pages [15] -->
1. In the 1950s, there were signiﬁcant changes in the variety of attributes of electronic music, from 0.93 to 0.10, and the score for acousticness, instrumentalness, iTunes, and energy increased by more than 200%. After the 1950s, electronic music became more intense and electrically enhanced. According to Wikipedia[6], the ﬁrst electronic music recorded on tape was composed by Louis and Bebe Barron in 1950, signifying the creation of true electronic music.

<!-- b000724 | prose | pages [15] -->
2. From the 1970s to the 1980s, there were a lot of innovations in electronic music equip- ment. Digital synthesizers and samplers replaced analog synthesizers, and more musicians could use a synthesizer for music creation.

<!-- b000725 | prose | pages [15] -->
3. After the 1980s, the Acid House movement in the UK pushed the development of elec- tronic music into the mainstream, and between the late 1990s and the beginning of the 21st cen- tury, electronic music using only electronic instruments became increasingly popular, a trend that continues today. Nightclubs around the world are playing electronic music on a regular basis.

<!-- b000726 | prose | pages [15] -->
• Analysis of correlation of changes between genres over time

<!-- b000727 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000728 | prose | pages [15] -->
We use Easy listening and New age as examples to analyze the interplay of genres during关注数学模型

<!-- b000729 | furniture | pages [15] -->
2

<!-- b000730 | furniture | pages [15] -->
MATHmodels

<!-- b000731 | furniture | pages [15] -->
获取更多资讯

<!-- b000732 | furniture | pages [16] -->
Team # 2107091

<!-- b000733 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000734 | furniture | pages [16] -->
Page 16 of 25

<!-- b000735 | prose | pages [16] -->
their change over time. We choose three characteristics of acousticness, tampo, and speechiness of these two genres to analyze how they change over time.

<!-- b000736 | prose | pages [16] -->
eacy listening new age

<!-- b000737 | prose | pages [16] -->
eacy listening

<!-- b000738 | prose | pages [16] -->
eacy listening new age

<!-- b000739 | prose | pages [16] -->
0.6

<!-- b000740 | prose | pages [16] -->
1.2

<!-- b000741 | prose | pages [16] -->
new age

<!-- b000742 | prose | pages [16] -->
0.08

<!-- b000743 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000744 | prose | pages [16] -->
0.5

<!-- b000745 | prose | pages [16] -->
1 0.8

<!-- b000746 | prose | pages [16] -->
0.4

<!-- b000747 | prose | pages [16] -->
0.6

<!-- b000748 | prose | pages [16] -->
0.3

<!-- b000749 | prose | pages [16] -->
0.4

<!-- b000750 | prose | pages [16] -->
0.2

<!-- b000751 | prose | pages [16] -->
0.2

<!-- b000752 | prose | pages [16] -->
0.1

<!-- b000753 | prose | pages [16] -->
0

<!-- b000754 | prose | pages [16] -->
0

<!-- b000755 | prose | pages [16] -->
1921

<!-- b000756 | prose | pages [16] -->
1940

<!-- b000757 | prose | pages [16] -->
1959

<!-- b000758 | prose | pages [16] -->
1978

<!-- b000759 | prose | pages [16] -->
1997

<!-- b000760 | prose | pages [16] -->
2016

<!-- b000761 | prose | pages [16] -->
1921

<!-- b000762 | prose | pages [16] -->
1940

<!-- b000763 | prose | pages [16] -->
1959

<!-- b000764 | prose | pages [16] -->
acousticness

<!-- b000765 | prose | pages [16] -->
0.07 0.06 0.05 0.04 0.03 0.02 0.01 0

<!-- b000766 | prose | pages [16] -->
1921

<!-- b000767 | prose | pages [16] -->
1940

<!-- b000768 | prose | pages [16] -->
1959

<!-- b000769 | prose | pages [16] -->
1978

<!-- b000770 | prose | pages [16] -->
1997

<!-- b000771 | prose | pages [16] -->
2016

<!-- b000772 | prose | pages [16] -->
1978

<!-- b000773 | prose | pages [16] -->
1997

<!-- b000774 | prose | pages [16] -->
2016

<!-- b000775 | prose | pages [16] -->
speechiness

<!-- b000776 | prose | pages [16] -->
tampo

<!-- b000777 | caption | pages [16] -->
Figure 12: Changes of New age and Easy listening Over Time

<!-- b000778 | prose | pages [16] -->
As can be seen from the Figure(12), both Easy listening and New age have a similar trend: acousticness gradually decreases, tempo stabilizes, and speechiness continues to decrease on top of the already low values. This is also in line with the development history of the real Easy listening and New age, that is, the rhythm is soothing, there is less spoken word, and gradually

<!-- b000779 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000780 | prose | pages [16] -->
introduced a small number of electronic instruments.

<!-- b000781 | prose | pages [16] -->
Exploring the sequential correlation between the changes of the two curves, we can also learn that the changes of New age always lag behind Easy listening and change in the direction of Easy listening changes. It can be further concluded that New age is inﬂuenced by Easy listening as it changes over time, which coincides with the fact that New age started later and is inﬂuenced by Easy listening.

<!-- b000782 | heading | pages [16] -->
Task 4 :Long-Short Term Inﬂuence Evaluation Model Based

<!-- b000783 | prose | pages [16] -->
5 on Sliding Window

<!-- b000784 | heading | pages [16] -->
Establishment of Sliding Window Model

<!-- b000785 | prose | pages [16] -->
5.1 To explore whether inﬂuencers inﬂuence the music created by followers, we evaluated the similarity between the music of inﬂuencers and followers by MS. Considering that the inﬂu- ence of followers by inﬂuencers changes continuously over time, we add sliding windows[9] to explore the short-term similarity MS of music based on the similarity evaluation model es- tablished in TASK 2 & 3, to capture the short-term inﬂuence STS of inﬂuencers on followers’ music. Finally, the magnitude of the change in short-term similarity is summed to obtain the long-term inﬂuence LTS of the inﬂuencer on the follower. An overview of the model is shown in the Figure(13).

<!-- b000786 | prose | pages [16] -->
We arrange the songs of inﬂuencers and followers by time, and as the window slides along the time line, new songs are added continuously on the right side, while some outdated songs are dropped on the left. We swipe two windows on the timelines of the works of inﬂuencers and followers at different times. Additionally, we ensure that the music in the inﬂuencer window is released earlier than the music in the follower window. Then calculate the similarity of inﬂuencer’s music and follower’s music MS in both windows.

<!-- b000787 | prose | pages [16] -->
In order to ﬁnd the most similar songs (songs with real inﬂuence relationships), we deﬁne the similarity of the song in the i th follower window to the inﬂuencer (MSi):

<!-- b000788 | prose | pages [16] -->
MSi = max{MS(Fli,In j), j = 1 to n} (21) Fli and In j are the music within the follower window i and the inﬂuencer window j, respec- tively. MS(Fli,In j) represents the short-term similarity of music within the inﬂuencer window

<!-- b000789 | prose | pages [16] -->
j to music within the follower window i. To satisfy that the music within the inﬂuencer window

<!-- b000790 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000791 | prose | pages [16] -->
关注数学模型 is released earlier than the followers, n changes as i changes.

<!-- b000792 | furniture | pages [16] -->
2

<!-- b000793 | furniture | pages [16] -->
MATHmodels

<!-- b000794 | furniture | pages [16] -->
获取更多资讯

<!-- b000795 | furniture | pages [17] -->
Team # 2107091

<!-- b000796 | prose | pages [17] -->
…

<!-- b000797 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000798 | furniture | pages [17] -->
Page 17 of 25

<!-- b000799 | prose | pages [17] -->
…

<!-- b000800 | prose | pages [17] -->
Follower

<!-- b000801 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000802 | prose | pages [17] -->
Muti-Similarity

<!-- b000803 | prose | pages [17] -->
Time Line

<!-- b000804 | prose | pages [17] -->
Maximum

<!-- b000805 | prose | pages [17] -->
Influencer

<!-- b000806 | prose | pages [17] -->
…

<!-- b000807 | prose | pages [17] -->
…

<!-- b000808 | prose | pages [17] -->
Time Line

<!-- b000809 | caption | pages [17] -->
Figure 13: Long-Short Term Inﬂuence Evaluation Model Based on Sliding Window

<!-- b000810 | prose | pages [17] -->
Deﬁne the magnitude of similarity change (∆MS)i for the follower’s timeline window:

<!-- b000811 | prose | pages [17] -->
(∆MS)i = MSi −MSi−1

<!-- b000812 | prose | pages [17] -->
(22)

<!-- b000813 | prose | pages [17] -->
MSi−1

<!-- b000814 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000815 | prose | pages [17] -->
Deﬁne short-term similarity (STS) and long-term similarity (LTS):

<!-- b000816 | prose | pages [17] -->
{

<!-- b000817 | prose | pages [17] -->
STS = max{(∆MS)i}

<!-- b000818 | prose | pages [17] -->
(23)

<!-- b000819 | prose | pages [17] -->
LTS = ∑(∆MS)i

<!-- b000820 | prose | pages [17] -->
We consider that when STS > 0.01, i.e., in the short term, there is a period of time when followers’ song styles are substantially closer to those of the inﬂuencers, and this is when the inﬂuencers can be considered to have inﬂuenced the followers. When LTS > 0, the follower’s music style is generally close to the inﬂuencer’s in the long run, and the inﬂuencer can be considered to have a long-term inﬂuence on the follower. Deﬁning the degree of inﬂuence long-term-short-term score IDS, when IDS > 0, the inﬂuencer can be considered to have an inﬂuence on the follower.

<!-- b000821 | prose | pages [17] -->
IDS = max(0,LTS)+max(0,STS−0.01)

<!-- b000822 | prose | pages [17] -->
5.2

<!-- b000823 | heading | pages [17] -->
Test of the Established Model

<!-- b000824 | prose | pages [17] -->
(24)

<!-- b000825 | prose | pages [17] -->
We set the window size to 5 and the move step to 3 for window sliding detection. The IDS between all inﬂuencers and followers are calculated using the model developed above and ﬁnd that 86.08% of the IDS are greater than 0. It can be concluded that in general inﬂuencers do inﬂuence the music created by their followers.

<!-- b000826 | prose | pages [17] -->
We choose the inﬂuencer: Black Box, and his followers: Soda Stereo and Dave Matthews Band as an example, the results are shown in the Table(7).

<!-- b000827 | caption | pages [17] -->
Table 7: Result of Sliding Window Model

<!-- b000828 | prose | pages [17] -->
Inﬂuencer Follower Black Box Soda Stereo Black Box Dave Matthews Band LTS STS IDS 0.00033 0.01251 0.000334 0.00553 0.00549 0.00553

<!-- b000829 | prose | pages [17] -->
It can be seen that Black Box did inﬂuence the music making of its followers, Soda Stereo and Dave Matthews Band, to varying degrees.

<!-- b000830 | prose | pages [17] -->
• For Soda Stereo: STS≫LTS, the short-term impact is greater.Inspired by a few songs from an inﬂuencer and subsequently less inﬂuenced by the inﬂuencer.

<!-- b000831 | prose | pages [17] -->
• For Dave Matthews Band: LTS>STS, the long-term impact is greater. Dave Matthews

<!-- b000832 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000833 | prose | pages [17] -->
关注数学模型 Band has been inﬂuenced by inﬂuencers for a long time and is a loyal follower.

<!-- b000834 | furniture | pages [17] -->
2

<!-- b000835 | furniture | pages [17] -->
MATHmodels

<!-- b000836 | furniture | pages [17] -->
获取更多资讯

<!-- b000837 | furniture | pages [18] -->
Team # 2107091

<!-- b000838 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000839 | furniture | pages [18] -->
Page 18 of 25

<!-- b000840 | prose | pages [18] -->
Contagious Evaluation of Musical Characteristics 5.3

<!-- b000841 | prose | pages [18] -->
Music has many different characteristics, and in order to explore whether there are more contagious (easy to spread) ones among different characteristics, we established a contagious

<!-- b000842 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000843 | prose | pages [18] -->
evaluation system for music characteristics based on the timeline of inﬂuencers’ and followers’ works in the previous section, and the music similarity (MS) evaluation model in 4.2.1. For a speciﬁc musician (as a follower), the contagious evaluation steps of musical features v(k) are as follows.

<!-- b000844 | prose | pages [18] -->
Step 1: Build the timelines of the works of this musician (single) and his inﬂuencer (possibly multiple) respectively, as shown in Figure(13) (4.4.2).

<!-- b000845 | prose | pages [18] -->
Step 2: For a musician’s song i, it is combined with an inﬂuencer’s song j, and then calculate the difference dif(i, j)(k) of the musical characteristics v(k) of the two songs.

<!-- b000846 | prose | pages [18] -->
dif(i, j)(k) = v(k)

<!-- b000847 | prose | pages [18] -->
−v(k)

<!-- b000848 | prose | pages [18] -->
(25)

<!-- b000849 | prose | pages [18] -->
i

<!-- b000850 | prose | pages [18] -->
j

<!-- b000851 | prose | pages [18] -->
Step 3: Musicians’ works may be inﬂuenced by only a relatively small number of enlighten- ing works, so there should be the smallest feature difference between them on v(k). We choose

<!-- b000852 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000853 | prose | pages [18] -->
the three smallest values of dif(i, j)(k) for weighted summation to obtain the difference DIF(k)

<!-- b000854 | prose | pages [18] -->
i between the follower’s song i on feature v(k) and and its corresponding enlightening work. dif (k)

<!-- b000855 | prose | pages [18] -->
1 , di f (k) 2 , di f (k) for the ﬁrst three smallest characteristic differences. 3

<!-- b000856 | prose | pages [18] -->
= 1

<!-- b000857 | prose | pages [18] -->
DIF(k)

<!-- b000858 | prose | pages [18] -->
2dif (k)

<!-- b000859 | prose | pages [18] -->
i

<!-- b000860 | prose | pages [18] -->
1 + 1

<!-- b000861 | prose | pages [18] -->
+ 1 3dif (k)

<!-- b000862 | prose | pages [18] -->
6dif (k) (26)

<!-- b000863 | prose | pages [18] -->
2

<!-- b000864 | prose | pages [18] -->
3

<!-- b000865 | prose | pages [18] -->
Step 4: Analyze the contagion of all the features within this musician’s works. Deﬁne the degree of closeness DC(k) of all songs of a follower to the songs of its inﬂuencer on v(k). And D[d](k) is the variance of all songs of this musician on the feature v(k). The smaller the ﬁnal value of DC(k) is, the more susceptible the musician is to inﬂuencers on v(k), and the more contagious the v(k) is.

<!-- b000866 | prose | pages [18] -->
DC(k) = ((1+average(DIF(k)

<!-- b000867 | prose | pages [18] -->
))·(1+minimum(DIF(k) i

<!-- b000868 | prose | pages [18] -->
))·D[d](k) (27) i

<!-- b000869 | prose | pages [18] -->
Using the above analysis process, Soda Stereo and Dave Matthews are selected as followers for the contagious analysis of music characteristics, and the results are obtained as shown in the following Table(8).

<!-- b000870 | caption | pages [18] -->
Table 8: Contagious of Musical Characteristics

<!-- b000871 | prose | pages [18] -->
speechiness Characteristics

<!-- b000872 | prose | pages [18] -->
Soda Stereo

<!-- b000873 | prose | pages [18] -->
DC energy instrumentalness 0.000249 0.0068 0.007554

<!-- b000874 | prose | pages [18] -->
speechiness Characteristic instrumentalness danceability 8.5279×10−5

<!-- b000875 | prose | pages [18] -->
Dave Matthews

<!-- b000876 | prose | pages [18] -->
DC 9.6721×10−5 0.012702

<!-- b000877 | prose | pages [18] -->
As can be seen from the Table(8), not all characteristics are highly contagious to a particular musician, and the most contagious characteristics vary from one musician to another. For Soda Stereo, the musical characteristic speechiness is the most contagious. For Dave Matthews, the musical characteristics of speechiness and instrumentalness are the most contagious.

<!-- b000878 | prose | pages [18] -->
Task 5 & 6 & 7: Analysis of Music Revolution Over Time 6

<!-- b000879 | prose | pages [18] -->
The Identiﬁcation of the Musical revolution 6.1

<!-- b000880 | prose | pages [18] -->
We analyze the given data to identify musical revolutions in terms of two symbol: changes

<!-- b000881 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000882 | prose | pages [18] -->
关注数学模型 in existing musical genres, the creation of new musical genres.

<!-- b000883 | furniture | pages [18] -->
2

<!-- b000884 | furniture | pages [18] -->
MATHmodels

<!-- b000885 | furniture | pages [18] -->
获取更多资讯

<!-- b000886 | furniture | pages [19] -->
Team # 2107091

<!-- b000887 | prose | pages [19] -->
• Changes in existing musical genres

<!-- b000888 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000889 | furniture | pages [19] -->
Page 19 of 25

<!-- b000890 | prose | pages [19] -->
Dramatic changes in musical characteristics within existing musical genres can be recog- nized as temporal musical revolution. The following are the conditions for determining the point in time when an evolution occurs:

<!-- b000891 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000892 | prose | pages [19] -->
A. The musical characteristics of the genre remained stable before and after the revolution.

<!-- b000893 | prose | pages [19] -->
B. In the year of the revolution, the musical characteristics of the genre change greatly.

<!-- b000894 | prose | pages [19] -->
C. There are at least two features that have taken a signiﬁcant turn at the same time.

<!-- b000895 | prose | pages [19] -->
The above conditions are quantiﬁed using mathematical formulas to explore whether a sig- niﬁcant change occurs within a six-year period of analysis. For the characteristic v(k) of the genre, the condition for determining that an evolution occurs in the 3th ∼4th year of the analy- sis cycle is deﬁned by the equation(28)

<!-- b000896 | prose | pages [19] -->


<!-- b000897 | prose | pages [19] -->
3 −v(k)

<!-- b000898 | prose | pages [19] -->
|v(k)

<!-- b000899 | prose | pages [19] -->


<!-- b000900 | prose | pages [19] -->
2 | < 0.03

<!-- b000901 | prose | pages [19] -->
   

<!-- b000902 | prose | pages [19] -->
|v(k)

<!-- b000903 | prose | pages [19] -->
2 −v(k)

<!-- b000904 | prose | pages [19] -->
 

<!-- b000905 | prose | pages [19] -->
1 | < 0.03

<!-- b000906 | prose | pages [19] -->


<!-- b000907 | prose | pages [19] -->
|v(k)

<!-- b000908 | prose | pages [19] -->
4 −v(k)

<!-- b000909 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000910 | prose | pages [19] -->
3 | > 0.1

<!-- b000911 | prose | pages [19] -->
  

<!-- b000912 | prose | pages [19] -->
(28)

<!-- b000913 | prose | pages [19] -->
3 )| < 0.02 or |v(k)

<!-- b000914 | prose | pages [19] -->
|(v(k)

<!-- b000915 | prose | pages [19] -->
5 −v(k) 4 )−(v(k) 4 −v(k)

<!-- b000916 | prose | pages [19] -->
    

<!-- b000917 | prose | pages [19] -->
5 −v(k) 4 | < 0.03

<!-- b000918 | prose | pages [19] -->
4 )| < 0.02 or |v(k)

<!-- b000919 | prose | pages [19] -->
|(v(k)

<!-- b000920 | prose | pages [19] -->
6 −v(k) 5 )−(v(k) 5 −v(k) 6 −v(k) 5 | < 0.03

<!-- b000921 | prose | pages [19] -->
Using a six-year time span as the width of the sliding window, a sliding window model is used for analysis to identify the years in which the upper constraint is satisﬁed, i.e., the time when a revolution occurs. If the trend of change continues in the years following a turning point, we consider a long-term change to have occurred during that period. Electronic is selected as the study object to explore the characteristics of signiﬁcant revolution in Electronic. With the above constraint equation, we capture the year 1950 and 1969 as the time points of the revolution. And the characteristics of Electronic in 1950 and 1969 are shown in the Table(9).

<!-- b000922 | caption | pages [19] -->
Table 9: Identiﬁcation of Revolution of Electronic

<!-- b000923 | prose | pages [19] -->
Year 1950 speechiness acousticness Characteristic Change 0.796 0.513 1969 energy instrumentalness acousticness 0.210 0.131 0.123

<!-- b000924 | prose | pages [19] -->
From the Table(9), it can be seen that Electronic in 1950 speechiness, energy and acous- ticness changed a lot. In 1969 instrumentalness and acousticness changed a lot. This is also similar to the conclusion of our analysis of Electronic in 4.4.2, and it can be considered that the established constraint equations can identify the revolution in the existing music genres.

<!-- b000925 | prose | pages [19] -->
• Creation of new musical genres

<!-- b000926 | prose | pages [19] -->
To identify the new generation of music genres, we visualize the number of musicians in each genre over time in Figure(14). Each surge in the number of musicians in each genre can be considered as an evolution in the genre. The ﬁrst surge in the number of musicians in each genre can be identiﬁed as the creation of a new genre.

<!-- b000927 | prose | pages [19] -->
Observe the Figure(14), using the analysis of R&B and Country as an example:

<!-- b000928 | prose | pages [19] -->
1. The ﬁrst explosion in the number of musicians in R&B occurred in 1950. There had not been an explosion in the number of musicians in the genre before that, so it can be argued that an evolution happened in 1950, when R&B was created. This also coincides with the start date of the R&B genre, according to Sound and Music from Xinhua News Agency[7].

<!-- b000929 | prose | pages [19] -->
2. The ﬁrst surge in the number of musicians in Country occurred in 1920, and it is also

<!-- b000930 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000931 | prose | pages [19] -->
logical to assume that Country had an evolution in 1920, when Country was born. The results关注数学模型

<!-- b000932 | furniture | pages [19] -->
2

<!-- b000933 | furniture | pages [19] -->
MATHmodels

<!-- b000934 | furniture | pages [19] -->
获取更多资讯

<!-- b000935 | furniture | pages [20] -->
Team # 2107091

<!-- b000936 | prose | pages [20] -->
2500

<!-- b000937 | prose | pages [20] -->
Total musicians number

<!-- b000938 | prose | pages [20] -->
2000

<!-- b000939 | prose | pages [20] -->
1500

<!-- b000940 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000941 | furniture | pages [20] -->
Page 20 of 25

<!-- b000942 | prose | pages [20] -->
Vocal Religious

<!-- b000943 | prose | pages [20] -->
Reggae R&B;

<!-- b000944 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000945 | prose | pages [20] -->
1000

<!-- b000946 | prose | pages [20] -->
500

<!-- b000947 | prose | pages [20] -->
0

<!-- b000948 | prose | pages [20] -->
1930 1950 1970

<!-- b000949 | prose | pages [20] -->
year

<!-- b000950 | prose | pages [20] -->
Latin Jazz

<!-- b000951 | prose | pages [20] -->
Electronic Country

<!-- b000952 | prose | pages [20] -->
Blues

<!-- b000953 | prose | pages [20] -->
1990 2010

<!-- b000954 | caption | pages [20] -->
Figure 14: Changes in the Number of Musicians Over Time

<!-- b000955 | prose | pages [20] -->
of the analysis are also consistent with the facts[7].

<!-- b000956 | prose | pages [20] -->
6.2 Major Inﬂuencers of Revolution

<!-- b000957 | prose | pages [20] -->
For a genre revolution, we analyze the music published within the genre in the two years

<!-- b000958 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000959 | prose | pages [20] -->
before and after the evolution, looking for the most popular artists during that part of the time. We sum the popularity of each musician’s works released during that period separately to obtain the popularity of each musician during that period, with the highest being the most inﬂuential in the evolution. Electronic is analyzed using the above method.

<!-- b000960 | prose | pages [20] -->
In 1950, Freestyle’s music has the highest sum of popularity: 144, can be considered as a major inﬂuencer on the 1950 evolution. In 1969, Jean-Jacques Perrey’s music has the highest sum of popularity: 139, can be considered as a major inﬂuencer for the 1969 evolution.

<!-- b000961 | prose | pages [20] -->
The trend of evolution in 1969 was maintained from the beginning of the evolution in 1969 to 1978, and we believe that a long-term change was produced during this period. We also identiﬁed the major inﬂuencers near 1969 to 1979 as Kraftwerk : sum of popularity=822, Yellow Magic Orchestra: sum of popularity=495, Vangelis: sum of popularity= 473.

<!-- b000962 | prose | pages [20] -->
Dynamic Inﬂuencer Evaluation Indicator 6.3

<!-- b000963 | prose | pages [20] -->
In the equation(24) in 5.1, we deﬁne IDS to measure the degree of inﬂuence that inﬂuencers have on their followers. As genres develop over time, there may be different key inﬂuencers within the genre at different times who will inﬂuence other musicians within the genre and lead the direction of the genre. To reveal the dynamic inﬂuencers within genre i, we deﬁne the Dynamic Inﬂuencer Indicator DII as follows.

<!-- b000964 | prose | pages [20] -->
For musician i, ﬁrst calculate its degree of inﬂuence IDSi,j on all musicians within the genre in turn and sum up IDS, to obtain the dynamic inﬂuencer index DIIi for musician i:

<!-- b000965 | prose | pages [20] -->
DIIi =

<!-- b000966 | prose | pages [20] -->
n n ∑

<!-- b000967 | prose | pages [20] -->
IDSi,j (29)

<!-- b000968 | prose | pages [20] -->
j=1

<!-- b000969 | prose | pages [20] -->
Within this genre, the musicians are ranked according to the DII of each musician. From the analysis of the percentage of major inﬂuencers in 3.3, a point threshold of 20% is used based on the law of Pareto’s Principle[4]. Musicians with DII ranking in the top 20% are then identiﬁed as dynamic inﬂuencers within this genre. We take Pop/Rock as an example, taking ten years as the analysis period, the DII of musicians within the genre of every period is calculated, and we list the two largest DII after normalization of musicians every decade shown in the Table(10).

<!-- b000970 | prose | pages [20] -->
As can be seen from the Table(10), the dynamic inﬂuencers within Pop/Rock are not the same in different eras, which is a good indication of the turnover of leading ﬁgures within the关注数学模型

<!-- b000971 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000972 | furniture | pages [20] -->
2

<!-- b000973 | furniture | pages [20] -->
MATHmodels

<!-- b000974 | furniture | pages [20] -->
获取更多资讯

<!-- b000975 | furniture | pages [21] -->
Team # 2107091

<!-- b000976 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000977 | furniture | pages [21] -->
Page 21 of 25

<!-- b000978 | caption | pages [21] -->
Table 10: DII of Musicians Over Time

<!-- b000979 | prose | pages [21] -->
Year 1950s 1960s Musician Elvis Presley Bob dylan 1970s 1980s 1990s The Clash Sex Pistols Blur

<!-- b000980 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000981 | prose | pages [21] -->
DII 0.9951 0.9926 Musician Little Richard Beatles DII 0.9814 1 0.9635 0.8964 0.9131 David Bowie Nirvana Beach Boys 0.9804 0.8413 0.8971

<!-- b000982 | prose | pages [21] -->
genre. The recognition threshold of DII is 0.8127, and musicians above this threshold can be identiﬁed as dynamic inﬂuencers.

<!-- b000983 | prose | pages [21] -->
Inﬂuence from Social, Political and Cultural Aspects 6.4

<!-- b000984 | prose | pages [21] -->
Changes in musical genre attributes often reﬂect the social, political, and cultural aspects of the time to some extent. We explore the social and cultural changes of the time by analyzing the changes in musical attributes such as valence related to emotions and acousticness related

<!-- b000985 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000986 | prose | pages [21] -->
to the use of science and technology in the music inﬂuence network across genres.

<!-- b000987 | prose | pages [21] -->
• From the general trends in the music industry

<!-- b000988 | prose | pages [21] -->
Taking the analysis of the emotional tendency of music as an example, we count the emo- tional tendency valence statistics of several genres of music that account for a relatively large proportion of the genre as shown in the Figure(15).

<!-- b000989 | prose | pages [21] -->
0.9 0.8 0.7 0.6 0.5

<!-- b000990 | prose | pages [21] -->
value

<!-- b000991 | prose | pages [21] -->
0.4 0.3 0.2 0.1 0

<!-- b000992 | prose | pages [21] -->
1921 1931 1941 1951 1961

<!-- b000993 | prose | pages [21] -->
Comedy/Spoken Jazz R&B; Religious

<!-- b000994 | prose | pages [21] -->
1971 1981 1991 2001 2011

<!-- b000995 | prose | pages [21] -->
year

<!-- b000996 | caption | pages [21] -->
Figure 15: Changes of valence Over Time

<!-- b000997 | prose | pages [21] -->
From the Figure(15), we can see that the emotional tendency of most genre songs started to become negative in 1947 and then became positive after 1965. Combined with the historical fact that the African-American Civil Rights Movement started in 1950 and ended in 1970, African- Americans were oppressed by society prior to the Civil Rights Movement, and the musicians used music to express their long-held negative feelings. After the civil rights movement, the future of African-Americans became clearer and they used music to express their desire for a better life. Thus we can consider that the emotional tendencies of music can, to some extent, reﬂect the implicit tendencies of society, politics, and culture, and be used to predict social revolution.

<!-- b000998 | prose | pages [21] -->
• From trends in speciﬁc music genres

<!-- b000999 | prose | pages [21] -->
Take the analysis of Electronic characteristics over time in 4.4.2 as an example. As shown in the Figure(11) in 4.4.2, the acousticness of Electronic increased signiﬁcantly in 1950, and so did the energy. It can be considered that Electronic has become more energetic and dynamic, which is related to the fact that people were in the ecstasy of achieving victory in the anti-fascist关注数学模型

<!-- b001000 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b001001 | furniture | pages [21] -->
2

<!-- b001002 | furniture | pages [21] -->
MATHmodels

<!-- b001003 | furniture | pages [21] -->
获取更多资讯

<!-- b001004 | furniture | pages [22] -->
Team # 2107091

<!-- b001005 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b001006 | furniture | pages [22] -->
Page 22 of 25

<!-- b001007 | prose | pages [22] -->
war after the Second World War in the 1950s. The cultural products of this historical period also fully reﬂect the optimistic and exciting social trends.

<!-- b001008 | prose | pages [22] -->
• From the listener’s reaction to the music

<!-- b001009 | prose | pages [22] -->
微信公众号：数学模型

<!-- b001010 | prose | pages [22] -->
In addition to the music itself, the connection between music and social development can also be glimpsed in the changes in listeners’ reactions to music. The trend of popularity in each category over time is plotted in Figure(16). It can be seen that there are more and more music listeners, which reﬂects the unprecedented increase in people’s ability to access information through the Internet as a result of the development of science and technology, making music accessible to a wider audience. This will further increase the inﬂuence of music on society, politics, and culture.

<!-- b001011 | prose | pages [22] -->
350 300

<!-- b001012 | prose | pages [22] -->
Total popularity

<!-- b001013 | prose | pages [22] -->
250 200 150 100 50

<!-- b001014 | prose | pages [22] -->
Vocal Religious

<!-- b001015 | prose | pages [22] -->
Reggae R&B;

<!-- b001016 | prose | pages [22] -->
Pop/Rock Latin

<!-- b001017 | prose | pages [22] -->
Jazz Electronic

<!-- b001018 | prose | pages [22] -->
微信号：MATHmodels

<!-- b001019 | prose | pages [22] -->
0

<!-- b001020 | prose | pages [22] -->
1921 1940 1959 1978

<!-- b001021 | prose | pages [22] -->
Year

<!-- b001022 | prose | pages [22] -->
Blues

<!-- b001023 | prose | pages [22] -->
1997 2016

<!-- b001024 | caption | pages [22] -->
Figure 16: Changes of popularity Over Time

<!-- b001025 | prose | pages [22] -->
7 Sensitive Analysis

<!-- b001026 | heading | pages [22] -->
Sensitive Analysis of Model in TASK 2

<!-- b001027 | prose | pages [22] -->
7.1

<!-- b001028 | prose | pages [22] -->
In Task 2 to build the Multi-dimensional Music Similarity Evaluation Model, we weight the local similarity Spart and the global similarity Sglobal to obtain MS:

<!-- b001029 | prose | pages [22] -->
MS = ((1−δ)Sglobal +δSpart)·(1+ 0.1

<!-- b001030 | prose | pages [22] -->
) (30)

<!-- b001031 | prose | pages [22] -->
Stime

<!-- b001032 | prose | pages [22] -->
The different weights δ may affect the evaluation results of similarity. Therefore, we choose 12 pieces of music from 3 genres to study the effect of different δ on the results, and choose δ = 0.2,0.5,0.8 to obtain the results of MS as Figure(17).

<!-- b001033 | prose | pages [22] -->
Looking at the above Figure(17) we can see that a change in δ does not change the broad similarity results respectively. However, the number of the parameter can have some effect on some speciﬁc categories of music, resulting in changes in musical similarity between or within genres, respectively.

<!-- b001034 | prose | pages [22] -->
• When δ is small, we can see higher similarity between genres. And Sglobal has a large weight and pays more attention to the differences of songs in all characteristics, which leads to lower similarity within the genre.

<!-- b001035 | prose | pages [22] -->
• When δ is large, it can be seen that the similarity between genres is lower. Spart has a larger weight and pays more attention to the differences in important features of songs, which makes the the similarity within the genre become higher.

<!-- b001036 | prose | pages [22] -->
Therefore, we choose δ = 0.5 in the model of the main text to make our similarity evaluation more balanced between local and global features.

<!-- b001037 | heading | pages [22] -->
Sensitive Analysis of Model in TASK 4

<!-- b001038 | prose | pages [22] -->
7.2

<!-- b001039 | prose | pages [22] -->
In the sliding window model in Task 4, the size of the window and step size may lead to

<!-- b001040 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b001041 | heading | pages [22] -->
different results. We use a variance-based sensitivity analysis method (Sobol method)[8] to关注数学模型

<!-- b001042 | furniture | pages [22] -->
2

<!-- b001043 | furniture | pages [22] -->
MATHmodels

<!-- b001044 | furniture | pages [22] -->
获取更多资讯

<!-- b001045 | furniture | pages [23] -->
Team # 2107091

<!-- b001046 | prose | pages [23] -->
δ =0.5

<!-- b001047 | prose | pages [23] -->
Pop/Rock R&B Jazz

<!-- b001048 | prose | pages [23] -->
Stash Old Treat Red Alma Lady Halo **** Doxy Oleo Work Maria

<!-- b001049 | prose | pages [23] -->
Stash 1.00 0.65 0.69 0.60 0.68 0.68 0.62 0.61 0.59 0.60 0.72 0.51

<!-- b001050 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b001051 | furniture | pages [23] -->
Page 23 of 25

<!-- b001052 | prose | pages [23] -->
Pop/Rock R&B Jazz

<!-- b001053 | prose | pages [23] -->
Stash Old Treat Red Almaz Lady Halo **** Doxy Oleo Work Maria Stash 1.00 0.47 0.52 0.42 0.51 0.51 0.44 0.43 0.44 0.44 0.64 0.41

<!-- b001054 | prose | pages [23] -->
Old 0.47 1.00 0.39 0.52 0.40 0.51 0.57 0.56 0.34 0.35 0.45 0.37 Treat 0.52 0.39 1.00 0.36 0.51 0.43 0.39 0.37 0.49 0.58 0.56 0.44 Red 0.42 0.52 0.36 1.00 0.40 0.50 0.57 0.63 0.34 0.33 0.42 0.36

<!-- b001055 | prose | pages [23] -->
微信公众号：数学模型

<!-- b001056 | prose | pages [23] -->
Old 0.65 1.00 0.59 0.67 0.57 0.66 0.71 0.70 0.49 0.51 0.58 0.44

<!-- b001057 | prose | pages [23] -->
Treat 0.69 0.59 1.00 0.55 0.68 0.63 0.58 0.57 0.62 0.68 0.67 0.53

<!-- b001058 | prose | pages [23] -->
Red 0.60 0.67 0.55 1.00 0.58 0.66 0.71 0.76 0.49 0.48 0.55 0.43

<!-- b001059 | prose | pages [23] -->
Alma

<!-- b001060 | prose | pages [23] -->
0.68 0.57 0.68 0.58 1.00 0.69 0.62 0.59 0.62 0.58 0.65 0.52 z

<!-- b001061 | prose | pages [23] -->
Lady 0.68 0.66 0.63 0.66 0.69 1.00 0.76 0.72 0.57 0.55 0.61 0.49

<!-- b001062 | prose | pages [23] -->
Halo 0.62 0.71 0.58 0.71 0.62 0.76 1.00 0.82 0.52 0.51 0.56 0.46

<!-- b001063 | prose | pages [23] -->
**** 0.61 0.70 0.57 0.76 0.59 0.72 0.82 1.00 0.50 0.50 0.55 0.44

<!-- b001064 | prose | pages [23] -->
Doxy 0.59 0.49 0.62 0.49 0.62 0.57 0.52 0.50 1.00 0.69 0.63 0.59

<!-- b001065 | prose | pages [23] -->
Oleo 0.60 0.51 0.68 0.48 0.58 0.55 0.51 0.50 0.69 1.00 0.65 0.60

<!-- b001066 | prose | pages [23] -->
Work 0.72 0.58 0.67 0.55 0.65 0.61 0.56 0.55 0.63 0.65 1.00 0.56

<!-- b001067 | prose | pages [23] -->
Maria 0.51 0.44 0.53 0.43 0.52 0.49 0.46 0.44 0.59 0.60 0.56 1.00

<!-- b001068 | prose | pages [23] -->
Almaz 0.51 0.40 0.51 0.40 1.00 0.52 0.44 0.41 0.47 0.43 0.54 0.42

<!-- b001069 | prose | pages [23] -->
Lady 0.51 0.51 0.43 0.50 0.52 1.00 0.63 0.57 0.41 0.39 0.49 0.40 Halo 0.44 0.57 0.39 0.57 0.44 0.63 1.00 0.72 0.36 0.35 0.43 0.38 **** 0.43 0.56 0.37 0.63 0.41 0.57 0.72 1.00 0.35 0.34 0.42 0.37 Doxy 0.44 0.34 0.49 0.34 0.47 0.41 0.36 0.35 1.00 0.51 0.43 0.35 Oleo 0.44 0.35 0.58 0.33 0.43 0.39 0.35 0.34 0.51 1.00 0.45 0.37 Work 0.64 0.45 0.56 0.42 0.54 0.49 0.43 0.42 0.43 0.45 1.00 0.31 Maria 0.41 0.37 0.44 0.36 0.42 0.40 0.38 0.37 0.35 0.37 0.31 1.00

<!-- b001070 | prose | pages [23] -->
Stash Old Treat Red Almaz Lady Halo **** Doxy Oleo Work Maria Stash 1.00 0.82 0.87 0.79 0.85 0.85 0.80 0.79 0.74 0.75 0.80 0.70

<!-- b001071 | prose | pages [23] -->
Old 0.82 1.00 0.78 0.82 0.74 0.81 0.85 0.84 0.63 0.67 0.71 0.62 Treat 0.87 0.78 1.00 0.80 0.86 0.83 0.78 0.76 0.75 0.79 0.78 0.73 Red 0.79 0.82 0.80 1.00 0.76 0.82 0.84 0.88 0.64 0.63 0.69 0.59 Almaz 0.85 0.74 0.86 0.76 1.00 0.85 0.79 0.78 0.76 0.74 0.76 0.72

<!-- b001072 | prose | pages [23] -->
Lady 0.85 0.81 0.83 0.82 0.85 1.00 0.89 0.86 0.73 0.72 0.74 0.69 Halo 0.80 0.85 0.78 0.84 0.79 0.89 1.00 0.92 0.68 0.68 0.69 0.64 **** 0.79 0.84 0.76 0.88 0.78 0.86 0.92 1.00 0.66 0.66 0.68 0.61 Doxy 0.74 0.63 0.75 0.64 0.76 0.73 0.68 0.66 1.00 0.86 0.82 0.83 Oleo 0.75 0.67 0.79 0.63 0.74 0.72 0.68 0.66 0.86 1.00 0.85 0.84 Work 0.80 0.71 0.78 0.69 0.76 0.74 0.69 0.68 0.82 0.85 1.00 0.80 Maria 0.70 0.62 0.73 0.59 0.72 0.69 0.64 0.61 0.83 0.84 0.80 1.00

<!-- b001073 | caption | pages [23] -->
Figure 17: Sensitive Analysis of the Model in Task 2

<!-- b001074 | prose | pages [23] -->
微信号：MATHmodels

<!-- b001075 | prose | pages [23] -->
investigate the effect on the results when multiple hyperparameters are varied simultaneously. The Sobol method simulates Monte Carlo sampling of the parameters in the feasible space and obtains a large number of outputs. The variance of the model output is the sum of all order variances of a single parameter. The equation for the contribution of the computed variance of the Sobol method is as follows:

<!-- b001076 | prose | pages [23] -->
p−1

<!-- b001077 | prose | pages [23] -->
p

<!-- b001078 | prose | pages [23] -->
∑

<!-- b001079 | prose | pages [23] -->
∑

<!-- b001080 | prose | pages [23] -->
Vi j +···+V1,···,p

<!-- b001081 | prose | pages [23] -->
V(Y) =

<!-- b001082 | prose | pages [23] -->
i=1

<!-- b001083 | prose | pages [23] -->
j=i+1

<!-- b001084 | prose | pages [23] -->
STi = EX∼i(VarXi(Y|X∼i))

<!-- b001085 | prose | pages [23] -->
Var(Y)

<!-- b001086 | prose | pages [23] -->
(31)

<!-- b001087 | prose | pages [23] -->
= 1−VarX∼i(EXi(Y|X∼i)

<!-- b001088 | prose | pages [23] -->
Var(Y)

<!-- b001089 | prose | pages [23] -->
The above equation measures the proportion of variance change caused by the interaction between one variable and other variables that change simultaneously. We then use the Sobol method on the sliding window model to study the sensitivity of window size and step size and show the sensitivity (ST) as Figure(18).

<!-- b001090 | caption | pages [23] -->
Figure 18: Sensitive Analysis of the Model in Task 4

<!-- b001091 | prose | pages [23] -->
It can be seen that the change in the size of the window of followers has the greatest im- pact on the results, which can indicate that the number of music selected in the calculation of short-term inﬂuences has the greatest impact on the ﬁnal inﬂuence results. This represents that

<!-- b001092 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b001093 | prose | pages [23] -->
for different musicians, when inﬂuenced by an inﬂuencer, different musicians may reﬂect the关注数学模型

<!-- b001094 | furniture | pages [23] -->
2

<!-- b001095 | furniture | pages [23] -->
MATHmodels

<!-- b001096 | furniture | pages [23] -->
获取更多资讯

<!-- b001097 | furniture | pages [24] -->
Team # 2107091

<!-- b001098 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b001099 | furniture | pages [24] -->
Page 24 of 25

<!-- b001100 | prose | pages [24] -->
inﬂuence of the inﬂuencer on several consecutive different songs. Some musicians may be in- spired only in the short term with only a small time period of songs reﬂecting this inﬂuence. While others may be inspired in the long term, with multiple songs over a long period of time reﬂecting the inﬂuence of an inﬂuencer on them.

<!-- b001101 | prose | pages [24] -->
微信公众号：数学模型

<!-- b001102 | prose | pages [24] -->
8

<!-- b001103 | heading | pages [24] -->
Strengths and Weaknesses

<!-- b001104 | prose | pages [24] -->
8.1

<!-- b001105 | heading | pages [24] -->
Strengths

<!-- b001106 | prose | pages [24] -->
• We used the theory of SNA to construct a network of inﬂuences between musicians and to measure the internal parameters of the network with more well-considered metrics.

<!-- b001107 | prose | pages [24] -->
• In analyzing whether inﬂuencers actually have an impact on followers, we used a sliding window time series approach to synthesize the short- and long-term impact of inﬂuencers on followers.

<!-- b001108 | prose | pages [24] -->
• We have done sufﬁcient visualization work on the algorithms and results of the model to facilitate understanding.

<!-- b001109 | prose | pages [24] -->
微信号：MATHmodels

<!-- b001110 | prose | pages [24] -->
• Most of our models are built with innovative ideas or improved based on original theories and speciﬁc problems, making our models both theoretical and innovative.

<!-- b001111 | prose | pages [24] -->
8.2

<!-- b001112 | heading | pages [24] -->
Weaknesses

<!-- b001113 | prose | pages [24] -->
• We could also go deeper into the analysis of certain issues, but due to space limitations, we can only stop here.

<!-- b001114 | prose | pages [24] -->
• Due to the lack of actual numerical reference, we can only observe the accuracy of our model from the actual situation and cannot numerically measure the accuracy of our model.

<!-- b001115 | heading | pages [24] -->
References

<!-- b001116 | references | pages [24] -->
[1] Zhang Cungang, Li Ming, Lu Demei. Social Network Analysis: An Important Sociological

<!-- b001117 | references | pages [24] -->
Research Method [J]. Gansu Social Sciences, 2004.

<!-- b001118 | references | pages [24] -->
[2] Haveliwala T H . Topic-sensitive PageRank: a context-sensitive ranking algorithm for Web

<!-- b001119 | references | pages [24] -->
search[J]. IEEE Transactions on Knowledge and Data Engineering, 2003, 15(4):p.784-

<!-- b001120 | references | pages [24] -->
796.

<!-- b001121 | references | pages [24] -->
[3] The 20 Most Representative Musicians in the World Jointly selected by CNN and Song-

<!-- b001122 | references | pages [24] -->
lines from http://edition.cnn.com/2010/SHOWBIZ/Music/08/04/your.music.i

<!-- b001123 | references | pages [24] -->
con/index.html

<!-- b001124 | references | pages [24] -->
[4] Chen Dao-lan. The Discriminatory Relationship Between the Law of Two and Eight and

<!-- b001125 | references | pages [24] -->
the Long Tail Theory[J]. Talent, 2010(15):280.

<!-- b001126 | references | pages [24] -->
[5] LIU Yan-xia, XIAO Wen-jun, XI Jian-qing, et al. Properties of Scale-free Networks with

<!-- b001127 | references | pages [24] -->
Power Index Less than 2 [J]. Journal of Nanchang University (Science Edition), 2013,

<!-- b001128 | references | pages [24] -->
37(004):350-354.

<!-- b001129 | references | pages [24] -->
[6] Electronic Music.Wikipedia https://en.wikipedia.org/wiki/Electronic_music

<!-- b001130 | references | pages [24] -->
[7] Sound and Music – 1890-2010, World Pop Music Echoes (news.cn) from the Xinhua News

<!-- b001131 | references | pages [24] -->
Agency http://fms.news.cn/swf/2016_sjxw/yqfm_2016/index.html

<!-- b001132 | references | pages [24] -->
[8] Zadeh, Farkhondeh Khorashadi,Nossent, Jiri,Sarrazin, Fanny, et al.Comparison of

<!-- b001133 | references | pages [24] -->
Variance-based and Moment-independent Global Sensitivity Analysis Approaches by Ap-

<!-- b001134 | references | pages [24] -->
plication to the SWAT Model [J].Environmental modelling & software,2017,91(May):210-

<!-- b001135 | references | pages [24] -->
222.

<!-- b001136 | references | pages [24] -->
[9] Tan H Q, Niu Q Q. A Time Series Symbolization Method Based on Sliding Window and

<!-- b001137 | references | pages [24] -->
Local Features[J]. Computer Application Research, 2013, 30(003):796-798.

<!-- b001138 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b001139 | references | pages [24] -->
关注数学模型

<!-- b001140 | furniture | pages [24] -->
2

<!-- b001141 | furniture | pages [24] -->
MATHmodels

<!-- b001142 | furniture | pages [24] -->
获取更多资讯

<!-- b001143 | furniture | pages [25] -->
Team # 2107091

<!-- b001144 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b001145 | furniture | pages [25] -->
Page 25 of 25

<!-- b001146 | heading | pages [25] -->
MEMO

<!-- b001147 | prose | pages [25] -->
To: Experts in The ICM Society

<!-- b001148 | prose | pages [25] -->
微信公众号：数学模型

<!-- b001149 | prose | pages [25] -->
From: Team 2107091 Date: February 8th, 2021 Subject: Analysis of Music Inﬂuence and Similarity, Suggestions for Futher Study

<!-- b001150 | prose | pages [25] -->
Dear experts in the ICM Society:

<!-- b001151 | prose | pages [25] -->
We are honored to inform you our achievement after performing data analysis and estab- lishing the music inﬂuence and similarity evaluation model.

<!-- b001152 | prose | pages [25] -->
Our team conducted a modeling analysis of the interactions between and within musicians across genres from 1921 to 2020. We develop a directed network for analyzing the interactions between musicians to understand the interactions that exist between musicians. An evaluation model to measure the similarity between the music is developed to provide an evaluation of the similarity between and within genres and to give the distinctive features of music in each genre.

<!-- b001153 | prose | pages [25] -->
微信号：MATHmodels

<!-- b001154 | prose | pages [25] -->
An evaluation model based on a sliding window is developed to select the leaders of each genre in different time periods. With the model we developed, we obtained the following valuable conclusions:

<!-- b001155 | prose | pages [25] -->
• The inﬂuence of musicians on each other is consistent with Pareto’s Principle, which states that a very small number of musicians have inﬂuenced the vast majority of musicians. We can consider that a very small number of outstanding musicians led the entire music world, and in-depth exploration of the works of these musicians may deepen our understanding of music.

<!-- b001156 | prose | pages [25] -->
• Although there are differences between the genres, they are not completely independent but have no clear boundaries. As a carrier of human emotions, music has similarities among genres. The study of the evolutionary process of musical alternation and fusion among genres is conducive to enhancing our perception of the evolution of music as a whole.

<!-- b001157 | prose | pages [25] -->
• Changes in music can clearly reﬂect social change. Music is a tool for people to express their feelings, and by monitoring changes in musical emotions, we can probe into the pent-up emotions in society and thus make predictions about social revolution.

<!-- b001158 | prose | pages [25] -->
The model we developed still has limitations due to incomplete data and space limitations. We also need more data to achieve the following objectives

<!-- b001159 | prose | pages [25] -->
• We found that some of the artists are not common to both datasets, and some of the artists’ debut dates are unknown, which causes some inaccuracy in our analysis. We hope to obtain a more complete dataset of artists and music.

<!-- b001160 | prose | pages [25] -->
• If we know the speciﬁc year in which the followers were inﬂuenced by the inﬂuencer, then we can reﬁne the model for determining the contagiousness of music and whether it actually produces change by the change in the music of the follower before and after the year of inﬂu- ence. Also, the dynamic impact indicators of inﬂuencers can be reﬁned based on the change in the number of inﬂuenced people.

<!-- b001161 | prose | pages [25] -->
• If we know the album information where the song is located, then we can modify our sliding window model to capture the short-term impact by directly comparing the similarity between albums.

<!-- b001162 | prose | pages [25] -->
We expect to build a dynamic network in the future in the dimension of time and genre.We also hope to make a more detailed division in genre and to develop a set of visualization system in the future, to more describe the internal development. The above are the results of our team’s

<!-- b001163 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b001164 | prose | pages [25] -->
关注数学模型 research, and we sincerely hope they can provide you with useful information and data.

<!-- b001165 | furniture | pages [25] -->
2

<!-- b001166 | furniture | pages [25] -->
MATHmodels

<!-- b001167 | furniture | pages [25] -->
获取更多资讯
