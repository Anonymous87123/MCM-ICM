# P-C-2014-28199-d39873d7

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->
Team # 28199                                                                Page 1 of 21

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | title | pages [1] -->
28199

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | prose | pages [1] -->
T1 ________________

<!-- b000007 | prose | pages [1] -->
T2 ________________

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | prose | pages [1] -->
T3 ________________

<!-- b000010 | prose | pages [1] -->
For office use only

<!-- b000011 | prose | pages [1] -->
F1 ________________

<!-- b000012 | prose | pages [1] -->
F2 ________________

<!-- b000013 | prose | pages [1] -->
F3 ________________

<!-- b000014 | prose | pages [1] -->
Problem Chosen

<!-- b000015 | prose | pages [1] -->
T4 ________________

<!-- b000016 | furniture | pages [1] -->


<!-- b000017 | prose | pages [1] -->
F4 ________________

<!-- b000018 | title | pages [1] -->
C

<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | heading | pages [1] -->
2014 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000023 | prose | pages [1] -->
Problem Clarification

<!-- b000024 | prose | pages [1] -->
In this paper, we build several networks, study their properties, and build models to measure players’ influence. Off-the-shelf measures like degree are not optimal for influence estimation, because they do not consider all aspects of the network. We seek to define more accurate measures based on previous research for various networks and explore their utility in real life. Model Design

<!-- b000025 | prose | pages [1] -->
Conventional measures such as centrality usually neglect some aspects of networks, for example, the weights of edges. Stephen P. Borgatti (2006) introduces a cohesion measure called KPP-NEG, but the order of nodes is still ignored, which causes inaccuracy.

<!-- b000026 | prose | pages [1] -->
We combine the Shapley approach with the cohesion measure to obtain the Shapley value of each node, which represents its contribution to the whole network’s cohesion. It involves weight, structure, and order of nodes at the same time, which makes it superior to both conventional measures and KPP-NEG. However, this new approach can’t be applied to directed networks.

<!-- b000027 | prose | pages [1] -->
Therefore, we use Pagerank algorithm derived from website networks to deal with directed networks like the citation network. But the basic method is not suitable for citation networks due to the differences between websites and papers and the limited network size. So we optimize it by adding a virtual node representing papers outside the network in two steps. The first is to adjust the weight of edges according to references. The second involves Times Cited of the target paper.

<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | caption | pages [1] -->
Figure 1. Model Design Process

<!-- b000030 | heading | pages [1] -->
Results

<!-- b000031 | prose | pages [1] -->
Erdos network is a small-world network according to its path length and clustering coefficient. Meanwhile, its degree distribution shows a feature of free-scale network.

<!-- b000032 | prose | pages [1] -->
For undirected networks, the Shapley value of Edros Network shows that the most influential co-author is ALON, NOGA M., which is different from that ranked by betweenness. The Shapley value implemented in the movie star network shows that the most influential star is Matt Damon, which is the same as that ranked by betweenness due to the relatively small size of the network.

<!-- b000033 | prose | pages [1] -->
For directed networks -- the citation network of 16 papers provided, the most influential paper remains the same whether in the extensive network or not, which is No.14. But the ranks of some papers change with different versions of Pagerank method.

<!-- b000034 | prose | pages [1] -->
Sensitivity analysis suggests that ranks based on Shapley value is sensitive to sample size, while ranks based on Pagerank is not sensitive to damping factor.

<!-- b000035 | furniture | pages [2] -->


<!-- b000036 | furniture | pages [2] -->
Team # 28199                                                                Page 2 of 21

<!-- b000037 | prose | pages [2] -->
Influence Measures in Networks

<!-- b000038 | furniture | pages [2] -->


<!-- b000039 | heading | pages [2] -->
Introduction

<!-- b000040 | prose | pages [2] -->
Problem Clarification

<!-- b000041 | prose | pages [2] -->
The study of complex networks is a young area of scientific research inspired

<!-- b000042 | prose | pages [2] -->
largely by the empirical study of real-world networks such as computer networks and

<!-- b000043 | prose | pages [2] -->
social networks.  With the development of society and technology, more and more

<!-- b000044 | prose | pages [2] -->
networks spring up in various aspects of our life. Properties of networks have been

<!-- b000045 | prose | pages [2] -->
widely explored, and models are needed to measure the influence and impact of

<!-- b000046 | prose | pages [2] -->
players in different networks. However, few researches considerate weight, structure

<!-- b000047 | prose | pages [2] -->
and order of notes at the same time, so we seek to define more accurate measures

<!-- b000048 | prose | pages [2] -->
based on previous research for networks with and without directions or weight.

<!-- b000049 | heading | pages [2] -->
Model Design

<!-- b000050 | prose | pages [2] -->
The most typical conventional measurement is centrality, which includes degree,

<!-- b000051 | furniture | pages [2] -->


<!-- b000052 | prose | pages [2] -->
betweenness and closeness. However, both degree and closeness neglect the weight

<!-- b000053 | prose | pages [2] -->
of each connection. In addition, Stephen P. Borgatti (2006) argues that the optimality

<!-- b000054 | prose | pages [2] -->
of betweenness in identifying the node whose removal from the network would most

<!-- b000055 | prose | pages [2] -->
reduce cohesion is not guaranteed under typical definitions of cohesion, and

<!-- b000056 | prose | pages [2] -->
introduces a cohesion measurement called KPP-POS to overcome the defects of

<!-- b000057 | prose | pages [2] -->
conventional approaches, but the order of nodes are ignored which causes

<!-- b000058 | prose | pages [2] -->
inaccuracy.

<!-- b000059 | prose | pages [2] -->
We combine the Shapley approach and the KPP-POS measurement to obtain

<!-- b000060 | prose | pages [2] -->
the Shapley value of each node as a influence measure, which represents its

<!-- b000061 | prose | pages [2] -->
contribution to the whole network’s cohesion. It considers the weight, the KPP-POS

<!-- b000062 | prose | pages [2] -->
problem and the order of nodes at the same time, which makes it superior to both

<!-- b000063 | prose | pages [2] -->
conventional measures and KPP-POS.

<!-- b000064 | prose | pages [2] -->
This new approach has many merits, but it can’t be applied to directed networks.

<!-- b000065 | prose | pages [2] -->
Therefore, we use Pagerank algorithm to deal with directed networks such as the

<!-- b000066 | prose | pages [2] -->
citation network. The conventional Pagerank method is applied to website networks,

<!-- b000067 | prose | pages [2] -->
but there are differences between website networks and paper citation networks. For

<!-- b000068 | prose | pages [2] -->
instance, once built, the citation link or network is static while the website links are

<!-- b000069 | prose | pages [2] -->
dynamically adjustable. Besides, the citation data related to papers outside the

<!-- b000070 | prose | pages [2] -->
network is not taken into consideration, which makes the Pagerank value

<!-- b000071 | furniture | pages [3] -->


<!-- b000072 | furniture | pages [3] -->
Team # 28199                                                                Page 3 of 21

<!-- b000073 | prose | pages [3] -->
meaningless in small networks. So we optimized this method by adding a virtual node

<!-- b000074 | prose | pages [3] -->
which represents papers outside the network in two steps. The first step is to adjust

<!-- b000075 | prose | pages [3] -->
the weight allocated to the cited paper according to the total number of its references.

<!-- b000076 | prose | pages [3] -->
In the second step, different weight is given to inside papers by the virtual node based

<!-- b000077 | prose | pages [3] -->
on their Times Cited since publication.

<!-- b000078 | furniture | pages [3] -->


<!-- b000079 | prose | pages [3] -->
Erdos Network

<!-- b000080 | heading | pages [3] -->
Assumptions

<!-- b000081 | prose | pages [3] -->
Co-author networks are undirected. The relationships between pairs of node are 

<!-- b000082 | prose | pages [3] -->
not directed, that is, the two nodes linked by the same line are equal.

<!-- b000083 | prose | pages [3] -->
The influence of the number of joint publications and the date of the first 

<!-- b000084 | prose | pages [3] -->
cooperation can be neglected. Due to the lack of relative information, numbers of

<!-- b000085 | prose | pages [3] -->
joint publications of different pairs are assumed to be the same. Therefore, our

<!-- b000086 | prose | pages [3] -->
Erdos network model is unweighted, but this assumption is released in our

<!-- b000087 | prose | pages [3] -->
movie-star network model.

<!-- b000088 | prose | pages [3] -->
Take no consideration of those with Edros number 2. In order to avoid too much 

<!-- b000089 | prose | pages [3] -->
work, authors whose Erdős numbers are greater than 1 are not involved in this

<!-- b000090 | prose | pages [3] -->
network.

<!-- b000091 | prose | pages [3] -->
Adjacent Matrix

<!-- b000092 | prose | pages [3] -->
The adjacent matrix of the co-author network can be figured out with MATLAB, in

<!-- b000093 | prose | pages [3] -->
  ijr 1 ijr which if i can reach j and 0 0 otherwise. W represents the adjacent

<!-- b000094 | prose | pages [3] -->
matrix and N is the number of nodes in the network.

<!-- b000095 | prose | pages [3] -->


<!-- b000096 | prose | pages [3] -->
r r

<!-- b000097 | prose | pages [3] -->
...

<!-- b000098 | prose | pages [3] -->
11 12

<!-- b000099 | prose | pages [3] -->


<!-- b000100 | prose | pages [3] -->
r r

<!-- b000101 | prose | pages [3] -->
...

<!-- b000102 | prose | pages [3] -->


<!-- b000103 | prose | pages [3] -->
21 22

<!-- b000104 | prose | pages [3] -->


<!-- b000105 | prose | pages [3] -->
W

<!-- b000106 | prose | pages [3] -->


<!-- b000107 | prose | pages [3] -->
...

<!-- b000108 | prose | pages [3] -->
...

<!-- b000109 | prose | pages [3] -->
...

<!-- b000110 | prose | pages [3] -->


<!-- b000111 | prose | pages [3] -->
r r

<!-- b000112 | prose | pages [3] -->
...

<!-- b000113 | prose | pages [3] -->


<!-- b000114 | prose | pages [3] -->
N

<!-- b000115 | prose | pages [3] -->
1

<!-- b000116 | prose | pages [3] -->
N

<!-- b000117 | prose | pages [3] -->
2

<!-- b000118 | prose | pages [3] -->
Network Visualization

<!-- b000119 | prose | pages [3] -->


<!-- b000120 | prose | pages [3] -->
r r

<!-- b000121 | prose | pages [3] -->
1 1

<!-- b000122 | prose | pages [3] -->
N

<!-- b000123 | prose | pages [3] -->


<!-- b000124 | prose | pages [3] -->
r r

<!-- b000125 | prose | pages [3] -->


<!-- b000126 | prose | pages [3] -->
2 2

<!-- b000127 | prose | pages [3] -->
N

<!-- b000128 | prose | pages [3] -->
(1)

<!-- b000129 | prose | pages [3] -->


<!-- b000130 | prose | pages [3] -->
...

<!-- b000131 | prose | pages [3] -->


<!-- b000132 | prose | pages [3] -->
r r

<!-- b000133 | prose | pages [3] -->


<!-- b000134 | prose | pages [3] -->
NN

<!-- b000135 | prose | pages [3] -->
Given the adjacent matrix, we can visualize the network with PAJEK, which is

<!-- b000136 | prose | pages [3] -->
represented in Figure 2. Visualized network can show relations among clusters

<!-- b000137 | prose | pages [3] -->
(global view) and extract nodes that belong to the same clusters (detailed local view).

<!-- b000138 | prose | pages [3] -->
The nodes in the center part of the network are closed to each other while there are

<!-- b000139 | prose | pages [3] -->
37 isolates at the edge. The graph shows that the node representing ALON, NOGA M.

<!-- b000140 | prose | pages [3] -->
has a degree of 52, which is the highest degree in Erdos network.

<!-- b000141 | furniture | pages [4] -->


<!-- b000142 | furniture | pages [4] -->
Team # 28199                                                                Page 4 of 21

<!-- b000143 | furniture | pages [4] -->


<!-- b000144 | caption | pages [4] -->
Figure 2. Node size corresponds to the degree of each author, a simple measure of

<!-- b000145 | prose | pages [4] -->
influence. Numbers beside the nodes represent the corresponding author.

<!-- b000146 | furniture | pages [4] -->


<!-- b000147 | prose | pages [4] -->
Properties of Network

<!-- b000148 | prose | pages [4] -->
Complex networks include small-world networks and free-scale networks.

<!-- b000149 | prose | pages [4] -->
Small-world networks are between regular networks and random networks. To

<!-- b000150 | prose | pages [4] -->
determine which type Erdos network belongs to, we analyze properties of it with three

<!-- b000151 | prose | pages [4] -->
measures [Albert,R. and Barabasi,A-L.,2002]: degree distribution, average path length

<!-- b000152 | prose | pages [4] -->
and clustering coefficient.

<!-- b000153 | prose | pages [4] -->
Firstly, degree distribution is the probability distribution of degrees over the whole

<!-- b000154 | prose | pages [4] -->
network. To demonstrate better the feature of the degree distribution of this network,

<!-- b000155 | prose | pages [4] -->
we plot the degree frequencies in Figure 3. A random network with same number of

<!-- b000156 | prose | pages [4] -->
nodes is also analyzed as a comparison.

<!-- b000157 | furniture | pages [4] -->


<!-- b000158 | caption | pages [4] -->
Figure 3. Degree Distribution of Erdos Network & Random Network with Same

<!-- b000159 | prose | pages [4] -->
Number of Nodes

<!-- b000160 | furniture | pages [5] -->


<!-- b000161 | furniture | pages [5] -->
Team # 28199                                                                Page 5 of 21

<!-- b000162 | prose | pages [5] -->
As is shown in Figure 3, the random network has a pronounced peak at average

<!-- b000163 | prose | pages [5] -->
degree 6.41, while the degrees of Erdos network follow the power-law distribution,

<!-- b000164 | prose | pages [5] -->
showing a feature of scale-free networks.

<!-- b000165 | prose | pages [5] -->
Secondly, the average path length of Erdos network is 3.82, which is defined as

<!-- b000166 | prose | pages [5] -->
the average number of steps along the shortest paths for all possible pairs of network

<!-- b000167 | prose | pages [5] -->
nodes, measuring the efficiency of information or mass transport on the network. The

<!-- b000168 | prose | pages [5] -->
result shows that the average path length of Erdos Network is very low.

<!-- b000169 | prose | pages [5] -->
Thirdly, the Watts-Strogatz clustering coefficient is 0.3428, so the nodes in Erdos

<!-- b000170 | prose | pages [5] -->
network tend to cluster together in a relatively deep extent.

<!-- b000171 | prose | pages [5] -->
The two preceding measures are calculated as follows (N is the number of nodes,

<!-- b000172 | prose | pages [5] -->
E is the number of edges, an edge eij connects node vi with node vj):

<!-- b000173 | prose | pages [5] -->
1

<!-- b000174 | prose | pages [5] -->


<!-- b000175 | prose | pages [5] -->


<!-- b000176 | prose | pages [5] -->
l r

<!-- b000177 | prose | pages [5] -->
(2)

<!-- b000178 | prose | pages [5] -->
G ij

<!-- b000179 | prose | pages [5] -->


<!-- b000180 | prose | pages [5] -->
N ( N )1

<!-- b000181 | prose | pages [5] -->


<!-- b000182 | prose | pages [5] -->
i j

<!-- b000183 | prose | pages [5] -->


<!-- b000184 | prose | pages [5] -->


<!-- b000185 | prose | pages [5] -->
2

<!-- b000186 | prose | pages [5] -->
e

<!-- b000187 | prose | pages [5] -->
:

<!-- b000188 | prose | pages [5] -->
v

<!-- b000189 | prose | pages [5] -->
,

<!-- b000190 | prose | pages [5] -->
v

<!-- b000191 | prose | pages [5] -->
jk j k

<!-- b000192 | prose | pages [5] -->


<!-- b000193 | prose | pages [5] -->
CC

<!-- b000194 | prose | pages [5] -->


<!-- b000195 | prose | pages [5] -->
i k k

<!-- b000196 | prose | pages [5] -->
i i

<!-- b000197 | prose | pages [5] -->
n

<!-- b000198 | prose | pages [5] -->
1

<!-- b000199 | prose | pages [5] -->


<!-- b000200 | prose | pages [5] -->


<!-- b000201 | prose | pages [5] -->
CC CC

<!-- b000202 | prose | pages [5] -->


<!-- b000203 | prose | pages [5] -->


<!-- b000204 | prose | pages [5] -->
N

<!-- b000205 | prose | pages [5] -->
,

<!-- b000206 | prose | pages [5] -->
e E

<!-- b000207 | prose | pages [5] -->
i jk

<!-- b000208 | prose | pages [5] -->
(3)

<!-- b000209 | prose | pages [5] -->
1

<!-- b000210 | prose | pages [5] -->
 

<!-- b000211 | prose | pages [5] -->
(4)

<!-- b000212 | prose | pages [5] -->
i N

<!-- b000213 | prose | pages [5] -->


<!-- b000214 | prose | pages [5] -->
i

<!-- b000215 | prose | pages [5] -->
1

<!-- b000216 | furniture | pages [5] -->


<!-- b000217 | prose | pages [5] -->
In order to describe properties more specifically, we use PAJEK to generate a

<!-- b000218 | prose | pages [5] -->
random network with same number of nodes, which is compared with Erdos network

<!-- b000219 | prose | pages [5] -->
in Table 1. This random network has the same number of nodes and average degree

<!-- b000220 | prose | pages [5] -->
with Erdos network.

<!-- b000221 | furniture | pages [5] -->


<!-- b000222 | caption | pages [5] -->
Table 1. Empirical results of networks

<!-- b000223 | furniture | pages [5] -->


<!-- b000224 | prose | pages [5] -->
L L

<!-- b000225 | furniture | pages [5] -->


<!-- b000226 | furniture | pages [5] -->


<!-- b000227 | furniture | pages [5] -->


<!-- b000228 | prose | pages [5] -->
random actual

<!-- b000229 | prose | pages [5] -->
3.82 3.64

<!-- b000230 | prose | pages [5] -->
CC CC

<!-- b000231 | furniture | pages [5] -->


<!-- b000232 | furniture | pages [5] -->


<!-- b000233 | prose | pages [5] -->
random actual

<!-- b000234 | prose | pages [5] -->
0.3428 0.0153

<!-- b000235 | prose | pages [5] -->
According to the above data, we can see that Erdos network shows the

<!-- b000236 | prose | pages [5] -->
L  L CC  CC but small-world phenomenon:

<!-- b000237 | prose | pages [5] -->
random

<!-- b000238 | prose | pages [5] -->
network is a small-world network.

<!-- b000239 | prose | pages [5] -->
. Therefore, Erdos random

<!-- b000240 | prose | pages [5] -->
The properties of Erdos network are summarized in Table 2. In Table 2 the

<!-- b000241 | prose | pages [5] -->
diagonal elements describe the small-world Erdos network and it is significant to note

<!-- b000242 | prose | pages [5] -->
that Erdos network shares some features with text book network prototypes, but also

<!-- b000243 | prose | pages [5] -->
differs from them. Its clustering coefficient is high while average length path is low, so

<!-- b000244 | furniture | pages [6] -->


<!-- b000245 | furniture | pages [6] -->
Team # 28199                                                                Page 6 of 21

<!-- b000246 | prose | pages [6] -->
the structure is like a small world network, in which most nodes are not neighbors of

<!-- b000247 | prose | pages [6] -->
one another, but most nodes can be reached from every other by a small number of

<!-- b000248 | prose | pages [6] -->
steps. Therefore, even a change of one shortcut can make a great difference in Erdos

<!-- b000249 | prose | pages [6] -->
network. However, since the degrees distribution follows a power law, it also has the

<!-- b000250 | prose | pages [6] -->
property of free-scale networks that a few nodes have many neighbors and they are

<!-- b000251 | prose | pages [6] -->
followed by nodes with smaller degree, which means that there are a few active

<!-- b000252 | prose | pages [6] -->
co-authors who have cooperated with many other co-authors in this network.

<!-- b000253 | furniture | pages [6] -->


<!-- b000254 | caption | pages [6] -->
Table  2. Properties of network: diagonal elements characterize small-world network

<!-- b000255 | prose | pages [6] -->
Properties

<!-- b000256 | prose | pages [6] -->
Clustering

<!-- b000257 | furniture | pages [6] -->


<!-- b000258 | prose | pages [6] -->
Coefficient

<!-- b000259 | prose | pages [6] -->
Networks

<!-- b000260 | prose | pages [6] -->
Regular High

<!-- b000261 | prose | pages [6] -->
Random Low

<!-- b000262 | prose | pages [6] -->
Scale Free Low

<!-- b000263 | furniture | pages [6] -->


<!-- b000264 | furniture | pages [6] -->


<!-- b000265 | prose | pages [6] -->
Average Path

<!-- b000266 | prose | pages [6] -->
Degree

<!-- b000267 | prose | pages [6] -->
Length

<!-- b000268 | prose | pages [6] -->
Distribution

<!-- b000269 | prose | pages [6] -->
High Equal and fixed

<!-- b000270 | prose | pages [6] -->
In/Out degrees to

<!-- b000271 | prose | pages [6] -->
each node

<!-- b000272 | prose | pages [6] -->
Low Exponential

<!-- b000273 | prose | pages [6] -->
Variable Power-law

<!-- b000274 | prose | pages [6] -->
distribution

<!-- b000275 | prose | pages [6] -->
Influence Measure for undirected network:

<!-- b000276 | prose | pages [6] -->
Shapley value

<!-- b000277 | prose | pages [6] -->
We calculate each node’s contribution to the cohesion of the whole network

<!-- b000278 | prose | pages [6] -->
through Shapley approach as the measurement of its influence. And the results are

<!-- b000279 | prose | pages [6] -->
compared with betweeness, which is the most commonly used traditional

<!-- b000280 | prose | pages [6] -->
measurement.

<!-- b000281 | prose | pages [6] -->
Conventional Approaches

<!-- b000282 | prose | pages [6] -->
Centrality is traditionally used to measure the impact of players in a network,

<!-- b000283 | prose | pages [6] -->
which has three aspects: degree, closeness, and betweenness [Freeman, 1979].

<!-- b000284 | prose | pages [6] -->
Degree is defined as the number of edges incident to a node, which is the simplest

<!-- b000285 | prose | pages [6] -->
concept of centrality. Closeness measures a node’s path length to all other nodes.

<!-- b000286 | prose | pages [6] -->
Both of degree and closeness ignore the weight of edges, and can’t be used for

<!-- b000287 | furniture | pages [7] -->


<!-- b000288 | furniture | pages [7] -->
Team # 28199                                                                Page 7 of 21

<!-- b000289 | prose | pages [7] -->
weighted networks. Betweenness centrality is the most commonly used among the

<!-- b000290 | prose | pages [7] -->
three, which quantifies the number of times a node acts as a bridge.  However, the

<!-- b000291 | prose | pages [7] -->
optimality of betweenness in identifying the node whose removal from the network

<!-- b000292 | prose | pages [7] -->
would most reduce cohesion is not guaranteed under typical definitions of cohesion.

<!-- b000293 | prose | pages [7] -->
[Stephen P. Borgatti, 2006]

<!-- b000294 | prose | pages [7] -->
Shapley Value

<!-- b000295 | prose | pages [7] -->
Because of the defects of conventional approaches in measuring a node’s

<!-- b000296 | prose | pages [7] -->
contribution to cohesion of the whole network, Stephen P. Borgatti (2006) introduced

<!-- b000297 | prose | pages [7] -->
a measurement of network’s cohesion. We firstly adjust it to make it applicable for

<!-- b000298 | prose | pages [7] -->
both weighted and unweighted network. In addition, we combine it with Shapley

<!-- b000299 | prose | pages [7] -->
approach to obtain the Shapley value of each node.

<!-- b000300 | prose | pages [7] -->
The measurement of a network’s cohesion is shown as follow:

<!-- b000301 | prose | pages [7] -->
1 2 ∑ 𝑖>𝑗 𝑑𝑖𝑗

<!-- b000302 | prose | pages [7] -->
𝑛(𝑛−1)                                        (5)

<!-- b000303 | prose | pages [7] -->
DF = 1 −

<!-- b000304 | prose | pages [7] -->
Where 𝑛 denotes the number of nodes in the network, and 𝑑𝑖𝑗 represents the

<!-- b000305 | prose | pages [7] -->
distance between node i and j. If there is no link between node i and j, 𝑑𝑖𝑗 is infinite.

<!-- b000306 | prose | pages [7] -->
In order to take the weight of edges into consideration, we adjust the measurement by

<!-- b000307 | prose | pages [7] -->
defining 𝑑𝑖𝑗 as:

<!-- b000308 | prose | pages [7] -->
𝑑𝑖𝑗= { 1 + 1

<!-- b000309 | prose | pages [7] -->
,     i and j are linked

<!-- b000310 | prose | pages [7] -->
(6)

<!-- b000311 | prose | pages [7] -->
𝑝𝑖𝑗

<!-- b000312 | prose | pages [7] -->
∞, i and j are not linked

<!-- b000313 | furniture | pages [7] -->


<!-- b000314 | prose | pages [7] -->
Where 𝑝𝑖𝑗 denotes the weight of the edge between node i and j. Particularly in

<!-- b000315 | prose | pages [7] -->
an unweithed network, 𝑝𝑖𝑗 is infinite, which can be shown as:

<!-- b000316 | furniture | pages [7] -->


<!-- b000317 | prose | pages [7] -->
𝑝𝑖𝑗= {𝑤𝑒𝑖𝑔ℎ𝑡 𝑜𝑓 𝑒𝑑𝑔𝑒,    weithed netwok

<!-- b000318 | prose | pages [7] -->
∞,                   unweithed network                     (7)

<!-- b000319 | furniture | pages [7] -->


<!-- b000320 | prose | pages [7] -->
Stephen P. Borgatti (2006) gets each node’s contribution simply by subtracting

<!-- b000321 | prose | pages [7] -->
DFs of the network with and without the node, which ignores the order of the nodes.

<!-- b000322 | prose | pages [7] -->
This problem can be solved by applying Shapley approach [Shapley, 1953]. Shapley

<!-- b000323 | prose | pages [7] -->
value is typically used in game theory, and has been developed recently into various

<!-- b000324 | prose | pages [7] -->
fields, including influence measurement in networks. The Shapley value can be

<!-- b000325 | prose | pages [7] -->
showed in the following way:

<!-- b000326 | furniture | pages [7] -->


<!-- b000327 | prose | pages [7] -->
Ω𝑖(𝑣) = 1

<!-- b000328 | prose | pages [7] -->
(8)

<!-- b000329 | prose | pages [7] -->
𝑁! ∑(𝑣(𝑃𝑟𝑒𝑖(𝑂)⋃𝑖) −𝑣(𝑃𝑟𝑒𝑖(𝑂)))

<!-- b000330 | prose | pages [7] -->
𝑂∈𝜋𝑁

<!-- b000331 | furniture | pages [8] -->


<!-- b000332 | furniture | pages [8] -->
Team # 28199                                                                Page 8 of 21

<!-- b000333 | prose | pages [8] -->
Where 𝑂 is defined as a permutation of players, 𝑣(𝑃𝑟𝑒𝑖(𝑂)) is the value

<!-- b000334 | prose | pages [8] -->
obtained in permutation 𝑂 by the players preceding player i and 𝑣(𝑃𝑟𝑒𝑖(𝑂)⋃𝑖) is the

<!-- b000335 | prose | pages [8] -->
value obtained in the same permutation when including player i. That is, Ω𝑖(𝑣) gives

<!-- b000336 | prose | pages [8] -->
the average marginal contribution of player i over all permutations.

<!-- b000337 | prose | pages [8] -->
To avoid too much calculation due to the rapid increase of number of

<!-- b000338 | prose | pages [8] -->
permutations with the number of players, the Shapley value can be approximated by

<!-- b000339 | prose | pages [8] -->
the average contribution nodes to network’s cohesion over k randomly sampled

<!-- b000340 | prose | pages [8] -->
permutations, which can be shown as:

<!-- b000341 | furniture | pages [8] -->


<!-- b000342 | prose | pages [8] -->
Ω𝑖(𝑣) ≈Ω̂𝑖(𝑣) = 1

<!-- b000343 | prose | pages [8] -->
(9)

<!-- b000344 | prose | pages [8] -->
𝑘∑(𝑣(𝑃𝑟𝑒𝑖(𝑂)⋃𝑖) −𝑣(𝑃𝑟𝑒𝑖(𝑂)))

<!-- b000345 | prose | pages [8] -->
𝑂∈𝜋𝑘

<!-- b000346 | furniture | pages [8] -->


<!-- b000347 | prose | pages [8] -->
It can be easily proved that the sample mean Ω̂𝑖(𝑣) is an unbiased estimator of

<!-- b000348 | prose | pages [8] -->
the population mean Ω𝑖(𝑣)[ Bluhm M, Faia E, Krahnen J P., 2013].

<!-- b000349 | prose | pages [8] -->
In this case, we combine the adjusted cohesion measurement with the Shapley

<!-- b000350 | prose | pages [8] -->
approach by defining the value used in Shapley equation as the cohesion

<!-- b000351 | prose | pages [8] -->
measurement DF:

<!-- b000352 | prose | pages [8] -->
𝑣= DF                              (10) As a smaller DF indicates a more cohesive network, it is obvious that a negative

<!-- b000353 | prose | pages [8] -->
Shapley value shows a node’s positive contribution to the cohesion of the whole

<!-- b000354 | prose | pages [8] -->
network. And the smaller a node’s Shapley value is, the more contribution it makes to

<!-- b000355 | prose | pages [8] -->
the network’s cohesion, thus it is more influential in the network.

<!-- b000356 | prose | pages [8] -->
Application in Edros Network

<!-- b000357 | prose | pages [8] -->
We firstly apply this methodology to the Edros Network built above, which is an

<!-- b000358 | prose | pages [8] -->
unweighted network, where  , We find the Top 10 influential co-authors, and

<!-- b000359 | prose | pages [8] -->
compare the results with that ranked by betweenness, as is shown in Table 3.

<!-- b000360 | furniture | pages [8] -->


<!-- b000361 | caption | pages [8] -->
Table 3. Top 10 influential co-authors ranked by Shapley value and Betweenness

<!-- b000362 | prose | pages [8] -->
Rank Name(Shapley value)

<!-- b000363 | prose | pages [8] -->
1 ALON, NOGA M.

<!-- b000364 | prose | pages [8] -->
(-0.001865084)

<!-- b000365 | prose | pages [8] -->
2 GYARFAS, ANDRAS

<!-- b000366 | prose | pages [8] -->
(-0.001762582)

<!-- b000367 | prose | pages [8] -->
3 SOS, VERA TURAN

<!-- b000368 | prose | pages [8] -->
(-0.001612491)

<!-- b000369 | prose | pages [8] -->
4 KLEITMAN, DANIEL J.

<!-- b000370 | prose | pages [8] -->
(-0.001596847)

<!-- b000371 | prose | pages [8] -->
Name(Betweenness)

<!-- b000372 | prose | pages [8] -->
HARARY, FRANK*

<!-- b000373 | prose | pages [8] -->
(9587.729986)

<!-- b000374 | prose | pages [8] -->
SOS, VERA TURAN

<!-- b000375 | prose | pages [8] -->
(8912.230744)

<!-- b000376 | prose | pages [8] -->
RUBEL, LEE ALBERT*

<!-- b000377 | prose | pages [8] -->
(8573.363779)

<!-- b000378 | prose | pages [8] -->
STRAUS, ERNST GABOR*

<!-- b000379 | prose | pages [8] -->
(8300.743649)

<!-- b000380 | furniture | pages [9] -->


<!-- b000381 | furniture | pages [9] -->
Team # 28199                                                                Page 9 of 21

<!-- b000382 | prose | pages [9] -->
5 TUZA, ZSOLT

<!-- b000383 | prose | pages [9] -->
(-0.00151064)

<!-- b000384 | prose | pages [9] -->
6 GRAHAM, RONALD LEWIS

<!-- b000385 | prose | pages [9] -->
(-0.001494127)

<!-- b000386 | prose | pages [9] -->
7 BOLLOBAS, BELA

<!-- b000387 | prose | pages [9] -->
(-0.00149078)

<!-- b000388 | prose | pages [9] -->
8 HARARY, FRANK*

<!-- b000389 | prose | pages [9] -->
(-0.001472003)

<!-- b000390 | prose | pages [9] -->
POMERANCE, CARL

<!-- b000391 | prose | pages [9] -->
BERNARD

<!-- b000392 | prose | pages [9] -->
(7434.669391)

<!-- b000393 | prose | pages [9] -->
FUREDI, ZOLTAN

<!-- b000394 | prose | pages [9] -->
(7410.069488)

<!-- b000395 | prose | pages [9] -->
ALON, NOGA M.

<!-- b000396 | prose | pages [9] -->
(6871.898202)

<!-- b000397 | prose | pages [9] -->
GRAHAM, RONALD LEWIS

<!-- b000398 | prose | pages [9] -->
(6817.155314)

<!-- b000399 | prose | pages [9] -->
FAUDREE, RALPH JASPER, 9

<!-- b000400 | prose | pages [9] -->
JR.

<!-- b000401 | prose | pages [9] -->
(-0.0013609)

<!-- b000402 | prose | pages [9] -->
10 RODL, VOJTECH

<!-- b000403 | prose | pages [9] -->
(-0.001300204)

<!-- b000404 | furniture | pages [9] -->


<!-- b000405 | prose | pages [9] -->
BOLLOBAS, BELA

<!-- b000406 | prose | pages [9] -->
(6699.546721)

<!-- b000407 | prose | pages [9] -->
PACH, JANOS

<!-- b000408 | prose | pages [9] -->
(6073.643237)

<!-- b000409 | prose | pages [9] -->
We can see from Table 3 that ALON, NOGA M. makes the most contribution to

<!-- b000410 | prose | pages [9] -->
the Edros Network’s cohesion, while HARARY, FRANK* bridges the most pairs in the

<!-- b000411 | prose | pages [9] -->
network. Moreover, there are five same co-authors in Top 10 ranked by the two

<!-- b000412 | prose | pages [9] -->
different measurements, who are ALON, NOGA M., SOS, VERA TURAN, GRAHAM,

<!-- b000413 | prose | pages [9] -->
RONALD LEWIS, BOLLOBAS, BELA, and HARARY, FRANK*. They are supposed to

<!-- b000414 | prose | pages [9] -->
be the most influential co-authors in the network.

<!-- b000415 | prose | pages [9] -->
Application in Movie Star Network

<!-- b000416 | prose | pages [9] -->
To implement our algorithm on a completely different set of network influence

<!-- b000417 | prose | pages [9] -->
data, we dig the cooperative relations between 20 movie stars who have all

<!-- b000418 | prose | pages [9] -->
cooperated with Jude Law. The same method is used to build the movie star network

<!-- b000419 | prose | pages [9] -->
and find the Top 5 influential stars in the network. Note that the movie star network is

<!-- b000420 | prose | pages [9] -->
a weighted network, and the weight of each edge depends on the times the stars have

<!-- b000421 | prose | pages [9] -->
cooperated.

<!-- b000422 | furniture | pages [9] -->


<!-- b000423 | furniture | pages [10] -->


<!-- b000424 | furniture | pages [10] -->
Team # 28199                                                                Page 10 of 21

<!-- b000425 | furniture | pages [10] -->


<!-- b000426 | caption | pages [10] -->
Figure 4. the Movie Star Network (The width of the edges reflects the times the two

<!-- b000427 | prose | pages [10] -->
stars have cooperated, and the size of the nodes reflects their degrees)

<!-- b000428 | furniture | pages [10] -->


<!-- b000429 | caption | pages [10] -->
Table 4. Top 5 influential movie stars ranked by Shapley value and Betweenness

<!-- b000430 | prose | pages [10] -->
Rank Name(Shapley)

<!-- b000431 | prose | pages [10] -->
1 Matt Damon

<!-- b000432 | prose | pages [10] -->
(-0.045389808)

<!-- b000433 | prose | pages [10] -->
2 Tom Hanks

<!-- b000434 | prose | pages [10] -->
(-0.041607503)

<!-- b000435 | prose | pages [10] -->
3 Robert Downey Jr.

<!-- b000436 | prose | pages [10] -->
(-0.018930241)

<!-- b000437 | prose | pages [10] -->
4 Daniel Craig

<!-- b000438 | prose | pages [10] -->
(-0.01560871)

<!-- b000439 | prose | pages [10] -->
5 Gwyneth Paltrow

<!-- b000440 | prose | pages [10] -->
(-0.014915669)

<!-- b000441 | furniture | pages [10] -->


<!-- b000442 | prose | pages [10] -->
Name(Betweenness)

<!-- b000443 | prose | pages [10] -->
Matt Damon

<!-- b000444 | prose | pages [10] -->
(29.1436926)

<!-- b000445 | prose | pages [10] -->
Tom Hanks

<!-- b000446 | prose | pages [10] -->
(24.3010304)

<!-- b000447 | prose | pages [10] -->
Robert Downey Jr.

<!-- b000448 | prose | pages [10] -->
(18.4906711)

<!-- b000449 | prose | pages [10] -->
Daniel Craig

<!-- b000450 | prose | pages [10] -->
(13.6563631)

<!-- b000451 | prose | pages [10] -->
Kate Winslet

<!-- b000452 | prose | pages [10] -->
(13.5588972)

<!-- b000453 | prose | pages [10] -->
The Top 5 influential movie stars ranked by Shapley value and betweenness are

<!-- b000454 | prose | pages [10] -->
almost the same, which is due to the relatively small size of the network. The

<!-- b000455 | prose | pages [10] -->
difference in the fifth most influential star indicates that the removal of Gwyneth

<!-- b000456 | prose | pages [10] -->
Paltrow has more impact on the cohesion of the network than that of Kate Winslet,

<!-- b000457 | prose | pages [10] -->
although the latter bridges more pairs in the network.

<!-- b000458 | heading | pages [10] -->
Strengths

<!-- b000459 | prose | pages [10] -->
The Shapley value is superior to degree and closeness centrality in that it can be 

<!-- b000460 | prose | pages [10] -->
applied to both unweighted and weighted networks.

<!-- b000461 | prose | pages [10] -->
The Shapley value is more appropriate than betweenness in the scenario where 

<!-- b000462 | furniture | pages [11] -->


<!-- b000463 | furniture | pages [11] -->
Team # 28199                                                                Page 11 of 21

<!-- b000464 | prose | pages [11] -->
a node has higher betweenness, but the removal of it has less impact on the

<!-- b000465 | prose | pages [11] -->
network’s cohesion.

<!-- b000466 | prose | pages [11] -->
The Shapley value considers the order when calculate the contribution of each 

<!-- b000467 | prose | pages [11] -->
node to the cohesion of the whole network, so the result is more accurate than

<!-- b000468 | prose | pages [11] -->
that of simply subtracting the DFs of the network with and without the node.

<!-- b000469 | heading | pages [11] -->
Weaknesses

<!-- b000470 | prose | pages [11] -->
The calculation of Shapley value is more complex than that of conventional 

<!-- b000471 | prose | pages [11] -->
centrality.

<!-- b000472 | prose | pages [11] -->
The Shapley value can’t be applied to directed networks, since the definition of 

<!-- b000473 | prose | pages [11] -->
the cohesion measurement DF does not reflect the directions of edges. So

<!-- b000474 | prose | pages [11] -->
another method needs to be introduced to measure the influence of nodes in

<!-- b000475 | prose | pages [11] -->
directed networks.

<!-- b000476 | prose | pages [11] -->
Utility

<!-- b000477 | prose | pages [11] -->
The Shapley value is applicable to most undirected networks.

<!-- b000478 | prose | pages [11] -->
Individual level

<!-- b000479 | prose | pages [11] -->
Improve social influence. Real social network is a typical undirected network, 

<!-- b000480 | prose | pages [11] -->
where one can always use the Shapley value to measure others’ impact on the

<!-- b000481 | prose | pages [11] -->
network. And choosing the people with lower Shapley value to make

<!-- b000482 | prose | pages [11] -->
acquaintance with can improve one’s social influence efficiently.

<!-- b000483 | prose | pages [11] -->
Make career decisions. As is illustrated above, cooperation networks like Edros 

<!-- b000484 | prose | pages [11] -->
Network and Movie Star Network are also undirected networks. Cooperating with

<!-- b000485 | prose | pages [11] -->
colleagues with lower Shapley value may boost your career status rapidly.

<!-- b000486 | prose | pages [11] -->
Organizational level

<!-- b000487 | prose | pages [11] -->
Choose business collaborator. Business cooperation network is similar to Edros 

<!-- b000488 | prose | pages [11] -->
Network and Movie Star Network, so the same strategy can be applied in order to

<!-- b000489 | prose | pages [11] -->
boost influence.

<!-- b000490 | prose | pages [11] -->
National level

<!-- b000491 | prose | pages [11] -->
Improve international relationship. Similarly, countries that want to be more active 

<!-- b000492 | prose | pages [11] -->
in international events can choose to establish diplomatic relations with those with

<!-- b000493 | prose | pages [11] -->
lower Shapley value.

<!-- b000494 | furniture | pages [11] -->


<!-- b000495 | prose | pages [11] -->
Influence measure for directed network:

<!-- b000496 | prose | pages [11] -->
Optimized Pagerank

<!-- b000497 | prose | pages [11] -->
The undirected network discussed above will produce a symmetric adjacency

<!-- b000498 | furniture | pages [12] -->


<!-- b000499 | furniture | pages [12] -->
Team # 28199                                                                Page 12 of 21

<!-- b000500 | prose | pages [12] -->
matrix. In contrast, directed networks, such as the web page network and the paper

<!-- b000501 | prose | pages [12] -->
citation network, are useful to study relative asymmetries and imbalances in link

<!-- b000502 | prose | pages [12] -->
formation. To analyze the influence ranking within a directed network, we take the

<!-- b000503 | prose | pages [12] -->
paper citation network as an example to study the methodology called Pagerank. And

<!-- b000504 | prose | pages [12] -->
we use the list of all 16 papers provided by the 2014 ICM problem file as our data. In

<!-- b000505 | prose | pages [12] -->
addition, the Pagerank measurement is optimized to apply to the real citation network

<!-- b000506 | prose | pages [12] -->
better according to the total numbers of the references of a certain paper under

<!-- b000507 | prose | pages [12] -->
consideration and the outside papers citing the target paper.

<!-- b000508 | heading | pages [12] -->
The basic Pagerank model

<!-- b000509 | prose | pages [12] -->
Pagerank is an algorithm originally used to measure the value of a website page

<!-- b000510 | prose | pages [12] -->
according to the number and quality of links to it. Because both of the website network

<!-- b000511 | prose | pages [12] -->
and the citation network can be regarded as directed graphs when papers or webs are

<!-- b000512 | prose | pages [12] -->
nodes and reference relationships or web links are arcs, we can conduct Pagerank

<!-- b000513 | prose | pages [12] -->
method to evaluate the contribution of papers. The main idea of this method is that the

<!-- b000514 | prose | pages [12] -->
relative importance of a certain node in a directed network hinges on the importance

<!-- b000515 | prose | pages [12] -->
of nodes attaching outbound links to it. Specifically, in the citation network, the

<!-- b000516 | prose | pages [12] -->
distribution of a target paper depends on the number and influence of papers citing it.

<!-- b000517 | prose | pages [12] -->
So the Pagerank value of a paper can be calculated as the following equation:

<!-- b000518 | furniture | pages [12] -->


<!-- b000519 | prose | pages [12] -->
PR(𝑝𝑖) = 𝑑∑

<!-- b000520 | prose | pages [12] -->
𝑝𝑗∈Π(𝑝𝑖)

<!-- b000521 | prose | pages [12] -->
PR(𝑝𝑖)

<!-- b000522 | prose | pages [12] -->
1−𝑑 𝑁        (11)

<!-- b000523 | prose | pages [12] -->
+ L(𝑝𝑗)

<!-- b000524 | furniture | pages [12] -->


<!-- b000525 | furniture | pages [12] -->


<!-- b000526 | prose | pages [12] -->
Where 𝑝1, 𝑝2, 𝑝3, … , 𝑝𝑁 present the papers in the network as the subscript means

<!-- b000527 | prose | pages [12] -->
their corresponding number based on the initial order, PR(𝑝𝑖) means the Pagerank

<!-- b000528 | prose | pages [12] -->
value of the target paper 𝑝𝑖 , Π(𝑝𝑖) is the set of papers that have cited 𝑝𝑖 , L(𝑝𝑗) is

<!-- b000529 | prose | pages [12] -->
the number of outbound links from  𝑝𝑗, and N is the total number of the papers in the

<!-- b000530 | prose | pages [12] -->
network, which is 16 in this case .

<!-- b000531 | prose | pages [12] -->
The denominator L(𝑝𝑗) means that every paper distributes equal link weight to

<!-- b000532 | prose | pages [12] -->
each of its reference in the network. And it’s worth noting that there would always be

<!-- b000533 | prose | pages [12] -->
at least one paper that does not cite other papers in the network, such as the paper

<!-- b000534 | prose | pages [12] -->
first published. So here a damping factor 𝑑, is introduced into the model to deal with

<!-- b000535 | prose | pages [12] -->
the papers with no outbound links by assuming every paper to link out to all other

<!-- b000536 | prose | pages [12] -->
papers in the collection evenly with a probability of 1 −𝑑. The empirical value of 𝑑 is

<!-- b000537 | prose | pages [12] -->
0.85, which means a paper’s Pagerank is 0.85/N even no paper links to it.

<!-- b000538 | prose | pages [12] -->
The iterative method

<!-- b000539 | prose | pages [12] -->
According to the definition equation of Pagerank value, we use MATLAB to

<!-- b000540 | furniture | pages [13] -->


<!-- b000541 | furniture | pages [13] -->
Team # 28199                                                                Page 13 of 21

<!-- b000542 | prose | pages [13] -->
operate the algorithm. Again, the adjacency matrix ,𝑊, extracted from the references

<!-- b000543 | prose | pages [13] -->
of each paper with equal link weight is used to describe the relations and links among

<!-- b000544 | prose | pages [13] -->
the total 16 papers, where 𝑟𝑖𝑗= 1 means that 𝑝𝑖 cites 𝑝𝑗.In matrix form, the

<!-- b000545 | prose | pages [13] -->
Pagerank matrix can be manifested by the following equation.

<!-- b000546 | furniture | pages [13] -->


<!-- b000547 | prose | pages [13] -->
PR = 𝑑∗(𝑊∗)′PR + (1 −𝑑) (𝐸∗𝐸′

<!-- b000548 | prose | pages [13] -->
)                   (12) 𝑛

<!-- b000549 | furniture | pages [13] -->


<!-- b000550 | prose | pages [13] -->
Where 𝑊∗ means the modified adjacency matrix after dividing every element by

<!-- b000551 | prose | pages [13] -->
the row sum.

<!-- b000552 | prose | pages [13] -->
Then we use the iterative method to get the most accurate value results under

<!-- b000553 | prose | pages [13] -->
the assumption that the distribution is evenly divided among all papers at the

<!-- b000554 | prose | pages [13] -->
beginning of the computational process. According to the Pagerank value of every

<!-- b000555 | prose | pages [13] -->
element, we can get the most influential paper with the highest Pagerank value (see

<!-- b000556 | prose | pages [13] -->
results in column 2 of Table 5. ).

<!-- b000557 | heading | pages [13] -->
The weakness of the basic model

<!-- b000558 | prose | pages [13] -->
Since the basic Pagerank method is derived from websites rank, such an

<!-- b000559 | prose | pages [13] -->
algorithm has weakness and cannot be simply applied to the paper influence rank due

<!-- b000560 | prose | pages [13] -->
to the following distinguishes between them.

<!-- b000561 | prose | pages [13] -->
Once built, the citation link or network is static while the website links are 

<!-- b000562 | prose | pages [13] -->
dynamically adjustable.

<!-- b000563 | prose | pages [13] -->
The citations must be unidirectional whereas it is generally seen that two web 

<!-- b000564 | prose | pages [13] -->
pages link to each other.

<!-- b000565 | prose | pages [13] -->
The noise of the citation network is much less than the website network. In 

<!-- b000566 | prose | pages [13] -->
general, every citation linked to a certain paper has relevance with it in a sense,

<!-- b000567 | prose | pages [13] -->
but some page links in the website network contains useless information, such as

<!-- b000568 | prose | pages [13] -->
advertisements, site navigations and friendly links.

<!-- b000569 | prose | pages [13] -->
The lack of enough citations makes the Pagerank value meaningless in a small 

<!-- b000570 | prose | pages [13] -->
network.

<!-- b000571 | prose | pages [13] -->
So it is necessary to improve the basic model in order to satisfy the properties of

<!-- b000572 | prose | pages [13] -->
the citation network.

<!-- b000573 | heading | pages [13] -->
The optimized Pagerank model

<!-- b000574 | prose | pages [13] -->
By taking other papers as a whole into account, we consider that other papers

<!-- b000575 | prose | pages [13] -->
outside the network can also influence the contribution of the target paper. To

<!-- b000576 | prose | pages [13] -->
optimize the Pagerank method, we assume that there is a virtual N+1 node, which

<!-- b000577 | prose | pages [13] -->
presents all of the other papers beyond the 16 papers (see Figure 5). These papers

<!-- b000578 | furniture | pages [14] -->


<!-- b000579 | furniture | pages [14] -->
Team # 28199                                                                Page 14 of 21

<!-- b000580 | prose | pages [14] -->
may also cite or be cited by the target paper.

<!-- b000581 | furniture | pages [14] -->


<!-- b000582 | furniture | pages [14] -->


<!-- b000583 | caption | pages [14] -->
Figure 5. Extensive citation network. The size of a node corresponds to the all degree

<!-- b000584 | prose | pages [14] -->
(in and out) of a paper. Arrows mean one paper cites another. Imaginary line

<!-- b000585 | prose | pages [14] -->
separates the initial citation network and the outside virtual node.

<!-- b000586 | furniture | pages [14] -->


<!-- b000587 | prose | pages [14] -->
After adding the virtual node, we get a new modified adjacency matrix(N+1×N+1)

<!-- b000588 | prose | pages [14] -->
of the extensive citation network.

<!-- b000589 | furniture | pages [14] -->


<!-- b000590 | prose | pages [14] -->


<!-- b000591 | prose | pages [14] -->
r r r

<!-- b000592 | prose | pages [14] -->
11 12 1

<!-- b000593 | prose | pages [14] -->


<!-- b000594 | prose | pages [14] -->
r r r

<!-- b000595 | prose | pages [14] -->


<!-- b000596 | prose | pages [14] -->
21 22 2

<!-- b000597 | prose | pages [14] -->
 

<!-- b000598 | prose | pages [14] -->
r r r

<!-- b000599 | prose | pages [14] -->


<!-- b000600 | prose | pages [14] -->
i

<!-- b000601 | prose | pages [14] -->
1

<!-- b000602 | prose | pages [14] -->
i

<!-- b000603 | prose | pages [14] -->
2

<!-- b000604 | prose | pages [14] -->
ij

<!-- b000605 | prose | pages [14] -->
 

<!-- b000606 | prose | pages [14] -->
r r r

<!-- b000607 | prose | pages [14] -->


<!-- b000608 | prose | pages [14] -->
N

<!-- b000609 | prose | pages [14] -->
1

<!-- b000610 | prose | pages [14] -->
N

<!-- b000611 | prose | pages [14] -->
2

<!-- b000612 | prose | pages [14] -->
Nj

<!-- b000613 | prose | pages [14] -->


<!-- b000614 | prose | pages [14] -->
r r r

<!-- b000615 | prose | pages [14] -->


<!-- b000616 | prose | pages [14] -->
  

<!-- b000617 | prose | pages [14] -->
(

<!-- b000618 | prose | pages [14] -->
N

<!-- b000619 | prose | pages [14] -->
1)1 (

<!-- b000620 | prose | pages [14] -->
N

<!-- b000621 | prose | pages [14] -->
1)2 (

<!-- b000622 | prose | pages [14] -->
N

<!-- b000623 | prose | pages [14] -->
Where

<!-- b000624 | prose | pages [14] -->
⁄

<!-- b000625 | prose | pages [14] -->


<!-- b000626 | prose | pages [14] -->
r r

<!-- b000627 | prose | pages [14] -->


<!-- b000628 | prose | pages [14] -->
j j

<!-- b000629 | prose | pages [14] -->
1

<!-- b000630 | prose | pages [14] -->
N

<!-- b000631 | prose | pages [14] -->
1(

<!-- b000632 | prose | pages [14] -->
N

<!-- b000633 | prose | pages [14] -->
1)

<!-- b000634 | prose | pages [14] -->


<!-- b000635 | prose | pages [14] -->
r r

<!-- b000636 | prose | pages [14] -->


<!-- b000637 | prose | pages [14] -->


<!-- b000638 | prose | pages [14] -->
j j

<!-- b000639 | prose | pages [14] -->
2

<!-- b000640 | prose | pages [14] -->
N

<!-- b000641 | prose | pages [14] -->
2(

<!-- b000642 | prose | pages [14] -->
N

<!-- b000643 | prose | pages [14] -->
1)

<!-- b000644 | prose | pages [14] -->
 

<!-- b000645 | prose | pages [14] -->
r r

<!-- b000646 | prose | pages [14] -->


<!-- b000647 | prose | pages [14] -->


<!-- b000648 | prose | pages [14] -->
iN i N

<!-- b000649 | prose | pages [14] -->
( 1)

<!-- b000650 | prose | pages [14] -->
 

<!-- b000651 | prose | pages [14] -->
r r

<!-- b000652 | prose | pages [14] -->


<!-- b000653 | prose | pages [14] -->


<!-- b000654 | prose | pages [14] -->
NN N N

<!-- b000655 | prose | pages [14] -->
( 1)

<!-- b000656 | prose | pages [14] -->


<!-- b000657 | prose | pages [14] -->
r r

<!-- b000658 | prose | pages [14] -->


<!-- b000659 | prose | pages [14] -->
  

<!-- b000660 | prose | pages [14] -->
1) 1)

<!-- b000661 | prose | pages [14] -->
j j

<!-- b000662 | prose | pages [14] -->
(

<!-- b000663 | prose | pages [14] -->
N

<!-- b000664 | prose | pages [14] -->
1)

<!-- b000665 | prose | pages [14] -->
N

<!-- b000666 | prose | pages [14] -->
(

<!-- b000667 | prose | pages [14] -->
N

<!-- b000668 | prose | pages [14] -->
1)(

<!-- b000669 | prose | pages [14] -->
N

<!-- b000670 | prose | pages [14] -->
1)

<!-- b000671 | furniture | pages [14] -->


<!-- b000672 | furniture | pages [14] -->


<!-- b000673 | prose | pages [14] -->
, when 𝑝𝑖cites  𝑝𝑗 and C is the number of all reference papers of 𝑝𝑖 𝑟𝑖𝑗= {1 𝐶

<!-- b000674 | furniture | pages [14] -->


<!-- b000675 | prose | pages [14] -->
0, when 𝑝𝑖 does not cite 𝑝𝑗

<!-- b000676 | furniture | pages [14] -->


<!-- b000677 | prose | pages [14] -->
𝑁

<!-- b000678 | furniture | pages [14] -->


<!-- b000679 | prose | pages [14] -->
𝑟𝑖(𝑁+1) = 1 −∑𝑟𝑖𝑗

<!-- b000680 | furniture | pages [14] -->


<!-- b000681 | prose | pages [14] -->
𝑗=1

<!-- b000682 | prose | pages [14] -->
⁄ 𝑟(𝑁=1)𝑗= 1 𝑁

<!-- b000683 | furniture | pages [14] -->


<!-- b000684 | furniture | pages [14] -->


<!-- b000685 | furniture | pages [15] -->


<!-- b000686 | furniture | pages [15] -->
Team # 28199                                                                Page 15 of 21

<!-- b000687 | prose | pages [15] -->
𝑟(𝑁+1)(𝑁+1) = 0

<!-- b000688 | furniture | pages [15] -->


<!-- b000689 | prose | pages [15] -->
As the improved matrix shows, every reference paper in the original network get

<!-- b000690 | prose | pages [15] -->
equal citation link weight from the source paper while the new N+1 node(the other

<!-- b000691 | prose | pages [15] -->
related papers) get the rest of the reference weight. Also, the N+1 node distribute its

<!-- b000692 | prose | pages [15] -->
link weight to N papers evenly. By this way, we consider the whole list of references

<!-- b000693 | prose | pages [15] -->
instead of the limited 16 objects in the network and adjust the weight allocated to the

<!-- b000694 | prose | pages [15] -->
cited paper according to the total number of the references. Similarly, we can use the

<!-- b000695 | prose | pages [15] -->
iterative method to calculate the Pagerank value results (see column 3 of Table X)in

<!-- b000696 | prose | pages [15] -->
the optimized model.

<!-- b000697 | prose | pages [15] -->
Involving Times Cited

<!-- b000698 | prose | pages [15] -->
The model discussed above assumes that the outside papers attach equal

<!-- b000699 | prose | pages [15] -->
weight to the paper in the network as the element of the N+1 row is the same.

<!-- b000700 | prose | pages [15] -->
Furthermore, we think that outside papers endows the inside papers with different

<!-- b000701 | prose | pages [15] -->
weight on the basis of the target paper’s Times Cited since its publication. So the

<!-- b000702 | prose | pages [15] -->
elements of last row are changed into:

<!-- b000703 | furniture | pages [15] -->


<!-- b000704 | prose | pages [15] -->
𝑁 𝑟(𝑁+1)𝑗= 𝑇𝑗∑ (13) ⁄ ⁄ 𝑇𝑗 𝑗=1

<!-- b000705 | furniture | pages [15] -->


<!-- b000706 | furniture | pages [15] -->


<!-- b000707 | prose | pages [15] -->
Where 𝑇𝑗 is the Times Cited data of 𝑝𝑗 from Google Scholar.

<!-- b000708 | prose | pages [15] -->
After considering the real Times Cited, the third method involves both the papers

<!-- b000709 | prose | pages [15] -->
having outbound links and inbound links to the initial network and can reflex the real

<!-- b000710 | prose | pages [15] -->
integrated impact of the target paper. And the new outcome can be seen in the

<!-- b000711 | prose | pages [15] -->
column 4 of Table 5.

<!-- b000712 | heading | pages [15] -->
Results

<!-- b000713 | prose | pages [15] -->
We can get three groups of results from the basic model, optimized model and

<!-- b000714 | prose | pages [15] -->
further optimized model (involving Times Cited) respectively. In addition, we select the

<!-- b000715 | prose | pages [15] -->
top 5 from 16 papers in accordance with their Pagerank values to compare the

<!-- b000716 | prose | pages [15] -->
effectiveness of these three methods in the Pagerank model. The importance ranking

<!-- b000717 | prose | pages [15] -->
results can be seen in Table 5, where the value under the paper number is its

<!-- b000718 | prose | pages [15] -->
Pagerank value.

<!-- b000719 | furniture | pages [15] -->


<!-- b000720 | furniture | pages [15] -->


<!-- b000721 | furniture | pages [15] -->


<!-- b000722 | furniture | pages [15] -->


<!-- b000723 | furniture | pages [16] -->


<!-- b000724 | furniture | pages [16] -->
Team # 28199                                                                Page 16 of 21

<!-- b000725 | caption | pages [16] -->
Table 5. Pagerank results of three methods in the Pagerank model

<!-- b000726 | prose | pages [16] -->
Basic Pagerank Model Optimized Pagerank Model

<!-- b000727 | furniture | pages [16] -->


<!-- b000728 | prose | pages [16] -->
Rank

<!-- b000729 | prose | pages [16] -->
Paper number

<!-- b000730 | prose | pages [16] -->
1 14

<!-- b000731 | prose | pages [16] -->
(0.7681)

<!-- b000732 | prose | pages [16] -->
2 3

<!-- b000733 | prose | pages [16] -->
(0.3846)

<!-- b000734 | prose | pages [16] -->
3 4

<!-- b000735 | prose | pages [16] -->
(0.2309)

<!-- b000736 | prose | pages [16] -->
4 6

<!-- b000737 | prose | pages [16] -->
(0.1515)

<!-- b000738 | prose | pages [16] -->
5 8

<!-- b000739 | prose | pages [16] -->
(0.1104)

<!-- b000740 | furniture | pages [16] -->


<!-- b000741 | prose | pages [16] -->
No Times Cited With Times Cited

<!-- b000742 | prose | pages [16] -->
Paper number Paper number

<!-- b000743 | prose | pages [16] -->
14

<!-- b000744 | prose | pages [16] -->
14

<!-- b000745 | prose | pages [16] -->
(0.3339)

<!-- b000746 | prose | pages [16] -->
(1.0312)

<!-- b000747 | prose | pages [16] -->
4 4

<!-- b000748 | prose | pages [16] -->
4

<!-- b000749 | prose | pages [16] -->
(0.295)

<!-- b000750 | prose | pages [16] -->
(0.8562)

<!-- b000751 | prose | pages [16] -->
6 6

<!-- b000752 | prose | pages [16] -->
2

<!-- b000753 | prose | pages [16] -->
(0.2871)

<!-- b000754 | prose | pages [16] -->
(0.6146)

<!-- b000755 | prose | pages [16] -->
8 8

<!-- b000756 | prose | pages [16] -->
11

<!-- b000757 | prose | pages [16] -->
(0.2842)

<!-- b000758 | prose | pages [16] -->
(0.5071)

<!-- b000759 | prose | pages [16] -->
3 3

<!-- b000760 | prose | pages [16] -->
1

<!-- b000761 | prose | pages [16] -->
(0.2806)

<!-- b000762 | prose | pages [16] -->
(0.2618)

<!-- b000763 | prose | pages [16] -->
As shown in table above, the most important paper remains the same under the

<!-- b000764 | prose | pages [16] -->
three methods which is No.14, Collective dynamics of `small-world' networks. It is

<!-- b000765 | prose | pages [16] -->
because No.14 is always contributing most and cited by other important papers more

<!-- b000766 | prose | pages [16] -->
frequently (its Times Cited on Google Scholar is 21688) no matter in the network with

<!-- b000767 | prose | pages [16] -->
limited size or that involving other papers.

<!-- b000768 | prose | pages [16] -->
Additionally, the papers which rank 2nd to 5th are changed after the model is

<!-- b000769 | prose | pages [16] -->
optimized. Specifically, the ranking of No.4 is elevated from 3rd to 2nd after extending

<!-- b000770 | prose | pages [16] -->
the network to outside papers because No.4 gets larger link weight relatively. Another

<!-- b000771 | prose | pages [16] -->
obvious change is that No.3 is absent from the Top list mainly since its Times Cited

<!-- b000772 | prose | pages [16] -->
(1956) is relatively small. On the contrary, No.2 and No.11 appear on the Top list of

<!-- b000773 | prose | pages [16] -->
optimized Pagerank Model with Times Cited due to their large Times Cited (13250

<!-- b000774 | prose | pages [16] -->
and 10616 respectively).

<!-- b000775 | prose | pages [16] -->
According to the results, the optimized Pagerank method is not confined to the

<!-- b000776 | prose | pages [16] -->
target papers and can be better applied to distinguish the most important paper from

<!-- b000777 | prose | pages [16] -->
others by evaluating synthetically the Pagerank values of papers within an extensive

<!-- b000778 | prose | pages [16] -->
network that considers both outbound and inbound links.

<!-- b000779 | heading | pages [16] -->
Strengths

<!-- b000780 | prose | pages [16] -->
High practicability. The Pagerank model is suitable to analyze the importance 

<!-- b000781 | prose | pages [16] -->
ranking in the complex network, especially in directed graphs cause it can

<!-- b000782 | prose | pages [16] -->
distinguish outbound links from inbound links.

<!-- b000783 | furniture | pages [17] -->


<!-- b000784 | furniture | pages [17] -->
Team # 28199                                                                Page 17 of 21

<!-- b000785 | prose | pages [17] -->
Optimized model. By involving outside citation links into the initial network, the 

<!-- b000786 | prose | pages [17] -->
optimized Pagerank model can break through the size limit of the citation network

<!-- b000787 | prose | pages [17] -->
so as to evaluate the integrated influence of a paper.

<!-- b000788 | prose | pages [17] -->
Wide application. The model can be applied universally to the entity importance 

<!-- b000789 | prose | pages [17] -->
ranking, such as the key words, scientific institutions and countries, as well as the

<!-- b000790 | prose | pages [17] -->
websites, papers and journals.

<!-- b000791 | heading | pages [17] -->
Weaknesses

<!-- b000792 | prose | pages [17] -->
Data limitations. The effective practice of the Pagerank model needs a large deal 

<!-- b000793 | prose | pages [17] -->
of information about the reference relationship or the accuracy of the influence

<!-- b000794 | prose | pages [17] -->
results changes along with the different network size and data abundance.

<!-- b000795 | prose | pages [17] -->
Improved application. Using Pagerank to assess papers or institutions is a new 

<!-- b000796 | prose | pages [17] -->
field, so it still remains several problems of applications, such as the dynamic

<!-- b000797 | prose | pages [17] -->
noise of the network, and needs further practice to improve the application

<!-- b000798 | prose | pages [17] -->
methods.

<!-- b000799 | prose | pages [17] -->
Utility

<!-- b000800 | prose | pages [17] -->
Our optimized Pagerank model is applicable to many networks especially

<!-- b000801 | prose | pages [17] -->
directed networks.

<!-- b000802 | prose | pages [17] -->
Individual level:

<!-- b000803 | prose | pages [17] -->
Choose the one to follow on social network society. Social relationships on the 

<!-- b000804 | prose | pages [17] -->
internet can be considered as a directed network because the links can be

<!-- b000805 | prose | pages [17] -->
one-way. For example, if you follow a friend on twitter while this friend does not

<!-- b000806 | prose | pages [17] -->
follow you in return, then there is a link from you to your friend, but the reversed

<!-- b000807 | prose | pages [17] -->
link does not exist. In order to get as much information as possible in a field in a

<!-- b000808 | prose | pages [17] -->
short time, we can build a network to figure out those who have the highest

<!-- b000809 | prose | pages [17] -->
Pagerank values and those who play the most important roles in this network.

<!-- b000810 | prose | pages [17] -->
Make academic decisions. With the data of citation relationships among papers 

<!-- b000811 | prose | pages [17] -->
written by different thesis advisors, we can figure out the Pagerank value of each

<!-- b000812 | prose | pages [17] -->
thesis advisor. Thesis advisors with higher Pagerank values are likely to have

<!-- b000813 | prose | pages [17] -->
stronger scientific research ability. In a similar way, by studying the papers written

<!-- b000814 | prose | pages [17] -->
by all the teachers and students at the school, we can choose a satisfying school

<!-- b000815 | prose | pages [17] -->
to go to.

<!-- b000816 | prose | pages [17] -->
National level:

<!-- b000817 | prose | pages [17] -->
Control systemic risk. Interbank borrowing market is a typical directed network 

<!-- b000818 | prose | pages [17] -->
which represents the debtor-creditor relationships between different financial

<!-- b000819 | prose | pages [17] -->
institutions. Financial institutions with high Pagerank value are too interconnected

<!-- b000820 | furniture | pages [18] -->


<!-- b000821 | furniture | pages [18] -->
Team # 28199                                                                Page 18 of 21

<!-- b000822 | prose | pages [18] -->
to fail because they play important roles in financial contagion and have a great

<!-- b000823 | prose | pages [18] -->
influence on other institutions. According to the Pagerank model, the supervisor is

<!-- b000824 | prose | pages [18] -->
supposed to pay special attention to these financial institutions to control the

<!-- b000825 | prose | pages [18] -->
systemic risk of the whole country.

<!-- b000826 | heading | pages [18] -->
Sensitivity analysis

<!-- b000827 | heading | pages [18] -->
Shapley value’s sensitivity to parameter k

<!-- b000828 | prose | pages [18] -->
One fatal flaw of the Shapley value is the huge computation. Although the

<!-- b000829 | prose | pages [18] -->
complexity has been mitigated from Equation (8) to (9) by replacing the total number

<!-- b000830 | prose | pages [18] -->
of permutations N! with the sample size of k, it still needs a lot of time and memory

<!-- b000831 | prose | pages [18] -->
space to run the program. So we explore the sensitivity of the results to the sample

<!-- b000832 | prose | pages [18] -->
size k by tracing 5 co-authors’ rank under different k, as is shown in Figure 6.

<!-- b000833 | prose | pages [18] -->
70

<!-- b000834 | prose | pages [18] -->
60

<!-- b000835 | prose | pages [18] -->
50

<!-- b000836 | prose | pages [18] -->
40

<!-- b000837 | prose | pages [18] -->
Rank

<!-- b000838 | prose | pages [18] -->
30

<!-- b000839 | prose | pages [18] -->
20

<!-- b000840 | prose | pages [18] -->
10

<!-- b000841 | prose | pages [18] -->
0

<!-- b000842 | prose | pages [18] -->
100 120 140 160 180 200 220 240 260 280 300 320 340 360 380 400 420 440 460 480 500

<!-- b000843 | prose | pages [18] -->
parameter k

<!-- b000844 | prose | pages [18] -->
ALON, NOGA M.

<!-- b000845 | prose | pages [18] -->
GYARFAS, ANDRAS SOS, VERA TURAN KLEITMAN, DANIEL J. TUZA, ZSOLT

<!-- b000846 | furniture | pages [18] -->


<!-- b000847 | caption | pages [18] -->
Figure 6. Sensitivity analysis results of Shapley value to parameter k. The 5 different

<!-- b000848 | prose | pages [18] -->
lines present 5 sets of ranks of 5 co-authors.

<!-- b000849 | furniture | pages [18] -->


<!-- b000850 | prose | pages [18] -->
As is shown above, the co-authors’ ranks differ remarkably under different value

<!-- b000851 | prose | pages [18] -->
of parameter k. And ranks tend to be stable with the increase of sample size k, which

<!-- b000852 | prose | pages [18] -->
is consistent with the basic principle of statistics. So we suggest selecting k that are

<!-- b000853 | prose | pages [18] -->
large enough to guarantee the accuracy of the results, but not too large to save time

<!-- b000854 | prose | pages [18] -->
and space. In this case, a figure over 400 can provide reasonable accuracy.

<!-- b000855 | heading | pages [18] -->
Pagerank value’s sensitivity to parameter d

<!-- b000856 | furniture | pages [19] -->


<!-- b000857 | furniture | pages [19] -->
Team # 28199                                                                Page 19 of 21

<!-- b000858 | prose | pages [19] -->
Considering the principle and computational process of Pagerank algorithm, it is

<!-- b000859 | prose | pages [19] -->
easy to find that the results of this methodology may be influenced by the damping

<!-- b000860 | prose | pages [19] -->
factor 𝑑 which is an empirical constant 0.85 in the model above. Since the parameter

<!-- b000861 | prose | pages [19] -->
𝑑 can change the probability of directing to a random node in the network, we can

<!-- b000862 | prose | pages [19] -->
conduct the sensitivity analysis of Pagerank value rank to parameter 𝑑. Here we use

<!-- b000863 | prose | pages [19] -->
the optimized Pagerank method with Times Cited .By changing the value of 𝑑 from

<!-- b000864 | prose | pages [19] -->
0.05 to 1 with the interval of 0.05, we observe the corresponding ranks of the original

<!-- b000865 | prose | pages [19] -->
Top 5 papers (in the column 4 of Table 5). The outcome of sensitivity analysis can be

<!-- b000866 | prose | pages [19] -->
seen in Figure 7.

<!-- b000867 | prose | pages [19] -->
6

<!-- b000868 | prose | pages [19] -->
5

<!-- b000869 | prose | pages [19] -->
4

<!-- b000870 | prose | pages [19] -->
Rank

<!-- b000871 | prose | pages [19] -->
3

<!-- b000872 | prose | pages [19] -->
2

<!-- b000873 | prose | pages [19] -->
1

<!-- b000874 | prose | pages [19] -->
0

<!-- b000875 | prose | pages [19] -->
0.05 0.15 0.25 0.35 0.45 0.55 0.1 0.2 0.3 0.4 0.5

<!-- b000876 | prose | pages [19] -->
No.14

<!-- b000877 | prose | pages [19] -->
No.4

<!-- b000878 | prose | pages [19] -->
No.2

<!-- b000879 | prose | pages [19] -->
No.11

<!-- b000880 | prose | pages [19] -->
No.1

<!-- b000881 | prose | pages [19] -->
0.65 0.75 0.85 0.95 1 0.6 0.7 0.8 0.9

<!-- b000882 | prose | pages [19] -->
Parameter d

<!-- b000883 | furniture | pages [19] -->


<!-- b000884 | caption | pages [19] -->
Figure 7. Sensitivity analysis results of Pagerank values to parameter𝑑. The 5

<!-- b000885 | prose | pages [19] -->
different lines present 5 sets of ranks of the 5 certain paper.

<!-- b000886 | furniture | pages [19] -->


<!-- b000887 | prose | pages [19] -->
Obviously, the results reveal that the rank of each paper is not changing along

<!-- b000888 | prose | pages [19] -->
with the change of parameter 𝑑, which means that the Pagerank method result is not

<!-- b000889 | prose | pages [19] -->
sensitive to 𝑑.Although 𝑑 can change the probability of random links, its action

<!-- b000890 | prose | pages [19] -->
principle is to add a constant weight to every element in the network to avoid the

<!-- b000891 | prose | pages [19] -->
misconvergence of Pagerank value but does not change the original importance of a

<!-- b000892 | prose | pages [19] -->
certain paper and the link weight distribution. As a result, the parameter 𝑑 has

<!-- b000893 | prose | pages [19] -->
nothing to do with the Pagerank value.

<!-- b000894 | furniture | pages [19] -->


<!-- b000895 | furniture | pages [19] -->


<!-- b000896 | furniture | pages [19] -->


<!-- b000897 | furniture | pages [19] -->


<!-- b000898 | furniture | pages [20] -->


<!-- b000899 | furniture | pages [20] -->
Team # 28199                                                                Page 20 of 21

<!-- b000900 | prose | pages [20] -->
Reference

<!-- b000901 | prose | pages [20] -->
Albert,R. and Barabasi,A-L.(2002).Statistical machanics of complex networks.

<!-- b000902 | prose | pages [20] -->
Reviews of modern Physics,74:47-97.

<!-- b000903 | prose | pages [20] -->
Markose, S., Giansante, S., Gatkowski, M. and Shaghaghi, A. R.(2009).Too

<!-- b000904 | prose | pages [20] -->
interconnected to fail: Financial contagion and systemic risk in network model of cds

<!-- b000905 | prose | pages [20] -->
and other credit enhancement obligations of us banks. analysis.

<!-- b000906 | prose | pages [20] -->
Freeman L C.(1979).Centrality in social networks conceptual clarification[J]. Social

<!-- b000907 | prose | pages [20] -->
networks, 1(3): 215-239.

<!-- b000908 | prose | pages [20] -->
Borgatti, S. (2006).Identifying sets of key players in a network. Computational and

<!-- b000909 | prose | pages [20] -->
Mathematical Organization Theory, 12: 21-34.

<!-- b000910 | prose | pages [20] -->
Shapley L S.(1952).A value for n-person games[R]. RAND CORP SANTA MONICA

<!-- b000911 | prose | pages [20] -->
CA.

<!-- b000912 | prose | pages [20] -->
Bluhm M, Faia E, Krahnen J P. (2013).Endogenous Banks’ Networks, Cascades and

<!-- b000913 | prose | pages [20] -->
Systemic Risk[R]. Mimeo, Goethe University.

<!-- b000914 | prose | pages [20] -->
Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of ‘small-world’networks.

<!-- b000915 | prose | pages [20] -->
nature, 393(6684), 440-442.

<!-- b000916 | prose | pages [20] -->
Borgatti, S. P., Jones, C., & Everett, M. G. (1998). Network measures of social capital.

<!-- b000917 | prose | pages [20] -->
Connections, 21(2), 27-36.

<!-- b000918 | prose | pages [20] -->
Newman, M. E. (2001). The structure of scientific collaboration networks. Proceedings

<!-- b000919 | prose | pages [20] -->
of the National Academy of Sciences, 98(2), 404-409.

<!-- b000920 | prose | pages [20] -->
Friedkin, N. E. (1991). Theoretical foundations for centrality measures. American

<!-- b000921 | prose | pages [20] -->
journal of Sociology, 1478-1504.

<!-- b000922 | prose | pages [20] -->
Knoke, D., & Yang, S. (2008). Social network analysis (Vol. 154). Sage.

<!-- b000923 | prose | pages [20] -->
Watts, D. J. (1999). Small worlds: the dynamics of networks between order and

<!-- b000924 | prose | pages [20] -->
randomness. Princeton university press.

<!-- b000925 | prose | pages [20] -->
Moody, J., & White, D. R. (2003). Structural cohesion and embeddedness: A

<!-- b000926 | prose | pages [20] -->
hierarchical concept of social groups. American Sociological Review, 103-127.

<!-- b000927 | prose | pages [20] -->
Kleinberg, J. M. (2000). Navigation in a small world. Nature, 406(6798), 845-845.

<!-- b000928 | prose | pages [20] -->
Everett, M. G., & Borgatti, S. P. (2000). Peripheries of cohesive subsets. Social

<!-- b000929 | prose | pages [20] -->
Networks, 21(4), 397-407.

<!-- b000930 | prose | pages [20] -->
Borgatti, S. P., & Everett, M. G. (2000). Models of core/periphery structures. Social

<!-- b000931 | prose | pages [20] -->
networks, 21(4), 375-395.

<!-- b000932 | prose | pages [20] -->
Glover, F. (1986). Future paths for integer programming and links to artificial

<!-- b000933 | prose | pages [20] -->
intelligence. Computers & Operations Research, 13(5), 533-549.

<!-- b000934 | prose | pages [20] -->
Seidman, S. B. (1983). Network structure and minimum degree. Social networks, 5(3),

<!-- b000935 | furniture | pages [21] -->


<!-- b000936 | furniture | pages [21] -->
Team # 28199                                                                Page 21 of 21

<!-- b000937 | prose | pages [21] -->
269-287.

<!-- b000938 | prose | pages [21] -->
http://baike.baidu.com/link?url=WckfiBvPGGGMxZd5DISq5UKMIcfibz2Nn-HwEOym

<!-- b000939 | prose | pages [21] -->
TU0QbYQf2hmZy17u4oa9_Kz2ZquoU91EHOIjlq6T8DL-va

<!-- b000940 | prose | pages [21] -->
http://baike.baidu.com/link?url=aOCz9onz7l-zRZrgHOqsCHpjgd_A2Q_Wvz55QJ8mX

<!-- b000941 | prose | pages [21] -->
uT1znQ54NPTdCHFxoIVTAfpFlyk4dv2ryrKI3eSsitu1K

<!-- b000942 | prose | pages [21] -->
http://en.wikipedia.org/wiki/Complex_network

<!-- b000943 | furniture | pages [21] -->


<!-- b000944 | furniture | pages [21] -->

