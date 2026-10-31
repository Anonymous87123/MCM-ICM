# P-D-2021-2106028-e54d016e

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen 2021 Team Control Number D MCM/ICM 2106028 Summary Sheet

<!-- b000002 | title | pages [1] -->
Mining the Influence of Music Based on Social Network Analysis and Statistical Methods

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
As the productivity has developed rapidly since last century, people have been paying more and more attention to their spiritual life. As an important part of art and culture, music also changes as times goes by, produces many branches and gains popularity all over the world.

<!-- b000005 | prose | pages [1] -->
In this paper, we systematically study influence of music through networks and our work can be summarized as following:

<!-- b000006 | list | pages [1] -->
• In Problem 1, we construct the influence network as a directed graph, and propose an overall measure for music influence based on several metrics of the network.

<!-- b000007 | list | pages [1] -->
• In Problem 2, we analyze the correlation between music features and propose to measure the distance and similarity of music in a latent space by using factor analysis.

<!-- b000008 | list | pages [1] -->
• In Problem 3, we discuss the similarity, influence and relation within genre and between genres, propose to distinguish genre by outlier detection, and describe the process of genre changing over time.

<!-- b000009 | list | pages [1] -->
• In Problem 4, we show by correlation analysis that reported influncers really affect the style of followers. We also find acousticness and valence, which just correspond to the first latent variable, are more contagious.

<!-- b000010 | list | pages [1] -->
• In Problem 5, based on the strategy of Bollinger Bands, we identify the signals of revolutions as those points outside the band. We observe strong signals of revolution in the 1960s and discover that Nat King Cole and The Beatles are the best representatives of revolutionary during this period.

<!-- b000011 | list | pages [1] -->
• In Problem 6, we think some artists of high influence and popularity might lead the trend of genre development. Therefore, we select the dynamic influencer according to these two indicators and show by visualization that genre leaders do play a guiding role and interact with the whole genre closely.

<!-- b000012 | list | pages [1] -->
• In Problem 7, we discuss the sociality of music using the music revolution in the 1960s raised by the counterculture movement as an example. We also explore the significant and possible influence of Internet.

<!-- b000013 | prose | pages [1] -->
Finally we conduct sensitivity analysis on the hyper-parameters used in our model, which proves the stability of our model and shows the rationality of our choice for hyper-parameters. The pros and cons of our model are discussed deeply as well.

<!-- b000014 | keywords | pages [1] -->
Keywords: Social network, Factor analysis, Correlation analysis, Bollinger Bands, Music evolution

<!-- b000015 | furniture | pages [1] -->
关注数学模型 获取更多资讯

<!-- b000016 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000017 | furniture | pages [2] -->
Team # 2106028

<!-- b000018 | furniture | pages [2] -->
Page 2 of 25

<!-- b000019 | contents | pages [2] -->
Mining the Inﬂuence of Music Based on Social

<!-- b000020 | contents | pages [2] -->
Network Analysis and Statistical Methods

<!-- b000021 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
1 Introduction

<!-- b000024 | contents | pages [2] -->
4

<!-- b000025 | contents | pages [2] -->
1.1

<!-- b000026 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
4

<!-- b000028 | contents | pages [2] -->
1.2

<!-- b000029 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
4

<!-- b000031 | contents | pages [2] -->
2 Problem 1: Network Building and Measures Development

<!-- b000032 | contents | pages [2] -->
5

<!-- b000033 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000034 | contents | pages [2] -->
2.1

<!-- b000035 | contents | pages [2] -->
Network Building . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
5

<!-- b000037 | contents | pages [2] -->
2.2

<!-- b000038 | contents | pages [2] -->
Music Inﬂuence Measures Development . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
6

<!-- b000040 | contents | pages [2] -->
2.3

<!-- b000041 | contents | pages [2] -->
Construct a Subnetwork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
8

<!-- b000043 | contents | pages [2] -->
3 Problem 2: Music Similarity Metric

<!-- b000044 | contents | pages [2] -->
9

<!-- b000045 | contents | pages [2] -->
4 Problem 3: Genre Relation and Development

<!-- b000046 | contents | pages [2] -->
11

<!-- b000047 | contents | pages [2] -->
4.1

<!-- b000048 | contents | pages [2] -->
Similarity and Inﬂuence Comparison . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000049 | contents | pages [2] -->
11

<!-- b000050 | contents | pages [2] -->
4.2

<!-- b000051 | contents | pages [2] -->
Genre Distinguishment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
12

<!-- b000053 | contents | pages [2] -->
4.2.1

<!-- b000054 | contents | pages [2] -->
Low-Variance Features . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
12

<!-- b000056 | contents | pages [2] -->
4.2.2

<!-- b000057 | contents | pages [2] -->
Analyzing Components . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [2] -->
12

<!-- b000059 | contents | pages [2] -->
4.2.3

<!-- b000060 | contents | pages [2] -->
Outlier Detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [2] -->
12

<!-- b000062 | contents | pages [2] -->
4.3

<!-- b000063 | contents | pages [2] -->
Genre Evolution and Relations

<!-- b000064 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
13

<!-- b000066 | contents | pages [2] -->
4.3.1

<!-- b000067 | contents | pages [2] -->
How Does the Number of Musicians in a Genre Change Over Time? . .

<!-- b000068 | contents | pages [2] -->
13

<!-- b000069 | contents | pages [2] -->
4.3.2

<!-- b000070 | contents | pages [2] -->
How Does the Number of Works in a Genre Change Over Time?

<!-- b000071 | contents | pages [2] -->
. . . .

<!-- b000072 | contents | pages [2] -->
14

<!-- b000073 | contents | pages [2] -->
4.3.3

<!-- b000074 | contents | pages [2] -->
How Do the Features of Each Genre Change Over Time? . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
14

<!-- b000076 | contents | pages [2] -->
5 Problem 4: Similarity Veriﬁcation and Feature Mining

<!-- b000077 | contents | pages [2] -->
15

<!-- b000078 | contents | pages [2] -->
6 Problem 5: Signals and Pioneers of Revolution

<!-- b000079 | contents | pages [2] -->
16

<!-- b000080 | contents | pages [2] -->
6.1

<!-- b000081 | contents | pages [2] -->
Identify Signals of Revolutions in Music Evolution . . . . . . . . . . . . . . . . .

<!-- b000082 | contents | pages [2] -->
16

<!-- b000083 | contents | pages [2] -->
6.2

<!-- b000084 | contents | pages [2] -->
Discover Musicians Who Can Represent Revolutionary Changes . . . . . . . . .

<!-- b000085 | contents | pages [2] -->
17

<!-- b000086 | contents | pages [2] -->
7 Problem 6: Case Study on Dynamic Inﬂuencers

<!-- b000087 | contents | pages [2] -->
18

<!-- b000088 | contents | pages [2] -->
7.1

<!-- b000089 | contents | pages [2] -->
Music Evolution over Time

<!-- b000090 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
18

<!-- b000092 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000093 | contents | pages [2] -->
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
Team # 2106028

<!-- b000099 | furniture | pages [3] -->
Page 3 of 25

<!-- b000100 | contents | pages [3] -->
7.2

<!-- b000101 | contents | pages [3] -->
Indicators of Dynamic Inﬂuencers

<!-- b000102 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | furniture | pages [3] -->
19

<!-- b000104 | contents | pages [3] -->
7.3

<!-- b000105 | contents | pages [3] -->
Interaction Between Genre and its Musician . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [3] -->
19

<!-- b000107 | heading | pages [3] -->
8 Problem 7: The Sociality of Music

<!-- b000108 | prose | pages [3] -->
20 微信公众号：数学模型

<!-- b000109 | heading | pages [3] -->
9 Sensitivity Analysis

<!-- b000110 | prose | pages [3] -->
21

<!-- b000111 | prose | pages [3] -->
9.1 Sensitivity of Moving Average Window . . . . . . . . . . . . . . . . . . . . . . . 21

<!-- b000112 | prose | pages [3] -->
9.2 Sensitivity of Revolutionary Threshold . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000113 | heading | pages [3] -->
10 Strengths and Weaknesses

<!-- b000114 | prose | pages [3] -->
22

<!-- b000115 | prose | pages [3] -->
10.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22

<!-- b000116 | prose | pages [3] -->
10.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

<!-- b000117 | heading | pages [3] -->
11 Conclusion

<!-- b000118 | prose | pages [3] -->
23 微信号：MATHmodels

<!-- b000119 | heading | pages [3] -->
12 Document to the ICM Society

<!-- b000120 | prose | pages [3] -->
24

<!-- b000121 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000122 | prose | pages [3] -->
关注数学模型

<!-- b000123 | furniture | pages [3] -->
2

<!-- b000124 | furniture | pages [3] -->
MATHmodels

<!-- b000125 | furniture | pages [3] -->
获取更多资讯

<!-- b000126 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000127 | furniture | pages [4] -->
Team # 2106028

<!-- b000128 | furniture | pages [4] -->
Page 4 of 25

<!-- b000129 | heading | pages [4] -->
1 Introduction

<!-- b000130 | heading | pages [4] -->
1.1 Problem Background

<!-- b000131 | prose | pages [4] -->
The culture and art industry has witnessed an unprecedented boom recently. Delighted 微信公众号：数学模型 with an ample supply of excellent masterpieces of art, audiences around the world are grateful for the effort made by those great artists. Among these popular productions, musical pieces are the most inﬂuential.

<!-- b000132 | prose | pages [4] -->
With a burning desire to understand the role of music in the collective human experience, we try to develop a method to quantify musical evolution. There are many factors that can in- ﬂuence artists when they create a new piece of music, including their innate ingenuity, current social or political events, access to new instruments or tools, or other personal experiences. Our goal is to comprehend and measure the inﬂuence of previous music productions.

<!-- b000133 | prose | pages [4] -->
Many musicians admit that there are lots of predecessors who inﬂuence their works pro- foundly. It has also been suggested that inﬂuence can be measured by the degree of similarity between song characteristics, such as structure, rhythm, or lyrics. There are sometimes revolu- 微信号：MATHmodels tionary shifts in music, offering new sounds or tempos, such as when a new genre emerges, or there is a reinvention of an existing genre (e.g. classical, pop/rock, jazz, etc.). This can result from a sequence of small changes, a cooperative effort of artists, a series of inﬂuential artists, or a shift within society.

<!-- b000134 | prose | pages [4] -->
There are many artists who have contributed to the great shifts of music genres. Sometimes these shifts are due to one artist inﬂuencing another. Sometimes it is a change that emerges in response to external events (such as major world events or technological advances). By considering networks of songs and their musical characteristics, we can begin to capture the inﬂuence that musical artists have on each other. And we can also obtain a comprehensive picture of how music evolves through societies over time.

<!-- b000135 | heading | pages [4] -->
1.2 Our Work

<!-- b000136 | prose | pages [4] -->
Our work follows the following workﬂow, as shown in Figure 1.

<!-- b000137 | prose | pages [4] -->
Propose 5 Indicators Build a Music Influence Network Calculate Weights by EWM Construct a Subnetwork

<!-- b000138 | prose | pages [4] -->
Factor Analysis Design a Music Similarity Metric Construct a Similarity Matrix

<!-- b000139 | prose | pages [4] -->
Compare Similarities and Influence 3 Methods for distinguishment

<!-- b000140 | prose | pages [4] -->
Music Evolution Verify the actual influence Discover Contagious Features

<!-- b000141 | prose | pages [4] -->
Bollinger Band Predict a music revolution Moving Average (MA) Identify Revolution Representatives

<!-- b000142 | prose | pages [4] -->
Analyze music-influence process Seek for Dynamic Influencers

<!-- b000143 | prose | pages [4] -->
Re-consider the music revolution Find Social Source

<!-- b000144 | caption | pages [4] -->
Figure 1: Work Flow

<!-- b000145 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000146 | prose | pages [4, 5] -->
关注数学模型 • In Problem 1, we build a music inﬂuence network and propose 5 indicators to quanti- tively measure the inﬂuence of each musician: 1. Betweeness Centrality. 2. Eigenvector Centrality. 3. Three Degree of Inﬂuence. 4. Follower Loyalty. 5. Diversity of Inﬂuenced Genres. Then we use entropy weight method(EWM) to calculate the weight of each in- dicator and thus formulate the music inﬂuence of each musician. Based on Breadth-First 微信公众号：数学模型 Search(BFS) and the indicators above, we easily construct a subnetwork and reveal latent properties of the subnetwork.

<!-- b000147 | furniture | pages [4] -->
2

<!-- b000148 | furniture | pages [4] -->
MATHmodels

<!-- b000149 | furniture | pages [4] -->
获取更多资讯

<!-- b000150 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000151 | furniture | pages [5] -->
Team # 2106028

<!-- b000152 | furniture | pages [5] -->
Page 5 of 25

<!-- b000154 | prose | pages [5] -->
• In Problem 2, we design a Music Similarity Metric. By applying Factor Analysis to reduce dimensions, we obtain 3 components to describe the music features of each artist and further, each genre. We also construct a similarity matrix to quantify the similarity of artists within and between genres.

<!-- b000155 | prose | pages [5] -->
• In Problem 3, we compare similarities and inﬂuences between and within genres. Then we put forward 3 approaches to distinguish a genre and depict genre evolution and relations over time.

<!-- b000156 | prose | pages [5] -->
• In Problem 4, we verify whether inﬂuencers indeed affect the music features of the 微信号：MATHmodels followers through hypothesis testing, and discover that ‘acousticness’ and ‘energy’ are more ‘contagious’ than other features.

<!-- b000157 | prose | pages [5] -->
• In Problem 5, we use the three components from Problem 2 to draw time series diagrams.

<!-- b000158 | prose | pages [5] -->
We can predict the occurrence of a music revolution by observing whether the Moving Average(MA) crosses the Bollinger Band, and thus infer that 1961-1968 is a potential rev- olution period. We also identify Nat King Cole and The Beatles as representatives of revolutionaries.

<!-- b000159 | prose | pages [5] -->
• In Problem 6, we analyze the process of music inﬂuence and seek for dynamic inﬂu- encers, who are considered to play a guiding role in music evolution.

<!-- b000160 | prose | pages [5] -->
• In Problem 7, we re-consider the drastic music revolution in the 1960s, and ﬁnd its so- cial source is the counterculture movement in western countries. We also discuss the inﬂuence possibly induced by the development of Internet.

<!-- b000161 | heading | pages [5] -->
2 Problem 1: Network Building and Measures Development

<!-- b000162 | heading | pages [5] -->
2.1 Network Building

<!-- b000163 | prose | pages [5] -->
First, we create a directed network G = {V, E}(vi ∈V ) of musical inﬂuence, where each vertex vi = ⟨idi, gi, sti⟩represents a corresponding musician. As is known to all, musicians may be inﬂuenced by their predecessors and then inﬂuence future generations of musicians, so each vertex can be either an inﬂuencer or a follower. In fact, this network describes a one- to-many or many-to-one mapping between inﬂuencers and followers. Here, musician vi with ID idi and main genre gi started to inﬂuence others or to follow someone at time sti. We can easily obtain the data above from influence_data.

<!-- b000164 | prose | pages [5] -->
Then we connect inﬂuencers to followers with directed edges. Suppose e(i, j) denotes the directed edge (and its weight for simplicity) from inﬂuencer vi to follower vj. We can get Figure 2, where different colors represent different genres.

<!-- b000165 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000166 | prose | pages [5, 6] -->
关注数学模型 PJ Harvey The Beatles

<!-- b000167 | furniture | pages [5] -->
2

<!-- b000168 | furniture | pages [5] -->
MATHmodels

<!-- b000169 | furniture | pages [5] -->
获取更多资讯

<!-- b000170 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000171 | furniture | pages [6] -->
Team # 2106028

<!-- b000172 | furniture | pages [6] -->
Page 6 of 25

<!-- b000174 | prose | pages [6] -->
T. Rex Chuck Berry 微信公众号：数学模型 Dead Boys Doc Watson Alice Cooper Bob Dylan Cisco Houston Zucchero Paolo Conte

<!-- b000175 | prose | pages [6] -->
Mississippi Sheiks Joe Ely Steve Earle Joan Baez Planxty

<!-- b000176 | caption | pages [6] -->
Figure 2: A local example of music inﬂuence network

<!-- b000177 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000178 | heading | pages [6] -->
2.2 Music Inﬂuence Measures Development

<!-- b000179 | prose | pages [6] -->
In this paper, we mainly consider the genres and topology of the music inﬂuence network and propose 5 indicators to quantitatively measure the inﬂuence of nodes. We also give the calculation methods of these indicators as follows.

<!-- b000180 | prose | pages [6] -->
• Betweenness Centrality (BC)[3, 4] Betweenness Centrality refers to the number of times that one node acts as the short- est bridge between the other two nodes in a network. Obviously, a node with higher betweenness centrality will have more control over the network, as more inﬂuence will pass through that node. We can deﬁne the Betweenness Centrality of node v as

<!-- b000181 | prose | pages [6] -->
σst(v) X BC(v) = . σst s̸=v̸=t

<!-- b000182 | prose | pages [6] -->
Here, σst is the total number of shortest paths from node s to node t and σst(v) is the number of those paths that pass through v. Furthermore, we can normalize the results above and obtain a scaled betweenness centrality

<!-- b000183 | prose | pages [6] -->
g(v) −min(g) normal(BC(v)) = max(g) −min(g)

<!-- b000184 | prose | pages [6] -->
For simplicity, we denote normal(BC(v)) as BC(v) in the following paragraphs.

<!-- b000185 | prose | pages [6] -->
• Eigenvector Centrality (EC)[5, 6, 7, 1] We also take the neighbors’ inﬂuence of a node into account. Suppose that nodes with higher-inﬂuence neighbor nodes have higher inﬂuence on their descendant nodes and vise versa. A high eigenvector centrality score means that a node is connected to many nodes who themselves are highly inﬂuencial.

<!-- b000186 | prose | pages [6] -->
To calculate this indicator, we deﬁne the adjacency matrix of graph G as A = (av,t), i.e.

<!-- b000187 | prose | pages [6] -->
av,t = 1 if vertex v is linked to vertex t, and av,t = 0 otherwise. The eigenvector centrality of vertex v can be formulated as EC(v) = 1 EC(t) = 1 X X av,tEC(t) λ λ t∈G

<!-- b000188 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000189 | prose | pages [6, 7] -->
t∈I(v) 关注数学模型 where I(v) is a set of the inﬂuencers of v and λ is the largest eigenvalue of eigenvector equation Ax = λx.

<!-- b000190 | furniture | pages [6] -->
2

<!-- b000191 | furniture | pages [6] -->
MATHmodels

<!-- b000192 | furniture | pages [6] -->
获取更多资讯

<!-- b000193 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000194 | furniture | pages [7] -->
Team # 2106028

<!-- b000195 | furniture | pages [7] -->
Page 7 of 25

<!-- b000197 | prose | pages [7] -->
• Three Degree of Inﬂuence (TDI)[2] Fowler et al.[2] proposed Three Degree of Inﬂuence Rule, indicating that nodes can affect 微信公众号：数学模型 not only their neighbor nodes (one degree), but also the neighbor nodes of the neighbor nodes (two degrees), and even the neighbor nodes of the neighbor nodes of the neighbor nodes (three degrees). Inﬂuence between nodes will decline or disappear when it comes to more than three degrees.

<!-- b000198 | prose | pages [7] -->
To calculate the exact score of Three Degree of Inﬂuence of one node, we adopt Breadth- First Search (BFS) on vertex vi with depth equals to 3 and obtain a subnetwork Gi = {V (i), E(i)}, which contains the subsequent three generations of vi. We deﬁne Three De- gree of Inﬂuence of vi as TDI(vi) = |V (i)|.

<!-- b000199 | prose | pages [7] -->
That is, Three Degree of Inﬂuence of vi equals to the number of elements in the subnet- work Gi. The more descendants vi have, the higher inﬂuence it holds.

<!-- b000200 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000201 | prose | pages [7] -->
• Follower Loyalty (FL) We can infer that if a follower is inﬂuenced by many inﬂuencers, then the follower will be less loyal to each inﬂuencer compared with the case where a follower is only inﬂuenced by one inﬂuencer. On the other hand, if an inﬂuencer can inﬂuence more followers, then his music inﬂuence should be greater.

<!-- b000202 | prose | pages [7] -->
We assume that the sum of each follower’s loyalty ratios to all his inﬂuencers equals to 1, and it is evenly distributed to each of his inﬂuencers. Namely, the contribution of each follower’s loyalty to the inﬂuencer’s Follower Loyalty FL equals to the reciprocal of the follower’s In-Degree. Then we can get the Follower Loyalty of musician v by

<!-- b000203 | prose | pages [7] -->
X FL(v) = Loy(t) t∈F(v)

<!-- b000204 | prose | pages [7] -->
where follower t’s loyalty is deﬁned by

<!-- b000205 | prose | pages [7] -->
1 Loy(t) = ID(t)

<!-- b000206 | prose | pages [7] -->
Here, ID(t) represents In-Degree of node t. F(v) is a set consisting of the immediate suc- cessor nodes of node v, namely, the follower set of musician v. Obviously, the higher score of Loy(t) has, the more deeply the follower t was inﬂuenced by each of his inﬂu- encer.

<!-- b000207 | prose | pages [7] -->
• Diversity of Inﬂuenced Genres (DIG) It can be noticed from the dataset that follower’s main genre may be different from that of the inﬂuencer. Suppose that the more genres a musician inﬂuences, the more inﬂuential he is in the network. So we count the number of different genres in the subsequent three generations of each node and deﬁne Diversity of Inﬂuenced Genres of musician vi as

<!-- b000208 | prose | pages [7] -->
X DIG(vi) = 1{gj=gi} j∈V (i)

<!-- b000209 | prose | pages [7] -->
where ( 1, gj = gi, if 1{gj=gi} = 0, gj̸ = gi. if

<!-- b000210 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000211 | prose | pages [7, 8] -->
关注数学模型 Apparently, the ﬁrst four indicators reﬂect the topology of the network, and the last indicator reﬂects the inﬂuence genres.

<!-- b000212 | furniture | pages [7] -->
2

<!-- b000213 | furniture | pages [7] -->
MATHmodels

<!-- b000214 | furniture | pages [7] -->
获取更多资讯

<!-- b000215 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000216 | furniture | pages [8] -->
Team # 2106028

<!-- b000217 | furniture | pages [8] -->
Page 8 of 25

<!-- b000219 | prose | pages [8] -->
Now we can use these 5 indicators to develop the measurement of music inﬂuence. We adopt the entropy weight method(EWM) to caculate the weights of each indicator, denote by w1, w2, w3, w4, w5. To be more speciﬁc, the greater the dispersion degree of an indicator is, 微信公众号：数学模型 the greater its information entropy will be, and the greater the inﬂuence (i.e. weight) of the indicator on the response variable will be. If all the values of an indicator are equal, the index will play no role in the response variable. From this point, our target function Music Inﬂuence can be represent in Equation (1).

<!-- b000220 | prose | pages [8] -->
MI(v) = w1 · BC(v) + w2 · EC(v) + w3 · TDI(v) + w4 · FA(v) + w5 · DIG(v) (1)

<!-- b000221 | prose | pages [8] -->
Thus, musician v’s inﬂuence on follower t can be formulated as

<!-- b000222 | prose | pages [8] -->
MI(v)t = MI(v) · Loy(t) (2)   w1 · BC(v) + w2 · EC(v) + w3 · TDI(v) + w4 · FL(v) + w5 · DIG(v) · Loy(t) =

<!-- b000223 | prose | pages [8] -->
We put the results in Table 1 and Table 2. 微信号：MATHmodels

<!-- b000224 | caption | pages [8] -->
Table 1: Weights of 5 indicators by EWM

<!-- b000225 | prose | pages [8] -->
w1 w2 w3 w4 w5 0.1801 0.3163 0.2343 0.1152 0.1539

<!-- b000226 | caption | pages [8] -->
Table 2: Music Inﬂuence score of several artists

<!-- b000227 | prose | pages [8] -->
TDI BC EC DIG FL MI score Name Genre

<!-- b000228 | prose | pages [8] -->
The Beatles Pop/Rock 3758 0.017854 2.48E-05 18 72.9157 0.587118 Miles Davis Jazz 3588 0.024155 2.09E-05 18 19.53379 0.520501 Willie Nelson Country 1453 0.037038 0.000311 14 5.200698 0.479064 The Kingston Trio Folk 2195 0.029905 3.05E-05 16 2.317591 0.457585 Sly & the Family Stone R&B; 2932 0.021835 4.64E-05 18 6.813955 0.443942

<!-- b000229 | heading | pages [8] -->
2.3 Construct a Subnetwork

<!-- b000230 | prose | pages [8] -->
Using measurements in the previous subsection, we can easily create a subnetwork of the directed music inﬂuence network above. For inﬂuencer vi, we adopt Breadth-First Search (BFS) on vertex vi with depth equals to 3 and obtain a subnetwork Gi = {V (i), E(i)}, which contains the subsequent three generations of descendants of vi. We have the following de- scriptions of subnetwork Gi.

<!-- b000231 | prose | pages [8] -->
1. Betweenness Centrality indicates the importance of musician vi in the whole network, thus the importance of the subnetwork compared to the whole network. Furthermore, we can explore Betweenness Centrality of each node in the subnetwork and determine their importance compared to the subnetwork.

<!-- b000232 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000233 | prose | pages [8, 9] -->
关注数学模型 2. Eigenvector Centrality reveals how close musician vi connects with inﬂuential musi- cians. That is, the followers of more inﬂuential musicians have higher inﬂuence and therefore higher scores of Eigenvector Centrality. We can also extend this attribute to the subnetwork, measuring whether the musicians in the subnetwork are affected by extremely inﬂuential predecessors or not. 微信公众号：数学模型

<!-- b000234 | furniture | pages [8] -->
2

<!-- b000235 | furniture | pages [8] -->
MATHmodels

<!-- b000236 | furniture | pages [8] -->
获取更多资讯

<!-- b000237 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000238 | furniture | pages [9] -->
Team # 2106028

<!-- b000239 | furniture | pages [9] -->
Page 9 of 25

<!-- b000241 | heading | pages [9] -->
3. Three Degree of Inﬂuence represents the quantity of musicians inﬂuenced by musician

<!-- b000242 | prose | pages [9] -->
vi, which exactly equals to |v(i)|. As Three Degree of Inﬂuence Rule suggests, we can conclude that the inﬂuence of vi continues to the third generation. Evidently, the more descendants vi have, the higher inﬂuence it holds.

<!-- b000243 | prose | pages [9] -->
4. Follower Loyalty shows the extent of distraction of each follower, and in turn the dis- persion of inﬂuence. By applying this property to the subnetwork, we can determine the level of inﬂuence and the distribution of loyalty of each follower.

<!-- b000244 | prose | pages [9] -->
5. Diversity of Inﬂuenced Genres reveals the diversity of genres in the subnetwork. The more genres vi inﬂuenced, the higher inﬂuence it holds. Judging from this indicator of the subnetwork, we can also gain a general picture of how genres inﬂuenced each other and how they evoluted over time. 微信号：MATHmodels

<!-- b000245 | heading | pages [9] -->
3 Problem 2: Music Similarity Metric

<!-- b000246 | prose | pages [9] -->
In the provided dataset, a music masterpiece is recorded as a group of numerical features, including danceability, valence, acousticness, etc. These features characterize the music from certain perspectives, such as emotion, rhythm and melody, while some of them might be strongly correlated. For example, we learn from common sense that positive emotions are often conveyed by faster tempo in music, which indicates that valence and tempo might have positive correlation. To form an intuition about this, we conduct a correlation analysis on all informative features and the result is shown in Figure 3.

<!-- b000247 | prose | pages [9] -->
From Figure 3, it is clear that some features might have strong correlation with others, and thus the Euclidean distance in original feature space is not a reasonable metric for music simi- larity. To address this problem, we adopt Factor Analysis (FA), which views original features as linear combinations of latent variables, to form a lower dimension space, where the Euclidean distance has much better performance as the measurement for music similarity.

<!-- b000248 | prose | pages [9] -->
FA is a widely-used method for mining latent variables, which is also called components sometimes. For a dataset X ∈Rm×n, we assume X is produced by some invisible random variables H ∈Rm×d in a latent space with lower dimension d < n. The relationship between H and X has the form of Equation (3)

<!-- b000249 | prose | pages [9] -->
X = HW + M + E (3) where W ∈Rd×n is weight matrix of latent variables, M is the empirical mean of each feature estimated from the dataset, and E is the stochastic error term with zero mean.

<!-- b000250 | prose | pages [9] -->
Equation (3) indicates that we might conduct a linear transform, which turns X into H, and utilize the distance metric of H space to measure the similarity of music. We then use the stan- dard Factor Analysis function in the scikit-learn python package to obtain the representations of X in a 3-D latent space by setting dimension d = 3. The result is shown as Figure 4.

<!-- b000251 | prose | pages [9] -->
In Figure 4, we visualize each piece of music as a point in the latent space, and use the genre of the ﬁrst musician (Some of the work was completed by several musicians. In this case, we

<!-- b000252 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000253 | prose | pages [9, 10] -->
关注数学模型 微信公众号：数学模型 微信号：MATHmodels

<!-- b000254 | furniture | pages [9] -->
2

<!-- b000255 | furniture | pages [9] -->
MATHmodels

<!-- b000256 | furniture | pages [9] -->
获取更多资讯

<!-- b000257 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000258 | furniture | pages [10] -->
Team # 2106028

<!-- b000259 | furniture | pages [10] -->
Page 10 of 25

<!-- b000261 | caption | pages [10] -->
Figure 3: Correlation coefﬁcient matrix of music features

<!-- b000262 | caption | pages [10] -->
Figure 5: Music similarity between genres

<!-- b000263 | caption | pages [10] -->
Figure 4: Representations on 3-D latent space

<!-- b000264 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000265 | prose | pages [10, 11] -->
关注数学模型 choose only the ﬁrst musician in the given data to identify the genre of the work) to deter- mine its color. It is obvious that music pieces belonging to the same genre gather at a speciﬁc region. Meanwhile, different genres form separate ’clusters’ in the latent space. We can infer from the ﬁgure that music pieces of the same genre are more similar than pieces of different genres, which also meets people’s intuitions and conﬁrms the rationality and effectiveness of 微信公众号：数学模型 our solution.

<!-- b000266 | furniture | pages [10] -->
2

<!-- b000267 | furniture | pages [10] -->
MATHmodels

<!-- b000268 | furniture | pages [10] -->
获取更多资讯

<!-- b000269 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000270 | furniture | pages [11] -->
Team # 2106028

<!-- b000271 | furniture | pages [11] -->
Page 11 of 25

<!-- b000273 | prose | pages [11] -->
At the end of this section, we look into the problem of similarity within genre and between genres. In total we have ng = 20 genres including an Unknown for unlabelled artists. We construct a similarity matrix S = {Sij} ∈Rng×ng satisfy 1 X X Sij = sim (x, y) , (4) |gi||gj| x∈gi y∈gj

<!-- b000274 | prose | pages [11] -->
where ⟨x, y⟩ sim (x, y) = . (5) ∥x∥2∥y∥2 Here, x represent a musician from genre gi and y regresent a musician from genre gj. Sij measures the average similarity of artists between music genres gi and gj. We use the cosine 微信号：MATHmodels function on vectors as the metric sim (·) for music similarity, and show the results by drawing a heat map in Figure 5.

<!-- b000275 | prose | pages [11] -->
From Figure 5, we ﬁnd that the similarity within genre is usually higher than that between genres, as the elements on the diagonal are relatively larger. However, there are also a few exceptions, which might be due to the profound inﬂuence from great masters and inﬂuential genres to artists of newborn genres.

<!-- b000276 | heading | pages [11] -->
4 Problem 3: Genre Relation and Development

<!-- b000277 | heading | pages [11] -->
4.1 Similarity and Inﬂuence Comparison

<!-- b000278 | prose | pages [11] -->
Although musicians within a genre is prone to communicate more and create masterpieces in more similar styles, some newborn genres can also be deeply inﬂuenced by that genre and thus highly similar to others. At speciﬁc periods in history, a popular genre might form mul- tiple branches and ﬁnally be divided into new genres. Both cases shows that the development of genres are not isolated, but closely related. In this section, we mainly discuss the relation about derivation, which corresponds to the former case.

<!-- b000279 | prose | pages [11] -->
In Section 3, we have proposed a similarity for music, and obtain the average similarity as plotted in Figure 5. Generally speaking, the more accumulated loyalty a musician pays to a genre, the more he or she might be inﬂuenced by musicians of that genre. Therefore, we will take these two metric for the following discussion on the similarity and inﬂuence with genre and between genres.

<!-- b000280 | prose | pages [11] -->
Based on the inﬂuence network built in Section 2, we compute the total accumulated loyalty of all artists within genre to another as the weight of edge from the former genre to the latter, and plot the inﬂuence between genres in Figure 6. In this ﬁgure, we use the width and color of an arc between genres to represent the weight and source genre of the edge. For example, the black arc from R&B to Pop/Rock is wider than the green arc from Pop/Rock to Electronic, and this means the total accumulated loyalty paid to Pop/Rock by R&B artists are larger than that to Electronic by Pop/Rock artists.

<!-- b000281 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000282 | prose | pages [11, 12] -->
关注数学模型 E le ct ro ni c R & B;

<!-- b000283 | furniture | pages [11] -->
2

<!-- b000284 | furniture | pages [11] -->
MATHmodels

<!-- b000285 | furniture | pages [11] -->
获取更多资讯

<!-- b000286 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000287 | furniture | pages [12] -->
Team # 2106028

<!-- b000288 | furniture | pages [12] -->
Page 12 of 25

<!-- b000290 | prose | pages [12] -->
lk Fo

<!-- b000291 | prose | pages [12] -->
微信公众号：数学模型 zz Ja

<!-- b000292 | prose | pages [12] -->
C ou nt ry ck Bl Ro ue p/ s Po

<!-- b000293 | prose | pages [12] -->
Vo ca l La n ti

<!-- b000294 | caption | pages [12] -->
Figure 6: Inﬂuence within genre and between genres

<!-- b000295 | heading | pages [12] -->
4.2 Genre Distinguishment

<!-- b000296 | prose | pages [12] -->
微信号：MATHmodels Now we focus on mining signiﬁcant features for each genre and employ 3 approaches to distinguish a certain genre.

<!-- b000297 | heading | pages [12] -->
4.2.1 Low-Variance Features

<!-- b000298 | prose | pages [12] -->
For better interpretability, we return to the original high-dimension representation in the given dataset to seek common characteristics. From the theory of statistics, we know that the common features within a genre tends to have lower variance since its values are close to each other. To be speciﬁc, assume we have a musical feature c, in a dataset containing m examples, the mathematical expectation of sample variance will be

<!-- b000299 | prose | pages [12] -->
" m # 1 X (c −¯c)2 ≈Var (c) E m i=1

<!-- b000300 | prose | pages [12] -->
That means we can approximately substitute sample variance for population variance.

<!-- b000301 | heading | pages [12] -->
4.2.2 Analyzing Components

<!-- b000302 | prose | pages [12] -->
We can see from Figure 4 that after factor analysis, the feature coordinates of the same genre are inclined to gather together. By analyzing the distribution characteristics of each genre, we can summarize the features of each genre.

<!-- b000303 | heading | pages [12] -->
4.2.3 Outlier Detection

<!-- b000304 | prose | pages [12] -->
Some genres may be extreme in certain characteristics. Based on this consideration, we propose a method of drawing violin plots to detect whether some genres have extreme per- formance in certain characteristics (outlier detection). To be speciﬁc, we draw Figure 7 and

<!-- b000305 | caption | pages [12] -->
Figure 8. from these two ﬁgures, we can see that

<!-- b000306 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000307 | prose | pages [12, 13] -->
关注数学模型 微信公众号：数学模型

<!-- b000308 | furniture | pages [12] -->
2

<!-- b000309 | furniture | pages [12] -->
MATHmodels

<!-- b000310 | furniture | pages [12] -->
获取更多资讯

<!-- b000311 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000312 | furniture | pages [13] -->
Team # 2106028

<!-- b000313 | furniture | pages [13] -->
Page 13 of 25

<!-- b000315 | caption | pages [13] -->
Figure 7: Violin plot of instrumentalness in sev-

<!-- b000316 | caption | pages [13] -->
Figure 8: Violin plot of acousticness in several

<!-- b000317 | prose | pages [13] -->
eral genres genres

<!-- b000318 | prose | pages [13] -->
• The acousticness score of Vocal is higher than that of all other genres. So, we can distin- 微信号：MATHmodels guish Vocal from other genres by identifying acousticness.

<!-- b000319 | prose | pages [13] -->
• The instrumentalness score of New Age is higher than that of all other genres. So, we can distinguish New Age from other genres by identifying instrumentalness.

<!-- b000320 | heading | pages [13] -->
4.3 Genre Evolution and Relations

<!-- b000321 | prose | pages [13] -->
We specify the problem into three parts. The number of musicians and the number of works in a genre can reasonably represent the scale of that genre and thus descride genre evolution. Furtheremore, we also explore the change of each genre’s components to depict the trend.

<!-- b000322 | prose | pages [13] -->
4.3.1 How Does the Number of Musicians in a Genre Change Over Time?

<!-- b000323 | prose | pages [13] -->
In this part, we take influencer_active_start and follower_active_start into account. We have not yet considered the length of time a musician staying active (in fact, there is no data for us to consider). In particular, we select several genres and plot a trend chart of the number of musicians in the genres as is shown in Figure 9. Due to incomplete data collection after 2010, Figure 9 is only drawn to 2000 (2000-2010).

<!-- b000324 | caption | pages [13] -->
Figure 10: How the number of works in a genre

<!-- b000325 | caption | pages [13] -->
Figure 9: How the number of musicians in a

<!-- b000326 | prose | pages [13] -->
changes over time genre changes over time

<!-- b000327 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000328 | prose | pages [13, 14] -->
关注数学模型 We can see from Figure 9 that

<!-- b000329 | furniture | pages [13] -->
2

<!-- b000330 | furniture | pages [13] -->
MATHmodels

<!-- b000331 | furniture | pages [13] -->
获取更多资讯

<!-- b000332 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000333 | furniture | pages [14] -->
Team # 2106028

<!-- b000334 | furniture | pages [14] -->
Page 14 of 25

<!-- b000336 | prose | pages [14] -->
1. Pop/Rock has developed rapidly since 1940 with a large group of musicians.

<!-- b000337 | prose | pages [14] -->
2. Vocal, Religious, Electronic music have relatively smaller scales. 微信公众号：数学模型 3. All genres peaked in 1990-2000 and declined in 2000-2010.

<!-- b000338 | prose | pages [14] -->
4.3.2 How Does the Number of Works in a Genre Change Over Time?

<!-- b000339 | prose | pages [14] -->
On the other hand, we can also identify how genres change by tracking the number of works in them. Similarly, we select several genres and plot a trend chart of the number of works in the genres as is shown in Figure 10.

<!-- b000340 | prose | pages [14] -->
As shown in Figure 10, we can conclude that

<!-- b000341 | prose | pages [14] -->
1. Vocal music ﬂourished between 1920 and 1950, and then its number of works declined.

<!-- b000342 | prose | pages [14] -->
微信号：MATHmodels 2. Pop/Rock has develop rapidly since 1960 and reached its peak between 1970 and 1990.

<!-- b000343 | prose | pages [14] -->
3. Musicians-number and works-number of R&B have changed roughly synchronously.

<!-- b000344 | prose | pages [14] -->
4. Religious and Electronic are relatively small-scale and produce very limited works.

<!-- b000345 | prose | pages [14] -->
4.3.3 How Do the Features of Each Genre Change Over Time?

<!-- b000346 | prose | pages [14] -->
With time passed, the features of each genre may change dramatically. We use the result of factor analysis in Problem 2 to analyze the trend of the three components of different genres. Here, we still take those 5 genres previously selected as examples, and analyze acoustics- energy component and valence component to draw Figure 11 and Figure 12.

<!-- b000347 | caption | pages [14] -->
Figure 12: How Valence Component of a genre

<!-- b000348 | caption | pages [14] -->
Figure 11: How Acoustics-energy Component of

<!-- b000349 | prose | pages [14] -->
changes over time a genre changes over time

<!-- b000350 | caption | pages [14] -->
Figure 11 shows that in terms of acoustic energy component, Pop/Rock, Electronic, and

<!-- b000351 | prose | pages [14] -->
Religious music had a similar trend from 1920 to 1960, all of which surged in 1920 to 1930 and then fell back in the next 20 years. Acoustic-energy component of all genres ﬂuctuated in a small range from 1980 to 2010.

<!-- b000352 | prose | pages [14] -->
As for Valence component, there has been an overall upward trend in all genres from 1920 to the present. Among them, Electronic ﬂuctuated sharply from 1950 to 1980, while Vocal,

<!-- b000353 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000354 | prose | pages [14, 15] -->
关注数学模型 Religious and R&B approximately increased synchronously. It is worth noting that the Valence component of Pop/Rock dropped after reaching a local maximum value in 1930, but steadily increased since 1950.

<!-- b000355 | furniture | pages [14] -->
2

<!-- b000356 | furniture | pages [14] -->
MATHmodels

<!-- b000357 | furniture | pages [14] -->
获取更多资讯

<!-- b000358 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000359 | furniture | pages [15] -->
Team # 2106028

<!-- b000360 | furniture | pages [15] -->
Page 15 of 25

<!-- b000362 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000363 | heading | pages [15] -->
5 Problem 4: Similarity Veriﬁcation and Feature Mining

<!-- b000364 | prose | pages [15] -->
In this section, we will examine whether followers are indeed inﬂuenced by inﬂuencers from the network, i.e., whether those interrelated musicians in the directed music inﬂuence network will have higher similarities. We will use hypothesis testing to explore this problem.

<!-- b000365 | prose | pages [15] -->
( H0 : Followers are indeed inﬂuenced by inﬂuencers. (6) H1 : Followers are not completely inﬂuenced by inﬂuencers.

<!-- b000366 | prose | pages [15] -->
Before testing this hypothesis, we need to clarify a confusing concept.

<!-- b000367 | prose | pages [15] -->
Deﬁnition 1. (Similarity between musician x and y) As deﬁned in Equation (5), similarity between 微信号：MATHmodels musician x and y can be formulated as

<!-- b000368 | prose | pages [15] -->
⟨x, y⟩ sim (x, y) = , ∥x∥2∥y∥2

<!-- b000369 | prose | pages [15] -->
which is a combination of various musical features of the works of musician x and y.

<!-- b000370 | prose | pages [15] -->
In other words, musician x, y might be similar to each other in a certain feature or another, whereas sim (x, y) measures a comprehensive level of similarities in these features.

<!-- b000371 | prose | pages [15] -->
On the other hand, We hold the opinion that the interrelation between musician x and y on the music inﬂuence network is determined by the direct connection betwee x and y. Namely, as long as there exists a directed edge from x to y or from y to x, we consider x and y are interrelated.

<!-- b000372 | prose | pages [15] -->
Then, to test H0 in (6), we only need to verify that both those various features’ similarity and the similarity function in Equation (5) of interrelated musicians are higher than that of any two randomly selected musicians. To calculate the similarity function and each feature’s similarity, we put forward the following method.

<!-- b000373 | prose | pages [15] -->
1. There are 12 original features and 3 compound features(components), a total of 15 fea- tures. For the sake of storing two musicians to be compared, we set two arrays for each feature, namely, Ai, Bi(i = 1, 2, · · · , 15).

<!-- b000374 | prose | pages [15] -->
2. Pair the musicians and devide them into two groups:

<!-- b000375 | prose | pages [15] -->
( Group 1: Musician-pairs in which direct interrelation exists.

<!-- b000376 | prose | pages [15] -->
Group 2: Randomly-selected musician-pairs, which is considered to be unrelated.

<!-- b000377 | prose | pages [15] -->
3. Put the musical features i(i = 1, 2, · · · , 15) of the musicians in Group 1 into the array Ai(i = 1, 2, · · · , 15) and the other one in the pairs into Bi(i = 1, 2, · · · , 15).

<!-- b000378 | prose | pages [15] -->
4. Do Jarque-Bera test to verify whether the data in the array obey normal distribution. If yes, we will use Pearson correlation coefﬁcients in the following step. If no, we will apply Spearman correlation coefﬁcients.

<!-- b000379 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000380 | prose | pages [15, 16] -->
关注数学模型 5. Calculate the correlation coefﬁcients of each feature.

<!-- b000381 | furniture | pages [15] -->
2

<!-- b000382 | furniture | pages [15] -->
MATHmodels

<!-- b000383 | furniture | pages [15] -->
获取更多资讯

<!-- b000384 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000385 | furniture | pages [16] -->
Team # 2106028

<!-- b000386 | furniture | pages [16] -->
Page 16 of 25

<!-- b000388 | prose | pages [16] -->
6. Repeat Step 3-5 for Group 2.

<!-- b000389 | prose | pages [16] -->
7. Compare the results using hypothesis testing and draw conclusions.

<!-- b000390 | prose | pages [16] -->
微信公众号：数学模型 We show the results in Figure 13. All of the features have considerably higher Spearman correlation coefﬁcients in Group 1 than in Group2. After hypothesis testing, we can claim that the similarity caused by the connection between musicians is by no means accidental. There- fore, We can accept the null hypothesis H0: Followers are indeed inﬂuenced by inﬂuencers.

<!-- b000391 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000392 | caption | pages [16] -->
Figure 13: Spearman correlation coefﬁents of Group 1 and Group 2

<!-- b000393 | heading | pages [16] -->
6 Problem 5: Signals and Pioneers of Revolution

<!-- b000394 | heading | pages [16] -->
6.1 Identify Signals of Revolutions in Music Evolution

<!-- b000395 | prose | pages [16] -->
On the one hand, we know that some music genres may change rapidly over time. On the other hand, even if the music genre stays the same, we can still ﬁnd that the intrinsic characteristics of some genres have changed. Music evolution can be interpreted as the change of those three components found in Problem 2. A drastic music revolution is a period in which these three components change dramatically.

<!-- b000396 | prose | pages [16] -->
So, what is the period of dramatic change? To solve this problem, we draw a time sequence diagram of the three components over time, and analyze it by using Bollinger Bands, which is a conﬁdence interval band obtained by statistical methods. We adopt Bollinger Bands and slope of Moving Average(MA) as predictors of the musical revolution. In this section, we set the sliding window of the Bollinger Band as 3 years, and the standard deviation factor β = 2. The results are shown in Figure 14a, 14b, 14c.

<!-- b000397 | prose | pages [16] -->
According to the Pauta Criterion, if random variable X ∼N(µ, σ2), then

<!-- b000398 | prose | pages [16] -->
P(X ∈(µ −3σ, µ + 3σ)) ≈0.9973.

<!-- b000399 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000400 | prose | pages [16, 17] -->
关注数学模型 微信公众号：数学模型 (c) Instrumental Component (b) Valence Component (a) Acoustics Component

<!-- b000401 | furniture | pages [16] -->
2

<!-- b000402 | furniture | pages [16] -->
MATHmodels

<!-- b000403 | furniture | pages [16] -->
获取更多资讯

<!-- b000404 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000405 | furniture | pages [17] -->
Team # 2106028

<!-- b000406 | furniture | pages [17] -->
Page 17 of 25

<!-- b000408 | caption | pages [17] -->
Figure 14: Time series of components

<!-- b000409 | prose | pages [17] -->
We claim that a musical revolution occurred when MovingAverage(MA) broke through the Bollinger Bands with a high slope.

<!-- b000410 | prose | pages [17] -->
By analyzing Bollinger Bands and slope of Moving Average(MA) in Figure 14a, 14b, 14c, we ﬁnd that all of the 3 components broke through the Bollinger Bands during 1961-1968. Mean- while, the slopes of these three Moving Average(MA) are considerably high. Therefore, 1961- 微信号：MATHmodels 1968 is very likely to be the musical revolution we are looking for.

<!-- b000411 | heading | pages [17] -->
6.2 Discover Musicians Who Can Represent Revolutionary Changes

<!-- b000412 | prose | pages [17] -->
In Section 6.1, We ﬁgure out that 1961-1968 is very likely to be the period in which music revolution took place. In this section, we will seek for the musicians who may lead the music revolution from those who published their works during 1961-1968.

<!-- b000413 | prose | pages [17] -->
Through the music inﬂuence network established in problem 1, we trace the source of these music-revolution-leader candidates to ﬁnd relatively ‘sophisticated’ musicians. Music revolution leaders are those who have high MusicInfluence(MI) scores and at the same time, their features change in sync with that of the whole music industry.

<!-- b000414 | prose | pages [17] -->
As shown in Equation (7), we calculate The First Order of Temporal Correlation Coefﬁcient of one musician’s score and music industry’s average with regard to a ﬁxed feature, in order to determine whether the feature of that musician changes in sync with that of the whole music industry.

<!-- b000415 | prose | pages [17] -->
PT−1 t=1 (xt+1 −xt) · (averaget+1 −averaget) CORT(XT, AverageT) = (7) r qPT−1 t=1 (xt+1 −xt)2 · PT−1 t=1 (averaget+1 −averaget)2

<!-- b000416 | prose | pages [17] -->
Here, XT represents the time series of a certain characteristic of a musician. AverageT denotes the time series of music industry’s average value on this characteristic. xt, averaget is the value of XT, AverageT at time t.

<!-- b000417 | prose | pages [17] -->
If CORT(XT, AverageT) ≈1, then the two time series have similar trends and they will rise or fall simultaneously. Namely, that musician are very likely to be the leader of the music revolution in terms of the ﬁxed feature.

<!-- b000418 | prose | pages [17] -->
We can do this with pseudo-code in Algorithm 1.

<!-- b000419 | prose | pages [17] -->
Through looking up for ancestors in the music inﬂuence network, analzing of the Music Inﬂuence(MI), calculating the The First Order of Temporal Correlation Coefﬁcient between the mu-

<!-- b000420 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000421 | prose | pages [17, 18] -->
关注数学模型 Name Acoustics-energy Component Valence Component Instrumental Component

<!-- b000422 | furniture | pages [17] -->
2

<!-- b000423 | furniture | pages [17] -->
MATHmodels

<!-- b000424 | furniture | pages [17] -->
获取更多资讯

<!-- b000425 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000426 | furniture | pages [18] -->
Team # 2106028

<!-- b000427 | furniture | pages [18] -->
Page 18 of 25

<!-- b000428 | caption | pages [18] -->
Table 3: Dynamic Inﬂuencer Evaluation Index(DIEI) score in 1965 when c1 = 0.3, c2 = 0.5

<!-- b000430 | prose | pages [18] -->
The Beatles -0.018271926 -0.229203397 0.408461158 微信公众号：数学模型 Nat King Cole 0.142897328 0.040045023 0.052714147

<!-- b000431 | prose | pages [18] -->
sicians, and the music industry average, we ﬁnd the Beatles and Nat King Cole as the pioneers of this musical revolution, as shown in Table 6. As revolutionary might be promoted by sev- eral musicians, we might not observe very strong correlation between the mean of the whole community and a single musician.

<!-- b000432 | heading | pages [18] -->
Algorithm 1: Algorithm for ﬁnding revolutionary artists

<!-- b000433 | prose | pages [18] -->
Input: Inﬂuence network G, Inﬂuence threshold c1, Correlation threshold c2, Artist set S, Artist component matrix by year F = {F(y)} Output: List of revolutionary artists L 微信号：MATHmodels

<!-- b000434 | heading | pages [18] -->
1 Initialize L to ∅;

<!-- b000435 | heading | pages [18] -->
2 With Bollinger band computed before, select years Y = {y} in which revolutionaries

<!-- b000436 | prose | pages [18] -->
might happen; 3 for Each y ∈Y do Find all revolutionary artists A = {a} who published their works in y; 4 Mark revolutionary artists in G as candidates; 5 for Each a ∈A do 6 if An inﬂuencer of a is revolutionary then 7 Mark a with an extra eliminated symbol; 8 end 9 end 10 Eliminate all artists a with eliminated symbol from A; 11 Compute the inﬂuence score for each a remained in A and sort them by score; 12 for Each a ∈A and inﬂuence score of a is larger than c1 do 13 Compute a trend correlation coefﬁcient s for a; 14 if s is larger than c2 then 15 Recognize a as a revolutionary artist and append a to L 16 end 17 end 18 19 end 20 return The list of revolutionary artists L;

<!-- b000437 | heading | pages [18] -->
7 Problem 6: Case Study on Dynamic Inﬂuencers

<!-- b000438 | heading | pages [18] -->
7.1 Music Evolution over Time

<!-- b000439 | prose | pages [18] -->
We believe that there is(are) one(or many) leader(s) (that is, dynamic inﬂuencer) within a genre who lead the evolution of the whole genre. Only musicians with great music inﬂuence

<!-- b000440 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000441 | prose | pages [18, 19] -->
关注数学模型 can perform such a role. Therefore, the dynamic inﬂuencers must be those contemporary musicians who are most popular and inﬂuential. In particular, the evolution trend of the whole genre and the leader should be approximately the same. Many musicians in the genre may follow those leaders in their creation.

<!-- b000442 | furniture | pages [18] -->
2

<!-- b000443 | furniture | pages [18] -->
MATHmodels

<!-- b000444 | furniture | pages [18] -->
获取更多资讯

<!-- b000445 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000446 | furniture | pages [19] -->
Team # 2106028

<!-- b000447 | furniture | pages [19] -->
Page 19 of 25

<!-- b000449 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000450 | heading | pages [19] -->
7.2 Indicators of Dynamic Inﬂuencers

<!-- b000451 | prose | pages [19] -->
Now we take a further step to identify indicators that reveal the leaders(dynamic inﬂu- encers). We raise 3 indicators to sole this problem.

<!-- b000452 | prose | pages [19] -->
1. Music Inﬂuence score(MI score). From Problem 1 we obtain Music Inﬂuence scores of each musician which are employed as an indicator in this section.

<!-- b000453 | prose | pages [19] -->
2. AveragePopularity score of each musician. Dataset full_music_data provide us with he Popularity of each work (Popularity). Suppose that every musician will get the corre- sponding Popularity score as long as he gets involved in the creation of the work.

<!-- b000454 | prose | pages [19] -->
微信号：MATHmodels 3. TotalPopularity score of each musician.

<!-- b000455 | prose | pages [19] -->
Note that Music Inﬂuence score(MI score) does not vary over time because we do not have relevant data as support, whereas Popularity score is measured by year. We still adopt En- tropy Weight Method(EWM) to calculate the weights of the above three indicators, which will change over year. Now we can represent Dynamic Inﬂuencer Evaluation Index(DIEI) of mu- sician v in Equation (8).

<!-- b000456 | prose | pages [19] -->
DIEI(v) = w1(t) · MI(v) + w2(t) · POPAverage(v, t) + w3(t) · POPTotal(v, t) (8)

<!-- b000457 | prose | pages [19] -->
Thus, the Dynamic Inﬂuencer Evaluation Index(DIEI) score of this question can be obtained, and the musicians with the highest score in each genre will be selected as the dynamic inﬂuencer. We draw a graph of the weight over time in Figure 15 and Then we take the data in 1965 for example, calculate the weights of 3 indicators as shown in Table 4 and list some of the results in Table 5.

<!-- b000458 | caption | pages [19] -->
Table 4: Weights of 3 indicators in 1965

<!-- b000459 | prose | pages [19] -->
w1 w2 w3

<!-- b000460 | prose | pages [19] -->
0.09355 0.40601 0.50043

<!-- b000461 | caption | pages [19] -->
Figure 15:

<!-- b000462 | prose | pages [19] -->
How weights of 3 indicators change over time

<!-- b000463 | heading | pages [19] -->
7.3 Interaction Between Genre and its Musician

<!-- b000464 | prose | pages [19] -->
Based on the approaches in Section 7.2, we can successfully identify those dynamic inﬂu- encers and we show some of our results in Figure 16a and Figure 16b. For visualization, we set 3 years as the Lag of Moving Average(MA), namely, the genre mean.

<!-- b000465 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000466 | prose | pages [19, 20] -->
关注数学模型 MI score POPAverage POPTotal DIEI score name genre

<!-- b000467 | furniture | pages [19] -->
2

<!-- b000468 | furniture | pages [19] -->
MATHmodels

<!-- b000469 | furniture | pages [19] -->
获取更多资讯

<!-- b000470 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000471 | furniture | pages [20] -->
Team # 2106028

<!-- b000472 | furniture | pages [20] -->
Page 20 of 25

<!-- b000473 | caption | pages [20] -->
Table 5: Dynamic Inﬂuencer Evaluation Index(DIEI) score of several artists in 1965

<!-- b000475 | prose | pages [20] -->
The Beatles Pop/Rock 0.587118 59.10714 1655 0.913469 微信公众号：数学模型 Bob Dylan Pop/Rock 0.428424 28.58571 2001 0.765057 Otis Redding R&B; 0.292864 29.13846 1894 0.720494 The Rolling Stones Pop/Rock 0.392363 29.83333 1790 0.715112

<!-- b000476 | prose | pages [20] -->
微信号：MATHmodels (a) Evolution of acousticness (b) Evolution of danceability

<!-- b000477 | caption | pages [20] -->
Figure 16: Evolution of Latin’s leaders and genre-mean

<!-- b000478 | prose | pages [20] -->
From Figure 16a and Figure 16b, we can clearly see that

<!-- b000479 | prose | pages [20] -->
• The leaders (dynamic inﬂuencers) in a genre play a guiding role in genre evolution.

<!-- b000480 | prose | pages [20] -->
• The evolution of the leaders is basically in sync with that of the genre.

<!-- b000481 | prose | pages [20] -->
• The features of leaders ﬂuctuate sharply, indicating that leaders are minority groups in each genre, making the indicators of leaders more sensitive to extreme values.

<!-- b000482 | prose | pages [20] -->
• The genre-mean reﬂects the average level of that indicator within the genre, so the vari- ation is relatively moderate.

<!-- b000483 | heading | pages [20] -->
8 Problem 7: The Sociality of Music

<!-- b000484 | prose | pages [20] -->
Music world is not an isolated island, as any changes in the real world might have a sig- niﬁcant and profound inﬂuence on the developing trend of music within a period of several years. In this section we will take the revolution happend in the 1960s, which was discussed only from the perspective of music feature above, as an example to show the sociality of music.

<!-- b000485 | prose | pages [20] -->
According to the modern western history, there was once a counterculture movement lasted from the 1960s to the 1970s. As the era unfolded, what emerged were new cultural forms and a dynamic subculture that celebrated experimentation, modern incarnations of Bo- hemianism, and the rise of the hippie and other alternative lifestyles. This embrace of creativ- ity is particularly notable in the works of British Invasion bands such as the Beatles [8]. Music, as a sort of culture, get deeply affected during this extraordinary period, and it became more bolshy, more unrestrained and more emotional, which we can also observe from Figure 16a and 16b. It was in this era that Pop/Rock had developed at an astonishing speed and gained much more popularity. We can ﬁnd the trace of this movement from data in many ways.

<!-- b000486 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000487 | prose | pages [20, 21] -->
关注数学模型 It is worth mentioning that the rapid and wide spread of the Internet is another example which shows reﬂects the external inﬂuence on music. The Internet provides a fast and con- vinient way for music spread, and also promotes fan economy and the leisure industry. The former helps great masterpieces to harvest more popularity while the latter might lead to the formation of many non-mainstream styles. Due to space limitation, we do not discuss it deeply 微信公众号：数学模型 here, and this topic might be fully explored when more sufﬁcient and fresh data are provided.

<!-- b000488 | furniture | pages [20] -->
2

<!-- b000489 | furniture | pages [20] -->
MATHmodels

<!-- b000490 | furniture | pages [20] -->
获取更多资讯

<!-- b000491 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000492 | furniture | pages [21] -->
Team # 2106028

<!-- b000493 | furniture | pages [21] -->
Page 21 of 25

<!-- b000495 | heading | pages [21] -->
9 Sensitivity Analysis

<!-- b000496 | heading | pages [21] -->
9.1 Sensitivity of Moving Average Window

<!-- b000497 | prose | pages [21] -->
In Section 6, we set the moving average window to 3-year to better capture the overall developing trend and the signals of revolution in music community. This is somehow a hyper- parameter in our model, and we choose different values here to verify the choice of 3-year.

<!-- b000498 | prose | pages [21] -->
Adjust the window length to 5-year and 9-year, we can obtain the moving average results 微信号：MATHmodels and corresponding Bollinger Bands as shown in Figure 17.

<!-- b000499 | prose | pages [21] -->
(b) Valence, W = 5 (c) Instrumental, W = 5 (a) Acoustics, W = 5

<!-- b000500 | prose | pages [21] -->
(e) Valence, W = 9 (f) Instrumental W = 9 (d) Acoustics, W = 9

<!-- b000501 | caption | pages [21] -->
Figure 17: Times series of components

<!-- b000502 | prose | pages [21] -->
From the ﬁgures above we can see that as the sliding window becomes longer, the curve becomes smoother, and the revolutions are harder to detect. However, the overall trend and the breakthrough made by revolutionaries remains roughly the same, which proves the stabil- ity of our method, as well as the choice of 3-year sliding window, considering the purpose of detect revolutions.

<!-- b000503 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000504 | prose | pages [21] -->
关注数学模型

<!-- b000505 | furniture | pages [21] -->
2

<!-- b000506 | furniture | pages [21] -->
MATHmodels

<!-- b000507 | furniture | pages [21] -->
获取更多资讯

<!-- b000508 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000509 | furniture | pages [22] -->
Team # 2106028

<!-- b000510 | furniture | pages [22] -->
Page 22 of 25

<!-- b000511 | heading | pages [22] -->
9.2 Sensitivity of Revolutionary Threshold

<!-- b000512 | prose | pages [22] -->
Another important hyper-parameter in our model is the inﬂuence and correlation thresh- old for detecting revolutionary pioneers. In Section 6.2, we critical value c1 = 0.3 and c2 = 0.5, now we take other values for c1 and c2 to verify the stability of our model here. 微信公众号：数学模型

<!-- b000513 | caption | pages [22] -->
Table 6: Dynamic Inﬂuencer Evaluation Index(DIEI) score in 1965 when c1 = 0.3, c2 = 0.5

<!-- b000514 | prose | pages [22] -->
Name Acoustics-energy Component Valence Component Instrumental Component

<!-- b000515 | prose | pages [22] -->
The Beatles -0.018271926 -0.229203397 0.408461158 Nat King Cole 0.142897328 0.040045023 0.052714147

<!-- b000516 | caption | pages [22] -->
Table 7: Dynamic Inﬂuencer Evaluation Index(DIEI) score in 1965 when c1 = 0.6, c2 = 0.9

<!-- b000517 | prose | pages [22] -->
Name Acoustics-energy Component Valence Component Instrumental Component

<!-- b000518 | prose | pages [22] -->
微信号：MATHmodels The Beatles -0.019367252 -0.257729132 0.430968754 Nat King Cole 0.127946278 0.083617453 0.059204672

<!-- b000519 | prose | pages [22] -->
As is clear in Table 6 and Table 7, although the result can possibly change a little bit when the two hyper-parameters are set to different values, our algorithm can always ﬁnd a decent pioneer the revolutions. This shows that our algorithm is not sensitive to these two parameters and can keep working well in a wide range.

<!-- b000520 | heading | pages [22] -->
10 Strengths and Weaknesses

<!-- b000521 | heading | pages [22] -->
10.1 Strengths

<!-- b000522 | heading | pages [22] -->
1. Comprehensive and reasonable measures for network and music.

<!-- b000523 | prose | pages [22] -->
We select several indices for the inﬂuence network of musicians, and each of them re- spectively describes the property of network from some different perspectives. As for the similarity, we analyze the correlation between music features from the dataset and propose a metric based on factor analysis and cosine similarity. Both of the two metrics comes up with full consideration.

<!-- b000524 | heading | pages [22] -->
2. Effective data-driven methods for data insights without human interference.

<!-- b000525 | prose | pages [22] -->
We utilize powerful and effective statistical methods, such as correlation analysis, factor analysis, hypothesis test, etc. to explore patterns of data. We also use entropy weight method to determine weights for factors when computing the score of music inﬂuence.

<!-- b000526 | prose | pages [22] -->
Most parts of our model are fully data-driven, which rules out possible impacts induced by human interference. We just let data speak.

<!-- b000527 | heading | pages [22] -->
3. Analysis from latent and feature spaces with high visual interpretability.

<!-- b000528 | prose | pages [22] -->
As the original features of music locate in a high-dimension space, we can hardly master the mathematical and numerical properties of their distances. Therefore, we lower the number of dimension by extract major factors and visualize the distribution of music in the latent space, which improves the interpretability of our model. In addition, we

<!-- b000529 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000530 | prose | pages [22, 23] -->
关注数学模型 perform analysis in either space according to our actual demands, and this enhances the expressive power and ﬂexibility.

<!-- b000531 | furniture | pages [22] -->
2

<!-- b000532 | furniture | pages [22] -->
MATHmodels

<!-- b000533 | furniture | pages [22] -->
获取更多资讯

<!-- b000534 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000535 | furniture | pages [23] -->
Team # 2106028

<!-- b000536 | furniture | pages [23] -->
Page 23 of 25

<!-- b000538 | heading | pages [23] -->
10.2 Weaknesses

<!-- b000539 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000540 | heading | pages [23] -->
1. Inadequate data for full utilization of data-driven model.

<!-- b000541 | prose | pages [23] -->
As discussed in the strengths of our model, we hear the voice of data without much hu- man interference. However, we have access to only a small part of music dataset, which might lead to problems like distribution mismatch of music works, misjudegement on the developing trend of genres, etc. When the dataset is larger and cleaner, these prob- lems are likely to be lessened.

<!-- b000542 | heading | pages [23] -->
2. Appropriate simpliﬁcation of indirect musical inﬂuence.

<!-- b000543 | prose | pages [23] -->
In Problem 4, we adopt an alternative approach by deﬁning an REL function, to repre- sent Interrelationship between musician x and y, which is determined by the reciprocal of harmonic mean of shortest path between two points. However, the correlation coef- ﬁcients calculated by this method is very small and the results are not satisfying. So we 微信号：MATHmodels give up this method, which might be reasonable to some extent.

<!-- b000544 | heading | pages [23] -->
3. Neglect indirect-connected musicians.

<!-- b000545 | prose | pages [23] -->
In Problem 4, we only consider the nodes having direct interrelations whereas neglect the potential interrelations between indirect-connected nodes. As Three Degree of Inﬂuence suggests, a musician can inﬂuence his successors up to three generations. In fact, we have tried to take three generations of successors into account, the results are still not satisfying.

<!-- b000546 | heading | pages [23] -->
11 Conclusion

<!-- b000547 | prose | pages [23] -->
In this paper, we systematically study inﬂuence of music through networks and our results: First, we construct music inﬂuence network, derive the inﬂuence score based on four network metrics. Second, we ﬁnd strong correlation between music features and thus measure music similarity in a latent space of three main components by factor analysis. Third, we discuss the similarity, inﬂuence and relation within genre and between genres, propose to distinguish genre by outlier detection, and describe the process of genre changing over time. Fourth, we prove the actual inﬂuence of reported inﬂuencers and ﬁnd more contagious features of music. Fifth, we observe revolutionary in the 1960s and discover that Nat King Cole and The Beatles represents this revolutionary. Sixthly, we claim that there are dynamic inﬂuencers playing a leader role of a genre, who guides the trend of genre developing and interact with the whole genre closely. Last, we discuss the sociality of music taking the revolutionary in the 1960s as example and the signiﬁcant and possible inﬂuence of Internet.

<!-- b000548 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000549 | prose | pages [23] -->
关注数学模型

<!-- b000550 | furniture | pages [23] -->
2

<!-- b000551 | furniture | pages [23] -->
MATHmodels

<!-- b000552 | furniture | pages [23] -->
获取更多资讯

<!-- b000553 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000554 | furniture | pages [24] -->
Team # 2106028

<!-- b000555 | furniture | pages [24] -->
Page 24 of 25

<!-- b000556 | heading | pages [24] -->
12 Document to the ICM Society

<!-- b000557 | prose | pages [24] -->
Dear ICM Society,

<!-- b000558 | prose | pages [24] -->
The culture and art industry has witnessed an unprecedented boom recently. Among these 微信公众号：数学模型 popular productions, musical pieces are the most inﬂuential. Accurately identifying music inﬂuence and mining important features are of vital importance to understand the evolution of music. As response to your association’s requirement, we are here pretty glad to have the opportunity to introduce our research and ﬁndings to you, with the hope that it may give you some insights of future music development.

<!-- b000559 | prose | pages [24] -->
It is a great opportunity to build a music inﬂuence network through which we have found the factors that affect a musician’s inﬂuence in the music industry. By our model we can predict the development trend of music well.Music is an important ﬁeld in culture. If we can predict the development trend of music well, We can quickly complete the transformation of music and culture and maintain a leading position in the music revolution. Therefore, our method has high academic and economic value.

<!-- b000560 | prose | pages [24] -->
Due to limited time and energy, we mainly use some relatively basic and reliable models 微信号：MATHmodels for data mining. But as the amount of data increases, ordinary machine learning models can no longer meet our demand for higher precision. We can consider using LSTM/VAE to analyze time series, using graph neural network for social network analysis and so on.

<!-- b000561 | prose | pages [24] -->
We recognize that the development of music is affected by the social environment. Music and culture both promote and restrict each other. The appearence of music is closely related to culture. Music is rooted in culture, and it blends with, relies on and promotes each other. From the music of a period, we can see the speciﬁc environment of this period and the cultural characteristics of different ethnic groups and different regions. Music can promote the cultural development of the same period. Good music can inspire and purify the soul. Therefore, music originates from culture, but at the same time it is higher than culture.Culture is the concepts and thoughts formed by a nation or country in a period of time. It represents the values and behaviors of this nation and nation, and reﬂects the state of life of this group in a certain period of time. Music inﬂuences and infects people’s thoughts and hearts through the inﬂuence of beauty. It is a bridge connecting national culture and regional culture and the best way to sustain national culture.

<!-- b000562 | prose | pages [24] -->
We are really appreciated for this opportunity to assist you in exploring music evolution and comprehending the inﬂuence of music by building networks, and we are convinced that our approach can be utilized in future music evolution. Please feel free to contact us for further information on this project.

<!-- b000563 | prose | pages [24] -->
Sincerely yours, MCM 2021 Team

<!-- b000564 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000565 | prose | pages [24] -->
关注数学模型

<!-- b000566 | furniture | pages [24] -->
2

<!-- b000567 | furniture | pages [24] -->
MATHmodels

<!-- b000568 | furniture | pages [24] -->
获取更多资讯

<!-- b000569 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000570 | furniture | pages [25] -->
Team # 2106028

<!-- b000571 | furniture | pages [25] -->
Page 25 of 25

<!-- b000572 | heading | pages [25] -->
References

<!-- b000573 | references | pages [25] -->
[1] Stephen P Borgatti. Centrality and network ﬂow. Social networks, 27(1):55–71, 2005.

<!-- b000574 | references | pages [25] -->
[2] James H Fowler and Nicholas A Christakis. Dynamic spread of happiness in a large social

<!-- b000575 | references | pages [25] -->
微信公众号：数学模型

<!-- b000576 | references | pages [25] -->
network: longitudinal analysis over 20 years in the framingham heart study. Bmj, 337,

<!-- b000577 | references | pages [25] -->
2008.

<!-- b000578 | references | pages [25] -->
[3] Linton C Freeman. A set of measures of centrality based on betweenness. Sociometry, pages

<!-- b000579 | references | pages [25] -->
35–41, 1977.

<!-- b000580 | references | pages [25] -->
[4] Mark EJ Newman. A measure of betweenness centrality based on random walks. Social

<!-- b000581 | references | pages [25] -->
networks, 27(1):39–54, 2005.

<!-- b000582 | references | pages [25] -->
[5] Mark EJ Newman. The mathematics of networks. The new palgrave encyclopedia of economics,

<!-- b000583 | references | pages [25] -->
2(2008):1–12, 2008.

<!-- b000584 | references | pages [25] -->
[6] Britta Ruhnau. Eigenvector-centrality—a node-centrality? Social networks, 22(4):357–365,

<!-- b000585 | references | pages [25] -->
2000.

<!-- b000586 | references | pages [25] -->
微信号：MATHmodels

<!-- b000587 | references | pages [25] -->
[7] Karen Stephenson and Marvin Zelen. Rethinking centrality: Methods and examples. Social

<!-- b000588 | references | pages [25] -->
networks, 11(1):1–37, 1989.

<!-- b000589 | references | pages [25] -->
[8] Wikipedia. Counterculture of the 1960s, 2021.

<!-- b000590 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000591 | references | pages [25] -->
关注数学模型

<!-- b000592 | furniture | pages [25] -->
2

<!-- b000593 | furniture | pages [25] -->
MATHmodels

<!-- b000594 | furniture | pages [25] -->
获取更多资讯
