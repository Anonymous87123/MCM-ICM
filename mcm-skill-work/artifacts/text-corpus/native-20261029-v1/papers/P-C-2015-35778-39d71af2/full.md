# P-C-2015-35778-39d71af2

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Human Capital Dynamic Network Model of Team Science

<!-- b000002 | heading | pages [1] -->
Summary

<!-- b000003 | prose | pages [1] -->
As an indispensable part of team science, managing human capital in organizations directly determines the company’s productivity. This paper tries to combine network model with team science.

<!-- b000004 | prose | pages [1] -->
Firstly, build the human capital static network: we use ICM’s 370 positions as nodes, the affiliations and cooperative relationships as edges. For different nodes of position, we define some quantified values that can reflect basic attributes of the position based on proper assumptions. By building the Post Archives simulate the real conditions. For every edge (𝑖𝑖, 𝑗𝑗), the value is 1 if and only the node 𝑖𝑖 and node 𝑗𝑗 have Matrix(PAM), we can record the internal attributes of each position. This matrix can be really helpful to

<!-- b000005 | prose | pages [1] -->
the working relationship. Then we put forward the relationship compactness calculation method, which combines affiliation and cooperative relationship, and this is applied to quantify team performance.

<!-- b000006 | prose | pages [1] -->
Secondly, build the human capital dynamic network model: we regard employees’ demission, promotion and recruitment as the main causes of network evolution and internal churn in the company. Based on the real conditions and some reasonable assumptions, we designed three evolution driving algorithms. For demission algorithm, there are two conditions: if the employee who wants to leave is in low level, he can dismiss directly; if he is in middle level, promotion and recruitment algorithm must be called to fill the position. What’s more, we consider carefully about the declination of working enthusiasm and the increasing in churn rate for surrounding people when there is one employee churn. For promotion algorithm, we determine the promotion conditions for different level to realize the layer-by-layer promotion of internal employees. Besides, promotion is always in priority to recruitment. For recruitment algorithm, we regard the 2/3 of the vacant position as recruitment plan and we build the on-position time vector to represent delaying effects.

<!-- b000007 | prose | pages [1] -->
next two years, the recruitment and training cost are 26.22σ and 140.15σ; When the churn rate reaches Thirdly, focusing on the issues that the supervisor needs us to consider, we draw the conclusions: in the

<!-- b000008 | prose | pages [1] -->
25% and 35%, working rate is steadily below 80% and bring some negative effects such as the declining of company performance and employees’ enthusiasm; The no-external recruitment policy is beneficial to maintain the company performance and working rate, but we still have to admit that it will cause the declining of enthusiasm of middle-level employees.

<!-- b000009 | prose | pages [1] -->
Finally, we regard friendships, competition and Human Capital as three network layers to describe the connection compactness in the whole team. By using the main statistical indicators (such as the average length of path), we draw the conclusion that multilayer network can reflect internal connections more precisely and comprehensively than human capital network.

<!-- b000010 | heading | pages [2] -->
Contents

<!-- b000011 | contents | pages [2] -->
1

<!-- b000012 | heading | pages [2] -->
Introduction

<!-- b000013 | prose | pages [2] -->
1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.1 Problem analysis 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.2 Literature review 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.3 Terminology and deﬁnitions 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1.4 Our work

<!-- b000014 | prose | pages [2] -->
2

<!-- b000015 | heading | pages [2] -->
Human Capital Evolution Network Model

<!-- b000016 | prose | pages [2] -->
2

<!-- b000017 | prose | pages [2] -->
3 Model overview and concepts deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 3 Human capital static network model . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 4 The main assumptions of static human capital network model 2.2.1 . . . . . . . . . .

<!-- b000018 | prose | pages [2] -->
4 The deﬁnition of node and edge . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2.2 4 Node attributes in the network . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2.3 6 The input and initialization of static network model. 2.2.4 . . . . . . . . . . . . . . .

<!-- b000019 | prose | pages [2] -->
6 Output of static network model . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2.5 7 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 Three evolution driving algorithm 7 Employee dismission algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.1 2.3.2 Employee promotion algorithm 7 . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | prose | pages [2] -->
9 Employee recruitment algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3.3 10 Simulation results of the model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.4 10 Prediction for ICM’s budget requirements . . . . . . . . . . . . . . . . . . . . . 2.4.1 10 Effects of the changing churn rate . . . . . . . . . . . . . . . . . . . . . . . . . 2.4.2 12 Effects of no external recruitment of middle-level employees . . . . . . . . . . . 2.4.3

<!-- b000021 | prose | pages [2] -->
3

<!-- b000022 | heading | pages [2] -->
Multilayer Network Model

<!-- b000023 | prose | pages [2] -->
13

<!-- b000024 | prose | pages [2] -->
16 The multilayer network for ICM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 16 The analysis of multilayer network . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2

<!-- b000025 | prose | pages [2] -->
4

<!-- b000026 | heading | pages [2] -->
Sensitivity Analysis

<!-- b000027 | prose | pages [2] -->
17

<!-- b000028 | prose | pages [2] -->
17 Uncertain effects produced by stochastic simulation . . . . . . . . . . . . . . . . . . . . 4.1 18 Subjective effects produced by some coefﬁcients 4.2

<!-- b000029 | prose | pages [2] -->
5

<!-- b000030 | heading | pages [2] -->
Conclusion

<!-- b000031 | prose | pages [2] -->
. . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | prose | pages [2] -->
18

<!-- b000033 | prose | pages [2] -->
18 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Strengths 19 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.2 19

<!-- b000034 | furniture | pages [3] -->
Team # 35778

<!-- b000035 | furniture | pages [3] -->
Page 1 of 20

<!-- b000036 | prose | pages [3] -->
1

<!-- b000037 | heading | pages [3] -->
Introduction

<!-- b000038 | prose | pages [3] -->
Human capital is an intangible asset, it is relatively abstract and it’s meaning develops with the devel- opment of our society. Pierre Bourdieu offers a nuanced conceptual alternative to human capital that

<!-- b000039 | prose | pages [3] -->
[1]. Human capital, when

<!-- b000040 | prose | pages [3] -->
includes cultural capital, social capital, economic capital, and symbolic capital

<!-- b000041 | prose | pages [3] -->
viewed from a time perspective, consumes time in one of key activities:

<!-- b000042 | prose | pages [3] -->
• Knowledge (activities involving one employee);

<!-- b000043 | prose | pages [3] -->
• Collaboration (activities involving more than 1 employee);

<!-- b000044 | prose | pages [3] -->
• Processes (activities speciﬁcally focused on the knowledge and collaborative activities generated by organizational structure-such as silo impacts, internal politics, etc.);

<!-- b000045 | prose | pages [3] -->
• Absence(annual leave, sick leave, holidays,etc.).

<!-- b000046 | prose | pages [3] -->
As the complexity of the workplace continues to grow, organizations increasingly depend on teams. Building an organization ﬁlled with good, talented, well-trained people is one of the keys to success. More and more people gradually begin to realize its charming power. So it is extremely important for the HR ofﬁce to assign employee to positions appropriate to their talents and experience. These positions are just the efﬁcient communication systems to facilitate development of innovative ideas and quality products (commodities or services).But how to manage the human capital has always been a great challenge.

<!-- b000047 | prose | pages [3] -->
1.1 Problem analysis

<!-- b000048 | prose | pages [3] -->
We focus on a more practical problem on the Information Cooperative Manufacturing (ICM) organiza- tion of 370 people, which is in a highly competitive market place.

<!-- b000049 | prose | pages [3] -->
Now, the actual situation of the organization: only 85% of its 370 positions are ﬁlled at any time. Con- sidering different position layers in which people are required to have certain years of experience, the low quality employees often stay with the company for a full career. However, mid-level positions suffer much higher turnover, and it’s often the case that churn seems to diffuse from former employees to oth- ers, so they are critical ones when consider the position changes. As for the CEO, the ratio of their salary to worker is approximately 10 times. Besides, in terms of time, the earlier an employee gains the loyalty, the more productive is the organization. What’s more, the annual evaluation based on performance is judged by the supervisor rather than the HR ofﬁce.

<!-- b000050 | prose | pages [3] -->
Our tasks:

<!-- b000051 | prose | pages [3] -->
• Build a human capital network model of ICM organization’s personnel situation that can identify dynamic processes to get certain inﬂuence such as the cost, the direct and indirect effects on organization’s productively with a certain churn rate as well as simulate or predict what will happen with a changed churn rate.

<!-- b000052 | prose | pages [3] -->
• Build a multilayer ncetwork that can connect our Human Capital network to other organizational network layers such as information ﬂow, trust, inﬂuence, and friendship.

<!-- b000053 | prose | pages [3] -->
1.2 Literature review

<!-- b000054 | prose | pages [3] -->
"Human capital" has been and continues to be criticized in numerous ways. Many researchers have en-

<!-- b000055 | prose | pages [3] -->
[2] [3]. In the early days, it is an aggregate economic view of

<!-- b000056 | prose | pages [3] -->
gaged in deﬁning and developing this concept

<!-- b000057 | prose | pages [3] -->
the human being acting within economies, which is an attempt to capture the social, biological, cultur- al and psychological complexity as they interact in explicit and/or economic transactions. Today, most

<!-- b000058 | prose | pages [3] -->
[4]-usually called

<!-- b000059 | prose | pages [3] -->
theories attempt to break down human capital into one or more components for analysis

<!-- b000060 | furniture | pages [4] -->
Team # 35778

<!-- b000061 | furniture | pages [4] -->
Page 2 of 20

<!-- b000062 | prose | pages [4] -->
"intangibles". Accordingly much more attention is paid to factors that led to success versus failure where human management is concerned. The role of leadership, talent, even celebrity is explored. How to make the best use of human capital in the organization, more speciﬁcally, to retain good people, keep them properly trained and placed in proper positions, and eventually target new hires to replace those leaving the organization has always been a challenge work.

<!-- b000063 | prose | pages [4] -->
Network has been widely used in various aspects, especially in natural science. For example, biolog- ical networks provide a mathematical analysis of connections found in ecological, evolutionary, and

<!-- b000064 | prose | pages [4] -->
[5]. In computer networks, networked computing devices

<!-- b000065 | prose | pages [4] -->
physiological studies, such as neural networks

<!-- b000066 | prose | pages [4] -->
pass data to each other along data connections (network links). As more and more people realized the power of the network, other complex networks, such as social network and business network forms the

<!-- b000067 | prose | pages [4] -->
[6]. For instance, a social network is a social structure made up of a set

<!-- b000068 | prose | pages [4] -->
nascent ﬁeld of network science

<!-- b000069 | prose | pages [4] -->
of social actors (such as individuals or organizations) and a set of the dyadic ties between these actors. Since using network in social areas is newly developed, the theory is relatively scarce and many theories are more focused on how to establish the structure of the network rather than the function-the practical use. So it is a novel perspective to build a human capital network to study how the churn and recruit employee will affect the efﬁciency of the organization. And as teams have increasingly become a way of life in many organizations, using the new concept of team science to build a human network has little been discussed.

<!-- b000070 | prose | pages [4] -->
What’s more, our life is ﬁlled with all kinds of networks, if we do more research on these networks, we may ﬁnd connection between them, especially a set of entities interact with each other in complicated pat- terns that can encompass multiple types of relationships,and it is important to take such"multilayer"features into account to try to improve our understanding of complex systems. So connect our Human Capital network to other organizational network layers such as information ﬂow, trust, inﬂuence, and friendship is just our creative and challenging work.

<!-- b000071 | prose | pages [4] -->
1.3 Terminology and deﬁnitions

<!-- b000072 | prose | pages [4] -->
• Churn: the resulting turbulence when people leaving for other jobs or retiring are replaced.

<!-- b000073 | prose | pages [4] -->
• Churn rate(turnover rate):a measure of the number of individuals or items moving out of a col-

<!-- b000074 | prose | pages [4] -->
lective group over a speciﬁc period of time,and it can be deﬁned as follows:

<!-- b000075 | prose | pages [4] -->
2NR (NS + NE) × 100% σCR(%) =

<!-- b000076 | prose | pages [4] -->
where, NR is the number of employees resigned during the month, NS is the number of employees at the start of the month and NEis the total number of employees at the end of the month.

<!-- b000077 | prose | pages [4] -->
1.4 Our work

<!-- b000078 | prose | pages [4] -->
This paper tries to combine network model with team science to deal with management issues.In section 2, we build human capital network. Firstly, in part 2 we use ICM’s 370 positions as nodes, the afﬁliations and cooperative relationships as edges to build a human capital static network model. Then in part 3 we design three evolution driving algorithms respectively which make the network change with certain initial conditions as well as the development of algorithm in time dimension. Thirdly, focused on the issues that the supervisor need us to deal with, we revise our model’s initial parameters and algorithms. Finally ,in part 4 ,based on our simulation results, we solve the issues supervisor requires and analyze effects under different conditions. In section 3, after studying the theory of multilayer network, we regard friendships, competition and afﬁliation as three network layers to describe the connection compactness in the whole team. We also ﬁnd that multilayer network can reﬂect internal connections more precisely and comprehensively than human capital network. In section 4, we do the sensitivity analysis for simulation

<!-- b000079 | furniture | pages [5] -->
Team # 35778

<!-- b000080 | furniture | pages [5] -->
Page 3 of 20

<!-- b000081 | prose | pages [5] -->
methods and some parameters. In section 5, we draw the conclusion of our model and get our strength and weakness.

<!-- b000082 | prose | pages [5] -->
2

<!-- b000083 | heading | pages [5] -->
Human Capital Evolution Network Model

<!-- b000084 | prose | pages [5] -->
2.1

<!-- b000085 | heading | pages [5] -->
Model overview and concepts deﬁnition

<!-- b000086 | prose | pages [5] -->
From the perspective of the human resources department, we build the human capital network model to reﬂect the human capital as well as its changes of each level of employees. According to the require- ments, our network should have the following functions:

<!-- b000087 | prose | pages [5] -->
• The network can clearly show the distribution of different levels of employees in each divisions or ofﬁces as well as the internal leading and being led relationships, which is the basic structure of the promotion mechanism in the organization.

<!-- b000088 | prose | pages [5] -->
• Since it is a human capital network, we must pay more attention to the main factors that can affect the human capital, which includes: the ability an employee has had when he gets the position, the productive enthusiasm of the employee, the time an employee stays in certain position and the training he obtained.

<!-- b000089 | prose | pages [5] -->
• Our human capital network is an evolutive network model. It has three fundamental dynamic phenomena: employees’ internal promotion, employees’ demission and external recruitment.

<!-- b000090 | prose | pages [5] -->
The churn of the employee is especially worrying in ICM organization that the current churn rate is 18% per year. So we should emphatically consider the how the churn rate will directly and indirectly affect the total beneﬁt and working rate (the effects on employees’ relationship and enthusiasm will also be considered). To better illustrate our human capital evolution network, the important elements and concepts are deﬁned as follows:

<!-- b000091 | prose | pages [5] -->
• Node: The nodes in the network model refer to 370 positions set up in the company. This is quite different from the nodes in a normal social network, which represents the actual person. In order to show the characteristic of these nodes more clearly, we build a matrix with 370 rows, and we call it "Post Archives Matrix" (denoted as PAM for the following illustration). In the matrix, each line represents a quantitative attribute of certain position. In order to satisﬁed the function, the quantitative attributes contains the level of position, the on-the-job condition of the position, working time and which division or ofﬁce it belongs to.

<!-- b000092 | prose | pages [5] -->
• Edge: Edge is the ditch that two points interact with each other. Focused on the present network that regard position as points, the two most direct connections are the afﬁliation in the division or the ofﬁce and the leading and being led relationship between divisions. In order to reﬂect inﬂuence of individual jobs on team work, we establish the matrix with the size of 370 × 370 to reﬂect the afﬁliation of different positions, which will be analyzed in the following part of this paper about the discussion of the teamwork.

<!-- b000093 | prose | pages [5] -->
[7],the input factors of the • Factor: Based on the description of the problem and the reference given evolution network model are the on-job-rate at the initial time and the churn rate, the output factors are the on-job-rate in the future , corporate performance, team work, the costs of recruitment and training , etc.

<!-- b000094 | prose | pages [5] -->
• Corporate performance: Our company’s corporate performance is the summation of productiv- ity in each position. In order to calculate changing performance, we consider that the maximum productivity is the summation of basic productivity in certain position and the individual experi- ence. Moreover, the actual productivity is on the base of the maximum productivity and effected by the individual working enthusiasm as well as team work, which will be illustrated in detail in our model.

<!-- b000095 | furniture | pages [6] -->
Team # 35778

<!-- b000096 | furniture | pages [6] -->
Page 4 of 20

<!-- b000097 | prose | pages [6] -->
• Minimum time unit: In our model, the minimum time unit is month, which is determined by the data given. So in each month, we will consider the number of people who submit the resignation, join the company and the people should be recruited by the company respectively as well as their enthusiasm in certain month to calculate the corporate performance in that month.

<!-- b000098 | prose | pages [6] -->
2.2

<!-- b000099 | heading | pages [6] -->
Human capital static network model

<!-- b000100 | prose | pages [6] -->
In order to obtain a network model with evolution function to assess the condition to human capital in the company, we ﬁrst build a complete Human capital static network model. The reason we call it static is that our network needs multiple dimensions to reﬂect the condition in all aspects in a certain time for the company. This static network model is the basic of evolution network. In the meanwhile, it can be used to describe the state indicator in all aspects in each time frame.

<!-- b000101 | prose | pages [6] -->
2.2.1

<!-- b000102 | heading | pages [6] -->
The main assumptions of static human capital network model

<!-- b000103 | prose | pages [6] -->
• As a network that reﬂects human capital, each node in the network represent a position and the number of position and the afﬁliation in the network are ﬁxed.

<!-- b000104 | prose | pages [6] -->
• Based on the relative date of ICM in the question, we need to divide the employee in seven levels into different divisions and ofﬁce. Here, we present a reasonable way of division, as is shown in Figure.1. The problem discussed in the following paper is based on this division structure.

<!-- b000105 | caption | pages [6] -->
Figure 1: Staff distribution structure in each division

<!-- b000106 | prose | pages [6] -->
2.2.2 The deﬁnition of node and edge

<!-- b000107 | prose | pages [6] -->
Taking the reference to the data of the structure of the company and the level of employee given in the question, we know that the network we build need to reﬂect several internal relationships. So it is neces- sary to build a network divided by different factors and then make the assignment to nodes and edges. Building the network just means deﬁning nodes and edges in the network. The relationships in the com- pany mainly have afﬁliation and the cooperative relationships: afﬁliation refers to the leading and being led relationships in divisions or between the division and its lower division; cooperative relationships refers to the cooperation of internal members in the same division, so we may as well regard that any two members have cooperative relationships in the same division. To simplify the problem, we consider the afﬁliations between divisions just the afﬁliation between two department managers. Considering that af- ﬁliation and the cooperative relationships exit simultaneously in the company, but the mutual correlation isn’t very osculating. Using reference on superposition principle in circuit ﬁeld, we abstracted the two relationships networks independently.

<!-- b000108 | prose | pages [6] -->
• Static afﬁliation network in ICM Taking the aeolotropism of afﬁliation into consideration, this network belongs to typical directed

<!-- b000109 | furniture | pages [7] -->
Team # 35778

<!-- b000110 | furniture | pages [7] -->
Page 5 of 20

<!-- b000111 | prose | pages [7] -->
network; meanwhile, there is no Intensity difference in afﬁliation, so it can be regarded as un- weighted network. This kind of network G = (V, E) can be formed by a node set V and a edge set E. The simplest way of showing afﬁliation is to represent direct connection in a matrix with a size of 370 × 370.

<!-- b000112 | prose | pages [7] -->
If there is afﬁliation in position, we deﬁne the manager as source and people being managed as target. There are total three conditions: when the source points to the target, we record 1 in certain place in the matrix; when the target points to the source, we record -1; when there is no afﬁliation, we record 0 in certain place in the matrix.

<!-- b000113 | prose | pages [7] -->
The following Figure.2 is the afﬁliation network structure. In order to better reﬂect the main characteristic in each position, we count the degree of each position and directly reﬂect it in the radius of each point. The value of the degree reﬂects the importance of this point in the whole network. The relationship is shown in Figure.2.

<!-- b000114 | caption | pages [7] -->
Figure 2: Static afﬁliation network in ICM

<!-- b000115 | caption | pages [7] -->
Figure 3: Static cooperation relationships network

<!-- b000116 | prose | pages [7] -->
in ICM

<!-- b000117 | prose | pages [7] -->
• Static cooperation relationships network in ICM For cooperation relationships in divisions or ofﬁces, since that there only exits four-team and fourteen-team two types, we can build a small network with a degree of one (there are edges between any two points) for discussion.

<!-- b000118 | prose | pages [7] -->
Considering that cooperation relationships has isotropy, this network belongs to typical undirected network; meanwhile, there are distinct Intensity differences in the network, so we regard it as weighted network. The intensity of cooperation relationship δij between position i and position j is affected by the intensity of afﬁliation αij and the intensity friendship relationship. Similarly to the former method, these are record in a matrix with a size of 370 × 370. Here, we deﬁne the intensity of afﬁliation αij is related to the shortest length dijminof the two position in the afﬁliation network, the equation can be shown as follows:

<!-- b000119 | prose | pages [7] -->
αij = dmax −dijmin

<!-- b000120 | prose | pages [7] -->
dmax

<!-- b000121 | prose | pages [7] -->
Where, dmax is the maximum of the shortest length in the network. For example, as is shown in Figure.3, the shortest length between employee3 and Exp.employee6 is 4. And the maximum length of shortest way is 5 so the relatively relationship intensity is 0.2. The intensity friendship relationship value is ﬁxed at the beginning, according the request, it will be affected by the churn of

<!-- b000122 | furniture | pages [8] -->
Team # 35778

<!-- b000123 | furniture | pages [8] -->
Page 6 of 20

<!-- b000124 | prose | pages [8] -->
employee so that it may decrease. The equation of the intensity of cooperation relationshipteam1 is shown as follows:

<!-- b000125 | prose | pages [8] -->
δteam1 =

<!-- b000126 | prose | pages [8] -->
where, n is the total number of nodes.

<!-- b000127 | prose | pages [8] -->
2.2.3 Node attributes in the network

<!-- b000128 | prose | pages [8] -->
n n

<!-- b000129 | prose | pages [8] -->
n

<!-- b000130 | prose | pages [8] -->
∑

<!-- b000131 | prose | pages [8] -->
∑

<!-- b000132 | prose | pages [8] -->
αij × βij

<!-- b000133 | prose | pages [8] -->
i=1

<!-- b000134 | prose | pages [8] -->
j=1

<!-- b000135 | prose | pages [8] -->
In the following paper, our model is start from the perspective of HR ofﬁce, so it is necessary to deﬁne the attribute of each node (position). Our processing method is:

<!-- b000136 | prose | pages [8] -->
• Set the number of ICM employees in descending order according to seven levels: From 1 to 370.

<!-- b000137 | prose | pages [8] -->
• Establish a Post Archives Matrix with 370 edges, and each edge reﬂects the working attributes in the position. The position attributes that will be used includes: division or ofﬁces the employ- ee is in, the level of the position, salary, training cost, recruitment cost, churn rate, the number of changing times, working time in the position, working enthusiasm(working efﬁciency), basic productivity in the position, on-job condition and request for departure, etc.

<!-- b000138 | prose | pages [8] -->
In these attributes, some will be refreshed because of the change of employee (such as the working time in the position, working enthusiasm(working efﬁciency), basic productivity in the position, on-job condition and request for departure) while others will stay the same. In particular, the number of changing times will continue to add one each time there is a position change to record the position condition in details. Besides, working enthusiasm is quantized through the number vary from 0 to 1.

<!-- b000139 | prose | pages [8] -->
• When there is change in position, we need to make some change in certain place in the Post archives matrix. We make the regulation: when the employee is promoted to new position, the original working time will not be retained. In other words, the working time will be record anew and this is in accord with the phenomenon that the employee will study some skills in order to adapt to the new position.

<!-- b000140 | prose | pages [8] -->
• The effect caused by training is extremely important. The company spends a certain money for training, we think that this kind of training will bring two aspects of beneﬁts: on the one hand, training can promote the level of productivity in present position, which provides theoretical sup- port when calculate productivity when consider the effect of working time; on the other hand, training can facilitate the recovery of the employee’s efﬁciency τ and restraint the rise of churn rate ν. In each time period, the equation is:

<!-- b000141 | prose | pages [8] -->
˜υ = υ −ξ2(υ −18%)

<!-- b000142 | prose | pages [8] -->
˜τ = τ + ξ1(1 −τ)

<!-- b000143 | prose | pages [8] -->
Where,ξ1 and ξ2 are the recovery coefﬁcient which indicates changing rate of the relatively ide- al value of employee’s efﬁciency per time unit and the churn rate.18% is the initial churn rate ascertained in the problem, and this value can be adjusted according to different conditions.

<!-- b000144 | prose | pages [8] -->
The input and initialization of static network model. 2.2.4

<!-- b000145 | prose | pages [8] -->
Based on the requirements and data given, it is quite convenient for us to initialize the main inputs. But there are still some phenomena and algorithms that only described qualitatively, so we need to make some reasonable assumptions for them.

<!-- b000146 | prose | pages [8] -->
• Working rate: As is stated in the task, the present working rate is 85% and middle positions cannot be vacant, so we place the vacant position evenly in low level positions.

<!-- b000147 | furniture | pages [9] -->
Team # 35778

<!-- b000148 | furniture | pages [9] -->
Page 7 of 20

<!-- b000149 | prose | pages [9] -->
• Churn rate: the given initial churn rate is 18% in the task, so we suppose that the churn rates in different levels are the same. In other words, the possibility of churn for each employee is 18% in a year.

<!-- b000150 | prose | pages [9] -->
• Recruitment rate: the determined recruitment rate is set approximately as 2/3 of the vacant po- sition, so that it has the negative feedback effect: when the number of churn employees rise, the number of recruitment employee will rise simultaneously. Besides, there is delaying effect in the process of recruitment and the speciﬁc algorithm will be illustrate in the following paper.

<!-- b000151 | prose | pages [9] -->
2.2.5

<!-- b000152 | heading | pages [9] -->
Output of static network model

<!-- b000153 | prose | pages [9] -->
Focused on human capital static network model, the main output can reﬂect the running condition of the company. We select the following datum as measurement index. The calculation of organization’s productivityφ: The company’s productivity is the sum of each employee’s productivity. Our performance is based on the following equations:

<!-- b000154 | prose | pages [9] -->
(

<!-- b000155 | prose | pages [9] -->
)

<!-- b000156 | prose | pages [9] -->
φ =⃗a

<!-- b000157 | prose | pages [9] -->
b + µ⃗c

<!-- b000158 | prose | pages [9] -->
where,

<!-- b000159 | prose | pages [9] -->
a is the row vector that record the employee’s efﬁciency in Post Archives Matrix; b is the column vector that record the employee’s basic productivity in Post Archives Matrix; c is the column vector that record the employee’s working time in Post Archives Matrix; µ a ﬁxed coefﬁcient that reﬂects the rise in employee ˛a´rs productivity per time unit. Based on the calculation method above, we can ﬁnd that the company’s productivity is affected by the churn directly and indirectly: on the one hand, the direct effect is that because there is adjustment in position, the working time will change and this is often regarded as the loss of working experience in the position in our real life; on the other hand, there are some indirect effects such as the decline in cooperation relationships and working enthusiasm caused by churn that can’t be ignored. At the same time, the churn rate will also rise. All these analyzed above will cause bad effect to the company.

<!-- b000160 | prose | pages [9] -->
2.3

<!-- b000161 | heading | pages [9] -->
Three evolution driving algorithm

<!-- b000162 | prose | pages [9] -->
After building the static network model, considering that our network model has the evolution character- istic in time dimension, we need to use evolution driving force to make the static network model develop and change. This is the source of churn in the organization.

<!-- b000163 | prose | pages [9] -->
There are three main drivers of evolution: the promotion of employees, the churn of employees and the recruitment of new employees externally. In the following section we will describe how these driving forces affect the evolution process of our network in details and then put it into operable and quanti- zable algorithm. Since the model is based on a series of bold assumptions, we will ﬁrst propose our assumptions.

<!-- b000164 | prose | pages [9] -->
2.3.1

<!-- b000165 | heading | pages [9] -->
Employee dismission algorithm

<!-- b000166 | prose | pages [9] -->
Just as the CEO is panicked when hearing that the current churn rate is 18% per year, the toughest problem the company faces is the extremely high churn rate. So the churn of employee has become the primary driving force, thus must be given priority to consideration. On the one hand, because employees in high-middle-level positions often has he high working ability, so if they churn, the company will suffer direct effects of the lower of productivity in certain position as well as the rising of recruitment cost. On the other hand, apart from direct effects, there are still some indirect effects that can’t be ignored such as the rising of churn rate or the lower of working enthusiasm in other divisions or ofﬁces. What’s more, if the vacant position needs to be ﬁlled through internal promotion, there will be a series of changes in position, which can badly affect the beneﬁt of company.

<!-- b000167 | furniture | pages [10] -->
Team # 35778

<!-- b000168 | furniture | pages [10] -->
Page 8 of 20

<!-- b000169 | prose | pages [10] -->
Aiming at ICM company, the employee churn algorithm is based on the following assumptions:

<!-- b000170 | prose | pages [10] -->
• The churn of employee is random, but throughout the year, the present churn rate is 18% (as is the case in issue 7), so we suppose the churn of employee is even throughout the year.

<!-- b000171 | prose | pages [10] -->
• If one employee put forward departure, it will cause bad effect to other employees in his division or ofﬁce (as is the case in issue 2).

<!-- b000172 | prose | pages [10] -->
• The position change, including promotion, churn and recruitment is regarded to take place once a month (the data given with the unit of per month); this assumption is always valid in the following statement.

<!-- b000173 | prose | pages [10] -->
• As is stated in the task, the mid-level positions are critical one that need to be ﬁlled all the time.

<!-- b000174 | prose | pages [10] -->
So we assume that employees in middle-low-level positions can leave the position directly but employees in middle-high-level positions must wait until there are new suitable substitutes.

<!-- b000175 | prose | pages [10] -->
Now we start to illustrate our employee dismission algorithm in detail. The churn of employee is ran- dom; here we use Monte Carlo Algorithm to simulate whether the employee will churn. Monte Carlo Algorithm is a method that uses random numbers to do the simulation experiment. It can be used to do the random observation of sampling in system we are studying, then we can do the observation statistics of the sample to obtained the possible development of system in the simulation condition.

<!-- b000176 | prose | pages [10] -->
In every month, we use Monte Carlo Algorithm to simulate whether an employee will churn and the expected churn rate is determined by the speciﬁc request in the task. Figure.4 is employee churn algo- rithm, the mainly steps are as follows:

<!-- b000177 | caption | pages [10] -->
Figure 4: Employee dismission algorithm

<!-- b000178 | prose | pages [10] -->
Step 1: Traverse every employee from high level to low level to set the churn probability according to the requirement of the question. Use Monte Carlo Algorithm to simulate the churn condition. If he churns, enter step 2; if not, repeat step 1 to test next employee.

<!-- b000179 | prose | pages [10] -->
Step 2: For churned employee, ﬁrst call Post Archives Matrix to read his level and record that he has churn tendency. Judge his level: if he is in low level then churn is permitted and return to step 1; if he is in high-middle level, then enter step 3.

<!-- b000180 | prose | pages [10] -->
Step 3: Given priority to promotion algorithm for the post mobilization in high-middle level position: if internal promotion can realize then churn is permitted meanwhile record vacancy in pre-promotion po- sition; if not, call employee recruitment algorithm and the employee can only leave till meet the median of the certain recruitment time. After that, the position is ﬁlled with new worker, the archive is refreshed.

<!-- b000181 | furniture | pages [11] -->
Team # 35778

<!-- b000182 | furniture | pages [11] -->
Page 9 of 20

<!-- b000183 | prose | pages [11] -->
To make further illustration, the analysis above contains the record of Post Archives Matrix: when churn request is put forward, position records as churn put forward; when churn happens, the number of posi- tion changing time add one and others return to initial values. Besides, if there exit the changing in other positions caused by churn, similar adjustment should be made in original position.

<!-- b000184 | prose | pages [11] -->
2.3.2

<!-- b000185 | heading | pages [11] -->
Employee promotion algorithm

<!-- b000186 | prose | pages [11] -->
Every company will give priority to promote internal employee to higher position, because this can di- rectly promote employees’ production enthusiasm. However, we must consider that only the employee with certain ability that required in a higher level position can be promoted, so that we can avoid under- mining the overall strength of the employees in the company.

<!-- b000187 | heading | pages [11] -->
The promotion of employees is based on the following assumptions:

<!-- b000188 | prose | pages [11] -->
• When one position is in vacancy, the HR ofﬁce will ﬁrst consider the promotion of internal em- ployee rather than the external recruitment.

<!-- b000189 | prose | pages [11] -->
• Whether the employee will be promoted will be affected by two conditions, which are indispens- able: for one thing, the employee’s synthetic ability meets the promotion standard; for another, there is vacancy in high level position. Once the employee meets these conditions, we consider that the employee is always willing to be promoted to higher position.

<!-- b000190 | prose | pages [11] -->
• The employee’s promotion is strictly according to the level (there are seven levels in total) given in the question, so there is no grade-skipping promotion. The employee’s is never restricted by present position, so they can be promoted to other divisions and positions.

<!-- b000191 | prose | pages [11] -->
Next, we will discuss the employee’s promotion strategy in details. Taking the promotion condition in assumption 2, we need to traverse the present position every month in order to promote the employee who meets the promotion condition to higher position to facilitate employees’ working enthusiasm. In view of the fact that the company has seven position levels, so we must ﬁrst ﬁll the position in high- er level. In other words, we need to test the vacant position in descending order. The promotion has the priority that the internal promotion has preference to external recruitment. Since the promotion the caused by employee’s churn has been discussed in employee churn algorithm, here we just consider pro- motion mechanism when there are vacant position in our promotion algorithm. Figure.5 is the employee promotion algorithm, the mainly steps are as follows:

<!-- b000192 | caption | pages [11] -->
Figure 5: Employee promotion algorithm

<!-- b000193 | prose | pages [11] -->
Step 1: Start from the highest position to check whether it is vacant. If it is vacant, enter the next level.

<!-- b000194 | prose | pages [11] -->
Step 2: In the lower level, rank the time of working time of employees who are still at position and have not put forward departure. Then select the maximum value and judge whether he meets the

<!-- b000195 | furniture | pages [12] -->
Team # 35778

<!-- b000196 | furniture | pages [12] -->
Page 10 of 20

<!-- b000197 | prose | pages [12] -->
promotion condition. Promotion condition is regard as the employee’s maximum productivity meets the initial value in higher level.

<!-- b000198 | prose | pages [12] -->
Step 3: If meets the condition, then promotion is permitted and record vacancy in the present posi- tion; otherwise, promotion isn’t permitted so the position is still vacant. Then return to step 1 to repeat the same step in next position.

<!-- b000199 | prose | pages [12] -->
To make further illustration, the Post Archives Matrix must be record timely when there exit promotion: when meets the promotion condition, the vacant position is ﬁlled and the employee-changing number adds one, other numbers return to the initial value; In the meantime , there will be new vacant position in lower level, which will be tested whether this position can be ﬁlled timely.

<!-- b000200 | prose | pages [12] -->
2.3.3

<!-- b000201 | heading | pages [12] -->
Employee recruitment algorithm

<!-- b000202 | prose | pages [12] -->
When there is vacant position but no internal employee can be promoted to this position, company must take external recruitment strategy. In the question, the recruitment of employees in different levels needs different time, which is just the delaying effect of recruitment.

<!-- b000203 | heading | pages [12] -->
The recruitment is based on the following assumptions:

<!-- b000204 | prose | pages [12] -->
• Since the median of recruitment time for employees in each level has been given, we consider that the company can always recruit suitable employees in certain time after the sending out of recruitment notice.

<!-- b000205 | prose | pages [12] -->
• The employee who is recruited should be with the lowest productivity in certain level.

<!-- b000206 | prose | pages [12] -->
• The number of the position that need recruitment should be in direct proportion to the number of present vacant position.

<!-- b000207 | prose | pages [12] -->
Next, we will illustrate the recruitment algorithm in details. Based on the churn and promotion algorithm, we ﬁnally take the recruitment algorithm. For high-middle level position, because that it isn’t permitted to be vacant, so if there is no one meets the promotion condition we will start the recruitment directly, which has been illustrated in churn algorithm. So here we will mainly illustrate recruitment algorithm in low level:

<!-- b000208 | prose | pages [12] -->
Step 1: After doing the churn and promotion algorithm, we sum up the vacant position condition in the company.

<!-- b000209 | prose | pages [12] -->
Step 2: Make use of the given recruitment rate to calculate the number of employees needed in different levels and then record it respectively in time vector which reﬂects the recruitment time. Each month, reduce one in this vector when there is recruitment plan in certain position and record the time value of the number of employee needs to be recruited in this month.

<!-- b000210 | prose | pages [12] -->
Step 3: Make initialization in Post Archives Matrix when the recruitment time reduces to zero, that means the position obtained new employee.

<!-- b000211 | prose | pages [12] -->
2.4

<!-- b000212 | heading | pages [12] -->
Simulation results of the model

<!-- b000213 | prose | pages [12] -->
2.4.1 Prediction for ICM’s budget requirements

<!-- b000214 | prose | pages [12] -->
Using our human capital evolution network model, we can commendably predict the budget require- ments in recruitment and training in two years.

<!-- b000215 | prose | pages [12] -->
• Parameters identiﬁcation The mainly parameters for the model has been given in the problem, so here we just identify a few parameters that are hard to quantify. We deﬁne these parameters to reﬂect the changes of employees’ efﬁciency and churn rate. According to our model, when ξ1=1/3, ξ2=1/3, ε% = 2%,

<!-- b000216 | furniture | pages [13] -->
Team # 35778

<!-- b000217 | furniture | pages [13] -->
Page 11 of 20

<!-- b000218 | prose | pages [13] -->
we can simulate the on-the-job rate curve in next 100 months, as is shown in Figure.6. In the ﬁgure,it’s quite clearly that the working rate ﬂuctuates around 85% at the beginning six months. Later there are some changes and ﬁnally becomes stable at 80%. This result is in accord with the real situation of ICM company.

<!-- b000219 | prose | pages [13] -->
0.86

<!-- b000220 | prose | pages [13] -->
0.85

<!-- b000221 | prose | pages [13] -->
0.84

<!-- b000222 | prose | pages [13] -->
0.83

<!-- b000223 | prose | pages [13] -->
working rate

<!-- b000224 | prose | pages [13] -->
0.82

<!-- b000225 | prose | pages [13] -->
0.81

<!-- b000226 | prose | pages [13] -->
0.8

<!-- b000227 | prose | pages [13] -->
0.79

<!-- b000228 | prose | pages [13] -->
0.78 0 10 20 30 40 50 50 60 70 80 90 100

<!-- b000229 | prose | pages [13] -->
time/month

<!-- b000230 | caption | pages [13] -->
Figure 6: The prediction of working rate

<!-- b000231 | prose | pages [13] -->
• Model results Because we use the Monte Carlo algorithm, it is inevitable that there are some ﬂuctuations. In order to deal with this problem, we simulate model 10 times to predict the cost of recruitment and training cost per month, as is shown in Figure.7, Figure.8. Calculate the average of ten simulation results , we obtain the conclusion that the budget requirements for recruitment is 26.22σ and the budget requirements for training is 140.15σ.

<!-- b000232 | caption | pages [13] -->
Figure 7: The cost of recruitment per month

<!-- b000233 | prose | pages [13] -->
• Rationality Analysis

<!-- b000234 | caption | pages [13] -->
Figure 8: The cost of training per month

<!-- b000235 | prose | pages [13] -->
According to simulation results in recruitment cost, we ﬁnd the cost is relatively stable in the beginning three months; this is affected by the hysteresis effect of low-level recruitment. Later, from the ﬁfth month to the ﬁfteenth month, recruitment cost ﬂuctuates drastically, the standard deviation is 0.955 and the highest cost per month even reached to 2.9σ. We analysis that during this period the churn effect is remarkable and the system is transiting from a stable condition to another stable condition. After the ﬁfteenth month, because the recruitment cost gradually becomes stable, the system enters a stable condition and the standard deviation is 0.156. It’s obvious from the simulation results that the training cost declines. We think that this is because every employee should be trained, so the working rate declines thus the training budget declines gradually and then reaches a stable value.

<!-- b000236 | furniture | pages [14] -->
Team # 35778

<!-- b000237 | prose | pages [14] -->
2.4.2 Effects of the changing churn rate

<!-- b000238 | furniture | pages [14] -->
Page 12 of 20

<!-- b000239 | prose | pages [14] -->
We know from the background, ICM suffers a lot from the increasing churn rate. On the one hand, the churn of employee will directly cause the declination of company’s performance; On the other hand, it can also cause indirect effects such as other employees’ working efﬁciency and churn rate which may cause the continue declination of the whole company performance. Then we suppose the churn rate reaches to 25% and 35% respectively to simulate the possible results to quantify the effects.

<!-- b000240 | prose | pages [14] -->
• Parameter idendiﬁcation The initialization parameter is the same with the former one, we only need to make some adjust- ments for ICM’s churn rate to let it to 25% and 35% respectively.

<!-- b000241 | prose | pages [14] -->
• Model results In order to describe the costs of these higher turnover rates and indirect effects of these high churn rates, we select three indicators: working rate, company performance and average enthusiasm of the employee. Then we use our model to simulate the changes of these indicators in the following 100 months and the results are as follows: When the churn rate is 25%, the working rate curve ﬁgure in the following 100 months is Fig- ure.9, the scatter diagram of total company performance per month is Figure.13 and the working efﬁciency curve ﬁgure of ICM’s employee Figure.11.

<!-- b000242 | prose | pages [14] -->
0.86

<!-- b000243 | prose | pages [14] -->
0.84

<!-- b000244 | prose | pages [14] -->
working rate when churn rate=25%

<!-- b000245 | prose | pages [14] -->
0.82

<!-- b000246 | prose | pages [14] -->
0.8

<!-- b000247 | prose | pages [14] -->
0.78

<!-- b000248 | prose | pages [14] -->
0.76

<!-- b000249 | prose | pages [14] -->
0.74

<!-- b000250 | prose | pages [14] -->
0.72

<!-- b000251 | prose | pages [14] -->
0.7 0 10 20 30 40 50 60 70 80 90 100

<!-- b000252 | prose | pages [14] -->
time/month

<!-- b000253 | caption | pages [14] -->
Figure 9: Working rate when churn rate is 25%

<!-- b000254 | prose | pages [14] -->
0.9

<!-- b000255 | prose | pages [14] -->
0.85

<!-- b000256 | prose | pages [14] -->
working rate when churn rate=35%

<!-- b000257 | prose | pages [14] -->
0.8

<!-- b000258 | prose | pages [14] -->
0.75

<!-- b000259 | prose | pages [14] -->
0.7

<!-- b000260 | prose | pages [14] -->
0.65 0 10 20 30 40 50 60 70 80 90 100

<!-- b000261 | prose | pages [14] -->
time/month

<!-- b000262 | caption | pages [14] -->
Figure 10: Working rate when churn rate is 35%

<!-- b000263 | prose | pages [14] -->
When the churn rate is 35%, the working rate curve ﬁgure in the following 100 months is Fig- ure.10 , the scatter diagram of total company performance per month is Figure.12 and the working efﬁciency curve ﬁgure of ICM’s employee is Figure.14.

<!-- b000264 | prose | pages [14] -->
1

<!-- b000265 | prose | pages [14] -->
enthusiasm when churn rate=25%

<!-- b000266 | prose | pages [14] -->
0.95

<!-- b000267 | prose | pages [14] -->
0.9

<!-- b000268 | prose | pages [14] -->
0.85 0 10 20 30 40 50 60 70 80 90 100

<!-- b000269 | prose | pages [14] -->
time/month

<!-- b000270 | caption | pages [14] -->
Figure 11: Working efﬁciency when churn rate is

<!-- b000271 | prose | pages [14] -->
25%

<!-- b000272 | prose | pages [14] -->
1

<!-- b000273 | prose | pages [14] -->
enthusiasm when churn rate=25%

<!-- b000274 | prose | pages [14] -->
0.95

<!-- b000275 | prose | pages [14] -->
0.9

<!-- b000276 | prose | pages [14] -->
0.85

<!-- b000277 | prose | pages [14] -->
0.8

<!-- b000278 | prose | pages [14] -->
0.75 0 10 20 30 40 50 60 70 80 90 100

<!-- b000279 | prose | pages [14] -->
time/month

<!-- b000280 | caption | pages [14] -->
Figure 12: Working efﬁciency when churn rate is

<!-- b000281 | prose | pages [14] -->
35%

<!-- b000282 | prose | pages [14] -->
When the churn rate is 25%: ICM’s working rate declines gradually. In the twelfth month, the working rate drops to below 80% and ultimately reaches to around 75%. The company perfor-

<!-- b000283 | furniture | pages [15] -->
Team # 35778

<!-- b000284 | furniture | pages [15] -->
Page 13 of 20

<!-- b000285 | prose | pages [15] -->
mance is continues in adjacent month, there is obvious ﬂuctuation at the beginning and gradually becomes stable. Ultimately, company performance reaches to around 179σ. In our model, em- ployees’ enthusiasm is a parameter with the value between 0 to 1 and the higher the value, the effective the employee. So this is an indirect indicator of company performance. The result of our simulation is that employees’ working efﬁciency reaches to 0.87.

<!-- b000286 | prose | pages [15] -->
195

<!-- b000287 | prose | pages [15] -->
benefit per month when churn rate=25%/¦Ò

<!-- b000288 | prose | pages [15] -->
190

<!-- b000289 | prose | pages [15] -->
185

<!-- b000290 | prose | pages [15] -->
180

<!-- b000291 | prose | pages [15] -->
average benefit per month

<!-- b000292 | prose | pages [15] -->
175

<!-- b000293 | prose | pages [15] -->
170

<!-- b000294 | prose | pages [15] -->
165 0 10 20 30 40 50 60 70 80 90 100

<!-- b000295 | prose | pages [15] -->
time/month

<!-- b000296 | caption | pages [15] -->
Figure 13: Company performance when churn rate

<!-- b000297 | prose | pages [15] -->
is 25%

<!-- b000298 | prose | pages [15] -->
195

<!-- b000299 | prose | pages [15] -->
190

<!-- b000300 | prose | pages [15] -->
benefit per month when churn rate=25%/¦Ò

<!-- b000301 | prose | pages [15] -->
185

<!-- b000302 | prose | pages [15] -->
180

<!-- b000303 | prose | pages [15] -->
175

<!-- b000304 | prose | pages [15] -->
170

<!-- b000305 | prose | pages [15] -->
165

<!-- b000306 | prose | pages [15] -->
160

<!-- b000307 | prose | pages [15] -->
average benefit

<!-- b000308 | prose | pages [15] -->
155

<!-- b000309 | prose | pages [15] -->
per month

<!-- b000310 | prose | pages [15] -->
150

<!-- b000311 | prose | pages [15] -->
145 0 10 20 30 40 50 60 70 80 90 100

<!-- b000312 | prose | pages [15] -->
time/month

<!-- b000313 | caption | pages [15] -->
Figure 14: Company performance when churn rate

<!-- b000314 | prose | pages [15] -->
is 35%

<!-- b000315 | prose | pages [15] -->
When the churn rate is 35%: ICM’s working rate declines faster than that of 25%. In the fourth month, the working rate drops to below 80% and ultimately reaches to around 67%. The company performance is continues in adjacent month, there is obvious ﬂuctuation at the beginning and gradually becomes stable. Ultimately, company performance reaches to around 153σ. The result of our simulation is that employees’ working efﬁciency reaches to 0.81, which is lower than the former result.

<!-- b000316 | prose | pages [15] -->
Based on what we have discussed above, we can draw the conclusion: with the increasing of churn rate, the working rate declines, the whole company performance slips down and the employee’s enthusiasm drops down correspondingly. To be more distinct, the direct effect is that beneﬁts of certain position declines and the indirect effect is that churn rate increases and the working enthu- siasm declines in other divisions and ofﬁces. Caused by direct and indirect effects, the company performance continually declines. In other words, churn rate has positive feedback effect that can accelerate the declination of company performance.

<!-- b000317 | prose | pages [15] -->
• Rationality analysis

<!-- b000318 | prose | pages [15] -->
The results we get is basically in accord with actual conditions in the company: under the condition that the present management method is unchanged, the more the employee churn, the faster the declination is the company performance. Only when consider the employee’s enthusiasm, we initialize it as 1 at the beginning in our model and this can be a cause of fast declination of average employee enthusiasm at the beginning.

<!-- b000319 | prose | pages [15] -->
Effects of no external recruitment of middle-level employees 2.4.3

<!-- b000320 | prose | pages [15] -->
We know from the background, ICM suffers a lot from the increasing churn rate. On the one hand, the churn of employee will directly cause the declination of company’s performance; On the other hand, it can also cause indirect effects such as other employees’ working efﬁciency and churn rate, which may cause the continue declination of the whole company performance. Then we suppose the churn rate reaches to 25% and 35% respectively to simulate the possible results to quantify the effects. The ICM HR supervisor presents us higher request for our human capital network model: in two years, there is no external recruitment of middle-level employees and we just consider internal promotion. In this way, we must make some adjustment in churn algorithm, promotion algorithm and recruitment algorithm to adapt to new regulation.

<!-- b000321 | furniture | pages [16] -->
Team # 35778

<!-- b000322 | furniture | pages [16] -->
Page 14 of 20

<!-- b000323 | prose | pages [16] -->
• Improvement for original algorithm

<!-- b000324 | heading | pages [16] -->
1) In churn algorithm, there is no extra effect for low-level employees. However, for middle-level

<!-- b000325 | prose | pages [16] -->
emoployees, they must stay until the low-level employees are able to be promoted. In order to be accord with real case, middle-level employees’ efﬁciency ε% will decline to 2%, if they have leaving tendency.

<!-- b000326 | heading | pages [16] -->
2) In recruitment algorithm, the company just recruit low-level employee. Under the condition

<!-- b000327 | prose | pages [16] -->
that the recruitment employee is 2/3 of the vacant position, the recruitment of low-level employees will increase.

<!-- b000328 | prose | pages [16] -->
• Parameter identiﬁcation The Initialization parameter is the same with the former one, we only need to make some adjust- ments for ICM’s churn rate, to let churn rate of middle-level employees to be 30% and others’ churn rate still maintains at 18%.

<!-- b000329 | prose | pages [16] -->
• Model results What are the effects for the HR health of the organization if we change the model? Here, we will describe the HR health in four indicators: working rate, company performance and average enthusiasm of middle-level employees and average change times of middle-level employees.

<!-- b000330 | prose | pages [16] -->
In order to make our simulation results directly reﬂect the effects of whether middle-level recruit- ment is permitted, we use control-variate method: that is we only change the recruitment method for middle-level position and other parameters such as churn rate stay the same. After ten times simulation, we calculate the average value of these main indicators per month to draw the gragh in order to analysis these indicators respectively.

<!-- b000331 | caption | pages [16] -->
Figure 15: Working rate of two recruitment methods

<!-- b000332 | prose | pages [16] -->
Working rate: the working rate of two different recruitment methods in two years is shown in Figure.15. Comparing the two curves, we ﬁnd that the working rate declines gradually from 85% and the working rate is higher if there is no external recruitment. From this result, we can draw the conclusion that taking the only-promotion method will decline the churn rate and this can do good to HR health.

<!-- b000333 | caption | pages [16] -->
Figure 16: Company performance of two recruitment methods

<!-- b000334 | furniture | pages [17] -->
Team # 35778

<!-- b000335 | furniture | pages [17] -->
Page 15 of 20

<!-- b000336 | prose | pages [17] -->
Company performance: the company performance of two different recruitment methods in two years is shown in Figure.16. Comparing the two curves, we ﬁnd that the company performance will gradually decrease and then become ﬂat; there is no distinct difference in the company perfor- mance: there is just a little increase if there is no external recruitment. So if we use the recruitment method that middle-level employees only promoted internally, we can slightly improve the com- pany performance and this is good to the HR health.

<!-- b000337 | caption | pages [17] -->
Figure 17: Average enthusiasm of middle-level employees of two recruitment

<!-- b000338 | prose | pages [17] -->
Average enthusiasm of middle-level employees: the average enthusiasm of middle-level employ- ees of two different recruitment methods in two years is shown in Figure.17. Comparing the two curves, we ﬁnd that the average enthusiasm is quite close in the ﬁrst ten months; after ten months, the average enthusiasm is higher if we hire the middle-level employees externally. This shows that if we use no-external recruitment method of middle-level employees, the average enthusiasm will decline. So HR ofﬁce should pay attention to it.

<!-- b000339 | caption | pages [17] -->
Figure 18: Average change times of middle-level employees of two recruitment

<!-- b000340 | prose | pages [17] -->
Average change times of middle-level employees: the average enthusiasm of middle-level em- ployees of two different recruitment methods in two years is shown in Figure.18. Comparing the two curves: if we permit external recruitment of middle-level employees, the average enthusias- m of middle-level employees will increase. We consider that this is because if we use external method, it is more convenient for employees to transfer the position. From the perspective of HR health, it will better improve the stability of the position if we permit external recruitment for middle-level employees.

<!-- b000341 | prose | pages [17] -->
Based on what have discussed above, we can draw the conclusion: from several indicators such as working rate, company performance and average enthusiasm of middle-level employees and average change times of middle-level employees, we think that it is more beneﬁcial for HR health if we use external method. Besides, although it may decrease the enthusiasm of some middle- level employee, it can greatly increase the enthusiasm of low-level employee and the stability of middle-level group.

<!-- b000342 | prose | pages [17] -->
• Rationality Analysis The results is basically in accord with the real case. What’s more, the study in human capital

<!-- b000343 | furniture | pages [18] -->
Team # 35778

<!-- b000344 | furniture | pages [18] -->
Page 16 of 20

<!-- b000345 | prose | pages [18] -->
ﬁelds also provide us following conclusions: if we use internal promotion method for middle- level employees, it will do good to personnel decision; the employee who has been working in an organization for some time can get involved in the organizational culture so that they have higher integrating degree with the organization; internal promotion can provide opportunities for each employee and this can increase the working enthusiasm; it can reduce the cost.

<!-- b000346 | prose | pages [18] -->
3

<!-- b000347 | heading | pages [18] -->
Multilayer Network Model

<!-- b000348 | prose | pages [18] -->
3.1 The multilayer network for ICM

<!-- b000349 | prose | pages [18] -->
The single layer network can only include one aspect of a problem. However, the team performance is not only inﬂuenced by working relationship but many relationships in common life. The Human Capital network is a one-layer network reﬂecting the relationship between higher level and lower level. We add the friendship network and the competition network to the human capital network. Thus we get a multi- layer network.

<!-- b000350 | prose | pages [18] -->
The multilayer network is based on the Networks ofﬁce in ICM, which consists of two divisions of 7 people. The reason why not based on the whole company is the complexity is too huge, that the number

<!-- b000351 | prose | pages [18] -->
(

<!-- b000352 | prose | pages [18] -->
n2(d+1))

<!-- b000353 | prose | pages [18] -->
[8].

<!-- b000354 | prose | pages [18] -->
of possible edges grows as O

<!-- b000355 | prose | pages [18] -->
.

<!-- b000356 | prose | pages [18] -->
The Human Capital network in this ofﬁce has been established above. And the relationship in it won ˛a´rt change anytime. For the friendship network, the edges between two nodes i,j stand for that i andj are good friends so they will attract each other. In other words, if i wants to leave ICM, j is one reason can hold i back. In the competition network, we assume the major competitions happen in peer group and all competitions are well to promote everyone to improve. The edges between two nodes i,jstand for that i and j compete with each other. Obviously, proper competitions can improve team performance which will also hold employees to stay.

<!-- b000357 | caption | pages [18] -->
Figure 19: The multilayer network for Networks ofﬁce

<!-- b000358 | prose | pages [18] -->
Figure.19 shows the whole multilayer network structure, deﬁned as M = (VM, EM, V, L).The net- work M has a total of 14 nodes, every node represent a worker,V = 1, 2, ..., 14. Three layers are connect- ed together, so theL = (L1, L2, L3). We represent the Human Capital layer as L1.he friendship layer as L2 and the competition layer as L3. Each layer contains whole 14 nodes of V .The set VM contains the whole nodes of the multilayer network.In this place it has 42 nodes. To extinguish every node in every layer, we use(i, Lj)to name the people i in the layer Lj. EM show the set which contains whole edges in M. We show the edges that remain inside of a layer as solid lines and the edges that cross layers as dotted lines. The real meaning of the solid lines has been given above. And the cross-layers-edges only couple the same people in different layers. Which means two different people can’t "communicate" in d-

<!-- b000359 | furniture | pages [19] -->
Team # 35778

<!-- b000360 | furniture | pages [19] -->
Page 17 of 20

<!-- b000361 | prose | pages [19] -->
ifferent layers. Not every cross-layers-edge is drawn in the Figure.19 just to show the meaning. To deﬁne every edge, we use((i, Lm), (j, Ln))to stand for the edge between node(i, Lm)and node(j, Ln).In ordi- nary graphs, adjacency matrices are often used to describe network. There are two methods to describe

<!-- b000362 | prose | pages [19] -->
[8]. The adjacency tensor is

<!-- b000363 | prose | pages [19] -->
multilayer networks, the adjacency tensor and the supra-adjacency matrices

<!-- b000364 | prose | pages [19] -->
named as AijLmLn For every person i in the layer Lm and person j in the layer Ln, AijLmLn has a value of 1 if and only ((i, Lm), (j, Ln))∈EM, otherwise the value is 0. And to get the supra-adjacency matric, we should use tensor ﬂattening to combine all aspects into one aspect. Then the supra-adjacency is just like normal adjacency matrices of ordinary graphs. In this paper, we deﬁne G1,G2,G3 as the adjacency matrices of every layer and GMas the supra-adjacency matrices of the multilayer network.

<!-- b000365 | prose | pages [19] -->
3.2 The analysis of multilayer network

<!-- b000366 | prose | pages [19] -->
Some important basic characters such as node degrees, clustering coefﬁcients, walks can be pretty help- ful for analyzing the graph in general singer layer network. And these characters can also be used in multilayer by aggregating data from the different layers into a monolayer network. According to the

<!-- b000367 | prose | pages [19] -->
[7] given by the question, team performance mainly affected by shared cognition. And shared

<!-- b000368 | prose | pages [19] -->
reference

<!-- b000369 | prose | pages [19] -->
cognition has positive correlation with the complexity of every aspect of the multilayer network. To explain this, we consider that:

<!-- b000370 | prose | pages [19] -->
• In the Human Capital layer, more edges or bigger degrees means one person needs to work with more people. It can make people get more training to cooperate with others so that the team performance can improve quickly.

<!-- b000371 | prose | pages [19] -->
• In the friendship layer, bigger degree for a node means this person has great relations with people which will make him/she in well mood and not want to leave.

<!-- b000372 | prose | pages [19] -->
• In the competition layer, proper competition is the best policy to promote every teammate to work efﬁciently. Besides, cooperation walks along with competition, so that people can learn a lot about teamwork.

<!-- b000373 | caption | pages [19] -->
Table 1: Main characters for networks

<!-- b000374 | prose | pages [19] -->
Average cluster The layer type Average degree

<!-- b000375 | prose | pages [19] -->
The Human Capital layer 0.929 The friendship layer 0.86 The competition network 2.214 The multilayer network 3.214

<!-- b000376 | prose | pages [19] -->
Average path length Graph density

<!-- b000377 | prose | pages [19] -->
0 2.978 0.143 0 1.632 0.11 1 1 0.341 0.638 1.571 0.484

<!-- b000378 | prose | pages [19] -->
Table.1 gives out the main character conclusions of three monolayer networks and the multilayer net- work. We can ﬁnd that every character of the multilayer network shows more detail information than monolayer networks. Using multilayer network can simulate the social relations more clearly than only using one monolayer network. We draw conclusions:

<!-- b000379 | prose | pages [19] -->
• The HR ofﬁce should use more detail data in this multilayer network to simulate the inﬂuence of churn.

<!-- b000380 | prose | pages [19] -->
• The competition network is important in teams, the company can divide divisions more scientiﬁ- cally to make teams in well competition.

<!-- b000381 | prose | pages [19] -->
4

<!-- b000382 | heading | pages [19] -->
Sensitivity Analysis

<!-- b000383 | prose | pages [19] -->
Our algorithm use Monte Carlo random numbers and some coefﬁcients determined by experience. This may bring to uncertainty effects and subjective effects. To analyze this inﬂuence we see these matters as independent variable and observe some important outcomes.

<!-- b000384 | furniture | pages [20] -->
Team # 35778

<!-- b000385 | furniture | pages [20] -->
Page 18 of 20

<!-- b000386 | prose | pages [20] -->
4.1 Uncertain effects produced by stochastic simulation

<!-- b000387 | prose | pages [20] -->
To observe the stochastic error produced by stochastic simulation. We use the working rate as the out- put and get the output in same situation by 6 times. Then take 6 groups (a1, a2, a3, a4, a5, a6)into the formula.

<!-- b000388 | prose | pages [20] -->
w = (a1 + a2 + a3) −(a4 + a5 + a6)

<!-- b000389 | prose | pages [20] -->
3 While the w represent the stochastic error. Figure.20 show us the stochastic error produced by the random process. The maximum of the error is under 0.015 which is small enough. So the stochastic error is under the limited range that we can assume it won ˛a´rt affect the output too much.

<!-- b000390 | caption | pages [20] -->
Figure 20: The stochastic error

<!-- b000391 | caption | pages [20] -->
Figure 21: The working rate under different growth

<!-- b000392 | prose | pages [20] -->
coefﬁcient

<!-- b000393 | prose | pages [20] -->
4.2 Subjective effects produced by some coefﬁcients

<!-- b000394 | prose | pages [20] -->
Because of the limited data some coefﬁcients are determined by experience. In order to analyze the inﬂuence of these subjective effects, we choose two important coefﬁcients to change slightly and observe what happen.

<!-- b000395 | prose | pages [20] -->
• Change the attenuation coefﬁcient produced by unsuccessful promotion of job When a worker is full ﬁlled with the condition of promotion, his working efﬁcient will decline if he can’t get promoted. The attenuation coefﬁcient is set as 0.95 by experience. We change this value into 0.90, 0.93, 0.95 and 0.97 to observe what happened to company performance. From the result we ﬁnd that when the value is more than 0.93 the company performance didn’t change obviously.

<!-- b000396 | prose | pages [20] -->
• Change the growth coefﬁcient of turnoff rate produced by churn When a people leave company will lead to a churn, which will promote some people surrounding to have more possibility to leave. The growth coefﬁcient is set as 1.02 by experience. We change this value into 1.05, 1.07, 1.10 and 1.13 to observe what happened to the working rate of company. A graph is given to describe the result. Figure.21 shows the change of working rate under different coefﬁcient value. The values 1.02, 1.05, 1.07, 1.10 and 1.13 stand for the different number of the growth coefﬁcient. We can ﬁnd that when the value is more than 1.07 the output didn’t change obviously. That means the value set as 1.02 won ˛a´rt cause too much inﬂuence on the outcomes. So it is proper to set this value as 1.02.

<!-- b000397 | prose | pages [20] -->
5

<!-- b000398 | heading | pages [20] -->
Conclusion

<!-- b000399 | prose | pages [20] -->
As an indispensable part of team science, managing human capital in organizations directly determines the company’s productivity. This paper tries to combine network model with team science. Firstly, we use ICM’s 370 positions as nodes, the afﬁliations and cooperative relationships as edges to build

<!-- b000400 | furniture | pages [21] -->
Team # 35778

<!-- b000401 | furniture | pages [21] -->
Page 19 of 20

<!-- b000402 | prose | pages [21] -->
a human capital static network model. In our model, we establish Post Archives Matrix to record the internal attributes of each position so that we can quantize some abstract concepts such as cooperative relationships reasonably. Secondly, we regard turnover, promotion and recruitment as main causes of network evolution and internal churn in the company. Then we design three evolution driving algorithms respectively which make the network change with certain initial conditions as well as the development of algorithm in time dimension. Thirdly, focused on the issues that the supervisor need us to deal with, we revise our model’s initial parameters and algorithms. Based on our simulation results, we obtain our predictions for these issues and analyze effects. Fourthly,after studying the theory of multilayer network, we regard friendships, competition and afﬁliation as three network layers to describe the connection compactness in the whole team. We also ﬁnd that multilayer network can reﬂect internal connections more precisely and comprehensively than human capital network. Finally,we do the sensitivity analysis for simulation methods and some parameters

<!-- b000403 | prose | pages [21] -->
5.1

<!-- b000404 | heading | pages [21] -->
Strengths

<!-- b000405 | prose | pages [21] -->
• We build a Post Archives Matrix to show the internal attributes of nodes. For one thing, we can use it to describe each position; For another, when an employee transfer from one position to another, he can bring the archives them him and initialize the original position.

<!-- b000406 | prose | pages [21] -->
• We consider the afﬁliations and cooperative relationships as edges to connect positions. Afﬁlia- tions are the bridges for the company’s operation and cooperative relationships are the roll booster for team beneﬁts. In the model, we combine these to relationships together and derive the equation of team work to qualify the connection compactness for a team.

<!-- b000407 | prose | pages [21] -->
• Network evolution is based on the connection and effects of three algorithms. There is an order in employees’ demission, promotion and recruitment. Based on the requirements, we determine a set of strategies for the real churn in ICM company and then use it solve the requests in the task.

<!-- b000408 | prose | pages [21] -->
• The details in algorithms are in accord with real conditions. We use it realize the reasonable quantiﬁcation of abstract factors. For example, in order to describe the bad effects caused by churn employees, we quantify employees’ working enthusiasm and the changing churn rate. There is another example: we consider the effect of training and ﬁnd that training can increase the working enthusiasm and at the same time decrease the demission possibility.

<!-- b000409 | prose | pages [21] -->
5.2

<!-- b000410 | heading | pages [21] -->
Weaknesses

<!-- b000411 | prose | pages [21] -->
• Different divisions’ effects and operation in ICM company should be regarded as another network to study. Considering the lacking of conditions and the time for us is limited, we don’t make further study in this aspect.

<!-- b000412 | prose | pages [21] -->
• Our model doesn’t consider the effects of the employees who retire or leave their position tem- porarily.

<!-- b000413 | furniture | pages [22] -->
Team # 35778

<!-- b000414 | furniture | pages [22] -->
Page 20 of 20

<!-- b000415 | heading | pages [22] -->
References

<!-- b000416 | references | pages [22] -->
[1] The Forms of Capital: English version published 1986 in J.G. Richardson’s Handbook for Theory

<!-- b000417 | references | pages [22] -->
and Research for the Sociology of Education, pp. 241-258.

<!-- b000418 | references | pages [22] -->
[2] Spence, Michael (1973). "Job Market Signaling". Quarterly Journal of Economics 87(3): 355-

<!-- b000419 | references | pages [22] -->
374. doi:10.2307/1882010.

<!-- b000420 | references | pages [22] -->
[3] The Forms of Capital: English version published 1986 in J.G. Richardson’s Handbook for Theory

<!-- b000421 | references | pages [22] -->
and Research for the Sociology of Education, pp. 241-258.

<!-- b000422 | references | pages [22] -->
[4] Paolo Magrassi (2002) "A Taxonomy of Intellectual Capital", Research Note COM-17-1985,

<!-- b000423 | references | pages [22] -->
Gartner.

<!-- b000424 | references | pages [22] -->
[5] Proulx, S. R.; Promislow, D. E. L.; Phillips, P. C. (2005). "Network thinking in ecology and

<!-- b000425 | references | pages [22] -->
evolution". Trends in Ecology and Evolution 20 (6): 345-353.doi:10.1016/j.tree.2005.04.004.

<!-- b000426 | references | pages [22] -->
PMID 16701391.

<!-- b000427 | references | pages [22] -->
[6] Borgatti, Stephen P.; Mehra, Ajay; Brass, Daniel J.; Labianca, Giuseppe (2009). "Network

<!-- b000428 | references | pages [22] -->
Analysis in the Social Sciences". Science 323(5916): 892-895. doi:10.1126/science.1165821.

<!-- b000429 | references | pages [22] -->
[7] E. Salas, N.J. Cooke, and M.A. Rosen. (2008). On Teams, Teamwork, and Team Performance:

<!-- b000430 | references | pages [22] -->
Discoveries and Developments. Human Factors: The Journal of the Human Factors and Er-

<!-- b000431 | references | pages [22] -->
gonomics Society June 2008 vol. 50 no. 3 540-547.

<!-- b000432 | references | pages [22] -->
[8] Mikko Kivel a, Alexandre Arenas, Marc Barthelemy, James P. Gleeson, YamirMoreno, Mason A.

<!-- b000433 | references | pages [22] -->
Porter. (2013). Multilayer Networks, J. Complex Networks, 2(3):203-271 (2014); arXiv preprint

<!-- b000434 | references | pages [22] -->
arXiv:1309.7233, 2013.

<!-- b000435 | references | pages [22] -->
[9] Hellmann T, Staudigl M. Evolution of social networks[J]. European Journal of Operational

<!-- b000436 | references | pages [22] -->
Research, 2014, 234(3): 583-596.

<!-- b000437 | references | pages [22] -->
[10] Long Q. Three-dimensional-ﬂow model of agent-based computational experiment for complex

<!-- b000438 | references | pages [22] -->
supply network evolution[J]. Expert Systems with Applications, 2015, 42(5): 2525-2537.

<!-- b000439 | references | pages [22] -->
[11] Garc´lła-Herrero S, Mariscal M A, Guti´l˛errez J M, et al. Using Bayesian networks to analyze

<!-- b000440 | references | pages [22] -->
occupational stress caused by work demands:

<!-- b000441 | references | pages [22] -->
Preventing stress through social support[J].

<!-- b000442 | references | pages [22] -->
Accident Analysis, 2013, 57: 114-123.
