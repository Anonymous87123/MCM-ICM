# P-C-2012-15356-6b8f0a28

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #: 15356                                                                  Page 1 of 20

<!-- b000002 | furniture | pages [1] -->
Team Control Number

<!-- b000003 | title | pages [1] -->
15356

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | prose | pages [1] -->
T1 ________________

<!-- b000007 | prose | pages [1] -->
F1 ________________

<!-- b000008 | prose | pages [1] -->
T2 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | prose | pages [1] -->
Problem Chosen

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | title | pages [1] -->
c

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
iRank Model: A New Approach To Criminal Network Detection

<!-- b000020 | heading | pages [1] -->
Summary

<!-- b000021 | prose | pages [1] -->
How to detect all the members and the leader of a conspiracy to commit a criminal act has long been the major concern of the Intergalactic Crime Modelers (ICM). The previous method is far from efficient for the current fund fraud conspiracy which involved over 21,000 words of message traffic. Here we will develop a more reliable network analysis model for large volumes of crime conspiracies data and other kinds of network data.

<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | prose | pages [1] -->
With the assumption of neglecting the time effect of the communication and assigning specific weightings to conspiratorial and irrelevant messages respectively, we develop an iRank rating model to unearth the hidden structure of the criminal network in the current fund fraud conspiracy. It is a modified version of PageRank algorithm which considers both the conspiratorial communication records and the communication density in  conspirators network to determine the ranking of conspirators.  Also inspired by Social Network Analysis clustering, the model contains a closeness factor to separate the conspirators and non-conspirators and the factor can help us detect the leader of the conspirators.  The model outputs the suspicion level of each suspect quantitatively as a priority list.

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | prose | pages [1] -->
To further improve the models, we take other elements like time series and contents of the messages into consideration. In the advanced criminal network detection model, we can detect the initiator of all the conspiratorial topics thus to lock the major suspect and avoid suing some innocent people who unconsciously spread conspiratorial in the network. Moreover, we will demonstrate how semantic network analysis and text analysis can improve the accuracy of the judgments by detecting some well-hidden conspirators like Inez and Bob in the first example.

<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | prose | pages [1] -->
In the final step, we validate the results by setting a critical value to the iRank value through conspirator group size estimation and visualization.  Furthermore we will analyze the strengths and weaknesses of the models comparing with PageRank algorithm and Social Network Analysis. In addition, we discuss how the model can be extended to other social network applications like biological systems

<!-- b000028 | furniture | pages [2] -->
Team #: 15356                                                                  Page 2 of 20

<!-- b000029 | heading | pages [2] -->
Introduction

<!-- b000030 | prose | pages [2] -->
Detecting criminal network within large amount of data is a well-studied problem in the real world. It is especially important to develop techniques for uncovering conspiracy networks involving white-collar crimes. In most of the cases, such well-organized criminal activities will follow some patterns. Thus we can uncover the structures of this kind of criminal network and nominate the leader of the group by studying reliable data with sophisticated techniques. It would save a lot of endeavors and time for the ICM to conduct their investigation and arrest work in the future.

<!-- b000031 | furniture | pages [2] -->


<!-- b000032 | prose | pages [2] -->
In the given ICM case, it is known that some conspirators are taking place to embezzle funds from the company and use internet fraud to steal funds from credit cards of people who do business with the company. Here, our goal is to separate the non-conspirators from the ones who are most likely to be conspirators. We will consider:

<!-- b000033 | prose | pages [2] -->
the development of criteria and methods to detect the criminal network and  the leader of the group

<!-- b000034 | prose | pages [2] -->
the application of semantic network analysis and text analysis to improve the  method

<!-- b000035 | prose | pages [2] -->
further recommendations and other applications of the model 

<!-- b000036 | furniture | pages [2] -->


<!-- b000037 | prose | pages [2] -->
Dataset Observations and Basic Statistical Analysis

<!-- b000038 | prose | pages [2] -->
To better understand different communication behaviors of conspirators and non-conspirators and to elaborate our assumptions, we conduct a statistical analysis for the given data. In task 1, given that Jean, Alex, Elsie, Paul, Ulf, Yao, and Harvey are conspirators while Darlene, Tran, Jia, Ellin, Gard, Chris, Paige, and Este are innocent, we reach some useful findings for model building. There are two “Elsie’s” in the company, No.7 and No.37. As the No.7 obviously has more connections with the other known conspirators, we lock No.7 as the conspirator.

<!-- b000039 | furniture | pages [2] -->


<!-- b000040 | furniture | pages [2] -->


<!-- b000041 | caption | pages [2] -->
Figure 1: Comparison of number of topics conversed by conspirators or

<!-- b000042 | prose | pages [2] -->
non-conspirators

<!-- b000043 | furniture | pages [3] -->
Team #: 15356                                                                  Page 3 of 20

<!-- b000044 | prose | pages [3] -->
In Figure 1, from the total number of conversations (left bar), we can see that conspirators are significantly more active than non-conspirators. They tend to communicate more often with other people. The information exchanges among known conspirators groups are also significantly more frequent than that among known non-conspirators.

<!-- b000045 | furniture | pages [3] -->


<!-- b000046 | prose | pages [3] -->
Carefully examining into the patterns of information exchanges and social connections in the network, we can see that only 24% messages carry conspiratorial information, which seems not systematically significant given that 20% of all the topics are conspiratorial. Therefore, two patterns can be inferred from the statistical results:

<!-- b000047 | furniture | pages [3] -->


<!-- b000048 | prose | pages [3] -->
Although conspirators are generally more active than the known innocent  people, they exchange irrelevant information with each other. Conspiratorial messages only take a small portion in their message traffic.

<!-- b000049 | furniture | pages [3] -->


<!-- b000050 | prose | pages [3] -->
Since the existing 7 conspirators have already involved in spreading about 40%  of the total conspiratorial messages, it is very likely that the total number of conspirators is less than 20.

<!-- b000051 | furniture | pages [3] -->


<!-- b000052 | furniture | pages [3] -->


<!-- b000053 | caption | pages [3] -->
Figure 2: Messages with conspiratorial topics conveyed by conspiracies and

<!-- b000054 | prose | pages [3] -->
non-conspiracies

<!-- b000055 | furniture | pages [3] -->


<!-- b000056 | prose | pages [3] -->
Another pattern we can derive from the original dataset is the correlation between the involvement of conspiratorial activities and the identity of the worker. We observe a few non-conspirators who have involved in talks with conspiratorial topics. Nevertheless, most of the non-conspirators only receive those messages and seldom give responses to them. Thus, the initiators of such a conversation should have more suspicion. Therefore, we can assume that the motivation of participating in conspiratorial topics is one of the most important indicators of a given worker’s identity.

<!-- b000057 | furniture | pages [4] -->
Team #: 15356                                                                  Page 4 of 20

<!-- b000058 | prose | pages [4] -->
Symbols and Definitions

<!-- b000059 | prose | pages [4] -->
Symbol Definition G Society network graph N A set of labeled nodes Formula

<!-- b000060 | furniture | pages [4] -->


<!-- b000061 | furniture | pages [4] -->


<!-- b000062 | prose | pages [4] -->
Nodes represent the conspirators nc

<!-- b000063 | furniture | pages [4] -->


<!-- b000064 | prose | pages [4] -->
Nodes represent the unknown nu

<!-- b000065 | furniture | pages [4] -->


<!-- b000066 | prose | pages [4] -->
Nodes represent the non-conspirators

<!-- b000067 | prose | pages [4] -->
nn

<!-- b000068 | furniture | pages [4] -->


<!-- b000069 | prose | pages [4] -->
The message sent from node i to node j

<!-- b000070 | prose | pages [4] -->
lij

<!-- b000071 | prose | pages [4] -->
L A set of labeled links

<!-- b000072 | furniture | pages [4] -->


<!-- b000073 | prose | pages [4] -->
Links contain conspiratorial messages Lc

<!-- b000074 | furniture | pages [4] -->


<!-- b000075 | prose | pages [4] -->
Links contain irrelevant messages Ln D Degrees of each node

<!-- b000076 | prose | pages [4] -->
O Out-degree

<!-- b000077 | prose | pages [4] -->
I In-degree

<!-- b000078 | prose | pages [4] -->
CL Centrality of each node

<!-- b000079 | prose | pages [4] -->
IR iRank model value

<!-- b000080 | furniture | pages [4] -->


<!-- b000081 | prose | pages [4] -->
= Number of links connected to node n = Out-degree of node n = In-degree of node n = Centrality of node n = Ranking weight of node n The link weight between two given nodes  αij =Link weight between α

<!-- b000082 | prose | pages [4] -->
f The heuristic function the ith and jth node f(l) = Heuristic function of link l Number of messages the node n sends nc msn to and receives from nc

<!-- b000083 | furniture | pages [4] -->


<!-- b000084 | prose | pages [4] -->
Number of messages the node n receives mrn from nc

<!-- b000085 | furniture | pages [4] -->


<!-- b000086 | prose | pages [4] -->
Number of times the node n sends lc tsn

<!-- b000087 | furniture | pages [4] -->


<!-- b000088 | prose | pages [4] -->
Number of times the node n receives lc trn

<!-- b000089 | furniture | pages [4] -->


<!-- b000090 | prose | pages [4] -->
Adjusting factor used to standardize the w units into a same scale

<!-- b000091 | furniture | pages [4] -->


<!-- b000092 | prose | pages [4] -->
Harmonic series of the number of times hs

<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | prose | pages [4] -->
that node n sends a conspiratorial message to a known conspirator

<!-- b000095 | prose | pages [4] -->
Harmonic series of the number of times hr

<!-- b000096 | furniture | pages [4] -->


<!-- b000097 | prose | pages [4] -->
that node n receives a suspicious message from a known conspirator

<!-- b000098 | prose | pages [4] -->
d Heuristic function of closeness

<!-- b000099 | furniture | pages [4] -->


<!-- b000100 | prose | pages [4] -->
d(n)= Heuristic function of closeness from node n to nc and nn

<!-- b000101 | furniture | pages [5] -->
Team #: 15356                                                                  Page 5 of 20

<!-- b000102 | heading | pages [5] -->
Assumptions

<!-- b000103 | prose | pages [5] -->
The criminal network problems can be really complicated if we take every effect into consideration. In Task 1 and Task 2, we simplify the model by assuming that:

<!-- b000104 | furniture | pages [5] -->


<!-- b000105 | prose | pages [5] -->
Only the7th, the 11st and the 13rd topics are related to conspiracy in Task 1,  and in Task 2 the 1st topic is added to the topics related to conspiracy;

<!-- b000106 | furniture | pages [5] -->


<!-- b000107 | prose | pages [5] -->
All the messages are exchanged in a very short period, thus the impact of  time can be neglected;

<!-- b000108 | furniture | pages [5] -->


<!-- b000109 | prose | pages [5] -->
The contents of the messages can be temporarily ignored, thus all the  conspiratorial topics are equally weighted.

<!-- b000110 | furniture | pages [5] -->


<!-- b000111 | prose | pages [5] -->
A message that involves k (k>1) topics is equivalent to k messages that each  involves 1 corresponding topic.  This is valid because we ignore the time effect of communication, and focus on the amount of information exchanged only.

<!-- b000112 | furniture | pages [5] -->


<!-- b000113 | prose | pages [5] -->
Meanwhile, according to the basic statistical results of the dataset, we can have the following assumptions.

<!-- b000114 | furniture | pages [5] -->


<!-- b000115 | prose | pages [5] -->
Non-conspirators do not know about who are conspirators. 

<!-- b000116 | prose | pages [5] -->
Non-conspirators seldom talk about conspiratorial topics with conspirators. 

<!-- b000117 | prose | pages [5] -->
Conspirators do talk conspiratorial topics with non-conspirators. 

<!-- b000118 | prose | pages [5] -->
The identity of an unknown node is determined by its neighboring nodes and  the links incident with it.

<!-- b000119 | furniture | pages [5] -->


<!-- b000120 | furniture | pages [5] -->


<!-- b000121 | furniture | pages [6] -->
Team #: 15356                                                                  Page 6 of 20

<!-- b000122 | prose | pages [6] -->
Task 1

<!-- b000123 | heading | pages [6] -->
The Mathematical Model — iRank Model

<!-- b000124 | prose | pages [6] -->
The aim of the task is to obtain a priority list according to the likelihood of being part of the conspiracy and to determine whether any of the senior managers are involved.  In this task we develop an iRank Model which is a combination of PageRank Algorithm and SNA technique. We apply this modified model in this problem as the original PageRank Algorithm cannot deal with links with different weights and the SNA technique does not take the identities of the nodes into consideration(Xu and Chen 2005).

<!-- b000125 | furniture | pages [6] -->


<!-- b000126 | prose | pages [6] -->
For the likelihood of being a conspirator, intuitively a person’s suspicious level relates to the percentage of conspirators he contacts and the percentage of suspicious messages he involves in.  Furthermore, a person seems even more suspicious when he sends a suspicious message to a known conspirator, or receives a suspicious message from a known conspirator.  Therefore we can consider a function that ranks each suspect by the factors mentioned above as our selection criteria to find out possible conspirators.

<!-- b000127 | furniture | pages [6] -->


<!-- b000128 | prose | pages [6] -->
In addition, in a normal social group the social activities should be evenly emerged along with the organizational structure to a certain extent. We believe the conspirator group as a sub-group in this company would cause abnormal social activity patterns reflected on their behaviors of communication. Specifically, based on Small World Theory(Natarajan 2006) which raised the relationship closeness of any two people among a social group, we pay attention to patterns of all nu connect to the conspirator group as well as the non-conspirator group. By our model, the abnormal distribution of social activities within the company caused by conspirator group can be tracked and related useful information, which helps us to distinguish people’s identities, can also be derived from it.

<!-- b000129 | furniture | pages [6] -->


<!-- b000130 | prose | pages [6] -->
To determine the conspiracy leaders, we will iteratively review how a person makes influence on the conspirator groups, or the degree of centrality we defined as follow, to find out a person’s impact among known conspirators.

<!-- b000131 | furniture | pages [6] -->


<!-- b000132 | prose | pages [6] -->
The iRank Model includes two steps: initialization and iteration.

<!-- b000133 | furniture | pages [6] -->


<!-- b000134 | prose | pages [6] -->
Step 1:  Initialization

<!-- b000135 | prose | pages [6] -->
The initialization offers a initial suspicious level to all nodes with unknown

<!-- b000136 | furniture | pages [7] -->
Team #: 15356                                                                  Page 7 of 20

<!-- b000137 | prose | pages [7] -->
identity nu.  Consider the iRank value IR(n) as the suspicious level of node n. Intuitively we have:

<!-- b000138 | furniture | pages [7] -->


<!-- b000139 | prose | pages [7] -->
IR(n) = Suspicion raised by the frequency of contacting nc

<!-- b000140 | prose | pages [7] -->
+Suspicion raised by the frequency of exchanging lc + Suspicion raised by the communication distance to nc        (1.1)

<!-- b000141 | furniture | pages [7] -->


<!-- b000142 | prose | pages [7] -->
Let    ,     denote the number of messages the n-th node sends to and receives from nc, respectively, and let     ,     denote the number of times the n-th node sends and receives lc, respectively.  Also let Cn be the centrality of node n and CL(nc ), CL(nn) denote the closeness from node n to nc and nn.

<!-- b000143 | furniture | pages [7] -->


<!-- b000144 | prose | pages [7] -->
Assume each part in (1.1) plays an equal importance in detecting conspiracy. Let    ,    ,     , and     denote the adjusting factor used to standardize the units into a same scale so that each part is assigned a same weight in IR(n). Therefore we can set up the following iRank function to assign an initial weight to each node.

<!-- b000145 | furniture | pages [7] -->


<!-- b000146 | furniture | pages [7] -->


<!-- b000147 | furniture | pages [7] -->


<!-- b000148 | furniture | pages [7] -->


<!-- b000149 | furniture | pages [7] -->


<!-- b000150 | furniture | pages [7] -->


<!-- b000151 | furniture | pages [7] -->


<!-- b000152 | furniture | pages [7] -->


<!-- b000153 | furniture | pages [7] -->


<!-- b000154 | furniture | pages [7] -->


<!-- b000155 | furniture | pages [7] -->


<!-- b000156 | furniture | pages [7] -->


<!-- b000157 | furniture | pages [7] -->


<!-- b000158 | furniture | pages [7] -->


<!-- b000159 | furniture | pages [7] -->


<!-- b000160 | furniture | pages [7] -->


<!-- b000161 | furniture | pages [7] -->


<!-- b000162 | prose | pages [7] -->
where hs(n), hr(n) are the harmonic series of the number of times that node n sends a suspicious message to a known conspirator, or receives a suspicious message from a known conspirator, and

<!-- b000163 | furniture | pages [7] -->


<!-- b000164 | prose | pages [7] -->
where

<!-- b000165 | furniture | pages [7] -->


<!-- b000166 | furniture | pages [7] -->


<!-- b000167 | furniture | pages [7] -->


<!-- b000168 | furniture | pages [7] -->


<!-- b000169 | furniture | pages [7] -->


<!-- b000170 | furniture | pages [7] -->


<!-- b000171 | furniture | pages [7] -->


<!-- b000172 | furniture | pages [7] -->


<!-- b000173 | prose | pages [7] -->
is a heuristic function of closeness from node n to nc and nn. Statistical analysis shows that the strong positive correlation of closeness to conspirator group and the closeness to non-conspirator group, expect that a few nodes demonstrating significantly more closeness towards conspirator group against non-conspirator group as following graph shows.

<!-- b000174 | furniture | pages [8] -->
Team #: 15356                                                                  Page 8 of 20

<!-- b000175 | prose | pages [8] -->
abnormal nodes

<!-- b000176 | furniture | pages [8] -->


<!-- b000177 | caption | pages [8] -->
Figure 3 Abnormal nodes observed by correlation of closeness to conspirator

<!-- b000178 | prose | pages [8] -->
group and non-conspirator group

<!-- b000179 | furniture | pages [8] -->


<!-- b000180 | furniture | pages [8] -->


<!-- b000181 | prose | pages [8] -->
Step 2:  Iteration

<!-- b000182 | prose | pages [8] -->
After obtaining the initial value, we can iteratively adjust the ranking weight of each node to get a more precise iRank value because for a node n its suspicious level IR(n) changes as the iRank values of its neighboring nodes have changed. Consider a rating system that contacting with a more suspicious node will results in a higher IR(n), we can set up the following rating function:

<!-- b000183 | furniture | pages [8] -->


<!-- b000184 | furniture | pages [8] -->


<!-- b000185 | furniture | pages [8] -->


<!-- b000186 | furniture | pages [8] -->


<!-- b000187 | furniture | pages [8] -->


<!-- b000188 | furniture | pages [8] -->


<!-- b000189 | furniture | pages [8] -->


<!-- b000190 | furniture | pages [8] -->


<!-- b000191 | furniture | pages [8] -->


<!-- b000192 | furniture | pages [8] -->


<!-- b000193 | furniture | pages [8] -->


<!-- b000194 | furniture | pages [8] -->


<!-- b000195 | furniture | pages [8] -->


<!-- b000196 | furniture | pages [8] -->


<!-- b000197 | prose | pages [8] -->
where adj(n) denotes a node that receives a message from the n-th node, and denotes the weight of the message from i-th node to j-th node that satisfies

<!-- b000198 | prose | pages [8] -->
.

<!-- b000199 | furniture | pages [8] -->


<!-- b000200 | furniture | pages [8] -->


<!-- b000201 | furniture | pages [8] -->


<!-- b000202 | furniture | pages [8] -->


<!-- b000203 | prose | pages [8] -->
By Markov property, for every    , IR(n) will eventually reach the limit after a large number of iterations, and the final IR(n) will be a credible estimate of the suspicious level of the node.

<!-- b000204 | furniture | pages [8] -->


<!-- b000205 | furniture | pages [9] -->
Team #: 15356                                                                  Page 9 of 20

<!-- b000206 | prose | pages [9] -->
Estimation of Parameters

<!-- b000207 | prose | pages [9] -->
By analyzing the sample data, we have the following statistical results:

<!-- b000208 | furniture | pages [9] -->


<!-- b000209 | prose | pages [9] -->
Task 1 Statistics

<!-- b000210 | prose | pages [9] -->
Sender Topic Receiver Count nc -- nc 26 nc -- nn 6 nn -- nc 5 nn -- nn 10 Sender Topic Receiver Count nc lc -- 31 nn lc -- 3 -- lc nc 28 -- lc nn 7

<!-- b000211 | furniture | pages [9] -->


<!-- b000212 | furniture | pages [9] -->


<!-- b000213 | caption | pages [9] -->
Table 1:   The statistics of suspicious action counts in Task 1

<!-- b000214 | furniture | pages [9] -->


<!-- b000215 | prose | pages [9] -->
Assume that the sample distribution is coherent with the total distribution, based on the observation on the sample data, we can find out

<!-- b000216 | furniture | pages [9] -->


<!-- b000217 | furniture | pages [9] -->


<!-- b000218 | furniture | pages [9] -->


<!-- b000219 | furniture | pages [9] -->


<!-- b000220 | furniture | pages [9] -->


<!-- b000221 | furniture | pages [9] -->


<!-- b000222 | furniture | pages [9] -->


<!-- b000223 | furniture | pages [9] -->


<!-- b000224 | prose | pages [9] -->
As the messages including suspicious topics are more useful for our detection of conspirators than irrelevant messages, we can define

<!-- b000225 | furniture | pages [9] -->


<!-- b000226 | furniture | pages [9] -->


<!-- b000227 | furniture | pages [9] -->


<!-- b000228 | furniture | pages [9] -->


<!-- b000229 | furniture | pages [9] -->


<!-- b000230 | furniture | pages [9] -->


<!-- b000231 | furniture | pages [9] -->


<!-- b000232 | furniture | pages [9] -->


<!-- b000233 | furniture | pages [9] -->


<!-- b000234 | prose | pages [9] -->
where      is the indicator function of whether the message from node n to node x contains suspicious topic, that is

<!-- b000235 | furniture | pages [9] -->


<!-- b000236 | furniture | pages [9] -->


<!-- b000237 | furniture | pages [9] -->


<!-- b000238 | furniture | pages [9] -->


<!-- b000239 | prose | pages [9] -->
Output and Evaluation

<!-- b000240 | prose | pages [9] -->
Node # 81 51 16 33

<!-- b000241 | prose | pages [9] -->
iR 0.8571 0.6244 0.6142 0.5765

<!-- b000242 | prose | pages [9] -->
.

<!-- b000243 | prose | pages [9] -->
57 60 28 79 10

<!-- b000244 | prose | pages [9] -->
0.5667 0.551 0.5377 0.5141 0.4790

<!-- b000245 | caption | pages [9] -->
Table 2:  Significant suspects ranked by IR in Task 1

<!-- b000246 | furniture | pages [10] -->
Team #: 15356                                                                  Page 10 of 20

<!-- b000247 | furniture | pages [10] -->


<!-- b000248 | caption | pages [10] -->
Figure 4: Suspicious level shown by IR

<!-- b000249 | furniture | pages [10] -->


<!-- b000250 | prose | pages [10] -->
To distinguish leaders from the conspirator group we found by our iRank model, we further develope the analytical model to demonstrate the leadership within the group. Firstly, we make following assumptions about the behavior of the leader in a group:

<!-- b000251 | furniture | pages [10] -->


<!-- b000252 | prose | pages [10] -->
The leader usually acts as an intermediate node to connect different  functional sub-groups

<!-- b000253 | furniture | pages [10] -->


<!-- b000254 | prose | pages [10] -->
The leader prefers to communicate with heads in different functional  sub-groups rather than common members.

<!-- b000255 | furniture | pages [10] -->


<!-- b000256 | prose | pages [10] -->
Sub-group heads, as an intermediate node among the leader and the other  members, can access all of their group members.

<!-- b000257 | furniture | pages [10] -->


<!-- b000258 | prose | pages [10] -->
From the above assumptions, the following facts can be inferred:

<!-- b000259 | furniture | pages [10] -->


<!-- b000260 | prose | pages [10] -->
Normally, the leader can achieve one of the highest neighborhood  connectivity among all members, since the leader can connect to all members through those sub-group heads.

<!-- b000261 | furniture | pages [10] -->


<!-- b000262 | prose | pages [10] -->
The leader may not have the smallest average shortest path length since the  number of members in different sub-groups may differ greatly.

<!-- b000263 | furniture | pages [10] -->


<!-- b000264 | furniture | pages [11] -->
Team #: 15356                                                                  Page 11 of 20

<!-- b000265 | prose | pages [11] -->
leadership

<!-- b000266 | furniture | pages [11] -->


<!-- b000267 | caption | pages [11] -->
Figure 5: the correlation between neighborhood connectivity and average

<!-- b000268 | prose | pages [11] -->
shortest path length

<!-- b000269 | furniture | pages [11] -->


<!-- b000270 | prose | pages [11] -->
Obviously, from the chart we infer that those two nodes showing abnormal patterns are very likely the leaders of the whole group. There are No.16 Jerome and No.10 Dolores.

<!-- b000271 | furniture | pages [11] -->


<!-- b000272 | furniture | pages [11] -->


<!-- b000273 | furniture | pages [11] -->


<!-- b000274 | furniture | pages [12] -->
Team #: 15356                                                                  Page 12 of 20

<!-- b000275 | prose | pages [12] -->
Task2

<!-- b000276 | heading | pages [12] -->
Adjusting to the iRank Model

<!-- b000277 | prose | pages [12] -->
We can apply the same model illustrated in Task 1, but we should calculate the new parameters according to the new condition added.

<!-- b000278 | furniture | pages [12] -->


<!-- b000279 | prose | pages [12] -->
Task 2 Statistics

<!-- b000280 | prose | pages [12] -->
Sender Topic Receiver Count nc nc -- 29 nc nn -- 9 nn nc -- 6 nn nn -- 3 Sender Topic Receiver Count nc lc -- 38 nn lc -- 5 lc nc -- 33 lc nn -- 9

<!-- b000281 | caption | pages [12] -->
Table 3: The statistics of suspicious action counts in Task 1

<!-- b000282 | prose | pages [12] -->
From the sample statistics we can find

<!-- b000283 | furniture | pages [12] -->


<!-- b000284 | furniture | pages [12] -->


<!-- b000285 | furniture | pages [12] -->


<!-- b000286 | furniture | pages [12] -->


<!-- b000287 | furniture | pages [12] -->


<!-- b000288 | furniture | pages [12] -->


<!-- b000289 | prose | pages [12] -->
Output

<!-- b000290 | prose | pages [12] -->
By iterating the iRank function 1000 times, we obtain the following results.

<!-- b000291 | prose | pages [12] -->
Node # iR

<!-- b000292 | prose | pages [12] -->
16 0.94099 81 0.86962 51 0.63188 56 0.60522 33 0.58404 57 0.57165 60 0.55354 28 0.54328 10 0.52434 79 0.51788 69 0.48713 13 0.45334 17 0.45170 20 0.45149 22 0.44896 3 0.42529

<!-- b000293 | prose | pages [12] -->
0.41772 15

<!-- b000294 | furniture | pages [12] -->


<!-- b000295 | furniture | pages [12] -->


<!-- b000296 | caption | pages [12] -->
Table 4: The significant suspects ranked by iR in Task 2

<!-- b000297 | furniture | pages [13] -->
Team #: 15356                                                                  Page 13 of 20

<!-- b000298 | furniture | pages [13] -->


<!-- b000299 | caption | pages [13] -->
Figure 6: Visualization of the Criminal Network Based on Task 2 Results

<!-- b000300 | furniture | pages [13] -->


<!-- b000301 | heading | pages [13] -->
Evaluation and Discussion

<!-- b000302 | heading | pages [13] -->
Strength

<!-- b000303 | prose | pages [13] -->
The iRank model perfectly distinguishes every different node and ranks the  suspicion level of all nodes quantitatively because IR(n) considers both the suspicious communication made by node n and the communication density of node n in a social network. For example, in the data set both Node 16 and Node 34 are called Jerome, but the model indicates that Node 16 is the senior manager and further shows that Node 16 is involved in the conspiracy.

<!-- b000304 | furniture | pages [13] -->


<!-- b000305 | prose | pages [13] -->
The iRank model generates an appropriate initial value for each node using  all the information known from the data set, which is better than the original Page Rank algorithm that generates the initial value randomly(Graham and Tsiatas 2010).

<!-- b000306 | furniture | pages [13] -->


<!-- b000307 | prose | pages [13] -->
The iRank model keeps track of the information flow by following the  numerical node weightings and link weightings, which is not considered in general Social Network Analysis clustering(Coffman, Greenblatt et al. 2004).

<!-- b000308 | furniture | pages [13] -->


<!-- b000309 | furniture | pages [14] -->
Team #: 15356                                                                  Page 14 of 20

<!-- b000310 | prose | pages [14] -->
The iRank model is highly efficient in time complexity and space complexity  because it can dynamically adjust the ranking of each node by iteration without performing high dimensional matrix operations by iterations.

<!-- b000311 | furniture | pages [14] -->


<!-- b000312 | heading | pages [14] -->
Weakness

<!-- b000313 | prose | pages [14] -->
The data structure of communication ignores the timing and the sequence of  messages, causing the information loss at the beginning stage. Our iRank model purely regards that, all conversations within the social group are organized as a static directed path of which a node denotes a group member and an edge denotes a message. Obviously, the information of timing and message sequence is fairly helpful in busting up crime syndicates, e.g. it is believed that one initiating a message carrying suspicious topics is more conspiratorial than one replying it.

<!-- b000314 | furniture | pages [14] -->


<!-- b000315 | prose | pages [14] -->
Another major weakness of iRank model is that, our model is not able to  indicate a critical value of conspirators and non-conspirators before reviewing the result of the priority list. Actually, to decide whether a person is a conspirator or not appropriately, we have to go over the data of results in detail and set the critical value manually based on our assumptions.

<!-- b000316 | furniture | pages [14] -->


<!-- b000317 | furniture | pages [14] -->


<!-- b000318 | furniture | pages [14] -->


<!-- b000319 | furniture | pages [14] -->


<!-- b000320 | furniture | pages [15] -->
Team #: 15356                                                                  Page 15 of 20

<!-- b000321 | prose | pages [15] -->
Task 3

<!-- b000322 | heading | pages [15] -->
Improvements on the Criminal Detection Model

<!-- b000323 | prose | pages [15] -->
In the above mathematical model, we assume every irrelevant topic is equally important, and we may ignore some underlying correlations between any two topics.  Next we will improve our model using semantic network analysis and text analysis.

<!-- b000324 | furniture | pages [15] -->


<!-- b000325 | prose | pages [15] -->
Semantic Network Analysis and Text Analysis

<!-- b000326 | prose | pages [15] -->
Semantic Network Analysis is a technique in which the content of a message is extracted from text and represented as a network of semantic relations between actors and issues, which can be queried to look for speciﬁc patterns and answer various research questions.”(Morselli 2010)  In our crime busting model, we can apply this technique to help us extract critical words or messages from the heavy message traffic.

<!-- b000327 | furniture | pages [15] -->


<!-- b000328 | prose | pages [15] -->
As the original messages are not given, here we will just demonstrate our method following the process below. Meanwhile, we will show in detail how this improvement to the criminal network detection model can help lock Inez and Bob in the first example.

<!-- b000329 | furniture | pages [15] -->


<!-- b000330 | caption | pages [15] -->
Figure 7: Semantic Network Analysis Work Flow

<!-- b000331 | furniture | pages [15] -->


<!-- b000332 | prose | pages [15] -->
In the first step, we will extract some conspiratorial or informative messages out from the message traffic.

<!-- b000333 | furniture | pages [15] -->


<!-- b000334 | prose | pages [15] -->
According to some basic criminal psychology knowledge, we can assume that  conspirators are usually under more pressures. We can ask the model to extract any phrases or words that can reveal the abnormal emotions of certain people. For example, in the first case, Inez mentioned two times that she was “tired” or “exhausted”, while Jaye did not have “much going on”. Harry also detected that George was stressed.

<!-- b000335 | furniture | pages [16] -->
Team #: 15356                                                                  Page 16 of 20

<!-- b000336 | furniture | pages [16] -->


<!-- b000337 | prose | pages [16] -->
Secondly, we should also extract messages in other language or which have  some ambiguous statements. It is likely that those are used as codes within the conspirators.

<!-- b000338 | furniture | pages [16] -->


<!-- b000339 | prose | pages [16] -->
Contents or conversations which show high exclusiveness should be pay  attention to, including the invitings to some private talks or meetings.

<!-- b000340 | furniture | pages [16] -->


<!-- b000341 | prose | pages [16] -->
Some messages which contain strong feelings should be extracted ant  analyzed.

<!-- b000342 | furniture | pages [16] -->


<!-- b000343 | prose | pages [16] -->
Also, if the conversation or message has mentioned other people, we will  extract the names and the related activities or descriptive words.

<!-- b000344 | furniture | pages [16] -->


<!-- b000345 | heading | pages [16] -->
The Mathematical Model

<!-- b000346 | prose | pages [16] -->
The model applied is similar to the iRank model in Task 1, but link weight of link l is determined by a text analysis function f(m) instead of a constant that is related to topic involved only.

<!-- b000347 | furniture | pages [16] -->


<!-- b000348 | prose | pages [16] -->
The text analysis function f(m) is judged by comparing the similarity with the message sent by nc or ni.  Inspired by the principal of supervised learning(Wiil, Memon et al. 2010), we can set the initial link weight of lc sent or received by nc to 1, and set the initial link weight of li sent or received by nn is -1.  In this way f(m) is a value from continuous interval [-1,1], and a larger f(m) value implies a greater likelihood of being a suspicious message.

<!-- b000349 | furniture | pages [16] -->


<!-- b000350 | prose | pages [16] -->
Hence we can rewrite the model in the iterative step as:

<!-- b000351 | furniture | pages [16] -->


<!-- b000352 | furniture | pages [16] -->


<!-- b000353 | furniture | pages [16] -->


<!-- b000354 | furniture | pages [16] -->


<!-- b000355 | furniture | pages [16] -->


<!-- b000356 | furniture | pages [16] -->


<!-- b000357 | furniture | pages [16] -->


<!-- b000358 | prose | pages [16] -->
where:

<!-- b000359 | furniture | pages [16] -->


<!-- b000360 | furniture | pages [16] -->


<!-- b000361 | furniture | pages [16] -->


<!-- b000362 | furniture | pages [16] -->


<!-- b000363 | furniture | pages [16] -->


<!-- b000364 | furniture | pages [16] -->


<!-- b000365 | furniture | pages [16] -->


<!-- b000366 | furniture | pages [16] -->


<!-- b000367 | furniture | pages [16] -->


<!-- b000368 | furniture | pages [16] -->


<!-- b000369 | furniture | pages [16] -->


<!-- b000370 | furniture | pages [16] -->


<!-- b000371 | furniture | pages [16] -->


<!-- b000372 | furniture | pages [16] -->


<!-- b000373 | furniture | pages [16] -->


<!-- b000374 | furniture | pages [16] -->


<!-- b000375 | furniture | pages [16] -->


<!-- b000376 | furniture | pages [16] -->


<!-- b000377 | furniture | pages [16] -->


<!-- b000378 | furniture | pages [16] -->


<!-- b000379 | furniture | pages [17] -->
Team #: 15356                                                                  Page 17 of 20

<!-- b000380 | heading | pages [17] -->
Evaluation and Discussion

<!-- b000381 | prose | pages [17] -->
We believe the semantic network analysis and the text analysis can efficiently enhance our model by assigning an appropriate weight for each message according to its own message content rather than assigning a same weight on messages of different importance.  For one hand, as a more irrelevant message owns a smaller weight and a more suspicious message owns a greater weight, the interactions of suspicious message flow will be clearer.  On the other hand, an effective text analysis take the correlation among messages into account, which can provide more accurate link weights and help us find out the underlying relationship among the communication network so that we can get a more credible result.

<!-- b000382 | furniture | pages [17] -->


<!-- b000383 | prose | pages [17] -->
The influence of a suspicious link on the corresponding node is strengthened in the improved model, which can be shown in the following simple numeric example.  In the picture below we can see that in previous model the significant message only contributes 0.5 to IR(n), equal to the contribution of irrelevant messages, whereas in the improved model the significant message contributes 0.9 to IR(n) under same circumstance.

<!-- b000384 | furniture | pages [17] -->


<!-- b000385 | furniture | pages [17] -->


<!-- b000386 | caption | pages [17] -->
Figure 8: The suspicious link contributes more on IR(n) in the improved model

<!-- b000387 | furniture | pages [17] -->


<!-- b000388 | prose | pages [17] -->
The correlation between messages can be found via semantic network analysis and text analysis.  For example, in the topic description given, we can find that the suspicious topic 7 involves Spanish words as codes, and we may further induce that the Spanish words in topic 2 and topic 12 can also be suspicious. Also in topic 4, 5, and 6 we can see some negative feelings like anxiety and complaints, which might infer that the sender is suffering from guilty conscience.

<!-- b000389 | furniture | pages [18] -->
Team #: 15356                                                                  Page 18 of 20

<!-- b000390 | prose | pages [18] -->
Task 4

<!-- b000391 | heading | pages [18] -->
Recommendations and Future Development

<!-- b000392 | prose | pages [18] -->
The IR model performs well in separating the non-conspirators and the conspirators as well as detecting the leader in the criminal network.  However, our models can be further improved by considering the following:

<!-- b000393 | furniture | pages [18] -->


<!-- b000394 | prose | pages [18] -->
Build a thorough network with more messages in the traffic with more links  between any two nodes.  It will increase the accuracy of the results of the model by considering more explicit interactions between the nodes.

<!-- b000395 | furniture | pages [18] -->


<!-- b000396 | prose | pages [18] -->
Introduce time series into the model.  A clear timeline may help us detect  the initiators of certain highly conspiratorial topics. It will also show the pattern changes in the network before and after a conspiracy occurred.

<!-- b000397 | furniture | pages [18] -->


<!-- b000398 | prose | pages [18] -->
Apply text analysis to deal with large volumes of data. Text analysis can help  us in detecting conspiratorial messages or some abnormal expressions efficiently when the dataset is large.

<!-- b000399 | furniture | pages [18] -->


<!-- b000400 | prose | pages [18] -->
Introduce the semantic network analysis. With accumulation of database, we  can uncover some usual tactics in high‐tech conspiracy crimes. For example, some sudden changes in attitudes and conversational styles between two workers may indicate a conspiracy. Also, the increasing frequency of some anxious or stressed words may suggest a conspiratorial event is taking place in the company.

<!-- b000401 | furniture | pages [18] -->


<!-- b000402 | prose | pages [18] -->
Other Applications

<!-- b000403 | prose | pages [18] -->
Besides the study of criminal network detection, we can use this model to deal with various network problems by adjusting the weighting parameters or adding new constraint equations. Here is an example about how this model can be implemented to find infected or diseased cell in biological network.

<!-- b000404 | furniture | pages [18] -->


<!-- b000405 | prose | pages [18] -->
The probability of getting infected is inversely proportional to the distance  between one infected cell and other healthy cells(Chen, Ding et al. 2009), so the weight of being infected between two cells    can be seen as 1/distance.

<!-- b000406 | furniture | pages [18] -->


<!-- b000407 | prose | pages [18] -->
Given some known infected cells, we can assume the infection ability of  different cells have some different probabilities IR(n).

<!-- b000408 | furniture | pages [18] -->


<!-- b000409 | furniture | pages [19] -->
Team #: 15356                                                                  Page 19 of 20

<!-- b000410 | furniture | pages [19] -->


<!-- b000411 | caption | pages [19] -->
Figure 7: The Model of the Infection Cells Detection

<!-- b000412 | furniture | pages [19] -->


<!-- b000413 | furniture | pages [19] -->


<!-- b000414 | furniture | pages [19] -->


<!-- b000415 | furniture | pages [20] -->
Team #: 15356                                                                  Page 20 of 20

<!-- b000416 | heading | pages [20] -->
References

<!-- b000417 | references | pages [20] -->
Chen, H., L. Ding, et al. (2009). "Semantic web for integrated network analysis in

<!-- b000418 | references | pages [20] -->
biomedicine." Briefings in Bioinformatics 10(2): 177-192.

<!-- b000419 | furniture | pages [20] -->


<!-- b000420 | furniture | pages [20] -->


<!-- b000421 | references | pages [20] -->
Coffman, T., S. Greenblatt, et al. (2004). "Graph-based technologies for

<!-- b000422 | references | pages [20] -->
intelligence analysis." Communications of the ACM 47(3): 45.

<!-- b000423 | furniture | pages [20] -->


<!-- b000424 | furniture | pages [20] -->


<!-- b000425 | references | pages [20] -->
Graham, F. and A. Tsiatas (2010). Finding and Visualizing Graph Clusters Using

<!-- b000426 | references | pages [20] -->
PageRank Optimization

<!-- b000427 | references | pages [20] -->
Algorithms and Models for the Web-Graph. R. Kumar and D. Sivakumar, Springer

<!-- b000428 | references | pages [20] -->
Berlin / Heidelberg. 6516: 86-97.

<!-- b000429 | furniture | pages [20] -->


<!-- b000430 | furniture | pages [20] -->


<!-- b000431 | references | pages [20] -->
Morselli, C. (2010). "Assessing Vulnerable and Strategic Positions in a Criminal

<!-- b000432 | references | pages [20] -->
Network." Journal of Contemporary Criminal Justice 26(4): 382-392.

<!-- b000433 | furniture | pages [20] -->


<!-- b000434 | furniture | pages [20] -->


<!-- b000435 | references | pages [20] -->
Natarajan, M. (2006). "Understanding the Structure of a Large Heroin

<!-- b000436 | references | pages [20] -->
Distribution Network: A Quantitative Analysis of Qualitative Data." Journal of

<!-- b000437 | references | pages [20] -->
Quantitative Criminology 22(2): 171-192.

<!-- b000438 | furniture | pages [20] -->


<!-- b000439 | furniture | pages [20] -->


<!-- b000440 | references | pages [20] -->
Wiil, U. K., N. Memon, et al. (2010). "Detecting New Trends in Terrorist

<!-- b000441 | references | pages [20] -->
Networks." 435-440.

<!-- b000442 | furniture | pages [20] -->


<!-- b000443 | furniture | pages [20] -->


<!-- b000444 | references | pages [20] -->
Xu, J. and H. Chen (2005). "Criminal network analysis and visualization."

<!-- b000445 | references | pages [20] -->
Communications of the ACM 48(6): 100-107.

<!-- b000446 | furniture | pages [20] -->


<!-- b000447 | furniture | pages [20] -->


<!-- b000448 | furniture | pages [20] -->


<!-- b000449 | furniture | pages [20] -->

