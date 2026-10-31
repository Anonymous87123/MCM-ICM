# P-C-2012-12218-14ded715

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
12218

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
T1 ________________

<!-- b000005 | prose | pages [1] -->
T2 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T3 ________________

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
F1 ________________

<!-- b000010 | prose | pages [1] -->
F2 ________________

<!-- b000011 | prose | pages [1] -->
F3 ________________

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T4 ________________

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | title | pages [1] -->
C

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | heading | pages [1] -->
2012 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000021 | prose | pages [1] -->
Type a summary of your results on this page. Do not include

<!-- b000022 | prose | pages [1] -->
the name of your school, advisor, or team members on this page.

<!-- b000023 | prose | pages [1] -->
Social Network Analysis in Crime Busting

<!-- b000024 | prose | pages [1] -->
Social network analysis (SNA) has been winning more and more attention in the last twenty years. The method provides an insight into various networks. In this paper, we use SNA and related techniques to analyze crime data and try to get potential criminal gang.

<!-- b000025 | prose | pages [1] -->
After first investigating the hidden features of a conspiratorial group, we consider one’s closeness to the criminal gang as the main reason in deciding whether a staff member should be

<!-- b000026 | heading | pages [1] -->
regarded as a conspirator. The introduction of cooperation distance metric (CD-metric) combined

<!-- b000027 | prose | pages [1] -->
with the analysis on cooperation factor makes up our model’s major base. Within these definitions, potential conspirators can be worked out by choosing those on the top of the ascending CD-metric list. Highest values of CD-metric can be recognized as being the farthest away from the conspiracy, in other words, they are the most innocent ones. A 12 members’ criminal group is dug out.

<!-- b000028 | prose | pages [1] -->
Before identifying the leading criminals, it is essential for us to quantify the ability of people’s leadership. Centrality analysis suggests a good way in determining the focal point(s) in a network. We make some amendments of the centrality measures so that it can be applied to a directed graph. What’s more, we combine centrality measures(degree, closeness and betweenness) and figure out the fusion values. We can form a ranking list of people’s ability of leadership then. The leaders in the criminal group are sure to come to surface after comparing with the priority list derived before.

<!-- b000029 | prose | pages [1] -->
In the refinement of the network model, we appeal to the theories of semantic network analysis and text analysis. On the purpose of making a deeper exploration of identifying the intrinsic character of one topic, we reapply the centrality analysis to data computing right after the construction of a semantic web. Based on text analysis approach, we build up a vector space model and compare the final outputs with ones obtained above, the results are robust.

<!-- b000030 | prose | pages [1] -->
This model’s application in other areas such as the biomedical domain has been discussed at the end of this paper, excellent performance happens when accessed to enough amounts of data. With a well-organized structure and a wide range of application, this methodology is sure to have a bright future.

<!-- b000031 | keywords | pages [1] -->
Keywords: Social Network Analysis, Centrality Measures, Semantic Web, Text Analysis

<!-- b000032 | furniture | pages [2] -->
Team # 12218

<!-- b000033 | heading | pages [2] -->
Contents

<!-- b000034 | contents | pages [2] -->
1

<!-- b000035 | heading | pages [2] -->
Introduction

<!-- b000036 | furniture | pages [2] -->
Page 1 of 18

<!-- b000037 | prose | pages [2] -->
2

<!-- b000038 | heading | pages [2] -->
Investigation Scenario Based on Crime Data Mining Model

<!-- b000039 | prose | pages [2] -->
2 2 General Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 2 Deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 3 Explanation of the Model . . . . . . . . . . . . . . . . . . . . . . 2.3 3 Tests and Veriﬁcations . . . . . . . . . . . . . . . . . . . . . . . . 2.4

<!-- b000040 | prose | pages [2] -->
3 Analysis on the Current Case

<!-- b000041 | prose | pages [2] -->
4

<!-- b000042 | prose | pages [2] -->
6 Priority Lists of Potential Conspirators . . . . . . . . . . . . . . . 3.1 6 Performance with More Accurate Information . . . . . . . . . . . 3.2

<!-- b000043 | prose | pages [2] -->
4 Searching for Leaders

<!-- b000044 | prose | pages [2] -->
7

<!-- b000045 | prose | pages [2] -->
7 Centrality Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 8 Interpretation of Results . . . . . . . . . . . . . . . . . . . . . . . 4.2

<!-- b000046 | prose | pages [2] -->
5

<!-- b000047 | heading | pages [2] -->
Model Optimizing

<!-- b000048 | prose | pages [2] -->
10

<!-- b000049 | prose | pages [2] -->
11 Semantic Network Analysis . . . . . . . . . . . . . . . . . . . . . 5.1 11 Construction of Semantic Network . . . . . . . . . . . . . 5.1.1 12 Topic Selection . . . . . . . . . . . . . . . . . . . . . . . . 5.1.2 12 Text Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 5.2.1 Vector Space Model 13 . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | prose | pages [2] -->
13 Corroboration of Model Reasonableness . . . . . . . . . . 5.2.4

<!-- b000051 | prose | pages [2] -->
6 Applications

<!-- b000052 | prose | pages [2] -->
7

<!-- b000053 | heading | pages [2] -->
Conclusion

<!-- b000054 | prose | pages [2] -->
14

<!-- b000055 | prose | pages [2] -->
15

<!-- b000056 | prose | pages [2] -->
15

<!-- b000057 | prose | pages [2] -->
1 1

<!-- b000058 | furniture | pages [3] -->
Team # 12218

<!-- b000059 | furniture | pages [3] -->
Page 2 of 18

<!-- b000060 | prose | pages [3] -->
1

<!-- b000061 | heading | pages [3] -->
Introduction

<!-- b000062 | prose | pages [3] -->
A crime is consist of a wide range of activities ranging from traﬃc violations to organized fraud in ﬁnancial ﬁeld. The major challenge lying ahead of all the authorities is how to accurately and eﬃciently analyze tremendous amount of the crime data [1].

<!-- b000063 | prose | pages [3] -->
With great advance in the information technology, the ﬁnancial crime hap- pens more often than ever. Due to a German report published not long before, the identiﬁed fraud cases related to card payments have risen 345% just from 2007 to 2009 [2]. A common analytical approach to this issue during recen- t years is called “Social Network Analysis”(SNA), which can be viewed as an innovation on mathematical perspective combined with sociology and crimi- nology.

<!-- b000064 | prose | pages [3] -->
This method can expose the hidden structural patterns in criminal networks [3], which can be oﬀered to the anti-crime departments in directing them to necessary surveillance or interrogation scenarios, after several steps of data processing.

<!-- b000065 | prose | pages [3] -->
According to Mena’s book, SNA is a data mining technique that reveals the structure and content of a body of information by representing it as a set of interconnected, linked objects or entities [4].

<!-- b000066 | prose | pages [3] -->
To further present the application of the SNA approach, we arrange paper as followed:

<!-- b000067 | prose | pages [3] -->
i. In section 2, we propose a way to construct a model in identifying potential

<!-- b000068 | prose | pages [3] -->
conspirators with the help from SNA in the ﬁrst place;

<!-- b000069 | prose | pages [3] -->
ii. In section 3, veriﬁed by the results of in small network, our model is applied

<!-- b000070 | prose | pages [3] -->
to a bigger one and we rank all the people according to their possibility of being involved in the conspiracy;

<!-- b000071 | prose | pages [3] -->
iii. In section 4, based on the centrality analysis theory, we explore a way in

<!-- b000072 | prose | pages [3] -->
determining all the criminal leaders;

<!-- b000073 | prose | pages [3] -->
iv. In section 5, after referring to the powerful techniques–semantic network

<!-- b000074 | prose | pages [3] -->
analysis and text analysis, we make some amendments of our model by considering the content and context of the message traﬃc;

<!-- b000075 | prose | pages [3] -->
v. At last, we discuss the model’s further developments when provided with

<!-- b000076 | prose | pages [3] -->
enormous amount of data and talk about the future application such as in the biomedical area.

<!-- b000077 | prose | pages [3] -->
2 Investigation Scenario Based on Crime Data

<!-- b000078 | heading | pages [3] -->
Mining Model

<!-- b000079 | prose | pages [3] -->
2.1

<!-- b000080 | heading | pages [3] -->
General Assumptions

<!-- b000081 | prose | pages [3] -->
• There is only one criminal gang in the given network;

<!-- b000082 | prose | pages [3] -->
• Messages can not be classiﬁed emotionally from appearance;

<!-- b000083 | prose | pages [3] -->
• Occurrences of messages are irrelevant to time;

<!-- b000084 | prose | pages [3] -->
• Eﬀects form data errors are negligible.

<!-- b000085 | prose | pages [3] -->
2

<!-- b000086 | furniture | pages [4] -->
Team # 12218

<!-- b000087 | furniture | pages [4] -->
Page 3 of 18

<!-- b000088 | prose | pages [4] -->
2.2 Deﬁnitions

<!-- b000089 | prose | pages [4] -->
Before proceeding to the real problem, we ﬁrst make some deﬁnitions: The multi-graph G = (V, E) is assumed to be a social network, where V denotes the set of nodes and E denotes the set of edges. A person in the network can be denoted by a node in the graph while edges stand for messages with certain topics passing through diﬀerent persons. Thus we can separate these persons into several cliques, judging from the topics of communication.

<!-- b000090 | prose | pages [4] -->
Let G′ = (V ′, E′) be a supergraph corresponding to multi-graph G, where V ′ is the set of supernodes and E′ is the set of superedges [5]. Each su- pernode P ′

<!-- b000091 | prose | pages [4] -->
i represents topic i with associated people in multi-graph G and there exists a superedge when supernodes connected by it possess common nodes. The weight of one superedge is the number of the common nodes.

<!-- b000092 | caption | pages [4] -->
Figure 1: Multi-graph

<!-- b000093 | caption | pages [4] -->
Figure 2: Supergraph

<!-- b000094 | caption | pages [4] -->
Figure 1 and 2 presented above display the transition from multi-graph to

<!-- b000095 | prose | pages [4] -->
the corresponding supergraph. Nodes in the multi-graph can be recognized as persons and supernodes in the supergraph can be recognized as topics involved with relevant people.

<!-- b000096 | prose | pages [4] -->
So the crime busting in a criminal network can be translated into: “Pro- vided with a multi-graph G = (V, E) and a query list Q = {q1, q2, q3, . . . , qi}, we aim to ﬁnd out all the possible subsets of nodes associated with ones in Q and form a list ordered by the measurements of association.”

<!-- b000097 | prose | pages [4] -->
2.3

<!-- b000098 | heading | pages [4] -->
Explanation of the Model

<!-- b000099 | prose | pages [4] -->
The researched crime network is connected by messages delivery, through information transmitting, the whole conspiratorial network can function eﬃ- ciently.

<!-- b000100 | prose | pages [4] -->
An common staﬀmember may have no idea in knowing whom the people really are, when having a conversation with them whereas the intrinsic character of topic can determine whether a person is involved in the conspiracy or not.

<!-- b000101 | prose | pages [4] -->
A piece of message is consist of countless information in many aspects. It is impossible and unnecessary to deal with them all at the same time, let alone composing these messages to a conclusion. In this case, we only focus our attention on three main aspects: Topics, Direction and People to whom they talked. However, the biggest challenge that we have confronted with is how to combine these three kinds of information appropriately.

<!-- b000102 | prose | pages [4] -->
3

<!-- b000103 | furniture | pages [5] -->
Team # 12218

<!-- b000104 | furniture | pages [5] -->
Page 4 of 18

<!-- b000105 | prose | pages [5] -->
We proposed a structure of network here in which the nodes denote topics of messages and edges denote people involved in them. Regarding the deﬁnition listed above, these characters are all possessed by the supergraph. In the general view, when a person switch his or her attention from one topic to another, we can regard it as person “ﬂows” among related topics, therefore the whole network become alive.

<!-- b000106 | prose | pages [5] -->
Before the further exploration of this method, we should ﬁrst analyze the “similarity” among collected topics. We use “Cooperation Factor (CF)” [5] to study the latent interrelationships.

<!-- b000107 | prose | pages [5] -->
Deﬁnition 2.3.1 (Cooperation Factor) In the supergraph G′ = (V ′, E′), the Cooperation Factor between two supernodes P ′

<!-- b000108 | prose | pages [5] -->
i and P ′

<!-- b000109 | prose | pages [5] -->
j is:

<!-- b000110 | prose | pages [5] -->
j ) = 2 × Nc(P ′

<!-- b000111 | prose | pages [5] -->
CF(S′, V ′

<!-- b000112 | prose | pages [5] -->
i , V ′

<!-- b000113 | prose | pages [5] -->
i, P ′

<!-- b000114 | prose | pages [5] -->
j)

<!-- b000115 | prose | pages [5] -->
CF ∈[0, 1]; , (1)

<!-- b000116 | prose | pages [5] -->
Nt(P ′

<!-- b000117 | prose | pages [5] -->
i, P ′

<!-- b000118 | prose | pages [5] -->
j)

<!-- b000119 | prose | pages [5] -->
Where: Nc denotes the number of common nodes between P ′

<!-- b000120 | prose | pages [5] -->
i and P ′

<!-- b000121 | prose | pages [5] -->
j; Nt denotes the number of total nodes contained in the P ′

<!-- b000122 | prose | pages [5] -->
i and P ′

<!-- b000123 | prose | pages [5] -->
j.

<!-- b000124 | prose | pages [5] -->
It is obvious that not all conspirators can contact directly but they must be very close for safety concern. To utilize this collective feature, it is essential to deﬁne a Cooperation Distance (CD) [5]:

<!-- b000125 | prose | pages [5] -->
Deﬁnition 2.3.2 (Cooperation Distance Metric) In the supergraph G′ = (V ′, E′) with a list of i person denoted by a query Q = {q1, q2, q3, . . . , qi}. Let v∗be a particular node in the multi-graph G, and V be the set of nodes in the multi-graph G. Then, the Cooperation Distance of v∗is then deﬁned as:

<!-- b000126 | prose | pages [5] -->
|Q|

<!-- b000127 | prose | pages [5] -->
ShortestPath(S′, v∗, qi)

<!-- b000128 | prose | pages [5] -->
P

<!-- b000129 | prose | pages [5] -->
i=1

<!-- b000130 | prose | pages [5] -->
CD(S′, v∗, V ) =

<!-- b000131 | prose | pages [5] -->
;

<!-- b000132 | prose | pages [5] -->
(2) |Q|

<!-- b000133 | prose | pages [5] -->
Where: the ShortestPath(S′, v∗, qi) is 0 when both qi and v∗belong to a same supernode, otherwise is the value derived from shortest path algorithm of v∗and qi with the weight of edges measured by CF.

<!-- b000134 | prose | pages [5] -->
The value of CF evaluates the level of correlation between two diﬀerent topics, then 1−CF indicates the level of uncorrelation in the opposite. We pick out the assumed conspiratorial topics and compare other unidentiﬁed topics with it by accordingly assign diﬀerent weights. Hence, we can apply the shortest path algorithm to this theory and ﬁgure out the corresponding CDs of each unidentiﬁed staﬀmember.

<!-- b000135 | prose | pages [5] -->
Those people with lowest values can be considered as having the most intimated communication with the criminal gang, which means they are more likely to be the real members in a criminal gang.

<!-- b000136 | prose | pages [5] -->
2.4 Tests and Veriﬁcations

<!-- b000137 | prose | pages [5] -->
After computing all the data we can obtain from the EZ (an investigation scenario provided by supervisor) case, concerning the points stated above, we can make a list of the CDs’ value in the ascending order, which indicates the possibility of a person being a conspirators in the opposite.

<!-- b000138 | prose | pages [5] -->
4 4

<!-- b000139 | furniture | pages [6] -->
Team # 12218

<!-- b000140 | furniture | pages [6] -->
Page 5 of 18

<!-- b000141 | prose | pages [6] -->
CD metric Name Rank 0.0000 Dave 1 0.0000 George 1 0.0000 Ellen 1 0.3333 Carol 4 0.3333 Fred 4 0.3333 Harry 4 0.7143 Bob 6 0.7143 Inez 6 1.0476 Anne 9 1.4286 Jaye 10

<!-- b000142 | caption | pages [6] -->
Table 1: Priority List for EZ Case

<!-- b000143 | prose | pages [6] -->
The top three in the list are the staﬀmembers with the highest possibilities of being involved in the conspiracy derived from our analysis, where there are already two are sure to be guilty. Moreover, Anne along with Jaye are both identiﬁed to be the “farthest away” from the conspiracy. But it is sad to ﬁnd that Carol may still be misjudged as a conspirator and we may probably leave Bob behind as well.

<!-- b000144 | caption | pages [6] -->
Figure 3: Discriminating Line for EZ Case

<!-- b000145 | prose | pages [6] -->
In order to determine a discriminating line in separating innocents from conspirators, we calculate the diﬀerence among pairs of neighbors in the list and pick out the biggest one through comparison. The hugest gap measured by curvature between two staﬀmembers can be deemed as a boundary that distinguishes two groups–the innocent one and the conspiratorial one for the conspiratorial messages is sure to be restricted in a small group.

<!-- b000146 | prose | pages [6] -->
Although there still exists several demerits considering the results, the ex- cellent structure of the investigation scenario encourages us to apply this method

<!-- b000147 | prose | pages [6] -->
5 5

<!-- b000148 | furniture | pages [7] -->
Team # 12218

<!-- b000149 | furniture | pages [7] -->
Page 6 of 18

<!-- b000150 | prose | pages [7] -->
to a larger criminal network with much more data.

<!-- b000151 | prose | pages [7] -->
Analysis on the Current Case 3

<!-- b000152 | prose | pages [7] -->
For now, the new network has 83 people involved, 400 collected messages, over 21,000 words of messages traﬃc, 15 topics, 7 known conspirators, and 8 known non-conspirators. There are also several members with same names in investigation which we just diﬀerentiate them by the denoted numbers. Based on the SNA method we proposed before, we calculate each staﬀmember’s CD metric and arrange them in an ascending order list. Considering the list size, we only list the top 40 to perform the results of our analysis.

<!-- b000153 | prose | pages [7] -->
Priority Lists of Potential Conspirators 3.1

<!-- b000154 | prose | pages [7] -->
We ﬁrst work out the CF values of each adjacent vertices in order to quantify the level of correlations among edges. Because there are three topics considered to be involved in the conspiracy, we make a combination of these three initial values into ones by setting equal weights and make an addition. Therefore CD metrics can be determined by making the use of shortest path algorithm and priority list may come to surface then.

<!-- b000155 | prose | pages [7] -->
The output of our analysis on the 3 topics which deemed to be conspiratorial and 7 known conspirators are listed below:

<!-- b000156 | prose | pages [7] -->
Name CD metric Elsie 0.0000 Jean 0.0000 Alex 0.0000 Elsie 0.0000 Paul 0.0000 Harvey 0.0000 Ulf 0.0000 Cha 0.0000 Sheng 0.0000 Darol 0.0000 Yao 0.0000 Stephanie 0.2265 Kim 0.2265 Beth 0.2265 Seeni 0.2265 Dolores 0.2340 Marion 0.2340 Dwight 0.2340 William 0.2340 Lars 0.2340 Name CD metric Paige 0.2859 Neal 0.2859 Priscilla 0.2859 Kristina 0.3641 Sherri 0.3641 Franklin 0.3641 Marcia 0.3641 Jerome 0.4224 Louis 0.4224 Beth 0.4420 Douglas 0.4420 Crystal 0.4480 Claire 0.4480 Jerome 0.4480 Darlene 0.4480 Patricia 0.4525 Jia 0.4525 Neal 0.4584 Melia 0.4584 Francis 0.4605

<!-- b000157 | caption | pages [7] -->
Table 2: Partial Priority List for Requirement 1

<!-- b000158 | prose | pages [7] -->
We note that the 11 persons on the top have the same values of CD metric, on the other hand, indicates that they can be regarded as having the same

<!-- b000159 | prose | pages [7] -->
6 6

<!-- b000160 | furniture | pages [8] -->
Team # 12218

<!-- b000161 | furniture | pages [8] -->
Page 7 of 18

<!-- b000162 | prose | pages [8] -->
possibilities of being a conspirator. The 7 known conspirators being involved in suspected group also demonstrates the reasonableness of our method.

<!-- b000163 | prose | pages [8] -->
Furthermore, we plot the discrimination line in the same way we displayed in the small network by comparing the separation among adjacent persons in the priority list. Thus, the possible conspirators are: Elsie, Jean, Alex, Elsie,

<!-- b000164 | caption | pages [8] -->
Figure 4: Discriminating Line for Requirement 1

<!-- b000165 | prose | pages [8] -->
Paul, Harvey, Ulf, Cha, Sheng, Darol and Yao.

<!-- b000166 | prose | pages [8] -->
3.2 Performance with More Accurate Information

<!-- b000167 | prose | pages [8] -->
The promising results obtained above motivate us to test our model’s per- formance with more accurate information in the same network. When Chris was identiﬁed to be a conspirator and Topic 1 was regarded as being associated with conspiracy, we revaluate the level of correlations among total 15 topics. After setting diﬀerent similarities’ weights to particular edges accordingly, we recompute these data and work out with a amended list and discriminating line. The results are displayed in Table 3 and Figure 5.

<!-- b000168 | prose | pages [8] -->
4 Searching for Leaders

<!-- b000169 | prose | pages [8] -->
It’s hard to uncover all the leaders in a well-organized crime networks due to its high complexity. But we can build a calibration system based on a theory called Centrality Analysis [6,7] to identify some suspects who are more likely to be the chief ones.

<!-- b000170 | prose | pages [8] -->
7

<!-- b000171 | furniture | pages [9] -->
Team # 12218

<!-- b000172 | prose | pages [9] -->
Name CD metric Chris 0.0000 Elsie 0.0000 Jean 0.0000 Alex 0.0000 Elsie 0.0000 Paul 0.0000 Harvey 0.0000 Ulf 0.0000 Cha 0.0000 Sheng 0.0000 Darol 0.0000 Yao 0.0000 Dolores 0.2869 Marion 0.2869 Dwight 0.2869 William 0.2869 Lars 0.2869 Seeni 0.2869 Stephanie 0.2877 Kim 0.2877

<!-- b000173 | furniture | pages [9] -->
Page 8 of 18

<!-- b000174 | prose | pages [9] -->
Name CD metric Beth 0.2877 Paige 0.3362 Neal 0.3362 Priscilla 0.3362 Crystal 0.3511 Lois 0.3511 Ellin 0.3511 Han 0.3511 Kristina 0.3525 Sherri 0.3525 Franklin 0.3525 Marcia 0.3525 Gretchen 0.3525 Douglas 0.3525 Claire 0.4294 Jerome 0.4294 Louis 0.4294 Darlene 0.4294 Jerome 0.4299 Beth 0.4549

<!-- b000175 | caption | pages [9] -->
Table 3: Partial Priority List for Requirement 2

<!-- b000176 | caption | pages [9] -->
Figure 5: Discriminating Line for Requirement 2

<!-- b000177 | prose | pages [9] -->
4.1 Centrality Analysis

<!-- b000178 | prose | pages [9] -->
There are three measures of centrality that have been widely used in social network analysis:

<!-- b000179 | prose | pages [9] -->
Betweenness Betweenness of one node is the number of geodesics (shortest

<!-- b000180 | prose | pages [9] -->
8 8

<!-- b000181 | furniture | pages [10] -->
Team # 12218

<!-- b000182 | furniture | pages [10] -->
Page 9 of 18

<!-- b000183 | prose | pages [10] -->
paths between any other two nodes in the network) passing through it:

<!-- b000184 | prose | pages [10] -->
CB(i) = gjk(i)

<!-- b000185 | prose | pages [10] -->
(3)

<!-- b000186 | prose | pages [10] -->
gjk

<!-- b000187 | prose | pages [10] -->
Where: gjk represents the number of shortest paths between any two nodes and gjk(i) represents the number of shortest paths running through node i;

<!-- b000188 | prose | pages [10] -->
Closeness Closeness is the sum of geodesics between the particular node and

<!-- b000189 | prose | pages [10] -->
every other node in the network:

<!-- b000190 | prose | pages [10] -->
CC(i) =

<!-- b000191 | prose | pages [10] -->
 N

<!-- b000192 | prose | pages [10] -->
−1

<!-- b000193 | prose | pages [10] -->
X

<!-- b000194 | prose | pages [10] -->
d(i, j)

<!-- b000195 | prose | pages [10] -->
(4)

<!-- b000196 | prose | pages [10] -->
j

<!-- b000197 | prose | pages [10] -->
Where: d(i, j) denotes the binary shortest distance between any two nodes in the network;

<!-- b000198 | prose | pages [10] -->
Degree The original concept [6] of one node’s degree is its number of links as:

<!-- b000199 | prose | pages [10] -->
ki = CX

<!-- b000200 | prose | pages [10] -->
N X

<!-- b000201 | prose | pages [10] -->
D (i) =

<!-- b000202 | prose | pages [10] -->
xij (5)

<!-- b000203 | prose | pages [10] -->
j

<!-- b000204 | prose | pages [10] -->
Where: i denotes the focal node, j denotes other nodes in the network; N is the node’s number and xij = {0, 1} are the entries in the adjacency matrix. However, some pioneers proposed a method which considering the weights of each edge in a weighted network [8–10] by introducing a new measure called strength:

<!-- b000205 | prose | pages [10] -->
si = CW

<!-- b000206 | prose | pages [10] -->
N X

<!-- b000207 | prose | pages [10] -->
D (i) =

<!-- b000208 | prose | pages [10] -->
wij (6)

<!-- b000209 | prose | pages [10] -->
j

<!-- b000210 | prose | pages [10] -->
Where: i denotes the focal node, j denotes other nodes in the network; N is the node’s number and wij are the entries in the adjacency matrix whose value is positive when i is connected to j (so that it can reﬂect the weight), otherwise is 0.

<!-- b000211 | prose | pages [10] -->
Now we utilize a method to combine both degree and strength with the introduction of a turning parameter α [11]:

<!-- b000212 | prose | pages [10] -->
(i) = ki × (si

<!-- b000213 | prose | pages [10] -->
CW α

<!-- b000214 | prose | pages [10] -->
D

<!-- b000215 | prose | pages [10] -->
)α = k(1−α)

<!-- b000216 | prose | pages [10] -->
× sα

<!-- b000217 | prose | pages [10] -->
(7) i

<!-- b000218 | prose | pages [10] -->
i

<!-- b000219 | prose | pages [10] -->
ki

<!-- b000220 | prose | pages [10] -->
Where: α is a positive value which can be set according to diﬀerent re- quest. When the parameter is between 0 and 1, then it would be favorable to obtain a high value, otherwise a low value would be preferable. In our crime network analysis, we choose 0.5 to accomplish our goal.

<!-- b000221 | prose | pages [10] -->
The leadership of one individual conspirator can be “revealed” by one mea- sure or the combination of two or three, whereas some extremely special cases such as gatekeepers and receptionists are still of high possibility [12]. According to the present research, this method can work out some results with fairly good accuracy and is easily to spread out [13].

<!-- b000222 | prose | pages [10] -->
9 9

<!-- b000223 | furniture | pages [11] -->
Team # 12218

<!-- b000224 | prose | pages [11] -->
4.2

<!-- b000225 | heading | pages [11] -->
Interpretation of Results

<!-- b000226 | furniture | pages [11] -->
Page 10 of 18

<!-- b000227 | prose | pages [11] -->
It is obvious to see that we can form diﬀerent lists according to diﬀerent measures, whereas we can hardly to tell which one is more important in deciding one’s leadership.

<!-- b000228 | prose | pages [11] -->
Closeness Name Degree Chris 7.905 Kristina 8.743 Paige 14.477 Sherri 13.013 Gretchen 8.599 Karen 6.433 Patrick 7.497 Elsie 11.959 Hazel 9.000 Malcolm 6.559 Dolores 8.396 Francis 7.737 Sandy 8.927 Marion 7.254 Beth 8.546 Julia 12.956 Jerome 4.469 Neal 10.915 Jean 11.336 Kristine 8.975 Betweeness 0.010 0.034 0.011 0.045 0.013 0.063 0.012 0.088 0.014 0.064 0.013 0.047 0.012 0.042 0.012 0.100 0.011 0.064 0.011 0.052 0.012 0.091 0.011 0.079 0.012 0.058 0.013 0.086 0.012 0.044 0.013 0.100 0.009 0.042 0.014 0.061 0.012 0.074 0.012 0.085

<!-- b000229 | caption | pages [11] -->
Table 4: Partial Outputs of Centrality Analysis

<!-- b000230 | prose | pages [11] -->
Although these three measure possess excellent in measuring one’s ability in leadership, some demerits still exist:

<!-- b000231 | prose | pages [11] -->
(i) Degree does not consider the overall structure of the network and will

<!-- b000232 | prose | pages [11] -->
inevitably lead to some misjudgments [14,15];

<!-- b000233 | prose | pages [11] -->
(ii) The major challenge standing ahead of closeness is lack of capability to

<!-- b000234 | prose | pages [11] -->
deal with the disconnected components in networks [11];

<!-- b000235 | prose | pages [11] -->
(iii) Betweenness may function improperly when faced with some particular

<!-- b000236 | prose | pages [11] -->
cases such as a node has none shortest path running through it.

<!-- b000237 | prose | pages [11] -->
With so many unpredictable situations to concern, we simply place an equal weight to all of them and get a fusion value as result. We choose 40 staﬀ members who possess the highest fusion value from our analysis, results are in

<!-- b000238 | caption | pages [11] -->
Table 5. They are deem to be ones who can have the most important impact on

<!-- b000239 | prose | pages [11] -->
the whole network, in other words, leaders in the company. Comparing it with the priority list we work out, we can infer that Alex is a leader in the criminal gang.

<!-- b000240 | prose | pages [11] -->
10 10

<!-- b000241 | furniture | pages [12] -->
Team # 12218

<!-- b000242 | prose | pages [12] -->
Name Fusion Value Rank Franklin 0.0763 1 Julia 0.0803 2 Alex 0.0884 3 Gretchen 0.0884 4 Darlene 0.0964 5 Jerome 0.1406 6 Elsie 0.1566 7 Paige 0.1606 8 Sherri 0.1647 9 Gretchen 0.1928 10 Kristine 0.1968 11 Neal 0.2008 12 Dolores 0.2088 13 Jean 0.2088 14 Marion 0.2570 15 Donald 0.2610 16 Paul 0.2610 17 Patricia 0.2610 18 Neal 0.3173 19 Sandy 0.3414 20

<!-- b000243 | furniture | pages [12] -->
Page 11 of 18

<!-- b000244 | prose | pages [12] -->
Name Fusion Value Rank Yao 0.3494 21 Eric 0.3574 22 Crystal 0.3695 23 Wayne 0.3735 24 Francis 0.3775 25 Stephanie 0.3855 26 Hazel 0.3896 27 Karen 0.3936 28 Christina 0.4016 29 Beth 0.4096 30 Lois 0.4257 31 William 0.4257 32 Beth 0.4297 33 Kristina 0.4337 34 Louis 0.4337 35 Dwight 0.4498 36 Harvey 0.4578 37 Elsie 0.4699 38 Patrick 0.4779 39 Malcolm 0.4940 40

<!-- b000245 | caption | pages [12] -->
Table 5: Partial Leadership List on Fusion Values

<!-- b000246 | prose | pages [12] -->
5

<!-- b000247 | heading | pages [12] -->
Model Optimizing

<!-- b000248 | prose | pages [12] -->
To make our model function better, we need to take a look back on the weight placed on each topics. In the previous work, we simply give the signiﬁcant topics an equal random initial value while others were determined by calculation based on the quantiﬁed correlations among them.

<!-- b000249 | prose | pages [12] -->
However, this process of quantiﬁcation can not provide a satisﬁed result precisely. To cross this barrier, we switch our attention to more powerful techniques–Semantic Network Analysis (SemNa) and Text Analysis.

<!-- b000250 | prose | pages [12] -->
Semantic Network Analysis 5.1

<!-- b000251 | prose | pages [12] -->
A semantic network is a network which represents semantic relations be- tween concepts in patterns of interconnected nodes and arcs. It is often used as a form of knowledge representation [16]. With the fast improvements of the SNA approach, the application of this method has been extent to the Web [17], encouraging us to apply it to the semantic network. In our current case, we need to analyze the “crime ontology” as carefully as possible, where a multi-graph can be constructed according to the theory of semantic network [18]. Here we

<!-- b000252 | heading | pages [12] -->
build a model based on the Semantic Network Analysis as the application

<!-- b000253 | prose | pages [12] -->
of SNA approach and centrality analysis we raised up before.

<!-- b000254 | prose | pages [12] -->
11 11

<!-- b000255 | furniture | pages [13] -->
Team # 12218

<!-- b000256 | furniture | pages [13] -->
Page 12 of 18

<!-- b000257 | prose | pages [13] -->
5.1.1 Construction of Semantic Network

<!-- b000258 | prose | pages [13] -->
In a semantic multi-graph, all nodes can be classiﬁed into two categories: concepts and property. As they literally mean, one concept can be expressed by using several properties, whereas diﬀerent collections of properties can ex- press diﬀerent concepts. One property can be used to describe a wide range of concepts while some of these concepts are speciﬁcal to this property. These relations among concepts and property can be used to construct a semantic network, which can be realized by the artiﬁcial intelligence system. Rules are displayed below [18]:

<!-- b000259 | caption | pages [13] -->
Figure 6: Relations among Nodes

<!-- b000260 | prose | pages [13] -->
The relations exhibited above can be concluded as:

<!-- b000261 | prose | pages [13] -->
• There exists a directed edge from C1 to C2, if concept C1 is a sub-concept of C2;

<!-- b000262 | prose | pages [13] -->
• There exists a directed edge from P1 to P2, if property P1 is a sub-property of P2;

<!-- b000263 | prose | pages [13] -->
• A directed edge should be added from each major concept node to the property node;

<!-- b000264 | prose | pages [13] -->
• Directed edges should be added from the property node to all range con- cept nodes.

<!-- b000265 | prose | pages [13] -->
5.1.2 Topic Selection

<!-- b000266 | prose | pages [13] -->
In our crime busting scenario, we can regard the concepts and properties deﬁned before as topics and keywords separately. We assess the importance of one topic in a criminal network by working out its centrality measures such as degree, closeness and betweenness. One with higher value of the combination of these three is supposed to be more crucial in a conspiracy. Thus, we can place the weights for each topic according to its conspiratorial level based on the content and context of messages’ transferring.

<!-- b000267 | prose | pages [13] -->
After revaluating the topics’ weights, we can reprocess the data to obtain a better result that can be closer to the truth. The partial results with top 40 derived from semantic web have been exhibited in Table 6.

<!-- b000268 | prose | pages [13] -->
12

<!-- b000269 | furniture | pages [14] -->
Team # 12218

<!-- b000270 | prose | pages [14] -->
Name CD Metric Chris 0.0000 Elsie 0.0000 Jean 0.0000 Alex 0.0000 Elsie 0.0000 Paul 0.0000 Harvey 0.0000 Ulf 0.0000 Cha 0.0000 Sheng 0.0000 Darol 0.0000 Yao 0.0000 Crystal 0.7423 Lois 0.7423 Ellin 0.7423 Han 0.7423 Dolores 0.7437 Marion 0.7437 Dwight 0.7437 William 0.7437

<!-- b000271 | furniture | pages [14] -->
Page 13 of 18

<!-- b000272 | prose | pages [14] -->
Name CD Metric Lars 0.7437 Seeni 0.7437 Paige 0.7445 Neal 0.7445 Priscilla 0.7445 Stephanie 0.7485 Kim 0.7485 Beth 0.7485 Sherri 0.9474 Jerome 0.9474 Louis 0.9474 Neal 0.9506 Jerome 0.9506 Douglas 0.9506 Melia 0.9506 Kristine 0.9597 Shelley 0.9597 Donald 0.9597 Carina 0.9597 Patrick 0.9770

<!-- b000273 | caption | pages [14] -->
Table 6: Partial Outputs from Semantic Web

<!-- b000274 | prose | pages [14] -->
5.2 Text Analysis

<!-- b000275 | prose | pages [14] -->
A large text databases potentially contain a great deal of knowledge, for text itself is a complex collection comprised of enormous amount of information [19]. However, it cannot be analyzed by applying common data mining methods. In order to extract valuable information from the messages, we construct a vector space model to estimate the importance of various topics.

<!-- b000276 | prose | pages [14] -->
5.2.1

<!-- b000277 | heading | pages [14] -->
Vector Space Model

<!-- b000278 | prose | pages [14] -->
Before making a careful analysis on the importance of topics, we should ﬁrst build a bridge connecting words and topics’ similarity. Therefore we introduce a measure called “Feature Item Weight” to quantify the impact of keywords on a particular topic [20].

<!-- b000279 | prose | pages [14] -->
Deﬁnition 5.2.2 (Feature Item Weight) Feature item weight wik indicates the importance of feature item Tk to the text Di:

<!-- b000280 | prose | pages [14] -->
tfik × log2(N/dfk) wik = qP

<!-- b000281 | prose | pages [14] -->


<!-- b000282 | prose | pages [14] -->
Tk∈Di

<!-- b000283 | prose | pages [14] -->
(8) 2

<!-- b000284 | prose | pages [14] -->
tfik × log2(N/dfk)

<!-- b000285 | prose | pages [14] -->
Where: tfik is the time of the feature item’s (Tk) appearance in text Di while dfk is the number of text including feature item Tk. feature item’s (Tk) ability of diﬀerentiating the diﬀerent kinds of text is weaker when the value of dfk is higher; N denotes the total number of text, idfk = log2(N/dfk) is the frequency of reverse text in which higher value indicate a stronger ability in diﬀerentiating the diﬀerent kinds of text.

<!-- b000286 | prose | pages [14] -->
13 13

<!-- b000287 | furniture | pages [15] -->
Team # 12218

<!-- b000288 | furniture | pages [15] -->
Page 14 of 18

<!-- b000289 | prose | pages [15] -->
Deﬁnition 5.2.3 (Text’s Similarity) Text’s similarity can be measured by the cosine of included angle formed by the corresponding vectors [21]:

<!-- b000290 | prose | pages [15] -->
Sim(di, dj) =

<!-- b000291 | prose | pages [15] -->
s

<!-- b000292 | prose | pages [15] -->
nP

<!-- b000293 | prose | pages [15] -->
wij × wjk

<!-- b000294 | prose | pages [15] -->
k=1

<!-- b000295 | prose | pages [15] -->
(9)

<!-- b000296 | prose | pages [15] -->
nP

<!-- b000297 | prose | pages [15] -->
nP

<!-- b000298 | prose | pages [15] -->
w2

<!-- b000299 | prose | pages [15] -->
w2

<!-- b000300 | prose | pages [15] -->
( (

<!-- b000301 | prose | pages [15] -->
ik)(

<!-- b000302 | prose | pages [15] -->
jk)

<!-- b000303 | prose | pages [15] -->
k=1

<!-- b000304 | prose | pages [15] -->
k=1

<!-- b000305 | prose | pages [15] -->
Where: di = (wi1, wi2, wi3, . . . , win) is a vector representing text Di in this vector space, and wik is the feature item weight.

<!-- b000306 | heading | pages [15] -->
Corroboration of Model Reasonableness

<!-- b000307 | prose | pages [15] -->
5.2.4

<!-- b000308 | prose | pages [15] -->
The value of the Sim can be used in weights’ determination through a more accurate way. When reapply the method to the big network in current case, we obtain a priority list resembled to the former one in Table 3, where the member of the criminal gang are still the same while some slight modiﬁcation of the CD metrics of the innocent ones. Nevertheless, we are still quite conﬁdent in a better performance of this model when accessed to a richer database. It is

<!-- b000309 | prose | pages [15] -->
Name CD Metric Chris 0.0000 Elsie 0.0000 Jean 0.0000 Alex 0.0000 Elsie 0.0000 Paul 0.0000 Harvey 0.0000 Ulf 0.0000 Cha 0.0000 Sheng 0.0000 Darol 0.0000 Yao 0.0000 Crystal 0.9174 Lois 0.9174 Ellin 0.9174 Han 0.9174 Kristina 0.9271 Paige 0.9271 Sherri 0.9271 Patrick 0.9271 Name CD Metric Dolores 0.9271 Marion 0.9271 Beth 0.9271 Julia 0.9271 Jerome 0.9271 Neal 0.9271 Franklin 0.9271 Claire 0.9271 Marcia 0.9271 Dwight 0.9271 Stephanie 0.9271 Gretchen 0.9271 Kim 0.9271 Jerome 0.9271 Shelley 0.9271 Priscilla 0.9271 Beth 0.9271 Douglas 0.9271 Patricia 0.9271 Louis 0.9271

<!-- b000310 | caption | pages [15] -->
Table 7: Partial Outputs of Vector Space Model

<!-- b000311 | prose | pages [15] -->
amazing that the members in criminal group are unchanged, where reversely corroborate the reasonableness of the network model.

<!-- b000312 | prose | pages [15] -->
14 14

<!-- b000313 | furniture | pages [16] -->
Team # 12218

<!-- b000314 | furniture | pages [16] -->
Page 15 of 18

<!-- b000315 | prose | pages [16] -->
6 Applications

<!-- b000316 | prose | pages [16] -->
Our method in analyzing the network with a complex database is comprised of social network analysis, centrality analysis, semantic network analysis and text analysis. Each of them can easily be extent to diﬀerent areas with the same intrinsic mechanism as we utilized, and some present researches even explain the reasons why these methods could possess a wide range of application with social concerns [22].

<!-- b000317 | prose | pages [16] -->
For now, text mining has become a prevalent automated method in exploit- ing the tremendous amount of knowledge in the biomedical literature such as the most common ones: rule-based or knowledgebased approaches, and statis- tical or machine-learning-based approaches [23]. The former one mainly focus on analyzing the structure of messages with sorts of knowledge while the latter one stresses on classifying full sentences. Several real performances of the se- mantic web application have already been surveyed in various biomedical area with knowledge integration and exploration [24].

<!-- b000318 | prose | pages [16] -->
With the useful information extracted from the messages transferred in the crowds, we can appeal to the semantic network analysis and text analysis for a deeper insight.

<!-- b000319 | prose | pages [16] -->
The theory of social network analysis provides a solid base to construct a semantic web in which content and context of one piece of message are under much more concern. Within a social group, the diﬀerence between each individual lies in the social experience and their relation with others, and these diﬀerence would eventually lead to a division of the social work, bringing various networks into function. Centrality can provide a good measurement of the structural importance of one node in the whole network [25]. This method of importance quantiﬁcation can help us with search for the focal point(s).

<!-- b000320 | prose | pages [16] -->
Therefore, we can be directed to a eﬃcient analyze by combining these methodology into one as a whole. A massive amount of data can enrich our sample collection and a good artiﬁcial intelligence system can enhance our semantic network analysis’s ability in information categorizing which strengthen the reasonableness of the whole model.

<!-- b000321 | prose | pages [16] -->
7

<!-- b000322 | heading | pages [16] -->
Conclusion

<!-- b000323 | prose | pages [16] -->
It’s not an easy task to formulate a well-organized crime busting scenario. In order to accomplish our goal, we ﬁrst discussed about the features one crim- inal gang could have. Based on the principle of secretness in a conspiracy, we deﬁned a cooperation distance (CD metric) to decide whether a person should be regarded as being involved in the conspiracy for we thought one’s closeness with the criminal group is a fairly conclusive argument.

<!-- b000324 | prose | pages [16] -->
Centrality measures provided a good way for us in detecting the leaders in the criminal network. Some modiﬁcations were proposed by us in order to apply the theory in a directed graph. Through comparison with the given information, it was delightful for us to ﬁnd that the true mangers possess high grades in the list of leadership measurement.

<!-- b000325 | prose | pages [16] -->
In the model’s reﬁnement work, we appealed to the techniques of semantic network analysis and text analysis. Visualization may be the most fundamental diﬀerence between the traditional analysis and the network research in nowadays study. After making a development of the Social Network Analysis, we success-

<!-- b000326 | prose | pages [16] -->
15

<!-- b000327 | furniture | pages [17] -->
Team # 12218

<!-- b000328 | furniture | pages [17] -->
Page 16 of 18

<!-- b000329 | prose | pages [17] -->
fully constructed a semantic web of topics and keywords connected by linguistic association.

<!-- b000330 | prose | pages [17] -->
Although objectiveness of this analytical method is fascinating, the unpredictable abilities of data processing for diﬀerent artiﬁcial intelligence system is a major barrier impeding the development of the semantic network analysis. We hope this situation can get a better changed with corresponding remediation.

<!-- b000331 | prose | pages [17] -->
A non-prominent output later obtained from the addition of text analysis is believed to result from being in lack of enough message simples. But the ﬁnal results was almost in acceptance because of the high resemblance to former ones. According to the statistical principles, we are expected to have a better consequence with more accuracy.

<!-- b000332 | prose | pages [17] -->
The promising results persuade us to put more faith in a good application of this model before long.

<!-- b000333 | prose | pages [17] -->
16

<!-- b000334 | furniture | pages [18] -->
Team # 12218

<!-- b000335 | heading | pages [18] -->
References

<!-- b000336 | furniture | pages [18] -->
Page 17 of 18

<!-- b000337 | references | pages [18] -->
[1] H. Chen, W. Chung, J.J. Xu, G. Wang, Y. Qin, and M. Chau. Crime data

<!-- b000338 | references | pages [18] -->
mining: a general framework and some examples. Computer, 37(4):50–56,

<!-- b000339 | references | pages [18] -->
2004.

<!-- b000340 | references | pages [18] -->
[2] B. Wiesbaden. Polizeiliche kriminalstatistik. Bundesrepublik Deutschland.

<!-- b000341 | references | pages [18] -->
Berichtsjahr, 2007.

<!-- b000342 | references | pages [18] -->
[3] M.K. Sparrow. The application of network analysis to criminal intelligence:

<!-- b000343 | references | pages [18] -->
An assessment of the prospects. Social networks, 13(3):251–274, 1991.

<!-- b000344 | references | pages [18] -->
Investigative data mining for security and criminal detection.

<!-- b000345 | references | pages [18] -->
[4] J. Mena.

<!-- b000346 | references | pages [18] -->
Butterworth-Heinemann, 2003.

<!-- b000347 | references | pages [18] -->
[5] A.M. Fard and M. Ester. Collaborative mining in multiple social networks

<!-- b000348 | references | pages [18] -->
data for criminal group discovery. In Computational Science and Engineer-

<!-- b000349 | references | pages [18] -->
ing, 2009. CSE’09. International Conference on, volume 4, pages 582–587.

<!-- b000350 | references | pages [18] -->
IEEE, 2009.

<!-- b000351 | references | pages [18] -->
[6] L.C. Freeman. Centrality in social networks conceptual clariﬁcation. Social

<!-- b000352 | references | pages [18] -->
networks, 1(3):215–239, 1979.

<!-- b000353 | references | pages [18] -->
[7] J. Xu and H. Chen. Criminal network analysis and visualization. Commu-

<!-- b000354 | references | pages [18] -->
nications of the ACM, 48(6):100–107, 2005.

<!-- b000355 | references | pages [18] -->
[8] A. Barrat, M. Barthelemy, R. Pastor-Satorras, and A. Vespignani. The

<!-- b000356 | references | pages [18] -->
architecture of complex weighted networks.

<!-- b000357 | references | pages [18] -->
Proceedings of the National

<!-- b000358 | references | pages [18] -->
Academy of Sciences of the United States of America, 101(11):3747, 2004.

<!-- b000359 | references | pages [18] -->
Analysis of weighted networks.

<!-- b000360 | references | pages [18] -->
[9] M.E.J. Newman.

<!-- b000361 | references | pages [18] -->
70(5):056131, 2004.

<!-- b000362 | references | pages [18] -->
Physical Review E,

<!-- b000363 | references | pages [18] -->
[10] T. Opsahl, V. Colizza, P. Panzarasa, and J.J. Ramasco.

<!-- b000364 | references | pages [18] -->
Prominence

<!-- b000365 | references | pages [18] -->
The weighted rich-club eﬀect.

<!-- b000366 | references | pages [18] -->
and control:

<!-- b000367 | references | pages [18] -->
101(16):168702, 2008.

<!-- b000368 | references | pages [18] -->
Physical review letters,

<!-- b000369 | references | pages [18] -->
[11] T. Opsahl, F. Agneessens, and J. Skvoretz.

<!-- b000370 | references | pages [18] -->
Node centrality in weight-

<!-- b000371 | references | pages [18] -->
ed networks: Generalizing degree and shortest paths.

<!-- b000372 | references | pages [18] -->
32(3):245–251, 2010.

<!-- b000373 | references | pages [18] -->
[12] W.E. Baker and R.R. Faulkner.

<!-- b000374 | references | pages [18] -->
Social Networks,

<!-- b000375 | references | pages [18] -->
The social organization of conspiracy:

<!-- b000376 | references | pages [18] -->
Illegal networks in the heavy electrical equipment industry. American So-

<!-- b000377 | references | pages [18] -->
ciological Review, pages 837–860, 1993.

<!-- b000378 | references | pages [18] -->
[13] V.E. Krebs. Mapping networks of terrorist cells. Connections, 24(3):43–52,

<!-- b000379 | references | pages [18] -->
2002.

<!-- b000380 | references | pages [18] -->
[14] D.J. Brass. Being in the right place: A structural analysis of individual

<!-- b000381 | references | pages [18] -->
inﬂuence in an organization. Administrative Science Quarterly, pages 518–

<!-- b000382 | references | pages [18] -->
539, 1984.

<!-- b000383 | references | pages [18] -->
[15] S.P. Borgatti. Centrality and network ﬂow. Social Networks, 27(1):55–71,

<!-- b000384 | references | pages [18] -->
2005.

<!-- b000385 | references | pages [18] -->
17

<!-- b000386 | references | pages [18] -->
17

<!-- b000387 | furniture | pages [19] -->
Team # 12218

<!-- b000388 | furniture | pages [19] -->
Page 18 of 18

<!-- b000389 | references | pages [19] -->
[16] J.F. Sowa. Semantic networks. Encyclopedia of Cognitive Science, 1992.

<!-- b000390 | references | pages [19] -->
[17] J.M. Kleinberg. Authoritative sources in a hyperlinked environment. Jour-

<!-- b000391 | references | pages [19] -->
nal of the ACM (JACM), 46(5):604–632, 1999.

<!-- b000392 | references | pages [19] -->
[18] B. Hoser, A. Hotho, R. J¨aschke, C. Schmitz, and G. Stumme. Semantic

<!-- b000393 | references | pages [19] -->
network analysis of ontologies. The Semantic Web: Research and Applica-

<!-- b000394 | references | pages [19] -->
tions, pages 514–529, 2006.

<!-- b000395 | references | pages [19] -->
[19] T. Nasukawa and T. Nagano. Text analysis and knowledge mining system.

<!-- b000396 | references | pages [19] -->
IBM Systems Journal, 40(4):967–984, 2001.

<!-- b000397 | references | pages [19] -->
[20] Qi Shiwei.

<!-- b000398 | references | pages [19] -->
Web text mining and its application in correlation analysis

<!-- b000399 | references | pages [19] -->
between events (in chinese). Master’s thesis, National University of Defense

<!-- b000400 | references | pages [19] -->
Technology, 2008.

<!-- b000401 | references | pages [19] -->
[21] Shi Zhiwei, Liu Tao, and Wu Gongyi. An eﬀective and eﬃcient algorithm for

<!-- b000402 | references | pages [19] -->
text categorization (in chinese). Computer Engineering and Applications,

<!-- b000403 | references | pages [19] -->
41(29):180–183, 2005.

<!-- b000404 | references | pages [19] -->
[22] A. Sih, S.F. Hanser, and K.A. McHugh. Social network theory: new insights

<!-- b000405 | references | pages [19] -->
and issues for behavioral ecologists. Behavioral Ecology and Sociobiology,

<!-- b000406 | references | pages [19] -->
63(7):975–988, 2009.

<!-- b000407 | references | pages [19] -->
[23] K.B. Cohen and L. Hunter. Getting started in text mining. PLoS compu-

<!-- b000408 | references | pages [19] -->
tational biology, 4(1):e20, 2008.

<!-- b000409 | references | pages [19] -->
[24] H. Chen, L. Ding, Z. Wu, T. Yu, L. Dhanapalan, and J.Y. Chen.

<!-- b000410 | references | pages [19] -->
Se-

<!-- b000411 | references | pages [19] -->
mantic web for integrated network analysis in biomedicine. Brieﬁngs in

<!-- b000412 | references | pages [19] -->
bioinformatics, 10(2):177–192, 2009.

<!-- b000413 | references | pages [19] -->
[25] K. Chan and J. Liebowitz.

<!-- b000414 | references | pages [19] -->
The synergy of social network analysis and

<!-- b000415 | references | pages [19] -->
knowledge mapping: a case study. International journal of management

<!-- b000416 | references | pages [19] -->
and decision making, 7(1):19–35, 2006.

<!-- b000417 | references | pages [19] -->
18
