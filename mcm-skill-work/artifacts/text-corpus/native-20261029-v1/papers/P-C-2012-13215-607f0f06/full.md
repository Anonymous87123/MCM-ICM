# P-C-2012-13215-607f0f06

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
13215

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


<!-- b000019 | heading | pages [1] -->
2012 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000020 | prose | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000021 | prose | pages [1] -->
Type a summary of your results on this page. Do not include the name of your school, advisor, or team members on this page.

<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | prose | pages [1] -->
Message Network Modeling for Crime Busting

<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | heading | pages [1] -->
Abstract

<!-- b000028 | prose | pages [1] -->
A particularly popular and challenging problem in crime analysis is to identify the conspirators through analysis of message networks. In this paper, using the data of message traffic, we model to prioritize the likelihood of one’s being conspirator, and nominate the probable conspiracy leaders.

<!-- b000029 | prose | pages [1] -->
We note a fact that any conspirator has at least one message communication with other conspirators, and assume that sending or receiving a message has the same effect, and then develop Model 1, 2 and 3 to make a priority list respectively and Model 4 to nominate the conspiracy leader.

<!-- b000030 | prose | pages [1] -->
In Model 1, we take the amount of one’s suspicious messages and one’s all messages with known conspirators into account, and define a simple composite index to measure the likelihood of one’s being conspirator.

<!-- b000031 | prose | pages [1] -->
Then, considering probability relevance of all nodes, we develop Model 2 based on Law of Total Probability. In this model, probability of one’s being conspirator is the weight sum of probabilities of others directly linking to it. And we develop Algorithm 1 to calculate probabilities of all the network nodes as direct calculation is infeasible.

<!-- b000032 | prose | pages [1] -->
Besides, in order to better quantify one’s relationship to the known conspirators, we develop Model 3, which brings in the concept “shortest path” of graph theory to create an indicator evaluating the likelihood of one’s being conspirator which can be calculated through Algorithm 2.

<!-- b000033 | prose | pages [1] -->
As a result, we compare three priority lists and conclude that the overall rankings are similar but quite changes appear in some nodes. Additionally, when altering the given information, we find that the priority list just changes slightly except for a few nodes, so that we validate the models’ stability.

<!-- b000034 | prose | pages [1] -->
Afterwards, by using Freeman’s centrality method, we develop Model 4 to nominate three most probable leaders: Paul, Elsie, Dolores (senior manager).

<!-- b000035 | prose | pages [1] -->
What’s more, we make some remarks about the models and discuss what could be done to enhance them in the future work. In addition, we further explain Investigation EZ through text and semantic network analysis, so to illustrate the models’ capacity of applying to more complicated cases. Finally, we briefly state the application of our models in other disciplines.

<!-- b000036 | furniture | pages [2] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000037 | furniture | pages [2] -->
1

<!-- b000038 | heading | pages [2] -->
Introduction

<!-- b000039 | prose | pages [2] -->
ICM is investigating a conspiracy whose members all work for the same noted company which majors in developing and marketing computer software for banks and credit card companies. Conspirators commit crimes by embezzling funds from the company and using internet fraud to steal funds from credit cards. It is a kind of commercial fraud. Fraud is a human endeavor, involving deception, purposeful intent, intensity of desire, risk of apprehension, violation of trust, rationalization, etc. Psychological factors influence the behaviors of fraud perpetrators (Sridhar Ramamoorti, 2008).

<!-- b000040 | prose | pages [2] -->
ICM provides us the following information that they have mastered ●All 83 office workers’ names; ●15 short descriptions of the topics ( Topic 7, 11, and 13 have been deemed to be suspicious);

<!-- b000041 | prose | pages [2] -->
●400 links of the nodes that transmit messages and the topic code numbers; ●7 known conspirators: Jean, Alex, Elsie, Paul, Ulf, Yao, and Harvey; ●8 known non-conspirators: Darlene, Tran, Jia, Ellin, Gard, Chris, Paige and Este;

<!-- b000042 | prose | pages [2] -->
●Jerome, Delores, and Gretchen are the senior managers of the company.

<!-- b000043 | furniture | pages [2] -->


<!-- b000044 | prose | pages [2] -->
For crime busting, we develop models to ●Identify all conspirators as accurately as possible, make a priority list that shows the likelihood of one’s being conspirator, so that erroneous judgments or miss-judgments won’t happen easily;

<!-- b000045 | prose | pages [2] -->
● Nominate the conspiracy leader.

<!-- b000046 | furniture | pages [2] -->


<!-- b000047 | prose | pages [2] -->
Declaration of the given data

<!-- b000048 | prose | pages [2] -->
●“Topics.xls” contains only 15 topics, but “topic 18” appears in line 215 of “Messages.xls”. To fix this error, we decide to neglect this invalid data and delete it.

<!-- b000049 | prose | pages [2] -->
●In page 5, line 2 of “2012_ICM_Problem.pdf”, it says that “Elsie” is one of the known conspirators. However we find two “Elsie” with node number “7” and “37”. Throughout some basic statistics about the message traffic containing suspicious topics, it appears that “7 Elsie” is more likely to be a known conspirator rather than “37 Elsie”. Therefore, we assume that “Elsie” in “2012_ICM_Problem.pdf” indicates “Elsie” with node number 7 in “names.xls”.

<!-- b000050 | prose | pages [2] -->
●As the problem paper point out, “Delores” is a senior manager. But “Delores” can’t be found in “names.xls” while “Dolores” is found. So we consider it as misspelling and replace “Delores” with “Dolores”.

<!-- b000051 | prose | pages [2] -->
●“Gretchen” is also one of the senior managers. But two “Gretchen” are found in “names.xls” with different node number “4” and “32”. In consideration of this redundancy, we determine to pick out node 32 for “Gretchen” indicated in the problem paper artificially. In addition, our basic statistics also shows that “32 Gretchen” has more message exchanges than “4 Gretchen”, which may imply that “32 Gretchen” is more probably the senior manager than “4 Gretchen” due to managers often contact others more than ordinary office workers.

<!-- b000052 | furniture | pages [3] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000053 | furniture | pages [3] -->
2

<!-- b000054 | heading | pages [3] -->
Problem analysis and assumption

<!-- b000055 | prose | pages [3] -->
Commercial fraud is committed by those intelligent people who are confident with their professional skills. Meanwhile, this kind of crime couldn’t involve only one person, but always need cooperation of a whole group. Thus, communication with other conspirators would be inevitable. However, they obviously know that they are linked together and if one person discloses their secrets, none of them can get off. So they are conscious when they communicate with their colleagues who aren’t their companions, especially when they talk about sensitive issues. And the higher intellectual level of perpetrators with rich society experience, the more conscious they are (Zhigang Lin,2010). And ICM can figure out suspicious topic which stands a good chance of being related to the conspiracy by some content analysis method. On the one hand, although Conspirators would try to avoid involving suspicious topics in their messages, they have to convey this kind of information sometimes due to the business or other reason. On the other hand, trust and close relationship play an important role in a conspiracy group, so normal messages exchanges can also reflect the conspiracy relationship.

<!-- b000056 | prose | pages [3] -->
Based on psychology analysis above, we can state that all conspirators have at least one message communication with other conspirators, whether suspicious or unsuspicious message.

<!-- b000057 | prose | pages [3] -->
In addition, we make the assumption that sending and receiving messages have same effect when we evaluate the likelihood of one’s being conspirator;

<!-- b000058 | furniture | pages [3] -->


<!-- b000059 | heading | pages [3] -->
Models

<!-- b000060 | heading | pages [3] -->
Model 1

<!-- b000061 | prose | pages [3] -->
Establishment of model

<!-- b000062 | prose | pages [3] -->
According to the analysis of the problem, the likelihood of one’s being conspirator is related to various factors, such as what topics are contained in the worker messages, how many messages and suspicious messages are the worker related with, who did the worker contact with, etc. To evaluate the likelihood of one’s being conspirators, we use the following equation which combines two quantity indexes:

<!-- b000063 | prose | pages [3] -->
⎛

<!-- b000064 | prose | pages [3] -->
n

<!-- b000065 | prose | pages [3] -->
1

<!-- b000066 | prose | pages [3] -->
⎜ =

<!-- b000067 | prose | pages [3] -->
1

<!-- b000068 | prose | pages [3] -->
i

<!-- b000069 | prose | pages [3] -->
p

<!-- b000070 | furniture | pages [3] -->


<!-- b000071 | prose | pages [3] -->
i

<!-- b000072 | prose | pages [3] -->
⎜

<!-- b000073 | prose | pages [3] -->
2 max{ }

<!-- b000074 | prose | pages [3] -->
n

<!-- b000075 | prose | pages [3] -->
⎝

<!-- b000076 | prose | pages [3] -->
1

<!-- b000077 | prose | pages [3] -->
i i

<!-- b000078 | prose | pages [3] -->
⎞

<!-- b000079 | prose | pages [3] -->
n

<!-- b000080 | prose | pages [3] -->
⎟ + + =

<!-- b000081 | prose | pages [3] -->
2

<!-- b000082 | prose | pages [3] -->
i

<!-- b000083 | prose | pages [3] -->
, 0,1,2,...,82

<!-- b000084 | prose | pages [3] -->
i

<!-- b000085 | prose | pages [3] -->
(1)

<!-- b000086 | prose | pages [3] -->
⎟

<!-- b000087 | prose | pages [3] -->
max{ }

<!-- b000088 | prose | pages [3] -->
n

<!-- b000089 | prose | pages [3] -->
⎠

<!-- b000090 | prose | pages [3] -->
2

<!-- b000091 | prose | pages [3] -->
i i

<!-- b000092 | prose | pages [3] -->
is the suspicious message number that office worker Where

<!-- b000093 | prose | pages [3] -->
n 1i

<!-- b000094 | prose | pages [3] -->
sent or received

<!-- b000095 | prose | pages [3] -->
i

<!-- b000096 | prose | pages [3] -->
is message number that office worker i sent to or received by known and

<!-- b000097 | prose | pages [3] -->
2n

<!-- b000098 | prose | pages [3] -->
i

<!-- b000099 | prose | pages [3] -->
conspirators.

<!-- b000100 | prose | pages [3] -->
and In order to get each value of

<!-- b000101 | prose | pages [3] -->
n 1i

<!-- b000102 | caption | pages [3] -->
Figure 1:

<!-- b000103 | prose | pages [3] -->
, we make data statistics and draw

<!-- b000104 | prose | pages [3] -->
n 2i

<!-- b000105 | furniture | pages [4] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000106 | furniture | pages [4] -->
3

<!-- b000107 | furniture | pages [4] -->


<!-- b000108 | prose | pages [4] -->
Figure. 1

<!-- b000109 | furniture | pages [4] -->


<!-- b000110 | prose | pages [4] -->
Result and analysis

<!-- b000111 | caption | pages [4] -->
Figure 1 shows all the values of

<!-- b000112 | prose | pages [4] -->
n 1i

<!-- b000113 | prose | pages [4] -->
and

<!-- b000114 | prose | pages [4] -->
n

<!-- b000115 | prose | pages [4] -->
. Using equation (1) we have put

<!-- b000116 | prose | pages [4] -->
2i

<!-- b000117 | prose | pages [4] -->
forward, we can easily calculate all the values of

<!-- b000118 | prose | pages [4] -->
1 (note that ip and make a priority list as Table ip is not a probability but a metric to evaluate the likelihood, though it value is between 0 and 1)

<!-- b000119 | prose | pages [4] -->
Table 1

<!-- b000120 | prose | pages [4] -->
No node p

<!-- b000121 | furniture | pages [4] -->


<!-- b000122 | prose | pages [4] -->
No node p

<!-- b000123 | prose | pages [4] -->
1 1

<!-- b000124 | furniture | pages [4] -->


<!-- b000125 | prose | pages [4] -->
21 30 0.1534 21

<!-- b000126 | prose | pages [4] -->
2 0.9091

<!-- b000127 | furniture | pages [4] -->


<!-- b000128 | prose | pages [4] -->
21 33 0.1534 67

<!-- b000129 | prose | pages [4] -->
3 0.6761

<!-- b000130 | furniture | pages [4] -->


<!-- b000131 | prose | pages [4] -->
21 35 0.1534 54

<!-- b000132 | prose | pages [4] -->
4 0.6307

<!-- b000133 | furniture | pages [4] -->


<!-- b000134 | prose | pages [4] -->
21 44 0.1534 7

<!-- b000135 | prose | pages [4] -->
5 0.4915

<!-- b000136 | furniture | pages [4] -->


<!-- b000137 | prose | pages [4] -->
21 46 0.1534 43

<!-- b000138 | prose | pages [4] -->
6 0.429

<!-- b000139 | furniture | pages [4] -->


<!-- b000140 | prose | pages [4] -->
27 6 0.1392 18

<!-- b000141 | prose | pages [4] -->
7 0.3835

<!-- b000142 | furniture | pages [4] -->


<!-- b000143 | prose | pages [4] -->
27 19 0.1392 49

<!-- b000144 | prose | pages [4] -->
8 81 0.3381

<!-- b000145 | furniture | pages [4] -->


<!-- b000146 | prose | pages [4] -->
27 37 0.1392

<!-- b000147 | prose | pages [4] -->
9 48 0.321

<!-- b000148 | furniture | pages [4] -->


<!-- b000149 | prose | pages [4] -->
27 38 0.1392

<!-- b000150 | prose | pages [4] -->
10 3 0.2784

<!-- b000151 | furniture | pages [4] -->


<!-- b000152 | prose | pages [4] -->
27 41 0.1392

<!-- b000153 | prose | pages [4] -->
10 10 0.2784

<!-- b000154 | furniture | pages [4] -->


<!-- b000155 | prose | pages [4] -->
27 50 0.1392

<!-- b000156 | prose | pages [4] -->
33 0 0.1364 12 20 0.2756

<!-- b000157 | furniture | pages [4] -->


<!-- b000158 | prose | pages [4] -->
13 2 0.2159

<!-- b000159 | furniture | pages [4] -->


<!-- b000160 | prose | pages [4] -->
34 15 0.125

<!-- b000161 | prose | pages [4] -->
13 34 0.2159

<!-- b000162 | furniture | pages [4] -->


<!-- b000163 | prose | pages [4] -->
34 22 0.125

<!-- b000164 | prose | pages [4] -->
15 16 0.2017

<!-- b000165 | furniture | pages [4] -->


<!-- b000166 | prose | pages [4] -->
36 14 0.1222

<!-- b000167 | prose | pages [4] -->
15 17 0.2017

<!-- b000168 | furniture | pages [4] -->


<!-- b000169 | prose | pages [4] -->
36 45 0.1222

<!-- b000170 | prose | pages [4] -->
17 28 0.1705

<!-- b000171 | furniture | pages [4] -->


<!-- b000172 | prose | pages [4] -->
38 31 0.108

<!-- b000173 | prose | pages [4] -->
17 47 0.1705

<!-- b000174 | furniture | pages [4] -->


<!-- b000175 | prose | pages [4] -->
38 36 0.108

<!-- b000176 | prose | pages [4] -->
19 4 0.1563

<!-- b000177 | furniture | pages [4] -->


<!-- b000178 | prose | pages [4] -->
38 65 0.108

<!-- b000179 | prose | pages [4] -->
19 13 0.1563

<!-- b000180 | furniture | pages [4] -->


<!-- b000181 | prose | pages [4] -->
41 29 0.0938

<!-- b000182 | prose | pages [4] -->
21 27 0.1534

<!-- b000183 | furniture | pages [4] -->


<!-- b000184 | prose | pages [4] -->
41 32 0.0938

<!-- b000185 | furniture | pages [4] -->


<!-- b000186 | prose | pages [4] -->
No node p No node p

<!-- b000187 | prose | pages [4] -->
43 1 0.0909 57 72 0.0313

<!-- b000188 | prose | pages [4] -->
44 60 0.0767 57 75 0.0313

<!-- b000189 | prose | pages [4] -->
44 69 0.0767 57 78 0.0313

<!-- b000190 | prose | pages [4] -->
44 82 0.0767 57 79 0.0313

<!-- b000191 | prose | pages [4] -->
47 5 0.0625 68 26 0

<!-- b000192 | prose | pages [4] -->
47 8 0.0625 68 52 0

<!-- b000193 | prose | pages [4] -->
47 9 0.0625 68 53 0

<!-- b000194 | prose | pages [4] -->
47 11 0.0625 68 55 0

<!-- b000195 | prose | pages [4] -->
47 40 0.0625 68 58 0

<!-- b000196 | prose | pages [4] -->
47 42 0.0625 68 59 0

<!-- b000197 | prose | pages [4] -->
47 80 0.0625 68 61 0

<!-- b000198 | prose | pages [4] -->
54 25 0.0455 68 62 0

<!-- b000199 | prose | pages [4] -->
54 66 0.0455 68 63 0

<!-- b000200 | prose | pages [4] -->
54 73 0.0455 68 64 0

<!-- b000201 | prose | pages [4] -->
57 12 0.0313 68 68 0

<!-- b000202 | prose | pages [4] -->
57 23 0.0313 68 70 0

<!-- b000203 | prose | pages [4] -->
57 24 0.0313 68 71 0

<!-- b000204 | prose | pages [4] -->
57 39 0.0313 68 74 0

<!-- b000205 | prose | pages [4] -->
57 51 0.0313 68 76 0

<!-- b000206 | prose | pages [4] -->
57 56 0.0313 68 77 0

<!-- b000207 | prose | pages [4] -->
57 57 0.0313

<!-- b000208 | furniture | pages [4] -->


<!-- b000209 | furniture | pages [4] -->


<!-- b000210 | furniture | pages [4] -->


<!-- b000211 | prose | pages [4] -->
As shown in Table 1, all the known conspirators (heavy tape and red mark) are ranked in the very front of the list, which indicates the model is effective to some extent that it can recognize some workers who is most likely to be conspirators. However, some non-conspirators (green mark and Italic type) are also up at the front,

<!-- b000212 | furniture | pages [5] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000213 | furniture | pages [5] -->
4

<!-- b000214 | prose | pages [5] -->
like node 48 and node 2, which shows that the model has a certain limitation and some wrong recognition.

<!-- b000215 | furniture | pages [5] -->


<!-- b000216 | heading | pages [5] -->
Model 2

<!-- b000217 | prose | pages [5] -->
In order to establish an improved model, we make one more assumptions Except for the known conspirators and non-conspirators, one’s probability of being conspirator is relate to those who have direct message contact with him/her. And the probability is both affected by the probability of his/her linking persons and the topic nature of the linking messages.

<!-- b000218 | furniture | pages [5] -->


<!-- b000219 | prose | pages [5] -->
Introduction of Law of Total Probability

<!-- b000220 | prose | pages [5] -->
In probability theory, the law of total probability or the formula of total probability is a fundamental regulation relating marginal probabilities. It can be described as follows:

<!-- b000221 | prose | pages [5] -->
n =

<!-- b000222 | prose | pages [5] -->
countably infinite partition of a sample space

<!-- b000223 | prose | pages [5] -->
B if { :

<!-- b000224 | prose | pages [5] -->
1,2,3,...} is a finite or n

<!-- b000225 | prose | pages [5] -->
and each event B in it is measurable, then for any event

<!-- b000226 | prose | pages [5] -->
n

<!-- b000227 | prose | pages [5] -->
space:

<!-- b000228 | prose | pages [5] -->
= ∑

<!-- b000229 | prose | pages [5] -->
of the same probability A

<!-- b000230 | prose | pages [5] -->
(2)

<!-- b000231 | prose | pages [5] -->
A B P( ) A P( n

<!-- b000232 | prose | pages [5] -->
Establishment of model

<!-- b000233 | prose | pages [5] -->
| | )P(

<!-- b000234 | prose | pages [5] -->
B

<!-- b000235 | prose | pages [5] -->
) n n

<!-- b000236 | furniture | pages [5] -->


<!-- b000237 | prose | pages [5] -->
According to the material we get hold of , since Topic 7, 11, and 13 have been deemed to be suspicious ,we name S={7,11,13} the suspicious topic set and U={1,2,3,4,5,6,8,9,10,12,14,15} the unsuspicious topic set. In addition, we categorize all 83 office workers into three groups: conspirators, non-conspirators and unknown

<!-- b000238 | prose | pages [5] -->
= jP j ( 0,1,...,83, except

<!-- b000239 | prose | pages [5] -->
ap , bp and ones.

<!-- b000240 | prose | pages [5] -->
15 15 known persons )

<!-- b000241 | prose | pages [5] -->
indicate the probability

<!-- b000242 | prose | pages [5] -->
of three kind of office workers commit crime. We have

<!-- b000243 | prose | pages [5] -->
ap =1, bp =0 and equaled

<!-- b000244 | prose | pages [5] -->
jP

<!-- b000245 | prose | pages [5] -->
different unknown numbers which between 0 and 1. The greater probability the unknown one is conspirator, the greater is. A person is much more suspicious if

<!-- b000246 | prose | pages [5] -->
jP jP

<!-- b000247 | prose | pages [5] -->
he/she sends or receives suspicious messages more frequently. We can use to

<!-- b000248 | prose | pages [5] -->
w

<!-- b000249 | prose | pages [5] -->
ji

<!-- b000250 | prose | pages [5] -->
represent the suspicious extent and it can be calculated by the following equations:

<!-- b000251 | prose | pages [5] -->
= × + × = w n a n b i ,

<!-- b000252 | prose | pages [5] -->
ji a b "

<!-- b000253 | prose | pages [5] -->
1,2, (3)

<!-- b000254 | prose | pages [5] -->
(n )is the number of suspicious(unsuspicious) messages a unknown one Where

<!-- b000255 | prose | pages [5] -->
an b

<!-- b000256 | prose | pages [5] -->
is the weight of elements in the set of S, and sends or receives,

<!-- b000257 | prose | pages [5] -->
a

<!-- b000258 | prose | pages [5] -->
elements in the set of U.

<!-- b000259 | furniture | pages [5] -->


<!-- b000260 | prose | pages [5] -->
is the weight of

<!-- b000261 | prose | pages [5] -->
b

<!-- b000262 | prose | pages [5] -->
Next, we will explain how “probability” works out in the messages network with

<!-- b000263 | caption | pages [5] -->
Figure 2.

<!-- b000264 | furniture | pages [6] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000265 | furniture | pages [6] -->
5

<!-- b000266 | furniture | pages [6] -->


<!-- b000267 | prose | pages [6] -->
Figure. 2 We consider that the whole network can be separating into a lot of small network like above. Bringing Law of Total Probability in our model, we treat the center node (not including nodes in known conspirators or non-conspirators group) as

<!-- b000268 | prose | pages [6] -->
A

<!-- b000269 | prose | pages [6] -->
in description of Law of Total Probability, and other nodes directly connected to it as

<!-- b000270 | prose | pages [6] -->
B n = ( 1,2,3,...) = jP P( ) A , probabilities of other

<!-- b000271 | prose | pages [6] -->
. So probability of center node is

<!-- b000272 | prose | pages [6] -->
n

<!-- b000273 | prose | pages [6] -->
= , and P( connecting nodes are p B P( ) ji i

<!-- b000274 | prose | pages [6] -->
w

<!-- b000275 | prose | pages [6] -->
ji

<!-- b000276 | prose | pages [6] -->
| ) = A B

<!-- b000277 | prose | pages [6] -->
.

<!-- b000278 | prose | pages [6] -->
∑

<!-- b000279 | prose | pages [6] -->
n

<!-- b000280 | prose | pages [6] -->
w

<!-- b000281 | prose | pages [6] -->
ji i

<!-- b000282 | prose | pages [6] -->
Based on illustrations we present, we calculate

<!-- b000283 | prose | pages [6] -->
⎛

<!-- b000284 | prose | pages [6] -->
w

<!-- b000285 | prose | pages [6] -->
⎜

<!-- b000286 | prose | pages [6] -->
∑

<!-- b000287 | prose | pages [6] -->
ji

<!-- b000288 | prose | pages [6] -->
= ×

<!-- b000289 | prose | pages [6] -->
P p

<!-- b000290 | prose | pages [6] -->
⎜

<!-- b000291 | prose | pages [6] -->
∑

<!-- b000292 | prose | pages [6] -->
j ji

<!-- b000293 | prose | pages [6] -->
w

<!-- b000294 | prose | pages [6] -->
⎜

<!-- b000295 | prose | pages [6] -->
i

<!-- b000296 | prose | pages [6] -->
⎝

<!-- b000297 | prose | pages [6] -->
i

<!-- b000298 | prose | pages [6] -->
P in the following way:

<!-- b000299 | prose | pages [6] -->
∑

<!-- b000300 | prose | pages [6] -->
⎞ ×

<!-- b000301 | prose | pages [6] -->
p w

<!-- b000302 | prose | pages [6] -->
ji ji

<!-- b000303 | prose | pages [6] -->
⎟ =

<!-- b000304 | prose | pages [6] -->
i

<!-- b000305 | prose | pages [6] -->
(4)

<!-- b000306 | prose | pages [6] -->
⎟

<!-- b000307 | prose | pages [6] -->
∑

<!-- b000308 | prose | pages [6] -->
w

<!-- b000309 | prose | pages [6] -->
⎟

<!-- b000310 | prose | pages [6] -->
ji ji ji

<!-- b000311 | prose | pages [6] -->
⎠

<!-- b000312 | prose | pages [6] -->
i

<!-- b000313 | prose | pages [6] -->
However, all the probabilities of nodes in the unknown group are uncertain. So it is impossible to use the equation above to calculate all the probabilities directly. As a solution, we develop the following algorithm.

<!-- b000314 | furniture | pages [6] -->


<!-- b000315 | prose | pages [6] -->
Algorithm 1

<!-- b000316 | prose | pages [6] -->
All 400 links can constitute a complex relative network, and each office worker can form a simply network centered on himself/herself. Considering the structure of network, we imitated the neural network algorithm but use iterative method to complete the whole relative network:

<!-- b000317 | prose | pages [6] -->
= = t = (0) , and initialize Step 1: Set iteration times as T

<!-- b000318 | prose | pages [6] -->
jP Step 2: Refreshing the network

<!-- b000319 | furniture | pages [6] -->


<!-- b000320 | prose | pages [6] -->
, ; jP 0( j 1,2,...,68) 1

<!-- b000321 | prose | pages [6] -->
( )t Loop j from 1 to 68 , then utilize equation (4) to calculate each ; jP

<!-- b000322 | prose | pages [6] -->
Step 3: Calculate the quadratic sum of probability errors between last time and present time;

<!-- b000323 | prose | pages [6] -->
68

<!-- b000324 | prose | pages [6] -->
∑ =

<!-- b000325 | prose | pages [6] -->
e t ( )

<!-- b000326 | prose | pages [6] -->
=

<!-- b000327 | prose | pages [6] -->
j

<!-- b000328 | prose | pages [6] -->
= + >

<!-- b000329 | prose | pages [6] -->
( ) ( )

<!-- b000330 | prose | pages [6] -->
−

<!-- b000331 | prose | pages [6] -->
1

<!-- b000332 | prose | pages [6] -->
t t

<!-- b000333 | prose | pages [6] -->
−

<!-- b000334 | prose | pages [6] -->
2

<!-- b000335 | prose | pages [6] -->
(5)

<!-- b000336 | prose | pages [6] -->
[ [ P P ] j j 1 1

<!-- b000337 | prose | pages [6] -->
, program ends up, else returns to Step 2. Step 4: Let , if t t 1 t T

<!-- b000338 | furniture | pages [6] -->


<!-- b000339 | prose | pages [6] -->
e t ( ) e t ( )

<!-- b000340 | prose | pages [6] -->
shows a downward trend. When the value of With

<!-- b000341 | prose | pages [6] -->
t

<!-- b000342 | prose | pages [6] -->
increasing,

<!-- b000343 | furniture | pages [6] -->


<!-- b000344 | prose | pages [6] -->
tends to become stable, or less equals than a small constant, we can consider all the

<!-- b000345 | furniture | pages [7] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000346 | prose | pages [7] -->
( )t

<!-- b000347 | furniture | pages [7] -->
6

<!-- b000348 | prose | pages [7] -->
satisfy equation (4) and be the probabilities of being conspirators. present jP

<!-- b000349 | prose | pages [7] -->
form large to small and make a list that shows the In the end, we can sort

<!-- b000350 | prose | pages [7] -->
jP

<!-- b000351 | prose | pages [7] -->
likelihood of one’s being conspirator, meanwhile, divide the list into two parts based on a critical value

<!-- b000352 | prose | pages [7] -->
dp which set in advance.

<!-- b000353 | furniture | pages [7] -->


<!-- b000354 | prose | pages [7] -->
Computing process can be shown in Figure 3, where every circle represents an office worker and the grey level of the circle stands for his/her probability in every

<!-- b000355 | prose | pages [7] -->
T

<!-- b000356 | prose | pages [7] -->
times iterations, the grey level of every circle basically no iteration. In the end of longer changed.

<!-- b000357 | furniture | pages [7] -->


<!-- b000358 | prose | pages [7] -->
Figure. 3

<!-- b000359 | furniture | pages [7] -->


<!-- b000360 | prose | pages [7] -->
Result and analysis

<!-- b000361 | prose | pages [7] -->
According to the given data in “Messages.xls”, “Names.xls” and Topics.xls, we can make a priority list that shows the likelihood of one’s being conspirator based on Model 2. We set

<!-- b000362 | prose | pages [7] -->
=

<!-- b000363 | prose | pages [7] -->
,which is the weight of elements in the set of a

<!-- b000364 | prose | pages [7] -->
0.9

<!-- b000365 | prose | pages [7] -->
=

<!-- b000366 | prose | pages [7] -->
; S ,which is the weight of elements in the set of b

<!-- b000367 | prose | pages [7] -->
0.1

<!-- b000368 | prose | pages [7] -->
=

<!-- b000369 | prose | pages [7] -->
,which is the iteration times; T

<!-- b000370 | prose | pages [7] -->
20

<!-- b000371 | prose | pages [7] -->
d =

<!-- b000372 | prose | pages [7] -->
; U

<!-- b000373 | prose | pages [7] -->
,which is the critical value separating the conspirator group and p

<!-- b000374 | prose | pages [7] -->
0.5

<!-- b000375 | prose | pages [7] -->
non-conspirator group.

<!-- b000376 | prose | pages [7] -->
After the iterative computation, e t ( )

<!-- b000377 | prose | pages [7] -->
4

<!-- b000378 | prose | pages [7] -->
3

<!-- b000379 | prose | pages [7] -->
e(t)

<!-- b000380 | prose | pages [7] -->
2

<!-- b000381 | prose | pages [7] -->
1

<!-- b000382 | prose | pages [7] -->
0

<!-- b000383 | furniture | pages [7] -->


<!-- b000384 | prose | pages [7] -->
0 2 4 6 8

<!-- b000385 | prose | pages [7] -->
tends to be 0 as Figure 4 shows

<!-- b000386 | furniture | pages [7] -->


<!-- b000387 | prose | pages [7] -->
10 12 14 16 18 20

<!-- b000388 | furniture | pages [7] -->


<!-- b000389 | prose | pages [7] -->
iteration times

<!-- b000390 | furniture | pages [8] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000391 | prose | pages [8] -->
0.015

<!-- b000392 | prose | pages [8] -->
0.01

<!-- b000393 | prose | pages [8] -->
e(t)

<!-- b000394 | prose | pages [8] -->
0.005

<!-- b000395 | prose | pages [8] -->
0 10 11 12 13 14

<!-- b000396 | furniture | pages [8] -->
7

<!-- b000397 | prose | pages [8] -->
15 16 17 18 19 20

<!-- b000398 | prose | pages [8] -->
iteration times

<!-- b000399 | furniture | pages [8] -->


<!-- b000400 | prose | pages [8] -->
Figure. 4

<!-- b000401 | prose | pages [8] -->
e t ( )

<!-- b000402 | prose | pages [8] -->
As shown in Figure 4, after 20 times’ iteration,

<!-- b000403 | prose | pages [8] -->
jP j =

<!-- b000404 | prose | pages [8] -->
is less than 0.001. So we can , which represents probability of being conspirator of consider

<!-- b000405 | prose | pages [8] -->
( 1,2,...,68)

<!-- b000406 | prose | pages [8] -->
person in the unknown group, is so stable that all

<!-- b000407 | prose | pages [8] -->
= ∑ ×

<!-- b000408 | prose | pages [8] -->
p w

<!-- b000409 | prose | pages [8] -->
i i i

<!-- b000410 | prose | pages [8] -->
equation

<!-- b000411 | prose | pages [8] -->
P

<!-- b000412 | prose | pages [8] -->
can perfectly satisfy the

<!-- b000413 | prose | pages [8] -->
P

<!-- b000414 | prose | pages [8] -->
j

<!-- b000415 | prose | pages [8] -->
jP j = which is presented in model 1. Size

<!-- b000416 | prose | pages [8] -->
∑

<!-- b000417 | prose | pages [8] -->
j

<!-- b000418 | prose | pages [8] -->
w

<!-- b000419 | prose | pages [8] -->
i i

<!-- b000420 | prose | pages [8] -->
we get the priority list as Table 2 shows

<!-- b000421 | furniture | pages [8] -->


<!-- b000422 | prose | pages [8] -->
( 1,2,...,68) down,

<!-- b000423 | prose | pages [8] -->
Table 2

<!-- b000424 | prose | pages [8] -->
No Node Pro

<!-- b000425 | furniture | pages [8] -->


<!-- b000426 | prose | pages [8] -->
No Node Pro

<!-- b000427 | prose | pages [8] -->
1 1

<!-- b000428 | furniture | pages [8] -->


<!-- b000429 | prose | pages [8] -->
22 1 0.6248 7

<!-- b000430 | prose | pages [8] -->
1 1

<!-- b000431 | furniture | pages [8] -->


<!-- b000432 | prose | pages [8] -->
23 31 0.6172 18

<!-- b000433 | prose | pages [8] -->
1 1

<!-- b000434 | furniture | pages [8] -->


<!-- b000435 | prose | pages [8] -->
24 14 0.6083 21

<!-- b000436 | prose | pages [8] -->
1 1

<!-- b000437 | furniture | pages [8] -->


<!-- b000438 | prose | pages [8] -->
25 27 0.584 43

<!-- b000439 | prose | pages [8] -->
1 1

<!-- b000440 | furniture | pages [8] -->


<!-- b000441 | prose | pages [8] -->
26 6 0.5809 49

<!-- b000442 | prose | pages [8] -->
1 1

<!-- b000443 | furniture | pages [8] -->


<!-- b000444 | prose | pages [8] -->
27 42 0.5798 54

<!-- b000445 | prose | pages [8] -->
1 1

<!-- b000446 | furniture | pages [8] -->


<!-- b000447 | prose | pages [8] -->
28 11 0.5765 67

<!-- b000448 | prose | pages [8] -->
1 73 1

<!-- b000449 | furniture | pages [8] -->


<!-- b000450 | prose | pages [8] -->
29 46 0.5762

<!-- b000451 | prose | pages [8] -->
9 81 0.9773

<!-- b000452 | furniture | pages [8] -->


<!-- b000453 | prose | pages [8] -->
30 69 0.5736

<!-- b000454 | prose | pages [8] -->
10 60 0.9367

<!-- b000455 | furniture | pages [8] -->


<!-- b000456 | prose | pages [8] -->
31 45 0.5728

<!-- b000457 | prose | pages [8] -->
11 59 0.9366

<!-- b000458 | furniture | pages [8] -->


<!-- b000459 | prose | pages [8] -->
32 16 0.5728

<!-- b000460 | prose | pages [8] -->
12 33 0.8078

<!-- b000461 | furniture | pages [8] -->


<!-- b000462 | prose | pages [8] -->
33 28 0.5632

<!-- b000463 | prose | pages [8] -->
34 41 0.5626 13 30 0.7769

<!-- b000464 | furniture | pages [8] -->


<!-- b000465 | prose | pages [8] -->
14 36 0.7561

<!-- b000466 | furniture | pages [8] -->


<!-- b000467 | prose | pages [8] -->
35 13 0.5444

<!-- b000468 | prose | pages [8] -->
15 37 0.6846

<!-- b000469 | furniture | pages [8] -->


<!-- b000470 | prose | pages [8] -->
36 44 0.5412

<!-- b000471 | prose | pages [8] -->
16 50 0.6683

<!-- b000472 | furniture | pages [8] -->


<!-- b000473 | prose | pages [8] -->
37 39 0.539

<!-- b000474 | prose | pages [8] -->
17 38 0.6591

<!-- b000475 | furniture | pages [8] -->


<!-- b000476 | prose | pages [8] -->
38 47 0.5386

<!-- b000477 | prose | pages [8] -->
18 10 0.6344

<!-- b000478 | furniture | pages [8] -->


<!-- b000479 | prose | pages [8] -->
39 34 0.5366

<!-- b000480 | prose | pages [8] -->
19 51 0.6344

<!-- b000481 | furniture | pages [8] -->


<!-- b000482 | prose | pages [8] -->
40 15 0.5364

<!-- b000483 | prose | pages [8] -->
20 9 0.6288

<!-- b000484 | furniture | pages [8] -->


<!-- b000485 | prose | pages [8] -->
41 25 0.5327

<!-- b000486 | prose | pages [8] -->
21 17 0.6254

<!-- b000487 | furniture | pages [8] -->


<!-- b000488 | prose | pages [8] -->
42 12 0.5065

<!-- b000489 | furniture | pages [8] -->


<!-- b000490 | prose | pages [8] -->
No Node Pro No Node Pro

<!-- b000491 | prose | pages [8] -->
43 22 0.5022 64 55 0.2658

<!-- b000492 | prose | pages [8] -->
44 5 0.4969 65 82 0.254

<!-- b000493 | prose | pages [8] -->
45 8 0.4906 66 52 0.2209

<!-- b000494 | prose | pages [8] -->
46 24 0.49 67 56 0.201

<!-- b000495 | prose | pages [8] -->
47 26 0.4792 67 57 0.201

<!-- b000496 | prose | pages [8] -->
48 72 0.476 69 63 0.1989

<!-- b000497 | prose | pages [8] -->
49 20 0.4741 70 79 0.1978

<!-- b000498 | prose | pages [8] -->
50 4 0.4591 71 77 0.1907

<!-- b000499 | prose | pages [8] -->
51 40 0.4407 72 23 0.1891

<!-- b000500 | prose | pages [8] -->
52 32 0.4192 73 80 0.1608

<!-- b000501 | prose | pages [8] -->
52 58 0.4192 74 76 0.1001

<!-- b000502 | prose | pages [8] -->
54 53 0.3987 75 75 0.01

<!-- b000503 | prose | pages [8] -->
55 62 0.3977 76 0 0

<!-- b000504 | prose | pages [8] -->
56 66 0.3964 76 2 0

<!-- b000505 | prose | pages [8] -->
57 61 0.3963 76 48 0

<!-- b000506 | prose | pages [8] -->
58 35 0.3915 76 64 0

<!-- b000507 | prose | pages [8] -->
59 3 0.3672 76 65 0

<!-- b000508 | prose | pages [8] -->
60 29 0.3543 76 68 0

<!-- b000509 | prose | pages [8] -->
61 19 0.3313 76 74 0

<!-- b000510 | prose | pages [8] -->
62 71 0.2883 76 78 0

<!-- b000511 | prose | pages [8] -->
63 70 0.2766

<!-- b000512 | furniture | pages [8] -->


<!-- b000513 | furniture | pages [8] -->


<!-- b000514 | furniture | pages [8] -->


<!-- b000515 | prose | pages [8] -->
dp = As for discriminate line, we previously have 0.5 , we can distinguish that the 43 previous workers in the list is categorized as conspirators while the others are non-conspirators.

<!-- b000516 | furniture | pages [8] -->


<!-- b000517 | furniture | pages [8] -->


<!-- b000518 | furniture | pages [9] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000519 | heading | pages [9] -->
Model 3

<!-- b000520 | prose | pages [9] -->
Introduction of graph theory

<!-- b000521 | furniture | pages [9] -->
8

<!-- b000522 | prose | pages [9] -->
In mathematics and computer science, graph theory is the study of graphs, mathematical structures used to model pairwise relations between objects from a certain collection. A “graph” in this context is a collection of “vertices” or “nodes” and a collection of edges that connect pairs of vertices. The “shortest path” represents a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized. And Dijkstra's algorithm, is a graph search algorithm that solves the single-source shortest path problem for a graph with nonnegative edge path costs, producing a shortest path tree.

<!-- b000523 | furniture | pages [9] -->


<!-- b000524 | prose | pages [9] -->
Establishment and Algorithm of the model

<!-- b000525 | prose | pages [9] -->
We develop a model based on graph theory which is good at dealing with network problem. As far as the second figure ICM shows us in the problem paper, we use a

<!-- b000526 | prose | pages [9] -->
=

<!-- b000527 | prose | pages [9] -->
to visualize the message traffic. A set of vertices graph

<!-- b000528 | prose | pages [9] -->
G { ( ), V G E G ( )}

<!-- b000529 | furniture | pages [9] -->


<!-- b000530 | prose | pages [9] -->
V G ( )

<!-- b000531 | prose | pages [9] -->
represents office workers, and a set of edges known conspirators is named represents messages. A set of

<!-- b000532 | prose | pages [9] -->
E G ( )

<!-- b000533 | prose | pages [9] -->
while a set of known non-conspirators is named

<!-- b000534 | prose | pages [9] -->
V G 0( ) ( ) V G

<!-- b000535 | prose | pages [9] -->
.

<!-- b000536 | prose | pages [9] -->
n

<!-- b000537 | prose | pages [9] -->
A member communicates with another through several paths in the conspirators’ message network. However，in order to reduce the intercepted risk in the process of information transfer, they usually choose the shortest one. So the shortest path is much more important than the longer one in the assessment of the suspicion. Of course, suspicious messages are more important than the unsuspicious one as well. So the probability of one’s being conspirator depends on the type and quantity of his message traffic, as well as the shortest distance between him and known conspirator group. It means the shortest distance between this vertex

<!-- b000538 | prose | pages [9] -->
in the network. We use

<!-- b000539 | prose | pages [9] -->
d v V G ( , V G 0( ) i 0

<!-- b000540 | prose | pages [9] -->
quantity of the edges.

<!-- b000541 | prose | pages [9] -->
=

<!-- b000542 | prose | pages [9] -->
and any element of

<!-- b000543 | prose | pages [9] -->
iv

<!-- b000544 | prose | pages [9] -->
( ))

<!-- b000545 | prose | pages [9] -->
to represent it, and its value is the

<!-- b000546 | prose | pages [9] -->
∈ min{ ( , d v V G ( , ( )) i 0 k d v v }, v V G ( ) (6) i k k 0

<!-- b000547 | prose | pages [9] -->
In conclusion, a suspicious index named is used to decide whether a

<!-- b000548 | prose | pages [9] -->
Score

<!-- b000549 | prose | pages [9] -->
member is worth to be suspicious. For each vertex, in

<!-- b000550 | prose | pages [9] -->
V G Score

<!-- b000551 | prose | pages [9] -->
, =10 ,while in

<!-- b000552 | prose | pages [9] -->
V G 0( ) Score i

<!-- b000553 | prose | pages [9] -->
=0. And the other vertices can be computed by ,

<!-- b000554 | prose | pages [9] -->
( ) N i

<!-- b000555 | furniture | pages [9] -->


<!-- b000556 | prose | pages [9] -->
=∑ Score

<!-- b000557 | prose | pages [9] -->
i

<!-- b000558 | prose | pages [9] -->
w

<!-- b000559 | prose | pages [9] -->
j

<!-- b000560 | prose | pages [9] -->
(7) d v V G

<!-- b000561 | prose | pages [9] -->
j

<!-- b000562 | prose | pages [9] -->
w

<!-- b000563 | prose | pages [9] -->
represents the weight of edge Where

<!-- b000564 | prose | pages [9] -->
j

<!-- b000565 | prose | pages [9] -->
( , ( ))

<!-- b000566 | prose | pages [9] -->
i

<!-- b000567 | prose | pages [9] -->
0

<!-- b000568 | prose | pages [9] -->
, which is linked with the vertex

<!-- b000569 | prose | pages [9] -->
iv

<!-- b000570 | furniture | pages [9] -->


<!-- b000571 | prose | pages [9] -->
ie

<!-- b000572 | prose | pages [9] -->
iv

<!-- b000573 | prose | pages [9] -->
directly; the summation symbol is for all the edges linked directly with the vertex .

<!-- b000574 | prose | pages [9] -->
i

<!-- b000575 | prose | pages [9] -->
is, the more suspicious the office worker

<!-- b000576 | prose | pages [9] -->
Score

<!-- b000577 | prose | pages [9] -->
The larger

<!-- b000578 | prose | pages [9] -->
i

<!-- b000579 | prose | pages [9] -->
is.

<!-- b000580 | prose | pages [9] -->
can be described as Figure 5. Score The calculating process of i

<!-- b000581 | furniture | pages [9] -->


<!-- b000582 | furniture | pages [10] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000583 | furniture | pages [10] -->
9

<!-- b000584 | furniture | pages [10] -->


<!-- b000585 | prose | pages [10] -->
Figure 5

<!-- b000586 | furniture | pages [10] -->


<!-- b000587 | prose | pages [10] -->
Algorithm 2 Step 1: Create the set of known conspirators ;

<!-- b000588 | prose | pages [10] -->
( ) V G n

<!-- b000589 | prose | pages [10] -->
and the set of non-conspirators

<!-- b000590 | prose | pages [10] -->
V G 0( )

<!-- b000591 | prose | pages [10] -->
Step 2: Compute the shortest distance from all the vertices to the

<!-- b000592 | furniture | pages [10] -->


<!-- b000593 | prose | pages [10] -->
; V G 0( )

<!-- b000594 | prose | pages [10] -->
Based on message network, create an adjacency matrix with the connected value

<!-- b000595 | prose | pages [10] -->
= d v V G ( , ( )) 0

<!-- b000596 | prose | pages [10] -->
equaled to 1 and the unconnected value equaled to 0. Initialize

<!-- b000597 | prose | pages [10] -->
= +∞ in V G 0( ) d v V G ( , ( ))

<!-- b000598 | prose | pages [10] -->
set of , and

<!-- b000599 | prose | pages [10] -->
k 0 1)

<!-- b000600 | prose | pages [10] -->
in the

<!-- b000601 | prose | pages [10] -->
k 0

<!-- b000602 | prose | pages [10] -->
V G ( ) , n n V G ,then search for any other vertex in matrix Start the vertices of 0( ) V G at the which connected with it directly and consist of a new set 1( ) same time , have its value equal to 1, 2) Continue to search down. But if one vertex has been visited, its value will not be assigned again. The loop will not stop until all the vertices are accessed;

<!-- b000603 | furniture | pages [10] -->


<!-- b000604 | prose | pages [10] -->
w

<!-- b000605 | prose | pages [10] -->
Step 3: Visit all the edges, assign a value to their weights

<!-- b000606 | prose | pages [10] -->
d v V G ( , ( ))

<!-- b000607 | prose | pages [10] -->
equation(6) to calculate

<!-- b000608 | prose | pages [10] -->
i 0

<!-- b000609 | prose | pages [10] -->
w

<!-- b000610 | prose | pages [10] -->
j

<!-- b000611 | prose | pages [10] -->
;

<!-- b000612 | prose | pages [10] -->
( , ( ))

<!-- b000613 | prose | pages [10] -->
d v V G

<!-- b000614 | prose | pages [10] -->
i

<!-- b000615 | prose | pages [10] -->
0

<!-- b000616 | prose | pages [10] -->
, and according to the

<!-- b000617 | prose | pages [10] -->
j

<!-- b000618 | prose | pages [10] -->
. And let its two vertices cumulative

<!-- b000619 | furniture | pages [11] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000620 | furniture | pages [11] -->
10

<!-- b000621 | furniture | pages [11] -->


<!-- b000622 | prose | pages [11] -->
Figure 6 d is the distance where searching the vertices. A known conspirator is represented by a black round

<!-- b000623 | furniture | pages [11] -->


<!-- b000624 | prose | pages [11] -->
Step 4: As for the vertices in V G , Scoreis assigned to 10.0 ; for the vertices in 0( )

<!-- b000625 | prose | pages [11] -->
V G , Scoreis assigned to 0.0 ;for the other vertices, Scorecan also be calculated. ( ) n

<!-- b000626 | furniture | pages [11] -->


<!-- b000627 | prose | pages [11] -->
Result and analys

<!-- b000628 | prose | pages [11] -->
is

<!-- b000629 | prose | pages [11] -->
In the model, we set

<!-- b000630 | prose | pages [11] -->
⎧ if the jthedg is asuspiciousmessage 1.0

<!-- b000631 | prose | pages [11] -->
= ⎨ w j

<!-- b000632 | furniture | pages [11] -->


<!-- b000633 | prose | pages [11] -->
if the jthedgis aunsuspiciousmessage 0.1

<!-- b000634 | prose | pages [11] -->
⎩

<!-- b000635 | prose | pages [11] -->
ssages is equal to 1 suspicious message

<!-- b000636 | prose | pages [11] -->
It means the effect of 10 unsuspicious me in the suspicious evaluation.

<!-- b000637 | prose | pages [11] -->
Score i = "

<!-- b000638 | heading | pages [11] -->
Based on the Algorithm 2, compute each

<!-- b000639 | prose | pages [11] -->
down, and list them on table 3:

<!-- b000640 | furniture | pages [11] -->


<!-- b000641 | prose | pages [11] -->
Score , size ( 1,2,3, ,83)

<!-- b000642 | furniture | pages [11] -->


<!-- b000643 | prose | pages [11] -->
i i

<!-- b000644 | prose | pages [11] -->
Table 3

<!-- b000645 | prose | pages [11] -->
No node Score

<!-- b000646 | furniture | pages [11] -->


<!-- b000647 | prose | pages [11] -->
No no Sco

<!-- b000648 | prose | pages [11] -->
de re

<!-- b000649 | prose | pages [11] -->
1 10.000 22 44 3.700 7

<!-- b000650 | prose | pages [11] -->
1 10.000 22 50 3.800 18

<!-- b000651 | prose | pages [11] -->
24 30 3.300

<!-- b000652 | prose | pages [11] -->
1 10.000 21

<!-- b000653 | furniture | pages [11] -->


<!-- b000654 | prose | pages [11] -->
24 31 3.300

<!-- b000655 | prose | pages [11] -->
1 10.000 43

<!-- b000656 | prose | pages [11] -->
1 10.000 26 35 3.100 49

<!-- b000657 | prose | pages [11] -->
1 10.000 27 4 3.050 54

<!-- b000658 | prose | pages [11] -->
1

<!-- b000659 | prose | pages [11] -->
10.000 28 27 3.000 67

<!-- b000660 | prose | pages [11] -->
15 2.900

<!-- b000661 | prose | pages [11] -->
8 3 8.200

<!-- b000662 | furniture | pages [11] -->


<!-- b000663 | prose | pages [11] -->
29

<!-- b000664 | prose | pages [11] -->
9

<!-- b000665 | prose | pages [11] -->
10 7.100

<!-- b000666 | furniture | pages [11] -->


<!-- b000667 | prose | pages [11] -->
30 13 2.850

<!-- b000668 | furniture | pages [11] -->


<!-- b000669 | prose | pages [11] -->
2.850

<!-- b000670 | prose | pages [11] -->
10 17 6.500

<!-- b000671 | furniture | pages [11] -->


<!-- b000672 | prose | pages [11] -->
30 32

<!-- b000673 | prose | pages [11] -->
11 34 6.000

<!-- b000674 | furniture | pages [11] -->


<!-- b000675 | prose | pages [11] -->
32 36 2.800

<!-- b000676 | furniture | pages [11] -->


<!-- b000677 | prose | pages [11] -->
12 16 5.500

<!-- b000678 | furniture | pages [11] -->


<!-- b000679 | prose | pages [11] -->
33 46 2.7

<!-- b000680 | prose | pages [11] -->
00

<!-- b000681 | prose | pages [11] -->
13 81 5.100

<!-- b000682 | furniture | pages [11] -->


<!-- b000683 | prose | pages [11] -->
34 22 2.650

<!-- b000684 | prose | pages [11] -->
14 47 4.900

<!-- b000685 | furniture | pages [11] -->


<!-- b000686 | prose | pages [11] -->
35 14 2.300

<!-- b000687 | prose | pages [11] -->
No node Score No node Score

<!-- b000688 | prose | pages [11] -->
42 40 1 .600 63 71 0.2 00

<!-- b000689 | prose | pages [11] -->
44 1 1.500 65 62 0.133

<!-- b000690 | prose | pages [11] -->
44 5 1.500 65 70 0.133

<!-- b000691 | prose | pages [11] -->
44 69 1.500 67 55 0.100

<!-- b000692 | prose | pages [11] -->
47 9 1.400 67 73 0.100

<!-- b000693 | prose | pages [11] -->
47 42 1.400 7 76 0.100

<!-- b000694 | prose | pages [11] -->
6

<!-- b000695 | prose | pages [11] -->
49 12 1.200 70 52 0.075

<!-- b000696 | prose | pages [11] -->
49 60 1.200 71 53 0.067

<!-- b000697 | furniture | pages [11] -->


<!-- b000698 | prose | pages [11] -->
80

<!-- b000699 | furniture | pages [11] -->


<!-- b000700 | prose | pages [11] -->
72 59 0.050

<!-- b000701 | prose | pages [11] -->
51

<!-- b000702 | furniture | pages [11] -->


<!-- b000703 | prose | pages [11] -->
1.100

<!-- b000704 | furniture | pages [11] -->


<!-- b000705 | prose | pages [11] -->
52 25 1.000 72 63 0.050

<!-- b000706 | prose | pages [11] -->
53 39 0.850 74 58 0.033

<!-- b000707 | furniture | pages [11] -->


<!-- b000708 | prose | pages [11] -->
23 0.750 75 61 0.025

<!-- b000709 | prose | pages [11] -->
54

<!-- b000710 | prose | pages [11] -->
55 26 0.700 76 0 0.000

<!-- b000711 | prose | pages [11] -->
56 79 0.550 76 2 0.000

<!-- b000712 | furniture | pages [12] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000713 | prose | pages [12] -->
15 28 4.600

<!-- b000714 | furniture | pages [12] -->


<!-- b000715 | prose | pages [12] -->
36 33 2.200

<!-- b000716 | prose | pages [12] -->
16 19 4.200

<!-- b000717 | furniture | pages [12] -->


<!-- b000718 | prose | pages [12] -->
36 45 2.200

<!-- b000719 | prose | pages [12] -->
16 20 4.200

<!-- b000720 | furniture | pages [12] -->


<!-- b000721 | prose | pages [12] -->
38 29 2.000

<!-- b000722 | prose | pages [12] -->
16 37 4.200

<!-- b000723 | furniture | pages [12] -->


<!-- b000724 | prose | pages [12] -->
39 82 1.800

<!-- b000725 | prose | pages [12] -->
19 6 4.000

<!-- b000726 | furniture | pages [12] -->


<!-- b000727 | prose | pages [12] -->
40 8 1.750

<!-- b000728 | prose | pages [12] -->
19 38 4.000

<!-- b000729 | furniture | pages [12] -->


<!-- b000730 | prose | pages [12] -->
41 24 1.650

<!-- b000731 | prose | pages [12] -->
19 41 4.000

<!-- b000732 | furniture | pages [12] -->


<!-- b000733 | prose | pages [12] -->
42 11 1.600

<!-- b000734 | furniture | pages [12] -->


<!-- b000735 | prose | pages [12] -->
rthe ore, w t cri al v ue as Fu rm e se tic al

<!-- b000736 | furniture | pages [12] -->
11

<!-- b000737 | prose | pages [12] -->
57 51 0.500 76 48 0.000

<!-- b000738 | prose | pages [12] -->
58 72 0.400 76 64 0.000

<!-- b000739 | prose | pages [12] -->
59 66 0.300 76 65 0.000

<!-- b000740 | prose | pages [12] -->
59 75 0.300 76 68 0.000

<!-- b000741 | prose | pages [12] -->
61 56 0.275 76 74 0.000

<!-- b000742 | prose | pages [12] -->
62 77 0.250 76 78 0.000

<!-- b000743 | prose | pages [12] -->
63 57 0.200

<!-- b000744 | furniture | pages [12] -->


<!-- b000745 | furniture | pages [12] -->


<!-- b000746 | furniture | pages [12] -->


<!-- b000747 | furniture | pages [12] -->


<!-- b000748 | furniture | pages [12] -->


<!-- b000749 | prose | pages [12] -->
Score =

<!-- b000750 | prose | pages [12] -->
quiva to c tact ith

<!-- b000751 | prose | pages [12] -->
. It i s e lent on w 2

<!-- b000752 | prose | pages [12] -->
is r ona e to co er a ffic

<!-- b000753 | prose | pages [12] -->
the known conspirator group by 2 messages. It

<!-- b000754 | prose | pages [12] -->
lin on tab

<!-- b000755 | prose | pages [12] -->
worker is a conspirator. Draw a e

<!-- b000756 | prose | pages [12] -->
bef the umbe

<!-- b000757 | prose | pages [12] -->
being conspirator comes ore n

<!-- b000758 | prose | pages [12] -->
the 38 p viou ork rs in th

<!-- b000759 | prose | pages [12] -->
conclude that re s w e

<!-- b000760 | prose | pages [12] -->
irators.

<!-- b000761 | prose | pages [12] -->
the others are non-consp

<!-- b000762 | furniture | pages [12] -->


<!-- b000763 | prose | pages [12] -->
eas bl nsid n o e

<!-- b000764 | prose | pages [12] -->
hic how hat the e p abi y of

<!-- b000765 | prose | pages [12] -->
le, w h s t larg rob lit

<!-- b000766 | prose | pages [12] -->
criti val . Thro ana ing we

<!-- b000767 | prose | pages [12] -->
r of cal ue ugh lyz ,

<!-- b000768 | prose | pages [12] -->
t ar ateg rized a nsp ors hile

<!-- b000769 | prose | pages [12] -->
e lis e c o s co irat w

<!-- b000770 | heading | pages [12] -->
Results comparison of Model 1, 2 and 3

<!-- b000771 | prose | pages [12] -->
Put t is get p

<!-- b000772 | prose | pages [12] -->
ting hree l ts we res ectivel

<!-- b000773 | caption | pages [12] -->
Figure 7 to co

<!-- b000774 | prose | pages [12] -->
e sist cy

<!-- b000775 | prose | pages [12] -->
mpare th con en of all

<!-- b000776 | prose | pages [12] -->
y in ree d eth we

<!-- b000777 | prose | pages [12] -->
th mo els tog er, can draw

<!-- b000778 | prose | pages [12] -->
three de su

<!-- b000779 | prose | pages [12] -->
mo l re lts.

<!-- b000780 | furniture | pages [12] -->


<!-- b000781 | prose | pages [12] -->
Figure. 7

<!-- b000782 | furniture | pages [12] -->


<!-- b000783 | prose | pages [12] -->
Note that we use logarithmic scale for the vertical axis as rank changes are m

<!-- b000784 | prose | pages [12] -->
uch

<!-- b000785 | prose | pages [12] -->
more important in high-ranking part than low-ranking part.

<!-- b000786 | prose | pages [12] -->
And from Figure 7 we can intuitively see certain changes in some particular nodes are apparent but the whole ranking distributions of three models in all 83 nodes are similar.

<!-- b000787 | furniture | pages [12] -->


<!-- b000788 | heading | pages [12] -->
Model 4

<!-- b000789 | prose | pages [12] -->
Relevant work

<!-- b000790 | prose | pages [12] -->
Centrality is a common Social network analysis which can be used to solve criminal network models (Peng Chen ,2011). Linton C. Freeman put forward a set of calculation method to find out the importance of any member in network (Freeman

<!-- b000791 | prose | pages [12] -->
s point ce

<!-- b000792 | prose | pages [12] -->
1979). He explained some terms such a ntrality oint degree of Point centrality: In a social network, if a conspirator has direct

<!-- b000793 | prose | pages [12] -->
P

<!-- b000794 | prose | pages [12] -->
ct with other conspirators, this conspirator is in the central part of the network

<!-- b000795 | prose | pages [12] -->
conta

<!-- b000796 | prose | pages [12] -->
and has much more control power. Thus the importance of a point could be weighed by the number of points linked to it.

<!-- b000797 | prose | pages [12] -->
C n ( ) D i = = d n (8) ( ) i

<!-- b000798 | furniture | pages [13] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000799 | furniture | pages [13] -->
12

<!-- b000800 | prose | pages [13] -->
d n is the number of points that member Where ( ) i

<!-- b000801 | prose | pages [13] -->
in

<!-- b000802 | prose | pages [13] -->
has contact with. The igher the point centrality degree, the more likely the conspirators is a leader.

<!-- b000803 | prose | pages [13] -->
h

<!-- b000804 | prose | pages [13] -->
ness of Point centrality: A point that falls on the shortest

<!-- b000805 | prose | pages [13] -->
Between communicatio

<!-- b000806 | prose | pages [13] -->
n paths between other points exhibits a potential for control of their

<!-- b000807 | prose | pages [13] -->
communication.

<!-- b000808 | prose | pages [13] -->
It is this potential for control that defines the centrality of these

<!-- b000809 | prose | pages [13] -->
ts.

<!-- b000810 | prose | pages [13] -->
poin

<!-- b000811 | prose | pages [13] -->
= ∑

<!-- b000812 | prose | pages [13] -->
C ( ) n B i j k

<!-- b000813 | prose | pages [13] -->
Where

<!-- b000814 | prose | pages [13] -->
g ( ) / n g

<!-- b000815 | prose | pages [13] -->
(9)

<!-- b000816 | prose | pages [13] -->
jk i jk

<!-- b000817 | prose | pages [13] -->
< <

<!-- b000818 | prose | pages [13] -->
g is the number of the shortest paths linking arbitrary conspirator jk

<!-- b000819 | prose | pages [13] -->
kn , but not including in .

<!-- b000820 | prose | pages [13] -->
and

<!-- b000821 | prose | pages [13] -->
arbitrary

<!-- b000822 | prose | pages [13] -->
kn that contain in and

<!-- b000823 | prose | pages [13] -->
jn

<!-- b000824 | prose | pages [13] -->
g g ( ) n is the number of paths linking jn jk i

<!-- b000825 | prose | pages [13] -->
y: Concerning with either independence or

<!-- b000826 | prose | pages [13] -->
Closeness of Point centralit

<!-- b000827 | prose | pages [13] -->
efficiency during the delivering of messages nece be m

<!-- b000828 | prose | pages [13] -->
, closeness of point centrality is

<!-- b000829 | prose | pages [13] -->
a

<!-- b000830 | prose | pages [13] -->
easured since it grows as points are far ap rt. ssarily to

<!-- b000831 | prose | pages [13] -->
= C n ( ) C i

<!-- b000832 | prose | pages [13] -->
Where ( , )

<!-- b000833 | prose | pages [13] -->
1 (10) g g

<!-- b000834 | prose | pages [13] -->
=∑ =∑

<!-- b000835 | prose | pages [13] -->
d n n

<!-- b000836 | prose | pages [13] -->
( , ) i j 1 1 j j

<!-- b000837 | prose | pages [13] -->
is the shortest distances between conspirator d n n i j in and in .

<!-- b000838 | prose | pages [13] -->
of the shortest distance from one conspirator to o

<!-- b000839 | prose | pages [13] -->
is an inverse of sum

<!-- b000840 | prose | pages [13] -->
C n ( ) C i

<!-- b000841 | prose | pages [13] -->
thers.

<!-- b000842 | prose | pages [13] -->
The larger its value is, the closer the relationship he/she

<!-- b000843 | furniture | pages [13] -->


<!-- b000844 | prose | pages [13] -->
Establishment of model

<!-- b000845 | prose | pages [13] -->
have with others.

<!-- b000846 | prose | pages [13] -->
lu e the p

<!-- b000847 | prose | pages [13] -->
In order to comprehensively eva at robability of one conspirator’s being

<!-- b000848 | prose | pages [13] -->
r, we define an aggregative index number

<!-- b000849 | prose | pages [13] -->
leade

<!-- b000850 | prose | pages [13] -->
β = C C 1

<!-- b000851 | prose | pages [13] -->
C

<!-- b000852 | prose | pages [13] -->
β β + + * * * * (11) C C 2 3 D D B C β represent weight coefficient of point degree, betweenness β , β and Where 1 2 3

<!-- b000853 | prose | pages [13] -->
* * C , C and and closenes s respectively.

<!-- b000854 | furniture | pages [13] -->


<!-- b000855 | prose | pages [13] -->
D B * *

<!-- b000856 | prose | pages [13] -->
C

<!-- b000857 | prose | pages [13] -->
C C are normalization of C ,

<!-- b000858 | prose | pages [13] -->
C and .

<!-- b000859 | prose | pages [13] -->
C C D B C

<!-- b000860 | prose | pages [13] -->
In addition, we define another aggregative

<!-- b000861 | prose | pages [13] -->
index reflecting the network’s

<!-- b000862 | prose | pages [13] -->
structure called network density, to assess the average of shortest distances of any two

<!-- b000863 | prose | pages [13] -->
er the value of the index is, the safer but less tors

<!-- b000864 | prose | pages [13] -->
conspira . The larg

<!-- b000865 | prose | pages [13] -->
nization be calculated by:

<!-- b000866 | prose | pages [13] -->
orga is. It can

<!-- b000867 | prose | pages [13] -->
,

<!-- b000868 | prose | pages [13] -->
ficient the

<!-- b000869 | prose | pages [13] -->
ef

<!-- b000870 | prose | pages [13] -->
∑

<!-- b000871 | prose | pages [13] -->
d

<!-- b000872 | prose | pages [13] -->
ij

<!-- b000873 | prose | pages [13] -->
∈ ∈ ≠

<!-- b000874 | prose | pages [13] -->
, ,

<!-- b000875 | prose | pages [13] -->
i j G i

<!-- b000876 | prose | pages [13] -->
ρ

<!-- b000877 | prose | pages [13] -->
= 1

<!-- b000878 | prose | pages [13] -->
j

<!-- b000879 | prose | pages [13] -->
(12)

<!-- b000880 | prose | pages [13] -->
2 N N −

<!-- b000881 | prose | pages [13] -->
Result and analysis

<!-- b000882 | prose | pages [13] -->
( ( 1)

<!-- b000883 | prose | pages [13] -->
Start a new social network of 43 conspirat ρ = 2.1971 s located in model 2. Then we have

<!-- b000884 | prose | pages [13] -->
or

<!-- b000885 | prose | pages [13] -->
tor can transmit information

<!-- b000886 | prose | pages [13] -->
after computing, which means that a conspira

<!-- b000887 | prose | pages [13] -->
rough only 2.1971 messages in average. That’s to say, the other c sp ator

<!-- b000888 | prose | pages [13] -->
to an on ir th

<!-- b000889 | prose | pages [13] -->
o ose t ensure safety. If a conspirator were caught, the others would ture are

<!-- b000890 | prose | pages [13] -->
struc to cl o

<!-- b000891 | prose | pages [13] -->
be found out in no time, which make the conspiracy at gr r k. How er

<!-- b000892 | prose | pages [13] -->
eat is ev ,

<!-- b000893 | prose | pages [13] -->
piracy has great operation efficiency. The result shows that a commercial fraud

<!-- b000894 | prose | pages [13] -->
cons

<!-- b000895 | prose | pages [13] -->
often need close cooperation. Compute = = = C ,respectively. Then set C , C and D B C w w w 1/ 3 , compute 1 2 3

<!-- b000896 | furniture | pages [14] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000897 | prose | pages [14] -->
C , then we have Table 4 .

<!-- b000898 | furniture | pages [14] -->
13

<!-- b000899 | prose | pages [14] -->
Table 4 rank 1 2 3 4 5

<!-- b000900 | prose | pages [14] -->
C Paul Elsie Alex Yao Neal D

<!-- b000901 | prose | pages [14] -->
C Elsie Paul Ulf Jean Dolores B

<!-- b000902 | prose | pages [14] -->
C Paul Elsie Jean Neal Beth C C Paul Elsie Dolores Jean Neal

<!-- b000903 | prose | pages [14] -->
6 7 8 9 10

<!-- b000904 | prose | pages [14] -->
Julia Jerome Stephanie Dolores Beth

<!-- b000905 | prose | pages [14] -->
William Yao Neal Alex Lars

<!-- b000906 | prose | pages [14] -->
Dolores Alex Kristina Jerome William Alex Ulf Yao Jerome Beth

<!-- b000907 | caption | pages [14] -->
Table 4 shows us Paul, Elsie and Dolores are three most probable conspiracy

<!-- b000908 | prose | pages [14] -->
leaders. Since Delores is one of the senior managers in the company, it may be an important intelligence.

<!-- b000909 | furniture | pages [14] -->


<!-- b000910 | prose | pages [14] -->
ee of Point centrality

<!-- b000911 | prose | pages [14] -->
20

<!-- b000912 | prose | pages [14] -->
15

<!-- b000913 | prose | pages [14] -->
10

<!-- b000914 | prose | pages [14] -->
5

<!-- b000915 | prose | pages [14] -->
egr

<!-- b000916 | prose | pages [14] -->
point d

<!-- b000917 | prose | pages [14] -->
0 0 5 10 15 20 25 30 35 40

<!-- b000918 | prose | pages [14] -->
rank of pro

<!-- b000919 | prose | pages [14] -->
bability

<!-- b000920 | prose | pages [14] -->
of being a

<!-- b000921 | prose | pages [14] -->
conspir

<!-- b000922 | prose | pages [14] -->
ator

<!-- b000923 | prose | pages [14] -->
entrality

<!-- b000924 | prose | pages [14] -->
0.015

<!-- b000925 | prose | pages [14] -->
c

<!-- b000926 | prose | pages [14] -->
0.01

<!-- b000927 | prose | pages [14] -->
Closenes of Point

<!-- b000928 | prose | pages [14] -->
0.005

<!-- b000929 | prose | pages [14] -->
s

<!-- b000930 | prose | pages [14] -->
0 0 5 10 15 20 25 30 35 40

<!-- b000931 | prose | pages [14] -->
rank of probability of being

<!-- b000932 | prose | pages [14] -->
a conspirat

<!-- b000933 | prose | pages [14] -->
or

<!-- b000934 | prose | pages [14] -->
ty

<!-- b000935 | prose | pages [14] -->
int centrali

<!-- b000936 | prose | pages [14] -->
0.2

<!-- b000937 | prose | pages [14] -->
0.15

<!-- b000938 | prose | pages [14] -->
of Po

<!-- b000939 | prose | pages [14] -->
0.1

<!-- b000940 | prose | pages [14] -->
eenness

<!-- b000941 | prose | pages [14] -->
0.05

<!-- b000942 | prose | pages [14] -->
0

<!-- b000943 | prose | pages [14] -->
Betw

<!-- b000944 | prose | pages [14] -->
0 5 10 15 20 25 30 35 40

<!-- b000945 | prose | pages [14] -->
rank of probability o

<!-- b000946 | prose | pages [14] -->
f being a

<!-- b000947 | prose | pages [14] -->
conspirator

<!-- b000948 | prose | pages [14] -->
aggregative index number

<!-- b000949 | prose | pages [14] -->
1

<!-- b000950 | prose | pages [14] -->
0.5

<!-- b000951 | prose | pages [14] -->
0 0 5 10 15 20 25 30 35 40

<!-- b000952 | prose | pages [14] -->
rank of prob

<!-- b000953 | prose | pages [14] -->
ability of be

<!-- b000954 | prose | pages [14] -->
ing a conspira

<!-- b000955 | prose | pages [14] -->
tor

<!-- b000956 | furniture | pages [14] -->


<!-- b000957 | prose | pages [14] -->
Figure. 8 In Figure 8, the sequence number in horizontal axis indicates the rank of probability of being a conspirator, and the smaller the number is, the greater probability of being a

<!-- b000958 | prose | pages [14] -->
conspirator. We consider these three index have remarkable correction after we compute their Pearson correlation coefficient:

<!-- b000959 | prose | pages [14] -->
= = ( , ) 0.600, ( , ) r C C r C C D B D C

<!-- b000960 | prose | pages [14] -->
=

<!-- b000961 | prose | pages [14] -->
0.861 ( , ) 0.498 and r C C , B C

<!-- b000962 | prose | pages [14] -->
which all pass significant test at 0.1% level. Moreover, betweenness of Point centrality varies in each conspirator is more significant than point degree of point centrality while closeness of point centrality is the least important one.

<!-- b000963 | furniture | pages [14] -->


<!-- b000964 | furniture | pages [14] -->


<!-- b000965 | heading | pages [14] -->
Validation

<!-- b000966 | prose | pages [14] -->
● Based on the statement in the ion part, we can suppose that every

<!-- b000967 | prose | pages [14] -->
Introduct

<!-- b000968 | prose | pages [14] -->
rk

<!-- b000969 | prose | pages [14] -->
er in conspiracy group must have message contact with other conspirator more or

<!-- b000970 | prose | pages [14] -->
wo

<!-- b000971 | prose | pages [14] -->
less. So that a message network made up by all the conspirators should be a “connected graph”, which is a term in graph theory means there is a path from any point to any other point in the graph. That is to say, every conspirator has at leas

<!-- b000972 | prose | pages [14] -->
t one ssage exchange with another conspirator, or no single conspirator who has no

<!-- b000973 | prose | pages [14] -->
me

<!-- b000974 | prose | pages [14] -->
message exchange will exist. Take the “connected graph” method above as a validation method for Model 2 and 3. After the computation, we find that both Model 2 and Model 3 satisfy the “connected graph” condition.

<!-- b000975 | prose | pages [14] -->
● Both in Model 2 & 3, we have some model parameters that we set manually. In

<!-- b000976 | prose | pages [14] -->
o

<!-- b000977 | prose | pages [14] -->
er to validate the model stability when these parameters change to a small extent,

<!-- b000978 | prose | pages [14] -->
rd

<!-- b000979 | prose | pages [14] -->
we vary the value of these parameters, run the model program again, and see how

<!-- b000980 | prose | pages [14] -->
ch the result changes. In turns out that the most workers’ rank in the priority list

<!-- b000981 | prose | pages [14] -->
mu

<!-- b000982 | prose | pages [14] -->
remain invariant or change a little, which illustrate that our models are capable to

<!-- b000983 | furniture | pages [15] -->
Team # 13215                                                                                                             Page      of  18

<!-- b000984 | prose | pages [15] -->
tolerate certain changes

<!-- b000985 | furniture | pages [15] -->
14

<!-- b000986 | prose | pages [15] -->
in model parameters and our manually given value of these

<!-- b000987 | prose | pages [15] -->
parameter are relatively

<!-- b000988 | prose | pages [15] -->
reasonable.

<!-- b000989 | furniture | pages [15] -->


<!-- b000990 | prose | pages [15] -->
Impact of information changes

<!-- b000991 | prose | pages [15] -->
Information collected by investigation organizations is not always precise and sometimes during the process of investigation, new information would add in and old information would be revised. Thus a robust model is which, when input data is modified or some intrinsic parameters are changed a little, its results should not change a lot.

<!-- b000992 | prose | pages [15] -->
In this case, we assume the next situation: new information comes to light that Topic 1 is also connected to the conspiracy and that Ch

<!-- b000993 | prose | pages [15] -->
ris is one of the conspirators.

<!-- b000994 | prose | pages [15] -->
g Model 2 with some corresponding modification as an example, we will see how

<!-- b000995 | prose | pages [15] -->
Usin

<!-- b000996 | prose | pages [15] -->
would the priority lists we got before changed (using Model 3 is similar).

<!-- b000997 | furniture | pages [15] -->


<!-- b000998 | prose | pages [15] -->
New priority list generated by Model 2:

<!-- b000999 | prose | pages [15] -->
Table 5

<!-- b001000 | prose | pages [15] -->
No node pro

<!-- b001001 | furniture | pages [15] -->


<!-- b001002 | prose | pages [15] -->
No node pro

<!-- b001003 | prose | pages [15] -->
1 1

<!-- b001004 | furniture | pages [15] -->


<!-- b001005 | prose | pages [15] -->
22 27 0.6177 ↑0

<!-- b001006 | prose | pages [15] -->
1 1

<!-- b001007 | furniture | pages [15] -->


<!-- b001008 | prose | pages [15] -->
23 17 0.6176 7

<!-- b001009 | prose | pages [15] -->
1 1

<!-- b001010 | furniture | pages [15] -->


<!-- b001011 | prose | pages [15] -->
24 9 0.6132 18

<!-- b001012 | prose | pages [15] -->
1 1

<!-- b001013 | furniture | pages [15] -->


<!-- b001014 | prose | pages [15] -->
25 31 0.6046 21

<!-- b001015 | prose | pages [15] -->
1 1

<!-- b001016 | furniture | pages [15] -->


<!-- b001017 | prose | pages [15] -->
26 1 0.599 43

<!-- b001018 | prose | pages [15] -->
1 1

<!-- b001019 | furniture | pages [15] -->


<!-- b001020 | prose | pages [15] -->
27 ↑28 0.5882 49

<!-- b001021 | prose | pages [15] -->
1 1

<!-- b001022 | furniture | pages [15] -->


<!-- b001023 | prose | pages [15] -->
28 6 0.58 54

<!-- b001024 | prose | pages [15] -->
1 1

<!-- b001025 | furniture | pages [15] -->


<!-- b001026 | prose | pages [15] -->
29 ↓14 0.5795 67

<!-- b001027 | prose | pages [15] -->
1 73 1

<!-- b001028 | furniture | pages [15] -->


<!-- b001029 | prose | pages [15] -->
30 ↓50 0.5777

<!-- b001030 | prose | pages [15] -->
10 81 0.9774

<!-- b001031 | furniture | pages [15] -->


<!-- b001032 | prose | pages [15] -->
31 ↑20 0.5752

<!-- b001033 | prose | pages [15] -->
11 60 0.9404

<!-- b001034 | furniture | pages [15] -->


<!-- b001035 | prose | pages [15] -->
32 16 0.5721

<!-- b001036 | prose | pages [15] -->
12 59 0.9403

<!-- b001037 | furniture | pages [15] -->


<!-- b001038 | prose | pages [15] -->
33 46 0.5705

<!-- b001039 | prose | pages [15] -->
13 33 0.8004

<!-- b001040 | furniture | pages [15] -->


<!-- b001041 | prose | pages [15] -->
34 ↑25 0.5575

<!-- b001042 | prose | pages [15] -->
14 30 0.7766

<!-- b001043 | furniture | pages [15] -->


<!-- b001044 | prose | pages [15] -->
35 41 0.549

<!-- b001045 | prose | pages [15] -->
9

<!-- b001046 | prose | pages [15] -->
0 0

<!-- b001047 | prose | pages [15] -->
15 36 .7497

<!-- b001048 | furniture | pages [15] -->


<!-- b001049 | prose | pages [15] -->
36 34 .5428

<!-- b001050 | prose | pages [15] -->
0.7 6

<!-- b001051 | prose | pages [15] -->
16 ↑69 48

<!-- b001052 | furniture | pages [15] -->


<!-- b001053 | prose | pages [15] -->
37 ↓11 0.5421

<!-- b001054 | prose | pages [15] -->
↑

<!-- b001055 | furniture | pages [15] -->


<!-- b001056 | prose | pages [15] -->
0.7 2

<!-- b001057 | prose | pages [15] -->
17 45 00

<!-- b001058 | furniture | pages [15] -->


<!-- b001059 | prose | pages [15] -->
38 15 0.5349

<!-- b001060 | prose | pages [15] -->
0.6 3

<!-- b001061 | prose | pages [15] -->
18 37 57

<!-- b001062 | furniture | pages [15] -->


<!-- b001063 | prose | pages [15] -->
39 39 0.531

<!-- b001064 | prose | pages [15] -->
0.

<!-- b001065 | prose | pages [15] -->
6

<!-- b001066 | prose | pages [15] -->
19 38 65

<!-- b001067 | furniture | pages [15] -->


<!-- b001068 | prose | pages [15] -->
40 47 0.5296

<!-- b001069 | prose | pages [15] -->
0.6 4 ↓

<!-- b001070 | prose | pages [15] -->
20 10 36

<!-- b001071 | furniture | pages [15] -->


<!-- b001072 | prose | pages [15] -->
41 42 0.5238

<!-- b001073 | prose | pages [15] -->
0.6 4

<!-- b001074 | prose | pages [15] -->
20 51 36

<!-- b001075 | furniture | pages [15] -->


<!-- b001076 | prose | pages [15] -->
42 ↑40 0.5145

<!-- b001077 | furniture | pages [15] -->


<!-- b001078 | prose | pages [15] -->
C aring to the list w ot

<!-- b001079 | prose | pages [15] -->
omp e g before

<!-- b001080 | prose | pages [15] -->
No node pro No node pro

<!-- b001081 | prose | pages [15] -->
43 22 0.508 64 ↓61 0.2804

<!-- b001082 | prose | pages [15] -->
44 8 0.502

<!-- b001083 | prose | pages [15] -->
7 65 63 0.2553

<!-- b001084 | prose | pages [15] -->
45 26 0.4984

<!-- b001085 | prose | pages [15] -->
66 71 0.2345

<!-- b001086 | prose | pages [15] -->
46 ↓44 0.4968 67 70 0.2257

<!-- b001087 | prose | pages [15] -->
47 ↓12 0.4927 68 56 0.2225

<!-- b001088 | prose | pages [15] -->
48 5 0.4887 69 57 0.2225

<!-- b001089 | prose | pages [15] -->
49 4 0.4747 70 79 0.2031

<!-- b001090 | prose | pages [15] -->
50 ↑55 0.4704 71 77 0.1906

<!-- b001091 | prose | pages [15] -->
51 72 0.4633 72 23 0.1655

<!-- b001092 | prose | pages [15] -->
52 32 0.4492 73 80 0.164

<!-- b001093 | prose | pages [15] -->
52 58 0.4492 74 ↓66 0.106

<!-- b001094 | furniture | pages [15] -->


<!-- b001095 | prose | pages [15] -->
0.1

<!-- b001096 | prose | pages [15] -->
54 ↓13 0.4478 75 76

<!-- b001097 | prose | pages [15] -->
55 53 0.4188 76 75 0.01

<!-- b001098 | prose | pages [15] -->
6 3 0.404 77 2 0

<!-- b001099 | prose | pages [15] -->
5

<!-- b001100 | prose | pages [15] -->
0.

<!-- b001101 | prose | pages [15] -->
57 35 3925 77 48 0

<!-- b001102 | prose | pages [15] -->
58 ↑82 0.3667 77 64 0

<!-- b001103 | prose | pages [15] -->
59 29 0.3602 77 65 0

<!-- b001104 | prose | pages [15] -->
60 ↓24 0.3597 77 68 0

<!-- b001105 | prose | pages [15] -->
61 19 0.3312 77 74 0

<!-- b001106 | prose | pages [15] -->
62 52 0.2955 77 78 0

<!-- b001107 | prose | pages [15] -->
↓

<!-- b001108 | prose | pages [15] -->
63 62 0.2837

<!-- b001109 | furniture | pages [15] -->


<!-- b001110 | furniture | pages [15] -->


<!-- b001111 | furniture | pages [15] -->


<!-- b001112 | prose | pages [15] -->
, there are totally 20 office workers whose ositio change of ranking exceeds m th

<!-- b001113 | prose | pages [15] -->
ore an 5 p

<!-- b001114 | prose | pages [15] -->
i e l b n w on r

<!-- b001115 | prose | pages [15] -->
n th ist a ove. A d e c side our Mo

<!-- b001116 | furniture | pages [15] -->


<!-- b001117 | prose | pages [15] -->
S re

<!-- b001118 | prose | pages [15] -->
t ngth n wea

<!-- b001119 | prose | pages [15] -->
s a d w i n wi rro y

<!-- b001120 | prose | pages [15] -->
ns, hich s show th a w s mbols

<!-- b001121 | prose | pages [15] -->
del 2 sta th out t om ris

<!-- b001122 | prose | pages [15] -->
is ble rough he c pa on.

<!-- b001123 | prose | pages [15] -->
kn s

<!-- b001124 | prose | pages [15] -->
e ses

<!-- b001125 | furniture | pages [16] -->
Team # 13215                                                                                                             Page      of  18

<!-- b001126 | prose | pages [16] -->
In

<!-- b001127 | prose | pages [16] -->
thi paper, e dev

<!-- b001128 | prose | pages [16] -->
s w elo

<!-- b001129 | prose | pages [16] -->
p th ee mod

<!-- b001130 | prose | pages [16] -->
r

<!-- b001131 | furniture | pages [16] -->
15

<!-- b001132 | prose | pages [16] -->
els (

<!-- b001133 | prose | pages [16] -->
Mo

<!-- b001134 | prose | pages [16] -->
del

<!-- b001135 | prose | pages [16] -->
1

<!-- b001136 | prose | pages [16] -->
, 2

<!-- b001137 | prose | pages [16] -->
& 3)

<!-- b001138 | prose | pages [16] -->
to m

<!-- b001139 | prose | pages [16] -->
ake

<!-- b001140 | prose | pages [16] -->
a p ority

<!-- b001141 | prose | pages [16] -->
ri lis

<!-- b001142 | prose | pages [16] -->
t ng co w

<!-- b001143 | prose | pages [16] -->
hic

<!-- b001144 | prose | pages [16] -->
h

<!-- b001145 | prose | pages [16] -->
sho s the l e hoo

<!-- b001146 | prose | pages [16] -->
w ik li d o

<!-- b001147 | prose | pages [16] -->
f o

<!-- b001148 | prose | pages [16] -->
ne

<!-- b001149 | prose | pages [16] -->
’s bei

<!-- b001150 | prose | pages [16] -->
nomin

<!-- b001151 | prose | pages [16] -->
ate th consp ra y le

<!-- b001152 | prose | pages [16] -->
e i c ad

<!-- b001153 | prose | pages [16] -->
er.

<!-- b001154 | prose | pages [16] -->
●

<!-- b001155 | prose | pages [16] -->
Me ic equa io giv

<!-- b001156 | prose | pages [16] -->
tr t n en

<!-- b001157 | prose | pages [16] -->
in

<!-- b001158 | prose | pages [16] -->
M

<!-- b001159 | prose | pages [16] -->
odel 1

<!-- b001160 | prose | pages [16] -->
basic ide s and stra

<!-- b001161 | prose | pages [16] -->
a

<!-- b001162 | prose | pages [16] -->
tegy

<!-- b001163 | prose | pages [16] -->
to weigh the like

<!-- b001164 | prose | pages [16] -->
nsp ator and on

<!-- b001165 | prose | pages [16] -->
ir , e model (Model 4) to

<!-- b001166 | prose | pages [16] -->
is s

<!-- b001167 | prose | pages [16] -->
o c

<!-- b001168 | prose | pages [16] -->
on

<!-- b001169 | prose | pages [16] -->
cise nd cle

<!-- b001170 | prose | pages [16] -->
a ar th

<!-- b001171 | prose | pages [16] -->
at i

<!-- b001172 | prose | pages [16] -->
t g

<!-- b001173 | prose | pages [16] -->
ive

<!-- b001174 | prose | pages [16] -->
s us

<!-- b001175 | prose | pages [16] -->
th

<!-- b001176 | prose | pages [16] -->
e lihood of one’s being conspirator and its ence m

<!-- b001177 | prose | pages [16] -->
eth

<!-- b001178 | prose | pages [16] -->
od

<!-- b001179 | prose | pages [16] -->
an

<!-- b001180 | prose | pages [16] -->
d

<!-- b001181 | prose | pages [16] -->
result

<!-- b001182 | prose | pages [16] -->
a e

<!-- b001183 | prose | pages [16] -->
r

<!-- b001184 | prose | pages [16] -->
wor

<!-- b001185 | prose | pages [16] -->
th

<!-- b001186 | prose | pages [16] -->
bei

<!-- b001187 | prose | pages [16] -->
ng

<!-- b001188 | prose | pages [16] -->
refer d. B t as

<!-- b001189 | prose | pages [16] -->
u it

<!-- b001190 | prose | pages [16] -->
’s far

<!-- b001191 | prose | pages [16] -->
too

<!-- b001192 | prose | pages [16] -->
sim

<!-- b001193 | prose | pages [16] -->
ple to include lex m m

<!-- b001194 | prose | pages [16] -->
or

<!-- b001195 | prose | pages [16] -->
e f

<!-- b001196 | prose | pages [16] -->
acto , we d

<!-- b001197 | prose | pages [16] -->
rs ev lo

<!-- b001198 | prose | pages [16] -->
e p tw mo comp

<!-- b001199 | prose | pages [16] -->
o re ●

<!-- b001200 | prose | pages [16] -->
Mo el 2,

<!-- b001201 | prose | pages [16] -->
d w ic

<!-- b001202 | prose | pages [16] -->
h h i

<!-- b001203 | prose | pages [16] -->
s

<!-- b001204 | prose | pages [16] -->
base on pr

<!-- b001205 | prose | pages [16] -->
d

<!-- b001206 | prose | pages [16] -->
od

<!-- b001207 | prose | pages [16] -->
els

<!-- b001208 | prose | pages [16] -->
to

<!-- b001209 | prose | pages [16] -->
so

<!-- b001210 | prose | pages [16] -->
lve thi

<!-- b001211 | prose | pages [16] -->
s pro

<!-- b001212 | prose | pages [16] -->
ble

<!-- b001213 | prose | pages [16] -->
m a

<!-- b001214 | prose | pages [16] -->
t it

<!-- b001215 | prose | pages [16] -->
s ba

<!-- b001216 | prose | pages [16] -->
sis

<!-- b001217 | prose | pages [16] -->
. obab

<!-- b001218 | prose | pages [16] -->
ilit

<!-- b001219 | prose | pages [16] -->
y

<!-- b001220 | prose | pages [16] -->
theo y, rega

<!-- b001221 | prose | pages [16] -->
r rds

<!-- b001222 | prose | pages [16] -->
the

<!-- b001223 | prose | pages [16] -->
w

<!-- b001224 | prose | pages [16] -->
hole

<!-- b001225 | prose | pages [16] -->
no

<!-- b001226 | prose | pages [16] -->
de

<!-- b001227 | prose | pages [16] -->
s network linking through various kinds of m

<!-- b001228 | prose | pages [16] -->
ess

<!-- b001229 | prose | pages [16] -->
ag

<!-- b001230 | prose | pages [16] -->
es a a “pro

<!-- b001231 | prose | pages [16] -->
s ba

<!-- b001232 | prose | pages [16] -->
bility network”. I

<!-- b001233 | furniture | pages [16] -->


<!-- b001234 | prose | pages [16] -->
t illfully links every node together using the Law of Total Probability, which makes

<!-- b001235 | prose | pages [16] -->
sk

<!-- b001236 | prose | pages [16] -->
y office worker’s probability of being a conspirator related to each other by

<!-- b001237 | prose | pages [16] -->
ever

<!-- b001238 | prose | pages [16] -->
message type and number.

<!-- b001239 | prose | pages [16] -->
n

<!-- b001240 | prose | pages [16] -->
● Model 3, which is based on graph theory, take the “distance” between a

<!-- b001241 | prose | pages [16] -->
nknown office worker and a known conspirator into account starting from the

<!-- b001242 | prose | pages [16] -->
u

<!-- b001243 | prose | pages [16] -->
l indicates the closeness

<!-- b001244 | prose | pages [16] -->
structure of the network graph. The “distance” we define wel

<!-- b001245 | prose | pages [16] -->
stance”, the more likely

<!-- b001246 | prose | pages [16] -->
of relationship with known conspirators. The shorter the “di the unknown one is a conspirator.

<!-- b001247 | prose | pages [16] -->
● Model 4 determines one’s possibility of being the conspiracy leader from the prospective of centrality, which conforms to the characteristic of leaders in real criminal organization.

<!-- b001248 | furniture | pages [16] -->


<!-- b001249 | prose | pages [16] -->
In order to enhance our model and increase the accuracy of our model results, some shortcoming and additional aspects about our models need to be pointed out so that further improvement and refinement can be made:

<!-- b001250 | prose | pages [16] -->
● Some model parameters such as weight coefficients and discriminate line in our models are mostly determined manually, which could cause uncertainty of our model solutions and the priority will change to some extent if different constant is set. Although we have varied the value of these constants and validate the models’ stability, we still can’t exp

<!-- b001251 | prose | pages [16] -->
lain why the way we set these values can guarantee the

<!-- b001252 | prose | pages [16] -->
rdance of our model results to the reality. Improvement methods are that we

<!-- b001253 | prose | pages [16] -->
acco

<!-- b001254 | prose | pages [16] -->
figure out a most suitable value for these model parameters by more means such as comparison with other model’s result, more actual cases, etc.

<!-- b001255 | prose | pages [16] -->
● In all of our models, we consider that sending and receiving a message have the same effect for our analysis,

<!-- b001256 | prose | pages [16] -->
which means the network graph is deem to be a

<!-- b001257 | prose | pages [16] -->
rected graph. But in fact, this assumption may have certain irrationality in some

<!-- b001258 | prose | pages [16] -->
undi

<!-- b001259 | prose | pages [16] -->
cases. So a certain modifications about the issue can be made to improve our models through further analysis

<!-- b001260 | prose | pages [16] -->
in our future work. ● When analyzing messages exchanges in our models, we actually only focus on

<!-- b001261 | prose | pages [16] -->
5 topics of the messages into account. More precisely, only two kinds of topics,

<!-- b001262 | prose | pages [16] -->
the 1

<!-- b001263 | prose | pages [16] -->
suspicious and unsuspicious, are we taking into account while modeling. And it is better if we have more detailed classification about the t

<!-- b001264 | prose | pages [16] -->
opics. Moreover, if we can get

<!-- b001265 | prose | pages [16] -->
pecific content of these messages, we can collect more information by identify if

<!-- b001266 | prose | pages [16] -->
the s

<!-- b001267 | prose | pages [16] -->
anyone is involved in the message content so that we can enhance our models.

<!-- b001268 | furniture | pages [16] -->


<!-- b001269 | heading | pages [16] -->
Further discussion

<!-- b001270 | prose | pages [16] -->
Text and semantic network analysis

<!-- b001271 | prose | pages [16] -->
Text

<!-- b001272 | prose | pages [16] -->
analysis

<!-- b001273 | furniture | pages [17] -->
Team # 13215                                                                                                             Page      of  18

<!-- b001274 | furniture | pages [17] -->
16

<!-- b001275 | prose | pages [17] -->
Text analysis is the analysis of text taking advantage of algorithmic techniques and usually be divided into three kinds according to algorithmic–exploratory spectrum: Concording, Content analysis, Statistical analysis.

<!-- b001276 | prose | pages [17] -->
Semantic network analysis

<!-- b001277 | prose | pages [17] -->
Semantic network analysis is both a research method and a theoretical framework, which focuses on the structure of a system based on shared meaning as well as cognitive processes. It requires a content analysis of textual data to determine the most frequently used symbols previously.

<!-- b001278 | prose | pages [17] -->
Apply Text and Semantic network analysis to crime case, here’s some procedure w e should taken: (1) Keywords mining

<!-- b001279 | prose | pages [17] -->
We use some mathematical methods or

<!-- b001280 | prose | pages [17] -->
computer technique to achieve keywords

<!-- b001281 | prose | pages [17] -->
mining in the text database, like Frequency Sta

<!-- b001282 | prose | pages [17] -->
tistics, Association Rule Analysis and Data Mining. The processing flow is as follows:

<!-- b001283 | prose | pages [17] -->
Step 1: Mining the high-frequency keywords

<!-- b001284 | prose | pages [17] -->
essage or text and consider

<!-- b001285 | prose | pages [17] -->
We perform the frequency Statistics of keywords in the m

<!-- b001286 | prose | pages [17] -->
cy keywords as High-frequency Keywords. Take supervior’s simply

<!-- b001287 | prose | pages [17] -->
the high frequen

<!-- b001288 | prose | pages [17] -->
case

<!-- b001289 | prose | pages [17] -->
as an example, the frequency of “budget” is 7/ 28 , “late” is 6/ 28 and “stress is 5/28 . Step 2: Identify Suspicious Keywords preliminarily

<!-- b001290 | prose | pages [17] -->
n of the conspiracy. Indentify its content or topics.

<!-- b001291 | prose | pages [17] -->
Study the implementatio Finish the classification of the High-frequency keywords and find out Suspicious Keywords.

<!-- b001292 | prose | pages [17] -->
However, it is defective to consider a message with only one Suspicious Keywords as a Suspicious Message, because some Suspicious Keywords may usually exit in the normal business, such as “budget” in the cases of economic crime. Step 3: Mining the new Suspicious Keywords:

<!-- b001293 | prose | pages [17] -->
iation Rule Analysis to mining the new Suspicious Keywords

<!-- b001294 | prose | pages [17] -->
We can use Assoc using the known Suspicious Keywords. If some word combinations’ support and confidence are bigger than the minimum support and minimum confidence we give and they contain a known Suspicious Keywords, we can successfully to mining out t e h ne Suspicious Keywords.

<!-- b001295 | prose | pages [17] -->
w (2) The classification of topics:

<!-- b001296 | prose | pages [17] -->
The keywords and their combinations can determine a topic. Besides, the suspicious messages depend on the classification of topics. It is more reliable to consider a message containing two or more Suspicious Keywords as a Suspicious ssa e. Thus, some non-conspirators can avoid fal Me g

<!-- b001297 | prose | pages [17] -->
sely being accused. In the current

<!-- b001298 | prose | pages [17] -->
a e, a non-conspirator Paige sent 4 suspicious messages. It shows that there are some

<!-- b001299 | prose | pages [17] -->
c s

<!-- b001300 | prose | pages [17] -->
defects in the topic classification of the messages.

<!-- b001301 | prose | pages [17] -->
On the other hand, criminal activities sometimes may be found and suspected. In the communication messages, someone who questions them is likely to be a non-conspirator. For example in the case of Investigation EZ, Anne questioned Bob’s tardiness, Harry questioned George' s stress and Harry question the status of budget. I n fact they are all non-conspirators.

<!-- b001302 | prose | pages [17] -->
, (3) Categorize social group

<!-- b001303 | prose | pages [17] -->
Look out names occurring on the message whose owners don’t contact directly. However these people have some relationship with both contacts. We can analyze emotional relationship from semantic and other aspects from similarity of characters in life as well work, then make sure their closeness so that we can categorize social

<!-- b001304 | furniture | pages [18] -->
Team # 13215                                                                                                             Page      of  18

<!-- b001305 | prose | pages [18] -->
group.

<!-- b001306 | furniture | pages [18] -->
17

<!-- b001307 | prose | pages [18] -->
As for the case, we semantic analyze social relationship, and indicate

<!-- b001308 | prose | pages [18] -->
Table 6

<!-- b001309 | prose | pages [18] -->
Close relationship content

<!-- b001310 | prose | pages [18] -->
Quarrel for Bob’ tardiness

<!-- b001311 | prose | pages [18] -->
Operation and interactive argue

<!-- b001312 | prose | pages [18] -->
Distant relationship

<!-- b001313 | furniture | pages [18] -->


<!-- b001314 | furniture | pages [18] -->


<!-- b001315 | prose | pages [18] -->
Anne、Bob

<!-- b001316 | furniture | pages [18] -->


<!-- b001317 | prose | pages [18] -->
Bob、Dave、George

<!-- b001318 | prose | pages [18] -->
Similar character of stress and tired

<!-- b001319 | furniture | pages [18] -->


<!-- b001320 | prose | pages [18] -->
Inez、George

<!-- b001321 | prose | pages [18] -->
Misunderstanding and suspicion

<!-- b001322 | prose | pages [18] -->
Cooperation and trust

<!-- b001323 | furniture | pages [18] -->


<!-- b001324 | furniture | pages [18] -->


<!-- b001325 | prose | pages [18] -->
Harry、George

<!-- b001326 | furniture | pages [18] -->


<!-- b001327 | prose | pages [18] -->
Anne、Carol

<!-- b001328 | furniture | pages [18] -->


<!-- b001329 | prose | pages [18] -->
ure. 9  The expand d relationship network

<!-- b001330 | prose | pages [18] -->
Fig e e epresent known c In the Figure 9 ,red r

<!-- b001331 | prose | pages [18] -->
ounds r

<!-- b001332 | prose | pages [18] -->
Suspicious Message co

<!-- b001333 | prose | pages [18] -->
mmunicat

<!-- b001334 | prose | pages [18] -->
ion;

<!-- b001335 | prose | pages [18] -->
onspirators and som one with the

<!-- b001336 | prose | pages [18] -->
e blue

<!-- b001337 | prose | pages [18] -->
rounds represent the known non-conspirators; red solid lines represent suspicious messages; dotted lines with different colors represent different clos relationship.

<!-- b001338 | prose | pages [18] -->
e relationship; crosse

<!-- b001339 | prose | pages [18] -->
s represent distant

<!-- b001340 | prose | pages [18] -->
As the Figure 9 shows, the expanded rela

<!-- b001341 | prose | pages [18] -->
by the actual case result.

<!-- b001342 | furniture | pages [18] -->


<!-- b001343 | furniture | pages [18] -->


<!-- b001344 | prose | pages [18] -->
Based on step

<!-- b001345 | prose | pages [18] -->
tionship network can be well explained

<!-- b001346 | prose | pages [18] -->
am could be written

<!-- b001347 | prose | pages [18] -->
-by-step procedure we introduce above, a progr

<!-- b001348 | prose | pages [18] -->
to analyze me d be figured out.

<!-- b001349 | prose | pages [18] -->
ssage traffic and the main idea of each traffic coul

<!-- b001350 | prose | pages [18] -->
sis can help us with large data sets ea

<!-- b001351 | prose | pages [18] -->
Semantic and text analy sily. Thus, even several

<!-- b001352 | prose | pages [18] -->
ssages need to be analyzed, we also can take advantage o

<!-- b001353 | prose | pages [18] -->
million me techniques and ma f these two

<!-- b001354 | prose | pages [18] -->
ke categorization for message traffic.

<!-- b001355 | furniture | pages [18] -->


<!-- b001356 | heading | pages [18] -->
Model application in other disciplines

<!-- b001357 | prose | pages [18] -->
In this paper, the case are actually not

<!-- b001358 | prose | pages [18] -->
models we establish for this specific crime

<!-- b001359 | prose | pages [18] -->
restri

<!-- b001360 | prose | pages [18] -->
cted to solve this kind of problem. A lot of knowledge and techniques we use in these models, such as probability theory, iterative algorithm, graph theory and so on, are widely applied in many different disciplines and domains. And the models we build are also particular suitable for analyze network database of many types to

<!-- b001361 | prose | pages [18] -->
oritize some nodes with some specific characteristic.

<!-- b001362 | prose | pages [18] -->
identify and pri

<!-- b001363 | prose | pages [18] -->
For example, identification of infected or diseased cells in cell network is one of

<!-- b001364 | prose | pages [18] -->
s. The probability of one cell’s being infected is much

<!-- b001365 | prose | pages [18] -->
the hot topics in biological term

<!-- b001366 | prose | pages [18] -->
like the probability of one office worker’s being conspirator in our Model 2. That is to say,

<!-- b001367 | prose | pages [18] -->
whether a cell’s being infected or not is connected to the situation of those cells directly around it. Through modern medical imaging technology and other medical

<!-- b001368 | furniture | pages [19] -->
Team # 13215                                                                                                             Page      of  18

<!-- b001369 | furniture | pages [19] -->
18

<!-- b001370 | prose | pages [19] -->
laboratory technologies, we can get the similar data as that we got in this crime case, such as how many and where are the cells infected already. Thus we can apply our model to calculate the infected probability of other cells

<!-- b001371 | prose | pages [19] -->
e

<!-- b001372 | prose | pages [19] -->
som model setting.

<!-- b001373 | prose | pages [19] -->
of unknown state by modify

<!-- b001374 | prose | pages [19] -->
In all, concept like “node” we use in our models

<!-- b001375 | prose | pages [19] -->
can be materialized to lots of

<!-- b001376 | prose | pages [19] -->
specific entities in reality, and then our models can be p

<!-- b001377 | prose | pages [19] -->
roperly altered, improved and

<!-- b001378 | prose | pages [19] -->
ted to solve a lot of practical problem but not just in criminology and biology.

<!-- b001379 | prose | pages [19] -->
adop

<!-- b001380 | furniture | pages [19] -->


<!-- b001381 | prose | pages [19] -->
Reference

<!-- b001382 | prose | pages [19] -->
Sridhar Ramamoorti. 2008.The Psychology and Sociology of Fraud:

<!-- b001383 | prose | pages [19] -->
Integrating the Behavioral Sciences Component Into Fraud and

<!-- b001384 | prose | pages [19] -->
Forensic Accounting Curricula. Issues in Accounting Education

<!-- b001385 | prose | pages [19] -->
(November): pp. 521–533

<!-- b001386 | prose | pages [19] -->
Zhigang Lin. 2010.psychology analysis of corruption and bribery crime.

<!-- b001387 | prose | pages [19] -->
Huaihaiwenhui(Chinese Journal)(03)

<!-- b001388 | prose | pages [19] -->
Zwillinger, D, Kokoska, S. 2000. CRC Standard Probability and Statistics

<!-- b001389 | prose | pages [19] -->
Tables and Formulae, CRC Press

<!-- b001390 | prose | pages [19] -->
Shuhe Wang. 1990.Graph theory and algorithm.Hefei,China:Press of

<!-- b001391 | prose | pages [19] -->
nce and Technology of China

<!-- b001392 | prose | pages [19] -->
University of Scie

<!-- b001393 | prose | pages [19] -->
Yuan. 2011.Social network analysis of crime

<!-- b001394 | prose | pages [19] -->
Peng Chen,Hongyong

<!-- b001395 | prose | pages [19] -->
organization structures.J Tsinghua Univ(Sci &Tech)51(8):1097-1

<!-- b001396 | prose | pages [19] -->
101

<!-- b001397 | prose | pages [19] -->
man L C. 1979.Centrality in social networks: Conceptual clarificati

<!-- b001398 | prose | pages [19] -->
Free

<!-- b001399 | prose | pages [19] -->
Social Networks(1):215-239

<!-- b001400 | prose | pages [19] -->
on.

<!-- b001401 | prose | pages [19] -->
oduction. Meth

<!-- b001402 | prose | pages [19] -->
od in text-analysis: An intr

<!-- b001403 | prose | pages [19] -->
h

<!-- b001404 | prose | pages [19] -->
http://www.cch.kcl.ac.uk/legacy/teaching/av1000/textanalysis/met

<!-- b001405 | prose | pages [19] -->
o

<!-- b001406 | prose | pages [19] -->
d.html

<!-- b001407 | prose | pages [19] -->
Marya L.Doerfel.1999.A Semantic Network Analysis of the International

<!-- b001408 | prose | pages [19] -->
Communication Association.Hum

<!-- b001409 | prose | pages [19] -->
an Communication Reseach(June)

<!-- b001410 | prose | pages [19] -->
Chang’an Yuan.2009.Data Mining Theory and Application of SPSS

<!-- b001411 | prose | pages [19] -->
Clemetine.Publishing House of Electronics Indu

<!-- b001412 | furniture | pages [19] -->


<!-- b001413 | prose | pages [19] -->
stry
