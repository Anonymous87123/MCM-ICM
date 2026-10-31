# P-D-2016-47876-968a1156

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
47876

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000004 | front_matter | pages [1] -->
D

<!-- b000005 | title | pages [1] -->
Abridge the Distance between Human Minds

<!-- b000006 | title | pages [1] -->
—Research on Social Information Circulation

<!-- b000007 | heading | pages [1] -->
Summary

<!-- b000008 | prose | pages [1] -->
Information circulation network is as complicated as the human brain, while brain with wisdom seeks to explore the mysteries of the information circulation network.

<!-- b000009 | prose | pages [1] -->
First, we establish a model of information circulation network (ICP). Then we establish five network topology graphs and qualitatively analyze evolution of five periods. Based on classical epidemic model, we introduce the super-spreader, which can effectively accelerate the circulation of information as the central node. The differential equations and their results give us reasonable circulation laws: the density of the spreader and the super-spreader rapidly increase at the beginning, then they reach a peak and decline rapidly; the ignorant density shows a rapid downward trend while the immune density generally increases.

<!-- b000010 | prose | pages [1] -->
We build the fuzzy comprehensive evaluation model (NF) to filter what qualifies as news. We propose audience awareness index (AAI) to indicate the inherent value of information. Then we use four given examples to test the model. Undoubtedly, the assassination of Abraham Lincoln was qualified as news; and so does the important person’s assassination today. As for information of Taylor’s style transition, it becomes news today, but it might not be news in 1860.

<!-- b000011 | prose | pages [1] -->
Then we use the neural network prediction model (ICNP) to predict the networks’ relationships and capacities. We get the node number and the node degree via previous data from three states in USA. And the results of ICNP model are: in the fifth period, node number of New York is 22535000, and its relative error is 15.32%; in the fifth period, node degree is 13533000, and its relative error is 20.58%. So it validates the reliability of ICP model. In around 2050, node number of New York is 34885000 and node degree is 23766000.

<!-- b000012 | prose | pages [1] -->
Finally, we build our model (PIINI) considering the interest attenuation mechanism and social strengthening mechanism. Taking the interaction of information circulation network and public interests into account, we establish differential equations similarly. And it comes to interaction laws: the density of the spreader and nodes in connection state rapidly increase at the beginning, they reach a peak and then decline rapidly. The ignorant density shows a rapid downward trend while the immune density generally increases.

<!-- b000013 | prose | pages [1] -->
As a part of ICM’s Information Analytics Division, we have accomplished the given assignments.

<!-- b000014 | keywords | pages [1] -->
Keyword: Information Circulation Network   Epidemic Model     Differential Equation,

<!-- b000015 | prose | pages [1] -->
BP Neural Networks

<!-- b000016 | contents | pages [2] -->
Abridge the Distance between Human Minds

<!-- b000017 | contents | pages [2] -->
—Research on Social Information Circulation

<!-- b000018 | heading | pages [2] -->
Content

<!-- b000019 | contents | pages [2] -->
1.

<!-- b000020 | contents | pages [2] -->
Restatement of the Problem .................................................................................... 1

<!-- b000021 | contents | pages [2] -->
2.

<!-- b000022 | contents | pages [2] -->
Introduction ............................................................................................................. 1

<!-- b000023 | contents | pages [2] -->
3.

<!-- b000024 | contents | pages [2] -->
Assumptions ............................................................................................................ 2

<!-- b000025 | contents | pages [2] -->
4.

<!-- b000026 | contents | pages [2] -->
Justification of Our Approach ................................................................................. 2

<!-- b000027 | contents | pages [2] -->
5.

<!-- b000028 | contents | pages [2] -->
Symbol Descriptions ............................................................................................... 3

<!-- b000029 | contents | pages [2] -->
6.

<!-- b000030 | contents | pages [2] -->
The Model ............................................................................................................... 3

<!-- b000031 | contents | pages [2] -->
6.1 Information circulation network model (ICN) ..................................................... 3

<!-- b000032 | contents | pages [2] -->
6.1.1 Topological Properties .................................................................................. 4

<!-- b000033 | contents | pages [2] -->
6.1.2 The model construction ................................................................................. 4

<!-- b000034 | contents | pages [2] -->
6.1.3 To solve the model ........................................................................................ 7

<!-- b000035 | contents | pages [2] -->
6.2 News filter model (NF) ........................................................................................ 8

<!-- b000036 | contents | pages [2] -->
6.2.1 Influential factors of audience’s awareness index ........................................ 8

<!-- b000037 | contents | pages [2] -->
6.2.2 The model construction ................................................................................. 8

<!-- b000038 | contents | pages [2] -->
6.2.3 The process to test the model ........................................................................ 9

<!-- b000039 | contents | pages [2] -->
6.3 Information circulation network prediction model (ICNP) ............................... 10

<!-- b000040 | contents | pages [2] -->
6.3.1 Influential factors ........................................................................................ 10

<!-- b000041 | contents | pages [2] -->
6.3.2 The model construction ............................................................................... 10

<!-- b000042 | contents | pages [2] -->
6.3.3 To solve the model ...................................................................................... 12

<!-- b000043 | contents | pages [2] -->
6.4 Public interest and information network interaction model (PIINI) .................. 12

<!-- b000044 | contents | pages [2] -->
6.4.1 The model construction ............................................................................... 13

<!-- b000045 | contents | pages [2] -->
6.4.2 To solve the model ...................................................................................... 16

<!-- b000046 | contents | pages [2] -->
7.

<!-- b000047 | contents | pages [2] -->
Sensitivity Analysis ............................................................................................... 17

<!-- b000048 | contents | pages [2] -->
8.

<!-- b000049 | contents | pages [2] -->
Strengths and Weaknesses .................................................................................... 19

<!-- b000050 | contents | pages [2] -->
9.

<!-- b000051 | contents | pages [2] -->
Conclusions ........................................................................................................... 19

<!-- b000052 | contents | pages [2] -->
References

<!-- b000053 | contents | pages [2] -->
Appendix (data and data source)

<!-- b000054 | furniture | pages [3] -->
Team # 47876                                              Page 1 of 19

<!-- b000055 | heading | pages [3] -->
1. Restatement of the Problem

<!-- b000056 | prose | pages [3] -->
Information spread quickly in today’s tech-connected communications network; sometimes it is due to the inherent value of the information itself, and other times it is due to the information finding its way to influential or central network nodes that accelerate its spread through social media.

<!-- b000057 | prose | pages [3] -->
 Explore the flow of information and filter or find what qualifies as news.  Validate your model’s reliability.  Predict the communication networks’ relationships and capacities around the year 2050.  Explore how public interest and opinion can be changed through information networks in today’s connected world.  Determine how information value, people’s initial opinion and bias, form of the message or its source, and the topology or strength of the information network in a region, country, or worldwide could be used to spread information and influence public opinion. Interpretation of these problems  We should build a model to indicate how information circulate in social network.  We should figure out an improved model to filter what qualifies as news based on first model.  We should predict present network’s relationship and capacity to validate first model by using our model’s prediction ability, and predict future network’s relationship and capacity in around 2050.  We should build another model to explore the interaction of public interest and information network.

<!-- b000058 | heading | pages [3] -->
2. Introduction

<!-- b000059 | prose | pages [3] -->
Social information circulation network is a very active research area. Building the social information circulation network is the hot area of complex network research. That research has very important value for understanding the dynamic behavior of the network.

<!-- b000060 | prose | pages [3, 4] -->
Previous work In previous analysis, most of models are based on the classical epidemic model SI, SIS and SIR, etc. [1, 2] The IC model [3, 4] proposed by Jacob Goldenberg and the LT model [5] proposed by Mark Granovetter is most widely studied currently. And Jaewon Yang and other researchers proposed a linear influence model [6] by the analysis of Twitter’s users’ behaviors.

<!-- b000061 | furniture | pages [4] -->
Team # 47876                                              Page 2 of 19

<!-- b000063 | prose | pages [4] -->
From the aspect of social psychology, the mass information circulation process is placed in a environment affected by a variety of social forces and psychological factors. Massa described the analysis and prediction of perceived user behavior based on trust framework [7]. Jamali and other researchers [8] use TrustWalker model to predict behaviors’ of users. Josang A [9] build a user trust prediction system to describe the development of trust between different users.

<!-- b000064 | heading | pages [4] -->
3. Assumptions

<!-- b000065 | caption | pages [4] -->
Table 1 assumptions

<!-- b000066 | heading | pages [4] -->
Assumptions

<!-- b000067 | prose | pages [4] -->
1) We do not take time delay during information circulation between Overall two nodes into account.

<!-- b000068 | prose | pages [4] -->
2) We think the public interest is consistent. ICN model 3) We do not take social strengthening into account.

<!-- b000069 | prose | pages [4] -->
4) We do not consider the difference between different information.

<!-- b000070 | prose | pages [4] -->
5) We think the influence between two nodes will not affect our model.

<!-- b000071 | prose | pages [4] -->
6) We think the audience awareness is the only indicator of public NF model interest and opinion.

<!-- b000072 | prose | pages [4] -->
7) We do not consider secondary factors. ICNP model 8) We think the network is universal around the world.

<!-- b000073 | prose | pages [4] -->
9) We do not consider secondary factors. PIINI model

<!-- b000074 | heading | pages [4] -->
4. Justification of Our Approach

<!-- b000075 | heading | pages [4] -->
ICN model

<!-- b000076 | prose | pages [4] -->
Dynamics of epidemic disease can effectively portray on the circulation characteristics of complex network, which is an important basis for the current network circulation dynamics. Super-spreader plays an important role in the information circulation network. On the basis of classical epidemic model we introduce of the super- spreader and establish differential equations which can effectively portray information circulation network’s characteristics.

<!-- b000077 | heading | pages [4] -->
NF model

<!-- b000078 | prose | pages [4] -->
News is objective report of what audiences are concerned about. The concept of audience awareness is vague, but we can qualitatively analyze audience awareness index has a positive influence on inherent value of information. The fuzzy comprehensive evaluation model can characterize the transition state between news and information. Therefore, it is appropriate to use NF model to filter what qualifies as news.

<!-- b000079 | heading | pages [4] -->
ICNP model

<!-- b000080 | prose | pages [4, 5] -->
Information circulation network is a complex and random system, influenced by many factors. Using the statistical forecasting model to predict might have defects especially when the sample data are not enough and when historical data are volatile. And we use BP neural network to build ICNP model, which can overcome this shortcoming.

<!-- b000081 | furniture | pages [5] -->
Team # 47876                                              Page 3 of 19

<!-- b000083 | heading | pages [5] -->
PIINI model

<!-- b000084 | prose | pages [5] -->
Strengthening social mechanism is an important distinction between the information circulation and the spread of disease. Social interest attenuation mechanism is also significant in information circulation network. Proposed PIINI model takes social interest attenuation and social strengthening into account, so it can be effectively and reasonably reveal laws in the information circulation network.

<!-- b000085 | heading | pages [5] -->
5. Symbol Descriptions

<!-- b000086 | prose | pages [5] -->
There are some major symbols appear in the model, as shown below:

<!-- b000087 | caption | pages [5] -->
Table 2 symbol descriptions

<!-- b000088 | prose | pages [5] -->
Definition Formula Index The number of nodes include Node -- connected and disconnected nodes. number(N) The degree of nodes is the number of N N connected nodes. And give adjacent     k a a Node degree(ki) i i j ji      j 1 j 1 matrix . A a i j  N N

<!-- b000089 | prose | pages [5] -->
N N The average of all node degrees of 1 Node degree     k k a i ji N the network. average (<k>)   i 1 i 1

<!-- b000090 | prose | pages [5] -->
Network density is a symptom of Network 2 L  D    N N 1 network’s completeness. density(D)

<!-- b000091 | prose | pages [5] -->
Clustering coefficient represent the probability of any two nodes being E 2 E Clustering   C i i         i k k -1 2 k k -1 neighbors. Ei is the edges between coefficient(Ci) i i i i node i and neighbors ki. Notes: we will explain other symbols when we use them.

<!-- b000092 | heading | pages [5] -->
6. The Model

<!-- b000093 | heading | pages [5] -->
6.1 Information circulation network model (ICN)

<!-- b000094 | prose | pages [5] -->
Social network is a complex network, which is composed of social individuals as well as the social relationships between individual members.[10] In the related social network research, researchers used ） graph to build model. V is the set （ G V , , E W of network nodes; E is the set of relationships between social individuals; W   V V is the weight of social individuals.

<!-- b000095 | furniture | pages [6] -->
Team # 47876                                              Page 4 of 19

<!-- b000096 | heading | pages [6] -->
6.1.1 Topological Properties

<!-- b000097 | prose | pages [6] -->
Topological properties of network are irrelevant with size, location, shape and function of nodes. However, they are only relevant with number of nodes and the connection features between connected nodes.

<!-- b000098 | prose | pages [6] -->
In the research of social networks, directed graph has a better expressive ability and applicability, so we use a directed graph to characterize social networks. And based on this, we present the following indices.

<!-- b000099 | heading | pages [6] -->
6.1.2 The model construction

<!-- b000100 | prose | pages [6] -->
There are lots of classical epidemic models, such as SI, SIS, SIR, IC and LT. We take into account the central node (such as the Internet) has higher spreading function than ordinary spreader. We then introduce super-spreaders to our network to improve the SIR model. We divide the user into four parts: ignorant, spreader, super-spreader and immune. And the definition of these are as follows[11]:

<!-- b000101 | caption | pages [6] -->
Table 3 Four type of users

<!-- b000102 | prose | pages [6] -->
Types of users Definition

<!-- b000103 | prose | pages [6] -->
The ignorant has not received any information from neighbors. Ignorant

<!-- b000104 | prose | pages [6] -->
The spreader receives information, the spreader will probably spread the Spreader information to neighbors.

<!-- b000105 | prose | pages [6] -->
The immune will not spread the information after receiving the information. Immune

<!-- b000106 | prose | pages [6] -->
Super- The super-spreader is able to quickly deliver information to more people. spreader

<!-- b000107 | prose | pages [6] -->
The rules of information circulation

<!-- b000108 | prose | pages [6] -->
Spreader γ

<!-- b000109 | prose | pages [6] -->
β α Ignorant

<!-- b000110 | prose | pages [6] -->
Super-spreader Immune δ

<!-- b000111 | prose | pages [6] -->
Fig 1 the propagation rules of the model The rules of information circulation are shown above. We can conclude the rules as follows:

<!-- b000112 | prose | pages [6] -->
If ignorant connects to a spreader, they will turn into spreader with a probability β.

<!-- b000113 | prose | pages [6] -->
For publicity and other reasons, some spreaders will turn into super-spreader with a probability α.

<!-- b000114 | prose | pages [6] -->
After contacting with other spreaders, the super-spreader will turn into the immune with probability δ.

<!-- b000115 | furniture | pages [7] -->
Team # 47876                                              Page 5 of 19

<!-- b000116 | prose | pages [7] -->
After contacting with other spreaders, immunes or super-spreaders, the spreader will turn into the immune with a probability γ. The information circulation network in five periods.

<!-- b000117 | prose | pages [7] -->
On the basis of the establishment of information circulation network model, considering the characteristics of modes information circulation in five periods, we list the network circulation information model in five periods as follows:

<!-- b000118 | caption | pages [7] -->
Table 4 the information circulation graph and characteristics

<!-- b000119 | prose | pages [7] -->
Periods Modes The information circulation graph Characteristics

<!-- b000120 | prose | pages [7] -->
(1)The number of node, the degree of node, internet density and clustering coefficient are small (2)"Newspaper office" node is regarded as super- Newspaper spreaders and plays an important role in the 1870s & information network.

<!-- b000121 | prose | pages [7] -->
Telegraph (3)The closeness of information circulation is poor.

<!-- b000122 | prose | pages [7] -->
Regional links between users are strong.

<!-- b000123 | prose | pages [7] -->
(4)Spreading flow is small and spreading speed is slow.

<!-- b000124 | prose | pages [7] -->
(1)Same to the first period, the number of node, the degree of node, internet density and clustering coefficient are small.

<!-- b000125 | prose | pages [7] -->
(2)"Radio" node is regarded as super-spreaders and plays an important role in the information network. 1920s Radios (3)The closeness of information circulation is poor.

<!-- b000126 | prose | pages [7] -->
Regional links between users decrease.

<!-- b000127 | prose | pages [7] -->
(4)Compared with first period, the spreading flow and spreading speed increase signally.

<!-- b000128 | prose | pages [7] -->
(1)The number of node, and internet density are large, while the degree of node and the clustering coefficient are small.

<!-- b000129 | prose | pages [7] -->
(2)"Television station" node is regarded as super- spreaders and plays an important role in the 1970s TV information network.

<!-- b000130 | prose | pages [7] -->
(3)The closeness of information circulation is better. Regional links between users is poor.

<!-- b000131 | prose | pages [7] -->
(4)Compared with second period, the spreading flow and spreading speed increase signally.

<!-- b000132 | furniture | pages [8] -->
Team # 47876                                              Page 6 of 19

<!-- b000133 | prose | pages [8] -->
(1)The number of node, the degree of node, internet density and clustering coefficient are large.

<!-- b000134 | prose | pages [8] -->
(2)The condition of super-spreader is inconspicuous. 1990s Internet (3)The closeness of information circulation is well.

<!-- b000135 | prose | pages [8] -->
Regional links between users is poor.

<!-- b000136 | prose | pages [8] -->
(4)Compared with third period, the spreading flow and spreading speed increase signally.

<!-- b000137 | prose | pages [8] -->
(1)Compared with the fourth period, the number of node, the degree of node, internet density and clustering coefficient are larger.

<!-- b000138 | prose | pages [8] -->
(2)Some nodes in internet are regarded as super- spreaders and play an important role in the 2010s Phone information network.

<!-- b000139 | prose | pages [8] -->
(3)The closeness of information circulation is well.

<!-- b000140 | prose | pages [8] -->
Regional links between users is poor.

<!-- b000141 | prose | pages [8] -->
(4)Compared with fourth period, the spreading flow and spreading speed increase signally.

<!-- b000142 | prose | pages [8] -->
Notes:  Which nodes do not enter the network are not shown in the graphs.  Solid circle represents the super-spreader, and dotted circle represents the spreader.

<!-- b000143 | prose | pages [8] -->
The differential equation of information circulation network.

<!-- b000144 | prose | pages [8] -->
Based on three circulation principles, we build differential equations as follows:

<!-- b000145 | prose | pages [8] -->
 dI t ( )   I t ( )  dt  dS t ( )        S t ( ) I t ( ) S t ( )  dt (1)  dJ t ( )      S t ( ) J t ( )  dt  dR t ( )       S t ( ) J t  dt

<!-- b000146 | prose | pages [8] -->
In these equations, I(t)，S(t)，J(t) and R(t) respectively represent, at time t, the density of the unknown, the spreader, the super-spreader and the immune. The density of four types of users meets the condition of normalization:        . I t S t J t R t 1 When , this model will turn into classical SIR model. With the evolution     0, 0 of the system, when the number of spreaders is zero, the process stops and spread of network ends. And the network will only contain those who have not yet received any information and the immune who are transformed from the spreader and super-spreader.

<!-- b000147 | furniture | pages [9] -->
Team # 47876                                              Page 7 of 19

<!-- b000148 | heading | pages [9] -->
6.1.3 To solve the model

<!-- b000149 | prose | pages [9] -->
We use Matlab 2014b software to solve differential equations. By means of numerical simulations, the number of configured nodes is 1000 in the network, the initial number of spreaders is 1.

<!-- b000150 | prose | pages [9] -->
,  ,  In the initial stage,       , and       S t   I t 0 999 1000 J t 0 R t 0 0 0 1 1000 [17]. Fig 1 shows general trends of four         we assume 0.1, 0.7, 0.5, 0.3 types of nodes’ density.

<!-- b000151 | prose | pages [9] -->
Fig 2 densities of different groups in the model According to the analysis of fig 2, we can conclude:

<!-- b000152 | prose | pages [9] -->
Law one: Spreader’ density rapid increase at the initial stage. After it reaches a peak, it declines rapidly, until the spreader enters into the immune state.

<!-- b000153 | prose | pages [9] -->
Law two: The evolutionary trend of super-spreaders like that of ordinary spreaders, and it also experiences an increase, and then decrease until it disappears. However, the curve changes gently. The peak density is also much smaller than ordinary spreaders. This shows that in the online social networks, super-spreaders are a small number of "star nodes."

<!-- b000154 | prose | pages [9] -->
Law three: Ignorant density shows a rapid downward trend. And it eventually settles to a non-zero value. And that reflects the information circulation’s breadth and depth are limited and it is impossible to cover all users.

<!-- b000155 | prose | pages [9] -->
Law four: The trend of immune density is opposite to that of the ignorant. It experiences a rapid increase stage and then gradually stabilizes to a value close to 1. Rapid increase of the immune density is mainly because spreaders and super- spreaders continue turning into the immune state. And the increasing trend slows because there is no new spreader.

<!-- b000156 | prose | pages [9] -->
Law five: It is worth noting that, when information circulation stops, the density of the spreader and the super-spreader are equal to zero, but the density of the ignorant and the immune are not zero. It indicates that there are users who does not receive the information in the network. The size of information circulation has a certain limit, and it is impossible to “infect” all users.

<!-- b000157 | furniture | pages [10] -->
Team # 47876                                              Page 8 of 19

<!-- b000158 | heading | pages [10] -->
6.2 News filter model (NF)

<!-- b000159 | prose | pages [10] -->
News is defined as a report for what audiences focus [12]. The dogs bite human beings is normal, while that human beings bite dogs will become news. The reason is we focus more on human beings biting dogs. So in the light of audience’s awareness, we define audience’s awareness index (AAI). By determining the value of AAI, we can filter what qualifies as news.

<!-- b000160 | heading | pages [10] -->
6.2.1 Influential factors of audience’s awareness index

<!-- b000161 | prose | pages [10] -->
The number of audiences, the political status of audiences and the influence of information have an influence on AAI [13]. And the analysis of these factors are as follows:

<!-- b000162 | prose | pages [10] -->
The number of audiences The number of audiences is the number of persons who are concerned about this information. The more the number of the audiences is, the higher the AAI is.

<!-- b000163 | prose | pages [10] -->
The political status of audiences Higher political status of audiences, the more it can arouse the audience's attention, so AAI will be higher.

<!-- b000164 | prose | pages [10] -->
The influence of news The higher the influence of news, the higher the value of AAI.

<!-- b000165 | prose | pages [10] -->
According to foregoing analysis, there are positive correlations between the AAI and these factors.

<!-- b000166 | heading | pages [10] -->
6.2.2 The model construction

<!-- b000167 | prose | pages [10] -->
In order to calculate, we build the fuzzy comprehensive evaluation model. First, we should determine index weight matrix. Then we improve the max min algorithm and the principal of maximum membership degree among evaluation results. We build the set of factors, the set of evaluation, membership function and the set of weight [13]. Last, we comprehensively evaluate AAI. Step 1: Determine the set of evaluation object.

<!-- b000168 | prose | pages [10] -->
P = {Information to be evaluated} Step 2: Build the set of evaluation index.

<!-- b000169 | prose | pages [10] -->
   U u u u , , 1 2 3 u u u is the number of audiences, the political status of audiences and the , , 1 2 3 influence of news respectively. Step 3: Determine the universe of evaluation degree.

<!-- b000170 | prose | pages [10, 11] -->
Build a set of evaluation v，each level can correspond to a fuzzy subset。   V = v ,v ,v =A,B,C 1 2 3 Step 4: Calculate index weight Use paired comparison method and 1-9 comparative scale to calculate index weight, we have A=[0.4,0.3,0.3] Step 5: Calculate fuzzy relationship matrix R Evaluate U, and then figure out the membership degree. Finally get the fuzzy relationship matrix R.

<!-- b000171 | furniture | pages [11] -->
Team # 47876                                              Page 9 of 19

<!-- b000173 | heading | pages [11] -->
Step 6: Calculate the vector of fuzzy evaluation results B

<!-- b000174 | prose | pages [11] -->
Use the weighted average of fuzzy arithmetic operators M, to determine index weight matrix A and fuzzy relationship matrix R, and the formula is:

<!-- b000175 | prose | pages [11] -->
  p p        b ( a r ) min 1, a r , j 1,2, m (2)   i i ij i ij     i 1 i 1

<!-- b000176 | prose | pages [11] -->
Synthesizing the A and R will get the vector of fuzzy evaluation results B. According to the definition, if Bs>Bt, the value of information s is higher than that of information t. The value of vector B is AAI. Step 7: Calculate the value of AAI B  We use to indicate the value of AAI. ' CAAI=( [3,2,1]) 3 i

<!-- b000177 | heading | pages [11] -->
6.2.3 The process to test the model

<!-- b000178 | prose | pages [11] -->
We use the given four examples to test our model:  Information a: country-turned-pop singer Taylor Swift’s possible engagement today.  Information b: country-turned-pop singer Taylor Swift’s possible engagement in 1860.  Information c: an important person was assassinated today.  Information d: assassination of US President Abraham Lincoln in 1865.

<!-- b000179 | prose | pages [11] -->
Due to space limitations, the solution process omits steps 1-4. And according to step 5, we get the evaluation matrixes:

<!-- b000180 | prose | pages [11] -->
    0.1 0.6 0.3 0.1 0.4 0.5     R = 0.3 0.5 0.2 R = 0.1 0.5 0.4 ， ，     a b     0.5 0.4 0.1 0.1 0.5 0.4     (3)     0.6 0.3 0.1 0.8 0.1 0.1     R = 0.8 0.2 0 R = 1 0 0 ， ，     c d     0.7 0.2 0.1 0.9 0.1 0    

<!-- b000181 | prose | pages [11] -->
We calculate the result of evaluation vector, and we have:

<!-- b000182 | furniture | pages [12] -->
Team # 47876                                              Page 10 of 19

<!-- b000183 | prose | pages [12] -->
B   [ 0 . 3 0 , 0 . 5 4 , bB [0.10,0.46,0.44] , ， a cB  B  [0.69,0.24,0.07] [0.89,0.07,0.04] , d Then according to step 7, we have:

<!-- b000184 | prose | pages [12] -->
CAAI =0.87， CAAI =0.95 CAAI =0.71， CAAI =0.55 ， c a b d According to previous analysis, the greater value of CAAI, the greater number of audiences will be concerned about given information. So there are more reasons to explain why this information is qualified as news. In this four examples, that the US president was assassinated undoubtedly became news; and so does the important person occurred today. As for information of Taylor transition style, it is still is a news today, but if it happened 1870, perhaps it will not be concerned about.

<!-- b000185 | heading | pages [12] -->
6.3 Information circulation network prediction model (ICNP)

<!-- b000186 | prose | pages [12] -->
Information circulation network is a complex and random system, influenced by many factors. Using the statistical forecasting model to predict might have defects especially when the sample data are not enough and when historical data are volatile. Therefore, we improve the ICN model by adding BP neural network prediction model to previous model to predict information circulation network’s node number and node degree.

<!-- b000187 | heading | pages [12] -->
6.3.1 Influential factors

<!-- b000188 | prose | pages [12] -->
Comprehensive analysis of factors that influence the spread of information networks is a prerequisite to improve ICN model by using its ability of prediction.

<!-- b000189 | prose | pages [12] -->
Based on the reality of social life and the complexity of finding data, we will select the following main factors:

<!-- b000190 | prose | pages [12] -->
 Level of regional economic development The level of regional economic development is measured by regional GDP. The higher the level, the more beneficial to information circulation.

<!-- b000191 | prose | pages [12] -->
 Level of regional communication development The level of regional communication development is measured by information communication technology development index (IDI) [15]. The larger the IDI, the more beneficial to information circulation.

<!-- b000192 | prose | pages [12] -->
 Level of regional education development The level of regional education development is measured by education index (EI). The larger the EI, the more beneficial to information circulation.

<!-- b000193 | heading | pages [12] -->
6.3.2 The model construction

<!-- b000194 | prose | pages [12, 13] -->
According to the foregoing ICN model, we will build ICNP model to predict the number of node and the degree of node. The number of node determine the size of network, and the degree of node determine the capacity of the network.

<!-- b000195 | furniture | pages [13] -->
Team # 47876                                              Page 11 of 19

<!-- b000197 | prose | pages [13] -->
Similar to the general neural network model, our ICNP model’s prediction process is as follows:

<!-- b000198 | prose | pages [13] -->
Fig 3 ICNP model’s prediction process Data preprocess In this paper, data are normalized by using maximum and minimum normalization method. The data normalized formula is:

<!-- b000199 | prose | pages [13] -->


<!-- b000200 | heading | pages [13] -->
X X

<!-- b000201 | prose | pages [13] -->
 X min (4) i 

<!-- b000202 | heading | pages [13] -->
X X

<!-- b000203 | prose | pages [13] -->
max min

<!-- b000204 | prose | pages [13] -->
Determine the input number of neurons According to Hurvich’s study, when sample data is less, if using ACI criteria, there will be great estimation bias. So, based on ACI criteria, Hurvich proposed AICC criteria specifically applicable to small samples. And the formula is :

<!-- b000205 | prose | pages [13] -->
 N m (5)   AICC m ( ) N ln E   N m 2 Among the formula:

<!-- b000206 | furniture | pages [14] -->
Team # 47876                                              Page 12 of 19

<!-- b000207 | prose | pages [14] -->
 N  , N 20 ~ 40  2  N N   m ~ , N 40 ~100  (6) 3 2   N  , N 100 ~ 200  ln N

<!-- b000208 | heading | pages [14] -->
6.3.3 To solve the model

<!-- b000209 | prose | pages [14] -->
 Collect data We collect from internet, and collect data in three states: California (CA), Texas (TX) and New York (NY) in USA. And these three states have top three largest population among fifty states in USA. The reason we choose these three states are because these data are easier to find and these data samples are larger.

<!-- b000210 | prose | pages [14] -->
The data and data source are shown in the appendix.

<!-- b000211 | prose | pages [14] -->
 Validate ICN model We use data excluding the data from New York at fifth period. And then we use the ICNP model to predict the data in New York at fifth period and compare these data with present data to validate our ICN model.

<!-- b000212 | caption | pages [14] -->
Table 5 during the sample period prediction

<!-- b000213 | prose | pages [14] -->
From ICN model From predict model Relative error (%) Number of 19541453 22535000 15.32 node(person) Degree of 11223538 13533000 20.58 node(person)

<!-- b000214 | prose | pages [14] -->
 Predict future network’s relationships and capacities in 2050.

<!-- b000215 | caption | pages [14] -->
Table 6 during the sample period prediction

<!-- b000216 | prose | pages [14] -->
ICNP model Number of node(person) 34885000 Degree of node(person) 23766000

<!-- b000217 | heading | pages [14] -->
6.4 Public interest and information network interaction model (PIINI)

<!-- b000218 | prose | pages [14] -->
In the process of social information circulation networks, the circulation of information affects individuals’ preferences. We also think that individuals’ different preferences affects information circulation networks. That is same as what question said that public interest can be changed through information networks. In the meantime, information value, people’s initial opinion and bias, form of the message or its source, and the topology or strength of the information network in a region, country, or worldwide could influence public opinion.

<!-- b000219 | furniture | pages [15] -->
Team # 47876                                              Page 13 of 19

<!-- b000220 | heading | pages [15] -->
6.4.1 The model construction

<!-- b000221 | prose | pages [15] -->
Information circulation is intrinsically different from the characteristics of the spread of disease [17]. And its characteristics should consider a variety of factors. We consider only consider two factors: public interest decay and social strengthening effect Based on these two factors, we build PIINI model to reveal the interaction of public interest and information network.

<!-- b000222 | prose | pages [15] -->
Public interest attenuation mechanism The public interest decay mechanism refers to the public interest decreases when the times of receiving same information increase [18]. If users repeatedly received the same information from neighboring nodes, users will acquiesce in information being widely disseminated. Then there exists attenuation coefficient [19] which indicates users will gradually decrease their behavior of circulating information. Therefore, we introduce a saturation function to represent public interest attenuation coefficient:

<!-- b000223 | prose | pages [15] -->
     m ( ) m a be (7)

<!-- b000224 | prose | pages [15] -->
And a is the maximum attenuation rate, b is the adjustable coefficient, the is public interest attenuation coefficient and m is the number of connected users. The saturation is a non-linear increasing function. When the maximum attenuation rate a = 1, b = 1 adjustable coefficient, as m increases and nonlinear growth, indicating that the loss of interest and forwarded into a connected state more and more users. When a = 1, b = 1, when m and increases, the number of users losing interest increases. As shown in fig 4.

<!-- b000225 | prose | pages [15] -->
Fig 4 the mechanism of interest decay Social strengthening mechanism Social strengthening have nonlinear cumulative effect which have a significant effect on public interest [20]. Because of this mechanism, an individual, users will be affected by neighbors’ cumulative effects before they adopt received opinions [21].

<!-- b000226 | prose | pages [15, 16] -->
In our paper, we define the social strengthening mechanism as: the probability of a user’s behavior (including the acceptance and dissemination of information) will decrease while strengthening factor generated from neighbors’ discouragement. The larger the strengthening factor, the lower the probability of a user’s behavior (including the acceptance and dissemination of information). We use the following nonlinear function to explain the social strengthening mechanism.

<!-- b000227 | furniture | pages [16] -->
Team # 47876                                              Page 14 of 19

<!-- b000229 | prose | pages [16] -->
 n   ( ) n (8)   1 n

<!-- b000230 | prose | pages [16] -->
indicates the probability of a user’s behavior (including the acceptance and

<!-- b000231 | prose | pages [16] -->
dissemination of information), n indicates the number of connected node, is the

<!-- b000232 | prose | pages [16] -->
strengthening factor, 0 .   1

<!-- b000233 | prose | pages [16] -->
Fig 5 the social strengthening effect changed with β

<!-- b000234 | prose | pages [16] -->
As fig5 shows, the larger value of , the larger value of n. In the meantime, the

<!-- b000235 | prose | pages [16] -->
larger value of, the smaller value of.

<!-- b000236 | furniture | pages [17] -->
Team # 47876                                              Page 15 of 19

<!-- b000237 | prose | pages [17] -->
Fig 6 the social strengthening effect changed with η As fig 6 shows, when the probability is constant, the value ofwill decrease when the value  increases. It shows that by increasing the effect of social strengthening, more users will stay in the unconnected state. And therefore the number of spreaders will decrease.

<!-- b000238 | heading | pages [17] -->
Improve the information circulation model

<!-- b000239 | prose | pages [17] -->
The state of connection defined as a state that users have already received information but they are not sure whether to spread the information. And the information circulation rules are as follows:

<!-- b000240 | prose | pages [17] -->
If ignorant is concerned about received information, the ignorant will turn into spreader with a probability β; if ignorant is not concerned about received information, the will turn into the immune with a probabilityγ.

<!-- b000241 | prose | pages [17] -->
With times of circulation increasing, the spreader will gradually lose interest in transferring information to others and turn into the immune with a probability of ξ.

<!-- b000242 | prose | pages [17] -->
When the spreader meets with other spreader or immune, the spreader might not transfer the information with a probability of θ.

<!-- b000243 | prose | pages [17] -->
Social strengthening mechanism Spreader Interest attenuation mechanism θ β ξ Igorants ζ γ

<!-- b000244 | prose | pages [17] -->
Connection Immune Status

<!-- b000245 | prose | pages [17] -->
Fig 7 the circulation rules of PIINI model

<!-- b000246 | heading | pages [17] -->
The differential equations in PIINI model

<!-- b000247 | prose | pages [17, 18] -->
C t and R t indicate the density of ignorant nodes, spreader nodes, I t 、( ) S t 、( ) ( ) ( ) nodes in connection state and immune nodes when node degree is k at time t. The equations are shown below:

<!-- b000248 | furniture | pages [18] -->
Team # 47876                                              Page 16 of 19

<!-- b000250 | prose | pages [18] -->
 dI t ( )   I t ( )  dt  dS t ( )            I t ( ) ( ) ( ) S t S t ( ) C t ( )  dt (9)  dC t ( )      S t ( ) C t ( )  dt  dR t ( )      ( ) ( ) S t  dt

<!-- b000251 | prose | pages [18] -->
When , this model will degenerate to classical model SIR.       0, 0, 0

<!-- b000252 | heading | pages [18] -->
6.4.2 To solve the model

<!-- b000253 | prose | pages [18] -->
We use Matlab 2014b software to solve differential equations. By means of numerical simulations, the number of configured nodes is 1000 in the network, the initial number of spreaders is 1.

<!-- b000254 | prose | pages [18] -->
        S t         , , and we 0 1 1000 I t 0 999 1000 J t 0 R t 0 0 And             [17]. Fig 8 shows assume 0.1, 0.7, 0.5, 0.3, 0.3, 0.15 general trends of four types of nodes’ density.

<!-- b000255 | prose | pages [18] -->
Fig 8 densities of different groups in the model According to the analysis of fig 8, we can conclude:

<!-- b000256 | prose | pages [18] -->
Law one: Spreader’ density rapid increase at the initial stage. After it reaches a peak, it declines rapidly, until the spreader enters into the immune state.

<!-- b000257 | prose | pages [18] -->
Law two: The evolutionary trend nodes in connection state like that of ordinary spreaders, and it also experiences an increase, and then decrease until it disappears.

<!-- b000258 | prose | pages [18] -->
However, the curve changes gently. The peak density is also much smaller than ordinary spreaders. This indicates that in today’s online social network nodes in the connection state are a small part of all nodes. And this state of node will change quickly into the spreading state.

<!-- b000259 | furniture | pages [19] -->
Team # 47876                                              Page 17 of 19

<!-- b000260 | prose | pages [19] -->
Law three: Ignorant density shows a rapid downward trend. And it eventually settles to a non-zero value. And that reflects the information circulation’s breadth and depth are limited and it is impossible to cover all users.

<!-- b000261 | prose | pages [19] -->
Law four: The trend of immune density is opposite to that of the ignorant. It experiences a rapid increase stage and then gradually stabilizes to a value close to 1. Rapid increase of the immune density is mainly because spreaders and super- spreaders continue turning into the immune state. And the increasing trend slows because there is no new spreader.

<!-- b000262 | prose | pages [19] -->
Law five: It is worth noting that, when information circulation stops, the density of the spreader and the super-spreader are equal to zero, but the density of the ignorant and the immune are not zero. It indicates that there are users who does not receive the information in the network. The size of information circulation has a certain limit, and it is impossible to “infect” all users.

<!-- b000263 | prose | pages [19] -->
This laws are similar with previous ICN model when the super-spreader is introduced.

<!-- b000264 | prose | pages [19] -->
According to previous research, the size of information circulation [17]:

<!-- b000265 | prose | pages [19] -->
        k ( t ) R P k ( ) 1 e (10) k

<!-- b000266 | prose | pages [19] -->
The formula indicates that the ultimate size of information circulation depends on the degree distribution P (k). And the node degree plays an important role. It also verify our ICNP model which uses node degree as a viable scientific indicator to measure t . So we need information circulation network. We introduce the auxiliary function ( ) to calculate  to indicate the size of information circulation.  ( t )

<!-- b000267 | heading | pages [19] -->
7. Sensitivity Analysis

<!-- b000268 | heading | pages [19] -->
The ICN model

<!-- b000269 | prose | pages [19] -->
In ICN model, we set the parameters of differential equations, and obtain a stable solution. And it successfully describes the process of information circulation. In order to test the stability of the model, we will change the value of α, β, γ, δ, and change is set to ± 5% to observe system’s stability status.

<!-- b000270 | prose | pages [19] -->
We change only one parameter every time, and other parameters remain unchanged. Due to space limitations, we only list sensitivity analysis to parameter β with biggest change.

<!-- b000271 | prose | pages [19, 20] -->
β=0.665               β=0.700                 β=0.735 Fig 9 the sensitivity analysis of β According to fig 9, when adjust the value of parameters, the overall trend is consistent and the system can quickly reach a steady state, only the time of reaching the steady state is different. The larger the value of β, the faster the convergence.

<!-- b000272 | furniture | pages [20] -->
Team # 47876                                              Page 18 of 19

<!-- b000274 | prose | pages [20] -->
For other parameters, by adjusting their values, change is not large. Through the above sensitivity analysis we validates our model is credible within a certain range of variation, which can be ignored.

<!-- b000275 | heading | pages [20] -->
The PIINI model

<!-- b000276 | prose | pages [20] -->
Similar to the previous analysis, we change only one parameter every time, and other parameters remain unchanged, to examine whether the status of the entire system is stable. During experiments similar conclusions can be obtained that the system is not sensitive to change of parameters. So our model is credible.

<!-- b000277 | heading | pages [20] -->
The ICNP model

<!-- b000278 | prose | pages [20] -->
We use the fit test to accomplish the error analysis. And coefficient of determination (R) is used in fit test to indicate the accuracy of our model. The bigger the R, the better the model results are. According to the fig 10, R is equal to 0.99, so the model is reliable.

<!-- b000279 | prose | pages [20] -->
Fig 10 the error analysis of ICNP model Due to space limitations, we only discuss number of hidden layer nodes, and coefficient of determination and epoch. The sensitivity analysis result is shown in table 7.

<!-- b000280 | caption | pages [20] -->
Table 7 the sensitivity analysis of ICNP model

<!-- b000281 | prose | pages [20] -->
Node number 1 2 3 4 5 6 7 8 9 10 20 50 Relative error 0.62 0.49 0.34 0.14 0.28 0.31 0.24 0.47 0.52 0.22 0.24 0.77 R 0.74 0.89 0.85 0.91 0.87 0.85 0.82 0.69 0.86 0.62 0.59 0.71 Epoch 7 9 17 14 10 8 11 15 7 8 6 5

<!-- b000282 | furniture | pages [21] -->
Team # 47876                                              Page 19 of 19

<!-- b000283 | heading | pages [21] -->
8. Strengths and Weaknesses

<!-- b000284 | caption | pages [21] -->
Table 8 strengths and weaknesses

<!-- b000285 | prose | pages [21] -->
Strengths Weaknesses (1). Considering previous model, we take (1). Ignore influence between super-spreader into account. each nodes. ICN (2). The results of model conform to the (2). The result of differential model reality well according to scond model results. equation is not stable.

<!-- b000286 | prose | pages [21] -->
(1). This model is simple, but universal and (1). The determination of index NF effective to solve given problem. weight is subjective model (1). Compared with the statistical forecasting (1). Collected sample data are model, the ICNP has higher accuracy. not enough. ICNP (2). The ICNP model can successfully model validate the first model.

<!-- b000287 | prose | pages [21] -->
(1). The PIINI model can successfully (1). We only consider two PIINI indicate the interaction of public interest and major factors, but we ignore model information network. some other factors.

<!-- b000288 | heading | pages [21] -->
9. Conclusions

<!-- b000289 | prose | pages [21] -->
As a part of ICM’s Information Analytics Division, we have accomplished the given assignments. Here is the overall results of our paper.

<!-- b000290 | prose | pages [21] -->
Based on improved epidemic model, we established five network topology graphs and come to several information circulation laws: the density of the spreader and the super-spreader rapidly increase at the beginning, then they reach a peak and decline rapidly; the ignorant density shows a rapid downward trend while the immune density generally increases.

<!-- b000291 | prose | pages [21] -->
In NF model, we conclude that the assassination of Abraham Lincoln undoubtedly becomes news; and so does the important person’s assassination today. As for information of Taylor’s style transition, it becomes news today, but it might not be news in 1860.

<!-- b000292 | prose | pages [21] -->
The ICNP model validate the reliability of ICP model and predict many parameters in the information circulation network. And the results of ICNP model are: in the fifth period, node number of New York is 22535000, and its relative error is 15.32%; in the fifth period, node degree is 13533000, and its relative error is 20.58%; in around 2050, node number of New York is 34885000 and node degree is 23766000.

<!-- b000293 | prose | pages [21] -->
And we establish differential equations and solve them and we come to interaction laws: the density of the spreader and nodes in connection state rapidly increase at the beginning, they reach a peak and then decline rapidly. The ignorant density shows a rapid downward trend while the immune density generally increases.

<!-- b000294 | heading | pages [22] -->
References

<!-- b000295 | references | pages [22] -->
[1] Diekmann O, Heesterbeek J A P. Mathematical epidemiology of infectious diseases: model

<!-- b000296 | references | pages [22] -->
building, analysis and interpretation [M]. Wiley, 2000.

<!-- b000297 | references | pages [22] -->
[2] Girvan M, Callaway D S, Newman M E. Simple model of epidemics with pathogen mutation [J].

<!-- b000298 | references | pages [22] -->
Physical Review E. 2002, 65 (3): 031915.

<!-- b000299 | references | pages [22] -->
[3] Goldenberg J, Libai B, Muller E. Talk of the network: A complex systems look at the underlying

<!-- b000300 | references | pages [22] -->
process of word-of-mouth [J]. Marketing letters. 2001, 12 (3):211–223.

<!-- b000301 | references | pages [22] -->
[4] Goldenberg J, Libai B, Muller E. Using complex systems analysis to advance marketing theory

<!-- b000302 | references | pages [22] -->
development: Modeling heterogeneity effects on new product growth through stochastic cellular

<!-- b000303 | references | pages [22] -->
automata [J]. Academy of Marketing Science Review.2001, 9 (3): 1–18.

<!-- b000304 | references | pages [22] -->
[5] Granovetter M. Threshold models of collective behavior [J]. American journal of sociology. 1978:

<!-- b000305 | references | pages [22] -->
1420–1443.

<!-- b000306 | references | pages [22] -->
[6] Yang J, Leskovec J. Modeling information diffusion in implicit networks [C]. In Proceedings of

<!-- b000307 | references | pages [22] -->
the 10th International Conference on Data Mining. 2010: 599–608.

<!-- b000308 | references | pages [22] -->
[7] Massa P, Avesani P. Trust-aware Recommender Systems. Proceedings of the ACM conference on

<!-- b000309 | references | pages [22] -->
recommender systems, 2007, 17-24.

<!-- b000310 | references | pages [22] -->
[8] Jamali M, Ester M. TrustWalker: a random walk model for combining trust-based and item-

<!-- b000311 | references | pages [22] -->
based recommendation. Proceedings of the 15th ACMSIGKDD international conference on

<!-- b000312 | references | pages [22] -->
knowledge discovery and data mining, 2009, 397-406.

<!-- b000313 | references | pages [22] -->
[9] Josang A, Ismail R, Boyd C. A survey of trust and reputation systems for online service

<!-- b000314 | references | pages [22] -->
provision. Decision support systems,43(2), 2007, 618-644.

<!-- b000315 | references | pages [22] -->
[10] http://en.wikipedia.org/wiki/Social_network.

<!-- b000316 | references | pages [22] -->
[11] YangR, WangB-H, Ren J. Epidemic spreading on heterogeneous networks with  identical

<!-- b000317 | references | pages [22] -->
infectivity[J]. Physics Letters A,2007,364(3-4):189-193.Saito.

<!-- b000318 | references | pages [22] -->
[12] https://en.wikipedia.org/wiki/News.

<!-- b000319 | references | pages [22] -->
[13] https://en.wikipedia.org/wiki/Public_opinion.

<!-- b000320 | references | pages [22] -->
[14] Yonghong Hu, Enhui He, Comprehensive evaluation metho[M].Beijing: Science Press, 2000:

<!-- b000321 | references | pages [22] -->
167-188.

<!-- b000322 | references | pages [22] -->
[15] http://www.itu.int/zh/Pages/default.aspx.

<!-- b000323 | references | pages [22] -->
[16] http://www.undp.org/.

<!-- b000324 | references | pages [22] -->
[17] Chaosheng Tang, Online social network information propagation modeling and prediction of

<!-- b000325 | references | pages [22] -->
forwarding[D]Yanshan: Yanshan University,2014.

<!-- b000326 | references | pages [22] -->
[18] Liu Y, Xiao L, Liu X. Location Awareness in Unstructured Peer-to-peer Systems [J]. IEEE

<!-- b000327 | references | pages [22] -->
Transactions on Parallel and Distributed Systems, 2005,16(2):163-174.

<!-- b000328 | references | pages [22] -->
[19]Dashu Tang, Mingke He, Qingsong Meng, Based on Power Law Distribution and Small World

<!-- b000329 | references | pages [22] -->
Character unstructured P2P network searching method [J]. Computer Research and Development,

<!-- b000330 | references | pages [23] -->
2007, 44(9): 1566-1571.

<!-- b000331 | references | pages [23] -->
[20] Lü L, Chen D-B, Zhou T. The Small World Yields the Most Effective Information Spreading [J].

<!-- b000332 | references | pages [23] -->
New Journal of Physics, 2011, 13(12): 123005.

<!-- b000333 | references | pages [23] -->
[21] Karrer B, Newman M E J. Message Passing approach For General Epidemic Models [J]. Physical

<!-- b000334 | references | pages [23] -->
Review E, 2010, 82(1): 016101.

<!-- b000335 | references | pages [23] -->
[22] Nekovee M, Moreno Y, Bianconi G. Theory of Rumor Spreading in Complex Social Networks

<!-- b000336 | references | pages [23] -->
[J]. Physica A: Statistical Mechanics and its Applications, 2007, 374(1): 457-470.

<!-- b000337 | heading | pages [23] -->
Appendix (data and data source)

<!-- b000338 | caption | pages [23] -->
Table 8 Collection data

<!-- b000339 | prose | pages [23] -->
1870s 1920s 1970s Index CA TX NY CA TX NY CA TX NY IDI 1.2 0.9 0.8 1.3 1.2 1.1 2.1 1.9 1.7 EI 0.736 0.723 0.722 0.834 0.823 0.832 0.856 0.845 0.845 GDP(million 1006 615 594 11492 7027 6788 46640.4 28522.2 27553.8 US$) Number of 4574962 3067451 2418760 24465442 16403752 12934761 29943110 20076455 15830777 node(person) Degree of 2407875 1614448 1273032 4286735 2874198 2266376 5926493 3973634 3133308 node(person)

<!-- b000340 | caption | pages [23] -->
Table 9 Collection data

<!-- b000341 | prose | pages [23] -->
Index CA TX 1990s 2010s TX NY 3.4 3.2 2.9 4.39 3.87 2.34 IDI 0.876 0.877 0.867 0.968 0.976 0.987 EI 77734 47537 45923 193640 120743 115650 GDP(million US$) 33978000 22781795 17964004 36961664 24782302 19541453 Number of node (person) 10183745 6828065 5384096 21228751 14233594 11223538 Degree of node (person)

<!-- b000342 | heading | pages [23] -->
Data source:

<!-- b000343 | prose | pages [23] -->
http://news.bbc.co.uk/2/hi/technology/8552410.stm https://www.census.gov http://www.bea.gov/national/index.htm#gdp http://www.people-press.org/2012/09/27/section-1-watching-reading-and-listening-to-the-news-3/ http://data.worldbank.org.cn/ http://www.undp.org/ http://www.itu.int/zh/Pages/default.aspx
