# P-C-2012-16075-4bbf9219

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team#16075

<!-- b000002 | furniture | pages [1] -->
Page 1 of 20

<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | title | pages [1] -->
Extended Criminal Network Analysis Model

<!-- b000005 | title | pages [1] -->
Allows Conspirators Nowhere to Hide

<!-- b000006 | heading | pages [1] -->
Abstract

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
High-tech conspiracy crimes arouse increasing attention of people in recent years. A particular challenging problem in conspiracy crime investigation is modeling to identify the conspirators in a group people.

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | prose | pages [1] -->
For the first requirement, based on graph theory, focusing on the problem from node-level and link-level, extending criminal network analysis model is established by us to prioritize persons in a network. The EZ case is applied to verify the our model. Computational result shows that Dave, George, Carol, Harry and Inez are identified as conspirators, which is consistent to the analysis of supervisor. The misjudgment rate of our model is 20%, and it is pretty stable. In the 83 workers, 23 persons including 7 known conspirators are discriminated as conspirators and Elsie is identified as leader or the criminal gang. Considering the position of Gretchen into the model only has slight influence to the result. Comparison between Fisher linear discrimination and our model is presented and the result shows the superiority of our model in several aspects.

<!-- b000011 | furniture | pages [1] -->


<!-- b000012 | prose | pages [1] -->
For the second requirement, when topic 1 are considered as suspicious question and Chris converts to be conspirator, recalculation of the model indicates that 28 conspirators are identified as conspirators, 21.7% more than the original network.

<!-- b000013 | furniture | pages [1] -->


<!-- b000014 | prose | pages [1] -->
For the third requirement, text analysis is employed to enhance our model. We divide suspicious information into four aspects indicating the meaning about crime. After changing the suspicious weight of topics, the model is computed again. The result shows that the number of conspirators rises to 28, 21.7% more than the former result while the leader of the criminal gang is still Elsie. The result also indicates that the likelihood of every person improves average 20%.

<!-- b000015 | prose | pages [1] -->
Furthermore, in-depth analysis is performed. The result shows link among conspirators is quite closely; Conspirators communicate with each other directly without passing through intermediate nodes. A primary conspirator will conduct many activities related to the conspiracy inevitably.

<!-- b000016 | prose | pages [1] -->
Finally, the strengths and weakness of the model are discussed, and the future work is pointed out.

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | furniture | pages [2] -->
Team#16075

<!-- b000021 | furniture | pages [2] -->
Page 2 of 20

<!-- b000022 | furniture | pages [2] -->


<!-- b000023 | furniture | pages [2] -->


<!-- b000024 | prose | pages [2] -->
1 Introduction ........................................................................................ 1

<!-- b000025 | prose | pages [2] -->
1.1 Problem Background .................................................................................. 1

<!-- b000026 | prose | pages [2] -->
1.2 Our Work ..................................................................................................... 1

<!-- b000027 | prose | pages [2] -->
2 General Assumptions ........................................................................ 2

<!-- b000028 | prose | pages [2] -->
3 Notations and Symbol Description .................................................. 2

<!-- b000029 | prose | pages [2] -->
3.1 Notations ..................................................................................................... 2

<!-- b000030 | prose | pages [2] -->
3.2 Symbol Description ..................................................................................... 3

<!-- b000031 | prose | pages [2] -->
4 Expanding Criminal Network Analysis Model................................. 3

<!-- b000032 | prose | pages [2] -->
4.1 Analysis of Question ................................................................................... 3

<!-- b000033 | prose | pages [2] -->
4.2 Establishment of ECNAM............................................................................ 4

<!-- b000034 | prose | pages [2] -->
4.3 Solution ....................................................................................................... 9

<!-- b000035 | prose | pages [2] -->
4.4 Fisher Discrimination and ECNAM ............................................................ 10

<!-- b000036 | prose | pages [2] -->
5 New Clues Discovered .................................................................... 12

<!-- b000037 | prose | pages [2] -->
6 Refined by Semantic Network Analysis ........................................ 12

<!-- b000038 | prose | pages [2] -->
6.1 Introduction of Semantic and Text Analyses .............................................. 13

<!-- b000039 | prose | pages [2] -->
6.2 Application of Text Analysis in ECNAM ..................................................... 13

<!-- b000040 | prose | pages [2] -->
6.3 Comparison and Analysis.......................................................................... 14

<!-- b000041 | prose | pages [2] -->
7 Simulation and Analysis.................................................................. 15

<!-- b000042 | prose | pages [2] -->
7.1 Depth analysis: characteristics of conspirators‘ activities .......................... 15

<!-- b000043 | prose | pages [2] -->
7.2 Simulation: The promotion of the model.................................................... 19

<!-- b000044 | prose | pages [2] -->
8 Strengths and Weaknesses ............................................................ 20

<!-- b000045 | prose | pages [2] -->
8.1 Strengths:.................................................................................................. 20

<!-- b000046 | prose | pages [2] -->
8.2 Weaknesses: ............................................................................................ 20

<!-- b000047 | prose | pages [2] -->
8.3 Future work: .............................................................................................. 20

<!-- b000048 | prose | pages [2] -->
9 References ........................................................................................ 20

<!-- b000049 | furniture | pages [2] -->


<!-- b000050 | furniture | pages [2] -->


<!-- b000051 | furniture | pages [3] -->
Team#16075

<!-- b000052 | furniture | pages [3] -->
Page 1 of 20

<!-- b000053 | furniture | pages [3] -->


<!-- b000054 | heading | pages [3] -->
1 Introduction

<!-- b000055 | prose | pages [3] -->
In recent years, with the means of crime becoming increasingly high-tech, cracking a criminal case becomes more complicated and difficult. A particularly challenging problem in high-tech crime is strategizing to identify members of a gang of high-tech crime as accurate as possible. However, no matter how skillful the criminal means is, there are always ways to find clues and solve crimes. One of the most effective ways to identify the members of a conspiracy is through analysis of large database such as message traffic—the theme of this paper.

<!-- b000056 | furniture | pages [3] -->


<!-- b000057 | prose | pages [3] -->
In this problem, there are 82 workers in a company. It is known that 7 persons of them are conspirators and 8 of them are non-conspirators. We are also informed the topics and the nature of these topics. The objective of us is modeling to identify people in the office complex who are the most likely conspirators and the leader of them based on the message traffic. This problem encompasses the following two questions:

<!-- b000058 | prose | pages [3] -->
 Given a group of people and relevant information, identify the conspirators.

<!-- b000059 | prose | pages [3] -->
 Given a criminal gang and message traffic, figure out the leader.

<!-- b000060 | heading | pages [3] -->
1.1 Problem Background

<!-- b000061 | prose | pages [3] -->
This problem could be regarded as a criminal network problem. A criminal network is primarily a social network in which person connects by relationships such as kindred, friendship and so on. Most of the efforts solving criminal network have been directed at analyzing the structural properties of criminal network by social network analysis (SNA) as done in [1] and [2]. Traditional approaches to criminal analysis put emphasis on nodes while U.K. Wiil et. al. in [3] posits an model to analyze the importance of links, which represents the security and efficiency of communication.

<!-- b000062 | furniture | pages [3] -->


<!-- b000063 | prose | pages [3] -->
Although it is promising, restricted by the imperfectness of itself, criminal analysis faces some challenges as follows:

<!-- b000064 | prose | pages [3] -->
 It does not take into account the significance and specific meaning of the

<!-- b000065 | prose | pages [3] -->
message. How about the message represents different meaning?

<!-- b000066 | prose | pages [3] -->
 The direction of message transmission is also ignored. All criminal gangs

<!-- b000067 | prose | pages [3] -->
have their own hierarchies. Isn‘t it should be differentiated between varying message?

<!-- b000068 | prose | pages [3] -->
 All the people in the network are conspirators, how to analyze the network that

<!-- b000069 | prose | pages [3] -->
some individuals in it are non-conspirators?

<!-- b000070 | prose | pages [3] -->
Hence, the criminal network remains to be completed to be more powerful.

<!-- b000071 | heading | pages [3] -->
1.2 Our Work

<!-- b000072 | furniture | pages [3] -->


<!-- b000073 | prose | pages [3] -->
Noticing that there are some problems in the attached data, we deal with them as the follows way:

<!-- b000074 | prose | pages [3] -->
 The name ‗Delores‘ is mistaken for ‗Dolores‘ in the name list. For the sake of

<!-- b000075 | prose | pages [3] -->
consistency, Dolores and Delores represent the same person.

<!-- b000076 | furniture | pages [3] -->


<!-- b000077 | furniture | pages [4] -->
Team#16075

<!-- b000078 | furniture | pages [4] -->
Page 2 of 20

<!-- b000079 | furniture | pages [4] -->


<!-- b000080 | prose | pages [4] -->
 There five groups of people with the same name in the message traffic and Elsie is one of them. Since Elsie is a known conspirator, we make a decision that Elsie whose number is 7 is a conspirator and the other remains to be seen.

<!-- b000081 | prose | pages [4] -->
 There is a strange message that node 3 talked to himself in the message traffic. We think that this record should be deleted.

<!-- b000082 | furniture | pages [4] -->


<!-- b000083 | prose | pages [4] -->
Our primary goal is to identify all the conspirators from the 83 workers, prioritize the suspects and figure out the leader of this criminal gang. As for this requirement, two models are established to meet it. On the one hand, adapting criminal analysis, we will give a priority list and determine the conspirators with an index; on the other hand, Fisher Discrimination is employed to compartmentalize into two groups – suspects and innocence, and then, the priority list is obtained according to the value of discriminant function. A secondary goal is to take into different actual conditions and analyze the influence of these modifications via new results. The last goal is to discover the impact of semantic network analysis and text analysis to our model. We will argue that this work is really helpful to our model.

<!-- b000084 | prose | pages [4] -->
This paper is organized as follows. First, combining with information in node-level and link-level, we present the Expanding Criminal Analysis model to prioritize the all the workers, point out the leader and identify all the conspirators. Next, the parameters of model are modified and semantic network analysis are added into the model to fulfill requirement two and three. Then, we compare our model with a model based on Fisher discrimination. Finally, we will promote our model to solve a similar problem in other field.

<!-- b000085 | heading | pages [4] -->
2 General Assumptions

<!-- b000086 | prose | pages [4] -->
 All the messages and the topics represent their thoughts, ignoring that someone

<!-- b000087 | prose | pages [4] -->
lies during the eavesdropping..  The likelihood of people who talks about suspicious topics will increase.

<!-- b000088 | prose | pages [4] -->
 The likelihood of people who communicates with known conspirators will

<!-- b000089 | prose | pages [4] -->
increase.  The known conspirators occupy important position in the group so that we can

<!-- b000090 | prose | pages [4] -->
take them as the criteria.

<!-- b000091 | heading | pages [4] -->
3 Notations and Symbol Description

<!-- b000092 | heading | pages [4] -->
3.1 Notations

<!-- b000093 | prose | pages [4] -->
To describe this problem clearly and explicitly, several terminologies [5] in graph theory and some notations defined in this paper are perform as follows:

<!-- b000094 | prose | pages [4] -->
Degree: The number of other points to which a given point is adjacent. It is the index of its potential communication activity.

<!-- b000095 | prose | pages [4] -->
Betweenness: The number of the shortest-path which passes through a given point in a network. It denotes the extent to which a particular node lies between other nodes in a network.

<!-- b000096 | prose | pages [4] -->
Closeness: the sum of the length of shortest-paths between a given point and all the

<!-- b000097 | furniture | pages [4] -->


<!-- b000098 | furniture | pages [5] -->
Team#16075

<!-- b000099 | furniture | pages [5] -->
Page 3 of 20

<!-- b000100 | furniture | pages [5] -->


<!-- b000101 | prose | pages [5] -->
other points in a network. It indicates how easily an individual connects to other members.

<!-- b000102 | prose | pages [5] -->
Centrality: a vector is made up of Degree, Betweenness and Closeness. It represents the significance of a specific point in a network.

<!-- b000103 | prose | pages [5] -->
Criminal Information Content (CIC): the weighted sum of all edges connected to a given point. It indicates the amount of criminal information of a member.

<!-- b000104 | heading | pages [5] -->
3.2 Symbol Description

<!-- b000105 | heading | pages [5] -->
Symbol

<!-- b000106 | prose | pages [5] -->
Description

<!-- b000107 | prose | pages [5] -->
v Denotes the number of node

<!-- b000108 | prose | pages [5] -->
d ( ) v Denotes the degree of node v in the network d

<!-- b000109 | prose | pages [5] -->
d v ( ) Denotes the betweenness of node v in the network b

<!-- b000110 | prose | pages [5] -->
cd v ( ) Denotes the closeness of node v in the network

<!-- b000111 | prose | pages [5] -->
sd v ( ) Denotes the Centrality of node v in the network

<!-- b000112 | prose | pages [5] -->
W v ( ) Denotes the suspect information of node v carried

<!-- b000113 | prose | pages [5] -->
S v ( ) Denotes the final score of node v

<!-- b000114 | prose | pages [5] -->
Denotes the misjudgment rate of the invest case R

<!-- b000115 | furniture | pages [5] -->


<!-- b000116 | furniture | pages [5] -->


<!-- b000117 | furniture | pages [5] -->


<!-- b000118 | furniture | pages [5] -->


<!-- b000119 | furniture | pages [5] -->


<!-- b000120 | furniture | pages [5] -->


<!-- b000121 | caption | pages [5] -->
Table 1: Symbol description

<!-- b000122 | heading | pages [5] -->
4 Expanding Criminal Network Analysis Model

<!-- b000123 | prose | pages [5] -->
Our main goal here is to build a model to complete the first task—prioritize the 83 office workers in the same company by likelihood of being part of the conspiracy. In this section, drawing lessons from previous research results, we will analyze this question at first. Next, combining node and link information of a network, expanding criminal network analysis model (ECNAM) is established based on SNA. Then, we will determine the parameters one by one and work out the solution of this question. At last, comparison of results between our model and Fisher Discrimination is presented to demonstrate the superiority of our model.

<!-- b000124 | heading | pages [5] -->
4.1 Analysis of Question

<!-- b000125 | prose | pages [5] -->
In this question, we are required to prioritize the rest 68 workers and determine the leader. According to the information we have known, this question can be boiled down to an extending criminal network problem. To solve it, we can define indices to assess the probability of an unknown worker to be identified as a conspirator and prioritize remaining workers by the probability.

<!-- b000126 | prose | pages [5] -->
The indices can be determined from two angles: network and practical viewpoint. Firstly, since this problem can be extracted as a social network problem, from the graph theory perspective, we can consider several indices mentioned in [5]: degree, betweenness and closeness. In this view, more attention is paid to the function of nodes in a network, thus, we call it node – level. There is a lot of model concerned

<!-- b000127 | furniture | pages [5] -->


<!-- b000128 | furniture | pages [6] -->
Team#16075

<!-- b000129 | furniture | pages [6] -->
Page 4 of 20

<!-- b000130 | furniture | pages [6] -->


<!-- b000131 | prose | pages [6] -->
about node-level, so we can adapt these models to describe this part of our model.

<!-- b000132 | furniture | pages [6] -->


<!-- b000133 | caption | pages [6] -->
Figure 1: An overview of the network, red nodes are known conspirators, red

<!-- b000134 | prose | pages [6] -->
edges represent suspicious message traffic

<!-- b000135 | prose | pages [6] -->
Secondly, in the view of practical question, it is not difficult to realize that the probability of an unknown worker to be identified as a conspirator can be determined by his topics, conversationalist, and the conversation‘s direction. For the edge of a network denotes the information flow in the network between varying nodes. Brief comparison reveals that the type of topic can be represented by the weight of the edge; the conversationalist can be regarded as node to which a given node points; the conversation‘s direction can be looked as the direction of an edge. Hence, analyzing from this view can be called as link-level. Because no paper we found studies the similar problem, we have to define metrics and solve it by ourselves.

<!-- b000136 | prose | pages [6] -->
From the two aspects—node-level and link-level, this question can be considered comprehensively. Finally, the model can be built according to the proper combination of the two aspects.

<!-- b000137 | heading | pages [6] -->
4.2 Establishment of ECNAM

<!-- b000138 | prose | pages [6] -->
From the previous analysis, there are two parts in our model. To describe the problem more clearly and conveniently, the establishment of our model will be divided into node-level and link-level, which will be explained in detailed in what follows.

<!-- b000139 | heading | pages [6] -->
4.2.1 Node-level

<!-- b000140 | prose | pages [6] -->
Extending of limitation

<!-- b000141 | prose | pages [6] -->
Centrality is often used to indicate the importance of a node within a network. In brief, the bigger centrality of a node, the more significant the node is. In a criminal network, the leader can be determined directly by centrality. In this paper, centrality also denotes the importance of a worker, big centrality represents high position. But what we have to explain is that this ―position‖ does not stand for the position in the criminal gang.

<!-- b000142 | furniture | pages [6] -->


<!-- b000143 | furniture | pages [7] -->
Team#16075

<!-- b000144 | furniture | pages [7] -->


<!-- b000145 | furniture | pages [7] -->
Page 5 of 20

<!-- b000146 | prose | pages [7] -->
A criminal network is constructed with nodes, links and groups. There exist many researches directed to criminal networks. Most of them focus on the detection and description of node level and group level, while some other put emphasis on the importance of link. However, all of them do not fit for this question for the reasons as follows.

<!-- b000147 | prose | pages [7] -->
 All the people in the network have been identified as criminals. However, the

<!-- b000148 | prose | pages [7] -->
network is a mixture of suspects, innocence and unidentified persons in this issue.

<!-- b000149 | prose | pages [7] -->
 The information transmitted between them is undirected while it has direction

<!-- b000150 | prose | pages [7] -->
in this question.

<!-- b000151 | prose | pages [7] -->
 The links in the network of those papers represent the same meaning while

<!-- b000152 | prose | pages [7] -->
the edges in our network have different implications such as suspicious topics and normal topics.

<!-- b000153 | prose | pages [7] -->
 The importance of a node in those networks only depends on centrality,

<!-- b000154 | prose | pages [7] -->
whereas the node‘s importance in our network not only impacted by its own position, but also by the characteristics of links connects to it.

<!-- b000155 | prose | pages [7] -->
Although none of these studies fit this problem completely, the solution of this question can refer to these researches. To deal with these differences, our model extends the model of criminal network analysis in following key ways:

<!-- b000156 | prose | pages [7] -->
 All the workers in the network can be looked as suspicious conspirators. Only

<!-- b000157 | prose | pages [7] -->
difference between them is the probability of suspicious conspirator. For identified suspects, the probability is 1; for innocence, the probability is 0; for the undetermined workers, the probability is between 0 and 1, which remains to make certain. The suspects and innocence can be looked as special suspicious conspirators as straight line can be looked as special curve.

<!-- b000158 | prose | pages [7] -->
 We can ignore the direction of communication in this condition. In this network,

<!-- b000159 | prose | pages [7] -->
communication between them means that there is relation between them. Moreover, the flow of information is bidirectional, no matter initiator of the conversation.

<!-- b000160 | prose | pages [7] -->
According to these modifications, the social network analysis model based on SNA can be used to describe the relationship of nodes in this specific network. However, the node-level does not involve all the information of this network, so the centrality of this model is different to the original ―centrality‖.

<!-- b000161 | prose | pages [7] -->
The Computation of Centrality

<!-- b000162 | prose | pages [7] -->
Three measures of centrality are commonly used in network analysis: degree, closeness and betweenness. All of these were defined in model from Freeman [1979].

<!-- b000163 | prose | pages [7] -->
Degree measures how active a particular node is. It is defined as the number of

<!-- b000164 | furniture | pages [7] -->


<!-- b000165 | prose | pages [7] -->
direct links a node v has. A high degree of a worker has means that this worker communicates frequently with other workers in the office. We therefore use this measure to represent a worker‘s activeness. The measure can be written:

<!-- b000166 | prose | pages [7] -->
n

<!-- b000167 | prose | pages [7] -->
 

<!-- b000168 | furniture | pages [7] -->


<!-- b000169 | prose | pages [7] -->
d

<!-- b000170 | prose | pages [7] -->
( )

<!-- b000171 | prose | pages [7] -->
v

<!-- b000172 | prose | pages [7] -->
d

<!-- b000173 | prose | pages [7] -->


<!-- b000174 | prose | pages [7] -->
i

<!-- b000175 | prose | pages [7] -->
1

<!-- b000176 | prose | pages [7] -->
v is the degree of a network; d ( ) Where d

<!-- b000177 | prose | pages [7] -->


<!-- b000178 | furniture | pages [7] -->


<!-- b000179 | prose | pages [7] -->
a i v

<!-- b000180 | prose | pages [7] -->
( , )

<!-- b000181 | prose | pages [7] -->
i v

<!-- b000182 | prose | pages [7] -->
a i v is a binary variables, when there is link ( , ) a i v , otherwise, between node i and nodev , ( , ) 1

<!-- b000183 | furniture | pages [7] -->


<!-- b000184 | prose | pages [7] -->
a i v  . n is the number of nodes ( , ) 0

<!-- b000185 | furniture | pages [8] -->
Team#16075

<!-- b000186 | furniture | pages [8] -->


<!-- b000187 | prose | pages [8] -->
in the network.

<!-- b000188 | furniture | pages [8] -->
Page 6 of 20

<!-- b000189 | prose | pages [8] -->
Considering that the size of the network might change, to compare the centrality

<!-- b000190 | furniture | pages [8] -->


<!-- b000191 | prose | pages [8] -->
of different graph, normalized measure can be derived:

<!-- b000192 | prose | pages [8] -->
n

<!-- b000193 | prose | pages [8] -->
  

<!-- b000194 | furniture | pages [8] -->


<!-- b000195 | prose | pages [8] -->
i

<!-- b000196 | prose | pages [8] -->
1

<!-- b000197 | prose | pages [8] -->
d

<!-- b000198 | prose | pages [8] -->
( )

<!-- b000199 | prose | pages [8] -->
v

<!-- b000200 | prose | pages [8] -->
d

<!-- b000201 | prose | pages [8] -->
n a i v

<!-- b000202 | prose | pages [8] -->
( , )

<!-- b000203 | prose | pages [8] -->


<!-- b000204 | furniture | pages [8] -->


<!-- b000205 | prose | pages [8] -->
(4-1)

<!-- b000206 | prose | pages [8] -->
i v

<!-- b000207 | prose | pages [8] -->
 

<!-- b000208 | prose | pages [8] -->
1

<!-- b000209 | prose | pages [8] -->
Betweenness measures the extent to which a given node lies between other

<!-- b000210 | furniture | pages [8] -->


<!-- b000211 | prose | pages [8] -->
nodes in a network. The betweenness of a node v equals the number of the shortest-paths between two nodes passing through it. A worker with higher betweenness means that more information flows through him. Thus betweenness can be used to represent the importance of a worker in information transmitting in a network. Considering again the change of network‘s size, we can obtain that:

<!-- b000212 | prose | pages [8] -->
n n n

<!-- b000213 | prose | pages [8] -->
 

<!-- b000214 | furniture | pages [8] -->


<!-- b000215 | prose | pages [8] -->
d v

<!-- b000216 | prose | pages [8] -->
( )

<!-- b000217 | prose | pages [8] -->
b

<!-- b000218 | prose | pages [8] -->
d is the betweenness of nodev ; Where b

<!-- b000219 | prose | pages [8] -->
g

<!-- b000220 | prose | pages [8] -->
( )

<!-- b000221 | prose | pages [8] -->
v

<!-- b000222 | prose | pages [8] -->
ij

<!-- b000223 | prose | pages [8] -->
  

<!-- b000224 | prose | pages [8] -->
i i

<!-- b000225 | prose | pages [8] -->
1 1

<!-- b000226 | prose | pages [8] -->
j

<!-- b000227 | prose | pages [8] -->
1

<!-- b000228 | furniture | pages [8] -->


<!-- b000229 | prose | pages [8] -->
(4-2)

<!-- b000230 | prose | pages [8] -->


<!-- b000231 | prose | pages [8] -->
2

<!-- b000232 | prose | pages [8] -->
( (

<!-- b000233 | prose | pages [8] -->
n

<!-- b000234 | prose | pages [8] -->
1)

<!-- b000235 | prose | pages [8] -->
v is a binary variable, denotes whether g g ( ) ij the shortest path of node i and j passes through nodev ; n is the number of nodes in a network.

<!-- b000236 | prose | pages [8] -->
Closeness measures the sum of the length of shortest paths between a particular node v and all the other nodes in a network. It represents the tightness of the net around the nodes. A higher closeness of nodes means that faster speed of information transfer. After normalization, the measure can be expressed as:

<!-- b000237 | prose | pages [8] -->
n

<!-- b000238 | prose | pages [8] -->
  

<!-- b000239 | prose | pages [8] -->
i

<!-- b000240 | prose | pages [8] -->
1

<!-- b000241 | prose | pages [8] -->
d v

<!-- b000242 | prose | pages [8] -->
( )

<!-- b000243 | furniture | pages [8] -->


<!-- b000244 | prose | pages [8] -->
c

<!-- b000245 | prose | pages [8] -->
(

<!-- b000246 | prose | pages [8] -->
n l i v

<!-- b000247 | prose | pages [8] -->
( , )

<!-- b000248 | prose | pages [8] -->


<!-- b000249 | prose | pages [8] -->
i v

<!-- b000250 | furniture | pages [8] -->


<!-- b000251 | prose | pages [8] -->
(4-3)

<!-- b000252 | prose | pages [8] -->
 

<!-- b000253 | prose | pages [8] -->
2

<!-- b000254 | prose | pages [8] -->
1)

<!-- b000255 | prose | pages [8] -->
l i v denotes the length of shortest-path between nodei and nodev . n is the Where ( , ) number of the nodes in the network.

<!-- b000256 | prose | pages [8] -->
Centrality consists of Degree, Betweenness and Closeness. There are various

<!-- b000257 | furniture | pages [8] -->


<!-- b000258 | prose | pages [8] -->
definitions of centrality, but all centralities are similar. Combining with equation (4-1) (4-2) and (4-3) here we choose one common definition of them:

<!-- b000259 | prose | pages [8] -->
d

<!-- b000260 | prose | pages [8] -->


<!-- b000261 | furniture | pages [8] -->


<!-- b000262 | prose | pages [8] -->
d v

<!-- b000263 | prose | pages [8] -->
( )

<!-- b000264 | prose | pages [8] -->
s

<!-- b000265 | heading | pages [8] -->
4.2.2 Link-level

<!-- b000266 | prose | pages [8] -->


<!-- b000267 | prose | pages [8] -->
( )

<!-- b000268 | prose | pages [8] -->
v d v

<!-- b000269 | prose | pages [8] -->
( )

<!-- b000270 | furniture | pages [8] -->


<!-- b000271 | prose | pages [8] -->
(4-4)

<!-- b000272 | prose | pages [8] -->
d d b

<!-- b000273 | prose | pages [8] -->
d v

<!-- b000274 | prose | pages [8] -->
( )

<!-- b000275 | prose | pages [8] -->
c

<!-- b000276 | prose | pages [8] -->
In a network, nodes link with each other by the edge between them. Each edge represents one kind of relation between two nodes. For example, in a criminal network, the edges represent information flow among them. Actually, the information with different kinds of topics has different safe class; the direction of information flows might influence the importance of members in the network. However, traditional criminal network analysis does not consider these ―differences‖ of edges. Although some researches also attach importance to a criminal network in link-level, they did not take into account all information in detail.

<!-- b000277 | furniture | pages [8] -->


<!-- b000278 | furniture | pages [9] -->
Team#16075

<!-- b000279 | furniture | pages [9] -->


<!-- b000280 | prose | pages [9] -->
Metric choosing

<!-- b000281 | furniture | pages [9] -->
Page 7 of 20

<!-- b000282 | prose | pages [9] -->
In this paper, to indentify all the conspirators from workers, in addition to consider the importance of a person in node-level, we also define an index in link-level which concerns about the information transferred by every person. Our goal is to find out the conspirators and leader of them, so the information our model concerns is the suspicious information. Here, we use CIC to measure the amount of suspicious information a person involves. According to the information we have known, we can conclude that CIC can be determined by following metrics:

<!-- b000283 | prose | pages [9] -->
 Topic. There are 15 topics in total. Some of them are suspicious while the

<!-- b000284 | prose | pages [9] -->
others are innocent. Those who talk about suspicious are suggested to be conspirators.

<!-- b000285 | prose | pages [9] -->
 Conversation object. All conspirators must connect with each other closely,

<!-- b000286 | prose | pages [9] -->
therefore, if one has been identified as a criminal, the person he communication with would have probability to be a conspirator.

<!-- b000287 | prose | pages [9] -->
 Direction. This metric is used to describe whether a person is active or

<!-- b000288 | prose | pages [9] -->
passive in a conversation. Consider these two workers, one talks suspicious topics with others actively while the other communicates the same topics with others, it is not difficult to realize that the former have greater suspicion to be regarded as a conspirator. Hence this factor impacts the judge of a worker‘s identity.

<!-- b000289 | prose | pages [9] -->
Computation of CIC

<!-- b000290 | prose | pages [9] -->
The object of CIC is edge, which represents one communication. For one directed edge, the CIC can be defined as:

<!-- b000291 | prose | pages [9] -->
  W w f v ( )

<!-- b000292 | furniture | pages [9] -->


<!-- b000293 | prose | pages [9] -->
1 t

<!-- b000294 | prose | pages [9] -->
Where

<!-- b000295 | prose | pages [9] -->
W is the value of CIC.  1

<!-- b000296 | prose | pages [9] -->
 w g v ( ) w h v ( )

<!-- b000297 | furniture | pages [9] -->


<!-- b000298 | prose | pages [9] -->
(4-5) c c d

<!-- b000299 | prose | pages [9] -->
w w w denotes the weight of topic, conversationalist and direction. , ,  t c d

<!-- b000300 | prose | pages [9] -->
f v ,otherwise f v is a binary variable, if the topic is a suspicious topic,  ( ) the value is 0.

<!-- b000301 | prose | pages [9] -->
( ) 1

<!-- b000302 | prose | pages [9] -->
h v because it represent that  If the edge is a out-degree of the point, the ( ) 1 the person talk this topic with others actively, otherwise the value is 0.5. It means that the person is passive in this conversation, though the person is passive, he have been involved in this conversation and touched this information.

<!-- b000303 | prose | pages [9] -->
g v is a ternary value, if the conversation object is an identified conspirators,  ( ) the value is 1 for talking with a conspirator will improve the probability of being identified as a criminal; if the object is a unknown person, the value is 0.5 for the possibility exist but not sure; if the object is a non-conspirator, the value is 0 for talking with a identified non-conspirator is safe.

<!-- b000304 | prose | pages [9] -->
If a person have talked with other several times, the degree of the node representing him is bigger than 1. Derived from equation (4-5), we can write that the total CIC of this person is:

<!-- b000305 | furniture | pages [9] -->


<!-- b000306 | furniture | pages [10] -->
Team#16075

<!-- b000307 | furniture | pages [10] -->


<!-- b000308 | prose | pages [10] -->
n

<!-- b000309 | prose | pages [10] -->


<!-- b000310 | prose | pages [10] -->
 

<!-- b000311 | furniture | pages [10] -->


<!-- b000312 | prose | pages [10] -->
W v

<!-- b000313 | prose | pages [10] -->
( )

<!-- b000314 | prose | pages [10] -->
w f v

<!-- b000315 | prose | pages [10] -->
( )

<!-- b000316 | prose | pages [10] -->
t i

<!-- b000317 | prose | pages [10] -->


<!-- b000318 | prose | pages [10] -->
i

<!-- b000319 | prose | pages [10] -->
1

<!-- b000320 | prose | pages [10] -->
Determination Metrics’ Weight

<!-- b000321 | furniture | pages [10] -->
Page 8 of 20

<!-- b000322 | prose | pages [10] -->


<!-- b000323 | prose | pages [10] -->
  

<!-- b000324 | furniture | pages [10] -->


<!-- b000325 | prose | pages [10] -->
(4-6)

<!-- b000326 | prose | pages [10] -->
w g v

<!-- b000327 | prose | pages [10] -->
( )

<!-- b000328 | prose | pages [10] -->
w h v

<!-- b000329 | prose | pages [10] -->
( )

<!-- b000330 | prose | pages [10] -->
c i d i

<!-- b000331 | prose | pages [10] -->
Having defined the metrics, following work will introduce how to determine the weight of these three metrics. Analytical Hierarchy Process (AHP), first proposed by American researcher T.L.Saaty, is a proper way to find the weights for different metrics.

<!-- b000332 | prose | pages [10] -->
Firstly, we must determine comparison matrix. There are three metrics in this matrix. The suspicious topic is the key factor during investigation. A person might have big suspicion if he talks with criminals. The direction of communication is also related to the identification of conspirator, however it is quiet slight. Hence the scores of each metric is:

<!-- b000333 | prose | pages [10] -->


<!-- b000334 | furniture | pages [10] -->


<!-- b000335 | prose | pages [10] -->
C 6;

<!-- b000336 | prose | pages [10] -->
C   3;

<!-- b000337 | prose | pages [10] -->
C 1 commun topic dir

<!-- b000338 | prose | pages [10] -->
Then, the comparison matrix can be derived:

<!-- b000339 | prose | pages [10] -->


<!-- b000340 | prose | pages [10] -->
1

<!-- b000341 | prose | pages [10] -->
 

<!-- b000342 | prose | pages [10] -->
A 1/ 2

<!-- b000343 | furniture | pages [10] -->


<!-- b000344 | prose | pages [10] -->


<!-- b000345 | prose | pages [10] -->
1/ 6

<!-- b000346 | prose | pages [10] -->
 

<!-- b000347 | prose | pages [10] -->
2 6

<!-- b000348 | prose | pages [10] -->


<!-- b000349 | prose | pages [10] -->
1 3

<!-- b000350 | furniture | pages [10] -->


<!-- b000351 | prose | pages [10] -->
(4-7)

<!-- b000352 | prose | pages [10] -->
 

<!-- b000353 | prose | pages [10] -->
1/ 3 1

<!-- b000354 | prose | pages [10] -->


<!-- b000355 | prose | pages [10] -->
  According to the matrix (4-7) and equation Aw

<!-- b000356 | furniture | pages [10] -->


<!-- b000357 | prose | pages [10] -->
w  weight vector . [0.6,0.3,0.1] w , we can figure out that the

<!-- b000358 | prose | pages [10] -->
CI  0 Finally, in consistency check, the consistency index

<!-- b000359 | furniture | pages [10] -->


<!-- b000360 | prose | pages [10] -->
，which means that consistency rate CR always equal to 0. The weight determined by AHP is very reasonable.

<!-- b000361 | heading | pages [10] -->
4.2.3 The Expression of ECNAM

<!-- b000362 | prose | pages [10] -->
After finishing the definition and computation of Centrality and CIC, the final model can be presented.

<!-- b000363 | prose | pages [10] -->
The final score of discrimination is determined by centrality and CIC. Centrality represents the importance and activity. The value of it can stand for the ability to transfer information. Bigger centrality represents greater ability to transfer information in a network. CIC represent the amount criminal information a person carries.

<!-- b000364 | prose | pages [10] -->
These two properties decide the result of discrimination commonly. Thus, we define the product of Centrality and CIC as the score of discrimination. Combining equation (4-4) and (4-6), the final model ECNAM can be derived:

<!-- b000365 | prose | pages [10] -->
 

<!-- b000366 | prose | pages [10] -->
d v d

<!-- b000367 | prose | pages [10] -->
( )

<!-- b000368 | prose | pages [10] -->
v

<!-- b000369 | prose | pages [10] -->


<!-- b000370 | prose | pages [10] -->
d

<!-- b000371 | prose | pages [10] -->
d v

<!-- b000372 | prose | pages [10] -->
( )

<!-- b000373 | prose | pages [10] -->


<!-- b000374 | prose | pages [10] -->
s

<!-- b000375 | prose | pages [10] -->
d v

<!-- b000376 | prose | pages [10] -->
( )

<!-- b000377 | prose | pages [10] -->


<!-- b000378 | prose | pages [10] -->
c

<!-- b000379 | furniture | pages [10] -->


<!-- b000380 | prose | pages [10] -->
n

<!-- b000381 | prose | pages [10] -->


<!-- b000382 | prose | pages [10] -->


<!-- b000383 | prose | pages [10] -->


<!-- b000384 | prose | pages [10] -->
W v

<!-- b000385 | prose | pages [10] -->
( )

<!-- b000386 | prose | pages [10] -->
w f v

<!-- b000387 | prose | pages [10] -->
( )

<!-- b000388 | prose | pages [10] -->


<!-- b000389 | prose | pages [10] -->
t i

<!-- b000390 | prose | pages [10] -->


<!-- b000391 | prose | pages [10] -->


<!-- b000392 | prose | pages [10] -->
i

<!-- b000393 | prose | pages [10] -->
1

<!-- b000394 | prose | pages [10] -->


<!-- b000395 | prose | pages [10] -->
S v

<!-- b000396 | prose | pages [10] -->
( )

<!-- b000397 | prose | pages [10] -->
d v W v

<!-- b000398 | prose | pages [10] -->
( ) ( )

<!-- b000399 | prose | pages [10] -->


<!-- b000400 | prose | pages [10] -->
s

<!-- b000401 | prose | pages [10] -->
( )

<!-- b000402 | prose | pages [10] -->
b b

<!-- b000403 | prose | pages [10] -->


<!-- b000404 | prose | pages [10] -->
 

<!-- b000405 | prose | pages [10] -->
w g v

<!-- b000406 | prose | pages [10] -->
( )

<!-- b000407 | prose | pages [10] -->
w h v

<!-- b000408 | prose | pages [10] -->
( )

<!-- b000409 | prose | pages [10] -->
c i d i

<!-- b000410 | furniture | pages [10] -->


<!-- b000411 | prose | pages [10] -->
To make the result more clear, we translate the final score into value from 0 to 100

<!-- b000412 | furniture | pages [10] -->


<!-- b000413 | prose | pages [10] -->
  by equation . S 100 S S / final max

<!-- b000414 | furniture | pages [10] -->


<!-- b000415 | furniture | pages [11] -->
Team#16075

<!-- b000416 | furniture | pages [11] -->
Page 9 of 20

<!-- b000417 | furniture | pages [11] -->


<!-- b000418 | furniture | pages [11] -->


<!-- b000419 | prose | pages [11] -->
Where S is the biggest score of the result. max

<!-- b000420 | furniture | pages [11] -->


<!-- b000421 | prose | pages [11] -->
To discriminate non-conspirators and criminals, we define the point where slope changes maximum as the cut-off point.

<!-- b000422 | prose | pages [11] -->
According to the model presented above, all workers can be divided into following four types:

<!-- b000423 | prose | pages [11] -->
 Both centrality and CIC are little. This kind of person is unsociable and has

<!-- b000424 | prose | pages [11] -->
little criminal information, so this type of people cannot be conspirators.

<!-- b000425 | prose | pages [11] -->
 Centrality is little while CIC is big. This kind of people has low position and

<!-- b000426 | prose | pages [11] -->
communicates with others rarely. As the assumption we have made, conspirator is relatively active. Hence, they cannot be regarded as conspirator.

<!-- b000427 | prose | pages [11] -->
 Centrality is big while CIC is little. This kind of people is important and has

<!-- b000428 | prose | pages [11] -->
high position in a network. They are active at social gatherings. However they do not talk about suspicious topic. So they cannot be identified as conspirators.

<!-- b000429 | prose | pages [11] -->
 Both Centrality and CIC are big. These people carry plentiful criminal

<!-- b000430 | prose | pages [11] -->
information and communication with others about suspicious topics. These people must be conspirators needed to identify.

<!-- b000431 | heading | pages [11] -->
4.3 Solution

<!-- b000432 | heading | pages [11] -->
4.3.1 Verification of ECNAM

<!-- b000433 | prose | pages [11] -->
At first, the simple example EZ case is used to test our model. Now following information have been informed:

<!-- b000434 | prose | pages [11] -->
 There are 5 topics among ten people and topic 3 is suspicious topic;

<!-- b000435 | prose | pages [11] -->
 Dave and George are known conspirators while Anne and Jaye are innocent.

<!-- b000436 | prose | pages [11] -->
Quantifying the information in the network and programming with Matlab software, we can get the result shown in Figure 2.

<!-- b000437 | furniture | pages [11] -->


<!-- b000438 | caption | pages [11] -->
Figure 2: likelihood rank of the example

<!-- b000439 | furniture | pages [11] -->


<!-- b000440 | prose | pages [11] -->
From the result shown in the figure above, several conclusions can be made:

<!-- b000441 | prose | pages [11] -->
 The top five persons are Dave, George, Ellen, Harry and Inez. Compared to the

<!-- b000442 | prose | pages [11] -->
actual result that the conspirators are Dave, George, Ellen, Inez and Bob. Just

<!-- b000443 | furniture | pages [11] -->


<!-- b000444 | furniture | pages [12] -->
Team#16075

<!-- b000445 | furniture | pages [12] -->
Page 10 of 20

<!-- b000446 | furniture | pages [12] -->


<!-- b000447 | prose | pages [12] -->
one person is misjudged. The error rate is 80%.

<!-- b000448 | prose | pages [12] -->
 Given that the supervisor did not identify Bob and she also misjudged Harry, our

<!-- b000449 | prose | pages [12] -->
result is consistent to the expert‘s result.

<!-- b000450 | prose | pages [12] -->
 The leader of this gang is Dave, who is an identified person. Thus, the result is

<!-- b000451 | prose | pages [12] -->
quiet reasonable.

<!-- b000452 | heading | pages [12] -->
4.3.2 Result of Requirement 1

<!-- b000453 | prose | pages [12] -->
In this requirement, it is known that 7 persons including Jean, Alex, Elsie, Paul, Ulf, Yao, and Harvey are conspirators. 8 persons are not conspirators. The three known suspicious topics are 7, 11 and 13. Using these information and programming with Matlab software, we can get the result as shown in Figure 3. The blue points represent the scores of every person. The names marked by red color are indentified conspirators.

<!-- b000454 | furniture | pages [12] -->


<!-- b000455 | furniture | pages [12] -->


<!-- b000456 | furniture | pages [12] -->


<!-- b000457 | prose | pages [12] -->
Figure 3(a): Original result

<!-- b000458 | furniture | pages [12] -->


<!-- b000459 | prose | pages [12] -->
Figure 3(b): Gretchen is a conspirator

<!-- b000460 | prose | pages [12] -->
From Figure 3(a), we can conclude:

<!-- b000461 | prose | pages [12] -->
 Elsie gets the highest score, so the leader of this criminal gang is Elsie.

<!-- b000462 | prose | pages [12] -->
 Five of the seven conspirators rank in top ten. It means that the identified

<!-- b000463 | prose | pages [12] -->
conspirators often get high score in our model. That is to say, our model is quite accurate.

<!-- b000464 | prose | pages [12] -->
 There are 23 conspirators in the company.

<!-- b000465 | prose | pages [12] -->
 The accuracy is around 80% according to the data we get.

<!-- b000466 | prose | pages [12] -->
If Gretchen is the manager of the company, observing the result can find out that his order is 18. He suspicion is pretty high. Thus we determine that he is an identified conspirator. Then computing the program again, we can figure out the result as shown in Figure 3(b). Comparing these two figures, we can conclude that:

<!-- b000467 | prose | pages [12] -->
 This information impacts the result slightly.

<!-- b000468 | furniture | pages [12] -->


<!-- b000469 | heading | pages [12] -->
4.4 Fisher Discrimination and ECNAM

<!-- b000470 | prose | pages [12] -->
This problem also can be solved by Fisher's linear discriminant proposed firstly by

<!-- b000471 | furniture | pages [12] -->


<!-- b000472 | furniture | pages [13] -->
Team#16075

<!-- b000473 | furniture | pages [13] -->


<!-- b000474 | furniture | pages [13] -->
Page 11 of 20

<!-- b000475 | prose | pages [13] -->
British statistician and geneticist R.A.Fisher. Fisher's linear discriminant are methods used in statistics, pattern recognition and machine learning to find a linear combination of features which characterizes or separates two or more classes of objects or events. The resulting combination may be used as a linear classifier or, more commonly, for dimensionality reduction before later classification.

<!-- b000476 | furniture | pages [13] -->


<!-- b000477 | prose | pages [13] -->
Referring to [6], the model based on Fisher discriminant can be written as follows:

<!-- b000478 | prose | pages [13] -->
T

<!-- b000479 | prose | pages [13] -->
w S w

<!-- b000480 | prose | pages [13] -->


<!-- b000481 | prose | pages [13] -->
b

<!-- b000482 | prose | pages [13] -->
J

<!-- b000483 | prose | pages [13] -->
( )

<!-- b000484 | prose | pages [13] -->
w

<!-- b000485 | prose | pages [13] -->
F T

<!-- b000486 | prose | pages [13] -->
w S w

<!-- b000487 | prose | pages [13] -->
w

<!-- b000488 | prose | pages [13] -->


<!-- b000489 | prose | pages [13] -->


<!-- b000490 | prose | pages [13] -->


<!-- b000491 | prose | pages [13] -->
* 1

<!-- b000492 | prose | pages [13] -->
w

<!-- b000493 | prose | pages [13] -->
S

<!-- b000494 | prose | pages [13] -->
(

<!-- b000495 | prose | pages [13] -->
m

<!-- b000496 | prose | pages [13] -->


<!-- b000497 | prose | pages [13] -->
w

<!-- b000498 | prose | pages [13] -->
1

<!-- b000499 | prose | pages [13] -->
  

<!-- b000500 | furniture | pages [13] -->


<!-- b000501 | prose | pages [13] -->
S

<!-- b000502 | prose | pages [13] -->
(

<!-- b000503 | prose | pages [13] -->
m m

<!-- b000504 | prose | pages [13] -->


<!-- b000505 | prose | pages [13] -->
b

<!-- b000506 | prose | pages [13] -->
1

<!-- b000507 | prose | pages [13] -->
  

<!-- b000508 | prose | pages [13] -->
S

<!-- b000509 | prose | pages [13] -->
(

<!-- b000510 | prose | pages [13] -->


<!-- b000511 | prose | pages [13] -->
w

<!-- b000512 | prose | pages [13] -->
 

<!-- b000513 | prose | pages [13] -->


<!-- b000514 | prose | pages [13] -->
i

<!-- b000515 | prose | pages [13] -->
1,2

<!-- b000516 | prose | pages [13] -->
x

<!-- b000517 | prose | pages [13] -->
i

<!-- b000518 | prose | pages [13] -->
 

<!-- b000519 | prose | pages [13] -->
m

<!-- b000520 | prose | pages [13] -->
)

<!-- b000521 | prose | pages [13] -->
2

<!-- b000522 | prose | pages [13] -->


<!-- b000523 | prose | pages [13] -->
T

<!-- b000524 | prose | pages [13] -->
)(

<!-- b000525 | prose | pages [13] -->
m m

<!-- b000526 | prose | pages [13] -->
)

<!-- b000527 | prose | pages [13] -->
2 2 1 2

<!-- b000528 | prose | pages [13] -->
 

<!-- b000529 | prose | pages [13] -->
T

<!-- b000530 | prose | pages [13] -->
x x m

<!-- b000531 | prose | pages [13] -->
)(

<!-- b000532 | prose | pages [13] -->
x m

<!-- b000533 | prose | pages [13] -->
)

<!-- b000534 | prose | pages [13] -->
i i

<!-- b000535 | prose | pages [13] -->
S is the dispersion matrix m represents the vector of sample mean;

<!-- b000536 | furniture | pages [13] -->


<!-- b000537 | prose | pages [13] -->
Where i w

<!-- b000538 | furniture | pages [13] -->


<!-- b000539 | prose | pages [13] -->
S denotes the dispersion matrix between class; within class;

<!-- b000540 | prose | pages [13] -->
b

<!-- b000541 | prose | pages [13] -->
* w is projecting direction.

<!-- b000542 | prose | pages [13] -->
J is criterion function; F

<!-- b000543 | prose | pages [13] -->
 Comparison between Fisher Discriminant and ECNAM

<!-- b000544 | prose | pages [13] -->
We chose three indices: Degree of a vertex, topic, and conversation object.

<!-- b000545 | prose | pages [13] -->
The conspirators identified by Fisher Discriminant are:

<!-- b000546 | caption | pages [13] -->
Table 2: The result of Fisher Discriminant

<!-- b000547 | prose | pages [13] -->
Number 7 10 13

<!-- b000548 | prose | pages [13] -->
Name Elsie Dolores Marion

<!-- b000549 | prose | pages [13] -->
Number 21 37 43

<!-- b000550 | prose | pages [13] -->
Name Alex Elsie Paul

<!-- b000551 | prose | pages [13] -->
The conspirators identified by ECNAM are:

<!-- b000552 | prose | pages [13] -->
16 17 18 20

<!-- b000553 | prose | pages [13] -->
Jerome Neal Jean Crystal

<!-- b000554 | prose | pages [13] -->
47 49 54 67

<!-- b000555 | prose | pages [13] -->
Christina Harvey Ulf Yao

<!-- b000556 | caption | pages [13] -->
Table 3: The result of ECNAM

<!-- b000557 | prose | pages [13] -->
Order 1 2 3

<!-- b000558 | prose | pages [13] -->
Number 8 22 4

<!-- b000559 | prose | pages [13] -->
Name Elsie Alex Sherri

<!-- b000560 | prose | pages [13] -->
Order 8 9 10

<!-- b000561 | prose | pages [13] -->
Number 3 33 19

<!-- b000562 | prose | pages [13] -->
Name Paige Gretchen Jean

<!-- b000563 | prose | pages [13] -->
4 5 6 7

<!-- b000564 | prose | pages [13] -->
68 45 44 20

<!-- b000565 | prose | pages [13] -->
Yao Patricia Paul Kristine

<!-- b000566 | prose | pages [13] -->
11 12 13 14

<!-- b000567 | prose | pages [13] -->
9 25 23 49

<!-- b000568 | prose | pages [13] -->
Hazel Franklin Eric Darlene

<!-- b000569 | prose | pages [13] -->
From the two table above, we can conclude that：

<!-- b000570 | prose | pages [13] -->
 The results of them are quite different. Only 5 persons are the same and the 5

<!-- b000571 | prose | pages [13] -->
person are the known conspirators.

<!-- b000572 | prose | pages [13] -->
 The Fisher discriminant only can discriminate the conspirators but cannot

<!-- b000573 | prose | pages [13] -->
prioritize them.

<!-- b000574 | furniture | pages [13] -->


<!-- b000575 | furniture | pages [14] -->
Team#16075

<!-- b000576 | furniture | pages [14] -->


<!-- b000577 | furniture | pages [14] -->
Page 12 of 20

<!-- b000578 | prose | pages [14] -->
 Fisher discriminant only use the statistics information of a network, while our

<!-- b000579 | prose | pages [14] -->
model have used the statistics information and the properties of network, so the result is relatively accurate.

<!-- b000580 | prose | pages [14] -->
 Fisher discriminant cannot differentiate a network that has small sample, for

<!-- b000581 | prose | pages [14] -->
example, we failed to use Fisher discriminant to identify the EZ case.

<!-- b000582 | heading | pages [14] -->
5 New Clues Discovered

<!-- b000583 | prose | pages [14] -->
With the progress of the case, how would the priority list change if new clues will

<!-- b000584 | furniture | pages [14] -->


<!-- b000585 | prose | pages [14] -->
come to light? When we substitute the parameters in our basic model, the answer becomes clear.

<!-- b000586 | prose | pages [14] -->
In this scenario, the result is shown as figure 4 and table 4：(In order to see the

<!-- b000587 | furniture | pages [14] -->


<!-- b000588 | prose | pages [14] -->
changes clearly, original likelihood rank is also listed)

<!-- b000589 | furniture | pages [14] -->


<!-- b000590 | caption | pages [14] -->
Figure 4: The result of new clues

<!-- b000591 | caption | pages [14] -->
Table 4: the top 8 identified conspirators of the two scenarios

<!-- b000592 | prose | pages [14] -->
Rank 1 2 3 4

<!-- b000593 | prose | pages [14] -->
New Sherri Gretchen Patricia Julia

<!-- b000594 | prose | pages [14] -->
5 6 7 8

<!-- b000595 | prose | pages [14] -->
Kristine Darlene Franklin -

<!-- b000596 | prose | pages [14] -->
Kristine Gretchen Hazel Original Sherri Patricia Franklin Eric Darlene

<!-- b000597 | prose | pages [14] -->
The second row represents the result under the new scenario while the third row

<!-- b000598 | furniture | pages [14] -->


<!-- b000599 | prose | pages [14] -->
shows the result of the original result

<!-- b000600 | prose | pages [14] -->
Basic conclusion based on the solution above:

<!-- b000601 | prose | pages [14] -->
 After applying the new discovery in the model, the number of conspirators

<!-- b000602 | prose | pages [14] -->
reduces to 28 while the original number is 23. Here are some reasons to explain this result. Since Chris becomes a conspirator, the likelihood of people who communicate with him will increase. According to the assumption, the likelihood will also increase if people talk about suspect topics.

<!-- b000603 | prose | pages [14] -->
 Most of the inferred suspects are the same while their ranks are different more or

<!-- b000604 | prose | pages [14] -->
less.

<!-- b000605 | heading | pages [14] -->
6 Refined by Semantic Network Analysis

<!-- b000606 | prose | pages [14] -->
In the previous model which is established to distinguish conspirators from

<!-- b000607 | furniture | pages [14] -->


<!-- b000608 | prose | pages [14] -->
non-conspirators, topics are absolutely divided into two aspects: conspiratorial and not conspiratorial. Since it ignores the potential linkages between topics, our model

<!-- b000609 | furniture | pages [14] -->


<!-- b000610 | furniture | pages [15] -->
Team#16075

<!-- b000611 | furniture | pages [15] -->


<!-- b000612 | furniture | pages [15] -->
Page 13 of 20

<!-- b000613 | prose | pages [15] -->
can be enhanced by using a powerful technique of Semantic and Text analyses.

<!-- b000614 | furniture | pages [15] -->


<!-- b000615 | heading | pages [15] -->
6.1 Introduction of Semantic and Text Analyses

<!-- b000616 | prose | pages [15] -->
In the everyday life, people can‘t avoid communicating with the outside world.

<!-- b000617 | furniture | pages [15] -->


<!-- b000618 | prose | pages [15] -->
What they inadvertently say may be exposed to the idea of mind. Semantic Network Analysis and Text Analysis is just the method to obtain and understand text information. Thus, potential linkages between the topics will be found.

<!-- b000619 | prose | pages [15] -->
For our crime busting scenario, the linkage only has an effect on the edge weight

<!-- b000620 | furniture | pages [15] -->


<!-- b000621 | prose | pages [15] -->
in the message traffic. As can be seen from the equation (4-6) that what really matters 1c while the other two values of each edge are constant. According to is the value of the literature, Text Analysis refers to the text representation of features selected. Those feature words extracted from the text are quantified to represent information, which provides an effective method to filter unwanted information and classify the topics.

<!-- b000622 | prose | pages [15] -->
Based on the above analysis, if feature words are extracted from the topic, topics

<!-- b000623 | furniture | pages [15] -->


<!-- b000624 | prose | pages [15] -->
can be divided into different parts and the potential linkage will be found. Thus, the 1c is the key factors resulting in a better model accurate value of

<!-- b000625 | furniture | pages [15] -->


<!-- b000626 | heading | pages [15] -->
6.2 Application of Text Analysis in ECNAM

<!-- b000627 | prose | pages [15] -->
Since the original message can‘t be obtained, the only way to determine the edge

<!-- b000628 | furniture | pages [15] -->


<!-- b000629 | prose | pages [15] -->
value is dividing the given topics into more detailed parts by using Text Analysis. The most important part is how to choose the feature words. According to the simple introduction to the conspirators, four indexes are promoted as follows: whether or not to talk about the economic situation, safety measures, known conspirators and talking in Spanish as a kind of code words. Four variables are promoted to represent the i i i i . The values of the four variables are 0 or 1. , , , value of those aspects, namely, 1 2 3 4 Based on the consideration of the four factors, we get the objective formula to

<!-- b000630 | furniture | pages [15] -->


<!-- b000631 | prose | pages [15] -->
calculate the weight of each edge:

<!-- b000632 | prose | pages [15] -->
  c k i

<!-- b000633 | furniture | pages [15] -->


<!-- b000634 | prose | pages [15] -->
1 1 1

<!-- b000635 | prose | pages [15] -->
Where

<!-- b000636 | prose | pages [15] -->
  k i k i

<!-- b000637 | furniture | pages [15] -->


<!-- b000638 | furniture | pages [15] -->


<!-- b000639 | prose | pages [15] -->
(4-8) 2 2 2 3 3

<!-- b000640 | prose | pages [15] -->
k k k k are the Preference coefficients: donates how evaluator lay emphasis , , ,

<!-- b000641 | furniture | pages [15] -->


<!-- b000642 | prose | pages [15] -->
1 2 3 4

<!-- b000643 | prose | pages [15] -->
k k k k are subjected to the , , , on each of the factors taken into consideration. And constrain:

<!-- b000644 | prose | pages [15] -->
  k k 1 2

<!-- b000645 | prose | pages [15] -->
1 2 3 4

<!-- b000646 | prose | pages [15] -->
  k k k 1 3 3 4

<!-- b000647 | prose | pages [15] -->
To simplify our model, we attach the same importance of the four factors. So,

<!-- b000648 | prose | pages [15] -->
  k k k 1 2   k 0.25

<!-- b000649 | furniture | pages [15] -->


<!-- b000650 | prose | pages [15] -->
3 3 4

<!-- b000651 | prose | pages [15] -->
From equation (4-8), the weights of those 15 topics are as follows:

<!-- b000652 | furniture | pages [15] -->


<!-- b000653 | caption | pages [15] -->
Table 5: the weight of those 15 topics

<!-- b000654 | prose | pages [15] -->
Topic number 1 2 3

<!-- b000655 | furniture | pages [15] -->


<!-- b000656 | prose | pages [15] -->
4 5 6 7 8

<!-- b000657 | furniture | pages [16] -->
Team#16075

<!-- b000658 | furniture | pages [16] -->


<!-- b000659 | prose | pages [16] -->
Weight 0.25 0.25 0

<!-- b000660 | prose | pages [16] -->
Topic number 9 10 11

<!-- b000661 | prose | pages [16] -->
Weight 0.25 0 0.75

<!-- b000662 | prose | pages [16] -->
From table 5，we can conclude that:

<!-- b000663 | furniture | pages [16] -->
Page 14 of 20

<!-- b000664 | prose | pages [16] -->
0.25 0.5 0.25 0.75 0

<!-- b000665 | prose | pages [16] -->
12 13 14 15

<!-- b000666 | furniture | pages [16] -->


<!-- b000667 | prose | pages [16] -->
0.25 1.0 0.25 0.5

<!-- b000668 | furniture | pages [16] -->


<!-- b000669 | prose | pages [16] -->
 Based on the weight of each topic, all the 15 topics can be divided into 5 groups.

<!-- b000670 | prose | pages [16] -->
topic 3, topic8 and topic10 are in the same group which has nothing to do with crime; topic1, topic2, topic4, topic6, topic9, topic12 and topic14 are in the same group whose weight is 0.25; topic5 and topic15 are in the same group and topic7 and topic11 are in the same group which shows some clues about crime while topic 13 shows direct connect with crime.  The weights of topic7, topic11 and topic13 indicate that these topics have closely

<!-- b000671 | prose | pages [16] -->
relationships with crime which matches the known conditions.  The values of three topics including topic3, topic8 and topic10 remains 0,which is

<!-- b000672 | prose | pages [16] -->
the same with the previous value while most of the rest have changed because of the discover of potential linkages between topics. Now table 4 can be applied in ECNAM taking place of 0.9 and 0.1.

<!-- b000673 | heading | pages [16] -->
6.3 Comparison and Analysis

<!-- b000674 | prose | pages [16] -->
We substitute the parameters in our model with all the above calculated values,

<!-- b000675 | furniture | pages [16] -->


<!-- b000676 | prose | pages [16] -->
getting solutions shown in Figure 5 and Table 5.

<!-- b000677 | furniture | pages [16] -->


<!-- b000678 | caption | pages [16] -->
Figure 5: the result of using and not using Text Analysis

<!-- b000679 | prose | pages [16] -->
In order to see the effect of using Text Analysis, the name of the top eight

<!-- b000680 | furniture | pages [16] -->


<!-- b000681 | prose | pages [16] -->
conspirators and their scores are listed as table 6 shows: ( The rows with the name New represents the result of using Text Analysis while the rest two rows are the result of not using Text Analysis)

<!-- b000682 | caption | pages [16] -->
Table 6: the result of the two scenarios

<!-- b000683 | prose | pages [16] -->
Rank 1 2 3 4 4 5 6 7 8

<!-- b000684 | prose | pages [16] -->
Franklin Gretchen Patricia Name Sherri

<!-- b000685 | prose | pages [16] -->
New

<!-- b000686 | prose | pages [16] -->
Score 97.70% 90.29% 89.62%

<!-- b000687 | prose | pages [16] -->
Name Sherri Patricia Kristine

<!-- b000688 | prose | pages [16] -->
Old

<!-- b000689 | prose | pages [16] -->
Score 73.18% 70.88% 64.93%

<!-- b000690 | furniture | pages [16] -->


<!-- b000691 | prose | pages [16] -->
Kristine Julia Jerome Hazel

<!-- b000692 | prose | pages [16] -->
78.94% 71.98% 66.24% 60.91% 60.15%

<!-- b000693 | prose | pages [16] -->
Gretchen Hazel Franklin Eric Julia

<!-- b000694 | prose | pages [16] -->
59.56% 53.53% 52.93% 52.04% 48.44%

<!-- b000695 | furniture | pages [17] -->
Team#16075

<!-- b000696 | furniture | pages [17] -->
Page 15 of 20

<!-- b000697 | furniture | pages [17] -->


<!-- b000698 | furniture | pages [17] -->


<!-- b000699 | prose | pages [17] -->
Based on figure 4 and table 5, we can conclude that:

<!-- b000700 | prose | pages [17] -->
 According to the assumption, for those whose likelihood is higher than 50% will be

<!-- b000701 | prose | pages [17] -->
convicted as criminals. Thus, there are 18 conspirators in total including the known conspirators. On the contrast, there are conspirators is 16 conspirators when we don‘t use Text Analysis. The weight of topic can explain the increasing number of conspirators well;  The top eight conspirators between the two different scenarios are almost

<!-- b000702 | prose | pages [17] -->
unanimously while the likelihood of the former is much higher than the later which will be more determined to convince the conspirators. Both the two methods have the same misjudgment rate. They all mistake Paige for conspirator and mistake Ulf and Harvey for non-conspirators. Thus, the misjudgment rate is 20% which will help the judge make the right choices.

<!-- b000703 | heading | pages [17] -->
7 Simulation and Analysis

<!-- b000704 | heading | pages [17] -->
7.1 Depth analysis: characteristics of conspirators’ activities

<!-- b000705 | prose | pages [17] -->
In depth analysis, the main content is to analyze the characteristics of conspirators‘ activities. And based on this result of analysis, investigators can carry out targeted supervise, execute specific investigation, and projecting investigation of identical and background information of conspirators.

<!-- b000706 | prose | pages [17] -->
The conspirators‘ network, on which we focus in analysis, is constituted only by the 28 conspirators we identified before and the message traffic between them.

<!-- b000707 | heading | pages [17] -->
7.1.1 Basic properties of conspirators’ network

<!-- b000708 | prose | pages [17] -->
First, we will analyze the properties of conspirators.

<!-- b000709 | prose | pages [17] -->
We inspect four properties of the network. Degree represents how many other conspirators a conspirator communicates with. Closeness depicts if conspirators directly talk to others, displayed with their degree.. The lower closeness is, the more directly talk is. Betweenness reflects the importance of a conspirator in a message traffic line, with a x-axis of degree too. The last property is shortest path distribution.

<!-- b000710 | furniture | pages [17] -->


<!-- b000711 | caption | pages [17] -->
Figure 6: result of basic information of each node

<!-- b000712 | furniture | pages [17] -->


<!-- b000713 | furniture | pages [18] -->
Team#16075

<!-- b000714 | furniture | pages [18] -->


<!-- b000715 | prose | pages [18] -->
Basic Conclusion based on figure 6 :

<!-- b000716 | furniture | pages [18] -->
Page 16 of 20

<!-- b000717 | prose | pages [18] -->
 All nodes‘ degree are higher than 5, which explains that communications

<!-- b000718 | prose | pages [18] -->
between conspirators is frequently. It can be surmised that conspirators often talk with others, maybe about conspiracy.

<!-- b000719 | prose | pages [18] -->
 With the growth of neighbors, closeness of conspirators also increase

<!-- b000720 | prose | pages [18] -->
distantly. It shows that in some extent, the network is hierarchy, which contains a potential leader.

<!-- b000721 | prose | pages [18] -->
 The Betweenness of nodes varies when conspirators have different count of

<!-- b000722 | prose | pages [18] -->
neighbors. A somewhat complexity exists in message traffic of the network.

<!-- b000723 | prose | pages [18] -->
 Shortest path in network have a length of 1 or 2. It manifests a clear fact that

<!-- b000724 | prose | pages [18] -->
the communications in the network are efficient. Conspirators do not need many Intermediate nodes to transfer messages.

<!-- b000725 | prose | pages [18] -->
The analysis shows that the message traffic between conspirators is a closely linked network. It proves that they talk much with others, which meets a basic feature of conspiracy activities.

<!-- b000726 | heading | pages [18] -->
7.1.2 Leader detection of conspirators’ network

<!-- b000727 | prose | pages [18] -->
Find out the leader of conspirators‘ network, and then certain the hierarchy of the network, in another word, how conspirators communicate with others to discuss the conspiracy, and how the conspiracy commands are transferred and executed.

<!-- b000728 | prose | pages [18] -->
To determine the leader, we consider the position of each conspirator in the network. We take into account three indexes to describe conspirators: degree, betweenness, and closeness of nodes that represents conspirators in network.

<!-- b000729 | prose | pages [18] -->
We figure the leader measured score with sum of three indexes above.

<!-- b000730 | prose | pages [18] -->
  

<!-- b000731 | furniture | pages [18] -->


<!-- b000732 | prose | pages [18] -->
Dregree Lead _det ect _ score Betweenness Closeness

<!-- b000733 | furniture | pages [18] -->


<!-- b000734 | caption | pages [18] -->
Figure 7: conspirator networks: the higher score of node is, the bigger node

<!-- b000735 | prose | pages [18] -->
size is, and the redder node color is.

<!-- b000736 | furniture | pages [18] -->


<!-- b000737 | furniture | pages [19] -->
Team#16075

<!-- b000738 | furniture | pages [19] -->


<!-- b000739 | furniture | pages [19] -->
Page 17 of 20

<!-- b000740 | caption | pages [19] -->
Table 7: indexes and leader detect score of top 5 conspirators

<!-- b000741 | prose | pages [19] -->
Betweenness Index Name Degree

<!-- b000742 | prose | pages [19] -->
3 Sherri 0.7407

<!-- b000743 | prose | pages [19] -->
7 Elsie 0.7037

<!-- b000744 | prose | pages [19] -->
67 Yao 0.7037

<!-- b000745 | prose | pages [19] -->
21 Alex 0.6667

<!-- b000746 | prose | pages [19] -->
32 Gretchen 0.5556

<!-- b000747 | prose | pages [19] -->
Closeness Leader Detect Score

<!-- b000748 | prose | pages [19] -->
0.1824 0.1015 1.0247

<!-- b000749 | prose | pages [19] -->
0.2209 0.0988 1.0233

<!-- b000750 | prose | pages [19] -->
0.1029 0.1097 0.9163

<!-- b000751 | prose | pages [19] -->
0.0947 0.1097 0.8711

<!-- b000752 | prose | pages [19] -->
0.1578 0.1015 0.8148

<!-- b000753 | prose | pages [19] -->
From figure 7 and table 7, we can conclude that:

<!-- b000754 | prose | pages [19] -->
 Sherri has the most possibility of becoming the leader of the network.

<!-- b000755 | prose | pages [19] -->
 Elsie‘s score is quiet close to Sherri. They may cooperate in plan of crime.

<!-- b000756 | prose | pages [19] -->
 Degree is key index, which contributes over half score in final result.

<!-- b000757 | prose | pages [19] -->
 Gretchen is a senior manager in the company, who ranks fifth in leader

<!-- b000758 | prose | pages [19] -->
detection. He is worth of paying special attention during investigation.

<!-- b000759 | heading | pages [19] -->
7.1.3 Analysis of three suspicious topic

<!-- b000760 | prose | pages [19] -->
We discuss the affect of three suspicious topics to depict characteristics of conspirators‘ net work in another respect. Indexes involved are active index, nodes related index, and average score of nodes index.

<!-- b000761 | prose | pages [19] -->
Active index measures the number of message traffic in specific topic. The more a topic is talked about, the more message of it is, and higher active index is. Nodes related index is the number of person involved in the topic. Average score of nodes index is the average of conspirator likelihood score of people involved in the topic.

<!-- b000762 | furniture | pages [19] -->


<!-- b000763 | caption | pages [19] -->
Figure 8: the visualized node layout of topic 7, 11, 13

<!-- b000764 | caption | pages [19] -->
Table 8: indexes of topic 7, 11, 13

<!-- b000765 | prose | pages [19] -->
Topic 7 Topic Index

<!-- b000766 | prose | pages [19] -->
Active Index

<!-- b000767 | prose | pages [19] -->
Nodes Related Index

<!-- b000768 | prose | pages [19] -->
Topic 11 Topic 13

<!-- b000769 | prose | pages [19] -->
40 35 29

<!-- b000770 | prose | pages [19] -->
40 44 35

<!-- b000771 | prose | pages [19] -->
32.78 Average Score Index

<!-- b000772 | furniture | pages [19] -->


<!-- b000773 | prose | pages [19] -->
30.50 36.60

<!-- b000774 | furniture | pages [19] -->


<!-- b000775 | furniture | pages [19] -->


<!-- b000776 | furniture | pages [20] -->
Team#16075

<!-- b000777 | furniture | pages [20] -->


<!-- b000778 | prose | pages [20] -->
/通用格式

<!-- b000779 | prose | pages [20] -->
/通用格式

<!-- b000780 | prose | pages [20] -->
/通用格式

<!-- b000781 | prose | pages [20] -->
/通用格式

<!-- b000782 | prose | pages [20] -->
/通用格式

<!-- b000783 | prose | pages [20] -->
/通用格式

<!-- b000784 | prose | pages [20] -->
/通用格式

<!-- b000785 | prose | pages [20] -->
`

<!-- b000786 | prose | pages [20] -->
/通用格式

<!-- b000787 | prose | pages [20] -->
/通用格式

<!-- b000788 | prose | pages [20] -->
/通用格式

<!-- b000789 | prose | pages [20] -->
/通用格式

<!-- b000790 | prose | pages [20] -->
Topic 7 Topic 11

<!-- b000791 | furniture | pages [20] -->
Page 18 of 20

<!-- b000792 | prose | pages [20] -->
Active Index

<!-- b000793 | prose | pages [20] -->
Nodes Related Index

<!-- b000794 | prose | pages [20] -->
Average Score Index

<!-- b000795 | prose | pages [20] -->
Topic 13

<!-- b000796 | furniture | pages [20] -->


<!-- b000797 | caption | pages [20] -->
Figure 9: indexes of topic 7, 11, 13

<!-- b000798 | heading | pages [20] -->
Conclusion:

<!-- b000799 | prose | pages [20] -->
 Topic 7 has an active index of 40, which is the highest. It might be a topic

<!-- b000800 | prose | pages [20] -->
discussing a specific plan in conspiracy.

<!-- b000801 | prose | pages [20] -->
 Nodes related index of Topic 11 is higher significantly, in which there are more

<!-- b000802 | prose | pages [20] -->
members involved. It is a general discussion.

<!-- b000803 | prose | pages [20] -->
 People talking about topic 13 have more conspiracy possibility, which the

<!-- b000804 | prose | pages [20] -->
third index describes.

<!-- b000805 | heading | pages [20] -->
7.1.4 Top Conspirators Analysis

<!-- b000806 | prose | pages [20] -->
Now, we investigate five people who have the highest conspiracy possibility as a sample to grasp characteristics of conspirators in the network. The indexes defined above, which are degree, betweenness, and closeness are considered to evaluate their significance in this network.

<!-- b000807 | furniture | pages [20] -->


<!-- b000808 | caption | pages [20] -->
Figure 10: top five conspirator nodes with their neighbors, nodes size and color

<!-- b000809 | prose | pages [20] -->
reflect final score

<!-- b000810 | furniture | pages [20] -->


<!-- b000811 | furniture | pages [21] -->
Team#16075

<!-- b000812 | furniture | pages [21] -->


<!-- b000813 | furniture | pages [21] -->
Page 19 of 20

<!-- b000814 | caption | pages [21] -->
Table 9: indexes and score of top five conspirator nodes

<!-- b000815 | prose | pages [21] -->
Index Name Data Degree

<!-- b000816 | prose | pages [21] -->
7 Elsie 7.8 0.24

<!-- b000817 | prose | pages [21] -->
21 Alex 8.6 0.24

<!-- b000818 | prose | pages [21] -->
3 Sherri 4.2 0.26

<!-- b000819 | prose | pages [21] -->
67 Yao 9.0 0.18

<!-- b000820 | prose | pages [21] -->
44 Patricia 7.5 0.21

<!-- b000821 | prose | pages [21] -->
Condition:

<!-- b000822 | prose | pages [21] -->
Betweenness Closeness Score

<!-- b000823 | prose | pages [21] -->
0.10 0.04 100.00

<!-- b000824 | prose | pages [21] -->
0.04 0.04 90.08

<!-- b000825 | prose | pages [21] -->
0.18 0.04 73.18

<!-- b000826 | prose | pages [21] -->
0.05 0.04 72.73

<!-- b000827 | prose | pages [21] -->
0.04 0.04 70.88

<!-- b000828 | prose | pages [21] -->
 A person who has high values of data and degree will be considered

<!-- b000829 | prose | pages [21] -->
conspirator first.

<!-- b000830 | prose | pages [21] -->
 The deeper a person involved in suspicious topic and suspicious person, the

<!-- b000831 | prose | pages [21] -->
higher score is.

<!-- b000832 | prose | pages [21] -->
 The increasing of communication capacity in network lifts final score.

<!-- b000833 | heading | pages [21] -->
7.1.5 Final Conclusion

<!-- b000834 | prose | pages [21] -->
Nodes in the conspirators‘ network are linked closely. They communicate directly without intermediate nodes. Although the total network has some feature of hierarchy. Issues of conspiracy are still being discussed. There is not a main conspiracy topic. To participate in the conspiracy, a person will conduct many activities related to the conspiracy inevitably.

<!-- b000835 | heading | pages [21] -->
7.2 Simulation: The promotion of the model

<!-- b000836 | prose | pages [21] -->
In process of model building, we have used many network techniques to empower our model. And in network analysis, indexes about nodes and edges are often used. For a specific network, there are always related information about nodes and edges in network. We both use the common and feature of network to build our model, with the goal that making the estimating result more accurate.

<!-- b000837 | prose | pages [21] -->
Degree, betweenness and closeness are common properties of nodes in a network. They describe basic characteristics of nodes, which also reflect the features of interactions made by nodes on other nodes of the network.

<!-- b000838 | prose | pages [21] -->
In this problem of crime busting, we take some particular conditions that have strongly correlations with conspiracy communication network, for example, suspicious topic and persons, into account, which improve accuracy of model too.

<!-- b000839 | prose | pages [21] -->
So, based on these conclusion, we state a general approach, by which can identify, prioritize, and categorize similar nodes in a network as follows:

<!-- b000840 | prose | pages [21] -->
 First, perform statistics of various network properties of nodes on the network

<!-- b000841 | prose | pages [21] -->
analyzed to estimate general characteristics of that network.

<!-- b000842 | prose | pages [21] -->
 Then, according to features of specified network, transform them into indexes

<!-- b000843 | prose | pages [21] -->
about nodes and edges just like what we do in our model.

<!-- b000844 | prose | pages [21] -->
 Finally, combine both of them together into a weighted average. And that is a

<!-- b000845 | prose | pages [21] -->
score mesures nodes with the given standard. With this score of result, identify, prioritize, and categorize similar nodes in network.

<!-- b000846 | furniture | pages [21] -->


<!-- b000847 | furniture | pages [22] -->
Team#16075

<!-- b000848 | furniture | pages [22] -->
Page 20 of 20

<!-- b000849 | furniture | pages [22] -->


<!-- b000850 | heading | pages [22] -->
8 Strengths and Weaknesses

<!-- b000851 | heading | pages [22] -->
8.1 Strengths:

<!-- b000852 | prose | pages [22] -->
 Comprehensive: we take both the message and node position into consideration

<!-- b000853 | prose | pages [22] -->
for identifying, prioritizing and categorizing. So, the solution of our model pursues high credibility, while reducing the misjudgment rate.  Reasonable: the result of our model match perfectly with the experience, which

<!-- b000854 | prose | pages [22] -->
proves the  rationality and correctness of our model  Extendable: the result of simulation shows that our model can be applied to other

<!-- b000855 | prose | pages [22] -->
field, not just crime busting.  Flexible: We can‘t judge a person to be conspiratorial or innocent only based on

<!-- b000856 | prose | pages [22] -->
the message traffic. Since everything may be an accident, our model has its false positive rate which allows the unexpected things to happen.

<!-- b000857 | heading | pages [22] -->
8.2 Weaknesses:

<!-- b000858 | prose | pages [22] -->
 We don‘t take the Criminal Psychology into consideration while the simple

<!-- b000859 | prose | pages [22] -->
example shows that some people may lie during the taping.  Since there is no clear criteria for the classification, those conspirators who are

<!-- b000860 | prose | pages [22] -->
slightly behind may be changed while the conspirators ranking in the front remain unchanged.

<!-- b000861 | heading | pages [22] -->
8.3 Future work:

<!-- b000862 | prose | pages [22] -->
 We will apply semantic network analysis to discovery the potential linkage

<!-- b000863 | prose | pages [22] -->
between the messages and scientifically classify them into different groups. Our model will be enhanced to a large extent.  Find reasonable criteria for the classification to distinguish the conspirators from

<!-- b000864 | prose | pages [22] -->
the innocent.

<!-- b000865 | heading | pages [22] -->
9 References

<!-- b000866 | references | pages [22] -->
[1] Krebs, V.E. （2001）. Mapping networks of terrorist cells. Connections, 24(3),

<!-- b000867 | references | pages [22] -->
43-52.

<!-- b000868 | references | pages [22] -->
[2] McAndrew, D. (1999). The structural analysis of criminal networks, in The social

<!-- b000869 | references | pages [22] -->
psychology of crime: Groups, teams, and networks, offender profiling series, iii,

<!-- b000870 | references | pages [22] -->
D.Canter & L.Alison (eds.). Aldershot: Dartmouth.

<!-- b000871 | references | pages [22] -->
[3] U.K. Wiil, J.Gniadek, N.Memon. (2010). Measuring Link Importance in Terrorist

<!-- b000872 | references | pages [22] -->
Networks. 2010 International Conference on Advances in Social Networks Analysis

<!-- b000873 | references | pages [22] -->
and Mining. 225-232.

<!-- b000874 | references | pages [22] -->
[4] Jennifer J.XU and Hsinchun Chen.(2005). CrimeNet Explorer: A Framework for

<!-- b000875 | references | pages [22] -->
CriminalNetwork Knowledge Discovery. ACM Transactions on Information Systems,

<!-- b000876 | references | pages [22] -->
23(2), 201–226.

<!-- b000877 | references | pages [22] -->
[5] Freeman, L.C. (1979). Centrality in social networks: Conceptual clarification.

<!-- b000878 | references | pages [22] -->
Social Networks, 1, 215-240.

<!-- b000879 | references | pages [22] -->
[6] Mika, S.Ratsch, G.Weston, J.Scholkopf, B.Mullers, K.R.. (1999). Fisher

<!-- b000880 | references | pages [22] -->
Discriminant Analysis With Kernels.  Neural Networks for Signal Processing

<!-- b000881 | references | pages [22] -->
IX,Proceedings of the 1999 IEEE Signal Processing Society Workshop, 41-48.

<!-- b000882 | furniture | pages [22] -->

