# P-D-2021-2100112-1b2d1f1c

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen 2021 Control Number D MCM/ICM 2100112 Summary Sheet

<!-- b000002 | title | pages [1] -->
Music Influence and Evolution Analysis Based on Networks

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
“Music is like a psychiatrist. It will answer you with things people can’t tell you.” said the Beatles, one of the most famous Pop/Rock artist. In this paper, we deeply explore the magic of music - its influence network, evolution path, and effects on the culture.

<!-- b000005 | prose | pages [1] -->
For Task 1, we build a directed network between influencers and followers. Based on network theory, we proposed three different metrics - Degree Centrality, Weighted Degree Centrality and Eigen Centrality. Then we develop a combination of these metrics as a comprehensive measure of music influence. After that, we create a subnetwork to illustrate our influence measure.

<!-- b000006 | prose | pages [1] -->
For Task 2, we first preprocess the data using Principal Component Analysis to reduce dimension and collinearity. Then we define and calculate the distance between different tracks to obtain the similarity between artists. By calculating the average similarity, we apply Mann-Whitney test. Results show that with the probability of 62.8% and p-value smaller than 0.001, artists within a genre are more similar than those between genres.

<!-- b000007 | prose | pages [1] -->
For Task 3, according to proposed music similarity measure, we find that similarities and influences within and between genres differ greatly when we analyse different genres. To distinguish one genre from others, we build a Genre Classification Tree Model. By analysing the number of influencers in different period, we explore the evolution path of genres. Based on the directed network on genre scale, we find Pop/Rock has a strong relationship with R&B, Blues and Folk.

<!-- b000008 | prose | pages [1] -->
For Task 4, we build a Similarity Bayesian Network to identify the real followers based on the music characterstic similarity in tracks. Then we apply a multivariate two-sample mean test and find there is no strong evidence (p-value > 0.1) that any music characteristic are more “contagious” than others.

<!-- b000009 | prose | pages [1] -->
For Task 5, we first analyze the rise and decline of genres and find the music revolution in 1950s. We proposed a Dynamic Programming Algorithm to detect change points in music characteristics which are consistent with the revolution. Our results show that acousticness, energy, danceability and loudness might signify revolutions. Based on the Bayesian Network, Elvis Presley and Cliff Richard represent revolutionaires.

<!-- b000010 | prose | pages [1] -->
For Task 6, to get a further insight into the evolution in Pop/Rock, we propose an Dynamic Influencer Indicator based on the lagging trend in music characteristics of the whole genre. From 1960s to 2010s, there are 10 dynamic influencers, each has his/her unique influence on the genre. Moreover, we explain the evolution of Pop/Rock.

<!-- b000011 | prose | pages [1] -->
For Task 7, three important periods are detected based on time series analysis, which show the culture-influence of music. Based on the model established, we identify social changes like countercultural movement and technological changes such as the proliferation of the Internet.

<!-- b000012 | prose | pages [1] -->
At last, we conduct sensitivity analysis, which shows the robustness of our model. We also summerize the stengths and weaknesses and provide insights to ICM society about the evolution and cultural influence of music.

<!-- b000013 | keywords | pages [1] -->
Keywords: Directed Network; Bayesian Network; Change Points Analysis

<!-- b000014 | furniture | pages [1] -->
关注数学模型 获取更多资讯

<!-- b000015 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1 Introduction

<!-- b000018 | contents | pages [2] -->
3

<!-- b000019 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000020 | contents | pages [2] -->
2 Problem Restatement and Analysis

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
3 Assumptions and Notations

<!-- b000023 | contents | pages [2] -->
4

<!-- b000024 | contents | pages [2] -->
3.1

<!-- b000025 | contents | pages [2] -->
Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
4

<!-- b000027 | contents | pages [2] -->
3.2

<!-- b000028 | contents | pages [2] -->
Notations

<!-- b000029 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
5

<!-- b000031 | contents | pages [2] -->
4 Models and Solutions

<!-- b000032 | contents | pages [2] -->
5

<!-- b000033 | contents | pages [2] -->
4.1

<!-- b000034 | contents | pages [2] -->
Task 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [2] -->
5

<!-- b000036 | contents | pages [2] -->
4.1.1

<!-- b000037 | contents | pages [2] -->
Directed Inﬂuencer Network . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000038 | contents | pages [2] -->
5

<!-- b000039 | contents | pages [2] -->
4.1.2

<!-- b000040 | contents | pages [2] -->
Music Inﬂuence Measure . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
6

<!-- b000042 | contents | pages [2] -->
4.1.3

<!-- b000043 | contents | pages [2] -->
Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
7

<!-- b000045 | contents | pages [2] -->
4.2

<!-- b000046 | contents | pages [2] -->
Task 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
7

<!-- b000048 | contents | pages [2] -->
4.2.1

<!-- b000049 | contents | pages [2] -->
Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
7

<!-- b000051 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000052 | contents | pages [2] -->
4.2.2

<!-- b000053 | contents | pages [2] -->
Similarity Measure and Test . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
8

<!-- b000055 | contents | pages [2] -->
4.2.3

<!-- b000056 | contents | pages [2] -->
Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
9

<!-- b000058 | contents | pages [2] -->
4.3

<!-- b000059 | contents | pages [2] -->
Task 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
10

<!-- b000061 | contents | pages [2] -->
4.3.1

<!-- b000062 | contents | pages [2] -->
Genre Similarity and Inﬂuence . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
10

<!-- b000064 | contents | pages [2] -->
4.3.2

<!-- b000065 | contents | pages [2] -->
Genre Classiﬁcation Tree . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
10

<!-- b000067 | contents | pages [2] -->
4.3.3

<!-- b000068 | contents | pages [2] -->
Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
10

<!-- b000070 | contents | pages [2] -->
4.4

<!-- b000071 | contents | pages [2] -->
Task 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000072 | contents | pages [2] -->
13

<!-- b000073 | contents | pages [2] -->
4.4.1

<!-- b000074 | contents | pages [2] -->
Similarity Bayesian Network . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
13

<!-- b000076 | contents | pages [2] -->
4.4.2

<!-- b000077 | contents | pages [2] -->
Contagious Characteristic Test . . . . . . . . . . . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
14

<!-- b000079 | contents | pages [2] -->
4.4.3

<!-- b000080 | contents | pages [2] -->
Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
15

<!-- b000082 | contents | pages [2] -->
4.5

<!-- b000083 | contents | pages [2] -->
Task 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
16

<!-- b000085 | contents | pages [2] -->
4.5.1

<!-- b000086 | contents | pages [2] -->
Deﬁnition of Revolution . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
16

<!-- b000088 | contents | pages [2] -->
4.5.2

<!-- b000089 | contents | pages [2] -->
Change Points Detection (DP Algorithm) . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
16

<!-- b000091 | contents | pages [2] -->
4.5.3

<!-- b000092 | contents | pages [2] -->
Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000093 | contents | pages [2] -->
17

<!-- b000094 | contents | pages [2] -->
4.6

<!-- b000095 | contents | pages [2] -->
Task 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
19

<!-- b000097 | contents | pages [2] -->
4.6.1

<!-- b000098 | contents | pages [2] -->
Dynamic Inﬂuencer Indicator

<!-- b000099 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
19

<!-- b000101 | contents | pages [2] -->
4.6.2

<!-- b000102 | contents | pages [2] -->
Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
20

<!-- b000104 | contents | pages [2] -->
4.7

<!-- b000105 | contents | pages [2] -->
Task 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
21

<!-- b000107 | contents | pages [2] -->
4.7.1

<!-- b000108 | contents | pages [2] -->
Cultural Inﬂuence of music . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
21

<!-- b000110 | contents | pages [2] -->
4.7.2

<!-- b000111 | contents | pages [2] -->
Changes identiﬁed within the network . . . . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [2] -->
21

<!-- b000113 | contents | pages [2] -->
5 Sensitivity Analysis

<!-- b000114 | contents | pages [2] -->
22

<!-- b000115 | contents | pages [2] -->
6 Strengths and Weaknesses

<!-- b000116 | contents | pages [2] -->
23

<!-- b000117 | contents | pages [2] -->
6.1

<!-- b000118 | contents | pages [2] -->
Strengths

<!-- b000119 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000120 | contents | pages [2] -->
23

<!-- b000121 | contents | pages [2] -->
6.2

<!-- b000122 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000123 | contents | pages [2] -->
23

<!-- b000124 | contents | pages [2] -->
References

<!-- b000125 | contents | pages [2] -->
23

<!-- b000126 | contents | pages [2] -->
A Document to ICM Society

<!-- b000127 | contents | pages [2] -->
24

<!-- b000128 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000129 | contents | pages [2] -->
关注数学模型

<!-- b000130 | furniture | pages [2] -->
2

<!-- b000131 | furniture | pages [2] -->
MATHmodels

<!-- b000132 | furniture | pages [2] -->
获取更多资讯

<!-- b000133 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000134 | furniture | pages [3] -->
Team # 2100112

<!-- b000135 | furniture | pages [3] -->
Page 3 of 24

<!-- b000136 | heading | pages [3] -->
1 Introduction

<!-- b000137 | prose | pages [3] -->
Nowadays, various kinds of music has increasingly become an indispensable part of human 微信公众号：数学模型 life. Thousands of music artists inﬂuence each other and form a complex music inﬂuence network. While some genres show great similarity to each other, other genres are quite different in music characteristics. Some artists are passionate revolutionaries, who lead to an emergeence of a new genre or reinvention of an existing genre. Despite culture inﬂuence, the change of music characteristics of artists also indicate external events like the proliferation of the Internet. In order to further explore the music inﬂuence network and the role music has played on the society, it is necessary to quantify music evolution.

<!-- b000138 | heading | pages [3] -->
2 Problem Restatement and Analysis

<!-- b000139 | prose | pages [3] -->
• Task 1 requires us to build a complex network between inﬂuencers and followers based on dataset “inﬂunce_data.csv” and develop metrics to capture the music inﬂuence in the 微信号：MATHmodels network. The key to this problem is to deﬁne directed inﬂuencer network and propose metrics that comprehensively measure the music inﬂuence of each inﬂuencers in the net- work.

<!-- b000140 | prose | pages [3] -->
• Task 2 requires us to use various musical characteristics in dataset “full_music_data.csv” to measure music similarity and judge whether musicians in the same genre are more similar than those in different genres. It is of great essence to deﬁne the distance between music works of artists, from which we can obtain the similarities between artists.

<!-- b000141 | prose | pages [3] -->
• Task 3 requires us to compare similarities and inﬂuences between and within genres.

<!-- b000142 | prose | pages [3] -->
It is necessary to deﬁne the distance between genres and measure similarities between them. We plan to build a classication tree to distinguish one genre from others. Besides, we can show how genres changing over time and the relationship between genres using visualization.

<!-- b000143 | prose | pages [3] -->
• Task 4 requires us to get a further insight into the similarity of music characters between inﬂuencers and followers. We plan to build a Bayesian Network to ﬁnd the real inﬂu- encer and use hypothesis test to evaluate whether some music characteristics are more ‘contagious’ than others.

<!-- b000144 | prose | pages [3] -->
• Task 5 requires us to identify the characteristics and major artists that signify music evo- lution. To handle this problem, we propose a Change Point Detection model based on DP algorithm and match the change of music characters with the musical revolution. Then ﬁnd revolutionaries via Bayesian Network.

<!-- b000145 | prose | pages [3] -->
• Task 6 requires us to develop indicators to analyse dynamic inﬂuencers and corresponding inﬂuence processes of musical evolution in one genre. In this problem, we will focus on Pop/Rock and then discuss the major contributors to the Pop/Rock evolution through decades.

<!-- b000146 | prose | pages [3] -->
• Task 7 requires us to identify the effects of social, political, or technological changes within the network and ﬁnd the cultural inﬂuence of music. Based on time series analysis, we intend to ﬁnd the connection between the change in music characteristics and the external events. We also detect several culture-inﬂuence of music in different time or

<!-- b000147 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000148 | prose | pages [3, 4] -->
circumstances. 关注数学模型 The workﬂow of this paper is shown in Figure 1.

<!-- b000149 | furniture | pages [3] -->
2

<!-- b000150 | furniture | pages [3] -->
MATHmodels

<!-- b000151 | furniture | pages [3] -->
获取更多资讯

<!-- b000152 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000153 | furniture | pages [4] -->
Team # 2100112

<!-- b000154 | furniture | pages [4] -->
Page 4 of 24

<!-- b000156 | prose | pages [4] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000157 | caption | pages [4] -->
Figure 1: Workﬂow of the paper

<!-- b000158 | heading | pages [4] -->
3 Assumptions and Notations

<!-- b000159 | heading | pages [4] -->
3.1 Assumptions and Justiﬁcations

<!-- b000160 | prose | pages [4] -->
• The similarity of artists is represented by the similarity of their musical character- istics. In all available datasets, the most reliable souce of information about an artist’s characteristics is tracks he/she released. Therefore, it is reasonable to use musical char- acteristics to represent the characteristics of artists.

<!-- b000161 | prose | pages [4] -->
• The reinvention and revolution of exisiting genre can be can be signiﬁed by the sharp change in music characteristics. Revolution shifts in a genre will denitely change the music characteristics, thus we can capture revolutions based on these changes.

<!-- b000162 | prose | pages [4] -->
• In different stages of genre development, music characters changed with a linear trend over time. This assumption is a reasonable simpliﬁcation to make breakpoints identiﬁcation possible.

<!-- b000163 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000164 | prose | pages [4] -->
关注数学模型

<!-- b000165 | furniture | pages [4] -->
2

<!-- b000166 | furniture | pages [4] -->
MATHmodels

<!-- b000167 | furniture | pages [4] -->
获取更多资讯

<!-- b000168 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000169 | furniture | pages [5] -->
Team # 2100112

<!-- b000170 | furniture | pages [5] -->
Page 5 of 24

<!-- b000171 | heading | pages [5] -->
3.2 Notations

<!-- b000172 | prose | pages [5] -->
The primary notations are shown in Table 1.

<!-- b000173 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000174 | caption | pages [5] -->
Table 1: Notations

<!-- b000175 | prose | pages [5] -->
Symbol Deﬁnition

<!-- b000176 | prose | pages [5] -->
DCi the local inﬂuence Degree Centrality of i th inﬂuencer WDCi weighted degree centrality for i th inﬂuencer ECi eigen centrality for i th inﬂuencer F −Scorei the comprehensive score of i th inﬂuencer Simi,j music similarity between track i and track j Acvi,j absolute coefﬁcient of variation of music character j in genre i similarity score between artist A and artist B ρAB length of lagging year µ

<!-- b000177 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000178 | heading | pages [5] -->
4 Models and Solutions

<!-- b000179 | heading | pages [5] -->
4.1 Task 1

<!-- b000180 | heading | pages [5] -->
4.1.1 Directed Inﬂuencer Network

<!-- b000181 | prose | pages [5] -->
We consider inﬂuencers and followers as nodes and collect all musicians together to make up the set V = {vi}n i=1. If artist i has an inﬂuence on artist j, then an edge from node i to node j m  will be generated. All the edges make up the set E = ej j=1, and the edges from node i make up set N(i). Based on the dataset “inﬂunce_data.csv”, we build a complex network involving n=5603 nodes (artists) and m=42770 edges (inﬂuence) in total, as shown in Figure 2.

<!-- b000182 | caption | pages [5] -->
Figure 2: 3D Directed Inﬂuencer Network

<!-- b000183 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000184 | prose | pages [5] -->
关注数学模型

<!-- b000185 | furniture | pages [5] -->
2

<!-- b000186 | furniture | pages [5] -->
MATHmodels

<!-- b000187 | furniture | pages [5] -->
获取更多资讯

<!-- b000188 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000189 | furniture | pages [6] -->
Team # 2100112

<!-- b000190 | furniture | pages [6] -->
Page 6 of 24

<!-- b000191 | heading | pages [6] -->
4.1.2 Music Inﬂuence Measure

<!-- b000192 | prose | pages [6] -->
We now deﬁne some essential metrics to measure the music inﬂuence in the network.

<!-- b000193 | prose | pages [6] -->
Degree Centrality: Degree is an important concept in network theory. In directed graph, 微信公众号：数学模型 out degree of node v represents the number of edges from node v[1].

<!-- b000194 | prose | pages [6] -->
outdegreev = #N(v) (1)

<!-- b000195 | prose | pages [6] -->
A naive idea to measure the local importance of the node is the out degree of the node. In other words, we use the number of followers to measure the local inﬂuence of a musician. We call the local inﬂuence Degree Centrality and deﬁne the Degree Centrality of inﬂuencer i as follows:

<!-- b000196 | prose | pages [6] -->
DCi = outdegreei/n (2)

<!-- b000197 | prose | pages [6] -->
Where n is the number of nodes in the network.

<!-- b000198 | prose | pages [6] -->
Weighted Degree Centrality: Some genres interact with each other closely, while others seem to have little connection. As a result, we can’t treat all the inﬂuences equally, and the 微信号：MATHmodels edges of the network should share different weights. If a musician has an inﬂuence on artists of other genres, it means that the musician has a wide range of inﬂuence. Similarly, if a musician has an inﬂuence on future musical generations decades later, it indicates that the inﬂuence lasts for a long time. In the cases above, we align greater weight.

<!-- b000199 | prose | pages [6] -->
We deﬁne the genre of musician i as G(i). The yeargap between followers and inﬂuencers is deﬁned as the time difference between the start of their careers. When the yeargap exceeds the threshold, we call it long-time inﬂuence, otherwise short-time inﬂuence. Here we set the threshold = 20.

<!-- b000200 | prose | pages [6] -->
The weight matrix W = (Wij) is deﬁned by integrating inﬂuence range and inﬂuence dura- tion as follows:

<!-- b000201 | prose | pages [6] -->
1 3 ∗(1+I{S(i)̸=S(j)} +I{yeargap>threshold}), j ∈N(i) Wij = (3) 0, else

<!-- b000202 | prose | pages [6] -->
Then we propose the Weighted Degree Centrality (WDC) to modify the Degree Centrality above:

<!-- b000203 | prose | pages [6] -->
WDCi = 1 n∗< Wi,1n > (4)

<!-- b000204 | prose | pages [6] -->
Where Wi represent the ith row of matrix W, 1n is a column vectors with all entries 1. DC and WDC both measure the local inﬂuence of an inﬂuencer.

<!-- b000205 | prose | pages [6] -->
Eigen Centrality: The basic idea of Eigen Centrality is to regard the inﬂuence of a node as a function of local inﬂuence of its adjacent node. In other words, the higher inﬂuence the artist’s followers have on others, the greater the Eigen Centrality of the artist himself/herself is.

<!-- b000206 | prose | pages [6] -->
Eigen Centrality is deﬁned as follows:

<!-- b000207 | prose | pages [6] -->
ECi = 1 n∗< Wi,OD > (5)

<!-- b000208 | prose | pages [6] -->
Where OD = (outdegree1,outdegree2,...,outdegreen)T and Wi = (Wi1,Wi2,...,Win)T both de- note a column vector. Intuitively, Eigen Centrality proportionally allocate the Degree Centrality from adjacent nodes to all nodes, which seems to "spread out" the Degree Centrality.

<!-- b000209 | prose | pages [6] -->
Comprehensive F-Score: The three different degrees above measure the music inﬂuence

<!-- b000210 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000211 | prose | pages [6, 7] -->
of artists in the network in different aspects. In order to get the comprehensive measure of each关注数学模型 inﬂuencer, we use weighted sum of the three degrees. In order to measure relative values, each degree is divided by the corresponding maximum value before the weighted sum:

<!-- b000212 | furniture | pages [6] -->
2

<!-- b000213 | furniture | pages [6] -->
MATHmodels

<!-- b000214 | furniture | pages [6] -->
获取更多资讯

<!-- b000215 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000216 | furniture | pages [7] -->
Team # 2100112

<!-- b000217 | furniture | pages [7] -->
Page 7 of 24

<!-- b000219 | prose | pages [7] -->
DCi WDCi ECi F −Scorei = w1 ∗ k (DCk) +w2 ∗ k (WDCk) +w3 ∗ (6) 微信公众号：数学模型 max max max k (ECk)

<!-- b000220 | prose | pages [7] -->
F-score, as a combinaiton of all three metrics, comprihensively measures the music inﬂu- ence of each inﬂuencer in the complex network.

<!-- b000221 | heading | pages [7] -->
4.1.3 Solutions

<!-- b000222 | prose | pages [7] -->
Based on the music inﬂuence measurement F-score (here we set w1 = w2 = w3 = 1 3), we extracted 10 directed inﬂuencer subnetworks from the original network, as shown in Figure 3. All metrics of these 10 inﬂuencers is shown in Table 2. The size of the core in each small subnetwork indicates the music inﬂuence of the top artist. It is clear that the subnetwork shows a radial-structure, with a great artist as the center, connecting to his followers. 微信号：MATHmodels

<!-- b000223 | caption | pages [7] -->
Figure 3: Directed Inﬂuencer Subnetwork

<!-- b000224 | prose | pages [7] -->
Generally, artist with higher music inﬂuence has more followers. However, Howlin’ Wolf has less followers than Marvin Gaye, whereas has greater music inﬂuence. This is because followers of Howlin’ Wolf are more famous and inﬂuential.

<!-- b000225 | heading | pages [7] -->
4.2 Task 2

<!-- b000226 | heading | pages [7] -->
4.2.1 Data Preprocessing

<!-- b000227 | prose | pages [7] -->
First, we preprocess the dataset “full_music_data.csv”. There are 14 characteristics related to music included in dataset, including danceability, energy, loudness, etc. Through data visual- ization, we ﬁnd that the Boolean variable “Explicit” is invalid: Out of 98430 tracks, only 3647 tracks are marked as 1, which means less than 4% tracks have explicit lyrics. As it conﬂicts with common sense, we believe most lyrics in tracks remained undetected. Thus, we remove

<!-- b000228 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000229 | prose | pages [7, 8] -->
“Explicit” data. After that, we standardize all continuous variables. 关注数学模型 Id Name Genre DC WDC EC F-Score

<!-- b000230 | furniture | pages [7] -->
2

<!-- b000231 | furniture | pages [7] -->
MATHmodels

<!-- b000232 | furniture | pages [7] -->
获取更多资讯

<!-- b000233 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000234 | furniture | pages [8] -->
Team # 2100112

<!-- b000235 | furniture | pages [8] -->
Page 8 of 24

<!-- b000236 | caption | pages [8] -->
Table 2: Metrics of top 10 artists

<!-- b000238 | prose | pages [8] -->
754032 The Beatles Pop/Rock 0.11 0.14 2.3 1.00 微信公众号：数学模型 66915 Bob Dylan Pop/Rock 0.07 0.1 1.65 0.68 894465 The Rolling Stones Pop/Rock 0.06 0.07 1.24 0.52 549797 Hank Williams Country 0.03 0.07 1.57 0.49 531986 David Bowie Pop/Rock 0.04 0.06 0.71 0.37 354105 Jimi Hendrix Pop/Rock 0.04 0.05 0.94 0.37 128099 James Brown R&B 0.03 0.05 1.11 0.36 276085 Howlin’ Wolf Blues 0.02 0.04 1.3 0.35 316834 Marvin Gaye R&B 0.03 0.06 0.72 0.34 139026 Led Zeppelin Pop/Rock 0.04 0.05 0.65 0.34

<!-- b000239 | prose | pages [8] -->
Some of the music characteristics have similar meanings, for example, “energy” and “loud- ness” both reﬂect the intensity and activity of tracks. To reduce the inﬂuence of collinearity 微信号：MATHmodels when calculating similarity, we use PCA (Principal Component Analysis) to reduce the dimen- sion of the data while preserving as much of the data’s variation as possible. After calculation, the cumulative variance contribution rate is shown in Table 3.

<!-- b000240 | caption | pages [8] -->
Table 3: Cumulative Variance Contribution Rate

<!-- b000241 | prose | pages [8] -->
Number of Principal Component 1 2 3 4 5 6 7 8

<!-- b000242 | prose | pages [8] -->
Cumulative Variance Contribution Rate 0.23 0.37 0.49 0.59 0.67 0.74 0.81 0.85

<!-- b000243 | prose | pages [8] -->
Based on the result of PCA, we choose ﬁrst seven principal component and ignore the rest. The seven new variables maintain more than 80% information of the original data.

<!-- b000244 | heading | pages [8] -->
4.2.2 Similarity Measure and Test

<!-- b000245 | prose | pages [8] -->
Inspired by the Euclidean distance, we deﬁne music similarity between track i and track j as follows:

<!-- b000246 | prose | pages [8] -->
1 Simij = i, j = 1,2,...,m (7) q 2 ∑m   xit −xjt t=1

<!-- b000247 | prose | pages [8] -->
Comparing to other measures like Mahalanobis distance, this simple measure doesn’t need any assumption on data and is easy to calculate.

<!-- b000248 | prose | pages [8] -->
To explore whether artists in the same genre are more similar than those in different genres, we construct Mann-Whitney hypothesis test. Comparing to traditional tests such as two-sample t-test, Mann-Whitney statistic does not require distributional assumptions for its validity. In this problem, the distributions of music similarity within and between genres are quite far away from the normality. Thus, this statistic will bring about better results.

<!-- b000249 | prose | pages [8] -->
We ﬁrst calculate the average music similarity within genre and between genres, which can

<!-- b000250 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000251 | prose | pages [8, 9] -->
关注数学模型 be expressed as

<!-- b000252 | furniture | pages [8] -->
2

<!-- b000253 | furniture | pages [8] -->
MATHmodels

<!-- b000254 | furniture | pages [8] -->
获取更多资讯

<!-- b000255 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000256 | furniture | pages [9] -->
Team # 2100112

<!-- b000257 | furniture | pages [9] -->
Page 9 of 24

<!-- b000259 | prose | pages [9] -->
n Simin,i = 1 ∑ Simi j (8) n j=1 微信公众号：数学模型 m Simbet,i = 1 ∑ Simik (9) m k=1

<!-- b000260 | prose | pages [9] -->
where j, k denote individual in the same genre and different genres with artist i, and n, m denote number of above individuals, respectively.

<!-- b000261 | prose | pages [9] -->
Then we calculate Mann-Whitney statistic as:

<!-- b000262 | prose | pages [9] -->
n+m n+m 1    U = Simin,i < Simbet,j ∑ ∑ I (10) (n+m)2 i=1 j=1

<!-- b000263 | prose | pages [9] -->
U−1 2nm Based on Central Limit Theorem, the asymptotic distribution of Z = 12nm(n+m+1) is normal 1 微信号：MATHmodels distribution[4]. Based on this, we can construct Mann-Whitney Test to ﬁnd out whether artists within a genre are more similar than those between genres.

<!-- b000264 | heading | pages [9] -->
4.2.3 Solutions

<!-- b000265 | prose | pages [9] -->
Similarity between all artists are shown in Figure 4. Mann-Whitney statistic shows that with a probability of 62.8% and p-value smaller than 0.001, artists within genre are more similar than those between genres.

<!-- b000266 | caption | pages [9] -->
Figure 4: Similarity between artists within a genre and between genres

<!-- b000267 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000268 | prose | pages [9] -->
关注数学模型

<!-- b000269 | furniture | pages [9] -->
2

<!-- b000270 | furniture | pages [9] -->
MATHmodels

<!-- b000271 | furniture | pages [9] -->
获取更多资讯

<!-- b000272 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000273 | furniture | pages [10] -->
Team # 2100112

<!-- b000274 | furniture | pages [10] -->
Page 10 of 24

<!-- b000275 | heading | pages [10] -->
4.3 Task 3

<!-- b000276 | heading | pages [10] -->
4.3.1 Genre Similarity and Inﬂuence

<!-- b000277 | prose | pages [10] -->
微信公众号：数学模型 To compare music similarity and inﬂuence on the genre level, we ﬁrst merge genre in dataset “inﬂunce_data.csv” to dataset “data_by_artist.csv”, then we group the data by different genres.

<!-- b000278 | prose | pages [10] -->
We deﬁne the similarity between genres as

<!-- b000279 | prose | pages [10] -->
1 Simij = i, j = 1,2,...,ng (11) q ng 2   cik −cjk ∑ k=1

<!-- b000280 | prose | pages [10] -->
where ng is the number of genres, cik is the kth average music characteristic value in genre i.

<!-- b000281 | prose | pages [10] -->
To evaluate the similarity within genres, we calculate the Absolute Coefﬁcient of Variation of each music character in different genres, which quantiﬁes the variation of some characteris- tics within genres. Let Acvij denote the Absolute Coefﬁcient of Variation of music character j in genre i, then: 微信号：MATHmodels r 2  1 1 xjk − #G(i) ∑k∈G(i) xjk #G(i) ∑k∈G(i) Acvij = (12) 1 | #G(i) ∑k∈G(i) xjk|

<!-- b000282 | prose | pages [10] -->
where xjk denotes the music character j of the artist k. By averaging the Acv of all continues music characters, we obtain the Average Absolute Coefﬁcient of Variation for each genre.

<!-- b000283 | heading | pages [10] -->
4.3.2 Genre Classiﬁcation Tree

<!-- b000284 | prose | pages [10] -->
According to our assumption, when we distinguish one genre from another, the main dif- ference lies in the creation styles - the various features of the music created by the artists. Considering each genre has its unique style, we separately analyze the distinguishing features of each genre.

<!-- b000285 | prose | pages [10] -->
Classiﬁcation tree can distinguish the relative importance of features: A feature closer to the root node is more important than those closer to the leave node. The speciﬁc steps to construct a Genre Classﬁcation Tree are listed as follows:

<!-- b000286 | prose | pages [10] -->
1. Identify the genre to be analyzed. Mark the artists in the genre as positive and the remaining artists as negative.

<!-- b000287 | heading | pages [10] -->
2. Construct the classiﬁcation tree and choose the appropriate tree size to keep the simplicity

<!-- b000288 | prose | pages [10] -->
of the classiﬁcation standard.

<!-- b000289 | prose | pages [10] -->
3. Sort the importance of features according to their relative position in the tree, visualize the tree and offer distinguishing strategy to identify the genre from others.

<!-- b000290 | heading | pages [10] -->
4.3.3 Solutions

<!-- b000291 | caption | pages [10] -->
Figure 12 shows the Similarity Matrix and Inﬂuence Matrix between Genres. Blues and

<!-- b000292 | prose | pages [10] -->
Easy Listening share some similar characteristics in musical features, whereas Electronic and Vocal are more similar. As for inﬂuence, Pop/Rock signiﬁcantly inﬂuences other genres. Inter- estingly, Pop/Rock has a strong inﬂuence on R&B, but they do not share signiﬁcant similarity

<!-- b000293 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000294 | prose | pages [10] -->
关注数学模型 in musical characteristics, which we will discuss the reason later.

<!-- b000295 | furniture | pages [10] -->
2

<!-- b000296 | furniture | pages [10] -->
MATHmodels

<!-- b000297 | furniture | pages [10] -->
获取更多资讯

<!-- b000298 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000299 | furniture | pages [11] -->
Team # 2100112

<!-- b000300 | furniture | pages [11] -->
Page 11 of 24

<!-- b000301 | prose | pages [11] -->
微信公众号：数学模型 (a) Inﬂuence between and within genres (b) Similarity between genres

<!-- b000302 | caption | pages [11] -->
Figure 5: Inﬂuence and Similarity between and within genres

<!-- b000303 | caption | pages [11] -->
Figure 6 and Figure 12a show the similarity and inﬂuence within a genre. Some genres like

<!-- b000304 | prose | pages [11] -->
微信号：MATHmodels R&B and Country have more variation within the genre than others, which indicates artist’s desire for true freedom of expression.At the same time, Pop/Rock and Jazz have a greater inﬂu- ence on themselves than others, which means they tend to maintain a consistent style.

<!-- b000305 | caption | pages [11] -->
Figure 6: Similarity within genres

<!-- b000306 | prose | pages [11] -->
Set R&B as an example, we construct classﬁcation tree as shown in Figure 7. danceabil- ity, duration and instrumentalness are vital features that distinguish R&B from other genres. Based on this approach, we can ﬁnd the vital features of every genre.

<!-- b000307 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000308 | prose | pages [11, 12] -->
关注数学模型 微信公众号：数学模型

<!-- b000309 | furniture | pages [11] -->
2

<!-- b000310 | furniture | pages [11] -->
MATHmodels

<!-- b000311 | furniture | pages [11] -->
获取更多资讯

<!-- b000312 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000313 | furniture | pages [12] -->
Team # 2100112

<!-- b000314 | furniture | pages [12] -->
Page 12 of 24

<!-- b000316 | caption | pages [12] -->
Figure 7: R&B Classiﬁcation tree

<!-- b000317 | prose | pages [12] -->
微信号：MATHmodels We use dataset “inﬂuence_data.csv” to depict how genres change over time. Based on the number of inﬂuencers in different genres through different time period, we draw Figure 8. As shown in the ﬁgure. Blues and Jazz ﬂourished from 1930s to 1950s, and then met a smooth decline. On the other hand, Country kept popular from 1930s to 1990s. Pop/Rock, similar to R&B, thrived between 1960s and 1990s.

<!-- b000318 | caption | pages [12] -->
Figure 8: Genres changing over time (Part)

<!-- b000319 | prose | pages [12] -->
To further explore the relationship between different genres, we construct a directed genre network based on the Inﬂuence matrix, as shown in Figure 9. Intuitively, if a genre is closely related to another, artists tend to have a great inﬂuence on each other’s tracks. Therefore, we consider “music inﬂuence” as the major measure of relationship.

<!-- b000320 | prose | pages [12] -->
The Genre Network illustrates that Pop/Rock artists have a great inﬂuence on many other genres, especially R&B, Blues and Folk etc., relating these genres together. In addition, Pop/Rock artists are deeply inﬂuenced by Electronic. Learning from Pop/Rock Musicians, artists in R&B have a number of interactions with artists in Avant-Grade.

<!-- b000321 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000322 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000323 | furniture | pages [12] -->
2

<!-- b000324 | furniture | pages [12] -->
MATHmodels

<!-- b000325 | furniture | pages [12] -->
获取更多资讯

<!-- b000326 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000327 | furniture | pages [13] -->
Team # 2100112

<!-- b000328 | furniture | pages [13] -->
Page 13 of 24

<!-- b000330 | caption | pages [13] -->
Figure 9: Genre Network

<!-- b000331 | heading | pages [13] -->
4.4 Task 4

<!-- b000332 | heading | pages [13] -->
4.4.1 Similarity Bayesian Network

<!-- b000333 | prose | pages [13] -->
This subsection aims to explore whether so-called ‘inﬂuencers’ truly have an inﬂuence on music created by ‘followers’, in other words, whether there is a signiﬁcant similarity between inﬂuencers’ music and pieces created by their followers.

<!-- b000334 | prose | pages [13] -->
To tackle this problem, we construct a Bayesian network based on similarity data. Here we deﬁne the similarity score between artist A and artist B as

<!-- b000335 | prose | pages [13] -->
∑nc ¯ ¯      ChaAi − ChaBi − ChaA ChaB i ρAB = (13) q 2 ∑nc 2 ∑nc ¯ ¯     ChaAi − ChaBi − ChaA ChaB i i

<!-- b000336 | prose | pages [13] -->
which has similar form to Pearson correlation, nc denotes the number of music characteristics, ¯ ChaAi denotes ith standardized music characteristic score of artist A, and ChaAi denotes the mean.

<!-- b000337 | prose | pages [13] -->
In our Bayesian Network, nodes denote artists, edges denote similarity scores. According to Fisher Z-Test[2], if A and B doesn’t have any similarity given C, then

<!-- b000338 | prose | pages [13] -->
p log1+ρAB|C n−|ChaC|−3 →N (0,1) (14) 1−ρAB|C 2

<!-- b000339 | prose | pages [13] -->
Based on the asymptotic distribution, we can calculate the similarity score between any two artists, then construct a Similarity Bayesian network. However, this traversal algorithm has NP problem. Therefore, we used Hill-Climbing algorithm with Random Starts instead. Deﬁne the Bayesian information as

<!-- b000340 | prose | pages [13] -->
nc logfAi (Ai|ΠAi)−d BIC = ∑ 2log(n) (15)

<!-- b000341 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000342 | prose | pages [13] -->
i=1 关注数学模型

<!-- b000343 | furniture | pages [13] -->
2

<!-- b000344 | furniture | pages [13] -->
MATHmodels

<!-- b000345 | furniture | pages [13] -->
获取更多资讯

<!-- b000346 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000347 | furniture | pages [14] -->
Team # 2100112

<!-- b000348 | furniture | pages [14] -->
Page 14 of 24

<!-- b000349 | heading | pages [14] -->
Algorithm 1 Similarity Bayesian Network

<!-- b000350 | prose | pages [14] -->
while i ≤Max_RandomNumber do Randomly generate a Similarity Bayesian network Calculate BIC_init 微信公众号：数学模型 BIC_best ←BIC_init while j ≤Max_iterations do Randomly choose add or delete an edge Calculate BIC_new if BIC_new ≤BIC_best then Net_best ←CurrentBayesianNetwork BIC_best ←BIC_new end if end while end while Rank the BIC_best of each i and ﬁnd the best Similarity Bayesian network Postprocess results and visualization 微信号：MATHmodels Where logfAi (Ai|ΠAi) is the conditional density function, the pseudocode of the algorithm is shown as follows:

<!-- b000351 | prose | pages [14] -->
To improve the stability of the solution, we use bootstrap method to calculate 500 different solutions and take an average.

<!-- b000352 | heading | pages [14] -->
4.4.2 Contagious Characteristic Test

<!-- b000353 | prose | pages [14] -->
In this subsection we analyse if some music characteristics are more‘contagious’ than others, or they all have similar roles in inﬂuencing a particular artist’s music. Based on the results in the last subsection, we tackle this task by analyzing The Beatles and their major followers: The Beach Boys, Led Zeppelin, Gram Parsons and David Bowie.

<!-- b000354 | prose | pages [14] -->
To ﬁnd out if there exists characteristics signiﬁcantly more contagious than others, we apply multivariate two-sample test[3]. The null hypothesis H0 is

<!-- b000355 | prose | pages [14] -->
H0 : µ1 = µ2 (16)

<!-- b000356 | prose | pages [14] -->
Where µ1 denotes the average music characteristic vector of all tracks released by The Beatles. µ2 denote the average music characteristic vecter of one of their followers.

<!-- b000357 | prose | pages [14] -->
According to asymptotic statistic theory, when p is ﬁxed and n tends to inﬁnity, by the Central Limit Theorem and Slutsky Theorem:

<!-- b000358 | prose | pages [14] -->
−1 S1 + S2 ( ¯X −¯Y)T ( ¯X −¯Y) →χ2(p) (17) n1 n2 where ¯X and ¯Y denote the sample mean respectively, and S1 and S2 denote the sample covariance matrix respectively.

<!-- b000359 | prose | pages [14] -->
Since the number of music characteristic (p = 9) is much smaller than the sample size, we do not need to make any distribution assumption for the data. The Chi-squared statistic follows a Chi-squared distribution with 9 degrees of freedom. By calculating the statistic, we can obtain the p-value according to the asymptotic distribution.

<!-- b000360 | prose | pages [14] -->
If the null hypothesis is accepted, we conclude that all music characteristics of followers are

<!-- b000361 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000362 | prose | pages [14, 15] -->
equally similar to their inﬂuencer, indicating no characteristics are signiﬁcantly ‘contagious’.关注数学模型 On the other hand, if the null hypothesis is rejected, we can further apply BH multiple hypoth- esis testing to further ﬁnd out which characteristic is more ‘contagious’.

<!-- b000363 | furniture | pages [14] -->
2

<!-- b000364 | furniture | pages [14] -->
MATHmodels

<!-- b000365 | furniture | pages [14] -->
获取更多资讯

<!-- b000366 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000367 | furniture | pages [15] -->
Team # 2100112

<!-- b000368 | furniture | pages [15] -->
Page 15 of 24

<!-- b000370 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000371 | heading | pages [15] -->
4.4.3 Solutions

<!-- b000372 | prose | pages [15] -->
Without the loss of generality, we put our focus on the most popular band – The Beatles and their followers. Setting similarity score threshold as 0.21, the Similarity Bayesian Network of the Beatles and their 29 most popular followers is shown in Figure 10.

<!-- b000373 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000374 | caption | pages [15] -->
Figure 10: Similarity Bayesian Network of the Beatles and their followers

<!-- b000375 | prose | pages [15] -->
As shown in ﬁgure 10, directly or indirectly, 72% alleged ‘followers’ have similar compos- ing style to the Beatles, their ‘inﬂuencer’. However, 28 % artists who claim they are inﬂuenced have insigniﬁcant (lower than the threshold) similarity to their ‘inﬂuencer’. In other words, based on similarity data, nearly three out of ten artists aren’t affected by their so-called ‘inﬂu- encers’.

<!-- b000376 | caption | pages [15] -->
Table 4: Contagious Characteristic Test

<!-- b000377 | prose | pages [15] -->
Follower Name chi-square value p-value

<!-- b000378 | prose | pages [15] -->
Led Zeppelin 3.183 0.957 Gram Parsons 5.971 0.743 David Bowie 7.232 0.613 The Beach Boys 14.284 0.113

<!-- b000379 | prose | pages [15] -->
The results of Contagious Characteristic test is shown in Table 4. Under the signiﬁcant level of 5%, all four null hypotheses are accepted, which indicates that all musical characteris- tics of The Beatles equally inﬂuence its followers, in other words, no characteristics are more contagious and prominent than others.

<!-- b000380 | prose | pages [15] -->
we should emphasize that in the above process, Type I error may accumulate due to multiple hypothesis tests. However, in this problem, all hypotheses are accepted. Thus, Type I errors can still be controlled within the signiﬁcance level.

<!-- b000381 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000382 | prose | pages [15] -->
关注数学模型

<!-- b000383 | furniture | pages [15] -->
2

<!-- b000384 | furniture | pages [15] -->
MATHmodels

<!-- b000385 | furniture | pages [15] -->
获取更多资讯

<!-- b000386 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000387 | furniture | pages [16] -->
Team # 2100112

<!-- b000388 | furniture | pages [16] -->
Page 16 of 24

<!-- b000389 | heading | pages [16] -->
4.5 Task 5

<!-- b000390 | heading | pages [16] -->
4.5.1 Deﬁnition of Revolution

<!-- b000391 | prose | pages [16] -->
微信公众号：数学模型 To tackle task 5, we ﬁrst deﬁne “music revolution”. The number of inﬂuencers in major genres is shown in ﬁgure 11. As time went by, some genre ﬂourished and others went out of favor.

<!-- b000392 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000393 | caption | pages [16] -->
Figure 11: The number of inﬂuencers in major genres

<!-- b000394 | prose | pages [16] -->
We deﬁne the revolution time for genres as the time when there are some genres declined and others springing up or dominating. From Figure 11, we ﬁnd in the 1950s, Electronic ﬂourished gradually, while Vocal all went from boom to bust. The popularity of Pop/Rock and R&B also met a sharp increase. These phenomena indicate that 1950s is one of the revolution periods.

<!-- b000395 | prose | pages [16] -->
After deﬁning revolution periods, we focus on ﬁnding a signiﬁcant change point of music characteristics in the 1950s to explain what we discussed above. The key to this problem is turned to identify the change points in time series of the music features. Based on the change points we ﬁnd, we then can identify artists that represent the revolutionaries.

<!-- b000396 | heading | pages [16] -->
4.5.2 Change Points Detection (DP Algorithm)

<!-- b000397 | prose | pages [16] -->
We deﬁne the set of the change points as Θ = {θi}m i=1. Let the time series of some music character {Yt}n t=1 admit:

<!-- b000398 | prose | pages [16] -->
 t  Yt = ai +bi ∗ θi−1 +1 ≤t ≤θi +εt (18) n

<!-- b000399 | prose | pages [16] -->
Where ai is the intercept term, bi measures the speed of linear trend, and the error term εt is a white noise process.

<!-- b000400 | prose | pages [16] -->
In order to ensure that the stability of parameters and change points, we also need to limit

<!-- b000401 | prose | pages [16] -->
θi −θi−1 > τ (19)

<!-- b000402 | prose | pages [16] -->
and we suggest τ = [0.1n], which will be disucssed in detail in sensitivity analysis.

<!-- b000403 | prose | pages [16] -->
Since yt changes with a linear trend in different stages, when εi follows independent and identical distribution, it is apparent to estimate parameters by minimizing the sum of squared residuals.

<!-- b000404 | prose | pages [16] -->
n {θi}m (yt −byt)2 i=1 = argmin ∑ (20)关注数学模型

<!-- b000405 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000406 | prose | pages [16, 17] -->
θ∈Θ t=1 When the number of change points is given, the key of using Dynamic Programming algo- rithm in this problem is to establish the recursive relationship of the sum of squared residuals before and after a new change point is added.

<!-- b000407 | furniture | pages [16] -->
2

<!-- b000408 | furniture | pages [16] -->
MATHmodels

<!-- b000409 | furniture | pages [16] -->
获取更多资讯

<!-- b000410 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000411 | furniture | pages [17] -->
Team # 2100112

<!-- b000412 | furniture | pages [17] -->
Page 17 of 24

<!-- b000414 | prose | pages [17] -->
Let δ (m,n) denote the sum of squared residuals associated with the optimal partition con- 微信公众号：数学模型 taining m breaks using ﬁrst n observations, RSS(i, j) denote the sum of squared residuals ob- tained by applying least-squares to a segment start from i to j.

<!-- b000415 | prose | pages [17] -->
Then, we can achieve the global minimization of overall sum of squared residuals by solving recursive problem as follows:

<!-- b000416 | prose | pages [17] -->
mτ≤j≤n−τδ(m−1, j)+RSS(j +1,n) δ (m,n) = min (21)

<!-- b000417 | prose | pages [17] -->
where τ is a trimming parameter that constrains the distance between two change points not to be too close.

<!-- b000418 | prose | pages [17] -->
It is important to note that the DP algorithm is O(T 2) and does not depend on the number of change points. Therefore, we can quickly estimate all the change points which are consistent 微信号：MATHmodels for real ones[5].

<!-- b000419 | prose | pages [17] -->
Obviously, we also need to penalize the number of change points. Considering the number of change points as a tuning parameter, We recommend to use BIC criterion to determine the optimal number of change points m∗.

<!-- b000420 | prose | pages [17] -->
RSSoverall +log(n)∗ˆσ2 ∗m m∗= argmin (22) m

<!-- b000421 | heading | pages [17] -->
4.5.3 Solutions

<!-- b000422 | prose | pages [17] -->
(a) Energy (b) Acousticness

<!-- b000423 | caption | pages [17] -->
Figure 12: Change points detection of acousticness and energy

<!-- b000424 | prose | pages [17] -->
By using the DP algorithm above, we detected the change points of 11 continuous music characteristics in the dataset “data_by_year.csv”, as shown in table 5.

<!-- b000425 | prose | pages [17] -->
It can be seen in table 5 that four music characters (acousticness, energy, danceability and loudness) show signiﬁcant changes around 1950.

<!-- b000426 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000427 | prose | pages [17, 18] -->
关注数学模型 Revolution date

<!-- b000428 | furniture | pages [17] -->
2

<!-- b000429 | furniture | pages [17] -->
MATHmodels

<!-- b000430 | furniture | pages [17] -->
获取更多资讯

<!-- b000431 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000432 | furniture | pages [18] -->
Team # 2100112

<!-- b000433 | furniture | pages [18] -->
Page 18 of 24

<!-- b000434 | caption | pages [18] -->
Table 5: Revolution date of music characteristics

<!-- b000436 | prose | pages [18] -->
Characteristic 1930s 1940s 1950s 1960s 1970s 1980s 1990s 2000s 微信公众号：数学模型 Instrumentalness 1933 1946 - 1964 - - - - Duration_ms - 1946 - 1966 - - - 2007 1950 Acousticness - - 1964 1979 - - - Tempo - 1947 - - 1979 - 1996 2008 1950 Danceability - - - - - 1997 2008 Valence - 1947 - 1966 - - - 2005 1951 Energy - - - 1979 - - 2008 Liveness - - 1956 - 1976 - - 2008 Speechness - - 1956 - - - - 2006 Popularity - - 1953 - 1970 - - 2006 1950 Loudness 1936 - - - - - 2008

<!-- b000437 | prose | pages [18] -->
微信号：MATHmodels To get a further insight into the revolution related to music characteristics in different genres, we draw boxplots of energy and acousticness respectively in ﬁgure 13. Obviously, the new genres (Pop/Rock, R&B and Electronic) have signiﬁcant higher energy, yet their acousticness is much lower than the old ones. This is consistent with the time series analysis above. Thus, we convinced that the four music characters: acousticness, energy, danceability and loudness might signify revolutions in musical evolution.

<!-- b000438 | prose | pages [18] -->
(a) Energy (b) Acousticness

<!-- b000439 | caption | pages [18] -->
Figure 13: Energy and Acousticness in different genres

<!-- b000440 | prose | pages [18] -->
We deﬁne two types of revolutionaries: artists who make a major change to existing genres and artists who create a new genre. For the ﬁrst type, we focus on Pop/Rock, which shows a dramatic change in 1950s. For the second type, we put our emphasis on Electronic, which ﬁrst emerges in early 1950s.

<!-- b000441 | prose | pages [18] -->
To ﬁnd out revolutionaries in our network, we ﬁrst ﬁlter Pop/Rock and Electronic tracks released in 1950s, then build a Similarity Bayesian Network based on the artists of these tracks. Intuitively, artists at the core of our network are revolutionaries, as they have a major inﬂuence on artists during this period.

<!-- b000442 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000443 | prose | pages [18, 19] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000444 | furniture | pages [18] -->
2

<!-- b000445 | furniture | pages [18] -->
MATHmodels

<!-- b000446 | furniture | pages [18] -->
获取更多资讯

<!-- b000447 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000448 | furniture | pages [19] -->
Team # 2100112

<!-- b000449 | furniture | pages [19] -->
Page 19 of 24

<!-- b000451 | caption | pages [19] -->
Figure 14: Similarity Bayesian Network of Pop/Rock and Electronic in 1950s

<!-- b000452 | prose | pages [19] -->
Our Similarity Bayesian Network is shown in ﬁgure 14. Elvis Presley, an inﬂuencer who has the most followers in 1950s in Pop/Rock, leads a countercultural movement in the United States. At the same time, Cliff Richard, an English artist, makes a dramatic change on the evolution of the genre. These two revolutionaries not only reinvent the existing genre, but also inspire artists like Moti and Freestyle to create a new genre – Electronic. Therefore, Elvis Presley and Cliff Richard represent revolutionaries in 1950s music revolution.

<!-- b000453 | heading | pages [19] -->
4.6 Task 6

<!-- b000454 | heading | pages [19] -->
4.6.1 Dynamic Inﬂuencer Indicator

<!-- b000455 | prose | pages [19] -->
In this task, we choose Pop Rock as the genre for research since it exists for a long time and there are several reinventions.

<!-- b000456 | prose | pages [19] -->
Intuitively, dynamic inﬂuencers dramatically change the trend of the genre in a speciﬁc period of time. Thus a dynamic inﬂuencer of a period should satisfy

<!-- b000457 | prose | pages [19] -->
1. He/She released more than 10 tracks in this period.

<!-- b000458 | prose | pages [19] -->
2. The music characteristics of these tracks are consistent with the lagging trend of Pop/Rock.

<!-- b000459 | prose | pages [19] -->
Based on the deﬁnition above, we construct an indicator of dynamic inﬂuencer as

<!-- b000460 | prose | pages [19] -->
!1/2 di = 1 2   xi,j,t −¯xj,t−υ |Ai| ∑ ∑ (23) j∈F t∈Ai

<!-- b000461 | prose | pages [19] -->
where xi,j,t is the music characteristics j of tracks released by the ith artist in the year t, ¯xj,t is the average value of artists, F is the set of music characteristics, υ is the lag year. Here we set υ = 1 , which means the dynamic inﬂuencer will lead the music trend a year after tracks are

<!-- b000462 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000463 | prose | pages [19] -->
关注数学模型 released.

<!-- b000464 | furniture | pages [19] -->
2

<!-- b000465 | furniture | pages [19] -->
MATHmodels

<!-- b000466 | furniture | pages [19] -->
获取更多资讯

<!-- b000467 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000468 | furniture | pages [20] -->
Team # 2100112

<!-- b000469 | furniture | pages [20] -->
Page 20 of 24

<!-- b000470 | heading | pages [20] -->
4.6.2 Solutions

<!-- b000471 | prose | pages [20] -->
Changes of music characteristics in Pop/Rock are shown in ﬁgure 15 Preliminary data anal- ysis shows that most Pop/Rock songs are released after 1956 (the dotted line). Before 1956, the 微信公众号：数学模型 ﬂuctuation of musical characteristics is caused by small sample size. Therefore, we only an- alyze changes after 1956. We set F = {acousticness,danceability,energy,loudness,valence}, as only these characteristics show signiﬁcant ﬂuctuations after 1956.

<!-- b000472 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000473 | caption | pages [20] -->
Figure 15: Changes of music characteristics in Pop/Rock

<!-- b000474 | prose | pages [20] -->
By calculating the value of dynamic inﬂuencer indicator of 99 most famous artists, we ﬁnd out top 10 dynamic Inﬂuencers that have giant impact on Pop/Rock. The inﬂuencer and his/her active period is shown in ﬁgure 16.

<!-- b000475 | caption | pages [20] -->
Figure 16: Changes of music characteristics in Pop/Rock

<!-- b000476 | prose | pages [20] -->
According to the ﬁgure 15, Some music characteristics of Pop/Rock have changed a lot over time. Acousticness and valence both experience a signiﬁcant decline after 1956, while energy and loudness show a consistent increase.

<!-- b000477 | prose | pages [20] -->
The change above is mainly caused by the change of dynamic inﬂuencers. With the tech- nology enhancements and electrical ampliﬁcation, the Beatles, Led Zeppelin and Eagles poured more intense emotion and passion into Pop Rock music in the last century. These artists tend to express sadness or depressed emotions. However, in recent 20 years, some great musicians, like Lincoln Park and Taylor Swift, switched the tone of Pop Rock music from sadness to happiness.

<!-- b000478 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000479 | prose | pages [20] -->
关注数学模型 They make pop music smooth, relaxing and much more suitable for dancing.

<!-- b000480 | furniture | pages [20] -->
2

<!-- b000481 | furniture | pages [20] -->
MATHmodels

<!-- b000482 | furniture | pages [20] -->
获取更多资讯

<!-- b000483 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000484 | furniture | pages [21] -->
Team # 2100112

<!-- b000485 | furniture | pages [21] -->
Page 21 of 24

<!-- b000486 | heading | pages [21] -->
4.7 Task 7

<!-- b000487 | heading | pages [21] -->
4.7.1 Cultural Inﬂuence of music

<!-- b000488 | prose | pages [21] -->
微信公众号：数学模型 Based on the models in the previous section, we detect three important periods in musical evolution, as shown in ﬁgure 17. We discuss the culture-inﬂuence processes as follows:

<!-- b000489 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000490 | caption | pages [21] -->
Figure 17: Culture-inﬂuence processes

<!-- b000491 | prose | pages [21] -->
Period I (1935-1945): This Period was shaped by the moods of the Great Depression. In these period, lots of artists begin to create music with high energy and fast tempo, as shown in

<!-- b000492 | caption | pages [21] -->
Figure 17. Reinvention and fast growth of Pop/Rock and the glamorous beginning of Reggae

<!-- b000493 | prose | pages [21] -->
form an upward look of culture.

<!-- b000494 | prose | pages [21] -->
Period II (1950-1960): Following the detrimental effects of World War II, people was about to embark on a musical journey and substantially change the music style, valence and dance- ability saw a sharp increase in music released in this period – the golden age of Pop/Rock. The whole culture becomes hopeful and energetic.

<!-- b000495 | prose | pages [21] -->
Period III (1995-2005): By late 1995, many young people were getting tired of the Pop/rock were inundating the airwaves with, the energy and tempo of music reached the peak and began to decline. A mature music culture is gradually formed.

<!-- b000496 | heading | pages [21] -->
4.7.2 Changes identiﬁed within the network

<!-- b000497 | prose | pages [21] -->
Social and Political Changes: According to Similarity Bayesian Network of Pop/Rock artists in 1950s. As shown in ﬁgure 18, 1950s’ Pop/Rock is diversiﬁed in several subgenres, which are rather different from each other (as there are no edges between artists in different subgenres). This feature of network identiﬁes the countercultural movement in 1950s – people have increasing desire for true freedom of expression and the diversity of people become more and more prominent.

<!-- b000498 | prose | pages [21] -->
Technological Changes: According to the Wikipedia, we know that the emergence of the Internet mainly leads to the rise of the Electronic, as the Internet made it easier to spread the software for producing Electronic music. Such trends can be identiﬁed through change of num- bers of inﬂuencers in Electronic over time, as shown in ﬁgure 19. Inﬂuence reaches its peak due to the proliferation of the Internet.

<!-- b000499 | prose | pages [21] -->
Analysis above shows that based the models established, we can ﬁnd the cultural inﬂuence of music in time and circumstances, and identify the effects of social, political or technological

<!-- b000500 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000501 | prose | pages [21] -->
关注数学模型 changes.

<!-- b000502 | furniture | pages [21] -->
2

<!-- b000503 | furniture | pages [21] -->
MATHmodels

<!-- b000504 | furniture | pages [21] -->
获取更多资讯

<!-- b000505 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000506 | furniture | pages [22] -->
Team # 2100112

<!-- b000507 | furniture | pages [22] -->
Page 22 of 24

<!-- b000508 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000509 | caption | pages [22] -->
Figure 18: Familiarity Beyesian Network of Pop/Rock in 1950s

<!-- b000510 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000511 | caption | pages [22] -->
Figure 19: Number of inﬂuencers in Electronic

<!-- b000512 | heading | pages [22] -->
5 Sensitivity Analysis

<!-- b000513 | prose | pages [22] -->
In Task 5, our Change Point Detection model involves a trimming parameter τ, which might have an effect on optimal change points detection. To test the robustness of the model, we apply a change to the trimming parameter and check whether the revolutionary in 1950s can be well detected.

<!-- b000514 | caption | pages [22] -->
Table 6: Inﬂuence of τ on change point detection

<!-- b000515 | prose | pages [22] -->
τ

<!-- b000516 | prose | pages [22] -->
Characteristic [0.05n] [0.10n] [0.15n] [0.20n]

<!-- b000517 | prose | pages [22] -->
Acousticness 1950 1964 1979 1950 1964 1979 1950 1964 1979 1950 1964 1979 Danceability 1928 1951 1997 2008 1950 1997 2008 1950 1997 2008 1950 2008 Energy 1951 1983 1994 2008 1951 1979 2008 1951 1979 2008 1951 1979 2008 Loudness 1936 1951 1980 2008 1936 1950 2008 1935 1950 2008 1950 2008

<!-- b000518 | prose | pages [22] -->
As shown in table 6, the proposed model is very robust to change points when τ is greater

<!-- b000519 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000520 | prose | pages [22] -->
关注数学模型 than or equal to [0.1n], which implies the value we selected is reasonable.

<!-- b000521 | furniture | pages [22] -->
2

<!-- b000522 | furniture | pages [22] -->
MATHmodels

<!-- b000523 | furniture | pages [22] -->
获取更多资讯

<!-- b000524 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000525 | furniture | pages [23] -->
Team # 2100112

<!-- b000526 | furniture | pages [23] -->
Page 23 of 24

<!-- b000527 | heading | pages [23] -->
6 Strengths and Weaknesses

<!-- b000528 | heading | pages [23] -->
6.1 Strengths

<!-- b000529 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000530 | prose | pages [23] -->
• Effective models: For different problems, we build several models including Bayesian network, Change Point Detection model, which makes the analysis of each problem de- tailed and convincing.

<!-- b000531 | prose | pages [23] -->
• Statistical tests: Instead of simply comparing the value, we apply Mann-Whitney Test and Multivariate Mean Test to make our conclusions are reliable.

<!-- b000532 | prose | pages [23] -->
• Vivid visualizations: We use many ﬁgures to show our results, make it easier to capture the key information.

<!-- b000533 | heading | pages [23] -->
6.2 Weaknesses

<!-- b000534 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000535 | prose | pages [23] -->
• Our analysis does not cover all genres in some models. Given space limitations, part of our analysis mainly focuses on two representive genres: Pop Rock and R&B.

<!-- b000536 | prose | pages [23] -->
• We make a strong assumption on time series, which doen’t always hold in reality. We assume the error term follows independent normal distribution, however, it often follows a weakly dependent stationary process in reality.

<!-- b000537 | heading | pages [23] -->
References

<!-- b000538 | references | pages [23] -->
[1] Chen, Guanrong. Introduction to complex networks : Models, structures and dynamics

<!-- b000539 | references | pages [23] -->
[M]. Higher Education Press, 2012.

<!-- b000540 | references | pages [23] -->
[2] Lawley, D. N. "A generalization of Fisher’s z test." Biometrika 30.1/2 (1938): 180-187.

<!-- b000541 | references | pages [23] -->
[3] Rencher A C , Christensen W F . Methods of Multivariate Analysis[J]. Technometrics,

<!-- b000542 | references | pages [23] -->
2002, 38(443):76-77.

<!-- b000543 | references | pages [23] -->
[4] McKnight, Patrick E., and Julius Najab. "Mann-Whitney U Test." The Corsini encyclope-

<!-- b000544 | references | pages [23] -->
dia of psychology (2010): 1-1.

<!-- b000545 | references | pages [23] -->
[5] Bai J , Perron P . Computation and analysis of multiple structural change models[J]. Jour-

<!-- b000546 | references | pages [23] -->
nal of Applied Econometrics, 2003.

<!-- b000547 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000548 | references | pages [23] -->
关注数学模型

<!-- b000549 | furniture | pages [23] -->
2

<!-- b000550 | furniture | pages [23] -->
MATHmodels

<!-- b000551 | furniture | pages [23] -->
获取更多资讯

<!-- b000552 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000553 | furniture | pages [24] -->
Team # 2100112

<!-- b000554 | furniture | pages [24] -->
Page 24 of 24

<!-- b000555 | references | pages [24] -->
A Document to ICM Society

<!-- b000556 | references | pages [24] -->
To: Integrative Collective Music Society

<!-- b000557 | references | pages [24] -->
微信公众号：数学模型

<!-- b000558 | references | pages [24] -->
From: Team 2100112

<!-- b000559 | references | pages [24] -->
In this document, we will show you how our networks offer a better understanding of the

<!-- b000560 | references | pages [24] -->
inﬂuence of music, and potential improvement given richer data. In addition, we will give you

<!-- b000561 | references | pages [24] -->
some recommendation about the further study of music and its cultural inﬂuence.

<!-- b000562 | references | pages [24] -->
Our approach gives a comprehensive measure of an artist’s inﬂuence. We propose met-

<!-- b000563 | references | pages [24] -->
rics based on network theory - the Degree Centrality, the Weighted Degree Centrality and the

<!-- b000564 | references | pages [24] -->
Eigen Centrality. The music inﬂuence measure consider both the number and the popularity of

<!-- b000565 | references | pages [24] -->
followers, making it more close to the reality.

<!-- b000566 | references | pages [24] -->
Based on the Bayesian Network, our approach measures real connections between the inﬂu-

<!-- b000567 | references | pages [24] -->
encers and followers. Although some followers claim they are inﬂuence by the inﬂuencer, their

<!-- b000568 | references | pages [24] -->
tracks don’t show any signiﬁcant similarity to their inﬂencer’s. By applying our Bayes Network

<!-- b000569 | references | pages [24] -->
微信号：MATHmodels

<!-- b000570 | references | pages [24] -->
model, you can ﬁnd out “true” followers and have a more objective understanding of the music

<!-- b000571 | references | pages [24] -->
inﬂuence network between artists.

<!-- b000572 | references | pages [24] -->
Beneﬁted from detailed time series analysis, our approach offer a further insight of the rise

<!-- b000573 | references | pages [24] -->
and decline of genres and music revolution. We propose a dynamic programming algorithm to

<!-- b000574 | references | pages [24] -->
detect the change points in music characteristics and revolutions. Combined with the Dynamic

<!-- b000575 | references | pages [24] -->
Inﬂuencer Indicator, you will learn a lot about the evolution process of music.

<!-- b000576 | references | pages [24] -->
What’s more, our networks can be considerably improved if more data is introduced. Thanks

<!-- b000577 | references | pages [24] -->
to the strong learning ability of Bayesian Network, if more data are introduced (like the data

<!-- b000578 | references | pages [24] -->
with more genres or more music characteristics), we can get more accute parameter estimation,

<!-- b000579 | references | pages [24] -->
which will bring out better results.

<!-- b000580 | references | pages [24] -->
They are a lot of topics about music worth further investigating. For example, if we ﬁnd

<!-- b000581 | references | pages [24] -->
the music in some country is getting more and more energetic, then we can go to check if there

<!-- b000582 | references | pages [24] -->
are any social, political or technological changes, such as countercultural movements and the

<!-- b000583 | references | pages [24] -->
proliferation of the Internet. When music characteristics are changes, so does the society. For

<!-- b000584 | references | pages [24] -->
instance, The spread of positive music styles will form an upward look of culture.

<!-- b000585 | references | pages [24] -->
Hope you will ﬁnd our paper helpful and take our recommendations into consideration. We

<!-- b000586 | references | pages [24] -->
are looking forward to contributing our efforts to get deeper insight into music evolution.

<!-- b000587 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000588 | references | pages [24] -->
关注数学模型

<!-- b000589 | furniture | pages [24] -->
2

<!-- b000590 | furniture | pages [24] -->
MATHmodels

<!-- b000591 | furniture | pages [24] -->
获取更多资讯
