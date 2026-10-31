# P-C-2015-33572-b32fb4b1

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For ofﬁce use only For ofﬁce use only

<!-- b000003 | title | pages [1] -->
33572

<!-- b000004 | prose | pages [1] -->
T1 F1 T2 F2 T3 F3 Problem Chosen T4 F4

<!-- b000005 | title | pages [1] -->
C

<!-- b000006 | heading | pages [1] -->
2015 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000007 | prose | pages [1] -->
Simulation company:

<!-- b000008 | prose | pages [1] -->
a dynamic model based on the Multiplex Network

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
In order to build a Human Capital Network model inside an organization, our idea is to establish a comprehensive model with plentiful properties of nodes which are consistent with the actual situations. Therefore, the concept of Multiplex Net- work is introduced to enrich the nodes’ characteristics. What’s more, the notion of automaton is applied to present the dynamic process within the company.

<!-- b000011 | prose | pages [1] -->
Based on the desire for simulating the reality more vividly, a multiplex net- work with speciﬁc assumptions describing the occupation distribution methods is selected rather than a single-layer network. Having considered about the complex- ity of human beings, four typical layers are explored to describe the relationship within the organization. The four subnets of the multiplex network are Friend- ship Network, Department Network, Leadership Network and Information Flow Network. The multiplex network of the Human Capital Network is set up after connecting the four layers together. And the four effect indexes, namely, friend- ship inﬂuence index, department inﬂuence index, leader changing inﬂuence index and message inﬂuence index are calculated to evaluate each subnets’ impact on the personnels.

<!-- b000012 | prose | pages [1] -->
Since the static network is gained, the dynamic process is divided into ﬁve events covering common scenarios like demission, promotion, transfer, recruit- ment and settlement to drive the network. Besides, some concepts are deﬁned before the course of evolution. Moreover, the demission index consists of the above four indexes and the occupation dissatisfaction index is proposed to measure the churn rate in the company. And the evaluation on the further inﬂuence on organi- zation’s productivity is conducted under the churn value of 18% in a decade.

<!-- b000013 | prose | pages [1] -->
The prediction about the company’s budget in the next two years indicates the ability of the algorithm serving for the above ﬁve events. After simulations of the process, the total recruiting budget is 32.8σ and the budget of training is 141.79σ.

<!-- b000014 | prose | pages [1] -->
The accuracy and stability of the Human Capital Network are proved by the sensitivity analysis on the changing churn rate. And ICM can not sustain its 80% full status no matter the annual churn rate is 25% or 35%. Task Five reﬂects the rationality of the construction method of the model due to the fact that ICM can sustain its 56.8% status under such extreme conditions.

<!-- b000015 | keywords | pages [1] -->
Key Words: Multiplex Network; Automaton; Churn rate; Dynamic processes

<!-- b000016 | furniture | pages [2] -->
Team # 33572

<!-- b000017 | furniture | pages [2] -->
Page 1 of 20

<!-- b000018 | heading | pages [2] -->
1 Introduction

<!-- b000019 | heading | pages [2] -->
1.1 Background

<!-- b000020 | prose | pages [2] -->
The company economic beneﬁt were limited much when the company organizations were lengthy and jumbled in the past. And the appearance of Human resource (HR) as a newly- developing discipline marks the arrival of Knowledge Management era. Human Capital con- cept is put forward to emphasize the importance of human resource management within the produce performance. Hence, as industries move from manual to more managerial professions so does the need for more highly skilled graduates.

<!-- b000021 | prose | pages [2] -->
HR specialists are hired to help senior leadership improve the corporate structure, provide mature ofﬁcers continuing education projects and foster an enterprise culture. Especially, lead- ers intend to establish an effective company structure where staff can get work training and remuneration as they deserve. Besides, priority promotions are given to employees who are more experienced. These talent managements and team building aspects of HR management improve the sense of belonging of each clerk and rise the company outcomes.

<!-- b000022 | prose | pages [2] -->
Therefore, it is necessary to build a Human Capital Network to reﬂect the dynamic pro- cess of HR. Thus, it would be much easier for senior managers to monitor and control skilled personnels in order to prevent them from turning over. Moreover, analyzing the network en- ables employers to optimize Workforce Management for saving money and contributes to the remake of companies in the end.

<!-- b000023 | heading | pages [2] -->
1.2 Problem Restatement and Analysis

<!-- b000024 | prose | pages [2] -->
Firstly, combining with the given nine issues, the HR manager requires writers to set up a model with bold assumptions to reﬂect the dynamic process within the human resource. Re- ferring to bibliography, the science of team science[1] and some discoveries on teamwork are applied to the modelling. What‘s more, a multi-layered model is taken into account to describe the connections among human capital, information ﬂow, friendship and so on. Having consid- ered about the speciﬁc situation within the networks, a multiplex network is used. The edges in the multiplex network link the same node in different layers and it satisﬁes our requirements. Therefore, on the basis of the multiplex network, our model is established to show the organi- zational churn and its inﬂuence on the company beneﬁts. As preparation we need to propose a dynamic occupation distribution method to allocate 370 positions into the comprehensive organizational graph.

<!-- b000025 | prose | pages [2] -->
Secondly, a vivid dynamic process involved in organizational churn should be presented. We decide to fulﬁll this through model simulation. The data obtained from simulating can ex- plain this course and its direct and indirect effects on the organization productivity. In addition, integrating the data with Table 1 in the problem, the organization‘s budget for talent manage- ment in terms of for both recruiting and training over the next 2 years should be worked out.

<!-- b000026 | prose | pages [2] -->
Finally, the HR manager asks authors evaluate sensitivity and robustness of the multilay- ered model by changing the annual churn rate and adding extra conditions.

<!-- b000027 | prose | pages [2] -->
Having considered about all the requirements above, our goal is to construct a four-layered model to simulate the behavior of turning over and gain further analysis and answers for the problem.

<!-- b000028 | furniture | pages [3] -->
Team # 33572

<!-- b000029 | furniture | pages [3] -->
Page 2 of 20

<!-- b000030 | heading | pages [3] -->
2 Bold Assumptions

<!-- b000031 | prose | pages [3] -->
• Efﬁciency man gets promotion eliminating other personal reasons;

<!-- b000032 | prose | pages [3] -->
• No discharge and demotion except for special cases;

<!-- b000033 | prose | pages [3] -->
• Demission, promotion, transfer and recruitment happen in the beginning of the month while settlement happens in the end of the month;

<!-- b000034 | prose | pages [3] -->
• The posting diagram is dynamic and thus has universality which means the model is suitable for multiple post distribution methods;

<!-- b000035 | prose | pages [3] -->
• The churn rate remains constant except for speciﬁc requirements;

<!-- b000036 | prose | pages [3] -->
• Administrative clerk can not be promoted to any other positions;

<!-- b000037 | prose | pages [3] -->
• The organizational churn rate is only related to the demission index.

<!-- b000038 | prose | pages [3] -->
Under the bold assumptions proposed in the paper, the occupation distribution method and the multiplex model can be designed later.

<!-- b000039 | heading | pages [3] -->
3 Symbol Description

<!-- b000040 | prose | pages [3] -->
In the section, we deﬁne some symbols when constructing the model as follows.

<!-- b000041 | caption | pages [3] -->
Table 1: Symbol Description

<!-- b000042 | heading | pages [3] -->
Symbol

<!-- b000043 | prose | pages [3] -->
Description X The set of personnels.

<!-- b000044 | prose | pages [3] -->
J The set of 7 kinds of jobs.

<!-- b000045 | prose | pages [3] -->
NP S The total number of company personnels.

<!-- b000046 | prose | pages [3] -->
NP M The number of middle managers.

<!-- b000047 | prose | pages [3] -->
Ab The current capacity value.

<!-- b000048 | prose | pages [3] -->
AbG Growth limitation.

<!-- b000049 | prose | pages [3] -->
AbN Position threshold.

<!-- b000050 | prose | pages [3] -->
PC Churn rate.

<!-- b000051 | heading | pages [3] -->
4 Model Preparation: occupation distribution

<!-- b000052 | prose | pages [3] -->
A comprehensive organizational graph describing the corporate structure is given by the HR manager. It is signiﬁcant to determine the occupation distribution before the construction of multi-layered networks. Because persons in different level of positions have diverse char- acteristics and thus the network structures among nodes vary from one plan to other plans. Therefore, it is necessary for us to work out an appropriate distribution plan to allocate 370 positions into the comprehensive organizational graph. What’s more, the arrangement should be dynamic and ﬂexible so that the model based on it could be universal. Several assumptions are made before the distribution as below.

<!-- b000053 | furniture | pages [4] -->
Team # 33572

<!-- b000054 | furniture | pages [4] -->
Page 3 of 20

<!-- b000055 | prose | pages [4] -->
• Divide the graph into two parts. The ﬁrst three layers are regarded as management layer and the latter two are called executive layer. The arrangements are completely indepen- dent from one another.

<!-- b000056 | prose | pages [4] -->
• The distribution order is arranged from top to bottom and left to right as well. And each department adopts one position at a time.

<!-- b000057 | prose | pages [4] -->
• The managers in the management layer are senior manager (SM) and junior manager (JM) while the mangers in the executive layer are experienced supervisor (ES) and inex- perienced supervisor (IS). SM is prior to JM and ES is prior to IS.

<!-- b000058 | prose | pages [4] -->
• Each department can only have one manager except for CEO and branchs. CEO and branches can have several managers in the mean while.

<!-- b000059 | prose | pages [4] -->
• The priority list of the rest of employees in the ofﬁce is administrative clerk (AC), expe- rienced employee (EE) and inexperienced employee (IE) respectively. The priority list of the rest of employees in the division is EE and IE.

<!-- b000060 | prose | pages [4] -->
• Allocate the ﬁrst place positions to the department as much as possible. Then the posi- tions in the second place is used to ﬁll the vacancies.

<!-- b000061 | prose | pages [4] -->
After applying the rules to the organizational graph, an occupation distribution diagram is drawn in Figure 1.

<!-- b000062 | prose | pages [4] -->
Management CEO SM layer 3*SM/JM/AC

<!-- b000063 | prose | pages [4] -->
Sales Research HR VP Facilities Marketing SM/JM CIO* CFO* SM/JM SM/JM SM/JM SM/JM 3*AC/EE/IE 3*AC/EE/IE 3*AC/EE/IE 3*AC/EE/IE 3*AC/EE/IE

<!-- b000064 | prose | pages [4] -->
Program Production Plant Plant World Networks* Information* Regional* Internet* Manager* Manager* Blue* Green* Wide*

<!-- b000065 | prose | pages [4] -->
Executive Director Management Branch* ES/IS * layer 3*AC/EE/IE

<!-- b000066 | prose | pages [4] -->
DIvision DIvision DIvision DIvision SM/JM SM/JM Branch* Branch* ES/IS ES/IS 6*EE/IE 6*EE/IE 6*IS/EE/IE 6*IS/EE/IE

<!-- b000067 | caption | pages [4] -->
Figure 1: Occupation distribution diagram

<!-- b000068 | prose | pages [4] -->
From Figure 1, the distribution plan is dynamic due to the fact that once someone leave the organization, his or her position can be replaced by other positions. For instance, an AC working in a VP ofﬁce quits his or her job and it is much easier for the VP ofﬁce to ﬁnd an EE or IE or another AC to replace her rather than only AC is feasible. Hence, the multi-layered network based on it is suitable for many organization structures.

<!-- b000069 | heading | pages [4] -->
5 A multiplex network construction: Human Capital Network model

<!-- b000070 | prose | pages [4, 5] -->
The concept of multiplex network [5] is introduced due to the consideration of personnels’ properties. An employee’s characteristics consist of several factors like the organization po- sition in a department, the connections between him and his friends, the leading role of his supervisors and the atmosphere among the organization and so on. Besides, in Task Six, the HR manager asserts that the HR ofﬁce should take the lead in the effort to connect network models of the organization, fulﬁlling the talent management. Therefore, the consideration of nodes’ properties in the human capital network counts on not only the characteristics of De- partment Network but also other networks such as Information Flow Network, Friendship Network and Leadership Network. Hence, a multiplex network is needed to combine all the factors we think about in different networks so that a comprehensive model can be set up.

<!-- b000071 | furniture | pages [5] -->
Team # 33572

<!-- b000072 | furniture | pages [5] -->
Page 4 of 20

<!-- b000074 | prose | pages [5] -->
First, a Department Network based on the occupation distribution diagram is constructed to describe the relationship inside the division or ofﬁce. And the index of departmental cohe- siveness is obtained. Then, the other three networks are used for reference. The structuring methods are explained and three equations to compute the inﬂuence index in each network is worked out below. Finally, the Department Network is connected with the other three net- works to gain the considerate network model, namely, Human Capital Network.

<!-- b000075 | heading | pages [5] -->
5.1 First layer: Department Network

<!-- b000076 | prose | pages [5] -->
The deﬁnition of the Department Network is GH = (VH, EH) where VH = X; EH stands for the relationship between an employee and the organization.

<!-- b000077 | prose | pages [5] -->
The Department Network details the occupation distribution diagram in respect of working divisions inside the department. And the part of the Department Network graph is drawn in

<!-- b000078 | caption | pages [5] -->
Figure 2.

<!-- b000079 | caption | pages [5] -->
Figure 2: The partial graph represents the typical construction inside the department where the rest of

<!-- b000080 | prose | pages [5] -->
the divisions and ofﬁces are similar to it. The seven staffs are divided into two parts which are the leader part consisting one person and the subordinate part consisting six persons respectively. The classiﬁcation method inside the department makes the distribution diagram more distinct.

<!-- b000081 | prose | pages [5] -->
From Figure 2, the Department Network is established by considering personnels inside the department as nodes while the connections between parent departments and child depart- ments are regarded as edges. Besides, there is no link among departments in the same layer. Thus the edges reﬂect the promotion path in the organization.

<!-- b000082 | prose | pages [5, 6] -->
Moreover, the change in the number of staffs within the department will inﬂuence the de- partmental cohesiveness. For example, a division with adequate and experienced employees has greater power of execution than a division lack of manpower. It means that working mem- bers in an outstanding department are much closer and work together to gain ofﬁce honour while people in a downhill department are more willing to leave. This phenomenon can be demonstrated by the index of department inﬂuence. And its calculation formula is listed be- low.

<!-- b000083 | furniture | pages [6] -->
Team # 33572

<!-- b000084 | furniture | pages [6] -->
Page 5 of 20

<!-- b000086 | prose | pages [6] -->
HD(x) IH(x) = (1) HM (x) −1 (x) is the job vacancy in node x’s department; HM (x) is the amount of positions in node x’s department. where x ∈X; HD

<!-- b000087 | heading | pages [6] -->
5.2 The other three layers: Friendship, Leadership and Information ﬂow Network

<!-- b000088 | prose | pages [6] -->
Task Six requires authors to connect Department Network to other organizational network layers such as information ﬂow, trust, inﬂuence, and friendship. After digging into the ref- erence and considering reality factors, the layers are simpliﬁed into three layers which are leadership, friendship and information ﬂow. The clerk loyalties to the ofﬁce complex and to subgroups mainly lie on the ability of a leader. And to great extent, a leader has great inﬂu- ence on the employee loyalties to the ofﬁce complex and to subgroups. Hence, it is sensible to classify trust and leader inﬂuence into the leadership layer.

<!-- b000089 | prose | pages [6] -->
The deﬁnition of the three networks are as follow.

<!-- b000090 | prose | pages [6] -->
• Friendship Network: GF = (VF , EF ) where VF = X; EF represents the undirected edge describing the friendship between two persons;

<!-- b000091 | prose | pages [6] -->
• Information ﬂow Network: GM = (VM, EM) where VM = X; EM stands for the undi- rected edge showing the information path among nodes;

<!-- b000092 | prose | pages [6] -->
• Leadership Network: GL = (VL, EL) where VL = X; EL is the directed edge pointed from immediate boss to their subordinates;

<!-- b000093 | prose | pages [6] -->
(A) (B) (C)

<!-- b000094 | caption | pages [6] -->
Figure 3: The three charts describe the same division with seven personnels. Chart A is a Friendship

<!-- b000095 | prose | pages [6] -->
Network and the edge between two nodes shows a friend relationship. The negative emotion of an em- ployee will pass on to his friends and lead to herd mentality. Chart B is a Information Flow Network and the edge between two nodes stands for the communication links. Once a clerk who is short-tempered talks to others, working atmosphere becomes stiﬂing. However, the connections between friends are much stronger than colleagues. Chart C is a Leadership Network and it is an oriented graph. The edge linking from supervisors to underlings represents the impact of leaders on their subordinates. Therefore, if a leader resign his position or is pointed to other positions, the morale of his department is sinking lower.

<!-- b000096 | furniture | pages [7] -->
Team # 33572

<!-- b000097 | furniture | pages [7] -->
Page 6 of 20

<!-- b000098 | prose | pages [7] -->
What is noticeable is that due to the lack of real data, all the three networks can only be established by virtual data which is in good agreement with life experience and theory in the reference. For example, certain information topics can only be assumed to simulate the message trafﬁc among personnels. Still, evaluations on the inﬂuence of the information network can be operated with the experience of daily conversations. Moreover, the Leadership Network is a directed tree graph where edges are pointed from immediate boss to their subordinates. Such linking method shows leaders’ impacts on the employees.

<!-- b000099 | prose | pages [7] -->
Then, according to the network theory, the nodes are considered as working staffs and use edges to describe the relationship among personnels. The speciﬁc construction method varies from one network to other networks. For instance, an edge between two nodes in the Information Flow Network means the communication links. And the numbers over the edge stand for the types of topics in the message trafﬁc. Afterwards, three networks are drawn in

<!-- b000100 | caption | pages [7] -->
Figure 3 and formula of each is obtained as follow.

<!-- b000101 | prose | pages [7] -->
One of the characteristic of Centrality called Degree Centrality[2] is introduced to depict the impact of friendship. It calculates the number of neighbour nodes linking to node x equals to the concept of degree in graph theory. In the Friendship Network, only neighbour nodes are considered as friends and have effect on each other. Therefore, when an employee complains about the regulations of the organization, the rest of his friends will also feel discontented about it. This phenomenon is called the herd mentality. The formula of friendship inﬂuence index measuring the inﬂuence degree of herd mentality is listed below:

<!-- b000102 | prose | pages [7] -->
1 IF (x) = (2) FS(x)+1

<!-- b000103 | prose | pages [7] -->
(x) represents the degree of node x. where x ∈X; FS

<!-- b000104 | prose | pages [7] -->
The PageRank[4], an algorithm used by Google Search to rank websites in their search en- gine results, is used in the Information Flow Network. The similarity between PageRank and the network is that they are both formed by nodes and edges referring to the interaction effect. And the PageRank is applied to the calculation of weights of nodes satisfying the requirement of representing the inﬂuence degree of message trafﬁc. As for the ofﬁce complex, a employee with bad mood may talk to others inappropriately and thus cause the person he chats with is also in a bad temper. Such phenomenon can be demonstrated by the PageRank algorithm. And the equation of message inﬂuence index is drawn below:

<!-- b000105 | prose | pages [7] -->
IM (x) = tansig  PR(x) (3)

<!-- b000106 | prose | pages [7] -->
where x ∈X; PR(x) is the value of PageRank in node x; tansig is the hyperbolic tangent function.

<!-- b000107 | prose | pages [7] -->
When it comes to the discussion of Leadership Network, the consideration of distance be- tween node i with its superior node is taken. The network is made up by a tree diagram which is similar to the occupation distribution diagram. Hence, the paper deﬁnes the greatest impact on an employee coming from his immediate supervisors is equal to the shortest distance in the diagram. In addition, once a leader in a department is promoted or ﬁred, the employee loyalties and sense of belonging is destroyed. The formula of leader changing inﬂuence index which calculates the distance of the two nodes is shown below:

<!-- b000108 | prose | pages [7] -->
  1 IL(x) = max (4) distance (x, y) y∈LL

<!-- b000109 | prose | pages [7] -->
where x ∈X; LL denotes the set of leaved leaders; distance (x, y) stands for the distance between node x and its immediate superior node y.

<!-- b000110 | furniture | pages [8] -->
Team # 33572

<!-- b000111 | furniture | pages [8] -->
Page 7 of 20

<!-- b000112 | prose | pages [8] -->
The model of Human Capital Network is established through the combination of Depart- ment Network and other three networks. The relation among four networks will be discussed below.

<!-- b000113 | heading | pages [8] -->
5.3 Connections among four networks

<!-- b000114 | prose | pages [8] -->
Due to the fact that a employee’s status is complex and related to the four factors discussed above, the transformation of the four networks into a multiplex network[5] is conducted, lead- ing to the construction of the Human Capital Network. The deﬁnition of the multiplex network is M = (G, C) where G = {GH, GF , GM, GL}; C shows the edges of the same node in different layers. And ﬁve effect indexes of nodes are imported from the four networks in order to de- scribe the speciﬁc dynamic process of organizational churn. The graph of multiplex network and its indexes are drawn as follow.

<!-- b000115 | prose | pages [8] -->
Department Occupation influence dissatisfaction

<!-- b000116 | prose | pages [8] -->
Friendship influence

<!-- b000117 | prose | pages [8] -->
Personnel situation

<!-- b000118 | prose | pages [8] -->
Message influence

<!-- b000119 | prose | pages [8] -->
Leader changing influence

<!-- b000120 | caption | pages [8] -->
Figure 4: The multiplex network is made up by the above four networks describing the same seven-

<!-- b000121 | prose | pages [8] -->
employee division. Besides, node x in each network represents the same staff. Moreover, a new property called occupation dissatisfaction index is introduced adding the list of effect index. The ﬁve effect indexes describe the status of a employee in total.

<!-- b000122 | prose | pages [8] -->
From the Leadership Network, we can see that node 1 is the boss in the division and the rest are under him. And node 7 is a friend of node 4 in the Friendship Network. However it doesn’t mean node 4 only has one friend. It can have connections with others outside the Department Network. Equally, the Information Flow Network is not limited to the seven- employee division network indicating people’s inﬂuence on others within the organization. What’s more, ﬁve indexes are detailed to describe the situation of organizational churn in the following ways.

<!-- b000123 | prose | pages [8, 9] -->
First, the department inﬂuence index stands for the efﬁciency inside the sector which means as the number of employees changes from biggest to smallest. The uncomfortable feelings among workers will breed and cause the situation where the work efﬁciency varies from top to bottom and people want to hunt for another job. Especially, when a leader is turn-over from the organization, it is a disaster for his department’s morale due to the fact that employees are used to taking orders from him rather than anyone else. It would be difﬁcult for the employees to listen to the new leader who may not as good as the former one. This phenomenon is depicted by the leadership inﬂuence index.

<!-- b000124 | furniture | pages [9] -->
Team # 33572

<!-- b000125 | furniture | pages [9] -->
Page 8 of 20

<!-- b000127 | prose | pages [9] -->
When considering the message inﬂuence index, if a colleague complains about the low payment and terrible working environment to an employee, the employee’s unsatisfactory will rise and may push him to quit the position. What’s worse, as for the friendship inﬂuence index, the impact is even stronger and results that both the friends and employee himself resign their positions.

<!-- b000128 | prose | pages [9] -->
In addition, even if a working member is not affected by others, it is possible for him to leave the organization. Because as time ﬂies, an inexperienced employee becomes an experienced one while the desire of promotion has grown. However, if the organization can not satisfy his expectation, the employee’s occupation dissatisfaction index will grow; thus let him quit ofﬁce eventually.

<!-- b000129 | prose | pages [9] -->
Having taken the ﬁve indexes into account, the Human Capital Network model is complete. Applying several events and threshold values to the network, the paper ﬁnally simulates the dynamic process below.

<!-- b000130 | heading | pages [9] -->
6 Description of the dynamic processes on organizational churn

<!-- b000131 | heading | pages [9] -->
6.1 Construction of ability system

<!-- b000132 | prose | pages [9] -->
The properties of nodes in the Human Capital Network must be determined before the simulation of organizational churn. Apart from the ﬁve effect indexes, a few basis factors of an employee are set below.

<!-- b000133 | prose | pages [9] -->
• Level of present position: the location of the staff’s present post in the list of position level;

<!-- b000134 | prose | pages [9] -->
moving to the next level means moving to the higher level of position called promotion.

<!-- b000135 | prose | pages [9] -->
• Ability score: a criterion to evaluate the working ability of a staff and estimate whether he is able to be promoted (move to the next level);

<!-- b000136 | prose | pages [9] -->
• Growth limitation on employee’s ability score: the maximum ability score a staff can obtained in the present position;

<!-- b000137 | prose | pages [9] -->
• Lower limit on next level position’s ability score: the minimum ability score needed to move to the next level.

<!-- b000138 | prose | pages [9] -->
• Type of present position: no matter the staff is a manager or a subordinate;

<!-- b000139 | prose | pages [9] -->
• Location in the Department Network: reﬂecting the department and position where the staff is in the Department Network.

<!-- b000140 | prose | pages [9] -->
• Employee churn rate: the probability for the staff to resign his position.

<!-- b000141 | prose | pages [9] -->
The equation of occupation dissatisfaction index is drawn after the deﬁnition of ability score.

<!-- b000142 | prose | pages [9] -->
( ifAb ≤AbN 0 IP (x) = (5) Ab(x)−AbN (x) else AbG(x)−AbN (x) where x ∈X;Ab(x) is the present ability score of node x; AbN (x) is the lowest limit on the next level position’s ability score;

<!-- b000143 | prose | pages [9, 10] -->
(x) is the growth limitation on employee’s ability score. AbG An ability growth system measuring the dynamic changes in the organization is established with the above properties. The annual growth of ability score is set based on the average annual training cost. Without loss of generality, the average annual salary rate for AC or IE is set to unit 1 in designing the table of position threshold. Besides the given Issue Six indicates that in order to move up into the higher management-level positions, people are currently required to have several years of experience in the organization at speciﬁc levels and types of positions. Therefore, the authors stipulate the promotion interval of each position referring to the enterprise’s regulations and rules. Assume the employee’s ability score increased by the month and the table of threshold in each position is drawn below:

<!-- b000144 | furniture | pages [10] -->
Team # 33572

<!-- b000145 | furniture | pages [10] -->
Page 9 of 20

<!-- b000147 | caption | pages [10] -->
Table 2: Threshold in each position

<!-- b000148 | prose | pages [10] -->
Level of Position Threshold in position Annual growth

<!-- b000149 | prose | pages [10] -->
AC 1 0.05 IE 1 0.3 EE 1.6 0.1 IS 1.8 0.3 ES 2.1 0.2 JM 2.3 0.6 SM 5.3 0.5

<!-- b000150 | prose | pages [10] -->
From Table 2, it takes two years for an IE to be promoted to EE. However, thinking over the special sorting technique using in the Department Network, an EE in the executive layer only need two years to be promoted to the manager part as IS in the division. Unfortunately, it will take him seven years to become a department manager as a JM in the management layer. Such situation is similar to our social experience.

<!-- b000151 | prose | pages [10] -->
In addition, the growth limitation on employee’s ability score in the present position is quantized as a computational formula:

<!-- b000152 | prose | pages [10] -->
AbB(x) = 1.3 · AbN (x)

<!-- b000153 | prose | pages [10] -->
Due to the fact that SM can not be promoted to the higher level and the assumption that AC can not be promoted to other positions, the growth limitation for SM and AC are shown re- spectively.

<!-- b000154 | prose | pages [10] -->
AbB(x) = 1.5 × 5.3 AbB(x) = 1.5 × 1

<!-- b000155 | prose | pages [10] -->
Once a staff’s ability score has risen to the upper limit and he cannot be moved to the higher level, the occupation dissatisfaction causing the rise of employee churn rate will increase .

<!-- b000156 | heading | pages [10] -->
6.2 Description of dynamic process

<!-- b000157 | prose | pages [10] -->
Since the salary is paid monthly and the median time to recruit is depicted by month, the nodes in the Human Capital Network are updated monthly[7].

<!-- b000158 | prose | pages [10, 11] -->
Before the discussion on the ﬁve events, it is necessary to draw a clear distinction between promotion and transfer. Promotion means a employee’s position is risen to the higher level. For example, an IE becoming an EE is called a direct promotion. On the contrary, to some ex- tent, transfer is different from promotion. Transfer stands for the change of node’s location in the Department Network. Hence, an IS who becomes an ES but still listen to the ES’s order Beginning Dimission Promotion Transfer Recruitment Settlement End of of the event event event event event the month month

<!-- b000159 | furniture | pages [11] -->
Team # 33572

<!-- b000160 | furniture | pages [11] -->
Page 10 of 20

<!-- b000162 | caption | pages [11] -->
Figure 5: The update order concludes ﬁve events which are demission event, promotion event, trans-

<!-- b000163 | prose | pages [11] -->
fer event, recruitment event and settlement event. The former four events happen in the beginning of a month and the latter one takes place in the end of the month.

<!-- b000164 | prose | pages [11] -->
in his branch is called promotion without transfer. And if the new ES becomes a manager in his department or other departments, this behaviour is called promotion with transfer. What’s more, the concept of transfer with no promotion depicts the situation where an JM is moved from one department manager location to another department manger location. After under- standing all the concepts, the ﬁve events are discussed below.

<!-- b000165 | prose | pages [11] -->
(1) Demission event:

<!-- b000166 | prose | pages [11] -->
The demission event represents the phenomenon where personnels resign their jobs due to the occupation dissatisfaction and the inﬂuence caused by others. In the given Issue Seven, the current churn rate is 18% per year constantly which is demonstrated by the number of resigned employees in each level. Hence, demission conditions and the demission index are worked out to make a priority list of the probability for a staff to resign in each position. Then, pick up the top of the list to meet the speciﬁed data of churn rate. Some parameters of the demission conditions are deﬁned as follows.

<!-- b000167 | prose | pages [11] -->
• Overall number of personnels: NPS

<!-- b000168 | prose | pages [11] -->
• The number of middle managers including JM, ES and IS: NPM

<!-- b000169 | prose | pages [11] -->
• Overall churn rate of the company: PC = 18%

<!-- b000170 | prose | pages [11] -->
2NPS·NPM·PC

<!-- b000171 | prose | pages [11] -->
• Churn rate of middle managers: PM = (NPS+NPM)·NPM

<!-- b000172 | prose | pages [11] -->
• Churn rate of other positions: PO = PM 2

<!-- b000173 | prose | pages [11] -->
 

<!-- b000174 | prose | pages [11] -->
• The number of resigned personnels per month: PL(p) = RP NP (p)·P (p) 12 where RP is a random function following Poissonian distribution; P (p) denotes the churn rate of each position which is equal to PM when p is a middle manager or PO when p is other positions.

<!-- b000175 | prose | pages [11] -->
The number of resigned personnels per month is calculated by the demission index. The demission index is an equation consisting of ﬁve effect indexes introduced before. And the An- alytic Hierarchy Process (AHP), a structured technique for organizing and analyzing complex decisions based on mathematics and psychology[3], is used to determine the weights of each effect index. The importance of the ﬁve indexes has been evaluated and the result shows that occupation dissatisfaction index is the most important one and friendship inﬂuence index take the second place. Department inﬂuence index weights the same to leader changing inﬂuence index. And leadership inﬂuence index is the least one. A priority list based on the employee’s churn rate is made after calculation.

<!-- b000176 | prose | pages [11, 12] -->
Applying AHP to the numeration of weights for each index, the results are WO = 0.5992, WH = 0.0795, WF = 0.1926, WM = 0.0492 and WL = 0.0795. Therefore, the equation of demission index is listed below ID = W · I (6) where I denotes the vector of indexes and W represents the vector of weights. According to Equation (1) (2) (3) (4) (5)

<!-- b000177 | furniture | pages [12] -->
Team # 33572

<!-- b000178 | furniture | pages [12] -->
Page 11 of 20

<!-- b000180 | prose | pages [12] -->
  WO WH WF WM WL W = ′  I = IO IH IF IM IL

<!-- b000181 | prose | pages [12] -->
Finally, the equation of demission index is listed below.

<!-- b000182 | prose | pages [12] -->
ID = 0.5992 × IO + 0.0795 × IH + 0.1926 × IF + 0.0492 × IM + 0.0795 × IL

<!-- b000183 | prose | pages [12] -->
Therefore, the algorithm of demission event can be divided into two steps.

<!-- b000184 | prose | pages [12] -->
• Step One: compute the churn rate of position in each level on the basis of overall churn rate of the organization;

<!-- b000185 | prose | pages [12] -->
• Step Two: compute the demission index of each employee and make a priority list based on the possibilities of quitting the job. Then pick up the top of the list to meet the speciﬁed data of churn rate in each position.

<!-- b000186 | prose | pages [12] -->
(2) Promotion event:

<!-- b000187 | prose | pages [12] -->
As time goes by, a employee’s ability score will increase and touch the lowest limit on the next level. Under such circumstance, two promotion methods are designed to reﬂect the real situations. The situations are converted into the following algorithm.

<!-- b000188 | prose | pages [12] -->
• Step One: update all working members’ ability scores;

<!-- b000189 | prose | pages [12] -->
• Step Two: if an employee’s ability score meets the lowest limit on the higher position and there are job vacancies in the same location of the Department Network, then the person is promoted to the next level (promotion without transfer);

<!-- b000190 | prose | pages [12] -->
• Step Three: Two: else if a employee’s ability score meets the lowest limit on the higher position and there are job vacancies in the superior location of the Department Network, then the person is promoted to the next level (promotion with transfer)

<!-- b000191 | prose | pages [12] -->
• Step Four: else if none of the above conditions is satisﬁed, the promotion is delayed.

<!-- b000192 | prose | pages [12] -->
(3) Transfer event:

<!-- b000193 | prose | pages [12] -->
The transfer event is triggered when someone is leaving from the organization. The occu- pation vacancy is needed to be ﬁlled so that the organization can maintain in good condition. The transfer for an EE, IE or AC is not considered in order to save labour. Equally the situations for managers’ transfer are divided into several steps.

<!-- b000194 | prose | pages [12] -->
• Step One: if someone inside the department is able to be promoted and cover the vacancy, then the transfer is conducted with promotion;

<!-- b000195 | prose | pages [12] -->
• Step Two: else if someone in the subordinate department satisfy the managerial level of position required in the department, then the transfer is conducted without promotion;

<!-- b000196 | prose | pages [12] -->
• Step Three: else if someone in the subordinate department meets the lowest limit on the managerial position, then the promotion and transfer are conducted.

<!-- b000197 | prose | pages [12] -->
• Step Four: else if the subordinate in the CEO ofﬁce meets the demand of manager’s level of position, then the transfer is conducted without promotion;

<!-- b000198 | furniture | pages [13] -->
Team # 33572

<!-- b000199 | furniture | pages [13] -->
Page 12 of 20

<!-- b000200 | prose | pages [13] -->
• Step Five: Search for the substitution manager among the brother departments;

<!-- b000201 | prose | pages [13] -->
– Substep One: if someone inside the brother departments is able to promote and cover the vacancy, then the transfer is conducted with promotion;

<!-- b000202 | prose | pages [13] -->
– Substep Two: else if someone in the subordinate sectors of the brother departments satisfy the managerial level of position required in the department, then the transfer is conducted without promotion;

<!-- b000203 | prose | pages [13] -->
– Substep Three: else if someone in the subordinate sectors of the brother departments meets the lowest limit on the managerial position, then promotion and transfer are conducted.

<!-- b000204 | prose | pages [13] -->
• Step Six: the position remains empty and waits for the recruitment.

<!-- b000205 | prose | pages [13] -->
(4) Recruitment event:

<!-- b000206 | prose | pages [13] -->
Once the suitable personnels cannot be found inside the organization to make up for the gap, it is time to recruit new employees from the outside world. The paper deﬁne the present month as NM and the medium time to recruit for the position P as M(P).What’s more JV (P) represents the number of the rest of the job vacancies.The algorithm is listed below.

<!-- b000207 | prose | pages [13] -->
• Step One: if NM mod M(P) = 0, conduct the recruitment and put the hired people into the list to be assigned, refreshing the multiplex network; this step indicates the minimum JV (p)·2/3    JV (p), RP recruiting numbers which is computed by the formula min and M(p)/12 the personnels hired meet the lowest limit on the recruiting department.

<!-- b000208 | prose | pages [13] -->
• Step Two: calculate the cost of recruitment according to the distribution list;

<!-- b000209 | prose | pages [13] -->
• Step Three: refer to the priority list of positions which is SM, JM, AC, ES, IS, EE and IE respectively, and allocate the hired personnels to the vacant departments until the distribution list is empty; the distribution order is from top to bottom and from left to right; and each department adopts one position at a time.

<!-- b000210 | prose | pages [13] -->
– Substep One: if the hired person in the list is suitable for a vacant position, put the person in the Department Network and delete its data in the list;

<!-- b000211 | prose | pages [13] -->
– Substep Two: else if there is no appropriate job vacancy, according to the distribution method, compare the present to-be-assigned employee to the personnels within the depart- ment in order; if the former one is prior to a certain person inside, swap the to-be-assigned employee with the old one then put the old one to the distribution list and delete the data of assigned employee; if not, change to the next department.

<!-- b000212 | prose | pages [13] -->
(5) Settlement event:

<!-- b000213 | prose | pages [13] -->
After the employee changes within a month, the settlement event happens at the end of the month to compute the expense in each category like continuing education, recruitment and so on. The evaluation of the settlement reﬂects the economic beneﬁt of the organization.

<!-- b000214 | heading | pages [13] -->
7 Task Two: Results and analysis on dynamic process

<!-- b000215 | heading | pages [13] -->
7.1 Analysis on the organizational churn

<!-- b000216 | prose | pages [13] -->
A comprehensive broken line graph is drawn to identify and analyze the dynamic processes of organizational churn.

<!-- b000217 | furniture | pages [14] -->
Team # 33572

<!-- b000218 | furniture | pages [14] -->
Page 13 of 20

<!-- b000219 | caption | pages [14] -->
Figure 6: Where the number of recruits, resignation and total personnels per month provides a full

<!-- b000220 | prose | pages [14] -->
picture of the dynamic processes involved in organizational churn under the circumstance of 18% churn rate. And the crests and troughs indicate the busy seasons and slack seasons of recruitment in a decade.

<!-- b000221 | prose | pages [14] -->
From Figure 6, a downtrend on the total number of employees is observed in the ﬁrst two years. Then with a gradual increase, the amount of staffs varies from 285 to 295 leading to a steady state. Besides, the per month amount of employees depends on the recruitments and the churn rate in each month. Due to the hiring cycle, the number of recruits varies from time to time. And the churn rate remains stable so that the number of employees will rise during the furious recruiting time and it will drop when few job fairs is held. The above mentioned are called hiring busy seasons and slack seasons respectively which cause the crests and troughs in the graph. For example, it is easier to ﬁnd that lost of people are hired in March, June, September and December thus the sum of the employees is increased. The reason to explain the phenomenon is the great amounts of EE and IE are hired during that period. What is more noticeable is that the sum of employees always rises to the peak in December in every year. This is related to the situation where most of the positions except for SM and ES are opening at that time.

<!-- b000222 | prose | pages [14] -->
Further digging focuses on proving the accuracy of the multiplex network. The comparison between the true value and ideal value is conducted during the steady stage in the later period.

<!-- b000223 | prose | pages [14] -->
First, some parameters are deﬁned. Let NS denotes the sum of employees in the steady state. And PC stands for the present churn rate. So the expectation of personnels leaving from the organization is NS×PC. Similarly, the expectation of personnels newly hired is (370 −NS)× 2/3. When the two expectations come to the balanced state, the equation is worked out below.

<!-- b000224 | prose | pages [14] -->
NS × PC = (370 −NS) × 2 3 NS = 370 × 2/3 (7) PC + 2/3

<!-- b000225 | prose | pages [14, 15] -->
As for the current case, PC = 18% and thus the ideal value for the amount of working members is 291 within the true value interval during the stable stage. This fact indicates the reliability and accuracy of our model.

<!-- b000226 | furniture | pages [15] -->
Team # 33572

<!-- b000227 | furniture | pages [15] -->
Page 14 of 20

<!-- b000229 | prose | pages [15] -->
What’s more, as the staff comes and goes, the structure of the multiplex network has been changed. The new nodes are put into the networks while the long gone nodes are deleted. Thus, the connections between nodes become changeable. As time goes by, the total number of clerk resigning their positions is increased, causing great damage to the Friendship Network. What’s worse, the dissatisfaction for not being promoted has pass on through the Information Flow Network resulting in the growth of bad atmosphere in the organization. So once a leader is moved to another department or quit his job, the demission index rises to the threshold and the demission event is triggered. After a gradual decline of the demission index, a dynamic balance is gained between the number of recruitment and the amount of resign. Therefore, the sum of personnels remains stable and the factors of the networks are dynamically balanced. Meanwhile, the structure of the multiplex network also becomes stable which means the allo- cation of each layer in the organization is steady.

<!-- b000230 | heading | pages [15] -->
7.2 Effects on organization’s productivity

<!-- b000231 | prose | pages [15] -->
Some deﬁnitions measuring the productive forces is needed before analyzing the dynamic process’s effect on organization’s productivity.

<!-- b000232 | prose | pages [15] -->
Staff Organization Ability Sum productivity productivity

<!-- b000233 | caption | pages [15] -->
Figure 7: Where the employee ability score evolves to the employee productivity on the basis of minor

<!-- b000234 | prose | pages [15] -->
effects. And the organization’s productivity is the summation of each employee productivity within the network.

<!-- b000235 | prose | pages [15] -->
The ﬁrst one is employee productive power which is mainly inﬂuenced by the ability score of clerk himself. Other minor inﬂuence factors are the ﬁve effect indexes talked above like the occupation dissatisfaction index, department inﬂuence index and so on. Hence, the equation of employee productivity is obtained as follow according to Equation (6).

<!-- b000236 | prose | pages [15] -->
Pro(x) = Ab(x) −weak · Ab(x)

<!-- b000237 | prose | pages [15] -->
weak = ID×0.5 = (0.5992 × IO + 0.0795 × IH + 0.1926 × IF + 0.0492 × IM + 0.0795 × IL)×0.5 where Pro(x) is the employee productive power; Ab(x) characterizes the employee’s ability score; weak represents the minor effect factors.

<!-- b000238 | prose | pages [15] -->
Taking the concepts of personnels above as reference, the ability score and productivity of the organization are deﬁned below.

<!-- b000239 | prose | pages [15, 16] -->
X Ab(x) AbO = x∈M X Pro(x) ProO = x∈M where AbO stands for the ability score of the organization; ProO denotes the productivity of the organization; M is the set of the working members.

<!-- b000240 | furniture | pages [16] -->
Team # 33572

<!-- b000241 | furniture | pages [16] -->
Page 15 of 20

<!-- b000243 | prose | pages [16] -->
The deﬁnition procedure can also be demonstrated by Figure 7.

<!-- b000244 | prose | pages [16] -->
From Figure 7 and the above-mentioned analysis, it is wise for us to regard the ability score of employees as the most powerful and favourable factor when determining the productivity of the organization. Other indirect acting factors working as adverse factors are occupation dis- satisfaction index, department inﬂuence index, friendship inﬂuence index, message inﬂuence index and leader changing inﬂuence index. The good effect brought by the employee’s ability score offsets part of the bad impact of the negative factors.

<!-- b000245 | prose | pages [16] -->
Moreover, a broken line graph describing the ten-year dynamic processes of organization’s productivity based on the 18% churn rate is drawn in Figure 8.

<!-- b000246 | caption | pages [16] -->
Figure 8: The ability score and productivity of organization are in the left vertical axis; The average

<!-- b000247 | prose | pages [16] -->
demission index is in the right vertical axis.

<!-- b000248 | caption | pages [16] -->
Figure 8 shows that the productivity rises with the ability score at ﬁrst. Then it keeps con-

<!-- b000249 | prose | pages [16] -->
stant within the interval from 600 to 700. And the demission index maintains its increase until it enters into the steady stage. Such phenomenon is accordant to the analysis of the organiza- tional churn.

<!-- b000250 | prose | pages [16] -->
The dynamic processes’ direct and indirect effects on the organization’s productivity are analyzed below:

<!-- b000251 | prose | pages [16] -->
• Direct effects:

<!-- b000252 | prose | pages [16] -->
From Figure 8, the productivity of the organization is directly inﬂuenced by the clerk’s ability score. In the early stage of the personnels, even though the number of employees is decreased, the ability score of the organization is increased. Because of the fact that the staff in the early stage has much promotion space so that the ability score of the or- ganization rises with the one of the employee, leading to the rising of the organization’s productivity. Finally, the number of employees is tending towards stability and the ability of employee is saturated over time. Thus the organization’s productivity keeps stable.

<!-- b000253 | furniture | pages [17] -->
Team # 33572

<!-- b000254 | furniture | pages [17] -->
Page 16 of 20

<!-- b000255 | prose | pages [17] -->
• Indirect effects:

<!-- b000256 | prose | pages [17] -->
The minor factor consisting of ﬁve effected indexes is similar to the demission index. Be- cause they all put negative impact on the productivity. From Figure 8 we can see that the difference value between ability and productivity becomes larger as the rising of de- mission index. However, when the demission index is unchanged, so does the difference value. And the description about the change of demission index has been discussed in the multiplex network section.

<!-- b000257 | heading | pages [17] -->
8 Task Three: prediction of the organization’s budget

<!-- b000258 | prose | pages [17] -->
Task Three requires the prediction of the organization‘s budget requirements for human resource management in terms of σ for both recruiting and training over the next 2 years. Besides the churn rate of the organization is still 18% per year.

<!-- b000259 | caption | pages [17] -->
Figure 9: The multiple graph consists of three simulation results in two years and shows the relationship

<!-- b000260 | prose | pages [17] -->
between cost for recruiting and the number of opening positions. Accumulative bar diagram stands for the cost for holding job fairs and hiring personnels monthly and broken line graph represents the number of job vacancies by the month.

<!-- b000261 | caption | pages [17] -->
Figure 9 gives three distinct simulation results which can be explained by the fact that both

<!-- b000262 | prose | pages [17] -->
the demission event and the recruitment event obey Poisson distribution. So the random varia- tion of these events is equal to the reality that the actual amount of recruitment depends on the quality of applicants rather than the expected quantity. What is noteworthy is that December is still the hiring peak in a year which is identical to the conclusion in Task Two.

<!-- b000263 | prose | pages [17] -->
In the mean time, the cost for hiring middle layer managers makes up a high proportion of the total cost. This situation can be demonstrated by the given Issue Four. And these mid-level positions suffer churn rate as twice the average rate of the rest of the company so that they are need ﬁlling all the time. Besides, the cost for hiring a middle layer manager is more expensive than other positions.

<!-- b000264 | prose | pages [17] -->
When it comes to the discussion about the reason why ES is not hired at a frenetic pace, the paper ﬁgures out that on the basis of a large amount of IS is recruited, the one-year promotion interval between IS and ES makes it possible for IS to fulﬁl the vacancy left by ES. Therefore, there is no need to hire extra ES from the outside.

<!-- b000265 | prose | pages [17] -->
From Figure 10, the total training cost to each position’s training cost ratio is very similar in the three simulations. And the total training cost remains invariant. The reasons for the phenomenon are the following two ways.

<!-- b000266 | furniture | pages [18] -->
Team # 33572

<!-- b000267 | furniture | pages [18] -->
Page 17 of 20

<!-- b000268 | caption | pages [18] -->
Figure 10: The accumulative bar diagram consists of three simulation results in two years and shows

<!-- b000269 | prose | pages [18] -->
the dynamic changes of the training cost with the 18% churn rate.

<!-- b000270 | prose | pages [18] -->
On the one hand, one of the conclusions drawn in the Task Two shows that the organization network is stable and the types of positions keeps unchanged in the two years. Therefore, the ratios among the simulations is quite close. On the other hand, there is no sign of randomness when compared with Figure 9 which is to say the stability of the company structure prevents the training cost from changing randomly.

<!-- b000271 | caption | pages [18] -->
Table 3: Organization’s budget

<!-- b000272 | prose | pages [18] -->
Using the Human Capital Network to simulate the cost of the company in terms of re- cruiting, salary, training and in total. And thus the prediction of the company’s budget in the following two years is made. As for the above three aspects, the total budget varies within a small interval. This result corresponds to the reality that the senior managers always want to keep the prosperity of their company.

<!-- b000273 | heading | pages [18] -->
9 Task Four: sensitivity analysis

<!-- b000274 | prose | pages [18] -->
Task Four requires to conduct a sensitivity analysis on the Human Capital Network by changing the annual churn rate for all positions. Estimating whether ICM can sustain its 80% full status for positions after the adjustment, the determination of the costs and indirect effects of these higher turnover rates is proceed.

<!-- b000275 | prose | pages [18, 19] -->
Three broken lines whose churn rates are 18%, 25% and 35% respectively are drawn below. Besides, after using the equation of employee’s steady-state value[Equation (7)] to calculate the ideal value of the amount of employees, the results are worked out as 291, 269 and 242 separately. However, the expected number of staffs is 296 which varies widely from the ideal value. Thus, ICM cannot sustain its 80% full status for positions after changing the turnover rate theoretically.

<!-- b000276 | furniture | pages [19] -->
Team # 33572

<!-- b000277 | furniture | pages [19] -->
Page 18 of 20

<!-- b000279 | prose | pages [19] -->
Change PC to satisfy the task and add the original curve to the graph, the dynamic process in the number of personnels with three different churn rates is drawn in Figure 11.

<!-- b000280 | prose | pages [19] -->
Dynamic processes in the number of personnels in a decade 310 Churn rate:18% Churn rate:25% 300 Churn rate:35%

<!-- b000281 | prose | pages [19] -->
290

<!-- b000282 | prose | pages [19] -->
Number of staff 280

<!-- b000283 | prose | pages [19] -->
270

<!-- b000284 | prose | pages [19] -->
260

<!-- b000285 | prose | pages [19] -->
250

<!-- b000286 | prose | pages [19] -->
240

<!-- b000287 | prose | pages [19] -->
230 0 20 40 60 80 100 120 Month

<!-- b000288 | caption | pages [19] -->
Figure 11: The number of personnels with three different churn rates in a decade.

<!-- b000289 | caption | pages [19] -->
Figure 11 implies that the higher the staff turnover is, the lower the steady-state value with

<!-- b000290 | prose | pages [19] -->
respect to the total number of employees. Besides, the curves drop much in the ﬁrst 36 months. All these three curves approach to the steady-state value at the end of the third year. And the steady areas are nearby the theoretical steady value corresponding to the churn rate. Hence the simulation results and the theoretical ones are consistent: the ICM company cannot sustain its 80% full status for positions.

<!-- b000291 | caption | pages [19] -->
Table 4: Several parameters in different churn rate

<!-- b000292 | caption | pages [19] -->
Table 4 indicates that the high turnover rate causes great damage to the health of human

<!-- b000293 | prose | pages [19] -->
resource. The cost for recruitment rises with the churn rate while salary and training fees drop much, causing the reduction of the total budget. As the turnover rate goes up, much more money is allocated to the recruitment, causing the rise of the recruitment costs. However, the more staffs leave the company the lower the cost is for training and salary. What’s worse, even if the total budget is decreased which saves money for the company, the number of job vacancies still increases and most of the departments are short of manpower. The disorder in the Department Network is harmful to the organization’s productivity eventually.

<!-- b000294 | prose | pages [19, 20] -->
The indirect effects of high turnover rate are mainly concentrated on the Human Capital Network and they are reﬂected by the ﬁve effect indexes. As for IO, the job vacancies in the Department Network make it easier for an employee to get promotion. And the lack of em- ployees raises the value of IH. As the number of people quitting jobs goes up, the number of friends people have is decreased; thus cause the rise of IF . When considering IL, the central- ization allows personnels connect with others much close. Thus the index of leadership drops. In addition, the index of demission ID relies on IO partly so that ID decreases with IO.

<!-- b000295 | furniture | pages [20] -->
Team # 33572

<!-- b000296 | furniture | pages [20] -->
Page 19 of 20

<!-- b000298 | heading | pages [20] -->
10 Task Five: analysis on speciﬁc conditions

<!-- b000299 | prose | pages [20] -->
Task Five simulates a situation where the churn rates are 30% in both junior managers and experienced supervisors. Besides, external recruiting is forbidden and only qualiﬁed employ- ees can be promoted inside the network for the next two years. Other churn values remain at 18%. In addition, an explanation on the impact of the speciﬁc situation on the HR health of the organization is asked.

<!-- b000300 | caption | pages [20] -->
Figure 12: The statistical chart reﬂects each amount of resigning, promoting, transferring, job vacancies

<!-- b000301 | prose | pages [20] -->
and total employees. The total number of employees is in the right vertical axis. The rest of properties are in the left vertical axis.

<!-- b000302 | caption | pages [20] -->
Figure 12 implies that the number of employees decreases little by little to 200 at the end of

<!-- b000303 | prose | pages [20] -->
the next year. In the mean time, the problem of lacking leaders becomes more serious. Even though some of the vacancies are ﬁlled by promotion and transfer, the gap is bigger and reach 9 at the end of the following year. It is due to the fact that it will take a long time before a general staff becomes a manager and the two-year time is too short.

<!-- b000304 | caption | pages [20] -->
Table 5: The number of personnels with three different churn rates in a decad

<!-- b000305 | prose | pages [20, 21] -->
Similarly with the situation in the Task Four, Table 5 discusses about the performance of ﬁve effect indexes especially in the last month of the following two years. Because there are nine leader vacancies in the last month, IL is small. It means the value of IO is also small. Since the message inﬂuence index is calculated by the PageRank algorithm, IM is much more stable and thus the Information Flow Network is steady. Based on the analysis of ﬁve indexes in different subnet, a employee’s situation can be described comprehensively.

<!-- b000306 | furniture | pages [21] -->
Team # 33572

<!-- b000307 | furniture | pages [21] -->
Page 20 of 20

<!-- b000309 | heading | pages [21] -->
11 Strengths and Weaknesses

<!-- b000310 | prose | pages [21] -->
Strengths:

<!-- b000311 | prose | pages [21] -->
• The multiplex network model is more comprehensive and effective to chracterize the Human Capital Network than single-layer Department Network in describing and esti- mating the demission index which is effected by a variety of factors.

<!-- b000312 | prose | pages [21] -->
• The dynamic process is divided into ﬁve events covering common scenarios like promo- tion, transfer and so on, which not only simplify the model and enhance the intelligibility, but also make model more robust in maintaining high occupancy of positions even if un- der the worst condition such as no recruitment event.

<!-- b000313 | prose | pages [21] -->
• The results of the simulations according to the multiplex network model are more reliable and practical than those of derivations simply based on empirical value.

<!-- b000314 | prose | pages [21] -->
Weaknesses:

<!-- b000315 | prose | pages [21] -->
• In multiplex network model, the edges connected between nodes in the same layer are randomly generated except for the Department Network,which do not necessarily con- form to reality.

<!-- b000316 | prose | pages [21] -->
• Subjective factors of employees are not taken into account in the conﬁguration of Table 4 which are uncontrollable, such as family factor.

<!-- b000317 | heading | pages [21] -->
References

<!-- b000318 | references | pages [21] -->
[1] D. Stokols, K.L. Hall, B.K. Taylor, R.P. Moser (2008). The Science of Team Science:

<!-- b000319 | references | pages [21] -->
Overview of the Field and Introduction to the Supplement, Am J Prev Med 2008;35(2S):

<!-- b000320 | references | pages [21] -->
S77-S89.

<!-- b000321 | references | pages [21] -->
[2] Wasserman, S. & Faust, K. (1994) Social Network Analysis: Methods and Applications.

<!-- b000322 | references | pages [21] -->
Cambridge: Cambridge University Press.

<!-- b000323 | references | pages [21] -->
[3] AHP. http://en.wikipedia.org/wiki/Analytic_hierarchy_process 02/08/2015

<!-- b000324 | references | pages [21] -->
[4] PageRank. http://en.wikipedia.org/wiki/PageRank 02/08/2015

<!-- b000325 | references | pages [21] -->
[5] Mikko KivelÃd’, Alexandre Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno,

<!-- b000326 | references | pages [21] -->
Mason A. Porter. (2013). Multilayer Networks, J. Complex Networks, 2(3):203-271 (2014);

<!-- b000327 | references | pages [21] -->
arXiv preprint arXiv:1309.7233, 2013.

<!-- b000328 | references | pages [21] -->
[6] E. Salas, N.J. Cooke, and M.A. Rosen. (2008). On Teams, Teamwork, and Team Perfor-

<!-- b000329 | references | pages [21] -->
mance: Discoveries and Developments. Human Factors: The Journal of the Human Fac-

<!-- b000330 | references | pages [21] -->
tors and Ergonomics Society June 2008 vol. 50 no. 3 540-547.

<!-- b000331 | references | pages [21] -->
[7] Hopcroft, John E. Introduction to automata theory, languages, and computation. Pearson

<!-- b000332 | references | pages [21] -->
Education India, 1979.
