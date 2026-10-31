# P-D-2021-2124668-12f9e4f1

Status: machine-draft; not source-verified.


<!-- b000001 | heading | pages [1] -->
SUMMARY

<!-- b000002 | front_matter | pages [1] -->
TEAM 2124668

<!-- b000003 | prose | pages [1] -->
From trained musicologists to outspoken hipsters, everyone believes they know the greatest musicians and greatest periods of music. Our goal was to use data describing artist influence and sound content in order to perform a quantitative analysis of the last 90 years of musical history.

<!-- b000004 | prose | pages [1] -->
First, we sought to identify the most influential artists by considering four distinct types of influence: direct, indirect, within genre, and across genre. Our key metric of influence was Katz centrality, which we refined to incorporate time and directness. Focusing on 21st century music, we determined Frank Ocean had the greatest overall influence.

<!-- b000005 | prose | pages [1] -->
We then developed a measure of musical similarity and wondered whether or not genre groupings are based on sonic characteristics. We trained a neural network to predict genres from sonic data inputs like danceability and tempo. It did not accurately predict established genres unless we limited the number of genres to the four largest. This failure inspired us to use k-means clustering on the sonic variable space to create original “sonic genres,” offering a perspective on music which is agnostic of familiar labels. When we use this partition map on the influence network, we calculate a modularity of Q = 0.17.

<!-- b000006 | prose | pages [1] -->
Next, we focused on identifying musical revolutions, since we heard such moments are not always televised [1]. We considered revolutions of four different types: revolutions of mainstream music, revolutions of established genres, revolutions of our “sonic genres,” and revolutions when specific genres exert more influence on the mainstream. We classified our first three types of revolution based on the greatest changes of a centroid point, an average of sonic characteristics weighted by popularity. We classified the final type of revolution based on the relative position of a genre’s centroid to the mainstream centroid. We then developed specified criteria to determine the musical revolutionaries most responsible for each musical leap.

<!-- b000007 | prose | pages [1] -->
Finally, we compared our revolutions to several accounts of musical history. We found that most of our revolutions matched up with moments of great political, social, or technological change. For instance, the Pop/Rock genre became much more mainstream in the 1960s with the British Invasion. We also speculated that the revolutions which did not clearly align with known history represent more subtle developments in music captured by our model. In particular, we determined a revolution occurred in one of our “sonic genres,” which may be invisible to historians who exclusively examine music through the lens of established genres.

<!-- b000008 | references | pages [1] -->
[1] Gil Scott-Heron. The Revolution Will Not be Televised.

<!-- b000009 | furniture | pages [1] -->
关注数学模型 获取更多资讯

<!-- b000010 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000011 | contents | pages [2] -->
S O N I C & I C O N I C

<!-- b000012 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000013 | contents | pages [2] -->
Establishing sound-based genres and using an inﬂuence network to discover music revolutions in

<!-- b000014 | contents | pages [2] -->
historical context

<!-- b000015 | contents | pages [2] -->
team 2124668

<!-- b000016 | heading | pages [2] -->
Contents

<!-- b000017 | contents | pages [2] -->
1

<!-- b000018 | contents | pages [2] -->
0

<!-- b000019 | contents | pages [2] -->
Problem Statement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | contents | pages [2] -->
2

<!-- b000021 | contents | pages [2] -->
1

<!-- b000022 | contents | pages [2] -->
Background Research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000024 | contents | pages [2] -->
3

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | contents | pages [2] -->
Assumptions & Rationales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
4

<!-- b000028 | contents | pages [2] -->
2

<!-- b000029 | contents | pages [2] -->
Table of Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
5

<!-- b000031 | contents | pages [2] -->
2

<!-- b000032 | contents | pages [2] -->
Model Development . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
5.1

<!-- b000034 | contents | pages [2] -->
2

<!-- b000035 | contents | pages [2] -->
Measuring the Inﬂuence of Artists in a Network . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
5.2

<!-- b000037 | contents | pages [2] -->
6

<!-- b000038 | contents | pages [2] -->
Musical Similarity Metric and Sonic Genres . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
5.3

<!-- b000040 | contents | pages [2] -->
10

<!-- b000041 | contents | pages [2] -->
Analyzing Established Genres . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
5.4

<!-- b000043 | contents | pages [2] -->
11

<!-- b000044 | contents | pages [2] -->
Inﬂuence vs. Sonic Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000045 | contents | pages [2] -->
5.5

<!-- b000046 | contents | pages [2] -->
13

<!-- b000047 | contents | pages [2] -->
Musical Evolution in Terms of Revolutions and Revolutionaries . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
5.6

<!-- b000049 | contents | pages [2] -->
16

<!-- b000050 | contents | pages [2] -->
Musical Evolution of R&B . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
5.7

<!-- b000052 | contents | pages [2] -->
16

<!-- b000053 | contents | pages [2] -->
Historical Impact of Technology on Sound, Genre, and Inﬂuence . . . . . . . . . . . . . . . .

<!-- b000054 | contents | pages [2] -->
6

<!-- b000055 | contents | pages [2] -->
17

<!-- b000056 | contents | pages [2] -->
Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
7

<!-- b000058 | contents | pages [2] -->
18

<!-- b000059 | contents | pages [2] -->
Error Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
8

<!-- b000061 | contents | pages [2] -->
18

<!-- b000062 | contents | pages [2] -->
Conclusions

<!-- b000063 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000064 | contents | pages [2] -->
8.1

<!-- b000065 | contents | pages [2] -->
19

<!-- b000066 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | contents | pages [2] -->
8.2

<!-- b000068 | contents | pages [2] -->
19

<!-- b000069 | contents | pages [2] -->
Weaknesses

<!-- b000070 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
9

<!-- b000072 | contents | pages [2] -->
19

<!-- b000073 | contents | pages [2] -->
Future Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
10 Letter to ICM

<!-- b000075 | contents | pages [2] -->
20

<!-- b000076 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
1

<!-- b000078 | contents | pages [2] -->
Problem Statement

<!-- b000079 | contents | pages [2] -->
Our goal is to construct a data-based model which analyzes musical inﬂuence in terms of genre and content

<!-- b000080 | contents | pages [2] -->
over the past 90 years. First, we determine a way to quantify the inﬂuence of individual artists based only

<!-- b000081 | contents | pages [2] -->
on the influence data ﬁle. Next, we use full music data ﬁle to develop a metric of musical similarity. We

<!-- b000082 | contents | pages [2] -->
apply this measure to analyze how genres are distinguished, how they relate to one another, and how they

<!-- b000083 | contents | pages [2] -->
change over time. Then, we analyze inﬂuencer-follower relationships with our musical similarity metric,

<!-- b000084 | contents | pages [2] -->
pinpointing the musical characteristics most correlated with inﬂuence. At this point, we will use all our

<!-- b000085 | contents | pages [2] -->
quantitative tools to identify both moments of musical revolution as well as musical revolutionaries. We

<!-- b000086 | contents | pages [2] -->
will then turn our focus to a speciﬁc genre, applying our tools to provide insight into the musical evolution

<!-- b000087 | contents | pages [2] -->
of this category. Finally, we will compare the revolutions we identiﬁed to a historical timeline of social and

<!-- b000088 | contents | pages [2] -->
political developments in musical evolution.

<!-- b000089 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000090 | furniture | pages [2] -->
关注数学模型

<!-- b000091 | furniture | pages [2] -->
2

<!-- b000092 | furniture | pages [2] -->
0

<!-- b000093 | furniture | pages [2] -->
MATHmodels

<!-- b000094 | furniture | pages [2] -->
获取更多资讯

<!-- b000095 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000096 | furniture | pages [3] -->
team 2124668

<!-- b000097 | furniture | pages [3] -->
page 1

<!-- b000098 | contents | pages [3] -->
2

<!-- b000099 | contents | pages [3] -->
Background Research

<!-- b000100 | contents | pages [3] -->
Throughout the last few decades, mathematicians have employed a variety of quantitative and data-based

<!-- b000101 | contents | pages [3] -->
tools to analyze music in terms of inﬂuence, genre, and sonic content.

<!-- b000102 | contents | pages [3] -->
微信公众号：数学模型

<!-- b000103 | contents | pages [3] -->
The use of network science to analyze patterns of music inﬂuence and similarity has become increasingly

<!-- b000104 | contents | pages [3] -->
common since the early 2000s [2]. P. Cano and M. Koppenberger constructed a network of interconnected

<!-- b000105 | contents | pages [3] -->
musicians based on expert opinions and playlist co-occurrences and then performed analysis based on

<!-- b000106 | contents | pages [3] -->
metrics such as the clustering coefﬁcient [4]. N. Collins constructed a network of musical inﬂuence based

<!-- b000107 | contents | pages [3] -->
on data from allmusic.com and also performed sound content analysis using MIR tools [1]. N. Bryan and

<!-- b000108 | contents | pages [3] -->
G. Wang examined a music-sampling network and employed the important metrics of Katz centrality and

<!-- b000109 | contents | pages [3] -->
genre entropy, which we will use throughout this paper. Other researchers have proposed metrics for

<!-- b000110 | contents | pages [3] -->
musical similarity, often with the intent of improving recommendation systems. J. Serra et al. use musical

<!-- b000111 | contents | pages [3] -->
characteristics such as pitch, timbre, and loudness to analyze changes over time in Western music [15].

<!-- b000112 | contents | pages [3] -->
There is also substantial precedent for utilizing tools of machine learning to analyze genres using sound

<!-- b000113 | contents | pages [3] -->
data. For example, convolutional neural networks have been used to automatically classify songs into

<!-- b000114 | contents | pages [3] -->
genres [16].

<!-- b000115 | contents | pages [3] -->
In order to compare our model to known history, we also consider several sources from musical journalism

<!-- b000116 | contents | pages [3] -->
微信号：MATHmodels

<!-- b000117 | contents | pages [3] -->
and literature such as [12], which describe the evolution of music and major genres over time.

<!-- b000118 | contents | pages [3] -->
3

<!-- b000119 | heading | pages [3] -->
Assumptions & Rationales

<!-- b000120 | prose | pages [3] -->
In order to create a model that effectively approximates patterns in music evolution, we made the following assumptions.

<!-- b000121 | prose | pages [3] -->
• We assume that an artist’s starting decade, represented as influencer active start in the data, is the most inﬂuential point in their career. In order to identify musical revolutionaries, we must associate each artist with a decade of maximal inﬂuence. Any such choice is subjective. We believe that, in general, artists who instigated revolutions did so within the ﬁrst decade of their career.

<!-- b000122 | prose | pages [3] -->
• We assume that each sonic variable (danceability, valence, etc.) provides an equivalent measure of sonic similarity. Since weighting any one metric more than other introduces a subjective and arbitrary scale, we elected to keep them equal.

<!-- b000123 | prose | pages [3] -->
• In 5.1, we measure overall inﬂuence of artists based on multiple factors summarized by the vector in Eq. 4. In 5.5, we identify revolutionaries by specifying relevant entries of the inﬂuence vector in Eq. 4 and also incorporating our sonic distance metric. In both cases, we weight all factors equally since any other weighting would be subjective.

<!-- b000124 | prose | pages [3] -->
• We assume that indirect inﬂuence accumulates geometrically over time. As artists inﬂuence followers, those followers in turn inﬂuence more artists. We use this assumption to deﬁne a time-scaled centrality metric that forms the core of our inﬂuence model.

<!-- b000125 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000126 | furniture | pages [3] -->
关注数学模型

<!-- b000127 | furniture | pages [3] -->
2

<!-- b000128 | furniture | pages [3] -->
mcm/icm 2021

<!-- b000129 | furniture | pages [3] -->
sonic & iconic

<!-- b000130 | furniture | pages [3] -->
MATHmodels

<!-- b000131 | furniture | pages [3] -->
获取更多资讯

<!-- b000132 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000133 | furniture | pages [4] -->
team 2124668

<!-- b000134 | furniture | pages [4] -->
page 2

<!-- b000135 | prose | pages [4] -->
4

<!-- b000136 | heading | pages [4] -->
Table of Notation

<!-- b000137 | heading | pages [4] -->
Notation

<!-- b000138 | prose | pages [4] -->
Meaning Deﬁnition 5.1 微信公众号：数学模型 NTot Full Inﬂuence Network 5.1 v ∈NTot Node Representing an Artist 5.1 G Partition of Network into Established Genres 5.2 Γ Partition of Network into Sonic Genres 5.1 Ng ⊂NTot Established Genre Subnetwork for g ∈G 5.2 Nγ ⊂NTot Sonic Genre Subnetwork for γ ∈Γ Eq. 2 ˜KN,α(v) Time-scaled KC for artist Eq. 5 Musical Similarity between Points x, y ∈X µ(x, y) Eq. 4 InfVec(v) Inﬂuence Vector of an Artist v 5.4 CTot Mainstream Centroid 5.4 Genre Centroid for g ∈G ∪Γ Cg Eq. 4 InfVec(v) Augmented Inﬂuence Vector of an Artist v Eq. 3 S(v) Genre Inﬂuence Entropy of artist v Eq. 9 ARI(P, P′) Adjusted Rand Index of Partitions P and P′ 微信号：MATHmodels Eq. 11 QP Directed Modularity of Partition Map P

<!-- b000139 | caption | pages [4] -->
Table 1: Table of Notation

<!-- b000140 | prose | pages [4] -->
5

<!-- b000141 | heading | pages [4] -->
Model Development

<!-- b000142 | prose | pages [4] -->
5.1 Measuring the Inﬂuence of Artists in a Network

<!-- b000143 | prose | pages [4] -->
“I know I’m the most inﬂuential.

<!-- b000144 | prose | pages [4] -->
That TIME cover was just conﬁrmation.”

<!-- b000145 | prose | pages [4] -->
Kanye West

<!-- b000146 | prose | pages [4] -->
How does one begin to understand the way in which 5854 artists inﬂuenced each other over the span of 90 years? Our ﬁrst step is to construct an unweighted directed network based only on the influence data ﬁle. We deﬁne our network N by creating a node for each artist and assigning an edge from node i to node j if the artist i is listed as an inﬂuence of artist j.

<!-- b000147 | prose | pages [4] -->
We make some immediate observations about our network N:

<!-- b000148 | prose | pages [4] -->
• The graph is made up of one large connected component and two other small components that are exceptions, each including only two artists. This conﬁrmed our expectation that musicians are very interconnected by their inﬂuencers and followers, even across distinct genres.

<!-- b000149 | prose | pages [4] -->
• While the graph does have some cycles, including cycles of length greater than 3, it is generally acyclic. For instance, we determined only 4% of artists in the Pop/Rock genre are part of cycles. This makes sense, since musical inﬂuence generally passes from older to newer generations of artists. The cycles that do occur represent groups of contemporary artists who listed each other as inﬂuences.

<!-- b000150 | prose | pages [4] -->
• While the number of inﬂuences of each artist is relatively low, almost all artists are impacted by many indirect inﬂuences. For instance, in Figure 7, Billie Eilish only has three direct inﬂuences. One would be led to believe that only Frank Ocean, Skylar Grey, and Ke$ha determine Eilish’s musical inﬂuence, but a single additional level shows wider inﬂuences on her music.

<!-- b000151 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000152 | furniture | pages [4] -->
关注数学模型

<!-- b000153 | furniture | pages [4] -->
2

<!-- b000154 | furniture | pages [4] -->
mcm/icm 2021

<!-- b000155 | furniture | pages [4] -->
sonic & iconic

<!-- b000156 | furniture | pages [4] -->
MATHmodels

<!-- b000157 | furniture | pages [4] -->
获取更多资讯

<!-- b000158 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000159 | furniture | pages [5] -->
team 2124668

<!-- b000160 | furniture | pages [5] -->
page 3

<!-- b000161 | prose | pages [5] -->
微信公众号：数学模型 (a) 1-edge inﬂuences. (b) 2-edge inﬂuences.

<!-- b000162 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000163 | caption | pages [5] -->
Figure 1: Billie Eilish’s inﬂuences.

<!-- b000164 | prose | pages [5] -->
5.1.1 Measuring the Inﬂuence of an Individual Artist in a Network

<!-- b000165 | prose | pages [5] -->
Next, we pose the complex question: how can we measure the inﬂuence of a single artist on the musical network as a whole? In developing such a metric, considering both direct and indirect inﬂuence is critical. For instance, many artists would list Elvis Presley as a major inﬂuence and no doubt recall his hit song “Hound Dog.” However, “Hound Dog” was written by the lesser known artist Big Mama Thornton. Thus, any follower of Elvis was probably also inﬂuenced by Big Mama Thornton, even if they do not cite her as an inﬂuence. Accordingly, there are major ﬂaws with any metric based solely on out-degree, i.e. the number of other artists who list the artist in question as an inﬂuence.

<!-- b000166 | prose | pages [5] -->
In [1], N. Bryan and G. Wang discuss alternative metrics for musical networks which incorporate indirect inﬂuence. They consider the famous network metric of eigenvector centrality, a measure for the inﬂuence of a node vi which takes into account both direct and indirect inﬂuence. They point out, however, that eigenvector centrality has limited application for directed networks without many cycles. Since we have already established our directed graph has relatively few cycles, we need a better metric.

<!-- b000167 | prose | pages [5] -->
They also discuss PageRank, a modiﬁed version of eigenvector centrality, which is the primary metric used by Google Search to measure the importance of website pages. A shortcoming of PageRank in the context of musical networks, however, is that the algorithm down-weights the importance of nodes with high in-degree [1], which in this case represent artists with many inﬂuences.

<!-- b000168 | prose | pages [5] -->
Instead, they utilize another modiﬁed version of eigenvector centrality known as Katz centrality. The Katz centrality of an artist v within a network N is written as KN,α(v), where α is a parameter. This metric is deﬁned implicitly as X (1) KN,α(vi) = α Aij KN,α(vj) + 1 j∈N

<!-- b000169 | prose | pages [5] -->
where Aij is the adjacency matrix. In other words, the Katz centrality of each node i is a linear combination of the Katz centralities of all the nodes inﬂuenced by node i with coefﬁcients in terms of α. The parameter α is a decay factor which scales the importance of indirect inﬂuence. For stability, 1 α must be greater than the largest eigenvalue of A. Therefore, we deﬁne an αmax = 1/λTot where Tot is the largest eigenvalue of the entire network. We use this constant as a unit with which to scale α values. In general, a larger α value implies greater importance of indirect inﬂuence.

<!-- b000170 | prose | pages [5, 6] -->
In Eq. 1, we add the constant 1 to the linear combination in order to ensure nodes with no followers do not have a Katz centrality of 0; if this were allowed, these nodes would not count toward their inﬂuencer’s Katz centrality. We encounter one issue with this deﬁnition when we compare the Katz centrality of artists in different networks. Since α ≪1, the leaf nodes (i.e. artist with no inﬂuence) contribute most when they are close to the artist in questions. In order to compare Katz centralities between networks, we therefore must replace the 1 in Eq. 1 with a constant that depends on the network. Based on the results of our 微信公众号：数学模型 calculation we choose |N|, the order of the network to be this value.

<!-- b000171 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000172 | furniture | pages [5] -->
关注数学模型

<!-- b000173 | furniture | pages [5] -->
2

<!-- b000174 | furniture | pages [5] -->
mcm/icm 2021

<!-- b000175 | furniture | pages [5] -->
sonic & iconic

<!-- b000176 | furniture | pages [5] -->
MATHmodels

<!-- b000177 | furniture | pages [5] -->
获取更多资讯

<!-- b000178 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000179 | furniture | pages [6] -->
team 2124668

<!-- b000180 | furniture | pages [6] -->
page 4

<!-- b000182 | prose | pages [6] -->
We can see the effect of α in Fig. 2. For a higher α value, and therefore a wider scope, older artists take precedence while more recent artists appear with a narrower scope. However, this model gives undue

<!-- b000183 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000184 | caption | pages [6] -->
Figure 2: Katz centrality of top twelve artists at any one time as function of α.

<!-- b000185 | prose | pages [6] -->
credit to older artists since they have more time to accumulate inﬂuence. If we assume indirect inﬂuence to accumulate exponentially in time, we can instead compare the exponential rates of Katz centrality over time, a value we call the “time-scaled Katz centrality.” This value is explicitly deﬁned as

<!-- b000186 | prose | pages [6] -->
1 (2) ˜KN,α(v) = 2020 −decade(t) exp (−KN,α(v)),

<!-- b000187 | prose | pages [6] -->
evaluated in Fig. 3. In this graph, there exists two distinct regimes of inﬂuence, one around α1 = 0.2αmax

<!-- b000188 | caption | pages [6] -->
Figure 3: Timescaled Katz centrality of top twelve artists at any one time as function of α.

<!-- b000189 | prose | pages [6] -->
and the other around α2 = 1.0αmax. These two parameters will deﬁne “Direct” and “Indirect Inﬂuence” inﬂuence.

<!-- b000190 | prose | pages [6] -->
At this point, we incorporate genre into our measure of inﬂuence. Measures based on the entire network cannot identify artists whose inﬂuence is mostly concentrated within their genre. We believe any artist that had a transformative impact within a major genre is important–even if their work never reached artists of different musical styles.

<!-- b000191 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000192 | furniture | pages [6] -->
关注数学模型

<!-- b000193 | furniture | pages [6] -->
2

<!-- b000194 | furniture | pages [6] -->
mcm/icm 2021

<!-- b000195 | furniture | pages [6] -->
sonic & iconic

<!-- b000196 | furniture | pages [6] -->
MATHmodels

<!-- b000197 | furniture | pages [6] -->
获取更多资讯

<!-- b000198 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000199 | furniture | pages [7] -->
team 2124668

<!-- b000200 | furniture | pages [7] -->
page 5

<!-- b000201 | prose | pages [7] -->
For this reason, we denote the set of all genres as G and deﬁne genre subnetworks Ng for each genre g ∈G. We can then apply direct Katz centrality metrics to each node within its own genre’s subnetwork in order to compute values measuring the direct genre inﬂuence of an artist. We only apply direct Katz centrality in this case because genre subnetworks are too small for indirect Katz Centrality to be meaningful. 微信公众号：数学模型 Instead, computing the top artists in a genre in terms of direct and indirect Katz Centrality results in almost identical lists.

<!-- b000202 | prose | pages [7] -->
On the other hand, some artists are considered legendary due to the broad spectrum of genres they inﬂuenced. In order to measure this breadth, we adapt Bryan and Wang’s [1] deﬁnition of “genre entropy,” applying it instead to artist data. This metric uses the “probability of inﬂuence,” which we deﬁne for each inﬂuencer as the number of followers in a genre divided by the total artists in that genre. We use this to deﬁne the entropy as

<!-- b000203 | prose | pages [7] -->
X followers of artist v  followers of artist v  (3) S(v) = − log |g| |g| g∈G

<!-- b000204 | prose | pages [7] -->
where G is the genre partition map and |g| is the order of genre g. The intuition behind this deﬁnition stems from the original meaning of entropy in the context of statistical physics, where the probability is deﬁned for each of the possible conﬁgurations of a system. The entropy indicates the “spread” of the 微信号：MATHmodels probabilities, reaching a maximum when all cases are equally likely. In the context of musical genre, a high entropy indicates that an artist has a wide spread of inﬂuence.

<!-- b000205 | prose | pages [7] -->
At this point, we have four different functions on artists in our network, each of which measure a distinct form of musical inﬂuence. We thus introduce what we refer to as the inﬂuence vector of an artist v.

<!-- b000206 | prose | pages [7] -->
˜KN,α1(v)     Direct KC in entire network ˜KN,α2(v) Indirect KC in entire network (4)  =   InfVec(v) = ˜KNg,α1(v) Direct KC in artist’s genre S(v) Genre Inﬂuence Entropy

<!-- b000207 | prose | pages [7] -->
Each of the four components of this vector are scores which determine the artist’s ranking based on different types of inﬂuence. If we normalize these values to be equally weighted, we can take the Euclidean norm of this vector to determine an overall measurement of inﬂuence. We could also weight some forms of inﬂuence above others but we refrain from doing that for the sake of objectivity.

<!-- b000208 | prose | pages [7] -->
5.1.2 Constructing and Analyzing a Subnetwork

<!-- b000209 | prose | pages [7] -->
In order to apply our deﬁnition of inﬂuence vectors of artists, we now carefully choose a subnetwork to ensure accurate and interesting results. Due to the existence of fringe genres such as Children’s Music, which only has four artists in our network, several of our metrics of inﬂuence are rendered invalid on the network as a whole. An artist making Children’s Music will likely have extremely high Katz Centrality within their genre, skewing these metrics in their favor. Likewise, Genre Inﬂuence Entropy measures the breadth of inﬂuence across many genres and would thus also be skewed by the existence of fringe genres.

<!-- b000210 | prose | pages [7] -->
To account for these issues, we consider a subnetwork ˜N, which only includes the top ﬁve genres in terms of number of artists. Moreover, since we were still left with a large network, we restrict further by specifying to artists that became active in the 21st century. By limiting our network to a shorter time span, we optimize computation and generated more precise and interesting results concerning the most inﬂuential artists of the last two decades. We call this new network ˜N⩾2000. Thus, we determine the major inﬂuencers included in ˜N⩾2000 according to each individual metric and the Euclidean norm of the inﬂuence vectors, shown in Tab. 2.

<!-- b000211 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000212 | furniture | pages [7] -->
关注数学模型

<!-- b000213 | furniture | pages [7] -->
2

<!-- b000214 | furniture | pages [7] -->
mcm/icm 2021

<!-- b000215 | furniture | pages [7] -->
sonic & iconic

<!-- b000216 | furniture | pages [7] -->
MATHmodels

<!-- b000217 | furniture | pages [7] -->
获取更多资讯

<!-- b000218 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000219 | furniture | pages [8] -->
team 2124668

<!-- b000220 | furniture | pages [8] -->
page 6

<!-- b000221 | prose | pages [8] -->
Total Direct Network Indirect Network Direct Genre Genre Entropy (||InfVec(v)||) 1. Frank Ocean Avril Lavigne CNCO Flying Lotus Frank Ocean 2. Flume All-American Rejects Zedd Bon Iver CNCO 微信公众号：数学模型 3. Alt-J Frank Ocean J Balvin India.Aire Flume 4. The Weeknd The Killers San Bandera Amy Winehouse Avril Lavigne 5. One Direction Rihanna EDEN Justice The Weekend

<!-- b000222 | caption | pages [8] -->
Table 2: Most inﬂuential artists from 2000-2020 as determined by the InfVec(v) vector.

<!-- b000223 | prose | pages [8] -->
5.2 Musical Similarity Metric and Sonic Genres

<!-- b000224 | prose | pages [8] -->
5.2.1 Selecting Sonic Variables

<!-- b000225 | prose | pages [8] -->
The ﬁrst step to determine sonic similarity as a metric would be to select a data set. Since our data about musical inﬂuence exists at the artist level, we start our sonic similarity exploration with the data by artist data set. Merging the follower main genre from the influence data into the data by artist data set assigns every artist an Established Genre. Later we will consider another grouping of artists that we 微信号：MATHmodels will refer to as Sonic Genres, so to eliminate confusion we will refer to genre in the traditional sense as Established Genre. In our data set, we choose to not include follower artists that have no primary Established Genre. This reduces the number of artists we consider by 809 to 5045.

<!-- b000226 | prose | pages [8] -->
We are given thirteen sonic variables for each artist: danceability, energy, valence, tempo, loudness, mode, key, acousticness, instrumentalness, liveness, speechiness, explicit, and duration. We ﬁrst remove the explicit category since it makes a content judgement. Additionally, we determine that musical key has little to no bearing on the listening experience of a track. Additionally, the key does not linearly relate to the sound of a song. For example a song in the key of C is no more related to a song in the key of C# than a song in the key of F. We therefore ignore key for the entirety of this study. On the contrary, the mode of a piece of music, being major or minor, has a very strong impact on the listening experience of a song. Therefore, we include this music theory attribute.

<!-- b000227 | prose | pages [8] -->
Before we begin considering music similarity, we normalize our sonic variable data using a MinMaxScaler that scales all features to a range of 0 to 1 [10]. Now we can consider different metrics of sonic similarity.

<!-- b000228 | prose | pages [8] -->
5.2.2 Reducing Music Similarity to Metric

<!-- b000229 | prose | pages [8] -->
The sonic variables that we choose to consider for a 11-dimensional vector space with artists and songs represented as points. By calculating the distance between these points, we can quantify their sonic similarity. A smaller distance means that two points are closer and therefore similar in sound. Below we deﬁne three different distance metrics.

<!-- b000230 | heading | pages [8] -->
1. Euclidean Distance: We consider the standard Euclidean Distance between two sonic points x =

<!-- b000231 | prose | pages [8] -->
(x1, . . . , xn) and (y1, . . . , yn) in our n-dimensional space X. In tandem, we deﬁne a Euclidean “musical similarity,” µ(x, y) = (1 + d(x, y))−1, (5)

<!-- b000232 | prose | pages [8] -->
where 1 is most similar. To improve our result, we could weight some sonic variables more heavily, however any such weighting would be arbitrary and subjective.

<!-- b000233 | heading | pages [8] -->
2. Manhattan Distance: We also consider the Manhattan Distance between two sonic points x =

<!-- b000234 | prose | pages [8] -->
(x1, . . . , xn) and (y1, . . . , yn) in our n-dimensional space X:

<!-- b000235 | prose | pages [8, 9] -->
n X (6) |xi −yi| dM(x, y) = i=1 3. Cosine Similarity : We consider the Cosine Similarity derived by constructing two vectors from the origin to each sonic point and taking the cosine of the angle between them.

<!-- b000236 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000237 | furniture | pages [8] -->
关注数学模型

<!-- b000238 | furniture | pages [8] -->
2

<!-- b000239 | furniture | pages [8] -->
mcm/icm 2021

<!-- b000240 | furniture | pages [8] -->
sonic & iconic

<!-- b000241 | furniture | pages [8] -->
MATHmodels

<!-- b000242 | furniture | pages [8] -->
获取更多资讯

<!-- b000243 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000244 | furniture | pages [9] -->
team 2124668

<!-- b000245 | furniture | pages [9] -->
page 7

<!-- b000247 | prose | pages [9] -->
These sonic similarity metrics can be applied to any two individual artists to quantify their sound similarity. However, applying these metrics to the full metric in a fashion that allows us to draw conclusions 微信公众号：数学模型 about the sound of artists with and between genres will require a more nuanced approach.

<!-- b000248 | prose | pages [9] -->
5.2.3 Predicting Established Genre from Sonic Variables

<!-- b000249 | prose | pages [9] -->
We deﬁne the similarity of two artists in terms of sonic similarity metrics, like Euclidean distance. If artists within a genre are more similar by the previous deﬁnition, then sonic variables should be able to predict genres. Vishnupriya and Meenakshi explain that most programmatic Established Genre classiﬁcations are performed via machine learning. In their research, they use a convolutional neural network to classify song clips into Established Genres [16].

<!-- b000250 | prose | pages [9] -->
We train the Sequential-modeled neural network in Fig. 4 to predict genre from sonic variables. Successful predictions imply a high correlation between sonic variable inputs and Established Genre outputs across the entire data set of artists. We use a categorical cross-entropy loss function, Adam optimizer, and choose to deﬁne model goodness as accuracy [3].

<!-- b000251 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000252 | caption | pages [9] -->
Figure 4: Neural network model structure.

<!-- b000253 | prose | pages [9] -->
We ﬁrst split our 5045 data set of artists into 70% training data and 30% test data. Since there is a disparity between the number of artists in each Established Genre represented in our data we choose to apply class weights to prevent our model from predicting that every artist ﬁts in the largest Established Genre “Pop/Rock.” Our data was previously normalized, and we train our neural network on the training sonic variables. We train for 150 epochs with a batch size of 5 and achieve an accuracy of 0.0% when we choose our best-performing model from 10 trials.

<!-- b000254 | prose | pages [9] -->
Looking closer at the data, we realize that some of the Established Genres have less than ten artists represented and that 4010 of the artists, approximately 80%, represent four genres: Pop/Rock, RB, Country, and Jazz. We remove all artists but those that belong to these 4 genres and achieve an accuracy on our test data set of 63.3% when we choose our best-performing model from 10 trials. This is better and suggests that sonic features somewhat correlate to genres, but this accuracy was only achieved when we limited to four genres. Perhaps there is a better way to group artists to capture the sonic style of artists outside the main four genres.

<!-- b000255 | prose | pages [9] -->
We can create new Sonic Genres that group artists based on sound alone. The history of Established Genres is undeniably relevant, but constructing Sonic Genres would allow us to analyze musical evolution and inﬂuence from a distinct perspective based solely on the categorization of the provided artist’s sound data. In particular, we could improve our inﬂuence vectors of artists to include their impact on the Sonic Genres we determine using Katz Centrality.

<!-- b000256 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000257 | furniture | pages [9] -->
关注数学模型

<!-- b000258 | furniture | pages [9] -->
2

<!-- b000259 | furniture | pages [9] -->
mcm/icm 2021

<!-- b000260 | furniture | pages [9] -->
sonic & iconic

<!-- b000261 | furniture | pages [9] -->
MATHmodels

<!-- b000262 | furniture | pages [9] -->
获取更多资讯

<!-- b000263 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000264 | furniture | pages [10] -->
team 2124668

<!-- b000265 | furniture | pages [10] -->
page 8

<!-- b000266 | prose | pages [10] -->
5.2.4 Using K-Means Clustering to Deﬁne Sonic Genres

<!-- b000267 | prose | pages [10] -->
K-Means is a clustering algorithm used to group data based on similarities. First, a set number of cluster centroids are instantiated in n-dimensional space, where n corresponds to the number of input variables, in 微信公众号：数学模型 this case the eleven sonic variables. The number of clusters that we instantiate is a hyperparameter that can be tuned. Next, all points are assigned to one of these centroids to form clusters. A point is assigned to its closest centroid according to Euclidean distance. The cluster centroids of these new clusters is determined and the process repeats.

<!-- b000268 | prose | pages [10] -->
The goal of this algorithm in the case of our inﬂuence network is to minimize the average sum-of-squared- errors until it converges for two groups of cluster centroids, which is deﬁned by:

<!-- b000269 | prose | pages [10] -->
|NTot| X 1 d(si, R(si))2 (7) E = |NTot| i=1

<!-- b000270 | prose | pages [10] -->
where si is the Sonic Point associated with the artist vi ∈NTot and R(si) is cluster center closest to si [14]. Thus, we seek to minimize the average Euclidean distance of each sonic point to the nearest sonic center.

<!-- b000271 | prose | pages [10] -->
Using scikit-learn, we apply the K-Means clustering algorithm to the entire data set of artists. Hin- neburg, Aggarwal, and Keim suggest that the best approach for calculating closeness between the cluster 微信号：MATHmodels centroids and all other points is Euclidean Distance, so we choose to use that sonic similarity metric here [14]. However, we must be wary of the “Curse of Dimensionality,” the issue that when applying certain metrics statistical metrics, the error of the metric increases as the number of dimensions increases. Is eleven dimensions too many and constitutes an issue with using Euclidean Distance? Other research into image classiﬁcation problems in data science sometimes uses K-Means clustering. For example, Ranjan et al. reduce the number of input dimensions, or Principle Components, to 50 and then apply K-Means clustering [11]. 50 is still more than our 11 dimensions. Furthermore, Hinneburg et al. analytically prove that Euclidean Distance and Manhattan Distance 6 are appropriate indicators of similarity in higher dimensions [7].

<!-- b000272 | prose | pages [10] -->
Sonic Genre Name Notable Artists “Here Comes the Sun” Genre The Beatles, Hank Williams, Bob Dylan “Thunderstruck” Genre AC/DC, Jimi Hendrix, David Bowie “I Will Survive” Genre Destiny’s Child, Sting, Sia “Swan Lake” Genre Chet Baker, Dave Brubeck, Howard Shore

<!-- b000273 | caption | pages [10] -->
Table 3: Sonic Genres

<!-- b000274 | prose | pages [10] -->
The resulting sonic clusters we deﬁne as our four Sonic Genres in Table 3. In choosing names, we selected well-known songs from each Sonic Genre that roughly corresponded to the sonic variables we observed. The centroids of each Sonic Genre cluster are provided in Table 4. Interesting highs of each sonic variable for each Sonic Genre are highlighted green and lows are highlighted red to draw attention to salient characteristics of each new genre. After clustering, all artists have been assigned a Sonic Genre. Artists in the same Sonic Genre have a similar sound.

<!-- b000275 | prose | pages [10, 11] -->
But how can we validate that these sonic genres mean anything? Are they actually representative of sonic feature clusters? We can validate our clusters by training our previous neural network architecture to predict Sonic Genres from the artists’s sonic variables. For our four Sonic Genres, if our neural network can only achieve 25% accuracy predicting Sonic Genres from sonic variable inputs, then our Sonic Genres could represent an arbitrary partition of artists’ sonic variables. Once again, we split the data by artist into a training and test set. However, now we are not only including artists from the top four genres, but rather all 5045 artists with an Established Genre label. Training our model 10 times and choosing the best accuracy determined from our test set representing 30% of the data we get 52.0%. This is over twice the accuracy we would get if the Sonic Genres were guessed randomly from the sonic variable inputs. This shows that our Sonic Genres are a meritorious grouping of artists based on sonic features, i.e. artists that sound the same “Here Comes the Sun” “Thunderstruck” “I Will Survive” “Swan Lake” 0.524 0.531 0.56 0.399 Danceability 0.422 0.725 0.626 0.31 Energy 0.536 0.57 0.544 0.313 Valence 0.483 0.534 0.51 0.462 Tempo 微信公众号：数学模型 0.682 0.778 0.749 0.566 Loudness 1.0 1.0 0.0 0.861 Mode 0.605 0.134 0.254 0.694 Acousticness 0.056 0.096 0.141 0.73 Instrumental 0.193 0.197 0.187 0.149 Liveness 0.049 0.048 0.059 0.029 Speechiness

<!-- b000276 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000277 | furniture | pages [10] -->
关注数学模型

<!-- b000278 | furniture | pages [10] -->
2

<!-- b000279 | furniture | pages [10] -->
mcm/icm 2021

<!-- b000280 | furniture | pages [10] -->
sonic & iconic

<!-- b000281 | furniture | pages [10] -->
MATHmodels

<!-- b000282 | furniture | pages [10] -->
获取更多资讯

<!-- b000283 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000284 | furniture | pages [11] -->
team 2124668

<!-- b000285 | furniture | pages [11] -->
page 9

<!-- b000287 | caption | pages [11] -->
Table 4: Sonic Genre centroid data. Lowest values for each category are shaded in red while highest values are shaded

<!-- b000288 | prose | pages [11] -->
in green.

<!-- b000289 | prose | pages [11] -->
are grouped into the same Sonic Genres. Sonic Genres allow us to compare music similarity across the entire network. We can now assess whether artists within a genre sound more similar than artists between 微信号：MATHmodels genres by comparing the Sonic Genre clusters to the Established Genre clusters.

<!-- b000290 | prose | pages [11] -->
5.2.5 Comparing Sonic Genres to Established and Sonic Genres to Inﬂuences

<!-- b000291 | prose | pages [11] -->
We analyze the relationship between sonic characteristics and Established Genres by directly comparing the network partition of Established Genres to the network partition of our Sonic Genres. In order to capture this, we use the Adjusted Rand Index (ARI), common measure of similarity between two partitions which was introduced in [8].

<!-- b000292 | prose | pages [11] -->
We deﬁne the Rand Index (RI) of a pair of partitions P = {X1, . . . , Xl} and P′ = {Y1, . . . , Ym} of a network of n artists as [10] :

<!-- b000293 | prose | pages [11] -->
RI(P, P′) = A + B (8)  n  2 Then, the RI metric may then be adjusted for chance to obtain:

<!-- b000294 | prose | pages [11] -->
RI −Expected RI ARI(P, P′) = (9) max(RI) −Expected RI

<!-- b000295 | prose | pages [11] -->
Values closer to 0 imply less similarity between a pair of partitions and 1 indicates perfect alignment between a pair of partitions. We compute that the ARI(G, Γ), the Adjusted Rand Index, of Established Genres versus Sonic Genres is 0.161. Since Sonic Genres are based on sonic similarity, one can conclude that artists between genres are sometimes more sonically similar than artists within genres.

<!-- b000296 | prose | pages [11] -->
But what if we just chose a number of clusters to minimize the Adjusted Rand Index? Since the number of clusters is a hyperparameter that we can tune, we can compare the Adjusted Rand Index between various numbers of Sonic Genre clusters.

<!-- b000297 | caption | pages [11] -->
Fig. 5 shows that clustering sonic variables to generate four Sonic Genres produces the highest Adjusted

<!-- b000298 | prose | pages [11] -->
Rand Index. Thus, choosing 4 clusters is the best we can do to generate clusters based on sonic features that correlate to the Established Genres.

<!-- b000299 | prose | pages [11] -->
5.2.6 Improving Inﬂuence Vectors with Sonic Genres

<!-- b000300 | prose | pages [11, 12] -->
Now that we have determined Sonic Genres, we have four new meaningful subnetworks on which we can apply our direct Katz Centrality metric. As with the Established Genres, we omit indirect Katz centrality 微信公众号：数学模型 微信号：MATHmodels

<!-- b000301 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000302 | furniture | pages [11] -->
关注数学模型

<!-- b000303 | furniture | pages [11] -->
2

<!-- b000304 | furniture | pages [11] -->
mcm/icm 2021

<!-- b000305 | furniture | pages [11] -->
sonic & iconic

<!-- b000306 | furniture | pages [11] -->
MATHmodels

<!-- b000307 | furniture | pages [11] -->
获取更多资讯

<!-- b000308 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000309 | furniture | pages [12] -->
team 2124668

<!-- b000310 | furniture | pages [12] -->
page 10

<!-- b000312 | caption | pages [12] -->
Figure 5: Adjusted Rand Index computed between various numbers of sonic clusters and Established Genres.

<!-- b000313 | prose | pages [12] -->
since we are dealing with smaller networks. In this way, we can augment our deﬁnition for inﬂuence vectors of an artist v in an Established Genre g ∈G and a Sonic Genre γ ∈Γ:

<!-- b000314 | prose | pages [12] -->
˜KN,α1(v)     Direct KC in entire network ˜KN,α2(v) Indirect KC in entire network     ˜KNg,α1(v) (10) InfVec(v) = = Direct KC in Established Genre ˜KNγ,α1(v) Direct KC in Sonic Genre S(v) Genre Inﬂuence Entropy

<!-- b000315 | prose | pages [12] -->
This new vector is a more sophisticated measurement in that it incorporates sound data to consider the inﬂuence an artist may have had on their own Sonic Genre. In section 5.5, we will use the metrics in each InfVec(v) vector to identify some artists as musical revolutionaries of different types.

<!-- b000316 | prose | pages [12] -->
5.3 Analyzing Established Genres

<!-- b000317 | prose | pages [12] -->
5.3.1 Distinguishing a Genre

<!-- b000318 | prose | pages [12] -->
Any self-respecting music lover has a lot to say about Established Genres like Jazz, Country, and R&B but what actually deﬁnes these musical categories? In 5.2, we partitioned our artist sound data into four distinct Sonic Genres. Using a neural network, we validated these Sonic Genre groupings and compared them to Established Genre groupings using an Adjusted Rand Index and found low similarity, suggesting sound is not the best predictor of Established Genres.

<!-- b000319 | prose | pages [12] -->
5.3.2 Modularity

<!-- b000320 | prose | pages [12] -->
We measure the accuracy of a particular partition map on the inﬂuence network using the “modularity,” deﬁned for direct maps as:

<!-- b000321 | prose | pages [12] -->
" # X X Av,v′ −kout kin QP = 1 v v′ (11) m m v,v′∈p p∈P

<!-- b000322 | prose | pages [12] -->
where: Av,v′ is the adjacency matrix, kout is the out-degree of artist v, kin v′ is the in-degree of artist v′, P is v the partition map, and m is the number of edges in the graph [9].

<!-- b000323 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000324 | furniture | pages [12] -->
关注数学模型

<!-- b000325 | furniture | pages [12] -->
2

<!-- b000326 | furniture | pages [12] -->
mcm/icm 2021

<!-- b000327 | furniture | pages [12] -->
sonic & iconic

<!-- b000328 | furniture | pages [12] -->
MATHmodels

<!-- b000329 | furniture | pages [12] -->
获取更多资讯

<!-- b000330 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000331 | furniture | pages [13] -->
team 2124668

<!-- b000332 | furniture | pages [13] -->
page 11

<!-- b000333 | prose | pages [13] -->
We use this metric to analyze the Established Genre partition map G, yielding QG = 0.38. Since the range of this value is 0 to 1, this value demonstrates signiﬁcant clustering with respect to inﬂuence. We conclude inﬂuence and genre correspond signiﬁcantly.

<!-- b000334 | prose | pages [13] -->
微信公众号：数学模型 5.3.3 Established Genres over Time

<!-- b000335 | prose | pages [13] -->
Initially, we plotted individual sonic variables as functions of time for different genres. We quickly realized these plots, while suggestive of the dynamic nature of genres, are not very meaningful on their own. Therefore, we sought ways to analyze the evolution of genres that include many different sonic variables.

<!-- b000336 | prose | pages [13] -->
One method is to measure the sonic similarity between each genre and the mainstream. As genres change over time, we can use musical similarity deﬁned in Eq. 5, to measure the inﬂuence of sound of certain genres on the mainstream. To analyze this data, we deﬁne the centroid CN of any network by taking an average of all associated songs weighted by popularity. We may then calculate the similarity between the mainstream and each of the top 10 established genres using centroids. To smooth the graph and remove discontinuities, we calculate this value for each grouping of ﬁve neighboring years. These values are plotted in Fig. 6. This graph illustrates genre trends, such as the rise in popularity of folk music in the 1960s and 1970s. We explore the changes in this graph as part of Sec. 5.5.

<!-- b000337 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000338 | caption | pages [13] -->
Figure 6: Similarity between mainstream centroid and genre centroid over time.

<!-- b000339 | prose | pages [13] -->
5.3.4 Interconnections between Established Genres

<!-- b000340 | prose | pages [13] -->
Other sources such as [1] generate directed networks of genre nodes with weighted edges to directly display interconnections between Established Genres. To avoid redundancy, we refrained from taking this approach.

<!-- b000341 | prose | pages [13] -->
To measure the interconnections between genres, we can use the entropy from Sec. 5.1. In order to measure the entropy of genres, as opposed to artists, we average the entropy of all artists in each genre. The values and rankings for the highest and lowest three genres are shown in Table 5.

<!-- b000342 | prose | pages [13] -->
5.4 Inﬂuence vs. Sonic Similarity

<!-- b000343 | prose | pages [13, 14] -->
To determine whether inﬂuencers affect followers, we use our sonic similarity metrics embodied in Sonic Genres to see how similar these groupings are to the inﬂuencer network. We can use the modularity metric S(v) Genre 1. 0.22 Avant-Garde 2. 0.17 Classical 3. 0.14 Folk 微信公众号：数学模型 ... ... ...

<!-- b000344 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000345 | furniture | pages [13] -->
关注数学模型

<!-- b000346 | furniture | pages [13] -->
2

<!-- b000347 | furniture | pages [13] -->
mcm/icm 2021

<!-- b000348 | furniture | pages [13] -->
sonic & iconic

<!-- b000349 | furniture | pages [13] -->
MATHmodels

<!-- b000350 | furniture | pages [13] -->
获取更多资讯

<!-- b000351 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000352 | furniture | pages [14] -->
team 2124668

<!-- b000353 | furniture | pages [14] -->
page 12

<!-- b000355 | prose | pages [14] -->
17. 0.05 Latin 18. 0.05 Electronic 19. 0.03 Pop/Rock

<!-- b000356 | caption | pages [14] -->
Table 5: Most and least entropic genres based on average artist entropy S(v).

<!-- b000357 | prose | pages [14] -->
Sonic Variable Contagiousness 9.076 Danceability 6.688 Energy 6.326 Valence 12.431 Tempo 12.150 Loudness 5.312 微信号：MATHmodels Mode 2.684 Key 5.308 Acousticness 7.782 Instrumentalness 11.459 Liveness 33.430 Speechiness 23.985 Duration

<!-- b000358 | caption | pages [14] -->
Table 6: Sonic variable contagiousness across the entire Inﬂuence Network N. Higher values shaded in green.

<!-- b000359 | prose | pages [14] -->
from Sec. 5.3.2 to analyze the partition map Γ corresponding to the four sonic genres deﬁned in Sec. 5.2. This yields a modularity of QΓ = 0.17. We can better compare this value to the established genres by only taking the top four established genres, yielding QG′ = 0.31. These values indicate that the sonic genres are not as clustered as the established genres but signiﬁcantly more clustered than a random partition map. We can trace this to cultural elements of established genres that are ignored in the sonic genre calculation. Since genre is subjective and based on more than just sound (as we showed in previous sections), we do not expect Sonic Genres to tell the full story, rather provide an interesting new tool to examine music history and inﬂuences.

<!-- b000360 | prose | pages [14] -->
Thus, artists do not inﬂuence the sound of other artists taking all sonic variables into account, but we can examine which sonic variables are more contagious relative to others, i.e. more likely to be the same between an inﬂuencer and a follower.

<!-- b000361 | prose | pages [14] -->
5.4.1 Sonic Variable Contagiousness

<!-- b000362 | prose | pages [14] -->
Again, we consider our 11 sonic variables and aim to determine if certain sonic variables are more contagious than others. We can quantify this metric by looking at how similar sonic variables are between inﬂuencers and followers across the entire network. Summing the absolute value of the difference between each sonic variable for the follower and the inﬂuencer, dividing by the number of edges, and taking the inverse:

<!-- b000363 | prose | pages [14] -->
number of edges (12) P |xinfluencer −xfollower| Sonic contagiousness =

<!-- b000364 | prose | pages [14] -->
yields the contagiousness of sonic variables shown in Table 6. Thus, some sonic variables like speechiness, duration, tempo, and loudness are more contagiousness than others.

<!-- b000365 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000366 | furniture | pages [14] -->
关注数学模型

<!-- b000367 | furniture | pages [14] -->
2

<!-- b000368 | furniture | pages [14] -->
mcm/icm 2021

<!-- b000369 | furniture | pages [14] -->
sonic & iconic

<!-- b000370 | furniture | pages [14] -->
MATHmodels

<!-- b000371 | furniture | pages [14] -->
获取更多资讯

<!-- b000372 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000373 | furniture | pages [15] -->
team 2124668

<!-- b000374 | furniture | pages [15] -->
page 13

<!-- b000375 | prose | pages [15] -->
5.5 Musical Evolution in Terms of Revolutions and Revolutionaries

<!-- b000376 | prose | pages [15] -->
5.5.1 Classifying Musical Revolutions

<!-- b000377 | prose | pages [15] -->
微信公众号：数学模型 “You say you want a revolution...”

<!-- b000378 | prose | pages [15] -->
The Beatles

<!-- b000379 | prose | pages [15] -->
The notions of a “musical revolution” and a “musical revolutionary” are both extremely elusive. Depend- ing on perspective, one could arrive at very different conclusions. For example, the top Google result for the search “musical revolution” is an article about Sesame Street (not to disparage Big Bird, of course) [13].

<!-- b000380 | prose | pages [15] -->
With tools to analyze musical inﬂuence and sonic similarity across the entire network and subnetworks, we classify musical revolutions. Although we believe there are many types of musical revolutions, we focus on two classes which we consider to be the most important. This decision is based both on our knowledge of musical history and the sudden changes which were most visible in our model. We must decide on a standard length of time in which a musical revolution might occur. Examining our data carefully, the 10-year periods are the best way to identify substantial and rapid musical shifts. Also, music history is often discussed in terms of decades. The two classes are as follows:

<!-- b000381 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000382 | prose | pages [15] -->
• Revolutions of an Inﬂuence Network N: These revolutions are moments in history in which the sonic characteristics of a network went through sudden shifts. In 5.3, we deﬁne network centroids CN, where N ∈{NTot, Ng, Nγ}. We consider change in a network’s sonic properties by measuring the Euclidean distance between the network’s centroid before and after a ten year period. This revolution metric encompasses three distinct types of revolution depending on which network we apply it to:

<!-- b000383 | prose | pages [15] -->
– Revolutions of the Mainstream: dramatic changes in the overall sound of music. For instance, Fig. 7a depicts the change in the centroid position of the mainstream versus time.

<!-- b000384 | prose | pages [15] -->
Using a threshold of 3.0, we identify the most signiﬁcant peak of change as a Revolution of the Mainstream in the 1930s. Fig. 7a also reveals signiﬁcant change in mainstream music in the 1960s, the 1970s, and the 1990s.

<!-- b000385 | prose | pages [15] -->
– Revolutions of Established Genres: dramatic changes in the sound of an Established Genre.

<!-- b000386 | prose | pages [15] -->
For instance, Fig. 7b depicts the change in the centroid positions of Cγ vs. time. Fig. 7b will be further discussed in 5.6.

<!-- b000387 | prose | pages [15] -->
– Revolutions of Sonic Genres: dramatic changes in the sound of a Sonic Genre. For instance, Fig. 7c depicts the change in the centroid positions of Cγ vs. time.

<!-- b000388 | prose | pages [15] -->
Using a threshold of 4.0, we identify the most signiﬁcant peak of change as a Revolution of the “I Will Survive” Genre in the 1960s. Fig. 7c also reveals signiﬁcant changes in the “I Will Survive” Genre in the 1990s and in the “Swan Lake” Genre in the 2010s.

<!-- b000389 | prose | pages [15] -->
• Revolutions of Mainstreaming Genre: These revolutions represent decades in which the similarity between an Established Genre and the mainstream suddenly increased. Such changes may reﬂect mainstream music shifting toward a speciﬁc genre or a genre suddenly exerting greater inﬂuence on all other genres. Unlike Revolutions of an Inﬂuence Network, these revolutions can only be detected on the overall network.

<!-- b000390 | prose | pages [15] -->
In Sec. 5.3, we consider Established Genre Centroids representing the average sonic characteristics of each genre over time. For any given year, we may compute the distance between some Genre Centroid and the Mainstream Centroid. We identify this type of revolution by considering the greatest changes in distance between an Established Genre and the mainstream over the course of a decade depicted in

<!-- b000391 | caption | pages [15] -->
Fig. 8. Using a threshold of 0.2, we identiﬁed that the most signiﬁcant Revolutions of Mainstreaming

<!-- b000392 | prose | pages [15] -->
Genre are:

<!-- b000393 | prose | pages [15, 16] -->
– A Revolution of Mainstreaming Jazz in the 1950s – A Revolution of Mainstreaming Pop/Rock in the 1960s 微信公众号：数学模型 (a) Mainstream (b) R&B

<!-- b000394 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000395 | furniture | pages [15] -->
关注数学模型

<!-- b000396 | furniture | pages [15] -->
2

<!-- b000397 | furniture | pages [15] -->
mcm/icm 2021

<!-- b000398 | furniture | pages [15] -->
sonic & iconic

<!-- b000399 | furniture | pages [15] -->
MATHmodels

<!-- b000400 | furniture | pages [15] -->
获取更多资讯

<!-- b000401 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000402 | furniture | pages [16] -->
team 2124668

<!-- b000403 | furniture | pages [16] -->
page 14

<!-- b000405 | prose | pages [16] -->
微信号：MATHmodels (c) Sonic Genres

<!-- b000406 | caption | pages [16] -->
Figure 7: Change in Position of Centroid vs. Time for various networks. Peaks indicate sonic revolutions.

<!-- b000407 | prose | pages [16] -->
– A Revolution of Mainstreaming Electronic in the 2000s

<!-- b000408 | prose | pages [16] -->
5.5.2 Classifying Musical Revolutionaries

<!-- b000409 | prose | pages [16] -->
Now that we have speciﬁc instances of four different types of musical revolution, how do we determine the revolutionary artists who were the primary instigators of these dramatic shifts? We believe each type of revolution requires its own criteria as outlined below. For all types of revolution, artists are only eligible as potential revolutionaries if their ﬁrst active decade overlaps with the decade of the revolution. We do not consider Indirect Katz Centrality as a factor for any revolutionary since that metric does not make since in such a short time period.

<!-- b000410 | prose | pages [16] -->
• Revolutionaries of an Inﬂuence Network N: Among eligible artists, we consider the following criteria for some artist v.

<!-- b000411 | prose | pages [16] -->
– The direct Katz Centrality ˜KN,α1(v) of v in the network N. In order to inﬂuence the overall sonic nature of a network N, an artist must have a high degree of direct inﬂuence.

<!-- b000412 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000413 | furniture | pages [16] -->
关注数学模型

<!-- b000414 | furniture | pages [16] -->
2

<!-- b000415 | furniture | pages [16] -->
mcm/icm 2021

<!-- b000416 | furniture | pages [16] -->
sonic & iconic

<!-- b000417 | furniture | pages [16] -->
MATHmodels

<!-- b000418 | furniture | pages [16] -->
获取更多资讯

<!-- b000419 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000420 | furniture | pages [17] -->
team 2124668

<!-- b000421 | furniture | pages [17] -->
page 15

<!-- b000422 | prose | pages [17] -->
微信公众号：数学模型 微信号：MATHmodels

<!-- b000423 | caption | pages [17] -->
Figure 8: Change in musical similarity of Genre Centroid to Mainstream Centroid versus time with ∂µ(Cg, CTot)/∂t =

<!-- b000424 | prose | pages [17] -->
0.2 revolution threshold.

<!-- b000425 | prose | pages [17] -->
– The distance d(s, CN,end) between the Sonic Point of an artist and the endpoint of the centroid CN after the revolution. For an artist to be credited for a Revolution of a Network, the entire network must have shifted to become more similar to the artist’s sound.

<!-- b000426 | prose | pages [17] -->
Applying these criteria to networks NTot, Ng, and Nγ, we can respectively identify Revolutionaries of the Mainstream, Revolutionaries of Established Genres, and Revolutionaries of Sonic Genres.

<!-- b000427 | prose | pages [17] -->
• Revolutionaries of Mainstreaming Genre: Artists from the appropriate time are eligible as potential revolutionaries of a given Revolution of Mainstreaming Genre if they are part of the Established Genre in question. Among eligible artists, we consider the following criteria for some artist vi in an Established Genre g:

<!-- b000428 | prose | pages [17] -->
– The direct Katz Centrality KN,α1(v) of v in the entire network. In order to signiﬁcantly inﬂuence mainstream music, an artist must have a high degree of direct inﬂuence on the network as a whole.

<!-- b000429 | prose | pages [17] -->
– Genre Entropy of an Artist S(v). In order to contribute to mainstream music becoming more similar to a speciﬁc genre, an artist must have inﬂuenced many genres.

<!-- b000430 | prose | pages [17] -->
Thus, we have metrics for each type of revolution which act as criteria for revolutionaries. We could certainly weight some metrics more heavily. However, there is no quantitative way to test our results given the data we have; accordingly any such weighting would be subjective. Instead, we weight each metric equally for all revolution types.

<!-- b000431 | prose | pages [17] -->
We then assign each eligible artist a vector measuring their potential to have instigated a given musical revolution. By multiplying the normalized Katz centrality ˜KN,α(v) (such that the most central artist is 1.0) with the similarity of artist and Endpoint Centroids, we rank potential revolutionaries and determine top candidates for each revolution. In the interest of time, we do not apply our revolutionary criteria to ﬁnd revolutionaries for any of the three Revolutions of Mainstreaming Genre.

<!-- b000432 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000433 | furniture | pages [17] -->
关注数学模型

<!-- b000434 | furniture | pages [17] -->
2

<!-- b000435 | furniture | pages [17] -->
mcm/icm 2021

<!-- b000436 | furniture | pages [17] -->
sonic & iconic

<!-- b000437 | furniture | pages [17] -->
MATHmodels

<!-- b000438 | furniture | pages [17] -->
获取更多资讯

<!-- b000439 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000440 | furniture | pages [18] -->
team 2124668

<!-- b000441 | furniture | pages [18] -->
page 16

<!-- b000442 | prose | pages [18] -->
1930s 1990s 1970s Mainstream Revolution R&B Revolution “I Will Survive” Genre Revolution 1. Howlin’ Wolf (0.55) Mary J. Blige (0.75) Barry White (0.71) 2. Hank Williams (0.47) R. Kelly (0.62) Parliament (0.59) 微信公众号：数学模型 3. Nat King Cole (0.48) D’Angelo (0.60) The Outsiders (0.54)

<!-- b000443 | caption | pages [18] -->
Table 7: Revolutionaries and with ranking metric for each of the three revolutions.

<!-- b000444 | prose | pages [18] -->
5.6 Musical Evolution of R&B

<!-- b000445 | prose | pages [18] -->
Our model can be applied to any Established Genre to identify key revolutions and revolutionaries. Looking at graphs of change in Sonic Centroid position vs. time for each genre, R&B has the clearest revolution of sound and overall musical evolution (depicted in Fig. 7b).

<!-- b000446 | prose | pages [18] -->
Fig. 7b begins in the 1970s when R&B becomes a major genre. In the early 1980s, R&B became the most static. Then, in the 1990s, we observe a Revolution of R&B, in which the degree of change peaked around 1997. We can then use our metrics from 5.5.2 to determine the revolutionaries responsible for this great leap in the genre. In Table 7, we identiﬁed the following top R&B Revolutionaries of the 1990s in order:

<!-- b000447 | prose | pages [18] -->
微信号：MATHmodels Mary J. Blige, R. Kelly, and D’Angelo.

<!-- b000448 | prose | pages [18] -->
Another perspective on the evolution of the genre of R&B comes from 8. While the 1990s may have been greatest moment of sonic change for the genre, there have three distinct peaks of R&B being close to the mainstream in the 1960s, the 1990s, and the 2010s. It is interesting to note that even though R&B has been very close to the mainstream in the last decade, the degree of change within the genre has been much lower recently than in the 1990s.

<!-- b000449 | prose | pages [18] -->
In Table 8, we also use our Inﬂuence Vectors from 5.1 to determine the top R&B artists of all time in terms of Direct Katz Inﬂuence.

<!-- b000450 | prose | pages [18] -->
˜KNg,α1(v) Artist 1. 1.00 Sam Cooke 2. 0.96 Marvin Gaye 3. 0.89 Stevie Wonder 4. 0.87 James Brown 5. 0.70 Gallant

<!-- b000451 | caption | pages [18] -->
Table 8: Most inﬂuential R&B artists as determined by direct Katz Centrality within genre, normalized.

<!-- b000452 | prose | pages [18] -->
Our results suggest that the artists in Table 8 had the greatest impact on R&B since the birth of the genre. On the other hand, the top R&B Revolutionaries of the 1990s were the important ﬁgures that catalyzed the biggest Revolution of R&B.

<!-- b000453 | prose | pages [18] -->
5.7 Historical Impact of Technology on Sound, Genre, and Inﬂuence

<!-- b000454 | prose | pages [18] -->
A lot of literature describes the evolution of music throughout the last century in terms of changes in sound, genre, and the mainstream. In this section, we seek to understand our identiﬁed revolutions in the context of well-known moments of social, political, and technological history of music.

<!-- b000455 | prose | pages [18] -->
For each revolution we identiﬁed, we offer possible historical context based on several sources offering summaries of the evolution of music:

<!-- b000456 | prose | pages [18] -->
• Revolution of the Mainstream in the 1930s: According to [12], the 1930s were a tremendous period of change due to the rise of Jazz and Blues as major genres. Sure enough, we identiﬁed the Blues artist Howlin’ Wolf and the Jazz artist Nat King Cole as two of the top revolutionaries in this period.

<!-- b000457 | prose | pages [18, 19] -->
The 1920s to 1950s is also considered the golden age of radio, so this technological development may have contributed to musical change in the 1930s. Our model suggests that the 1930s were the most signiﬁcant period of change in the sonic properties of music overall in the last 90 years.

<!-- b000458 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000459 | furniture | pages [18] -->
关注数学模型

<!-- b000460 | furniture | pages [18] -->
2

<!-- b000461 | furniture | pages [18] -->
mcm/icm 2021

<!-- b000462 | furniture | pages [18] -->
sonic & iconic

<!-- b000463 | furniture | pages [18] -->
MATHmodels

<!-- b000464 | furniture | pages [18] -->
获取更多资讯

<!-- b000465 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000466 | furniture | pages [19] -->
team 2124668

<!-- b000467 | furniture | pages [19] -->
page 17

<!-- b000469 | prose | pages [19] -->
• Revolution of “I Will Survive” Genre in the 1960s: According to [12], the 1960s are most notable for 微信公众号：数学模型 the British Invasion, a period in which the Pop/Rock genre exerted great inﬂuence. Sure enough, we already identiﬁed this era as a Revolution of Mainstreaming Pop/Rock. What’s fascinating about the Revolution of the “I Will Survive Genre” is that it represents a major change during this period that is distinct from the British Invasion. The top two revolutionaries of the “I Will Survive” Genre are both R&B artists. We speculate that this Revolution of Sonic Genre is a dramatic change in musical style that rarely shows up in musical historiography due to the focus on constructs of genre rather than pure sonic data. We argue that this is the reason to also consider musical history from the perspective of Sonic Genres.

<!-- b000470 | prose | pages [19] -->
• Revolution of R&B in the 1990s: According to [17], the 1990s were a transformative period for R&B due to the sudden popularity of emerging genres like Hip Hop and Neo-Soul. While neither of these genres are included in our data, we attribute the sudden R&B shift to these other important genres.

<!-- b000471 | prose | pages [19] -->
[17] mentions Mary J. Blige and D’Angelo, both of whom our model identiﬁed as revolutionaries.

<!-- b000472 | prose | pages [19] -->
• Revolutions of Mainstreaming Genre 微信号：MATHmodels – Mainstreaming Jazz in the 1950s: As we already established, [12] describes the critical period of Jazz popularity as the 1930s rather than the 1950s. Instead, this article describes the 1950s as largely deﬁned by emerging genres such as R&B and Rock. We speculate that the reason for this discrepancy may have to do with Genre Entropy. Since the popularity of Jazz peaked in the 1930s, Jazz likely had tremendous inﬂuence on next generation artists of all genres. We believe this revolution may indicate that artists in mainstream genres of the 1950s drew from past inﬂuence and thus pushed the sonic data of the mainstream to be more similar to Jazz.

<!-- b000473 | prose | pages [19] -->
– Mainstreaming Pop/Rock Revolution of the 1960s [12]: describes the British Invasion of the 1960s, a period in the Pop/Rock genre exploded in popularity. It is unsurprising that this is our most extreme Revolution of Mainstreaming Genre in terms of change.

<!-- b000474 | prose | pages [19] -->
– Mainstreaming Electronic Revolution in the 2000s: [6] explains that, starting in the 1990s and throughout the 2000s, electronic music dramatically increased in popularity due to the improvement of computers and the invention of the internet. We suspect mainstream genres also began to employ electronic music styles more frequently. Our model clearly captures this moment of technological and musical change.

<!-- b000475 | prose | pages [19] -->
6

<!-- b000476 | heading | pages [19] -->
Sensitivity Analysis

<!-- b000477 | prose | pages [19] -->
In 5.1.2, we deﬁne a meaningful subnetwork that we could use as a model input by removing all artists but those from the largest 5 Established Genres. Otherwise, our model for determining inﬂuence using InfVec(v) was too sensitive to artists in the smaller genres when we tried to determine the most inﬂuential artists using Direct KC and Indirect KC on N ⩾2000.

<!-- b000478 | prose | pages [19] -->
As shown in Figures 2 and 3, changing α biases which artists are considered inﬂuential to either younger or older artists. This is a balancing act to ensure all artists have a chance to be recognized later on as revolutionaries in any time period according to the Katz centrality metric.

<!-- b000479 | prose | pages [19] -->
Additionally, the Katz centrality metric has issues when comparing values from different networks. Since the centrality depends heavily on the order of the network, we adjusted the constant term in Equation 1 (see Sec. 5.2.1), however this change was mostly based on quality of results. A more robust model would provide a more systematic adjustment here.

<!-- b000480 | prose | pages [19, 20] -->
Smaller genres continue to pose problems when trying to develop a neural network to predict genre from sonic features. Before we decided to add class weights, the imbalance of the number of artists in each genre meant that the model could predict that the sonic variable inputs corresponded to “Pop/Rock” every time and achieve over 50% accuracy. Thus, we added class weights. Again we had to limit the number of Established Genres we considered to four before our neural network was able to make decent predictions.

<!-- b000481 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000482 | furniture | pages [19] -->
关注数学模型

<!-- b000483 | furniture | pages [19] -->
2

<!-- b000484 | furniture | pages [19] -->
mcm/icm 2021

<!-- b000485 | furniture | pages [19] -->
sonic & iconic

<!-- b000486 | furniture | pages [19] -->
MATHmodels

<!-- b000487 | furniture | pages [19] -->
获取更多资讯

<!-- b000488 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000489 | furniture | pages [20] -->
team 2124668

<!-- b000490 | furniture | pages [20] -->
page 18

<!-- b000492 | prose | pages [20] -->
Later when we tried to put all artists into Sonic Genres, we had to choose how many cluster centroids to instantiate. We chose 4 because it correlated with our previous analysis to use the neural network 微信公众号：数学模型 to predict the top 4 genres based on sound. It also had the highest Adjusted Rand Index compared to other amounts of clusters. However, the number of clusters is still a hyperparameter to be tuned and is sensitive to adjustments. Furthermore, our machine learning methods to deﬁne and connect the Sonic and Established Genres with sonic variable inputs depend on many hyperparameters. Tuning these variables could make the model more robust.

<!-- b000493 | prose | pages [20] -->
7 Error Analysis

<!-- b000494 | prose | pages [20] -->
“If you learn music, you’ll learn mathematics. If you learn music, you’ll learn most all there is to learn.”

<!-- b000495 | prose | pages [20] -->
Edgar Cayce

<!-- b000496 | prose | pages [20] -->
微信号：MATHmodels First, our model could not entirely predict Sonic Genres from sonic variables with our neural network (only 52.0% accurate). This could be a result of our hyperparameter choices like the number of clusters provided to K-Means as a parameter. Often when clustering with K-Means, researchers plot the data in 2 or 3 dimensions and then decide how many clusters to use as an input based on how the data appears to cluster into natural groups.

<!-- b000497 | prose | pages [20] -->
Another source of potential error arises in 5.4 and appears in 6. We identiﬁed speechiness and duration as the top contagious sonic variables but both of these metrics would likely be consistent within a genre. For this reason, we may be measuring how genre relates to inﬂuence more than how the sonic variables themselves relate to inﬂuence.

<!-- b000498 | prose | pages [20] -->
When identifying moments of revolution and their correspondent revolutionaries, we use metrics from almost every stage of our model development. Thus, any source of error in our model may contribute to inaccuracy in this classiﬁcation. On the other hand, most of the revolutions we identify do line up with famous moments of musical change. While we speculate the other revolutions are also meaningful, they could be a product of error which accumulated throughout our model creation.

<!-- b000499 | prose | pages [20] -->
We would love to have better error analysis but due to the nature of this inquiry as an exploratory analysis, it was difﬁcult to validate our results. We only had access to the data provided and could not validate beyond our neural network the Sonic Genres or the choices of revolutionary eras for which we determined revolutionaries. We did our best to support our choices, i.e. sonic similarity metrics and inﬂuence metrics, with background research, but the ﬁnal list of artists considered inﬂuential and revolutionaries were impossible to validate against a ground truth. This speaks to the nature of using math to determine musical revolutionaries and inﬂuence; some elements will always be subjective and difﬁcult to quantify in a fair way.

<!-- b000500 | prose | pages [20] -->
8

<!-- b000501 | heading | pages [20] -->
Conclusions

<!-- b000502 | prose | pages [20] -->
The construction of our model led to several major conclusions. In 5.1, we found that there are many different types of inﬂuence, each of which leads to distinct conclusions about which artists are the most important. In 5.2 and 5.3, we found that genres are dynamic and interconnected and do not depend greatly on sonic content. In 5.4, we found that speechiness and duration were the most “contagious” sonic variables passing from inﬂuencers to followers. Finally, in sections 5.5, 5.6, and 5.7, we use our model to identify revolutions of four different types throughout the last 90 years. We believe our model has several key strengths that led to these interesting results while also being limited by certain weakness:

<!-- b000503 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000504 | furniture | pages [20] -->
关注数学模型

<!-- b000505 | furniture | pages [20] -->
2

<!-- b000506 | furniture | pages [20] -->
mcm/icm 2021

<!-- b000507 | furniture | pages [20] -->
sonic & iconic

<!-- b000508 | furniture | pages [20] -->
MATHmodels

<!-- b000509 | furniture | pages [20] -->
获取更多资讯

<!-- b000510 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000511 | furniture | pages [21] -->
team 2124668

<!-- b000512 | furniture | pages [21] -->
page 19

<!-- b000513 | prose | pages [21] -->
8.1 Strengths

<!-- b000514 | prose | pages [21] -->
• We quantify sonic similarity across the entire network using Sonic Genres. We use our Sonic Genres to establish new metrics of inﬂuence and pinpoint revolutionary shifts in music i.e. when artists 微信公众号：数学模型 popularize new sounds or tempos. While viewing music history from the perspective of Established Genre is undeniably valuable, our Sonic Genres represent a lens on the evolution of history based solely on sound itself.

<!-- b000515 | prose | pages [21] -->
• We use Katz Centrality, which was introduced in [1], as a metric for inﬂuence. We improve on this metric greatly by adjusting and reﬁning to account for time, direct and indirect inﬂuence, and network size. We also apply it to distinct subnetworks to generate even more metrics.

<!-- b000516 | prose | pages [21] -->
• We adapt the concept of genre entropy from [1] to a narrower scope, looking at the genre breadth of inﬂuence for speciﬁc artists. This is a relatively unique metric that balances out our consideration of an artist’s inﬂuence within their own genre.

<!-- b000517 | prose | pages [21] -->
• In deﬁning musical revolutionaries, we not only consider our inﬂuence vectors from 5.1 but also incorporate our measure of musical similarity. In this way, we synthesize distinct portions of our model. 微信号：MATHmodels 8.2 Weaknesses

<!-- b000518 | prose | pages [21] -->
• Many sources such as [15] analyze musical similarity based on highly reﬁned and complicated functions on sonic data points. Our measure of sonic similarity is based on Euclidean Distance. In 5.2, we justify this measure of similarity as effective and suitable for our purposes. With more time, however, we could make great improvements to it.

<!-- b000519 | prose | pages [21] -->
• As discussed throughout the paper, we made subjective choices. For example, we set the revolution thresholds at values that yield a few clear peaks. We felt that this was necessary to make relevant conclusions.

<!-- b000520 | prose | pages [21] -->
• In 5.7, we seek to align the revolutions we identiﬁed with sources summarizing musical history. There is clearly some bias in this process since we start from a given revolution and then match it to a reasonable historical explanation. With more time, we would validate our model by analyzing the proportion of major musical revolutions in literature that our model identiﬁes.

<!-- b000521 | prose | pages [21] -->
9 Future Considerations

<!-- b000522 | prose | pages [21] -->
We have Sonic Genres, we have Established Genres, but what about...Inﬂuence Genres? One future path would be to group the inﬂuence network based on communities. We initially attempted this computation using the Girvan-Newman algorithm [5] but it proved too computationally expensive given the size of our inﬂuence network. However, with more computing power and processing time, Inﬂuence Genres could provide further partition which one could explore using the Adjusted Rand Index. We could also compare Inﬂuence Genres to Sonic Genres using the Adjusted Rand Index to evaluate using another metric beyond the ones described in this paper whether or not artists who inﬂuence each other sound the same. We predict that Inﬂuence Genres would match better to Established Genres compared to Sonic Genres.

<!-- b000523 | prose | pages [21] -->
Another future path would be adding new deﬁnitions of revolution to include moments were genres are either born or mostly disappear. These are clearly moments of tremendous musical change and it would be fascinating to consider which revolutionaries are responsible for them. We refrain from doing this because we feel it would be extremely difﬁcult to quantify these processes, which are highly dependent on other genres and may occur gradually over long periods of time.

<!-- b000524 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000525 | furniture | pages [21] -->
关注数学模型

<!-- b000526 | furniture | pages [21] -->
2

<!-- b000527 | furniture | pages [21] -->
mcm/icm 2021

<!-- b000528 | furniture | pages [21] -->
sonic & iconic

<!-- b000529 | furniture | pages [21] -->
MATHmodels

<!-- b000530 | furniture | pages [21] -->
获取更多资讯

<!-- b000531 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000532 | furniture | pages [22] -->
team 2124668

<!-- b000533 | furniture | pages [22] -->
page 20

<!-- b000534 | prose | pages [22] -->
10

<!-- b000535 | heading | pages [22] -->
Letter to ICM

<!-- b000536 | prose | pages [22] -->
Dear Integrative Collective Music Society, 微信公众号：数学模型 We have carefully analyzed the data you provided and have come to some conclusions which we expect you will ﬁnd very interesting. As music experts, we imagine you often engage in intense debates over which artists are most inﬂuential. To consider different perspectives on impact, we have found a quantitative way to rate both the direct and indirect inﬂuence of any artist, as well as an artist’s effect on their own and other genres. We found Frank Ocean to be the overall most inﬂuential artist of the 21st century.

<!-- b000537 | prose | pages [22] -->
We also started to question the incorporation of genre into almost every conversation about music history. Genre is undoubtedly important to music, but how well does it predict musical elements? Our model says not very well, suggesting genre is not closely linked to sound data. For that reason, we pretended to have no concept of genre and created our own categories based on sound data alone. We named these 4 “Sonic Genres” after famous songs that roughly represent the sound of each category as a whole. We created the “Here Comes the Sun” Genre for folksy music, the “Thunderstruck” Genre for high-energy music, the “I Will Survive” Genre for danceable music and the “Swan Lake” Genre for instrumental music.

<!-- b000538 | prose | pages [22] -->
Next, we used our model to identify the most important musical revolutions and revolutionaries of the 微信号：MATHmodels last century. We ﬁrst considered moments when music overall changed dramatically in sound. As you might predict, the most signiﬁcant period coincided with the Rise of Jazz and Blues in the 1930s with Howlin’ Wolf as the top revolutionary. Next, we investigated moments when the R&B genre changed dramatically and found the most signiﬁcant revolution to be the 1990s with Mary J. Blige as the top revolutionary.

<!-- b000539 | prose | pages [22] -->
In order to provide music fans everywhere with quantitative evidence supporting their complaints that their favorite genre has become “too mainstream,” we also analyzed revolutions in which certain genres and the mainstream suddenly became more similar. We identiﬁed eras of music you would expect such as Pop/Rock becoming more mainstream in the 1960s with the British Invasion.

<!-- b000540 | prose | pages [22] -->
Finally, we looked for revolutions in the “Sonic Genres” we created based solely on sound. The “I Will Survive” Genre went through a dramatic change during the 1960s–but not because of the British Invasion. Instead, this was the result of revolutionary artists of other genres like R&B legend Barry White. We believe this is evidence that our “Sonic Genres” are capturing moments of change that might not be evident in a traditional musical history.

<!-- b000541 | prose | pages [22] -->
Of course our ﬁndings are limited to the data we used. For instance, Hip Hop artists weren’t included in the data, even though they likely had a huge impact on the revolution of R&B in the 1990s. With more data, we could continue identifying different types of musical revolutions with greater precision. We could thus craft detailed, parallel histories of musical evolution in terms of both the genres we know and the “Sonic Genres” that naturally emerge from sound content alone. With these tools, we believe we could identify and discover many fascinating periods of change; perhaps one day Barry White will be considered as much of a revolutionary as The Beatles.

<!-- b000542 | prose | pages [22] -->
Sincerely, Team 2124668

<!-- b000543 | heading | pages [22] -->
References

<!-- b000544 | references | pages [22] -->
[1]

<!-- b000545 | references | pages [22] -->
Nicholas Bryan and Ge Wang. Musical Inﬂuence Network Analysis and Rank of Sample-Based Music. Jan.

<!-- b000546 | references | pages [22] -->
2011.

<!-- b000547 | references | pages [22] -->
[2]

<!-- b000548 | references | pages [22] -->
Pedro Cano and Markus Koppenberger. The emergence of complex network patterns in music networks.

<!-- b000549 | references | pages [22] -->
Jan. 2004.

<!-- b000550 | references | pages [22] -->
[3]

<!-- b000551 | references | pages [22] -->
Francois Chollet et al. Keras. 2015. url: https://github.com/fchollet/keras.

<!-- b000552 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000553 | furniture | pages [22] -->
关注数学模型

<!-- b000554 | furniture | pages [22] -->
2

<!-- b000555 | furniture | pages [22] -->
mcm/icm 2021

<!-- b000556 | furniture | pages [22] -->
sonic & iconic

<!-- b000557 | furniture | pages [22] -->
MATHmodels

<!-- b000558 | furniture | pages [22] -->
获取更多资讯

<!-- b000559 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000560 | furniture | pages [23] -->
team 2124668

<!-- b000561 | furniture | pages [23] -->
page 21

<!-- b000562 | references | pages [23] -->
[4]

<!-- b000563 | references | pages [23] -->
Nick Collins. Computational Analysis of Musical Inﬂuence: A Musicological Case Study Using MIR Tools.

<!-- b000564 | references | pages [23] -->
Jan. 2010.

<!-- b000565 | references | pages [23] -->
[5]

<!-- b000566 | references | pages [23] -->
M. Girvan and M. E. J. Newman. “Community structure in social and biological networks”. In:

<!-- b000567 | references | pages [23] -->
Proceedings of the National Academy of Sciences 99.12 (2002), pp. 7821–7826. issn: 0027-8424. doi:

<!-- b000568 | references | pages [23] -->
微信公众号：数学模型

<!-- b000569 | references | pages [23] -->
10.1073/pnas.122653799. eprint: https://www.pnas.org/content/99/12/7821.full.pdf. url:

<!-- b000570 | references | pages [23] -->
https://www.pnas.org/content/99/12/7821.

<!-- b000571 | references | pages [23] -->
[6]

<!-- b000572 | references | pages [23] -->
Omar Hage-Hassan. The Evolution of Electronic Music. Apr. 2017. url: https://medium.com/4thought-

<!-- b000573 | references | pages [23] -->
studios/the-evolution-of-electronic-music-9c9bd6156874.

<!-- b000574 | references | pages [23] -->
[7]

<!-- b000575 | references | pages [23] -->
Alexander Hinneburg, Charu C. Aggarwal, and Daniel A. Keim. “What Is the Nearest Neighbor

<!-- b000576 | references | pages [23] -->
in High Dimensional Spaces?” In: Proceedings of the 26th International Conference on Very Large Data

<!-- b000577 | references | pages [23] -->
Bases. VLDB ’00. San Francisco, CA, USA: Morgan Kaufmann Publishers Inc., 2000, pp. 506–515. isbn:

<!-- b000578 | references | pages [23] -->
1558607153.

<!-- b000579 | references | pages [23] -->
Lawrence Hubert and Phipps Arabie. Comparing partitions. 1985. url: https://EconPapers.repec.

<!-- b000580 | references | pages [23] -->
[8]

<!-- b000581 | references | pages [23] -->
org/RePEc:spr:jclass:v:2:y:1985:i:1:p:193-218.

<!-- b000582 | references | pages [23] -->
[9]

<!-- b000583 | references | pages [23] -->
Fragkiskos D. Malliaros and Michalis Vazirgiannis. “Clustering and community detection in directed

<!-- b000584 | references | pages [23] -->
networks: A survey”. In: Physics Reports 533.4 (Dec. 2013), pp. 95–142. issn: 0370-1573. doi: 10.1016/

<!-- b000585 | references | pages [23] -->
微信号：MATHmodels

<!-- b000586 | references | pages [23] -->
j.physrep.2013.08.002.

<!-- b000587 | references | pages [23] -->
[10]

<!-- b000588 | references | pages [23] -->
F. Pedregosa et al. “Scikit-learn: Machine Learning in Python”. In: Journal of Machine Learning Research

<!-- b000589 | references | pages [23] -->
12 (2011), pp. 2825–2830.

<!-- b000590 | references | pages [23] -->
[11]

<!-- b000591 | references | pages [23] -->
S. Ranjan et al. “Hyperspectral image classiﬁcation: A k-means clustering based approach”. In: 2017

<!-- b000592 | references | pages [23] -->
4th International Conference on Advanced Computing and Communication Systems (ICACCS). 2017, pp. 1–7.

<!-- b000593 | references | pages [23] -->
doi: 10.1109/ICACCS.2017.8014707.

<!-- b000594 | references | pages [23] -->
[12]

<!-- b000595 | references | pages [23] -->
[Author Removed at Request of the Publisher]. 6.2 The Evolution of Popular Music. Mar. 2016.

<!-- b000596 | references | pages [23] -->
[13]

<!-- b000597 | references | pages [23] -->
Melena Ryzik. How ’Sesame Street’ Started a Musical Revolution. Aug. 2019. url: https://www.nytimes.

<!-- b000598 | references | pages [23] -->
com/2019/08/22/arts/music/sesame-street-anniversary.html.

<!-- b000599 | references | pages [23] -->
[14]

<!-- b000600 | references | pages [23] -->
P. Prusinkiewicz S. J. Wan S. K. M. Wong. An algorithm for multidimensional data clustering. June 1988.

<!-- b000601 | references | pages [23] -->
doi: 10.1145/45054.45056.

<!-- b000602 | references | pages [23] -->
Joan Serr`a et al. Measuring the Evolution of Contemporary Western Popular Music. May 2012. doi:

<!-- b000603 | references | pages [23] -->
[15]

<!-- b000604 | references | pages [23] -->
10.1038/srep00521.

<!-- b000605 | references | pages [23] -->
[16]

<!-- b000606 | references | pages [23] -->
S. Vishnupriya and K. Meenakshi. “Automatic Music Genre Classiﬁcation using Convolution Neural

<!-- b000607 | references | pages [23] -->
Network”. In: 2018 International Conference on Computer Communication and Informatics (ICCCI). 2018,

<!-- b000608 | references | pages [23] -->
pp. 1–4. doi: 10.1109/ICCCI.2018.8441340.

<!-- b000609 | references | pages [23] -->
Donovan Wilkins et al. The Evolution of R&B. Dec. 1969. url: https://www.tucmag.net/music/the-

<!-- b000610 | references | pages [23] -->
[17]

<!-- b000611 | references | pages [23] -->
evolution-of-rb/.

<!-- b000612 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000613 | furniture | pages [23] -->
关注数学模型

<!-- b000614 | furniture | pages [23] -->
2

<!-- b000615 | furniture | pages [23] -->
mcm/icm 2021

<!-- b000616 | furniture | pages [23] -->
sonic & iconic

<!-- b000617 | furniture | pages [23] -->
MATHmodels

<!-- b000618 | furniture | pages [23] -->
获取更多资讯
