# P-D-2021-2100112-1b2d1f1c

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | prose | pages [1] -->
Control Number

<!-- b000003 | furniture | pages [1] -->
2021

<!-- b000004 | prose | pages [1] -->
Problem Chosen

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
D

<!-- b000007 | furniture | pages [1] -->
2100112

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
Music Inﬂuence and Evolution Analysis Based on Networks

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | title | pages [1] -->
微信公众号：数学模型

<!-- b000012 | prose | pages [1] -->
“Music is like a psychiatrist. It will answer you with things people can’t tell you.” said the Beatles, one of the most famous Pop/Rock artist. In this paper, we deeply explore the magic of music - its inﬂuence network, evolution path, and effects on the culture.

<!-- b000013 | prose | pages [1] -->
For Task 1, we build a directed network between inﬂuencers and followers. Based on net- work theory, we proposed three different metrics - Degree Centrality, Weighted Degree Central- ity and Eigen Centrality. Then we develop a combination of these metrics as a comprehensive measure of music inﬂuence. After that, we create a subnetwork to illustrate our inﬂuence mea- sure.

<!-- b000014 | prose | pages [1] -->
For Task 2, we ﬁrst preprocess the data using Principal Component Analysis to reduce dimension and collinearity. Then we deﬁne and calculate the distance between different tracks to obtain the similarity between artists. By calculating the average similarity, we apply Mann-

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
Whitney test. Results show that with the probability of 62.8% and p-value smaller than 0.001, artists within a genre are more similar than those between genres.

<!-- b000017 | prose | pages [1] -->
For Task 3, according to proposed music similarity measure, we ﬁnd that similarities and inﬂuences within and between genres differ greatly when we analyse different genres. To dis- tinguish one genre from others, we build a Genre Classiﬁcation Tree Model. By analysing the number of inﬂuencers in different period, we explore the evolution path of genres. Based on the directed network on genre scale, we ﬁnd Pop/Rock has a strong relationship with R&B, Blues and Folk.

<!-- b000018 | prose | pages [1] -->
For Task 4, we build a Similarity Bayesian Network to identify the real followers based on the music characterstic similarity in tracks. Then we apply a multivariate two-sample mean test and ﬁnd there is no strong evidence (p-value > 0.1) that any music characteristic are more “contagious” than others.

<!-- b000019 | prose | pages [1] -->
For Task 5, we ﬁrst analyze the rise and decline of genres and ﬁnd the music revolution in 1950s. We proposed a Dynamic Programming Algorithm to detect change points in music characteristics which are consistent with the revolution. Our results show that acousticness, energy, danceability and loudness might signify revolutions. Based on the Bayesian Network, Elvis Presley and Cliff Richard represent revolutionaires.

<!-- b000020 | prose | pages [1] -->
For Task 6, to get a further insight into the evolution in Pop/Rock, we propose an Dynamic Inﬂuencer Indicator based on the lagging trend in music characteristics of the whole genre. From 1960s to 2010s, there are 10 dynamic inﬂuencers, each has his/her unique inﬂuence on the genre. Moreover, we explain the evolution of Pop/Rock.

<!-- b000021 | prose | pages [1] -->
For Task 7, three important periods are detected based on time series analysis, which show the culture-inﬂuence of music. Based on the model established, we identify social changes like countercultural movement and technological changes such as the proliferation of the Internet.

<!-- b000022 | prose | pages [1] -->
At last, we conduct sensitivity analysis, which shows the robustness of our model. We also summerize the stengths and weaknesses and provide insights to ICM society about the evolution and cultural inﬂuence of music.

<!-- b000023 | keywords | pages [1] -->
Keywords: Directed Network; Bayesian Network; Change Points Analysis

<!-- b000024 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000025 | prose | pages [1] -->
关注数学模型

<!-- b000026 | furniture | pages [1] -->
2

<!-- b000027 | furniture | pages [1] -->
MATHmodels

<!-- b000028 | furniture | pages [1] -->
获取更多资讯

<!-- b000029 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000030 | heading | pages [2] -->
Contents

<!-- b000031 | contents | pages [2] -->
1

<!-- b000032 | heading | pages [2] -->
Introduction

<!-- b000033 | prose | pages [2] -->
3

<!-- b000034 | prose | pages [2] -->
微信公众号：数学模型

<!-- b000035 | prose | pages [2] -->
2 Problem Restatement and Analysis

<!-- b000036 | prose | pages [2] -->
3

<!-- b000037 | heading | pages [2] -->
Assumptions and Notations

<!-- b000038 | prose | pages [2] -->
3

<!-- b000039 | prose | pages [2] -->
4 Assumptions and Justiﬁcations . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000040 | heading | pages [2] -->
Notations

<!-- b000041 | prose | pages [2] -->
4

<!-- b000042 | heading | pages [2] -->
Models and Solutions

<!-- b000043 | prose | pages [2] -->
5

<!-- b000044 | prose | pages [2] -->
5 Task 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 5 Directed Inﬂuencer Network . . . . . . . . . . . . . . . . . . . . . . . 4.1.1 5 Music Inﬂuence Measure . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.2 6 Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1.3 7 Task 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 7 Data Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 7

<!-- b000045 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000046 | prose | pages [2] -->
Similarity Measure and Test . . . . . . . . . . . . . . . . . . . . . . . 4.2.2 8 Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.3 9 Task 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 10 Genre Similarity and Inﬂuence . . . . . . . . . . . . . . . . . . . . . . 4.3.1 10 Genre Classiﬁcation Tree . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.2 10 Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.3 10 Task 4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 13 Similarity Bayesian Network . . . . . . . . . . . . . . . . . . . . . . . 4.4.1 13 Contagious Characteristic Test . . . . . . . . . . . . . . . . . . . . . . 4.4.2 14 Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4.3 15 Task 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5 16 Deﬁnition of Revolution . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.1 16 Change Points Detection (DP Algorithm) . . . . . . . . . . . . . . . . 4.5.2 16 Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5.3 17 Task 6 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6 4.6.1 Dynamic Inﬂuencer Indicator 19 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | prose | pages [2] -->
19 Solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.6.2 20 Task 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.7 21 Cultural Inﬂuence of music . . . . . . . . . . . . . . . . . . . . . . . . 4.7.1 21 Changes identiﬁed within the network . . . . . . . . . . . . . . . . . . 4.7.2

<!-- b000048 | prose | pages [2] -->
5

<!-- b000049 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000050 | prose | pages [2] -->
6

<!-- b000051 | heading | pages [2] -->
Strengths and Weaknesses

<!-- b000052 | prose | pages [2] -->
21

<!-- b000053 | prose | pages [2] -->
22

<!-- b000054 | prose | pages [2] -->
23 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 Strengths 23 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2

<!-- b000055 | heading | pages [2] -->
References

<!-- b000056 | references | pages [2] -->
A Document to ICM Society

<!-- b000057 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000058 | references | pages [2] -->
23

<!-- b000059 | references | pages [2] -->
23

<!-- b000060 | references | pages [2] -->
24

<!-- b000061 | references | pages [2] -->
关注数学模型

<!-- b000062 | furniture | pages [2] -->
2

<!-- b000063 | furniture | pages [2] -->
MATHmodels

<!-- b000064 | furniture | pages [2] -->
获取更多资讯

<!-- b000065 | furniture | pages [3] -->
Team # 2100112

<!-- b000066 | references | pages [3] -->
1

<!-- b000067 | heading | pages [3] -->
Introduction

<!-- b000068 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000069 | furniture | pages [3] -->
Page 3 of 24

<!-- b000070 | prose | pages [3] -->
Nowadays, various kinds of music has increasingly become an indispensable part of human

<!-- b000071 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000072 | prose | pages [3] -->
life. Thousands of music artists inﬂuence each other and form a complex music inﬂuence network. While some genres show great similarity to each other, other genres are quite different in music characteristics. Some artists are passionate revolutionaries, who lead to an emergeence of a new genre or reinvention of an existing genre. Despite culture inﬂuence, the change of music characteristics of artists also indicate external events like the proliferation of the Internet. In order to further explore the music inﬂuence network and the role music has played on the society, it is necessary to quantify music evolution.

<!-- b000073 | prose | pages [3] -->
Problem Restatement and Analysis 2

<!-- b000074 | prose | pages [3] -->
• Task 1 requires us to build a complex network between inﬂuencers and followers based on dataset “inﬂunce_data.csv” and develop metrics to capture the music inﬂuence in the

<!-- b000075 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000076 | prose | pages [3] -->
network. The key to this problem is to deﬁne directed inﬂuencer network and propose metrics that comprehensively measure the music inﬂuence of each inﬂuencers in the net- work.

<!-- b000077 | prose | pages [3] -->
• Task 2 requires us to use various musical characteristics in dataset “full_music_data.csv” to measure music similarity and judge whether musicians in the same genre are more similar than those in different genres. It is of great essence to deﬁne the distance between music works of artists, from which we can obtain the similarities between artists.

<!-- b000078 | prose | pages [3] -->
• Task 3 requires us to compare similarities and inﬂuences between and within genres. It is necessary to deﬁne the distance between genres and measure similarities between them. We plan to build a classication tree to distinguish one genre from others. Besides, we can show how genres changing over time and the relationship between genres using visualization.

<!-- b000079 | prose | pages [3] -->
• Task 4 requires us to get a further insight into the similarity of music characters between inﬂuencers and followers. We plan to build a Bayesian Network to ﬁnd the real inﬂu- encer and use hypothesis test to evaluate whether some music characteristics are more ‘contagious’ than others.

<!-- b000080 | prose | pages [3] -->
• Task 5 requires us to identify the characteristics and major artists that signify music evo- lution. To handle this problem, we propose a Change Point Detection model based on DP algorithm and match the change of music characters with the musical revolution. Then ﬁnd revolutionaries via Bayesian Network.

<!-- b000081 | prose | pages [3] -->
• Task 6 requires us to develop indicators to analyse dynamic inﬂuencers and corresponding inﬂuence processes of musical evolution in one genre. In this problem, we will focus on Pop/Rock and then discuss the major contributors to the Pop/Rock evolution through decades.

<!-- b000082 | prose | pages [3] -->
• Task 7 requires us to identify the effects of social, political, or technological changes within the network and ﬁnd the cultural inﬂuence of music. Based on time series analysis, we intend to ﬁnd the connection between the change in music characteristics and the external events. We also detect several culture-inﬂuence of music in different time or

<!-- b000083 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000084 | prose | pages [3] -->
circumstances.

<!-- b000085 | prose | pages [3] -->
关注数学模型

<!-- b000086 | furniture | pages [3] -->
2

<!-- b000087 | furniture | pages [3] -->
MATHmodels

<!-- b000088 | furniture | pages [3] -->
获取更多资讯

<!-- b000089 | furniture | pages [4] -->
Team # 2100112

<!-- b000090 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000091 | furniture | pages [4] -->
Page 4 of 24

<!-- b000092 | prose | pages [4] -->
The workﬂow of this paper is shown in Figure 1.

<!-- b000093 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000094 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000095 | caption | pages [4] -->
Figure 1: Workﬂow of the paper

<!-- b000096 | prose | pages [4] -->
3

<!-- b000097 | heading | pages [4] -->
Assumptions and Notations

<!-- b000098 | prose | pages [4] -->
3.1

<!-- b000099 | heading | pages [4] -->
Assumptions and Justiﬁcations

<!-- b000100 | prose | pages [4] -->
• The similarity of artists is represented by the similarity of their musical character- istics. In all available datasets, the most reliable souce of information about an artist’s characteristics is tracks he/she released. Therefore, it is reasonable to use musical char- acteristics to represent the characteristics of artists.

<!-- b000101 | prose | pages [4] -->
• The reinvention and revolution of exisiting genre can be can be signiﬁed by the sharp change in music characteristics. Revolution shifts in a genre will denitely change the music characteristics, thus we can capture revolutions based on these changes.

<!-- b000102 | prose | pages [4] -->
• In different stages of genre development, music characters changed with a linear

<!-- b000103 | heading | pages [4] -->
trend over time. This assumption is a reasonable simpliﬁcation to make breakpoints

<!-- b000104 | prose | pages [4] -->
identiﬁcation possible.

<!-- b000105 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000106 | prose | pages [4] -->
关注数学模型

<!-- b000107 | furniture | pages [4] -->
2

<!-- b000108 | furniture | pages [4] -->
MATHmodels

<!-- b000109 | furniture | pages [4] -->
获取更多资讯

<!-- b000110 | furniture | pages [5] -->
Team # 2100112

<!-- b000111 | prose | pages [5] -->
3.2

<!-- b000112 | heading | pages [5] -->
Notations

<!-- b000113 | prose | pages [5] -->
The primary notations are shown in Table 1.

<!-- b000114 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000115 | furniture | pages [5] -->
Page 5 of 24

<!-- b000116 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000117 | caption | pages [5] -->
Table 1: Notations

<!-- b000118 | prose | pages [5] -->
Symbol Deﬁnition

<!-- b000119 | prose | pages [5] -->
DCi the local inﬂuence Degree Centrality of i th inﬂuencer WDCi weighted degree centrality for i th inﬂuencer ECi eigen centrality for i th inﬂuencer F −Scorei the comprehensive score of i th inﬂuencer Simi,j music similarity between track i and track j Acvi,j absolute coefﬁcient of variation of music character j in genre i similarity score between artist A and artist B ρAB length of lagging year µ

<!-- b000120 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000121 | prose | pages [5] -->
4

<!-- b000122 | heading | pages [5] -->
Models and Solutions

<!-- b000123 | prose | pages [5] -->
4.1 Task 1

<!-- b000124 | prose | pages [5] -->
4.1.1 Directed Inﬂuencer Network

<!-- b000125 | prose | pages [5] -->
We consider inﬂuencers and followers as nodes and collect all musicians together to make up the set V = {vi}n

<!-- b000126 | prose | pages [5] -->
i=1. If artist i has an inﬂuence on artist j, then an edge from node i to node j

<!-- b000127 | prose | pages [5] -->
m

<!-- b000128 | prose | pages [5] -->


<!-- b000129 | prose | pages [5] -->
will be generated. All the edges make up the set E =

<!-- b000130 | prose | pages [5] -->
ej

<!-- b000131 | prose | pages [5] -->
j=1, and the edges from node i make up set N(i). Based on the dataset “inﬂunce_data.csv”, we build a complex network involving n=5603 nodes (artists) and m=42770 edges (inﬂuence) in total, as shown in Figure 2.

<!-- b000132 | caption | pages [5] -->
Figure 2: 3D Directed Inﬂuencer Network

<!-- b000133 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000134 | prose | pages [5] -->
关注数学模型

<!-- b000135 | furniture | pages [5] -->
2

<!-- b000136 | furniture | pages [5] -->
MATHmodels

<!-- b000137 | furniture | pages [5] -->
获取更多资讯

<!-- b000138 | furniture | pages [6] -->
Team # 2100112

<!-- b000139 | prose | pages [6] -->
4.1.2 Music Inﬂuence Measure

<!-- b000140 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000141 | furniture | pages [6] -->
Page 6 of 24

<!-- b000142 | prose | pages [6] -->
We now deﬁne some essential metrics to measure the music inﬂuence in the network.

<!-- b000143 | prose | pages [6] -->
Degree Centrality: Degree is an important concept in network theory. In directed graph,

<!-- b000144 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000145 | prose | pages [6] -->
out degree of node v represents the number of edges from node v[1].

<!-- b000146 | prose | pages [6] -->
outdegreev = #N(v) (1)

<!-- b000147 | prose | pages [6] -->
A naive idea to measure the local importance of the node is the out degree of the node. In other words, we use the number of followers to measure the local inﬂuence of a musician. We call the local inﬂuence Degree Centrality and deﬁne the Degree Centrality of inﬂuencer i as follows:

<!-- b000148 | prose | pages [6] -->
DCi = outdegreei/n

<!-- b000149 | prose | pages [6] -->
Where n is the number of nodes in the network.

<!-- b000150 | prose | pages [6] -->
(2)

<!-- b000151 | prose | pages [6] -->
Weighted Degree Centrality: Some genres interact with each other closely, while others seem to have little connection. As a result, we can’t treat all the inﬂuences equally, and the

<!-- b000152 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000153 | prose | pages [6] -->
edges of the network should share different weights. If a musician has an inﬂuence on artists of other genres, it means that the musician has a wide range of inﬂuence. Similarly, if a musician has an inﬂuence on future musical generations decades later, it indicates that the inﬂuence lasts for a long time. In the cases above, we align greater weight.

<!-- b000154 | prose | pages [6] -->
We deﬁne the genre of musician i as G(i). The yeargap between followers and inﬂuencers is deﬁned as the time difference between the start of their careers. When the yeargap exceeds the threshold, we call it long-time inﬂuence, otherwise short-time inﬂuence. Here we set the threshold = 20.

<!-- b000155 | prose | pages [6] -->
The weight matrix W = (Wij) is deﬁned by integrating inﬂuence range and inﬂuence dura- tion as follows:

<!-- b000156 | prose | pages [6] -->
1

<!-- b000157 | prose | pages [6] -->
3 ∗(1+I{S(i)̸=S(j)} +I{yeargap>threshold}),

<!-- b000158 | prose | pages [6] -->
Wij =

<!-- b000159 | prose | pages [6] -->
0, j ∈N(i) (3) else

<!-- b000160 | prose | pages [6] -->
Then we propose the Weighted Degree Centrality (WDC) to modify the Degree Centrality above:

<!-- b000161 | prose | pages [6] -->
WDCi = 1

<!-- b000162 | prose | pages [6] -->
n∗< Wi,1n > (4)

<!-- b000163 | prose | pages [6] -->
Where Wi represent the ith row of matrix W, 1n is a column vectors with all entries 1. DC and WDC both measure the local inﬂuence of an inﬂuencer.

<!-- b000164 | prose | pages [6] -->
Eigen Centrality: The basic idea of Eigen Centrality is to regard the inﬂuence of a node as a function of local inﬂuence of its adjacent node. In other words, the higher inﬂuence the artist’s followers have on others, the greater the Eigen Centrality of the artist himself/herself is.

<!-- b000165 | prose | pages [6] -->
Eigen Centrality is deﬁned as follows:

<!-- b000166 | prose | pages [6] -->
ECi = 1

<!-- b000167 | prose | pages [6] -->
n∗< Wi,OD > (5)

<!-- b000168 | prose | pages [6] -->
Where OD = (outdegree1,outdegree2,...,outdegreen)T and Wi = (Wi1,Wi2,...,Win)T both de- note a column vector. Intuitively, Eigen Centrality proportionally allocate the Degree Centrality from adjacent nodes to all nodes, which seems to "spread out" the Degree Centrality.

<!-- b000169 | prose | pages [6] -->
Comprehensive F-Score: The three different degrees above measure the music inﬂuence

<!-- b000170 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000171 | prose | pages [6] -->
of artists in the network in different aspects. In order to get the comprehensive measure of each关注数学模型

<!-- b000172 | furniture | pages [6] -->
2

<!-- b000173 | furniture | pages [6] -->
MATHmodels

<!-- b000174 | furniture | pages [6] -->
获取更多资讯

<!-- b000175 | furniture | pages [7] -->
Team # 2100112

<!-- b000176 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000177 | furniture | pages [7] -->
Page 7 of 24

<!-- b000178 | prose | pages [7] -->
inﬂuencer, we use weighted sum of the three degrees. In order to measure relative values, each degree is divided by the corresponding maximum value before the weighted sum:

<!-- b000179 | prose | pages [7] -->
DCi F −Scorei = w1 ∗

<!-- b000180 | prose | pages [7] -->
WDCi

<!-- b000181 | prose | pages [7] -->
ECi

<!-- b000182 | prose | pages [7] -->
k (DCk) +w2 ∗

<!-- b000183 | prose | pages [7] -->
k (WDCk) +w3 ∗

<!-- b000184 | prose | pages [7] -->
(6)

<!-- b000185 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000186 | prose | pages [7] -->
max

<!-- b000187 | prose | pages [7] -->
k (ECk)

<!-- b000188 | prose | pages [7] -->
max

<!-- b000189 | prose | pages [7] -->
max

<!-- b000190 | prose | pages [7] -->
F-score, as a combinaiton of all three metrics, comprihensively measures the music inﬂu- ence of each inﬂuencer in the complex network.

<!-- b000191 | prose | pages [7] -->
4.1.3

<!-- b000192 | heading | pages [7] -->
Solutions

<!-- b000193 | prose | pages [7] -->
Based on the music inﬂuence measurement F-score (here we set w1 = w2 = w3 = 1

<!-- b000194 | prose | pages [7] -->
3), we extracted 10 directed inﬂuencer subnetworks from the original network, as shown in Figure 3. All metrics of these 10 inﬂuencers is shown in Table 2. The size of the core in each small subnetwork indicates the music inﬂuence of the top artist. It is clear that the subnetwork shows a radial-structure, with a great artist as the center, connecting to his followers.

<!-- b000195 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000196 | caption | pages [7] -->
Figure 3: Directed Inﬂuencer Subnetwork

<!-- b000197 | prose | pages [7] -->
Generally, artist with higher music inﬂuence has more followers. However, Howlin’ Wolf has less followers than Marvin Gaye, whereas has greater music inﬂuence. This is because followers of Howlin’ Wolf are more famous and inﬂuential.

<!-- b000198 | prose | pages [7] -->
4.2 Task 2

<!-- b000199 | prose | pages [7] -->
4.2.1 Data Preprocessing

<!-- b000200 | prose | pages [7] -->
First, we preprocess the dataset “full_music_data.csv”. There are 14 characteristics related to music included in dataset, including danceability, energy, loudness, etc. Through data visual- ization, we ﬁnd that the Boolean variable “Explicit” is invalid: Out of 98430 tracks, only 3647 tracks are marked as 1, which means less than 4% tracks have explicit lyrics. As it conﬂicts with common sense, we believe most lyrics in tracks remained undetected. Thus, we remove

<!-- b000201 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000202 | prose | pages [7] -->
“Explicit” data. After that, we standardize all continuous variables.

<!-- b000203 | prose | pages [7] -->
关注数学模型

<!-- b000204 | furniture | pages [7] -->
2

<!-- b000205 | furniture | pages [7] -->
MATHmodels

<!-- b000206 | furniture | pages [7] -->
获取更多资讯

<!-- b000207 | furniture | pages [8] -->
Team # 2100112

<!-- b000208 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000209 | furniture | pages [8] -->
Page 8 of 24

<!-- b000210 | caption | pages [8] -->
Table 2: Metrics of top 10 artists

<!-- b000211 | prose | pages [8] -->
Id Name Genre DC WDC EC F-Score

<!-- b000212 | prose | pages [8] -->
Pop/Rock 754032 The Beatles 0.11 0.14 2.3 1.00

<!-- b000213 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000214 | prose | pages [8] -->
Pop/Rock 66915 Bob Dylan 0.07 0.1 1.65 0.68 Pop/Rock 894465 The Rolling Stones 0.06 0.07 1.24 0.52 Country 549797 Hank Williams 0.03 0.07 1.57 0.49 Pop/Rock 531986 David Bowie 0.04 0.06 0.71 0.37 Pop/Rock 354105 Jimi Hendrix 128099 James Brown R&B 276085 Howlin’ Wolf Blues 316834 Marvin Gaye R&B 0.04 0.05 0.94 0.37 0.03 0.05 1.11 0.36 0.02 0.04 1.3 0.35 0.03 0.06 0.72 0.34 Pop/Rock 139026 Led Zeppelin 0.04 0.05 0.65 0.34

<!-- b000215 | prose | pages [8] -->
Some of the music characteristics have similar meanings, for example, “energy” and “loud- ness” both reﬂect the intensity and activity of tracks. To reduce the inﬂuence of collinearity

<!-- b000216 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000217 | prose | pages [8] -->
when calculating similarity, we use PCA (Principal Component Analysis) to reduce the dimen- sion of the data while preserving as much of the data’s variation as possible. After calculation, the cumulative variance contribution rate is shown in Table 3.

<!-- b000218 | caption | pages [8] -->
Table 3: Cumulative Variance Contribution Rate

<!-- b000219 | prose | pages [8] -->
Number of Principal Component 1

<!-- b000220 | prose | pages [8] -->
Cumulative Variance Contribution Rate 0.23

<!-- b000221 | prose | pages [8] -->
2 3 4 5 6 7 8

<!-- b000222 | prose | pages [8] -->
0.37 0.49 0.59 0.67 0.74 0.81 0.85

<!-- b000223 | prose | pages [8] -->
Based on the result of PCA, we choose ﬁrst seven principal component and ignore the rest. The seven new variables maintain more than 80% information of the original data.

<!-- b000224 | prose | pages [8] -->
4.2.2 Similarity Measure and Test

<!-- b000225 | prose | pages [8] -->
Inspired by the Euclidean distance, we deﬁne music similarity between track i and track j as follows:

<!-- b000226 | prose | pages [8] -->
1 Simij = q

<!-- b000227 | prose | pages [8] -->
∑m

<!-- b000228 | prose | pages [8] -->
 

<!-- b000229 | prose | pages [8] -->
xit −xjt

<!-- b000230 | prose | pages [8] -->
t=1

<!-- b000231 | prose | pages [8] -->
i, j = 1,2,...,m (7) 2

<!-- b000232 | prose | pages [8] -->
Comparing to other measures like Mahalanobis distance, this simple measure doesn’t need any assumption on data and is easy to calculate.

<!-- b000233 | prose | pages [8] -->
To explore whether artists in the same genre are more similar than those in different genres, we construct Mann-Whitney hypothesis test. Comparing to traditional tests such as two-sample t-test, Mann-Whitney statistic does not require distributional assumptions for its validity. In this problem, the distributions of music similarity within and between genres are quite far away from the normality. Thus, this statistic will bring about better results.

<!-- b000234 | prose | pages [8] -->
We ﬁrst calculate the average music similarity within genre and between genres, which can

<!-- b000235 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000236 | prose | pages [8] -->
关注数学模型

<!-- b000237 | furniture | pages [8] -->
2

<!-- b000238 | furniture | pages [8] -->
MATHmodels

<!-- b000239 | furniture | pages [8] -->
获取更多资讯

<!-- b000240 | furniture | pages [9] -->
Team # 2100112

<!-- b000241 | prose | pages [9] -->
be expressed as

<!-- b000242 | prose | pages [9] -->
Simin,i = 1

<!-- b000243 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000244 | furniture | pages [9] -->
Page 9 of 24

<!-- b000245 | prose | pages [9] -->
n ∑

<!-- b000246 | prose | pages [9] -->
Simi j (8)

<!-- b000247 | prose | pages [9] -->
n n

<!-- b000248 | prose | pages [9] -->
j=1

<!-- b000249 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000250 | prose | pages [9] -->
Simbet,i = 1

<!-- b000251 | prose | pages [9] -->
m ∑

<!-- b000252 | prose | pages [9] -->
Simik (9)

<!-- b000253 | prose | pages [9] -->
m m

<!-- b000254 | prose | pages [9] -->
k=1

<!-- b000255 | prose | pages [9] -->
where j, k denote individual in the same genre and different genres with artist i, and n, m denote number of above individuals, respectively.

<!-- b000256 | prose | pages [9] -->
Then we calculate Mann-Whitney statistic as:

<!-- b000257 | prose | pages [9] -->
n+m

<!-- b000258 | prose | pages [9] -->
n+m

<!-- b000259 | prose | pages [9] -->
1 U =

<!-- b000260 | prose | pages [9] -->
∑

<!-- b000261 | prose | pages [9] -->
∑

<!-- b000262 | prose | pages [9] -->
(n+m)2

<!-- b000263 | prose | pages [9] -->
i=1

<!-- b000264 | prose | pages [9] -->
j=1

<!-- b000265 | prose | pages [9] -->
 

<!-- b000266 | prose | pages [9] -->


<!-- b000267 | prose | pages [9] -->
Simin,i < Simbet,j

<!-- b000268 | prose | pages [9] -->
I

<!-- b000269 | prose | pages [9] -->
(10)

<!-- b000270 | prose | pages [9] -->
U−1

<!-- b000271 | prose | pages [9] -->
2nm

<!-- b000272 | prose | pages [9] -->
Based on Central Limit Theorem, the asymptotic distribution of Z =

<!-- b000273 | prose | pages [9] -->
12nm(n+m+1) is normal 1

<!-- b000274 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000275 | prose | pages [9] -->
distribution[4]. Based on this, we can construct Mann-Whitney Test to ﬁnd out whether artists within a genre are more similar than those between genres.

<!-- b000276 | prose | pages [9] -->
4.2.3

<!-- b000277 | heading | pages [9] -->
Solutions

<!-- b000278 | prose | pages [9] -->
Similarity between all artists are shown in Figure 4. Mann-Whitney statistic shows that with a probability of 62.8% and p-value smaller than 0.001, artists within genre are more similar than those between genres.

<!-- b000279 | caption | pages [9] -->
Figure 4: Similarity between artists within a genre and between genres

<!-- b000280 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000281 | prose | pages [9] -->
关注数学模型

<!-- b000282 | furniture | pages [9] -->
2

<!-- b000283 | furniture | pages [9] -->
MATHmodels

<!-- b000284 | furniture | pages [9] -->
获取更多资讯

<!-- b000285 | furniture | pages [10] -->
Team # 2100112

<!-- b000286 | prose | pages [10] -->
4.3 Task 3

<!-- b000287 | prose | pages [10] -->
4.3.1 Genre Similarity and Inﬂuence

<!-- b000288 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000289 | furniture | pages [10] -->
Page 10 of 24

<!-- b000290 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000291 | prose | pages [10] -->
To compare music similarity and inﬂuence on the genre level, we ﬁrst merge genre in dataset “inﬂunce_data.csv” to dataset “data_by_artist.csv”, then we group the data by different genres.

<!-- b000292 | prose | pages [10] -->
We deﬁne the similarity between genres as

<!-- b000293 | prose | pages [10] -->
1 Simij = q

<!-- b000294 | prose | pages [10] -->
ng

<!-- b000295 | prose | pages [10] -->
 

<!-- b000296 | prose | pages [10] -->
cik −cjk

<!-- b000297 | prose | pages [10] -->
∑

<!-- b000298 | prose | pages [10] -->
k=1

<!-- b000299 | prose | pages [10] -->
i, j = 1,2,...,ng (11) 2

<!-- b000300 | prose | pages [10] -->
where ng is the number of genres, cik is the kth average music characteristic value in genre i.

<!-- b000301 | prose | pages [10] -->
To evaluate the similarity within genres, we calculate the Absolute Coefﬁcient of Variation of each music character in different genres, which quantiﬁes the variation of some characteris- tics within genres. Let Acvij denote the Absolute Coefﬁcient of Variation of music character j in genre i, then:

<!-- b000302 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000303 | prose | pages [10] -->
r

<!-- b000304 | prose | pages [10] -->
1 #G(i) ∑k∈G(i)

<!-- b000305 | prose | pages [10] -->
Acvij =

<!-- b000306 | prose | pages [10] -->
1

<!-- b000307 | prose | pages [10] -->
2

<!-- b000308 | prose | pages [10] -->
 

<!-- b000309 | prose | pages [10] -->
1 xjk − #G(i) ∑k∈G(i) xjk

<!-- b000310 | prose | pages [10] -->
(12) #G(i) ∑k∈G(i) xjk| |

<!-- b000311 | prose | pages [10] -->
where xjk denotes the music character j of the artist k. By averaging the Acv of all continues music characters, we obtain the Average Absolute Coefﬁcient of Variation for each genre.

<!-- b000312 | prose | pages [10] -->
4.3.2 Genre Classiﬁcation Tree

<!-- b000313 | prose | pages [10] -->
According to our assumption, when we distinguish one genre from another, the main dif- ference lies in the creation styles - the various features of the music created by the artists. Considering each genre has its unique style, we separately analyze the distinguishing features of each genre.

<!-- b000314 | prose | pages [10] -->
Classiﬁcation tree can distinguish the relative importance of features: A feature closer to the root node is more important than those closer to the leave node. The speciﬁc steps to construct a Genre Classﬁcation Tree are listed as follows:

<!-- b000315 | heading | pages [10] -->
1. Identify the genre to be analyzed. Mark the artists in the genre as positive and the remaining

<!-- b000316 | prose | pages [10] -->
artists as negative.

<!-- b000317 | heading | pages [10] -->
2. Construct the classiﬁcation tree and choose the appropriate tree size to keep the simplicity

<!-- b000318 | prose | pages [10] -->
of the classiﬁcation standard.

<!-- b000319 | heading | pages [10] -->
3. Sort the importance of features according to their relative position in the tree, visualize the

<!-- b000320 | prose | pages [10] -->
tree and offer distinguishing strategy to identify the genre from others.

<!-- b000321 | prose | pages [10] -->
4.3.3

<!-- b000322 | heading | pages [10] -->
Solutions

<!-- b000323 | caption | pages [10] -->
Figure 12 shows the Similarity Matrix and Inﬂuence Matrix between Genres. Blues and

<!-- b000324 | prose | pages [10] -->
Easy Listening share some similar characteristics in musical features, whereas Electronic and Vocal are more similar. As for inﬂuence, Pop/Rock signiﬁcantly inﬂuences other genres. Inter- estingly, Pop/Rock has a strong inﬂuence on R&B, but they do not share signiﬁcant similarity

<!-- b000325 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000326 | prose | pages [10] -->
关注数学模型 in musical characteristics, which we will discuss the reason later.

<!-- b000327 | furniture | pages [10] -->
2

<!-- b000328 | furniture | pages [10] -->
MATHmodels

<!-- b000329 | furniture | pages [10] -->
获取更多资讯

<!-- b000330 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000331 | furniture | pages [11] -->
Team # 2100112

<!-- b000332 | furniture | pages [11] -->
Page 11 of 24

<!-- b000333 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000334 | prose | pages [11] -->
(a) Inﬂuence between and within genres (b) Similarity between genres

<!-- b000335 | caption | pages [11] -->
Figure 5: Inﬂuence and Similarity between and within genres

<!-- b000336 | caption | pages [11] -->
Figure 6 and Figure 12a show the similarity and inﬂuence within a genre. Some genres like

<!-- b000337 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000338 | prose | pages [11] -->
R&B and Country have more variation within the genre than others, which indicates artist’s desire for true freedom of expression.At the same time, Pop/Rock and Jazz have a greater inﬂu- ence on themselves than others, which means they tend to maintain a consistent style.

<!-- b000339 | caption | pages [11] -->
Figure 6: Similarity within genres

<!-- b000340 | prose | pages [11] -->
Set R&B as an example, we construct classﬁcation tree as shown in Figure 7. danceabil- ity, duration and instrumentalness are vital features that distinguish R&B from other genres. Based on this approach, we can ﬁnd the vital features of every genre.

<!-- b000341 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000342 | prose | pages [11] -->
关注数学模型

<!-- b000343 | furniture | pages [11] -->
2

<!-- b000344 | furniture | pages [11] -->
MATHmodels

<!-- b000345 | furniture | pages [11] -->
获取更多资讯

<!-- b000346 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000347 | furniture | pages [12] -->
Team # 2100112

<!-- b000348 | furniture | pages [12] -->
Page 12 of 24

<!-- b000349 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000350 | caption | pages [12] -->
Figure 7: R&B Classiﬁcation tree

<!-- b000351 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000352 | prose | pages [12] -->
We use dataset “inﬂuence_data.csv” to depict how genres change over time. Based on the number of inﬂuencers in different genres through different time period, we draw Figure 8. As shown in the ﬁgure. Blues and Jazz ﬂourished from 1930s to 1950s, and then met a smooth decline. On the other hand, Country kept popular from 1930s to 1990s. Pop/Rock, similar to R&B, thrived between 1960s and 1990s.

<!-- b000353 | caption | pages [12] -->
Figure 8: Genres changing over time (Part)

<!-- b000354 | prose | pages [12] -->
To further explore the relationship between different genres, we construct a directed genre network based on the Inﬂuence matrix, as shown in Figure 9. Intuitively, if a genre is closely related to another, artists tend to have a great inﬂuence on each other’s tracks. Therefore, we consider “music inﬂuence” as the major measure of relationship.

<!-- b000355 | prose | pages [12] -->
The Genre Network illustrates that Pop/Rock artists have a great inﬂuence on many other genres, especially R&B, Blues and Folk etc., relating these genres together. In addition, Pop/Rock artists are deeply inﬂuenced by Electronic. Learning from Pop/Rock Musicians, artists in R&B have a number of interactions with artists in Avant-Grade.

<!-- b000356 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000357 | prose | pages [12] -->
关注数学模型

<!-- b000358 | furniture | pages [12] -->
2

<!-- b000359 | furniture | pages [12] -->
MATHmodels

<!-- b000360 | furniture | pages [12] -->
获取更多资讯

<!-- b000361 | furniture | pages [13] -->
Team # 2100112

<!-- b000362 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000363 | furniture | pages [13] -->
Page 13 of 24

<!-- b000364 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000365 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000366 | caption | pages [13] -->
Figure 9: Genre Network

<!-- b000367 | prose | pages [13] -->
4.4 Task 4

<!-- b000368 | prose | pages [13] -->
4.4.1 Similarity Bayesian Network

<!-- b000369 | prose | pages [13] -->
This subsection aims to explore whether so-called ‘inﬂuencers’ truly have an inﬂuence on music created by ‘followers’, in other words, whether there is a signiﬁcant similarity between inﬂuencers’ music and pieces created by their followers.

<!-- b000370 | prose | pages [13] -->
To tackle this problem, we construct a Bayesian network based on similarity data. Here we deﬁne the similarity score between artist A and artist B as

<!-- b000371 | prose | pages [13] -->
∑nc

<!-- b000372 | prose | pages [13] -->
 

<!-- b000373 | prose | pages [13] -->
ChaAi −

<!-- b000374 | prose | pages [13] -->
i

<!-- b000375 | prose | pages [13] -->
ρAB =

<!-- b000376 | prose | pages [13] -->
q

<!-- b000377 | prose | pages [13] -->
∑nc

<!-- b000378 | prose | pages [13] -->
 

<!-- b000379 | prose | pages [13] -->
ChaAi −

<!-- b000380 | prose | pages [13] -->
¯

<!-- b000381 | prose | pages [13] -->
¯

<!-- b000382 | prose | pages [13] -->
 

<!-- b000383 | prose | pages [13] -->


<!-- b000384 | prose | pages [13] -->
ChaBi −

<!-- b000385 | prose | pages [13] -->
ChaA

<!-- b000386 | prose | pages [13] -->
ChaB

<!-- b000387 | prose | pages [13] -->
(13)

<!-- b000388 | prose | pages [13] -->
2 ∑nc

<!-- b000389 | prose | pages [13] -->
2

<!-- b000390 | prose | pages [13] -->
¯ ¯

<!-- b000391 | prose | pages [13] -->
¯

<!-- b000392 | prose | pages [13] -->
 

<!-- b000393 | prose | pages [13] -->
ChaBi −

<!-- b000394 | prose | pages [13] -->
ChaA

<!-- b000395 | prose | pages [13] -->
i

<!-- b000396 | prose | pages [13] -->
ChaB

<!-- b000397 | prose | pages [13] -->
i

<!-- b000398 | prose | pages [13] -->
which has similar form to Pearson correlation, nc denotes the number of music characteristics, ¯ ChaAi denotes ith standardized music characteristic score of artist A, and mean.

<!-- b000399 | prose | pages [13] -->
ChaAi denotes the

<!-- b000400 | prose | pages [13] -->
In our Bayesian Network, nodes denote artists, edges denote similarity scores. According to Fisher Z-Test[2], if A and B doesn’t have any similarity given C, then

<!-- b000401 | prose | pages [13] -->
p

<!-- b000402 | prose | pages [13] -->
log1+ρAB|C

<!-- b000403 | prose | pages [13] -->
n−|ChaC|−3

<!-- b000404 | prose | pages [13] -->
2

<!-- b000405 | prose | pages [13] -->
→N (0,1) (14) 1−ρAB|C

<!-- b000406 | prose | pages [13] -->
Based on the asymptotic distribution, we can calculate the similarity score between any two artists, then construct a Similarity Bayesian network. However, this traversal algorithm has NP problem. Therefore, we used Hill-Climbing algorithm with Random Starts instead. Deﬁne the Bayesian information as

<!-- b000407 | prose | pages [13] -->
nc

<!-- b000408 | prose | pages [13] -->
logfAi (Ai|ΠAi)−d

<!-- b000409 | prose | pages [13] -->
BIC =

<!-- b000410 | prose | pages [13] -->
∑

<!-- b000411 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000412 | prose | pages [13] -->
i=1

<!-- b000413 | prose | pages [13] -->
2log(n) (15)

<!-- b000414 | prose | pages [13] -->
关注数学模型

<!-- b000415 | furniture | pages [13] -->
2

<!-- b000416 | furniture | pages [13] -->
MATHmodels

<!-- b000417 | furniture | pages [13] -->
获取更多资讯

<!-- b000418 | furniture | pages [14] -->
Team # 2100112

<!-- b000419 | heading | pages [14] -->
Algorithm 1 Similarity Bayesian Network

<!-- b000420 | prose | pages [14] -->
while i ≤Max_RandomNumber do

<!-- b000421 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000422 | furniture | pages [14] -->
Page 14 of 24

<!-- b000423 | prose | pages [14] -->
Randomly generate a Similarity Bayesian network Calculate BIC_init

<!-- b000424 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000425 | prose | pages [14] -->
BIC_best ←BIC_init while j ≤Max_iterations do

<!-- b000426 | prose | pages [14] -->
Randomly choose add or delete an edge Calculate BIC_new if BIC_new ≤BIC_best then

<!-- b000427 | prose | pages [14] -->
Net_best ←CurrentBayesianNetwork BIC_best ←BIC_new end if end while end while Rank the BIC_best of each i and ﬁnd the best Similarity Bayesian network Postprocess results and visualization

<!-- b000428 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000429 | prose | pages [14] -->
Where logfAi (Ai|ΠAi) is the conditional density function, the pseudocode of the algorithm is shown as follows:

<!-- b000430 | prose | pages [14] -->
To improve the stability of the solution, we use bootstrap method to calculate 500 different solutions and take an average.

<!-- b000431 | prose | pages [14] -->
4.4.2 Contagious Characteristic Test

<!-- b000432 | prose | pages [14] -->
In this subsection we analyse if some music characteristics are more‘contagious’ than others, or they all have similar roles in inﬂuencing a particular artist’s music. Based on the results in the last subsection, we tackle this task by analyzing The Beatles and their major followers: The Beach Boys, Led Zeppelin, Gram Parsons and David Bowie.

<!-- b000433 | prose | pages [14] -->
To ﬁnd out if there exists characteristics signiﬁcantly more contagious than others, we apply multivariate two-sample test[3]. The null hypothesis H0 is

<!-- b000434 | prose | pages [14] -->
H0 : µ1 = µ2 (16)

<!-- b000435 | prose | pages [14] -->
Where µ1 denotes the average music characteristic vector of all tracks released by The Beatles. µ2 denote the average music characteristic vecter of one of their followers.

<!-- b000436 | prose | pages [14] -->
According to asymptotic statistic theory, when p is ﬁxed and n tends to inﬁnity, by the Central Limit Theorem and Slutsky Theorem:

<!-- b000437 | prose | pages [14] -->
S1

<!-- b000438 | prose | pages [14] -->
+ S2

<!-- b000439 | prose | pages [14] -->
( ¯X −¯Y)T

<!-- b000440 | prose | pages [14] -->
n1

<!-- b000441 | prose | pages [14] -->
n2

<!-- b000442 | prose | pages [14] -->
−1

<!-- b000443 | prose | pages [14] -->
( ¯X −¯Y) →χ2(p) (17)

<!-- b000444 | prose | pages [14] -->
where ¯X and ¯Y denote the sample mean respectively, and S1 and S2 denote the sample covariance matrix respectively.

<!-- b000445 | prose | pages [14] -->
Since the number of music characteristic (p = 9) is much smaller than the sample size, we do not need to make any distribution assumption for the data. The Chi-squared statistic follows a Chi-squared distribution with 9 degrees of freedom. By calculating the statistic, we can obtain the p-value according to the asymptotic distribution.

<!-- b000446 | prose | pages [14] -->
If the null hypothesis is accepted, we conclude that all music characteristics of followers are

<!-- b000447 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000448 | prose | pages [14] -->
equally similar to their inﬂuencer, indicating no characteristics are signiﬁcantly ‘contagious’.关注数学模型

<!-- b000449 | furniture | pages [14] -->
2

<!-- b000450 | furniture | pages [14] -->
MATHmodels

<!-- b000451 | furniture | pages [14] -->
获取更多资讯

<!-- b000452 | furniture | pages [15] -->
Team # 2100112

<!-- b000453 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000454 | furniture | pages [15] -->
Page 15 of 24

<!-- b000455 | prose | pages [15] -->
On the other hand, if the null hypothesis is rejected, we can further apply BH multiple hypoth- esis testing to further ﬁnd out which characteristic is more ‘contagious’.

<!-- b000456 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000457 | prose | pages [15] -->
4.4.3

<!-- b000458 | heading | pages [15] -->
Solutions

<!-- b000459 | prose | pages [15] -->
Without the loss of generality, we put our focus on the most popular band – The Beatles and their followers. Setting similarity score threshold as 0.21, the Similarity Bayesian Network of the Beatles and their 29 most popular followers is shown in Figure 10.

<!-- b000460 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000461 | caption | pages [15] -->
Figure 10: Similarity Bayesian Network of the Beatles and their followers

<!-- b000462 | prose | pages [15] -->
As shown in ﬁgure 10, directly or indirectly, 72% alleged ‘followers’ have similar compos- ing style to the Beatles, their ‘inﬂuencer’. However, 28 % artists who claim they are inﬂuenced have insigniﬁcant (lower than the threshold) similarity to their ‘inﬂuencer’. In other words, based on similarity data, nearly three out of ten artists aren’t affected by their so-called ‘inﬂu- encers’.

<!-- b000463 | caption | pages [15] -->
Table 4: Contagious Characteristic Test

<!-- b000464 | prose | pages [15] -->
chi-square value Follower Name p-value

<!-- b000465 | prose | pages [15] -->
3.183 Led Zeppelin 0.957 5.971 Gram Parsons 0.743 7.232 David Bowie 0.613 14.284 The Beach Boys 0.113

<!-- b000466 | prose | pages [15] -->
The results of Contagious Characteristic test is shown in Table 4. Under the signiﬁcant level of 5%, all four null hypotheses are accepted, which indicates that all musical characteris- tics of The Beatles equally inﬂuence its followers, in other words, no characteristics are more contagious and prominent than others.

<!-- b000467 | prose | pages [15] -->
we should emphasize that in the above process, Type I error may accumulate due to multiple hypothesis tests. However, in this problem, all hypotheses are accepted. Thus, Type I errors can still be controlled within the signiﬁcance level.

<!-- b000468 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000469 | prose | pages [15] -->
关注数学模型

<!-- b000470 | furniture | pages [15] -->
2

<!-- b000471 | furniture | pages [15] -->
MATHmodels

<!-- b000472 | furniture | pages [15] -->
获取更多资讯

<!-- b000473 | furniture | pages [16] -->
Team # 2100112

<!-- b000474 | prose | pages [16] -->
4.5 Task 5

<!-- b000475 | prose | pages [16] -->
4.5.1 Deﬁnition of Revolution

<!-- b000476 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000477 | furniture | pages [16] -->
Page 16 of 24

<!-- b000478 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000479 | prose | pages [16] -->
To tackle task 5, we ﬁrst deﬁne “music revolution”. The number of inﬂuencers in major genres is shown in ﬁgure 11. As time went by, some genre ﬂourished and others went out of favor.

<!-- b000480 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000481 | caption | pages [16] -->
Figure 11: The number of inﬂuencers in major genres

<!-- b000482 | prose | pages [16] -->
We deﬁne the revolution time for genres as the time when there are some genres declined and others springing up or dominating. From Figure 11, we ﬁnd in the 1950s, Electronic ﬂourished gradually, while Vocal all went from boom to bust. The popularity of Pop/Rock and R&B also met a sharp increase. These phenomena indicate that 1950s is one of the revolution periods.

<!-- b000483 | prose | pages [16] -->
After deﬁning revolution periods, we focus on ﬁnding a signiﬁcant change point of music characteristics in the 1950s to explain what we discussed above. The key to this problem is turned to identify the change points in time series of the music features. Based on the change points we ﬁnd, we then can identify artists that represent the revolutionaries.

<!-- b000484 | heading | pages [16] -->
Change Points Detection (DP Algorithm)

<!-- b000485 | prose | pages [16] -->
4.5.2

<!-- b000486 | prose | pages [16] -->
We deﬁne the set of the change points as Θ = {θi}m

<!-- b000487 | prose | pages [16] -->
character {Yt}n

<!-- b000488 | prose | pages [16] -->
t=1 admit:

<!-- b000489 | prose | pages [16] -->
 t

<!-- b000490 | prose | pages [16] -->


<!-- b000491 | prose | pages [16] -->
Yt = ai +bi ∗

<!-- b000492 | prose | pages [16] -->
+εt

<!-- b000493 | prose | pages [16] -->
n

<!-- b000494 | prose | pages [16] -->
i=1. Let the time series of some music

<!-- b000495 | prose | pages [16] -->
θi−1 +1 ≤t ≤θi (18)

<!-- b000496 | prose | pages [16] -->
Where ai is the intercept term, bi measures the speed of linear trend, and the error term εt is a white noise process.

<!-- b000497 | prose | pages [16] -->
In order to ensure that the stability of parameters and change points, we also need to limit

<!-- b000498 | prose | pages [16] -->
θi −θi−1 > τ (19)

<!-- b000499 | prose | pages [16] -->
and we suggest τ = [0.1n], which will be disucssed in detail in sensitivity analysis.

<!-- b000500 | prose | pages [16] -->
Since yt changes with a linear trend in different stages, when εi follows independent and identical distribution, it is apparent to estimate parameters by minimizing the sum of squared residuals.

<!-- b000501 | prose | pages [16] -->
{θi}m

<!-- b000502 | prose | pages [16] -->
i=1 = argmin

<!-- b000503 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000504 | prose | pages [16] -->
θ∈Θ

<!-- b000505 | prose | pages [16] -->
n

<!-- b000506 | prose | pages [16] -->
(yt −byt)2

<!-- b000507 | prose | pages [16] -->
∑

<!-- b000508 | prose | pages [16] -->
(20)关注数学模型

<!-- b000509 | prose | pages [16] -->
t=1

<!-- b000510 | furniture | pages [16] -->
2

<!-- b000511 | furniture | pages [16] -->
MATHmodels

<!-- b000512 | furniture | pages [16] -->
获取更多资讯

<!-- b000513 | furniture | pages [17] -->
Team # 2100112

<!-- b000514 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000515 | furniture | pages [17] -->
Page 17 of 24

<!-- b000516 | prose | pages [17] -->
When the number of change points is given, the key of using Dynamic Programming algo- rithm in this problem is to establish the recursive relationship of the sum of squared residuals before and after a new change point is added.

<!-- b000517 | prose | pages [17] -->
Let δ (m,n) denote the sum of squared residuals associated with the optimal partition con-

<!-- b000518 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000519 | prose | pages [17] -->
taining m breaks using ﬁrst n observations, RSS(i, j) denote the sum of squared residuals ob- tained by applying least-squares to a segment start from i to j.

<!-- b000520 | prose | pages [17] -->
Then, we can achieve the global minimization of overall sum of squared residuals by solving recursive problem as follows:

<!-- b000521 | prose | pages [17] -->
mτ≤j≤n−τδ(m−1, j)+RSS(j +1,n) δ (m,n) = min (21)

<!-- b000522 | prose | pages [17] -->
where τ is a trimming parameter that constrains the distance between two change points not to be too close.

<!-- b000523 | prose | pages [17] -->
It is important to note that the DP algorithm is O(T 2) and does not depend on the number of change points. Therefore, we can quickly estimate all the change points which are consistent

<!-- b000524 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000525 | prose | pages [17] -->
for real ones[5].

<!-- b000526 | prose | pages [17] -->
Obviously, we also need to penalize the number of change points. Considering the number of change points as a tuning parameter, We recommend to use BIC criterion to determine the optimal number of change points m∗.

<!-- b000527 | prose | pages [17] -->
RSSoverall +log(n)∗ˆσ2 ∗m

<!-- b000528 | prose | pages [17] -->
m∗= argmin

<!-- b000529 | prose | pages [17] -->
m

<!-- b000530 | prose | pages [17] -->
4.5.3

<!-- b000531 | heading | pages [17] -->
Solutions

<!-- b000532 | prose | pages [17] -->
(a) Energy

<!-- b000533 | prose | pages [17] -->
(22)

<!-- b000534 | prose | pages [17] -->
(b) Acousticness

<!-- b000535 | caption | pages [17] -->
Figure 12: Change points detection of acousticness and energy

<!-- b000536 | prose | pages [17] -->
By using the DP algorithm above, we detected the change points of 11 continuous music characteristics in the dataset “data_by_year.csv”, as shown in table 5.

<!-- b000537 | prose | pages [17] -->
It can be seen in table 5 that four music characters (acousticness, energy, danceability and loudness) show signiﬁcant changes around 1950.

<!-- b000538 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000539 | prose | pages [17] -->
关注数学模型

<!-- b000540 | furniture | pages [17] -->
2

<!-- b000541 | furniture | pages [17] -->
MATHmodels

<!-- b000542 | furniture | pages [17] -->
获取更多资讯

<!-- b000543 | furniture | pages [18] -->
Team # 2100112

<!-- b000544 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000545 | furniture | pages [18] -->
Page 18 of 24

<!-- b000546 | caption | pages [18] -->
Table 5: Revolution date of music characteristics

<!-- b000547 | prose | pages [18] -->
Characteristic 1930s 1940s 1950s

<!-- b000548 | prose | pages [18] -->
Revolution date

<!-- b000549 | prose | pages [18] -->
1960s 1970s 1980s 1990s 2000s

<!-- b000550 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000551 | prose | pages [18] -->
Instrumentalness 1933 1946 - Duration_ms - 1946 - 1950 Acousticness - - Tempo - 1947 - 1950 Danceability - - Valence - 1947 - 1951 Energy - - Liveness - - 1956 Speechness - - 1956 Popularity - - 1953 1950 Loudness 1936 - 1964 - - - - 1966 - - - 2007 1964 1979 - - - - 1979 - 1996 2008 - - - 1997 2008 1966 - - - 2005 - 1979 - - 2008 - 1976 - - 2008 - - - - 2006 - 1970 - - 2006 - - - - 2008

<!-- b000552 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000553 | prose | pages [18] -->
To get a further insight into the revolution related to music characteristics in different genres, we draw boxplots of energy and acousticness respectively in ﬁgure 13. Obviously, the new genres (Pop/Rock, R&B and Electronic) have signiﬁcant higher energy, yet their acousticness is much lower than the old ones. This is consistent with the time series analysis above. Thus, we convinced that the four music characters: acousticness, energy, danceability and loudness might signify revolutions in musical evolution.

<!-- b000554 | prose | pages [18] -->
(a) Energy (b) Acousticness

<!-- b000555 | caption | pages [18] -->
Figure 13: Energy and Acousticness in different genres

<!-- b000556 | prose | pages [18] -->
We deﬁne two types of revolutionaries: artists who make a major change to existing genres and artists who create a new genre. For the ﬁrst type, we focus on Pop/Rock, which shows a dramatic change in 1950s. For the second type, we put our emphasis on Electronic, which ﬁrst emerges in early 1950s.

<!-- b000557 | prose | pages [18] -->
To ﬁnd out revolutionaries in our network, we ﬁrst ﬁlter Pop/Rock and Electronic tracks released in 1950s, then build a Similarity Bayesian Network based on the artists of these tracks. Intuitively, artists at the core of our network are revolutionaries, as they have a major inﬂuence on artists during this period.

<!-- b000558 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000559 | prose | pages [18] -->
关注数学模型

<!-- b000560 | furniture | pages [18] -->
2

<!-- b000561 | furniture | pages [18] -->
MATHmodels

<!-- b000562 | furniture | pages [18] -->
获取更多资讯

<!-- b000563 | furniture | pages [19] -->
Team # 2100112

<!-- b000564 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000565 | furniture | pages [19] -->
Page 19 of 24

<!-- b000566 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000567 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000568 | caption | pages [19] -->
Figure 14: Similarity Bayesian Network of Pop/Rock and Electronic in 1950s

<!-- b000569 | prose | pages [19] -->
Our Similarity Bayesian Network is shown in ﬁgure 14. Elvis Presley, an inﬂuencer who has the most followers in 1950s in Pop/Rock, leads a countercultural movement in the United States. At the same time, Cliff Richard, an English artist, makes a dramatic change on the evolution of the genre. These two revolutionaries not only reinvent the existing genre, but also inspire artists like Moti and Freestyle to create a new genre – Electronic. Therefore, Elvis Presley and Cliff Richard represent revolutionaries in 1950s music revolution.

<!-- b000570 | prose | pages [19] -->
4.6 Task 6

<!-- b000571 | prose | pages [19] -->
4.6.1 Dynamic Inﬂuencer Indicator

<!-- b000572 | prose | pages [19] -->
In this task, we choose Pop Rock as the genre for research since it exists for a long time and there are several reinventions.

<!-- b000573 | prose | pages [19] -->
Intuitively, dynamic inﬂuencers dramatically change the trend of the genre in a speciﬁc period of time. Thus a dynamic inﬂuencer of a period should satisfy

<!-- b000574 | prose | pages [19] -->
1. He/She released more than 10 tracks in this period.

<!-- b000575 | prose | pages [19] -->
2. The music characteristics of these tracks are consistent with the lagging trend of Pop/Rock.

<!-- b000576 | prose | pages [19] -->
Based on the deﬁnition above, we construct an indicator of dynamic inﬂuencer as

<!-- b000577 | furniture | pages [19] -->


<!-- b000578 | prose | pages [19] -->
di = 1

<!-- b000579 | prose | pages [19] -->
 

<!-- b000580 | prose | pages [19] -->
|Ai| ∑

<!-- b000581 | prose | pages [19] -->
∑ j∈F

<!-- b000582 | prose | pages [19] -->
t∈Ai

<!-- b000583 | prose | pages [19] -->
!1/2

<!-- b000584 | prose | pages [19] -->
2

<!-- b000585 | prose | pages [19] -->
xi,j,t −¯xj,t−υ

<!-- b000586 | prose | pages [19] -->
(23)

<!-- b000587 | prose | pages [19] -->
where xi,j,t is the music characteristics j of tracks released by the ith artist in the year t, ¯xj,t is the average value of artists, F is the set of music characteristics, υ is the lag year. Here we set υ = 1 , which means the dynamic inﬂuencer will lead the music trend a year after tracks are

<!-- b000588 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000589 | prose | pages [19] -->
released.

<!-- b000590 | prose | pages [19] -->
关注数学模型

<!-- b000591 | furniture | pages [19] -->
2

<!-- b000592 | furniture | pages [19] -->
MATHmodels

<!-- b000593 | furniture | pages [19] -->
获取更多资讯

<!-- b000594 | furniture | pages [20] -->
Team # 2100112

<!-- b000595 | prose | pages [20] -->
4.6.2

<!-- b000596 | heading | pages [20] -->
Solutions

<!-- b000597 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000598 | furniture | pages [20] -->
Page 20 of 24

<!-- b000599 | prose | pages [20] -->
Changes of music characteristics in Pop/Rock are shown in ﬁgure 15 Preliminary data anal- ysis shows that most Pop/Rock songs are released after 1956 (the dotted line). Before 1956, the

<!-- b000600 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000601 | prose | pages [20] -->
ﬂuctuation of musical characteristics is caused by small sample size. Therefore, we only an- alyze changes after 1956. We set F = {acousticness,danceability,energy,loudness,valence}, as only these characteristics show signiﬁcant ﬂuctuations after 1956.

<!-- b000602 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000603 | caption | pages [20] -->
Figure 15: Changes of music characteristics in Pop/Rock

<!-- b000604 | prose | pages [20] -->
By calculating the value of dynamic inﬂuencer indicator of 99 most famous artists, we ﬁnd out top 10 dynamic Inﬂuencers that have giant impact on Pop/Rock. The inﬂuencer and his/her active period is shown in ﬁgure 16.

<!-- b000605 | caption | pages [20] -->
Figure 16: Changes of music characteristics in Pop/Rock

<!-- b000606 | prose | pages [20] -->
According to the ﬁgure 15, Some music characteristics of Pop/Rock have changed a lot over time. Acousticness and valence both experience a signiﬁcant decline after 1956, while energy and loudness show a consistent increase.

<!-- b000607 | prose | pages [20] -->
The change above is mainly caused by the change of dynamic inﬂuencers. With the tech- nology enhancements and electrical ampliﬁcation, the Beatles, Led Zeppelin and Eagles poured more intense emotion and passion into Pop Rock music in the last century. These artists tend to express sadness or depressed emotions. However, in recent 20 years, some great musicians, like Lincoln Park and Taylor Swift, switched the tone of Pop Rock music from sadness to happiness.

<!-- b000608 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000609 | prose | pages [20] -->
关注数学模型 They make pop music smooth, relaxing and much more suitable for dancing.

<!-- b000610 | furniture | pages [20] -->
2

<!-- b000611 | furniture | pages [20] -->
MATHmodels

<!-- b000612 | furniture | pages [20] -->
获取更多资讯

<!-- b000613 | furniture | pages [21] -->
Team # 2100112

<!-- b000614 | prose | pages [21] -->
4.7 Task 7

<!-- b000615 | prose | pages [21] -->
4.7.1 Cultural Inﬂuence of music

<!-- b000616 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000617 | furniture | pages [21] -->
Page 21 of 24

<!-- b000618 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000619 | prose | pages [21] -->
Based on the models in the previous section, we detect three important periods in musical evolution, as shown in ﬁgure 17. We discuss the culture-inﬂuence processes as follows:

<!-- b000620 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000621 | caption | pages [21] -->
Figure 17: Culture-inﬂuence processes

<!-- b000622 | prose | pages [21] -->
Period I (1935-1945): This Period was shaped by the moods of the Great Depression. In these period, lots of artists begin to create music with high energy and fast tempo, as shown in

<!-- b000623 | caption | pages [21] -->
Figure 17. Reinvention and fast growth of Pop/Rock and the glamorous beginning of Reggae

<!-- b000624 | prose | pages [21] -->
form an upward look of culture.

<!-- b000625 | prose | pages [21] -->
Period II (1950-1960): Following the detrimental effects of World War II, people was about to embark on a musical journey and substantially change the music style, valence and dance- ability saw a sharp increase in music released in this period – the golden age of Pop/Rock. The whole culture becomes hopeful and energetic.

<!-- b000626 | prose | pages [21] -->
Period III (1995-2005): By late 1995, many young people were getting tired of the Pop/rock were inundating the airwaves with, the energy and tempo of music reached the peak and began to decline. A mature music culture is gradually formed.

<!-- b000627 | prose | pages [21] -->
4.7.2 Changes identiﬁed within the network

<!-- b000628 | prose | pages [21] -->
Social and Political Changes: According to Similarity Bayesian Network of Pop/Rock artists in 1950s. As shown in ﬁgure 18, 1950s’ Pop/Rock is diversiﬁed in several subgenres, which are rather different from each other (as there are no edges between artists in different subgenres). This feature of network identiﬁes the countercultural movement in 1950s – people have increasing desire for true freedom of expression and the diversity of people become more and more prominent.

<!-- b000629 | prose | pages [21] -->
Technological Changes: According to the Wikipedia, we know that the emergence of the Internet mainly leads to the rise of the Electronic, as the Internet made it easier to spread the software for producing Electronic music. Such trends can be identiﬁed through change of num- bers of inﬂuencers in Electronic over time, as shown in ﬁgure 19. Inﬂuence reaches its peak due to the proliferation of the Internet.

<!-- b000630 | prose | pages [21] -->
Analysis above shows that based the models established, we can ﬁnd the cultural inﬂuence of music in time and circumstances, and identify the effects of social, political or technological

<!-- b000631 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000632 | prose | pages [21] -->
changes.

<!-- b000633 | prose | pages [21] -->
关注数学模型

<!-- b000634 | furniture | pages [21] -->
2

<!-- b000635 | furniture | pages [21] -->
MATHmodels

<!-- b000636 | furniture | pages [21] -->
获取更多资讯

<!-- b000637 | furniture | pages [22] -->
Team # 2100112

<!-- b000638 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000639 | furniture | pages [22] -->
Page 22 of 24

<!-- b000640 | prose | pages [22] -->
微信公众号：数学模型

<!-- b000641 | caption | pages [22] -->
Figure 18: Familiarity Beyesian Network of Pop/Rock in 1950s

<!-- b000642 | prose | pages [22] -->
微信号：MATHmodels

<!-- b000643 | caption | pages [22] -->
Figure 19: Number of inﬂuencers in Electronic

<!-- b000644 | prose | pages [22] -->
5

<!-- b000645 | heading | pages [22] -->
Sensitivity Analysis

<!-- b000646 | prose | pages [22] -->
In Task 5, our Change Point Detection model involves a trimming parameter τ, which might have an effect on optimal change points detection. To test the robustness of the model, we apply a change to the trimming parameter and check whether the revolutionary in 1950s can be well detected.

<!-- b000647 | caption | pages [22] -->
Table 6: Inﬂuence of τ on change point detection

<!-- b000648 | prose | pages [22] -->
Characteristic [0.05n]

<!-- b000649 | prose | pages [22] -->
τ

<!-- b000650 | prose | pages [22] -->
[0.10n] [0.15n] [0.20n]

<!-- b000651 | prose | pages [22] -->
1950 1964 1979 Acousticness 1950 1964 1979 1950 1964 1979 1950 1964 1979 1950 1997 2008 Danceability 1928 1951 1997 2008 1950 1997 2008 1950 2008 1951 1979 2008 Energy 1951 1983 1994 2008 1951 1979 2008 1951 1979 2008 1936 1950 2008 Loudness 1936 1951 1980 2008 1935 1950 2008 1950 2008

<!-- b000652 | prose | pages [22] -->
As shown in table 6, the proposed model is very robust to change points when τ is greater

<!-- b000653 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000654 | prose | pages [22] -->
关注数学模型 than or equal to [0.1n], which implies the value we selected is reasonable.

<!-- b000655 | furniture | pages [22] -->
2

<!-- b000656 | furniture | pages [22] -->
MATHmodels

<!-- b000657 | furniture | pages [22] -->
获取更多资讯

<!-- b000658 | furniture | pages [23] -->
Team # 2100112

<!-- b000659 | prose | pages [23] -->
6

<!-- b000660 | heading | pages [23] -->
Strengths and Weaknesses

<!-- b000661 | prose | pages [23] -->
6.1

<!-- b000662 | heading | pages [23] -->
Strengths

<!-- b000663 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000664 | furniture | pages [23] -->
Page 23 of 24

<!-- b000665 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000666 | heading | pages [23] -->
• Effective models: For different problems, we build several models including Bayesian

<!-- b000667 | prose | pages [23] -->
network, Change Point Detection model, which makes the analysis of each problem de- tailed and convincing.

<!-- b000668 | prose | pages [23] -->
• Statistical tests: Instead of simply comparing the value, we apply Mann-Whitney Test and Multivariate Mean Test to make our conclusions are reliable.

<!-- b000669 | prose | pages [23] -->
• Vivid visualizations: We use many ﬁgures to show our results, make it easier to capture the key information.

<!-- b000670 | prose | pages [23] -->
6.2

<!-- b000671 | heading | pages [23] -->
Weaknesses

<!-- b000672 | prose | pages [23] -->
微信号：MATHmodels

<!-- b000673 | prose | pages [23] -->
• Our analysis does not cover all genres in some models. Given space limitations, part of our analysis mainly focuses on two representive genres: Pop Rock and R&B.

<!-- b000674 | prose | pages [23] -->
• We make a strong assumption on time series, which doen’t always hold in reality. We assume the error term follows independent normal distribution, however, it often follows a weakly dependent stationary process in reality.

<!-- b000675 | heading | pages [23] -->
References

<!-- b000676 | references | pages [23] -->
[1] Chen, Guanrong. Introduction to complex networks : Models, structures and dynamics

<!-- b000677 | references | pages [23] -->
[M]. Higher Education Press, 2012.

<!-- b000678 | references | pages [23] -->
[2] Lawley, D. N. "A generalization of Fisher’s z test." Biometrika 30.1/2 (1938): 180-187.

<!-- b000679 | references | pages [23] -->
[3] Rencher A C , Christensen W F . Methods of Multivariate Analysis[J]. Technometrics,

<!-- b000680 | references | pages [23] -->
2002, 38(443):76-77.

<!-- b000681 | references | pages [23] -->
[4] McKnight, Patrick E., and Julius Najab. "Mann-Whitney U Test." The Corsini encyclope-

<!-- b000682 | references | pages [23] -->
dia of psychology (2010): 1-1.

<!-- b000683 | references | pages [23] -->
[5] Bai J , Perron P . Computation and analysis of multiple structural change models[J]. Jour-

<!-- b000684 | references | pages [23] -->
nal of Applied Econometrics, 2003.

<!-- b000685 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000686 | references | pages [23] -->
关注数学模型

<!-- b000687 | furniture | pages [23] -->
2

<!-- b000688 | furniture | pages [23] -->
MATHmodels

<!-- b000689 | furniture | pages [23] -->
获取更多资讯

<!-- b000690 | furniture | pages [24] -->
Team # 2100112

<!-- b000691 | references | pages [24] -->
A Document to ICM Society

<!-- b000692 | references | pages [24] -->
To: Integrative Collective Music Society

<!-- b000693 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000694 | furniture | pages [24] -->
Page 24 of 24

<!-- b000695 | references | pages [24] -->
微信公众号：数学模型

<!-- b000696 | references | pages [24] -->
From: Team 2100112

<!-- b000697 | references | pages [24] -->
In this document, we will show you how our networks offer a better understanding of the

<!-- b000698 | references | pages [24] -->
inﬂuence of music, and potential improvement given richer data. In addition, we will give you

<!-- b000699 | references | pages [24] -->
some recommendation about the further study of music and its cultural inﬂuence.

<!-- b000700 | references | pages [24] -->
Our approach gives a comprehensive measure of an artist’s inﬂuence. We propose met-

<!-- b000701 | references | pages [24] -->
rics based on network theory - the Degree Centrality, the Weighted Degree Centrality and the

<!-- b000702 | references | pages [24] -->
Eigen Centrality. The music inﬂuence measure consider both the number and the popularity of

<!-- b000703 | references | pages [24] -->
followers, making it more close to the reality.

<!-- b000704 | references | pages [24] -->
Based on the Bayesian Network, our approach measures real connections between the inﬂu-

<!-- b000705 | references | pages [24] -->
encers and followers. Although some followers claim they are inﬂuence by the inﬂuencer, their

<!-- b000706 | references | pages [24] -->
tracks don’t show any signiﬁcant similarity to their inﬂencer’s. By applying our Bayes Network

<!-- b000707 | references | pages [24] -->
微信号：MATHmodels

<!-- b000708 | references | pages [24] -->
model, you can ﬁnd out “true” followers and have a more objective understanding of the music

<!-- b000709 | references | pages [24] -->
inﬂuence network between artists.

<!-- b000710 | references | pages [24] -->
Beneﬁted from detailed time series analysis, our approach offer a further insight of the rise

<!-- b000711 | references | pages [24] -->
and decline of genres and music revolution. We propose a dynamic programming algorithm to

<!-- b000712 | references | pages [24] -->
detect the change points in music characteristics and revolutions. Combined with the Dynamic

<!-- b000713 | references | pages [24] -->
Inﬂuencer Indicator, you will learn a lot about the evolution process of music.

<!-- b000714 | references | pages [24] -->
What’s more, our networks can be considerably improved if more data is introduced. Thanks

<!-- b000715 | references | pages [24] -->
to the strong learning ability of Bayesian Network, if more data are introduced (like the data

<!-- b000716 | references | pages [24] -->
with more genres or more music characteristics), we can get more accute parameter estimation,

<!-- b000717 | references | pages [24] -->
which will bring out better results.

<!-- b000718 | references | pages [24] -->
They are a lot of topics about music worth further investigating. For example, if we ﬁnd

<!-- b000719 | references | pages [24] -->
the music in some country is getting more and more energetic, then we can go to check if there

<!-- b000720 | references | pages [24] -->
are any social, political or technological changes, such as countercultural movements and the

<!-- b000721 | references | pages [24] -->
proliferation of the Internet. When music characteristics are changes, so does the society. For

<!-- b000722 | references | pages [24] -->
instance, The spread of positive music styles will form an upward look of culture.

<!-- b000723 | references | pages [24] -->
Hope you will ﬁnd our paper helpful and take our recommendations into consideration. We

<!-- b000724 | references | pages [24] -->
are looking forward to contributing our efforts to get deeper insight into music evolution.

<!-- b000725 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000726 | references | pages [24] -->
关注数学模型

<!-- b000727 | furniture | pages [24] -->
2

<!-- b000728 | furniture | pages [24] -->
MATHmodels

<!-- b000729 | furniture | pages [24] -->
获取更多资讯
