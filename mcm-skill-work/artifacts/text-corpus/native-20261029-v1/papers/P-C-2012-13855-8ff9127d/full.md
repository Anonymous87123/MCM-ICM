# P-C-2012-13855-8ff9127d

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Crime Busting by An Iterative 2-phase

<!-- b000002 | title | pages [1] -->
Propagation Method

<!-- b000003 | furniture | pages [1] -->
Team # 13855

<!-- b000004 | heading | pages [1] -->
Summary

<!-- b000005 | prose | pages [1] -->
In this article, we develop an efﬁcient method to deal with the problem of ﬁnding out the likelihood of each person involved in a conspiracy. All the possible suspected conspirators work in the same ofﬁce complex and communicate with each other, thus forming a message network. We design a model and develop corresponding methodology to tackle this model and ﬁnally produce a priority list of potential conspirators.

<!-- b000006 | prose | pages [1] -->
We assign each person(i.e. a node in message network) a real number to represent the likelihood of being involved in conspiracy. This number will be updated during the iterative propagation process.

<!-- b000007 | prose | pages [1] -->
We also assign a real number to each topic to indicate how probable this topic is involved in the conspiracy. This number is not ﬁxed and will also be iteratively modiﬁed during the propagation.

<!-- b000008 | prose | pages [1] -->
In the article, we formally deﬁne these two values and develop their for- mulations so that we could design an algorithm that could calculate these two functions.

<!-- b000009 | prose | pages [1] -->
We do several iterations of the following 2-phase propagation process until convergence.

<!-- b000010 | prose | pages [1] -->
Each iteration consists of the following two phases: Person Phase In this phase, we recalculate the suspiciousness of each node, based on the suspiciousness of its neighbours and messages between it and its neighbours.

<!-- b000011 | prose | pages [1] -->
Topic Phase In this phase, we recalculate the suspiciousness of each topic, based on the suspiciousness of people who talk about this topic.

<!-- b000012 | prose | pages [1] -->
We also exploit an exponential decay between two iterations to make the effect of messages attenuate as the distance increase.

<!-- b000013 | prose | pages [1] -->
The ﬁnal suspiciousness of each person is used to produce the priority list of conspirators.

<!-- b000014 | prose | pages [1] -->
At last, we do a series of experiments to evaluate our models and anal- yse the results. We also discuss our model’s sensitivity to the choice of the parameters and its scalability to other applications.

<!-- b000015 | prose | pages [1] -->
1

<!-- b000016 | furniture | pages [2] -->
Team # 13855

<!-- b000017 | furniture | pages [2] -->
Page 2 of 19

<!-- b000018 | heading | pages [2] -->
Contents

<!-- b000019 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | contents | pages [2] -->
1

<!-- b000021 | heading | pages [2] -->
Problem Restatement

<!-- b000022 | prose | pages [2] -->
3

<!-- b000023 | prose | pages [2] -->
Problem Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 3

<!-- b000024 | prose | pages [2] -->
Basic Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 3

<!-- b000025 | prose | pages [2] -->
Models and Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . 4 4

<!-- b000026 | prose | pages [2] -->
Deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 4

<!-- b000027 | prose | pages [2] -->
Preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 5

<!-- b000028 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 Methodology 5

<!-- b000029 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3.1 Overview 5

<!-- b000030 | prose | pages [2] -->
Formulations of S Function . . . . . . . . . . . . . . . . . . . 4.3.2 6

<!-- b000031 | prose | pages [2] -->
Formulations of R Function . . . . . . . . . . . . . . . . . . . 4.3.3 7

<!-- b000032 | prose | pages [2] -->
Exponential Decay . . . . . . . . . . . . . . . . . . . . . . . . 4.3.4 8

<!-- b000033 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

<!-- b000034 | heading | pages [2] -->
Results and Analyses

<!-- b000035 | prose | pages [2] -->
9

<!-- b000036 | prose | pages [2] -->
Requirement 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 9

<!-- b000037 | prose | pages [2] -->
Main Task . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1.1 9

<!-- b000038 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . 5.1.2 Senior Managers 10

<!-- b000039 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . 5.1.3 Conspiracy Leaders 12

<!-- b000040 | prose | pages [2] -->
Evaluation and Further Discussions . . . . . . . . . . . . . . . . . . . . . 6 12

<!-- b000041 | prose | pages [2] -->
Requirement 3: Impacts of NLP developments on our model . . . . 6.1 12

<!-- b000042 | prose | pages [2] -->
Model Sensitivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 13

<!-- b000043 | prose | pages [2] -->
Requirement 2: Changing Prior Knowledge . . . . . . . . . . 6.2.1 13

<!-- b000044 | prose | pages [2] -->
Initial Value for R function 6.2.2 . . . . . . . . . . . . . . . . . . .

<!-- b000045 | prose | pages [2] -->
15

<!-- b000046 | prose | pages [2] -->
Decay rate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2.3 16

<!-- b000047 | prose | pages [2] -->
Requirement 4: Model Scalability and Other Applications . . . . . . 6.3 17

<!-- b000048 | prose | pages [2] -->
Model Drawbacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.4 18

<!-- b000049 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | heading | pages [2] -->
Appendices

<!-- b000051 | prose | pages [2] -->
19

<!-- b000052 | prose | pages [2] -->
Appendix A Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | prose | pages [2] -->
19

<!-- b000054 | furniture | pages [3] -->
Team # 13855

<!-- b000055 | furniture | pages [3] -->
Page 3 of 19

<!-- b000056 | prose | pages [3] -->
1

<!-- b000057 | heading | pages [3] -->
Problem Restatement

<!-- b000058 | prose | pages [3] -->
We are given a group of suspected conspirators who form a communication network by sending messages of various topics to each other. Some of the given people are known to be involved in the conspiracy while some others innocent. We are required to identify the most probable conspirators among the remaining ones.

<!-- b000059 | prose | pages [3] -->
We are also encouraged to ﬁnd out the leaders of the conspiracy and talk about several other topics, such as how could the semantic and text analysis improve our methodology.

<!-- b000060 | prose | pages [3] -->
2 Problem Analysis

<!-- b000061 | prose | pages [3] -->
In order to ﬁnd out the most probable conspirators, we believe that a priority list would be an ideal output. Therefore, we assign the ith person a real number Si (Si ∈[0, 1]) to indicate the likelihood of him involved in the conspiracy.

<!-- b000062 | prose | pages [3] -->
And we try to ﬁgure out a method to eventually determine these numbers.

<!-- b000063 | prose | pages [3] -->
We also believe that topics have their suspiciousness. Different topics suggest different probability of the speakers being conspirators. For example, a cabal who frequently talk about having a secret convention are highly suspicious.

<!-- b000064 | prose | pages [3] -->
On the other hand, we think that the people who are talking about a topic can reversely affect the suspiciousness of that topic. For instance, the conspirators may develop some argots which perhaps seem innocuous and are not considered as suspicious at ﬁrst. Therefore, we make the suspiciousness of a topic changeable following the intuition that frequent mentions among conspirators can make a topic more suspicious.

<!-- b000065 | prose | pages [3] -->
We thereby develop our iterative 2-phase propagation method to solve this problem.

<!-- b000066 | prose | pages [3] -->
3

<!-- b000067 | heading | pages [3] -->
Basic Assumptions

<!-- b000068 | prose | pages [3] -->
In this section, we discuss several key assumptions we have made and ratio- nale for making these assumptions.

<!-- b000069 | prose | pages [3] -->
Assumption 1. We assume that the suspiciousness of a person is determined by both the people with whom he talks and the topics he talk about.

<!-- b000070 | prose | pages [3] -->
We believe that a conspirator may be a good friend to some non-conspirator and they talks of a lot of everyday topics. So being intimate with some highly sus- pected conspirators does not inevitably suggest a extremely high probability of involvement in the conspiracy. We must take both these two factors into account with some elaborate formulations to determine one’s suspiciousness.

<!-- b000071 | prose | pages [3] -->
Assumption 2. We treat the inﬂuence of a message as bidirectional.

<!-- b000072 | furniture | pages [4] -->
Team # 13855

<!-- b000073 | furniture | pages [4] -->
Page 4 of 19

<!-- b000074 | prose | pages [4] -->
For example, no matter one send a suspicious message to a probable conspir- ator or receive one from him, he becomes more suspicious. In Section 4.2, we discuss the preprocessing works we have done to tailor the data to meet this as- sumption.

<!-- b000075 | heading | pages [4] -->
Assumption 3. We assume the suspiciousness of prior known conspirators and non-

<!-- b000076 | prose | pages [4] -->
conspirators to be ﬁxed as 1 and 0 respectively, and will never change during the iterative propagation process.

<!-- b000077 | prose | pages [4] -->
Assumption 4. We treat one message on multiple topics as several messages that each is on a single topic.

<!-- b000078 | prose | pages [4] -->
Assumption 5. We assume the impacts of suspiciousness imposed on a speciﬁc person by different contacts are independent.

<!-- b000079 | prose | pages [4] -->
We explain the rationale for making this assumption in Section 4.3.2 after we present our models.

<!-- b000080 | prose | pages [4] -->
Assumption 6. The impacts of suspiciousness imposed by someone diminish as the dis- tance to this person in the message network becomes longer based on an exponential decay rule.

<!-- b000081 | prose | pages [4] -->
We discuss this in further details in Section 4.3.4.

<!-- b000082 | heading | pages [4] -->
Models and Methodology

<!-- b000083 | prose | pages [4] -->
4

<!-- b000084 | prose | pages [4] -->
4.1 Deﬁnitions

<!-- b000085 | prose | pages [4] -->
Name Deﬁnition Value or Expression PN is the total number of people. PN 83 910 α MN is the total number of messages. MN

<!-- b000086 | prose | pages [4] -->
TN is the total number of topics of messages. TN 15 P is the set of all people(represented by their IDs). P {p|0 ⩽p < PN, p ∈N} T is the set of all topics(represented by their IDs). T {t|1 ⩽t ⩽TN, t ∈N} pi is a speciﬁc person whose id is i, where i ∈P pi ti is a speciﬁc topic whose id is i, where i ∈T ti txy is the topic of the message sent from px to py txy 0 ⩽Si ⩽1 Si is the likelihood of pi involved in the conspiracy. Si 0 ⩽Ri ⩽1 β Ri is the suspiciousness of ti. Ri

<!-- b000087 | prose | pages [4] -->
DRS is the decay rate of the propagation of S function. DRS DRR is the decay rate of the propagation of R function. DRR cDRS = (DRS)n γ cDRS indicates the current degree of decay of S. cDRS

<!-- b000088 | prose | pages [4] -->
cDRS = (DRS)n cDRR indicates the current degree of decay of R. cDRR

<!-- b000089 | prose | pages [4] -->
α We will explicate this value in Section 4.2. β We will give detailed deﬁnitions and formulations of Si and Ri in the following sections. γ n is the # of current iterations.

<!-- b000090 | caption | pages [4] -->
Table 1: Model Deﬁnitions

<!-- b000091 | furniture | pages [5] -->
Team # 13855

<!-- b000092 | furniture | pages [5] -->
Page 5 of 19

<!-- b000093 | prose | pages [5] -->
4.2 Preprocessing

<!-- b000094 | prose | pages [5] -->
Before we present our models, we would like to address the preprocessing works we have done to the data.

<!-- b000095 | prose | pages [5] -->
First, we ﬁnd that there are two self-towards messages, which are sent by p3 and p30 to themselves. We expurgate these two messages since we believe that it makes no sense to send a message to oneself. Also, we discover a message whose topic is 18, which is invalid, so we expurgate this message as well. Still, there are different employees with same names in the ofﬁce complex who are distin- guished primarily by node IDs, are renamed with a sufﬁx though. For instance, p4 Gretchen 1 and p32 Gretchen 2.

<!-- b000096 | prose | pages [5] -->
We build a graph model using the provided data, in which people are vertices and messages are edges.

<!-- b000097 | prose | pages [5] -->
In addition, since we have assumed that a message has bidirectional inﬂuence (in Section 3), we have done the following modiﬁcations to the graph. For each edge in the graph (i.e. a message), we create another message of the same topic whose sender and receiver are swapped, which is a common trick to turn a di- rected graph into an undirected one. For this reason, in the remaining part of this article, every time we mention receiving a message, we mean both sending and receiving a message.

<!-- b000098 | prose | pages [5] -->
When a message contains more than one topics, we split it into several mes- sages for the convenience of manipulation.

<!-- b000099 | prose | pages [5] -->
These preliminary works could answer why M equals 910 rather than 400.

<!-- b000100 | prose | pages [5] -->
4.3 Methodology

<!-- b000101 | prose | pages [5] -->
4.3.1 Overview

<!-- b000102 | prose | pages [5] -->
As we described in the abstract, our method exploits the propagation of sus- piciousness in the message network to determine how likely a person is involved in the conspiracy.

<!-- b000103 | prose | pages [5] -->
Our model can be better understood based on the following intuition. Sus- piciousness can be passed along with the message. i.e. You become more sus- picious when you received a message from a suspected person. On the other hand, the topic of the message can affect the probability of transmission of suspiciousness. Talking with someone about a dubious topic would increase the likelihood of transmitting his suspiciousness to you.

<!-- b000104 | prose | pages [5] -->
Following this intuition, we deﬁned Si for each person pi and Ri for each topic ti and calculate them in turn during an iterative propagation process.

<!-- b000105 | prose | pages [5] -->
Deﬁnition 1 (Person Suspiciousness Function S). Si is the likelihood of person pi to be involved in the conspiracy.

<!-- b000106 | prose | pages [5] -->
Deﬁnition 2 (Topic Suspiciousness Function R). Ri is deﬁned as the suspiciousness transmission rate of topic ti.

<!-- b000107 | furniture | pages [6] -->
Team # 13855

<!-- b000108 | furniture | pages [6] -->
Page 6 of 19

<!-- b000109 | prose | pages [6] -->
We give more speciﬁc deﬁnitions and formulate the expressions of these two functions in Section 4.3.2 and 4.3.3.

<!-- b000110 | prose | pages [6] -->
We do several iterations to calculate the value of S and R. Each iteration con- sists of a P phase and a T phase. In each phase, we use the value of S and R calculated in the previous P&T phases to recalculate the new S or R values.

<!-- b000111 | prose | pages [6] -->
We believe that a direct contact has a far more powerful inﬂuence than an indirect contact, we exploit an exponential decay as the number of iteration grows to make the propagation decrescendo.

<!-- b000112 | prose | pages [6] -->
Algorithm 1 shows an overview of our algorithm.

<!-- b000113 | heading | pages [6] -->
Algorithm 1 Top view of the whole methodology

<!-- b000114 | prose | pages [6] -->
Initialization:

<!-- b000115 | prose | pages [6] -->
Build the graph and assign appropriate initial values to S and R. Iterations:

<!-- b000116 | prose | pages [6] -->
for i = 1 →MAX ITER NUM do

<!-- b000117 | prose | pages [6] -->
PropagateP(cDRS); { P phase with the current decay degree of S} PropagateT(cDRR); { T phase with the current decay degree of R}

<!-- b000118 | prose | pages [6] -->
cDRS ←cDRS ∗DRS; cDRR ←cDRR ∗DRR; end for return S;

<!-- b000119 | prose | pages [6] -->
Formulations of S Function 4.3.2

<!-- b000120 | prose | pages [6] -->
According to the aforementioned discussions and Assumption 1, we try to formulate S function for a person pi based on the impacts imposed by all pi’s neighbours.

<!-- b000121 | prose | pages [6] -->
For a speciﬁc neighbour of pi: pj, we deﬁne the impact imposed on pi by pj as Cji = Sj ∗Rtji.

<!-- b000122 | prose | pages [6] -->
For two distinctive neighbour of pi: pj and pk, we believe that under most circumstances, the presence of Cki has limited effect on Cji. Therefore, we assume Cji and Cki are independent.

<!-- b000123 | prose | pages [6] -->
So for a person pi:

<!-- b000124 | prose | pages [6] -->
∪

<!-- b000125 | prose | pages [6] -->
Si =

<!-- b000126 | prose | pages [6] -->
Cji

<!-- b000127 | prose | pages [6] -->
(j,i)∈M

<!-- b000128 | prose | pages [6] -->
∪

<!-- b000129 | prose | pages [6] -->
= Cji +

<!-- b000130 | prose | pages [6] -->
(k,i)∈M−{j}

<!-- b000131 | prose | pages [6] -->
= . . .

<!-- b000132 | prose | pages [6] -->
. . .

<!-- b000133 | prose | pages [6] -->
∪

<!-- b000134 | prose | pages [6] -->
Cki −Cji ∗

<!-- b000135 | prose | pages [6] -->
Cki (1)

<!-- b000136 | prose | pages [6] -->
(k,i)∈M−{j}

<!-- b000137 | prose | pages [6] -->
We thus convert the calculation of arbitrary union of all pi’s neighbours into one of its sub-problem of calculating ∪

<!-- b000138 | prose | pages [6] -->
Cki.

<!-- b000139 | prose | pages [6] -->
(k,i)∈M−{j}

<!-- b000140 | furniture | pages [7] -->
Team # 13855

<!-- b000141 | furniture | pages [7] -->
Page 7 of 19

<!-- b000142 | prose | pages [7] -->
∪

<!-- b000143 | prose | pages [7] -->
∪ Cki, then use it to calculate

<!-- b000144 | prose | pages [7] -->
Cji. And

<!-- b000145 | prose | pages [7] -->
We could ﬁrst calculate

<!-- b000146 | prose | pages [7] -->
(k,i)∈M−{j}

<!-- b000147 | prose | pages [7] -->
(j,i)∈M

<!-- b000148 | prose | pages [7] -->
we could apply the method in Euqation 1 recursively to convert the calculation ∪

<!-- b000149 | prose | pages [7] -->
Cki into solving its sub-problem until the number of neighbours de-

<!-- b000150 | prose | pages [7] -->
of

<!-- b000151 | prose | pages [7] -->
(k,i)∈M−{j}

<!-- b000152 | prose | pages [7] -->
creases to 1, in which case it simply equals Cki.

<!-- b000153 | prose | pages [7] -->
We design the following Algorithm 2 to calculate Si iteratively based on this method.

<!-- b000154 | heading | pages [7] -->
Algorithm 2 Algorithm for calculating Si

<!-- b000155 | prose | pages [7] -->
Initialization:

<!-- b000156 | prose | pages [7] -->
S and R values are those produced in the last P phase and T phase Set each Cji = Sj ∗Rtji Result ←0 {The reason for using the notation Result instead of Si is to avoid confusion with Si calcualated in last P Phase} Iterations:

<!-- b000157 | prose | pages [7] -->
for all pj ∈pi’s neighbours do

<!-- b000158 | prose | pages [7] -->
Result = Result+Cji−Result∗Cji {Calculate Si iteratively using the method in Equation 1} end for return (1 −cRDS) ∗Si + cRDS ∗Result {We do not use Result directly as Si, becasue of the exponential decay, explained in Section 4.3.4}

<!-- b000159 | prose | pages [7] -->
In the P phase of one iteration, for each pi which is neither known conspira- tor nor known innocent, we use Algorithm 2 to recalculate Si to propagate the suspiciousness to its neighbours.

<!-- b000160 | prose | pages [7] -->
The initial value of S is set as follows: All the known conspirators have S = 1 while known non-conspirators have S = 0. And other ordinary people have S = 0.5.

<!-- b000161 | prose | pages [7] -->
Formulations of R Function 4.3.3

<!-- b000162 | prose | pages [7] -->
As we mentioned before, we believe that topics are also of different suspi- ciousness, which are related to the suspiciousness of those who frequently talks about these topics.

<!-- b000163 | prose | pages [7] -->
In our model, we deﬁne the suspiciousness asscociated with a topic to be the likelihood of the suspiciousness to be passed along the message of that topic.

<!-- b000164 | prose | pages [7] -->
We interpret this deﬁnition by deﬁning R as follows: Suppose pi has only one neighbour pj, which is a known conpirator. We deﬁne Rtji as the probability of pi to be a conspirator.

<!-- b000165 | prose | pages [7] -->
This deﬁnition can be understood this way: All the suspiciousness of pi comes from pj since pj is the only neighbour of pi. And because pj is a known con- spirator, where Sj = 1, Si can reﬂect the likelihood of pj’s suspiciousness to be transmitted to pi.

<!-- b000166 | prose | pages [7] -->
Now we present the formulation of R. Suppose (pj, pi) is a message from pj to

<!-- b000167 | furniture | pages [8] -->
Team # 13855

<!-- b000168 | furniture | pages [8] -->
Page 8 of 19

<!-- b000169 | prose | pages [8] -->
pi of topic tx. According to Equation 1 in Section 4.3.2, we have

<!-- b000170 | prose | pages [8] -->
∪

<!-- b000171 | prose | pages [8] -->
Si =

<!-- b000172 | prose | pages [8] -->
Cki

<!-- b000173 | prose | pages [8] -->
(k,i)∈M

<!-- b000174 | prose | pages [8] -->
∪

<!-- b000175 | prose | pages [8] -->
Sk ∗Rtki

<!-- b000176 | prose | pages [8] -->
=

<!-- b000177 | prose | pages [8] -->
(k,i)∈M

<!-- b000178 | prose | pages [8] -->
∪

<!-- b000179 | prose | pages [8] -->
Sj ∗Rx + =

<!-- b000180 | prose | pages [8] -->
(k,i)∈M−{j}

<!-- b000181 | prose | pages [8] -->
So we have

<!-- b000182 | prose | pages [8] -->
Si −

<!-- b000183 | prose | pages [8] -->
Rx =

<!-- b000184 | prose | pages [8] -->
(2)

<!-- b000185 | prose | pages [8] -->
∪

<!-- b000186 | prose | pages [8] -->
Cki −Sj ∗Rx ∗

<!-- b000187 | prose | pages [8] -->
Cki

<!-- b000188 | prose | pages [8] -->
(k,i)∈M−{j}

<!-- b000189 | prose | pages [8] -->
∪

<!-- b000190 | prose | pages [8] -->
Cki

<!-- b000191 | prose | pages [8] -->
(k,i)∈M−{j}

<!-- b000192 | prose | pages [8] -->
∪

<!-- b000193 | prose | pages [8] -->
(3)

<!-- b000194 | prose | pages [8] -->
Sj ∗(1 −

<!-- b000195 | prose | pages [8] -->
Cki)

<!-- b000196 | prose | pages [8] -->
(k,i)∈M−{j}

<!-- b000197 | prose | pages [8] -->
∪

<!-- b000198 | prose | pages [8] -->
Cki.

<!-- b000199 | prose | pages [8] -->
We could use Algorithm 2 described in Section 4.3.2 to calculate

<!-- b000200 | prose | pages [8] -->
(k,i)∈M−{j}

<!-- b000201 | prose | pages [8] -->
Since there may be many messages sharing a common topic tx, using Equation 3 will yield one Rx for each message, producting several Rx. We then use the arithmatic average to modify Rx under the rule of the exponential decay.

<!-- b000202 | prose | pages [8] -->
Algorithm 3 shows how to calculate Rx at the T phase at a speciﬁc iteration.

<!-- b000203 | heading | pages [8] -->
Algorithm 3 Algorithm for calculating Rx

<!-- b000204 | prose | pages [8] -->
Initialization:

<!-- b000205 | prose | pages [8] -->
S and R values are those produced in the previous P phase and T phase Result ←0 Count ←0 {Count is the number of messages on tx} Iterations:

<!-- b000206 | prose | pages [8] -->
for all edges (pj, pi) where tji = x do

<!-- b000207 | prose | pages [8] -->
∪

<!-- b000208 | prose | pages [8] -->
Cki {Using the method in Algorithm 2}

<!-- b000209 | prose | pages [8] -->
Temp ←

<!-- b000210 | prose | pages [8] -->
(k,i)∈M−{j}

<!-- b000211 | prose | pages [8] -->
Si−Temp Sj∗(1−Temp) {Equation 3} Result ←Result + Count ←Count + 1 end for Result ←Result/Count {Taking average over all messages}

<!-- b000212 | prose | pages [8] -->
return (1 −cRDR) ∗Rx + cRDR ∗Result {Exponential decay, explained in Section 4.3.4}

<!-- b000213 | prose | pages [8] -->
The initial value of R is set as follows: All the known suspicious topics have R = 0.7 while all other topics have R = 0.05.

<!-- b000214 | prose | pages [8] -->
In Section 6.2, we discuss some more elaborate allocations of the initial value of R.

<!-- b000215 | prose | pages [8] -->
4.3.4 Exponential Decay

<!-- b000216 | prose | pages [8] -->
As we mentioned, we exploit an exponential decay in the calculation of S and R to make the near people have a stronger inﬂuence than far ones.

<!-- b000217 | furniture | pages [9] -->
Team # 13855

<!-- b000218 | furniture | pages [9] -->
Page 9 of 19

<!-- b000219 | prose | pages [9] -->
To better understand this, consider a simple scenario: a chain. If the message network is a chain with the beginning person a known conspirator and all others unknown, the suspiciousness of the ﬁrst person would keep transmitting to all other people. All the Si on this chain would converge to 1 as the number of iteraions approaches to the inﬁnity.

<!-- b000220 | prose | pages [9] -->
So we do not simply use the S and R calculated in each iteration to replace those calculated in the previous iteration. Instead, we use them to modify the previous results based on the exponential decay rule. This is the reason for the expression at the end of both Algorithm 2 and 3.

<!-- b000221 | prose | pages [9] -->
(1 −cRDS) ∗Si + cRDS ∗Result (1 −cRDR) ∗Rx + cRDR ∗Result

<!-- b000222 | prose | pages [9] -->
cRDS and cRDR shrink to a constant proportion compared with the previous iteration.

<!-- b000223 | prose | pages [9] -->
cDRS = (DRS)n

<!-- b000224 | prose | pages [9] -->
cDRR = (DRR)n

<!-- b000225 | prose | pages [9] -->
where n is the number of the current iteration.

<!-- b000226 | prose | pages [9] -->
DRS and DRR are set to 0.5 in the basic experiments, and we will discuss our model’s sensitivity to different settings of DRS and DRR in Section 6.2.

<!-- b000227 | prose | pages [9] -->
Conseqently, as the iterations proceed, the previous results play an increas- ingly important role while the impacts of current propagation iteration dimin- ishes until convergence.

<!-- b000228 | prose | pages [9] -->
5

<!-- b000229 | heading | pages [9] -->
Results and Analyses

<!-- b000230 | prose | pages [9] -->
In this secion, we discuss the basic results of our models applied to Require- ment 1 and the corresponding analyses. We put the discussion of Requirement 2, 3 and 4 into Section 6.

<!-- b000231 | prose | pages [9] -->
5.1 Requirement 1

<!-- b000232 | prose | pages [9] -->
5.1.1 Main Task

<!-- b000233 | prose | pages [9] -->
In this basic requirement, there are 8 known conspirators 1 and 8 known non- conspirators. There are also 3 known suspicious topics.

<!-- b000234 | prose | pages [9] -->
In this basic experiment, the initial values of different variables and constants are set as follows. All the known conspirators have S = 1 while known non- conspirators have S = 0. And other ordinary people have S = 0.5. All the known suspicious topics have R = 0.7 while all other topics have R = 0.05.

<!-- b000235 | prose | pages [9] -->
When applying our model to this scenario, a priority list of all 83 people is produced, which is shown in Table 2.

<!-- b000236 | prose | pages [9] -->
And the R value for all topics are shown in Table 3.

<!-- b000237 | prose | pages [9] -->
1Because there are two people named Elsie

<!-- b000238 | furniture | pages [10] -->
Team # 13855

<!-- b000239 | furniture | pages [10] -->
S value

<!-- b000240 | furniture | pages [10] -->
S value

<!-- b000241 | furniture | pages [10] -->
ID

<!-- b000242 | furniture | pages [10] -->
ID

<!-- b000243 | prose | pages [10] -->
49 1 38 0.793437 18 1 50 0.790764 21 1 30 0.76857 67 1 32 0.766605 43 1 6 0.760001 7 1 41 0.754968 37 1 44 0.746949 54 1 40 0.724757 81 0.850742 20 0.720356 10 0.847161 8 0.718942 17 0.838916 33 0.714468 13 0.829731 31 0.711505 3 0.819499 24 0.701129 4 0.816793 19 0.695165 28 0.809526 11 0.694822 15 0.806096 27 0.686166 16 0.804627 29 0.685091 34 0.802074 46 0.679116 36 0.798483 42 0.668063 22 0.796896 9 0.667589 47 0.793939 5 0.664651

<!-- b000244 | furniture | pages [10] -->
Page 10 of 19

<!-- b000245 | furniture | pages [10] -->
S value

<!-- b000246 | furniture | pages [10] -->
S value

<!-- b000247 | furniture | pages [10] -->
ID

<!-- b000248 | furniture | pages [10] -->
ID

<!-- b000249 | prose | pages [10] -->
12 0.640781 70 0.224238 60 0.61854 77 0.217232 35 0.611702 73 0.215225 45 0.608586 76 0.204149 14 0.607512 53 0.203252 39 0.551087 55 0.197634 69 0.528206 75 0.18895 1 0.519437 52 0.183797 26 0.475945 58 0.179185 51 0.444996 59 0.176167 72 0.430927 63 0.163895 82 0.409267 61 0.16224 25 0.39586 2 0 80 0.388173 78 0 79 0.366544 0 0 56 0.364273 74 0 57 0.352322 68 0 23 0.287067 48 0 71 0.27554 65 0 62 0.255381 64 0 66 0.239405

<!-- b000250 | caption | pages [10] -->
Table 2: Priority list for Requirement 1

<!-- b000251 | prose | pages [10] -->
R value R value ID ID 1 0.114903 5 0.0474539 2 0.16544 6 0.0839097 3 0.203057 7 0.569282 4 0.0863024 8 0.108256 R value R value ID ID 9 0.133353 13 0.591751 10 0.102462 14 0.13817 11 0.549412 15 0.153815 12 0.0928846

<!-- b000252 | caption | pages [10] -->
Table 3: Suspiciousness of topics(R values) for Requirement 1

<!-- b000253 | prose | pages [10] -->
We ﬁnd out that among all the three suspicious topics, t13 has a slightly larger R value than the other two. And as the data describes, t13 is believed as the key in the conspiracy, which validates our models and methodology.

<!-- b000254 | prose | pages [10] -->
In addition, among all other topics, t2 and t3 have relatively high suspicious- ness. When we put t2 under scrutiny, we ﬁnd that the data show some of the message trafﬁc of t2 contain Spanish words. And based on our model, t2 is rel- atively frequently talked about among suspicious people. So it may be the case that t2 contains some form of argots or jargons which need to be further inves- tigated. Therefore, our model can help to ﬁnd out potentially suspicious topics which could direct the investigation of ICM ofﬁcers.

<!-- b000255 | prose | pages [10] -->
5.1.2 Senior Managers

<!-- b000256 | prose | pages [10] -->
The three senior managers of the company stated in the problem are Gretchen, Jerome and Delores, but there is not anyone whose name is Delores in the name list and we found there is a name called Dolores instead. Furthermore we found

<!-- b000257 | furniture | pages [11] -->
Team # 13855

<!-- b000258 | furniture | pages [11] -->
Page 11 of 19

<!-- b000259 | prose | pages [11] -->
two Gretchen and two Jerome in the name list. In this way, we analyze the ﬁve people, Dolores, two Jerome and two Gretchen whose IDs are 4, 10, 16, 32 and 34.

<!-- b000260 | prose | pages [11] -->
First, we found that these peoples S values are as shown in Table 4.

<!-- b000261 | prose | pages [11] -->
Name & ID Gretchen No.4 Dolores No.10 Jerome No.16 S value 0.816793 0.847161 0.804627 Gretchen No.32 Jerome No.34 0.766605 0.802074

<!-- b000262 | caption | pages [11] -->
Table 4: S values for Senior Managers

<!-- b000263 | prose | pages [11] -->
We can see that the suspiciousness of Dolores No.10, Jerome No.16 , Jerome No.34 and Gretchen No. 4 are relatively high. But we cannot conﬁrm that any- one of them is conspirator, because none of their suspiciousness is conspicuously high. As a result, we must further analyze these three people.

<!-- b000264 | prose | pages [11] -->
We analyze the messages talked by the people mentioned above which are conspiratorial. We deﬁne the conspiratorial messages talked with person whose priority is comparatively high as marked messages. We took the highest 20 peo- ple (including known conspirators) as highly suspected people. We count the conspiratorial messages, marked messages and total messages sent or received by the ﬁve people mentioned above. The data is displayed in Table 5.

<!-- b000265 | prose | pages [11] -->
Name & ID Marked Msgs Gretchen No.4 2 Dolores No.10 3 Jerome No.16 1 Gretchen No.32 0 Jerome No.34 0 Conspiratorial Msgs Total Msgs 5 16 6 17 5 10 3 30 4 24

<!-- b000266 | caption | pages [11] -->
Table 5: Messages of Senior Managers

<!-- b000267 | prose | pages [11] -->
When analyzing these data, we ﬁnd out that although Gretchen No.32 and Jerome No.34 are in the upper third in the whole priority list, they never discuss conspiratorial topics with highly suspected conspirators.

<!-- b000268 | prose | pages [11] -->
The reason of the fact that they have relatively high suspiciousness is that even some non-conspiratorial message sent or received by a person will slightly increase the suspiciousness of that person in our model.

<!-- b000269 | prose | pages [11] -->
Furthermore, we can explain the large total number of messages by the fact that they are senior managers. Because they are senior managers, they have to contact with lots of people. So considering that they may need to contact with all kinds of people and the limited number of marked and conspiratorial messages, we opine that their suspiciousness are not very high.

<!-- b000270 | prose | pages [11] -->
On the other hand, we notice that Dolores No.10 has small number of total messages but the largest number of marked and conspiratorial messages among the ﬁve. In other words, the ratio of suspicious messages is very high of Dolores No.10.

<!-- b000271 | furniture | pages [12] -->
Team # 13855

<!-- b000272 | furniture | pages [12] -->
Page 12 of 19

<!-- b000273 | prose | pages [12] -->
Therefore, we can conclude that Dolores No.10 is probably a conspirator.

<!-- b000274 | prose | pages [12] -->
5.1.3 Conspiracy Leaders

<!-- b000275 | prose | pages [12] -->
To determine the leader(s) of the conspiracy, we think that the person who contact with more conspirators using conspiratorial messages is more likely to be the leader.

<!-- b000276 | prose | pages [12] -->
Therefore, we count the number of probable conspirators a person contacts with using conspiratorial messages. The same as above, we consider the people who are top 20 in the priority list as probable conspirators. The statistics of the top 20 people in the priority list is shown in Table 6.

<!-- b000277 | prose | pages [12] -->
ID # ID # 3 3 15 1 4 1 16 1 7 4 17 3 10 2 18 4 13 1 21 6 ID # ID # 22 2 43 7 28 2 49 3 34 0 54 4 37 2 67 6 38 2 81 1

<!-- b000278 | caption | pages [12] -->
Table 6: # of Suspicious contacts of highly suspected conspirators on conspirato-

<!-- b000279 | prose | pages [12] -->
rial topics

<!-- b000280 | prose | pages [12] -->
From the Table 6, we can ﬁnd that p21, p43 and p67 have relatively large num- ber of probable conspirators contacted on conspiratorial topics. So we can draw a conclusion that p21 Alex, p43 Paul and p67 Yao are probably the leaders of con- spirators.

<!-- b000281 | prose | pages [12] -->
Evaluation and Further Discussions 6

<!-- b000282 | heading | pages [12] -->
Requirement 3: Impacts of NLP developments on our model

<!-- b000283 | prose | pages [12] -->
6.1

<!-- b000284 | prose | pages [12] -->
The development of Natural Language Processing will not only improve the performance of our current model, but also could help us to build more powerful models which is far beyond our expectation using the information that we are provided now.

<!-- b000285 | prose | pages [12] -->
The precision of topic extraction is a key constraint to the performance of our model. Take the case EZ for example, in which topic 4 is summarized as George’s stress. If we are only given the information that Harry, Dave and George are involved in this topic (which is the case in our current ICM case), we would think of Harry as highly dubious since he shares a topic with and basically only with those known conspirators.

<!-- b000286 | prose | pages [12] -->
However, if we are informed of the content of all the messages, we would discover that we are totally misled. The fact is Harry has no idea where George’s stress comes from and Dave wants George to appease Harry, which may on the quite opposite prove the innocence of Harry.

<!-- b000287 | furniture | pages [13] -->
Team # 13855

<!-- b000288 | furniture | pages [13] -->
Page 13 of 19

<!-- b000289 | prose | pages [13] -->
So some important information are lost during the topic extraction and classi- ﬁcation. As the topic discovery develops by enhancing or replacing the currently used topic models such as Latent Dirichlet Allocation and probabilistic Latent Seman- tic Indexing, our model’s performance would enhance.

<!-- b000290 | prose | pages [13] -->
Our model will also beneﬁt a lot from the development of the textual atti- tude/emotion extraction and analysis. The development in all these techniques will produce ﬁne-grained topics which may be able to identify the nuances be- tween Harry and Dave when they are talking about George’s stress.

<!-- b000291 | prose | pages [13] -->
With these informations, we may add relationships to the topics to make them not isolated but interactive.

<!-- b000292 | prose | pages [13] -->
Regardless of all these impacts based on the evolutionary changes of NLP, which is unlikely to be achieved in the recent future, introducing pragmatic NLP techniques to the data will also ameliorate our current model.

<!-- b000293 | prose | pages [13] -->
A simple example is that we could use text analysis to each topic to assign a suspiciousness value to each topic, rather than simply marking some topics as suspicious. We do this (by human efforts rather than NLP techniques) in our experiments, which is discussed in Section 6.2.2.

<!-- b000294 | prose | pages [13] -->
6.2

<!-- b000295 | heading | pages [13] -->
Model Sensitivity

<!-- b000296 | prose | pages [13] -->
In this section, we discuss our model’s sensitivity to the prior knowledges, the settings of parameters and initial values of S and R functions with a series of experiments.

<!-- b000297 | prose | pages [13] -->
6.2.1 Requirement 2: Changing Prior Knowledge

<!-- b000298 | prose | pages [13] -->
If Chris has gone rogue and t1 is connected to the conspir- Priority list change acy as well, there would be a considerable change of the sequence in the priority list with several major leap on the rank of the most suspected, and a subtle varia- tion of the most dubious topics measured by the R value of each topic. The result is shown in Table 13, which is put into the Appendix for the compactness of the article due to its large volume.

<!-- b000299 | prose | pages [13] -->
Analysis As our assumption indicated, the whole communication network model sees one more afﬁrmative conspirator as one more evil propagation source with the S value of 1, and one more message delivering conspiracy as several more dangerous links initiated by high R value. Reasonably, people who have closer relationship with this new evil via more doubtable links should gain more atten- tion in that chances are gauge on them may change tremendously or even ﬂip over. On the other side, judgment on people who have few immediate contacts with Chris and talk less about topic 1 may remain a lot more similar.

<!-- b000300 | prose | pages [13] -->
Comparing the result, it is rather obvious that some node with a rank of top 20 50 in the previous priority list and an S value between 0.52 0.73 which was hard to discriminate them from conspirators have a much higher S value and move up at least 7 places on the priority list. Among these nodes are p32, p45,

<!-- b000301 | furniture | pages [14] -->
Team # 13855

<!-- b000302 | furniture | pages [14] -->
Page 14 of 19

<!-- b000303 | prose | pages [14] -->
p14, p69, p25, p31 and p20. Basically, these nodes are mostly among top 30 now due to their abnormal message or their intimate connection with Chris, which can be seen in Table 7 and 8. This can also be veriﬁed by the illustration in Figure 1 that nodes mentioned above are either interlocutors of t1 (yellow links) or contacts of Chris (red links).

<!-- b000304 | prose | pages [14] -->
66

<!-- b000305 | prose | pages [14] -->
64

<!-- b000306 | prose | pages [14] -->
51

<!-- b000307 | prose | pages [14] -->
62

<!-- b000308 | prose | pages [14] -->
1

<!-- b000309 | prose | pages [14] -->
17

<!-- b000310 | prose | pages [14] -->
78

<!-- b000311 | prose | pages [14] -->
3

<!-- b000312 | prose | pages [14] -->
13

<!-- b000313 | prose | pages [14] -->
32

<!-- b000314 | prose | pages [14] -->
21

<!-- b000315 | prose | pages [14] -->
34

<!-- b000316 | prose | pages [14] -->
26

<!-- b000317 | prose | pages [14] -->
61

<!-- b000318 | prose | pages [14] -->
9

<!-- b000319 | prose | pages [14] -->
12

<!-- b000320 | prose | pages [14] -->
43

<!-- b000321 | prose | pages [14] -->
5

<!-- b000322 | prose | pages [14] -->
65

<!-- b000323 | prose | pages [14] -->
8

<!-- b000324 | prose | pages [14] -->
59

<!-- b000325 | prose | pages [14] -->
50

<!-- b000326 | prose | pages [14] -->
7

<!-- b000327 | prose | pages [14] -->
39

<!-- b000328 | prose | pages [14] -->
11

<!-- b000329 | prose | pages [14] -->
16

<!-- b000330 | prose | pages [14] -->
45

<!-- b000331 | prose | pages [14] -->
29

<!-- b000332 | prose | pages [14] -->
33

<!-- b000333 | prose | pages [14] -->
19

<!-- b000334 | prose | pages [14] -->
55

<!-- b000335 | prose | pages [14] -->
70

<!-- b000336 | prose | pages [14] -->
23

<!-- b000337 | prose | pages [14] -->
30

<!-- b000338 | prose | pages [14] -->
69

<!-- b000339 | prose | pages [14] -->
42

<!-- b000340 | prose | pages [14] -->
28

<!-- b000341 | prose | pages [14] -->
22

<!-- b000342 | prose | pages [14] -->
72

<!-- b000343 | prose | pages [14] -->
56

<!-- b000344 | prose | pages [14] -->
57

<!-- b000345 | prose | pages [14] -->
53

<!-- b000346 | prose | pages [14] -->
47

<!-- b000347 | prose | pages [14] -->
2

<!-- b000348 | prose | pages [14] -->
0

<!-- b000349 | prose | pages [14] -->
15

<!-- b000350 | prose | pages [14] -->
10

<!-- b000351 | prose | pages [14] -->
81

<!-- b000352 | prose | pages [14] -->
14

<!-- b000353 | prose | pages [14] -->
68

<!-- b000354 | prose | pages [14] -->
41

<!-- b000355 | prose | pages [14] -->
20

<!-- b000356 | prose | pages [14] -->
6

<!-- b000357 | prose | pages [14] -->
63

<!-- b000358 | prose | pages [14] -->
49

<!-- b000359 | prose | pages [14] -->
75

<!-- b000360 | prose | pages [14] -->
77

<!-- b000361 | prose | pages [14] -->
37 38

<!-- b000362 | prose | pages [14] -->
4

<!-- b000363 | prose | pages [14] -->
25

<!-- b000364 | prose | pages [14] -->
18

<!-- b000365 | prose | pages [14] -->
74

<!-- b000366 | prose | pages [14] -->
48

<!-- b000367 | prose | pages [14] -->
58

<!-- b000368 | prose | pages [14] -->
24

<!-- b000369 | prose | pages [14] -->
67

<!-- b000370 | prose | pages [14] -->
44

<!-- b000371 | prose | pages [14] -->
76

<!-- b000372 | prose | pages [14] -->
35

<!-- b000373 | prose | pages [14] -->
60

<!-- b000374 | prose | pages [14] -->
46

<!-- b000375 | prose | pages [14] -->
40

<!-- b000376 | prose | pages [14] -->
27

<!-- b000377 | prose | pages [14] -->
80

<!-- b000378 | prose | pages [14] -->
82

<!-- b000379 | prose | pages [14] -->
73

<!-- b000380 | prose | pages [14] -->
36

<!-- b000381 | prose | pages [14] -->
71

<!-- b000382 | prose | pages [14] -->
54

<!-- b000383 | prose | pages [14] -->
31

<!-- b000384 | prose | pages [14] -->
52

<!-- b000385 | prose | pages [14] -->
79

<!-- b000386 | caption | pages [14] -->
Figure 1: All connections with Chris(Node 0) and topic 1

<!-- b000387 | prose | pages [14] -->
Interlocutor No.

<!-- b000388 | prose | pages [14] -->
Identity 32 Unknown 21 conspirator 2 non-conspirator 68 non-conspirator Number of messages Topics 3 3,6,9 3 1 6 2,9,14,15 1 1

<!-- b000389 | caption | pages [14] -->
Table 7: Chris’s message record

<!-- b000390 | prose | pages [14] -->
To give a speciﬁc illustration, we present Gretchen 2, p32, who grabs our atten- tion because it epitomizes the effect of the new information. p32 has heard from Chris 3 times and each time with a different topic [Table 7], and it has also been involved in up to three messages about t1 [Table 8]. These facts are deﬁnitely the reason that its rank jumps from 17th to 6th and its likelihood of being a conspira- tor soars from 76.66% to 83.46% [Table 13].

<!-- b000391 | prose | pages [14] -->
Accordingly, those nodes which are far from Chris and have less involved in t1, almost remain the same places in the priority list [Table 13]. Among them are

<!-- b000392 | furniture | pages [15] -->
Team # 13855

<!-- b000393 | prose | pages [15] -->
From To From 0 21 17 0 21 21 3 32 21 3 34 21 8 16 24 10 27 25 13 48 26 14 25 31 14 44 32 17 9 32

<!-- b000394 | furniture | pages [15] -->
Page 15 of 19

<!-- b000395 | prose | pages [15] -->
To From To 15 40 31 0 41 22 7 43 45 20 54 69 48 55 11 1 62 63 22 64 66 47 68 0 12 71 56 15 82 50

<!-- b000396 | caption | pages [15] -->
Table 8: All messages about topic 1

<!-- b000397 | prose | pages [15] -->
extremely-suspected conspirators like p3, p16 and p34 and unsuspected employees like p53, p58 and p59. There are also another explanation counts for this result which is that new information changes are extremely outnumbered when judging these people considering their abundant message records.

<!-- b000398 | prose | pages [15] -->
Initial Value for R function 6.2.2

<!-- b000399 | prose | pages [15] -->
We try to set different initial values of R function for different topics, based on their textual characteristics.

<!-- b000400 | prose | pages [15] -->
R value Topic No.

<!-- b000401 | prose | pages [15] -->
Topic No. 1 0.6 6 2 0.4 7 3 0.1 8 4 0.2 9 5 0.5 10 R value R value Topic No. 0.2 11 1 1 12 0.4 0.3 13 1 0.2 14 0 0.3 15 0

<!-- b000402 | caption | pages [15] -->
Table 9: R value initiation after topic analysis

<!-- b000403 | prose | pages [15] -->
These R values in Table 9 is given based on a somehow casual deduction. For instance, a Spanish atmosphere in this company is observed due to its frequent usage in communication like massages about t2, t7, t10, t12, in which t7 is afﬁr- matively connected to the conspiracy. Nevertheless, the contents of these topics are also dubious. Such as choosing a best restaurant for lunch, inviting a cer- tain group of people for ski trip, these topics are all about an isolated activity with restricted participants, which might be a conspiracy meeting. Those close relationships between topics and their suspicious details might increase their R value.

<!-- b000404 | prose | pages [15] -->
As shown in Table 10, an initiation of R value can cause considerable effect on the priority list, which could reﬂect our model’s sensitivity to the settings of initial values of R function. Also, we may expect that a better Semantic and Text Analyses can bring about more precise and discreet result by an accurate initiation of R as we mentioned in Section 6.1.

<!-- b000405 | furniture | pages [16] -->
Team # 13855

<!-- b000406 | furniture | pages [16] -->
ID

<!-- b000407 | prose | pages [16] -->
S Rank Change

<!-- b000408 | furniture | pages [16] -->
ID

<!-- b000409 | prose | pages [16] -->
S 7 1.0000 0 20 0.8459 18 1.0000 0 41 0.8440 21 1.0000 0 44 0.8426 37 1.0000 0 14 0.8422 43 1.0000 0 6 0.8420 49 1.0000 0 11 0.8402 54 1.0000 0 33 0.8386 67 1.0000 0 8 0.8373 10 0.8556 9 9 0.8349 17 0.8556 6 27 0.8326 81 0.8555 3 19 0.8315 3 0.8551 1 5 0.8283 13 0.8551 4 29 0.8272 15 0.8545 -3 45 0.8257 34 0.8543 -3 1 0.8251 28 0.8543 -7 46 0.8203 50 0.8541 -7 42 0.8103 38 0.8527 1 25 0.8070 36 0.8525 -4 35 0.8068 22 0.8525 1 12 0.8000 30 0.8523 -1 26 0.7946 32 0.8519 3 60 0.7923 47 0.8516 1 69 0.7827 4 0.8512 -1 39 0.7228 40 0.8500 2 82 0.6642 16 0.8494 6 72 0.6196 24 0.8490 -1 80 0.6123 31 0.8480 -6 62 0.5934

<!-- b000410 | furniture | pages [16] -->
Page 16 of 19

<!-- b000411 | prose | pages [16] -->
Rank Change

<!-- b000412 | furniture | pages [16] -->
ID

<!-- b000413 | prose | pages [16] -->
S Rank Change -1 56 0.5691 -7 1 51 0.5585 9 -1 79 0.5518 -4 4 71 0.5351 10 2 23 0.5123 2 6 57 0.4927 -3 -2 70 0.4357 -3 5 66 0.4313 0 2 55 0.4193 0 -9 77 0.3808 -4 5 63 0.3443 -6 5 61 0.2836 1 -7 58 0.2772 -3 -4 59 0.2754 -2 3 76 0.2716 1 -2 52 0.2237 -1 4 75 0.1948 2 1 53 0.1921 -1 -4 73 0.1836 -1 5 0 0.0000 0 3 2 0.0000 0 -2 48 0.0000 0 7 64 0.0000 0 -15 65 0.0000 0 3 68 0.0000 0 3 74 0.0000 0 -1 78 0.0000 0 -5

<!-- b000414 | caption | pages [16] -->
Table 10: Priority list after topic analysis

<!-- b000415 | prose | pages [16] -->
6.2.3 Decay rate

<!-- b000416 | prose | pages [16] -->
As we said in Section 4.3.4, we use the decay rate (represented by DRS and DRR) to control the degree of propagation. In speciﬁc, DRS controls the propaga- tion of people’s suspiciousness S while DRR controls the propagation of topics’ suspiciousness R.

<!-- b000417 | prose | pages [16] -->
So we could achieve a variety of different goals by use ﬂexible settings. Since displaying the priority list is too space consuming, we just do two experiments as illustration.

<!-- b000418 | prose | pages [16] -->
First we set them both to be 1 (i.e. diable the exponential decay) to test the effect of introducing such decay. The resulting priority list is shown in Table 11.

<!-- b000419 | prose | pages [16] -->
The results turn out to be coordinate with our postulation in Section 4.3.4. A majority of nodes have a tendency to have a S function converged to 1.

<!-- b000420 | prose | pages [16] -->
Then we set DRR to be 0, which means the suspiciousness of topics will never change during the iterations. This shows the results under the condition that we only take those topics believed suspicious in the problem statement as dubious. The results are shown in Table 12.

<!-- b000421 | furniture | pages [17] -->
Team # 13855

<!-- b000422 | furniture | pages [17] -->
Page 17 of 19

<!-- b000423 | furniture | pages [17] -->
S value

<!-- b000424 | furniture | pages [17] -->
S value

<!-- b000425 | furniture | pages [17] -->
S value

<!-- b000426 | furniture | pages [17] -->
ID

<!-- b000427 | furniture | pages [17] -->
ID

<!-- b000428 | furniture | pages [17] -->
ID

<!-- b000429 | prose | pages [17] -->
40 1 49 1 13 26 1 54 1 14 27 1 67 1 15 28 1 69 1 17 30 1 77 1 22 31 1 80 1 18 32 1 82 1 19 34 1 24 1 20 35 1 1 1 21 37 1 3 1 29 38 1 4 1 5 39 1 6 1 50 41 1 7 1 36 43 1 8 1 16 44 1 10 1 42 45 1 11 1 46 47 1 12 1 9

<!-- b000430 | furniture | pages [17] -->
S value

<!-- b000431 | furniture | pages [17] -->
S value

<!-- b000432 | furniture | pages [17] -->
ID

<!-- b000433 | furniture | pages [17] -->
ID

<!-- b000434 | prose | pages [17] -->
1 25 1 57 0.976686 1 81 1 51 0.974359 1 23 1 73 0.958333 1 71 0.999999 61 0.931401 1 33 0.999998 58 0.907174 1 72 0.999965 59 0.906998 1 62 0.999909 63 0.872648 1 76 0.999849 74 0 1 70 0.999839 0 0 1 60 0.999805 68 0 1 53 0.999273 78 0 1 52 0.998788 48 0 1 75 0.998326 2 0 1 66 0.997768 65 0 1 79 0.997184 64 0 1 55 0.996628 1 56 0.994773

<!-- b000435 | caption | pages [17] -->
Table 11: Priority list when setting DRS = DRR = 1

<!-- b000436 | prose | pages [17] -->
S value S value ID ID ID 67 1 15 0.803964 19 43 1 38 0.801247 46 21 1 50 0.801028 29 54 1 22 0.798566 27 37 1 47 0.797955 42 7 1 34 0.79138 9 18 1 30 0.772823 60 49 1 6 0.763542 5 81 0.853917 41 0.754253 24 10 0.84965 32 0.74663 12 17 0.839955 33 0.736335 14 13 0.834948 44 0.713927 35 4 0.819865 40 0.709913 45 28 0.819123 8 0.708059 39 3 0.817 20 0.702925 69 16 0.811792 31 0.688978 51 36 0.803966 11 0.68853 72 S value S value S value ID ID 0.682531 1 0.422953 53 0.176714 0.680683 80 0.399671 75 0.168908 0.673473 79 0.381148 52 0.168527 0.667362 26 0.377577 58 0.165943 0.664048 56 0.373485 59 0.164828 0.663387 57 0.366902 63 0.157118 0.652621 25 0.325067 61 0.157118 0.652462 82 0.308527 68 0 0.64319 23 0.240106 74 0 0.587289 71 0.218424 65 0 0.574714 62 0.204772 64 0 0.569191 77 0.196454 78 0 0.561554 70 0.192799 48 0 0.534129 66 0.19245 2 0 0.526705 76 0.180432 0 0 0.478053 73 0.179955 0.445297 55 0.176714

<!-- b000437 | caption | pages [17] -->
Table 12: Priority list when setting DRR = 0

<!-- b000438 | heading | pages [17] -->
Requirement 4: Model Scalability and Other Applications

<!-- b000439 | prose | pages [17] -->
6.3

<!-- b000440 | prose | pages [17] -->
Our model is based on the property that some particular feature possessed by some nodes may propagate through some edges. In our case, for instance, suspiciousness can propagate through communications. As a result, our model accords with the kind of networks in which features may transmit through edges and edges’ probability to transmit is also taken into account. Furthermore, we ﬁnd that many pragmatic problems accord with this kind of network.

<!-- b000441 | prose | pages [17] -->
We illustrate the scalability of our model by applying our model to the prob- lem of the spread of viral disease within human or other population.

<!-- b000442 | furniture | pages [18] -->
Team # 13855

<!-- b000443 | furniture | pages [18] -->
Page 18 of 19

<!-- b000444 | prose | pages [18] -->
In this virus instance, we ignored the dynamics of viral growth within individ- uals. In other words, we assume that the ability of a individual to transmit virus is constant. For each member pi of the population of n individuals, we could use Si in our model to represent his virion level. And Rij ∗Si is the expected rate of transmission infectious particles from individual pi to individual pj. In this instance, the transmission rate will also declines exponentially with distance be- tween individuals, which is fairly reasonable. As a result, the distribution of the ﬁnal size of this epidemic can be estimated by our model, for the various initial patterns of infection.

<!-- b000445 | prose | pages [18] -->
To sum up, our model can solve the problem of prioritizing and categorizing the infected nodes in this network as well as other problems having the same property we presented at the beginning of this section.

<!-- b000446 | prose | pages [18] -->
6.4

<!-- b000447 | heading | pages [18] -->
Model Drawbacks

<!-- b000448 | prose | pages [18] -->
One drawback for our model is that the presence of a neighbour can never reduce one’s suspiciousness.

<!-- b000449 | prose | pages [18] -->
A communication with a person with a quite low suspiciousness will also increase one’s suspiciousness, although very slightly.

<!-- b000450 | prose | pages [18] -->
Talking with a person with low S value on a topic with a low R value may induce an increase in suspiciousness of at most S ∗R, which is typically compara- ble to 10−2, but having many communications still may result in a relatively high suspiciousness.

<!-- b000451 | furniture | pages [19] -->
Team # 13855

<!-- b000452 | heading | pages [19] -->
Appendices

<!-- b000453 | heading | pages [19] -->
Appendix A

<!-- b000454 | prose | pages [19] -->
Tables

<!-- b000455 | prose | pages [19] -->
S(Old) S(New) Node Rank(Old) 0 0 - 1 45 0.608586 38 0.76127 14 0.607512 39 0.745367 55 0.197634 61 0.414291 69 0.528206 41 0.721606 63 0.163895 66 0.345939 32 0.766605 17 0.834614 25 0.39586 47 0.637846 31 0.711505 25 0.795509 20 0.720356 22 0.803063 71 0.27554 53 0.439828 56 0.364273 50 0.49602 9 0.667589 33 0.735734 22 0.796896 12 0.829145 62 0.255381 54 0.409737 12 0.640781 35 0.717535 27 0.686166 29 0.755073 15 0.806096 8 0.835188 82 0.409267 46 0.562015 1 0.519437 42 0.619194 8 0.718942 23 0.767619 47 0.793939 13 0.815351 3 0.819499 5 0.840111 34 0.802074 10 0.822496 50 0.790764 15 0.808414 26 0.475945 43 0.605413 40 0.724757 21 0.774412 11 0.694822 28 0.738048 41 0.754968 19 0.792661 44 0.746949 20 0.783491 17 0.838916 3 0.848474 52 0.183797 63 0.189941 10 0.847161 2 0.850208 61 0.16224 67 0.16395 81 0.850742 1 0.850546 16 0.804627 9 0.822188 53 0.203252 60 0.203409 58 0.179185 64 0.177722 59 0.176167 65 0.172444 57 0.352322 51 0.382491 70 0.224238 56 0.225577 75 0.18895 62 0.187607 66 0.239405 55 0.235887 73 0.215225 58 0.211614 77 0.217232 57 0.212775 13 0.829731 4 0.831232 51 0.444996 44 0.444483 76 0.204149 59 0.202278 38 0.793437 14 0.79481 72 0.430927 45 0.429841 5 0.664651 34 0.663021 23 0.287067 52 0.284276 80 0.388173 48 0.384105 39 0.551087 40 0.553689 79 0.366544 49 0.369136 4 0.816793 6 0.818802 46 0.679116 31 0.680476 29 0.685091 30 0.686281 42 0.668063 32 0.669088 36 0.798483 11 0.799232 35 0.611702 37 0.611383 60 0.61854 36 0.61792 28 0.809526 7 0.811838 33 0.714468 24 0.717777 24 0.701129 26 0.703047 19 0.695165 27 0.69616 6 0.760001 18 0.760596 30 0.76857 16 0.766879 α Variation = New value - Old value

<!-- b000456 | furniture | pages [19] -->
Page 19 of 19

<!-- b000457 | prose | pages [19] -->
S Variation Rank(New) Rank Variation 0 - 1 24 -14 0.152684 27 -12 0.137855 50 -11 0.216657 30 -11 0.1934 55 -11 0.182044 6 -11 0.068009 39 -8 0.241986 17 -8 0.084004 15 -7 0.082707 48 -5 0.164288 46 -4 0.131747 29 -4 0.068145 8 -4 0.032249 51 -3 0.154356 32 -3 0.076754 26 -3 0.068907 5 -3 0.029092 44 -2 0.152748 40 -2 0.099757 22 -1 0.048677 12 -1 0.021412 4 -1 0.020612 9 -1 0.020422 14 -1 0.01765 43 0 0.129468 21 0 0.049655 28 0 0.043226 19 0 0.037693 20 0 0.036542 3 0 0.009558 63 0 0.006144 2 0 0.003047 67 0 0.00171 1 0 -0.000196 10 1 0.017561 61 1 0.000157 65 1 -0.001463 66 1 -0.003723 53 2 0.030169 58 2 0.001339 64 2 -0.001343 57 2 -0.003518 60 2 -0.003611 59 2 -0.004457 7 3 0.001501 47 3 -0.000513 62 3 -0.001871 18 4 0.001373 49 4 -0.001086 38 4 -0.00163 56 4 -0.002791 52 4 -0.004068 45 5 0.002602 54 5 0.002592 11 5 0.002009 36 5 0.00136 35 5 0.00119 37 5 0.001025 16 5 0.000749 42 5 -0.000319 41 5 -0.00062 13 6 0.002312 31 7 0.003309 33 7 0.001918 34 7 0.000995 25 7 0.000595 23 7 -0.001691 β The priority list ranks all nodes with unknown identity. Nodes with an S

<!-- b000458 | prose | pages [19] -->
value of 0 or 1 are not included.

<!-- b000459 | caption | pages [19] -->
Table 13: Priority list Comparison
