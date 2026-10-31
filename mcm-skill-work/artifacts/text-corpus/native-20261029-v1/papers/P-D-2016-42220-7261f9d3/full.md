# P-D-2016-42220-7261f9d3

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
For office use only

<!-- b000006 | prose | pages [1] -->
For office use only

<!-- b000007 | prose | pages [1] -->
42220

<!-- b000008 | prose | pages [1] -->
T1 ________________

<!-- b000009 | prose | pages [1] -->
T2 ________________

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F1 ________________

<!-- b000013 | prose | pages [1] -->
F2 ________________

<!-- b000014 | prose | pages [1] -->
F3 ________________

<!-- b000015 | prose | pages [1] -->
Problem Chosen

<!-- b000016 | prose | pages [1] -->
T4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | prose | pages [1] -->
F4 ________________

<!-- b000019 | prose | pages [1] -->
D D

<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | prose | pages [1] -->
2016

<!-- b000022 | prose | pages [1] -->
MCM/ICM

<!-- b000023 | heading | pages [1] -->
Summary Sheet

<!-- b000024 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.)

<!-- b000025 | prose | pages [1] -->
Analysis of Society’s Information Networks

<!-- b000026 | prose | pages [1] -->
With the development of technology, the situation of information flow becomes more complicated which has aroused widely concerns. In this paper, we establish a double-layer complex network model to measure the evolution and influence in society’s information networks.

<!-- b000027 | prose | pages [1] -->
In our double-layered complex network model, the inner layer is to analyze the situation of the information flow among a region. We specially take several factors such as inherent value of information, the media effect and personal subjective emotions into account to quantify the attributes of node and side. Optimizing the AsIC Model, we establish point to point model to simulate the flow of information in the network. In the outer layer, Based on the Reaction-Diffusion Model, we establish a global network model to correct the formulas of propagation probability and propagation delay by taking the distance factor into consideration.

<!-- b000028 | prose | pages [1] -->
Based on our constructed model, with the combination of the inherent value of the information and the efficiency of information flow, we first give out the method of qualifying news. According to the different condition of media usage, we obtain the proportion of different media in different areas based on regression analysis. Compared the simulation of propagation ratio in our network with the actual market share of a certain media, we find that the relative error is less than 10%. Based on our collecting data, we predict that the propagation probability will increase rapidly while the propagation delay will decrease around the year 2050. Meanwhile, the significance of inherent value of information will depress.

<!-- b000029 | prose | pages [1] -->
Later, based on Bounded Confidence Model, we establish an interaction model to analyze factors which influence the public interest and opinion through information networks. As a result, we get distribution function of public opinion to observe the change of public opinion. Through a piece of specific information, we find the public opinion changes rapidly in the beginning and finally into the stable state. Next, we analyze the influence of several factors in spreading information and public opinion. We get diagram after calculation to show the trend. For example, the propagation probability and change rate of opinion are proportional to information value while propagation delay is opposite.

<!-- b000030 | prose | pages [1] -->
Meanwhile, we adopt sensitivity analysis on different elements. We conclude that the model is more sensitive to Authority, later comes Influence, Activity and Willing.

<!-- b000031 | furniture | pages [1] -->


<!-- b000032 | keywords | pages [1] -->
Key words: double-layer complex network model, point to point model, Bounded Confidence Model, information flow

<!-- b000033 | furniture | pages [2] -->
Page 1 of 20

<!-- b000034 | furniture | pages [2] -->
Team #42220

<!-- b000035 | prose | pages [2] -->
1. Introduction ................................................................................................................................... 2 1.1 Background ......................................................................................................................... 2 1.2 Our work ............................................................................................................................. 2 2. Assumptions .................................................................................................................................. 2 3. Task 1: Establish a Double-layer Complex Network .................................................................... 3 3.1 Frame .................................................................................................................................. 3 3.2 Inner Layer:Information Flow over a Region ..................................................................... 4 3.2.1 Index Extraction ....................................................................................................... 4 3.2.2 Information flow between two nodes ....................................................................... 7 3.2.3 Coefficient calculation ............................................................................................. 7 3.3 Outer Layer: Information Flow from Region to Region ..................................................... 8 3.4 Information Flow Situation ............................................................................................... 10 3.5 Sensitivity Analysis ........................................................................................................... 11 3.5.1 Change the Value of Index ..................................................................................... 11 3.5.2 Remove a Index...................................................................................................... 12 4. Application and Analysis ............................................................................................................ 12 4.1 Task 1:Qualification of News ............................................................................................ 12 4.2 Task 2:Predict the Information Communication Situation for Today ............................... 13 4.3 Task 3:Predict the situation around the year 2050 ............................................................. 15 4.3.1 Communication networks’ relationships ................................................................ 15 4.3.2 Communication networks’ capacities ..................................................................... 15 4.4 Task 4:Influence in Public Interest and Opinion ............................................................... 16 4.4.1 Foundation of Model .............................................................................................. 16 4.4.2 Suggestions ............................................................................................................ 17 4.5 Task 5:Factors Influence in Spreading Information and Public Opinion .......................... 18 4.5.1 Influence in Spreading Information ....................................................................... 18 4.5.2 Influence in Public Opinion ................................................................................... 18 5. Strengths and Weaknesses ........................................................................................................... 19 5.1 Strengths ............................................................................................................................ 19 5.2 Weaknesses ....................................................................................................................... 19 Reference ........................................................................................................................................ 19

<!-- b000036 | furniture | pages [2] -->


<!-- b000037 | furniture | pages [2] -->


<!-- b000038 | furniture | pages [2] -->


<!-- b000039 | furniture | pages [2] -->


<!-- b000040 | furniture | pages [2] -->


<!-- b000041 | furniture | pages [2] -->


<!-- b000042 | furniture | pages [2] -->


<!-- b000043 | furniture | pages [2] -->


<!-- b000044 | furniture | pages [2] -->


<!-- b000045 | furniture | pages [2] -->


<!-- b000046 | furniture | pages [3] -->
Page 2 of 20

<!-- b000047 | furniture | pages [3] -->
Team #42220

<!-- b000048 | heading | pages [3] -->
1. Introduction

<!-- b000049 | heading | pages [3] -->
1.1 Background

<!-- b000050 | prose | pages [3] -->
Nowadays, information is spread quickly in our daily life. Due to the development of technology, no matter the big events or the trivia, people have access to information quickly and conveniently. As a result, the information garbage is everywhere which influences our life. In order to manage and track the flow of information, people raise awareness of the importance of establishing a society information network.

<!-- b000051 | prose | pages [3] -->
Interested in information communication situation of social network, several methods have been adopted to describe it. Most models supposed that information is spread according to time sequence. For example, Independent Cascade Model[1] regards that propagation probability is same among nodes all the time which has no memory. Meanwhile, Linear threshold model[2] concentrates on cumulative probability which reflects the accepted ability of receiver. However, these models ignore such factors:

<!-- b000052 | prose | pages [3] -->
 Attributes of nodes such as personal interests.  Influence of inherent value of information in propagation.  Propagation process is not synchronous.

<!-- b000053 | prose | pages [3] -->
Therefore, there is an urgent need for a complete scientific model. Based on it, we establish a double-layer complex network.

<!-- b000054 | heading | pages [3] -->
1.2 Our work

<!-- b000055 | prose | pages [3] -->
To further present our solutions, we arrange our paper as follow.

<!-- b000056 | prose | pages [3] -->
 In section 2, we give out the reliable assumptions to simplify the model.  In section 3, the double-layer network is constructed to analyze and forecast the information flow. The inner layer analyzes the information flow among a region. While the outer layer analyze the flow from region to region. Meanwhile, the sensitivity analysis is given out to validate our model.  In section 4, we apply our model to solve a series of problem, such as qualification of news, prediction of information flow today and around the year 2050. Next, we establish a model to analyze the factors to influence the public interest and opinion. Later, we analyze the influence of different indexes in Spreading Information and Public Opinion.  At last, we discuss the strengths and weaknesses of our model in detail.

<!-- b000057 | heading | pages [3] -->
2. Assumptions

<!-- b000058 | prose | pages [3] -->
 The data we found is authentic and reliable.  No invention of media in the time for prediction. That is to say, people use the same media as today, just the proportion of media changes.  Ignore the firewall among countries which restrains the spread of information. The

<!-- b000059 | furniture | pages [3] -->


<!-- b000060 | furniture | pages [4] -->
Page 3 of 20

<!-- b000061 | furniture | pages [4] -->
Team #42220

<!-- b000062 | prose | pages [4] -->
information in the our network is not secret.  Due to the difference of development level is relatively little in a small area, we ignore the difference in media usage from a statistical point of view.  To simplify the model, we only consider six media to spread information which are newspaper, telegraph, radio, television, the Internet and mobile phone.  The node spread the same message only once. That is to say，the in-degree of a node is no more than 1.

<!-- b000063 | heading | pages [4] -->
3. Task 1: Establish a Double-layer Complex Network

<!-- b000064 | heading | pages [4] -->
3.1 Frame

<!-- b000065 | prose | pages [4] -->
A large amount of factors ought to take into account to quantify the flow of information. For example, due to the difference in development level among countries, the way and speed of flow must be different. Also, with the Internet technology become more sophisticated, each person plays a more and more important role in spreading information instead of original media such as newspaper and television, which the objective factors such as personal interests should be taken into consideration.

<!-- b000066 | prose | pages [4] -->
Based on above analysis, we can see that a simple network cannot reflect the whole situation of the flow of information well. As a result, a complex network with multi-layers, whose layers have a certain interactions and independence, seems to be more reasonable.

<!-- b000067 | prose | pages [4] -->
Therefore, we come up with a double-layered network, global information network and point to point information network, which belongs to a complex network, to reflect the information flow more specifically.

<!-- b000068 | prose | pages [4] -->
The structure of our double-layer complex network is shown in Figure 1.

<!-- b000069 | furniture | pages [4] -->


<!-- b000070 | caption | pages [4] -->
Figure 1 A double-layer Network

<!-- b000071 | prose | pages [4] -->
The blue dots represent each person and small circle represents a region. The directed line represents the direction of information flow. The figure vividly indicates that the information originates from a node(source), then spread quickly over a region and at last spread the whole world. The internal and external factors which influence the information flow is analyzed in detail in next two sections.

<!-- b000072 | furniture | pages [4] -->


<!-- b000073 | furniture | pages [5] -->
Page 4 of 20

<!-- b000074 | furniture | pages [5] -->
Team #42220

<!-- b000075 | heading | pages [5] -->
3.2 Inner Layer: Information Flow over a Region

<!-- b000076 | prose | pages [5] -->
The process of information propagation can be divided into massive point to point cases. Each case has three entities: sender(S), receiver(R) and content(C). Figure 2 shows the relationship.

<!-- b000077 | furniture | pages [5] -->


<!-- b000078 | caption | pages [5] -->
Figure 2 Relationships of three entities in the diffusion process

<!-- b000079 | prose | pages [5] -->
The information spread from sender to receiver, each spread case carries a piece of information.

<!-- b000080 | heading | pages [5] -->
3.2.1 Index Extraction

<!-- b000081 | prose | pages [5] -->
In order to describe the flow of information specifically, we choose Twitter as an example. Based on the AsIC Model, to improve the accuracy of our model, we take the inherent value of information, the media effect and personal subjective emotions into consideration and give five indexes to analyze the information flow: Communication Media Effect, Sender Characteristic, Receiver Characteristic, Content Characteristic, Relation between Sender and Receiver. Suppose that node u as a sender, node v as a receiver.

<!-- b000082 | prose | pages [5] -->
)  Communication Media Characteristic ( m m

<!-- b000083 | prose | pages [5] -->
From a historical perspective, the communication media change a lot. From newspaper, and radio in the early time to television, Internet, mobile phone and many other media nowadays. Information tends to spread more quickly and wide. Due to the difference in social developments, mainstream media of different regions varies a lot. Based on six media (newspaper, telegraph, radio, television, Internet and mobile phone), communication medium

<!-- b000084 | prose | pages [5] -->
is calculated as follows: effect m

<!-- b000085 | prose | pages [5] -->
  

<!-- b000086 | prose | pages [5] -->
( i

<!-- b000087 | prose | pages [5] -->
m i i

<!-- b000088 | prose | pages [5] -->
i

<!-- b000089 | prose | pages [5] -->
 

<!-- b000090 | prose | pages [5] -->
N , TEL , R , TV , I , M )

<!-- b000091 | prose | pages [5] -->
(1)

<!-- b000092 | prose | pages [5] -->
When N,TEL,R,TV,I is short for six media, newspaper, telegraph, radio, television the

<!-- b000093 | prose | pages [5] -->
idenotes the market share of ith medium Internet and mobile phone respectively; where

<!-- b000094 | prose | pages [5] -->
idenotes corresponding effect on spreading communication such as propagation speed and

<!-- b000095 | prose | pages [5] -->
and scope.

<!-- b000096 | prose | pages [5] -->
Base on the Analytic Hierarchy Process[3], we train the collected data and obtain the final weights as follows. The result has been approximated in order to simplify calculation.

<!-- b000097 | furniture | pages [5] -->


<!-- b000098 | furniture | pages [6] -->
Page 5 of 20

<!-- b000099 | furniture | pages [6] -->
Team #42220

<!-- b000100 | prose | pages [6] -->
Meanwhile, in a specific area we assume that iand  is constant which represent the m

<!-- b000101 | prose | pages [6] -->
average level. The weight of different media is listed in Table 1.

<!-- b000102 | caption | pages [6] -->
Table 1 Different media and their effect on spreading communication

<!-- b000103 | prose | pages [6] -->
Medium Weight Newspaper 1 Telegraphy 0.5 Radio 2

<!-- b000104 | furniture | pages [6] -->


<!-- b000105 | prose | pages [6] -->
s)  Sender Characteristic (

<!-- b000106 | prose | pages [6] -->


<!-- b000107 | prose | pages [6] -->
Medium Weight Television 2.5 Internet 3 Mobile phone 3.5

<!-- b000108 | prose | pages [6] -->
Influence(F): Influence shows the importance degree of a node. It should be:

<!-- b000109 | prose | pages [6] -->
InF   ( ( u u ) ) lg( RT )1 (2)

<!-- b000110 | prose | pages [6] -->
Where RT denotes the total number of forwarding times of a node.  Authority(A): It is defined as the ratio of in-degree divides out-degree which is calculated as follows:

<!-- b000111 | prose | pages [6] -->
A FO   (u) lg( )1 (3) FR

<!-- b000112 | prose | pages [6] -->
Where FO denotes the number of fans while FR denotes the number of idol.  Activity(Ac):

<!-- b000113 | prose | pages [6] -->
Ac PO   ( ( u u ) lg( )1 (4) D

<!-- b000114 | prose | pages [6] -->
Where PO denotes total number of messages the user has been published. D denotes the number of the user’s active days.

<!-- b000115 | prose | pages [6] -->
We take normalized form membership functions for each index so that values of all the factors can be constrained between 0 and 1.The normalization is shown as follows:

<!-- b000116 | prose | pages [6] -->


<!-- b000117 | prose | pages [6] -->
'

<!-- b000118 | prose | pages [6] -->
x

<!-- b000119 | prose | pages [6] -->
i

<!-- b000120 | prose | pages [6] -->
max

<!-- b000121 | prose | pages [6] -->
 

<!-- b000122 | prose | pages [6] -->
1

<!-- b000123 | prose | pages [6] -->
j

<!-- b000124 | prose | pages [6] -->
' ix and

<!-- b000125 | prose | pages [6] -->


<!-- b000126 | prose | pages [6] -->
x x

<!-- b000127 | prose | pages [6] -->
min {

<!-- b000128 | prose | pages [6] -->
x

<!-- b000129 | prose | pages [6] -->
}

<!-- b000130 | prose | pages [6] -->
i i j

<!-- b000131 | prose | pages [6] -->
 

<!-- b000132 | prose | pages [6] -->
1

<!-- b000133 | prose | pages [6] -->
j n

<!-- b000134 | prose | pages [6] -->
(5)

<!-- b000135 | prose | pages [6] -->


<!-- b000136 | prose | pages [6] -->
{ {

<!-- b000137 | prose | pages [6] -->
x x

<!-- b000138 | prose | pages [6] -->
} min {

<!-- b000139 | prose | pages [6] -->
x

<!-- b000140 | prose | pages [6] -->
}

<!-- b000141 | prose | pages [6] -->
j j

<!-- b000142 | prose | pages [6] -->
 

<!-- b000143 | prose | pages [6] -->
1

<!-- b000144 | prose | pages [6] -->
j n n n

<!-- b000145 | prose | pages [6] -->
ix respectively denotes the original value and the value after standar-

<!-- b000146 | prose | pages [6] -->
Where

<!-- b000147 | prose | pages [6] -->
dization.

<!-- b000148 | prose | pages [6] -->
)  Receiver Characteristic( R

<!-- b000149 | prose | pages [6] -->
 Willing(W): The value of willing indicates the possible trend for receivers to spr- ead the information(v) is calculated as follows:

<!-- b000150 | prose | pages [6] -->
R   W W ( v ) lg( )1 (6) P

<!-- b000151 | prose | pages [6] -->
Where R denotes the number of retweet times. P denotes the number of original messages.

<!-- b000152 | prose | pages [6] -->
In the same way, normalize the index as

<!-- b000153 | furniture | pages [6] -->


<!-- b000154 | prose | pages [6] -->
, , iy .

<!-- b000155 | furniture | pages [7] -->
Page 6 of 20

<!-- b000156 | furniture | pages [7] -->
Team #42220

<!-- b000157 | prose | pages [7] -->
c)  Content Characteristic (

<!-- b000158 | prose | pages [7] -->
Inherent value of content plays an important role in the information flow. For example, the funnier or more important message tends to spread more quickly. To evaluate such abstract idea, we quantify it for two aspects: the value of information content and the quality of presentation.

<!-- b000159 | prose | pages [7] -->
Luckily, the article in Journal of Information Engineering University[4] determines 5 indicators for the value of information content and 5 indicators for the quality of presentation. Specific indexes and their weights are shown in Table 2.

<!-- b000160 | caption | pages [7] -->
Table 2 Evaluation indexes and their weights

<!-- b000161 | prose | pages [7] -->
Specific indicator General  indicator Weight

<!-- b000162 | prose | pages [7] -->
Authenticity 0.318 Importance 0.174 Timeliness

<!-- b000163 | prose | pages [7] -->
Inherent value(0.7)

<!-- b000164 | prose | pages [7] -->
0.247 Target 0.102 Confidentiality 0.159

<!-- b000165 | prose | pages [7] -->
Clear scheme 0.203 Careful thinking 0.063 Accurate description

<!-- b000166 | prose | pages [7] -->
Quality of presentation(0.3)

<!-- b000167 | prose | pages [7] -->
0.299 Concise expression 0.232 Comprehensive factors

<!-- b000168 | furniture | pages [7] -->


<!-- b000169 | prose | pages [7] -->
0.203

<!-- b000170 | prose | pages [7] -->
We give out general formulas to calculate the above two aspects below:

<!-- b000171 | prose | pages [7] -->
 value

<!-- b000172 | prose | pages [7] -->
 qua

<!-- b000173 | prose | pages [7] -->
  7.0 c

<!-- b000174 | prose | pages [7] -->


<!-- b000175 | prose | pages [7] -->
5

<!-- b000176 | prose | pages [7] -->
 

<!-- b000177 | prose | pages [7] -->
  (7) i i i 1

<!-- b000178 | prose | pages [7] -->


<!-- b000179 | prose | pages [7] -->
10

<!-- b000180 | prose | pages [7] -->
 

<!-- b000181 | prose | pages [7] -->
  (8) i i i 6

<!-- b000182 | prose | pages [7] -->
      3.0 (9) value qua

<!-- b000183 | prose | pages [7] -->
denotes the weight of above 10 indicators respectively. Where i i denotes the value

<!-- b000184 | prose | pages [7] -->
 of the corresponding index, which arranges from 0 to 9.

<!-- b000185 | prose | pages [7] -->


<!-- b000186 | prose | pages [7] -->
denotes the value of value

<!-- b000187 | prose | pages [7] -->
denotes the quality of presentation. information content and pre

<!-- b000188 | prose | pages [7] -->
  Relation between Sender and Receiver (

<!-- b000189 | prose | pages [7] -->


<!-- b000190 | prose | pages [7] -->
) S, S, R R

<!-- b000191 | prose | pages [7] -->
Interest similarity(Si): The message the user published indicates his or her interests which plays an important role in spreading information. TF-IDF model[5] is adopted to information retrieval and data mining. Sim-i(u,v) is:

<!-- b000192 | prose | pages [7] -->
Si

<!-- b000193 | prose | pages [7] -->
( 

<!-- b000194 | prose | pages [7] -->
P Q

<!-- b000195 | prose | pages [7] -->


<!-- b000196 | prose | pages [7] -->
u u

<!-- b000197 | prose | pages [7] -->
, ,

<!-- b000198 | prose | pages [7] -->
v

<!-- b000199 | prose | pages [7] -->
) (10)

<!-- b000200 | prose | pages [7] -->


<!-- b000201 | prose | pages [7] -->
P Q

<!-- b000202 | prose | pages [7] -->
where P and Q respectively file vector of uses u and v.  Structural similarity(Ss):It illustrates the similarity of circle of friends among users. The Jaccard Distance[6] is applied to the calculation:

<!-- b000203 | furniture | pages [7] -->


<!-- b000204 | furniture | pages [8] -->
Page 7 of 20

<!-- b000205 | furniture | pages [8] -->
Team #42220

<!-- b000206 | prose | pages [8] -->
Ss

<!-- b000207 | prose | pages [8] -->
(

<!-- b000208 | prose | pages [8] -->
u

<!-- b000209 | prose | pages [8] -->
,

<!-- b000210 | prose | pages [8] -->
v

<!-- b000211 | prose | pages [8] -->
)

<!-- b000212 | furniture | pages [8] -->


<!-- b000213 | prose | pages [8] -->
N ( iv )

<!-- b000214 | prose | pages [8] -->
 N

<!-- b000215 | prose | pages [8] -->
(

<!-- b000216 | prose | pages [8] -->
u

<!-- b000217 | prose | pages [8] -->
)

<!-- b000218 | prose | pages [8] -->
N

<!-- b000219 | prose | pages [8] -->
(

<!-- b000220 | prose | pages [8] -->
v

<!-- b000221 | prose | pages [8] -->
)

<!-- b000222 | prose | pages [8] -->
  (11) 

<!-- b000223 | prose | pages [8] -->
N

<!-- b000224 | prose | pages [8] -->
(

<!-- b000225 | prose | pages [8] -->
u

<!-- b000226 | prose | pages [8] -->
)

<!-- b000227 | prose | pages [8] -->
N

<!-- b000228 | prose | pages [8] -->
(

<!-- b000229 | prose | pages [8] -->
v

<!-- b000230 | prose | pages [8] -->
)

<!-- b000231 | prose | pages [8] -->
iv . denotes the neighboring nodes of node Where

<!-- b000232 | prose | pages [8] -->
CL ( u , v )  ):When the message contains information of receiver, it will be Closeness(

<!-- b000233 | prose | pages [8] -->
CL ( u , v ) as follows: spread more easily. Define

<!-- b000234 | prose | pages [8] -->


<!-- b000235 | prose | pages [8] -->
,1 when the

<!-- b000236 | prose | pages [8] -->


<!-- b000237 | prose | pages [8] -->
CL ( u , v )

<!-- b000238 | prose | pages [8] -->


<!-- b000239 | prose | pages [8] -->
,0

<!-- b000240 | prose | pages [8] -->
on the 

<!-- b000241 | heading | pages [8] -->
3.2.2 Information flow between two nodes

<!-- b000242 | prose | pages [8] -->
message of u mentions v (12)

<!-- b000243 | prose | pages [8] -->
contrary

<!-- b000244 | prose | pages [8] -->
) and side vector Based on above analysis, we establish eigenvector of node vector (

<!-- b000245 | prose | pages [8] -->
e) .These two vectors are shown as follows: (

<!-- b000246 | prose | pages [8] -->


<!-- b000247 | prose | pages [8] -->
  n S

<!-- b000248 | prose | pages [8] -->
n

<!-- b000249 | prose | pages [8] -->


<!-- b000250 | prose | pages [8] -->
T   (13) R C

<!-- b000251 | prose | pages [8] -->
  (14) e e S , R To obtain the propagation probability, fundamentally function is calculated as follows:

<!-- b000252 | prose | pages [8] -->
 f ( u , v , c )        T T k k (15) 1 m 1 n 2 e

<!-- b000253 | prose | pages [8] -->
denotes weight of nodes’ characteristic, is a constant, Where 1 m denotes weight 2 of sides’ characteristic. The weight represents how corresponding characteristic influence in 1k is the weight. propagation probability.

<!-- b000254 | prose | pages [8] -->
Based on Bayesian logistic function[7],the propagation probability is calculated:

<!-- b000255 | prose | pages [8] -->
p ( u , v , c ) 1   (16)   1 In ( f ( u , v , c ))

<!-- b000256 | prose | pages [8] -->
In the same way, propagation delay is calculated as follows:

<!-- b000257 | prose | pages [8] -->
 ( u , v , c )          T T k (17) 2 m 1 n 2 e

<!-- b000258 | prose | pages [8] -->
respectively denotes weight of nodes and sides and  Where is constant, 1 2 m 2k is the weight. characteristics.

<!-- b000259 | heading | pages [8] -->
3.2.3 Coefficient calculation

<!-- b000260 | prose | pages [8] -->
 and ik , In order to calculate the coefficient theory[8] is adopted as follows.

<!-- b000261 | prose | pages [8] -->
i(i=1,2), maximum likelihood estimate i i

<!-- b000262 | prose | pages [8] -->
Taking time decay factor into account, the propagation probability decreases as time goes by. Accumulated propagation probability from node u to node v is defined as follows:

<!-- b000263 | prose | pages [8] -->
F (( v , t (|) u v

<!-- b000264 | prose | pages [8] -->
 ti ( i u , v )

<!-- b000265 | prose | pages [8] -->
t

<!-- b000266 | prose | pages [8] -->
 

<!-- b000267 | prose | pages [8] -->
v

<!-- b000268 | prose | pages [8] -->
, , t t )) f ( u , v , c ) dt (18) u t

<!-- b000269 | prose | pages [8] -->
u

<!-- b000270 | prose | pages [8] -->
denotes the time when node i spread the information. Where

<!-- b000271 | prose | pages [8] -->
S (( v , t (|) u , t )) as the probability of which node u will not spread the Define v u

<!-- b000272 | prose | pages [8] -->
vt . information to v before time

<!-- b000273 | prose | pages [8] -->
S (( v , t (|) u , v

<!-- b000274 | prose | pages [8] -->
D  k {( v , t ),..., ( v , t Determine a set i i n

<!-- b000275 | furniture | pages [8] -->


<!-- b000276 | prose | pages [8] -->
 t t )) 1 - F (( v , t (|) u , t )) (19) u u v u

<!-- b000277 | prose | pages [8] -->
)} )} to represents all the node and its spreading n n

<!-- b000278 | furniture | pages [9] -->
Page 8 of 20

<!-- b000279 | furniture | pages [9] -->
Team #42220

<!-- b000280 | prose | pages [9] -->
   k k Q {( v , t ) D , t t time. And the set i i i

<!-- b000281 | prose | pages [9] -->
par (v )

<!-- b000282 | prose | pages [9] -->
} } denotes the nodes which spread information

<!-- b000283 | prose | pages [9] -->
is defined as the information source of node v, that is to say, the before time t.

<!-- b000284 | prose | pages [9] -->
par (v ) information spread from to v.

<!-- b000285 | prose | pages [9] -->
The propagation of a piece of information

<!-- b000286 | prose | pages [9] -->


<!-- b000287 | prose | pages [9] -->


<!-- b000288 | prose | pages [9] -->
k

<!-- b000289 | prose | pages [9] -->
f

<!-- b000290 | prose | pages [9] -->
(

<!-- b000291 | prose | pages [9] -->
c

<!-- b000292 | prose | pages [9] -->
)

<!-- b000293 | prose | pages [9] -->
F

<!-- b000294 | prose | pages [9] -->
((

<!-- b000295 | prose | pages [9] -->
v

<!-- b000296 | prose | pages [9] -->
,

<!-- b000297 | prose | pages [9] -->
t

<!-- b000298 | prose | pages [9] -->
(|)

<!-- b000299 | prose | pages [9] -->
v

<!-- b000300 | prose | pages [9] -->
(

<!-- b000301 | prose | pages [9] -->
v

<!-- b000302 | prose | pages [9] -->
,

<!-- b000303 | prose | pages [9] -->
t

<!-- b000304 | prose | pages [9] -->
)

<!-- b000305 | prose | pages [9] -->
v

<!-- b000306 | prose | pages [9] -->
kc is calculated as follows:

<!-- b000307 | prose | pages [9] -->


<!-- b000308 | prose | pages [9] -->


<!-- b000309 | prose | pages [9] -->
u

<!-- b000310 | prose | pages [9] -->
,

<!-- b000311 | prose | pages [9] -->
t

<!-- b000312 | prose | pages [9] -->
))

<!-- b000313 | prose | pages [9] -->
S

<!-- b000314 | prose | pages [9] -->
((

<!-- b000315 | prose | pages [9] -->
v

<!-- b000316 | prose | pages [9] -->
,

<!-- b000317 | prose | pages [9] -->
t

<!-- b000318 | prose | pages [9] -->
(|)

<!-- b000319 | prose | pages [9] -->
u

<!-- b000320 | prose | pages [9] -->
,

<!-- b000321 | prose | pages [9] -->
t

<!-- b000322 | prose | pages [9] -->
))

<!-- b000323 | prose | pages [9] -->
(20)

<!-- b000324 | prose | pages [9] -->
u

<!-- b000325 | prose | pages [9] -->
v u

<!-- b000326 | prose | pages [9] -->
k

<!-- b000327 | prose | pages [9] -->


<!-- b000328 | prose | pages [9] -->


<!-- b000329 | prose | pages [9] -->
Q

<!-- b000330 | prose | pages [9] -->
(

<!-- b000331 | prose | pages [9] -->
v

<!-- b000332 | prose | pages [9] -->
\)

<!-- b000333 | prose | pages [9] -->
par

<!-- b000334 | prose | pages [9] -->
(

<!-- b000335 | prose | pages [9] -->
v

<!-- b000336 | prose | pages [9] -->
)

<!-- b000337 | prose | pages [9] -->
C  1 2 nc { c , c ,..., } So the propagation probability of all pieces of information in set be obtained in the following formula:

<!-- b000338 | prose | pages [9] -->
f

<!-- b000339 | prose | pages [9] -->
(

<!-- b000340 | prose | pages [9] -->
f (C )

<!-- b000341 | prose | pages [9] -->
can

<!-- b000342 | prose | pages [9] -->


<!-- b000343 | prose | pages [9] -->


<!-- b000344 | prose | pages [9] -->
kc C C

<!-- b000345 | prose | pages [9] -->
)

<!-- b000346 | prose | pages [9] -->
f

<!-- b000347 | prose | pages [9] -->
( ) (21)

<!-- b000348 | prose | pages [9] -->
 

<!-- b000349 | prose | pages [9] -->
1

<!-- b000350 | prose | pages [9] -->
k n

<!-- b000351 | prose | pages [9] -->
, we set the object function: To get the larger value of

<!-- b000352 | prose | pages [9] -->
 min lg f ( C ) (22)

<!-- b000353 | prose | pages [9] -->
 and ik , Train data through computer, we can finally obtain the value of coefficient

<!-- b000354 | prose | pages [9] -->
i(i=1,2).

<!-- b000355 | furniture | pages [9] -->


<!-- b000356 | prose | pages [9] -->
i

<!-- b000357 | heading | pages [9] -->
3.3 Outer Layer: Information Flow from Region to Region

<!-- b000358 | prose | pages [9] -->
As analyzed above, the development level is unbalanced on the Earth which influences the flow of information, so the nodes we choose must be representative. To simplify the model, we choose GDP per capita as the criteria, with data from the CJDBY.net[9], which is shown in Figure 3.

<!-- b000359 | furniture | pages [9] -->


<!-- b000360 | caption | pages [9] -->
Figure 3 GDP per capita                    Figure 4 Global network

<!-- b000361 | prose | pages [9] -->
We can see that each of which has obvious difference GDP per capita is signed by a certain color. Apparently, the GDP per capita of America, Canada, Northern Europe and Australia(area with color of purple)is four times as big as the world’s average level. On the contrary, the one of area with dark blue color is relative low. According to development level and geography, we choose seven typical countries in Figure 4:America, Brazil, France, Congo, Russia, China and Austria.

<!-- b000362 | prose | pages [9] -->
In order to investigate the flow of information among nodes, we detail this phenomenon by applying the mechanism of two-dimensional reaction-diffusion model(R-D equation).

<!-- b000363 | furniture | pages [9] -->


<!-- b000364 | furniture | pages [10] -->
Page 9 of 20

<!-- b000365 | furniture | pages [10] -->
Team #42220

<!-- b000366 | prose | pages [10] -->
  f ( , ) and its gradient, whose magnitude is the maximum rate of change A scalar field

<!-- b000367 | prose | pages [10] -->
of f per unit length of the coordinate space at the given point, could be described below in

<!-- b000368 | prose | pages [10] -->
polar coordinate system:

<!-- b000369 | prose | pages [10] -->
 

<!-- b000370 | prose | pages [10] -->
 

<!-- b000371 | prose | pages [10] -->


<!-- b000372 | prose | pages [10] -->
V

<!-- b000373 | prose | pages [10] -->
[

<!-- b000374 | prose | pages [10] -->
f

<!-- b000375 | prose | pages [10] -->
( , )]

<!-- b000376 | prose | pages [10] -->
  f ( , )

<!-- b000377 | prose | pages [10] -->
 

<!-- b000378 | prose | pages [10] -->


<!-- b000379 | prose | pages [10] -->
f f

<!-- b000380 | prose | pages [10] -->
1

<!-- b000381 | prose | pages [10] -->
f

<!-- b000382 | prose | pages [10] -->


<!-- b000383 | prose | pages [10] -->
e e

<!-- b000384 | prose | pages [10] -->
（23）

<!-- b000385 | prose | pages [10] -->
 

<!-- b000386 | prose | pages [10] -->
 

<!-- b000387 | prose | pages [10] -->
   

<!-- b000388 | prose | pages [10] -->
will transfer into a vector field V after derogating Therefore, this scalar field

<!-- b000389 | prose | pages [10] -->
gradient. For a source flow, all the streamlines are straight lines emanating from a central point, as shown in Figure 5. Obviously, we see that the components in the radial and

<!-- b000390 | prose | pages [10] -->
/   /   f f     f / 0 , respectively, where tangential directions are and .

<!-- b000391 | furniture | pages [10] -->


<!-- b000392 | caption | pages [10] -->
Figure 5 A point source flow

<!-- b000393 | prose | pages [10] -->
According to the mechanism of reaction-diffusion model, the divergence of every

<!-- b000394 | prose | pages [10] -->
point in this vector field V can be obtained easily :

<!-- b000395 | prose | pages [10] -->
 

<!-- b000396 | prose | pages [10] -->
div div

<!-- b000397 | prose | pages [10] -->
(

<!-- b000398 | prose | pages [10] -->


<!-- b000399 | prose | pages [10] -->
1

<!-- b000400 | prose | pages [10] -->


<!-- b000401 | prose | pages [10] -->


<!-- b000402 | prose | pages [10] -->


<!-- b000403 | prose | pages [10] -->


<!-- b000404 | prose | pages [10] -->
( div ) Where :

<!-- b000405 | prose | pages [10] -->
denotes divergence while

<!-- b000406 | prose | pages [10] -->


<!-- b000407 | prose | pages [10] -->
f

<!-- b000408 | prose | pages [10] -->


<!-- b000409 | prose | pages [10] -->
f f

<!-- b000410 | prose | pages [10] -->
) )

<!-- b000411 | prose | pages [10] -->
div

<!-- b000412 | prose | pages [10] -->
(

<!-- b000413 | prose | pages [10] -->
e

<!-- b000414 | prose | pages [10] -->
)

<!-- b000415 | prose | pages [10] -->


<!-- b000416 | prose | pages [10] -->


<!-- b000417 | prose | pages [10] -->


<!-- b000418 | prose | pages [10] -->
(24)

<!-- b000419 | prose | pages [10] -->


<!-- b000420 | prose | pages [10] -->


<!-- b000421 | prose | pages [10] -->


<!-- b000422 | prose | pages [10] -->
2

<!-- b000423 | prose | pages [10] -->
f

<!-- b000424 | prose | pages [10] -->
1

<!-- b000425 | prose | pages [10] -->
f f

<!-- b000426 | prose | pages [10] -->


<!-- b000427 | prose | pages [10] -->


<!-- b000428 | prose | pages [10] -->


<!-- b000429 | prose | pages [10] -->


<!-- b000430 | prose | pages [10] -->
( ( )

<!-- b000431 | prose | pages [10] -->


<!-- b000432 | prose | pages [10] -->
 

<!-- b000433 | prose | pages [10] -->


<!-- b000434 | prose | pages [10] -->


<!-- b000435 | prose | pages [10] -->


<!-- b000436 | prose | pages [10] -->


<!-- b000437 | prose | pages [10] -->
2

<!-- b000438 | prose | pages [10] -->
 ( ) denotes gradient.

<!-- b000439 | prose | pages [10] -->
f /   2 2 The second part in above equation, that is, , has little impacts on the final

<!-- b000440 | prose | pages [10] -->
value. Here, for the convenience of calculations, we overlook this part.

<!-- b000441 | furniture | pages [10] -->


<!-- b000442 | prose | pages [10] -->
1 f  d i v ( ) (25) 

<!-- b000443 | prose | pages [10] -->
And final conclusion could be draw that divergence of gradient of a scalar field is

<!-- b000444 | furniture | pages [10] -->


<!-- b000445 | furniture | pages [11] -->
Page 10 of 20

<!-- b000446 | furniture | pages [11] -->
Team #42220

<!-- b000447 | prose | pages [11] -->
inversely proportional to the radial distance.

<!-- b000448 | prose | pages [11] -->
Considering the fact that the further distance leads to weaker propagation of information, so we only take the link between a node and its neighboring node into account. Figure 4 shows the nodes chosen and its direct connect. The yellow line represents international information flow.

<!-- b000449 | prose | pages [11] -->
)is a constant From above analysis, we assume that Communication Media Effect ( m

<!-- b000450 | prose | pages [11] -->
among a country which ignores the difference of development level among the range of

<!-- b000451 | prose | pages [11] -->
countries. Meanwhile, the factor of distance is neglected in point to point information network

<!-- b000452 | prose | pages [11] -->
as well.

<!-- b000453 | prose | pages [11] -->
To full present the reality, based on above model, we taken into distance between two

<!-- b000454 | prose | pages [11] -->
 into account. It is a common sense that propagation of countries and difference of m

<!-- b000455 | prose | pages [11] -->
information between points is inversely proportional to their distance while the propagation

<!-- b000456 | prose | pages [11] -->
delay is on the contrary. And the information flow is limited to relatively backward country.

<!-- b000457 | prose | pages [11] -->
between two countries and choose the lower value of Compare the m into calculation. m

<!-- b000458 | prose | pages [11] -->
According to above assumption, together with the mechanism of reaction- diffsion

<!-- b000459 | prose | pages [11] -->
model[10], we suppose that the propagation of information happens from node u to n

<!-- b000460 | prose | pages [11] -->
ode v .The propagation probability  between u and v can p and propagation delay ex

<!-- b000461 | prose | pages [11] -->
be described as:

<!-- b000462 | prose | pages [11] -->


<!-- b000463 | prose | pages [11] -->
p

<!-- b000464 | prose | pages [11] -->


<!-- b000465 | prose | pages [11] -->
ex

<!-- b000466 | prose | pages [11] -->


<!-- b000467 | prose | pages [11] -->


<!-- b000468 | prose | pages [11] -->
ex

<!-- b000469 | prose | pages [11] -->
ex

<!-- b000470 | prose | pages [11] -->
p

<!-- b000471 | prose | pages [11] -->
(

<!-- b000472 | prose | pages [11] -->
u

<!-- b000473 | prose | pages [11] -->
,

<!-- b000474 | prose | pages [11] -->
v

<!-- b000475 | prose | pages [11] -->
,

<!-- b000476 | prose | pages [11] -->
c

<!-- b000477 | prose | pages [11] -->
)

<!-- b000478 | prose | pages [11] -->
 

<!-- b000479 | prose | pages [11] -->
k

<!-- b000480 | prose | pages [11] -->
1

<!-- b000481 | prose | pages [11] -->
d

<!-- b000482 | prose | pages [11] -->
(26)

<!-- b000483 | prose | pages [11] -->
uv

<!-- b000484 | prose | pages [11] -->
  

<!-- b000485 | prose | pages [11] -->


<!-- b000486 | prose | pages [11] -->


<!-- b000487 | prose | pages [11] -->
k

<!-- b000488 | prose | pages [11] -->
(

<!-- b000489 | prose | pages [11] -->
u

<!-- b000490 | prose | pages [11] -->
,

<!-- b000491 | prose | pages [11] -->
v

<!-- b000492 | prose | pages [11] -->
,

<!-- b000493 | prose | pages [11] -->
c

<!-- b000494 | prose | pages [11] -->
)

<!-- b000495 | prose | pages [11] -->
d

<!-- b000496 | prose | pages [11] -->
2

<!-- b000497 | prose | pages [11] -->
uv

<!-- b000498 | prose | pages [11] -->
denotes the distance from node u to node v , and d Where :

<!-- b000499 | prose | pages [11] -->
uv

<!-- b000500 | prose | pages [11] -->
weight respectively.

<!-- b000501 | heading | pages [11] -->
3.4 Information Flow Situation

<!-- b000502 | prose | pages [11] -->
k 1,k denotes the 2

<!-- b000503 | prose | pages [11] -->
We have obtained the propagation probability and propagation delay from above analysis. Set up two sets: set K includes the nodes which have spread the information(including the information source) and set N includes all nodes except nodes in set K.

<!-- b000504 | prose | pages [11] -->
To express the information flow clearly ,there are mainly four steps as follows:

<!-- b000505 | prose | pages [11] -->
as the information source and the number of all nodes is  Step 1:Suppose the node 1

<!-- b000506 | prose | pages [11] -->
 idenotes the spread time from source to node i).    1  0 K m.

<!-- b000507 | prose | pages [11] -->
.

<!-- b000508 | prose | pages [11] -->
( 1

<!-- b000509 | prose | pages [11] -->
the number of nodes in set K).

<!-- b000510 | prose | pages [11] -->


<!-- b000511 | prose | pages [11] -->
 n 1 (n denotes

<!-- b000512 | prose | pages [11] -->
     f ( , ) ( , ) Step 2:Calculate the propagation probability and propagation delay

<!-- b000513 | furniture | pages [11] -->


<!-- b000514 | prose | pages [11] -->
i j i j

<!-- b000515 | prose | pages [11] -->
in set K and all their neighboring node between the node i

<!-- b000516 | prose | pages [11] -->
   

<!-- b000517 | prose | pages [11] -->
in set N. j

<!-- b000518 | prose | pages [11] -->
into set K. (is a threshold, usually from 0.5 to 0.6), take node f ( , )  Step 3:If i j        n  ( , ) n 1 j .Return to Step 2. , j i i j

<!-- b000519 | prose | pages [11] -->
   f ( u , v ) Step 4:If there not exists a node v which and the last included node is

<!-- b000520 | prose | pages [11] -->
is the total propagation time,

<!-- b000521 | heading | pages [11] -->
.The conclusion is that

<!-- b000522 | prose | pages [11] -->
p p

<!-- b000523 | prose | pages [11] -->
ratio.

<!-- b000524 | furniture | pages [11] -->


<!-- b000525 | prose | pages [11] -->
n/ m is the total propagation

<!-- b000526 | furniture | pages [12] -->
Page 11 of 20

<!-- b000527 | furniture | pages [12] -->
Team #42220

<!-- b000528 | caption | pages [12] -->
Figure 5 and 6 help visualize spread of information.

<!-- b000529 | furniture | pages [12] -->


<!-- b000530 | furniture | pages [12] -->


<!-- b000531 | furniture | pages [12] -->


<!-- b000532 | caption | pages [12] -->
Figure 5 Original network            Figure 6 Information spreading network

<!-- b000533 | prose | pages [12] -->
The blue spots represents the nodes which have spread the information. As shown in the Figure 5,there is only one node in the beginning which is information source. Through the spread of information, as shown in Figure 6, the number of blue spots increases and new blue spots work as new ‘information source’ to spread information.

<!-- b000534 | heading | pages [12] -->
3.5 Sensitivity Analysis

<!-- b000535 | heading | pages [12] -->
3.5.1 Change the Value of Index

<!-- b000536 | prose | pages [12] -->
Based on our constructed model, we extract many indexes as the attributes of node and side. For the purpose of concise writing, we choose two representative indexes for detailed description which represents the attributes of node and side respectively.

<!-- b000537 | furniture | pages [12] -->


<!-- b000538 | furniture | pages [12] -->


<!-- b000539 | caption | pages [12] -->
Figure 7 Sensitivity analysis of W         Figure 8 Sensitivity analysis of Si

<!-- b000540 | caption | pages [12] -->
Figure 7 and Figure 8 show the sensitivity analysis of willing degree of receiver

<!-- b000541 | prose | pages [12] -->
(attributes of node) and the interest similarity between the sender and receiver (attributes of side).The blue solid line represents the original trend of willing degree, the dashed lines represent adjusted trends of index; red one matches expanding value of index, while green one matches reducing influence of index.

<!-- b000542 | prose | pages [12] -->
It is obvious that the total trend of three lines in Figure 13 is all rising, which represents that the propagation ratio is in proportion to willing degree. Increasing the value of willing degree seems to help improve the flow of information.

<!-- b000543 | prose | pages [12] -->
The results of sensitivity analysis of Si is similar to the one of W. But the trend for Si is smoother which shows that our model is not sensitive to the interest similarity compared to

<!-- b000544 | furniture | pages [12] -->


<!-- b000545 | furniture | pages [13] -->
Page 12 of 20

<!-- b000546 | furniture | pages [13] -->
Team #42220

<!-- b000547 | prose | pages [13] -->
willing degree of receiver.

<!-- b000548 | heading | pages [13] -->
3.5.2 Remove a Index

<!-- b000549 | prose | pages [13] -->
To show the different influence degree of different indexes to the flow of information, we choose four indexes: Influence(F), Authority(A), Activity(Ac), Willing(W) as example.

<!-- b000550 | caption | pages [13] -->
Figure 9 shows the different propagation delay (when the propagation ratio reaches 10%)

<!-- b000551 | prose | pages [13] -->
of the case when we remove one of above four indexes.

<!-- b000552 | furniture | pages [13] -->


<!-- b000553 | caption | pages [13] -->
Figure 9 Sensitivity Analysis of Removing a index

<!-- b000554 | prose | pages [13] -->
We can conclude that the lack of Influence index and Willing index leads to increasing the propagation delay time. The difference between the case of lack F and the normal is larger than the case of lack W and the normal, which represents that F is more sensitive to our model than W. In the same way, the lack of Authority leads to decreasing the propagation delay time. Among all these four indexes, model is most sensitive to authority, later comes influence, Activity and Willing.

<!-- b000555 | prose | pages [13] -->
Meanwhile, the difference is relatively small which indicates the stability of our model.

<!-- b000556 | heading | pages [13] -->
4. Application and Analysis

<!-- b000557 | prose | pages [13] -->
After all equations are determined above, our model is final completed. So next, we concentrate on solving relative problems and giving out analysis as well.

<!-- b000558 | heading | pages [13] -->
4.1 Task 1: Qualification of News

<!-- b000559 | prose | pages [13] -->
Both the inherent value of the information itself and speed of information are vital to information propagation. News, a form of information which satisfies the law of information propagation, ought to be qualified from above two aspects. The inherent value of news are divided into the value of content and the quality of presentation which we have analyzed above. We will discuss the information flow efficiency in detail as below.

<!-- b000560 | prose | pages [13] -->
As we have analyzed above, the total propagation delay timeand the total propagation

<!-- b000561 | prose | pages [13] -->
ratio ,which reflects the flow efficiency, can be obtained through computer calculation.

<!-- b000562 | prose | pages [13] -->
 Quantify the efficiency below: eff

<!-- b000563 | prose | pages [13] -->
 eff

<!-- b000564 | prose | pages [13] -->
 ( 

<!-- b000565 | prose | pages [13] -->
   1     (27) 2

<!-- b000566 | prose | pages [13] -->
is negative while i 2,1 ) Where denotes the weight. i

<!-- b000567 | furniture | pages [13] -->


<!-- b000568 | prose | pages [13] -->
is positive. 1 1 2

<!-- b000569 | furniture | pages [14] -->
Page 13 of 20

<!-- b000570 | furniture | pages [14] -->
Team #42220

<!-- b000571 | prose | pages [14] -->
In conclusion, the quality of news can be calculated as follows:

<!-- b000572 | prose | pages [14] -->
 quality

<!-- b000573 | prose | pages [14] -->
i ( 

<!-- b000574 | prose | pages [14] -->
      (28) 1 eff 2 c

<!-- b000575 | prose | pages [14] -->
 denotes the weight of ith indicator. i 2,1 ) Where denotes information flow eff

<!-- b000576 | prose | pages [14] -->
cdenotes the inherent value which has been analyzed above. efficiency and

<!-- b000577 | prose | pages [14] -->
   For the different situation, we can set different threshold .When

<!-- b000578 | prose | pages [14] -->
information can qualified as news.

<!-- b000579 | prose | pages [14] -->
,the quality

<!-- b000580 | heading | pages [14] -->
4.2 Task 2: Predict the Information Communication Situation for Today

<!-- b000581 | prose | pages [14] -->
The market share of different media is an indicator to quantify the information

<!-- b000582 | prose | pages [14] -->
i  into 1 in equation(1) and let communication. Change the weight N 0 (i=TEL,R,TV,I,M)

<!-- b000583 | prose | pages [14] -->
,which is analyzed in section 4.2. Compared to calculate the propagation ratio N with the N

<!-- b000584 | prose | pages [14] -->
actual market share of newspaper, we come to analyze the error between our model and the

<!-- b000585 | prose | pages [14] -->
reality. The market share forecast of other media is in the same way.

<!-- b000586 | prose | pages [14] -->
First, we give out the total trend in market share of six media plots as follows based on regression analysis. We choose two representative countries: America and China as study objects.

<!-- b000587 | furniture | pages [14] -->


<!-- b000588 | furniture | pages [14] -->


<!-- b000589 | furniture | pages [14] -->


<!-- b000590 | caption | pages [14] -->
Figure 10 Media Market Share in America      Figure 11 Media Market Share in China

<!-- b000591 | prose | pages [14] -->
The specific value of market share of different media is listed in Table 3 and Table 4.

<!-- b000592 | caption | pages [14] -->
Table 3 Media Market Share in America

<!-- b000593 | prose | pages [14] -->
Radio Medium Newspaper Telegraph Television Internet Phone 0.04 Weigh 0.09 0.01

<!-- b000594 | furniture | pages [14] -->


<!-- b000595 | prose | pages [14] -->
0.32 0.27 0.27

<!-- b000596 | caption | pages [14] -->
Table 4 Media Market Share in China

<!-- b000597 | prose | pages [14] -->
Radio Medium Newspaper Telegraph Television Internet Phone 0.07 Weigh 0.12 0.02 0.29 0.25 0.25

<!-- b000598 | prose | pages [14] -->
We can see that the market share of traditional media such as newspaper and radio is descending all the time. On the contrary, the new media such as the Internet and mobile phone occupy more media share.

<!-- b000599 | prose | pages [14] -->
There are six media and seven regions, for concise writing, we choose the newspaper and the Internet of America for example. We collect data from a discussion paper from communic@tions Management Inc[11]and BBC news[12].

<!-- b000600 | furniture | pages [14] -->


<!-- b000601 | furniture | pages [15] -->
Page 14 of 20

<!-- b000602 | furniture | pages [15] -->
Team #42220

<!-- b000603 | furniture | pages [15] -->


<!-- b000604 | furniture | pages [15] -->


<!-- b000605 | furniture | pages [15] -->


<!-- b000606 | caption | pages [15] -->
Figure 12 Market share of Newspaper        Figure 13 Market share of the Internet

<!-- b000607 | caption | pages [15] -->
Figure 12 shows the market share of newspaper while Figure 13 shows the one of the

<!-- b000608 | prose | pages [15] -->
Internet. The blue full line represents the reality and the green dashed line represents the forecast based on the past data. Obviously, the green line is close to the blue one ,with the relative error is under 10%, shows that our model is reliable. The specific error is shown in

<!-- b000609 | caption | pages [15] -->
Table 5.

<!-- b000610 | caption | pages [15] -->
Table 5 The Error in the Market Share of Different Media

<!-- b000611 | prose | pages [15] -->
Forecast Medium True value Absolute Error Relative Error 0.28 Newspaper 0.3 0.02 6.67% 0.785 Internet 0.773

<!-- b000612 | prose | pages [15] -->
 Example

<!-- b000613 | prose | pages [15] -->
0.12 1.55%

<!-- b000614 | prose | pages [15] -->
To specify the information communication situation for today, we choose a important world event about the death of Bin Laden, which happens in May 1st, 2011. Based on our model, we calculate information value as the number of 8.3.

<!-- b000615 | prose | pages [15] -->
In order to reduce the amount of calculation, we choose to calculate the number of propagation nodes in one minute to verify our model. Following are our results.

<!-- b000616 | furniture | pages [15] -->


<!-- b000617 | caption | pages [15] -->
Figure 14 Information Spread Network

<!-- b000618 | prose | pages [15] -->
We obtained that the number of nodes is 89.According to the data from peixun.net[13],we know that there are 80 people re-post the information in Twitter, which is similar to our evaluation. From above example, we validate our model’s reliability.

<!-- b000619 | furniture | pages [15] -->


<!-- b000620 | furniture | pages [16] -->
Page 15 of 20

<!-- b000621 | furniture | pages [16] -->
Team #42220

<!-- b000622 | heading | pages [16] -->
4.3 Task 3: Predict the situation around the year 2050

<!-- b000623 | prose | pages [16] -->
There are seven regions, thus, for concise writing, we choose two representative regions, where United States and Congo respectively as our study objects.

<!-- b000624 | heading | pages [16] -->
4.3.1 Communication networks’ relationships

<!-- b000625 | prose | pages [16] -->
As time goes on, our society tends to information-overloaded, with more and more useless information around us. With the development of technology and minds changing, it is obviously that the inherent value of information itself decreases while the efficiency of information flow increases. To show the relationship between flow of speed of  c), which have been quantified above, ) vs inherent value of information( information( eff we define the ratio s as follows:

<!-- b000626 | furniture | pages [16] -->


<!-- b000627 | prose | pages [16] -->


<!-- b000628 | prose | pages [16] -->
eff

<!-- b000629 | prose | pages [16] -->


<!-- b000630 | prose | pages [16] -->
s s

<!-- b000631 | prose | pages [16] -->
(29)

<!-- b000632 | prose | pages [16] -->


<!-- b000633 | prose | pages [16] -->
c

<!-- b000634 | furniture | pages [16] -->


<!-- b000635 | caption | pages [16] -->
Figure 15 Ratio changes in America         Figure 16 Ratio changes in Congo

<!-- b000636 | furniture | pages [16] -->


<!-- b000637 | caption | pages [16] -->
Figure 15 shows the ratio changes in America. The line decreases quickly in the early

<!-- b000638 | prose | pages [16] -->
time and reaches a plateau around the year 2030, which indicates the popularity rate of the Internet will be high and stable at that moment. The ratio will reach approximately the number of 14 around the year 2050. In the same way, Figure 16 shows trend of ratio changes in Congo, which is different from the one of America. The line declines slowly at first and falls faster in about the year 2020, and finally will reach the number of 30 around the year 2050, which is lower than the one of America. These figures indicate the difference of social development level.

<!-- b000639 | heading | pages [16] -->
4.3.2 Communication networks’ capacities

<!-- b000640 | heading | pages [16] -->
According to our constructed model, the total propagation time and the total

<!-- b000641 | prose | pages [16] -->
propagation radioare the two indicators to evaluate networks’ capacities. The data are employed to train the network. Figure 11 and 12 show indicators and  of two countries

<!-- b000642 | prose | pages [16] -->
from the year 1860 to the year 2050 below. We assume that the quantitative value of propagation delay is the number of 1.

<!-- b000643 | furniture | pages [16] -->


<!-- b000644 | furniture | pages [16] -->


<!-- b000645 | furniture | pages [17] -->
Page 16 of 20

<!-- b000646 | furniture | pages [17] -->
Team #42220

<!-- b000647 | furniture | pages [17] -->


<!-- b000648 | furniture | pages [17] -->


<!-- b000649 | caption | pages [17] -->
Figure 17 Capacities changes in America       Figure 18 Capacities changes in Congo

<!-- b000650 | caption | pages [17] -->
Figure 17 plots the variation trend for these two indicators of America. Propagation

<!-- b000651 | prose | pages [17] -->
delay decreases while propagation probability increases on the contrary. There are two time point in the graph, the first one is around the year 1870 when the newspaper come to the world, which improve the spread of information extremely. The second one is the year around 2000 because of the rapid development of Internet technology. These two graphs indicate the history of media and its importance in spreading information. Figure 18 indicates the capacities in Congo changes in the same way.

<!-- b000652 | prose | pages [17] -->
To sum up, the global network capacity increases rapidly before the year 2050 and the developed countries reach a plateau while developing countries are still in their developing period.

<!-- b000653 | heading | pages [17] -->
4.4 Task 4: Influence in Public Interest and Opinion

<!-- b000654 | heading | pages [17] -->
4.4.1 Foundation of Model

<!-- b000655 | prose | pages [17] -->
) ,which represents the interest for In above analysis, we assume that Receiver Effect ( R

<!-- b000656 | prose | pages [17] -->
an individual, is a constant of a node. However, the opinion of an individual is not static all

<!-- b000657 | prose | pages [17] -->
the time. It will be influenced by the spread information or the opinion of its acquaintance and

<!-- b000658 | prose | pages [17] -->
other factors. With the evolution of opinion of each individual, public interest and opinion can

<!-- b000659 | prose | pages [17] -->
be obtained. To simplify the model, we only assume the opinion of an individual is influenced

<!-- b000660 | prose | pages [17] -->
by the spread information.

<!-- b000661 | prose | pages [17] -->
Based on the Bounded Confidence Model[14] ,we establish the public interest and opinion

<!-- b000662 | prose | pages [17] -->
(  si (t ) si t ) [ ]1,0 change model as follows. Define the opinion of node i in time t is  si ( t ) 5.0 represents neutral point of view, , .When:  si si ( ( t ) 5.0 represents positive opinion, with the

<!-- b000663 | prose | pages [17] -->
value more close to the number of 1,the opinion is more positive. The same way,

<!-- b000664 | prose | pages [17] -->
represents negative opinion. Threshold  is the maximum value for two nodes’  si ( t ) 5.0

<!-- b000665 | prose | pages [17] -->
   s ( t ) s ( t ) opinion differences to spread information. That is to say, when

<!-- b000666 | prose | pages [17] -->
can be spread.

<!-- b000667 | prose | pages [17] -->
,information i j

<!-- b000668 | prose | pages [17] -->
The changes in opinion are shown in the following formula:

<!-- b000669 | prose | pages [17] -->
 

<!-- b000670 | prose | pages [17] -->


<!-- b000671 | prose | pages [17] -->
s

<!-- b000672 | prose | pages [17] -->
(

<!-- b000673 | prose | pages [17] -->
t

<!-- b000674 | prose | pages [17] -->
)1

<!-- b000675 | prose | pages [17] -->
s

<!-- b000676 | prose | pages [17] -->
(

<!-- b000677 | prose | pages [17] -->
t

<!-- b000678 | prose | pages [17] -->


<!-- b000679 | prose | pages [17] -->
i i

<!-- b000680 | prose | pages [17] -->
 

<!-- b000681 | prose | pages [17] -->


<!-- b000682 | prose | pages [17] -->
s

<!-- b000683 | prose | pages [17] -->
(

<!-- b000684 | prose | pages [17] -->
t

<!-- b000685 | prose | pages [17] -->
)1

<!-- b000686 | prose | pages [17] -->
s

<!-- b000687 | prose | pages [17] -->
(

<!-- b000688 | prose | pages [17] -->
j j

<!-- b000689 | prose | pages [17] -->
Where is the weight. Usually,   [ ]1,0

<!-- b000690 | furniture | pages [17] -->


<!-- b000691 | prose | pages [17] -->
 

<!-- b000692 | prose | pages [17] -->


<!-- b000693 | prose | pages [17] -->


<!-- b000694 | prose | pages [17] -->
) ) [(

<!-- b000695 | prose | pages [17] -->
s

<!-- b000696 | prose | pages [17] -->
(

<!-- b000697 | prose | pages [17] -->
t

<!-- b000698 | prose | pages [17] -->
)

<!-- b000699 | prose | pages [17] -->
s

<!-- b000700 | prose | pages [17] -->
(

<!-- b000701 | prose | pages [17] -->
t

<!-- b000702 | prose | pages [17] -->
)]

<!-- b000703 | prose | pages [17] -->
j i

<!-- b000704 | prose | pages [17] -->
(30)

<!-- b000705 | prose | pages [17] -->


<!-- b000706 | prose | pages [17] -->


<!-- b000707 | prose | pages [17] -->


<!-- b000708 | prose | pages [17] -->
t t

<!-- b000709 | prose | pages [17] -->
) ) [(

<!-- b000710 | prose | pages [17] -->
s

<!-- b000711 | prose | pages [17] -->
(

<!-- b000712 | prose | pages [17] -->
t

<!-- b000713 | prose | pages [17] -->
)

<!-- b000714 | prose | pages [17] -->
s

<!-- b000715 | prose | pages [17] -->
(

<!-- b000716 | prose | pages [17] -->
t

<!-- b000717 | prose | pages [17] -->
)]

<!-- b000718 | prose | pages [17] -->
i j

<!-- b000719 | prose | pages [17] -->
. .

<!-- b000720 | furniture | pages [18] -->
Page 17 of 20

<!-- b000721 | furniture | pages [18] -->
Team #42220

<!-- b000722 | prose | pages [18] -->
Based on our double-layer network, with regard task 4,we only take the Internet as

<!-- b000723 | prose | pages [18] -->
si (t ) media. When the information spread in our network, of each node i can be recorded. By

<!-- b000724 | prose | pages [18] -->
as means of statistical methods, we can finally get the average public interest and opinion

<!-- b000725 | prose | pages [18] -->
follows:

<!-- b000726 | prose | pages [18] -->


<!-- b000727 | prose | pages [18] -->
o

<!-- b000728 | prose | pages [18] -->
o

<!-- b000729 | prose | pages [18] -->


<!-- b000730 | prose | pages [18] -->
s

<!-- b000731 | prose | pages [18] -->
(

<!-- b000732 | prose | pages [18] -->
t

<!-- b000733 | prose | pages [18] -->
)

<!-- b000734 | prose | pages [18] -->
i

<!-- b000735 | prose | pages [18] -->
 

<!-- b000736 | prose | pages [18] -->
i M

<!-- b000737 | prose | pages [18] -->
( (

<!-- b000738 | prose | pages [18] -->
t t

<!-- b000739 | prose | pages [18] -->
) ) (31)

<!-- b000740 | prose | pages [18] -->
m

<!-- b000741 | prose | pages [18] -->
Where m denotes the total number of nodes in our network. Set M includes all the nodes

<!-- b000742 | prose | pages [18] -->
 can reflect the public opinion comprehensively. in our network so that the value of o

<!-- b000743 | prose | pages [18] -->
  ( t ) 0

<!-- b000744 | prose | pages [18] -->
The change rate of public opinion is defined as

<!-- b000745 | prose | pages [18] -->
 Example

<!-- b000746 | prose | pages [18] -->
. 

<!-- b000747 | prose | pages [18] -->
t

<!-- b000748 | prose | pages [18] -->
To simplify how public interest and opinion changed through information networks, we choose a important event which is about the China helped people in Africa combat Ebola

<!-- b000749 | prose | pages [18] -->
 change is virus.to spread in the network. The trend for he public interest and opinion

<!-- b000750 | prose | pages [18] -->
shown as follows:

<!-- b000751 | prose | pages [18] -->
o

<!-- b000752 | furniture | pages [18] -->


<!-- b000753 | caption | pages [18] -->
Figure 19 Public Opinion Changes

<!-- b000754 | prose | pages [18] -->
is From above picture, we come to a conclusion that before the information spread, o

<!-- b000755 | prose | pages [18] -->
close to 0.5 which represents that the public opinion is neutral. Later in the early time of

<!-- b000756 | prose | pages [18] -->
 tends information spread, the changes of public opinion are extreme. As the time goes by, o

<!-- b000757 | prose | pages [18] -->
to a constant(the number of 0.65)which represents the average public opinion.

<!-- b000758 | heading | pages [18] -->
4.4.2 Suggestions

<!-- b000759 | prose | pages [18] -->
Based on our constructed model above, we can give some suggestions to the government or relevant departments to manage the public interest and opinion on the Internet effectively.  Filter bad or false information when necessary. That is to say, reduce the value of threshold to restrain the spread.  The content of news information ought to be carefully selected. Based on our model to

<!-- b000760 | furniture | pages [18] -->


<!-- b000761 | furniture | pages [19] -->
Page 18 of 20

<!-- b000762 | furniture | pages [19] -->
Team #42220

<!-- b000763 | prose | pages [19] -->
qualify news in section 4.3, we can increases the value of threshold  to guarantee the quality of news.  Strengthen the construction of mainstream news website. Use mainstream voice to influence public opinion, which these websites are more credible and attracts more people.  Besides, the Internet ought to actively interact with the traditional news media to manage public opinion.

<!-- b000764 | furniture | pages [19] -->


<!-- b000765 | heading | pages [19] -->
4.5 Task 5: Factors Influence in Spreading Information and Public Opinion

<!-- b000766 | prose | pages [19] -->
With regard to task 5, we have analyzed information value, people’s initial opinion and bias, form of the message or its source, and the topology or strength of the information network in a region, country, or worldwide from our constructed model. For concise writing, we only analyze how information value spread information and influence public opinion.

<!-- b000767 | heading | pages [19] -->
4.5.1 Influence in Spreading Information

<!-- b000768 | prose | pages [19] -->
We have concluded that propagation probability and propagation delay are two indicators to show the information flow. In order to better illustrate the difference among countries, we choose America and China for example. Figure 20 and 21 show these two indicators’ change trend with time.

<!-- b000769 | furniture | pages [19] -->


<!-- b000770 | furniture | pages [19] -->


<!-- b000771 | caption | pages [19] -->
Figure 20 Propagation Probability Changes     Figure 21 Propagation Delay Changes

<!-- b000772 | prose | pages [19] -->
Horizontal axis is the information value, with its value ranges from 0 to 9 which have analyzed above. Propagation probability increases results from the increasing value of information. On the contrary, propagation delay decreases. These two graphs illustrates that the information with higher value can be spread more quickly and wide. Meanwhile, the propagation probability of China is lower than the one of America while the situation of propagation delay is on the contrary.

<!-- b000773 | heading | pages [19] -->
4.5.2 Influence in Public Opinion

<!-- b000774 | prose | pages [19] -->
  ( t ) 0

<!-- b000775 | prose | pages [19] -->
The value of

<!-- b000776 | prose | pages [19] -->
represents the influence in public opinion. The higher value 

<!-- b000777 | prose | pages [19] -->
t

<!-- b000778 | prose | pages [19] -->
indicates that the public opinion can be influenced more easily. Figure 22 shows the change of its value over time.

<!-- b000779 | furniture | pages [19] -->


<!-- b000780 | furniture | pages [20] -->
Page 19 of 20

<!-- b000781 | furniture | pages [20] -->
Team #42220

<!-- b000782 | furniture | pages [20] -->


<!-- b000783 | caption | pages [20] -->
Figure 22 Changes of Change rate

<!-- b000784 | prose | pages [20] -->
As is shown in the picture, we can conclude that the information with higher value can change the public opinion more easily, which has a greater influence in public opinion. Compare China with America, we can find that the change rate of America is relative higher than the one of China, mainly due to the different proportion of media and development level.

<!-- b000785 | heading | pages [20] -->
5. Strengths and Weaknesses

<!-- b000786 | heading | pages [20] -->
5.1 Strengths

<!-- b000787 | prose | pages [20] -->
 The model combines several attributes of side and code such as the inherent value of information, personal interests, changes of media, which reflects the reality well. Considering seven regions divided from the whole world into our double-layer network,  our model is already comprehensive to some extent.

<!-- b000788 | heading | pages [20] -->
5.2 Weaknesses

<!-- b000789 | prose | pages [20] -->
 The model is applied to well-constructed network such as Facebook or Twitter. It cannot reflect the random event very well.  Due to our complex model and amounts of indicators to calculate, it is inevitable to increase calculated amount which decreases the efficiency of network.  Because of several factors are not considered and the lack of data, our model are not enough to indicate the accurate situation which has a risk of error.

<!-- b000790 | prose | pages [20] -->
Reference

<!-- b000791 | prose | pages [20] -->
[1]  Independent Cascade Model

<!-- b000792 | prose | pages [20] -->
http://www.sumankundu.info/articles/detail/How-To-Code-Independent-Cascade-Model- of-Information-Diffusion [2]  Lagnier C, Denoyer L, Gaussier E, et al. Predicting information diffusion in social

<!-- b000793 | prose | pages [20] -->
networks using content and user’s profiles. Advance in Information Retrieval. Berlin: Springer,2013:74-85. [3]  Thomas L.Saaty, Decision making with analytic hierarchy process. Int. J. Services

<!-- b000794 | prose | pages [20] -->
Sciences, Vol. 1, No. 1, 2008:83-97.

<!-- b000795 | furniture | pages [20] -->


<!-- b000796 | furniture | pages [21] -->
Page 20 of 20

<!-- b000797 | furniture | pages [21] -->
Team #42220

<!-- b000798 | prose | pages [21] -->
[4]  Liu Shuli, Han Zhonggeng, Song Liuyong et al. Comprehensive evaluation model of

<!-- b000799 | prose | pages [21] -->
information value, Journal of Information Engineering University.V0l.8,No.a.Mar. 2007. [5]  TF-IF Model

<!-- b000800 | prose | pages [21] -->
https://en.wikipedia.org/wiki/Tf%E2%80%93idf [6]  Jaccard Distance

<!-- b000801 | prose | pages [21] -->
http://mathoverflow.net/questions/18084/is-the-jaccard-distance-a-distance [7]  Bayesian logistic function

<!-- b000802 | prose | pages [21] -->
http://web.cse.ohio-state.edu/~kulis/teaching/788_sp12/scribe_notes/lecture6.pdf [8]  In Jae Myung, Tutorial on maximum likelihood estimation, Journal of Mathematical

<!-- b000803 | prose | pages [21] -->
Psychology,2003:90-100 [9]  Global GDP per capita

<!-- b000804 | prose | pages [21] -->
http://lt.cjdby.net/thread-1966820-1-1.html [10] Reaction-diffusion model

<!-- b000805 | prose | pages [21] -->
http://mrob.com/pub/comp/xmorphia/ [11] Market share of the newspaper in America

<!-- b000806 | prose | pages [21] -->
http://media-cmi.com/downloads/Sixty_Years_Daily_Newspaper_Circulation_Trends_0 50611.pdf [12] Market share of the Internet in America

<!-- b000807 | prose | pages [21] -->
http://news.bbc.co.uk/2/hi/technology/8552410.stm [13] The situation of information flow about the death of Bin Laden

<!-- b000808 | prose | pages [21] -->
http://www.peixun.net/view/49_author.html [14] Wan Yan, Zhang han. Research on the dynamic model of public opinion in the mode of

<!-- b000809 | prose | pages [21] -->
online comment. Journal of Beijing University of Posts and Telecommunications. V0l.14, No.4. Aug. 2012.

<!-- b000810 | furniture | pages [21] -->


<!-- b000811 | furniture | pages [21] -->

