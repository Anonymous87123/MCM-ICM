# P-D-2016-44173-aa1c9913

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
44173

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000005 | title | pages [1] -->
D

<!-- b000006 | heading | pages [1] -->
2016 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000007 | front_matter | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000008 | prose | pages [1] -->
How to Understand the Information The ﬂow of information has never been as easy or wide-ranging as it is today. This paper proposes some models to explore the relationship between speed/ﬂow of information with inherent value of information.

<!-- b000009 | prose | pages [1] -->
First,to explore information ﬂow, we build up a SIIR model which takes the me- dia inﬂuence into consideration. This model is developed from the classical SIR model.We introduce the concept of hot transmission nodes to highlight the impact of media. We demonstrate our design with American media data. The results show that our model has a signiﬁcant performance in validating predicted values of the characteristics of information network in 2050.

<!-- b000010 | prose | pages [1] -->
Second,the information ﬁltering can be regarded as a classiﬁcation problem. We design a radial basis function network to implement the information ﬁltering. In order to solve sample noises and improve the computing performance,we decide to use K-means algorithm and RLS algorithm to implement our RBF network. We demonstrate our network in online news dataset ,with an training accuracy of 75.1%,and testing accuracy of 74.3%.we are satisﬁed that the accuracy rate with information ﬁltering as news.

<!-- b000011 | prose | pages [1] -->
Third, We have only considered the social network in the Internet and build a social network SIR(SN-SIR) model to explore the problem-how public interest and opin- ion can be changed through network.It simulates in the standard dataset: Facebook social network dataset .By analyzing the factors which can implement our result- s,we can make a plan to determinate information propagation. Then,we take infor- mation values ,people ˛a´rs initial opinion and bias, form of the message or its source, and topology or other reasons into account and propose a detailed scheme.

<!-- b000012 | prose | pages [1] -->
Finally, effects of external factors are considered in our models.And we analyze the stability and sensitively of our models. Although there are some weakness in our models,the results still demonstrate that our model can undergo disturbance in certain extent.

<!-- b000013 | furniture | pages [2] -->
Team # 44173

<!-- b000014 | furniture | pages [2] -->
Page 2 of 22

<!-- b000015 | heading | pages [2] -->
Contents

<!-- b000016 | contents | pages [2] -->
1 Introduction

<!-- b000017 | contents | pages [2] -->
3

<!-- b000018 | contents | pages [2] -->
1.1

<!-- b000019 | contents | pages [2] -->
Background

<!-- b000020 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000021 | contents | pages [2] -->
3

<!-- b000022 | contents | pages [2] -->
1.2

<!-- b000023 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
3

<!-- b000025 | contents | pages [2] -->
2 Assumptions

<!-- b000026 | contents | pages [2] -->
4

<!-- b000027 | contents | pages [2] -->
3 A SIIR Model of Information Flow

<!-- b000028 | contents | pages [2] -->
4

<!-- b000029 | contents | pages [2] -->
3.1

<!-- b000030 | contents | pages [2] -->
Social Network Information Dissemination . . . . . . . . . . . . . . . . . . . . . .

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
3.1.1

<!-- b000033 | contents | pages [2] -->
Social Network Information Dissemination Characteristics . . . . . . . . .

<!-- b000034 | contents | pages [2] -->
4

<!-- b000035 | contents | pages [2] -->
3.1.2

<!-- b000036 | contents | pages [2] -->
Model Building . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
5

<!-- b000038 | contents | pages [2] -->
3.2

<!-- b000039 | contents | pages [2] -->
Calculating and Simplifying the Model

<!-- b000040 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000041 | contents | pages [2] -->
6

<!-- b000042 | contents | pages [2] -->
3.2.1

<!-- b000043 | contents | pages [2] -->
The Model Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
6

<!-- b000045 | contents | pages [2] -->
3.2.2

<!-- b000046 | contents | pages [2] -->
Rationality validation And Sensitivity analysis . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [2] -->
7

<!-- b000048 | contents | pages [2] -->
3.3

<!-- b000049 | contents | pages [2] -->
Prediction

<!-- b000050 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000051 | contents | pages [2] -->
8

<!-- b000052 | contents | pages [2] -->
4 A Model of Information Filtering

<!-- b000053 | contents | pages [2] -->
11

<!-- b000054 | contents | pages [2] -->
4.1

<!-- b000055 | contents | pages [2] -->
Model Description

<!-- b000056 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
11

<!-- b000058 | contents | pages [2] -->
4.2

<!-- b000059 | contents | pages [2] -->
Hybrid Learning Procedure For Networks . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000060 | contents | pages [2] -->
11

<!-- b000061 | contents | pages [2] -->
4.3

<!-- b000062 | contents | pages [2] -->
Experiment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
13

<!-- b000064 | contents | pages [2] -->
4.4

<!-- b000065 | contents | pages [2] -->
Sensitively Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
13

<!-- b000067 | contents | pages [2] -->
4.5

<!-- b000068 | contents | pages [2] -->
Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000069 | contents | pages [2] -->
13

<!-- b000070 | contents | pages [2] -->
5 A SN-SIR Model

<!-- b000071 | contents | pages [2] -->
14

<!-- b000072 | contents | pages [2] -->
5.1

<!-- b000073 | contents | pages [2] -->
The Way of Information Dissemination in Network

<!-- b000074 | contents | pages [2] -->
. . . . . . . . . . . . . . . . .

<!-- b000075 | contents | pages [2] -->
14

<!-- b000076 | contents | pages [2] -->
5.2

<!-- b000077 | contents | pages [2] -->
A Model of Public Opinion Dissemination in Social Network . . . . . . . . . . . .

<!-- b000078 | contents | pages [2] -->
14

<!-- b000079 | contents | pages [2] -->
5.2.1

<!-- b000080 | contents | pages [2] -->
Model Building . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000081 | contents | pages [2] -->
15

<!-- b000082 | contents | pages [2] -->
5.3

<!-- b000083 | contents | pages [2] -->
Sensitivity Analysis and Model Validation . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000084 | contents | pages [2] -->
16

<!-- b000085 | contents | pages [2] -->
5.3.1

<!-- b000086 | contents | pages [2] -->
Model Validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000087 | contents | pages [2] -->
16

<!-- b000088 | contents | pages [2] -->
5.3.2

<!-- b000089 | contents | pages [2] -->
Sensitivity, parameter validation analysis . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [2] -->
17

<!-- b000091 | contents | pages [2] -->
5.4

<!-- b000092 | contents | pages [2] -->
Result Analysis

<!-- b000093 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
20

<!-- b000095 | contents | pages [2] -->
6 Analysis

<!-- b000096 | contents | pages [2] -->
21

<!-- b000097 | contents | pages [2] -->
6.1

<!-- b000098 | contents | pages [2] -->
Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
21

<!-- b000100 | contents | pages [2] -->
6.2

<!-- b000101 | contents | pages [2] -->
Weaknesses

<!-- b000102 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
21

<!-- b000104 | furniture | pages [3] -->
Team # 44173

<!-- b000105 | furniture | pages [3] -->
Page 3 of 22

<!-- b000106 | heading | pages [3] -->
1 Introduction

<!-- b000107 | heading | pages [3] -->
1.1 Background

<!-- b000108 | prose | pages [3] -->
Broadly speaking, information is one of the important ways for us to perceive the outside world. Today it spreads quickly in tech-connected communication network. Sometimes it is due to the information ﬁnding its way to inﬂuential or central network nodes that accelerate its spread through social media. Our prevailing premise is that this cultural characteristic to share information (both serious and trivial) has always been three. At present, information propa- gation is exposed explosive growth.Beacause our social networks and medium are more and more complex.Without effective ways to solve these problems ,it will ﬁnally cause information propagation is more and more difﬁcult to umderstand.Hence,our work has its unprecedented signiﬁcance in world nowadays.

<!-- b000109 | heading | pages [3] -->
1.2 Our Work

<!-- b000110 | prose | pages [3] -->
This paper propose some models to explore the relationship between speed/ﬂow of informa- tion with inherent value of information. The Dilemma:

<!-- b000111 | prose | pages [3] -->
• An adaptive ﬂow model is established with the consideration of the complex network changes.

<!-- b000112 | prose | pages [3] -->
• Make use of the existing parameters to ﬁlter the information reasonably.

<!-- b000113 | prose | pages [3] -->
• Reasonable analysis of inﬂuencing factors in the process of information transmission.

<!-- b000114 | prose | pages [3] -->
The Approach:

<!-- b000115 | prose | pages [3] -->
• FirstˇcˇnTo explore information ﬂow, we build up a SIIR model which takes the special fea- tures if media inﬂuence into consideration. This model is developed from classical SIR model.

<!-- b000116 | prose | pages [3] -->
• The Results show that our model has a signiﬁcant performance in validate the value of prediction with real value. And then ,we predict the rate of daily contact in 2050.

<!-- b000117 | prose | pages [3] -->
• Information ﬁltering is regarded as classiﬁcation problem. we design a radial basis func- tion network to implement information ﬁltering. In order to solve sample noise and com- puting performance, we decide to use K-means algorithm and RLS algorithm to imple- ment our RBF network.

<!-- b000118 | prose | pages [3] -->
• We have only considered the social network in the Internet and build a social network SIR(SN-SIR) to explore the problem ˛a´s how public interest an opinion can be changed through network ˛a´s.

<!-- b000119 | prose | pages [3] -->
• We can make a plan to determinate information propagation. Then ,we take information value ,people ˛a´rs initial opinion and bias, form of the message or its source, and topology or other reasons into account and build a detailed scheme.

<!-- b000120 | furniture | pages [4] -->
Team # 44173

<!-- b000121 | furniture | pages [4] -->
Page 4 of 22

<!-- b000122 | heading | pages [4] -->
2 Assumptions

<!-- b000123 | prose | pages [4] -->
The accuracy of our models rely on certain key, simplifying assumptions. These assumptions are listed below:

<!-- b000124 | prose | pages [4] -->
• Do not consider factors such as natural birth,death,and population mobility.The total population keeps as a constant K.

<!-- b000125 | prose | pages [4] -->
• Infected individuals once contact with susceptible individuals,Infected individuals change to susceptible individuals at a certain probability.

<!-- b000126 | prose | pages [4] -->
• At a certain time,The number of individuals per unit time removing from the infected individuals is proportional to the number of patients.

<!-- b000127 | prose | pages [4] -->
• The number of media is relatively ﬁxed in the same period.

<!-- b000128 | prose | pages [4] -->
Under the above and basic assumptions, we can set out to construct our model.

<!-- b000129 | heading | pages [4] -->
3 A SIIR Model of Information Flow

<!-- b000130 | prose | pages [4] -->
Information is created by the social network users and transmits in the entire network.The result of transmission is that the receiver of the information translates into the transmitter and disseminate the information to others,or translates to the recovered one and does not transmit to others.Obviously, this transmission way is similar with the way Infectious diseases spread in the crowd. Based on the analysis of social network structure,we introduce the hot transmission node into network,and proposes an information transmission model based on the improved SIR model [1],which is simulated with the data-based Facebook social network.

<!-- b000131 | heading | pages [4] -->
3.1 Social Network Information Dissemination

<!-- b000132 | heading | pages [4] -->
3.1.1 Social Network Information Dissemination Characteristics

<!-- b000133 | prose | pages [4] -->
In this section,we propose a to explore a general model of information ﬂow problems, which is not subjected to the limitations of the times and mediums of communication.

<!-- b000134 | prose | pages [4] -->
The total number of user nodes in social networks is denoted as N.The network is assumed to be an undirected graph and each node in the network may be in one of three states: susceptible(s), infected(i), or recovered(r).Nodes in state i have received the message and have the ability to transmit it.Nodes in state s have not received the message and have the possibility to receive it.Nodes in state r have received the message and will not transmit it any more.

<!-- b000135 | prose | pages [4] -->
There are a variety of mediums of communication,such as newspapers,televisions,the Inter- net and so on.Different mediums have different ability of transmission,but all of these medi- ums owe stronger ability than human beings.We consider media as the hot transmission n- odes.Their contact rate is denoted as λ1. Ordinary users in networks are considered as ordinary nodes.Their contact rate is denoted as λ2.

<!-- b000136 | prose | pages [4, 5] -->
The laws of Information dissemination of social networks with hot transmission nodes are as below:[2] • Hot transmission nodes contact with other nodes with the contact rate x1,while ordinary nodes with the contact rate λ2.

<!-- b000137 | furniture | pages [5] -->
Team # 44173

<!-- b000138 | furniture | pages [5] -->
Page 5 of 22

<!-- b000140 | prose | pages [5] -->
• After nodes in state s received the information from nodes in state i,they change into recovered nodes in a probability of µ,and into ordinary infected nodes in a probability of 1 −µ.

<!-- b000141 | prose | pages [5] -->
• With the propagation of information,the proportion of three types of nodes will tend to be stable.

<!-- b000142 | prose | pages [5] -->
The schematic diagram of information dissemination of social networks with hot transmis- sion nodes as shown in Figure 1, the solid line shows the information transmission between two points.

<!-- b000143 | caption | pages [5] -->
Figure 1: the Information Transmission of Atrioventricular Model Structure Diagrams

<!-- b000144 | caption | pages [5] -->
Figure 2: the Improved SIR Model

<!-- b000145 | heading | pages [5] -->
3.1.2 Model Building

<!-- b000146 | prose | pages [5] -->
According to the characteristics of the transmission above,we can get the information transmis- sion of atrioventricular model structure diagrams, as shown in Figure 1.

<!-- b000147 | prose | pages [5] -->
i0 is the proportion of hot transmission nodes in networks,which is usually ﬁxed.i(t) is the proportion of ordinary infected nodes in the time of t,which consists of i1(t),the ordinary in- fected nodes generated by hot transmission nodes,and i2(t),the ordinary nodes infected nodes generated by ordinary infected nodes.λ1 is the contact rate of hot transmission nodes,while λ2 is the contact rate of ordinary infected nodes.r(t) is the proportion of nodes in state r,µ is the rate of Immune probability.[3] We can get the model as follows:

<!-- b000148 | prose | pages [5] -->
ds(t)  = −λ1i0s(t) −λ2s(t)i(t) dt        di(t)  = µ[λ1i0s(t) + λ2s(t)i(t)]   dt        dr(t) = (1 −µ)[λ1i0s(t) + λ2s(t)i(t)] (1) dt       s(t) + i(t) + i0 + r(t) = 1           i0 = i10, i(0) = i20, s(0) = s0, r(0) = r0 

<!-- b000149 | furniture | pages [6] -->
Team # 44173

<!-- b000150 | furniture | pages [6] -->
Page 6 of 22

<!-- b000151 | heading | pages [6] -->
3.2 Calculating and Simplifying the Model

<!-- b000152 | heading | pages [6] -->
3.2.1 The Model Results

<!-- b000153 | prose | pages [6] -->
Take the United States as an example,we obtain the statistical data of the circulation of news- papers, and numbers of users of radio, television, mobile phone and the Internet in different years.After analysis,we calculate the daily contact ratio of the ﬁve media,λi.We calculated the proportion of people contact with the different media group in all the population in the US. at that time.

<!-- b000154 | prose | pages [6] -->
N X λ1 = λiPi (2) i=1

<!-- b000155 | prose | pages [6] -->
We choose ﬁve years:1850,1930,1960,1996,2012,to calculate the model,and get the pictures of the change trend of the proportion of three kinds of nodes.

<!-- b000156 | prose | pages [6] -->
100 100 90 90 Susceptible individuals Susceptible individuals Recovered individuals Recovered individuals 80 80 Infected individuals Infected individuals 70 70 the rate of three node the rate of three node 60 60 X: 66.04 X: 83.88 Y: 50.07 Y: 50.02 50 50 40 40 30 30 20 20 X: 72.35 X: 54.55 Y: 10.06 Y: 10.08 10 10 0 0 0 10 20 30 40 50 60 70 80 90 100 0 10 20 30 40 50 60 70 80 90 100 time/days time/days

<!-- b000157 | caption | pages [6] -->
Figure 3: 1850

<!-- b000158 | caption | pages [6] -->
Figure 4: 1930

<!-- b000159 | prose | pages [6] -->
100 100 Susceptible individuals 90 90 Susceptible individuals Recovered individuals Recovered individuals 80 80 Infected individuals Infected individuals 70 70 the rate of three node the rate of three node 60 60 X: 62.19 X: 59.29 Y: 50.3 Y: 50.06 50 50 40 40 30 30 20 20 X: 47.75 X: 50.62 Y: 10.05 Y: 9.897 10 10 0 0 0 10 20 30 40 50 60 70 80 90 100 0 10 20 30 40 50 60 70 80 90 100 time/days time/days

<!-- b000160 | caption | pages [6] -->
Figure 5: 1960

<!-- b000161 | caption | pages [6] -->
Figure 6: 1996

<!-- b000162 | prose | pages [6] -->
The simulation results show that,the number of individuals who have known the informa- tion is increasing,and the proportion of susceptible nodes is decreasing over time.If the time is long enough, information can spread throughout the entire network.By contrast,we can know that the average contact rate of infected nodes increases gradually,which shortens the period of information dissemination and expands the scope of information dissemination.

<!-- b000163 | prose | pages [6] -->
In conclusion,the improved information transmission model can reveal the inherent law of information transmission in social network more accurately.

<!-- b000164 | furniture | pages [7] -->
Team # 44173

<!-- b000165 | furniture | pages [7] -->
Page 7 of 22

<!-- b000166 | prose | pages [7] -->
100 90 Susceptible individuals Recovered individuals 80 Infected individuals 70 the rate of three node 60 X: 62.08 Y: 50.3 50 40 30 20 X: 50.74 Y: 10.3 10 0 0 10 20 30 40 50 60 70 80 90 100 time/days

<!-- b000167 | caption | pages [7] -->
Figure 7: 2012

<!-- b000168 | heading | pages [7] -->
3.2.2 Rationality validation And Sensitivity analysis

<!-- b000169 | prose | pages [7] -->
In order to illustrate the model better , we investigate Facebook data and get the latest Facebook data on DMR website.Total number of Facebook daily active users is 1038 billionˇcˇn26.7 per- cent of the Internet users in the US. that clicked a Facebook share button on blog posts they enjoyed.General users has 245 friends in average.Model parameters can be determined by the conditions and the initial value is as follows: λ1 = 1000, λ2 = 245, µ = 73.3%, i0 = 5 × 10 −7, i(0) = 0, s0 = 1, r(0) = 0, we use Matlab to solve the Differential equations and get the ﬁgures of the change trend of the proportion of three kinds of nodes in Facebook.It can be seen that:

<!-- b000170 | prose | pages [7] -->
More than half of the users has received the message In less than 7 days.After ten days, about 70% of the users in the network have get the message.Eventually the ratios of the number of three kinds of nodes achieve stable.

<!-- b000171 | prose | pages [7] -->
The Inﬂuence of Parameters on the Information Dissemination 1.Contact rates of hot transmission nodes By changing the daily contact rate of hot transmission nodes in social network,we can ﬁnd the result in Figure5,After contrast,we know that with the increase of average daily contact rate of transmission nodes,the period of information dissemination has been shortened and the scope of information dissemination has been expanded.

<!-- b000172 | prose | pages [7] -->
100 Susceptible individuals Recovered individuals Infected individuals 80

<!-- b000173 | prose | pages [7] -->
60 X: 7.155 the rate of three node Y: 49.99

<!-- b000174 | prose | pages [7] -->
40

<!-- b000175 | prose | pages [7] -->
20 X: 6.131 Y: 10.09

<!-- b000176 | prose | pages [7] -->
0

<!-- b000177 | prose | pages [7, 8] -->
−20 0 5 10 15 20 time/days 100 100 100 Susceptible individuals Susceptible individuals Susceptible individuals Recovered individuals Recovered individuals Recovered individuals Infected individuals Infected individuals Infected individuals 80 80 80

<!-- b000178 | caption | pages [7] -->
Figure 8: facebook

<!-- b000179 | furniture | pages [8] -->
Team # 44173

<!-- b000180 | furniture | pages [8] -->
Page 8 of 22

<!-- b000182 | prose | pages [8] -->
60 60 60 X: 7.825 X: 7.542 X: 6.928 the rate of three node the rate of three node the rate of three node Y: 50.19 Y: 50.07 Y: 50.05

<!-- b000183 | prose | pages [8] -->
40 40 40

<!-- b000184 | prose | pages [8] -->
20 20 20 X: 6.516 X: 5.902 Y: 10.04 Y: 10.03

<!-- b000185 | prose | pages [8] -->
0 0 0

<!-- b000186 | prose | pages [8] -->
−20 −20 −20 0 5 10 15 20 0 5 10 15 20 0 5 10 15 20 time/days time/days time/days

<!-- b000187 | caption | pages [8] -->
Figure 9: λ1 = 300

<!-- b000188 | caption | pages [8] -->
Figure 10: λ1 = 500

<!-- b000189 | caption | pages [8] -->
Figure 11: λ1 = 1500

<!-- b000190 | prose | pages [8] -->
100 100 Susceptible individuals Susceptible individuals Recovered individuals Recovered individuals Infected individuals Infected individuals 80 80

<!-- b000191 | prose | pages [8] -->
60 60 X: 16.29 X: 4.555 the rate of three node the rate of three node Y: 50.4 Y: 50.01

<!-- b000192 | prose | pages [8] -->
40 40

<!-- b000193 | prose | pages [8] -->
20 20

<!-- b000194 | prose | pages [8] -->
0 0

<!-- b000195 | prose | pages [8] -->
−20 −20 0 10 20 30 40 50 0 5 10 15 20 time/days time/days

<!-- b000196 | caption | pages [8] -->
Figure 12: λ2 = 100

<!-- b000197 | caption | pages [8] -->
Figure 13: λ2 = 400

<!-- b000198 | prose | pages [8] -->
2.The Probability of the Immune By changing the probability of the immune,we can ﬁnd the result in pictures as bellow. The probability of the immune can impact the period of information dissemination,too.Reducing the probability of the immune can speed up the information transmission and shorten the pe- riod of information dissemination.

<!-- b000199 | heading | pages [8] -->
3.3 Prediction

<!-- b000200 | prose | pages [8] -->
We carry out the multiple regression analysis on data and make predictions,and get general changes of daily contact rate for each media.Figure14

<!-- b000201 | prose | pages [8] -->
With the changes of The times and the emergence of kinds of media,the proportion of each medium also changes over time.as is shown in Figure15

<!-- b000202 | prose | pages [8] -->
Considering the tendency of different media and changes of the way people get their news,combining with relevant information and data.We can ﬁnd that:

<!-- b000203 | furniture | pages [9] -->
Team # 44173

<!-- b000204 | furniture | pages [9] -->
Page 9 of 22

<!-- b000205 | prose | pages [9] -->
100 100 Susceptible individuals Susceptible individuals Recovered individuals Recovered individuals Infected individuals Infected individuals 80 80

<!-- b000206 | prose | pages [9] -->
60 60 the rate of three node the rate of three node X: 11.36 Y: 34.84 40 40

<!-- b000207 | prose | pages [9] -->
X: 8.459 20 20 Y: 14.84

<!-- b000208 | prose | pages [9] -->
0 0 X: 5.328 X: 4.541 Y: 0.5121 Y: 0.4047 −20 −20 0 5 10 15 20 0 5 10 15 20 time/days time/days

<!-- b000209 | caption | pages [9] -->
Figure 14: µ = 0.65

<!-- b000210 | caption | pages [9] -->
Figure 15: µ = 0.85

<!-- b000211 | caption | pages [9] -->
Figure 16: Change of Daily Contact Rate

<!-- b000212 | prose | pages [9] -->
1.Before the 19th century, the newspaper is the main access to gain news, and around 1950, the radio has a majority of users,.The data changes again in 1980, TV at this time holds the leading position.After that,the number of users of mobile phones, and the Internet is constantly rising.Besides,after 2000, the number rises quickly and clearly, and the Internet and the mobile phone gradually become the main tools to get news and messages in people’s daily lives.

<!-- b000213 | prose | pages [9] -->
2.Users of newspapers, radio and television have decreased constantly.But in recent years the pace of decline has gradually slowed down.But after 2020, with the popularity of the Internet, the users number will tend to be saturated, although there is still a rising trend, but the rise has slowed.

<!-- b000214 | prose | pages [9] -->
In the case of 2050, we take the predict data into information ˛a´rs ﬂow model, the situation of the information ﬂow is shown as follows.

<!-- b000215 | prose | pages [9] -->
When only consider the changes of average daily contact rate of average daily contact rate,we can see that:

<!-- b000216 | furniture | pages [10] -->
Team # 44173

<!-- b000217 | furniture | pages [10] -->
Page 10 of 22

<!-- b000218 | caption | pages [10] -->
Figure 17: Change of The Proportion of Daily Contact Rate

<!-- b000219 | prose | pages [10] -->
100 90 Susceptible individuals 80 Recovered individuals 70 Infected individuals the rate of three node 60 50 40 30 20 10 0 0 20 40 60 80 100 120 time/days

<!-- b000220 | caption | pages [10] -->
Figure 18: 2050

<!-- b000221 | prose | pages [10] -->
1.Compared with 2012,the speed of news propagation will keep going up in 2050.In less than 40 days,almost half of the people can acquire the news when it happens.While in 2012,nearly half of the people learn a message in 50 days.The speed of information transmission increased by about 25%.

<!-- b000222 | prose | pages [10] -->
2.The transmission of the message gets into its stride at the 20th day in 2012.While in 2050,the transmission of the message starts at the 10th day.In 2050, by contrast, the begining of the trans- mission will be in advance,which is another sign of increasing of the information transmission speed.

<!-- b000223 | prose | pages [10] -->
3.In 2012,the spread of information cycle lasts about 60 days,while in 2050,The spread of infor- mation cycle lasts about only 50 days,which means that in the same length of time, the amount of messages people contact will increase.And this portends that information capacity will be constantly increasing,with the development of communication tools .

<!-- b000224 | prose | pages [10] -->
From 2000,the number of people using social networks has increased,and the contact rate of ordinary nodes has changed,too.Ordinary nodes have more opportunity to change into hot transmission nodes,resulting to the proportion of hot transmission nodes in the whole heat has increased.So we boost the number of hot transmission nodes and the contact rate of ordinary nodes.The model adjusted is as follow:

<!-- b000225 | furniture | pages [11] -->
Team # 44173

<!-- b000226 | furniture | pages [11] -->
Page 11 of 22

<!-- b000227 | prose | pages [11] -->
100 Susceptible individuals Recovered individuals Infected individuals 80

<!-- b000228 | prose | pages [11] -->
60 the rate of three node 40

<!-- b000229 | prose | pages [11] -->
20

<!-- b000230 | prose | pages [11] -->
0

<!-- b000231 | prose | pages [11] -->
−20 0 10 20 30 40 50 60 70 80 90 100 time/days

<!-- b000232 | caption | pages [11] -->
Figure 19: 2050

<!-- b000233 | prose | pages [11] -->
Compare two results, the information transmission will accelerate again,and the transmis- sion cycle will shorten again.Owing to this,information will exist in a shorter time, and a lot of information will become a fast-good-type messages,which is a kind of portrayal of real life.

<!-- b000234 | heading | pages [11] -->
4 A Model of Information Filtering

<!-- b000235 | heading | pages [11] -->
4.1 Model Description

<!-- b000236 | prose | pages [11] -->
The purpose of information ﬁltering is to extract the information as news.Essentially, infor- mation ﬁltering is a classiﬁcation problem. We propose a radial basis function network(RBF) model[4]. In order to solve the samples noise and computing performance, we decide to use K-means algorithm and RLS algorithm implement network. We demonstrate our model using online news dataset.

<!-- b000237 | heading | pages [11] -->
4.2 Hybrid Learning Procedure For Networks

<!-- b000238 | prose | pages [11] -->
we develop a hybrid learning procedure for RBF networks. First,we use K-means algorithm to train hidden layer. And then, RLS algorithm is checked to train output layer. We call The hybrid learning procedure as “”K-means RLS “”algorithm. The algorithm is divided to three steps:

<!-- b000239 | prose | pages [11] -->
• Input layer.

<!-- b000240 | prose | pages [11] -->
The size of input layer is determined by the dimensionality of input vector x, which is denoted by m0.

<!-- b000241 | prose | pages [11] -->
• Hidden layer.

<!-- b000242 | prose | pages [11, 12] -->
1. The size of the hidden layer ,m1 is determined by the proposed number of clusters, K. Indeed, the parameter K may by viewed as a degree of freedom under the design- er ˛a´rs control. As such, the parameter K holds the key to the model-selection problem and thereby controls not only the performance, but also computational complexity of network.

<!-- b000243 | furniture | pages [12] -->
Team # 44173

<!-- b000244 | furniture | pages [12] -->
Page 12 of 22

<!-- b000246 | heading | pages [12] -->
2. The cluster mean ˆµj,computed by the K-means algorithm working on the unlabeled

<!-- b000247 | prose | pages [12] -->
sample xiN i=1 of input vectors, determines the center xj in the Gaussian function φ(·, xj) assigned to the hidden unit j = 1, 2, · · · , k. 3. To simplify the design ,the same width, denoted by σ,is assigned to all the Gaussian functions in accordance with the spread of the centers discovered by the K-means algo- rithm ,as shown by σ = dmax √ 2K ,where K is the number of centers and dmax is the maximum distance between them. This formula ensures that the individual Gaussian units are not too peaked or too ﬂat;both extreme conditions should be avoided in practice.

<!-- b000248 | prose | pages [12] -->
• Output layer.

<!-- b000249 | prose | pages [12] -->
Once the training of the hidden layer is completed, the training of the output layer can begin. Let the K × 1 vector.

<!-- b000250 | prose | pages [12] -->
  ϕ(xi, x1) ϕ(xi, x2)   φ(x) = (3)   ...     ϕ(xi, xK)

<!-- b000251 | prose | pages [12] -->
denote the outputs of the K units in the hidden layer. This vector is produced in response to the stimulus xi, i = 1, 2, , N. Thus, insofar as the supervised training of the output layer is concerned,the training sample is deﬁned by

<!-- b000252 | prose | pages [12] -->
Φ(i), d(i)N i=1

<!-- b000253 | prose | pages [12] -->
,where di is desired response at the overall output of the RBF network for input xi,This training is carried out using the RLS algorithm. Once the network training is completed, testing of the whole network with data not seen before can begin.

<!-- b000254 | furniture | pages [13] -->
Team # 44173

<!-- b000255 | furniture | pages [13] -->
Page 13 of 22

<!-- b000256 | heading | pages [13] -->
4.3 Experiment

<!-- b000257 | prose | pages [13] -->
We demonstrate out model in online news dataset[5].we pre-process dataset in term of ﬁlter Unnecessary factors. Our dataset is divided to two class , the number of shares more than 1400 is considered signiﬁcant ˛a ˛a information. The number of information is 39240,we train our net- work using 27908 information, and then test with 11332 information.The considering factors as follows, 1) Days between the article publication and the dataset acquisition(non-predictive). 2) Number of words in the title. 3) Number of words in the content. 4) Number of images. 5) Number of videos. 6) Number of keywords in the metadata. 7) Data channel: lifestyle, entertainment , business, social media,tech,world. 8) Was the article published on the weekend? 9) Number of shares

<!-- b000258 | prose | pages [13] -->
The results of our network is given in table: Accuracy in train procedure is 75.1%.

<!-- b000259 | heading | pages [13] -->
4.4 Sensitively Analysis

<!-- b000260 | prose | pages [13] -->
We draw a ROC curve graph to verify the sensitively of our network. The curve can cover most area. It indicate our network is sensitive. In order to validate the stability of our network ˇcˇnwe test our network in our dataset. The re- sults is given in table as above. Accuracy in test procedure is 74.3%.The results show that out model can adapt to data-change, and ﬁlter information as news.

<!-- b000261 | heading | pages [13] -->
4.5 Conclusion

<!-- b000262 | prose | pages [13, 14] -->
The RBF network adopt “”K-means RLS“” algorithm, which can improve the performance of computing. This algorithm has two characteristics: computational simplicity and acceleration convergence. The only suspect is the lack of the training of hidden layer and the training of output layer combined with the most criteria, which in the statistical sense to ensure the entire system of optimality. The only thing to doubt is not to p=optimize the training of hidden layer and output layer, so as to ensure the optimality of whole system in statistics. Using RBF network ,we can implement our information ﬁltering efﬁciently.

<!-- b000263 | furniture | pages [14] -->
Team # 44173

<!-- b000264 | furniture | pages [14] -->
Page 14 of 22

<!-- b000266 | heading | pages [14] -->
5 A SN-SIR Model

<!-- b000267 | prose | pages [14] -->
To solve the problem of how public interest and opinion can be changed through information networks in the Internet,we model of social network mainly about public opinion based on SIR and complex network theory,and then we text the model performance by FaceBook’s social network datasets.

<!-- b000268 | heading | pages [14] -->
5.1 The Way of Information Dissemination in Network

<!-- b000269 | prose | pages [14] -->
In the social network ,the relationship between the user can be established only by both sides of the identity authentication .[7] So social network can be thought of as net which does not has directions and weight and use the users and the relation ship between users replaces nodes and edges,and topics or news spread along the edges.[8]

<!-- b000270 | caption | pages [14] -->
Figure 20: The way of Public Opinion Dissemination in Social Network

<!-- b000271 | heading | pages [14] -->
5.2 A Model of Public Opinion Dissemination in Social Network

<!-- b000272 | prose | pages [14] -->
we classify nodes into three types as same as we deﬁne above,and assume that all nodes are susceptible in the beginning,but adding or changing some deﬁnition of factors are as follows.

<!-- b000273 | prose | pages [14] -->
• 1)Psi is the rate of probability of node in state s turn to Node in state i when s contacts with i.

<!-- b000274 | furniture | pages [15] -->
Team # 44173

<!-- b000275 | furniture | pages [15] -->
Page 15 of 22

<!-- b000276 | prose | pages [15] -->
• 2)α is the rate of probability of node s turned to node i when s gets some public opinions but does not contact with i.

<!-- b000277 | prose | pages [15] -->
• 3)Pir is the rate of probability of node i turn to node r in state r when node i lose s interest about a public opinion and stops spreading the public opinion.

<!-- b000278 | prose | pages [15] -->
• 4)Psr is the rate of probability of node s trun to node r when s gets a public opinion it is not interested in and dose not want to spread the public opinion.

<!-- b000279 | prose | pages [15] -->
• 5)k is the degree value of each node.

<!-- b000280 | heading | pages [15] -->
5.2.1 Model Building

<!-- b000281 | prose | pages [15] -->
It is a kind of dynamic procedure when we refer to the spread of social networking topic. Propaga of topic is inﬂuenced by one or more factors . The spread when a node in social net- work want to spread some opinions will be inﬂuenced by the ability of neighboring nodes. The greater the degree of spread of nodes,the better to public opinion spread in the network. Make a conclusion about the above knowable,and we get the model of node state transition in social network.[6] On the basis of model of node state transition and theory about SIR,we build the public opin-

<!-- b000282 | prose | pages [15] -->
ion transmission model in the social network is as followsˇcž

<!-- b000283 | prose | pages [15, 16] -->
ds(k,t)  = −psiks(k, t)θt −αs(k, t) −psrs(k, t) dt        di(k,t)  = psiksk, tθt + αs(k, t) −pirs(k, t)   dt   (4) dr(k,t)  = psrsk, t + pirik, t   dt         s(k, t) + i(k, t) + r(k, t) = 1  In the above equation,θ(t) signiﬁes the probability of any edges can contact with nodes in state i at time of t,and its equation is as follows:

<!-- b000284 | furniture | pages [16] -->
Team # 44173

<!-- b000285 | furniture | pages [16] -->
Page 16 of 22

<!-- b000287 | prose | pages [16] -->
P k kP(k)i(k, t) θ(t) = (5) < k > In the above equation,P(k) is the degree distribution function of social networksˇc˙z< k > is the average node degree of social networks.

<!-- b000288 | heading | pages [16] -->
5.3 Sensitivity Analysis and Model Validation

<!-- b000289 | heading | pages [16] -->
5.3.1 Model Validation

<!-- b000290 | prose | pages [16] -->
In order to validate the efﬁciency of public opinion topic transmission model which we pro- posed,we choose the standard data sets -“” Facebook social network dataset“”which includes 4039 nodes and 88234 sides to carry on our simulation experiment.[9] 1. The relation between the density of different nodes over time Assuming that there is only one communication node in the network and the rest areall nodes in state s .Set the total pa- rameters of ( 1 ) as follows : the external infection probability Psi = 0.4; the internal infection probability α = 0.3; the immune probability Pir = 0.2; the direct immune probability Psr = 0.1. The change relation between the density of each node and the spread of public opinion topic is shown in ﬁgure 3.From pictures below:

<!-- b000291 | furniture | pages [17] -->
Team # 44173

<!-- b000292 | furniture | pages [17] -->
Page 17 of 22

<!-- b000293 | prose | pages [17] -->
we can see: The density of the susceptible nodes have a tendency to attenuate until it is close to zero.The density of transmission node have a rapid growth in the initial stage,and it will decline rapidly after its peak until its tendency to zero.While the density of the immune node shows a quick growth at the beginning of the diffusion of a topic.It will become stable gradually after its peak and tend to be 1 in the end. We can draw the conclusions as follows after our parameter veriﬁcation of the social network.

<!-- b000294 | prose | pages [17] -->
• 1.Generally speaking ,the higher the value of an information is,the lower immunisation rates of the information will be ,the higher the internal infection rate will be. There will be more transmission nodes and less immune nodes in a short transmission-cycle time.Which means the more quickly the information spread,the more widely the range of users will cover.

<!-- b000295 | prose | pages [17] -->
• 2.User ˛a´rs interests and prejudices can react on the immune probability and the infection rate,the higher the user’s interests in the message is,the lower the corresponding immune probability and direct immune immunisation rates will be ,and the infection rate will rise accordingly, when the message comes to the user, the speed of the spread will be faster, and as for a message, the more uses are interested in, the lower the corresponding im- munity will be,the more people infected will be,the more transmission nodes will be, the faster the news propagation speed will be ,that is to say,the transmission will be faster if it owns more users interested in.

<!-- b000296 | heading | pages [17] -->
5.3.2 Sensitivity, parameter validation analysis

<!-- b000297 | prose | pages [17] -->
1.The inﬂuence of Psi When Psi is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as followsˇcž

<!-- b000298 | prose | pages [17] -->
(1)Before the Internet reach steady state, with the increase of Psi ,the density about nodes in state s is growth,but the density about nodes in state r is go down.The reason about this is the greater of Psi ,the more number of nodes in state i transform into nodes in state sˇc˙z

<!-- b000299 | prose | pages [17] -->
(2)With the increase of Psi ,the time of The spread of social network public opinion reaches a steady state is more longer.

<!-- b000300 | prose | pages [17] -->
(3)When Psi=0, social network information can still be propagated,this is different with pre- vious research results.The reason about this is the connectivity of social networks is higher when it compare with traditional network and social network user can get public opinion from each other and other mode.

<!-- b000301 | prose | pages [17, 18] -->
2,The inﬂuence of Pir When Pir is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as followsˇcž (1) When Pir >0, before the Internet reach steady state, Pir and the density about nodes in state s against each other and found a negative correlation,but Pir and the density about nodes in state r found a positive correlation.So,the value of Pir is greater,the rate of probability of nodes in state i turn to state r is higher.

<!-- b000302 | furniture | pages [18] -->
Team # 44173

<!-- b000303 | furniture | pages [18] -->
Page 18 of 22

<!-- b000305 | prose | pages [18] -->
(2) When Pir =0, Pir increase rapidly in the early,gradually stabilized after get to the peak .The reason about this is when Pir =0, nodes in state I Will always keep their state and do not switch to the state r.However,the density about nodes in stater !=0 because of the inﬂuence of Psr and some nodes in state s turn to stater.

<!-- b000306 | prose | pages [18] -->
3,The inﬂuence of α When α is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as follows.The ﬁgure shows that before the Internet reach steady state,as long as the value of˛eÁ- further increase, the density about nodes in state i increases correspondingly,but the density about nodes in state r decrease all the time.This is mainly because the value of α is greater,the rate of probability of nodes in state s turn to state i is higher.

<!-- b000307 | prose | pages [18] -->
4,The inﬂuence of Psr When Psr is changed ,the variation trend of density ﬂuctuation about nodes in state s and r is as follows.The ﬁgure shows that with the increase of Psr,the density about nodes in state r is growth,but the density about nodes in state i is go down. This is mainly because the value of Psr is greater,the rate of probability of nodes in state s turn to state r directly without turn to state i is higher.

<!-- b000308 | prose | pages [18, 19] -->
5,The inﬂuence of initial nodes degree k0 When k0 is changed ,the variation trend of den- sity ﬂuctuation about nodes in state s is as follows.And we can know that the value of k0 is greater,the speed of public opinion propagation is faster in social network.

<!-- b000309 | furniture | pages [19] -->
Team # 44173

<!-- b000310 | furniture | pages [19] -->
Page 19 of 22

<!-- b000312 | prose | pages [19] -->
6,The inﬂuence of different node density changes over time When the density about nodes in state s,i and r is changed, public opinion evolution trend over time is as follows.From the picture,we can kown that, no matter how the density about nodes in state s,i and r change with time, public opinion evolution trend are basically identical. This shows that the different value of nodes has similar behavior characteristics.

<!-- b000313 | furniture | pages [20] -->
Team # 44173

<!-- b000314 | furniture | pages [20] -->
Page 20 of 22

<!-- b000315 | heading | pages [20] -->
5.4 Result Analysis

<!-- b000316 | prose | pages [20] -->
Using social network dataset to validate the patameters , we can draw the conclusions as fol- lows. (1)Generally speaking ,the higher the value of an information is , the lower immune probability of the information will be ,the higher the internal infection probability will be. There will be more nodes in state s and less nodes in state r in a short transmission-cycle time , which means the more quickly the information spread, the more widely the range of users will cover.

<!-- b000317 | prose | pages [20] -->
(2)User ˛a´rs interests and prejudices can react on the immune probability and the infection rate .The higher the user’s interests in the message is , the lower the corresponding immune prob- ability and direct immune rates will be ,and the infection rate will rise accordingly, when the message comes to the user, the speed of the spread will be faster, and as for a message, the more uses are interested in, the lower the corresponding immunity will be , and the more people in- fected will be , the more transmission nodes will be, the faster the news propagation speed will be ,that is to say , the transmission will be faster if it owns more users interested in.

<!-- b000318 | prose | pages [20] -->
(3)In social network ,the source of the message can be divided into hot transmission nodes and normal transmission nodes as we discussed in the information ﬂow model. Hot trans- mission nodes have larger infection rate and degree of value ,but normal transmission nodes that infection rate is lesser, degree of value is smaller than hot transmission nodes. Consider- ing the inﬂuence of parameters, we parsed on the information dissemination model, when the news that come from hot transmission nodes have faster transmission speed and wider scope of news than ordinary nodes.

<!-- b000319 | prose | pages [20, 21] -->
(4) Using degree value of the nodes describes the different network topology and strength . Through transformation analysis of parameters, the degree of initial node in social networks have an obvious impact on public opinion propagation velocity , and different nodes ˛a˝o distri- bution has a small impact.

<!-- b000320 | furniture | pages [21] -->
Team # 44173

<!-- b000321 | furniture | pages [21] -->
Page 21 of 22

<!-- b000323 | heading | pages [21] -->
6 Analysis

<!-- b000324 | heading | pages [21] -->
6.1 Strengths

<!-- b000325 | prose | pages [21] -->
• Our model invokes and expand the classical SIR model.

<!-- b000326 | prose | pages [21] -->
We take times ,Medium inﬂuence into consideration and develop a SIIR model to solve information ﬂow problem. the external infection rate is taken into account.In order to adapt internet information ﬂow,we propose a SIR model that base on social network in internet.

<!-- b000327 | prose | pages [21] -->
• The solving processing and solution is stable.

<!-- b000328 | prose | pages [21] -->
• The result of out model is visible and easy to understand.

<!-- b000329 | prose | pages [21] -->
We demonstrate our model using data, and the result can be understand from the exper- iments. Consequently , anyone can comprehend the evaluation without any background knowledge.

<!-- b000330 | prose | pages [21] -->
• Our model has a strong sense of professional background.

<!-- b000331 | prose | pages [21] -->
Our model based on both subjective and objective methods solve the information ﬂow , information ﬁltering ,and ﬁnd the factors of inﬂuence information ﬂow.

<!-- b000332 | prose | pages [21] -->
• Our model can be extended into higher dimension.

<!-- b000333 | prose | pages [21] -->
As an information ﬁltering system can extend to take more dimension factors ,and then using our model to ﬁlter the information. Our model can explain the sustainability in a more explicit way.

<!-- b000334 | prose | pages [21] -->
• The dynamic prediction can be easily tracked.

<!-- b000335 | prose | pages [21] -->
The mechanism of our system dynamic offers handy to predict information ﬂow and capacity.

<!-- b000336 | heading | pages [21] -->
6.2 Weaknesses

<!-- b000337 | prose | pages [21] -->
• The model does not take platformsˇcˇnnetwork complexityˇcˇnRegion inﬂuenceˇcˇngovern- ment control and other factors into consider.

<!-- b000338 | prose | pages [21] -->
The model cannot accurately forecast information ﬂow between different region or plat- form, thus the sustainability is not necessarily exact in terms of some uncontrollable fac- tors.

<!-- b000339 | prose | pages [21] -->
• The statistical date used in implementing of model not complete achievable.

<!-- b000340 | prose | pages [21] -->
We cannot ﬁnd all data we required for sustainability. Fortunately, ICM‘’s extensive Medium resources and inﬂuence would deﬁnitely help ICM to attain the data.

<!-- b000341 | prose | pages [21] -->
• The dynamic system can only explain the local part of information ﬂow.

<!-- b000342 | prose | pages [21] -->
We invoke SIR to solve the model which is not fully simulate the formation dissemination of the real world.

<!-- b000343 | furniture | pages [22] -->
Team # 44173

<!-- b000344 | furniture | pages [22] -->
Page 22 of 22

<!-- b000345 | heading | pages [22] -->
References

<!-- b000346 | references | pages [22] -->
[1] Kai Zhu and Lei Ying ,Information Source Detection in the SIR Model: A Sample Path

<!-- b000347 | references | pages [22] -->
Based Approach

<!-- b000348 | references | pages [22] -->
[2] YanChao Zhang, Yun Liu,Hai FengZhang ,“A Information Transmission Based on the On-

<!-- b000349 | references | pages [22] -->
line Social Network”, Journal of Physics,2011(5):60-66.

<!-- b000350 | references | pages [22] -->
[3] Ting Xu, Feng Zhu, “A SIR Model on the Scale-free n Networks”, Real Practice and Un-

<!-- b000351 | references | pages [22] -->
derstanding of Mathematics, 2011,41(11)254-256ˇc˝o

<!-- b000352 | references | pages [22] -->
[4] Simon Haykin.Neural Networks and Learning Machines.

<!-- b000353 | references | pages [22] -->
[5] K. Fernandes, P. Vinagre and P. Cortez.A Proactive Intelligent Decision Support System for

<!-- b000354 | references | pages [22] -->
Predicting the Popularity of Online News. Proceedings of the 17th EPIA 2015 - Portuguese

<!-- b000355 | references | pages [22] -->
Conference on Artiﬁcial Intelligence, September, Coimbra, Portugal.

<!-- b000356 | references | pages [22] -->
[6] Zhu Sch. of Electr., Comput. & Energy Eng., Arizona State Univ., Tempe, AZ, USA

<!-- b000357 | references | pages [22] -->
[7] Yang Li,XiaoYan Wang,Kun Kun,The Study Based on the Security the Social Network

<!-- b000358 | references | pages [22] -->
[J].2012ˇcˇn49ˇc´l7ˇcl’124-130.

<!-- b000359 | references | pages [22] -->
[8] Mo MˇcˇnWang D.Exploit of Online Social Networks With Semi-supervised Learn-

<!-- b000360 | references | pages [22] -->
ing[C]Proceedings of IEEE World Congress on Computational Intelligenceˇcˇn2010 18-23.

<!-- b000361 | references | pages [22] -->
[9] Danon LˇcˇnDiaz-Guilera AˇcˇnDuch Jˇcˇnet al.Comparing Community Structure Identiﬁca-

<!-- b000362 | references | pages [22] -->
tion[J].Journal of Statistical MechanicsˇcžTheory and Experimentˇcˇn2005ˇcˇn2005ˇc´l9ˇcl’.

<!-- b000363 | references | pages [22] -->
[10] YouFang Lin,TianYu Wang,Rui Tang.An Effective Social Network Community Find Model

<!-- b000364 | references | pages [22] -->
and Algorithm[J].Computer Research and Development2012ˇcˇn49ˇc´l2ˇcl’ 337-345.

<!-- b000365 | references | pages [22] -->
[11] The

<!-- b000366 | references | pages [22] -->
Personal

<!-- b000367 | references | pages [22] -->
News

<!-- b000368 | references | pages [22] -->
Cycle:

<!-- b000369 | references | pages [22] -->
How

<!-- b000370 | references | pages [22] -->
Americans

<!-- b000371 | references | pages [22] -->
choose

<!-- b000372 | references | pages [22] -->
to

<!-- b000373 | references | pages [22] -->
get

<!-- b000374 | references | pages [22] -->
news

<!-- b000375 | references | pages [22] -->
https://www.americanpressinstitute.org/publications/reports/survey-

<!-- b000376 | references | pages [22] -->
research/personal-news-cycle/

<!-- b000377 | references | pages [22] -->
[12] http://hypertextbook.com/facts/2007/TamaraTamazashvili.shtml

<!-- b000378 | references | pages [22] -->
[13] http://www.pewresearch.org/fact-tank/2013/10/16/12-trends-shaping-digital-news/

<!-- b000379 | references | pages [22] -->
[14] http://www.people-press.org/2012/09/27/section-1-watching-reading-and-listening-

<!-- b000380 | references | pages [22] -->
to-the-news-3/
