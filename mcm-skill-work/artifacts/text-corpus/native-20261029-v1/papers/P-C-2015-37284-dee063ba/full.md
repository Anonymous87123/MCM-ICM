# P-C-2015-37284-dee063ba

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | prose | pages [1] -->
For office use only

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
37284

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T2 ________________

<!-- b000008 | prose | pages [1] -->
F1 ________________

<!-- b000009 | prose | pages [1] -->
F2 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________

<!-- b000012 | prose | pages [1] -->
F3 ________________

<!-- b000013 | title | pages [1] -->
C

<!-- b000014 | prose | pages [1] -->
T4 ________________

<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | prose | pages [1] -->
F4 ________________

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
Human Capital Management in Organizations

<!-- b000020 | prose | pages [1] -->
Information Cooperative Manufacturing(ICM) is an organization of 370 people, who is facing the

<!-- b000021 | prose | pages [1] -->
challenging issue related to effectively managing its human capital. In this paper, we establish models to

<!-- b000022 | prose | pages [1] -->
help figuring out the problem.

<!-- b000023 | prose | pages [1] -->
Firstly, we build a static human capital network. To begin with, there are three kinds of relationships:

<!-- b000024 | prose | pages [1] -->
the relationship among people, the relationship among positions, the relationship between people and

<!-- b000025 | prose | pages [1] -->
positions. Then we use a bipartite graph to indicate the assignment of positions. After matching people

<!-- b000026 | prose | pages [1] -->
and position, it forms a static human capital network. In addition, we define loyalty and intimacy to

<!-- b000027 | prose | pages [1] -->
measure the probability of churn. These two indices consider two situations: people churn by their own

<!-- b000028 | prose | pages [1] -->
reason and people churn by others’ influence.

<!-- b000029 | prose | pages [1] -->
Secondly, we take time into consideration and get a dynamic network. We first analyze the change

<!-- b000030 | prose | pages [1] -->
of loyalty and intimacy. Loyalty is influenced by the relation of the time that people works in the same

<!-- b000031 | prose | pages [1] -->
position and the mean time of promotion. In addition, it will increase if the employees get promoted.

<!-- b000032 | prose | pages [1] -->
Intimacy is influenced by two employees’ disparity of position levels. Next, we simulate the churn in the

<!-- b000033 | prose | pages [1] -->
dynamic process. After that, we describe the cost, which consists of the direct cost and indirect cost.

<!-- b000034 | prose | pages [1] -->
More specifically, they are related to the number of working people and the organizational structure.

<!-- b000035 | prose | pages [1] -->
Besides, we using genetic algorithm to get the optimal assignment——minimizing the cost.

<!-- b000036 | prose | pages [1] -->
In general, the dynamic process can be divided to three circulatory parts. The first one is to use

<!-- b000037 | prose | pages [1] -->
computer simulation to simulate the churn and recruitment of employees. The second part is the change

<!-- b000038 | prose | pages [1] -->
of loyalty and intimacy which is determined by the change of network. And the third one is to use the

<!-- b000039 | prose | pages [1] -->
Genetic Algorithm to get the optimal assignment to minimize the cost and this is the only part that HR

<!-- b000040 | prose | pages [1] -->
manager can intervene.

<!-- b000041 | prose | pages [1] -->
Thirdly, we apply the model to solve three questions, which are corresponding to Task (3)(4)(5). For

<!-- b000042 | prose | pages [1] -->
(3), the cost of recruitment is 38.2 and the cost of training is 127.08 over the next two years. For (4),

<!-- b000043 | prose | pages [1] -->
if the churn rate is 25%, the organization can sustain 80% full status. The recruitment is 22% and the total

<!-- b000044 | prose | pages [1] -->
cost is 617.64. If the churn rate is 35%, the organization can sustain 80% full status. The recruitment is

<!-- b000045 | prose | pages [1] -->
31% and the total cost is 533.66. A higher churn rate will decrease the direct cost but it will cause

<!-- b000046 | prose | pages [1] -->
unsteadiness of the organizational structure, which is the indirect effect. For (5), a higher churn rate in

<!-- b000047 | prose | pages [1] -->
middle levels (junior manager and experienced supervisor) will provide more chance for people to

<!-- b000048 | prose | pages [1] -->
promote. As a result, it can refresh the organizational structure and improve people’s cohesion to the

<!-- b000049 | prose | pages [1] -->
organization.

<!-- b000050 | prose | pages [1] -->
Fourth, we analyze the parameters in our paper. We identify the parameters determined by data or

<!-- b000051 | prose | pages [1] -->
experience and the parameters determined by experiments. After analyzing, we let the number of

<!-- b000052 | prose | pages [1] -->
population, the iteration times, the mutation rate and the crossover rate to 200, 2000, 0.4 and 0.1

<!-- b000053 | prose | pages [1] -->
respectively, which are suitable parameters in the Genetic Algorithm.

<!-- b000054 | prose | pages [1] -->
Finally, we introduce the concept of team science and focus on the information flow. We add the

<!-- b000055 | prose | pages [1] -->
information network to our human capital network and it comes into being a multi-layers network, which

<!-- b000056 | prose | pages [1] -->
can make our analysis more comprehensive and reasonable.

<!-- b000057 | furniture | pages [2] -->
Team #37284                                                                Page 1 of 20

<!-- b000058 | heading | pages [2] -->
1. Introduction

<!-- b000059 | prose | pages [2] -->
As we all know, an organization filled with good, talented, well-trained people is more prone to success. Actually, people often leave for other jobs or retire and then may be replaced, which forms a fluid network of human capital. Information Cooperative Manufacturing(ICM), an organization of 370 people, who are facing the challenging issue related to effectively managing its human capital. And now, we write this paper to help them figure out this problem.

<!-- b000060 | prose | pages [2] -->
In this paper, we first build three networks independently: the network among people, the network among position and the bipartite graph between people and positions. Next we put them together and get a human capital network. Then considering the time, we build a dynamic human capital network to indicate the dynamic process of human capital. In the meantime, we use the Genetic Algorithm to get the optimal matching and then manage the human capital. After that, we apply our model to answer the Task (3), (4), (5). Finally, we discuss the team science and multi-layers network in HR management.

<!-- b000061 | prose | pages [2] -->
In section 3, considering the relation among people without the influence of positions, we first build a network among people and define two indices: loyalty and intimacy. Loyalty is an index to indicate the probability of staying in the organization. Its initial value is determined by organization culture and staff’s own expectations. Intimacy represents the following probability with connected people who have churned. Its initial value is determined by the time of know and the similarity of interest of two individuals. Next we build a position network to indicate the relationship among the positions. Then, we build a bipartite graph to measure the matching of people and positions. Finally, putting three graphs together and we get a human capital network.

<!-- b000062 | prose | pages [2] -->
In section 4, we take time into account and get a dynamic human capital network. Then we analyze the change of loyalty and intimacy with the dynamic process. After that, we describe the process of churn and how the network changes. Finally, under the principle of minimizing the cost, we use Genetic Algorithm to assign people to the positions.

<!-- b000063 | prose | pages [2] -->
In section 5, we apply the model to solve three Tasks. The first one is to calculate the budget requirements for both recruiting and training over the next two years. The second one is to analyze the influence of changing annual churn rate. The third one is to discuss the impact on the HR health of the organization under the situation that the churn rate of middle levels is higher than that of lower levels.

<!-- b000064 | prose | pages [2] -->
In section 6, we analyze the parameters in our paper. There are two kinds of parameter: one is determined by data and another is determined by experiments. We describe how to choose the better parameters.

<!-- b000065 | prose | pages [2] -->
In section 7, we introduce the concept of team science and focus on the information flow. We add the information network to our human capital network and it comes into being a multi-layers network, which can make our analysis more comprehensive and reasonable.

<!-- b000066 | heading | pages [2] -->
2. Assumptions and Justification

<!-- b000067 | prose | pages [2] -->
(1) The longer time an individual works, the more experienced they are. We assume that the years that people work in ICM is proportional to their knowledge and abilities. It is hard for us to measure the people’s knowledge and abilities, so we use the work years in the company to measure their abilities. Since people must have several years of experience before they move up into the higher management-level, it is suitable for us to consider working time.

<!-- b000068 | prose | pages [2] -->
(2) No employee is fired. In the operation of ICM, marginal and poor employees are allowed to stay because ICM always worries about being shorted-handed.

<!-- b000069 | prose | pages [2] -->
(3) The time unit in this paper is one month. The human capital network is dynamic and companies often take one month as time unit. For example, an employee who hands his notice on February 10th and it will become effective in March 1st.

<!-- b000070 | prose | pages [2] -->
(4) The influence of churn will work in the next month. If a person churned in this month, we assume the person who connected to him or her dos not know before. Therefore, they cannot churn together and he or she may be influenced in the next month.

<!-- b000071 | prose | pages [2] -->
(5)ICM will have the maximum output when 85% of its 370 positions filled. Actually, many

<!-- b000072 | furniture | pages [2] -->


<!-- b000073 | furniture | pages [3] -->
Team #37284                                                                Page 2 of 20

<!-- b000074 | prose | pages [3] -->
companies do not have 100% of its positions filled. On the one hand, an organization should have some vacant higher position to motivate employees to work harder. On the other hand, some vacant position can avoid repeating work and overstaffing. Usually, ICM has 85% of its 370 position filled at any time. So it is suitable for us to assume that the organization have the maximum output under this situation.

<!-- b000075 | prose | pages [3] -->
(6) We make a Hypothesis of Economic Man. That is to say, we assume that all the people want to pursue a high position just because of the higher salary. So we divide the positions into six levels according to the salary. In this paper, we have no clues about people’s ambitions, expectations, abilities, knowledge, so we only use salary to measure their willing. Also, it is hard to say the belonging relationship between departments. Hence, we use the salary levels to define the level of position.

<!-- b000076 | prose | pages [3] -->
(7) The organization need to pay the recruitment cost for a new person but need not to pay the training cost for him in the beginning. And the organization should pay the training cost for the qualified staff every year. We assume that the people in the organization should be trained every year to improve their abilities and neglect the training cost of new people because we think the recruitment cost contains that cost in the beginning.

<!-- b000077 | heading | pages [3] -->
3. The human capital network

<!-- b000078 | prose | pages [3] -->
Actually, a human capital network contains many factors, such as people, position, the matching between people and position, the relationship among people, the relationship among position, factors influencing their relationship and so on.

<!-- b000079 | prose | pages [3] -->
In this part, we first discuss the network among people and positions respectively and the matching relationship between people and positions. Then we synthetize three independent part and form an integrated static human capital network. Finally, we introduce the concept of time stamp to build a dynamic human capital network.

<!-- b000080 | heading | pages [3] -->
3.1 The network among people

<!-- b000081 | prose | pages [3] -->
In the human capital network, the relationship between people can be friendship, leadership or others. In the people network, we do not take the leadership(position) into account. Namely, there is friendship among people which dos not relate to the business. In the network of friendship, we just consider the intimacy among people. If the intimacy between A and B is high and A churned in the last month, B is more likely to churn in this month. Therefore, it is necessary or us to build a model to describe the influence of others’ churn.

<!-- b000082 | caption | pages [3] -->
Figure 1: The intimacy among people

<!-- b000083 | prose | pages [3] -->
G （V，E）, whereV is the set of nodes and E is the set of edges = The network is a tuple that connect pairs of nodes. The nodes mean people working in ICM and the edges mean there is a relationship between two nodes.

<!-- b000084 | prose | pages [3] -->
There are two situations that people may churn the organization (including leave for other jobs and retire).

<!-- b000085 | prose | pages [3] -->
(1) Employees churn because their own reasons. (2) Employees churn because the people they were connected to have churned before. We assume the influence of churned people will work in the next month. That is to say, if A

<!-- b000086 | furniture | pages [3] -->


<!-- b000087 | furniture | pages [4] -->
Team #37284                                                                Page 3 of 20

<!-- b000088 | prose | pages [4] -->
churned in this month and B is connected to A. And then if B wants to churn under the influence of A, he only can churn in the next month. When discussing the fluid of human capital network, we should measure the probability of churn.

<!-- b000089 | prose | pages [4] -->
In get further discussion, we define two indices: loyalty() and intimacy( ). Loyalty refers to people’s inner character, which means the probability of retaining in the organization. More specifically, the loyalty of a person is, and the probability for he or she to . In this part, we know that many factors will influence the value of, such as the  1- churn is ratio of working time and mean time of moving up into the higher position, the culture of organization, the expectation of the employee and so on. Since many inner character will not change, we define the initial loyalty as :

<!-- b000090 | prose | pages [4] -->
 (0)

<!-- b000091 | prose | pages [4] -->
Where: F means a function.

<!-- b000092 | prose | pages [4] -->
  F c e ( , )

<!-- b000093 | furniture | pages [4] -->


<!-- b000094 | furniture | pages [4] -->


<!-- b000095 | prose | pages [4] -->
c means the factor cause by organization culture; e means the expectation discrepancy factor. Of course, the loyalty will change with the change of position levels and the years retaining in the same position level. We will discuss it in the following dynamic process section.

<!-- b000096 | prose | pages [4] -->
Intimacy refers to the influence among people, which is an exterior character determined by relationship. The intimacy between people may be influenced by many factors, such as the know of time, the distance of working departments, the discrepancy of position levels, the similarity of interest and so on. In this paper, we define the initial intimacy as:

<!-- b000097 | prose | pages [4] -->
 (0) ij   F (t ,s )

<!-- b000098 | furniture | pages [4] -->


<!-- b000099 | prose | pages [4] -->
ij ij

<!-- b000100 | prose | pages [4] -->
Where: tij represents the time of know between personi and person j .

<!-- b000101 | prose | pages [4] -->
sij represents the similarity between personi and person j . Similarly, the intimacy will change with the change of the gap between people’s position level. And we also discuss it in the dynamic process.

<!-- b000102 | prose | pages [4] -->
After giving the definition of loyalty and intimacy, we can take a look at the network.

<!-- b000103 | furniture | pages [4] -->


<!-- b000104 | caption | pages [4] -->
Figure 2: The network of loyalty and intimacy

<!-- b000105 | prose | pages [4] -->
As shown in Figure 2, we can clearly see the relationship between two people and the description of  and . At the beginning, the initial loyalty and intimacy consist of a initial network. As time goes on, the network changes in the dynamic process. Every month, it is a static network and has new loyalty and intimacy. The dynamic process will be discussed in the following part.

<!-- b000106 | heading | pages [4] -->
3.2 The network among position

<!-- b000107 | prose | pages [4] -->
Obviously, the relationship of positions can form a tree network. In this problem, we regards there are six levels of positions in ICM organization, which refers to the level of salary. The highest level is senior manager and the lowest level is administrative clerk and inexperienced employee.

<!-- b000108 | furniture | pages [4] -->


<!-- b000109 | furniture | pages [5] -->
Team #37284                                                                Page 4 of 20

<!-- b000110 | furniture | pages [5] -->


<!-- b000111 | caption | pages [5] -->
Figure 3: A tree network of positions

<!-- b000112 | prose | pages [5] -->
In the position network, the nodes mean positions. Additionally, the solid line with arrow represents the belonging relation and the dash line means the adjustment of position. In a whole, this graph indicates the level structure among positions and the adjustment from one position to another one.

<!-- b000113 | prose | pages [5] -->
If a person moves up into a higher position, the loyalty and intimacy will change. Hence, we use the position network to analyze the influence on loyalty and intimacy with the change of positon.

<!-- b000114 | prose | pages [5] -->
For the change of loyalty, we define a transformation matrix to describe the influence of position changes.

<!-- b000115 | prose | pages [5] -->


<!-- b000116 | prose | pages [5] -->
t

<!-- b000117 | prose | pages [5] -->
11

<!-- b000118 | prose | pages [5] -->


<!-- b000119 | prose | pages [5] -->
t

<!-- b000120 | prose | pages [5] -->
 

<!-- b000121 | prose | pages [5] -->
21

<!-- b000122 | prose | pages [5] -->
T

<!-- b000123 | prose | pages [5] -->


<!-- b000124 | prose | pages [5] -->
t

<!-- b000125 | prose | pages [5] -->


<!-- b000126 | prose | pages [5] -->
m

<!-- b000127 | prose | pages [5] -->
1

<!-- b000128 | prose | pages [5] -->


<!-- b000129 | prose | pages [5] -->
t t t

<!-- b000130 | prose | pages [5] -->
12 1

<!-- b000131 | prose | pages [5] -->
m

<!-- b000132 | prose | pages [5] -->


<!-- b000133 | prose | pages [5] -->
t t t

<!-- b000134 | prose | pages [5] -->


<!-- b000135 | prose | pages [5] -->
22 2

<!-- b000136 | prose | pages [5] -->
m

<!-- b000137 | furniture | pages [5] -->


<!-- b000138 | prose | pages [5] -->
 

<!-- b000139 | prose | pages [5] -->
t t t

<!-- b000140 | prose | pages [5] -->


<!-- b000141 | prose | pages [5] -->
m

<!-- b000142 | prose | pages [5] -->
2

<!-- b000143 | prose | pages [5] -->
mm

<!-- b000144 | prose | pages [5] -->
ijt means the change of loyalty if people move from level i position to level j Where:

<!-- b000145 | prose | pages [5] -->
position m means the quantity of position level  (t ) 0t and he moves from position For example, an employee has an initial loyalty at time 0

<!-- b000146 | prose | pages [5] -->
i to j in the next month. According to the influence brought by position change, we can get his new loyalty.

<!-- b000147 | prose | pages [5] -->
    (t ) ijt

<!-- b000148 | furniture | pages [5] -->


<!-- b000149 | prose | pages [5] -->
0

<!-- b000150 | prose | pages [5] -->
t t 1 1

<!-- b000151 | prose | pages [5] -->
The adjustment of position can also bring some change to the intimacy. However, we will discuss it in section 4.2.

<!-- b000152 | heading | pages [5] -->
3.3 The bipartite graph between people and positions

<!-- b000153 | prose | pages [5] -->
We have introduced the graph among people and positions respectively. It is time to take a look at the graph between staff and positions. Each person in ICM can take a wide range of positions, and it is a problem for HR manager to assign these jobs to staff. We can use a bipartite graph[4] [5] to describe this problem.

<!-- b000154 | prose | pages [5] -->
In general, there are two sets which represent staff and occupations. The edge matching an employee to an occupation means this person is assigned to this position by HR manager. In addition, each edge has a value which indicates the cost if this person take this job. It is vivid to show in the following figure.

<!-- b000155 | furniture | pages [5] -->


<!-- b000156 | caption | pages [5] -->
Figure 4: The match between employees and occupations

<!-- b000157 | furniture | pages [5] -->


<!-- b000158 | furniture | pages [6] -->
Team #37284                                                                Page 5 of 20

<!-- b000159 | prose | pages [6] -->
Where: U is the set of employees;

<!-- b000160 | prose | pages [6] -->
V is the set of positions. In the ICM, there are seven kinds of positons. In addition,

<!-- b000161 | prose | pages [6] -->
8v inV , and the person who connects to that vertex we added a virtual vertex means that he is under training. iu is the employee i .

<!-- b000162 | furniture | pages [6] -->


<!-- b000163 | prose | pages [6] -->
iv is the i kind of position.

<!-- b000164 | furniture | pages [6] -->


<!-- b000165 | furniture | pages [6] -->


<!-- b000166 | prose | pages [6] -->
The value of each edge means the cost of assigning personi to position j .

<!-- b000167 | prose | pages [6] -->
iu to iv means iu can be assigned to iv and the blue The edge connecting edge means the decision finally made by the HR manager. It is worth mentioning the characters of our bipartite graph. Firstly, there may not exist a perfect matching(every vertex in U is connect to different vertices in V). In our graph, not all people may have a job and not all jobs are taken by people. Secondly, the vertices in occupational set represents levels of position, so many staff can connect to the same vertex in V.

<!-- b000168 | prose | pages [6] -->
Finally, we use a bipartite graph to describe the problem of job assignment. In this way, once we determine the cost of each assignment and the possibility of each matching, we can get the best matching plan.

<!-- b000169 | heading | pages [6] -->
3.4 The human capital network

<!-- b000170 | prose | pages [6] -->
In section 3.1 to 3.3, we introduce three graphs respectively: the friendship network among people, the network among positions and the matching graph between staff and positions. Now we put three graphs together and then get a static human capital network. It is shown in the figure below.

<!-- b000171 | furniture | pages [6] -->


<!-- b000172 | caption | pages [6] -->
Figure 5: A static human capital network

<!-- b000173 | prose | pages [6] -->
In this network, we can see the relationship among people and also the relationship among the positions. Additionally, it can indicate the matching between staff and positions. According to this network, we can see the static human capital network and it will be the basic of managing the human capital in organizations.

<!-- b000174 | heading | pages [6] -->
4. The dynamic human capital network

<!-- b000175 | heading | pages [6] -->
4.1 The frame of the model

<!-- b000176 | prose | pages [6] -->
In order to identify dynamic processes within our Human Capital network, we take time into consideration to form a dynamic human capital network.

<!-- b000177 | prose | pages [6] -->
In the assumption, we define one month to be the time unit. Now we add the time stamp to the static human capital network and get a dynamic one shown in figure 6.

<!-- b000178 | furniture | pages [6] -->


<!-- b000179 | furniture | pages [7] -->
Team #37284                                                                Page 6 of 20

<!-- b000180 | furniture | pages [7] -->


<!-- b000181 | caption | pages [7] -->
Figure 6: A dynamic human capital network

<!-- b000182 | furniture | pages [7] -->


<!-- b000183 | prose | pages [7] -->
In the picture, there are several levels. In detail, every layer indicates a human capital network at a specific time. It contains the set of people, the set of positions and the matching relation between individuals and positions. As time goes by, the content in each level changes and a dynamic human capital network generates.

<!-- b000184 | prose | pages [7] -->
More specifically, there are three kinds of change in the network. (1) No people churn and no new recruited people. The HR manager can adjust the matching between people and positions to influence the whole network.

<!-- b000185 | prose | pages [7] -->
(2) Some people churn and the connections between some retaining employees and churned employees disappear. Then the HR should decide to recruit new employees to fill with the positions. Of course, he also can adjust the retaining people’s positions to minimize the cost and maximum the output.

<!-- b000186 | prose | pages [7] -->
(3) Some people join in the organization and there are some new connections in the network among people. Then the HR manager should assign them into the vacant positions.

<!-- b000187 | heading | pages [7] -->
4.2 The change of loyalty and intimacy in the dynamic process

<!-- b000188 | prose | pages [7] -->
In the dynamic process, the loyalty will change with the change of position levels and the years retaining in the same position level. We can define the change of loyalty as:

<!-- b000189 | prose | pages [7] -->
(1) Retaining in the same position level

<!-- b000190 | prose | pages [7] -->


<!-- b000191 | prose | pages [7] -->
  

<!-- b000192 | prose | pages [7] -->
n

<!-- b000193 | prose | pages [7] -->


<!-- b000194 | prose | pages [7] -->


<!-- b000195 | prose | pages [7] -->
 

<!-- b000196 | prose | pages [7] -->
 

<!-- b000197 | prose | pages [7] -->
(0)

<!-- b000198 | prose | pages [7] -->
 

<!-- b000199 | prose | pages [7] -->
12 d

<!-- b000200 | furniture | pages [7] -->


<!-- b000201 | prose | pages [7] -->
Where: d means the change proportion of loyalty as years goes on. n means the number of months that the employee stay in the same position.

<!-- b000202 | prose | pages [7] -->
means the mean years to promotion at a specific position The loyalty of an employee will decrease if his working time in one position is more than the mean promotion years. Similarly, the loyalty of an employee will increase if his working time in one position is less than the mean promotion years.

<!-- b000203 | prose | pages [7] -->
(2) Position adjustment

<!-- b000204 | furniture | pages [7] -->


<!-- b000205 | caption | pages [7] -->
Figure 7: The change of loyalty when position changes

<!-- b000206 | prose | pages [7] -->


<!-- b000207 | furniture | pages [7] -->


<!-- b000208 | prose | pages [7] -->
  

<!-- b000209 | prose | pages [7] -->
(0)

<!-- b000210 | prose | pages [7] -->
ijt

<!-- b000211 | furniture | pages [7] -->


<!-- b000212 | prose | pages [7] -->
ijt means the change proportion of loyalty moving from position i to position j . Where: Consider the skip of promotion, we define that:

<!-- b000213 | prose | pages [7] -->
t   t t

<!-- b000214 | furniture | pages [7] -->


<!-- b000215 | prose | pages [7] -->
ij ij ik kj Similarly, the intimacy will change with the change of the gap between people’s position

<!-- b000216 | furniture | pages [7] -->


<!-- b000217 | furniture | pages [8] -->
Team #37284                                                                Page 7 of 20

<!-- b000218 | prose | pages [8] -->
level. There are three kinds of situations that may change the intimacy:

<!-- b000219 | furniture | pages [8] -->


<!-- b000220 | caption | pages [8] -->
Figure 8: The intimacy changes in different situations

<!-- b000221 | prose | pages [8] -->
(1)The position gap enlarges If a person is promoted and another one stay in the same positon, their intimacy will decrease because they have fewer common topics or the person at a lower position envies another with a higher position.

<!-- b000222 | prose | pages [8] -->
(2)The position gap shortens If the employee with a lower position is promoted to the same position level as another with

<!-- b000223 | furniture | pages [8] -->


<!-- b000224 | prose | pages [8] -->
a higher position, their intimacy will increase because they have more chance to contact each other.

<!-- b000225 | prose | pages [8] -->
(3)The position gap stays the same If two persons all stay in the old position or they are promoted with a same grade, their intimacy will not change.

<!-- b000226 | prose | pages [8] -->
So we use the gap between people’s position levels to calculate the change of intimacy. The intimacy is defined as:

<!-- b000227 | prose | pages [8] -->
  

<!-- b000228 | prose | pages [8] -->
ij

<!-- b000229 | prose | pages [8] -->


<!-- b000230 | prose | pages [8] -->
 

<!-- b000231 | prose | pages [8] -->
 

<!-- b000232 | prose | pages [8] -->
l

<!-- b000233 | prose | pages [8] -->
1

<!-- b000234 | prose | pages [8] -->
old

<!-- b000235 | prose | pages [8] -->
(0) (0)

<!-- b000236 | furniture | pages [8] -->


<!-- b000237 | prose | pages [8] -->
 

<!-- b000238 | prose | pages [8] -->
ij ij

<!-- b000239 | prose | pages [8] -->
  l

<!-- b000240 | prose | pages [8] -->
1

<!-- b000241 | prose | pages [8] -->
new

<!-- b000242 | prose | pages [8] -->
represents the primary difference between the level of person i and j . l Where:

<!-- b000243 | prose | pages [8] -->
old  represents the new difference between the level of personi and j . l

<!-- b000244 | furniture | pages [8] -->


<!-- b000245 | prose | pages [8] -->
new The gap between position levels of position can be given as:

<!-- b000246 | caption | pages [8] -->
Table 1: The levels of positions

<!-- b000247 | prose | pages [8] -->
Position Level Administrative clerk, Inexperienced employee Experienced employee Inexperienced supervisor Experienced supervisor Junior manager Senior manager And the gap between position levels is:

<!-- b000248 | prose | pages [8] -->
 l

<!-- b000249 | prose | pages [8] -->
ipl means the level of position i .

<!-- b000250 | prose | pages [8] -->
Where:

<!-- b000251 | heading | pages [8] -->
4.3 The calculation of loyalty

<!-- b000252 | prose | pages [8] -->
1 2 3 4 5 6

<!-- b000253 | prose | pages [8] -->
 l l

<!-- b000254 | furniture | pages [8] -->


<!-- b000255 | prose | pages [8] -->
p p i j

<!-- b000256 | prose | pages [8] -->
As we mentioned in section 3.1, Loyalty is influenced by many factors. If a person is promoted by HR manager, his loyalty may be change. Also, if a person stay at one position too long and have little expectation to be promoted, his loyalty may drop. Now we discuss the calculation about the change.

<!-- b000257 | prose | pages [8] -->
 ( )t At time t , we define the loyalty of employee k as

<!-- b000258 | prose | pages [8] -->
   ( ) t [

<!-- b000259 | prose | pages [8] -->
( )t

<!-- b000260 | prose | pages [8] -->
and let k

<!-- b000261 | prose | pages [8] -->
  ( ) ( ) t t ( ) t ( ) t , , , , ]

<!-- b000262 | furniture | pages [8] -->


<!-- b000263 | prose | pages [8] -->
1 1 2 n

<!-- b000264 | prose | pages [8] -->
(t) a

<!-- b000265 | prose | pages [8] -->
A  to indicate the assignment of jobs. The element Then we define a matrix N M

<!-- b000266 | furniture | pages [8] -->


<!-- b000267 | prose | pages [8] -->
is defined as: ij

<!-- b000268 | furniture | pages [9] -->
Team #37284                                                                Page 8 of 20

<!-- b000269 | prose | pages [9] -->
 if employiisat position j

<!-- b000270 | prose | pages [9] -->
1

<!-- b000271 | prose | pages [9] -->


<!-- b000272 | prose | pages [9] -->
( )

<!-- b000273 | prose | pages [9] -->
t

<!-- b000274 | prose | pages [9] -->
a

<!-- b000275 | prose | pages [9] -->
ij

<!-- b000276 | furniture | pages [9] -->


<!-- b000277 | prose | pages [9] -->
if employiisnot at position j

<!-- b000278 | prose | pages [9] -->
0

<!-- b000279 | prose | pages [9] -->


<!-- b000280 | prose | pages [9] -->
diag [M] Let function as

<!-- b000281 | prose | pages [9] -->
 diag M

<!-- b000282 | prose | pages [9] -->
[ ]

<!-- b000283 | prose | pages [9] -->
According to the calculation of matrix, we can get:

<!-- b000284 | prose | pages [9] -->
   ( ) t ( t 1) ( t diag A [

<!-- b000285 | prose | pages [9] -->
   M M if i j ij

<!-- b000286 | furniture | pages [9] -->


<!-- b000287 | prose | pages [9] -->


<!-- b000288 | prose | pages [9] -->
0

<!-- b000289 | prose | pages [9] -->
if i j  

<!-- b000290 | prose | pages [9] -->
    1) 1) TA ] where t 1 ( ) t

<!-- b000291 | prose | pages [9] -->
is the transpose of (t)

<!-- b000292 | prose | pages [9] -->
(t)

<!-- b000293 | prose | pages [9] -->
A .

<!-- b000294 | prose | pages [9] -->
A Where T is the matrix we introduced in section 3.2 and

<!-- b000295 | prose | pages [9] -->
In order to give a more intuitionistic expression, we show an example to illustrate these t , they 1 formulas. In the following graph, there are four positions and two employees. At time are at position 4 and position 3 and the corresponding loyalty is 0.95 and 0.92. At time t , they all get promoted. Then we can calculate their loyalty at time t .

<!-- b000296 | furniture | pages [9] -->


<!-- b000297 | caption | pages [9] -->
Figure 9: The calculation of loyalty when promoted

<!-- b000298 | prose | pages [9] -->
According to the figure, we know:

<!-- b000299 | prose | pages [9] -->
t   ( 1) [0.95,0.92]

<!-- b000300 | prose | pages [9] -->
  0 1 0 0  (t) A

<!-- b000301 | prose | pages [9] -->
,

<!-- b000302 | prose | pages [9] -->
 1 0 0 0  

<!-- b000303 | prose | pages [9] -->
Then we can get their loyalty at timet :

<!-- b000304 | prose | pages [9] -->
 

<!-- b000305 | prose | pages [9] -->
  

<!-- b000306 | prose | pages [9] -->
( )

<!-- b000307 | prose | pages [9] -->
t

<!-- b000308 | prose | pages [9] -->
(

<!-- b000309 | prose | pages [9] -->
t

<!-- b000310 | prose | pages [9] -->
1) (

<!-- b000311 | prose | pages [9] -->
t

<!-- b000312 | prose | pages [9] -->
1)

<!-- b000313 | prose | pages [9] -->
T diag A

<!-- b000314 | prose | pages [9] -->
[

<!-- b000315 | prose | pages [9] -->
TA

<!-- b000316 | prose | pages [9] -->
] [0.95,0.92]

<!-- b000317 | prose | pages [9] -->
diag

<!-- b000318 | prose | pages [9] -->
( )

<!-- b000319 | prose | pages [9] -->
t

<!-- b000320 | prose | pages [9] -->
 

<!-- b000321 | prose | pages [9] -->
1.03 0

<!-- b000322 | prose | pages [9] -->
 

<!-- b000323 | prose | pages [9] -->
[0.95,0.92] [0.9785,0.9384]

<!-- b000324 | prose | pages [9] -->
 

<!-- b000325 | prose | pages [9] -->
0 1.02

<!-- b000326 | prose | pages [9] -->
 

<!-- b000327 | prose | pages [9] -->
 

<!-- b000328 | prose | pages [9] -->
0 0 0 1

<!-- b000329 | prose | pages [9] -->
A  

<!-- b000330 | prose | pages [9] -->
( (

<!-- b000331 | prose | pages [9] -->
t t

<!-- b000332 | prose | pages [9] -->
1) , ,

<!-- b000333 | furniture | pages [9] -->


<!-- b000334 | prose | pages [9] -->


<!-- b000335 | prose | pages [9] -->
0 0 1 0

<!-- b000336 | prose | pages [9] -->
 

<!-- b000337 | prose | pages [9] -->
 

<!-- b000338 | prose | pages [9] -->
1 0 0 0

<!-- b000339 | prose | pages [9] -->
 

<!-- b000340 | prose | pages [9] -->
1.05 1 0 0

<!-- b000341 | prose | pages [9] -->
  

<!-- b000342 | prose | pages [9] -->
T T

<!-- b000343 | furniture | pages [9] -->


<!-- b000344 | prose | pages [9] -->


<!-- b000345 | prose | pages [9] -->
1.02 1 1 0

<!-- b000346 | prose | pages [9] -->
 

<!-- b000347 | prose | pages [9] -->
1.07 1.03 1 1

<!-- b000348 | prose | pages [9] -->
 

<!-- b000349 | prose | pages [9] -->
     

<!-- b000350 | prose | pages [9] -->
1 0 0 0 0 1

<!-- b000351 | prose | pages [9] -->
       

<!-- b000352 | prose | pages [9] -->
0 0 0 1 1.05 1 0 0 1 0

<!-- b000353 | prose | pages [9] -->
             

<!-- b000354 | prose | pages [9] -->
0 0 1 0 1.02 1 1 0 0 0

<!-- b000355 | prose | pages [9] -->
       

<!-- b000356 | furniture | pages [9] -->


<!-- b000357 | prose | pages [9] -->
  

<!-- b000358 | prose | pages [9] -->
1.07 1.03 1 1 0 0

<!-- b000359 | prose | pages [9] -->
     

<!-- b000360 | heading | pages [9] -->
4.4 Organizational churn in dynamic process

<!-- b000361 | prose | pages [9] -->
In every month, we know every individual’s loyalty, which may be adjusted by the regulation of position or the churn of connected people. According to the loyalty, we can simulate the organizational churn.

<!-- b000362 | prose | pages [9] -->
There are two reasons may lead to people’s churn. (1) People want to churn for their own reasons, which are not influenced by connecting people. Loyalty will identify this situation.

<!-- b000363 | prose | pages [9] -->
(2) People want to churn because of connecting people’s influence. For this reason, we take both loyalty and intimacy into account.

<!-- b000364 | prose | pages [9] -->
The whole process can be described as follows. In the first month, people may churn according to their initial loyalty, which leads to the

<!-- b000365 | furniture | pages [9] -->


<!-- b000366 | furniture | pages [10] -->
Team #37284                                                                Page 9 of 20

<!-- b000367 | prose | pages [10] -->
change of human capital network. Then in the following month, we should calculate two kinds of probability for each employee. The first one is the churn probability influenced by connected people who has churned in the last month.

<!-- b000368 | prose | pages [10] -->
 P i

<!-- b000369 | prose | pages [10] -->
is the loyalty of employeei ; Where:

<!-- b000370 | prose | pages [10] -->
i

<!-- b000371 | prose | pages [10] -->
    (1 )

<!-- b000372 | furniture | pages [10] -->


<!-- b000373 | prose | pages [10] -->
i ij j j

<!-- b000374 | prose | pages [10] -->
j is the person who connected to i and churned in the last month.

<!-- b000375 | prose | pages [10] -->
is the intimacy between employeei and j ;

<!-- b000376 | furniture | pages [10] -->


<!-- b000377 | prose | pages [10] -->
ij The second one is loyalty. We simulate the change of human capital network according to their loyalty like the first month. Actually, we calculate two kinds of probability can effectively distinguish the churn caused by their own wills or others’ influence. As the time goes by, it forms the dynamic process of within the human capital network.

<!-- b000378 | prose | pages [10] -->
In the network among people, the dynamic process can be described in the figure 10.

<!-- b000379 | furniture | pages [10] -->


<!-- b000380 | caption | pages [10] -->
Figure 10: Dynamic process of the change of human capital network

<!-- b000381 | heading | pages [10] -->
4.5 The productivity and cost

<!-- b000382 | prose | pages [10] -->
As we all know, the task of HR is maximize the output and minimize the cost. Maximizing the profit is the most important principle of all profit organization. Then, we discuss the productivity and cost.

<!-- b000383 | heading | pages [10] -->
4.5.1 Productivity

<!-- b000384 | prose | pages [10] -->
In this paper, we assume the output is related to the rate of on-the-job and the organizational structure. In the provided data we know ICM usually has only 85% of its 370 positions filled at any time. So we assume that under this situation the organization can operate effectively and make maximum output.

<!-- b000385 | furniture | pages [10] -->


<!-- b000386 | furniture | pages [11] -->
Team #37284                                                                Page 10 of 20

<!-- b000387 | prose | pages [11] -->
There are two factors will influence the output (1)The number of employees (2)The structure of the organization A good organizational means every level has moderate people. If the organization has too many senior and junior mangers and few employees, the productivity will not be high because few people do the direct production work. Similarly, if the organization has too many inexperienced employees and experienced employees, the operation of the organization will not be good because few people assign job and consider the overall plan. In conclusion, keep 85% of every level’s position filled will be the best.

<!-- b000388 | prose | pages [11] -->
Considering two factors, we can get the productivity of the organization.

<!-- b000389 | prose | pages [11] -->
6

<!-- b000390 | prose | pages [11] -->


<!-- b000391 | prose | pages [11] -->


<!-- b000392 | prose | pages [11] -->
 

<!-- b000393 | prose | pages [11] -->
Y = S i i

<!-- b000394 | prose | pages [11] -->


<!-- b000395 | prose | pages [11] -->
i 1

<!-- b000396 | prose | pages [11] -->
iis a coefficient,  iS

<!-- b000397 | prose | pages [11] -->
6

<!-- b000398 | prose | pages [11] -->
 

<!-- b000399 | prose | pages [11] -->


<!-- b000400 | prose | pages [11] -->
  

<!-- b000401 | prose | pages [11] -->
n n S n n

<!-- b000402 | furniture | pages [11] -->


<!-- b000403 | prose | pages [11] -->
i i i i i i

<!-- b000404 | prose | pages [11] -->


<!-- b000405 | prose | pages [11] -->
i 1

<!-- b000406 | prose | pages [11] -->
means the output produced by people who are in i position Where:

<!-- b000407 | prose | pages [11] -->
i level. We assume people’s output is proportional to their salary. is a coefficient,  iS means the loss of output if the number of on-the -job staff

<!-- b000408 | furniture | pages [11] -->


<!-- b000409 | prose | pages [11] -->
i i is larger or smaller than the optimal number. in means the number of staff who are now on-the-job in i position level.

<!-- b000410 | furniture | pages [11] -->


<!-- b000411 | prose | pages [11] -->
in means the optimal number of staff who are now on-the-job in i position level.

<!-- b000412 | furniture | pages [11] -->


<!-- b000413 | prose | pages [11] -->
Obviously, this equation is comprised of two parts. The first part is related to the number of employees, which means more workers will produce more. This is the direct effects caused by the dynamic processes within the human capital network. The second part is related to the structure of the organization. A good structure will produce more. Once the structure become unbalanced, including redundant or vacant, it will bring some negative effects to the output. And this is the indirect effects caused by the dynamic processes within the human capital network.

<!-- b000414 | heading | pages [11] -->
4.5.2 Cost

<!-- b000415 | prose | pages [11] -->
Considering that the provided data dos NOT contain the staff’s output, we cannot use the maximum profit to measure an optimal human capital. Therefore, in the paper, we set our target as minimize the cost.

<!-- b000416 | prose | pages [11] -->
In section 4.1, we mention the loss of unbalanced organizational structure. Actually, it also can be regarded as cost, which caused by unbalanced structure. In general, the cost contains several parts.

<!-- b000417 | prose | pages [11] -->
(1) The cost of organizational structure (2) The cost of salary, training and recruitment. Then, we can get the total cost( C ) as:

<!-- b000418 | prose | pages [11] -->
C    C C

<!-- b000419 | furniture | pages [11] -->


<!-- b000420 | prose | pages [11] -->
1 2 C means the annual cost of organizational structure. Where:

<!-- b000421 | prose | pages [11] -->
1 C means the annual cost of salary, training and recruitment.

<!-- b000422 | furniture | pages [11] -->


<!-- b000423 | prose | pages [11] -->
2 Obviously, we can have:

<!-- b000424 | prose | pages [11] -->
6

<!-- b000425 | prose | pages [11] -->
 

<!-- b000426 | prose | pages [11] -->
C 1

<!-- b000427 | prose | pages [11] -->


<!-- b000428 | prose | pages [11] -->
i  

<!-- b000429 | prose | pages [11] -->
  

<!-- b000430 | prose | pages [11] -->
S n n

<!-- b000431 | furniture | pages [11] -->


<!-- b000432 | prose | pages [11] -->
i i i i i 1 1

<!-- b000433 | prose | pages [11] -->
When calculating the cost of every individual, we assume that they all need be trained every year. Then we can have

<!-- b000434 | prose | pages [11] -->
6

<!-- b000435 | prose | pages [11] -->
   

<!-- b000436 | prose | pages [11] -->
C S n

<!-- b000437 | prose | pages [11] -->
2

<!-- b000438 | prose | pages [11] -->
i i

<!-- b000439 | prose | pages [11] -->


<!-- b000440 | prose | pages [11] -->
i

<!-- b000441 | prose | pages [11] -->
1

<!-- b000442 | prose | pages [11] -->
6 6 6

<!-- b000443 | prose | pages [11] -->
     

<!-- b000444 | prose | pages [11] -->
new old r n k n

<!-- b000445 | furniture | pages [11] -->


<!-- b000446 | prose | pages [11] -->
i i i i

<!-- b000447 | prose | pages [11] -->
  

<!-- b000448 | prose | pages [11] -->
i i

<!-- b000449 | prose | pages [11] -->
1 1

<!-- b000450 | prose | pages [11] -->
i

<!-- b000451 | prose | pages [11] -->
1

<!-- b000452 | prose | pages [11] -->
ik means the average annual training cost of position level i . Where:

<!-- b000453 | prose | pages [11] -->
ir means the average annual recruitment cost of position level i .

<!-- b000454 | furniture | pages [11] -->


<!-- b000455 | prose | pages [11] -->
new in means the number of new staff of position level i .

<!-- b000456 | furniture | pages [11] -->


<!-- b000457 | prose | pages [11] -->
old in means the number of the old on-the-job staff of position level i As a HR manager, his job is managing the human capital with comprehensive consideration of direct cost and indirect cost.

<!-- b000458 | furniture | pages [11] -->


<!-- b000459 | furniture | pages [12] -->
Team #37284                                                                Page 11 of 20

<!-- b000460 | heading | pages [12] -->
4.6 Optimize the management of human capital

<!-- b000461 | prose | pages [12] -->
In the section 3.3, we have built a bipartite to indicate the matching of people and positions. According to section 4.2, we know the cost of every matching. And then our target is to minimize the total cost and get the optimal human capital structure. Now, we use Genetic Algorithm to assign positions.

<!-- b000462 | prose | pages [12] -->
A typical genetic algorithm requires two aspects[6]: (1)A genetic representation (2)The definition of fitness function Now, we apply this algorithm to our assignment problem. First, we give the concrete explanation of these two aspects.

<!-- b000463 | prose | pages [12] -->
(1)The representation of chromosome The represent of chromosome is the basic of Genetic Algorithm[7]. As we know, the chromosomes are the units that indicate people’s character. In our model, a valid chromosome is an effective assignment of positions. We use the following indices:

<!-- b000464 | caption | pages [12] -->
Table 2: The meanings of indexes

<!-- b000465 | prose | pages [12] -->
Index Meaning 0 people are new recruited and still under training 1-6 People in six position levels relation to their salary, higher is better N The people are not in the organization now. D The people departed from the organization thi bit stands for that the level of Then, the chromosome is a series of numbers. The thi person. position of the

<!-- b000466 | furniture | pages [12] -->


<!-- b000467 | caption | pages [12] -->
Figure 11: The chromosome we defined

<!-- b000468 | furniture | pages [12] -->


<!-- b000469 | prose | pages [12] -->
(2)The Fitness Function The fitness function is to evaluate the fitness of an individual whether it can suit to the environment. That is to say, this function is used as an elimination criterion. In our model, we can use total cost as the fitness function.

<!-- b000470 | prose | pages [12] -->
The Genetic Algorithm(GA) process contains four steps: Initialization, Selection, Genetic operators, Termination. It is an iterative process and each process represents a generation. With the finite numbers of iteration, the algorithm can produce an approximate optimal solution[8].  Initialization At this stage we define the number of population (N), mutation rate, crossover rate, fitness function. Then it will produce the initial individuals. In our model, we produce the chromosome 0t . of positions at time  Selection We use the fitness function to select the first N individuals which are better fit to the environment. It is worth mentioning that a chromosome will be eliminated immediately if the structure is unreasonable. For example, there are only 25 positions in level 3. However, the number of “3” is more than 25 in the chromosome. As a result, we eliminate this chromosome.  Genetic operators There are two main operations, mutation and crossover, which are the methods to produce new individuals.

<!-- b000471 | prose | pages [12] -->
Mutation in GA is that a gene of a chromosome changes to any other possible gene with a possibility. In our model, changing a gene represents the promotion of a person. So the number should increase when the gene is under mutation.

<!-- b000472 | prose | pages [12] -->
Crossover in GA is that two chromosomes exchange their genes with each other at the same

<!-- b000473 | furniture | pages [12] -->


<!-- b000474 | furniture | pages [13] -->
Team #37284                                                                Page 12 of 20

<!-- b000475 | prose | pages [13] -->
position at their chromosomes. In our model, we only take promotion into account. Hence, the exchange can only happen when the person who has the lower position get exchanged with the

<!-- b000476 | prose | pages [13] -->
same position with the higher position level.

<!-- b000477 | caption | pages [13] -->
Figure 12: Genetic operators

<!-- b000478 | furniture | pages [13] -->


<!-- b000479 | prose | pages [13] -->
In the picture, the left are two chromosomes represent two individuals. In the middle,

<!-- b000480 | prose | pages [13] -->
chromosome A has a mutation on one gene, which means that the person was promoted from

<!-- b000481 | prose | pages [13] -->
level 3 to level 4, so does the chromosome B. On the right, chromosome B get the same gene

<!-- b000482 | prose | pages [13] -->
with A at the red point, which means that the person was promoted form level 3 to level 5.  Termination With the finite times of iteration, the algorithm will come to termination. Finally, the individual with the highest fitness is an approximate optimal solution.

<!-- b000483 | prose | pages [13] -->
To give a more visual process, a flowchart is shown.

<!-- b000484 | furniture | pages [13] -->


<!-- b000485 | caption | pages [13] -->
Figure 13: The flowchart of termination

<!-- b000486 | furniture | pages [13] -->


<!-- b000487 | prose | pages [13] -->
To sum up, the whole process of managing human capital consists three parts: (1) The change of loyalty and intimacy (2) The churn and recruitment of people

<!-- b000488 | furniture | pages [13] -->


<!-- b000489 | furniture | pages [14] -->
Team #37284                                                                Page 13 of 20

<!-- b000490 | prose | pages [14] -->
(3) The assignment of HR manager The first part can be calculated as the human capital network changes. The second part is dependent on computer simulation. The third part is the only one that we can intervene. We use the Genetic Algorithm to get the optimal assignment and do some adjustment. All in all, the whole model can be described as:

<!-- b000491 | furniture | pages [14] -->


<!-- b000492 | caption | pages [14] -->
Figure 14: The pie of the whole model

<!-- b000493 | heading | pages [14] -->
5. Application of the Model

<!-- b000494 | heading | pages [14] -->
5.1 The organization’s budget requirements

<!-- b000495 | prose | pages [14] -->
According to the provided data, ICM usually has 85% of its 370 positions filled at any time and the HR office is actively hiring about 8-10% of its position. In addition, the current churn rate is 18%, which can keep the organization on an optimal structure.

<!-- b000496 | prose | pages [14] -->
The annual budget requirements for recruiting and training can be calculated as:

<!-- b000497 | prose | pages [14] -->
6

<!-- b000498 | prose | pages [14] -->
 

<!-- b000499 | prose | pages [14] -->
B = r n i

<!-- b000500 | prose | pages [14] -->


<!-- b000501 | prose | pages [14] -->
i 1

<!-- b000502 | prose | pages [14] -->
6

<!-- b000503 | prose | pages [14] -->
  

<!-- b000504 | prose | pages [14] -->
new old k n

<!-- b000505 | furniture | pages [14] -->


<!-- b000506 | prose | pages [14] -->
i i i i

<!-- b000507 | prose | pages [14] -->


<!-- b000508 | prose | pages [14] -->
i 1

<!-- b000509 | prose | pages [14] -->
ir represents the cost of recruitment at position level i . Where:

<!-- b000510 | prose | pages [14] -->
ik represents the cost of training at position level i .

<!-- b000511 | furniture | pages [14] -->


<!-- b000512 | prose | pages [14] -->
new in represents the number of new employees at position level i .

<!-- b000513 | furniture | pages [14] -->


<!-- b000514 | prose | pages [14] -->
old in represents the number of old employees(not new recruited)at level i .

<!-- b000515 | furniture | pages [14] -->


<!-- b000516 | prose | pages [14] -->
Then, we start to find the number of churn people and new recruited people within next two year at any time. That is to say, we then use our model to clarify the concrete fluid of human capital network.

<!-- b000517 | prose | pages [14] -->
Step1: Initialization The initial rate of on-the-job is 85%. The hiring rate is 10%. The churn rate is 18%. And we regards 500 people are considered in the next two years. As for the initial connected relation we use a Random Graph to simulate. Since there is no data to calculate people’s initial loyalty and intimacy, we also give a random value. Then we set a parameter to multiply the loyalty and adjust the parameter to reach a churn rate of 18%.

<!-- b000518 | prose | pages [14] -->
Step2: Simulation After setting the initial value, we use the computer simulation to indicate process of “churn” and “recruit”. In this process, the change of loyalty and intimacy is calculated by our model which shown in section 3.5.2. In the simulation of this dynamic process, we can clearly see the churn people and new recruited people.

<!-- b000519 | furniture | pages [14] -->


<!-- b000520 | prose | pages [14] -->
Step3: Assignment

<!-- b000521 | furniture | pages [14] -->


<!-- b000522 | furniture | pages [15] -->
Team #37284                                                                Page 14 of 20

<!-- b000523 | prose | pages [15] -->
We use genetic algorithm to assign people to positions. In the genetic algorithm, we set the number of genes in one chromosome to be 500. In addition, let the number of population, the iteration times, the mutation rate and crossover rate to be 200, 2000, 0.4 and 0.1 respectively.

<!-- b000524 | prose | pages [15] -->
Using this method, after five times simulations, we calculate the average value and shown it in the following table.

<!-- b000525 | furniture | pages [15] -->


<!-- b000526 | furniture | pages [15] -->


<!-- b000527 | caption | pages [15] -->
Table 3: The data of simulation

<!-- b000528 | prose | pages [15] -->
The accumulative

<!-- b000529 | prose | pages [15] -->
The accumulative

<!-- b000530 | prose | pages [15] -->
The number

<!-- b000531 | prose | pages [15] -->
Churn

<!-- b000532 | prose | pages [15] -->
Churn for

<!-- b000533 | prose | pages [15] -->
Month

<!-- b000534 | prose | pages [15] -->
follows

<!-- b000535 | prose | pages [15] -->
own

<!-- b000536 | prose | pages [15] -->
of

<!-- b000537 | prose | pages [15] -->
cost of

<!-- b000538 | prose | pages [15] -->
cost of

<!-- b000539 | prose | pages [15] -->
recruitment()

<!-- b000540 | prose | pages [15] -->
training()

<!-- b000541 | prose | pages [15] -->
recruitment

<!-- b000542 | prose | pages [15] -->
others

<!-- b000543 | prose | pages [15] -->
reasons

<!-- b000544 | prose | pages [15] -->
1 0 11 1 2 3 6 4 3 1 6 1 4 0 4 1 5 0 5 3 6 0 4 2 7 0 5 3 8 1 1 1 9 1 8 3 10 0 10 5 11 1 4 3 12 1 6 4 13 0 2 1 14 0 7 3 15 0 6 4 16 1 4 2 17 1 2 1 18 1 3 2 19 0 2 3 20 0 3 9 21 1 3 6 22 0 9 6 23 1 5 2 24 1 4 5 total 14 120 75

<!-- b000545 | furniture | pages [15] -->


<!-- b000546 | furniture | pages [15] -->


<!-- b000547 | prose | pages [15] -->
0.12 5.88 0.60 11.59 0.90 17.24 1.50 22.82 3.30 28.33 4.70 33.84 8.30 39.33 8.42 44.91 9.72 50.31 11.28 55.55 12.60 60.80 15.30 65.94 15.90 71.22 17.22 76.39 18.42 81.55 19.62 86.59 20.22 91.63 21.62 96.63 24.62 101.69 26.94 106.74 29.66 111.94 33.50 117.03 34.70 122.08 38.20 127.08

<!-- b000548 | furniture | pages [15] -->


<!-- b000549 | furniture | pages [15] -->


<!-- b000550 | prose | pages [15] -->
According to the table, we can know the annual churn rate is approximate to 19% and the recruitment rate is 12%, which are close to the initial value 18% and 10%. Therefore, our simulation process is suitable. In the table, it is clear that the total cost of recruitment is 38.2 and the total cost of training is 127.08. Hence, the organization’s budget requirements for both recruiting and training over the next years are 165.28.

<!-- b000551 | heading | pages [15] -->
5.2 The influence of churn rate on full status rate for positions

<!-- b000552 | prose | pages [15] -->
If the ICM organization wants to sustain its 80% full status for positions under the change of annual churn rate, it will spend more to recruit people. In this part, we try to analyze the direct cost and indirect cost with the high churn rate.

<!-- b000553 | heading | pages [15] -->
5.2.1 Direct cost

<!-- b000554 | prose | pages [15] -->
In the section 4.5.2, the direct cost consists of three parts. Obviously, the direct cost is related to the churn rate, recruitment rate and the vacant positions’ level. If more people churn, we need to recruit more people to replace them and of course the cost will be high. Similarly, if more people in higher position levels churn, the cost will be higher that more people in lower position levels. We do the simulation as the churn rate changes. Then we get the annual direct cost.

<!-- b000555 | furniture | pages [15] -->


<!-- b000556 | furniture | pages [16] -->
Team #37284                                                                Page 15 of 20

<!-- b000557 | furniture | pages [16] -->


<!-- b000558 | furniture | pages [16] -->


<!-- b000559 | caption | pages [16] -->
Table 4: The change of cost following the churn rate

<!-- b000560 | prose | pages [16] -->
Cost of training

<!-- b000561 | prose | pages [16] -->
Churn rate

<!-- b000562 | prose | pages [16] -->
Recruitment rate to

<!-- b000563 | prose | pages [16] -->
(%)

<!-- b000564 | prose | pages [16] -->
sustain 80% full status

<!-- b000565 | prose | pages [16] -->
21 0.19

<!-- b000566 | prose | pages [16] -->
22 0.20

<!-- b000567 | prose | pages [16] -->
23 0.20

<!-- b000568 | prose | pages [16] -->
24 0.21

<!-- b000569 | prose | pages [16] -->
25 0.22

<!-- b000570 | prose | pages [16] -->
26 0.23

<!-- b000571 | prose | pages [16] -->
27 0.22

<!-- b000572 | prose | pages [16] -->
28 0.24

<!-- b000573 | prose | pages [16] -->
29 0.26

<!-- b000574 | prose | pages [16] -->
30 0.26

<!-- b000575 | prose | pages [16] -->
31 0.28

<!-- b000576 | prose | pages [16] -->
32 0.29

<!-- b000577 | prose | pages [16] -->
33 0.29

<!-- b000578 | prose | pages [16] -->
34 0.30

<!-- b000579 | prose | pages [16] -->
35 0.31

<!-- b000580 | prose | pages [16] -->
36 0.32

<!-- b000581 | prose | pages [16] -->
37 0.34

<!-- b000582 | prose | pages [16] -->
38 0.34

<!-- b000583 | prose | pages [16] -->
39 0.35

<!-- b000584 | prose | pages [16] -->
40 0.36

<!-- b000585 | prose | pages [16] -->
Cost of recruitment

<!-- b000586 | prose | pages [16] -->
Total cost

<!-- b000587 | prose | pages [16] -->
()

<!-- b000588 | prose | pages [16] -->
()

<!-- b000589 | prose | pages [16] -->
() 540 34.73 574.73

<!-- b000590 | prose | pages [16] -->
530 35.81 565.81

<!-- b000591 | prose | pages [16] -->
532 36.26 568.26

<!-- b000592 | prose | pages [16] -->
575 36.86 611.86

<!-- b000593 | prose | pages [16] -->
580 37.64 617.64

<!-- b000594 | prose | pages [16] -->
563 39.21 602.21

<!-- b000595 | prose | pages [16] -->
540 40.21 580.21

<!-- b000596 | prose | pages [16] -->
552 42.62 594.62

<!-- b000597 | prose | pages [16] -->
543 43.78 586.78

<!-- b000598 | prose | pages [16] -->
554 45.88 599.88

<!-- b000599 | prose | pages [16] -->
530 47.72 577.72

<!-- b000600 | prose | pages [16] -->
512 48.64 560.64

<!-- b000601 | prose | pages [16] -->
511 49.91 560.91

<!-- b000602 | prose | pages [16] -->
496 50.61 546.61

<!-- b000603 | prose | pages [16] -->
483 50.66 533.66

<!-- b000604 | prose | pages [16] -->
492 51.27 543.27

<!-- b000605 | prose | pages [16] -->
472 52.24 524.24

<!-- b000606 | prose | pages [16] -->
484 56.33 540.33

<!-- b000607 | prose | pages [16] -->
479 60.25 539.25

<!-- b000608 | prose | pages [16] -->
468 60.75 528.75 According to the table, we know that if the organization want to keep 80% full status for positions at a churn rate of 25%, the recruitment rate should be 22% and the direct cost is 617.64

<!-- b000609 | prose | pages [16] -->
. If the churn rate is 35%, the recruitment rate should be 31% and the direct cost is 533.66.

<!-- b000610 | furniture | pages [16] -->


<!-- b000611 | caption | pages [16] -->
Figure 15: The line chart of total cost

<!-- b000612 | furniture | pages [16] -->


<!-- b000613 | prose | pages [16] -->
From the graph, we can see the direct cost first increases and then decreases as the increase of churn rate. It is rational because as the churn rate increases, more people will under recruitment. As a result, the salary cost will decrease.

<!-- b000614 | heading | pages [16] -->
5.2.2 Indirect cost

<!-- b000615 | prose | pages [16] -->
The indirect cost is the cost caused by unbalanced organizational structure. We have  as i , which means a vacancy of a introduced it in section 4.5.2. Now we let the parameter i higher level will bring more loss . Then we calculate the indirect cost.

<!-- b000616 | furniture | pages [16] -->


<!-- b000617 | furniture | pages [17] -->
Team #37284                                                                Page 16 of 20

<!-- b000618 | furniture | pages [17] -->


<!-- b000619 | caption | pages [17] -->
Figure 16: The line chart of indirect cost

<!-- b000620 | furniture | pages [17] -->


<!-- b000621 | prose | pages [17] -->
From the graph, we can see the indirect cost increase. If the more people churn, the positions will be vacant for a period of time. As a result, some new people will join the organization. Hence, the structure will not be stable. That is to say, the indirect cost will increase.

<!-- b000622 | heading | pages [17] -->
5.2.3 Comprehensive analysis and Conclusion

<!-- b000623 | prose | pages [17] -->
As the change of churn rate and recruitment rate, the rate of full status for positions will change. In the paper, our target is to make it sustain in 80% and also keep a better structure of organization. Then we analyze every situation when churn rate and recruitment rate changes from 0% to 40%.

<!-- b000624 | furniture | pages [17] -->


<!-- b000625 | caption | pages [17] -->
Figure 17: Situations of different churn and recruitment rates

<!-- b000626 | furniture | pages [17] -->


<!-- b000627 | prose | pages [17] -->
In this picture, the circle means the rate of full status can be 80% and the structure is good under the recruitment rate and churn rate. The square means the rate of full status can be 80% but the structure is not good. The cross means the rate of full status cannot be 80%. Then, we draw the line according to the solution at each situation and get the corresponding region.

<!-- b000628 | prose | pages [17] -->
In conclusion, if the churn rate is 25%, ICM can sustain its 80 full status and the direct cost is 617.64. Similarly, if the churn rate is 35%, the direct cost is 533.66. A higher churn rate will decrease the direct cost but it will cause unsteadiness of the organizational structure, which is the indirect effect.

<!-- b000629 | heading | pages [17] -->
5.3 The HR health of the organization

<!-- b000630 | prose | pages [17] -->
In this part, we first define the HR health of the organization. It is related to the cohesion of staff, staff’s loyalty to the organization and the structure of human capital.

<!-- b000631 | prose | pages [17] -->
The churn rate is 30% in both junior managers and experienced supervisors. That is to say, there are many vacant high level positions. Without recruitment of junior managers and experienced supervisors, these positions can only be taken by qualified employees who are promoted. Then in next two years, the people in every position level will be:

<!-- b000632 | furniture | pages [17] -->


<!-- b000633 | furniture | pages [18] -->
Team #37284                                                                Page 17 of 20

<!-- b000634 | furniture | pages [18] -->


<!-- b000635 | caption | pages [18] -->
Table 5: Numbers of employees of different positions

<!-- b000636 | prose | pages [18] -->
The number

<!-- b000637 | prose | pages [18] -->
The number

<!-- b000638 | prose | pages [18] -->
The number

<!-- b000639 | prose | pages [18] -->
The number

<!-- b000640 | prose | pages [18] -->
of people get

<!-- b000641 | prose | pages [18] -->
Position

<!-- b000642 | prose | pages [18] -->
The number

<!-- b000643 | prose | pages [18] -->
The number of

<!-- b000644 | prose | pages [18] -->
of people

<!-- b000645 | prose | pages [18] -->
of recruited

<!-- b000646 | prose | pages [18] -->
of employees

<!-- b000647 | prose | pages [18] -->
promoted to

<!-- b000648 | prose | pages [18] -->
level

<!-- b000649 | prose | pages [18] -->
of employees

<!-- b000650 | prose | pages [18] -->
churn employees

<!-- b000651 | prose | pages [18] -->
promoted

<!-- b000652 | prose | pages [18] -->
employees

<!-- b000653 | prose | pages [18] -->
in two years

<!-- b000654 | prose | pages [18] -->
this level

<!-- b000655 | prose | pages [18] -->
1 153 56

<!-- b000656 | prose | pages [18] -->
2 93 30

<!-- b000657 | prose | pages [18] -->
3 21 10

<!-- b000658 | prose | pages [18] -->
4 21 13

<!-- b000659 | prose | pages [18] -->
5 17 10

<!-- b000660 | prose | pages [18] -->
6 8 2

<!-- b000661 | prose | pages [18] -->
Sum 313 121

<!-- b000662 | furniture | pages [18] -->


<!-- b000663 | prose | pages [18] -->
30 0 0 91 158

<!-- b000664 | prose | pages [18] -->
12 15 15 16 82

<!-- b000665 | prose | pages [18] -->
7 13 13 5 22

<!-- b000666 | prose | pages [18] -->
2 14 14 0 20

<!-- b000667 | prose | pages [18] -->
2 9 9 0 14

<!-- b000668 | prose | pages [18] -->
0 2 2 0 8

<!-- b000669 | prose | pages [18] -->
53 53 53 112 304

<!-- b000670 | prose | pages [18] -->
From the table, we know that the proportion of old people stay in the same position in level 1, 2 and 3 will be 43%, 55% and 19%. That is to say, people are less likely to stay on the same position and their loyalty will be improved. In addition, the new promotion rate in level 4 (experienced supervisor) and level 5(junior manager) is 66.7% and 53%. Namely, most people are just promoted to the higher level position. As a result, their loyalty will increase and they will have more motivation to work hard.

<!-- b000671 | prose | pages [18] -->
In conclusion, a higher churn rate in middle levels (junior manager and experienced supervisor) will provide more chance for people to promote. As a result, it can refresh the organizational structure and improve people’s cohesion to the organization.

<!-- b000672 | heading | pages [18] -->
6. The Analysis of Parameter

<!-- b000673 | prose | pages [18] -->
There are many parameters in our model, so it is necessary to give an analysis to these parameters. According to the assumption of our model, some parameters are abstract and determined by the data in reality. Others are selected by experiments.  Parameters determined by data Loyalty() and intimacy( ) are the parameters describing the inner character and the measurement of the relationship among people. There are abstract and we can use the daily performance of an employee to quantify these indices.

<!-- b000674 | prose | pages [18] -->
Transformation Matrix T is used as a measurement of the change of loyalty influenced by the change of position. Actually, it is also an empirical parameter, we can get this parameter according to the performance of employees who get promoted.

<!-- b000675 | prose | pages [18] -->
iis a coefficient, which measures the relation between people’s salary and output. In the reality, it can be given by counting people’s effective output over the years.

<!-- b000676 | prose | pages [18] -->
is a coefficient, which indicates the degree of the loss of structure. Similarly, it is also an i empirical parameter. We can set its value by listening to the idea of experienced experts.  Parameters chosen by experiments In this part, we mainly take the parameters in GA into account. Actually, many papers have discussed the parameters in GA. The parameters in GA are the number of population (N), Iteration Times(K), mutation rate(MR) and crossover rate(CR)

<!-- b000677 | prose | pages [18] -->
Number of population ( N ) is the number of population. Generally, the value of N is usually 20~200[9]. In this paper, we use N  200 . Iteration Times( K ) decides whether can we get the optimal solution. If we iterate few times, we may not get the optimal solution. On the contrary, if we iterate many times, it is time-consuming. When we choose iteration times in GA, we can do some experiments to choose a better value. Taking section 5.1 as an example, in the second month, we can get the following graph:

<!-- b000678 | furniture | pages [18] -->


<!-- b000679 | furniture | pages [19] -->
Team #37284                                                                Page 18 of 20

<!-- b000680 | furniture | pages [19] -->


<!-- b000681 | caption | pages [19] -->
Figure 18: Iteration times to get the optimal solution

<!-- b000682 | furniture | pages [19] -->


<!-- b000683 | prose | pages [19] -->
K  1000 From the picture above, we think is a good point for GA to converge. We usually take twice, so we choose 2000 to be the value of K .

<!-- b000684 | prose | pages [19] -->
Mutation Rate( MR ) and Crossover Rate(CR ) also need to be determined by experiments. In our model, we fix one value at 0.1 and change another from 0 to 1. Then we can get the better MR and CR respectively according to the minimum iteration times.

<!-- b000685 | furniture | pages [19] -->


<!-- b000686 | caption | pages [19] -->
Figure 19: The fluctuate of mutation and crossover rate

<!-- b000687 | furniture | pages [19] -->


<!-- b000688 | prose | pages [19] -->
According to the picture, the minimum iteration times appear at the rate of 0.4 and 0.1 MR  CR  0.4 respectively. Hence, we choose , 0.1 0.1 in our Genetic Algorithm.

<!-- b000689 | heading | pages [19] -->
7. Team Science and Multi-layer Networks

<!-- b000690 | prose | pages [19] -->
In the decision process of HR manager, there are many influenced factors. In the above part, we have discussed the potential influence of loyalty and intimacy on the organization. However, we do not take information flow into account, which is an important part in the team science[1][2]. Sharing cognition is very important in team science, which can form the information flow and run among people to form an information network.

<!-- b000691 | prose | pages [19] -->
The criterion of HR decision is team performance. The study of team science is to improve the team performance. If the information flows among people run smoothly, it will improve the team performance. On the contrary, if something hinders the flow of information, it will reduce the performance. In addition, effective information flow can reduce the obstacle in compatibility decision and concerted action, which is equal to improve the interaction among members.

<!-- b000692 | prose | pages [19] -->
As we all know, the organizational culture is the soft power. It would not only raise the team productivity, but would also advance the staff’s loyalty and intimacy. Obviously, a good information flow will contribute to forming a healthy organizational culture.

<!-- b000693 | prose | pages [19] -->
In section 3.4, we have discussed the human capital network. Actually, the network has two layers. According to the reference[3], we know about the multi-layers network. Taking information network into account, we can get a new multi-layers network, which consists of information network, relationship network and position network.

<!-- b000694 | furniture | pages [19] -->


<!-- b000695 | furniture | pages [20] -->
Team #37284                                                                Page 19 of 20

<!-- b000696 | furniture | pages [20] -->


<!-- b000697 | caption | pages [20] -->
Figure 20: Multi-layers network

<!-- b000698 | prose | pages [20] -->
Instead of single-layer network, using this multi-layers network to analyze the human capital can be more comprehensive and reasonable.

<!-- b000699 | heading | pages [20] -->
8. Further Discussion

<!-- b000700 | prose | pages [20] -->
In reality, the structure of department in an organization has a significant impact on the analysis of managing human capital. Obviously, the individuals working in one department have more complex relationship, including both positive and negative relation. Considering the structure of department, we plan to do some further work:

<!-- b000701 | prose | pages [20] -->
 When setting the initial value of loyalty and intimacy, we should analyze whether they

<!-- b000702 | prose | pages [20] -->
are in one department. On the other hand, we should consider the influence of the leadership of department.  In the dynamic process of human capital network, we should also consider the

<!-- b000703 | prose | pages [20] -->
adjustment from one department to another department, which are in the same level. Although the adjustment does not change the position level, but the adjustment on department will influence people’s intimacy.  Consider the organizational structure, we should take all department into account. in

<!-- b000704 | prose | pages [20] -->
general, there are proper number of people in all departments that will bring maximum productivity because each department performs its own functions.

<!-- b000705 | heading | pages [20] -->
9. Strengths and Weaknesses

<!-- b000706 | heading | pages [20] -->
9.1 Strengths

<!-- b000707 | prose | pages [20] -->
1. We use three graphs to represent the relationship between staff and positions, and use time stamp to simulate the dynamic process. In addition, we combine computer simulation, HR adjustment (Using GA) and Transformation Matrix to our model to analyze the dynamic process of human capital network. 2. We set the loyalty and intimacy to identify the churn caused by people’s own relation or influenced by others. More specifically, we associate the change of loyalty and intimacy with the change of position. Then, we use the computer to simulate the churn of staff, which provides us an intuitive process. 3. Genetic Algorithm is an efficient way to get an approximate optional solution, which is used by us to assign the position to the employee. Since we do not take firing people and degrading into consideration, we modified the GA to better fit our model. 4. When discussing the cost, we divide it into two parts: the direct cost and the indirect cost.

<!-- b000708 | prose | pages [20] -->
The direct cost is related to the number of employees and their levels. The indirect cost is related to the organizational structure.

<!-- b000709 | heading | pages [20] -->
9.2 Weaknesses

<!-- b000710 | prose | pages [20] -->
1. Due to the lacking of data, some values are based on the assumption we made. It may be different from the reality. 2. Because the organizational graph does not coordinate with the structure table, so we just use the structure table. We should also take organizational graph into account.

<!-- b000711 | furniture | pages [20] -->


<!-- b000712 | furniture | pages [21] -->
Team #37284                                                                Page 20 of 20

<!-- b000713 | prose | pages [21] -->
Reference

<!-- b000714 | prose | pages [21] -->
[1] E. Salas, N.J. Cooke, and M.A. Rosen. (2008). On Teams, Teamwork, and Team Performance:

<!-- b000715 | prose | pages [21] -->
Discoveries and Developments. Human Factors: The Journal of the Human Factors and

<!-- b000716 | prose | pages [21] -->
Ergonomics Society June 2008 vol. 50 no. 3 540-547.

<!-- b000717 | prose | pages [21] -->
[2] D. Stokols, K.L. Hall, B.K. Taylor, R.P. Moser (2008). The Science of Team Science: Overview of

<!-- b000718 | prose | pages [21] -->
the Field and Introduction to the Supplement, Am J Prev Med 2008;35(2S): S77-S89

<!-- b000719 | prose | pages [21] -->
[3] Mikko Kivelä, Alexandre Arenas, Marc Barthelemy, James P. Gleeson, Yamir Moreno, Mason A.

<!-- b000720 | prose | pages [21] -->
Porter. (2013). Multilayer Networks, J. Complex Networks, 2(3):203-271 (2014); arXiv preprint

<!-- b000721 | prose | pages [21] -->
arXiv:1309.7233, 2013

<!-- b000722 | prose | pages [21] -->
[4] Bipartite graph Wikipedia http://en.wikipedia.org/wiki/Bipartite_graph 7 February 2015

<!-- b000723 | prose | pages [21] -->
[5] Giles R. The Strong Perfect Graph Theorem for a Class of Partitionable Graphs[J].

<!-- b000724 | prose | pages [21] -->
North-Holland Mathematics Studies, 1984:161–167.

<!-- b000725 | prose | pages [21] -->
[6] Genetic algorithm https://en.wikipedia.org/wiki/Genetic_algorithm 8 February 2015

<!-- b000726 | prose | pages [21] -->
[7] Goldberg D E. The design of innovation: Lessons from and for competent genetic algorithms[J].

<!-- b000727 | prose | pages [21] -->
JASSS-THE JOURNAL OF ARTIFICIAL SOCIETIES AND SOCIAL SIMULATION, 2005, 8(3).

<!-- b000728 | prose | pages [21] -->
[8] Bies R R, Muldoon M F, Pollock B G, et al. A Genetic Algorithm-Based, Hybrid Machine

<!-- b000729 | prose | pages [21] -->
Learning Approach to Model Selection[J].

<!-- b000730 | prose | pages [21] -->
Journal of Pharmacokinetics and

<!-- b000731 | prose | pages [21] -->
Pharmacodynamics, 2006, 33(2):195-221. [9] Wang Xiaohua, Yang Na. The parameter optimization estimation model based on genetic

<!-- b000732 | prose | pages [21] -->
algorithm[J]. Electronic World, 2012, (24):118-119.

<!-- b000733 | furniture | pages [21] -->

