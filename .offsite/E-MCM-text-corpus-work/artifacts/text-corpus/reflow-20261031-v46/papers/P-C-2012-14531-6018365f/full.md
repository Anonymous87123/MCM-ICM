# P-C-2012-14531-6018365f

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
For office use only T1 ________________ T2 ________________ T3 ________________ T4 ________________ Team Control Number 14531 Problem Chosen C For office use only F1 ________________ F2 ________________ F3 ________________ F4 ________________ 2012 Mathematical Contest in Modeling (MCM) Summary Sheet (Attach a copy of this page to each copy of your solution paper.) Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000002 | title | pages [1] -->
Finding Conspirators in the Network: Machine Learning with Resource-allocation Dynamics

<!-- b000003 | prose | pages [1] -->
Problem Clarification: A conspiracy network is embedded into a network of employees of a company, with its every edge representing a message sent from one node to the other and categorized by topics. Given a few known criminals, non-criminals and suspicious topics, we are fundamentally asked to estimate the probability of criminals involvement for the not identified individuals , and to clarify the leader of conspirators. Besides, relevant discussions are suggested.

<!-- b000004 | prose | pages [1] -->
Assumptions：(i) Two classes, conspirators and non-conspirators, are linearly separable in the space spanned by local features of a node, which is necessary to machine learning.(ii) A conspirator is reluctant to mention topics related to crime when talking with an outsider.(iii) Conspirators tend not to talk about irrelevant topics frequently with each other. (iv) The leader of conspiracy tries to minimize risk by restricting direct contacts. (v) A non-conspirator has no idea of who are conspirators, thus treating conspirator and non-conspirators equally.

<!-- b000005 | prose | pages [1] -->
Model Design and Justification：The probability of conspiracy for an unidentified node is modeled as a sigmoid function in terms of a linear combination of the node’s features (logistic regression), whereas features are formulated from local topological measures and the node’s semantic messaging patterns. Parameters of this model are trained by using a subset of identified conspirators and non-conspirators. The performance of the model is enhanced by discovering potential relationship of similarities among topics via topic-word bipartite dynamics. Resource-allocation dynamics are performed to identify the leader of the conspirators, which win theoretical evidence in criminal network research.

<!-- b000006 | prose | pages [1] -->
Results and Sensitivity Analysis：(i)The accuracy of the machine learning scheme is measured by its performance on leave-one-out cross validation. Basic solution gets 73% prediction accuracy and semantic enhanced solution win 87% correct rate. (ii)The insensitivity of priority conspirator list is manifested by analyzing Kendall’s tau. This argument is 0.86 illustrates high stability of the model performance.(iii)The leader we predicted tends to be Yao  and the top three in priority list are Dolores, Crystal and Jerome (known conspirators excluded).

<!-- b000007 | heading | pages [1] -->
Strengths and Weaknesses Discussion：

<!-- b000008 | prose | pages [1] -->
The combination of both the topology properties and semantic affinity among individuals leads to a good performance. The time complexity is linear in the whole process in mining of semantic potential information, which is suitable with large amounts of data.

<!-- b000009 | prose | pages [1] -->
However, when facing with large amounts of data, our model prefer obtaining assistance from semantic network analysis to form the expert dictionary. Such features might also meaningless when change a new network background.

<!-- b000010 | author_callout | pages [1] -->
KEY CONCEPT Machine learning Logistic regression Semantic diffusion Bipartite graph Resource-allocation dynamics Kendall’s tau coefficient

<!-- b000011 | author_callout | pages [1] -->
KEY TECHNIQUES Gradient descent Revised Leader Rank Bipartite graph transmission

<!-- b000012 | furniture | pages [2] -->
Team # 14531

<!-- b000013 | furniture | pages [2] -->
Page 1 of 19

<!-- b000014 | heading | pages [2] -->
Contents

<!-- b000015 | contents | pages [2] -->
1

<!-- b000016 | contents | pages [2] -->
Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000017 | contents | pages [2] -->
2

<!-- b000018 | contents | pages [2] -->
2

<!-- b000019 | contents | pages [2] -->
A Machine Learning Solution to Criminal Priority . . . . . . . .

<!-- b000020 | contents | pages [2] -->
4

<!-- b000021 | contents | pages [2] -->
2.1

<!-- b000022 | contents | pages [2] -->
Feature formulation . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000023 | contents | pages [2] -->
4

<!-- b000024 | contents | pages [2] -->
2.2

<!-- b000025 | contents | pages [2] -->
Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000026 | contents | pages [2] -->
6

<!-- b000027 | contents | pages [2] -->
2.2.1

<!-- b000028 | contents | pages [2] -->
Logistic regression

<!-- b000029 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
7

<!-- b000031 | contents | pages [2] -->
2.2.2

<!-- b000032 | contents | pages [2] -->
Gradient descent

<!-- b000033 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
7

<!-- b000035 | contents | pages [2] -->
2.2.3

<!-- b000036 | contents | pages [2] -->
Leave-one-out cross validation . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
8

<!-- b000038 | contents | pages [2] -->
2.2.4

<!-- b000039 | contents | pages [2] -->
Selecting regularization parameter . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
8

<!-- b000041 | contents | pages [2] -->
2.3

<!-- b000042 | contents | pages [2] -->
Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
8

<!-- b000044 | contents | pages [2] -->
2.4

<!-- b000045 | contents | pages [2] -->
Semantic model enhancement

<!-- b000046 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
10

<!-- b000048 | contents | pages [2] -->
3

<!-- b000049 | contents | pages [2] -->
Identifying the leader of the conspiracy . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [2] -->
12

<!-- b000051 | contents | pages [2] -->
3.1

<!-- b000052 | contents | pages [2] -->
LeaderRank . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [2] -->
13

<!-- b000054 | contents | pages [2] -->
3.2

<!-- b000055 | contents | pages [2] -->
Suspicious topic sub-network extraction . . . . . . . . . . . . . . . .

<!-- b000056 | contents | pages [2] -->
13

<!-- b000057 | contents | pages [2] -->
3.3

<!-- b000058 | contents | pages [2] -->
Edge reverse . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000059 | contents | pages [2] -->
13

<!-- b000060 | contents | pages [2] -->
3.4

<!-- b000061 | contents | pages [2] -->
Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
14

<!-- b000063 | contents | pages [2] -->
3.5

<!-- b000064 | contents | pages [2] -->
Empirical support . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
14

<!-- b000066 | contents | pages [2] -->
3.6

<!-- b000067 | contents | pages [2] -->
Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
15

<!-- b000069 | contents | pages [2] -->
4

<!-- b000070 | contents | pages [2] -->
Evaluating the Model . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
15

<!-- b000072 | contents | pages [2] -->
4.1

<!-- b000073 | contents | pages [2] -->
Sensitivity analysis . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
15

<!-- b000075 | contents | pages [2] -->
4.1.1

<!-- b000076 | contents | pages [2] -->
Priority list . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
15

<!-- b000078 | contents | pages [2] -->
4.1.2

<!-- b000079 | contents | pages [2] -->
Probability inﬂation

<!-- b000080 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
16

<!-- b000082 | contents | pages [2] -->
5 Discussion and Conclusion

<!-- b000083 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
18

<!-- b000085 | contents | pages [2] -->
5.1

<!-- b000086 | contents | pages [2] -->
Summary

<!-- b000087 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
18

<!-- b000089 | contents | pages [2] -->
5.2

<!-- b000090 | contents | pages [2] -->
Further discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
18

<!-- b000092 | furniture | pages [3] -->
Team # 14531

<!-- b000093 | furniture | pages [3] -->
Page 2 of 19

<!-- b000094 | heading | pages [3] -->
1 Introduction

<!-- b000095 | prose | pages [3] -->
As illustrated in Figure 1, criminals and conspirators tend to form organization- al patterns, interconnected with each other for collaboration, while still maintaining social ties with the outside, thus providing a natural context for description and analysis with networks [Baker & Faulkner, 1993].

<!-- b000096 | caption | pages [3] -->
Figure 1: The 83-employee network(red nodes are known conspirators and the blue

<!-- b000097 | prose | pages [3] -->
ones are known non-conpirators)

<!-- b000098 | prose | pages [3] -->
Criminal networks can be captured from various information, resulting in d- iﬀerent types of networks, where each node represents a person, and an edge is present when two nodes collaborate in the same task, share the same family name etc., or, as in this case, exchange messages [Krebs, 2002].

<!-- b000099 | prose | pages [3, 4] -->
As nodes in this graph can be a mixture of both criminals and non-criminals, it is desirable to determine all the suspicious criminals from topological properties of the network and other prior knowledge, which includes known criminals, known non-criminals and other information related to their interactions. Moreover, it is usually of further interest that a priority list with descending criming likelihood is obtained and the primary leader of the organization is identiﬁed, which eﬀectively facilitates law-enforcement by focusing our attention on the most suspicious and the most essential.

<!-- b000100 | furniture | pages [4] -->
Team # 14531

<!-- b000101 | furniture | pages [4] -->
Page 3 of 19

<!-- b000103 | prose | pages [4] -->
Despite the discrepancy with network types, several general methods have been proposed by researchers.

<!-- b000104 | prose | pages [4] -->
Most notably, many authors have adopted centrality measures of the graph for analyzing the characteristics of criminals. It has been found that criminals with high betweenness centrality are usually brokers, while those with high degree centrality enjoy better proﬁt by taking higher risk [Krebs, 2002]. And Morselli et al. proposed that leaders of a criminal organization tend to balance proﬁt and risk by making a careful trade-oﬀbetween degree centrality and betweenness centrality [Morselli, 2010].

<!-- b000105 | prose | pages [4] -->
However, centrality approaches, which utilize local properties, tend to overlook the complex topology with the whole networks. Therefore, social network analysis (SNA) methods including subgroup detection and block-modeling have been intro- duced, which try to discover the hidden topological patterns by partitioning the big network into small closely connected cliques [Xu, 2005]. Despite the light they shed upon the internal structures of criminal networks, these methods still suﬀer from intimidating complexity with large databases [Wheat, 2007].

<!-- b000106 | prose | pages [4] -->
In this paper, we carefully combine the local-feature-based methods with ap- proaches related to global topology of conspiracy networks. We propose a machine learning scheme to leverage local features, so as to estimate each node’s likelihood of conspiracy involvement. And dynamics-based methods, which are less compu- tationally expensive than most of other topology-based approaches, are adopted to help ﬁnd out the leader of conspirators and to discover semantic connections between topics.

<!-- b000107 | prose | pages [4] -->
We start with the formulation of useful local features of a node in the network, which then lead to the machine learning scheme. By feeding a subset of known conspirators and non-conspirators as training samples into the learning algorithm, the classiﬁcation hypothesis is formed. We then use it to estimate the probability of being a conspirator for every unidentiﬁed individual in the network.

<!-- b000108 | prose | pages [4] -->
As highly suspicious topics are essential to the performance of machine learning, we then try to discover similarities between topics, by performing simple source- allocation dynamics on the bipartite semantic network made up of topics and sen- sitive words. Those ﬁndings expanded our knowledge on suspicious topics, thus enhancing the accuracy of our machine learning model.

<!-- b000109 | prose | pages [4] -->
Motivated by the goal of ﬁnding criminal leaders, we applied a dynamics-based ranking algorithms on a subgraph extracted from the network. Our ﬁndings are in agreement with empirical knowledge on the centrality balance of criminal leaders.

<!-- b000110 | prose | pages [4] -->
Finally, sensitivity analysis is performed to test the robustness of our approach, followed by further discussions.

<!-- b000111 | furniture | pages [5] -->
Team # 14531

<!-- b000112 | furniture | pages [5] -->
Page 4 of 19

<!-- b000113 | heading | pages [5] -->
2 A Machine Learning Solution to Criminal Pri-

<!-- b000114 | prose | pages [5] -->
ority

<!-- b000115 | prose | pages [5] -->
Machine learning is carefully selected by us to play the key role in the en- tire the strategy mainly for consideration on its capability of adaptiveness and reorganization, which simulate human beings on actions of study to obtain fresh knowledge. Such character is quite important since now we encounter a problem which is usually done by people through just the same method: deduction, reason- ing and reorganization our structure of knowledge to get over it. Especially met with such deduction task based on hundreds of thousands of data or big amount of information, people are helpless and their ability so terribly limited that we have to turn to machines.

<!-- b000116 | prose | pages [5] -->
In this section, we will describe the whole construction process of our machine learning framework in detail including feature formulation, core learning methods and experimental results. Through statistical analysis on the results, we propose our enhancement based on semantic diﬀusion.

<!-- b000117 | prose | pages [5] -->
We commence with several necessary assumptions:

<!-- b000118 | prose | pages [5] -->
• We assume that all the data and information about the EZ case network and 83-node network are relatively stable in a long period, rather than from coincident observation, to guarantee the representability of the results from the aspect of data origin.

<!-- b000119 | prose | pages [5] -->
• Based on necessary observation on the network, which will be exhaustively described in main body, we put forward our assumption that the contents of the communication among conspirators tends to be relevant about suspicious topics or some formal issues, rather than gossip.

<!-- b000120 | prose | pages [5] -->
• We assume that both networks in EZ case and in more complicated case obey the same information transmission rule that ensure the analogy about some core mechanism could stand.

<!-- b000121 | heading | pages [5] -->
2.1 Feature formulation

<!-- b000122 | prose | pages [5] -->
• Centrality

<!-- b000123 | prose | pages [5] -->
We exploit three types of centrality including degree, betweenness and close- ness centrality to determine the center of the suspicious network from diﬀerent aspects:

<!-- b000124 | prose | pages [5] -->
▶Degree centrality [Freeman, 1979] indicates activeness of a member, i.e.

<!-- b000125 | prose | pages [5, 6] -->
the member who tends to have more links to its surroundings. As explained in [Xu & Chen, 2003], degree centrality is not quite reliable to indicate the team leader in a criminal network. For a graph G(V, E), the normalized degree centrality of node i is as follows:

<!-- b000126 | furniture | pages [6] -->
Team # 14531

<!-- b000127 | furniture | pages [6] -->
Page 5 of 19

<!-- b000129 | prose | pages [6] -->
∑|V | j=1 ν(i, j) , i̸ = j CD(i) = (1) |V | −1

<!-- b000130 | prose | pages [6] -->
Where ν is a binary indicator showing whether exists a link between two nodes. Considering the graph is directed in our case, we separately calculate the in-degree and out-degree of every node.

<!-- b000131 | prose | pages [6] -->
▶Betweenness centrality [Freeman, 1979] describes how much a node tends to be on the shortest path of other nodes. A node with large betweenness centrality does not necessarily induce its large degree, but illustrates its role of “gatekeeper”, who is more possibly to be a intermediary when any oth- er two members transmit information between themselves. The normalized betweenness centrality is deﬁned as:

<!-- b000132 | prose | pages [6] -->
∑|V | ∑|V | k<j ωj,k(i) j=1 , k̸ = i CB(i) = (2) |V | −1

<!-- b000133 | prose | pages [6] -->
where ωj,k(i) indicates whether the shortest path between node j and node k passes through node i.

<!-- b000134 | prose | pages [6] -->
▶Closeness centrality [Sabidussi, 1966] is usually utilized to measure how far away one node is from the others. Closeness of a node is deﬁned as the inverse of the sum of its distances to all other nodes and can be treat as a measure of eﬃciency when spreading information from itself to all other nodes sequentially. It indicates how easily an individual connects with other members. The normalized closeness centrality is deﬁned as:

<!-- b000135 | prose | pages [6] -->
∑|V | j=1 ρ(i, j) −Ccmin , i̸ = j Cc(i) = (3) Ccmax −Ccmin

<!-- b000136 | prose | pages [6] -->
where ρ(i, j) is the length of the shortest path connecting nodes i and j.

<!-- b000137 | prose | pages [6] -->
Ccmin and Ccmax are the minimum and maximum lengths of the shortest paths respectively.

<!-- b000138 | prose | pages [6] -->
• Number of known neighboring conspirators

<!-- b000139 | prose | pages [6, 7] -->
We consider the number of known neighboring conspirators of a node as a signiﬁcant feature. The interaction among known conspirators in message network suggests a much stronger connectivity than the one among the known non-conspirators. This phenomenon reasonably reveal that a conspirator is more likely to communicate with his or her accomplice rather than a outlier and, on the contrary, non-conspirators lack such consciousness. As shown in Figure 2, we calculate the possession rate of its confederacy among all its neighbors, which illustrates his or her compactness with known accomplices:

<!-- b000140 | furniture | pages [7] -->
Team # 14531

<!-- b000141 | furniture | pages [7] -->
Page 6 of 19

<!-- b000143 | prose | pages [7] -->
the value is 1 if it connects with all the known conspirators and 0 means no conspirators is adjacent to it. The known suspicious clique obviously represents a compacter connectivity. Therefore, the more known conspirators being a node’s neighbors, the more possibly the node itself is a accomplice.

<!-- b000144 | prose | pages [7] -->
0 Gard 0.25 Derlene Tran 0.5 Harvey Ellin Yao 0.75 Alex Ulf 1 0.75 0.5 0.25 0 0 3 Paige Jean Chris Paul Jia Elsie

<!-- b000145 | prose | pages [7] -->
Este

<!-- b000146 | prose | pages [7] -->
Known conspirators 0 Known non-conspirators

<!-- b000147 | caption | pages [7] -->
Figure 2: Possession rate of neighboring accomplices distribution

<!-- b000148 | prose | pages [7] -->
• Number of current non-suspicious messages from the known con- spirators

<!-- b000149 | caption | pages [7] -->
Table 2.1 is the topics mentioned between known conspirators.1 It is obvi-

<!-- b000150 | prose | pages [7] -->
ous that a known conspirator rarely talks about irrelevant topics, i.e. topics irrelevant to their conspiracy, with his or her accomplices even though some unknown topics appear among them, which accounts for a very small propor- tion. If the information received from a known conspirator is most irrelevant, the receiver is much probably to be an outlier. So it is quite reasonable to take such argument as a feature.

<!-- b000151 | heading | pages [7] -->
2.2 Methods

<!-- b000152 | prose | pages [7] -->
We use the L-2 regularized logistic regression to model the probability of a node being involved in the conspiracy, and the parameters of the model are ob- tained by solving an optimization problem related to training set by gradient ascent algorithm.

<!-- b000153 | prose | pages [7] -->
1Topic No. 16 in the raw data is regarded as wrong and thus discarded.

<!-- b000154 | furniture | pages [8] -->
Team # 14531

<!-- b000155 | furniture | pages [8] -->
Page 7 of 19

<!-- b000156 | prose | pages [8] -->
Jean Alex Elsie Poul Ulf Yao Harvey 11⋆ Jean 8 14 13⋆ 11⋆ 3,7⋆ Alex 1 11⋆ 13⋆ Elsie 11⋆ 7⋆ 7⋆ Poul 4 7⋆, 11⋆, 13⋆ 13⋆ Ulf 13⋆ 7⋆, 11⋆, 13⋆ 7⋆,9 13⋆ 2, 7⋆ Yao 13⋆ Harvey

<!-- b000157 | caption | pages [8] -->
Table 1: Topics among known conspirators ( known conspiratorial topics are those

<!-- b000158 | prose | pages [8] -->
with star and highlighted in blue)

<!-- b000159 | heading | pages [8] -->
2.2.1 Logistic regression

<!-- b000160 | prose | pages [8] -->
We consider a training set of size m: {(x(1), y(1)), (x(2), y(2)), · · · , (x(m), y(m))}, where x(i) is an n-dimensional feature vector, and y(i) indicates the classiﬁcation of the agent, i.e. y(i) = 1 for conspirators and y(i) = 0 for non-conspirators. All the nodes in the training set are drawn from the 15 known conspirators and non- conspirators.

<!-- b000161 | prose | pages [8] -->
As a descendant of generalized linear model for Bernoulli distribution, logistic regression tries to estimate the probability of being a conspirators as 1 P(y = 1|x; θ) = hθ(x) = 1 + e−θT x, (4)

<!-- b000162 | prose | pages [8] -->
where θ ∈Rn is the parameter vector.

<!-- b000163 | prose | pages [8] -->
Then, under the framework of generalized linear model, the maximum a poste- riori (MAP) estimate of the parameter θ is given by

<!-- b000164 | prose | pages [8] -->
min J(θ), (5) θ where the cost function is given by m n ∑ ∑ J(θ) = 1 [−y(i) log(hθ(x)(i)) −(1 −y(i)) log(1 −hθ(x(i)))] + λ θ2 j, (6) m 2m i=1 j=1

<!-- b000165 | prose | pages [8] -->
with λ being the regularization parameter.

<!-- b000166 | heading | pages [8] -->
2.2.2 Gradient descent

<!-- b000167 | prose | pages [8] -->
The cost function J(θ) is minimized by using the algorithm of gradient descent, which always drives θ down the locally steepest slope, in hope to reach the global minimum of the cost function.

<!-- b000168 | prose | pages [8] -->
At every iteration before convergence, new θ is replaced by the old θ as

<!-- b000169 | prose | pages [8] -->
θ := θ −α∇θJ(θ), (7)

<!-- b000170 | prose | pages [8] -->
where α is a small positive constant.

<!-- b000171 | furniture | pages [9] -->
Team # 14531

<!-- b000172 | furniture | pages [9] -->
Page 8 of 19

<!-- b000173 | heading | pages [9] -->
2.2.3 Leave-one-out cross validation

<!-- b000174 | prose | pages [9] -->
As we are only informed of the correct classiﬁcation of 15 nodes, at a given round, we only use 14 of them as the training set, while leaving one out for cross validation (C-V). At every round, the next correctly classiﬁed node is left out and the others serve as the training set, then the trained hypothesis is tested on the left-out node. In this way, by averaging 15 rounds without overlapping, the error for both the training set and the cross validation set can be evaluated.

<!-- b000175 | prose | pages [9] -->
Supposing, for example, in the j-th round, sample (x(j), y(j)) is left out, and the training set is given by

<!-- b000176 | prose | pages [9] -->
Sj = {(x(l), y(l))|l = 1, 2, · · · , j −1, j + 1, · · · , 15}. (8)

<!-- b000177 | prose | pages [9] -->
Using this training set, parameter vector θ(j) is obtained, and the corresponding hypothesis is tested on both Sj and the left-out (x(j), y(j)), arriving at this round’s training error εSj and C-V error εj respectively.

<!-- b000178 | prose | pages [9] -->
Hence, by averaging them over j, the training error is given by

<!-- b000179 | prose | pages [9] -->
15 ∑ εS = 1 εSj, (9) 15 j=1

<!-- b000180 | prose | pages [9] -->
and the cross validation error is given by

<!-- b000181 | prose | pages [9] -->
15 ∑ ε = 1 εj. (10) 15 j=1

<!-- b000182 | heading | pages [9] -->
2.2.4 Selecting regularization parameter

<!-- b000183 | prose | pages [9] -->
The regularization parameter λ (λ > 0) is selected optimally as to minimize the cross validation error, i.e.

<!-- b000184 | prose | pages [9] -->
λ = arg min ε. (11) λ>0

<!-- b000185 | heading | pages [9] -->
2.3 Results

<!-- b000186 | prose | pages [9] -->
By training the logistic regression with our leave-one-out cross validation s- trategy, λ is optimally set to 1.9 and the overall C-V error ε = 0.27 (training error εS = 0). Then, while ﬁxing the chosen λ, the hypothesis is ﬁnally retrained on the maximum training set, making full use of every known conspirators and non-conspirators.

<!-- b000187 | prose | pages [9] -->
The trained hypothesis gives us the estimated probability for node i being a conspirator, resulting in a priority list of suspicious individuals, ranked in descent order of criminal likelihood. The top 10 suspicious are shown in Table 2, where managers are marked by a star (⋆).

<!-- b000188 | furniture | pages [10] -->
Team # 14531

<!-- b000189 | furniture | pages [10] -->
Page 9 of 19

<!-- b000190 | prose | pages [10] -->
Name Dolores ⋆ Crystal Jerome ⋆ Sherri Neal

<!-- b000191 | prose | pages [10] -->
Node No. 10 20 34 3 17

<!-- b000192 | prose | pages [10] -->
Probability of conspiracy 0.555 0.508 0.388 0.316 0.299

<!-- b000193 | prose | pages [10] -->
Name Christina Jerome William Dwight Beth

<!-- b000194 | prose | pages [10] -->
Node No. 47 16 50 28 38

<!-- b000195 | prose | pages [10] -->
Probability of conspiracy 0.267 0.252 0.245 0.242 0.233

<!-- b000196 | caption | pages [10] -->
Table 2: Top 10 in the priority list (known conspirators excluded)

<!-- b000197 | caption | pages [10] -->
Figure 3 illustrates the probability of criminal involvement estimated by hθ(x)

<!-- b000198 | prose | pages [10] -->
versus the corresponding rank in the priority list, where three managers (Jerome, Dolores and Gretchen)2 are marked by circles.

<!-- b000199 | prose | pages [10] -->
Dolores (manager) is indeed the person deserving highest suspicion, and Jerome (manager) is also likely to be involved in conspiracy.

<!-- b000200 | prose | pages [10] -->
1

<!-- b000201 | prose | pages [10] -->
0.9

<!-- b000202 | prose | pages [10] -->
All the members 0.8 Gretchen (manager) Jerome (manager) 0.7 Probability of being criminal Dolores (manager) 0.6

<!-- b000203 | prose | pages [10] -->
0.5

<!-- b000204 | prose | pages [10] -->
0.4

<!-- b000205 | prose | pages [10] -->
0.3

<!-- b000206 | prose | pages [10] -->
0.2

<!-- b000207 | prose | pages [10] -->
0.1

<!-- b000208 | prose | pages [10] -->
0 10 20 30 40 50 60 70 80 Rank in the priority list

<!-- b000209 | caption | pages [10] -->
Figure 3: Probability of conspiracy versus the corresponding rank in priority list

<!-- b000210 | prose | pages [10] -->
2As more than one nodes are named either Gretchen or Jerome, we select those with bigger out-degrees to be managers, i.e. Manager Gretchen is Node No. 32 and Manager Jerome is Node No. 34

<!-- b000211 | furniture | pages [11] -->
Team # 14531

<!-- b000212 | furniture | pages [11] -->
Page 10 of 19

<!-- b000213 | heading | pages [11] -->
2.4 Semantic model enhancement

<!-- b000214 | prose | pages [11] -->
When talking about enhancement of the accuracy, we should reduce the diﬀer- ence the performance with those who could deal with it more ﬂexibly and exactly: human being. A very important way we humans solve cases is analysis the com- munication contents including messages and records. However, just as aforemen- tioned, our ability so quite limited when handling huge amount of information that we have to utilize machine to help us. Therefore, semantical information is more important for humans rather than extremely complicated topology structure. For example,through analysis into the information in message traﬃc, we could discover several interesting and helpful phenomena.

<!-- b000215 | prose | pages [11] -->
As is in EZ case, Some similar text information in the dialog motivate us to discover that Inez represents some attributes that are quite similar to George, who is deﬁnitely a conspirator. For instance, the word “tired” when describing Inez and the word “stressed” when describing George. Similar case can be also found in the 83-people network case such as the word “Spanish” from known conspiratorial topic 7 is highly suspectable and appear in other unknown topis (e.g.topic 2 and 12) repeatedly. The contents about “computer security” which is treated as part of the key in the whole conspiracy also keep active in many other unknown topics like 5 and 15. Above relativity in information may easily cause humans’ vigilance. Hence it is natural to train a computer to ﬁnd a method that could measure similarities among topics and reveal some potential information.

<!-- b000216 | prose | pages [11] -->
Undetermined Message 1

<!-- b000217 | prose | pages [11] -->
suspicious Conspiratorial Message 1 Undetermined Message 2 word 1 suspicious word 2 Conspiratorial Message 2 Undetermined Message 3 suspicious word 3

<!-- b000218 | prose | pages [11] -->
Undetermined Message 4 suspicious Conspiratorial Message x word n Legend:

<!-- b000219 | prose | pages [11] -->
New conspiratorial Message Conspiratorial Undetermined Message m New non-conspiratorial Message Dictionary

<!-- b000220 | caption | pages [11] -->
Figure 4: Framework of topic semantic diﬀusion

<!-- b000221 | prose | pages [11, 12] -->
Lexical ambiguity broadly exists among words and they always contain diﬀerent meanings depending on particular scenarios. Therefore, it is not wise to abandon human intelligence and only depend on particular algorithms to crack a criminal case during the detection period. Detectors’ reasoning plays a indispensable role through out the entire process. Therefore, we draw the problem of topic semantic diﬀusion into a topic similarity measurement task based on expert dictionary. As seen in Figure 4, a conspiratorial dictionary is ﬁrstly constructed from the conspir- atorial messages about known suspicious topics. Resource allocation mechanism on bipartite network outperforms in extracting the hidden information of networks [Zhou, 2007], which is exploited by us to unfold the similarity among diﬀerent top- ics after a bipartite network is constructed (see Figure 4) between the conspiratorial dictionary and all the information in message traﬃc.

<!-- b000222 | furniture | pages [12] -->
Team # 14531

<!-- b000223 | furniture | pages [12] -->
Page 11 of 19

<!-- b000225 | prose | pages [12] -->
The bipartite network is modeled by G = (D, T, E). E is an edge set, indicating the relationship between key word set D of expert dictionary and topic set T , where D = d1, d2...dn and T = t1, t2...tm. Then, we arrange all the topics with 0 resource except each known conspiratorial topic with one unit of resource and commence with the ﬁrst allocation from set T to set D:

<!-- b000226 | prose | pages [12] -->
n ∑ ailf(di) f(tl) = D(di) . (12) i=1

<!-- b000227 | prose | pages [12] -->
Equation 12 expresses the calculation of the resource held by t(l) after the ﬁrst step : f(tl). D(di) indicates the degree of the node di and ail is deﬁnrd as follows:

<!-- b000228 | prose | pages [12] -->
{1, ditl ∈E ail = (13) 0, otherwise.

<!-- b000229 | prose | pages [12] -->
Intuitive explanation of step 1 is to arrange the resource averagely by degree of ti from T to D if ti owns resource. The second step is to reﬂect the resource ﬂow back to T from D obeying the same rule. So the resource ﬁnally locates on ti satisﬁes :

<!-- b000230 | prose | pages [12] -->
m m n ∑ ∑ ∑ ailf(dl) ail ajif(tj) ′(ti) = f D(dl) = D(tj) . (14) D(dl) j=1 l=1 l=1

<!-- b000231 | prose | pages [12] -->
After this two-fold method, the amount of resource held by every element in T could be seen as a score of similarity. The rank of all topics according to such score represents the degree of their similarity to the information from dictionary,i.e. the higher this score is, the topic is more likely to be a newly found conspiratorial topic.

<!-- b000232 | prose | pages [12] -->
Since we set D = {′spanish′,′ system′,′ network′,′ computer′,′ meeting′} as the conspiratorial dictionary, table 2.4 illustrates the ﬁnal result of all the 15 topics in 83-people network case. The known suspicious topic numbers 7,11,13, which is our fundamental basis for further development, are naturally to be top three and topic 5 is also very suspicious than other unknown topics. 2,12,15 are among the group with the second highest possibility in unknowns and the left ones tends to be irrelevant topics to the conspiracy.

<!-- b000233 | prose | pages [12, 13] -->
We then append topic 4 into the set of known conspiratorial topic set and train the model again, the overall C-V error decrease from former 0.27 to current value of 0.13. As the conﬁdence degree of topic 2,12,15 is low as shown in table 2.4, there is not obvious inﬂuence on the detection correctness. The limited resource and the impressive performance here indicate that if we absorb enough key words into Rank Topic Number Similarity to known suspicious topics 11⋆ 1 0.750 7⋆ 2 0.667 13⋆ 3 0.667 4 5 0.417 5 2 0.167 6 12 0.167 7 15 0.167 8 1,3,4,6,8,9,10,14 0

<!-- b000234 | furniture | pages [13] -->
Team # 14531

<!-- b000235 | furniture | pages [13] -->
Page 12 of 19

<!-- b000237 | caption | pages [13] -->
Table 3: Rank of all topics based on similarity to known suspicious topics.(known

<!-- b000238 | prose | pages [13] -->
conspiratorial topics are those with star and highlighted in blue)

<!-- b000239 | prose | pages [13] -->
conspiratorial dictionary and more topics with abundant contents, such method is much likely to perform better. However, when dealing with huge amounts of information, it will become a problem to get valuable words into dictionary as human wisdom become helpless.

<!-- b000240 | prose | pages [13] -->
On the other hand, if we utilize the speaker instead of the key words to con- struct a bipartite graph with the topics, we will also get similarity among topics based on speaker who transmit them. However, the determination of the relation- ship between diﬀerent results under these two standards, even more standards, is deﬁnitely beyond this paper.

<!-- b000241 | prose | pages [13] -->
After comprehending the actual meaning of the topics, we ﬁnd the rank result is quite reasonable and valuable. Meanwhile, it is not only its reliable result impresses us a lot, but also its high eﬃciency and low complexity of implementation will give it another good performance in huge amounts of data, for this method is only of linear time complexity O(n).

<!-- b000242 | heading | pages [13] -->
3 Identifying the leader of the conspiracy

<!-- b000243 | prose | pages [13] -->
Our machine learning scheme tries to estimate the likelihood of a node com- mitting conspiracy, however, the likelihood does not proportionally indicate the leadership inside the network, for the identiﬁcation of leaders is further complicat- ed by its topology.

<!-- b000244 | prose | pages [13] -->
Thus we adopt LeaderRank, a node ranking algorithm closely related to net- work topology, to ﬁnd the leader of the criminal group. Meanwhile, a subgraph connected by known suspicious topics is extracted from the network, in order to decouple the structure with company employees. Besides, because of its robust- ness against random noise, LeaderRank is also appropriate for addressing criminal network problems, which usually suﬀer from incompleteness and incorrectness.

<!-- b000245 | furniture | pages [14] -->
Team # 14531

<!-- b000246 | furniture | pages [14] -->
Page 13 of 19

<!-- b000247 | heading | pages [14] -->
3.1 LeaderRank

<!-- b000248 | prose | pages [14] -->
LeaderRank algorithm is a state-of-art achievement on node ranking, which is more tolerant of noisy data and robust against manipulations than more tradi- tional algorithms including HITS and PageRank [L¨u et al., 2011]. This method is mathematically equivalent to random walk mechanism on the directed network with adaptive probability, leading to a parameter-free algorithm readily applica- ble to any type of graph. A ground node, who connects with every node through newly added bidirectional links, is arranged into the topology in order to make the entire network a strongly connected one and hence the random walk will deﬁnitely converge into a homeostasis process.

<!-- b000249 | prose | pages [14] -->
For a graph G = (V, E), every node in the graph obtains 1 unit of resource except the ground node. After the commence of voting process, node i at step t will get an adaptive voting score ν(t) according to the voting from its neighbors:

<!-- b000250 | prose | pages [14] -->
|V |+1 ∑ µij νi(t + 1) = Dout(j)νi(t) (15) j=1

<!-- b000251 | prose | pages [14] -->
Where µij is a binary indicator with value 1 if node i points to j and 0 otherwise. Dout(j) denotes the out-degree of node j. The fraction of above two arguments could be considered as the probability that a random walker at i goes to j in the next step. Finally, the leadership score of node i is proved to be νi(Tc)+νgn(Tc)/|V |, where νgn(Tc) is the score of the ground node at steady state.

<!-- b000252 | heading | pages [14] -->
3.2 Suspicious topic sub-network extraction

<!-- b000253 | prose | pages [14] -->
As the criminal network in embedded in a network of company employees, we extract the sub-network GTS connected by suspicious topics only, so as to minimize the coupling of the company’s hierarchical structure to the conspiracy relations.

<!-- b000254 | prose | pages [14] -->
Supposing Tij denotes the set of topics mentioned by messages from node i to node j, and TS denotes the set of known suspicious topics (TS = {7, 11, 13}). Then GTS is the maximum subgraph of the original graph G, whereas

<!-- b000255 | prose | pages [14] -->
Tij ⊆TS, for all (i, j) ⊆ETS (16)

<!-- b000256 | heading | pages [14] -->
3.3 Edge reverse

<!-- b000257 | prose | pages [14] -->
Because the original LeaderRank deals with ﬁnding leaders in Internet social networks (SNS), where the direction of an edge has a dissimilar meaning from our case, i.e. if A points to (follows) B in twitter, then B is considered to be a leader of A. However, in our communication network, an edge pointing from A to B suggests A has sent B a message. Therefore, if assuming that a leader in a criminal network tends to be the sender of a message rather than receiver by issuing commands, then each edge in GTS has to be reversed to be compatible with LeaderRank’s original design. The reversed sub-network induced by suspicious topics is denoted by G′ TS.

<!-- b000258 | furniture | pages [15] -->
Team # 14531

<!-- b000259 | furniture | pages [15] -->
Page 14 of 19

<!-- b000260 | heading | pages [15] -->
3.4 Results

<!-- b000261 | prose | pages [15] -->
By running LeaderRank on G′ TS , a ranking score is assigned to every node in this subgraph, which generates a list of possible leaders ranked in descent order, as shown in Table 4.

<!-- b000262 | prose | pages [15] -->
Yao (node number 67) is ranked as the chief leader of the conspiracy organiza- tion.

<!-- b000263 | prose | pages [15] -->
Name LeaderRank score

<!-- b000264 | prose | pages [15] -->
Yao 2.67 Alex 2.21 Paul 1.92 Elsie 1.62

<!-- b000265 | caption | pages [15] -->
Table 4: Partial results of LeaderRank on G′

<!-- b000266 | prose | pages [15] -->
TS

<!-- b000267 | heading | pages [15] -->
3.5 Empirical support

<!-- b000268 | prose | pages [15] -->
Empirical analysis of criminal networks has found that a leader of a criminal or- ganization tends to carefully balancing his or her degree centrality and betweenness centrality. It has been proposed that the leader usually maintains a high between- ness centrality but a relatively low degree centrality, for enhancing eﬃciency and meanwhile ensuring safety [Morselli, 2010].

<!-- b000269 | prose | pages [15] -->
Known conspirators 20 High conspiracy prob.

<!-- b000270 | prose | pages [15] -->
Yao (inferred leader) 18

<!-- b000271 | prose | pages [15] -->
16 Degree centrality 14

<!-- b000272 | prose | pages [15] -->
12

<!-- b000273 | prose | pages [15] -->
10

<!-- b000274 | prose | pages [15] -->
8

<!-- b000275 | prose | pages [15, 16] -->
0.00 0.01 0.02 0.03 0.04 0.05 Betweenness centrality And our inference that Yao is the leader is thus empirically supported. Figure 5 illustrates the joint distribution of betweenness centrality CB and degree centrality (Din+Dout) for 7 known conspirators and 10 nodes with high conspiracy likelihood, where two dashed lines mark average values of the displayed nodes. Yao’s high betweenness centrality with relatively low degree centrality accord with the identity of a leader.

<!-- b000276 | caption | pages [15] -->
Figure 5: The joint distribution of betweenness centrality and degree centrality

<!-- b000277 | furniture | pages [16] -->
Team # 14531

<!-- b000278 | furniture | pages [16] -->
Page 15 of 19

<!-- b000280 | heading | pages [16] -->
3.6 Discussion

<!-- b000281 | prose | pages [16] -->
The leader of the criminal network is identiﬁed by performing LeaderRank on the extracted, edge-reversed, suspicious-topic-connected subgraph. And our ﬁndings are strengthened by empirical research results.

<!-- b000282 | prose | pages [16] -->
LeaderRank, as an algorithm that ranks nodes by performing source reallo- cation dynamics on the network, is generally more computationally inexpensive compared to traditional methods like block-modeling. Our scheme accommodates large databases with higher eﬃciency.

<!-- b000283 | heading | pages [16] -->
4 Evaluating the Model

<!-- b000284 | heading | pages [16] -->
4.1 Sensitivity analysis

<!-- b000285 | prose | pages [16] -->
Considering the usual incompleteness, imprecision and even inconsistency with criminal social networks [Xu, 2005], the method for inferring criminality or con- spiracy should be robust enough to cope with minor alternations of the network. Otherwise, small ﬂaws or incompleteness of the network would possibly lead to mistaken accusations or connivance of criminals. Therefore, a sensitivity analysis is performed for our approach.

<!-- b000286 | prose | pages [16] -->
Requirement 2 provides an appropriate scenario for such a test: while other conditions remain unchanged, new information indicates that Topic 1 is also con- nected to criminal activity, and Chris, who was considered innocent before, has now proved guilty.

<!-- b000287 | heading | pages [16] -->
4.1.1 Priority list

<!-- b000288 | prose | pages [16] -->
By applying our methods to these altered conditions, we ﬁnd out that among the top-10 of the previous priority list (7 known conspirator excluded), 7 of them are still top-10 holders of the current list, while the remaining three ﬁnd their new places at 12th, 14th and 16th respectively, as illustrated in Table 5.

<!-- b000289 | prose | pages [16] -->
A more sophisticated measurement of the sensitivity of priority list is Kendall’s tau coeﬃcient τ [Sen, 1968]. Given two priority lists {pk} = {p1, p2, · · · , pn} and {qk} = {q1, q2, · · · , qn} (for example, p2 = 5 means node 2 is ranked 5th by {pk} list), then (i, j), i̸ = j is said to be a concordant pair if their rankings agree in two lists, i.e. pi > pj, qi > qj or pi < pj, qi < qj; (i, j) is said to be a discordant pair if their rankings disagree in two lists.

<!-- b000290 | furniture | pages [17] -->
Team # 14531

<!-- b000291 | furniture | pages [17] -->
Page 16 of 19

<!-- b000292 | prose | pages [17] -->
Name Dolores Crystal Jerome Sherri Neal

<!-- b000293 | prose | pages [17] -->
Rank (previous) 1 2 3 4 5

<!-- b000294 | prose | pages [17] -->
Prob. of conspiracy (previous) 0.555 0.508 0.388 0.316 0.299

<!-- b000295 | prose | pages [17] -->
Rank (new) 2 1 6 9 3

<!-- b000296 | prose | pages [17] -->
Prob. of conspiracy (new) 0.621 0.629 0.405 0.393 0.504

<!-- b000297 | prose | pages [17] -->
Name Christina Jerome William Dwight Beth

<!-- b000298 | prose | pages [17] -->
Rank (previous) 6 7 8 9 10

<!-- b000299 | prose | pages [17] -->
Prob. of conspiracy (previous) 0.555 0.508 0.388 0.316 0.299

<!-- b000300 | prose | pages [17] -->
Rank (new) 14 5 4 12 16

<!-- b000301 | prose | pages [17] -->
Prob. of conspiracy (new) 0.335 0.407 0.409 0.352 0.334

<!-- b000302 | caption | pages [17] -->
Table 5: Change with top 10 in the priority list (known conspirators excluded)

<!-- b000303 | prose | pages [17] -->
Then Kendall’s tau is deﬁned as

<!-- b000304 | prose | pages [17] -->
τ = (number of concordant pairs) −(number of discordant pairs) . (17) 1 2n(n −1)

<!-- b000305 | prose | pages [17] -->
τ lies in the range of [−1, 1], whereas 1 for perfect ranking agreement, −1 for utter disagreement.

<!-- b000306 | prose | pages [17] -->
The Kendall’s tau between two priority lists obtained in Requirement 1 and Requirement 2 is τ = 0.86, justifying the robustness of the machine learning ap- proach.

<!-- b000307 | prose | pages [17] -->
If we assume those known conspirators and non-conspirators are independently wrongly classiﬁed with certain probability, then the expected value of τ between our computed priority list and the real priority list would vary with that probability.

<!-- b000308 | caption | pages [17] -->
Figure 6 depicts the expected Kendall’s tau versus the misclassiﬁcation probability

<!-- b000309 | prose | pages [17] -->
of conspirator set and non-conspiracy set separately.

<!-- b000310 | prose | pages [17] -->
As can be seen from Figure 6, even if the misclassiﬁcation error occurs with probability as big as 0.5, the Kendall’s tau does not drop below 0.80, substantially proving the inherent stability of our methods.

<!-- b000311 | heading | pages [17] -->
4.1.2 Probability inﬂation

<!-- b000312 | caption | pages [17] -->
Figure 7 illustrates the change with estimated conspiracy probability due to

<!-- b000313 | prose | pages [17] -->
modiﬁed conditions in Requirement 2, with the previous value as x-axis, and the new as y-axis. Generally, most nodes exhibit a small “inﬂation” in criminal prob- ability, as indicated by the distribution of dots skewed from the diagonal line. The augmented probability is compatible with the new information that expands both the set of suspicious topics and known conspirators.

<!-- b000314 | furniture | pages [18] -->
Team # 14531

<!-- b000315 | furniture | pages [18] -->
Page 17 of 19

<!-- b000316 | prose | pages [18] -->
1

<!-- b000317 | prose | pages [18] -->
0.98 Conspirators Non−conspirators 0.96

<!-- b000318 | prose | pages [18] -->
0.94

<!-- b000319 | prose | pages [18] -->
0.92 Kendall’s tau 0.9

<!-- b000320 | prose | pages [18] -->
0.88

<!-- b000321 | prose | pages [18] -->
0.86

<!-- b000322 | prose | pages [18] -->
0.84

<!-- b000323 | prose | pages [18] -->
0.82

<!-- b000324 | prose | pages [18] -->
0.8 0 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45 0.5 Probability of wrong classification

<!-- b000325 | caption | pages [18] -->
Figure 6: The expected Kendall’s tau declines as misclassiﬁcation probability in-

<!-- b000326 | prose | pages [18] -->
creases

<!-- b000327 | prose | pages [18] -->
1

<!-- b000328 | prose | pages [18] -->
0.9 Probability of being a conspirator (Requirement 2 ) 0.8

<!-- b000329 | prose | pages [18] -->
0.7

<!-- b000330 | prose | pages [18] -->
0.6

<!-- b000331 | prose | pages [18] -->
0.5

<!-- b000332 | prose | pages [18] -->
0.4 Training set Unknown nodes 0.3 Chris Gretchen (manager) Jerome (manager) 0.2 Dolores (manager) 0.1

<!-- b000333 | prose | pages [18] -->
0 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 Probability of being a conspirator (Requirement 1)

<!-- b000334 | caption | pages [18] -->
Figure 7: Criminal probabilities before and after the change of conditions

<!-- b000335 | prose | pages [18] -->
The analysis suggests that our machine learning method is insensitive to minor alternations with known conditions, while still able to produce new, reasonable results implied by newly introduced information.

<!-- b000336 | furniture | pages [19] -->
Team # 14531

<!-- b000337 | furniture | pages [19] -->
Page 18 of 19

<!-- b000338 | heading | pages [19] -->
5 Discussion and Conclusion

<!-- b000339 | heading | pages [19] -->
5.1 Summary

<!-- b000340 | prose | pages [19] -->
We draw the problem of predicting conspiracy in a company on a multi-feature machine learning problem. 5 features are selected for their representation of cen- trality in topology, conspiratorial level of connectivity and communication contents. Experimental results hits about 73% correct prediction rate in the basis model.

<!-- b000341 | prose | pages [19] -->
Then, we oﬀer an algorithm, which refers to resource allocation mechanism in bipartite graph, to reveal potential similarity among topics and discover new conspiratorial topics to feedback in the optimized learning process. Obvious en- hancement lead us to some deeper discursion about background of large data and extended standards for measuring similarity among topics.

<!-- b000342 | prose | pages [19] -->
In the following section, Revised LeaderRank scheme is proposed in searching for the leader, required by DA. We additionally validate our result from aspects on the topology property of a criminal leader.

<!-- b000343 | prose | pages [19] -->
Finally, the high value of Kendall’s tau illustrates the nonsensitive property of the model. The weakness of our model is mainly about features. Diﬀerent networks may not share the same features. Thereby the features of particular network may become meaningless when type of network changes. Furthermore, large amounts of information might seriously limit the capability of the resource allocation strategy because the construction of bipartite graph itself becomes a problem when facing with too much noise information.

<!-- b000344 | heading | pages [19] -->
5.2 Further discussion

<!-- b000345 | prose | pages [19] -->
When taking about the good portability of a model on diﬀerent models, we could focus on two aspects: the similarity of two networks and diﬀerence. Some common pattern appeared in diﬀerent kinds of networks,including biological network, are the small-world property, power-law degree distributions, network transitivity and community structure [Girvan, 2001]. Either topology or transmission properties shared by diﬀerent networks could help to build a model with good portability.

<!-- b000346 | prose | pages [19] -->
However, on the other hand, the fundamental diﬀerence in mechanism of in- formation transmission decides the distinguishing models: people ﬁnd out clues through evidence or relative materials to break down the invisibility of a criminal network based on reasoning and deduction. Even though share some similar prop- erties, individuals in other networks like some biological networks communicate with each other under some relatively ﬁxed principles or unchangeable pattern for division of work. The co-occurrence-based approaches always fail to characterize biological interactions [Chen & Sharp, 2004], where particular dynamics function of analytical model might perform better like utilizing revised infectious disease model to predict disfunction or diseased biological components.

<!-- b000347 | furniture | pages [20] -->
Team # 14531

<!-- b000348 | furniture | pages [20] -->
Page 19 of 19

<!-- b000349 | heading | pages [20] -->
References

<!-- b000350 | references | pages [20] -->
[Baker & Faulkner, 1993] Baker, W. E. & Faulkner, R. R. (1993).

<!-- b000351 | references | pages [20] -->
The Social

<!-- b000352 | references | pages [20] -->
Organization of Conspiracy: Illegal Networks in the Heavy Electrical Equipment

<!-- b000353 | references | pages [20] -->
Industry.

<!-- b000354 | references | pages [20] -->
[Chen & Sharp, 2004] Chen, H. & Sharp, B. M. (2004). Content-rich biological

<!-- b000355 | references | pages [20] -->
network constructed by mining PubMed abstracts.. BMC bioinformatics 5, 147.

<!-- b000356 | references | pages [20] -->
[Freeman, 1979] Freeman, L. (1979). Centrality in social networks conceptual clar-

<!-- b000357 | references | pages [20] -->
iﬁcation. Social networks.

<!-- b000358 | references | pages [20] -->
[Girvan, 2001] Girvan, M. (2001). Community structure in social and biological

<!-- b000359 | references | pages [20] -->
networks. PNAS.

<!-- b000360 | references | pages [20] -->
[Krebs, 2002] Krebs, V. E. (2002). Mapping Networks of Terrorist Cells. 24(3),

<!-- b000361 | references | pages [20] -->
43–52.

<!-- b000362 | references | pages [20] -->
[L¨u et al., 2011] L¨u, L., Zhang, Y.-C., Yeung, C. H., & Zhou, T. (2011). Leaders

<!-- b000363 | references | pages [20] -->
in social networks, the Delicious case.. PloS one 6(6), e21202.

<!-- b000364 | references | pages [20] -->
[Morselli, 2010] Morselli, C. (2010). Assessing Vulnerable and Strategic Positions

<!-- b000365 | references | pages [20] -->
in a Criminal Network. Journal of Contemporary Criminal Justice 26(4), 382–

<!-- b000366 | references | pages [20] -->
392.

<!-- b000367 | references | pages [20] -->
[Sabidussi, 1966] Sabidussi, G. (1966). The centrality index of a graph. Psychome-

<!-- b000368 | references | pages [20] -->
trika.

<!-- b000369 | references | pages [20] -->
[Sen, 1968] Sen, K. P. (1968).

<!-- b000370 | references | pages [20] -->
Estimates of the regression coeﬃcient based on

<!-- b000371 | references | pages [20] -->
Kendall’s tau. Journal of the American Statistical Association.

<!-- b000372 | references | pages [20] -->
[Wheat, 2007] Wheat, C. (2007). Algorithmic Complexity and Structural Models

<!-- b000373 | references | pages [20] -->
of Social Networks. Management , 1–38.

<!-- b000374 | references | pages [20] -->
[Xu, 2005] Xu, J. (2005). Criminal network analysis and visualization. Communi-

<!-- b000375 | references | pages [20] -->
cations of the ACM 48(6).

<!-- b000376 | references | pages [20] -->
[Xu & Chen, 2003] Xu, J. & Chen, H. (2003). Untangling Criminal Networks : A

<!-- b000377 | references | pages [20] -->
Case Study. World Trade , 232–248.

<!-- b000378 | references | pages [20] -->
[Zhou, 2007] Zhou, T. (2007). Bipartite network projection and personal recom-

<!-- b000379 | references | pages [20] -->
mendation. Physical Review E 76(4), 1–7.
