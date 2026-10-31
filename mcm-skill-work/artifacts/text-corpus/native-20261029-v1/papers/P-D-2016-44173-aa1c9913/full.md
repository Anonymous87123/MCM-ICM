# P-D-2016-44173-aa1c9913

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only

<!-- b000003 | prose | pages [1] -->
For ofﬁce use only

<!-- b000004 | title | pages [1] -->
44173

<!-- b000005 | prose | pages [1] -->
T1

<!-- b000006 | prose | pages [1] -->
F1

<!-- b000007 | prose | pages [1] -->
T2

<!-- b000008 | prose | pages [1] -->
F2

<!-- b000009 | prose | pages [1] -->
T3

<!-- b000010 | prose | pages [1] -->
F3

<!-- b000011 | prose | pages [1] -->
Problem Chosen

<!-- b000012 | prose | pages [1] -->
T4

<!-- b000013 | prose | pages [1] -->
F4

<!-- b000014 | title | pages [1] -->
D

<!-- b000015 | heading | pages [1] -->
2016 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000016 | prose | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000017 | prose | pages [1] -->
How to Understand the Information The ﬂow of information has never been as easy or wide-ranging as it is today. This paper proposes some models to explore the relationship between speed/ﬂow of information with inherent value of information.

<!-- b000018 | prose | pages [1] -->
First,to explore information ﬂow, we build up a SIIR model which takes the me- dia inﬂuence into consideration. This model is developed from the classical SIR model.We introduce the concept of hot transmission nodes to highlight the impact of media. We demonstrate our design with American media data. The results show that our model has a signiﬁcant performance in validating predicted values of the characteristics of information network in 2050.

<!-- b000019 | prose | pages [1] -->
Second,the information ﬁltering can be regarded as a classiﬁcation problem. We design a radial basis function network to implement the information ﬁltering. In order to solve sample noises and improve the computing performance,we decide to use K-means algorithm and RLS algorithm to implement our RBF network. We demonstrate our network in online news dataset ,with an training accuracy of 75.1%,and testing accuracy of 74.3%.we are satisﬁed that the accuracy rate with information ﬁltering as news.

<!-- b000020 | prose | pages [1] -->
Third, We have only considered the social network in the Internet and build a social network SIR(SN-SIR) model to explore the problem-how public interest and opin- ion can be changed through network.It simulates in the standard dataset: Facebook social network dataset .By analyzing the factors which can implement our result- s,we can make a plan to determinate information propagation. Then,we take infor- mation values ,people ˛a´rs initial opinion and bias, form of the message or its source, and topology or other reasons into account and propose a detailed scheme.

<!-- b000021 | prose | pages [1] -->
Finally, effects of external factors are considered in our models.And we analyze the stability and sensitively of our models. Although there are some weakness in our models,the results still demonstrate that our model can undergo disturbance in certain extent.

<!-- b000022 | furniture | pages [2] -->
Team # 44173

<!-- b000023 | furniture | pages [2] -->
Page 2 of 22

<!-- b000024 | heading | pages [2] -->
Contents

<!-- b000025 | contents | pages [2] -->
1

<!-- b000026 | heading | pages [2] -->
Introduction

<!-- b000027 | prose | pages [2] -->
3

<!-- b000028 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Background 3

<!-- b000029 | prose | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2

<!-- b000030 | prose | pages [2] -->
2

<!-- b000031 | heading | pages [2] -->
Assumptions

<!-- b000032 | prose | pages [2] -->
3

<!-- b000033 | heading | pages [2] -->
A SIIR Model of Information Flow

<!-- b000034 | prose | pages [2] -->
3

<!-- b000035 | prose | pages [2] -->
4

<!-- b000036 | prose | pages [2] -->
4

<!-- b000037 | prose | pages [2] -->
Social Network Information Dissemination . . . . . . . . . . . . . . . . . . . . . . 3.1 4

<!-- b000038 | prose | pages [2] -->
Social Network Information Dissemination Characteristics . . . . . . . . . 3.1.1 4

<!-- b000039 | prose | pages [2] -->
Model Building . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1.2

<!-- b000040 | prose | pages [2] -->
3.2 Calculating and Simplifying the Model

<!-- b000041 | prose | pages [2] -->
5

<!-- b000042 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | prose | pages [2] -->
6

<!-- b000044 | prose | pages [2] -->
The Model Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2.1 6

<!-- b000045 | prose | pages [2] -->
Rationality validation And Sensitivity analysis . . . . . . . . . . . . . . . . 3.2.2 7

<!-- b000046 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 Prediction

<!-- b000047 | prose | pages [2] -->
4

<!-- b000048 | heading | pages [2] -->
A Model of Information Filtering

<!-- b000049 | prose | pages [2] -->
8

<!-- b000050 | prose | pages [2] -->
11

<!-- b000051 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 Model Description 11

<!-- b000052 | prose | pages [2] -->
Hybrid Learning Procedure For Networks . . . . . . . . . . . . . . . . . . . . . . . 4.2 11

<!-- b000053 | prose | pages [2] -->
Experiment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 13

<!-- b000054 | prose | pages [2] -->
Sensitively Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.4 13

<!-- b000055 | prose | pages [2] -->
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.5

<!-- b000056 | prose | pages [2] -->
5

<!-- b000057 | heading | pages [2] -->
A SN-SIR Model

<!-- b000058 | prose | pages [2] -->
13

<!-- b000059 | prose | pages [2] -->
14

<!-- b000060 | prose | pages [2] -->
The Way of Information Dissemination in Network 5.1 . . . . . . . . . . . . . . . . .

<!-- b000061 | prose | pages [2] -->
14

<!-- b000062 | prose | pages [2] -->
A Model of Public Opinion Dissemination in Social Network . . . . . . . . . . . . 5.2 14

<!-- b000063 | prose | pages [2] -->
Model Building . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 15

<!-- b000064 | prose | pages [2] -->
Sensitivity Analysis and Model Validation . . . . . . . . . . . . . . . . . . . . . . . 5.3 16

<!-- b000065 | prose | pages [2] -->
Model Validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.3.1 16

<!-- b000066 | prose | pages [2] -->
Sensitivity, parameter validation analysis . . . . . . . . . . . . . . . . . . . 5.3.2 17

<!-- b000067 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.4 Result Analysis

<!-- b000068 | prose | pages [2] -->
6 Analysis

<!-- b000069 | prose | pages [2] -->
20

<!-- b000070 | prose | pages [2] -->
21

<!-- b000071 | prose | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 21

<!-- b000072 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 Weaknesses 21

<!-- b000073 | furniture | pages [3] -->
Team # 44173

<!-- b000074 | furniture | pages [3] -->
Page 3 of 22

<!-- b000075 | prose | pages [3] -->
1

<!-- b000076 | heading | pages [3] -->
Introduction

<!-- b000077 | prose | pages [3] -->
1.1

<!-- b000078 | heading | pages [3] -->
Background

<!-- b000079 | prose | pages [3] -->
Broadly speaking, information is one of the important ways for us to perceive the outside world. Today it spreads quickly in tech-connected communication network. Sometimes it is due to the information ﬁnding its way to inﬂuential or central network nodes that accelerate its spread through social media. Our prevailing premise is that this cultural characteristic to share information (both serious and trivial) has always been three. At present, information propa- gation is exposed explosive growth.Beacause our social networks and medium are more and more complex.Without effective ways to solve these problems ,it will ﬁnally cause information propagation is more and more difﬁcult to umderstand.Hence,our work has its unprecedented signiﬁcance in world nowadays.

<!-- b000080 | prose | pages [3] -->
1.2 Our Work

<!-- b000081 | prose | pages [3] -->
This paper propose some models to explore the relationship between speed/ﬂow of informa- tion with inherent value of information. The Dilemma:

<!-- b000082 | prose | pages [3] -->
• An adaptive ﬂow model is established with the consideration of the complex network changes.

<!-- b000083 | prose | pages [3] -->
• Make use of the existing parameters to ﬁlter the information reasonably.

<!-- b000084 | prose | pages [3] -->
• Reasonable analysis of inﬂuencing factors in the process of information transmission.

<!-- b000085 | prose | pages [3] -->
The Approach:

<!-- b000086 | prose | pages [3] -->
• FirstˇcˇnTo explore information ﬂow, we build up a SIIR model which takes the special fea- tures if media inﬂuence into consideration. This model is developed from classical SIR model.

<!-- b000087 | prose | pages [3] -->
• The Results show that our model has a signiﬁcant performance in validate the value of prediction with real value. And then ,we predict the rate of daily contact in 2050.

<!-- b000088 | prose | pages [3] -->
• Information ﬁltering is regarded as classiﬁcation problem. we design a radial basis func- tion network to implement information ﬁltering. In order to solve sample noise and com- puting performance, we decide to use K-means algorithm and RLS algorithm to imple- ment our RBF network.

<!-- b000089 | prose | pages [3] -->
• We have only considered the social network in the Internet and build a social network SIR(SN-SIR) to explore the problem ˛a´s how public interest an opinion can be changed through network ˛a´s.

<!-- b000090 | prose | pages [3] -->
• We can make a plan to determinate information propagation. Then ,we take information value ,people ˛a´rs initial opinion and bias, form of the message or its source, and topology or other reasons into account and build a detailed scheme.

<!-- b000091 | furniture | pages [4] -->
Team # 44173

<!-- b000092 | furniture | pages [4] -->
Page 4 of 22

<!-- b000093 | prose | pages [4] -->
2

<!-- b000094 | heading | pages [4] -->
Assumptions

<!-- b000095 | prose | pages [4] -->
The accuracy of our models rely on certain key, simplifying assumptions. These assumptions are listed below:

<!-- b000096 | prose | pages [4] -->
• Do not consider factors such as natural birth,death,and population mobility.The total population keeps as a constant K.

<!-- b000097 | prose | pages [4] -->
• Infected individuals once contact with susceptible individuals,Infected individuals change to susceptible individuals at a certain probability.

<!-- b000098 | prose | pages [4] -->
• At a certain time,The number of individuals per unit time removing from the infected individuals is proportional to the number of patients.

<!-- b000099 | prose | pages [4] -->
• The number of media is relatively ﬁxed in the same period.

<!-- b000100 | prose | pages [4] -->
Under the above and basic assumptions, we can set out to construct our model.

<!-- b000101 | prose | pages [4] -->
3

<!-- b000102 | heading | pages [4] -->
A SIIR Model of Information Flow

<!-- b000103 | prose | pages [4] -->
Information is created by the social network users and transmits in the entire network.The result of transmission is that the receiver of the information translates into the transmitter and disseminate the information to others,or translates to the recovered one and does not transmit to others.Obviously, this transmission way is similar with the way Infectious diseases spread in the crowd. Based on the analysis of social network structure,we introduce the hot transmission node into network,and proposes an information transmission model based on the improved SIR model [1],which is simulated with the data-based Facebook social network.

<!-- b000104 | prose | pages [4] -->
3.1 Social Network Information Dissemination

<!-- b000105 | prose | pages [4] -->
3.1.1 Social Network Information Dissemination Characteristics

<!-- b000106 | prose | pages [4] -->
In this section,we propose a to explore a general model of information ﬂow problems, which is not subjected to the limitations of the times and mediums of communication.

<!-- b000107 | prose | pages [4] -->
The total number of user nodes in social networks is denoted as N.The network is assumed to be an undirected graph and each node in the network may be in one of three states: susceptible(s), infected(i), or recovered(r).Nodes in state i have received the message and have the ability to transmit it.Nodes in state s have not received the message and have the possibility to receive it.Nodes in state r have received the message and will not transmit it any more.

<!-- b000108 | prose | pages [4] -->
There are a variety of mediums of communication,such as newspapers,televisions,the Inter- net and so on.Different mediums have different ability of transmission,but all of these medi- ums owe stronger ability than human beings.We consider media as the hot transmission n- odes.Their contact rate is denoted as λ1. Ordinary users in networks are considered as ordinary nodes.Their contact rate is denoted as λ2.

<!-- b000109 | prose | pages [4] -->
The laws of Information dissemination of social networks with hot transmission nodes are as below:[2]

<!-- b000110 | furniture | pages [5] -->
Team # 44173

<!-- b000111 | furniture | pages [5] -->
Page 5 of 22

<!-- b000112 | prose | pages [5] -->
• Hot transmission nodes contact with other nodes with the contact rate x1,while ordinary nodes with the contact rate λ2.

<!-- b000113 | prose | pages [5] -->
• After nodes in state s received the information from nodes in state i,they change into recovered nodes in a probability of µ,and into ordinary infected nodes in a probability of 1 −µ.

<!-- b000114 | prose | pages [5] -->
• With the propagation of information,the proportion of three types of nodes will tend to be stable.

<!-- b000115 | prose | pages [5] -->
The schematic diagram of information dissemination of social networks with hot transmis- sion nodes as shown in Figure 1, the solid line shows the information transmission between two points.

<!-- b000116 | caption | pages [5] -->
Figure 1: the Information Transmission of Atrioventricular Model Structure Diagrams

<!-- b000117 | caption | pages [5] -->
Figure 2: the Improved SIR Model

<!-- b000118 | prose | pages [5] -->
3.1.2

<!-- b000119 | heading | pages [5] -->
Model Building

<!-- b000120 | prose | pages [5] -->
According to the characteristics of the transmission above,we can get the information transmis- sion of atrioventricular model structure diagrams, as shown in Figure 1.

<!-- b000121 | prose | pages [5] -->
i0 is the proportion of hot transmission nodes in networks,which is usually ﬁxed.i(t) is the proportion of ordinary infected nodes in the time of t,which consists of i1(t),the ordinary in- fected nodes generated by hot transmission nodes,and i2(t),the ordinary nodes infected nodes generated by ordinary infected nodes.λ1 is the contact rate of hot transmission nodes,while λ2 is the contact rate of ordinary infected nodes.r(t) is the proportion of nodes in state r,µ is the rate of Immune probability.[3] We can get the model as follows:

<!-- b000122 | prose | pages [5] -->
ds(t)

<!-- b000123 | prose | pages [5] -->


<!-- b000124 | prose | pages [5] -->
= −λ1i0s(t) −λ2s(t)i(t) dt

<!-- b000125 | prose | pages [5] -->
      

<!-- b000126 | prose | pages [5] -->
di(t)

<!-- b000127 | prose | pages [5] -->


<!-- b000128 | prose | pages [5] -->
= µ[λ1i0s(t) + λ2s(t)i(t)]

<!-- b000129 | prose | pages [5] -->
 

<!-- b000130 | prose | pages [5] -->
dt

<!-- b000131 | prose | pages [5] -->
      

<!-- b000132 | prose | pages [5] -->
dr(t)

<!-- b000133 | prose | pages [5] -->
= (1 −µ)[λ1i0s(t) + λ2s(t)i(t)]

<!-- b000134 | prose | pages [5] -->
(1)

<!-- b000135 | prose | pages [5] -->
dt

<!-- b000136 | prose | pages [5] -->
     

<!-- b000137 | prose | pages [5] -->
s(t) + i(t) + i0 + r(t) = 1

<!-- b000138 | prose | pages [5] -->
         

<!-- b000139 | prose | pages [5] -->
i0 = i10, i(0) = i20, s(0) = s0, r(0) = r0

<!-- b000140 | prose | pages [5] -->


<!-- b000141 | furniture | pages [6] -->
Team # 44173

<!-- b000142 | furniture | pages [6] -->
Page 6 of 22

<!-- b000143 | heading | pages [6] -->
Calculating and Simplifying the Model

<!-- b000144 | prose | pages [6] -->
3.2

<!-- b000145 | prose | pages [6] -->
3.2.1

<!-- b000146 | heading | pages [6] -->
The Model Results

<!-- b000147 | prose | pages [6] -->
Take the United States as an example,we obtain the statistical data of the circulation of news- papers, and numbers of users of radio, television, mobile phone and the Internet in different years.After analysis,we calculate the daily contact ratio of the ﬁve media,λi.We calculated the proportion of people contact with the different media group in all the population in the US. at that time.

<!-- b000148 | prose | pages [6] -->
λ1 =

<!-- b000149 | prose | pages [6] -->
N N X

<!-- b000150 | prose | pages [6] -->
λiPi (2)

<!-- b000151 | prose | pages [6] -->
i=1 i=1

<!-- b000152 | prose | pages [6] -->
We choose ﬁve years:1850,1930,1960,1996,2012,to calculate the model,and get the pictures of the change trend of the proportion of three kinds of nodes.

<!-- b000153 | furniture | pages [6] -->


<!-- b000154 | prose | pages [6] -->
100

<!-- b000155 | prose | pages [6] -->
90

<!-- b000156 | prose | pages [6] -->
Susceptible individuals Recovered individuals

<!-- b000157 | prose | pages [6] -->
80

<!-- b000158 | prose | pages [6] -->
Infected individuals

<!-- b000159 | prose | pages [6] -->
70

<!-- b000160 | prose | pages [6] -->
the rate of three node

<!-- b000161 | prose | pages [6] -->
60

<!-- b000162 | prose | pages [6] -->
X: 83.88 Y: 50.02

<!-- b000163 | prose | pages [6] -->
50

<!-- b000164 | prose | pages [6] -->
40

<!-- b000165 | prose | pages [6] -->
30

<!-- b000166 | prose | pages [6] -->
20

<!-- b000167 | prose | pages [6] -->
X: 72.35 Y: 10.06

<!-- b000168 | prose | pages [6] -->
10

<!-- b000169 | furniture | pages [6] -->


<!-- b000170 | prose | pages [6] -->
0 0 10 20 30 40 50 60 70 80 90 100

<!-- b000171 | prose | pages [6] -->
time/days

<!-- b000172 | furniture | pages [6] -->


<!-- b000173 | prose | pages [6] -->
100 100

<!-- b000174 | prose | pages [6] -->
90 90

<!-- b000175 | prose | pages [6] -->
Susceptible individuals Recovered individuals

<!-- b000176 | prose | pages [6] -->
80 80

<!-- b000177 | prose | pages [6] -->
Infected individuals

<!-- b000178 | prose | pages [6] -->
70 70

<!-- b000179 | prose | pages [6] -->
the rate of three node the rate of three node

<!-- b000180 | prose | pages [6] -->
60 60

<!-- b000181 | prose | pages [6] -->
X: 66.04 Y: 50.07

<!-- b000182 | prose | pages [6] -->
50 50

<!-- b000183 | prose | pages [6] -->
40 40

<!-- b000184 | prose | pages [6] -->
30 30

<!-- b000185 | prose | pages [6] -->
20 20

<!-- b000186 | prose | pages [6] -->
X: 54.55 Y: 10.08

<!-- b000187 | prose | pages [6] -->
10 10

<!-- b000188 | furniture | pages [6] -->


<!-- b000189 | furniture | pages [6] -->


<!-- b000190 | prose | pages [6] -->
0 0 0 0 10 20 30 40 50 60 70 80 90 100

<!-- b000191 | prose | pages [6] -->
time/days

<!-- b000192 | caption | pages [6] -->
Figure 3: 1850

<!-- b000193 | caption | pages [6] -->
Figure 4: 1930

<!-- b000194 | furniture | pages [6] -->


<!-- b000195 | prose | pages [6] -->
100

<!-- b000196 | prose | pages [6] -->
90

<!-- b000197 | prose | pages [6] -->
Susceptible individuals Recovered individuals

<!-- b000198 | prose | pages [6] -->
80

<!-- b000199 | prose | pages [6] -->
Infected individuals

<!-- b000200 | prose | pages [6] -->
70

<!-- b000201 | prose | pages [6] -->
the rate of three node

<!-- b000202 | prose | pages [6] -->
60

<!-- b000203 | prose | pages [6] -->
X: 59.29 Y: 50.06

<!-- b000204 | prose | pages [6] -->
50

<!-- b000205 | prose | pages [6] -->
40

<!-- b000206 | prose | pages [6] -->
30

<!-- b000207 | prose | pages [6] -->
20

<!-- b000208 | prose | pages [6] -->
X: 47.75 Y: 10.05

<!-- b000209 | prose | pages [6] -->
10

<!-- b000210 | furniture | pages [6] -->


<!-- b000211 | prose | pages [6] -->
0 0 10 20 30 40 50 60 70 80 90 100

<!-- b000212 | prose | pages [6] -->
time/days

<!-- b000213 | furniture | pages [6] -->


<!-- b000214 | prose | pages [6] -->
100 100

<!-- b000215 | prose | pages [6] -->
Susceptible individuals

<!-- b000216 | prose | pages [6] -->
90 90

<!-- b000217 | prose | pages [6] -->
Recovered individuals

<!-- b000218 | prose | pages [6] -->
80 80

<!-- b000219 | prose | pages [6] -->
Infected individuals

<!-- b000220 | prose | pages [6] -->
70 70

<!-- b000221 | prose | pages [6] -->
the rate of three node the rate of three node

<!-- b000222 | prose | pages [6] -->
60 60

<!-- b000223 | prose | pages [6] -->
X: 62.19 Y: 50.3

<!-- b000224 | prose | pages [6] -->
50 50

<!-- b000225 | prose | pages [6] -->
40 40

<!-- b000226 | prose | pages [6] -->
30 30

<!-- b000227 | prose | pages [6] -->
20 20

<!-- b000228 | prose | pages [6] -->
X: 50.62 Y: 9.897

<!-- b000229 | prose | pages [6] -->
10 10

<!-- b000230 | furniture | pages [6] -->


<!-- b000231 | furniture | pages [6] -->


<!-- b000232 | prose | pages [6] -->
0 0 0 0 10 20 30 40 50 60 70 80 90 100

<!-- b000233 | prose | pages [6] -->
time/days

<!-- b000234 | caption | pages [6] -->
Figure 5: 1960

<!-- b000235 | caption | pages [6] -->
Figure 6: 1996

<!-- b000236 | prose | pages [6] -->
The simulation results show that,the number of individuals who have known the informa- tion is increasing,and the proportion of susceptible nodes is decreasing over time.If the time is long enough, information can spread throughout the entire network.By contrast,we can know that the average contact rate of infected nodes increases gradually,which shortens the period of information dissemination and expands the scope of information dissemination.

<!-- b000237 | prose | pages [6] -->
In conclusion,the improved information transmission model can reveal the inherent law of information transmission in social network more accurately.

<!-- b000238 | furniture | pages [7] -->
Team # 44173

<!-- b000239 | prose | pages [7] -->
100

<!-- b000240 | prose | pages [7] -->
90

<!-- b000241 | prose | pages [7] -->
Susceptible individuals Recovered individuals

<!-- b000242 | prose | pages [7] -->
80

<!-- b000243 | prose | pages [7] -->
Infected individuals

<!-- b000244 | prose | pages [7] -->
70

<!-- b000245 | prose | pages [7] -->
the rate of three node

<!-- b000246 | prose | pages [7] -->
60

<!-- b000247 | prose | pages [7] -->
50

<!-- b000248 | prose | pages [7] -->
40

<!-- b000249 | prose | pages [7] -->
30

<!-- b000250 | prose | pages [7] -->
20

<!-- b000251 | prose | pages [7] -->
10

<!-- b000252 | furniture | pages [7] -->


<!-- b000253 | prose | pages [7] -->
0 0 10 20 30 40

<!-- b000254 | furniture | pages [7] -->
Page 7 of 22

<!-- b000255 | furniture | pages [7] -->


<!-- b000256 | prose | pages [7] -->
X: 62.08 Y: 50.3

<!-- b000257 | prose | pages [7] -->
X: 50.74 Y: 10.3

<!-- b000258 | prose | pages [7] -->
50 50 60 70 80 90 100

<!-- b000259 | prose | pages [7] -->
time/days

<!-- b000260 | caption | pages [7] -->
Figure 7: 2012

<!-- b000261 | heading | pages [7] -->
Rationality validation And Sensitivity analysis

<!-- b000262 | prose | pages [7] -->
3.2.2

<!-- b000263 | prose | pages [7] -->
In order to illustrate the model better , we investigate Facebook data and get the latest Facebook data on DMR website.Total number of Facebook daily active users is 1038 billionˇcˇn26.7 per- cent of the Internet users in the US. that clicked a Facebook share button on blog posts they enjoyed.General users has 245 friends in average.Model parameters can be determined by the conditions and the initial value is as follows: λ1 = 1000, λ2 = 245, µ = 73.3%, i0 = 5 × 10 −7, i(0) = 0, s0 = 1, r(0) = 0, we use Matlab to solve the Differential equations and get the ﬁgures of the change trend of the proportion of three kinds of nodes in Facebook.It can be seen that:

<!-- b000264 | prose | pages [7] -->
More than half of the users has received the message In less than 7 days.After ten days, about 70% of the users in the network have get the message.Eventually the ratios of the number of three kinds of nodes achieve stable.

<!-- b000265 | prose | pages [7] -->
The Inﬂuence of Parameters on the Information Dissemination 1.Contact rates of hot transmission nodes By changing the daily contact rate of hot transmission nodes in social network,we can ﬁnd the result in Figure5,After contrast,we know that with the increase of average daily contact rate of transmission nodes,the period of information dissemination has been shortened and the scope of information dissemination has been expanded.

<!-- b000266 | prose | pages [7] -->
100

<!-- b000267 | prose | pages [7] -->
80

<!-- b000268 | prose | pages [7] -->
60

<!-- b000269 | prose | pages [7] -->
X: 7.155

<!-- b000270 | prose | pages [7] -->
the rate of three node

<!-- b000271 | prose | pages [7] -->
Y: 49.99

<!-- b000272 | prose | pages [7] -->
40

<!-- b000273 | prose | pages [7] -->
20

<!-- b000274 | prose | pages [7] -->
X: 6.131 Y: 10.09

<!-- b000275 | prose | pages [7] -->
0

<!-- b000276 | furniture | pages [7] -->


<!-- b000277 | prose | pages [7] -->
−20 0 5

<!-- b000278 | furniture | pages [7] -->


<!-- b000279 | prose | pages [7] -->
Susceptible individuals Recovered individuals Infected individuals

<!-- b000280 | prose | pages [7] -->
10 15 20

<!-- b000281 | prose | pages [7] -->
time/days

<!-- b000282 | caption | pages [7] -->
Figure 8: facebook

<!-- b000283 | furniture | pages [8] -->
Team # 44173

<!-- b000284 | furniture | pages [8] -->


<!-- b000285 | prose | pages [8] -->
100

<!-- b000286 | prose | pages [8] -->
100

<!-- b000287 | prose | pages [8] -->
Susceptible individuals Recovered individuals Infected individuals

<!-- b000288 | prose | pages [8] -->
80

<!-- b000289 | prose | pages [8] -->
80

<!-- b000290 | prose | pages [8] -->
60

<!-- b000291 | prose | pages [8] -->
60

<!-- b000292 | prose | pages [8] -->
X: 7.825

<!-- b000293 | prose | pages [8] -->
the rate of three node

<!-- b000294 | prose | pages [8] -->
the rate of three node

<!-- b000295 | prose | pages [8] -->
Y: 50.19

<!-- b000296 | prose | pages [8] -->
40

<!-- b000297 | prose | pages [8] -->
40

<!-- b000298 | prose | pages [8] -->
20

<!-- b000299 | prose | pages [8] -->
20

<!-- b000300 | prose | pages [8] -->
X: 6.516 Y: 10.04

<!-- b000301 | prose | pages [8] -->
0

<!-- b000302 | prose | pages [8] -->
0

<!-- b000303 | furniture | pages [8] -->


<!-- b000304 | furniture | pages [8] -->


<!-- b000305 | prose | pages [8] -->
−20

<!-- b000306 | prose | pages [8] -->
−20

<!-- b000307 | prose | pages [8] -->
0 5 10 15 20

<!-- b000308 | prose | pages [8] -->
0 5

<!-- b000309 | prose | pages [8] -->
time/days

<!-- b000310 | furniture | pages [8] -->
Page 8 of 22

<!-- b000311 | furniture | pages [8] -->


<!-- b000312 | furniture | pages [8] -->


<!-- b000313 | prose | pages [8] -->
100

<!-- b000314 | prose | pages [8] -->
Susceptible individuals

<!-- b000315 | prose | pages [8] -->
Susceptible individuals

<!-- b000316 | prose | pages [8] -->
Recovered individuals

<!-- b000317 | prose | pages [8] -->
Recovered individuals

<!-- b000318 | prose | pages [8] -->
Infected individuals

<!-- b000319 | prose | pages [8] -->
Infected individuals

<!-- b000320 | prose | pages [8] -->
80

<!-- b000321 | prose | pages [8] -->
60

<!-- b000322 | prose | pages [8] -->
X: 7.542 X: 7.542

<!-- b000323 | prose | pages [8] -->
X: 6.928

<!-- b000324 | prose | pages [8] -->
the rate of three node

<!-- b000325 | prose | pages [8] -->
Y: 50.07 Y: 50.07

<!-- b000326 | prose | pages [8] -->
Y: 50.05

<!-- b000327 | prose | pages [8] -->
40

<!-- b000328 | prose | pages [8] -->
20

<!-- b000329 | prose | pages [8] -->
X: 5.902 Y: 10.03

<!-- b000330 | prose | pages [8] -->
0

<!-- b000331 | furniture | pages [8] -->


<!-- b000332 | prose | pages [8] -->
−20

<!-- b000333 | prose | pages [8] -->
10 10 15 20

<!-- b000334 | prose | pages [8] -->
0 5 10 15 20

<!-- b000335 | prose | pages [8] -->
time/days

<!-- b000336 | prose | pages [8] -->
time/days

<!-- b000337 | caption | pages [8] -->
Figure 9: λ1 = 300

<!-- b000338 | caption | pages [8] -->
Figure 10: λ1 = 500

<!-- b000339 | caption | pages [8] -->
Figure 11: λ1 = 1500

<!-- b000340 | furniture | pages [8] -->


<!-- b000341 | prose | pages [8] -->
100

<!-- b000342 | prose | pages [8] -->
Susceptible individuals Recovered individuals Infected individuals

<!-- b000343 | prose | pages [8] -->
80

<!-- b000344 | prose | pages [8] -->
60

<!-- b000345 | prose | pages [8] -->
X: 16.29

<!-- b000346 | prose | pages [8] -->
the rate of three node

<!-- b000347 | prose | pages [8] -->
Y: 50.4

<!-- b000348 | prose | pages [8] -->
40

<!-- b000349 | prose | pages [8] -->
20

<!-- b000350 | prose | pages [8] -->
0

<!-- b000351 | furniture | pages [8] -->


<!-- b000352 | prose | pages [8] -->
−20 0 10 20 30 40 50

<!-- b000353 | prose | pages [8] -->
time/days

<!-- b000354 | furniture | pages [8] -->


<!-- b000355 | prose | pages [8] -->
100

<!-- b000356 | prose | pages [8] -->
Susceptible individuals Recovered individuals Infected individuals

<!-- b000357 | prose | pages [8] -->
80

<!-- b000358 | prose | pages [8] -->
60

<!-- b000359 | prose | pages [8] -->
X: 4.555

<!-- b000360 | prose | pages [8] -->
the rate of three node

<!-- b000361 | prose | pages [8] -->
Y: 50.01

<!-- b000362 | prose | pages [8] -->
40

<!-- b000363 | prose | pages [8] -->
20

<!-- b000364 | prose | pages [8] -->
0

<!-- b000365 | furniture | pages [8] -->


<!-- b000366 | prose | pages [8] -->
−20 0 5 10 15 20

<!-- b000367 | prose | pages [8] -->
time/days

<!-- b000368 | caption | pages [8] -->
Figure 12: λ2 = 100

<!-- b000369 | caption | pages [8] -->
Figure 13: λ2 = 400

<!-- b000370 | prose | pages [8] -->
2.The Probability of the Immune By changing the probability of the immune,we can ﬁnd the result in pictures as bellow. The probability of the immune can impact the period of information dissemination,too.Reducing the probability of the immune can speed up the information transmission and shorten the pe- riod of information dissemination.

<!-- b000371 | prose | pages [8] -->
3.3 Prediction

<!-- b000372 | prose | pages [8] -->
We carry out the multiple regression analysis on data and make predictions,and get general changes of daily contact rate for each media.Figure14

<!-- b000373 | prose | pages [8] -->
With the changes of The times and the emergence of kinds of media,the proportion of each medium also changes over time.as is shown in Figure15

<!-- b000374 | prose | pages [8] -->
Considering the tendency of different media and changes of the way people get their news,combining with relevant information and data.We can ﬁnd that:

<!-- b000375 | furniture | pages [9] -->
Team # 44173

<!-- b000376 | furniture | pages [9] -->


<!-- b000377 | prose | pages [9] -->
100

<!-- b000378 | prose | pages [9] -->
Susceptible individuals Recovered individuals Infected individuals

<!-- b000379 | prose | pages [9] -->
80

<!-- b000380 | prose | pages [9] -->
60

<!-- b000381 | prose | pages [9] -->
the rate of three node

<!-- b000382 | prose | pages [9] -->
X: 11.36 Y: 34.84

<!-- b000383 | prose | pages [9] -->
40

<!-- b000384 | prose | pages [9] -->
20

<!-- b000385 | prose | pages [9] -->
0

<!-- b000386 | prose | pages [9] -->
X: 5.328 Y: 0.5121

<!-- b000387 | furniture | pages [9] -->


<!-- b000388 | prose | pages [9] -->
−20 0 5 10 15 20

<!-- b000389 | prose | pages [9] -->
time/days

<!-- b000390 | furniture | pages [9] -->
Page 9 of 22

<!-- b000391 | furniture | pages [9] -->


<!-- b000392 | prose | pages [9] -->
100

<!-- b000393 | prose | pages [9] -->
Susceptible individuals Recovered individuals Infected individuals

<!-- b000394 | prose | pages [9] -->
80

<!-- b000395 | prose | pages [9] -->
60

<!-- b000396 | prose | pages [9] -->
the rate of three node

<!-- b000397 | prose | pages [9] -->
40

<!-- b000398 | prose | pages [9] -->
X: 8.459 Y: 14.84

<!-- b000399 | prose | pages [9] -->
20

<!-- b000400 | prose | pages [9] -->
0

<!-- b000401 | prose | pages [9] -->
X: 4.541 Y: 0.4047

<!-- b000402 | furniture | pages [9] -->


<!-- b000403 | prose | pages [9] -->
−20 0 5 10 15 20

<!-- b000404 | prose | pages [9] -->
time/days

<!-- b000405 | caption | pages [9] -->
Figure 14: µ = 0.65

<!-- b000406 | caption | pages [9] -->
Figure 15: µ = 0.85

<!-- b000407 | caption | pages [9] -->
Figure 16: Change of Daily Contact Rate

<!-- b000408 | prose | pages [9] -->
1.Before the 19th century, the newspaper is the main access to gain news, and around 1950, the radio has a majority of users,.The data changes again in 1980, TV at this time holds the leading position.After that,the number of users of mobile phones, and the Internet is constantly rising.Besides,after 2000, the number rises quickly and clearly, and the Internet and the mobile phone gradually become the main tools to get news and messages in people’s daily lives.

<!-- b000409 | prose | pages [9] -->
2.Users of newspapers, radio and television have decreased constantly.But in recent years the pace of decline has gradually slowed down.But after 2020, with the popularity of the Internet, the users number will tend to be saturated, although there is still a rising trend, but the rise has slowed.

<!-- b000410 | prose | pages [9] -->
In the case of 2050, we take the predict data into information ˛a´rs ﬂow model, the situation of the information ﬂow is shown as follows.

<!-- b000411 | prose | pages [9] -->
When only consider the changes of average daily contact rate of average daily contact rate,we can see that:

<!-- b000412 | furniture | pages [10] -->
Team # 44173

<!-- b000413 | furniture | pages [10] -->
Page 10 of 22

<!-- b000414 | caption | pages [10] -->
Figure 17: Change of The Proportion of Daily Contact Rate

<!-- b000415 | prose | pages [10] -->
100

<!-- b000416 | prose | pages [10] -->
90

<!-- b000417 | prose | pages [10] -->
80

<!-- b000418 | prose | pages [10] -->
70

<!-- b000419 | prose | pages [10] -->
the rate of three node

<!-- b000420 | prose | pages [10] -->
60

<!-- b000421 | prose | pages [10] -->
50

<!-- b000422 | prose | pages [10] -->
40

<!-- b000423 | prose | pages [10] -->
30

<!-- b000424 | prose | pages [10] -->
20

<!-- b000425 | prose | pages [10] -->
10

<!-- b000426 | furniture | pages [10] -->


<!-- b000427 | prose | pages [10] -->
0 0 20 40

<!-- b000428 | furniture | pages [10] -->


<!-- b000429 | prose | pages [10] -->
Susceptible individuals Recovered individuals Infected individuals

<!-- b000430 | prose | pages [10] -->
60 60 80 100 120

<!-- b000431 | prose | pages [10] -->
time/days

<!-- b000432 | caption | pages [10] -->
Figure 18: 2050

<!-- b000433 | prose | pages [10] -->
1.Compared with 2012,the speed of news propagation will keep going up in 2050.In less than 40 days,almost half of the people can acquire the news when it happens.While in 2012,nearly half of the people learn a message in 50 days.The speed of information transmission increased by about 25%.

<!-- b000434 | prose | pages [10] -->
2.The transmission of the message gets into its stride at the 20th day in 2012.While in 2050,the transmission of the message starts at the 10th day.In 2050, by contrast, the begining of the trans- mission will be in advance,which is another sign of increasing of the information transmission speed.

<!-- b000435 | prose | pages [10] -->
3.In 2012,the spread of information cycle lasts about 60 days,while in 2050,The spread of infor- mation cycle lasts about only 50 days,which means that in the same length of time, the amount of messages people contact will increase.And this portends that information capacity will be constantly increasing,with the development of communication tools .

<!-- b000436 | prose | pages [10] -->
From 2000,the number of people using social networks has increased,and the contact rate of ordinary nodes has changed,too.Ordinary nodes have more opportunity to change into hot transmission nodes,resulting to the proportion of hot transmission nodes in the whole heat has increased.So we boost the number of hot transmission nodes and the contact rate of ordinary nodes.The model adjusted is as follow:

<!-- b000437 | furniture | pages [11] -->
Team # 44173

<!-- b000438 | prose | pages [11] -->
100

<!-- b000439 | prose | pages [11] -->
80

<!-- b000440 | prose | pages [11] -->
60

<!-- b000441 | prose | pages [11] -->
the rate of three node

<!-- b000442 | prose | pages [11] -->
40

<!-- b000443 | prose | pages [11] -->
20

<!-- b000444 | prose | pages [11] -->
0

<!-- b000445 | furniture | pages [11] -->


<!-- b000446 | prose | pages [11] -->
−20 0 10 20 30 40

<!-- b000447 | furniture | pages [11] -->
Page 11 of 22

<!-- b000448 | furniture | pages [11] -->


<!-- b000449 | prose | pages [11] -->
Susceptible individuals Recovered individuals Infected individuals

<!-- b000450 | prose | pages [11] -->
50 60 70 80 90 100

<!-- b000451 | prose | pages [11] -->
time/days

<!-- b000452 | caption | pages [11] -->
Figure 19: 2050

<!-- b000453 | prose | pages [11] -->
Compare two results, the information transmission will accelerate again,and the transmis- sion cycle will shorten again.Owing to this,information will exist in a shorter time, and a lot of information will become a fast-good-type messages,which is a kind of portrayal of real life.

<!-- b000454 | heading | pages [11] -->
A Model of Information Filtering

<!-- b000455 | prose | pages [11] -->
4

<!-- b000456 | prose | pages [11] -->
4.1

<!-- b000457 | heading | pages [11] -->
Model Description

<!-- b000458 | prose | pages [11] -->
The purpose of information ﬁltering is to extract the information as news.Essentially, infor- mation ﬁltering is a classiﬁcation problem. We propose a radial basis function network(RBF) model[4]. In order to solve the samples noise and computing performance, we decide to use K-means algorithm and RLS algorithm implement network. We demonstrate our model using online news dataset.

<!-- b000459 | prose | pages [11] -->
Hybrid Learning Procedure For Networks 4.2

<!-- b000460 | prose | pages [11] -->
we develop a hybrid learning procedure for RBF networks. First,we use K-means algorithm to train hidden layer. And then, RLS algorithm is checked to train output layer. We call The hybrid learning procedure as “”K-means RLS “”algorithm. The algorithm is divided to three steps:

<!-- b000461 | prose | pages [11] -->
• Input layer. The size of input layer is determined by the dimensionality of input vector x, which is denoted by m0.

<!-- b000462 | prose | pages [11] -->
• Hidden layer. 1. The size of the hidden layer ,m1 is determined by the proposed number of clusters,

<!-- b000463 | furniture | pages [12] -->
Team # 44173

<!-- b000464 | furniture | pages [12] -->
Page 12 of 22

<!-- b000465 | prose | pages [12] -->
K. Indeed, the parameter K may by viewed as a degree of freedom under the design- er ˛a´rs control. As such, the parameter K holds the key to the model-selection problem and thereby controls not only the performance, but also computational complexity of network.

<!-- b000466 | heading | pages [12] -->
2. The cluster mean ˆµj,computed by the K-means algorithm working on the unlabeled

<!-- b000467 | prose | pages [12] -->
sample xiN

<!-- b000468 | prose | pages [12] -->
i=1 of input vectors, determines the center xj in the Gaussian function φ(·, xj) assigned to the hidden unit j = 1, 2, · · · , k. 3. To simplify the design ,the same width, denoted by σ,is assigned to all the Gaussian functions in accordance with the spread of the centers discovered by the K-means algo- rithm ,as shown by

<!-- b000469 | prose | pages [12] -->
σ = dmax √

<!-- b000470 | prose | pages [12] -->
2K

<!-- b000471 | prose | pages [12] -->
,where K is the number of centers and dmax is the maximum distance between them. This formula ensures that the individual Gaussian units are not too peaked or too ﬂat;both extreme conditions should be avoided in practice.

<!-- b000472 | prose | pages [12] -->
• Output layer. Once the training of the hidden layer is completed, the training of the output layer can begin. Let the K × 1 vector.

<!-- b000473 | prose | pages [12] -->
φ(x) =

<!-- b000474 | prose | pages [12] -->
 

<!-- b000475 | prose | pages [12] -->


<!-- b000476 | prose | pages [12] -->
ϕ(xi, x1) ϕ(xi, x2)

<!-- b000477 | prose | pages [12] -->
 

<!-- b000478 | prose | pages [12] -->
 (3)

<!-- b000479 | prose | pages [12] -->
 

<!-- b000480 | prose | pages [12] -->


<!-- b000481 | prose | pages [12] -->
...

<!-- b000482 | prose | pages [12] -->
 

<!-- b000483 | prose | pages [12] -->


<!-- b000484 | prose | pages [12] -->
 

<!-- b000485 | prose | pages [12] -->


<!-- b000486 | prose | pages [12] -->
ϕ(xi, xK)

<!-- b000487 | prose | pages [12] -->
denote the outputs of the K units in the hidden layer. This vector is produced in response to the stimulus xi, i = 1, 2, , N. Thus, insofar as the supervised training of the output layer is concerned,the training sample is deﬁned by

<!-- b000488 | prose | pages [12] -->
Φ(i), d(i)N

<!-- b000489 | prose | pages [12] -->
i=1

<!-- b000490 | prose | pages [12] -->
,where di is desired response at the overall output of the RBF network for input xi,This training is carried out using the RLS algorithm. Once the network training is completed, testing of the whole network with data not seen before can begin.

<!-- b000491 | furniture | pages [13] -->
Team # 44173

<!-- b000492 | furniture | pages [13] -->
Page 13 of 22

<!-- b000493 | prose | pages [13] -->
4.3 Experiment

<!-- b000494 | prose | pages [13] -->
We demonstrate out model in online news dataset[5].we pre-process dataset in term of ﬁlter Unnecessary factors. Our dataset is divided to two class , the number of shares more than 1400 is considered signiﬁcant ˛a ˛a information. The number of information is 39240,we train our net- work using 27908 information, and then test with 11332 information.The considering factors as follows, 1) Days between the article publication and the dataset acquisition(non-predictive). 2) Number of words in the title. 3) Number of words in the content. 4) Number of images. 5) Number of videos. 6) Number of keywords in the metadata. 7) Data channel: lifestyle, entertainment , business, social media,tech,world. 8) Was the article published on the weekend? 9) Number of shares

<!-- b000495 | prose | pages [13] -->
The results of our network is given in table: Accuracy in train procedure is 75.1%.

<!-- b000496 | prose | pages [13] -->
4.4 Sensitively Analysis

<!-- b000497 | prose | pages [13] -->
We draw a ROC curve graph to verify the sensitively of our network. The curve can cover most area. It indicate our network is sensitive. In order to validate the stability of our network ˇcˇnwe test our network in our dataset. The re- sults is given in table as above. Accuracy in test procedure is 74.3%.The results show that out model can adapt to data-change, and ﬁlter information as news.

<!-- b000498 | prose | pages [13] -->
4.5

<!-- b000499 | heading | pages [13] -->
Conclusion

<!-- b000500 | prose | pages [13] -->
The RBF network adopt “”K-means RLS“” algorithm, which can improve the performance of computing. This algorithm has two characteristics: computational simplicity and acceleration

<!-- b000501 | furniture | pages [14] -->
Team # 44173

<!-- b000502 | furniture | pages [14] -->
Page 14 of 22

<!-- b000503 | prose | pages [14] -->
convergence. The only suspect is the lack of the training of hidden layer and the training of output layer combined with the most criteria, which in the statistical sense to ensure the entire system of optimality. The only thing to doubt is not to p=optimize the training of hidden layer and output layer, so as to ensure the optimality of whole system in statistics. Using RBF network ,we can implement our information ﬁltering efﬁciently.

<!-- b000504 | prose | pages [14] -->
5

<!-- b000505 | heading | pages [14] -->
A SN-SIR Model

<!-- b000506 | prose | pages [14] -->
To solve the problem of how public interest and opinion can be changed through information networks in the Internet,we model of social network mainly about public opinion based on SIR and complex network theory,and then we text the model performance by FaceBook’s social network datasets.

<!-- b000507 | prose | pages [14] -->
5.1 The Way of Information Dissemination in Network

<!-- b000508 | prose | pages [14] -->
In the social network ,the relationship between the user can be established only by both sides of the identity authentication .[7] So social network can be thought of as net which does not has directions and weight and use the users and the relation ship between users replaces nodes and edges,and topics or news spread along the edges.[8]

<!-- b000509 | caption | pages [14] -->
Figure 20: The way of Public Opinion Dissemination in Social Network

<!-- b000510 | prose | pages [14] -->
5.2

<!-- b000511 | heading | pages [14] -->
A Model of Public Opinion Dissemination in Social Network

<!-- b000512 | prose | pages [14] -->
we classify nodes into three types as same as we deﬁne above,and assume that all nodes are susceptible in the beginning,but adding or changing some deﬁnition of factors are as follows.

<!-- b000513 | prose | pages [14] -->
• 1)Psi is the rate of probability of node in state s turn to Node in state i when s contacts with i.

<!-- b000514 | furniture | pages [15] -->
Team # 44173

<!-- b000515 | furniture | pages [15] -->
Page 15 of 22

<!-- b000516 | prose | pages [15] -->
• 2)α is the rate of probability of node s turned to node i when s gets some public opinions but does not contact with i.

<!-- b000517 | prose | pages [15] -->
• 3)Pir is the rate of probability of node i turn to node r in state r when node i lose s interest about a public opinion and stops spreading the public opinion.

<!-- b000518 | prose | pages [15] -->
• 4)Psr is the rate of probability of node s trun to node r when s gets a public opinion it is not interested in and dose not want to spread the public opinion.

<!-- b000519 | prose | pages [15] -->
• 5)k is the degree value of each node.

<!-- b000520 | prose | pages [15] -->
5.2.1

<!-- b000521 | heading | pages [15] -->
Model Building

<!-- b000522 | prose | pages [15] -->
It is a kind of dynamic procedure when we refer to the spread of social networking topic. Propaga of topic is inﬂuenced by one or more factors . The spread when a node in social net- work want to spread some opinions will be inﬂuenced by the ability of neighboring nodes. The greater the degree of spread of nodes,the better to public opinion spread in the network. Make a conclusion about the above knowable,and we get the model of node state transition in social network.[6]

<!-- b000523 | prose | pages [15] -->
On the basis of model of node state transition and theory about SIR,we build the public opin-

<!-- b000524 | prose | pages [15] -->
ion transmission model in the social network is as followsˇcž

<!-- b000525 | prose | pages [15] -->
ds(k,t)

<!-- b000526 | prose | pages [15] -->


<!-- b000527 | prose | pages [15] -->
= −psiks(k, t)θt −αs(k, t) −psrs(k, t) dt

<!-- b000528 | prose | pages [15] -->
      

<!-- b000529 | prose | pages [15] -->
di(k,t)

<!-- b000530 | prose | pages [15] -->


<!-- b000531 | prose | pages [15] -->
= psiksk, tθt + αs(k, t) −pirs(k, t)

<!-- b000532 | prose | pages [15] -->
 

<!-- b000533 | prose | pages [15] -->
dt

<!-- b000534 | prose | pages [15] -->
 

<!-- b000535 | prose | pages [15] -->
(4)

<!-- b000536 | prose | pages [15] -->
dr(k,t)

<!-- b000537 | prose | pages [15] -->


<!-- b000538 | prose | pages [15] -->
= psrsk, t + pirik, t

<!-- b000539 | prose | pages [15] -->
 

<!-- b000540 | prose | pages [15] -->
dt

<!-- b000541 | prose | pages [15] -->
       

<!-- b000542 | prose | pages [15] -->
s(k, t) + i(k, t) + r(k, t) = 1

<!-- b000543 | prose | pages [15] -->


<!-- b000544 | furniture | pages [16] -->
Team # 44173

<!-- b000545 | furniture | pages [16] -->
Page 16 of 22

<!-- b000546 | prose | pages [16] -->
In the above equation,θ(t) signiﬁes the probability of any edges can contact with nodes in state i at time of t,and its equation is as follows:

<!-- b000547 | prose | pages [16] -->
P

<!-- b000548 | prose | pages [16] -->
k kP(k)i(k, t)

<!-- b000549 | prose | pages [16] -->
θ(t) =

<!-- b000550 | prose | pages [16] -->
(5) < k >

<!-- b000551 | prose | pages [16] -->
In the above equation,P(k) is the degree distribution function of social networksˇc˙z< k > is the average node degree of social networks.

<!-- b000552 | prose | pages [16] -->
5.3

<!-- b000553 | heading | pages [16] -->
Sensitivity Analysis and Model Validation

<!-- b000554 | prose | pages [16] -->
5.3.1

<!-- b000555 | heading | pages [16] -->
Model Validation

<!-- b000556 | prose | pages [16] -->
In order to validate the efﬁciency of public opinion topic transmission model which we pro- posed,we choose the standard data sets -“” Facebook social network dataset“”which includes 4039 nodes and 88234 sides to carry on our simulation experiment.[9] 1. The relation between the density of different nodes over time Assuming that there is only one communication node in the network and the rest areall nodes in state s .Set the total pa- rameters of ( 1 ) as follows : the external infection probability Psi = 0.4; the internal infection probability α = 0.3; the immune probability Pir = 0.2; the direct immune probability Psr = 0.1. The change relation between the density of each node and the spread of public opinion topic is shown in ﬁgure 3.From pictures below:

<!-- b000557 | furniture | pages [17] -->
Team # 44173

<!-- b000558 | furniture | pages [17] -->
Page 17 of 22

<!-- b000559 | prose | pages [17] -->
we can see: The density of the susceptible nodes have a tendency to attenuate until it is close to zero.The density of transmission node have a rapid growth in the initial stage,and it will decline rapidly after its peak until its tendency to zero.While the density of the immune node shows a quick growth at the beginning of the diffusion of a topic.It will become stable gradually after its peak and tend to be 1 in the end. We can draw the conclusions as follows after our parameter veriﬁcation of the social network.

<!-- b000560 | prose | pages [17] -->
• 1.Generally speaking ,the higher the value of an information is,the lower immunisation rates of the information will be ,the higher the internal infection rate will be.

<!-- b000561 | prose | pages [17] -->
There will be more transmission nodes and less immune nodes in a short transmission-cycle time.Which means the more quickly the information spread,the more widely the range of users will cover.

<!-- b000562 | prose | pages [17] -->
• 2.User ˛a´rs interests and prejudices can react on the immune probability and the infection rate,the higher the user’s interests in the message is,the lower the corresponding immune probability and direct immune immunisation rates will be ,and the infection rate will rise accordingly, when the message comes to the user, the speed of the spread will be faster, and as for a message, the more uses are interested in, the lower the corresponding im- munity will be,the more people infected will be,the more transmission nodes will be, the faster the news propagation speed will be ,that is to say,the transmission will be faster if it owns more users interested in.

<!-- b000563 | prose | pages [17] -->
5.3.2

<!-- b000564 | heading | pages [17] -->
Sensitivity, parameter validation analysis

<!-- b000565 | prose | pages [17] -->
1.The inﬂuence of Psi When Psi is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as followsˇcž

<!-- b000566 | prose | pages [17] -->
(1)Before the Internet reach steady state, with the increase of Psi ,the density about nodes in state s is growth,but the density about nodes in state r is go down.The reason about this is the greater of Psi ,the more number of nodes in state i transform into nodes in state sˇc˙z

<!-- b000567 | prose | pages [17] -->
(2)With the increase of Psi ,the time of The spread of social network public opinion reaches a steady state is more longer.

<!-- b000568 | prose | pages [17] -->
(3)When Psi=0, social network information can still be propagated,this is different with pre- vious research results.The reason about this is the connectivity of social networks is higher when it compare with traditional network and social network user can get public opinion from each other and other mode.

<!-- b000569 | prose | pages [17] -->
2,The inﬂuence of Pir When Pir is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as followsˇcž (1) When Pir >0, before the Internet reach steady state, Pir and the density about nodes in state s against each other and found a negative correlation,but Pir and the density about nodes in state r found a positive correlation.So,the value of Pir is greater,the rate of probability of nodes

<!-- b000570 | furniture | pages [18] -->
Team # 44173

<!-- b000571 | furniture | pages [18] -->
Page 18 of 22

<!-- b000572 | prose | pages [18] -->
in state i turn to state r is higher.

<!-- b000573 | prose | pages [18] -->
(2) When Pir =0, Pir increase rapidly in the early,gradually stabilized after get to the peak .The reason about this is when Pir =0, nodes in state I Will always keep their state and do not switch to the state r.However,the density about nodes in stater !=0 because of the inﬂuence of Psr and some nodes in state s turn to stater.

<!-- b000574 | prose | pages [18] -->
3,The inﬂuence of α When α is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as follows.The ﬁgure shows that before the Internet reach steady state,as long as the value of˛eÁ- further increase, the density about nodes in state i increases correspondingly,but the density about nodes in state r decrease all the time.This is mainly because the value of α is greater,the rate of probability of nodes in state s turn to state i is higher.

<!-- b000575 | prose | pages [18] -->
4,The inﬂuence of Psr When Psr is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as follows.The ﬁgure shows that with the increase of Psr,the density about nodes in state r is growth,but the density about nodes in state i is go down. This is mainly because the value of Psr is greater,the rate of probability of nodes in state s turn to state r directly without turn to state i is higher.

<!-- b000576 | prose | pages [18] -->
5,The inﬂuence of initial nodes degree k0 When k0 is changed ,the variation trend of den-

<!-- b000577 | furniture | pages [19] -->
Team # 44173

<!-- b000578 | furniture | pages [19] -->
Page 19 of 22

<!-- b000579 | prose | pages [19] -->
sity ﬂuctuation about nodes in state s is as follows.And we can know that the value of k0 is greater,the speed of public opinion propagation is faster in social network.

<!-- b000580 | prose | pages [19] -->
6,The inﬂuence of different node density changes over time When the density about nodes in state s,i and r is changed, public opinion evolution trend over time is as follows.From the picture,we can kown that, no matter how the density about nodes in state s,i and r change with time, public opinion evolution trend are basically identical. This shows that the different value of nodes has similar behavior characteristics.

<!-- b000581 | furniture | pages [20] -->
Team # 44173

<!-- b000582 | furniture | pages [20] -->
Page 20 of 22

<!-- b000583 | prose | pages [20] -->
5.4

<!-- b000584 | heading | pages [20] -->
Result Analysis

<!-- b000585 | prose | pages [20] -->
Using social network dataset to validate the patameters , we can draw the conclusions as fol- lows. (1)Generally speaking ,the higher the value of an information is , the lower immune probability of the information will be ,the higher the internal infection probability will be. There will be more nodes in state s and less nodes in state r in a short transmission-cycle time , which means the more quickly the information spread, the more widely the range of users will cover.

<!-- b000586 | prose | pages [20] -->
(2)User ˛a´rs interests and prejudices can react on the immune probability and the infection rate .The higher the user’s interests in the message is , the lower the corresponding immune prob- ability and direct immune rates will be ,and the infection rate will rise accordingly, when the message comes to the user, the speed of the spread will be faster, and as for a message, the more uses are interested in, the lower the corresponding immunity will be , and the more people in- fected will be , the more transmission nodes will be, the faster the news propagation speed will be ,that is to say , the transmission will be faster if it owns more users interested in.

<!-- b000587 | prose | pages [20] -->
(3)In social network ,the source of the message can be divided into hot transmission nodes and normal transmission nodes as we discussed in the information ﬂow model. Hot trans- mission nodes have larger infection rate and degree of value ,but normal transmission nodes that infection rate is lesser, degree of value is smaller than hot transmission nodes. Consider- ing the inﬂuence of parameters, we parsed on the information dissemination model, when the news that come from hot transmission nodes have faster transmission speed and wider scope of news than ordinary nodes.

<!-- b000588 | prose | pages [20] -->
(4) Using degree value of the nodes describes the different network topology and strength . Through transformation analysis of parameters, the degree of initial node in social networks

<!-- b000589 | furniture | pages [21] -->
Team # 44173

<!-- b000590 | furniture | pages [21] -->
Page 21 of 22

<!-- b000591 | prose | pages [21] -->
have an obvious impact on public opinion propagation velocity , and different nodes ˛a˝o distri- bution has a small impact.

<!-- b000592 | prose | pages [21] -->
6 Analysis

<!-- b000593 | prose | pages [21] -->
6.1

<!-- b000594 | heading | pages [21] -->
Strengths

<!-- b000595 | prose | pages [21] -->
• Our model invokes and expand the classical SIR model. We take times ,Medium inﬂuence into consideration and develop a SIIR model to solve information ﬂow problem. the external infection rate is taken into account.In order to adapt internet information ﬂow,we propose a SIR model that base on social network in internet.

<!-- b000596 | prose | pages [21] -->
• The solving processing and solution is stable.

<!-- b000597 | prose | pages [21] -->
• The result of out model is visible and easy to understand. We demonstrate our model using data, and the result can be understand from the exper- iments. Consequently , anyone can comprehend the evaluation without any background knowledge.

<!-- b000598 | prose | pages [21] -->
• Our model has a strong sense of professional background. Our model based on both subjective and objective methods solve the information ﬂow , information ﬁltering ,and ﬁnd the factors of inﬂuence information ﬂow.

<!-- b000599 | prose | pages [21] -->
• Our model can be extended into higher dimension. As an information ﬁltering system can extend to take more dimension factors ,and then using our model to ﬁlter the information. Our model can explain the sustainability in a more explicit way.

<!-- b000600 | prose | pages [21] -->
• The dynamic prediction can be easily tracked. The mechanism of our system dynamic offers handy to predict information ﬂow and capacity.

<!-- b000601 | prose | pages [21] -->
6.2

<!-- b000602 | heading | pages [21] -->
Weaknesses

<!-- b000603 | heading | pages [21] -->
• The model does not take platformsˇcˇnnetwork complexityˇcˇnRegion inﬂuenceˇcˇngovern-

<!-- b000604 | prose | pages [21] -->
ment control and other factors into consider. The model cannot accurately forecast information ﬂow between different region or plat- form, thus the sustainability is not necessarily exact in terms of some uncontrollable fac- tors.

<!-- b000605 | prose | pages [21] -->
• The statistical date used in implementing of model not complete achievable. We cannot ﬁnd all data we required for sustainability.

<!-- b000606 | prose | pages [21] -->
Fortunately, ICM‘’s extensive Medium resources and inﬂuence would deﬁnitely help ICM to attain the data.

<!-- b000607 | prose | pages [21] -->
• The dynamic system can only explain the local part of information ﬂow. We invoke SIR to solve the model which is not fully simulate the formation dissemination of the real world.

<!-- b000608 | furniture | pages [22] -->
Team # 44173

<!-- b000609 | heading | pages [22] -->
References

<!-- b000610 | furniture | pages [22] -->
Page 22 of 22

<!-- b000611 | references | pages [22] -->
[1] Kai Zhu and Lei Ying ,Information Source Detection in the SIR Model: A Sample Path

<!-- b000612 | references | pages [22] -->
Based Approach

<!-- b000613 | references | pages [22] -->
[2] YanChao Zhang, Yun Liu,Hai FengZhang ,“A Information Transmission Based on the On-

<!-- b000614 | references | pages [22] -->
line Social Network”, Journal of Physics,2011(5):60-66.

<!-- b000615 | references | pages [22] -->
[3] Ting Xu, Feng Zhu, “A SIR Model on the Scale-free n Networks”, Real Practice and Un-

<!-- b000616 | references | pages [22] -->
derstanding of Mathematics, 2011,41(11)254-256ˇc˝o

<!-- b000617 | references | pages [22] -->
[4] Simon Haykin.Neural Networks and Learning Machines.

<!-- b000618 | references | pages [22] -->
[5] K. Fernandes, P. Vinagre and P. Cortez.A Proactive Intelligent Decision Support System for

<!-- b000619 | references | pages [22] -->
Predicting the Popularity of Online News. Proceedings of the 17th EPIA 2015 - Portuguese

<!-- b000620 | references | pages [22] -->
Conference on Artiﬁcial Intelligence, September, Coimbra, Portugal.

<!-- b000621 | references | pages [22] -->
[6] Zhu Sch. of Electr., Comput. & Energy Eng., Arizona State Univ., Tempe, AZ, USA

<!-- b000622 | references | pages [22] -->
[7] Yang Li,XiaoYan Wang,Kun Kun,The Study Based on the Security the Social Network

<!-- b000623 | references | pages [22] -->
[J].2012ˇcˇn49ˇc´l7ˇcl’124-130.

<!-- b000624 | references | pages [22] -->
[8] Mo MˇcˇnWang D.Exploit of Online Social Networks With Semi-supervised Learn-

<!-- b000625 | references | pages [22] -->
ing[C]Proceedings of IEEE World Congress on Computational Intelligenceˇcˇn2010 18-23.

<!-- b000626 | references | pages [22] -->
[9] Danon LˇcˇnDiaz-Guilera AˇcˇnDuch Jˇcˇnet al.Comparing Community Structure Identiﬁca-

<!-- b000627 | references | pages [22] -->
tion[J].Journal of Statistical MechanicsˇcžTheory and Experimentˇcˇn2005ˇcˇn2005ˇc´l9ˇcl’.

<!-- b000628 | references | pages [22] -->
[10] YouFang Lin,TianYu Wang,Rui Tang.An Effective Social Network Community Find Model

<!-- b000629 | references | pages [22] -->
and Algorithm[J].Computer Research and Development2012ˇcˇn49ˇc´l2ˇcl’ 337-345.

<!-- b000630 | references | pages [22] -->
How

<!-- b000631 | references | pages [22] -->
[11] The

<!-- b000632 | references | pages [22] -->
Personal

<!-- b000633 | references | pages [22] -->
News

<!-- b000634 | references | pages [22] -->
Cycle:

<!-- b000635 | references | pages [22] -->
Americans

<!-- b000636 | references | pages [22] -->
choose

<!-- b000637 | references | pages [22] -->
to

<!-- b000638 | references | pages [22] -->
get

<!-- b000639 | references | pages [22] -->
news

<!-- b000640 | references | pages [22] -->
https://www.americanpressinstitute.org/publications/reports/survey-

<!-- b000641 | references | pages [22] -->
research/personal-news-cycle/

<!-- b000642 | references | pages [22] -->
[12] http://hypertextbook.com/facts/2007/TamaraTamazashvili.shtml

<!-- b000643 | references | pages [22] -->
[13] http://www.pewresearch.org/fact-tank/2013/10/16/12-trends-shaping-digital-news/

<!-- b000644 | references | pages [22] -->
[14] http://www.people-press.org/2012/09/27/section-1-watching-reading-and-listening-

<!-- b000645 | references | pages [22] -->
to-the-news-3/
