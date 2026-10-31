# P-D-2021-2124497-1be43b7c

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | prose | pages [1] -->
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
2124497

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
How to analyze the music objectively?

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
Music is a form of art that profoundly inﬂuences humans and societies. Given the four data sets, we are motivated to develop a series of objective measurements to analyze the music from four perspectives.

<!-- b000013 | prose | pages [1] -->
First of all, the measurement of music inﬂuence between artists is given by the combination of three indicators: 1) the indicator related to artists active in one certain decade being followed by artists active in other decades, 2) the indicator related to artists of one certain genre being followed by artists of other genres, and 3) the out-degree of the inﬂuencers. A weighted directed graph 퐺(푉, 퐸) is constructed to represent the inﬂuence network, where an edge is directed from the inﬂuencer to the

<!-- b000014 | title | pages [1] -->
微信号：MATHmodels

<!-- b000015 | prose | pages [1] -->
follower. Therefore, the calculated inﬂuence between the two artists is the weight of a directed edge.

<!-- b000016 | prose | pages [1] -->
Secondly, the music similarity is quantiﬁed. Since the provided data sets full_music_data contains high-dimensional data, thus the dimension reduction is needed. We are motivated to use the modiﬁed randomly distributed embedding (RDE) framework to take good advantage of interaction information of high-dimensional data. Moreover, the Bayes error rate is used to identify whether the distributions of within-genre and between-genre are signiﬁcantly diﬀerent.

<!-- b000017 | prose | pages [1] -->
Thirdly, we analyzed two kinds of roles of musical characteristics by examining the 푝-values from Kruskal-Wallis test. We removed each characteristic one at a time, and compared the 푝-values before and after the certain characteristics is removed. From the experiment results, the most inﬂuential characteristics in distinguishing genres are Energy, Valence, and Speechiness. The most contagious characteristics among artists are Acousticness, Danceability, and Valence.

<!-- b000018 | prose | pages [1] -->
Finally, we detected the most revolutionary artists by detecting the important nodes in the inﬂu- ence network using the modiﬁed closeness centrality (the synthesized centrality of in-closeness and out-closeness centrality). The calculated top 12 evolutionary artists are listed, including Bob Dylan, Chuck Berry, The Beatles, etc. In addition, the dynamic process of evolution is analyzed. By con- ducting discrete Fourier transform (DFT) and detecting the time series which is reconstructed from low-frequency components, we can observe the low-frequency components in a musical characteristic over time. An indicator 휎is proposed to measure the proportion of low-frequency components among all the frequency components. Energy and Popularity have large 휎values according to the experiment, meaning that there are rich low-frequency components in the time series of these two characteristics.

<!-- b000019 | keywords | pages [1] -->
Keywords: Complex Network; Bayes Error Rate; Closeness Centrality; Kruskal-Wallis Test;

<!-- b000020 | prose | pages [1] -->
Discrete Fourier Transform

<!-- b000021 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000022 | furniture | pages [1] -->
关注数学模型

<!-- b000023 | furniture | pages [1] -->
2

<!-- b000024 | furniture | pages [1] -->
MATHmodels

<!-- b000025 | furniture | pages [1] -->
获取更多资讯

<!-- b000026 | furniture | pages [2] -->
Team # 2124497

<!-- b000027 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000028 | furniture | pages [2] -->
Page 1 of 22

<!-- b000029 | heading | pages [2] -->
Contents

<!-- b000030 | contents | pages [2] -->
1

<!-- b000031 | heading | pages [2] -->
Introduction

<!-- b000032 | prose | pages [2] -->
2

<!-- b000033 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000034 | prose | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 2

<!-- b000035 | prose | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 An Overview of Our work

<!-- b000036 | prose | pages [2] -->
2 Problem Analysis

<!-- b000037 | prose | pages [2] -->
3

<!-- b000038 | heading | pages [2] -->
Model Assumptions and Notations

<!-- b000039 | prose | pages [2] -->
2

<!-- b000040 | prose | pages [2] -->
3

<!-- b000041 | prose | pages [2] -->
3

<!-- b000042 | prose | pages [2] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 3

<!-- b000043 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000044 | heading | pages [2] -->
Notations

<!-- b000045 | prose | pages [2] -->
4

<!-- b000046 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000047 | prose | pages [2] -->
4

<!-- b000048 | heading | pages [2] -->
Model Construction

<!-- b000049 | prose | pages [2] -->
4 Measurement of Inﬂuence between Artists . . . . . . . . . . . . . . . . . . . . . . 4.1 4 The Music Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 7

<!-- b000050 | prose | pages [2] -->
Quantiﬁcation of Similarities Based on the MRDE Framework . . . . . . . 4.2.1 8

<!-- b000051 | prose | pages [2] -->
Distribution of Similarities Between and Within Genres 4.2.2 . . . . . . . . . .

<!-- b000052 | prose | pages [2] -->
10 Test the Measurement of Inﬂuence by the Similarity Network 4.2.3 . . . . . . .

<!-- b000053 | prose | pages [2] -->
12

<!-- b000054 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 The Roles of Characteristics 14 Characteristics that Distinguish Genres 4.3.1 . . . . . . . . . . . . . . . . . . .

<!-- b000055 | prose | pages [2] -->
14

<!-- b000056 | prose | pages [2] -->
The Contagious Characteristics among Artists 4.3.2 . . . . . . . . . . . . . . .

<!-- b000057 | prose | pages [2] -->
16

<!-- b000058 | prose | pages [2] -->
Revolutionary Artists Based on Closeness Centrality 4.4 . . . . . . . . . . . . . . . .

<!-- b000059 | prose | pages [2] -->
17

<!-- b000060 | prose | pages [2] -->
Dynamic Process of Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5

<!-- b000061 | prose | pages [2] -->
5

<!-- b000062 | heading | pages [2] -->
Test the Model

<!-- b000063 | prose | pages [2] -->
6

<!-- b000064 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000065 | prose | pages [2] -->
18

<!-- b000066 | prose | pages [2] -->
21

<!-- b000067 | prose | pages [2] -->
21

<!-- b000068 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Strengths 21

<!-- b000069 | prose | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000070 | prose | pages [2] -->
7

<!-- b000071 | heading | pages [2] -->
Conclusion

<!-- b000072 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000073 | prose | pages [2] -->
22

<!-- b000074 | prose | pages [2] -->
22

<!-- b000075 | furniture | pages [2] -->
关注数学模型

<!-- b000076 | furniture | pages [2] -->
2

<!-- b000077 | furniture | pages [2] -->
MATHmodels

<!-- b000078 | furniture | pages [2] -->
获取更多资讯

<!-- b000079 | furniture | pages [3] -->
Team # 2124497

<!-- b000080 | prose | pages [3] -->
1

<!-- b000081 | heading | pages [3] -->
Introduction

<!-- b000082 | prose | pages [3] -->
1.1

<!-- b000083 | heading | pages [3] -->
Background

<!-- b000084 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000085 | furniture | pages [3] -->
Page 2 of 22

<!-- b000086 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000087 | prose | pages [3] -->
Music has had a profound eﬀect on humans and societies throughout history. The evolution of music occurs constantly, inﬂuenced by advanced technology, personal experiences, social events, etc. The internal inﬂuence between artists also accounts for the music changes. Analysis of music is usually deemed relatively perceptual and subjective. However, music that is more abstract in itself can be quantiﬁed by various characteristics, which makes it possible for us to analyze the music systematically and objectively.

<!-- b000088 | prose | pages [3] -->
One of our goals in this paper is to develop appropriate measures to quantify the inﬂuence and similarity of music. Based on the quantiﬁcation, more thorough analyses could be conducted, including identifying the signiﬁcant artists and characteristics. We believe that a better understand- ing of the music evolved could be also be obtained with a series of carefully designed models and experiments.

<!-- b000089 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000090 | prose | pages [3] -->
1.2 Restatement of the Problem

<!-- b000091 | prose | pages [3] -->
The analysis of music inﬂuence involves detail ranging from methods for quantiﬁcation to identiﬁcation of decisive factors. Thus, in order to analyze the inﬂuence of music in a clear and systematic way, we restate the problem as follows.

<!-- b000092 | prose | pages [3] -->
• Develop a measurement of music inﬂuence between artists, and construct a directed inﬂuence network that connects inﬂuencers and followers accordingly;

<!-- b000093 | prose | pages [3] -->
• Quantify the music similarities and compare the music similarities between and within genres;

<!-- b000094 | prose | pages [3] -->
• Testify whether there are signiﬁcant diﬀerences between the distributions of within-genre and between-genre similarities;

<!-- b000095 | prose | pages [3] -->
• Discover the decisive music characteristics that distinguish genres;

<!-- b000096 | prose | pages [3] -->
• Determine the most contagious music characteristics among artists;

<!-- b000097 | prose | pages [3] -->
• Identify the revolutionary artists, and analyze the evolution of music.

<!-- b000098 | prose | pages [3] -->
1.3 An Overview of Our work

<!-- b000099 | prose | pages [3] -->
To address the problem, this paper proposed ﬁve models to solve the respective sub-problems. The rest of the paper is structured as follows. Section 2 states a thorough problem analysis and our motivations. In Section 3, we give the assumptions and notations of the model. Section 4 provides suﬃcient details of our model. In Section 5, we test the proposed model. Section 6 analyzed the strengths and weaknesses of our model. At lat, a conclusion is given in Section 7. A one-page document to the ICM Society is given in the appendices???.

<!-- b000100 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000101 | furniture | pages [3] -->
关注数学模型

<!-- b000102 | furniture | pages [3] -->
2

<!-- b000103 | furniture | pages [3] -->
MATHmodels

<!-- b000104 | furniture | pages [3] -->
获取更多资讯

<!-- b000105 | furniture | pages [4] -->
Team # 2124497

<!-- b000106 | prose | pages [4] -->
2 Problem Analysis

<!-- b000107 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000108 | furniture | pages [4] -->
Page 3 of 22

<!-- b000109 | prose | pages [4] -->
Based on the detailed information provided by the four data sets, we ﬁrst systematically analyze the problem. After exploring and reviewing the relevant literature research, we then construct a

<!-- b000110 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000111 | prose | pages [4] -->
detailed model.

<!-- b000112 | prose | pages [4] -->
To begin with, the a directed network is required to be constructed from the inﬂuence_data data set. In inﬂuence_data, a detailed relationship between inﬂuencers and followers is given. For an inﬂuence network, an edge is directed from the inﬂuencer to the follower. Though a directed graph is easy to construct, a measurement of inﬂuence should be developed to describe the strength of the inﬂuence. Therefore, three factors are taking into account to measure the inﬂuence:1) the indicator related to artists active in one certain decade being followed by artists active in other decades, 2) the indicator related to artists of one certain genre being followed by artists of other genres, and 3) the out-degree of the inﬂuencers.

<!-- b000113 | prose | pages [4] -->
On top of that, the music similarity also needs to be quantiﬁed. An abundant amount of data are provided in full_music_data data set, and the quantiﬁcation of high-dimensional data is therefore

<!-- b000114 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000115 | prose | pages [4] -->
essential. Classical methods, such as the principal components analysis (PCA), are commonly used for dimension reduction. However, we are motivated to use the modiﬁed the randomly distributed framework (RDE) instead, which can take good advantage of interaction information provided by high-dimensional data. We also testify diﬀerence between the distribution of within-genre and between-genre similarities to justify whether the inﬂuencers indeed inﬂuence the followers.

<!-- b000116 | prose | pages [4] -->
Thirdly, we need to analyze roles of characteristics under diﬀerent circumstances. The inﬂuential characteristics are deﬁned to be the ones that are eﬀective in distinguishing the genres, and the contagious characteristics are deﬁned to represent the common inherent music features among artists. We are inspired to test the inﬂuence of a characteristics by comparing the p-values (obtained by conducting non-parametric test) before and after it is removed from other characteristics.

<!-- b000117 | prose | pages [4] -->
Afterwards, the artists who signify the revolutionaries is detected. Empirically, we assume that the revolutionary artists have great impact on others while receiving small inﬂuence from others. Therefore, we are motivated to calculate closeness centrality of the directed inﬂuence network, and use the diﬀerence between out-closeness and in-closeness centrality to measure how revolutionary an artist is.

<!-- b000118 | prose | pages [4] -->
Finally, the analyze of dynamic process of evolution is needed. With the date given in data_year, we aim at analyzing the evolution trend of each musical characteristics from the perspective of frequency domain. Therefore, we are motivated to conduct the discrete Fourier transform in order to observe the diﬀerent frequency components. Since it is not objective to observe the series by the curve shapes, we developed an indicator σ that measures the proportion of low-frequency components.

<!-- b000119 | heading | pages [4] -->
Model Assumptions and Notations

<!-- b000120 | prose | pages [4] -->
3

<!-- b000121 | prose | pages [4] -->
3.1

<!-- b000122 | heading | pages [4] -->
Assumptions and Justiﬁcations

<!-- b000123 | prose | pages [4] -->
• The musical characteristics chosen in the data set are representative;

<!-- b000124 | prose | pages [4] -->
• The data collected are reliable;

<!-- b000125 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000126 | furniture | pages [4] -->
关注数学模型

<!-- b000127 | furniture | pages [4] -->
2

<!-- b000128 | furniture | pages [4] -->
MATHmodels

<!-- b000129 | furniture | pages [4] -->
获取更多资讯

<!-- b000130 | furniture | pages [5] -->
Team # 2124497

<!-- b000131 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000132 | furniture | pages [5] -->
Page 4 of 22

<!-- b000133 | prose | pages [5] -->
• The revolutionary artist are the ones who have large impact on others while receiving small inﬂuence from others;

<!-- b000134 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000135 | prose | pages [5] -->
3.2

<!-- b000136 | heading | pages [5] -->
Notations

<!-- b000137 | prose | pages [5] -->
Symbol Deﬁnition G A directed graph describing the inﬂuence among artists

<!-- b000138 | prose | pages [5] -->
The ith node in the graph G vi

<!-- b000139 | prose | pages [5] -->
The edge in graph G directed from node vi to node vj eij

<!-- b000140 | prose | pages [5] -->
wij The weight of edge eij

<!-- b000141 | prose | pages [5] -->
The number of nodes in graph G n0

<!-- b000142 | prose | pages [5] -->
The in-degree of node vj nj

<!-- b000143 | prose | pages [5] -->
The inﬂuence of inﬂuencer vi on follower vj Iij

<!-- b000144 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000145 | prose | pages [5] -->
The weight on edge eij in graph G wij

<!-- b000146 | prose | pages [5] -->
Sij The musical similarity between two nodes

<!-- b000147 | prose | pages [5] -->
The ith musical characteristics, i = 1, 2, ...13 ci

<!-- b000148 | prose | pages [5] -->
The set of labels of artists that followed artist vi Fi

<!-- b000149 | prose | pages [5] -->
The in-closeness centrality of node vi CCi(i)

<!-- b000150 | prose | pages [5] -->
The out-closeness centrality of node vi CCo(i)

<!-- b000151 | prose | pages [5] -->
The synthesized closeness centrality of node vi C(i)

<!-- b000152 | prose | pages [5] -->
4

<!-- b000153 | heading | pages [5] -->
Model Construction

<!-- b000154 | prose | pages [5] -->
Measurement of Inﬂuence between Artists 4.1

<!-- b000155 | prose | pages [5] -->
According to the inﬂuence relationship revealed in the inﬂuence_data data set, a directed graph G(V, E) can be constructed, where V is a set of nodes and E is a set of links directed from one node to another. Let n0 be the number of nodes (the number of artists mentioned in inﬂuence_data). The n0 nodes are labeled from v1 to vn0, and eij denotes the edge directed from vi to vj. For each follower vj, let nj represent its in-degree (i. e. the number of artists that inﬂuence vj). A subgraph showing the relation among one follower and its inﬂuencers is illustrated in Fig. 1.

<!-- b000156 | prose | pages [5] -->
In a addition to construct a directed network by simply connecting the inﬂuencer to the follower, we aim at measuring the inﬂuence by three indicators from the perspective of a pair of the follower and inﬂuencer on edge eij: 1) frequency ekij that indicates the inﬂuence according to the period where inﬂuencer vi and follower vj are active, 2) frequency emij that describes the inﬂuence due to

<!-- b000157 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000158 | furniture | pages [5] -->
关注数学模型

<!-- b000159 | furniture | pages [5] -->
2

<!-- b000160 | furniture | pages [5] -->
MATHmodels

<!-- b000161 | furniture | pages [5] -->
获取更多资讯

<!-- b000162 | furniture | pages [6] -->
Team # 2124497

<!-- b000163 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000164 | furniture | pages [6] -->
Page 5 of 22

<!-- b000165 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000166 | caption | pages [6] -->
Fig. 1. The subgraph of one follower vj and its nj inﬂuencers

<!-- b000167 | prose | pages [6] -->
the main genres of inﬂuencer vi and follower vj, and 3) the out degree Oi of the inﬂuencer vi. To better explain the three indicator, more explicit deﬁnitions of ekij and emij are given as follows.

<!-- b000168 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000169 | prose | pages [6] -->
Let Di be the decade when the artist vi begin his or her music career. For inﬂuencer vi and follower vj on edge eij, kij is deﬁned to be the total number of times that artists in period Di are followed by artists in period Dj.

<!-- b000170 | prose | pages [6] -->
Deﬁnition 4.1. For edge eij that is directed from inﬂuencer vi to follower vj, the indicator ekij is deﬁned as:

<!-- b000171 | prose | pages [6] -->
ekij = P kij

<!-- b000172 | prose | pages [6] -->
(1)

<!-- b000173 | prose | pages [6] -->
l∈Sj klj

<!-- b000174 | prose | pages [6] -->
where Sj is the set of labels of inﬂuencers of follower vj.

<!-- b000175 | prose | pages [6] -->
Similarly, let Ri be the main genre of artist vi. Then mij is deﬁned as the total number of times that artists of genre Ri are followed by artists in genre Rj.

<!-- b000176 | prose | pages [6] -->
Deﬁnition 4.2. For edge eij that is directed from inﬂuencer vi to follower vj, the indicator emij is deﬁned as:

<!-- b000177 | prose | pages [6] -->
emij = P mij

<!-- b000178 | prose | pages [6] -->
(2)

<!-- b000179 | prose | pages [6] -->
l∈Sj mlj

<!-- b000180 | prose | pages [6] -->
where Sj is the set of labels of inﬂuencers of follower vj.

<!-- b000181 | prose | pages [6] -->
Applying the data from inﬂuence_data), the ekij and emij for inﬂuencers and followers of each type (including the decade when they began their music career and their main genres) are shown in

<!-- b000182 | caption | pages [6] -->
Fig. 2.

<!-- b000183 | prose | pages [6] -->
Therefore, the inﬂuence Iij of inﬂuencer vi on follower vj should be able to aggregate the data and information provided by the three indicators, i. e. ekij, emij and Oi.

<!-- b000184 | prose | pages [6] -->
Deﬁnition 4.3. The inﬂuence Iij of inﬂuencer vi on follower vj on edge eij is deﬁned as:

<!-- b000185 | prose | pages [6] -->
Iij = ekij · emij · Oi

<!-- b000186 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000187 | prose | pages [6] -->
(3)

<!-- b000188 | furniture | pages [6] -->
关注数学模型

<!-- b000189 | furniture | pages [6] -->
2

<!-- b000190 | furniture | pages [6] -->
MATHmodels

<!-- b000191 | furniture | pages [6] -->
获取更多资讯

<!-- b000192 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000193 | furniture | pages [7] -->
Team # 2124497

<!-- b000194 | furniture | pages [7] -->
Page 6 of 22

<!-- b000195 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000196 | prose | pages [7] -->
(a) The indicator kij

<!-- b000197 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000198 | prose | pages [7] -->
(b) The indicator mij

<!-- b000199 | caption | pages [7] -->
Fig. 2. The calculation results of mij and kij. (a) The indicator kij for any pair of inﬂuencers and

<!-- b000200 | prose | pages [7] -->
followers, where the vertical axis denotes the decade when the followers began their music career, and the horizontal axis denotes the time interval of the decade of followers and inﬂuencers. (b) The indicator mij for any pair of inﬂuencers and followers, where the vertical and horizontal axes represent the main genre of the followers and inﬂuencers, respectively.

<!-- b000201 | prose | pages [7] -->
Here, in Example 1, we give a brief example to better illustrate the calculation of inﬂuence emij (the indicator ekij can be calculated by using the exact same method). Since the number of inﬂuencer is huge and the out-degree Oi for the inﬂuencers in each edge can be easily found out from the data set, we will avoid displaying the cumbersome data here.

<!-- b000202 | prose | pages [7] -->
Consider an inﬂuencer vi and a follower vj whose main genres are Avant_garde Example 1 and Classical, respectively. Through the statistics in inﬂuence_data data set, the total number of times for artists of genre Classical to be inﬂuenced by artists of genre Avant_garde is 11, i. e. mij = 11. Additionally, there are in total 37 artists of various genres being followed by the artists of genre Avant_garde. Therefore, it can be calculated that the indicator emij between these two

<!-- b000203 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000204 | furniture | pages [7] -->
关注数学模型

<!-- b000205 | furniture | pages [7] -->
2

<!-- b000206 | furniture | pages [7] -->
MATHmodels

<!-- b000207 | furniture | pages [7] -->
获取更多资讯

<!-- b000208 | furniture | pages [8] -->
Team # 2124497

<!-- b000209 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000210 | furniture | pages [8] -->
Page 7 of 22

<!-- b000211 | prose | pages [8] -->
artists is emij = 11/37 ≈0.2973. It should be noted that the emij remains the same for any pair of inﬂuencer and follower whose genres are respectively Avant_garde and Classical.

<!-- b000212 | prose | pages [8] -->
By employing the calculation method illustrated in Example 1, let the weight wij of each

<!-- b000213 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000214 | prose | pages [8] -->
directed edge in graph G be the quantiﬁed inﬂuence Iij (i. e. wij = Iij). Therefore, a weight matrix W is obtained, and graph G can be extended to G(V, E, W ). Fig. 3 demonstrated the overall structure of graph G.

<!-- b000215 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000216 | caption | pages [8] -->
Fig. 3. The structure of graph G. The size of nodes represents the out-degree. The largest two

<!-- b000217 | prose | pages [8] -->
nodes are Bod Dylan and The Beatles, whose subnetwork is presented in Fig. 4

<!-- b000218 | prose | pages [8] -->
In Fig. 3, the color of nodes represent the genre they belong to, and the thickness of an edge denote the its weight (the thicker the edge is, the larger its weight is). Fig. 3 gives a rough distribution of genres and inﬂuence among artist, but is hard to discover details from. To give a better insight into the inﬂuence among artists, a subnetwork shown in Fig. 4 is provided.

<!-- b000219 | prose | pages [8] -->
4.2 The Music Similarity

<!-- b000220 | prose | pages [8] -->
With an abundant amount of data regarding the music-related characteristics, it is essential to develop a measurement to quantify the similarity with these high-dimensional data. Moreover, it is also of great importance to analysis whether the genres are distinguishable according to the similarity measurement that we developed. In this section, we proposed a modiﬁed randomly distributed embedding (MRDE) framework to measure the music similarity, which takes good advantage of interaction information among high-dimensional data. Afterwards, we analyze the similarity distribution between and within genres to identify whether the diﬀerence between within- genre similarity and between-genre similarity is signiﬁcant. Finally, we test the eﬀectiveness of the proposed measurement of inﬂuence in Section 4.1 by analyzing the similarity distribution among artist who do or do nor have mutual inﬂuence.

<!-- b000221 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000222 | furniture | pages [8] -->
关注数学模型

<!-- b000223 | furniture | pages [8] -->
2

<!-- b000224 | furniture | pages [8] -->
MATHmodels

<!-- b000225 | furniture | pages [8] -->
获取更多资讯

<!-- b000226 | furniture | pages [9] -->
Team # 2124497

<!-- b000227 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000228 | furniture | pages [9] -->
Page 8 of 22

<!-- b000229 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000230 | caption | pages [9] -->
Fig. 4. A subnetwork of Bod Dylan, The Beatles and their followers

<!-- b000231 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000232 | prose | pages [9] -->
Quantiﬁcation of Similarities Based on the MRDE Framework 4.2.1

<!-- b000233 | prose | pages [9] -->
In this section, we demonstrate our model for quantifying the musical similarity. The proposed MRDE framework is explained carefully, and the quantiﬁcation result is then given and visualized.

<!-- b000234 | prose | pages [9] -->
To begin with, a brief introduction of the original RDE (randomly distributed embedding) framework is given. The RDE framework is ﬁrst proposed by Ma et al. in 2018 published on PNAS [1]. When dealing with high-dimensional data, dimension reduction techniques are usually applied, but the application is likely to overlook the interactions among high-dimensional variables. To make good use of the interaction information, the RDE framework builds a distribution of a suﬃcient number of embeddings of low-dimension. While each low-dimensional embedding preserves a part a information of the whole system, these low-dimensional embeddings form a probability distribution which can be used to obtain the ﬁnal one-dimensional variable (or the value). Readers could refer to more details in [1]. Hence, we proposed the MRDE framework to adapt the original RDE framework for the problem discussed in this paper, which provides another perspective for the comprehensive evaluation.

<!-- b000235 | prose | pages [9] -->
Among the fourteen musical characteristics summarized in data_by_artist, we eliminate the factor count for the experiment in this section, since count is not music-related and do not provide any information about an artist’s music style. Then we are left with 13 musical characteristics from danceability to popularity. In the MRDE framework, we choose the embedding dimension e to be e = 3 empirically according to the experiment in [1]. In other words, for each 3-dimension embedding, we randomly choose 3 characteristics out of the 13 musical characteristics. There are in total q kinds of combination of the chosen 3 characteristics, which can be calculated by Eq. (4).

<!-- b000236 | prose | pages [9] -->
q =

<!-- b000237 | prose | pages [9] -->
E

<!-- b000238 | prose | pages [9] -->


<!-- b000239 | prose | pages [9] -->
(4)

<!-- b000240 | prose | pages [9] -->
e

<!-- b000241 | prose | pages [9] -->
where E = 13 is the total number of musical characteristics involved in the analysis, e = 3 is the embedding dimension.

<!-- b000242 | prose | pages [9] -->
Each of the 13 musical characteristic is label from c1 to c13. For each 3-dimensional embedding,

<!-- b000243 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000244 | furniture | pages [9] -->
关注数学模型

<!-- b000245 | furniture | pages [9] -->
2

<!-- b000246 | furniture | pages [9] -->
MATHmodels

<!-- b000247 | furniture | pages [9] -->
获取更多资讯

<!-- b000248 | furniture | pages [10] -->
Team # 2124497

<!-- b000249 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000250 | furniture | pages [10] -->
Page 9 of 22

<!-- b000251 | prose | pages [10] -->
we construct an index tuple l = (l1, l2, l2), (lk = 1, 2, ...13, k = 1, 2, 3), where l1, l2 and l3 are Let Cj represent the tuple of values of 3 chosen the indexes of characteristics in this tuple. characteristics for node vj, then the three characteristics of artist vj is represented as Cj =

<!-- b000252 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000253 | prose | pages [10] -->
(cl1, cl2, cl3).

<!-- b000254 | prose | pages [10] -->
When measuring the similarity between artist vi and artist vj, we need to ﬁrst identify their rough similarity calculated by each embedding. For the kth 3-dimensional embedding (k=1, 2, ..., q), we deﬁne its rough similarity srk as

<!-- b000255 | prose | pages [10] -->
srk = 1 −∥Ci −Cj∥2 (5)

<!-- b000256 | prose | pages [10] -->
Let Sr be the random variable where srk(k = 1, 2, ..., q) are the speciﬁc value. Therefore, the q rough similarity labeled from sr1 to srq can form a probability distribution. The actual similarity Sij between vi and vj is deﬁned as the expectation value of the distribution, formulated in Eq. (6).

<!-- b000257 | prose | pages [10] -->
Sij = E(Sr) (6)

<!-- b000258 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000259 | prose | pages [10] -->
where Sij ∈[0, 1], and E(Sr) is the expectation of random variable Sr. When Sij is large, it indicates that the these two artist are more similar, and vice versa.

<!-- b000260 | prose | pages [10] -->
By using Eq. (5) and Eq. (6), the similarity Sij between vi and vj can be calculated. The proposed MRDE framework can be better illustrated by the following steps:

<!-- b000261 | prose | pages [10] -->
Step 1: Randomly choose q tuples. Each tuple contains 3 index numbers denoted as l = (l1, l2, l2),

<!-- b000262 | prose | pages [10] -->
and the musical characteristics in this tuple are denoted as (cl1, cl2, cl3);

<!-- b000263 | prose | pages [10] -->
Step 2: For the q tuples (namely the 3-dimensional embeddings), calculated the rough similarity

<!-- b000264 | prose | pages [10] -->
srk, k = 1, 2, ..., q by using Eq. (5);

<!-- b000265 | prose | pages [10] -->
Step 3: Aggregate the rough similarities calculated in each embedding to form the probability

<!-- b000266 | prose | pages [10] -->
distribution of the random variable Sr;

<!-- b000267 | prose | pages [10] -->
Step 4: Given the distribution of Sr, obtain the similarity Sij = E(Sr) by calculating the expec-

<!-- b000268 | prose | pages [10] -->
tation value of random variable Sr.

<!-- b000269 | prose | pages [10] -->
A undirected network G1(V1, E1) is constructed, where V1 is the set of nodes and E1 the set of undirected edges. Since nodes being analyzed are the same as in G, so the label of nodes remain the same (such v1, v2 etc.). It should be noted that even though Eq. (6) and Fig. ?? measures the musical similarity between two artists, the proposed MRDE scheme can also be applied to quantify the musical similarity between genres and songs, as long as the musical characteristics are available.

<!-- b000270 | heading | pages [10] -->
Discussion

<!-- b000271 | prose | pages [10] -->
In the original data_by_artist data set, the order of magnitude of each musical characteristics varies from −6 to 5 . However, since the Euclidean norm is used to measure the rough similarity, the inﬂuence of order of magnitude must be eliminated as much as possible before calculating the

<!-- b000272 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000273 | furniture | pages [10] -->
关注数学模型

<!-- b000274 | furniture | pages [10] -->
2

<!-- b000275 | furniture | pages [10] -->
MATHmodels

<!-- b000276 | furniture | pages [10] -->
获取更多资讯

<!-- b000277 | furniture | pages [11] -->
Team # 2124497

<!-- b000278 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000279 | furniture | pages [11] -->
Page 10 of 22

<!-- b000280 | prose | pages [11] -->
Euclidean norm. Thus, the min-max normalization is utilized to normalize each characteristics. All of the normalized value of musical characteristics range from 0 to 1. Moreover, when we apply

<!-- b000281 | prose | pages [11] -->
√

<!-- b000282 | prose | pages [11] -->
3. Thus, the calculated

<!-- b000283 | prose | pages [11] -->
the 3-dimensional embedding, the maximum value of rough similarity is

<!-- b000284 | prose | pages [11] -->
√

<!-- b000285 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000286 | prose | pages [11] -->
similarities Sij are reduced to 1/

<!-- b000287 | prose | pages [11] -->
3 of the original scale.

<!-- b000288 | prose | pages [11] -->
Distribution of Similarities Between and Within Genres 4.2.2

<!-- b000289 | prose | pages [11] -->
From Section 4.2.1, we have obtained the similarity between every two artists.

<!-- b000290 | prose | pages [11] -->
From the inﬂuence_data data set, we can easily label each artist with his or her main genre. Therefore, the similarity distribution among artists can easily be transformed into similarity distribution between and within genres. From our intuitive understanding, we would assume that the similarity within genres are smaller than between genres. We might assume that the similarity between genres might also varies. For instance, the genre of Electronic and Country may diﬀer from each other from our daily experience. In this section, we will use the similarity distribution, Gaussian ﬁtting and Bayes error rate for a thorough analysis.

<!-- b000291 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000292 | prose | pages [11] -->
Among the 19 genres (the genre Unknown is eliminated due to the possible interference of wrong or missing information), there are in total

<!-- b000293 | prose | pages [11] -->
 19

<!-- b000294 | prose | pages [11] -->


<!-- b000295 | prose | pages [11] -->
kinds of combinations. Fig. 5 is an example

<!-- b000296 | prose | pages [11] -->
2

<!-- b000297 | prose | pages [11] -->
of the similarity distribution within the genre Folk and between Folk and Reggae.

<!-- b000298 | caption | pages [11] -->
Fig. 5. The similarity within and between genres. The blue part denotes the similarity distribution

<!-- b000299 | prose | pages [11] -->
within the genre of Folk, while the red part denotes the distribution between Folk and Reggae. The vertical axis represents the number of times that a certain value of similarity appears in the total calculated similarities, and the horizontal axis represents the similarity ranged from 0 to 1.

<!-- b000300 | prose | pages [11] -->
From Fig. 5, we can have an intuitive understanding that the similarity distribution within and between genres is diﬀerent in the given example. But now a question arises: how can this diﬀerence be measured?

<!-- b000301 | prose | pages [11] -->
We are motivated to measure the above-mentioned diﬀerence by using Bayes error rate. Bayesian decision theory can address the patter classiﬁcation problem from the perspective of statistics [2].

<!-- b000302 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000303 | furniture | pages [11] -->
关注数学模型

<!-- b000304 | furniture | pages [11] -->
2

<!-- b000305 | furniture | pages [11] -->
MATHmodels

<!-- b000306 | furniture | pages [11] -->
获取更多资讯

<!-- b000307 | furniture | pages [12] -->
Team # 2124497

<!-- b000308 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000309 | furniture | pages [12] -->
Page 11 of 22

<!-- b000310 | prose | pages [12] -->
The theory quantiﬁes the trade-oﬀbetween the decision made and the costs that accompany the decision. Bayes error, on the other hand, is the lowest possible error rate for a pattern classiﬁcation problem [3]. Let class ω1 denote the within genres, class ω2 denote the between genres, and s denote

<!-- b000311 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000312 | prose | pages [12] -->
the similarity value. P(ωi|s), i = 1, 2 is the posterior probability. For the distribution illustrated in Fig. 6, the probability of error can be calculated by Eq. (7).

<!-- b000313 | prose | pages [12] -->
(

<!-- b000314 | prose | pages [12] -->
P(ω1|s)

<!-- b000315 | prose | pages [12] -->
P(error|s) =

<!-- b000316 | prose | pages [12] -->
P(ω2|s) whenP(ω2|s) > P(ω1|s) (7) whenP(ω1|s) > P(ω2|s)

<!-- b000317 | prose | pages [12] -->
The Bayes error rate is therefore formulated in Eq. (8).

<!-- b000318 | prose | pages [12] -->
Z s0

<!-- b000319 | prose | pages [12] -->
Z ∞

<!-- b000320 | prose | pages [12] -->
P(ω2|s)p(s)ds +

<!-- b000321 | prose | pages [12] -->
P(error) =

<!-- b000322 | prose | pages [12] -->
−∞

<!-- b000323 | prose | pages [12] -->
P(ω1|s)p(s)ds (8)

<!-- b000324 | prose | pages [12] -->
s0

<!-- b000325 | prose | pages [12] -->
where s0 is a certain point on the horizontal axis shown in Fig. 6 that divides the space into two parts. P(error) can also be denoted as the size of shadow area.

<!-- b000326 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000327 | prose | pages [12] -->
Due to the large scale of data, we demonstrate some typical similarity distribution here. First of all, Fig. 7 shows the similarity within and between the genres of Country and Eletronic.

<!-- b000328 | prose | pages [12] -->
From Fig. 7, it can be observed that the overall similarity within Country is much smaller than the one within Electronic and between these two genres. The results indicate that value of musical characteristics of artists of genre Country are highly similar, whereas the ones of artists of genre Electronic are relatively scattered. Moreover, by performing Gaussian ﬁtting, the estimated distribution for within the genre Country, within the genre Electronic and between the two genres are N(0.85, 0.06), N(0.74, 0.0.8) and N(0.75, 0.09), respectively. With the Gaussian ﬁtting results, the Bayes error of distributions in Fig. 7(a) and Fig. 7(b) are 0.486 and 0.916, respectively, indicating again that the similarity distributions in Fig. 7(a) are more diﬀerent and distinguishable.

<!-- b000329 | prose | pages [12] -->
In order to have an overall understanding of the similarity within and between genres, Fig. 8 shows the similarity distribution by combining all the values of similarity within each genre and between every two genres.

<!-- b000330 | prose | pages [12] -->
The Gaussianﬁttingresultofthewithin-genreandbetween-genredistributionareN(0.806, 0.078) and N(0.758, 0.095), respectively. The Bayes error rate calculated is 0.770. Combining the vi- sualization result in Fig. 8, the Gaussian ﬁtting result and the calculated Bayes error rate, we can

<!-- b000331 | caption | pages [12] -->
Fig. 6. An example of probability distribution to illustrate the Bayes error rate

<!-- b000332 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000333 | furniture | pages [12] -->
关注数学模型

<!-- b000334 | furniture | pages [12] -->
2

<!-- b000335 | furniture | pages [12] -->
MATHmodels

<!-- b000336 | furniture | pages [12] -->
获取更多资讯

<!-- b000337 | furniture | pages [13] -->
Team # 2124497

<!-- b000338 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000339 | furniture | pages [13] -->
Page 12 of 22

<!-- b000340 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000341 | prose | pages [13] -->
(a) The similarity within Country and between genres (b) The similarity within Electronic and between genres

<!-- b000342 | caption | pages [13] -->
Fig. 7. The similarity distribution within and between two typical genres. (a) The light blue and

<!-- b000343 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000344 | prose | pages [13] -->
blue curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result between Country and Electronic. The light orange and orange curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result within Country. (b) The light blue and blue curves denote the same thing as in subgraph a. The light orange and orange curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result within Electronic.

<!-- b000345 | prose | pages [13] -->
reach a conclusion: 1) the similarity between genres is generally larger than within genres, and 2) the smaller the between-genre similarity is, the less similar are the corresponding two genres.

<!-- b000346 | prose | pages [13] -->
Test the Measurement of Inﬂuence by the Similarity Network 4.2.3

<!-- b000347 | prose | pages [13] -->
In section 4.1, the measurement of inﬂuence among artists is proposed. In Section 4.2.1, we quantify the similarities of musical characteristics. To discover the interaction relationship between the above-mentioned two measurements, we conduct another experiment by combining the directed network G of inﬂuence and the undirected network G1 of similarities. The experiment is aim at detecting whether the measurement of inﬂuence in Section 4.1 can actually reﬂect the real-world inﬂuence among artists.

<!-- b000348 | prose | pages [13] -->
First of all, we will explained how the combination works in this paper. Basically, we will reallocate the similarity distribution in G1 in to two distribution, based on whether two artists have unilateral or mutual inﬂuence on each other in graph G. Let S1 and S2 be two random variables, where S1 denotes the similarity distribution of edges in G1 that are connected in graph G (the directed graph describing the inﬂuence), and S2 denotes the similarity distribution of edges in G1 that are not connected in graph G.

<!-- b000349 | prose | pages [13] -->
Step 1: Start traversing all edges in the undirected similarity network G1;

<!-- b000350 | prose | pages [13] -->
Step 2: Consider an undirected edge that connect node vi and vj. If there exists a directed edge in

<!-- b000351 | prose | pages [13] -->
the inﬂuence network G directed from vi to vj or from vj to vi, then the similarity value Sij on this undirected edge is a possible value of the random variable S1;

<!-- b000352 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000353 | furniture | pages [13] -->
关注数学模型

<!-- b000354 | furniture | pages [13] -->
2

<!-- b000355 | furniture | pages [13] -->
MATHmodels

<!-- b000356 | furniture | pages [13] -->
获取更多资讯

<!-- b000357 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000358 | furniture | pages [14] -->
Team # 2124497

<!-- b000359 | furniture | pages [14] -->
Page 13 of 22

<!-- b000360 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000361 | caption | pages [14] -->
Fig. 8. The overall similarity distribution. The light orange and orange curves denote the distribution

<!-- b000362 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000363 | prose | pages [14] -->
that concludes the between-genre similarity of any combination of two genres. The light blue and blue curves denote the distribution that concludes all the within-genre similarity of every genre.

<!-- b000364 | prose | pages [14] -->
Step 3: Consider the same edge in Step 2. If no directed edge exists between vi and vj in graph G,

<!-- b000365 | prose | pages [14] -->
then the similarity value Sij is a possible value of the random variable S2;

<!-- b000366 | prose | pages [14] -->
Step 4: Repeat Step 2 and Step 3 until all the undirected edges in graph G1 have been traversed;

<!-- b000367 | prose | pages [14] -->
Step 5: Compute the distributions of random variables S1 and S2.

<!-- b000368 | prose | pages [14] -->
The visualization of distributions of the two random variables are displayed in Fig. 9.

<!-- b000369 | caption | pages [14] -->
Fig. 9. The distributions of S1 and S2. The light orange and orange curves denote the distribution

<!-- b000370 | prose | pages [14] -->
when there is no inﬂuence between to artists. The light blue and blue curves denote the distribution when two artists are unilaterally or mutually inﬂuence by each other.

<!-- b000371 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000372 | furniture | pages [14] -->
关注数学模型

<!-- b000373 | furniture | pages [14] -->
2

<!-- b000374 | furniture | pages [14] -->
MATHmodels

<!-- b000375 | furniture | pages [14] -->
获取更多资讯

<!-- b000376 | furniture | pages [15] -->
Team # 2124497

<!-- b000377 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000378 | furniture | pages [15] -->
Page 14 of 22

<!-- b000379 | prose | pages [15] -->
The GaussianﬁttingresultforthedistributionofS1 andS2 are N(0.830, 0.067)andN(0.781, 0.076), respectively. The Bayes error rate is 0.6452. The overall similarity between the artists who uni- laterally or mutually inﬂuenced one another is signiﬁcantly larger than similarity of artists that did

<!-- b000380 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000381 | prose | pages [15] -->
not inﬂuence each other. The result demonstrates that the similarity of artists who have a inﬂuence relationship is in fact larger than the artists who do not. That is to say, the identiﬁed inﬂuencers indeed inﬂuence the respective followers from a statistical perspective.

<!-- b000382 | prose | pages [15] -->
4.3 The Roles of Characteristics

<!-- b000383 | prose | pages [15] -->
When measuring the music similarity, we have combined the information of 13 musical char- acteristics to form the quantiﬁcation. However, what remains unknown is the roles that diﬀerent musical characteristics plays in inﬂuencing the music. In other words, we wish to identify the one or several characteristics that are signiﬁcant in distinguishing the genres. We also analyze which characteristics indicate the more general inherent features among artists. In this section, we ﬁrst deﬁne the central node in each genre. Then we eliminate the characteristics one at a time or one by one, and conduct the non-parametric test to identify the roles of characteristics.

<!-- b000384 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000385 | prose | pages [15] -->
4.3.1 Characteristics that Distinguish Genres

<!-- b000386 | prose | pages [15] -->
Due to the lack of synthesized data for each genre, we ﬁrst synthesize the information about musical characteristics by deﬁning the central nodes. Then the Kruskal-Wallis test is utilized to identify the most inﬂuential characteristics that distinguish genres.

<!-- b000387 | prose | pages [15] -->
The Central Nodes of Each Genre:

<!-- b000388 | prose | pages [15] -->
We assume that each node in one genre is accounted for a certain percentage when deciding the central node of this genre. The percentage of node vj is denoted as Pj, formulated in Eq. (9).

<!-- b000389 | prose | pages [15] -->
P

<!-- b000390 | prose | pages [15] -->
Pj =

<!-- b000391 | prose | pages [15] -->
k∈Fj IjkSjk

<!-- b000392 | prose | pages [15] -->
(9)

<!-- b000393 | prose | pages [15] -->
Oj

<!-- b000394 | prose | pages [15] -->
where Fj is the set of labels of artists that follow artist vj. Ijk and Sjk denote the inﬂuence and similarity between vj and vk, respectively.

<!-- b000395 | prose | pages [15] -->
Let Ri be the set of labels of nodes that belong to the ith genre, where i = 1, 2, ...19. Let Chi represent the 13 musical characteristics of the central node of the ith genre, then Chi is deﬁned in Eq. (10).

<!-- b000396 | prose | pages [15] -->
P

<!-- b000397 | prose | pages [15] -->
Chi =

<!-- b000398 | prose | pages [15] -->
j∈Ri Pj · Cj

<!-- b000399 | prose | pages [15] -->
(10)

<!-- b000400 | prose | pages [15] -->
P

<!-- b000401 | prose | pages [15] -->
j∈Ri Pj

<!-- b000402 | prose | pages [15] -->
where Cj is the vector of 13 musical characteristics of node vj.

<!-- b000403 | prose | pages [15] -->
We can then obtain the 13 musical characteristics of central nodes of each genre by using Eq. (10).

<!-- b000404 | prose | pages [15] -->
The Most Inﬂuential Characteristics:

<!-- b000405 | prose | pages [15] -->
Let M1 be the 19 × 13 matrix, where each row stores the vector of 13 musical characteristics

<!-- b000406 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000407 | furniture | pages [15] -->
关注数学模型

<!-- b000408 | furniture | pages [15] -->
2

<!-- b000409 | furniture | pages [15] -->
MATHmodels

<!-- b000410 | furniture | pages [15] -->
获取更多资讯

<!-- b000411 | furniture | pages [16] -->
Team # 2124497

<!-- b000412 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000413 | furniture | pages [16] -->
Page 15 of 22

<!-- b000414 | prose | pages [16] -->
of the central node of each genre. M1 is formulated in Eq. (11).

<!-- b000415 | prose | pages [16] -->
 

<!-- b000416 | prose | pages [16] -->


<!-- b000417 | prose | pages [16] -->
Ch1 Ch2

<!-- b000418 | prose | pages [16] -->
 

<!-- b000419 | prose | pages [16] -->


<!-- b000420 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000421 | prose | pages [16] -->
M1 =

<!-- b000422 | prose | pages [16] -->
(11)

<!-- b000423 | prose | pages [16] -->
... Ch19

<!-- b000424 | prose | pages [16] -->
where Chi represents the 13 musical characteristics of the central node of the ith genre.

<!-- b000425 | prose | pages [16] -->
The uniformed values of matrix M1 is visualized in Fig. 10. For each column in Fig. 10, the corresponding characteristics has a great inﬂuence in distinguishing genres if the colors of each cube demonstrates a greater variability. We could roughly observe that the values of characteristics of Energy, Valence, Speechiness varies to a large extent, while values of Acousticness, Instrumen- talness have relatively concentrated distribution. We will test the rough conclusion by conducting Kruskal-Wallis test on these 5 characteristics in the following part.

<!-- b000426 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000427 | caption | pages [16] -->
Fig. 10. The values of musical characteristics of the central nodes in each genre.

<!-- b000428 | prose | pages [16] -->
The Kruskal-Wallis test is a non-parametric test that can assess the the signiﬁcant diﬀerences by two or more groups of variables [4]. The null hypothesis H0 and the alternative hypothesis H1 are deﬁned. The null hypothesis represents no eﬀect or no diﬀerence, while the alternative hypothesis denotes the presence of an eﬀect or a diﬀerence [5]. A p−value is the probability that assumes H0 is true. Namely, the smaller the p-value, the strong the evidence evidence against the null hypothesis.

<!-- b000429 | prose | pages [16] -->
By the most inﬂuential characteristics, we mean that theses characteristics play important roles in distinguishing the genres. In other words, the similarity between genres will signiﬁcantly increase once theses characteristics are removed from matrix M1. Therefore, we removed each one of the 13 columns in M1, and calculate the respective p-value before and after the elimination. The Kruskal-Wallis test is applied in calculating the p-value. The typical p-values calculated are presented in Table 2.

<!-- b000430 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000431 | furniture | pages [16] -->
关注数学模型

<!-- b000432 | furniture | pages [16] -->
2

<!-- b000433 | furniture | pages [16] -->
MATHmodels

<!-- b000434 | furniture | pages [16] -->
获取更多资讯

<!-- b000435 | furniture | pages [17] -->
Team # 2124497

<!-- b000436 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000437 | furniture | pages [17] -->
Page 16 of 22

<!-- b000438 | caption | pages [17] -->
Table 2: The typical p-values when removing one of the characteristics

<!-- b000439 | prose | pages [17] -->
Valence The removed characteristics Energy Speechiness Acousticness Instrumentalness

<!-- b000440 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000441 | prose | pages [17] -->
p-value before elimination 0.1284 0.1284

<!-- b000442 | prose | pages [17] -->
p-value after elimination 0.6500 0.5319

<!-- b000443 | prose | pages [17] -->
0.1284 0.1284 0.1284

<!-- b000444 | prose | pages [17] -->
0.3057 0.0086 0.0035

<!-- b000445 | prose | pages [17] -->
* The p-values in the second row denote the non-parametric results before elimination. The p-values in the third row is the result after the characteristics of this column has been eliminated.

<!-- b000446 | prose | pages [17] -->
From Table 2, the result shows that after eliminating Energy, Valence and Speechiness, the p-value increases signiﬁcantly, meaning that the similarity distributions of each genre become less diﬀerent after the elimination. Therefore, Energy, Valence, Speechiness are inﬂuential character- istics in distinguishing genres. The experiment result analysis is similar for other characteristics. On the other hand, the p-values become extremely small after eliminating Acousticness and Instru- mentalness, meaning that these two characteristics are distributed similarly among genres. We can

<!-- b000447 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000448 | prose | pages [17] -->
conclude that Energy, Valence and Speechiness are the relatively inﬂuential characteristics, while Energy is even more inﬂuential than other inﬂuential characteristics.

<!-- b000449 | prose | pages [17] -->
The Contagious Characteristics among Artists 4.3.2

<!-- b000450 | prose | pages [17] -->
In the last section, we discussed how inﬂuential the characteristics are when distinguishing the genres. In this section, we aim at discovering how Contagious the characteristics are when deciding the musical style of various artists.

<!-- b000451 | prose | pages [17] -->
The Selected Artists:

<!-- b000452 | prose | pages [17] -->
Since there are in total 5854 artists in the data_by_artists data set, it is neither practical nor necessary to perform the Kruskal-Wallis test among all the available artists. Therefore, we selected the top 25 artists who have the highest Pj value (who accounted for more percentage when deciding the central nodes) introduced in Section 4.3.1. Let M1 be the 25 × 13 matrix, where each row stores the vector of 13 musical characteristics of the central node of each genre. M1 is formulated in Eq. (11).

<!-- b000453 | prose | pages [17] -->
M2 =

<!-- b000454 | prose | pages [17] -->
 

<!-- b000455 | prose | pages [17] -->


<!-- b000456 | prose | pages [17] -->
Ch1 Ch2

<!-- b000457 | prose | pages [17] -->
 

<!-- b000458 | prose | pages [17] -->
 (12)

<!-- b000459 | prose | pages [17] -->
... Ch25

<!-- b000460 | prose | pages [17] -->
where Chi represents the 13 musical characteristics of the central node of the ith artists.

<!-- b000461 | prose | pages [17] -->
The Most Contagious Characteristics:

<!-- b000462 | prose | pages [17] -->
Diﬀerent from the level of characteristics inﬂuence in Section 4.3.1, we deﬁne the characteristics to be Contagious when they represent the common inherent features of artists’ musical styles. Following the idea of non-parametric test in Section 4.3.1, the Kruskal-Wallis test can also be used here to measure the level Contagious. The adapted method is illustrated as follows:

<!-- b000463 | prose | pages [17] -->
Step 1: For the 13 musical characteristics, calculate the corresponding 13 p-values. Each p-value

<!-- b000464 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000465 | furniture | pages [17] -->
关注数学模型

<!-- b000466 | furniture | pages [17] -->
2

<!-- b000467 | furniture | pages [17] -->
MATHmodels

<!-- b000468 | furniture | pages [17] -->
获取更多资讯

<!-- b000469 | furniture | pages [18] -->
Team # 2124497

<!-- b000470 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000471 | furniture | pages [18] -->
Page 17 of 22

<!-- b000472 | prose | pages [18] -->
is obtained by conducting Kruskal-Wallis test when the certain one out of 13 characteristics is temporally removed;

<!-- b000473 | prose | pages [18] -->
Step 2: Pick out the smallest p-value in step one and eliminate the respective characteristics per-

<!-- b000474 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000475 | prose | pages [18] -->
manently from M2. Name the characteristics as the most contagious characteristics;

<!-- b000476 | prose | pages [18] -->
Step 3: For the rest 12 characteristics, repeat the process in Step 1 and Step2. The characteristics that

<!-- b000477 | prose | pages [18] -->
was picked out and eliminated is named as the the second most contagious characteristics;

<!-- b000478 | prose | pages [18] -->
Step 4: Repeat the process described from Step 1 to Step 3, until all the 13 characteristics have

<!-- b000479 | prose | pages [18] -->
been sorted with an order.

<!-- b000480 | prose | pages [18] -->
Due to the limited length of the article, we will only demonstrate the 4 most contagious characteristics calculated from the above steps. Moreover, among the 25 artists we chose, their characteristics Mode all possess the value 1. Since Mode is apparently the same for all the selected artists, it can be deemed as the most contagious characteristics. Table 3 listed the p-values of the

<!-- b000481 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000482 | prose | pages [18] -->
other 3 most contagious characteristics before and after they are eliminated.

<!-- b000483 | caption | pages [18] -->
Table 3: The p-values when removing the 4 most contagious characteristics

<!-- b000484 | prose | pages [18] -->
Acousticness The removed characteristics

<!-- b000485 | prose | pages [18] -->
p-value before elimination 0.7786

<!-- b000486 | prose | pages [18] -->
p-value after elimination 0.2631

<!-- b000487 | prose | pages [18] -->
Danceability Valence

<!-- b000488 | prose | pages [18] -->
0.2631 0.0326

<!-- b000489 | prose | pages [18] -->
0.0326 0.0205

<!-- b000490 | prose | pages [18] -->
* The p-values in the second row denote the non-parametric results before elimination of the characteristics of the corresponding column, while the third row denotes results after elimination.

<!-- b000491 | prose | pages [18] -->
From Table 3, we can draw a conclusion that Mode, Acousticness, Danceability and Valence are the most contagious characteristics among artists, while the Mode and Acousticness have the highest and the second highest level of contagiousness. The Danceability and Valence are the third and fourth most contagious characteristics, respectively. Since the smaller p-values represent larger signiﬁcant diﬀerence, our experiment results are valid because: the elimination of our discovered contagious characteristics will lead to signiﬁcant reduction of the p-value, indicating that characteristics have more concentrated distribution after the contagious characteristics are removed. The results is in correspondence with our deﬁnition of contagiousness.

<!-- b000492 | prose | pages [18] -->
Revolutionary Artists Based on Closeness Centrality 4.4

<!-- b000493 | prose | pages [18] -->
By revolutionary artists, we generally mean that their contribution to the ﬁeld should be signiﬁcant. Moreover, they ought to have great impact on others while receiving small inﬂuence from others. Inspired by the structure of the inﬂuence network G constructed in Section 4.1, we apply the evaluation of important nodes in discovering the revolutionary artists. To be more speciﬁc, we combine the in-closeness and out-closeness centrality to evaluate the signiﬁcance of an artists in revolutionaries. Our goal is to discover the artists with small in-closeness centrality and large out-closeness centrality.

<!-- b000494 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000495 | furniture | pages [18] -->
关注数学模型

<!-- b000496 | furniture | pages [18] -->
2

<!-- b000497 | furniture | pages [18] -->
MATHmodels

<!-- b000498 | furniture | pages [18] -->
获取更多资讯

<!-- b000499 | furniture | pages [19] -->
Team # 2124497

<!-- b000500 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000501 | furniture | pages [19] -->
Page 18 of 22

<!-- b000502 | prose | pages [19] -->
For the inﬂuence network G(V, E), the closeness centrality CC(i) of node vi is the average farness to all the other nodes in the network, formulated in Eq. (13).

<!-- b000503 | prose | pages [19] -->
n −1

<!-- b000504 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000505 | prose | pages [19] -->
CC(i) =

<!-- b000506 | prose | pages [19] -->
where n is the number of nodes in graph G.

<!-- b000507 | prose | pages [19] -->
(13)

<!-- b000508 | prose | pages [19] -->
P P

<!-- b000509 | prose | pages [19] -->
j̸=i d(i, j)

<!-- b000510 | prose | pages [19] -->
Since closeness is a directional measure in the directed graph, the in-closeness centrality CCi(i) and the out-closeness centrality CCo(i) can be calculated accordingly. To evaluate the inﬂuence of the evolutionary artists who have large out-closeness centrality and small in-closeness centrality, the synthesized closeness centrality of artist vi is deﬁned in Eq. (14).

<!-- b000511 | prose | pages [19] -->
C(i) = CCo(i) −CCi(i) (14)

<!-- b000512 | prose | pages [19] -->
The synthesized closeness centrality of the top 12 artists are shown in Fig. 11.

<!-- b000513 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000514 | caption | pages [19] -->
Fig. 11. The synthesized closeness centrality of the top 12 artists

<!-- b000515 | prose | pages [19] -->
The basic information of top 12 evolutionary artists are listed in Table 4.

<!-- b000516 | prose | pages [19] -->
Reader can easily ﬁnd our results reliable according the name of these 12 artist. For instance, Dylan was awarded the Nobel Prize in Literature in 2016, Chuck Berry is one of the pioneers of Rock and Roll music, and The Beatles is regarded as the most inﬂuential band of all time.

<!-- b000517 | prose | pages [19] -->
4.5 Dynamic Process of Evolution

<!-- b000518 | prose | pages [19] -->
From data_by_year data set, we have known the evolution trend of the musical characteristics over time. Though the general trend is easy to observe by visualizing the data, deeper information

<!-- b000519 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000520 | furniture | pages [19] -->
关注数学模型

<!-- b000521 | furniture | pages [19] -->
2

<!-- b000522 | furniture | pages [19] -->
MATHmodels

<!-- b000523 | furniture | pages [19] -->
获取更多资讯

<!-- b000524 | furniture | pages [20] -->
Team # 2124497

<!-- b000525 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000526 | furniture | pages [20] -->
Page 19 of 22

<!-- b000527 | caption | pages [20] -->
Table 4: The basic information of top 12 evolutionary artists

<!-- b000528 | prose | pages [20] -->
Artist ID Name Centrality Artist ID Name Centrality

<!-- b000529 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000530 | prose | pages [20] -->
120521 Chuck Berry 0.2921

<!-- b000531 | prose | pages [20] -->
824022 Little Richard 0.2904

<!-- b000532 | prose | pages [20] -->
66915 Bob Dylan 0.2838

<!-- b000533 | prose | pages [20] -->
79016 Billie Holiday 0.2806

<!-- b000534 | prose | pages [20] -->
608701 Muddy Waters 0.2801

<!-- b000535 | prose | pages [20] -->
46861 Ray Charles 0.2783

<!-- b000536 | prose | pages [20] -->
287604 Louis Jordan 0.2777

<!-- b000537 | prose | pages [20] -->
269972 Little Willie John 0.2731

<!-- b000538 | prose | pages [20] -->
549797 Hank Williams 0.2730

<!-- b000539 | prose | pages [20] -->
317093 Nat King Cole 0.2729

<!-- b000540 | prose | pages [20] -->
754032 The Beatles 0.2708

<!-- b000541 | prose | pages [20] -->
238115 Sam Cooke 0.2702

<!-- b000542 | prose | pages [20] -->
* From left to right, top to bottom, the 12 artists are sorted according to their synthesized centrality.

<!-- b000543 | prose | pages [20] -->
could still be discovered. We are then motivated to analyze the frequency components of time series of each musical characteristics.

<!-- b000544 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000545 | prose | pages [20] -->
Discrete Fourier transform (DFT) could transform a sequence of samples with a ﬁnite length into a equally-spaced samples discrete-time Fourier transform with the same length [7]. Let x[n] denote a time series. The DFT X[k] of the series x[n] is formulated in Eq. (15).

<!-- b000546 | prose | pages [20] -->
N−1

<!-- b000547 | prose | pages [20] -->
x[n]e−j 2π

<!-- b000548 | prose | pages [20] -->
X

<!-- b000549 | prose | pages [20] -->
N kn,

<!-- b000550 | prose | pages [20] -->
X[k] =

<!-- b000551 | prose | pages [20] -->
n=0

<!-- b000552 | prose | pages [20] -->
where N is the length of series x[n].

<!-- b000553 | prose | pages [20] -->
k = 0, 1, 2, ..., N −1 (15)

<!-- b000554 | prose | pages [20] -->
An indicator σ is developed in Eq. (16), which measures the proportion of low-frequency components in the time series x[n].

<!-- b000555 | prose | pages [20] -->
σ = 2 P4

<!-- b000556 | prose | pages [20] -->
m=1 |X[m]|2 PN−1

<!-- b000557 | prose | pages [20] -->
(16) m=0 |X[m]|2

<!-- b000558 | prose | pages [20] -->
PN−1

<!-- b000559 | prose | pages [20] -->
m=0 |X[m]|2

<!-- b000560 | prose | pages [20] -->
is the energy of series x[n]. It should be noted that FFT

<!-- b000561 | prose | pages [20] -->
where N is the length of x[n],

<!-- b000562 | prose | pages [20] -->
N (fast Fourier transform) is used instead of DFT when computing DFT by computers.

<!-- b000563 | prose | pages [20] -->
Eq. (16) is reasonable because |X[0]| = 0 (the DC component) according to data preprocessing, x[n]−¯x[n] x[n]max−¯x[n]. ¯x[n] and x[n]max denote the average and maximum value of series x[n], where ˆx[n] = respectively.

<!-- b000564 | prose | pages [20] -->
For computers, we apply IFFT (inverse fast Fourier transform) to the four low-frequency components illustrated in Eq. (16). The time series x[n] is the data of Acousticness from 1955 to 2014 of the genre Pop & Rock. N = 60 is the length of x[n]. The results of FFT are shown in Fig. 12.

<!-- b000565 | prose | pages [20] -->
From Fig. 12, we can observe that the time series reconstructed from the low-frequency com- ponents can well represent the overall trend of the original time series. The result also indicates the the low-frequency components takes up more percentage in the time series of Acousticness of the genre Pop & Rock

<!-- b000566 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000567 | furniture | pages [20] -->
关注数学模型

<!-- b000568 | furniture | pages [20] -->
2

<!-- b000569 | furniture | pages [20] -->
MATHmodels

<!-- b000570 | furniture | pages [20] -->
获取更多资讯

<!-- b000571 | furniture | pages [21] -->
Team # 2124497

<!-- b000572 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000573 | furniture | pages [21] -->
Page 20 of 22

<!-- b000574 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000575 | prose | pages [21] -->
(a) Amplitude of the FFT result (b) Phase of the FFT result

<!-- b000576 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000577 | prose | pages [21] -->
(c) The original time series (d) The IFFT of low-frequency components of the original seires

<!-- b000578 | caption | pages [21] -->
Fig. 12. The process of reserving the low-frequency components of x[n]

<!-- b000579 | prose | pages [21] -->
We calculate σ for other typical characteristics of the genre Pop & Rock. The result is listed in

<!-- b000580 | caption | pages [21] -->
Table 5.

<!-- b000581 | caption | pages [21] -->
Table 5: The σ values in for the time series of three typical characteristics

<!-- b000582 | prose | pages [21] -->
Energy Characteristics

<!-- b000583 | prose | pages [21] -->
σ 0.7895

<!-- b000584 | prose | pages [21] -->
Popularity Liveness

<!-- b000585 | prose | pages [21] -->
0.8481 0.4936

<!-- b000586 | prose | pages [21] -->
The results indicate that Energy and Popularity have larger proportion of low-frequency com- ponents, and have a smoother revolution over time. Meanwhile, Liveness has more high-frequency components. The dynamic process of evolution for other characteristics can be computed and analyzed in the exact same way.

<!-- b000587 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000588 | furniture | pages [21] -->
关注数学模型

<!-- b000589 | furniture | pages [21] -->
2

<!-- b000590 | furniture | pages [21] -->
MATHmodels

<!-- b000591 | furniture | pages [21] -->
获取更多资讯

<!-- b000592 | furniture | pages [22] -->
Team # 2124497

<!-- b000593 | prose | pages [22] -->
5

<!-- b000594 | heading | pages [22] -->
Test the Model

<!-- b000595 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000596 | furniture | pages [22] -->
Page 21 of 22

<!-- b000597 | prose | pages [22] -->
In Section 4.3.1 we introduced the deﬁnition of Central node in each genre. Therefore, we will test the eﬀectiveness of our Central node model in this section.

<!-- b000598 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000599 | prose | pages [22] -->
The within-genre similarity distribution of Country is given in Section 4.2.2, while the Gaussian ﬁtting result is N(0.85, 0.06). Diﬀerent from the similarity distribution deﬁned previously (where similarity denotes the similarity between every two nodes in the certain genre), we re-deﬁne the distribution of similarity values between the central node and other nodes within Country.

<!-- b000600 | prose | pages [22] -->
From the deﬁnition of central nodes, we can have an intuitive understanding that the overall similarity will become smaller after the re-deﬁnition, because the central node is likely to locate at the "center" of the genre. The new similarity distribution within Country is shown in Fig. 13.

<!-- b000601 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000602 | caption | pages [22] -->
Fig. 13. The new similarity distribution.

<!-- b000603 | prose | pages [22] -->
The Gaussian ﬁtting result for the new distribution is N(0.45, 0.04). Compared with the original distribution (which is N(0.85, 0.06)), the expectation value of similarity is signiﬁcantly reduced, meaning that our proposed model of central nodes is valid.

<!-- b000604 | prose | pages [22] -->
6

<!-- b000605 | heading | pages [22] -->
Strengths and Weaknesses

<!-- b000606 | prose | pages [22] -->
6.1

<!-- b000607 | heading | pages [22] -->
Strengths

<!-- b000608 | prose | pages [22] -->
1. For the measurement of inﬂuence, we have considered comprehensive aspects with the provided information in the inﬂuence relationship;

<!-- b000609 | prose | pages [22] -->
2. The MRDE framework we proposed for similarity measurement can well retain information of high-dimensional data;

<!-- b000610 | prose | pages [22] -->
3. Closeness centrality is used to detect the revolutionary artists. The idea of this method is tested to be eﬀective by comparing the results with real-life information of corresponding

<!-- b000611 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000612 | furniture | pages [22] -->
关注数学模型

<!-- b000613 | furniture | pages [22] -->
2

<!-- b000614 | furniture | pages [22] -->
MATHmodels

<!-- b000615 | furniture | pages [22] -->
获取更多资讯

<!-- b000616 | furniture | pages [23] -->
Team # 2124497

<!-- b000617 | prose | pages [23] -->
artists.

<!-- b000618 | prose | pages [23] -->
6.2

<!-- b000619 | heading | pages [23] -->
Weaknesses

<!-- b000620 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000621 | furniture | pages [23] -->
Page 22 of 22

<!-- b000622 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000623 | prose | pages [23] -->
1. The aggregation we used in the MRDE framework is not accurate enough for deﬁning the actual similarity value from the distribution;

<!-- b000624 | prose | pages [23] -->
2. When we introduced the method for time series analysis, more state-of-the-art mechanism can be utilized.

<!-- b000625 | prose | pages [23] -->
7

<!-- b000626 | heading | pages [23] -->
Conclusion

<!-- b000627 | prose | pages [23] -->
In this paper, we proposed a detailed model in order to analyze the music objectively. The measurement of inﬂuence and quantiﬁcation of similarity is proposed.

<!-- b000628 | prose | pages [23] -->
Kruskal-Wallis test is performed to identify the inﬂuential characteristics in distinguishing genres, and the contagious nodes are detected using the similar method.

<!-- b000629 | prose | pages [23] -->
Moreover, careful analyses of dynamic process

<!-- b000630 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000631 | prose | pages [23] -->
evolution are done by transforming the characteristics’ time series by discrete Fourier transform.

<!-- b000632 | prose | pages [23] -->
In the future, more state-of-the-art techniques could be utilized to analyze the evolution process. For example, the long short term memory (LSTM) framework to predict the time series, providing insight into the possible future trend of music evolution. Meanwhile, the external inﬂuence on the evolution of music could be examined or even quantiﬁed by calculating the correlation value (the Pearson correlation for instance) between the given the time series of external factors and a certain characteristics.

<!-- b000633 | heading | pages [23] -->
References

<!-- b000634 | references | pages [23] -->
[1] Ma, H., Leng, S., Aihara, K., Lin, W., & Chen, L. (2018). Randomly distributed embedding

<!-- b000635 | references | pages [23] -->
making short-term high-dimensional data predictable. Proceedings of the National Academy

<!-- b000636 | references | pages [23] -->
of Sciences, 115(43), E9994-E10002.

<!-- b000637 | references | pages [23] -->
[2] Yuille, A. L., & Bülthoﬀ, H. H. (1993). Bayesian decision theory and psychophysics.

<!-- b000638 | references | pages [23] -->
[3] Tumer, K., & Ghosh, J. (1996, August). Estimating the Bayes error rate through classiﬁer

<!-- b000639 | references | pages [23] -->
combining. In Proceedings of 13th international conference on pattern recognition (Vol. 2,

<!-- b000640 | references | pages [23] -->
pp. 695-699). IEEE.

<!-- b000641 | references | pages [23] -->
[4] McKight, P. E., & Najab, J. (2010). Kruskal-wallis test. The corsini encyclopedia of psychol-

<!-- b000642 | references | pages [23] -->
ogy, 1-1.

<!-- b000643 | references | pages [23] -->
[5] Hamill, T. M. (1999). Hypothesis tests for evaluating numerical precipitation forecasts.

<!-- b000644 | references | pages [23] -->
Weather and Forecasting, 14(2), 155-167.

<!-- b000645 | references | pages [23] -->
[6] Valente, T. W., Coronges, K., Lakon, C., & Costenbader, E. (2008). How correlated are

<!-- b000646 | references | pages [23] -->
network centrality measures?. Connections (Toronto, Ont.), 28(1), 16.

<!-- b000647 | references | pages [23] -->
[7] Winograd, S. (1978). On computing the discrete Fourier transform. Mathematics of compu-

<!-- b000648 | references | pages [23] -->
tation, 32(141), 175-199.

<!-- b000649 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000650 | furniture | pages [23] -->
关注数学模型

<!-- b000651 | furniture | pages [23] -->
2

<!-- b000652 | furniture | pages [23] -->
MATHmodels

<!-- b000653 | furniture | pages [23] -->
获取更多资讯

<!-- b000654 | furniture | pages [24] -->


<!-- b000655 | furniture | pages [24] -->
Team # 2124497

<!-- b000656 | furniture | pages [24] -->


<!-- b000657 | furniture | pages [24] -->


<!-- b000658 | furniture | pages [24] -->


<!-- b000659 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000660 | references | pages [24] -->
Feb 9th , 2021

<!-- b000661 | references | pages [24] -->
A Valuable Work to Analyze the Influence of Music

<!-- b000662 | references | pages [24] -->
微信公众号：数学模型

<!-- b000663 | references | pages [24] -->
Understanding the influence

<!-- b000664 | references | pages [24] -->
K E Y W O R D S :

<!-- b000665 | references | pages [24] -->
of music is a skill that

<!-- b000666 | references | pages [24] -->
humans have always

<!-- b000667 | references | pages [24] -->
wanted to possess. Whether

<!-- b000668 | references | pages [24] -->
Complex Network

<!-- b000669 | references | pages [24] -->
to explore the influence

<!-- b000670 | references | pages [24] -->
relationship between

<!-- b000671 | references | pages [24] -->
musicians or study the

<!-- b000672 | references | pages [24] -->
微信号：MATHmodels

<!-- b000673 | references | pages [24] -->
Bayes Error Rate

<!-- b000674 | references | pages [24] -->
music similarity, the models

<!-- b000675 | references | pages [24] -->
and methods of complex

<!-- b000676 | references | pages [24] -->
network analysis are always

<!-- b000677 | references | pages [24] -->
Closeness Centrality

<!-- b000678 | references | pages [24] -->
valuable. By connecting

<!-- b000679 | references | pages [24] -->
influencers and followers

<!-- b000680 | references | pages [24] -->
and assigning weights to the

<!-- b000681 | references | pages [24] -->
Kruskal-Wallis Test

<!-- b000682 | references | pages [24] -->
corresponding edges, a

<!-- b000683 | references | pages [24] -->
directed influence network

<!-- b000684 | references | pages [24] -->
among artists can be

<!-- b000685 | references | pages [24] -->
Discrete Fourier Transform

<!-- b000686 | references | pages [24] -->
established. Our work

<!-- b000687 | references | pages [24] -->
analyzes this network in

<!-- b000688 | references | pages [24] -->
detail, and obtains the

<!-- b000689 | references | pages [24] -->
quantified influence values.

<!-- b000690 | references | pages [24] -->
At the same time, the

<!-- b000691 | references | pages [24] -->
similarity distribution within

<!-- b000692 | references | pages [24] -->
and between genres of is

<!-- b000693 | references | pages [24] -->
also analyzed.  The results

<!-- b000694 | references | pages [24] -->
show that the similarity

<!-- b000695 | references | pages [24] -->
within genres is generally

<!-- b000696 | references | pages [24] -->
larger than that between-

<!-- b000697 | references | pages [24] -->
genre similarity.  We

<!-- b000698 | references | pages [24] -->
obtained the representative

<!-- b000699 | references | pages [24] -->
vector of each genre that

<!-- b000700 | references | pages [24] -->
synthesized the music

<!-- b000701 | references | pages [24] -->
characteristics. The

<!-- b000702 | references | pages [24] -->
synthesized data has been

<!-- b000703 | references | pages [24] -->
tested to be indeed

<!-- b000704 | references | pages [24] -->
representative.  Based on

<!-- b000705 | references | pages [24] -->
the synthesized result, we

<!-- b000706 | references | pages [24] -->
detected the main

<!-- b000707 | references | pages [24] -->
differentiating factors

<!-- b000708 | references | pages [24] -->
between different genres.

<!-- b000709 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000710 | references | pages [24] -->
However, due to the

<!-- b000711 | references | pages [24] -->
limited data, our analysis

<!-- b000712 | references | pages [24] -->
of certain types of music

<!-- b000713 | references | pages [24] -->
may not be sufficient.

<!-- b000714 | references | pages [24] -->
With more data, we can

<!-- b000715 | references | pages [24] -->
In fact, based on these

<!-- b000716 | references | pages [24] -->
have more effective

<!-- b000717 | references | pages [24] -->
data, we have also

<!-- b000718 | references | pages [24] -->
information in the

<!-- b000719 | references | pages [24] -->
analyzed results other

<!-- b000720 | references | pages [24] -->
network analysis.  Since

<!-- b000721 | references | pages [24] -->
than similarity and

<!-- b000722 | references | pages [24] -->
our model mainly use the

<!-- b000723 | references | pages [24] -->
influence.  For

<!-- b000724 | references | pages [24] -->
matrix-based linear

<!-- b000725 | references | pages [24] -->
example, we can

<!-- b000726 | references | pages [24] -->
calculation, the

<!-- b000727 | references | pages [24] -->
analyze the

<!-- b000728 | references | pages [24] -->
increased number of

<!-- b000729 | references | pages [24] -->
revolutionary

<!-- b000730 | references | pages [24] -->
data will not significantly

<!-- b000731 | references | pages [24] -->
musicians by finding

<!-- b000732 | references | pages [24] -->
increase the

<!-- b000733 | references | pages [24] -->
the important nodes by

<!-- b000734 | references | pages [24] -->
computational

<!-- b000735 | references | pages [24] -->
closeness centrality in

<!-- b000736 | references | pages [24] -->
complexity.  In addition,

<!-- b000737 | references | pages [24] -->
the network. We have

<!-- b000738 | references | pages [24] -->
when there is a larger

<!-- b000739 | references | pages [24] -->
also established a

<!-- b000740 | references | pages [24] -->
order of magnitude of

<!-- b000741 | references | pages [24] -->
model for analyzing

<!-- b000742 | references | pages [24] -->
data, our model still

<!-- b000743 | references | pages [24] -->
dynamic influence

<!-- b000744 | references | pages [24] -->
retains computational

<!-- b000745 | references | pages [24] -->
indicators, and

<!-- b000746 | references | pages [24] -->
advantages.  For

<!-- b000747 | references | pages [24] -->
correspondingly, we

<!-- b000748 | references | pages [24] -->
example, the proposed

<!-- b000749 | references | pages [24] -->
have analyzed the

<!-- b000750 | references | pages [24] -->
MRDE framework can

<!-- b000751 | references | pages [24] -->
dynamic process of the

<!-- b000752 | references | pages [24] -->
take random tuple

<!-- b000753 | references | pages [24] -->
evolution for different

<!-- b000754 | references | pages [24] -->
selection to obtain the

<!-- b000755 | references | pages [24] -->
genres of music in the

<!-- b000756 | references | pages [24] -->
same effective similarity

<!-- b000757 | references | pages [24] -->
past 100 years.

<!-- b000758 | references | pages [24] -->
distribution.

<!-- b000759 | furniture | pages [24] -->
关注数学模型

<!-- b000760 | furniture | pages [24] -->
2

<!-- b000761 | furniture | pages [24] -->
MATHmodels

<!-- b000762 | furniture | pages [24] -->
获取更多资讯
