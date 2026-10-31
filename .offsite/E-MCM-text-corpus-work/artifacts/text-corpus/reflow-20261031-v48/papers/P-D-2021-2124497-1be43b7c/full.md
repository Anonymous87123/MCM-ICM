# P-D-2021-2124497-1be43b7c

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen 2021 Team Control Number MCM/ICM D 2124497 Summary Sheet

<!-- b000002 | title | pages [1] -->
How to analyze the music objectively?

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
Music is a form of art that profoundly influences humans and societies. Given the four data sets, we are motivated to develop a series of objective measurements to analyze the music from four perspectives.

<!-- b000005 | prose | pages [1] -->
First of all, the measurement of music influence between artists is given by the combination of three indicators: 1) the indicator related to artists active in one certain decade being followed by artists active in other decades, 2) the indicator related to artists of one certain genre being followed by artists of other genres, and 3) the out-degree of the influencers. A weighted directed graph G(V, E) is constructed to represent the influence network, where an edge is directed from the influencer to the follower. Therefore, the calculated influence between the two artists is the weight of a directed edge.

<!-- b000006 | furniture | pages [1] -->
O

<!-- b000007 | prose | pages [1] -->
Secondly, the music similarity is quantified. Since the provided data sets full_music_data contains high-dimensional data, thus the dimension reduction is needed. We are motivated to use the modified randomly distributed embedding (RDE) framework to take good advantage of interaction information of high-dimensional data. Moreover, the Bayes error rate is used to identify whether the distributions of within-genre and between-genre are significantly different.

<!-- b000008 | prose | pages [1] -->
Thirdly, we analyzed two kinds of roles of musical characteristics by examining the p-values from Kruskal-Wallis test. We removed each characteristic one at a time, and compared the p-values before and after the certain characteristics is removed. From the experiment results, the most influential characteristics in distinguishing genres are Energy, Valence, and Speechiness. The most contagious characteristics among artists are Acousticness, Danceability, and Valence.

<!-- b000009 | prose | pages [1] -->
Finally, we detected the most revolutionary artists by detecting the important nodes in the influence network using the modified closeness centrality (the synthesized centrality of in-closeness and out-closeness centrality). The calculated top 12 evolutionary artists are listed, including Bob Dylan, Chuck Berry, The Beatles, etc. In addition, the dynamic process of evolution is analyzed. By conducting discrete Fourier transform (DFT) and detecting the time series which is reconstructed from low-frequency components, we can observe the low-frequency components in a musical characteristic over time. An indicator σ is proposed to measure the proportion of low-frequency components among all the frequency components. Energy and Popularity have large σ values according to the experiment, meaning that there are rich low-frequency components in the time series of these two characteristics.

<!-- b000010 | keywords | pages [1] -->
Keywords: Complex Network; Bayes Error Rate; Closeness Centrality; Kruskal-Wallis Test; Discrete Fourier Transform

<!-- b000011 | furniture | pages [1] -->
关注数学模型 获取更多资讯

<!-- b000012 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000013 | furniture | pages [2] -->
Team # 2124497

<!-- b000014 | furniture | pages [2] -->
Page 1 of 22

<!-- b000015 | heading | pages [2] -->
Contents

<!-- b000016 | contents | pages [2] -->
1 Introduction

<!-- b000017 | contents | pages [2] -->
2

<!-- b000018 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000019 | contents | pages [2] -->
1.1

<!-- b000020 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | contents | pages [2] -->
2

<!-- b000022 | contents | pages [2] -->
1.2

<!-- b000023 | contents | pages [2] -->
Restatement of the Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
2

<!-- b000025 | contents | pages [2] -->
1.3

<!-- b000026 | contents | pages [2] -->
An Overview of Our work

<!-- b000027 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
2 Problem Analysis

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
3 Model Assumptions and Notations

<!-- b000032 | contents | pages [2] -->
3

<!-- b000033 | contents | pages [2] -->
3.1

<!-- b000034 | contents | pages [2] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
3

<!-- b000036 | contents | pages [2] -->
3.2

<!-- b000037 | contents | pages [2] -->
Notations

<!-- b000038 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
4

<!-- b000040 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000041 | contents | pages [2] -->
4 Model Construction

<!-- b000042 | contents | pages [2] -->
4

<!-- b000043 | contents | pages [2] -->
4.1

<!-- b000044 | contents | pages [2] -->
Measurement of Inﬂuence between Artists . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
4

<!-- b000046 | contents | pages [2] -->
4.2

<!-- b000047 | contents | pages [2] -->
The Music Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
7

<!-- b000049 | contents | pages [2] -->
4.2.1

<!-- b000050 | contents | pages [2] -->
Quantiﬁcation of Similarities Based on the MRDE Framework . . . . . . .

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
4.2.2

<!-- b000053 | contents | pages [2] -->
Distribution of Similarities Between and Within Genres

<!-- b000054 | contents | pages [2] -->
. . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
10

<!-- b000056 | contents | pages [2] -->
4.2.3

<!-- b000057 | contents | pages [2] -->
Test the Measurement of Inﬂuence by the Similarity Network

<!-- b000058 | contents | pages [2] -->
. . . . . . .

<!-- b000059 | contents | pages [2] -->
12

<!-- b000060 | contents | pages [2] -->
4.3

<!-- b000061 | contents | pages [2] -->
The Roles of Characteristics

<!-- b000062 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
14

<!-- b000064 | contents | pages [2] -->
4.3.1

<!-- b000065 | contents | pages [2] -->
Characteristics that Distinguish Genres

<!-- b000066 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
14

<!-- b000068 | contents | pages [2] -->
The Contagious Characteristics among Artists

<!-- b000069 | contents | pages [2] -->
4.3.2

<!-- b000070 | contents | pages [2] -->
. . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
16

<!-- b000072 | contents | pages [2] -->
4.4

<!-- b000073 | contents | pages [2] -->
Revolutionary Artists Based on Closeness Centrality

<!-- b000074 | contents | pages [2] -->
. . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
17

<!-- b000076 | contents | pages [2] -->
4.5

<!-- b000077 | contents | pages [2] -->
Dynamic Process of Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
18

<!-- b000079 | contents | pages [2] -->
5 Test the Model

<!-- b000080 | contents | pages [2] -->
21

<!-- b000081 | contents | pages [2] -->
6 Strengths and Weaknesses

<!-- b000082 | contents | pages [2] -->
21

<!-- b000083 | contents | pages [2] -->
6.1

<!-- b000084 | contents | pages [2] -->
Strengths

<!-- b000085 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
21

<!-- b000087 | contents | pages [2] -->
6.2

<!-- b000088 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [2] -->
22

<!-- b000090 | contents | pages [2] -->
7 Conclusion

<!-- b000091 | contents | pages [2] -->
22

<!-- b000092 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000093 | furniture | pages [2] -->
关注数学模型

<!-- b000094 | furniture | pages [2] -->
2

<!-- b000095 | furniture | pages [2] -->
MATHmodels

<!-- b000096 | furniture | pages [2] -->
获取更多资讯

<!-- b000097 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000098 | furniture | pages [3] -->
Team # 2124497

<!-- b000099 | furniture | pages [3] -->
Page 2 of 22

<!-- b000100 | heading | pages [3] -->
1 Introduction

<!-- b000101 | heading | pages [3] -->
1.1 Background

<!-- b000102 | prose | pages [3] -->
微信公众号：数学模型 Music has had a profound eﬀect on humans and societies throughout history. The evolution of music occurs constantly, inﬂuenced by advanced technology, personal experiences, social events, etc. The internal inﬂuence between artists also accounts for the music changes. Analysis of music is usually deemed relatively perceptual and subjective. However, music that is more abstract in itself can be quantiﬁed by various characteristics, which makes it possible for us to analyze the music systematically and objectively.

<!-- b000103 | prose | pages [3] -->
One of our goals in this paper is to develop appropriate measures to quantify the inﬂuence and similarity of music. Based on the quantiﬁcation, more thorough analyses could be conducted, including identifying the signiﬁcant artists and characteristics. We believe that a better understand- ing of the music evolved could be also be obtained with a series of carefully designed models and experiments.

<!-- b000104 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000105 | heading | pages [3] -->
1.2 Restatement of the Problem

<!-- b000106 | prose | pages [3] -->
The analysis of music inﬂuence involves detail ranging from methods for quantiﬁcation to identiﬁcation of decisive factors. Thus, in order to analyze the inﬂuence of music in a clear and systematic way, we restate the problem as follows.

<!-- b000107 | prose | pages [3] -->
• Develop a measurement of music inﬂuence between artists, and construct a directed inﬂuence network that connects inﬂuencers and followers accordingly;

<!-- b000108 | prose | pages [3] -->
• Quantify the music similarities and compare the music similarities between and within genres;

<!-- b000109 | prose | pages [3] -->
• Testify whether there are signiﬁcant diﬀerences between the distributions of within-genre and between-genre similarities;

<!-- b000110 | prose | pages [3] -->
• Discover the decisive music characteristics that distinguish genres;

<!-- b000111 | prose | pages [3] -->
• Determine the most contagious music characteristics among artists;

<!-- b000112 | prose | pages [3] -->
• Identify the revolutionary artists, and analyze the evolution of music.

<!-- b000113 | heading | pages [3] -->
1.3 An Overview of Our work

<!-- b000114 | prose | pages [3] -->
To address the problem, this paper proposed ﬁve models to solve the respective sub-problems. The rest of the paper is structured as follows. Section 2 states a thorough problem analysis and our motivations. In Section 3, we give the assumptions and notations of the model. Section 4 provides suﬃcient details of our model. In Section 5, we test the proposed model. Section 6 analyzed the strengths and weaknesses of our model. At lat, a conclusion is given in Section 7. A one-page document to the ICM Society is given in the appendices???.

<!-- b000115 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000116 | furniture | pages [3] -->
关注数学模型

<!-- b000117 | furniture | pages [3] -->
2

<!-- b000118 | furniture | pages [3] -->
MATHmodels

<!-- b000119 | furniture | pages [3] -->
获取更多资讯

<!-- b000120 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000121 | furniture | pages [4] -->
Team # 2124497

<!-- b000122 | furniture | pages [4] -->
Page 3 of 22

<!-- b000123 | heading | pages [4] -->
2 Problem Analysis

<!-- b000124 | prose | pages [4] -->
Based on the detailed information provided by the four data sets, we ﬁrst systematically analyze the problem. After exploring and reviewing the relevant literature research, we then construct a 微信公众号：数学模型 detailed model.

<!-- b000125 | prose | pages [4] -->
To begin with, the a directed network is required to be constructed from the inﬂuence_data data set. In inﬂuence_data, a detailed relationship between inﬂuencers and followers is given. For an inﬂuence network, an edge is directed from the inﬂuencer to the follower. Though a directed graph is easy to construct, a measurement of inﬂuence should be developed to describe the strength of the inﬂuence. Therefore, three factors are taking into account to measure the inﬂuence:1) the indicator related to artists active in one certain decade being followed by artists active in other decades, 2) the indicator related to artists of one certain genre being followed by artists of other genres, and 3) the out-degree of the inﬂuencers.

<!-- b000126 | prose | pages [4] -->
On top of that, the music similarity also needs to be quantiﬁed. An abundant amount of data are provided in full_music_data data set, and the quantiﬁcation of high-dimensional data is therefore 微信号：MATHmodels essential. Classical methods, such as the principal components analysis (PCA), are commonly used for dimension reduction. However, we are motivated to use the modiﬁed the randomly distributed framework (RDE) instead, which can take good advantage of interaction information provided by high-dimensional data. We also testify diﬀerence between the distribution of within-genre and between-genre similarities to justify whether the inﬂuencers indeed inﬂuence the followers.

<!-- b000127 | prose | pages [4] -->
Thirdly, we need to analyze roles of characteristics under diﬀerent circumstances. The inﬂuential characteristics are deﬁned to be the ones that are eﬀective in distinguishing the genres, and the contagious characteristics are deﬁned to represent the common inherent music features among artists. We are inspired to test the inﬂuence of a characteristics by comparing the p-values (obtained by conducting non-parametric test) before and after it is removed from other characteristics.

<!-- b000128 | prose | pages [4] -->
Afterwards, the artists who signify the revolutionaries is detected. Empirically, we assume that the revolutionary artists have great impact on others while receiving small inﬂuence from others. Therefore, we are motivated to calculate closeness centrality of the directed inﬂuence network, and use the diﬀerence between out-closeness and in-closeness centrality to measure how revolutionary an artist is.

<!-- b000129 | prose | pages [4] -->
Finally, the analyze of dynamic process of evolution is needed. With the date given in data_year, we aim at analyzing the evolution trend of each musical characteristics from the perspective of frequency domain. Therefore, we are motivated to conduct the discrete Fourier transform in order to observe the diﬀerent frequency components. Since it is not objective to observe the series by the curve shapes, we developed an indicator σ that measures the proportion of low-frequency components.

<!-- b000130 | heading | pages [4] -->
3 Model Assumptions and Notations

<!-- b000131 | heading | pages [4] -->
3.1 Assumptions and Justiﬁcations

<!-- b000132 | prose | pages [4] -->
• The musical characteristics chosen in the data set are representative;

<!-- b000133 | prose | pages [4] -->
• The data collected are reliable;

<!-- b000134 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000135 | furniture | pages [4] -->
关注数学模型

<!-- b000136 | furniture | pages [4] -->
2

<!-- b000137 | furniture | pages [4] -->
MATHmodels

<!-- b000138 | furniture | pages [4] -->
获取更多资讯

<!-- b000139 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000140 | furniture | pages [5] -->
Team # 2124497

<!-- b000141 | furniture | pages [5] -->
Page 4 of 22

<!-- b000142 | prose | pages [5] -->
• The revolutionary artist are the ones who have large impact on others while receiving small inﬂuence from others;

<!-- b000143 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000144 | heading | pages [5] -->
3.2 Notations

<!-- b000145 | prose | pages [5] -->
Symbol Deﬁnition G A directed graph describing the inﬂuence among artists

<!-- b000146 | prose | pages [5] -->
vi The ith node in the graph G

<!-- b000147 | prose | pages [5] -->
eij The edge in graph G directed from node vi to node vj wij The weight of edge eij

<!-- b000148 | prose | pages [5] -->
n0 The number of nodes in graph G

<!-- b000149 | prose | pages [5] -->
nj The in-degree of node vj

<!-- b000150 | prose | pages [5] -->
Iij The inﬂuence of inﬂuencer vi on follower vj 微信号：MATHmodels wij The weight on edge eij in graph G Sij The musical similarity between two nodes

<!-- b000151 | prose | pages [5] -->
ci The ith musical characteristics, i = 1, 2, ...13

<!-- b000152 | prose | pages [5] -->
Fi The set of labels of artists that followed artist vi

<!-- b000153 | prose | pages [5] -->
CCi(i) The in-closeness centrality of node vi

<!-- b000154 | prose | pages [5] -->
CCo(i) The out-closeness centrality of node vi

<!-- b000155 | prose | pages [5] -->
C(i) The synthesized closeness centrality of node vi

<!-- b000156 | heading | pages [5] -->
4 Model Construction

<!-- b000157 | heading | pages [5] -->
4.1 Measurement of Inﬂuence between Artists

<!-- b000158 | prose | pages [5] -->
According to the inﬂuence relationship revealed in the inﬂuence_data data set, a directed graph G(V, E) can be constructed, where V is a set of nodes and E is a set of links directed from one node to another. Let n0 be the number of nodes (the number of artists mentioned in inﬂuence_data). The n0 nodes are labeled from v1 to vn0, and eij denotes the edge directed from vi to vj. For each follower vj, let nj represent its in-degree (i. e. the number of artists that inﬂuence vj). A subgraph showing the relation among one follower and its inﬂuencers is illustrated in Fig. 1.

<!-- b000159 | prose | pages [5, 6] -->
In a addition to construct a directed network by simply connecting the inﬂuencer to the follower, we aim at measuring the inﬂuence by three indicators from the perspective of a pair of the follower and inﬂuencer on edge eij: 1) frequency ekij that indicates the inﬂuence according to the period where inﬂuencer vi and follower vj are active, 2) frequency emij that describes the inﬂuence due to 微信公众号：数学模型

<!-- b000160 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000161 | furniture | pages [5] -->
关注数学模型

<!-- b000162 | furniture | pages [5] -->
2

<!-- b000163 | furniture | pages [5] -->
MATHmodels

<!-- b000164 | furniture | pages [5] -->
获取更多资讯

<!-- b000165 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000166 | furniture | pages [6] -->
Team # 2124497

<!-- b000167 | furniture | pages [6] -->
Page 5 of 22

<!-- b000169 | caption | pages [6] -->
Fig. 1. The subgraph of one follower vj and its nj inﬂuencers

<!-- b000170 | prose | pages [6] -->
the main genres of inﬂuencer vi and follower vj, and 3) the out degree Oi of the inﬂuencer vi. To better explain the three indicator, more explicit deﬁnitions of ekij and emij are given as follows. 微信号：MATHmodels Let Di be the decade when the artist vi begin his or her music career. For inﬂuencer vi and follower vj on edge eij, kij is deﬁned to be the total number of times that artists in period Di are followed by artists in period Dj.

<!-- b000171 | prose | pages [6] -->
Deﬁnition 4.1. For edge eij that is directed from inﬂuencer vi to follower vj, the indicator ekij is deﬁned as:

<!-- b000172 | prose | pages [6] -->
kij ekij = (1) P l∈Sj klj

<!-- b000173 | prose | pages [6] -->
where Sj is the set of labels of inﬂuencers of follower vj.

<!-- b000174 | prose | pages [6] -->
Similarly, let Ri be the main genre of artist vi. Then mij is deﬁned as the total number of times that artists of genre Ri are followed by artists in genre Rj. Deﬁnition 4.2. For edge eij that is directed from inﬂuencer vi to follower vj, the indicator emij is deﬁned as: mij emij = (2) P l∈Sj mlj

<!-- b000175 | prose | pages [6] -->
where Sj is the set of labels of inﬂuencers of follower vj.

<!-- b000176 | prose | pages [6] -->
Applying the data from inﬂuence_data), the ekij and emij for inﬂuencers and followers of each type (including the decade when they began their music career and their main genres) are shown in

<!-- b000177 | caption | pages [6] -->
Fig. 2.

<!-- b000178 | prose | pages [6] -->
Therefore, the inﬂuence Iij of inﬂuencer vi on follower vj should be able to aggregate the data and information provided by the three indicators, i. e. ekij, emij and Oi. Deﬁnition 4.3. The inﬂuence Iij of inﬂuencer vi on follower vj on edge eij is deﬁned as:

<!-- b000179 | prose | pages [6, 7] -->
Iij = ekij · emij · Oi (3) 微信公众号：数学模型 (a) The indicator kij

<!-- b000180 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000181 | furniture | pages [6] -->
关注数学模型

<!-- b000182 | furniture | pages [6] -->
2

<!-- b000183 | furniture | pages [6] -->
MATHmodels

<!-- b000184 | furniture | pages [6] -->
获取更多资讯

<!-- b000185 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000186 | furniture | pages [7] -->
Team # 2124497

<!-- b000187 | furniture | pages [7] -->
Page 6 of 22

<!-- b000189 | prose | pages [7] -->
微信号：MATHmodels (b) The indicator mij

<!-- b000190 | caption | pages [7] -->
Fig. 2. The calculation results of mij and kij. (a) The indicator kij for any pair of inﬂuencers and

<!-- b000191 | prose | pages [7] -->
followers, where the vertical axis denotes the decade when the followers began their music career, and the horizontal axis denotes the time interval of the decade of followers and inﬂuencers. (b) The indicator mij for any pair of inﬂuencers and followers, where the vertical and horizontal axes represent the main genre of the followers and inﬂuencers, respectively.

<!-- b000192 | prose | pages [7] -->
Here, in Example 1, we give a brief example to better illustrate the calculation of inﬂuence emij (the indicator ekij can be calculated by using the exact same method). Since the number of inﬂuencer is huge and the out-degree Oi for the inﬂuencers in each edge can be easily found out from the data set, we will avoid displaying the cumbersome data here.

<!-- b000193 | prose | pages [7, 8] -->
Consider an inﬂuencer vi and a follower vj whose main genres are Avant_garde Example 1 and Classical, respectively. Through the statistics in inﬂuence_data data set, the total number of times for artists of genre Classical to be inﬂuenced by artists of genre Avant_garde is 11, i. e. mij = 11. Additionally, there are in total 37 artists of various genres being followed by the artists of genre Avant_garde. Therefore, it can be calculated that the indicator emij between these two artists is emij = 11/37 ≈0.2973. It should be noted that the emij remains the same for any pair of inﬂuencer and follower whose genres are respectively Avant_garde and Classical.

<!-- b000194 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000195 | furniture | pages [7] -->
关注数学模型

<!-- b000196 | furniture | pages [7] -->
2

<!-- b000197 | furniture | pages [7] -->
MATHmodels

<!-- b000198 | furniture | pages [7] -->
获取更多资讯

<!-- b000199 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000200 | furniture | pages [8] -->
Team # 2124497

<!-- b000201 | furniture | pages [8] -->
Page 7 of 22

<!-- b000203 | prose | pages [8] -->
By employing the calculation method illustrated in Example 1, let the weight wij of each 微信公众号：数学模型 directed edge in graph G be the quantiﬁed inﬂuence Iij (i. e. wij = Iij). Therefore, a weight matrix W is obtained, and graph G can be extended to G(V, E, W ). Fig. 3 demonstrated the overall structure of graph G.

<!-- b000204 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000205 | caption | pages [8] -->
Fig. 3. The structure of graph G. The size of nodes represents the out-degree. The largest two

<!-- b000206 | prose | pages [8] -->
nodes are Bod Dylan and The Beatles, whose subnetwork is presented in Fig. 4

<!-- b000207 | prose | pages [8] -->
In Fig. 3, the color of nodes represent the genre they belong to, and the thickness of an edge denote the its weight (the thicker the edge is, the larger its weight is). Fig. 3 gives a rough distribution of genres and inﬂuence among artist, but is hard to discover details from. To give a better insight into the inﬂuence among artists, a subnetwork shown in Fig. 4 is provided.

<!-- b000208 | heading | pages [8] -->
4.2 The Music Similarity

<!-- b000209 | prose | pages [8] -->
With an abundant amount of data regarding the music-related characteristics, it is essential to develop a measurement to quantify the similarity with these high-dimensional data. Moreover, it is also of great importance to analysis whether the genres are distinguishable according to the similarity measurement that we developed. In this section, we proposed a modiﬁed randomly distributed embedding (MRDE) framework to measure the music similarity, which takes good advantage of interaction information among high-dimensional data. Afterwards, we analyze the similarity distribution between and within genres to identify whether the diﬀerence between within- genre similarity and between-genre similarity is signiﬁcant. Finally, we test the eﬀectiveness of the proposed measurement of inﬂuence in Section 4.1 by analyzing the similarity distribution among artist who do or do nor have mutual inﬂuence.

<!-- b000210 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000211 | furniture | pages [8] -->
关注数学模型

<!-- b000212 | furniture | pages [8] -->
2

<!-- b000213 | furniture | pages [8] -->
MATHmodels

<!-- b000214 | furniture | pages [8] -->
获取更多资讯

<!-- b000215 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000216 | furniture | pages [9] -->
Team # 2124497

<!-- b000217 | furniture | pages [9] -->
Page 8 of 22

<!-- b000218 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000219 | caption | pages [9] -->
Fig. 4. A subnetwork of Bod Dylan, The Beatles and their followers

<!-- b000220 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000221 | heading | pages [9] -->
4.2.1 Quantiﬁcation of Similarities Based on the MRDE Framework

<!-- b000222 | prose | pages [9] -->
In this section, we demonstrate our model for quantifying the musical similarity. The proposed MRDE framework is explained carefully, and the quantiﬁcation result is then given and visualized.

<!-- b000223 | prose | pages [9] -->
To begin with, a brief introduction of the original RDE (randomly distributed embedding) framework is given. The RDE framework is ﬁrst proposed by Ma et al. in 2018 published on PNAS [1]. When dealing with high-dimensional data, dimension reduction techniques are usually applied, but the application is likely to overlook the interactions among high-dimensional variables. To make good use of the interaction information, the RDE framework builds a distribution of a suﬃcient number of embeddings of low-dimension. While each low-dimensional embedding preserves a part a information of the whole system, these low-dimensional embeddings form a probability distribution which can be used to obtain the ﬁnal one-dimensional variable (or the value). Readers could refer to more details in [1]. Hence, we proposed the MRDE framework to adapt the original RDE framework for the problem discussed in this paper, which provides another perspective for the comprehensive evaluation.

<!-- b000224 | prose | pages [9] -->
Among the fourteen musical characteristics summarized in data_by_artist, we eliminate the factor count for the experiment in this section, since count is not music-related and do not provide any information about an artist’s music style. Then we are left with 13 musical characteristics from danceability to popularity. In the MRDE framework, we choose the embedding dimension e to be e = 3 empirically according to the experiment in [1]. In other words, for each 3-dimension embedding, we randomly choose 3 characteristics out of the 13 musical characteristics. There are in total q kinds of combination of the chosen 3 characteristics, which can be calculated by Eq. (4).

<!-- b000225 | prose | pages [9] -->
E  q = (4) e

<!-- b000226 | prose | pages [9] -->
where E = 13 is the total number of musical characteristics involved in the analysis, e = 3 is the embedding dimension.

<!-- b000227 | prose | pages [9, 10] -->
Each of the 13 musical characteristic is label from c1 to c13. For each 3-dimensional embedding, we construct an index tuple l = (l1, l2, l2), (lk = 1, 2, ...13, k = 1, 2, 3), where l1, l2 and l3 are Let Cj represent the tuple of values of 3 chosen the indexes of characteristics in this tuple. characteristics for node vj, then the three characteristics of artist vj is represented as Cj = 微信公众号：数学模型 (cl1, cl2, cl3).

<!-- b000228 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000229 | furniture | pages [9] -->
关注数学模型

<!-- b000230 | furniture | pages [9] -->
2

<!-- b000231 | furniture | pages [9] -->
MATHmodels

<!-- b000232 | furniture | pages [9] -->
获取更多资讯

<!-- b000233 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000234 | furniture | pages [10] -->
Team # 2124497

<!-- b000235 | furniture | pages [10] -->
Page 9 of 22

<!-- b000237 | prose | pages [10] -->
When measuring the similarity between artist vi and artist vj, we need to ﬁrst identify their rough similarity calculated by each embedding. For the kth 3-dimensional embedding (k=1, 2, ..., q), we deﬁne its rough similarity srk as

<!-- b000238 | prose | pages [10] -->
srk = 1 −∥Ci −Cj∥2 (5)

<!-- b000239 | prose | pages [10] -->
Let Sr be the random variable where srk(k = 1, 2, ..., q) are the speciﬁc value. Therefore, the q rough similarity labeled from sr1 to srq can form a probability distribution. The actual similarity Sij between vi and vj is deﬁned as the expectation value of the distribution, formulated in Eq. (6).

<!-- b000240 | prose | pages [10] -->
Sij = E(Sr) (6) 微信号：MATHmodels where Sij ∈[0, 1], and E(Sr) is the expectation of random variable Sr. When Sij is large, it indicates that the these two artist are more similar, and vice versa.

<!-- b000241 | prose | pages [10] -->
By using Eq. (5) and Eq. (6), the similarity Sij between vi and vj can be calculated. The proposed MRDE framework can be better illustrated by the following steps:

<!-- b000242 | prose | pages [10] -->
Step 1: Randomly choose q tuples. Each tuple contains 3 index numbers denoted as l = (l1, l2, l2), and the musical characteristics in this tuple are denoted as (cl1, cl2, cl3);

<!-- b000243 | prose | pages [10] -->
Step 2: For the q tuples (namely the 3-dimensional embeddings), calculated the rough similarity srk, k = 1, 2, ..., q by using Eq. (5);

<!-- b000244 | prose | pages [10] -->
Step 3: Aggregate the rough similarities calculated in each embedding to form the probability distribution of the random variable Sr;

<!-- b000245 | prose | pages [10] -->
Step 4: Given the distribution of Sr, obtain the similarity Sij = E(Sr) by calculating the expec- tation value of random variable Sr.

<!-- b000246 | prose | pages [10] -->
A undirected network G1(V1, E1) is constructed, where V1 is the set of nodes and E1 the set of undirected edges. Since nodes being analyzed are the same as in G, so the label of nodes remain the same (such v1, v2 etc.). It should be noted that even though Eq. (6) and Fig. ?? measures the musical similarity between two artists, the proposed MRDE scheme can also be applied to quantify the musical similarity between genres and songs, as long as the musical characteristics are available.

<!-- b000247 | heading | pages [10] -->
Discussion

<!-- b000248 | prose | pages [10, 11] -->
In the original data_by_artist data set, the order of magnitude of each musical characteristics varies from −6 to 5 . However, since the Euclidean norm is used to measure the rough similarity, the inﬂuence of order of magnitude must be eliminated as much as possible before calculating the Euclidean norm. Thus, the min-max normalization is utilized to normalize each characteristics. All of the normalized value of musical characteristics range from 0 to 1. Moreover, when we apply √ 3. Thus, the calculated the 3-dimensional embedding, the maximum value of rough similarity is √ 微信公众号：数学模型 similarities Sij are reduced to 1/ 3 of the original scale.

<!-- b000249 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000250 | furniture | pages [10] -->
关注数学模型

<!-- b000251 | furniture | pages [10] -->
2

<!-- b000252 | furniture | pages [10] -->
MATHmodels

<!-- b000253 | furniture | pages [10] -->
获取更多资讯

<!-- b000254 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000255 | furniture | pages [11] -->
Team # 2124497

<!-- b000256 | furniture | pages [11] -->
Page 10 of 22

<!-- b000258 | heading | pages [11] -->
4.2.2 Distribution of Similarities Between and Within Genres

<!-- b000259 | prose | pages [11] -->
From Section 4.2.1, we have obtained the similarity between every two artists. From the inﬂuence_data data set, we can easily label each artist with his or her main genre. Therefore, the similarity distribution among artists can easily be transformed into similarity distribution between and within genres. From our intuitive understanding, we would assume that the similarity within genres are smaller than between genres. We might assume that the similarity between genres might also varies. For instance, the genre of Electronic and Country may diﬀer from each other from our daily experience. In this section, we will use the similarity distribution, Gaussian ﬁtting and Bayes error rate for a thorough analysis.

<!-- b000260 | prose | pages [11] -->
微信号：MATHmodels Among the 19 genres (the genre Unknown is eliminated due to the possible interference of  19  wrong or missing information), there are in total kinds of combinations. Fig. 5 is an example 2 of the similarity distribution within the genre Folk and between Folk and Reggae.

<!-- b000261 | caption | pages [11] -->
Fig. 5. The similarity within and between genres. The blue part denotes the similarity distribution

<!-- b000262 | prose | pages [11] -->
within the genre of Folk, while the red part denotes the distribution between Folk and Reggae. The vertical axis represents the number of times that a certain value of similarity appears in the total calculated similarities, and the horizontal axis represents the similarity ranged from 0 to 1.

<!-- b000263 | prose | pages [11] -->
From Fig. 5, we can have an intuitive understanding that the similarity distribution within and between genres is diﬀerent in the given example. But now a question arises: how can this diﬀerence be measured?

<!-- b000264 | prose | pages [11] -->
We are motivated to measure the above-mentioned diﬀerence by using Bayes error rate. Bayesian decision theory can address the patter classiﬁcation problem from the perspective of statistics [2].

<!-- b000265 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000266 | furniture | pages [11] -->
关注数学模型

<!-- b000267 | furniture | pages [11] -->
2

<!-- b000268 | furniture | pages [11] -->
MATHmodels

<!-- b000269 | furniture | pages [11] -->
获取更多资讯

<!-- b000270 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000271 | furniture | pages [12] -->
Team # 2124497

<!-- b000272 | furniture | pages [12] -->
Page 11 of 22

<!-- b000273 | prose | pages [12] -->
The theory quantiﬁes the trade-oﬀbetween the decision made and the costs that accompany the decision. Bayes error, on the other hand, is the lowest possible error rate for a pattern classiﬁcation problem [3]. Let class ω1 denote the within genres, class ω2 denote the between genres, and s denote 微信公众号：数学模型 the similarity value. P(ωi|s), i = 1, 2 is the posterior probability. For the distribution illustrated in Fig. 6, the probability of error can be calculated by Eq. (7).

<!-- b000274 | prose | pages [12] -->
( P(ω1|s) whenP(ω2|s) > P(ω1|s) P(error|s) = (7) P(ω2|s) whenP(ω1|s) > P(ω2|s)

<!-- b000275 | prose | pages [12] -->
The Bayes error rate is therefore formulated in Eq. (8).

<!-- b000276 | prose | pages [12] -->
Z ∞ Z s0 P(ω2|s)p(s)ds + P(ω1|s)p(s)ds P(error) = (8) −∞ s0

<!-- b000277 | prose | pages [12] -->
where s0 is a certain point on the horizontal axis shown in Fig. 6 that divides the space into two parts. P(error) can also be denoted as the size of shadow area. 微信号：MATHmodels Due to the large scale of data, we demonstrate some typical similarity distribution here. First of all, Fig. 7 shows the similarity within and between the genres of Country and Eletronic.

<!-- b000278 | prose | pages [12] -->
From Fig. 7, it can be observed that the overall similarity within Country is much smaller than the one within Electronic and between these two genres. The results indicate that value of musical characteristics of artists of genre Country are highly similar, whereas the ones of artists of genre Electronic are relatively scattered. Moreover, by performing Gaussian ﬁtting, the estimated distribution for within the genre Country, within the genre Electronic and between the two genres are N(0.85, 0.06), N(0.74, 0.0.8) and N(0.75, 0.09), respectively. With the Gaussian ﬁtting results, the Bayes error of distributions in Fig. 7(a) and Fig. 7(b) are 0.486 and 0.916, respectively, indicating again that the similarity distributions in Fig. 7(a) are more diﬀerent and distinguishable.

<!-- b000279 | prose | pages [12] -->
In order to have an overall understanding of the similarity within and between genres, Fig. 8 shows the similarity distribution by combining all the values of similarity within each genre and between every two genres.

<!-- b000280 | prose | pages [12, 13] -->
The Gaussianﬁttingresultofthewithin-genreandbetween-genredistributionareN(0.806, 0.078) and N(0.758, 0.095), respectively. The Bayes error rate calculated is 0.770. Combining the vi- sualization result in Fig. 8, the Gaussian ﬁtting result and the calculated Bayes error rate, we can 微信公众号：数学模型 (a) The similarity within Country and between genres (b) The similarity within Electronic and between genres

<!-- b000281 | caption | pages [12] -->
Fig. 6. An example of probability distribution to illustrate the Bayes error rate

<!-- b000282 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000283 | furniture | pages [12] -->
关注数学模型

<!-- b000284 | furniture | pages [12] -->
2

<!-- b000285 | furniture | pages [12] -->
MATHmodels

<!-- b000286 | furniture | pages [12] -->
获取更多资讯

<!-- b000287 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000288 | furniture | pages [13] -->
Team # 2124497

<!-- b000289 | furniture | pages [13] -->
Page 12 of 22

<!-- b000291 | caption | pages [13] -->
Fig. 7. The similarity distribution within and between two typical genres. (a) The light blue and

<!-- b000292 | prose | pages [13] -->
微信号：MATHmodels blue curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result between Country and Electronic. The light orange and orange curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result within Country. (b) The light blue and blue curves denote the same thing as in subgraph a. The light orange and orange curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result within Electronic.

<!-- b000293 | prose | pages [13] -->
reach a conclusion: 1) the similarity between genres is generally larger than within genres, and 2) the smaller the between-genre similarity is, the less similar are the corresponding two genres.

<!-- b000294 | heading | pages [13] -->
4.2.3 Test the Measurement of Inﬂuence by the Similarity Network

<!-- b000295 | prose | pages [13] -->
In section 4.1, the measurement of inﬂuence among artists is proposed. In Section 4.2.1, we quantify the similarities of musical characteristics. To discover the interaction relationship between the above-mentioned two measurements, we conduct another experiment by combining the directed network G of inﬂuence and the undirected network G1 of similarities. The experiment is aim at detecting whether the measurement of inﬂuence in Section 4.1 can actually reﬂect the real-world inﬂuence among artists.

<!-- b000296 | prose | pages [13] -->
First of all, we will explained how the combination works in this paper. Basically, we will reallocate the similarity distribution in G1 in to two distribution, based on whether two artists have unilateral or mutual inﬂuence on each other in graph G. Let S1 and S2 be two random variables, where S1 denotes the similarity distribution of edges in G1 that are connected in graph G (the directed graph describing the inﬂuence), and S2 denotes the similarity distribution of edges in G1 that are not connected in graph G.

<!-- b000297 | prose | pages [13] -->
Step 1: Start traversing all edges in the undirected similarity network G1;

<!-- b000298 | prose | pages [13] -->
Step 2: Consider an undirected edge that connect node vi and vj. If there exists a directed edge in the inﬂuence network G directed from vi to vj or from vj to vi, then the similarity value Sij on this undirected edge is a possible value of the random variable S1;

<!-- b000299 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000300 | furniture | pages [13] -->
关注数学模型

<!-- b000301 | furniture | pages [13] -->
2

<!-- b000302 | furniture | pages [13] -->
MATHmodels

<!-- b000303 | furniture | pages [13] -->
获取更多资讯

<!-- b000304 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000305 | furniture | pages [14] -->
Team # 2124497

<!-- b000306 | furniture | pages [14] -->
Page 13 of 22

<!-- b000307 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000308 | caption | pages [14] -->
Fig. 8. The overall similarity distribution. The light orange and orange curves denote the distribution

<!-- b000309 | prose | pages [14] -->
微信号：MATHmodels that concludes the between-genre similarity of any combination of two genres. The light blue and blue curves denote the distribution that concludes all the within-genre similarity of every genre.

<!-- b000310 | prose | pages [14] -->
Step 3: Consider the same edge in Step 2. If no directed edge exists between vi and vj in graph G, then the similarity value Sij is a possible value of the random variable S2;

<!-- b000311 | prose | pages [14] -->
Step 4: Repeat Step 2 and Step 3 until all the undirected edges in graph G1 have been traversed;

<!-- b000312 | prose | pages [14] -->
Step 5: Compute the distributions of random variables S1 and S2.

<!-- b000313 | prose | pages [14] -->
The visualization of distributions of the two random variables are displayed in Fig. 9.

<!-- b000314 | caption | pages [14] -->
Fig. 9. The distributions of S1 and S2. The light orange and orange curves denote the distribution

<!-- b000315 | prose | pages [14] -->
when there is no inﬂuence between to artists. The light blue and blue curves denote the distribution when two artists are unilaterally or mutually inﬂuence by each other.

<!-- b000316 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000317 | furniture | pages [14] -->
关注数学模型

<!-- b000318 | furniture | pages [14] -->
2

<!-- b000319 | furniture | pages [14] -->
MATHmodels

<!-- b000320 | furniture | pages [14] -->
获取更多资讯

<!-- b000321 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000322 | furniture | pages [15] -->
Team # 2124497

<!-- b000323 | furniture | pages [15] -->
Page 14 of 22

<!-- b000324 | prose | pages [15] -->
The GaussianﬁttingresultforthedistributionofS1 andS2 are N(0.830, 0.067)andN(0.781, 0.076), respectively. The Bayes error rate is 0.6452. The overall similarity between the artists who uni- laterally or mutually inﬂuenced one another is signiﬁcantly larger than similarity of artists that did 微信公众号：数学模型 not inﬂuence each other. The result demonstrates that the similarity of artists who have a inﬂuence relationship is in fact larger than the artists who do not. That is to say, the identiﬁed inﬂuencers indeed inﬂuence the respective followers from a statistical perspective.

<!-- b000325 | heading | pages [15] -->
4.3 The Roles of Characteristics

<!-- b000326 | prose | pages [15] -->
When measuring the music similarity, we have combined the information of 13 musical char- acteristics to form the quantiﬁcation. However, what remains unknown is the roles that diﬀerent musical characteristics plays in inﬂuencing the music. In other words, we wish to identify the one or several characteristics that are signiﬁcant in distinguishing the genres. We also analyze which characteristics indicate the more general inherent features among artists. In this section, we ﬁrst deﬁne the central node in each genre. Then we eliminate the characteristics one at a time or one by one, and conduct the non-parametric test to identify the roles of characteristics. 微信号：MATHmodels

<!-- b000327 | heading | pages [15] -->
4.3.1 Characteristics that Distinguish Genres

<!-- b000328 | prose | pages [15] -->
Due to the lack of synthesized data for each genre, we ﬁrst synthesize the information about musical characteristics by deﬁning the central nodes. Then the Kruskal-Wallis test is utilized to identify the most inﬂuential characteristics that distinguish genres.

<!-- b000329 | prose | pages [15] -->
The Central Nodes of Each Genre:

<!-- b000330 | prose | pages [15] -->
We assume that each node in one genre is accounted for a certain percentage when deciding the central node of this genre. The percentage of node vj is denoted as Pj, formulated in Eq. (9).

<!-- b000331 | prose | pages [15] -->
P k∈Fj IjkSjk Pj = (9) Oj

<!-- b000332 | prose | pages [15] -->
where Fj is the set of labels of artists that follow artist vj. Ijk and Sjk denote the inﬂuence and similarity between vj and vk, respectively.

<!-- b000333 | prose | pages [15] -->
Let Ri be the set of labels of nodes that belong to the ith genre, where i = 1, 2, ...19. Let Chi represent the 13 musical characteristics of the central node of the ith genre, then Chi is deﬁned in Eq. (10).

<!-- b000334 | prose | pages [15] -->
P j∈Ri Pj · Cj Chi = (10) P j∈Ri Pj where Cj is the vector of 13 musical characteristics of node vj.

<!-- b000335 | prose | pages [15] -->
We can then obtain the 13 musical characteristics of central nodes of each genre by using Eq. (10).

<!-- b000336 | prose | pages [15] -->
The Most Inﬂuential Characteristics:

<!-- b000337 | prose | pages [15, 16] -->
Let M1 be the 19 × 13 matrix, where each row stores the vector of 13 musical characteristics of the central node of each genre. M1 is formulated in Eq. (11).

<!-- b000338 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000339 | furniture | pages [15] -->
关注数学模型

<!-- b000340 | furniture | pages [15] -->
2

<!-- b000341 | furniture | pages [15] -->
MATHmodels

<!-- b000342 | furniture | pages [15] -->
获取更多资讯

<!-- b000343 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000344 | furniture | pages [16] -->
Team # 2124497

<!-- b000345 | furniture | pages [16] -->
Page 15 of 22

<!-- b000347 | prose | pages [16] -->
  Ch1 Ch2   微信公众号：数学模型 M1 = (11) ...

<!-- b000348 | prose | pages [16] -->
Ch19

<!-- b000349 | prose | pages [16] -->
where Chi represents the 13 musical characteristics of the central node of the ith genre.

<!-- b000350 | prose | pages [16] -->
The uniformed values of matrix M1 is visualized in Fig. 10. For each column in Fig. 10, the corresponding characteristics has a great inﬂuence in distinguishing genres if the colors of each cube demonstrates a greater variability. We could roughly observe that the values of characteristics of Energy, Valence, Speechiness varies to a large extent, while values of Acousticness, Instrumen- talness have relatively concentrated distribution. We will test the rough conclusion by conducting Kruskal-Wallis test on these 5 characteristics in the following part.

<!-- b000351 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000352 | caption | pages [16] -->
Fig. 10. The values of musical characteristics of the central nodes in each genre.

<!-- b000353 | prose | pages [16] -->
The Kruskal-Wallis test is a non-parametric test that can assess the the signiﬁcant diﬀerences by two or more groups of variables [4]. The null hypothesis H0 and the alternative hypothesis H1 are deﬁned. The null hypothesis represents no eﬀect or no diﬀerence, while the alternative hypothesis denotes the presence of an eﬀect or a diﬀerence [5]. A p−value is the probability that assumes H0 is true. Namely, the smaller the p-value, the strong the evidence evidence against the null hypothesis.

<!-- b000354 | prose | pages [16] -->
By the most inﬂuential characteristics, we mean that theses characteristics play important roles in distinguishing the genres. In other words, the similarity between genres will signiﬁcantly increase once theses characteristics are removed from matrix M1. Therefore, we removed each one of the 13 columns in M1, and calculate the respective p-value before and after the elimination. The Kruskal-Wallis test is applied in calculating the p-value. The typical p-values calculated are presented in Table 2.

<!-- b000355 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000356 | furniture | pages [16] -->
关注数学模型

<!-- b000357 | furniture | pages [16] -->
2

<!-- b000358 | furniture | pages [16] -->
MATHmodels

<!-- b000359 | furniture | pages [16] -->
获取更多资讯

<!-- b000360 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000361 | furniture | pages [17] -->
Team # 2124497

<!-- b000362 | furniture | pages [17] -->
Page 16 of 22

<!-- b000363 | caption | pages [17] -->
Table 2: The typical p-values when removing one of the characteristics

<!-- b000364 | prose | pages [17] -->
The removed characteristics Energy Valence Speechiness Acousticness Instrumentalness 微信公众号：数学模型 p-value before elimination 0.1284 0.1284 0.1284 0.1284 0.1284

<!-- b000365 | prose | pages [17] -->
p-value after elimination 0.6500 0.5319 0.3057 0.0086 0.0035

<!-- b000366 | prose | pages [17] -->
* The p-values in the second row denote the non-parametric results before elimination. The p-values in the third row is the result after the characteristics of this column has been eliminated.

<!-- b000367 | prose | pages [17] -->
From Table 2, the result shows that after eliminating Energy, Valence and Speechiness, the p-value increases signiﬁcantly, meaning that the similarity distributions of each genre become less diﬀerent after the elimination. Therefore, Energy, Valence, Speechiness are inﬂuential character- istics in distinguishing genres. The experiment result analysis is similar for other characteristics. On the other hand, the p-values become extremely small after eliminating Acousticness and Instru- mentalness, meaning that these two characteristics are distributed similarly among genres. We can 微信号：MATHmodels conclude that Energy, Valence and Speechiness are the relatively inﬂuential characteristics, while Energy is even more inﬂuential than other inﬂuential characteristics.

<!-- b000368 | heading | pages [17] -->
4.3.2 The Contagious Characteristics among Artists

<!-- b000369 | prose | pages [17] -->
In the last section, we discussed how inﬂuential the characteristics are when distinguishing the genres. In this section, we aim at discovering how Contagious the characteristics are when deciding the musical style of various artists.

<!-- b000370 | prose | pages [17] -->
The Selected Artists:

<!-- b000371 | prose | pages [17] -->
Since there are in total 5854 artists in the data_by_artists data set, it is neither practical nor necessary to perform the Kruskal-Wallis test among all the available artists. Therefore, we selected the top 25 artists who have the highest Pj value (who accounted for more percentage when deciding the central nodes) introduced in Section 4.3.1. Let M1 be the 25 × 13 matrix, where each row stores the vector of 13 musical characteristics of the central node of each genre. M1 is formulated in Eq. (11).

<!-- b000372 | prose | pages [17] -->
  Ch1 Ch2   M2 = (12) ...

<!-- b000373 | prose | pages [17] -->
Ch25

<!-- b000374 | prose | pages [17] -->
where Chi represents the 13 musical characteristics of the central node of the ith artists.

<!-- b000375 | prose | pages [17] -->
The Most Contagious Characteristics:

<!-- b000376 | prose | pages [17] -->
Diﬀerent from the level of characteristics inﬂuence in Section 4.3.1, we deﬁne the characteristics to be Contagious when they represent the common inherent features of artists’ musical styles. Following the idea of non-parametric test in Section 4.3.1, the Kruskal-Wallis test can also be used here to measure the level Contagious. The adapted method is illustrated as follows:

<!-- b000377 | prose | pages [17, 18] -->
Step 1: For the 13 musical characteristics, calculate the corresponding 13 p-values. Each p-value is obtained by conducting Kruskal-Wallis test when the certain one out of 13 characteristics is temporally removed;

<!-- b000378 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000379 | furniture | pages [17] -->
关注数学模型

<!-- b000380 | furniture | pages [17] -->
2

<!-- b000381 | furniture | pages [17] -->
MATHmodels

<!-- b000382 | furniture | pages [17] -->
获取更多资讯

<!-- b000383 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000384 | furniture | pages [18] -->
Team # 2124497

<!-- b000385 | furniture | pages [18] -->
Page 17 of 22

<!-- b000387 | prose | pages [18] -->
Step 2: Pick out the smallest p-value in step one and eliminate the respective characteristics per- 微信公众号：数学模型 manently from M2. Name the characteristics as the most contagious characteristics;

<!-- b000388 | prose | pages [18] -->
Step 3: For the rest 12 characteristics, repeat the process in Step 1 and Step2. The characteristics that was picked out and eliminated is named as the the second most contagious characteristics;

<!-- b000389 | prose | pages [18] -->
Step 4: Repeat the process described from Step 1 to Step 3, until all the 13 characteristics have been sorted with an order.

<!-- b000390 | prose | pages [18] -->
Due to the limited length of the article, we will only demonstrate the 4 most contagious characteristics calculated from the above steps. Moreover, among the 25 artists we chose, their characteristics Mode all possess the value 1. Since Mode is apparently the same for all the selected artists, it can be deemed as the most contagious characteristics. Table 3 listed the p-values of the 微信号：MATHmodels other 3 most contagious characteristics before and after they are eliminated.

<!-- b000391 | caption | pages [18] -->
Table 3: The p-values when removing the 4 most contagious characteristics

<!-- b000392 | prose | pages [18] -->
The removed characteristics Acousticness Danceability Valence

<!-- b000393 | prose | pages [18] -->
p-value before elimination 0.7786 0.2631 0.0326

<!-- b000394 | prose | pages [18] -->
p-value after elimination 0.2631 0.0326 0.0205

<!-- b000395 | prose | pages [18] -->
* The p-values in the second row denote the non-parametric results before elimination of the characteristics of the corresponding column, while the third row denotes results after elimination.

<!-- b000396 | prose | pages [18] -->
From Table 3, we can draw a conclusion that Mode, Acousticness, Danceability and Valence are the most contagious characteristics among artists, while the Mode and Acousticness have the highest and the second highest level of contagiousness. The Danceability and Valence are the third and fourth most contagious characteristics, respectively. Since the smaller p-values represent larger signiﬁcant diﬀerence, our experiment results are valid because: the elimination of our discovered contagious characteristics will lead to signiﬁcant reduction of the p-value, indicating that characteristics have more concentrated distribution after the contagious characteristics are removed. The results is in correspondence with our deﬁnition of contagiousness.

<!-- b000397 | heading | pages [18] -->
4.4 Revolutionary Artists Based on Closeness Centrality

<!-- b000398 | prose | pages [18] -->
By revolutionary artists, we generally mean that their contribution to the ﬁeld should be signiﬁcant. Moreover, they ought to have great impact on others while receiving small inﬂuence from others. Inspired by the structure of the inﬂuence network G constructed in Section 4.1, we apply the evaluation of important nodes in discovering the revolutionary artists. To be more speciﬁc, we combine the in-closeness and out-closeness centrality to evaluate the signiﬁcance of an artists in revolutionaries. Our goal is to discover the artists with small in-closeness centrality and large out-closeness centrality.

<!-- b000399 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000400 | furniture | pages [18] -->
关注数学模型

<!-- b000401 | furniture | pages [18] -->
2

<!-- b000402 | furniture | pages [18] -->
MATHmodels

<!-- b000403 | furniture | pages [18] -->
获取更多资讯

<!-- b000404 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000405 | furniture | pages [19] -->
Team # 2124497

<!-- b000406 | furniture | pages [19] -->
Page 18 of 22

<!-- b000407 | prose | pages [19] -->
For the inﬂuence network G(V, E), the closeness centrality CC(i) of node vi is the average farness to all the other nodes in the network, formulated in Eq. (13).

<!-- b000408 | prose | pages [19] -->
n −1 微信公众号：数学模型 CC(i) = (13) P j̸=i d(i, j)

<!-- b000409 | prose | pages [19] -->
where n is the number of nodes in graph G.

<!-- b000410 | prose | pages [19] -->
Since closeness is a directional measure in the directed graph, the in-closeness centrality CCi(i) and the out-closeness centrality CCo(i) can be calculated accordingly. To evaluate the inﬂuence of the evolutionary artists who have large out-closeness centrality and small in-closeness centrality, the synthesized closeness centrality of artist vi is deﬁned in Eq. (14).

<!-- b000411 | prose | pages [19] -->
C(i) = CCo(i) −CCi(i) (14)

<!-- b000412 | prose | pages [19] -->
The synthesized closeness centrality of the top 12 artists are shown in Fig. 11. 微信号：MATHmodels

<!-- b000413 | caption | pages [19] -->
Fig. 11. The synthesized closeness centrality of the top 12 artists

<!-- b000414 | prose | pages [19] -->
The basic information of top 12 evolutionary artists are listed in Table 4.

<!-- b000415 | prose | pages [19] -->
Reader can easily ﬁnd our results reliable according the name of these 12 artist. For instance, Dylan was awarded the Nobel Prize in Literature in 2016, Chuck Berry is one of the pioneers of Rock and Roll music, and The Beatles is regarded as the most inﬂuential band of all time.

<!-- b000416 | heading | pages [19] -->
4.5 Dynamic Process of Evolution

<!-- b000417 | prose | pages [19, 20] -->
From data_by_year data set, we have known the evolution trend of the musical characteristics over time. Though the general trend is easy to observe by visualizing the data, deeper information Artist ID Name Centrality Artist ID Name Centrality 微信公众号：数学模型 120521 Chuck Berry 0.2921 287604 Louis Jordan 0.2777 824022 Little Richard 0.2904 269972 Little Willie John 0.2731 66915 Bob Dylan 0.2838 549797 Hank Williams 0.2730 79016 Billie Holiday 0.2806 317093 Nat King Cole 0.2729 608701 Muddy Waters 0.2801 754032 The Beatles 0.2708 46861 Ray Charles 0.2783 238115 Sam Cooke 0.2702

<!-- b000418 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000419 | furniture | pages [19] -->
关注数学模型

<!-- b000420 | furniture | pages [19] -->
2

<!-- b000421 | furniture | pages [19] -->
MATHmodels

<!-- b000422 | furniture | pages [19] -->
获取更多资讯

<!-- b000423 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000424 | furniture | pages [20] -->
Team # 2124497

<!-- b000425 | furniture | pages [20] -->
Page 19 of 22

<!-- b000426 | caption | pages [20] -->
Table 4: The basic information of top 12 evolutionary artists

<!-- b000428 | prose | pages [20] -->
* From left to right, top to bottom, the 12 artists are sorted according to their synthesized centrality.

<!-- b000429 | prose | pages [20] -->
could still be discovered. We are then motivated to analyze the frequency components of time series of each musical characteristics.

<!-- b000430 | prose | pages [20] -->
微信号：MATHmodels Discrete Fourier transform (DFT) could transform a sequence of samples with a ﬁnite length into a equally-spaced samples discrete-time Fourier transform with the same length [7]. Let x[n] denote a time series. The DFT X[k] of the series x[n] is formulated in Eq. (15).

<!-- b000431 | prose | pages [20] -->
N−1 x[n]e−j 2π X N kn, k = 0, 1, 2, ..., N −1 X[k] = (15) n=0

<!-- b000432 | prose | pages [20] -->
where N is the length of series x[n].

<!-- b000433 | prose | pages [20] -->
An indicator σ is developed in Eq. (16), which measures the proportion of low-frequency components in the time series x[n].

<!-- b000434 | prose | pages [20] -->
σ = 2 P4 m=1 |X[m]|2 (16) PN−1 m=0 |X[m]|2

<!-- b000435 | prose | pages [20] -->
PN−1 m=0 |X[m]|2 where N is the length of x[n], is the energy of series x[n]. It should be noted that FFT N (fast Fourier transform) is used instead of DFT when computing DFT by computers.

<!-- b000436 | prose | pages [20] -->
Eq. (16) is reasonable because |X[0]| = 0 (the DC component) according to data preprocessing, x[n]−¯x[n] where ˆx[n] = x[n]max−¯x[n]. ¯x[n] and x[n]max denote the average and maximum value of series x[n], respectively.

<!-- b000437 | prose | pages [20] -->
For computers, we apply IFFT (inverse fast Fourier transform) to the four low-frequency components illustrated in Eq. (16). The time series x[n] is the data of Acousticness from 1955 to 2014 of the genre Pop & Rock. N = 60 is the length of x[n]. The results of FFT are shown in Fig. 12.

<!-- b000438 | prose | pages [20, 21] -->
From Fig. 12, we can observe that the time series reconstructed from the low-frequency com- ponents can well represent the overall trend of the original time series. The result also indicates the the low-frequency components takes up more percentage in the time series of Acousticness of the genre Pop & Rock 微信公众号：数学模型 (a) Amplitude of the FFT result (b) Phase of the FFT result

<!-- b000439 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000440 | furniture | pages [20] -->
关注数学模型

<!-- b000441 | furniture | pages [20] -->
2

<!-- b000442 | furniture | pages [20] -->
MATHmodels

<!-- b000443 | furniture | pages [20] -->
获取更多资讯

<!-- b000444 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000445 | furniture | pages [21] -->
Team # 2124497

<!-- b000446 | furniture | pages [21] -->
Page 20 of 22

<!-- b000448 | prose | pages [21] -->
微信号：MATHmodels (c) The original time series (d) The IFFT of low-frequency components of the original seires

<!-- b000449 | caption | pages [21] -->
Fig. 12. The process of reserving the low-frequency components of x[n]

<!-- b000450 | prose | pages [21] -->
We calculate σ for other typical characteristics of the genre Pop & Rock. The result is listed in

<!-- b000451 | caption | pages [21] -->
Table 5.

<!-- b000452 | caption | pages [21] -->
Table 5: The σ values in for the time series of three typical characteristics

<!-- b000453 | prose | pages [21] -->
Energy Popularity Liveness Characteristics

<!-- b000454 | prose | pages [21] -->
σ 0.7895 0.8481 0.4936

<!-- b000455 | prose | pages [21] -->
The results indicate that Energy and Popularity have larger proportion of low-frequency com- ponents, and have a smoother revolution over time. Meanwhile, Liveness has more high-frequency components. The dynamic process of evolution for other characteristics can be computed and analyzed in the exact same way.

<!-- b000456 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000457 | furniture | pages [21] -->
关注数学模型

<!-- b000458 | furniture | pages [21] -->
2

<!-- b000459 | furniture | pages [21] -->
MATHmodels

<!-- b000460 | furniture | pages [21] -->
获取更多资讯

<!-- b000461 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000462 | furniture | pages [22] -->
Team # 2124497

<!-- b000463 | furniture | pages [22] -->
Page 21 of 22

<!-- b000464 | heading | pages [22] -->
5 Test the Model

<!-- b000465 | prose | pages [22] -->
In Section 4.3.1 we introduced the deﬁnition of Central node in each genre. Therefore, we will test the eﬀectiveness of our Central node model in this section. 微信公众号：数学模型 The within-genre similarity distribution of Country is given in Section 4.2.2, while the Gaussian ﬁtting result is N(0.85, 0.06). Diﬀerent from the similarity distribution deﬁned previously (where similarity denotes the similarity between every two nodes in the certain genre), we re-deﬁne the distribution of similarity values between the central node and other nodes within Country.

<!-- b000466 | prose | pages [22] -->
From the deﬁnition of central nodes, we can have an intuitive understanding that the overall similarity will become smaller after the re-deﬁnition, because the central node is likely to locate at the "center" of the genre. The new similarity distribution within Country is shown in Fig. 13.

<!-- b000467 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000468 | caption | pages [22] -->
Fig. 13. The new similarity distribution.

<!-- b000469 | prose | pages [22] -->
The Gaussian ﬁtting result for the new distribution is N(0.45, 0.04). Compared with the original distribution (which is N(0.85, 0.06)), the expectation value of similarity is signiﬁcantly reduced, meaning that our proposed model of central nodes is valid.

<!-- b000470 | heading | pages [22] -->
6 Strengths and Weaknesses

<!-- b000471 | heading | pages [22] -->
6.1 Strengths

<!-- b000472 | prose | pages [22] -->
1. For the measurement of inﬂuence, we have considered comprehensive aspects with the provided information in the inﬂuence relationship;

<!-- b000473 | prose | pages [22] -->
2. The MRDE framework we proposed for similarity measurement can well retain information of high-dimensional data;

<!-- b000474 | prose | pages [22, 23] -->
3. Closeness centrality is used to detect the revolutionary artists. The idea of this method is tested to be eﬀective by comparing the results with real-life information of corresponding artists.

<!-- b000475 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000476 | furniture | pages [22] -->
关注数学模型

<!-- b000477 | furniture | pages [22] -->
2

<!-- b000478 | furniture | pages [22] -->
MATHmodels

<!-- b000479 | furniture | pages [22] -->
获取更多资讯

<!-- b000480 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000481 | furniture | pages [23] -->
Team # 2124497

<!-- b000482 | furniture | pages [23] -->
Page 22 of 22

<!-- b000484 | heading | pages [23] -->
6.2 Weaknesses

<!-- b000485 | prose | pages [23] -->
微信公众号：数学模型 1. The aggregation we used in the MRDE framework is not accurate enough for deﬁning the actual similarity value from the distribution;

<!-- b000486 | prose | pages [23] -->
2. When we introduced the method for time series analysis, more state-of-the-art mechanism can be utilized.

<!-- b000487 | heading | pages [23] -->
7 Conclusion

<!-- b000488 | prose | pages [23] -->
In this paper, we proposed a detailed model in order to analyze the music objectively. The measurement of inﬂuence and quantiﬁcation of similarity is proposed. Kruskal-Wallis test is performed to identify the inﬂuential characteristics in distinguishing genres, and the contagious nodes are detected using the similar method. Moreover, careful analyses of dynamic process 微信号：MATHmodels evolution are done by transforming the characteristics’ time series by discrete Fourier transform.

<!-- b000489 | prose | pages [23] -->
In the future, more state-of-the-art techniques could be utilized to analyze the evolution process. For example, the long short term memory (LSTM) framework to predict the time series, providing insight into the possible future trend of music evolution. Meanwhile, the external inﬂuence on the evolution of music could be examined or even quantiﬁed by calculating the correlation value (the Pearson correlation for instance) between the given the time series of external factors and a certain characteristics.

<!-- b000490 | heading | pages [23] -->
References

<!-- b000491 | references | pages [23] -->
[1] Ma, H., Leng, S., Aihara, K., Lin, W., & Chen, L. (2018). Randomly distributed embedding

<!-- b000492 | references | pages [23] -->
making short-term high-dimensional data predictable. Proceedings of the National Academy

<!-- b000493 | references | pages [23] -->
of Sciences, 115(43), E9994-E10002.

<!-- b000494 | references | pages [23] -->
[2] Yuille, A. L., & Bülthoﬀ, H. H. (1993). Bayesian decision theory and psychophysics.

<!-- b000495 | references | pages [23] -->
[3] Tumer, K., & Ghosh, J. (1996, August). Estimating the Bayes error rate through classiﬁer

<!-- b000496 | references | pages [23] -->
combining. In Proceedings of 13th international conference on pattern recognition (Vol. 2,

<!-- b000497 | references | pages [23] -->
pp. 695-699). IEEE.

<!-- b000498 | references | pages [23] -->
[4] McKight, P. E., & Najab, J. (2010). Kruskal-wallis test. The corsini encyclopedia of psychol-

<!-- b000499 | references | pages [23] -->
ogy, 1-1.

<!-- b000500 | references | pages [23] -->
[5] Hamill, T. M. (1999). Hypothesis tests for evaluating numerical precipitation forecasts.

<!-- b000501 | references | pages [23] -->
Weather and Forecasting, 14(2), 155-167.

<!-- b000502 | references | pages [23] -->
[6] Valente, T. W., Coronges, K., Lakon, C., & Costenbader, E. (2008). How correlated are

<!-- b000503 | references | pages [23] -->
network centrality measures?. Connections (Toronto, Ont.), 28(1), 16.

<!-- b000504 | references | pages [23] -->
[7] Winograd, S. (1978). On computing the discrete Fourier transform. Mathematics of compu-

<!-- b000505 | references | pages [23] -->
tation, 32(141), 175-199.

<!-- b000506 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000507 | furniture | pages [23] -->
关注数学模型

<!-- b000508 | furniture | pages [23] -->
2

<!-- b000509 | furniture | pages [23] -->
MATHmodels

<!-- b000510 | furniture | pages [23] -->
获取更多资讯

<!-- b000511 | furniture | pages [24] -->
Team # 2124497

<!-- b000512 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000513 | references | pages [24] -->
Feb 9th , 2021

<!-- b000514 | references | pages [24] -->
A Valuable Work to Analyze the Influence of Music

<!-- b000515 | references | pages [24] -->
微信公众号：数学模型

<!-- b000516 | references | pages [24] -->
Understanding the influence

<!-- b000517 | references | pages [24] -->
K E Y W O R D S :

<!-- b000518 | references | pages [24] -->
of music is a skill that

<!-- b000519 | references | pages [24] -->
humans have always

<!-- b000520 | references | pages [24] -->
wanted to possess. Whether

<!-- b000521 | references | pages [24] -->
Complex Network

<!-- b000522 | references | pages [24] -->
to explore the influence

<!-- b000523 | references | pages [24] -->
relationship between

<!-- b000524 | references | pages [24] -->
musicians or study the

<!-- b000525 | references | pages [24] -->
微信号：MATHmodels

<!-- b000526 | references | pages [24] -->
Bayes Error Rate

<!-- b000527 | references | pages [24] -->
music similarity, the models

<!-- b000528 | references | pages [24] -->
and methods of complex

<!-- b000529 | references | pages [24] -->
network analysis are always

<!-- b000530 | references | pages [24] -->
Closeness Centrality

<!-- b000531 | references | pages [24] -->
valuable. By connecting

<!-- b000532 | references | pages [24] -->
influencers and followers

<!-- b000533 | references | pages [24] -->
and assigning weights to the

<!-- b000534 | references | pages [24] -->
Kruskal-Wallis Test

<!-- b000535 | references | pages [24] -->
corresponding edges, a

<!-- b000536 | references | pages [24] -->
directed influence network

<!-- b000537 | references | pages [24] -->
among artists can be

<!-- b000538 | references | pages [24] -->
Discrete Fourier Transform

<!-- b000539 | references | pages [24] -->
established. Our work

<!-- b000540 | references | pages [24] -->
analyzes this network in

<!-- b000541 | references | pages [24] -->
detail, and obtains the

<!-- b000542 | references | pages [24] -->
quantified influence values.

<!-- b000543 | references | pages [24] -->
At the same time, the

<!-- b000544 | references | pages [24] -->
similarity distribution within

<!-- b000545 | references | pages [24] -->
and between genres of is

<!-- b000546 | references | pages [24] -->
also analyzed.  The results

<!-- b000547 | references | pages [24] -->
show that the similarity

<!-- b000548 | references | pages [24] -->
within genres is generally

<!-- b000549 | references | pages [24] -->
larger than that between-

<!-- b000550 | references | pages [24] -->
genre similarity.  We

<!-- b000551 | references | pages [24] -->
obtained the representative

<!-- b000552 | references | pages [24] -->
vector of each genre that

<!-- b000553 | references | pages [24] -->
synthesized the music

<!-- b000554 | references | pages [24] -->
characteristics. The

<!-- b000555 | references | pages [24] -->
synthesized data has been

<!-- b000556 | references | pages [24] -->
tested to be indeed

<!-- b000557 | references | pages [24] -->
representative.  Based on

<!-- b000558 | references | pages [24] -->
the synthesized result, we

<!-- b000559 | references | pages [24] -->
detected the main

<!-- b000560 | references | pages [24] -->
differentiating factors

<!-- b000561 | references | pages [24] -->
between different genres.

<!-- b000562 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000563 | references | pages [24] -->
However, due to the

<!-- b000564 | references | pages [24] -->
limited data, our analysis

<!-- b000565 | references | pages [24] -->
of certain types of music

<!-- b000566 | references | pages [24] -->
may not be sufficient.

<!-- b000567 | references | pages [24] -->
With more data, we can

<!-- b000568 | references | pages [24] -->
In fact, based on these

<!-- b000569 | references | pages [24] -->
have more effective

<!-- b000570 | references | pages [24] -->
data, we have also

<!-- b000571 | references | pages [24] -->
information in the

<!-- b000572 | references | pages [24] -->
analyzed results other

<!-- b000573 | references | pages [24] -->
network analysis.  Since

<!-- b000574 | references | pages [24] -->
than similarity and

<!-- b000575 | references | pages [24] -->
our model mainly use the

<!-- b000576 | references | pages [24] -->
influence.  For

<!-- b000577 | references | pages [24] -->
matrix-based linear

<!-- b000578 | references | pages [24] -->
example, we can

<!-- b000579 | references | pages [24] -->
calculation, the

<!-- b000580 | references | pages [24] -->
analyze the

<!-- b000581 | references | pages [24] -->
increased number of

<!-- b000582 | references | pages [24] -->
revolutionary

<!-- b000583 | references | pages [24] -->
data will not significantly

<!-- b000584 | references | pages [24] -->
musicians by finding

<!-- b000585 | references | pages [24] -->
increase the

<!-- b000586 | references | pages [24] -->
the important nodes by

<!-- b000587 | references | pages [24] -->
computational

<!-- b000588 | references | pages [24] -->
closeness centrality in

<!-- b000589 | references | pages [24] -->
complexity.  In addition,

<!-- b000590 | references | pages [24] -->
the network. We have

<!-- b000591 | references | pages [24] -->
when there is a larger

<!-- b000592 | references | pages [24] -->
also established a

<!-- b000593 | references | pages [24] -->
order of magnitude of

<!-- b000594 | references | pages [24] -->
model for analyzing

<!-- b000595 | references | pages [24] -->
data, our model still

<!-- b000596 | references | pages [24] -->
dynamic influence

<!-- b000597 | references | pages [24] -->
retains computational

<!-- b000598 | references | pages [24] -->
indicators, and

<!-- b000599 | references | pages [24] -->
advantages.  For

<!-- b000600 | references | pages [24] -->
correspondingly, we

<!-- b000601 | references | pages [24] -->
example, the proposed

<!-- b000602 | references | pages [24] -->
have analyzed the

<!-- b000603 | references | pages [24] -->
MRDE framework can

<!-- b000604 | references | pages [24] -->
dynamic process of the

<!-- b000605 | references | pages [24] -->
take random tuple

<!-- b000606 | references | pages [24] -->
evolution for different

<!-- b000607 | references | pages [24] -->
selection to obtain the

<!-- b000608 | references | pages [24] -->
genres of music in the

<!-- b000609 | references | pages [24] -->
same effective similarity

<!-- b000610 | references | pages [24] -->
past 100 years.

<!-- b000611 | references | pages [24] -->
distribution.

<!-- b000612 | furniture | pages [24] -->
关注数学模型

<!-- b000613 | furniture | pages [24] -->
2

<!-- b000614 | furniture | pages [24] -->
MATHmodels

<!-- b000615 | furniture | pages [24] -->
获取更多资讯
